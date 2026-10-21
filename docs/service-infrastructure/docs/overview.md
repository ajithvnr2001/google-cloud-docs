---
url: https://docs.cloud.google.com/service-infrastructure/docs/overview/
title: Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:39.135950+00:00
---

# Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Service Infrastructure Stay organized with collections  Save and categorize content based on your preferences. 

Service Infrastructure is a foundational platform for creating, managing, securing, and consuming APIs and services across organizations. It is used by [Google APIs](https://github.com/googleapis/googleapis), [Cloud APIs](https://docs.cloud.google.com/apis), [Cloud Endpoints](https://docs.cloud.google.com/endpoints), and [API Gateway](https://docs.cloud.google.com/api-gateway). Service Infrastructure provides a wide range of features to service consumers and service producers, including authentication, authorization, auditing, rate limiting, analytics, billing, logging, and monitoring.

## Architecture

Service Infrastructure is designed to support millions of service producers and service consumers. In order to handle such scalability, Service Infrastructure uses a distributed microservice architecture. The system is divided into three _planes_ based on their functionality:

  * The Management Plane, which lets developers manage configurations of their services and their usage of services.
  * The Data Plane, which handles the data traffic between the clients and the services. The data plane can run in different environments and support both internal and external clients.
  * The Control Plane, which controls the data plane based on the configurations coming from the management plane, such as rate limiting.



![Architecture diagram for Service Infrastructure.](https://docs.cloud.google.com/static/service-infrastructure/docs/architecture.png)

Service Infrastructure provides multiple public APIs for these planes. A developer can use these APIs to integrate their service directly with Service Infrastructure, or use a framework built on top of these APIs, such as [Cloud Endpoints](https://docs.cloud.google.com/endpoints) and [API Gateway](https://docs.cloud.google.com/api-gateway).

## Creating APIs and services

To create a managed service using Service Infrastructure, you need to create a [service configuration](https://docs.cloud.google.com/service-infrastructure/docs/glossary#config) to define your service settings and behaviors, such as service name and API surface. You then deploy your service configuration to the Service Management API to create your service and register it with Google Cloud.

For more information, see Managing Services in the [How-to Guides](https://docs.cloud.google.com/service-infrastructure/docs/how-to).

## Running APIs and services

To run a managed service using Service Infrastructure, your service needs to call the Service Control API for admission control on each request, and telemetry reporting on each response, such as validating API keys and reporting API metrics. It allows your service to leverage the rich set of features provided by Google Cloud.

If your service has some internal components, such as billing pipelines, they can also use the Service Control API for admission control and telemetry reporting. For example, reporting billing metrics to [Cloud Billing](https://cloud.google.com/billing/docs).

For more information, see Integrating with Service Infrastructure in the [How-to Guides](https://docs.cloud.google.com/service-infrastructure/docs/how-to).

## Managing APIs and services

If you are a service producer, you can use the Service Consumer Management API and the Service Networking API to manage consumers of your service, including creating tenant projects for your consumers, setting up network peering between tenant projects and consumer projects, and managing the quota limits of your consumers.

For more information, see Managing Service Consumers in the [How-to Guides](https://docs.cloud.google.com/service-infrastructure/docs/how-to).

## Consuming APIs and services

If you are a service consumer, you can use the Service Usage to list, enable, and disable APIs and services in your Google Cloud projects, and apply quota restrictions to services used by your Google Cloud projects or within your organization. You can manage both Google-provided services and services created using [Cloud Endpoints](https://cloud.google.com/endpoints).

For more information, see the [Service Usage](https://docs.cloud.google.com/service-usage/docs) documentation.

## Getting started

The recommended way for most use cases to use Service Infrastructure is to use [Cloud Endpoints](https://docs.cloud.google.com/endpoints) to create and manage your services. To get started, see [Cloud Endpoints Quickstart](https://docs.cloud.google.com/endpoints/docs/deploy-api).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
