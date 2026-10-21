---
url: https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections/
title: Monitor Private Service Connect connections \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:16:00.735744+00:00
---

# Monitor Private Service Connect connections  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor Private Service Connect connections

This page describes how to monitor both the producer and consumer sides of Private Service Connect connections.

Private Service Connect exposes key metrics to Cloud Monitoring that give you insights into your Private Service Connect connections.

Metrics are sent automatically to Monitoring. There, you can create custom dashboards, set up alerts, and query the metrics.

For information about monitoring Private Service Connect connections that aren't supported by Private Service Connect metrics, see Limitations.

## Monitor published services

You can monitor published services by using predefined dashboards or Google Cloud metrics.

### View dashboards for published services

Private Service Connect provides a set of predefined dashboards that display the following metrics for a published service:

  * Connected forwarding rules
  * NAT IP addresses in use
  * Open connections
  * New connections
  * Closed connections
  * Network traffic
  * Network packets
  * Dropped sent packets
  * Dropped received packets



To view predefined dashboards from the details page of a particular Private Service Connect published service, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click an existing service.

  4. Click the **Monitoring** tab.

You can change the view of the charts by using the control at the top of the page. Hovering over a point on the graph gives you details for that specific time.




### Metrics for published services

The "metric type" strings in this table must be prefixed with `compute.googleapis.com/`. That prefix has been omitted from the entries in the table.

For a full list of Google Cloud metrics, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

For information about using these metrics for troubleshooting, see [published service troubleshooting](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#dropped-packets).

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`private_service_connect/producer/closed_connections_count` GA ** _(project)_**   
Closed connections count   
`DELTA`, `INT64`, `{connection}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of TCP/UDP connections closed over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/connected_consumer_forwarding_rules` GA ** _(project)_**   
Connected consumer forwarding rules   
`GAUGE`, `INT64`, `1`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Number of Consumer Forwarding Rules connected to a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`private_service_connect/producer/dropped_received_packets_count` GA ** _(project)_**   
Received packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of received packets dropped by a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/dropped_sent_packets_count` GA ** _(project)_**   
Sent packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of sent packets dropped by a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/nat_ip_address_capacity` GA ** _(project)_**   
Nat ip address capacity   
`GAUGE`, `INT64`, `1`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Number of total IP addresses of a PSC Service Attachment resource ID. (Value -1 means the number is larger than the max value of INT64.) Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`private_service_connect/producer/new_connections_count` GA ** _(project)_**   
New connections count   
`DELTA`, `INT64`, `{connection}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of new TCP/UDP connections created over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/open_connections` GA ** _(project)_**   
Open connections   
`GAUGE`, `INT64`, `{connection}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Number of TCP/UDP connections currently open on a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/received_bytes_count` GA ** _(project)_**   
Received bytes count   
`DELTA`, `INT64`, `By`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of bytes received (PSC - > Service) over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/received_packets_count` GA ** _(project)_**   
Received packets count   
`DELTA`, `INT64`, `{packet}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of packets received (PSC - > Service) over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/sent_bytes_count` GA ** _(project)_**   
Sent bytes count   
`DELTA`, `INT64`, `By`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of bytes sent (Service - > PSC) over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/sent_packets_count` GA ** _(project)_**   
Sent packets count   
`DELTA`, `INT64`, `{packet}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of packets sent (Service - > PSC) over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/used_nat_ip_addresses` GA ** _(project)_**   
Used nat ip addresses   
`GAUGE`, `INT64`, `1`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _IP usage of the monitored service attachment. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
  
## Monitor endpoints and backends that connect to published services

This section describes how to monitor Private Service Connect endpoints and backends that connect to published services. The available options depend on the type of consumer (endpoint or backend).

This section doesn't apply to endpoints or backends that connect to Google APIs. For information about monitoring Google APIs, see Limitations.

### View dashboards for endpoints

Private Service Connect provides a set of predefined dashboards that display the following metrics for endpoints that connect to published services:

  * Open connections
  * New connections
  * Closed connections
  * Network traffic
  * Network packets
  * Dropped sent packets
  * Dropped received packets



To view predefined dashboards from the details page of a particular Private Service Connect endpoint, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

  3. Click an endpoint that connects to a published service.

  4. Click the **Monitoring** tab.

You can change the view of the charts by using the control at the top of the page. Hovering over a point on the graph gives you details for that specific time.




### Metrics for endpoints and backends

Both Private Service Connect [endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) and [backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) are monitored as [Private Service Connect Endpoint](https://docs.cloud.google.com/monitoring/api/resources?_gl#tag_compute.googleapis.com/PrivateServiceConnectEndpoint) resources.

The metrics in this table are not generated for endpoints or backends that connect to Google APIs.

The "metric type" strings in this table must be prefixed with `compute.googleapis.com/`. That prefix has been omitted from the entries in the table.

For a full list of Google Cloud metrics, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

For information about using these metrics to troubleshoot endpoints, see [endpoint troubleshooting](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#dropped-packets).

For information about using these metrics to troubleshoot backends, see [backend troubleshooting](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls#dropped-packets).

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`private_service_connect/consumer/closed_connections_count` GA ** _(project)_**   
Closed connections count   
`DELTA`, `INT64`, `{connection}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of TCP/UDP connections closed over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/dropped_received_packets_count` GA ** _(project)_**   
Received packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of received packets dropped by a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/dropped_sent_packets_count` GA ** _(project)_**   
Sent packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of sent packets dropped by a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/new_connections_count` GA ** _(project)_**   
New connections count   
`DELTA`, `INT64`, `{connection}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of new TCP/UDP connections created over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/open_connections` GA ** _(project)_**   
Open connections   
`GAUGE`, `INT64`, `{connection}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Number of TCP/UDP connections currently open on a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/received_bytes_count` GA ** _(project)_**   
Received bytes count   
`DELTA`, `INT64`, `By`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of bytes received (PSC - > Clients) over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/received_packets_count` GA ** _(project)_**   
Received packets count   
`DELTA`, `INT64`, `{packet}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of packets received (PSC - > Clients) over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/sent_bytes_count` GA ** _(project)_**   
Sent bytes count   
`DELTA`, `INT64`, `By`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of bytes sent (Clients - > PSC) over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/sent_packets_count` GA ** _(project)_**   
Sent packets count   
`DELTA`, `INT64`, `{packet}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of packets sent (Clients - > PSC) over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
  
## Define alerting policies

To create a [metrics-based alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui), follow these steps. Use a resource type of `Service Attachment` for metrics about published services. Use a resource type of `Private Service Connect Endpoint` for metrics about endpoints or backends.

### Console

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `the resource type` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select the resource type.
     3. For the **Metric category** , select **Private_service_connect**.
     4. For the **Metric** , select the metric to use for this policy.
     5. Select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Select a condition type and, if necessary, specify a threshold. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). 
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

## View logs

You can view logs for Private Service Connect endpoints and published services by using Cloud Logging. [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) is a fully managed service that lets you store, search, analyze, monitor, and alert on logging data and events.

  * Audit logs let you monitor Private Service Connect activity. [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs are always written.
  * VPC Flow Logs lets you monitor Private Service Connect traffic. You must [enable VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enabling-vpc-flow-logs) for each subnet, VLAN attachment for Cloud Interconnect, or Cloud VPN tunnel that you want to monitor.



You can use these logs to correlate events between the service consumer and service producer. For example, if the connection status of a consumer forwarding rule changes unexpectedly, you can request that the service producer verify their logs for any service attachment deletion or update events.

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. If you don't see the query editor field in the **Query** pane, click the **Show query** toggle.

  3. In the query editor field, enter a query. For example, to view an endpoint's connection status change, enter the following query, replacing `CONSUMER_PROJECT_ID` with the consumer project ID:
         
         resource.type="gce_forwarding_rule"
         log_name="projects/CONSUMER_PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
         protoPayload.methodName="LogPscConnectionStatusUpdate"
         

For more examples of queries that you can run to view common logging events, see Common logging events for endpoints.

  4. Click **Run query**.




For more information about querying your audit logs, see [Viewing audit logs](https://docs.cloud.google.com/logging/docs/audit#view-logs).

### Common logging events for published services

The following table lists common logging events for Private Service Connect published services.

Event description | Logging advanced filter  
---|---  
Service attachment deletion | 
    
    
    resource.type="audited_resource"
    log_name="projects/PRODUCER_PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.labels.method="compute.serviceAttachments.delete"  
  
Service attachment enabling connection reconciliation | 
    
    
    resource.type="audited_resource"
    log_name="projects/PRODUCER_PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.labels.method="compute.serviceAttachments.patch"
    protoPayload.request.reconcileConnections="true"  
  
Service attachment rejecting a consumer project URI | 
    
    
    resource.type="audited_resource"
    log_name="projects/PRODUCER_PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    protoPayload.request.consumerRejectLists="CONSUMER_PROJECT_ID"  
  
Endpoint connection status change due to service attachment connection policy or organization policy | 
    
    
    resource.type="gce_service_attachment"
    log_name="projects/PRODUCER_PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
    protoPayload.methodName="LogPscProducerConnectionStatusChange"  
  
VPC Flow Logs for traffic from a Private Service Connect subnet to any backend VM instance (including GKE nodes) | 
    
    
    resource.type="gce_subnetwork"
    logName="projects/PRODUCER_PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows"
    json_payload.connection.src_ip=~"PSC_SUBNET_REGEX.*"
    jsonPayload.dest_instance.vm_name=~"VM_INSTANCE_PREFIX.*"  
  
Replace the following:

  * `PRODUCER_PROJECT_ID`: the project ID of the service producer.
  * `CONSUMER_PROJECT_ID`: the project ID of the service consumer.
  * `PSC_SUBNET_REGEX`: a regular expression that matches a pattern in the Private Service Connect subnet. For example, replace `PSC_SUBNET_REGEX` with `172\.16\.[0-1]` if the Private Service Connect subnet is `172.16.0.0/23`.
  * `VM_INSTANCE_PREFIX`: the prefix of the backend VM instances.



### Common logging events for endpoints

The following table lists common logging events for Private Service Connect endpoints.

Event description | Logging advanced filter  
---|---  
Private Service Connect endpoint creation | 
    
    
    resource.type="gce_forwarding_rule"
    log_name="projects/CONSUMER_PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    protoPayload.methodName="v1.compute.forwardingRules.insert"
    "compute.forwardingRules.pscCreate"  
  
Private Service Connect endpoint creation failure | 
    
    
    resource.type="gce_forwarding_rule"
    log_name="projects/CONSUMER_PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    protoPayload.methodName="v1.compute.forwardingRules.insert"
    "compute.forwardingRules.pscCreate"
    severity>=ERROR  
  
Private Service Connect endpoint connection status change | 
    
    
    resource.type="gce_forwarding_rule"
    log_name="projects/CONSUMER_PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
    protoPayload.methodName="LogPscConnectionStatusUpdate"  
  
Rejected Private Service Connect endpoint connection | 
    
    
    resource.type="gce_forwarding_rule"
    log_name="projects/CONSUMER_PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
    protoPayload.methodName="LogPscConnectionStatusUpdate"
    protoPayload.metadata.pscConnectionStatus="REJECTED"  
  
Quota `PSC_INTERNAL_LB_FORWARDING_RULES` exceeded | 
    
    
    resource.type="gce_forwarding_rule"
    log_name="projects/CONSUMER_PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    protoPayload.methodName="v1.compute.forwardingRules.insert"
    "QUOTA_EXCEEDED"
    severity=ERROR  
  
VPC Flow Logs for traffic from a VM instance to a Private Service Connect endpoint | 
    
    
    resource.type="gce_subnetwork"
    logName="projects/CONSUMER_PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows"
    jsonPayload.connection.dest_ip="PSC_ENDPOINT_IP_ADDRESS"
    jsonPayload.src_instance.vm_name="VM_INSTANCE_NAME"  
  
VPC Flow Logs for traffic from a gateway to a Private Service Connect endpoint | 
    
    
    resource.type="vpc_flow_logs_config"
    logName="projects/CONSUMER_PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows"
    jsonPayload.connection.dest_ip="PSC_ENDPOINT_IP_ADDRESS"
    jsonPayload.src_gateway.name="GATEWAY_NAME"  
  
Replace the following:

  * `CONSUMER_PROJECT_ID`: the project ID of the service consumer.
  * `PSC_ENDPOINT_IP_ADDRESS`: the IP address of the Private Service Connect endpoint.
  * `VM_INSTANCE_NAME`: the name of a source VM instance in the project of the service consumer.
  * `GATEWAY_NAME`: the name of a source VLAN attachment or Cloud VPN tunnel in the project of the service consumer.



### Logging events for Composite Health

If a published service is configured to use [Composite Health](https://docs.cloud.google.com/vpc/docs/about-composite-health), you can use the following queries in the Logs Explorer to view [health state](https://docs.cloud.google.com/vpc/docs/about-composite-health#health-states) transitions. These logs are generated each time a monitored resource changes its state—for example, from `HEALTHY` to `UNHEALTHY`.

Logging is enabled by default for producer resources (health sources and composite health checks) and consumer resources (Private Service Connect NEGs that connect to published services that use Composite Health).

Event description | Logging advanced filter  
---|---  
Producer health state transitions | 
    
    
    logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fcompositehealth"  
  
Consumer health state transitions | 
    
    
    logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fservicehealthchecks"  
  
Replace `PROJECT_ID` with your project ID.

## Limitations

Private Service Connect metrics have the following limitations:

  * **Unsupported load balancers** : Private Service Connect metrics aren't generated for services that are published through global external proxy Network Load Balancers or global external Application Load Balancers.

To monitor services that use these load balancers, use the load balancer's metrics and logs. For more information, see the following:

    * [Proxy Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring)
    * [Global external Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring)
  * **Google APIs** : Private Service Connect metrics aren't available for endpoints or backends that connect to Google APIs. You can use one of the following alternative methods to monitor connections to Google APIs:

    * **Use load balancer monitoring with Private Service Connect backends** : If you connect to Google APIs by using a Private Service Connect backend, you can use the load balancer's metrics and logging to monitor API traffic. For more information, see [External Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logs-monitor-overview).
    * **Use VPC Flow Logs with Private Service Connect endpoints** : If you connect to Google APIs by using a Private Service Connect endpoint, you can monitor API traffic by configuring [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs). You can analyze information from VPC Flow Logs by using [Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview).



## What's next

  * [Learn more about Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)
  * [Learn more about Logging](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
