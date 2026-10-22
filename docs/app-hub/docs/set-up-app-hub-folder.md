---
url: https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder/
title: Set up a folder \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:14.162791+00:00
---

# Set up a folder  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Set up a folder Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up a Google Cloud folder as an [app-enabled folder](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-enabled-folder).

With an app-enabled folder, you can manage applications and group resources from all projects and subfolders it contains. This configuration is also known as the [folder-level boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).

App-enabled folders contain a [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) and support all Application-centric Google Cloud features, including application design in Application Design Center, insights in Cloud Hub, and assistance from Gemini Cloud Assist. You can register resources from the Google Cloud projects in the app-enabled folder as [services](https://docs.cloud.google.com/app-hub/docs/key-concepts#service) and [workloads](https://docs.cloud.google.com/app-hub/docs/key-concepts#workload) of applications.

After you set up an App Hub application on an app-enabled folder, you can use natural language prompts to retrieve information about this application. For more information, see [Use Gemini Cloud Assist in the Google Cloud console](https://docs.cloud.google.com/cloud-assist/chat-panel).

You use [Resource Manager](https://docs.cloud.google.com/resource-manager/docs) to configure and manage app-enabled folders. For more information about the application-centric model and its resource organization, see [Application-centric Google Cloud](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud).

## Configure an app-enabled folder

Before you begin, ensure you have the [required roles](https://docs.cloud.google.com/resource-manager/docs/manage-applications#roles) to configure the app-enabled folder.

To set up the folder, follow the Resource Manager instructions to [manage applications in a folder](https://docs.cloud.google.com/resource-manager/docs/manage-applications).

## Manage projects in your app-enabled folder

App-enabled folders automatically make infrastructure resources from all descendant projects and folders available to group into an application. To control which resources are available, you can create, move, or delete projects and folders in the app-enabled folder:

  * [Create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project)
  * [Shutting down (deleting) projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects)
  * [Moving a project](https://docs.cloud.google.com/resource-manager/docs/moving-projects-folders)
  * [Moving a folder](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#moving_a_folder_into_another_folder)



It is important to understand the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) in your app-enabled folder. If a project or folder containing services and workloads that you have grouped in an application is moved out of the app-enabled folder, the application will continue to exist in the app-enabled folder, but the [registration status of services and workloads](https://docs.cloud.google.com/app-hub/docs/overview#registration-status) from that project or folder will change to _detached_.

## Disable application management in a folder

You can disable application management from your Google Cloud folder if you don't want it to be an app-enabled folder anymore. For instructions, see [Disable application management](https://docs.cloud.google.com/resource-manager/docs/manage-applications#disable-application-management).

## What's next

  * [Quickstart: Create an application from existing resources](https://docs.cloud.google.com/app-hub/docs/quickstart-create-application)
  * [Prepare for application lifecycle management](https://docs.cloud.google.com/app-hub/docs/prepare-for-app-lifecycle-management)
  * [Register resources to an application](https://docs.cloud.google.com/app-hub/docs/register-resources)
  * [Set up application monitoring](https://docs.cloud.google.com/monitoring/docs/setup-application-monitoring)
  * [App Hub IAM roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions)
  * [App Hub overview](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
