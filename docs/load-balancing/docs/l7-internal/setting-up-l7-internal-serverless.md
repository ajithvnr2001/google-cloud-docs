---
url: https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless/
title: Set up a regional internal Application Load Balancer with Cloud Run \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:21.092164+00:00
---

# Set up a regional internal Application Load Balancer with Cloud Run  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional internal Application Load Balancer with Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to deploy a regional internal Application Load Balancer with Cloud Run. To set this up, you use a _serverless NEG_ backend for the load balancer.

Although this document describes a Cloud Run configuration, a serverless NEG for Cloud Run can point to either a Cloud Run resource or a Cloud Run functions (2nd gen) resource.

Before you try this procedure, make sure you are familiar with the following topics:

  * [Regional internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
  * [Serverless NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)



This document shows you how to configure an Application Load Balancer that proxies requests to a serverless NEG backend.

[Serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) let you use Cloud Run services with your load balancer. After you configure a load balancer with the serverless NEG backend, requests to the load balancer are routed to the Cloud Run backend.

## Before you begin

  1. Install the Google Cloud CLI
  2. Deploy a Cloud Run service
  3. Configure permissions



### Install Google Cloud SDK

Install the Google Cloud CLI tool. For conceptual and installation information about the gcloud CLI, see [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud).

If you haven't run the gcloud CLI previously, first run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to initialize your gcloud CLI directory.

### Deploy a Cloud Run service

The instructions on this page assume you already have a Cloud Run service running.

For the example on this page, you can use [any of the Cloud Run quickstarts](https://docs.cloud.google.com/run/docs/quickstarts) to deploy a Cloud Run service.

The serverless NEG, the load balancer, and any client VMs must be in the same region as the Cloud Run service. 

To prevent access to the Cloud Run service from the internet, [restrict network ingress to `internal`](https://docs.cloud.google.com/run/docs/securing/ingress). Traffic from the internal Application Load Balancer is considered _internal_ traffic.
    
    
    gcloud run deploy CLOUD_RUN_SERVICE_NAME \
        --platform=managed \
        --allow-unauthenticated \
        --ingress=internal \
        --region=REGION \
        --image=IMAGE_URL
    

Note the name of the service that you create. The rest of this page shows you how to set up a load balancer that routes requests to this service.

### Configure permissions

To follow this guide, you need to create a serverless NEG and create a load balancer in a project. You must be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you have the following [Compute Engine IAM roles and permissions](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required role  
---|---  
Create load balancer and networking components | [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)  
Create and modify NEGs | [Compute Instance Admin (v1)](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin) (`roles/compute.instanceAdmin.v1`)  
Create and modify SSL certificates | [Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) (`roles/iam.securityAdmin`)  
  
## Configure the network and subnets

To configure the network and its subnets, perform the following tasks:

  * Create a Virtual Private Cloud (VPC) network and subnet.
  * Create a proxy-only subnet.



### Create the VPC network

Create a custom mode VPC network, then the subnets that you want within a region.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. For **Subnet creation mode** , select **Custom**.

  5. In the **New subnet** section, specify the following configuration parameters for a subnet:

     1. For **Name** , enter `lb-subnet`.
     2. Select a **Region**.
     3. For **IP address range** , enter `10.1.2.0/24`.
     4. Click **Done**.
  6. Click **Create**.




###  gcloud 

  1. Create the custom VPC network by using the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create):
         
         gcloud compute networks create lb-network --subnet-mode=custom
         

  2. Create a subnet in the `lb-network` network. This example uses an IP address range of `10.1.2.0/24` for the subnet. You can configure any [valid subnet range](https://docs.cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges).
         
         gcloud compute networks subnets create lb-subnet \
             --network=lb-network \
             --range=10.1.2.0/24 \
             --region=REGION
         




### Create a proxy-only subnet

Create a proxy-only subnet for all [regional Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets#envoy-lb) in a specific region of the `lb-network` network.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the Shared VPC network that you want to add the proxy-only subnet to.

  3. Click **Add subnet**.

  4. In the **Name** field, enter `proxy-only-subnet`.

  5. Select a **Region**.

  6. Set **Purpose** to **Regional Managed Proxy**.

  7. Enter an **IP address range** as `10.129.0.0/23`.

  8. Click **Add**.




###  gcloud 

Create the proxy-only subnet by using the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).

This example uses an IP address range of `10.129.0.0/23` for the proxy-only subnet. You can configure any [valid subnet range](https://docs.cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges).
    
    
      gcloud compute networks subnets create proxy-only-subnet \
          --purpose=REGIONAL_MANAGED_PROXY \
          --role=ACTIVE \
          --region=REGION \
          --network=lb-network \
          --range=10.129.0.0/23
    

## Create the load balancer

In the following diagram, the load balancer uses a serverless NEG backend to direct requests to a serverless Cloud Run service.

Traffic going from the load balancer to the serverless NEG backends uses special routes defined outside your VPC that aren't subject to firewall rules. Therefore, if your load balancer only has serverless NEG backends, you don't need to create firewall rules to allow traffic from the proxy-only subnet to the serverless backend.

[ ![Internal HTTP or HTTPS load balancing architecture for a Cloud Run application.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-int-https.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-int-https.svg) Internal HTTP or HTTPS load balancing architecture for a Cloud Run application (click to enlarge).

### Console

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Internal** and click **Next**.
  5. For **Cross-region or single region deployment** , select **Best for regional workloads** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

  1. For the name of the load balancer, enter `serverless-lb`.
  2. Select the **Network** as `lb_network`.
  3. Keep the window open to continue.



#### Configure the frontend

  1. Before you proceed, make sure you have an [SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates).
  2. Click **Frontend configuration**.
  3. Enter a **Name**.
  4. To configure an internal Application Load Balancer, fill in the fields as follows.
     1. For **Protocol** , select **HTTPS**.
     2. For **Subnetwork** , select the subnetwork.
     3. For **IP version** , select **IPv4**.
     4. For **IP address** , select **Ephemeral**.
     5. For **Port** , select `443`.
     6. For **Choose certificate repository** , select **Classic Certificates**.

The following example shows you how to create Compute Engine SSL certificates:

     7. Click **Create a new certificate**.
        1. In the **Name** field, enter a name.
        2. In the appropriate fields, upload your PEM-formatted files: 
           * **Certificate**
           * **Private key**
        3. Click **Create**.

If you want to test this process without setting up an SSL certificate resource, you can set up an HTTP load balancer. 

  5. Optional: To create an HTTP load balancer, do the following:
     1. For **Protocol** , select **HTTP**.
     2. For **Subnetwork** , select the subnetwork.
     3. For **IP version** , select **IPv4**.
     4. For **IP address** , select **Ephemeral**.
     5. For **Port** , select `80`.
  6. Click **Done**.



#### Configure the backend services

  1. Click **Backend configuration**.
  2. In the **Create or select backend services** menu, hold the pointer over **Backend services** , and then select **Create a backend service**. 
  3. In the **Create a backend service** window, enter a **Name**.
  4. For **Backend type** , select **Serverless network endpoint group**.
  5. Leave **Protocol** unchanged. This parameter is ignored.
  6. For **Backends > New backend**, select **Create serverless network endpoint group**. 
     1. In the **Create serverless network endpoint group** window, enter a **Name**.
     2. For **Region** , the region of the load balancer is displayed.
     3. From the **Serverless network endpoint group type** field, select **Cloud Run**. Cloud Run is the only supported type.
     4. Select **Select service name**.
     5. From the **Service** list, select the Cloud Run service that you want to create a load balancer for. 
     6. Click **Done**.
     7. Click **Create**.
  7. Optional: Configure a default backend security policy. The default security policy throttles traffic over a user-configured threshold. For more information about default security policies, see the [Rate limiting overview](https://docs.cloud.google.com/armor/docs/rate-limiting-overview#default-policy).

     1. To opt out of the Cloud Armor default security policy, select `None` in the **Cloud Armor backend security policy** list.
     2. To configure the Cloud Armor default security policy, select **Default security policy** in the **Cloud Armor backend security policy** list.
     3. In the **Policy name** field, accept the automatically generated name or enter a name for your security policy.
     4. In the **Request count** field, accept the default request count or enter an integer between `1` and `10,000`.
     5. In the **Interval** field, select an interval.
     6. In the **Enforce on key** field, choose one of the following values: **All** , **IP address** , or **X-Forwarded-For IP address**. For more information about these options, see [Identifying clients for rate limiting](https://docs.cloud.google.com/armor/docs/rate-limiting-overview#identifying_clients_for_rate_limiting).
  8. In the **Create backend service** window, click **Create**.



#### Configure routing rules

Routing rules determine how your traffic is directed. You can direct traffic to a backend service or a Kubernetes service. Any traffic not explicitly matched with a host and path matcher is sent to the default service. 

  1. Click **Simple host and path rule**.
  2. Select a backend service from the **Backend** list.



#### Review the configuration

  1. Click **Review and finalize**.
  2. Review the values for **Backend** , **Host and Path rules** and **Frontend**.
  3. Optional: Click **Equivalent Code** to view the REST API request that will be used to create the load balancer.
  4. Click **Create**. Wait for the load balancer to be created. 
  5. Click the name of the load balancer (**serverless-lb**).
  6. Note the IP address of the load balancer for the next task. 

When you use the Google Cloud console to create an HTTP(S) load balancer with a serverless NEG backend, logging is enabled by default. You can use the [ `gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) to disable logging if needed. 

### gcloud

  1. Create a serverless NEG for your Cloud Run service: 
         
         gcloud compute network-endpoint-groups create SERVERLESS_NEG_NAME \
                 --region=REGION \
                 --network-endpoint-type=serverless  \
                 --cloud-run-service=CLOUD_RUN_SERVICE_NAME
             

  2. Create a regional backend service. Set the `--protocol` to HTTP. This parameter is ignored but it is required because the `--protocol` otherwise defaults to TCP. 
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
                 --load-balancing-scheme=INTERNAL_MANAGED \
                 --protocol=HTTP \
                 --region=REGION
             

  3. Add the serverless NEG as a backend to the backend service: 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
                 --region=REGION \
                 --network-endpoint-group=SERVERLESS_NEG_NAME \
                 --network-endpoint-group-region=REGION
             

  4. Create a regional URL map to route incoming requests to the backend service: 
         
         gcloud compute url-maps create URL_MAP_NAME \
                 --default-service=BACKEND_SERVICE_NAME \
                 --region=REGION
             

This example URL map only targets one backend service representing a single serverless app, so you don't need to set up host rules or path matchers. 
  5. Optional: Perform this step if you are using HTTPS between the client and the load balancer. This step isn't required for HTTP load balancers. 

You can create either Compute Engine or Certificate Manager certificates. Use any of the following methods to create certificates using Certificate Manager:

     * Regional self-managed certificates. For information about creating and using regional self-managed certificates, see [Deploy a regional self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional). Certificate maps aren't supported.
     * Regional Google-managed certificates. Certificate maps aren't supported.

The following types of regional Google-managed certificates are supported by Certificate Manager:

       * Regional Google-managed certificates with per-project DNS authorization. For more information, see [Deploy a regional Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-regional).
       * Regional Google-managed (private) certificates with Certificate Authority Service. For more information, see [Deploy a regional Google-managed certificate with Certificate Authority Service](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas-regional).

After you create certificates, attach the certificate directly to the target proxy.

To create a regional self-managed SSL certificate resource: 
    
    gcloud compute ssl-certificates create SSL_CERTIFICATE_NAME \
            --certificate CRT_FILE_PATH \
            --private-key KEY_FILE_PATH \
            --region=REGION
        

  6. Create a regional target proxy to route requests to the URL map.  
  
For an HTTP load balancer, create an HTTP target proxy: 
         
         gcloud compute target-http-proxies create TARGET_HTTP_PROXY_NAME \
                 --url-map=URL_MAP_NAME \
                 --region=REGION
             

For an HTTPS load balancer, create an HTTPS target proxy. The proxy is the portion of the load balancer that holds the SSL certificate for HTTPS Load Balancing, so you also load your certificate in this step. 
         
         gcloud compute target-https-proxies create TARGET_HTTPS_PROXY_NAME \
                 --ssl-certificates=SSL_CERTIFICATE_NAME \
                 --url-map=URL_MAP_NAME \
                 --region=REGION
             

  7. Create a forwarding rule to route incoming requests to the proxy. Don't use the proxy-only subnet for the forwarding rule IP address. You can configure any valid IP address from the subnet (`lb-subnet`).  
  
For an HTTP load balancer: 
         
         gcloud compute forwarding-rules create HTTP_FORWARDING_RULE_NAME \
                 --load-balancing-scheme=INTERNAL_MANAGED \
                 --network=lb-network \
                 --subnet=lb-subnet \
                 --target-http-proxy=TARGET_HTTP_PROXY_NAME \
                 --target-http-proxy-region=REGION \
                 --region=REGION \
                 --ports=80
             

For an HTTPS load balancer: 
         
         gcloud compute forwarding-rules create HTTPS_FORWARDING_RULE_NAME \
                 --load-balancing-scheme=INTERNAL_MANAGED \
                 --network=lb-network \
                 --subnet=lb-subnet \
                 --target-https-proxy=TARGET_HTTPS_PROXY_NAME \
                 --target-https-proxy-region=REGION \
                 --region=REGION \
                 --ports=443
             




## Test the load balancer

Now that you have configured your load balancer, you can start sending traffic to the load balancer's IP address.

### Create a client VM

This example creates a client VM (`vm-client`) in the same region as the load balancer. The client is used to validate the load balancer's configuration and demonstrate expected behavior.

###  gcloud 

The client VM can be in any zone in the same region as the load balancer, and it can use any subnet in the same VPC network.
    
    
    gcloud compute instances create vm-client \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=allow-ssh \
        --network=lb-network \
        --subnet=lb-subnet \
        --zone=ZONE
    

### Configure the firewall rule

This example requires the following firewall rule for the test client VM:

**`fw-allow-ssh`.** An ingress rule, applicable to the test client VM, that allows incoming SSH connectivity on TCP port `22` from any address. You can choose a more restrictive source IP address range for this rule; for example, you can specify just the IP address ranges of the system from which you initiate SSH sessions. This example uses the target tag `allow-ssh`.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.   
[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)
  2. Click **Create firewall rule** to create the rule to allow incoming SSH connections: 
     * **Name** : `allow-ssh`
     * **Network** : `lb-network`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-ssh`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `0.0.0.0/0`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `22` for the port number.
  3. Click **Create**.



###  gcloud 

Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`. When you omit `source-ranges`, Google Cloud [interprets the rule to mean any source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule).
    
    
    gcloud compute firewall-rules create fw-allow-ssh \
      --network=lb-network \
      --action=allow \
      --direction=ingress \
      --target-tags=allow-ssh \
      --rules=tcp:22
    

### Send traffic to the load balancer

It might take a few minutes for the load balancer configuration to propagate after you first deploy it.

  * Connect to the client instance using SSH.
        
        gcloud compute ssh vm-client \
          --zone=ZONE
        

  * Verify that the load balancer is serving the Cloud Run service homepage as expected.

For HTTP testing, run:
        
        curl IP_ADDRESS
        

For HTTPS testing, run:
        
        curl -k -s 'https://TEST_DOMAIN_URL:443' --connect-to TEST_DOMAIN_URL:443:IP_ADDRESS:443
        

Replace `TEST_DOMAIN_URL` with the domain associated with your application. For example, `test.example.com`.

The `-k` flag causes curl to skip certificate validation. 




## Additional configuration options

This section expands on the configuration example to provide alternative and additional configuration options. All of the tasks are optional. You can perform them in any order.

### Using a URL mask

When creating a serverless NEG, instead of selecting a specific Cloud Run service, you can use a URL mask to point to multiple services serving at the same domain. A URL mask is a template of your URL schema. The serverless NEG uses this template to extract the service name from the incoming request's URL and map the request to the appropriate service.

URL masks are particularly useful if your service is [mapped to a custom domain](https://docs.cloud.google.com/run/docs/mapping-custom-domains) rather than to the default address that Google Cloud provides for the deployed service. A URL mask lets you target multiple services and versions with a single rule even when your application is using a custom URL pattern.

If you haven't already done so, make sure you read the [Serverless NEGS overview: URL Masks](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#url_masks).

#### Construct a URL mask

To construct a URL mask for your load balancer, start with the URL of your service. This example uses a sample serverless app running at `https://example.com/login`. This is the URL where the app's `login` service is served.

  1. Remove the `http` or `https` from the URL. You are left with `example.com/login`.
  2. Replace the service name with a placeholder for the URL mask. 
     * Cloud Run: Replace the Cloud Run service name with the placeholder `<service>`. If the Cloud Run service has a tag associated with it, replace the tag name with the placeholder `<tag>`. In this example, the URL mask you are left with is `example.com/<service>`.
  3. Optional: If the service name can be extracted from the path portion of the URL, the domain can be omitted. The path part of the URL mask is distinguished by the first slash (`/`) character. If a slash (`/`) is not present in the URL mask, the mask is understood to represent the host only. Therefore, for this example, the URL mask can be reduced to `/<service>`.

Similarly, if `<service>` can be extracted from the host part of the URL, you can omit the path altogether from the URL mask.

You can also omit any host or subdomain components that come before the first placeholder as well as any path components that come after the last placeholder. In such cases, the placeholder captures the required information for the component.




Here are a few more examples that demonstrate these rules:

This table assumes that you have a custom domain called `example.com` and all your Cloud Run services are being [mapped to this domain](https://docs.cloud.google.com/run/docs/mapping-custom-domains).

Service, Tag name | Cloud Run custom domain URL | URL mask  
---|---|---  
service: login | https://login-home.example.com/web | <service>-home.example.com  
service: login | https://example.com/login/web | example.com/<service> or /<service>  
service: login, tag: test | https://test.login.example.com/web | <tag>.<service>.example.com  
service: login, tag: test | https://example.com/home/login/test | example.com/home/<service>/<tag> or /home/<service>/<tag>  
service: login, tag: test | https://test.example.com/home/login/web | <tag>.example.com/home/<service>  
  
#### Creating a serverless NEG with a URL mask

###  Console 

For a new load balancer, you can use the same end-to-end process as described previously in this document. When configuring the backend service, instead of selecting a specific service, enter a URL mask.

If you have an existing load balancer, you can edit the backend configuration and have the serverless NEG point to a URL mask instead of a specific service.

To add a URL mask-based serverless NEG to an existing backend service, do the following: 

  1. In the Google Cloud console, go to the **Load balancing** page.  
[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/)
  2. Click the name of the load balancer that has the backend service you want to edit.
  3. On the **Load balancer details** page, click edit**Edit**.
  4. On the **Edit global external Application Load Balancer** page, click **Backend configuration**.
  5. On the **Backend configuration** page, click edit**Edit** for the backend service you want to modify.
  6. Click **Add backend**.
  7. Select **Create Serverless network endpoint group**.
     1. For the **Name** , enter `helloworld-serverless-neg`.
     2. Under **Region** , the region of the load balancer is displayed.
     3. Under **Serverless network endpoint group type** , **Cloud Run** is the only supported network endpoint group type. 
        1. Select **Use URL Mask**.
        2. Enter a URL mask. For information about how to create a URL mask, see Constructing a URL mask.
        3. Click **Create**.

  8. In the **New backend** , click **Done**.
  9. Click **Update**.



###  gcloud 

To create a serverless NEG with a sample URL mask of `example.com/<service>`:
    
    
    gcloud compute network-endpoint-groups create SERVERLESS_NEG_MASK_NAME \
        --region=REGION \
        --network-endpoint-type=serverless \
        --cloud-run-url-mask="example.com/<service>"
    

### Update client HTTP keepalive timeout

The load balancer created in the previous steps has been configured with a default value for the [client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/l7-internal#http-keepalive-timeout). 

To update the client HTTP keepalive timeout, use the following instructions.

### Console

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/add).

  2. Click the name of the load balancer that you want to modify.
  3. Click edit**Edit**.
  4. Click **Frontend configuration**.
  5. Expand **Advanced features**. For **HTTP keepalive timeout** , enter a timeout value.
  6. Click **Update**.
  7. To review your changes, click **Review and finalize** , and then click **Update**.



### gcloud

For an HTTP load balancer, update the target HTTP proxy by using the [`gcloud compute target-http-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update).
    
    
          gcloud compute target-http-proxies update TARGET_HTTP_PROXY_NAME \
              --http-keep-alive-timeout-sec=HTTP_KEEP_ALIVE_TIMEOUT_SEC \
              --region=REGION
          

For an HTTPS load balancer, update the target HTTPS proxy by using the [`gcloud compute target-https-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update).
    
    
          gcloud compute target-https-proxies update TARGET_HTTP_PROXY_NAME \
              --http-keep-alive-timeout-sec=HTTP_KEEP_ALIVE_TIMEOUT_SEC \
              --region REGION
          

Replace the following:

  * `TARGET_HTTP_PROXY_NAME`: the name of the target HTTP proxy.
  * `TARGET_HTTPS_PROXY_NAME`: the name of the target HTTPS proxy.
  * `HTTP_KEEP_ALIVE_TIMEOUT_SEC`: the HTTP keepalive timeout value from 5 to 600 seconds.



## Deleting a serverless NEG

A network endpoint group cannot be deleted if it is attached to a backend service. Before you delete a NEG, ensure that it is detached from the backend service.

###  Console 

  1. To make sure the serverless NEG you want to delete is not in use by any backend service, go to the **Backend services** tab on the **Load balancing components** page.  
[Go to Backend services](https://console.cloud.google.com/networking/loadbalancing/advanced/backendServices/list)
  2. If the serverless NEG is in use, do the following:
     1. Click the name of the backend service that is using the serverless NEG.
     2. Click edit**Edit**.
     3. From the list of **Backends** , click delete to remove the serverless NEG backend from the backend service.
     4. Click **Save**.

  3. Go to the **Network endpoint group** page in the Google Cloud console.  
[Go to Network endpoint group](https://console.cloud.google.com/compute/networkendpointgroups/list)
  4. Select the checkbox for the serverless NEG you want to delete.
  5. Click **Delete**.
  6. Click **Delete** again to confirm.



###  gcloud 

To remove a serverless NEG from a backend service, you must specify the region where the NEG was created.
    
    
    gcloud compute backend-services remove-backend BACKEND_SERVICE_NAME \
        --network-endpoint-group=SERVERLESS_NEG_NAME \
        --network-endpoint-group-region=REGION \
        --region=REGION
    

To delete the serverless NEG:
    
    
    gcloud compute network-endpoint-groups delete SERVERLESS_NEG_NAME \
        --region=REGION
    

## What's next

  * [Deploy a regional internal Application Load Balancer with Cloud Run by using Terraform](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/v43.0.0/blueprints/serverless/cloud-run-corporate)
  * [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup)
  * [Deprovision Shared VPC](https://docs.cloud.google.com/vpc/docs/deprovisioning-shared-vpc)
  * [Regional internal Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring)
  * [Troubleshoot issues with regional internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/troubleshooting-l7-ilb)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
