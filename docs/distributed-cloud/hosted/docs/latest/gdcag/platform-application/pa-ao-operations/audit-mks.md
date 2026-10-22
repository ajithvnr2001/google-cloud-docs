---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-mks/
title: Managed Kubernetes Service (MKS) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:57.236708+00:00
---

# Managed Kubernetes Service (MKS)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-mks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Managed Kubernetes Service (MKS) Stay organized with collections  Save and categorize content based on your preferences. 

Audit logs in Google Distributed Cloud (GDC) air-gapped record create, read, update, and delete (CRUD) activity across your Kubernetes clusters. This document lists the tracked operations, payload fields, and an example entry for `NodePoolClaim`, `AddressPoolClaim`, `SubnetClaim`, `CIDRClaim`, and `NodePool` custom resources.

## CRUD operations

CRUD operations include:

  * `NodePoolClaim` data
  * `AddressPoolClaim` data
  * `SubnetClaim` data
  * `CIDRClaim` data
  * Cluster data
  * `NodePool` data
  * MKS Cluster data



The following table contains an example for `NodePoolClaim` data (CRUD operations):

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  User performing the action: `user.username: system:serviceaccount:kube-system:anthos-cluster-operator-1.13.2` _Full object snippet:_
    
    
    "user":{
      "username": "system:serviceaccount:kube-system:anthos-cluster-operator-1.13.2",
      "uid": "4ebfd4f7-f371-4c40-9f88-ea0709a7039e",
      "groups": [
        "system:serviceaccounts",
        "system:serviceaccounts:kube-system",
        "system:authenticated"
      ],
      "extra": {
         "authentication.kubernetes.io/pod-name": [
           "anthos-cluster-operator-1.13.2-bc6b7467d-22z88"
         ],
         "authentication.kubernetes.io/pod-uid": [
           "004e1b37-6d4d-4959-b77d-0e69dce5ef4a"
         ]
      }
    }  
  
**Target** _(KRM object being acted upon)_ | `objectRef` / `requestURI` |  Specific object reference:
    
    
    "objectRef": {
      "resource": "nodepoolclaims",
      "namespace": "org-1",
      "name": "admin-control-plane-node-pool",
      "apiGroup": "baremetal.cluster.gke.io",
      "apiVersion": "v1",
      "subresource": "status"
    }

Request URI: `/apis/baremetal.cluster.gke.io/v1/namespaces/org-1/nodepoolclaims/admin-control-plane-node-pool/status`  
**Action** _(The CRUD operation performed)_ | `verb` |  Operation performed: `update` _(Other possible values: get, create, apply, patch, delete, list, watch)_  
**Event timestamp** |  `requestReceivedTimestamp` |  `2022-11-23T23:19:42.690064Z`  
**Source of action** | `_gdch_cluster`, `sourceIPs` |  Cluster: `root-admin` Source IP address: `["10.253.128.74"]`  
**Outcome** | `responseStatus`, `stage` |  Stage: `ResponseComplete` Response Status:
    
    
    "responseStatus": {
      "metadata": {},
      "code": 200
    }

_(Code`200` indicates success)_  
**Other useful fields** | `auditID`, `annotations`, _Search Filter_ |  Audit ID: `0539ea3a-b858-4a43-b516-812fc7e80dbd` Annotations include authorization details. _Search Filter:_ `{service_name="apiserver"} |= `"resource":"nodepoolclaims"``  
  
**Example log**
    
    
    {
      "responseStatus": {
        "metadata": {},
        "code": 200
      },
      "_gdch_cluster": "root-admin",
      "sourceIPs": [
        "10.253.128.74"
      ],
      "annotations": {
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"operator-rolebinding-1.13.2\" of ClusterRole \"anthos-baremetal-operator-1.13.2\" to ServiceAccount \"anthos-cluster-operator-1.13.2/kube-system\"",
        "authorization.k8s.io/decision": "allow"
      },
      "requestReceivedTimestamp": "2022-11-23T23:19:42.690064Z",
      "stageTimestamp": "2022-11-23T23:19:42.695372Z",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-4hlmv",
      "apiVersion": "audit.k8s.io/v1",
      "level": "Metadata",
      "user": {
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "anthos-cluster-operator-1.13.2-bc6b7467d-22z88"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "004e1b37-6d4d-4959-b77d-0e69dce5ef4a"
          ]
        },
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:kube-system",
          "system:authenticated"
        ],
        "username": "system:serviceaccount:kube-system:anthos-cluster-operator-1.13.2",
        "uid": "4ebfd4f7-f371-4c40-9f88-ea0709a7039e"
      },
      "stage": "ResponseComplete",
      "requestURI": "/apis/baremetal.cluster.gke.io/v1/namespaces/org-1/nodepoolclaims/admin-control-plane-node-pool/status",
      "kind": "Event",
      "objectRef": {
        "resource": "nodepoolclaims",
        "namespace": "org-1",
        "subresource": "status",
        "name": "admin-control-plane-node-pool",
        "apiVersion": "v1",
        "apiGroup": "baremetal.cluster.gke.io",
        "resourceVersion": "878163",
        "uid": "b2e1bec0-0f7c-4a57-869b-3fcb969ba7e2"
      },
      "verb": "update",
      "userAgent": "operator/v0.0.0 (linux/amd64) kubernetes/$Format",
      "auditID": "0539ea3a-b858-4a43-b516-812fc7e80dbd",
      "_gdch_service_name": "apiserver"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
