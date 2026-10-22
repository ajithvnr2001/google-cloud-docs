---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-fw/
title: Firewall (FW) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:49.919243+00:00
---

# Firewall (FW)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-fw/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Firewall (FW) Stay organized with collections  Save and categorize content based on your preferences. 

## IDPS firewall

**Workload location** |  Hardware  
---|---  
**Audit log source** |  Palo Alto Firewall  
**Audited operations** | 

  * Log in to Web UI and show settings
  * Commit job changes

  
  
### Log in to Web UI and show settings

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message` |  A subset of the `message` value. For example, `admin`  
**Target** _(Fields and values that call the API)_ | `message` |  For example, ` "message":"012501009150,2022/11/22 12:03:54,audit,2561,gui-op,admin,\"<show><system><setting><multi-vsys/></setting></system></show>\",success" `  
**Action** _(Fields containing the performed operation)_ |  `message` |  A subset of the `message` value. For example, ` gui-op,admin,\"<show><system><setting><multi-vsys/></setting></system></show>\" `  
**Event timestamp** | `time` |  For example, `"time": "2022-11-22T12:03:55-08:00"`  
**Source of action** | `host` |  For example, `"host":"10.251.72.101"`  
**Outcome** | _Not applicable_ | _Not applicable_  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "pri": "14",
      "time": "2022-11-22T12:03:55-08:00",
      "host": "10.251.72.101",
      "ident": "-",
      "pid": "-",
      "msgid": "-",
      "extradata": "-",
      "message": "012501009150,2022/11/22 12:03:54,audit,2561,gui-op,admin,\"<show><system><setting><multi-vsys/></setting></system></show>\",success",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-6lgds",
      "_gdch_service_name": "panw_audit_logs"
    }
    

### Commit job changes

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message` |  A subset of the `message` value. For example, `admin`  
**Target** _(Fields and values that call the API)_ | `message` |  For example, ` "message":"1,2022/11/22 12:11:33,012501009150,CONFIG,0,2561,2022/11/22 12:11:33,10.251.72.79,,commit,admin,Web,Submitted,,7168767370163388448,0x0,0,0,0,0,,zb-aa-fw01,0,,0,2022-11-22T12:11:34.635-08:00" `  
**Action** _(Fields containing the performed operation)_ |  `message` |  A subset of the `message` value. For example, `Web,Submitted`  
**Event timestamp** | `time` |  For example, `"time": "2022-11-22T12:11:34-08:00"`  
**Source of action** | `host` |  For example, `"host":"10.251.72.101"`  
**Outcome** | _Not applicable_ | _Not applicable_  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "pri": "14",
      "time": "2022-11-22T12:11:34-08:00",
      "host": "10.251.72.101",
      "ident": "-",
      "pid": "-",
      "msgid": "-",
      "extradata": "-",
      "message": "1,2022/11/22 12:11:33,012501009150,CONFIG,0,2561,2022/11/22 12:11:33,10.251.72.79,,commit,admin,Web,Submitted,,7168767370163388448,0x0,0,0,0,0,,zb-aa-fw01,0,,0,2022-11-22T12:11:34.635-08:00",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-6lgds",
      "_gdch_service_name": "panw_audit_logs"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
