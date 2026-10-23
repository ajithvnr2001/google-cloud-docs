---
url: https://docs.cloud.google.com/infrastructure-manager/docs/deploy-vpc-with-terraform/
title: Quickstart: Deploy a VPC with Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:17.251279+00:00
---

# Quickstart: Deploy a VPC with Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/deploy-vpc-with-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy a VPC with Terraform

Learn how to use Infrastructure Manager to deploy a Virtual Private Cloud (VPC).

This quickstart uses a Terraform configuration that is stored in a public GitHub repository. The configuration defines the VPC to provision.

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

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

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Infrastructure Manager API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable config.googleapis.com

  8. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant the `roles/config.agent` IAM role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=roles/config.agent

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Infrastructure Manager API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable config.googleapis.com

  15. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant the `roles/config.agent` IAM role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=roles/config.agent

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 




## Grant permissions for resources in the configuration

You have granted permissions needed to run Infra Manager, but you also need to grant permissions that are specific to the resources described in the configuration you are deploying.

Grant permissions for the VPC, which is the resource defined in the Terraform configuration.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --role=roles/compute.networkAdmin
    

Replace the following:

  * SERVICE_ACCOUNT_NAME: the name of the service account.
  * PROJECT_ID: your project ID.



## Preview the deployment

Before you create a deployment, you can create a preview of the deployment. You can use this preview to verify the resources that are planned to be provisioned.

The following command has four values populated that don't have a default value. These values are: your project ID, the service account name, the location `us-central1`, and the name `quickstart-vpc` for the network you're creating.

To create a preview, use the following command:
    
    
        gcloud infra-manager previews create projects/PROJECT_ID/locations/us-central1/previews/quickstart-preview \
            --service-account projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
            --git-source-repo=https://github.com/terraform-google-modules/terraform-google-network \
            --git-source-directory=modules/vpc \
            --git-source-ref=main \
            --input-values=project_id=PROJECT_ID,network_name=quickstart-vpc
    

After you create a preview, you can review the preview results. This quickstart skips this step, but you can see [Export and view preview results](https://docs.cloud.google.com/infrastructure-manager/docs/export-view-preview-results) if you want more details.

## Create a deployment

Use Infra Manager to create a deployment. This means that Infra Manager provisions the resources that are defined in the Terraform configuration.

The configuration for this quickstart has four values that don't have a default value. The following command adds these values: your project ID, the service account name, the location `us-central1`, and the name `quickstart-vpc` for the network you're creating.
    
    
    gcloud infra-manager deployments apply projects/PROJECT_ID/locations/us-central1/deployments/quickstart-deployment \
        --service-account=projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --git-source-repo=https://github.com/terraform-google-modules/terraform-google-network \
        --git-source-directory=modules/vpc \
        --git-source-ref=main \
        --input-values=project_id=PROJECT_ID,network_name=quickstart-vpc
    

When the deployment is done, you see:
    
    
    Creating the deployment...done
    

The VPC is now created and configured as described in the configuration.

## View the build results in Cloud Build

To view the Cloud Build job that Infra Manager used to create the deployment, open the **Build History** page in the Google Cloud console:

[Open the Build History page](https://console.cloud.google.com/cloud-build/builds)

## View the status of the deployment

Now that the deployment is done, you can view its description to review information about it, including the state.

View the description of the deployment:
    
    
    gcloud infra-manager deployments describe projects/PROJECT_ID/locations/us-central1/deployments/quickstart-deployment
    

The output has details about the deployment, including the timestamp of the deployment, the name of the latest revision, and the state.

For the state, you see `ACTIVE`.

## View details about the provisioned VPC

View details about the provisioned VPC:
    
    
    gcloud infra-manager resources list --revision=projects/PROJECT_ID/locations/us-central1/deployments/quickstart-deployment/revisions/REVISION_ID
    

Replace REVISION_ID with the ID of the latest revision. This ID is `r-0`, unless you deployed multiple times. You can see the ID of the latest revision in the deployment description in the previous section.

## View the VPC in the console

View the VPC in the console:

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

You see the VPC named `quickstart-vpc`. This is the VPC that Infra Manager provisioned.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, make sure that you delete resources that you no longer need.

### Delete the VPC

Delete the VPC and the metadata about the deployment:
    
    
    gcloud infra-manager deployments delete projects/PROJECT_ID/locations/us-central1/deployments/quickstart-deployment
    

### Optional: Delete the project

If you deployed the solution in a new Google Cloud project, and if you no longer the project, then delete it by completing the following steps:

**Caution:** If you delete a project, all the resources in the project are permanently deleted.

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. At the prompt, type the project ID, and then click **Shut down**. 



## What's next

  * To learn more about Infra Manager, see [How Infra Manager works](https://docs.cloud.google.com/infrastructure-manager/docs/overview#how_works).
  * Learn more about [Infra Manager and Terraform](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform).
  * [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).
  * [Automate deployments](https://docs.cloud.google.com/infrastructure-manager/docs/automate-git).
  * For a set of configurations and modules ready to use with Google Cloud, see [Terraform blueprints and modules for Google Cloud](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
