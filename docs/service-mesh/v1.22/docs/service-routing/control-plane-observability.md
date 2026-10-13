---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/control-plane-observability/
title: Control plane logging and monitoring \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:50.017290+00:00
---

# Control plane logging and monitoring  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/control-plane-observability/

You are viewing archived v1.22 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Control plane logging and monitoring

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This document demonstrates how to use [Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to view logs and metrics for the Cloud Service Mesh control plane.

Using a service mesh gives you the ability to observe traffic to and from services, which allows for richer monitoring and debugging without code changes in the service itself. Log entries can provide important information for troubleshooting your service mesh, including records of successful connections and disconnections, error reports for misconfigured clients, and alerts about API resource conflicts.

## Use cases

The following are three use cases for control plane logging and monitoring:

  * **Cloud Logging for Cloud Service Mesh control plane** : You can securely store, search, analyze, and set alerts on all of your Cloud Service Mesh logging data and events using all the built-in features of Logging. Cloud Service Mesh exports logs to Logging when an Envoy or gRPC client connects or disconnects, as well as when it detects configuration issues.
  * **Cloud Monitoring for Cloud Service Mesh control plane** : Cloud Service Mesh exports a key metric indicating the number of clients connected to the Cloud Service Mesh control plane to Monitoring. You can set up a dashboard in Monitoring and visualize this metric in real time to monitor the health of the mesh as clients connect and disconnect. This also lets you set up an SLO for your mesh.
  * **Troubleshoot issues immediately** : Cloud Service Mesh exports telemetry to Logging and Monitoring by default. No additional setup is necessary to configure logging and monitoring, enabling you to troubleshoot issues at any time, including when you are setting up the mesh for the first time.



## View logs

To view Cloud Service Mesh logs, use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface). The following section presents an example query to view Cloud Service Mesh logs, but you can use the previous link to create your own query.

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Resource** list, 
     * If you use the service routing APIs, select `Gateway Scope` or `Mesh`.
     * If you use the older APIs, select `GCE Network`.
  3. In the **Log name** list, select `trafficdirector.googleapis.com/events`.
  4. Click **Run query**.



### Cloud Service Mesh log entry fields

Field | Description  
---|---  
`node_id` | ID of the xDS-client node, as provided by the xDS-client.  
`client_type` | Type of xDS-client connected to Cloud Service Mesh. Possible values: 

  * `ENVOY`
  * `GRPC-JAVA`
  * `GRPC-C++`
  * `GRPC-PYTHON`
  * `GRPC-GO`
  * `UNKNOWN`

  
`node_ip` | IP address of the node as provided by the client.  
`api_version` | The xDS API version used by xDS clients to connect to Cloud Service Mesh. Possible values are `V2` and `V3`.  
`description` | Text description of the event with additional details.  
  
### Example log entries

Example of the log entry | Description  
---|---  
"Cloud Service Mesh could not find any configuration for xDS client." | This log is generated when the xDS client is rejected by Cloud Service Mesh because no configuration exists. This might be due to the incomplete setup of Cloud Service Mesh-relevant API resources.   
"Client has successfully connected." | This type of log message is generated every time a client connects successfully to Cloud Service Mesh.  
"Client has successfully disconnected." | This type of log message is generated every time an established client is disconnected from Cloud Service Mesh.  
"TRAFFICDIRECTOR_INTERCEPTION_PORT metadata variable is not set. Routing configuration for the interception listener exists, but will be ignored." | This type of log message is generated when Cloud Service Mesh resources are configured correctly, but the `TRAFFICDIRECTOR_INTERCEPTION_PORT` variable is not set in the xDS-client node metadata, so this configuration can not be added to the client.  
"Interception listener is built on the given port 15001, but routing configuration does not exist for it." | This type of log message is generated when the `TRAFFICDIRECTOR_INTERCEPTION_PORT` variable is set in the xDS-client node metadata, but no resources were configured for Cloud Service Mesh to generate a complete xDS response.  
"Sending ADS response from Cloud Service Mesh failed. Last discovery request from the node had an incorrect version and/or nonce." | This type of log message is generated when Cloud Service Mesh could not process xDS response correctly due to corrupted communication from the xDS client. This message indicates an implementation error in the client. We recommend checking the client's logs.  
"Client sending cross-region traffic to backend service `backend_service_id`. Source region: `source_region` Destination region(s): `destination_region1, destination_region2`" | This type of log message is generated when a client reports to Cloud Service Mesh that it sent cross-region traffic from a source region to one or more destination regions.  
  
## View metrics

Cloud Service Mesh exports three metrics to Cloud Monitoring: **xDS API Connected Streams** , **Request count** , and **Request count by zone**. **xDS API Connected Streams** indicates the number of clients that are connected to your control plane; **Request count** indicates the number of requests sent to a backend service, grouped by source region, destination region, and request status. **Request count by zone** indicates the number of requests sent to a backend service, grouped by source zone, destination zone, and request status. To view these metrics, use the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

To view Cloud Service Mesh metrics, do the following:

  1. In the Google Cloud console, go to the **Metrics Explorer** page.

[Go to the Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. In the **Resource type** list, select a resource. 
     * If you use the service routing APIs, select `Gateway Scope` or `Mesh`.
     * If you use the older APIs, select `Network`.
  3. In the **Metric** list, select `connected_clients`.
  4. Return to the **Resource type** list, and then select `Compute Engine Backend Service`.
  5. In the **Metric** list, select either `Request count` or `Request count by zone`.



Alternatively, you can use a query to view the cross-region request count:

  1. Select **MQL**.
  2. In the field, enter the following example query: 
         
         fetch gce_backend_service
         | metric 'trafficdirector.googleapis.com/xds/server/request_count'
         | filter ( ne(metric.source_region, metric.destination_region))
         | align rate(1m)
         | every 1m
         | group_by [metric.source_region, metric.destination_region, resource.backend_service_id],
         [value_request_count_aggregate: aggregate(value.request_count)]
         

  3. Click **Run query**.



## Set up logs-based metrics and alerts

The following steps require that you set up logs-based metrics. For more information about setting up logs-based metrics, see the [overview](https://docs.cloud.google.com/logging/docs/logs-based-metrics#viewing).

You can configure alerts to notify you when user-specified messages appear in your included logs. These alerts can notify the operator when something unexpected occurs. For example, if a change in Cloud Service Mesh configuration results in API resource conflicts, you can receive an alert on the error message. To set up alerts on your log-based metrics, see [Configure charts and alerts](https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts#alert-on-lbm).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
