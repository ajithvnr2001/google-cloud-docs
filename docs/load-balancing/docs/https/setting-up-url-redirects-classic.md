---
url: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-url-redirects-classic/
title: Set up a URL redirect for a classic Application Load Balancer \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:40.090739+00:00
---

# Set up a URL redirect for a classic Application Load Balancer  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-url-redirects-classic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a URL redirect for a classic Application Load Balancer Stay organized with collections  Save and categorize content based on your preferences. 

This example demonstrates how to use [URL redirects](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#url-redirects) to redirect all incoming requests to a different host or path.

## Related content

This page is for a classic Application Load Balancer only. If you are using a load balancer in a different mode, see one of the following pages:

  * [Configure a URL redirect for global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#configure_a_url_redirect)

  * [Configure a URL redirect for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#configure_a_url_redirect)




If you're trying to set up an HTTP-to-HTTPS redirect, see [Set up an HTTP-to-HTTPS redirect for a classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-http-https-redirect).

## Add a URL redirect

###  Console 

  1. Go to your list of load balancers in the Google Cloud console.   
[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list/loadBalancers)
  2. For a load balancer of type **HTTP(S) (Classic)** , click the load balancer's name link.
  3. Click **Edit** edit.
  4. In **Host and path rules** , select **Advanced host and path rule (URL redirect, URL rewrite)**.
  5. Click **Add host and path rule**.
  6. In the **Hosts** field, enter *****.
  7. Click edit.
  8. For the **Action** , select **Redirect the client to different host/path**.
  9. For the host redirect, enter a hostname to redirect to, or omit to keep the requested host.
  10. For **Path redirect** , select **Full path redirect**.
  11. For **Path value** , enter a path to redirect to, or omit to keep the requested path.
  12. For **Strip query** , click **Enable**.
  13. Click **Save** to finish configuring the host and path rule.
  14. Click **Done** to finish editing the URL map.
  15. Click **Update** to finish editing the load balancer.



###  gcloud 

The following example returns a configurable 3xx response code, sets the `Location` response header with the appropriate URI, and replaces the host and path as specified in the redirect action.

  1. Export the existing URL map using the [`gcloud compute url-maps export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/export) command:
         
         gcloud compute url-maps export web-map-http \
           --destination=lb-map-config.yaml \
           --global
         

  2. Update the URL map file `lb-map-config.yaml` by adding this to the end of the file:
         
         hostRules:
         - hosts:
           - '*'
           pathMatcher: path-matcher-1
         name: web-map-http
         pathMatchers:
         - defaultUrlRedirect:
             hostRedirect: NEW_HOSTNAME # Omit to keep the requested host
             httpsRedirect: false
             pathRedirect: /NEW_PATH # Omit to keep the requested path
             redirectResponseCode: MOVED_PERMANENTLY_DEFAULT
             stripQuery: true
           name: path-matcher-1
         

  3. Update the URL map using the [`gcloud compute url-maps import`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/import) command:
         
         gcloud compute url-maps import web-map-http \
            --global \
            --source=lb-map-config.yaml
         




## What's next

  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
