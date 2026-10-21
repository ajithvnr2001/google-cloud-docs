---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search/
title: Search with follow-ups \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:09.741930+00:00
---

# Search with follow-ups  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Search with follow-ups Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** Search with follow-ups is based on the [`converse`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.conversations/converse) method. There is a newer method, the answer method, which has the same capabilities and more. For more information, see [Get answers and follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer).

This page introduces search with follow-ups for Agent Search and shows you how to implement it using API calls.

If you want to add search with follow-ups to the search widget, see [Configure results for the search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes#display-unstructured).

Search with follow-ups applies to search apps with [unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#unstructured-data) and [websites](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#websites).

## About search with follow-ups

Search with follow-ups is based on generative AI models. Search with follow-ups is different from the [regular unstructured data search](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#structured-unstructured) because search with follow-ups takes into account previous queries in the same search session.

Search with follow-ups supports the following:

  * **Natural language query processing:** It processes and understands human language input, identifies the intent behind a query, and returns relevant results.

  * **Context awareness:** It understands the context of prior interactions and provides context-aware answers.

  * **Multi-turn:** It allows users to ask follow-up questions and receive relevant responses.




### Example of search with follow-ups

The following is an example of search with follow-ups. Suppose that you want to know about vacationing in Mexico:

  * **You:** When is the best time of the year to vacation in Mexico?

  * **Search with follow-ups:** The best time to vacation in Mexico is during the dry season, which runs from November to April.

  * **You:** What is the exchange rate?

  * **Search with follow-ups:** 1 USD is equal to approximately 17.65 Mexican pesos.

  * **You:** What's the average temperature in December?

  * **Search with follow-ups:** The average temperature varies from 70-78°F. Cancun's average is ~ 77°F.




With regular search, your question "What is the exchange rate"? wouldn't be answerable because regular search wouldn't know that you wanted the Mexican exchange rate. Similarly, a regular search wouldn't maintain context to give you temperatures for Mexico.

### About conversations

In search with follow-ups, a conversation is made up of text queries provided by a user and responses provided by Agent Search.

These query and response pairs are sometimes referred to as _messages_. In the preceding example, the second message is made up of "What is the exchange rate?" and "1 USD is equal to approximately 17.65 Mexican pesos."

The conversations are stored in the same data store where the unstructured data is kept. In the data store, a conversation is represented by the [Conversation resource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations). In addition to containing the query and response messages, the conversation resource has:

  * A unique name (the conversation ID).

  * A state (in-progress or completed).

  * A user pseudo ID, which is a visitor ID that tracks the user. It can be assigned programmatically.

  * A start time and an end time.




## Before you begin

Make sure you satisfy the following prerequisites. Requirements vary depending on the type of app you have.

  * If you have an unstructured search app, make sure the [Generative response](https://docs.cloud.google.com/generative-ai-app-builder/docs/advanced-llm) option is turned on.

  * If you have a website search app, make sure the following are turned on:

    * [Enterprise edition features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#enterprise-features)

    * [Generative responses](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#generative-response-features)

    * [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing)




## Store conversations and get responses

You can use the command line or client libraries to generate search responses and to store the search-with-follow-ups conversation.

### REST

To use the command line to create a conversation and generate responses from the user's input, follow these steps:

  1. Specify the data store where you want to store the conversation history:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations" \
         -d '{
           "user_pseudo_id": "USER_PSEUDO_ID"
         }'
         

     * PROJECT_ID: The project number or ID of your Google Cloud project

     * DATA_STORE_ID: The ID of the data store that is associated with your app.

     * USER_PSEUDO_ID: This is a unique identifier for tracking a search visitor. For example, you can implement this with an HTTP cookie, which uniquely identifies a visitor on a single device.

Click for an example response from the `POST` command.
    
    {
      "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/conversations/11078281986791420687",
      "state": "IN_PROGRESS",
      "userPseudoId": "test_id",
      "startTime": "2023-08-15T20:08:12.094639Z"
    }

  2. Generate a search response and add it to a new or existing conversation in your data store:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID:converse" \
         -d '{
           "query": { "input": "FREE_TEXT"},
           "filter": "FILTER"
         }'
         

     * PROJECT_ID: The project number or ID of your Google Cloud project

     * DATA_STORE_ID: The ID of the data store that is associated with your app.

     * CONVERSATION_ID: A unique ID for the conversation, for example, `123456`. For a search-with-follow-ups conversation, use the same conversation ID in every turn.

     * FREE_TEXT: A free text string that contains the user's question—for example, `what is bigquery?`

     * FILTER: A text field for filtering search using a filter expression. The default value is an empty string. The way you construct your filter varies depending on whether you have website data or unstructured data with metadata. For more information, see Filter search with follow-ups.

Click for an example response from the `POST` command.
    
    {
    "reply": {
    "summary": {
      "summaryText": "BigQuery is a cloud-based data warehouse that enables businesses to analyze all their data very quickly. It is a fully managed service that provides a simple and cost-effective way to store and analyze large amounts of data."
    }
    },
    "conversation": {
    "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/conversations/11078281986791420687",
    "state": "IN_PROGRESS",
    "userPseudoId": "test_id",
    "messages": [
      {
        "userInput": {
          "input": "what is bigquery?"
        }
      },
      {
        "reply": {
          "summary": {
            "summaryText": "BigQuery is a cloud-based data warehouse that enables businesses to analyze all their data very quickly. It is a fully managed service that provides a simple and cost-effective way to store and analyze large amounts of data."
          }
        }
      }
    ],
    "startTime": "2023-08-15T20:08:12.094639Z"
    },
    "searchResults": [
    {
      "id": "c86f19582746b56f71c9bb6929893835",
      "document": {
        "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/branches/0/documents/c86f19582746b56f71c9bb6929893835",
        "id": "c86f19582746b56f71c9bb6929893835",
        "derivedStructData": {
          "link": "gs://aquamuse-data-ucs-eval-dev/documents/94627ee0249dfdfda25b1b158c717bca.txt",
          "snippets": [
            {
              "snippet_status": "SUCCESS",
              "snippet": "For larger websites, talk to the IT team and/or utilize a big data solution such as Google \u003cb\u003eBigQuery\u003c/b\u003e to extract all URLs. It may also be necessary to ask the ..."
            }
          ],
          "extractive_answers": [
            {
              "content": "Alternatively, load the Server Log Files into Google BigQuery and use the Google BigQuery interface or the 360 Data Studio to analyze the data. To monitor the indexation numbers of the HTTP and the HTTPS version, keep an eye on all submitted XML Sitemaps."
            }
          ]
        }
      }
    },
    {
      "id": "774bd7ce2a3509ab4bbd1fc876f39dc2",
      "document": {
        "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/branches/0/documents/774bd7ce2a3509ab4bbd1fc876f39dc2",
        "id": "774bd7ce2a3509ab4bbd1fc876f39dc2",
        "derivedStructData": {
          "snippets": [
            {
              "snippet": "No snippet is available for this page.",
              "snippet_status": "NO_SNIPPET_AVAILABLE"
            }
          ],
          "extractive_answers": [
            {
              "content": "This consists of a collection of virtual tables. A virtual table exists for every queryable object type (content type if you prefer) in the repository. Each row in these virtual tables correspond to an instance of the corresponding object type (or of one of its subtypes)."
            }
          ],
          "link": "gs://aquamuse-data-ucs-eval-dev/documents/28841ef8590a105e9415f1390648a811.txt"
        }
      }
    },
    {
      "id": "3e1d306e49aefd9e23f2d5f7a66e6c76",
      "document": {
        "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/branches/0/documents/3e1d306e49aefd9e23f2d5f7a66e6c76",
        "id": "3e1d306e49aefd9e23f2d5f7a66e6c76",
        "derivedStructData": {
          "snippets": [
            {
              "snippet": "No snippet is available for this page.",
              "snippet_status": "NO_SNIPPET_AVAILABLE"
            }
          ],
          "extractive_answers": [
            {
              "content": "Other logo switches are based on search terms. For instance, if the term "ASCII art" is searched, an ASCII art version of the Google logo will appear next to the search box."
            }
          ],
          "link": "gs://aquamuse-data-ucs-eval-dev/documents/98008df3eef5d3ee1661c52f23189190.txt"
        }
      }
    },
    {
      "id": "cf94e24aacd47cd2c2f5effcbdeda832",
      "document": {
        "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/branches/0/documents/cf94e24aacd47cd2c2f5effcbdeda832",
        "id": "cf94e24aacd47cd2c2f5effcbdeda832",
        "derivedStructData": {
          "extractive_answers": [
            {
              "content": "The company is listed on the NASDAQ stock exchange under the ticker symbols GOOGL and GOOG, and on the Frankfurt Stock Exchange under the ticker symbol GGQ1. These ticker symbols now refer to Alphabet Inc., Google's holding company, since the fourth quarter of 2015."
            }
          ],
          "snippets": [
            {
              "snippet": "No snippet is available for this page.",
              "snippet_status": "NO_SNIPPET_AVAILABLE"
            }
          ],
          "link": "gs://aquamuse-data-ucs-eval-dev/documents/d80204083ef1096799fa4b7257548b33.txt"
        }
      }
    },
    {
      "id": "05bc6497a4e7e6ca36b2e495b354b764",
      "document": {
        "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/branches/0/documents/05bc6497a4e7e6ca36b2e495b354b764",
        "id": "05bc6497a4e7e6ca36b2e495b354b764",
        "derivedStructData": {
          "extractive_answers": [
            {
              "content": "SQL injection countermeasures are designed to utilize secure programming methods. By changing the variables used by the application code, weaknesses in applications can be greatly minimized. This report will detail how to perform a SQL injection and explore the best countermeasures to prevent the attack."
            }
          ],
          "link": "gs://aquamuse-data-ucs-eval-dev/documents/7cba75d646f5774a21d96801bec68bb3.txt",
          "snippets": [
            {
              "snippet_status": "NO_SNIPPET_AVAILABLE",
              "snippet": "No snippet is available for this page."
            }
          ]
        }
      }
    }
    ]
    }

  3. Repeat step 2 for each new question in the conversation.




### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
    # data_store_id = "YOUR_DATA_STORE_ID"
    # search_queries = ["YOUR_FIRST_SEARCH_QUERY", "YOUR_SECOND_SEARCH_QUERY"]
    
    
    def multi_turn_search_sample(
        project_id: str,
        location: str,
        data_store_id: str,
        search_queries: List[str],
    ) -> List[discoveryengine.ConverseConversationResponse]:
        #  For more information, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        client_options = (
            ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
            if location != "global"
            else None
        )
    
        # Create a client
        client = discoveryengine.ConversationalSearchServiceClient(
            client_options=client_options
        )
    
        # Initialize Multi-Turn Session
        conversation = client.create_conversation(
            # The full resource name of the data store
            # e.g. projects/{project_id}/locations/{location}/dataStores/{data_store_id}
            parent=client.data_store_path(
                project=project_id, location=location, data_store=data_store_id
            ),
            conversation=discoveryengine.Conversation(),
        )
    
    
        for search_query in search_queries:
            # Add new message to session
            request = discoveryengine.ConverseConversationRequest(
                name=conversation.name,
                query=discoveryengine.TextInput(input=search_query),
                serving_config=client.serving_config_path(
                    project=project_id,
                    location=location,
                    data_store=data_store_id,
                    serving_config="default_config",
                ),
                # Options for the returned summary
                summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
                    # Number of results to include in summary
                    summary_result_count=3,
                    include_citations=True,
                ),
            )
            response = client.converse_conversation(request)
    
            print(f"Reply: {response.reply.summary.summary_text}\n")
    
            for i, result in enumerate(response.search_results, 1):
                result_data = result.document.derived_struct_data
                print(f"[{i}]")
                print(f"Link: {result_data['link']}")
                print(f"First Snippet: {result_data['snippets'][0]['snippet']}")
                print(
                    "First Extractive Answer: \n"
                    f"\tPage: {result_data['extractive_answers'][0]['pageNumber']}\n"
                    f"\tContent: {result_data['extractive_answers'][0]['content']}\n\n"
                )
            print("\n\n")
    

## Filter search with follow-ups

When making a query with search with follow-ups, you can include the `filter` field to restrict the pool of documents from which a response is derived. You construct your filter using filter expressions. The filter expressions that you use vary depending on whether you have website data or unstructured data with metadata.

### Filter expressions for website data

If you have a data store with website data, you can filter your search with follow-ups query using the filter expressions in [Filter expressions with advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search#filter-expressions-advanced-indexing). After you construct your filter expression, use it for the value of the `filter` field in step 2 of Store conversations and get responses.

### Filter expressions for unstructured data with metadata

If you have a data store with unstructured data with metadata, you can filter your search with follow-ups query so that it returns documents based on the metadata fields that the documents contain. See [Filter search for structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata) to understand how to use metadata to filter ordinary search (without follow-ups). You can use these same principles to use metadata to filter search with follow-ups. After you construct your filter expression, use it for the value of the `filter` field in step 2 of Store conversations and get responses.

## Configure the summary

The response message from search with follow ups is a generated summary returned in `summaryText`. There are various ways that you can configure the generated summary. These are described in the following sections:

  * Get citations with search results
  * Ignore adversarial queries
  * Ignore non-summary seeking queries
  * Set the number of results to use in the summary
  * Get customized summaries
  * Apply SafeSearch to chat responses



### Get citations with search results

Citations, when specified, are numbers that are placed inline in a search summary. These numbers indicate from which search results specific sentences in the summary are taken.

To get citations:

  * Follow the preceding Store conversations and get chat responses procedure except at step 2, run this command that includes the `summarySpec` field that sets `includeCitations` to true.
        
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID:converse" \
        -d '{
          "query": { "input": "FREE_TEXT"},
          "summarySpec": { "include_citations": true }
        }'
        

Click for part of the response from an example command.
        
        {
        "reply": {
        "summary": {
        }
        "reply": {
        "summary": {
          "summaryText": "BigQuery is a cloud-based data warehouse that enables businesses to analyze all their data very quickly [1]. It is a fully managed service that provides a simple and cost-effective way to store and analyze large amounts of data [2, 3].",
          "safetyAttributes": {
            "categories": [
              "Finance",
              "Legal"
            ]
        …




Citation numbers are included in summary text. The citation numbers refer to the returned search results and are 1-indexed. For example, `[1]` means that the sentence is attributed to the first search result. `[2, 3]` means that the sentence is attributed to both the second and third search results.

### Ignore adversarial queries

Adversarial queries include negative comments or are designed to generate unsafe, policy-violating output. You can specify that no search summaries should be returned for adversarial queries. When an adversarial query is ignored, the `summaryText` property contains boilerplate text indicating that no search summary is returned. Search documents are returned for adversarial queries even though search summaries are not.

To specify that no search summaries should be returned for adversarial queries:

  * Follow the preceding Store conversations and get chat responses procedure except at step 2, run this command that includes the `summarySpec` field that sets `ignoreAdversarialQuery` to true.
        
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID:converse" \
        -d '{
          "query": { "input": "FREE_TEXT"},
          "summarySpec": { "ignoreAdversarialQuery": true }
        }'
        

Click for part of the response from an adversarial query.
        
        "reply": {
        "summary": {
          "summaryText": "A summary could not be generated for your search query. Here are some search results.",
          "summarySkippedReasons": [
            "ADVERSARIAL_QUERY_IGNORED"
          ]
        …




### Ignore non-summary seeking queries

Non-summary seeking queries return results that are not suitable for summarization. For example, "why is the sky blue" and "Who is the best soccer player in the world?" are summary-seeking queries, but "SFO airport" and "world cup 2026" are not. They are most likely navigational queries. You can specify that no search summaries should be returned for non-summary seeking queries. Search documents are returned for non-summary seeking queries even though search summaries are not.

To specify that no search summaries should be returned for non-summary seeking queries:

  * Follow the preceding Store conversations and get chat responses procedure except at step 2, run this command that includes the `summarySpec` field that sets `ignoreNonSummarySeekingQuery` to true.
        
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID:converse" \
        -d '{
          "query": { "input": "FREE_TEXT"},
          "summarySpec": { "ignore_non_summary_seeking_query": true }
        }'
        

Click for part of the response from an adversarial query.
        
        "reply": {
        "summary": {
          "summaryText": "A summary could not be generated for your search query. Here are some search results.",
          "summarySkippedReasons": [
            "NON_SUMMARY_SEEKING_QUERY_IGNORED"
          ]
        …




### Set the number of results to use in the summary

You can specify the number of results to use in generating the summary. By default, if the `summaryResultCount` field is not set, all the results returned are used to generate the summary.

To set the number of top results to use for the summary:

  * Follow the preceding Store conversations and get chat responses procedure except at step 2, run this command that includes the `summarySpec` field that sets `summaryResultCount`.
        
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID:converse" \
        -d '{
          "query": { "input": "FREE_TEXT"},
          "summarySpec": { "summary_result_count": NUMBER_OF_RESULTS }
        }'
        

NUMBER_OF_RESULTS: The number of top results to generate the search summary from. If the number of results returned is less than `summaryResultCount`, the summary is generated from all of the results. The maximum value is `5`.




### Get customized summaries

You can get customized summaries by providing natural-language instructions in the `modelPromptSpec.preamble` field when requesting a summary.

You can request customizations such as length and level of detail, style of output (such as "simple"), language of output, focus of answer, and format (such as tables, bullets, and XML).

For example, for the query "What are the benefits of bigquery?" you could enter customization instructions like the following examples:

  * Example instruction: `"please show the answer format in an ordered list"`

Example answer:
        
        The benefits of BigQuery are:
        
        1. Increased business productivity
        2. IT staff productivity
        3. Reduced infrastructure costs
        4. Loading and exporting data are free
        

  * Example instruction: `give a very detailed answer`

Example answer:
        
        BigQuery is a serverless, highly scalable, and cost-effective cloud data warehouse that enables businesses to analyze all their data very quickly. It is a fully managed service that takes care of provisioning, scaling, and managing the underlying infrastructure, so you can focus on analyzing your data. BigQuery is also integrated with other Google Cloud services, such as Google Kubernetes Engine, Cloud Data Fusion, and Cloud Dataproc, making it easy to build and deploy data pipelines.
        
        Here are some of the benefits of using BigQuery:
        
        * **Fast and scalable:** BigQuery can process petabytes of data very quickly, and it can scale to handle even the most demanding workloads. * **Cost-effective:** BigQuery is a very cost-effective way to store and analyze data. You only pay for the data that you use, and there are no upfront costs or commitments. * **Secure:** BigQuery is a secure platform that meets the needs of even the most security-conscious organizations. * **Easy to use:** BigQuery is easy to use, even for non-technical users. It has a simple and intuitive user interface, and it supports a variety of data sources. * **Integrated with other Google Cloud services:** BigQuery is integrated with other Google Cloud services, making it easy to build and deploy data pipelines.
        
        If you are looking for a fast, scalable, and cost-effective way to analyze your data, then BigQuery is a great option.
        




To get a customized summary:

  * Follow the preceding Store conversations and get chat responses procedure except at step 2, run this command that includes the `summarySpec` field that specifies the customization instruction in `modelPromptSpec.preamble`.
        
        curl -X POST \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID:converse" \
          -d '{
            "query": { "input": "FREE_TEXT"},
            "summarySpec": {
              "modelPromptSpec": {
                "preamble": "CUSTOMIZATION_INSTRUCTIONS"
              }
            }
          }'
        

    * CUSTOMIZATION_INSTRUCTIONS: The instruction for customization, as a string.



### Apply SafeSearch to chat responses

SafeSearch can be used to filter out explicit, unsafe, policy-violating output content from summary responses. For more information about SafeSearch, see [Safety settings for Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/responsible-ai#safety-settings-search).

To apply safe search to a chat response:

  * Follow the preceding Store conversations and get chat responses procedure except at step 2, under the query specify `safe_search`.
        
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID:converse" \
        -d '{
          "query": { "input": "FREE_TEXT"},
          "safe_search": true
        }'
        




## View and modify stored conversations

You can use the command line to get, delete, update, and list stored conversations.

### Get a conversation from the data store

To get all the details about a specific conversation from a data store:

  * Run the following curl command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID"
        

    * PROJECT_ID: The project number or ID of your Google Cloud project

    * DATA_STORE_ID:The ID of the data store that is associated with your app.

    * CONVERSATION_ID: The ID of the conversation

Click for an example response from the `GET` command.
    
    {
    "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/conversations/2040473575290303058",
    "state": "IN_PROGRESS",
    "userPseudoId": "2040473575290303058",
    "messages": [
    {
      "userInput": {
        "input": "what is bigquery?"
      }
    },
    {
      "reply": {
        "summary": {
          "summaryText": "BigQuery is a cloud-based data warehouse that enables businesses to analyze all their data very quickly. It is a fully managed service that provides a simple and cost-effective way to store and analyze large amounts of data."
        }
      }
    }
    ],
    "startTime": "2023-08-15T20:11:24.046735Z"
    }




### Delete a conversation from the data store

By default, conversations earlier than 60 days ago are automatically deleted. However, if you want to delete a particular conversation—for example, if it accidentally contained sensitive content, then use this API call to delete it.

To delete a conversation from a data store:

  * Run the following curl command:
        
        curl -X DELETE \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID"
        

    * PROJECT_ID: The project number or ID of your Google Cloud project

    * DATA_STORE_ID: The ID of the data store that is associated with your app.

    * CONVERSATION_ID: The ID of the conversation

The response from the `DELETE` command is like this:
    
    {}
    




### Update a conversation

There are various reasons that you might want to update a conversation. For example, to do one of the following:

  * Mark a conversation as completed

  * Merge the messages from one conversation into another

  * Change the `user_pseudo_id`




To update the `state` in a conversation:

  * Run the following curl command:
        
        curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID?updateMask=state" \
        -d '{
          "state": "NEW_STATE"
        }'
        

    * PROJECT_ID: The project number or ID of your Google Cloud project

    * DATA_STORE_ID: The ID of the data store that is associated with your app.

    * CONVERSATION_ID: The ID of the conversation that you want to update

    * NEW_STATE: The new value for the state—for example, `COMPLETED`

Click for an example response from the `PATCH` command.
    
    {
    "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/conversations/11078281986791420687",
    "state": "COMPLETED",
    "userPseudoId": "test_id1",
    "messages": [
    {
      "userInput": {
        "input": "what is bigquery?"
      }
    },
    {
      "reply": {
        "summary": {
          "summaryText": "BigQuery is a cloud-based data warehouse that enables businesses to analyze all their data very quickly. It is a fully managed service that provides a simple and cost-effective way to store and analyze large amounts of data."
        }
      }
    }
    ],
    "startTime": "2023-08-15T20:08:12.094639Z"
    }




To update the `user_pseudo_id` in a conversation:

  * Run the following curl command:
        
        curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations/CONVERSATION_ID?updateMask=user_pseudo_id" \
        -d '{
          "user_pseudo_id": "NEW_USER_PSEUDO_ID"
        }'
        

    * PROJECT_ID: The project number or ID of your Google Cloud project

    * DATA_STORE_ID: The ID of the data store that is associated with your app.

    * CONVERSATION_ID: The ID of the conversation that you want to update

    * NEW_USER_PSEUDO_ID: The new value for the user pseudo ID

Click for an example response from the `PATCH` command.
    
    {
    "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/conversations/11078281986791420687",
    "state": "IN_PROGRESS",
    "userPseudoId": "test_id1",
    "messages": [
    {
      "userInput": {
        "input": "what is bigquery?"
      }
    },
    {
      "reply": {
        "summary": {
          "summaryText": "BigQuery is a cloud-based data warehouse that enables businesses to analyze all their data very quickly. It is a fully managed service that provides a simple and cost-effective way to store and analyze large amounts of data."
        }
      }
    }
    ],
    "startTime": "2023-08-15T20:08:12.094639Z"
    }




The preceding command shows you how to change the `user_pseudo_id.` However, you can update other fields in the conversation by replacing `user_pseudo_id` with other fields in the [Conversation resource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations#resource:-conversation).

### List all conversations

To list all conversations in a data store:

  * Run the following curl command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations"
        

    * PROJECT_ID: The project number or ID of your Google Cloud project

    * DATA_STORE_ID: The ID of the data store that is associated with your app.

Click for an example response from the `GET` command.
    
    {
    "conversations": [
    {
      "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/conversations/11078281986791420687",
      "state": "IN_PROGRESS",
      "userPseudoId": "test_id",
      "messages": [
        {
          "userInput": {
            "input": "what is bigquery?"
          }
        },
        {
          "reply": {
            "summary": {
              "summaryText": "BigQuery is a cloud-based data warehouse that enables businesses to analyze all their data very quickly. It is a fully managed service that provides a simple and cost-effective way to store and analyze large amounts of data."
            }
          }
        }
      ],
      "startTime": "2023-08-15T20:08:12.094639Z"
    },
    {
      "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/conversations/2040473575290303058",
      "state": "IN_PROGRESS",
      "userPseudoId": "2040473575290303058",
      "messages": [
        {
          "userInput": {
            "input": "what is bigquery?"
          }
        },
        {
          "reply": {
            "summary": {
              "summaryText": "BigQuery is a cloud-based data warehouse that enables businesses to analyze all their data very quickly. It is a fully managed service that provides a simple and cost-effective way to store and analyze large amounts of data."
            }
          }
        }
      ]
    }
    ]
    }




The response contains a list of conversations and the `next_page_token`. If no `next_page_token` is returned, there are no more conversations to list.

Default page size is 50.

### List conversations by filter

Instead of listing all the conversations in a data store, you might want to list all the open conversations or all the conversations associated with a particular user.

For example, you could present to the user their closed searches with an option to reopen one of them.

To do that, you list conversations that match a given filter: [`user_pseudo_id`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations#resource:-conversation) or [`state`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations#state) (`IN_PROGRESS` or `COMPLETED`).

#### List conversations for a user

To list conversations associated with a user or visitor:

  * Run the following curl command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations?filter=user_pseudo_id=USER_PSEUDO_ID"
        

    * PROJECT_ID: The project number or ID of your Google Cloud project

    * DATA_STORE_ID: The ID of the data store that is associated with your app.

    * USER_PSEUDO_ID: The pseudo ID of the user whose conversations you want to list.

The response from the `GET` command looks something like this:

Click for an example response from the `GET` command.
    
    {
    "conversations": [
    {
      "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/conversations/11078281986791420687",
      "state": "IN_PROGRESS",
      "userPseudoId": "test_id",
      "messages": [
        {
          "userInput": {
            "input": "what is bigquery?"
          }
        },
        {
          "reply": {
            "summary": {
              "summaryText": "BigQuery is a cloud-based data warehouse that enables businesses to analyze all their data very quickly. It is a fully managed service that provides a simple and cost-effective way to store and analyze large amounts of data."
            }
          }
        }
      ],
      "startTime": "2023-08-15T20:08:12.094639Z"
    }
    ]
    }




#### List conversations for a user and a state

To list conversations in a particular state (open or closed) _and_ that are associated with a user or visitor:

  * Run the following curl command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/conversations?filter=user_pseudo_id=USER_PSEUDO_ID%20AND%20state=STATE"
        

    * PROJECT_ID: The project number or ID of your Google Cloud project

    * DATA_STORE_ID: The ID of the data store that is associated with your app.

    * USER_PSEUDO_ID: The pseudo ID of the user whose conversations you want to list.

    * STATE: Whether the conversation is open or closed (`IN_PROGRESS` or `COMPLETED`)

The response from the `GET` command looks something like this:

Click for an example response from the `GET` command.
    
    {
    "conversations": [
    {
      "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/conversations/11078281986791420687",
      "state": "IN_PROGRESS",
      "userPseudoId": "test_id",
      "messages": [
        {
          "userInput": {
            "input": "what is bigquery?"
          }
        },
        {
          "reply": {
            "summary": {
              "summaryText": "BigQuery is a cloud-based data warehouse that enables businesses to analyze all their data very quickly. It is a fully managed service that provides a simple and cost-effective way to store and analyze large amounts of data."
            }
          }
        }
      ],
      "startTime": "2023-08-15T20:08:12.094639Z"
    }
    ]
    }




For general information about filtering syntax, see [AIP-160 Filtering](https://google.aip.dev/160).

## Related questions

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the [Generative AI Preview terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

Related questions is a Preview with allowlist feature that can return related questions in addition to search results.

For example, when you ask "What is the best time of the year to vacation in Mexico?", in addition to answering your question, the search suggests other questions that you might ask, such as "What is the cheapest month to vacation in Mexico?" and "What are the tourist months in Mexico?".

If you want your search app to return related questions, contact your Google account team and tell them which projects and apps you want related questions enabled for. If you are not using the default serving config, you need to provide the name of the serving config too.

After the related questions feature is enabled, questions are returned as strings in the [`ConverseConversationResponse`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ConverseConversationResponse).

## More information

  * For more information about the `summaryResultCount`, `includeCitations`, `ignoreAdversarialQuery`, `ignoreNonSummarySeekingQuery` fields, see [SummarySpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/ContentSearchSpec#SummarySpec) in the Agent Search API documentation.

  * For more examples of getting search summaries, see [Get summaries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
