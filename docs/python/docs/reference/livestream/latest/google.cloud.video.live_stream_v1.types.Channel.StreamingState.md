---
url: https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Channel.StreamingState
title: Class StreamingState (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:10.024676+00:00
---

# Class StreamingState (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Channel.StreamingState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class StreamingState (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.1  1.7.4  1.6.0  1.5.2  1.4.1  1.3.0  1.2.1  1.1.0  1.0.4  0.2.0  0.1.5 
    
    
    StreamingState(value)

State of streaming operation that the channel is running.

## Enums  
  
---  
**Name** | **Description**  
`STREAMING_STATE_UNSPECIFIED` | Streaming state is not specified.  
`STREAMING` | Channel is getting the input stream, generating the live streams to the specified output location.  
`AWAITING_INPUT` | Channel is waiting for the input stream through the input.  
`STREAMING_ERROR` | Channel is running, but has trouble publishing the live streams onto the specified output location (for example, the specified Cloud Storage bucket is not writable).  
`STREAMING_NO_INPUT` | Channel is generating live streams with no input stream. Live streams are filled out with black screen, while input stream is missing. Not supported yet.  
`STOPPED` | Channel is stopped, finishing live streams.  
`STARTING` | Channel is starting.  
`STOPPING` | Channel is stopping.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
