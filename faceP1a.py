import cv2
import timeit
import datetime
#p1a

#cascPath = sys.argv[1]
#cascPath = "./face.xml"
#cascPath = "./haarcascade_eye.xml"
faceCascade = cv2.CascadeClassifier("./face.xml")
eyeCascade = cv2.CascadeClassifier("./haarcascade_eye.xml")
#smileCascade = cv2.CascadeClassifier("./Nariz.xml")
noseCascade = cv2.CascadeClassifier("./Nariz.xml")

video_capture = cv2.VideoCapture(-1)
t = datetime.datetime.today()

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    eyes = eyeCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    nose = noseCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        a = 0
        b = 0
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #print "x=",x," y=",y," w=",w,"h= ",h,
        #roi_NB = frame[y:y + h, x:x + w]
        #roi_eye = frame[y:y + h, x:x + w]
        for (ex, ey, ew, eh) in eyes:
            a += 1
            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (12, 64, 0), 2)
            #print "ex=", ex ," ey=", ey ," ew=", ew ,"eh= ", eh , b'\x08',
        for (nx, ny, nw, nh) in nose:
            b += 1
            cv2.rectangle(frame, (nx, ny), (nx + nw, ny + nh), (255, 0, 0), 2)
            #print "nx=",nx," ny=",ny," nw=",nw,"nh= ",nh ,
            #print a, b
            if ((a == 2) and (b == 1 and (((x<ex) and (y <ey)) and ((x + w) > (ex + ew)) and ((y + h) > (ey + eh))) and (((x < nx) and (y < ny)) and ((x + w) > (nx + nw)) and ((y + h) > (ny + nh))))):
                print "LOL "+str(t.hour)+str(t.minute)+"\a",
                cv2.imwrite("./LOL2/image"+str(t.hour)+str(t.minute)+"&"+str(timeit.timeit())+".jpg", frame)
            elif (a == 4 and b == 1 and (((x<ex) and (y <ey)) and ((x + w) > (ex + ew)) and ((y + h) > (ey + eh))) and (((x < nx) and (y < ny)) and ((x + w) > (nx + nw)) and ((y + h) > (ny + nh)))):
                print "LoLol "+str(t.hour)+str(t.minute)+"\a",
                cv2.imwrite("./LOL4/image"+str(t.hour)+str(t.minute)+"&"+str(timeit.timeit())+".jpg", frame)
            #faces.
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) == ord('1'):
        video_capture.release()
        video_capture = cv2.VideoCapture(0)
    elif cv2.waitKey(1) == ord('2'):
        video_capture.release()
        video_capture = cv2.VideoCapture(1)


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()