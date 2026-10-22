---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-hc-data/
title: Refresh healthcare data \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:23.828340+00:00
---

# Refresh healthcare data  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-hc-data/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Refresh healthcare data Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 

**Caution:**

  * Restrictions for healthcare: As a customer, you will not, and will not allow End Users to, use the Generative AI Services for clinical purposes (for clarity, non-clinical research, scheduling, or other administrative tasks is not restricted), as a substitute for professional medical advice, or in any manner that is overseen by or requires clearance or approval from any applicable regulatory authority. For more information, see [Service Specific Terms](https://cloud.google.com/terms/service-terms). 

For clarity, with respect to the use of Agent Search to retrieve and summarize existing medical information, the restriction on the use for clinical purposes means the restriction on the use for direct diagnosis or treatment purposes without review by a licensed professional in compliance with applicable laws and regulations. 

  * The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased (for example, stereotypes or other harmful content) information and should be reviewed. All summaries or answers should be considered draft and not final.
  * This product's intended usage is not to provide information pertaining to the prevention, diagnosis or treatment of illness or disease. Questions regarding diagnosis or treatment recommendations are not intended to be addressed by the product. This product's intended use is to retrieve and summarize existing medical information provided by users.
  * Due to limited test data, this product may or may not be applicable to age group 0-18 and to age group 85 and above. Therefore, when reviewing the generated output, customers must consider the representativeness of subpopulations within their source data.



After the initial import of data into your Agent Search healthcare data store, you might have performed any of the following updates in your source FHIR store:

  * Added new FHIR resources
  * Updated existing FHIR resources
  * Deleted FHIR resources



In such cases, you can _reconcile_ the changes from your source FHIR store into your Agent Search healthcare data store.

## Reconciliation overview

**Key Term:** A document in Agent Search healthcare data store corresponds to a FHIR R4 resource in a FHIR store.

You can reconcile the changes either incrementally or fully. The two modes are compared in the following table.

Changes to the source FHIR store  | Incremental mode  | Full mode   
---|---|---  
New FHIR resources  | Adds new documents to the Agent Search data store  | Adds new documents to the Agent Search data store   
Updated FHIR resources  | Replaces the existing documents in the Agent Search data store while retaining the document ID  | Replaces the existing documents in the Agent Search data store while retaining the document ID   
Deleted FHIR resources  | Doesn't reconcile  | Removes the corresponding documents from your Agent Search data store   
  
## Before you begin

Review the [quotas and limits](https://docs.cloud.google.com/generative-ai-app-builder/quotas) for your Google Cloud project. Your Agent Search healthcare data store can contain a maximum of 1 million documents per project. If this quota is reached during the import, the import process stops.

## Perform an incremental import

The following sample shows how to import incremental changes from a Cloud Healthcare API FHIR store using the [`documents.import`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.branches.documents/import) method.

#### Permissions required for this task

Grant the following Identity and Access Management (IAM) roles to the `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com` service account in the project that contains the Agent Search data store:

Purpose | Roles  
---|---  
To perform a one-time batch import of FHIR data from FHIR stores in Cloud Healthcare API. | 

  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [Healthcare FHIR Store Administrator (`roles/healthcare.fhirStoreAdmin`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirStoreAdmin)

  
To perform a streaming import of FHIR data from FHIR stores in Cloud Healthcare API in the same Google Cloud project. | 

  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [Healthcare FHIR Store Administrator (`roles/healthcare.fhirStoreAdmin`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirStoreAdmin)
  * [Healthcare FHIR Resource Reader (`roles/healthcare.fhirResourceReader`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirResourceReader)

  
To perform a streaming import of FHIR data from FHIR stores in Cloud Healthcare API in a different Google Cloud project. | 

  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [Healthcare FHIR Store Administrator (`roles/healthcare.fhirStoreAdmin`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirStoreAdmin)
  * [Healthcare FHIR Resource Reader (`roles/healthcare.fhirResourceReader`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirResourceReader)

  
To import FHIR data that references files in Cloud Storage. These are granted by default if the referenced files are in the same Google Cloud project as the Agent Search app. |  [Storage Object Admin (`roles/storage.objectAdmin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)  
To customize the schema when creating a data store to configure the indexability, searchability, and retrievability of FHIR resources and elements. |  [Storage Object Admin (`roles/storage.objectAdmin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)  
  
Grant the following Identity and Access Management roles to the `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com` service account in the project that contains the Cloud Healthcare API FHIR R4 data store:

Purpose | Roles  
---|---  
To perform a streaming import of FHIR data from FHIR stores in Cloud Healthcare API in a different Google Cloud project. | 

  * [Healthcare FHIR Store Administrator (`roles/healthcare.fhirStoreAdmin`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirStoreAdmin)
  * [Healthcare FHIR Resource Reader (`roles/healthcare.fhirResourceReader`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirResourceReader)

  
  
Grant the following Identity and Access Management roles to the `service-SOURCE_PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com` service account in the project that contains the Cloud Healthcare API FHIR R4 data store:

Purpose | Roles  
---|---  
To perform a streaming import of FHIR data from FHIR stores in Cloud Healthcare API in the same Google Cloud project. | 

  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)

  
To customize the schema when creating a data store to configure the indexability, searchability, and retrievability of FHIR resources and elements. |  [Storage Object Admin (`roles/storage.objectAdmin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)  
  
### REST

  1. Perform an incremental import.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://us-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/us/dataStores/DATA_STORE_ID/branches/0/documents:import" \
         -d '{
            "reconciliation_mode": "INCREMENTAL",
            "fhir_store_source": {"fhir_store": "projects/PROJECT_ID/locations/CLOUD_HEALTHCARE_DATASET_LOCATION/datasets/CLOUD_HEALTHCARE_DATASET_ID/fhirStores/FHIR_STORE_ID"}
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.
     * `CLOUD_HEALTHCARE_DATASET_ID`: the ID of the Cloud Healthcare API dataset that contains the source FHIR store.
     * `CLOUD_HEALTHCARE_DATASET_LOCATION`: the location of the Cloud Healthcare API dataset that contains the source FHIR store.
     * `FHIR_STORE_ID`: the ID of the Cloud Healthcare API FHIR R4 store.

#### Response

You should receive a JSON response similar to the following. The response contains an identifier for a long-running operation. Long-running operations are returned when method calls might take a substantial amount of time to complete. Note the value of IMPORT_OPERATION_ID. You need this value to verify the status of the import. 
    
    {
        "name": "projects/PROJECT_ID/locations/us/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/operations/IMPORT_OPERATION_ID",
        "metadata": {
          "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.ImportDocumentsMetadata"
        }
      }
    

  2. Verify whether the FHIR data import operation is complete.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://us-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/us/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/operations/IMPORT_OPERATION_ID"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.
     * `IMPORT_OPERATION_ID`: the operation ID of the long-running operation that's returned when you call the `import` method.

#### Response

You should receive a JSON response similar to the following. Import operation is a long-running operation. While the operation is running, the response contains the following fields:

     * `successCount`: indicates the number of FHIR resources that were imported successfully so far.
     * `failureCount`: indicates the number of FHIR resources that failed to be imported so far. This field is displayed only if there are any FHIR resources that failed to be imported.

When the operation is complete, the response contains the following fields:

     * `successCount`: indicates the number of FHIR resources that were imported successfully.
     * `failureCount`: indicates the number of FHIR resources that failed to be imported. This field is displayed only if there are any FHIR resources that failed to be imported.
     * `totalCount`: indicates the number of FHIR resources that are present in the source FHIR store. This field is displayed only if there are any FHIR resources that failed to be imported.
     * `done`: has the value `true` to indicate that the import operation is complete
     * `errorSamples`: provides information about the resources that failed to be imported. This field is displayed only if there are any FHIR resources that failed to be imported.
     * `errorConfig`: provides a path to a Cloud Storage location that contains the error summary log file.
    
    {
     "name": "projects/PROJECT_ID/locations/us/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/operations/IMPORT_OPERATION_ID",
     "metadata": {
       "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.ImportDocumentsMetadata",
       "createTime": "START_TIMESTAMP",
       "updateTime": "END_TIMESTAMP",
       "successCount": "SUCCESS_COUNT",
       "failureCount": "FAILURE_COUNT",
       "totalCount": "TOTAL_COUNT",
     },
     "done": true,
     "response": {
       "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.ImportDocumentsResponse",
      "errorSamples": [ERROR_SAMPLE],
      "errorConfig": {
         "gcsPrefix": "LOG_FILE_LOCATION"
       }
     }
    }
    




### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION" # Values: "us"
    # data_store_id = "YOUR_DATA_STORE_ID"
    # healthcare_project_id = "YOUR_HEALTHCARE_PROJECT_ID"
    # healthcare_location = "YOUR_HEALTHCARE_LOCATION"
    # healthcare_dataset_id = "YOUR_HEALTHCARE_DATASET_ID"
    # healthcare_fihr_store_id = "YOUR_HEALTHCARE_FHIR_STORE_ID"
    
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )
    
    # Create a client
    client = discoveryengine.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html)(client_options=client_options)
    
    # The full resource name of the search engine branch.
    # e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
    parent = client.[branch_path](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_branch_path)(
        project=project_id,
        location=location,
        data_store=data_store_id,
        branch="default_branch",
    )
    
    request = discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html)(
        parent=parent,
        fhir_store_source=discoveryengine.[FhirStoreSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FhirStoreSource.html)(
            fhir_store=client.[fhir_store_path](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_fhir_store_path)(
                healthcare_project_id,
                healthcare_location,
                healthcare_dataset_id,
                healthcare_fihr_store_id,
            ),
        ),
        # Options: `FULL`, `INCREMENTAL`
        reconciliation_mode=discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html).[ReconciliationMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.ReconciliationMode.html).INCREMENTAL,
    )
    
    # Make the request
    operation = client.[import_documents](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_import_documents)(request=request)
    
    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()
    
    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.[ImportDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsMetadata.html)(operation.metadata)
    
    # Handle the response
    print(response)
    print(metadata)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
