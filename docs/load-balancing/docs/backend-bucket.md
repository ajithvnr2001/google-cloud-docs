---
url: https://docs.cloud.google.com/load-balancing/docs/backend-bucket/
title: Backend buckets overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:37.128323+00:00
---

# Backend buckets overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/backend-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Backend buckets overview Stay organized with collections  Save and categorize content based on your preferences. 

A backend bucket lets you use a Cloud Storage bucket as a backend for your Application Load Balancer. We recommend that you use backend buckets particularly when your application needs to serve _static_ content such as images or video.

If your application needs to serve _dynamic_ content over HTTP(S), use [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service) instead.

## Load balancer support

The following load balancers support the use of backend buckets:

  * Global external Application Load Balancer
  * Classic Application Load Balancer
  * Regional external Application Load Balancer
  * Cross-region internal Application Load Balancer
  * Regional internal Application Load Balancer



### Private Service Connect NEG deployments

Backend buckets offer a seamless, fully-integrated experience so that your load balancer can serve content directly from your Cloud Storage bucket.

However, Private Service Connect offers an alternative deployment type where you create a Private Service Connect NEG that points to Cloud Storage API endpoints, and then configure this NEG as a backend for a load balancer. This deployment type provides a private network path to the Cloud Storage API endpoints. However, note that this method doesn't inherently grant access to private buckets. Additionally, you are responsible for making sure that the client application can authenticate itself to Cloud Storage.

For details, see [Access global Google APIs through backends](https://docs.cloud.google.com/vpc/docs/access-global-google-apis-backends).

## Cloud CDN support

By default, Cloud Storage [uses the same cache](https://docs.cloud.google.com/storage/docs/caching) that Cloud CDN uses. While Cloud Storage does include built-in caching for its objects, we recommend that you enable Cloud CDN on your backend bucket for better performance delivering content to your users.

If you don't enable Cloud CDN on your backend bucket, you can only use origin `Cache-Control` headers to control caching for smaller content, as set by the Cloud Storage metadata.

If you do enable Cloud CDN on your backend bucket, you can use more Cloud CDN controls on your content such as cache modes, signed URLs, and cache invalidation. Cloud CDN also lets you cache content larger than 10 MiB. For more details and pricing considerations, see [Cloud Storage and Cloud CDN](https://docs.cloud.google.com/storage/docs/caching#cloud-cdn) in the Cloud Storage documentation.

## Sample architecture

In the following diagram, the external Application Load Balancer uses a URL map to direct traffic from specified URL paths to your backends.

The load balancer sends traffic with a URL path including `/love-to-fetch/` to a Cloud Storage bucket in the `us-east1` region. All other requests go to a Cloud Storage bucket in the `europe-north1` region.

[ ![The load balancer sends traffic to a Cloud Storage backend.](https://docs.cloud.google.com/static/load-balancing/images/lb-gcs-wo-cdn-paths.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-gcs-wo-cdn-paths.svg) Distributing traffic to Cloud Storage

## API and `gcloud` reference

For more information about the properties of the backend bucket resource, see the following reference documentation:

  * [Global backend bucket API resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets)
  * [Regional backend bucket API resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendBuckets)
  * [`gcloud compute backend-buckets` page](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets) (for global and regional resources)



## What's next

  * [Set up a global external Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-buckets)
  * [Set up a regional external Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/https/setup-reg-ext-app-lb-backend-buckets)
  * [Set up a classic Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/https/ext-load-balancer-backend-buckets)
  * [Set up a cross-region internal Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-cross-region-internal-https-buckets)
  * [Set up a regional internal Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-internal-buckets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
