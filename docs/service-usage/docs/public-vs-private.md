---
url: https://docs.cloud.google.com/service-usage/docs/public-vs-private/
title: Public and private services \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:09.397940+00:00
---

# Public and private services  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/public-vs-private/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ Guides ](https://docs.cloud.google.com/service-usage/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Public and private services

Service Usage lets you discover, enable, and manage both globally available Google Cloud APIs and restricted custom APIs in your Google Cloud project. While public services are visible to every consumer, private services built with Cloud Endpoints require explicit access grants before you can list or call them.

## Public APIs and services

Public APIs and services are globally visible across all Google Cloud projects. Examples of public Google Cloud APIs and services include:

  * [BigQuery](https://docs.cloud.google.com/bigquery)
  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring)



You need the appropriate permissions to list or use public APIs and services in a Google Cloud project. For example, to enable a service, you need the `serviceusage.services.enable` [Identity and Access Management](https://docs.cloud.google.com/iam) permission. To learn about the required IAM permissions for Service Usage, see [Access control with IAM](https://docs.cloud.google.com/service-usage/docs/access-control).

## Private APIs and services

Private services are typically APIs implemented using [Cloud Endpoints](https://docs.cloud.google.com/endpoints) running in another Google Cloud project. To discover or use private APIs and services, you must first be granted access by a principal with the necessary permissions. To learn how to grant access to enable Cloud Endpoints APIs from a Google Cloud project, see the following pages for each of the respective Cloud Endpoints API frameworks:

  * [Controlling who can enable your API](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-callers) for the OpenAPI Specification.
  * [Controlling who can enable your API](https://docs.cloud.google.com/endpoints/docs/frameworks/control-api-callers) for Endpoints Frameworks.
  * [Controlling who can enable your API](https://docs.cloud.google.com/endpoints/docs/grpc/control-api-callers) for gRPC.



You must also have the appropriate IAM permissions to list or use private APIs and services. For example, to call the [`services.enable`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/enable) method for a private service, the `servicemanagement.services.bind` permission is required. To learn about the necessary permissions for Service Usage, see [Access control with IAM](https://docs.cloud.google.com/service-usage/docs/access-control).

When you list available or enabled APIs and services in a Google Cloud project, the results include any public and private APIs you have access to. To learn more about listing enabled and available services in your Google Cloud projects, see [List services](https://docs.cloud.google.com/service-usage/docs/list-services).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
