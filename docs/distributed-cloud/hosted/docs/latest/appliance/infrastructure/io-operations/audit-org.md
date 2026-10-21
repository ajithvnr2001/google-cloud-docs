---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-org/
title: Organizations (ORG) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:51.674964+00:00
---

# Organizations (ORG)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-org/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Organizations (ORG) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Root only workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** |  Perform operations on the KRM API Management Plane  
  
## Perform operations on the KRM API Management Plane

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{"uid": "253b9e2f-fde2-4e37-ae7b-36a55d57aafb", "username": "system:serviceaccount: gatekeeper-system: gatekeeper-admin", "extra": {"authentication.kubernet es.io/pod-name": [ "gatekeeper-audit-7fd7bc5d97-x9x8b"], "authentication.kubernetes.io/pod-uid":["e62eaabc-2530-4c36-b793-a98b42c061eb"]}, "groups":["system: serviceaccounts", "system: serviceacc ounts: gatekeeper-system", "system: authenticated"]}  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  For example, `"requestURI":"/apis/resourcemanager.gdc.goog/v1"`  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"list"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-12-06T23:05:22.586546Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.200.0.4"]`  
**Outcome** | `responseStatus` |  For example, `"responseStatus":{"code":200, "metadata":{}}`  
**Other fields** | `annotations` |  For example,
    
    
    "annotations":{"authorization.k8s.io/decision": "allow","authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"gatekeeper-manager-rolebinding\" of ClusterRole \"gatekeeper-manager-role\" to ServiceAccount \"gatekeeper-admin/gatekeeper-system\""}  
  
**Example log**
    
    
    {
       "userAgent":"gatekeeper/v3.7.0 (linux/amd64) 3ba8e93/2021-11-15T20:59:44Z",
       "sourceIPs":[
          "10.200.0.4"
       ],
       "objectRef":{
          "apiGroup":"resourcemanager.gdc.goog",
          "resource":"organizations",
          "apiVersion":"v1alpha1"
       },
       "stageTimestamp":"2022-12-06T23:05:22.590986Z",
       "kind":"Event",
       "apiVersion":"audit.k8s.io/v1",
       "level":"Metadata",
       "auditID":"38da3a00-47b8-424f-8d63-d89258e2043e",
       "requestReceivedTimestamp":"2022-12-06T23:05:22.586546Z",
       "verb":"list",
       "_gdch_cluster":"root-admin",
       "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-2j85z",
       "stage":"ResponseComplete",
       "responseStatus":{
          "code":200,
          "metadata":{}
       },
       "user":{
          "uid":"253b9e2f-fde2-4e37-ae7b-36a55d57aafb",
          "username":"system:serviceaccount:gatekeeper-system:gatekeeper-admin",
          "extra":{
             "authentication.kubernet es.io/pod-name":[
                "gatekeeper-audit-7fd7bc5d97-x9x8b"
             ],
             "authentication.kubernetes.io/pod-uid":[
                "e62eaabc-2530-4c36-b793-a98b42c061eb"
             ]
          },
          "groups":[
             "system:serviceaccounts",
             "system:serviceaccounts:gatekeeper-system",
             "system: authenticated"
          ]
       },
       "requestURI":"/apis/resourcemanager.gdc.goog/v1alpha1/organizations?limit=500",
       "annotations":{
          "authorization.k8s.io/decision":"allow",
          "authorization.k8s.io/reason":"RBAC: allowed by ClusterRoleBinding \"gatekeeper-manager-rolebinding\" of ClusterRole \"gatekeeper-manager-role\" to ServiceAccount \"gatekeeper-admin/gatekeeper-system\""
       },
       "_gdch_service_name":"apiserver"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
