---
url: https://docs.cloud.google.com/data-catalog/docs/how-to/search/
title: Search data assets with Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:32:53.498598+00:00
---

# Search data assets with Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/how-to/search/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/data-catalog/docs/concepts/overview)



Send feedback 

#  Search data assets with Data Catalog Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use Data Catalog to search for data assets. 

You can search for the following data assets:

  * BigQuery sharing (formerly Analytics Hub) linked datasets
  * BigQuery datasets, tables, views, and models
  * Bigtable instances, clusters, and tables (including column family details)
  * Data Catalog tag templates, entry groups, and custom entries
  * Knowledge Catalog lakes, zones, tables, and filesets
  * Dataproc Metastore services, databases, and tables
  * Pub/Sub data streams
  * Spanner instances, databases, tables, and views
  * Vertex AI Models, Datasets, and Vertex AI Feature Store resources
  * Assets in enterprise data silos connected to Data Catalog



## Search scope

You might have different search results based on your permissions. Data Catalog search results are scoped according to your role.

The search results include those resources that belong to all organizations that you have access to.

You can review the different types of [IAM role and permissions](https://docs.cloud.google.com/data-catalog/docs/concepts/iam) available for Data Catalog. For example, if you have BigQuery metadata read access to an object, that object appears in your Data Catalog search results.

The following list describes the minimum permissions required to perform search:

  * To search for a table, you need `bigquery.tables.get` permission for that table.

  * To search for a dataset, you need `bigquery.datasets.get` permission for that dataset.

  * To search for metadata for a dataset or a table, you need the [`roles/bigquery.metadataViewer`](https://docs.cloud.google.com/bigquery/docs/access-control#bq-permissions) IAM role.

  * To search for all resources within a project or organization, you need `datacatalog.catalogs.searchAll` permission. It works for all resources independent of the source system.




If you have access to a BigQuery table but not to the dataset containing that table, the table still shows up as expected in the Data Catalog search. The same access logic applies to all supported systems, such as Pub/Sub and Data Catalog itself.

### Recall issues in search

Data Catalog search queries don't guarantee full recall. Results that match your query might not be returned, even in subsequent result pages. Additionally, if you repeat search queries, returned (and not returned) results can vary.

If you are experiencing recall issues and you don't have to fetch the results in any specific order, consider setting the `orderBy` parameter to `default` when calling the [catalog.search](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/catalog/search) method.

#### Use the `admin_search` flag

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Using the `admin_search` flag on the search request ensures full recall. Administrator search requires `datacatalog.catalogs.searchAll` permission to be set on all projects and organizations in the search scope. When using `admin_search`, only `default` `orderBy` is allowed.

### Date-sharded tables

Data Catalog aggregates date-sharded tables into a single logical entry. This entry has the same schema as the table shard with the most recent date, and contains aggregate information about the total number of shards. The entry derives its access level from the dataset it belongs to. Data Catalog search only shows these logical entries if the user has the access to the dataset that contains them. Individual date-sharded tables aren't visible in Data Catalog search, even if they are present in Data Catalog and can be tagged.

## Filters

Filters let you narrow down search results. All filters are grouped in sections:

  * **Scope** to limit search to starred items only.
  * **Systems** such as BigQuery, Pub/Sub, Knowledge Catalog, Dataproc Metastore, custom systems, Vertex AI, and Data Catalog itself. Data Catalog system contains filesets and custom entries.
  * **Lakes and zones** come from Knowledge Catalog.
  * **Data types** such as data streams, datasets, lakes, zones, filesets, models, tables, views, services, databases, and custom types.
  * **Projects** lists all projects available to you.
  * **Tags** lists all tag templates (and their individual fields) available to you.
  * **Datasets** come from BigQuery and Vertex AI.
  * **Public datasets** are publicly available data from BigQuery.



You can combine filters from multiple sections to find assets that match at least one condition from every selected section. Multiple filters selected within a single section are evaluated using the `OR` logical operator. For example, consider the following filter combination:

Example that shows how filters from multiple sections can be combined.![Tag value filter pane with multiple sections selected.](https://docs.cloud.google.com/static/data-catalog/images/multiple-filter-sections.png)

Data Catalog looks for the following:

  * BigQuery datasets tagged with `MyTemplate1` template.

  * BigQuery datasets tagged with `MyTemplate2` template.

  * BigQuery tables tagged with `MyTemplate1` template.

  * BigQuery tables tagged with `MyTemplate2` template.




### Filter by tag value

The **Tags** filters let you query for assets tagged using a specific template. You can use the playlist_add**Customize** menu to further refine results and filter by specific tag values. The tag value filter conditions depend on that tag field's data type. For example, for datetime and number fields, you can specify a specific date or a range.

### Filters visibility

The filters displayed in every section depend on the current query in the **Search** box. The whole set of search results might include entries that match the current query, but the filters that correspond to those entries might not be shown on the **Filters** pane.

**Note:** If you change selected filters, filter sets aren't refreshed. For example, if you select the BigQuery system in the **Systems** section, **Data type** filters don't narrow down to the BigQuery- specific data types, such as **Table** , **View** , and **Dataset**.

## Search for data assets

###  Console 

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex)

  2. For **Choose search platform** , select **Data Catalog** as the search mode.

  3. In the search field, enter your query or use the **Filters** pane to refine the search parameters.

You can manually add the following filters:

     * In **Projects** , add a project filter. Click **Add project** , search for and select a specific project, and click **Open**.
     * In **Tags** , add a tag template filter. Click the **Add more tag templates** menu, search for and select a specific template, and click **OK**.

To search for data assets publicly available in Google Cloud in addition to the assets available to you, select **Include public datasets**




Additionally, you can do the following:

  * Filter your search by adding a keyword:value to your search terms in the search field: 

Keyword| Description  
---|---  
`name:` | Match data asset name  
`column:` | Match column name or nested column name  
`description:` | Match table description  



* Perform a tag search by adding one of the following tag keyword prefixes to your search terms in the search field: 

Tag| Description  
---|---  
`tag:project-name.tag_template_name` | Match tag name  
`tag:project-name.tag_template_name.key` | Match a tag key  
`tag:project-name.tag_template_name.key:value` | Match tag `key:string value` pair  
  
### Search expression tips

  * Enclose your search expression in quotes ("`search terms`") if it contains spaces.

  * You can precede a keyword with "NOT" (all CAPS required) to match the logical negation of the `keyword:term` filter. You can also use "AND" and "OR" (all-CAPS required) boolean operators to combine search expressions.

For example:`NOT column:term` lists all columns except those that match the specified term. For a list of keywords and other terms you can use in a Data Catalog search expression, see [Data Catalog search syntax](https://docs.cloud.google.com/data-catalog/docs/how-to/search-reference).




### Search example

Consider an example where you want to search for the `trips` table that you set up in [Tag a BigQuery table by using Data Catalog](https://docs.cloud.google.com/data-catalog/docs/tag-bigquery-dataset):

  1. In the search field, enter `trips`, and click **Search**.
  2. In the **Filters** pane, select the following:

     * In the **Systems** section, select **BigQuery** to exclude data assets with the same name that belong to other systems.
     * In the **Projects** section, select your project ID to exclude data assets from other projects. If your project isn't displayed, click **Add project** and select your project.
     * In the **Tags** section, select **Demo Tag Template** to check if a tag that uses this template is attached to the `trips` table. If this template isn't displayed, click the **Add more tag templates** , search for and select the tag template, and click **OK**.



With all the selected filters, the search results contain only one entry—the BigQuery `trips` table in your project with an attached tag that uses the `Demo Tag Template` template.

**Note:** To preview the content of a BigQuery table, in the search result, click the manage_search next to the table.![](https://docs.cloud.google.com/static/data-catalog/images/search-filter-for-trips.png)

###  Java 

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

###  Node.js 

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

###  Python 

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

###  REST & CMD LINE 

### REST

If you don't have access to Cloud Client libraries for your language or want to test the API using REST requests, see the following examples and refer to the [Data Catalog REST API](https://docs.cloud.google.com/data-catalog/docs/reference/rest) documentation.

### 1\. Search catalog.

Before using any of the request data, make the following replacements: 

  * organization-id: GCP organization ID
  * project-id: GCP project ID



HTTP method and URL: 
    
    
    POST https://datacatalog.googleapis.com/v1/catalog:search

Request JSON body: 
    
    
    {
      "query":"trips",
      "scope":{
        "includeOrgIds":[
          "organization-id"
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datacatalog.googleapis.com/v1/catalog:search"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://datacatalog.googleapis.com/v1/catalog:search" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "results":[
        {
          "searchResultType":"ENTRY",
          "searchResultSubtype":"entry.table",
    "relativeResourceName":"projects/project-id/locations/US/entryGroups/@bigquery/entries/entry1-id",
          "linkedResource":"//bigquery.googleapis.com/projects/project-id/datasets/demo_dataset/tables/taxi_trips"
        },
        {
          "searchResultType":"ENTRY",
          "searchResultSubtype":"entry.table",
          "relativeResourceName":"projects/project-id/locations/US/entryGroups/@bigquery/entries/entry2-id",
          "linkedResource":"//bigquery.googleapis.com/projects/project-id/datasets/demo_dataset/tables/tlc_yellow_trips_2018"
        }
      ]
    }
    

## View table details

Use Data Catalog to view table details.

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/search)

  2. For **Choose search platform** , select **Data Catalog** as the search mode.

  3. In the search box, enter the name of a dataset that has a table.

For example, if you completed the [Tag a BigQuery table by using Data Catalog](https://docs.cloud.google.com/data-catalog/docs/tag-bigquery-dataset) quickstart, you can search for `demo-dataset` and select the `trips` table.

  4. Click the table.

The BigQuery table details page opens.




The table details include the following sections:

  * **BigQuery table details.** Includes information such as the time of creation, time of last modification, time of expiration, resource URLs, and labels.

  * **Tags.** Lists the applied tags.You can edit the tags from this page and view the tag template. Click the more_vert**Actions** icon.

  * **Schema and column tags.** Lists the applied schema and their values.




## Star your favorite entries and search for them

If you frequently browse the same data assets, you can include their entries in a personalized list by marking them with stars.

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/search)

  2. For **Choose search platform** , select **Data Catalog** as the search mode.

  3. Find your asset, and then star its entry in one of two ways:

     * Click star_border next to the entry in the search results.
     * Click the entry name to open its details page and click the star_border**STAR** on the action bar at the top.



You can star up to 200 entries.

Starred entries appear in the **Starred Entries** list on the search page before you enter a search query in the search bar. This list is visible only to you.

To search for only starred entries, in the **Filters** pane, in the **Scope** section, select **Starred**.

You can also use the corresponding methods of [Data Catalog API](https://docs.cloud.google.com/data-catalog/docs/reference) to star and unstar entries. When searching for assets, use the `starredOnly` parameter in the `scope` object. For more information, see the [catalog.search](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/catalog/search#Scope) method.

## What's next

  * Understand [search syntax for Data Catalog](https://docs.cloud.google.com/data-catalog/docs/how-to/search-reference).

  * Learn how to [search for resources in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-30 UTC."],[],[]] 
