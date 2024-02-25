import cv2

def takePhoto():

    video_capture = cv2.VideoCapture(0)
    name = input('Enter you name: ')

    while True:
        ret, frame = video_capture.read()

        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite(str(name) + ".jpg", frame)
            cv2.waitKey(2000)
            break

        

    video_capture.release() 

    cv2.destroyAllWindows() 