from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
import time


def get_scheduler(blocking=False):
    scheduler = None
    if blocking:
        scheduler = BlockingScheduler()
    else:
        scheduler = BackgroundScheduler()
    return scheduler


if __name__ == "__main__":
    def job1():
        print("job1")

    scheduler = get_scheduler(blocking=True)
    scheduler.add_job(job1, "interval", seconds=1)

    @scheduler.scheduled_job("cron", second="0/3", hour="*")
    def job2():
        print("job2")

    scheduler.start()
