---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables/
title: Configuration analysis states \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:21.267809+00:00
---

# Configuration analysis states  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)



Send feedback 

#  Configuration analysis states Stay organized with collections  Save and categorize content based on your preferences. 

A Connectivity Test configuration analysis goes through a series of test states as it checks the configuration of each Google Cloud resource in a network path from a designated source to a designated destination. Use this reference to interpret these states.

For more information about Connectivity Tests, including details about live data plane analysis, see the [overview](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview).

## Test states

A Connectivity Test configuration analysis provides data for the following test states in the order listed:

  * Initial state
  * Configuration checking state
  * Forwarding state
  * Transition state
  * Special state
  * Final state
  * Overall reachability result



Some of these states appear in every trace, while others only appear when testing the configuration of a specific Google Cloud resource or when performing a certain task.

The final state and the overall reachability result provide the most important test output.

In addition, test output can include metadata for Google Cloud resources that are associated with one or more of the states; for example, information about a virtual machine (VM) instance's name and IP address.

## How the configuration analysis evaluates reachability

The configuration analysis simulates a test packet through a network path by verifying configurations for Google Cloud resources in that path. Some examples of invalid network configurations are a Cloud Load Balancing forwarding rule that has no backends or a network route that doesn't exist.

During the configuration checking state, Connectivity Tests collects information about network routes such as user-configured routes, dynamic routes based on BGP advertisements, or policy-based routes. The configuration analysis then chooses a network route based on [applicability and order](https://docs.cloud.google.com/vpc/docs/routes#instancerouting).

For the configuration checking state, `verified` means that Connectivity Tests confirms that a configuration for the Google Cloud resource tested is valid. The configuration allows the simulated test packet to continue through the network path being tested.

For ingress and egress firewall rules, `verified` means that the configuration analysis confirms that the firewall rule is valid. The firewall rule permits the simulated test packet to pass.

If Connectivity Tests determines that a configuration is invalid, the packet has a final state of `Drop`.

## Overall reachability result

**Note:** Knowing the overall reachability result can be helpful for setting up monitoring or automation.

The configuration analysis provides an overall summary of reachability status, also known as a result. Results can have one of four values: `Reachable`, `Unreachable`, `Ambiguous`, and `Undetermined`.

### Values table

The following table describes the value for each type of overall reachability result.

Overall reachability result | Description  
---|---  
`Reachable` | There are two possible scenarios. In both scenarios, Connectivity Tests does not find any configuration issues. Thus, both scenarios are considered `Reachable`.

  * In the first scenario, the packet originating from the source is expected to reach its destination. The final state of one or more traces is `Deliver`.
  * In the second scenario, the analysis is partially complete based on configurations where the user has permission. The final state of one or more traces is `Forward`.

  
`Unreachable` | The packet originating from the source is expected to be dropped before reaching its destination. The final state of all the traces is `Drop`.  
`Ambiguous` |  This result is returned if the source and destination endpoints do not uniquely identify the test location in the network, and the overall reachability result contains multiple traces with mixed `Reachable` and `Unreachable` states. In this case, the final states among multiple traces return different final states. The `Ambiguous` result doesn't apply to tests that contain only one trace.  
`Undetermined` |  Reachability could not be determined. The final state for one trace is `Forward` or `Abort`. For multiple traces, the final state is a combination of either `Forward` or `Abort`. The reachability from the source to the destination cannot be determined for one of the following reasons:

  * The analysis is aborted due to a permission error. The user does not have read permission to the projects listed in the test.
  * The analysis is aborted due to internal errors.

  
  
### Multiple traces

Each configuration analysis can contain multiple traces, and the final state of these traces might not be the same. For example, a packet to the VIP for a Google Cloud load balancer might have `n` traces if there are `n` backend VM instances configured for the load balancer. These `n` traces might not have the same final states.

Because an analysis can produce multiple possible traces, the following is true:

  * If there is only one trace result, the overall reachability result is the same as the final state of the trace.
  * If there are multiple trace results, the overall reachability result is calculated based on the distribution of the final states contained in all of the traces.



### Result metadata

In addition to the overall reachability result for traces, every test result contains the following metadata:

  * The time the test state for the test was verified
  * Error details of a test failure or cancellation
  * Trace details for each trace



Error details of a test failure or cancellation are shown as codes and messages displayed in the overall reachability result. For example, a test with a final state of `Abort` might show an error message such as `Failed to pull initial config. An internal error occurred.`

## Initial state

During the initial state, the configuration analysis simulates starting from a network [endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints).

Message | Description  
---|---  
`START_FROM_INSTANCE` | The packet originated from a Compute Engine instance. `InstanceInfo` metadata was populated by Connectivity Tests.  
`START_FROM_INTERNET` | The packet originated from the internet. `EndpointInfo` metadata was populated by Connectivity Tests.  
`START_FROM_PRIVATE_NETWORK` | The packet originated from a VPC network or an on-premises network with an internal source IP address. If the source was a VPC network visible to the user, the `NetworkInfo` metadata was populated with network details by Connectivity Tests.  
`START_FROM_CLOUD_FUNCTION` | The packet originated from a Cloud Run function. `CloudFunctionInfo` metadata was populated by Connectivity Tests.  
`START_FROM_CLOUD_RUN_REVISION` | The packet originated from a revision of a Cloud Run service. `CloudRunRevisionInfo` metadata was populated by Connectivity Tests.  
`START_FROM_APP_ENGINE_VERSION` | The packet originated from a version of an App Engine standard environment service. `AppEngineVersionInfo` metadata was populated by Connectivity Tests.  
  
## Final state

There are four final states: `Drop`, `Abort`, `Forward`, and `Deliver`. Each of the following sections has a table that contains messages and descriptions for each state.

### Drop

Connectivity Tests dropped the simulated test packet because the test target was unreachable for the following reasons.

Message | Description  
---|---  
`UNKNOWN_EXTERNAL_ADDRESS` | The destination external address can't be resolved to a known target.  
`FOREIGN_IP_DISALLOWED` | The VM instance can only send or receive a packet with a foreign IP address if `ip_forward` is enabled. In other words, the foreign IP address failed a [spoof check](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#spoof-checking).  
`[FIREWALL_RULE](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/states/reasons-dropped-packets#firewall-rule)` |  Dropped due to a firewall rule unless allowed due to [connection tracking](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/sect-security_guide-firewalls-iptables_and_connection_tracking). Connectivity Tests might deny a test packet because the packet matches a blocking firewall rule. However, the actual data plane might allow the packet through due to connection tracking on the firewall rule. Connection tracking allows packets for an existing connection to return in spite of the firewall rule.  
`[NO_ROUTE](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/states/reasons-dropped-packets#no-route)` | Dropped due to no routes.  
`ROUTE_BLACKHOLE` | Dropped because the next hop of the matched route doesn't exist.  
`ROUTE_WRONG_NETWORK` | The packet was sent to the wrong (unintended) network, as shown in [Detect invalid or inconsistent configurations](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/detecting-configs).   
`[PRIVATE_TRAFFIC_TO_INTERNET](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/states/reasons-dropped-packets#private-traffic-to-internet)` | A packet with an internal destination address was sent to an internet gateway.  
`PRIVATE_GOOGLE_ACCESS_DISALLOWED` | A VM instance with only an internal IP address tried to access a Google API or Google service, but Private Google Access was not enabled.  
`[NO_EXTERNAL_ADDRESS](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/states/reasons-dropped-packets#no-external-address)` | A VM instance with only an internal IP address tried to access external hosts through a route whose next hop is the default internet gateway. Expected when Cloud NAT is not enabled in the subnet or when there's no other default route that uses a different type of next hop (such as a proxy VM).  
`UNKNOWN_INTERNAL_ADDRESS` | A destination internal address could not be resolved to a known target.  
`[FORWARDING_RULE_MISMATCH](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/states/reasons-dropped-packets#forwarding-rule-mismatch)` | A forwarding rule's protocol and ports did not match the packet header, or the packet does not originate from or is not directed to the same region as the regional load balancer.   
`[FORWARDING_RULE_NO_INSTANCES](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/states/reasons-dropped-packets#forwarding-rule-no-instances)` | A forwarding rule did not have backends configured.  
`FIREWALL_BLOCKING_LOAD_BALANCER_BACKEND_HEALTH_CHECK` |  A firewall rule blocked the health check probes to the backends and caused the backends to be unavailable for traffic from the load balancer. As part of its testing sequence for Cloud Load Balancing, the configuration analysis verifies that existing firewall rules have been configured to allow a health check probing packet to be sent to the Cloud Load Balancing backends. This configuration check results in a `healthCheckFirewallState`. For details, see [Health check firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-checks#firewall_rules).  
`INSTANCE_NOT_RUNNING` | A packet was sent from or to a VM instance that was not in a running state.  
`[TRAFFIC_TYPE_BLOCKED](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/states/reasons-dropped-packets#traffic-type-blocked)` | The type of traffic was blocked and the user could not configure a firewall rule to enable it. For details, see [Always blocked traffic](https://docs.cloud.google.com/vpc/docs/firewalls#blockedtraffic).   
`GKE_MASTER_UNAUTHORIZED_ACCESS` | Access to the Google Kubernetes Engine [control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#control_plane) endpoint was not authorized. For details, see [Access to the cluster endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#endpoints).  
`DROPPED_INSIDE_GKE_SERVICE` | A packet was dropped inside the Google Kubernetes Engine service.  
`CLOUD_SQL_INSTANCE_UNAUTHORIZED_ACCESS` | Access to the Cloud SQL instance endpoint is not authorized. For details, see [Authorizing with authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks).  
`DROPPED_INSIDE_CLOUD_SQL_SERVICE` | A packet was dropped inside the Cloud SQL service.  
`GOOGLE_MANAGED_SERVICE_NO_PEERING` | A packet was dropped because there is no peering between the originating network and the Google-managed services network.  
`CLOUD_SQL_INSTANCE_NO_IP_ADDRESS` | A packet was dropped because the Cloud SQL instance has neither a private nor a public IP address.  
`PSC_CONNECTION_NOT_ACCEPTED` | A packet was dropped because the connection to the published service that uses Private Service Connect is not accepted.  
`CLOUD_FUNCTION_NOT_ACTIVE` | A packet was dropped because the Cloud Run function is not active.  
`VPC_CONNECTOR_NOT_SET` | A packet was dropped because the App Engine standard environment service, the Cloud Run function, or the Cloud Run revision doesn't have a [Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) configured.   
`VPC_CONNECTOR_NOT_RUNNING` | A packet was dropped because the [Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) is not running.  
`CLOUD_RUN_REVISION_NOT_READY` | A packet was dropped because the Cloud Run revision is not ready and cannot serve traffic.  
  
### Abort

The configuration analysis was stopped because of lack of basic information, such as lack of access to the network configuration.

This state usually happens when Connectivity Tests does not have the correct permissions to obtain the configuration from the host project for a service project, as shown in the following table.

Message | Description | `UNKNOWN_NETWORK` | Aborted due to an unknown network. The analysis cannot proceed because, in a Shared VPC network, the user running the test does not have access to the host project's network configurations, including firewall rules and routes. Running a Connectivity Test requires that the user running the test can read configurations for resources such as routes in the host project. This happens because network resources are allocated in the host project, but the actual resources exist in the service project.  
---|---  
`UNKNOWN_IP` |  The analysis aborted because the IP addresses required for analysis were unknown. This is due to incorrect user input, or the configuration analysis could not determine a valid endpoint based on the provided input parameters. In a Shared VPC network, the user running the test did not have access to the host project's network configurations. This access is required for testing against IP addresses in the service project.  
`UNKNOWN_PROJECT` | The analysis aborted because no project information could be derived from the input to the Connectivity Test. This is due to incorrect user input or, based on the provided input parameters, the analysis could not determine a valid project.  
`PERMISSION_DENIED` | The analysis was aborted because the user lacked the permission to access all or part of the network configurations required to run the test.  
`NO_SOURCE_LOCATION` | The analysis aborted because no valid source endpoint could be derived from the test input. This is due to incorrect user input or, based on the provided input parameters, the analysis could not determine a valid source endpoint.  
`INVALID_ARGUMENT` | The analysis aborted because the source and/or destination endpoint specified in the test input were invalid. The possible reasons for this message include the following:

  * A malformed IP address
  * A non-existent VM instance or network URI
  * An IP address that is not in the range of the specified network URI
  * A VM instance that doesn't own the network interface in the specified network

  
`NO_EXTERNAL_IP` | The analysis aborted because traffic was sent from a public IP address to a VM instance that did not have an external IP address.  
`UNINTENDED_DESTINATION` | The analysis aborted because none of the traces were able to match the destination information specified in the test input.  
`TRACE_TOO_LONG` | The analysis aborted because the number of steps in the trace exceeded a certain limit. This issue might be caused by a routing loop.  
`INTERNAL_ERROR` | Aborted due to internal server error.  
`SOURCE_ENDPOINT_NOT_FOUND` | Aborted because the source endpoint could not be found.  
`MISMATCHED_SOURCE_NETWORK` | Aborted because the source network does not match the source endpoint.  
`DESTINATION_ENDPOINT_NOT_FOUND` | Aborted because the destination endpoint could not be found.  
`MISMATCHED_DESTINATION_NETWORK` | Aborted because the destination network does not match the destination endpoint.  
  
### Forward

The analysis stopped at a specific endpoint and could go no further:

  * The analysis is partially complete based on configurations where the user has permission.
  * The test packet was forwarded to a network with an unknown configuration.
  * The test target has not been dropped according to the known configuration, and the test packet has been forwarded to a network where Connectivity Tests has no visibility.

Message | Forwarded | `PEERING_VPC` | To a peer VPC network  
---|---  
`VPN_GATEWAY` | To a Cloud VPN gateway  
`INTERCONNECT` | To a Cloud Interconnect connection  
`GKE_MASTER` | To a GKE control plane  
`IMPORTED_CUSTOM_ROUTE_NEXT_HOP` | To the next hop of a custom route imported from a peered VPC network  
`CLOUD_SQL_INSTANCE` | To a Cloud SQL instance  
  
### Deliver

The analysis was able to reach the target and deliver the simulated test packet.

A final state of `Deliver` does not guarantee that traffic can pass through the data plane. The purpose of the analysis is to validate configuration issues that might cause traffic to drop.

Message | Target | `INSTANCE` | A Compute Engine VM instance  
---|---  
`INTERNET` | The internet  
`GOOGLE_API` | A Google API  
`GKE_MASTER` | A GKE control plane  
`CLOUD_SQL_INSTANCE` | A Cloud SQL instance  
`PSC_GOOGLE_API` | All Google APIs and services that use Private Service Connect  
`PSC_VPC_SC` | VPC Service Controls that use Private Service Connect  
`PSC_PUBLISHED_SERVICE` | A published service that uses Private Service Connect  
  
### Metadata

The configuration analysis shows the following metadata for the final state.

Metadata name | Description  
---|---  
`AbortInfo` | Cause of an `Abort` final state and the resource URI that caused that state.  
`DropInfo` | Cause of a `Drop` final state and the resource URI that caused that state.  
`ForwardInfo` | The target type and target resource URI that a test packet was finally forwarded to (`Forward` final state).  
  
## Other states

Before the test packet reaches one of the final states, it goes through the following intermediate states: configuration checking state, forwarding state, transition state, and special state.

### Configuration checking state

During the configuration checking state, Connectivity Tests checks the configuration of Google Cloud resources in the simulated network path, verifies that the resource configuration is valid, and verifies that the configuration allows the simulated test packet to continue on through the network path.

If needed, the configuration analysis performs a spoof check.

Message | Description | `APPLY_INGRESS_FIREWALL_RULE` | Verified ingress firewall rule.  
---|---  
`APPLY_EGRESS_FIREWALL_RULE` | Verified egress firewall rule.  
`APPLY_ROUTE` | Verified route.  
`APPLY_FORWARDING_RULE` | Matched forwarding rule.  
`SPOOFING_APPROVED` | The packet was sent or received under a foreign IP address, but allowed. For details, see [spoof checking](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#spoof-checking).  
  
### Forwarding state

During the forwarding state, Connectivity Tests simulates a packet arriving at an intermediate Google Cloud resource in the testing path (for example, a packet arriving at a Cloud VPN gateway or a Google Cloud load balancer).

Message | Description | `ARRIVE_AT_INSTANCE` | Arrived at a Compute Engine VM instance.  
---|---  
`ARRIVE_AT_INTERNAL_LOAD_BALANCER` | Arrived at a Google Cloud load balancer that uses a private IP address as a VIP.  
`ARRIVE_AT_EXTERNAL_LOAD_BALANCER` | Arrived at the public IP address of a Google Cloud load balancer.  
`ARRIVE_AT_VPN_GATEWAY` | Arrived at a Cloud VPN gateway.  
`ARRIVE_AT_VPN_TUNNEL` | Arrived at a Cloud VPN tunnel.  
`ARRIVE_AT_VPC_CONNECTOR` | Arrived at a [ Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access).  
  
### Transition state

During the transition state, Connectivity Tests verifies simulated configurations where a packet is changed (for example, where Cloud NAT translates a packet header, or when a Google Cloud load balancing proxy terminates and reinitiates an inbound TCP session to VM instances).

Message | Description | `NAT` | The packet header was translated.  
---|---  
`PROXY_CONNECTION` | The original connection was terminated, and a new proxied connection was initiated.  
  
### Special state

In this state, a test viewer does not have permission to view one or more Google Cloud resources. For more information, see [Test permissions](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#test-perms).

Metadata name | Description  
---|---  
`VIEWER_PERMISSION_MISSING` | The viewer of the test result does not have permission to see the configuration for the Google Cloud resource in this step.  
  
## Resource metadata

Connectivity Tests shows the following metadata for the Google Cloud resource configurations that it checks.

Metadata name | Description  
---|---  
`EndpointInfo` | Endpoints used for the test. Connectivity Tests obtains `EndpointInfo` from source and destination endpoints and validates the information by using the model for the data plane.  
`FirewallInfo` | Metadata associated with a firewall rule.  
`ForwardingRuleInfo` | Metadata associated with a VPC forwarding rule.  
`InstanceInfo` | Metadata associated with a Compute Engine VM instance.  
`LoadBalancerInfo` | Metadata associated with a Google Cloud load balancer.  
`NetworkInfo` | Metadata associated with a VPC network.  
`RouteInfo` | Metadata associated with a VPC network route.  
`AppEngineVersionInfo` | Metadata associated with a version of an App Engine standard environment service.  
`CloudRunRevisionInfo` | Metadata associated with a Cloud Run revision.  
`CloudFunctionInfo` | Metadata associated with a Cloud Run function.  
`VpcConnectorInfo` | Metadata associated with a Serverless VPC Access connector.  
  
## What's next

  * [Learn about Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview)
  * [Troubleshoot Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
