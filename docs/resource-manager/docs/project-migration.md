---
url: https://docs.cloud.google.com/resource-manager/docs/project-migration/
title: Migrate projects between organization resources \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:00.495556+00:00
---

# Migrate projects between organization resources  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/project-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Migrate projects between organization resources Stay organized with collections  Save and categorize content based on your preferences. 

Migrating a Google Cloud project is a metadata operation that changes the project's location in the resource hierarchy. This page provides an overview of how migrations work, what stays the same, and what changes when a project moves to a new organization.

## Projects in the resource hierarchy

The project resource is the base-level organizing entity in a Google Cloud organization resource. Projects are created under organization resources and can be placed under folders or the organization resource itself, forming the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

You may need to migrate projects between organization resources due to acquisitions, regulatory requirements, or the separation of business units. You can use the Resource Manager API to migrate these projects. The migration operation returns a string representing the operation name. The API also lets you roll back a migration, moving the project back to its original place in the hierarchy if necessary.

## Migration scenarios

Your project's location determines which of two paths you take:

  * Migrate projects from one organization to another organization resource.
  * Migrate a standalone project (created without an organization) into the hierarchy of an organization resource.



If you need to move a project back to **No organization** after it is associated with an organization resource, you must contact Cloud Customer Care. Self-service rollback from an organization back to no organization isn't supported.

In addition to the API, you can also use the Google Cloud console to move projects by selecting the project and assigning it a new parent destination.

## Identify the project's current state

Before you begin, you must determine if your project is associated with an organization resource. This determines whether you follow the _Organization-to-Organization_ path or the _No Organization_ path.

If you don't have the `resourcemanager.organizations.get` permission on the parent organization resource of the project, it's likely that your projects don't reflect as expected under the actual organization in the Google Cloud console. This can make it seem like the project is not associated with any organization resource.

To determine whether the project is associated with an organization resource, run the following command:

###  gcloud 
    
    
    gcloud projects get-ancestors PROJECT_ID
    

Replace PROJECT_ID with the ID of the project that you want to migrate.

If the output includes an `organization` resource type in the hierarchy, your project is already part of an organization hierarchy.

If the `organization` type is missing or empty, the project is a standalone project with no organization resource.

Based on your project's state, follow the relevant guide:

  * If you want to migrate projects that were created with no associated organization, see [Migrate projects that are not associated with an organization resource](https://docs.cloud.google.com/resource-manager/docs/handle-special-cases#migrating_projects_no_org).
  * If you want to migrate projects from one organization to another organization resource, see [Migrate projects between organization resources](https://docs.cloud.google.com/resource-manager/docs/project-migration).

**Note:** If you want to transfer Google Workspace domains between organization resources, contact your Support representative.

## How migration works

A project migration is not a data transfer. Your services, databases, and virtual machine (VM) instances remain active and don't experience downtime. Instead, the migration updates the project's parent resource. Because Google Cloud follows a hierarchical inheritance model, the project's security posture changes the moment it's attached to a new parent.

Feature | Status | Impact  
---|---|---  
Project ID and number | Stays the same | API keys, service names, and hardcoded IDs remain unchanged.  
Data and resources | Stays the same | VMs, Storage buckets, and databases remain online.  
Direct IAM roles | Stays the same | Roles granted directly on the project move with it.  
Inherited IAM roles | Changes | Roles granted at the source organization or folder level are lost.  
Organization policies | Changes | Source constraints are replaced by destination constraints.  
Quotas | Changes | Inherited organization-level quotas are lost; project-level quotas remain.  
Billing account | Stays the same | The project remains linked to the original billing account.  
  
### Quota impact

If you have quotas defined at a certain resource level, the following aspects are applied after migration:

  * Any quotas defined at the project level remain unchanged.
  * Any quotas defined at the organization resource level are _not_ transferred. The organization loses any inherited quotas or quota overrides.



The following pages can be used to determine what quotas are applied to an organization resource:

  * [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage)
  * [List quotas with gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/quota/list)
  * [List quotas with RPC](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics/list)
  * [Example quota bucket](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits#quotabucket)



#### Example
    
    
    $ gcloud alpha services quota list --service=compute.googleapis.com --consumer=projects/workloadyee --filter="metric: compute.googleapis.com/cpus"
    
    ...
      - defaultLimit: '600'
        dimensions:
          region: us-central1
        effectiveLimit: '650'
    ...
    

## Critical considerations

Before starting a migration, review these high-risk areas to prevent service disruption:

  * Quota Limits: If the destination organization has lower quota limits than the source, your project may exceed its quota upon arrival.

  * Asset Inventory: Updates to the complete list of resources in Cloud Asset Inventory can take a few days to fully propagate after migration.

  * Cost and discounts: If the original organization had SKU-based or Enterprise Discount Program (EDP) discounts, those discounts don't apply in the new organization until you negotiate them with your Google Sales representative. Committed use discounts (CUDs) and Google Cloud Marketplace purchases might also need repurchasing.

  * Support Tiers: If there is no active support contract or a lower-tier support level in the destination organization, you might lose your current support tier.

  * Custom roles: If your project relies on custom IAM roles defined at the organization level, those roles won't exist in the destination. Recreate them in the destination organization before moving.




## The migration roadmap

Use the following roadmap to navigate the project migration process:

  1. Prepare: [Create a migration plan](https://docs.cloud.google.com/resource-manager/docs/create-migration-plan) to to coordinate timing.
  2. Perform: Assign IAM roles and configure organization policies and [execute the migration](https://docs.cloud.google.com/resource-manager/docs/perform-migration).
  3. Verify: Complete post-migration tasks, such as auditing inherited policies and updating billing.



## What's next

  * [Create a migration plan](https://docs.cloud.google.com/resource-manager/docs/create-migration-plan)
  * [Perform the migration](https://docs.cloud.google.com/resource-manager/docs/perform-migration)
  * [Handle special cases](https://docs.cloud.google.com/resource-manager/docs/handle-special-cases)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
