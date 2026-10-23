---
url: https://docs.cloud.google.com/alloydb/docs/psa-remove-allocated-range/
title: Remove a private services access allocated range \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:07.238387+00:00
---

# Remove a private services access allocated range  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/psa-remove-allocated-range/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Remove a private services access allocated range Stay organized with collections  Save and categorize content based on your preferences. 

To reclaim IP address space in your Virtual Private Cloud (VPC) network after deleting all AlloyDB for PostgreSQL clusters and instances that use an allocated range, you can remove the private services access allocated range.

When you create an AlloyDB cluster or instance in a region that doesn't yet have any clusters or instances, AlloyDB creates a subnet in that region in a Google-owned and managed project, which is called a _tenant project_. The subnet is connected to your network using the private services access VPC Network Peering connection.

If you decide to remove all AlloyDB resources associated with an allocated range, as well as the allocated range itself, follow the steps in this document to clean up your network resources.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.

  * To remove the allocated IP address range, you also must have these Identity and Access Management (IAM) permissions: 
    * `compute.networks.list`
    * `compute.addresses.delete`
    * `compute.addresses.list`
    * `servicenetworking.services.addPeering`



## Remove an allocated range

To remove an allocated range associated with your AlloyDB resources, follow these steps:

  1. [Delete all AlloyDB resources](https://docs.cloud.google.com/alloydb/docs/cluster-delete) that are using the allocated range.
  2. [Remove the allocated range from the private services access connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#modifying-connection).
  3. [Delete the allocated range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#deleting-allocation).
  4. Contact [Support](https://docs.cloud.google.com/support) and ask them to delete the subnets that private services access created on the tenant project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
