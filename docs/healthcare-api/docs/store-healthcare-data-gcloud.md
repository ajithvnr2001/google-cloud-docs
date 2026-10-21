---
url: https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-gcloud/
title: Quickstart: Store healthcare data with the Google Cloud CLI \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:10.889415+00:00
---

# Quickstart: Store healthcare data with the Google Cloud CLI  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store healthcare data with the Google Cloud CLI

This page shows you how to use the Cloud Healthcare API and the Google Cloud CLI to complete the following tasks: 

  1. Create a Cloud Healthcare API dataset.
  2. Create one of the following data stores inside the dataset:
     * Digital Imaging and Communications in Medicine (DICOM) store
     * Fast Healthcare Interoperability Resources (FHIR) store
     * Health Level Seven International Version 2 (HL7v2) store
  3. Store DICOM, FHIR, and HL7v2 data, and view DICOM metadata.



If you're only interested in working with one type of data store, you can skip directly to that section of the quickstart after completing the steps in Before you begin and Create a dataset. 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Healthcare API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable healthcare.googleapis.com

  8. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/healthcare.datasetAdmin, roles/healthcare.fhirStoreAdmin, roles/healthcare.dicomStoreAdmin, roles/healthcare.hl7V2StoreAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER&quot; --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Cloud Healthcare API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable healthcare.googleapis.com

  15. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/healthcare.datasetAdmin, roles/healthcare.fhirStoreAdmin, roles/healthcare.dicomStoreAdmin, roles/healthcare.hl7V2StoreAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER&quot; --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.




## Create a dataset

_Datasets_ contain data stores, and data stores contain healthcare data. To use the Cloud Healthcare API, you must create at least one dataset. 

The following sample shows how to create a dataset named `my-dataset` in the `us-central1` region. You use the dataset throughout this quickstart to create DICOM stores, FHIR stores, and HL7v2 stores.

### gcloud

Create a dataset using the [`gcloud healthcare datasets create`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/datasets/create) command.

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare datasets create my-dataset \
      --project=PROJECT_ID \
      --location=us-central1

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare datasets create my-dataset `
      --project=PROJECT_ID `
      --location=us-central1

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare datasets create my-dataset ^
      --project=PROJECT_ID ^
      --location=us-central1

You should receive a response similar to the following:

#### Response
    
    
    Create request issued for: [my-dataset]
    Created dataset [my-dataset].
    

To complete this quickstart, choose from one of the following sections:

  * Store and view a DICOM instance
  * Store FHIR resources
  * Store an HL7v2 message



## Store and view a DICOM instance

This section shows how to complete the following tasks:

  1. Create a DICOM store.
  2. Import a DICOM instance from a public Cloud Storage bucket into the DICOM store.
  3. View the DICOM instance's metadata.



The Cloud Healthcare API implements the [DICOMweb](https://www.dicomstandard.org/using/dicomweb) standard to store and access medical imaging data.

### Create a DICOM store

DICOM stores exist inside datasets and contain DICOM instances. The following sample shows how to create a DICOM store named `my-dicom-store`.

### gcloud

Create a DICOM store using the [`gcloud healthcare dicom-stores create`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/create) command.

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores create my-dicom-store \
      --project=PROJECT_ID \
      --dataset=my-dataset \
      --location=us-central1

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores create my-dicom-store `
      --project=PROJECT_ID `
      --dataset=my-dataset `
      --location=us-central1

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores create my-dicom-store ^
      --project=PROJECT_ID ^
      --dataset=my-dataset ^
      --location=us-central1

You should receive a response similar to the following:

#### Response
    
    
    Created dicomStore [my-dicom-store].

### Import a DICOM instance

Sample DICOM data is available in the `gs://gcs-public-data--healthcare-nih-chest-xray` Cloud Storage bucket.

### gcloud

Import the [`gs://gcs-public-data--healthcare-nih-chest-xray/dicom/00000001_000.dcm`](https://console.cloud.google.com/storage/browser/gcs-public-data--healthcare-nih-chest-xray/dicom/00000001_000.dcm) instance using the [`gcloud healthcare dicom-stores import`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/import) command.

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores import gcs my-dicom-store \
      --project=PROJECT_ID \
      --dataset=my-dataset \
      --location=us-central1 \
      --gcs-uri=gs://gcs-public-data--healthcare-nih-chest-xray/dicom/00000001_000.dcm

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores import gcs my-dicom-store `
      --project=PROJECT_ID `
      --dataset=my-dataset `
      --location=us-central1 `
      --gcs-uri=gs://gcs-public-data--healthcare-nih-chest-xray/dicom/00000001_000.dcm

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores import gcs my-dicom-store ^
      --project=PROJECT_ID ^
      --dataset=my-dataset ^
      --location=us-central1 ^
      --gcs-uri=gs://gcs-public-data--healthcare-nih-chest-xray/dicom/00000001_000.dcm

In this output:

  * `PROJECT_ID`, `us-central1`, `my-dataset`, `my-dicom-store`: the values you provided when running the command
  * `OPERATION_ID`: an identifier for the [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) provided by the Cloud Healthcare API when you import a DICOM instance. Long-running operations are returned when method calls might take a long time to complete. Importing one DICOM instance is usually a quick operation, so the output is returned almost immediately.



#### Response
    
    
    Request issued for: [my-dicom-store]
    Waiting for operation [projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/operations/OPERATION_ID] to complete...done.
    name: projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/dicomStores/my-dicom-store
    

### View DICOM instance metadata

The gcloud CLI doesn't support [DICOMweb transactions](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#chapter_10), such as viewing or retrieving instances. Instead, you can use the [DICOMweb command-line tool](https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli) from Google, which runs using Python. For information on how to set up Python on Google Cloud, see [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup).

Complete the following steps to view the DICOM instance metadata using the DICOMweb command-line tool:

  1. Install the DICOMweb command-line tool using Pip:
         
         pip install https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli/archive/v1.0.zip
         

  2. Update the `PATH` variable to include the `dcmweb` install location:
         
         export PATH="$HOME/bin:$PATH"
         

  3. View the DICOM instance's metadata:
         
         dcmweb \
           https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/dicomStores/my-dicom-store/dicomWeb \
           search instances

Replace `PROJECT_ID` with the ID of the Google Cloud project that you created or selected in Before you begin.

The output is the following. See [Attributes of the SOP Common Module](https://dicom.nema.org/medical/Dicom/current/output/html/part03.html#table_C.12-1) for the fields in the output.
         
         [
           {
             "00080016": {
               "Value": [
                 "1.2.840.10008.5.1.4.1.1.7"
               ],
               "vr": "UI"
             },
             "00080018": {
               "Value": [
                 "1.3.6.1.4.1.11129.5.5.153751009835107614666834563294684339746480"
               ],
               "vr": "UI"
             },
             "00080060": {
               "Value": [
                 "DX"
               ],
               "vr": "CS"
             },
             "00100020": {
               "Value": [
                 "1"
               ],
               "vr": "LO"
             },
             "00100040": {
               "Value": [
                 "M"
               ],
               "vr": "CS"
             },
             "0020000D": {
               "Value": [
                 "1.3.6.1.4.1.11129.5.5.111396399361969898205364400549799252857604"
               ],
               "vr": "UI"
             },
             "0020000E": {
               "Value": [
                 "1.3.6.1.4.1.11129.5.5.195628213694300498946760767481291263511724"
               ],
               "vr": "UI"
             },
             "00280010": {
               "Value": [
                 1024
               ],
               "vr": "US"
             },
             "00280011": {
               "Value": [
                 1024
               ],
               "vr": "US"
             },
             "00280100": {
               "Value": [
                 8
               ],
               "vr": "US"
             }
           }
         ]
         




After importing the DICOM instance into the Cloud Healthcare API and viewing its metadata, continue to Clean up to avoid incurring charges to your Google Cloud account for the resources used in this page.

For information on next steps, such as how to search for or retrieve DICOM images using the DICOMweb standard in the Cloud Healthcare API, see What's next.

## Store FHIR resources

**Note:** The Cloud Healthcare API REST API implements the [FHIR standard](https://docs.cloud.google.com/healthcare-api/docs/fhir) to manage FHIR data. The gcloud CLI doesn't support the FHIR standard, but it provides alternatives for operations like storing FHIR resources.

This section shows how to complete the following tasks:

  1. Create a FHIR store.
  2. Import FHIR resources from a public Cloud Storage bucket into the FHIR store.



### Create a FHIR store

FHIR stores exist inside datasets and contain FHIR resources. The following sample shows how to create a FHIR store named `my-fhir-store` that uses [FHIR version R4](https://hl7.org/fhir/R4/).

### gcloud

Create a FHIR store using the [`gcloud healthcare fhir-stores create`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create) command.

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores create my-fhir-store \
      --project=PROJECT_ID \
      --dataset=my-dataset \
      --location=us-central1 \
      --version=R4

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores create my-fhir-store `
      --project=PROJECT_ID `
      --dataset=my-dataset `
      --location=us-central1 `
      --version=R4

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores create my-fhir-store ^
      --project=PROJECT_ID ^
      --dataset=my-dataset ^
      --location=us-central1 ^
      --version=R4

You should receive a response similar to the following:

#### Response
    
    
    Created fhirStore [my-fhir-store].

### Import FHIR resources

Sample FHIR data is available in the `gs://gcp-public-data--synthea-fhir-data-10-patients` Cloud Storage bucket.

### gcloud

Import the FHIR resources in [`gs://gcp-public-data--synthea-fhir-data-10-patients`](https://console.cloud.google.com/storage/browser/gcp-public-data--synthea-fhir-data-10-patients) using the [`gcloud healthcare fhir-stores import`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/import) command.

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores import gcs my-fhir-store \
      --project=PROJECT_ID \
      --dataset=my-dataset \
      --location=us-central1 \
      --gcs-uri=gs://gcp-public-data--synthea-fhir-data-10-patients/fhir_r4_ndjson/*.ndjson \
      --content-structure=RESOURCE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores import gcs my-fhir-store `
      --project=PROJECT_ID `
      --dataset=my-dataset `
      --location=us-central1 `
      --gcs-uri=gs://gcp-public-data--synthea-fhir-data-10-patients/fhir_r4_ndjson/*.ndjson `
      --content-structure=RESOURCE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores import gcs my-fhir-store ^
      --project=PROJECT_ID ^
      --dataset=my-dataset ^
      --location=us-central1 ^
      --gcs-uri=gs://gcp-public-data--synthea-fhir-data-10-patients/fhir_r4_ndjson/*.ndjson ^
      --content-structure=RESOURCE

In this output:

  * `PROJECT_ID`, `us-central1`, `my-dataset`, `my-fhir-store`: the values you provided when running the command
  * `OPERATION_ID`: an identifier for the [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) provided by the Cloud Healthcare API when you import a FHIR resource. Long-running operations are returned when method calls might take a long time to complete. Importing the FHIR resources takes about one to two minutes.
  * `R4`: the FHIR store version



#### Response
    
    
    Request issued for: [my-fhir-store]
    Waiting for operation [projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/operations/OPERATION_ID] to complete...done.
    name: projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/fhirStores/my-fhir-store
    version: R4
    

After importing the FHIR resources into the Cloud Healthcare API, continue to Clean up to avoid incurring charges to your Google Cloud account for the resources used in this page.

For information on next steps, such as how to view and search for FHIR resources, see What's next.

## Store an HL7v2 message

This section shows how to complete the following tasks:

  1. Create an HL7v2 store.
  2. Import an HL7v2 message from a public Cloud Storage bucket into the HL7v2 store.



The HL7v2 implementation in the Cloud Healthcare API aligns with the [HL7v2 standard](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=185).

### Create an HL7v2 store

HL7v2 stores exist inside datasets and contain HL7v2 messages. The following sample shows how to create an HL7v2 store named `my-hl7v2-store`.

### gcloud

Create an HL7v2 store using the [`gcloud healthcare hl7v2-stores create`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/create) command.

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores create my-hl7v2-store \
      --project=PROJECT_ID \
      --dataset=my-dataset \
      --location=us-central1

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores create my-hl7v2-store `
      --project=PROJECT_ID `
      --dataset=my-dataset `
      --location=us-central1

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores create my-hl7v2-store ^
      --project=PROJECT_ID ^
      --dataset=my-dataset ^
      --location=us-central1

You should receive a response similar to the following:

#### Response
    
    
    Created hl7v2Store [my-hl7v2-store].

### Import HL7v2 messages

### gcloud

Import the [`gs://cloud-samples-data/healthcare/hl7v2/messages.ndjson`](https://storage.googleapis.com/cloud-samples-data/healthcare/hl7v2/messages.ndjson) HL7v2 message using the [`gcloud healthcare hl7v2-stores import`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/hl7v2-stores/import) command.

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores import gcs my-hl7v2-store \
      --project=PROJECT_ID \
      --dataset=my-dataset \
      --location=us-central1 \
      --gcs-uri=gs://cloud-samples-data/healthcare/hl7v2/messages.ndjson

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores import gcs my-hl7v2-store `
      --project=PROJECT_ID `
      --dataset=my-dataset `
      --location=us-central1 `
      --gcs-uri=gs://cloud-samples-data/healthcare/hl7v2/messages.ndjson

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores import gcs my-hl7v2-store ^
      --project=PROJECT_ID ^
      --dataset=my-dataset ^
      --location=us-central1 ^
      --gcs-uri=gs://cloud-samples-data/healthcare/hl7v2/messages.ndjson

In this output:

  * `PROJECT_ID`, `us-central1`, `my-dataset`, `my-hl7v2-store`: the values you provided when running the command
  * `OPERATION_ID`: an identifier for the [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) provided by the Cloud Healthcare API when you import an HL7v2 message. Long-running operations are returned when method calls might take a long time to complete. Importing one HL7v2 message is usually a quick operation, so the output is returned almost immediately.



#### Response
    
    
    Request issued for: [my-hl7v2-store]
    Waiting for operation [projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/operations/OPERATION_ID] to complete...done.
    name: projects/PROJECT_ID/locations/us-central1/datasets/my-dataset/hl7V2Stores/my-hl7v2-store
    

After importing the HL7v2 message into the Cloud Healthcare API, continue to Clean up to avoid incurring charges to your Google Cloud account for the resources used in this page.

For information on next steps, such as how to view the contents of an HL7v2 message, see What's next.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

If you created a new project for this quickstart, follow the steps in Delete the project. Otherwise, follow the steps in Delete the dataset.

Optional: Revoke credentials from the gcloud CLI. 
    
    
    gcloud auth revoke

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete the dataset

If you no longer need the dataset created in this quickstart, you can delete it. Deleting a dataset permanently deletes the dataset and any FHIR, HL7v2, or DICOM stores it contains.

### gcloud

Delete a dataset using the [`gcloud healthcare datasets delete`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/datasets/delete) command.

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of the Google Cloud project that you created or selected in Before you begin



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare datasets delete my-dataset \
      --project=PROJECT_ID \
      --location=us-central1

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare datasets delete my-dataset `
      --project=PROJECT_ID `
      --location=us-central1

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare datasets delete my-dataset ^
      --project=PROJECT_ID ^
      --location=us-central1

To confirm, type **Y**. You should receive a response similar to the following. 

#### Response
    
    
    You are about to delete dataset [my-dataset]
    
    Do you want to continue (Y/n)?  Y
    
    Deleted dataset [my-dataset].
    

## How did it go?

It worked!  **Great!** What did you like about the quickstart? What could we have done better?  Let us know!.  I got stuck.  **We're sorry to hear that.** Let us know what went wrong. We'll want to fix it. 

## What's next

See the following sections for general information on the Cloud Healthcare API and how to perform the tasks in this quickstart using another interface:

  * Read an [overview of Cloud Healthcare API concepts](https://docs.cloud.google.com/healthcare-api/docs/concepts/introduction)
  * [Store healthcare data with `curl` or PowerShell](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest)
  * [Store healthcare data with client libraries](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library)
  * [Store healthcare data with the gcloud CLI](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-gcloud)



### DICOM

  * [Create and manage DICOM stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom)
  * [Connect a PACS to the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs)
  * [Use the DICOMweb standard](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb)
  * [Import and export DICOM data using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export)



See the [DICOM conformance statement](https://docs.cloud.google.com/healthcare-api/docs/dicom) for information on how the Cloud Healthcare API implements the DICOMweb standard.

### FHIR

  * [Create and manage FHIR stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir)
  * [Create and manage FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources)
  * [Import and export FHIR data using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export)



See the [FHIR conformance statement](https://docs.cloud.google.com/healthcare-api/docs/fhir) for information on how the Cloud Healthcare API implements the FHIR standard.

### HL7v2

  * [Create and manage HL7v2 stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2)
  * [Create and manage HL7v2 messages](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages)
  * [Transmit HL7v2 messages over TCP/IP connections](https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter)
  * [Import and export HL7v2 messages using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-import-export)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
