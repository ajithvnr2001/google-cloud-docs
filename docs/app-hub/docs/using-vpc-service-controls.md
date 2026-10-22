---
url: https://docs.cloud.google.com/app-hub/docs/using-vpc-service-controls/
title: Use VPC Service Controls with App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:13.498093+00:00
---

# Use VPC Service Controls with App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/using-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Use VPC Service Controls with App Hub Stay organized with collections  Save and categorize content based on your preferences. 

VPC Service Controls is a Google Cloud feature that lets you set up a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) that creates a data transfer boundary around Google Cloud resources. VPC Service Controls provides more security for your App Hub resources such as mitigating the risk of data exfiltration. Using VPC Service Controls, you can add projects to service perimeters that protect applications, services, and workloads from requests that cross the perimeter.

App Hub resources are exposed on the `apphub.googleapis.com` API, which lets you perform operations, such as creation and deletion of applications, services, and workloads. You can set up VPC Service Controls with App Hub by restricting connectivity to this API surface.

We recommend that you protect all App Hub resources when creating a service perimeter.

App Hub supports the following resource types:

  * Application
  * Discovered service
  * Discovered workload
  * Service
  * Service project attachment (only for applications managed by a host project)
  * Workload



## Applications in a management project

When you enable the App Hub API for a single-project or folder-level [boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models), the system enables the required APIs for application management in the [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project).

After the management project is created, you can also enable recommended APIs that provide more application-centric features.

To include the management project in a service perimeter, [create](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) or [update](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) your service perimeter so that the management project and the enabled APIs are included in the perimeter.

For applications in a [folder boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary), VPC Service Controls restrictions apply only to App Hub interactions in the management project. App Hub can read application data and discover services and workloads for all descendent projects of the app-enabled folder, even if those projects are not in the same perimeter as the management project.

To learn about which APIs are required and recommended, see [Required and recommended APIs](https://docs.cloud.google.com/app-hub/docs/enabled-apis#apis).

## Applications managed by a host project

For [legacy host projects](https://docs.cloud.google.com/app-hub/docs/key-concepts#host-project), you can only attach a [service project](https://docs.cloud.google.com/app-hub/docs/key-concepts#service-project) if the host project and service project are in the same perimeter. If you move a previously-attached service project outside the perimeter, the service project's resources remain accessible until you detach the service project from the host project.

## What's next

  * To learn more about VPC Service Controls, see the [overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview) and [supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).

  * For best practices for enabling VPC Service Controls, see [Best practices for enabling VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/enable).

  * For best practices for designing service perimeters, see [Design and architect service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/architect-perimeters).

  * To set up a service perimeter, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
