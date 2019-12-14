import ctypes

ctypes.windll.winmm.mciSendStringW("set cdaudio door open",None, 0, None)
