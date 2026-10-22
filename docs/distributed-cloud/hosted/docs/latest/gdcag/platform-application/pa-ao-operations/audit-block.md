---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-block/
title: Block storage (BLOCK) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:49.335685+00:00
---

# Block storage (BLOCK)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-block/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Block storage (BLOCK) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** All Block storage logs are for create, modify, and delete operations that you execute over CLI, REST API or SNMP. Read-only requests are not logged. Consider the complete list of logs as the entirety of the CLI and REST documentation. The following are examples of create, modify, and delete operations.**Workload location** |  Block storage  
---|---  
**Audit log source** |  Block storage  
**Example audited operations** | 

  * Create a volume
  * Set the size of a volume
  * Delete a volume

  
  
## Create a volume

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` | For example, 
    
    
    "message":"{"user":{"identity":"root-admin-client-cert"}}  
  
**Target** _(Fields and values that call the API)_ | `message.action` | For example, 
    
    
    "message":"{"action":"volume-create"}"  
  
**Action** _(Fields containing the performed operation)_ |  `action` |  For example, `"action":"volume-create"`  
**Event timestamp** |  `time` |  For example, `"time":"2022-12-07T13:46:49.133781Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":"{"sourceIPs":["10.252.143.2"]}"  
  
**Outcome** | `message.response` |  For example,
    
    
    "message":"{"response":"success"}"  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log**
    
    
    {
      "pri":"14",
      "time":"2022-12-07T13:46:49.133781Z",
      "host":"storage",
      "ident":"storage",
      "pid":"-",
      "msgid":"-",
      "extradata":"-",
      "message":"{"time":"2022-12-07T13:40:18Z","auditID":"90199274229","user":{"identity":"root-admin-client-cert"},"resource":"{"Application":"ontapi","Hostname":"zh-ad-stge02-02","StorageVirtualMachine":"root-admin"}","action":"volume-create","sourceIPs":["10.252.143.2"],"response":"success","_gdch_org":"root-admin"}",
      "_gdch_cluster":"root-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-vn8f9",
      "_gdch_service_name":"admin-audit-logs"
    }
    

## Set the size of a volume

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` | For example, 
    
    
    "message":"{"user":{"identity":"root-admin-client-cert"}}  
  
**Target** _(Fields and values that call the API)_ | `message.action` | For example, 
    
    
    "message":"{"action":"volume-size"}"  
  
**Action** _(Fields containing the performed operation)_ |  `action` |  For example, `"action":"volume-size"`  
**Event timestamp** |  `time` |  For example, `"time":"2022-12-07T13:46:49.133781Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":"{"sourceIPs":["10.252.143.2"]}"  
  
**Outcome** | `message.response` |  For example,
    
    
    "message":"{"response":"success"}"  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log**
    
    
    {
      "pri":"14",
      "time":"2022-12-07T13:46:49.135968Z",
      "host":"storage",
      "ident":"storage",
      "pid":"-",
      "msgid":"-",
      "extradata":"-",
      "message":"{"time":"2022-12-07T13:46:36Z","auditID":"120264072202","user":{"identity":"root-admin-client-cert"},"resource":"{"Application":"ontapi","Hostname":"zh-ad-stge03-01","StorageVirtualMachine":"root-admin"}","action":"volume-size","sourceIPs":["10.252.143.2"],"response":"success","_gdch_org":"root-admin"}",
      "_gdch_cluster":"root-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-vn8f9",
      "_gdch_service_name":"admin-audit-logs"
    }
    
    

## Delete a volume

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` | For example, 
    
    
    "message":"{"user":{"identity":"root-admin-client-cert"}}  
  
**Target** _(Fields and values that call the API)_ | `message.action` | For example, 
    
    
    "message":"{"action":"volume-destroy"}"  
  
**Action** _(Fields containing the performed operation)_ |  `action` |  For example, `"action":"volume-destroy"`  
**Event timestamp** |  `time` |  For example, `"time":"2022-12-07T13:46:49.133781Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":"{"sourceIPs":["10.252.143.2"]}"  
  
**Outcome** | `message.response` |  For example,
    
    
    "message":"{"response":"success"}"  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log**
    
    
    {
      "pri":"14",
      "time":"2022-12-07T13:46:49.136236Z",
      "host":"storage",
      "ident":"storage",
      "pid":"-",
      "msgid":"-",
      "extradata":"-",
      "message":"{"time":"2022-12-07T13:46:37Z","auditID":"90203137689","user":{"identity":"root-admin-client-cert"},"resource":"{"Application":"ontapi","Hostname":"zh-ad-stge01-02","StorageVirtualMachine":"root-admin"}","action":"volume-destroy","sourceIPs":["10.252.143.2"],"response":"success","_gdch_org":"root-admin"}",
      "_gdch_cluster":"root-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-vn8f9",
      "_gdch_service_name":"admin-audit-logs"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
