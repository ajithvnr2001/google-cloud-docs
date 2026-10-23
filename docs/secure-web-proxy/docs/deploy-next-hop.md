---
url: https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop/
title: Deploy Secure Web Proxy as next hop \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:17.068726+00:00
---

# Deploy Secure Web Proxy as next hop  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Deploy Secure Web Proxy as next hop Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of how to create a Secure Web Proxy policy and then explains how to configure next hop routing for your Secure Web Proxy instance. In addition, this page describes how to configure either static routing or policy-based routing for your next hop.

By default, `SecureWebProxy` instances have a `RoutingMode` value of `EXPLICIT_ROUTING_MODE`, which means that you must configure your workloads to explicitly send HTTP(S) traffic to Secure Web Proxy. Instead of configuring individual clients to point to your Secure Web Proxy instance, you can set your Secure Web Proxy instance's `RoutingMode` as `NEXT_HOP_ROUTING_MODE`, which lets you define routes that direct traffic to your Secure Web Proxy instance.

When deploying your Secure Web Proxy instance as next hop, you can enable the gateway to listen on all ports (from `1` to `65535`), simplifying the configuration for dynamic environments or services that use multiple ports.

## Configure next hop routing for Secure Web Proxy

This section describes the steps to create a Secure Web Proxy policy and the procedure to deploy your Secure Web Proxy instance as next hop.

### Create a Secure Web Proxy policy

  1. [Complete all the required prerequisite steps](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart#before-you-begin).
  2. [Create a Secure Web Proxy policy](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart#create-secure-web-proxy-policy).
  3. [Create Secure Web Proxy rules](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart#create-rules).



### Deploy your Secure Web Proxy instance as next hop

###  Console 

  1. In the Google Cloud console, go to the **Web Proxies** page.

[Go to Web Proxies](https://console.cloud.google.com/net-security/swp/web-proxies/list)

  2. Click add_box **Create a secure web proxy**.

  3. Enter a name for the web proxy that you want to create, such as `myswp`.

  4. Enter a description of the web proxy, such as `My new swp`.

  5. For **Routing mode** , select the **Next hop** option.

  6. In the **Regions** list, select the region where you want to create the web proxy.

  7. In the **Network** list, select the network where you want to create the web proxy.

  8. In the **Subnetwork** list, select the subnetwork where you want to create the web proxy.

  9. Optional: Enter the Secure Web Proxy IP address. You can enter an IP address from the range of Secure Web Proxy IP addresses that reside in the subnetwork you created in the previous step. If you don't enter the IP address, then your Secure Web Proxy instance automatically chooses an IP address from the selected subnetwork.

  10. In the **Certificate** list, select the certificate that you want to use to create the web proxy.

  11. In the **Policy** list, select the policy that you created to associate the web proxy with.

  12. Click **Create**.




###  Cloud Shell 

  1. Use a text editor to create a `gateway.yaml` file.

  2. Add the following code to the `gateway.yaml` file:
         
         name: projects/PROJECT_ID/locations/REGION/gateways/swp1
         type: SECURE_WEB_GATEWAY
         addresses: ["IP_ADDRESS"]
         ports: [443, 80]
         gatewaySecurityPolicy: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1
         network: projects/PROJECT_ID/global/networks/NETWORK
         subnetwork: projects/PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK
         routingMode: NEXT_HOP_ROUTING_MODE
         

**Optional** : To configure the gateway to listen on all ports (from `1` to `65535`), add the `all_ports` field in the `gateway.yaml` file and set it to `true`. This feature is supported in [Preview](https://cloud.google.com/products#product-launch-stages).

For information about the limitations related to using the `all_ports` feature, see Limitations.
         
         name: projects/PROJECT_ID/locations/REGION/gateways/swp1
         type: SECURE_WEB_GATEWAY
         addresses: ["IP_ADDRESS"]
         all_ports: true
         gatewaySecurityPolicy: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1
         network: projects/PROJECT_ID/global/networks/NETWORK
         subnetwork: projects/PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK
         routingMode: NEXT_HOP_ROUTING_MODE
         

**Optional** : To allow client applications from other Google Cloud regions to connect to your proxy, enable [global access](https://docs.cloud.google.com/secure-web-proxy/docs/configure-global-access) when creating your Secure Web Proxy instance.

In the `gateway.yaml` file, add the `allowGlobalAccess` field and set it to `true`.

**Important** : You can enable `allowGlobalAccess` only when you create a Secure Web Proxy instance. You can't configure this setting later.
         
         name: projects/PROJECT_ID/locations/REGION/gateways/swp1
         type: SECURE_WEB_GATEWAY
         addresses: ["IP_ADDRESS"]
         ports: [443, 80]
         gatewaySecurityPolicy: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1
         network: projects/PROJECT_ID/global/networks/NETWORK
         subnetwork: projects/PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK
         routingMode: NEXT_HOP_ROUTING_MODE
         allowGlobalAccess: true
         

  3. Create a Secure Web Proxy instance.
         
         gcloud network-services gateways import swp1 \
         --source=gateway.yaml \
         --location=REGION
         

A Secure Web Proxy instance can take several minutes to deploy.




## Create routes for next hop

After you have created a Secure Web Proxy instance, you can configure either static routing or policy-based routing for your next hop:

  * Static routes direct the traffic within your network to your Secure Web Proxy instance in the same region. To set up a static route with your Secure Web Proxy as next hop, you must configure [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).
  * Policy-based routes let you direct traffic to your Secure Web Proxy instance from a source IP address range. When you configure a policy-based route for the first time, you must also configure another policy-based route to be the default route.



The following two sections explain how to create static routes and policy-based routes.

### Create static routes

**Important:** After you finish creating a static route, you must complete all actions specified in the Post-deployment checklist section. This helps ensure that the route correctly directs traffic to your Secure Web Proxy instance.

To route traffic to your Secure Web Proxy instance, set up a static route with the `gcloud compute routes create` command. You must associate the static route with a [network tag](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags), and use the same network tag on all of your source resources to help ensure that their traffic is redirected to your Secure Web Proxy instance. Static routes don't let you define a source IP address range.

For more information about how static routes work in Google Cloud, see [Static routes](https://docs.cloud.google.com/vpc/docs/static-routes).

###  gcloud 

Use the following command to create a static route.
    
    
    gcloud compute routes create STATIC_ROUTE_NAME \
        --network=NETWORK_NAME \
        --next-hop-ilb=SWP_IP \
        --destination-range=DESTINATION_RANGE \
        --priority=PRIORITY \
        --tags=TAGS \
        --project=PROJECT
     

Replace the following:

  * `STATIC_ROUTE_NAME`: name of your static route
  * `NETWORK_NAME`: name of your network
  * `SWP_IP`: IP address of your `SecureWebProxy` instance in the subnetwork specified in the `gateway.yaml` file
  * `DESTINATION_RANGE`: range of IP addresses to which you want to redirect the traffic. For example, use `0.0.0.0/0` to route all internet traffic to your Secure Web Proxy instance
  * `PRIORITY`: priority of your route; higher numbers denote a lower priority. Make sure that the priority of your route is numerically lower than the default internet route, which is typically `1000`
  * `TAGS`: comma-separated list of tags that you you'll use with your Secure Web Proxy instance
  * `PROJECT`: ID of your project



**Create a VM in the appropriate subnet with network tags specified in the route**
    
    
    gcloud compute instances create swp-nexthop-test-vm \
        --subnet=SUBNETWORK \
        --zone=ZONE \
        --image-project=debian-cloud \
        --image-family=debian-11 \
        --tags=TAGS

Replace the following:

  * `SUBNETWORK`: subnetwork that you configured for the web proxy
  * `ZONE`: zone of your test VM instance
  * `TAGS`: comma-separated list of tags that you'll use with your Secure Web Proxy instance



### Create policy-based routes

**Important:** Misconfigured policy-based routes can severely disrupt the flow of traffic through your network. To make sure that your routes are correctly configured, follow these steps:  
1\. Before you create a policy-based route, review the [limitations](https://docs.cloud.google.com/vpc/docs/policy-based-routes#limitations) of policy-based routes.   
2\. After you finish creating a policy-based route, you must complete all actions specified in the Post-deployment checklist section.

As an alternative to static routing, you can set up a policy-based route by using the `network-connectivity policy-based-routes create` command. You also need to create a policy-based route to be the default route, which enables default routing for the traffic between virtual machine (VM) instances within your network. For more information about how policy-based routes work in Google Cloud, see [Policy-based routing](https://docs.cloud.google.com/vpc/docs/policy-based-routes).

The priority of the route that enables [default routing](https://docs.cloud.google.com/vpc/docs/policy-based-routes#skip-option) must be higher (numerically lower) than the priority of the policy-based route that directs traffic to the Secure Web Proxy instance. If you create the policy-based route at a higher priority than the route that enables default routing, it takes priority over all other VPC routes.

Use the following example to create a policy-based route that directs traffic to your Secure Web Proxy instance.

###  gcloud 

Use the following command to create the policy-based route.
    
    
    gcloud network-connectivity policy-based-routes create POLICY_BASED_ROUTE_NAME \
        --network="projects/PROJECT/global/networks/NETWORK_NAME" \
        --next-hop-ilb-ip=SWP_IP \
        --protocol-version="IPV4" \
        --destination-range=DESTINATION_RANGE \
        --source-range=SOURCE_RANGE \
        --priority=2 \
        --project=PROJECT
     

Replace the following:

  * `POLICY_BASED_ROUTE_NAME`: name of your policy-based route
  * `NETWORK_NAME`: name of your network
  * `SWP_IP`: IP address of your Secure Web Proxy instance
  * `DESTINATION_RANGE`: range of IP addresses to which you want to redirect the traffic
  * `SOURCE_RANGE`: range of IP addresses from which you want to redirect the traffic
  * `PROJECT`: ID of your project



Next, use the following steps to create the default-routing policy-based route.

###  gcloud 

Use the following command to create the default-routing policy-based route.
    
    
    gcloud network-connectivity policy-based-routes create DEFAULT_POLICY_BASED_ROUTE_NAME \
        --network="projects/PROJECT/global/networks/NETWORK_NAME" \
        --next-hop-other-routes="DEFAULT_ROUTING" \
        --protocol-version="IPV4" \
        --destination-range=DESTINATION_RANGE \
        --source-range=SOURCE_RANGE \
        --priority=1 \
        --project=PROJECT
     

Replace the following:

  * `DEFAULT_POLICY_BASED_ROUTE_NAME`: name of your policy-based route
  * `NETWORK_NAME`: name of your network
  * `DESTINATION_RANGE`: range of IP addresses to which you want to redirect the traffic
  * `SOURCE_RANGE`: range of IP addresses from which you want to redirect the traffic
  * `PROJECT`: ID of your project



## Post-deployment checklist

Make sure that you complete the following tasks after configuring either a static route or a policy-based route with your Secure Web Proxy instance as next hop:

  * Confirm that there is a [default route to the internet gateway](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet).
  * Add the correct [network tag](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#interaction_with_routes) to the static route that points to your Secure Web Proxy instance as next hop.
  * Define an appropriate priority for the default route to your Secure Web Proxy instance as next hop.
  * Because Secure Web Proxy is a regional service, make sure that the client traffic originates in the same region as your Secure Web Proxy instance.

**Caution:** You must complete all checklist items to help ensure that the route correctly directs traffic to your Secure Web Proxy instance.

## Limitations

  * `SecureWebProxy` instances with `RoutingMode` set as `NEXT_HOP_ROUTING_MODE` support HTTP(S) and TCP proxy traffic. Other types of traffic, including cross-region traffic, are dropped without notification.
  * When you use `next-hop-ilb`, the limitations that apply to internal passthrough Network Load Balancers apply to next hops if the destination next hop is a Secure Web Proxy instance. For more information, see the next hops and features tables for [static routes](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops).
  * All the traffic from virtual machines (VMs), including background traffic and updates, that your next hop route matches will get routed to your Secure Web Proxy instance.
  * For a VPC network in a region, you can deploy only one Secure Web Proxy as next hop (SWPaNH) instance.
  * When you use the `all_ports` feature, the following limitations apply: 
    * The `all_ports` feature is applicable only for gateways with `type: SECURE_WEB_GATEWAY`.
    * You can use the `all_ports: true` configuration only when `routingMode` is set to `NEXT_HOP_ROUTING_MODE`.
    * You can't specify both the `all_ports: true` configuration and list individual ports in the ports field for the same gateway resource. You must use only one type of port configuration, not both.
    * Within a given network and region, you can't simultaneously deploy one Secure Web Proxy instance in next hop mode with the `all_ports: true` configuration and another Secure Web Proxy instance in any other mode.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
