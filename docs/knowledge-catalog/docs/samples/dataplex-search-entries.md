---
url: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-search-entries/
title: Search entries \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:25.282496+00:00
---

# Search entries  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-search-entries/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/knowledge-catalog/docs/samples)



#  Search entries Stay organized with collections  Save and categorize content based on your preferences. 

Use search to retrieve entries matching the query. 

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html);
    import com.google.cloud.dataplex.v1.[SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest.html);
    import com.google.cloud.dataplex.v1.[SearchEntriesResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesResult.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.stream.Collectors;
    
    public class SearchEntries {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        // How to write query for search: https://cloud.google.com/dataplex/docs/search-syntax
        String query = "MY_QUERY";
    
        List<Entry> entries = searchEntries(projectId, query);
        entries.forEach(entry -> System.out.println("Entry name found in search: " + entry.getName()));
      }
    
      // Method to search Entries located in projectId and matching query
      public static List<Entry> searchEntries(String projectId, String query) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) client = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest.html) searchEntriesRequest =
              [SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest.html).newBuilder()
                  .setPageSize(100)
                  // Required field, will by default limit search scope to organization under which the
                  // project is located
                  .setName(String.format("projects/%s/locations/global", projectId))
                  // Optional field, will further limit search scope only to specified project
                  .setScope(String.format("projects/%s", projectId))
                  .setQuery(query)
                  .build();
    
          [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).[SearchEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.SearchEntriesPagedResponse.html) searchEntriesResponse =
              client.searchEntries(searchEntriesRequest);
          return searchEntriesResponse.getPage().getResponse().getResultsList().stream()
              // Extract Entries nested inside search results
              .map(SearchEntriesResult::getDataplexEntry)
              .collect(Collectors.toList());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    from google.cloud.dataplex_v1 import [Entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entry.html)
    
    
    def search_entries(project_id: str, query: str) -> List[Entry]:
        """Method to search Entries located in project_id and matching query"""
    
        # Initialize client that will be used to send requests across threads. This
        # client only needs to be created once, and can be reused for multiple requests.
        # After completing all of your requests, call the "__exit__()" method to safely
        # clean up any remaining background resources. Alternatively, use the client as
        # a context manager.
        with [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)() as client:
            search_entries_request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[SearchEntriesRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.SearchEntriesRequest.html)(
                page_size=100,
                # Required field, will by default limit search scope to organization under which the project is located
                name=f"projects/{project_id}/locations/global",
                # Optional field, will further limit search scope only to specified project
                scope=f"projects/{project_id}",
                query=query,
            )
    
            search_entries_response = client.search_entries(search_entries_request)
            return [
                result.dataplex_entry
                for result in search_entries_response._response.results
            ]
    
    
    if __name__ == "__main__":
        # TODO(developer): Replace these variables before running the sample.
        project_id = "MY_PROJECT_ID"
        # How to write query for search: https://cloud.google.com/dataplex/docs/search-syntax
        query = "MY_QUERY"
    
        entries = search_entries(project_id, query)
        for entry in entries:
            print(f"Entry name found in search: {entry.name}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataplex). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
