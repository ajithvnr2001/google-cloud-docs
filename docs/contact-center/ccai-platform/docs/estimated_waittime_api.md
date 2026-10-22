---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/estimated_waittime_api/
title: Estimated Wait Time API \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:04.085535+00:00
---

# Estimated Wait Time API  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/estimated_waittime_api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Estimated Wait Time API Stay organized with collections  Save and categorize content based on your preferences. 

This API endpoint returns the calculated estimated wait time (EWT) per queue.

This can be used for custom support channel EWT displays on web pages or mobile apps outside of the Contact Center AI Platform (CCAI Platform) SDK, or for custom notifications or triggers.

## Example Request

**URL: http://{subdomain}.{domain}/apps/api/v1/wait_times**

**Parameters**

ID | Field Name | Type | Required | Description | Values | Notes  
---|---|---|---|---|---|---  
1 | menu_id | id | No | Response will filter all menus (queues) in that menu's sub-menu, including that menu | Root Menu (default) Specific menu | If nothing is passed, will return whole queue structure  
2 | channel_type | enum | No | Returns menus of a specific channel | voice_call chat | Optional param  
3 | menu_type | enum | No | Returns menus of specific types | ivr_menu mobile_menu web_menu All (default) | optional  
4 | wait[from] | int | No | Returns records if they have a wait greater than the value |  | Validation:Positive Int only  
5 | wait[to] | int | No | Returns records if they have a wait less than the value |  | Validation:Positive Int only  
6 | lang | enum | Yes | Queue structure to retrieve the ewt | Ex: "en" "es" "fr" "de" "it" "ja" "ko" "pt" "pt-BR" "sv" |   
  
### Responses

**ID** | **Field Name** | **Type** | **Required** | **Description**  
---|---|---|---|---  
1 | menu_id | id | yes | Foreign key to the /menus manager api endpoint  
2 | wait | INT | yes | Wait time in minutes  
3 | Materialized path | String | Yes | Materialized path as found in the /menus api  
  
### Example

http://{subdomain}.{domain}/apps/api/v1/wait_times?lang=en&menu_id=10
    
    
    [
        {
            "menu_id": 10,
            "menu_type": "ivr_menu",
            "voice_call": 120,
            "materialized_path": "Subscription",
            "logged_in_agents": 3,
            "available_agents": 0,
            "breakthrough_agents": 1
        }
    ]
    

**_Status Code:_** 200

Menu ID 10 estimated wait time is 120 seconds (or two minutes)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
