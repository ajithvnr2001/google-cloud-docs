---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls/
title: Configure serving controls for search \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:47.988727+00:00
---

# Configure serving controls for search  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Configure serving controls for search Stay organized with collections  Save and categorize content based on your preferences. 

Serving controls (also called controls) change the default behavior of how a request is served when results are returned. Serving controls act at a data-store level.

For example, controls can boost and bury results, filter entries from returned results, associate strings with each other as synonyms, or redirect results to specified URIs.

This page describes serving controls for search apps. For information about using serving controls with media recommendations, see [Create and manage media serving configs](https://docs.cloud.google.com/generative-ai-app-builder/docs/serving-configs).

## About serving controls

To change the results of a request, first create a serving control. Then, attach that control to the _serving config_ of a search app. A [serving config](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs) configures metadata that's used to generate serving time results, such as search results or answers. A serving control only affects requests served by the app if the control is attached to the app's serving config.

Some controls, such as boost controls, have dependencies on data stores. If a data store is removed from an app, then any data store-dependent controls are also removed from that app and become inactive, but are not deleted.

## Serving control types

The following types of serving controls are available:

Control | Description | Available for  
---|---|---  
**Boost control** | Changes the returned order of results | Search apps with data stores that support a schema, such as data stores that contain structured data, websites with structured data (advanced website indexing), unstructured data with metadata, or media data  
**Filter control** | Removes entries from returned results | Search apps with data stores that support a schema, such as data stores that contain structured data, websites (advanced website indexing), unstructured data with metadata, or media data  
**Synonyms control** | Associates queries with each other | Search apps with website (advanced website indexing), structured, unstructured, or media data stores  
**Redirect control** | Redirects to a specified URI | All search apps  
**Promote control** | Promotes a specified link for a query | All search apps  
  
## About conditions

When creating a control, you can optionally define a condition that determines when the control is applied. Conditions are defined using condition fields. The following condition fields are available:

  * **Query terms (`queryTerms`)**. An optional control that's applied when specific queries are searched for. When the `queryTerms` condition is used, the control is applied when the value of `queryTerms` matches a term in `SearchRequest.query`. Query terms can only be used when the `Control.searchUseCase` is set as `SOLUTION_TYPE_SEARCH`. Up to 10 different `queryTerms` can be specified on a single `Control.condition`. If no query terms are specified, the `queryTerms` field is ignored.

For a promote serving control, `queryTerms` can't be specified if you're specifying the `queryRegex` condition, which is applicable to basic website search only. Additionally, the `fullMatch` field for basic website search, must be set to `true` if `queryTerms` is specified. For all other search apps, only `queryTerms` is supported and `fullMatch` can be set to `true` or `false`.

  * **Time range (`activeTimeRange`)**. An optional control that's applied when a request occurs within a specified time range. It checks that the time a request was received is between `activeTimeRange.startTime` and `activeTimeRange.endTime`. Up to 10 `activeTimeRange` ranges can be specified on a single `Control.condition`. If the `activeTimeRange` field isn't specified, the field is ignored.

  * **`queryRegex`**. Only available for a promote serving control for basic website search only. This is an optional condition that applies the control when the query matches the specified regular expression. This condition can't be specified if you're specifying the `queryTerms` condition.




If multiple conditions are specified for a control, the control is applied to the search request when both condition types are satisfied. If multiple values for the same condition are specified, only one of the values needs to match for that condition to be satisfied.

For example, consider the following condition with two query terms specified:
    
    
    "queryTerms": [
      {
        "value": "gShoe",
        "fullMatch": true
      },
      {
        "value": "gBoot",
        "fullMatch": true
      }
    ]
    

The condition will be satisfied for a request with `SearchRequest.query="gShoe"` or a request with `SearchRequest.query="gBoot"`, but won't be satisfied with `SearchRequest.query="gSandal"` or any other string.

If no conditions are specified, the control is always applied.

For more information, see the [`Condition`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.Condition) field in the API reference.

## Create and attach boost serving controls

A boost serving control reorders the results by promoting or demoting them based on the applied conditions. Boost works by applying a multiplying factor to the ranking of a document that meets the boost conditions.

Use the following instructions to create a boost serving control.

### Console

To create and attach a boost control using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Select the app for which you want to create the boost control.

  3. On your app's overview page, make sure you are on the **System overview** tab.

  4. In the **Signal** stage, click the **Boost/Bury** tile.

  5. Click **Create control**.

  6. For **Name Your Control** , enter a name for your boost/bury control and click **Continue**.

  7. For **Set Rule Scope & Impact**, define the actions that you want to trigger with this control:

     1. Select a data store from the list. If you want the action to be applied to multiple data stores, create a control for each data store.

     2. For **Filter** , add a filter.

This is a string specifying requirements that must be met by the document. Only if the document matches all the requirements, the boost condition is applied. Otherwise, there is no change. If you don't specify a filter, then the boost is applied to all documents in the data store.

To understand how to write filter expressions, see [Filter custom search for structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata) and [Syntax for advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search#filter-expressions-advanced-indexing).

     3. For **Boost/bury value** , select a boost/bury value in the range [-1, 1] using the slider. The slider moves in steps of 0.01.

     4. Click **Continue**.

  8. For **Optional: When This Rule Activates** , set the following conditions that trigger the control. If no conditions are configured, the control is always in effect:

     1. Add **Partial match query terms**. The control takes effect when these query terms match partially.

     2. Add **Exact match query terms**. The control takes effect when these query terms match exactly.

     3. To add an active time range, click **Add time range** and set **Start Time 1** and **End Time 1**. This defines the window when the condition is active. You can add a maximum of 10 time ranges.

     4. Click **Continue**.

  9. For **Additional settings** , choose if you want to activate the rule:

     1. If you don't want to activate this control as soon as it's created, turn off **Publish this control immediately**.

     2. Click **Continue**.

  10. Click **Submit**.




### REST

A boost serving control is defined as a control with a `boostAction`.

Use the following instructions to create a boost serving control.

For field details, see the [`engines.controls` API reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.controls) and the [`engines.controls.create` API reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.controls/create).

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Run the following curl commands to create your controls.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls?controlId=CONTROL_ID" \
         -d '{
         "displayName": "DISPLAY_NAME",
         "solutionType": "SOLUTION_TYPE_SEARCH",
         "useCases": [
           "USE_CASE"
         ],
         "conditions": {
          "queryTerms": [
            {
              "value": "VALUE",
              "fullMatch": FULL_MATCH
            }
          ],
          "activeTimeRange": [
            {
              "startTime": "START_TIMESTAMP",
              "endTime": "END_TIMESTAMP"
            }
          ]
         },
         "boostAction": {
           "boost": BOOST_VALUE,
           "filter": "FILTER",
           "dataStore": "DATA_STORE_RESOURCE_PATH"
          }
         }'

Replace the following:

     * `PROJECT_ID`: the number or ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app.
     * `CONTROL_ID`: a unique identifier for the control. The ID can contain [1-63] characters that can be letters, digits, hyphens, and underscores.
     * `DISPLAY_NAME`: the human-readable name for the control. Google recommends that this name provide an indication of when or why to use the control. Must be a UTF-8 encoded string with length [1,128].
     * `USE_CASE`: must be either `SEARCH_USE_CASE_SEARCH` or `SEARCH_USE_CASE_BROWSE`. If `SEARCH_USE_CASE_BROWSE` is specified, then `Condition.queryTerms` can't be used in the condition.
     * `CONDITION`: an optional field that defines when the control should be applied. Contains the following fields: 
       * `VALUE`: the specific query value to match against. It's a lowercase UTF-8 string with length `[1, 5000]`. If `FULL_MATCH_1` is `true`, this field can have at most three space-separated terms.
       * `FULL_MATCH`: a boolean that indicates whether the search query needs to exactly match the query term. When set to `true`, it requires `SearchRequest.query` to completely match the `queryTerm.value`. When set to `false`, it requires `SearchRequest.query` to contain `queryTerm.value` as a substring.
       * `START_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the start of a time range.
       * `END_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the end of a time range.
     * `BOOST_VALUE`: a floating point number in the range [-1,1]. When the value is negative, results are demoted (they appear lower down in the results). When the value is positive, results are promoted (they appear higher up in the results). For more information, see [`boostAction`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#boostaction).
     * `FILTER`: a string specifying requirements that must be met by the document. If the document matches all the requirements, the boost is applied. Otherwise, there is no change. If this field is empty, then the boost is applied to all documents in the data store. For information about the filtering syntax, see [Filter expression syntax](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax) and [Syntax for advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search#filter-expressions-advanced-indexing). For a list key property fields that can be used in filters, see [Key properties that support filtering](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#key-properties-filtering).
     * `DATA_STORE_RESOURCE_PATH`: the full resource path of the data store whose documents should be boosted by this control. The format of the full resource path is `projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATA_STORE_ID`. This data store must be attached to the engine specified in the request.
  3. Attach the control to the app's serving config using the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/patch) method.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search?update_mask=boost_control_ids" \
         -d '{
          "boostControlIds": ["BOOST_ID_1", "BOOST_ID_2"]
         }'

Replace `BOOST_ID_N` with the control IDs that you created in the previous step. 




## Create and attach filter serving controls

A filter serving control filters by a given criteria or rule. For example, for hotel site, you can apply a filter for `(price < 175 AND petfriendly = "true")` that only shows pet-friendly hotels under the price of $175 USD per night.

A filter serving control is defined as a control with a `filterAction`.

Use the following instructions to create a filter serving control.

For field details, see the [`engines.controls` API reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.controls) and the [`engines.controls.create` API reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.controls/create).

### Console

To create and attach a filter control using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Select the app for which you want to create the promote control.

  3. On your app's overview page, make sure you are on the **System overview** tab.

  4. In the **Signal** stage, click the **Filter** tile.

  5. Click **Create control**.

  6. For **Name Your Control** , enter a name for your filter control and click **Continue**.

  7. For **Rule Scope & Impact**, set the following:

     1. **Select a data store** from the list that you want to attach this filter control to. If you want the action to be applied to multiple data stores, create a control for each data store.

     2. For **Filter** , tell the rule which specific items to look for. You can combine search terms using `AND`, `OR`, `NOT`, and group terms with `()`. For exact phrases, use quotes `""`. For example: `status: "open" AND priority:"P1"`.

To understand how to write filter expressions, see [Filter custom search for structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata) and [Syntax for advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search#filter-expressions-advanced-indexing).

     3. Click **Continue**.

  8. For **Optional: When This Rule Activates** , define the actions that you want to trigger with this control. If no conditions are configured, the control is always in effect:

     1. Add **Partial match query terms**. The control takes effect when these query terms match partially.

     2. Add **Exact match query terms**. The control takes effect when these query terms match exactly.

     3. To add an active time range, click **Add time range** and set **Start Time 1** and **End Time 1**. This defines the window when the condition is active. You can add a maximum of 10 time ranges.

     4. Click **Continue**.

  9. For **Additional settings** , choose if you want to activate the rule:

     1. If you don't want to activate this control as soon as it's created, turn off **Publish this control immediately**.

     2. Click **Continue**.

  10. Click **Submit**.




### REST

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Run the following curl commands to create your controls.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls?controlId=CONTROL_ID" \
         -d '{
         "displayName": "DISPLAY_NAME",
         "solutionType": "SOLUTION_TYPE_SEARCH",
         "useCases": ["USE_CASE"],
         "conditions": {
           "queryTerms": [
             {
               "value": "VALUE",
               "fullMatch": FULL_MATCH
             }
           ],
           "activeTimeRange": [
             {
               "startTime": "START_TIMESTAMP",
               "endTime": "END_TIMESTAMP"
             }
           ]
         },
         "filterAction": {
           "filter": "FILTER"
          }
         }'

Replace the following:

     * `PROJECT_ID`: the number or ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app.
     * `CONTROL_ID`: a unique identifier for the control. The ID can contain [1-63] characters that can be letters, digits, hyphens, and underscores.
     * `DISPLAY_NAME`: the human-readable name for the control. Google recommends that this name provide an indication of when or why to use the control. Must be a UTF-8 encoded string with length [1,128].
     * `USE_CASE`: must be either `SEARCH_USE_CASE_SEARCH` or `SEARCH_USE_CASE_BROWSE`. If `SEARCH_USE_CASE_BROWSE` is specified, then `Condition.queryTerms` can't be used in the condition.
     * `CONDITION`: an optional field that defines when the control should be applied. Contains the following fields: 
       * `VALUE`: the specific query value to match against. It's a lowercase UTF-8 string with length `[1, 5000]`. If `FULL_MATCH_1` is `true`, this field can have at most three space-separated terms.
       * `FULL_MATCH`: a boolean that indicates whether the search query needs to exactly match the query term. When set to `true`, it requires `SearchRequest.query` to completely match the `queryTerm.value`. When set to `false`, it requires `SearchRequest.query` to contain `queryTerm.value` as a substring.
       * `START_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the start of a time range.
       * `END_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the end of a time range.
     * `FILTER`: a string specifying requirements that must be met by the document. If the document matches all the requirements, the document is returned in the results. Otherwise, the document is not in the results.

For more information, see [`filterAction`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#filteraction). For information about the filtering syntax, see [Filter expression syntax](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax) and [Syntax for advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search#filter-expressions-advanced-indexing).

**Note:** The document field `title` can't be filtered.
  3. Attach the control to the app's serving config using the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/patch) method.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search?update_mask=filter_control_ids" \
         -d '{
           "filterControlIds": ["FILTER_ID_1", "FILTER_ID_2"]
         }'

Replace `FILTER_ID_N` with the control IDs that you created in the previous step. 




## Create and attach synonyms serving controls

A synonyms serving control is defined as a control with a `synonymsAction`.

Use the following instructions to create a synonyms serving control.

For field details, see the [`engines.controls` API reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.controls) and the [`engines.controls.create` API reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.controls/create).

### Console

To create and attach a synonmys control using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Select the app for which you want to create the synonyms control.

  3. On your app's overview page, make sure you are on the **System overview** tab.

  4. In the **Prepare** stage, click the **Synonyms** tile.

  5. Click **Create control**.

  6. For **Name Your Control** , enter a name for your synonyms control and click **Continue**.

  7. For **Rule Scope & Impact**:

     1. Enter the synonyms you want to have considered in the control. For example, enter _cats_ followed by a return (not comma), then _feline._

     2. When you are finished entering synonyms, click **Continue**.

  8. For **Optional: When This Rule Activates** , define the actions that you want to trigger with this control. If no conditions are configured, the control is always in effect:

     1. To add an active time range, click **Add time range** and set **Start Time 1** and **End Time 1**. This defines the window when the condition is active. You can add a maximum of 10 time ranges.

     2. Click **Continue**.

  9. For **Additional settings** , choose if you want to activate the rule:

     1. If you don't want to activate this control as soon as it's created, turn off **Publish this control immediately**.

     2. Click **Continue**.

  10. Click **Submit**.




### REST

  1. Run the following curl commands to create your controls.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls?controlId=CONTROL_ID" \
         -d '{
         "displayName": "DISPLAY_NAME",
         "solutionType": "SOLUTION_TYPE_SEARCH",
         "useCases": ["USE_CASE"],
         "conditions": {
           "queryTerms": [
             {
               "value": "VALUE",
               "fullMatch": FULL_MATCH
             }
           ],
           "activeTimeRange": [
             {
               "startTime": "START_TIMESTAMP",
               "endTime": "END_TIMESTAMP"
             }
           ]
         },
         "synonymsAction": {
           "synonyms": ["SYNONYMS_1","SYNONYMS_2"]
          }
         }'

Replace the following:

     * `PROJECT_ID`: the number or ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app.
     * `CONTROL_ID`: a unique identifier for the control. The ID can contain [1-63] characters that can be letters, digits, hyphens, and underscores.
     * `DISPLAY_NAME`: the human-readable name for the control. Google recommends that this name provide an indication of when or why to use the control. Must be a UTF-8 encoded string with length [1,128].
     * `USE_CASE`: must be either `SEARCH_USE_CASE_SEARCH` or `SEARCH_USE_CASE_BROWSE`. If `SEARCH_USE_CASE_BROWSE` is specified, then `Condition.queryTerms` can't be used in the condition.
     * `CONDITION`: an optional field that defines when the control should be applied. Contains the following fields: 
       * `VALUE`: the specific query value to match against. It's a lowercase UTF-8 string with length `[1, 5000]`. If `FULL_MATCH_1` is `true`, this field can have at most three space-separated terms.
       * `FULL_MATCH`: a boolean that indicates whether the search query needs to exactly match the query term. When set to `true`, it requires `SearchRequest.query` to completely match the `queryTerm.value`. When set to `false`, it requires `SearchRequest.query` to contain `queryTerm.value` as a substring.
       * `START_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the start of a time range.
       * `END_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the end of a time range.
     * `SYNONYMS_N`: a list of strings that are associated with each other, making it more likely for each to show similar results. While it's more likely that you get similar results, when you search for each of the synonym entries, you might not receive all the relevant results for all the associated synonyms. You must specify at least two synonyms and you can specify up to 100 synonyms. Each synonym must be UTF-8 encoded and in lowercase. No duplicate strings are allowed. For example, you can add "pixel", "android phone", and "google phone" as synonyms. For more information, see [`synonymsAction`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#synonymsaction).
  2. Attach the control to the app's serving config using the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/patch) method.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search?update_mask=synonyms_control_ids" \
         -d '{
           "synonymsControlIds": ["SYNONYMS_ID_1", "SYNONYMS_ID_2"]
         }'

Replace `SYNONYMS_ID_N` with the control IDs that you created in the previous step.




## Create and attach redirect serving controls

A redirect serving control allows redirecting users to a provided URI. Redirect controls are defined as a control with a `redirectAction`.

Use the following instructions to create a redirect serving control.

For field details, see the [`engines.controls` API reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.controls) and the [`engines.controls.create` API reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.controls/create).

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Run the following curl commands to create your controls.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls?controlId=CONTROL_ID" \
         -d '{
         "displayName": "DISPLAY_NAME",
         "solutionType": "SOLUTION_TYPE_SEARCH",
         "useCases": ["USE_CASE"],
         "conditions": {
           "queryTerms": [
             {
               "value": "VALUE",
               "fullMatch": FULL_MATCH
             }
           ],
           "activeTimeRange": [
             {
               "startTime": "START_TIMESTAMP",
               "endTime": "END_TIMESTAMP"
             }
           ]
         },
         "redirectAction": {
           "redirectURI": "REDIRECT_URI"
          }
         }'

Replace the following:

     * `PROJECT_ID`: the number or ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app.
     * `CONTROL_ID`: a unique identifier for the control. The ID can contain [1-63] characters that can be letters, digits, hyphens, and underscores.
     * `DISPLAY_NAME`: the human-readable name for the control. Google recommends that this name provide an indication of when or why to use the control. Must be a UTF-8 encoded string with length [1,128].
     * `USE_CASE`: must be either `SEARCH_USE_CASE_SEARCH` or `SEARCH_USE_CASE_BROWSE`. If `SEARCH_USE_CASE_BROWSE` is specified, then `Condition.queryTerms` can't be used in the condition.
     * `CONDITION`: an optional field that defines when the control should be applied. Contains the following fields: 
       * `VALUE`: the specific query value to match against. It's a lowercase UTF-8 string with length `[1, 5000]`. If `FULL_MATCH_1` is `true`, this field can have at most three space-separated terms.
       * `FULL_MATCH`: a boolean that indicates whether the search query needs to exactly match the query term. When set to `true`, it requires `SearchRequest.query` to completely match the `queryTerm.value`. When set to `false`, it requires `SearchRequest.query` to contain `queryTerm.value` as a substring.
       * `START_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the start of a time range.
       * `END_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the end of a time range.
     * `REDIRECT_URI_N`: a URI where you are redirected. Can have a maximum length of 2000 characters. For example, if the value of the query term is "support", you can set a redirect to your technical support page instead of returning (or failing to return) search results for "support". In this example, the redirect URI becomes `"https://www.example.com/support"`. For more information, see [`redirectAction`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#redirectaction).
  3. Attach the control to the app's serving config using the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/patch) method.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search?update_mask=redirect_control_ids" \
         -d '{
           "redirectControlIds": ["REDIRECT_ID_1", "REDIRECT_ID_2"]
         }'

Replace `REDIRECT_ID_N` with the control IDs that you created in the previous step.




## Create and attach promote serving controls

A promote serving control lets you display a link as a promoted result and is available for the following types of search data stores:

  * Website data stores with basic website search: For these data stores, you don't need to attach a promote control to the serving config of the app. Creating and enabling a promote control activates the promote control. You can turn a promote control on or off by enabling or disabling it.

  * Data stores with structured and unstructured data, website data with advanced website indexing, and blended search apps: For these data stores, you need to attach the promote control to the serving config.




Promote controls are defined using a `promoteAction`.

To successfully create a promote control, one of the following fields is required in the creation request:

  * **`queryTerms`** : This condition can't be specified if you're specifying the `queryRegex` condition, which is applicable to basic website search only. For basic website search, `fullMatch` must be set to `true` if `queryTerms` is specified. For all other search apps, only `queryTerms` is supported and `fullMatch` can be set to `true` or `false`.
  * **`queryRegex`**. Only available for a promote serving control for basic website search only. This condition applies the control when the query matches the specified regular expression. This condition can't be specified if you're specifying the `queryTerms` condition.



That is, for basic website search, you must either specify the `queryTerms` field with `fullMatch` set to `true` or specify the `queryRegex` field. For all other types of search, specify the `queryTerms` field with `fullMatch` set to `true` or `false`.

Use the following instructions to create a promote serving control.

For field details, see the [`engines.controls` API reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.controls) and the [`engines.controls.create` API reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.controls/create).

### Console

To create and attach a promote control for a basic website search app using the Google Cloud console, do the following. To create a promote control for other app types, follow the instructions on the REST tab.

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Select the app for which you want to create the filter control.

  3. On your app's overview page, make sure you are on the **System overview** tab.

  4. In the **Signal** stage, click the **Promote** tile.

  5. Click **Create control**.

  6. For **Name Your Control** , enter a name for your promote control and click **Continue**.

  7. For **Rule Scope & Impact**, set the following:

     1. **Select a data store** from the list that you want to attach this filter control to. If you want the action to be applied to multiple data stores, create a control for each data store.

     2. Enter the **Promote title** , such as _View latest video._

     3. Enter the **Promote URL** , such as the location of the video.

     4. Enter the **Promote image URL** , such as a thumbnail or screenshot.

     5. Enter a brief **Promote description** , such as what the video is about. The maximum is 250 characters.

  8. For **Optional: When This Rule Activates** , define the actions that you want to trigger with this control. If no conditions are configured, the control is always in effect:

     1. Add **Exact match query terms**. The control takes effect when these query terms match exactly.

     2. To add an active time range, click **Add time range** and set **Start Time 1** and **End Time 1**. This defines the window when the condition is active. You can add a maximum of 10 time ranges.

     3. Click **Continue**.

  9. Click **Submit**.




### REST

  1. Run the following curl commands to create your controls.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls?controlId=CONTROL_ID" \
         -d '{
         "displayName": "DISPLAY_NAME",
         "solutionType": "SOLUTION_TYPE_SEARCH",
         "useCases": ["USE_CASE"],
         "conditions": {
           "queryTerms": [
             {
               "value": "VALUE",
               "fullMatch": true
             }
           ],
           "activeTimeRange": [
             {
               "startTime": "START_TIMESTAMP",
               "endTime": "END_TIMESTAMP"
             }
           ],
           "queryRegex": "VALUE_REGEX"
         },
         "promoteAction": {
           "dataStore": "DATA_STORE_RESOURCE_PATH",
           "searchLinkPromotion": {
              "document": "DOCUMENT_RESOURCE_PATH",
              "title": "TITLE",
              "uri": "URI",
              "description": "DESCRIPTION",
              "enabled": ENABLED_TRUE|FALSE,
           }
          }
         }'

Replace the following:

     * `PROJECT_ID`: the number or ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app.
     * `CONTROL_ID`: a unique identifier for the control. The ID can contain [1-63] characters that can be letters, digits, hyphens, and underscores.
     * `DISPLAY_NAME`: the human-readable name for the control. Google recommends that this name provide an indication of when or why to use the control. Must be a UTF-8 encoded string with length [1,128].
     * `USE_CASE`: must be either `SEARCH_USE_CASE_SEARCH` or `SEARCH_USE_CASE_BROWSE`. If `SEARCH_USE_CASE_BROWSE` is specified, then `Condition.queryTerms` can't be used in the condition.
     * **`Condition`** : an optional object that defines when the control should be applied. Contains the following fields: 
       * `queryTerms`: It can't be used with the `queryRegex` field. 
         * `VALUE`: the specific query value to match against. It's a lowercase UTF-8 string with length `[1, 5000]`.
       * `activeTimeRange`: 
         * `START_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the start of a time range.
         * `END_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the end of a time range.
       * `queryRegex`: only available for data stores with basic website search. This field can't be used with the `queryTerms` field. 
         * `VALUE_REGEX`: a regular expression to match the query against.
     * `DATA_STORE_RESOURCE_PATH`: the full resource path of the data store whose search results contain the promoted URL. The format of the full resource path is `projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATA_STORE_ID`. This data store must be attached to the engine specified in the request.
     * `DOCUMENT_RESOURCE_PATH`: a field to specify the document resource path of the document to be promoted: 
       * For search data stores with structured and unstructured data, you must provide either the document resource path in the `DOCUMENT_RESOURCE_PATH` field, the URI in the `URI` field, or both. The format of the full resource path is `projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID`.
       * For website data stores, this field must be unset and set the URI field instead.
     * `TITLE`: a required field to specify the title of the document or the web page to be promoted. This title is displayed in the search result.
     * `URI`: a required field to specify the URI link where the search result leads the user. This URI need not be included in the data store. 
       * For search data stores with structured and unstructured data, you must provide either the document resource path in the `DOCUMENT_RESOURCE_PATH` field, the URI in the `URI` field, or both.
       * For website data stores, this is a required field and you must set it.
     * `DESCRIPTION`: an optional field to describe the document or web page to be promoted, which is displayed in the search result.
     * `ENABLED_TRUE|FALSE`: an optional boolean field to indicate whether the promote control is turned on and attached to the app. This field is applicable to website data stores with basic website search only. When you set this field to `false`, the promote serving control is turned off and for the control to take effect, you must update the control by enabling it, as explained in the next step. For more information, see [`promoteAction`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#promoteaction).

#### Response

You should receive a JSON response similar to the following:
    
    {
     "name": "projects/PROJECT_NUMBER/locations/global/collections/default_collection/engines/APP_ID/controls/PROMOTE_CONTROL_ID",
     "displayName": "PROMOTE_CONTROL_NAME",
     "solutionType": "SOLUTION_TYPE_SEARCH",
     "conditions": [
       {
         "queryTerms": [
           {
             "value": "VALUE",
             "fullMatch": true
           }
         ]
       }
     ],
     "useCases": [
       "SEARCH_USE_CASE_SEARCH"
     ],
     "promoteAction": {
       "dataStore": "projects/PROJECT_NUMBER/locations/global/collections/default_collection/dataStores/DATA_STORE_ID",
       "searchLinkPromotion": {
         "title": "URI_TITLE",
         "uri": "URI",
         "description": "URI_DESCRIPTION",
         "enabled": ENABLED_TRUE|FALSE
      }
     }
    }
    

  2. For all search apps except for basic website search, attach the control to the app's serving config using the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/patch) method. The order in which the `promoteControlIds` are attached in the following request is the order in which the promoted results are returned.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search?update_mask=promote_control_ids" \
         -d '{
           "promoteControlIds": ["PROMOTE_ID_1", "PROMOTE_ID_2"]
         }'

Replace `PROMOTE_ID_N` with the control IDs that you created in the previous step.

  3. Optional: For basic website search, you need not attach the control to the app's serving config. However, for basic website search you can turn a promote control on or off after the control is created, call the [`engines.control.patch`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.controls/patch) method.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/controls/CONTROL_ID?updateMask=promoteAction.searchLinkPromotion.enabled" \
         -d '{
         "promoteAction": {
           "searchLinkPromotion": {
              "enabled": ENABLED_TRUE|FALSE,
           }
         }
         }'




### Example

When you send a search request to the app with a query that matches the query or query regular expression specified for the promote control, the promoted link appears in the response.

For example, suppose that you create a promote control with the following configuration in a data store with basic website search:
    
    
    {
     "conditions": [
       {
         "queryTerms": [
           {
             "value": "artificial intelligence",
             "fullMatch": true
           }
         ]
       }
     ]"
     ...
     promoteAction": {
      "dataStore": "https://discoveryengine.googleapis.com/v1alpha/projects/123456/locations/us/collections/default_collection/dataStores/basic-website-data-store" \
      "searchLinkPromotion": {
        "title": "What is AI?",
        "uri": "https://cloud.google.com/learn/what-is-artificial-intelligence",
        "description": "Explain what is AI"
        "enabled": true
      }
     }
    }
    

Then, you send the following [search](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/search) request:
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://discoveryengine.googleapis.com/v1alpha/projects/123456/locations/us/collections/default_collection/engines/basic-website-app/servingConfigs/default_search:search" \
      -d '{
    "query": "artificial intelligence"
    }'
    

You should receive a JSON response similar to the following truncated response. The response contains the `searchLinkPromotions` field that contains the promoted link.
    
    
    {
     "results": [...],
      "totalSize": 3,
      "attributionToken": "_gHw_QoMCMSbhboGELuI1qwCEiQ2NzQwYmYzYi0wMDAwLTJmYTctYTk1OC0yNDA1ODg4MzZmYjgiB0dFTkVSSUMqvAGrxIotzua1L5neqC_n7YgtxPzLMIOymiK0kq4wxPi8MPn2sy3LmrQw6d3EMNSynRWc1rctnN3YMOuCsS3ogrEto4CXIsLwnhX89rMtkKS0MJbeqC-jibMtkPeyMMTGsTCZ3dgw5O2ILa7Eii2NpLQw5t3EMN6PmiKOvp0VwfzLMICymiKq-LMt0ea1L634sy3Fy_MXtreMLbeSrjDHxrEwzpq0MMH4vDCgibMtn9a3LZSSxTCOkckw24-aIjAB",
      "guidedSearchResult": {},
      "summary": {},
      "searchLinkPromotions": [
        {
          "title": "What is AI?",
          "uri": "https://cloud.google.com/learn/what-is-artificial-intelligence",
          "description": "Explain what is AI"
        }
      ]
    }
    

## Modify serving controls

To modify a control's configuration, do the following:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Select the app for which you want to modify controls.

  3. In the **System overview** tab, select either the **Prepare** or **Signal** stage where your control is located.

  4. In the list of the app's controls, click more_vert for a control that you want to modify and click **Edit**.

  5. Edit the control in the **Edit control** pane:

     1. To enable or disable a control, in the list of the app's filter controls, click more_vert for a control that you want to enable or disable and click **Enable** or **Disable** , respectively.

     2. To delete a control, in the list of the app's controls, click more_vert for a control that you want to delete and click **Delete**.




## What's next

  * To understand the impact of a serving control on the search quality of a custom search app, evaluate the search quality. For more information, see [Evaluate search quality](https://docs.cloud.google.com/generative-ai-app-builder/docs/evaluate-search-quality).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
