---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-advanced-autocomplete/
title: Configure advanced autocomplete \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:57:47.946566+00:00
---

# Configure advanced autocomplete  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-advanced-autocomplete/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure advanced autocomplete Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Gemini Enterprise's advanced autocomplete feature.

In the same way as basic autocomplete, advanced autocomplete generates query suggestions based on the first few characters entered for the query.

Before reading this page, become familiar with Gemini Enterprise's basic autocomplete. See [Configure autocomplete](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete).

## Key features of advanced autocomplete

The key features of advanced autocomplete that distinguish it from the basic autocomplete are as follows:

  * **Blended search:** Advanced autocomplete can be used with apps that are connected to more than one data store.

  * **Access control:** Advanced autocomplete respects access controls. (Access controls are also referred to as ACLs, access control lists.) Advanced autocomplete only suggests search queries that are related to documents that the searcher has access to. For information about access control, see [Identity and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/identity).



  * **Language boost:** Advanced autocomplete can be set to boost suggestions in one or more languages. For example, if the browser language is Dutch, autocomplete suggestions in that language could be boosted. For more information, see Send an autocomplete request with a language boost.


  * **Different types of suggestions:** With advanced autocomplete, instead of regular autocomplete query suggestions, you can specify that you want different types of suggestions:

    * **Rich suggestions:** As autocomplete suggestions, users get information about documents where the titles prefix-match the letters that they type. For more information, see Send an autocomplete request and return rich suggestions.

    * **Recent queries:** As autocomplete suggestions, users get their recent queries that prefix-match the letters that they type. For more information, see Send an autocomplete request and return recent queries.




## Before you begin

Before you begin to use advanced autocomplete, do the following:

  * Review and optionally edit the autocomplete settings for your app. See [Update autocomplete settings](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete#update-autocomplete).

  * For smaller data stores, set **Enable autocomplete** to **Now**. We recommend this because small data stores might not contain sufficient data to provide accurate suggestions.

  * If your data stores contain any personally identifiable information (PII) or if you use the search history or user events query suggestions model, review [Protect against PII leaks](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete#pii) and set up data loss prevention (DLP) safeguards that might be needed to prevent leaks of PII.

  * If you plan to use recent search suggestions (`RECENT_SEARCH`), ensure that you record search user events. Gemini Enterprise doesn't automatically populate the recent search index when searches are performed using the [`SearchService.Search`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method. To return recent queries, you must record search user events by using the [`userEvents.write`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/write) method. See Before you begin for recent queries.




## Send autocomplete requests

The following shows how to send advanced autocomplete requests using the [`completionConfig.completeQuery`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.completionConfig/completeQuery) method.

### REST

To send an autocomplete request using the API, follow these steps:

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Call the [`completionConfig.completeQuery`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.completionConfig/completeQuery) method.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/completionConfig:completeQuery" \
         -d '{
               "query":"QUERY_STRING"
             }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.

     * `APP_ID`: the ID of the app.

     * `QUERY_STRING`: the typeahead input used to fetch suggestions.




## Send an autocomplete request with a language boost

You can boost or bury autocomplete suggestions according to language code, for example, make autocomplete suggestions in some languages more or less likely to appear.

The boost value must be between -1 and 1. Setting a negative number "buries" autocomplete suggestions in that language and a positive number boosts the language.

Use two-letter language tags defined by BCP 47—for example, `en`, `fr`, `hi`, and `zh`.

### REST

To send an autocomplete request that includes a language boost value, follow these steps:

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Call the [`completionConfig.completeQuery`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.completionConfig/completeQuery) method.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/completionConfig:completeQuery" \
         -d '{
               "query":"QUERY_STRING",
               "boostSpec": {
                  "conditionBoostSpecs": [{
                    "condition": "(langCode: ANY(LANG_CODE))",
                    "boost": BOOST_VALUE
                  }]
               }
             }'
         
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.

     * `APP_ID`: the ID of the app.

     * `QUERY_STRING`: the typeahead input used to fetch suggestions.

     * `LANG_CODE`: the two-letter code for one or more languages, in escaped quotes. For example, `\"fr\", \"es\"` to apply the boost value to Spanish and French.

     * `BOOST_VALUE`: a floating point number between -1 and 1. When the value is negative, autosuggestions in the language are demoted (they appear lower down in the list of suggestions). When the value is positive, suggestions are promoted (they appear higher up in the list).

#### Example command
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/completionConfig:completeQuery" \
    -d '{
         "query": "hol",
         "boostSpec": {
            "conditionBoostSpecs": [{
              "condition": "(langCode: ANY(\"es\", \"fr\"))",
              "boost": 0.75 }, {
              "condition": "(langCode: ANY(\"en\"))",
              "boost": -1
            }]
          }
        }'
     

In this example, the autocomplete suggestions for the query `Co` are boosted (placed higher in the autosuggestion list) if they are in French or Spanish and buried (placed lower in the autosuggestion list) if they are in English.




## Send an autocomplete request and return rich suggestions

Rich autocomplete returns content (documents) where the titles contain words that start with the query.

In addition to the title for the document, the autocomplete request returns the `source_type` and `entity_type`, and, if available, the key properties: `uri`, `create_time`, and `update_time`. You can view and edit key property mappings on the **Schema** tab of the data store page.

As with all advanced autocomplete suggestions, ACLs are respected for any suggested documents.

### Example

An employee is querying their company intranet site looking for technical information about access permissions.

The employee begins typing `tec`, and the following documents might be returned: `Data technicians handbook`, `Access technology guide`, and `Techniques for troubleshooting access issues`.

With rich suggestions, for each of these suggested documents, you can display the following information about the document:

  * the document title (`title`), a link to the document (`uri`)

  * when it was last updated (`update_time`)

  * the source (`source_type`), for example, whether the document was found in Confluence Cloud or Slack.




Knowing how recently a document was updated and the source for the document helps the employee choose which document to look at first.

### Limitations

Rich autocomplete only applies to third-party connectors and only to certain entity data stores for those third-party connectors. The following table shows which entities are supported for which connectors.

Third-party connector | Entities supported  
---|---  
**Box** | File |  |  |   
**Confluence Cloud** | Page | Space |  |   
**Dropbox** | File |  |  |   
**Jira Cloud** | Issue | Space |  |   
**OneDrive** | File |  |  |   
**Salesforce** | Account | Lead | Opportunity |   
**ServiceNow** | Incident | Knowledge |  |   
**Sharepoint Online** | Attachment | Event | File | Page  
**Slack** | Message |  |  |   
  
### Procedure

To send an autocomplete request that returns a rich suggestion, follow these steps:

### REST

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Call the [`completionConfig.completeQuery`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.completionConfig/completeQuery) method.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/completionConfig:completeQuery" \
         -d '{
               "query":"QUERY_STRING",
               "suggestionTypes": ["CONTENT"]
             }'
         
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.

     * `APP_ID`: the ID of the app.

     * `QUERY_STRING`: the typeahead input used to fetch suggestions.

#### Example command and result
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1/projects/1234/locations/global/collections/default_collection/engines/my_app/completionConfig:completeQuery" \
    - d {
          "query": "C",
          "suggestionTypes": ["CONTENT"]
        }'
    
    
    * * *
    
    
    {
      "contentSuggestions": [{
        "suggestion": "critical crash in payment module",
        "document": {
          "name": "projects/1234/locations/global/collections/default_collection/dataStores/my_data_store/branches/0/documents/10000",
          "derivedStructData": {
            "title": "Critical Crash in Payment Module",
            "uri": "https://cymballabs.atlassian.net/browse/CPT-1",
            "source_type": "jira",
            "entity_type": "issue"
          }
        },
        "dataStore": "projects/1234/locations/global/collections/default_collection/dataStores/my_data_store"
      }]
    }
    
    


**Note:** If you specify `suggestionTypes` as `CONTENT`, then any `boostSpec`, [`queryModel`](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete#diff-model), or [`includeTailSuggestions`](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete#tail-match-suggestions) parameters in your curl command are ignored.

## Send an autocomplete request and return recent queries

Return, as suggestions, a list of the user's most recent queries that prefix-match the query in the request.

The matching query suggestions are listed from the most recent to the oldest. To use recent search, the user pseudo ID must be provided.

**Important:** Gemini Enterprise doesn't automatically record search queries executed using the [`SearchService.Search`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method into a user's recent search history. To return recent queries, you must record search user events. For details, see Before you begin.

### Before you begin

Before you can retrieve recent queries with autocomplete, you must record user searches as search user events by calling the [`userEvents.write`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/write) method.

If search user events are not written, requests to `completionConfig.completeQuery` with `suggestionTypes: ["RECENT_SEARCH"]` return an empty list of suggestions (`{}`).

To record a search user event, send a POST request to the [`userEvents.write`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/write) method with the following values:

  * `eventType`: set to `"search"`
  * `userPseudoId`: set to the user's unique pseudonymized identifier
  * `engine`: set to the resource name of your engine
  * `searchInfo.searchQuery`: set to the search query string entered by the user


    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/userEvents:write" \
      -d '{
            "eventType": "search",
            "userPseudoId": "USER_PSEUDO_ID",
            "engine": "projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID",
            "searchInfo": {
              "searchQuery": "SEARCH_QUERY"
            }
          }'
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `LOCATION`: the location of your app or data store (for example, `global` or `us`).
  * `APP_ID`: the ID of the app.
  * `USER_PSEUDO_ID`: a pseudonymized identifier of the user. This must match the `userPseudoId` passed in subsequent `completionConfig.completeQuery` requests.
  * `SEARCH_QUERY`: the query string searched by the user.



For more information, see [Record real-time user events with the `userEvents.write` method](https://docs.cloud.google.com/gemini/enterprise/docs/record-user-events#record-with-userevents-write-method).

### Example

An employee is querying their company intranet site to get information about taking vacations. The employee has performed the following queries, listed from most recent to oldest:

`PTO`, `Vacation blackout periods`, `How much vacation time do I have?`, `Time off`, `Vacation policy`, `covering a vacant position during absences`, and `Can I take unpaid time off?`.

Now, in response to the employee typing `vac` in the search box, the autocomplete suggestions would be as follows:

  * `Vacation blackout periods`
  * `How much vacation time do I have?`
  * `Vacation policy`
  * `Covering a vacant position during absences`



### Procedure

To send an autocomplete request that returns the user's most recent queries, follow these steps:

### REST

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Call the [`completionConfig.completeQuery`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.completionConfig/completeQuery) method.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/completionConfig:completeQuery" \
         -d '{
               "query":"QUERY_STRING",
               "suggestionTypes": ["RECENT_SEARCH"],
               "userPseudoId": "USER_PSEUDO_ID"
             }'
         
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.

     * `APP_ID`: the ID of the app.

     * `QUERY_STRING`: the typeahead input used to fetch suggestions.

     * `USER_PSEUDO_ID`: a pseudonymized identifier of the user. You can use an HTTP cookie for this field, which uniquely identifies a visitor on a single device. Don't set this field to the same identifier for multiple users. This would combine their query histories. Don't include personally identifiable information (PII) in this field.

#### Example command and result
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/completionConfig:completeQuery" \
    -d '{
          "query": "hol",
          "suggestionTypes": ["RECENT_SEARCH"],
          "userPseudoId": "test_user"
        }'
    
    
    * * *
    
    
    {
      "recentSearchSuggestions": [
        {
          "suggestion": "holiday readiness",
          "recentSearchTime": "2025-05-19T18:27:07.261698Z"
        },
        {
          "suggestion": "holiday freeze",
          "recentSearchTime": "2025-05-19T18:25:45.744021Z"
        },
        {
          "suggestion": "holiday",
          "recentSearchTime": "2025-05-19T18:20:08.916884Z"
        }
      ]
    }
    


**Note:** If you specify `suggestionTypes` as `RECENT_SEARCH`, then any `boostSpec`, [`queryModel`](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete#diff-model), or [`includeTailSuggestions`](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete#tail-match-suggestions) parameters in your curl command are ignored.

## Use an autocomplete denylist

You can use a denylist to prevent specific terms from appearing as autocomplete suggestions.

Although advanced autocomplete is at the app-level, denylists are at the data-store-level. This is significant if your app is a blended search app. Create a denylist for each data store connected to the app.

For information about creating and using denylists, see [Use an autocomplete denylist](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete#denylist).

## Use an imported list of autocomplete suggestions

You can choose to provide your own list of autocomplete suggestions instead of using autocomplete suggestions generated from an autocomplete data model.

For information about how to import a list, see [Use an imported list of autocomplete suggestions](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete#imported-suggestions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
