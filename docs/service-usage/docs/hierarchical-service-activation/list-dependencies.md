---
url: https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/list-dependencies/
title: List service dependencies \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:50.017134+00:00
---

# List service dependencies  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/list-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ Guides ](https://docs.cloud.google.com/service-usage/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# List service dependencies

**Preview — Hierarchical service activation**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Hierarchical service activation lets you manage service enablement that is inherited through the Google Cloud resource hierarchy. For more information, see the [overview](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/overview).

Many Google Cloud services need other services to function. When you enable a service using hierarchical service activation, its required dependencies are automatically added to the `ConsumerPolicy`. A _service dependency group_ contains these relied-on services, which you can list to better understand and manage them.

This document shows you how to use the Google Cloud CLI to list service dependencies for projects, folders, and organizations.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  11. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  12. If you don't indicate the Google Cloud resource that you want to manage, the commands in this document default to the current project. For example, `gcloud beta services groups list-members bigquery.googleapis.com dependencies` lists the members for the current project. 

You can retrieve the current project ID:
         
         gcloud config list --format='text(core.project)'




### Required roles

To get the permissions that you need to list service dependencies, ask your administrator to grant you the [Service Usage Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer) (`roles/serviceusage.serviceUsageViewer`) IAM role on your target resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list service dependencies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list service dependencies:

  * List dependency group members: `serviceusage.groups.listMembers`
  * List expanded dependency group members: `serviceusage.groups.listExpandedMembers`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List dependency group members

You can list the direct members of a service dependency group for a project, folder, or organization by using the [`gcloud beta services groups list-members`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/groups/list-members) command:
    
    
    gcloud beta services groups list-members SERVICE GROUP \
        --RESOURCE_TYPE=RESOURCE_ID
    

Replace the following:

  * `SERVICE`: the name of the service you want to list members for.

  * `GROUP`: the name of the service dependency group you want to list members for. The primary supported group is `dependencies`.

  * `RESOURCE_TYPE`: the type of the resource you want to list members for. Valid values are `project`, `folder`, and `organization`. You can omit this flag entirely to return results for the current project.

  * `RESOURCE_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders), or [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id), depending on the value you used for `RESOURCE_TYPE`.




You can use [other flags](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/groups/list-members) to filter and limit the members listed.

## List expanded dependency group members

You can list the expanded members of a service dependency group for a project, folder, or organization by using the [`gcloud beta services groups list-expanded-members`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/groups/list-expanded-members) command.

This command returns a flattened list of all dependencies, including those in nested groups, to provide a complete, combined list of all service dependencies.
    
    
    gcloud beta services groups list-expanded-members SERVICE GROUP \
        --RESOURCE_TYPE=RESOURCE_ID
    

Replace the following:

  * `SERVICE`: the name of the service you want to list members for.

  * `GROUP`: the name of the service dependency group you want to list members for. The primary supported group is `dependencies`.

  * `RESOURCE_TYPE`: the type of the resource you want to list members for. Valid values are `project`, `folder`, and `organization`. You can omit this flag entirely to return results for the current project.

  * `RESOURCE_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders), or [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id), depending on the value you used for `RESOURCE_TYPE`.




You can use [other flags](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/groups/list-expanded-members) to filter and limit the members listed.

## Examples

#### Listing direct dependency group members

  * Listing direct dependencies of BigQuery service for the current project: 
        
        gcloud beta services groups list-members bigquery.googleapis.com dependencies

Output:
        
        NAME: services/analyticshub.googleapis.com
        REASON: BigQuery depends on this group to allow users to exchange data and analytics assets.
        
        NAME: services/bigquery.googleapis.com
        REASON: The service representing BigQuery which owns this dependency group and depends on the other members of this group.
        
        NAME: services/bigqueryconnection.googleapis.com
        REASON: BigQuery depends on this group to allow users to manage connections to external data sources.
        
        NAME: services/bigquerydatapolicy.googleapis.com
        REASON: BigQuery depends on this group to allow users to manage their data policies.
        
        ...

  * Attempting to list dependencies of API keys service without a corresponding service dependency group: 
        
        gcloud beta services groups list-members apikeys.googleapis.com dependencies --project=test-project

Output:
        
        Listed 0 items.




#### Listing expanded dependency group members

  * Listing expanded dependencies of BigQuery service for the current project: 
        
        gcloud beta services groups list-expanded-members bigquery.googleapis.com dependencies

Output:
        
        services/analyticshub.googleapis.com
        services/bigquery.googleapis.com
        services/bigqueryconnection.googleapis.com
        services/bigquerydatapolicy.googleapis.com
        services/bigquerydatatransfer.googleapis.com
        services/bigquerymigration.googleapis.com
        services/bigqueryreservation.googleapis.com
        services/bigquerystorage.googleapis.com
        services/cloudresourcemanager.googleapis.com
        services/dataform.googleapis.com
        services/dataplex.googleapis.com




## What's next

  * To enable and disable services, see [Manage service enablement](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-enablement).
  * To manage policies, see [Manage consumer policies](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-consumer-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
