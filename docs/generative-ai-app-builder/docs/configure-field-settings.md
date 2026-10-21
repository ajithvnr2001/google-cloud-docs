---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings/
title: Configure field settings \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:04.346599+00:00
---

# Configure field settings  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Configure field settings Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure the schema fields to set up an app for structured data, for unstructured data with metadata, or for website data with custom, structured attributes.

Field settings help determine how Agent Search uses fields in its results. You can use the **Schema** tab in the Google Cloud console to configure field settings.

Configuring field settings is available only for apps with data stores containing either structured data or unstructured data with metadata.

## Field settings

The following field settings are available for many field types in your search or recommendations data, but not for all data types. A schema contains multiple field settings for individual fields, and the next table contains settings which can be applied to a field within a schema. Using structured data is highly recommended for these field settings:

Setting | Definition | Purpose | Use case example  
---|---|---|---  
**Indexable** | Setting fields to indexable allows for operations like filtering, boosting, and faceting on structured fields within a document. Fields of type `Object` can't be set to `Indexable`. | Marking a field as `Indexable` allows quicker lookups. Note that marking a field as `Indexable` increases the size of the search index and can slow down indexing. | In a hotel data store, you can set a field, such as `hotel_chain`, as indexable. This lets you apply ranking, filtering, and boosting operations on `hotel_chain`. For example, you can apply a filter so that the search will turn up only search results containing the filtered hotel chain.  
**Searchable** |  Fields that are most likely to be related to searches are designated as `Searchable`. A field can be searchable without being indexable or retrievable. Only fields with text values can be marked searchable. Thus, a numeric price field can be indexable (for filtering or faceting) but can't be searchable as full text. |  Setting a field to **Searchable** improves recall for that field in search queries, allowing users to find content, such as web pages, by querying the text within these fields. Marking a field as searchable allows ranking to be applied. Consequently, marking an excessive number of fields as searchable can negatively affect search precision by oversaturating the ranking algorithm and returning too many results. This can lead to irrelevant search returns. You can apply a relative weighting to searchable fields; however, because of robust defaults, this is rarely necessary. See Weight searchable fields below. |  An internet service provider's support ticket system stores each ticket as a structured document. If these documents contain Searchable text fields, such as `issue_description` or `resolution_notes`, a support agent can perform a query related to the content in those fields, such as _how to fix slow internet speeds after modem reset._ The system would then surface the documents that contain any of those search terms, including _modem_ , _internet_ , _speed_ , in either one or both `issue_description` or `resolution_notes` fields.  
**Prefix matchable**  
(Preview) | Allows prefix matching text fields using the `STARTS_WITH` operator in filter expressions. Only fields of type `String` or `String Array` can be set to Prefix matchable. For more information, see Make fields available for prefix and partial matching below. | Setting a field to prefix matchable enables the search engine to match query strings that are prefixes of the field's value. This is particularly useful for matching hierarchical identifiers, paths, or codes where the beginning of the string is known. Prefix matching is limited to the first 12 characters of the normalized field value and increases the size of the search index. You can't set more than 10 fields as prefix matchable. |  You have a field, `ticket_id`, that uses a format like `<country-code><city-code><number>`. Examples include `UKLON100`, `UKMAN100`, `UKMAN101`, and `USNY200`. To find all tickets from Manchester (UK), you can set the `ticket_id` field as prefix matchable and then use the filter `ticket_id: STARTS_WITH("UKMAN")`, which returns `UKMAN100` and `UKMAN101`.  
**Partially matchable**  
(Preview) |  Allows partial string matching on text fields using the `CONTAINS` operator in filter expressions. Only fields of type `String` or `String Array` can be set to partially matchable. For more information, see Make fields available for prefix and partial matching below. |  Setting a field to partially matchable enables token-based matching within a field, allowing users to find content when only a part of the field value is known. The search engine matches query tokens against tokens in the field value, regardless of their order. Note that marking a field as partially matchable increases the size of the search index. You can't set more than 10 fields as partially matchable.  |  You want to filter for regions in Europe. The `region` names include `Central Europe` and `Eastern Europe`. If your filter is `region: ANY("Europe")`, you won't get any matches. However, if the `region` field is set as partially matchable, you can filter with `region: CONTAINS("Europe")` and get matches for `Central Europe` and `Eastern Europe`.   
**Dynamic facetable** | Provides context-aware filters to better target searches for users. Setting a field as `Dynamic Facetable` allows the system to automatically generate interactive filters (facets) based on the unique values present in the field. | Setting a field to `Dynamic facetable` enables users to dynamically refine search results by selecting categories or attributes directly derived from your ingested data, without having to manually pre-define every possible filter option. This allows the user to narrow down their search to highly specific web content.  
Use **Dynamic Facetable** with **Searchable** to achieve better results, which improves both the recall of your search and the quality of the facets offered to the user.  | Pages in an internal corporate knowledge base, such as HR policies, are ingested with data like `department`, `document_type`, or `last_modified_date`. If these fields are tagged as `dynamic facetable`, an employee search for a term like _expense reimbursement_ dynamically generates interactive filters based on the relevant results found. In such case, the web interface could display facets for **Department: Finance, Travel** , **Document Type: Policy, FAQ** , or **Last Modified Date: This Quarter, Last Year**.  
**Retrievable** | When a search query hits matching content, the search engine can pull the values of retrievable fields to display or for use in the application, meaning that information from the original document is displayed as part of the search results. Key fields (unique identifiers for documents) are set up as retrievable.  | Retrievable fields provide search context by distinguishing fields whose values can be displayed from those that are only to be used in the search logic but whose raw values are not meant to be shown to the end-user. | For a product search on a merchant site, `product_id`, `name`, `price`, and an `image_url` are typical fields that you want to set as retrievable. On the other hand, the `internal_tracking_code` can be indexed and filterable for administrative purposes only, but not retrievable in public search results.  
**Completable** | Allows a field's contents to used for search query suggestions. For more information, see [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete). | This setting enables values within that field to be used for providing real-time query suggestions as users type. This feature helps guide your users to relevant content and accelerates the search process. Certain factors such as use of natural language filtering can impact this performance. | If the `completable` field is set for `product_name`, `brand`, and `category`, when the user types _Tech,_ the autocomplete suggestions can show: 

  * **TechCo** (from the `brand` field)
  * **TechCo** UltraBook X1 (from the `product_name` field)
  * **Technology** GameMaster Pro (another product from the `category` field)

  
**Filterable** | Allows recommendations to use a field to filter recommended results, determining which search results your users see. For information about filtering recommendations, see [Filter recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations). | Setting a field to `Filterable` helps customize recommendations for users. Note that [filtering limits](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations#filter-limits) apply. | A filter setting by language and drama could look like: `language_code: ANY("en", "fr") OR categories: ANY("drama")`.  
  
## Differences between commonly used settings

There are key differences between the indexable, searchable, and retrievable field settings. The table summarizes these differences.

Feature | Indexable | Searchable | Retrievable  
---|---|---|---  
**Primary Role** | Makes field content available to search engine  | Allows full-text querying against field content  | Allows field's value to be returned in search results   
**Analysis** | Content is processed and put into an index.  | Typically undergoes extensive lexical analysis.  | Value is stored as-is for display.   
**Can it be...** |  |  |   
...Searchable?  | Yes (often a prerequisite)  | N/A  | Not necessarily (can be retrievable without being searchable)   
...Retrievable?  | Not necessarily  | Not necessarily  | N/A   
...Filterable/Sortable/Facetable?  | Yes (generally a prerequisite for these too)  | Not directly; these are separate attributes often built on an indexable field.  | Not directly; these attributes relate to how the field is indexed and queried, not just displayed.   
  
In practice, many fields that are crucial for user experience (such as titles, descriptions, and identifying information) are often set to be `indexable`, `searchable`, and `retrievable`.

**Note:** The exact terminology and behavior can sometimes vary slightly between different search engine technologies (such as Elasticsearch, Apache Solr, Azure AI Search, Google Cloud Search), but the core concepts remain largely the same.

## Limitations

Field settings have the following limitations:

  * You can configure up to 50 fields as indexable, searchable, retrievable, or dynamic facetable.
  * To configure a field as dynamic facetable, it must first be configured as indexable.
  * Changing the indexable setting requires re-indexing the data, which can take hours, especially for large data stores.



If you are configuring fields for a media search app and want detailed information about the fields in the schema, see [About media documents and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents).

## Update field settings

To update field settings:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app that you want to edit.

  3. Click **Data**.

  4. Click the **Schema** tab. This tab shows current field settings.

You won't see the **Schema** tab if your data store contains [basic website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#websites) or [unstructured data without metadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#unstructured-data).

  5. Click **Edit**.

  6. Select or clear field settings that you need to update. Some field settings are not supported. For example, numerical fields cannot be set to **Searchable**.

  7. Click **Save** to apply your changes.




## Weight searchable fields (Preview)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you mark a field searchable, you can specify a weight to indicate its relative importance in search results. Most situations don't require you to specify weights for individual fields because the default weights work well.

However, adjusting weights can be necessary in a few situations, for example:

  * You're migrating data from an existing search platform that already uses weighted fields.

  * When default weights aren't providing satisfactory search results. Specifically, this can happen when you have many searchable fields and some are markedly more important than others.

Perhaps, the summary is the most important field for searches and so you want to prioritize that text.

Or, the schema has a field containing highly relevant keywords that are excellent predictors for search results, but, because this field is much shorter than others, its influence is often overshadowed by longer fields. Increasing its weight ensures it has the intended impact.




### Weight levels

Weights are banded into the following levels:

Field importance | Explanation  
---|---  
**Very low** | A low value that the system still considers when it combines scores from all fields. If you want even less weight so that the effect is negligible, don't mark the field searchable.  
**Low** | A weight that is lower than the default.  
**Default** | The standard weight for searchable fields. This weight provides reasonably good performance for most cases.  
**High** | A weight that is noticeably higher than the default.  
**Very high** | A dominating weight. Typically, you reserve this for, at most, one field.  
  
### Schema update and reindexing

Adding weights to searchable fields requires a schema update and subsequent re-indexing of the data in the data store. Updating the schema takes hours, and there isn't a reliable indicator to tell you when indexing is completed, so you need to overestimate the indexing time.

### Set weight levels on fields

The task of setting weight levels for fields can be tedious because you should make only small changes and carefully review search results afterward to check for unintended consequences. After each change, you must wait for re-indexing to complete before you can evaluate the impact of the change.

**Note:** You can't apply a weight to a field that's a key property, such as `title` or `description`. Agent Search already applies a higher weighting for fields marked as key properties.

You can configure search field weighting only through the API. This feature is not available in the Google Cloud console.

To set weights, you need to update the schema for the data store through the API [`projects.locations.dataStores.schemas.patch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.schemas/patch) method.

  1. If you don't have your schema already, follow the instructions to get your schema in [View a schema definition](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-schema-definition).

  2. Follow the instructions to [update the schema programmatically](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas). Add weights to one or more searchable fields, as in these examples:
         
         "summary": {
            "type": "string",
            "searchable": true,
            "weight": "high"
          },
          "uri": {
            "type": "string",
            "searchable": true,
            "weight": "low"
          },
         

In this example, the `summary` field is set to a higher weight than normal and the `uri` field to a lower weight. If you want to return a weight to the default value, set it to `default`.

Allowed values for the weight parameter are:

     * `very_low`
     * `low`
     * `default`
     * `high`
     * `very_high`

#### Example command and result
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/dataStores/my-data-store/schemas/default_schema" \
    -d '{
    "structSchema": { "$schema": "https://json-schema.org/draft/2020-12/schema", "properties": { "amenities": { "items": { "completable": true, "dynamicFacetable": true, "indexable": true, "retrievable": true, "searchable": true, "type": "string", "weight": "high" }, "type": "array" }, "available_date": { "indexable": true, "retrievable": true, "type": "datetime" }, "id": { "dynamicFacetable": false, "indexable": true, "retrievable": true, "type": "number" }, "location": { "indexable": true, "retrievable": true, "type": "geolocation" }, "non_smoking": { "dynamicFacetable": true, "indexable": true, "type": "boolean" }, "price_per_night": { "indexable": true, "retrievable": true, "type": "number" }, "rating": { "dynamicFacetable": true, "indexable": true, "retrievable": true, "type": "number" }, "room_types": { "items": { "dynamicFacetable": true, "indexable": true, "retrievable": true, "searchable": true, "type": "string", "weight": "low" }, "type": "array" }, "title": { "keyPropertyMapping": "title", "retrievable": true, "type": "string" } }, "type": "object" }
    }'
    
    
    * * *
    
    
    {
    "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/schemas/default_schema/operations/update-schema-123456",
    "metadata": {
    "@type": "type.googleapis.com/google.cloud.discoveryengine.v1beta.UpdateSchemaMetadata"
    }
    }
    

In this example, the `amentities` field is given a higher than normal weighting and the `room_types` field is given a lower weighting.

  3. Wait for reindexing to complete and test the search behavior.




## Make fields available for prefix and partial matching (Preview)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For fields of type `string`, you can edit the schema to make the fields available for prefix matching or partial matching. This lets you use `STARTS_WITH` or `CONTAINS` in filter expressions.

### Schema update and reindexing

Making fields available for prefix or partial matching requires a schema update and subsequent re-indexing of the data in the data store. Updating the schema takes hours, and there isn't a reliable indicator to tell you when indexing is completed, so you need to overestimate the indexing time.

### Update schema for prefix and partial matching

**Note:** You can configure prefix and partial matching only through the API. This feature is not available in the Google Cloud console.

To specify fields as available for prefix matching or partial matching, you need to update the schema for the data store through the API [`projects.locations.dataStores.schemas.patch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.schemas/patch) method.

  1. If you don't have your schema already, follow the instructions to get your schema in [View a schema definition](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-schema-definition).

  2. Follow the instructions to [update the schema programmatically](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas). Set the matchable parameters to `true` in the schema, as in these examples:
         
         "zone": {
            "type": "string",
            "searchable": true,
            "prefixMatchable": true
          },
          "region": {
            "type": "string",
            "searchable": true,
            "partialMatchable": true
          },
          "model": {
            "type": "string",
            "searchable": true,
            "prefixMatchable": true,
            "partialMatchable": true
          },
         

In this example, the `zone` field is set to be prefix matchable. Up to 12 characters, case insensitive, can be used in the filter expression to match the field value. The `region` field is set to be partially matchable.

#### Example command and result
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/dataStores/my-data-store/schemas/default_schema" \
         -d '{
           "structSchema": { "$schema": "https://json-schema.org/draft/2020-12/schema",
           "properties": { "amenities": { "items": { "completable":
           true,"partialMatchable": true, "dynamicFacetable": true, "indexable": true,
           "retrievable": true, "searchable": true, "type": "string" },
           "type": "array" }, "available_date": { "indexable": true, "retrievable": true,
           "type": "datetime" }, "id": { "dynamicFacetable": false, "indexable": true,
           "retrievable": true, "type": "number" }, "location": { "indexable": true,
           "retrievable": true, "type": "geolocation" }, "non_smoking": {
           "dynamicFacetable": true, "indexable": true, "type": "boolean" },
           "price_per_night": { "indexable": true, "retrievable": true, "type": "number"
           }, "rating": { "dynamicFacetable": true, "indexable": true, "retrievable":
           true, "type": "number" }, "room_types": { "items": { "dynamicFacetable": true,
           "prefixMatchable": true, "indexable": true, "retrievable": true,
           "searchable": true, "type": "string" }, "type": "array" }, "title": {
           "keyPropertyMapping": "title", "retrievable": true, "type": "string" } },
           "type": "object" } }'
         
         
         * * *
         
         
         {
         "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/schemas/default_schema/operations/update-schema-123456",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.discoveryengine.v1beta.UpdateSchemaMetadata"
           }
         }
         

In this example, the `amentities` field is partially matchable. This means that `CONTAINS("outdoor pool")` matches an amenity with a value of `outdoor swimming pool`. The `room_type` field is prefix matchable, which means that a filter of `STARTS_WITH("lux")` matches with a room type of `Luxury Room` but not `Deluxe`).

  3. Wait for reindexing to complete.




### Details about prefix matching

Prefix matching in Agent Search lets you filter results based on whether a field's value starts with a specific string. This capability is powered by the `STARTS_WITH` operator and requires that the target text field be configured as `prefixMatchable` in the schema.

#### Normalization and matching logic

To optimize performance and ensure consistency, the system applies a specific normalization process to both the **field value** (during indexing) and the **query string** (during search).

  1. **Lowercasing** : All characters are converted to lowercase. This makes the matching case-insensitive.

  2. **12-character truncation** : The system only considers the first **12 characters** of the string. Any characters beyond this limit are ignored for prefix matching purposes.




#### How it works

At indexing time, for a field marked as `prefixMatchable`, the system generates prefix tokens for the first 12 characters. For a value like `asia-south1-c`, the index stores tokens for `a`, `as`, `asi`, `asia`, `asia-`, and so on, up to the 12th character (`asia-south1-`).

At query time, the string provided to the `STARTS_WITH` operator is also lowercased and truncated to 12 characters. The query is then matched against the stored prefix tokens.

#### Examples

The following examples demonstrate how the 12-character normalization affects search results:

  * **Broad matches** : `STARTS_WITH("A")` matches any value starting with "a" (case-insensitive), such as `asia`, `australia`, or `africa`.

  * **Partial prefixes** : `STARTS_WITH("asia-south")` matches both `asia-south1-a` and `asia-southeast1-b` because both start with the specified 10-character string.

  * **Truncation behavior** : Because only the first 12 characters are matched, `STARTS_WITH("asia-south1-a")` matches a field value of `asia-south1-c`. This occurs because both strings are normalized to the same 12-character prefix: `asia-south1-`.




### Details about partial matching

Partial matching in Agent Search lets you filter results based on whether a field's value contains specific words or tokens. This capability is powered by the `CONTAINS` operator and requires that the target text field be configured as `partialMatchable` in the schema.

#### Normalization and tokenization logic

The Agent Search normalizes and tokenizes both the **field value** (during indexing) and the **query string** (during search):

  * **Lowercasing** : Agent Search converts the characters to lowercase. This makes the matching case-insensitive.

  * **Tokenization** : Agent Search splits the string into individual tokens (words) using spaces and other characters as delimiters.

    * **Standard delimiters** : Spaces and common punctuation act as delimiters; these include hyphens (`-`), slashes (`/`), commas (`,`), periods (`.`), asterisks (`*`), curly brackets (`{ }`), square brackets (`[ ]`), round brackets (`( )`), and apostrophes (`'`).

    * **Non-delimiters** : Ampersand (`&`) and underscore (`_`) don't act as delimiters. The system treats characters joined by these symbols as a single token.

    * **Email delimiter (`@`)**: The `@` symbol acts as a special delimiter to assist in recognizing email addresses. The system generates tokens for the individual components as well as combined forms. For example, it tokenizes `support+tier1@example.com` to `support`, `tier1`, `example`, `com`, `support+tier1@example.com`, and `support@example.com`.




#### How it works

At indexing time, for a field marked as `partialMatchable`, the system normalizes and tokenizes the field value and stores the resulting tokens in the index. For example, it tokenizes a field value of `25-meter, outdoor, swimming pool` to `[25, meter, outdoor, swimming, pool]`.

At query time, the string provided to the `CONTAINS` operator undergoes the same normalization and tokenization process. The search engine then verifies that all resulting query tokens match the stored tokens for the field. The order of the tokens has no effect.

#### Examples

The following examples demonstrate how tokenization affects partial matching results:

  * **Basic token matching** : If the field value is `25-meter, outdoor, swimming pool`, a filter of `CONTAINS("Outdoor pool")` matches. The system tokenizes the query to `[outdoor, pool]`, both of which exist in the field's tokens.

  * **Order independence** : A filter of `CONTAINS("pool outdoor")` also matches the field value `25-meter, outdoor, swimming pool` because the system checks for the presence of each token independently of their order.

  * **Email address matching** : If a field stores the email `support+tier1@example.com`, filters like `CONTAINS("support")`, `CONTAINS("example.com")`, or `CONTAINS("support@example.com")` all successfully match due to the special tokenization of the `@` symbol.




## What's next

  * [Update a schema for structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas)
  * [Configure search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes)
  * [Preview search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
