---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking/
title: Improve search and RAG quality with ranking API \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:37.257644+00:00
---

# Improve search and RAG quality with ranking API  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Improve search and RAG quality with ranking API Stay organized with collections  Save and categorize content based on your preferences. 

As part of your Retrieval Augmented Generation (RAG) experience in Agent Search, you can rank a set of documents based on a query.

The ranking API takes a list of documents and reranks those documents based on how relevant the documents are to a query. Compared to embeddings, which look only at the semantic similarity of a document and a query, the ranking API can give you precise scores for how well a document answers a given query. The ranking API can be used to improve the quality of search results after retrieving an initial set of candidate documents.

The ranking API is stateless so there's no need to index documents before calling the API. All you need to do is pass in the query and documents. This makes the API well suited for reranking documents from Vector Search and other search solutions.

This page describes how to use the ranking API to rank a set of documents based on a query.

## Use cases

The primary use case of the ranking API is to improve the quality of search results.

However, the ranking API can be valuable for any scenario where you need to find what pieces of content are most relevant to a user's query. For example, the ranking API can assist you in the following:

  * Finding the right content to give to an LLM for grounding

  * Improving the relevance of an existing search experience

  * Identifying relevant sections of a document




The following flow outlines how you might use the ranking API to improve the quality of results for chunked documents:

  1. Use Document AI Layout Parser API to split a set of documents into chunks.

  2. Use an embeddings API to create embeddings for each of the chunks.

  3. Load the embeddings into Vector Search or another search solution.

  4. Query your search index and retrieve the most relevant chunks.

  5. Rerank the relevant chunks using the ranking API.




## Input data

**Key Term:** The ranking API uses the term _record_ to indicate a document. A record is made up of an ID, a title, and the content of a document. Unlike the _documents_ that are contained in Agent Search data stores, the records input to the ranking API are in JSON format and have not been indexed by Agent Search.

The ranking API requires the following inputs:

  * The query for which you're ranking the records.

For example:
        
        "query": "Why is the sky blue?"
        

  * A set of records that are relevant to the query. The records are provided as an array of objects. Each record can include a unique ID, a title, and the content of the document. For each record include either a title, content, or both. The maximum supported tokens per record depends on the model version being used. For example, models up to version `003` support 512 tokens, while version `004` supports 1024 tokens. If the combined length of the title and content exceeds the model's token limit, the extra content is truncated. You can include up to 1000 records per request.

For example, a record array looks something like this. In reality, many more records would be included in the array and the content would be much longer:
        
        "records": [
           {
               "id": "1",
               "title": "The Color of the Sky: A Poem",
               "content": "A canvas stretched across the day,\nWhere sunlight learns to dance and play.\nBlue, a hue of scattered light,\nA gentle whisper, soft and bright."
           },
           {
               "id": "2",
               "title": "The Science of a Blue Sky",
               "content": "The sky appears blue due to a phenomenon called Rayleigh scattering. Sunlight is comprised of all the colors of the rainbow. Blue light has shorter wavelengths than other colors, and is thus scattered more easily."
           }
        ]
        

  * Optional: The maximum number of records that you want the ranking API to return. By default, all records are returned; however, you can use the`topN` field to return fewer records. All records are ranked regardless of what value is set.

For example, this returns the top 10 ranked records:
        
        "topN": 10,
        

  * Optional: A setting that specifies whether you want just the ID of the record returned by the API or if you want the record title and content returned as well. By default, the full record is returned. The main reason to set this is if you want to reduce the size of the response payload.

For example, setting to `true` returns only the record ID, not the title or content:
        
        "ignoreRecordDetailsInResponse": true,
        

  * Optional: The model name. This specifies the model to be used for ranking the documents. If no model is specified, then `semantic-ranker-default@latest` is used, which automatically points to the latest available model. To point to a specific model, specify one of the model names listed in Supported models, for example `semantic-ranker-512-003`.

In the following example, `model` is set to `semantic-ranker-default@latest`. This means that the ranking API will always use the latest available model.
        
        "model": "semantic-ranker-default@latest"
        




### Output data

The ranking API returns a ranked list of records with following outputs:

  * Score: a float value between 0 and 1 that indicates relevance of the record.

  * ID: the unique ID of the record.

  * If requested, the full object: the ID, title, and content.

For example:



    
    
    {
        "records": [
            {
                "id": "2",
                "score": 0.98,
                "title": "The Science of a Blue Sky",
                "content": "The sky appears blue due to a phenomenon called Rayleigh scattering. Sunlight is comprised of all the colors of the rainbow. Blue light has shorter wavelengths than other colors, and is thus scattered more easily."
            },
            {
                "id": "1",
                "score": 0.64,
                "title": "The Color of the Sky: A Poem",
                "content": "A canvas stretched across the day,\nWhere sunlight learns to dance and play.\nBlue, a hue of scattered light,\nA gentle whisper, soft and bright."
            }
        ]
    }
    

## Rank (or rerank) a set of records according to a query

Typically, you'll supply the ranking API with a query and a set of records that are relevant to that query and have already been ranked by some other method such as a keyword search or a vector search. Then, you use the ranking API to improve the quality of the ranking and determine a score that indicates the relevance of each record to the query.

  1. Obtain the query and resulting records. Ensure that each record has an ID and either a title, content, or both.

The maximum number of supported tokens per record depends on the model version. Models up to version `003`, such as `semantic-ranker-512-003`, support 512 tokens per record. Starting from version `004`, this limit increases to 1024 tokens. If the combined length of the title and content exceeds the model's token limit, the extra content is truncated.

  2. Call the [`rankingConfigs.rank`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.rankingConfigs/rank) method using the following code:




### REST
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/rankingConfigs/default_ranking_config:rank" \
    -d '{
    "model": "semantic-ranker-default@latest",
    "query": "QUERY",
    "records": [
        {
            "id": "RECORD_ID_1",
            "title": "TITLE_1",
            "content": "CONTENT_1"
        },
        {
            "id": "RECORD_ID_2",
            "title": "TITLE_2",
            "content": "CONTENT_2"
        },
        {
            "id": "RECORD_ID_3",
            "title": "TITLE_3",
            "content": "CONTENT_3"
        }
    ]
    }'
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project..
  * `QUERY`: the query against which the records are ranked and scored.
  * `RECORD_ID_n`: a unique string that identifies the record.
  * `TITLE_n`: the title of the record.
  * `CONTENT_n`: the content of the record.

**Note:** You can test the API by typing your own values into these placeholders and pasting the command into Cloud Shell. However, in reality, the `records` array would be larger.

For general information about this method, see [`rankingConfigs.rank`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.rankingConfigs/rank).

Click for an example curl command and response.
    
    
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -H "X-Goog-User-Project: my-project-123" \
        "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/rankingConfigs/default_ranking_config:rank" \
        -d '{
            "model": "semantic-ranker-default@latest",
            "query": "what is Google gemini?",
            "records": [
                {
                    "id": "1",
                    "title": "Gemini",
                    "content": "The Gemini zodiac symbol often depicts two figures standing side-by-side."
                },
                {
                    "id": "2",
                    "title": "Gemini",
                    "content": "Gemini is a cutting edge large language model created by Google."
                },
                {
                    "id": "3",
                    "title": "Gemini Constellation",
                    "content": "Gemini is a constellation that can be seen in the night sky."
                }
            ]
        }'
        
    
    
    {
        "records": [
            {
                "id": "2",
                "title": "Gemini",
                "content": "Gemini is a cutting edge large language model created by Google.",
                "score": 0.97
            },
            {
                "id": "3",
                "title": "Gemini Constellation",
                "content": "Gemini is a constellation that can be seen in the night sky.",
                "score": 0.18
            },
            {
                "id": "1",
                "title": "Gemini",
                "content": "The Gemini zodiac symbol often depicts two figures standing side-by-side.",
                "score": 0.05
            }
        ]
    }

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    
    client = discoveryengine.RankServiceClient()
    
    # The full resource name of the ranking config.
    # Format: projects/{project_id}/locations/{location}/rankingConfigs/default_ranking_config
    ranking_config = client.ranking_config_path(
        project=project_id,
        location="global",
        ranking_config="default_ranking_config",
    )
    request = discoveryengine.RankRequest(
        ranking_config=ranking_config,
        model="semantic-ranker-default@latest",
        top_n=10,
        query="What is Google Gemini?",
        records=[
            discoveryengine.RankingRecord(
                id="1",
                title="Gemini",
                content="The Gemini zodiac symbol often depicts two figures standing side-by-side.",
            ),
            discoveryengine.RankingRecord(
                id="2",
                title="Gemini",
                content="Gemini is a cutting edge large language model created by Google.",
            ),
            discoveryengine.RankingRecord(
                id="3",
                title="Gemini Constellation",
                content="Gemini is a constellation that can be seen in the night sky.",
            ),
        ],
    )
    
    response = client.rank(request=request)
    
    # Handle the response
    print(response)

To see an example of ranking api, run the "Ranking API Beir evaluation" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/search/ranking-api/ranking_api_beir_evaluation.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/search/ranking-api/ranking_api_beir_evaluation.ipynb)

## Supported models

The following models are available.

Model name | Latest default model (`semantic-ranker-default@latest`) | Latest fast model (`semantic-ranker-fast@latest`) | Input | Context window | Release date | Discontinuation date  
---|---|---|---|---|---|---  
`semantic-ranker-default-005` | Yes | No | Text (25 languages) | 1024 | September 1, 2026 | To be determined  
`semantic-ranker-fast-005` | No | Yes | Text (25 languages) | 1024 | September 1, 2026 | To be determined  
`semantic-ranker-default-004` | No | No | Text (25 languages) | 1024 | April 9, 2025 | To be determined  
`semantic-ranker-fast-004` | No | No | Text (25 languages) | 1024 | April 9, 2025 | To be determined  
`semantic-ranker-default-003` | No | No | Text (25 languages) | 512 | September 10, 2024 | To be determined  
`semantic-ranker-default-002` | No | No | Text (en only) | 512 | June 3, 2024 | To be determined  
  
## What's next

Learn how to use the ranking method with other RAG APIs to [generate grounded answers from unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/builder-apis#builder-apis-workflow).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
