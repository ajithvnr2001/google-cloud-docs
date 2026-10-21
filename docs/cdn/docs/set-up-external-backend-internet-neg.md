---
url: https://docs.cloud.google.com/cdn/docs/set-up-external-backend-internet-neg/
title: Set up an external backend with an internet NEG \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:50.171695+00:00
---

# Set up an external backend with an internet NEG  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/set-up-external-backend-internet-neg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Set up an external backend with an internet NEG Stay organized with collections  Save and categorize content based on your preferences. 

This guide uses an example to describe the fundamentals of using an external backend (sometimes called a _custom origin_) in an external Application Load Balancer. An external backend is an endpoint that is external to Google Cloud. When you use an external backend with an external Application Load Balancer, you can improve performance by using Cloud CDN caching.

The guide steps through how to configure a global external Application Load Balancer with a Cloud CDN-enabled backend service that proxies to an external backend server at `backend.example.com`.

In the example, the load balancer accepts HTTPS requests from clients and proxies these requests as HTTPS to the external backend. This example assumes that the external backend supports HTTPS.

Other options would be to configure a load balancer to accept HTTP or HTTPS requests, and use HTTPS when proxying requests to the external backend.

This guide assumes that you have already set up a load balancer and you are adding a new external backend. For more information, see [Set up a classic Application Load Balancer with a managed instance group backend](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple).

Figure 1 shows a sample architecture.

[ ![Figure 1. Typical use case for external backends.](https://docs.cloud.google.com/static/load-balancing/images/cdn-custom-origin-config.svg)](https://docs.cloud.google.com/static/load-balancing/images/cdn-custom-origin-config.svg) **Figure 1.** Typical use case for external backends.

In the diagram, `www.example.com` has a load balancer frontend with the IP address `120.1.1.1`. When there is a cache miss, user requests for `/cart/id/1223515` are fetched from the external backend by way of HTTPS. All other incoming traffic is directed to either the Google Cloud backend service with Compute Engine VMs or to the backend bucket, based on the URL map.

## Before you begin

Before following this guide, familiarize yourself with the following:

  * [Internet network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts), which includes the limitations.

  * [External backends specified by using internet NEGs](https://docs.cloud.google.com/cdn/docs/ext-backend-internet-neg-overview)




### Permissions

To follow this guide, you need to create an internet network endpoint group (NEG) and create or modify an external Application Load Balancer in a project. You should be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you should have both of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam).

Task | Required role  
---|---  
Create and modify load balancer components | [Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
Create and modify NEGs | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
  
## Configure a load balancer with an external backend

This section shows you how to configure and test an internet NEG.

### Setup overview

Setting up an internet NEG involves doing the following:

  * Defining the internet endpoint in an internet NEG.
  * Adding an internet NEG as the backend to a backend service.
  * Defining which user traffic to map to this backend service by configuring your external Application Load Balancer's URL map.
  * Allowlisting the necessary IP ranges.



This example creates the following resources:

  * A forwarding rule with the `120.1.1.1` IP address directs incoming requests to a target proxy.
    * The `networkTier` of the forwarding rule must be `PREMIUM`.
  * The target proxy checks each request against the URL map to determine the appropriate backend service for the request.
    * For external backends, the target proxy must be `TargetHttpProxy` or `TargetHttpsProxy`. This example uses `TargetHttpsProxy`.
  * Cloud CDN enabled (optional) on the backend service allows caching and serving responses from Cloud CDN caches.
  * This example includes a [custom header](https://docs.cloud.google.com/load-balancing/docs/custom-headers), which is required when the external backend expects a particular value for the HTTP request's `Host` header.



The setup looks like the following.

![Figure 2. Cloud CDN with an on-premises backend.](https://docs.cloud.google.com/static/cdn/images/cdn-on-prem-config.svg)**Figure 2.** Cloud CDN with an on-premises backend.

### Create the NEG and internet endpoint

###  Console 

  1. In the Google Cloud console, go to the **Network endpoint groups** page. 

[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click **Create network endpoint group**.
  3. Enter the name of the network endpoint group: `example-fqdn-neg`.
  4. For **Network endpoint group type** , select **Network endpoint group (Internet)**.
  5. For **Default port** , enter `443`.
  6. For **New network endpoint** , select **Fully qualified domain name and port**.
  7. For the FQDN, enter `backend.example.com`.
  8. For **Port type** , select **Default** , and verify that **Port number** is `443`.
  9. Click **Create**.



###  gcloud 

  1. Create an internet NEG, and set the `--network-endpoint-type` to `internet-fqdn-port` (the hostname and port where your external backend can be reached):
         
         gcloud compute network-endpoint-groups create example-fqdn-neg \
             --network-endpoint-type="internet-fqdn-port" --global
         

  2. Add your endpoint to the NEG. If a port isn't specified, the port selection defaults to port `80` (HTTP) or `443` (HTTPS; HTTP/2) depending on the protocol configured in the backend service. Make sure to include the `--global` flag:
         
         gcloud compute network-endpoint-groups update example-fqdn-neg \
             --add-endpoint="fqdn=backend.example.com,port=443" \
             --global
         

  3. List the created internet NEG:
         
         gcloud compute network-endpoint-groups list --global
         

Output: 
         
         NAME                LOCATION   ENDPOINT_TYPE        SIZE
         example-fqdn-neg    global     INTERNET_FQDN_PORT   1
         

  4. List the endpoint within that NEG:
         
         gcloud compute network-endpoint-groups list-network-endpoints example-fqdn-neg \
             --global
         

Output: 
         
         INSTANCE   IP_ADDRESS   PORT   FQDN
                                        backend.example.com
         




### Add an external backend to a load balancer

The following example updates an existing load balancer.

In the existing load balancer, the default service is a Google Cloud service. The example modifies the existing URL map by adding a path matcher that sends all requests for `cart/id/1223515` to the `images` backend service, which is associated with the internet NEG.

###  Console 

#### Create the backend service and add the internet NEG

  1. In the Google Cloud console, go to the **Load balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. To add the backend service to an existing load balancer, select your classic Application Load Balancer, click more_vert**Menu** , and then select **Edit**.
  3. Click **Backend configuration**.
  4. In the **Backend services & backend buckets** menu, select **Create a backend service**.
  5. Set the name of the backend service to `images`.
  6. For **Backend type** , select **Internet network endpoint group**.
  7. Select the protocol that you intend to use from the load balancer to the internet NEG. For this example, select **HTTPS**.
  8. Under **New backend > Internet network endpoint group**, select `example-fqdn-neg`, and then click **Done**.
  9. Select **Enable Cloud CDN**.
  10. Optional: Modify the [cache mode](https://docs.cloud.google.com/cdn/docs/using-cache-modes) and [TTL](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides) settings.
  11. In **Advanced configurations** , under **Custom request headers** , click **Add header**. 
     1. For **Header name** , enter `Host`.
     2. For **Header value** , enter `backend.example.com`.
  12. Click **Create**.
  13. Keep the window open to continue.



#### Attach the backend service to an existing URL map

  1. Click **Host and path rules**.
  2. The first row or rows have Google Cloud services in the right column, and one of them is already populated with the default rule `Any unmatched (default)` for **Hosts** and **Paths**.
  3. Ensure that there is a row with `images` selected in the right column. If it doesn't exist, click **Add host and path rule** , and select `images`. Populate the other fields as follows: 
     1. In **Hosts** , enter `*`.
     2. In **Paths** , enter `/cart/id/1223515`.



#### Review and finalize

  1. Click **Review and finalize**.
  2. Compare your settings to what you intended to create.
  3. If everything looks correct, click **Update**.



###  gcloud 

  1. Create a new backend service for the NEG:
         
         gcloud compute backend-services create images \
            --global \
            --enable-cdn \
            --cache-mode=CACHE_MODE \
            --protocol=HTTP2
         

Set the [cache mode](https://docs.cloud.google.com/cdn/docs/using-cache-modes) by replacing CACHE_MODE with one of the following:

     * `CACHE_ALL_STATIC`: automatically caches [static content](https://docs.cloud.google.com/cdn/docs/caching#static)

     * `USE_ORIGIN_HEADERS` (default): requires the origin to set [valid caching headers](https://docs.cloud.google.com/cdn/docs/caching#cacheability) to cache content

     * `FORCE_CACHE_ALL`: caches all content, ignoring any `private`, `no-store`, or `no-cache` directives in `Cache-Control` response headers

  2. Configure the backend service to add the custom request header `Host: backend.example.com` to the request:
         
         gcloud compute backend-services update images \
            --custom-request-header "Host: backend.example.com" --global
         

  3. Use the `backend-services add-backend` command to add the internet NEG to the backend service:
         
         gcloud compute backend-services add-backend images \
           --network-endpoint-group "example-fqdn-neg" \
           --global-network-endpoint-group \
           --global
         

  4. Attach the new backend service to the load balancer's URL map by [creating a new matching rule](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher) to direct requests to that backend:
         
         gcloud compute url-maps add-path-matcher EXAMPLE_URL_MAP \
           --default-service=GCP_SERVICE_EXAMPLE \
           --path-matcher-name=CUSTOM_ORIGIN_PATH_MATCHER_EXAMPLE \
           --backend-service-path-rules=/CART/ID/1223515=IMAGES
         

Replace the following:

     * `EXAMPLE_URL_MAP`: the name of your existing URL map
     * `GCP_SERVICE_EXAMPLE`: the name of an existing default backend service
     * `CUSTOM_ORIGIN_PATH_MATCHER_EXAMPLE`: the name of this new path rule
     * `/CART/ID/1223515`: the path
     * `IMAGES`: the name of the new backend service with the attached internet NEG



### Allowlist the necessary IP ranges

To allow an external Application Load Balancer to send requests to your internet NEG, you must query the `_cloud-eoips.googleusercontent.com` DNS TXT record by using a tool like `dig` or `nslookup`.

For example, run the following `dig` command:
    
    
    dig TXT _cloud-eoips.googleusercontent.com | grep -Eo 'ip4:[^ ]+' | cut -d':' -f2
    

The output contains two IP ranges, as follows:
    
    
    34.96.0.0/20
    34.127.192.0/18
    

**Caution:** These IP ranges are subject to change.

Note the IP ranges and ensure that these ranges are allowed by your firewall or cloud access control list (ACL).

For more information, see [Authenticating requests](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#authenticating_requests).

## Connect your domain to your load balancer

After the load balancer is created, note the IP address that is associated with the load balancer—for example, `30.90.80.100`. To point your domain to your load balancer, create an `A` record by using your domain registration service. If you added multiple domains to your SSL certificate, you must add an `A` record for each one, all pointing to the load balancer's IP address. For example, to create `A` records for `www.example.com` and `example.com`, use the following:
    
    
    NAME                  TYPE     DATA
    www                   A        30.90.80.100
    @                     A        30.90.80.100
    

If you use Cloud DNS as your DNS provider, see [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records).

## Test the external Application Load Balancer

**Note:** It might take a few minutes for the load balancer configuration to propagate globally after you first deploy it.

Now that you have configured your load balancer, you can start sending traffic to the load balancer's IP address. If you configured a domain, you can send traffic to the domain name as well. However, DNS propagation can take time to complete so you can start by using the IP address for testing.

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click on the load balancer that you just created.

  3. Note the IP address of the load balancer.

  4. If you created an **HTTP load balancer** , you can test your load balancer by using a web browser at `http://IP_ADDRESS`. Replace `IP_ADDRESS` with the load balancer's IP address. You should be directed to the `helloworld` service home page.

If you created an **HTTPS load balancer** , you can test your load balancer by using a web browser at `https://IP_ADDRESS`. Replace `IP_ADDRESS` with the load balancer's IP address. You should be directed to the `helloworld` service home page.

If that does not work and you are using a Google-managed certificate, confirm that your certificate resource's status is ACTIVE. For more information, see [Google-managed SSL certificate resource status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#certificate-managed-status).

Alternatively, you can use `curl` from your local machine's command line. Replace `IP_ADDRESS` with the load balancer's IPv4 address.

If you're using a Google-managed certificate, test the domain that points to the load balancer's IP address. For example: 
         
         curl -s 'https://www.example.com:443' --resolve www.example.com:443:IP_ADDRESS
         

  5. Optional: If you are using a custom domain, you might need to wait for the updated DNS settings to propagate. Then, test your domain (for example, `backend.example.com`) in the web browser.

For help with troubleshooting, see [Troubleshooting external backend and internet NEG issues](https://docs.cloud.google.com/load-balancing/docs/https/troubleshooting-ext-https-lbs#external-backends-internet-neg).




## Disable Cloud CDN

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/add).

  2. Click the name of the load balancer that you want to modify.

  3. Click edit**Edit**.

  4. Click **Backend configuration**.

  5. For the backend service with the internet NEG backend, click edit**Edit**.

  6. Clear the **Enable Cloud CDN** checkbox.

  7. To review your changes, click **Review and finalize** , and then click **Update**.




###  gcloud 
    
    
    gcloud compute backend-services update BACKEND_SERVICE_NAME \
        --no-enable-cdn
    

Disabling Cloud CDN does not invalidate or purge caches. If you turn Cloud CDN off and back on again, most or all of your cached content might still be cached. To prevent content from being used by the caches, you must [invalidate that content](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content).

## What's next

  * To check whether Cloud CDN is serving responses from cache, see [Logs and metrics for caching](https://docs.cloud.google.com/cdn/docs/logging).
  * To learn about which content is cacheable or non-cacheable, see [Caching overview](https://docs.cloud.google.com/cdn/docs/caching).
  * To find GFE points of presence, see [Cache locations](https://docs.cloud.google.com/cdn/docs/locations).
  * To set up cache policies in URL maps, see [Configure a Cloud CDN cache policy](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#cdn-cache-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
