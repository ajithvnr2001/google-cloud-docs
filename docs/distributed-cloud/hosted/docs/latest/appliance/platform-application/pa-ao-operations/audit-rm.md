---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-rm/
title: Resource manager (RM) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:08.937333+00:00
---

# Resource manager (RM)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-rm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Resource manager (RM) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Root and organization workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** | 

  * KRM API Management Plane Audit Logs (Project)
  * KRM API Management Plane Audit Logs (Project RBAC - ProjectRole)
  * KRM API Management Plane Audit Logs (Project RBAC - ProjectRoleBinding)

  
  
## KRM API Management Plane Audit Logs (Project)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example,
    
    
    "username":system:serviceaccount:gpc-system:fleet-admin-controller"
        
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"apis/resourcemanager.gdc.goog/v1alpha1/namespaces/ gpc-system/projects/istio-system`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"update"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, ` "requestReceivedTimestamp": "2022-12-22T15:46:41.028873Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.253.128.178"],`  
**Outcome** | `stage` |  For example,
    
    
    "stage": "ResponseComplete"  
  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
    "kind": "Event",
    "objectRef": {
          "name": "istio-system",
          "apiVersion": "v1alpha1",
          "apiGroup": "resourcemanager.gdc.goog",
          "resourceVersion": "7812139",
          "resource": "projects",
          "uid": "7d3a3bb1-a0be-4c5c-980b-f9cd3632f6e3",
          "namespace": "gpc-system"
      },  
  
**Example log**
    
    
    {
        "stage": "ResponseComplete",
        "apiVersion": "audit.k8s.io/v1",
        "objectRef": {
          "name": "istio-system",
          "apiVersion": "v1alpha1",
          "apiGroup": "resourcemanager.gdc.goog",
          "resourceVersion": "7812139",
          "resource": "projects",
          "uid": "7d3a3bb1-a0be-4c5c-980b-f9cd3632f6e3",
          "namespace": "gpc-system"
        },
        "requestReceivedTimestamp": "2022-12-22T15:46:41.028873Z",
        "sourceIPs": [
          "10.253.128.178"
        ],
        "annotations": {
          "authorization.k8s.io/decision": "allow",
          "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"fleet-admin-common-controller\" of ClusterRole \"fleet-admin-common-controllers-role\" to ServiceAccount \"fleet-admin-controller/gpc-system\"",
          "mutation.webhook.admission.k8s.io/round_0_index_5": "{\"configuration\":\"gatekeeper-mutating-webhook-configuration\",\"webhook\":\"mutation.gatekeeper.sh\",\"mutated\":false}"
        },
        "_gdch_cluster": "root-admin",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-t4rld",
        "user": {
          "uid": "da8e839f-eca4-4a96-9058-94fa4202824f",
          "extra": {
            "authentication.kubernetes.io/pod-uid": [
              "09335650-82b0-451c-83e2-f8157e9d518c"
            ],
            "authentication.kubernetes.io/pod-name": [
              "fleet-admin-controller-75dbdf7659-ccfrn"
            ]
          },
          "groups": [
            "system:serviceaccounts",
            "system:serviceaccounts:gpc-system",
            "system:authenticated"
          ],
          "username": "system:serviceaccount:gpc-system:fleet-admin-controller"
        },
        "stageTimestamp": "2022-12-22T15:46:41.119767Z",
        "kind": "Event",
        "verb": "update",
        "requestURI": "/apis/resourcemanager.gdc.goog/v1alpha1/namespaces/gpc-system/projects/istio-system",
        "responseStatus": {
          "metadata": {},
          "code": 200
        },
        "userAgent": "fleet-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
        "auditID": "5aeaeab6-7371-4b63-8355-b4469e1440bb",
        "level": "Metadata",
        "_gdch_service_name": "apiserver",
        "_gdch_tenant_id": "infra-obs"
      }
    

## KRM API Management Plane Audit Logs (Project RBAC - ProjectRole)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example,
    
    
    "username": "system:serviceaccount:
    gpc-system:fleet-admin-controller"
         
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI":"/apis/resourcemanager.gdc.goog/ v1alpha1/namespaces/vm-prober-system-obs-system/ projectroles/service-now-admin/status"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"update"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2022-12-21T23:36:45.808663Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.253.128.178"]`  
**Outcome** | `stage` |  For example,
    
    
      "stage": "ResponseComplete"
       
  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
    "kind": "Event",
    "objectRef": {
       "apiVersion": "v1alpha1",
       "namespace": "vm-prober-system-obs-system",
       "resourceVersion": "5573513",
       "apiGroup": "resourcemanager.gdc.goog",
       "resource": "projectroles",
       "name": "service-now-admin",
       "subresource": "status",
       "uid": "c220806d-a708-4e42-8a2c-8442b6a74038"
    },  
  
**Example log**
    
    
    {
        "verb": "update",
        "responseStatus": {
          "metadata": {},
          "code": 200
        },
        "objectRef": {
          "apiVersion": "v1alpha1",
          "namespace": "vm-prober-system-obs-system",
          "resourceVersion": "5573513",
          "apiGroup": "resourcemanager.gdc.goog",
          "resource": "projectroles",
          "name": "service-now-admin",
          "subresource": "status",
          "uid": "c220806d-a708-4e42-8a2c-8442b6a74038"
        },
        "apiVersion": "audit.k8s.io/v1",
        "sourceIPs": [
          "10.253.128.178"
        ],
        "kind": "Event",
        "requestURI": "/apis/resourcemanager.gdc.goog/v1alpha1/namespaces/vm-prober-system-obs-system/projectroles/service-now-admin/status",
        "auditID": "e40537d8-0e49-4f34-85b3-f6bb5c373a58",
        "_gdch_cluster": "root-admin",
        "annotations": {
          "authorization.k8s.io/decision": "allow",
          "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"fleet-admin-controller\" of ClusterRole \"fleet-admin-controller\" to ServiceAccount \"fleet-admin-controller/gpc-system\""
        },
        "stageTimestamp": "2022-12-21T23:36:45.814414Z",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-t4rld",
        "level": "Metadata",
        "stage": "ResponseComplete",
        "userAgent": "fleet-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
        "requestReceivedTimestamp": "2022-12-21T23:36:45.808663Z",
        "user": {
          "extra": {
            "authentication.kubernetes.io/pod-name": [
              "fleet-admin-controller-75dbdf7659-ccfrn"
            ],
            "authentication.kubernetes.io/pod-uid": [
              "09335650-82b0-451c-83e2-f8157e9d518c"
            ]
          },
          "groups": [
            "system:serviceaccounts",
            "system:serviceaccounts:gpc-system",
            "system:authenticated"
          ],
          "username": "system:serviceaccount:gpc-system:fleet-admin-controller",
          "uid": "da8e839f-eca4-4a96-9058-94fa4202824f"
        },
        "_gdch_service_name": "apiserver",
        "_gdch_tenant_id": "infra-obs"
      }
    

## KRM API Management Plane Audit Logs (Project RBAC - ProjectRoleBinding)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example,
    
    
    "username": "system:serviceaccount:
    gatekeeper-system:gatekeeper-admin"
        
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"/apis/resourcemanager.gdc.goog/ v1alpha1/projectrolebindings?limit=500"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb":"list"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, ` "requestReceivedTimestamp": "2022-12-06T23:03:32.904478Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.253.165.69"],`  
**Outcome** | `stage` |  For example,
    
    
    "stage": "RequestReceived"  
  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
    "kind": "Event",
    "objectRef": {
        "resource": "projectrolebindings",
        "apiVersion": "v1alpha1",
        "apiGroup": "resourcemanager.gdc.goog"
      },  
  
**Example log**
    
    
    {
      "verb": "list",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-t4rld",
      "userAgent": "gatekeeper/v3.7.0 (linux/amd64) 3ba8e93/2021-11-15T20:59:44Z",
      "objectRef": {
        "apiVersion": "v1alpha1",
        "resource": "projectrolebindings",
        "apiGroup": "resourcemanager.gdc.goog"
      },
      "sourceIPs": [
        "10.253.128.219"
      ],
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "kind": "Event",
      "stage": "ResponseComplete",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"gatekeeper-manager-rolebinding\" of ClusterRole \"gatekeeper-manager-role\" to ServiceAccount \"gatekeeper-admin/gatekeeper-system\""
      },
      "requestURI": "/apis/resourcemanager.gdc.goog/v1alpha1/projectrolebindings?limit=500",
      "user": {
        "uid": "d23f8b07-b318-47fb-a81d-9932e81c3be8",
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:gatekeeper-system",
          "system:authenticated"
        ],
        "extra": {
          "authentication.kubernetes.io/pod-uid": [
            "86ab2ec3-93ae-49b6-9feb-cadae6d014c4"
          ],
          "authentication.kubernetes.io/pod-name": [
            "gatekeeper-audit-54d846f776-z6bzn"
          ]
        },
        "username": "system:serviceaccount:gatekeeper-system:gatekeeper-admin"
      },
      "stageTimestamp": "2022-12-21T23:11:57.899640Z",
      "auditID": "e8d0d02b-f309-4127-8cdb-e93a39ebaea7",
      "apiVersion": "audit.k8s.io/v1",
      "level": "Metadata",
      "_gdch_cluster": "root-admin",
      "requestReceivedTimestamp": "2022-12-21T23:11:57.897447Z",
      "_gdch_service_name": "apiserver",
      "_gdch_tenant_id": "infra-obs"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
