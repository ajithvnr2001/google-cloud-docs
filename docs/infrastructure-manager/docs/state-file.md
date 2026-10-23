---
url: https://docs.cloud.google.com/infrastructure-manager/docs/state-file/
title: Manage the Terraform state file \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:21.190773+00:00
---

# Manage the Terraform state file  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/state-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Manage the Terraform state file Stay organized with collections  Save and categorize content based on your preferences. 

For any deployment, you may want to inspect or modify the state file. For example, you may want to import or remove resources from the deployment, which you do through modifying the state file.

This page describes how to work with the Terraform state file that is created for each deployment and revision. To learn more about the state file, see [State](https://developer.hashicorp.com/terraform/language/state).

The instructions on this page assume that you are familiar with [Terraform](https://developer.hashicorp.com/terraform/intro).

## Before you begin

  1. Ensure you have the required permissions to work with the state file. The `config.admin` role includes the required permissions. The specific permissions needed are:

     * `config.deployments.lock`
     * `config.revisions.getState`
     * `config.deployments.updateState`
     * `config.deployments.unlock`
     * `config.deployments.getLock`
     * `config.deployments.getState`
  2. Ensure you have a local copy of the Terraform configuration. This is the configuration that corresponds to the state file you are working with.

The local copy of the configuration lets you run commands such as `terraform refresh` or `terraform plan` locally while you are modifying the state file.

  3. [Install Terraform](https://developer.hashicorp.com/terraform/downloads) to use the Terraform CLI on your local machine.




## Mutate or inspect the state file

To mutate (modify) or inspect the state file, you need to lock the deployment and download the state file. You can then mutate or inspect the state file.

After you mutate the state file, you then upload the file for Infra Manager to use in your deployment.

### Lock the deployment

  1. Lock the deployment to prevent any changes to the deployment while you mutate the statefile. The deployment must be locked to be able to download the state file.
         
         gcloud infra-manager deployments lock DEPLOYMENT_ID --project PROJECT_ID --location LOCATION
         

Replace:

     * DEPLOYMENT_ID with the deployment identifier.
     * PROJECT_ID with the project where the deployment runs.
     * LOCATION with the location where the deployment runs.

The output of this command contains a `lock ID` that is used for uploading and unlocking the statefile.

  2. To retrieve the lock ID at any time, use the command:
         
         gcloud infra-manager deployments export-lock DEPLOYMENT_ID --project PROJECT_ID --location LOCATION
         




### Download the state file

To download the state file, you use a [signed Cloud Storage URL](https://docs.cloud.google.com/storage/docs/access-control/signed-urls):
    
    
    SIGNED_STATE_DOWNLOAD_URL=$(gcloud infra-manager deployments export-statefile DEPLOYMENT_ID --project PROJECT_ID --location LOCATION --format="get(signedUri)")
    
    curl -s -X GET --output terraform.tfstate ${SIGNED_STATE_DOWNLOAD_URL}
    

### Mutate the state file locally

  1. Confirm that the configuration (`*.tf` files) is in the same directory as the downloaded state file (`terraform.tfstate`).

  2. Initialize Terraform:
         
         terraform init
         

  3. If you have previously initialized Terraform, you may need to initialize with the reconfigure flag:
         
         terraform init -reconfigure
         

  4. Work with the state file as you need. For example, you can do [state inspection](https://developer.hashicorp.com/terraform/cli/state/inspect) or [mutation](https://developer.hashicorp.com/terraform/cli/state/move) operations. For more details about working with the state file, see [Manipulating Terraform State](https://developer.hashicorp.com/terraform/cli/state).

  5. If you make any changes to the Terraform configuration files locally, then upload the modified configuration. Upload this configuration to the [storage bucket](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment) or public git repository that you are using as the source to deploy the configuration.




### Upload the state file

Use a [signed Cloud Storage URL](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) to upload the state file:

  1. Get the lock ID:
         
         LOCK_ID=$(gcloud infra-manager deployments export-lock DEPLOYMENT_ID --project PROJECT_ID --location LOCATION --format="get(lockId)")
         

  2. Get the upload URL:
         
         SIGNED_STATE_UPLOAD_URL=$(gcloud infra-manager deployments import-statefile DEPLOYMENT_ID --project PROJECT_ID --location LOCATION --lock-id ${LOCK_ID} --format="get(signedUri)")
         
         curl -s -X PUT --upload-file terraform.tfstate ${SIGNED_STATE_UPLOAD_URL}
         




### Unlock the deployment

  1. Get the lock ID:
         
         LOCK_ID=$(gcloud infra-manager deployments export-lock DEPLOYMENT_ID --project PROJECT_ID --location LOCATION --format="get(lockId)")
         

  2. Unlock the deployment:
         
         gcloud infra-manager deployments unlock DEPLOYMENT_ID --project PROJECT_ID --location LOCATION --lock-id ${LOCK_ID}
         




## What's next

  * Learn more about [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).
  * [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).
  * [View the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).
  * [View resources deployed](https://docs.cloud.google.com/infrastructure-manager/docs/view-resources).
  * [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
