---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-cobrowse/
title: Screen Share endpoint \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:56.041256+00:00
---

# Screen Share endpoint  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-cobrowse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Screen Share endpoint Stay organized with collections  Save and categorize content based on your preferences. 

The Screen Share sessions endpoint provides access to the Screen Share service.

## Screen Share sessions endpoint

Parameter | Required | Data Type | Definition  
---|---|---|---  
ext_session_id | TRUE | String | The external Screen Share session ID  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{​{subdomain}​}.{​{domain}​}/apps/api/v1/cobrowse_sessions/
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {}
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### End a Screen Share session using an external session ID

This example shows how to end a current Screen Share session.

##### Request

You can end a Screen Share session using an external session ID.

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Parameter | Required | Data Type | Definition  
---|---|---|---  
ext_session_id | TRUE | String | The external Screen Share session ID  
  
Request URL:
    
    
    POST https://SUBDOMAIN.DOMAIN/apps/api/v1/cobrowse_sessions/EXTERNAL_SESSION_ID/end
    

Replace the following:

  * `SUBDOMAIN`: Your CCAI Platform tenant name.

  * `DOMAIN`: The domain for your instance.

  * `EXTERNAL_SESSION_ID`: The external session ID for the Screen Share session that you want to end.




##### Response: Session terminated
    
    
    {
        "message": "Session terminated"
    }
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
