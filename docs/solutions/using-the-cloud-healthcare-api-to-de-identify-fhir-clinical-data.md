---
url: https://docs.cloud.google.com/solutions/using-the-cloud-healthcare-api-to-de-identify-fhir-clinical-data/
title: Using the Cloud Healthcare API to de-identify FHIR clinical data \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:46:17.728859+00:00
---

# Using the Cloud Healthcare API to de-identify FHIR clinical data  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/using-the-cloud-healthcare-api-to-de-identify-fhir-clinical-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Using the Cloud Healthcare API to de-identify FHIR clinical data Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows researchers, data scientists, and IT teams working with healthcare and life sciences organizations how to use the [Fast Healthcare Interoperability Resources (FHIR)](https://www.hl7.org/fhir/overview.html) de-identification operation of the [Cloud Healthcare API](https://docs.cloud.google.com/healthcare) to remove or modify [personally identifiable information (PII)](https://wikipedia.org/wiki/Personal_data), including [protected health information (PHI)](https://wikipedia.org/wiki/Protected_health_information), from FHIR clinical data. De-identifying medical data helps to protect patient privacy and to prepare healthcare data for use in research, data sharing, and machine learning. 

This tutorial assumes that you have a fundamental knowledge of Linux. A basic understanding of Google Cloud and the [FHIR Specification](https://www.hl7.org/fhir/stu3/) and its use in electronic health records systems (EHRs) is also helpful. Run all commands in this tutorial in [Cloud Shell](https://docs.cloud.google.com/shell). 

## Objectives

  * Create a Cloud Healthcare API [dataset](https://docs.cloud.google.com/healthcare/docs/concepts/projects-datasets-data-stores#datasets_and_data_stores) and [FHIR store](https://docs.cloud.google.com/healthcare/docs/concepts/fhir#fhir_stores).
  * Import FHIR data into the Cloud Healthcare API FHIR store.
  * Use the FHIR de-identification operation of the Cloud Healthcare API to remove or modify PII and PHI in FHIR instances in a FHIR store.
  * Use the `curl` command-line tool to make a FHIR de-identification call through the Cloud Healthcare API.



## Costs

This tutorial uses the following billable components of Google Cloud: 

  * [Cloud Healthcare API](https://docs.cloud.google.com/healthcare/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

## Before you begin

All Cloud Healthcare API usage occurs within the context of a Google Cloud project. Projects form the basis for creating, enabling, and using all Google Cloud services, including managing APIs, enabling billing, adding and removing collaborators, and managing permissions for Google Cloud resources. Use the following procedure to create a Google Cloud project, or select a project that you have already created. 

  1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Healthcare API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=healthcare.googleapis.com)

  5. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  6. In Cloud Shell, run the `gcloud components update` command to make sure that you have the latest version of the gcloud CLI that includes Cloud Healthcare API-related functionality.



When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Creating an IAM service account

The Healthcare Dataset Administrator, FHIR Administrator, and FHIR Resource Editor roles are required for this tutorial. Use the following steps to create a service account and assign the correct roles:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).
  2. [Assign roles to the service account:](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource)

     * Healthcare Dataset Administrator
     * Healthcare FHIR Administrator
     * Healthcare FHIR Resource Editor
  3. [Create and download the service account JSON key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).

  4. Activate your service account key:
         
         gcloud auth activate-service-account --key-file=path-to-key-file
         

The output is the following:
         
         Activated service account credentials for: [key-name@project-name.iam.gserviceaccount.com]
         

     * `key-name` is the name that you assigned to the service account key.
     * `project-name` is the name of your Google Cloud project.



## Obtaining an OAuth 2.0 access token

To use the Cloud Healthcare API to ingest data, you need an OAuth 2.0 access token that the commands in this tutorial obtain for you. In this tutorial, some of the example Cloud Healthcare API requests use the `curl` command-line tool. These examples use the `gcloud auth print-access-token` command to obtain an OAuth 2.0 bearer token and to include the token in the request's authorization header. For more information about this command, see [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

## Setting up the FHIR dataset for de-identification

Each FHIR resource is a JSON-like object that contains key-value pairs. Some elements are standardized and other elements are free text. You can use the de-identification operation to do the following:

  * Remove the values for specific keys in the FHIR resource.
  * Process the unstructured text to remove only the PII elements, leaving the rest of the content in the text as is.



When you de-identify a dataset, the destination dataset _must not_ exist before you make the de-identification API call. The de-identification operation creates the destination dataset.

When you de-identify a single FHIR store, the destination dataset _must_ exist before you make the de-identification API call.

The source dataset, the FHIR store, and the destination dataset's FHIR store must reside in the same Google Cloud project. When you run the de-identification operation, the destination dataset and the FHIR store are created in the same Google Cloud project as the source dataset and FHIR store.

If you want to generate synthetic FHIR data to use for this tutorial, you can use [Synthea](https://github.com/synthetichealth/synthea) to generate synthetic data in the FHIR STU3 format, copy the generated data to a Cloud Storage bucket, and then import it into the Cloud Healthcare API FHIR store. Synthea doesn't generate FHIR data with free or unstructured text components, so you can't use it to explore these aspects of de-identification.

For this tutorial, you import sample FHIR data into the FHIR store as indicated in the following procedure.

  1. Set up environment variables for the project and location where the dataset, the FHIR store, and the FHIR data will be stored. The values assigned to the environment variables are sample values, as follows:
         
         export PROJECT_ID=MyProj
         export REGION=us-central1
         export SOURCE_DATASET_ID=dataset1
         export FHIR_STORE_ID=FHIRstore1
         export DESTINATION_DATASET_ID=deid-dataset1
         

The definitions of the environment variables that are declared in the preceding example are as follows:

     * `$PROJECT_ID` is your Google Cloud project identifier.
     * `$REGION` is your the Google Cloud region where the Cloud Healthcare APIdataset is created.
     * `$SOURCE_DATASET_ID` is the name of the Cloud Healthcare API dataset where the source data is stored.
     * `$FHIR_STORE_ID` is the name of the source Cloud Healthcare API FHIR store.
     * `$DESTINATION_DATASET_ID` is the name of the Cloud Healthcare API destination dataset where the de-identified data is written.

You'll also use these environment variables later in this tutorial.

  2. Create a Cloud Healthcare API dataset:
         
         gcloud healthcare datasets create $SOURCE_DATASET_ID --location=$REGION
         

The output is similar to the following, where `[OPERATION_NUMBER]` is the dataset creation operation identifier that is used for tracking the request:
         
         Create request issued for: $SOURCE_DATASET_ID
         
         Waiting for operation [OPERATION_NUMBER] to complete...done.
         Created dataset $SOURCE_DATASET_ID.
         

The preceding command creates the source dataset with the name `$SOURCE_DATASET_ID` in the region `$REGION`.

  3. Create a FHIR store by using the following command:
         
         gcloud healthcare fhir-stores create $FHIR_STORE_ID \
             --dataset=$SOURCE_DATASET_ID --location=$REGION
         

The preceding command creates a FHIR store with the name `$FHIR_STORE_ID` in the dataset `$SOURCE_DATASET_ID`.

  4. Add the FHIR Patient resource to the FHIR store by using the [FHIR `create` function](https://docs.cloud.google.com/solutions/importing-fhir-clinical-data#use_the_fhir_create_function) with the following command:
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/fhir+json; charset=utf-8" \
             --data "{
                \"address\": [
             {
               \"city\": \"Anycity\",
               \"district\": \"Anydistrict\",
               \"line\": [
                 \"123 Main Street\"
               ],
               \"period\": {
                 \"start\": \"1990-12-05\"
               },
               \"postalCode\": \"12345\",
               \"state\": \"CA\",
               \"text\": \"123 Main Street Anycity, Anydistrict, CA 12345\",
               \"use\": \"home\"
             }
           ],
                   \"name\": [
                 {
                   \"family\": \"Smith\",
                   \"given\": [
                     \"Darcy\"
                   ],
                   \"use\": \"official\"
                 }
               ],
               \"gender\": \"female\",
               \"birthDate\": \"1980-12-05\",
               \"resourceType\": \"Patient\"
             }" \
         "https://healthcare.googleapis.com/v1/projects/$PROJECT_ID/locations/$REGION/datasets/$SOURCE_DATASET_ID/fhirStores/$FHIR_STORE_ID/fhir/Patient"
         

The command's argument corresponds to the example FHIR resource, a [FHIR Patient resource](https://www.hl7.org/fhir/stu3/patient.html).
         
         {
           "address": [
             {
               "city": "Anycity",
               "district": "Anydistrict",
               "line": [
                 "123 Main Street"
               ],
               "period": {
                 "start": "1990-12-05"
               },
               "postalCode": "12345",
               "state": "CA",
               "text": "123 Main Street Anycity, Anydistrict, CA 12345",
               "use": "home"
             }
           ],
           "name": [
             {
               "family": "Smith",
               "given": [
                 "Darcy"
               ],
         "use": "official"
             }
           ],
         "gender": "female",
         "birthDate": "1980-12-05",
          "resourceType": "Patient"
         }
         

If the request is successful, the server returns an output like the following:
         
         {
           "address": [
             {
               "city": "Anycity",
               "district": "Anydistrict",
               "line": [
                 "123 Main Street"
               ],
               "period": {
                 "start": "1990-12-05"
               },
               "postalCode": "12345",
               "state": "CA",
               "text": "123 Main Street Anycity, Anydistrict, CA 12345",
               "use": "home"
             }
           ],
           "birthDate": "1980-12-05",
           "gender": "female",
           "id": "0359c226-5d63-4845-bd55-74063535e4ef",
           "meta": {
             "lastUpdated": "2020-02-08T00:03:21.745220+00:00",
             "versionId": "MTU4MTEyMDIwMTc0NTIyMDAwMA"
           },
           "name": [
             {
               "family": "Smith",
               "given": [
                 "Darcy"
               ],
               "use": "official"
             }
           ],
           "resourceType": "Patient"
         }
         

The preceding `curl` command inserts a new Patient resource in the source FHIR store. A patient identifier (`id`) is generated in the output. The patient identifier is a de-identified alphanumeric string that is used in the FHIR Encounter resource to link to the FHIR Patient resource.

  5. Add the FHIR Encounter resource to the FHIR store by using the [FHIR `create` function](https://docs.cloud.google.com/solutions/importing-fhir-clinical-data#use_the_fhir_create_function) with the following command. In the command, replace the `subject.reference` value with the patient identifier value from the output of the preceding `curl` command:
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/fhir+json; charset=utf-8" \
             --data "{
               \"status\": \"finished\",
               \"class\": {
                 \"system\": \"http://hl7.org/fhir/v3/ActCode\",
                 \"code\": \"IMP\",
                 \"display\": \"inpatient encounter\"
               },
               \"reason\": [
                 {
                   \"text\": \"Mrs. Smith is a 39-year-old female who has a past
         medical history significant for a myocardial infarction. Catheterization
         showed a possible kink in one of her blood vessels.\"
                 }
               ],
               \"subject\": {
                 \"reference\":
         \"Patient/0359c226-5d63-4845-bd55-74063535e4ef\"
               },
               \"resourceType\": \"Encounter\"
             }" \
         
         "https://healthcare.googleapis.com/v1/projects/$PROJECT_ID/locations/$REGION/datasets/$SOURCE_DATASET_ID/fhirStores/$FHIR_STORE_ID/fhir/Encounter"
         

The command's argument corresponds to the example FHIR resource, a [FHIR Encounter resource](https://www.hl7.org/fhir/stu3/encounter.html):
         
         {
               "status": "finished",
               "class": {
                 "system": "http://hl7.org/fhir/v3/ActCode",
                 "code": "IMP",
                 "display": "inpatient encounter"
               },
               "reason": [
                 {
                   "text": "Mrs. Smith is a 39-year-old female who has a past medical
         history significant for a myocardial infarction. Catheterization showed a
         possible kink in one of her blood vessels."
                 }
               ],
               "subject": {
                 "reference": "Patient/0359c226-5d63-4845-bd55-74063535e4ef"
               },
               "resourceType": "Encounter"
             }
         

If the request is successful, the server returns an output like the following:
         
         {
           "class": {
             "code": "IMP",
             "display": "inpatient encounter",
             "system": "http://hl7.org/fhir/v3/ActCode"
           },
           "id": "0038a95f-3c11-4163-8c2e-10842b6b1547",
           "meta": {
             "lastUpdated": "2020-02-12T00:39:16.822443+00:00",
             "versionId": "MTU4MTQ2Nzk1NjgyMjQ0MzAwMA"
           },
           "reason": [
             {
               "text": "Mrs. Smith is a 39-year-old female who has a past medical history
         significant for a myocardial infarction. Catheterization showed a possible
         kink in one of her blood vessels."
             }
           ],
           "resourceType": "Encounter",
           "status": "finished",
           "subject": {
             "reference": "Patient/0359c226-5d63-4845-bd55-74063535e4ef"
           }
         

The preceding `curl` command inserts a new Encounter resource in the source FHIR store. 




## De-identifying FHIR data

Next, you de-identify the FHIR data that you inserted in the source FHIR store. You redact or transform all PII elements in structured fields, such as the `Patient.name` and `Patient.address` fields. You also de-identify the PII elements in the unstructured data in text, such as `Encounter.reason.text`.

Optionally, you can then export the resulting data directly to [BigQuery](https://docs.cloud.google.com/bigquery) for analysis and machine learning training.

This configuration of de-identification can be used for a population health analysis or a similar use case. In the context of this tutorial, you can move de-identified structured data to BigQuery to assess large-scale trends. You might not need unstructured fields, which are hard to normalize and analyze at a large scale. However, unstructured fields are included in this tutorial as a reference.

There are many potential use cases for de-identifying FHIR data. There are also many configuration options supported by the Cloud Healthcare API. For more information, including sample `curl` commands for different scenarios, see [De-identifying FHIR data](https://docs.cloud.google.com/healthcare/docs/how-tos/fhir-deidentify).

Fields that contain a date are transformed by [date shifting](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-date-shifting)—a technique that changes all the dates in a FHIR resource by a consistent, random amount. Date shifting maintains consistency within a FHIR resource so that medically relevant details, such as patient age and time between appointments, are maintained without revealing identifying information about the patient. All identifiers in unstructured fields are transformed, as well.

The following example also includes a hashing transformation on the `name` fields. Hashing is a one-way encryption technique that ensures that a name is always transformed to the same output value, generating consistent outputs for the same patient name across multiple records in the dataset. In this operation, you obscure PII while also retaining links between resources.

In this example, the provided cryptographic key, `U2FsdGVkX19bS2oZsdbK9X5zi2utBn22uY+I2Vo0zOU=`, is a sample AES-encrypted, 256-bit, base64-encoded key that is generated by using the following command.
    
    
    echo -n "test" | openssl enc -e -aes-256-ofb -a -salt
    

The command asks you to enter a password. Enter a password of your choice.

**Note:** If you don't provide a cryptographic key, the Cloud Healthcare API generates its own crypto key each time the de-identification operation runs on date values. This can result in inconsistent date outputs between runs.

  1. Use the `curl` command to redact or transform all PII elements in structured fields, such as the `name` and `address` fields, and to transform all identifiers in unstructured fields.
         
         curl -X POST \
             -H "Authorization: Bearer "$(gcloud auth print-access-token) \
             -H "Content-Type: application/json; charset=utf-8" \
             --data "{
               'destinationDataset':
         'projects/$PROJECT_ID/locations/$REGION/datasets/$DESTINATION_DATASET_ID',
               'config': {
               'fhir': {
                   'fieldMetadataList': {
                     'paths': [
                       'Patient.address.state',
                       'Patient.address.line',
                       'Patient.address.text',
                       'Patient.address.postalCode'
                     ],
                     'action': 'TRANSFORM'
                   },
                  'fieldMetadataList': {
                    'paths': [
                      'Encounter.reason.text'
                    ],
                    'action': 'INSPECT_AND_TRANSFORM'
                  },
                'text': {
                  'transformations': [
                    {
                      'infoTypes': [],
                      'replaceWithInfoTypeConfig': {}
                    }
                  ]
                },
                   'fieldMetadataList': {
                     'paths': [
                       'Patient.name.family',
                       'Patient.name.given'
                     ],
                     'action': 'TRANSFORM'
                   },
                 'text': {
                   'transformations': {
                     'infoTypes': [
                       'PERSON_NAME'
                     ],
                     'cryptoHashConfig': {
                       'cryptoKey':
         'U2FsdGVkX19bS2oZsdbK9X5zi2utBn22uY+I2Vo0zOU='
                     }
                   }
                 },
                   'fieldMetadataList': {
                     'paths': [
                       'Patient.birthDate',
                       'Patient.address.period.start'
                     ],
                     'action': 'TRANSFORM'
                   },
                 'text': {
                   'transformations': {
                     'infoTypes': [
                       'DATE'
                     ],
                     'dateShiftConfig': {
                       'cryptoKey':
         'U2FsdGVkX19bS2oZsdbK9X5zi2utBn22uY+I2Vo0zOU='
                     }
                   }
                 }
               }
             }"
         "https://healthcare.googleapis.com/v1/projects/$PROJECT_ID/locations/$REGION/datasets/$SOURCE_DATASET_ID:deidentify"
         

If the request is successful, the server returns a response in JSON format like the following:
         
         {
           "name": "projects/$PROJECT_ID/locations/$REGION/datasets/$SOURCE_DATASET_ID/OPERATION_NAME"
         }
         

In the preceding example, the `curl` command de-identifies the FHIR resource by transforming values in the following ways:

     * Redacts the `Patient.address.line` value, the `Patient.address.text` value, and the `Patient.address.postalCode` value.
     * Replaces the `Patient.name.family` value with a hash value and replaces the `Patient.name.given` value with a hash value.
     * Replaces the values in the `Patient.birthDate` field and the `period.start` field with values that are produced by date-shifting with a 100-day differential.
     * In the `Encounter.reason.text` field, replaces the patient's family name with a hash value, and replaces the patient's age with the literal value `[AGE]`.
  2. The response to the preceding operation contains an operation name. Use the [`get` method](https://docs.cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation:
         
         curl -X GET \
             -H "Authorization: Bearer "$(gcloud auth print-access-token) \
             -H "Content-Type: application/json; charset=utf-8" \
         "https://healthcare.googleapis.com/v1/projects/$PROJECT_ID/locations/$REGION/datasets/$SOURCE_DATASET_ID/operations/OPERATION_NAME"
         

If the request is successful, the server returns a response in JSON format. After the de-identification process completes, the response includes `"done": true`.
         
         {
           "name": "projects/$PROJECT_ID/locations/$REGION/datasets/$SOURCE_DATASET_ID/operations/OPERATION_NAME",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
             "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
             "createTime": "2018-01-01T00:00:00Z",
             "endTime": "2018-01-01T00:00:00Z"
           },
           "done": true,
           "response": {
             "@type": "...",
             "successStoreCount": "SUCCESS_STORE_COUNT"
           }
         }
         

The preceding command returns the status of the de-identification operation.

  3. Use the patient identifier to get the details of the FHIR Patient resource in the new destination dataset by running the following command:
         
         curl -X GET \
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://healthcare.googleapis.com/v1/projects/$PROJECT_ID/locations/$REGION/datasets/$DESTINATION_DATASET_ID/fhirStores/$FHIR_STORE_ID/fhir/Patient/a952e409-2403-43e6-9815-cb78c5b5eca2/\$everything"
         

If the request is successful, the server returns a response like the following, which is the de-identified version of original FHIR resources:
         
         "entry": [\
             {\
               "resource": {\
                 "class": {\
                   "code": "IMP",\
                   "display": "inpatient encounter",\
                   "system": "http://hl7.org/fhir/v3/ActCode"\
                 },\
                 "id": "0038a95f-3c11-4163-8c2e-10842b6b1547",\
                 "reason": [\
                   {\
                     "text": "Mr. NlVBV12Hhb5DD8WNqlTpXboFxzlUSlqAmYDet/jIViQ= is a [AGE]
         gentleman who has a past medical history significant for a myocardial
         infarction. Catheterization showed a possible kink in one of his vessels."\
                   }\
                 ],\
                 "resourceType": "Encounter",\
                 "status": "finished",\
                 "subject": {\
                   "reference": "Patient/0359c226-5d63-4845-bd55-74063535e4ef"\
                 }\
               }\
             },\
             {\
               "resource": {\
                 "address": [\
                   {\
                     "city": "Anycity",\
                     "district": "Anydistrict",\
                     "line": [\
                       ""\
                     ],\
                     "period": {\
                       "start": "1990-09-23"\
                     },\
                     "postalCode": "",\
                     "state": "",\
                     "text": "",\
                     "use": "home"\
                   }\
                 ],\
                 "birthDate": "1980-09-23",\
                 "gender": "female",\
                 "id": "0359c226-5d63-4845-bd55-74063535e4ef",\
                 "name": [\
                   {\
                     "family": "NlVBV12Hhb5DD8WNqlTpXboFxzlUSlqAmYDet/jIViQ=",\
                     "given": [\
                       "FSH4e the project.D/IGb80a1rS0L0kqfC3DCDt6//17VPhIkOzH2pk="\
                     ],\
                     "use": "official"\
                   }\
                 ],\
                 "resourceType": "Patient"\
               }\
             }\
           ],\
           "resourceType": "Bundle",\
           "total": 2,\
           "type": "searchset"\
         }
         

The preceding command verifies that the de-identification operation is successful in de-identifying the FHIR resources.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources

  * Delete the destination datasets:
        
        gcloud healthcare datasets delete $DESTINATION_DATASET_ID
        




## What's next

  * [Cloud Healthcare API FHIR concepts](https://docs.cloud.google.com/healthcare/docs/concepts/fhir).
  * [Importing FHIR clinical data into the cloud using the Cloud Healthcare API](https://docs.cloud.google.com/solutions/importing-fhir-clinical-data).
  * [De-identifying FHIR data](https://docs.cloud.google.com/healthcare/docs/how-tos/fhir-deidentify).
  * [Exporting FHIR resources to BigQuery](https://docs.cloud.google.com/healthcare/docs/how-tos/fhir-export-bigquery).
  * [Cloud Healthcare API documentation](https://docs.cloud.google.com/healthcare/docs).
  * [Our Cloud Healthcare API and other solutions for supporting healthcare and life sciences organizations during the pandemic](https://cloud.google.com/blog/topics/inside-google-cloud/how-google-cloud-is-supporting-healthcare-and-life-sciences-organizations).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
