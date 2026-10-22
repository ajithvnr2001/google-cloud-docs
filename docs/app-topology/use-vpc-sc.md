---
url: https://docs.cloud.google.com/app-topology/use-vpc-sc/
title: Use VPC Service Controls with App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:38.593633+00:00
---

# Use VPC Service Controls with App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/use-vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ Guides ](https://docs.cloud.google.com/app-topology/overview)



Send feedback 

#  Use VPC Service Controls with App Topology Stay organized with collections  Save and categorize content based on your preferences. 

App Topology supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to strengthen data security and mitigate the risks of data exfiltration. With VPC Service Controls, you can configure security perimeters around the resources of your Google Cloud services and control the movement of data across the perimeter boundary.

When you enable the App Topology API, App Topology adds an access path for limited metadata for App Hub applications, Cloud Trace traces, and Cloud Monitoring alerts. Examples of metadata include trace span start and end times and App Topology application IDs.

VPC Service Controls restrictions for App Hub apply only to App Hub interactions in the management project. As a result, App Topology can read data for applications and discovered services and workloads for all descendent projects of the app-enabled folder, even if those projects are not in the same perimeter as the management project.

When you restrict the App Topology API in a perimeter, we recommend that you add to that perimeter the APIs for services that provide data to App Topology, including:

  * App Hub API (`apphub.googleapis.com`)
  * Cloud Asset API (`cloudasset.googleapis.com`)
  * Developer Connect API (`developerconnect.googleapis.com`)
  * Cloud Monitoring API (`monitoring.googleapis.com`)
  * Security Command Center API (`securitycenter.googleapis.com`)
  * Cloud Trace API (`trace.googleapis.com`)



See the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) for more information about supported products.

## What's next

  * Learn about [configuring service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
