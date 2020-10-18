#!/usr/bin/env python

"""
Example DaVinci Resolve script:
Adds subclips [frame 0 .. 23] to current timeline for all media pool root folder clips
Example usage: 7_add_subclips_to_timeline.py
"""

from python_get_resolve import GetResolve

if __name__ == "__main__":
    resolve = GetResolve()
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    mediaPool = project.GetMediaPool()
    rootFolder = mediaPool.GetRootFolder()
    clips = rootFolder.GetClipList()

    for clip in clips:
        if clip.GetClipProperty()["Video Codec"] != "":
            subClip = {
                "mediaPoolItem": clip,
                "startFrame": 0,
                "endFrame": 23,
            }

            if mediaPool.AppendToTimeline([ subClip ]):
                print("added subclip (first 24 frames) of \"" + clip.GetName() + "\" to current timeline.")

