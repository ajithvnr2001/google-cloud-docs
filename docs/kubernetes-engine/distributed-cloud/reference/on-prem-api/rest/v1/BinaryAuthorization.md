---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BinaryAuthorization/
title: BinaryAuthorization \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:18.004611+00:00
---

# BinaryAuthorization  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BinaryAuthorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  BinaryAuthorization Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EvaluationMode



Configuration for Binary Authorization.

JSON representation  
---  
      
    
    {
      "evaluationMode": enum ([EvaluationMode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BinaryAuthorization#EvaluationMode))
    }  
  
Fields  
---  
`evaluationMode` |  `enum (`[EvaluationMode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BinaryAuthorization#EvaluationMode)`)` Mode of operation for binauthz policy evaluation. If unspecified, defaults to DISABLED.  
  
## EvaluationMode

Binary Authorization mode of operation.

Enums  
---  
`EVALUATION_MODE_UNSPECIFIED` | Default value  
`DISABLED` | Disable BinaryAuthorization  
`PROJECT_SINGLETON_POLICY_ENFORCE` | Enforce Kubernetes admission requests with BinaryAuthorization using the project's singleton policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
