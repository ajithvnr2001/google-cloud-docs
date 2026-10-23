---
url: https://docs.cloud.google.com/secure-web-proxy/docs/view-proxy-transaction-logs/
title: View proxy transaction logs \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:59:32.051129+00:00
---

# View proxy transaction logs  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/view-proxy-transaction-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  View proxy transaction logs Stay organized with collections  Save and categorize content based on your preferences. 

Proxy transaction logs provide detailed information about each request that Secure Web Proxy processes. These logs include a record of every transaction that Secure Web Proxy mediates between users and the internet. This document explains how to access and interpret the transaction logs that your Secure Web Proxy instances generate.

## Types of proxy transaction log entries

Proxy transaction log entries are of three types:

  * HttpRequest
  * LoadBalancerLogEntry
  * GatewayLogEntry



These logs are useful for the following actions:

  * Security analysis and threat detection
  * Troubleshooting connectivity and policy issues
  * Auditing web access
  * Secure Web Proxy performance analysis



### HttpRequest

These log entries contain the following information:

Name | Type | Description  
---|---|---  
`requestMethod` | String  | Type of request method, such as `GET`, `HEAD`, `PUT`, or `POST`.   
`requestUrl` | String  | Scheme (`http` or `https`), hostname, path, and the query portion of the requested URL. For example, `http://example.com/some/info?color=red`.   
`requestSize` |  String ([int64](https://developers.google.com/discovery/v1/type-format) format) | Size, in bytes, of the HTTP request message, including the request headers and request body.  
`status` | Integer  | HTTP or HTTPS status code that indicates the response. For example, `200 OK` or `404 Not Found`.   
`responseSize` |  String ([int64](https://developers.google.com/discovery/v1/type-format) format) | Size, in bytes, of the HTTP status code that's sent back to the client, including the headers and body.  
`userAgent` | String  | User agent that the client sends, such as `Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)`.   
`remoteIp` | String  | IP address (IPv4 or IPv6) of the client that issued the HTTP request. This field can include port information. For example, `192.168.1.1`, `10.0.0.1:80`, and `FE80::0202:B3FF:FE1E:8329`.   
`serverIp` | String  | IP address (IPv4 or IPv6) of the origin server to which the request was sent. This field can include port information. For example, `192.168.1.1`, `10.0.0.1:80`, and `FE80::0202:B3FF:FE1E:8329`.   
`referrer` | String  | Referrer URL of the request, as defined in [HTTP/1.1 Header Field Definitions](https://datatracker.ietf.org/doc/html/rfc2616#section-14.36).   
`latency` |  String ([Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration) format) | Request processing latency on the server, from the time the request was received until the response was sent. Latency is a duration in seconds with up to nine fractional digits and ends with `s`, such as `3.5s`.  
`cacheLookup` | Boolean  | Indicates whether a cache lookup was attempted.   
`cacheHit` | Boolean  | Indicates whether an entity was served from the cache (with or without validation).   
`cacheValidatedWithOriginServer` | Boolean  | Indicates whether the response was validated with the origin server before being served from the cache. This field is meaningful only if `cacheHit` is `True`.   
`cacheFillBytes` |  String ([int64](https://developers.google.com/discovery/v1/type-format) format) | Number of HTTP status code bytes that are inserted.  
`protocol` | String  | Protocol used for the request, such as `HTTP/1.1`, `HTTP/2`, and `websocket`.   
  
### LoadBalancerLogEntry

These log entries contain the following information:

Name | Type | Description  
---|---|---  
`insertId` | String  | Unique log ID.   
`jsonPayload.@type` | String  | Log type. The log type value is always `type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry`.   
`jsonPayload.enforcedGatewaySecurityPolicy.hostname` | String  | Hostname associated with the request.   
`jsonPayload.enforcedGatewaySecurityPolicy.matchedRules.action` | String  | Action taken on the request.   
`jsonPayload.enforcedGatewaySecurityPolicy.matchedRules.rule` | String  | Name of the rule applied to the request.   
`jsonPayload.enforcedGatewaySecurityPolicy.clientServiceAccount` | String  | Service account associated with the request.   
`jsonPayload.enforcedGatewaySecurityPolicy.clientSecureTags` | String  | Secure tags associated with the request.   
  
### GatewayLogEntry

These log entries contain the following information:

Name | Type | Description  
---|---|---  
`resource_container` | String  | Container associated with the gateway.   
`location` | String  | Name of the region in which the gateway is defined.   
`network_name` | String  | Name of the Virtual Private Cloud (VPC) network in which the gateway was created.   
`gateway_type` | String  | Enum type of the gateway. For Secure Web Proxy, the value must be `SECURE_WEB_GATEWAY`.   
`gateway_name` | String  | Name of the gateway resource.   
  
## Format of proxy transaction logs

Proxy transaction logs are written to Cloud Logging with the log name as `projects/PROJECT_ID/logs/networkservices.googleapis.com%2Fgateway_requests`.

The JSON payload of each log entry contains detailed information about the transaction. Log entries contain the following key fields:

Name | Type | Description  
---|---|---  
`destination_ip` | String | Resolved IP address of the destination.  
`instance` | String | Name of the Secure Web Proxy instance that processed the request.  
`mtls_info` | Object | Information about the mTLS handshake, if applicable.  
`policy_evaluation_results` | Object | Information about which rules were matched and the resulting action, such as `allow` or `deny`.  
`request_host` | String | Requested hostname.  
`request_method` | String | HTTP method, such as `GET` or `POST`.  
`request_path` | String | Path of the request.  
`request_port` | Integer | Destination port.  
`request_protocol` | String | HTTP protocol version.  
`request_scheme` | String | Scheme of the URL request, such as `http` or `https`.  
`request_time` | Timestamp | Date and time at which the proxy received the request. The timestamp is specified in `ISO 8601` format: `YYYY-MM-DDTHH:MM:SS.MsMsMsZoneOffset`. For example, `2025-06-03T11:52:26.452Z`.  
`response_code` | Integer | HTTP status code that's returned to the client.  
`response_size` | Integer | Size of the response body, measured in bytes.  
`response_time` | Timestamp | Date and time at which the proxy sent the response to the client. The timestamp is specified in `ISO 8601` format: `YYYY-MM-DDTHH:MM:SS.MsMsMsZoneOffset`. For example, `2025-06-03T11:52:26.452Z`.  
`source_ip` | String | Client IP address.  
`source_port` | Integer | Client source port.  
`tls_cipher_suite` | String | Cipher suite used for the TLS connection.  
`tls_version` | String | TLS version used for the connection.  
  
## Monitor proxy transaction logs

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select your Google Cloud project.

  3. Use the following query to view all Secure Web Proxy transaction logs:
         
         logName="projects/PROJECT_ID/logs/networkservices.googleapis.com%2Fgateway_requests"
         

Replace `PROJECT_ID` with the ID of your target Google Cloud project.

Here are a few sample queries that you can use to view specific details:

     * Find all denied requests.
           
           logName="projects/PROJECT_ID/logs/networkservices.googleapis.com%2Fgateway_requests"
           jsonPayload.policy_evaluation_results.policy_action="DENY"
           

     * Find requests from a specific source IP address.
           
           logName="projects/PROJECT_ID/logs/networkservices.googleapis.com%2Fgateway_requests"
           jsonPayload.source_ip="192.0.2.1"
           

     * Find requests to a specific host.
           
           logName="projects/PROJECT_ID/logs/networkservices.googleapis.com%2Fgateway_requests"
           jsonPayload.request_host="example.com"
           




## Correlate proxy transaction logs with Cloud Trace

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When distributed tracing is enabled on your Secure Web Proxy gateway, you can correlate proxy transaction log entries with trace spans in Trace by following these steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Expand any `gateway_requests` log entry.

  3. Locate the top-level `trace` field: 
         
         projects/PROJECT_ID/traces/TRACE_ID
           

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project
     * `TRACE_ID`: 128-bit (32-character hexadecimal) trace ID from your client or trace span. For example, `4bf92f3577b34da6a3ce929d0e0e4736`.
  4. Click the `trace` URL, and then select **View trace details** to directly navigate to the trace waterfall in Cloud Trace.

  5. To filter logs for a known trace ID from an OpenTelemetry-instrumented client, run the following query in Logs Explorer:
         
         logName="projects/PROJECT_ID/logs/networkservices.googleapis.com%2Fgateway_requests"
         trace="projects/PROJECT_ID/traces/TRACE_ID"
         




For more information, see [Distributed tracing overview](https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview) and [Trace outbound traffic with Cloud Trace](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-traces).

## Route proxy transaction logs

You can route proxy transaction logs to other destinations like Cloud Storage, BigQuery, or Pub/Sub by using log sinks. For more information, see [Route log entries](https://docs.cloud.google.com/logging/docs/routing/overview).

## What's next?

  * [Distributed tracing overview](https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview)
  * [Trace outbound traffic with Cloud Trace](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-traces)
  * [Logs and monitoring overview](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-logs)
  * [Secure Web Proxy audit logging](https://docs.cloud.google.com/secure-web-proxy/docs/audit-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
