---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-opa/
title: OPA Gatekeeper (OPA) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:12:05.050820+00:00
---

# OPA Gatekeeper (OPA)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-opa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  OPA Gatekeeper (OPA) Stay organized with collections  Save and categorize content based on your preferences. 

## All operations through the Kubernetes API

**Log schema** : KRM API

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` | 
    
    
    "user": {
      "groups": [
        "system:authenticated"
      ],
      "username": "fop-platform-admin@example.com"
    },
    "annotations": {
      "authorization.k8s.io/decision": "allow",
      "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"project-creator-binding\" of ClusterRole \"project-creator\" to Group \"system:authenticated\""
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef": {
      "apiVersion": "v1",
      "name": "app1-project",
      "resource": "projects",
      "namespace": "gpc-system",
      "apiGroup": "resourcemanager.gdc.goog"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` | 
    
    
    "verb": "create"  
  
**Event timestamp** | `requestReceivedTimestamp` | 
    
    
    "requestReceivedTimestamp": "2022-12-09T23:51:56.997825Z"  
  
**Source of action** | `sourceIPs` | 
    
    
    "sourceIPs": [
      "10.200.0.2"
    ]  
  
**Outcome** | `responseStatus` | 
    
    
    "responseStatus": {
      "code": 403,
      "status": "Failure",
      "metadata": {},
      "message": "admission webhook \"validation.gatekeeper.sh\" denied the request: [restrictprojectaccess] username  with groups <[\"system:authenticated\"]> is not allowed for this resource ",
      "reason": "[restrictprojectaccess] username  with groups <[\"system:authenticated\"]> is not allowed for this resource "
    }  
  
**Other fields** | `responseStatus_message` | 
    
    
    "responseStatus": {
      "code": 403,
      "status": "Failure",
      "metadata": {},
      "message": "admission webhook \"validation.gatekeeper.sh\" denied the request: [restrictprojectaccess] username  with groups <[\"system:authenticated\"]> is not allowed for this resource ",
      "reason": "[restrictprojectaccess] username  with groups <[\"system:authenticated\"]> is not allowed for this resource "
    }  
  
### Example log KRM API
    
    
    {
      "sourceIPs": [
        "10.200.0.2"
      ],
      "_gdch_cluster": "root-admin",
      "objectRef": {
        "apiVersion": "v1",
        "name": "app1-project",
        "resource": "projects",
        "namespace": "gpc-system",
        "apiGroup": "resourcemanager.gdc.goog"
      },
      "kind": "Event",
      "level": "Metadata",
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "3611358c-f8b0-4780-9268-950eccc5881a",
      "stage": "ResponseComplete",
      "requestURI": "/apis/resourcemanager.gdc.goog/v1/namespaces/gpc-system/projects?fieldManager=kubectl-client-side-apply&fieldValidation=Strict",
      "verb": "create",
      "requestReceivedTimestamp": "2022-12-09T23:51:56.997825Z",
      "responseStatus": {
        "code": 403,
        "status": "Failure",
        "metadata": {},
        "message": "admission webhook \"validation.gatekeeper.sh\" denied the request: [restrictprojectaccess] username <fop-platform-admin@example.com> with groups <[\"system:authenticated\"]> is not allowed for this resource <Project/app1-project>",
        "reason": "[restrictprojectaccess] username <fop-platform-admin@example.com> with groups <[\"system:authenticated\"]> is not allowed for this resource <Project/app1-project>"
      },
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-b9kk4",
      "stageTimestamp": "2022-12-09T23:51:57.015134Z",
      "userAgent": "kubectl/v1.25.4 (linux/amd64) kubernetes/872a965",
      "user": {
        "groups": [
          "system:authenticated"
        ],
        "username": "fop-platform-admin@example.com"
      },
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"project-creator-binding\" of ClusterRole \"project-creator\" to Group \"system:authenticated\""
      },
      "_gdch_service_name": "apiserver"
    }
    

## Start an audit process

**Log schema** : Gatekeeper

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | _Not applicable_ |   
**Target** _(Fields and values that call the API)_ | `process` | 
    
    
    \"process\":\"audit\"  
  
**Action** _(Fields containing the performed operation)_ | `event_type` | 
    
    
    \"event_type\":\"audit_started\"  
  
**Event timestamp** | `audit_id` | 
    
    
    \"audit_id\":\"2022-12-13T23:07:11Z\"  
  
**Source of action** | `pod_name` | 
    
    
    "pod_name": "gatekeeper-audit-b7 65495d8-tb4kc"
      
  
**Ou tcome** | `msg` | 
    
    
    \"msg\":\"auditing constraints and violations\"  
  
**Other fields** | _Not applicable_ |   
  
## Finish an audit process

**Log schema** : Gatekeeper

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | _Not applicable_ |   
**Target** _(Fields and values that call the API)_ | `process` | 
    
    
    \"process\":\"audit\"  
  
**Action** _(Fields containing the performed operation)_ | `event_type` | 
    
    
    \"event_type\":\"audit_finished\"  
  
**Event timestamp** | `audit_id` | 
    
    
    \"audit_id\":\"2022-12-13T23:05:32Z\"  
  
**Source of action** | `pod_name` | 
    
    
    "pod_name": "gatekeeper-audit-b765495d8-tb4k c"
      
  
**Ou tcome** | `msg` | 
    
    
    \"msg\":\"auditing is complete\"  
  
**Other fields** | _Not applicable_ |   
  
## Audit violation

**Log schema** :Gatekeeper

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `details` | 
    
    
    \"details\":{\"missing_labels\":[\"gatekeeper\"]}  
  
**Target** _(Fields and values that call the API)_ | `process` | 
    
    
    \"process\":\"audit\"  
  
**Action** _(Fields containing the performed operation)_ | `event_type` | 
    
    
    \"event_type\":\"violation_audited\"  
  
**Event timestamp** | `audit_id` | 
    
    
    \"audit_id\":\"2022-12-13T23:07:11Z\"  
  
**Source of action** | `pod_name` | 
    
    
    "pod_name": "gatekeeper-audit-b765495d8-tb4kc"  
  
**Outcome** | `msg` | 
    
    
    \"msg\":\"you must provide labels: {\\\"gatekeeper\\\"}\"  
  
**Other fields** | _Not applicable_ |   
  
## Audit constraint

**Log schema** : Gatekeeper

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `constraint_name` | 
    
    
    \"constraint_name\":\"ns-must-have-gk\"  
  
**Target** _(Fields and values that call the API)_ | `process` | 
    
    
    \"process\":\"audit\"  
  
**Action** _(Fields containing the performed operation)_ | `event_type` | 
    
    
    \"event_type\":\"constraint_audited\"  
  
**Event timestamp** | `audit_id` | 
    
    
    \"audit_id\":\"2022-12-13T23:07:11Z\"  
  
**Source of action** | `pod_name` | 
    
    
    "pod_name": "gatekeeper-audit-b 765495d8-tb4kc"  
  
**Outcome** | `msg` | 
    
    
    \"msg\":\"audit results for constraint\"  
  
**Other fields** | _Not applicable_ |   
  
### Example log Gatekeeper
    
    
    {
      "stream":"stderr",
      "logtag":"F",
      "log":"{
        \"level\":\"info\",
        \"ts\":1670972934.0394588,
        \"logger\":\"controller\",
        \"msg\":\"audit results for constraint\",
        \"process\":\"audit\",
        \"audit_id\":\"2022-12-13T23:07:11Z\",
        \"event_type\":\"constraint_audited\",
        \"constraint_group\":\"constraints.gatekeeper.sh \",
        \"constraint_api_version\":\"v1\",
        \"constraint_kind\":\"K8sRequiredLabels\",
        \"constraint_name\":\"ns-must-have-gk\",
        \"constraint_namespace\":\"\",
        \"constraint_action\":\"deny\",
        \"constraint_status\":\"enforced\",
        \"constraint_violations\":\"64\"
        }",
      "kubernetes":{
        "pod_name": "gatekeeper-audit-b 765495d8-tb4kc",
        "namespace_name":"gatekeeper-system",
        "pod_id":"3c75b257-0917-4575-bb69-ab5eb6f5839d",
        "labels":{
          "app": "gatekeeper",
          "chart": "gatekeeper",
          "control-plane":"audit-controller",
          "gatekeeper.sh/operation":"audit",
          "gatekeeper.sh/system": "yes",
          "heritage" : "Helm",
          "pod-template-hash": "b765495d 8",
          "release":"gatekeeper"
          },
        "host": "gpc-adhoc-2801b240vm-worker-node2",
        "container_name": "manager",
        "docker_id":"33f7eb658cb7a17c50ce917dcc727628bc40ea7d160fb1a20d0d61ae4e51b473",
        "container_hash": "gcr.io/private-cloud-staging/gatekeeper@sha256:5d91735b2378723a74930cdff2298efeea6f6bebc8ea9dd0106bfdb067f5a07d", "container_image": "gcr.io/private-cloud-staging/gatekeeper: v3.7.0"
        },
      "_gdch_tenant_id":"infra-obs"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
