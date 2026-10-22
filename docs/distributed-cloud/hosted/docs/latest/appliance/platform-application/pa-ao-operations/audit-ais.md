---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-ais/
title: GKE Identity Service (AIS) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:30.002630+00:00
---

# GKE Identity Service (AIS)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-ais/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  GKE Identity Service (AIS) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Root and organization workloads  
---|---  
**Audit log source** |  GKE Identity Service  
**Audited operations** |  Create STS token  
  
## Create STS token

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `identity` |  For example, `"identity":"fop-shengjiang"`  
**Target** _(Fields and values that call the API)_ | `resource` | `"resource":"AIS STS token"`  
**Action** _(Fields containing the performed operation)_ | `action` | `"action":"Create"`  
**Event timestamp** | `time` |  For example, `"time":"2022-11-22T18:31:37.084205362+00:00"`  
**Source of action** | `userAgent` |  For example, `"userAgent":"Go-http-client/2.0"`  
**Outcome** | `response` |  For example, `"response":"Success"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "action":"Create",
      "auditID":"vwWq8fQ-o9RTopgcZtAC_psm1aYyMKxkv47GOkdU",
      "description":"An AIS STS token is minted for fop-shengjiang (from fake-oidc-provider) and will be valid for 11h59m49.438314611s",
      "resource":"AIS STS token",
      "response":"Success",
      "time":"2022-11-22T18:31:37.084205362+00:00",
      "user":{
        "groups":[
          "group-claim-1",
          "group-claim-2"
          ],
        "identity":"fop-shengjiang",
        "issuer":"fake-oidc-provider"
        },
      "userAgent":"Go-http-client/2.0"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
