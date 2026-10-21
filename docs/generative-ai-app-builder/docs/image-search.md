---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/image-search/
title: Search for images on websites \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:08.540057+00:00
---

# Search for images on websites  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/image-search/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Search for images on websites Stay organized with collections  Save and categorize content based on your preferences. 

With Agent Search, you can search for images using a app with website data. You supply a query in the form of a text string or an image, and the `default_config.search` method returns images for that query.

**Note:** Image search is not available using the Google Cloud console and is not supported for [blended search](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#blended) apps (apps with multiple data stores).

## Before you begin

Make sure you satisfy the following prerequisites. Requirements vary depending on whether you search using a text query or an image query.

  * If you search using a text query in your website search app, make sure the following is turned on: [Enterprise edition features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#enterprise-features)

  * If you search using an image query in your website search app, make sure the following are turned on:

    * [Enterprise edition features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#enterprise-features)

    * [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing)




## Preview image search

To use the command line to preview image results for a website, use the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method:

**Note:** You can search over an app using the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method and you can search over a data store using the [`dataStores.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) method. For the following procedure, Google recommends searching using the `engines.servingConfigs.search` method.

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Call the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method, specifying `1` for the `search_type`. Choose the method syntax depending on whether your query is text or image bytes.

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.

### Query is a text string
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_config:search" \
         -d '{
         "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
         "query": "QUERY",
         "pageSize": "PAGE_SIZE",
         "offset": "OFFSET",
         "params": {"search_type": 1}
         }'
         

### Query is an image
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
         "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
         "imageQuery": {"imageBytes":"IMAGE_BYTES"},
         "pageSize": "PAGE_SIZE",
         "offset": "OFFSET",
         "params": {"search_type": 1}
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.

     * `APP_ID`: the ID of your app.

     * `QUERY`: the search query text. For example, "Round headlight cars" or "show me dress with stripes."

     * `IMAGE_BYTES`: the image in Base64 encoded bytes. Supported formats are JPEG, PNG, and BMP.

     * `PAGE_SIZE`: optional. The number of results returned by the search. The default value is 10 for website search.

       * Values below 0 cause an error.
       * Values above 100 cause the value to be set to 100.
     * `OFFSET`: optional. The starting index of the results. The default value is 0.

For example, if the offset is 2 and the page size is 10, results 2 through 11 are returned.

  3. Review the response. See the following table for field descriptions:

Field  | Description   
---|---  
`title` | The plain text title of the web page that contains the image   
`htmlTitle` | The title, in HTML, of the web page that contains the image   
`displayLink` | An abridged version of this search's result URL, usually the domain name—for example, `www.example.com`  
`link` | The URL of the image   
`image.contextLink` | Context link: A URL pointing to the web page that contains the image   
`image.byteSize` | The size of the image, in bytes   
`image.width` | The width of the image, in pixels   
`image.height` | The height of the image, in pixels   
`image.thumbnailWidth` | The width of the thumbnail image, in pixels   
`image.thumbnailHeight` | The height of the thumbnail image, in pixels   
`image.thumbnailLink` | The URL of the thumbnail image   
`mime` | The MIME type of the image   
`fileFormat` | The file format of the image   



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
