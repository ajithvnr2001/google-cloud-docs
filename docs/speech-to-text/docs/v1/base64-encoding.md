---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/base64-encoding/
title: Base64 encoding audio content \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:46.401618+00:00
---

# Base64 encoding audio content  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/base64-encoding/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Base64 encoding audio content Stay organized with collections  Save and categorize content based on your preferences. 

When you send audio data to the Cloud Speech-to-Text API you can either send the data directly (within the request's [`content`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionAudio) field) or have the API perform recognition remotely on data stored in a Cloud Storage bucket. You can send data directly in the `content` field for [synchronous recognition](https://docs.cloud.google.com/speech-to-text/docs/v1/sync-recognize#performing_synchronous_speech_recognition_on_a_local_file) **only** if your audio data is a maximum of 60 seconds and 10 MB. Any audio data in the `content` field must be in base64 format. This page describes how to convert audio from a binary file to base64-encoded data.

If your audio data exceeds 60 seconds or 10 MB, it must be stored in a Cloud Storage bucket in order to be sent for recognition. You can analyze it asynchronously without converting it to base64 format. See the [asynchronous recognition documentation](https://docs.cloud.google.com/speech-to-text/docs/v1/async-recognize) for details.

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
    
    
    Base64.exe -e INPUT_FILE > OUTPUT_FILE
    

### PowerShell

Encode the file using the `Convert.ToBase64String` method:
    
    
    [Convert]::ToBase64String([IO.File]::ReadAllBytes("./INPUT_FILE")) > OUTPUT_FILE
    

Create a JSON request file, inlining the base64-encoded data:

### JSON
    
    
    {
      "config": {
        "encoding": "FLAC",
        "sampleRateHertz": 16000,
        "languageCode": "en-US"
      },
      "audio": {
        "content": "ZkxhQwAAACIQABAAAAUJABtAA+gA8AB+W8FZndQvQAyjv..."
      }
    }

## Using client libraries

Embedding binary data into requests through text editors is neither desirable or practical. In practice, you will be embedding base64 encoded files within client code. All supported programming languages have built-in mechanisms for base64 encoding content.

### Python

In Python, base64 encode audio files as follows:
    
    
    # Import the base64 encoding library.
    import base64
    
    # Pass the audio data to an encoding function.
    def encode_audio(audio):
      audio_content = audio.read()
      return base64.b64encode(audio_content)
    

### Node.js

In Node.js, base64 encode audio files as follows, where `audioFile` is the path to the audio-encoded file.
    
    
    const fs = require('fs');
    const content = fs.readFileSync(audioFile).toString('base64');
    

### Java

In Java, use the `encodeBase64` static method within `org.apache.commons.codec.binary.Base64` to base64 encode binary files:
    
    
    // Import the Base64 encoding library.
    import org.apache.commons.codec.binary.Base64;
    
    // Encode the speech.
    byte[] encodedAudio = Base64.encodeBase64(audio.getBytes());
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
