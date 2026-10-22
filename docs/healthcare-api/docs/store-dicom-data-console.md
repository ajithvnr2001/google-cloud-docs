---
url: https://docs.cloud.google.com/healthcare-api/docs/store-dicom-data-console/
title: Quickstart: Store DICOM healthcare data with the Google Cloud console \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:58.013512+00:00
---

# Quickstart: Store DICOM healthcare data with the Google Cloud console  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/store-dicom-data-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store DICOM healthcare data with the Google Cloud console

This page shows you how to use the Cloud Healthcare API and Google Cloud console to complete the following tasks:

  1. Create a Cloud Healthcare API dataset.
  2. Create a Digital Imaging and Communications in Medicine (DICOM) store inside the dataset.
  3. Store a DICOM instance in the DICOM store.
  4. Clean up to avoid billing charges.



* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/home/dashboard?tutorial=healthcare-api__dicom-quickstart-console)

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

  1. In the list of data stores in your dataset, find the `my-dicom-store` DICOM store, and then select the **Actions** menu.

  2. Select **Import**.

  3. In the **Import to DICOM store** page, select the **Advanced options** menu, and then select **Override Cloud Storage path**.

  4. In the **Location** field under the **Advanced options** menu, enter the following location of the DICOM instance you are importing:
         
         gs://gcs-public-data--healthcare-nih-chest-xray/dicom/00000001_000.dcm
         

  5. Click **Import**.

  6. To track the status of the import, click the **Operations** tab.

If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**.




Now that you've stored a DICOM instance in the Cloud Healthcare API, clean up the resources you created in this quickstart, or continue to What's next for information on next steps, such as how to search for or retrieve DICOM images.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

If you no longer need the dataset and DICOM store created in this quickstart, you can delete the dataset. Deleting a dataset permanently deletes the dataset and any DICOM stores it contains.

To delete a dataset, complete the following steps:

  1. Click **Browser** to go to the **Datasets** page.
  2. Click **Actions** next to the dataset, and then click **Delete**.
  3. Confirm your deletion.



Or you can [delete the project](https://console.cloud.google.com/cloud-resource-manager) that you created.

## What's next

Continue to the [DICOM guide](https://docs.cloud.google.com/healthcare-api/docs/how-tos#dicom-guide) to read topics such as the following:

  * [Creating and managing DICOM stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom)
  * [Connecting a PACS to the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs)
  * [Using the DICOMweb standard](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb)
  * [Importing and exporting DICOM data using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export)



See the [DICOM conformance statement](https://docs.cloud.google.com/healthcare-api/docs/dicom) for information on how the Cloud Healthcare API implements the DICOMweb standard.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
