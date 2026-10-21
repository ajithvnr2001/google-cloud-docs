---
url: https://docs.cloud.google.com/alloydb/docs/tags/
title: Organize resources using tags \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:04.095166+00:00
---

# Organize resources using tags  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Organize resources using tags Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Google Cloud tags and how to use them with AlloyDB for PostgreSQL. To add tags to AlloyDB clusters and backups using `Google Cloud CLI`, see [Attach and manage tags](https://docs.cloud.google.com/alloydb/docs/manage-tags).

## Overview of tags

Google Cloud _tags_ are key-value pairs that you can use to organize your AlloyDB resources.

For example, a tag key can be a property, such as `environment`, and the tag value can be an attribute, such as `development` or `production`. A tag can have only one value for a given key on a particular resource.

Tags are created at the [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) or [project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) level. In AlloyDB, they are attached to the cluster or backup resources through the Resource Manager, which is used across Google Cloud.

You can add a reference to tags in [Identity and Access Management (IAM) policy bindings](https://docs.cloud.google.com/iam/docs/tags-access-control) to grant conditional access to resources. Tags are different from [labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#what-are-labels) which are another way to organize and filter your AlloyDB resources. Tags and labels work independently of each other, and you can use both on the same AlloyDB resource.

## Grant permissions based on conditional tag bindings

After you attach a tag to an AlloyDB resource, you can use the tag with IAM Conditions to conditionally grant access to AlloyDB resources. For more information about setting conditions based on tags, see [Resource tags](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags). IAM Conditions let you impose fine-grained access control on AlloyDB resources.

To use IAM Conditions, you reference the tags in IAM policy bindings. For more information about how to control access to your Google Cloud resources using use tags with IAM, see [Tags and conditional access](https://docs.cloud.google.com/iam/docs/tags-access-control).

## Export Cloud Billing data to BigQuery with resource-level tags

After configuring your project to export Cloud Billing data to BigQuery, your Cloud Billing data such as usage, cost estimates, and pricing details are automatically and continuously exported to a BigQuery dataset. You can then query this data using resource-level tags in BigQuery.

For setup instructions and query examples, see:

  * [Set up Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)
  * [Query examples with tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags)



## Enforcement of mandatory tags using organization policies

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can enforce mandatory tags on AlloyDB cluster and backup resources using an organization policy. To ensure compliance, mandatory tags enforce your organization's tagging policies, and prevent the creation of AlloyDB resources if the mandatory tag values are missing.

To learn how to enforce mandatory tags using custom organization policies, see [enforcing mandatory tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#enforce_tags) in Resource Manager documentation.

## Limitations

Tags have the following restrictions:

  * You can't attach tags to the instance resource in AlloyDB.
  * Backup resources don't inherit tags from their corresponding clusters.
  * Tag-based permissions might fail permission checks performed using the UI since AlloyDB might falsely deny access for resources that have policies applied at the resource level. However, other access methods like Google Cloud CLI, REST API, and Terraform work correctly.
  * You can only enforce mandatory tags for on-demand backups. Enforcing mandatory tags on for automated or continuous backups isn't supported.



## What's next

  * Learn how to [create and manage tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing) using Resource Manager.
  * See specific `gcloud CLI` commands for AlloyDB in [Manage tags on AlloyDB](https://docs.cloud.google.com/alloydb/docs/manage-tags). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
