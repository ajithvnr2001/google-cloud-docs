---
url: https://docs.cloud.google.com/tasks/docs/use-vpc-service-controls/
title: Set up a service perimeter using VPC Service Controls \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:45.820479+00:00
---

# Set up a service perimeter using VPC Service Controls  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/use-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Set up a service perimeter using VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

VPC Service Controls is a Google Cloud feature that lets you set up a service perimeter and create a data transfer boundary. You can use VPC Service Controls with Cloud Tasks to help protect your services.

## Supported targets

Once you set up a service perimeter, HTTP requests from a Cloud Tasks execution are allowed for:

  * Authenticated requests to VPC Service Controls-compliant Cloud Run functions targets at `functions.net` endpoints
  * Authenticated requests to VPC Service Controls-compliant Cloud Run targets at `run.app` endpoints



## Examples of unsupported targets

Once you set up a service perimeter, non-compliant HTTP requests from a Cloud Tasks execution are blocked and fail with a `TARGET_TYPE_NOT_PERMITTED_FOR_VPC` error code. For example, requests to all of the following are blocked:

  * Non-VPC Service Controls-compliant Cloud Run functions targets at `functions.net` endpoints
  * Non-VPC Service Controls-compliant Cloud Run targets at `run.app` endpoints
  * Cloud Run functions targets at non-`functions.net` endpoints
  * Cloud Run targets at non-`run.app` endpoints
  * Non-Cloud Run functions endpoints
  * Non-Cloud Run endpoints



## What's next

  * To set up a service perimeter, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

  * To adjust the ingress settings of your Cloud Run function, see [Configuring network settings](https://docs.cloud.google.com/functions/docs/networking/network-settings).

  * To adjust the ingress settings of your Cloud Run service, see [Restricting ingress for Cloud Run](https://docs.cloud.google.com/run/docs/securing/ingress).

  * To learn more about VPC Service Controls, see the [overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview) and [supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
