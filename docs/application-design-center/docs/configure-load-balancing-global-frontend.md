---
url: https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-frontend/
title: Configure a global Cloud Load Balancing frontend \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:20.566705+00:00
---

# Configure a global Cloud Load Balancing frontend  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-frontend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a global Cloud Load Balancing frontend Stay organized with collections  Save and categorize content based on your preferences. 

You create a load balancer in your application by configuring and connecting distinct [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) frontend and backend components, which help you apply separate controls for external and internal traffic and prevent direct access to data. In App Design Center, the global Cloud Load Balancing frontend component handles incoming traffic, defines routing rules, and directs requests through a target proxy, URL map, forwarding rule, and SSL certificate, with connections and configuration parameters based on the [terraform-google-lb-http](https://github.com/terraform-google-modules/terraform-google-lb-http/tree/main/modules/frontend) Terraform module.

## Component connections

To create a complete Cloud Load Balancing component, you must connect your global Cloud Load Balancing frontend to at least one global Cloud Load Balancing backend. Connected Cloud Load Balancing components are displayed as a group in the design canvas.

The following table lists the components that you can connect to a global Cloud Load Balancing frontend, and the resulting updates to your application and Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Global Cloud Load Balancing backend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-backend) (required) | 

  * The Cloud Load Balancing frontend, which handles incoming requests, is linked to the Cloud Load Balancing backend, which processes the requests.
  * The backend service information is added to the frontend URL map input.
  * Incoming traffic is served based on the host path mappings you configure in the global Cloud Load Balancing backend URL maps.

| [URL maps overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts)  
  
## Required configuration parameters

If your template includes a global Cloud Load Balancing frontend component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Name** | [name](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.name) | [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
**Project ID** | The project where you want to deploy the Cloud Load Balancing frontend. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Create Address** | Create a new global IPv4 address. | [IP Address specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications)  
| **Address** | [IPAddress](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.ip_address) | [IP Address specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications)  
| **Enable IPv6** | [ipVersion](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.ip_version) | [IPv6 for Application Load Balancers and proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/ipv6)  
| **Create IPv6 Address** | Create a new global IPv6 address. | [IP Address specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications)  
| **IPv6 Address** | [IPAddress](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.ip_address) | [IP Address specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications)  
| **Create URL Map** | Automatically create a URL map. Clear the checkbox if you want to configure your own URL map in **URL Map Input** | [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map)  
URL Map Input | **Host** | [Configure URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) | [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map)  
**Path** | [Configure URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) | [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map)  
**Backend Service** | [Configure URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) | [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map)  
| **URL Map Resource URI** | The URI for a URL map that you previously created. | [urlMap](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies)  
| **HTTP Forward** | Clear to disable HTTP port 80 forwarding. | [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
| **SSL** | Enable SSL support and then do one of the following:

  * Enable **Create SSL Certificate** and enter **Private Key** and **Certificate**.
  * Enter **SSL Certificates**.
  * Enter **Managed SSL Certificate Domains**.

| [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates)  
| **Create SSL Certificate** | Create a certificate using the information you enter in **Private Key** and **Certificate**. | [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates)  
| **SSL Certificates** | [sslCertificates[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies#TargetHttpsProxy.FIELDS.ssl_certificate) | [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates)  
| **Private Key** | [privateKey](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslCertificates#SslCertificate.FIELDS.private_key) | [Step 1: Create a private key and certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert)  
| **Certificate** | [certificate](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslCertificates#SslCertificate.FIELDS.certificate) | [Step 1: Create a private key and certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert)  
| **Managed SSL Certificate Domains** | [managed.domains[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslCertificates#SslCertificate.FIELDS.inlinedField) | [Use Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)  
| **Certificate Map** | [certificateMap](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies#TargetHttpsProxy.FIELDS.certificate_map) | [Certificate configuration methods](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#config-tech)  
| **SSL Policy** | [sslPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies#TargetHttpsProxy.FIELDS.ssl_policy) | [SSL policies for SSL and TLS protocols](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)  
| **QUIC** | [quicOverride](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies#TargetHttpsProxy.FIELDS.quic_override) | [Configure HTTP/3](https://docs.cloud.google.com/load-balancing/docs/https#configuring-http3)  
| **HTTPS Redirect** | Select this option to enable HTTPS redirect. | [Set up an HTTP-to-HTTPS redirect for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-http-https-redirect)  
| **Random Certificate Suffix** | Select this option to generate random certificate names. Enable this setting if you need to change the SSL certificate. | [random_certificate_suffix](https://github.com/terraform-google-modules/terraform-google-lb-http/tree/main/modules/frontend#inputs)  
Labels | **Key** | [labels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.labels) | [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources)  
**Value** | [labels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.labels) | [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources)  
| **Load Balancing Scheme** | [loadBalancingScheme](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.load_balancing_scheme) | [Summary of types of Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#summary-gclb)  
| **Network** | [network](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules#ForwardingRule.FIELDS.network) | [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)  
| **Server TLS policy** | [serverTlsPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies#TargetHttpsProxy.FIELDS.authentication) | [Mutual TLS overview](https://docs.cloud.google.com/load-balancing/docs/mtls)  
| **HTTP Port** | The port for the HTTP load balancer. | [Port specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications)  
| **HTTPS Port** | The port for the HTTPS load balancer. | [Port specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications)  
| **HTTP Keep Alive Timeout Sec** | [httpKeepAliveTimeoutSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies#TargetHttpsProxy.FIELDS.http_keep_alive_timeout_sec) | [Timeouts and retries](https://docs.cloud.google.com/load-balancing/docs/https#timeouts_and_retries)  
  
## What's next

Connect your frontend component to a backend component. To configure the backend component, see [Configure a global Cloud Load Balancing backend service in Application Design Center](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-backend).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
