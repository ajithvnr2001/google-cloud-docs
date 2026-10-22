---
url: https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline/
title: Create a custom OS image pipeline programmatically \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:28.059227+00:00
---

# Create a custom OS image pipeline programmatically  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a custom OS image pipeline programmatically Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage). 

You can configure and submit an Image Builder pipeline programmatically by using the gcloud CLI, Terraform, or client libraries such as Go. Configuring your pipeline programmatically lets you define infrastructure settings, base OS images, customization actions, and validation tests in declarative configuration files.

## Before you begin

  * Complete the environment setup steps in [Prepare your environment](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites). 
  * If you intend to deploy your pipeline using Terraform or automate builds from a repository, connect your GitHub, GitLab, or Bitbucket repository by using [Cloud Build repositories (`2nd gen`) or Developer Connect connection links](https://docs.cloud.google.com/build/docs/repositories). 
  * If you plan to use Terraform, install the [Terraform CLI](https://developer.hashicorp.com/terraform/downloads) version 1.3 or later. 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 




## Required roles

To get the permissions that you need to create and submit image customization pipelines programmatically, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create configuration files

To configure your pipeline by using the gcloud CLI or Terraform, create two configuration files:

  * [`imagebuilder.yaml`](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema): defines the customization recipe for the image, including the base OS image, worker VM infrastructure settings, target image output details, and the sequential customization steps such as running shell scripts, transferring files, or performing reboots.
  * [`cloudbuild.yaml`](https://docs.cloud.google.com/compute/docs/images/image-builder/build-configuration-schema): orchestrates the build process steps in Cloud Build, including parsing, validation, building, testing, and publishing the custom OS image.



If you submit your build by using Go, you only need to create the `imagebuilder.yaml` file and upload it to your Cloud Storage bucket, because the Go sample defines the Cloud Build orchestration steps in code.

### Create the image configuration file

To specify your image configuration, create a file named `imagebuilder.yaml` in your local directory. For a complete list of all supported schema fields and customization actions, see [Customization recipe schema](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema) and [Supported customization actions](https://docs.cloud.google.com/compute/docs/images/image-builder/supported-customization-actions).

The following sample `imagebuilder.yaml` file configures a pipeline that builds a customized Ubuntu 22.04 LTS image using an `e2-standard-4` worker VM in your specified region and zone, and performs a system package update.
    
    
    apiVersion: imagebuilder.gcp.com/v1
    kind: OSImageCustomization
    metadata:
      name: customized-ubuntu-baseline
      description: "Ubuntu 22.04 LTS custom OS baseline image"
    infrastructureConfig:
      machineType: e2-standard-4
      zone: ZONE
      debug: false
    source:
      imageFamily: projects/ubuntu-os-cloud/global/images/family/ubuntu-2204-lts
    destinations:
      - diskImage:
          name: custom-ubuntu-v1
          family: custom-ubuntu-family
          project: PROJECT_ID
          storageLocations:
            - REGION
    spec:
      config:
        skipSystemTests: false
      steps:
        -   name: "System Package Update"
          action: Shell
          inputs:
            command: "apt-get update -y && apt-get upgrade -y"

Replace the following placeholder values:

  * `PROJECT_ID`: your project ID.
  * `REGION`: the target image storage location, for example, `us-east1` or `europe-west1`. Ensure that you meet the following regional and zonal requirements: 
    * Image Builder is only supported in [regions where Cloud Build is available](https://docs.cloud.google.com/build/docs/locations).
    * The worker VM `ZONE` must be located within your specified `REGION`.
    * To minimize network latency and prevent cross-region egress charges, ensure that your worker VM zone, Cloud Storage staging bucket, Artifact Registry repository, and target image storage location are co-located in the same region.
  * `ZONE`: a zone located within your specified `REGION`, for example, `us-east1-b` or `europe-west1-b`.

**Note:** By default, Image Builder provisions worker and test VMs on your `default` VPC network with ephemeral external IP addresses. To use a custom VPC network, subnetwork, or disable external IP addresses by setting `externalIP` to `none`, configure the `network`, `subnetwork`, and `externalIP` properties under `infrastructureConfig`. For details, see [Infrastructure configuration in the customization recipe schema](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema#infrastructureconfig).

### Create the orchestrator build file

Create a file named `cloudbuild.yaml` in the same directory. This file calls the Image Builder container steps to build, validate, and publish the custom OS image.
    
    
    substitutions:
      _GCS_WORKDIR: 'gs://STAGING_BUCKET_NAME/workdir/'
      _IMAGE_BUILDER_CONFIG_PATH: 'imagebuilder.yaml'
      _SERVICE_ACCOUNT: 'projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_EMAIL'
      _IMAGE_OUTPUT_PATH: 'image-builder/binaryOut'
      _ARTIFACT_REGISTRY_RESOURCE_URI: 'projects/PROJECT_ID/locations/REGION/repositories/REPOSITORY_NAME/packages/PACKAGE_NAME/versions/v${BUILD_ID}'
    
    steps:
      #  Step 1: Parse configs and run OS customization on worker VM
      - name: 'REGION-docker.pkg.dev/image-builder-official/release/builder:stable'
        script: |
          #!/usr/bin/env bash
          /build
        id: 'imagebuilder-customize'
        results:
          - name: image_builder_telemetry_metrics
          - name: base_image
            attestationType: "https://cloudbuild.googleapis.com/attestations/build_content_restrictions"
            attestationContent: base_image
    
      # Step 2: Validate by running system boot checks on a test VM
      - name: 'REGION-docker.pkg.dev/image-builder-official/release/validator:stable'
        script: |
          #!/usr/bin/env bash
          /validate
        id: 'imagebuilder-validate'
        results:
          - name: image_builder_telemetry_metrics
    
      # Step 3: Register image in Compute Engine and upload tar files to Artifact Registry
      - name: 'REGION-docker.pkg.dev/image-builder-official/release/builder:stable'
        script: |
          #!/usr/bin/env bash
          /publish
        id: 'imagebuilder-publish'
        results:
          - name: image_builder_telemetry_metrics
    
    options:
      automapSubstitutions: true
      requestedVerifyOption: VERIFIED
      substitutionOption: ALLOW_LOOSE
      dynamicSubstitutions: true
      logging: CLOUD_LOGGING_ONLY
    
    artifacts:
      generic_artifacts:
        - folder: '${_IMAGE_OUTPUT_PATH}'
          registry_path: '${_ARTIFACT_REGISTRY_RESOURCE_URI}'
    
    timeout: '3600s'

Replace the following placeholder values:

  * `STAGING_BUCKET_NAME`: an existing Cloud Storage bucket in your project to use as a temporary staging workspace. If you don't have a bucket, you can create one by running `gcloud storage buckets create gs://STAGING_BUCKET_NAME`. If you deploy your pipeline using Terraform, Terraform creates this bucket automatically.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the Google Cloud region for you Artifact Registry repository, for example, `us-east1` or `europe-west1`.
  * `SERVICE_ACCOUNT_EMAIL`: the email for the service account that you [configured with the required IAM permissions](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#service-account).
  * `REPOSITORY` and `PACKAGE`: the target repository and package name created in Artifact Registry. To set up the Artifact Registry registry, see [Configure Artifact Registry](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#configure-artifact-registry).



## Create and submit the build pipeline

To run your image customization pipeline, submit a build by using the gcloud CLI, deploy your pipeline by using Terraform, or submit a build by using the Go client library. Select one of the following tabs:

###  gcloud 

To deploy and run your image customization pipeline, from your local terminal directory containing both configuration files, run the [`gcloud builds submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit):
    
    
    gcloud builds submit . \
        --config=cloudbuild.yaml \
        --project=PROJECT_ID \
        --service-account="projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_EMAIL" \
        --region=REGION
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the Google Cloud region to run your image customization pipeline job in.
  * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account configured with the required IAM permissions.



This command uploads your customization workspace, registers the Cloud Build execution, and launches the orchestration containers.

###  Terraform 

To provision the infrastructure required to automatically build and validate customized OS images, you can use Terraform. This Terraform configuration completes the following tasks:

  * Enables required Google Cloud APIs.
  * Creates a dedicated Cloud Storage bucket (`workdir_bucket`) to store temporary logs and build artifacts.
  * Configures a Cloud Build trigger (`image_builder_trigger`) linked to your Developer Connect GitHub repository connection.



### Create your Terraform configuration files

To organize and deploy your pipeline infrastructure by using Terraform, complete the following steps:

  1. Create a dedicated directory on your local workstation or CI/CD environment, separate from your application repository, and change into it:
         
         mkdir terraform-image-builder && cd terraform-image-builder
         

  2. In this directory, create the following five Terraform configuration files:

     * `terraform.tfvars`: sets values for project-specific variables.
     * `main.tf`: provisions resources in your Google Cloud project, including enabling required APIs, creating the Cloud Storage staging bucket (`workdir_bucket`), and deploying the Cloud Build trigger (`image_builder_trigger`).
     * `outputs.tf`: defines output values displayed in your terminal after deployment, such as the trigger ID and staging bucket name.
     * `providers.tf`: specifies the required Terraform version (`>= 1.3`) and configures the Google Cloud provider (`hashicorp/google`).
     * `variables.tf`: defines input variables, default values, and validation rules for the deployment.

Select one of the following tabs to view and copy each file's configuration into your local directory:

###  `terraform.tfvars`

This file specifies parameter values for your environment for the declared variables:
    
    project_id                = "PROJECT_ID"
    builder_service_account   = "SERVICE_ACCOUNT_EMAIL"
    github_repo_name          = "projects/PROJECT_ID/locations/LOCATION/connections/CONNECTION/repositories/REPO_NAME"
    region                    = "REGION"
    trigger_name              = "TRIGGER_NAME"
    cloudbuild_yaml_path      = "CLOUDBUILD_YAML_PATH"
    image_builder_config_path = "RECIPE_PATH"
    gcs_lifecycle_age_days    = LIFECYCLE_DAYS
    ar_repository_id          = "REPOSITORY_NAME"
    ar_package_name           = "PACKAGE_NAME"
    

Replace the following placeholders for your pre-existing resources:

     * `PROJECT_ID`: your existing Google Cloud project ID.
     * `SERVICE_ACCOUNT_EMAIL`: the email address of your build service account configured in [Configure Image Builder service account](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#service-account).
     * `LOCATION`, `CONNECTION`, and `REPO_NAME`: your Developer Connect host region, connection name, and repository link configured in [Connect a repository](https://docs.cloud.google.com/build/docs/repositories).
     * `CLOUDBUILD_YAML_PATH`: the relative path to your `cloudbuild.yaml` file in your local directory. You don't need to check `cloudbuild.yaml` into your Git repository.
     * `RECIPE_PATH`: the relative path to your `imagebuilder.yaml` customization recipe file checked into your Git repository.
     * `REPOSITORY_NAME`: the existing generic Artifact Registry repository created in [Configure Artifact Registry](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#configure-artifact-registry).

Replace the following placeholders for the resources that Terraform creates:

     * `REGION`: the target Google Cloud region where Terraform provisions the Cloud Storage staging bucket and Cloud Build trigger, for example, `us-central1`.
     * `TRIGGER_NAME`: the name for the new Cloud Build repository trigger created by Terraform, for example, `git-push-os-builder`.
     * `LIFECYCLE_DAYS`: the retention period in days before intermediate artifacts in the Cloud Storage staging bucket created by Terraform are automatically deleted, for example, `30`.
     * `PACKAGE_NAME`: the name that you want Terraform to use for the package created inside your Artifact Registry repository. This package stores published OS image versions, for example, `ubuntu-custom`.

###  `main.tf`

This file declares the core infrastructure resources and data sources for the deployment:
    
    # Main resource configurations for Image Builder.
    # 1. Enable Required APIs
    resource "google_project_service" "apis" {
      for_each = toset([
        "compute.googleapis.com",
        "cloudbuild.googleapis.com",
        "artifactregistry.googleapis.com",
        "serviceusage.googleapis.com",
        "cloudresourcemanager.googleapis.com",
        "iam.googleapis.com",
        "storage.googleapis.com"
      ])
      project = var.project_id
      service = each.key
      disable_on_destroy = false
    }
    
    # 2. Project data source to retrieve Project Number
    data "google_project" "project" {
      project_id = var.project_id
      depends_on = [google_project_service.apis]
    }
    
    locals {
      builder_sa = var.builder_service_account
    }
    
    # 3. Storage Bucket for Image Builder Workdir
    resource "google_storage_bucket" "workdir_bucket" {
      name                        = var.gcs_bucket_name != "" ? var.gcs_bucket_name : "${var.project_id}-vm-builder-workdir"
      project                     = var.project_id
      location                    = var.region
      force_destroy               = true
      uniform_bucket_level_access = true
      lifecycle_rule {
        action {
          type = "Delete"
        }
        condition {
          age = var.gcs_lifecycle_age_days
        }
      }
      depends_on = [google_project_service.apis]
    }
    
    # 4. Cloud Build Trigger
    resource "google_cloudbuild_trigger" "image_builder_trigger" {
      name        = var.trigger_name
      location    = var.region
      project     = var.project_id
      description = "Trigger that runs Image Builder customization"
    
      service_account = var.builder_service_account != "" ? "projects/${var.project_id}/serviceAccounts/${var.builder_service_account}" : null
    
      repository_event_config {
        repository = replace(var.github_repo_name, "gitRepositoryLinks", "repositories")
        push {
          branch = "^main$"
        }
      }
      filename = var.cloudbuild_yaml_path
    
      substitutions = {
        _GCS_WORKDIR                    = "gs://${google_storage_bucket.workdir_bucket.name}/workdir/"
        _SERVICE_ACCOUNT                = "projects/${var.project_id}/serviceAccounts/${local.builder_sa}"
        _IMAGE_OUTPUT_PATH              = "image-builder/binaryOut"
        _PROJECT_ID                     = var.project_id
        _LOCATION                       = var.region
        _REPOSITORY_NAME                = var.ar_repository_id
        _PACKAGE_NAME                   = var.ar_package_name
        _IMAGE_BUILDER_CONFIG_PATH      = var.image_builder_config_path
        _ARTIFACT_REGISTRY_RESOURCE_URI = "projects/${var.project_id}/locations/${var.region}/repositories/${var.ar_repository_id}/packages/${var.ar_package_name}/versions/v$${BUILD_ID}"
      }
      depends_on = [
        google_project_service.apis
      ]
    }
    

###  `outputs.tf`

This file defines the output attributes returned to your terminal after deployment:
    
    output "builder_service_account" {
      value       = local.builder_sa
      description = "The email representation of the resolved Image Builder service account."
    }
    
    output "workdir_bucket" {
      value       = google_storage_bucket.workdir_bucket.name
      description = "The name of the storage workdir bucket."
    }
    
    output "artifact_registry_repository" {
      value       = "projects/${var.project_id}/locations/${var.region}/repositories/${var.ar_repository_id}"
      description = "The fully qualified resource path of the Artifact Registry repository."
    }
    
    output "cloud_build_trigger_id" {
      value       = google_cloudbuild_trigger.image_builder_trigger.trigger_id
      description = "The unique ID for the created Cloud Build Trigger."
    }
    

###  `providers.tf`

This file configures the required Terraform version and region settings:
    
    terraform {
      required_version = ">= 1.3"
      required_providers {
        google = {
          source  = "hashicorp/google"
          version = ">= 5.0, < 7.0"
        }
      }
    }
    
    provider "google" {
      project = var.project_id
      region  = var.region
    }
    

###  `variables.tf`

This file declares all required and optional input variables and validation rules:
    
    variable "project_id" {
      type        = string
      description = "The target Project ID where resources will be created."
      validation {
        condition     = can(regex("^[a-z0-9-]{6,30}$", var.project_id))
        error_message = "The project_id must consist of lowercase letters, numbers, and hyphens, and be between 6 and 30 characters."
      }
    }
    
    variable "region" {
      type        = string
      default     = "us-central1"
      description = "Location used for cloud build triggers, storage buckets, and artifact registry."
    }
    
    variable "github_repo_name" {
      type        = string
      default     = ""
      description = "Developer Connect github repository details, format: projects/PROJECT_ID/locations/LOCATION/connections/CONNECTION/repositories/REPO_LINK"
      validation {
        condition     = can(regex("^projects/[^/]+/locations/[^/]+/connections/[^/]+/(gitRepositoryLinks|repositories)/[^/]+$", var.github_repo_name))
        error_message = "The github_repo_name must follow either the Cloud Build v2 repository link format (using '/repositories/') or the Developer Connect resource format (using '/gitRepositoryLinks/')."
      }
    }
    
    variable "builder_service_account" {
      type        = string
      default     = ""
      description = "The email representation of the pre-existing Image Builder service account. If omitted, the default Cloud Build service account will be used."
    }
    
    variable "gcs_bucket_name" {
      type        = string
      default     = ""
      description = "Custom name for the workdir storage bucket. If left empty, a default name using the project ID will be constructed."
    }
    
    variable "gcs_lifecycle_age_days" {
      type        = number
      default     = 30
      description = "The number of days after which temporary logs and artifacts in the storage workdir bucket are deleted."
    }
    
    variable "ar_repository_id" {
      type        = string
      default     = "vm-images"
      description = "The repository ID for the generic Artifact Registry hosting the final OS image tarballs."
    }
    
    variable "ar_package_name" {
      type        = string
      default     = "image-builder"
      description = "The package name under which the generic OS image artifact will be registered in Artifact Registry."
    }
    
    variable "trigger_name" {
      type        = string
      default     = "custom-os-image-builder"
      description = "The name of the Cloud Build trigger."
    }
    
    variable "cloudbuild_yaml_path" {
      type        = string
      default     = "cloudbuild.yaml"
      description = "The path to the cloudbuild.yaml configuration file relative to the repository root."
    }
    
    variable "image_builder_config_path" {
      type        = string
      default     = "imagebuilder.yaml"
      description = "The path to the imagebuilder.yaml configuration file relative to the repository root."
    }
    

  3. To deploy the configurations, run the following commands in the directory containing your Terraform files:

     1. Initialize the directory: 
            
            terraform init

     2. Validate the syntax: 
            
            terraform validate

     3. Preview the deployment: 
            
            terraform plan

     4. Apply the configuration: 
            
            terraform apply




###  Go 

Before you run this sample, upload your `imagebuilder.yaml` configuration file to your Cloud Storage staging bucket, for example, `gs://STAGING_BUCKET_NAME/imagebuilder.yaml`.

To submit a Cloud Build build that runs the Image Builder pipeline by using the Cloud Build Go client library, use the following sample:
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"io"
    
    	"google.golang.org/api/cloudbuild/v1"
    )
    
    // submitBuild submits a Cloud Build build that uses Image Builder to
    // customize, validate, and publish a VM image to Compute Engine and Artifact
    // Registry.
    //
    // Before you run this sample, upload your imagebuilder.yaml configuration file
    // to Cloud Storage, create a generic Artifact Registry repository, and create a
    // service account to run the build.
    func submitBuild(w io.Writer, projectID, gcsWorkdir, configPath, serviceAccount string) error {
    	// projectID := "my-project-id"
    	region := "us-central1"
    	// gcsWorkdir := "gs://my-bucket/workdir/"
    	// configPath := "gs://my-bucket/imagebuilder.yaml"
    	repository := "vm-images"
    	packageName := "custom-os-images"
    	// serviceAccount := "image-builder@my-project-id.iam.gserviceaccount.com"
    
    	ctx := context.Background()
    	cbService, err := cloudbuild.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("cloudbuild.NewService: %w", err)
    	}
    
    	sa := fmt.Sprintf("projects/%s/serviceAccounts/%s", projectID, serviceAccount)
    	req := &cloudbuild.Build{
    		ServiceAccount: sa,
    		// AutomapSubstitutions exposes these substitutions to every step as
    		// environment variables. See
    		// https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values#mapping_substitutions_to_environment_variables
    		Substitutions: map[string]string{
    			"_GCS_WORKDIR":               gcsWorkdir,
    			"_SERVICE_ACCOUNT":           sa,
    			"_IMAGE_OUTPUT_PATH":         "image-builder/binaryOut",
    			"_IMAGE_BUILDER_CONFIG_PATH": configPath,
    			"_ARTIFACT_REGISTRY_RESOURCE_URI": fmt.Sprintf(
    				"projects/%s/locations/%s/repositories/%s/packages/%s/versions/v${BUILD_ID}",
    				projectID, region, repository, packageName,
    			),
    		},
    		Steps: []*cloudbuild.BuildStep{
    			{
    				Id:     "imagebuilder-customize",
    				Name:   "us-docker.pkg.dev/image-builder-official/release/builder:stable",
    				Script: "#!/usr/bin/env bash\n/build",
    				Results: []*cloudbuild.StepResult{
    					{
    						Name:            "base_image",
    						AttestationType: "https://cloudbuild.googleapis.com/attestations/build_content_restrictions",
    					},
    					{Name: "image_builder_telemetry_metrics"},
    				},
    			},
    			{
    				Id:      "imagebuilder-validate",
    				Name:    "us-docker.pkg.dev/image-builder-official/release/validator:stable",
    				Script:  "#!/usr/bin/env bash\n/validate",
    				Results: []*cloudbuild.StepResult{{Name: "image_builder_telemetry_metrics"}},
    			},
    			{
    				Id:      "imagebuilder-publish",
    				Name:    "us-docker.pkg.dev/image-builder-official/release/builder:stable",
    				Script:  "#!/usr/bin/env bash\n/publish",
    				Results: []*cloudbuild.StepResult{{Name: "image_builder_telemetry_metrics"}},
    			},
    		},
    		Options: &cloudbuild.BuildOptions{
    			AutomapSubstitutions:  true,
    			DynamicSubstitutions:  true,
    			RequestedVerifyOption: "VERIFIED",
    			SubstitutionOption:    "ALLOW_LOOSE",
    			// Builds that run as a user-specified service account must set a
    			// logging option.
    			Logging: "CLOUD_LOGGING_ONLY",
    		},
    		Artifacts: &cloudbuild.Artifacts{
    			GenericArtifacts: []*cloudbuild.GenericArtifact{
    				{
    					Folder:       "${_IMAGE_OUTPUT_PATH}",
    					RegistryPath: "${_ARTIFACT_REGISTRY_RESOURCE_URI}",
    				},
    			},
    		},
    		Timeout: "3600s",
    	}
    
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, region)
    	op, err := cbService.Projects.Locations.Builds.Create(parent, req).Context(ctx).Do()
    	if err != nil {
    		return fmt.Errorf("Builds.Create: %w", err)
    	}
    
    	// The operation metadata contains the build that was created.
    	var metadata cloudbuild.BuildOperationMetadata
    	if err := json.Unmarshal(op.Metadata, &metadata); err != nil {
    		return fmt.Errorf("json.Unmarshal: %w", err)
    	}
    	fmt.Fprintf(w, "Build submitted. ID: %s\n", metadata.Build.Id)
    	fmt.Fprintf(w, "Logs: %s\n", metadata.Build.LogUrl)
    	return nil
    }
    

## Verify and monitor the build

To track the progress of your build pipeline, complete the following steps:

  1. In the Google Cloud console, go to the **Cloud Build** page.

[Go to Cloud Build](https://console.cloud.google.com/cloud-build/builds)

  2. In the navigation menu, click **History** to view active or completed jobs.

  3. In the **Builds** list, click the **Build ID** of your build to inspect container run logs. The logs display steps being performed inside the worker VM such as system package updates or custom shell commands, followed by validation test results from the test VM, and final output registration.




## What's next

  * To configure and launch recurring or automated builds from the command line: 
    * [Schedule custom OS image builds](https://docs.cloud.google.com/compute/docs/images/image-builder/schedule-builds)
    * [Automate builds on repository events](https://docs.cloud.google.com/compute/docs/images/image-builder/automate-builds-on-events)
  * [Verify image provenance](https://docs.cloud.google.com/compute/docs/images/image-builder/verify-image-provenance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
