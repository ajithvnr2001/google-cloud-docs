---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-contact-data/
title: Contact data endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:35:25.212546+00:00
---

# Contact data endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-contact-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Contact data endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) provides the CRM contact data endpoint for setting contact data.

## CRM - contact_data

Parameter | Required | Data Type | Definition  
---|---|---|---  
lang | TRUE | String | Language code of the queue. (e.g. 'en')  
menu_id | FALSE | Integer | Response will filter all menus in that menu's subtree, including that menu.  
menu_type | FALSE | String | Returns menus of specific types. Possible values: ivr_menu, mobile_menu, web_menu).  
channel_type | FALSE | String | Returns menus of a specific channel. Possible values: voice_call, chat).  
wait[from] | FALSE | Integer | Returns records if they have a wait greater than the value.  
wait[to] | FALSE | Integer | Returns records if they have a wait less than the value.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/crm/contact_data
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "call_id" : "1917",
        "agent_id" : "1", 
        "lcm_key" : "2922|1|2|39|2|0|1",
        "dnis" : "8001992999",
        "org_id" : "tenant1",
        "contact" : {
            "first_name" : "Alex",
            "last_name" : "Phil",
            "account_no" : "10002-2989",
            "crm_id" : "220-39307-92",
            "address" : "",
            "city" : "",
            "loan_type" : "",
            "due_date" : "" 
        },
        "pacing_mode" : "Predictive",
        "call_type" : "OB_Regular"
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
