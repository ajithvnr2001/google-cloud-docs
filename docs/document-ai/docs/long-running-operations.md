---
url: https://docs.cloud.google.com/document-ai/docs/long-running-operations/
title: Managing long-running operations (LROs) \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:13.040264+00:00
---

# Managing long-running operations (LROs)  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/long-running-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Managing long-running operations (LROs) Stay organized with collections  Save and categorize content based on your preferences. 

[_Long-Running Operations_](https://google.aip.dev/151) are returned by batch processing method calls because they take a longer time to complete than is appropriate for an API response. This is so the calling thread is not held open while many documents are processed. The Document AI API creates an LRO every time you call [`projects.locations.processors.batchProcess`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/batchProcess) through the API or Client Libraries. The LRO tracks the status of the processing job.

You can use the [operations methods](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.operations) that the Document AI API provides to check the status of LROs. You can also list, poll, or cancel LROs. Client libraries calling async method poll internally, enabling callback. (For Python, `await` is enabled.) They also feature a timeout parameter. Within the main LRO returned by .batchProcess, an LRO is created for each document (because batch page-count limits are much higher than the sync `process` call and can take significant time to process). When the main LRO ends, the detailed status of each document LRO is provided.

LROs are managed at the Google Cloud project and location level. When making a request to the API, include the Google Cloud project and the location in which the LRO is running.

The record of an LRO is kept for approximately 30 days after the LRO finishes, meaning that you cannot view or list an LRO after that point.

## Getting details about a long-running operation

The following samples show how to get details about an LRO.

### REST

To get the status of and view details about an LRO, call the [`projects.locations.operations.get`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.operations/get) method.

Suppose that you receive the following response after calling [`projects.locations.processors.batchProcess`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/batchProcess):
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID"
    }
    

The `name` value in the response shows that the Document AI API created an LRO named `projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID`.

You can also retrieve the LRO name by listing long-running operations.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: the [location](https://docs.cloud.google.com/document-ai/docs/regions) where the LRO is running, for example: 
    * `us` \- United States
    * `eu` \- European Union
  * OPERATION_ID: The ID of your operation. The ID is the last element of the name of your operation. For example: 
    * Operation name: `projects/PROJECT_ID/locations/LOCATION/operations/**bc4e1d412863e626**`
    * Operation id: `**bc4e1d412863e626**`



HTTP method and URL: 
    
    
    GET https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata",
        "state": "SUCCEEDED",
        "stateMessage": "Processed 1 document(s) successfully",
        "createTime": "TIMESTAMP",
        "updateTime": "TIMESTAMP",
        "individualProcessStatuses": [
          {
            "inputGcsSource": "INPUT_BUCKET_FOLDER/DOCUMENT1.ext",
            "status": {},
            "outputGcsDestination": "OUTPUT_BUCKET_FOLDER/OPERATION_ID/0",
            "humanReviewStatus": {
              "state": "ERROR",
              "stateMessage": "Sharded document protos are not supported for human review."
            }
          }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessResponse"
      }
    }
    

### Go

For more information, see the [Document AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	documentai "cloud.google.com/go/documentai/apiv1"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := documentai.[NewDocumentProcessorClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1.html#cloud_google_com_go_documentai_apiv1_DocumentProcessorClient_NewDocumentProcessorClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1.html#cloud_google_com_go_documentai_apiv1_DocumentProcessorClient_Close)()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    from google.longrunning.operations_pb2 import GetOperationRequest  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # location = "YOUR_PROCESSOR_LOCATION"  # Format is "us" or "eu"
    # operation_name = "YOUR_OPERATION_NAME"  # Format is "projects/{project_id}/locations/{location}/operations/{operation_id}"
    
    
    def get_operation_sample(location: str, operation_name: str) -> None:
        # You must set the `api_endpoint` if you use a location other than "us".
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        request = GetOperationRequest(name=operation_name)
    
        # Make GetOperation request
        operation = client.[get_operation](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_get_operation)(request=request)
        # Print the Operation Information
        print(operation)
    
    

## Listing long-running operations

The following samples show how to list the LROs in a Google Cloud project and location.

### REST

To list the LROs in a Google Cloud project and location, call the [`projects.locations.operations.list`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.operations/list) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: the [location](https://docs.cloud.google.com/document-ai/docs/regions) where one or more LROs are running, for example: 
    * `us` \- United States
    * `eu` \- European Union
  * FILTER: (Required) Query for LROs to return. Options: 
    * TYPE: (Required) LRO type to list. Options:
      * `BATCH_PROCESS_DOCUMENTS`
      * `CREATE_PROCESSOR_VERSION`
      * `DELETE_PROCESSOR`
      * `ENABLE_PROCESSOR`
      * `DISABLE_PROCESSOR`
      * `UPDATE_HUMAN_REVIEW_CONFIG`
      * `HUMAN_REVIEW_EVENT`
      * `CREATE_LABELER_POOL`
      * `UPDATE_LABELER_POOL`
      * `DELETE_LABELER_POOL`
      * `DEPLOY_PROCESSOR_VERSION`
      * `UNDEPLOY_PROCESSOR_VERSION`
      * `DELETE_PROCESSOR_VERSION`
      * `SET_DEFAULT_PROCESSOR_VERSION`
      * `EVALUATE_PROCESSOR_VERSION`
      * `EXPORT_PROCESSOR_VERSION`
      * `UPDATE_DATASET`
      * `IMPORT_DOCUMENTS`
      * `ANALYZE_HITL_DATA`
      * `BATCH_MOVE_DOCUMENTS`
      * `RESYNC_DATASET`
      * `BATCH_DELETE_DOCUMENTS`
      * `DELETE_DATA_LABELING_JOB`
      * `EXPORT_DOCUMENTS`



HTTP method and URL: 
    
    
    GET https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations?filter=TYPE=TYPE

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations?filter=TYPE=TYPE"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations?filter=TYPE=TYPE" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "operations": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata",
            "state": "SUCCEEDED",
            "stateMessage": "Processed 1 document(s) successfully",
            "createTime": "TIMESTAMP",
            "updateTime": "TIMESTAMP",
            "individualProcessStatuses": [
              {
                "inputGcsSource": "INPUT_BUCKET_FOLDER/DOCUMENT1.ext",
                "status": {},
                "outputGcsDestination": "OUTPUT_BUCKET_FOLDER/OPERATION_ID/0",
                "humanReviewStatus": {
                  "state": "ERROR",
                  "stateMessage": "Sharded document protos are not supported for human review."
                }
              }
            ]
          },
          "done": true,
          "response": {
            "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessResponse"
          }
        },
        ...
      ]
    }
    

### Go

For more information, see the [Document AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	documentai "cloud.google.com/go/documentai/apiv1"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := documentai.[NewDocumentProcessorClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1.html#cloud_google_com_go_documentai_apiv1_DocumentProcessorClient_NewDocumentProcessorClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1.html#cloud_google_com_go_documentai_apiv1_DocumentProcessorClient_Close)()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    from google.longrunning.operations_pb2 import ListOperationsRequest  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_PROCESSOR_LOCATION"  # Format is "us" or "eu"
    
    # Create filter in https://google.aip.dev/160 syntax
    # For full options, refer to:
    # https://cloud.google.com/document-ai/docs/long-running-operations#listing_long-running_operations
    # operations_filter = 'YOUR_FILTER'
    
    # Example:
    # operations_filter = "TYPE=BATCH_PROCESS_DOCUMENTS AND STATE=RUNNING"
    
    
    def list_operations_sample(
        project_id: str, location: str, operations_filter: str
    ) -> None:
        # You must set the `api_endpoint` if you use a location other than "us".
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # Format: `projects/{project_id}/locations/{location}`
        name = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_common_location_path)(project=project_id, location=location)
        request = ListOperationsRequest(
            name=f"{name}/operations",
            filter=operations_filter,
        )
    
        # Make ListOperations request
        operations = client.[list_operations](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_list_operations)(request=request)
    
        # Print the Operation Information
        print(operations)
    
    

## Polling a long-running operation

The following samples show how to poll the status of an LRO.

### REST

To poll an LRO, repeatedly call the [`projects.locations.operations.get`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.operations/get) method until the operation finishes. Use a backoff between each poll request, such as 10 seconds.

Before using any of the request data below, make the following replacements:

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location where the LRO is running
  * OPERATION_ID: the identifier for the LRO



HTTP method and URL:
    
    
    GET https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
      

To send your request, choose one of these options:

**Note:** If you are not executing the commands below from [Cloud Shell](https://docs.cloud.google.com/shell/docs) or [Compute Engine](https://docs.cloud.google.com/compute), ensure you have set the [**`GOOGLE_APPLICATION_CREDENTIALS`**](https://docs.cloud.google.com/docs/authentication/production) environment variable to your service account private key file path.

### curl

Execute the following command to poll for the status of an LRO every 10 seconds:
    
    
    while true; \
        do curl -X GET \
        -H "Authorization: Bearer "$(gcloud auth print-access-token) \
        "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"; \
        sleep 10; \
        done

You should receive a JSON response every 10 seconds. While the operation is running, the response will contain `"state": "RUNNING"`. When the operation finishes, the response will contain `"state": "SUCCEEDED"` and `"done": true`.

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata",
        "state": "RUNNING",
        "createTime": "TIMESTAMP",
        "updateTime": "TIMESTAMP"
      }
    }
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata",
        "state": "RUNNING",
        "createTime": "TIMESTAMP",
        "updateTime": "TIMESTAMP"
      }
    }
    ...
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata",
        "state": "SUCCEEDED",
        "stateMessage": "Processed 1 document(s) successfully",
        "createTime": "TIMESTAMP",
        "updateTime": "TIMESTAMP",
        "individualProcessStatuses": [
          {
            "inputGcsSource": "INPUT_BUCKET_FOLDER/DOCUMENT1.ext",
            "status": {},
            "outputGcsDestination": "OUTPUT_BUCKET_FOLDER/OPERATION_ID/0",
            "humanReviewStatus": {
              "state": "ERROR",
              "stateMessage": "Sharded document protos are not supported for human review."
            }
          }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessResponse"
      }
    }
    

### PowerShell

Execute the following command to poll for the status of an LRO every ten seconds:
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Do {
      Invoke-WebRequest `
        -Method Get `
        -Headers $headers `
        -Uri "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content
    sleep 10
    }
    
    while ($true)

You should receive a JSON response every 10 seconds. While the operation is running, the response will contain `"state": "RUNNING"`. When the operation finishes, the response will contain `"state": "SUCCEEDED"` and `"done": true`.

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata",
        "state": "RUNNING",
        "createTime": "TIMESTAMP",
        "updateTime": "TIMESTAMP"
      }
    }
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata",
        "state": "RUNNING",
        "createTime": "TIMESTAMP",
        "updateTime": "TIMESTAMP"
      }
    }
    ...
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata",
        "state": "SUCCEEDED",
        "stateMessage": "Processed 1 document(s) successfully",
        "createTime": "TIMESTAMP",
        "updateTime": "TIMESTAMP",
        "individualProcessStatuses": [
          {
            "inputGcsSource": "INPUT_BUCKET_FOLDER/DOCUMENT1.ext",
            "status": {},
            "outputGcsDestination": "OUTPUT_BUCKET_FOLDER/OPERATION_ID/0",
            "humanReviewStatus": {
              "state": "ERROR",
              "stateMessage": "Sharded document protos are not supported for human review."
            }
          }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessResponse"
      }
    }
    

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from time import sleep
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    from google.longrunning.operations_pb2 import GetOperationRequest  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # location = "YOUR_PROCESSOR_LOCATION"  # Format is "us" or "eu"
    # operation_name = "YOUR_OPERATION_NAME"  # Format is "projects/{project_id}/locations/{location}/operations/{operation_id}"
    
    
    def poll_operation_sample(location: str, operation_name: str) -> None:
        # You must set the `api_endpoint` if you use a location other than "us".
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        request = GetOperationRequest(name=operation_name)
    
        while True:
            # Make GetOperation request
            operation = client.[get_operation](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_get_operation)(request=request)
            # Print the Operation Information
            print(operation)
    
            # Stop polling when Operation is no longer running
            if operation.done:
                break
    
            # Wait 10 seconds before polling again
            sleep(10)
    
    

**Note:** The code is a generic function designed for polling an LRO to check the status of single or multiple batch_process jobs. In cases where you want to wait until the `batch_process_documents` operation is completed fully, client libraries offer their own polling methods. Refer to [Batch processing](https://docs.cloud.google.com/document-ai/docs/send-request#batch-process) for more information.

## Cancelling a long-running operation

The following samples show how to cancel an LRO while it is running.

### REST

To cancel an LRO, call the [`projects.locations.operations.cancel`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.operations/cancel) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: the [location](https://docs.cloud.google.com/document-ai/docs/regions) where the LRO is running, for example: 
    * `us` \- United States
    * `eu` \- European Union
  * OPERATION_ID: The ID of your operation. The ID is the last element of the name of your operation. For example: 
    * Operation name: `projects/PROJECT_ID/locations/LOCATION/operations/**bc4e1d412863e626**`
    * Operation id: `**bc4e1d412863e626**`



HTTP method and URL: 
    
    
    POST https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID:cancel

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID:cancel"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID:cancel" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

If you attempt to cancel an operation that has already completed, you should receive the following error message: 
    
    
      "error": {
          "code": 400,
          "message": "Operation has completed and cannot be cancelled: 'PROJECT_ID/locations/LOCATION/operations/OPERATION_ID'.",
          "status": "FAILED_PRECONDITION"
      }

### Go

For more information, see the [Document AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	documentai "cloud.google.com/go/documentai/apiv1"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := documentai.[NewDocumentProcessorClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1.html#cloud_google_com_go_documentai_apiv1_DocumentProcessorClient_NewDocumentProcessorClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1.html#cloud_google_com_go_documentai_apiv1_DocumentProcessorClient_Close)()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    from google.longrunning.operations_pb2 import CancelOperationRequest  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # location = "YOUR_PROCESSOR_LOCATION"  # Format is "us" or "eu"
    # operation_name = "YOUR_OPERATION_NAME"  # Format is "projects/{project_id}/locations/{location}/operations/{operation_id}"
    
    
    def cancel_operation_sample(location: str, operation_name: str) -> None:
        # You must set the `api_endpoint` if you use a location other than "us".
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        request = CancelOperationRequest(name=operation_name)
    
        # Make CancelOperation request
        client.[cancel_operation](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_cancel_operation)(request=request)
        print(f"Operation {operation_name} cancelled")
    
    

[ Previous arrow_back  Handle response  ](https://docs.cloud.google.com/document-ai/docs/handle-response)

[ Next Custom metadata  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/custom-metadata-labels)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
