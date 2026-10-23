---
url: https://docs.cloud.google.com/load-balancing/docs/tutorials/http-https-over-same-domain/
title: Deliver HTTP and HTTPS content over the same published domain \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:42.536022+00:00
---

# Deliver HTTP and HTTPS content over the same published domain  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/tutorials/http-https-over-same-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Deliver HTTP and HTTPS content over the same published domain Stay organized with collections  Save and categorize content based on your preferences. 

It is common to deliver HTTP and HTTPS content over the same hostname when using Cloud CDN. While many browsers enforce the use of Transport Layer Security (TLS) and disallow non-secure content delivery, there are still use cases where non-secure delivery and secure delivery must be allowed over the same hostname. This article discusses how you can achieve this functionality using Cloud CDN.

## Challenge

When a client is establishing a connection with a CDN edge server, the end-user delivery protocol is negotiated. Most conventional CDN platforms direct traffic to their respective delivery footprint by:

  1. Pointing to a domain name belonging to the CDN, using a DNS CNAME record.
  2. Routing traffic to a subset of servers that support TLS negotiation for that domain name.



Because Cloud CDN integrates with Cloud Load Balancing, Cloud CDN's approach differs from the approach of conventional CDNs. Cloud CDN leverages the Anycast IP address of the external Application Load Balancer. When configuring Cloud CDN, you have a specific IP address to direct traffic to. This requires an A record (for IPv4) and/or AAAA (for IPv6) record construct in your DNS record, rather than a CNAME record with a hostname value.

By default, when configuring the frontend of the load balancer, Google Cloud dynamically assigns an ephemeral IP address. Because you need to configure your HTTP and HTTPS configurations separately, this can cause you to have two IP addresses for your Cloud CDN instance. Because the same A or AAAA record IP address is for both HTTP and HTTPS, it's not possible to properly handle this case in DNS.

## Solution

When delivering both secure and non-secure content over the same hostname, the client is directed to an edge server that can negotiate either HTTP or HTTPS. To make this work with Cloud CDN, you can reserve an IP address and bind the reserved IP address to both the HTTP and HTTPS frontend configuration in the external Application Load Balancer.

[ ![HTTP and HTTPS over the same domain](https://docs.cloud.google.com/static/cdn/images/cdn-hybrid-ipv4-ipv6.svg)](https://docs.cloud.google.com/static/cdn/images/cdn-hybrid-ipv4-ipv6.svg) HTTP and HTTPS over the same domain

In the diagram:

  * incoming requests for www.example.com come from clients using HTTP/2, HTTPS, and HTTP.
  * Two IP addresses are reserved, one for IPv4 and one for IPv6:

    * 34.95.111.204
    * [2600:1901:0:b13e::]
  * These two IP addresses are bound to www.example.com in Cloud DNS.

  * When configuring the external Application Load Balancer, the frontend configuration includes four forwarding rules that use the reserved IP addresses:

Name | Protocol | IP:Port  
---|---|---  
ipv4-http | HTTP | 34.95.111.204:80  
ipv4-https | HTTPS | 34.95.111.204:443  
ipv6-http | HTTP | [2600:1901:0:b13e::]:80  
ipv6-https | HTTPS | [2600:1901:0:b13e::]:443  
  * For Cloud CDN cache misses, the load balancer distributes requests to the backend origins, based on settings defined in the load balancer's URL map.




## Step 1: Reserve a global external IP address

Create an IPv4 or an IPv6 address (or both). To support IPv4 and IPv6 addressing, you must create one IPv4 address and one IPv6 address.

In your DNS record,create an A (or AAAA) record to direct traffic to this reserved IP address.

###  Console 

**Note:** For global external Application Load Balancers, the Google Cloud console isn't supported.

  1. In the Google Cloud console, go to the **External IP addresses** page. 

[Go to the External IP addresses page](https://console.cloud.google.com/addresses/list)

  2. Click **Reserve static address** to reserve an IPv4 address.
  3. Assign a **Name** of `ipv4-address`.
  4. Set the Network tier to **Premium**.
  5. Set the **IP version** to **IPv4**.
  6. Set the **Type** to **Global**.
  7. Click **Reserve**.



The load balancer uses [Premium Tier networking](https://docs.cloud.google.com/network-tiers/docs/overview#premium_tier), as required when Cloud CDN is enabled.

###  gcloud 
    
    
    gcloud compute addresses create ipv4-address \
        --network-tier=PREMIUM \
        --ip-version=IPV4 \
        --global
    

Note the IPv4 address that was reserved:
    
    
    gcloud compute addresses describe lb-ipv4-1 \
        --format="get(address)" \
        --global
    

Repeat this step for IPv6.

For more information, see [Reserving a new static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address).

## Step 2: Bind the reserved IP address to the load balancer

This section shows how to assign the IP address(es) to your load balancer. End-to-end instructions for setting up the load balancer are beyond the scope of this article. For an example setup, see [Creating an HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/https/https-load-balancer-example).

The frontend configuration section allows you to select the protocol used between the client and the load balancer.

In this example, you are using both HTTP and HTTPS between the client and the load balancer, so you need one or more SSL certificate resources to configure the proxy.

###  Console 

**Note:** For global external Application Load Balancers, the Google Cloud console isn't supported.

### Configuring the HTTP forwarding rule

  1. In the Google Cloud console, go to the **Load balancing** page. 

[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/add)

  2. Select your load balancer and click **Edit**.
  3. In the left panel, click **Frontend configuration**.
  4. In the **Name** field, enter `ipv4-http`.
  5. In the **Protocol** field, select `HTTP`.
  6. Set **IP version** to `IPv4`.
  7. In **IP address** , select `ipv4-address`, which you created earlier.
  8. Ensure that the **Port** is set to `80`, to allow HTTP traffic.
  9. Click **Done**.



### Configuring the HTTPS forwarding rule

  1. In the Google Cloud console, go to the **Load balancing** page. 

[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/add)

  2. Select your load balancer and click **Edit**.
  3. In the left panel, click **Frontend configuration**.
  4. In the **Name** field, enter `ipv4-https`.
  5. In the **Protocol** field, select `HTTPS`.
  6. Set **IP version** to `IPv4`.
  7. In **IP address** , select `ipv4-address`, which you created earlier.
  8. Ensure that the **Port** is set to `443`, to allow HTTP traffic.
  9. For **Choose certificate repository** , select **Use certificate map** or **Use classic certificates**.
  10. Depending on your selection, select a certificate map or a classic certificate.
  11. Click **Done**.



Repeat these steps for IPv6.

### Review and finalize

  1. In the left panel, click **Review and finalize**.
  2. Compare your settings to what you intended to create.
  3. If everything looks correct, click **Update**.



###  gcloud 

  1. Create a target HTTP proxy to route requests to your URL map.
         
         gcloud compute target-http-proxies create http-lb-proxy \
           --url-map=web-map
         

  2. Create a target HTTPS proxy to route requests to your URL map. The proxy is the portion of the load balancer that holds the SSL certificate for HTTPS Load Balancing, so you also load your certificate in this step.
         
         gcloud compute target-https-proxies create https-lb-proxy \
           --url-map=web-map --ssl-certificates=www-ssl-cert
         

  3. Create two global forwarding rules to route incoming requests to the proxy, one for each of the IP address(es) you created.

     * For a global external Application Load Balancer, use the gcloud CLI command with `load-balancing-scheme=EXTERNAL_MANAGED`. This setting offers [advanced traffic management capability](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global).
     * For an classic Application Load Balancer, use `load-balancing-scheme=EXTERNAL`.
    
    gcloud compute forwarding-rules create ipv4-http \
      --load-balancing-scheme=LOAD_BALANCING_SCHEME \
      --network-tier=PREMIUM \
      --address=ipv4-address \
      --global \
      --target-http-proxy=http-lb-proxy \
      --ports=80
    
    
    gcloud compute forwarding-rules create ipv4-https \
      --load-balancing-scheme=LOAD_BALANCING_SCHEME \
      --network-tier=PREMIUM \
      --address=ipv4-address  \
      --global \
      --target-https-proxy=https-lb-proxy \
      --ports=443
    




After creating the global forwarding rules, it can take several minutes for your configuration to propagate worldwide.

## Step 3: Create an A or AAAA record in your DNS zone file

The last step in the process is creating an A and/or AAAA record in your DNS zone file to point to Cloud CDN where your hostname value will answer with the reserved IP address(es) that you assigned on the load balancer.

Now, you can serve both HTTP and HTTPS over the same hostname through Cloud CDN.

### Optional: Redirecting HTTP to HTTPS

If you want to redirect HTTP requests to your HTTPS load balancer, you must add a partial HTTP load balancer that has a frontend but no backends. The frontend receives requests and then redirects them to the HTTPS load balancer. It does this by using the following:

  * A forwarding rule with the same reserved external IP address that your HTTPS load balancer uses, as shown on this page.
  * A target HTTP proxy, as shown on this page.
  * A URL map that [ redirects traffic to the HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-http-https-redirect#partial-http-lb). 



## Getting support

If you have questions about Google Cloud and Cloud CDN, contact your Google Cloud Sales team or reach out via the [Google Cloud Community Slack channel](https://googlecloud-community.slack.com/) and post a note in the #cloud-cdn channel.

## What's next?

  * For details about what content is cached, see [Caching details](https://docs.cloud.google.com/cdn/docs/caching).
  * For resolving load balancer issues, see the [load balancer troubleshooting page](https://docs.cloud.google.com/load-balancing/docs/https/troubleshooting-ext-https-lbs).
  * For resolving Cloud CDN issues, see the [Cloud CDN troubleshooting page](https://docs.cloud.google.com/cdn/docs/troubleshooting-steps).
  * For information about using Cloud CDN in GKE, see [Cloud CDN on the Ingress features page](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-features#cloud_cdn).
  * To check whether Cloud CDN is serving responses from cache, [View logs](https://docs.cloud.google.com/cdn/docs/logging).
  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
