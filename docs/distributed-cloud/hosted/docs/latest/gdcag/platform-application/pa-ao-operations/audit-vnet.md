---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-vnet/
title: Virtual networking (VNET) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:46.744679+00:00
---

# Virtual networking (VNET)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-vnet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Virtual networking (VNET) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  File and block storage  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** | 

  * CRUD operations on the project network policy
  * CRUD operations on the load balancer

  
  
## CRUD operations on the project network policy

Log type: KRM API management plane audit logs.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "uid": "6e805ff0-3f8c-4073-b4e1-6a0582ff1263",
      "username": "system:serviceaccount:gpc-system:fleet-admin-controller",
      "extra": {
        "authentication.kubernetes.io/pod-uid": [
          "45ce2b16-3584-448e-8caf-49cb299dfb55"
        ],
        "authentication.kubernetes.io/pod-name": [
          "fleet-admin-controller-5b5d848876-764mt"
        ]
      },
      "groups": [
        "system:serviceaccounts",
        "system:serviceaccounts:gpc-system",
        "system:authenticated"
      ]
    }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI": "/apis/networking.gdc.goog/v1alpha1/namespaces/platform-obs/projectnetworkpolicies"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  For example, `"verb": "patch"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2022-12-09T04:21:55.497089Z"`  
**Source of action** | `sourceIPs` |  For example,
    
    
    "sourceIPs": [
      "10.253.164.215"
    ]  
  
**Outcome** | `stage` |  For example, `"stage": "ResponseComplete"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "auditID": "ff8266f6-685f-4239-9ab8-c55083d575e0",
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "level": "Metadata",
      "requestURI": "/apis/networking.gdc.goog/v1alpha1/namespaces/platform-obs/projectnetworkpolicies/base-policy-allow-intra-project-traffic/status",
      "user": {
        "uid": "6e805ff0-3f8c-4073-b4e1-6a0582ff1263",
        "username": "system:serviceaccount:gpc-system:fleet-admin-controller",
        "extra": {
          "authentication.kubernetes.io/pod-uid": [
            "45ce2b16-3584-448e-8caf-49cb299dfb55"
          ],
          "authentication.kubernetes.io/pod-name": [
            "fleet-admin-controller-5b5d848876-764mt"
          ]
        },
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:gpc-system",
          "system:authenticated"
        ]
      },
      "_gdch_cluster": "org-1-admin",
      "objectRef": {
        "resource": "projectnetworkpolicies",
        "apiGroup": "networking.gdc.goog",
        "name": "base-policy-allow-intra-project-traffic",
        "apiVersion": "v1alpha1",
        "namespace": "platform-obs",
        "subresource": "status"
      },
      "verb": "patch",
      "kind": "Event",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-4267r",
      "stage": "ResponseComplete",
      "apiVersion": "audit.k8s.io/v1",
      "requestReceivedTimestamp": "2022-12-09T04:21:55.497089Z",
      "sourceIPs": [
        "10.253.164.215"
      ],
      "userAgent": "fleet-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
      "stageTimestamp": "2022-12-09T04:21:55.505045Z",
      "annotations": {
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"fleet-admin-controller\" of ClusterRole \"fleet-admin-controller\" to ServiceAccount \"fleet-admin-controller/gpc-system\"",
        "authorization.k8s.io/decision": "allow"
      },
      "_gdch_service_name": "apiserver"
    }
    

## CRUD operations on the load balancer

Log type: KRM API management plane audit logs.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "groups": [
        "system:masters",
        "system:authenticated"
      ],
      "username": "kubernetes-admin"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef.resource` | 
    
    
    "objectRef": {
      "resource": "services"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  For example, `"verb": "get"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2022-12-09T04:29:53.577417Z"`  
**Source of action** | `sourceIPs` |  For example,
    
    
    "sourceIPs": [
      "10.200.0.5"
    ]  
  
**Outcome** | `stage` |  For example, `"stage": "ResponseComplete"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "apiVersion": "audit.k8s.io/v1",
      "level": "Metadata",
      "_gdch_cluster": "org-1-admin",
      "auditID": "113e562b-0576-4b97-bc5f-168a60428f6d",
      "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
      },
      "stageTimestamp": "2022-12-09T04:29:53.579903Z",
      "sourceIPs": [
        "10.200.0.5"
      ],
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": ""
      },
      "stage": "ResponseComplete",
      "requestURI": "/api/v1/namespaces/harbor-system/services/harbor-harbor-harbor-core",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-8kc9n",
      "verb": "get",
      "objectRef": {
        "apiVersion": "v1",
        "apiGroup": "UNKNOWN",
        "resource": "services",
        "namespace": "harbor-system",
        "name": "harbor-harbor-harbor-core"
      },
      "userAgent": "root-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
      "kind": "Event",
      "requestReceivedTimestamp": "2022-12-09T04:29:53.577417Z",
      "_gdch_service_name": "apiserver"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
