import reapy
import time

project = reapy.Project()
project.add_track(name="Test Track")

tracks = project.tracks

current_track = tracks[0]

current_track.recarm_change(1)
current_track.set_info_value("I_RECINPUT", 1) # 0 based index

project.current_surface_record()
time.sleep(5)
project.current_surface_stop()