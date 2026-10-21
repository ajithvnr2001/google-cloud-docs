---
url: https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-consumer-policies/
title: Manage consumer policies \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:36.321080+00:00
---

# Manage consumer policies  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-consumer-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ Guides ](https://docs.cloud.google.com/service-usage/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage consumer policies

**Preview — Hierarchical service activation**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Hierarchical service activation lets you manage service enablement that is inherited through the Google Cloud resource hierarchy. For more information, see the [overview](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/overview).

The `ConsumerPolicy` is a Service Usage API resource found at each level of the Google Cloud resource hierarchy. This resource, always named `default`, contains the `enableRules` that define which services are enabled. Instead of enabling or disabling a specific service, you can modify the `ConsumerPolicy` resource. When a service name is in its list, the service is enabled at that hierarchy level.

This document shows you how to use the Google Cloud CLI to manage consumer policies for projects, folders, and organizations.

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

  12. If you don't indicate the Google Cloud resource that you want to manage, the commands in this document default to the current project. For example, `gcloud beta services policies get --policy-name=default` returns the consumer policy for the current project. 

You can retrieve the current project ID:
         
         gcloud config list --format='text(core.project)'




### Required roles

To get the permissions that you need to manage consumer policies, ask your administrator to grant you the [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) IAM role on your target resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to manage consumer policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage consumer policies:

  * Get a consumer policy: `serviceusage.consumerpolicy.get`
  * Update a consumer policy: 
    * `serviceusage.consumerpolicy.analyze`
    * `serviceusage.consumerpolicy.update`
  * Get an effective policy: `serviceusage.effectivepolicy.get`
  * Check if a service is enabled: `serviceusage.values.test`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Get a consumer policy

You can retrieve the `ConsumerPolicy` for a project, folder, or organization by using the [`gcloud beta services policies get`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/policies/get) command.

This command returns the `enableRules` set at that exact resource level, and not inherited rules. For a more complete view that includes inherited rules, you can retrieve the effective policy. Only the `default` policy name is supported.
    
    
    gcloud beta services policies get --policy-name=default \
        --RESOURCE_TYPE=RESOURCE_ID \
        --output-file=OUTPUT_FILE
    

Replace the following:

  * `RESOURCE_TYPE`: the type of resource that you want to get the consumer policy for. Valid values are `project`, `folder`, and `organization`. You can omit this flag to return the consumer policy for the current project.

  * `RESOURCE_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders), or [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id), depending on the value you used for `RESOURCE_TYPE`.

  * `OUTPUT_FILE`: (optional) the path to an output file where the contents of the consumer policy can be saved. Supported file formats are JSON and YAML.




## Update a consumer policy

You can update a `ConsumerPolicy` by using the [`gcloud beta services policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/policies/update) command. This lets you replace the current policy and use a YAML file to update many enabled services at once.

This command doesn't automatically enable [service dependencies](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/overview#service_dependencies). You must list all service dependencies explicitly in the input file. You can use the `--validate-only` flag to preview changes before applying them.
    
    
    gcloud beta services policies update --consumer-policy-file=PATH_TO_CONSUMER_POLICY
    

Replace `PATH_TO_CONSUMER_POLICY` with the path to the YAML file that contains the consumer policy—for example:

`gcloud beta services policies update --consumer-policy-file=/path/to/the/file.yaml`

Supported flags:

  * `--bypass-api-usage-check` to bypass usage checks. Otherwise, the system returns an error if any service you want to disable was used in the last 30 days or enabled in the last 3 days.

  * `--bypass-dependency-check` to bypass the check for dependencies. When adding a service, all service dependencies must be present in the policy. When removing a service, no other services in the policy can depend on it. Otherwise, the update doesn't succeed and an error is returned.

  * `--validate-only` to validate the update without actually performing the operation.




Note the following:

  * To get a YAML template for the policy file, first retrieve the consumer policy and use the `--output-file` flag to save the policy to a file. Then, modify this file and use it as input for the update command. Sample template:
        
        name: projects/PROJECT_ID/consumerPolicies/default
        enableRules:
          - services:
            - services/SERVICE
            - ...
            - ...
        

Replace the following:

    * `PROJECT_ID`: your [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). Other supported resource names follow a similar format—for example: `folders/FOLDER_ID/consumerPolicies/default`.

    * `SERVICE`: the name of the service—for example: `bigquery.googleapis.com`.




## Get an effective policy

You can retrieve the effective policy for a resource by using the [`gcloud beta services policies get-effective`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/policies/get-effective) command.

The effective policy combines the resource's `ConsumerPolicy` with the policies of all its ancestors. This gives you a complete view of all enabled services, including all services enabled directly on the resource, and those inherited from its ancestors.
    
    
    gcloud beta services policies get-effective \
        --RESOURCE_TYPE=RESOURCE_ID \
        --view=VIEW
    

Replace the following:

  * `RESOURCE_TYPE`: the type of resource that you want to get the effective policy for. Valid values are `project`, `folder`, and `organization`. You can omit this flag to return the effective policy for the current project.

  * `RESOURCE_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders), or [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id), depending on the value you used for `RESOURCE_TYPE`.

  * `VIEW`: either `BASIC` to retrieve a limited set of metadata or `FULL` to retrieve the full set of metadata, including where each service was enabled in the hierarchy. Default is `BASIC`.




## Check if a service is enabled

You can check if a service is enabled on a resource by using the [`gcloud beta services policies test-enabled`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/policies/test-enabled) command.

When checking the status of a service, this command considers the effective policy and the full Google Cloud resource hierarchy.
    
    
    gcloud beta services policies test-enabled SERVICE \
        --RESOURCE_TYPE=RESOURCE_ID
    

Replace the following:

  * `SERVICE`: the name of the service you want to check.

  * `RESOURCE_TYPE`: the type of resource that you want to check. Valid values are `project`, `folder`, and `organization`. You can omit this flag to check the status for the current project.

  * `RESOURCE_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders), or [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id), depending on the value you used for `RESOURCE_TYPE`.




## Examples

#### Retrieving consumer policy

  * Retrieving consumer policy for current project: 
        
        gcloud beta services policies get

Output:
        
        name: projects/PROJECT_ID/consumerPolicies/default
        enableRules:
         services:
          - services/apikeys.googleapis.com
          - services/compute.googleapis.com
          - services/oslogin.googleapis.com
          - services/serviceusage.googleapis.com
        updateTime: 2025-09-11T23:05:22.758394Z
        createTime: 2025-01-31T20:17:37.272343Z
        etag: W/"W9nsVJK0V1m7ee7tM7pFDg=="




#### Updating consumer policy

  * Successfully updating consumer policy: 
        
        gcloud beta services policies update --consumer-policy-file=/tmp/test.yaml

Output:
        
        Operation [operations/ucpat.p39-581601899707-86fe7e37-c7f9-4624-90c4-d54754d57eed] complete. Result: {
            "@type":"type.googleapis.com/google.api.serviceusage.v2beta.ConsumerPolicy",
            "createTime":"1970-01-01T00:00:00Z",
            "enableRules":[
                {
                    "services":[
                        "services/apikeys.googleapis.com"
                    ]
                }
            ],
            "name":"projects/PROJECT_ID/consumerPolicies/default",
            "updateTime":"1970-01-01T00:00:00Z"
        }

  * Unsuccessfully updating consumer policy: 
        
        gcloud beta services policies update --consumer-policy-file=/tmp/test.json

Error message:
        
        ERROR: (gcloud.beta.services.policies.update) Invalid consumer_policy_file format. Please provide path to a yaml file.

  * Attempting to update consumer policy when service has been used or enabled recently: 
        
        gcloud beta services policies update --consumer-policy-file=/tmp/test.yaml

Output:
        
        The operation "operations/ucpat.p39-581601899707-4884bdb0-d899-49ac-9c83-38457950ef33" resulted in a failure "The services apikeys.googleapis.com have usage in the last 30 days or were enabled in the past 3 days. Please specify force if you want to proceed with the destructive policy change. Help Token: AVSZLmtCfGwMm4oHmOyExdDEFRQ0pFiBrl879nbZlY2JkfVzeU63u66ApXYr6MIEAoig..."

  * Updating consumer policy when service has been used or enabled recently by bypassing usage check: 
        
        gcloud beta services policies update --consumer-policy-file=/tmp/test.yaml --bypass-api-usage-check

Output:
        
        Operation [operations/ucpat.p39-581601899707-8ffda670-ed04-4776-8d43-d2f8e1817e00] complete. Result: {
            "@type":"type.googleapis.com/google.api.serviceusage.v2beta.ConsumerPolicy",
            "createTime":"1970-01-01T00:00:00Z",
            "enableRules":[
                {
                    "services":[
                        "services/serviceusage.googleapis.com"
                    ]
                }
            ],
            "name":"projects/PROJECT_ID/consumerPolicies/default",
            "updateTime":"1970-01-01T00:00:00Z"
        }




#### Retrieving effective policy

  * Retrieving `BASIC` view of the effective policy for current project: 
        
        gcloud beta services policies get-effective

Output:
        
        EnabledRules:
         Services:
          -   services/apikeys.googleapis.com
          -   services/compute.googleapis.com
          -   services/computescanning.googleapis.com
          -   services/containeranalysis.googleapis.com
          -   services/containerscanning.googleapis.com
          -   services/gkebackup.googleapis.com
          -   services/osconfig.googleapis.com
          -   services/oslogin.googleapis.com
          -   services/serviceusage.googleapis.com

  * Retrieving `FULL` view of the effective policy for current project: 
        
        gcloud beta services policies get-effective --view=FULL

Output:
        
        EnabledRules:
         Services:
          -   services/apikeys.googleapis.com
          -   services/compute.googleapis.com
          -   services/computescanning.googleapis.com
          -   services/containeranalysis.googleapis.com
          -   services/containerscanning.googleapis.com
          -   services/gkebackup.googleapis.com
          -   services/osconfig.googleapis.com
          -   services/oslogin.googleapis.com
          -   services/serviceusage.googleapis.com
        
        Metadata of effective policy:
        EnabledService: services/apikeys.googleapis.com
        EnabledPolicies: ['projects/PROJECT_ID/consumerPolicies/default']
        
        EnabledService: services/bcidcloudenforcer-pa.googleapis.com
        EnabledPolicies: ['folders/FOLDER_ID/consumerPolicies/default']
        
        EnabledService: services/compute.googleapis.com
        EnabledPolicies: ['projects/PROJECT_ID/consumerPolicies/default']
        ...




#### Checking if a service is enabled

  * Checking the status of enabled API keys service for current project: 
        
        gcloud beta services policies test-enabled apikeys.googleapis.com

Output:
        
        Service apikeys.googleapis.com is ENABLED for resource projects/test-project.

  * Checking the status of disabled App Hub service for current project: 
        
        gcloud beta services policies test-enabled apphub.googleapis.com

Output:
        
        Service apphub.googleapis.com is NOT ENABLED for resource projects/test-project.




## What's next

  * To enable and disable services, see [Manage service enablement](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-enablement).
  * To inspect service dependencies, see [List service dependencies](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/list-dependencies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
