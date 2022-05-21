from executer.receiver import Receiver
#from executer.face_recon import FaceRecognizer 
import multiprocessing as mp
import webInterface.interface as web

rcv = Receiver
#fr = FaceRecognizer

def main():
    web.flaskThread.start()
    rcv.listener().start()
    #fr.start()
    
    web.flaskThread.join()
    rcv.join()
    #fr.start()
    
if __name__ == "__main__":
    main()
    
    
    