---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/mid-session-authentication-apps-api/
title: Mid-Session authentication by API \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:58.321996+00:00
---

# Mid-Session authentication by API  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/mid-session-authentication-apps-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Mid-Session authentication by API Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use call and chat API endpoints for mid-session authentication in your SDK channels.

Users can start a support session, such as a support chat, without authenticating. When end-user authentication becomes necessary, you can initiate an authentication flow. Upon successful authentication, you can update the `end_user` identifier to link the session to the verified end-user.

## URI and authentication

The base URI for this new endpoint differs depending on the `comm_type`.

For the `call` comm_type:

POST `https://&lt;subdomain>.&lt;domain>//apps/api/v1/calls/:call_id/end_user`

For the `chat` comm_type:

POST `https://&lt;subdomain>.&lt;domain>//apps/api/v1/chats/:chat_id/end_user`

## API operations

### Parameters

The body of the API request should have the following fields:

ID  | Field name  | Type  | Required?  | Description  | Example values   
---|---|---|---|---|---  
0  | `identifier` | String  | Yes  | Unique external identifier provided.  |   
1  | `name` | String  | No  | The generic name or identifier associated with the interaction. Aids with customer lookup.  | `John Doe`  
2  | `email` | String  | No  | The generic email address associated with the interaction. Aids with customer lookup.  | `john@doe.com`  
3  | `phone` | String  | No  | The generic phone number associated with the interaction. Aids with customer lookup.  | `123-456-7890`  
  
## API samples

### Sample API response

#### Success response sample:

`202 Accepted`
    
    
    {
     "message": "accepted"
    }
    

#### Failure response samples

##### Missing Parameters
    
    
    400 {"message": "param is missing or the value is empty: comm_type"}
    400 {"message": "param is missing or the value is empty: identifier"}
    

##### Referencing a comm type other than call or chat
    
    
    404 {"message": "Not Found"}
    

##### Session not active
    
    
    400 {"message": "Call is already ended"}
    400 {"message": "Chat is already ended"}
    

##### Unsupported CRM request
    
    
    400 {"message": "Unsupported CRM request"}
    

##### Duplicate request
    
    
    400 {"message": "Duplicate request: Please wait for the interval to expire"}
    

## API request sample

### Call Comm Type
    
    
    POST https://<subdomain>.<domain>/apps/api/v1/calls/:call_id/end_user
    Content-Type: application/json
    Authorization: Bearer <your_access_token>
    
    {
        "identifier": "unique_external_id",
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "123-456-7890"
    }
    

### Chat Comm Type
    
    
    POST https://<subdomain>.<domain>/apps/api/v1/chats/:chat_id/end_user
    Content-Type: application/json
    Authorization: Bearer <your_access_token>
    
    {
        "identifier": "unique_external_id",
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "phone": "098-765-4321"
    }
    

## Apps API Documentation

For additional apps API endpoints, see [Apps API Publication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
