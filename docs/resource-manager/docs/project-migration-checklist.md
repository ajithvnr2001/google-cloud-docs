---
url: https://docs.cloud.google.com/resource-manager/docs/project-migration-checklist/
title: Project migration checklist \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:28.203180+00:00
---

# Project migration checklist  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/project-migration-checklist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Project migration checklist Stay organized with collections  Save and categorize content based on your preferences. 

This checklist will help you to migrate projects between organization resources. The checklist below contains a list of the major tasks involved in migrating a project between organization resources, brief instructions for each step, and a link to more information.

****

###  Create a migration plan 

Analyze the impact of the migration on services running inside the project. Changes in the resource hierarchy can affect inherited policies. 

  * **Run Move Analysis** : Use the [Move Analysis API](https://docs.cloud.google.com/resource-manager/docs/analyze-move) to get a detailed breakdown of blockers.
  * **Evaluate policy impact** : Determine how the move affects inherited organization policies and Identity and Access Management (IAM) policies.
  * **Plan for downtime** : Some services might experience brief interruptions during the transition.



For more information, see [Create a migration plan](https://docs.cloud.google.com/resource-manager/docs/create-migration-plan). 

###  Address any special cases 

Identify and prepare for scenarios that require special handling at the project or organization level. 

  * **Check service dependencies** : Review if your project depends on services like Shared VPC, VPC Service Controls, or has active billing/subscriptions.
  * **Review special cases list** : Ensure you have a plan for each service listed in the detailed guide.
  * **Prepare rollback plan** : Understand how to roll back the migration if issues arise.



For a list of special cases and how to handle them, see [Handling special cases](https://docs.cloud.google.com/resource-manager/docs/handle-special-cases). 

###  Assign Identity and Access Management roles 

Assign the required IAM roles to the same principal email address in both the source and destination organization resources. 

You need the following roles:

  * Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) on the project you want to migrate.
  * Project Mover (`roles/resourcemanager.projectMover`) on the project's parent resource (folder or organization resource).
  * **If the destination is a folder** : Project Mover (`roles/resourcemanager.projectMover`) on the destination folder.
  * **If the destination is an organization** : Project Creator (`roles/resourcemanager.projectCreator`) on the destination organization resource.
  * Organization Policy Admin (`roles/orgpolicy.policyAdmin`) on both the source and destination organization resources.



For more details, see [Assign permissions](https://docs.cloud.google.com/resource-manager/docs/perform-migration#required-roles). 

###  Configure organization policies 

Enable cross-organization project migration by configuring specific organization policies. Without these, the migration will fail. 

  * **Configure source policy** : Set the `constraints/resourcemanager.allowedExportDestinations` constraint on the parent resource to allow exporting to the destination.
  * **Configure destination policy** : Set the `constraints/resourcemanager.allowedImportSources` constraint on the destination resource to allow importing from the source.



For more information, see [Configure organization policies](https://docs.cloud.google.com/resource-manager/docs/perform-migration#required-org-policies). 

###  Perform the migration 

Execute the migration using the Google Cloud console, Google Cloud CLI, or the Resource Manager API. 

  * **Run migration** : Use the `gcloud beta projects move` command or the Cloud Console to perform the move.
  * **Verify migration** : Confirm the project appears in the new destination and verify resource access.
  * **Perform post-migration tasks** : Verify inherited policies, audit access, and optionally update the billing account.
  * **Clean up** : Revoke temporary IAM roles and remove the temporary organization policy constraints.



For step-by-step instructions, see [Perform the migration](https://docs.cloud.google.com/resource-manager/docs/perform-migration). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
