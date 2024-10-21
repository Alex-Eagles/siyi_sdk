import subprocess

# Command to run mpv with your stream and options
mpv_command = [
    "mpv",
    "--msg-color=yes", "--msg-module=yes", "--keepaspect=yes",
    "--no-correct-pts", "--untimed", "--vd-lavc-threads=1", "--cache=no",
    "--cache-pause=no", "--demuxer-lavf-o-add=fflags=+nobuffer+fastseek+flush_packets",
    "--demuxer-lavf-probe-info=nostreams", "--demuxer-lavf-analyzeduration=0.1",
    "--demuxer-max-bytes=500MiB", "--demuxer-readahead-secs=0.1", "--interpolation=no",
    "--hr-seek-framedrop=no", "--video-sync=display-resample", "--temporal-dither=yes",
    "--framedrop=decoder+vo", "--deband=no", "--dither=no", "--hwdec=auto-copy",
    "--hwdec-codecs=all", "--video-latency-hacks=yes", "--profile=low-latency",
    "--linear-downscaling=no", "--correct-downscaling=yes", "--sigmoid-upscaling=yes",
    "--scale=ewa_hanning", "--scale-radius=3.2383154841662362", "--cscale=ewa_lanczossoft",
    "--dscale=mitchell", "--fs", "--osc=no", "--osd-duration=450", "--border=no",
    "--no-pause", "--no-resume-playback", "--keep-open=no", "--network-timeout=0",
    "--stream-lavf-o=reconnect_streamed=1", "--vf=scale=854:480", "--vf-add=fps=30",
    "rtsp://192.168.144.25:8554/main.264"
]

# Running mpv as a subprocess
process = subprocess.Popen(mpv_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Read output from mpv (can be logs, messages, etc.)
while True:
    output = process.stdout.readline()
    if output == b'' and process.poll() is not None:
        break
    if output:
        print(output.strip().decode())
