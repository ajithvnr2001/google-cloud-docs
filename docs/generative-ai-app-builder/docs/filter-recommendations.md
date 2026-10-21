---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations/
title: Filter recommendations \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:07.799135+00:00
---

# Filter recommendations  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Filter recommendations Stay organized with collections  Save and categorize content based on your preferences. 

If you have a recommendations app, you can use document fields to filter your recommendation results. This page explains how to use document fields to filter a recommendation to a specific set of documents. Although the examples on this page are for media recommendations, the principles shown here are the same for custom recommendations. For more information about media recommendations, see [Introduction to Agent Search for media](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media).

## Filter recommendations and data store updates

After any data store update, you'll need to wait up to 8 hours while the model retrains. This is because the model needs to know about the current values in the document metadata, as well as what fields are configured as filterable. You need to wait for document changes and schema changes to propagate. For recommendations (unlike for search), filtering is not done in real time.

**Note:** By default, retraining takes about 8 hours. However, if your business case requires a shorter training period, contact your Google account team to ask about fast model updates.

## Filters and diversification settings (Media recommendations only)

In addition to filters, an app's diversification setting also affects the results returned in a media recommendation response. The effects of filters and diversification are combined. The diversification is done first and the filtering is done second.

Combining high, rule-based diversity and category-based attribute filtering often results in empty output. This is because high diversity limits the app to returning one result for each category.

For example, you want to recommend movies based on Toy Story. You set the rule-based diversity level to high. Because the diversity level is high, although many movies might be recommended only one movie (for example, WALL·E) in the category of children's movies is returned. When the filter for children's movies is then applied, only WALL·E is returned as a recommendation.

For general information about diversity, see [Diversify media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/diversify-recommendations).

## Before you begin

Make sure you have created a recommendations app and data store. For more information, see [Create media apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media) or [Create a custom recommendations data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-recommendations).

### Example documents

Review these example media documents. You can refer back to these example documents as you read through this page.
    
    
    {"id":"1","schemaId":"default_schema","structData":{"title":"Toy Story (1995)","categories":["Adventure","Animation","Children","Comedy","Fantasy"],"uri":"http://mytestdomain.movie/content/1","available_time":"2023-01-01T00:00:00Z","media_type":"movie"}}
    {"id":"88125","schemaId":"default_schema","structData":{"title":"Harry Potter and the Deathly Hallows: Part 2 (2011)","categories":["Action","Adventure","Drama","Fantasy","Mystery","IMAX"],"uri":"http://mytestdomain.movie/content/88125","available_time":"2023-01-01T00:00:00Z","media_type":"movie"}}
    {"id":"2857","schemaId":"default_schema","structData":{"title":"Yellow Submarine (1968)","categories":["Adventure","Animation","Comedy","Fantasy","Musical"],"uri":"http://mytestdomain.movie/content/2857","available_time":"2023-01-01T00:00:00Z","media_type":"movie"}}
    {"id":"60069","schemaId":"default_schema","structData":{"title":"WALL·E (2008)","categories":["Adventure","Animation","Children","Romance","Sci-Fi"],"uri":"http://mytestdomain.movie/content/60069","available_time":"2023-01-01T00:00:00Z","media_type":"movie"}}
    

## Filter expressions

Use filter expressions to define your recommendations filters.

### Filter expressions syntax

The following [Extended Backus–Naur form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form#:%7E:text=In%20compute) summarizes the filter expression syntax that you can use to define your recommendations filters.
    
    
      # A single expression or multiple expressions that are joined by "AND" or "OR".
      **filter** = **expression** , { " AND " | "OR", **expression** };
      # An expression can be prefixed with "-" or "NOT" to express a negation.
      **expression** = [ "-" | "NOT " ],
        # A parenthesized expression
        | "(", expression, ")"
        # A simple expression applying to a textual field.
        # Function "ANY" returns true if the field contains any of the literals.
        **textual_field** , ":", "ANY", "(", **literal** , { ",", **literal** }, ")"
        # OR filter by "available"
        available, ":", "true",
      # A literal is any double-quoted string. You must escape backslash (\) and
      # quote (") characters.
      **literal** = double-quoted string;
      **textual_field** = see the tables below;

### Filter expressions restrictions

The following restrictions apply to filter expressions for recommendations:

  * The depth of embedding `AND` and `OR` operators in parentheses is limited. The logical expressions in the filter must be in [conjunctive normal form (CNF)](https://en.wikipedia.org/wiki/Conjunctive_normal_form). The most complex supported logical expression can be an `AND`-connected list of clauses that only contain `OR` operators, such as: `(... OR ... OR ...) AND (... OR ...) AND (... OR ...)`
  * Expressions can be negated with the `NOT` keyword or with `-`. This only works with `ANY()` expressions with a single argument.

  * `available` restrictions must be at the top level. They cannot be used as part of an `OR` clause or a negation (`NOT`). You can only use `available: true`. If you omit this filter, expired documents and not-yet-available documents might be returned as recommendations.

The `available` field maps to the following logic:

`datetime.now >= available_time AND datetime.now <= expire_time`

If the `expire_time` is not set, `datetime.now <= expire_time` resolves to `true`.

  * The maximum number of terms in the top-level `AND` clause is 20.

  * An `OR` clause can have up to 100 arguments that are included in `ANY()` expressions. If an `OR` clause has multiple `ANY()` expressions, their arguments all count toward this limit. For example, `categories: ANY("drama", "comedy") OR categories: ANY("adventure")` has three arguments.




### Filter expressions examples

The following table shows valid and invalid filter expression examples. It also gives the reasons why the invalid examples are invalid.

Expression | Valid | Notes  
---|---|---  
`language_code: ANY("en", "fr")` | Yes |   
`NOT language_code: ANY("en")` | Yes |   
`NOT language_code: ANY("en", "fr")` | No | Negates an `ANY()` with more than one argument.  
`language_code: ANY("en", "fr") OR categories: ANY("drama")` | Yes |   
`(language_code: ANY("en") OR language_code: ANY("fr")) AND categories: ANY("drama")` | Yes |   
`(language_code: ANY("en") AND language_code: ANY("fr")) OR categories: ANY("drama")` | No | Not in conjunctive normal form.  
`(language_code: ANY("en")) AND (available: true)` | Yes |   
`(language_code: ANY("en")) OR (available: true)` | No | Combines `available` in an `OR` expression with other conditions.  
  
The following filter expression filters for documents that are in the drama or action category, that are not in English, and that are available:
    
    
    categories: ANY("drama", "action") AND NOT language_code: ANY("en") AND available: true
    

## Filtering limits

Each filterable document field consumes some memory in each of your models. The following limits help prevent adverse effects on serving performance:

  * Up to 10 custom fields can be set as filterable in your schema.

If more than 10 custom fields are found during app training, only 10 are used.

  * Up to 100,000,000 filterable field values can be present in your schema.

You can estimate the total number of filterable field values in your schema by multiplying the number of documents in your schema by the number of filterable fields. If you exceed these limits, the following things happen:

    * You cannot set additional fields as filterable.
    * App training fails.



## Filter recommendations

To filter media recommendations, follow these steps:

  1. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  2. Determine the document field or fields that you want to filter on. For example, for the documents in Before you begin, you could use the `categories` field as a filter.

  3. To make the `categories` field filterable, do the following:

     1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

     2. Click your recommendations app.

     3. Click the **Schema** tab. This tab shows current field settings.

     4. Click **Edit**.

     5. If it's not already selected, select the **Filterable** checkbox in the **categories** row, and then click **Save**.

     6. Wait six hours to allow time for your schema edit to propagate. After six hours, you can proceed to the following step.

  4. To get a recommendation and filter on the `categories` field, run the following code at the command line:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
              "userEvent": {
                "eventType": "EVENT_TYPE",
                "userPseudoId": "USER_PSEUDO_ID",
                "documents": {
                  "id": "DOCUMENT_ID"
                }
              },
              "params": {
                "returnDocument": true,
                "attributeFilteringSyntax": true,
                "strictFiltering": true
              },
              "filter": "FILTER"
            }' \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/servingConfigs/SERVING_CONFIG_ID:recommend"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `DATA_STORE_ID`: the ID of your data store.
     * `DOCUMENT_ID`: the ID of the document that you want to preview recommendations for. Use the ID that you used for this document at the time you ingested your data.
     * `EVENT_TYPE`: the type of user event. For `eventType` values, see [UserEvent](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.userEvents#UserEvent).
     * `USER_PSEUDO_ID`: a UTF-8 encoded string, which acts as a unique pseudonymized identifier that tracks the users. It can have a maximum length of 128 characters. Google strongly recommends using this field because it improves model performance and personalization quality. You can use an HTTP cookie for this field, which uniquely identifies a visitor on a single device. Some important considerations are as follows: 

       * This identifier doesn't change when the visitor signs in or out of a website.
       * This field must not be set to the same identifier for multiple users. Otherwise, same user ID can combine event histories of different users and degrade model quality.
       * This field must not include personally identifiable information (PII).

For more information, see [`userPseudoId`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.user_pseudo_id). 

     * `SERVING_CONFIG_ID`: the ID of your serving config. Your serving config ID is the same as your engine ID, so use your engine ID here.
     * `FILTER`: a text field that lets you to filter on a specified set of fields, using filter expression syntax. The default value is an empty string, which means no filter is applied.

For example, suppose you want a recommendation for a specific media-play user event, and you want to filter the recommendation results to contain only documents that are: (1) In the Children category, and (2) Currently available. You would do that by including the following statements with your call:

     * `"eventType": "media-play"`
     * `"filter": "categories: ANY(\"Children\") AND available: true"`

For more information, see the [`recommend`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs/recommend) method.

Click for an example response.

If you make a recommendation request like the preceding one, you can expect to get a response similar to the following. Notice that the response includes the two documents that have a `categories` value of `Children` and an `availability_start_time` value that is later than the current date.
    
    {
    "results": [
      {
        "id":"1",
        "schemaId":"default_schema",
        "structData":{"title":"Toy Story (1995)","categories":["Adventure","Animation","Children","Comedy","Fantasy"],"uri":"http://mytestdomain.movie/content/1",
        "availability_start_time":"2023-01-01T00:00:00Z",
        "media_type":"movie"
        }
      },
      {
        "id":"60069",
        "schemaId":"default_schema",
        "structData":{"title":"WALL·E (2008)","categories":["Adventure","Animation","Children","Romance","Sci-Fi"],"uri":"http://mytestdomain.movie/content/60069",
        "availability_start_time":"2023-01-01T00:00:00Z",
        "media_type":"movie"
        }
      }
    ],
    "attributionToken": "ChMzMDk3NTQ4MzQxOTcxOTE0ODM1GglhZi10ZXN0LTEiDmFmLXRlc3QtMTE0NTE0KAAwBg"
    }




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
