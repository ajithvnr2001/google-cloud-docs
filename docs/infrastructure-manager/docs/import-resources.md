---
url: https://docs.cloud.google.com/infrastructure-manager/docs/import-resources/
title: Import deployed resources into Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:46.569709+00:00
---

# Import deployed resources into Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/import-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Import deployed resources into Infrastructure Manager Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates how to import Google Cloud resources into a Infrastructure Manager deployment. You can only import resources that were provisioned using Terraform. 

If you have a Terraform configuration and have not yet deployed it on Google Cloud, then see [deploy infrastructure using Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).

This tutorial begins with deploying a Virtual Private Cloud (VPC) onto Google Cloud using the Terraform CLI. Then, this tutorial demonstrates how to import these deployed resources into Infrastructure Manager so that the resources can be managed as an Infrastructure Manager deployment.

You can use the example in this tutorial to understand how to import other Google Cloud resources into Infra Manager. To import the deployment into Infra Manager, the Terraform configuration used to provision the resources does need to comply with the [constraints](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#constraints), and the resources need to have been provisioned using a [supported Terraform version](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions).

## Costs

This tutorial uses the following billable components of Google Cloud:

  * [Infrastructure Manager](https://cloud.google.com/infrastructure-manager/pricing)
  * [Virtual Private Cloud (VPC)](https://cloud.google.com/vpc/pricing)



## Before you begin

**Note:** If you're using this tutorial to understand how to import other deployments into Infra Manager, ensure that the Terraform configuration you used to provision the resources the complies with the [constraints](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#constraints), and that the resources were provisioned using a [supported Terraform version](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions).

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

  16. Install a [supported version](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions) of [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli). 



## Deploy resources to Google Cloud

The Google Cloud resource that you deploy in this tutorial is a VPC. This section shows you how to deploy the resource to use as an example for importing deployed resources into Infra Manager.

This tutorial uses the `us-central1` region. If you want to use another region, then you can use any of the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.

### Grant permissions for resources in the configuration

You have granted permissions needed to run Infra Manager, but you also need to grant permissions that are specific to the resources described in the configuration you are deploying.

Grant permissions to be able to create the VPC network, which is the resource defined in the Terraform configuration:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --role=roles/compute.networkAdmin
    

Replace the following:

  * SERVICE_ACCOUNT_NAME: the name of the service account.
  * PROJECT_ID: your project ID.



### Deploy resources using the Terraform CLI

  1. Create a VPC network using the following Terraform configuration. To do so, run the following command:
         
         mkdir vpc_to_import
         cd vpc_to_import
         cat <<EOF > main.tf
         variable "project_id" {
           type = string
         }
         
         resource "google_compute_network" "vpc_network" {
           name = "my-custom-mode-network"
           project = var.project_id
         }
         EOF
         

  2. Deploy the configuration using the Terraform CLI using the following command:
         
         terraform init
         echo "**************  TERRAFORM APPLY  ******************"
         terraform apply -var="project_id=PROJECT_ID" -auto-approve
         cd ..
         




When the VPC is provisioned, you see output that begins with the text `Creation complete`.

The VPC that is defined in the Terraform configuration is now deployed on Google Cloud. Terraform creats a state file, and this file is on the file system next to the `main.tf` file.

## Create a placeholder deployment in Infrastructure Manager

To import resources into Infra Manager, you need an existing deployment in Infra Manager.

This tutorial uses a storage bucket to store the Terraform configuration. If you are using this tutorial to understand how to import other deployments into Infra Manager, then you can store the Terraform configuration in a storage bucket, public Git repository, or on your local machine.

  1. Add an empty Terraform configuration to the storage bucket:
         
         gcloud storage buckets create gs://import-deployment-configuration --project=PROJECT_ID
         
         mkdir placeholder_deployment
         cd placeholder_deployment
         cat <<EOF > main.tf
         EOF
         
         gcloud storage cp main.tf gs://import-deployment-configuration
         cd ..
         

  2. Create a deployment using Infra Manager.
         
         gcloud infra-manager deployments apply projects/PROJECT_ID/locations/us-central1/deployments/import-deployment \
         --gcs-source gs://import-deployment-configuration \
         --input-values project_id=PROJECT_ID \
         --service-account projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT
         

When the deployment is done, you see:
         
         Creating the deployment...done
         




You now have an Infra Manager deployment. Next, you need to add the state file and Terraform configuration to this deployment so that this deployment manages the VPC.

## Import the state file and Terraform configuration

To manage the deployed resource (the VPC) using Infra Manager, you need to add the state file and the Terraform configuration to Infra Manager.

### Lock the deployment

Lock the Infra Manager deployment so you can make changes to its state.
    
    
    LOCK_ID=$(gcloud infra-manager deployments lock projects/PROJECT_ID/locations/us-central1/deployments/import-deployment --format="get(lockId)")
    

### Import the Terraform state file into Infra Manager

Import the state file for your deployed resources. This state file was created by Terraform when you deployed the VPC using the Terraform CLI.

Upload the Terraform state file to the Infra Manager deployment.
    
    
    SIGNED_STATE_UPLOAD_URL=$(gcloud infra-manager deployments import-statefile projects/PROJECT_ID/locations/us-central1/deployments/import-deployment --lock-id ${LOCK_ID} --format="get(signedUri)")
    cd vpc_to_import
    curl -s -X PUT --upload-file terraform.tfstate $SIGNED_STATE_UPLOAD_URL
    

### Upload the Terraform configuration to the Cloud Storage bucket

Now that you have uploaded the Terraform state file, you also need to upload the Terraform configuration that you used to create the VPC network. Infra Manager needs the Terraform state file so that when a Infra Manager preview is run, it doesn't find any changes to the resources.

Upload the Terraform configuration to Cloud Storage using the following command:
    
    
    gcloud storage cp main.tf gs://import-deployment-configuration
    

### Unlock the deployment

If you are using this tutorial to understand how to import any resources into Infra Manager, ensure that the state file and Terraform configuration don't have differences. If there are differences between the state file and the Terraform configuration, then ensure that the state file describes the resources that you want deployed. When you unlock the deployment, if there are differences between the state file and Terraform configuration, then when you unlock the deployment Infra Manager creates or deletes resources to match the state file.

**Caution:** Deleting Google Cloud resources can cause unrecoverable data loss. Re-deploying the configuration won't restore data.

You need to unlock the deployment to be able to manage the resources using Infra Manager. In this tutorial, the state file and Terraform configuration describe the same configuration, and so Infra Manager doesn't create or delete any resources.

Release the lock from the deployment by running the following.
    
    
    gcloud infra-manager deployments unlock projects/PROJECT_ID/locations/us-central1/deployments/import-deployment \
    --project PROJECT_ID \
    --location us-central1 \
    --lock-id ${LOCK_ID}
    

Now that the state file and Terraform configuration are added to your Infra Manager deployment, you have finished importing the deployed resources. The deployed VPC is now managed by Infra Manager.

## Preview resource changes

Run a preview on the deployment to confirm that the Terraform state and the resources deployed on Google Cloud are in sync.

  1. Create a preview using the following command:
         
         gcloud infra-manager previews create projects/PROJECT_ID/locations/us-central1/previews/IMPORT_DEPLOYMENT_PREVIEW_NAME \
         --gcs-source gs://import-deployment-configuration \
         --deployment projects/PROJECT_ID/locations/us-central1/deployments/import-deployment \
         --service-account projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         --location us-central1
         

  2. Get preview details to make sure it has finished successfully.
         
         gcloud infra-manager previews describe projects/PROJECT_ID/locations/us-central1/previews/IMPORT_DEPLOYMENT_PREVIEW_NAME
         

  3. Export the preview to review changes.
         
         SIGNED_BIN_PLAN_URL=$(gcloud infra-manager previews export projects/PROJECT_ID/locations/us-central1/previews/IMPORT_DEPLOYMENT_PREVIEW_NAME --format "get(result.binarySignedUri)")
         curl -X GET --output tfplan.out $SIGNED_BIN_PLAN_URL
         

  4. Ensure the configuration is present locally and initialized with the following command:
         
         terraform init
         

  5. Run Terraform show to review changes between Infrastructure Manager deployment state and the configuration.
         
         terraform show tfplan.out
         




If the VPC resource on Google Cloud and the state file are in sync, then `terraform show` outputs the following validating that Infrastructure Manager does not see any changes between deployment state and the configuration. You see an output similar to the following:
    
    
    No changes. Your infrastructure matches the configuration.
    
    Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
    

You have now imported the deployed resources so that they are managed by Infra Manager. For example, you can now use Infra Manager to [update the deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).

You can also [update the deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment) to validate that the deployment was successfully imported into Infra Manager.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

Delete the VPC and the metadata about the deployment:
    
    
    gcloud infra-manager deployments delete projects/PROJECT_ID/locations/us-central1/deployments/quickstart-deployment
    

## What's next

  * Learn more about [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).
  * [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).
  * [View the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).
  * [View resources deployed](https://docs.cloud.google.com/infrastructure-manager/docs/view-resources).
  * [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
