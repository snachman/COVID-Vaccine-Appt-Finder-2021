import os
import datetime




def alert(message, channel):

    main_channel = "https://hooks.slack.com/services/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"
    maryland_channel = "https://hooks.slack.com/services/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"
    high_confidence_channel = "https://hooks.slack.com/services/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"
    personal_channel = "https://hooks.slack.com/services/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"
    new_jersey_channel = "https://hooks.slack.com/services/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"
    ohio_channel = "https://hooks.slack.com/services/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"
    delaware_channel = "https://hooks.slack.com/services/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"
    florida_channel = "https://hooks.slack.com/services/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"

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
    now = datetime.datetime.utcnow()+datetime.timedelta(hours=-5)
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