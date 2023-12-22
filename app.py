
import subprocess

def run():
    
    cl = subprocess.Popen(["python","client.py"])
    sr = subprocess.Popen(["python","server.py"])
    sr.wait()
    #sr.send_signal()
    cl.wait()

if __name__ == "__main__":
    run()