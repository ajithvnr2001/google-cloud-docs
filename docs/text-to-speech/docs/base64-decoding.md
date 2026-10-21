---
url: https://docs.cloud.google.com/text-to-speech/docs/base64-decoding/
title: Decode base64-encoded audio content \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:15.427757+00:00
---

# Decode base64-encoded audio content  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/base64-decoding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)



Send feedback 

#  Decode base64-encoded audio content Stay organized with collections  Save and categorize content based on your preferences. 

Audio data is binary data. You can read the binary data directly from a gRPC response; however, JSON is used when responding to a REST request. Because JSON is a text format that does not directly support binary data, Cloud Text-to-Speech returns a response string encoded in [Base64](https://en.wikipedia.org/wiki/Base64). You must convert the base64-encoded text data from the response to binary before you can play it on a device.

JSON responses from the Cloud Text-to-Speech include base64-encoded audio content in the `audioContent` field. For example:
    
    
    {
      "audioContent": "//NExAARqoIIAAhEuWAAAGNmBGMY4EBcxvABAXBPmPIAF//yAuh9Tn5CEap3/o..."
    }
    

To decode base64 into an audio file:

### Linux

  1. Copy only the base-64 encoded content into a text file.

  2. Decode the source text file using the base64 command line tool by using the `-d` flag:



    
    
        $ base64 SOURCE_BASE64_TEXT_FILE -d > DESTINATION_AUDIO_FILE

### Mac OSX

  1. Copy only the base-64 encoded content into a text file.

  2. Decode the source text file using the base64 command line tool:



    
    
        $ base64 --decode -i SOURCE_BASE64_TEXT_FILE > DESTINATION_AUDIO_FILE

### Windows

  1. Copy only the base-64 encoded content into a text file.

  2. Decode the source text file using the [`certutil`](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certutil) command.



    
    
       certutil -decode SOURCE_BASE64_TEXT_FILE DESTINATION_AUDIO_FILE

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
