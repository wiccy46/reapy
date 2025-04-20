import reapy
import time

project = reapy.Project()
project.add_track(name="Test Track")

tracks = project.tracks

current_track = tracks[0]

current_track.add_fx("ReaQE")