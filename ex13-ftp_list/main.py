import requests
from bs4 import BeautifulSoup
import ftplib
from queue import Queue
from threading import Thread
from urllib.parse import urlparse


class WorkerThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the next FTP site from the queue
            url = self.queue.get()
            parsed_url = urlparse(url)
            hostname = parsed_url.hostname
            print(hostname)

            try:
                ftp = ftplib.FTP(hostname)
                ftp.login("anonymous", "")
                files = ftp.nlst()
                for file in files:
                    print(f"File: {file}")
                ftp.quit()

            except ftplib.all_errors as e:
                print(f"Error connecting to {hostname}: {str(e)}")

            finally:
                self.queue.task_done()


url = "https://launchpad.net/ubuntu/+cdmirrors"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

ftp_list = [a["href"] for a in soup.find_all("a", href=lambda href: href and href.startswith("ftp://"))]

queue = Queue()

for ftp_site in ftp_list[:20]:
    queue.put(ftp_site)

for _ in range(3):
    worker = WorkerThread(queue)
    worker.start()

queue.join()
