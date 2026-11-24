import os
# One-liner entry (116 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "Approved. The logic is sound, the tests pass, and I have a terrible feeling about the function named doEverything()."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
