---
url: https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid/
title: Configure Private Google Access for on-premises hosts \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:51.707443+00:00
---

# Configure Private Google Access for on-premises hosts  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Private Google Access for on-premises hosts

Private Google Access for on-premises hosts provides a way for on-premises systems to connect to [Google APIs and services](https://developers.google.com/apis-explorer/) by routing traffic through a [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) tunnel or a VLAN attachment for [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect). Private Google Access for on-premises hosts is an alternative to connecting to Google APIs and services over the internet.

This document describes how to enable Private Google Access for on-premises hosts.

**Note:** These instructions also apply to host machines in a [Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs) region extension. Except in reference to name servers in the DNS configuration section, the term _on-premises_ in these instructions is equivalent to _Bare Metal Solution_. For DNS name servers, the DNS name server that you use can be your own enterprise server in your actual on-premises environment, a DNS name server on Google Cloud, or, if you enable your Bare Metal Solution machines to connect to the internet, a public DNS name server.

## Specifications and requirements

Private Google Access for on-premises hosts has the following requirements:

  * You must direct Google APIs and services traffic sent by on-premises systems to the IP addresses associated with either the `private.googleapis.com` or the `restricted.googleapis.com` special domain names. For details about what services can be accessed on each domain, see Domain options.

  * Your on-premises network must be connected to a [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) by using either Cloud VPN tunnels or VLAN attachments.

  * The VPC network to which your on-premises network is connected must have appropriate routes for either the `private.googleapis.com` or `restricted.googleapis.com` destination IP ranges. For details, see VPC network routing.

  * The VPC network to which your on-premises network is connected must have appropriate routes to reach the on-premises network. The next hop Cloud VPN tunnels or VLAN attachments that connect to your on-premises network for these routes must be within the same region where the request originated. If the next hop is in a region different from where the request to Private Google Access originated, response from Private Google Access will not reach the on-premises network.

  * Your on-premises network must have routes for either the `private.googleapis.com` or `restricted.googleapis.com` destination IP ranges. These routes must direct traffic to the appropriate Cloud VPN tunnel or VLAN attachment that connects to your VPC network. For details, see on-premises routing with Cloud Router.

  * To let IPv6 clients in your on-premises environment access Google APIs by using `private.googleapis.com` or `restricted.googleapis.com`, you must configure the connection to your VPC network to support IPv6. For more information, see the following pages: 

    * [IPv6 support for HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ipv6_support)
    * [IP protocols support for Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#ip-protocols)
  * On-premises clients can send requests from any IPv6 GUA or ULA addresses, except for the ULA range `fda3:e722:ac3:cc00::/64`, which is reserved for internal use. 

  * If your project is providing access to Google APIs for on-premises hosts only, you don't need to enable the Google APIs for the project.

However, if resources within the project need to access Google APIs, you might need to separately [enable the APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for the services that they need to access. For more information about using Private Google Access for resources within a project, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).




### Permissions

Project owners, editors, and IAM principals with the [Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) role can create or update subnets and assign IP addresses.

For more information about roles, read the [IAM roles](https://docs.cloud.google.com/compute/docs/access/iam) documentation.

## Network configuration

Private Google Access for on-premises hosts has specific network requirements for on-premises systems and for the VPC network through which the on-premises systems send traffic to Google APIs and services.

### Domain options

Private Google Access for on-premises hosts requires that you direct services to one of the following special domains. The special domain you choose determines which services you can access.

The `private.googleapis.com` and `restricted.googleapis.com` VIPs support only HTTP-based protocols over TCP (HTTP, HTTPS, and HTTP/2). All other protocols, including MQTT and ICMP, are not supported.

Domain and IP address ranges | Supported services | Example usage  
---|---|---  
`private.googleapis.com` `199.36.153.8/30` `2600:2d00:0002:2000::/56` | Enables API access to most Google APIs and services regardless of whether they are supported by VPC Service Controls. Includes API access to Google Maps, Google Ads, Google Cloud, and most other Google APIs, including the following list. Does not support Google Workspace web applications such as Gmail and Google Docs. Does not support any interactive websites.  Domain names that match: 

  * `accounts.google.com` (only supports paths needed for OAuth authentication of service accounts; user account authentication is interactive and not supported)
  * `*.aiplatform-notebook.cloud.google.com`
  * `*.aiplatform-notebook.googleusercontent.com`
  * `appengine.google.com`
  * `*.appspot.com`
  * `*.backupdr.cloud.google.com`
  * `backupdr.cloud.google.com`
  * `*.backupdr.googleusercontent.com`
  * `backupdr.googleusercontent.com`
  * `*.cloudfunctions.net`
  * `*.cloudproxy.app`
  * `*.composer.cloud.google.com`
  * `*.composer.googleusercontent.com`
  * `*.datafusion.cloud.google.com`
  * `*.datafusion.googleusercontent.com`
  * `*.dataproc.cloud.google.com`
  * `dataproc.cloud.google.com`
  * `*.dataproc.googleusercontent.com`
  * `dataproc.googleusercontent.com`
  * `*.developerconnect.dev`
  * `dl.google.com`
  * `gcr.io` or `*.gcr.io`
  * `*.googleapis.com`Excludes `*.rep.googleapis.com` [regional and multi-regional endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints).
  * `*.gke.goog`
  * `gstatic.com` or `*.gstatic.com`
  * `*.kernels.googleusercontent.com`
  * `*.ltsapis.goog`
  * `*.notebooks.byoid.googleusercontent.com`
  * `*.notebooks.cloud.google.com`
  * `notebooks.cloud.google.com`
  * `*.notebooks.googleusercontent.com`
  * `packages.cloud.google.com`
  * `pkg.dev` or `*.pkg.dev`
  * `pki.goog` or `*.pki.goog`
  * `*.run.app`
  * `source.developers.google.com`
  * `storage.cloud.google.com`

| Use `private.googleapis.com` to access Google APIs and services using a set of IP addresses only routable from within Google Cloud. Choose `private.googleapis.com` under these circumstances: 

  * You don't use VPC Service Controls.
  * You do use VPC Service Controls, but you also need to access Google APIs and services that are not supported by VPC Service Controls. 1

  
`restricted.googleapis.com` `199.36.153.4/30` `2600:2d00:0002:1000::/56` | Enables API access to [Google APIs and services that are supported by VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products). Blocks access to Google APIs and services that do not support [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). Does not support Google Workspace APIs or Google Workspace web applications such as Gmail and Google Docs.  | Use `restricted.googleapis.com` to access Google APIs and services using a set of IP addresses only routable from within Google Cloud. Choose `restricted.googleapis.com` when you _only_ need access to Google APIs and services that _are_ supported by VPC Service Controls. The `restricted.googleapis.com` domain does not permit access to Google APIs and services that do not support VPC Service Controls. 1  
  
1 If you need to restrict users to just the Google APIs and services that support [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs), use `restricted.googleapis.com`, as it provides additional risk mitigation for data exfiltration. Using `restricted.googleapis.com` denies access to Google APIs and services that are not supported by VPC Service Controls. See [Setting up private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity) in the VPC Service Controls documentation for more details. 

### IPv6 support for `private.googleapis.com` and `restricted.googleapis.com`

The following IPv6 address ranges can be used to direct traffic from IPv6 clients to Google APIs and services:

  * `private.googleapis.com`: `2600:2d00:0002:2000::/56`
  * `restricted.googleapis.com`: `2600:2d00:0002:1000::/56`



Consider configuring the IPv6 addresses if you want to use the `private.googleapis.com` or `restricted.googleapis.com` domain, and you have clients that use IPv6 addresses. IPv6 clients that also have IPv4 addresses configured can reach Google APIs and services by using the IPv4 addresses. Not all services accept traffic from IPv6 clients.

### DNS configuration

Your on-premises network must have DNS zones and records configured so that the domain names of the services that you're accessing resolve to the set of IP addresses for either `private.googleapis.com` or `restricted.googleapis.com`. You can create Cloud DNS managed private zones and use a Cloud DNS inbound server policy, or you can configure on-premises name servers. For example, you can use [BIND](https://www.wikipedia.org/wiki/BIND) or [Microsoft Active Directory DNS](https://docs.microsoft.com/en-us/windows-server/networking/dns/dns-top).

The following sections describe how to use DNS zones to send packets to the IP addresses that are associated with your chosen VIP. Follow the instructions for all scenarios that apply to you:

  * If you use services that have `*.googleapis.com` domain names, see Configure DNS for `googleapis.com`.
  * If you use services that have other domain names, see Configure DNS for other domains. For example, if you use Google Kubernetes Engine (GKE), you also need to configure `*.pkg.dev`, or if you use Cloud Run, you need to configure `*.run.app`. 
  * If you use Cloud Storage buckets, and you send requests to a Cloud Storage custom domain name, see Configure DNS for Cloud Storage custom domain names. 

  * If you implement the DNS configuration using Cloud DNS, see Configure DNS for on-premises systems.




When you configure DNS records for the VIPs, use only the IP addresses that are described in the following steps. Do not mix addresses from the `private.googleapis.com` and `restricted.googleapis.com` VIPs. This can cause intermittent failures because the services that are offered differ based on a packet's destination.

**Note:** There are public DNS records for private.googleapis.com or restricted.googleapis.com. However, you can't use the public records to access Google APIs. You must create a private DNS zone and records.

#### Configure DNS for `googleapis.com`

Create a DNS zone and records for `googleapis.com`:

  1. Create a private DNS zone for `googleapis.com`. Consider [creating a Cloud DNS private zone](https://docs.cloud.google.com/dns/zones#create-private-zone) for this purpose.
  2. In the `googleapis.com` zone, create the following private DNS records for _either_ `private.googleapis.com` or `restricted.googleapis.com`, depending on which domain you've chosen to use.

     * For `private.googleapis.com`:

       1. Create an `A` record for `private.googleapis.com` pointing to the following IP addresses: `199.36.153.8`, `199.36.153.9`, `199.36.153.10`, `199.36.153.11`.

       2. To connect to APIs using IPv6 addresses, also configure an `AAAA` record for `private.googleapis.com` pointing to `2600:2d00:0002:2000::`.

     * For `restricted.googleapis.com`:

       1. Create an `A` record for `restricted.googleapis.com` pointing to the following IP addresses: `199.36.153.4`, `199.36.153.5`, `199.36.153.6`, `199.36.153.7`.

       2. To connect to APIs using IPv6 addresses, also create an `AAAA` record for `restricted.googleapis.com` pointing to `2600:2d00:0002:1000::`.

To create private DNS records in Cloud DNS, see [add a record](https://docs.cloud.google.com/dns/docs/records#add_a_record).

  3. In the `googleapis.com` zone, create a `CNAME` record for `*.googleapis.com` that points to the domain that you've configured: `private.googleapis.com` or `restricted.googleapis.com`.




#### Configure DNS for other domains

Some Google APIs and services are provided using additional domain names, including `*.gcr.io`, `*.gstatic.com`, `*.pkg.dev`, `pki.goog`, `*.run.app`, and `*.gke.goog`. Refer to the _domain and IP address ranges table_ in Domain options to determine if the additional domain's services can be accessed using `private.googleapis.com` or `restricted.googleapis.com`. Then, for each of the additional domains:

  1. Create a DNS zone for `DOMAIN` (for example, `gcr.io`). If you're using Cloud DNS, make sure this zone is located in the same project as your `googleapis.com` private zone.

  2. In this DNS zone, create the following private DNS records for _either_ `private.googleapis.com` or `restricted.googleapis.com`, depending on which domain you've chosen to use.

     * For `private.googleapis.com`:

       1. Create an `A` record for `DOMAIN` pointing to the following IP addresses: `199.36.153.8`, `199.36.153.9`, `199.36.153.10`, `199.36.153.11`.

       2. To connect to APIs using IPv6 addresses, also create an `AAAA` record for `DOMAIN` pointing to `2600:2d00:0002:2000::`.

     * For `restricted.googleapis.com`:

       1. Create an `A` record for `DOMAIN` pointing to the following IP addresses: `199.36.153.4`, `199.36.153.5`, `199.36.153.6`, `199.36.153.7`.

       2. To connect to APIs using IPv6 addresses, also create an `AAAA` record for `DOMAIN` pointing to `2600:2d00:0002:1000::`.

  3. In the `DOMAIN` zone, create a `CNAME` record for `*.DOMAIN` that points to `DOMAIN`. For example, create a `CNAME` record for `*.gcr.io` that points to `gcr.io`.




#### Configure DNS for Cloud Storage custom domain names

If you are using Cloud Storage buckets, and you send requests to a [Cloud Storage custom domain name](https://docs.cloud.google.com/storage/docs/domain-name-verification), configuring DNS records for the custom Cloud Storage domain name to point to the IP addresses for `private.googleapis.com` or `restricted.googleapis.com` is not sufficient to allow access to the Cloud Storage buckets.

If you want to send requests to a Cloud Storage custom domain name, you must also explicitly set the HTTP request's Host header and TLS SNI to `storage.googleapis.com` The IP addresses for `private.googleapis.com` and `restricted.googleapis.com` do not support custom Cloud Storage hostnames in HTTP request Host headers and TLS SNIs.

#### Configure DNS for on-premises systems

If you've implemented the DNS configuration using Cloud DNS, you'll need to configure on-premises systems so that they can make queries to your Cloud DNS managed private zones:

  * Create an [inbound server policy](https://docs.cloud.google.com/dns/docs/policies#create-in) in the VPC network to which your on-premises network connects.
  * Identify the [inbound forwarder entry points](https://docs.cloud.google.com/dns/docs/policies#list-in-entrypoints), in the region(s) where your Cloud VPN tunnels and VLAN attachments are located, in the VPC network to which your on-premises network connects.
  * Configure on-premises systems and on-premises DNS name servers to forward `googleapis.com` and any of the additional domain names to an inbound forwarder entry point _in the same region as the Cloud VPN tunnel or VLAN attachment that connects to the VPC network_.



### VPC network routing

The VPC network to which your on-premises network connects must have routes for the IP address ranges used by `private.googleapis.com` or `restricted.googleapis.com`. These routes must use the default internet gateway next hop.

Google Cloud doesn't publish routes on the internet for the IP address ranges used by the `private.googleapis.com` or `restricted.googleapis.com` domains. Consequently, even though the routes in the VPC network send traffic to the _default internet gateway_ next hop, packets sent to those IP address ranges remain within Google's network.

If the VPC network to which your on-premises network connects contains a [default route](https://docs.cloud.google.com/vpc/docs/vpc#routingpacketsinternet) whose next hop is the default internet gateway, that route meets the routing requirements for Private Google Access for on-premises hosts.

#### VPC network custom routing

If you've replaced or changed your default route, ensure that you have custom static routes configured for the destination IP ranges used by `private.googleapis.com` or `restricted.googleapis.com`. To check the configuration of custom routes for Google APIs and services in a given network, follow these directions.

###  Console 

  1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Use the _Filter table_ text field to filter the list of routes using the following criteria, replacing `NETWORK_NAME` with the name of the VPC network to which your on-premises network connects:

     * Network: `NETWORK_NAME`
     * Next hop type: `default internet gateway`
  3. Look at the _Destination IP range_ column for each route. Look for a route whose destination range matches:

     * `199.36.153.8/30` if you chose `private.googleapis.com`
     * `199.36.153.4/30` if you chose `restricted.googleapis.com`



###  gcloud 

Use the following `gcloud` command, replacing `NETWORK_NAME` with the name of the VPC network to which your on-premises network connects:
    
    
    gcloud compute routes list \
        --filter="default-internet-gateway NETWORK_NAME"
    

Routes are listed in table format unless you customize the command with the `--format` flag. Look in the `DEST_RANGE` column for a route whose destination range matches:

  * `199.36.153.8/30` if you chose `private.googleapis.com`
  * `199.36.153.4/30` if you chose `restricted.googleapis.com`



If you need to create routes in your VPC network, see [Adding a static route](https://docs.cloud.google.com/vpc/docs/using-routes#addingroute).

### On-premises routing with Cloud Router

Routes in your on-premises network must be configured to direct traffic for the IP address ranges used by the `private.googleapis.com` or `restricted.googleapis.com` domains to the next hop Cloud VPN tunnels or VLAN attachments that connect to your VPC network.

You can use [Cloud Router Custom Route Advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) to announce routes for the IP ranges used by the `private.googleapis.com` and `restricted.googleapis.com` domains.

IPv6 routes are advertised only in BGP sessions where [IPv6 is enabled](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-ipv6-bgp). 

**Important:** IP address ranges for `private.googleapis.com` and `restricted.googleapis.com` are not routable on the internet.

###  Console 

**To update the route advertisement mode for all BGP sessions on a Cloud Router, except for those BGP sessions that use custom BGP advertisements themselves:**

  1. In the Google Cloud console, go to the **Cloud Router** page.

[Go to Cloud Router](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router that manages BGP sessions for the Cloud VPN tunnels or VLAN attachments that connect your on-premises network to your VPC network.

  3. In the Cloud Router's detail page, select **Edit**.

  4. Expand the **Advertised routes** section.

  5. For the **Routes** , select **Create custom routes**.

  6. If you want to advertise all subnet routes available to the Cloud Router, select **Advertise all subnets visible to the Cloud Router**. This setting replicates the default configuration to your custom configuration.

  7. For each advertised route that you want to add, do the following:

     1. Select **Add custom route**.
     2. For **Source** , select **Custom IP range**.
     3. For **IP address range** , enter one of the ranges that you want to use: 
        * If you use `private.googleapis.com`: 
          * For IPv4 connectivity: `199.36.153.8/30`
          * For IPv6 connectivity: `2600:2d00:0002:2000::/56`
        * If you use `restricted.googleapis.com`: 
          * For IPv4 connectivity: `199.36.153.4/30`
          * For IPv6 connectivity: `2600:2d00:0002:1000::/56`
     4. Click **Done**.
  8. After you're done adding routes, select **Save**.




**To update the route advertisement mode for a particular BGP session:**

  1. In the Google Cloud console, go to the **Cloud Router** page.

[Go to Cloud Router](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router that manages the BGP session for a Cloud VPN tunnel or VLAN attachment that connects your on-premises network to your VPC network.

  3. In the Cloud Router's detail page, select the BGP session to update.

  4. In the BGP session details page, click **Edit**.

  5. For the **Routes** , select **Create custom routes**.

  6. Select **Advertise all subnets visible to the Cloud Router** to advertise all subnet routes available to the Cloud Router if you desire the Cloud Router's default behavior.

  7. For each advertised route that you want to add, do the following:

     1. Select **Add custom route**.
     2. For **Source** , select **Custom IP range**.
     3. For **IP address range** , enter one of the ranges that you want to use: 
        * If you use `private.googleapis.com`: 
          * For IPv4 connectivity: `199.36.153.8/30`
          * For IPv6 connectivity: `2600:2d00:0002:2000::/56`
        * If you use `restricted.googleapis.com`: 
          * For IPv4 connectivity: `199.36.153.4/30`
          * For IPv6 connectivity: `2600:2d00:0002:1000::/56`
     4. Click **Done**.
  8. After you're done adding routes, select **Save**.




###  gcloud 

  1. Identify the name and region of the Cloud Router that manages BGP sessions on the Cloud VPN tunnels or VLAN attachments that connect your on-premises network to your VPC network.

  2. Use [`compute routers update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update) to update the route advertisement mode on all the Cloud Router's BGP sessions, except for those BGP sessions that use custom BGP advertisements themselves:
         
         gcloud compute routers update ROUTER_NAME \
             --region=REGION \
             --advertisement-mode=CUSTOM \
             --set-advertisement-groups=ALL_SUBNETS \
             --set-advertisement-ranges=CUSTOM_RANGES
         

You can append new advertisement ranges if you're already using the `CUSTOM` advertisement mode for the Cloud Router. This updates the route advertisement mode on all the Cloud Router's BGP sessions, except for those BGP sessions that use custom BGP advertisements themselves:
         
         gcloud compute routers update ROUTER_NAME \
             --region=REGION \
             --add-advertisement-ranges=CUSTOM_RANGES
         

  3. Alternatively, use [`compute routers update-bgp-peer`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer) to configure a specific BGP peer on the Cloud Router:

If you are adding IPv6 custom ranges, and if IPv6 traffic is disabled for the BGP session, you can enable it with the `--enable-ipv6` flag. 
         
         gcloud compute routers update-bgp-peer ROUTER_NAME \
             --region=REGION \
             --peer-name=PEER_NAME \
             --advertisement-mode=CUSTOM \
             --set-advertisement-groups=ALL_SUBNETS \
             --set-advertisement-ranges=CUSTOM_RANGES
         

You can append new advertisement ranges if you're already using the `CUSTOM` advertisement mode for a BGP session on a Cloud Router

If you are adding IPv6 custom ranges, and if IPv6 traffic is disabled for the BGP session, you can enable it with the `--enable-ipv6` flag. 
         
         gcloud compute routers update-bgp-peer ROUTER_NAME \
             --region=REGION \
             --peer-name=PEER_NAME \
             --add-advertisement-ranges=CUSTOM_RANGES
         

In the commands above, replace the following with valid values:

     * `ROUTER_NAME`: The name of the Cloud Router
     * `REGION`: The region of the Cloud Router
     * `PEER_NAME`: The name of the BGP peer configured when you [create a VLAN attachment for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments), when you [create a VLAN attachment for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments), or when you [create an HA VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn)
     * Leave `--set-advertisement-groups=ALL_SUBNETS` in order to advertise all subnet routes available to the Cloud Router. This is the Cloud Router's default behavior.
     * `CUSTOM_RANGES`: A comma-delimited list of custom ranges to advertise. 
       * For `private.googleapis.com`: 
         * For IPv4 connectivity: `199.36.153.8/30`
         * For both IPv4 and IPv6 connectivity: `199.36.153.8/30,2600:2d00:0002:2000::/56`
       * For `restricted.googleapis.com`: 
         * For IPv4 connectivity: `199.36.153.4/30`
         * For both IPv4 and IPv6 connectivity: `199.36.153.4/30,2600:2d00:0002:1000::/56`



### Firewall considerations

Google Cloud firewall rules in the VPC network to which your on-premises network connects have no effect upon:

  * Packets sent through a Cloud VPN tunnel connected to the VPC network
  * Packets sent through a VLAN attachment connected to the VPC network
  * Incoming packets to Cloud DNS inbound forwarder IP addresses in the VPC network



You should ensure that the firewall configuration of on-premises systems allows outbound traffic to and established responses from the appropriate IP addresses:

  * If you use `private.googleapis.com`: 
    * For IPv4 connectivity: `199.36.153.8/30`
    * For IPv6 connectivity: `2600:2d00:0002:2000::/56`
  * If you use `restricted.googleapis.com`: 
    * For IPv4 connectivity: `199.36.153.4/30`
    * For IPv6 connectivity: `2600:2d00:0002:1000::/56`
  * Any Cloud DNS inbound forwarder IP addresses, if you're using Cloud DNS for the DNS configuration



## What's next

  * If you need VMs in your Google Cloud VPC network to access Google APIs and services, see [Configure Private Google Access for VPC](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
