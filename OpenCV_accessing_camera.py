import cv2

def main():
    capture = cv2.VideoCapture(0)   #open default camera at o index 

    if not capture.isOpened():
        print("Error: occured camera not opened!!")
        return

    while True:
        returning,frame = capture.read()    #returning frame by frame

        if not returning:
            print("Error: Frame not returning!!")
            break

        mirror_fr = cv2.flip(frame,1)   #flip the camera horizontally 

        cv2.imshow('Camera',mirror_fr)   #display camera 

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
