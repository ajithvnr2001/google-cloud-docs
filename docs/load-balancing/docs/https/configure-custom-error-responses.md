---
url: https://docs.cloud.google.com/load-balancing/docs/https/configure-custom-error-responses/
title: Configure custom error responses \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:40.074047+00:00
---

# Configure custom error responses  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/configure-custom-error-responses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Configure custom error responses Stay organized with collections  Save and categorize content based on your preferences. 

This document provides example configurations of custom error responses. Before you configure a custom error response, read the [Custom error response overview](https://docs.cloud.google.com/load-balancing/docs/https/custom-error-response).

The example configurations described on this page configure a custom error response policy at three levels of the [URL map resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps)—the load balancer level, the URL domain level, and the URL path level.

The example configurations draw on concepts and build on setups described in the following documents:

  * [Set up a global external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute)
  * [Create backend buckets](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-buckets#prepare_your_buckets_and_content)
  * [How URL maps work](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#how_url_maps_work)
  * [Configure URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps)



## Example 1: Configure an error page for all `4xx` errors common to all hosts

This example assumes that you have set up a load balancer as described in [Set up a global external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute).

In this example, requests to the load balancer are routed to the backend service named `web-backend-service`. If the request encounters a `4xx` response, the custom error response policy is configured to then send the request to the error service, and an error object (`not-found.html`) is returned to the client.

To create a custom error response policy, follow these steps:

  1. Upload the HTML error page (`not-found.html`) to the Cloud Storage bucket.
         
         gcloud storage cp Desktop/not-found.html gs://GCS_BUCKET_NAME/
         

  2. Export the URL map (`web-map-http`) into a file named `web-map-http.yaml`.
         
         gcloud compute url-maps export web-map-http --destination web-map-http.yaml
         

Before you add the custom error response policy, the URL map (`web-map-http`) has a configuration similar to the following.
         
         creationTimestamp: '2020-01-14T19:12:44.680-08:00'
         defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/web-backend-service
         fingerprint: d0eJJpCBpHg=
         kind: compute#urlMap
         name: web-map-http
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/web-map-http
         

  3. Edit `web-map-http.yaml` to add a custom error response policy as highlighted in the following YAML configuration, in the `defaultCustomErrorResponsePolicy` section. In this example, an error response policy is configured at the load balancer level (`urlMaps.defaultCustomErrorResponsePolicy`).
         
         creationTimestamp: '2020-01-14T19:12:44.680-08:00'
         defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/web-backend-service
         defaultCustomErrorResponsePolicy:
           errorResponseRules:
             - matchResponseCodes:
               - 4xx
               path: '/not-found.html'
           errorService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/CUSTOM_ERRORS_BUCKET
         fingerprint: d0eJJpCBpHg=
         kind: compute#urlMap
         name: web-map-http
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/web-map-http
         

We recommend that you store all your error objects in a Cloud Storage bucket and have them referenced by a backend bucket attached to your load balancer. Cloud Storage buckets provide a simple way for you to store your error objects and have them returned to your clients by using the load balancer. However, you can also serve error pages and related assets without using a backend bucket. For example, you can use a backend service, which references a VM instance group backend that has an Apache server configured to serve a custom error response page.

  4. Update the URL map by importing the latest configuration from `web-map-http.yaml`.
         
         gcloud compute url-maps import web-map-http --source web-map-http.yaml
         

  5. After you update the URL map, you need to wait for some time before you can start sending traffic to your load balancer's IP address.

Send a request for a page that does not exist.
         
         curl -I http://IP_ADDRESS/a-page-that-does-not-exist
         

The error content from `not-found.html` is served and an HTTP `404` status code is returned.




## Example 2: Configure an error page for a specific error code for a specific host

This example builds on the previous example—Configure an error page for all `4xx` errors common to all hosts. It assumes that a load balancer is already configured such that requests to the host `video.example.com` are routed to the backend service named `video-backend-service`. If a request fails authorization by the backend service, the service returns a `401 (Unauthorized)` response. The custom error response policy is configured to then send the request to the error service, and an error object (`video-obtain-authorization.html`) is returned to the client.

In most cases, your error content is likely to contain links to assets—for example, a logo image. The client makes requests for assets referenced in the error page, and additional requests are sent to the load balancer to fetch them. The load balancer then responds to the request and returns the linked assets. This is accomplished by storing these assets in the same backend bucket specified in `defaultCustomErrorResponsePolicy` and adding a rule to route requests from asset URLs (for example, `/assets/logo.svg`) to the backend bucket. The load balancer's response to the request for linked assets is not an error response, but a normal response, as shown in the following configuration.
    
    
    pathMatchers:
    ...
      pathRules:
      - service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/CUSTOM_ERRORS_BUCKET
        paths:
        - /assets
    

The policy also lets you define what the final response code for the request should be. In this example, the response code has changed from `401` to `200` by specifying the value of `overrideResponseCode` to `200`. For all other `4xx` errors, the error content in `not-found.html` is returned to the client, and the original HTTP response code from the backend service is preserved.

As shown in the following table, two custom error response policies are configured in this example. These policies are created at the load balancer level and the URL domain level.

Policy level | API field | Match HTTP response code | Error service | Error object returned  
---|---|---|---|---  
URL domain | `pathMatchers[].defaultCustomErrorResponsePolicy` | 401 | `CUSTOM_ERRORS_BUCKET` | `video-obtain-authorization.html`  
Load balancer | `urlMaps.defaultCustomErrorResponsePolicy` | All 4xx | `CUSTOM_ERRORS_BUCKET` | `not-found.html`  
  
To create a custom error response policy for a `401` error code for the host `video.example.com`, follow these steps:

  1. Upload the HTML error page (`video-obtain-authorization.html`) and related assets (`logo.svg`) to the Cloud Storage bucket.
         
         gcloud storage cp Desktop/video-obtain-authorization.html gs://GCS_BUCKET_NAME/
         gcloud storage cp Desktop/logo.svg gs://GCS_BUCKET_NAME/assets/
         

  2. Export the URL map (`web-map-http`) into a file named `web-map-http.yaml`.
         
         gcloud compute url-maps export web-map-http --destination web-map-http.yaml
         

  3. Edit `web-map-http.yaml` to add a custom error response policy as highlighted in the following YAML configuration, in the `defaultCustomErrorResponsePolicy` section. In this example, a custom error response policy is configured at the load balancer level (`urlMaps.defaultCustomErrorResponsePolicy`) and the URL domain level (`pathMatchers[].defaultCustomErrorResponsePolicy`).

Because the error service is not defined at the URL domain level, the error service at the URL domain level defaults to the error service defined at the higher level; that is, the load balancer level.
         
         creationTimestamp: '2020-01-14T19:12:44.680-08:00'
         defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/web-backend-service
         defaultCustomErrorResponsePolicy:
           errorResponseRules:
             - matchResponseCodes:
               - 4xx
               path: '/not-found.html'
           errorService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/CUSTOM_ERRORS_BUCKET
         fingerprint: d0eJJpCBpHg=
         hostRules:
         - hosts:
           - video.example.com
           pathMatcher: path-matcher-1
         kind: compute#urlMap
         name: web-map-http
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/web-map-http
         pathMatchers:
         - defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-backend-service
           name: path-matcher-1
           defaultCustomErrorResponsePolicy:
             errorResponseRules:
               - matchResponseCodes:
                 - 401
                 path: "/video-obtain-authorization.html
                 overrideResponseCode: 200
             // The `errorService` in `pathMatchers[].defaultCustomErrorResponsePolicy` references the
             // error service configured in `urlMaps.defaultCustomErrorResponsePolicy`.
         
           // A URL map path rule to route requests from asset URLs (for example, "/assets/logo.svg") to the backend bucket.
           pathRules:
           - service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/CUSTOM_ERRORS_BUCKET
             paths:
             - /assets
         

  4. Update the URL map by importing the latest configuration from `web-map-http.yaml`.
         
         gcloud compute url-maps import web-map-http --source web-map-http.yaml
         

  5. After you update the URL map, you need to wait for some time before you can start sending traffic to your load balancer's IP address.

Send a request to your host for a URL that needs authorization.
         
         curl -I http://video.example.com/a-page-that-needs-authorization
         

The error content from `video-obtain-authorization.html` is served, and an HTTP `200` status code is returned.




## Example 3: Configure granular custom error response policies for different domains, paths, and error response codes

This example shows how you can customize specific error responses for different URL domains, URL paths, and HTTP error response codes.

The custom error response configuration, explained in this example, assumes the following:

  * You have [configured a URL map for an external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#example_url_map_workflow_with_an) with a host and path-based routing as depicted in the following image.

[ ![Example backend service setup](https://docs.cloud.google.com/static/load-balancing/images/url-map-model.svg)](https://docs.cloud.google.com/static/load-balancing/images/url-map-model.svg) Example backend service setup (click to enlarge) 
  * You have configured two backend buckets named `BUCKET_1` and `BUCKET_2` to return the custom error pages.




As shown in the following table, four custom error response policies are configured in this example. These policies are created across three levels in the following order of precedence:

  1. URL path (`pathMatchers[].pathRules[].customErrorResponsePolicy`)
  2. URL domain (`pathMatchers[].defaultCustomErrorResponsePolicy`)
  3. Load balancer (`urlMaps.defaultCustomErrorResponsePolicy`)

Policy level | Request URL | Match HTTP response code | Error service | Error object returned  
---|---|---|---|---  
URL path | `example.net/video/hd/*` | 404 | `BUCKET-2` | `not-found-hd-videos-404.html`  
URL path | `example.net/video/sd/*` | 404 | `BUCKET-2` | `not-found-sd-videos-404.html`  
URL domain | `example.net/*` | All 4xx | `BUCKET-1` | `example-net-4xx.html`  
Load balancer | `Any` | All 4xx or 5xx | `BUCKET-1` | `error-page-generic.html`  
  
The custom error response policy at the _load balancer_ level is applied only if the policy matches the error conditions and no matching policy has been defined for the error code at the lower levels; that is, the URL domain or the URL path. Similarly, the custom error response policy at the _URL domain_ level is applied only if the policy matches the error conditions and no matching policy has been defined for the error code at the lower level; that is, the URL path. In this example, if a request to the URL `www.example.net/video/hd` encounters a `404` response, then the file `not-found-hd-videos-404.html` is returned. However, if a `404` response is encountered for a request to the URL `www.example.net/video/`, then the file `example-net-4xx.html` is returned.

To create custom error response policies across three levels of the URL map, follow these steps:

  1. Upload the error objects to the Cloud Storage buckets.
         
         gcloud storage cp Desktop/error-page-generic.html gs://GCS_BUCKET_1_NAME/
         gcloud storage cp Desktop/example-net-4xx.html gs://GCS_BUCKET_1_NAME/
         gcloud storage cp Desktop/not-found-sd-videos-404.html gs://GCS_BUCKET_2_NAME/
         gcloud storage cp Desktop/not-found-hd-videos-404.html gs://GCS_BUCKET_2_NAME/
         

  2. Export the URL map (`video-org-url-map`) into a file named `video-org-url-map.yaml.`
         
         gcloud compute url-maps export video-org-url-map --destination video-org-url-map.yaml
         

Before you add the custom error response policy, the URL map (`video-org-url-map`) has a configuration similar to the following.
         
         creationTimestamp: '2021-03-05T13:34:15.833-08:00'
         defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/org-site
         fingerprint: mfyJIT7Zurs=
         hostRules:
         - hosts:
           - '*'
           pathMatcher: video-matcher
         - hosts:
           - example.net
           pathMatcher: video-matcher
         id: '8886405179645041976'
         kind: compute#urlMap
         name: video-org-url-map
         pathMatchers:
         - defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-site
           name: video-matcher
           pathRules:
           - paths:
             - /video/hd
             - /video/hd/*
             service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-hd
           - paths:
             - /video/sd
             - /video/sd/*
             service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-sd
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/video-org-url-map
         

  3. Edit `video-org-url-map.yaml` to add custom error response policies as highlighted in the following YAML configuration, in the `defaultCustomErrorResponsePolicy` section.

Because the error service is not defined at the URL domain level, the error service at the URL domain level defaults to the error service defined at the higher level; that is, the load balancer level.
         
         creationTimestamp: '2021-03-05T13:34:15.833-08:00'
         defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/org-site
         fingerprint: mfyJIT7Zurs=
         hostRules:
         - hosts:
           - '*'
           pathMatcher: video-matcher
         - hosts:
           - example.net
           pathMatcher: video-matcher
         id: '8886405179645041976'
         kind: compute#urlMap
         name: video-org-url-map
         defaultCustomErrorResponsePolicy:
           errorResponseRules:
             - matchResponseCodes:
               - 4xx
               - 5xx
               path: '/error-page-generic.html'
           errorService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/BUCKET-1
         pathMatchers:
         - defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-site
           name: video-matcher
           defaultCustomErrorResponsePolicy:
               errorResponseRules:
                 - matchResponseCodes:
                   - 4xx
                   path: '/example-net-4xx.html'
               // The `errorService` in `pathMatchers[].defaultCustomErrorResponsePolicy` references the
               // error service configured in `urlMaps.defaultCustomErrorResponsePolicy`.
           pathRules:
           - paths:
             - /video/hd
             - /video/hd/*
             service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-hd
             customErrorResponsePolicy:
                   errorResponseRules:
                     - matchResponseCodes:
                       - 404
                       path: '/not-found-hd-videos-404.html'
                   errorService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/BUCKET-2
           - paths:
             - /video/sd
             - /video/sd/*
             service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-sd
             customErrorResponsePolicy:
                   errorResponseRules:
                     - matchResponseCodes:
                       - 404
                       path: '/not-found-sd-videos-404.html'
                   errorService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/BUCKET-2
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/video-org-url-map
         

  4. Update the URL map by importing the latest configuration from `video-org-url-map.yaml`.
         
         gcloud compute url-maps import video-org-url-map --source video-org-url-map.yaml
         

  5. After you update the URL map, you need to wait for some time before you can start sending traffic to your load balancer's IP address.

Send a request for a page that does not exist.
         
         curl -I http://example.net/a-page-that-does-not-exist
         

The error content from `example-net-4xx.html` is served.

Similarly, test for other URLs with different URL domains and URL paths.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
