---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-inv/
title: Inventory Management \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:50.983878+00:00
---

# Inventory Management  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/audit-inv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Inventory Management Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Root only workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** |  Data changes (CRUD operations)  
  
## Data changes (CRUD operations)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "username": "kubernetes-admin",
      "groups":["system:masters","system:authenticated"]
    }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` | `"requestURI": "/apis/system.private.gdc.goog/v1alpha1/namespaces/gpc-system/spareparts"`  
**Action** _(Fields containing the performed operation)_ | `verb` | `"verb":"create"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-12-22T00:28:24.763163Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.200.0.2"]`  
**Outcome** | `responseStatus` |  For example, `"responseStatus":{"code":201,"metadata":{}}`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
       "verb":"create",
       "user":{
          "username":"kubernetes-admin",
          "groups":[
             "system:masters",
             "system:authenticated"
          ]
       },
       "sourceIPs":[
          "10.200.0.2"
       ],
       "annotations":{
          "authorization.k8s.io/decision":"allow",
          "mutation.webhook.admission.k8s.io/round_0_index_2":"{\"configuration\":\"gatekeeper-mutating-webhook-configuration\",\"webhook\":\"mutation.gatekeeper.sh\",\"mutated\":false}",
          "authorization.k8s.io/reason":""
       },
       "requestReceivedTimestamp":"2022-12-22T00:28:24.763163Z",
       "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-swcss",
       "responseStatus":{
          "code": 201,
          "metadata":{}
       },
       "objectRef":{
          "namespace":"gpc-system",
          "apiGroup":"system.private.gdc.goog",
          "resource":"spareparts",
          "name":"p06186-001-1234569087a",
          "apiVersion":"v1alpha1"
       },
       "apiVersion":"audit.k8s.io/v1",
       "_gdch_cluster":"root-admin",
       "level":"Metadata",
       "requestURI":"/apis/system.private.gdc.goog/v1alpha1/namespaces/gpc-system/spareparts?fieldManager=kubectl-client-side-apply",
       "auditID":"d9aa524b-0654-4e57-813f-b176a24244f1",
       "stageTimestamp":"2022-12-22T00:28:24.779255Z",
       "stage":"ResponseComplete",
       "userAgent":"kubectl/v1.22.9 (darwin/amd64) kubernetes/2b63bf7",
       "kind":"Event",
       "_gdch_service_name":"apiserver",
       "_gdch_tenant_id":"infra-obs"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
