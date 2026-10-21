---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites/
title: Prerequisites for using policy orchestrator \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:19.856874+00:00
---

# Prerequisites for using policy orchestrator  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Prerequisites for using policy orchestrator Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the prerequisites for using the policy orchestrator feature in VM Manager.

## gcloud CLI commands for policy orchestrator prerequisites

This section lists all `gcloud` commands that you need to run before you can use the policy orchestrator feature.

###  Project 

The following commands perform the tasks required to create project-level orchestrations:

  * Enable OS Config API for the project in which you create the OS policy orchestrator.
  * Enable Progressive Rollout API for the project in which you create the OS policy orchestrator.
  * Create required service agents, if these have not already been created.
  * Grant IAM roles to the service agents.


    
    
      # Enable OS Config API
      gcloud services enable osconfig.googleapis.com
    
      # Enable Progressive Rollout API
      gcloud services enable progressiverollout.googleapis.com
    
      # Create an OS config service agent
      gcloud beta services identity create --service=osconfig.googleapis.com  --project=PROJECT_NUMBER
    
      # Create a Progressive Rollout service agent
      gcloud beta services identity create --service=progressiverollout.googleapis.com  --project=PROJECT_NUMBER
    
      # Grant the required role to the OS config rollout service agent
      gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com" \
      --role="roles/osconfig.rolloutServiceAgent"
    
      # Grant the required role to the OS config service agent
      gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com" \
      --role="roles/osconfig.serviceAgent"
    
      # Grant the required role to the Progressive Rollout service agent
      gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-progrollout.iam.gserviceaccount.com" \
      --role="roles/progressiverollout.serviceAgent"
    

Replace the following:

  * `PROJECT_ID`: the numeric ID of the project in which you want to create the service agent.
  * `PROJECT_NUMBER`: the project resource number assigned by Google when you created the project.



For more information, see [The project resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects).

###  Folder 

The following commands perform the tasks required for creating folder-level orchestrations:

  * Set up a quota project.
  * Enable OS Config API for the project in which you create the OS policy orchestrator.
  * Create required service agents, if these have not already been created.
  * Grant IAM roles to the service agents.


    
    
      # Set up the quota project
      gcloud config set billing/quota_project QUOTA_PROJECT_ID
    
      # Enable OS Config API
      gcloud services enable osconfig.googleapis.com
    
      # Create an OS config service agent
      gcloud beta services identity create --service=osconfig.googleapis.com  --folder=FOLDER_NUMBER
    
      # Create a Progressive Rollout service agent
      gcloud beta services identity create --service=progressiverollout.googleapis.com  --folder=FOLDER_NUMBER
    
      # Grant the required role to the OS config rollout service agent
      gcloud resource-manager folders add-iam-policy-binding FOLDER_NUMBER \
      --member="serviceAccount:service-folder-FOLDER_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com" \
      --role="roles/osconfig.rolloutServiceAgent"
    
      # Grant the required role to the OS config service agent
      gcloud resource-manager folders add-iam-policy-binding FOLDER_NUMBER \
      --member="serviceAccount:service-folder-FOLDER_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com" \
      --role="roles/osconfig.serviceAgent"
    
      # Grant the required role to the Progressive Rollout service agent
      gcloud resource-manager folders add-iam-policy-binding FOLDER_NUMBER \
      --member="serviceAccount:service-folder-FOLDER_NUMBER@gcp-sa-progrollout.iam.gserviceaccount.com" \
      --role="roles/progressiverollout.serviceAgent"
      

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the quota project. You can choose any project with billing enabled.
  * `FOLDER_NUMBER`: the numeric ID of the folder in which you want to create the service agent.



###  Organization 

The following commands perform the tasks required for creating organization-level orchestrations:

  * Set up a quota project.
  * Enable OS Config API for the project in which you create the OS policy orchestrator.
  * Create required service agents, if these have not already been created.
  * Grant IAM roles to the service agents.


    
    
      # Set up the quota project
      gcloud config set billing/quota_project QUOTA_PROJECT_ID
    
      # Enable OS Config API
      gcloud services enable osconfig.googleapis.com
    
      # Create an OS config service agent
      gcloud beta services identity create --service=osconfig.googleapis.com --organization=ORGANIZATION_NUMBER
    
      # Create a Progressive Rollout service agent
      gcloud beta services identity create --service=progressiverollout.googleapis.com  --organization=ORGANIZATION_NUMBER
    
      # Grant the required role to the OS config rollout service agent
      gcloud organizations add-iam-policy-binding ORGANIZATION_NUMBER \
      --member="serviceAccount:service-org-ORGANIZATION_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com" \
      --role="roles/osconfig.rolloutServiceAgent"
    
      # Grant the required role to the OS config service agent
      gcloud organizations add-iam-policy-binding ORGANIZATION_NUMBER \
      --member="serviceAccount:service-org-ORGANIZATION_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com" \
      --role="roles/osconfig.serviceAgent"
    
      # Grant the required role to the Progressive Rollout service agent
      gcloud organizations add-iam-policy-binding ORGANIZATION_NUMBER \
      --member="serviceAccount:service-org-ORGANIZATION_NUMBER@gcp-sa-progrollout.iam.gserviceaccount.com" \
      --role="roles/progressiverollout.serviceAgent"
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the quota project. You can choose any project with billing enabled.
  * `ORGANIZATION_NUMBER` with the numeric ID of the organization in which you want to create the service agent.



## Set up a quota or billing project for organization and folder orchestrations

When you use policy orchestrators to manage OS policy resources in your organization or folders, you make requests to a [client-based API](https://docs.cloud.google.com/docs/quotas/quota-project#project-client-based). A _quota project_ is required for client-based APIs. For more information about client-based APIs and setting up quota projects, see [Quota project overview](https://docs.cloud.google.com/docs/quotas/quota-project).

When you use the gcloud CLI or REST API to call the policy orchestrator methods, specify the quota project as follows:

**Note:** For the quota project, you can use any project that has [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project).

###  gcloud 

Set your quota project in your gcloud CLI configuration property:
    
    
    gcloud config set billing/quota_project QUOTA_PROJECT_ID
    

Replace `QUOTA_PROJECT_ID` with the project ID of the quota project.

Alternatively, set the quota project for a specific command by using the `--billing-project` flag, which takes precedence over the configuration property.

###  REST 

Add the `x-goog-user-project` HTTP header to specify a quota project in each request. For details, see [Set the quota project with a REST request](https://docs.cloud.google.com/docs/quotas/set-quota-project#rest_request).

## Enable OS Config API

To use the policy orchestrator feature in VM Manager, enable OS Config API in the following projects:

  * For organization-level and folder-level orchestrations, enable the OS Config API for the quota project.
  * For project-level orchestrations, enable the OS Config API in the project where you create policy orchestrators.



For more information, see [Enable OS Config API](https://docs.cloud.google.com/compute/vm-manager/docs/setup#enable-service-api).

## Enable Progressive Rollout API for the projects

**Note:** This step is required only for project-level orchestrations.

###  Console 

  1. In the Google Cloud console, select the Google Cloud project for which you want to enable the API, and then go to the **APIs & Services** page:

[Go to **APIs & Services**](https://console.cloud.google.com/apis/dashboard)

  2. Click **Enable APIs and Services**.

  3. Search for "Progressive Rollout".

  4. In the search results, click **Progressive Rollout API**.

  5. If the API is not already enabled, then click **Enable**.




###  gcloud 

  1. To see if the Progressive Rollout API is enabled, list the enabled services for your project:
         
         gcloud services list --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project for which you want to enable the API.

If `progressiverollout.googleapis.com` appears in the output, the API is enabled.

  2. If the API is not enabled, then run the following command to enable it:
         
         gcloud services enable progressiverollout.googleapis.com
         

For more information, see [`gcloud services`](https://docs.cloud.google.com/sdk/gcloud/reference/services).




## Set up the OS Config service agents

The policy orchestrator uses the OS Config service agents to perform actions in your projects. It also depends on the Progressive Rollout API, which has its own service agents. For more information, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents).

You must create the service agents for each project, folder, or organization in which you create the policy orchestrator. For the policy orchestrator to function properly, grant the following required IAM roles to these service agents at the parent resource of the orchestrator:

  * OSConfig Service Agent (`roles/osconfig.serviceAgent`) for the @gcp-sa-osconfig.iam.gserviceaccount.com account
  * OSConfig Rollout Service Agent (`roles/osconfig.rolloutServiceAgent`) for the @gcp-sa-osconfig-rollout.iam.gserviceaccount.com account
  * Progressiverollout Service Agent (`roles/progressiverollout.serviceAgent`) for the @gcp-sa-progrollout.iam.gserviceaccount.com account



To grant IAM roles to the service agents, use the Google Cloud console or the [`add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding). For more information, see [Grant a role to the service agent](https://docs.cloud.google.com/iam/docs/create-service-agents#grant-role).

### Required roles

  * To get the permissions that you need to grant the service agents access, ask your administrator to grant you the following IAM roles on the project, folder, or organization that you're granting access to: 

    * Grant service agents access to a project: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
    * Grant service agents access to a folder: [Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`) 
    * Grant service agents access to projects, folders, and organizations: [Organization Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to grant the service agents access. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to grant the service agents access:

    * Grant service agents access to a project: 
      * `resourcemanager.projects.getIamPolicy`
      * `resourcemanager.projects.setIamPolicy`
    * Grant service agents access to a folder: 
      * `resourcemanager.folders.getIamPolicy`
      * `resourcemanager.folders.setIamPolicy`
    * Grant service agents access to an organization: 
      * `resourcemanager.organizations.getIamPolicy`
      * `resourcemanager.organizations.setIamPolicy`

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




To create the service agents, do the following.

  1. Review the format of the service agent email address for each resource:

###  Project 

     * `service-PROJECT_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com`
     * `service-PROJECT_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com`
     * `service-PROJECT_NUMBER@gcp-sa-progrollout.iam.gserviceaccount.com`

Replace `PROJECT_NUMBER` with the numeric ID of the project where you create the policy orchestrators.

###  Folder 

     * `service-folder-FOLDER_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com`
     * `service-folder-FOLDER_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com`
     * `service-folder-FOLDER_NUMBER@gcp-sa-progrollout.iam.gserviceaccount.com`

Replace `FOLDER_NUMBER` with the numeric ID of the folder where you create the policy orchestrators.

###  Organization 

     * `service-org-ORGANIZATION_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com`
     * `service-org-ORGANIZATION_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com`
     * `service-org-ORGANIZATION_NUMBER@gcp-sa-progrollout.iam.gserviceaccount.com`

Replace `ORGANIZATION_NUMBER` with the numeric ID of the organization in which you create the policy orchestrators.

  2. To create the service agent for a specified API and resource, use the [`gcloud beta services identity create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/identity/create):

###  Project 
         
         # Create an OS config service agent
         gcloud beta services identity create --service=osconfig.googleapis.com  --project=PROJECT_NUMBER
         
         # Create a Progressive Rollout service agent
         gcloud beta services identity create --service=progressiverollout.googleapis.com  --project=PROJECT_NUMBER
         

Replace `PROJECT_NUMBER` with the numeric ID of the project in which you want to create the service agent.

###  Folder 
         
         # Create an OS config service agent
         gcloud beta services identity create --service=osconfig.googleapis.com  --folder=FOLDER_NUMBER
         
         # Create a Progressive Rollout service agent
         gcloud beta services identity create --service=progressiverollout.googleapis.com  --folder=FOLDER_NUMBER
         

Replace `FOLDER_NUMBER` with the numeric ID of the folder in which you want to create the service agent.

###  Organization 
         
         # Create an OS config service agent
         gcloud beta services identity create --service=osconfig.googleapis.com --organization=ORGANIZATION_NUMBER
         
         # Create a Progressive Rollout service agent
         gcloud beta services identity create --service=progressiverollout.googleapis.com  --organization=ORGANIZATION_NUMBER
         

Replace `ORGANIZATION_NUMBER` with the numeric ID of the organization in which you want to create the service agent.




## Grant IAM roles to the service agents

To grant the service agent roles, run the `gcloud add-iam-policy-binding` as follows:

###  Project 
    
    
    # Grant the required role to the OS config rollout service agent
     gcloud projects add-iam-policy-binding PROJECT_ID \
     --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com" \
     --role="roles/osconfig.rolloutServiceAgent"
    
     # Grant the required role to the OS config service agent
     gcloud projects add-iam-policy-binding PROJECT_ID \
     --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com" \
     --role="roles/osconfig.serviceAgent"
    
     # Grant the required role to the Progressive Rollout service agent
     gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-progrollout.iam.gserviceaccount.com" \
    --role="roles/progressiverollout.serviceAgent"
    

Replace the `PROJECT_NUMBER` with the numeric ID of the project to which the IAM policy binding is being added.

###  Folder 
    
    
    # Grant the required role to the OS config rollout service agent
    gcloud resource-manager folders add-iam-policy-binding FOLDER_NUMBER \
     --member="serviceAccount:service-folder-FOLDER_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com" \
     --role="roles/osconfig.rolloutServiceAgent"
    
    # Grant the required role to the OS config service agent
    gcloud resource-manager folders add-iam-policy-binding FOLDER_NUMBER \
     --member="serviceAccount:service-folder-FOLDER_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com" \
     --role="roles/osconfig.serviceAgent"
    
    # Grant the required role to the Progressive Rollout service agent
    gcloud resource-manager folders add-iam-policy-binding FOLDER_NUMBER \
    --member="serviceAccount:service-folder-FOLDER_NUMBER@gcp-sa-progrollout.iam.gserviceaccount.com" \
    --role="roles/progressiverollout.serviceAgent"
    

Replace the `FOLDER_NUMBER` with the numeric ID of the folder to which the IAM policy binding is being added.

###  Organization 
    
    
    # Grant the required role to the OS config rollout service agent
    gcloud organizations add-iam-policy-binding ORGANIZATION_NUMBER \
     --member="serviceAccount:service-org-ORGANIZATION_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com" \
     --role="roles/osconfig.rolloutServiceAgent"
    
     # Grant the required role to the OS config service agent
     gcloud organizations add-iam-policy-binding ORGANIZATION_NUMBER \
     --member="serviceAccount:service-org-ORGANIZATION_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com" \
     --role="roles/osconfig.serviceAgent"
    
     # Grant the required role to the Progressive Rollout service agent
     gcloud organizations add-iam-policy-binding ORGANIZATION_NUMBER \
    --member="serviceAccount:service-org-ORGANIZATION_NUMBER@gcp-sa-progrollout.iam.gserviceaccount.com" \
    --role="roles/progressiverollout.serviceAgent"
    

Replace the `ORGANIZATION_NUMBER` with the numeric ID of the organization to which the IAM policy binding is being added.

## Configure access for projects in VPC Service Controls perimeters

If you use organization-level or folder-level policy orchestrators in projects protected by VPC Service Controls, then you must grant the OSConfig Rollout service agent access to the VPC Service Controls service perimeter. If you don't grant this access, then policy orchestrator fails to create, update, or delete OS policy assignments for these projects.

### Required roles

To get the permissions that you need to configure OS policy orchestrators for use within VPC Service Controls perimeters, ask your administrator to grant you the [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to configure OS policy orchestrators for use within VPC Service Controls perimeters. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure OS policy orchestrators for use within VPC Service Controls perimeters:

  * Grant service agents access to a project: 
    * `resourcemanager.projects.getIamPolicy`
    * `resourcemanager.projects.setIamPolicy`
  * Grant service agents access to a folder: 
    * `resourcemanager.folders.getIamPolicy`
    * `resourcemanager.folders.setIamPolicy`
  * Grant service agents access to an organization: 
    * `resourcemanager.organizations.getIamPolicy`
    * `resourcemanager.organizations.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Create the ingress rules

To let the service agent access resources protected by VPC Service Controls, add an ingress rule to the relevant service perimeter.

For more information about how to create ingress rules, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

### Folder

### Console

  1. In the Google Cloud console, go to the **VPC Service Controls** page. 

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. Select your organization.
  3. On the **VPC Service Controls** page, select the access policy that contains the service perimeter that you want to update.
  4. Click the name of the service perimeter that you want to update, and then click **Edit**.
  5. Click **Ingress policy**.
  6. Click **Add an ingress rule**.
  7. In the **From** section, specify the identity for the service agent: 
     1. For **Identities** > **Identity** , select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address that identifies the following OSconfig rollout service agent: 

`service-folder-FOLDER_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com`

Replace `FOLDER_NUMBER` with the numeric ID of the folder.

  8. In the **To** section, specify the allowed operations: 
     1. For **Resources** > **Projects** , select **All projects**.
     2. For **Operations or IAM roles** , select **Select operations**.
     3. Click **Add operations** , and then add the following operation: 
        1. Add the `osconfig.googleapis.com` service.
        2. Click **All methods**.
  9. Click **Done**.
  10. Click **Save**.



### gcloud

To add the ingress rule, create a YAML file that contains the ingress rule and use the [`gcloud access-context-manager perimeters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update) with the `--set-ingress-policies` flag.

  1. Create an ingress policy YAML file named `ingress_policy.yaml` with the following contents:
         
         - ingressFrom:
              identities:
              - serviceAccount:service-folder-FOLDER_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com
              sources:
              - accessLevel: '*'
            ingressTo:
              operations:
              - serviceName: osconfig.googleapis.com
                methodSelectors:
                - method: "*"
              resources:
              - "*"
         

Replace `FOLDER_NUMBER` with the numeric ID of the folder.

  2. Add the ingress policy to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
            --set-ingress-policies=ingress_policy.yaml
         

Replace `PERIMETER_NAME` with the name of your service perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`.




### Organization

### Console

  1. In the Google Cloud console, go to the **VPC Service Controls** page. 

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. Select your organization.
  3. On the **VPC Service Controls** page, select the access policy that contains the service perimeter that you want to update.
  4. Click the name of the service perimeter that you want to update, and then click **Edit**.
  5. Click **Ingress policy**.
  6. Click **Add an ingress rule**.
  7. In the **From** section, specify the identity for the service agent: 
     1. For **Identities** > **Identity** , select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address that identifies the following OSconfig rollout service agent: 

`service-org-ORGANIZATION_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com`

Replace `ORGANIZATION_NUMBER` with the numeric ID of the organization.

  8. In the **To** section, specify the allowed operations: 
     1. For **Resources** > **Projects** , select **All projects**.
     2. For **Operations or IAM roles** , select **Select operations**.
     3. Click **Add operations** , and then add the following operation: 
        1. Add the `osconfig.googleapis.com` service.
        2. Click **All methods**.
  9. Click **Done**.
  10. Click **Save**.



### gcloud

To add the ingress rule, create a YAML file that contains the ingress rule and use the [`gcloud access-context-manager perimeters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update) with the `--set-ingress-policies` flag.

  1. Create an ingress policy YAML file named `ingress_policy.yaml` with the following contents:
         
         - ingressFrom:
              identities:
              - serviceAccount:service-org-ORGANIZATION_NUMBER@gcp-sa-osconfig-rollout.iam.gserviceaccount.com
              sources:
              - accessLevel: '*'
            ingressTo:
              operations:
              - serviceName: osconfig.googleapis.com
                methodSelectors:
                - method: "*"
              resources:
              - "*"
         

Replace `ORGANIZATION_NUMBER` with the numeric ID of the organization.

  2. Add the ingress policy to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
           --set-ingress-policies=ingress_policy.yaml
         

Replace `PERIMETER_NAME` with the name of your service perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`.




## What's next?

  * Learn how to [manage OS policy assignments using policy orchestrator](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/use-policy-orchestrator).
  * Learn how to [view and edit policy orchestrators](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/view-edit-policy-orchestrator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
