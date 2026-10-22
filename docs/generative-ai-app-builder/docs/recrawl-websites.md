---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites/
title: Refresh web pages using automatic and manual refresh \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:46.342270+00:00
---

# Refresh web pages using automatic and manual refresh  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Refresh web pages using automatic and manual refresh Stay organized with collections  Save and categorize content based on your preferences. 

**Key Term:** The term _refresh_ can be used interchangeably with the term _recrawl_ in the context of a website. Refreshing or recrawling fetches the most recent version of a page and _indexes_ it. Reindexing indexes documents that have already been crawled.

If your data store uses basic website search, the freshness of your store's index mirrors the freshness that's available in Google Search.

If advanced website indexing is enabled in your data store, the web pages in your data store are refreshed in the following ways:

  * Automatic refresh
  * Manual refresh
  * Sitemap-based refresh



This page describes automatic and manual refresh. To understand and implement sitemap-based refresh, see [Index and refresh according to sitemap](https://docs.cloud.google.com/generative-ai-app-builder/docs/index-refresh-sitemap).

## Before you begin

If you use the `robots.txt` file in your website, update it. For more information, see how to [prepare your website's `robots.txt` file](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#robots).

## Automatic refresh

Agent Search performs automatic refresh as follows:

  * After you create a data store, it generates an initial index for the included pages.
  * After the initial indexing, it indexes any newly discovered pages and recrawls existing pages on a best-effort basis.
  * It regularly refreshes data stores that encounter a query rate of 50 queries/30 days.

**Note:** The **Automatic refresh** feature is a discovery-based process for finding new pages that are not listed in a sitemap. When using sitemaps for precise indexing control, we recommend disabling this feature. Disabling **Automatic refresh** does not stop the separate refresh process based on sitemap modifications. For more information, see [Index and refresh web pages using sitemaps](https://docs.cloud.google.com/generative-ai-app-builder/docs/index-refresh-sitemap).

## Manual refresh

If you want to refresh specific web pages in a data store with [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing) turned on, you can call the [`recrawlUris`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.siteSearchEngine/recrawlUris) method. You use the `uris` field to specify each web page that you want to crawl. The `recrawlUris` method is a [long-running operation](https://docs.cloud.google.com/generative-ai-app-builder/docs/long-running-operations) that runs until your specified web pages are crawled or until it times out after 24 hours, whichever comes first. If the `recrawlUris` method times out you can call the method again, specifying the web pages that remain to be crawled. You can poll the [`operations.get`](https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.operations/get) method to monitor the status of your recrawl operation.

**Note:** The [`recrawlUris`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.siteSearchEngine/recrawlUris) method recognizes literal URIs, not URI patterns. Any asterisk (`*`) in your URI is treated as a regular character. This is different from specifying the URLs to index when creating a website data store. When creating a data store, you can specify individual web pages or use wildcards to specify an entire website or part of a website—for example, `www.mysite.com/*`. By contrast, `recrawlUris` assumes `www.mysite.com/*` is a single page. For more information about creating a website data store, see [Website URLs](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#website).

### Limits on recrawling

There are limits to how often you can crawl web pages and how many web pages that you can crawl at a time:

  * **Calls per day.** The maximum number of calls to the `recrawlUris` method allowed is 20 per day, per project.
  * **Web pages per call.** The maximum number of `uris` values that you can specify with a call to the `recrawlUris` method is 10,000.



### Recrawl the web pages in your data store

You can manually crawl specific web pages in a data store that has [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing) turned on.

### REST

To use the command line to crawl specific web pages in your data store, follow these steps:

  1. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  2. Call the [`recrawlUris`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.siteSearchEngine/recrawlUris) method, using the `uris` field to specify each web page that you want to crawl. Each `uri` represents a single page even if it contains asterisks (`*`). Wildcard patterns are not supported.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/siteSearchEngine:recrawlUris" \
         -d '{
           "uris": [URIS]
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.
     * `URIS`: the list of web pages that you want to crawl—for example, `"https://example.com/page-1", "https://example.com/page-2", "https://example.com/page-3"`.

The output is similar to the following:
    
    {
      "name": "projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/operations/recrawl-uris-0123456789012345678",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.RecrawlUrisMetadata"
      }
    }
    

  3. Save the `name` value as input for the `operations.get` operation when monitoring the status of your recrawl operation.




### Monitor the status of your recrawl operation

The `recrawlUris` method, which you use to crawl web pages in a data store, is a [long-running operation](https://docs.cloud.google.com/generative-ai-app-builder/docs/long-running-operations) that runs until your specified web pages are crawled or until it times out after 24 hours, whichever comes first. You can monitor the status of the this long-running operation by polling the [`operations.get`](https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.operations/get) method, specifying the `name` value returned by the `recrawlUris` method. Continue polling until the response indicates that either: (1) All of your web pages are crawled, or (2) The operation timed out before all of your web pages were crawled. If `recrawlUris` times out, you can call it again, specifying the websites that were not crawled.

### REST

To use the command line to monitor the status of a recrawl operation, follow these steps:

  1. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  2. Poll the [`operations.get`](https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.operations/get) method.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/OPERATION_NAME"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `OPERATION_NAME`: the operation name, found in the `name` field returned in your call to the `recrawlUris` method in Recrawl the web pages in your data store. You can also get the operation name by [listing long-running operations](https://docs.cloud.google.com/generative-ai-app-builder/docs/long-running-operations#list-lros).
  3. Evaluate each response.

     * If a response indicates that there are pending URIs and the recrawl operation is not done, your web pages are still being crawled. Continue polling.

Example
           
           {
               "name": "projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/operations/recrawl-uris-0123456789012345678",
               "metadata": {
                 "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.RecrawlUrisMetadata",
                 "createTime": "2023-09-05T22:07:28.690950Z",
                 "updateTime": "2023-09-05T22:22:10.978843Z",
                 "validUrisCount": 4000,
                 "successCount": 2215,
                 "pendingCount": 1785
               },
               "done": false,
               "response": {
                 "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.RecrawlUrisResponse",
               }
             }

The response fields can be described as follows:

       * `createTime`: indicates the time that the long-running operation started.
       * `updateTime`: indicates the last time that the long-running operation metadata was updated. indicates the metadata updates every five minutes until the operation is done.
       * `validUrisCount`: indicates that you specified 4,000 valid URIs in your call to the `recrawlUris` method.
       * `successCount`: indicates that 2,215 URIs were successfully crawled.
       * `pendingCount`: indicates that 1,785 URIs have not yet been crawled.
       * `done`: a value of `false` indicates that the recrawl operation is still in progress.

     * If a response indicates that there are no pending URIs (no `pendingCount` field is returned) and the recrawl operation is done, then your web pages are crawled. Stop polling—you can quit this procedure.

Example
           
           {
               "name": "projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/operations/recrawl-uris-0123456789012345678",
               "metadata": {
                 "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.RecrawlUrisMetadata",
                 "createTime": "2023-09-05T22:07:28.690950Z",
                 "updateTime": "2023-09-05T22:37:11.367998Z",
                 "validUrisCount": 4000,
                 "successCount": 4000
               },
               "done": true,
               "response": {
                 "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.RecrawlUrisResponse"
               }
             }

The response fields can be described as follows:

       * `createTime`: indicates the time that the long-running operation started.
       * `updateTime`: indicates the last time that the long-running operation metadata was updated. indicates the metadata updates every five minutes until the operation is done.
       * `validUrisCount`: indicates that you specified 4,000 valid URIs in your call to the `recrawlUris` method.
       * `successCount`: indicates that 4,000 URIs were successfully crawled.
       * `done`: a value of `true` indicates that the recrawl operation is done. 

  4. If a response indicates that there are pending URIs and the recrawl operation is done, then the recrawl operation timed out (after 24 hours) before all of your web pages were crawled. Start again at Recrawl the web pages in your data store. Use the `failedUris` values in the `operations.get` response for the values in the `uris` field in your new call to the `recrawlUris` method.

Example.
         
         {
           "name": "projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/operations/recrawl-uris-8765432109876543210",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.RecrawlUrisMetadata",
             "createTime": "2023-09-05T22:07:28.690950Z",
             "updateTime": "2023-09-06T22:09:10.613751Z",
             "validUrisCount": 10000,
             "successCount": 9988,
             "pendingCount": 12
           },
           "done": true,
           "response": {
             "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.RecrawlUrisResponse",
             "failedUris": [
               "https://example.com/page-9989",
               "https://example.com/page-9990",
               "https://example.com/page-9991",
               "https://example.com/page-9992",
               "https://example.com/page-9993",
               "https://example.com/page-9994",
               "https://example.com/page-9995",
               "https://example.com/page-9996",
               "https://example.com/page-9997",
               "https://example.com/page-9998",
               "https://example.com/page-9999",
               "https://example.com/page-10000"
             ],
             "failureSamples": [
               {
                 "uri": "https://example.com/page-9989",
                 "failureReasons": [
                   {
                     "corpusType": "DESKTOP",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   },
                   {
                     "corpusType": "MOBILE",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   }
                 ]
               },
               {
                 "uri": "https://example.com/page-9990",
                 "failureReasons": [
                   {
                     "corpusType": "DESKTOP",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   },
                   {
                     "corpusType": "MOBILE",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   }
                 ]
               },
               {
                 "uri": "https://example.com/page-9991",
                 "failureReasons": [
                   {
                     "corpusType": "DESKTOP",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   },
                   {
                     "corpusType": "MOBILE",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   }
                 ]
               },
               {
                 "uri": "https://example.com/page-9992",
                 "failureReasons": [
                   {
                     "corpusType": "DESKTOP",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   },
                   {
                     "corpusType": "MOBILE",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   }
                 ]
               },
               {
                 "uri": "https://example.com/page-9993",
                 "failureReasons": [
                   {
                     "corpusType": "DESKTOP",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   },
                   {
                     "corpusType": "MOBILE",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   }
                 ]
               },
               {
                 "uri": "https://example.com/page-9994",
                 "failureReasons": [
                   {
                     "corpusType": "DESKTOP",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   },
                   {
                     "corpusType": "MOBILE",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   }
                 ]
               },
               {
                 "uri": "https://example.com/page-9995",
                 "failureReasons": [
                   {
                     "corpusType": "DESKTOP",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   },
                   {
                     "corpusType": "MOBILE",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   }
                 ]
               },
               {
                 "uri": "https://example.com/page-9996",
                 "failureReasons": [
                   {
                     "corpusType": "DESKTOP",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   },
                   {
                     "corpusType": "MOBILE",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   }
                 ]
               },
               {
                 "uri": "https://example.com/page-9997",
                 "failureReasons": [
                   {
                     "corpusType": "DESKTOP",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   },
                   {
                     "corpusType": "MOBILE",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   }
                 ]
               },
               {
                 "uri": "https://example.com/page-9998",
                 "failureReasons": [
                   {
                     "corpusType": "DESKTOP",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   },
                   {
                     "corpusType": "MOBILE",
                     "errorMessage": "Page was crawled but was not indexed by UCS within 24 hours."
                   }
                 ]
               }
             ]
           }
         }

Here are some descriptions of response fields:

     * `createTime`. The time that the long-running operation started.
     * `updateTime`. The last time that the long-running operation metadata was updated. The metadata updates every five minutes until the operation is done.
     * `validUrisCount`. Indicates that you specified 10,000 valid URIs in your call to the `recrawlUris` method.
     * `successCount`. Indicates that 9,988 URIs were successfully crawled.
     * `pendingCount`. Indicates that 12 URIs have not yet been crawled.
     * `done`. A value of `true` indicates that the recrawl operation is done.
     * `failedUris`. A list of URIs that were not crawled before the recrawl operation timed out.
     * `failureInfo`. Information about URIs that failed to crawl. At most, ten `failureInfo` array values are returned, even if more than ten URIs failed to crawl.
     * `errorMessage`. The reason a URI failed to crawl, by `corpusType`. For more information, see Error messages. 




### Timely refresh

Google recommends that you perform manual refresh on your new and updated pages to ensure that you have the latest index.

### Error messages

When you are monitoring the status of your recrawl operation, if the recrawl operation times out while you are polling the `operations.get` method, `operations.get` returns error messages for web pages that were not crawled. The following table lists the error messages, whether the error is transient (a temporary error that resolves itself), and the actions that you can take before retrying the `recrawlUris` method. You can retry all transient errors immediately. All intransient errors can be retried after implementing the remedy.

Error message  | Is it a transient error?  | Action before retrying recrawl   
---|---|---  
**Page was crawled but was not indexed by Agent Search within 24 hours** | Yes | Use the `failedUris` values in the `operations.get` response for the values in the `uris` field when you call the `recrawlUris` method.  
**Crawling was blocked by the site's`robots.txt`** | No | Unblock the URI in your website's `robots.txt` file, ensure that the Google-CloudVertexBot user agent is permitted to crawl the website, and retry recrawl. For more information, see [Website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data) in _Prepare data for ingesting_. If you can't access the `robots.txt` file, contact the domain owner.  
**Page is unreachable** | No | Check the URI that you specified when you call the `recrawlUris` method. Ensure you provide the literal URI and not a URI pattern.  
**Crawling timed out** | Yes | Use the `failedUris` values in the `operations.get` response for the values in the `uris` field when you call the `recrawlUris` method.  
**Page was rejected by Google crawler** | Yes | Use the `failedUris` values in the `operations.get` response for the values in the `uris` field when you call the `recrawlUris` method.  
**URL could not be followed by Google crawler** | No | If there are multiple redirects, use the URI from the last redirect and retry  
**Page was not found (404)** | No | Check the URI that you specified when you call the `recrawlUris` method. Ensure you provide the literal URI and not a URI pattern. Any page that responds with a `4xx` error code is removed from the index.  
**Page requires authentication** | No | Advanced website indexing doesn't support crawling web pages that require authentication.  
  
## How deleted pages are handled

When a page is deleted, Google recommends that you manually refresh the deleted URLs.

When your website data store is crawled during either an automatic or a manual refresh, if a web page responds with a `4xx` client error code or `5xx` server error code, the unresponsive web page is removed from the index.

If the data store is set so that **Sitemap Mode** is **Exact** , then removing a URL from the sitemap deletes the URL from the index.

If the data store is set so that **Sitemap Mode** is **Discovery** , then removing a URL from the sitemap doesn't delete the URL from the index. The URL won't be deleted from the index until the website is crawled and the page returns a `4xx` or `5xx` code.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
