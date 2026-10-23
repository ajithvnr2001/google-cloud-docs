---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/index-refresh-sitemap/
title: Index and refresh web pages using sitemaps \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:56.932831+00:00
---

# Index and refresh web pages using sitemaps  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/index-refresh-sitemap/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Index and refresh web pages using sitemaps Stay organized with collections  Save and categorize content based on your preferences. 

**Key Term:** The term _refresh_ can be used interchangeably with the term _recrawl_ in the context of a website. Refreshing or recrawling fetches the most recent version of a page and _indexes_ it. Reindexing indexes documents that have already been crawled.

If advanced website indexing is enabled in your data store, you can submit and use sitemaps to index and refresh the web pages in your data store. This feature supports only [XML sitemaps and sitemap indexes](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap#xml).

This page describes how to submit a sitemap or sitemap index to trigger sitemap-based indexing and refresh. To understand and implement automatic and manual refresh without a sitemap, see [Refresh web pages](https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites).

Additionally, this page describes how to view the sitemaps in your data store or delete a sitemap.

## Sitemap-based refresh concepts

Here are some key concepts and terms that'll help you get started:

  * **Sitemap protocol** : All sitemaps and sitemap indexes that Agent Search supports must follow the [sitemap protocol](https://www.sitemaps.org/protocol.html).

  * **Sitemap** : A sitemap is a UTF-8 encoded, XML file that contains a list of URLs of the web pages and files in your website with other important but optional information such as the web page's last modified date and the priority of the web page for a crawler against other web pages in your website. According to the [sitemap protocol](https://www.sitemaps.org/protocol.html), a single sitemap can contain a maximum of 50,000 URLs and it can be a maximum of 50 MB.

  * **Sitemap index** : When your sitemap exceeds the maximum URLs or maximum size, you can create multiple sitemaps and list these sitemaps in a sitemap index file. According to the [sitemap protocol](https://www.sitemaps.org/protocol.html), a single sitemap index can nest a maximum of 50,000 sitemaps and it can be a maximum of 50 MB.




You can submit one or more sitemaps, one or more sitemap indexes, or a combination of sitemaps and sitemap indexes to Agent Search.

When you submit your sitemap or sitemap index to the Agent Search data store, you trigger the following actions:

  * Indexing of the included URLs in your data store index.

    * For a sitemap-only refresh, this list contains only those URLs in the sitemap or sitemap index that fit the URL pattern included in your data store.
    * For a combination refresh, this list contains all the URLs that the automatic refresh process discovers.

For more information on these two refresh processes, see Website data store refresh methods and Sitemap-only refresh.

  * Daily refresh of any added, deleted, and updated URLs to the sitemap. An example of an updated URL is when you update the `lastmod` field of a URL in the sitemap.

  * Periodic refresh of unchanged URLs every 14 days.




### Website data store refresh methods

You can choose one of the following ways to incorporate sitemap-based refresh in your data store:

  * **Sitemap-only refresh** : Use sitemap-based refresh exclusively by turning off initial indexing and automatic refresh.
  * **Combination refresh** : Use sitemap-based refresh with initial indexing and automatic refresh.



You can [manually refresh](https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites#manual_refresh) specific web pages in your data store index at any time, regardless of the refresh method that you choose.

### Sitemap-only refresh

When you create a website data store, you must provide URL patterns for the web pages that you want to include in your data store's index. By default, when you finish creating a website data store, Agent Search generates an initial index for these included web pages.

For website data stores with advanced website indexing, the initial indexing process is a part of [automatic refresh](https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites#automatic_refresh). The initial indexing process indexes all the included URLs that are available in Google Search. The initial freshness of these URLs mirrors the freshness available in Google Search. After the initial indexing, the automatic refresh process discovers new pages and refreshes them on a best-effort basis. This can result in relatively stale pages and a bulkier index because this process discovers URLs that might be beyond what are required.

Instead, you can choose to perform sitemap-only refresh, which is useful in the following scenarios:

  * You have a well-maintained sitemap that's up-to-date.
  * You have a large website and you need a tighter control over which web pages are indexed. This results in a leaner, manageable index.
  * You need to refresh your added and updated pages daily, and remove deleted pages. This results in a fresher index that reflects the sitemap.



The following table compares the different methods that refresh the data store index:

Refresh method | Precision | Manual intervention | Frequency | Discovery  
---|---|---|---|---  
Sitemap-based refresh | Exact. Indexes only the URLs in the sitemaps. | Not required after submitting the sitemap or sitemap index | Daily for added, deleted, updated URLs in the sitemap. 14 days for unchanged URLs | Not beyond those specified in the sitemap.  
Manual refresh (also known as recrawl) | Exact. Indexes only the URLs specified in the recrawl request. | Required | On demand | No.  
Automatic refresh | Not exact. The data store is refreshed on a best-effort basis. | Not required | Random and on best-effort basis | Yes. Discovers URLs beyond what's available in Google Search.  
  
## Before you begin

Before you submit a sitemap or sitemap index to the Agent Search data store:

  * Create an XML sitemap or a sitemap index that references all the sitemaps for your website according to the [sitemap protocol](https://www.sitemaps.org/protocol.html).

    * Understand the fundamentals of building a sitemap. For more information, see Sitemap-based refresh concepts and [Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap).
  * Understand that to submit a sitemap or a sitemap index to the Agent Search data store, it's not necessary submit them to Google Search.

  * All the URLs in your sitemap that you want indexed must belong to public domains that are verified in your data store. For more information, see [Verify website domains](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification).

  * The sitemap URI (or the sitemap index URI with the nested sitemap URIs) must be publicly available and reachable by the [Googlebot](https://developers.google.com/search/docs/crawling-indexing/googlebot) user agent. Unlike web page crawling, which uses the `Google-CloudVertexBot` user agent, Agent Search uses `Googlebot` to fetch the sitemap file. If your `robots.txt` file, CDN, or firewall blocks `Googlebot` from the sitemap URI, Agent Search can't fetch the sitemap, and its URLs aren't indexed or refreshed through the sitemap, even when `Google-CloudVertexBot` is crawling your web pages.

  * If you use the `robots.txt` file in your website, update it to allow both the `Google-CloudVertexBot` user agent (to crawl and index your web pages) and the `Googlebot` user agent (to fetch your sitemap). For more information, see how to [prepare your website's `robots.txt` file](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#robots).




## Submit a sitemap or sitemap index to a data store

To trigger the indexing and refreshing of the included web pages in your data store, follow these steps:

  1. Decide whether you want to perform a sitemap-only refresh or combination refresh with other methods.

  2. To perform a sitemap-only refresh, follow this step, else skip to the next step.

You can't use an existing data store which has initial indexing and refreshing. You must create a new data store by turning off initial indexing and automatic refresh using the [`AdvancedSiteSearchConfig`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rpc/google.cloud.discoveryengine.v1#advancedsitesearchconfig) configuration.

### REST

Create a data store in which only sitemap refresh is enabled. This is done by turning off initial index and automatic refresh.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID&createAdvancedSiteSearch=true" \
         -d '{
            "displayName": "DATA_STORE_DISPLAY_NAME",
            "industryVertical": "GENERIC",
            "content_config": "PUBLIC_WEBSITE",
            "searchTier": "ENTERPRISE",
            "advancedSiteSearchConfig": {
               "disableInitialIndex": true,
               "disableAutomaticRefresh": true,
            }
         }'
         

Note: Setting `disableAutomaticRefresh` to `true` only deactivates the discovery-based automatic refresh. It does not affect the daily, automatic refresh that occurs based on the provided sitemap (checking for changes like the `lastmod` field).

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store that you want to create. This ID can contain only lowercase letters, digits, underscores, and hyphens.
     * `DATA_STORE_DISPLAY_NAME`: the display name of the Agent Search data store that you want to create.
**Note:** The [industry vertical](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/IndustryVertical) `GENERIC` is used to create structured, unstructured, and website data stores for custom search apps. 

#### Response

You should receive a JSON response similar to the following. 
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/collections/default_collection/operations/DATA_STORE_CREATION_OPERATION_ID",
      "done": true
    }
    

  3. Update the URL patterns of the sites to include and exclude in your data store. For more information, [Create a data store using website content](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#website).

  4. [Verify the domains](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification) of the web pages included in your data store.

  5. Whether you choose sitemap-only refresh or a combination refresh, submit a sitemap or sitemap index URI to a data store using the [`sitemaps.create`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.siteSearchEngine.sitemaps/create) method.

### REST

Submit a sitemap or sitemap index.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_NUMBER" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/siteSearchEngine/sitemaps?sitemap.uri=SITEMAP_URI"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.
     * `SITEMAP_URI`: the public URI for the individual sitemap or the sitemap index that you want to submit. When you submit a sitemap index, it's sufficient to submit the URI of the sitemap index. Agent Search automatically indexes the included URLs in all the sitemaps nested within the sitemap index.

#### Response

You should receive a JSON response similar to the following. If the value for the `done` key is `true`, it indicates that the operation to submit the sitemap was completed. Otherwise, the operation was unsuccessful. The response contains a `SITEMAP_ID`, which uniquely identifies the submitted sitemap or sitemap index. 
    
    {
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.Sitemap",
        "name": "projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/siteSearchEngine/sitemaps/SITEMAP_ID",
        "uri": "SITEMAP_URI",
        "createTime": "2024-11-11T16:22:30Z"
      }
    }
    

After you submit the sitemap or sitemap index to the data store, Agent Search triggers the following:

     * An indexing of the eligible URLs in the sitemap—those which are included in your data store. This process takes few hours on average to complete. Larger sitemaps can take longer to index.
     * A daily refresh of the web pages with eligible URLs.

To know how modifications to the sitemap or sitemap index effect the refresh, see Changes to sitemap and sitemap index.

  6. View the sitemaps in your data store.




## Changes to sitemap and sitemap index

After the initial submit, Agent Search detects modifications in your sitemap or sitemap index on a daily basis and handles these modifications in the following manner:

  * Changes to a sitemap: 
    * When you add URLs: URLs that match the included URLs pattern for the data store are added to the index and refreshed on a daily basis.
    * When you remove URLs: If the removed URLs are in the index, they're removed from the index and are no longer refreshed.
    * When you update the existing URLs—for example, when you update the `lastmod` field for a URL in the sitemap: Any updated URLs that match the included URLs pattern for the data store are refreshed. The refresh usually occurs within 24 hours after the update.
  * Changes to a sitemap index: 
    * When you add a sitemap: URLs in the new sitemap that match the included URLs pattern for the data store are added to the index and refreshed on a daily basis.
    * When you remove a sitemap: The URLs that match the included URLs pattern for the data store are no longer refreshed. However, they still remain in the index. To remove the sitemap and its URLs from the index, see Remove a sitemap and its URLs from the index.



## List the sitemaps and sitemap indexes in a data store

To list all the sitemaps and sitemap indexes in a data store, use the [`sitemaps.fetch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.siteSearchEngine.sitemaps/fetch) method. If you have submitted a sitemap index, then this method returns the sitemap index and not the individual, nested sitemaps. If there are no sitemaps in the data store, this request returns an empty JSON file.

### REST

List the sitemaps and sitemap indexes in a data store.
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/siteSearchEngine/sitemaps:fetch"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `DATA_STORE_ID`: the ID of the Agent Search data store.



#### Response

You should receive a JSON response similar to the following. The sitemap name for a given sitemap URI is unique and is needed when you delete the sitemap. 
    
    
     {
       "sitemapsMetadata": [
         {
           "sitemap": {
             "name": "projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/siteSearchEngine/sitemaps/SITEMAP_ID",
             "uri": "SITEMAP_URI"
           }
         }
       ]
     }
     

## Check whether a sitemap or sitemap index is present in a data store

To check whether a sitemap or sitemap index is present in a data store, use the `sitemaps.fetch` method. If the sitemap or sitemap index for which you're checking is submitted to the data store, then the response contains the sitemap name and URI of the sitemap. If you have submitted a sitemap index, then checking for individual sitemaps within the sitemap index won't return the correct results.

### REST

Check for a sitemap or sitemap index in a data store.
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/siteSearchEngine/sitemaps:fetch?matcher.uris_matcher.uris=SITEMAP_URI_1&matcher.uris_matcher.uris=SITEMAP_URI_2"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `DATA_STORE_ID`: the ID of the Agent Search data store.
  * `SITEMAP_URI_N`: the public URI of the sitemap or the sitemap index for which you want to check in the data store.



#### Response

You should receive a JSON response similar to the following. This response returns metadata of only the sitemaps that are present in the data store. 
    
    
     {
       "sitemapsMetadata": [
         {
           "sitemap": {
             "name": "projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/siteSearchEngine/sitemaps/SITEMAP_ID_1",
             "uri": "SITEMAP_URI_1"
           }
         }
       ]
     }
     

## Delete a sitemap or sitemap index from the data store

To delete a sitemap from the data store, use the [`sitemap.delete`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.siteSearchEngine.sitemaps/delete) method. Deleting a sitemap doesn't remove its URLs from the index. To remove the sitemap and its URLs from the index, see Remove a sitemap and its URLs from the index.

### REST

Delete a sitemap or sitemap index.
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/siteSearchEngine/sitemaps/SITEMAP_ID"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `DATA_STORE_ID`: the ID of the Agent Search data store.
  * `SITEMAP_ID`: a unique ID that identifies a sitemap or sitemap index. You can find this ID in the name field of the response when when you submit a sitemap or a sitemap index, or list the sitemaps and sitemap indexes in your data store.



#### Response

If the delete operation was successful, you should receive a JSON response similar to the following. 
    
    
     {
       "done": true
     }
     

## Remove a sitemap or a sitemap index and its URLs from the data store index

To remove a sitemap or a sitemap index and its URLs from the index, follow these steps:

  1. Empty the sitemap or the sitemap index that was submitted to the data store by removing all its URLs.

If you submitted a sitemap index to the data store, empty the nested sitemaps by removing all the URLs and remove the sitemap from the sitemap index.

  2. Wait for a period of 48 hours for Agent Search to process these changes and remove the URLs from the data store's index.

  3. Delete the sitemap or the sitemap index.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
