---
url: https://docs.cloud.google.com/binary-authorization/quotas/
title: Quotas and limits \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:47.883169+00:00
---

# Quotas and limits  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Resources ](https://docs.cloud.google.com/binary-authorization/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

## Request rate limits

Binary Authorization enforces the following request rate limits:

Request type | Value  
---|---  
Read request | 100 per user-project-minute  
Update or delete request | 20 per user-project-minute  
Create request | 10 per user-project-minute  
AdmissionReview request (Binary Authorization enforcement) | 500 per user-project-minute  
**Note:** When Binary Authorization enforcement is enabled, GKE sends AdmissionReview requests every time a Pod is created or updated, regardless of whether the creation or update is manual or automated, and regardless of whether there are new images being deployed. For example, it sends AdmissionReview requests when when a ReplicaSet creates a new Pod to create more capacity, or to compensate for a Pod or machine failure. Any Kubernetes operation that creates or updates many Pods sends an AdmissionReview request for each Pod separately. Every Admission review request counts toward the AdmissionReview quota.

## Resource limits

Binary Authorization also enforces the following limits:

Limit | Value  
---|---  
Number of attestor resources per project | 200  
Number of attestor references per Policy | 200  
Number of keys per attestor | 1000  
Number of Binary Authorization platform policy bindings per cluster | 10  
Number of attestation projects allowed per check | 10  
  
## Quota increases

If you would like to increase any of the limits, we might like to understand more about your needs. You can submit a Binary Authorization quota request for your project in the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
