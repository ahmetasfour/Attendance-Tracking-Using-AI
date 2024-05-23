from flask import Flask, render_template, request, session, redirect, url_for, Response, jsonify,render_template, request, redirect, url_for, session
import mysql.connector
import time
from datetime import date
import cv2
import os
import numpy as np
from PIL import Image
from flask import Flask, render_template, request


app = Flask(__name__)

cnt = 0
pause_cnt = 0
justscanned = False

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="flask_db"
)
mycursor = mydb.cursor()


# MySQL Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "passwd": "",
    "database": "flask_db",
}

def generate_dataset(nbr):
    face_classifier = cv2.CascadeClassifier(
        "/Users/ahmed777/p2/resources/haarcascade_frontalface_default.xml")

    def face_cropped(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 7)
        # Görüntüde tespit edilen yüzlerin etrafına dikdörtgen oluşturmak için kullanılır.
        # Parametreler:
        # scaleFactor: Görüntünün boyutunu
        # ayarlamak için kullanılır.
        # minNeighbors: Bir kişinin
        # kaç komşusu olabileceğini belirtir.

        # scaling factor=1.3
        # Minimum neighbor = 7

        if faces is ():
            return None
        for (x, y, w, h) in faces:
            cropped_face = img[y:y + h, x:x + w]
        return cropped_face

    cap = cv2.VideoCapture(0)

    mycursor.execute("select ifnull(max(img_id), 0) from img_dataset")
    row = mycursor.fetchone()
    lastid = row[0]

    img_id = lastid
    max_imgid = img_id + 100
    count_img = 0

    while True:
        ret, img = cap.read()
        if face_cropped(img) is not None:
            count_img += 1
            img_id += 1
            face = cv2.resize(face_cropped(img), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            file_name_path = "dataset/" + nbr + "." + str(img_id) + ".jpg"
            cv2.imwrite(file_name_path, face)
            cv2.putText(face, str(count_img), (75, 75), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)

            mycursor.execute("""INSERT INTO `img_dataset` (`img_id`, `img_person`) VALUES
                                ('{}', '{}')""".format(img_id, nbr))
            mydb.commit()

            frame = cv2.imencode('.jpg', face)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

            if cv2.waitKey(1) == 13 or int(img_id) == int(max_imgid):
                break
                cap.release()
                cv2.destroyAllWindows()

#yuz tanıma:

@app.route('/train_classifier/<nbr>')
def train_classifier(nbr):
    dataset_dir = "/Users/ahmed777/p2/dataset"

    path = [os.path.join(dataset_dir, f) for f in os.listdir(dataset_dir) if f.endswith(('.jpg', '.png'))]

    faces = []
    ids = []

    for image in path:
        try:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
        except Exception as e:
            print(f"Error processing image {image}: {e}")

    ids = np.array(ids)

    # Train the classifier and save
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.write("classifier.xml")

    return redirect('/')


def face_recognition():  # generate frame by frame from camera
    def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        global justscanned
        global pause_cnt

        pause_cnt += 1

        coords = []

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            id, pred = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int(100 * (1 - pred / 300))

            if confidence > 70 and not justscanned:
                global cnt
                cnt += 1

                n = (100 / 30) * cnt
                # w_filled = (n / 100) * w
                w_filled = (cnt / 30) * w

                cv2.putText(img, str(int(n)) + ' %', (x + 20, y + h + 28), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                            (0, 122, 98), 2, cv2.LINE_AA)

                cv2.rectangle(img, (x, y + h + 40), (x + w, y + h + 50), color, 2)
                cv2.rectangle(img, (x, y + h + 40), (x + int(w_filled), y + h + 50), (0, 255, 0), cv2.FILLED)

                mycursor.execute("select a.img_person, b.std_name, b.std_lesson "
                                 "  from img_dataset a "
                                 "  left join std_mnst b on a.img_person = b.std_nbr "
                                 " where img_id = " + str(id))
                row = mycursor.fetchone()
                pnbr = row[0]
                pname = row[1]
                plesson = row[2]

                if int(cnt) == 30:
                    cnt = 0

                    # mycursor2 = mydb.cursor()
                    # mycursor2.execute(
                    #     f"select * from accs_hist where UNIX_TIMESTAMP(accs_added) - {int(time.time())} < 86400")
                    # r = mycursor2.fetchone()
                    # if(not r):

                    mycursor.execute("insert into accs_hist (accs_date, accs_student) values('" + str(
                        date.today()) + "', '" + pnbr + "')")
                    mydb.commit()

                    cv2.putText(img, pname + ' | ' + plesson, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                                (255, 255, 153), 2, cv2.LINE_AA)
                    time.sleep(1)

                    justscanned = True
                    pause_cnt = 0

            else:
                if not justscanned:
                    cv2.putText(img, 'UNKNOWN', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
                else:
                    cv2.putText(img, ' ', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)

                if pause_cnt > 80:
                    justscanned = False

            coords = [x, y, w, h]
        return coords

    def recognize(img, clf, faceCascade):
        coords = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
        return img

    faceCascade = cv2.CascadeClassifier(
        "/Users/ahmed777/p2/resources/haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    wCam, hCam = 400, 400

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    while True:
        ret, img = cap.read()
        img = recognize(img, clf, faceCascade)

        frame = cv2.imencode('.jpg', img)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        key = cv2.waitKey(1)
        if key == 27:
            break


@app.route('/')
def home():
    mycursor.execute("select std_nbr, std_name, std_lesson, std_active, std_added from std_mnst")
    data = mycursor.fetchall()

    return render_template('index.html', data=data)

@app.route('/addprsn')
def addprsn():
    mycursor.execute("select ifnull(max(std_nbr) + 1, 101) from std_mnst")
    row = mycursor.fetchone()
    nbr = row[0]
    print(int(nbr))

    return render_template('addprsn.html', newnbr=int(nbr))


@app.route('/addprsn_submit', methods=['POST'])
def addprsn_submit():
    prsnbr = request.form.get('txtnbr')
    prsname = request.form.get('txtname')
    prslesson = request.form.get('optlesson')

    mycursor.execute("""INSERT INTO `std_mnst` (`std_nbr`, `std_name`, `std_lesson`) VALUES
                    ('{}', '{}', '{}')""".format(prsnbr, prsname, prslesson))
    mydb.commit()
    # return redirect(url_for('home'))
    return redirect(url_for('vfdataset_page', prs=prsnbr))


@app.route('/vfdataset_page/<prs>')
def vfdataset_page(prs):
    return render_template('gendataset.html', prs=prs)


@app.route('/vidfeed_dataset/<nbr>')
def vidfeed_dataset(nbr):
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(generate_dataset(nbr), mimetype='multipart/x-mixed-replace; boundary=frame')

# ==========================

@app.route('/video_feed')
def video_feed():
    return Response(face_recognition(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/r_page', methods=['GET'])
def r_page():
    try:
        mydb = mysql.connector.connect(**db_config)
        mycursor = mydb.cursor()

        search = request.args.get('search')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        # query = "SELECT a.*, b.std_name, b.std_lesson " \
        #         "FROM accs_hist a " \
        #         "JOIN std_mnst b ON a.accs_student = b.std_nbr  "

        query = "SELECT a.*, b.std_name, b.std_lesson, " \
                "(SELECT COUNT(*) FROM accs_hist WHERE accs_date <= a.accs_date AND accs_student = a.accs_student) AS count_col " \
                "FROM accs_hist a " \
                "JOIN std_mnst b ON a.accs_student = b.std_nbr"
        # Adding conditions based on search parameters
        conditions = []
        if search:
            conditions.append(f"b.std_name LIKE '%{search}%'")
        if start_date:
            conditions.append(f"a.accs_date >= '{start_date}'")
        if end_date:
            conditions.append(f"a.accs_date <= '{end_date}'")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " ORDER BY a.accs_id DESC"

        mycursor.execute(query)
        data = mycursor.fetchall()

        mycursor.close()
        mydb.close()

        return render_template('r_page.html', data=data)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error connecting to the database"


@app.route('/fr_page')
def fr_page():
    """Video streaming home page."""
    mycursor.execute("select a.accs_id, a.accs_student, b.std_name, b.std_lesson, a.accs_added "
                     "  from accs_hist a "
                     "  left join std_mnst b on a.accs_student = b.std_nbr "
                     " where a.accs_date = curdate() "
                     " order by 1 desc")
    data = mycursor.fetchall()

    return render_template('fr_page.html', data=data)


@app.route('/countTodayScan')
def countTodayScan():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="flask_db"
    )
    mycursor = mydb.cursor()

    mycursor.execute("select count(*) "
                     "  from accs_hist "
                     " where accs_date = curdate() ")
    row = mycursor.fetchone()
    rowcount = row[0]

    return jsonify({'rowcount': rowcount})


@app.route('/loadData', methods=['GET', 'POST'])
def loadData():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="flask_db"
    )
    mycursor = mydb.cursor()

    mycursor.execute(
        "select a.accs_id, a.accs_student, b.std_name, b.std_lesson, date_format(a.accs_added, '%H:%i:%s') "
        "  from accs_hist a "
        "  left join std_mnst b on a.accs_student = b.std_nbr "
        " where a.accs_date = curdate() "
        " order by 1 desc")
    data = mycursor.fetchall()

    return jsonify(response=data)




if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)