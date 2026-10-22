---
url: https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites/
title: Prepare your environment \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:39.303232+00:00
---

# Prepare your environment  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Prepare your environment Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage). 

Before you create an Image Builder pipeline, you must first prepare your Google Cloud environment. To prepare your environment, complete the following tasks:

  * Submit an onboarding request
  * Enable required Cloud APIs
  * Configure Image Builder service account
  * Configure trusted image organization policy
  * Configure VPC network and access requirements
  * Configure Artifact Registry



## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Required roles

To get the permissions that you need to prepare your environment, ask your administrator to grant you the following IAM roles on your project: 

  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
  * Project Identity and Access Management (IAM) Admin (`roles/resourcemanager.projectIamAdmin`) or Service Account Admin (`roles/iam.serviceAccountAdmin`) 
  * [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Onboarding request

Image Builder is [generally available](https://docs.cloud.google.com/products#product-launch-stages) with an allowlist. To onboard your Google Cloud project for the image customization pipeline, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team.

### Service accounts covered by the allowlist

The allowlist grants access to your project by project number. As a result, the allowlist covers only the service accounts, which include the following:

  * **User-managed service accounts** that you create in your project.
  * **Default service accounts** that Google Cloud creates in your project, such as the Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`).



The allowlist doesn't cover Google-owned service accounts, because Google Cloud creates these service accounts in Google-owned projects rather than in your project. Google-owned service accounts include the following:

  * **Service agents** , such as `service-PROJECT_NUMBER@gcp-sa-SERVICE.iam.gserviceaccount.com`.
  * **The legacy Cloud Build service account** (`PROJECT_NUMBER@cloudbuild.gserviceaccount.com`), which Google owns and manages.



For more information about these service account types, see [Types of service accounts](https://docs.cloud.google.com/iam/docs/service-account-types).

If a build runs as a Google-owned service account, then the build can't read the Image Builder orchestrator container images in Artifact Registry. As a result, the pipeline fails with a permission-denied error. To avoid this failure, run your pipelines as a user-managed service account that you create in your project and specify that service account when you submit a build. For more information, see Configure Image Builder service account and [Default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).

## Enable APIs

Image Builder requires that you enable the Compute Engine, Cloud Build, Artifact Registry, Service Usage, and Resource Manager APIs. To enable the APIs by using the Google Cloud console or the Google Cloud CLI, select one of the following tabs:

###  Console 

Enable the Compute Engine, Cloud Build, Artifact Registry, Service Usage, and Cloud Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,cloudbuild.googleapis.com,artifactregistry.googleapis.com,serviceusage.googleapis.com,cloudresourcemanager.googleapis.com)

###  gcloud 

Enable the Compute Engine, Cloud Build, Artifact Registry, Service Usage, and Cloud Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable compute.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com serviceusage.googleapis.com cloudresourcemanager.googleapis.com

## Configure Image Builder service account

The Image Builder orchestrator runs using a user-managed service account. When you run an image build pipeline, Cloud Build attaches this service account to temporary worker VM and test VM instances to perform customization and validation actions. This service account needs the following roles:

  * **Compute Admin** (`roles/compute.admin`): manages VM instances, persistent disks, and guest OS images.
  * **Service Account User** (`roles/iam.serviceAccountUser`): allows Cloud Build to attach the service account to the ephemeral worker and test VM instances.
  * **Storage Admin** (`roles/storage.admin`): reads and writes temporary build artifacts and logs in the Cloud Storage `workdir` staging bucket.
  * **Logging Log Writer** (`roles/logging.logWriter`): writes execution logs to Cloud Logging.
  * **Service Usage Viewer** (`roles/serviceusage.serviceUsageViewer`): checks project service states during pipeline execution.
  * **Cloud Build Editor** (`roles/cloudbuild.builds.editor`): triggers and runs Cloud Build jobs and exports images.
  * (Optional) **Artifact Registry Admin** (`roles/artifactregistry.admin`): uploads generated OS image tar files to Artifact Registry.



You can use an existing service account or create a new dedicated service account for your build pipeline. Use a service account that resides in your project. Don't run your pipelines as a Google-owned service account, such as the legacy Cloud Build service account, because the Image Builder allowlist doesn't cover these service accounts. For more information, see Service accounts covered by the allowlist and [Default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).

To create a new dedicated service account and grant the required roles by using either the Google Cloud console or the gcloud CLI, select one of the following tabs:

###  Console 

Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  1. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
  2. Select your project. 
  3. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

  4. Click **Create and continue**. 
  5. Grant the following roles to the service account: **Compute Engine > Compute Admin, Service Accounts > Service Account User, Cloud Storage > Storage Admin, Cloud Logging > Logs Writer, Service Usage > Service Usage Viewer, Cloud Build > Cloud Build Editor, Artifact Registry > Artifact Registry Admin**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
  6. Click **Continue**. 
  7. In the **Service account users role** field, enter the identifier for the principal that will attach the service account to other resources, such as Compute Engine instances. 

This is typically the email address for a Google Account.

  8. Click **Done** to finish creating the service account. 




###  gcloud 

  1. Create a service account for your build pipeline:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
             --display-name="Image Builder Service Account"
         

  2. Grant the required roles (`roles/compute.admin`, `roles/iam.serviceAccountUser`, `roles/storage.admin`, `roles/logging.logWriter`, `roles/serviceusage.serviceUsageViewer`, and `roles/cloudbuild.builds.editor`) to your service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role="roles/compute.admin"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role="roles/iam.serviceAccountUser"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role="roles/storage.admin"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role="roles/logging.logWriter"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role="roles/serviceusage.serviceUsageViewer"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role="roles/cloudbuild.builds.editor"
         

  3. Optional: Grant the optional role (`roles/artifactregistry.admin`) to your service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role="roles/artifactregistry.admin"
         




Replace the following:

  * `SERVICE_ACCOUNT_NAME`: the name of the build service account to create. For example, `custom-builder-sa`.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `SERVICE_ACCOUNT_EMAIL`: the email address of your build service account.



## Configure trusted image organization policy

Because Image Builder internally uses standard Compute Engine image import and export tools during build execution, your project's trusted image policy (`compute.trustedImageProjects`) must explicitly allow images from the following project:

  * `projects/compute-image-import`



If your organization policy restricts this project, the image export phase fails.

To update your organization policy:

  1. In your organization policy for the `compute.trustedImageProjects` constraint, add `projects/compute-image-import` to your list of allowed publishers.
  2. For detailed instructions on configuring organization policy constraints, see [Setting up trusted image policies](https://docs.cloud.google.com/compute/docs/images/restricting-image-access) and [Export a custom image to Cloud Storage](https://docs.cloud.google.com/compute/docs/images/export-image).



## Configure VPC network and access requirements

During build and validation phases, Image Builder provisions temporary worker and test VMs in your Google Cloud project. By default, Image Builder connects instances to your `default` VPC network and assigns ephemeral external IP addresses.

If you specify a custom `network` or `subnetwork`, or configure `externalIP: none` in your [`imagebuilder.yaml`](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema#infrastructureconfig) recipe file:

  * **Private Google Access and Cloud NAT:** If worker or test VMs are configured with `externalIP: none` (no external IP), your VPC subnetwork must have [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) enabled so the instances can reach Google APIs and services (such as Cloud Storage and Artifact Registry). If your customization steps download OS packages or dependencies from external internet repositories, you must also configure [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) on the subnetwork.
  * **Firewall rules:** Make sure your VPC firewall rules allow egress traffic to Google APIs and necessary software repositories. If you're planning to connect to active worker VMs for interactive debugging (`debug: true`), make sure firewall rules allow ingress on TCP port 22. If VM instances have no external IP, allow ingress from Identity-Aware Proxy (IAP) IP range `35.235.240.0/20` for [TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding).



## Configure Artifact Registry

To store and manage your custom OS images, security metadata, and SLSA build provenance attestations, you must set up a generic repository in Artifact Registry. Storing your images in Artifact Registry lets you maintain a secure, immutable record of published images.

When you configure an Artifact Registry destination, Image Builder performs the following steps:

  * Exports the finalized VM boot disk as a standard tar file (`.tar.gz`).
  * Uploads the tar file to your generic repository in Artifact Registry.
  * Generates and signs SLSA build provenance attestations for the artifact to link it to the source metadata.
  * Registers the production-ready Compute Engine image with Compute Engine by using the Artifact Registry tar file URI as the template source.



To configure a generic Artifact Registry, complete the following tasks:

  1. Ensure the service account that is used to run the Image Builder pipeline has the **Artifact Registry Admin** role (`roles/artifactregistry.admin`) on the repository or project level. For detailed instructions, see Configure Image Builder service account.

  2. Create a repository of format `generic`. To create your repository, run the [`gcloud artifacts repositories create` command](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create):
         
         gcloud artifacts repositories create REPOSITORY_NAME \
             --repository-format=generic \
             --location=REPOSITORY_LOCATION
         

Replace the following placeholders:

     * `REPOSITORY_NAME`: a name for your generic repository. For example, `custom-os-images`.
     * `REPOSITORY_LOCATION`: a supported region. For example, `us-central1`.



## What's next

  * [Create and manage pipelines using the Google Cloud console](https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline-console).
  * [Create and manage pipelines programmatically](https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline).
  * Learn how to define customization recipes in the [Customization recipe schema](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema).
  * Review the [Build configuration (`cloudbuild.yaml`) file](https://docs.cloud.google.com/compute/docs/images/image-builder/build-configuration-schema) structure.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
