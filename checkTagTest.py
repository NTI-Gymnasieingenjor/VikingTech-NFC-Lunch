import json
import checkTag

tagFile = open("tags.json")
# Creates a dictionary that contains all the tags and the connected class,
# to be able to search for specific tags
fileData: dict = json.load(tagFile)

tagList = ["67523475", "876348574", "952224470", "7978497850", "537059654", "536961030"]

for tag in tagList:
    tagCheck = checkTag.CheckTag()
    tagCheck.start(tag=tag)
