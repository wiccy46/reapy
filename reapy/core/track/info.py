class TrackSendInfo():
    """
    Enum for track send info, option in the routing dialog.
    https://www.reaper.fm/sdk/reascript/reascripthelp.html#SetTrackSendInfo_Value
    """
    IS_MUTED = "B_MUTE"
    IS_PHASE_INVERTED = "B_PHASE"
    IS_MONO = "B_MONO"
    VOLUME = "D_VOL" # 1.0 = +0dB etc
    PANNING = "D_PAN" # -1.0..+1.0
    PAN_LAW = "D_PANLAW" # 1.0=+0.0db, 0.5=-6dB, -1.0 = projdef etc
    SEND_MODE = "I_SENDMODE" # 0=post-fader, 1=pre-fx, 2=post-fx (deprecated), 3=post-fx
    AUTO_MODE = "I_AUTOMODE" # automation mode (-1=use track automode, 0=trim/off, 1=read, 2=touch, 3=write, 4=latch)
    SOURCE_CHANNEL = "I_SRCCHAN" # Source channel index,&1024=mono, -1 for none
    DESTINATION_CHANNEL = "" # Destination channel index, &1024=mono, otherwise stereo pair, hwout:&512=rearoute
    MIDI_FLAG = "I_MIDIFLAGS" # low 5 bits=source channel 0=all, 1-16, next 5 bits=dest channel, 0=orig, 1-16=chan


class MediaInfo():
    """
    A more human-readable enum options for media item info.
    https://www.reaper.fm/sdk/reascript/reascripthelp.html#GetMediaItemInfo_Value
    """
    IS_MUTED = "B_MUTE"
    IS_PHASE_INVERTED = "B_PHASE"
    HAS_RECORD_MONITORING = "B_RECMON_IN_EFFECT"
    TRACK_NUMBER = "IP_TRACKNUMBER" # 1 base
    IS_SOLOED = "I_SOLO"
    IS_SOLO_DEFEAT = "B_SOLO_DEFEAT" # When set if anything else is soloed and this track is not mute, this track acts soloed
    IS_FX_ENABLED = "I_FXEN"
    IS_REC_ARMED = "I_RECARM"
    REC_INPUT = "I_RECINPUT" # record input, <0=no input. if 4096 set, input is MIDI and low 5 bits represent channel (0=all, 1-16=only chan), next 6 bits represent physical input (63=all, 62=VKB). If 4096 is not set, low 10 bits (0..1023) are input start channel (ReaRoute/Loopback start at 512). If 2048 is set, input is multichannel input (using track channel count), or if 1024 is set, input is stereo input, otherwise input is mono.
    REC_MODE = "I_RECMODE" 
    REC_MONITORING = "I_RECMON"
    REC_MONITOR_ITEMS = "I_RECMONITEMS"
    IS_RECARM_ON_SELECTED = "B_AUTO_RECARM"
    TRACK_VU_MODE = "I_VUMODE" # &1:disabled, &30==0:stereo peaks, &30==2:multichannel peaks, &30==4:stereo RMS, &30==8:combined RMS, &30==12:LUFS-M, &30==16:LUFS-S (readout=max), &30==20:LUFS-S (readout=current), &32:LUFS calculation on channels 1+2 only
    TRACK_AUTOMATION_MODE = "I_AUTOMODE" # 0=trim/off, 1=read, 2=touch, 3=write, 4=latch
    TRACK_CHANNELS = "I_NCHAN"
    IS_SELECTED = "I_SELECTED"
    TCP_WIN_HEIGHT_INCL_ENVELOPES = "I_WNDH" # Current TCP window height in pixels incl envelopes (Read only)
    TCP_WIN_HEIGHT = "I_TCPH" # Current TCP window height not incl envelopes (Read only)
    MCP_X = "I_MCPX" # MCP X position in pixels relative to mixer container (Read only)
    MCP_Y = "I_MCPY" # MCP Y position in pixels relative to mixer container (Read only)
    MCP_WIDTH = "I_MCPW" # MCP width in pixels (Read only)
    MCP_HEIGHT = "I_MCPH" # MCP height in pixels (Read only)
    FOLDER_DEPTH = "I_FOLDERDEPTH" # Folder depth change, 0=normal, 1=track is a folder parent, -1=track is the last in the innermost folder, -2=track is the last in the innermost and next-innermost folders, etc
    FOLDER_COMPACTED_STATE = "I_FOLDERCOMPACT" # Folder compacted state (only valid on folders), 0=normal, 1=small, 2=tiny children
    TRACK_MIDI_HW_OUTPUT_IDX = "I_MIDIHWOUT" # Track midi hardware output index, <0=disabled, low 5 bits are which channels (0=all, 1-16), next 5 bits are output device index (0-31)
    TRACK_PERFORMANCE_FLAG = "I_PERFFLAGS" # Track performance flags, &1=no media buffering, &2=no anticipative FX
    CUSTOM_COLOR = "I_CUSTOMCOLOR" # Custom color, OS dependent color|0x1000000 (i.e. ColorToNative(r,g,b)|0x1000000). If you do not |0x1000000, then it will not be used, but will store the color
    CUSTOM_HEIGHT_OVERRIDE = "I_HEIGHTOVERRIDE" # Custom height override for TCP window, 0 for none, otherwise size in pixels
    IS_TRACK_HEIGHT_LOCKED = "B_HEIGHTLOCK" # Must set I_HEIGHTOVERRIDE before locking
    TRIM_TRACK_VOLUME = "D_VOL"  # Trim volume of track, 0=-inf, 0.5=-6dB, 1=+0dB, 2=+6dB, etc
    TRIM_TRACK_PAN = "D_PAN" # Trim pan of track, -1..1
    TRACK_WIDTH = "D_WIDTH" # Width of track, -1..1
    DUALPAN_POS_L = "D_DUALPANL" # Dualpan position 1, -1..1, only if I_PANMODE == 6
    DUALPAN_POS_R = "D_DUALPANR" # Dualpan position 2, -1..1, only if I_PANMODE == 6
    PAN_MODE = "I_PANMODE" # 0=classic 3.x, 3=new balance, 5=stereo pan, 6=dual pan
    PAN_LAW = "D_PANLAW" # Pan law of track, <0=project default, 1=+0dB, etc
    TRACK_ENVELOPE_ID = "P_ENV" # P_ENV:<envchunkname or P_ENV:{GUID... : TrackEnvelope * : (read-only) chunkname can be <VOLENV, <PANENV, etc; GUID is the stringified envelope GUID.
    IS_TRACK_CTL_VISIBLE_IN_MIXER = "B_SHOWINMIXER" 
    IS_TRACK_CTL_VISIBLE_IN_ARRANGE_VIEW = "B_SHOWINTCP"
    IS_TRACK_SENDS_TO_PARENT = "B_MAINSEND" # Track sends audio to parent
    CHANNEL_OFFSET_SEND_TO_PARENT_STR = "C_MAINSEND_OFFS"
    CHANNEL_COUNT_SEND_TO_PARENT_STR = "C_MAINSEND_NCH" # Channel count of track send to parent (0=use all child track channels, 1=use one channel only)
    IS_TRACK_FREE_POSITIONING = "B_FREEMODE" # Track free item positioning enabled (call UpdateTimeline() after changing)
    TRACK_TIMEBASE_STR = "C_BEATATTACHMODE" # Track timebase, -1=project default, 0=time, 1=beats (position, length, rate), 2=beats (position only)
    MCP_FXSEND_SCALE = "F_MCP_FXSEND_SCALE" # Scale of fx+send area in MCP (0=minimum allowed, 1=maximum allowed)
    MCP_FXPARAM_SCALE = "F_MCP_FXPARAM_SCALE" # Scale of fx parameter area in MCP (0=minimum allowed, 1=maximum allowed)
    MCP_SENDRGN_SCALE = "F_MCP_SENDRGN_SCALE" # Scale of send area as proportion of the fx+send total area (0=minimum allowed, 1=maximum allowed)
    TPC_FXPARAM_SCALE = "F_TCP_FXPARM_SCALE" # Scale of TCP parameter area when TCP FX are embedded (0=min allowed, default, 1=max allowed)
    TRACK_MEDIAPLAYBACK_OFFSET_FLAG = "I_PLAY_OFFSET_FLAG" # Track media playback offset state, &1=bypassed, &2=offset value is measured in samples (otherwise measured in seconds)
    TRACK_MEDIAPLAYBACK_OFFSET = "D_PLAY_OFFSET"  # Double track media playback offset, units depend on I_PLAY_OFFSET_FLAG
