---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-mkt/
title: Marketplace (MKT) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:44:09.183788+00:00
---

# Marketplace (MKT)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-mkt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Marketplace (MKT) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Organization only workloads  
---|---  
**Audit log source** |  [KRM API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** | 

  * Creating a Marketplace service
  * Updating a Marketplace service
  * Revoking or granting access to a Marketplace service

  
  
## Creating a Marketplace service

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, ` "username": "system:serviceaccount:gpc-system:mkt-controller"`  
**Target** _(Fields and values that call the API)_ | `apiGroup` |  For example, `"apiGroup": "marketplace.gdc.goog"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  For example, `"verb": "create"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-12-04T03:07:21.657328Z"`  
**Source of action** | `userAgent` |  For example, `"userAgent": "fleet-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-1-admin",
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "c142325e-8dee-4f36-b392-6d4dfe33947f",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "name": "dataproc-service",
        "namespace": "gpc-system",
        "resource": "marketplaceservices",
        "apiGroup": "marketplace.gdc.goog",
        "apiVersion": "v1alpha1"
      },
      "requestReceivedTimestamp": "2022-12-04T03:07:21.657328Z",
      "requestURI": "/apis/marketplace.gdc.goog/v1alpha1/namespaces/gpc-system/marketplaceservices"
      "responseStatus": {
        "code": 201,
        "metadata": {},
      }
       "sourceIPs": [
        "10.53.166.199"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2022-12-04T03:07:21.657328Z",
      "user": {
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "fleet-admin-controller-59cc779bfd-vtx96"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "3f656979-43ea-4012-892c-a595cf94a17b"
          ]
        }
        "username": "system:serviceaccount:gpc-system:mkt-controller",
        "uid": "884009bb-d50c-46a1-a68c-8fa1b91da675"
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:gpc-system",
          "system:authenticated"
        ]
          },
          "userAgent": "fleet-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
          "verb": "create"
    }
    

## Updating a Marketplace service

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, ` "username": "kubernetes-admin"`  
**Target** _(Fields and values that call the API)_ | `apiGroup` |  For example, `"apiGroup": "marketplace.gdc.goog"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  For example, `"verb": "patch"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-12-03T01:09:47.451242Z"`  
**Source of action** | `userAgent` |  For example, `"userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "cluster": "org-1-admin",
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "c142325e-8dee-4f36-b392-6d4dfe33947f",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "name": "dataproc-service",
        "namespace": "gpc-system",
        "resource": "marketplaceservices",
        "apiGroup": "marketplace.gdc.goog",
        "apiVersion": "v1alpha1"
      },
      "requestReceivedTimestamp": "2022-12-04T03:07:21.657328Z",
      "requestURI": "/apis/marketplace.gdc.goog/v1alpha1/namespaces/gpc-system/marketplaceservices/dataproc-service?fieldManager=kubectl-edit"
      "responseStatus": {
        "code": 201,
        "metadata": {},
      }
       "sourceIPs": [
        "10.200.0.6"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2022-12-04T03:07:21.657328Z",
       "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
          ],
          "username": "kubernetes-admin"
          },
          "userAgent": "kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
          "verb": "patch"
    }
    

## Revoking or granting access to a Marketplace service

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username": "fop-platform-admin@example.com"`  
**Target** _(Fields and values that call the API)_ | `apiGroup` |  For example, `"apiGroup": "rbac.authorization.k8s.io"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  For example, `"verb": "create"`  
**Event timestamp** | `time` |  For example, `"time":"2022-12-04T02:00:17.475634Z"`  
**Source of action** | `username` |  For example, `"username": "fop-platform-admin@example.com"`  
**Outcome** | `response_code` |  For example, `"response_code":"201"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "cluster": "org-1-admin",
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "c142325e-8dee-4f36-b392-6d4dfe33947f",
      "impersonatedUser": {
      "groups": [
        "system:authenticated"
        "username": "fop-platform-admin@example.com"
        }
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiVersion": "v1"
        "name": "user-fop-platform-admin--example--com-marketplace-viewer",
        "resource": "clusterrolebindings",
        "apiGroup": "rbac.authorization.k8s.io",
      },
      "requestReceivedTimestamp": "2022-12-04T03:07:21.657328Z",
      "requestURI": "/apis/rbac.authorization.k8s.io/v1/clusterrolebindings"
      "responseStatus": {
        "code": 201,
        "metadata": {},
      }
       "sourceIPs": [
        "10.253.164.220"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2022-12-04T03:07:21.657328Z",
       "user": {
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "fleet-admin-gateway-server-c8b7f879c-zwchc"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "f0ec7e0-a604-4b70-a5fc-793e0c158349"
          ]
          }
        "username": "system:serviceaccount:gpc-system:fleet-admin-gateway-server-sa",
        "uid": "72904c96-d59a-4344-8408-5751f42ffdd88"
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:gpc-system",
          "system:authenticated"
          },
          "userAgent": "ui-gateway-server/v0.0.0 (linux/amd64) kubernetes/$Format",
          "verb": "create"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
