---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-os/
title: Node and operating system (OS) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:57.092054+00:00
---

# Node and operating system (OS)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-os/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Node and operating system (OS) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Hardware  
---|---  
**Audit log source** |  Node OS  
**Audited operations** | 

  * Sign-in events
  * Operating system teletypewriter (OS TTY) events
  * Clam antivirus (ClamAV) events
  * Advanced Intrusion Detection Environment (AIDE) events

  
  
## Sign-in events

All access attempts and actions through OS SSH connections.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `ident` |  `"ident": "sshd"`  
**Target** _(Fields and values that call the API)_ | `message` |  For example, `"message": "pam_tty_audit(sshd:session): restored status to 0"`  
**Action** _(Fields containing the performed operation)_ | `message` |  For example, `"message": "pam_tty_audit(sshd:session): restored status to 0"`  
**Event timestamp** | `time` |  For example, `"time": "2022-11-30T22:53:39.442037+00:00"`  
**Source of action** | `host` |  For example, `"host": "zb-aa-bm01"`  
**Outcome** | `message` |  For example, `"message": "pam_tty_audit(sshd:session): restored status to 0"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "pri": "87",
      "time": "2022-11-30T22:53:39.442037+00:00",
      "host": "zb-aa-bm01",
      "ident": "sshd",
      "pid": "757322",
      "msgid": "-",
      "extradata": "-",
      "message": "pam_tty_audit(sshd:session): restored status to 0",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-dn5jn",
      "_gdch_service_name": "inventory-machine-bm-e2c2a7e1"
    }
    

## OS TTY events

All commands printing outputs on the console.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `ident` |  `"ident": "audispd"`  
**Target** _(Fields and values that call the API)_ | `message` |  For example, `"message": "node=ubuntu type=TTY msg=audit(1671531815.870:94280): tty pid=1217279 uid=0 auid=0 ses=3536 major=136 minor=0 comm=\"pager\" data=71"`  
**Action** _(Fields containing the performed operation)_ | `message` |  For example, `"message": "node=ubuntu type=TTY msg=audit(1671531815.870:94280): tty pid=1217279 uid=0 auid=0 ses=3536 major=136 minor=0 comm=\"pager\" data=71"`  
**Event timestamp** | `time` |  For example, `"time": "2022-12-20T10:23:35.878924+00:00"`  
**Source of action** | `host` |  For example, `"host": "zk-aa-bm08"`  
**Outcome** | `message` |  For example, `"message": "node=ubuntu type=TTY msg=audit(1671531815.870:94280): tty pid=1217279 uid=0 auid=0 ses=3536 major=136 minor=0 comm=\"pager\" data=71"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "pri": "14",
      "time": "2022-12-20T10:23:35.878924+00:00",
      "host": "zk-aa-bm08",
      "ident": "audispd",
      "pid": "-",
      "msgid": "-",
      "extradata": "-",
      "message": "node=ubuntu type=TTY msg=audit(1671531815.870:94280): tty pid=1217279 uid=0 auid=0 ses=3536 major=136 minor=0 comm=\"pager\" data=71",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-w6fl4",
      "_gdch_service_name": "inventory-machine-bm-7cc496d5"
    }
    

## ClamAV events

All ClamAV scanning events.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `ident` |  Possible values:

  * `"ident": "clamav"`
  * `"ident": "clamonacc"`

  
**Target** _(Fields and values that call the API)_ | `message` |  For example, `"message": "No virus found"`  
**Action** _(Fields containing the performed operation)_ | `message` |  For example, `"message": "No virus found"`  
**Event timestamp** | `time` |  For example, `"time": "2022-12-20T04:01:47.219862+00:00"`  
**Source of action** | `host` |  For example, `"host": "zk-aa-bm09"`  
**Outcome** | `message` |  For example, `"message": "No virus found"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "pri": "86",
      "time": "2022-12-20T04:01:47.219862+00:00",
      "host": "zk-aa-bm09",
      "ident": "clamav",
      "pid": "-",
      "msgid": "-",
      "extradata": "-",
      "message": "No virus found",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-lcxgq",
      "_gdch_service_name": "inventory-machine-bm-b11f4752"
    }
    

## AIDE events

All AIDE intrusion detection events.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `ident` |  `"ident": "aide"`  
**Target** _(Fields and values that call the API)_ | `message` |  For example, `"message": "AIDE check passed."`  
**Action** _(Fields containing the performed operation)_ | `message` |  For example, `"message": "AIDE check passed."`  
**Event timestamp** | `time` |  For example, `"time": "2022-12-20T10:20:09.428106+00:00"`  
**Source of action** | `host` |  For example, `"host": "zk-aa-bm08"`  
**Outcome** | `message` |  For example, `"message": "AIDE check passed."`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "pri": "86",
      "time": "2022-12-20T10:20:09.428106+00:00",
      "host": "zk-aa-bm08",
      "ident": "aide",
      "pid": "-",
      "msgid": "-",
      "extradata": "-",
      "message": "AIDE check passed.",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-lcxgq",
      "_gdch_service_name": "inventory-machine-bm-7cc496d5"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
