---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kms/
title: Key Management Service (KMS) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:44:08.936929+00:00
---

# Key Management Service (KMS)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Key Management Service (KMS) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Organization only workloads  
---|---  
**Audit log source** | 

  * [Service Mesh Envoy access logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-service-mesh-envoy)
  * [Kubernetes audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-kubernetes)

  
**Audited operations** | 

  * API server (control plane)
  * Istio (data plane)
  * Server (data plane)

  
  
## API server

Log type: Control plane.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `user` |  For example,
    
    
    "user":{
      "groups":["system:authenticated"],
      "username":"fop-platform-admin@example.com"
    }  
  
**Target** _(Fields and values that call the API)_ | `objectRef` | 
    
    
    "objectRef":{
      "resource":"aeadkeys",
      "apiGroup":"kms.gdc.goog",
      "apiVersion":"v1",
      "namespace":"kms-test1"
    }  
  
**Action** _(Fields containing the performed operation)_ | `verb` |  For example, `"verb": "create"`  
**Event timestamp** | `requestReceivedTimestamp` |  For example, `"requestReceivedTimestamp":"2022-12-08T03:59:20.025703Z"`  
**Source of action** | `sourceIPs` |  For example,
    
    
    "sourceIPs":[
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
      "user":{
        "groups":["system:authenticated"],
        "username":"fop-platform-admin@example.com"
      },
      "auditID":"bec33328-b4ba-431e-96a2-9bbb77666478",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-wxw7t",
      "stage":"RequestReceived",
      "_gdch_cluster":"org-1-admin",
      "userAgent":"kubectl/v1.25.4 (linux/amd64) kubernetes/872a965",
      "kind":"Event",
      "level":"Metadata",
      "stageTimestamp":"2022-12-08T03:59:20.025703Z",
      "requestReceivedTimestamp":"2022-12-08T03:59:20.025703Z",
      "objectRef":{
        "resource":"aeadkeys",
        "apiGroup":"kms.gdc.goog",
        "apiVersion":"v1",
        "namespace":"kms-test1"
      },
      "sourceIPs":[
        "10.200.0.7"
      ],
      "apiVersion":"audit.k8s.io/v1",
      "requestURI":"/apis/kms.gdc.goog/v1/namespaces/kms-test1/aeadkeys?fieldManager=kubectl-client-side-apply&fieldValidation=Strict",
      "verb":"create",
      "_gdch_service_name":"apiserver"
    }
    

## Istio

Log type: Data plane.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"fop-platform-admin@example.com"`  
**Target** _(Fields and values that call the API)_ | `resource` | 
    
    
    "resource":{
      "node_name":"sidecar~10.253.166.144~kms-backend-84f5c4f4c7-ncl4d.kms-system~kms-system.svc.cluster.local",
      "cluster_name":"kms-backend.kms-system",
      "zone_name":"europe-west4-b",
      "log_name":"otel_envoy_accesslog"
    }  
  
**Action** _(Fields containing the performed operation)_ | `path` |  For example, `"path":"/goog.gdc.kms.v1.CryptoOperationsService/Encrypt"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-12-08T04:03:33.859Z"`  
**Source of action** | `x_forwarded_for` |  For example, `"x_forwarded_for":"10.253.165.123"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "response_code":"200",
      "response_code_details":"via_upstream",
      "response_flags":"-",
      "route_name":"default",
      "severity_number":0,
      "severity_text":"",
      "start_time":"2022-12-08T04:03:33.859Z",
      "_gdch_service_name":"istio",
      "upstream_host":"10.253.166.144:8080",
      "upstream_local_address":"127.0.0.6:54383",
      "user_agent":"grpc-go/1.49.0",
      "_gdch_service_tenant":"platform-obs",
      "username":"fop-platform-admin@example.com",
      "x_envoy_upstream_service_time":"104",
      "x_forwarded_for":"10.253.165.123",
      "x_goog_api_client":"-",
      "x_request_id":"c11cbf94-765d-440d-9d36-56654d93d834",
      "authority":"kms.org-1.zone1.google.gdch.test",
      "bytes_received":"32756",
      "body":{},
      "upstream_transport_failure_reason":"-",
      "bytes_sent":"0",
      "downstream_local_address":"10.253.166.144:8080",
      "downstream_remote_address":"10.253.165.123:0",
      "duration":"318",
      "method":"POST",
      "observed_time_unix_nano":0,
      "protocol":"HTTP/2",
      "requested_server_name":"outbound_.8080_._.kms-backend.kms-system.svc.cluster.local",
      "_gdch_namespace":"istio-system",
      "path":"/goog.gdc.kms.v1.CryptoOperationsService/Encrypt",
      "connection_termination_details":"-",
      "time_unix_nano":1670472213859570944,
      "upstream_cluster":"inbound|8080||",
      "resource":{
        "node_name":"sidecar~10.253.166.144~kms-backend-84f5c4f4c7-ncl4d.kms-system~kms-system.svc.cluster.local",
        "cluster_name":"kms-backend.kms-system",
        "zone_name":"europe-west4-b",
        "log_name":"otel_envoy_accesslog"
      },
      "_gdch_cluster":"org-1-admin",
      "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-cr9h7"
    }
    

## Server

Log type: Data plane.

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `message.user.identity` |  For example, `"message":{"user":"{"identity":"fop-platform-admin@example.com"}}"`  
**Target** _(Fields and values that call the API)_ | `_gdch_service_name` |  `"_gdch_service_name":"kms-backend"`  
**Action** _(Fields containing the performed operation)_ | `message.action` |  For example, `"message":"{"action":"/goog.gdc.kms.v1.CryptoOperationsService/Encrypt"}"`  
**Event timestamp** | `time` |  For example, `"time":"2022-12-08T04:25:32.676604174Z"`  
**Source of action** | `_gdch_cluster` |  For example, `"_gdch_cluster":"org-1-admin"`  
**Outcome** | `message.response` |  For example, `"message":"{"response":"OK"}"`  
**Other fields** | _The`message.description` field contains the complete log message._ | For more information, see the **Example log**.  
  
**Example log**
    
    
    {
        "pri":"46",
        "time":"2023-05-30T20:58:25Z",
        "host":"kms-backend-9dd54b666-jfp5v",
        "ident":"/kms_bin",
        "pid":"1",
        "msgid":"audit-log",
        "extradata":"-",
        "message":"{\"time\":\"2023-08-01T18:04:00.458810232Z\",\"auditID\":\"6f848640-8af1-4659-b9c9-a358d19bea5f\",\"user\":{\"identity\":\"fop-platform-admin@example.com\"},\"resource\":\"namespaces/testnamespace/aeadKeys/testcryptokey\",\"action\":\"/goog.gdc.kms.v1.CryptoOperationsService/Decrypt\",\"description\":\"{\"duration_ms\":202}\",\"userAgent\":\"grpc-go/1.55.0\",\"response\":\"OK\",\"_gdch_service\":\"kms\"}",
        "_gdch_org_name":"org-1",
        "_gdch_org_id":"org-1.zone1.google.gdch.test",
        "_gdch_cluster":"org-1-admin",
        "_gdch_fluentbit_pod":"anthos-audit-logs-forwarder-5lq2g",
        "_gdch_service_name":"kms-backend",
        "_gdch_tenant_id":"platform-obs"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
