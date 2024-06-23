from configs.settings import settings

async def logFile():
    with open(settings.LOG_FILEPATH, "r") as file:
        contents = file.read()
        return contents