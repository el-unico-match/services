async def logFile():
    with open('log', "r") as file:
        contents = file.read()
        return contents