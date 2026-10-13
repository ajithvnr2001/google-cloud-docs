---
url: https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-gcloud/
title: Deploy an App Engine app in the standard environment to Cloud Run \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:22.137210+00:00
---

# Deploy an App Engine app in the standard environment to Cloud Run  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Deploy an App Engine app in the standard environment to Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

**Preview — Deploy an existing App Engine app in the standard environment to Cloud Run**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide describes how to deploy your existing apps in the standard environment to [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run). The instructions are applicable for [second-generation runtimes](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule) that don't use the App Engine legacy bundled services.

The steps described in this guide don't affect your existing App Engine app's functionality or traffic flow. The newly created Cloud Run service is a replica of the App Engine service that you can test independently.

Cloud Run uses much of the same infrastructure as App Engine standard environment resulting in many similarities between the platforms. To learn more about the similarities and differences between App Engine and Cloud Run, including the benefits of migrating to Cloud Run, see the [comparison summary](https://docs.cloud.google.com/appengine/migration-center/run/compare-gae-with-run). 

To deploy to Cloud Run, choose one of the following strategies:

  * **Use the local configuration of an`app.yaml` file (recommended)**: Choose this option to build a container image directly from your local source code and deploy it to Cloud Run. This ensures that any recent local modifications to your code or configuration are included in the new deployment.

  * **Use a previously built image** : This option is useful if you don't have access to the source code. Choose this option to deploy an exact copy of a version that is already running onvApp Engine, without rebuilding the container image. This is useful if you want to verify the behavior of the active deployment without code changes.




## Before you begin

  1. Make sure that your App Engine application runs without errors. You need access to your App Engine source code if you choose to deploy using your local configuration.

  2. Enable the Cloud Run Admin API and the Artifact Registry API:

[Enable APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,artifactregistry.googleapis.com&_ga=2.109139269.1795509783.1687809390-606913076.1686784330)

  3. Configure your project and region using the following command:
         
         gcloud auth login
         gcloud config set project PROJECT_ID
         gcloud config set run/region REGION
         gcloud components update
         

Replace the following:

     * PROJECT_ID: your Google Cloud project ID.
     * REGION: the region where you want to deploy your Cloud Run service.
  4. Check for incompatible features in your application, and remove them before migrating to Cloud Run. To check your application for incompatibility without performing a migration or deployment, run the following command:
         
         gcloud beta app migrate-to-run --dry-run
         

Review the compatibility check results and make the recommended changes if required.

  5. Review the following Cloud Run differences:

     * Cloud Run uses the term `Revision`, instead of `Version`, to represent each time that you deploy changes to a specific service. Deploying your app to a service in Cloud Run for the first time creates its first revision. Each subsequent deployment of a service creates another revision. [Learn more about deploying to Cloud Run](https://docs.cloud.google.com/run/docs/deploying#service).

     * You can deploy your source code to Cloud Run using the gcloud CLI or Google Cloud console to configure and manage your app settings. Cloud Run doesn't require file-based configuration; however, [YAML configuration](https://docs.cloud.google.com/run/docs/deploying?tab=yaml#revision) is supported.

     * Every service that you deploy to Cloud Run uses the [`run.app`](https://docs.cloud.google.com/run/docs/triggering/https-request#creating_public_services) domain in the URL to access the service publicly.

     * Unlike App Engine services that are public by default, [Cloud Run services are private by default](https://docs.cloud.google.com/run/docs/authenticating/overview) and require you to configure them for public (unauthenticated) access.




### Required roles

You can choose to either create a new service account or use the same user-managed service account in Cloud Run that you are using for the standard environment. You or your administrator must grant the deployer account and the Cloud Build service account the following IAM roles.

#### Click to view required roles for the deployer account

To get the permissions that you need to build and deploy from source, ask your administrator to grant you the following IAM roles:

  * [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`) on your project
  * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on your project
  * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Cloud Run service identity



#### Click to view required roles for the Cloud Build service account

Cloud Build automatically uses the [Compute Engine default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) as the default Cloud Build service account to build your source code and Cloud Run resource, unless you override this behavior. For Cloud Build to build your sources, ask your administrator to grant [Cloud Run Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`) to the Compute Engine default service account on your project:
    
    
      gcloud projects add-iam-policy-binding PROJECT_ID \
          --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
          --role=roles/run.builder
      

Replace `PROJECT_NUMBER` with your Google Cloud project number, and `PROJECT_ID` with your Google Cloud project ID. For detailed instructions on how to find your project ID, and project number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

Granting the Cloud Run builder role to the Compute Engine default service account takes a couple of minutes to [propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Use the local configuration of an `app.yaml` file

Deploy your local App Engine configuration to Cloud Run using the Google Cloud console or the gcloud CLI. 

### Console

  1. In the Google Cloud console, go to the **App Engine** page.

[Go to App Engine](https://console.cloud.google.com/appengine)

  2. In the navigation menu, click **Migration hub** to deploy your App Engine app to Cloud Run. The **Migration hub** also lets you check your estimated savings on Cloud Run for cost estimation and recommendations.

  3. Select the service you want to migrate, and click **Check compatibility**.

  4. Select your **Service** and **Version** to see the compatibility results. The migration hub runs a compatibility checker to identify incompatible features.

  5. Review the results to verify that your app is fully compatible with Cloud Run, and click **Continue** to proceed to the **Review & Deploy** section.

  6. Copy the command in the **Deploy through gcloud** section, and run it within your project directory.

  7. Click **View deployed versions** to see your App Engine services deployed in Cloud Run.




###  gcloud 

To deploy your Cloud Run service using the local `app.yaml` file of an existing App Engine configuration, follow these steps:

  1. In your terminal, change to your source directory where the `app.yaml` file exists.

  2. Run the following command to deploy your service to Cloud Run:
         
         gcloud beta app migrate-to-run
         

This command generates the `service.yaml` file configuration for Cloud Run and saves it locally to the same directory as your `app.yaml` file. For more information, see [`gcloud beta app migrate-to-run`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-to-run).

     * When prompted `Proceed with the deployment?`, enter `Y` to build a container image from your source code, and deploy the service to Cloud Run.
  3. Visit your deployed Cloud Run service by opening the service URL in a web browser.

Optional:

     * If your `app.yaml` file is in a different directory, specify its path using the `--appyaml` flag:
           
           gcloud beta app migrate-to-run --appyaml=PATH
           

Replace PATH with the path to your `app.yaml` file.

     * To generate and export the Cloud Run `service.yaml` configuration without deploying the service, use the `--export-only` flag:
           
           gcloud beta app migrate-to-run --export-only=EXPORT_PATH
           

Replace EXPORT_PATH with the directory or path where you want to save the `service.yaml` file.




## Use a previously built image

To deploy using a previously built container image from a deployed App Engine version instead of rebuilding the container image from a local `app.yaml` file, follow these steps:

You don't need your application's source code for this deployment.

  1. Run the following command to deploy your service to Cloud Run. This command uses the container image of an active App Engine deployment and doesn't capture recent changes from your local `app.yaml` file, which might result in an outdated deployment:
         
         gcloud beta app migrate-to-run --service=SERVICE --version=VERSION --from-image
         

Replace the following:

     * SERVICE: the name of your App Engine service.
     * VERSION: the version ID of your service.

This command fetches the configuration of the specified service and version to generate the `service.yaml` file for Cloud Run. For more information, see [`gcloud beta app migrate-to-run`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-to-run).

     * When prompted with `Proceed with the deployment?`, enter `Y` to export your existing App Engine container image and deploy the service to Cloud Run.
  2. Visit your deployed Cloud Run service by opening the service URL in a web browser.

Optional:

     * To generate the Cloud Run `service.yaml` configuration without deploying the service, run the following command:
           
           gcloud beta app migrate-to-run --service=SERVICE \
               --version=VERSION \
               --from-image \
               --export-only=EXPORT_PATH
           

Replace EXPORT_PATH with the directory or path where you want to save the `service.yaml` file.




## Incompatible features

The migration command fails if your `app.yaml` file contains any of the following unsupported configurations: 

  * **Inbound services** :
        
        inbound_services:
        - warmup
        

**Solution** : Delete the `inbound_services` section from your `app.yaml` file. Cloud Run warms up instances using the container entrypoint, so you don't need to configure warmup requests. If you need to run initialization code before serving traffic, configure your service to run it at startup, before listening for requests or use [startup probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#configure-probes). You can also configure [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances) to keep instances warm.



  * **Custom error pages** :
        
        error_handlers:
         - file: default_error.html
         - error_code: over_quota
         file: over_quota.html
        

**Solution** : Delete the `error_handlers` section from your `app.yaml` file, and follow either or both of these strategies:

    * Implement error handling directly within your application code. Catch standard HTTP error codes, such as `404` or `500`, and serve your custom HTML error pages from within your application logic.
    * If you are using Cloud Load Balancing with Cloud Run, configure custom error responses at the load balancer level. This lets you serve custom error pages from Cloud Storage based on the response code from your Cloud Run service.
  * **Bundled services for second-generation runtimes** :
        
        app_engine_apis: true
        

**Solution** : Delete the `app_engine_apis` setting from your `app.yaml` file, and migrate to Google Cloud APIs or third-party alternatives instead. For more information, see [Migrating from bundled services](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services).

  * **First-generation runtimes** :
        
        runtime: python27
        

**Solution** : Upgrade your application to a [supported second-generation runtime](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule). For more information, see the [Migrating to second-generation runtimes overview](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/overview). 




## What's next

  * Understand how to [manage your Cloud Run services](https://docs.cloud.google.com/run/docs/managing/services).
  * See the Cloud Run [container runtime contract](https://docs.cloud.google.com/run/docs/container-contract) to understand the requirements and behaviors of containers in Cloud Run.
  * Learn how to store dependencies for your service requiring API keys, passwords, or other sensitive information using a [Secret Manager](https://docs.cloud.google.com/run/docs/configuring/services/secrets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
