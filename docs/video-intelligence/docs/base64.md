---
url: https://docs.cloud.google.com/video-intelligence/docs/base64/
title: Base64 Encoding \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:25.481939+00:00
---

# Base64 Encoding  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/base64/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Base64 Encoding Stay organized with collections  Save and categorize content based on your preferences. 

When passing video to the Video Intelligence API, you can either pass a Cloud Storage URI, or you can embed video data directly within the request's `content` field, which must be base64 encoded.

## Using the command line

Within a gRPC request, you can simply write binary data out directly; however, JSON is used when making a REST request. JSON is a text format that does not directly support binary data, so you will need to convert such binary data into text using [Base64](https://en.wikipedia.org/wiki/Base64) encoding.

Most development environments contain a native `base64` utility to encode a binary into ASCII text data. To encode a file:

### Linux

Encode the file using the `base64` command line tool, making sure to prevent line-wrapping by using the `-w 0` flag:
    
    
    base64 INPUT_FILE -w 0 > OUTPUT_FILE
    

### macOS

Encode the file using the `base64` command line tool:
    
    
    base64 -i INPUT_FILE -o OUTPUT_FILE
    

### Windows

Encode the file using the `Base64.exe` tool:
    
    
    certutil -encodehex SOURCE_VIDEO_FILE > DEST_TEXT_FILE 0x40000001
    

### PowerShell

Encode the file using the `Convert.ToBase64String` method:
    
    
    [Convert]::ToBase64String([IO.File]::ReadAllBytes("./INPUT_FILE")) > OUTPUT_FILE
    

Create a JSON request file, inlining the base64-encoded data:

### JSON
    
    
    {
      "requests":[
        {
          "image":{
            "content": "ZkxhQwAAACIQABAAAAUJABtAA+gA8AB+W8FZndQvQAyjv..."
          },
          "features": [
            {
              "type":"LABEL_DETECTION",
              "maxResults":1
            }
          ]
        }
      ]
    }

## Using client libraries

Embedding binary data into requests through text editors is neither desirable or practical. In practice, you will be embedding base64 encoded files within client code. All supported programming languages have built-in mechanisms for base64 encoding content.

### Python

In Python, base64 encode video files as follows:
    
    
    # Import the base64 encoding library.
    import base64
    
    # Pass the video data to an encoding function.
    def encode_video(video):
      video_content = video.read()
      return base64.b64encode(video_content)
    

### Node.js

In Node.js, base64 encode video files as follows:
    
    
    // Read the file into memory.
    var fs = require('fs');
    var videoFile = fs.readFileSync('/path/to/file');
    
    // Convert the video data to a Buffer and base64 encode it.
    var encoded = new Buffer(videoFile).toString('base64');
    

### Java

In Java, you can base64 encode image files as follows:
    
    
    // Import the Base64 encoding library.
    import org.apache.commons.codec.binary.Base64;
    
    // Encode the video.
    byte[] videoData = Base64.encodeBase64(videoFile.getBytes());
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
