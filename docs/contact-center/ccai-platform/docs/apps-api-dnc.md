---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-dnc/
title: Company do not call (DNC) list endpoints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:29.013887+00:00
---

# Company do not call (DNC) list endpoints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-dnc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Company do not call (DNC) list endpoints Stay organized with collections  Save and categorize content based on your preferences. 

The company DNC (do not call) list lets you block direct, manual outbound calls as well as outbound and scheduled calls created by the Apps API.

Contact Center AI Platform (CCAI Platform) Apps API provides the following three endpoints for DNC:

  * Add phone numbers to DNC list.

  * Remove phone numbers from DNC list.

  * Check whether a phone number is in the DNC list.




## Add phone numbers to the DNC list

Parameter | Required | Data Type | Definition  
---|---|---|---  
contacts | TRUE | Array contacts | An array of contacts. Each contact has a `phone_number` attribute and optional `expires_at` attribute  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.{domain}/apps/api/v1/outbound_dialer/dnc
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "contacts": [
            {
                "phone_number": "+1-7187309219",
                "expires_at": "2022-10-29 00:00:00 UTC"
            },
            {
                "phone_number": "+1-(358)-213-1634"
            }
        ]
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Add some contacts to the DNC list

This example shows the adding of contacts to the DNC list.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "contacts": [
            {
                "phone_number": "+1-7187309219",
                "expires_at": "2022-10-29 00:00:00 UTC"
            },
            {
                "phone_number": "+1-(358)-213-1634"
            },
            {
                "phone_number": "+1-4151113333",
                "expires_at": "2022-10-30 00:00:00 UTC"
            },
            {
                "phone_number": "+1-4151115555"
            },
            {
                "phone_number": "+1-7187309219",
                "expires_at": "2022-10-27 00:00:00 UTC"
            },
            {
                "phone_number": "sssssss"
            },
            {
                "phone_number": "911",
                "expires_at": "2023-02-05 00:00:00 UTC"
            }
        ]
    }
    

##### Response
    
    
    [
        {
            "phone_number": "+1-7187309219",
            "expires_at": "2022-10-29 00:00:00 UTC",
            "status": "created"
        },
        {
            "phone_number": "+1-(358)-213-1634",
            "status": "created"
        },
        {
            "phone_number": "+1-4151113333",
            "expires_at": "2022-10-30 00:00:00 UTC",
            "status": "updated"
        },
        {
            "phone_number": "+1-4151115555",
            "status": "updated"
        },
        {
            "phone_number": "+1-7187309219",
            "expires_at": "2022-10-27 00:00:00 UTC",
            "error": "expires_at cannot be past date/time",
            "status": "failed"
        },
        {
            "phone_number": "sssssss",
            "error": "phone_number is invalid",
            "status": "failed"
        },
        {
            "phone_number": "911",
            "expires_at": "2023-02-05 00:00:00 UTC",
            "error": "emergency phone number is not allowed",
            "status": "failed"
        }
    ]
    

`Code: 200`

## Remove numbers from the DNC list

Parameter | Required | Data Type | Definition  
---|---|---|---  
phone_numbers | TRUE | Array String | An array containing phone numbers that should be removed from the DNC list.  
  
**_Endpoint:_**
    
    
    Method: POST
    Type: RAW
    URL: https://{subdomain}.{domain}/apps/api/v1/outbound_dialer/dnc/remove
    

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "phone_numbers": [
            "1-415-111-1111"
        ]
    }
    

### Example request and responses

The following sections provide example requests to the endpoint.

#### Remove a list of phone numbers

This example shows how to remove phone numbers from the list.

##### Request

**_Headers:_**

Key | Value | Description  
---|---|---  
Content-Type | application/json |   
  
**_Body:_**
    
    
    {
        "phone_numbers": [
            "1-415-111-1111",
            "1-415-222-2222",
            "1-415-333-333-3333"
        ]
    }
    

##### Response: Success
    
    
    {}
    

**_Status Code:_** 200

## Check whether a phone number is on the DNC list

Parameter | Required | Data Type | Definition  
---|---|---|---  
phone_number | TRUE | String | The phone number to check if it is in the DNC list  
  
**_Endpoint:_**
    
    
    Method: GET
    Type: 
    URL: URL: https://{subdomain}.{domain}/apps/api/v1/outbound_dialer/dnc/check?phone_number={phone_number}
    

**_Headers:_**

None

**_Body:_**

None

### Example request and responses

The following sections provide example requests to the endpoint.

#### Check if number is in the DNC list

This example showes how to check if a phone number is in the DNC list.

##### Request

Key | Value  
---|---  
phone_number | {PHONE_NUMBER} (Number) The end-user's phone number.  
      
    
    GET https://{subdomain}.{domain}/apps/api/v1/outbound_dialer/dnc/check?phone_number={PHONE_NUMBER}
    

##### Response
    
    
    {
    "phone_number": "1-415-111-1111",
    "expired_at": "2023-08-05 22:02:36.362009 +0000"
    "do_not_call": true
    }
    

`Code: 200`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
