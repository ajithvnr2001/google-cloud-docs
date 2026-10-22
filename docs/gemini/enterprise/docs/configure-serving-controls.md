---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-serving-controls/
title: Configure serving controls \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:37.102522+00:00
---

# Configure serving controls  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-serving-controls/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure serving controls Stay organized with collections  Save and categorize content based on your preferences. 

Serving controls (also called controls) change the default behavior of how a request is served when results are returned. Serving controls act at a data-store level.

For example, controls can boost and bury results, filter entries from returned results, associate strings with each other as synonyms, or redirect results to specified URIs.

## About serving controls

To change the results of a request, first create a serving control. Then, attach that control to the _serving config_ of an app. A [serving config](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs) configures metadata that's used to generate serving time results, such as search results or answers. A serving control only affects requests served by the app if the control is attached to the app's serving config.

Some controls, such as boost controls, have dependencies on data stores. If a data store is removed from an app, then any data store-dependent controls are also removed from that app and become inactive, but are not deleted.

### Serving control types

The following types of serving controls are available:

Control | Description | Available for  
---|---|---  
**Boost control** | Changes the returned order of results | Search apps with data stores that support a schema, such as data stores that contain structured data or unstructured data with metadata  
**Filter control** | Removes entries from returned results | Search apps with data stores that support a schema, such as data stores that contain structured data or unstructured data with metadata  
**Synonyms control** | Associates queries with each other | Search apps with structured or unstructured data stores  
**Redirect control** | Redirects to a specified URI | All search apps  
**Promote control** | Promotes a specified link for a query | Search apps with structured or unstructured data stores  
  
## About conditions

When creating a control, you can optionally define a condition that determines when the control is applied. Conditions are defined using condition fields. The following condition fields are available:

  * **`queryTerms`**. An optional control that's applied when specific queries are searched for. When the `queryTerms` condition is used, the control is applied when the value of `queryTerms` matches a term in `SearchRequest.query`. Query terms can only be used when the `Control.searchUseCase` is set as `SOLUTION_TYPE_SEARCH`. Up to 10 different `queryTerms` can be specified on a single `Control.condition`. If no query terms are specified, the `queryTerms` field is ignored.

To successfully create a promote control, you must specify the `queryTerms` field with `fullMatch` set to `true` or `false`.

  * **`activeTimeRange`**. An optional control that's applied when a request occurs within a specified time range. It checks that the time a request was received is between `activeTimeRange.startTime` and `activeTimeRange.endTime`. Up to 10 `activeTimeRange` ranges can be specified on a single `Control.condition`. If the`activeTimeRange` field isn't specified, the field is ignored.




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

For more information, see the [`Condition`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.Condition) field in the API reference.

## Create and attach boost serving controls

A boost serving control reorders the results by promoting or demoting them based on the applied conditions. Boost works by applying a multiplying factor to the ranking of a document that meets the boost conditions.

Use the following instructions to create a boost serving control.

### Console

To create and attach a boost control using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select the app for which you want to create the boost control.

  3. Click **Configurations** and then click the **Control** tab.

  4. Click **Create control**.

  5. For **What do you want to do?** , specify the control name and type:

     1. For **Control name** , enter a name for your boost/bury control.

     2. For **Control Type** , select **Boost/bury**.

     3. Click **Continue**.

  6. For **Set Rule Scope & Impact**, define the actions that you want to trigger with this control:

     1. Select a data store from the list. If you want the action to be applied to multiple data stores, create a control for each data store.

     2. For **Filter** , add a filter.

This is a string specifying requirements that must be met by the document. Only if the document matches all the requirements, the boost condition is applied. Otherwise, there is no change. If you don't specify a filter, then the boost is applied to all documents in the data store.

For information about the filtering syntax, see [Filter expression syntax](https://docs.cloud.google.com/gemini/enterprise/docs/filter-search-metadata#filter-expression-syntax).

     3. For **Boost/bury value** , select a boost/bury value in the range [-1, 1] using the slider. The slider moves in steps of 0.01.

     4. Click **Continue**.

  7. For **Optional: When This Rule Activates** , set the following conditions that trigger the control. If no conditions are configured, the control is always in effect:

     1. Add **Partial match query terms**. The control takes effect when these query terms match partially.

     2. Add **Exact match query terms**. The control takes effect when these query terms match exactly.

     3. To add an active time range, click **Add time range** and set **Start Time 1** and **End Time 1**. This defines the window when the condition is active. You can add a maximum of 10 time ranges.

     4. Click **Continue**.

  8. For **Additional settings** , choose if you want to activate the rule:

     1. If you don't want to activate this control as soon as it's created, turn off **Publish this control immediately**.

     2. Click **Continue**.

  9. Click **Submit**. 




### REST

A boost serving control is defined as a control with a `boostAction`.

Use the following instructions to create a boost serving control.

For field details, see the [`engines.controls` API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls) and the [`engines.controls.create` API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls/create).

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

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
     * `APP_ID`: the ID of the app.
     * `CONTROL_ID`: a unique identifier for the control. The ID can contain [1-63] characters that can be letters, digits, hyphens, and underscores.
     * `DISPLAY_NAME`: the human-readable name for the control. Google recommends that this name provide an indication of when or why to use the control. Must be a UTF-8 encoded string with length [1,128].
     * `USE_CASE`: must be either `SEARCH_USE_CASE_SEARCH` or `SEARCH_USE_CASE_BROWSE`. If `SEARCH_USE_CASE_BROWSE` is specified, then `Condition.queryTerms` can't be used in the condition.
     * `CONDITION`: an optional field that defines when the control should be applied. Contains the following fields: 
       * `VALUE`: the specific query value to match against. It's a lowercase UTF-8 string with length `[1, 5000]`. If `FULL_MATCH_1` is `true`, this field can have at most three space-separated terms.
       * `FULL_MATCH`: a boolean that indicates whether the search query needs to exactly match the query term. When set to `true`, it requires `SearchRequest.query` to completely match the `queryTerm.value`. When set to `false`, it requires `SearchRequest.query` to contain `queryTerm.value` as a substring.
       * `START_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the start of a time range.
       * `END_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the end of a time range.
     * `BOOST_VALUE`: a floating point number in the range [-1,1]. When the value is negative, results are demoted (they appear lower down in the results). When the value is positive, results are promoted (they appear higher up in the results). For more information, see [`boostAction`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#boostaction).
     * `FILTER`: a string specifying requirements that must be met by the document. If the document matches all the requirements, the boost is applied. Otherwise there is no change. If this field is empty, then the boost is applied to all documents in the data store. For the filtering syntax, see [Filter expression syntax](https://docs.cloud.google.com/gemini/enterprise/docs/filter-search-metadata#filter-expression-syntax). Note: The document field `title` can't be filtered.
     * `DATA_STORE_RESOURCE_PATH`: the full resource path of the data store whose documents should be boosted by this control. The format of the full resource path is `projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATA_STORE_ID`. This data store must be attached to the engine specified in the request.
  3. Attach the control to the app's serving config using the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/patch) method.
         
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

A filter serving control is defined as a control with a `filterAction`.

Use the following instructions to create a filter serving control.

### Console

To create and attach a filter control using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select the app for which you want to create the filter control.

  3. Click **Configurations** and then click the **Control** tab.

  4. Click **Create control**.

  5. For **What do you want to do?** , specify the control name and type:

     1. For **Control name** , enter a name for your filter control.

     2. For **Control Type** , select **Filter**.

     3. Click **Continue**.

  6. For **Set Rule Scope & Impact**, define the actions that you want to trigger with this control:

     1. Select a data store from the list. If you want the action to be applied to multiple data stores, create a control for each data store.

     2. For **Filter** , tell the rule which specific items to look for. You can combine search terms using `AND`, `OR` `NOT` and group terms with `()`. For exact phrases, use quotation marks (`""`). For example: `category: "electronics" AND price < 500, status: "open" AND priority:"P1"`.

For information about the filtering syntax, see [Filter expression syntax](https://docs.cloud.google.com/gemini/enterprise/docs/filter-search-metadata#filter-expression-syntax).

     3. Click **Continue**.

  7. For **Optional: When This Rule Activates** , set the following conditions that trigger the control. If no conditions are configured, the control is always in effect:

     1. Add **Partial match query terms**. The control takes effect when these query terms match partially.

     2. Add **Exact match query terms**. The control takes effect when these query terms match exactly.

     3. To add an active time range, click **Add time range** and set **Start Time 1** and **End Time 1**. This defines the window when the condition is active. You can add a maximum of 10 time ranges.

     4. Click **Continue**.

  8. For **Additional settings** , choose if you want to activate the rule:

     1. If you don't want to activate this control as soon as it's created, turn off **Publish this control immediately**.

     2. Click **Continue**.

  9. Click **Submit**. 




### REST

For field details, see the [`engines.controls` API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls) and the [`engines.controls.create` API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls/create).

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

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
     * `APP_ID`: the ID of the app.
     * `CONTROL_ID`: a unique identifier for the control. The ID can contain [1-63] characters that can be letters, digits, hyphens, and underscores.
     * `DISPLAY_NAME`: the human-readable name for the control. Google recommends that this name provide an indication of when or why to use the control. Must be a UTF-8 encoded string with length [1,128].
     * `USE_CASE`: must be either `SEARCH_USE_CASE_SEARCH` or `SEARCH_USE_CASE_BROWSE`. If `SEARCH_USE_CASE_BROWSE` is specified, then `Condition.queryTerms` can't be used in the condition.
     * `CONDITION`: an optional field that defines when the control should be applied. Contains the following fields: 
       * `VALUE`: the specific query value to match against. It's a lowercase UTF-8 string with length `[1, 5000]`. If `FULL_MATCH_1` is `true`, this field can have at most three space-separated terms.
       * `FULL_MATCH`: a boolean that indicates whether the search query needs to exactly match the query term. When set to `true`, it requires `SearchRequest.query` to completely match the `queryTerm.value`. When set to `false`, it requires `SearchRequest.query` to contain `queryTerm.value` as a substring.
       * `START_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the start of a time range.
       * `END_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the end of a time range.
     * `FILTER`: a string specifying requirements that must be met by the document. If the document matches all the requirements, the document is returned in the results. Otherwise the document is not in the results. For information about the filtering syntax, see [Filter expression syntax](https://docs.cloud.google.com/gemini/enterprise/docs/filter-search-metadata#filter-expression-syntax). For more information, see [`filterAction`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#filteraction). Note: The document field `title` can't be filtered.
  3. Attach the control to the app's serving config using the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/patch) method.
         
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

### Console

To create and attach a synonyms control using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select the app for which you want to create the synonyms control.

  3. Click **Configurations** and then click the **Control** tab.

  4. Click **Create control**.

  5. For **What do you want to do?** , specify the control name and type:

     1. For **Name Your Control** , enter a name for your synonyms control.

     2. For **Control Type** , select **Synonyms**.

     3. Click **Continue**.

  6. For **Set Rule Scope & Impact**, define the actions that you want to trigger with this control:

     1. Enter the synonyms you want to have considered in the control. For example, enter _cats_ followed by a return (not comma), then _feline._

     2. Click **Continue**.

  7. For **Optional: When This Rule Activates** , set the following conditions that trigger the control. If no conditions are configured, the control is always in effect:

     1. To add an active time range, click **Add time range** and set **Start Time 1** and **End Time 1**. This defines the window when the condition is active. You can add a maximum of 10 time ranges.

     2. Click **Continue**.

  8. For **Additional settings** , choose if you want to activate the rule:

     1. If you don't want to activate this control as soon as it's created, turn off **Publish this control immediately**.

     2. Click **Continue**.

  9. Click **Submit**. 




### REST

For field details, see the [`engines.controls` API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls) and the [`engines.controls.create` API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls/create).

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

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
         "synonymsAction": {
           "synonyms": ["SYNONYMS_1","SYNONYMS_2"]
          }
         }'

Replace the following:

     * `PROJECT_ID`: the number or ID of your Google Cloud project.
     * `APP_ID`: the ID of the app.
     * `CONTROL_ID`: a unique identifier for the control. The ID can contain [1-63] characters that can be letters, digits, hyphens, and underscores.
     * `DISPLAY_NAME`: the human-readable name for the control. Google recommends that this name provide an indication of when or why to use the control. Must be a UTF-8 encoded string with length [1,128].
     * `USE_CASE`: must be either `SEARCH_USE_CASE_SEARCH` or `SEARCH_USE_CASE_BROWSE`. If `SEARCH_USE_CASE_BROWSE` is specified, then `Condition.queryTerms` can't be used in the condition.
     * `CONDITION`: an optional field that defines when the control should be applied. Contains the following fields: 
       * `VALUE`: the specific query value to match against. It's a lowercase UTF-8 string with length `[1, 5000]`. If `FULL_MATCH_1` is `true`, this field can have at most three space-separated terms.
       * `FULL_MATCH`: a boolean that indicates whether the search query needs to exactly match the query term. When set to `true`, it requires `SearchRequest.query` to completely match the `queryTerm.value`. When set to `false`, it requires `SearchRequest.query` to contain `queryTerm.value` as a substring.
       * `START_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the start of a time range.
       * `END_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the end of a time range.
     * `SYNONYMS_N`: a list of strings that are associated with each other, making it more likely for each to show similar results. While it's more likely that you get similar results, when you search for each of the synonym entries, you might not receive all the relevant results for all the associated synonyms. You must specify at least two synonyms and you can specify up to 100 synonyms. Each synonym must be UTF-8 encoded and in lowercase. No duplicate strings are allowed. For example, you can add "pixel", "android phone", and "google phone" as synonyms. For more information, see [`synonymsAction`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#synonymsaction).
  3. Attach the control to the app's serving config using the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/patch) method.
         
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

For field details, see the [`engines.controls` API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls) and the [`engines.controls.create` API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls/create).

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

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
     * `APP_ID`: the ID of the app.
     * `CONTROL_ID`: a unique identifier for the control. The ID can contain [1-63] characters that can be letters, digits, hyphens, and underscores.
     * `DISPLAY_NAME`: the human-readable name for the control. Google recommends that this name provide an indication of when or why to use the control. Must be a UTF-8 encoded string with length [1,128].
     * `USE_CASE`: must be either `SEARCH_USE_CASE_SEARCH` or `SEARCH_USE_CASE_BROWSE`. If `SEARCH_USE_CASE_BROWSE` is specified, then `Condition.queryTerms` can't be used in the condition.
     * `CONDITION`: an optional field that defines when the control should be applied. Contains the following fields: 
       * `VALUE`: the specific query value to match against. It's a lowercase UTF-8 string with length `[1, 5000]`. If `FULL_MATCH_1` is `true`, this field can have at most three space-separated terms.
       * `FULL_MATCH`: a boolean that indicates whether the search query needs to exactly match the query term. When set to `true`, it requires `SearchRequest.query` to completely match the `queryTerm.value`. When set to `false`, it requires `SearchRequest.query` to contain `queryTerm.value` as a substring.
       * `START_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the start of a time range.
       * `END_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the end of a time range.
     * `REDIRECT_URI_N`: a URI where you are redirected. Can have a maximum length of 2000 characters. For example, if the value of the query term is "support", you can set a redirect to your technical support page instead of returning (or failing to return) search results for "support". In this example, the redirect URI becomes `"https://www.example.com/support"`. For more information, see [`redirectAction`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#redirectaction).
  3. Attach the control to the app's serving config using the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/patch) method.
         
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

A promote serving control lets you display a link as a promoted result. This control is available for search apps with structured or unstructured data stores and blended search apps.

For the promote control to take effect, you must attach it to the serving config of the app.

Promote controls are defined using a `promoteAction`.

To successfully create a promote control, you must specify the `queryTerms` field with `fullMatch` set to `true` or `false`.

Use the following instructions to create a promote serving control.

### Console

To create a promote serving control, follow the instructions on the REST tab.

### REST

For field details, see the [`engines.controls` API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls) and the [`engines.controls.create` API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls/create).

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

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
         "promoteAction": {
           "dataStore": "DATA_STORE_RESOURCE_PATH",
           "searchLinkPromotion": {
              "document": "DOCUMENT_RESOURCE_PATH",
              "title": "TITLE",
              "uri": "URI",
              "description": "URI_DESCRIPTION"
           }
          }
         }'

Replace the following:

     * `PROJECT_ID`: the number or ID of your Google Cloud project.
     * `APP_ID`: the ID of the app.
     * `CONTROL_ID`: a unique identifier for the control. The ID can contain [1-63] characters that can be letters, digits, hyphens, and underscores.
     * `DISPLAY_NAME`: the human-readable name for the control. Google recommends that this name provide an indication of when or why to use the control. Must be a UTF-8 encoded string with length [1,128].
     * `USE_CASE`: must be either `SEARCH_USE_CASE_SEARCH` or `SEARCH_USE_CASE_BROWSE`. If `SEARCH_USE_CASE_BROWSE` is specified, then `Condition.queryTerms` can't be used in the condition.
     * `CONDITION`: an optional field that defines when the control should be applied. Contains the following fields: 
       * `VALUE`: the specific query value to match against. It's a lowercase UTF-8 string with length `[1, 5000]`.
       * `FULL_MATCH`: a boolean to indicate whether the query term must be fully matched.
       * `START_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the start of a time range.
       * `END_TIMESTAMP`: a timestamp in RFC 3339 UTC "Zulu" format to indicate the end of a time range.
     * `DATA_STORE_RESOURCE_PATH`: the full resource path of the data store whose search results contain the promoted URL. The format of the full resource path is `projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATA_STORE_ID`. This data store must be attached to the engine specified in the request.
     * `DOCUMENT_RESOURCE_PATH`: a field to specify the resource path of the document to be promoted. You must provide either the document ID in the `DOCUMENT_RESOURCE_PATH` field, the URI in the `URI` field, or both.

The format of the full resource path is: `projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID`.

     * `TITLE`: a required field to specify the title of the document or the web page to be promoted. This title is displayed in the search result.

     * `URI`: a field to specify the URI where the search result leads the user. You must provide either the document ID in the `DOCUMENT_RESOURCE_PATH` field, the URI in the `URI` field, or both.

     * `URI_DESCRIPTION`: an optional field to describe the URI, which is displayed in the search result.

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
    

The response contains promotion control IDs that you need to attach your promote control to your search app.

  3. Attach the control to the app's serving config using the [`engines.servingConfigs.patch`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/patch) method. The order in which you attach the `promoteControlIds` in the following request is the order in which the promoted results are returned.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search?update_mask=promote_control_ids" \
         -d '{
           "promoteControlIds": ["PROMOTE_ID_1", "PROMOTE_ID_2"]
         }'

Replace `PROMOTE_ID_N` with the control IDs that you received in the previous step. 




## Modify serving controls

To modify a control's configuration, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select the app for which you want to modify controls.

  3. Click **Configurations** and then click the **Control** tab.

  4. In the list of the app's controls, click more_vert for a control that you want to modify and click **Edit**.

  5. Edit the control in the **Edit control** pane:

     1. To enable or disable a control, in the list of the app's filter controls, click more_vert for a control that you want to enable or disable and click **Enable** or **Disable** , respectively.

     2. To delete a control, in the list of the app's controls, click more_vert for a control that you want to delete and click **Delete**.




## What's next

  * To understand the impact of a serving control on the search quality of an app, [evaluate search quality](https://docs.cloud.google.com/gemini/enterprise/docs/evaluate-search-quality).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
