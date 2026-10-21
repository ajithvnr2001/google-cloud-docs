---
url: https://docs.cloud.google.com/dataplex/docs/search-assets/
title: Search for data assets in Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:01.226783+00:00
---

# Search for data assets in Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataplex/docs/search-assets/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Search for data assets in Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions on how to search for data assets in Knowledge Catalog.

## Before you begin

Before you perform search, ensure that you are granted the required roles and have enabled the necessary API.

**Note:** If this is your first time using Knowledge Catalog to discover data, consider following the quickstart [Create and use a business glossary](https://docs.cloud.google.com/knowledge-catalog/docs/quickstart-business-glossary).

### Required roles

To get the permissions that you need to search for entries and access search results in Knowledge Catalog, ask your administrator to grant you the following IAM roles: 

  * Search for entries: 
    * [Dataplex Catalog Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`) on the project used for search
    * [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) on the project used for search
    * [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the project used for search
  * Search for metadata for BigQuery datasets and tables: [BigQuery Metadata Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.metadataViewer) (`roles/bigquery.metadataViewer`) on the dataset or table 
  * Search for custom entries: [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the project used for search 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Data asset-level permissions

Search results are scoped to your access level, independently of the selected project. To find a data asset in Knowledge Catalog, you must have the appropriate read permissions for that data asset in its underlying source system. 

For example, finding a BigQuery table requires the `roles/bigquery.metadataViewer` role, while finding a Cloud SQL instance requires its equivalent [Cloud SQL permissions](https://docs.cloud.google.com/sql/docs/mysql/iam-permissions). For more details, see [Search scope](https://docs.cloud.google.com/knowledge-catalog/docs/about-search#search-scope).

### Enable the API

Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

## Search for data assets

**Note:** Knowledge Catalog indexes each shard of a date-sharded table as a separate table. Search results return all individual shards (for example, `my_table20240312` and `my_table20240311`).

### Console

To search for data assets, follow these steps:

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. If you see the **Try natural language search** button prompt, click it. By default, natural language search is selected.

  3. In the **Find resources across projects with natural language** field, enter your query and then click **Enter**.

  4. To refine your search, click **Filters**.

     * Filters in multiple sections are evaluated with the `AND` logical operator.
     * Multiple filters within a single section are evaluated with the `OR` logical operator. 

The following filters are available:

     * **Scope** : search across the organization (default), the current project, or only for starred data assets. For more information, see [Search scope](https://docs.cloud.google.com/knowledge-catalog/docs/about-search#search-scope).
     * **Systems** : the Google Cloud service that the asset belongs to, such as BigQuery. The Knowledge Catalog system contains [entry groups](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entry-groups).
     * **Projects** : the projects to search in.
     * **Type** : the data asset type, such as BigQuery connection, Cloud Storage bucket, or database. Depending on the data asset type, you can also filter by subtype, such as the connection type or SQL dialect.
     * **Select locations** : the locations to search in.
     * **Select datasets** : the search results are limited to BigQuery assets that belong to the selected BigQuery datasets. In the **Type to filter** field, enter the name of the dataset.
     * **Aspect types** : the Knowledge Catalog [aspect types](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspect-types) that are associated with the data asset that you're searching for. To filter by aspect values, click **Filter on aspect type values** , and then select the values.
  5. To view more information about the searched data asset, click the data asset name in the search results to open the entry details page.




###  Google Cloud CLI 

To search for data assets, use the [`gcloud dataplex entries search` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/search):
    
    
    gcloud dataplex entries search 'foo' \
      --project=PROJECT_ID \
      --semantic-search
    

Replace `PROJECT_ID` with the ID of the Google Cloud project.

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using System;
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for SearchEntries</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void SearchEntriesRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [SearchEntriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.SearchEntriesRequest.html) request = new [SearchEntriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.SearchEntriesRequest.html)
            {
                LocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                Query = "",
                OrderBy = "",
                Scope = "",
                SemanticSearch = false,
            };
            // Make the request
            PagedEnumerable<SearchEntriesResponse, SearchEntriesResult> response = catalogServiceClient.[SearchEntries](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_SearchEntries_Google_Api_Gax_ResourceNames_LocationName_System_String_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Iterate over all response items, lazily performing RPCs as required
            foreach ([SearchEntriesResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.SearchEntriesResult.html) item in response)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
    
            // Or iterate over pages (of server-defined size), performing one RPC per page
            foreach ([SearchEntriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.SearchEntriesResponse.html) page in response.AsRawResponses())
            {
                // Do something with each page of items
                Console.WriteLine("A page of results:");
                foreach ([SearchEntriesResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.SearchEntriesResult.html) item in page)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
            }
    
            // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
            int pageSize = 10;
            Page<SearchEntriesResult> singlePage = response.ReadPage(pageSize);
            // Do something with the page of items
            Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
            foreach ([SearchEntriesResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.SearchEntriesResult.html) item in singlePage)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
            // Store the pageToken, for when the next page is required.
            string nextPageToken = singlePage.NextPageToken;
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.SearchEntriesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#SearchEntriesRequest.
    	}
    	it := c.SearchEntries(ctx, req)
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
    		_ = it.Response.(*dataplexpb.SearchEntriesResponse)
    	}
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    import com.google.cloud.dataplex.v1.[SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest.html);
    import com.google.cloud.dataplex.v1.[SearchEntriesResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesResult.html);
    
    public class SyncSearchEntries {
    
      public static void main(String[] args) throws Exception {
        syncSearchEntries();
      }
    
      public static void syncSearchEntries() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest.html) request =
              [SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest.html).newBuilder()
                  .setName([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .setQuery("query107944136")
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .setOrderBy("orderBy-1207110587")
                  .setScope("scope109264468")
                  .[setSemanticSearch](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest.Builder.html#com_google_cloud_dataplex_v1_SearchEntriesRequest_Builder_setSemanticSearch_boolean_)(true)
                  .build();
          for ([SearchEntriesResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesResult.html) element : catalogServiceClient.searchEntries(request).iterateAll()) {
            // doThingsWith(element);
          }
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The project to which the request should be attributed in the
     *  following form: `projects/{project}/locations/global`.
     */
    // const name = 'abc123'
    /**
     *  Required. The query against which entries in scope should be matched.
     *  The query syntax is defined in Search syntax for Dataplex Universal
     *  Catalog (https://cloud.google.com/dataplex/docs/search-syntax).
     */
    // const query = 'abc123'
    /**
     *  Optional. Number of results in the search page. If <=0, then defaults
     *  to 10. Max limit for page_size is 1000. Throws an invalid argument for
     *  page_size > 1000.
     */
    // const pageSize = 1234
    /**
     *  Optional. Page token received from a previous `SearchEntries` call. Provide
     *  this to retrieve the subsequent page.
     */
    // const pageToken = 'abc123'
    /**
     *  Optional. Specifies the ordering of results.
     *  Supported values are:
     *  * `relevance`
     *  * `last_modified_timestamp`
     *  * `last_modified_timestamp asc`
     */
    // const orderBy = 'abc123'
    /**
     *  Optional. The scope under which the search should be operating. It must
     *  either be `organizations/<org_id>` or `projects/<project_ref>`. If it is
     *  unspecified, it defaults to the organization where the project provided in
     *  `name` is located.
     */
    // const scope = 'abc123'
    /**
     *  Optional. Specifies whether the search should understand the meaning and
     *  intent behind the query, rather than just matching keywords.
     */
    // const semanticSearch = true
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callSearchEntries() {
      // Construct request
      const request = {
        name,
        query,
      };
    
      // Run request
      const iterable = dataplexClient.[searchEntriesAsync](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/v1.catalogserviceclient.html)(request);
      for await (const response of iterable) {
          console.log(response);
      }
    }
    
    callSearchEntries();

### PHP

### PHP

Before trying this sample, follow the PHP setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    use Google\Cloud\Dataplex\V1\Client\CatalogServiceClient;
    use Google\Cloud\Dataplex\V1\SearchEntriesRequest;
    use Google\Cloud\Dataplex\V1\SearchEntriesResult;
    
    /**
     * Searches for Entries matching the given query and scope.
     *
     * @param string $formattedName The project to which the request should be attributed in the
     *                              following form: `projects/{project}/locations/global`. Please see
     *                              {@see CatalogServiceClient::locationName()} for help formatting this field.
     * @param string $query         The query against which entries in scope should be matched.
     *                              The query syntax is defined in [Search syntax for Dataplex Universal
     *                              Catalog](https://cloud.google.com/dataplex/docs/search-syntax).
     */
    function search_entries_sample(string $formattedName, string $query): void
    {
        // Create a client.
        $catalogServiceClient = new CatalogServiceClient();
    
        // Prepare the request message.
        $request = (new SearchEntriesRequest())
            ->setName($formattedName)
            ->setQuery($query);
    
        // Call the API and handle any network failures.
        try {
            /** @var PagedListResponse $response */
            $response = $catalogServiceClient->searchEntries($request);
    
            /** @var SearchEntriesResult $element */
            foreach ($response as $element) {
                printf('Element data: %s' . PHP_EOL, $element->serializeToJsonString());
            }
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    
    /**
     * Helper to execute the sample.
     *
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function callSample(): void
    {
        $formattedName = CatalogServiceClient::locationName('[PROJECT]', '[LOCATION]');
        $query = '[QUERY]';
    
        search_entries_sample($formattedName, $query);
    }

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_search_entries():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[SearchEntriesRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.SearchEntriesRequest.html)(
            name="name_value",
            query="query_value",
        )
    
        # Make the request
        page_result = client.[search_entries](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_search_entries)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the search_entries call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#search_entries.
    #
    def search_entries
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::SearchEntriesRequest.new
    
      # Call the search_entries method.
      result = client.search_entries request
    
      # The returned object is of type Gapic::PagedEnumerable. You can iterate
      # over elements, and API calls will be issued to fetch pages as needed.
      result.each do |item|
        # Each element is of type ::Google::Cloud::Dataplex::V1::SearchEntriesResult.
        p item
      end
    end

### REST

To search for data assets, use the [`searchEntries` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries) with the `SemanticSearch` parameter set to `true`.
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:searchEntries?query=foo&semanticSearch=true
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the region where the project exists (for example, `us-central1`)



## View details of a data asset returned by search

### Console

Use Knowledge Catalog search to view the details of a data asset.

  1. Search for a data asset in Knowledge Catalog.

  2. In the search results, click the data asset for which you want to view the details.

The entry details page opens. The page includes the following sections:

     * **Entry details** : includes information such as the entry type, system, platform, fully qualified name, creation time, last modification time, description, and stewards.
     * **Overview** : an overview of the entry, if available.
     * **Aspects** : the required and optional aspects defined for the entry. For more information, see [Categories of aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#categories-aspects).



###  gcloud 

[`gcloud dataplex entries lookup` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/lookup):
    
    
    gcloud dataplex entries lookup ENTRY_ID \
      --entry-group=ENTRY_GROUP_ID \
      --location=LOCATION \
      --project=PROJECT_ID
    

Replace the following:

  * `ENTRY_ID`: the ID of the entry
  * `ENTRY_GROUP_ID`: the ID of the entry group
  * `LOCATION`: the region where the project exists
  * `PROJECT_ID`: the ID of the Google Cloud project



### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for LookupEntry</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void LookupEntryRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [LookupEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.LookupEntryRequest.html) request = new [LookupEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.LookupEntryRequest.html)
            {
                Name = "",
                View = [EntryView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.EntryView.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.EntryView.html#Google_Cloud_Dataplex_V1_EntryView_Unspecified),
                AspectTypes = { "", },
                Paths = { "", },
                EntryAsEntryName = [EntryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.EntryName.html).[FromProjectLocationEntryGroupEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.EntryName.html#Google_Cloud_Dataplex_V1_EntryName_FromProjectLocationEntryGroupEntry_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]"),
            };
            // Make the request
            [Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Entry.html) response = catalogServiceClient.[LookupEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_LookupEntry_Google_Cloud_Dataplex_V1_LookupEntryRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.LookupEntryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#LookupEntryRequest.
    	}
    	resp, err := c.LookupEntry(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html);
    import com.google.cloud.dataplex.v1.[EntryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryName.html);
    import com.google.cloud.dataplex.v1.[EntryView](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryView.html);
    import com.google.cloud.dataplex.v1.[LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryRequest.html);
    import java.util.ArrayList;
    
    public class SyncLookupEntry {
    
      public static void main(String[] args) throws Exception {
        syncLookupEntry();
      }
    
      public static void syncLookupEntry() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryRequest.html) request =
              [LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryRequest.html).newBuilder()
                  .setName("name3373707")
                  .setView([EntryView](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryView.html).forNumber(0))
                  .addAllAspectTypes(new ArrayList<String>())
                  .addAllPaths(new ArrayList<String>())
                  .setEntry(
                      [EntryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryName.html).of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString())
                  .build();
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html) response = catalogServiceClient.lookupEntry(request);
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The project to which the request should be attributed in the
     *  following form: `projects/{project}/locations/{location}`.
     */
    // const name = 'abc123'
    /**
     *  Optional. View to control which parts of an entry the service should
     *  return.
     *  **Please check the limitations on returned aspects in the Entry view
     *  documentation. Amount of returned aspects depends on the selected Entry
     *  View.**
     */
    // const view = {}
    /**
     *  Optional. Limits the aspects returned to the provided aspect types.
     *  It only works for CUSTOM view.
     */
    // const aspectTypes = ['abc','def']
    /**
     *  Optional. Limits the aspects returned to those associated with the provided
     *  paths within the Entry. It only works for CUSTOM view.
     */
    // const paths = ['abc','def']
    /**
     *  Required. The resource name of the Entry:
     *  `projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}`.
     */
    // const entry = 'abc123'
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callLookupEntry() {
      // Construct request
      const request = {
        name,
        entry,
      };
    
      // Run request
      const response = await dataplexClient.lookupEntry(request);
      console.log(response);
    }
    
    callLookupEntry();

### PHP

### PHP

Before trying this sample, follow the PHP setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Dataplex\V1\Client\CatalogServiceClient;
    use Google\Cloud\Dataplex\V1\Entry;
    use Google\Cloud\Dataplex\V1\LookupEntryRequest;
    
    /**
     * Looks up an entry by name using the permission on the source system.
     *
     * @param string $name           The project to which the request should be attributed in the
     *                               following form: `projects/{project}/locations/{location}`.
     * @param string $formattedEntry The resource name of the Entry:
     *                               `projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}`. Please see
     *                               {@see CatalogServiceClient::entryName()} for help formatting this field.
     */
    function lookup_entry_sample(string $name, string $formattedEntry): void
    {
        // Create a client.
        $catalogServiceClient = new CatalogServiceClient();
    
        // Prepare the request message.
        $request = (new LookupEntryRequest())
            ->setName($name)
            ->setEntry($formattedEntry);
    
        // Call the API and handle any network failures.
        try {
            /** @var Entry $response */
            $response = $catalogServiceClient->lookupEntry($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    
    /**
     * Helper to execute the sample.
     *
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function callSample(): void
    {
        $name = '[NAME]';
        $formattedEntry = CatalogServiceClient::entryName(
            '[PROJECT]',
            '[LOCATION]',
            '[ENTRY_GROUP]',
            '[ENTRY]'
        );
    
        lookup_entry_sample($name, $formattedEntry);
    }

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_lookup_entry():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[LookupEntryRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.LookupEntryRequest.html)(
            name="name_value",
            entry="entry_value",
        )
    
        # Make the request
        response = client.[lookup_entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_lookup_entry)(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the lookup_entry call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#lookup_entry.
    #
    def lookup_entry
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::LookupEntryRequest.new
    
      # Call the lookup_entry method.
      result = client.lookup_entry request
    
      # The returned object is of type Google::Cloud::Dataplex::V1::Entry.
      p result
    end

### REST

To view the details of a data asset, use the [`lookupEntry` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupEntry).

## Limitations

Search has the following limitations:

  * Public data assets are outside the scope of natural language search.
  * Aspects attached to entry links are outside the scope of natural language search.



## What's next

  * Understand [search syntax for Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax).
  * Learn more [about metadata in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).
  * Learn how to [enrich entries and entry links with metadata using aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata).
  * Learn how to [manage entries and ingest custom sources](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources).
  * Try [Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases).
  * Leverage answering complex natural language queries with the Knowledge Catalog [discovery agent](https://docs.cloud.google.com/knowledge-catalog/docs/use-discovery-agent).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
