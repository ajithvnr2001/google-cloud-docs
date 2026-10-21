---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-asm/
title: Cloud Service Mesh (CSM) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:34.491985+00:00
---

# Cloud Service Mesh (CSM)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-asm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Cloud Service Mesh (CSM) Stay organized with collections  Save and categorize content based on your preferences. 

Istio is the audited operable component of Cloud Service Mesh.

**Workload location** |  Root and organization workloads  
---|---  
**Audit log source** |  [Istio Service Mesh Envoy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-service-mesh-envoy)  
**Audited operations** |  Received requests and responses  
  
## Received requests and responses

Fields in the log entry that contain audit information  
---  
Audit metadata | Audit field name | Value  
**User or service identity** | `username` |  For example, `"username": "fop-cluster-admin@example.com"`  
**Target** _(Fields and values that call the API)_ | 

  * `authority`
  * `resource.cluster_name`
  * `resource.log_name`
  * `resource.node_name`
  * `resource.zone_name`

|  For example,
    
    
    "authority": "console.zone1.google.gdch.test",
    "resource": {
      "cluster_name": "fleet-admin-platform.gpc-system",
      "log_name": "otel_envoy_accesslog",
      "node_name": "sidecar~10.253.132.163",
      "zone_name": "europe-west4-a"
      }  
  
**Action** _(Fields containing the performed operation)_ | 

  * `body`
  * `bytes_received`
  * `bytes_sent`
  * `connection_termination_details`
  * `downstream_local_address`
  * `downstream_remote_address`
  * `duration`
  * `method`

|  For example,
    
    
    "body": {},
    "bytes_received": "0",
    "bytes_sent": "46259",
    "connection_termination_details": "-",
    "downstream_local_address": "10.253.132.163:80",
    "downstream_remote_address": "10.200.0.1:0",
    "duration": "4",
    "method": "GET"  
  
**Event timestamp** | 

  * `start_time`
  * `time_unix_nano`

|  For example,
    
    
    "start_time": "2022-11-15T23:59:41.041Z",
    "time_unix_nano": 1668556781041333000  
  
**Source of action** | `downstream_remote_address` |  For example, `"downstream_remote_address": "10.200.0.1:0"`  
**Outcome** | `response_code` |  For example, `"response_code": "200"`  
**Other fields** | _Not applicable_ | _Not applicable_  
  
**Example log**
    
    
    {
      "authority":"cortex-tenant.obs-system.svc:9009",
      "body":{},
      "bytes_received":"573",
      "bytes_sent":"19",
      "connection_termination_details":"-",
      "downstream_local_address":"10.253.132.167:9009",
      "downstream_remote_address":"10.253.132.122:48272",
      "duration":"1",
      "method":"POST",
      "observed_time_unix_nano":0,
      "path":"/push",
      "protocol":"HTTP/1.1",
      "requested_server_name":"-",
      "resource":{
        "cluster_name":"cortex-tenant.obs-system",
        "log_name":"otel_envoy_accesslog",
        "node_name":"sidecar~10.253.132.167~cortex-tenant-7b9678cfb5-tl4xz.obs-system~obs-system.svc.cluster.local",
        "zone_name":"us-east1-b"
        },
      "response_code":"503",
      "response_code_details":"via_upstream",
      "response_flags":"-",
      "route_name":"default",
      "severity_number":0,
      "severity_text":"",
      "start_time":"2022-11-18T15:59:55.958Z",
      "time_unix_nano":1668787195958027000,
      "upstream_cluster":"inbound|9009||",
      "upstream_host":"10.253.132.167:9009",
      "upstream_local_address":"127.0.0.6:43899",
      "upstream_transport_failure_reason":"-",
      "user_agent":"Prometheus/2.29.2",
      "username":"-",
      "x_envoy_upstream_service_time":"1",
      "x_forwarded_for":"-",
      "x_goog_api_client":"-",
      "x_request_id":"9e942509-9d28-4164-850f-9666b3eb272e"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
