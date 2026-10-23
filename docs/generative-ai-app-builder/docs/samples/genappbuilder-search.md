---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-search/
title: Search a data store \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:36.199465+00:00
---

# Search a data store  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-search/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  Search a data store Stay organized with collections  Save and categorize content based on your preferences. 

Perform a search query for a data store.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Gemini Enterprise client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries)
  * [Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results)
  * [Improve search results with search tuning](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search)
  * [Vertex AI Search client libraries](https://docs.cloud.google.com/generative-ai-app-builder/docs/libraries)



## Code sample

### Java

For more information, see the [Agent Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/overview). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.discoveryengine.v1.[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.html);
    import com.google.cloud.discoveryengine.v1.[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html);
    import com.google.cloud.discoveryengine.v1.[SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.html);
    import com.google.cloud.discoveryengine.v1.[SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceSettings.html);
    import com.google.cloud.discoveryengine.v1.[ServingConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfigName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class Search {
      public static void main() throws IOException, ExecutionException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "PROJECT_ID";
        // Location of the data store. Options: "global", "us", "eu"
        String location = "global";
        // Collection containing the data store.
        String collectionId = "default_collection";
        // Data store ID.
        String dataStoreId = "DATA_STORE_ID";
        // Serving configuration. Options: "default_search"
        String servingConfigId = "default_search";
        // Search Query for the data store.
        String searchQuery = "Google";
        search(projectId, location, collectionId, dataStoreId, servingConfigId, searchQuery);
      }
    
      /** Performs a search on a given datastore. */
      public static void search(
          String projectId,
          String location,
          String collectionId,
          String dataStoreId,
          String servingConfigId,
          String searchQuery)
          throws IOException, ExecutionException {
        // For more information, refer to:
        // https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        String endpoint = (location.equals("global")) 
            ? String.format("discoveryengine.googleapis.com:443", location) 
            : String.format("%s-discoveryengine.googleapis.com:443", location);
        [SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceSettings.html) settings =
            [SearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `searchServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.html) searchServiceClient = [SearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchServiceClient.html).create(settings)) {
          [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.html) request =
              [SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.html).newBuilder()
                  .setServingConfig(
                      [ServingConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfigName.html).[formatProjectLocationCollectionDataStoreServingConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfigName.html#com_google_cloud_discoveryengine_v1_ServingConfigName_formatProjectLocationCollectionDataStoreServingConfigName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
                          projectId, location, collectionId, dataStoreId, servingConfigId))
                  .setQuery(searchQuery)
                  .setPageSize(10)
                  .build();
          [SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html) response = searchServiceClient.search(request).getPage().getResponse();
          for ([SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html).SearchResult element : response.[getResultsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchResponse.html#com_google_cloud_discoveryengine_v1_SearchResponse_getResultsList__)()) {
            System.out.println("Response content: " + element);
          }
        }
      }
    }

### Node.js

For more information, see the [Agent Search Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_LOCATION';              // Options: 'global', 'us', 'eu'
    // const collectionId = 'default_collection';     // Options: 'default_collection'
    // const dataStoreId = 'YOUR_DATA_STORE_ID'       // Create in Cloud Console
    // const servingConfigId = 'default_config';      // Options: 'default_config'
    // const searchQuery = 'Google';
    
    const {SearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
    // For more information, refer to:
    // https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    const apiEndpoint =
      location === 'global'
        ? 'discoveryengine.googleapis.com'
        : `${location}-discoveryengine.googleapis.com`;
    
    // Instantiates a client
    const client = new [SearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)({apiEndpoint: apiEndpoint});
    
    async function search() {
      // The full resource name of the search engine serving configuration.
      // Example: projects/{projectId}/locations/{location}/collections/{collectionId}/dataStores/{dataStoreId}/servingConfigs/{servingConfigId}
      // You must create a search engine in the Cloud Console first.
      const name = client.projectLocationCollectionDataStoreServingConfigPath(
        projectId,
        location,
        collectionId,
        dataStoreId,
        servingConfigId
      );
    
      const request = {
        pageSize: 10,
        query: searchQuery,
        servingConfig: name,
      };
    
      const IResponseParams = {
        ISearchResult: 0,
        ISearchRequest: 1,
        ISearchResponse: 2,
      };
    
      // Perform search request
      const response = await client.search(request, {
        // Warning: Should always disable autoPaginate to avoid iterate through all pages.
        //
        // By default NodeJS SDK returns an iterable where you can iterate through all
        // search results instead of only the limited number of results requested on
        // pageSize, by sending multiple sequential search requests page-by-page while
        // iterating, until it exhausts all the search results. This will be unexpected and
        // may cause high Search API usage and long wait time, especially when the matched
        // document numbers are huge.
        autoPaginate: false,
      });
      const results = response[IResponseParams.ISearchResponse].results;
    
      for (const result of results) {
        console.log(result);
      }
    }

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION"          # Values: "global", "us", "eu"
    # engine_id = "YOUR_APP_ID"
    # search_query = "YOUR_SEARCH_QUERY"
    
    
    def search_sample(
        project_id: str,
        location: str,
        engine_id: str,
        search_query: str,
    ) -> discoveryengine.services.search_service.pagers.SearchPager:
        #  For more information, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        client_options = (
            ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
            if location != "global"
            else None
        )
    
        # Create a client
        client = discoveryengine.SearchServiceClient(client_options=client_options)
    
        # The full resource name of the search app serving config
        serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_config"
    
        # Optional - only supported for unstructured data: Configuration options for search.
        # Refer to the `ContentSearchSpec` reference for all supported fields:
        # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec
        content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
            # For information about snippets, refer to:
            # https://cloud.google.com/generative-ai-app-builder/docs/snippets
            snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
                return_snippet=True
            ),
            # For information about search summaries, refer to:
            # https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries
            summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
                summary_result_count=5,
                include_citations=True,
                ignore_adversarial_query=True,
                ignore_non_summary_seeking_query=True,
                model_prompt_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec(
                    preamble="YOUR_CUSTOM_PROMPT"
                ),
                model_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec(
                    version="stable",
                ),
            ),
        )
    
        # Refer to the `SearchRequest` reference for all supported fields:
        # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest
        request = discoveryengine.SearchRequest(
            serving_config=serving_config,
            query=search_query,
            page_size=10,
            content_search_spec=content_search_spec,
            query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
                condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
            ),
            spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
                mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
            ),
            # Optional: Use fine-tuned model for this request
            # custom_fine_tuning_spec=discoveryengine.CustomFineTuningSpec(
            #     enable_search_adaptor=True
            # ),
        )
    
        page_result = client.search(request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
        return page_result
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
