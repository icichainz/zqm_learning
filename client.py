#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import asyncio

context = zmq.Context()

async def run_client(id:int)->None:
    #  Socket to talk to server
   
    print("Connecting to hello world server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    #  Do 10 requests, waiting each time for a response
    for request in range(100):
        print(f"client id {id}")
        print("Sending request %s …" % request)
        socket.send(b"Every body")

        #  Get the reply.
        message = socket.recv()
        
        print("Received reply %s [ %s ]" % (request, message))
        
    socket.close()
    
async def main():
    tasks = [
        
        asyncio.create_task(run_client(1)),
        asyncio.create_task(run_client(2)),
        asyncio.create_task(run_client(3)),
        asyncio.create_task(run_client(4)),
        asyncio.create_task(run_client(5))
    ]
    
    await asyncio.gather(*tasks)
    

if __name__ == "__main__":
    asyncio.run(main())
  