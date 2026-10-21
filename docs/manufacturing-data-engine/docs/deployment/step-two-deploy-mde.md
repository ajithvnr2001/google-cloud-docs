---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-two-deploy-mde/
title: Step 2: Deploy MDE \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:40.442678+00:00
---

# Step 2: Deploy MDE  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-two-deploy-mde/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Step 2: Deploy MDE

This page describes the steps to deploy MDE services using Terraform. Before continue, make sure to complete all steps from [Step 1: Prepare your project](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-one-prepare-your-project).

**Note:** Before upgrading your MDE deployment, see the [Known issues](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/known-issues) page.

## 1\. Get the MDE deployment assets

Access to the MDE deployment assets requires prior approval from your Google Cloud account team. Reach out to them if you are interested in testing or deploying MDE and they will start the process to give you access. If you don't know who your Google Cloud account team is, feel free to [**Contact Us**](mailto:mde-eng@google.com) and we will be in touch shortly.

## 2\. Configure gcloud CLI

Login with the `--update-adc` option, which saves the access credentials to the well-known location for Application Default Credentials (ADC). Configuring ADC is necessary so that Terraform can create resources as the `mde-tf` service account with your access credentials. Use the following command:
    
    
    #skip this if you're deploying using Cloud Shell
    gcloud auth login --update-adc
    

## 3\. Navigate to the Terraform directory

From the MDE release package root folder, navigate from the `deployment/terraform` folder using the following command:
    
    
    cd deployment/terraform
    

## 4\. Create a Terraform backend configuration:

To enable Terraform to store its state in the `PROJECT_ID-tf` Cloud Storage bucket, you must edit the `backend.conf` file in the `terraform` directory with the following instructions:

  1. Open the file in a text editor or use `sed` command on Linux.
  2. Substitute the placeholder `PROJECT_ID` for the project ID of the MDE deployment project in the `bucket` and `impersonate_service_account` variables.
  3. Save changes.



## 5\. Initialize Terraform

Initialize Terraform with the backend configuration using the following command:
    
    
    # Execute from deployment/terraform directory
    terraform init -backend-config=backend.conf -reconfigure
    

## 6\. Edit the `input.tfvars` file

Edit the `input.tfvars` file (you can find it under `deployment/terraform`) and provide values for the required variables, based on your environment. The following subsections describe them.

### MDE Project ID

The MDE Project ID should be the Project ID where you would like the GKE services to be deployed. It should be the same that you prepared in the [Step 1](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-one-prepare-your-project).

### MDE BigQuery Project ID

It is possible to designate a different project where MDE will write data to. If your organization uses a specific project where BigQuery will receive the data, use MDE BigQuery Project ID variable. In most cases, MDE will write on BigQuery in the same project, so this variable and the previous one will have the same Project ID.

### Deployment size

Pay particular attention when selecting the appropriate deployment size. The size option changes what is deployed as well as scale parameters such as max replicas, max workers for Dataflow, machine types, and others. For more information, see [Deployment sizes](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/sizes).

### Service accounts

The next two variables (`mde_tf_sa` and `mde_dataflow_sa`) contain the names of the service Accounts that you created on the [Step 1](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-one-prepare-your-project#3_create_service_accounts).

### Regions and zones for deployment

The next four variables (`mde_region`, `mde_zone`, `mde_bigquery_location`, and `mde_gke_location`) specify the regions and zones where the different components of MDE will be deployed. Check the [regions and zones](https://cloud.google.com/about/locations) available. You should only select those regions and zones where BigQuery, Dataflow and Google Kubernetes Engine are available, since these are MDE components that are not global.

### MDE web interface

**Note:** If you plan to use Manufacturing Connect (MC), you don't need to additionally deploy the MDE web interface. The MDE web interface is integrated into MC.

By default, MDE deploys with a web interface application, but it is only accessible over a private IP. See the [SSH tunneling over IAP](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-three-configure-access#ssh-tunneling-over-IAP) section on how to access the MDE web interface over a private IP from your local workstation using SSH tunneling with IAP after deployment.

To expose the MDE web interface to a wider group of users, you can optionally deploy an External HTTP Load Balancer for the MDE web interface by setting in `input.tfvars`:
    
    
    mde_ui_ext_http_lb = {
        enabled = true
        domain = "MDE_UI_DOMAIN_NAME"
    }
    

If you enable the External HTTP Load Balancer option for the MDE web interface, you must also supply a domain name. Select a domain name for which you are authorized to create DNS records.

Replace the following:

`MDE_UI_DOMAIN_NAME:` with the domain name for the _MDE web interface_. A Google-managed SSL certificate will be created for this domain.

**Important:** If you enable the External Load Balancer for the MDE web interface, you must perform additional configuration steps after the Terraform deployment. See the post-deployment sections on configuring [DNS](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/guide#configure_dns_for_mde_ui) and [IAP](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/guide#configure_access_to_the_mde_ui_external_http_load_balancer_using_iap) for more details.

## 7\. Create a Terraform plan

After the input parameters are ready, you must create a Terraform plan with the following command. You can use the plan to verify what artifacts and configurations will be created to the project.
    
    
    terraform plan -var-file=./input.tfvars -out=./tfplan
    

## 8\. Apply the Terraform plan

Apply the Terraform plan with the following command:
    
    
    terraform apply ./tfplan
    

**Note:** The Terraform deployment takes about 40 minutes to execute.

## 9\. Verify that the deployment succeeded

After the `terraform apply` command finishes executing, you should see a success message that looks similar to the following (the actual number depends on the specific deployment options you have chosen):
    
    
    Apply complete! Resources: 251 added, 0 changed, 0 destroyed.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
