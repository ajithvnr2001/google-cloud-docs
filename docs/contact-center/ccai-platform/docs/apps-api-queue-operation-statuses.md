---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-queue-operation-statuses/
title: Queue operation statuses endpoint \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:08:55.886524+00:00
---

# Queue operation statuses endpoint  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-queue-operation-statuses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)



Send feedback 

#  Queue operation statuses endpoint Stay organized with collections  Save and categorize content based on your preferences. 

You can use the queue operation statuses endpoint to get availability status for a queue before you deflect a session to it. This endpoint returns the following boolean properties:

  * `after_hours`: `true` if the queue is unavailable because it's in an after hours state

  * `overcapacity`: `true` if the queue is unavailable because it's in an overcapacity state




**_Endpoint:_**

Method: `GET`

Type: RAW

URL: `https://{subdomain}.{domain}/apps/api/v1/queue_operation_statuses`

**_Query:_**

Key | Value | Description  
---|---|---  
`menu_id` | integer | The ID for the queue that you want availability information for. Required.  
`lang` | string | The two-letter language code for the queue, in ISO 639-1 format. Required.  
`channel_type` | string | The channel type. Possible values are `call` and `chat`. Required.  
  
### Example request and response

This section provides an example request and response.

#### Request
    
    
    https://{subdomain}.{domain}/apps/api/v1/queue_operation_statuses?menu_id=1&lang=en&channel_type=call
    

#### Response
    
    
    {
      "menu_id": 1,
      "lang": "en",
      "channel_type": "call",
      "after_hour": false,
      "overcapacity": true
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
