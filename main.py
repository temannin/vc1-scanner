import glob
import subprocess
import json

import probe

file_path = "PATH"


for file in glob.iglob(file_path, recursive=True):
    if (not file.endswith(".mkv")):
        continue

    args = "ffprobe -v quiet -print_format json -show_format -show_streams".split(
        " ")

    args.append(file)

    process_result = subprocess.run(args, capture_output=True)
    probe_data = json.loads(process_result.stdout.decode("utf-8"))
    probe_result = probe.ProbeResult.from_dict(probe_data)

    break
