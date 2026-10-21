---
url: https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-external-backend/
title: Set up a global external Application Load Balancer with an external backend \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:41:59.650982+00:00
---

# Set up a global external Application Load Balancer with an external backend  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-external-backend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a global external Application Load Balancer with an external backend Stay organized with collections  Save and categorize content based on your preferences. 

This guide uses an example to teach the fundamentals of using an external backend (sometimes called a _custom origin_) with a global external Application Load Balancer. An external backend is an endpoint that is external to Google Cloud. When you use an external backend with a global external Application Load Balancer, you can improve performance by using Cloud CDN caching.

The guide shows you how to configure a global external Application Load Balancer with a Cloud CDN-enabled backend service that proxies requests to an external backend server.

Before following this guide, familiarize yourself with the [Internet NEG overview](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts) documentation, including the [limitations](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#limitations). 

The following architecture diagram shows a global external Application Load Balancer frontend with an external backend.

[ ![A global external Application Load Balancer with an external backend.](https://docs.cloud.google.com/static/load-balancing/images/internet-neg-external-backend.svg)](https://docs.cloud.google.com/static/load-balancing/images/internet-neg-external-backend.svg) **Figure 1.** A global external Application Load Balancer with an external backend (click to enlarge).

## Permissions

To follow this guide, you need to create an internet NEG and create or modify an external Application Load Balancer in a project. You should be either a project [Owner or Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner` or `roles/editor`), or you should have both of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam).

Task | Required role  
---|---  
Create and modify load balancer components | [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
(`roles/compute.networkAdmin`)   
Create and modify NEGs | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
(`roles/compute.instanceAdmin`)   
  
## Optional: Use BYOIP addresses

With bring your own IP (BYOIP), you can import your own public addresses to Google Cloud to use the addresses with Google Cloud resources. For example, if you import your own IPv4 addresses, you can assign one to the forwarding rule when you configure your load balancer. When you follow the instructions in this document to [create the load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-external-backend#create_the_load_balancer), provide the BYOIP address as the **IP address**.

For more information about using BYOIP, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

## Set up your external backend environment outside Google Cloud

To set up your environment, see the following sections.

### Configure network endpoints

Configure a network endpoint to expose your external backend to Google Cloud. Make sure that the endpoint—either an IP:Port combination or a fully-qualified domain name (FQDN) and port—is reachable over the internet. This endpoint is later referenced from the internet NEG.

For detailed configuration requirements for internet NEG endpoints, see the [Internet NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts).

### Allow the external backend to receive traffic from Google Cloud

To allow requests from Google Cloud to reach your external backend, you must allowlist the IP address ranges that Google uses to send requests to external backends. To look up the IP addresses that need to be allowed to send traffic to your external backends, query the `_cloud-eoips.googleusercontent.com` DNS TXT record by using a tool such as `dig` or `nslookup`.

Examples:

  * Run the following `nslookup` command:
        
        nslookup -q=TXT _cloud-eoips.googleusercontent.com 8.8.8.8
        

The output looks like the following:
        
        Non-authoritative answer:
        _cloud-eoips.googleusercontent.com    text = "v=spf1 ip4:34.96.0.0/20 ip4:34.127.192.0/18 ~all"
        

Note the CIDR ranges following `ip4:` and ensure that these ranges are allowed by the firewall rules or cloud access control lists (ACLs) configured on your external backend.

  * Run the following `dig` command:
        
        dig TXT _cloud-eoips.googleusercontent.com | grep -Eo 'ip4:[^ ]+' | cut -d':' -f2
        

The output contains two IP address ranges, as follows:
        
        34.96.0.0/20
        34.127.192.0/18
        


**Caution:** These IP address ranges are subject to change. Make sure that you always confirm the Google Cloud IP address ranges that send traffic to your external backends.

## Set up your Google Cloud environment

Create the global external Application Load Balancer with an internet NEG backend.

### Reserve an external IP address

Reserve a global static external IP address that clients use to reach your application.

**Note:** This step is required for this example, and recommended in general. Reserving an IP address is also essential if you are using a custom domain for your external backend (also required for Google-managed SSL certificates). With a custom domain, you must update your DNS records to point your domain to this IP address.

###  Console 

  1. In the Google Cloud console, go to the **External IP addresses** page.

[Go to External IP addresses](https://console.cloud.google.com/addresses/list)

  2. Click **Reserve external static address** to reserve an IPv4 address.

  3. Enter a name.

  4. For **Network Service Tier** , select **Premium**.

  5. For **IP version** , select **IPv4**.

  6. For **Type** , select **Global**.

  7. Click **Reserve**.




###  gcloud 
    
    
    gcloud compute addresses create LB_IP_ADDRESS_NAME \
        --network-tier=PREMIUM \
        --ip-version=IPV4 \
        --global
    

Note the IPv4 address that was reserved:
    
    
    gcloud compute addresses describe LB_IP_ADDRESS_NAME \
        --format="get(address)" \
        --global
    

### Set up the internet NEG

###  Console 

  1. In the Google Cloud console, go to the **Network endpoint groups** page.

[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click **Create network endpoint group**.

  3. Enter a name.

  4. For **Network endpoint group type** , select **Network endpoint group (Internet)**.

  5. For **Default port** , enter `443`.

  6. For **New network endpoint** , select **Fully qualified domain name and port**.

  7. Enter the **Fully qualified domain name**.

  8. For **Port type** , select **Default** , and verify that **Port number** is `443`.

  9. Click **Create**.




###  gcloud 

  1. Create an internet NEG, and set the `--network-endpoint-type` to `internet-fqdn-port` (the hostname and port where your external backend can be reached):
         
         gcloud compute network-endpoint-groups create INTERNET_NEG_NAME \
             --network-endpoint-type="internet-fqdn-port" \
             --global
         

  2. Add your endpoint to the NEG. If a port isn't specified, the port selection defaults to port `80` (HTTP) or `443` (HTTPS; HTTP/2) depending on the protocol configured in the backend service. Make sure to include the `--global` flag:
         
         gcloud compute network-endpoint-groups update INTERNET_NEG_NAME \
             --add-endpoint="fqdn=FULLY_QUALIFIED_DOMAIN_NAME,port=443" \
             --global
         




### Set up an SSL certificate resource

To create the load balancer, you must have an [SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) that can be attached to the target proxy. The SSL certificate resource can be either a certificate map or a Compute Engine SSL certificate (classic certificate).

#### Certificate map

You can create a certificate map as described in one of the following documents:

  * [Deploy a global Google-managed certificate with load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-lb-auth)
  * [Deploy a global Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth)
  * [Deploy a global Google-managed certificate with Certificate Authority Service](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas)
  * [Deploy a global self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed)



#### Compute Engine SSL certificate

For an HTTPS load balancer, create a Compute Engine SSL certificate resource as described in one of the following documents:

  * [Use self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs)
  * [Use Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)



We recommend using a Google-managed certificate.

**Warning:** Don't use a self-signed certificate for production purposes.

### Create the load balancer

###  Console 

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  5. For **Global or single region deployment** , select **Best for global workloads** and click **Next**.
  6. For **Load balancer generation** , select **Global external Application Load Balancer** and click **Next**.
  7. Click **Configure**.



#### Frontend configuration

  1. Click **Frontend configuration**.
  2. Enter a name.
  3. To create an **HTTPS load balancer** , you must have an SSL certificate. We recommend using a Google-managed certificate.

Verify that the following options are configured with these values. 

Property | Value (type a value or select an option as specified)  
---|---  
Protocol | HTTPS  
Network Service Tier | Premium  
  
IP version | IPv4  
IP address | Select the IP address created in the Reserve an external IP address step.  
Port | 443  
Optional: HTTP keepalive timeout | Enter a timeout value from 5 to 1200 seconds. The default value is 610 seconds.  
Certificate |  For **Choose certificate repository** , select **Use certificate map** or **Use classic certificates**. Depending on your selection, select a certificate map or a classic certificate.   
Optional: Enable HTTP to HTTPS Redirect | Use this checkbox to enable HTTP to HTTPS redirects. Enabling this checkbox creates an additional partial HTTP load balancer that uses the same IP address as your HTTPS load balancer and redirects HTTP requests to your load balancer's HTTPS frontend. This checkbox can only be selected when the HTTPS protocol is selected and a reserved IP address is used.  
  
If you want to test this process without setting up an SSL certificate resource (or a domain as required by Google-managed certificates), you can set up an HTTP load balancer.

**To create an**HTTP** load balancer**, verify that the following options are configured with these values:

Property | Value (type a value or select an option as specified)  
---|---  
Protocol | HTTP  
Network Service Tier | Premium  
IP version | IPv4  
IP address | Select the IP address created in the Reserve an external IP address step.  
Port | 80  
Optional: HTTP keepalive timeout | Enter a timeout value from 5 to 1200 seconds. The default value is 610 seconds.  
  4. Click **Done**.




#### Backend configuration

  1. Click **Backend configuration**.
  2. Click **Backend services and backend buckets**.
  3. Click **Create a backend service**.
  4. Enter a name.
  5. For **Backend type** , select **Internet network endpoint group**.
  6. For **Protocol** , select the protocol that you intend to use from the load balancer to the internet NEG. For this example, select **HTTP/2**.
  7. For **Backends** , in the **New backend** window, select the internet NEG created in the previous step.
  8. Click **Create**.



#### Review and finalize

  1. Click **Review and finalize**.
  2. If everything looks correct, click **Create**.



###  gcloud 

  1. Create a backend service: 
         
         gcloud compute backend-services create BACKEND_SERVICE \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --global
           

  2. Add the internet NEG to the backend service: 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE \
               --network-endpoint-group=INTERNET_NEG_NAME \
               --global-network-endpoint-group \
               --global
            

  3. Create a URL map to route incoming requests to the backend service: 
         
         gcloud compute url-maps create URL_MAP_NAME \
               --default-service=BACKEND_SERVICE \
               --global
           

  4. _Perform this step only if you want to create an HTTPS load balancer._ This step is not required for HTTP load balancers.

To create an HTTPS load balancer, you must have an [SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) to use in the HTTPS target proxy. You can create an SSL certificate resource by using either a Google-managed SSL certificate or a self-managed SSL certificate. We recommend using Google-managed certificates because Google Cloud obtains, manages, and renews these certificates automatically.

To create a Google-managed certificate, [you must have a domain](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#before_you_begin). If you don't have a domain, you can use a self-managed SSL certificate for testing.

To create a Google-managed SSL certificate resource: 
         
         gcloud compute ssl-certificates create SSL_CERTIFICATE_NAME \
               --domains DOMAIN
           

To create a self-managed SSL certificate resource: 
         
         gcloud compute ssl-certificates create SSL_CERTIFICATE_NAME \
               --certificate CRT_FILE_PATH \
               --private-key KEY_FILE_PATH
           

  5. Create a target HTTP(S) proxy to route requests to your URL map.

For an HTTP load balancer, create an HTTP target proxy:
         
         gcloud compute target-http-proxies create TARGET_HTTP_PROXY_NAME \
               --url-map=URL_MAP_NAME \
               --global
           

For an HTTPS load balancer, create an HTTPS target proxy. The proxy is the portion of the load balancer that holds the SSL certificate for HTTPS Load Balancing, so you also load your certificate in this step.
         
         gcloud compute target-https-proxies create TARGET_HTTPS_PROXY_NAME \
               --ssl-certificates=SSL_CERTIFICATE_NAME \
               --url-map=URL_MAP_NAME \
               --global
           

Replace the following:

     * `TARGET_HTTP_PROXY_NAME`: the name of the target HTTP proxy.
     * `TARGET_HTTPS_PROXY_NAME`: the name of the target HTTPS proxy.
     * `SSL_CERTIFICATE_NAME`: the name of the SSL certificate.
     * `URL_MAP_NAME`: the name of the URL map.
Optional: For global external Application Load Balancers, you can set an [client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/https#http-keepalive-timeout) by using the `--http-keep-alive-timeout-sec` option. The timeout value must be between 5 to 1200 seconds. The default value is 610 seconds. 
  6. Create a forwarding rule to route incoming requests to the proxy.

For an HTTP load balancer:
         
         gcloud compute forwarding-rules create HTTP_FORWARDING_RULE_NAME \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --network-tier=PREMIUM \
               --address=LB_IP_ADDRESS_NAME \
               --target-http-proxy=TARGET_HTTP_PROXY_NAME \
               --global \
               --ports=80
           

For an HTTPS load balancer:
         
         gcloud compute forwarding-rules create HTTPS_FORWARDING_RULE_NAME \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --network-tier=PREMIUM \
               --address=LB_IP_ADDRESS_NAME \
               --target-https-proxy=TARGET_HTTPS_PROXY_NAME \
               --global \
               --ports=443
           




## Connect your domain to your load balancer

After the load balancer is created, note the IP address that is associated with the load balancer—for example, `30.90.80.100`. To point your domain to your load balancer, create an `A` record by using your domain registration service. If you added multiple domains to your SSL certificate, you must add an `A` record for each one, all pointing to the load balancer's IP address. For example, to create `A` records for `www.example.com` and `example.com`, use the following:
    
    
    NAME                  TYPE     DATA
    www                   A        30.90.80.100
    @                     A        30.90.80.100
    

If you use Cloud DNS as your DNS provider, see [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records).

## Test the load balancer

**Note:** It might take a few minutes for the load balancer configuration to propagate globally after you first deploy it.

Now that you have configured your load balancer, you can start sending traffic to the load balancer's IP address. If you configured a domain, you can send traffic to the domain name as well. However, DNS propagation can take time to complete, so you can start by using the IP address for testing.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the load balancer that you just created.

  3. Note the IP address of the load balancer.

  4. Send traffic to the load balancer.

     * If you created an **HTTP load balancer** , you can test your load balancer by going to `http://IP_ADDRESS`. Replace `IP_ADDRESS` with the load balancer's IP address. You should be directed to the application you're running on the external backend.

     * If you created an **HTTPS load balancer** , you can test your load balancer by going to `https://IP_ADDRESS`. Replace `IP_ADDRESS` with the load balancer's IP address. You should be directed to the you're application running on the external backend.

If that does not work and you are using a Google-managed certificate, confirm that your certificate resource's status is ACTIVE. For more information, see [Google-managed SSL certificate resource status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#certificate-resource-status).

Alternatively, you can use `curl` from your local machine's command line. Replace `IP_ADDRESS` with the load balancer's IPv4 address. If you're using a Google-managed certificate, test the domain that points to the load balancer's IP address. For example: 
    
    curl -s 'https://www.example.com:443' --resolve www.example.com:443:IP_ADDRESS
    

  5. Optional: If you are using a custom domain, you might need to wait for the updated DNS settings to propagate. Then, test your domain in the web browser.

For help with troubleshooting, see [Troubleshooting external backend and internet NEG issues](https://docs.cloud.google.com/load-balancing/docs/https/troubleshooting-ext-https-lbs#external-backends-internet-neg).




## Additional configuration

This section expands on the configuration example to provide alternative and additional configuration options. All of the tasks are optional. You can perform them in any order.

### Enable Cloud CDN

When Cloud CDN is enabled, the external Application Load Balancer sends requests to the internet NEG backend only when there is a Cloud CDN cache miss.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/add).

  2. Click the name of the load balancer that you want to modify.

  3. Click edit**Edit**.

  4. Click **Backend configuration**.

  5. For the backend service with the internet NEG backend, click edit**Edit**.

  6. Select **Enable Cloud CDN**.

  7. Optional: Modify the [cache mode](https://docs.cloud.google.com/cdn/docs/using-cache-modes) and [TTL](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides) settings.

  8. Click **Update**.

  9. To review your changes, click **Review and finalize** , and then click **Update**.




###  gcloud 

  * To enable Cloud CDN on the backend service, use the following command: 
        
        gcloud compute backend-services update BACKEND_SERVICE \
              --load-balancing-scheme=EXTERNAL_MANAGED \
              --global \
              --enable-cdn \
              --cache-mode=CACHE_MODE
          

Set the [cache mode](https://docs.cloud.google.com/cdn/docs/using-cache-modes) by replacing `CACHE_MODE` with one of the following:

    * `CACHE_All_STATIC`: automatically caches [static content](https://docs.cloud.google.com/cdn/docs/caching#static).
    * `USE_ORIGIN_HEADERS` (default): requires the origin to set [valid caching headers](https://docs.cloud.google.com/cdn/docs/caching#cacheability) to cache content.
    * `FORCE_CACHE_ALL`: caches all content, ignoring any `private`, `no-store`, or `no-cache` directives in `Cache-Control` response headers.



### Use a custom header to authenticate requests

To authenticate requests sent to your external backend, you can set a custom header to indicate that the request came from a Google Cloud load balancer. For example, you can configure the external backend to expect a particular value for the HTTP request's `Host` header, and you can configure the backend service to set the `Host` header to that expected value.

Use the following steps to configure the backend service to add a custom `Host` header to each request.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/add).

  2. Click the name of the load balancer that you want to modify.

  3. Click edit**Edit**.

  4. Click **Backend configuration**.

  5. For the backend service with the internet NEG backend, click edit**Edit**.

  6. Click **Advanced configurations**.

  7. For **Custom request headers** , click **Add header** :

     1. For **Header name** , enter `Host`.
     2. For **Header value** , enter `FQDN_NEG_ENDPOINT`.
  8. Click **Update**.

  9. To review your changes, click **Review and finalize** , and then click **Update**.




###  gcloud 

  * Use the following command to configure the backend service to add a custom `Host` header to each request. 
        
        gcloud compute backend-services update BACKEND_SERVICE \
              --custom-request-header "Host: HEADER_VALUE" \
              --load-balancing-scheme=EXTERNAL_MANAGED \
              --global
          




Make sure that you also configured the external backend to expect a `Host` header so that it can authenticate incoming requests.

For general information about custom request headers, see [Configure custom request headers](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers#working-with-request). For other authentication methods, see [Authenticate requests to the external backend](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#authenticate-requests).

### Enable IAP on the external Application Load Balancer

Note: IAP isn't compatible with Cloud CDN. 

You can configure IAP to be enabled or disabled (default). If enabled, you must provide values for `oauth2-client-id` and `oauth2-client-secret`.

To enable IAP, update the backend service to include the `--iap=enabled` flag with the `oauth2-client-id` and `oauth2-client-secret`.
    
    
    gcloud compute backend-services update BACKEND_SERVICE_NAME \
        --iap=enabled,oauth2-client-id=ID,oauth2-client-secret=SECRET \
        --global
    

Optionally, you can [enable IAP](https://docs.cloud.google.com/iap/docs/enabling-compute-howto#enabling) for a Compute Engine resource by using the Google Cloud console, gcloud CLI, or API.

### Update client HTTP keepalive timeout

The load balancer created in the previous steps has been configured with a default value for the [client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/https#http-keepalive-timeout). 

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

For an HTTP load balancer, update the target HTTP proxy by using the [`gcloud compute target-http-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update):
    
    
          gcloud compute target-http-proxies update TARGET_HTTP_PROXY_NAME \
              --http-keep-alive-timeout-sec=HTTP_KEEP_ALIVE_TIMEOUT_SEC \
              --global
        

For an HTTPS load balancer, update the target HTTPS proxy by using the [`gcloud compute target-https-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update):
    
    
          gcloud compute target-https-proxies update TARGET_HTTPS_PROXY_NAME \
              --http-keep-alive-timeout-sec=HTTP_KEEP_ALIVE_TIMEOUT_SEC \
              --global
        

Replace the following:

  * `TARGET_HTTP_PROXY_NAME`: the name of the target HTTP proxy.
  * `TARGET_HTTPS_PROXY_NAME`: the name of the target HTTPS proxy.
  * `HTTP_KEEP_ALIVE_TIMEOUT_SEC`: the HTTP keepalive timeout value from 5 to 600 seconds.



## What's next

  * To check whether Cloud CDN is serving responses from cache, see [Viewing logs](https://docs.cloud.google.com/cdn/docs/logging).
  * To learn about which content is cacheable or non-cacheable, see [Caching overview](https://docs.cloud.google.com/cdn/docs/caching).
  * To find Cloud CDN's points of presence, see [Cache locations](https://docs.cloud.google.com/cdn/docs/locations).
  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).
  * To learn how to disable Cloud CDN, see [Disable Cloud CDN](https://docs.cloud.google.com/cdn/docs/set-up-external-backend-internet-neg#disable).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
