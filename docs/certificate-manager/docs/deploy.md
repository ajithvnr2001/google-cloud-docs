---
url: https://docs.cloud.google.com/certificate-manager/docs/deploy/
title: Deployment overview \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:00:05.451580+00:00
---

# Deployment overview  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Deployment overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of how to use Certificate Manager to provision Google-managed and self-managed certificates for Application Load Balancers and proxy Network Load Balancers.

Before reading this page, ensure that you're familiar with the [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) in the Cloud Load Balancing documentation.

## Certificate Manager configuration methods

Certificate Manager offers two certificate configuration methods for Application Load Balancers using target HTTPS proxies and proxy Network Load Balancers using target SSL proxies. These are two of three possible certificate configuration methods for Cloud Load Balancing. For more information about Certificate Manager and Cloud Load Balancing, see [Certificate configuration methods](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#config-tech) in the load balancing documentation.

  * **Load balancer's target proxy references a Certificate Manager certificate map** : the load balancer's target proxy references a single [certificate map](https://docs.cloud.google.com/certificate-manager/docs/maps). The certificate map supports thousands of entries by default, and can scale to millions of entries. This method is used by external Application Load Balancers and external proxy Network Load Balancers that are powered by Google Front Ends (GFEs):

    * Global external Application Load Balancers
    * Classic Application Load Balancers
    * Global external proxy Network Load Balancers
    * Classic proxy Network Load Balancers
  * **Load balancer's target proxy references Certificate Manager certificates directly** : the load balancer's target proxy can reference up to 100 [Certificate Manager certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates). This method is used by the following Application Load Balancers that are powered by managed [open-source Envoy proxy](https://www.envoyproxy.io/) software:

    * Regional external Application Load Balancers
    * Regional internal Application Load Balancers
    * Cross-region internal Application Load Balancers



Certificate Manager also supports the following products, which reference Certificate Manager certificates as part of their configuration:

  * **Secure Web Proxy gateway references Certificate Manager certificates** : before you can configure a Secure Web Proxy gateway, you create one or more Certificate Manager certificates for the gateway to use. For more information, see [Deploy an SSL certificate](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#create-upload-ssl-certificate) and [Deploy a Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart).

  * **Media CDN edge cache service references Certificate Manager certificates** : a Media CDN edge cache service supports up to five Certificate Manager certificates. For more information, see [SSL (TLS) Certificates](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates) and [Configure SSL (TLS) certificates](https://docs.cloud.google.com/media-cdn/docs/configure-ssl-certificates).




## Certificate types

Certificate Manager supports both Google-managed and self-managed certificates. All Application Load Balancers using target HTTPS proxies and all proxy Network Load Balancers that support target SSL proxies can use either Google-managed or self-managed Certificate Manager certificates.

  * **Google-managed Certificate Manager certificates** : certificates that Google Cloud obtains and manages for you. Depending on the load balancer and its Certificate Manager configuration method, Google-managed Certificate Manager certificates can be provisioned by using load balancer authorization, DNS authorization, or by using Certificate Authority Service (CA Service).

  * **Self-managed Certificate Manager certificates** : certificates that you obtain, provision, and renew yourself.


**Note:** If you use Google Kubernetes Engine (GKE), GKE Gateway supports certificates managed by Certificate Manager. For more information, see [Secure a Gateway using Certificate Manager](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-certificate-manager). However, GKE Ingress does _not_ support certificates managed by Certificate Manager. To use Google-managed certificates with Ingress, you must use the `ManagedCertificate` resource. For more information, see [Secure traffic for GKE Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-traffic-management).

## Product support

The following table summarizes the support for Google-managed and self-managed Certificate Manager certificates by product.

Product | Google-managed certificates | Self-managed certificates  
---|---|---  
Load balancer authorization | DNS authorization | Certificate Authority Service (CA Service)  
Global external Application Load Balancers and proxy Network Load Balancers 

  * Global external Application Load Balancer
  * Classic Application Load Balancer
  * Global external proxy Network Load Balancer
  * Classic proxy Network Load Balancer

|   
[ Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-lb-auth) |   
[ Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth) |   
[Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas) |   
[Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed)  
Regional external and internal Application Load Balancers: 

  * Regional external Application Load Balancer
  * Regional internal Application Load Balancer

|  |   
[ Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-regional) |   
[ Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas-regional) |   
[Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional)  
Cross-region internal Application Load Balancers |  |   
[ Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth-cross-reg) |   
[ Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas-cross-reg) |   
[Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-cross-reg)  
[ Secure Web Proxy gateways](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#create-upload-ssl-certificate) |  |   
[ Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-regional) |   
[ Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas-regional) |   
[Deployment guide](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional)  
[ Media CDN edge cache services](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates) |  |  |  |   
  
## What's next

  * If you want to migrate an existing certificate from your load balancer to Certificate Manager, follow the instructions in [Migrate a certificate to Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/migrate).
  * For more information about Certificate Manager and GFE-based load balancers, see [How Certificate Manager works](https://docs.cloud.google.com/certificate-manager/docs/how-it-works).
  * If you want to use mutual TLS authentication (mTLS), see [Mutual TLS authentication](https://docs.cloud.google.com/load-balancing/docs/mtls) in the Cloud Load Balancing documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
