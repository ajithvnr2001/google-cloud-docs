---
url: https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-http-to-https-redirect/
title: Set up HTTP-to-HTTPS redirect for regional internal Application Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:20.337625+00:00
---

# Set up HTTP-to-HTTPS redirect for regional internal Application Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-http-to-https-redirect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up HTTP-to-HTTPS redirect for regional internal Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to use [URL map redirects](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#url-redirects) to redirect all internal Application Load Balancer requests from HTTP to HTTPS. The example on this page uses the well-known ports 80 (for HTTP) and 443 (for HTTPS). However, you're not required to use these specific port numbers. Each forwarding rule for an Application Load Balancer can reference a [single port from 1-65535](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications).

To configure HTTP-to-HTTPS redirects, you must create two load balancers, one for HTTPS traffic and another for HTTP traffic. Each load balancer has its own forwarding rule, target proxy, and URL map, but they share the same IP address. For the HTTP load balancer, you don't need to configure a backend because the frontend redirects traffic to the HTTPS load balancer's backend.

At a high level, to redirect HTTP traffic to HTTPS, you must do the following:

  1. Create a regular internal _HTTPS_ load balancer with a reserved, shared internal IP address.
  2. Test the load balancer to make sure that it's working.
  3. Redirect traffic to the HTTPS load balancer.

To do this, you must create a partial internal _HTTP_ load balancer that only has a frontend. The frontend receives requests and then redirects them to the HTTPS load balancer by using the following resources:

     * A forwarding rule with the same reserved internal IP address as the HTTPS load balancer you created in step 1
     * A target HTTP proxy
     * A URL map that redirects traffic to the HTTPS load balancer



As shown in the following diagram, the HTTPS load balancer is a regular load balancer with the expected [Internal Application Load Balancer components](https://docs.cloud.google.com/load-balancing/docs/l7-internal#components).

The HTTP load balancer has the same IP address as the HTTPS load balancer and a redirect instruction in the URL map.

[ ![Internal HTTP-to-HTTPS redirect configuration.](https://docs.cloud.google.com/static/load-balancing/images/internal-http-to-https-redirect.svg)](https://docs.cloud.google.com/static/load-balancing/images/internal-http-to-https-redirect.svg) Internal HTTP-to-HTTPS redirect configuration (click to enlarge).

## Create the internal HTTPS load balancer

To set up a regional internal Application Load Balancer, use the instructions at [setting up an internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal).

If you already have a functioning regional internal Application Load Balancer, make sure that it has a [reserved, shared IP address for the forwarding rule](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#reserve-ip), and then move on to the next section, Redirect traffic to your HTTPS load balancer.

For _cross-region internal Application Load Balancers_ , use the instructions in [Set up a cross-region internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal) to create two load balancers, and then follow the instructions in Redirect traffic to your HTTPS load balancer.

## Redirect traffic to your HTTPS load balancer

Create a _partial HTTP load balancer_ that has the same IP address as the HTTPS load balancer created in the previous step. The partial load balancer redirects traffic from port `80` to port `443`.

###  Console 

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Internal** and click **Next**.
  5. For **Cross-region or single region deployment** , select **Best for regional workloads** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

  1. For the name of the load balancer, enter `l7-ilb-http-redirect`.
  2. For **Region** , select `us-west1`.
  3. For **Network** , select `lb-network`.



#### Configure the backend service

  1. Click **Backend configuration**.
  2. In the **Select backend services** menu, select the existing backend service `l7-ilb-backend-service`.
  3. Click **OK**.



#### Configure the URL map

  1. Click **Routing rules**.
  2. For **Mode** , select **Advanced host and path rule**.
  3. Click **Add host and path rule**.
  4. Set **Hosts** to `*`.

  5. For **Path matcher (matches, actions and services)** , enter the following code: 
         
         name: matcher1
         defaultUrlRedirect:
           httpsRedirect: true
           hostRedirect: IP_ADDRESS:443
           redirectResponseCode: PERMANENT_REDIRECT

  6. Ensure that the `l7-ilb-backend-service` is the only backend service for any unmatched host and any unmatched path.




For information about traffic management, see [Set up traffic management for internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management).

#### Configure the frontend for HTTP

  1. Click **Frontend configuration**.
  2. Set the name of the forwarding rule to `l7-ilb-forwarding-rule`.
  3. Set **Protocol** to `HTTP`.
  4. Set the **Subnetwork** to `backend-subnet`.
  5. Set the **Port** to `80`.
  6. In the **IP address** menu, select the shared IP address that was reserved for the HTTPS load balancer forwarding rule.
  7. Click **Done**.



#### Review the configuration

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Optional: Click **Equivalent code** to view the REST API request that will be used to create the load balancer.
  4. Click **Create**.



###  gcloud 

  1. Create a new URL map by creating a YAML file with the traffic redirect configuration. Replace IP_ADDRESS with the shared IP address that was reserved for the HTTPS load balancer forwarding rule.
         
         defaultService: regions/us-west1/backendServices/l7-ilb-backend-service
         kind: compute#urlMap
         name: l7-ilb-redirect-url-map
         hostRules:
         - hosts:
          - '*'
          pathMatcher: matcher1
         pathMatchers:
         - name: matcher1
          defaultUrlRedirect:
                hostRedirect: IP_ADDRESS:443
                redirectResponseCode: PERMANENT_REDIRECT
                httpsRedirect: True

  2. Import the YAML file to the new URL map:
         
         gcloud compute url-maps import l7-ilb-redirect-url-map \
            --source=/tmp/url_map.yaml \
            --region=us-west1
         

  3. Create the HTTP load balancer's target proxy:
         
         gcloud compute target-http-proxies create l7-ilb-http-proxy \
            --url-map=l7-ilb-redirect-url-map \
            --region=us-west1
         

  4. Create a new forwarding rule and the shared IP address:
         
         gcloud compute forwarding-rules create l7-ilb-forwarding-rule \
            --load-balancing-scheme=INTERNAL_MANAGED \
            --network=lb-network \
            --subnet=backend-subnet \
            --address=IP_ADDRESS \
            --ports=80 \
            --region=us-west1 \
            --target-http-proxy=l7-ilb-http-proxy \
            --target-http-proxy-region=us-west1
         




## Test the traffic redirect

  1. Connect to your client VM.
         
         gcloud compute ssh l7-ilb-client-us-west1-a \
            --zone=us-west1-a
         

  2. Send an HTTP request to IP_ADDRESS on port `80`, and expect a traffic redirect.
         
         curl -L -k IP_ADDRESS

  3. View the sample output.
         
         Page served from: l7-ilb-backend-w11t
         

Add `-vvv` to see more details.
         
         curl -L -k IP_ADDRESS -vvv
         
         
         

     * Rebuilt URL to: IP_ADDRESS/
     * Trying IP_ADDRESS...
     * TCP_NODELAY set
     * Connected to IP_ADDRESS (IP_ADDRESS) port 80 (#0) > GET / HTTP/1.1 > Host: IP_ADDRESS > User-Agent: curl/7.52.1 > Accept: _/_ > < HTTP/1.1 308 Permanent Redirect < location: https://IP_ADDRESS:443/ < date: Fri, 07 Aug 2020 05:07:18 GMT < via: 1.1 google < content-length: 0 <
     * Curl_http_done: called premature == 0
     * Connection #0 to host IP_ADDRESS left intact
     * Issue another request to this URL: 'https://IP_ADDRESS:443/'
     * Trying IP_ADDRESS...
     * TCP_NODELAY set
     * Connected to IP_ADDRESS (IP_ADDRESS) port 443 (#1)
     * ALPN, offering h2
     * ALPN, offering http/1.1
     * Cipher selection: ALL:!EXPORT:!EXPORT40:!EXPORT56:!aNULL:!LOW:!RC4:@STRENGTH
     * successfully set certificate verify locations:
     * CAfile: /etc/ssl/certs/ca-certificates.crt CApath: /etc/ssl/certs ... ...
     * SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
     * ALPN, server accepted to use h2
     * Server certificate:
     * subject: O=Google TESTING; CN=test_cert_1
     * start date: Jan 1 00:00:00 2015 GMT
     * expire date: Jan 1 00:00:00 2025 GMT
     * issuer: O=Google TESTING; CN=Intermediate CA
     * SSL certificate verify result: unable to get local issuer certificate (20), continuing anyway.
     * Using HTTP2, server supports multi-use
     * Connection state changed (HTTP/2 confirmed)
     * Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
     * Using Stream ID: 1 (easy handle 0x561a6b0e3ea0) > GET / HTTP/1.1 > Host: IP_ADDRESS > User-Agent: curl/7.52.1 > Accept: _/_ >
     * Connection state changed (MAX_CONCURRENT_STREAMS updated)! < HTTP/2 200 < date: Fri, 07 Aug 2020 05:07:18 GMT < server: Apache/2.4.25 (Debian) < last-modified: Thu, 06 Aug 2020 13:30:21 GMT < etag: "2c-5ac357d7a47ec" < accept-ranges: bytes < content-length: 44 < content-type: text/html < via: 1.1 google < Page served from: l7-ilb-backend-https-w11t
     * Curl_http_done: called premature == 0
     * Connection #1 to host IP_ADDRESS left intact



## What's next

  * To learn how internal Application Load Balancers work, see [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal).

  * To manage the proxy-only subnet resource required by internal Application Load Balancers, see [Proxy-only subnet for internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/proxy-only-subnets).

  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
