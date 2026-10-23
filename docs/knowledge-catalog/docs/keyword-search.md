---
url: https://docs.cloud.google.com/knowledge-catalog/docs/keyword-search/
title: Use keyword-only search in Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:42.948748+00:00
---

# Use keyword-only search in Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/keyword-search/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Use keyword-only search in Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To query Knowledge Catalog data, use [Knowledge Catalog search](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets). Use keyword-only search for backward compatibility only.

Use keyword-only search in Knowledge Catalog to find resources using specific keywords, filters, and a defined syntax. Keyword-only search provides precise control over your search queries and lets you narrow down results based on metadata fields.

## Before you begin

Before you perform search, ensure that you are granted the required roles and have enabled the necessary API.

### Required roles

To get the permissions that you need to search for entries and access search results in Knowledge Catalog, ask your administrator to grant you the following IAM roles: 

  * Search for entries: 
    * [**Dataplex Catalog Admin** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`) on the project used for search
    * [**Dataplex Catalog Editor** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) on the project used for search
    * [**Dataplex Catalog Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the project used for search
  * Search for metadata for BigQuery datasets and tables: [**BigQuery Metadata Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.metadataViewer) (`roles/bigquery.metadataViewer`) on the dataset or table 
  * Search for custom entries: [**Dataplex Catalog Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Use keyword-only search

### Console

To search for resources using keyword search, follow these steps:

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In the **Find resources across projects** field, enter your query.

  3. To refine your search, use the **Filters** panel. The following filters are available:

     * **Systems** provide a list of available systems, such as BigQuery or Cloud SQL. The Knowledge Catalog system contains custom entries.
     * **Aspects** let you query for assets tagged using a specific template. You can use the **Customize** menu to further refine results and filter by specific aspect values.
     * **Project** lists the projects you can scope the search to.
     * **Type aliases** are data types associated with an entry type. An entry type might have the name `projects/test-project/locations/us/entryTypes/my-entry-type`, but you can search for it using its type aliases `TABLE` or `DATABASE`. You can set one or more type aliases when you [create](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#create-entry-type) or [update](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#update-entry-type) an entry type.
     * **Datasets** come from BigQuery.

You can manually add the following filters:

     * Add a project filter: in **Project** , click **Add project**. Search for a specific project, select the project, and then click **Open**.
     * Add an aspect type filter: in **Aspects** , click the **Add more aspect types** menu. Search for a specific template, select it, and then click **OK**.
  4. Optional: In addition to the assets available to you, you can search for resources that are publicly available in Google Cloud by selecting **Include public datasets**.

Use the following tips to construct a search query:

     * Enclose your search expression in quotes if it contains spaces. For example, `"search terms"`.
     * Precede a keyword with `NOT` to match the logical negation of the `keyword:term` filter. You can also use `AND` and `OR` Boolean operators to combine search expressions. The `AND`, `OR`, and `NOT` operators aren't case-sensitive.

For example, `NOT column:term` lists all columns except those that match the specified term.

  5. To view more information about the searched resource, in the search results, click the resource name. This opens the entry details page.




###  gcloud 

To search for resources, use the [`gcloud dataplex entries search` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/search).

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

To search for resources, use the [`searchEntries` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries).

## Keyword-only search syntax

For precise searches, you can construct a query using specific syntax, including qualifiers, logical operators, and aspect searches.

### Qualified predicates

You can qualify a predicate by prefixing it with a key that restricts the matching to a specific piece of metadata:

  * An equal sign (`=`) restricts the search to an exact match.
  * A colon (`:`) after the key matches the predicate to either a substring or a token within the value in the search results.



Tokenization splits the stream of text into a series of tokens, with each token usually corresponding to a single word.

The predicate keys `type`, `system`, `location`, and `orgid` support only the exact match (`=`) qualifier, not the substring qualifier (`:`). For example, `type=foo` or `orgid=number`.

Knowledge Catalog keyword search supports the following qualifiers:

Qualifier | Description  
---|---  
`name:x` | Matches `x` as a substring of the resource ID.  
`displayname:x` | Matches `x` as a substring of the resource display name.  
`column:x` | Matches `x` as a substring of the column name (or nested column name) in the schema of the resource.  
`description:x` | Matches `x` as a token in the resource description.  
`label:bar` | Matches BigQuery resources that have a label (with some value) and the label key has `bar` as a substring.  
`label=bar` | Matches BigQuery resources that have a label (with some value) and the label key equals `bar` as a string.  
`label:bar:x` | Matches `x` as a substring in the value of a label with key `bar` attached to a BigQuery resource.  
`label=foo:bar` | Matches BigQuery resources where the key equals `foo` and the key value equals `bar`.  
`label.foo=bar` | Matches BigQuery resources where the key equals `foo` and the key value equals `bar`.  
`label.foo` | Matches BigQuery resources that have a label whose key equals `foo` as a string.  
`type=TYPE` | Matches resources of a specific entry type or its type alias.  
`projectid:bar` | Matches resources within Google Cloud projects that match `bar` as a substring in the ID.  
`parent:x` | Matches `x` as a substring of the hierarchical path of a resource. The parent path is a `fully_qualified_name` of the parent resource.  
`orgid=number` | Matches resources within a Google Cloud organization with the exact ID value of `number`.  
`system=SYSTEM` | Matches resources from a specified system.  
`location=LOCATION` |  Matches resources in a specified location with an exact name. For example, `location=us-central1` matches assets hosted in Iowa. BigQuery Omni assets support this qualifier by using the [BigQuery Omni location name](https://docs.cloud.google.com/bigquery/docs/omni-introduction#locations). For example, `location=aws-us-east-1` matches BigQuery Omni assets in Northern Virginia.  
`createtime` |  Finds resources that were created within, before, or after a given date or time. For example:

  * `createtime:2019-01-01` matches resources created on 2019-01-01.
  * `createtime<2019-02` matches resources created before 2019-02-01T00:00:00.
  * `createtime>2019-02` matches resources created after 2019-02-01T00:00:00.

Timestamp format: `YYYY-MM-DDThh:mm:ss` All timestamps must be in GMT; time zones are not supported. Partial timestamps, hyphen (`-`) date separators, and slash (`/`) date separators are supported. For example:

  * `2010-10-22T05:36:24`
  * `2010-10-22T05:36`
  * `2010-10-22T05`
  * `2010-10-22`
  * `2010-10`
  * `2010`
  * `2010/10/22`

  
`updatetime` |  Finds resources that were updated within, before, or after a given date or time. For example:

  * `updatetime:2019-01-01` matches resources updated on 2019-01-01.
  * `updatetime<2019-02` matches resources updated before 2019-02-01T00:00:00.
  * `updatetime>2019-02` matches resources updated after 2019-02-01T00:00:00.

Timestamp format: `YYYY-MM-DDThh:mm:ss` All timestamps must be in GMT; time zones are not supported. Partial timestamps, hyphen (`-`) date separators, and slash (`/`) date separators are supported. For example:

  * `2010-10-22T05:36:24`
  * `2010-10-22T05:36`
  * `2010-10-22T05`
  * `2010-10-22`
  * `2010-10`
  * `2010`
  * `2010/10/22`

  
`fully_qualified_name:x` | Matches `x` as a substring of `fully_qualified_name`.  
`fully_qualified_name=x` | Matches `x` as `fully_qualified_name`.  
  
### Aspect search

To search for entries based on their attached aspects, use the following query syntax.

**Note:** The substring match tries to match against a limited number of aspects. If you can't find the entry by using a fragment of the path, then use the full path to narrow the search and increase recall.Qualifier | Description  
---|---  
`aspect:x` | Matches `x` as a substring of the full path to the aspect type of an aspect that is attached to the entry, in the format `projectid.location.ASPECT_TYPE_ID`  
`aspect=x` | Matches `x` as the full path to the aspect type of an aspect that is attached to the entry, in the format `projectid.location.ASPECT_TYPE_ID`  
`aspect:xOPERATORvalue` |  Searches for aspect field values. Matches `x` as a substring of the full path to the aspect type and field name of an aspect that is attached to the entry, in the format `projectid.location.ASPECT_TYPE_ID.FIELD_NAME` The list of supported operators depends on the type of field in the aspect, as follows:

  * **String** : `=` (exact match) and `:` (substring)
  * **All number types** : `=`, `:`, `<`, `>`, `<=`, `>=`, `=>`, `=<`
  * **Enum** : `=`
  * **Datetime** : same as for numbers, but the values to compare are treated as datetimes instead of numbers
  * **Boolean** : `=`

Only top-level fields of the aspect are searchable. For example, all of the following queries match entries where the value of the `is-enrolled` field in the `employee-info` aspect is `true`. Other entries that match on the substring are also returned.

  * `aspect:example-project.us-central1.employee-info.is-enrolled=true`
  * `aspect:example-project.us-central1.employee=true`
  * `aspect:employee=true`

  
  
## Logical operators

A query can consist of several predicates linked with logical operators `AND`, `OR`, or `NOT`.

  * If you don't specify an operator, logical `AND` is implied. For example, `foo bar` returns resources that match both predicate `foo` and predicate `bar`.
  * Negate a predicate with a `-` (hyphen) or `NOT` prefix. For example, `-name:foo` returns resources with names that don't match the predicate `foo`.



In keyword-only search, logical operators aren't case-sensitive.

### Abbreviated syntax

To use abbreviated syntax in your queries, use `|` (vertical bar) for `OR` operators and `,` (comma) for `AND` operators. The abbreviated syntax works for the qualified predicates except for `label`.

The following examples show how to use abbreviated syntax with keyword-only search.

  * Search for entries inside one of many projects using the `OR` operator:
        
        projectid:(id1|id2|id3|id4)
        

The same search without using abbreviated syntax looks as follows:
        
        projectid:id1 OR projectid:id2 OR projectid:id3 OR projectid:id4
        

  * Search for entries with matching column names:

    * **AND** : `column:(name1,name2,name3)`
    * **OR** : `column:(name1|name2|name3)`



## What's next

  * Learn more [about metadata management in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).
  * Learn how to [enrich entries and entry links with metadata by using aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata).
  * Learn how to [manage entries and ingest custom sources](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
