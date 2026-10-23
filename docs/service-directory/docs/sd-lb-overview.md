---
url: https://docs.cloud.google.com/service-directory/docs/sd-lb-overview/
title: Service Directory and load balancers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:32.598401+00:00
---

# Service Directory and load balancers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/sd-lb-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Service Directory and load balancers Stay organized with collections  Save and categorize content based on your preferences. 

You can choose to automatically register your load balancer service with Service Directory when you create a load balancer. This enables client applications to use Service Directory through HTTP, gRPC, or DNS to resolve the address of the load balancer service and connect to it directly.

Registering your load balancer with Service Directory lets you do the following:

  * Choose custom DNS names to serve the network locations of your internal load balancers as opposed to DNS accessing your internal load balancer only through an internally generated DNS name in the `.internal` domain.
  * Serve multiple load balancers from the same DNS domain name, which is otherwise not possible with the auto-generated DNS records. This is useful for internal load balancers in a private DNS zone.
  * Register load balancers directly and automatically in Service Directory providing a single repository for all your services in Google Cloud.
  * See standalone services, endpoints, and your load balancer endpoints with a single command in the Service Directory API.
  * Apply administrative actions like access control at the namespace or service level to encompass both your load balancer endpoints and other backend services.



For instructions about how to register an internal load balancer in Service Directory, see [Configure an internal load balancer in Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-ilb-in-sd).

For instructions about how to register a network load balancer in Service Directory, see [Configure a regional external passthrough Network Load Balancer in Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-netlb-in-sd).

## What's next

  * To get an overview of Service Directory, see the [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To find solutions for common issues that you might encounter when using Service Directory, see [Troubleshooting](https://docs.cloud.google.com/service-directory/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
