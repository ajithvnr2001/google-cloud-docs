---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-serv/
title: Physical servers (SERV) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:50.544533+00:00
---

# Physical servers (SERV)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-serv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Physical servers (SERV) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Organization only workloads  
---|---  
**Audit log source** | 

  * Physical servers
  * Server custom resources

  
**Audited operations** | 

  * Machine events
  * Data changes (CRUD operations)

  
  
## Machine events

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `gdch_service_name` |  For example,
    
    
    "_gdch_service_name": "bm_nodes"
        
  
**Target** _(Fields and values that call the API)_ | `description` |  ` "description": "The overall security state of the system is at \"Risk\"`  
**Action** _(Fields containing the performed operation)_ | `description` |  ` "description": "The overall security state of the system is at \"Risk\"`  
**Event timestamp** |  `time` |  For example, `"time": "2022-12-02T16:06:29Z"`  
**Source of action** | `resource` |  For example, `"resource": "zb-ab-bm07"`  
**Outcome** | _Not applicable_ | _Not applicable_  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "description": "The overall security state of the system is at \"Risk\".",
      "_gdch_service_name": "bm_nodes",
      "resource": "zb-ab-bm07",
      "auditID": "IEL#32321",
      "user": {},
      "time": "2022-12-02T16:06:29Z",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-5k8l2"
    }
    
    

## Data changes (CRUD operations)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example,
    
    
    "user":{
     "username":"system:serviceaccount:
     gpc-system:root-admin-controller-sa"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/apis/system.private.gdc.goog/v1alpha1/ namespaces/gpc-system/servers/zb-aa-bm07/status"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"patch"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-12-02T23:52:22.509246Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.251.127.4"]`  
**Outcome** | `responseStatus` |  For example, `"responseStatus":{"metadata":{},"code":200}`  
**Other fields** | 

  * `annotations`
  * `objectRef`

|  For example,
    
    
     "objectRef":{
    "resource":"servers",
    "apiGroup":
    "system.private.gdc.goog",
    "name":"zb-aa-bm07",
    "apiVersion":"v1alpha1",
    "namespace":"gpc-system",
    "subresource":"status"
        }  
  
**Example log**
    
    
    {
    "user":{
    "groups":["system:serviceaccounts","system:serviceaccounts:gpc-system"
    "system:authenticated"]
    "extra":{"authentication.kubernetes.io/pod-uid":["8a33590d-bbf2-4a23-b5de-851a451fac32"],
    "authentication.kubernetes.io/pod-name":["root-admin-controller-5c5d44f45-2r5d4"]
    },
    "username":"system:serviceaccount:gpc-system:root-admin-controller-sa",
    "uid":"ecaee5a1-f7e0-47e7-ae46-1cbd42fb2e99"
    },
    "requestURI":"/apis/system.private.gdc.goog/v1alpha1/namespaces/gpc-system/servers/zb-aa-bm07/status",
    "sourceIPs":["10.251.127.4"],
    "verb":"patch",
    "userAgent":"root-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
    "requestReceivedTimestamp":"2022-12-02T23:52:22.509246Z",
    "stageTimestamp":"2022-12-02T23:52:22.527613Z",
    "_gdch_cluster":"root-admin",
    "responseStatus":{"metadata":{},"code":200},
    "annotations":{
    "authorization.k8s.io/reason":"RBAC: allowed by ClusterRoleBinding \
    "root-admin-rootadmin-controllers-rolebinding\" of ClusterRole \
    "root-admin-rootadmin-controllers-role\" to ServiceAccount \
    "root-admin-controller-sa/gpc-system\"","authorization.k8s.io/decision":"allow"
    },
    "objectRef":{
    "resource":"servers",
    "apiGroup":
    "system.private.gdc.goog",
    "name":"zb-aa-bm07",
    "apiVersion":"v1alpha1",
    "namespace":"gpc-system",
    "subresource":"status"
    },
    "gdch_fluentbit_pod":"anthos-audit-logs-forwarder-kp68x",
    "kind":"Event",
    "apiVersion":"audit.k8s.io/v1",
    "stage":"ResponseComplete",
    "level":"Metadata",
    "auditID":"2b2b0ec8-627b-4f69-aa19-b6ba2c3e20cb",
    "_gdch_service_name":"apiserver"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
