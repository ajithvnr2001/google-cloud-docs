---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/json/decode/
title: Function: json.decode \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:12.422813+00:00
---

# Function: json.decode  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/json/decode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: json.decode Stay organized with collections  Save and categorize content based on your preferences. 

Decodes given JSON bytes (assuming UTF-8), or a string, into an object.

If the input is bytes, it is first converted to a string, as if by calling `text.decode(data, 'UTF-8')`.

## Arguments

Arguments  
---  
`data` |  `bytes|string` The input to be decoded.  
  
## Returns

The decoded object.

## Raised exceptions

Exceptions  
---  
`ValueError` | If given data is not a valid JSON object.  
  
## Examples

For more information, see [Returning bytes](https://cloud.google.com/workflows/docs/reference/syntax/datatypes.md#bytes).
    
    
    # Decode Base64-encoded string to bytes, then decode bytes to object
    - init:
        assign:
          - project: '${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}'
          - subscription: SUBSCRIPTION_ID
    - pullMessage:  # pulls Pub/Sub message
        call: googleapis.pubsub.v1.projects.subscriptions.pull
        args:
            subscription: '${"projects/" + project + "/subscriptions/" + subscription}'
            body:
                maxMessages: 1
        result: m
    - outputMessage:
        return: '${json.decode(base64.decode(m.receivedMessages[0].message.data))}'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
