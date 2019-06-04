from apscheduler.schedulers.background import BackgroundScheduler
import time


def job1():
    print("11111")


scheduler = BackgroundScheduler()
scheduler.add_job(job1, "interval", seconds=1)

scheduler.start()

while True:
    time.sleep(10)
