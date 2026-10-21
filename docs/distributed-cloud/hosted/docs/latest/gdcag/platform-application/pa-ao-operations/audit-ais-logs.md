---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-ais-logs/
title: GKE Identity Service audit logs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:10:45.199010+00:00
---

# GKE Identity Service audit logs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-ais-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  GKE Identity Service audit logs Stay organized with collections  Save and categorize content based on your preferences. 

GKE Identity Service is an authentication proxy used in GDC to let customers bring their existing identity solutions for user authentication.

**JSON representation**
    
    
    {
      "description": string,
      "id": string,
      "metadata": object {
        "timestamp": string,
        "userAgent": string
      },
      "operation": string,
      "payload": object {},
      "resource": string
    }
    

Fields  
---  
`id` |  `string` A unique ID assigned to every audit event. For example, `"d53270e7-d9e7-4d49-b16a-a5ed161c1469"`  
`description` |  `string` A human-readable description of the event. For example, `"An STS token was minted for user: 102405777051160536773"`  
`resource` |  `string` The resource being audited. Allowed values are `"session"`, `"login_token"`, or `"sts_token"`. For example, `"sts_token"`  
`operation` |  `string` The operation being performed on the resource. Allowed values are `"create"`, `"revoke"`, or `"list"`. For example, `"create"`  
`metadata` |  `object` The metadata associated with the event.  
`userAgent` |  `string` The user-agent HTTP header, if applicable.  
`timestamp` |  `string` The timestamp at which the event was created. For example, `"2022-12-16T00:53:32.005010538+00:00"`  
`payload` |  `object` Arbitrary event-specific payload. For example,
    
    
            {
              "audience": "test-audience",
              "expirationTime": "2022-12-16T12:53:31.95180671+00:00",
              "issuer": "",
              "user": "102405777051160536773"
              "groups": [],
              "parentId": "8216278b-295e-4fef-af8d-a6c0a54d15e5"
           }
             
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
