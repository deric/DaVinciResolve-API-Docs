--[[
Example DaVinci Resolve script:
Adds subclips [frame 0 .. 23] to current timeline for all media pool root folder clips
--]]

resolve = Resolve()
projectManager = resolve:GetProjectManager()
project = projectManager:GetCurrentProject()
mediaPool = project:GetMediaPool()
rootFolder = mediaPool:GetRootFolder()
clips = rootFolder:GetClips()

for clipIndex in pairs(clips) do
  clip = clips[clipIndex]
  videoCodec = clip:GetClipProperty()["Video Codec"]
  if videoCodec ~= "" then
    subClip = {}
    subClip["mediaPoolItem"] = clip
    subClip["startFrame"] = 0
    subClip["endFrame"] = 23

    if mediaPool:AppendToTimeline({ subClip }) then
      print("added subclip (first 24 frames) of \"" .. clip:GetName() .. "\" to current timeline.")
    end
  end
end

