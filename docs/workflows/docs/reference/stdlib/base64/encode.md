---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/base64/encode/
title: Function: base64.encode \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:00.475348+00:00
---

# Function: base64.encode  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/base64/encode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: base64.encode Stay organized with collections  Save and categorize content based on your preferences. 

Encodes given bytes to Base64 text.

## Arguments

Arguments  
---  
`data` |  `bytes` The input to be encoded.  
`padding` |  `boolean` Specifies whether padding characters should be used to align the output to a multiple of 4 bytes (default: `true`).  
  
## Returns

The encoded Base64 output, as a string.

## Examples

For more information, see [Returning bytes](https://cloud.google.com/workflows/docs/reference/syntax/datatypes.md#bytes).
    
    
    # Encode message to JSON bytes, then encode bytes to Base64 text
    - init:
        assign:
          - project: '${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}'
          - topic: TOPIC_ID
          - message:
              hello: world
          - base64Msg: '${base64.encode(json.encode(message))}'
    - publish_message_to_topic:  # publishes message to Pub/Sub topic
        call: googleapis.pubsub.v1.projects.topics.publish
        args:
          topic: '${"projects/" + project + "/topics/" + topic}'
          body:
            messages:
              - data: '${base64Msg}'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
