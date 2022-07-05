import os


def create(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)


def move(foldername, filelist, map):
    for file in filelist:
        os.replace(file, f"{foldername}/{file}")
        map[foldername] += 1


if __name__ == "__main__":

    allfiles = os.listdir()
    allfiles.remove("organizer.py")

    create("Images")
    create("Docs")
    create("Videos")
    create("Coding Files")
    create("Others")

    imgexts = [".jpg", ".png", ".jpeg"]
    docexts = [".doc", ".docx", ".pdf", ".txt"]
    videxts = [".avi", ".mkv", ".mp4", ".wav", ".mov", ".mpeg-4"]
    codexts = [".c", ".cpp", ".java", ".js", ".php"]

    images = [file for file in allfiles if os.path.splitext(file)[1].lower() in imgexts]
    docs = [file for file in allfiles if os.path.splitext(file)[1].lower() in docexts]
    media = [file for file in allfiles if os.path.splitext(file)[1].lower() in videxts]
    codes = [file for file in allfiles if os.path.splitext(file)[1].lower() in codexts]
    others = [
        file
        for file in allfiles
        if (os.path.splitext(file)[1].lower() not in imgexts)
        and (os.path.splitext(file)[1].lower() not in docexts)
        and (os.path.splitext(file)[1].lower() not in videxts)
        and (os.path.splitext(file)[1].lower() not in codexts)
        and os.path.isfile(file)
    ]
    map = {"Images": 0, "Docs": 0, "Videos": 0, "Coding Files": 0, "Others": 0}
    move("Images", images, map)
    move("Docs", docs, map)
    move("Videos", media, map)
    move("Coding Files", codes, map)
    move("Others", others, map)
    print(f"Directory Organized.", len(map), "folders created.")
    for i in map:
        if map.get(i) != 0:
            print("->", map.get(i), "files to", i)
