---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-dhcp/
title: Dynamic Host Configuration Protocol (DHCP) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:22.616920+00:00
---

# Dynamic Host Configuration Protocol (DHCP)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-dhcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Dynamic Host Configuration Protocol (DHCP) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Root only workloads  
---|---  
**Audit log source** | [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** | CRUD operations to the DHCP config  
  
## CRUD operations to the DHCP config

The CRUD operations include data changes to the DHCP config logged in the audit log server.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `userAgent`, `user_name` |  For example,
    
    
    "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
    "user": {
      "username": "kubernetes-admin"
    }
              
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  For example,
    
    
    "requestURI": "/api/v1/namespaces/gpc-system/configmaps/gpc-dhcp-conf?fieldManager=kubectl-edit"
              
  
**Action** _(Fields containing the performed operation)_ | `verb` |  For example, ` "verb": "patch" `  
**Event timestamp** | `requestReceivedTimestamp` |  For example, ` "requestReceivedTimestamp": "2022-12-13T06:59:55.681994Z" `  
**Source of action** | `_gdch_service_name` |  For example,
    
    
     "_gdch_service_name": "apiserver"
              
  
**Outcome** | `code` |  For example,
    
    
    "responseStatus": {
        "code": 200,
      }
              
  
**Example log**
    
    
    {
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-2z87b",
      "_gdch_service_name": "apiserver",
      "annotations": {
        "authorization_k8s_io_decision": "allow",
        "authorization_k8s_io_reason": ""
      },
      "apiGroup": "UNKNOWN",
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "8841cec6-1557-4278-8ba2-1f89b7953a81",
      "cluster": "root-admin",
      "auditID": "069120c2-c182-4e8f-b863-9c640885bf2b",
      "fluentbit_pod": "anthos-audit-logs-forwarder-2z87b",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "UNKNOWN",
        "apiVersion": "v1",
        "name": "gpc-dhcp-conf",
        "namespace": "gpc-system",
        "resource": "configmaps"
      },
      "requestReceivedTimestamp": "2022-12-13T06:59:55.681994Z",
      "requestURI": "/api/v1/namespaces/gpc-system/configmaps/gpc-dhcp-conf?fieldManager=kubectl-edit",
      "responseStatus": {
        "code": 200
      },
      "service_name": "apiserver",
      "stage": "ResponseComplete",
      "stageTimestamp": "2022-12-13T06:59:55.699551Z",
      "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
      "user": {
        "username": "kubernetes-admin"
      },
      "verb": "patch",
      "Detected": "fields",
      "Time": "1670915285440",
      "tsNs": "1670915285440328017"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
