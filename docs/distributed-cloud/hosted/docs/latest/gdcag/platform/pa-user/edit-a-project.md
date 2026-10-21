---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/edit-a-project/
title: Edit a project \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:40.419891+00:00
---

# Edit a project  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/edit-a-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Edit a project Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to edit an existing Google Distributed Cloud (GDC) air-gapped project. There are a subset of configurations for your project that can be updated after creation, such as project name, billing account, and data exfiltration protection. You can update these configurations as your usage of the project evolves.

This document is for audiences such as IT administrators, security engineers, and network administrators within the platform administrator group, who are responsible for managing resources within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To perform the tasks in this document, you must complete the following requirements:

  * To get the permissions that you need to edit an existing project, ask your Organization IAM Admin to grant you the Project Editor role (`project-editor`).

  * To use the gdcloud CLI, ensure you have it installed. For more information, see [Install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).




## Edit the configuration of a project

Projects offer a subset of configurations you can update after creation. Complete the following steps to find and change the configurable settings of your project:

###  Console 

  1. Open the navigation menu and select **Projects**.

  2. Click the project you want to edit.

  3. Click edit **Edit** next to the field you want to update.

  4. Provide the updated project configuration and click **Save**.




###  gdcloud 

  1. List the available configurations you can change for a project:
         
         gdcloud projects update --help
         

The output provides flags you can set in the `gdcloud projects update` command to update configurations of the project. For example, the `--name` flag updates the project name.

  2. Run the `gdcloud projects update` command with the flag corresponding to the configuration to update. For example, to update the project name, run:
         
         gdcloud projects update PROJECT_ID --name=PROJECT_NAME
         

Replace the following variables:

     * `PROJECT_ID`: the unique identifier for your project.
     * `PROJECT_NAME`: the new name for the project.



## What's next

  * [Design access boundaries between resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries)
  * [Configure organization policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-policy)
  * [Create and link billing accounts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
