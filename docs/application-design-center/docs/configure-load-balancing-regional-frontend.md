---
url: https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-frontend/
title: Configure a regional Cloud Load Balancing frontend \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:58.329861+00:00
---

# Configure a regional Cloud Load Balancing frontend  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-frontend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a regional Cloud Load Balancing frontend Stay organized with collections  Save and categorize content based on your preferences. 

You create a load balancer in your application by configuring and connecting distinct Cloud Load Balancing frontend and backend components. The separate components help you apply distinct controls for external and internal traffic, and prevent direct access to data.

The regional Cloud Load Balancing frontend component helps you configure the public-facing elements of a load balancer. The frontend handles incoming traffic, defines routing rules, and directs requests to the appropriate backend. You can configure the following:

  * Target Proxy: Terminates client connections and forwards requests.
  * URL Map: Defines routing rules based on hostnames and URL paths.
  * Forwarding Rule: Assigns an IP address and port to the load balancer, making it accessible.



For more information, see [Cloud Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).

This document describes the connections and parameters you can configure when using App Design Center to create a regional Cloud Load Balancing frontend. The configuration parameters are based on the [terraform-google-regional-lb-http](https://github.com/GoogleCloudPlatform/terraform-google-regional-lb-http/tree/main/modules/frontend) Terraform module.

## Component connections

To create a complete Cloud Load Balancing component, you must connect your regional Cloud Load Balancing frontend to at least one regional Cloud Load Balancing backend. Connected Cloud Load Balancing components are displayed as a group in the design canvas.

The following table includes the components that you can connect to a regional Cloud Load Balancing frontend, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instances can redirect traffic to the regional Cloud Load Balancing frontend.
  * The Cloud Load Balancing address is added to the Compute Engine instance template.

| [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The HTTP and HTTPS IP addresses of the load balancer are available to the application running in the Cloud Run container.
  * The Cloud Load Balancing address metadata is added to the Cloud Run environment variables.

| [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
[Regional Cloud Load Balancing backend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-backend) (required) | 

  * The Cloud Load Balancing frontend, which handles incoming requests, is linked to the Cloud Load Balancing backend, which processes the requests.
  * The backend service information is added to the frontend URL map input.
  * Incoming traffic is served based on the host path mappings you configure in the regional Cloud Load Balancing backend URL maps.

| [URL maps overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts)  
  
## Required configuration parameters

If your template includes a regional Cloud Load Balancing frontend component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the Cloud Load Balancing frontend. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Region** | [region](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.region) | [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
**Name** | [name](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.name) | [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
**Network** | [network](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.network) | [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Subnetwork** | [subnetwork](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.subnetwork) | [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
| **Create Proxy Only Subnet** | [create_proxy_only_subnet](https://github.com/terraform-google-modules/terraform-google-lb/tree/main/modules/regional_proxy_lb#inputs) | [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)  
| **Proxy Only Subnet IP** | [ipCidrRange](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks) | [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)  
| **Load Balancing Scheme** | [loadBalancingScheme](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.load_balancing_scheme) | [Summary of types of Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#summary-gclb)  
| **Create URL Map** | Automatically create a URL map. Clear the checkbox if you want to configure your own URL map in **URL Map Input**. | [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map)  
URL Map Input | **Host** | [Configure URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) | [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map)  
**Path** | [Configure URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) | [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map)  
**Backend Service** | [Configure URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) | [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map)  
| **URL Map Resource URI** | The URI for a URL map that you previously created. | [urlMap](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies)  
| **Create Address** | Create a global IPv4 address. | [IP Address specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications)  
| **Address** | [IPAddress](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.ip_address) | [IP Address specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications)  
| **Enable IPv6** | Enable IPv6 address on the CDN load balancer. | [IPv6 for Application Load Balancers and proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/ipv6)  
| **Create IPv6 Address** | Allocate an IPv6 address. | [IPv6 for Application Load Balancers and proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/ipv6)  
| **IPv6 Address** | [IPAddress](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.ip_address) | [IP Address specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications)  
Labels | **Key** | [labels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.labels) | [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources)  
**Value** | [labels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.labels) | [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources)  
| **SSL** | Enable SSL support and then do one of the following:

  * Enable **Create SSL Certificate** and enter **Private Key** and **Certificate**.
  * Enter **SSL Certificates**.
  * Enter **Managed SSL Certificate Domains**.

| [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates)  
| **Create SSL Certificate** | Create a certificate using the information you enter in **Private Key** and **Certificate**. | [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates)  
| **Private Key** | [privateKey](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionSslCertificates#SslCertificate.FIELDS.private_key) | [Step 1: Create a private key and certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert)  
| **Certificate** | [certificate](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionSslCertificates#SslCertificate.FIELDS.certificate) | [Step 1: Create a private key and certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert)  
| **SSL Certificates** | [sslCertificates[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpsProxies#TargetHttpsProxy.FIELDS.ssl_certificate) | [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates)  
| **Managed SSL Certificate Domains** | [managed.domains[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionSslCertificates#SslCertificate.FIELDS.inlinedField) | [Use Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)  
| **Random Certificate Suffix** | Select to generate random certificate names. Enable this setting if you need to change the SSL certificate. | [random_certificate_suffix](https://github.com/terraform-google-modules/terraform-google-lb-http/blob/main/modules/serverless_negs/README.md#inputs)  
| **HTTP Port** | The port for the HTTP load balancer. | [Port specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications)  
| **HTTPS Port** | The port for the HTTPS load balancer. | [Port specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications)  
| **HTTPS Redirect** | Select to enable HTTPS redirect. | [Set up an HTTP-to-HTTPS redirect for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-http-https-redirect)  
| **HTTP Forward** | Clear to disable HTTP port 80 forwarding. | [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
| **SSL Policy** | [sslPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpsProxies#TargetHttpsProxy.FIELDS.ssl_policy) | [SSL policies for SSL and TLS protocols](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)  
| **Server TLS policy** | [serverTlsPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpsProxies#TargetHttpsProxy.FIELDS.server_tls_policy) | [Mutual TLS overview](https://docs.cloud.google.com/load-balancing/docs/mtls)  
| **HTTP Keep Alive Timeout Sec** | [httpKeepAliveTimeoutSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpsProxies#TargetHttpsProxy.FIELDS.http_keep_alive_timeout_sec) | [Timeouts and retries](https://docs.cloud.google.com/load-balancing/docs/https#timeouts_and_retries)  
  
## What's next

You must connect your frontend component to a backend component. To configure the backend component, see [Configure a regional Cloud Load Balancing backend service in Application Design Center](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-backend).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
