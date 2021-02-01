import os
import datetime




def alert(message, debug_flag=False):
    if debug_flag == True:
        destination = ["https://hooks.slack.com/services/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", "https://hooks.slack.com/services/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"] # logs channel
    elif debug_flag == False:
        destination = ["https://hooks.slack.com/services/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"] # covid-vaccine-general channel
    for dest in destination:
        curl = """curl -X POST -H 'Content-type: application/json' --data '{"text":"%s"}' %s""" % (
            message, dest)
        os.popen(curl)


def log(message):
    now = datetime.datetime.now()
    stamp = now.strftime("%m/%d/%Y,%H:%M,")
    with open("log.txt", "a") as file:
        line = stamp + message + "\n"
        file.write(line)
        curl = """curl -X POST -H 'Content-type: application/json' --data '{"text":"%s"}' https://hooks.slack.com/services/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""" % (
            line)
        os.popen(curl)
        file.close()
