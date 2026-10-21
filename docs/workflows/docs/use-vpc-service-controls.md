---
url: https://docs.cloud.google.com/workflows/docs/use-vpc-service-controls/
title: Set up a service perimeter using VPC Service Controls \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:36.313301+00:00
---

# Set up a service perimeter using VPC Service Controls  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/use-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Set up a service perimeter using VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

VPC Service Controls is a Google Cloud feature that allows you to set up a service perimeter and create a data transfer boundary. You can use VPC Service Controls with Workflows to help protect your services.

HTTP requests from a Workflows execution are supported as follows:

  * [Authenticated requests](https://docs.cloud.google.com/workflows/docs/authenticate-from-workflow#authenticate-apis) to VPC Service Controls-compliant Google Cloud endpoints are allowed.
  * Requests to Cloud Run functions and Cloud Run service endpoints are allowed.
  * Requests to third-party endpoints are blocked.
  * Requests to non-VPC Service Controls-compliant Google Cloud endpoints are blocked.



## What's next

  * To learn more about VPC Service Controls, see the [overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview) and [supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).

  * For the recommended process to configure and enforce VPC Service Controls protection in your Google Cloud organization, see [Best practices for enabling VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/enable).

  * For best practices for designing service perimeters, see [Design and architect service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/architect-perimeters).

  * To set up a service perimeter, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

  * To invoke a private endpoint, see [Invoke a private endpoint using Service Directory's service registry](https://docs.cloud.google.com/workflows/docs/invoke-private-endpoint-vpc).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
