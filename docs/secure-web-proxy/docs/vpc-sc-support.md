---
url: https://docs.cloud.google.com/secure-web-proxy/docs/vpc-sc-support/
title: Configure VPC Service Controls for Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:07.022475+00:00
---

# Configure VPC Service Controls for Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/vpc-sc-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Configure VPC Service Controls for Secure Web Proxy Stay organized with collections  Save and categorize content based on your preferences. 

You can use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to improve the security of your Secure Web Proxy instance.

VPC Service Controls provides additional security for Secure Web Proxy to help mitigate the risk of data exfiltration. By using VPC Service Controls, you can add projects to service perimeters that protect resources and services from requests that originate outside the perimeter.

To learn how to create a service perimeter, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) in the VPC Service Controls documentation.

You can include the following APIs in your service perimeter:

API name | API identifier | Requirement  
---|---|---  
[Network Services API](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-services/rest) | `networkservices.googleapis.com` | `Required`  
[Network Security API](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest) | `networksecurity.googleapis.com` | `Required`  
[Certificate Manager API](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest) | `certificatemanager.googleapis.com` | `Optional` If you provision your proxy with a [certificate](https://docs.cloud.google.com/certificate-manager/docs/certificates), then you must also include this API in your service perimeter.  
[Certificate Authority Service API](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest) | `privateca.googleapis.com` | `Optional` If you [enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection) for your proxy, then you must also include this API in your service perimeter.  
[Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) | `compute.googleapis.com` | `Optional` If your Secure Web Proxy configuration interacts with Compute Engine resources across your service perimeter, then you must include this API.  
  
## What's next

  * [Learn how to enable Secure Web Proxy with VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_swp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
