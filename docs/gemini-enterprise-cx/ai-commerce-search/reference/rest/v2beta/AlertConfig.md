---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/AlertConfig/
title: AlertConfig \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:22:28.887218+00:00
---

# AlertConfig  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/AlertConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  AlertConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AlertPolicy
    * JSON representation
  * EnrollStatus
  * Recipient
    * JSON representation



Project level alert config.

JSON representation  
---  
      
    
    {
      "name": string,
      "alertPolicies": [
        {
          object ([AlertPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/AlertConfig#AlertPolicy))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. Immutable. The name of the AlertConfig singleton resource. Format: projects/*/alertConfig  
`alertPolicies[]` |  `object (`[AlertPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/AlertConfig#AlertPolicy)`)` Alert policies for a customer. They must be unique by [AlertPolicy.alert_group]  
  
## AlertPolicy

Alert policy for a customer.

JSON representation  
---  
      
    
    {
      "alertGroup": string,
      "enrollStatus": enum ([EnrollStatus](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/AlertConfig#EnrollStatus)),
      "recipients": [
        {
          object ([Recipient](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/AlertConfig#Recipient))
        }
      ]
    }  
  
Fields  
---  
`alertGroup` |  `string` The feature that provides alerting capability. Supported value: - `search-data-quality` for retail search customers. - `conv-data-quality` for retail conversation customers.  
`enrollStatus` |  `enum (`[EnrollStatus](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/AlertConfig#EnrollStatus)`)` The enrollment status of a customer.  
`recipients[]` |  `object (`[Recipient](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/AlertConfig#Recipient)`)` Recipients for the alert policy. One alert policy should not exceed 20 recipients.  
  
## EnrollStatus

The enrollment status enum for alert policy.

Enums  
---  
`ENROLL_STATUS_UNSPECIFIED` | Default value. Used for customers who have not responded to the alert policy.  
`ENROLLED` | Customer is enrolled in this policy.  
`DECLINED` | Customer declined this policy.  
  
## Recipient

Recipient contact information.

JSON representation  
---  
      
    
    {
      "emailAddress": string
    }  
  
Fields  
---  
`emailAddress` |  `string` Email address of the recipient.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
