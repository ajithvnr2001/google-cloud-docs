---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-add-third-party-to-call/
title: Add a third party to a call \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:31.211901+00:00
---

# Add a third party to a call  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-add-third-party-to-call/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Add a third party to a call Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use the `/calls/CALL_ID/dial` endpoint of the apps API to dial a third party and then add them to an ongoing call. When you make a request to this endpoint, the system automatically dials the third-party's phone number, and the agent's call adapter displays the **Calling** screen. Adding third parties to calls in this way works regardless of whether the call adapter is running in the agent desktop, in your CRM, or in the CCAI Platform portal. An agent must be on an active call for this endpoint to function.

## Call the endpoint

To add a third party to a call, make a `POST` request to the following endpoint:
    
    
    https://YOUR_CCAAS_HOST/apps/api/v1/calls/CALL_ID/dial
    

Replace `CALL_ID` with the call ID.

### Request body

The following is an example of a request body:
    
    
    {
      "agent_email": "AGENT_EMAIL",
      "phone_number": "PHONE_NUMBER"
    }
    

Replace the following:

  * `AGENT_EMAIL`: The email address of the agent on the call.
  * `PHONE_NUMBER`: The phone number of the third party to be added to the call.



### Response

The output is similar to the following.

#### Success response
    
    
    {
        "message": "Third party dialing initiated",
        "participant": {
            "id": 54321,
            "type": "third_party",
            "status": "connecting"
        }
    }
    

#### Error responses

  * `400 Bad Request` \- `phone_number` or `agent_email` is missing or empty. Body: `{"message": "param is missing or the value is empty: <name>"}`.
  * `400 Bad Request` \- `agent_email` does not match a known user. Body: `{"message": "Invalid agent_email"}`.
  * `401 Unauthorized` \- authentication failed. Body: `{"message": "Not Authorized"}`.
  * `404 Not Found` \- no call exists with the supplied `call_id`. Body: `{"message": "Not Found"}`.
  * `422 Unprocessable Entity` \- the agent identified by `agent_email` is not connected to the call. Body: `{"message": "Agent is not connected to the call"}`.
  * `422 Unprocessable Entity` \- the dial couldn't be initiated; covers phone-number normalization failures and provider dial-initiation errors. Body: `{"message": "Error dialing third party"}`.
  * `500 Internal Server Error` \- unexpected failure during dial. Body: `{"message": "Unexpected error dialing third party"}`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
