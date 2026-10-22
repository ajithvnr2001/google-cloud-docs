---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-add/
title: Add-on manager (ADD) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:56.356524+00:00
---

# Add-on manager (ADD)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Add-on manager (ADD) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Root only workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** |  Data changes  
  
## Data changes (CRUD operations)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
     "username":"system:serviceaccount:kube-system:
       addon-manager-controller-sa"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/apis/addon.private.gdc.goog/VERSION/ namespaces/root/addonsets/root-admin/status"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"patch"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":2022-11-18T23:15:22.882546Z`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.253.132.107"]`  
**Outcome** | `stage` |  For example, `"stage":"RequestReceived"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "kind": "Event",
      "apiVersion": "audit.k8s.io/v1",
      "level": "Metadata",
      "auditID": "8c604d8d-368c-4294-9cfa-e361b4cbbefa",
      "stage": "RequestReceived",
      
      "requestURI": "/apis/addon.private.gdc.goog/VERSION/namespaces/root/addonsets/root-admin/status",
      
      "verb": "patch",
      "user": {
        "username": "system:serviceaccount:kube-system:addon-manager-controller-sa",
        "uid": "43ee00d0-fd9a-48ff-9e74-da11e39144fe",
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:kube-system",
          "system:authenticated"
        ],
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "addon-manager-controller-55cc67bf8f-dr7z7"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "735fc26e-a94a-4c10-a90a-86948cda9eeb"
          ]
        }
      },
      "sourceIPs": [
        "10.253.132.107"
      ],
      "userAgent": "addon-manager-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
      "objectRef": {
        "resource": "addonsets",
        "namespace": "root",
        "name": "root-admin",
        "apiGroup": "addon.private.gdc.goog",
        "apiVersion": "VERSION",
        "subresource": "status"
      },
      "requestReceivedTimestamp": "2022-11-18T23:15:22.882546Z",
      "stageTimestamp": "2022-11-18T23:15:22.882546Z"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
