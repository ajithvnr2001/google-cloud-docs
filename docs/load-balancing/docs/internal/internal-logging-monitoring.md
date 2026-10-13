---
url: https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring/
title: Internal passthrough Network Load Balancer logging and monitoring \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:59.168651+00:00
---

# Internal passthrough Network Load Balancer logging and monitoring  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Internal passthrough Network Load Balancer logging and monitoring Stay organized with collections  Save and categorize content based on your preferences. 

To gain operational insights into your internal passthrough Network Load Balancers, you can integrate [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring). These services provide data such as traffic distribution, backend health, and connection errors, enabling you to monitor performance and troubleshoot issues with your load balancer.

## Logging

Logs provide useful information for troubleshooting and monitoring the passthrough Google Cloud load balancer. Logs are aggregated per connection and exported in near real time. Logs are generated for each load-balanced instance TCP and UDP flows for both ingress and egress traffic. For more information about the fields provided in the log entry, see Log fields.

There are no additional charges for using logs. Based on how you ingest logs, standard pricing for [Cloud Logging](https://cloud.google.com/stackdriver/pricing#google-clouds-operations-suite-pricing), BigQuery, or Pub/Sub apply. Enabling logs has no effect on the performance of the load balancer.

Logging provides the following benefits:

  * **Internal passthrough Network Load Balancer traffic monitoring.** Per-connection logging gives you insight into how each connection is routed to serving backends.

  * **Network troubleshooting.** You can utilize internal passthrough Network Load Balancer logs for troubleshooting. For more information, see [Troubleshoot internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/troubleshooting-ilb).




### Sample log format for VM to VM flows

The following diagram shows the inbound and outbound traffic for an internal client (192.168.1.2), internal passthrough Network Load Balancer (10.240.0.200), and backend instance (10.240.0.3).

[ ![Internal client to backend VM services flows.](https://docs.cloud.google.com/static/load-balancing/images/tcpudp_ilb_logging.svg)](https://docs.cloud.google.com/static/load-balancing/images/tcpudp_ilb_logging.svg) Inbound and outbound flows for VM to VM flows.

Internal passthrough Network Load Balancer logs for connections from the client to the backend instance are formatted as follows:

  * `connection.clientIp`: 192.168.1.2
  * `connection.serverIp`: 10.240.0.200
  * `bytesSent`: 1256
  * `bytesReceived`: 4521



### Logs sampling and collection

Google Cloud samples the packets that leave and enter load balancer backend VMs. Those sampled packets are processed to generate logs.

Not every packet is sampled. Google Cloud samples a variable subset of packets depending on the amount of traffic on the physical host. The lowest possible sampling rate is one out of 1,024 packets. The sampling rate is dynamically controlled by Google Cloud. You cannot adjust the sampling rate.

The packet sampling interacts with firewall rules in the following ways:

  * Packets are sampled _before_ egress firewall rules are applied.
  * Packets are sampled _after_ ingress firewall rules are applied.



After packet sampling, Google Cloud processes the sampled packets according to the following procedure:

  1. **Aggregation** : Sampled packets are aggregated over a five-second interval to produce a single flow entry.

  2. **Configurable (secondary) log sampling** : This is a second sampling process, sampling the flows. You control the fraction of the flow entries that are emitted as log entries according to the [logConfig.sampleRate](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert#request-body) parameter. When `logConfig.sampleRate` is `1.0` (100%), this means that _all of the sampled packets_ are processed.

  3. **Write to logging** : The log entries are written to Cloud Logging.




### Optional fields

Log records contain required fields and optional fields. The Log fields section lists which fields are optional and which are required. All required fields are always included. You can customize which optional fields you keep.

  * If you select **include all optional** , all optional fields in the log record format are included in the flow logs. When new optional fields are added to the record format, the flow logs automatically include the new fields.

  * If you select **exclude all optional** , this omits all optional fields.

  * If you select **custom** , you can specify the optional fields that you want to include by the parent field, such as `serverInstance`, or by their full names, such as `serverInstance.vm`.

When new optional fields are added to the record format, the logs do not include these fields unless they are a new field within a parent field that you have specified to include.

If you specify a custom optional field by using parent fields, when new optional fields are added to the record format within that parent field, the logs automatically include the new fields. For example, if you choose to include `optionalFieldA`, then a new field added to the logs with the name `optionalFieldA.subField1` is included automatically.




For instructions about customizing optional fields, see Enable logging on a new backend service.

### Response packet source IP address requirements

Internal passthrough Network Load Balancer logging samples the response packets from the backend VMs only if the source IP address for those packets matches the load balancer's forwarding rule IP address. For TCP connections, response packets must always have sources that match the request packet's destination; however, for other protocols, it's possible for response packets to use a different source IP address. For additional details, see [IP addresses for request and return packets](https://docs.cloud.google.com/load-balancing/docs/internal#tcp-udp-request-return).

The packet sampling process used by internal passthrough Network Load Balancers omits any response packets from backend VMs if those response packets have sources that do not match an IP address of a forwarding rule for an internal passthrough Network Load Balancer.

### Enable logging for a new backend service

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the name of your load balancer.

  3. Click edit**Edit** , and then click **Backend Configuration**.

  4. Select **Create a backend service** , and then complete the required backend service fields.

  5. Click **Enable logging**.

  6. Set a **Sample rate** fraction. You can set a rate to `0.0` through `1.0` (default).

  7. Optional: To include all the optional fields in the logs, in the **Optional fields** section, click **Include all optional fields**. 

**Pro tip:** To specify the **CUSTOM** option, use the gcloud CLI and the REST API.

  8. To finish editing the backend service, click **Update**.

  9. To finish editing the load balancer, click **Update**.




###  gcloud 

Create a backend service and enable logging by using the [`gcloud compute backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create).
    
    
    gcloud compute backend-services create BACKEND_SERVICE \
      --region=REGION \
      --enable-logging \
      --logging-sample-rate=SAMPLE_RATE
      --logging-optional=LOGGING_OPTIONAL \
      --logging-optional-fields=OPTIONAL_FIELDS
    

Replace the following:

  * `BACKEND_SERVICE`: the name of the backend service.
  * `REGION`: the region of the backend service to create.
  * `SAMPLE_RATE`: this field can only be specified if logging is enabled for this backend service.

The value of the field must be from `0.0` to `1.0`, where `0.0` means that no logs are reported and `1.0` means that logs are generated for all of the sampled packets. Enabling logging but setting the sampling rate to `0.0` is equivalent to disabling logging. The default value is `1.0`.

  * `LOGGING_OPTIONAL`: the optional annotations that you want to include in the logs:

    * `INCLUDE_ALL_OPTIONAL` to include all optional annotations.

    * `EXCLUDE_ALL_OPTIONAL` (default) to exclude all optional annotations.

    * `CUSTOM` to include a custom list of optional fields that you specify in `OPTIONAL_FIELDS`.

  * `OPTIONAL_FIELDS`: a comma-separated list of optional fields that you want to include in the logs.

For example, `serverInstance.vm, serverGkeDetails`. Can only be set if `LOGGING_OPTIONAL` is set to `CUSTOM`.




###  API 

Make a `POST` request to the [`regionBackendServices.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert) method.
    
    
     POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/backendServices
     

#### Exclude all optional fields
    
    
     {
     "name": "BACKEND_SERVICE",
      "loadBalancingScheme": "INTERNAL",
      "logConfig": {
       "enable": true,
       "sampleRate": SAMPLE_RATE,
       "optionalMode": "EXCLUDE_ALL_OPTIONAL"
      }
     }
    

#### Include all optional fields
    
    
    {
     "name": "BACKEND_SERVICE",
     "loadBalancingScheme": "INTERNAL",
     "logConfig": {
       "enable": true,
       "sampleRate": SAMPLE_RATE,
       "optionalMode": "INCLUDE_ALL_OPTIONAL"
      }
    }
    

#### Include a custom list of optional fields
    
    
    {
     "name": "BACKEND_SERVICE",
     "loadBalancingScheme": "INTERNAL",
     "logConfig": {
       "enable": true,
       "sampleRate": SAMPLE_RATE,
       "optionalMode": "CUSTOM",
       "optionalFields": ["field1","field2",...]
      }
    }
    

### Enable logging on an existing backend service

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the name of your load balancer.

  3. Click edit**Edit** , and then click **Backend Configuration**.

  4. Next to your backend service, click edit**Edit**.

  5. Click **Enable logging**.

  6. Set a **Sample rate** fraction. You can set a rate to `0.0` through `1.0` (default).

  7. Optional: To include all the optional fields in the logs, in the **Optional fields** section, click **Include all optional fields**. 

**Pro tip:** To specify the **CUSTOM** option, use the gcloud CLI and the REST API.

  8. To finish editing the backend service, click **Update**.

  9. To finish editing the load balancer, click **Update**.




###  gcloud 

Enable logging on an existing backend service with the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update).
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
    --region=REGION \
    --enable-logging \
    --logging-sample-rate=SAMPLE_RATE \
    --logging-optional=LOGGING_OPTIONAL \
    --logging-optional-fields=OPTIONAL_FIELDS
    

Replace the following:

  * `BACKEND_SERVICE`: the name of the backend service.
  * `REGION`: the region of the backend service to create.
  * `SAMPLE_RATE`: this field can only be specified if logging is enabled for this backend service.

The value of the field must be from `0.0` to `1.0`, where `0.0` means that no logs are reported and `1.0` means that logs are generated for all of the sampled packets. Enabling logging but setting the sampling rate to `0.0` is equivalent to disabling logging. The default value is `1.0`.

  * `LOGGING_OPTIONAL`: the optional annotations that you want to include in the logs.

    * `INCLUDE_ALL_OPTIONAL` to include all optional annotations.

    * `EXCLUDE_ALL_OPTIONAL` (default) to exclude all optional annotations.

    * `CUSTOM` to include a custom list of optional fields that you specify in `OPTIONAL_FIELDS`.

  * `OPTIONAL_FIELDS`: a comma-separated list of optional fields that you want to include in the logs.

For example, `serverInstance.vm,serverGkeDetails`. Can only be set if `LOGGING_OPTIONAL` is set to `CUSTOM`.




###  API 

Make a `PATCH` request to the [`regionBackendServices/patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/patch) method.
    
    
     PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE
     

#### Exclude all optional fields
    
    
     "logConfig": {
       "enable": true,
       "sampleRate": SAMPLE_RATE,
       "optionalMode": "EXCLUDE_ALL_OPTIONAL"
      }
     

#### Include all optional fields
    
    
     "logConfig": {
       "enable": true,
       "sampleRate": SAMPLE_RATE,
       "optionalMode": "INCLUDE_ALL_OPTIONAL"
      }
     

#### Include a custom list of optional fields
    
    
     "logConfig": {
       "enable": true,
       "sampleRate": SAMPLE_RATE,
       "optionalMode": "CUSTOM",
       "optionalFields": ["field1","field2",...]
      }
    

### Disable logging on an existing backend service

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the name of your load balancer.

  3. Click edit**Edit** , and then click **Backend Configuration**.

  4. To disable logging entirely, clear **Enable logging**.

  5. If you leave logging enabled, you can set a different **Sample rate** fraction. You can set the rate to `0.0` through `1.0` (default). To only generate logs for 20% of the sampled packets, set the value to `0.2`.

  6. To finish editing the backend service, click **Update**.

  7. To finish editing the load balancer, click **Update**.




###  gcloud 

Disable logging on a backend service with the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update).
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
      --region=REGION \
      --no-enable-logging
    

Replace the following:

  * `BACKEND_SERVICE`: the name of the backend service.
  * `REGION`: the region of the backend service to create.



###  API 

Make a `PATCH` request to the [`regionBackendServices/patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/patch) method.
    
    
     PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE
    
    
     {
     "logConfig": {
       "enable": false
      }
     }
     

### View logs

When logs are ingested into Cloud Logging and not excluded through a [Log router sink](https://docs.cloud.google.com/logging/docs/routing/overview#sinks), you can read logs by using the [Cloud Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) and the [Google Cloud CLI](https://docs.cloud.google.com/logging/docs/api/gcloud-logging#reading_log_entries).

To view all the internal passthrough Network Load Balancer logs:

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Select the **Internal Passthrough Network Load Balancer Rule** resource type.

  3. Select the **loadbalancing.googleapis.com/flows** log name.




###  Console query 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Click the **Show query** toggle.

  3. Paste the following into the query field. Replace `PROJECT_ID` with your project ID.
         
         resource.type="loadbalancing.googleapis.com/InternalNetworkLoadBalancerRule"
         logName="projects/PROJECT_ID/logs/loadbalancing.googleapis.com%2Fflows"
         

  4. Click **Run query**.




#### View logs for a backend service

To view the internal passthrough Network Load Balancer logs for a specific backend service:

###  Console query 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Click the **Show query** toggle.

  3. Paste the following into the query field. Replace `PROJECT_ID` with your project ID and `BACKEND_SERVICE_NAME` with the name of your backend service.
         
         resource.type="loadbalancing.googleapis.com/InternalNetworkLoadBalancerRule"
         logName="projects/PROJECT_ID/logs/loadbalancing.googleapis.com%2Fflows"
         resource.labels.backend_service_name="BACKEND_SERVICE_NAME"
         

  4. Click **Run query**.




#### View logs for a backend instance group

To view the internal passthrough Network Load Balancer logs for a specific backend instance group or network endpoint group (NEG) with `GCE_VM_IP` endpoints, follow these steps:

###  Console query 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Click the **Show query** toggle.

  3. Paste the following into the query field. Replace `PROJECT_ID` with your project ID and the `BACKEND_GROUP_NAME` with the name of the instance group or NEG.
         
         resource.type="loadbalancing.googleapis.com/InternalNetworkLoadBalancerRule"
         logName="projects/PROJECT_ID/logs/loadbalancing.googleapis.com%2Fflows"
         resource.labels.backend_group_name="BACKEND_GROUP_NAME"
         

  4. Click **Run query**.




### Log fields

Log records contain required fields—the default fields of every log record—and optional fields that add additional information. Optional fields can be omitted to save storage costs.

Some log fields are in a multi-field format, with more than one piece of data in a given field. For example, the `connection` field is of the `IpConnection` format, which contains the source and destination IP address and port plus the protocol in a single field. These multi-field fields are described in the following record format table.

The monitored resource is [loadbalancing.googleapis.com/InternalNetworkLoadBalancerRule](https://docs.cloud.google.com/logging/docs/api/v2/resource-list).

Field | Field format | Field type: Required or Optional | Description  
---|---|---|---  
**connection** | IpConnection | Required |  5-Tuple describing this connection.  
**startTime** | string | Required |  Timestamp (RFC 3339 date string format) of the first observed packet during the aggregated time interval.  
**endTime** | string | Required |  Timestamp (RFC 3339 date string format) of the last observed packet during the aggregated time interval.  
**bytesSent** | string | Required |  Number of bytes sent from the server to the client.  
**bytesReceived** | int64 | Required |  Number of bytes received by the server from the client.  
**packetsSent** | int64 | Required |  Number of packets sent from the server to the client.  
**packetsReceived** | int64 | Required |  Number of packets received by the server from the client.  
**rtt** | string | Required | Latency is measured only for TCP connections. Latency is the sum of estimated network round-trip time (RTT) plus time consumed processing the packet within the client's VM operating system. For sampled packets, the RTT is calculated from the perspective of a load-balanced backend by measuring time differences between the backend sending a TCP segment and the backend receiving a TCP acknowledgment for the sequence number of the sent segment. Latency is formatted as a string that begins with the number of seconds and ends with "s" to indicate seconds. Nanoseconds is expressed as fractional seconds. For example, the latency of 250 milliseconds is formatted as "0.250000000s".  
**clientInstance** | InstanceDetails | Optional |  VM instance details of the client. Only available if the client's VM instance is located in the same project.  
**serverInstance** | InstanceDetails | Optional |  VM instance details of the backend VM.  
**clientVpc** | VpcDetails | Optional |  VPC network details of the client. Only available if the client is an endpoint inside a VPC network located in the same project.  
**clientGkeDetails** | GkeDetails | Optional |  GKE metadata for the client. Only available if the client is a GKE endpoint in the same project.   
**serverGkeDetails** | GkeDetails | Optional |  GKE metadata for the server backend. Only available if the backend is a GKE endpoint.  
  
#### IpConnection field format

Field | Type | Description  
---|---|---  
**clientIp** | string | Client IP address  
**clientPort** | int32 | Client port. Set for TCP and UDP connections only.  
**serverIp** | string | Server IP address (forwarding rule IP)  
**serverPort** | int32 | Server port. Set for TCP and UDP connections only.  
**protocol** | int32 |  [IANA protocol number](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)  
  
#### InstanceDetails field format

Field | Type | Description  
---|---|---  
**projectId** | string  | ID of the project containing the VM   
**vm** | string  | Instance name of the VM   
**region** | string  | Region of the VM   
**zone** | string  | Zone of the VM   
**vmIp** | string  | Primary internal IP of the NIC that served the connection   
  
#### VpcDetails field format

Field | Type | Description  
---|---|---  
**projectId** | string  | ID of the project containing the VPC network   
**vpc** | string  | VPC network on which the VM is operating   
**subnetwork** | string  | Subnetwork on which the VM is operating   
  
#### GkeDetails field format

Field | Type | Description  
---|---|---  
**cluster** | ClusterDetail | GKE cluster metadata   
**pod** | PodDetails | GKE Pod metadata, populated when the source or destination of the traffic is a Pod   
**service** | ServiceDetails | GKE Service metadata, populated in service endpoints only. The record contains up to two services. If there are more than two relevant services, this field contains a single service with a special **MANY_SERVICES** marker.   
  
#### ClusterDetails field format

Field | Type | Description  
---|---|---  
**cluster** | string  | GKE cluster name   
**clusterLocation** | string  | Location of the cluster. The cluster location can be a zone or a region.   
  
#### PodDetails field format

Field | Type | Description  
---|---|---  
**pod** | string  | Name of the Pod   
**podNamespace** | string  | Namespace of the Pod   
  
#### ServiceDetails field format

Field | Type | Description  
---|---|---  
**service** | string  | Name of the service. If there are more than two relevant services, the field is set to a special **MANY_SERVICES** marker.   
**serviceNamespace** | string  | Namespace of the service   
  
## Monitoring

An internal passthrough Network Load Balancer exports monitoring data to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).

Monitoring metrics can be used for the following purposes:

  * Evaluate an internal passthrough Network Load Balancer's configuration, usage, and performance
  * Troubleshoot problems
  * Improve resource utilization and user experience



In addition to the predefined dashboards in Monitoring, you can create custom dashboards, set up alerts, and query the metrics through the [Monitoring API](https://docs.cloud.google.com/monitoring/api).

### View Monitoring dashboards

###  Console 

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. If **Resources** appears in the navigation pane, select **Resources** , and then select **Google Cloud Load Balancers**. Otherwise, select **Dashboards** , and then select the dashboard named **Google Cloud Load Balancers**.

  3. Click the name of your load balancer.




In the left pane, you can see various details for the selected load balancer. In the right pane, you can see time series graphs. Click the **Breakdowns** link to see specific breakdowns. The left pane presents currently configured data, while the right pane can present data served by historical configurations not currently reflected in the left pane.

**Note:** Monitoring collects internal passthrough Network Load Balancer data every 15 minutes. However, it might take up to two hours after you create your first internal passthrough Network Load Balancer for data to be available in Cloud Logging and Monitoring.

### Define Monitoring custom dashboards

You can create custom Monitoring dashboards for internal passthrough Network Load Balancer metrics.

###  Console 

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Dashboards > Create Dashboard**.

  3. Click **Add Chart**.

  4. Give the chart a title.

  5. Select metrics and filters. For metrics, the resource type is **Internal Passthrough TCP Network Load Balancer Rule** (`internal_tcp_lb_rule`) or **Internal Passthrough UDP Network Load Balancer Rule** (`internal_udp_lb_rule`).

  6. Click **Save**.




### Define alerting policies

###  Console 

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `Google Cloud TCP Load Balancer or Google Cloud UDP Load Balancer` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select **Google Cloud TCP Load Balancer** or **Google Cloud UDP Load Balancer**.
     3. Select a **Metric category** and a **Metric** , and then select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Select a condition type and, if necessary, specify a threshold. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). 
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

### Metrics for internal passthrough Network Load Balancers

The following metrics for internal passthrough Network Load Balancers are reported into Monitoring.

Metric | metric_name | Description  
---|---|---  
Inbound Throughput | `loadbalancing.googleapis.com/l3/internal/ingress_bytes_count` | The number of bytes sent from the client to the internal passthrough Network Load Balancer backend. For TCP flows, only bytes in the application stream are counted.  
Inbound Packets | `loadbalancing.googleapis.com/l3/internal/ingress_packets_count` | The number of packets sent from the client to the internal passthrough Network Load Balancer backend.  
Outbound Throughput | `loadbalancing.googleapis.com/l3/internal/egress_bytes_count` | The number of bytes sent from the internal passthrough Network Load Balancer backend to the client. For TCP flows, only bytes in the application stream are counted.  
Outbound Packets | `loadbalancing.googleapis.com/l3/internal/egress_packets_count` | The number of packets sent from the internal passthrough Network Load Balancer backend to the client.  
Latency | `loadbalancing.googleapis.com/l3/internal/rtt_latencies` | A distribution of RTT measured over TCP connections for internal passthrough Network Load Balancer flows. Available only for TCP traffic.  
  
### Filter dimensions for internal passthrough Network Load Balancer metrics

Metrics are aggregated for each internal passthrough Network Load Balancer. Metrics can be further broken down by the following dimensions:

Property | Description  
---|---  
BACKEND NAME | The name of the instance group or network endpoint group (NEG) with `GCE_VM_IP` endpoints.  
BACKEND SCOPE | The scope ([region or zone](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones)) of the backend that received the connection.  
BACKEND ZONE | For zonal instance groups and network endpoint groups, [zone](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones) of the backend that served the connection.  
CLIENT NETWORK | The network of the client instance that connected to the internal passthrough Network Load Balancer.   
CLIENT SUBNETWORK | The subnetwork of the client instance that connected to the internal passthrough Network Load Balancer.  
CLIENT ZONE | The Google Cloud [zone](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones) of the instance that connected to the forwarding rule.  
FORWARDING RULE | The name of the internal passthrough Network Load Balancer's forwarding rule.  
  
### Metric reporting frequency and retention

Metrics for the internal passthrough Network Load Balancers are exported to Monitoring in one-minute granularity batches. Monitoring data is retained for six weeks. Metrics are based on sampled traffic (sampling rate is dynamic and cannot be adjusted). The dashboard provides data analysis in default intervals of one hour (1H), six hours (6H), one day (1D), one week (1W), and six weeks (6W). You can manually request analysis in any interval from six weeks to one minute.

## What's next

  * For information about fundamentals, see [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal).
  * For information about failover, see [Failover for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview).
  * For available DNS name options for your load balancer, see [Internal load balancing and DNS names](https://docs.cloud.google.com/load-balancing/docs/dns-names).
  * For an example internal passthrough Network Load Balancer configuration, see [Set up an internal passthrough Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal).
  * For information about how to configure and test an internal passthrough Network Load Balancer that uses failover configuration, see [Configure failover for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-failover).
  * For information about accessing internal load balancers from peer networks connected to your VPC network, see [Internal passthrough Network Load Balancers and connected networks](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks).
  * For information about how to troubleshoot, see [Troubleshoot internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/troubleshooting-ilb).
  * For information about how to troubleshoot issues with logs, see [Troubleshoot logging issues](https://docs.cloud.google.com/load-balancing/docs/internal/troubleshooting-ilb#troubleshoot-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
