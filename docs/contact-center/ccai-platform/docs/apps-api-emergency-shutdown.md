---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-emergency-shutdown/
title: Emergency shutdown \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:22.414634+00:00
---

# Emergency shutdown  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-emergency-shutdown/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Emergency shutdown Stay organized with collections  Save and categorize content based on your preferences. 

Turn on or off emergency shutdown on one or more queues. This API lets external systems remotely control queue availability during emergency situations.

Parameter | Required | Data Type | Definition  
---|---|---|---  
`menu_id` | true | Array | Array of queue IDs to update.  
`language` | true | String | ISO 639-1 language code (for example, `en`, `es`).  
`emergency_shutdown.enabled` | true | Boolean | Enable (`true`) or disable (`false`) emergency shutdown.  
`emergency_shutdown.message.type` | false | String | Message type: `tts` (text-to-speech) or `audio` (audio URL).  
`emergency_shutdown.message.content` | false | String | TTS text or audio file URL. Required if `message.type` is specified.  
`emergency_shutdown.in_progress_calls` | false | String | How to handle in-progress calls: `allow_finish`, `end_and_redirect_to_after_hours`, `end_and_redirect_to_overcapacity`.  
`emergency_shutdown.queued_calls` | false | String | How to handle queued calls: `disconnect`, `redirect_to_after_hours`, `redirect_to_overcapacity`.  
  
**Notes:**

  * If no message is specified when enabling, the global default emergency shutdown message is used.

  * The `in_progress_calls` and `queued_calls` parameters are optional. If they're not specified, global settings are inherited.

  * To use this API, you must enable both the API and the emergency queue capability.




## Examples

This section contains code examples for the emergency shutdown API.

### Endpoint

Method: `POST`

URL: `https://{subdomain}.{domain}/apps/api/v1/menus/shutdown`

### Headers

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json |   
  
### Example 1: shutdown enabled

This example enables the emergency queue shutdown capability.

#### Request body
    
    
    {
        "menu_id": [
            123,
            456
        ],
        "language": "en",
        "emergency_shutdown": {
            "enabled": true,
            "message": {
                "type": "tts",
                "content": "We are currently experiencing an emergency. Please call back later."
            },
            "in_progress_calls": "allow_finish",
            "queued_calls": "disconnect"
        }
    }
    

#### Response
    
    
    {
        "menu_id": [
            123,
            456
        ],
        "language": "en",
        "emergency_shutdown": {
            "enabled": true,
            "message": {
                "type": "tts",
                "content": "We are currently experiencing an emergency. Please call back later."
            },
            "in_progress_calls": "allow_finish",
            "queued_calls": "disconnect"
        }
    }
    

### Example 2: shutdown enabled, default global message

This example enables the emergency queue shutdown capability and uses the default global message.

#### Request body
    
    
    {
        "menu_id": [
            123
        ],
        "language": "en",
        "emergency_shutdown": {
            "enabled": true
        }
    }
    

#### Response
    
    
    {
        "success": true,
        "affected_queues": [
            123
        ],
        "emergency_shutdown": {
            "enabled": true,
            "message_source": "global_default",
            "in_progress_calls": null,
            "queued_calls": null
        }
    }
    

### Example 3: shutdown disabled

This example disables the emergency queue shutdown capability.

#### Request body
    
    
    {
        "menu_id": [
            123
        ],
        "language": "en",
        "emergency_shutdown": {
            "enabled": false
        }
    }
    

#### Response
    
    
    {
        "success": true,
        "affected_queues": [
            123
        ],
        "emergency_shutdown": {
            "enabled": false,
            "message_source": null,
            "in_progress_calls": null,
            "queued_calls": null
        }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
