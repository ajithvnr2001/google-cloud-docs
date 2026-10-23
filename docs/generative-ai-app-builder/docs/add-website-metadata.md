---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata/
title: Use structured data for advanced website indexing \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:05.688607+00:00
---

# Use structured data for advanced website indexing  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Use structured data for advanced website indexing Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If advanced website indexing is enabled in your data store, you can use the following types of structured data to enrich your indexing:

  * Predefined, Google-inferred page dates
  * Custom structured data attributes
    * Metadata using `meta` tags
    * PageMaps
    * Schema.org data



This page introduces both these types of structured data for your web pages and describes how to add custom structured attributes to your data store schema.

## About predefined, Google-inferred page dates

When crawling through the web pages in your website data store, Google infers page data using the properties that apply to your content. Agent Search adds these inferred page data properties to your schema. This inferred data includes the following predefined date properties, which are also called _byline dates_ :

  * `datePublished`: the date and time when the page was first published
  * `dateModified`: the date and time when the page was most recently modified



These properties are indexed automatically. You can directly use these date properties to enrich your search without adding them to your schema. To add byline dates to your website, see [Influence your byline dates in Google Search](https://developers.google.com/search/docs/appearance/publication-dates).

To understand how to include these predefined date properties in your search requests, such as in filter expressions and boost specifications, see [Example use case using a Google-inferred page date](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results#predefined-date-example).

## About custom datetime fields on a web page

You can add custom datetime fields to your web pages. Such tags can be used with advanced indexing when you add custom structured data attributes to the data store schema. Here's an example that shows where to add a custom datetime meta tag named `lastModified` on your web page.
    
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Your web page title</title>
    
        <!-- Agent Search can use this date. -->
        <meta name="lastModified" content="2022-07-01">
    </head>
    <body>
        </body>
    </html>
    

To understand how to include such custom datetime tags in your search requests, such as in filter expressions and boost specifications, see [Example use case using a custom datetime attribute](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results#custom-datetime-example).

## About custom structured data attributes

You can add structured data attributes as `meta` tags and PageMaps to your web pages and use these to enrich your indexing. To use custom structured attributes for indexing, you must update your schema.

### Example use case for `meta` tags

Suppose you have a large number of web pages that are relevant to various departments in your organization. You can use `meta` tags to label the pages that are relevant for each department. You can then use the indexed tags as filters in your queries. This lets you to restrict search results to web pages containing a label that matches any of the specified departments.

This process can be summarized as follows:

  1. Add the following `meta` tags to a subset of your web pages:

     * Relevant to engineering and IT departments:
           
           <meta name="department" content="eng, infotech">
           <meta property="og:title" content="Password best practices">
           

     * Relevant to finance and HR departments:
           
           <meta name="department" content="finance, human resources">
           <meta property="og:image" content="https://example.com/images/team-training-contractors.jpg">
           

For a more elaborate example, see Example `meta` tags on a web page.

  2. Recrawl the updated pages.

  3. Add `department` to your data store schema as an indexable array as described in the Add custom structured data attributes to the data store schema section.




After updating your schema, your data store is automatically reindexed. After the reindexing is complete, you can use the `department` filter in a [filter expression](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax) to reorder or filter search results. For example, when users from the finance department issue queries, the search results can be made more relevant for them with the `department` [filter](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search) set to `finance`.

### Example `meta` tags on a web page

Here's an example of the `meta` tags that you can add to your web page. Such tags can be used with advanced indexing when you add custom structured data attributes to the data store schema.
    
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Your web page title</title>
    
        <!-- Robots instructions for crawlers and for Agent Search. -->
        <meta name="robots" content="index,follow">
    
        <!-- Agent Search can use custom datetime fields to filter, boost, and order. -->
        <meta name="lastModified" content="2024-09-06">
    
        <!-- Agent Search can filter by category or tags. -->
        <meta name="category" content="archived">
        <meta name="tags" content="legacy,interesting,faq">
    
        <!-- Agent Search can index these common HTML tags. -->
        <meta name="description" content="A description of your web page's content.">
        <meta name="author" content="Your name or organization">
        <meta name="keywords" content="relevant,keywords,separated,by,commas">
        <link rel="canonical" href="https://www.yourwebsite.com/this-page">
        <meta property="og:title" content="Your Webpage Title">
        <meta property="og:description" content="A description of your webpage's content.">
        <meta property="og:image" content="https://www.yourwebsite.com/image.jpg">
        <meta property="og:url" content="https://www.yourwebsite.com/this-page">
        <meta property="og:type" content="website">
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:title" content="Your customized Webpage Title">
        <meta name="twitter:description" content="A description of your webpage's content.">
        <meta name="twitter:image" content="https://www.yourwebsite.com/image.jpg">
    </head>
    <body>
    ...
    </body>
    </html>
    

### Example use case for PageMaps

Suppose you have several web pages that contain food recipes. You can add PageMap data to each page's HTML content. You can then use the indexed PageMap attribute names as filters in your queries. For example, if you intend to boost or bury web pages depending on the recipe ratings, you can follow this process:

  1. Add PageMap data similar to the following to your web pages:
         
         <html>
         <head>
         ...
         <!--
         <PageMap>
             <DataObject type="document">
                 <Attribute name="title">Baked potatoes</Attribute>
                 <Attribute name="author">Dana A.</Attribute>
                 <Attribute name="description">Homestyle baked potatoes in oven. This
                 recipe uses Russet potatoes.</Attribute>
                 <Attribute name="rating">4.9</Attribute>
                 <Attribute name="lastUpdate">2015-01-01</Attribute>
             </DataObject>
         </PageMap>
         -->
         </head>
         ...
         </html>
         

  2. Recrawl the updated pages.

  3. Add `rating` to your data store schema as an indexable array as described in the Add custom structured data attributes to the data store schema section.




After updating your schema, your data store is automatically reindexed. After the reindexing is complete, you can use the `rating` attribute in a [filter expression](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax) to reorder or filter search results. For example, when users search for recipes, boost the search results that are top-rated by using `rating` as a [custom numerical attribute](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results#custom-numerical-attr-boost).

### Example use case for schema.org data

Suppose you have a review website and its web pages are annotated with schema.org data in JSON-LD format within the HTML `script` tag. You can then use the indexed annotations as filters in your queries. For example, if you intend to boost or bury web pages depending on the aggregate ratings, you can follow this process:

  1. Add the schema.org annotations for [review content](https://schema.org/Review) similar to the following to your web pages. To view other types of schema.org templates that are available, see [Schemas](https://schema.org/docs/schemas.html):
         
         <script type="application/ld+json">
         {
           "@context": "https://schema.org",
           "@type": "Review",
           "aggregateRating": {
             "@type": "Average Rating",
             "ratingValue": 3.5,
             "reviewCount": 11
           },
           "description": "Published in 1843, this is the perfect depiction of the Victorian London. A Christmas Carol is the story of Ebenezer Scrooge's transformation.",
           "name": "A Christmas Carol",
           "image": "christmas-carol-first-ed.jpg",
           "review": [
             {
               "@type": "Review",
               "author": "Alex T.",
               "datePublished": "2000-01-01",
               "reviewBody": "Read this in middle school and have loved this ever since.",
               "name": "Worth all the adaptations",
               "reviewRating": {
                 "@type": "Rating",
                 "bestRating": 5,
                 "ratingValue": 5,
                 "worstRating": 1
               }
             }
           ]
         }
         </script>
         

  2. Recrawl the updated pages.

  3. Add the path to `ratingValue` to your data store schema. Use an identifier as the field name in the data store schema, such as `rating_value` as described in the Add custom structured data attributes to the data store schema section.




After updating your schema, your data store is automatically reindexed. After the reindexing is complete, you can use the `rating_value` attribute in a [filter expression](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax) to reorder or filter search results. For example, when users search for books, boost the search results that are top-rated by using `rating_value` as a [custom numerical attribute](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results#custom-numerical-attr-boost).

## Before you begin

Before you update the data store schema, do the following:

  * Turn on advanced website indexing for the data store. For more information, see [Turn on advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-on-advanced-indexing).
  * [Understand how structured data works](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).
  * Understand how to [use PageMaps](https://developers.google.com/custom-search/docs/structured_data#using-pagemaps). Review the list of [recognized DataObjects](https://support.google.com/programmable-search/answer/1628213) that can be added to PageMap data.
  * Understand how to [use `meta` tags](https://developers.google.com/custom-search/docs/structured_data#using-meta-tags). Ensure that you don't use any [excluded `meta` tag names](https://developers.google.com/custom-search/docs/structured_data#excluded-meta-tags) or [unsupported meta tags](https://developers.google.com/search/docs/crawling-indexing/special-tags#unsupported-tags-and-attributes). However, if you already have excluded `meta` tag names, see the `siteSearchMetatagName` workaround.
  * Ensure that the attribute that needs to be indexed doesn't have any of the following values: 
    * `datePublished`
    * `dateModified`
    * `siteSearch`
  * Understand that after you add structured data to your web pages, you must recrawl the pages. This might take several hours.
  * Understand that after you add structured data attributes to the data store schema, the web pages in your data store are reindexed automatically. Reindexing is a long-running operation that might take several hours.



## Add custom structured data attributes to the data store schema

To add custom structured data attributes to the data store schema:

  1. Add `meta` tags, PageMap data, and schema.org data to the pages in your website that you want to enrich with structured data indexing:

     * For `meta` tags:

       * Each `meta` tag must have its `name` attribute set to the field you want to index and its `content` attribute to a string of one or more comma-separated values.
       * Agent Search supports `meta` tags with names that match the pattern `[a-zA-Z0-9][a-zA-Z0-9-_]*`. However, if you already have `meta` tags with names that include other characters, see the `siteSearchMetatagName` workaround.
       * Agent Search doesn't support the use of any [excluded `meta` tag names](https://developers.google.com/custom-search/docs/structured_data#excluded-meta-tags) or [unsupported meta tags](https://developers.google.com/search/docs/crawling-indexing/special-tags#unsupported-tags-and-attributes). However, if you already have excluded `meta` tag names, see the `siteSearchMetatagName` workaround.
     * For PageMap data:

       * PageMap data must consist of [recognized DataObjects](https://support.google.com/programmable-search/answer/1628213) that contain Attribute names that you want to index. The Attribute names within the DataObjects must be set to the field you want to index.
     * For schema.org data:

       * The annotations must be in valid JSON-LD, Microdata, or RDFa format. For more information, see [Supported formats](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data#supported-formats).
  2. [Recrawl](https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites) the updated web pages.

  3. [View the schema definition](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-schema-definition) for your data store over REST API.

  4. [Update the data store schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas) using Google Cloud console or the API. If you choose to do it over the API, learn how to [provide your own schema as a JSON object](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema#provide-your-own).

     1. Add objects for each custom attribute that you want to make searchable, retrievable, or indexable.

     2. Add the custom attribute and set its `type` to `array`.

     3. Add the data type of the custom attribute's value.

     4. Specify the source of the custom attribute where it can be found in the `siteSearchStructuredDataSources` field.

     5. For schema.org data: Specify the path of the attribute in the schema.org annotation starting with string `_root` in the `siteSearchSchemaOrgPaths` field.

The following is an example of a schema update for a website:
    
    {
      "type": "object",
      "properties": {
        "CUSTOM_ATTRIBUTE": {
          "type": "array",
          "items": {
            "type": "DATA_TYPE",
            "searchable": true,
            "retrievable": true,
            "indexable": true,
            "siteSearchMetatagName": "METATAG_NAME",
            "siteSearchStructuredDataSources": ["STRUCTURED_DATA_SOURCE_1", "STRUCTURED_DATA_SOURCE_2"]
          }
        },
        "IDENTIFIER_FOR_SCHEMA_ORG_FIELD": {
          "type": "array",
          "items": {
            "type": "DATA_TYPE_SCHEMA_ORG_FIELD",
            "searchable": true,
            "retrievable": true,
            "indexable": true,
            "siteSearchSchemaOrgPaths": ["_root.PATH_TO_THE_SCHEMA_ORG_FIELD"]
          }
        }
      },
      "$schema": "https://json-schema.org/draft/2020-12/schema"
    }

Replace the following:

     * `CUSTOM_ATTRIBUTE`: the value of the `name` attribute. For example:

       * For a `meta` tag defined as `<meta name="department" content="eng, infotech">`, use `department`
       * For a PageMap Attribute defined as `<Attribute name="rating">4.9</Attribute>`, use `rating`
     * `DATA_TYPE`: the data type of the `name` attribute. Must be either string, number, or datetime. For example:

       * For a `meta` tag defined as `<meta name="department" content="eng, infotech">`, use `string`
       * For a PageMap Attribute defined as `<Attribute name="rating">4.9</Attribute>`, use `number`
       * For a PageMap Attribute defined as `<Attribute name="lastPublished">2015-01-01</Attribute>`, use `datetime`

For more information, see [`FieldType`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.schemas#fieldtype).

     * `METATAG_NAME`: The value for the `siteSearchMetatagName` field, which lets you specify the exact name of a `meta` tag from your web page.

You only need to use the `siteSearchMetatagName` workaround in the following scenarios:

       * The `meta` tag's `name` attribute contains special characters (such as a colon) and doesn't match the required pattern for `CUSTOM_ATTRIBUTE`, which is `[a-zA-Z0-9][a-zA-Z0-9-_]*`.

> For example, if you have a tag `<meta name="og:updated_time">`, then, you can't use `og:updated_time` as a `CUSTOM_ATTRIBUTE`. Instead, you would use a compliant identifier for `CUSTOM_ATTRIBUTE` (like `og_updated_time`) and then, set the value of `siteSearchMetatagName` to `og:updated_time`.

       * The `meta` tag's `name` attribute is an [excluded `meta` tag name](https://developers.google.com/custom-search/docs/structured_data#excluded-meta-tags).

> For example, if you have a tag `<meta name="description">`, then, you can't use `description` as a `CUSTOM_ATTRIBUTE`. Instead, you would use a compliant identifier for `CUSTOM_ATTRIBUTE` (like `meta_tag_description`) and then, set the value of `siteSearchMetatagName` to `meta_tag_description`.

When you use `siteSearchMetatagName` to update the schema, you must use the v1alpha endpoint instead of the v1 endpoint to call the [`schema`](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas) method.

     * `STRUCTURED_DATA_SOURCE_N`: an array consisting of one or both of the following structured data sources where the `CUSTOM_ATTRIBUTE` attribute can be found:

       * If the custom attribute can be found as a `meta` tag, specify `METATAGS`
       * If the custom attribute can be found as a PageMap attribute, specify `PAGEMAP`
       * If the custom attribute can be found as a schema.org data, specify `SCHEMA_ORG`
       * If the `siteSearchStructuredDataSources` field is absent or left empty, the values from all three data sources are merged in an array.
     * `IDENTIFIER_FOR_SCHEMA_ORG_FIELD`: a custom identifier to denote the schema.org field. It doesn't need to be exactly same as the field name in the schema.org annotation on your web page. For example, if the path of the field is `_root.nutrition.calories`, the identifier can be `calorific_value` or `nutrition_value`.

     * `DATA_TYPE_SCHEMA_ORG_FIELD`: the data type of the schema.org field. Must be string, number, or datetime. For example:

       * For a schema.org field defined as "calories":"240 calories", use `string`
       * For a schema.org field defined as "calories": 240, use `number`
       * For a schema.org field defined as "foundingDate": "1991-05-01", use `datetime`

For more information, see [`FieldType`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.schemas#fieldtype).

     * `PATH_TO_THE_SCHEMA_ORG_FIELD`: the path to a single field in the schema.org field that needs to be accessed. It is specified using dot separators after each nested level. You must specify the complete path needed to access the required field. For example, if a field `ratingValue` is nested in the `aggregateRating` field, you can specify the path as `_root.aggregateRating.ratingValue`.




After you update the website schema, the website is reindexed automatically. This is a long-running operation that can take several hours.

## What's next

Use the indexed metadata for the following:

  * [Serving controls](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls), such as boost, bury, and filter
  * Surfacing as [facets](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-facets) in search results
  * [Filter search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search)
  * [Boost search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
