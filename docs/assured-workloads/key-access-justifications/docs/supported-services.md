---
url: https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/supported-services/
title: Supported services \u00a0|\u00a0 Key Access Justifications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:52.908269+00:00
---

# Supported services  |  Key Access Justifications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/supported-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management)
  * [ Key Access Justifications ](https://docs.cloud.google.com/assured-workloads/key-access-justifications)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supported services

Key Access Justifications supports all services supported by Assured Workloads for [EU Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-access-justifications). In addition, Key Access Justifications supports the following Google Cloud products:

**Service** | **Status**  
---|---  
AlloyDB for PostgreSQL  | GA   
Backup for GKE  | GA   
Firestore  | GA   
Private services access  | GA   
Gemini Enterprise Agent Platform Workbench  | GA   
  
If Key Access Justifications is in Preview for a service, Google recommends that you don't use Key Access Justifications in production for that service. You should use Key Access Justifications for a service in production only if Key Access Justifications for that service is in General Availability (GA). This includes transitive usage of unintegrated or Preview services that don't themselves store data encrypted using customer keys, because all services involved in servicing a request must have a GA Key Access Justifications integration status for Google to reliably generate justifications.

If you are unable to avoid using a service for which Key Access Justifications isn't in GA in your workloads that depend on Key Access Justifications, then you must also allow `REASON_NOT_EXPECTED`, `REASON_UNSPECIFIED`, and `CUSTOMER_AUTHORIZED_WORKFLOW_SERVICING` justifications in your Key Access Justifications policies or risk outages.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
