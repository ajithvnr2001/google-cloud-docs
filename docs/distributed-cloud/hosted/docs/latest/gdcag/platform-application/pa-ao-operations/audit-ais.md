---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-ais/
title: GKE Identity Service (GIS) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:21.199663+00:00
---

# GKE Identity Service (GIS)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-ais/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  GKE Identity Service (GIS) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Root and organization workloads  
---|---  
**Audit log source** |  GKE Identity Service  
**Audited operations** | 

  * Revoke or create a login token
  * Create an STS token

  
  
## Revoke or create a login token

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `payload.user` |  For example,
    
    
    "payload":{
      "user":"fop-infrastructure-operator@example.com"
    }  
  
**Target** _(Fields and values that call the API)_ | `resource` | `"resource":"login_token"`  
**Action** _(Fields containing the performed operation)_ | `operation` | `"operation":"revoke"`  
**Event timestamp** | `metadata.timestamp` |  For example,
    
    
    "metadata":{
      "timestamp":"2023-01-13T20:04:30.529916149+00:00"
    }  
  
**Source of action** | `payload.issuer` |  For example,
    
    
    "payload":{
      "issuer":"fake-oidc-provider"
    }  
  
**Outcome** | `description` | `"description":"Revoked Login Token '84518e03-396a-425d-93ac-5ff1e1c993f8' which was previously issued to user 'fop-infrastructure-operator@example.com' due to a web logout"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "description":"Revoked Login Token '84518e03-396a-425d-93ac-5ff1e1c993f8' which was previously issued to user 'fop-infrastructure-operator@example.com' due to a web logout",
      "id":"55f2ae33-d229-4057-aa1f-d62349281e9c",
      "_gdch_service_tenant":"platform-obs",
      "resource":"login_token",
      "_gdch_tenant_id":"platform-obs",
      "payload":{
        "id":"84518e03-396a-425d-93ac-5ff1e1c993f8",
        "expirationTime":"2023-01-14T08:03:33.413710266+00:00",
        "user":"fop-infrastructure-operator@example.com",
        "groups":[""],
        "issuer":"fake-oidc-provider"
        },
      "_gdch_service_name":"ais",
      "_gdch_namespace":"anthos-identity-service",
      "operation":"revoke",
      "metadata":{
        "userAgent":"",
        "timestamp":"2023-01-13T20:04:30.529916149+00:00"
        },
      "_gdch_org_name":"UNKNOWN",
      "_gdch_org_id":"UNKNOWN",
      "_gdch_cluster":"org-1-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-nhbwb"
    }
    

## Create an STS token

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
