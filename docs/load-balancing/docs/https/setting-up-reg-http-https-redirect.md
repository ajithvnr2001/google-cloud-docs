---
url: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-http-https-redirect/
title: Set up an HTTP-to-HTTPS redirect for regional external Application Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:22.594555+00:00
---

# Set up an HTTP-to-HTTPS redirect for regional external Application Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-http-https-redirect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up an HTTP-to-HTTPS redirect for regional external Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set up an HTTP-to-HTTPS redirect for the regional external Application Load Balancer. This page is for a regional external Application Load Balancer only. If you use a load balancer in a different mode, see one of the following pages: 

  * [Set up an HTTP-to-HTTPS redirect for global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-http-https-redirect)

  * [Set up an HTTP-to-HTTPS redirect for a classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-http-https-redirect)




This example shows how to use [URL map redirects](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#url-redirects) to redirect all requests from HTTP to HTTPS. This example shows how you set up redirects by using the well-known ports 80 (for HTTP) and 443 (for HTTPS). However, you're not required to use these specific port numbers. Each forwarding rule for an Application Load Balancer can reference a [single port from 1-65535](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications).

HTTPS uses TLS (SSL) to encrypt HTTP requests and responses, making it safer and more secure. A website that uses HTTPS has `https://` in the beginning of its URL instead of `http://`.

## For new HTTPS load balancers

Regional external Application Load Balancers don't support creating HTTP-to-HTTPS redirects while creating a new load balancer. You'll need to first use the instructions from the [Compute Engine backend guide](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb) to create a new load balancer. You can then use the instructions in the next section to set up a redirect for all requests from HTTP to HTTPS.

This procedure assumes that you already have an external HTTPS load balancer that is serving HTTPS traffic on port 443.

## For existing load balancers

If you already have an HTTPS Application Load Balancer (called here _LB1_) that is serving HTTPS traffic on port 443, you must create a partial _HTTP_ Application Load Balancer (called here _LB2_) with the following setup:

  * The same frontend IP address used by LB1
  * A redirect configured in the URL map



This partial HTTP load balancer uses the same IP address as your HTTPS load balancer and redirects HTTP requests to your load balancer's HTTPS frontend.

This architecture is shown in the following diagram.

[ ![HTTP-to-HTTPS redirect configuration architecture.](https://docs.cloud.google.com/static/load-balancing/images/http-to-https-redirect.svg)](https://docs.cloud.google.com/static/load-balancing/images/http-to-https-redirect.svg) **Figure 2.** HTTP-to-HTTPS redirect configuration architecture (click to enlarge).

### Redirecting traffic to your HTTPS load balancer

After you have verified that your HTTPS load balancer (LB1) is working, you can create the partial HTTP load balancer (LB2) with its frontend configured to redirect traffic to LB1.

This example uses the 301 response code. You can instead use a different [response code](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management#response-codes).

To configure the redirect with `gcloud`, you must import a YAML file and make sure that your target HTTP proxy points to the URL map that redirects traffic. If you're using the Google Cloud console, this is handled for you.

Regional external Application Load Balancers aren't supported in the Google Cloud console.

### gcloud

  1. Create a YAML file `/tmp/web-map-http.yaml`. This example uses MOVED_PERMANENTLY_DEFAULT as the response code.
    
    kind: compute#urlMap
           name: web-map-http
           defaultUrlRedirect:
             redirectResponseCode: MOVED_PERMANENTLY_DEFAULT
             httpsRedirect: True
           tests:
           - description: Test with no query parameters
             host: example.com
             path: /test/
             expectedOutputUrl: https://example.com/test/
             expectedRedirectResponseCode: 301
           - description: Test with query parameters
             host: example.com
             path: /test/?parameter1=value1&parameter2=value2
             expectedOutputUrl: https://example.com/test/?parameter1=value1&parameter2=value2
             expectedRedirectResponseCode: 301
           

  2. Create the HTTP load balancer's URL map by importing the YAML file. The name for this URL map is `web-map-http`.
    
    gcloud compute url-maps import web-map-http \
               --source /tmp/web-map-http.yaml \
               --region=REGION
           

If you are updating an existing URL map, the following prompt appears:
    
    Url Map [web-map-http] will be overwritten.
    
           Do you want to continue (Y/n)?
           

To continue, press **Y**.

  3. Verify that the URL map is updated. Your HTTP load balancer's URL map should look something like this:
    
    gcloud compute url-maps describe web-map-http \
               --region=REGION
           
    
    creationTimestamp: '2020-03-23T10:53:44.976-07:00'
           defaultUrlRedirect:
             httpsRedirect: true
             redirectResponseCode: MOVED_PERMANENTLY_DEFAULT
           fingerprint: 3A5N_RLrED8=
           id: '2020316695093397831'
           kind: compute#urlMap
           name: web-map-http
           selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/urlMaps/web-map-http
           

  4. Create a new target HTTP proxy or update an existing target HTTP proxy, using `web-map-http` as the URL map.
    
    gcloud compute target-http-proxies create http-lb-proxy \
               --url-map=web-map-http \
               --region=REGION
           

OR 
    
    gcloud compute target-http-proxies update http-lb-proxy \
               --url-map=web-map-http \
               --region=REGION
           

  5. Create a forwarding rule to route incoming requests to the proxy. The `--address` flag specifies `lb-ipv4-1`, which is the same IP address used for the external HTTPS load balancer.
    
    gcloud compute forwarding-rules create http-content-rule \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --address=lb-ipv4-1 \
               --network-tier=STANDARD \
               --region=REGION \
               --target-http-proxy=http-lb-proxy \
               --target-http-proxy-region=REGION \
               --ports=80
           




## Testing the HTTP-to-HTTPS redirect

Note the reserved IP address that you are using for both load balancers.
    
    
    gcloud compute addresses describe lb-ipv4-1   
    
        --format="get(address)"   
    
        --region=REGION
    

**Important:** If **LB1** and **LB2** don't have the same IP address, the redirect won't work. In this case, [delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/delete) the forwarding rule in **LB2** (HTTP load balancer) and create a new one that uses the same IP address as the forwarding rule in **LB1** (HTTPS load balancer).

In this example, assume that the reserved IP address is `34.98.77.106`. The `http://34.98.77.106/` URL redirects to `https://34.98.77.106/`.

After a few minutes have passed, you can test this by running the following `curl` command.
    
    
    curl -v http://hostname.com
    

Sample output:
    
    
    * Connected to 34.98.77.106 (34.98.77.106) port 80 (#0)
    > GET / HTTP/1.1
    > Host: hostname.com
    > User-Agent: curl/7.64.0
    > Accept: */*
    >
    < HTTP/1.1 301 Moved Permanently
    < Cache-Control: private
    < Content-Type: text/html; charset=UTF-8
    < Referrer-Policy: no-referrer
    < Location: https://hostname.com
    < Content-Length: 220
    < Date: Fri, 30 Jul 2021 21:32:25 GMT
    <
    <HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
    <TITLE>301 Moved</TITLE></HEAD><BODY>
    <H1>301 Moved</H1>
    The document has moved
    <A HREF="https://hostname.com">here</A>.
    </BODY></HTML>
    * Connection #0 to host hostname.com left intact
    

## Related procedures

  * To use Terraform, see the [HTTP-to-HTTPS redirect tab](https://docs.cloud.google.com/load-balancing/docs/https/ext-http-lb-tf-module-examples#http-to-https-redirect).

  * For GKE, see the [HTTP-to-HTTPS redirects in the GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-features#https_redirect).

  * For internal Application Load Balancers, see [Setting up HTTP-to-HTTPS redirect for internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-http-to-https-redirect).

  * For other types of redirects, see [URL redirects](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#url-redirects).




## What's next

  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
