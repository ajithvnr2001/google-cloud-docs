---
url: https://docs.cloud.google.com/vpc/docs/access-apis-external-ip/
title: Access APIs from VMs with external IP addresses \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:34:54.504035+00:00
---

# Access APIs from VMs with external IP addresses  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/access-apis-external-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access APIs from VMs with external IP addresses

A virtual machine (VM) instance with an [external IP address assigned to its network interface](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address) can connect to Google APIs and services if the network requirements described on this page are met. Though the connection is made from the VM's external IP address, the traffic stays within Google Cloud and is not sent through the public internet.

## Network requirements

You must meet the following requirements to access Google APIs and services from a VM with an external IP address:

  * If needed, you enable the API for the services that you want to access:

    * If you're accessing a Google API service endpoint, you must [enable the API](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for that service.

For example, to create a Cloud Storage bucket through the storage.googleapis.com API service endpoint or a client library, you must enable the Cloud Storage API.

    * If you're accessing other types of resources, you might not need to enable any APIs.

For example, to access a Cloud Storage bucket in another project through its storage.googleapis.com URL, you don't need to enable the Cloud Storage API.



  * If you want to connect to Google APIs and services using IPv6, you must meet both of these requirements:

    * Your VM must be [configured with an external `/96` IPv6 address range](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address).

    * The software running on the VM must send packets whose sources match one of those IPv6 addresses from that range.




  * Depending on your chosen configuration, you might need to update DNS entries, routes, and firewall rules. For more information, see Summary of configuration options.



## Summary of configuration options

The following table summarizes the different ways that a VM with an external IP address can access APIs and services that are hosted in Google's production infrastructure. For more detailed configuration information, see Network configuration.

**Note:** Some Google APIs and services offer direct connectivity from Compute Engine virtual machine (VM) instances, bypassing Google Front Ends (GFEs). To allow this traffic, you must ensure that your routes and firewall rules allow egress traffic to reach `34.126.0.0/18` and `2001:4860:8040::/42`. You don't need to create DNS records for these addresses. Services that offer direct connectivity support VPC Service Controls.

Domain option | DNS configuration | Routing configuration | Firewall configuration  
---|---|---|---  
Default domains | You access Google APIs and services through their public IP addresses, so no special DNS configuration is required. | Ensure that your VPC network can route traffic to the IP address ranges that are used by Google APIs and services.

  * Basic configuration: Confirm that you have default routes with next hop `default-internet-gateway` and a destination range of `0.0.0.0/0` (for IPv4 traffic) and `::/0` (for IPv6 traffic, if needed). Create those routes if they are missing.
  * Custom configuration: Create routes for the IP address ranges used by Google APIs and services.

|  Ensure that your firewall rules allow egress to the IP address ranges used by Google APIs and services. The default allow egress firewall rule allows this traffic, if there is no higher priority rule that blocks it.  
`private.googleapis.com` |  Configure DNS records in a private DNS zone to send requests to the following IP addresses: For IPv4 traffic:

  * `199.36.153.8/30`

For IPv6 traffic:

  * `2600:2d00:0002:2000::/56`

|  Ensure that your VPC network has routes to the following IP ranges: For IPv4 traffic:

  * `199.36.153.8/30`
  * `34.126.0.0/18`

For IPv6 traffic:

  * `2600:2d00:0002:2000::/56`
  * `2001:4860:8040::/42`

|  Ensure that your firewall rules allow egress to the following IP ranges: For IPv4 traffic:

  * `199.36.153.8/30`
  * `34.126.0.0/18`

For IPv6 traffic:

  * `2600:2d00:0002:2000::/56`
  * `2001:4860:8040::/42`

  
`restricted.googleapis.com` |  Configure DNS records to send requests to the following IP addresses: For IPv4 traffic:

  * `199.36.153.4/30`

For IPv6 traffic:

  * `2600:2d00:0002:1000::/56 `

|  Ensure that your VPC network has routes to the following IP ranges: For IPv4 traffic:

  * `199.36.153.4/30`
  * `34.126.0.0/18`

For IPv6 traffic:

  * `2600:2d00:0002:1000::/56 `
  * `2001:4860:8040::/42`

|  Ensure that your firewall rules allow egress to the following IP ranges: For IPv4 traffic:

  * `199.36.153.4/30`
  * `34.126.0.0/18`

For IPv6 traffic:

  * `2600:2d00:0002:1000::/56`
  * `2001:4860:8040::/42`

  
  
## Network configuration

This section describes the basic network requirements you must meet in order for a VM in your VPC network to access Google APIs and services.

### Domain options

Choose the domain that you want to use to access Google APIs and services.

The `private.googleapis.com` and `restricted.googleapis.com` virtual IP addresses (VIPs) support only HTTP-based protocols over TCP (HTTP, HTTPS, and HTTP/2). All other protocols, including MQTT and ICMP, are not supported. Interactive websites and features that use the internet—for example, for redirects or retrieving content—are not supported. 

Domain and IP address ranges | Supported services | Example usage  
---|---|---  
Default domains. All domain names for Google APIs and services _except for_ `private.googleapis.com` and `restricted.googleapis.com`. Various IP address ranges—you can determine a set of IP ranges that contains the possible addresses used by the default domains by referencing [IP addresses for default domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults). | Enables API access to most Google APIs and services regardless of whether they are supported by VPC Service Controls. Includes API access to Google Maps, Google Ads, and Google Cloud. Includes Google Workspace web applications such as Gmail and Google Docs, and other web applications.  | The default domains are used when you don't configure DNS records for `private.googleapis.com` and `restricted.googleapis.com`.  
`private.googleapis.com` `199.36.153.8/30` `2600:2d00:0002:2000::/56` | Enables API access to most Google APIs and services regardless of whether they are supported by VPC Service Controls. Includes API access to Google Maps, Google Ads, Google Cloud, and most other Google APIs, including the following list. Does not support Google Workspace web applications such as Gmail and Google Docs.  Domain names that match: 

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

| Use `private.googleapis.com` to access Google APIs and services by using a set of IP addresses only routable from within Google Cloud. Choose `private.googleapis.com` under these circumstances: 

  * You don't use VPC Service Controls.
  * You do use VPC Service Controls, but you also need to access Google APIs and services that are not supported by VPC Service Controls.1

  
`restricted.googleapis.com` `199.36.153.4/30` `2600:2d00:0002:1000::/56` | Enables API access to [Google APIs and services that are supported by VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products). Blocks access to Google APIs and services that do not support [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). Does not support Google Workspace APIs or Google Workspace web applications such as Gmail and Google Docs.  | Use `restricted.googleapis.com` to access Google APIs and services by using a set of IP addresses only routable from within Google Cloud. Choose `restricted.googleapis.com` when you _only_ need access to Google APIs and services that _are_ supported by VPC Service Controls. The `restricted.googleapis.com` domain does not permit access to Google APIs and services that do not support VPC Service Controls.1  
  
1 If you need to restrict users to just the Google APIs and services that support [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs), use `restricted.googleapis.com`, as it provides additional risk mitigation for data exfiltration. Using `restricted.googleapis.com` denies access to Google APIs and services that are not supported by VPC Service Controls. See [Setting up private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity) in the VPC Service Controls documentation for more details. 

### IPv6 support for `private.googleapis.com` and `restricted.googleapis.com`

The following IPv6 address ranges can be used to direct traffic from IPv6 clients to Google APIs and services:

  * `private.googleapis.com`: `2600:2d00:0002:2000::/56`
  * `restricted.googleapis.com`: `2600:2d00:0002:1000::/56`



Consider configuring the IPv6 addresses if you want to use the `private.googleapis.com` or `restricted.googleapis.com` domain, and you have clients that use IPv6 addresses. IPv6 clients that also have IPv4 addresses configured can reach Google APIs and services by using the IPv4 addresses. Not all services accept traffic from IPv6 clients.

### DNS configuration

For connectivity to Google APIs and services, you can choose to send packets to the IP addresses associated with the `private.googleapis.com` or `restricted.googleapis.com` VIP. To use a VIP, you must configure DNS so that VMs in your VPC network reach services by using the VIP addresses instead of the public IP addresses.

The following sections describe how to use DNS zones to send packets to the IP addresses that are associated with your chosen VIP. Follow the instructions for all scenarios that apply to you:

  * If you use services that have `googleapis.com` domain names, see Configure DNS for `googleapis.com`.
  * If you use services that have other domain names, see Configure DNS for other domains. For example, if you use Google Kubernetes Engine (GKE), you also need to configure `*.gcr.io` and `*.pkg.dev`, or if you use Cloud Run, you need to configure `*.run.app`.

  * If you use Cloud Storage buckets, and you send requests to a Cloud Storage custom domain name, see Configure DNS for Cloud Storage custom domain names. 




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

### Routing options

Your VPC network must have appropriate routes whose next hops are the default internet gateway. Google Cloud does not support routing traffic to Google APIs and services through other VM instances or custom next hops. Despite being called _default internet gateway_ , packets sent from VMs in your VPC network to Google APIs and services remain within Google's network.

  * If you select the default domains, your VM instances connect to Google APIs and services using a subset of Google's external IP addresses. These IP addresses are publicly routable, but the path from a VM in a VPC network to those addresses remains within Google's network.

  * Google doesn't publish routes on the internet to any of the IP addresses used by either the `private.googleapis.com` or `restricted.googleapis.com` domains. Consequently, these domains can only be accessed by VMs in a VPC network or on-premises systems connected to a VPC network.




If your VPC network contains a [default route](https://docs.cloud.google.com/vpc/docs/vpc#routingpacketsinternet) whose next hop is the default internet gateway, you can use that route to access Google APIs and services, without needing to create custom routes. See routing with a default route for details.

If you have replaced a default route (destination `0.0.0.0/0` or `::0/0`) with a custom route whose next hop is _not_ the default internet gateway, you can meet the routing requirements for Google APIs and services using custom routing instead.

If your VPC network does not have an IPv6 default route, you won't have IPv6 connectivity to Google APIs and services. [Add an IPv6 default route](https://docs.cloud.google.com/vpc/docs/using-routes#addingroute-ipv6) to allow IPv6 connectivity.

### Routing with a default route

Each VPC network contains an IPv4 default route (`0.0.0.0/0`) when it is created. If you enable external IPv6 addresses on a subnet, a system-generated IPv6 default route (`::/0`) is added to that VPC network.

The default routes provide a path to the IP addresses for the following destinations:

  * The default domains.

  * `private.googleapis.com`: `199.36.153.8/30` and `2600:2d00:0002:2000::/56`.

  * `restricted.googleapis.com`: `199.36.153.4/30` and `2600:2d00:0002:1000::/56`.




To check the configuration of a default route in a given network, follow these directions.

###  Console 

  1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Filter the list of routes to show just the routes for the network you need to inspect.

  3. Look for a route whose destination is `0.0.0.0/0` for IPv4 traffic or `::/0` for IPv6 traffic and whose next hop is _default internet gateway_.




###  gcloud 

Use the following `gcloud` command, replacing `NETWORK_NAME` with the name of the network to inspect:
    
    
    gcloud compute routes list \
        --filter="default-internet-gateway NETWORK_NAME"
    

If you need to create a replacement default IPv4 route, see [Adding a static route](https://docs.cloud.google.com/vpc/docs/using-routes#addingroute).

If you need to create a replacement default IPv6 route, see [Adding an IPv6 default route](https://docs.cloud.google.com/vpc/docs/using-routes#addingroute-ipv6). 

### Custom routing

As an alternative to a default route, you can use custom static routes, each having a more specific destination, and each using the default internet gateway next hop. The number of routes you need and their destination IP addresses depend on the domain that you choose.

  * Default domains: you must have routes for the IP address ranges for Google APIs and services.
  * `private.googleapis.com`: `199.36.153.8/30` and `2600:2d00:0002:2000::/56`
  * `restricted.googleapis.com`: `199.36.153.4/30` and `2600:2d00:0002:1000::/56`



Additionally, we recommend that you add routes for `34.126.0.0/18` and `2001:4860:8040::/42`. For more information, see Summary of configuration options.

To check the configuration of custom routes for Google APIs and services in a given network, follow these directions.

###  Console 

  1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Use the _Filter table_ text field to filter the list of routes using the following criteria, replacing `NETWORK_NAME` with the name of your VPC network.

     * Network: `NETWORK_NAME`
     * Next hop type: `default internet gateway`
  3. Look at the _Destination IP range_ column for each route. If you chose the default domains, check for several custom static routes, one for each IP address range used by the default domain. If you chose `private.googleapis.com` or `restricted.googleapis.com`, look for that domain's IP range.




###  gcloud 

Use the following `gcloud` command, replacing `NETWORK_NAME` with the name of the network to inspect:
    
    
    gcloud compute routes list \
        --filter="default-internet-gateway NETWORK_NAME"
    

Routes are listed in table format unless you customize the command with the `--format` flag. Look in the `DEST_RANGE` column for the destination of each route. If you chose the default domains, check for several custom static routes, one for each IP address range used by the default domain. If you chose `private.googleapis.com` or `restricted.googleapis.com`, look for that domain's IP range.

If you need to create routes, see [Adding a static route](https://docs.cloud.google.com/vpc/docs/using-routes#addingroute). 

### Firewall configuration

The firewall configuration of your VPC network must allow access from VMs to the IP addresses used by Google APIs and services. The implied `allow egress` rule satisfies this requirement.

In some firewall configurations, you need to create specific egress allow rules. For example, suppose you've created an egress deny rule that blocks traffic to all destinations (`0.0.0.0` for IPv4 or `::/0` for IPv6). In that case, you must create one egress allow firewall rule whose priority is higher than the egress deny rule for each IP address range used by your chosen domain for Google APIs and services.

  * Default domains: all IP address ranges for Google APIs and services.
  * `private.googleapis.com`: `199.36.153.8/30` and `2600:2d00:0002:2000::/56`
  * `restricted.googleapis.com`: `199.36.153.4/30` and `2600:2d00:0002:1000::/56`



Additionally, we recommend that you include `34.126.0.0/18` and `2001:4860:8040::/42` in your egress allow firewall rule. For more information, see Summary of configuration options.

To create firewall rules, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules). You can limit the VMs to which the firewall rules apply when you define [the target](https://docs.cloud.google.com/vpc/docs/firewalls#rule_assignment) of each egress allow rule. 

### IP addresses for default domains

This section describes how to create a list of default domain IP ranges used by Google APIs and services. These ranges are allocated dynamically and change often, so it's not possible to define specific IP ranges for individual services or APIs. To maintain an accurate list, set up automation to run the script every day.

If you have strict egress requirements, don't use the IP addresses for the default domains. Use a [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis), or the private.googleapis.com or restricted.googleapis.com VIP. These options require additional DNS configuration, but don't require that you maintain a list of IP address ranges.

Follow these steps to determine the IP address ranges used by the default domains, such as `*.googleapis.com`.

  * Google publishes a list of Google-owned IP addresses in [goog.json](https://www.gstatic.com/ipranges/goog.json).

  * Google also publishes a list of global and regional external IP addresses ranges available for customers' Google Cloud resources in [cloud.json](https://www.gstatic.com/ipranges/cloud.json).




Taking away all ranges in `cloud.json` from those in `goog.json` results in a large set of IP addresses that are used by global Google APIs and other Google services, including customer-facing products outside of Google Cloud. These lists are updated frequently.

You can use the following Python script to create a list of IP address ranges that include those used by the default domains for Google APIs and services.

For information about running this script, see [How to run](https://github.com/GoogleCloudPlatform/networking-tools-python/tree/main/tools/cidr#how-to-run).
    
    
    from __future__ import print_function
    
    import json
    
    try:
        from urllib import urlopen
    except ImportError:
        from urllib.request import urlopen
        from urllib.error import HTTPError
    
    import netaddr
    
    IPRANGE_URLS = {
        "goog": "https://www.gstatic.com/ipranges/goog.json",
        "cloud": "https://www.gstatic.com/ipranges/cloud.json",
    }
    
    
    def read_url(url):
        try:
            return json.loads(urlopen(url).read())
        except (IOError, HTTPError):
            print("ERROR: Invalid HTTP response from %s" % url)
        except json.decoder.JSONDecodeError:
            print("ERROR: Could not parse HTTP response from %s" % url)
    
    
    def get_data(link):
        data = read_url(link)
        if data:
            print("{} published: {}".format(link, data.get("creationTime")))
            cidrs = netaddr.IPSet()
            for e in data["prefixes"]:
                if "ipv4Prefix" in e:
                    cidrs.add(e.get("ipv4Prefix"))
                if "ipv6Prefix" in e:
                    cidrs.add(e.get("ipv6Prefix"))
            return cidrs
    
    
    def main():
        cidrs = {group: get_data(link) for group, link in IPRANGE_URLS.items()}
        if len(cidrs) != 2:
            raise ValueError("ERROR: Could process data from Google")
        print("IP ranges for Google APIs and services default domains:")
        for ip in (cidrs["goog"] - cidrs["cloud"]).iter_cidrs():
            print(ip)
    
    
    if __name__ == "__main__":
        main()

**Note:** In the past, Google Cloud published a list of IP address ranges in the `_spf.google.com` DNS TXT record (and the records it referenced). While this DNS TXT record continues to be accurate for [SPF purposes](https://support.google.com/a/answer/33786), it does not contain the complete set of possible IP address ranges used by the default domains for Google APIs and services.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
