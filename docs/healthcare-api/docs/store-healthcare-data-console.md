---
url: https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-console/
title: Quickstart: Store healthcare data with the Google Cloud console \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:57.626151+00:00
---

# Quickstart: Store healthcare data with the Google Cloud console  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store healthcare data with the Google Cloud console

This page shows you how to use the Cloud Healthcare API and the Google Cloud console to complete the following tasks: 

  1. Create a Cloud Healthcare API dataset.
  2. Create one of the following data stores inside the dataset:
     * Digital Imaging and Communications in Medicine (DICOM) store
     * Fast Healthcare Interoperability Resources (FHIR) store
     * Health Level Seven International Version 2 (HL7v2) store
  3. Store DICOM or FHIR data, and view FHIR resource contents.



If you're only interested in working with one type of data store, you can skip directly to that section of the quickstart after completing the steps in Before you begin and Create a dataset. 

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/home/dashboard?tutorial=healthcare-api__quickstart-console)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Healthcare API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=healthcare.googleapis.com)




## Create a dataset

_Datasets_ contain data stores, and data stores contain healthcare data. To use the Cloud Healthcare API, you must create at least one dataset. 

  1. In the Google Cloud console, click **Healthcare** to go to the **Datasets** page.

[Go to Browser](https://console.cloud.google.com/healthcare/browser)

  2. Click **Create dataset**.

  3. In the **Name** field, enter `my-dataset`.

  4. In the **Region** field, select `us-central1`, and then click **Create**.




The new dataset appears in the list of datasets in the browser.

To complete this quickstart, choose from one of the following sections:

  * Store a DICOM instance
  * Store and view FHIR resources
  * Store HL7v2 messages



## Store a DICOM instance

This section shows how to complete the following tasks:

  1. Create a DICOM store.
  2. Import a DICOM instance into the DICOM store.



The Cloud Healthcare API implements the [DICOMweb](https://www.dicomstandard.org/using/dicomweb) standard to store and access medical imaging data. The Google Cloud console does not support DICOMweb transactions, such as viewing or retrieving instances.

### Create a DICOM store

  1. In the Google Cloud console, go to the Cloud Healthcare API **Browser** page:

[Go to Browser](https://console.cloud.google.com/healthcare/browser)



  1. Click the `my-dataset` dataset.

  2. Click **Create data store**.

  3. In the **Type** menu, select **DICOM**.

  4. In the **ID** field, enter `my-dicom-store`.

  5. Click **Create**.




The `my-dicom-store` DICOM store displays in the **Data stores** page in the `my-dataset` dataset.

### Import a DICOM instance

Sample DICOM data is available in the `gs://gcs-public-data--healthcare-nih-chest-xray` Cloud Storage bucket.

  1. In the list of data stores in your dataset, find the DICOM store that you created, and then select the **Actions** menu.

  2. Select **Import**.

  3. In the **Import to DICOM store** page, select the **Advanced options** menu, and then select **Override Cloud Storage path**.

  4. In the **Location** field under the **Advanced options** menu, enter the following location of the DICOM instance you are importing:
         
         gs://gcs-public-data--healthcare-nih-chest-xray/dicom/00000001_000.dcm
         

  5. Click **Import**.

  6. To track the status of the import, click the **Operations** tab.

If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**.




Now that you've stored a DICOM instance in the Cloud Healthcare API, continue to What's next for information on next steps, such as how to search for or retrieve DICOM images.

## Store and view FHIR resources

This section shows how to complete the following tasks:

  1. Create a FHIR store.
  2. Import FHIR resources into the FHIR store.
  3. View the FHIR resources' data.



The Cloud Healthcare API implements the [FHIR specification](https://docs.cloud.google.com/healthcare-api/docs/fhir) to store and access FHIR data. The Google Cloud console does not support certain FHIR API methods, such as creating or deleting FHIR resources, but you can use the **FHIR viewer** to view the contents of FHIR resources.

### Create a FHIR store

  1. Click **Browser** to go to the **Datasets** page.

  2. Click the `my-dataset` dataset.

  3. Click **Create data store**.

  4. In the **Type** menu, select **FHIR**.

  5. In the **ID** field, enter `my-fhir-store`.

  6. To open the **Configure your FHIR store** section, click **Next**.

  7. Click **R4**.

  8. Click **Create**.




The `my-fhir-store` FHIR store displays in the **Data stores** page in the `my-dataset` dataset.

### Import FHIR resources

Sample FHIR data is available in the `gs://gcp-public-data--synthea-fhir-data-10-patients` Cloud Storage bucket. The bucket contains a directory, `fhir_r4_ndjson/`, which contains several types of FHIR resources.

  1. In the list of data stores in your dataset, find the `my-fhir-store` FHIR store you created, and then select the **Actions** menu.

  2. Select **Import**.

  3. Select the **Advanced options** menu, and then select **Override Cloud Storage path**.

  4. In the **Location** field under the **Advanced options** menu, enter the following location of the FHIR resources you are importing:
         
         gs://gcp-public-data--synthea-fhir-data-10-patients/fhir_r4_ndjson/*.ndjson
         

  5. In the **FHIR import settings** section, select **Resource**.

  6. Click **Import**.

  7. To track the status of the import, click the **Operations** tab.

If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**.




### View FHIR resource contents

  1. In the Google Cloud console, go to the **FHIR viewer** page.

[Go to the FHIR viewer](https://console.cloud.google.com/healthcare/fhirviewer)



  1. In the **FHIR store** drop-down list, select the `my-dataset` dataset, and then select the `my-fhir-store` FHIR store.

  2. Click the **Resource Type** field. In the **Properties** drop-down list that appears, select **Resource type** , and then enter **Patient**.

  3. Click **Patient** in the **Resource type** list.

  4. Select one of the Patient resources that appears. To view more information about the Patient resource, click the **Elements** tab, or click the **JSON** tab to view the Patient resource details in JSON format.




Now that you've stored and viewed a FHIR resource in the Cloud Healthcare API, continue to What's next for information on next steps.

## Store HL7v2 messages

This section shows how to complete the following tasks:

  1. Create an HL7v2 store.
  2. Import HL7v2 messages into the HL7v2 store.



### Create an HL7v2 store

HL7v2 stores exist inside datasets and hold HL7v2 messages.

  1. Click **Browser** to go to the **Datasets** page.

  2. Click the `my-dataset` dataset.

  3. Click **Create data store**.

  4. In the **Type** menu, select **HL7v2**.

  5. In the **ID** field, enter `my-hl7v2-store`.

  6. Click **Create**.




The `my-hl7v2-store` HL7v2 store displays in the **Data stores** page in the `my-dataset` dataset.

### Import HL7v2 messages

Sample HL7v2 messages are available in `gs://cloud-samples-data/healthcare/hl7v2/messages.ndjson`.

  1. In the list of data stores in your dataset, find the HL7v2 store that you created, and then select the **Actions** menu.

  2. Select **Import**.

  3. In the **Import to HL7v2 store** page, select the **Advanced options** menu, and then select **Override Cloud Storage path**.

  4. In the **Location** field under the **Advanced options** menu, enter the following location of the HL7v2 messages you are importing:
         
         gs://cloud-samples-data/healthcare/hl7v2/messages.ndjson
         

  5. Click **Import**.

  6. To track the status of the import, click the **Operations** tab.

If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**.




Now that you've created an HL7v2 store, continue to What's next for information on next steps, such as how to ingest and view HL7v2 messages.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

If you no longer need the dataset and data store created in this quickstart, you can delete the dataset. Deleting a dataset permanently deletes the dataset and any FHIR, HL7v2, or DICOM stores it contains.

To delete a dataset, complete the following steps:

  1. Click **Browser** to go to the **Datasets** page.
  2. Click **Actions** next to the dataset, and then click **Delete**.
  3. Confirm your deletion.



Or you can [delete the project](https://console.cloud.google.com/cloud-resource-manager) that you created.

## What's next

See the following sections for general information on the Cloud Healthcare API and how to perform tasks using HTTP requests and the Google Cloud CLI:

  * Read an [overview of Cloud Healthcare API concepts](https://docs.cloud.google.com/healthcare-api/docs/concepts/introduction).
  * [Use the Cloud Healthcare API with `curl` or PowerShell](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest).
  * [Use the Cloud Healthcare API with the gcloud CLI](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-gcloud).



### DICOM

Continue to the [DICOM guide](https://docs.cloud.google.com/healthcare-api/docs/how-tos#dicom-guide) to read topics such as the following:

  * [Creating and managing DICOM stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom)
  * [Connecting a PACS to the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs)
  * [Using the DICOMweb standard](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb)
  * [Importing and exporting DICOM data using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export)



See the [DICOM conformance statement](https://docs.cloud.google.com/healthcare-api/docs/dicom) for information on how the Cloud Healthcare API implements the DICOMweb standard.

### FHIR

Continue to the [FHIR guide](https://docs.cloud.google.com/healthcare-api/docs/how-tos#fhir-guide) to read topics such as the following:

  * [Creating and managing FHIR stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir)
  * [Creating and managing FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources)
  * [Importing and exporting FHIR data using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export)



See the [FHIR conformance statement](https://docs.cloud.google.com/healthcare-api/docs/fhir) for information on how the Cloud Healthcare API implements the FHIR standard.

### HL7v2

Continue to the [HL7v2 guide](https://docs.cloud.google.com/healthcare-api/docs/how-tos#hl7v2-guide) to read topics such as the following:

  * [Creating and managing HL7v2 stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2)
  * [Creating and managing HL7v2 messages](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages)
  * [Transmitting HL7v2 messages over TCP/IP connections](https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter)
  * [Importing and exporting HL7v2 messages using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-import-export)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
