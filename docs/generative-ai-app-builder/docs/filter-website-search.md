---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search/
title: Filter website search \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:29.951810+00:00
---

# Filter website search  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Filter website search Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to filter search queries for a search app with [website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#websites).

## Before you begin

Make sure you have created an app and data store and have ingested website data into your data store. For more information, see [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es).

## About filter expressions

Use filter expressions to construct your website search filters. How you construct your filters varies depending on whether you have turned on [advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing). See one of the following sections, depending on whether you have basic website search or advanced website indexing:

  * Filter expressions for basic website search

  * Filter expressions for advanced website indexing




## Filter expressions for basic website search

This section explains filter expression behavior with basic website search (advanced website indexing is turned off).

### Syntax for basic website search

The following [Extended Backus–Naur form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form#:%7E:text=In%20compute) summarizes filter expression syntax for constructing a website search filter when you have basic website search. Double quotes after the colon in a filter are strictly enforced.
    
    
        # A single expression or multiple expressions that are joined by "AND".
      **filter** = **expression** , { "AND", **expression** };
      **expression** =
        # A simple expression applying to a text url string.
        | filter_key, ":", \"text_value\"
      **filter_key** = **( cr | highRange | lowRange | fileType | lr | rights | siteSearch)**;
      **text_value** = string value to filter on;

### Available fields for basic website search

Here are the fields that are available for filtering your website search when you have basic website search:

  * `cr` (string) Restricts search results to documents from a specific country. For a list of supported values, see [Country Collection Values](https://developers.google.com/custom-search/docs/json_api_reference#countryCollections).

  * `highRange` (string) Specifies the upper limit of the search range. If a document contains a number, the number must be at or below the value of `highRange` for that document to be included in the response. Specify both `highRange` and `lowRange` to create a search query within the range of these parameters.

  * `lowRange` (string) Specifies the lower limit of the search range. If a document contains a number, the number must be at or above the value of `lowRange` for that document to be included in the response. Specify both `lowRange` and `highRange` to create a search query within the range of these parameters.

  * `fileType` (string) Restricts search results to documents with a specified extension. For a list of supported file types, see [File types indexable by Google](https://developers.google.com/search/docs/crawling-indexing/indexable-file-types?visit_id=638338519105717597-4216646087&rd=1).

  * `lr` (string) Restricts search results to documents written in a specified language. For a list of supported languages, see [Query parameters (lr)](https://developers.google.com/custom-search/v1/reference/rest/v1/cse.siterestrict/list#body.QUERY_PARAMETERS.lr).

  * `rights` (string) Filters search results based on licensing. For supported values, see [Query parameters (rights)](https://developers.google.com/custom-search/v1/reference/rest/v1/cse.siterestrict/list#body.QUERY_PARAMETERS.rights).

  * `siteSearch` (string) Specifies A URL pattern for the web pages that your query should search through.




### Examples for basic website search

Here are some filter examples for basic website search:

  * `{"filter": "cr:\"countryUS\" AND siteSearch:\"https://example.com/example_domain\""}`

Filters for documents that are: (1) From the US, and (2) In the domain `https://example.com/example_domain`.

  * `{"filter": "fileType:\".pdf\" AND lr:\"lang_en\""}`

Filters for documents that are: (1) PDF files, and (2) In English.

  * `{"filter": "rights:\"cc_publicdomain\""}`

Filters for documents that are in the public domain.




## Filter expressions with advanced website indexing

This section explains filter expression behavior with advanced website indexing (advanced website indexing is turned on).

**Note:** Another approach to use filters with advanced website indexing is to apply document-level relevance filtering. For information about this Preview feature, see [Filter searches by document-level relevance](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance).

### Available fields for advanced website indexing

When you have advanced website indexing, you can filter your website search using these fields:

  * `siteSearch` (string): A URL pattern for the web pages that your query should search through.
  * `meta` tag names and PageMap Attribute names: Structured data from your web pages that can be added to your data store's schema to make the fields searchable, retrievable, and indexable. For more information, see [Use structured data for advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata).



### Syntax for advanced website indexing

The following [Extended Backus–Naur form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form#:%7E:text=In%20compute) summarizes filter expression syntax for constructing a website search filter when you have advanced website indexing. Double quotes after the colon in a filter are strictly enforced.

When filtering for `siteSearch` the EBNF syntax is:
    
    
        # A single expression or multiple expressions that are joined by "OR".
      **filter** = **expression** , { "OR", **expression** };
        # Expressions can be prefixed with "-" or "NOT" to express a negation.
      **expression** = [ "-" | "NOT " ],
        # A simple expression applying to a text url string.
        | filter_key, ":", \"url_string\"
      **filter_key** = **siteSearch** ;
      **url_string** = double quoted string representing a URL;

When filtering for `meta` tag names and PageMap Attribute names, the EBNF syntax is:
    
    
        # A single expression or multiple expressions that are joined by "OR".
      **filter** = **expression** , { "OR", **expression** };
        # Expressions can be prefixed with "-" or "NOT" to express a negation.
      **expression** = [ "-" | "NOT " ],
       # Function "ANY" returns true if the field exactly matches any of the literals.
        | text_field, ":", "ANY", "(", literal, { ",", literal }, ")"
       # A simple expression applying to any indexable field.
       # Preview: Function "EXISTS" returns true if the field is not NULL, empty, or containing the default value.
        | text_field, ":", "EXISTS"
        | numerical_field, ":", "EXISTS"
      **literal** = double quoted string;
      # text_field corresponds to the meta tag or PageMap Attribute name, for example, category
      **text_field** = text field;

### Examples for advanced website indexing

Here are some filter examples for advanced website indexing with `siteSearch`:

  * `{"filter": "siteSearch:\"https://example.com/example_domain\""}`

Filters for documents that are in the domain `https://example.com/example_domain`. For example, `https://example.com/example_domain/index.html`.

  * `{"filter": "siteSearch:\"https://example.com/subdomains/*\""}`

Filters for documents that are in any domains matching `https://example.com/subdomains/*`. For example, `https://example.com/subdomains/example_subdomain_page`.

  * `{"filter": "siteSearch:\"https://altostrat.com/subdomain/pages/*\" OR siteSearch:\"http://cymbalgroup.com/pages/*\""}`

Filters for documents that are in any domains matching the first or second URL pattern. For example, `https://altostrat.com/subdomain/pages/title_page`, `https://cymbalgroup.com/subdomain/pages/title_page`, or `https://altostrat.com/subdomain/pages/INFO`.




Here are some examples for `meta` or PageMap Attribute name filtering:

  * `{"filter": "product: EXISTS"}`

Filters for documents that contain the `meta` tag or PageMap attribute named `product`, with its value being not empty.

  * `{"filter": "product: ANY(\"networking\",\"compute\")"}`

Filters for documents that contain the `meta` tag or PageMap attribute named `product`, with its value as either `networking` or `compute`.

  * `{"filter": "NOT product: ANY(\"storage\")"}`

Filters for documents that don't contain the `meta` tag or PageMap Attribute name `product` with its value as `storage`.

  * `{"filter": "dateModified>= \"2025-07-31T00:00:00Z\")"}`

Filters for documents that have the last modified date as 31 July, 2025. The format must conform to format in the document schema. For more information, see [`DATETIME`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.schemas#Schema.FieldType.ENUM_VALUES.DATETIME).




For more information on `meta` tag names and PageMap Attribute names used for indexing, see [Example use case for `meta` tags](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata#example-meta-tags) and [Example use case for PageMaps](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata#example-pagemaps).

## Filter a website search

To filter a website search, follow these steps: **Note:** You can search over an app using the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method and you can search over a data store using the [`dataStores.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) method. For the following procedure, Google recommends searching using the `engines.servingConfigs.search` method.

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. To filter a website search, use the `filter` field with the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method.

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
          "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
         "query": "QUERY",
         "filter": "FILTER"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `APP_ID`: the ID of your app.
     * `QUERY`: the query text to search.
     * `FILTER`: a text field for filtering your search using a filter expression. The default value is an empty string.

For information about constructing a filter for basic website search, see Filter expressions with basic website search.

For information about constructing a filter for advanced website indexing, see Filter expressions with advanced website indexing.

**Troubleshooting:** If you use an `OR` operator in your filter expression and you receive the following error message, then advanced website indexing is not turned on for your app:  
`Parsing filter failed with error: Unsupported expression type in filter. Supported expression types are: (1) expression without logical joiner. (2) expressions joint by AND..`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
