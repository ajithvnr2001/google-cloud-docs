---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kub/
title: Kubernetes cluster (KUB) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:49.729324+00:00
---

# Kubernetes cluster (KUB)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Kubernetes cluster (KUB) Stay organized with collections  Save and categorize content based on your preferences. 

Audit logs in Google Distributed Cloud (GDC) air-gapped record administrative activity and configuration changes across your Kubernetes clusters. This document lists the tracked operations, payload fields, and example entries for `NodePoolClaim`, `AddressPoolClaim`, `SubnetClaim`, `CIDRClaim`, `Cluster`, and `NodePool` custom resources.

**Workload location** |  Root only workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** | 

  * NodePoolClaim data changes
  * AddressPoolClaim data changes
  * SubnetClaim data changes
  * CIDRClaim data changes
  * Cluster data changes
  * NodePool data changes

  
  
## NodePoolClaim data changes (CRUD operations)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
     "username":"system:serviceaccount:kube-system:
      anthos-cluster-operator-1.13.2"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/apis/baremetal.cluster.gke.io/v1/ namespaces/org-1/nodepoolclaims/admin-control-plane-node-pool/ status"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"update"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-18T23:15:22.882546Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.253.128.74"]`  
**Outcome** | `stage` |  For example, `"stage":"ResponseComplete"`  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
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
        }  
  
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
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \
        "operator-rolebinding-1.13.2\
        "of ClusterRole \"anthos-baremetal-operator-1.13.2\" 
        to ServiceAccount \"anthos-cluster-operator-1.13.2/kube-system\"",
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
      "requestURI": "/apis/baremetal.cluster.gke.io/v1/namespaces/org-1/
                     nodepoolclaims/admin-control-plane-node-pool/status",
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
    

## AddressPoolClaim data changes (CRUD operations)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
     "username":"system:serviceaccount:
      gpc-system:root-admin-controller-sa"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/apis/system.private.gdc.goog/VERSION/ namespaces/org-1/addresspoolclaims/admin-control-plane-node-pool? fieldManager=Organization&force=true"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"patch"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-23T23:24:13.087516Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.128.3.197"]`  
**Outcome** | `stage` |  For example, `"stage":"ResponseComplete"`  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
      "objectRef": {
        "namespace": "org-1",
        "name": "admin-control-plane-node-pool",
        "apiGroup": "system.private.gdc.goog",
        "apiVersion": "VERSION",
        "resource": "addresspoolclaims"
        }  
  
**Example log**
    
    
    {
      "_gdch_cluster": "root-admin",
      "requestReceivedTimestamp": "2022-11-23T23:24:13.087516Z",
      "userAgent": "root-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
      "kind": "Event",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-4hlmv",
      "apiVersion": "audit.k8s.io/v1",
      "level": "Metadata",
      "auditID": "3e46bf8d-fc26-4b43-85fe-34f1f55a0398",
      "requestURI": "/apis/system.private.gdc.goog/VERSION/namespaces/org-1/
        addresspoolclaims/admin-control-plane-node-pool?
        fieldManager=Organization&force=true",
      "stage": "ResponseComplete",
      "user": {
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:gpc-system",
          "system:authenticated"
        ],
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "root-admin-controller-55b54bc95c-wjnwm"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "915f7dcd-e8cb-4a1a-9c53-4b8e2751cf03"
          ]
        },
        "username": "system:serviceaccount:gpc-system:root-admin-controller-sa",
        "uid": "1ddfb03e-0dd5-42df-b8cb-c53a504d9026"
      },
      "verb": "patch",
      "responseStatus": {
        "metadata": {},
        "code": 200
      },
      "objectRef": {
        "namespace": "org-1",
        "name": "admin-control-plane-node-pool",
        "apiGroup": "system.private.gdc.goog",
        "apiVersion": "VERSION",
        "resource": "addresspoolclaims"
      },
      "sourceIPs": [
        "10.128.3.197"
      ],
      "annotations": {
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \
        "root-admin-rootadmin-controllers-rolebinding\" of ClusterRole \
        "root-admin-rootadmin-controllers-role\" to ServiceAccount \"root-admin-controller-sa/
        gpc-system\"",
        "authorization.k8s.io/decision": "allow"
      },
      "stageTimestamp": "2022-11-23T23:24:13.100163Z",
      "_gdch_service_name": "apiserver"
    }
    

## SubnetClaim data changes (CRUD operations)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
     "username":"system:serviceaccount:
                 gatekeeper-system:gatekeeper-admin"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/apis/system.private.gdc.goog/ VERSION/subnetclaims?limit=500"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"list"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-23T23:25:32.726387Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.253.129.191"]`  
**Outcome** | `stage` |  For example, `"stage":"ResponseComplete"`  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
      "objectRef": {
        "resource": "subnetclaims",
        apiVersion": "VERSION",
        "apiGroup": "system.private.gdc.goog"
        }  
  
**Example log**
    
    
    {
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-gc5d7",
      "stageTimestamp": "2022-11-23T23:25:32.733616Z",
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "objectRef": {
        "resource": "subnetclaims",
        "apiVersion": "VERSION",
        "apiGroup": "system.private.gdc.goog"
      },
      "auditID": "b611ebea-4c30-4962-9283-c5dcc95c6e13",
      "verb": "list",
      "kind": "Event",
      "annotations": {
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"gatekeeper-manager-rolebinding\
                                       " of ClusterRole \"gatekeeper-manager-role\" to ServiceAccount \
                                       "gatekeeper-admin/gatekeeper-system\"",
        "authorization.k8s.io/decision": "allow"
      },
      "user": {
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "gatekeeper-audit-b765495d8-4znjd"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "9e515f53-15bf-4570-9c57-2f53e0b69a5d"
          ]
        },
        "uid": "d5dc180d-1bca-4d84-885d-a871e0b6d5a2",
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:gatekeeper-system",
          "system:authenticated"
        ],
        "username": "system:serviceaccount:gatekeeper-system:gatekeeper-admin"
      },
      "stage": "ResponseComplete",
      "userAgent": "gatekeeper/v3.7.0 (linux/amd64) 3ba8e93/2021-11-15T20:59:44Z",
      "requestURI": "/apis/system.private.gdc.goog/VERSION/subnetclaims?limit=500",
      "requestReceivedTimestamp": "2022-11-23T23:25:32.726387Z",
      "sourceIPs": [
        "10.253.129.191"
      ],
      "level": "Metadata",
      "apiVersion": "audit.k8s.io/v1",
      "_gdch_service_name": "apiserver"
    }
    

## CIDRClaim data changes (CRUD operations)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
     "username":"system:serviceaccount:
                 gatekeeper-system:gatekeeper-admin"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/apis/baremetal.cluster.gke.io/ VERSION/addonconfigurations?limit=500"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"list"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-23T23:29:31.952355Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.253.129.191"]`  
**Outcome** | `stage` |  For example, `"stage":"ResponseComplete"`  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
    "objectRef": {
        "apiGroup": "dr.private.gdc.goog",
        "resource": "cidrclaimallocations",
        "apiVersion": "VERSION"
        }  
  
**Example log**
    
    
    {
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-gc5d7",
      "objectRef": {
        "apiGroup": "dr.private.gdc.goog",
        "resource": "cidrclaimallocations",
        "apiVersion": "VERSION"
      },
      "responseStatus": {
        "metadata": {},
        "code": 200
      },
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"gatekeeper-manager-rolebinding\" of ClusterRole \"gatekeeper-manager-role\" to ServiceAccount \"gatekeeper-admin/gatekeeper-system\""
      },
      "stageTimestamp": "2022-11-23T23:26:28.165121Z",
      "kind": "Event",
      "level": "Metadata",
      "auditID": "a21c62ab-6f86-4898-a719-0970e89a031c",
      "user": {
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:gatekeeper-system",
          "system:authenticated"
        ],
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "gatekeeper-audit-b765495d8-4znjd"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "9e515f53-15bf-4570-9c57-2f53e0b69a5d"
          ]
        },
        "username": "system:serviceaccount:gatekeeper-system:gatekeeper-admin",
        "uid": "d5dc180d-1bca-4d84-885d-a871e0b6d5a2"
      },
      "stage": "ResponseComplete",
      "apiVersion": "audit.k8s.io/v1",
      "requestURI": "/apis/dr.private.gdc.goog/VERSION/cidrclaimallocations?limit=500",
      "requestReceivedTimestamp": "2022-11-23T23:26:28.159646Z",
      "verb": "list",
      "sourceIPs": [
        "10.253.129.191"
      ],
      "userAgent": "gatekeeper/v3.7.0 (linux/amd64) 3ba8e93/2021-11-15T20:59:44Z",
      "_gdch_service_name": "apiserver"
    }
    

## Cluster data changes (CRUD operations)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
     "username":"system:serviceaccount:
                 gatekeeper-system:gatekeeper-admin"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/apis/baremetal.cluster.gke.io/ VERSION/addonconfigurations?limit=500"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"list"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-23T23:29:31.952355Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.253.129.191"]`  
**Outcome** | `stage` |  For example, `"stage":"ResponseComplete"`  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
    "objectRef": {
        "apiGroup": "baremetal.cluster.gke.io",
        "resource": "addonconfigurations",
        "apiVersion": "VERSION"
        }  
  
**Example log**
    
    
    {
      "sourceIPs": [
        "10.253.129.191"
      ],
      "stageTimestamp": "2022-11-23T23:29:31.952355Z",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-gc5d7",
      "_gdch_cluster": "root-admin",
      "userAgent": "gatekeeper/v3.7.0 (linux/amd64) 3ba8e93/2021-11-15T20:59:44Z",
      "stage": "RequestReceived",
      "auditID": "3f05e001-38f0-431e-8cc2-61d00d992b6d",
      "kind": "Event",
      "level": "Metadata",
      "apiVersion": "audit.k8s.io/v1",
      "requestURI": "/apis/baremetal.cluster.gke.io/VERSION/addonconfigurations?limit=500",
      "requestReceivedTimestamp": "2022-11-23T23:29:31.952355Z",
      "verb": "list",
      "user": {
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "gatekeeper-audit-b765495d8-4znjd"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "9e515f53-15bf-4570-9c57-2f53e0b69a5d"
          ]
        },
        "uid": "d5dc180d-1bca-4d84-885d-a871e0b6d5a2",
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:gatekeeper-system",
          "system:authenticated"
        ],
        "username": "system:serviceaccount:gatekeeper-system:gatekeeper-admin"
      },
      "objectRef": {
        "apiGroup": "baremetal.cluster.gke.io",
        "resource": "addonconfigurations",
        "apiVersion": "VERSION"
      },
      "_gdch_service_name": "apiserver"
    }
    

## NodePool data changes (CRUD operations)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
     "username":"system:serviceaccount:
                 kube-system:lifecycle-controllers-manager"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/apis/baremetal.cluster.gke.io/v1/nodepools"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"list"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-23T23:29:31.952355Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["2022-11-23T23:28:41.742117Z"]`  
**Outcome** | `stage` |  For example, `"stage":"ResponseComplete"`  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
    "objectRef": {
        "apiGroup": "baremetal.cluster.gke.io",
        "resource": "nodepools",
        "apiVersion": "v1"
        }  
  
**Example log**
    
    
    {
      "requestURI": "/apis/baremetal.cluster.gke.io/v1/nodepools",
      "_gdch_cluster": "root-admin",
      "sourceIPs": [
        "10.253.130.147"
      ],
      "stageTimestamp": "2022-11-23T23:28:41.746854Z",
      "responseStatus": {
        "metadata": {},
        "code": 200
      },
      "annotations": {
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \
                                      "lifecycl-controllers-manager-rolebinding\" 
                                      of ClusterRole \"lifecycle-controllers-manager\
                                      " to ServiceAccount \"lifecycle-controllers-manager/kube-system\"",
        "authorization.k8s.io/decision": "allow"
      },
      "requestReceivedTimestamp": "2022-11-23T23:28:41.742117Z",
      "userAgent": "manager/v0.0.0 (linux/amd64) kubernetes/$Format",
      "kind": "Event",
      "auditID": "c916fab1-a10b-4df8-b680-71ccb5d339ac",
      "user": {
        "extra": {
          "authentication.kubernetes.io/pod-uid": [
            "0b1e3b51-8bdb-4527-8a34-1ae7577cf0aa"
          ],
          "authentication.kubernetes.io/pod-name": [
            "lifecycle-controllers-manager-7495f9dd99-bfvdg"
          ]
        },
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:kube-system",
          "system:authenticated"
        ],
        "username": "system:serviceaccount:kube-system:lifecycle-controllers-manager",
        "uid": "c84957dc-f483-41c4-b0e1-1a2c9cb93dda"
      },
      "stage": "ResponseComplete",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-4hlmv",
      "verb": "list",
      "apiVersion": "audit.k8s.io/v1",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "baremetal.cluster.gke.io",
        "resource": "nodepools",
        "apiVersion": "v1"
      },
      "_gdch_service_name": "apiserver"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
