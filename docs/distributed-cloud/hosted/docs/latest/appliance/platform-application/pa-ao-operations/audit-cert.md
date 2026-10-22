---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-cert/
title: Certificate Manager (CERT) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:18.899977+00:00
---

# Certificate Manager (CERT)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-cert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Certificate Manager (CERT) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Root and organization workloads  
---|---  
**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-kubernetes)  
**Audited operations** | 

  * Create a Certificate
  * Request a Certificate
  * TLS secret

  
  
## Create a Certificate

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
      "username": "system:serviceaccount:kube-system:metrics-server-operator"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI": "/apis/cert-manager.io/v1/namespaces/gke-managed-metrics-server/ certificates/metrics-server-cert"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb": "get"`  
**Event timestamp** |  `ts` |  For example, `"requestReceivedTimestamp": "2023-01-19T18:25:29.964302Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs": "10.253.128.143"`  
**Outcome** | `stage` |  For example,
    
    
    "stage": "ResponseComplete"
      }  
  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
    "kind": "Event"
    "objectRef": {
        "namespace": "gke-managed-metrics-server",
        "apiGroup": "cert-manager.io",
        "resource": "certificates",
        "name": "metrics-server-cert",
        "apiVersion": "v1"
      }  
  
**Example log**
    
    
    {
      "objectRef": {
        "namespace": "gke-managed-metrics-server",
        "apiGroup": "cert-manager.io",
        "resource": "certificates",
        "name": "metrics-server-cert",
        "apiVersion": "v1"
      },
      "_gdch_service_name": "apiserver",
      "_gdch_tenant_id": "infra-obs",
      "kind": "Event",
      "requestURI": "/apis/cert-manager.io/v1/namespaces/gke-managed-metrics-server/certificates/metrics-server-cert",
      "requestReceivedTimestamp": "2023-01-19T18:25:29.964302Z",
      "auditID": "7190b768-89fa-4fbf-9413-77f273f537d8",
      "stageTimestamp": "2023-01-19T18:25:29.966946Z",
      "user": {
        "uid": "41e7bf0b-fc7b-4fdb-b8df-b6b58b896831",
        "extra": {
          "authentication.kubernetes.io/pod-uid": [
            "b5ea1eeb-95d9-4845-85c5-1fcd2c3d1f9e"
          ],
          "authentication.kubernetes.io/pod-name": [
            "metrics-server-operator-76fcd579d7-gp5df"
          ]
        },
        "username": "system:serviceaccount:kube-system:metrics-server-operator",
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:kube-system",
          "system:authenticated"
        ]
      },
      "level": "Metadata",
      "annotations": {
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"metrics-server-operator\" of ClusterRole \"metrics-server-operator\" to ServiceAccount \"metrics-server-operator/kube-system\"",
        "authorization.k8s.io/decision": "allow"
      },
      "stage": "ResponseComplete",
      "userAgent": "manager/v0.0.0 (linux/amd64) kubernetes/$Format",
      "responseStatus": {
        "metadata": {},
        "code": 200
      },
      "sourceIPs": [
        "10.253.128.143"
      ],
      "verb": "get",
      "apiVersion": "audit.k8s.io/v1",
      "_gdch_org_name": "root",
      "_gdch_org_id": "root.zone1.google.gdch.test",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-zthjs"
    }
    

## Request a certificate

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
      "username": "system:serviceaccount:gatekeeper-system:gatekeeper-admin"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI": "/apis/cert-manager.io/v1/certificaterequests?limit=500"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb": "list"`  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2023-01-19T18:30:11.574690Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":["10.253.128.74"]`  
**Outcome** | `responseStatus.code` |  For example,
    
    
    "responseStatus":{
      "code":200
      }  
  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
    "kind": "Event",
    "objectRef": {
        "apiGroup": "cert-manager.io",
        "resource": "certificaterequests",
        "apiVersion": "v1"
      }  
  
**Example log**
    
    
    {
      "objectRef": {
        "apiGroup": "cert-manager.io",
        "resource": "certificaterequests",
        "apiVersion": "v1"
      },
      "_gdch_service_name": "apiserver",
      "_gdch_tenant_id": "infra-obs",
      "kind": "Event",
      "requestURI": "/apis/cert-manager.io/v1/certificaterequests?limit=500",
      "responseStatus": {
        "metadata": {},
        "code": 200
      },
      "apiVersion": "audit.k8s.io/v1",
      "stage": "ResponseComplete",
      "verb": "list",
      "level": "Metadata",
      "requestReceivedTimestamp": "2023-01-19T18:30:11.574690Z",
      "auditID": "dda83584-94dc-4388-bb68-ffa932d94e85",
      "stageTimestamp": "2023-01-19T18:30:11.641010Z",
      "annotations": {
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"gatekeeper-manager-rolebinding\" of ClusterRole \"gatekeeper-manager-role\" to ServiceAccount \"gatekeeper-admin/gatekeeper-system\"",
        "authorization.k8s.io/decision": "allow"
      },
      "sourceIPs": [
        "10.253.128.74"
      ],
      "userAgent": "gatekeeper/v3.7.0 (linux/amd64) 3ba8e93/2021-11-15T20:59:44Z",
      "user": {
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "gatekeeper-audit-5f8c9cc9bf-sjbfr"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "dc956543-76d9-4654-a757-4f4a11c38fa7"
          ]
        },
        "uid": "af529d1d-7139-4afc-b8fd-380218e344b7",
        "username": "system:serviceaccount:gatekeeper-system:gatekeeper-admin",
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:gatekeeper-system",
          "system:authenticated"
        ]
      },
      "_gdch_org_name": "root",
      "_gdch_org_id": "root.zone1.google.gdch.test",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-zthjs"
    }
    

## TLS secret

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user.username` |  For example,
    
    
    "user":{
      "username": "kubernetes-admin"
      }  
  
**Target** _(Fields and values that call the API)_ | `requestURI` |  `"requestURI": "/api/v1/namespaces/istio-system/secrets/web-tls"`  
**Action** _(Fields containing the performed operation)_ | `verb` |  `"verb": "get"`  
**Event timestamp** |  `stageTimestamp` |  For example, `"stageTimestamp": "2023-01-19T18:37:17.571558Z"`  
**Source of action** | `sourceIPs` |  For example, `"sourceIPs":[""10.200.0.2""]`  
**Outcome** | `responseStatus.code` |  For example,
    
    
    "requestReceivedTimestamp": "2023-01-19T18:37:17.568664Z"
      }  
  
**Other fields** | 

  * `kind`
  * `objectRef`

|  For example,
    
    
    "kind": "Event",
    "objectRef": {
        "namespace": "istio-system",
        "apiVersion": "v1",
        "name": "web-tls",
        "apiGroup": "UNKNOWN",
        "resource": "secrets"
      }  
  
**Example log**
    
    
    {
      "objectRef": {
        "namespace": "istio-system",
        "apiVersion": "v1",
        "name": "web-tls",
        "apiGroup": "UNKNOWN",
        "resource": "secrets"
      },
      "auditID": "83d2c117-fb8b-4dfe-9a16-413c084162c0",
      "_gdch_service_name": "apiserver",
      "_gdch_tenant_id": "infra-obs",
      "kind": "Event",
      "requestURI": "/api/v1/namespaces/istio-system/secrets/web-tls",
      "stageTimestamp": "2023-01-19T18:37:17.571558Z",
      "verb": "get",
      "user": {
        "username": "kubernetes-admin",
        "groups": [
          "system:masters",
          "system:authenticated"
        ]
      },
      "level": "Metadata",
      "sourceIPs": [
        "10.200.0.2"
      ],
      "apiVersion": "audit.k8s.io/v1",
      "responseStatus": {
        "metadata": {},
        "code": 200
      },
      "stage": "ResponseComplete",
      "requestReceivedTimestamp": "2023-01-19T18:37:17.568664Z",
      "userAgent": "k9s/v0.0.0 (linux/amd64) kubernetes/$Format",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": ""
      },
      "_gdch_org_name": "root",
      "_gdch_org_id": "root.zone1.google.gdch.test",
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-zthjs"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
