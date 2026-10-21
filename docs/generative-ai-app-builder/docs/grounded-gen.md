---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen/
title: Generate grounded answers with RAG \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:53:56.650761+00:00
---

# Generate grounded answers with RAG  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Generate grounded answers with RAG Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** The Grounded Generation API is deprecated. Google isn't accepting new requests for the Grounded Generation API. Use Gemini Enterprise Agent Platform for grounding instead, which is publicly available. For more information, see [Grounding overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview).

As part of your Retrieval Augmented Generation (RAG) experience in Agent Search, you can generate grounded answers to prompts based on the following grounding sources:

  * Google Search: Use Grounding with Google Search if you want to connect the model with world knowledge, a wide range of topics, or up-to-date information on the internet. Grounding with Google Search supports dynamic retrieval that gives you the option to generate Grounded Results with Google Search only when necessary. Therefore, the dynamic retrieval configuration evaluates whether a prompt requires knowledge about recent events and enables Grounding with Google Search. For more information, see Dynamic retrieval. **Important:** If you receive Google Search Suggestions with a response, that response is a "Grounded Result" subject to the Grounding with Google Search terms in the [Service Terms](https://cloud.google.com/terms/service-terms) section of the Service Specific Terms. To use Google Search Suggestions, see [ Use Google Search Suggestions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/grounding-search-suggestions).
  * Inline text: Use grounding with inline text to ground the answer in pieces of text called _fact text_ that are provided in the request. A fact text is a user-provided statement that is considered to be factual for a given request. The model doesn't check the authenticity of the fact text.
  * Agent Search data stores: Use grounding with Agent Search if you want to connect the model to your enterprise documents from Agent Search data stores.



This page describes how to generate grounded answers based on these grounding sources using the following approaches:

  * Single-turn answer generation

    * Inline text and Agent Search data store
    * Google Search
  * Multi-turn answer generation




Additionally, you can choose to stream the answers from the model. Generating a grounded answer by streaming is an Experimental feature.

You can use other methods to generate grounded answers, to suit your application. For more information, see [Vertex AI APIs for building search and RAG experiences](https://docs.cloud.google.com/generative-ai-app-builder/docs/builder-apis#generation).

## Terminology

Before you use the grounded answer generation method, it helps to understand the inputs and outputs, how to structure your request, and RAG-related terminology.

### RAG terms

RAG is a methodology that enables Large Language Models (LLMs) to generate responses that are grounded to your data source of choice. There are two stages in RAG:

  1. **Retrieval** : Getting the most relevant facts quickly can be a common search problem. With RAG, you can quickly retrieve the facts that are important to generate an answer.
  2. **Generation:** The retrieved facts are used by the LLM to generate a grounded response.



Therefore, the grounded answer generation method retrieves the facts from the grounding source and generates a grounded answer.

### Input data

The grounded answer generation method requires the following inputs in the request:

  * **Role** : The sender of a given text that's either a user (`user`) or a model (`model`).

  * **Text** : When the role is `user`, the text is a prompt and when the role is `model`, the text is a grounded answer. How you specify the role and text in a request is determined as follows:

    * For a single-turn answer generation, the user sends the prompt text in the request and the model sends the answer text in the response.
    * For a multi-turn answer generation, the request contains the prompt-answer pair for all the previous turns and the prompt text from the user for the current turn. Therefore, in such a request, the role is `user` for a prompt text and it is `model` for the answer text.
  * **System instruction** : A preamble to your prompt that governs the behavior of the model and modifies the output accordingly. For example, you can add a persona to the generated answer or instruct the model to format the output text a certain way. For multi-turn answer generation, you must provide the system instructions for every turn. For more information, see [Use system instructions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions).

  * **Grounding source** : The source in which the answer is grounded and can be one or more of the following:

    * Google Search: Ground the answers with Google Search results. When the grounding source is Google Search, you can specify a _dynamic retrieval_ configuration with a dynamic retrieval threshold. For more information, see Dynamic retrieval. **Important:** If you receive Google Search Suggestions with a response, that response is a "Grounded Result" subject to the Grounding with Google Search terms in the [Service Terms](https://cloud.google.com/terms/service-terms) section of the Service Specific Terms. To use Google Search Suggestions, see [ Use Google Search Suggestions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/grounding-search-suggestions).

    * Inline text: Ground the answer in _fact text_ that is provided in the request. A fact text is a user-provided statement that is considered to be factual for a given request. The model doesn't check the authenticity of the fact text. You can provide a maximum of 100 fact texts in each inline text source. The fact texts can be supported using meta attributes, such as title, author and URI. These meta attributes are returned in the response when quoting the chunks that support the answer.

    * Agent Search data stores: Ground the answer in the documents from Agent Search data stores. You can't specify a website search data store as the grounding source.

In a given request, you can provide both an inline text source and a Agent Search data store source. You can't combine Google Search with either of these sources. Therefore, if you want to ground your answers with Google Search results, you must send a separate request specifying Google Search as the only grounding source.

You can provide a maximum of 10 grounding sources in any order. For example, suppose that you provide the grounding sources with the following count, in the following order to obtain a total of 10 grounding sources:

    * Three inline text sources, each of which can contain a maximum of 100 fact texts
    * Six Agent Search data stores
    * One inline text source, containing a maximum of 100 fact texts

Each source is assigned an index in the order in which it is specified in the request. For example, if you have specified a combination of sources in your request, then the source index is assigned as illustrated in the following table:

Grounding source | Index  
---|---  
Inline text #1 | 0  
Inline text #2 | 1  
Agent Search data store #1 | 2  
Inline text #3 | 3  
Agent Search data store #2 | 4  
  
This index is cited in the response and is helpful when tracing the provenance.

  * **Generation specifications** : The specifications for model configuration that consist of the following information:

    * **Model ID** : Specifies the Vertex AI Gemini model to use for answer generation. For a list of Gemini models that you can use to generate grounded answers, see [Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models).

    * **Model parameters** : Specify the parameters that you can set for the model that you choose to use. These parameters are: language, temperature, top-P, and top-K. For details about these parameters, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters).

  * **Language code** : The language of the generated answer is generally set to match the language of the prompt. If there is no single language in the prompt (for example, if the prompt is very short and can be valid in multiple languages), then the language code field determines the language of the answer.

For a list of language codes, see [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales).

  * **Latitude and longitude** : Specifies the user's latitude and longitude. If the query contains location-specific questions, such as "Find a coffee shop near me," then these fields are used. If the query language can't be determined and the language code isn't set, then the latitude and longitude are used to determine the language of the answer.




### Output data

The response that the model generates is called a _candidate_ and it contains the following data. Not all fields might be present in the output.

  * **Role** : The sender of the grounded answer. The response always contains the grounded answer text. Therefore, the role in a response is always a model.

  * **Text** : A grounded answer.

  * **Grounding score** : A float value in the range [0, 1] that indicates how well an answer is grounded in the given sources.

  * **Grounding metadata** : Metadata about the grounding source. Grounding metadata contains the following information:

    * **Support chunks** : A list of chunks that support the answer. Each support chunk is assigned a support chunk index that is helpful when tracing the provenance. Each support chunk contains the following:

      * **Chunk text** : A portion of text quoted verbatim from the source from which the answer or a part of answer (called the _claim text_) is extracted. This might not always be present in the response.
      * **Source** : An index assigned to the source in the request.
      * **Source metadata** : Metadata about the chunk. Depending on the source, the source metadata can be any of the following:

        * For an inline source, the metadata can be the additional details that were specified in the request such as title, author, or URI.
        * For the Agent Search data store, the metadata can be the document ID, document title, the URI (Cloud Storage location), or the page number.
        * For Grounding with Google Search, when a grounded result is generated, the metadata contains a URI that redirects to the publisher of the content that was used to generate the grounded result. The metadata also contains the publisher's domain. The provided URIs remain accessible for up to 30 days after the grounded result is generated.
**Important:** The provided URI must be directly accessed by the end users and must not be queried programmatically through automated means. If automated access is detected, the Grounding with Google Search service might stop providing the redirection URIs. To restart the redirection URIs, contact your customer engineer.
    * **Grounding support** : Grounding information for a claim in the answer. Grounding support contains the following information:

      * **Claim text** : The answer or a part of the answer that is substantiated with the support chunk text.
      * **Support chunk index** : An index assigned to the support chunk in the order in which the chunk appears in the list of support chunks.
      * **Web search queries** : The suggested search queries for the Google Search Suggestions.
      * **Search Suggestions** : If you receive Google Search Suggestions with a response, that response is a "Grounded Result" subject to the service terms for Grounding with Google Search. For more information, see [Service Terms](https://cloud.google.com/terms/service-terms#panel0-2). The `renderedContent` field within the `searchEntryPoint` field is the provided code for implementing Google Search Suggestions. To use Google Search Suggestions, see [Use Google Search Suggestions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/grounding-search-suggestions).



## Generate a grounded answer in a single turn

This section describes how to generate answers grounded in the following sources:

  * Inline text and Agent Search data store
  * Google Search



### Ground the answer in inline text and Agent Search data store

The following sample shows how to send prompt text by specifying an inline text and a Agent Search data store as the grounding source. You can't specify a website search data store as the grounding source. This sample uses the `generateGroundedContent` method.

### REST

  1. Send the prompt in the following curl request.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global:generateGroundedContent" \
         -d '
         {
         "contents": [
          {
            "role": "user",
            "parts": [
              {
                "text": "PROMPT_TEXT"
              }
            ]
          }
         ],
         "systemInstruction": {
            "parts": {
                "text": "SYSTEM_INSTRUCTION"
            }
         },
         "groundingSpec": {
          "groundingSources": [
            {
              "inlineSource": {
                "groundingFacts": [
                  {
                    "factText": "FACT_TEXT_1",
                    "attributes": {
                      "title": "TITLE_1",
                      "uri": "URI_1",
                      "author": "AUTHOR_1"
                    }
                  }
                ]
              }
            },
            {
              "inlineSource": {
                "groundingFacts": [
                  {
                    "factText": "FACT_TEXT_2",
                    "attributes": {
                      "title": "TITLE_2",
                      "uri": "URI_2"
                    }
                  },
                  {
                    "factText": "FACT_TEXT_3",
                    "attributes": {
                      "title": "TITLE_3",
                      "uri": "URI_3"
                    }
                  }
                ]
              }
            },
            {
              "searchSource": {
                "servingConfig": "projects/PROJECT_NUMBER/locations/global/collections/default_collection/engines/APP_ID_1/servingConfigs/default_search"
              }
            },
            {
              "searchSource": {
                "servingConfig": "projects/PROJECT_NUMBER/locations/global/collections/default_collection/engines/APP_ID_2/servingConfigs/default_search"
              }
            }
           ]
         },
         "generationSpec": {
           "modelId": "MODEL_ID",
           "temperature": TEMPERATURE,
           "topP": TOP_P,
           "topK": TOP_K
         },
         "user_context": {
           "languageCode: "LANGUAGE_CODE",
           "latLng": {
             "latitude": LATITUDE,
             "longitude": LONGITUDE
          },
         }
         }'
         

Replace the following:

     * `PROJECT_NUMBER`: the number of your Google Cloud project.
     * `PROMPT_TEXT`: the prompt from the user. 
     * `SYSTEM_INSTRUCTION`: an optional field to provide a preamble or some additional context. 
     * `FACT_TEXT_N`: the inline text to ground the answer. You can provide a maximum of 100 fact texts. 
     * `TITLE_N`: an optional field to set the title meta attribute for the inline text. 
     * `URI_N`: an optional field to set the URI meta attribute for the inline text. 
     * `AUTHOR_N`: an optional field to set the author meta attribute for the inline text. 
     * `APP_ID_N`: the ID of the Agent Search app.
     * `MODEL_ID`: an optional field to set the model ID of the Gemini model that you'd like to use to generate the grounded answer. For a list of available model IDs, see [Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models) in the Generative AI on Vertex AI product documentation. 
     * `TEMPERATURE`: an optional field to set the temperature used for sampling. Google recommends a temperature of 0.0. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `TOP_P`: an optional field to set the top-P value for the model. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `TOP_K`: an optional field to set the top-K value for the model. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `LANGUAGE_CODE`: an optional field that might be used to set the language for the generated answer and for the chunk text that is returned. if the language can't be determined from the query, this field is used. The default value is `en`. For a list of language codes, see [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales). 
     * `LATITUDE`: an optional field to set the latitude. Enter the value in decimal degrees—for example, `-25.34`. 
     * `LONGITUDE`: an optional field to set the longitude. Enter the value in decimal degrees—for example, `131.04`. 

#### Response

You should receive a JSON response similar to the following truncated response. To understand your response, see Output data.
    
    {
     "candidates": [
       {
         "content": {
           "role": "model",
           "parts": [
             {
               "text": "ANSWER_TEXT"
             }
           ]
         },
         "groundingScore": GROUNDING_SCORE,
         "groundingMetadata": {
           "supportChunks": [
             {
               "chunkText": "CHUNK_TEXT_FROM_A_DOCUMENT_IN_A_DATA_STORE ",
               "source": "4",
               "sourceMetadata": {
                 "title": "DOCUMENT_TITLE",
                 "uri": "gs://PATH/TO/DOCUMENT.pdf",
                 "document_id": "DOCUMENT_ID",
                 "page_identifier": "PAGE_NUMBER"
               }
             },
             {
               "chunkText": "CHUNK_TEXT_FROM_FACT_TEXT_1",
               "source": "0",
               "sourceMetadata": {
                 "title": "TITLE_1",
                 "uri": "URI_1",
                 "author": "AUTHOR_1"
               }
             }
           ],
           "groundingSupport": [
             {
               "claimText": "CLAIM_TEXT_1",
               "supportChunkIndices": [
                 0,
                 1
               ]
             }
           ]
         }
       }
     ]
    }
    




### Example for single-turn answer generation grounded in inline text and Agent Search

In the following example, the request specifies the following grounding sources: one inline text fact and one Agent Search data store. This sample uses the `generateGroundedContent` method. This example also uses a system instruction to end the answer with a smiley emoji.

**Note:** The generated answer in the response might vary and might not contain citations from all the specified grounding sources.

### REST
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1/projects/123456/locations/global:generateGroundedContent" \
    -d '
    {
      "contents": [
        {
          "role": "user",
          "parts": [
            {
              "text": "How did Google do in 2020? Where can I find BigQuery docs?"
            }
          ]
        }
      ],
      "systemInstruction": {
          "parts": {
              "text": "Add a smiley emoji after the answer."
          }
      },
      "groundingSpec": {
        "groundingSources": [
          {
            "inline_source": {
              "grounding_facts": [
                {
                  "fact_text": "The BigQuery documentation can be found at https://cloud.google.com/bigquery/docs/introduction",
                  "attributes": {
                    "title": "BigQuery Overview",
                    "uri": "https://cloud.google.com/bigquery/docs/introduction"
                  }
                }
              ]
            }
          },
          {
            "searchSource": {
              "servingConfig": "projects/123456/locations/global/collections/default_collection/engines/app_id_example/servingConfigs/default_search"
            }
          }
        ]
      },
      "generationSpec": {
        "modelId": "gemini-2.5-flash"
      },
      "user_context": {
        "languageCode: "en",
        "latLng": {
           "latitude": 37.422131,
           "longitude": -122.084801
        }
      }
    }'
    
    

#### Response

You should receive a JSON response similar to the following truncated response. To understand your response, see Output data.
    
    
    {
     "candidates": [
       {
         "content": {
           "role": "model",
           "parts": [
             {
               "text": "Google's revenue increased by 23% in 2020, reaching $182.5 billion. Google Cloud revenue was $13.1 billion for 2020. You can find BigQuery documentation at https://cloud.google.com/bigquery/docs/introduction. 😊 \n"
             }
           ]
         },
         "groundingScore": 0.86738646,
         "groundingMetadata": {
           "supportChunks": [
             {
               "chunkText": "Alphabet Announces Fourth Quarter and Fiscal Year 2020 Results\nMOUNTAIN VIEW, Calif. – February 2, 2021 – Alphabet Inc. (NASDAQ: GOOG, GOOGL) today announced\nfinancial results for the quarter and fiscal year ended December 31, 2020. Sundar Pichai, CEO of Google and Alphabet, said: "Our strong results this quarter reflect the helpfulness of our\nproducts and services to people and businesses, as well as the accelerating transition to online services and the\ncloud. Google succeeds when we help our customers and partners succeed, and we see significant opportunities to\nforge meaningful partnerships as businesses increasingly look to a digital future." Ruth Porat, CFO of Google and Alphabet, said: "Our strong fourth quarter performance, with revenues of $56.9\nbillion, was driven by Search and YouTube, as consumer and business activity recovered from earlier in the year. Google Cloud revenues were $13.1 billion for 2020, with significant ongoing momentum, and we remain focused on\ndelivering value across the growth opportunities we see." New reporting segment structure and operating results\nWe are now reporting results for three segments: Google Services, Google Cloud, and Other Bets. \n...\nIn 2020, we entered into derivatives that hedged the changes in fair value of certain marketable equity securities, which\nresulted in a $497 million net loss for the quarter ended December 31, 2020. The offsetting recognized gains on the\nmarketable equity securities are reflected in Gain (loss) on equity securities, net. Segment results\nThe following table presents our revenues and operating income (loss) (in millions; unaudited): Quarter Fiscal Year Q4 2019 Q1 2020 Q2 2020 Q3 2020 Q4 2020 2018 2019 2020 Revenues:\nGoogle Services $ 43,198 $ 38,198 $ 34,991 $ 42,573 $ 52,873 $ 130,524 $ 151,825 $ 168,635 Google Cloud 2,614 2,777 3,007 3,444 3,831 5,838 8,918 13,059 Other Bets 172 135 148 178 196 595 659 657 Hedging gains (losses) 91 49 151 (22) (2) (138) 455 176 Total revenues $ 46,075 $ 41,159 $ 38,297 $ 46,173 $ 56,898 $ 136,819 $ 161,857 $ 182,527 Quarter Fiscal Year Q4 2019 Q1 2020 Q2 2020 Q3 2020 Q4 2020 2018 2019 2020 Operating income (loss):\nGoogle Services $ 13,488 $ 11,548 $ 9,539 $ 14,453 $ 19,066 $ 43,137 $ 48,999 $ 54,606 Google Cloud (1,194) (1,730) (1,426) (1,208) (1,243) (4,348) (4,645) (5,607) Other Bets (2,026) (1,121) (1,116) (1,103) (1,136) \n...\nQ4 2020 financial highlights\nThe following table summarizes our consolidated financial results for the quarters ended December 31, 2019 and\n2020 (in millions, except for per share information and percentages; unaudited). Quarter Ended December 31,\n2019 2020 Revenues $ 46,075 $ 56,898 Increase in revenues year over year 17 % 23 % Increase in constant currency revenues year over year(1) 19 % 23 % Operating income $ 9,266 $ 15,651 Operating margin 20 % 28 % Other income (expense), net $ 1,438 $ 3,038 Net income $ 10,671 $ 15,227 Diluted EPS $ 15.35 $ 22.30 (1) Non-GAAP measure. See the table captioned "Reconciliation from GAAP revenues to non-GAAP constant currency\nrevenues" for more details. Q4 2020 supplemental information (in millions, except for number of employees; unaudited)\nRevenues, Traffic Acquisition Costs (TAC) and number of employees\nThe following table summarizes our revenues, total TAC and number of employees. Quarter Ended December 31,\n2019 2020 Google Search & other $ 27,185 $ 31,903 YouTube ads 4,717 6,885 Google Network Members' properties 6,032 7,411 Google advertising 37,934 46,199 Google other 5,264 6,674 Google Services total 43,198 52,873 Google Cloud 2,614 3,831 Other Bets 172 196 Hedging gains (losses) 91 (2) Total revenues $ 46,075 $ 56,898 Total TAC $ 8,501 $ 10,466 Number of employees 118,899 135,301 ",
               "source": "1",
               "sourceMetadata": {
                 "title": "GOOG Exhibit 99.1 Q4'20",
                 "page_identifier": "2",
                 "uri": "gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2020Q4_alphabet_earnings_release.pdf",
                 "document_id": "projects/123456/locations/global/collections/default_collection/dataStores/data_store_id_example/branches/0/documents/217e8bedecfe08e3c43f5b289af15243"
               }
             },
             {
               "chunkText": "Alphabet Announces Fourth Quarter and Fiscal Year 2020 Results\nMOUNTAIN VIEW, Calif. – February 2, 2021 – Alphabet Inc. (NASDAQ: GOOG, GOOGL) today announced\nfinancial results for the quarter and fiscal year ended December 31, 2020. Sundar Pichai, CEO of Google and Alphabet, said: "Our strong results this quarter reflect the helpfulness of our\nproducts and services to people and businesses, as well as the accelerating transition to online services and the\ncloud. Google succeeds when we help our customers and partners succeed, and we see significant opportunities to\nforge meaningful partnerships as businesses increasingly look to a digital future." Ruth Porat, CFO of Google and Alphabet, said: "Our strong fourth quarter performance, with revenues of $56.9\nbillion, was driven by Search and YouTube, as consumer and business activity recovered from earlier in the year. Google Cloud revenues were $13.1 billion for 2020, with significant ongoing momentum, and we remain focused on\ndelivering value across the growth opportunities we see." New reporting segment structure and operating results\nWe are now reporting results for three segments: Google Services, Google Cloud, and Other Bets. \n...\nIn 2020, we entered into derivatives that hedged the changes in fair value of certain marketable equity securities, which\nresulted in a $497 million net loss for the quarter ended December 31, 2020. The offsetting recognized gains on the\nmarketable equity securities are reflected in Gain (loss) on equity securities, net. Segment results\nThe following table presents our revenues and operating income (loss) (in millions; unaudited): Quarter Fiscal Year Q4 2019 Q1 2020 Q2 2020 Q3 2020 Q4 2020 2018 2019 2020 Revenues:\nGoogle Services $ 43,198 $ 38,198 $ 34,991 $ 42,573 $ 52,873 $ 130,524 $ 151,825 $ 168,635 Google Cloud 2,614 2,777 3,007 3,444 3,831 5,838 8,918 13,059 Other Bets 172 135 148 178 196 595 659 657 Hedging gains (losses) 91 49 151 (22) (2) (138) 455 176 Total revenues $ 46,075 $ 41,159 $ 38,297 $ 46,173 $ 56,898 $ 136,819 $ 161,857 $ 182,527 Quarter Fiscal Year Q4 2019 Q1 2020 Q2 2020 Q3 2020 Q4 2020 2018 2019 2020 Operating income (loss):\nGoogle Services $ 13,488 $ 11,548 $ 9,539 $ 14,453 $ 19,066 $ 43,137 $ 48,999 $ 54,606 Google Cloud (1,194) (1,730) (1,426) (1,208) (1,243) (4,348) (4,645) (5,607) Other Bets (2,026) (1,121) (1,116) (1,103) (1,136) \n...\nQ4 2020 financial highlights\nThe following table summarizes our consolidated financial results for the quarters ended December 31, 2019 and\n2020 (in millions, except for per share information and percentages; unaudited). Quarter Ended December 31,\n2019 2020 Revenues $ 46,075 $ 56,898 Increase in revenues year over year 17 % 23 % Increase in constant currency revenues year over year(1) 19 % 23 % Operating income $ 9,266 $ 15,651 Operating margin 20 % 28 % Other income (expense), net $ 1,438 $ 3,038 Net income $ 10,671 $ 15,227 Diluted EPS $ 15.35 $ 22.30 (1) Non-GAAP measure. See the table captioned "Reconciliation from GAAP revenues to non-GAAP constant currency\nrevenues" for more details. Q4 2020 supplemental information (in millions, except for number of employees; unaudited)\nRevenues, Traffic Acquisition Costs (TAC) and number of employees\nThe following table summarizes our revenues, total TAC and number of employees. Quarter Ended December 31,\n2019 2020 Google Search & other $ 27,185 $ 31,903 YouTube ads 4,717 6,885 Google Network Members' properties 6,032 7,411 Google advertising 37,934 46,199 Google other 5,264 6,674 Google Services total 43,198 52,873 Google Cloud 2,614 3,831 Other Bets 172 196 Hedging gains (losses) 91 (2) Total revenues $ 46,075 $ 56,898 Total TAC $ 8,501 $ 10,466 Number of employees 118,899 135,301 ",
               "source": "1",
               "sourceMetadata": {
                 "document_id": "projects/123456/locations/global/collections/default_collection/dataStores/data_store_id_example/branches/0/documents/217e8bedecfe08e3c43f5b289af15243",
                 "page_identifier": "2",
                 "title": "GOOG Exhibit 99.1 Q4'20",
                 "uri": "gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2020Q4_alphabet_earnings_release.pdf"
               }
             },
             {
               "chunkText": "The BigQuery documentation can be found at https://cloud.google.com/bigquery/docs/introduction ",
               "source": "0",
               "sourceMetadata": {
                 "uri": "https://cloud.google.com/bigquery/docs/introduction",
                 "title": "BigQuery Overview"
               }
             }
           ],
           "groundingSupport": [
             {
               "claimText": "Google's revenue increased by 23% in 2020, reaching $182.5 billion.",
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "Google Cloud revenue was $13.1 billion for 2020.",
               "supportChunkIndices": [
                 1
               ]
             },
             {
               "claimText": "You can find BigQuery documentation at https://cloud.google.com/bigquery/docs/introduction.😊 ",
               "supportChunkIndices": [
                 2
               ]
             }
           ]
         }
       }
     ]
    }
    

### Python
    
    
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_number = "YOUR_PROJECT_NUMBER"
    # engine_id = "YOUR_ENGINE_ID"
    
    client = discoveryengine.GroundedGenerationServiceClient()
    
    request = discoveryengine.GenerateGroundedContentRequest(
        # The full resource name of the location.
        # Format: projects/{project_number}/locations/{location}
        location=client.common_location_path(project=project_number, location="global"),
        generation_spec=discoveryengine.GenerateGroundedContentRequest.GenerationSpec(
            model_id="gemini-2.5-flash",
        ),
        # Conversation between user and model
        contents=[
            discoveryengine.GroundedGenerationContent(
                role="user",
                parts=[
                    discoveryengine.GroundedGenerationContent.Part(
                        text="How did Google do in 2020? Where can I find BigQuery docs?"
                    )
                ],
            )
        ],
        system_instruction=discoveryengine.GroundedGenerationContent(
            parts=[
                discoveryengine.GroundedGenerationContent.Part(
                    text="Add a smiley emoji after the answer."
                )
            ],
        ),
        # What to ground on.
        grounding_spec=discoveryengine.GenerateGroundedContentRequest.GroundingSpec(
            grounding_sources=[
                discoveryengine.GenerateGroundedContentRequest.GroundingSource(
                    inline_source=discoveryengine.GenerateGroundedContentRequest.GroundingSource.InlineSource(
                        grounding_facts=[
                            discoveryengine.GroundingFact(
                                fact_text=(
                                    "The BigQuery documentation can be found at https://cloud.google.com/bigquery/docs/introduction"
                                ),
                                attributes={
                                    "title": "BigQuery Overview",
                                    "uri": "https://cloud.google.com/bigquery/docs/introduction",
                                },
                            ),
                        ]
                    ),
                ),
                discoveryengine.GenerateGroundedContentRequest.GroundingSource(
                    search_source=discoveryengine.GenerateGroundedContentRequest.GroundingSource.SearchSource(
                        # The full resource name of the serving config for a Vertex AI Search App
                        serving_config=f"projects/{project_number}/locations/global/collections/default_collection/engines/{engine_id}/servingConfigs/default_search",
                    ),
                ),
            ]
        ),
    )
    response = client.generate_grounded_content(request)
    
    # Handle the response
    print(response)

## Generate grounded answer with Google Search

You can ground the generated responses with publicly available web data. **Important:** If you receive Google Search Suggestions with a response, that response is a "Grounded Result" subject to the Grounding with Google Search terms in the [Service Terms](https://cloud.google.com/terms/service-terms) section of the Service Specific Terms. To use Google Search Suggestions, see [ Use Google Search Suggestions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/grounding-search-suggestions).

**Note for web publishers:** Grounding with Google Search on Vertex AI does not use web pages for grounding that have disallowed Google-Extended. Web publishers can [manage inclusion in Google-Extended with a robots.txt file](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers#google-extended).

### Dynamic retrieval

You can use dynamic retrieval in your request to choose when to turn off grounding with Google Search. This is useful when the prompt doesn't require an answer that's grounded with Google Search and the model can provide an answer based on its knowledge without grounding. This helps you to manage latency, quality, and cost more effectively.

#### Dynamic retrieval prediction score and threshold

When you send a request to generate a grounded answer, Agent Search assigns a _prediction score_ to the prompt. The prediction score is a floating point value in the range [0,1]. Its value depends on whether the prompt can benefit from grounding the answer with the most up-to-date information from Google Search. Therefore, a prompt that requires an answer grounded in the most recent facts on the web has a higher prediction score, and a prompt for which a model-generated answer is sufficient has a lower prediction score.

Here are examples of some prompts and their prediction scores.

**Note:** The prediction scores are assigned by Agent Search and can vary over time depending on several factors.Prompt | Prediction score | Comment  
---|---|---  
"Write a poem about peonies" | 0.13 | The model can rely on its knowledge and the answer doesn't need grounding  
"Suggest a toy for a 2yo child" | 0.36 | The model can rely on its knowledge and the answer doesn't need grounding  
"Can you give a recipe for an asian-inspired guacamole?" | 0.55 | Google Search can give a grounded answer, but grounding is not strictly required; the model knowledge might be sufficient  
"What's Agent Search? How is grounding billed in Agent Search?" | 0.72 | Requires Google Search to generate a well-grounded answer  
"Who won the latest F1 grand prix?" | 0.97 | Requires Google Search to generate a well-grounded answer  
  
In your grounded answer generation request, you can specify a dynamic retrieval configuration with a threshold. The threshold is a floating point value in the range [0,1] and defaults to 0.7. If the threshold value is zero, the response is always grounded in Google Search. For all other values of threshold, the following is applicable:

  * If the prediction score is greater than or equal to the threshold, the answer is grounded with Google Search. A lower threshold implies that more prompts have responses that are generated using Grounding with Google Search.
  * If the prediction score is less than the threshold, the model may still generate the answer, but it isn't grounded with Google Search.



To find a good threshold that suits your business needs, you can create a representative set of queries that you expect to encounter. Then, you can sort the queries according to the prediction score in the response and select a good threshold for your use case.

### Ground the answer with Google Search

The following sample shows how to generate a grounded answer from a prompt by specifying Google Search as the grounding source. This sample uses the `generateGroundedContent` method.

### REST

  1. Send the prompt in the following curl request.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global:generateGroundedContent" \
         -d '
         {
         "contents": [
          {
            "role": "user",
            "parts": [
              {
                "text": "PROMPT_TEXT"
              }
            ]
          }
         ],
         "systemInstruction": {
            "parts": {
                "text": "SYSTEM_INSTRUCTION"
            }
         },
         "groundingSpec": {
          "groundingSources": [
          {
              "googleSearchSource": {
                   "dynamicRetrievalConfig": {
                       "predictor":{
                           "threshold": DYNAMIC_RETRIEVAL_THRESHOLD
                       }
                   }
              }
          }
         ]
         },
         "generationSpec": {
          "modelId": "MODEL_ID",
          "temperature": TEMPERATURE,
          "topP": TOP_P,
          "topK": TOP_K
         },
         "user_context": {
          "languageCode: "LANGUAGE_CODE",
          "latLng": {
            "latitude": LATITUDE,
            "longitude": LONGITUDE
          },
         }
         }'
         

Replace the following:

     * `PROJECT_NUMBER`: the number of your Google Cloud project.
     * `PROMPT_TEXT`: the prompt from the user. 
     * `SYSTEM_INSTRUCTION`: an optional field to provide a preamble or some additional context. 
     * `DYNAMIC_RETRIEVAL_THRESHOLD`: an optional field to set the threshold to invoke the dynamic retrieval configuration. It is floating point value in the range [0,1]. If you add the `dynamicRetrievalConfig` field, but you don't set the `predictor` or `threshold` field, the threshold value defaults to 0.7. If you don't set the `dynamicRetrievalConfig` field, the answer is always grounded.
     * `MODEL_ID`: an optional field to set the model ID of the Gemini model that you'd like to use to generate the grounded answer. For a list of available model IDs, see [Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models) in the Generative AI on Vertex AI product documentation. 
     * `TEMPERATURE`: an optional field to set the temperature used for sampling. Google recommends a temperature of 0.0. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `TOP_P`: an optional field to set the top-P value for the model. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `TOP_K`: an optional field to set the top-K value for the model. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `LANGUAGE_CODE`: an optional field that might be used to set the language for the generated answer and for the chunk text that is returned. if the language can't be determined from the query, this field is used. The default value is `en`. For a list of language codes, see [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales). 
     * `LATITUDE`: an optional field to set the latitude. Enter the value in decimal degrees—for example, `-25.34`. 
     * `LONGITUDE`: an optional field to set the longitude. Enter the value in decimal degrees—for example, `131.04`. 

#### Response

You should receive a JSON response similar to the following truncated response. To understand your response, see Output data. 

**Note:** The model that evaluates the prediction score is subject to change but the prediction scores might still lie in the same range. For examples of some prompts and their prediction scores, see Dynamic retrieval prediction score and threshold.
    
    {
     "candidates": [
       {
         "content": {
           "role": "model",
           "parts": [
             {
               "text": "ANSWER_TEXT"
             }
           ]
         },
         "groundingScore":GROUNDING_SCORE,
         "groundingMetadata": {
           "supportChunks": [
             {
              "source": "0",
              "sourceMetadata": {
                "uri": "REDIRECTION_URI",
                "domain": "PUBLISHER_DOMAIN"
              }
             }
           ],
           "groundingSupport": [
             {
               "claimText": "CLAIM_TEXT_1",
               "supportScore": SUPPORT_SCORE,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "CLAIM_TEXT_2",
               "supportScore": SUPPORT_SCORE,
               "supportChunkIndices": [
                 0
               ]
             }
           ],
           "webSearchQueries": [
             "QUERY_BUILT_FROM_USER_PROMPT"
           ],
           "searchEntryPoint": {
             "renderedContent": "RENDERED_CONTENT"
           },
         }
       }
     ]
    }
    {
     "candidates": [
       {
         "content": {
           "role": "model",
           "parts": [
             {
               "text": "ANSWER_TEXT"
             }
           ]
         },
         "groundingScore":GROUNDING_SCORE,
         "groundingMetadata": {
           "supportChunks": [
             {}
           ],
           "groundingSupport": [
             {
               "claimText": "CLAIM_TEXT_1",
               "supportScore": SUPPORT_SCORE,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "CLAIM_TEXT_2",
               "supportScore": SUPPORT_SCORE,
               "supportChunkIndices": [
                 0
               ]
             }
           ],
           "webSearchQueries": [
             "QUERY_BUILT_FROM_USER_PROMPT"
           ],
           "searchEntryPoint": {
             "renderedContent": "RENDERED_CONTENT"
           },
           "retrievalMetadata": [
             {
               "source": "GOOGLE_SEARCH",
               "dynamicRetrievalMetadata": {
                 "predictorMetadata": {
                   "version": "V1_INDEPENDENT",
                   "prediction": PREDICTION_SCORE
                 }
               }
             }
           ]
         }
       }
     ]
    }
    




### Python
    
    
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_number = "YOUR_PROJECT_NUMBER"
    
    client = discoveryengine.GroundedGenerationServiceClient()
    
    request = discoveryengine.GenerateGroundedContentRequest(
        # The full resource name of the location.
        # Format: projects/{project_number}/locations/{location}
        location=client.common_location_path(project=project_number, location="global"),
        generation_spec=discoveryengine.GenerateGroundedContentRequest.GenerationSpec(
            model_id="gemini-2.5-flash",
        ),
        # Conversation between user and model
        contents=[
            discoveryengine.GroundedGenerationContent(
                role="user",
                parts=[
                    discoveryengine.GroundedGenerationContent.Part(
                        text="How much is Google stock?"
                    )
                ],
            )
        ],
        system_instruction=discoveryengine.GroundedGenerationContent(
            parts=[
                discoveryengine.GroundedGenerationContent.Part(text="Be comprehensive.")
            ],
        ),
        # What to ground on.
        grounding_spec=discoveryengine.GenerateGroundedContentRequest.GroundingSpec(
            grounding_sources=[
                discoveryengine.GenerateGroundedContentRequest.GroundingSource(
                    google_search_source=discoveryengine.GenerateGroundedContentRequest.GroundingSource.GoogleSearchSource(
                        # Optional: For Dynamic Retrieval
                        dynamic_retrieval_config=discoveryengine.GenerateGroundedContentRequest.DynamicRetrievalConfiguration(
                            predictor=discoveryengine.GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor(
                                threshold=0.7
                            )
                        )
                    )
                ),
            ]
        ),
    )
    response = client.generate_grounded_content(request)
    
    # Handle the response
    print(response)

### Example for single-turn answer generation grounded with Google Search

In the following example, the request specifies Google Search as the grounding source. This sample uses the `generateGroundedContent` method. This example also uses a system instruction to end the answer with a smiley emoji.

**Important:** If you receive Google Search Suggestions with a response, that response is a "Grounded Result" subject to the Grounding with Google Search terms in the [Service Terms](https://cloud.google.com/terms/service-terms) section of the Service Specific Terms. To use Google Search Suggestions, see [ Use Google Search Suggestions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/grounding-search-suggestions).

**Note:** The generated answer in the response might vary.

### REST
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1/projects/123456/locations/global:generateGroundedContent" \
    -d '
    {
    "contents": [{
      "role": "user",
      "parts": [{
        "text": "What is Agent Search?"
    }]
    }],
    "systemInstruction": {
       "parts": {
          "text": "Add a smiley emoji after the answer."
       }
    },
    "groundingSpec": {
      "groundingSources": [
      {
          "googleSearchSource": {
            "dynamicRetrievalConfig": {
                   "predictor":{
                       "threshold": 0.6
                   }
               }
          }
      }
     ]
    },
    "generationSpec": {
      "modelId": "gemini-2.5-flash"
    }
    }
    '
    

#### Response

You should receive a JSON response similar to the following truncated response. To understand your response, see Output data.
    
    
    {
     "candidates": [
       {
         "content": {
           "role": "model",
           "parts": [
             {
               "text": "Agent Search is a platform developed by Google Cloud that simplifies the creation and deployment of generative AI agents. It offers both no-code and code-first approaches, allowing developers of all skill levels to build AI-powered agents. \n\nHere are some key features of Agent Search:\n\n* **No-code interface:**  Use natural language to design and build agents without writing code.\n* **Code-first approach:**  Utilize powerful orchestration and customization capabilities.\n* **Enterprise-grade security and compliance:**  Built-in security, compliance, and governance features align with industry certifications like HIPAA, ISO 27000-series, SOC-1/2/3, VPC-SC, and CMEK.\n* **Integration with enterprise data:**  Easily ground your agents in enterprise data using Agent Search and Retrieval Augmented Generation (RAG) APIs.\n* **Pre-built templates:**  Rapidly prototype and experiment with pre-built templates for conversational AI and process automation agents.\n* **Advanced integrations:**  Supports integrations with frameworks like LlamaIndex and LangChain for enhanced AI capabilities.\n* **Natural language understanding (NLU):**  Accurate query responses and support for multiple languages.\n\nAgent Search is designed to help developers create AI agents that can:\n\n* Answer complex questions\n* Provide support and personalize user experiences\n* Automate tasks and processes\n* Interact with backend systems\n\nOverall, Agent Search is a powerful tool that makes it easier for developers to build and deploy generative AI agents, regardless of their experience level. 😊 \n"
             }
           ]
         },
         "groundingScore": 0.80400103,
         "groundingMetadata": {
           "supportChunks": [
             {
              "source": "0",
              "sourceMetadata": {
              "uri": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/{unique_string}",
              "domain": "example.com"
             }
            }
           ],
           "groundingSupport": [
             {
               "claimText": "Agent Search is a platform developed by Google Cloud that simplifies the creation and deployment of generative AI agents.",
               "supportScore": 0.9541752,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "It offers both no-code and code-first approaches, allowing developers of all skill levels to build AI-powered agents.",
               "supportScore": 0.9648506,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "* **No-code interface:**  Use natural language to design and build agents without writing code.",
               "supportScore": 0.77115613,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "* **Code-first approach:**  Utilize powerful orchestration and customization capabilities.",
               "supportScore": 0.8540146,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "* **Enterprise-grade security and compliance:**  Built-in security, compliance, and governance features align with industry certifications like HIPAA, ISO 27000-series, SOC-1/2/3, VPC-SC, and CMEK.",
               "supportScore": 0.9574074,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "* **Integration with enterprise data:**  Easily ground your agents in enterprise data using Agent Search and Retrieval Augmented Generation (RAG) APIs.",
               "supportScore": 0.9533333,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "* **Pre-built templates:**  Rapidly prototype and experiment with pre-built templates for conversational AI and process automation agents.",
               "supportScore": 0.9457701,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "* **Advanced integrations:**  Supports integrations with frameworks like LlamaIndex and LangChain for enhanced AI capabilities.",
               "supportScore": 0.9541752,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "* **Natural language understanding (NLU):**  Accurate query responses and support for multiple languages.",
               "supportScore": 0.97726375,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "* Provide support and personalize user experiences",
               "supportScore": 0.8540146,
               "supportChunkIndices": [
                 0
               ]
             },
             {
               "claimText": "* Automate tasks and processes",
               "supportScore": 0.82046676,
               "supportChunkIndices": [
                 0
               ]
             }
           ],
           "webSearchQueries": [
             "what is Agent Search"
           ],
           "searchEntryPoint": {
             "renderedContent": "\u003cstyle\u003e\n.container {\n  align-items: center;\n  border-radius: 8px;\n  display: flex;\n  font-family: Google Sans, Roboto, sans-serif;\n  font-size: 14px;\n  line-height: 20px;\n  padding: 8px 12px;\n}\n.chip {\n  display: inline-block;\n  border: solid 1px;\n  border-radius: 16px;\n  min-width: 14px;\n  padding: 5px 16px;\n  text-align: center;\n  user-select: none;\n  margin: 0 8px;\n  -webkit-tap-highlight-color: transparent;\n}\n.carousel {\n  overflow: auto;\n  scrollbar-width: none;\n  white-space: nowrap;\n  margin-right: -12px;\n}\n.headline {\n  display: flex;\n  margin-right: 4px;\n}\n.gradient-container {\n  position: relative;\n}\n.gradient {\n  position: absolute;\n  transform: translate(3px, -9px);\n  height: 36px;\n  width: 9px;\n}\n@media (prefers-color-scheme: light) {\n  .container {\n    background-color: #fafafa;\n    box-shadow: 0 0 0 1px #0000000f;\n  }\n  .headline-label {\n    color: #1f1f1f;\n  }\n  .chip {\n    background-color: #ffffff;\n    border-color: #d2d2d2;\n    color: #5e5e5e;\n    text-decoration: none;\n  }\n  .chip:hover {\n    background-color: #f2f2f2;\n  }\n  .chip:focus {\n    background-color: #f2f2f2;\n  }\n  .chip:active {\n    background-color: #d8d8d8;\n    border-color: #b6b6b6;\n  }\n  .logo-dark {\n    display: none;\n  }\n  .gradient {\n    background: linear-gradient(90deg, #fafafa 15%, #fafafa00 100%);\n  }\n}\n@media (prefers-color-scheme: dark) {\n  .container {\n    background-color: #1f1f1f;\n    box-shadow: 0 0 0 1px #ffffff26;\n  }\n  .headline-label {\n    color: #fff;\n  }\n  .chip {\n    background-color: #2c2c2c;\n    border-color: #45474d;\n    color: #fff;\n    text-decoration: none;\n  }\n  .chip:hover {\n    background-color: #353536;\n  }\n  .chip:focus {\n    background-color: #353536;\n  }\n  .chip:active {\n    background-color: #464849;\n    border-color: #53575b;\n  }\n  .logo-light {\n    display: none;\n  }\n  .gradient {\n    background: linear-gradient(90deg, #1f1f1f 15%, #1f1f1f00 100%);\n  }\n}\n\u003c/style\u003e\n\u003cdiv class=\"container\"\u003e\n  \u003cdiv class=\"headline\"\u003e\n    \u003csvg class=\"logo-light\" width=\"18\" height=\"18\" viewBox=\"9 9 35 35\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\"\u003e\n      \u003cpath fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M42.8622 27.0064C42.8622 25.7839 42.7525 24.6084 42.5487 23.4799H26.3109V30.1568H35.5897C35.1821 32.3041 33.9596 34.1222 32.1258 35.3448V39.6864H37.7213C40.9814 36.677 42.8622 32.2571 42.8622 27.0064V27.0064Z\" fill=\"#4285F4\"/\u003e\n      \u003cpath fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M26.3109 43.8555C30.9659 43.8555 34.8687 42.3195 37.7213 39.6863L32.1258 35.3447C30.5898 36.3792 28.6306 37.0061 26.3109 37.0061C21.8282 37.0061 18.0195 33.9811 16.6559 29.906H10.9194V34.3573C13.7563 39.9841 19.5712 43.8555 26.3109 43.8555V43.8555Z\" fill=\"#34A853\"/\u003e\n      \u003cpath fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M16.6559 29.8904C16.3111 28.8559 16.1074 27.7588 16.1074 26.6146C16.1074 25.4704 16.3111 24.3733 16.6559 23.3388V18.8875H10.9194C9.74388 21.2072 9.06992 23.8247 9.06992 26.6146C9.06992 29.4045 9.74388 32.022 10.9194 34.3417L15.3864 30.8621L16.6559 29.8904V29.8904Z\" fill=\"#FBBC05\"/\u003e\n      \u003cpath fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M26.3109 16.2386C28.85 16.2386 31.107 17.1164 32.9095 18.8091L37.8466 13.8719C34.853 11.082 30.9659 9.3736 26.3109 9.3736C19.5712 9.3736 13.7563 13.245 10.9194 18.8875L16.6559 23.3388C18.0195 19.2636 21.8282 16.2386 26.3109 16.2386V16.2386Z\" fill=\"#EA4335\"/\u003e\n    \u003c/svg\u003e\n    \u003csvg class=\"logo-dark\" width=\"18\" height=\"18\" viewBox=\"0 0 48 48\" xmlns=\"http://www.w3.org/2000/svg\"\u003e\n      \u003ccircle cx=\"24\" cy=\"23\" fill=\"#FFF\" r=\"22\"/\u003e\n      \u003cpath d=\"M33.76 34.26c2.75-2.56 4.49-6.37 4.49-11.26 0-.89-.08-1.84-.29-3H24.01v5.99h8.03c-.4 2.02-1.5 3.56-3.07 4.56v.75l3.91 2.97h.88z\" fill=\"#4285F4\"/\u003e\n      \u003cpath d=\"M15.58 25.77A8.845 8.845 0 0 0 24 31.86c1.92 0 3.62-.46 4.97-1.31l4.79 3.71C31.14 36.7 27.65 38 24 38c-5.93 0-11.01-3.4-13.45-8.36l.17-1.01 4.06-2.85h.8z\" fill=\"#34A853\"/\u003e\n      \u003cpath d=\"M15.59 20.21a8.864 8.864 0 0 0 0 5.58l-5.03 3.86c-.98-2-1.53-4.25-1.53-6.64 0-2.39.55-4.64 1.53-6.64l1-.22 3.81 2.98.22 1.08z\" fill=\"#FBBC05\"/\u003e\n      \u003cpath d=\"M24 14.14c2.11 0 4.02.75 5.52 1.98l4.36-4.36C31.22 9.43 27.81 8 24 8c-5.93 0-11.01 3.4-13.45 8.36l5.03 3.85A8.86 8.86 0 0 1 24 14.14z\" fill=\"#EA4335\"/\u003e\n    \u003c/svg\u003e\n    \u003cdiv class=\"gradient-container\"\u003e\u003cdiv class=\"gradient\"\u003e\u003c/div\u003e\u003c/div\u003e\n  \u003c/div\u003e\n  \u003cdiv class=\"carousel\"\u003e\n    \u003ca class=\"chip\" href=\"https://www.google.com/search?q=what+is+ai-applications&client=app-vertex-grounding&safesearch=active\"\u003ewhat is Agent Search\u003c/a\u003e\n  \u003c/div\u003e\n\u003c/div\u003e\n"
           },
           "retrievalMetadata": [
             {
               "source": "GOOGLE_SEARCH",
               "dynamicRetrievalMetadata": {
                 "predictorMetadata": {
                   "version": "V1_INDEPENDENT",
                   "prediction": 0.671875
                 }
               }
             }
           ]
         }
       }
     ]
    }
    

## Generate a grounded answer in multiple turns

In multi-turn answer generation, in each request you must send all the text exchanged between the user and the model in all the previous turns. This ensures continuity and maintains context to generate the answer for the latest prompt.

To obtain a grounded answer by multi-turn answer generation, do the following:

### REST

The following samples show how to send follow-up prompt text over multiple turns. These samples use the `generateGroundedContent` method and ground the answers with Google Search. You can use similar steps to generate grounded answers using other grounding sources. **Important:** If you receive Google Search Suggestions with a response, that response is a "Grounded Result" subject to the Grounding with Google Search terms in the [Service Terms](https://cloud.google.com/terms/service-terms) section of the Service Specific Terms. To use Google Search Suggestions, see [ Use Google Search Suggestions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/grounding-search-suggestions).

  1. Send the first prompt in the following curl request.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global:generateGroundedContent" \
         -d '
         {
         "contents": [
          {
            "role": "user",
            "parts": [
              {
                "text": "PROMPT_TEXT_TURN_1"
              }
            ]
          }
         ],
         "systemInstruction": {
            "parts": {
                "text": "SYSTEM_INSTRUCTION_TURN_1"
            }
         },
         "groundingSpec": {
          "groundingSources": [
            {
              "googleSearchSource": {}
            }
          ]
         },
         "generationSpec": {
          "modelId": "MODEL_ID",
          "temperature": TEMPERATURE,
          "topP": TOP_P,
          "topK": TOP_K
         },
         "user_context": {
          "languageCode: "LANGUAGE_CODE",
          "latLng": {
            "latitude": LATITUDE,
            "longitude": LONGITUDE
          },
         }
         }'
         

Replace the following:

     * `PROJECT_NUMBER`: the number of your Google Cloud project.
     * `PROMPT_TEXT_TURN_1`: the prompt text from the user in the first turn.
     * `SYSTEM_INSTRUCTION_TURN_1`: an optional field to provide a preamble or some additional context. For multi-turn answer generation, you must provide the system instructions for every turn.
     * `MODEL_ID`: an optional field to set the model ID of the Gemini model that you'd like to use to generate the grounded answer. For a list of available model IDs, see [Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models) in the Generative AI on Vertex AI product documentation. 
     * `TEMPERATURE`: an optional field to set the temperature used for sampling. Google recommends a temperature of 0.0. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `TOP_P`: an optional field to set the top-P value for the model. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `TOP_K`: an optional field to set the top-K value for the model. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `LANGUAGE_CODE`: an optional field that might be used to set the language for the generated answer and for the chunk text that is returned. if the language can't be determined from the query, this field is used. The default value is `en`. For a list of language codes, see [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales). 
     * `LATITUDE`: an optional field to set the latitude. Enter the value in decimal degrees—for example, `-25.34`. 
     * `LONGITUDE`: an optional field to set the longitude. Enter the value in decimal degrees—for example, `131.04`. 

#### Response

You should receive a JSON response similar to the following truncated response. To understand your response, see Output data.
    
    {
    "candidates": [
     {
       "content": {
         "role": "model",
         "parts": [
           {
             "text": "ANSWER_TEXT_TURN_1"
           }
         ]
       },
       "groundingScore": GROUNDING_SCORE,
       "groundingMetadata": {
         "supportChunks": [],
         "groundingSupport": [
           {
             "claimText": "CLAIM_TEXT_1",
             "supportChunkIndices": [
               0,
               1
             ]
           },
           {
             "claimText": "CLAIM_TEXT_2",
             "supportChunkIndices": [
               1
             ]
           }
         ],
         "webSearchQueries": [
           "QUERY_BUILT_FROM_USER_PROMPT"
         ],
         "searchEntryPoint": {
           "renderedContent": "RENDERED_CONTENT"
         }
       }
     }
    ]
    } 

  2. Send the second prompt as a follow-up. Add the first prompt from the user followed by its corresponding answer from the model for context.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global:generateGroundedContent" \
         -d '
         {
         "contents": [
          {
            "role": "user",
            "parts": [
              {
                "text": "PROMPT_TEXT_TURN_1"
              }
            ]
          },
          {
            "role": "model",
            "parts": [
              {
                "text": "ANSWER_TEXT_TURN_1"
              }
            ]
          },
          {
            "role": "user",
            "parts": [
              {
                "text": "PROMPT_TEXT_TURN_2"
              }
            ]
          }
         ],
         "systemInstruction": {
            "parts": {
                "text": "SYSTEM_INSTRUCTION_TURN_2"
            }
         },
         "groundingSpec": {
          "groundingSources": [
            {
              "googleSearchSource": {}
            }
          ]
         },
         "generationSpec": {
          "modelId": "MODEL_ID",
          "temperature": TEMPERATURE,
          "topP": TOP_P,
          "topK": TOP_K
         },
         "user_context": {
          "languageCode: "LANGUAGE_CODE",
          "latLng": {
            "latitude": LATITUDE,
            "longitude": LONGITUDE
          },
         }
         }'
         

Replace the following:

     * `PROJECT_NUMBER`: the number of your Google Cloud project.
     * `PROMPT_TEXT_TURN_1`: the prompt text from the user in the first turn.
     * `ANSWER_TEXT_TURN_1`: the answer text from the model in the first turn.
     * `PROMPT_TEXT_TURN_2`: the prompt text from the user in the second turn.
     * `SYSTEM_INSTRUCTION_TURN_2`: an optional field to provide a preamble or some additional context. For multi-turn answer generation, you must provide the system instructions for every turn.
     * `MODEL_ID`: an optional field to set the model ID of the Gemini model that you'd like to use to generate the grounded answer. For a list of available model IDs, see [Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models) in the Generative AI on Vertex AI product documentation. 
     * `TEMPERATURE`: an optional field to set the temperature used for sampling. Google recommends a temperature of 0.0. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `TOP_P`: an optional field to set the top-P value for the model. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `TOP_K`: an optional field to set the top-K value for the model. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `LANGUAGE_CODE`: an optional field that might be used to set the language for the generated answer and for the chunk text that is returned. if the language can't be determined from the query, this field is used. The default value is `en`. For a list of language codes, see [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales). 
     * `LATITUDE`: an optional field to set the latitude. Enter the value in decimal degrees—for example, `-25.34`. 
     * `LONGITUDE`: an optional field to set the longitude. Enter the value in decimal degrees—for example, `131.04`. 

#### Response

You should receive a JSON response similar to the following truncated response. To understand your response, see Output data.
    
    {
    "candidates": [
     {
       "content": {
         "role": "model",
         "parts": [
           {
             "text": "ANSWER_TEXT_TURN_2"
           }
         ]
       },
       "groundingScore": GROUNDING_SCORE,
       "groundingMetadata": {
         "supportChunks": [],
         "groundingSupport": [
           {
             "claimText": "CLAIM_TEXT_1",
             "supportChunkIndices": [
               0
             ]
           },
           {
             "claimText": "CLAIM_TEXT_2",
             "supportChunkIndices": [
               1,
               2
             ]
           }
         ],
         "webSearchQueries": [
           "QUERY_BUILT_FROM_USER_PROMPT"
         ],
         "searchEntryPoint": {
           "renderedContent": "RENDERED_CONTENT"
         }
       }
     }
    ]
    }   

  3. Repeat this process to get further follow-up answers. In each turn, add all the previous prompts from the user followed by their corresponding answers from the model.




### Example for multi-turn answer generation

In the following example, the request specifies three inline fact texts as the grounding source to generate answers over two turns. This sample uses the `generateGroundedContent` method. This example also uses a system instruction to end the answer in the first turn with a smiley emoji.

**Note:** The generated answer in the response might vary.

### REST

  1. Send the first prompt in the following curl request.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/123456/locations/global:generateGroundedContent" \
         -d '
         {
         "contents": [
          {
            "role": "user",
            "parts": [
              {
                "text": "Summarize what happened in 2023 in one paragraph."
              }
            ]
          }
         ],
         "systemInstruction": {
           "parts": {
               "text": "Add a smiley emoji after the answer."
           }
         },
         "grounding_spec": {
          "grounding_sources": [
            {
              "inline_source": {
                "grounding_facts": [
                  {
                    "fact_text": "In 2023, the world population surpassed 8 billion. This milestone marked a significant moment in human history, highlighting both the rapid growth of our species and the challenges of resource management and sustainability in the years to come.",
                    "attributes": {
                      "title": "title_1",
                      "uri": "some-uri-1"
                    }
                  }
                ]
              }
            },
            {
              "inline_source": {
                "grounding_facts": [
                  {
                    "fact_text": "In 2023, global e-commerce sales reached an estimated $5.7 trillion. The continued rise of online shopping solidified its position as a dominant force in retail, with major implications for traditional brick-and-mortar stores and the logistics networks supporting worldwide deliveries.",
                    "attributes": {
                      "title": "title_2",
                      "uri": "some-uri-2"
                    }
                  }
                ]
              }
            },
            {
              "inline_source": {
                "grounding_facts": [
                  {
                    "fact_text": "In 2023, the global average surface temperature was approximately 0.2 degrees Celsius higher than the 20th-century average. This continued the worrying trend of global warming, underscoring the urgency of worldwide climate initiatives, carbon reduction efforts, and investment in renewable energy sources.",
                    "attributes": {
                      "title": "title_3",
                      "uri": "some-uri-3"
                    }
                  }
                ]
              }
            }
          ]
         },
         "generationSpec": {
          "modelId": "gemini-2.5-flash"
         }
         }'
         

#### Response

You should receive a JSON response similar to the following truncated response. To understand your response, see Output data.
         
         {
         "candidates": [
          {
            "content": {
              "role": "model",
              "parts": [
                {
                  "text": "In 2023, the global average surface temperature increased, the world population surpassed 8 billion, and global e-commerce sales reached an estimated $5.7 trillion.  😊 \n"
                }
              ]
            },
            "groundingScore": 1,
            "groundingMetadata": {
              "supportChunks": [
                {
                  "chunkText": "In 2023, global e-commerce sales reached an estimated $5.7 trillion. The continued rise of online shopping solidified its position as a dominant force in retail, with major implications for traditional brick-and-mortar stores and the logistics networks supporting worldwide deliveries. ",
                  "source": "1",
                  "sourceMetadata": {
                    "uri": "some-uri-2",
                    "title": "title_2"
                  }
                },
                {
                  "chunkText": "In 2023, the world population surpassed 8 billion. This milestone marked a significant moment in human history, highlighting both the rapid growth of our species and the challenges of resource management and sustainability in the years to come. ",
                  "source": "0",
                  "sourceMetadata": {
                    "uri": "some-uri-1",
                    "title": "title_1"
                  }
                },
                {
                  "chunkText": "In 2023, the global average surface temperature was approximately 0.2 degrees Celsius higher than the 20th-century average. This continued the worrying trend of global warming, underscoring the urgency of worldwide climate initiatives, carbon reduction efforts, and investment in renewable energy sources. ",
                  "source": "2",
                  "sourceMetadata": {
                    "title": "title_3",
                    "uri": "some-uri-3"
                  }
                }
              ],
              "groundingSupport": [
                {
                  "claimText": "In 2023, the global average surface temperature increased, the world population surpassed 8 billion, and global e-commerce sales reached an estimated $5.7 trillion.",
                  "supportScore": 1,
                  "supportChunkIndices": [
                    0,
                    1,
                    2
                  ]
                }
              ]
            }
          }
         ]
         }
         

  2. Send the second prompt as a follow-up. Add the first prompt from the user followed by its corresponding answer from the model for context.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/123456/locations/global:generateGroundedContent" \
         -d '
         {
         "contents": [
          {
            "role": "user",
            "parts": [
              {
                "text": "Summarize what happened in 2023 in one paragraph."
              }
            ]
          },
          {
            "role": "model",
            "parts": [
              {
                "text": "In 2023, the global average surface temperature increased, the world population surpassed 8 billion, and global e-commerce sales reached an estimated $5.7 trillion.  😊 \n"
              }
            ]
          },
          {
            "role": "user",
            "parts": [
              {
                "text": "Rephrase the answer in an abstracted list."
              }
            ]
          }
         ],
         "grounding_spec": {
          "grounding_sources": [
            {
              "inline_source": {
                "grounding_facts": [
                  {
                    "fact_text": "In 2023, the world population surpassed 8 billion. This milestone marked a significant moment in human history, highlighting both the rapid growth of our species and the challenges of resource management and sustainability in the years to come.",
                    "attributes": {
                      "title": "title_1",
                      "uri": "some-uri-1"
                    }
                  }
                ]
              }
            },
            {
              "inline_source": {
                "grounding_facts": [
                  {
                    "fact_text": "In 2023, global e-commerce sales reached an estimated $5.7 trillion. The continued rise of online shopping solidified its position as a dominant force in retail, with major implications for traditional brick-and-mortar stores and the logistics networks supporting worldwide deliveries.",
                    "attributes": {
                      "title": "title_2",
                      "uri": "some-uri-2"
                    }
                  }
                ]
              }
            },
            {
              "inline_source": {
                "grounding_facts": [
                  {
                    "fact_text": "In 2023, the global average surface temperature was approximately 0.2 degrees Celsius higher than the 20th-century average. This continued the worrying trend of global warming, underscoring the urgency of worldwide climate initiatives, carbon reduction efforts, and investment in renewable energy sources.",
                    "attributes": {
                      "title": "title_3",
                      "uri": "some-uri-3"
                    }
                  }
                ]
              }
            }
          ]
         },
         "generationSpec": {
          "modelId": "gemini-2.5-flash"
         }
         }'
         

#### Response

You should receive a JSON response similar to the following truncated response. To understand your response, see Output data.
         
         {
         "candidates": [
          {
            "content": {
              "role": "model",
              "parts": [
                {
                  "text": "- The global average surface temperature increased in 2023.\n- The world population surpassed 8 billion in 2023.\n- Global e-commerce sales reached an estimated $5.7 trillion in 2023. \n"
                }
              ]
            },
            "groundingScore": 0.99073017,
            "groundingMetadata": {
              "supportChunks": [
                {
                  "chunkText": "In 2023, the global average surface temperature was approximately 0.2 degrees Celsius higher than the 20th-century average. This continued the worrying trend of global warming, underscoring the urgency of worldwide climate initiatives, carbon reduction efforts, and investment in renewable energy sources. ",
                  "source": "2",
                  "sourceMetadata": {
                    "uri": "some-uri-3",
                    "title": "title_3"
                  }
                },
                {
                  "chunkText": "In 2023, the world population surpassed 8 billion. This milestone marked a significant moment in human history, highlighting both the rapid growth of our species and the challenges of resource management and sustainability in the years to come. ",
                  "source": "0",
                  "sourceMetadata": {
                    "uri": "some-uri-1",
                    "title": "title_1"
                  }
                },
                {
                  "chunkText": "In 2023, global e-commerce sales reached an estimated $5.7 trillion. The continued rise of online shopping solidified its position as a dominant force in retail, with major implications for traditional brick-and-mortar stores and the logistics networks supporting worldwide deliveries. ",
                  "source": "1",
                  "sourceMetadata": {
                    "title": "title_2",
                    "uri": "some-uri-2"
                  }
                }
              ],
              "groundingSupport": [
                {
                  "claimText": "- The global average surface temperature increased in 2023.",
                  "supportScore": 0.9883382,
                  "supportChunkIndices": [
                    0
                  ]
                },
                {
                  "claimText": "- The world population surpassed 8 billion in 2023.",
                  "supportScore": 0.9919262,
                  "supportChunkIndices": [
                    1
                  ]
                },
                {
                  "claimText": "- Global e-commerce sales reached an estimated $5.7 trillion in 2023.",
                  "supportScore": 0.9919262,
                  "supportChunkIndices": [
                    2
                  ]
                }
              ]
            }
          }
         ]
         }
         




## Stream grounded answers

**Experimental**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can choose to stream the answers from the model. This is useful in those use cases where the answer is especially long and sending the entire response all at once causes a significant delay. Streaming the answer breaks down the response into an array of several candidates that contain sequential parts of the answer text.

To obtain a streamed, grounded answer, do the following:

### REST

The following sample shows how to stream a grounded answer. This sample uses the `streamGenerateGroundedContent` method and grounds the answer with Google Search without the dynamic retrieval configuration. You can use similar steps to generate grounded answers using other grounding sources.

  1. Send the prompt in the following curl request.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/global:streamGenerateGroundedContent" \
         -d '
         [
         {
          "contents": [
            {
              "role": "user",
              "parts": [
                {
                  "text": "PROMPT_TEXT"
                }
              ]
            }
          ],
          "systemInstruction": {
              "parts": {
                  "text": "SYSTEM_INSTRUCTION"
              }
          },
          "groundingSpec": {
            "groundingSources": [
              {
                "googleSearchSource": {}
              }
            ]
          },
         "generationSpec": {
          "modelId": "MODEL_ID",
          "temperature": TEMPERATURE,
          "topP": TOP_P,
          "topK": TOP_K
         },
         "user_context": {
          "languageCode: "LANGUAGE_CODE",
          "latLng": {
            "latitude": LATITUDE,
            "longitude": LONGITUDE
          },
         }
         }
         ]'
         

Replace the following:

     * `PROJECT_NUMBER`: the number of your Google Cloud project.
     * `PROMPT_TEXT`: the prompt from the user. 
     * `SYSTEM_INSTRUCTION`: an optional field to provide a preamble or some additional context. 
     * `MODEL_ID`: an optional field to set the model ID of the Gemini model that you'd like to use to generate the grounded answer. For a list of available model IDs, see [Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models) in the Generative AI on Vertex AI product documentation. 
     * `TEMPERATURE`: an optional field to set the temperature used for sampling. Google recommends a temperature of 0.0. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `TOP_P`: an optional field to set the top-P value for the model. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `TOP_K`: an optional field to set the top-K value for the model. For more information, see [Gemini model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#parameters). 
     * `LANGUAGE_CODE`: an optional field that might be used to set the language for the generated answer and for the chunk text that is returned. if the language can't be determined from the query, this field is used. The default value is `en`. For a list of language codes, see [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales). 
     * `LATITUDE`: an optional field to set the latitude. Enter the value in decimal degrees—for example, `-25.34`. 
     * `LONGITUDE`: an optional field to set the longitude. Enter the value in decimal degrees—for example, `131.04`. 

#### Response

You should receive a JSON response similar to the following truncated response. To understand your response, see Output data.
    
    [{
     "candidates": [
       {
         "content": {
           "role": "model",
           "parts": [
             {
               "text": "ANSWER_TEXT_PART_1"
             }
           ]
         }
       }
     ]
    },
    {
     "candidates": [
       {
         "content": {
           "role": "model",
           "parts": [
             {
               "text": "ANSWER_TEXT_PART_2"
             }
           ]
         }
       }
     ]
    },
    {
     "candidates": [
       {
         "content": {
           "role": "model",
           "parts": [
             {
               "text": "ANSWER_TEXT_PART_3"
             }
           ]
         }
       }
     ]
    },
    {
     "candidates": [
       {
         "groundingMetadata": {
           "supportChunks": [
             {
              "source": "0",
              "sourceMetadata": {
                "uri": "REDIRECTION_URI",
                "domain": "PUBLISHER_DOMAIN"
              }
             }
           ],
           "groundingSupport": [
             {
               "claimText": "CLAIM_TEXT_1",
               "supportChunkIndices": [
                 0
               ]
             }
           ],
           "webSearchQueries": [
             "QUERY_BUILT_FROM_USER_PROMPT"
           ],
           "searchEntryPoint": {
             "renderedContent": "RENDERED_CONTENT"
           }
         }
       }
     ]
    }]
    




### Python
    
    
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    
    client = discoveryengine.GroundedGenerationServiceClient()
    
    request = discoveryengine.GenerateGroundedContentRequest(
        # The full resource name of the location.
        # Format: projects/{project_number}/locations/{location}
        location=client.common_location_path(project=project_number, location="global"),
        generation_spec=discoveryengine.GenerateGroundedContentRequest.GenerationSpec(
            model_id="gemini-2.5-flash",
        ),
        # Conversation between user and model
        contents=[
            discoveryengine.GroundedGenerationContent(
                role="user",
                parts=[
                    discoveryengine.GroundedGenerationContent.Part(
                        text="Summarize how to delete a data store in Vertex AI Agent Builder?"
                    )
                ],
            )
        ],
        grounding_spec=discoveryengine.GenerateGroundedContentRequest.GroundingSpec(
            grounding_sources=[
                discoveryengine.GenerateGroundedContentRequest.GroundingSource(
                    google_search_source=discoveryengine.GenerateGroundedContentRequest.GroundingSource.GoogleSearchSource()
                ),
            ]
        ),
    )
    responses = client.stream_generate_grounded_content(iter([request]))
    
    for response in responses:
        # Handle the response
        print(response)

### Example for streaming grounded answers

In the following example, the request specifies Google Search as the grounding source to stream an answer without the dynamic retrieval configuration. The streamed answer is distributed over several response candidates. This sample uses the `streamGenerateGroundedContent` method.

**Note:** The generated answer in the response might vary.

### REST
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1alpha/projects/123456/locations/global:streamGenerateGroundedContent" \
    -d '
    [
    {
      "contents": [
        {
          "role": "user",
          "parts": [
            {
              "text": "Summarize How to delete a data store in Agent Search?"
            }
          ]
        }
      ],
      "groundingSpec": {
        "groundingSources": [
          {
            "googleSearchSource": {}
          }
        ]
      },
      "generationSpec": {
        "modelId": "gemini-2.5-flash"
      }
    }
    ]'
    

#### Response

You should receive a JSON response similar to the following truncated response. To understand your response, see Output data.
    
    
    [{
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": "To"
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": " delete a data store in Agent Search, you must first purge all data"
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": " from the data store. "
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "groundingMetadata": {
          "supportChunks": [
            {
              "source": "0",
              "sourceMetadata": {
                "uri": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/{unique_string}",
                "domain": "cloud.google.com"
              }
            }
          ],
          "groundingSupport": [
            {
              "claimText": "To delete a data store in Agent Search, you must first purge all data from the data store. ",
              "supportChunkIndices": [
                0
              ]
            }
          ],
          "webSearchQueries": [
            "how to delete a data store in Agent Search"
          ],
          "searchEntryPoint": {
          }
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": "You can purge data from a data store"
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": " using the Google Cloud console or the command line. "
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "groundingMetadata": {
          "groundingSupport": [
            {
              "claimText": "You can purge data from a data store using the Google Cloud console or the command line. ",
              "supportChunkIndices": [
                0
              ]
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": "Once the data is purged, you can delete the data store. "
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "groundingMetadata": {
          "groundingSupport": [
            {
              "claimText": "Once the data is purged, you can delete the data store. ",
              "supportChunkIndices": [
                0
              ]
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": "You cannot delete"
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": " a data store that is connected to an app. "
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "groundingMetadata": {
          "groundingSupport": [
            {
              "claimText": "You cannot delete a data store that is connected to an app. ",
              "supportChunkIndices": [
                0
              ]
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": "You must first delete the app that the data store is connected to. "
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "groundingMetadata": {
          "groundingSupport": [
            {
              "claimText": "You must first delete the app that the data store is connected to. ",
              "supportChunkIndices": [
                0
              ]
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": "You also"
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": " cannot delete a data store that is in the process of upgrading or downgrading. "
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "groundingMetadata": {
          "groundingSupport": [
            {
              "claimText": "You also cannot delete a data store that is in the process of upgrading or downgrading. ",
              "supportChunkIndices": [
                0
              ]
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": "You must wait for the upgrade or downgrade to complete before deleting the data store."
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": " \n"
            }
          ]
        }
      }
    ]
    }
    ,
    {
    "candidates": [
      {
        "groundingMetadata": {
          "groundingSupport": [
            {
              "claimText": "You must wait for the upgrade or downgrade to complete before deleting the data store. \n",
              "supportChunkIndices": [
                0
              ]
            }
          ]
        }
      }
    ]
    }
    ]
    

## What's next

Learn how to use the grounded generation method with other RAG APIs to [generate grounded answers from unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/builder-apis#builder-apis-workflow).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
