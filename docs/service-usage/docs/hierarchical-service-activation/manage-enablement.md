---
url: https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-enablement/
title: Manage service enablement \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:56.730887+00:00
---

# Manage service enablement  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-enablement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ Guides ](https://docs.cloud.google.com/service-usage/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage service enablement

**Preview — Hierarchical service activation**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Hierarchical service activation lets you manage service enablement that is inherited through the Google Cloud resource hierarchy. For more information, see the [overview](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/overview).

This document shows you how to use the Google Cloud CLI to manage service enablement for projects, folders, and organizations.

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

  12. If you don't indicate the Google Cloud resource that you want to manage, the commands in this document default to the current project. For example, `gcloud beta services list --enabled` returns a list of enabled services for the current project. 

You can retrieve the current project ID:
         
         gcloud config list --format='text(core.project)'




### Required roles

To get the permissions that you need to manage service enablement, ask your administrator to grant you the [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) IAM role on your target resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to manage service enablement. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage service enablement:

  * List services: 
    * `serviceusage.effectivepolicy.get`
    * `serviceusage.services.list`
    * `serviceusage.services.get`
  * Enable services: 
    * `serviceusage.consumerpolicy.get`
    * `serviceusage.consumerpolicy.update`
    * `serviceusage.groups.listExpandedMembers`
  * Disable services: 
    * `serviceusage.consumerpolicy.get`
    * `serviceusage.consumerpolicy.update`
    * `serviceusage.consumerpolicy.analyze`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List services

You can list the Google APIs and services that are enabled or available for a project, folder, or organization by using the [`gcloud beta services list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/list) command.

Service enablement and availability can be inherited from resource ancestors. A resource's enabled services include services that are enabled on the resource itself and enabled on all resource ancestors.

**Note:** Services hidden in the previous Service Usage release might now appear in the list of enabled services when using hierarchical service activation. This doesn't necessarily mean they were newly enabled. If required, you can disable them.
    
    
    gcloud beta services list --enabled \
        --RESOURCE_TYPE=RESOURCE_ID
    

Replace the following:

  * `RESOURCE_TYPE`: the type of resource that you want to list services for. Valid values are `project`, `folder`, and `organization`. You can omit this flag to return results for the current project.

  * `RESOURCE_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders), or [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id), depending on the value you used for `RESOURCE_TYPE`.




Note the following:

  * You must specify _one_ of the following flags:

    * `--available` to list services that _can be_ enabled for consumption.
    * `--enabled` to list the services that _are_ enabled for consumption.
  * You can use [other flags](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/list) to filter and limit the services listed.




## Enable services

You can enable one or more services for a project, folder, or organization by using the [`gcloud beta services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/enable) command.

This command updates the `ConsumerPolicy` at the target resource. For more information, see [Manage consumer policies](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-consumer-policies).
    
    
    gcloud beta services enable SERVICE \
        --RESOURCE_TYPE=RESOURCE_ID
    

Replace the following:

  * `SERVICE`: the name of the service you want to enable. To enable multiple services, use space-delimited service names. For example, the following command enables both the API keys and BigQuery services:
        
        gcloud beta services enable apikeys.googleapis.com bigquery.googleapis.com
        

  * `RESOURCE_TYPE`: the type of resource that you want to enable services for. Valid values are `project`, `folder`, and `organization`. You can omit this flag to enable services for the current project.

  * `RESOURCE_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders), or [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id), depending on the value you used for `RESOURCE_TYPE`.




Supported flags:

  * `--async` to return immediately, without waiting for the operation in progress to complete.

  * `--skip-dependency` to skip enabling any service dependencies. Otherwise, all service dependencies are enabled by default.

You can inspect service dependencies. For more information, see [List service dependencies](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/list-dependencies).

  * `--validate-only` to validate the enablement without actually performing the operation.




Note the following:

  * If you try to enable a service that is already enabled, you will receive an error stating that the service is already enabled and present in the consumer policy. (If the service is already enabled but its dependencies are not, the command will succeed.)

  * The organization policy constraint `constraints/serviceuser.services` isn't compatible with hierarchical service activation and shouldn't be used with it. Instead, to control which services can be enabled for a resource, use the `constraints/gcp.restrictServiceUsage` constraint. For more information, see [Restricting resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources).

    * If your organization has previously used `constraints/serviceuser.services` and you receive an error when you attempt to use hierarchical service activation, contact [Cloud Customer Care](https://docs.cloud.google.com/support).
  * Google Cloud creates and manages service accounts for many Google Cloud services. These service accounts are known as [_service agents_](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents). If you encounter a `service account not found` error, you might need to create a service agent using the [`gcloud beta services identity create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/identity/create) command.




## Disable services

You can disable one or more services for a project, folder, or organization by using the [`gcloud beta services disable`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/disable) command.

This command updates the `ConsumerPolicy` at the target resource. For more information, see [Manage consumer policies](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-consumer-policies).

**Note:** Existing resources might prevent you from disabling a service. You can delete these resources and try to disable the service again. Alternatively, you can [restrict resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) using an organization policy constraint.
    
    
    gcloud beta services disable SERVICE \
        --RESOURCE_TYPE=RESOURCE_ID
    

Replace the following:

  * `SERVICE`: the name of the service you want to disable. To disable multiple services, use space-delimited service names. For example:
        
        gcloud beta services disable apikeys.googleapis.com bigquery.googleapis.com
        

  * `RESOURCE_TYPE`: the type of resource that you want to disable services for. Valid values are `project`, `folder`, and `organization`. You can omit this flag to disable services for the current project.

  * `RESOURCE_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders), or [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id), depending on the value you used for `RESOURCE_TYPE`. Or, omit the flag to default to the current project.




Supported flags:

  * `--async` to return immediately, without waiting for the operation in progress to complete.

  * `--bypass-api-usage-check` to bypass usage checks. Otherwise, the system returns an error if the service you want to disable was used in the last 30 days or enabled in the last 3 days.

  * You can specify _one_ of the following flags:

    * `--bypass-dependency-service-check` to bypass the check for dependencies; any enabled services that depend on the service you are disabling remain enabled.
    * `--disable-dependency-services` to proceed with disabling the service and any enabled services that depend on the service you are disabling.

You can inspect service dependencies. For more information, see [List service dependencies](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/list-dependencies).

  * `--force` to proceed even if there are enabled services that depend on the service, or the service was used in the last 30 days, or enabled in the last 3 days. Any dependent services are also disabled.

The `--bypass-api-usage-check`, `--bypass-dependency-service-check`, and `--disable-dependency-services` flags all take precedence over the `--force` flag.

Using both the `--disable-dependency-services` and `--bypass-api-usage-check` flags is equivalent to using the `--force` flag. The service and its dependencies are disabled without checking their usage.

  * `--validate-only` to validate the disablement without actually performing the operation.




## Examples

#### Enabling a service

  * Enabling BigQuery service without its dependencies: 
        
        gcloud beta services enable bigquery.googleapis.com --skip-dependency

Output:
        
        Operation [operations/ucpat.p39-581601899707-73a57d57-aa46-4d0b-a5ee-57034a42f2b3] complete. Result: {
              "@type":"type.googleapis.com/google.api.serviceusage.v2beta.ConsumerPolicy",
              "createTime":"2025-01-31T20:17:37.272343Z",
              "enableRules":[
                  {
                      "services":[
                          "services/apikeys.googleapis.com",
                          "services/compute.googleapis.com",
                          "services/oslogin.googleapis.com",
                          "services/serviceusage.googleapis.com",
                          "services/bigquery.googleapis.com"
                      ]
                  }
              ],
              "etag":"W/\"W9nsVJK0V1m7ee7tM7pFDg==\"",
              "name":"projects/PROJECT_ID/consumerPolicies/default",
              "updateTime":"2025-09-11T23:05:22.758394Z"
          }

  * Enabling BigQuery service with its dependencies: 
        
        gcloud beta services enable bigquery.googleapis.com

Output:
        
        Operation [operations/ucpat.p39-581601899707-73192b0f-053c-46ee-911a-7eca6b8fe899] complete. Result: {
              "@type":"type.googleapis.com/google.api.serviceusage.v2beta.ConsumerPolicy",
              "createTime":"2025-01-31T20:17:37.272343Z",
              "enableRules":[
                  {
                      "services":[
                          "services/apikeys.googleapis.com",
                          "services/compute.googleapis.com",
                          "services/oslogin.googleapis.com",
                          "services/serviceusage.googleapis.com",
                          "services/cloudresourcemanager.googleapis.com",
                          "services/dataplex.googleapis.com",
                          "services/bigquery.googleapis.com",
                          "services/bigquerystorage.googleapis.com",
                          "services/bigqueryconnection.googleapis.com",
                          "services/analyticshub.googleapis.com",
                          "services/bigquerymigration.googleapis.com",
                          "services/dataform.googleapis.com",
                          "services/bigquerydatapolicy.googleapis.com",
                          "services/bigquerydatatransfer.googleapis.com",
                          "services/bigqueryreservation.googleapis.com"
                      ]
                  }
              ],
              "etag":"W/\"FDXMAIdsBW7BrXjL7oP6FA==\"",
              "name":"projects/PROJECT_ID/consumerPolicies/default",
              "updateTime":"2025-09-12T19:44:23.675769Z"
          }




#### Disabling a service

  * Attempting to disable BigQuery service with active dependencies: 
        
        gcloud beta services disable bigquery.googleapis.com

Error message:
        
        ERROR: (gcloud.beta.services.disable) The services are depended on by the following active service(s) {"bigquery.googleapis.com": ["services/bigquerystorage.googleapis.com"]} . Please remove the active dependent services or provide the --disable-dependency-services flag to disable them, or --bypass-dependency-service-check to ignore this check.

  * Attempting to disable BigQuery service with recent usage: 
        
        gcloud beta services disable bigquery.googleapis.com --disable-dependency-services

Error message:
        
        ERROR: (gcloud.beta.services.disable) The operation "operations/ucpat.p39-581601899707-d35c2e2b-d2a3-47af-a1c0-033ed65df236" resulted in a failure "The services bigquery.googleapis.com,bigquerystorage.googleapis.com have usage in the last 30 days or were enabled in the past 3 days. Please specify force if you want to proceed with the destructive policy change.

  * Disabling BigQuery service and its dependencies and bypassing the usage check: 
        
        gcloud beta services disable bigquery.googleapis.com --disable-dependency-services --bypass-api-usage-check

Output:
        
        Operation [operations/ucpat.p39-581601899707-5c02aa04-7ad7-4eb6-a6a1-dc68653bcdb4] complete. Result: {
            "@type":"type.googleapis.com/google.api.serviceusage.v2beta.ConsumerPolicy",
            "createTime":"2025-01-31T20:17:37.272343Z",
            "enableRules":[
                {
                    "services":[
                        "services/analyticshub.googleapis.com",
                        "services/apikeys.googleapis.com",
                        "services/bigqueryconnection.googleapis.com",
                        "services/bigquerydatapolicy.googleapis.com",
                        "services/bigquerydatatransfer.googleapis.com",
                        "services/bigquerymigration.googleapis.com",
                        "services/bigqueryreservation.googleapis.com",
                        "services/cloudresourcemanager.googleapis.com",
                        "services/compute.googleapis.com",
                        "services/dataform.googleapis.com",
                        "services/dataplex.googleapis.com",
                        "services/oslogin.googleapis.com",
                        "services/serviceusage.googleapis.com"
                    ]
                }
            ],
            "etag":"W/\"TqbPaELDHlZQOj7As1P06g==\"",
            "name":"projects/PROJECT_ID/consumerPolicies/default",
            "updateTime":"2025-09-30T21:39:40.746125Z"
        }




## What's next

  * To manage policies, see [Manage consumer policies](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-consumer-policies).
  * To inspect service dependencies, see [List service dependencies](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/list-dependencies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
