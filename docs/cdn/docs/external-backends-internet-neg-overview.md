---
url: https://docs.cloud.google.com/cdn/docs/external-backends-internet-neg-overview/
title: External backends specified by using internet NEGs \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:06.321353+00:00
---

# External backends specified by using internet NEGs  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/external-backends-internet-neg-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  External backends specified by using internet NEGs Stay organized with collections  Save and categorize content based on your preferences. 

Use external backends (also called _custom origins_) for Cloud CDN (Content Delivery Network) when content is hosted on-premises or in another cloud, and you want to deliver the content over Google's [high performance](https://itm.cloud.com/google-reports/), distributed edge caching infrastructure.

## Terminology

The following terms are sometimes used interchangeably because they have the same or similar meanings:

  * **external backend:** A backend that resides outside of Google Cloud and is reachable across the internet. The endpoint in an internet NEG. 
  * **internet network endpoint group (NEG):** The Google Cloud API resource that you use to specify an external backend.
  * **external endpoint:** Same as an _external backend_.



To maintain consistency with the [load balancing documentation](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-external-backend-internet-neg), this document uses the term _external backend_ except when referring to the internet NEG API resource.

## Supported backend types for Cloud CDN

Cloud CDN works with an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) to deliver content to your users. The external Application Load Balancer provides the frontend IP addresses and ports that receive requests. Cloud CDN content can be sourced from various types of backends:

  * [Instance groups](https://docs.cloud.google.com/compute/docs/instance-groups)
  * [Zonal network endpoint groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts)
  * [Serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts): One or more [App Engine](https://docs.cloud.google.com/appengine/docs), [Cloud Run](https://docs.cloud.google.com/run/docs), or [Cloud Run functions](https://docs.cloud.google.com/functions/docs) services
  * [Internet NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts) for external backends
  * Buckets in [Cloud Storage](https://docs.cloud.google.com/storage/docs)



External backends can be hosted within an on-premises infrastructure or origins provided by third-party providers. The following sections discuss external backends in more detail.

## Hybrid and multi-cloud architectures

As you move your services to Google Cloud, you might need to do so in phases. Sometimes certain content can't immediately be moved to a cloud environment and might need to stay on-premises. In other cases, the content might be hosted in another cloud. Cloud CDN support for external backends lets you use Google's [globally distributed edge caching infrastructure](https://docs.cloud.google.com/cdn/docs/locations) for such content.

[ ![Hybrid and multi-cloud architecture](https://docs.cloud.google.com/static/load-balancing/images/cdn-hybrid-multicloud.svg)](https://docs.cloud.google.com/static/load-balancing/images/cdn-hybrid-multicloud.svg) Hybrid and multi-cloud architecture

In the diagram, `images` content resides in Google Cloud, while `video` resides in a Tokyo data center, which could be on-premises or in another cloud. With external backends, origins in the Tokyo data center can be the backend source of the `video` content with Cloud CDN and the external Application Load Balancer delivering the content to users.

Using [URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts), this deployment can direct origin pull requests for video traffic to the external backend in Tokyo. This mapping is determined based on request URL: `/video`.

For images (determined based on request URL: `/images`), content is sourced from Google Cloud and is delivered by the Cloud CDN edge infrastructure.

**Note:** Cloud CDN supports fetching content from a single external backend for a service. It does not provide load balancing among multiple external backends for a service, nor does it load balance between an external backend and a Google Cloud backend.

## Specifying an external backend

Similar to configuring Cloud CDN with your endpoints deployed in Google Cloud, you can use the [network endpoint groups (NEGs) API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups) to add your server as the external backend for Cloud CDN.

To specify the external backend, use an internet NEG. An internet NEG has one of the endpoint types shown in the following table.

Endpoint address | Type | Definition | When to use  
---|---|---|---  
Hostname and an optional port | `INTERNET_FQDN_PORT` | A publicly resolvable fully qualified domain name (FQDN), and an optional port, for example `backend.example.com:443` (default ports: `80` for HTTP and `443` for HTTPS) | Use this endpoint when your external backend can be resolved by using an FQDN with public DNS.  
IP address and an optional port | `INTERNET_IP_PORT` | A publicly accessible IP address and an optional port, for example `192.0.2.8` or `192.0.2.8:443` (default ports: `80` for HTTP and `443` for HTTPS) | Use this endpoint to specify a publicly accessible IP address and a port to connect to.  
  
The best practice is to create the internet NEG with the `INTERNET_FQDN_PORT` endpoint type and an FQDN value as an origin hostname value. This insulates the Cloud CDN configuration from IP address changes in the origin infrastructure. Network endpoints that are defined by using FQDNs are resolved through public DNS. Make sure that the configured FQDN is resolvable through [Google Public DNS](https://developers.google.com/speed/public-dns/).

After you create the internet NEG, the type cannot be changed between `INTERNET_FQDN_PORT` and `INTERNET_IP_PORT`. You need to create a new internet NEG and change your backend service to use the new internet NEG.

When using an external backend that expects a particular value for the HTTP request's `Host` header, you must configure the backend service to set the `Host` header to that expected value. If you don't configure a user-defined request header, a backend service preserves the `Host` header that the client used to connect to the Google Cloud external Application Load Balancer. For general information about custom headers, see [Create custom headers in backend services](https://docs.cloud.google.com/load-balancing/docs/custom-headers). For a specific example, see [Setting up Cloud CDN with an external backend](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-ex-backend-internet-neg).

## Using external backends and Google Cloud-based origins

The following figure shows an internet NEG used to deploy an external backend with an external Application Load Balancer and Cloud CDN.

[ ![Cloud CDN with external backends](https://docs.cloud.google.com/static/load-balancing/images/cdn-custom-origins-negs.svg)](https://docs.cloud.google.com/static/load-balancing/images/cdn-custom-origins-negs.svg) Cloud CDN with external backends

## What's next

  * To set up an external backend, see [Set up an external backend with an internet NEG](https://docs.cloud.google.com/cdn/docs/set-up-external-backend-internet-neg).
  * To learn about what content is cached, see [Caching overview](https://docs.cloud.google.com/cdn/docs/caching).
  * To resolve issues, see [Troubleshooting external backend and internet NEG issues](https://docs.cloud.google.com/load-balancing/docs/https/troubleshooting-ext-https-lbs#external-backends-internet-neg).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
