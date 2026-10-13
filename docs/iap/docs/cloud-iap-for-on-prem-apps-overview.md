---
url: https://docs.cloud.google.com/iap/docs/cloud-iap-for-on-prem-apps-overview/
title: Overview of IAP for on-premises apps \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:06.348083+00:00
---

# Overview of IAP for on-premises apps  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/cloud-iap-for-on-prem-apps-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Overview of IAP for on-premises apps Stay organized with collections  Save and categorize content based on your preferences. 

[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) allows you to manage access to HTTP-based apps outside of Google Cloud. This includes apps on-premises in your enterprise's data centers.

To learn how to secure on-premises apps with IAP, see [Setting up IAP for on-premises apps](https://docs.cloud.google.com/iap/docs/enabling-on-prem-howto).

## Introduction

IAP targets on-premises apps with the [IAP On-Prem Connector](https://cloud.google.com/iap/docs/enabling-on-prem-howto). The On-Prem Connector uses a [Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs) template to create the resources needed to host and deploy the IAP On-Prem Connector into an IAP-enabled Google Cloud project, forwarding authenticated and authorized requests to on-premises apps.

The On-Prem Connector creates the following resources:

  * A [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) deployment that acts as a proxy for the on-premises app. 
  * An [external Application Load Balancer](https://cloud.google.com/load-balancing/docs/https/) that acts as the ingress controller for requests.
  * Routing rules.



A deployment can have multiple Cloud Service Mesh backend services that run behind one external Application Load Balancer. Each backend service maps to an individual on-premises app.

When the IAP on-prem connector is deployed and IAP is enabled for the newly created on-prem connector backend service, IAP secures your app with identity and [context based](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto) Identity and Access Management (IAM) access policies. Because an IAM access policy is configured on the backend service resource level, you're able to have different access control lists for each of your on-premises apps. This means only one Google Cloud project is needed to manage access to multiple on-premises apps.

## How IAP for on-premises apps works

When a request is sent to an app hosted on Google Cloud, IAP authenticates and authorizes the user requests. It then grants the user access to the Google Cloud app.

When a request is sent to an on-premises app, IAP authenticates and authorizes the user request. It then routes the request to the IAP on-prem connector. The IAP on-prem connector forwards the request through a [Hybrid Connectivity Network Endpoint Group](https://cloud.google.com/load-balancing/docs/negs#hybrid-neg) from Google Cloud to the on-premises network.

The following diagram shows the high-level traffic flow of a web request for a Google Cloud app (**app1**) and an on-premises app (**app2**).

![](https://docs.cloud.google.com/iap/images/iap-connector-flow.png)

## Routing rules

When configuring a IAP connector deployment, you configure the routing rules. These rules route authenticated and authorized web requests coming to your DNS hostname ingress point to the DNS hostname that's the destination.

The following is an example of `routing` parameters defined for a IAP connector Deployment Manager template.
    
    
       routing:
         - name: hr
           mapping:
            - name: host
              source: www.hr-domain.com
              destination: hr-internal.domain.com
            - name: sub
              source: sheets.hr-domain.com
              destination: sheets.hr-internal.domain.com
         - name: finance
           mapping:
            - name: host
              source: www.finance-domain.com
              destination: finance-internal.domain.com

  * Each `routing` name corresponds to a new, Ambassador-created Compute Engine backend service resource.
  * The `mapping` parameter specifies a list of Ambassador routing rules for a backend service.
  * The `source` of a routing rule is mapped to a `destination`, where `source` is the URL of requests coming to Google Cloud, and `destination` is the URL for your on-premises app that IAP routes traffic to after a user has been authorized and authenticated.



The following table demonstrates example rules to route incoming requests from `www.hr-domain.com` to `hr-internal.domain.com`:

Compute Engine backend service | Routing rule name | Source | Destination  
---|---|---|---  
hr | hr-host | www.hr-domain.com | hr-internal.domain.com  
hr-sub | sheets.hr-domain.com | sheets.hr-internal.domain.com  
finance | finance-host | www.finance-domain.com | finance-internal.domain.com  
  
## What's next

  * Learn how to [secure on-premises apps with IAP](https://docs.cloud.google.com/iap/docs/enabling-on-prem-howto).
  * Learn more about [how IAP works](https://docs.cloud.google.com/iap/docs/concepts-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
