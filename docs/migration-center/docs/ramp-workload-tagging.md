---
url: https://docs.cloud.google.com/migration-center/docs/ramp-workload-tagging/
title: RaMP workload tagging guide \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:41.841968+00:00
---

# RaMP workload tagging guide  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/ramp-workload-tagging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Resources ](https://docs.cloud.google.com/migration-center/docs/release-notes)



Send feedback 

#  RaMP workload tagging guide Stay organized with collections  Save and categorize content based on your preferences. 

## Tag workloads for RaMP incentives

Google Cloud [RaMP](https://cloud.google.com/solutions/cloud-migration-program) is an end-to-end migration and modernization program to help customers use expertise and best practices, lower risk, control costs, and simplify their path to cloud success.

RaMP accelerates customer workload migrations to Google Cloud through partner expertise and commercial incentives. This document outlines the workload tagging requirements customers must follow for RaMP incentive eligibility.

## Workload tagging - incentive requirements

To qualify for incentives, the following requirements must be met:

  * **Identify project(s):** Select a Google Cloud project for deploying your RaMP workload. You may spread a single Workload ID across multiple projects, but don't mix resources from different RaMP Workload IDs within the same project.
  * **Google curated tag key:** The curated **RaMP workload tag key** `google/deployment-wl-id`, which is a Google managed **Dynamic Tag Key** available in your Google Cloud organization, must be used to identify the RaMP workload. Google systems won't recognize a manually created tag, even if the **RaMP workload tag key** is used.
  * **Tag binding at project level:** RaMP incentives are based on the project level tag. Resources that are tagged differently within a project won't affect incentive calculations.
  * **Tag value:** For the Google curated tag, ensure the **tag value** is identical to the Workload ID found in the RaMP Agreement.



The following sections cover how to perform each of these required steps.

### Workload identification: use tags to identify RaMP Workloads

A key operational step of the migration and modernization phase is the RaMP workload tagging. This step ensures Google Cloud can track the workload, and is a necessary step to qualify for RaMP incentives.

The **Workload Identifier** (pre-fixed by `WL-`) has been generated and assigned to each workload deployment described in your RaMP Agreement. Once the RaMP Agreement has been executed, the **Workload Identifiers** are also available in your Google Cloud Console (organization).

As part of the migration and modernization phase, you can tag each RaMP workload with the **Workload Identifier** assigned to that workload. This **Workload Identification** process ensures accurate tracking between the anticipated deployment described in the contract and the actual deployment.

**Note:** You cannot list the pre-created `google/deployment-wl-id` tag key until you bind a Workload Identifier to a project.

### Tag Workloads

To qualify for RaMP incentives customers must select an existing, or create new Google Cloud projects for each RaMP Workload ID. Every project must be tagged with the correct Workload Identifier. While a single workload may span multiple projects, each project must be dedicated exclusively to one RaMP workload.

After creating the RaMP workload projects, customers must bind the curated tag to the projects using the Workload Identifier. This identifier can be found in the RaMP Agreement or the Google Cloud console.

RaMP Agreement (Workload Identifier is found in section 3 of the Agreement):

![Workload Identifier example from RaMP Agreement.](https://docs.cloud.google.com/static/migration-center/images/workload-identifier.png)Workload Identifier example from RaMP Agreement.

  * To view the tagged RaMP workload, go to **Cloud Billing** > **Workloads**.

[Go to Workloads in Cloud Billing console](https://console.cloud.google.com/billing/workloads)

![Example of the Workloads page in Cloud Billing.](https://docs.cloud.google.com/static/migration-center/images/workloads-billing-page.png)Workloads billing page.

**Note:** The **Workloads** page displays your tagged resources and Workload IDs. To monitor your milestone progress and earned credits, see [Track the status of your conditional incentives](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker). Tagged spend can take up to three days to appear in the incentives program tracker.

The curated tag key `google/deployment-wl-id` has been pre-created by Google and is already available in your Google Cloud organization. You don't need to create a new key.

Google Cloud tag binding is a feature that links tags to resources, such as an organization, folder, project. For the purpose of RaMP incentives, tag binding must be done at the project level.

For each relevant project, create a tag binding using the following parameters:

  * **Tag key:** `google/deployment-wl-id`
  * **Tag value:** WORKLOAD_IDENTIFIER



To bind the tag, the user needs the `resourcemanager.hierarchyNodes.createTagBinding` permission on the project. This permission is included in the following roles:

  * **Standard roles:** `Tag User`, `Owner`, or `Editor`.
  * **Custom roles:** Any custom role configured with the `resourcemanager.hierarchyNodes.createTagBinding` permission.



The tag key `google/deployment-wl-id` is public, so you only need permissions on the project, not on the tag key itself.

You can bind the tag to your project in one of the following ways:

###  gcloud 

  1. To create a `google/deployment-wl-id` tag binding, run the following command:
         
         gcloud resource-manager tags bindings create --parent="//cloudresourcemanager.googleapis.com/projects/PROJECT_ID" --tag-value="google/deployment-wl-id/WORKLOAD_IDENTIFIER"
         

  2. To verify that the tag binding was successfully created, run the following command:
         
         gcloud resource-manager tags bindings list --parent="//cloudresourcemanager.googleapis.com/projects/PROJECT_ID"
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * WORKLOAD_IDENTIFIER: the Workload Identifier assigned to the workload in your RaMP agreement.



###  Terraform 

To bind the `google/deployment-wl-id` tag to a project with Terraform, use the following configuration:
    
    
      resource "google_tags_tag_binding" "binding" {
        parent = "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
        tag_value = "google/deployment-wl-id/WORKLOAD_IDENTIFIER"
      }
    

Replace the following:

  * PROJECT_NUMBER: the number of your Google Cloud project.
  * WORKLOAD_IDENTIFIER: the Workload Identifier assigned to the workload in your RaMP Agreement.

**Note:** Terraform Google provider must be version v7.17.0 or later.

### Troubleshoot workload tagging errors

If you have applied an incorrect tag to a project, bind the correct tag to that project. Cloud Billing uses the last tag applied to calculate incentives.

#### Correct a tag bound to the wrong project

If a tag is bound to the wrong project, do the following:

  1. Bind the RaMP tag to the correct project.
  2. Unbind the tag from the incorrect project.



gcloud CLI supports both `create` and `delete` actions for managing these tag bindings. For more information, see [Tag Workloads](https://docs.cloud.google.com/migration-center/docs/ramp-workload-tagging#tagging-workloads).

## What's next

  * Learn how to [get started with Google Cloud Migration Center](https://docs.cloud.google.com/migration-center/docs/get-started-with-migration-center).
  * Learn how to [generate a rapid cost estimate](https://docs.cloud.google.com/migration-center/docs/generate-estimate).
  * Learn how to [track the status of your conditional incentives](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker).
  * Learn more about [creating and managing Resource Manager tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).
  * Learn more about [RaMP](https://cloud.google.com/solutions/cloud-migration-program).
  * Explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
