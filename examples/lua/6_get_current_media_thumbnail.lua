--[[
Example DaVinci Resolve script:
Retrieve current media thumbnail from the color page
--]]

resolve = Resolve()
projectManager = resolve:GetProjectManager()
project = projectManager:GetCurrentProject()
timeline = project:GetCurrentTimeline()
currentMediaThumbnail = timeline:GetCurrentClipThumbnailImage()
width = currentMediaThumbnail["width"]
height = currentMediaThumbnail["height"]
format = currentMediaThumbnail["format"]
imageBase64str = currentMediaThumbnail["data"]
print(" Width of the thumbnail is " .. width .. ", Height is " .. height .. ", Format is " .. format .. "\n Thumbnail image data in base64 is " .. imageBase64str)
-- Need to decode the image from base 64 to retrieve the image just like the python example.
