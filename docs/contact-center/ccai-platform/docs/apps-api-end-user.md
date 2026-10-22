---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-end-user/
title: End users endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:32.414932+00:00
---

# End users endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-end-user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  End users endpoints Stay organized with collections  Save and categorize content based on your preferences. 

The end users API endpoints provide access to the end-user objects. An end-user object is created for each end user of Contact Center AI Platform (CCAI Platform).

The following are the call API endpoints:

  * Update end-user

  * Get end-user




## Update end-user

This endpoint lets you update an end-user details including:

  * email address

  * name

  * phone number



    
    
    {
        "identifier": "string",
        "email": "string",
        "name": "string",
        "phone": "string"
    }
    

**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.{domain}/apps/api/v1/end_users
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
Accept | application/json |   
  
**_Body:_**
    
    
    {
        "identifier": "abc123",
        "email": "joe@mydomain.com",
        "name": "Joe Smith",
        "phone": "+16171231234"
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### End user ID and identifier

This example shows how to update an end-user by providing the ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "identifier": "string",
        "email": "string",
        "name": "string",
        "phone": "string"
    }
    

##### Response
    
    
    {
        "id": "integer",
        "identifier": "string"
    }
    

**_Status Code:_** 200

## Get end-user

This endpoint provides the ability to retrieve an end-user using either the `id` or `identifier`.

**_Endpoint:_**
    
    
    Method: GET
    Type:
    URL: https://{subdomain}.{domain}/apps/api/v1/end_users
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
id | integer | Internal ID for the End User  
identifier | string | External identifier for the End User  
  
### Example request and responses

The following sections provide example requests to the endpoint.

#### Get by ID

This example shows how to retrieve an end-user by providing the ID.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
id | integer | Internal ID for the End User  
  
##### Response
    
    
    {
        "id": "integer",
        "identifier": "string"
    }
    

**_Status Code:_** 200

#### Get by identifier

This example shows how to retrieve an end-user by providing the identifier.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Query:_**

Key | Value | Description  
---|---|---  
identifier | string | External identifier for the End User  
  
##### Response
    
    
    {
        "id": "integer",
        "identifier": "string"
    }
    

**_Status Code:_** 200

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
