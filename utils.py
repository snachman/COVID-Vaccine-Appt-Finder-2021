import os
import datetime




def alert(message, channel):

    main_channel = "https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXX/REDACTED"
    maryland_channel = "https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXX/REDACTED"
    high_confidence_channel = "https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXX/REDACTED"
    personal_channel = "https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXX/REDACTED"
    new_jersey_channel = "https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXX/REDACTED"
    ohio_channel = "https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXX/REDACTED"
    delaware_channel = "https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXX/REDACTED"
    florida_channel = "https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXX/REDACTED"

    if channel.lower() == "maryland":
        destination = [maryland_channel]
    elif channel.lower() == "personal" or channel.lower() == "debug":
        destination = [personal_channel]
    elif channel.lower() == "new jersey":
        destination = [new_jersey_channel]
    elif channel.lower() == "delaware":
        destination = [delaware_channel]
    elif channel.lower() == "ohio":
        destination = [ohio_channel]
    elif channel.lower() == "florida":
        destination = [florida_channel]
    else:
        destination = [personal_channel]

    for dest in destination:
        curl = """curl -X POST -H 'Content-type: application/json' --data '{"text":"%s"}' %s""" % (
            message, dest)
        os.popen(curl)


def log(message):
    message = message.replace("\n", " ")
    now = datetime.datetime.utcnow()+datetime.timedelta(hours=-4)
    stamp = now.strftime("%m/%d/%Y,%H:%M,")
    with open("log.txt", "a") as file:
        line = stamp + message + "\n"
        file.write(line)
        curl = """curl -X POST -H 'Content-type: application/json' --data '{"text":"%s"}' https://hooks.slack.com/services/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""" % (
            line)
        os.popen(curl)
        file.close()


def write_to_scratchpad(message):
    with open('scratchpad.txt', 'a') as file:
        file.write("\n----------" + message + "\n\n")
        file.close()