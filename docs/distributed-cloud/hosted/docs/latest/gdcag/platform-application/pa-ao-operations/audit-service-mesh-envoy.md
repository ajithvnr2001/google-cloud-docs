---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-service-mesh-envoy/
title: Service Mesh Envoy access logs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:16:04.720041+00:00
---

# Service Mesh Envoy access logs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-service-mesh-envoy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Service Mesh Envoy access logs Stay organized with collections  Save and categorize content based on your preferences. 

Applications (Envoy sidecars) that generate audit logs on the service mesh upon receiving requests have the following log format.

**JSON representation**
    
    
    {
      "bytes_sent": string,
      "x_forwarded_for": string,
      "severity_text": string,
      "observed_time_unix_nano": integer,
      "user_agent": string,
      "x_request_id": string,
      "start_time": string,
      "upstream_local_address": string,
      "connection_termination_details": string,
      "severity_number": integer,
      "resource": {
        object
      },
      "x_envoy_upstream_service_time": string,
      "response_code_details": string,
      "upstream_host": string,
      "duration": string,
      "upstream_cluster": string,
      "upstream_transport_failure_reason": string,
      "authority": string,
      "username": string,
      "protocol": string,
      "route_name": string,
      "requested_server_name": string,
      "method": string,
      "time_unix_nano": integer,
      "bytes_received": string,
      "path": string,
      "response_flags": string,
      "x_goog_api_client": string,
      "body": {
        object
      },
      "downstream_local_address": string,
      "downstream_remote_address": string,
      "response_code": string
    }
    

Fields  
---  
`bytes_sent` |  `string` The bytes sent in the body. For a websocket connection, it also includes the bytes sent in the response header. For example, `"46259"`  
`x_forwarded_for` |  `string` The IP addresses visited by a request from the client to the server. For example, `"10.200.0.1"`  
`severity_text` |  `string` Information about the severity level of the log entry. It might be an empty value.  
`observed_time_unix_nano` |  `integer` The UNIX epoch time in nanoseconds of the log entry collection. For example, `1668556781041333000`  
`user_agent` |  `string` The name of the software that retrieves, renders, and facilitates end-user interaction with the web content. It also refers to the user interface implemented using web technologies. For example, `"Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"`  
`x_request_id` |  `string` The unique ID of a single request. For example, `"a4cadca4-662f-4a9c-af63-39a5b3275d8b"`  
`start_time` |  `string` The start time of the request up to milliseconds. For example, `"2022-11-15T23:59:41.041Z"`  
`upstream_local_address` |  `string` The local address of the upstream connection. If it is an IP address, it includes the address and the port. For example, `"127.0.0.6:42179"`  
`connection_termination_details` |  `string` Additional information about why Envoy terminated the connection. It might be an empty value.  
`severity_number` |  `integer` The severity level of the log entry. For example, `0`  
`resource` |  `object` The attributes of the Envoy resource that produced the log entry. These attributes are in key-value pairs in the object. For example,
    
    
    {
      "log_name": string,
      "cluster_name": string,
      "node_name": string,
      "zone_name": string
    }  
  
`x_envoy_upstream_service_time` |  `string` The time in milliseconds that the upstream host spent processing the request. For example, `"0"`  
`response_code_details` |  `string` Additional information about the response code, such as who set it (the upstream or Envoy) and why. For example, `"via_upstream"`  
`upstream_host` |  `string` The URL of the upstream host. For example, `"10.253.132.163:80"`  
`duration` |  `string` Total duration in milliseconds of the request from the start time to the last byte out. For example, `"4"`  
`upstream_cluster` |  `string` The cluster to which the upstream host belongs. For example, `"inbound|80||"`  
`upstream_transport_failure_reason` |  `string` If the upstream connection fails due to a transport socket, it provides the failure reason from the transport socket. The format of this field depends on the configured upstream transport socket. For example, `"SSLV3_ALERT_CERTIFICATE_EXPIRED"`  
`authority` |  `string` The host and port information from the target URI. For example, `"console.zone1.google.gdch.test"`  
`username` |  `string` The user identity that initiated the request. For example, `"fop-cluster-admin@example.com"`  
`protocol` |  `string` The protocol type of the request. For example, `"HTTP/1.1"`  
`route_name` |  `string` The name of the route. For example, `"default"`  
`requested_server_name` |  `string` The value set on the SSL connection socket for Server Name Indication (SNI). For example, `"outbound_.80_._.fleet-admin-platform-admin-ui.gpc-system.svc.cluster.local"`  
`method` |  `string` The name of the method. For example, `"GET"`  
`time_unix_nano` |  `integer` The UNIX epoch time in nanoseconds of the log entry collection. For example, `1668556781041333000`  
`bytes_received` |  `string` The bytes received in the body. For example, `"0"`  
`path` |  `string` The path of the HTTP request. For example, `"/metrics"`  
`response_flags` |  `string` Additional details about the response or connection, if any. For example, `"UH (no healthy upstream hosts)"`  
`x_goog_api_client` |  `string` The API client identification. It might be an empty value.  
`body` |  `object` The request body. It might be an empty value.  
`downstream_local_address` |  `string` The local address of the downstream connection. If it is an IP address, it includes the address and the port. For example, `"10.253.132.163:80"`  
`downstream_remote_address` |  `string` The remote address of the downstream connection. If it is an IP address, it includes the address and the port. For example, `"10.200.0.1:0"`  
`response_code` |  `string` The HTTP response code. Possible values:

  * `"200"` _(Success)_
  * `"403"` _(Forbidden request)_
  * `"500"` _(Error)_

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
