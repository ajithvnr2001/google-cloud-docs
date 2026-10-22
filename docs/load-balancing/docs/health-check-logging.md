---
url: https://docs.cloud.google.com/load-balancing/docs/health-check-logging/
title: Health check logging information \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:35.980564+00:00
---

# Health check logging information  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/health-check-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Health check logging information Stay organized with collections  Save and categorize content based on your preferences. 

You can get logs of load balancing [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) when an endpoint changes in health status. You can use health check logs for the following:

  * Live debugging and troubleshooting your endpoint health status
  * Getting visibility into your endpoint's health status
  * Auditing and compliance purposes



Health checks log health transition information to [Logging](https://docs.cloud.google.com/logging/docs). You enable or disable logging on a per-health check basis.

To see health check logs in Logging, you must ensure that you don't have a logs exclusion that applies to health checks. For instructions about how to verify that `GCE Instance Group` and `Network Endpoint Group` logs are allowed, see [Exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).

## Enable and disable logging

This section describes how to enable logging on a new or an existing health check, and how to disable logging on an existing health check.

### Enable logging on a new health check

###  Console 

  1. In the Google Cloud console, go to the **Health checks** page.

[Go to Health checks](https://console.cloud.google.com/compute/healthChecks)

  2. Click **Create health check**.

  3. For **Logs** , select **On**.

  4. Continue setting up your health check.




###  gcloud 
    
    
    gcloud compute health-checks create PROTOCOL HEALTH_CHECK_NAME \
        --enable-logging
    

The flag `--enable-logging` enables logging for that health check.

###  Terraform 

To create a health check for different protocols with logging, use the [`google_compute_health_check` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_health_check). 
    
    
    resource "google_compute_health_check" "health_check_tcp_with_logging" {
      provider = google-beta
    
      name = "health-check-tcp"
    
      timeout_sec        = 1
      check_interval_sec = 1
    
      tcp_health_check {
        port = "22"
      }
    
      log_config {
        enable = true
      }
    }

For a regional load balancer, use the [`google_compute_region_health_check` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_health_check).

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Enable logging on an existing health check

###  Console 

  1. In the Google Cloud console, go to the **Health checks** page.

[Go to Health checks](https://console.cloud.google.com/compute/healthChecks)

  2. Click the name of your health check.

  3. Click edit**Edit**.

  4. For **Logs** , select **On**.

  5. Click **Save**.




###  gcloud 
    
    
    gcloud compute health-checks update PROTOCOL HEALTH_CHECK_NAME \
        --enable-logging
    

The flag `--enable-logging` enables logging for that health check.

### Disable logging on an existing health check

###  Console 

  1. In the Google Cloud console, go to the **Health checks** page.

[Go to Health checks](https://console.cloud.google.com/compute/healthChecks)

  2. Click the name of your health check.

  3. Click edit**Edit**.

  4. For **Logs** , select **Off**.

  5. Click **Save**.




###  gcloud 
    
    
    gcloud compute health-checks update PROTOCOL HEALTH_CHECK_NAME \
        --no-enable-logging
    

The flag `--no-enable-logging` disables logging for that health check.

## View logs

  1. To view logs, go to the [Logs explorer](https://console.cloud.google.com/logs).

Health check logs are indexed by [instance group](https://docs.cloud.google.com/compute/docs/instance-groups) or [network endpoint group](https://docs.cloud.google.com/load-balancing/docs/negs).

  2. To see all logs, in the **Resource** menu, select either `GCE Instance Group` or `Network Endpoint Group`, depending on the type of backend.

  3. Alternatively, paste the following into the **Query** field. Replace `PROJECT_ID` with your project's ID.
         
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fhealthchecks"
         




You can configure export of [logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) for load balancer health checks.

### Use filters to view logs

You can also get logs based on more specific searches. For example, the following filter shows all logs for a specified backend instance IP address:
    
    
      logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fhealthchecks"
    jsonPayload.healthCheckProbeResult.ipAddress="IP_ADDRESS"
    

Log fields of type _boolean_ typically only appear if they have a value of `true`. If a boolean field has a value of `false`, that field is omitted from the log.

[UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoding is enforced for log fields. Characters that are not UTF-8 characters are replaced with question marks.

## What is logged

Health check log entries contain information useful for monitoring and debugging the state of your endpoints. Log entries contain the following types of information:

  * General information shown in most logs, such as severity, project ID, project number, and timestamp.
  * Fields specific to health checks, described in the following tables.



### Health check states

An endpoint is considered either `HEALTHY` or `UNHEALTHY`. These are the basic states. Within each of these basic states, there are several more detailed states.

_Hybrid NEGs and regional internet NEGs using distributed Envoy health checks do not support detailed health states._

The following table shows the mapping between basic and detailed health states.

Basic health state | Detailed health state  
---|---  
`HEALTHY` | `HEALTHY`  
`DRAINING`  
`UNHEALTHY` | `UNKNOWN`  
`UNHEALTHY`  
`TIMEOUT`  
  
State changes don't always alter the behavior of the load balancer. Consider the following case:

  1. The server is giving the wrong response, so the endpoint is considered `UNHEALTHY`.
  2. The server then stops responding, and the new state is `TIMEOUT`.
  3. The load balancer still considers the endpoint to be `UNHEALTHY` because the detailed `TIMEOUT` state maps to the basic `UNHEALTHY` state.



The following table provides a definition of each health state.

Detailed health check state | Meaning | Basic state  
---|---|---  
`HEALTHY` | The endpoint is reachable and conforms to the requirements defined by the health check.  | `HEALTHY`  
`UNHEALTHY` | The endpoint is reachable but does not conform to the requirements defined by the health check.  | `UNHEALTHY`  
`DRAINING` | The endpoint is being drained. The existing connections to the endpoint are allowed to complete, but the new ones are being refused. Endpoint is considered `HEALTHY`.  | `HEALTHY`  
`TIMEOUT` | The endpoint is unreachable. Depending on the health check type, either a connection to the endpoint cannot be established or the server did not respond within the specified timeout. Endpoint is considered `UNHEALTHY`.  | `UNHEALTHY`  
`UNKNOWN` | The health check system is aware of the endpoint, but its health is not known. Endpoint is considered `UNHEALTHY`.  | `UNHEALTHY`  
  
There are multiple health checkers probing each endpoint; Google Cloud de-duplicates the log entries before logging so that only unique logs are generated.

If a health checker restarts, you might occasionally see the logged health state change from `UNKNOWN` to one of the known states listed earlier even though the endpoint's health state has not actually changed. Google Cloud uses best-effort heuristics to suppress such log entries.

If you are using [connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining), then health check logs are _not_ be generated with the endpoint health status `DRAINING`. This is because health check logs reflect the results observed by the health check probes, and connection draining does not impact the results observed by the health check probe. Connection draining works by just informing the load balancer that the new state is `DRAINING`, and it effectively overrides the true health state of the endpoint as observed by the health checker.

You can interact with the logs by using the Cloud Logging API. The API provides ways to interactively filter logs that have specific fields set and export matching logs to Cloud Logging, Cloud Storage, BigQuery, or Pub/Sub. For more information about the Cloud Logging API, see [Cloud Logging API overview](https://docs.cloud.google.com/logging/docs/reference/api-overview).

### Health check log entry

The [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) `jsonPayload` is populated with a field `healthCheckProbeResult` that contains the following information.

Field | Type | Description  
---|---|---  
`ipAddress` | `string` | The primary internal IP address associated with the primary network interface of each backend VM. This is a human-readable string.  
`healthCheckProtocol` | `enum(HealthCheckProtocol)` | The health check protocol used for health checking the endpoint. Examples: TCP, HTTP, HTTPS.  
`healthState` | `enum(HealthState)` | Current health status of the endpoint: `HEALTHY` or `UNHEALTHY`.  
`previousHealthState` | `enum(HealthState)` | The previous health status of the endpoint: `HEALTHY` or `UNHEALTHY`.  
`detailedHealthState` | `enum(DetailedHealthState)` | Current detailed health status of the endpoint. For a list of possibilities, see Health check states. Not supported for distributed Envoy health checks for hybrid NEGs and regional internet NEGs.  
`previousDetailedHealthState` | `enum(DetailedHealthState)` | The previous detailed health status of the endpoint. For a list of possibilities, see Health check states. Not supported for distributed Envoy health checks for hybrid NEGs and regional internet NEGs.  
`probeRequest` | `string` | For HTTP, HTTPS, and HTTP/2, this is the URL request path (`requestPath` field in the resource config). For TCP/SSL, this is the configured optional string that is sent after the health check connection is established (`request` field in the resource config). Not supported for distributed Envoy health checks for hybrid NEGs and regional internet NEGs.  
`probeCompletionTimestamp` | `google.protobuf.Timestamp` | Probe completion timestamp.  
`connectLatency` | `google.protobuf.Duration` | Time spent on setting up the connection for connection-oriented health check protocols TCP, SSL, HTTP, HTTPS, and HTTP/2. Not supported for distributed Envoy health checks for hybrid NEGs and regional internet NEGs.  
`responseLatency` | `google.protobuf.Duration` | Latency between request and response, as measured by the prober. Not supported for distributed Envoy health checks for hybrid NEGs and regional internet NEGs.  
`probeResultText` | `string` | Descriptive text related to the probe result. It might say something like "Connection timed out" or "HTTP response: Bad Gateway", or it could be empty. Not supported for distributed Envoy health checks for hybrid NEGs and regional internet NEGs.  
`probeSourceIp` | `string` | The IP address from which the health check probe was sent. For distributed Envoy health checks, this corresponds to the proxy IP address from the proxy-only subnet.  
`probeSourceRegion` | `string` | The cloud vantage point region from which the health check originated. This field is populated only for probes of Cloud DNS routing policies if the `sourceRegions` field is set in the corresponding health check.  
`targetIp` | `string` | The IP address that is the target of the probe. This can be different than `ipAddress`. The destination IP address of the probe depends on the type of load balancer. For details, see [ Destination for probe packets](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#hc-packet-dest) in the Health checks overview.   
`targetPort` | `int` | The port that was the target of the probe. This can be the default port of the probe or the port that you specified when you created the health check.  
  
## Example filters

This section provides examples of common log filters.

### Find all health check results for a particular instance group
    
    
    logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fhealthchecks"  AND
    resource.type="gce_instance_group" AND
    resource.labels.instance_group_name="INSTANCE_GROUP_NAME"
    

### Find all health check results for a particular NEG
    
    
    logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fhealthchecks"  AND
    resource.type="gce_network_endpoint_group" AND
    resource.labels.network_endpoint_group_id="ENDPOINT_GROUP_ID"
    

### Find all health check transitions for backend instance IP address `10.128.15.201`
    
    
    logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fhealthchecks"
    jsonPayload.healthCheckProbeResult.ipAddress="10.128.15.201"
    

### Find all endpoints that were previously HEALTHY but now TIMEOUT
    
    
    logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fhealthchecks"
    jsonPayload.healthCheckProbeResult.previousDetailedHealthState="HEALTHY"
    jsonPayload.healthCheckProbeResult.detailedHealthState="TIMEOUT"
    

### Find health logs from a specific time range
    
    
    logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fhealthchecks"
    timestamp>"2019-02-14T02:20:00.0Z"
    timestamp<"2019-02-14T03:30:00.0Z"
    

## Limitations

  * Logs are generated for endpoint health transition only.
  * [Legacy health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#legacy-health-checks) are not supported.
  * Target pools are not supported.
  * Logs are not generated when the endpoint's health state is `UNKNOWN`.
  * In case of VM migrations, you might not see any log entries generated when the endpoint's health transitions to the `UNHEALTHY` state.
  * Logs are not generated when endpoints are deleted. For example, when you stop a VM.



## What's next

  * Read [conceptual information about health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).
  * Create a [health check](https://docs.cloud.google.com/load-balancing/docs/health-checks).
  * Read about [Logging](https://docs.cloud.google.com/logging/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
