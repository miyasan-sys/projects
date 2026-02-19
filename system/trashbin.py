import datetime
import pathlib

def duration(source, limit): # the duration
    folder = pathlib.Path(source)
    
    if not folder.exists():
        print("Folder not found!")
        return 0

    ngayon = datetime.datetime.now()
    timer = ngayon - datetime.timedelta(minutes=limit)
    count = 0

    for screenshots in folder.iterdir(): # check if the file is expired or not
        if screenshots.is_file():
            ftime = datetime.datetime.fromtimestamp(screenshots.stat().st_mtime)
            
            if ftime < timer:
                screenshots.unlink
                print("Deleted: " + screenshots.name)
                count += 1
        else:
            print("Skipped directory: " + screenshots.name)
            
    return count

duration("/home/miyasan/Pictures/Screenshots", 10)
        