import os
from smi2srt_handle import SMI2SRTHandle

def Start():
  pass   

def convertSubtitles(part):
  Log(part.file)
  basePath = os.path.splitext(part.file)[0]
  smiPath = basePath+'.smi'
  ret = SMI2SRTHandle.start(smiPath, no_remove_smi=not Prefs['remove_smi'])
  Log(ret)

# entry for Movie
class SmiSubtitleAgentMovies(Agent.Movies):
  name = 'SMI Converter'
  #languages = [Locale.Language.NoLanguage]
  languages = [Locale.Language.Korean]
  primary_provider = False
  
  def search(self, results, media, lang):
    results.Append(MetadataSearchResult(id = 'null', score = 100))
    
  def update(self, metadata, media, lang):
    for i in media.items:
      for part in i.parts:
        convertSubtitles(part)

# entry for TV shows
class SmiSubtitleAgentTV(Agent.TV_Shows):
  name = 'SMI Converter'
  #languages = [Locale.Language.NoLanguage]
  languages = [Locale.Language.Korean]
  primary_provider = False

  def search(self, results, media, lang):
    results.Append(MetadataSearchResult(id = 'null', score = 100))

  def update(self, metadata, media, lang):
    for s in media.seasons:
      # just like in the Local Media Agent, if we have a date-based season skip for now.
      if int(s) < 1900:
        for e in media.seasons[s].episodes:
          for i in media.seasons[s].episodes[e].items:
            for part in i.parts:
              convertSubtitles(part)
