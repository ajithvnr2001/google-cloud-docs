---
url: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart/
title: Quickstart: Deploy feature flags \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:18.585900+00:00
---

# Quickstart: Deploy feature flags  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy feature flags

This quickstart shows you how to create, rollout and use feature flags with App Lifecycle Manager.

In this quickstart, you'll learn how to install and configure a flag provider, and perform basic feature flagging using App Lifecycle Manager feature flags.

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the App Lifecycle Manager, Artifact Registry, Infrastructure Manager, Developer Connect, Cloud Build, Cloud Storage, Cloud Run and SaaS Config APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=saasservicemgmt.googleapis.com,artifactregistry.googleapis.com,config.googleapis.com,developerconnect.googleapis.com,cloudbuild.googleapis.com,storage.googleapis.com,saasconfig.googleapis.com,run.googleapis.com)

  5. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Project > Owner** role to the service account. 

To grant the role, find the **Select a role** list, then select **Project > Owner**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  11. Enable the App Lifecycle Manager, Artifact Registry, Infrastructure Manager, Developer Connect, Cloud Build, Cloud Storage, Cloud Run and SaaS Config APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=saasservicemgmt.googleapis.com,artifactregistry.googleapis.com,config.googleapis.com,developerconnect.googleapis.com,cloudbuild.googleapis.com,storage.googleapis.com,saasconfig.googleapis.com,run.googleapis.com)

  12. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Project > Owner** role to the service account. 

To grant the role, find the **Select a role** list, then select **Project > Owner**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  16. Create an App offering. You need an App offering to complete this quickstart. For more information about how to create an App offering, see [Create an App offering](https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering).



## Grant permissions to App Lifecycle Manager service account

When you enable the App Lifecycle Manager API, App Lifecycle Manager creates a service account. This service account is called `service-PROJECT-NUMBER@gcp-sa-saasservicemgmt.iam.gserviceaccount.com`, where `PROJECT-NUMBER` is your project number.

Grant this service account required permissions by running the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-saasservicemgmt.iam.gserviceaccount.com" \
        --role="roles/saasservicemgmt.serviceAgent"
    

Replace:

  * PROJECT_ID: A string identifier representing your project ID.
  * PROJECT_NUMBER: Your project number.



Locating reference documentation

This service account acts on your behalf for various tasks like provisioning units.

## Create a repository in Artifact Registry

To use App Lifecycle Manager, you need a repository in Artifact Registry. To create this repository, run the following command in your terminal:
    
    
    gcloud artifacts repositories create flags-quickstart \
        --repository-format=docker \
        --location=us-central1
    

This repository will contain a blueprint (packaged Terraform files) describing how to provision your units.

## Create a feature flagging application blueprint

Create a Python script that reads a feature flag and use it to build and push a Docker image:

  1. Create a directory named `alm_docker` for your Docker build context.

  2. In the `alm_docker` directory, create the file `flags.py` with the this snippet:
         
         import google.auth.transport.grpc
         import google.auth.transport.requests
         import grpc
         import logging
         import time
         import os
         import sys
         from flask import Flask, jsonify
         
         from openfeature import api
         from openfeature.provider import ProviderEvent, ProviderStatus
         from openfeature.contrib.provider.flagd import FlagdProvider
         from openfeature.contrib.provider.flagd.config import ResolverType
         
         # --- Flask App Setup ---
         app = Flask(__name__)
         
         # --- Logging Setup ---
         logging.basicConfig(stream=sys.stdout) # Log to stdout for Cloud Run
         log = logging.getLogger(__name__)
         log.setLevel(logging.INFO) # Use INFO or DEBUG as needed
         
         # --- OpenFeature/Flagd Setup ---
         FLAG_KEY = "quickstart-flag"
         DEFAULT_FLAG_VALUE = False
         
         # Check for necessary environment variable
         provider_id = os.environ.get("FLAGD_SOURCE_PROVIDER_ID")
         if not provider_id:
           log.critical("FATAL: FLAGD_SOURCE_PROVIDER_ID environment variable not set.")
           sys.exit("FLAGD_SOURCE_PROVIDER_ID not set") # Exit if critical config is missing
         
         log.info(f"Initializing OpenFeature provider for ID: {provider_id}")
         
         def add_x_goog_request_params_header(config_name):
           return lambda context, callback: callback([("x-goog-request-params", f'name={config_name}')], None)
         
         try:
           # Configure gRPC credentials for Google Cloud service
           configservice_credentials = grpc.composite_channel_credentials(
               grpc.ssl_channel_credentials(),
               grpc.metadata_call_credentials(
                   google.auth.transport.grpc.AuthMetadataPlugin(
                       google.auth.default()[0], # Get just the credentials from the tuple
                       google.auth.transport.requests.Request()
                   )
               ),
               grpc.metadata_call_credentials(
                   add_x_goog_request_params_header(provider_id)
               )
           )
         
           # Set up the Flagd provider to connect to SaaS Config service
           # Using IN_PROCESS resolver type as recommended for direct gRPC connection
           provider = FlagdProvider(
               resolver_type=ResolverType.IN_PROCESS,
               host="saasconfig.googleapis.com",
               port=443,
               sync_metadata_disabled=True, # Important when using IN_PROCESS with direct service
               provider_id=provider_id,
               channel_credentials=configservice_credentials
           )
           api.set_provider(provider)
           client = api.get_client()
         
           initial_flag_value = client.get_boolean_value(FLAG_KEY, DEFAULT_FLAG_VALUE)
           log.info(f"***** STARTUP FLAG CHECK ***** Flag '{FLAG_KEY}' evaluated to: {initial_flag_value}")
         
         except Exception as e:
           log.critical(f"FATAL: Failed to initialize OpenFeature provider: {e}", exc_info=True)
           # Depending on the desired behavior, you might exit or let Flask start
           # but log the critical failure. Exiting might be safer in production.
           sys.exit(f"Provider initialization failed: {e}")
         
         # --- Flask Routes ---
         @app.route('/')
         def home():
           """Endpoint to check the feature flag's value."""
           log.info(f"Request received for flag: {FLAG_KEY}")
           try:
               # Get the flag value. Use the client initialized earlier.
               # The default value (DEFAULT_FLAG_VALUE) is returned if the flag isn't found
               # or if the provider isn't ready/errors occur during evaluation.
               flag_value = client.get_boolean_value(FLAG_KEY, DEFAULT_FLAG_VALUE)
               log.info(f"Evaluated flag '{FLAG_KEY}': {flag_value}")
               return jsonify({
                   "flag_key": FLAG_KEY,
                   "value": flag_value,
               })
           except Exception as e:
               log.error(f"Error evaluating flag '{FLAG_KEY}': {e}", exc_info=True)
               # Return an error response but keep the server running
               return jsonify({
                   "error": f"Failed to evaluate flag {FLAG_KEY}",
                   "details": str(e),
               }), 500
         
         if __name__ == '__main__':
           port = int(os.environ.get('PORT', 8080))
           log.info(f"Starting Flask server on port {port}")
           app.run(host='0.0.0.0', port=port)
         

This Python script demonstrates how to access feature flags within your application running as a Docker image on an App Lifecycle Manager unit. It uses standard OpenFeature principles to integrate with the App Lifecycle Manager feature flag config service (`saasconfig.googleapis.com`).

  3. Create a text file named `requirements.txt` in the `alm_docker` directory that contains this snippet:
         
         google-auth
         grpcio>=1.49.1,<2.0.0dev
         openfeature-sdk==0.8.0
         openfeature-provider-flagd==0.2.2
         requests 
         typing_extensions
         Flask>=2.0
         

  4. Append the `Dockerfile` in the `alm_docker` directory with:
         
         FROM python:3.11-slim
         
         WORKDIR /app
         
         COPY requirements.txt .
         
         RUN pip install --no-cache-dir -r requirements.txt
         COPY flags.py .
         CMD ["python", "flags.py"]
         

  5. Run this command in your local environment to build and push the Docker image:
         
         export DOCKER_REGISTRY="us-central1-docker.pkg.dev/PROJECT_ID/flags-quickstart"
         export FULL_IMAGE_PATH="${DOCKER_REGISTRY}/flags-quickstart:latest"
         docker build -t "${FULL_IMAGE_PATH}" .
         docker push "${FULL_IMAGE_PATH}"
         

Replace:

     * PROJECT_ID: A string identifier representing your project ID.
  6. In your Docker environment, create an `alm_terraform` directory.

  7. In `alm_terraform`, create these files:

`main.tf`
         
         locals {
           config_path = "projects/${var.system_unit_project}/locations/${var.system_unit_location}/featureFlagsConfigs/${var.system_unit_name}"
           docker_image_path = "${var.system_unit_location}-docker.pkg.dev/${var.system_unit_project}/${var.docker_repo_name}/${var.docker_tag}"
         }
         
         provider "google" {
           project = var.system_unit_project
           region  = var.system_unit_location
         }
         
         resource "google_cloud_run_service" "flags_quickstart_service" {
           name     = var.cloud_run_service_name
           location = var.system_unit_location
           project  = var.system_unit_project
         
           template {
             spec {
               containers {
                 image = local.docker_image_path 
         
                 env {
                   name  = "FLAGD_SOURCE_PROVIDER_ID"
                   value = local.config_path
                 }
               }
               service_account_name = var.actuation_sa
             }
           }
         }
         

`variables.tf`
         
         variable "actuation_sa" {
           description = "Actuation SA"
           type        = string
         }
         
         variable "system_unit_project" {
           description = "Project id - variable set by App Lifecycle Manager"
           type        = string
         }
         
         variable "system_unit_location" {
           description = "Location - variable set by App Lifecycle Manager"
           type        = string
         }
         
         variable "system_unit_name" {
           description = "Unit name- variable set by App Lifecycle Manager"
           type = string
         }
         
         variable "docker_repo_name" {
           description = "The name of the Artifact Registry repository where the Docker image is stored."
           type        = string
           default     = "flags-quickstart"
         }
         
         variable "docker_tag" {
           description = "The tag of the Docker image to deploy."
           type        = string
           default     = "flags-quickstart:latest"
         }
         
         variable "cloud_run_service_name" {
           description = "Name for the Cloud Run service to be created."
           type        = string
           default     = "saas-flags-quickstart-svc"
         }
         

  8. In the `alm_terraform` directory, run this command to package the Terraform blueprint files:
         
         zip terraform-files.zip main.tf variables.tf
         




## Use the application blueprint to create a unit

After you've created an application blueprint that utilizes feature flags, you need to create a App Lifecycle Manager unit kind (`flags-unit-kind`), and then create a unit of this kind (`flags-quickstart-unit`).

For more information about units and unit kinds, see [Model and package units of a deployment](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering).

To use the application blueprint to create a unit, follow these gcloud CLI steps:

  1. To package your Terraform configuration as an OCI image (blueprint), create a file named `Dockerfile` in your Terraform directory:
         
         # syntax=docker/dockerfile:1-labs
         FROM scratch
         COPY --exclude=Dockerfile --exclude=.git --exclude=.gitignore . /
         

  2. Build and push `Dockerfile` to your Artifact Registry repository:
         
         IMAGE_NAME="us-central1-docker.pkg.dev/PROJECT_ID/flags-quickstart/flags-quickstart-blueprint:latest"
         ENGINE_TYPE=inframanager
         ENGINE_VERSION=1.5.7
         
         docker buildx build -t $IMAGE_NAME \
           --push \
           --annotation "com.easysaas.engine.type=$ENGINE_TYPE" \
           --annotation "com.easysaas.engine.version=$ENGINE_VERSION" \
           --provenance=false .
         

Replace:

     * PROJECT_ID: A string identifier representing your project ID.
  3. Create `flags-unit-kind` and `flags-release` resource:
         
         # Create unit kind
         gcloud beta app-lifecycle-manager unit-kinds create flags-unit-kind \
           --project=PROJECT_ID \
           --location=global \
           --saas=flags-quickstart-saas-offering
         
         # Create release referencing the Blueprint image
         gcloud beta app-lifecycle-manager releases create flags-release \
           --project=PROJECT_ID \
           --location=global \
           --unit-kind=flags-unit-kind \
           --blueprint-package=$IMAGE_NAME
         

Replace:

     * PROJECT_ID: A string identifier representing your project ID.
  4. Create the `flags-quickstart-unit` unit:
         
         gcloud beta app-lifecycle-manager units create flags-quickstart-unit \
           --project=PROJECT_ID \
           --location=us-central1 \
           --unit-kind=flags-unit-kind \
           --management-mode=user
         

Replace:

     * PROJECT_ID: A string identifier representing your project ID.



## Create and provision a feature flag

Before a App Lifecycle Manager feature flag can be utilized by your provisioned unit, you must create the feature flag resource and initiate a rollout to propagate the configuration to the unit.

Run the commands to create and provision the `quickstart-flag` feature flag:

  1. In your environment, define these variables:
         
         export FLAG_ID="quickstart-flag"
         export FLAG_KEY="quickstart-flag"
         export SAAS_OFFERING_ID="flags-quickstart-saas-offering"
         export UNIT_KIND_ID="flags-unit-kind"
         export UNIT_ID="flags-quickstart-unit"
         export ROLLOUT_KIND_ID="flags-quickstart-rollout-kind"
         export ROLLOUT_ID="flags-quickstart-rollout"
         

  2. Create the feature flag resource:
         
         gcloud beta app-lifecycle-manager flags create ${FLAG_ID} \
           --project=${PROJECT_ID} \
           --key=${FLAG_KEY} \
           --flag-value-type=BOOL \
           --location=global \
           --unit-kind=${UNIT_KIND_ID}
         

  3. Create a revision:
         
         export FLAG_REVISION_ID="${FLAG_ID}-rev1"
         gcloud beta app-lifecycle-manager flags revisions create ${FLAG_REVISION_ID} \
           --project=${PROJECT_ID} \
           --flag=${FLAG_ID} \
           --location=global
         

  4. Create a release:
         
         export FLAG_RELEASE_ID="${FLAG_ID}-rel1"
         gcloud beta app-lifecycle-manager flags releases create ${FLAG_RELEASE_ID} \
           --project=${PROJECT_ID} \
           --flag-revisions=${FLAG_REVISION_ID} \
           --unit-kind=${UNIT_KIND_ID} \
           --location=global
         

  5. Create a rollout kind:
         
         gcloud beta app-lifecycle-manager rollout-kinds create ${ROLLOUT_KIND_ID} \
           --project=${PROJECT_ID} \
           --unit-kind=${UNIT_KIND_ID} \
           --rollout-orchestration-strategy=Google.Cloud.Simple.AllAtOnce \
           --location=global
         

  6. Create the rollout:
         
         gcloud beta app-lifecycle-manager rollouts create ${ROLLOUT_ID} \
           --project=${PROJECT_ID} \
           --flag-release=${FLAG_RELEASE_ID} \
           --rollout-kind=${ROLLOUT_KIND_ID} \
           --location=global
         




You can monitor the rollout status with:
    
    
    gcloud beta app-lifecycle-manager rollouts describe ${ROLLOUT_ID} --project=${PROJECT_ID} --location=global
    

## View the flag value in your running service

After your App Lifecycle Manager unit has successfully provisioned the Cloud Run service, you can verify that your application is running and correctly evaluating the feature flag:

  1. In Google Cloud console, go to **Cloud Run** :

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Find the service named `saas-flags-quickstart-svc` in the `us-central1` region. A checkmark next to `saas-flags-quickstart-svc` indicates that it's running successfully.

  3. Click `saas-flags-quickstart-svc` to view its details.

[Go to saas-flags-quickstart-svc](https://console.cloud.google.com/run/detail/us-central1/saas-flags-quickstart-svc).

  4. Select the **Logs** tab.

     1. In the log entries, look for a message similar to the following:
            
            INFO:__main__:***** STARTUP FLAG CHECK ***** Flag 'quickstart-flag' evaluated to: false
            

This confirms that the application started, connected to the SaaS Config service, and evaluated the `quickstart-flag`.

  5. To access the public endpoint, click the **Networking** tab.

     1. Find the public **URL** listed under the **Endpoints** section.
     2. Click the URL to open it in your browser, or use a tool like `curl` to access it from your terminal (`curl YOUR_SERVICE_URL`, for example).
     3. Each time you access the URL, the service evaluates the feature flag and returns its current value in JSON format. For example:
            
            {
              "flag_key": "quickstart-flag",
              "value": false
            }
            




You have successfully deployed a Google Cloud service that reads a App Lifecycle Manager managed feature flag. You can experiment with changing the flag's value and creating a new rollout to see your application pick up the change.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Optional: Delete the project

If you deployed the solution in a new Google Cloud project, and if you no longer the project, then delete it by completing the following steps:

**Caution:** If you delete a project, all the resources in the project are permanently deleted.

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. At the prompt, type the project ID, and then click **Shut down**. 



## What's next

  * Try the [Deploy feature flags standalone quickstart](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-standalone-quickstart) to use flags independently of App Lifecycle Manager managed deployments.
  * Explore the language-specific integration guides ([Python](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-python), [Java](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-java), [Go](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-golang)).
  * Review the [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview) to learn more about App Lifecycle Manager.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
