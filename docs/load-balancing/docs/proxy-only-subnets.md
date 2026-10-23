---
url: https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets/
title: Proxy-only subnets for Envoy-based load balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:56.850871+00:00
---

# Proxy-only subnets for Envoy-based load balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Proxy-only subnets for Envoy-based load balancers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to work with proxy-only subnets used by Envoy-based load balancers. A proxy-only subnet provides a pool of IP addresses that are reserved exclusively for Envoy proxies used by Google Cloud load balancers. It can't be used for any other purposes.

The proxies terminate incoming connections and then evaluate where each request should go based on the URL map, the backend service's session affinity, the balancing mode of each backend instance group or NEG, and other factors.

  1. A client makes a connection to the IP address and port of the load balancer's forwarding rule.

  2. Each proxy listens on the IP address and port specified by the corresponding load balancer's forwarding rule. One of the proxies receives and terminates the client's network connection.

  3. The proxy establishes a connection to the appropriate backend VM or endpoint in a NEG, as determined by the load balancer's URL map and backend services.




Each of the load balancer's proxies is assigned an internal IP address. Packets sent from a proxy to a backend VM or endpoint has a source IP address from the proxy-only subnet.

The proxy-only subnet can't be used for any other purpose. The IP address for the load balancer's forwarding rule doesn't come from the proxy-only subnet. Also, the IP addresses of the backend VMs and endpoints don't come from the proxy-only subnet.

## Supported load balancers and products

Envoy-based Cloud Load Balancing and Secure Web Proxy products require proxy-only subnets:

  * Proxy-only subnet with purpose **`GLOBAL_MANAGED_PROXY`** : In a given VPC network and region, only a single proxy-only subnet with purpose `GLOBAL_MANAGED_PROXY` can be active at any point in time. The active proxy-only subnet powers all of the following products:

    * [Cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
    * [Cross-region internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)


  * Proxy-only subnet with purpose **`REGIONAL_MANAGED_PROXY`** : In a given VPC network and region, only a single proxy-only subnet with purpose `REGIONAL_MANAGED_PROXY` can be active at any point in time. The active proxy-only subnet powers all of the following products:

    * [Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)
    * [Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
    * [Regional external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp)
    * [Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)
    * [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview)
    * [Cloud DNS Outbound Endpoints](https://docs.cloud.google.com/dns/docs/outbound-endpoints-overview) ([Preview](https://cloud.google.com/products#product-launch-stages))

**Note:**

If the client sends packets with the port explicitly specified, Envoy-based load balancers don't remove the port number by default. For example, traffic with `example.net:443` is first forwarded to an Envoy-based load balancing service and then routed to the backend by the URL map.

If there is no matching routing rule in the URL map, the traffic is routed to the default backend. You can specify URL map routing rules to specify the port number by setting the hostname as `example.net:443` and path `/*`. For more information, see [URL Map components](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#url-map-components).

gRPC library for golang mandates addition of port at the end of the hostname, so if a request is initiated to the load balancer, ensure that we have a matching host rule in the load balancer configuration.

## How proxy-only subnets fit into the load balancer's architecture

The following diagram shows the Google Cloud resources required for a regional internal Application Load Balancer.

[ ![Regional internal Application Load Balancer numbered components.](https://docs.cloud.google.com/static/load-balancing/images/ilb-l7-components.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-l7-components.svg) Regional internal Application Load Balancer numbered components (click to enlarge).

As shown in the diagrams, an Envoy-based load balancer deployment requires at least two subnets:

  * The load balancer's backend VMs and backend endpoints use a single subnet whose primary IP address range is `10.1.2.0/24` (in this example). _This subnet isn't the proxy-only subnet._ You can use multiple subnets for your backend VMs and endpoints if the subnets are in the same region as the load balancer. For internal Application Load Balancers, the load balancer's IP address associated with the forwarding rule can also be in this subnet (but does not need to be).
  * The proxy-only subnet is `10.129.0.0/23` (in this example).



## Planning the size of your proxy-only subnet

A proxy-only subnet must provide 64 or more IP addresses. This corresponds to a prefix length of `/26` or shorter. We recommend that you start with a proxy-only subnet with a `/23` prefix (512 proxy-only addresses) and change the size as your traffic needs change.

**Note:** You can use the non-RFC 1918 address range for the proxy-only subnet. This can be helpful if you have insufficient available addresses in your RFC 1918 address range.

Proxies are allocated at the VPC level, not the load balancer level. You must create one proxy-only subnet in each region of a VPC network in which you use Envoy-based load balancers. If you deploy multiple load balancers in the same region and same VPC network, they share the same proxy-only subnet for load balancing. Envoy-based load balancers automatically scale the number of proxies available to handle your traffic based on your traffic needs.

The number of proxies allocated to your load balancer is calculated based on the measured capacity needed to handle your traffic over a 10-minute time period. During this time period, we look at the greater of:

  * **The number of proxies needed to serve your traffic's bandwidth needs**. Each proxy instance can handle up to 18 MB per second. We monitor the total bandwidth required and divide that total by the bandwidth that a proxy instance can support.

  * **The number of proxies needed to handle connections and requests**. We count the total of each of the following resources and divide each value by what a proxy instance can handle:

    * 600 (HTTP) or 150 (HTTPS) new connections per second
    * 3,000 active connections
    * 1,400 requests per second

A proxy instance can handle 1,400 requests per second if Cloud Logging is disabled. If you enable Logging, your proxy instance can handle fewer requests per second. For example: logging 100% of requests decreases the proxy's request handling capacity to 700 requests per second. You can configure Logging to sample a smaller percentage of traffic. This lets you meet your observability needs while controlling your cost.




Each additional proxy incurs an additional hourly charge. To learn about how proxy-only subnets are billed, see the _Proxy instance charge_ section in the [Cloud Load Balancing pricing documentation](https://docs.cloud.google.com/vpc/network-pricing?e=48754805#section-2).

### Envoy-based load balancers and Secure Web Proxy Envoy proxies

When configuring both an Envoy-based load balancer and Secure Web Proxy in the same VPC, it is important to note the following:

  * Both the Envoy-based load balancer and Secure Web Proxy use IP addresses from the same proxy-only subnet.

  * To accommodate IP address requirements for both the services, consider using a larger proxy-only subnet, such as a `/22` subnet. This helps ensure sufficient address space for both configurations.

  * We recommend that you monitor proxy capacity to track IP address consumption. This helps prevent exhaustion of the proxy-only subnet, which can disrupt services.


**Note:** Google Cloud doesn't warn you if your proxy-only subnet runs out of IP addresses. However, you can configure Monitoring to monitor the IP address usage of your proxy-only subnet. You can [define alerting policies](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#defining_alerting_policies) to set up an alert for the `loadbalancing.googleapis.com/subnet/proxy_only/addresses` metric.

## Create proxy-only subnets

Depending on your load balancer and backend requirements, you can create the proxy-only subnet as either single-stack (`IPV4_ONLY`) or dual-stack (`IPV4_IPV6`).

  * `IPV4_ONLY`: You must use a single-stack proxy-only subnet when your load balancer needs to terminate IPv4 traffic.
  * `IPV4_IPV6`: You must use a dual-stack proxy-only subnet when your load balancer needs to terminate IPv4 or IPv6 traffic. To support an IPv6 forwarding rule, the proxy-only subnet must be dual-stack.



You must create proxy-only subnets for Envoy-based load balancers regardless of whether your network is auto-mode or custom. Creating a proxy-only subnet is essentially the same procedure as [creating any subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets), except with the addition of some flags.

For a proxy-only subnet, the `--purpose` must be set to either `REGIONAL_MANAGED_PROXY` or `GLOBAL_MANAGED_PROXY`, depending on your load balancer.

You can't reuse an existing subnet as the proxy-only subnet; you _must_ create a new subnet in each region that has an Envoy-based load balancer. This is in part because the [`subnets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update) doesn't allow modifying a subnet's `--purpose` field.

**Note:** For regional internal Application Load Balancers, set the purpose of the subnet to `--purpose=REGIONAL_MANAGED_PROXY`. If you previously created a proxy-only subnet with `--purpose=INTERNAL_HTTPS_LOAD_BALANCER`, you will need to migrate the subnet's purpose to `REGIONAL_MANAGED_PROXY` before you can create other Envoy-based load balancers in the same region of the VPC network.

You must create a proxy-only subnet for use by the load balancers' proxies, before creating forwarding rules for your regional load balancers. If you try to configure a load balancer without first creating a proxy-only subnet for the region, the load balancer creation process fails.

### Create an `IPV4-ONLY` proxy-only subnet

To configure an `IPV4-ONLY` proxy-only subnet, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.   
[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)
  2. Click the name of the Shared VPC network that you want to add a proxy-only subnet to.
  3. Click **Add subnet**.
  4. Enter a **Name**.
  5. Select a **Region**. 
  6. Set **Purpose** to one of the following: 
     * For regional load balancers: **Regional Managed Proxy**
     * For cross-region load balancers: **Cross-region Managed Proxy**
     * Enter an **IP address range**.
     * Click **Add**.



###  gcloud 

The [gcloud compute networks subnets create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) command creates a proxy-only subnet.
    
    
    gcloud compute networks subnets create SUBNET_NAME \
        --purpose=SUBNET_PURPOSE \
        --role=ACTIVE \
        --region=REGION \
        --network=VPC_NETWORK_NAME \
        --range=CIDR_RANGE
    

Replace the following:

  * `SUBNET_NAME`: the name of the proxy-only subnet.
  * `SUBNET_PURPOSE`: the purpose of the subnet. Set this to either `REGIONAL_MANAGED_PROXY` or `GLOBAL_MANAGED_PROXY`, depending on your load balancer.
  * `REGION`: the region of the proxy-only subnet.
  * `VPC_NETWORK_NAME`: the name of the VPC network that contains the subnet.
  * `CIDR_RANGE`: the primary IP address range of the subnet. You must use a subnet mask no longer than `26` so that at least 64 IP addresses are available for proxies in the region. The recommended subnet mask length is `/23`.



### Create a dual-stack proxy-only subnet

For regional internal, regional external, and cross-region Application Load Balancers and proxy Network Load Balancers, you can configure the proxy-only subnet to support dual-stack (IPv4 and IPv6) traffic.

  1. Create a [custom mode VPC network with a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-network-dual). Ensure the following:

     * The VPC network must use custom subnet mode, `--subnet-mode custom`.
     * You must enable internal IPv6 on the network using the `--enable-ula-internal-ipv6` flag.
  2. Create a dual-stack proxy-only subnet:
         
         gcloud compute networks subnets create NEW_PROXY_ONLY_SUBNET_NAME \
            --purpose=SUBNET_PURPOSE \
            --role=ACTIVE \
            --region=REGION \
            --network=VPC_NETWORK_NAME \
            --range=NEW_PROXY_ONLY_SUBNET_RANGE \
            --stack-type=IPV4_IPV6
         

Replace the following:

     * `NEW_PROXY_ONLY_SUBNET_NAME`: the name of the proxy-only subnet.
     * `SUBNET_PURPOSE`: the purpose of the subnet. Set this to either `REGIONAL_MANAGED_PROXY` or `GLOBAL_MANAGED_PROXY`, depending on your load balancer.
     * `REGION`: the region of the proxy-only subnet.
     * `VPC_NETWORK_NAME`: the name of the VPC network that contains the subnet.
     * `NEW_PROXY_ONLY_SUBNET_RANGE`: the primary IPv4 address range of the subnet, in CIDR notation. For example, `10.1.2.0/24`. You can't specify an IPv6 address range; the range is automatically allocated from the network's ULA (Unique Local Address) range.



### Configure backend firewall rules

For a complete configuration example, refer to [Configuring the proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb#configuring_the_proxy-only_subnet).

You must configure a firewall rule for your backends to accept connections from the proxy-only subnet. For a complete configuration example, including firewall rule setup, see the following:

  * [Set up a regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb)
  * [Set up a regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal)
  * [Set up a regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs)
  * [Set up a regional external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-migs)
  * [Set up a cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal)
  * [Set up a cross-region internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-migs)



### Proxy availability

Sometimes Google Cloud regions don't have enough proxy capacity for a new load balancer. If this happens, the Google Cloud console provides a proxy availability warning message when you are creating your load balancer. To resolve this issue, you can do one of the following:

  * Select a different region for your load balancer. This can be a practical option if you have backends in another region.
  * Select a VPC network that already has an allocated proxy-only subnet.
  * Wait for the capacity issue to be resolved.



## Change the size or address range of a proxy-only subnet

When the amount of traffic handled by your load balancer increases, you might need to increase the size of your proxy-only subnet to allow a larger number of Envoy proxies to power your load balancers.

You can't expand the primary IPv4 address range of a proxy-only subnet in the same way that you would expand the primary IPv4 address range of a regular subnet (with the [expand-ip-range command](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#expand-subnet)). Instead, you must replace the proxy-only subnet with a new one. The replacement process works like this:

  * Create a new proxy-only subnet, in the same region and VPC network as the existing (original) proxy-only subnet. When creating this new proxy-only subnet, set its `role` to `BACKUP`. (For each proxy-only subnet purpose, Google Cloud allows one `ACTIVE` and one `BACKUP` proxy-only subnet to exist in a given region and VPC network.)

  * Adjust ingress allow firewall rules, applicable to your backends, so that they allow connections from the primary IPv4 address ranges of both the original and new proxy-only subnets.

  * Set the role of the new proxy-only subnet to `ACTIVE` and specify a draining period to allow connections between your backends and the Envoy proxies in the original proxy-only subnet to terminate. (Google Cloud automatically sets the role of the original proxy-only subnet to `BACKUP` when you set the role of the new proxy-only subnet to `ACTIVE`.)

  * Monitor the status of the original proxy-only subnet (see the gcloud tab for more information on monitoring). Once its status is `READY`, the subnet is no longer used, provided that its role is `BACKUP`. At this point, you can adjust ingress allow firewall rules to permit connections from just the primary IPv4 address range of the new proxy-only subnet, and you can delete the original proxy-only subnet.




###  Console 

  1. Create the new proxy-only subnet in the same region and VPC network, specifying a primary IPv4 address range that meets your needs. Set the role of the new proxy-only subnet to backup.

     1. In the Google Cloud console, go to the **VPC networks** page.   
[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)
     2. Click the name of the Shared VPC network that you want to add a proxy-only subnet to.
     3. Click **Add subnet**.
     4. Enter a **Name**.
     5. Select a **Region**. 
     6. Set **Purpose** to one of the following: 
        * For regional load balancers: **Regional Managed Proxy**
        * For cross-region load balancers: **Cross-region Managed Proxy**
        * For the **Role** , select **Backup**.
        * Enter an **IP address range**.
        * Click **Add**.
  2. Update ingress allow firewall rules that apply to your backend VMs or endpoints so that they include the primary IPv4 address ranges of _both_ the original and new proxy-only subnets.

  3. Set the role of the new proxy-only subnet to active, and specify a draining timeout to allow connections between your backends and the original proxy-only subnet to terminate. Google Cloud automatically sets the role of the original proxy-only subnet to backup when you set the role of the new proxy-only subnet to active.

     1. In the Google Cloud console, go to the **VPC networks** page.   
[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)
     2. Click the name of the Shared VPC network that you want to modify.
     3. Under **Reserved proxy-only subnets for load balancing** , locate the backup subnet created in the previous step.
     4. Click **Activate**.
     5. Specify an optional **Drain timeout**.
     6. Click **Activate the subnet**.
  4. After the connection draining timeout, or after you're confident that connections to your backend VMs or endpoints aren't coming from proxies in the original proxy-only subnet, you can do the following:

     * Update ingress allow firewall rules that apply to your backend VMs or endpoints so that they include the primary IPv4 address range of just the new proxy-only subnet.
     * [Delete](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#deleting_subnets) the original proxy-only subnet.

**Note:** The gcloud steps provide more information about how to monitor the draining status of the original proxy-only subnet.

###  gcloud 

The following steps show how to swap an existing proxy-only subnet with a new proxy-only subnet. In all of the following steps:

  * `ORIGINAL_PROXY_ONLY_SUBNET_NAME`: the name of the existing proxy-only subnet
  * `ORIGINAL_PROXY_ONLY_SUBNET_RANGE`: the primary IPv4 address range of the existing proxy-only subnet in CIDR format. This is an address range you chose previously.
  * `NEW_PROXY_ONLY_SUBNET_NAME`: the name of the new proxy-only subnet
  * `NEW_PROXY_ONLY_SUBNET_RANGE`: the primary IPv4 address range of the new proxy-only subnet in CIDR format. Choose an IPv4 address range to meet your needs.
  * `PROXY_ONLY_SUBNET_FIREWALL_RULE`: the name of an ingress allow VPC firewall rule that permits connections from proxy-only subnets
  * `REGION`: the region that contains the original and new proxy-only subnets
  * `VPC_NETWORK_NAME`: the VPC network name of the network that contains the original and new proxy-only subnets


  1. Create a new proxy-only subnet in the same region and VPC network using the [gcloud compute networks subnets create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) command with the `--role=BACKUP` flag.
         
         gcloud compute networks subnets create NEW_PROXY_ONLY_SUBNET_NAME \
            --purpose=SUBNET_PURPOSE \
            --role=BACKUP \
            --region=REGION \
            --network=VPC_NETWORK_NAME \
            --range=NEW_PROXY_ONLY_SUBNET_RANGE
         

Replace the following:

     * `SUBNET_PURPOSE`: Either `REGIONAL_MANAGED_PROXY` or `GLOBAL_MANAGED_PROXY` depending on the load balancer that needs to use the proxy-only subnet. For more information, see Supported load balancers.
  2. Update ingress allow firewall rules that apply to your backend VMs or endpoints so that they include the primary IPv4 address ranges of _both_ the original and new proxy-only subnets.
         
         gcloud compute firewall-rules update PROXY_ONLY_SUBNET_FIREWALL_RULE \
           --source-ranges=ORIGINAL_PROXY_ONLY_SUBNET_RANGE,NEW_PROXY_ONLY_SUBNET_RANGE
         

  3. Set the role of the new proxy-only subnet to `ACTIVE`, and specify a draining timeout (`--drain-timeout`) to allow connections between your backends and the original proxy-only subnet to terminate. Google Cloud automatically sets the role of the original proxy-only subnet to `BACKUP` when you set the role of the new proxy-only subnet to `ACTIVE`.

To immediately break connections between your backends and Envoy proxies in the original proxy-only subnet, set the `--drain-timeout` to `0s`.
         
         gcloud compute networks subnets update NEW_PROXY_ONLY_SUBNET_NAME \
            --region=REGION \
            --role=ACTIVE \
            --drain-timeout=CONNECTION_DRAINING_TIMEOUT
         

Replace the following:

     * `CONNECTION_DRAINING_TIMEOUT`: the amount of time, in seconds, to let existing connections between your backends and Envoy proxies in the original proxy-only subnet terminate.
  4. Monitor the status of the original proxy-only subnet by using the [gcloud compute networks subnets describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/describe) command.
         
         gcloud compute networks subnets describe ORIGINAL_PROXY_ONLY_SUBNET_NAME \
            --region=REGION
         

Wait for draining to complete. During draining, the original proxy-only subnet's status is `DRAINING`. You might have to execute the `describe` command a few times before the status of the original proxy-only subnet changes to `READY`.

  5. After the original proxy-only subnet is `READY` with the `BACKUP` role, the subnet is no longer used. Update ingress allow firewall rules that apply to your backend VMs or endpoints so that they include the primary IPv4 address range of just the new proxy-only subnet.
         
         gcloud compute firewall-rules update PROXY_ONLY_SUBNET_FIREWALL_RULE \
           --source-ranges=NEW_PROXY_ONLY_SUBNET_RANGE
         

  6. Delete the original proxy-only subnet.
         
         gcloud compute networks subnets delete ORIGINAL_PROXY_ONLY_SUBNET_NAME \
           --region=REGION
         




## Migrate the purpose of a proxy-only subnet

If you previously created a proxy-only subnet with `--purpose=INTERNAL_HTTPS_LOAD_BALANCER`, you will need to migrate the subnet's purpose to `REGIONAL_MANAGED_PROXY` before you can create other Envoy-based load balancers in the same region of the VPC network.

###  Console 

If you're using the Google Cloud console to create the load balancer, you will be prompted to migrate the purpose of a previously created proxy-only subnet from `--purpose=INTERNAL_HTTPS_LOAD_BALANCER` to `REGIONAL_MANAGED_PROXY` while creating the load balancer.

###  gcloud 

To change the purpose of an existing proxy-only subnet from `--purpose=INTERNAL_HTTPS_LOAD_BALANCER` to `REGIONAL_MANAGED_PROXY`, use the following command:
    
    
    gcloud compute networks subnets update PROXY_ONLY_SUBNET \
        --purpose=REGIONAL_MANAGED_PROXY \
        --region=REGION
    

Migrating the purpose of a proxy-only subnet from `--purpose=INTERNAL_HTTPS_LOAD_BALANCER` to `REGIONAL_MANAGED_PROXY` does not cause any downtime. The change should take effect nearly instantly.

## Delete a proxy-only subnet

Deleting a proxy-only subnet releases its primary IP address range so you can use the range for another purpose. Google Cloud enforces the following rules when it receives a request to delete a proxy-only subnet:

  * An active proxy-only subnet can't be deleted if there is at least one regional load balancer in the same region and VPC network.

  * An active proxy-only subnet can't be deleted if there is a backup proxy-only subnet in the same region and VPC network.

If you try to delete an active proxy-only subnet before deleting the backup, the following error message appears: "Invalid resource usage: Cannot delete ACTIVE subnetwork because a BACKUP subnetwork exists."




Practically, these rules have the following effect:

  * If no regional load balancer is defined in a given region and VPC network, you can delete the proxy-only subnets in that region. If a backup proxy-only subnet exists, you must first delete it before you can delete the active proxy-only subnet.

  * If you have at least one regional load balancer defined in a given region and VPC network, you can't delete the active proxy-only subnet; however, you can promote a backup proxy-only subnet to the active role, which automatically demotes the previously active proxy-only subnet to the backup role. After connections are drained, you can delete the backup (previously active) proxy-only subnet.




Refer to [deleting subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#deleting_subnets) in the VPC network documentation for more information.

## Limitations

The following constraints apply to proxy-only subnets:

  * You can't create a proxy-only subnet with a stack type of `IPV6_ONLY` for any load balancer. For regional external load balancers, the proxy-only subnet can have a stack type of either `IPV4_ONLY` or `IPV4_IPV6` (dual-stack) to support IPv6 traffic. However, for regional internal and cross-region internal load balancers, you must use the stack type, `IPV4_IPV6`.

  * You can't have both an `INTERNAL_HTTPS_LOAD_BALANCER` and a `REGIONAL_MANAGED_PROXY` subnet in the same network and region, in the same way you can't have two `REGIONAL_MANAGED_PROXY` proxies or two `INTERNAL_HTTPS_LOAD_BALANCER` proxies.

  * You can create only one active and one backup proxy-only subnet in each region in each VPC network.

  * You can't create a backup proxy-only subnet unless you have already created an active proxy-only subnet in that region and network.

  * You can change the role of a proxy-only subnet from backup to active by updating the subnet. When you do that, Google Cloud automatically changes the previously active proxy-only subnet to backup. You can't explicitly set the role of a proxy-only subnet to backup by updating it.

  * During a proxy-only subnet's connection draining period (`--drain-timeout`), you can't change the role of a proxy-only subnet from backup to active.

  * Proxy-only subnets don't support [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs).




## What's next

  * [Set up a regional external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb)
  * [Set up a regional external Application Load Balancer in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-shared-vpc)
  * [Set up a regional internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal)
  * [Set up a regional internal Application Load Balancer or cross-region internal Application Load Balancer in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/l7-internal/l7-internal-shared-vpc)
  * [Set up a regional internal proxy Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs)
  * [Set up a regional external proxy Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-migs)
  * [Set up a cross-region internal proxy Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-migs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
