---
url: https://docs.cloud.google.com/healthcare-api/docs/permissions-healthcare-api-gcp-products/
title: Managing permissions between the Cloud Healthcare API and other Google Cloud products \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:41.071347+00:00
---

# Managing permissions between the Cloud Healthcare API and other Google Cloud products  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/permissions-healthcare-api-gcp-products/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Managing permissions between the Cloud Healthcare API and other Google Cloud products Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Healthcare API does not have automatic access to other Google Cloud resources in your project, such as Cloud Storage buckets and BigQuery datasets. When accessing these resources, the Cloud Healthcare API uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) called the **Cloud Healthcare Service Agent**.

To perform operations such as notifying Pub/Sub topics of changes, importing data from Cloud Storage buckets, exporting data to BigQuery datasets, and so on, you must first grant the service account the Identity and Access Management (IAM) permissions necessary to access the resources outside of the Cloud Healthcare API. This page describes which permissions are required for various operations, and how to grant them.

To learn more about using IAM to configure permissions within the Cloud Healthcare API, see [Access control](https://docs.cloud.google.com/healthcare-api/docs/access-control).

## The Cloud Healthcare Service Agent

The **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts) is automatically created after you enable the Cloud Healthcare API. Its member name is `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`. To find the PROJECT_NUMBER for your Google Cloud project, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

You can view detailed information about the **Cloud Healthcare Service Agent** service account, such as the roles it has been granted, on the [Identity and Access Management page](https://console.cloud.google.com/iam-admin/iam) in Google Cloud console.

To learn more about the **Cloud Healthcare Service Agent** and its interaction with Identity and Access Management (IAM) roles and permissions, see [Access control](https://docs.cloud.google.com/healthcare-api/docs/access-control#cloud_healthcare_service_agent).

## Dataset CMEK permissions

You can use a customer-managed encryption key (CMEK) when [creating a Cloud Healthcare API dataset](https://docs.cloud.google.com/healthcare-api/docs/cmek). To let the **Cloud Healthcare Service Agent** service account encrypt and decrypt objects using the CMEK key, grant the service account the [CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) role.

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin)

  2. Select the check_box_outline_blank **Include Google-provided role grants** checkbox.

  3. Ensure the **View by principals** tab is selected. Locate the row containing the **Cloud Healthcare Service Agent** service account, and click edit **Edit principal** in that row. The **Edit permissions** pane is displayed.

  4. Click add **Add another role**.

  5. From the **Select a role** drop-down menu, search for and then click **CryptoKey Encrypter/Decrypter**.

  6. Click **Save**.




## DICOM, FHIR, and HL7v2 store Pub/Sub permissions

Changes within DICOM, FHIR, and HL7v2 stores can be sent to a [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) topic. For more information, see [Using Cloud Pub/Sub for Notifications](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub).

The methods within these stores require additional permissions on the **Cloud Healthcare Service Agent** service account to publish changes to a Pub/Sub topic.

Use the Google Cloud console or the gcloud CLI to add the `pubsub.publisher` role to your project's service account:

### Console

  1. Make sure that you have [enabled the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest#before-you-begin).
  2. On the [IAM page](https://console.cloud.google.com/iam-admin/) in Google Cloud console, verify that the role **Healthcare Service Agent** appears in the **Role** column for the **Cloud Healthcare Service Agent** service account. The service account identifier is `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`.
  3. In the **Inheritance** column that matches the role, click the pencil icon. The **Edit permissions** pane opens.
  4. Click **Add another role** and then search for the **Pub/Sub Publisher** role.
  5. Select the role and then click **Save**. The `pubsub.publisher` role is added to the service account.



### gcloud

To add the service account permissions, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. To find the PROJECT_ID and PROJECT_NUMBER, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/pubsub.publisher

### Configure Pub/Sub permissions between projects

To publish Pub/Sub notifications to a topic in another project, grant the **Cloud Healthcare Service Agent** service account the `pubsub.publisher` role on the topic. For more information, see [Control access through the Google Cloud console](https://docs.cloud.google.com/pubsub/docs/access-control#console) and [Control access through the IAM API](https://docs.cloud.google.com/pubsub/docs/access-control#api).

For an example of publishing Pub/Sub notifications between projects, see [Sample use case: cross-project communication](https://docs.cloud.google.com/pubsub/docs/access-control#sample_use_case_cross-project_communication).

## DICOM store Cloud Storage permissions

The [`projects.locations.datasets.dicomStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/import) and [`projects.locations.datasets.dicomStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export) methods require additional permissions on the **Cloud Healthcare Service Agent** service account to import data from and export data to Cloud Storage.

### Importing data from Cloud Storage

You can use Google Cloud console or the gcloud CLI to add the required `storage.objectViewer` role to your project's service account. 

### Console

  1. Make sure that you have [enabled the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest#before_you_begin).
  2. On the [IAM page](https://console.cloud.google.com/iam-admin/) in Google Cloud console, verify that the role **Healthcare Service Agent** appears in the **Role** column for the Cloud Healthcare Service Agent service account. The service account identifier is `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`.
  3. In the **Inheritance** column that matches the role, click the pencil icon. The **Edit permissions** pane opens.
  4. Click **Add another role** and then search for the **Storage Object Viewer** role.
  5. Select the role and then click **Save**. The `storage.objectViewer` role is then added to the service account.



### gcloud

To add the service account permissions, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. To find the PROJECT_ID and PROJECT_NUMBER, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/storage.objectViewer 

### Exporting data to Cloud Storage

You can use Google Cloud console or the gcloud CLI to add the required `storage.objectAdmin` role to your project's service account:

### Console

  1. Make sure that you have [enabled the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest#before-you-begin).
  2. On the [IAM page](https://console.cloud.google.com/iam-admin/) in Google Cloud console, verify that the role **Healthcare Service Agent** appears in the **Role** column for the Cloud Healthcare Service Agent service account. The service account identifier is `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`.
  3. In the **Inheritance** column that matches the role, click the pencil icon. The **Edit permissions** pane opens.
  4. Click **Add another role** and then search for the **Storage Object Admin** role.
  5. Select the role and then click **Save**. The `storage.objectAdmin` role is then added to the service account.



### gcloud

To add the service account permissions, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. To find the PROJECT_ID and PROJECT_NUMBER, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/storage.objectAdmin

## DICOM store BigQuery permissions

The [`projects.locations.datasets.dicomStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export) method requires additional permissions on the **Cloud Healthcare Service Agent** service account to export DICOM metadata to BigQuery. You must also grant `WRITER` access for the BigQuery dataset to the **Cloud Healthcare Service Agent** ' service account.

### Granting permissions to the Cloud Healthcare Service Agent service account

You can use the Google Cloud console or the gcloud CLI to add the required `bigquery.dataEditor` and `bigquery.jobUser` roles to your project's service account.

### Console

  1. Make sure that you have [enabled the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest#before_you_begin).
  2. On the [IAM page](https://console.cloud.google.com/iam-admin/) in Google Cloud console, verify that the role **Healthcare Service Agent** appears in the **Role** column for the Cloud Healthcare Service Agent service account. The service account identifier is `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`.
  3. In the **Inheritance** column that matches the role, click the pencil icon. The **Edit permissions** pane opens.
  4. Click **Add another role** and then search for the **BigQuery Data Editor** and **BigQuery Job User** roles.
  5. Select each role and then click **Save**. The `bigquery.dataEditor` and `bigquery.jobUser`roles are then added to the service account.



### gcloud

To add the service account permissions, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. To find the PROJECT_ID and PROJECT_NUMBER, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  1. Grant the `roles/bigquery.dataEditor` role:

Before using any of the command data below, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * PROJECT_NUMBER: the number of your Google Cloud project

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/bigquery.dataEditor

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID `
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com `
        --role=roles/bigquery.dataEditor

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com ^
        --role=roles/bigquery.dataEditor

You should receive a response similar to the following:
    
    Updated IAM policy for project [PROJECT_ID].
    bindings:
    ...
    - members:
      - serviceAccount:service-NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com
      role: roles/bigquery.dataEditor
    ...
    etag: ETAG
    version: VERSION
    

  2. Grant the `roles/bigquery.jobUser` role:

Before using any of the command data below, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * PROJECT_NUMBER: the number of your Google Cloud project

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/bigquery.jobUser

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID `
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com `
        --role=roles/bigquery.jobUser

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com ^
        --role=roles/bigquery.jobUser

You should receive a response similar to the following:
    
    Updated IAM policy for project [PROJECT_ID].
    bindings:
    ...
    - members:
      - serviceAccount:service-NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com
      role: roles/bigquery.jobUser
    ...
    etag: ETAG
    version: VERSION
    




### Granting `WRITER` access to the BigQuery dataset

If you have added the `bigquery.dataEditor` and `bigquery.jobUser` roles to your project's service account, you will have `WRITER` access for all BigQuery datasets. However, if you have not added these roles and you require `WRITER` access to a single BigQuery dataset, you can grant `WRITER` access just for that dataset. To grant `WRITER` access to a BigQuery dataset, complete the following steps: 

  1. Navigate to [Controlling access to a dataset](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls#controlling_access_to_a_dataset).
  2. Using one of the available methods, grant the **Cloud Healthcare Service Agent** 's email address `WRITER` access to the BigQuery dataset. (Look for the email address that ends in `@gcp-sa-healthcare.iam.gserviceaccount.com`).



For example, if your **Cloud Healthcare Service Agent** 's email address is `service-000000000000@gcp-sa-healthcare.iam.gserviceaccount.com`, and if you are using the BigQuery web UI, you would:

  1. Follow the [Console](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls#controlling_access_to_a_dataset) instructions.
  2. In the **Add principals** field, enter `service-000000000000@gcp-sa-healthcare.iam.gserviceaccount.com` and select the `bigquery.dataEditor` role.



### Exporting DICOM metadata across Google Cloud projects

To export DICOM metadata from a DICOM store in one project to a BigQuery table in a different project, you must add the source project's **Cloud Healthcare Service Agent** service account to the destination project and grant the service account the `bigquery.dataEditor` and `bigquery.jobUser` roles in the destination project.

To find the source project's **Cloud Healthcare Service Agent** service account, complete the following steps:

  1. Make sure that you have [enabled the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest#before_you_begin).
  2. On the [IAM page](https://console.cloud.google.com/iam-admin/) in Google Cloud console, verify that the role **Healthcare Service Agent** appears in the **Role** column for the **Cloud Healthcare Service Agent** service account. The service account identifier is `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`. Note this address in the source project, as it will be used in the following steps.



Add the **Cloud Healthcare Service Agent** service account from the source project to the destination project and grant the service account the required BigQuery permissions by completing the following steps:

### Console

  1. Open the destination project's [IAM page](https://console.cloud.google.com/iam-admin/) in Google Cloud console.
  2. Click **Add**.
  3. In the **New members** field, enter the address of the source project's **Cloud Healthcare Service Agent** service account.
  4. Click **Add another role** and then search for the **BigQuery Data Editor** and **BigQuery Job User** roles.
  5. Select the role and then click **Save**. The source project's **Cloud Healthcare Service Agent** service account now has `bigquery.dataEditor` and `bigquery.jobUser` roles on the destination project.



### gcloud

To add the **Cloud Healthcare Service Agent** service account from the source project to the destination project and grant the service account the required BigQuery permissions, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. To find the project ID and project number for your source and destination projects, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
    
    
    gcloud projects add-iam-policy-binding DESTINATION_PROJECT_ID \
        --member=serviceAccount:service-SOURCE_PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/bigquery.dataEditor
    
    
    gcloud projects add-iam-policy-binding DESTINATION_PROJECT_ID \
        --member=serviceAccount:service-SOURCE_PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/bigquery.jobUser

Complete the steps in Granting `WRITER` access to the BigQuery dataset to allow the source project to write to the destination dataset.

## FHIR store Cloud Storage permissions

The following sections describe FHIR methods that require additional permissions on the **Cloud Healthcare Service Agent** to read from or write to Cloud Storage.

### Importing FHIR resources from Cloud Storage

The [`projects.locations.datasets.fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import) method requires the following permissions on the **Cloud Healthcare Service Agent** service account:

  * `storage.objects.get`
  * `storage.objects.list`



These permissions are included in the predefined `storage.objectViewer` role.

You can also add the permissions to a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles), or they might be included in other [basic roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

You can use Google Cloud console or the gcloud CLI to add the required `storage.objectViewer` role to your project's service account. 

### Console

  1. Make sure that you have [enabled the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest#before_you_begin).
  2. On the [IAM page](https://console.cloud.google.com/iam-admin/) in Google Cloud console, verify that the role **Healthcare Service Agent** appears in the **Role** column for the Cloud Healthcare Service Agent service account. The service account identifier is `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`.
  3. In the **Inheritance** column that matches the role, click the pencil icon. The **Edit permissions** pane opens.
  4. Click **Add another role** and then search for the **Storage Object Viewer** role.
  5. Select the role and then click **Save**. The `storage.objectViewer` role is then added to the service account.



### gcloud

To add the service account permissions, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. To find the PROJECT_ID and PROJECT_NUMBER, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/storage.objectViewer 

### Exporting FHIR resources to Cloud Storage

To use the [`projects.locations.datasets.fhirStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export) method requires the following permissions on the **Cloud Healthcare Service Agent** service account:

  * `storage.objects.create`
  * `storage.objects.delete`
  * `storage.objects.list`



These permissions are included in the predefined `storage.objectAdmin` role.

You can also add the permissions to a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles), or they might be included in other [basic roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

To grant the service account the `storage.objectAdmin` role, follow these steps:

### Console

  1. Ensure you [enabled the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest#before-you-begin).
  2. On the [IAM page](https://console.cloud.google.com/iam-admin/) in Google Cloud console, verify that the role **Healthcare Service Agent** appears in the **Role** column for the Cloud Healthcare Service Agent service account. The service account identifier is `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`.
  3. In the **Inheritance** column that matches the role, click the pencil icon. The **Edit permissions** pane opens.
  4. Click **Add another role** and then search for the **Storage Object Creator** role.
  5. Select the role and then click **Save**. The `storage.objectAdmin` role is then added to the service account.



### gcloud

To add the service account permissions, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. To find the PROJECT_ID and PROJECT_NUMBER, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/storage.objectAdmin

### Bulk-deleting FHIR resources

The [`projects.locations.datasets.fhirStores.bulkDelete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/bulkDelete) method requires the following permissions on the **Cloud Healthcare Service Agent** service account, depending on the fields in the request:

  * To read resource IDs from the `gcsSource` location: `storage.objects.get` and `storage.objects.list`. These permissions are included in the predefined `storage.objectViewer` role.
  * To write the list of deleted resources to the `gcsDestination` location: the permissions included in the predefined `storage.objectAdmin` role.



You can also add the permissions to a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles), or they might be included in other [basic roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

### Read filter files from Cloud Storage

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The [`projects.locations.datasets.fhirStores.rollback`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores/rollback) method requires the following permissions on the **Cloud Healthcare Service Agent** service account to read [filter files](https://docs.cloud.google.com/healthcare-api/docs/fhir-pitr#filter) from Cloud Storage:

  * `storage.objects.get`
  * `storage.objects.list`



These permissions are included in the predefined `storage.objectViewer` role.

You can also add the permissions to a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles), or they might be included in other [basic roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

To grant the `storage.objectViewer` role to the service account, follow these steps:

### Write output files to Cloud Storage

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The [`projects.locations.datasets.fhirStores.rollback`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores/rollback) method requires the following permissions on the **Cloud Healthcare Service Agent** service account to write [output files](https://docs.cloud.google.com/healthcare-api/docs/fhir-pitr#filter) to Cloud Storage:

  * `storage.objects.create`
  * `storage.objects.delete`
  * `storage.objects.get`
  * `storage.objects.list`



These permissions are included in the predefined `storage.objectAdmin` role.

You can also add the permissions to a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles), or they might be included in other [basic roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

To grant the `storage.objectAdmin` role to the service account, follow these steps:

## FHIR store BigQuery permissions

The [`projects.locations.datasets.fhirStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export) method requires additional permissions on the **Cloud Healthcare Service Agent** service account to export FHIR resources to BigQuery. You must also grant `WRITER` access for the BigQuery dataset to the **Cloud Healthcare Service Agent** ' service account.

### Granting permissions to the Cloud Healthcare Service Agent service account

### Console

  1. Make sure that you have [enabled the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest#before_you_begin).
  2. On the [IAM page](https://console.cloud.google.com/iam-admin/) in Google Cloud console, verify that the role **Healthcare Service Agent** appears in the **Role** column for the Cloud Healthcare Service Agent service account. The service account identifier is `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`.
  3. In the **Inheritance** column that matches the role, click the pencil icon. The **Edit permissions** pane opens.
  4. Click **Add another role** and then search for the **BigQuery Data Editor** and **BigQuery Job User** roles.
  5. Select each role and then click **Save**. The `bigquery.dataEditor` and `bigquery.jobUser`roles are then added to the service account.



### gcloud

To add the service account permissions, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. To find the PROJECT_ID and PROJECT_NUMBER, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  1. Grant the `roles/bigquery.dataEditor` role:

Before using any of the command data below, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * PROJECT_NUMBER: the number of your Google Cloud project

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/bigquery.dataEditor

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID `
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com `
        --role=roles/bigquery.dataEditor

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com ^
        --role=roles/bigquery.dataEditor

You should receive a response similar to the following:
    
    Updated IAM policy for project [PROJECT_ID].
    bindings:
    ...
    - members:
      - serviceAccount:service-NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com
      role: roles/bigquery.dataEditor
    ...
    etag: ETAG
    version: VERSION
    

  2. Grant the `roles/bigquery.jobUser` role:

Before using any of the command data below, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * PROJECT_NUMBER: the number of your Google Cloud project

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/bigquery.jobUser

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID `
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com `
        --role=roles/bigquery.jobUser

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com ^
        --role=roles/bigquery.jobUser

You should receive a response similar to the following:
    
    Updated IAM policy for project [PROJECT_ID].
    bindings:
    ...
    - members:
      - serviceAccount:service-NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com
      role: roles/bigquery.jobUser
    ...
    etag: ETAG
    version: VERSION
    




### Granting `WRITER` access to the BigQuery dataset

If you have added the `bigquery.dataEditor` and `bigquery.jobUser` roles to your project's service account, you will have `WRITER` access for all BigQuery datasets. However, if you have not added these roles and you require `WRITER` access to a single BigQuery dataset, you can grant `WRITER` access just for that dataset. To grant `WRITER` access to a BigQuery dataset, complete the following steps: 

  1. Navigate to [Controlling access to a dataset](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls#controlling_access_to_a_dataset).
  2. Using one of the available methods, grant the **Cloud Healthcare Service Agent** 's email address `WRITER` access to the BigQuery dataset. (Look for the email address that ends in `@gcp-sa-healthcare.iam.gserviceaccount.com`).



For example, if your **Cloud Healthcare Service Agent** 's email address is `service-000000000000@gcp-sa-healthcare.iam.gserviceaccount.com`, and if you are using the BigQuery web UI, you would:

  1. Follow the [Console](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls#controlling_access_to_a_dataset) instructions.
  2. In the **Add principals** field, enter `service-000000000000@gcp-sa-healthcare.iam.gserviceaccount.com` and select the `bigquery.dataEditor` role.



## HL7v2 store Cloud Storage permissions

The [`projects.locations.datasets.hl7V2Stores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/import) and [`projects.locations.datasets.hl7V2Stores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/export) methods require additional permissions on the **Cloud Healthcare Service Agent** service account to import HL7v2 messages from and export HL7v2 messages to Cloud Storage.

Determine the permissions that the service account requires based on the actions that the application performs:

  * If the application imports HL7v2 messages from Cloud Storage to an HL7v2 store, the service account requires the `storage.objects.get` and `storage.objects.list` permissions, which are included in the `storage.objectViewer` role.
  * If the application exports HL7v2 messages from an HL7v2 store to Cloud Storage, the service account requires the `storage.objects.create`, `storage.objects.delete`, and `storage.objects.list` permissions, which are included in the `storage.objectCreator` role.

**Note:** Granting the `storage.objectAdmin` role to a service account permits both of these actions, as well as editing objects' permissions. You might want to define your own roles which contain only the required permissions. To learn how to do so, see [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

### Importing HL7v2 messages from Cloud Storage

You can use Google Cloud console or the gcloud CLI to add the required `storage.objectViewer` role to your project's service account. 

### Console

  1. Make sure that you have [enabled the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest#before_you_begin).
  2. On the [IAM page](https://console.cloud.google.com/iam-admin/) in Google Cloud console, verify that the role **Healthcare Service Agent** appears in the **Role** column for the Cloud Healthcare Service Agent service account. The service account identifier is `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`.
  3. In the **Inheritance** column that matches the role, click the pencil icon. The **Edit permissions** pane opens.
  4. Click **Add another role** and then search for the **Storage Object Viewer** role.
  5. Select the role and then click **Save**. The `storage.objectViewer` role is then added to the service account.



### gcloud

To add the service account permissions, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. To find the PROJECT_ID and PROJECT_NUMBER, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/storage.objectViewer 

### Exporting HL7v2 messages to Cloud Storage

You can use Google Cloud console or the gcloud CLI to add the required `storage.objectCreator` role to your project's service account:

### Console

  1. Make sure that you have [enabled the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest#before-you-begin).
  2. On the [IAM page](https://console.cloud.google.com/iam-admin/) in Google Cloud console, verify that the role **Healthcare Service Agent** appears in the **Role** column for the Cloud Healthcare Service Agent service account. The service account identifier is `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`.
  3. In the **Inheritance** column that matches the role, click the pencil icon. The **Edit permissions** pane opens.
  4. Click **Add another role** and then search for the **Storage Object Creator** role.
  5. Select the role and then click **Save**. The `storage.objectCreator` role is then added to the service account.



### gcloud

To add the service account permissions, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. To find the PROJECT_ID and PROJECT_NUMBER, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/storage.objectCreator

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
