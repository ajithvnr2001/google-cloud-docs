---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/states/reasons-dropped-packets/
title: Reasons for dropped test packets \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:40.781743+00:00
---

# Reasons for dropped test packets  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/states/reasons-dropped-packets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)



Send feedback 

#  Reasons for dropped test packets Stay organized with collections  Save and categorize content based on your preferences. 

Connectivity Tests can drop a test packet for any of the following reasons.

For a full list of possible reasons, see [Configuration analysis states](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables#drop-state).

## Foreign IP address disallowed

The packet is dropped because a Compute Engine instance can send or receive packets with a foreign IP address only when IP forwarding is enabled.

### Probable cause

The VM instance doesn't have IP forwarding enabled, but the source or destination IP address of the packet going through it doesn't match the instance's IP addresses. This might happen, for example, when the packet is delivered to the instance using a [static route with the VM instance as a next hop](https://docs.cloud.google.com/vpc/docs/static-routes#instance_next_hops).

### Recommendations

Create a Compute Engine instance with IP forwarding enabled, or set the corresponding attribute for the existing instance. For more information, see [Enable IP forwarding for instances](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward).

## Dropped due to a firewall rule

The packet can be dropped because of a firewall rule, except when the packet is allowed due to [connection tracking](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/sect-security_guide-firewalls-iptables_and_connection_tracking).

### Probable cause

Connectivity Tests might deny a test packet because the packet matches a blocking [firewall rule](https://docs.cloud.google.com/firewall/docs/firewalls) or a [firewall policy rule](https://docs.cloud.google.com/vpc/docs/firewall-policies). However, the actual data plane might allow the packet through due to connection tracking on the firewall rule. Connection tracking allows packets for an existing connection to return despite the firewall rule.

Every VPC network has [two implied firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) that allow egress traffic to everywhere and block incoming traffic from everywhere. You might also have a higher priority deny egress firewall rule.

For connectivity to succeed, you need an egress firewall rule at the source allowing access to the destination endpoint, and an ingress firewall rule at the destination to allow this connection.

VPC firewall rules are [stateful](https://docs.cloud.google.com/vpc/docs/firewalls#specifications). If the specified destination endpoint is normally the side that initiates the communication, response traffic is automatically allowed with connection tracking and there is no need for an ingress firewall rule.

### Recommendations

Delete the deny rule or create an allow rule based on the details in the Connectivity Tests results. For more information, see [Firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) and [Use VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls). If the firewall policy rule that denied traffic has a network context specified, understand the [firewall policy rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details) to determine whether the rule applies to your use case.

## Dropped due to no matching route

The packet is dropped due to no matching routes.

### Probable cause

There is no active route matching the packet attributes (like a destination IP address) in the packet network and region.

### Recommendations

Verify the [list of effective routes](https://docs.cloud.google.com/vpc/docs/using-routes#listingroutes) in the Google Cloud console. If you have just created a new route, note that [it might take some time](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting#config-changes) for Connectivity Tests to receive a configuration update and incorporate it into analysis.

If you try to access the destination endpoint by using its internal IP address, make sure that the source and destination networks are connected (for example, using the [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview), or a [hybrid connectivity solution](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#google-cloud) such as Cloud VPN).

Note that [transitive VPC peering](https://docs.cloud.google.com/vpc/docs/vpc-peering#transit-network) is not supported. Consider connecting the source and destination networks directly or by using a hybrid connectivity solution.

If you try to access the destination endpoint through the internet, make sure that you have a route for the destination IP address with the next hop internet gateway.

If the packet is going through the [hybrid connectivity network endpoint group](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts), consider [additional requirements for routes applicability](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#network_connectivity_requirements). Some routes you see in the route view table might not be available for traffic from hybrid NEGs.

For more information, see [Routes](https://docs.cloud.google.com/vpc/docs/routes) and [Use routes](https://docs.cloud.google.com/vpc/docs/using-routes).

## The packet is sent to a wrong network

The packet is sent to an unintended network. For example, you execute a test from a Compute Engine instance in the `network-1` network to the Compute Engine instance in the `network-2` network, but the packet is sent to the `network-3` network.

### Probable cause

The `network-1` network has a route with a destination range that includes the destination instance IP address with the next hop in a different network (`network-3` in the example above).

### Recommendations

Verify the [list of effective routes](https://docs.cloud.google.com/vpc/docs/using-routes#listingroutes) and the [list of routes applicable to the source instance](https://docs.cloud.google.com/vpc/docs/using-routes#applicable-routes), in the Google Cloud console. For more information about route creation and [applicability](https://docs.cloud.google.com/vpc/docs/routes#instancerouting), see [Routes](https://docs.cloud.google.com/vpc/docs/routes) and [Use routes](https://docs.cloud.google.com/vpc/docs/using-routes).

## Route next hop IP address is not resolved

The packet is sent to a destination using an invalid route with the next hop IP address not assigned to any resource.

### Probable cause

If this is a route with `next-hop-address`, the next hop address must be a primary internal IPv4 address or an IPv6 address of the Compute Engine instance in the route's VPC network. Addresses in peered networks are not supported.

If this is a route with `next-hop-ilb`, the next hop address must be an address of the internal passthrough Network Load Balancer (forwarding rules used by other load balancers, protocol forwarding, or as Private Service Connect endpoints are not supported). The IP address must be assigned to a resource in the route's VPC network, or in a network connected to it with VPC Network Peering.

### Recommendations

Verify the next hop IP address belongs to a supported resource. For more information, see [Considerations for next hop instances](https://docs.cloud.google.com/vpc/docs/static-routes#next-hop-vm-only) and [Considerations for internal passthrough Network Load Balancer next hops](https://docs.cloud.google.com/vpc/docs/static-routes#next-hop-l4ilb-only).

## Route next hop instance has a NIC in the wrong network

The packet is sent to a destination using an invalid route with the next hop Compute Engine instance not having a network interface controller (NIC) in the route's network.

### Probable cause

The Compute Engine instance used as a route next hop must have a NIC in the route's network (not a peered VPC network).

### Recommendations

Verify that the next hop Compute Engine instance has a NIC in the route's network. For more information, see [Considerations for next hop instances](https://docs.cloud.google.com/vpc/docs/static-routes#next-hop-vm-only).

## Route next hop address is not a VM primary IP address

The packet is sent to a destination using an invalid route with the next hop IP address (`next-hop-address`) not being a primary IP address of the Compute Engine instance.

### Probable cause

The route's next hop IP address (`next-hop-address`) must be a primary internal IPv4 address of the Compute Engine instance. [Alias IP address ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) are not supported.

### Recommendations

Verify that the next hop IP address is a primary internal IPv4 address of the Compute Engine instance. For more information, see [Considerations for next hop instances](https://docs.cloud.google.com/vpc/docs/static-routes#next-hop-vm-only).

## Route next hop forwarding rule type is invalid

The packet is sent to a destination using an invalid route with the next hop forwarding rule (`next-hop-ilb`) not being a forwarding rule of the internal passthrough Network Load Balancer.

### Probable cause

The route's next hop forwarding rule must be a forwarding rule of the internal passthrough Network Load Balancer. For more information, see [Considerations for internal passthrough Network Load Balancer next hops](https://docs.cloud.google.com/vpc/docs/static-routes#next-hop-l4ilb-only).

### Recommendations

Create a route targeting a supported forwarding rule instead of the invalid route.

## Private traffic to internet

A packet with an internal destination address was sent to an internet gateway.

### Probable cause

The packet destination IP address is a [private IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses), which cannot be reached through the internet. However, the packet leaves the source Compute Engine instance, and matches a route with the next hop internet gateway.

### Recommendations

If you'd like to access the destination through the internet, make sure that the source Compute Engine instance has internet connectivity—for example, it has an external IP address or uses [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview)— and use the destination endpoint's external IP address in the test.

If you'd like to access the destination through its internal IP address, you need to establish connectivity (create routes) between the source and destination networks. You can do this in any of the following ways:

  1. If your destination endpoint is within an on-premises network, use a [NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) solution or a [hybrid connectivity solution](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#google-cloud), such as [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
  2. If your destination endpoint is within Google Cloud: 
     1. Configure [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) between VPC networks.
     2. Configure [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) between VPC networks.
     3. Configure network connectivity using Network Connectivity Center [VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview).
  3. If you already have a connection to the destination network:

     1. The source endpoint network doesn't have a route through this connection or uses the default route that goes through the internet gateway. Verify the [list of effective routes](https://docs.cloud.google.com/vpc/docs/using-routes#listingroutes), and the [list of routes applicable to the source instance](https://docs.cloud.google.com/vpc/docs/using-routes#applicable-routes) in the Google Cloud console. For more information about route creation and [applicability](https://docs.cloud.google.com/vpc/docs/routes#instancerouting), see [Routes](https://docs.cloud.google.com/vpc/docs/routes) and [Use routes](https://docs.cloud.google.com/vpc/docs/using-routes).

If you are testing connectivity to an on-premises network from a peered network, see [this example](https://docs.cloud.google.com/vpc/docs/vpc-peering#on-premises_access_from_peer_network) for custom advertisement, network routing mode, and exchanging custom routes.

[Transitive VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering#transit-network) is not supported. You can use VPN or peering for these two VPC networks.




## Private Google Access is disallowed

Compute Engine instance with only an internal IP address tries to reach the external IP address of Google APIs and services, but Private Google Access is not enabled in the instance's subnet.

### Recommendations

You can allow the Compute Engine VM instance to reach the external IP address of Google APIs and services in any of the following ways:

  1. Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) for the instance's subnet.
  2. Assign an external IP address to the Compute Engine NIC.
  3. Enable [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) for the VM instance's subnet.



## Private Google Access through VPN tunnel is not supported

A source endpoint with an internal IP address tries to reach the external IP address of Google APIs and services through the VPN tunnel to another network, but Private Google Access needs to be enabled in the source endpoint network.

### Probable cause

The packet from the source endpoint to the external IP address of the Google APIs and services is routed through the Cloud VPN tunnel, but such a configuration is not supported.

### Recommendations

If the source endpoint is a Google Cloud endpoint (like a Compute Engine VM instance), consider enabling [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) in its source subnet.

If the source endpoint is an on-premises endpoint, refer to the [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid) for detailed instructions.

## Unknown internal address

The destination internal IP address can't be resolved to a known target.

### Recommendations

  * If you are testing connectivity for a Shared VPC network, check if the service project ID is provided as a test input.
  * Verify that the IP address is assigned to a supported destination endpoint.



## Forwarding rule mismatch

The forwarding rule's protocol and ports don't match the packet header.

### Probable cause

The packet is sent using a protocol that isn't supported by the forwarding rule, or the packet is sent to a destination port that doesn't match the ports supported by the forwarding rule.

### Recommendations

Confirm the destination forwarding rule protocol and ports.

## Forwarding rule region mismatch

The forwarding rule doesn't have global access enabled, and its region doesn't match the packet's region.

### Probable cause

Depending on the load balancer and its tier, a [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) is either global or regional. For more details, see [the load balancer types table](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#summary-of-google-cloud-load-balancers).

If the forwarding rule is regional, the client (for example, the VM or the VPC connector) should be in the same region as the load balancer.

### Recommendations

If you connect to the load balancer from a Google Cloud endpoint such as a Compute Engine VM instance, make sure it's located in the same region as the forwarding rule.

While connecting from an on-premises network, make sure that the client accesses the load balancer through Cloud VPN tunnels or VLAN attachments that are in the same region as the load balancer. For more details, see [Internal Application Load Balancers and connected networks](https://docs.cloud.google.com/load-balancing/docs/l7-internal/internal-https-lb-and-other-networks).

You can enable [global access](https://docs.cloud.google.com/load-balancing/docs/internal#client-access) on internal Application Load Balancers and regional internal proxy Network Load Balancers to access clients in any region. By default, clients for these load balancers must be in the same region as the load balancer. For more information, see [Enable global access for internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#global-access) and [Enable global access for regional internal proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs#global-access).

## Firewall blocking load balancer backend health check

Firewalls block health check probes to the backends and cause backends to be unavailable for traffic from the load balancer.

### Probable cause

For health checks to work, you must create ingress allow firewall rules that allow traffic from Google Cloud probers to reach your backends. Otherwise, the backends are considered unhealthy.

### Recommendations

Create ingress allow firewall rules according to the [probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges) table. For more information, see [Required firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-checks#firewall_rules).

## No external address available

A VM instance with only an internal IP address tried to access external hosts through a route whose next hop is the default internet gateway. Expected when Cloud NAT is not enabled in the subnet or when there's no other default route that uses a different type of next hop (such as a proxy VM).

### Probable cause

An instance with only an internal IP address tried to access an external host but it did not have an external IP address or Cloud NAT was not enabled in the subnet.

### Recommendations

If you'd like to access external endpoints, you can assign an [external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses) to your instance. Alternatively, you can enable [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) on its subnet unless the connection goes through a proxy instance that gives access to the internet.

## Forwarding rule with no instances

The forwarding rule isn't associated with any backends.

### Probable cause

This drop occurs for the following reasons:

  * No backends are attached to the backend service of the load balancer.
  * The forwarding rule references a target proxy and that target proxy is missing its routing configuration: 
    * **Application Load Balancers** : the target proxy isn't associated with a URL map.
    * **Proxy Network Load Balancers that use Server Name Indication (SNI) routing** : the target proxy isn't associated with a TLS route.



### Recommendations

Review your load balancer configuration as follows:

  * Make sure that the default [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) has backends attached.
  * For Application Load Balancers, make sure that the target proxy references a [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) and the backend service or services that are defined in the URL map have backends attached.
  * For proxy Network Load Balancers that use SNI routing, make sure that the target proxy is referenced in at least one [TLS route](https://docs.cloud.google.com/load-balancing/docs/tcp#tls-routes) and the backend service or services that are defined in the TLS route have backends attached.



## Traffic type is blocked

The type of traffic is blocked and you cannot configure a firewall rule to enable it. For more details, see [Always blocked traffic](https://docs.cloud.google.com/vpc/docs/firewalls#blockedtraffic).

### Probable cause

This traffic type is blocked by default and can't be enabled by creating firewall rules. Common scenarios are as follows:

  1. Sending egress traffic to an external destination with TCP port 25 (SMTP). For more details, see [Always blocked traffic](https://docs.cloud.google.com/vpc/docs/firewalls#blockedtraffic).
  2. Sending traffic to an unsupported port on a Cloud SQL instance. For example, sending traffic to TCP port 3310 to a MySQL Cloud SQL instance with port 3306 open.
  3. Sending egress traffic from an App Engine standard environment version, a Cloud Run function, a Cloud Run revision, or a Cloud Run job that uses a protocol other than TCP or UDP.



### Recommendations

For egress SMTP (egress traffic to an external destination with TCP port 25) traffic, see [Sending email from an instance](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail).

For DHCP protocol, including UDP IPv4 packets to destination port 68 (DHCPv4 responses) and UDP IPv6 packets to destination port 546 (DHCPv6 responses), DHCP traffic is only allowed from the metadata server (169.254.169.254).

For Cloud SQL connectivity, make sure the port used is correct.

## Access to the control plane of the GKE cluster is not authorized

Access to the control plane of the GKE cluster from the source IP address is not authorized.

### Probable cause

The source IP you are using doesn't match the authorized access rules that are configured on your GKE cluster. For more information, see [Access to the cluster endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#access_to_the_cluster_endpoints).

### Recommendations

Update the GKE control plane access to allow the selected source, as described in [Modify the control plane access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#modify_the_control_plane_access).

## Access to the Cloud SQL instance is not authorized

Access to the Cloud SQL instance from the source IP address isn't authorized.

### Probable cause

The source IP you are using doesn't match the authorized networks configured on your Cloud SQL instance. For the connection to work, your client application's IP address or address range must be configured as an authorized network on the Cloud SQL instance.

### Recommendations

Update the Cloud SQL instance access to allow the selected source IP address, as described in [Authorize with authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks).

## Network tags are not supported by Direct VPC egress in ingress firewall rules

The packet is dropped because Direct VPC egress doesn't support source network tags in ingress firewall rules.

### Probable cause

Matching ingress firewall rules by source network tags isn't supported for Cloud Run connections through Direct VPC egress. For more information, see [Limitations](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#limitations).

### Recommendations

Update your firewall rules to use source IP ranges instead of source network tags to match traffic from Cloud Run connections through Direct VPC egress.

## Serverless VPC Access connector is not configured

The packet was dropped because the App Engine standard environment version, the Cloud Run function, or the Cloud Run revision or job doesn't have a [Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) configured.

### Probable cause

The destination IP address is a [private IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses), which cannot be reached through the internet. The packet leaves the source, but there is no Serverless VPC Access connector configured for the App Engine standard environment version, the Cloud Run function, or the Cloud Run revision or job.

### Recommendations

If you try to access the destination endpoint by using its private IP address, make sure that you have configured a Serverless VPC Access connector for the App Engine standard environment version, the Cloud Run function, or the Cloud Run revision or job.

## Serverless VPC Access connector is not running

The packet was dropped because the [Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) is not running.

### Probable cause

The packet was dropped because all the Serverless VPC Access connector instances are stopped.

### Recommendations

For a list of troubleshooting steps, see [Troubleshooting](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#troubleshooting).

## Private Service Connect connection is not accepted

The packet was dropped because the Private Service Connect connection was not accepted.

### Probable cause

The Private Service Connect endpoint is in a project that is not approved to connect to the service. For more information, see [View endpoint details](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#endpoint-details).

### Recommendations

Make sure that the Private Service Connect endpoint is in a project that is approved to connect to the managed service.

## Private Service Connect endpoint is accessed from a peered network

The packet is sent to the Private Service Connect endpoint in the peered network, but such a configuration [is not supported](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility#endpoints-services).

### Recommendations

Google recommends that you transition to a [hub-and-spoke architecture that uses Network Connectivity Center](https://cloud.google.com/architecture/deploy-hub-spoke-vpc-network-topology#ncc) to enable [Private Service Connect connection propagation](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview).

Alternatively, consider one of the following connectivity patterns:

  * If supported by the service producer, transition to a [multi-point access](https://cloud.google.com/vpc/docs/private-service-connect-deployments#multi-point) connectivity pattern.

  * If supported by the service producer, configure a [supported consumer load balancer](https://cloud.google.com/vpc/docs/private-service-connect-backends#consumer-configuration-backends) with a Private Service Connect backend.




For further assistance, contact your service producer support or Google Cloud representative.

## No valid route from a Google-managed network to destination

The packet is dropped because there is no valid matching route from the network of the Google-managed service to the destination.

This drop cause applies to any Google-managed service supported by Connectivity Tests, including Cloud SQL and GKE.

### Recommendations

Verify whether the Google-managed service is configured to send traffic to the destination.

  * If the destination is intended to be reachable through local static or dynamic routes configured in your VPC network, ensure that the VPC network exports those routes to the network of the Google-managed service. This pattern is common for connections from Google-managed services to destinations reachable through Cloud VPN or Cloud Interconnect.

    * For connections over VPC Network Peering, see [Options for exchanging static routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#static-route-exchange) and [Options for exchanging dynamic routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#dynamic-route-exchange).

    * For connections through Network Connectivity Center producer VPC spokes, see [Route exchange with VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes) and [Shared properties with VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview#shared-properties).

  * If the destination is located in a subnetwork configured with privately used public IP address ranges, ensure that your network exports the corresponding subnet routes to the network of the Google-managed service.

    * For connections over VPC Network Peering, see [Options for exchanging subnet routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#subnet-route-exchange).

    * For connections through Network Connectivity Center producer VPC spokes, see [Privately used public IPv4 addresses](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#privately-used-public-ip-addresses).

  * If the destination is an internet-routable external IP address, ensure that the Google-managed service is configured for this connectivity path. For example, some types of Cloud SQL instances don't support outbound external connections.

  * If the destination is intended to be reachable through dynamic routes imported to the network of the Google-managed service through VPC Network Peering, the [Dynamic routes per region per peering group](https://docs.cloud.google.com/vpc/docs/quota#per_network) limit for the service network might be reached. If you believe this limit has been reached, [file a support case](https://cloud.google.com/support-hub).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
