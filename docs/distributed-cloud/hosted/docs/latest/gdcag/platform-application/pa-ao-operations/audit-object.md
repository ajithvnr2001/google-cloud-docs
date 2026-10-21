---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-object/
title: Object storage (OBJ) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:44:11.035819+00:00
---

# Object storage (OBJ)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-object/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Object storage (OBJ) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Object storage  
---|---  
**Audit log source** |  Object storage  
**Audited operations** | 

  * Delete an object
  * Read an object
  * Put an object into a bucket
  * List objects
  * Create a bucket
  * Delete a bucket
  * Read bucket metadata
  * Update bucket metadata
  * Grant and revoke access to a bucket
  * Create a bucket
  * Patch a bucket
  * Delete a bucket

  
  
## Delete an object

**Log type** : Data access.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` | For example, 
    
    
    "message":"{"user":{"identity":"Alice"}}  
  
**Target** _(Fields and values that call the API)_ | `message.action` | For example, 
    
    
    "message":"{"action":"OBJECT_DELETE"}"  
  
**Action** _(Fields containing the performed operation)_ |  `action` |  For example, `"action":"OBJECT_DELETE"`  
**Event timestamp** |  `time` |  For example, `"time":"2022-11-09T15:25:26.781513Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":"{"sourceIPs":["10.21.21.30"]}"  
  
**Outcome** | `message.response` |  For example,
    
    
    "message":"{"response":"SUCS"}"  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log**
    
    
    {
    "pid":"-",
    "msgid":"-",
    "extradata":"-",
    "message":"{
      "time":"2022-11-09T15:25:26.781513Z",
      "auditID":"6a5542fd-cc1e-46b1-aa8d-514c650eba37",
      "user":{"identity":"Alice"},
      "resource":"x1vdn-bucket-for-testing-1",
      "action":"OBJECT_DELETE",
      "description":"{
        "tenantId":"23500289276650416831",
        "storageClass":"standard",
        "workloadType":"user"
        }",
      "sourceIPs":["10.21.21.30"],
      "response":"SUCS",
      "_gdch_org":"org-1-admin"
      }",
    "_gdch_flbProcessedTimestamp":1668007526.781513,
    "time":"2022-11-09T15:25:26.781513Z",
    "pri":"14",
    "_gdch_cluster":"org-1-admin",
    "host":"objectstorage",
    "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-7hwsp",
    "ident":"objectstorage",
    "_gdch_service_name":"admin-audit-logs"
    }
    
    

## Read an object

**Log type** : Data access.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` | For example, 
    
    
    "message":"{"user":{"identity":"Alice"}}  
  
**Target** _(Fields and values that call the API)_ | `message.action` | For example, 
    
    
    "message":"{"action":"OBJECT_READ"}"  
  
**Action** _(Fields containing the performed operation)_ |  `action` |  For example, `"action":"OBJECT_READ"`  
**Event timestamp** |  `time` |  For example, `"time":"2022-11-09T15:25:26.781513Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":"{"sourceIPs":["10.21.21.30"]}"  
  
**Outcome** | `message.response` |  For example,
    
    
    "message":"{"response":"SUCS"}"  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log**
    
    
    {
    "pid":"-",
    "msgid":"-",
    "extradata":"-",
    "message":"{
      "time":"2022-11-09T15:25:26.781513Z",
      "auditID":"6a5542fd-cc1e-46b1-aa8d-514c650eba37",
      "user":{"identity":"Alice"},
      "resource":"x1vdn-bucket-for-testing-1",
      "action":"OBJECT_READ",
      "description":"{
        "objectSize":4,
        "tenantId":"23500289276650416831"
        "storageClass":"standard",
        "workloadType":"user"
        }",
      "sourceIPs":["10.21.21.30"],
      "response":"SUCS",
      "numBytesSent":4
      "_gdch_org":"org-1-admin"
      }",
    "_gdch_flbProcessedTimestamp":1668007526.781513,
    "time":"2022-11-09T15:25:26.781513Z",
    "pri":"14",
    "_gdch_cluster":"org-1-admin",
    "host":"objectstorage",
    "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-7hwsp",
    "ident":"objectstorage",
    "_gdch_service_name":"admin-audit-logs"
    }
    
    

## Put an object into a bucket

**Log type** : Data access.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` | For example, 
    
    
    "message":"{"user":{"identity":"Alice"}}  
  
**Target** _(Fields and values that call the API)_ | `message.action` | For example, 
    
    
    "message":"{"action":"OBJECT_CREATE"}"  
  
**Action** _(Fields containing the performed operation)_ |  `action` |  For example, `"action":"OBJECT_CREATE"`  
**Event timestamp** |  `time` |  For example, `"time":"2022-11-09T15:25:26.781513Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":"{"sourceIPs":["10.21.21.30"]}"  
  
**Outcome** | `message.response` |  For example,
    
    
    "message":"{"response":"SUCS"}"  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log**
    
    
    {
    "pid":"-",
    "msgid":"-",
    "extradata":"-",
    "message":"{
      "time":"2022-11-09T15:25:26.781513Z",
      "auditID":"6a5542fd-cc1e-46b1-aa8d-514c650eba37",
      "user":{"identity":"Alice"},
      "resource":"x1vdn-bucket-for-testing-1",
      "action":"OBJECT_CREATE",
      "description":"{
        "tenantId":"23500289276650416831"
        "storageClass":"standard",
        "workloadType":"user"
        }",
      "sourceIPs":["10.21.21.30"],
      "response":"SUCS",
      "numBytesReceived":4
      "_gdch_org":"org-1-admin"
      }",
    "_gdch_flbProcessedTimestamp":1668007526.781513,
    "time":"2022-11-09T15:25:26.781513Z",
    "pri":"14",
    "_gdch_cluster":"org-1-admin",
    "host":"objectstorage",
    "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-7hwsp",
    "ident":"objectstorage",
    "_gdch_service_name":"admin-audit-logs"
    }
    
    
    

## List objects

**Log type** : Data access.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` | For example, 
    
    
    "message":"{"user":{"identity":"Alice"}}  
  
**Target** _(Fields and values that call the API)_ | `message.action` | For example, 
    
    
    "message":"{"action":"OBJECT_LIST"}"  
  
**Action** _(Fields containing the performed operation)_ |  `action` |  For example, `"action":"OBJECT_LIST"`  
**Event timestamp** |  `time` |  For example, `"time":"2022-11-09T15:25:26.781513Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":"{"sourceIPs":["10.21.21.30"]}"  
  
**Outcome** | `message.response` |  For example,
    
    
    "message":"{"response":"SUCS"}"  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log**
    
    
    {
    "pid":"-",
    "msgid":"-",
    "extradata":"-",
    "message":"{
      "time":"2022-11-09T15:25:26.781513Z",
      "auditID":"6a5542fd-cc1e-46b1-aa8d-514c650eba37",
      "user":{"identity":"Alice"},
      "resource":"x1vdn-bucket-for-testing-1",
      "action":"OBJECT_LIST",
      "description":"{
        "tenantId":"23500289276650416831"
        "storageClass":"standard",
        "workloadType":"user"
        }",
      "sourceIPs":["10.21.21.30"],
      "response":"SUCS",
      "_gdch_org":"org-1-admin"
      }",
    "_gdch_flbProcessedTimestamp":1668007526.781513,
    "time":"2022-11-09T15:25:26.781513Z",
    "pri":"14",
    "_gdch_cluster":"org-1-admin",
    "host":"objectstorage",
    "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-7hwsp",
    "ident":"objectstorage",
    "_gdch_service_name":"admin-audit-logs"
    }
    
    

## Create a bucket

**Log type** : Admin activity.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` | For example, 
    
    
    "message":"{"user":{"identity":"Alice"}}  
  
**Target** _(Fields and values that call the API)_ | `message.action` | For example, 
    
    
    "message":"{"action":"BUCKET_CREATE"}"  
  
**Action** _(Fields containing the performed operation)_ |  `action` |  For example, `"action":"BUCKET_CREATE"`  
**Event timestamp** |  `time` |  For example, `"time":"2022-11-09T15:25:26.781513Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":"{"sourceIPs":["10.21.21.30"]}"  
  
**Outcome** | `message.response` |  For example,
    
    
    "message":"{"response":"SUCS"}"  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log**
    
    
    {
      "pri":"14",
      "time":"2022-11-30T19:21:47.577678Z",
      "host":"obj",
      "ident":"obj",
      "pid":"-",
      "msgid":"-",
      "extradata":"-",
      "message":"{
        "time":"2022-11-30T19:21:47.577678Z","auditID":"d3b0c42c-0a3d-4fc9-951a-c41b863058f2",
        "user":{
          "identity":"objectstorage-tenant-bucket-controller-standard-system-sa"
          },
          "resource":"syism-zakmiller-8-17-22",
          "action":"BUCKET_CREATE",
          "description":"{
            "tenantId":"63704411338737989311",
            "storageClass":"standard",
            "workloadType":"system"
            }",
          "sourceIPs":["10.2.2.34"],
          "response":"SUCS",
          "_gdch_org":"root-admin"
          }",
      "_gdch_cluster":"root-admin","_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-tfvcf","_gdch_service_name":"admin-audit-logs"
    }
    
    

## Delete a bucket

**Log type** : Admin activity.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` | For example, 
    
    
    "message":"{"user":{"identity":"Alice"}}  
  
**Target** _(Fields and values that call the API)_ | `message.action` | For example, 
    
    
    "message":"{"action":"BUCKET_DELETE"}"  
  
**Action** _(Fields containing the performed operation)_ |  `action` |  For example, `"action":"BUCKET_DELETE"`  
**Event timestamp** |  `time` |  For example, `"time":"2022-11-09T15:25:26.781513Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":"{"sourceIPs":["10.21.21.30"]}"  
  
**Outcome** | `message.response` |  For example,
    
    
    "message":"{"response":"SUCS"}"  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log**
    
    
    {
      "pri":"14",
      "time":"2022-11-30T19:21:47.577678Z",
      "host":"obj",
      "ident":"obj",
      "pid":"-",
      "msgid":"-",
      "extradata":"-",
      "message":"{
        "time":"2022-11-30T19:21:47.577678Z","auditID":"d3b0c42c-0a3d-4fc9-951a-c41b863058f2",
        "user":{
          "identity":"objectstorage-tenant-bucket-controller-standard-system-sa"
          },
          "resource":"syism-zakmiller-8-17-22",
          "action":"BUCKET_DELETE",
          "description":"{
            "tenantId":"63704411338737989311",
            "storageClass":"standard",
            "workloadType":"system"
            }",
          "sourceIPs":["10.2.2.34"],
          "response":"SUCS",
          "_gdch_org":"root-admin"
          }",
      "_gdch_cluster":"root-admin","_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-tfvcf","_gdch_service_name":"admin-audit-logs"
    }
    
    

## Read bucket metadata

**Log type** : Admin activity.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` | For example, 
    
    
    "message":"{"user":{"identity":"Alice"}}  
  
**Target** _(Fields and values that call the API)_ | `message.action` | For example, 
    
    
    "message":"{"action":"BUCKET_METADATA_READ"}"  
  
**Action** _(Fields containing the performed operation)_ |  `action` |  For example, `"action":"BUCKET_METADATA_READ"`  
**Event timestamp** |  `time` |  For example, `"time":"2022-11-09T15:25:26.781513Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":"{"sourceIPs":["10.21.21.30"]}"  
  
**Outcome** | `message.response` |  For example,
    
    
    "message":"{"response":"SUCS"}"  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log**
    
    
    {
      "pri":"14",
      "time":"2022-11-30T19:21:47.577678Z",
      "host":"obj",
      "ident":"obj",
      "pid":"-",
      "msgid":"-",
      "extradata":"-",
      "message":"{
        "time":"2022-11-30T19:21:47.577678Z","auditID":"d3b0c42c-0a3d-4fc9-951a-c41b863058f2",
        "user":{
          "identity":"objectstorage-tenant-bucket-controller-standard-system-sa"
          },
          "resource":"syism-zakmiller-8-17-22",
          "action":"BUCKET_METADATA_READ",
          "description":"{
            "tenantId":"63704411338737989311",
            "storageClass":"standard",
            "workloadType":"system"
            }",
          "sourceIPs":["10.2.2.34"],
          "response":"SUCS",
          "_gdch_org":"root-admin"
          }",
      "_gdch_cluster":"root-admin","_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-tfvcf","_gdch_service_name":"admin-audit-logs"
    }
    
    

## Update bucket metadata

**Log type** : Admin activity.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` | For example, 
    
    
    "message":"{"user":{"identity":"Alice"}}  
  
**Target** _(Fields and values that call the API)_ | `message.action` | For example, 
    
    
    "message":"{"action":"BUCKET_METADATA_UPDATE"}"  
  
**Action** _(Fields containing the performed operation)_ |  `action` |  For example, `"action":"BUCKET_METADATA_UPDATE"`  
**Event timestamp** |  `time` |  For example, `"time":"2022-11-09T15:25:26.781513Z"`  
**Source of action** | `message.sourceIPs` |  For example,
    
    
    "message":"{"sourceIPs":["10.21.21.30"]}"  
  
**Outcome** | `message.response` |  For example,
    
    
    "message":"{"response":"SUCS"}"  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log**
    
    
    {
      "pri":"14",
      "time":"2022-11-30T19:21:47.577678Z",
      "host":"obj",
      "ident":"obj",
      "pid":"-",
      "msgid":"-",
      "extradata":"-",
      "message":"{
        "time":"2022-11-30T19:21:47.577678Z","auditID":"d3b0c42c-0a3d-4fc9-951a-c41b863058f2",
        "user":{
          "identity":"objectstorage-tenant-bucket-controller-standard-system-sa"
            },
          "resource":"syism-zakmiller-8-17-22",
          "action":"BUCKET_METADATA_UPDATE",
          "description":"{
            "tenantId":"63704411338737989311",
            "storageClass":"standard",
            "workloadType":"system"
            }",
          "sourceIPs":["10.2.2.34"],
          "response":"SUCS",
          "_gdch_org":"root-admin"
          }",
      "_gdch_cluster":"root-admin","_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-tfvcf","_gdch_service_name":"admin-audit-logs"
    }
    
    

## Grant and revoke access to a bucket

**Log type** : Admin activity.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` | For example, 
    
    
    "user": {"groups": ["system:masters","system:authenticated"], "username":"kubernetes-admin"}  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  For example, `"requestURI":"/apis/rbac.authorization.k8s.io/v1/namespaces/<namespace>/rolebindings?fieldSelector=metadata.name%3D<role-name>"`  
**Action** _(Fields containing the performed operation)_ |  `verb` |  For example, `"verb":"create"`  
**Event timestamp** |  `time` |  For example, `"requestReceivedTimestamp":"2022-11-09T18:53:33.352930Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.21.21.28"]`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{"code":201,"metadata":{}}  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log for granting access**
    
    
    {
    "stageTimestamp":"2022-11-09T18:53:33.421853Z",
    "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-2bqjb",
    "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
    "verb":"create",
    "sourceIPs": ["10.21.21.28"],
    "requestReceivedTimestamp":"2022-11-09T18:53:33.352930Z",
    "requestURI":"/apis/rbac.authorization.k8s.io/v1/namespaces/gpc-system/rolebindings?fieldManager=kubectl-client-side-apply",
    "stage":"ResponseComplete",
    "_gdch_cluster":"org-1-admin",
    "responseStatus":{
    "code":201,
    "metadata":{}
    },
    "user": {
        "groups": ["system:masters","system:authenticated"],
        "username":"kubernetes-admin"
        },
    "objectRef":{
      "name":"alice-can-read",
      "apiGroup":"rbac.authorization.k8s.io",
        "namespace":"gpc-system",
        "resource":"rolebindings",
        "apiVersion":"v1"
            },
    "Annotations":{
            "authorization.k8s.io/reason":"",
            "authorization.k8s.io/decision":"allow"
            },
    "apiVersion":"audit.k8s.io/v1",
    "kind":"Event",
    "auditID":"066660c3-29d8-4cd3-bed8-0727ca1ba7a7",
    "level":"Metadata",
    "_gdch_flbProcessedTimestamp":1668020013.467199,
    "_gdch_service_name":"apiserver"
    }
    
    

**Example log for revoking access**
    
    
    {
    "sourceIPs": ["10.21.21.28"],
    "_gdch_flbProcessedTimestamp":1668020014.507883,
    "level":"Metadata",
    "apiVersion":"audit.k8s.io/v1",
    "auditID":"d0d42688-9e0e-4ed3-9a7f-d3c91c345640",
    "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-5t1tx",
    "kind":"Event",
    "stageTimestamp":"2022-11-09T18:53:33.911438Z",
    "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
    "responseStatus":{
        "Details":{
            "kind":"rolebindings",
            "group":"rbac.authorization.k8s.io",
            "uid":"f00c521a-b65a-b65d-4f08-9082-de7837eda84c",
            "name":"alice-can-read"
            },
            "metadata":{},
            "status":"Success",
            "code":200
            }
    "objectRef":{
        "resource":"rolebindings",
            "namespace":"gpc-system",
            "name":"alice-can-read",
    "apiVersion":"v1",
            "apiGroup":"rbac.authorization.k8s.io"
            },
        "requestURI":"/apis/rbac.authorization.k8s.io/v1/namespaces/gpc/system/rolebindings/alice-can-read",
    "requestReceivedTimestamp":"2022-11-09T18:53:33.773949X",
    "user": {"username":"kubernetes-admin",
        "groups": ["system:masters", "system:authenticated"]
        },
    "annotations": {
            "authorization.k8s.io/reason":"",
            "authorization.k8s.io/decision":"allow"
            },
    "_gdch_cluster":"org-1-admin",
    "stage":"ResponseComplete",
    "verb":"delete",
    "_gdch_service-name":"apiserver"
    }
    
    

## Create a bucket

**Log type** : Admin activity.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` | For example, 
    
    
    "user":{"username":"kubernetes-admin", "groups": ["system:masters","system:authenticated"]}  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  For example, `"requestURI":"/apis/object.gdc.goog/v1/"`  
**Action** _(Fields containing the performed operation)_ |  `verb` |  For example, `"verb":"create"`  
**Event timestamp** |  `time` |  For example, `"requestReceivedTimestamp":"2022-11-09T18:47:18.331288Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.21.21.30"]`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{"metadata":{},"code":201}  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log for creating a bucket**
    
    
    {
    "responseStatus":{"metadata":{},"code":201},
    "_gdch_flbProcessedTimestamp":1668006515.011904,
    "sourceIPs":["10.21.21.28"],
    "stageTimestamp":"2022-11-09T14:48:05.433558Z",
    "apiVersion":"audit.k8s.io/v1",
    "annotations":{
      "authorization.k8.io/reason":"",
      "authorization.k8.io/decision":"allow"
      },
    "objectRef":{
      "apiVersion":"v1",
      "namespace":"bucket-test-2",
      "resource":"buckets",
      "name":"bucket-for-testing-1",
      "apiGroup":"object.gdc.goog"
      },
    "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
    "kind":"Event",
    "level":"Metadata",
    "auditID":"c3b1897a-d1c9-4de8-b5e6-d7875ab3f318",
    "stage":"ResponseComplete",
    "requestURI":"/apis/object.gdc.goog/v1/namespace/bucket-test-2/buckets?fieldManager-kubectl-client-side-apply",
    "requestReceivedTimestamp":"2022-11-09T14:48:05.283425Z",
    "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-5tltx",
    "_gdch_cluster":"org-1-admin",
    "user":{
      "username":"kubernetes-admin",
      "groups": ["system:masters","system:authenticated"]
      },
    "verb":"create",
    "_gdch_service_name":"apiserver"
    }
    
    

## Patch a bucket

**Log type** : Admin activity.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` | For example, 
    
    
    "user":{"username":"kubernetes-admin", "groups": ["system:masters","system:authenticated"]}  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  For example, `"requestURI":"/apis/object.gdc.goog/v1/"`  
**Action** _(Fields containing the performed operation)_ |  `verb` |  For example, `"verb":"patch"`  
**Event timestamp** |  `time` |  For example, `"requestReceivedTimestamp":"2022-11-09T18:47:18.331288Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.21.21.30"]`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{"metadata":{},"code":201}  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log for patching a bucket**
    
    
    {
    "requestReceivedTimestamp":"2022-11-09T18:40:54.0865902",
    "auditID":"c7219d20-64d1-4bfd-85a8-5a2f1b898fa8",
    "sourceIPs":["10.21.21.2 8"],
    "_gdch_flbProcessedTimestamp":1668019271.206281,
    "requestURI":"/apis/object.gdc.goog/v1/namespaces/gpc-system/buckets/buck et-for-testing-1?fieldManager-kubectl -client-side-apply",
    "responseStatus":{"code":200,"metadata":{}},
    "apiVersion":"audit.k8s.io/v 1",
    "objectRef":{
        "namespace":"gpc-system",
        "name":"bucket-for-testing-1",
        "apiVersion":"v1",
        "apiGroup":"object.gdc.goog",
        "resource":"buckets"
          },"
    _gdch_cluster":"org-1-admin",
    "annotations":{"authorization.k8s.io/reason":"","authorization.k8s.io/decision":"allow"},
    "verb":"patch",
    "stageTimestamp":"2022-11-09T18:40:54.1386612",
    "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-5t1tx",
    "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
    "stage":"ResponseComplete",
    "kind":"Event",
    "user":{"username":"kubernetes-admin","groups":["system:masters", "system:authenticated"]},
    "level":"Metadata",
    "_gdch_service_name":"apiserver"
    }
    
    

## Delete a bucket

**Log type** : Admin activity.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` | For example, 
    
    
    "user":{"username":"kubernetes-admin", "groups": ["system:masters","system:authenticated"]}  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  For example, `"requestURI":"/apis/object.gdc.goog/v1/"`  
**Action** _(Fields containing the performed operation)_ |  `verb` |  For example, `"verb":"delete"`  
**Event timestamp** |  `time` |  For example, `"requestReceivedTimestamp":"2022-11-09T18:47:18.331288Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.21.21.30"]`  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{"metadata":{},"code":201}  
  
**Other fields** | Not applicable |  Not applicable  
  
**Example log for deleting a bucket**
    
    
    {
    "level":"Metadata",
    "sourceIPs":["10.21.21.28"],
    "_gdch_flbProcessedTimestamp":1668006515.011904,
    "user":{"username":"kubernetes-admin",
    "groups":["system:masters","system:authenticated"]},
    "apiVersion":"audit.k8s.io/v1",
    "stage":"ResponseComplete",
    "auditID":"afce809c-fc06-4aac-b5af-654c91db6159",
    "responseStatus":{"metadata":{},
        "code":200},
    "stageTimestamp":"2022-11-09T18:47:18.530272Z",
    "objectRef":{
        "namespace":"gpc-system",
        "resource":"buckets",
        "apiVersion":"v1",
        "apiGroup":"object.gdc.goog",
        "name":"bucket-for-testing-1",
      },
    "requestURI":"/apis/object.gdc.goog/v1/namespaces/gpc-system/buckets/bucket-for-testing-1",
        "annotations"{"authorization.k8s.io/reason":"",
        "authorization.k8s.io/decision":"allow"
            },
    "userAgent":"kubectl/v1.23.5 (linux/amd64) kubernetes/c285e78",
    "kind":"Event",
    "_gdch_cluster":"org-1-admin",
    "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-5tltx",
    "requestReceivedTimestamp":"2022-11-09T18:47:18.331288Z",
    "verb":"delete",
    "_gdch_service_name":"apiserver"
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
