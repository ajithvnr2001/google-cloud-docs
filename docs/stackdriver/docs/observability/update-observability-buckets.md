---
url: https://docs.cloud.google.com/stackdriver/docs/observability/update-observability-buckets/
title: Update observability buckets \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:37.630720+00:00
---

# Update observability buckets  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/update-observability-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Update observability buckets Stay organized with collections  Save and categorize content based on your preferences. 

You can update the display name, description, or Cloud Key Management Service key of an observability bucket to reflect organizational changes or rotate encryption keys.

You can't use these update operations to resolve compliance issues. For example, you can't use these operations to change the location of an observability bucket or apply a Cloud KMS key to a bucket that uses Google-default encryption.

## Effects of updating a Cloud KMS key

Updating the Cloud KMS key for an observability bucket doesn't affect stored data. That is, before the update completes, the original key encrypts new data. After the update completes, the updated key encrypts new data.

You can continue to access and view the stored data provided that the original Cloud KMS key remains [enabled](https://docs.cloud.google.com/kms/docs/key-states#enabled) and the Google Cloud Observability service account retains the [encrypter/decrypter permissions](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles).

If you disable or destroy the original Cloud KMS key, then any data written while that key was active immediately becomes **permanently inaccessible and unreadable**.

## Limitations

The following restrictions apply:

  * You can't modify the location.
  * You can't apply a Cloud KMS key to an observability bucket that uses Google-default encryption.
  * The display name must not exceed 100 encoded bytes.
  * The description must not exceed 1000 encoded bytes.
  * Data is stored for 30 days. You can omit the retention period or set it to `30`.
  * If you update the Cloud KMS key, then the location of the key must exactly match the parent location of the observability bucket.



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

  8. To get the permissions that you need to update observability buckets, ask your administrator to grant you the [Observability Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

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

Optional. If you plan to update the Cloud KMS key that the observability bucket uses, then do the following:

  1. Enable the Cloud Key Management Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  2. [Create a key ring and key](https://docs.cloud.google.com/kms/docs/creating-keys).

The location of the observability bucket must match the location of the key.

  3. Replace PROJECT_ID with your project's ID, and then run the following command:
         
         gcloud observability settings describe \
         --location=global --project=PROJECT_ID
         

The response to the preceding command lists the ID of the Google Cloud Observability service account.

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
     * service-PROJECT_NUMBER: The name of the Google Cloud Observability service account that was listed in the preceding step.
     * KMS_KEY_LOCATION: The Cloud KMS key's region.
     * KMS_KEY_RING: The Cloud KMS key ring's name.
     * KMS_KEY_NAME: The Cloud KMS key's name. It is formatted like this: `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KEY`.



## Update an observability bucket

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.
  * LOCATION: The location of the observability bucket.
  * DESCRIPTION: A description. This field is optional.
  * DISPLAY_NAME: The display name. This field is optional.
  * PROJECT_ID: The identifier of the project.



The gcloud CLI command also provides options to update the Cloud KMS key. For more information, see [`gcloud observability buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/update).

Execute the [`gcloud observability buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability buckets update BUCKET_ID \
     --location=LOCATION \
     --description="DESCRIPTION" \
     --display-name="DISPLAY_NAME" \
     --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability buckets update BUCKET_ID `
     --location=LOCATION `
     --description="DESCRIPTION" `
     --display-name="DISPLAY_NAME" `
     --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability buckets update BUCKET_ID ^
     --location=LOCATION ^
     --description="DESCRIPTION" ^
     --display-name="DISPLAY_NAME" ^
     --project=PROJECT_ID

The update command initiates a long-running operation and blocks until the operation completes. The following is an example of a response when the command is successful: 
    
    
    Request issued for: [_Trace]
    Waiting for operation [projects/my-project/locations/us/operations/operation-1790096940299-65c156c3d730f-5fbc9362-10d93b76] to complete...done.
    Updated bucket [_Trace].
    createTime: '2026-09-09T21:06:30.590367694Z'
    description: Updated bucket for storing trace data
    displayName: Updated display name
    name: projects/my-project/locations/us/buckets/_Trace
    updateTime: '2026-09-22T17:09:00.301850190Z'
    

###  Terraform 

To update the display name, the description, or the CMEK, use the Terraform resource [`google_observability_bucket`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_bucket) and set the following fields:

  * `project`: The ID of your project.
  * `location`: The location of the observability bucket. For more information, see [Locations](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
  * `bucket_id`: The ID of the observability bucket. This field must be set to `_Trace`.



You can update only the description, the display name, and the CMEK. For more information, see the documentation for the resource.

###  REST 

To update an observability bucket, send a request to [`projects.locations.buckets.patch`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets/patch).

You must specify the parent parameter, which identifies the bucket to update. This parameter has the following form:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID
    

The fields in the preceding expression have the following meanings:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The [location of the observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.



The query parameter must specify an `updateMask` field, which identifies which fields to modify. For example:

  * To update the description, use `updateMask=description`.
  * To update the Cloud KMS key and the description, use `updateMask=description,cmekSettings.kmsKey`.



The request body is a [`Bucket`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets#Bucket) object. You must populate every field specified by the update mask. Don't populate fields that you aren't updating.

For example, to update only the `description` field, you could use the following `Bucket` object:
    
    
    {
        "description": "Updated description for my observability bucket."
    }
    

The response is an [`Operation`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations.operations#Operation) object. Typically, this method takes less than a minute to complete.

Typically, to determine whether a method that returns an `Operation` object is complete, you poll the object by calling [`projects.locations.operations.get`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.operations/get) until the `Operation.done` field is set to `true`. You can then use other fields in the `Operation` structure to determine whether the method succeeded or failed.

However, the `patch` method completes quickly. Therefore, an alternative is to wait a minute and then verify the update by listing your observability buckets.

## What's next

  * [View and analyze telemetry](https://docs.cloud.google.com/stackdriver/docs/observability/query-and-view-overview)
  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets): Configure a default storage location and a default customer-managed encryption key (CMEK) for your observability buckets.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
