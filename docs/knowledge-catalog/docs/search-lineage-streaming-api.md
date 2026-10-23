---
url: https://docs.cloud.google.com/knowledge-catalog/docs/search-lineage-streaming-api/
title: Search multi-region lineage using server-side automation \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:59.429034+00:00
---

# Search multi-region lineage using server-side automation  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/search-lineage-streaming-api/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Search multi-region lineage using server-side automation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to look up multi-level, cross-regional data lineage by using the `searchLineageStreaming` API.

The [`searchLineageStreaming`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLineageStreaming) API performs a breadth-first search in a specified direction (upstream or downstream) starting from a defined set of root entities, and returns a unified lineage graph as a real-time streaming response.

Unlike standard lineage lookup APIs that might time out on massive multi-project graphs, `searchLineageStreaming` delivers real-time, chunked responses. Use this API when building tools that need to traverse broad, deep, or cross-regional data architectures without request timeouts.

For more information, see [About multi-region lineage search](https://docs.cloud.google.com/knowledge-catalog/docs/multi-region-lineage-overview).

## Key capabilities

The `searchLineageStreaming` API includes the following capabilities:

  * **Breadth-first search** : Traverses the lineage graph layer by layer, accurately calculating the depth of each connected asset.

  * **Streaming response** : Returns subgraphs and lineage links as they are discovered by the backend system. This is highly efficient for broad or deep lineage graphs and prevents request timeouts.

  * **Multi-location and multi-project traversal** : Although you specify only one billing project in the request path, the API automatically discovers and traverses lineage links across multiple Google Cloud projects and geographical locations, provided you have the required permissions.

  * **Fine-grained column-level lineage** : Supports searching for column-level dependencies between assets.

  * **Wildcard lookups** : Lets you to retrieve all column-level lineage for a specific entity by suffixing the fully qualified name (FQN) with `*`.

  * **Pipeline insights** : Optionally retrieves metadata about the transformation pipelines (processes) that created the lineage links.




## Before you begin

Before you make requests to the API, ensure that you have met the following security and environmental prerequisites:

### Required roles

To get the permissions that you need to search for data lineage links, ask your administrator to grant you the [Data Lineage Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`) IAM role on the projects where the lineage links and processes are stored. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to search for data lineage links. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to search for data lineage links:

  * Search entity-level lineage: `datalineage.events.get` on the project where the link is stored 
  * Search column-level lineage: `datalineage.events.getFields` on the project where the link is stored 
  * Retrieve full pipeline process details: `datalineage.processes.get` on the project where the process is stored 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Resource scoping

When you configure your API request, you must distinguish between the resource used for administrative billing and the actual locations scanned by the API:

  * Billing parent path: The `parent` path in the URL request must use the format `projects/project/locations/location`. This specific project-location pair is used exclusively to evaluate billing quotas and API rate limits.

  * Target locations: Explicitly define the regions you want the backend to scan in the `locations` array inside the request body.




### Authentication setup

Initialize an environment variable with a Google Cloud access token to authenticate your `curl` commands:
    
    
    export ACCESS_TOKEN=$(gcloud auth print-access-token)
    

## Usage examples

The following examples use the endpoint `datalineage.googleapis.com`.

**Note:** In all requests, the `parent` defined in the URL path must exactly match the parent property provided inside the JSON request body payload.

### Search multi-level, multi-project lineage

To execute a deep lineage search that traverses across multiple depths of the graph and scans across distinct Google Cloud projects, define the following variables:

  * Set `limits.maxDepth` to your target traversal depth (accepts values from `1` to `100`).

  * Populate the `locations` array with the target regions you want the backend to cross-reference (for example, `["us", "us-east1"]`).




### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Data Lineage quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart). For more information, see the [Data Lineage C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest). 

To authenticate to Data Lineage, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.Grpc](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.DataCatalog.Lineage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.html);
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedLineageClientSnippets
    {
        /// <summary>Snippet for SearchLineageStreaming</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task SearchLineageStreamingRequestObject()
        {
            // Create client
            [LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient.html) lineageClient = [LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient.html#Google_Cloud_DataCatalog_Lineage_V1_LineageClient_Create)();
            // Initialize request argument(s)
            [SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.html) request = new [SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                Locations = { "", },
                RootCriteria = new SearchLineageStreamingRequest.Types.RootCriteria(),
                Direction = [SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.html).[SearchDirection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.SearchDirection.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.SearchDirection.html#Google_Cloud_DataCatalog_Lineage_V1_SearchLineageStreamingRequest_Types_SearchDirection_Unspecified),
                Filters = new SearchLineageStreamingRequest.Types.SearchFilters(),
                Limits = new SearchLineageStreamingRequest.Types.SearchLimits(),
            };
            // Make the request, returning a streaming response
            using LineageClient.SearchLineageStreamingStream response = lineageClient.[SearchLineageStreaming](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient.html#Google_Cloud_DataCatalog_Lineage_V1_LineageClient_SearchLineageStreaming_Google_Cloud_DataCatalog_Lineage_V1_SearchLineageStreamingRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Read streaming responses from server until complete
            // Note that C# 8 code can use await foreach
            AsyncResponseStream<SearchLineageStreamingResponse> responseStream = response.GetResponseStream();
            while (await responseStream.MoveNextAsync())
            {
                [SearchLineageStreamingResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingResponse.html) responseItem = responseStream.Current;
                // Do something with streamed response
            }
            // The response stream has completed
        }
    }

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Data Lineage quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart). For more information, see the [Data Lineage Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/overview). 

To authenticate to Data Lineage, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ServerStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStream.html);
    import com.google.cloud.datacatalog.lineage.v1.[LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html);
    import com.google.cloud.datacatalog.lineage.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LocationName.html);
    import com.google.cloud.datacatalog.lineage.v1.[SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html);
    import com.google.cloud.datacatalog.lineage.v1.[SearchLineageStreamingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingResponse.html);
    import java.util.ArrayList;
    
    public class AsyncSearchLineageStreaming {
    
      public static void main(String[] args) throws Exception {
        asyncSearchLineageStreaming();
      }
    
      public static void asyncSearchLineageStreaming() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html) lineageClient = [LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html).create()) {
          [SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html) request =
              [SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .[addAllLocations](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.Builder.html#com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_Builder_addAllLocations_java_lang_Iterable_java_lang_String__)(new ArrayList<String>())
                  .[setRootCriteria](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.Builder.html#com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_Builder_setRootCriteria_com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_RootCriteria_)([SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html).RootCriteria.newBuilder().build())
                  .[setFilters](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.Builder.html#com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_Builder_setFilters_com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_SearchFilters_)([SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html).SearchFilters.newBuilder().build())
                  .[setLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.Builder.html#com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_Builder_setLimits_com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_SearchLimits_)([SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html).SearchLimits.newBuilder().build())
                  .build();
          ServerStream<SearchLineageStreamingResponse> stream =
              lineageClient.[searchLineageStreamingCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html#com_google_cloud_datacatalog_lineage_v1_LineageClient_searchLineageStreamingCallable__)().call(request);
          for ([SearchLineageStreamingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingResponse.html) response : stream) {
            // Do something when a response is received.
          }
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Data Lineage quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart). For more information, see the [Data Lineage Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest). 

To authenticate to Data Lineage, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The project and location to initiate the search from.
     */
    // const parent = 'abc123'
    /**
     *  Required. The locations to search in.
     */
    // const locations = ['abc','def']
    /**
     *  Required. Criteria for the root of the search.
     */
    // const rootCriteria = {}
    /**
     *  Required. Direction of the search.
     */
    // const direction = {}
    /**
     *  Optional. Filters for the search.
     */
    // const filters = {}
    /**
     *  Optional. Limits for the search.
     */
    // const limits = {}
    
    // Imports the Lineage library
    const {LineageClient} = require('[@google-cloud/lineage](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/overview.html)').v1;
    
    // Instantiates a client
    const lineageClient = new [LineageClient](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/overview.html)();
    
    async function callSearchLineageStreaming() {
      // Construct request
      const request = {
        parent,
        locations,
        rootCriteria,
        direction,
      };
    
      // Run request
      const stream = await lineageClient.searchLineageStreaming(request);
      stream.on('data', (response) => { console.log(response) });
      stream.on('error', (err) => { throw(err) });
      stream.on('end', () => { /* API call completed */ });
    }
    
    callSearchLineageStreaming();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Data Lineage quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart). For more information, see the [Data Lineage Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/lineage/latest). 

To authenticate to Data Lineage, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    
    def sample_search_lineage_streaming():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[SearchLineageStreamingRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingRequest.html)(
            parent="parent_value",
            locations=["locations_value1", "locations_value2"],
            direction="UPSTREAM",
        )
    
        # Make the request
        stream = client.[search_lineage_streaming](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_search_lineage_streaming)(request=request)
    
        # Handle the response
        for response in stream:
            print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Data Lineage quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart). For more information, see the [Data Lineage Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage/latest). 

To authenticate to Data Lineage, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/data_catalog/lineage/v1"
    
    ##
    # Snippet for the search_lineage_streaming call in the Lineage service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DataCatalog::Lineage::V1::Lineage::Client#search_lineage_streaming.
    #
    def search_lineage_streaming
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DataCatalog::Lineage::V1::Lineage::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DataCatalog::Lineage::V1::SearchLineageStreamingRequest.new
    
      # Call the search_lineage_streaming method to start streaming.
      output = client.search_lineage_streaming request
    
      # The returned object is a streamed enumerable yielding elements of type
      # ::Google::Cloud::DataCatalog::Lineage::V1::SearchLineageStreamingResponse
      output.each do |current_response|
        p current_response
      end
    end

### REST

To search for data lineage, use the [`searchLineageStreaming` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLineageStreaming).

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID used for administrative billing and quota evaluation.
  * `LOCATION_ID`: the Google Cloud location, such as `us-central1`.
  * `SOURCE_PROJECT_ID`: the Google Cloud project ID where the source table is located.
  * `DATASET_ID`: the BigQuery dataset ID.
  * `TABLE_ID`: the BigQuery table ID.



HTTP method and URL: 
    
    
    POST https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID:searchLineageStreaming

Request JSON body: 
    
    
    {
      "parent": "projects/PROJECT_ID/locations/LOCATION_ID",
      "locations": [
        "LOCATION_ID",
        "us-east1",
        "us-central1"
      ],
      "rootCriteria": {
        "entities": {
          "entities": [
            {
              "fullyQualifiedName": "bigquery:SOURCE_PROJECT_ID.DATASET_ID.TABLE_ID"
            }
          ]
        }
      },
      "direction": "DOWNSTREAM",
      "limits": {
        "maxDepth": 10,
        "maxResults": 5000
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID:searchLineageStreaming"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID:searchLineageStreaming" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "links": [
        {
          "source": {
            "fullyQualifiedName": "bigquery:project-prod.dataset.source_table"
          },
          "target": {
            "fullyQualifiedName": "bigquery:project-prod.dataset.target_table"
          },
          "depth": 1,
          "location": "us"
        }
      ]
    }
    

### Search multiple geographical locations

You can limit or expand your lineage graph scan by modifying the geographical regions passed inside the `locations` repeated array field.

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Data Lineage quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart). For more information, see the [Data Lineage C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest). 

To authenticate to Data Lineage, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.Grpc](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.DataCatalog.Lineage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.html);
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedLineageClientSnippets
    {
        /// <summary>Snippet for SearchLineageStreaming</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task SearchLineageStreamingRequestObject()
        {
            // Create client
            [LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient.html) lineageClient = [LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient.html#Google_Cloud_DataCatalog_Lineage_V1_LineageClient_Create)();
            // Initialize request argument(s)
            [SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.html) request = new [SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                Locations = { "", },
                RootCriteria = new SearchLineageStreamingRequest.Types.RootCriteria(),
                Direction = [SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.html).[SearchDirection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.SearchDirection.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.SearchDirection.html#Google_Cloud_DataCatalog_Lineage_V1_SearchLineageStreamingRequest_Types_SearchDirection_Unspecified),
                Filters = new SearchLineageStreamingRequest.Types.SearchFilters(),
                Limits = new SearchLineageStreamingRequest.Types.SearchLimits(),
            };
            // Make the request, returning a streaming response
            using LineageClient.SearchLineageStreamingStream response = lineageClient.[SearchLineageStreaming](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient.html#Google_Cloud_DataCatalog_Lineage_V1_LineageClient_SearchLineageStreaming_Google_Cloud_DataCatalog_Lineage_V1_SearchLineageStreamingRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Read streaming responses from server until complete
            // Note that C# 8 code can use await foreach
            AsyncResponseStream<SearchLineageStreamingResponse> responseStream = response.GetResponseStream();
            while (await responseStream.MoveNextAsync())
            {
                [SearchLineageStreamingResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingResponse.html) responseItem = responseStream.Current;
                // Do something with streamed response
            }
            // The response stream has completed
        }
    }

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Data Lineage quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart). For more information, see the [Data Lineage Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/overview). 

To authenticate to Data Lineage, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ServerStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStream.html);
    import com.google.cloud.datacatalog.lineage.v1.[LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html);
    import com.google.cloud.datacatalog.lineage.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LocationName.html);
    import com.google.cloud.datacatalog.lineage.v1.[SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html);
    import com.google.cloud.datacatalog.lineage.v1.[SearchLineageStreamingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingResponse.html);
    import java.util.ArrayList;
    
    public class AsyncSearchLineageStreaming {
    
      public static void main(String[] args) throws Exception {
        asyncSearchLineageStreaming();
      }
    
      public static void asyncSearchLineageStreaming() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html) lineageClient = [LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html).create()) {
          [SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html) request =
              [SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .[addAllLocations](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.Builder.html#com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_Builder_addAllLocations_java_lang_Iterable_java_lang_String__)(new ArrayList<String>())
                  .[setRootCriteria](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.Builder.html#com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_Builder_setRootCriteria_com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_RootCriteria_)([SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html).RootCriteria.newBuilder().build())
                  .[setFilters](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.Builder.html#com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_Builder_setFilters_com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_SearchFilters_)([SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html).SearchFilters.newBuilder().build())
                  .[setLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.Builder.html#com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_Builder_setLimits_com_google_cloud_datacatalog_lineage_v1_SearchLineageStreamingRequest_SearchLimits_)([SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.html).SearchLimits.newBuilder().build())
                  .build();
          ServerStream<SearchLineageStreamingResponse> stream =
              lineageClient.[searchLineageStreamingCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html#com_google_cloud_datacatalog_lineage_v1_LineageClient_searchLineageStreamingCallable__)().call(request);
          for ([SearchLineageStreamingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingResponse.html) response : stream) {
            // Do something when a response is received.
          }
        }
      }
    }

### Node.js

### Java

Before trying this sample, follow the Java setup instructions in the [Data Lineage quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart). 

To authenticate to Data Lineage, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The project and location to initiate the search from.
     */
    // const parent = 'abc123'
    /**
     *  Required. The locations to search in.
     */
    // const locations = ['abc','def']
    /**
     *  Required. Criteria for the root of the search.
     */
    // const rootCriteria = {}
    /**
     *  Required. Direction of the search.
     */
    // const direction = {}
    /**
     *  Optional. Filters for the search.
     */
    // const filters = {}
    /**
     *  Optional. Limits for the search.
     */
    // const limits = {}
    
    // Imports the Lineage library
    const {LineageClient} = require('[@google-cloud/lineage](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/overview.html)').v1;
    
    // Instantiates a client
    const lineageClient = new [LineageClient](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/overview.html)();
    
    async function callSearchLineageStreaming() {
      // Construct request
      const request = {
        parent,
        locations,
        rootCriteria,
        direction,
      };
    
      // Run request
      const stream = await lineageClient.searchLineageStreaming(request);
      stream.on('data', (response) => { console.log(response) });
      stream.on('error', (err) => { throw(err) });
      stream.on('end', () => { /* API call completed */ });
    }
    
    callSearchLineageStreaming();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Data Lineage quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart). For more information, see the [Data Lineage Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/lineage/latest). 

To authenticate to Data Lineage, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    
    def sample_search_lineage_streaming():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[SearchLineageStreamingRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingRequest.html)(
            parent="parent_value",
            locations=["locations_value1", "locations_value2"],
            direction="UPSTREAM",
        )
    
        # Make the request
        stream = client.[search_lineage_streaming](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_search_lineage_streaming)(request=request)
    
        # Handle the response
        for response in stream:
            print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Data Lineage quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart). For more information, see the [Data Lineage Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage/latest). 

To authenticate to Data Lineage, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/data_catalog/lineage/v1"
    
    ##
    # Snippet for the search_lineage_streaming call in the Lineage service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DataCatalog::Lineage::V1::Lineage::Client#search_lineage_streaming.
    #
    def search_lineage_streaming
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DataCatalog::Lineage::V1::Lineage::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DataCatalog::Lineage::V1::SearchLineageStreamingRequest.new
    
      # Call the search_lineage_streaming method to start streaming.
      output = client.search_lineage_streaming request
    
      # The returned object is a streamed enumerable yielding elements of type
      # ::Google::Cloud::DataCatalog::Lineage::V1::SearchLineageStreamingResponse
      output.each do |current_response|
        p current_response
      end
    end

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID used for administrative billing and quota evaluation.
  * `LOCATION_ID`: the Google Cloud location, such as `us-central1`.
  * `SOURCE_PROJECT_ID`: the Google Cloud project ID where the source table is located.
  * `DATASET_ID`: the BigQuery dataset ID.
  * `TABLE_ID`: the BigQuery table ID.



HTTP method and URL: 
    
    
    POST https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID:searchLineageStreaming

Request JSON body: 
    
    
    {
      "parent": "projects/PROJECT_ID/locations/LOCATION_ID",
      "locations": [
        "LOCATION_ID",
        "us-east1",
        "us-central1"
      ],
      "rootCriteria": {
        "entities": {
          "entities": [
            {
              "fullyQualifiedName": "bigquery:SOURCE_PROJECT_ID.DATASET_ID.TABLE_ID"
            }
          ]
        }
      },
      "direction": "DOWNSTREAM",
      "limits": {
        "maxDepth": 10,
        "maxResults": 5000
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID:searchLineageStreaming"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID:searchLineageStreaming" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "links": [
        {
          "source": {
            "fullyQualifiedName": "bigquery:project-prod.dataset.source_table"
          },
          "target": {
            "fullyQualifiedName": "bigquery:project-prod.dataset.target_table"
          },
          "depth": 1,
          "location": "us"
        }
      ]
    }
    

### Retrieve process names for lineage links

By default, the API leaves process information omitted (`maxProcessPerLink` defaults to `0`). To retrieve the resource names of the pipelines that created your data links, configure `limits.maxProcessPerLink` to a non-zero positive integer.

For example:

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Data Lineage quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart). For more information, see the [Data Lineage Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/overview). 

To authenticate to Data Lineage, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.datacatalog.lineage.v1.[LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html);
    import com.google.cloud.datacatalog.lineage.v1.[Process](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Process.html);
    import com.google.cloud.datacatalog.lineage.v1.[ProcessName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ProcessName.html);
    
    public class SyncGetProcessProcessname {
    
      public static void main(String[] args) throws Exception {
        syncGetProcessProcessname();
      }
    
      public static void syncGetProcessProcessname() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html) lineageClient = [LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html).create()) {
          [ProcessName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ProcessName.html) name = [ProcessName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ProcessName.html).of("[PROJECT]", "[LOCATION]", "[PROCESS]");
          [Process](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Process.html) response = lineageClient.getProcess(name);
        }
      }
    }

### REST

Before using any of the request data, make the following replacements: 

  * `BILLING_PROJECT_ID`: the Google Cloud project used for administrative billing and quota evaluation. Provide a project number or project ID.
  * `LOCATION_ID`: the Google Cloud location where the lineage search is performed.
  * `FULLY_QUALIFIED_NAME`: the fully qualified name (FQN) of the target entity, in the format `bigquery:PROJECT_ID.DATASET_ID.TABLE_ID`.



HTTP method and URL: 
    
    
    POST https://datalineage.googleapis.com/v1/projects/BILLING_PROJECT_ID/locations/LOCATION_ID:searchLineageStreaming

Request JSON body: 
    
    
    {
      "parent": "projects/BILLING_PROJECT_ID/locations/LOCATION_ID",
      "locations": [
        "LOCATION_ID"
      ],
      "rootCriteria": {
        "entities": {
          "entities": [
            {
              "fullyQualifiedName": "FULLY_QUALIFIED_NAME"
            }
          ]
        }
      },
      "direction": "UPSTREAM",
      "limits": {
        "maxProcessPerLink": 5
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datalineage.googleapis.com/v1/projects/BILLING_PROJECT_ID/locations/LOCATION_ID:searchLineageStreaming"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://datalineage.googleapis.com/v1/projects/BILLING_PROJECT_ID/locations/LOCATION_ID:searchLineageStreaming" | Select-Object -Expand Content

Response behavior: The resulting stream populates the `links[].processes` field with process messages containing only their absolute system resource name (such as `projects/my-project/locations/us/processes/my-process`).

### Retrieve full process details using a FieldMask

If you need full structural metadata about a pipeline (such as its `displayName`, system `attributes`, or execution `origin`) instead of just its resource name, you must use an API `FieldMask`:

  1. Provide a non-zero value to `limits.maxProcessPerLink`.

  2. Append a `fields` query parameter to the URL path, specifying `links.processes.process` along with other required fields.




For example:
    
    
    curl -H "Authorization: Bearer ${ACCESS_TOKEN}" \
    -H "Content-Type: application/json" \
    -X POST "https://datalineage.googleapis.com/v1/projects/my-billing-project/locations/us:searchLineageStreaming?fields=links.processes.process,links.source,links.target,links.depth" \
    --data '{
      "parent": "projects/my-billing-project/locations/us",
      "locations": ["us"],
      "rootCriteria": {
        "entities": {
          "entities": [{
            "fullyQualifiedName": "bigquery:my-project.dataset.target_table"
          }]
        }
      },
      "direction": "UPSTREAM",
      "limits": {
        "maxProcessPerLink": 5
      }
    }'
    

### Search both table-level and column-level lineage

You can search for both table-level (asset-level) and column-level (field-level) lineage in a single request by providing multiple entities in the `rootCriteria.entities.entities` list:

  * For table-level lineage, omit the `field` array.

  * For column-level lineage, specify a single column in the `field` array.




For example:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -X POST https://datalineage.googleapis.com/v1/projects/my-billing-project/locations/us:searchLineageStreaming \
         --data '{
           "parent": "projects/my-billing-project/locations/us",
           "locations": ["us"],
           "rootCriteria": {
             "entities": {
               "entities": [
                 {
                   "fullyQualifiedName": "bigquery:my-project.dataset.table_a"
                 },
                 {
                   "fullyQualifiedName": "bigquery:my-project.dataset.table_b",
                   "field": ["email"]
                 }
               ]
             }
           },
           "direction": "DOWNSTREAM"
         }'
    

### Use wildcards for column-level lineage

To search for all available column-level lineage for a specific table without listing every column individually, use the wildcard character `*` as the single value in the `field` array.

For example:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -X POST https://datalineage.googleapis.com/v1/projects/my-billing-project/locations/us:searchLineageStreaming \
         --data '{
           "parent": "projects/my-billing-project/locations/us",
           "locations": ["us"],
           "rootCriteria": {
             "entities": {
               "entities": [{
                 "fullyQualifiedName": "bigquery:my-project.dataset.my_table",
                 "field": ["*"]
               }]
             }
           },
           "direction": "DOWNSTREAM"
         }'
    

## Filter lineage results

You can refine your lineage search results by using the `filters` block in the request body.

### Filter by dependency type

To restrict results to specific dependency types, such as direct copies (`EXACT_COPY`) or transformations like filtering and grouping (`OTHER`), use the `dependencyTypes` filter.

For example:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -X POST https://datalineage.googleapis.com/v1/projects/my-billing-project/locations/us:searchLineageStreaming \
         --data '{
           "parent": "projects/my-billing-project/locations/us",
           "locations": ["us"],
           "rootCriteria": {
             "entities": {
               "entities": [{
                 "fullyQualifiedName": "bigquery:my-project.dataset.my_table"
               }]
             }
           },
           "direction": "DOWNSTREAM",
           "filters": {
             "dependencyTypes": ["EXACT_COPY"]
           }
         }'
    

### Exclude column-level lineage (Table-only search)

To ensure that the search returns only table-level lineage and completely excludes column-level lineage, set the `entitySet` filter to `ENTITIES`.

For example:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -X POST https://datalineage.googleapis.com/v1/projects/my-billing-project/locations/us:searchLineageStreaming \
         --data '{
           "parent": "projects/my-billing-project/locations/us",
           "locations": ["us"],
           "rootCriteria": {
             "entities": {
               "entities": [{
                 "fullyQualifiedName": "bigquery:my-project.dataset.my_table"
               }]
             }
           },
           "direction": "DOWNSTREAM",
           "filters": {
             "entitySet": "ENTITIES"
           }
         }'
    

### Filter by time range

You can restrict the lineage search results to a specific time interval.

**Note:** You can set at most one of either `startTime` or `endTime` inside the `timeRange` interval object.

For example, to search for lineage data created after a specific timestamp, use the following request:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -X POST https://datalineage.googleapis.com/v1/projects/my-billing-project/locations/us:searchLineageStreaming \
         --data '{
           "parent": "projects/my-billing-project/locations/us",
           "locations": ["us"],
           "rootCriteria": {
             "entities": {
               "entities": [{
                 "fullyQualifiedName": "bigquery:my-project.dataset.my_table"
               }]
             }
           },
           "direction": "DOWNSTREAM",
           "filters": {
             "timeRange": {
               "startTime": "2026-01-01T00:00:00Z"
             }
           }
         }'
    

## Troubleshooting: Handle unreachable locations and partial graphs

Because the streaming API scans across a distributed set of projects and locations simultaneously, some remote regions might be temporarily down, uncommunicative, or misconfigured during execution.

  * **Symptom** : The returned lineage graph layout appears incomplete or is missing expected regional hops.

  * **Diagnostic** : To protect data integrity, the `searchLineageStreamingResponse` stream populates a dedicated `unreachable` field (repeated string) with problematic locations, using the format `projects/PROJECT_NUMBER/locations/LOCATION` (for example, `projects/123456789/locations/us-east1`).

  * **Best practice** : Always build your client applications to inspect the `unreachable` field to verify data completeness before processing the graph.




## What's next

  * Learn more [about multi-region lineage search](https://docs.cloud.google.com/knowledge-catalog/docs/multi-region-lineage-overview).

  * Learn more [about data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage).

  * Learn more about [lineage visualization](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
