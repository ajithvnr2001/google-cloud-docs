---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-rm/
title: Resource Manager (RM) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:45.265583+00:00
---

# Resource Manager (RM)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-rm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Resource Manager (RM) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Root and organization workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** | 

  * KRM API Management Plane Audit Logs (Project)

  
  
## KRM API Management Plane Audit Logs (Project)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example,
    
    
    "username":system:serviceaccount:gpc-system:fleet-admin-controller"
        
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"apis/resourcemanager.gdc.goog/v1/namespaces/ gpc-system/projects/istio-system`  
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
          "apiVersion": "v1",
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
          "apiVersion": "v1",
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
        "requestURI": "/apis/resourcemanager.gdc.goog/v1/namespaces/gpc-system/projects/istio-system",
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
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
