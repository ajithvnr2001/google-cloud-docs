---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/manage-harbor-instances/
title: Manage Harbor registry instances \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:12.042048+00:00
---

# Manage Harbor registry instances  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/manage-harbor-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage Harbor registry instances Stay organized with collections  Save and categorize content based on your preferences. 

This page details how to manage your created Harbor registry instances. View or delete your created Harbor registry instances using the Google Distributed Cloud (GDC) air-gapped console or the GDC gdcloud CLI. Delete unused Harbor instance registries to lower your storage costs and free up space.

## Before you begin

Request the necessary permissions from your IAM administrator. Enforce least privilege access by requesting only the roles required for your specific tasks.

### Required IAM roles

If you are responsible for managing Harbor registry instances, contact your IAM Project Admin to request the following project-level roles:

  * **Harbor Instance Admin** (`harbor-instance-admin`): get, list, watch, create, update, patch, and delete Harbor instances, backup repositories, backup plans, backups, and restores within a project. Request this role if you are responsible for permanently deleting unused Harbor instances to free up space.
  * **Harbor Instance Viewer** (`harbor-instance-viewer`): get, list, and watch Harbor instances within a project. Request this role if you only need the permissions to view the details and status of existing instances.



## View Harbor registry instances

View your created Harbor registry instances in the GDC console or use the GDC gdcloud CLI.

###  Console 

  1. In the navigation menu, in the **CI/CD** section, click **Harbor Container Registry**.
  2. View the list of created Harbor instances in the **Instances** section.
  3. For more detail about a specific instance, click the **Go to Harbor Instance** external link.



###  gdcloud 

View the Harbor registry instance:
    
    
    gdcloud harbor instances describe INSTANCE \
      --project=PROJECT
    

Replace the following:

  * `INSTANCE`: the name of the instance.
  * `PROJECT`: the name of the project.



## Delete Harbor registry instances

Delete an existing Harbor registry instance if it is no longer required. Harbor registry instances in the GDC console or use the GDC gdcloud CLI.

###  Console 

  1. In the navigation menu, in the **CI/CD** section, click **Harbor Container Registry**.
  2. Click **Delete Instance**.
  3. On the confirmation dialog:

     1. Click **Cancel** to stop the delete operation.
     2. Click **Delete** to confirm the deletion of the Harbor instance.



###  gdcloud 

Delete the Harbor registry instance:
    
    
    gdcloud harbor instances delete INSTANCE \
      --project=PROJECT
    

Replace the following:

  * `INSTANCE`: the name of the instance.
  * `PROJECT`: the name of the project.



## What's next

To start hosting and managing images in your instance, create a Harbor project and configure your client connection to the Harbor registry:

  * [Create Harbor projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-projects)
  * [Configure Docker to trust the Harbor root CA](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-trust)
  * [Sign in to Docker and Helm](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-authentication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
