import os
import subprocess
import threading
import time
import webview

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def iniciar_django():

    proyecto = os.path.abspath(
        os.path.join(BASE_DIR, "..")
    )

    subprocess.Popen(
        ["python", "manage.py", "runserver", "127.0.0.1:8000"],
        cwd=proyecto
    )

threading.Thread(
    target=iniciar_django,
    daemon=True
).start()

time.sleep(8)

webview.create_window(
    "Mantención ANAM",
    "http://127.0.0.1:8000",
    width=1400,
    height=900
)

webview.start()