---
url: https://docs.cloud.google.com/speech-to-text/docs/base64-encoding/
title: Base64 encoding audio content \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:00.866386+00:00
---

# Base64 encoding audio content  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/base64-encoding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Base64 encoding audio content Stay organized with collections  Save and categorize content based on your preferences. 

When you send audio data to the Speech-to-Text API, you can either send the data directly (within the request's [`content`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#google.cloud.speech.v2.RecognizeRequest.FIELDS.bytes.google.cloud.speech.v2.RecognizeRequest.content) field) or have the API perform recognition remotely on data stored in a Cloud Storage bucket by specifying the storage object in the request's [`uri`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#google.cloud.speech.v2.RecognizeRequest.FIELDS.string.google.cloud.speech.v2.RecognizeRequest.uri) field.

Any audio data in the `content` field in HTTP requests must be in base64 format. This page describes how to convert audio from a binary file to base64-encoded data.

**Note:** For clients using client libraries or a gRPC client, audio content should be in binary format, not base64 format.**Note:** Check the [quotas and limits](https://docs.cloud.google.com/speech-to-text/quotas) documentation for the content limits on inline audio.

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
      "recognizer": "projects/PROJECT_ID/locations/global/recognizers/_",
      "content": "ZkxhQwAAACIQABAAAAUJABtAA+gA8AB+W8FZndQvQAyjv..."
    }
    

## Using client libraries

Embedding binary data into requests through text editors is neither desirable or practical. In practice, you will be embedding base64 encoded files within client code. All supported programming languages have built-in mechanisms for base64 encoding content.

### Python

In Python, base64 encode audio files as follows:
    
    
    # Import the base64 encoding library.
    import base64
    
    # Pass the audio data to an encoding function.
    def encode_audio(audio_file):
        with open(audio_file, "rb") as f:
            encoded_content = base64.b64encode(f.read())
        return encoded_content
    

### Node.js
    
    
    // Read the file into memory.
    var fs = require('fs');
    var audioFile = fs.readFileSync('/full/path/to/audio/file.wav');
    
    // Convert the audio data to a Buffer and base64 encode it.
    var encoded = Buffer.from(audioFile).toString('base64');
    

### Java
    
    
    // Import the Base64 encoding library.
    import org.apache.commons.codec.binary.Base64;
    
    // Encode the audio.
    byte[] audioData = Base64.encodeBase64(audioFile.getBytes());
    String encodedString = Base64.getEncoder().encodeToString(audioData);
    

### Go
    
    
    import (
        "bufio"
        "encoding/base64"
        "io"
        "os"
    )
    
    // Open audio file.
    f, _ := os.Open("/full/path/to/audio/file.wav")
    
    // Read entire audio into byte slice.
    reader := bufio.NewReader(f)
    content, _ := io.ReadAll(reader)
    
    // Encode audio as base64.
    base64.StdEncoding.EncodeToString(content)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
