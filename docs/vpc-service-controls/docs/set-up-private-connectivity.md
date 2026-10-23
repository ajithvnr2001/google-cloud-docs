---
url: https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity/
title: Set up private connectivity to Google APIs and services \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:22.385440+00:00
---

# Set up private connectivity to Google APIs and services  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Set up private connectivity to Google APIs and services Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up private connectivity from hosts in a VPC network or on-premises network to Google APIs and services that VPC Service Controls supports.

Before you read this document, we recommend that you familiarize yourself with [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access#pga) concepts, [specifications, and network configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access). See example topology diagrams about using [Private Google Access with VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity).

## Before you begin

  * [Enable the APIs](https://support.google.com/cloud/answer/6158841) that you want to access through the [APIs & services page](https://console.cloud.google.com/apis/dashboard) in the Google Cloud console.
  * Ensure that you have the required role to create or update subnets. Project owners, editors, and IAM principals with the [Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) role can create or update subnets and assign IP addresses. For more information about roles, read the [IAM roles](https://docs.cloud.google.com/compute/docs/access/iam) documentation.
  * Verify that a [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) is set up for Private Google Access and Private Google Access for on-premises hosts. Both auto and custom mode VPC networks are supported. [Legacy networks](https://docs.cloud.google.com/vpc/docs/legacy) are not supported.
  * Ensure that VM instances in a VPC network have a private IP address (no public IP address) and are in a subnet with [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access#pga) enabled.
  * For on-premises hosts, ensure that you have an existing [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) tunnel or a [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) connection to your VPC network. To support on-premises hosts that have IPv6 addresses, see IPv6 support.



## Overview of procedure

To set up private connectivity, complete the following tasks:

  * Configure routes for the `restricted.googleapis.com` IP address ranges. For more information, see Configure routes.
  * Configure firewall rules to let the appropriate traffic reach the `restricted.googleapis.com` IP address ranges. For more information, see Configure firewall rules.
  * Configure DNS so that traffic to Google APIs resolves to the `restricted.googleapis.com` IP address ranges. For more information, see Configure DNS.



### IPv6 support for `restricted.googleapis.com`

You can access Google APIs by using the IPv6 address range for the `restricted.googleapis.com` domain: `2600:2d00:0002:1000::/56`.

Consider configuring the IPv6 addresses if you want to use the `restricted.googleapis.com` domain, and you have clients that use IPv6 addresses. IPv6 clients that also have IPv4 addresses configured can reach Google APIs and services by using the IPv4 addresses. Not all services accept traffic from IPv6 clients.

To let IPv6 clients in your on-premises environment access Google APIs by using `restricted.googleapis.com`, you must configure the connection to your VPC network to support IPv6. For more information, see the following pages: 

  * [IPv6 support for HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ipv6_support)
  * [IP protocols support for Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#ip-protocols)



On-premises clients can send requests from any IPv6 GUA or ULA addresses, except for the ULA range `fda3:e722:ac3:cc00::/64`, which is reserved for internal use. 

For more information about the `restricted.googleapis.com` VIP, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

### Direct connectivity to APIs and services

Some Google APIs and services support direct connectivity from Compute Engine virtual machine (VM) instances, bypassing [Google Front Ends (GFEs)](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service), offering better performance.

To establish direct connectivity, it is necessary that your [routes](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-routing-custom) and [firewall rules](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-firewall) allow IPv4 traffic to reach `34.126.0.0/18` and IPv6 traffic to reach `2001:4860:8040::/42`.

These IP addresses support VPC Service Controls. Additionally, DNS records don't need to be created for these addresses.

Note that direct connectivity is available only from Google Cloud resources and is not supported from on-premises hosts.

## Configure routes to `restricted.googleapis.com`

Although VPC Service Controls are enforced for compatible and configured services, regardless of the domain you use, `restricted.googleapis.com` provides additional risk mitigation for data exfiltration. `restricted.googleapis.com` denies access to Google APIs and services that are not supported by VPC Service Controls.

For both Private Google Access and Private Google Access for on-premises hosts, your VPC network must include a route for the `restricted.googleapis.com` IP address ranges whose next hop is the default internet gateway. Even though the next hop is a default internet gateway, the traffic sent to `restricted.googleapis.com` remains within Google's network.

If your VPC network does not have a [default route](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet) whose next hop is the default internet gateway, you can create a custom static route whose destination is the `restricted.googleapis.com` IP address range, and whose next hop is the default internet gateway. To prevent access to the internet, you must remove other routes whose next hop is the default internet gateway.

For more information about working with VPC routes, see [Using Routes](https://docs.cloud.google.com/vpc/docs/using-routes) in the VPC documentation.

### Configure custom static routes in a VPC network

Add custom static routes to enable access to Google-managed services that VPC Service Controls supports.
    
    
    gcloud compute routes create ROUTE_NAME \
      --network=NETWORK_NAME \
      --destination-range=DESTINATION_RANGE \
      --next-hop-gateway=default-internet-gateway

Replace the following:

  * `ROUTE_NAME`: a name for the custom route
  * `NETWORK_NAME`: the name of your VPC network
  * `DESTINATION_RANGE`: the destination range for the route 
    * To route traffic to the `restricted.googleapis.com` VIP, use the following ranges: 
      * For IPv4 traffic: `199.36.153.4/30`
      * For IPv6 traffic: `2600:2d00:0002:1000::/56`
    * To route traffic to APIs that allow direct connectivity, use the following ranges: 
      * For IPv4 traffic: `34.126.0.0/18`
      * For IPv6 traffic: `2001:4860:8040::/42`



### Announce the restricted route to hosts in an on-premises network

If you're using Private Google Access for on-premises hosts, configure routes so that Google API traffic is forwarded through your Cloud VPN or Cloud Interconnect connection. To announce the restricted VIP address ranges to your on-premises network, use [Cloud Router custom advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip). The restricted VIP address ranges are only accessible to on-premises hosts that can reach your VPC network through private IP addresses.

**Note:** If you have multiple tunnels or interconnects, you can't create cross-region asymmetric routes back to your on-premises network. Google Cloud doesn't support them.

You can add this custom advertised route to a Cloud Router (for all BGP sessions on the router) or a select BGP session (for a single Cloud VPN tunnel or VLAN attachment).

IPv6 routes are advertised only in BGP sessions where [IPv6 is enabled](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-ipv6-bgp). 

To create a custom advertised route for the restricted range for all BGP sessions on an existing Cloud Router, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router to update.

  3. In the Cloud Router's detail page, select **Edit**.

  4. Expand the **Advertised routes** section.

  5. For the **Routes** , select **Create custom routes**.

  6. To continue advertising the subnets available to the Cloud Router, select **Advertise all subnets visible to the Cloud Router**. Enabling this option mimics the Cloud Router's default behavior.

  7. To add an advertised route, select **Add custom route** .

  8. Configure the route advertisement.

     * **Source** : Select **Custom IP range**.
     * **IP address range** : 
       * For IPv4 connectivity: `199.36.153.4/30`
       * For IPv6 connectivity: `2600:2d00:0002:1000::/56`
     * **Description** : Add a description of `Restricted Google APIs IPs`.
  9. After you add routes, select **Save**.




###  gcloud 

Run the `update` command, using either the `--set-advertisement-ranges` or `--add-advertisement-ranges` flag to specify the custom IP ranges:

  * To set custom IP ranges, use the `--set-advertisement-ranges` flag. Any existing custom advertised routes are replaced. The following example updates the `my-router` Cloud Router to advertise all subnets and the `restricted.googleapis.com` IP address ranges.
        
        gcloud compute routers update my-router \
            --advertisement-mode CUSTOM \
            --set-advertisement-groups ALL_SUBNETS \
            --set-advertisement-ranges RANGES
        

Replace `RANGES` with the ranges that you want to use: 

    * For IPv4 connectivity: `199.36.153.4/30`
    * For IPv6 connectivity: `2600:2d00:0002:1000::/56`
    * For both IPv4 and IPv6 connectivity: `199.36.153.4/30,2600:2d00:0002:1000::/56`
  * To append custom IP ranges to an existing advertisement, use the `--add-advertisement-ranges` flag. Note that this flag requires the Cloud Router's advertisement mode to already be set to `custom`. The following example adds the `restricted.googleapis.com` IP address ranges to the Cloud Router's advertisements:
        
        gcloud compute routers update my-router \
            --add-advertisement-ranges RANGES
        

Replace `RANGES` with the ranges that you want to use: 

    * For IPv4 connectivity: `199.36.153.4/30`
    * For IPv6 connectivity: `2600:2d00:0002:1000::/56`
    * For both IPv4 and IPv6 connectivity: `199.36.153.4/30,2600:2d00:0002:1000::/56`



To create a custom advertised route for the restricted range on a specific BGP session of an existing Cloud Router, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router that contains the BGP session to update.

  3. In the Cloud Router's detail page, select the BGP session to update.

  4. In the **BGP session details** page, select **Edit**.

  5. For the **Routes** , select **Create custom routes**.

  6. Select **Advertise all subnets visible to the Cloud Router** to continue advertising the subnets available to the Cloud Router. Enabling this option mimics the Cloud Router's default behavior.

  7. Select **Add custom route** to add an advertised route.

  8. Configure the route advertisement.

     * **Source** : Select **Custom IP range** to specify a custom IP range.
     * **IP address range** : 
       * For IPv4 connectivity: `199.36.153.4/30`
       * For IPv6 connectivity: `2600:2d00:0002:1000::/56`
     * **Description** : Add a description of `Restricted Google APIs IPs`.
  9. After you're done adding routes, select **Save**.




###  gcloud 

Run the `update-bgp-peer` command, using either the `--set-advertisement-ranges` or `--add-advertisement-ranges` flag to specify the custom IP ranges.

  * To set custom IP ranges, use the `--set-advertisement-ranges` flag. Any existing custom advertised routes are replaced.

If you are adding IPv6 custom ranges, and if IPv6 traffic is disabled for the BGP session, you can enable it with the `--enable-ipv6` flag. 

The following example updates the `my-bgp-session` BGP session on the `my-router` Cloud Router to advertise all subnets and the custom IP range:
        
        gcloud compute routers update-bgp-peer my-router \
            --peer-name my-bgp-session \
            --advertisement-mode CUSTOM \
            --set-advertisement-groups ALL_SUBNETS \
            --set-advertisement-ranges RANGES
        

Replace `RANGES` with the ranges that you want to use: 

    * For IPv4 connectivity: `199.36.153.4/30`
    * For IPv6 connectivity: `2600:2d00:0002:1000::/56`
    * For both IPv4 and IPv6 connectivity: `199.36.153.4/30,2600:2d00:0002:1000::/56`
  * To append custom IP ranges to existing ones, use the `--add-advertisement-ranges` flag. Note that this flag requires the Cloud Router's advertisement mode to already be set to `custom`.

If you are adding IPv6 custom ranges, and if IPv6 traffic is disabled for the BGP session, you can enable it with the `--enable-ipv6` flag. 

The following example adds the restricted VIP address ranges to the Cloud Router's advertisements:
        
        gcloud compute routers update-bgp-peer my-router \
            --peer-name my-bgp-session \
            --add-advertisement-ranges RANGES
        

Replace `RANGES` with the ranges that you want to use: 

    * For IPv4 connectivity: `199.36.153.4/30`
    * For IPv6 connectivity: `2600:2d00:0002:1000::/56`
    * For both IPv4 and IPv6 connectivity: `199.36.153.4/30,2600:2d00:0002:1000::/56`

For more information about custom advertisement mode, see [Custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes).




## Configure firewall rules

For Private Google Access, VM instances use internal IP addresses and don't require external IP addresses to reach protected Google API resources. However, it's possible for VM instances to possess external IP addresses or otherwise meet the [requirements for internet access](https://docs.cloud.google.com/vpc/docs/vpc#internet_access_reqs). In addition to custom advertised routes, you can restrict egress traffic from VM instances in your VPC network by creating firewall rules to deny egress traffic.

By default, the [implied allow egress firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) permits VM instances to send traffic to any destination if an applicable route exists. You can first create an egress deny rule to block all outbound traffic. You can then create higher priority egress rules that permit traffic to selected destinations in your VPC network and to the `restricted.googleapis.com` IP address ranges. All communication to `restricted.googleapis.com` is on TCP port `443`.

To let traffic from Google Cloud reach the `restricted.googleapis.com` VIPs, add firewall rules for the following destinations:

  * For IPv4 traffic: `199.36.153.4/30`
  * For IPv6 traffic: `2600:2d00:0002:1000::/56`



To allow traffic from Google Cloud to reach APIs and services that allow direct connectivity, add firewall rules for the following destinations:

  * For IPv4 traffic: `34.126.0.0/18`
  * For IPv6 traffic: `2001:4860:8040::/42`

**Note:** Before blocking internet access, carefully consider the impact on your VM instances. Blocking internet access can reduce your risk of data exfiltration, but it can also block legitimate traffic, including essential traffic for software updates. Without internet access, you are only able to access your VM instances through an on-premises network connected through a Cloud VPN tunnel or Cloud Interconnect connection. After you block internet access, VM instances cannot call third-party APIs and services.

For more information about working with VPC firewall rules, see [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls) in the Cloud Next Generation Firewall documentation.

Configure your on-premises firewall rules to let traffic from your on-premises hosts reach the `restricted.googleapis.com` IP address ranges.

  * For IPv4 traffic: `199.36.153.4/30`
  * For IPv6 traffic: `2600:2d00:0002:1000::/56`



Direct connectivity to Google APIs and services is not supported from on-premises networks.

## Configure DNS

You can use managed private zones for your VPC networks. Cloud DNS private DNS zones enable you to host a DNS zone accessible from authorized VPC networks. To configure forwarding from certain on-premises name servers, you can use the `restricted.googleapis.com` IP address ranges. You can then create a private zone for `googleapis.com` with a DNS A record that maps `restricted.googleapis.com` and appropriate CNAME records for each `*.googleapis.com` name. For more information, see [Managing zones](https://docs.cloud.google.com/dns/zones).

For on-premises access, you can configure a Cloud DNS inbound forwarding policy to enable on-premises name servers to query a Cloud DNS managed private zone. You can also configure an on-premises name server, such as one using [BIND](https://www.wikipedia.org/wiki/BIND):

**Note:** We suggest that you use BIND only for on-premises implementations.

### Configure DNS with Cloud DNS

To enable DNS resolution for VM instances in your VPC network, hosts in an on-premises network, or both, use Cloud DNS. If you're using Shared VPC, see [Private zones and Shared VPC](https://docs.cloud.google.com/dns/docs/overview#shared-vpc) in the Cloud DNS documentation. Also, if you're using Shared VPC, we recommend that you include the Shared VPC network host project in the same service perimeter as projects that connect to the network.

#### Configure Cloud DNS by using private zones

You can use private zones to configure Cloud DNS:

  1. Create a managed private zone for your VPC network.
         
         gcloud dns managed-zones create ZONE_NAME \
          --visibility=private \
          --networks=https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME \
          --description=DESCRIPTION \
          --dns-name=googleapis.com

Replace the following:

     * `ZONE_NAME`: a name for the zone that you are creating. For example, `vpc`. This name is used in each of the following steps.
     * `PROJECT_ID`: the ID of the project that hosts your VPC network.
     * `NETWORK_NAME`: the name of your VPC network.
     * `DESCRIPTION`: an optional, human-readable description of the managed zone.
  2. Start a transaction.
         
         gcloud dns record-sets transaction start --zone=ZONE_NAME

Replace `ZONE_NAME` with the name of the zone that you created in the first step.

  3. Add DNS records.
         
         gcloud dns record-sets transaction add --name=*.googleapis.com. \
             --type=CNAME restricted.googleapis.com. \
             --zone=ZONE_NAME \
             --ttl=300

Replace `ZONE_NAME` with the name of the zone that you created in the first step.
         
         gcloud dns record-sets transaction add --name=restricted.googleapis.com. \
             --type=A 199.36.153.4 199.36.153.5 199.36.153.6 199.36.153.7 \
             --zone=ZONE_NAME \
             --ttl=300

Replace `ZONE_NAME` with the name of the zone that you created in the first step.

If you're configuring the IPv6 addresses for `restricted.googleapis.com`, also create the following record set:
         
         gcloud dns record-sets transaction add --name=restricted.googleapis.com. \
             --type=AAAA 2600:2d00:0002:1000:: \
             --zone=ZONE_NAME \
             --ttl=300

  4. Execute the transaction.
         
         gcloud dns record-sets transaction execute --zone=ZONE_NAME

Replace `ZONE_NAME` with the name of the zone that you created in the first step.

  5. Optional. To enable on-premises hosts to reach the restricted VIP, complete the following steps:

     1. Create a DNS policy and enable inbound DNS forwarding to make VPC network's name resolution services externally available to systems in on-premises networks,
            
            gcloud dns policies create POLICY_NAME \
             --networks=https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME \
             --enable-inbound-forwarding \
             --description=DESCRIPTION

Replace the following:

        * `POLICY_NAME`: a name for the policy that you are creating. For example, `apipolicy`.
        * `PROJECT_ID`: the ID of the project that hosts your VPC network.
        * `NETWORK_NAME`: the name of your VPC network.
        * `DESCRIPTION`: an optional, human-readable description of the managed zone.
     2. In your on-premises network, point your on-premises DNS to the Cloud DNS forwarder IP address. To find the forwarder IP address, use the `compute addresses list` command:
            
            gcloud compute addresses list --filter='name ~ ^dns-forwarding.*' \
             --format='csv[no-heading](address, subnetwork)'

**Note:** Your VPC network only has a forwarder IP address if you have configured an inbound DNS forwarding policy for it. For more information about DNS policies, see the [Cloud DNS server policies overview](https://docs.cloud.google.com/dns/docs/server-policies-overview) and [Creating an inbound server policy](https://docs.cloud.google.com/dns/docs/policies#create-in).



### Configure DNS with BIND

If you use [BIND](https://www.wikipedia.org/wiki/BIND) for DNS resolution, you can configure it to resolve Google API requests to the restricted Google APIs. Use the following example BIND configuration, which makes use of [response policy zones](https://wikipedia.org/wiki/Response_policy_zone) (RPZ) to achieve this behavior:

  1. Add the following lines to `/etc/bind/named.conf`:
         
         include "/etc/bind/named.conf.options";
         include "/etc/bind/named.conf.local";
         

  2. Add the following lines to `/etc/bind/named.conf.options`:
         
         options {
           directory "/var/cache/bind";
         
           dnssec-validation no;
         
           auth-nxdomain no;    # conform to RFC 1035
           listen-on-v6 { any; };
           listen-on { any; };
           response-policy { zone "googleapis.zone"; };
           allow-query { any;};
         };
         

  3. Add the following lines to `/etc/bind/named.conf.local`: 
         
         include "/etc/bind/named.conf.default-zones";
         
         
         
         zone "googleapis.zone" {
           type master;
           file "/etc/bind/db.googleapis.zone";
           allow-query {none;};
         };
         

  4. Add the following lines to `/etc/bind/db.googleapis.zone`: 
         
         $TTL 1H
         @                       SOA LOCALHOST. noreply.localhost(1 1h 15m 30d 2h)
                                 NS  LOCALHOST.
         
         
         
         *.googleapis.com CNAME restricted.googleapis.com.
         restricted.googleapis.com CNAME rpz-passthru.
         




### Configure DNS in special cases

When you need to configure DNS in special cases, keep the following in mind:

  * Custom BIND is not supported when using Dataflow. To customize DNS resolution when using Dataflow with VPC Service Controls, use Cloud DNS [private zones](https://docs.cloud.google.com/dns/docs/overview#dns-private-zones) instead of using custom BIND servers. To use your own on-premises DNS resolution, consider using a Google Cloud [DNS forwarding method](https://docs.cloud.google.com/dns/docs/overview#dns-forwarding-methods).
  * You might need to also configure DNS for `gcr.io` if, for example, you're using Google Kubernetes Engine (GKE). For more information, see [Setting up Container Registry for GKE private clusters](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-gke#configure-dns).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
  *[VPC]: Virtual Private Cloud
