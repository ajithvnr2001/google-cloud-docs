---
url: https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-block-storage-commitments/
title: Purchase block storage commitments for Exapools \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:34.587615+00:00
---

# Purchase block storage commitments for Exapools  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-block-storage-commitments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Purchase block storage commitments for Exapools Stay organized with collections  Save and categorize content based on your preferences. 

In Compute Engine, block storage is commonly referred to as disks, volumes, or storage pools. [Block storage commitments](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#block_storage_commitments) provide committed use discounts (CUDs) specifically for block storage in Hyperdisk Exapools. To receive block storage CUDs, you must first purchase a 1-year or 3-year commitment for Exapool [capacity units](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools#how_capacity_units_work). After your commitment becomes active, Google Cloud applies CUDs to the matching capacity units that you provision in your Exapools. Persistent Disk volumes, Hyperdisk Storage Pools, and standalone Hyperdisk volumes created outside of an Exapool aren't eligible for block storage CUDs. 

This document explains how to request block storage commitments for Exapool capacity units.

## Before you begin

Before you request block storage commitments from your account team, complete the following prerequisites:

  1. Review the following documents: 
     * [Hyperdisk Exapools overview](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools) document
     * [Block storage commitments](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#block_storage_commitments) in the resource-based committed use discounts overview
     * [Service-specific terms](https://cloud.google.com/terms/service-terms)
  2. Verify that your project has sufficient regional `Commitments` quota in the region where you want to purchase the commitment. For more information, see [Quotas for commitments and committed resources](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#quota).



### Required roles

To get the permissions that you need to view and manage block storage commitments after your account team creates them, ask your administrator to grant you the following IAM roles on your project: 

  * To view block storage commitments: Compute Viewer (`roles/compute.viewer`) or Compute Admin (`roles/compute.admin`) 
  * To enable or disable auto-renewal on an existing block storage commitment: [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view and manage block storage commitments after your account team creates them. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view and manage block storage commitments after your account team creates them:

  * To view block storage commitments: `compute.commitments.get` and `compute.commitments.list`
  * To enable or disable auto-renewal on an existing block storage commitment: `compute.commitments.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Request block storage commitments through your account team

To purchase block storage commitments for Hyperdisk Exapools, contact your Google Cloud account team. Compute Engine doesn't support self-service purchase of these commitments through the Google Cloud console, the gcloud CLI, or REST.

When you contact your account team, be prepared to provide the following details for your commitment request:

  * **Project ID** : the ID of the project where you want to purchase the commitment.
  * **Region** : the region where you plan to provision your Exapool capacity.
  * **Commitment plan** : the duration of the commitment (`1-year` or `3-year` plan).
  * **Exapool type** : the pool type that you want to commit to purchasing (Hyperdisk Balanced Exapool or Hyperdisk Throughput Exapool).
  * **Capacity unit types and amounts** : the amount of capacity (in GiB) that you want to commit to purchasing for each applicable [capacity unit type](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools#how_capacity_units_work) (capacity-optimized, read-optimized, or write-optimized units).
  * **Auto-renewal setting** : whether you want the commitment to [renew automatically](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically) at the end of its term.



After you purchase a commitment, your commitment becomes active on the following day at 12 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during daylight saving time). Compute Engine [ maintains a lien on your project](https://docs.cloud.google.com/resource-manager/docs/project-liens) for each region in your project where you purchase a commitment. When you purchase a new commitment for any region in your project, Compute Engine associates the lien for that region with the newly created commitment. 

Between the time of your commitment purchase and its activation time, the status of your commitment remains as `NOT_YET_ACTIVE` (or as `PENDING` on the Google Cloud console). After activation, the status of your commitment changes to `ACTIVE`. For example, suppose that you purchase your commitment on January 20, 2024, at 10:00 PM US and Canadian Pacific Time (UTC-8 or UTC-7). Compute Engine creates your commitment immediately with its status as `NOT_YET_ACTIVE`. Your commitment becomes `ACTIVE` on January 21, 2024, at 12:00 AM US and Canadian Pacific Time (UTC-8 or UTC-7). 

**Important:** After you purchase a commitment, you can't cancel it. If you move the project that is associated with the commitment to a different Cloud Billing account, then the project inherits the attribution and CUD sharing settings that apply to the destination account. For more information, see [Impact of changing a project's Cloud Billing account](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#moving-project-billing-account).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
