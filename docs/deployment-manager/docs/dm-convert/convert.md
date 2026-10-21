---
url: https://docs.cloud.google.com/deployment-manager/docs/dm-convert/convert/
title: Convert your Deployment Manager configurations with DM Convert \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:59.083553+00:00
---

# Convert your Deployment Manager configurations with DM Convert  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/dm-convert/convert/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Convert your Deployment Manager configurations with DM Convert Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes the process of using DM Convert to convert your Deployment Manager configurations to [Kubernetes Resource Model (KRM)](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md) or [Terraform](https://www.terraform.io/).

## Set up your environment

### Set up your environment variables

Save the following environment variables, which the rest of this guide uses:
    
    
    export PROJECT_ID=$(gcloud config get-value project) \
    export DM_CONVERT_IMAGE="us-central1-docker.pkg.dev/\
    dm-convert-host/deployment-manager/dm-convert:public-preview"
    

**Note:** This docker image is just to facilitate the process of creating output file from any deployment yaml.

### Set up your tools

You must have access to the following tools:

  * `gcloud`

  * `docker`

  * `kubectl`

  * `bq`

  * [`jq`](https://stedolan.github.io/jq/download/)




If you use [Cloud Shell](https://docs.cloud.google.com/shell) to run DM Convert, you already have access to them.

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/GoogleCloudPlatform/deploymentmanager-samples.git)

## Convert your configurations

At a high level, you migrate your Deployment Manager configuration to Terraform or KRM by:

  1. Preparing a Deployment Manager deployment for conversion.

  2. Converting the configuration to either the HCL (HashiCorp configuration language, for Terraform) or the KRM (Kubernetes Resource Model) format.

  3. Using Terraform or Config Connector to apply the converted configuration.

  4. Abandoning the existing Deployment Manager deployment.




### Prepare your existing deployment

DM Convert operates on Deployment Manager configuration files and templates. Throughout the guide, these files will be created and saved locally as input for the DM Convert tool.

You can create a configuration file yourself or acquire a configuration from a live deployment.

#### Convert a configuration file

You can use the following sample configuration to try out the converter. Replace `PROJECT_ID` with your Google Cloud project ID, and save the below contents to a file called `deployment.yaml`:
    
    
      resources:
      - name: bigquerydataset
        type: bigquery.v2.dataset
        properties:
          datasetReference:
            datasetId: bigquerydataset
            projectId: PROJECT_ID
          defaultTableExpirationMs: 36000000
          location: us-west1
      - type: bigquery.v2.table
        name: bigquerytable
        properties:
          datasetId: bigquerydataset
          labels:
            data-source: external
            schema-type: auto-junk
          tableReference:
            projectId: PROJECT_ID
            tableId: bigquerytable
        metadata:
          dependsOn:
          - bigquerydataset
    

**Note:** If you want to try out a different configuration, ensure that the configuration file and all of its dependencies (Jinja or Python templates) are copied in the same folder hierarchy from this example.

  * Acquire a configuration from a live deployment

If you want to acquire and convert the configuration of a live deployment, you can retrieve the expanded configuration and save it to disk by running the following commands, replacing `DEPLOYMENT_NAME` with the name of the deployment.
        
        # Configure your project/deployment
        DEPLOYMENT_NAME=DEPLOYMENT_NAME
        PROJECT_ID=PROJECT_ID
        
        # Fetch the latest manifest for the given deployment
        gcloud deployment-manager deployments describe $DEPLOYMENT_NAME \
          --project $PROJECT_ID --format="value(deployment.manifest)"
        
        # The output should look like this:
        # https://www.googleapis.com/deploymentmanager/v2/projects/$PROJECT_ID/global/deployments/bq/manifests/manifest-1618872644848
        
        # The manifest name is the last path segment from the URI
        # in the above command output
        MANIFEST_NAME="manifest-1618872644848"
        # Save the expanded manifest to deployment.yaml
        gcloud deployment-manager manifests describe $MANIFEST_NAME \
          --deployment $DEPLOYMENT_NAME --project $PROJECT_ID \
          --format="value(expandedConfig)" > deployment.yaml
        




## Convert your deployment

To convert resources in `deployment.yaml` to HCL or KRM format and save them as converted outputs, run the following command in the same directory as `deployment.yaml` with the desired substitutions:
    
    
    CONVERTED_RESOURCES=OUTPUT_FILE
    
    docker run --rm -it --workdir=/convert \
    --volume=$(pwd):/convert \
    $DM_CONVERT_IMAGE \
    --config deployment.yaml \
    --output_format OUTPUT_FORMAT \
    --output_file OUTPUT_FILE \
    --output_tf_import_file OUTPUT_IMPORT_FILE \
    --deployment_name DEPLOYMENT_NAME \
    --project_id $PROJECT_ID
    

Make the following substitutions:

  * `OUTPUT_FORMAT`: The output format for the conversion. This can be either `TF` for Terraform or `KRM` for KRM.

  * `OUTPUT_FILE`: The name of the file to which the converted output is saved.

  * **(Terraform Only)** `OUTPUT_IMPORT_FILE`: The name of the file to which the Terraform import commands are saved. If a `project_id` flag is specified, the import commands are generated based on that flag. If a `project_id` flag isn't specified, the import commands are generated based on the `projectId` attribute from the resource configuration. 

  * `DEPLOYMENT_NAME`: The name of the deployment. This is relevant if you're using templates in your Deployment Manager configuration, and are also using the `deployment` environment variable. For more information, visit [Using an environment variable](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables#using_an_environment_variable).




### View the conversions
    
    
    # Print output file
    cat OUTPUT_FILE
    

## Apply your converted configuration

### Terraform

### Set up Terraform
    
    
    # Configure default project
    cat <<EOF > echo > main.tf
    provider "google" {
      project = "$PROJECT_ID"
    }
    EOF
    

**Note:** The Terraform setup in this guide is suitable for testing purposes. For a comprehensive list of best practices for running Terraform on Google Cloud, including using Cloud Storage to store and manage Terraform state remotely, visit [Managing infrastructure as code with Terraform, Cloud Build, and GitOps](https://docs.cloud.google.com/architecture/managing-infrastructure-as-code).

After you've converted your Deployment Manager resources to Terraform, you can use Terraform to create resources by directly deploying the converted configuration.

### Deploy your converted configuration using Terraform
    
    
    # NOTE: if Terraform state gets corrupted during testing,
    # use init --reconfigure to reset backend
    terraform init
    echo "***************  TERRAFORM PLAN  ******************"
    terraform plan
    echo "**************  TERRAFORM APPLY  ******************"
    terraform apply
    

### (Optional) Import existing resources

If you're converting an existing deployment and you want to use Terraform to manage its resources without redeploying, you can do so by using Terraform [Import feature](https://developer.hashicorp.com/terraform/cli/import).

For this section, you will use `deployment.yaml` for the import process.

Initialize Terraform:
    
    
    # NOTE: if Terraform state gets corrupted during testing,
    # use init --reconfigure to reset backend
    terraform init
    

The import commands are generated and saved to `OUTPUT_IMPORT_FILE`. To review its contents, run the following command:
    
    
    cat OUTPUT_IMPORT_FILE
    

To import the resources for `deployment.yaml`, run the following command:
    
    
    # Make the import file executable
    chmod +x OUTPUT_IMPORT_FILE
    # Perform the import
    ./OUTPUT_IMPORT_FILE
    

After you've imported the resources into your Terraform state, you can verify if there are any changes between the state and the generated Terraform configuration by running the Terraform `plan` command:
    
    
    terraform plan
    

This produces the following output:
    
    
    Terraform will perform the following actions:
    
    # google_bigquery_dataset.bigquerydataset will be updated in-place
    ~ resource "google_bigquery_dataset" "bigquerydataset" {
        ...
        ~ labels = {
            # the label value will be based on the deployment name and may not
            # match
            - "goog-dm" = "bq-for-import" -> null
          }
        ...
      }
    
    # google_bigquery_table.bigquerytable will be updated in-place
    ~ resource "google_bigquery_table" "bigquerytable" {
        ...
        ~ labels = {
            # the label value will be based on the deployment name and may not
            # match
            - "goog-dm" = "bq-for-import" -> null
          }
        ...
      }
    
    Plan: 0 to add, 2 to change, 0 to destroy.
    

Accept this change in the Terraform plan since it is removing Deployment Manager specific labels i.e. `goog-dm` which are not required once resources are being managed by Terraform.

**Note:** In the example provided here, the converted configuration doesn't have significant changes from the original configuration. However, when you import resources, you must carefully review any changes between the imported state and the generated configurations before you apply them.

To apply the Terraform configuration, run the following command:
    
    
    # Accept changes by entering yes when prompted
    terraform apply
    

Now all resources defined in `deployment.yaml` are under Terraform management.

For instance, if you'd like to verify that Terraform is in fact managing the converted resources, you can do so by making a slight change to the Terraform configuration by modifying the default table expiration time in the `google_bigquery_dataset.bigquerydataset` resource:
    
    
    ...
    # change from 10 hrs to 12 hrs
    default_table_expiration_ms = 43200000
    ...
    

After you make your changes, you can apply the Terraform configuration, and use the `bq` command-line interface (CLI) to verify the changes:
    
    
    # Accept changes by entering yes when prompted
    terraform apply
    # Access the dataset properties via bq to verify the changes
    bq show --format=prettyjson bigquerydataset | jq '.defaultTableExpirationMs'
    

The output you receive should match the values provided in the updated Terraform configuration, confirming that Terraform is now managing these resources.

### KRM

### Set up Config Connector

**Note:** Config Connector itself doesn't incur any cost, but the Google Kubernetes Engine (GKE) clusters and resources created by Config Connector do. For more details, visit [Quotas and limits](https://docs.cloud.google.com/kubernetes-engine/quotas).

To actuate the resources in the KRM configuration files, you need a Kubernetes cluster with Config Connector installed. To create a test cluster, refer to [Installing with the GKE add-on](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall).

In Cloud Shell, ensure that your `kubectl` credentials are configured for the GKE cluster that you want to use. Replace `GKE_CLUSTER` with the name of the cluster, and run the following command:
    
    
    gcloud container clusters get-credentials GKE_CLUSTER
    

### Deploy your converted KRM configuration by using `kubectl`

To deploy your converted KRM configuration using `kubectl`, run the following commands:
    
    
    # Ensure that the namespace is annotated to create resources in the correct
    # project/folder/organization. https://cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall#specify
    kubectl apply -n CONFIG_CONNECTOR_NAMESPACE \
      -f OUTPUT_FILE
    
    # Wait for the resources to become healthy
    kubectl wait -n CONFIG_CONNECTOR_NAMESPACE \
      --for=condition=Ready \
      --timeout=5m -f OUTPUT_FILE
    

## Clean up

### Clean up the sample dataset and table

### Terraform
    
    
    # NOTE: if Terraform state gets corrupted during testing,
    # use init --reconfigure to reset backend
    echo "***************  TERRAFORM INIT  ******************"
    terraform init
    # Remove delete protection on BigQuery table
    sed -i "/resource \"google_bigquery_table\"/a deletion_protection=\"false\"" \
    OUTPUT_FILE
    terraform apply
    echo "***************  TERRAFORM DESTROY ****************"
    terraform destroy
    

### KRM

To clean up the BigQuery dataset and table from the sample configuration, run:
    
    
    # If the resource was created via Config Connector:
    kubectl delete -n CONFIG_CONNECTOR_NAMESPACE \
      -f OUTPUT_FILE
    

## Abandon the sample Deployment Manager deployment

To abandon a live deployment that you successfully converted to KRM or Terraform, run:

**Note:** this command should be run for sample deployments only that created as part of this guide.
    
    
    gcloud deployment-manager deployments delete DEPLOYMENT_NAME --delete-policy ABANDON
    

## Supported resources for conversion

### Terraform

To list supported resources for Terraform, run the following command:
    
    
    docker run --rm -it \
    us-central1-docker.pkg.dev/dm-convert-host/deployment-manager/dm-convert:public-preview \
    --output_format tf \
    --list_supported_types
    

### KRM

To list supported resources for KRM, run the following command:
    
    
    docker run --rm -it \
    us-central1-docker.pkg.dev/dm-convert-host/deployment-manager/dm-convert:public-preview \
    --output_format krm \
    --list_supported_types
    

## Next steps

Review [best practices and recommendations](https://docs.cloud.google.com/deployment-manager/docs/dm-convert/docs/dm-convert/best-practices) for the converted configuration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
