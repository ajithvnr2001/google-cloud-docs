---
url: https://docs.cloud.google.com/document-ai/docs/create-processor/
title: Creating and managing processors \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:51.349270+00:00
---

# Creating and managing processors  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/create-processor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Creating and managing processors Stay organized with collections  Save and categorize content based on your preferences. 

Before you can send documents to be processed, you must first create your own instance of a processor. This page provides details about creating and managing processors.

## Available processors

To create a processor instance using API, you need to know the name for each processor type. Get this list dynamically (with the code below), because your access may change.

The publicly available processor types are:

### Digitize processors

  * `OCR_PROCESSOR`
  * `FORM_PARSER_PROCESSOR`
  * `LAYOUT_PARSER_PROCESSOR`



### Pretrained processors

  * `BANK_STATEMENT_PROCESSOR`
  * `EXPENSE_PROCESSOR`
  * `FORM_W2_PROCESSOR`
  * `ID_PROOFING_PROCESSOR`
  * `INVOICE_PROCESSOR`
  * `PAYSTUB_PROCESSOR`
  * `US_DRIVER_LICENSE_PROCESSOR`
  * `US_PASSPORT_PROCESSOR`
  * `UTILITY_PROCESSOR`



### Extract / classify / split processors

  * `CUSTOM_EXTRACTION_PROCESSOR`
  * `CUSTOM_CLASSIFICATION_PROCESSOR`
  * `CUSTOM_SPLITTING_PROCESSOR`
  * `SUMMARIZER_PROCESSOR`



## List processor types

### Web UI

  1. In the Google Cloud console, in the Document AI section, go to the **Processor Gallery** page.

[Go to Processor Gallery](https://console.cloud.google.com/ai/document-ai/processor-library)

  2. View or search the list of processor types.




### REST

This sample shows how to list the available processor types for your project using the [`fetchProcessorTypes`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations/fetchProcessorTypes) method.

Before using any of the request data, make the following replacements: 

  * LOCATION: your processor's [location](https://docs.cloud.google.com/document-ai/docs/regions), for example: 
    * `us` \- United States
    * `eu` \- European Union
  * PROJECT_ID: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    GET https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:fetchProcessorTypes

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:fetchProcessorTypes"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:fetchProcessorTypes" | Select-Object -Expand Content

The response is a list of [`ProcessorType`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations/fetchProcessorTypes#ProcessorType) which shows the available processor types, along with the category and available locations. 
    
    
    {
      "processorTypes": [
      [
        ...
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/processorTypes/FORM_PARSER_PROCESSOR",
          "type": "FORM_PARSER_PROCESSOR",
          "category": "GENERAL",
          "availableLocations": [
            {
              "locationId": "eu"
            },
            {
              "locationId": "us"
            }
          ],
          "allowCreation": true,
          "launchStage": "GA"
        },
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/processorTypes/OCR_PROCESSOR",
          "type": "OCR_PROCESSOR",
          "category": "GENERAL",
          "availableLocations": [
            {
              "locationId": "eu"
            },
            {
              "locationId": "us"
            }
          ],
          "allowCreation": true,
          "launchStage": "GA"
        },
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/processorTypes/INVOICE_PROCESSOR",
          "type": "INVOICE_PROCESSOR",
          "category": "SPECIALIZED",
          "availableLocations": [
            {
              "locationId": "eu"
            },
            {
              "locationId": "us"
            }
          ],
          "allowCreation": true,
          "launchStage": "GA"
        },
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/processorTypes/US_DRIVER_LICENSE_PROCESSOR",
          "type": "US_DRIVER_LICENSE_PROCESSOR",
          "category": "SPECIALIZED",
          "availableLocations": [
            {
              "locationId": "us"
            },
            {
              "locationId": "eu"
            }
          ],
          "allowCreation": true,
          "launchStage": "GA"
        },
        ...
      ]
    }
    

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
    
    
    def fetch_processor_types_sample(project_id: str, location: str) -> None:
        # You must set the api_endpoint if you use a location other than 'us'.
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # The full resource name of the location
        # e.g.: projects/project_id/locations/location
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_common_location_path)(project_id, location)
    
        # Fetch all processor types
        response = client.[fetch_processor_types](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_fetch_processor_types)(parent=parent)
    
        print("Processor types:")
        # Print the available processor types
        for processor_type in response.processor_types:
            if processor_type.allow_creation:
                print(processor_type.type_)
    
    

### Go

For more information, see the [Document AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	documentai "cloud.google.com/go/documentai/apiv1"
    	documentaipb "cloud.google.com/go/documentai/apiv1/documentaipb"
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
    
    	req := &documentaipb.FetchProcessorTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/documentai/apiv1/documentaipb#FetchProcessorTypesRequest.
    	}
    	resp, err := c.FetchProcessorTypes(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

For more information, see the [Document AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/overview). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.documentai.v1.[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html);
    import com.google.cloud.documentai.v1.[FetchProcessorTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.FetchProcessorTypesRequest.html);
    import com.google.cloud.documentai.v1.[FetchProcessorTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.FetchProcessorTypesResponse.html);
    import com.google.cloud.documentai.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.LocationName.html);
    
    public class SyncFetchProcessorTypes {
    
      public static void main(String[] args) throws Exception {
        syncFetchProcessorTypes();
      }
    
      public static void syncFetchProcessorTypes() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html) documentProcessorServiceClient =
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html).create()) {
          [FetchProcessorTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.FetchProcessorTypesRequest.html) request =
              [FetchProcessorTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.FetchProcessorTypesRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .build();
          [FetchProcessorTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.FetchProcessorTypesResponse.html) response =
              documentProcessorServiceClient.fetchProcessorTypes(request);
        }
      }
    }

### Ruby

For more information, see the [Document AI Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/document_ai/v1"
    
    ##
    # Snippet for the fetch_processor_types call in the DocumentProcessorService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client#fetch_processor_types.
    #
    def fetch_processor_types
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DocumentAI::V1::FetchProcessorTypesRequest.new
    
      # Call the fetch_processor_types method.
      result = client.fetch_processor_types request
    
      # The returned object is of type Google::Cloud::DocumentAI::V1::FetchProcessorTypesResponse.
      p result
    end

### C#

For more information, see the [Document AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.html);
    
    public sealed partial class GeneratedDocumentProcessorServiceClientSnippets
    {
        /// <summary>Snippet for FetchProcessorTypes</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void FetchProcessorTypesRequestObject()
        {
            // Create client
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html) documentProcessorServiceClient = [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_Create)();
            // Initialize request argument(s)
            [FetchProcessorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.FetchProcessorTypesRequest.html) request = new [FetchProcessorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.FetchProcessorTypesRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
            };
            // Make the request
            [FetchProcessorTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.FetchProcessorTypesResponse.html) response = documentProcessorServiceClient.[FetchProcessorTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_FetchProcessorTypes_Google_Api_Gax_ResourceNames_LocationName_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

## Create a processor

### Web UI

  1. In the Google Cloud console, in the Document AI section, go to the **Processor Gallery** page.

[Go to Processor Gallery](https://console.cloud.google.com/ai/document-ai/processor-library)

  2. View or search the processor gallery to find the processor you want to create.

  3. Click on the processor type from the list you want to create.

  4. In the side **Create processor** window specify a processor name.

  5. Select your [**Region**](https://docs.cloud.google.com/document-ai/docs/regions) from the list.

  6. Click **Create** to create your processor.

You will be taken to the processor's **Overview** tab, which contains information such as _Name_ , _ID_ , _Type_ , and _Prediction endpoint_. Use this endpoint to [send requests](https://docs.cloud.google.com/document-ai/docs/send-request).




### REST

This sample shows you how to create a new [`processor`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors#resource:-processor) using the [`processors.create`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/create) method.

Before using any of the request data, make the following replacements: 

  * LOCATION: your processor's [location](https://docs.cloud.google.com/document-ai/docs/regions), for example: 
    * `us` \- United States
    * `eu` \- European Union
  * PROJECT_ID: Your Google Cloud project ID.
  * PROCESSOR_TYPE: Type of the Processor, for example: 
    * `OCR_PROCESSOR`
    * `FORM_PARSER_PROCESSOR`
    * `INVOICE_PROCESSOR`
    * `US_DRIVER_LICENSE_PROCESSOR`
  * DISPLAY_NAME: Display name for the processor.



HTTP method and URL: 
    
    
    POST https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors

Request JSON body: 
    
    
    {
      "type": "PROCESSOR_TYPE",
      "displayName": "DISPLAY_NAME"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format. The response contains information about the newly created processor, such as the `processEndpoint` and full processor name. Both of these strings contain the unique processor ID (e.g. `aa22ec60216f6ccc`) needed to [send requests](https://docs.cloud.google.com/document-ai/docs/send-request). 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID",
      "type": "PROCESSOR_TYPE",
      "displayName": "DISPLAY_NAME",
      "state": "ENABLED",
      "processEndpoint": "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID:process",
      "createTime": "2022-03-02T22:50:31.395849Z",
      "defaultProcessorVersion": "projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID/processorVersions/pretrained"
    }
    

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
    # processor_display_name = 'YOUR_PROCESSOR_DISPLAY_NAME' # Must be unique per project, e.g.: 'My Processor'
    # processor_type = 'YOUR_PROCESSOR_TYPE' # Use fetch_processor_types to get available processor types
    
    
    def create_processor_sample(
        project_id: str, location: str, processor_display_name: str, processor_type: str
    ) -> None:
        # You must set the api_endpoint if you use a location other than 'us'.
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # The full resource name of the location
        # e.g.: projects/project_id/locations/location
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_common_location_path)(project_id, location)
    
        # Create a processor
        processor = client.[create_processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_create_processor)(
            parent=parent,
            processor=documentai.[Processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Processor.html)(
                display_name=processor_display_name, type_=processor_type
            ),
        )
    
        # Print the processor information
        print(f"Processor Name: {processor.name}")
        print(f"Processor Display Name: {processor.display_name}")
        print(f"Processor Type: {processor.type_}")
    
    

### Go

For more information, see the [Document AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	documentai "cloud.google.com/go/documentai/apiv1"
    	documentaipb "cloud.google.com/go/documentai/apiv1/documentaipb"
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
    
    	req := &documentaipb.CreateProcessorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/documentai/apiv1/documentaipb#CreateProcessorRequest.
    	}
    	resp, err := c.CreateProcessor(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

For more information, see the [Document AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/overview). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.documentai.v1.[CreateProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.CreateProcessorRequest.html);
    import com.google.cloud.documentai.v1.[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html);
    import com.google.cloud.documentai.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.LocationName.html);
    import com.google.cloud.documentai.v1.[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor.html);
    
    public class SyncCreateProcessor {
    
      public static void main(String[] args) throws Exception {
        syncCreateProcessor();
      }
    
      public static void syncCreateProcessor() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html) documentProcessorServiceClient =
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html).create()) {
          [CreateProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.CreateProcessorRequest.html) request =
              [CreateProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.CreateProcessorRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .setProcessor([Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor.html).newBuilder().build())
                  .build();
          [Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor.html) response = documentProcessorServiceClient.createProcessor(request);
        }
      }
    }

### Ruby

For more information, see the [Document AI Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/document_ai/v1"
    
    ##
    # Snippet for the create_processor call in the DocumentProcessorService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client#create_processor.
    #
    def create_processor
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DocumentAI::V1::CreateProcessorRequest.new
    
      # Call the create_processor method.
      result = client.create_processor request
    
      # The returned object is of type Google::Cloud::DocumentAI::V1::Processor.
      p result
    end

### C#

For more information, see the [Document AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.html);
    
    public sealed partial class GeneratedDocumentProcessorServiceClientSnippets
    {
        /// <summary>Snippet for CreateProcessor</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void CreateProcessorRequestObject()
        {
            // Create client
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html) documentProcessorServiceClient = [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_Create)();
            // Initialize request argument(s)
            [CreateProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.CreateProcessorRequest.html) request = new [CreateProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.CreateProcessorRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                Processor = new [Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Processor.html)(),
            };
            // Make the request
            [Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Processor.html) response = documentProcessorServiceClient.[CreateProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_CreateProcessor_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_DocumentAI_V1_Processor_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

## Get a list of processors

### Web UI

  1. In the Google Cloud console, in the Document AI section, go to the **Processors** page.

[Go to the Processors page](https://console.cloud.google.com/ai/document-ai/processors)

The **Processors** page lists all of the processors along with their _Name_ , _Status_ , _Region_ , and _Type_.




### REST

This sample shows you how to list existing [`processors`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors#resource:-processor) using the [`processors.list`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/list) method.

Before using any of the request data, make the following replacements: 

  * LOCATION: your processor's [location](https://docs.cloud.google.com/document-ai/docs/regions), for example: 
    * `us` \- United States
    * `eu` \- European Union
  * PROJECT_ID: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    GET https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors" | Select-Object -Expand Content

The response is a list of [`Processors`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/list#response-body), which contains information about each processor such as its `name`, `type`, `state`, and other details. 
    
    
    {
      "processors": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID",
          "type": "FORM_PARSER_PROCESSOR",
          "displayName": "DISPLAY_NAME",
          "state": "ENABLED",
          "processEndpoint": "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID:process",
          "createTime": "2022-03-02T22:33:54.938593Z",
          "defaultProcessorVersion": "projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID/processorVersions/pretrained"
        }
      ]
    }
    

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
    
    
    def list_processors_sample(project_id: str, location: str) -> None:
        # You must set the api_endpoint if you use a location other than 'us'.
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # The full resource name of the location
        # e.g.: projects/project_id/locations/location
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_common_location_path)(project_id, location)
    
        # Make ListProcessors request
        processor_list = client.[list_processors](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_list_processors)(parent=parent)
    
        # Print the processor information
        for processor in processor_list:
            print(f"Processor Name: {processor.name}")
            print(f"Processor Display Name: {processor.display_name}")
            print(f"Processor Type: {processor.type_}")
            print("")
    
    

### Go

For more information, see the [Document AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	documentai "cloud.google.com/go/documentai/apiv1"
    	documentaipb "cloud.google.com/go/documentai/apiv1/documentaipb"
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
    
    	req := &documentaipb.ListProcessorsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/documentai/apiv1/documentaipb#ListProcessorsRequest.
    	}
    	it := c.ListProcessors(ctx, req)
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
    		_ = it.Response.(*documentaipb.ListProcessorsResponse)
    	}
    }
    

### Java

For more information, see the [Document AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/overview). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.documentai.v1.[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html);
    import com.google.cloud.documentai.v1.[ListProcessorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorsRequest.html);
    import com.google.cloud.documentai.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.LocationName.html);
    import com.google.cloud.documentai.v1.[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor.html);
    
    public class SyncListProcessors {
    
      public static void main(String[] args) throws Exception {
        syncListProcessors();
      }
    
      public static void syncListProcessors() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html) documentProcessorServiceClient =
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html).create()) {
          [ListProcessorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorsRequest.html) request =
              [ListProcessorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorsRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .build();
          for ([Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor.html) element :
              documentProcessorServiceClient.listProcessors(request).iterateAll()) {
            // doThingsWith(element);
          }
        }
      }
    }

### Ruby

For more information, see the [Document AI Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/document_ai/v1"
    
    ##
    # Snippet for the list_processors call in the DocumentProcessorService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client#list_processors.
    #
    def list_processors
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DocumentAI::V1::ListProcessorsRequest.new
    
      # Call the list_processors method.
      result = client.list_processors request
    
      # The returned object is of type Gapic::PagedEnumerable. You can iterate
      # over elements, and API calls will be issued to fetch pages as needed.
      result.each do |item|
        # Each element is of type ::Google::Cloud::DocumentAI::V1::Processor.
        p item
      end
    end

### C#

For more information, see the [Document AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.html);
    using System;
    
    public sealed partial class GeneratedDocumentProcessorServiceClientSnippets
    {
        /// <summary>Snippet for ListProcessors</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void ListProcessorsRequestObject()
        {
            // Create client
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html) documentProcessorServiceClient = [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_Create)();
            // Initialize request argument(s)
            [ListProcessorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorsRequest.html) request = new [ListProcessorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorsRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
            };
            // Make the request
            PagedEnumerable<ListProcessorsResponse, Processor> response = documentProcessorServiceClient.[ListProcessors](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_ListProcessors_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Iterate over all response items, lazily performing RPCs as required
            foreach ([Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Processor.html) item in response)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
    
            // Or iterate over pages (of server-defined size), performing one RPC per page
            foreach ([ListProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorsResponse.html) page in response.AsRawResponses())
            {
                // Do something with each page of items
                Console.WriteLine("A page of results:");
                foreach ([Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Processor.html) item in page)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
            }
    
            // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
            int pageSize = 10;
            Page<Processor> singlePage = response.ReadPage(pageSize);
            // Do something with the page of items
            Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
            foreach ([Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Processor.html) item in singlePage)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
            // Store the pageToken, for when the next page is required.
            string nextPageToken = singlePage.NextPageToken;
        }
    }

## View details about a processor

### Web UI

  1. In the Google Cloud console, in the Document AI section, go to the **Processors** page.

[Go to the Processors page](https://console.cloud.google.com/ai/document-ai/processors)

  2. From the list of processors, click on the name of the processor that you want to view details for.

You will be taken to the processor's **Overview** tab, which contains information such as _Name_ , _ID_ , _Type_ , and _Prediction endpoint_.




### REST

This sample shows you how to get details about an existing [`Processor`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors#Processor) using the [`processors.get`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/get) method.

Before using any of the request data, make the following replacements: 

  * LOCATION: your processor's [location](https://docs.cloud.google.com/document-ai/docs/regions), for example: 
    * `us` \- United States
    * `eu` \- European Union
  * PROJECT_ID: Your Google Cloud project ID.
  * PROCESSOR_ID: the ID of your custom processor.



HTTP method and URL: 
    
    
    GET https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID" | Select-Object -Expand Content

The response is a [`Processor`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/get#response-body), which contains information about the processor such as its `name`, `type`, `state`, and other details. 
    
    
    {
      "processors": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID",
          "type": "OCR_PROCESSOR",
          "displayName": "DISPLAY_NAME",
          "state": "ENABLED",
          "processEndpoint": "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID:process",
          "createTime": "2022-03-02T22:33:54.938593Z",
          "defaultProcessorVersion": "projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID/processorVersions/pretrained"
        }
      ]
    }
    

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
    # processor_id = 'YOUR_PROCESSOR_ID'
    
    
    def get_processor_sample(project_id: str, location: str, processor_id: str) -> None:
        # You must set the api_endpoint if you use a location other than 'us'.
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # The full resource name of the processor, e.g.:
        # projects/{project_id}/locations/{location}/processors/{processor_id}
        name = client.[processor_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_path)(project_id, location, processor_id)
    
        # Make GetProcessor request
        processor = client.[get_processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_get_processor)(name=name)
    
        # Print the processor information
        print(f"Processor Name: {processor.name}")
        print(f"Processor Display Name: {processor.display_name}")
        print(f"Processor Type: {processor.type_}")
    
    

### Go

For more information, see the [Document AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	documentai "cloud.google.com/go/documentai/apiv1"
    	documentaipb "cloud.google.com/go/documentai/apiv1/documentaipb"
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
    
    	req := &documentaipb.GetProcessorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/documentai/apiv1/documentaipb#GetProcessorRequest.
    	}
    	resp, err := c.GetProcessor(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

For more information, see the [Document AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/overview). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.documentai.v1.[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html);
    import com.google.cloud.documentai.v1.[GetProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GetProcessorRequest.html);
    import com.google.cloud.documentai.v1.[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor.html);
    import com.google.cloud.documentai.v1.[ProcessorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorName.html);
    
    public class SyncGetProcessor {
    
      public static void main(String[] args) throws Exception {
        syncGetProcessor();
      }
    
      public static void syncGetProcessor() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html) documentProcessorServiceClient =
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html).create()) {
          [GetProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GetProcessorRequest.html) request =
              [GetProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GetProcessorRequest.html).newBuilder()
                  .setName([ProcessorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorName.html).of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
                  .build();
          [Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor.html) response = documentProcessorServiceClient.getProcessor(request);
        }
      }
    }

### Ruby

For more information, see the [Document AI Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/document_ai/v1"
    
    ##
    # Snippet for the get_processor call in the DocumentProcessorService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client#get_processor.
    #
    def get_processor
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DocumentAI::V1::GetProcessorRequest.new
    
      # Call the get_processor method.
      result = client.get_processor request
    
      # The returned object is of type Google::Cloud::DocumentAI::V1::Processor.
      p result
    end

### C#

For more information, see the [Document AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.html);
    
    public sealed partial class GeneratedDocumentProcessorServiceClientSnippets
    {
        /// <summary>Snippet for GetProcessor</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void GetProcessorRequestObject()
        {
            // Create client
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html) documentProcessorServiceClient = [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_Create)();
            // Initialize request argument(s)
            [GetProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.GetProcessorRequest.html) request = new [GetProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.GetProcessorRequest.html)
            {
                ProcessorName = [ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName.html).[FromProjectLocationProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName.html#Google_Cloud_DocumentAI_V1_ProcessorName_FromProjectLocationProcessor_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[PROCESSOR]"),
            };
            // Make the request
            [Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Processor.html) response = documentProcessorServiceClient.[GetProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_GetProcessor_Google_Cloud_DocumentAI_V1_GetProcessorRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

## Enable a processor

### Web UI

  1. In the Google Cloud console, in the Document AI section, go to the **Processors** page.

[Go to the Processors page](https://console.cloud.google.com/ai/document-ai/processors)

  2. Next to your processor, in the **Action menu** more_vert, click **Enable processor**.




### REST

This sample shows you how to enable an existing [`Processor`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors#Processor) using the [`processors.enable`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/enable) method.

Before using any of the request data, make the following replacements: 

  * LOCATION: your processor's [location](https://docs.cloud.google.com/document-ai/docs/regions), for example: 
    * `us` \- United States
    * `eu` \- European Union
  * PROJECT_ID: Your Google Cloud project ID.
  * PROCESSOR_ID: the ID of your custom processor.



HTTP method and URL: 
    
    
    POST https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID:enable

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID:enable"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID:enable" | Select-Object -Expand Content

The response is a [long running operation](https://docs.cloud.google.com/document-ai/docs/long-running-operations)
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.EnableProcessorMetadata",
        "commonMetadata": {
          "state": "RUNNING",
          "createTime": "2022-03-02T22:52:49.957096Z",
          "updateTime": "2022-03-02T22:52:50.175976Z",
          "resource": "projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID"
        }
      }
    }
    

  1. To poll the long-running operation, call [operations.get](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.operations/get):
         
         curl -X GET https://documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION \
                -H "Authorization: Bearer "$(gcloud auth print-access-token) \
                -H "X-Goog-User-Project: PROJECT_ID"

  2. The [`EnableProcessorMetadata`](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/EnableProcessorMetadata) in the response indicates the state of the operation:
         
         {
           "name": "projects/<project_id>/locations/<location>/operations/<operation>",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.documentai.v1.EnableProcessorMetadata",
             "commonMetadata": {
               "state": "SUCCEEDED",
               "createTime": "2022-03-02T22:52:49.957096Z",
               "updateTime": "2022-03-02T22:52:50.175976Z",
               "resource": "projects/<project_id>/locations/<location>/processors/<processor_id>"
             }
           },
           "done": true,
           "response": {
             "@type": "type.googleapis.com/google.cloud.documentai.v1.EnableProcessorResponse"
           }
         }
         




### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.api_core.exceptions import FailedPrecondition
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
    # processor_id = 'YOUR_PROCESSOR_ID'
    
    
    def enable_processor_sample(project_id: str, location: str, processor_id: str) -> None:
        # You must set the api_endpoint if you use a location other than 'us'.
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # The full resource name of the location
        # e.g.: projects/project_id/locations/location/processors/processor_id
        processor_name = client.[processor_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_path)(project_id, location, processor_id)
        request = documentai.[EnableProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.EnableProcessorRequest.html)(name=processor_name)
    
        # Make EnableProcessor request
        try:
            operation = client.[enable_processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_enable_processor)(request=request)
    
            # Print operation name
            print(operation.operation.name)
            # Wait for operation to complete
            operation.result()
        # Cannot enable a processor that is already enabled
        except FailedPrecondition as e:
            print(e.message)
    
    

### Go

For more information, see the [Document AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	documentai "cloud.google.com/go/documentai/apiv1"
    	documentaipb "cloud.google.com/go/documentai/apiv1/documentaipb"
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
    
    	req := &documentaipb.EnableProcessorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/documentai/apiv1/documentaipb#EnableProcessorRequest.
    	}
    	op, err := c.EnableProcessor(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

For more information, see the [Document AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/overview). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.documentai.v1.[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html);
    import com.google.cloud.documentai.v1.[EnableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorRequest.html);
    import com.google.cloud.documentai.v1.[EnableProcessorResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorResponse.html);
    import com.google.cloud.documentai.v1.[ProcessorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorName.html);
    
    public class SyncEnableProcessor {
    
      public static void main(String[] args) throws Exception {
        syncEnableProcessor();
      }
    
      public static void syncEnableProcessor() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html) documentProcessorServiceClient =
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html).create()) {
          [EnableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorRequest.html) request =
              [EnableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorRequest.html).newBuilder()
                  .setName([ProcessorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorName.html).of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
                  .build();
          [EnableProcessorResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorResponse.html) response =
              documentProcessorServiceClient.[enableProcessorAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html#com_google_cloud_documentai_v1_DocumentProcessorServiceClient_enableProcessorAsync_com_google_cloud_documentai_v1_EnableProcessorRequest_)(request).get();
        }
      }
    }

### Ruby

For more information, see the [Document AI Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/document_ai/v1"
    
    ##
    # Snippet for the enable_processor call in the DocumentProcessorService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client#enable_processor.
    #
    def enable_processor
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DocumentAI::V1::EnableProcessorRequest.new
    
      # Call the enable_processor method.
      result = client.enable_processor request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

### C#

For more information, see the [Document AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedDocumentProcessorServiceClientSnippets
    {
        /// <summary>Snippet for EnableProcessor</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void EnableProcessorRequestObject()
        {
            // Create client
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html) documentProcessorServiceClient = [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_Create)();
            // Initialize request argument(s)
            [EnableProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EnableProcessorRequest.html) request = new [EnableProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EnableProcessorRequest.html)
            {
                ProcessorName = [ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName.html).[FromProjectLocationProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName.html#Google_Cloud_DocumentAI_V1_ProcessorName_FromProjectLocationProcessor_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[PROCESSOR]"),
            };
            // Make the request
            Operation<EnableProcessorResponse, EnableProcessorMetadata> response = documentProcessorServiceClient.[EnableProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_EnableProcessor_Google_Cloud_DocumentAI_V1_EnableProcessorRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<EnableProcessorResponse, EnableProcessorMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [EnableProcessorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EnableProcessorResponse.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<EnableProcessorResponse, EnableProcessorMetadata> retrievedResponse = documentProcessorServiceClient.[PollOnceEnableProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_PollOnceEnableProcessor_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [EnableProcessorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EnableProcessorResponse.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

## Disable a processor

**Note:** Disabled processors count toward the number of created processors quota.

### Web UI

  1. In the Google Cloud console, in the Document AI section, go to the **Processors** page.

[Go to the Processors page](https://console.cloud.google.com/ai/document-ai/processors)

     1. Next to your processor, in the **Action menu** more_vert, click **Disable processor**.



### REST

This sample shows you how to disable an existing [`Processor`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors#Processor) using the [`processors.disable`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/disable) method.

Before using any of the request data, make the following replacements: 

  * LOCATION: your processor's [location](https://docs.cloud.google.com/document-ai/docs/regions), for example: 
    * `us` \- United States
    * `eu` \- European Union
  * PROJECT_ID: Your Google Cloud project ID.
  * PROCESSOR_ID: the ID of your custom processor.



HTTP method and URL: 
    
    
    POST https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID:disable

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID:disable"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID:disable" | Select-Object -Expand Content

The response is a [long running operation](https://docs.cloud.google.com/document-ai/docs/long-running-operations)
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.DisableProcessorMetadata",
        "commonMetadata": {
          "state": "RUNNING",
          "createTime": "2022-03-02T22:52:49.957096Z",
          "updateTime": "2022-03-02T22:52:50.175976Z",
          "resource": "projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID"
        }
      }
    }
    

  1. To poll the long-running operation, call [operations.get](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.operations/get):
         
         curl -X GET https://documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION \
                -H "Authorization: Bearer "$(gcloud auth print-access-token) \
                -H "X-Goog-User-Project: PROJECT_ID"

     1. The [`DisableProcessorMetadata`](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/DisableProcessorMetadata) in the response indicates the state of the operation:
            
            {
              "name": "projects/<project_id>/locations/<location>/operations/<operation>",
              "metadata": {
                "@type": "type.googleapis.com/google.cloud.documentai.v1.DisableProcessorMetadata",
                "commonMetadata": {
                  "state": "SUCCEEDED",
                  "createTime": "2022-03-02T22:52:49.957096Z",
                  "updateTime": "2022-03-02T22:52:50.175976Z",
                  "resource": "projects/<project_id>/locations/<location>/processors/<processor_id>"
                }
              },
              "done": true,
              "response": {
                "@type": "type.googleapis.com/google.cloud.documentai.v1.DisableProcessorResponse"
              }
            }
            




### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.api_core.exceptions import FailedPrecondition
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
    # processor_id = 'YOUR_PROCESSOR_ID'
    
    
    def disable_processor_sample(project_id: str, location: str, processor_id: str) -> None:
        # You must set the api_endpoint if you use a location other than 'us'.
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # The full resource name of the processor
        # e.g.: projects/project_id/locations/location/processors/processor_id
        processor_name = client.[processor_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_path)(project_id, location, processor_id)
        request = documentai.[DisableProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.DisableProcessorRequest.html)(name=processor_name)
    
        # Make DisableProcessor request
        try:
            operation = client.[disable_processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_disable_processor)(request=request)
    
            # Print operation name
            print(operation.operation.name)
            # Wait for operation to complete
            operation.result()
        # Cannot disable a processor that is already disabled
        except FailedPrecondition as e:
            print(e.message)
    
    

### Go

For more information, see the [Document AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	documentai "cloud.google.com/go/documentai/apiv1"
    	documentaipb "cloud.google.com/go/documentai/apiv1/documentaipb"
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
    
    	req := &documentaipb.DisableProcessorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/documentai/apiv1/documentaipb#DisableProcessorRequest.
    	}
    	op, err := c.DisableProcessor(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

For more information, see the [Document AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/overview). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.documentai.v1.[DisableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorRequest.html);
    import com.google.cloud.documentai.v1.[DisableProcessorResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorResponse.html);
    import com.google.cloud.documentai.v1.[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html);
    import com.google.cloud.documentai.v1.[ProcessorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorName.html);
    
    public class SyncDisableProcessor {
    
      public static void main(String[] args) throws Exception {
        syncDisableProcessor();
      }
    
      public static void syncDisableProcessor() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html) documentProcessorServiceClient =
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html).create()) {
          [DisableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorRequest.html) request =
              [DisableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorRequest.html).newBuilder()
                  .setName([ProcessorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorName.html).of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
                  .build();
          [DisableProcessorResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorResponse.html) response =
              documentProcessorServiceClient.[disableProcessorAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html#com_google_cloud_documentai_v1_DocumentProcessorServiceClient_disableProcessorAsync_com_google_cloud_documentai_v1_DisableProcessorRequest_)(request).get();
        }
      }
    }

### Ruby

For more information, see the [Document AI Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/document_ai/v1"
    
    ##
    # Snippet for the disable_processor call in the DocumentProcessorService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client#disable_processor.
    #
    def disable_processor
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DocumentAI::V1::DisableProcessorRequest.new
    
      # Call the disable_processor method.
      result = client.disable_processor request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

### C#

For more information, see the [Document AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedDocumentProcessorServiceClientSnippets
    {
        /// <summary>Snippet for DisableProcessor</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void DisableProcessorRequestObject()
        {
            // Create client
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html) documentProcessorServiceClient = [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_Create)();
            // Initialize request argument(s)
            [DisableProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DisableProcessorRequest.html) request = new [DisableProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DisableProcessorRequest.html)
            {
                ProcessorName = [ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName.html).[FromProjectLocationProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName.html#Google_Cloud_DocumentAI_V1_ProcessorName_FromProjectLocationProcessor_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[PROCESSOR]"),
            };
            // Make the request
            Operation<DisableProcessorResponse, DisableProcessorMetadata> response = documentProcessorServiceClient.[DisableProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_DisableProcessor_Google_Cloud_DocumentAI_V1_DisableProcessorRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<DisableProcessorResponse, DisableProcessorMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [DisableProcessorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DisableProcessorResponse.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<DisableProcessorResponse, DisableProcessorMetadata> retrievedResponse = documentProcessorServiceClient.[PollOnceDisableProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_PollOnceDisableProcessor_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [DisableProcessorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DisableProcessorResponse.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

## Delete a processor

### Web UI

  1. In the Google Cloud console, in the Document AI section, go to the **Processors** page.

[Go to the Processors page](https://console.cloud.google.com/ai/document-ai/processors)

     1. Next to your processor, in the **Action menu** more_vert, click **Delete processor**.



### REST

This sample shows you how to delete an existing [`Processor`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors#Processor) using the [`processors.delete`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/delete) method.

Before using any of the request data, make the following replacements: 

  * LOCATION: your processor's [location](https://docs.cloud.google.com/document-ai/docs/regions), for example: 
    * `us` \- United States
    * `eu` \- European Union
  * PROJECT_ID: Your Google Cloud project ID.
  * PROCESSOR_ID: the ID of your custom processor.



HTTP method and URL: 
    
    
    DELETE https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://LOCATION-documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID" | Select-Object -Expand Content

The response is a [long-running operation](https://docs.cloud.google.com/document-ai/docs/long-running-operations)
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.documentai.v1.DeleteProcessorMetadata",
        "commonMetadata": {
          "state": "RUNNING",
          "createTime": "2022-03-02T22:52:49.957096Z",
          "updateTime": "2022-03-02T22:52:50.175976Z",
          "resource": "projects/PROJECT_ID/locations/LOCATION/processors/PROCESSOR_ID"
        }
      }
    }
    

  1. To poll the long-running operation, call [operations.get](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.operations/get):
         
         curl -X GET https://documentai.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION \
                -H "Authorization: Bearer "$(gcloud auth print-access-token) \
                -H "X-Goog-User-Project: PROJECT_ID"

  2. The [`DeleteProcessorMetadata`](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/DeleteProcessorMetadata) in the response indicates the state of the operation:
         
         {
             "name": "projects/<project_id>/locations/<location>/operations/<operation>",
             "metadata": {
               "@type": "type.googleapis.com/google.cloud.documentai.v1.DeleteProcessorMetadata",
               "commonMetadata": {
                 "state": "SUCCEEDED",
                 "createTime": "2022-03-02T22:52:49.957096Z",
                 "updateTime": "2022-03-02T22:52:50.175976Z",
                 "resource": "projects/<project_id>/locations/<location>/processors/<processor_id>"
               }
             },
             "done": true,
             "response": {
               "@type": "type.googleapis.com/google.protobuf.Empty"
             }
           }
         




### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.api_core.exceptions import NotFound
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
    # processor_id = 'YOUR_PROCESSOR_ID'
    
    
    def delete_processor_sample(project_id: str, location: str, processor_id: str) -> None:
        # You must set the api_endpoint if you use a location other than 'us'.
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # The full resource name of the processor
        # e.g.: projects/project_id/locations/location/processors/processor_id
        processor_name = client.[processor_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_path)(project_id, location, processor_id)
    
        # Delete a processor
        try:
            operation = client.[delete_processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_delete_processor)(name=processor_name)
            # Print operation details
            print(operation.operation.name)
            # Wait for operation to complete
            operation.result()
        except NotFound as e:
            print(e.message)
    
    

### Go

For more information, see the [Document AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/documentai/latest/apiv1). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	documentai "cloud.google.com/go/documentai/apiv1"
    	documentaipb "cloud.google.com/go/documentai/apiv1/documentaipb"
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
    
    	req := &documentaipb.DeleteProcessorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/documentai/apiv1/documentaipb#DeleteProcessorRequest.
    	}
    	op, err := c.DeleteProcessor(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### Java

For more information, see the [Document AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/overview). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.documentai.v1.[DeleteProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorRequest.html);
    import com.google.cloud.documentai.v1.[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html);
    import com.google.cloud.documentai.v1.[ProcessorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorName.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    
    public class SyncDeleteProcessor {
    
      public static void main(String[] args) throws Exception {
        syncDeleteProcessor();
      }
    
      public static void syncDeleteProcessor() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html) documentProcessorServiceClient =
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html).create()) {
          [DeleteProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorRequest.html) request =
              [DeleteProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorRequest.html).newBuilder()
                  .setName([ProcessorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorName.html).of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
                  .build();
          documentProcessorServiceClient.[deleteProcessorAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.html#com_google_cloud_documentai_v1_DocumentProcessorServiceClient_deleteProcessorAsync__org_jspecify_annotations_Nullable_com_google_cloud_documentai_v1_ProcessorName_)(request).get();
        }
      }
    }

### Ruby

For more information, see the [Document AI Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/document_ai/v1"
    
    ##
    # Snippet for the delete_processor call in the DocumentProcessorService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client#delete_processor.
    #
    def delete_processor
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DocumentAI::V1::DeleteProcessorRequest.new
    
      # Call the delete_processor method.
      result = client.delete_processor request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

### C#

For more information, see the [Document AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedDocumentProcessorServiceClientSnippets
    {
        /// <summary>Snippet for DeleteProcessor</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void DeleteProcessorRequestObject()
        {
            // Create client
            [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html) documentProcessorServiceClient = [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_Create)();
            // Initialize request argument(s)
            [DeleteProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DeleteProcessorRequest.html) request = new [DeleteProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DeleteProcessorRequest.html)
            {
                ProcessorName = [ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName.html).[FromProjectLocationProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName.html#Google_Cloud_DocumentAI_V1_ProcessorName_FromProjectLocationProcessor_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[PROCESSOR]"),
            };
            // Make the request
            Operation<Empty, DeleteProcessorMetadata> response = documentProcessorServiceClient.[DeleteProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_DeleteProcessor_Google_Cloud_DocumentAI_V1_DeleteProcessorRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<Empty, DeleteProcessorMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Empty, DeleteProcessorMetadata> retrievedResponse = documentProcessorServiceClient.[PollOnceDeleteProcessor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient.html#Google_Cloud_DocumentAI_V1_DocumentProcessorServiceClient_PollOnceDeleteProcessor_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

[ Previous arrow_back  BigQuery integration  ](https://docs.cloud.google.com/document-ai/docs/big-query-integration)

[ Next Process documents with client libraries  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/process-documents-client-libraries)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
