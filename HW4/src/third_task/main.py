import multiprocessing
import time
import codecs
from datetime import datetime


def process_a(child_conn_ma, queue_ba):
    while True:
        message = child_conn_ma.recv()
        if message == "STOP":
            break
        message_lower = message.lower()
        queue_ba.put(message_lower)
        time.sleep(5)


def process_b(queue_ba, conn_mb):
    while True:
        message_lower = queue_ba.get()
        if message_lower == "STOP":
            break
        encoded_message = codecs.encode(message_lower, 'rot_13')
        conn_mb.send((datetime.now(), encoded_message))


def main():
    queue_ba = multiprocessing.Queue()
    parent_conn_ma, child_conn_ma = multiprocessing.Pipe()
    parent_conn_mb, child_conn_mb = multiprocessing.Pipe()

    log_file_name = "../../artifacts/4.3/interaction_log.txt"

    process_a_instance = multiprocessing.Process(target=process_a, args=(child_conn_ma, queue_ba))
    process_b_instance = multiprocessing.Process(target=process_b, args=(queue_ba, child_conn_mb))

    process_a_instance.start()
    process_b_instance.start()

    try:
        while True:
            message = input("Enter a message to send to process A: ")
            log_message = f"[{datetime.now()}] User input: {message}\n"
            with open(log_file_name, "a") as f:
                f.write(log_message)

            if message == "STOP":
                break
            parent_conn_ma.send(message)

            if parent_conn_mb.poll():
                timestamp, encoded_message = parent_conn_mb.recv()
                log_message = f"[{timestamp}] Encoded message from process B: {encoded_message}\n"
                print(log_message)

                with open(log_file_name, "a") as f:
                    f.write(log_message)

    except KeyboardInterrupt:
        pass
    finally:
        parent_conn_ma.send("STOP")
        queue_ba.put("STOP")
        process_a_instance.join()
        process_b_instance.join()

        parent_conn_mb.close()
        child_conn_mb.close()


if __name__ == "__main__":
    main()
