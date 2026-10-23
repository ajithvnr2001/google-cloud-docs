---
url: https://docs.cloud.google.com/secure-web-proxy/docs/monitor-logs/
title: Logs, metrics, and traces \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:14.957298+00:00
---

# Logs, metrics, and traces  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/monitor-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Logs, metrics, and traces Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how Secure Web Proxy logs its operational data, how to use Cloud Monitoring API metrics to analyze the proxy performance, and how you can use distributed tracing to observe request lifecycles.

## Logs

Secure Web Proxy uses Cloud Logging to let you capture information and perform various tasks in the following key areas:

  * **Monitoring and compliance**

    * Enforce compliance with regulations, improve network security, and provide visibility into the outbound web traffic that's sent to allowed external destinations.
    * Acquire valuable layers of control and visibility over workload traffic.
    * Gain critical insights for effective Security Operations Center (SOC) monitoring.
    * Use logs to detect and track security events to respond to threats proactively.
  * **Deployment and configuration**

    * Track your initial infrastructure setup, user account creation, and configuration changes.
    * Monitor for potential errors to help ensure a smooth and secure deployment.
    * Understand the impact of policy-tuning adjustments and optimize your protection.



### Types of logs

Secure Web Proxy uses Logging to capture and store the following types of logs:

  * [Cloud Audit Logs](https://docs.cloud.google.com/secure-web-proxy/docs/audit-logging): capture administrative changes and data access to your Secure Web Proxy resources. These logs include the following:

    * [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) for API calls and other actions that modify your Secure Web Proxy resources like gateways and policies. Admin Activity logs are always enabled.

    * [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access), if enabled.

  * [Proxy transaction logs](https://docs.cloud.google.com/secure-web-proxy/docs/view-proxy-transaction-logs): capture details about specific web requests that your Secure Web Proxy processes. These logs provide insights into the traffic flow, policy enforcement, and performance of your Secure Web Proxy instance.




### Configure log alerts

You can configure alerts for events that Secure Web Proxy writes to Logging, such as traffic denials or specific rule matches. For general instructions about how to set up these alerts, see [Configure log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

Here are a few examples of queries that you can use to configure log-based alerts for Secure Web Proxy:

#### Alert for traffic denied by a Secure Web Proxy policy

Use the following query to trigger an alert when your Secure Web Proxy policy denies a request:
    
    
    logName="projects/PROJECT_ID/logs/networkservices.googleapis.com%2Fgateway_requests"
    resource.type="networkservices.googleapis.com/Gateway"
    jsonPayload.enforcedGatewaySecurityPolicy.matchedRules.action="DENIED"
    

Replace `PROJECT_ID` with the ID of your target Google Cloud project.

#### Alert for traffic denied by a Secure Web Proxy rule

Use the following query to trigger an alert when a specific Secure Web Proxy rule (such as, `my-specific-deny-rule`) denies a request:
    
    
    logName="projects/PROJECT_ID/logs/networkservices.googleapis.com%2Fgateway_requests"
    resource.type="networkservices.googleapis.com/Gateway"
    jsonPayload.enforcedGatewaySecurityPolicy.matchedRules.action="DENIED"
    AND jsonPayload.enforcedGatewaySecurityPolicy.matchedRules.name=~"projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/POLICY_NAME/rules/my-specific-deny-rule$"
    

Replace the following:

  * `PROJECT_ID`: ID of your target Google Cloud project
  * `REGION`: region of your Secure Web Proxy instance
  * `POLICY_NAME`: name of your Secure Web Proxy policy



#### Alert for traffic throttled by a service rate limiting policy

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use the following query to trigger an alert when a service rate limiting policy throttles a request:
    
    
    logName="projects/PROJECT_ID/logs/networkservices.googleapis.com%2Fgateway_requests"
    resource.type="networkservices.googleapis.com/Gateway"
    jsonPayload.rateLimitPolicyInfo.overallResult="THROTTLED"
    

Replace `PROJECT_ID` with the ID of your target Google Cloud project.

#### Alert for high latency requests

Use the following query to get notified when requests exceed a certain latency, such as five seconds:
    
    
    logName="projects/'PROJECT_ID'/logs/networkservices.googleapis.com%2Fgateway_requests"
    resource.type="networkservices.googleapis.com/Gateway"
    latency >= "5s"
    

Replace `PROJECT_ID` with the ID of your target Google Cloud project.

### View logs in Cloud Logging

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select your Google Cloud project.

  3. Use the drop-down menus to select either the `networkservices.googleapis.com/Gateway` resource or your Secure Web Proxy instance.


**Note:** If you [enable global access](https://docs.cloud.google.com/secure-web-proxy/docs/configure-global-access) for your Secure Web Proxy instance, then the logs include information about the region of origin for the outbound traffic. This data can help you differentiate between local regional traffic and cross-region traffic for auditing and troubleshooting purposes.

For more information, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### Examples of log entries

Secure Web Proxy generates detailed log entries each time it processes a request, keeping track of its actions and applied policies. The following examples show how Secure Web Proxy logs work.

#### Example of an allow log entry

The following log entry shows that the Secure Web Proxy instance intercepted and inspected the HTTPS traffic for [`www.example.com`](https://www.example.com), and then allowed it to proceed to the destination website. The policy and rule names are `swp-policy` and `allow-port-443`, respectively.

Field | Values  
---|---  
`enforcedGatewaySecurityPolicy` | 
    
    
    {
            "requestWasTlsIntercepted": true,
            "hostname": "www.example.com",
            "matchedRules": [
              {
                "action": "ALLOWED",
                "name": "projects/76537/locations/us-central1/gatewaySecurityPolicies/swp-policy/rules/allow-port-443"
              }
            ]
          }  
  
`httpRequest` | 
    
    
    {
            "requestMethod": "GET",
            "requestUrl": "https://www.example.com/",
            "requestSize": "41",
            "status": 200,
            "responseSize": "1446",
            "userAgent": "curl/7.74.0",
            "remoteIp": "10.128.0.12:35418",
            "serverIp": "93.184.216.34:443",
            "latency": "0.051800s",
            "protocol": "HTTP/2"
          }  
  
`resource` | 
    
    
    {
            "type": "networkservices.googleapis.com/Gateway",
            "labels": {
              "gateway_name": "multi-level-tlds",
              "network_name": "projects/76537/global/networks/default",
              "location": "us-central1",
              "resource_container": "",
              "gateway_type": "SECURE_WEB_GATEWAY"
            }
          }  
  
`timestamp` | "2024-02-15T16:56:19.570534Z"  
`severity` | "INFO"  
`logName` | "projects/76537/logs/networkservices.googleapis.com%2Fgateway_requests"  
`receiveTimestamp` | "2024-02-15T16:56:20.714988329Z"  
  
#### Example of a deny log entry

This log entry shows that the Secure Web Proxy instance inspected the traffic for [`www.example.com:443`](http://www.example.com:443) and denied the HTTPS request due to the `default_denied` rule in the Secure Web Proxy policy.

Field | Values  
---|---  
`enforcedGatewaySecurityPolicy` | 
    
    
    {
            "hostname": "www.example.com:443",
            "matchedRules": [
              {
                "name": "default_denied",
                "action": "DENIED"
              }
            ]
          }  
  
`httpRequest` | 
    
    
    {
            "requestMethod": "CONNECT",
            "requestSize": "122",
            "status": 403,
            "responseSize": "141",
            "userAgent": "curl/7.74.0",
            "remoteIp": "10.128.0.12:36338",
            "latency": "0.000133s",
            "protocol": "HTTP/1.1"
          }  
  
`resource` | 
    
    
    {
            "type": "networkservices.googleapis.com/Gateway",
            "labels": {
              "gateway_type": "SECURE_WEB_GATEWAY",
              "resource_container": "",
              "location": "us-central1",
              "network_name": "projects/gcp-1768/global/networks/default",
              "gateway_name": "high-latency-repro"
            }
          }  
  
`timestamp` | "2024-02-15T16:55:00.089727Z"  
`severity` | "WARNING"  
`logName` | "projects/gcp-1768/logs/networkservices.googleapis.com%2Fgateway_requests"  
`receiveTimestamp` | "2024-02-15T16:55:04.456901833Z"  
  
#### Example of a service rate limiting policy log entry

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following log entry shows that the Secure Web Proxy instance throttled a request because the client exceeded the `RateLimitPolicy` (named `rl-egress-policy`) under the `rl_default_rpm_limit` `RateLimitBucket`.

Field | Values  
---|---  
`rateLimitPolicyInfo` | 
    
    
    {
              "policies": [
                {
                  "name": "projects/76537/locations/us-central1/rateLimitPolicies/rl-egress-policy",
                  "buckets": [
                    {
                      "bucket": "rl_default_rpm_limit",
                      "key": "spiffe://projects-123.global.workload.id.goog/ns/ns1/sa/hellomcp",
                      "result": "THROTTLED"
                    }
                  ],
                  "result": "THROTTLED",
                  "details": "Default user rate limit rate exceeded client-side."
                }
              ],
              "overallResult": "THROTTLED"
            }  
  
`httpRequest` | 
    
    
    {
              "requestMethod": "POST",
              "requestUrl": "https://example.com/v1/chat/completions",
              "requestSize": "144",
              "status": 429,
              "responseSize": "85",
              "userAgent": "curl/7.74.0",
              "remoteIp": "10.128.0.12:35418",
              "serverIp": "93.184.216.34:443",
              "latency": "0.001200s",
              "protocol": "HTTP/2"
            }  
  
`resource` | 
    
    
    {
              "type": "networkservices.googleapis.com/Gateway",
              "labels": {
                "gateway_type": "SECURE_WEB_GATEWAY",
                "resource_container": "",
                "location": "us-central1",
                "network_name": "projects/76537/global/networks/default",
                "gateway_name": "egress-swp-gateway"
              }
            }  
  
`timestamp` | "2026-02-15T16:56:19.570534Z"  
`severity` | "WARNING"  
`logName` | "projects/76537/logs/networkservices.googleapis.com%2Fgateway_requests"  
`receiveTimestamp` | "2026-02-15T16:56:20.714988329Z"  
  
## Distributed tracing with Cloud Trace

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Secure Web Proxy supports built-in distributed request tracing integrated with [Trace](https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview).

### Log-trace correlation

Every proxy transaction log entry that's written to Logging includes a `trace` field containing the Google Cloud trace resource string:
    
    
    <pre class="devsite-click-to-copy">
    "trace": "projects/PROJECT_ID/traces/TRACE_ID"
    </pre>
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `TRACE_ID`: 128-bit (32-character hexadecimal) trace ID from your client or trace span. For example, `4bf92f3577b34da6a3ce929d0e0e4736`.



You can use this trace ID to correlate log entries with their corresponding trace spans:

  * **From Logs to Traces** : in the Logs Explorer, click any log entry's `trace` field and then select **View trace details** to open the full request waterfall in Trace.
  * **From Traces to Logs** : in Trace, click **Show logs** on the **Trace Details** pane to view all proxy transaction logs that are associated with the trace.



For more information, see [Distributed tracing with Trace](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-traces).

## Metrics

Cloud Monitoring API metrics help you observe the performance, health, and usage of your Secure Web Proxy instances.

### Monitored resource

Metrics for Secure Web Proxy are exported under the following monitored resource:

  * `networkservices.googleapis.com/Gateway`: represents a Secure Web Proxy gateway instance.



The following table describes the available resources for `networkservices.googleapis.com/Gateway`. You can use these resources to filter and aggregate your monitoring data.

Label | Description  
---|---  
`resource_container` | ID of the project associated with the Secure Web Proxy gateway instance.  
`location` | Google Cloud region where the gateway is deployed.  
`gateway_id` | Unique name of the Secure Web Proxy gateway instance.  
`gateway_type` | Type of gateway, which is set to `SECURE_WEB_GATEWAY`.  
`network_name` | Name of the Virtual Private Cloud (VPC) network associated with the gateway.  
  
### Available metrics

The following metrics are available for the `Gateway` resource. All metrics are prefixed with `networkservices.googleapis.com/https/`.

**Note:** Use the `proxy_response_code_details` metric to differentiate between successful connections and requests that are blocked by your security policies or URL lists.Metric type | Display name | Kind, Type, Unit | Description  
---|---|---|---  
`networkservices.googleapis.com/https/request_count` | Request count | `DELTA`, `INT64`, `1` | Total number of requests processed by the proxy.  
`networkservices.googleapis.com/https/request_bytes_count` | Request bytes | `DELTA`, `INT64`, `By` | Total number of bytes received in requests.  
`networkservices.googleapis.com/https/response_bytes_count` | Response bytes | `DELTA`, `INT64`, `By` | Total number of bytes sent in responses.  
`networkservices.googleapis.com/https/total_latencies` | Total latencies | `DELTA`, `DIST`, `ms` | Time from when the first byte of a request was received until the last byte of the response was sent.  
`networkservices.googleapis.com/https/backend_latencies` | Backend latencies | `DELTA`, `DIST`, `ms` | Time from when the request was sent to the backend until the first byte of the response was received.  
  
### Create a custom dashboard

To build a custom dashboard for visualizing the performance and traffic trends of your Secure Web Proxy instances, do the following:

  1. In the Google Cloud console, go to the **Dashboards** page.

[Go to Dashboards](https://console.cloud.google.com/monitoring/dashboards)

  2. Click add_box**Create Custom Dashboard**.

  3. Click add_box**Add widget** , and then select the **Line** chart option.

  4. In the **Metric** field, search for `networkservices.googleapis.com/https/request_count`.

  5. In the **Filter** field, you can filter by `gateway_id` if you have configured multiple Secure Web Proxy instances.

  6. In the **Aggregation** section, set the **Alignment Period** to `1 minute` and select `rate` for **Aligner**.

This converts the raw request data into a requests per second rate, making it easier to view and analyze consistent traffic trends over time.

  7. To save the widget, click **Apply**.




## What's next

  * [Distributed tracing overview](https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview)
  * [Trace outbound traffic with Trace](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-traces)
  * [Secure Web Proxy audit logging](https://docs.cloud.google.com/secure-web-proxy/docs/audit-logging)
  * [View proxy transaction logs](https://docs.cloud.google.com/secure-web-proxy/docs/view-proxy-transaction-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
