---
url: https://docs.cloud.google.com/load-balancing/docs/target-proxies/
title: Target proxies overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:39.031183+00:00
---

# Target proxies overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/target-proxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Target proxies overview Stay organized with collections  Save and categorize content based on your preferences. 

When you create an Application Load Balancer or a proxy Network Load Balancer, one of the resources that you configure is the target proxy. Target proxies terminate incoming connections from clients and create new connections from the load balancer to the backends.

At a high-level, traffic is handled according to the following process:

  1. A target proxy is referenced by one or more forwarding rules. The target proxy listens on the IP address and port specified by the load balancer's forwarding rule.

  2. A client makes a connection to the IP address and port of the load balancer's forwarding rule.

  3. The target proxy receives the client request. It then compares the request's destination IP address and port to the IP address and port configured in each forwarding rule that references the target proxy. If a match is found, the target proxy terminates the client's network connection.

Depending on the type of load balancer, target proxies terminate connections by using either [Google Front Ends (GFEs)](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service) or [Envoy proxies](https://www.envoyproxy.io/).

  4. The target proxy establishes a new connection to the appropriate backend VM instance or endpoint, as determined by the load balancer's URL map (applicable only to Application Load Balancers), TLS route ([Preview](https://cloud.google.com/products#product-launch-stages), applicable only to certain proxy Network Load Balancers), and backend service configuration.


**Note:** Target proxies are also used by [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/target-proxies). This page only discusses target proxies in the context of Cloud Load Balancing. 

## Target proxy types

Cloud Load Balancing uses different target proxies depending on the type of load balancer that you configure.

Load balancer | Target proxy type | Target proxy scope | Target proxy reference  
---|---|---|---  
Global external Application Load Balancer | Target HTTP proxy  
Target HTTPS proxy | Global | Target proxy references a URL map.  
Classic Application Load Balancer | Target HTTP proxy  
Target HTTPS proxy | Global | Target proxy references a URL map.  
Regional external Application Load Balancer * | Target HTTP proxy  
Target HTTPS proxy | Regional | Target proxy references a URL map.  
Cross-region internal Application Load Balancer * | Target HTTP proxy  
Target HTTPS proxy | Global | Target proxy references a URL map.  
Regional internal Application Load Balancer * | Target HTTP proxy  
Target HTTPS proxy | Regional | Target proxy references a URL map.  
Global external proxy Network Load Balancer | Target SSL proxy  
Target TCP proxy | Global | Target proxy references a single backend service.  
Classic proxy Network Load Balancer | Target SSL proxy  
Target TCP proxy | Global | Target proxy references a single backend service.  
Regional external proxy Network Load Balancer * | Target TCP proxy | Regional | Target proxy references either a single backend service or one or more TLS routes ([Preview](https://cloud.google.com/products#product-launch-stages)).  
Regional internal proxy Network Load Balancer * | Target TCP proxy | Regional | Target proxy references either a single backend service or one or more TLS routes ([Preview](https://cloud.google.com/products#product-launch-stages)).  
Cross-region internal proxy Network Load Balancer * | Target TCP proxy | Global | Target proxy references either a single backend service or one or more TLS routes ([Preview](https://cloud.google.com/products#product-launch-stages)).  
  
* This load balancer requires a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) in each region of a VPC network in which you use an Envoy-based load balancer. Connections to the backend originate from this proxy-only subnet.

Cloud Load Balancing supports the following resource combinations:

  * Forwarding rule > target HTTPS proxy > URL map > one or more backend services
  * Forwarding rule > target HTTP proxy > URL map > one or more backend services
  * Forwarding rule > target TCP proxy > one backend service
  * Forwarding rule > target TCP proxy > one or more TLS routes ([Preview](https://cloud.google.com/products#product-launch-stages)) > one or more backend services 
  * Forwarding rule > target SSL proxy > one backend service 



Health checks and backends are not shown in the preceding list.

## SSL certificates

Google Cloud proxy load balancers whose forwarding rules reference a target HTTPS proxy or target SSL proxy require a private key and SSL certificate as part of the load balancer's target proxy configuration. Depending on the type of load balancer you configure, you use either a Compute Engine SSL certificate resource or Certificate Manager.

To learn about which SSL certificate is supported for your configuration, see [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates).

## Optional features available

The following optional features can be configured on target proxies associated with certain types of load balancers. See the topics for more details.

  * [SSL policies](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)
  * [HTTP/3 support](https://docs.cloud.google.com/load-balancing/docs/https#QUIC)
  * [Client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/https/request-distribution#timeouts_and_retries)



## Use target proxies

If you're using the Google Cloud console to set up a load balancer, the target proxy is set up implicitly as part of your frontend configuration. If you're using the Google Cloud CLI or the API, you need to configure the target proxy explicitly.

You can't use the Google Cloud console to modify individual target proxies. However, you can update certain settings for target proxies by editing the frontend configuration of the load balancer they are associated with. Use either the gcloud CLI or the API to make any other changes.

To delete a target proxy, make sure that you first delete any forwarding rules that reference it.

### APIs

For descriptions of the properties and methods available to you when working with target proxies through the [REST API](https://docs.cloud.google.com/compute/docs/reference/rest/v1), see the following topics:

  * Target HTTPS proxy: [Global](https://docs.cloud.google.com/compute/docs/reference/v1/targetHttpsProxies) | [Regional](https://docs.cloud.google.com/compute/docs/reference/v1/regionTargetHttpsProxies)
  * Target HTTP proxy: [Global](https://docs.cloud.google.com/compute/docs/reference/v1/targetHttpProxies) | [Regional](https://docs.cloud.google.com/compute/docs/reference/v1/regionTargetHttpProxies)
  * Target TCP proxy: [Global](https://docs.cloud.google.com/compute/docs/reference/v1/targetTcpProxies) | [Regional](https://docs.cloud.google.com/compute/docs/reference/v1/regionTargetTcpProxies)
  * Target SSL proxy: [Global](https://docs.cloud.google.com/compute/docs/reference/v1/targetSslProxies)



### gcloud CLI

For the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute) reference documentation, see the following topics:

  * [`gcloud compute target-https-proxies`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies)
  * [`gcloud compute target-http-proxies`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies)
  * [`gcloud compute target-tcp-proxies`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies)
  * [`gcloud compute target-ssl-proxies`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies)



## What's next

  * To learn more about the proxy-only subnets used by Envoy-based load balancers, see [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).
  * To update the SSL certificate that your target proxy points to: 
    * **For self-managed SSL certificates:** [Replace or renew an SSL certificate before it expires](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#replacing-certificates)
    * **For Google-managed SSL certificates:** [Replace an existing SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#replace-ssl)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
