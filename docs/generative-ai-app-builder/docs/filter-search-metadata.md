---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata/
title: Filter custom search for structured or unstructured data \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:30.454925+00:00
---

# Filter custom search for structured or unstructured data  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Filter custom search for structured or unstructured data Stay organized with collections  Save and categorize content based on your preferences. 

If you have a search app that uses structured data or unstructured data with metadata, you can use the metadata to filter your search queries. This page explains how to use metadata fields to restrict your search to a specific set of documents.

**Note:** Other approaches to filters for structured data are: 

  * Have natural-language understanding create filters from your users' queries. For more information, see [Filter with natural language understanding](https://docs.cloud.google.com/generative-ai-app-builder/docs/natural-language-queries). 
  * Use document-level relevance filtering to reduce the number of results returned. For more information, see [Filter searches by document-level relevance](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance). 



To see an example of search filters metadata, run the "Search filters metadata" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/search/search_filters_metadata.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/search/search_filters_metadata.ipynb)

## Metadata example

Review this example of metadata for four PDF files (`document_1.pdf`, `document_2.pdf`, `document_3.pdf`, and `document_4.pdf`). This metadata would be in a JSON file in a Cloud Storage bucket, along with the PDF files. You can refer back to this example as you read through this page.
    
    
    {"id": "1", "structData": {"title": "Policy on accepting corrected claims", "category": ["persona_A"]}, "content": {"mimeType": "application/pdf", "uri": "gs://bucketname_87654321/data/document_1.pdf"}}
    {"id": "2", "structData": {"title": "Claims documentation and reporting guidelines for commercial members", "category": ["persona_A", "persona_B"]}, "content": {"mimeType": "application/pdf", "uri": "gs://bucketname_87654321/data/document_2.pdf"}}
    {"id": "3", "structData": {"title": "Claims guidelines for bundled services and supplies for commercial members", "category": ["persona_B", "persona_C"]}, "content": {"mimeType": "application/pdf", "uri": "gs://bucketname_87654321/data/document_3.pdf"}}
    {"id": "4", "structData": {"title": "Advantage claims submission guidelines", "category": ["persona_A", "persona_C"]}, "content": {"mimeType": "application/pdf", "uri": "gs://bucketname_87654321/data/document_4.pdf"}}
    

## Filter expression syntax

Make sure you understand the syntax of the filter expression that you'll use to define your search filter. The filter expression syntax can be summarized by the following [Extended Backus–Naur form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form#:%7E:text=In%20compute):

**Note:** The `CONTAINS` and `STARTS_WITH` operators are in Preview. For more information, see [Make fields available for prefix and partial matching (Preview)](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings#update_schema_for_prefix_and_partial_matching).
    
    
      # A single expression or multiple expressions that are joined by "AND" or "OR".
      **filter** = **expression** , { " AND " | "OR", **expression** };
      # Expressions can be prefixed with "-" or "NOT" to express a negation.
      **expression** = [ "-" | "NOT " ],
        # A parenthetical expression.
        | "(", expression, ")"
        # A simple expression applying to a text field.
        # Function "ANY" returns true if the field exactly matches any of the literals.
        | **text_field** , ":", "ANY", "(", **literal** , { ",", **literal** }, ")"
        # A simple expression applying to any indexable field.
        # Preview: Function "EXISTS" returns true if the field is not NULL, empty, or containing the default value.
        | **text_field** , ":", "EXISTS"
        | **numerical_field** , ":", "EXISTS"
        # Function "CONTAINS" returns true if the field contains the tokens in any of the literals.
        # This is a partial match, not an exact match.
        | **text_field** , ":", "CONTAINS", "(", **literal** , ")"
        # Function "STARTS_WITH" returns true if the field begins with the same characters
        # as in any of the literals. The prefix matches up to 12 characters.
        | **text_field** , ":", "STARTS_WITH", "(", **literal** , ")"
        # A simple expression applying to a numerical field. Function "IN" returns true
        # if a field value is within the range. By default, lower_bound is inclusive and
        # upper_bound is exclusive.
        | **numerical_field** , ":", "IN", "(", **lower_bound** , ",", **upper_bound** , ")"
        # A simple expression that applies to a numerical field and compares with a double value.
        | **numerical_field** , **comparison** , double
        # An expression that applies to a geolocation field with text/street/postal address.
        |  **geolocation_field** , ":", "GEO_DISTANCE(", literal, ",", distance_in_meters, ")"
        # An expression that applies to a geolocation field with latitude and longitude.
        | **geolocation_field** , ":", "GEO_DISTANCE(", latitude_double, ",", longitude_double, ",", distance_in_meters, ")"
        # Datetime field
        | **datetime_field** , **comparison** , literal_iso_8601_datetime_format);
      # A lower_bound is either a double or "*", which represents negative infinity.
      # Explicitly specify inclusive bound with the character 'i' or exclusive bound
      # with the character 'e'.
      **lower_bound** = ( double, [ "e" | "i" ] ) | "*";
      # An upper_bound is either a double or "*", which represents infinity.
      # Explicitly specify inclusive bound with the character 'i' or exclusive bound
      # with the character 'e'.
      **upper_bound** = ( double, [ "e" | "i" ] ) | "*";
      # Supported comparison operators.
      **comparison** = "<=" | "<" | ">=" | ">" | "=";
      # A literal is any double quoted string. You must escape backslash (\) and
      # quote (") characters.
      **literal** = double quoted string;
      **text_field** = text field - for example, category;
      **numerical_field** = numerical field - for example, score;
      **geolocation_field** = field of geolocation data type - for example home_address, location;
      **datetime_field** = field of datetime data type - for example creation_date, expires_on;
      **literal_iso_8601_datetime_format** = either a double quoted string representing ISO 8601 datetime or a numerical field representing microseconds from unix epoch.

## Key properties that support filtering

Even if a key property field is set to indexable, it might not support filtering, facets, and sorting. For example, you can't filter on a field that maps to the key property `title`.

The following key property fields can be used for filtering, facets, and reordering.

Key property fields for custom search that can be used in filters, facets, and sorting:

  * `CATEGORIES` (`category`)
  * `CREATE_TIME` (`create_time`)
  * `HASHTAGS` (`hashtag`)
  * `LANGUAGE_CODE` (`language_code`)
  * `UPDATE_TIME` (`update_time`)
  * `URI` (`uri`)



Key property fields for media search that can be used in filters, facets, and sorting:

  * `MEDIA_AVAILABLE_TIME` (`media_available_time`)
  * `MEDIA_CONTENT_INDEX` (`media_content_index`)
  * `MEDIA_CONTENT_RATING` (`media_content_rating`)
  * `MEDIA_COUNTRY_OF_ORIGIN` (`media_country_of_origin`)
  * `MEDIA_DURATION` (`media_duration`)
  * `MEDIA_EXPIRE_TIME` (`media_expire_time`)
  * `MEDIA_FILTER_TAGS` (`media_filter_tag`)
  * `MEDIA_HASH_TAGS` (`media_hash_tag`)
  * `MEDIA_IN_LANGUAGES` (`media_in_language`)
  * `MEDIA_LIVE_EVENT_END_TIME` (`media_live_event_end_time`)
  * `MEDIA_LIVE_EVENT_START_TIME` (`media_live_event_start_time`)
  * `MEDIA_PRODUCTION_YEAR` (`media_production_year`)
  * `MEDIA_TYPE` (`media_type`)



## Before you begin

Make sure you have created an app and ingested structured data or unstructured data with metadata. For more information, see [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es).

## Search using a metadata filter

To search using a metadata filter, follow these steps:

  1. Determine the metadata field to use for filtering your search queries.

For example, for the metadata in Before you begin, you could use the `category` field as a search filter. When filtering over structured data, as in metadata example, specify the full path to the field: `structData.category`. Then, your users could filter on `persona_A`, `persona_B`, or `persona_C`, so their search is restricted to the documents associated with the persona that they're interested in.

  2. Make the metadata field indexable:

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Apps**.

[Go to the Apps page](https://console.cloud.google.com/gen-app-builder/engines)

     2. Click your search app.

     3. In the navigation menu, click **Data**.

     4. Click the **Schema** tab. This tab shows current field settings.

**Note:** The **Schema** tab appears only for data stores that contain structured data or unstructured data with metadata.
     5. Click **Edit**.

     6. Select the **Indexable** checkbox for the field that you want to make indexable.

     7. Click **Save**. For more information, see [Configure field settings](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings).

  3. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  4. Get search results.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
         "query": "QUERY",
         "filter": "FILTER"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `APP_ID`: the ID of your app.
     * `QUERY`: the query text to search.
     * `FILTER`: optional. A text field that lets you to filter on a specified set of fields, using filter expression syntax. The default value is an empty string, which means no filter is applied.

For example, say that you imported the four PDF files with metadata from Before you begin. You want to search for documents that contain the word "claims", and only query documents with a `category` value of `persona_A`. You would do that by including the following statements with your call:
    
    "query": "claims",
    "filter": "category: ANY(\"persona_A\")"
    

For more information, see the REST tab at [Get search results for an app with structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#structured-unstructured).

Click for an example response.

If you perform a search like the one in the preceding procedure, you can expect to get a response similar to the following. Notice that the response includes the three documents that have a `category` value of `persona_A`.
    
    {
    "results": [
    {
      "id": "2",
      "document": {
        "name": "projects/abcdefg/locations/global/collections/default_collection/dataStores/search_store_id/branches/0/documents/2",
        "id": "2",
        "structData": {
          "title": "Claims documentation and reporting guidelines for commercial members",
          "category": [
            "persona_A",
            "persona_B"
          ]
        },
        "derivedStructData": {
          "link": "gs://bucketname_87654321/data/document_2.pdf",
          "extractive_answers": [
            {
              "pageNumber": "1",
              "content": "lorem ipsum"
            }
          ]
        }
      }
    },
    {
      "id": "1",
      "document": {
        "name": "projects/abcdefg/locations/global/collections/default_collection/dataStores/search_store_id/branches/0/documents/1",
        "id": "1",
        "structData": {
          "title": "Policy on accepting corrected claims",
          "category": [
            "persona_A"
          ]
        },
        "derivedStructData": {
          "extractive_answers": [
            {
              "pageNumber": "2",
              "content": "lorem ipsum"
            }
          ],
          "link": "gs://bucketname_87654321/data/document_1.pdf"
        }
      }
    },
    {
      "id": "4",
      "document": {
        "name": "projects/abcdefg/locations/global/collections/default_collection/dataStores/search_store_id/branches/0/documents/4",
        "id": "4",
        "structData": {
          "title": "Advantage claims submission guidelines",
          "category": [
            "persona_A",
            "persona_C"
          ]
        },
        "derivedStructData": {
          "extractive_answers": [
            {
              "pageNumber": "47",
              "content": "lorem ipsum"
            }
          ],
          "link": "gs://bucketname_87654321/data/document_4.pdf"
        }
      }
    }
    ],
    "totalSize": 330,
    "attributionToken": "UvBRCgsI26PxpQYQs7vQZRIkNjRiYWY1MTItMDAwMC0yZWIwLTg3MTAtMTQyMjNiYzYzMWEyIgdHRU5FUklDKhSOvp0VpovvF8XL8xfC8J4V1LKdFQ",
    "guidedSearchResult": {},
    "summary": {}
    }
    




## Examples of filter expressions

The following table provides examples of filter expressions.

Filter | Only returns results for documents where:  
---|---  
`category: ANY("persona_A")` | the text field `category` is `persona_A`  
`category: EXISTS` | the text field `category` has a non-NULL value; it contains text 1  
`score: EXISTS` | the numerical field `score` has a non-NULL value; it has a value that is not zero 1  
`score: IN(*, 100.0e)` | the numerical field `score` is greater than negative infinity and less than 100.0  
`non-smoking = "true"` | the boolean `non-smoking` is true  
`pet-friendly = "false"` | the boolean `pet-friendly` is false  
`manufactured_date = "2023"` | the `manufactured date` is any time in 2023  
`manufactured_date >= "2024-04-16"` | the `manufactured_date` is on or after April 16, 2024  
`manufactured_date < "2024-04-16T12:00:00-07:00"` | the `manufactured_date` is before noon Pacific Daylight Time on April 16, 2024  
`office.location:GEO_DISTANCE("1600 Amphitheater Pkwy, Mountain View, CA, 94043", 500)` | the geolocation field `office.location` is within a 500 m distance of 1600 Amphitheater Pkwy  
`NOT office.location:GEO_DISTANCE("Palo Alto, CA", 1000)` | the geolocation field `office.location` is not within a 1 km radius of Palo Alto, California.  
`office.location:GEO_DISTANCE(34.1829, -121.293, 500)` | the geolocation field `office.location` is within a 500 m radius of latitude 34.1829 and longitude -121.293  
`category: ANY("persona_A") AND score: IN(*, 100.0e)` | `category` is `persona_A` and `score` is less than 100  
`office.location:GEO_DISTANCE("Mountain View, CA", 500) OR office.location:GEO_DISTANCE("Palo Alto, CA", 500)` | `office.location` is within a 500 m distance of either Mountain View or Palo Alto.  
`(price<175 AND pet-friendly = "true") OR (price<125 AND pet-friendly = "false")` | `price` is less than 175 and I can bring my pet, or `price` is less than 125 and I can't bring my pet  
`zone: STARTS_WITH("asia-")` | the text field `zone` begins with `asia-`, such as `asia-south1-a` or `asia-east1-c`.  
**Note:** The `STARTS_WITH` operator is in Preview. For more information, see [Make fields available for prefix and partial matching (Preview)](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings#update_schema_for_prefix_and_partial_matching).  
`region: CONTAINS("Europe")` | the text field `region` contains the token `Europe`, such as `Central Europe` or `Eastern Europe`.  
**Note:** The `CONTAINS` operator is in Preview. For more information, see [Make fields available for prefix and partial matching (Preview)](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings#update_schema_for_prefix_and_partial_matching).  
`url: CONTAINS("WWW.altostrat.com")` | this expression is the equivalent of `CONTAINS("www") AND CONTAINS("altostrat") AND CONTAINS("com")`. It matches a field value `www.altostrat.com` as well as variations such as `www.altostrat.com/help`.   
**Note:** The `CONTAINS` operator is in Preview. For more information, see [Make fields available for prefix and partial matching (Preview)](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings#update_schema_for_prefix_and_partial_matching).  
`email: CONTAINS("info@CymbalGroup.com")` | this expression is the equivalent of `CONTAINS("info") AND CONTAINS("cymbalgroup") AND CONTAINS("com") AND CONTAINS("info@cymbalgroup.com")`. Because of the special behavior of the `@` separator, this expression matches a field value of `info+sales@cymbalgroup.com` as well as the (expected) value of `info@cymbalgroup.com`.   
**Note:** The `CONTAINS` operator is in Preview. For more information, see [Make fields available for prefix and partial matching (Preview)](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings#update_schema_for_prefix_and_partial_matching).  
**Note:** If you use these filters in a curl command or a language, such as Java or C++, where double quotes are a reserved character, then you need to escape the double quotes with a backslash. Therefore, in these examples, you would replace occurrences of `"` with `\"`.

## What's next

  * To understand the impact of filters on the search quality, evaluate the search quality. For more information, see [Evaluate search quality](https://docs.cloud.google.com/generative-ai-app-builder/docs/evaluate-search-quality).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
