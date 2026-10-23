---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/upgrade-guide/
title: Upgrade guide \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:12.243346+00:00
---

# Upgrade guide  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/upgrade-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upgrade guide

This guide provides general guidance on how to upgrade an existing Manufacturing Data Engine (MDE) installation using Terraform.

If you have modified Terraform scripts you might need additional steps. This is a generic upgrade guide so always make sure that you also read the full [releases notes](https://docs.cloud.google.com/manufacturing-data-engine/docs/release-notes) for the specific version you are deploying as this may include information you need to take into consideration.

**Caution:** If you are upgrading from v1.4.x to v1.5, the process will recreate some of the internal Pub/Sub subscriptions. Make sure that the existing MDE instance is fully drained and that it doesn't have any internal messages in the Pub/Sub subscriptions before running the upgrade script. You can achieve this by stopping the messages sent to the `input-message` subscription.**Note:** MDE only supports sequential upgrades. If you are running a major release earlier than 1.4.x, you must upgrade your MDE one major version at a time.

## Before you begin

**Note:** Before upgrading your MDE deployment, see the [Known issues](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/known-issues) page.

Some Dataflow jobs need to be stopped manually before upgrading. The [release notes](https://docs.cloud.google.com/manufacturing-data-engine/docs/release-notes) list the jobs you have to stop manually for the specific version you are upgrading to.

This guide requires the follow prerequisites:

  1. You are using the default deployment package.
  2. Your client environment has the required CLI tools installed in their most updated version:

     * [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) with the following additional components installed:

       * [kubectl](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_kubectl)
       * [cbt](https://docs.cloud.google.com/bigtable/docs/cbt-overview#installing)
       * [Terraform CLI](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) ( 1.9.x or later)
       * [Helm CLI](https://helm.sh/docs/intro/install/) (3.9.x or later)

You can use any client environment to deploy MDE, but you can save time by deploying from Cloud Shell since it has most of the required tools already installed. 

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. You have full access to the MDE Google Cloud project and access to the configuration files used for the original deployment:

     * Service Account JSON key file: `mde-imgs-service-account-key.json`.
     * Terraform: `input.tfvars`.
     * Terraform: `backend.conf`.
**Note:** MDE v1.5 doesn't require the Service Account JSON key file.

All `gcloud` commands in this guide assume that the default project is set to the MDE deployment project. You can set the default project using the following command:
    
    gcloud config set project PROJECT_ID
    

Replace PROJECT_ID with the MDE deployment project ID.

  4. You have acquired the credentials for the MDE GKE cluster. Use the following command if you haven't already:
         
         export CLUSTER_NAME="mde-gke"
         export CLUSTER_LOCATION=$(gcloud container clusters list --filter="name:$CLUSTER_NAME" --format="value(LOCATION)" )
         
         # when upgrading to 1.5.2 we need to enable DNS endpoint on GKE cluster to allow Terraform connect to it
         gcloud container clusters update $CLUSTER_NAME --region $CLUSTER_LOCATION --enable-dns-access
         
         export KUBE_CONFIG_PATH=~/.kube/config
         gcloud container clusters get-credentials $CLUSTER_NAME --region $CLUSTER_LOCATION --dns-endpoint
         

Replace CLUSTER_NAME with the name of the cluster if you changed the default name (`mde-gke`). Change `KUBE_CONFIG_PATH` if your kubeconfig is not on the default path.




## Upgrade

This section provides guidance on how perform the upgrade using Terraform.

  1. Update the Terraform service account permissions to add the newly required permissions from MDE 1.4.0 and up. They can be added by using the following commands:
         
         export PROJECT_ID=$(gcloud config get-value project)
         export SA_TERRAFORM="mde-tf"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
         --member="serviceAccount:$SA_TERRAFORM@$PROJECT_ID.iam.gserviceaccount.com" \
         --role='roles/file.editor'
         

  2. Backup the old deployment folder using the following command:
         
         cp -r MDE_FOLDER MDE_FOLDER_BACKUP
         

Replace MDE_FOLDER and MDE_FOLDER_BACKUP with the name of the MDE folder and backup folder.

  3. Download the latest MDE solution release package and extract it:

**Note:** Access to the MDE deployment assets requires approval from your Google Cloud team. We suggest reaching out to them as soon as possible if you are interested in testing or deploying MDE. If you don't know who your Google Cloud account team is, feel free to use the `Contact Us` button on the top right of the screen and we will be in touch shortly.
     1. Download the solution package.
     2. Extract the package to your client environment.
     3. Move into the new release folder using the `cd` command.
  4. If you are upgrading to v1.4.x, copy the following files from the backup to the new folder using the following commands (files paths may differ):
         
         cp ../MDE_FOLDER_BACKUP/mde-imgs-service-account-key.json .
         cd deployment/terraform
         cp ../../../MDE_FOLDER_BACKUP/deployment/terraform/input.tfvars .
         cp ../../../MDE_FOLDER_BACKUP/deployment/terraform/backend.conf .
         

If you are upgrading to v1.5.1, copy only the following files:
         
         cd deployment/terraform
         cp ../../../MDE_FOLDER_BACKUP/deployment/terraform/input.tfvars .
         cp ../../../MDE_FOLDER_BACKUP/deployment/terraform/backend.conf .
         

Replace MDE_FOLDER_BACKUP with the MDE backup folder name.

  5. If you are upgrading from v.1.4.x to v1.5.x or from v1.5.0 to v1.5.1, run the pre-upgrade script included in the release package:

**Note:** Make sure that you run this script after all the Pub/Sub subscriptions have been drained, you can use the '/configuration/v1/processing:stop' API or toggle the `Messages processing` switch in the MDE UI to stop the processing and let the system drain before running this script.
         
         # Execute script from the upgrade/1.5 directory and return to the terraform directory
         cd ../../upgrade/1.5
         export BQ_PROJECT_ID=$(gcloud config get-value project)
         export PUBSUB_PROJECT_ID=$(gcloud config get-value project)
         sh migrate-metadata-instance-bq-table.sh "$BQ_PROJECT_ID" "$PUBSUB_PROJECT_ID"
         cd ../../deployment/terraform
         

  6. If you are upgrading to 1.5.2, you need to switch the Kubernetes providers to use the local kubeconfig in the `providers.tf` file with the following command:
         
         provider "kubernetes" {
         config_path            = "~/.kube/config"
         # host                   = "https://${local.gke_host}"
         # token                  = data...
         # cluster_ca_certificate = local.gke_ca_cert
         }
         
         provider "helm" {
         kubernetes {
             config_path            = "~/.kube/config"
             # host                   = "https://${local.gke_host}"
             # token                  = data...
             # cluster_ca_certificate = local.gke_ca_cert
         }
         }
         

**Note:** After you have finished applying the upgrade (after step 10), this change can be rolled back to continue using the dynamic Kubernetes configuration inside Terraform.
  7. Reload the Terraform state using the following command:
         
         terraform init -backend-config=backend.conf -reconfigure
         

  8. Create a Terraform plan.

Once the input parameters are ready, you must create a Terraform plan using the following command. You can use the plan to verify what artifacts and configurations will be created in the project.

**Note:** Since the Service Account key is no longer necessary after v1.5.x, you might see a Terraform warning about `mde_artifact_registry_sa_path`. You can safely ignore this warning, comment out or delete this variable from the `input.tfvars` file.
         
         terraform plan -var-file=./input.tfvars -out=./tfplan
         

You can browse the planned changed by using this command:
         
         terraform show -no-color ./tfplan > tfplan.txt
         more tfplan.txt
         

**Important:** If Terraform shows errors during the planning phase that certain Pub/Sub subscriptions that end up with the `-materialization` suffix can't be deleted because they have a `lifecycle.prevent_destroy` flag, then you will need to manually delete all of the Pub/Sub topics that end up with the `-materialization` suffix along with the subscriptions that were attached to it. You will need to perform this step _before_ starting the deployment to make sure that the topics are created automatically by MDE post the deployment.
  9. Apply the Terraform plan using the following command:
         
         terraform apply ./tfplan
         

  10. Verify that the deployment succeeded.

After the `terraform apply` command finishes executing, you should see a success message that looks similar to the following (the actual number will depend on the specific deployment options and version):
         
         Apply complete! Resources: 1 added, 34 changed, 0 destroyed.
         




## Post Upgrade

After the upgrade is complete, you need to perform one or more of the following steps depending on the status of the earlier MDE deployment.

### BigQuery views for existing types

If you are upgrading from a release before 1.4.x, then the created types won't have an analytics view created for it as this feature was introduced in 1.4.0. You'll need to activate the existing types once again to trigger the analytics view recreation. You can check the `/activate` endpoint in the Postman kit that's shipped with the release.

### GKE cluster filestore driver

If you experience an issue that the GKE cluster pods are starting or stuck in `ContainerCreating`, then it could be the result of the filestore driver not being enabled. You can enable it by following the steps in the deployment [guide](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-three-configure-access#enabling-GKE%20cluster-filestore-driver)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
