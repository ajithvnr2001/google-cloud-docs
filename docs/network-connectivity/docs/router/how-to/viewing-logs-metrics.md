---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics/
title: View logs and metrics \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:22.111600+00:00
---

# View logs and metrics  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View logs and metrics

Cloud Router sends logging information to Cloud Logging and sends monitoring metrics to Cloud Monitoring. This page shows you how to access both types of information.

## Logs

Cloud Router sends logging information to [Cloud Logging](https://docs.cloud.google.com/logging/docs), which logs the following events:

  * Router events related to your Cloud Router
  * BGP events related to a BGP configuration and session
  * Route events related to route announcements between the two BGP peers
  * Route quota events related to Cloud Router unique prefix quotas



### View logs

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/networking/routers/list)

  2. Select a Cloud Router from the list of Cloud Routers.

  3. In the **Logs** column, click **View**.

Cloud Router logs have the following formats:

     * **Router, BGP, and route announcement events** : Logs (`compute.googleapis.com/router_events`) associated with the `gce_router` monitored resource:
           
           [Event Type]: [Log Text]
           

     * **Route quota events** : JSON logs (`router.googleapis.com/route_quota_events`) associated with the `gce_network_region` monitored resource. For details about the payload structure, see Route quota events log.

**Note:** Some log entries refer to a Cloud Router's _BGP router ID_. This ID is assigned to the Cloud Router based on the IP address of one of its interfaces.
  4. To build queries in the Logs Explorer, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).




### Info log

The following table lists events that are logged in the Logging Info log.

Event | Description  
---|---  
Router event | Router task activated  
Router task de-activated  
BGP event | Successfully added configuration for peers: `LIST_OF_PEERS`  
BGP peering with `PEER` came up _x_ seconds ago  
BGP peering with `PEER` went down with the reason `MESSAGE`, where `MESSAGE` provides an explanation such as `HOLD_TIMER_EXPIRED` or `LINK_DOWN`.   
For more information about `LINK_DOWN`, see [`LINK_DOWN` message appears in Cloud Router logs](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-log-messages#link-down-in-logs).  
BGP Router ID set to `BGP_ROUTER_ID`  
Route event | Advertising prefix to peers: `PREFIX`  
Withdrawing prefix from peers: `PREFIX`  
Prefix `PREFIX` Nexthops `LIST_OF_NEXTHOPS` received by Cloud Router  
Prefix `PREFIX` Nexthops `LIST_OF_NEXTHOPS` deleted from Cloud Router  
  
### Common Logging events

To view common Logging events for Cloud Router as listed in the following table, use the steps for viewing logs. Specify one of the advanced filters listed in the table. Adjust the timeframe for the Logging search as needed.

**Note:** The `Adding learned routes` and `Removing learned routes` events refer to routes that are received through BGP. They are unrelated to [custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).Event description | Logging advanced filter  
---|---  
Migrating or restarting a Cloud Router process | resource.type="gce_router"  
"task activated"  
Adding learned routes | resource.type="gce_router"  
"received by cloud router"  
Removing learned routes | resource.type="gce_router"  
"deleted from cloud router"  
Exporting advertised routes | resource.type="gce_router"  
("Route Event" AND "Advertising prefix")  
BGP peering came up  | resource.type="gce_router"  
("BGP peering" AND "came up")  
BGP peering came up with MD5 authentication | resource.type="gce_router"  
("BGP peering" AND "came up" AND "MD5 authentication enabled")  
BGP peering went down | resource.type="gce_router"  
("BGP peering" AND "went down")  
BGP peering went down because the link went down on the Google peering edge router | resource.type="gce_router"  
("BGP peering" AND "went down" AND "LINK_DOWN")  
A BGP session was shut down due to excessive received routes | resource.type="gce_router"  
("NOTIFICATION 6/1")   
severity="CRITICAL"  
A Cloud Router dynamic route prefix quota has been exceeded | resource.type="gce_network_region"  
("No more routes" AND "can be programmed")   
severity="ERROR"  
A route was dropped because of a quota issue | resource.type="gce_network_region"  
severity="ERROR"   
jsonPayload.affectedResource.routes.nextHopIpAddresses="`PEER_IP_ADDRESS`"   
A BFD session waiting for peer | resource.type="gce_router"  
("BFD Event" AND "bfd enabled, state [Init, NoDiagnostic]")   
A BFD session came up | resource.type="gce_router"  
("BFD Event" AND "to [Up, NoDiagnostic]")   
A BFD session went down (Rx Timer expired) | resource.type="gce_router"  
("BFD Event" AND "to [Down, ControlDetectionTimeExpired]")   
A BFD session went down (Peer's state is `Down` or `AdminDown`) | resource.type="gce_router"  
("BFD Event" AND "to [Down, NeighborSessionDown]")   
A BFD session is disabled locally | resource.type="gce_router"  
("BFD Event" AND "bfd disabled")   
  
### Route quota events log

Cloud Router writes route quota events to Cloud Logging under `router.googleapis.com/route_quota_events` through the `gce_network_region` monitored resource. These logs help you monitor route prefix usage against your [quotas](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#quotas) and identify any dropped routes.

Route quota events are logged at the following severity levels:

  * **`WARNING`** : Route usage approaches the quota limit (usage reaches or exceeds 75% of the regional or global limit).
  * **`ERROR`** : Route usage reaches or exceeds 100% of the limit. Excess routes can't be programmed and are dropped. If routes are dropped due to quota exhaustion, the log entry includes details about the dropped routes in the `jsonPayload.affectedResource.routes` field.



#### Route quota event fields

Route quota log entries contain a structured JSON payload (`jsonPayload`) with the following fields:

Field | Description  
---|---  
`eventTime` | The timestamp when the quota event occurred.  
`routeQuotaEvent.helperMessage` | A message describing the quota state—for example, warning when the usage of a Cloud Router unique prefix quota is approaching or has exceeded its limit.  
`routeQuotaEvent.regionalRouteCount` | The usage of the _unique Cloud Router dynamic route prefixes from own region per region per VPC network_ quota. The usage represents the number of unique route prefixes, processed by the dynamic route control plane in a given region of a VPC network, received from all Cloud Router BGP sessions in that same region and network.  
`routeQuotaEvent.regionalRouteLimit` | The limit of the _unique Cloud Router dynamic route prefixes from own region per region per VPC network_ quota. The limit represents the maximum number of unique route prefixes that can be processed by the dynamic route control plane in a given region of a VPC network, received from all Cloud Router BGP sessions in that same region and network.  
`routeQuotaEvent.globalRouteCount` | The usage of the _unique Cloud Router dynamic route prefixes from other regions per region per VPC network_ quota. The usage represents the number of unique route prefixes, processed by the dynamic route control plane in a given region of a VPC network, received from all Cloud Router BGP sessions in other regions of the same network.  
`routeQuotaEvent.globalRouteLimit` | The limit of the _unique Cloud Router dynamic route prefixes from other regions per region per VPC network_ quota. The limit represents the maximum number of unique route prefixes that can be processed by the dynamic route control plane in a given region of a VPC network, received from all Cloud Router BGP sessions in other regions of the same network.  
`affectedResource.routes[]` | An entry containing attributes for dropped prefixes that didn't result in the creation of dynamic routes when a Cloud Router unique prefix quota's usage exceeds its limit (present in `ERROR` severity events). Each entry includes these attributes: 

  * `ipPrefix`: The prefix (destination) in CIDR format.
  * `nextHopIpAddresses`: The BGP IP addresses of the Cloud Router BGP sessions that learned the prefix.
  * `medValue`: The MED attribute.
  * `srcRouterIds`: The IDs of the Cloud Router(s) that manage the BGP session(s).

  
  
## Metrics

Cloud Router publishes metrics to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). For a list of metrics published for Cloud Router, see Monitor metrics for Cloud Router.

All Cloud Router metrics cover both IPv4 and IPv6 traffic.

### View metrics by using the API

You can access these metrics by using the Cloud Monitoring API. For more information, see [Read metric data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics).

### View metrics by using Monitoring dashboards

You can also create a custom dashboard in Cloud Monitoring to help you analyze these metrics. For more information, see [Manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

To create a custom dashboard, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Dashboards** , and then on the **Dashboards Overview** page, click add**Create dashboard**.

  3. Optional: Update the dashboard title with a descriptive name for your dashboard.

  4. In the **Chart library** , select the chart that you want to add. For example, to add a **Line** chart to the dashboard, click or drag that entry from the **Chart library** to the graph area.

  5. In **Chart Title** , change the chart title or use the suggested title.

  6. In **What data do you want to view?** , do the following:

     1. In **Resource type** , click the **Type to filter** field, and enter `Cloud Router`.
     2. In **Metric** , add a Cloud Router metric.
  7. Use the **Filter** controls to restrict the view to only certain routers or sessions.

  8. To add another metric, click **Add another metric**.




Some metrics are for the Cloud Router and some metrics are for a BGP session on a given Cloud Router. Cloud Router metrics are shown as `router-name`, while BGP session metrics are shown as `router-name(bgp-name)`.

### Monitoring metrics for Cloud Router

**Note:** Metrics that describe _received routes_ or _learned routes_ reflect data about dynamically learned routes. They are unrelated to the [Custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes) feature.

The "metric type" strings in this table must be prefixed with `router.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`best_received_routes_count` GA ** _(project)_**   
Received routes count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Current number of best routes received by router. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`bfd/control/receive_intervals` GA ** _(project)_**   
BFD control packets receive intervals   
`GAUGE`, `INT64`, `ms`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _BFD control packets receive intervals. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bfd/control/received_packets_count` GA ** _(project)_**   
Control packets received   
`DELTA`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of control packets received from this BFD session. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bfd/control/rejected_packets_count` GA ** _(project)_**   
Control packets rejected   
`DELTA`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of control packets rejected, from this BFD session. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bfd/control/transmit_intervals` GA ** _(project)_**   
BFD control packets transmit intervals   
`GAUGE`, `INT64`, `ms`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _BFD control packets transmit intervals. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bfd/control/transmitted_packets_count` GA ** _(project)_**   
Control packets transmitted   
`DELTA`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of control packets transmitted from this BFD session. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bfd/session_flap_events_count` GA ** _(project)_**   
BFD session flap   
`DELTA`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of each BFD flap event from this BFD session. A session flap event refers to the transition from Up state. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`event_type`: The reason for the BFD flap such as "AdminDown" or "ControlDetectionTimeExpired".   
`bfd/session_up` GA ** _(project)_**   
BFD session status   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Indicator for successful BFD session establishment. 1 indicates the session is up. 0 indicates the session is down. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bgp/received_routes_count` GA ** _(project)_**   
BGP received routes count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Current number of routes received on a bgp session. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`bgp_peer_name`: The name of the bgp session.   
`bgp/sent_routes_count` GA ** _(project)_**   
BGP sent routes count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Current number of routes sent on a bgp session. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`bgp_peer_name`: The name of the bgp session.   
`bgp/session_up` GA ** _(project)_**   
BGP session status   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Indicator for successful bgp session establishment. 1 indicates the session is up. 0 indicates the session is down. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`bgp_peer_name`: The name of the bgp session.   
`bgp_sessions_down_count` GA ** _(project)_**   
BGP sessions down count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of BGP sessions on the router that are down. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`bgp_sessions_up_count` GA ** _(project)_**   
BGP sessions up count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of BGP sessions on the router that are up. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`dynamic_routes/learned_routes/any_dropped_unique_destinations` BETA ** _(project)_**   
Any unique destinations dropped   
`GAUGE`, `BOOL`, `1`   
**[gce_network_region](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_network_region)** |  _A boolean metric of whether there are any unique destinations dropped in a network region due to exceeding quota. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`routing_mode`: Routing mode of the route, one of ["global" - learned from remote regions; "regional" - learned from local regions].   
`dynamic_routes/learned_routes/dropped_unique_destinations` BETA ** _(project)_**   
Unique destinations dropped   
`GAUGE`, `INT64`, `1`   
**[gce_network_region](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_network_region)** |  _The number of unique destinations dropped in a network region due to exceeding quota. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`routing_mode`: Routing mode of the route, one of ["global" - learned from remote regions; "regional" - learned from local regions].   
`dynamic_routes/learned_routes/unique_destinations_limit` BETA ** _(project)_**   
Unique destinations limit   
`GAUGE`, `INT64`, `1`   
**[gce_network_region](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_network_region)** |  _The maximum number of unique destinations allowed by route quota for this network region. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`routing_mode`: Routing mode of the route, one of ["global" - learned from remote regions; "regional" - learned from local regions].   
`dynamic_routes/learned_routes/used_unique_destinations` BETA ** _(project)_**   
Unique destinations used   
`GAUGE`, `INT64`, `1`   
**[gce_network_region](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_network_region)** |  _Number of unique destinations used by learned routes for this network region. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`routing_mode`: Routing mode of the route, one of ["global" - learned from remote regions; "regional" - learned from local regions].   
`nat/allocated_ports` GA ** _(project)_**   
Allocated ports   
`GAUGE`, `INT64`, `{port}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Number of ports allocated to all VMs by the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`nat_ip`: NAT IP of the ports.   
`nat/closed_connections_count` GA ** _(project)_**   
Closed connections count   
`DELTA`, `INT64`, `{connection}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of connections closed over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/dropped_received_packets_count` GA ** _(project)_**   
Received packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of received packets dropped by the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/dropped_sent_packets_count` GA ** _(project)_**   
Sent packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of sent packets dropped by the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`reason`: The reason for the packet drop. Possible values are OUT_OF_RESOURCES, ENDPOINT_INDEPENDENCE_CONFLICT.   
`nat/nat_allocation_failed` GA ** _(project)_**   
NAT allocation failed   
`GAUGE`, `BOOL`, ``   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Indicates if there is a failure in allocating NAT IPs to any VM in the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`nat/new_connections_count` GA ** _(project)_**   
New connections count   
`DELTA`, `INT64`, `{connection}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of new connections created over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/open_connections` GA ** _(project)_**   
Open connections   
`GAUGE`, `INT64`, `{connection}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Number of connections currently open on the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/port_usage` GA ** _(project)_**   
Port usage   
`GAUGE`, `INT64`, `{port}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Maximum number of connections from VM to a single internet endpoint (IP:port). Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/received_bytes_count` GA ** _(project)_**   
Received bytes count   
`DELTA`, `INT64`, `By`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of bytes received (destination - > VMs) via the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/received_packets_count` GA ** _(project)_**   
Received packets count   
`DELTA`, `INT64`, `{packet}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of packets received (destination - > VMs) via the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/sent_bytes_count` GA ** _(project)_**   
Sent bytes count   
`DELTA`, `INT64`, `By`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of bytes sent (VMs - > destination) over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/sent_packets_count` GA ** _(project)_**   
Sent packets count   
`DELTA`, `INT64`, `{packet}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of packets sent (VMs - > destination) over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`router_up` GA ** _(project)_**   
Router tasks up   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of router software tasks that are running successfully. A value greater than or equal to 1 indicates that the router is up, although not all software tasks may be running. Compare the returned number to the expected number of software tasks for the router. A value of 0 indicates that the router is down. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`sent_routes_count` GA ** _(project)_**   
Sent routes count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Current number of routes sent by router. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
  
Table generated at 2026-10-08 15:22:12 UTC.

## What's next

  * To troubleshoot issues when using Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
