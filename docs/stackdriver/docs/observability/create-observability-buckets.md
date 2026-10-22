---
url: https://docs.cloud.google.com/stackdriver/docs/observability/create-observability-buckets/
title: Create observability buckets \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:50.977698+00:00
---

# Create observability buckets  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/create-observability-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Create observability buckets Stay organized with collections  Save and categorize content based on your preferences. 

You can manually create the `_Trace` observability bucket before your project receives trace data to customize its storage location and customer-managed encryption key (CMEK) settings. If your Google Cloud project ingests trace data before this bucket exists, then Google Cloud Observability automatically provisions the bucket using your project's [default settings for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

For information about how Google Cloud Observability stores data, see [Storage overview](https://docs.cloud.google.com/stackdriver/docs/observability/storage-overview).

## Interaction with organization policies

A request to create an observability bucket verifies that the command parameters comply with organization policies. For example, if an organization policy restricts resource locations, then creating a bucket fails if you specify a restricted location.

## Interaction with default settings for observability buckets

When Google Cloud Observability automatically creates an observability bucket due to ingestion of data, it uses the default settings for observability buckets that apply to the parent resource of the bucket. Those default settings might be defined in the parent or in a hierarchical ancestor of the parent, and they specify the following:

  * The storage location.
  * The Cloud KMS key to use for the stored data.



When creating an observability bucket, you **must specify a location**. Google Cloud Observability applies the Cloud KMS key defined in your default settings unless you explicitly specify a different key in your create request.

You cannot create a bucket with Google-default encryption if the applicable default settings specify a Cloud KMS key. To use Google-default encryption, ensure no Cloud KMS key is configured in your default settings.

For information about default settings for observability buckets, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

## Limitations

The following restrictions apply:

  * You must specify a [supported location](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
  * The BUCKET_ID must be `_Trace`.
  * The display name must not exceed 100 encoded bytes.
  * The description must not exceed 1000 encoded bytes.
  * Data is stored for 30 days. You must either omit the retention period or set it to `30`.
  * If you provide a Cloud KMS key, then the location of the key must exactly match the parent location of the observability bucket.
  * You can only create observability buckets in Google Cloud projects.
  * A Google Cloud project can have at most one observability bucket named `_Trace`.



## Before you begin

Configure your project and your IAM roles, and select the interface that you plan to use.

### Configure your project and roles

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  8. To get the permissions that you need to create observability buckets, ask your administrator to grant you the [Observability Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




### Configure interfaces

### gcloud

**Note** : You must use gcloud CLI version 586.0.0 or later.

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

### Configure Cloud KMS key

Optional. If you plan to create an observability bucket and to specify a Cloud KMS key, then do the following:

  1. Enable the Cloud Key Management Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  2. [Create a key ring and keys](https://docs.cloud.google.com/kms/docs/creating-keys).

The location of the observability bucket must match the location of the key.

  3. Replace PROJECT_ID with your project's ID, and then run the following command:
         
         gcloud observability settings describe \
         --location=global --project=PROJECT_ID
         

The preceding command checks whether you've configured a default storage location. It also creates the Google Cloud Observability service account when that account doesn't exist. The command's response lists the service account's ID.

  4. Grant the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) role to the Google Cloud Observability service account.
         
         gcloud kms keys add-iam-policy-binding \
         --project=KMS_PROJECT_ID \
         --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-observability.iam.gserviceaccount.com \
         --role=roles/cloudkms.cryptoKeyEncrypterDecrypter \
         --location=KMS_KEY_LOCATION \
         --keyring=KMS_KEY_RING \
         KMS_KEY_NAME
         

Before running the preceding command, make the following replacements:

     * KMS_PROJECT_ID: The unique alphanumeric identifier, composed of your Google Cloud project name and a randomly assigned number, of the Google Cloud project running Cloud KMS. For information about getting this identifier, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * service-PROJECT_NUMBER: The name of the Observability service account that was listed in the response of the preceding step.
     * KMS_KEY_LOCATION: The Cloud KMS key's region.
     * KMS_KEY_RING: The Cloud KMS key ring's name.
     * KMS_KEY_NAME: The Cloud KMS key's name. It is formatted like this: `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY`.



## Create an observability bucket

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.
  * LOCATION: The location of the observability bucket.
  * PROJECT_ID: The identifier of the project.



The gcloud CLI command also provides options to set the display name, description, and Cloud KMS key. For more information, see [`gcloud observability buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/create).

Execute the [`gcloud observability buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/create) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability buckets create BUCKET_ID \
     --location=LOCATION --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability buckets create BUCKET_ID `
     --location=LOCATION --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability buckets create BUCKET_ID ^
     --location=LOCATION --project=PROJECT_ID

The create command initiates a long-running operation and blocks until the operation completes. The following is an example of a response when the command is successful: 
    
    
    Create request issued for: [_Trace]
    Waiting for operation [projects/my-project/locations/us/operations/operation-1775164903749-64e80c9817833-9ff804b6-c3e9cbe7] to complete...done.
    Created bucket [_Trace].
    

###  Terraform 

To create an observability bucket, use the Terraform resource [`google_observability_bucket`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_bucket) and set the following fields:

  * `project`: The ID of your project.
  * `location`: The location of the observability bucket. For more information, see [Locations](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
  * `bucket_id`: The ID of the observability bucket. This field must be set to `_Trace`.



You can also set a description and display name, and provide a CMEK. For more information, see the documentation for the resource.

###  REST 

To create an observability bucket, send a request to [`projects.locations.buckets.create`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets/create).

You must specify the parent parameter, which has the following form:
    
    
    projects/PROJECT_ID/locations/LOCATION
    

The fields in the preceding expression have the following meanings:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The [location of the observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).



The request body is a [`Bucket`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets#Bucket) object. Complete the following fields:

  * `name`: Set this field to the following:
        
        projects/PROJECT_ID/locations/LOCATION/buckets/_Trace
        

  * Optional: Provide values for the `displayName` and `description` fields.

  * Optional: Provide a CMEK. When specified, this key encrypts the stored data.

If you don't provide a CMEK, then the default settings that apply to the bucket's parent resource determine the encryption key. If the default settings specify a Cloud KMS key, then that key encrypts the stored data. Otherwise, Google-default encryption is used.




The response is an [`Operation`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations.operations#Operation) object. Poll the [`projects.locations.operations.get`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.operations/get) method until the `Operation.done` field is set to `true`. Other fields in the `Operation` structure provide information about the success or failure of the request.

## List observability buckets

You can list the observability buckets to verify that the create request completed successfully.

This section describes how to list your observability buckets. An observability bucket is the management entity for datasets, which store data.

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * LOCATION: The location of the observability buckets. To list all observability buckets, regardless of location, set the location to a hyphen (`-`).
  * PROJECT_ID: The identifier of the project..



Execute the [`gcloud observability buckets list`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/list) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability buckets list \
     --location=LOCATION --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability buckets list `
     --location=LOCATION --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability buckets list ^
     --location=LOCATION --project=PROJECT_ID

The response lists the name, description, and create time of each observability buckets. The following is an example of a response when the command is successful: 
    
    
    ---
    createTime: '2026-01-21T21:39:22.381083860Z'
    description: Bucket for storing spans from Cloud Trace.
    name: projects/my-project/locations/us/buckets/_Trace
    

###  Terraform 

You can't use Terraform to list observability buckets.

###  REST 

To list the observability buckets that are in your project and in a specific location, use the [`projects.locations.buckets.list`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets/list) method.

You must specify the parent parameter, which has the following form:
    
    
    projects/PROJECT_ID/locations/LOCATION
    

The fields in the previous expression have the following meanings:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The [location of the observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations). If you set LOCATION to a hyphen (`-`), then all observability buckets in your project are listed.



The response is an array of [`Bucket`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets#Bucket) objects. For each object, the value of the `name` field has the following format:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID
    
    

The following shows a sample response:
    
    
    {
      "buckets": [
        {
          "name": "projects/my-project/locations/us/buckets/_Trace",
          "description": "Trace Bucket",
          "createTime": "2025-01-01T15:42:30.988919645Z",
          "updateTime": "2025-02-04T15:42:30.988919645Z",
          "retentionDays": 30
        }
      ]
    }
    

You can use the Observability API to get more information about the bucket whose ID is BUCKET_ID. For example, you can list the datasets on that bucket, and the views and links on each dataset. For more information, see the [Observability API reference documentation](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest).

## What's next

  * [View and analyze telemetry](https://docs.cloud.google.com/stackdriver/docs/observability/query-and-view-overview)

  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets): Configure a default storage location and a default customer-managed encryption key (CMEK) for your observability buckets.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
