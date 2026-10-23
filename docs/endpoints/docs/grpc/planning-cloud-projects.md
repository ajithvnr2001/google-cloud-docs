---
url: https://docs.cloud.google.com/endpoints/docs/grpc/planning-cloud-projects/
title: Planning Your Cloud Projects \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:08.082724+00:00
---

# Planning Your Cloud Projects  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/planning-cloud-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Planning Your Cloud Projects Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/planning-cloud-projects "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This page provides recommendations for naming conventions of the Cloud projects that you may need to create in addition to the Cloud project for your production backend.

Depending on the purpose of the environment or the stage in the API lifecycle, you may want to:

  * Change the API name or the Cloud Endpoints service name. See [Configuring Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints#service_name) for more information.
  * Create a different project.
  * Change the path that the API is served from.



Following are some common patterns you may want to use:

  * **Versioning the API** : When you think you may need to make backwards-incompatible changes in the future, plan ahead and add the version number in the path where the API is served from. For example:

    * `my-api.endpoints.my‐project.cloud.goog/**v1** /echo`
  * **Development/test instances** : Each developer stands up their own version of the service, in their own project. For example, Dan the developer uses:

    * `my-api.endpoints.**dan-dev-project**.cloud.goog/v1/echo`
  * **Staging** : Before you deploy to production, you test your APIs on your staging backend, which is in its own project. For example:

    * `my-api.endpoints.**my‐project-staging**.cloud.goog/v1/echo`
  * **Running a private alpha** : When you want to test a new version of your service with some customers, but not all, the easiest approach is to put the alpha version in its own project, which provides the highest level of isolation from production. For example:

    * `my-api.endpoints.**my‐project-alpha**.cloud.goog/**v2alpha** /echo`

Alternatively, you could put the alpha version in the same project but configure it as a separate service. Since it is a separate service, you can restrict access to only the alpha customers. For example:

    * `**my-api-alpha**.endpoints.my-project.cloud.goog/**v2alpha** /echo`
  * **Running an open alpha** : When you want to release an alpha version that is available to all customers, you can put it in the same service and project as the existing version, and change the path. For example:

    * `my-api.endpoints.my-project.cloud.goog/**v2alpha** /echo`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
