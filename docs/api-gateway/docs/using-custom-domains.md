---
url: https://docs.cloud.google.com/api-gateway/docs/using-custom-domains/
title: Use a custom domain with API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:34.259467+00:00
---

# Use a custom domain with API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/using-custom-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Use a custom domain with API Gateway

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A custom domain for your gateway can be implemented by configuring [HTTP(S) Load Balancing for API GatewayPREVIEW](https://docs.cloud.google.com/api-gateway/docs/gateway-load-balancing). Once the HTTP(S) load balancer for your gateway is set up, follow these steps to update your custom domain's DNS records to point to the new load balancer service.

**Important:** Gateways with an `effectiveStreamingMode` of `EFFECTIVE_STREAMING_MODE_ENABLED` are incompatible with HTTP(S) Load Balancing for API Gateway and Serverless NEGs during Public Preview. Consequently, you cannot use custom domains with these gateways using this method.

These steps are also required when using an HTTP(S) load balancer with a Google-managed certificate (which requires a domain). Allocating and using [a static IP address](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create) is recommended when used with DNS. The specific instructions for this step depend on your DNS provider.

For more information on setting up an HTTP(S) Load Balancer for API Gateway, see [Get started with HTTP(S) Load Balancing for API GatewayPREVIEW](https://docs.cloud.google.com/api-gateway/docs/gateway-serverless-neg)

To configure your custom domain with the backend:

  1. To send traffic to the load balancer, the DNS record of your custom domain (for example, `my-app-domain`) must point to the IP address(es) of the load balancer.

To find the IP address of your global forwarding rule, use this command:
         
         gcloud compute forwarding-rules list

  2. Update your domain's DNS A or AAAA record to point to the load balancer's IP address so that traffic sent to the existing custom domain URL is routed through the load balancer instead. It may take as little as several seconds or as long as several hours for DNS to propagate this change to the DNS server.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
