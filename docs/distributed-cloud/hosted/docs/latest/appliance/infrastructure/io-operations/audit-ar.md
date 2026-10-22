---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-ar/
title: Artifact Registry (AR) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:47.232868+00:00
---

# Artifact Registry (AR)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-ar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Artifact Registry (AR) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  File storage  
---|---  
**Audit log source** |  [Artifact Management audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-am)  
**Audited operations** | 

  * Create an artifact
  * Delete an artifact
  * Pull an artifact

  
**Log type** |  Data plane  
  
## Create an artifact

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "identity":"s:gpc-system:artifact-registry-services-registry-exporter",
      "issuer":"artifact.private.gdc.goog/hra"
    }  
  
**Target** _(Fields and values that call the API)_ | 

  * `resource`
  * `_gdch_service_name`
  * `_gdch_cluster`

| 
    
    
    "resource": "library/configsync:1.9.0-gdch.306",
    "_gdch_service_name": "artifactmanagement",
    "_gdch_cluster": "root-admin"  
  
**Action** _(Fields containing the performed operation)_ | `action` |  `"action": "create"`  
**Event timestamp** |  `time` |  For example, `"time": "2022-11-30T02:14:33Z"`  
**Source of action** | _Not available._ |  _Not available._  
**Outcome** | _Only successful operations are logged._ |  _Only successful operations are logged._  
**Other fields** | `_gdch_cluster` |  For example, `"_gdch_cluster": "root-admin"`  
  
### Example log
    
    
    {
      "auditID": "15000",
      "action": "create",
      "time": "2022-11-30T02:14:33Z",
      "user":{
        "identity":"s:gpc-system:artifact-registry-services-registry-exporter",
        "issuer":"artifact.private.gdc.goog/hra"
      },
      "resource": "library/configsync:1.9.0-gdch.306",
      "_gdch_service_name": "artifactmanagement",
      "_gdch_namespace": "harbor-system",
      "_gdch_service_tenant": "infra-obs",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-wqbg8"
    }
    

## Delete an artifact

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "identity":"s:gpc-system:artifact-registry-services-registry-exporter",
      "issuer":"artifact.private.gdc.goog/hra"
    }  
  
**Target** _(Fields and values that call the API)_ | 

  * `resource`
  * `_gdch_service_name`
  * `_gdch_cluster`

| 
    
    
    "resource": "library/test:v1",
    "_gdch_service_name": "artifactmanagement",
    "_gdch_cluster": "root-admin"  
  
**Action** _(Fields containing the performed operation)_ | `action` |  `"action": "delete"`  
**Event timestamp** |  `time` |  For example, `"time": "2022-11-30T21:26:17.718Z"`  
**Source of action** | _Not available._ |  _Not available._  
**Outcome** | _Only successful operations are logged._ |  _Only successful operations are logged._  
**Other fields** | `_gdch_cluster` |  For example, `"_gdch_cluster": "root-admin"`  
  
### Example log
    
    
    {
      "auditID": "3993",
      "action": "delete",
      "time": "2022-11-30T21:26:17.718Z",
      "user":{
        "identity":"s:gpc-system:artifact-registry-services-registry-exporter",
        "issuer":"artifact.private.gdc.goog/hra"
      },
      "resource": "library/test:v1",
      "_gdch_service_name": "artifactmanagement",
      "_gdch_namespace": "harbor-system",
      "_gdch_service_tenant": "infra-obs",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-wqbg8"
    }
    

## Pull an artifact

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "identity":"s:gpc-system:artifact-registry-services-registry-exporter",
      "issuer":"artifact.private.gdc.goog/hra"
    }  
  
**Target** _(Fields and values that call the API)_ | 

  * `resource`
  * `_gdch_service_name`
  * `_gdch_cluster`

| 
    
    
    "resource": "library/test:v1",
    "_gdch_service_name": "artifactmanagement",
    "_gdch_cluster": "root-admin"  
  
**Action** _(Fields containing the performed operation)_ | `action` |  `"action": "pull"`  
**Event timestamp** |  `time` |  For example, `"time": "2022-11-30T02:14:33Z"`  
**Source of action** | _Not available._ |  _Not available._  
**Outcome** | _Only successful operations are logged._ |  _Only successful operations are logged._  
**Other fields** | `_gdch_cluster` |  For example, `"_gdch_cluster": "root-admin"`  
  
### Example log
    
    
    {
      "auditID": "3996",
      "action": "pull",
      "time": "2022-11-30T02:14:33Z",
      "user":{
        "identity":"s:gpc-system:artifact-registry-services-registry-exporter",
        "issuer":"artifact.private.gdc.goog/hra"
      },
      "resource": "library/test:v1",
      "_gdch_service_name": "artifactmanagement",
      "_gdch_namespace": "harbor-system",
      "_gdch_service_tenant": "infra-obs",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-wqbg8"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
