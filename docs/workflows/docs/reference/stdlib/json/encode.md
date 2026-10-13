---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/json/encode/
title: Function: json.encode \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:12.933738+00:00
---

# Function: json.encode  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/json/encode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: json.encode Stay organized with collections  Save and categorize content based on your preferences. 

Encodes given input object to JSON bytes, using UTF-8 charset.

If `indent` is provided, it must be either a boolean, or a dictionary with two optional string attributes: `prefix` (defaulting to an empty string), and `indent` (defaulting to four spaces). Setting `indent` to `true` is equivalent to setting it to an empty dictionary. Setting `indent` to `false` is equivalent to not setting it.

When the indentation is enabled, each JSON element begins on a new line beginning with `prefix` and followed by zero or more copies of `indent` according to the structural nesting.

## Arguments

Arguments  
---  
`data` | The input to be encoded.  
`indent` | Optional indentation options.  
  
## Returns

The resulting JSON bytes.

## Raised exceptions

Exceptions  
---  
`ValueError` | If the input contains types that cannot be JSON-encoded. Examples of such types include callable and bytes.  
  
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
