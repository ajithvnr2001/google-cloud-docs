---
url: https://docs.cloud.google.com/load-balancing/docs/https/setup-regional-ext-https-external-backend/
title: Set up a regional external Application Load Balancer with an external backend \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:22.307747+00:00
---

# Set up a regional external Application Load Balancer with an external backend  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setup-regional-ext-https-external-backend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional external Application Load Balancer with an external backend Stay organized with collections  Save and categorize content based on your preferences. 

The guide shows you how to configure a regional external Application Load Balancer that proxies requests to an external backend. An external backend is an endpoint that is external to Google Cloud. 

Before following this guide, familiarize yourself with the [Internet NEG overview](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts) documentation, including the [limitations](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#limitations).

The following architecture diagram shows a regional external Application Load Balancer frontend with an external backend. [ ![A regional external Application Load Balancer with an external backend.](https://docs.cloud.google.com/static/load-balancing/images/reg-ext-app-internet-neg.svg)](https://docs.cloud.google.com/static/load-balancing/images/reg-ext-app-internet-neg.svg) **Figure 1.** A regional external Application Load Balancer with an external backend (click to enlarge).

**Note:** Regional external Application Load Balancers support both the Premium and Standard Network Service Tiers. This procedure demonstrates the setup with Standard Tier.

## Permissions

To follow this guide, you need to create an internet NEG and create or modify an Application Load Balancer in a project. You should be either a project [Owner or Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner` or `roles/editor`), or you should have both of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam).

Task | Required role  
---|---  
Create and modify load balancer components | [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
(`roles/compute.networkAdmin`)   
Create and modify NEGs | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
(`roles/compute.instanceAdmin`)   
  
## Optional: Use BYOIP addresses

With bring your own IP (BYOIP), you can import your own public addresses to Google Cloud to use the addresses with Google Cloud resources. For example, if you import your own IPv4 addresses, you can assign one to the forwarding rule when you configure your load balancer. When you follow the instructions in this document to [create the load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setup-regional-ext-https-external-backend#create_the_load_balancer), provide the BYOIP address as the **IP address**.

For more information about using BYOIP, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

## Set up your external backend environment outside Google Cloud

To set up your external backend environment, see the following sections.

### Configure network endpoints

Configure a network endpoint to expose your external backend to Google Cloud. Make sure that the endpoint—either an IP:Port combination or a fully-qualified domain name (FQDN) and port—is reachable over the internet. This endpoint is later referenced from the internet NEG.

For detailed configuration requirements for internet NEG endpoints, see the [Internet NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts).

### Allow the external backend to receive traffic from Google Cloud

**_This step can be completed after you've created the proxy-only subnet and set up the Cloud NAT gateway._**

To allow requests from Google Cloud to reach your external backend, you'll need to perform the following steps:

  1. Configure a Cloud NAT gateway with IP addresses that are used for egress traffic from Google Cloud. The gateway maps the proxy-only subnet range to the external IP addresses. For the steps, see Set up a Cloud NAT gateway.
  2. Make sure that your external backend environment is configured to allow traffic from Google Cloud to reach the external backend. For example, if you used pre-reserved IP addresses for the NAT gateway, you'll allowlist those IP addresses on your external environment. You'll likely need to work with the network or security admin of your external environment to set this up.



## Set up your Google Cloud environment

You'll need a VPC network with two subnets: one for the load balancer components and the other for the region's proxy-only subnet. Then you'll create the load balancer with an internet NEG backend.

**Note:** If you're planning a cross-cloud deployment with a regional internet NEG, you can use Cloud Location Finder to identify the optimal region or zone for your deployment based on factors like distance, network latency, carbon footprint (Google CFE%), or the territory code (in case you have regulatory requirements for your network traffic). For details, see the [Cloud Location Finder documentation](https://docs.cloud.google.com/location-finder/docs/overview) ([Preview](https://cloud.google.com/products/#product-launch-stages)). 

### Create the VPC network and subnet

This subnet is used to create the load balancer's components.

###  Cloud console 

  1. In the Google Cloud console, go to the **VPC networks** page.   
[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)
  2. Click **Create VPC network**.
  3. Enter a **Name** : LB_NETWORK.
  4. In the **Subnets** section: 
     * Set the **Subnet creation mode** to **Custom**.
     * In the **New subnet** section, enter the following information: 
       * **Name** : LB_SUBNET_NAME
       * **Region** : REGION
       * **IP address range** : LB_SUBNET_RANGE
     * Click **Done**.
  5. Click **Create**.



###  gcloud 

  1. Create the custom VPC network by using the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create):
         
         gcloud compute networks create LB_NETWORK \
           --subnet-mode=custom
         

  2. Create a subnet in the LB_NETWORK network.
         
         gcloud compute networks subnets create LB_SUBNET_NAME \
           --network=LB_NETWORK \
           --range=LB_SUBNET_RANGE \
           --region=REGION
         




### Configure the proxy-only subnet

This proxy-only subnet is used by all regional Envoy-based load balancers in the REGION region.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.   
[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)
  2. Select a **Network** from the list.
  3. Click **Add subnet**.
  4. Enter a **Name** : PROXY_ONLY_SUBNET_NAME.
  5. Select a **Region** : REGION.
  6. Set **Purpose** to **Regional Managed Proxy**.
  7. Enter an **IP address range** : PROXY_ONLY_SUBNET_RANGE.
  8. Click **Add**.



###  gcloud 

Create the proxy-only subnet with the [`gcloud compute networks subnets create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) command.
    
    
    gcloud compute networks subnets create PROXY_ONLY_SUBNET_NAME \
      --purpose=REGIONAL_MANAGED_PROXY \
      --role=ACTIVE \
      --region=REGION \
      --network=LB_NETWORK \
      --range=PROXY_ONLY_SUBNET_RANGE
    

### Set up a Cloud NAT gateway

Before you configure the Cloud NAT gateway, make sure you've reviewed the associated limitations and pricing considerations. For details, see [Regional NEGs: Use a Cloud NAT gateway](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#nat-support). 

The following commands describe how to set up a Cloud NAT gateway. The Cloud NAT gateway can be configured to use either automatic NAT external IP addresses, in which allocation is based on demand, or to use a manually pre-reserved set of external IP addresses. The gateway maps the proxy-only subnet range to the external IP addresses.

#### Set up automatic NAT allocated IP addresses

When you create a Cloud NAT gateway with automatic NAT IP address allocation, you can specify the [Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/overview) (Premium Tier or Standard Tier) from which the Cloud NAT gateway allocates the IP addresses.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** or **Create Cloud NAT gateway**. **Note:** If this is the first Cloud NAT gateway that you're creating, click **Get started**. If you already have existing gateways, then instead of **Get started** , Google Cloud displays the **Create Cloud NAT gateway** button. To create another gateway, click **Create Cloud NAT gateway**.

  3. Enter a gateway name LB_NAT_CONFIG.

  4. For **NAT type** , select **Public**.

  5. In the **Network** list, select LB_NETWORK.

  6. In the **Region** list, select REGION.

  7. Create a Cloud Router in the region.

  8. For **Source endpoint type** , select **Managed proxy load balancers**.

  9. In the **Source** list, select **Custom**.

     * For **Subnets** , select PROXY_ONLY_SUBNET_NAME.
  10. In the **Cloud NAT IP addresses** list, select **Automatic (recommended)**.

  11. For **Network service tier** , choose either **Premium** or **Standard**.

  12. Click **Create**.




###  gcloud 

Use dynamically allocated IP addresses if your external backend environment doesn't require you to allowlist specific Google Cloud IP addresses that can send traffic to the external backend.

  1. Create a Cloud Router:
         
         gcloud beta compute routers create ROUTER_NAME \
           --network=LB_NETWORK \
           --region=REGION

  2. Set up the Cloud NAT gateway.
         
         gcloud beta compute routers nats create LB_NAT_CONFIG \
           --router=ROUTER_NAME \
           --endpoint-types=ENDPOINT_TYPE_MANAGED_PROXY_LB \
           --nat-custom-subnet-ip-ranges=PROXY_ONLY_SUBNET_NAME \
           --auto-allocate-nat-external-ips \
           --region=REGION
         




Replace the following:

  * `LB_NAT_CONFIG`: the name of your NAT configuration.

  * `ROUTER_NAME`: the name of your Cloud Router.

  * `REGION`: the region of the NAT to create. If not specified, you might be prompted to select a region (interactive mode only).

  * `PROXY_ONLY_SUBNET_NAME`: the name of your proxy only subnet.




#### Set up manually allocated IP addresses

Use manually allocated IP addresses only if your external backend environment requires you to use an allowlist for specific Google Cloud IP addresses. If the external backend environment doesn't need an allowlist, use dynamic allocation instead as shown previously.

When creating a Cloud NAT gateway, you can choose to manually assign NAT IP addresses from either Premium Tier or Standard Tier or both, subject to certain [conditions](https://docs.cloud.google.com/nat/docs/ports-and-addresses#assign-mixed-tier-ip).

**Warning:** If you provision fewer NAT IP addresses than the [number of assigned Envoy proxies](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets#proxy-subnet-size), requests sent to the internet NEG might result in HTTP 5xx errors. To ensure that you are informed when such an event occurs, set up an alert for the [nat_allocation_failed](https://docs.cloud.google.com/nat/docs/monitoring#gateway-metrics) metric. Contact support if you need help calculating the number of IP addresses that must be allocated for your load balancer in a specific region.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** or **Create Cloud NAT gateway**. **Note:** If this is the first Cloud NAT gateway that you're creating, click **Get started**. If you already have existing gateways, then instead of **Get started** , Google Cloud displays the **Create Cloud NAT gateway** button. To create another gateway, click **Create Cloud NAT gateway**.

  3. Enter a gateway name LB_NAT_CONFIG.

  4. In the **Network** list, select LB_NETWORK.

  5. In the **Region** list, select REGION.

  6. Select or create a Cloud Router in the region.

  7. For **Source endpoint type** , select **Managed proxy load balancers**.

  8. In the **Source** list, select **Custom**.

     * In the **Subnets** , select PROXY_ONLY_SUBNET_NAME.
  9. In the **Cloud NAT IP addresses** list, select **Manual**.

  10. For **Network service tier** , choose either **Premium** or **Standard**.

  11. Select or create a static reserved external IP address to use for NAT.

**Note:** You can only select or create IP addresses based on the tier that you have selected in the previous step.
  12. If you want to specify additional IP addresses, click **Add IP address** , and then select or create an additional static reserved external IP address.

  13. Click **Create**.




###  gcloud 

  1. Create the IP addresses. Because the gateway performs one-to-one NAT translation, you must make sure that the pool of reserved IP addresses is big enough to handle the amount of traffic you're expecting. Insufficiently allocated NAT IP addresses could result in traffic loss.
         
         gcloud compute addresses create IP_ADDRESS_NAME_1 IP_ADDRESS_NAME_2 [IP_ADDRESS_NAME_3 ...] \
           --region=REGION
         

  2. Create a Cloud Router:
         
         gcloud compute routers create ROUTER_NAME \
           --network=LB_NETWORK \
           --region=REGION

  3. Set up the Cloud NAT gateway.
         
         gcloud beta compute routers nats create LB_NAT_CONFIG \
           --router=ROUTER_NAME \
           --endpoint-types=ENDPOINT_TYPE_MANAGED_PROXY_LB \
           --nat-custom-subnet-ip-ranges=PROXY_ONLY_SUBNET_NAME \
           --nat-external-ip-pool=IP_ADDRESS_NAME_1,IP_ADDRESS_NAME_2,[IP_ADDRESS_NAME_3 ...] \
           --region=REGION
         

Replace the following:



  * `LB_NAT_CONFIG`: the name of your NAT configuration.

  * `ROUTER_NAME`: the name of your Cloud Router.

  * `PROXY_ONLY_SUBNET_NAME`: the name of your proxy only subnet.

  * `REGION`: the region of the NAT to create. If not specified, you might be prompted to select a region (interactive mode only).




#### Set up dynamic port allocation

Update the Cloud NAT gateway to use dynamic port allocation mode to fully use the assigned IP addresses.

###  gcloud 

  1. Update the Cloud NAT gateway. We recommend that you set the minimum number of ports to 2048 and the maximum number of ports to 4096.
         
         gcloud compute routers nats update LB_NAT_CONFIG \
             --router=ROUTER_NAME \
             --enable-dynamic-port-allocation \
             --min-ports-per-vm=MIN_PORTS_PER_VM \
             --max-ports-per-vm=MAX_PORTS_PER_VM \
             --region=REGION
         

  2. Verify that dynamic port allocation is enabled and the minimum and maximum number of ports are set.
         
         gcloud compute routers nats describe LB_NAT_CONFIG \
              --router=ROUTER_NAME \
              --region=REGION
         

The output is similar to the following:
         
         enableDynamicPortAllocation: true
         enableEndpointIndependentMapping: false
         endpointTypes:
         ‐ ENDPOINT_TYPE_MANAGED_PROXY_LB
         logConfig:
           enable: true
           filter: ALL
         maxPortsPerVm: 4096
         minPortsPerVm: 2048
         name: LB_NAT_CONFIG
         natIpAllocateOption: MANUAL_ONLY
         natIps:
         ‐ https://www.googleapis.com/compute/projects/PROJECT_NAME/regions/REGION/addresses/ADDRESS
         sourceSubnetworkIpRangesToNat: ALL_SUBNETWORKS_ALL_IP_RANGES
         type: PUBLIC
         




For more information, see [Specify subnet ranges for NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#specify_subnet_ranges_for_nat) in the Cloud NAT documentation.

Make sure that you use an allowlist for the NAT IP address ranges on your external backend environment, so that your external backend can receive traffic from Google Cloud.

### Reserve the load balancer's IP address

Reserve a static IP address for the load balancer.

###  Console 

  1. In the Google Cloud console, go to the **Reserve a static address** page.

[Go to Reserve a static address](https://console.cloud.google.com/networking/addresses/add)

  2. Choose a **Name** for the new address.

  3. For **Network Service Tier** , select **Standard**.

  4. For **IP version** , select **IPv4**. IPv6 addresses can only be global and can only be used with global load balancers.

  5. For **Type** , select **Regional**.

  6. Select a **Region**.

  7. Leave the **Attached to** option set to **None**. After you create the load balancer, this IP address will be attached to the load balancer's forwarding rule.

  8. Click **Reserve** to reserve the IP address.




###  gcloud 

  1. To reserve a static external IP address using `gcloud compute`, use the [`compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
         
         gcloud compute addresses create LB_IP_ADDRESS  \
            --region=REGION \
            --network-tier=STANDARD
         

Replace the following:

     * `LB_IP_ADDRESS`: the name you want to call this address.
     * `REGION`: the region where you want to reserve this address. This region should be the same region as the load balancer. All regional IP addresses are `IPv4`.
  2. Use the [`compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) to view the result:
         
         gcloud compute addresses describe LB_IP_ADDRESS
         




### Set up the internet NEG

You can create an internet NEG using either `INTERNET_FQDN_PORT` endpoints or `INTERNET_IP_PORT` endpoints.

###  Console 

**Create a NEG with`INTERNET_FQDN_PORT` endpoints**

  1. In the Google Cloud console, go to the **Network endpoint group** page.

[Go to Network endpoint group](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click **Create network endpoint group**.

  3. Specify an INTERNET_NEG_NAME for your Internet NEG. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  4. In the **Network endpoint group type** list, select **Network endpoint group (Internet)** and then do the following:

     * In the **Scope** list, select **Regional**.
     * Optional: In the **Region** list, change the REGION for this NEG.
     * In the **Network** list, select LB_NETWORK.
     * In the **Default port** box, enter DEFAULT_PORT_NUMBER.
     * In the **Add endpoints through** list, select **Fully qualified domain name and port**.
  5. Select **Create**.



**Add`INTERNET_FQDN_PORT` endpoints to the NEG**

  1. In the Google Cloud console, go to the **Network endpoint group** page.

[Go to Network endpoint group](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click INTERNET_NEG_NAME.
  3. Enter the **Fully qualified domain name** such as `myorg.example.com`. You must specify the FQDN objects in [standard FQDN syntax](https://wikipedia.org/wiki/Fully_qualified_domain_name#Syntax).

  4. Optional: For **Port type** , select **Custom**. If the **Port type** is `Default`, the default port of the NEG is used.

  5. In the **Port number** box, enter PORT_NUMBER_1.
  6. Select **Create**.



**Create a NEG with`INTERNET_IP_PORT` endpoints**

  1. In the Google Cloud console, go to the **Network endpoint group** page.

[Go to Network endpoint group](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click **Create network endpoint group**.

  3. Specify a name INTERNET_NEG_NAME for your Internet NEG. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  4. In the **Network endpoint group type** list, select **Network endpoint group (Internet)** and then do the following:

     * In the **Scope** list, select **Regional**.
     * Optional: In the **Region** list, change the REGION for this NEG.
     * In the **Network** list, select LB_NETWORK.
     * In the **Default port** box, enter DEFAULT_PORT_NUMBER.
     * In the **Add endpoints through** list, select **IP and port**.
  5. Select **Create**.



**Add`INTERNET_IP_PORT` endpoints to the NEG**

  1. In the Google Cloud console, go to the **Network endpoint group** page.

[Go to Network endpoint group](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click INTERNET_NEG_NAME.
  3. In the **IP address** field, enter IP_ADDRESS_1.
  4. Optional: In the **Port type** list, select **Custom**. If the **Port type** is `Default`, the default port of the NEG is used.

  5. In the **Port number** field, enter a PORT_NUMBER_1.
  6. Select **Create**.



###  gcloud 

#### To create a NEG with `INTERNET_FQDN_PORT` endpoints:

  1. Create the NEG resource.
         
         gcloud beta compute network-endpoint-groups create INTERNET_NEG_NAME \
             --network-endpoint-type=INTERNET_FQDN_PORT \
             --default-port=DEFAULT_PORT_NUMBER \
             --network=LB_NETWORK \
             --region=REGION
         

  2. Add endpoints to the NEG. If a port isn't specified, the default port of the NEG is used.
         
         gcloud beta compute network-endpoint-groups update INTERNET_NEG_NAME \
             --add-endpoint="fqdn=FULLY_QUALIFIED_DOMAIN_NAME_1,port=PORT_NUMBER_1" \
             [--add-endpoint="fqdn=FULLY_QUALIFIED_DOMAIN_NAME_2,port=PORT_NUMBER_2" \]
             --region=REGION
         

Replace the following:

     * `FULLY_QUALIFIED_DOMAIN_NAME`: the fully qualified domain name for the endpoint
     * `PORT_NUMBER`: the port number for the endpoint

You can add up to 256 endpoints per NEG.




If your domain is resolvable over the internet, no other configuration is needed to set up DNS. However, if you're using private FQDNs, you'll need to configure Cloud DNS to facilitate DNS resolution. The name must be hosted on Cloud DNS or be resolvable through DNS forwarding from Cloud DNS to an on-premises DNS.

Start by creating a [Cloud DNS zone](https://docs.cloud.google.com/dns/docs/zones) to host the DNS records in your project. Then add the DNS records to it. Refer the [Cloud DNS documentation](https://docs.cloud.google.com/dns/docs/overview) for specific configuration steps.

#### To create a NEG with `INTERNET_IP_PORT` endpoints:

  1. Create the NEG resource.
         
         gcloud beta compute network-endpoint-groups create INTERNET_NEG_NAME \
             --network-endpoint-type=INTERNET_IP_PORT \
             --default-port=DEFAULT_PORT_NUMBER \
             --network=LB_NETWORK \
             --region=REGION
         

  2. Add endpoints to the NEG. If a port isn't specified, the default port of the NEG is used.
         
         gcloud beta compute network-endpoint-groups update INTERNET_NEG_NAME \
             --add-endpoint="ip=IP_ADDRESS_1,port=PORT_NUMBER_1" \
             [--add-endpoint="ip=IP_ADDRESS_2,port=PORT_NUMBER_2" \]
             --region=REGION
         

Replace the following:

     * `IP_ADDRESS`: the IP address for the endpoint
     * `PORT_NUMBER`: the port number for the endpoint

You can repeat this step to add up to 256 endpoints per NEG.




### Create the load balancer

###  Console 

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  5. For **Global or single region deployment** , select **Best for regional workloads** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

  1. Enter a **Load balancer name**.
  2. For **Region** , select REGION.
  3. For **Network** , select LB_NETWORK.



#### Reserve a proxy-only subnet

**Note:** If you already created the proxy-only subnet, the **Reserve subnet** button isn't displayed. You can skip this section and continue with the steps in the **Frontend configuration** section.

To reserve a proxy-only subnet:

  1. Click **Reserve subnet**.
  2. For **Name** , enter PROXY_ONLY_SUBNET_NAME.
  3. For **IP address range** , enter PROXY_ONLY_SUBNET_RANGE.
  4. Click **Add**.



#### Frontend configuration

  1. Click **Frontend configuration**.
  2. Enter a **Name**. 
  3. To create an **HTTPS load balancer** , you must have an SSL certificate. In this example, you create a Compute Engine SSL certificate.

Property | Value (type a value or select an option as specified)  
---|---  
Protocol | HTTPS  
IP version | IPv4  
IP address | Select the IP address reserved previously: LB_IP_ADDRESS.  
Port | 443  
Certificate |  For **Choose certificate repository** , select **Classic Certificates**. Select an existing SSL certificate or create a new certificate. To create an HTTPS load balancer, you must have an SSL certificate resource to use in the HTTPS proxy.  
  
If you want to test this process without setting up an SSL certificate resource (or a domain as required by Google-managed certificates), you can set up an HTTP load balancer.

To create an **HTTP** load balancer, verify that the following options are configured with these values:

Property | Value (type a value or select an option as specified)  
---|---  
Protocol | HTTP  
IP version | IPv4  
IP address | Select the IP address reserved previously: LB_IP_ADDRESS.  
Port | 80  
  4. Click **Done**.




#### Backend configuration

  1. Click **Backend configuration**.
  2. Click **Backend services and backend buckets**.
  3. Click **Create a backend service**.
  4. Enter a name.
  5. For **Backend type** , select **Internet network endpoint group**.
  6. For **Protocol** , select the protocol that you intend to use from the load balancer to the internet NEG.
  7. For **Backends** , in the **New backend** window, select the **Regional internet network endpoint group** created in the previous step.
  8. Click **Done**.
  9. Configure the health check: 
     1. For **Health check** , select **Create a health check**.
     2. Set the health check name to HTTP_HEALTH_CHECK_NAME.
     3. For **Protocol** , select **HTTP**.
     4. Set **Port** to `80`.
  10. Click **Create**.



#### Review and finalize

  1. Click **Review and finalize**.
  2. If everything looks correct, click **Create**.



###  gcloud 

  1. Optional: Create a health check. Health check probes for external backends use the [distributed Envoy health checks](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#health-checks) and are later NAT-translated. 
         
         gcloud compute health-checks create http HTTP_HEALTH_CHECK_NAME \
             --region=REGION \
             --use-serving-port
         

  2. Create a backend service: 
         
         gcloud compute backend-services create BACKEND_SERVICE \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --protocol=HTTP \
             --health-checks=HTTP_HEALTH_CHECK_NAME \
             --health-checks-region=REGION \
             --region=REGION
         

  3. Add the internet NEG to the backend service: 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE \
             --network-endpoint-group=INTERNET_NEG_NAME \
             --network-endpoint-group-region=REGION \
             --region=REGION
         

  4. Create a URL map to route incoming requests to the backend service: 
         
         gcloud compute url-maps create URL_MAP_NAME \
             --default-service=BACKEND_SERVICE \
             --region=REGION
         

  5. Optional: Perform this step if you are using HTTPS between the client and the load balancer. This step is not required for HTTP load balancers. 

You can create either Compute Engine or Certificate Manager certificates. Use any of the following methods to create certificates using Certificate Manager:

     * Regional self-managed certificates. For information about creating and using regional self-managed certificates, see [Deploy a regional self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional). Certificate maps aren't supported.
     * Regional Google-managed certificates. Certificate maps aren't supported.

The following types of regional Google-managed certificates are supported by Certificate Manager:

       * Regional Google-managed certificates with per-project DNS authorization. For more information, see [Deploy a regional Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-regional).
       * Regional Google-managed (private) certificates with Certificate Authority Service. For more information, see [Deploy a regional Google-managed certificate with Certificate Authority Service](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas-regional).

After you create certificates, attach the certificate directly to the target proxy.

To create a Compute Engine self-managed SSL certificate resource: 
    
    gcloud compute ssl-certificates create SSL_CERTIFICATE_NAME \
        --certificate CRT_FILE_PATH \
        --private-key KEY_FILE_PATH
    

  6. Create a target HTTP(S) proxy to route requests to your URL map.

For an HTTP load balancer, create an HTTP target proxy:
         
         gcloud compute target-http-proxies create TARGET_HTTP_PROXY_NAME \
             --url-map=URL_MAP_NAME \
             --region=REGION
         

For an HTTPS load balancer, create an HTTPS target proxy. The proxy is the portion of the load balancer that holds the SSL certificate for HTTPS Load Balancing, so you also load your certificate in this step.
         
         gcloud compute target-https-proxies create TARGET_HTTPS_PROXY_NAME \
             --ssl-certificates=SSL_CERTIFICATE_NAME \
             --url-map=URL_MAP_NAME \
             --region=REGION
         

  7. Create a forwarding rule to route incoming requests to the proxy.

For an HTTP load balancer:
         
         gcloud compute forwarding-rules create HTTP_FORWARDING_RULE_NAME \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --network-tier=STANDARD \
             --network=LB_NETWORK \
             --address=LB_IP_ADDRESS \
             --target-http-proxy=TARGET_HTTP_PROXY_NAME \
             --target-http-proxy-region=REGION \
             --region=REGION \
             --ports=80
         

For an HTTPS load balancer:
         
         gcloud compute forwarding-rules create HTTPS_FORWARDING_RULE_NAME \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --network-tier=STANDARD \
             --network=LB_NETWORK \
             --address=LB_IP_ADDRESS \
             --target-https-proxy=TARGET_HTTPS_PROXY_NAME \
             --target-https-proxy-region=REGION \
             --region=REGION \
             --ports=443
         




## Connect your domain to your load balancer

After the load balancer is created, note the IP address that is associated with the load balancer—for example, `30.90.80.100`. To point your domain to your load balancer, create an `A` record by using your domain registration service. If you added multiple domains to your SSL certificate, you must add an `A` record for each one, all pointing to the load balancer's IP address. For example, to create `A` records for `www.example.com` and `example.com`, use the following:
    
    
    NAME                  TYPE     DATA
    www                   A        30.90.80.100
    @                     A        30.90.80.100
    

If you use Cloud DNS as your DNS provider, see [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records).

## Test the load balancer

**Note:** It might take a few minutes for the load balancer configuration to propagate after you first deploy it.

Now that you have configured your load balancer, you can start sending traffic to the load balancer's IP address. If you configured a domain, you can send traffic to the domain name as well. However, DNS propagation can take time to complete, so you can start by using the IP address for testing.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the load balancer that you just created.

  3. Note the IP address of the load balancer.

  4. Send traffic to the load balancer.

     * If you created an **HTTP load balancer** , you can test your load balancer by going to `http://IP_ADDRESS`. Replace `IP_ADDRESS` with the load balancer's IP address. You should be directed to the application you're running on the external backend.

     * If you created an **HTTPS load balancer** , you can test your load balancer by going to `https://IP_ADDRESS`. Replace `IP_ADDRESS` with the load balancer's IP address. You should be directed to the application you're running on the external backend.

If that does not work and you are using a Google-managed certificate, confirm that your certificate resource's status is ACTIVE. For more information, see [Google-managed SSL certificate resource status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#certificate-resource-status).

Alternatively, you can use `curl` from your local machine's command line. Replace `IP_ADDRESS` with the load balancer's IPv4 address. If you're using a Google-managed certificate, test the domain that points to the load balancer's IP address. For example:
    
    curl -s 'https://www.example.com:443' --resolve www.example.com:443:IP_ADDRESS
    

  5. Optional: If you are using a custom domain, you might need to wait for the updated DNS settings to propagate. Then, test your domain in the web browser.

For help with troubleshooting, see [Troubleshooting external backend and internet NEG issues](https://docs.cloud.google.com/load-balancing/docs/https/troubleshooting-ext-https-lbs#external-backends-internet-neg).




## Additional configuration

This section expands on the configuration example to provide alternative and additional configuration options. All of the tasks are optional. You can perform them in any order.

### Use a custom header to authenticate requests

To authenticate requests sent to your external backend, you can set a custom header to indicate that the request came from a Google Cloud load balancer. You'll also need to configure the external backend to expect this custom header on traffic coming from Google Cloud.

To learn how to set up custom headers, see [Set up advanced traffic management](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt). 

For other authentication methods, see [Authenticate requests to the external backend](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#authenticate-requests).

### Enable IAP on the external Application Load Balancer

You can configure IAP to be enabled or disabled (default). If enabled, you must provide values for `oauth2-client-id` and `oauth2-client-secret`.

To enable IAP, update the backend service to include the `--iap=enabled` flag with the `oauth2-client-id` and `oauth2-client-secret`.

Optionally, you can [enable IAP](https://docs.cloud.google.com/iap/docs/enabling-compute-howto#enabling) for a Compute Engine resource by using the Google Cloud console, gcloud CLI, or API.

## What's next

  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
