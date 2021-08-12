import pathlib
import subprocess
from typing import Optional

class Playa:
    def __init__ (self, music_file: pathlib.Path):
        self.music_file = music_file
        self.started = False
        self.stopped = False
        self.subprocess: Optional [subprocess.Popen] = None
    def start (self):
        self.subprocess = subprocess.Popen (f"ffmpeg -i '{self.music_file}' -map 0:a -c copy -f matroska - | ffplay -f matroska -", shell = True) # drops all other streams that aren't the first audio track
        self.started = True
    def stop (self):
        assert self.started
        if self.stopped: return
        self.subprocess.kill ()
        self.stopped = True
    def wait_for_end (self):
        assert self.started
        if self.stopped: return
        self.subprocess.wait ()
        self.stopped = True
    def __enter__ (self, *args): self.start ()
    def __exit__ (self, *args): self.wait_for_end ()