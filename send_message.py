from notify_run import Notify
import datetime

#notify = Notify()
#notify.send('any message you want')


def startMessage():
    time = datetime.datetime.now()
    notify = Notify()
    message = "Starting new scrape, time: " + time.strftime("%X")
    notify.send(message)


def endMessage(time):
    notify = Notify()
    message = "Scrape finished, time taken: " + time
    notify.send(message)

def errorMessage():
    notify = Notify()
    notify.send("An error occureed during runtime, scrape failed")
