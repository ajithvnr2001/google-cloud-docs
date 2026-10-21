---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-a-project/
title: Delete a project \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:42.611326+00:00
---

# Delete a project  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-a-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Delete a project Stay organized with collections  Save and categorize content based on your preferences. 

Delete a project to remove a group of resources within an organization. When deleting a project in Google Distributed Cloud (GDC) air-gapped, the system first verifies the project is eligible for deletion. If the system reports precheck errors, you must manually fix the issues before you can initiate project deletion.

## Before you begin

To get the permissions needed to delete a project, ask your Organization IAM Admin to grant you the Project Editor role (`project-editor`).

## Delete a project and its resources

**Important:** Project deletion in the GDC console does not work, although the delete **Delete** button and corresponding deletion page are available. Delete a project using the supported workflows for gdcloud or Terraform.

To delete a project, complete the following steps:

###  gdcloud 

  1. Ensure you have the gdcloud CLI installed. For more information, see the gdcloud CLI [Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview#download_and_install_the) page.

  2. To delete the project, run:
         
         gdcloud projects delete PROJECT_ID
         

Replace `PROJECT_ID` with the unique identifier for the project to delete.




If the project deletion prechecks complete successfully, the GDC system begins deleting the project. If the prechecks don't complete successfully, precheck failures with corresponding error codes are reported in the gdcloud CLI.

###  Terraform 

  * To delete a project using Terraform, run:
        
        terraform destroy -target kubernetes_manifest.project-create
        




You must manually fix the issues reported before you can delete the project. See the Handle project deletion precheck failures section for steps to manually fix precheck failures.

## Handle project deletion precheck failures

If the project deletion precheck task isn't successful, you are given a code that maps to the issue. Locate the code in the following sections, and complete the outlined steps to fix the issue.

### OBJ-E0001: Buckets must be deleted in project

This error occurs when deleting a project if it has storage buckets remaining. You must remove the buckets before the project can be deleted successfully.

Follow the [Delete storage buckets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-storage-buckets#cli) section to manually delete your project's storage buckets.

### DBS-E000X: Database clusters must be deleted in project

This error occurs when deleting a project if it has database clusters remaining.

#### DBS-E0001: PostgreSQL database clusters must be deleted

This error indicates that you still have PostgreSQL database clusters remaining in the project you are trying to delete.

You must remove all of the PostgreSQL database clusters in your project before the project can be deleted successfully.

Follow the [Delete database clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-delete-cluster) section to manually delete your project's database clusters.

#### DBS-E0002: Oracle database clusters must be deleted

This error indicates that you still have Oracle database clusters remaining in the project you are trying to delete.

You must remove all of the Oracle database clusters in your project before the project can be deleted successfully.

Follow the [Delete database clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-delete-cluster) section to manually delete your project's database clusters.

#### DBS-E0003: AlloyDB Omni database clusters must be deleted

This error indicates that you still have AlloyDB Omni database clusters remaining in the project you are trying to delete.

You must remove all of the AlloyDB Omni database clusters in your project before the project can be deleted successfully.

Follow the [Delete database clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-delete-cluster) section to manually delete your project's database clusters.

### VMM0001: Buckets must be deleted in shadow project

This error occurs when deleting a project if it has VM image buckets remaining in an internal project named a _shadow project_. Because this is an internal project, you must ask your Infrastructure Operator (IO) to complete this task.

Ask your IO to complete the [VMM-R0101](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/gdcag-io/service-manual/vmm/runbooks/vmm-r0101) runbook to delete the VM image buckets remaining in the shadow project. Be sure to provide the shadow project name to the IO, which follows the following format:
    
    
    PROJECT_NAME-vm-system
    

Replace `PROJECT_NAME` with the name of the project you want to delete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
