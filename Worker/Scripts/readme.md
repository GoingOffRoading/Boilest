# Workflow

This is the Boilest workflow, and work that is currently outstanding 

# To Do List
- [x] Cron that checks the queue, and injects the find_files task if the queue is empty
- [x] Task that recusively searches directories based on file extensions
- [x] For each file, calls the next step
- [x] Function that calls FFprobe for the file, and determines next step
- [x] Function that calls FFmpeg and processes the file
- [x] Function that moves the encoded file into the source and deletes the soure file
- [x] Function that checks the files size of the new and old file
- [x] Configuration based
- [x] Writing results of the ffencode step to SQLite
- [x] Starts workflow based on a JSON configuration
- [x] Rewrite the FFProbe section to handle when a media file doesn't have a video, audio, or subtitle stream
- [x] Expirement with AV1 film grain: https://www.google.com/search?q=av1+film+grain+synthesis+anime
- [x] Fix an issue where invalid ffmpeg settings would crash ffmpeg, and a file of 0kb would replace source 
- [ ] Expirement with subtitle settings
- [ ] Experiement with audio codec settings
- [ ] UI
- [x] When establishing the codecs, we check for keywords like 'video' (see line 91 in Taks.py), which may return a false positive because ffprobe could use the keyworld 'video' in objects not related to defining the stream type.  Will need to figure out how to work around this.
- [ ] Stopping the script does not stop the ffmpeg terminal/os command.  There should be a way to interupt ffmpeg from the script
- [ ] Add more inline documentation
- [ ] Add additional fields so different file attributes can get different ffmpeg commands
- [x] Celery queues: https://stackoverflow.com/questions/51631455/how-to-route-tasks-to-different-queues-with-celery-and-django
- [X] Celery starts queues based on docker env variables
- [x] Around line 150 in tasks...  The function to check if ffmpeg should run checks for a variable like subtitle, without establishing if the subtitle stream exists.  This casues all media missing the stream to encode.  Need to fix.
- [ ] Repo Documentation
- [x] Add the other two SQL insert statements to fresults
- [ ] Rearrange git repo/directory structure
- [ ] Experiment with the Ubuntu FFMpeg image for SVT-AV! latest and greatest
- [ ] Create and integrate a secrets/config file/template, or maybe use container evars
- [ ] See if we can create a test pipeline using open source video clip
- [ ] Sort through the test scrips, and start deleting duplicates
- [ ] Rewrite the function that checks the queues as that is spagetti
- [ ] Replace the print statements with logging: https://docs.python.org/3/howto/logging.html