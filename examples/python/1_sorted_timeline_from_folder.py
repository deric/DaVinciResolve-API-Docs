#!/usr/bin/env python


"""
Example DaVinci Resolve script:
Based on a given media folder path, this script creates a new project, a default timeline and appends clips into the timeline sorted by name
Example usage: 1_sorted_timeline_from_folder.py project1 24 1920 1080 /Users/username/Movies
"""

from python_get_resolve import GetResolve
import sys

# Inputs:
# - project name
# - project framerate
# - project width, in pixels
# - project height, in pixels
# - path to media
if len(sys.argv) < 6:
    print("input parameters for scripts are [project name] [framerate] [width] [height] [path to media]")
    sys.exit()

projectName = sys.argv[1]
framerate = sys.argv[2]
width = sys.argv[3]
height = sys.argv[4]
mediaPath = sys.argv[5]

# Create project and set parameters:
resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.CreateProject(projectName)

if not project:
    print("Unable to create a project '" + projectName + "'")
    sys.exit()

project.SetSetting("timelineFrameRate", str(framerate))
project.SetSetting("timelineResolutionWidth", str(width))
project.SetSetting("timelineResolutionHeight", str(height))

# Add folder contents to Media Pool:
mediapool = project.GetMediaPool()
rootFolder = mediapool.GetRootFolder()
clips = resolve.GetMediaStorage().AddItemListToMediaPool(mediaPath)

# Create timeline:
timelineName = "Timeline 1"
timeline = mediapool.CreateEmptyTimeline(timelineName)
if not timeline:
    print("Unable to create timeline '" + timelineName + "'")
    sys.exit()

# Sort by name
clips = sorted(clips, key = lambda clip : clip.GetClipProperty("File Name")["File Name"])

for clip in clips:
    mediapool.AppendToTimeline(clip)

projectManager.SaveProject()

print("'" + projectName + "' has been added")
