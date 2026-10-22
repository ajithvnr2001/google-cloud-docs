---
url: https://docs.cloud.google.com/dns/docs/troubleshooting/
title: Troubleshoot Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:32.002398+00:00
---

# Troubleshoot Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Troubleshoot Cloud DNS Stay organized with collections  Save and categorize content based on your preferences. 

This page provides solutions for common issues that you might encounter when using Cloud DNS to create public zones, private zones, reverse lookup zones, forwarding zones, and resource records.

## Public zones

This section covers issues with public zones.

### Cannot create a public zone

If you get an `attempted action failed` error, it means that the Cloud DNS API is not enabled on your project.

To enable the Cloud DNS API, follow these steps:

  1. In the Google Cloud console, go to the **API Library** page.

[Go to the API Library](https://console.cloud.google.com/project/_/apis/library)

  2. For **Select a recent project** , select the Google Cloud project where you want to enable the API.

  3. On the **API library** page, use the **Search for APIs & Services** box to search for `Cloud DNS API`. A page describing the API appears.

  4. Click **Enable**. 




## Private zones

This section covers issues with private zones.

### Private zone problems in Shared VPC service projects

For important information about using private zones with Shared VPC networks, see [Private zones and Shared VPC](https://docs.cloud.google.com/dns/docs/overview#shared-vpc).

### Cannot create a private zone, cannot list or create policies

You must have the [DNS Administrator role](https://docs.cloud.google.com/dns/docs/access-control#roles) to perform various private zone actions, such as listing Domain Name System (DNS) server policies or creating a private zone. This role can be [granted through the Identity and Access Management (IAM) tool](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console).

### Private zones not resolving in the same VPC network

First, make sure that you're performing the test from the same network.

#### Verify that your VM instance's primary interface is on the same network as the private zone that you have created

A virtual machine (VM) instance sends all traffic out of its primary interface unless the traffic is destined for a subnet attached to one of the other interfaces or if the VM has [policy routing](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface#configuring_policy_routing) configured. Make sure that your test VM has its primary interface on the same network as the private zone that you're testing.

Determine that your VM is using:
    
    
    gcloud compute instances describe VM_NAME \
        --zone=GCE_ZONE \
        --format="csv[no-heading](networkInterfaces['network'])"
    

Ensure that the network is in the list of networks authorized to query your private zone:
    
    
    gcloud dns managed-zones describe PRIVATE_ZONE_NAME \
        --format="csv(privateVisibilityConfig['networks'])"
    

#### Verify that the DNS name in the query matches your zone

Google Cloud resolves a record according to the [name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order), using the zone with the longest suffix to decide which zone to query for a given DNS name. Make sure that the suffix for the record that you're querying matches at least one private zone accessible in your VPC network. For example, Google Cloud first looks for `myapp.dev.gcp.example.lan` in a zone that serves `dev.gcp.example.lan`, if accessible, before it looks for it in a zone that serves `gcp.example.lan`, if accessible.

The output of the following command shows the DNS suffix for a given private zone:
    
    
    gcloud dns managed-zones describe PRIVATE_ZONE_NAME \
        --format="csv[no-heading](dnsName)"
    

#### Query for the DNS name using the metadata server

Use `dig` to submit the DNS name query directly to the Google Cloud metadata server, `169.254.169.254`:
    
    
    dig DNS_NAME @169.254.169.254
    

Use `dig` to query the VM's default name server:
    
    
    dig DNS_NAME
    

If the output of the two `dig` commands produces different answers, check the `;; SERVER:` section of the second command. The responding server must be the metadata server, `169.254.169.254`. If it is not, then you've configured the guest operating system to use a custom DNS name server instead of the default Google Cloud metadata server. Cloud DNS private zones require that you use the metadata server for name resolution. Both the [Linux guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment#linux) and the [Windows guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment#windows) do this for you. If you've imported the image that you're using for a VM, verify that the appropriate guest environment has been installed.

### Private zones not resolving through Cloud VPN or Cloud Interconnect

First make sure that you can successfully query and resolve the DNS name from within an authorized VPC network.

#### Verify connectivity through Cloud VPN or Cloud Interconnect

Ensure that connectivity from an on-premises system to your VPC network is operational. Specifically, TCP and UDP traffic on port 53 must be able to leave your on-premises network and be delivered to your VPC network. Verify the configuration of on-premises firewalls to make sure that such egress traffic is allowed.

You can use any protocol, such as `ping` (ICMP), to test connectivity to a sample VM in your VPC network from on-premises. While Cloud DNS requests are not sent to Google Cloud VMs, testing connectivity to a sample VM lets you verify connectivity through a Cloud VPN tunnel or Cloud Interconnect connection. Make sure that you configure an appropriate ingress allow firewall rule for the sample Google Cloud VM because the [implied deny ingress rule](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) blocks all incoming traffic otherwise.

#### Ensure inbound forwarding is enabled for the authorized VPC network

Inbound forwarding must be enabled for each VPC network that is authorized to query your Cloud DNS private zone. Use the following command to list all policies:
    
    
    gcloud dns policies list
    

Identify the network in the output table, and check for the **Forwarding** field to see if forwarding is enabled.

#### Make sure the authorized network is a VPC network

DNS forwarding requires subnets, which are only available to [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc), _not_ [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy).
    
    
    gcloud compute networks list \
        --format="csv[no-heading](name, SUBNET_MODE)"
    

Legacy networks are identified in the output as `LEGACY`.

#### Make sure there is a valid DNS forwarding address reserved in that network

The following command shows all the reserved DNS forwarding IP addresses in your project.
    
    
    gcloud compute addresses list \
        --filter="purpose=DNS_RESOLVER" \
        --format='csv[no-heading](address, subnetwork)'
    

You can add an `AND` clause to the filter to limit the output to only the subnetwork that you care about.

Example:

`--filter="name ~ ^dns-forwarding AND subnetwork ~ SUBNETWORK_NAME"`

If you don't see an IP address in the network or region that you expected, file a ticket with [Google Cloud Support](https://docs.cloud.google.com/support).

Run the `dig` command pointing the query at the address that you found in the preceding command. Do so from a VM in the same network. This test verifies that the inbound forwarder is working, and that the problem lies elsewhere.
    
    
    dig DNS_NAME @10.150.0.1 # address returned by previous command
    

Repeat the same `dig` command but from an on-premises host across the VPN.

### CNAME record defined in a private zone not working

Cloud DNS only chases CNAME records as described in [CNAME chasing](https://docs.cloud.google.com/dns/docs/cnamechasing).

## Reverse lookup zones

This section provides troubleshooting tips for reverse lookup zones. Some private zone issues also apply to reverse lookup zones. For additional tips, see the Private zones troubleshooting section.

### VM with non-RFC 1918 address not resolving

If you have a non-RFC 1918 address, reconcile your VM.

#### Reconciliate your VM with a non-RFC 1918 address

If you created a VM during the non-RFC 1918 alpha before Cloud DNS support was launched, these VMs might not resolve correctly. To resolve this issue, restart your VMs.

## Forwarding zones

This section provides troubleshooting tips for forwarding zones. Some private zone issues also apply to forwarding zones. For additional tips, see the Private zones troubleshooting section.

### Forwarding zones (outbound forwarding) not working

First make sure that you can successfully query and resolve the DNS name from within an authorized VPC network.

### Forwarding queries from VMs in a consumer VPC network to a producer VPC network not working

If you are using DNS peering and you want to forward queries from VMs in a consumer VPC network to a producer VPC network, and then to one or more on-premises name servers, make sure that one of the following prerequisites is met:

  * The producer VPC network has its [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes) set to `GLOBAL`.

  * The VM in the consumer VPC network is in the same region as the VPN tunnel or Cloud Interconnect in the producer VPC.

  * (**(Static routes or custom next hops only**) The producer VPC network has a [static route](https://docs.cloud.google.com/vpc/docs/routes#static_routes) configured to send traffic destined for the on-premise name servers through the Classic VPN tunnel, a self-managed VPN, or a non-BGP gateway. The producer VPC network must also have a VM or a VPN tunnel in the same region as the subnetwork used by the client VMs.

    * For example, suppose that VPC1 uses a peering zone that sends queries for `example.com.` to VPC2. Suppose also that VPC2 has a private forwarding zone for `example.com.` that forwards the queries to an on-premises name server using a Classic VPN tunnel.

For a VM located in `us-east1` in VPC1 to be able to query `example.com.`, VPC2 must have a VM located in `us-east1`. A [static route](https://docs.cloud.google.com/vpc/docs/routes#static_routes) must also be configured covering the CIDR ranges of the on-premises name servers, with the next hop configured as the Classic VPN tunnel.

#### Verify connectivity through Cloud VPN or Cloud Interconnect




You can use any protocol, such as `ping` (ICMP), to test connectivity to a sample VM in your VPC network from on-premises. You must also attempt to query your on-premises name server directly from a sample Google Cloud VM by using a tool like `dig`:
    
    
    dig DNS_NAME @192.168.x.x # address of the onprem DNS server
    

#### Check firewall rules in your VPC network

The [implied allow egress firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) allows outbound connections and established responses from VMs in your VPC network unless you have created custom rules to deny egress. If you've created custom deny egress rules, you'll need to create higher priority allow rules that permit egress to at least your on-premises name servers.

#### Check on-premises firewall

Make sure that your on-premises firewall is configured to allow incoming traffic from and outgoing traffic to `35.199.192.0/19`.

Check logs in your on-premises firewall, looking for DNS requests from `35.199.192.0/19`. To use a `regex` expression to search, use the following:

`"35\.199\.(19[2-9]|20[0-9]|21[0-9]|22[0-3]).*"`

#### Check on-premises name server

Verify that you don't have any ACL configured in your on-premises name server that would block queries from `35.199.192.0/19`.

Check your on-premises name server to see if it is receiving packets from `35.199.192.0/19`. If you have shell access, you can use a tool such as `tcpdump` to look for both incoming packets from and outgoing packets to `35.199.192.0/19`:
    
    
    sudo tcpdump port 53 and tcp -vv
    

#### Verify return routes

Your on-premises network must have a route to the `35.199.192.0/19` destination with the next hop being a VPN tunnel or Interconnect connection for the same VPC network that sent the DNS request. This behavior is described in [Creating forwarding zones](https://docs.cloud.google.com/dns/docs/zones#creating-forwarding-zones).

If you use multiple VPN tunnels to connect the same VPC network to your on-premises network, the response does not have to be delivered using the same tunnel that sent it. However, the response must be delivered by using a VPN tunnel with a next hop in the _same_ VPC network from which the request originated.

If you have connected more than one VPC network to your on-premises network, you must ensure that DNS replies are not sent to the wrong one. Google Cloud discards DNS responses sent to the wrong VPC network. For a recommended solution, see our [Best practices](https://docs.cloud.google.com/dns/docs/best-practices#hybrid-architecture-using-multiple-vpc-networks) guide.

### Outbound forwarding to a name server that uses a non-RFC 1918 IP address fails

By default, Cloud DNS uses standard routing, which routes queries through the public internet when the target name server has a non-RFC 1918 IP address. Standard routing doesn't support forwarding queries to name servers with non-RFC 1918 addresses that are not reachable from the public internet.

To forward queries to a name server that uses a non-RFC 1918 IP address through your VPC network, configure the Cloud DNS forwarding zone or server policy to use private routing for the target name server.

For an explanation of the differences between standard and private routing, see [forwarding targets and routing methods](https://docs.cloud.google.com/dns/docs/overview#fz-targets).

This limitation applies even if there is a VPC route for the target name server; routes for non-RFC 1918 addresses have no effect on Cloud DNS's outbound forwarding behavior when standard routing is configured. 

### Outbound forwarding to a secondary NIC fails

Make sure that you have set up your secondary network interface controller (NIC) correctly.

For instructions about how to set up additional NICs, see [Creating virtual machine instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces#creating_virtual_machine_instances_with_multiple_network_interfaces).

### Outbound forwarded queries receive SERVFAIL errors

If Cloud DNS receives an error from all target name servers or does not receive a response from any of the target name servers, it returns a `SERVFAIL` error.

To resolve this issue, verify that your on-premises name servers are properly configured. Then, verify that your on-premises name servers respond to queries from the Cloud DNS address range described in [Open Google Cloud and on-premises firewalls to allow DNS traffic](https://docs.cloud.google.com/dns/docs/best-practices#open-google-cloud-and-on-premises-firewalls) within 4 seconds. If your on-premises name servers consult upstream name servers (for example, due to being configured as caching resolvers), check that there are no issues with upstream name servers.

Additionally, if the forwarding target is an on-premises system, be aware that the routes configured for that path can be custom dynamic routes or custom static routes, with the important exception that _custom static routes with network tags are not valid for forwarding DNS queries_. Ensure that the route used to reach the on-premises name server does not specify a network tag.

## Resource records

This section provides troubleshooting tips for resource records.

### Unexpected data when querying for resource record sets present in the zone

There are several reasons why you might receive unexpected data when querying for resource record sets present in a Cloud DNS managed zone:

  1. Resource record sets created by using the `@` syntax specified in [RFC 1035](https://tools.ietf.org/html/rfc1035#section-5.1) are not supported. Cloud DNS interprets the `@` symbol in such resource record sets literally; therefore, in the `example.com.` zone, a record set created for the QNAME `@` is interpreted as `@.example.com.` instead of `example.com.`. To resolve this issue, ensure that you create record sets without the `@` symbol; all names are relative to the apex of the zone.

  2. Like all records, wildcard CNAME records are subject to the existence rules described in [RFC 4592](https://tools.ietf.org/html/rfc4592#section-2.2). For example, suppose that you define the following record sets in the `example.com.` zone:

`*.images.example.com. IN CNAME _static.example.com.`

`srv1.images.example.com. IN A 192.0.2.91`

`_static.example.com. IN A 192.0.2.92`

A query for `public.srv1.images.example.com.` returns `NOERROR` with an empty answer section. The existence of a record _between_ the CNAME and the QNAME prevents the CNAME from being returned, but there's no record that matches the QNAME exactly, so Cloud DNS returns an empty answer. This is standard DNS behavior.




### Google Cloud VM shows incorrect pointer (PTR) records

When a VM is migrated during a maintenance event, the PTR record logic doesn't handle some edge cases correctly and reverts the DNS PTR records to the `googleusercontent.com` fully qualified domain name (FQDN). To restore functionality, apply the PTR record again.

For details about how to apply PTR records on a VM, see [Creating a PTR record for a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-ptr-record). 

### Cloud DNS resource record sets returned in random order

Consistent with DNS industry practices, Cloud DNS name servers now randomize the order of the resource record sets and ignore the ordering given by the authoritative server. This is normal DNS behavior and applies to both public _and_ private Cloud DNS zones.

## Unsupported zonal resource type

When you enter the `--location` flag to a `gcloud` command or API request for a feature that targets a different Cloud DNS zone, the request is rejected. For example, if you send a zonal-only feature request to a global server, or a global-only feature request to a zonal server, the server rejects the request and gives an _UNSUPPORTED_ZONAL_RESOURCE _TYPE_ error.

For a list of resources and features that zonal Cloud DNS supports, see [zonal Cloud DNS support](https://docs.cloud.google.com/dns/docs/zones/zones-overview#zonal-dns-support).

## Advanced threat detection

This section provides information about issues that you might encounter when using DNS Armor and provides suggestions for how to fix each of them.

### Metrics show no or very low DNS queries being sent to the threat detector

First, verify that you have a DNS threat detector.

#### Verify your DNS threat detector

  1. In the Google Cloud console, go to the **Advanced threat detection** page.

[Go to Advanced threat detection](https://console.cloud.google.com/net-security/dns-armor/threat-detectors/list)

  2. Verify that you have a threat detector listed.




#### Verify region support

  1. Make sure that [Locations](https://docs.cloud.google.com/dns/docs/threat-detector-locations) contains the region serving your workflow's DNS queries.



#### Verify that you have internet-bound queries

Query logs are only sent when internet-bound queries or requests are made of your network.

  1. In the Google Cloud console, go to the Monitoring page.

[Go to Monitoring](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. In **Metric** select `Cloud DNS Query`, then choose `Query` and `DNS response counts`.

  3. View the metrics for target types that are internet-bound.




Alternatively, if you have enabled Cloud logging for DNS queries, use the Logs Explorer to verify that you have internet-bound queries.

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer?resource=dns_query)

  2. View your DNS logs and check for internet-bound queries.




### Threat event logs aren't returned

If threat events aren't received by Cloud Logging, first verify that an advanced threat detector is set up on the [Dashboard](https://console.cloud.google.com/home/dashboard). Note that threat event logs are only returned when a threat is detected.

#### Verify threat detection is enabled

  1. In the Google Cloud console, go to the **Advanced threat detection** page.

[Go to Advanced threat detection](https://console.cloud.google.com/net-security/dns-armor/threat-detectors/list)

  2. Verify that you have a threat detector listed.




### DNS threats events aren't generated for some abusive or bad domains

Some DNS threat events for abusive or bad domains might not be generated for domains obtained from public bad domain lists on the Internet as DNS threat domains change frequently. Old or expired domains from those lists don't generate DNS threat events.

The following are test domains you can use to verify DNS threat domains:

  * dnst-gcp-blox.com
  * ftags-gcp-blox.com
  * dga-gcp-blox.com



#### Verify that DNS threat events are generated for test domains

  1. Sign in to a VM that is part of project you're monitoring.

  2. Open a terminal and issue a dig command for one of the test domains. 
         
         domain=TEST_DOMAIN   
         
         dig $domain -t A
         

Replace `TEST_DOMAIN` with one of the listed domains.

  3. Open the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer)

  4. Run the following query: `resource.type="networksecurity.googleapis.com/DnsThreatDetector"`

  5. Search for the test domain you used in the dig command.

These domains generate DNS threat events. If you can't find DNS logs for the listed domains, contact [Support](https://docs.cloud.google.com/dns/docs/support).




## Outbound Endpoints

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This section describes issues you might encounter when using Outbound Endpoints and how to resolve them.

### DNS queries not being forwarded to the target servers

There are several potential causes for this issue.

#### Resource misconfiguration

Your endpoint and forwarding zone or server policy needs to be properly configured. This includes the endpoint being associated with the correct VPC network and region, or the forwarding zone or server policy being configured to use the right Outbound Endpoint(s).

Make sure the regional proxy-only subnet is configured correctly and has sufficient IP addresses available for proxying queries. You can also enable query logging and then check the query logs for the `jsonPayload.egressPath` field; this field is set to `OUTBOUND_ENDPOINT` if the forwarded query is using Outbound Endpoints. If the query logs don't include this field, or if the field isn't set to `OUTBOUND_ENDPOINT`, traffic defaults to `35.199.192.0/19`.

You can verify your configuration by running the [`gcloud beta dns outbound-endpoints describe` command](https://docs.cloud.google.com/dns/docs/create-update-outbound-endpoints#view-outbound-endpoints):
    
    
    gcloud beta dns outbound-endpoints describe ENDPOINT_NAME \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `ENDPOINT_NAME`: name of the endpoint
  * `PROJECT_ID`: project ID
  * `REGION`: region where the endpoint is located



#### Network connectivity

Verify a route exists from your VPC network to the on-premises or remote DNS servers and that the on-premises firewall rules allow TCP/UDP port 53 traffic from proxy-only subnet IP range. Also check that a route exists from the on-premises network back to the proxy-only subnet IP range.

### Shared VPC or peering issue

  * **Shared VPC issue** : Outbound Endpoints must be created in the host project where the Shared VPC network and subnets reside. When associating a forwarding zone or DNS server policy in a service project with an Outbound Endpoint in the host project, verify the user has `dns.outboundEndpoints.bindPrivateDNSZone` or `dns.outboundEndpoints.bindPrivateDNSPolicy` on the host project.
  * **Peering issue** : verify the VPC network peering status is set to `Active`.



Also check that routes and firewall rules allow DNS traffic (UDP and TCP port 53) between the regional proxy-only subnet IP range in the endpoint's VPC network and the target DNS servers.

### DNS queries timing out

The following sections describe why your DNS queries might be timing out when using Outbound Endpoints.

#### Network latency issue between the Outbound Endpoint and target servers

Check the latency between your VPC network and target DNS servers. Moving the target DNS servers geographically closer to your Google Cloud project may also help.

#### Proxy-only subnet exhaustion

Check the IP address utilization of the proxy-only subnet in the region where queries are failing with Monitoring. If the subnet is almost exhausted, migrate to a larger proxy-only subnet using the steps in [Subnet modification](https://docs.cloud.google.com/dns/docs/outbound-endpoints-overview#subnet-modification).

#### Geolocation policy misconfiguration

Verify your Geolocation routing policy contains an entry for the region where the Outbound Endpoint is located. Also check if the FQDN destination in your forwarding zone matches the DNS name of your Geolocation policy zone.

### Can't create an Outbound Endpoint

The following sections describe why you might be unable to create an Outbound Endpoint.

#### IAM permission issue

Verify the user or service account has the `roles/dns.admin` and `roles/compute.networkAdmin` roles (or permissions for `dns.outboundEndpoints.create`, `compute.networks.get`, `compute.subnetworks.get`, and `compute.subnetworks.use`). For a Shared VPC, Outbound Endpoints must be created in the host project (creating an Outbound Endpoint in a service project is not supported).

#### IP address string provided in `endpointIp` doesn't match the CIDR range of the specified regular subnet, or is malformed

Check the CIDR range of the specified regular subnet in the target region and ensure the IP string provided in `endpointIp` (`--endpoint-ip`) is within the subnet's primary CIDR range. Also make sure the IP isn't a reserved IP address in the subnet (for example, gateway or broadcast).

#### IP address string provided is valid but already in use by another resource

Check in Google Cloud console for your VPC network's IP addresses or use the [`gcloud compute addresses list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/list) and provide a different unallocated IPv4 address from the regular subnet with `--endpoint-ip`.

#### The system couldn't find an active regional proxy-only subnet

Make sure an active regional proxy-only subnet exists in the specified VPC network and region. If one doesn't exist, create a regional proxy-only subnet (minimum `/26`) with `--purpose=REGIONAL_MANAGED_PROXY` and `--role=ACTIVE` (see [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)).

### Resource deletion fails

If you are unable to delete a resource, it might be in active use by an Outbound Endpoint.

#### Attempt to delete a resource that is in active use

Follow the steps outlined in [Manage network resources associated with Outbound Endpoints](https://docs.cloud.google.com/dns/docs/outbound-endpoints-overview#manage-network-resources).

## What's next

  * To learn more about Cloud DNS features, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).
  * To resolve errors, see [Error messages](https://docs.cloud.google.com/dns/docs/error-messages).
  * To get additional help, see [Support](https://docs.cloud.google.com/dns/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
