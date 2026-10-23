---
url: https://docs.cloud.google.com/vpc-service-controls/docs/vpc-perimeters-management/
title: VPC networks management in service perimeters \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:11.915725+00:00
---

# VPC networks management in service perimeters  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/vpc-perimeters-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  VPC networks management in service perimeters Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of how you can manage VPC networks and VPC Service Controls.

You can create separate perimeters for each of the VPC networks in your host project instead of creating a single perimeter for the entire host project. For example, if your host project contains separate VPC networks for development, test, and production environments, you can create separate perimeters for the development, test, and production networks.

You can also allow access from a VPC network that is not inside your perimeter to resources inside your perimeter by specifying an ingress rule.

The following diagram shows an example of a VPC networks host project and how you can apply a different perimeter policy for each VPC network:

![Perimeter policy for each VPC network](https://docs.cloud.google.com/static/vpc-service-controls/images/vpc-network-entity.svg)

  * **VPC networks host project**. The host project contains VPC network 1 and VPC network 2, each containing virtual machines VM A and VM B respectively.
  * **Service perimeters**. The service perimeters SP1 and SP2 contain BigQuery and Cloud Storage resources. As VPC network 1 is added to perimeter SP1, VPC network 1 can access resources in perimeter SP1 but cannot access resources in perimeter SP2. As VPC network 2 is added to perimeter SP2, VPC network 2 can access resources in perimeter SP2 but cannot access resources in perimeter SP1.



## Manage VPC networks in a service perimeter

You can perform the following tasks to manage VPC networks in a perimeter:

  * Add a single VPC network to a perimeter instead of adding an entire host project to the perimeter.
  * Remove a VPC network from a perimeter.
  * Allow a VPC network to access resources inside a perimeter by specifying an ingress policy.
  * Migrate from a single perimeter setup to a multiple perimeter setup and use dry-run mode to test the migration.



## Limitations

The following are the limitations when you manage VPC networks in service perimeters:

  * You can add VPC networks from another organization to your service perimeter or specify them as an ingress source only if you have the [`roles/compute.networkViewer`](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkViewer) role for those networks.
  * If you delete a VPC network protected by a perimeter and then recreate a VPC network with the same name, the service perimeter does not protect the VPC network that you recreate. We recommend that you don't recreate a VPC network with the same name. To resolve this issue, create a VPC network with a different name and add it to the perimeter.
  * The limit for the number of VPC networks that you can have under an organization is 500.
  * If a VPC network has a custom subnet mode but if no subnets exist, then that VPC network cannot be added independently to VPC Service Controls. To add a VPC network to a perimeter, the VPC network must contain at least one subnet.



## What's next

  * Learn about [rules to add VPC networks to service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-networks-rules).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
