---
url: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-standalone-quickstart/
title: Quickstart: Use feature flags Standalone \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:19.201981+00:00
---

# Quickstart: Use feature flags Standalone  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-standalone-quickstart/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use feature flags Standalone

Learn how to use App Lifecycle Manager feature flags as a standalone service to manage feature availability in your applications, even if those applications are not deployed or managed by App Lifecycle Manager.

## Introduction

This quickstart shows you how to use the robust feature flagging and controlled rollout capabilities of App Lifecycle Manager without needing to use App Lifecycle Manager for infrastructure provisioning (like deploying VMs or Cloud Run services using Terraform blueprints). This approach is ideal if you manage your application infrastructure independently, but want to **use** App Lifecycle Manager for safe feature flag management.

In this standalone approach, you will:

  1. **Model your system with lightweight App Lifecycle Manager resources:** Create App Lifecycle Manager `Units` to represent components of your existing infrastructure (e.g., a specific microservice deployment, a tenant environment, a single binary instance). These Units act solely as targets for flag configurations and do **not** involve deploying infrastructure using App Lifecycle Manager blueprints.
  2. **Define and Distribute Flags:** Use the App Lifecycle Manager API or Google Cloud console to create feature flags. Manage their lifecycle using App Lifecycle Manager `Rollouts` to ensure safe, gradual propagation of configuration changes to your modeled `Units`. This provides operational consistency and safety even when only managing flags.
  3. **Integrate with your Application:** Use the OpenFeature SDK with the `flagd` provider in your application code (running anywhere – locally, **on-premises** , self-managed cloud). Configure it to connect to the App Lifecycle Manager flag service (`saasconfig.googleapis.com`), authenticate, and identify itself **using** its corresponding `Unit` resource name to fetch the correct flag values.



This approach lets you benefit from managed, safe flag distribution without altering your existing deployment pipelines or infrastructure management tools.

App Lifecycle Manager feature flags are in **Private Preview**. Access requires allowlisting. To request access for your organization or project, [complete this form](https://forms.gle/B1Jnj8akw1MSVNq2A).

This quickstart uses a basic Python application run locally to demonstrate accessing the flags, simulating how your existing application would integrate.

## Objectives

  * Set up a new Google Cloud project or use an existing one.
  * Enable required APIs (App Lifecycle Manager and SaaS Config).
  * Grant necessary Identity and Access Management permissions for resource creation and flag reading.
  * Create minimal App Lifecycle Manager resources (App offering, Unit Kind, Unit) to model an application component _without_ deploying infrastructure.
  * Define a feature flag resource associated with the Unit Kind.
  * Create a flag rollout mechanism (Rollout Kind) defining the distribution strategy.
  * **Distribute** the initial flag configuration using an App Lifecycle Manager Rollout.
  * Run a sample Python application locally that connects to the App Lifecycle Manager flag service and evaluates the flag for the modeled Unit.
  * Update the flag value, create a new flag release, and **distribute** the change.
  * Verify the application picks up the updated flag value.



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

  4. Enable the App Lifecycle Manager and SaaS Config APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=saasservicemgmt.googleapis.com,saasconfig.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the App Lifecycle Manager and SaaS Config APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=saasservicemgmt.googleapis.com,saasconfig.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. **Install Python:** Ensure you have Python 3.7+ installed on the machine where you will run the sample application. You also need pip to install dependencies. 
         
         python --version
         
         pip --version

  15. **Authenticate gcloud for Application Default Credentials (ADC):** The local Python script uses ADC to authenticate to Google Cloud services. Sign in using your user account: 
         
         gcloud auth application-default login

  16. **Grant Application Identity Permissions:** Your application needs permission to read flag configurations from the SaaS Config service. Grant the `roles/saasconfig.viewer` role to the identity the application will use. For this quickstart using ADC locally with your user account, grant the role to your email address: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
                 --member="user:YOUR_EMAIL_ADDRESS" \
                 --role="roles/saasconfig.viewer"

Replace PROJECT_ID with your Google Cloud project ID and YOUR_EMAIL_ADDRESS with the email associated with your CLI login. **Note:** In a production scenario, your application running on Google Cloud or elsewhere would typically use a dedicated service account. You would grant the roles/saasconfig.viewer role to that service account instead of your user account. 



## Create minimal App Lifecycle Manager resources

Even though we aren't deploying infrastructure with App Lifecycle Manager, we need a few resources to organize, target, and **distribute** our flags safely. These resources represent your existing application components within App Lifecycle Manager.

**Note:** The following commands create resources in `global` and specific regions (e.g., `us-central1`). Flags are defined globally, but Units representing your application instances exist in specific regions. The rollout process replicates the global flag configuration to the relevant regions where Units exist. 

  1. **Define variables:** Set environment variables for resource names and locations.
         
         export PROJECT_ID="your-project-id"
         export SAAS_OFFERING_ID="standalone-flags-saas"
         export UNIT_KIND_ID="standalone-app-kind"
         export UNIT_ID="my-app-instance-01"
         export LOCATION_1="us-central1" # Example region where your app instance conceptually resides
         # Add more locations if your app components span multiple regions
         # export LOCATION_2="europe-west1"
         

  2. **Create an App offering:** This acts as a top-level container for your service's configuration, including flags.
         
         gcloud beta app-lifecycle-manager saas create ${SAAS_OFFERING_ID} \
             --project=${PROJECT_ID} \
             --location=global \
             --locations=name=${LOCATION_1} # Add --locations=name=${LOCATION_2} if using more regions
         
          gcloud beta app-lifecycle-manager saas create ${SAAS_OFFERING_ID} \
             --project=${PROJECT_ID} \
             --location=${LOCATION_1} \
             --locations=name=${LOCATION_1} 
         

  3. **Create a unit kind:** This defines the type of component you are modeling. Crucially, we do not provide a blueprint because we are not managing infrastructure.
         
         gcloud beta app-lifecycle-manager unit-kinds create ${UNIT_KIND_ID} \
           --project=${PROJECT_ID} \
           --location=global \
           --saas=${SAAS_OFFERING_ID}
         
         gcloud beta app-lifecycle-manager unit-kinds create ${UNIT_KIND_ID} \
           --project=${PROJECT_ID} \
           --location=${LOCATION_1} \
           --saas=${SAAS_OFFERING_ID}
         

  4. **Create a unit:** This represents a specific instance of your application.
         
         gcloud beta app-lifecycle-manager units create ${UNIT_ID} \
           --project=${PROJECT_ID} \
           --unit-kind=${UNIT_KIND_ID} \
           --location=${LOCATION_1} 
         




## Define and rollout the feature flag

Now, create the actual feature flag and use the App Lifecycle Manager rollout mechanism to make its configuration available to the units you created.

  1. **Define flag variables:**
         
         export FLAG_ID="standalone-flag-01"
         export FLAG_KEY="enable-beta-feature" 
         

  2. **Create the flag resource, revision, and release:**
         
         gcloud beta app-lifecycle-manager flags create ${FLAG_ID} \
           --project=${PROJECT_ID} \
           --key=${FLAG_KEY} \
           --flag-value-type=BOOL \
           --location=global \
           --unit-kind=${UNIT_KIND_ID} \
         
         export FLAG_REVISION_ID_1="${FLAG_ID}-rev1"
         gcloud beta app-lifecycle-manager flags revisions create ${FLAG_REVISION_ID_1} \
           --project=${PROJECT_ID} \
           --flag=${FLAG_ID} \
           --location=global
         
         export FLAG_RELEASE_ID_1="${FLAG_ID}-rel1"
         gcloud beta app-lifecycle-manager flags releases create ${FLAG_RELEASE_ID_1} \
           --project=${PROJECT_ID} \
           --flag-revisions=${FLAG_REVISION_ID_1} \
           --unit-kind=${UNIT_KIND_ID} \
           --location=global
         

  3. **Create a rollout kind:** Define the strategy for distributing flag changes.
         
         export ROLLOUT_KIND_ID="standalone-flags-rollout-kind"
         
         gcloud beta app-lifecycle-manager rollout-kinds create ${ROLLOUT_KIND_ID} \
           --project=${PROJECT_ID} \
           --unit-kind=${UNIT_KIND_ID} \
           --rollout-orchestration-strategy=Google.Cloud.Simple.AllAtOnce \
           --location=global
         

  4. **Create the rollout:** Initiate the distribution process.
         
         export ROLLOUT_ID_1="${FLAG_ID}-rollout1"
         
         gcloud beta app-lifecycle-manager rollouts create ${ROLLOUT_ID_1} \
           --project=${PROJECT_ID} \
           --flag-release=${FLAG_RELEASE_ID_1} \
           --rollout-kind=${ROLLOUT_KIND_ID} \
           --location=global
         

  5. **Monitor the rollout:** Ensure the deployment succeeds before proceeding.
         
         gcloud beta app-lifecycle-manager rollouts describe ${ROLLOUT_ID_1} \
           --project=${PROJECT_ID} \
           --location=global
         




## Configure standalone infrastructure

In a standalone setup, you manage your own application hosting (e.g., Cloud Run or GKE) and use App Lifecycle Manager purely for configuration sync. The application code remains standard across deployments; it only requires the `FLAGD_SOURCE_PROVIDER_ID` environment variable to be present at runtime to connect to the SaaS Config Service.

You can map your App Lifecycle Manager unit definitions into your standard Terraform deployment definitions by passing the constructed path as an environment variable.

  1. **Define your infrastructure:** Map the path in your deployment template (e.g., `standalone.tf`).
         
         variable "project_id" { type = string }
         variable "region"     { type = string }
         variable "unit_id"    { type = string }
         
         resource "google_cloud_run_v2_service" "standalone_app" {
           name     = "my-standalone-service"
           location = var.region
         
           template {
             containers {
               image = "us-central1-docker.pkg.dev/my-project/my-repo/my-image:latest"
         
               env {
                 name  = "FLAGD_SOURCE_PROVIDER_ID"
                 value = "projects/${var.project_id}/locations/${var.region}/featureFlagsConfigs/${var.unit_id}"
               }
             }
           }
         }
         

  2. **Define your variable values:** Provide the configuration unit parameters in an associated variable file (e.g., `terraform.tfvars`).
         
         project_id = "PROJECT_ID"
         region     = "LOCATION_1"
         unit_id    = "UNIT_ID"
         




## Integrate and run the sample application

Run an example Python application locally to connect to the App Lifecycle Manager flag service using the modeled unit configurations.

  1. **Create project directory and files:**
         
         mkdir saas_flags_standalone_app
         cd saas_flags_standalone_app
         

Create `requirements.txt`:
         
         google-auth
         grpcio>=1.49.1,<2.0.0dev
         openfeature-sdk==0.8.0
         openfeature-provider-flagd==0.2.2
         requests
         typing_extensions
         Flask>=2.0
         

Install dependencies:
         
         pip install -r requirements.txt
         

  2. **Create app.py:**
         
         import google.auth.transport.grpc
         import google.auth.transport.requests
         import grpc
         import logging
         import time
         import os
         import sys
         from flask import Flask, jsonify
         
         from openfeature import api
         from openfeature.contrib.provider.flagd import FlagdProvider
         from openfeature.contrib.provider.flagd.config import ResolverType
         
         app = Flask(__name__)
         
         logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                             format='%(asctime)s - %(levelname)s - %(message)s')
         log = logging.getLogger(__name__)
         
         FLAG_KEY = os.environ.get("FLAG_KEY", "enable-beta-feature")
         DEFAULT_FLAG_VALUE = False 
         
         # CRITICAL: Read the Unit resource name from environment variable.
         # This identifies the application instance to the flag service.
         provider_id = os.environ.get("FLAGD_SOURCE_PROVIDER_ID")
         if not provider_id:
             log.critical("FATAL: FLAGD_SOURCE_PROVIDER_ID not set.")
             sys.exit("FLAGD_SOURCE_PROVIDER_ID not set")
         
         log.info(f"Initializing OpenFeature provider for Unit: {provider_id}")
         
         def add_x_goog_request_params_header(config_name):
             return lambda context, callback: callback([("x-goog-request-params", f'name={config_name}')], None)
         
         try:
             credentials, detected_project_id = google.auth.default(
                 scopes=["https://www.googleapis.com/auth/cloud-platform"] 
             )
             auth_req = google.auth.transport.requests.Request() 
         
             configservice_credentials = grpc.composite_channel_credentials(
                 grpc.ssl_channel_credentials(), 
                 grpc.metadata_call_credentials( 
                     google.auth.transport.grpc.AuthMetadataPlugin(credentials, auth_req)
                 ),
                 grpc.metadata_call_credentials(
                     add_x_goog_request_params_header(provider_id)
                 )
             )
         
             provider = FlagdProvider(
                 resolver_type=ResolverType.IN_PROCESS,    
                 host="saasconfig.googleapis.com",         
                 port=443,                                 
                 sync_metadata_disabled=True,              
                 provider_id=provider_id,                  
                 channel_credentials=configservice_credentials 
             )
         
             api.set_provider(provider)
             client = api.get_client()
         
             time.sleep(5)
         
             initial_flag_value = client.get_boolean_value(FLAG_KEY, DEFAULT_FLAG_VALUE)
             log.info(f"***** STARTUP FLAG CHECK ***** Flag '{FLAG_KEY}' evaluated to: {initial_flag_value}")
         
         except Exception as e:
             log.critical(f"FATAL: Failed to initialize OpenFeature provider: {e}", exc_info=True)
             sys.exit(f"Provider initialization failed: {e}")
         
         @app.route('/')
         def home():
             log.info(f"Request received for endpoint '/', evaluating flag: {FLAG_KEY}")
             try:
                 flag_value = client.get_boolean_value(FLAG_KEY, DEFAULT_FLAG_VALUE)
                 log.info(f"Evaluated flag '{FLAG_KEY}': {flag_value}")
                 return jsonify({
                     "flag_key": FLAG_KEY,
                     "value": flag_value,
                     "provider_id": provider_id 
                 })
             except Exception as e:
                 log.error(f"Error evaluating flag '{FLAG_KEY}': {e}", exc_info=True)
                 return jsonify({
                     "error": f"Failed to evaluate flag {FLAG_KEY}",
                     "details": str(e),
                 }), 500
         
         if __name__ == '__main__':
             port = int(os.environ.get('PORT', 8080))
             log.info(f"Starting Flask web server on host 0.0.0.0 port {port}")
             app.run(host='0.0.0.0', port=port)
         

  3. **Run the application:**
         
         export FLAGD_SOURCE_PROVIDER_ID="projects/${PROJECT_ID}/locations/${LOCATION_1}/featureFlagsConfigs/${UNIT_ID}"
         python app.py
         

  4. **Verify the initial flag value:** Execute a check against the local endpoint in a secondary terminal.
         
         curl http://localhost:8080
         




## Update the flag and distribute the change

Modify the flag definition runtime state and distribute the update to connected targets.

  1. **Update the flag resource:**
         
         gcloud beta app-lifecycle-manager flags create ${FLAG_ID} \
             --project=${PROJECT_ID} \
             --key=${FLAG_KEY} \
             --flag-value-type=BOOL \
             --location=global \
             --unit-kind=${UNIT_KIND_ID}
         
         export FLAG_REVISION_ID_2="${FLAG_ID}-rev2"
         gcloud beta app-lifecycle-manager flags revisions create ${FLAG_REVISION_ID_2} \
           --project=${PROJECT_ID} \
           --flag=${FLAG_ID} \
           --location=global
         
         export FLAG_RELEASE_ID_2="${FLAG_ID}-rel2"
         gcloud beta app-lifecycle-manager flags releases create ${FLAG_RELEASE_ID_2} \
           --project=${PROJECT_ID} \
           --flag-revisions=${FLAG_REVISION_ID_2} \
           --unit-kind=${UNIT_KIND_ID} \
           --location=global
         

  2. **Create a new rollout for the update:**
         
         export ROLLOUT_ID_2="${FLAG_ID}-rollout2"
         
         gcloud beta app-lifecycle-manager rollouts create ${ROLLOUT_ID_2} \
           --project=${PROJECT_ID} \
           --flag-release=${FLAG_RELEASE_ID_2} \
           --rollout-kind=${ROLLOUT_KIND_ID} \
           --location=global
         

  3. **Monitor the new rollout:**
         
         gcloud beta app-lifecycle-manager rollouts describe ${ROLLOUT_ID_2} \
           --project=${PROJECT_ID} \
           --location=global 
         

  4. **Verify the change in the running application:**
         
         curl http://localhost:8080
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Press `Ctrl+C` in the terminal where `app.py` is running to stop the local Python application.
  2. Set the flag state.
  3. Create a new rollout to remove obsolete flags.
  4. After the rollout has completed and obsolete flags have been removed, delete the App Lifecycle Manager resources:
         
         gcloud beta app-lifecycle-manager rollouts delete ${ROLLOUT_ID_1} --project=${PROJECT_ID} --location=global --quiet 
         gcloud beta app-lifecycle-manager rollouts delete ${ROLLOUT_ID_2} --project=${PROJECT_ID} --location=global --quiet 
         gcloud beta app-lifecycle-manager rollout-kinds delete ${ROLLOUT_KIND_ID} --project=${PROJECT_ID} --location=global --quiet 
         gcloud beta app-lifecycle-manager flags releases delete ${FLAG_RELEASE_ID_1} --project=${PROJECT_ID} --location=global --quiet 
         gcloud beta app-lifecycle-manager flags releases delete ${FLAG_RELEASE_ID_2} --project=${PROJECT_ID} --location=global --quiet 
         gcloud beta app-lifecycle-manager flags delete ${FLAG_ID} --project=${PROJECT_ID} --location=global --quiet 
         gcloud beta app-lifecycle-manager units delete ${UNIT_ID} --project=${PROJECT_ID} --location=${LOCATION_1} --quiet 
         gcloud beta app-lifecycle-manager unit-kinds delete ${UNIT_KIND_ID} --project=${PROJECT_ID} --location=global --quiet 
         gcloud beta app-lifecycle-manager unit-kinds delete ${UNIT_KIND_ID} --project=${PROJECT_ID} --location=${LOCATION_1} --quiet 
         gcloud beta app-lifecycle-manager saas delete ${SAAS_OFFERING_ID} --project=${PROJECT_ID} --location=global --quiet 
         gcloud beta app-lifecycle-manager saas delete ${SAAS_OFFERING_ID} --project=${PROJECT_ID} --location=${LOCATION_1} --quiet 
         

  5. Delete the local directory:
         
         cd ..
         rm -rf saas_flags_standalone_app
         




## What's next

  * Read the [App Lifecycle Manager feature flags overview](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-overview) for more conceptual details.
  * Try the [Deploy feature flags quickstart](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart) to see how flags integrate tightly with App Lifecycle Manager-managed deployments.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
