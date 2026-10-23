---
url: https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless/
title: Set up a global external Application Load Balancer with Cloud Run, App Engine, or Cloud Run functions \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:24.201391+00:00
---

# Set up a global external Application Load Balancer with Cloud Run, App Engine, or Cloud Run functions  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a global external Application Load Balancer with Cloud Run, App Engine, or Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

You can create an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) to route external requests to _serverless_ backends. In this guide, serverless refers to the following compute products:

  * App Engine
  * Cloud Run functions
  * Cloud Run



[Serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) allow cloud administrators and developers to use [Google Cloud serverless apps](https://docs.cloud.google.com/serverless) with Application Load Balancers. After you configure the load balancer with a serverless NEG backend, it provides your serverless apps with a single external IP address, custom domain support, SSL certificate management, and security policies.

To learn more about serverless NEGs, see the [Serverless NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts).

If you are an existing user of the classic Application Load Balancer, make sure that you review [Migration overview](https://docs.cloud.google.com/load-balancing/docs/https/migrate-to-global) when you plan a new deployment with the global external Application Load Balancer. 

## Before you begin

  1. Deploy an App Engine, Cloud Run functions, or Cloud Run service.
  2. If you haven't already done so, install the Google Cloud CLI.
  3. Configure permissions. 
  4. Add an SSL certificate resource. 



### Deploy an App Engine, Cloud Run functions, or Cloud Run service

The instructions on this page assume you already have a Cloud Run, Cloud Run functions, or App Engine service running.

For the example on this page, we have used the [Cloud Run Python quickstart](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy) to deploy a Cloud Run service in the `us-central1` region. The rest of this page shows you how to set up an external Application Load Balancer that uses a serverless NEG backend to route requests to this service.

If you haven't already deployed a serverless app, or if you want to try a serverless NEG with a sample app, use one of the following quickstarts. You can create a serverless app in any region, but you must use the _same_ region later on to create the serverless NEG and load balancer.

**Cloud Run**

To create a simple Hello World application, package it into a container image, and trhen deploy the container image to Cloud Run, see [Quickstart: Build and Deploy](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy).

If you already have a sample container uploaded to the Container Registry, see [Quickstart: Deploy a Prebuilt Sample Container](https://docs.cloud.google.com/run/docs/quickstarts/deploy-container).

**Cloud Run functions**

See [Cloud Run functions: Python Quickstart](https://docs.cloud.google.com/functions/docs/create-deploy-python).

**App Engine**

See the following App Engine quickstart guides for Python 3:

  * [Standard Environment](https://docs.cloud.google.com/appengine/docs/standard/python3/create-app)
  * [Flexible Environment](https://docs.cloud.google.com/appengine/docs/flexible/python/create-app)



### Install the Google Cloud CLI

Install the Google Cloud CLI. See [gcloud Overview](https://docs.cloud.google.com/sdk/gcloud) for conceptual and installation information about the tool.

If you haven't run the gcloud CLI previously, first run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to initialize your gcloud directory.

### Configure permissions

To follow this guide, you need to create a serverless NEG and create an external HTTP(S) load balancer in a project. You should be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you should have the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required Role  
---|---  
Create load balancer and networking components | [Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
Create and modify NEGs | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
Create and modify SSL certificates | [Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
  
### Optional: Use BYOIP addresses

With bring your own IP (BYOIP), you can import your own public addresses to Google Cloud to use the addresses with Google Cloud resources. For example, if you import your own IPv4 addresses, you can assign one to the forwarding rule when you configure your load balancer. When you follow the instructions in this document to [create the load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless#creating_the_load_balancer), provide the BYOIP address as the **IP address**.

For more information about using BYOIP, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

## Reserve an external IP address

Now that your services are up and running, set up a [global static external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses) that your customers use to reach your load balancer.

**Note:** This step is required for this example, and recommended in general, because a static external IP address provides a single address to point your serverless app to. Reserving an IP address is also essential if you are using a custom domain for your serverless app (also required for Google-managed SSL certificates). With a custom domain, you will need to update your DNS records to point your domain to this IP address.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Click **Reserve external**.

  3. On the **Reserve external static IP address** page, for **Name** , enter `example-ip`.

  4. For **Network service tier** , select **Premium**.

  5. For **IP version** , select **IPv4**.

  6. For **Type** , select **Global**.

  7. Click **Reserve**.




###  gcloud 
    
    
    gcloud compute addresses create EXAMPLE_IP \
        --network-tier=PREMIUM \
        --ip-version=IPV4 \
        --global
    

Note the IPv4 address that was reserved:
    
    
    gcloud compute addresses describe EXAMPLE_IP \
        --format="get(address)" \
        --global
    

Replace `EXAMPLE_IP` with the name of the IP address. 

## Create an SSL certificate resource

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

## Create the load balancer

In the following diagram, the load balancer uses a serverless NEG backend to direct requests to a serverless Cloud Run service. For this example, we have used the [Cloud Run Python quickstart](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy) to deploy a Cloud Run service.

[ ![External Application Load Balancer architecture for a Cloud Run application.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-run-ext-https.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-run-ext-https.svg) External Application Load Balancer architecture for a Cloud Run application (click to enlarge).

Because health checks are not supported for backend services with serverless NEG backends, you don't need to create a firewall rule allowing health checks if the load balancer has only serverless NEG backends.

### Console

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  5. For **Global or single region deployment** , select **Best for global workloads** and click **Next**.
  6. For **Load balancer generation** , select **Global external Application Load Balancer** and click **Next**.
  7. Click **Configure**.



**Basic configuration**

  1. For the name of the load balancer, enter `serverless-lb`.
  2. Keep the window open to continue.



#### Frontend configuration

  1. Click **Frontend configuration**.
  2. For **Name** , enter a name.
  3. To create an HTTPS load balancer, you must have an [SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) (`gcloud compute ssl-certificates list`). 

We recommend using a Google-managed certificate as described previously. 

To configure an external Application Load Balancer, fill in the fields as follows.

Verify the following options are configured with these values:

Property | Value (type a value or select an option as specified)  
---|---  
Protocol | HTTPS  
Network Service Tier | Premium  
  
IP version | IPv4  
IP address | example-ip  
Port | 443  
Optional: HTTP keepalive timeout | Enter a timeout value from 5 to 1200 seconds. The default value is 610 seconds.  
Certificate |  For **Choose certificate repository** , select **Use certificate map** or **Use classic certificates**. Depending on your selection, select a certificate map or a classic certificate.   
Optional: Enable HTTP to HTTPS Redirect |  Use this checkbox to enable HTTP to HTTPS redirects. Enabling this checkbox creates an additional partial HTTP load balancer that uses the same IP address as your HTTPS load balancer and redirects HTTP requests to your load balancer's HTTPS frontend.  This checkbox can only be selected when the HTTPS protocol is selected and a reserved IP address is used.   
  
If you want to test this process without setting up an SSL certificate resource (or a domain as required by Google-managed certificates), you can set up an HTTP load balancer. 

**To create an HTTP load balancer** , verify that the following options are configured with these values: 

Property | Value (type a value or select an option as specified)  
---|---  
Protocol | HTTP  
Network Service Tier | Premium  
IP version | IPv4  
IP address | example-ip  
Port | 80  
Optional: HTTP keepalive timeout | Enter a timeout value from 5 to 1200 seconds. The default value is 610 seconds.  
  4. Click **Done**.



#### Backend configuration

  1. Click **Backend configuration**.
  2. In the **Backend services & backend buckets** list, click **Create a backend service**. 
  3. For **Name** , enter a name.
  4. In **Backend type** , select **Serverless network endpoint group**. 
  5. Leave **Protocol** unchanged. This parameter is ignored.
  6. In the **Backends** section, for **New backend** , select **Create Serverless network endpoint group**. 
  7. For **Name** , enter a name.
  8. In **Region** , select **us-central1** , and then select **Cloud Run**.
  9. Select **Select service name**.
  10. In the **Service** list, select the Cloud Run service that you want to create a load balancer for. 
  11. Click **Create**.
  12. In the **New backend** section, click **Done**.
  13. Click **Create**.



#### Routing rules

Routing rules determine how your traffic is directed. To configure routing, you'll set up host rules and path matchers, which are configuration components of an external Application Load Balancer's [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts). 

  1. Click **Routing rules**. 

  2. Retain the default hosts and paths. For this example, all requests go to the backend service created in the previous step. 



#### Reviewing the configuration

  1. Click **Review and finalize**.
  2. Review all the settings.
  3. Optional: Click **Equivalent Code** to view the REST API request that will be used to create the load balancer.
  4. Click **Create**.
  5. Wait for the load balancer to be created.
  6. Click the name of the load balancer (**serverless-lb**).
  7. Note the IP address of the load balancer for the next task. It's referred to as `IP_ADDRESS`. 

When you use the Google Cloud console to create an HTTP(S) load balancer with a serverless NEG backend, logging is enabled by default. You can use the [`gcloud compute backend-services update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command to disable logging if needed. 

### gcloud

  1. Create a serverless NEG for your serverless app. 

To create a serverless NEG with a Cloud Run service: 
         
         gcloud compute network-endpoint-groups create SERVERLESS_NEG_NAME \
                --region=us-central1 \
                --network-endpoint-type=serverless  \
                --cloud-run-service=CLOUD_RUN_SERVICE_NAME
            

For more options, see the `gcloud` reference guide for [`gcloud compute network-endpoint-groups create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/create). 
  2. Create a backend service. 
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
                --load-balancing-scheme=EXTERNAL_MANAGED \
                --global
            

  3. Add the serverless NEG as a backend to the backend service: 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
                --global \
                --network-endpoint-group=SERVERLESS_NEG_NAME \
                --network-endpoint-group-region=us-central1
            

  4. Create a URL map to route incoming requests to the backend service: 
         
         gcloud compute url-maps create URL_MAP_NAME \
                --default-service BACKEND_SERVICE_NAME
            

This example URL map only targets one backend service representing a single serverless app, so we don't need to set up host rules or path matchers. If you have more than one backend service, you can use host rules to direct requests to different services based on the host name, and you can set up path matchers to direct requests to different services based on the request path.

  5. Perform this step only if you want to create an HTTPS load balancer. This is not required for HTTP load balancers.  To create an HTTPS load balancer, you must have an [SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) to use in the HTTPS target proxy. You can create an SSL certificate resource using either a Google-managed SSL certificate or a self-managed SSL certificate. Using Google-managed certificates is recommended because Google Cloud obtains, manages, and renews these certificates automatically.  
  
To create a Google-managed certificate, [ you must have a domain](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#before_you_begin). If you do not have a domain, you can use a self-signed SSL certificate for testing.  
  
To create a Google-managed SSL certificate resource: 
         
         gcloud compute ssl-certificates create SSL_CERTIFICATE_NAME \
                --domains DOMAIN
            

To create a self-managed SSL certificate resource: 
         
         gcloud compute ssl-certificates create SSL_CERTIFICATE_NAME \
                --certificate CRT_FILE_PATH \
                --private-key KEY_FILE_PATH
            

  6. Create a target HTTP(S) proxy to route requests to your URL map.

For an HTTP load balancer, create an HTTP target proxy:
         
         gcloud compute target-http-proxies create TARGET_HTTP_PROXY_NAME \
               --http-keep-alive-timeout-sec=HTTP_KEEP_ALIVE_TIMEOUT_SEC \
               --url-map=URL_MAP_NAME
            

For an HTTPS load balancer, create an HTTPS target proxy. The proxy is the portion of the load balancer that holds the SSL certificate for HTTPS Load Balancing, so you also load your certificate in this step.
         
         gcloud compute target-https-proxies create TARGET_HTTPS_PROXY_NAME \
                --http-keep-alive-timeout-sec=HTTP_KEEP_ALIVE_TIMEOUT_SEC \
                --ssl-certificates=SSL_CERTIFICATE_NAME \
                --url-map=URL_MAP_NAME
            

Replace the following:

     * `TARGET_HTTP_PROXY_NAME`: the name of the target HTTP proxy.
     * `TARGET_HTTPS_PROXY_NAME`: the name of the target HTTPS proxy.
     * `HTTP_KEEP_ALIVE_TIMEOUT_SEC`: an optional field used to specify the [client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/https#http-keepalive-timeout). The timeout value must be from 5 to 1200 seconds. The default value is 610 seconds.
     * `SSL_CERTIFICATE_NAME`: the name of the SSL certificate.
     * `URL_MAP_NAME`: the name of the URL map.
  7. Create a forwarding rule to route incoming requests to the proxy.  
  


For an HTTP load balancer:
         
         gcloud compute forwarding-rules create HTTP_FORWARDING_RULE_NAME \
            --load-balancing-scheme=EXTERNAL_MANAGED \
            --network-tier=PREMIUM \
            --address=EXAMPLE_IP \
            --target-http-proxy=TARGET_HTTP_PROXY_NAME \
            --global \
            --ports=80
            

For an HTTPS load balancer:
         
         gcloud compute forwarding-rules create HTTPS_FORWARDING_RULE_NAME \
                --load-balancing-scheme=EXTERNAL_MANAGED \
                --network-tier=PREMIUM \
                --address=EXAMPLE_IP \
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

Now that you have configured your load balancer, you can start sending traffic to the load balancer's IP address. If you configured a domain, you can send traffic to the domain name as well. However, DNS propagation can take time to complete so you can start by using the IP address for testing.

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/add)

  2. Click on the load balancer you just created.

  3. Note the **IP Address** of the load balancer. 

  4. For an **_HTTP load balancer_** , you can test your load balancer using a web browser by going to `http://IP_ADDRESS`. Replace `IP_ADDRESS` with the load balancer's IP address. You should be directed to the `helloworld` service homepage.   


  5. For an **_HTTPS load balancer_** , you can test your load balancer using a web browser by going to `https://IP_ADDRESS`. Replace `IP_ADDRESS` with the load balancer's IP address. You should be directed to the `helloworld` service homepage.   
If that does not work and you are using a Google-managed certificate, confirm that your certificate resource's status is ACTIVE. For more information, see [Google-managed SSL certificate resource status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#certificate-managed-status).  
If you used a self-signed certificate for testing, your browser displays a warning. You must explicitly instruct your browser to accept a self-signed certificate. Click through the warning to see the actual page. 




## Restrict ingress on default endpoint

Without the proper ingress settings, users can use your serverless application's default URL to bypass the load balancer, Cloud Armor security policies, SSL certificates, and private keys that are passed through the load balancer.

Ensure external traffic only reaches your serverless application from the load balancer by using setting ingress to "Internal and Cloud Load Balancing".

  * [Set network ingress to "Internal and Cloud Load Balancing" for App Engine](https://docs.cloud.google.com/appengine/docs/standard/ingress-settings)
  * [Set network ingress to "Internal and Cloud Load Balancing" for Cloud Run functions](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--ingress-settings)
  * [Set network ingress to "Internal and Cloud Load Balancing" for Cloud Run](https://docs.cloud.google.com/run/docs/securing/ingress)



Additionally, you can [disable the default URL](https://docs.cloud.google.com/run/docs/securing/ingress) for Cloud Run.

## Additional configuration options

This section expands on the configuration example to provide alternative and additional configuration options. All of the tasks are optional. You can perform them in any order.

### Set up multi-region load balancing

**Note:** For serverless NEGs, multi-region load balancing is supported only if the serverless NEG points to a Cloud Run or a Cloud Run functions service. Multi-region load balancing with outlier detection isn't supported with App Engine because you can't deploy a project's App Engine in multiple regions.

In the example described earlier on this page, we have only one Cloud Run service serving as the backend in the `us-central1` region. Because the serverless NEG can point to only one endpoint at a time, load balancing is not performed across multiple regions. The external Application Load Balancer serves as the frontend only, and it proxies traffic to the specified `helloworld` app endpoint. However, you might want to serve your Cloud Run app from more than one region to improve end-user latency.

If a backend service has several serverless NEGs attached to it, the load balancer balances traffic by forwarding requests to the serverless NEG in the closest available region. However, backend services can only contain one serverless NEG _per region_. To make your Cloud Run service available from multiple regions, you need to set up cross-region routing. You should be able to use a single URL scheme that works anywhere in the world, yet serves user requests from the region closest to the user.

To set up multi-region serving, you will need to use the Premium network tier to ensure that all the regional Cloud Run deployments are compatible and ready to serve traffic from any region.

To set up a multi-region load balancer:

  1. Set up two Cloud Run services in different regions. Let's assume that you have deployed two Cloud Run services: one to a region in the US, and another to a region in Europe.
  2. Create an external Application Load Balancer with the following setup: 
     1. Set up a global backend service with two serverless NEGs: 
        1. Create the first NEG in the same region as the Cloud Run service deployed in the US.
        2. Create the second NEG in the same region as the Cloud Run service deployed in Europe.
     2. Set up your frontend configuration with the Premium Network Service Tier.



The resulting setup is shown in the following diagram.

[ ![Multi-region routing for serverless applications.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-multi-region.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-multi-region.svg) Multi-region routing for serverless applications

This section builds on the load-balancer setup described earlier on this page, in which you created one serverless NEG in the `us-central1` region that points to a Cloud Run service in the same region. It also assumes that you've created a second Cloud Run service in the `europe-west1` region. The second serverless NEG that you create will point to this Cloud Run service in the `europe-west1` region.

In this example, you will complete the following steps:

  1. Create a second serverless NEG in the `europe-west1` region.
  2. Attach the second serverless NEG to the backend service.



To add a second serverless NEG to an existing backend service, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/)

  2. Click the name of the load balancer whose backend service you want to edit.

  3. On the **Load balancer details** page, click edit**Edit**.

  4. On the **Edit global external Application Load Balancer** page, click **Backend configuration**.

  5. On the **Backend configuration** page, click edit**Edit** for the backend service that you want to modify.

  6. In the **Backends** section, click **Add a backend**.

  7. In the **Serverless network endpoint groups** list, select **Create Serverless network endpoint group.**

  8. Enter a name for the serverless NEG.

  9. For **Region** , select `europe-west1`.

  10. For **Serverless network endpoint group type** , select **Cloud Run** , and then do the following:

     1. Select the **Select Service** option.
     2. In the **Service** list, select the Cloud Run service that you want to create a load balancer for.
  11. Click **Create**.

  12. On the **New backend** page, click **Done**.

  13. Click **Save**.

  14. To update the backend service, click **Update**.

  15. To update the load balancer, on the **Edit global external Application Load Balancer** page, click **Update**.




###  gcloud 

  1. Create a second serverless NEG in the same region in which the Cloud Run service is deployed.
         
         gcloud compute network-endpoint-groups create SERVERLESS_NEG_NAME_2 \
           --region=europe-west1 \
           --network-endpoint-type=SERVERLESS \
           --cloud-run-service=CLOUD_RUN_SERVICE_2
         

Replace the following:

     * `SERVERLESS_NEG_NAME_2`: the name of the second serverless NEG
     * `CLOUD_RUN_SERVICE_2`: the name of the Cloud Run service
  2. Add the second serverless NEG as a backend to the backend service.
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --global \
           --network-endpoint-group=SERVERLESS_NEG_NAME_2 \
           --network-endpoint-group-region=europe-west1
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service
     * `SERVERLESS_NEG_NAME_2`: the name of the second serverless NEG



#### Use an authenticated Pub/Sub push subscription with a multi-region Cloud Run deployment

For authenticated push requests, Cloud Run expects a region-specific audience field by default. In case of a multi-region Cloud Run deployment, if the push request is routed to a Cloud Run service in a different region, the JWT token verification fails due to an audience mismatch.

To work around this region-specific restriction:

  1. Configure a [custom audience](https://docs.cloud.google.com/run/docs/configuring/custom-audiences) that's the same for service deployments in different regions.
  2. Configure the Pub/Sub push messages to use the custom audience as the [audience in the JWT token](https://docs.cloud.google.com/pubsub/docs/authenticate-push-subscriptions).



### Set up regional routing

A common reason for serving applications from multiple regions is to meet data locality requirements. For example, you might want to ensure that requests made by European users are always served from a region located in Europe. To set this up you need a URL schema with separate URLs for EU and non-EU users, and direct your EU users to the EU URLs.

In such a scenario, you would use the URL map to route requests from specific URLs to their corresponding regions. With such a setup, requests meant for one region are never delivered to a different region. This provides isolation between regions. On the other hand, when a region fails, requests are not routed to a different region. So this setup does not increase your service's availability.

To set up regional routing, you will need to use the Premium network tier so that you can combine different regions in a single forwarding rule.

To set up a load balancer with regional routing:

  1. Set up two Cloud Run services in different regions. Let's assume you have deployed two Cloud Run services: hello-world-eu to a region in Europe, and hello-world-us to a region in the US.
  2. Create an external Application Load Balancer with the following setup: 
     1. Set up a backend service with a serverless NEG in Europe. The serverless NEG must be created in the same region as the Cloud Run service deployed in Europe.
     2. Set up a second backend service with another serverless NEG in the US. This serverless NEG must be created in the same region as the Cloud Run service deployed in the US.
     3. Set up your URL map with the appropriate host and path rules so that one set of URLs routes to the European backend service while all the requests route to the US backend service.
     4. Set up your frontend configuration with the Premium network tier.



The rest of the setup can be the same as described previously. Your resulting setup should look like this:

[ ![Regional routing for serverless applications without failover.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-regional.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-regional.svg) Regional routing for serverless applications without failover

### Use a URL mask

When creating a serverless NEG, instead of selecting a specific Cloud Run service, you can use a URL mask to point to multiple services serving at the same domain. A URL mask is a template of your URL schema. The serverless NEG will use this template to extract the service name from the incoming request's URL and map the request to the appropriate service.

URL masks are particularly useful if your service is [mapped to a custom domain](https://docs.cloud.google.com/run/docs/mapping-custom-domains) rather than the default address that Google Cloud provides for the deployed service. A URL mask allows you to target multiple services and versions with a single rule even when your application is using a custom URL pattern.

If you haven't already done so, make sure you read [Serverless NEGs overview: URL Masks](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#url_masks).

#### Construct a URL mask

To construct a URL mask for your load balancer, start with the URL of your service. For this example, we will use a sample serverless app running at `https://example.com/login`. This is the URL where the app's `login` service will be served.

  1. Remove the `http` or `https` from the URL. You are left with `example.com/login`.
  2. Replace the service name with a placeholder for the URL mask. 
     1. Cloud Run: Replace the Cloud Run service name with the placeholder `<service>`. If the Cloud Run service has a tag associated with it, replace the tag name with the placeholder `<tag>`. In this example, the URL mask you are left with is, `example.com/<service>`.
     2. Cloud Run functions: Replace the function name with the placeholder `<function>`. In this example, the URL mask you are left with is, `example.com/<function>`.
     3. App Engine: Replace the service name with the placeholder `<service>`. If the service has a version associated with it, replace the version with the placeholder `<version>`. In this example, the URL mask you are left with is, `example.com/<service>`.
     4. API Gateway: Replace the gateway name with the placeholder `<gateway>`. In this example, the URL mask you are left with is, `example.com/<gateway>`.
  3. **(Optional)** If the service name (or function, version, or tag) can be extracted from the path portion of the URL,the domain can be omitted. The path part of the URL mask is distinguished by the first `/` character. If a `/` is not present in the URL mask, the mask is understood to represent the host only. Therefore, for this example, the URL mask can be reduced to `/<service>`, `/<gateway>`, or `/<function>`.

Similarly, if the service name can be extracted from the host part of the URL, you can omit the path altogether from the URL mask.

You can also omit any host or subdomain components that come before the first placeholder as well as any path components that come after the last placeholder. In such cases, the placeholder captures the required information for the component.




Here are a few more examples that demonstrate these rules:

###  Cloud Run 

This table assumes that you have a custom domain called `example.com` and all your Cloud Run services are being mapped to this domain by using an external Application Load Balancer.

Service, Tag name | Custom domain URL  | URL mask   
---|---|---  
service: login  | https://login-home.example.com/web  | <service>-home.example.com  
service: login  | https://example.com/login/web  | example.com/<service> or /<service>  
service: login, tag: test  | https://test.login.example.com/web  | <tag>.<service>.example.com   
service: login, tag: test  | https://example.com/home/login/test  | example.com/home/<service>/<tag> or /home/<service>/<tag>  
service: login, tag: test  | https://test.example.com/home/login/web  | <tag>.example.com/home/<service>  
  
###  Cloud Run functions 

This table assumes that you have a custom domain called `example.com` and all your Cloud Run functions services are being mapped to this domain.

Function Name | Custom domain URL | URL Mask  
---|---|---  
login  | https://example.com/login  | /<function>  
login  | https://example.com/home/login  | /home/<function>  
login  | https://login.example.com  | <function>.example.com   
login  | https://login.home.example.com  | <function>.home.example.com   
  
###  App Engine 

This table assumes that you have a custom domain called `example.com` and all your App Engine services are being mapped to this domain.

Service name, version  | Custom domain URL  | URL mask   
---|---|---  
service: login  | https://login.example.com/web  | <service>.example.com   
service: login  | https://example.com/home/login/web  | example.com/home/<service>, or /home/<service>  
service: login, version: test  | https://test.example.com/login/web  | <version>.example.com/<service>  
service: login, version: test  | https://example.com/login/test  | example.com/<service>/<version>  
  
###  API Gateway 

This table assumes that you have a custom domain called `example.com` and all your API Gateway services are being [mapped to this domain](https://docs.cloud.google.com/api-gateway/docs/using-custom-domains).

Gateway name  | API Gateway(Preview) custom domain URL  | URL mask   
---|---|---  
login  | https://example.com/login  | /<gateway>  
login  | https://example.com/home/login  | /home/<gateway>  
login  | https://login.example.com  | <gateway>.example.com   
login  | https://login.home.example.com  | <gateway>.home.example.com   
  
#### Create a serverless NEG with a URL mask

###  Console 

For a new load balancer, you can use the same end-to-end process as described previously in this topic. When configuring the backend service, instead of selecting a specific service, enter a URL mask.

If you have an existing load balancer, you can edit the backend configuration and have the serverless NEG point to a URL mask instead of a specific service.

To add a URL mask-based serverless NEG to an existing backend service:

  1. Go to the Load balancing page in the Google Cloud console.   
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/)
  2. Click the name of the load balancer whose backend service you want to edit.
  3. On the **Load balancer details** page, click **Edit** edit.
  4. On the **Edit global external Application Load Balancer** page, click **Backend configuration**.
  5. On the **Backend configuration** page, click **Edit** edit for the backend service you want to modify.
  6. Click **Add backend**.
  7. Select **Create Serverless network endpoint group**. 
     1. For the **Name** , enter `helloworld-serverless-neg`.
     2. Under **Region** , select **us-central1**.
     3. Under **Serverless network endpoint group type** , select the platform where your serverless apps (or services or functions) were created. 
        1. Select **Use URL Mask**.
        2. Enter a URL mask. For instructions on how to create a URL mask, see Constructing a URL mask.
        3. Click **Create**.
  8. In the **New backend** section, click **Done**.
  9. Click **Update**.



###  gcloud: Cloud Run 

To create a Serverless NEG with a sample URL mask of `example.com/<service>`:
    
    
    gcloud compute network-endpoint-groups create helloworld-neg-mask \
      --region=us-central1 \
      --network-endpoint-type=serverless \
      --cloud-run-url-mask="example.com/<service>"
    

###  gcloud: Cloud Run functions 

To create a Serverless NEG with a sample URL mask of `example.com/<service>`:
    
    
    gcloud compute network-endpoint-groups create helloworld-neg-mask \
     --region=us-central1 \
     --network-endpoint-type=serverless \
     --cloud-function-url-mask="example.com/<service>"
    

###  gcloud: App Engine 

To create a Serverless NEG with a sample URL mask of `example.com/<service>`:
    
    
    gcloud compute network-endpoint-groups create helloworld-neg-mask \
        --region=us-central1 \
        --network-endpoint-type=serverless \
        --app-engine-url-mask="example.com/<service>"
    

###  gcloud: API Gateway 

To create a Serverless NEG with a sample URL mask of `example.com/<gateway>`:
    
    
    gcloud beta compute network-endpoint-groups create helloworld-neg-mask \
      --region=us-central1 \
      --network-endpoint-type=serverless \
      --serverless-deployment-platform=apigateway.googleapis.com \
      --serverless-deployment-resource=my-gateway \
      --serverless-deployment-url-mask="example.com/<gateway>"
    

To learn how the load balancer handles issues with URL mask mismatches, see [Troubleshooting issues with serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/https/troubleshooting-ext-https-lbs#serverless-negs).

### Move your custom domain to be served by the external Application Load Balancer

If your serverless compute apps are being mapped to custom domains, you might want to update your DNS records so that traffic sent to the existing Cloud Run, Cloud Run functions, API Gateway, or App Engine custom domain URLs is routed through the load balancer instead.

For example, if you have a custom domain called `example.com` and all your Cloud Run services are mapped to this domain, you should update the DNS record for `example.com` to point to the load balancer's IP address.

Before updating the DNS records, you can test your configuration locally by forcing local DNS resolution of the custom domain to the load balancer's IP address. To test locally, either modify the `/etc/hosts/` file on your local machine to point `example.com` to the load balancer's IP address, or, use the `curl --resolve` flag to force `curl` to use the load balancer's IP address for the request.

When the DNS record for `example.com` resolves to the HTTP(S) load balancer's IP address, requests sent to `example.com` begin to be routed via the load balancer. The load balancer dispatches them to the relevant backend service according to its URL map. Additionally, if the backend service is configured with a URL mask, the serverless NEG uses the mask to route the request to the appropriate Cloud Run, Cloud Run functions, API Gateway, or App Engine service.

**Note:** If you use [Google-managed certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates), migrating an existing service to an external Application Load Balancer may incur some downtime, typically less than an hour. This is because the SSL certificate for your external Application Load Balancer won't be provisioned until you update your DNS records to point to the load balancer's IP address.

### Enable Cloud CDN

Enabling [Cloud CDN](https://docs.cloud.google.com/cdn) for your Cloud Run service allows you to optimize content delivery by caching content close to your users.

You can enable Cloud CDN on backend services used by global external Application Load Balancers by using the [`gcloud compute backend-services update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command.
    
    
    gcloud compute backend-services update helloworld-backend-service   
    
        --enable-cdn   
    
        --global
    

Cloud CDN is supported for backend services with Cloud Run, Cloud Run functions, API Gateway, and App Engine backends.

### Enable IAP on the external Application Load Balancer

Note: IAP isn't compatible with Cloud CDN. 

You can configure IAP to be enabled or disabled (default). If enabled, you must provide values for `oauth2-client-id` and `oauth2-client-secret`.

To enable IAP, update the backend service to include the `--iap=enabled` flag with the `oauth2-client-id` and `oauth2-client-secret`.
    
    
    gcloud compute backend-services update BACKEND_SERVICE_NAME \
        --iap=enabled,oauth2-client-id=ID,oauth2-client-secret=SECRET \
        --global
    

Optionally, you can [enable IAP](https://docs.cloud.google.com/iap/docs/enabling-compute-howto#enabling) for a Compute Engine resource by using the Google Cloud console, gcloud CLI, or API.

### Enable Google Cloud Armor

[Cloud Armor](https://docs.cloud.google.com/armor/docs) is a security product that provides protection against distributed denial-of-service (DDoS) attacks to all GCLB proxy load balancers. Cloud Armor also provides configurable security policies to services accessed through an external Application Load Balancer. To learn about Cloud Armor security policies for external Application Load Balancers, see [Cloud Armor security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-concepts).

Optional: Configure a default backend security policy. The default security policy throttles traffic over a user-configured threshold. For more information about default security policies, see the [Rate limiting overview](https://docs.cloud.google.com/armor/docs/rate-limiting-overview#default-policy).

  1. To opt out of the Cloud Armor default security policy, select `None` in the **Cloud Armor backend security policy** list.
  2. To configure the Cloud Armor default security policy, select **Default security policy** in the **Cloud Armor backend security policy** list.
  3. In the **Policy name** field, accept the automatically generated name or enter a name for your security policy.
  4. In the **Request count** field, accept the default request count or enter an integer between `1` and `10,000`.
  5. In the **Interval** field, select an interval.
  6. In the **Enforce on key** field, choose one of the following values: **All** , **IP address** , or **X-Forwarded-For IP address**. For more information about these options, see [Identifying clients for rate limiting](https://docs.cloud.google.com/armor/docs/rate-limiting-overview#identifying_clients_for_rate_limiting).



### Enable logging and monitoring

You can enable, disable, and view logs for an external Application Load Balancer backend service. When using the Google Cloud console, logging is enabled by default for backend services with serverless NEG backends. You can use `gcloud` to disable logging for each backend service as needed. For instructions, see [Logging](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#logging).

The load balancer also exports monitoring data to Cloud Monitoring. Monitoring metrics can be used to evaluate a load balancer's configuration, usage, and performance. Metrics can also be used to troubleshoot problems and improve resource utilization and user experience. For instructions, see [Monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring).

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



### Enable outlier detection

You can enable [outlier detection](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection) on global backend services to identify unhealthy serverless NEGs and reduce the number the requests sent to the unhealthy serverless NEGs.

Outlier detection is enabled on the backend service by using one of the following methods:

  * The `consecutiveErrors` method (`outlierDetection.consecutiveErrors`), in which a `5 _xx_` series HTTP status code qualifies as an error.
  * The `consecutiveGatewayFailure` method (`outlierDetection.consecutiveGatewayFailure`), in which only the `502`, `503`, and `504` HTTP status codes qualify as an error.



Use the following steps to enable outlier detection for an existing backend service. Note that even after enabling outlier detection, some requests can be sent to the unhealthy service and return a `5 _xx_` status code to the clients. To further reduce the error rate, you can configure more aggressive values for the outlier detection parameters. For more information, see the [`outlierDetection` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.outlier_detection).

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/)

  2. Click the name of the load balancer whose backend service you want to edit.

  3. On the **Load balancer details** page, click edit**Edit**. 

  4. On the **Edit global external Application Load Balancer** page, click **Backend configuration**. 

  5. On the **Backend configuration** page, click edit**Edit** for the backend service that you want to modify.

  6. Scroll down and expand the **Advanced configurations** section.

  7. In the **Outlier detection** section, select the **Enable** checkbox.

  8. Click edit**Edit** to configure outlier detection.

Verify that the following options are configured with these values:

Property | Value  
---|---  
**Consecutive errors** | 5  
**Interval** | 1000  
**Base ejection time** | 30000  
**Max ejection percent** | 50  
**Enforcing consecutive errors** | 100  
  
In this example, the outlier detection analysis runs every one second. If the number of consecutive HTTP `5 _xx_` status codes received by an Envoy proxy is five or more, the backend endpoint is ejected from the load-balancing pool of that Envoy proxy for 30 seconds. When the enforcing percentage is set to 100%, the backend service enforces the ejection of unhealthy endpoints from the load-balancing pools of those specific Envoy proxies every time the outlier detection analysis runs. If the ejection conditions are met, up to 50% of the backend endpoints from the load-balancing pool can be ejected. 

  9. Click **Save**.

  10. To update the backend service, click **Update**. 

  11. To update the load balancer, on the **Edit global external Application Load Balancer** page, click **Update**. 




###  gcloud 

  1. Export the backend service into a YAML file.
         
         gcloud compute backend-services export BACKEND_SERVICE_NAME \
           --destination=BACKEND_SERVICE_NAME.yaml --global
         

Replace `BACKEND_SERVICE_NAME` with the name of the backend service.

  2. Edit the YAML configuration of the backend service to add the fields for outlier detection as highlighted in the following YAML configuration, in the `outlierDetection` section:

In this example, the outlier detection analysis runs every one second. If the number of consecutive HTTP `5 _xx_` status codes received by an Envoy proxy is five or more, the backend endpoint is ejected from the load-balancing pool of that Envoy proxy for 30 seconds. When the enforcing percentage is set to 100%, the backend service enforces the ejection of unhealthy endpoints from the load-balancing pools of those specific Envoy proxies every time the outlier detection analysis runs. If the ejection conditions are met, up to 50% of the backend endpoints from the load-balancing pool can be ejected. 
         
         name: BACKEND_SERVICE_NAME
         backends:
         - balancingMode: UTILIZATION
           capacityScaler: 1.0
           group: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_A/networkEndpointGroups/SERVERLESS_NEG_NAME
         - balancingMode: UTILIZATION
           capacityScaler: 1.0
           group: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_B/networkEndpointGroups/SERVERLESS_NEG_NAME_2
         outlierDetection:
           baseEjectionTime:
             nanos: 0
             seconds: 30
           consecutiveErrors: 5
           enforcingConsecutiveErrors: 100
           interval:
             nanos: 0
             seconds: 1
           maxEjectionPercent: 50
         port: 80
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME
         sessionAffinity: NONE
         timeoutSec: 30
         ...
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service
     * `PROJECT_ID`: the ID of your project
     * `REGION_A` and `REGION_B`: the regions where the load balancer has been configured.
     * `SERVERLESS_NEG_NAME`: the name of the first serverless NEG
     * `SERVERLESS_NEG_NAME_2`: the name of the second serverless NEG
  3. Update the backend service by importing the latest configuration.
         
         gcloud compute backend-services import BACKEND_SERVICE_NAME \
           --source=BACKEND_SERVICE_NAME.yaml --global
         

Outlier detection is now enabled on the backend service.




## Delete a serverless NEG

A network endpoint group cannot be deleted if it is attached to a backend service. Before you delete a NEG, ensure that it is detached from the backend service.

###  Console 

  1. To make sure the serverless NEG you want to delete is not currently in use by any backend service, go to the **Backend services** tab in the **Load balancing advanced menu**.  
[Go to the Backend services tab](https://console.cloud.google.com/networking/loadbalancing/advanced/backendServices/list)
  2. If the serverless NEG is currently in use: 
     1. Click the name of the backend service using the serverless NEG.
     2. Click **Edit** edit.
     3. From the list of **Backends** , click delete to remove the serverless NEG backend from the backend service.
     4. Click **Save**.
  3. Go to the **Network endpoint group** page in the Google Cloud console.  
[Go to the Network Endpoint Group page](https://console.cloud.google.com/compute/networkendpointgroups/list)
  4. Select the checkbox for the serverless NEG you want to delete.
  5. Click **Delete**.
  6. Click **Delete** again to confirm.



###  gcloud 

To remove a serverless NEG from a backend service, you must specify the region where the NEG was created. You must also specify the `--global` flag because `helloworld-backend-service` is a global resource.
    
    
    gcloud compute backend-services remove-backend helloworld-backend-service \
        --network-endpoint-group=helloworld-serverless-neg \
        --network-endpoint-group-region=us-central1 \
        --global
    

To delete the serverless NEG:
    
    
    gcloud compute network-endpoint-groups delete helloworld-serverless-neg \
        --region=us-central1
    

## What's next

  * [Using logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring)
  * [Troubleshooting serverless NEGs issues](https://docs.cloud.google.com/load-balancing/docs/https/troubleshooting-ext-https-lbs#serverless-negs)
  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup)
  * [Using a Terraform module for an external HTTPS load balancer with a Cloud Run backend](https://docs.cloud.google.com/load-balancing/docs/https/ext-http-lb-tf-module-examples#cloud-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
