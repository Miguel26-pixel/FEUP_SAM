
def init():
    global appRunning
    appRunning = False

    global savingFile
    savingFile = False

    global readingFile
    readingFile = False

    global readingPaused
    readingPaused = False

    global stopReading
    stopReading = False

    global filePath
    filePath = ""

    global sentenceIndex
    sentenceIndex = 0

    global voiceId
    voiceId = 0

    global temp_dir
    temp_dir = ""

    global temp_wav_path
    temp_wav_path = ""
