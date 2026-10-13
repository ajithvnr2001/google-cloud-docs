---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/conversational-filtering-dev-guide/
title: Conversational filtering developer's guide \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:56.649751+00:00
---

# Conversational filtering developer's guide  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/conversational-filtering-dev-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Conversational filtering developer's guide Stay organized with collections  Save and categorize content based on your preferences. 

The following is a developer's guide on how to integrate conversational product filtering in your API.

## Meet minimum data requirements to activate conversational filtering

To meet the 25% quota required for activating conversational product filtering, you must increase the volume of user events that contain valid filter information. The more filters you upload within your user events, the higher the conversational coverage.

Here are the specific steps and logic to increase coverage:

  * **Upload filters in user events**. You need to increase the input of user-event-applied filters. This ensures that when a user applies a filter like color or price on your site, that action is captured in the filter field of the corresponding search user event sent to AI Commerce Search.

  * **Establish a feedback loop**. The LLM infers facet popularity from these filters. By including corresponding filters in search events when an attribute is marked as dynamically facetable, you initiate the model's learning process. Ideally, your user interface should capture and relay user filter selections in both search requests and events to drive this continuous model refinement.

  * **Monitor data quality advisory checks**. If you have met the initial threshold of 1,000 queries per day but have not reached 25% coverage, the **Data quality** page in the console (under the **Conversation** tab) will provide specific advisory checks. These checks calculate and display the exact percentage by which your user-event-applied filters must increase to reach the coverage goal.

  * **Ensure attribute configuration**. Because the model uses the attributes you're filtering to generate questions, ensure that they're correctly configured in your catalog as indexable and dynamically facetable.




## Administrator experience

Manage the generative questions and conversational product filtering directly in the API, or in the AI Commerce Search in Gemini Enterprise for Customer Experience console, and set it up in the Data quality and Evaluate sections of the AI Commerce Search in Gemini Enterprise for Customer Experience console.

###  Cloud console 

The console allows retailers to manage generative questions in a conversational product filtering experience. Learn more about using generative questions in conversational product filtering.

### Steps to use the generative question service

  1. Satisfy data requirements.

  2. Configure manual question overrides.

  3. Turn the feature on.

  4. Preview and test.




### Data requirements

To find out if your search data is ready for conversational product filtering, in the console, under **Conversational product filtering and browse** , or under **Data quality > Conversation**, go to the **Coverage checks** tab.

To enable conversational product filtering, you need to meet certain data requirements.

These are:

  * **1,000 queries per day** : After you reach this first threshold, a conversation plan is generated that evaluates your inputs and outputs:
  * **Inputs** : filter count in events
  * **Outputs** : conversational coverage
  * **25% conversational coverage** : Calculated by AI Commerce Search models, conversational coverage means the percentage of queries that have one question. A frequency-weighted 25% (by volume) of queries should have at least a first question that matches it.



If you don't have 25% conversational coverage yet, but have the first prerequisite 1000 queries per day, blocking and advisory checks begin to be applied to your outputs and inputs, respectively. Here, AI Commerce Search begins to calculate by how much of a percentage your user-event-applied filters have to increase in order to reach the 25% conversational coverage threshold. The more filters that are uploaded, the higher the coverage reached.

To view your conversational readiness:

  1. Go to the **Conversation** tab in the [Data quality](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data_quality/) page in the AI Commerce Search in Gemini Enterprise for Customer Experience console. This provides you with a critical check of whether a minimum of 25% of search queries have at least one follow-up question, as well as advisory checks as to what percentage of user events with valid filters is needed to reach that conversational coverage goal.



![Conversational readiness](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/convo-filitering-coverage-checks.png)**Figure 1**. Conversational readiness check.

  1. If you pass the critical check, with sufficient user events with valid filters, proceed to the next step.

  2. To control how generative questions are served, go to the [Conversational product filtering and browse page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/conversational_search/) in the AI Commerce Search console.




### Generative question controls

The generative AI writes a question for every indexable attribute in the catalog, using both names and values of attributes for system and custom attributes. These questions are generated by an LLM and aim to enhance the search experience. For example, for furniture type, values can be indoor or outdoor, the AI synthesizes a question about what type of furniture you are looking for.

Each facet has one generated question. Based on historic user events and facet engagement from past search event data, the questions are sorted by expected frequency of the question appearing. The AI first looks at the questions on top, then finds what is relevant by attribute. The list of questions is generated once. If a new attribute is added, it is reflected in the list in two hours.

  1. Go to the **Shopping agent** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Conversational search and browse page.](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/conversational_search/)

  2. Under the **Manage AI generated questions** tab, view all the questions sorted by how often they are used, in query-weighted frequency, meaning how often they are served with common queries. The ranking uses the frequency field in the `GenerativeQuestionConfig` configuration. This field is responsible for sorting the AI-generated questions by how often they are used.

  3. You can use the filter option to filter the questions.

  4. Check the box to enable question visibility for each attribute.

  5. Click _edit_ at the end of each row to open an edit panel for each question.




To make bulk edits, follow these steps:

  1. Select or clear the boxes next to the questions that you want to include or exclude in conversation.

  2. Click either the _add_**Allow in conversation** or the _remove_**Disallow in conversation** buttons that appear at the top of the list. Alternatively, to edit an individual question, click _edit_ and clear or recheck the box next to **Allowed in conversation** in the pane that opens:




![Edit each question](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/edit-questions-flyout.png)**Figure 2**. Edit each AI-generated question.

### Use generative questions in conversational product filtering

The generative question service API provides controls to mitigate potential inconsistencies in the LLM output. These can be managed from the console. Here, retailers can also configure conversational product filtering by toggling its enabled state and setting the minimum number of products required to trigger it.

You can define the questions, specifying the question itself, potential answers, and whether the question is allowed in the conversation. Individual questions can be generated by an LLM or overridden by the retailer. The console supports reviewing AI-generated questions, allowing retailers to override them or toggle their conversational status. Questions can also be bulk edited.

### Edit individual questions

You can also use controls to curate the individual questions. It is recommended to do this before you turn conversational product filtering on.

For each question, there are two options. Click _edit_ in in the last column to access the questions visible to the users panel:

  1. **Turn off a question for all queries** : The question is enabled by default. Clear (or check again) the box next to **Allowed in conversation**. This option skips the question altogether. A retailer can opt to disable a question entirely if it doesn't relate to the queried attributes or could be misconstrued as inappropriate (a question, such as _What dress size are you looking for?_ , might be perceived as prying about weight.)
  2. **Rewrite a question** : In the pane, you can see the AI-generated question, what attribute it is attached to and what values the attribute has. Click the pencil to rewrite it.



### Turn on conversational filtering

After you have edited your generative AI questions in the console, you are ready to turn on conversational product filtering.

To enable conversational product filtering, go to the [Conversational product filtering and browse page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/conversational_search/) in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

  1. Go to the **Shopping agent** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Conversational search and browse page.](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/conversational_search/)

  2. Consider the minimum amount of products in your catalog you want returned in the search before questions are generated. This number can be higher but never lower than 2. One row to a page is often the right amount for triggering a conversation.

  3. Configure the number and switch the toggle to **On**. If fewer products match the number, they get filtered out.




![Switch on](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/conversational-switch-on.png)**Figure 3**. Switch toggle to **Enable conversational search**.

**Note:** If generative AI is enabled and the LLM relates an AI-generated question to any related attribute value, an AI question could appear.

This page provides information as to the status of your blocking and advisory checks. If you have enough search queries with at least one follow-up question, your site is now conversational search-enabled.

### Evaluate and test

**Evaluate** lets you preview the serving experience by running a test search and testing your questions against displayed facets. This part of the console provides you with a preview of your serving experience with conversational product filtering.

To evaluate and test, follow these steps. In the **Evaluate** section on the **Search** or **Browse** tabs on the [Evaluate page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) of the AI Commerce Search in Gemini Enterprise for Customer Experience console.

  1. Go to the **Evaluate** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Evaluate page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/)

  2. Click **Search** or **Browse**.

  3. In the **Search Evaluation** field, enter a test query that makes sense based on the catalog you have uploaded to search, such as _shoes_ if your catalog consists of clothing items.

  4. Click **Search preview** to see search results.




![Evaluate search results](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/conversational-evaluate-tab.png)**Figure 4**. Preview results.

If you have conversational product filtering enabled, generative questions are enabled.

###  Generative Question API 

This section describes how to use the generative question API to integrate the Conversational API into your web interface, manage the generative questions, and serve conversational product filtering on your site.

### API integration

**Objects** :

  * GenerativeQuestionsFeatureConfig
  * GenerativeQuestionConfig
  * GenerativeQuestions Service 
    * UpdateGenerativeQuestionsFeatureConfiguration
    * UpdateGenerativeQuestionConfig
    * ListGenerativeQuestionConfigs
    * GetGenerativeQuestionFeatureConfig
    * BatchUpdateGenerativeQuestionConfigs



The core to integrating conversational product filtering is defining the `question` resource. This includes the question itself and whether the question is allowed in the conversation. The question is by default generated by an LLM but can be overridden by the administrator.

### Enable conversational product filtering

**Object** :

  * GenerativeQuestionsFeatureConfig



This object is a control configuration file for enabling conversational product filtering for generative questions to manage the overall serving experience. `GenerativeQuestionsFeatureConfig` uses a `GET` method to obtain attribute information and whether the attributes are indexable or not from the catalog associated with the project.

The `feature_enabled` switch determines whether questions are used at serving time. It manages the top-level toggles in the console.

**Note:** You **can't** enable conversational product filtering until data requirements are satisfied. If the data requirements aren't met, the API triggers a validation error. The data requirements validation is visible in the AI Commerce Search in Gemini Enterprise for Customer Experience console, which, under the hood, calls the Conversational Configuration API.

#### Enable the feature
    
    
    // Configuration for overall generative question feature state.
    message GenerativeQuestionsFeatureConfig {
    ...
    
    // Resource name of the affected catalog.
    // Format: projects/{project}/locations/{location}/catalogs/{catalog}
    string catalog = 1 [(google.api.field_behavior) = REQUIRED];
    
    // Determines whether questions are used at serving time.
    // Note: You cannot enable this until initial data requirements are
    // satisfied.
    bool feature_enabled = 2 [(google.api.field_behavior) = OPTIONAL];
    
    // Minimum number of products in the response to trigger follow-up questions.
    // Value must be 0 or positive.
    int32 minimum_products = 3 [(google.api.field_behavior) = OPTIONAL];
    }

**Conversation-relevant fields**  
---  
catalog  | string  | The resource name of the affected catalog at the project level. Format: **projects/{project}/locations/{location}/catalogs/{catalog}**.  
feature_enabled  | boolean  | Switches questions on or off. Optional field. It cannot be enabled until data requirements are met. If attempted, it throws an error.  
minimum_products  | Integer32  | Minimum number of products in the response to trigger follow-up questions. Must have a value of 0 or greater.  
  
#### Manage the generative questions

**Object** :

  * `GenerativeQuestionConfig`



A question can be conversation-enabled with the boolean field `allowed_in_conversation`. It controls the configuration for a single generated question.

**Fields (control behaviors for conversation highlighted)**  
---  
catalog  | string  | Used to identify which set of attributes (and by extension questions) are available. These values are all defined in the catalog. Required field.  
facet  | string  | Facet to which a question is associated. Required field.  
generated_question  | string  | The LLM generated default question. Output only.  
**final_question** | string  | The question that is asked. It can have a max length of 300 bytes. Optional field.   
example_values  | Repeated string  | Values that can be used to answer the question. Output only.  
frequency  | float  | The ratio of how often a question was asked. Output only.  
**allowed_in_conversation** | boolean  | Whether the question is asked at serving time. This field is optional.   
  
## Serving experience

Conversational product filtering is based on engaging your user with an ongoing conversation of multiple turns. Therefore, there's at least a second response required for conversational product filtering to work. Your user is presented with a follow-up question and suggested answers in the response, and your user can respond to this follow-up question either by either entering their answer or by clicking on a suggested answer (multiple choice option).

The multiple choice option functions behind the scenes like a facet (an event type filter), which narrows the query using filtering. In the background, when the user clicks on a multiple choice response, a filter is applied to the query. Applying a filter using conversational multiple choice is identical to applying the same filter using dynamic facets or tiles.

### Service enabled by conversational product filtering

The generative questions service (`service GenerativeQuestionService{...}`) is used for managing LLM-generated questions. Its parent object is the catalog, where it retrieves information from to return questions for a given catalog. The service is used to manage the overall generative question state, make individual or batch changes, and toggle questions on or off. Data requirements must be met to interface with the Service API, and the questions must be initialized before the questions can be managed.

The service interacts with the feature-level and question-level configuration files with two sets of handlers:

  * **`GenerativeQuestionsFeatureConfig` handlers (feature-level)**:

    1. **Update** Lets you change minimum products and enable fields.
    2. **Get** Returns an object.
  * **GenerativeQuestion Config handlers (question-level)** :

    1. **List** Returns all questions for a given catalog.
    2. **Update** Performs individual question management.
    3. **Batch Update** Performs grouped question management.



The service returns a semantically appropriate question based on the initial query.

A follow-up question is generated by the LLM model and can be overridden. The questions are displayed based on how likely it is used by customers by calling the search event history. If there is no search event history, the fallback is on the commerce search logs.

Different questions are generated based on the previous query. There are no fixed weights. The AI that drives the LLM-generated questions learns from the queries and changes the weighting for every query, so that "shirt", for example, weighs the category very heavily, but "XL red shirt" weighs category, size and color.

### Configure the serving experience

Configure the serving experience by integrating the conversational filtering configuration API with the Search API.

The configuration API [`ConversationalFilteringSpec`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#conversationalfilteringspec) for the feature sits on top of the [Conversational API](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#conversationalsearchservice). You can either call both APIs in parallel or in this order:

  1. Conversational API
  2. Search API


  * **`ConversationalFilteringSpec`** : This optional field has been added to `ConversationalSearchRequest` but is required if you want to use conversational product filtering. The field reuses the `SearchRequest` fields, query and filter. It also includes a field to enable a follow-up question served to the user after an initial query and a `conversation_id` to maintain the state of the conversation between the client and server.
  * **`ConversationalFilteringResult`** : A proto file contains extra information needed to be returned for the conversational CRS flow in `ConversationalSearchResponse`. This includes a `conversation_id`, `refined_query`, `additional_filters`, `follow_up_question`, and `suggested_answers`.



## User journey in the conversational API

The user initiates a search with an initial query and sets the [`mode`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#mode) flag to `CONVERSATIONAL_FILTER_ONLY`. The user then selects an answer, which is sent back to the API using the `user_answer` field.

The Conversational API provides the [`additional_filter`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#conversationalfilteringresult) field in the response. The user must apply these filters to the Search API follow-up request. The search results are based on the user's input and provide a new follow-up question, prompting a follow-up query and continuing the conversation in multiple turns until the user finds what they're looking for on the retailer website.

**Note:** Conversational product filtering interfaces with two APIs, which include Search and Conversational. The Search API is intended to fetch the search results, and Conversational API is intended to fetch the conversational response. The Conversational API doesn't return search results.

Assuming conversational product filtering is enabled on the website, the user journey and subsequent interaction with AI Commerce Search follows this path:

  * Step 1. First query comes from user to both Search and Conversational API. The Search API only returns search results. The Conversational API returns the suggested answers and follow-up questions. Call the Search API for the same query or `page_category` and fetch the search results. Follow-up conversation requested is sent to conversational search. Call the Conversational API with the right conversation filtering mode.

  * Step 2. Initial search response with search results only. The Conversational API refines the query by returning the suggested answers and follow-up questions. The end user then selects multiple choice:

    * The selected answer filter is sent to the Conversational API.
    * Conversation and Search APIs run with the applied filter.



### Initial user query

The first query is when your user starts a conversation in AI Commerce Search and looks for `dress` in the search box.

  * **User action** : The end user searches for _dress_.
  * **Your implementation** : Make two API calls.
  * **Conversational API request** : 
    * `query`: "dress"
    * `conversational_search_spec`: 
      * `mode`: `"CONVERSATIONAL_FILTER_ONLY"` This is the key parameter.
  * **Search API request** : 
    * `query`: _dress_
  * **Conversational API response** : 
    * `conversation_id`: "c15..." Store this variable.
    * `followup_question`: **What is the color?** question is generated.
    * `suggested_answers`: `[ {name: "colors", value: "yellow"}, {name: "colors", value: "blue"}, ... ]`
  * **Action** : Display the `followup_question` and `suggested_answers` to the user.

**Note:** There are two different API endpoints. The core Search API must be used to fetch search results, and the Conversational API must be used to fetch the conversational experience. Conversational API doesn't return search results.

#### Send request to Search API

Send a request to the Search API by creating the following search request by setting `dress` as the query (or whatever the actual query is):

#### Search API request
    
    
    {
      query: "dress",
      Search_params : {
        "filter": string,
        "canonicalFilter": string,
        "sortBy": string,
        "boostSpec": {
           object (BoostSpec)
        }
      }
    }

There is no change in the search API request as part of the conversational product filtering.

#### Send request to the Conversational API

Send a request to the Conversational API by doing the following:

  * Create a conversational search request by setting `dress` as the query (or whatever the actual query is).

  * Set `mode` to `CONVERSATIONAL_FILTER_ONLY` in order to get a conversational response. If it's set to `DISABLED`, no follow-up question is supplied.

  * Populate `SearchParams` in the conversational search request. The search parameters should be the same as the Search API call.




#### Conversational API request
    
    
    {
      "query": "dress",
      "conversational_search_spec":  {
        "mode": "CONVERSATIONAL_FILTER_ONLY"
      }
    }

#### Conversational API response

Your response from the Conversational API then looks like this:

#### Conversational API request
    
    
    {
      conversation_id: "c154d073-87f5-4edb-accd-587eabe014ff"
      refined_query: "dress"
      conversational_filtering_result: {
        followup_question{
          followup_question: "What is the color?"
          suggested_answers {
            product_attribute_value {
              name: "colors",
              value: "yellow"
            }
          }
        suggested_answers {
          product_attribute_value {
            name: "colors",
            value: "blue"
          }
        }
        suggested_answers {
          product_attribute_value {
            name: "colors",
            value: "red"
          }
        }
       }
      }
    }

What you should do with the response:

  * **`conversation_id`** : This ID can be stored in the browser session storage and can be used to continue the conversational search with the server. Because one shopper might have multiple tabs open with more than one conversation, the `conversation_id` is used to track the conversations.
  * **`refined_query`** : Identifies the current query. You must use this response to call the Search API to fetch the product results.
  * **`followup_question`** : Identifies the question to show to the user.
  * **`suggested_answers`** : An ordered list of the multiple-choice answers that should be shown to your users. If you want to show fewer answers, just show the first N results. The list is sorted in the order the results should be shown.



The initial query then has the conversation enabled.

#### Conversational API request
    
    
    {
      "query": "dress",
      "conversational_search_spec":  {
        "mode": "CONVERSATIONAL_FILTER_ONLY"
      }
    }

### Search handles multiple choice answers

  * **User action** : Clicks **yellow**.
  * **Your implementation** : Make two new API calls.
  * **Conversational API request** : 
    * `query`: _dress_
    * `conversation_id`: `"c15..."` Use the stored ID.
    * `user_answer`: { `selected_answer`: { `product_attribute_value`: { name: "colors", value: "yellow" } } }
  * **Search API request** : 
    * `query`: _dress_.
  * **Conversational API response** : 
    * `additional_filter`: { `product_attribute_value`: { name: "colors", value: "yellow" } }
    * `followup_question`: **What is the occasion?**
  * **Action** : Use `additional_filter` to update the web interface, such as check the **yellow** filter box, and display the new question.



#### Conversational API response
    
    
    {
      conversation_id: "c154d073-87f5-4edb-accd-587eabe014ff"
      refined_query: "dress"
      conversational_filtering_result: {
        followup_question{
          followup_question: "What is the color?"
          suggested_answers {
            product_attribute_value {
              name: "colors",
              value: "yellow"
            }
          }
        suggested_answers {
          product_attribute_value {
            name: "colors",
            value: "blue"
          }
        }
        suggested_answers {
          product_attribute_value {
            name: "colors",
            value: "red"
          }
        }
       }
      }
    }

  * `conversational_filtering_result` is a field that relates to [`ConversationalFilteringResult`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#conversationalfilteringresult) is a proto that contains extra information returned from the conversational flow. The `conversational_filtering_result` field in `ConversationalSearchResponse` provides supplementary data that is crucial for user interface rendering. The `conversational_filtering_result` field uses nested messages, such as `SuggestedAnswer` and [`AdditionalFilter`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#additionalfilter) to structure the returned data in a clear and comprehensible manner. This hierarchical structure ensures that the information exchanged between the client and server is well-defined and interpretable.
  * The suggested answers are sorted by which facet values in the catalog were most often engaged in the user events as filters for all queries. The sorting uses the `engagement_rate` field in the follow-up question generated by the [`ConversationalSearch`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.ConversationalSearchService) service. This field captures the historical engagement rate that the filter shows from the retailer's search events sent to the server.
  * All the other fields are unchanged when conversation is used.



**What to do with the initial conversational search return**

  * On the client side, developers should store the `conversation_id` in browser session storage so that this can be used to continue the conversational search with the server.
  * This is used to keep track of the ongoing conversation, since one shopper could have multiple tabs open with multiple running conversations.


* `refined_query` tells the retailer what the current query is.

  * This should be used if the retailer wants to show the current query to the user.


* `followup_question` tells the retailer what question to show to the user
* `suggested_answers`.

  * This is an ordered list of the multiple choice answers that should be shown to the users. 
  * If you want to show fewer than the full list, just show the first N results
  * This list is sorted, so it must be shown in the proper order. In other words, the first result to show is the first one listed.



Conversational product filtering serves these options for continued conversational engagement, leading to faster search refinement:

When your user is served search results, they can select a multiple-choice option.

This code sample demonstrates that the user selected the multiple choice answer _yellow,_ and a new conversational request is sent to the Search API by sending the query again along with the correct user filter applied.

#### Search API request
    
    
    {
      query: "dress",
      "search_params": {
        "boost_spec": {},
        "canonical_filter": "",
        "filter": "colors: ANY("yellow")"
        "sort_by": ""
      }
    }

To send a request to the Conversational API:

  1. Restore the `conversation_id` from session storage.
  2. Set `mode` to be `CONVERSATIONAL_FILTER_ONLY`.
  3. Set `user_answer` for what the user selects.



#### Conversational API request
    
    
    {
      query: "dress"
      conversation_id: "c154d073-87f5-4edb-accd-587eabe014ff"
      conversational_search_spec {
        "mode": "CONVERSATIONAL_FILTER_ONLY"
        user_answer {
          selected_answer {
            product_attribute_value {
              name: "colors"
              value: "yellow"
            }
          }
        }
      }
    }

The response from the Conversational API then looks like this:

#### Conversational API response
    
    
    {
      conversation_id: "c154d073-87f5-4edb-accd-587eabe014ff"
      refined_query: "dress"
      conversational_filtering_result {
        additional_filter {
          product_attribute_value {
            name: "colors",
            value: "yellow"
          }
        }
        followup_question{
        followup_question: "What is the occasion?"
        suggested_answers {
          product_attribute_value {
            name: "attribute.occasion",
            value: "wedding"
          }
        }
        suggested_answers {
          product_attribute_value {
            name: "attribute.occasion",
            value: "party"
          }
        }
      }
     }
    }

What you should do with the response:

  * The Google response is basically identical to the response to the first query, except the `additional_filter` field can be used to check off the filter box for `color = yellow` and should be added to any other filters that the user has selected.
  * The `additional_filter` should also be added to the filter field event sent to Google for this follow-up query and the follow-up search request. It should be applied in the search request to fetch search products and should also be applied to the conversational search request to fetch the follow-up conversation.
  * The `refined_query` should be sent to the Search API to fetch more relevant products.



## Implement product filters

This section serves as a guide for users to implement conversational product filtering at the API level. The starting (neutral) state is a landing page, likely with a search bar, recommendations, or marketing campaigns, depending on your AI Commerce Search application. Calls haven't been made to the Search or the Conversation API.

### Starting state

This is the landing page for the user interface, for recommendations or campaigns. No Search for Conversational API calls have been made yet.

![User enters query and calls AI Commerce Search APIs](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/1-conversational-filtering-implementation-Neutral-State.png)

### User enters a query

Enter a query, such as _lipstick,_ to issue parallel calls to the Search and Conversation APIs.

![User enters query and calls AI Commerce Search APIs](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/2-user-types-query-lipstick.png)

### Search and conversation serve first question

The API responses appear, including an initial question and a set of answer options. The responses from the Conversational and Search APIs to the initial user query are respectively asynchronous.

![Response from search and conversation APIs](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/3-response-from-search-and-convo.png)

![User presented with options](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/4-what-brand.png)

### User selects a presented answer or filter facet

The user selects a presented answer or filter facet.

![User selects presented answer or filter facet](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/5-user-selects-brand.png)

The user selection then issues a second call to both APIs with the user's filter facet or answer.

![Parallel calls to search and conversation APIs with user answer](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/6-user-answer-parallel-calls.png)

### APIs serve follow-up question

The Search and Conversation APIs both respond asynchronously to serve another question and presented answer options.

![User selects presented answer or filter facet](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/7-user-selection-round-2.png)

The user sees the next question and a set of answer options to the next question.

![User sees next question and selects presented answer to next question](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/8-what-color.png)

### Edge cases

There are a few other possible scenarios that are covered by the implementation.

#### User enters a new query

If the user is in the midst of entering a conversation filter for a query, such as _lipstick,_ the web interface has already been populated with the API's initial response. However, when the user enters a new query, such as _sunscreen_ , a new conversation starts. If this happens, the API implementation reverts back to a new query, but with an empty `conversation_id` field. This new query regenerates a new response and, in turn, repopulates the web interface with a new respective response.

![User changes query mid-conversation](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/user-changes-query.png)

#### User deselects a facet filter or previously answered question

If the user is in an interface that was already populated with the response from a previous query, but deselects the selected facet filter or answer, a new conversation session is initiated with `searchParam` filters. The reason is that the user is breaking out of the current conversation flow.

![User deselects previous selection](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/user-deselects.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
