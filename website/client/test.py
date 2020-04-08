from client import Client
import time
from threading import Thread

c1 = Client("Uday")
c2 = Client("Aman")


def update_messages():
    """
    updates the local list of messages
    :return: None
    """
    msgs = []
    run = True
    while run:
        time.sleep(0.1)  # update every 1/10th of a second
        new_messages = c1.get_messages()  # get any new messages from client
        msgs.extend(new_messages)  # add to local list of messages
        for msg in new_messages:  # display new messages
            print(msg)
            if msg == "{quit}":
                run = False
                break


Thread(target=update_messages).start()

c1.send_message("Hello mote")
time.sleep(1)
c2.send_message("whats up")
time.sleep(1)
c1.send_message("mota mental")
time.sleep(1)
c2.send_message("haha")
time.sleep(3)
c1.disconnect()
time.sleep(2)
c2.disconnect()
