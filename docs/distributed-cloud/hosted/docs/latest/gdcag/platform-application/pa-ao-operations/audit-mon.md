---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-mon/
title: Monitoring (MON) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:12.494627+00:00
---

# Monitoring (MON)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-mon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Monitoring (MON) Stay organized with collections  Save and categorize content based on your preferences. 

Monitoring (MON) audit logs in Google Distributed Cloud (GDC) air-gapped let you track PromQL query execution along with dashboard and alert configuration changes. The observability audit logger and Kubernetes audit logs record metadata fields and JSON payloads for these data plane and control plane operations.

**Audit log source** | 

  * [Observability audit logger](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-observability-logger)
  * [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)

  
---|---  
**Audited operations** | 

  * Run PromQL queries using the user interface of the monitoring instance
  * Run PromQL queries using the HTTP API
  * Perform dashboard CRUD operations
  * Perform alert CRUD operations

  
  
## Run PromQL queries using the user interface of the monitoring instance

**Audit log source** |  Proxy server  
---|---  
**Log type** |  Data plane  
Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "identity":"fop-cluster-admin@example.com",
      "issuer":"https://ais-core.org-1.zone1.google.gdch.test"
    }  
  
**Target** _(Fields and values that call the API)_ | `resource` |  For example, `"resource": "/infra-obs/grafana/api/ds/query"`  
**Action** _(Fields containing the performed operation)_ | `action` |  Possible values:

  * `"action": "QUERY"`
  * `"action": "CREATE"`
  * `"action": "READ"`
  * `"action": "UPDATE"`
  * `"action": "DELETE"`
  * `"action": "CREATE/UPDATE"`

  
**Event timestamp** |  `time` |  For example, `"time": "2022-12-05T14:39:15.713354008Z"`  
**Source of action** | 

  * `sourceIPs`
  * `_gdch_service_name`

|  For example,
    
    
    "sourceIPs":[
      "10.253.166.214",
      "127.0.0.6"
    ],
    "_gdch_service_name":"grafana"  
  
**Outcome** | `response` |  For example, `"response": "Successful: 200 OK"`  
**Other fields** | `description` | The `description` value contains the complete query. For more information. see the **Example log**.  
  
**Example log**
    
    
    {
      "resource":"/infra-obs/grafana/api/ds/query",
      "response":"Successful: 200 OK",
      "_gdch_service_tenant":"infra-obs",
      "sourceIPs":[
        "10.253.166.214",
        "127.0.0.6"
      ],
      "_gdch_namespace":"infra-obs-obs-system",
      "userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0",
      "time":"2022-12-05T14:39:15.713354008Z",
      "auditID":"6bba5ff1-97d9-4bf8-92af-4f63049448cf",
      "numBytesSent":1821,
      "action":"QUERY",
      "_gdch_service_name":"grafana",
      "numBytesReceived":2827,
      "description":"{
          \"queries\":[{
          \"refId\":\"A\",
          \"expr\":\"{container=\\\"grafana-proxy-server\\\"},
          \"queryType\":\"range\",
          \"datasource\":{\"uid\":\"P982945308D3682D1\",\"type\":\"loki\"},
          \"key\":\"Q-c63373da-dec2-49c3-aa6c-4e5ba07ec8de-0\",
          \"editorMode\":\"builder\",
          \"maxLines\":1000,
          \"legendFormat\":\"\",
          \"datasourceId\":2,
          \"intervalMs\":1000,
          \"maxDataPoints\":2493
        }],
        \"range\":{
          \"from\":\"2022-12-05T13:39:15.461Z\",
          \"to\":\"2022-12-05T14:39:15.461Z\",
          \"raw\":{\"from\":\"now-1h\",\"to\":\"now\"}
        },
        \"from\":\"1670247555461\",
        \"to\":\"1670251155461\"
      }",
      "user":{
        "identity":"fop-cluster-admin@example.com",
        "issuer":"https://ais-core.org-1.zone1.google.gdch.test"
      },
      "_gdch_cluster":"org-1-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-whltm"
    }
    

## Run PromQL queries using the HTTP API

**Audit log source** |  Proxy server  
---|---  
**Log type** |  Data plane  
Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "issuer":"https://ais-core.org-1.zone1.google.gdch.test",
      "identity":"fop-cluster-admin@example.com"
    }  
  
**Target** _(Fields and values that call the API)_ | `resource` |  For example, `"resource":"/alertmanager/api/v2/alerts/groups?silenced=false&inhibited=false&active=true"`  
**Action** _(Fields containing the performed operation)_ | `action` |  Possible values:

  * `"action": "QUERY"`
  * `"action": "CREATE"`
  * `"action": "READ"`
  * `"action": "UPDATE"`
  * `"action": "DELETE"`
  * `"action": "CREATE/UPDATE"`

  
**Event timestamp** |  `time` |  For example, `"time": "2022-12-05T18:20:50.616925009Z"`  
**Source of action** | 

  * `sourceIPs`
  * `_gdch_service_name`

|  For example,
    
    
    "sourceIPs":[
      "10.200.0.1",
      "127.0.0.6"
    ],
    "_gdch_service_name":"cortex"  
  
**Outcome** | `response` |  For example, `"response": "Successful: 200 OK"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "user":{
        "issuer":"https://ais-core.org-1.zone1.google.gdch.test",
        "identity":"fop-cluster-admin@example.com"
      },
      "_gdch_service_tenant":"infra-obs",
      "_gdch_service_name":"cortex",
      "resource":"/alertmanager/api/v2/alerts/groups?silenced=false&inhibited=false&active=true",
      "time":"2022-12-05T18:20:50.616925009Z",
      "action":"READ",
      "numBytesReceived":2376,
      "sourceIPs":[
        "10.200.0.1",
        "127.0.0.6"
      ],
      "_gdch_namespace":"obs-system",
      "userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0",
      "numBytesSent":173,
      "auditID":"8451a7b3-77f9-4878-9308-641b55a83865",
      "response":"Successful: 200 OK",
      "_gdch_cluster":"org-1-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-2wqxp"
    }
    

## Perform dashboard CRUD operations

**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
---|---  
**Log type** |  Control plane  
Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "extra":{
        "authentication.kubernetes.io/pod-name":["fleet-admin-controller-875778d98-dnkj2"],
        "authentication.kubernetes.io/pod-uid":["caa4df7a-ae04-458e-a616-1c6893ce6e46"]
      },
      "username":"system:serviceaccount:gpc-system:fleet-admin-controller",
      "groups":[
        "system:serviceaccounts",
        "system:serviceaccounts:gpc-system",
        "system:authenticated"
      ],
      "uid":"0b93d757-e3be-440a-b18a-4a2b524de156"
    }  
  
**Target** _(Fields and values that call the API)_ | 

  * `requestURI`
  * `objectRef`

|  For example,
    
    
    "requestURI":"/apis/observability.gdc.goog/v1/namespaces/alice-obs-system/dashboards",
    "objectRef":{
      "apiVersion":"v1",
      "apiGroup":"observability.gdc.goog",
      "resource":"dashboards",
      "namespace":"alice-obs-system"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  Possible values:

  * `"verb": "create"`
  * `"verb": "delete"`
  * `"verb": "get"`
  * `"verb": "list"`
  * `"verb": "patch"`
  * `"verb": "update"`
  * `"verb": "watch"`

  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2022-12-05T15:36:24.980257Z"`  
**Source of action** | 

  * `sourceIPs`
  * `_gdch_service_name`

|  For example,
    
    
    "sourceIPs":["10.253.166.100"],
    "_gdch_service_name":"apiserver"  
  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "user":{
        "extra":{
          "authentication.kubernetes.io/pod-name":["fleet-admin-controller-875778d98-dnkj2"],
          "authentication.kubernetes.io/pod-uid":["caa4df7a-ae04-458e-a616-1c6893ce6e46"]
        },
        "username":"system:serviceaccount:gpc-system:fleet-admin-controller",
        "groups":[
          "system:serviceaccounts",
          "system:serviceaccounts:gpc-system",
          "system:authenticated"
        ],
        "uid":"0b93d757-e3be-440a-b18a-4a2b524de156"
      },
      "kind":"Event",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-2wqxp",
      "apiVersion":"audit.k8s.io/v1",
      "_gdch_cluster":"org-1-admin",
      "level":"Metadata",
      "stageTimestamp":"2022-12-05T15:36:24.980257Z",
      "auditID":"a060d80a-4a47-4490-a859-5d3ccff36d3d",
      "requestReceivedTimestamp":"2022-12-05T15:36:24.980257Z",
      "userAgent":"fleet-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
      "stage":"RequestReceived",
      "requestURI":"/apis/observability.gdc.goog/v1/namespaces/alice-obs-system/dashboards",
      "objectRef":{
        "apiVersion":"v1",
        "apiGroup":"observability.gdc.goog",
        "resource":"dashboards",
        "namespace":"alice-obs-system"
      },
      "verb":"create",
      "sourceIPs":["10.253.166.100"],
      "_gdch_service_name":"apiserver"
    }
    

## Perform alert CRUD operations

**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
---|---  
**Log type** |  Control plane  
Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "username":"kubernetes-admin",
      "groups":[
        "system:masters",
        "system:authenticated"
      ]
    }  
  
**Target** _(Fields and values that call the API)_ | 

  * `requestURI`
  * `objectRef`

|  For example,
    
    
    "requestURI":"/apis/monitoring.gdc.goog/v1/namespaces/alice/monitoringrules?fieldManager=kubectl-client-side-apply&fieldValidation=Strict",
    "objectRef":{
      "apiVersion":"v1",
      "apiGroup":"monitoring.gdc.goog",
      "name":"obs-test-alert-sequel",
      "namespace":"alice",
      "resource":"monitoringrules"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  Possible values:

  * `"verb": "create"`
  * `"verb": "delete"`
  * `"verb": "get"`
  * `"verb": "list"`
  * `"verb": "patch"`
  * `"verb": "update"`
  * `"verb": "watch"`

  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2022-12-05T16:28:50.619659Z"`  
**Source of action** | 

  * `sourceIPs`
  * `_gdch_service_name`

|  For example,
    
    
    "sourceIPs":["10.200.0.6"],
    "_gdch_service_name":"apiserver"  
  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus":{
      "code":201,
      "metadata":{}
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "level":"Metadata",
      "sourceIPs":[
        "10.200.0.6"
      ],
      "auditID":"753c3370-d3a5-4717-b84e-00fd56883fc4",
      "requestURI":"/apis/monitoring.gdc.goog/v1/namespaces/alice/monitoringrules?fieldManager=kubectl-client-side-apply&fieldValidation=Strict",
      "apiVersion":"audit.k8s.io/v1",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-fgkth",
      "user":{
        "username":"kubernetes-admin",
        "groups":[
          "system:masters",
          "system:authenticated"
        ]
      },
      "userAgent":"kubectl/v1.25.4 (linux/amd64) kubernetes/872a965",
      "verb":"create",
      "stage":"ResponseComplete",
      "stageTimestamp":"2022-12-05T16:28:50.636050Z",
      "_gdch_cluster":"org-1-admin",
      "objectRef":{
        "apiVersion":"v1",
        "apiGroup":"monitoring.gdc.goog",
        "name":"obs-test-alert-sequel",
        "namespace":"alice",
        "resource":"monitoringrules"
      },
      "responseStatus":{
        "code":201,
        "metadata":{}
      },
      "kind":"Event",
      "annotations":{
        "authorization.k8s.io/reason":"",
        "authorization.k8s.io/decision":"allow"
      },
      "requestReceivedTimestamp":"2022-12-05T16:28:50.619659Z",
      "_gdch_service_name":"apiserver"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
