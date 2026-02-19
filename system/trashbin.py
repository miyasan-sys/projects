import datetime
import pathlib


def duration(source, limit): # the duration
    folder = pathlib.Path(source)
    ngayon = datetime.datetime.now()
    timer = ngayon - datetime.timedelta(minutes=limit)
    count = 0

    for screenshots in folder.iterdir(): #check if the file is expired or not
        if screenshots.is_file():
            ftime = datetime.datetime.fromtimestamp(screenshots.stat().st_mtime)
            if ftime < timer:
                print("rm " + screenshots.name)
                count += 1
        else:
            print("no directories")
    return count

duration("/home/miyasan/Pictures/Screenshots", 10)


        