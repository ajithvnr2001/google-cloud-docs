---
url: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-search-assets/
title: Search data assets \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:33.380669+00:00
---

# Search data assets  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-search-assets/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/data-catalog/docs/samples)



#  Search data assets Stay organized with collections  Save and categorize content based on your preferences. 

Perform a search of data assets, such as datasets, tables, views, and Cloud Pub/Sub topics in Google Cloud Platform projects.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Search data assets with Data Catalog](https://docs.cloud.google.com/data-catalog/docs/how-to/search)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/overview). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.datacatalog.v1.[DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html);
    import com.google.cloud.datacatalog.v1.[DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html).[SearchCatalogPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.SearchCatalogPagedResponse.html);
    import com.google.cloud.datacatalog.v1.[SearchCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogRequest.html);
    import com.google.cloud.datacatalog.v1.[SearchCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogRequest.html).[Scope](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogRequest.Scope.html);
    import com.google.cloud.datacatalog.v1.[SearchCatalogResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogResult.html);
    import java.io.IOException;
    
    // Sample to search catalog
    public class SearchAssets {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String query = "type=dataset";
        searchCatalog(projectId, query);
      }
    
      public static void searchCatalog(String projectId, String query) throws IOException {
        // Create a scope object setting search boundaries to the given organization.
        // Scope scope = Scope.newBuilder().addIncludeOrgIds(orgId).build();
    
        // Alternatively, search using project scopes.
        [Scope](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogRequest.Scope.html) scope = [Scope](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogRequest.Scope.html).newBuilder().[addIncludeProjectIds](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogRequest.Scope.Builder.html#com_google_cloud_datacatalog_v1_SearchCatalogRequest_Scope_Builder_addIncludeProjectIds_java_lang_String_)(projectId).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html) dataCatalogClient = [DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html).create()) {
          // Search the catalog.
          [SearchCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogRequest.html) searchCatalogRequest =
              [SearchCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogRequest.html).newBuilder().[setScope](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogRequest.Builder.html#com_google_cloud_datacatalog_v1_SearchCatalogRequest_Builder_setScope_com_google_cloud_datacatalog_v1_SearchCatalogRequest_Scope_)(scope).[setQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogRequest.Builder.html#com_google_cloud_datacatalog_v1_SearchCatalogRequest_Builder_setQuery_java_lang_String_)(query).build();
          [SearchCatalogPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.SearchCatalogPagedResponse.html) response = dataCatalogClient.searchCatalog(searchCatalogRequest);
    
          System.out.println("Search results:");
          for ([SearchCatalogResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogResult.html) result : response.iterateAll()) {
            System.out.println(result);
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Node.js API reference documentation](https://googleapis.dev/nodejs/datacatalog/latest/index.html). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client library.
    const {DataCatalogClient} = require('[@google-cloud/datacatalog](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)').v1;
    const datacatalog = new [DataCatalogClient](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)();
    
    async function searchAssets() {
      // Search data assets.
    
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'my_project'; // Google Cloud Platform project
    
      // Set custom query.
      const query = 'type=lake';
    
      // Create request.
      const scope = {
        includeProjectIds: [projectId],
        // Alternatively, search using Google Cloud Organization scopes.
        // includeOrgIds: [organizationId],
      };
    
      const request = {
        scope: scope,
        query: query,
      };
    
      const [result] = await datacatalog.searchCatalog(request);
    
      console.log(`Found ${[result](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.longrunning.operation.html).length} datasets in project ${projectId}.`);
      console.log('Datasets:');
      [result](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.longrunning.operation.html).forEach(dataset => {
        console.log(dataset.relativeResourceName);
      });
    }
    searchAssets();

### Python

Before trying this sample, follow the Python setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest)
    
    datacatalog = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[DataCatalogClient](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html)()
    
    # TODO: Set these values before running the sample.
    project_id = "project_id"
    
    # Set custom query.
    search_string = "type=dataset"
    scope = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[SearchCatalogRequest](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.SearchCatalogRequest.html).[Scope](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.SearchCatalogRequest.Scope.html)()
    scope.include_project_ids.append(project_id)
    
    # Alternatively, search using organization scopes.
    # scope.include_org_ids.append("my_organization_id")
    
    search_results = datacatalog.[search_catalog](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html#google_cloud_datacatalog_v1_services_data_catalog_DataCatalogClient_search_catalog)(scope=scope, query=search_string)
    
    print("Results in project:")
    for result in search_results:
        print(result)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datacatalog). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
