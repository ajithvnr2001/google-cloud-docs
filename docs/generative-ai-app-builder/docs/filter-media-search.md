---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-media-search/
title: Filter media search \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:58.021764+00:00
---

# Filter media search  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-media-search/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Filter media search Stay organized with collections  Save and categorize content based on your preferences. 

If you have a media search app, you can use metadata to filter your search queries. This page explains how use metadata fields to restrict your search to a specific set of documents.

## Before you begin

Make sure you have created a media app and data store and ingested data. For more information, see [Create a media data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-media) and [Create a media app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media).

### Example documents

Review these example media documents. You can refer back to them as you read through this page.
    
    
    {"id":"172851","schemaId":"default_schema","jsonData":"{\"title\":\"Avatar: Creating the World of Pandora (2010)\",\"categories\":[\"Documentary\"],\"uri\":\"http://mytestdomain.movie/content/172851\",\"available_time\":\"2023-01-01T00:00:00Z\",\"media_type\":\"movie\"}"}
    {"id":"243308","schemaId":"default_schema","jsonData":"{\"title\":\"Capturing Avatar (2010)\",\"categories\":[\"Documentary\"],\"uri\":\"http://mytestdomain.movie/content/243308\",\"available_time\":\"2023-01-01T00:00:00Z\",\"media_type\":\"movie\"}"}
    {"id":"280218","schemaId":"default_schema","jsonData":"{\"title\":\"Avatar: The Way of Water (2022)\",\"categories\":[\"Action\",\"Adventure\",\"Sci-Fi\"],\"uri\":\"http://mytestdomain.movie/content/280218\",\"available_time\":\"2023-01-01T00:00:00Z\",\"media_type\":\"movie\"}"}
    {"id":"72998","schemaId":"default_schema","jsonData":"{\"title\":\"Avatar (2009)\",\"categories\":[\"Action\",\"Adventure\",\"Sci-Fi\",\"IMAX\"],\"uri\":\"http://mytestdomain.movie/content/72998\",\"available_time\":\"2023-01-01T00:00:00Z\",\"media_type\":\"movie\"}"}
    

### Filter expression syntax

Make sure you understand the filter expression syntax that you'll use to define your search filter. The filter expression syntax can be summarized by the following [Extended Backus–Naur form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form#:%7E:text=In%20compute):
    
    
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
        # A simple expression applying to a numerical field. Function "IN" returns true
        # if a field value is within the range. By default, lower_bound is inclusive and
        # upper_bound is exclusive.
        | **numerical_field** , ":", "IN", "(", **lower_bound** , ",", **upper_bound** , ")"
        # A simple expression that applies to a numerical field and compares with a double value.
        | **numerical_field** , **comparison** , double;
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
      **datetime_field** = field of datetime data type - for example available_time;
      **literal_iso_8601_datetime_format** = either a double quoted string representing ISO 8601 datetime or a numerical field representing microseconds from unix epoch.

## Filter media search

To filter media search using metadata, follow these steps:

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Determine the document field or fields that you want to filter on. For example, for the documents in Before you begin, you could use the `categories` field as a filter.

You can only use indexable fields in filter expressions. To determine if a field is indexable, do the following:

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. In the **Name** column, click the data store.

     4. Click the **Schema** tab to view the schema for your data store. If **Indexable** for the field is:

        * Selected check_circle, then that field is ready to be filtered on for search; skip step 3.

        * Not selected cancel, then follow step 3 to enable the field for indexing.

        * Not available noise_control_off, then the field can't be indexed.

  3. To make a field, such as the `categories` field, filterable, do the following:

     1. In the Google Cloud console, go to the **AI Applications** page, and in the navigation menu, click **Apps**.

[Go to the Apps page](https://console.cloud.google.com/gen-app-builder/engines)

     2. Click your media search app.

     3. In the navigation menu, click **Data**.

     4. Click the **Schema** tab. This tab shows current field settings.

     5. Click **Edit**.

     6. If it's not already selected, select the **Indexable** checkbox in the **categories** row, and then click **Save**.

     7. Wait six hours to allow time for your schema edit to propagate. After six hours, you can proceed to the following step.

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
     * `FILTER`: a text field for filtering your search using a filter expression.

For example, suppose you want to search through the movies in the Before you begin section, and you want search results only for movies that: (1) Contain the word "avatar", and (2) are in the "Documentary" category. You would do that by including the following statements with your call:
    
    "query": "avatar",
    "filter": "categories: ANY(\"Documentary\")"
    

For more information, see the [`search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) method.

Click for an example response.

If you perform a search like the one in the preceding procedure, you can expect to get a response similar to the following. Notice that the response includes only the Avatar documentaries.
    
    {
      "results": [
        {
          "id": "243308",
          "document": {
            "name": "projects/431678329718/locations/global/collections/default_collection/dataStores/rdds3_1698205785399/branches/0/documents/243308",
            "id": "243308",
            "structData": {
              "categories": [
                "Documentary"
              ],
              "title": "Capturing Avatar (2010)",
              "uri": "http://mytestdomain.movie/content/243308",
              "media_type": "movie"
            }
          }
        },
        {
          "id": "172851",
          "document": {
            "name": "projects/431678329718/locations/global/collections/default_collection/dataStores/rdds3_1698205785399/branches/0/documents/172851",
            "id": "172851",
            "structData": {
              "categories": [
                "Documentary"
              ],
              "uri": "http://mytestdomain.movie/content/172851",
              "media_type": "movie",
              "title": "Avatar: Creating the World of Pandora (2010)"
            }
          }
        }
      ],
      "totalSize": 2,
      "attributionToken": "XfBcCgwIvIzJqwYQ2_qNxwMSJDY1NzEzNmY1LTAwMDAtMmFhMy05YWU3LTE0MjIzYmIwOGVkMiIFTUVESUEqII6-nRXFy_MXnIaOIsLwnhXUsp0VpovvF6OAlyKiho4i",
      "guidedSearchResult": {},
      "summary": {}
    }




## Filter for available documents

If you want your search results to return only available documents, you need to include a filter for this in your queries. Available documents are those where the `available_time` is in the past and the `expire_time` is not specified or is set to a future date.

Filter to return only documents that are currently available:
    
    
      available_time <= \"DATE_TIME\" AND expire_time > \"DATE_TIME\"
    

Replace `DATE_TIME` with today's date—for example, `2025-04-21` or `2025-04-21T00:00:00Z`.

## Filters for ratings, people, and organizations

The filter syntax for media ratings, persons, and organizations is unique and doesn't follow the patterns above. Use the following examples and copyable filter snippets to create filters for ratings, people, and organizations.

The filter differs depending on whether you're using the Google predefined schema or your own custom schema.

### Filters for ratings, people, and organizations (Google predefined schema)

Syntax and examples for the rating, person, and organization filters are as follows:

  * **Filter on ratings:** filter on ratings from a given source.
        
        rating(RATING_SOURCE, aggregate_ratings.rating_score) OPERATOR RATING_SCORE
        

Replace the following:

    * `RATING_SOURCE`: the source for the rating. For a predefined schema, this is a value in the `aggregate_ratings.rating_source` field.

    * `OPERATOR`: one of the comparison operators, `<=` , `<` , `>=` , `>` , or `=`

    * `RATING_SCORE`: a rating value in the [1,5] range. For a predefined schema, this is a value in the `aggregate_ratings.rating_score` field.

Example: This filter restricts the search to movies with IMDB ratings greater than 2½ stars. The value within the parentheses resolves to the value of the IMDB rating:
    
    "filter": "rating(imdb, aggregate_ratings.rating_score) > 2.5"
    

  * **Filter people:** filter on a peoples' names for given role.
        
        person(PERSONS_ROLE, persons.name): ANY NAME_STRING
        

Replace the following:

    * `PERSONS_ROLE`: For a predefined schema, this is a value in the `persons.role` field (`director`, `actor`, `player`, `team`, `league`, `editor`, `author`, `character`, `contributor`, `creator`, `editor`, `funder`, `producer`, `provider`, `publisher`, `sponsor`, `translator`, `music-by`, `channel`, or `custom-role`).

    * `NAME_STRING`: One or more names of people with the role specified. For curl commands, such as in Step 4, the double quotes need to be escaped with the backslash character.

Example: This filter restricts the search to movies where one of the actors is Brad Pitt or Kate Winslet.
    
    filter: "person(actor, persons.name): ANY(\"Brad Pitt\", \"Kate Winslet\")"
    

  * **Filter organizations:** filter on an organization name for given role.
        
        org(ORG_ROLE, organization.name): ANY NAME_STRING
        

Replace the following:

    * `ORG_ROLE`: For a predefined schema, this is a value in the `organizations.role` field (`director`, `actor`, `player`, `team`, `league`, `editor`, `author`, `character`, `contributor`, `creator`, `editor`, `funder`, `producer`, `provider`, `publisher`, `sponsor`, `translator`, `music-by`, `channel`, or `custom-role`).

    * `NAME_STRING`: One or more names of organizations with the role specified. For curl commands, such as in Step 4, the double quotes need to be escaped with the backslash character.

This example restricts the search to movies where the production organization is Walt Disney Studios:
    
    filter: "org(producer, organizations.name): ANY(\"Walt Disney Studios\")"
    




### Filters for ratings, people, and organizations (custom schema)

If you use a custom schema, review the Google predefined schema section, and then the examples in this section. For the rating, person, and organization filters to work in a custom schema, the property mappings must be set correctly. For information about property mappings, see [Custom schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents#custom-schema).

Filter | Properties to map  
---|---  
rating | `media_aggregated_rating`  
`media_aggregated_rating_score`  
`media_aggregated_rating_source`  
person | `media_person`  
`media_person_name`  
`media_person_role`  
org | `media_organization`  
`media_organization_name`  
`media_organization_role`  
  
**Example of a ratings filter for a custom schema**

This filter searches movies that have a 5-star rating from Rotten Tomatoes:
    
    
    "filter": "rating(rotten_tomatoes, custom_rating.star_score) = 5"
    

The `rotten_tomatoes` is a value in the field mapped to `media_aggregated_rating_source`. The `custom_rating.star_score` is the field mapped to the `media_aggregated_rating.media_aggregated_rating_score` key property.

**Example of an org filter for a custom schema**

This filter searches for movies where the music was by the London Symphony Orchestra or the Hollywood Studio Symphony.
    
    
    "filter: org(music-by, company.id): ANY (\"London Symphony Orchestra\", \"Hollywood Studio Symphony\" )
    

The `company.id` is the name of the field mapped to the `media_organization_name` property. And, the `music-by` is a value in the company record field that maps to `media_organization_role`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
