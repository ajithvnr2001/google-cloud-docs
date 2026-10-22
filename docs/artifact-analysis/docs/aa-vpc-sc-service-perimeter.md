---
url: https://docs.cloud.google.com/artifact-analysis/docs/aa-vpc-sc-service-perimeter/
title: Protect Artifact Analysis in a service perimeter \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:20.328216+00:00
---

# Protect Artifact Analysis in a service perimeter  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/aa-vpc-sc-service-perimeter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Protect Artifact Analysis in a service perimeter Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) improves your ability to mitigate the risk of unauthorized copying or transfer of data from Google-managed services.

With VPC Service Controls, you can configure security perimeters around the resources of your Google-managed services and control the movement of data across the perimeter boundary.

## Use Artifact Analysis with VPC Service Controls

VPC Service Controls provides support for Artifact Analysis. Depending on your pipeline, it might require adding some other services to your service perimeter. To learn more, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_artifact-analysis).

For general instructions to add Artifact Analysis to a service perimeter, see [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

Ensure that other Google Cloud services that you use with Artifact Analysis are also in the perimeter, including:

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc)
  * [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/securing-with-vpcsc)



**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
