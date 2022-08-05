<h1>The SC2 Build Extractor</h1>

Project Goal:
---
The goal of this project was to create a tool that can extract build orders out of 
StarCraft2 replay files.<br> These builds are sent out as JSON formatted data, which can then be
plugged into the accompanying application I am working on. 

That application can be found here:  
https://github.com/Soule222/sc2BuildPractice

This project is fully functional with Terran, and will mostly work with Zerg and Protoss, but
their supply counters are currently wrong and there may be some missing build items still. 

**Getting Started / Usage**
---

Make sure to install SC2Reader via pip or it's associated GitHub page:   
https://github.com/ggtracker/sc2reader

Locate the file in which you have a StarCraft2 replay saved and use the following input on the command line:

  ```sh
  python buildmain.py "PATHTOYOURREPLAY.SC2Replay"
  ```
You will then be prompted to give your files names, and that's it!

Here's an example:

![example-screenshot]

After that, if you have never run this script before, a build folder
will be created in your local repository, where you can find the 
exported build order. 

**Acknowledgements**
---
StarCraft 2 and all assests related to StarCraft all belong to Blizzard Entertainment, Inc.

StarCraft® II: Wings of Liberty®<br>
©2010 Blizzard Entertainment, Inc. All rights reserved. Wings of Liberty is a trademark, and StarCraft and Blizzard Entertainment are trademarks or registered trademarks of Blizzard Entertainment, Inc. in the U.S. and/or other countries.

StarCraft® II: Heart of the Swarm<br>
©2013 Blizzard Entertainment, Inc. All rights reserved. Heart of the Swarm and StarCraft are trademarks or registered trademarks of Blizzard Entertainment, Inc. in the U.S. and/or other countries.

Unfortunately Blizzard doesn't also include a copyright notice on their webpage for StarCraft II: Legacy of the Void, but it applies here as well.

I'd also like to thank @Graylin Kim and his library: SC2Reader that made this all possible:

https://github.com/ggtracker/sc2reader

[example-screenshot]: buildextractor/images/screenshot.png