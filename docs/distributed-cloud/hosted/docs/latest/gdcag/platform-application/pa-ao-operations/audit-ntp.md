---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-ntp/
title: NTP server workloads (NTP) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:13.604068+00:00
---

# NTP server workloads (NTP)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-ntp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  NTP server workloads (NTP) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Root only workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** |  Data changes  
  
## Data changes (CRUD operations)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, ` "user_username": "system:serviceaccount:gpc-system:root-admin-controller-sa"`  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"//apis/system.private.gdc.goog/VERSION/ namespaces/gpc-system/ntpservers/ntp-relay-fhr6t/status"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"patch"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":2022-12-13T13:48:30.014578Z`  
**Source of action** | `_gdch_service_name` |  For example, `"_gdch_service_name": "apiserver"`  
**Outcome** | `responseStatus_code` |  For example, `"responseStatus_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
    "_gdch_cluster": "root-admin",
    "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-w5srk",
    "_gdch_service_name": "apiserver",
    "annotations_authorization_k8s_io_decision":  " allow",
    "annotations_authorization_k8s_io_reason RBAC": allowed by ClusterRoleBinding "root-admin-common-controllers-rolebinding" of ClusterRole "root-admin-common-controllers-role" to ServiceAccount "root-admin-controller-sa/gpc-system",
    "apiGroup"  :  "system.private.gdc.goog",
    "apiVersion":  "audit.k8s.io/v1",
    "auditID": 05e72a29-1b18-4db7-9ded-8f51e3a145d8,
    "cluster": "root-admin",
    "fluentbit_pod":   "anthos-audit-logs-forwarder-w5srk",
    "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "system.private.gdc.goog",
        "apiVersion": "v1alpha1",
        "name": "ntp-relay-fhr6t",
        "namespace": "gpc-system",
        "resource": "ntpservers",
        "subresource":  "status"
      },
    "requestReceivedTimestamp": "2022-12-13T13:48:29.996912Z",
    "requestURI": "/apis/system.private.gdc.goog/v1alpha1/namespaces/gpc-system/ntpservers/ntp-relay-fhr6t/status"
    "responseStatus": {
        "code": 200,
        "metadata": {},
      },
    "service_name": "apiserver",
    "stage": "ResponseComplete",
    "stageTimestamp": "2022-12-13T13:48:30.014578Z",
    "userAgent": "root-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
    "user_uid": "c01df74a-a983-44db-8fd3-e0dae87c0796",
    "user_username": "system:serviceaccount:gpc-system:root-admin-controller-sa",
    "verb": "patch",
    "Time" : "1670939310014",
    "tsNs": "1670939310014791527"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
