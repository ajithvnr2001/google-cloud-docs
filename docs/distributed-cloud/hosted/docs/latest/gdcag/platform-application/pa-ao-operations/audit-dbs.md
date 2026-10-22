---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-dbs/
title: Database Service \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:39.179631+00:00
---

# Database Service  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-dbs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Database Service Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Organization only workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** | 

  * Create a DBClusters resource
  * Update a DBClusters resource
  * Patch a DBClusters resource
  * List DBClusters resources
  * Create a Backup
  * Update a Backup
  * Delete a backup
  * List Backups
  * Create a BackupPlan
  * Update a BackupPlan
  * Delete a BackupPlan
  * List BackupPlans
  * Create an Import
  * Delete an Import
  * List Imports
  * Create an Export
  * Update an Export
  * Delete an Export
  * List Exports
  * Create a Restore
  * Update a Restore
  * Delete a Restore
  * List Restores

  
  
## DBClusters

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User identity** | `user.username` |  For example,
    
    
    "user":{"username":"kubernetes-admin"}
        
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef":{
        "name":"emuv2",
        "namespace":"obs-system",
        "resource":"dbclusters",
        "apiGroup":"postgresql.dbadmin.gdc.goog",
        "apiVersion":"v1"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | 

  * `"verb":"create"`
  * `"verb":"update"`
  * `"verb":"patch"`
  * `"verb":"list"`

  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `sourceIPs` |  For example, `["10.200.0.7"]`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":201
    }  
  
**Other fields** | `annotations` | For example,
    
    
    "annotations":{
    "mutation.webhook.admission.k8s.io/round_0_index_24":
      "{\"configuration\":\"mutating-webhook-configurati on\",\"webhook\":\"mdbcluster.postgresql.dbadmin.gdc.goog\",\"mutated\":true}",
      "authorization.k8s.io/decision": "allow", "authorization.k8s.io/reason":""}
          
  
**Example log**
    
    
    {
      "userAgent": "kubectl/v1.24.2 (linux/amd64) kubernetes/f66044f",
      "apiVersion": "audit.k8s.io/v1",
      "stageTimestamp": "2022-12-02T23:55:23.818903Z",
      "_gdch_cluster": "org-1-admin",
      "level": "Metadata",
      "auditID": "9365cb9f-9403-446a-a88a-f91b88284acf",
      "verb": "create",
      "stage": "ResponseComplete",
      "requestURI": "/a pis/postgresql.dbadmin.gdc.goog/v1/namespaces/obs-system/dbclusters?fieldManager-kubectl -client-side-apply&fieldValidation=Strict",
      "responseStatus": {
        "metadata": {},
        "code": 201
      },
      "annotations": {
        "mutation.webhook.admission.k8s.io/round_0_index_24": "{\"configuration\":\"mutating-webhook-configurati on\",\"webhook\":\"mdbcluster.postgresql.dbadmin.gdc.goog\",\"mutated\":true}",
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": ""
      },
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-t21dm",
      "objectRef": {
        "name": "emuv2",
        "namespace": "obs-system",
        "resource": "dbclusters",
        "apiGrou p": "postgresql.dbadmin.gdc.goog",
        "apiVersion": "v1"
      },
      "sourceIPs": [
        "10.200.0.7"
      ],
      "kind": "Event",
      "user": {
        "username": "kubernetes-admin",
        "groups": [
          "system:masters",
          "system:authenticated"
        ]
      },
      "requestReceivedTimestamp": "2022-12-02T23:55:23.739779Z",
      "_gdch_service_name": "apiserver"
    }
    

## Backup

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User identity** | `user.username` |  For example,
    
    
    "user":{"username":"system:serviceaccount:ods-fleet-system: fleet-controller-manager"}
        
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "postgresql.dbadmin.gdc.goog",
        "apiVersion": "v1",
        "resource": "backups",
        "namespace": "obs-system",
        "resourceVersion": "3189223",
        "name": "backup1",
        "uid": "3b5f6255-9a6d-4556-94b3-9956a5e6c8c2"
      }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | 

  * `"verb":"create"`
  * `"verb":"update"`
  * `"verb":"delete"`
  * `"verb":"list"`

  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `sourceIPs` |  For example, `["10.200.0.7"]`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":200
    }  
  
**Other fields** | `annotations` | For example,
    
    
    "annotations":{
            "authorization.k8s.io/reason": "RBAC: allowed by Cluster RoleBinding \"fleet -manager-rolebinding\" of Cluster Role \"fleet-manager-role\" to ServiceAccount \"fleet-controller-manager/ods-fleet-system\"",
            "authorization.k8s.io/decision": "allow"
        }
          
  
**Example log**
    
    
    {
      "responseStatus": {
        "metadata": {},
        "code": 200
      },
      "_gdch_cluster": "org-1-admin",
      "userAgent": "manager/v0.0.0 (linux/amd64) kubernetes/$Format",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-q2pvd",
      "annotations": {
        "authorization.k8s.io/reason": "RBAC: allowed by Cluster RoleBinding \"fleet -manager-rolebinding\" of Cluster Role \"fleet-manager-role\" to ServiceAccount \"fleet-controller-manager/ods-fleet-system\"",
        "authorization.k8s.io/decision": "allow"
      },
      "requestURI": "/apis/postgresql.dbadmin.gdc.goog/v1/namespaces/obs-system/backups/backup1",
      "kind": "Event",
      "leve 1": "Metadata",
      "verb": "update",
      "apiVersion": "audit.k8s.io/v1",
      "requestReceived Timestamp": "2022-12-03T02:10:57.714186Z",
      "stageTimestamp": "2022-12-03T02:10:57.801287Z",
      "auditID": "9b2721c8-db96-491b-90ce-4771979dceb3",
      "user": {
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:ods -fleet-system",
          "system: authenticated"
        ],
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "fleet-controller-manager-659bc596c4-v6zll"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "6000181a-2050-497e-be3f-313456b88902"
          ]
        },
        "username": "system:serviceaccount:ods-fleet-system: fleet-controller-m anager",
        "uid": "66743ae3-eb0e-4608-9dea-2e6e33da24f1"
      },
      "stage": "ResponseComplete",
      "sourceIPs": [
        "10.253.165.17"
      ],
      "objectRef": {
        "apiGroup": "postgresql.dbadmin.gdc.goog",
        "apiVersion": "v1",
        "resource": "backups",
        "namespace": "obs-system",
        "resourceVersion": "3189223",
        "name": "backup1",
        "ui d": "3b5f6255-9a6d-4556-94b3-9956a5e6c8c2"
      },
      "_gdch_service_name": "apiserver"
    }
    

## BackupPlan

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User identity** | `user.username` |  For example,
    
    
    "user":{"username":"kubernetes-admin", "groups":["system:masters","system:authenticated"]}
        
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "name": "backupplan1",
        "apiGroup": "postgresql.dbadmin.gdc.goog",
        "apiVersion": "v1",
        "namespace": "obs-system",
        "resource": "backupplans"
      }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | 

  * `"verb":"create"`
  * `"verb":"update"`
  * `"verb":"delete"`
  * `"verb":"list"`

  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `sourceIPs` |  For example, `["10.200.0.7"]`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":200
    }  
  
**Other fields** | `annotations` | For example,
    
    
      "annotations": {
        "authorization.k8s.io/reason": "",
        "authorization.k8s.io/deci sion": "allow"
      }
          
  
**Example log**
    
    
    {
      "apiVersion": "audit.k8s.io/v1",
      "stageTimestamp": "2022-12-03T00:13:15.939390Z",
      "requestURI": "/apis/postgresql.dbadmin.gdc.goog/v1/namespaces/obs-system/backupplans?fieldManager-kubectl -client-side-apply&fieldValidation=Strict",
      "kind": "Event",
      "level": "Metadata",
      "auditID": "5841cc4f-74d0-44e3-b8 2b-a84fadaf492b",
      "responseStatus": {
        "metadata": {},
        "code": 201
      },
      "stage": "ResponseComplete",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-9x9pd",
      "userAgent": "kubectl/v1.24.2 (linux/amd64) kubernetes/f66044f",
      "verb": "create",
      "annotations": {
        "authorization.k8s.io/reason": "",
        "authorization.k8s.io/deci sion": "allow"
      },
      "user": {
        "groups": [
          "system:masters",
          "system: authenticated"
        ],
        "username": "kubernetes-admin"
      },
      "_gdch_cluster": "org-1-admin",
      "objectRef": {
        "name": "backupplan1",
        "apiGroup": "postgresql.dbadmin.gdc.goog",
        "apiVersion": "v1",
        "namespace": "obs-system",
        "resource": "backupplans"
      },
      "sourceIPs": [
        "10.200.0.7"
      ],
      "requestReceivedTimestamp": "2022-12-03T00:13:15.921957Z",
      "_gdch_service_name": "apiserver"
    }
    

## Import

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User identity** | `user.username` |  For example,
    
    
    "user":{"groups":["system: masters", "system: authenticated"], "username": "kubernetes-admin"}
        
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
      "objectRef": {
        "resource": "imports",
        "apiVersion": "v1",
        "apiGroup": "postgresql.dbadmin.gdc.goog",
        "name": "import-1",
        "namespace": "obs-system"
      },  
  
**Action** _(Fields containing the performed operation)_ | `verb` | 

  * `"verb":"create"`
  * `"verb":"delete"`
  * `"verb":"list"`

  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-11-11T22:02:02.034688Z"`  
**Source of action** | `sourceIPs` |  For example, `["10.200.0.7"]`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":201
    }  
  
**Other fields** | `annotations` | For example,
    
    
    "annotations": {
      "mutation.webhook.admission.k8s.io/round_@_index_26": "{\"configuration\":\"mutating-webhook-configuration\", \"webhook\":\"import.postgresql.dbadmin.gdc.goog\",\"mutated\":true}",
      "authorization.k8s.io/decision": "allow",
      "authorization.k8s.io/reason": ""
    }
          
  
**Example log**
    
    
    {
      "verb": "create",
      "apiVersion": "audit.k8s.io/v1",
      "requestReceived Timestamp": "2022-12-03T02:22:14.605452Z",
      "requestURI": "/apis/postgresql.dbadmin.gdc.goog/v1/namespaces/obs-system/imports?fieldManager-kubectl -client-side-apply&fieldValidation=Strict",
      "stageTimestamp": "2022-12-03T 02:22:14.637697Z",
      "_gdch_cluster": "org-1-admin",
      "annotations": {
        "mutation.webhook.admission.k8s.io/round_@_index_26": "{\"configuration\":\"mutating-webhook-configuration\", \"webhook\":\"mimport.postgresql.dbadmin.gdc.goog\",\"mutated\":true}",
        "authorization.k8s.io/decision": "allow",
        "a uthorization.k8s.io/reason": ""
      },
      "kind": "Event",
      "level": "Metadata",
      "auditID": "d04e1c23-13fa-4d18-bec7-31d652531151",
      "stage": "ResponseComplete",
      "responseStatus": {
        "metadata": {},
        "code": 201
      },
      "objectRef": {
        "resource": "imports",
        "apiVersion": "v1",
        "apiGroup": "postgresql.dbadmin.gdc.goo g",
        "name": "import-1",
        "namespace": "obs-system"
      },
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-9x9pd",
      "sourceIPs": [
        "10.200.0.7"
      ],
      "user": {
        "groups": [
          "system: masters",
          "system: authenticated"
        ],
        "username": "kubernetes-admin"
      },
      "userAgent": "kubectl/v1.24.2 (linux/amd64) kubernetes/f66044 f",
      "_gdch_service_name": "apiserver"
    }
    

## Export

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User identity** | `user.username` |  For example,
    
    
    "user":{"groups":["system: masters", "system: authenticated"], "username": "kubernetes-admin"}
        
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiVersio n": "v1",
        "apiGroup": "postgresql.dbadmin.gdc.goog",
        "namespace": "obs-system",
        "resource": "exports",
        "name": "export1"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | 

  * `"verb":"create"`
  * `"verb":"update"`
  * `"verb":"delete"`
  * `"verb":"list"`

  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-12-03T07:41:29.462690Z"`  
**Source of action** | `sourceIPs` |  For example, `["10.200.0.7"]`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":201
    }  
  
**Other fields** | `annotations` | For example,
    
    
    "annotations": {
        "authorization.k8s.io/reason": "",
        "mutation.webhook.admission.k8s.io/round_0_index_25": "{\"configuration\":\"mutating-webhook-configuratio n\",\"webhook\":\"mexport.postgresql.dbadmin.gdc.goog\",\"mutated\":true}",
        "authorization.k8s.io/decision": "allow"
    }
          
  
**Example log**
    
    
    {
      "apiVersion": "audit.k8s.io/v1",
      "userAgent": "kubectl/v1.24.2 (linux/amd64) kubernetes/f66044f",
      "requestURI": "/apis/postgresql.dbadmin.gdc.goog/v1/namespaces/obs-system/exports?fieldManager=kubectl-client-side-apply&fieldValidation=Strict",
      "stageTimestamp": "2022-12-03T07:41:29.532729Z",
      "kind": "Event",
      "level": "Metadata",
      "_gdch_cluster": "org-1-admin",
      "stage": "ResponseComplete",
      "_gdc h_fluentbit_pod": "anthos-audit-logs-forwarder-9x9pd",
      "verb": "create",
      "requestReceivedTimestamp": "2022-12-03T07:41:29.462690Z",
      "responseStatus": {
        "code": 201,
        "metadata": {}
      },
      "objectRef": {
        "apiVersio n": "v1",
        "apiGroup": "postgresql.dbadmin.gdc.goog",
        "namespace": "obs-system",
        "resource": "exports",
        "name": "export1"
      },
      "user": {
        "groups": [
          "system:masters",
          "system: authenticated"
        ],
        "username": "kube rnetes-admin"
      },
      "sourceIPs": [
        "10.200.0.7"
      ],
      "annotations": {
        "authorization.k8s.io/reason": "",
        "mutation.webhook.admission.k8s.io/round_0_index_25": "{\"configuration\":\"mutating-webhook-configuratio n\",\"webhook\":\"mexport.postgresql.dbadmin.gdc.goog\",\"mutated\":true}",
        "authorization.k8s.io/decision": "allow"
      },
      "auditID": "2537d860-affd-420d-adec-13a270c1dcb2",
      "_gdch_service_name": "apiserver"
    }
    

## Restore

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User identity** | `user.username` |  For example,
    
    
    "user": {
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:ods- fleet-system",
          "system: authenticated"
        ],
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "fleet-controller-manager-659bc596c4-v6z11"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "6000181a-2050-497e-be3f-313456b88902"
          ]
        },
        "username": "system:serviceaccount:ods-fleet-system: fleet-controller-manager",
        "uid": "6 6743ae3-eb0e-4608-9dea-2e6e33da24f1"
      }
        
  
**Target** _(Fields and values that call the API)_ | `objectRef` |  For example,
    
    
    "objectRef": {
        "apiGroup": "postgresql.dbadmin.gdc.goog",
        "name": "restore1",
        "subresource": "status",
        "uid": "9408379e-7c72-4052-b279-369f6457408a",
        "namespace": "obs-system",
        "apiVersion": "v1",
        "resource": "restores",
        "resourceVersion": "326530"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | 

  * `"verb":"create"`
  * `"verb":"update"`
  * `"verb":"delete"`
  * `"verb":"list"`

  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-12-03T02:33:06.498531Z"`  
**Source of action** | `sourceIPs` |  For example, `["18.253.165.17"]`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
        "metadata":{},
        "code":200
    }  
  
**Other fields** | `annotations` | For example,
    
    
    "annotations": {
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"fleet-manager-rolebinding\" of Cluster Role \"fleet-manager-role\" to Service Account \"fleet-controller-manager/ods-fleet-system\"",
        "authorization.k8s.io/decision": "allow"
      }
          
  
**Example log**
    
    
    {
      "_gdch_cluster": "org-1-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-q2pvd",
      "level": "Metadata",
      "requestURI": "/apis/postgresql.dbadmin.gdc.goog/v1/namespaces/obs-system/restores/restore1/status",
      "kind": "Event",
      "user": {
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:ods- fleet-system",
          "system: authenticated"
        ],
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "fleet-controller-manager-659bc596c4-v6z11"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "6000181a-2050-497e-be3f-313456b88902"
          ]
        },
        "username": "system:serviceaccount:ods-fleet-system: fleet-controller-manager",
        "uid": "6 6743ae3-eb0e-4608-9dea-2e6e33da24f1"
      },
      "annotations": {
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"fleet-manager-rolebinding\" of Cluster Role \"fleet-manager-role\" to Service Account \"fleet-controller-manager/ods-fleet-system\"",
        "authorization.k8s.io/decision": "allow"
      },
      "apiv ersion": "audit.k8s.io/v1",
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "stageTimestamp": "2022-12-03T02:33:06.504990Z",
      "verb": "update",
      "userAgent": "manager/v0.0.0 (linux/amd64) kubernetes/$Format",
      "auditID": "8cd077e4-776f-4179-933c-7e44951a59cf",
      "sourceIPs": [
        "18.253.165.17"
      ],
      "stage": "ResponseComplete",
      "requestReceivedTimestamp": "2022-12-03T02:33:06.498531Z",
      "objectRef": {
        "apiGroup": "postgresql.dbadmin.gdc.goog",
        "name": "restore1",
        "subresource": "status",
        "uid": "9408379e-7c72-4052-b279-369f6457408a",
        "namespace": "obs-system",
        "apiVersion": "v1",
        "resource": "restores",
        "resourceVersion": "326530"
      }
    }```
    
    
          
          
      
      
    
      
        

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
