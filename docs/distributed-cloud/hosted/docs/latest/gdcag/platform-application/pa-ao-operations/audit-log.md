---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-log/
title: Logging and Audit Logging (LOG and AL) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:44:08.463864+00:00
---

# Logging and Audit Logging (LOG and AL)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-log/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Logging and Audit Logging (LOG and AL) Stay organized with collections  Save and categorize content based on your preferences. 

**Audit log source** | 

  * [Observability audit logger](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-observability-logger)
  * [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)

  
---|---  
**Audited operations** | 

  * Run LogQL queries or export logs using the user interface of the monitoring instance
  * Perform actions on the `LoggingTarget` custom resource
  * Perform actions on the `LoggingRule` custom resource
  * Perform actions on the `SIEMOrgForwarder` custom resource

  
  
## Run LogQL queries or export logs using the user interface of the monitoring instance

**Note:** You can export all queries in the monitoring instance. That action doesn't separately capture the export from the user interface, but it logs the executed query.**Audit log source** |  Proxy server  
---|---  
**Log type** |  Data plane  
Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
      "issuer": "https://ais-core.org-1.zone1.google.gdch.test",
      "identity": "fop-infrastructure-operator@example.com"
      }  
  
**Target** _(Fields and values that call the API)_ | `resource` |  For example, `"resource": "/infra-obs/grafana/api/ds/query"`  
**Action** _(Fields containing the performed operation)_ | `action` |  Possible values:

  * `"action": "QUERY"`
  * `"action": "CREATE"`
  * `"action": "READ"`
  * `"action": "UPDATE"`
  * `"action": "DELETE"`
  * `"action": "CREATE/UPDATE"`

  
**Event timestamp** |  `time` |  For example, `"time": "2022-12-02T21:37:03.657277582Z"`  
**Source of action** | 

  * `sourceIPs`
  * `_gdch_service_name`

|  For example,
    
    
    "sourceIPs": [
      [
      "10.253.165.26",
      "127.0.0.6"
    ],
    "_gdch_service_name": "grafana"  
  
**Outcome** | `response` |  For example, `"response": "Successful: 200 OK"`  
**Other fields** | `description` | The `description` value contains the complete query. For more information. see the **Example log**.  
  
**Example log**
    
    
    {
      "sourceIPs": [
        "10.253.165.26",
        "127.0.0.6"
      ],
      "description": "{
        \"queries\":
          [{
            \"refId\":\"A\",
            \"datasource\":
              {
                \"uid\":\"P762A5DD6F13C8B7A\",
                \"type\":\"loki\"
              },
            \"editorMode\":\"builder\",
            \"expr\":\"{service_name=\\\"grafana\\\"} |= ``\",
            \"queryType\":\"range\",
            \"key\":\"Q-fd978c0c-86fd-4c70-bb38-07737a3be3ad-0\",
            \"maxLines\":1000,
            \"legendFormat\":\"\",
            \"datasourceId\":3,
            \"intervalMs\":500,
            \"maxDataPoints\":1688
          }],
        \"range\":
          {
            \"from\":\"2022-12-02T21:22:03.496Z\",
            \"to\":\"2022-12-02T21:37:03.496Z\",
            \"raw\":{\"from\":\"now-15m\",\"to\":\"now\"}
          },
        \"from\":\"1670016123496\",
        \"to\":\"1670017023496\"
      }",
      "response": "Successful: 200 OK",
      "_gdch_namespace": "infra-obs-obs-system",
      "numBytesSent": 190079,
      "time": "2022-12-02T21:37:03.657277582Z",
      "user": {
        "issuer": "https://ais-core.org-1.zone1.google.gdch.test",
        "identity": "fop-infrastructure-operator@example.com"
      },
      "_gdch_service_name": "grafana",
      "_gdch_service_tenant": "infra-obs",
      "numBytesReceived": 3172,
      "resource": "/infra-obs/grafana/api/ds/query",
      "auditID": "b519ec65-d906-4a79-bcfe-a4e1984045fe",
      "action": "QUERY",
      "_gdch_cluster": "org-1-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-9x9pd"
    }
    

## Perform actions on the `LoggingTarget` custom resource

**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
---|---  
**Log type** |  Control plane  
Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "extra": {
            "authentication.kubernetes.io/pod-name": [
                "fleet-admin-controller-875778d98-99l6n"
            ],
            "authentication.kubernetes.io/pod-uid": [
                "4800e06c-c96d-4e17-ae1a-b5a74eedf6ee"
            ]
        },
        "uid": "b18e586e-db0e-417e-9dff-1a722ab36bf4",
        "username": "system:serviceaccount:gpc-system:fleet-admin-controller",
        "groups": [
            "system:serviceaccounts",
            "system:serviceaccounts:gpc-system",
            "system:authenticated"
        ]
    }  
  
**Target** _(Fields and values that call the API)_ | 

  * `requestURI`
  * `objectRef`

|  For example,
    
    
    "requestURI": "/apis/logging.gdc.goog/v1/namespaces/obs-system/loggingtargets/lt-cfg1",
    "objectRef": {
        "uid": "2e540720-ed23-4665-8c40-c399cb6be624",
        "namespace": "obs-system",
        "name": "lt-cfg1",
        "resource": "loggingtargets",
        "apiVersion": "v1",
        "apiGroup": "logging.gdc.goog",
        "resourceVersion": "5326570"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  Possible values:

  * `"verb": "create"`
  * `"verb": "delete"`
  * `"verb": "get"`
  * `"verb": "list"`
  * `"verb": "patch"`
  * `"verb": "update"`
  * `"verb": "watch"`

  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2022-12-06T14:37:41.035715Z"`  
**Source of action** | 

  * `sourceIPs`
  * `_gdch_service_name`

|  For example,
    
    
    "sourceIPs": [
        "10.253.164.209"
    ],
    "_gdch_service_name": "apiserver"  
  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "metadata": {},
        "code": 200
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "level": "Metadata",
      "auditID": "94c2106f-1fd1-428b-adbc-80ac48ef479e",
      "_gdch_cluster": "org-1-admin",
      "requestURI": "/apis/logging.gdc.goog/v1/namespaces/obs-system/loggingtargets/lt-cfg1",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-4gwpn",
      "verb": "update",
      "userAgent": "fleet-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
      "responseStatus": {
        "metadata": {},
        "code": 200
      },
      "user": {
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "fleet-admin-controller-875778d98-99l6n"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "4800e06c-c96d-4e17-ae1a-b5a74eedf6ee"
          ]
        },
        "uid": "b18e586e-db0e-417e-9dff-1a722ab36bf4",
        "username": "system:serviceaccount:gpc-system:fleet-admin-controller",
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:gpc-system",
          "system:authenticated"
        ]
      },
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"fleet-admin-common-controller\" of ClusterRole \"fleet-admin-common-controllers-role\" to ServiceAccount \"fleet-admin-controller/gpc-system\""
      },
      "sourceIPs": [
        "10.253.164.209"
      ],
      "stage": "ResponseComplete",
      "kind": "Event",
      "apiVersion": "audit.k8s.io/v1",
      "stageTimestamp": "2022-12-06T14:37:41.035715Z",
      "objectRef": {
        "uid": "2e540720-ed23-4665-8c40-c399cb6be624",
        "namespace": "obs-system",
        "name": "lt-cfg1",
        "resource": "loggingtargets",
        "apiVersion": "v1",
        "apiGroup": "logging.gdc.goog",
        "resourceVersion": "5326570"
      },
      "requestReceivedTimestamp": "2022-12-06T14:37:40.942762Z",
      "_gdch_service_name": "apiserver"
    }
    

## Perform actions on the `LoggingRule` custom resource

**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
---|---  
**Log type** |  Control plane  
Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "extra": {
            "authentication.kubernetes.io/pod-name": [
                "fleet-admin-controller-875778d98-99l6n"
            ],
            "authentication.kubernetes.io/pod-uid": [
                "4800e06c-c96d-4e17-ae1a-b5a74eedf6ee"
            ]
        },
        "uid": "b18e586e-db0e-417e-9dff-1a722ab36bf4",
        "username": "system:serviceaccount:gpc-system:fleet-admin-controller",
        "groups": [
            "system:serviceaccounts",
            "system:serviceaccounts:gpc-system",
            "system:authenticated"
        ]
    }  
  
**Target** _(Fields and values that call the API)_ | 

  * `requestURI`
  * `objectRef`

|  For example,
    
    
    "requestURI": "/apis/logging.gdc.goog/v1/namespaces/obs-system/loggingrules/lr-cfg1",
    "objectRef": {
        "uid": "2e540720-ed23-4665-8c40-c399cb6be624",
        "namespace": "obs-system",
        "name": "lr-cfg1",
        "resource": "loggingrules",
        "apiVersion": "v1",
        "apiGroup": "logging.gdc.goog",
        "resourceVersion": "5326570"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  Possible values:

  * `"verb": "create"`
  * `"verb": "delete"`
  * `"verb": "get"`
  * `"verb": "list"`
  * `"verb": "patch"`
  * `"verb": "update"`
  * `"verb": "watch"`

  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2022-12-06T14:37:41.035715Z"`  
**Source of action** | 

  * `sourceIPs`
  * `_gdch_service_name`

|  For example,
    
    
    "sourceIPs": [
        "10.253.164.209"
    ],
    "_gdch_service_name": "apiserver"  
  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "metadata": {},
        "code": 200
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "level": "Metadata",
      "auditID": "94c2106f-1fd1-428b-adbc-80ac48ef479e",
      "_gdch_cluster": "org-1-admin",
      "requestURI": "/apis/logging.gdc.goog/v1/namespaces/obs-system/loggingrules/lr-cfg1",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-4gwpn",
      "verb": "update",
      "userAgent": "fleet-admin-cm/v0.0.0 (linux/amd64) kubernetes/$Format",
      "responseStatus": {
        "metadata": {},
        "code": 200
      },
      "user": {
        "extra": {
          "authentication.kubernetes.io/pod-name": [
            "fleet-admin-controller-875778d98-99l6n"
          ],
          "authentication.kubernetes.io/pod-uid": [
            "4800e06c-c96d-4e17-ae1a-b5a74eedf6ee"
          ]
        },
        "uid": "b18e586e-db0e-417e-9dff-1a722ab36bf4",
        "username": "system:serviceaccount:gpc-system:fleet-admin-controller",
        "groups": [
          "system:serviceaccounts",
          "system:serviceaccounts:gpc-system",
          "system:authenticated"
        ]
      },
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding \"fleet-admin-common-controller\" of ClusterRole \"fleet-admin-common-controllers-role\" to ServiceAccount \"fleet-admin-controller/gpc-system\""
      },
      "sourceIPs": [
        "10.253.164.209"
      ],
      "stage": "ResponseComplete",
      "kind": "Event",
      "apiVersion": "audit.k8s.io/v1",
      "stageTimestamp": "2022-12-06T14:37:41.035715Z",
      "objectRef": {
        "uid": "2e540720-ed23-4665-8c40-c399cb6be624",
        "namespace": "obs-system",
        "name": "lr-cfg1",
        "resource": "loggingrules",
        "apiVersion": "v1",
        "apiGroup": "logging.gdc.goog",
        "resourceVersion": "5326570"
      },
      "requestReceivedTimestamp": "2022-12-06T14:37:40.942762Z",
      "_gdch_service_name": "apiserver"
    }
    

## Perform actions on the `SIEMOrgForwarder` custom resource

**Audit log source** |  [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)  
---|---  
**Log type** |  Control plane  
Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user": {
        "username": "kubernetes-admin",
        "groups": [
            "system:masters",
            "system:authenticated"
        ]
    }  
  
**Target** _(Fields and values that call the API)_ | 

  * `requestURI`
  * `objectRef`

|  For example,
    
    
    "requestURI": "/apis/logging.gdc.goog/v1/namespaces/alice/siemorgforwarders/audits",
    "objectRef": {
        "apiGroup": "logging.gdc.goog",
        "apiVersion": "v1",
        "name": "audits",
        "resource": "siemorgforwarders",
        "namespace": "alice"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  Possible values:

  * `"verb": "create"`
  * `"verb": "delete"`
  * `"verb": "get"`
  * `"verb": "list"`
  * `"verb": "patch"`
  * `"verb": "update"`
  * `"verb": "watch"`

  
**Event timestamp** |  `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp": "2025-02-05T03:06:13.738683Z"`  
**Source of action** | 

  * `sourceIPs`

|  For example,
    
    
    "sourceIPs": [
        "10.200.0.7"
    ]  
  
**Outcome** | `responseStatus` |  For example,
    
    
    "responseStatus": {
        "metadata": {},
        "code": 200
    }  
  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "_gdch_cluster": "root-admin",
      "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-vrfkc",
      "_gdch_org_id": "root.zone1.google.gdch.test",
      "_gdch_org_name": "root",
      "_gdch_zone_id": "zone1",
      "annotations": {
        "authorization.k8s.io/decision": "allow",
        "authorization.k8s.io/reason": ""
      },
      "apiVersion": "audit.k8s.io/v1",
      "auditID": "ade605c0-8043-4231-8471-dc02b14ff327",
      "kind": "Event",
      "level": "Metadata",
      "objectRef": {
        "apiGroup": "logging.gdc.goog",
        "apiVersion": "v1",
        "name": "audit",
        "namespace": "alice",
        "resource": "siemorgforwarders"
      },
      "requestReceivedTimestamp": "2025-02-05T03:16:06.564964Z",
      "requestURI": "/apis/logging.gdc.goog/v1/namespaces/alice/siemorgforwarders/audit",
      "responseStatus": {
        "code": 200,
        "metadata": {}
      },
      "sourceIPs": [
        "10.200.0.4"
      ],
      "stage": "ResponseComplete",
      "stageTimestamp": "2025-02-05T03:16:06.567624Z",
      "user": {
        "groups": [
          "system:masters",
          "system:authenticated"
        ],
        "username": "kubernetes-admin"
      },
      "userAgent": "k9s/v0.0.0 (linux/amd64) kubernetes/$Format",
      "verb": "get"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
