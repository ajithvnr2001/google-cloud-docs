---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-vai/
title: Vertex AI (VAI) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:53.521332+00:00
---

# Vertex AI (VAI)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-vai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Vertex AI (VAI) Stay organized with collections  Save and categorize content based on your preferences. 

**Workload location** |  Organization only workloads  
---|---  
**Audit log source** |  Pre-trained AI/ML from Vertex AI (VAI)  
**Audited operations** | 
* HTTP API that translates input text and returns translated text
* Get supported language pairs (HTTP GET)
* Detect language for a given input text (HTTP GET) 
* Create glossaries (HTTP POST)
* Get glossaries (HTTP GET)
* List glossaries (HTTP GET)
* Delete glossary (HTTP POST)
* Get operations (HTTP GET)
* List operations (HTTP GET)
* gRPC call that translates input text and returns translated text
* Detect language for a given input text (gRPC)
* Get supported language pairs (gRPC)
* Translate a document (gRPC)
* Create glossaries (gRPC)
* Get glossaries (gRPC)
* List glossaries (gRPC)
* Delete glossary (gRPC)
* Get operations (gRPC)
* List operations (gRPC)
* Detect text in a batch of files (gRPC)
* Detect text in image file (gRPC)
* Detect text in file (gRPC)
* Transcribe speech to text (gRPC)
* Transcribe streaming speech to text (gRPC)
* Get status of AIML Pre-trained APIs (HTTP GET)
* Enable the AIML Pre-trained APIs (HTTP POST)
* Disable the AIML Pre-trained APIs (HTTP POST)  
  
## HTTP API that translates input text and returns translated text

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/v3/projects/PROJECT_ID:translateText" `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/v3/projects/iam-test:translateText",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Get supported language pairs (HTTP GET)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/v3/projects/PROJECT_ID:getSupportedLanguages" `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/v3/projects/iam-test:getSupportedLanguages",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Detect language for a given input text (HTTP GET)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/v3/projects/PROJECT_ID:detectLanguage" `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/v3/projects/iam-test:detectLanguage",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Create glossaries (HTTP POST)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/v3/projects/PROJECT_ID:glossaries" `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"CREATE"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "CREATE",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/v3/projects/iam-test:glossaries",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Get glossaries (HTTP GET)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/v3/projects/PROJECT_ID:glossaries" `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/v3/projects/iam-test:glossaries",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## List glossaries (HTTP GET)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/v3/projects/PROJECT_ID:glossaries?page_size=10" `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/v3/projects/iam-test:glossaries?page_size=10",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Delete glossary (HTTP POST)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/v3/projects/PROJECT_ID/glossaries/GLOSSARY_ID `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"DELETE"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "DELETE",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/v3/projects/iam-test/glossaries/[GLOSSARY_ID]",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Get operations (HTTP GET)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/v3/projects/PROJECT_ID/operations" `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/v3/projects/iam-test/operations",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## List operations (HTTP GET)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/v3/projects/PROJECT_ID/operations?page_size=10" `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/v3/projects/iam-test/operations?page_size=10",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## gRPC call that translates input text and returns translated text

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.cloud.translation.v3.TranslationService/TranslateText"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.cloud.translation.v3.TranslationService/TranslateText",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Detect language for a given input text (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.cloud.translation.v3.TranslationService/DetectLanguage"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.cloud.translation.v3.TranslationService/DetectLanguage",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Get supported language pairs (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.cloud.translation.v3.TranslationService/GetSupportedLanguages"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.cloud.translation.v3.TranslationService/GetSupportedLanguages",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Translate a document (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.cloud.translation.v3.TranslationService/TranslateDocument"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.cloud.translation.v3.TranslationService/TranslateDocument",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Create glossaries (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.cloud.translation.v3.TranslationService/CreateGlossary"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"CREATE"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "CREATE",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.cloud.translation.v3.TranslationService/CreateGlossary",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Get glossaries (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.cloud.translation.v3.TranslationService/GetGlossary"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.cloud.translation.v3.TranslationService/GetGlossary",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## List glossaries (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.cloud.translation.v3.TranslationService/ListGlossaries"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.cloud.translation.v3.TranslationService/ListGlossaries",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Delete glossary (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.cloud.translation.v3.TranslationService/DeleteGlossaries" `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"DELETE"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "DELETE",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.cloud.translation.v3.TranslationService/DeleteGlossaries",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Get operations (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.longrunning.Operations/GetOperation"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.longrunning.Operations/GetOperation",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## List operations (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.longrunning.Operations/ListOperations"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "translation.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.translation-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-translation-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.longrunning.Operations/ListOperations",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Detect text in a batch of files (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.cloud.vision.v1.ImageAnnotator.BatchAnnotateFiles"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "vision.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.vision-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-vision-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-vision-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.cloud.vision.v1.ImageAnnotator.BatchAnnotateFiles",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Detect text in image file (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/v1/images:annotate"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "vision.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.vision-frontend-server.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-vision-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-vision-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/v1/images:annotate",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Detect text in file (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/v1/files:annotate" `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "vision.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.vision-frontend-server.ai-speech-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-vision-frontend-server-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-vision-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/v1/files:annotate",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Transcribe speech to text (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.cloud.speech.v1p1beta1.Speech.Recognize"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "speech.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.speech.ai-speech-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-speech-758f6c76b7-cn2qv.ai-speech-system~ai-speech-system.svc.cluster.local",
            "cluster_name": "dep-speech.ai-speech-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.cloud.speech.v1p1beta1.Speech.Recognize",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Transcribe streaming speech to text (gRPC)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"google.cloud.speech.v1p1beta1.Speech.StreamingRecognize" `  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "speech.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.speech.ai-speech-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~dep-speech-758f6c76b7-cn2qv.ai-speech-system~ai-speech-system.svc.cluster.local",
            "cluster_name": "dep-speech.ai-speech-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "google.cloud.speech.v1p1beta1.Speech.StreamingRecognize",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Get status of AIML Pre-trained APIs (HTTP GET)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/ai-service-status"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"GET"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "aip-web-plugin-frontend-svc.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "GET",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.aip-web-plugin-frontend-svc.ai-translation-system.svc.cluster.local",
        "resource": { 
            "node_name": "sidecar~10.253.168.130~aip-web-plugin-frontend-svc-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "aip-web-plugin-frontend-svc.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/ai-service-status",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Enable the AIML Pre-trained APIs (HTTP POST)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/enable-ai-service"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"POST"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"201"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "aip-web-plugin-frontend-svc.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "POST",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.aip-web-plugin-frontend-svc.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~aip-web-plugin-frontend-svc-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "dep-translation-frontend-server.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/enable-ai-service",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "201",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

## Disable the AIML Pre-trained APIs (HTTP POST)

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username":"gdch-system:serviceaccount:iam-test:psa-test"`  
**Target** _(Fields and values that call the API)_ | `path` | `"path":"/disable-ai-service"`  
**Action** _(Fields containing the performed operation)_ | `method` | `"method":"POST"`  
**Event timestamp** | `start_time` |  For example, `"start_time":"2022-11-23T00:58:52.092Z"`  
**Source of action** | `upstream_host` |  For example, `"upstream_host":"10.253.168.130:9998"`  
**Outcome** | `response_code` |  For example, `"response_code":"200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
        "authority": "aip-web-plugin-frontend-svc.org-1.zone1.google.gdch.test",
        "x_forwarded_for": "10.253.168.4",
        "severity_number": 0,
        "start_time": "2022-11-23T00:58:52.092Z",
        "upstream_cluster": "inbound|9998||",
        "upstream_transport_failure_reason": "-",
        "user_agent": "curl/7.85.0",
        "username": "gdch-system:serviceaccount:iam-test:psa-test",
        "x_envoy_upstream_service_time": "399",
        "x_goog_api_client": "-",
        "x_request_id": "8b2977b0-2ffc-48cb-83b8-2b4c1ebca615",
        "downstream_remote_address": "10.253.168.4:0",
        "duration": "420",
        "method": "POST",
        "observed_time_unix_nano": 0,
        "protocol": "HTTP/1.1",
        "requested_server_name": "outbound_.9998_._.aip-web-plugin-frontend-svc.ai-translation-system.svc.cluster.local",
        "resource": {
            "node_name": "sidecar~10.253.168.130~aip-web-plugin-frontend-svc-758f6c76b7-cn2qv.ai-translation-system~ai-translation-system.svc.cluster.local",
            "cluster_name": "aip-web-plugin-frontend-svc.ai-translation-system",
            "log_name": "otel_envoy_accesslog",
            "zone_name": "us-east1-b"
        },
        "path": "/disable-ai-service",
        "bytes_received": "128",
        "connection_termination_details": "-",
        "downstream_local_address": "10.253.168.130:9998",
        "response_code": "200",
        "route_name": "default",
        "response_code_details": "via_upstream",
        "response_flags": "-",
        "bytes_sent": "60",
        "_gdch_service_name": "istio",
        "upstream_host": "10.253.168.130:9998",
        "time_unix_nano": 1669165132092378112,
        "severity_text": "",
        "_gdch_namespace": "istio-system",
        "_gdch_service_tenant": "platform-obs",
        "upstream_local_address": "127.0.0.6:58945",
        "body": {},
        "_gdch_cluster": "org-1-system",
        "_gdch_fluentbit_pod": "anthos-audit-logs-forwarder-62rz6"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
