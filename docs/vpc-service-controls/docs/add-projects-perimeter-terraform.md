---
url: https://docs.cloud.google.com/vpc-service-controls/docs/add-projects-perimeter-terraform/
title: Add projects to service perimeters using Terraform \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:38.195340+00:00
---

# Add projects to service perimeters using Terraform  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/add-projects-perimeter-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Add projects to service perimeters using Terraform Stay organized with collections  Save and categorize content based on your preferences. 

VPC Service Controls lets you isolate resources of a supported multi-tenant Google Cloud service to mitigate data exfiltration risks. You can use Terraform to add a project in a folder to a service perimeter.

To automatically add a folder to a service perimeter, you can use Cloud Run functions. When the function detects a new project being added to the folder, it executes the Terraform script to add the new project to the perimeter. Similarly, the function automatically removes projects from the perimeter if they are moved out of the folder.

For more information, see [Automatically secured folder](https://github.com/terraform-google-modules/terraform-google-vpc-service-controls/tree/master/examples/automatic_folder).

## What's next

  * [Overview of a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters)
  * [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
