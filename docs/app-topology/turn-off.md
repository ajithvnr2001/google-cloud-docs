---
url: https://docs.cloud.google.com/app-topology/turn-off/
title: Turn off App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:39.018292+00:00
---

# Turn off App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/turn-off/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ Guides ](https://docs.cloud.google.com/app-topology/overview)



Send feedback 

#  Turn off App Topology Stay organized with collections  Save and categorize content based on your preferences. 

App Topology is [enabled by default](https://docs.cloud.google.com/service-usage/docs/enabled-service#default) when you create a project using Google Cloud console or Google Cloud CLI and is automatically enabled for an App Hub [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project).

To turn off App Topology in a project, disable the App Topology API (`apptopology.googleapis.com`). You can block API activation using an organization policy constraint, or you can selectively disable the API in specific projects.

## Restrict API activation using policies

To block usage of the App Topology API, use the **Restrict Resource Service Usage** organization policy constraint. You can define restrictions at the organization, folder, or project level. For details, see [Restrict service usage](https://docs.cloud.google.com/organization-policy/restrict-services).

## Disable the App Topology API

The following instructions describe how to disable the App Topology API on individual projects. If you want to disable the API at the folder or organization level without using an organization policy constraint, see [Hierarchical-service-activation](https://docs.cloud.google.com/service-usage/docs/overview/overview).

  1. To get the permissions that you need to disable the API, ask your administrator to grant you the [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. To turn off App Topology, do the following:

###  gcloud 

     1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

     2. Turn off the App Topology API (`apptopology.googleapis.com`) using the command [`gcloud services disable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/disable):
            
            gcloud services disable apptopology.googleapis.com
            

If successful, the command returns the following message:
            
            Operation finished successfully.
            

###  API 

Turn off the API (`apptopology.googleapis.com`) using the [`services.disable` method](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/disable):
    
    curl -X POST   
    
        -H "Authorization: Bearer $(gcloud auth print-access-token)"   
    
        "https://serviceusage.googleapis.com/v1/projects/PROJECT_ID/services/apptopology.googleapis.com:disable"
      

Replace `PROJECT_ID` with the ID of the project for which you are disabling App Topology.

If the command succeeds, it returns a [`long-running operation`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/operations), which includes a `name` field. You can use the value in the `name` field to [check the status of the operation](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/operations/get).




## What's next

Learn more about [enabling and disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
