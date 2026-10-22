---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/custom-ranking/
title: Customize search results ranking \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:12.673296+00:00
---

# Customize search results ranking  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/custom-ranking/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Customize search results ranking Stay organized with collections  Save and categorize content based on your preferences. 

Because search needs can differ for different industries and can vary from time to time, the default ranking behavior might not be optimal for every business need. To address this, you can modify the ranking behavior using custom ranking.

This page describes how to use a custom ranking formula in your search request and how to tune the formula. This feature is available for structured, unstructured, and website data.

## Overview

Custom ranking lets you provide a mathematical expression that relies on a set of model-computed signals, such as semantic relevance score and keyword similarity score; and document-based signals, such as a custom field like distance or document age.

With custom ranking, you can achieve the following:

  * **Gain visibility** : Understand which signals contribute to the final ranking of your search results.
  * **Tune existing signals** : Adjust the weights of various signals like semantic similarity, keyword matching, or document freshness.
  * **Incorporate business logic** : Add your own custom signals from your document data directly into the ranking formula.
  * **Optimize systematically** : Use the open-source Python library to programmatically discover the optimal ranking formula.



## Need for custom ranking—an example

Consider a scenario where the following string is queried on a hotel booking website:
    
    
    luxury hotel with a large rooftop pool in Vancouver, pet-friendly and close to airport.
    

Say, the following entries are retrieved:

  * **Hotel A:** "Vancouver's premier **luxury** hotel overlooking the **airport**. Features a stunning **rooftop pool**. _No pets allowed._ "
  * **Hotel B:** "Modern, _stylish_ hotel in _downtown Vancouver_. **Pet-friendly** with spacious rooms. Features a large _indoor pool_ and fitness center."
  * **Hotel C:** "A charming **pet-friendly** boutique hotel near Aquarium (a _10-minute walk from downtown_). Features a lovely garden courtyard. _No pool._ "
  * **Hotel D:** "An iconic _rustic_ resort. Known for its exquisite dining and impeccable service. Features an _indoor pool_ and spa. **Pet-friendly** options available on request."



All hotels in the catalog include a field `distance_from_airport` in kilometers (km).

### Embedding-based ranking

The search system converts the query into a single embedding. It then compares this query embedding to the embeddings of all hotels in its catalog. Hotels with embeddings that are numerically closest to the query's embedding are ranked higher.

Here's the likely ranking from a purely embedding-based relevance search:

Ranking | Hotel | Possible reason for this ranking  
---|---|---  
1 | **Hotel A** | Very strong semantic match for luxury, airport, rooftop pool. The "no pets" isn't desirable, but the other strong matches dominate.  
2 | **Hotel B** | Good semantic match for "pet-friendly" and "pool". But "indoor" instead of "rooftop", "modern" and "stylish" instead of "luxury" and "downtown" instead of "airport" make it less relevant than A.  
3 | **Hotel D** | Strong semantic match for pet-friendly, large pool, but "indoor" instead of "rooftop" and "rustic" instead of "luxury" make it slightly less semantically relevant than A and B.  
4 | **Hotel C** | Strong pet-friendly, but "no pool" and "boutique" significantly reduce its relevance to this specific query.  
  
This ranking doesn't deliver the most relevant results. Hotel A is ranked at the top, even though with "no pets allowed" it might not be preferred by many users. Hotel D, fits many criteria, is ranked lower because its "rustic" status doesn't necessarily map to "luxury" and the "indoor" pool is ranked lower than exact matches of "large" and "outdoor".

### Custom ranking

Say, you have configured the following ranking expression for this example scenario. For information about the components of this expression, see About implementing custom ranking.
    
    
    rankingExpression = drr(semantic_similarity_score, 32) * 0.4 + drr(keyword_similarity_score, 32) * 0.3 + drr(c.distance_from_airport * -1, 32) * 0.8
    

Where `distance_from_airport` is a retrievable field in the catalog and `c.distance_from_airport` acts as a signal.

In custom ranking, you consider different signals that influence the relevance of a document. Then, you create a mathematical expression containing these signals using a valid syntax. In this expression, you normalize the signals and add weights to their derived scores. The final custom score is calculated and the documents are ranked.

In this example, this process can be explained as follows:

  1. Each hotel is awarded a semantic similarity score and a keyword similarity score. Additionally, distance from the airport is an important signal derived from the document.

  2. The dense reciprocal rank transformation function or `drr()` is used to transform all the scores to the same scale.

  3. The score derived from each signal is given a weight and then the sum of all the individual scores becomes the custom-ranking score for each hotel.




The different signals for each hotel are tabulated as follows:

Hotel | `semantic_similarity_score` | `keyword_similarity_score` | `c.distance_from_airport` | Custom ranking score | Custom ranking | Embedding-based ranking  
---|---|---|---|---|---|---  
Hotel A | 9.0 | 6.2 ("airport", "luxury", "rooftop pool") | 5.0 | 0.04879 | 2 | 1  
Hotel B | 7.5 | 5.6 ("pet-friendly", "downtown", "indoor pool", "stylish") | 12.5 | 0.04691 | 3 | 2  
Hotel C | 5.0 | 3.4 ("pet-friendly", "downtown") | 18 | 0.04525 | 4 | 4  
Hotel D | 8.0 | 4.5 ("indoor pool", "pet-friendly", "rustic") | 1 | 0.04890 | 1 | 3  
  
Comparing the two ranking methods, custom ranking gives a more considered ranking that likely matches a user's needs better than a purely embedding-based ranking.

## About implementing custom ranking

To get custom ranking in your search results, you must call the [`search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) method by providing the following fields:

  * **Ranking expression backend** (`rankingExpressionBackend`): This field indicates which of the following ranking mechanisms is to be used.

    * `RANK_BY_EMBEDDING`: This is the default value when this field is unspecified. Choosing this ranks the results according to a predefined ranking expression that's either embedding-based or relevance-based.
    * `RANK_BY_FORMULA`: This overrides the default ranking and lets you provide your custom formula in the `rankingExpression` field.
  * **Ranking expression** (`rankingExpression`): This field contains a mathematical formula that decides the ranking of the retrieved documents.

    * For `RANK_BY_EMBEDDING`, this is either relevance-score based (`double * relevanceScore`) or embedding-based (`double * dotProduct(embedding_field_path)`).

    * For `RANK_BY_FORMULA`, this is a curated expression that combines multiple signals to compute a new score for each search result.




### Standard signals

Agent Search offers a variety of signals that you can use to formulate custom ranking. Here are the standard signals available:

Signal name | Description  
---|---  
`default_rank` | The default rank of the document as determined by the standard Agent Search ranking algorithm.  
`semantic_similarity_score` | A score computed based on query and content embeddings to determine how similar is a search query to a document's content. This is computed using a proprietary Google algorithm.  
`relevance_score` | A score produced by a deep-relevance model, which handles complex query-document interactions. The model determines the meaning and intention of a query in the context of the content. This is computed using a proprietary Google algorithm.  
`keyword_similarity_score` | A score with a strong emphasis on keyword matching. This signal uses the Best Match 25 (BM25) ranking function.  
`document_age` | The age of the document in hours. Supports floating point values. For example, a value of 0.5 means 30 minutes while 50 means 2 days and 2 hours. For `document_age` to be non-zero, fields in the schema must be mapped to the key properties `update_time` and `create_time`. These fields are used to calculate `document_age`. If `update_time` isn't available, custom ranking uses `create_time` as a fallback to determine `document_age`. For how to map key properties, see [ Update your schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas#update-schema).   
`pctr_rank` | A rank to denote predicted conversion rates, computed based on user event data. This signal uses predicted Click-through rate (pCTR) to gauge the relevance of a search result from a user's perspective.  
`topicality_rank` | A rank to denote keyword similarity adjustment computed using a proprietary Google algorithm.  
`boosting_factor` | A combination of all custom boosts you have applied to the document.  
  
### Custom signals

In addition to the standard signals, you can use signals from any numeric custom field in a document that is marked as retrievable. To do so, add `c.` prefix to their field names. For example, if you have a custom field named `date_approved`, then you can use `c.date_approved` as a custom signal.

Signal names are a combination of alphabetical characters and underscores (`_`). The following is a list of reserved names that can't be used as signal names: `log`, `exp`, `rr`, `drr`, `is_nan`, `fill_nan`, and `geo_distance`.

### Geodistance—a derived signal

Derived signals, such as geodistance, are computed based on standard and custom signals. Geodistance is a function that computes the distance between a source and a destination location. The `geo_distance()` function is expressed as `geo_distance(source_location, destination_location)`. It is composed of the following arguments:

  * The source location or `source_location`: The origin for calculating distance, which can be one of the following types:

    * **Query location** : the location that's parsed from the query using natural language understanding models. For example, in the query `Hotels along the M6`, the natural language understanding model extracts `Hotels` as the _what_ and `M6` as the _where_ part of the search parameters. The _where_ part is the query location and can be represented as a point, polyline, circle, or polygon.
          
          {
           "query": "Hotels along M6",
           "ranking_expression": "geo_distance(query_loc, c.hotel_location)",
           "ranking_expression_backend": "RANK_BY_FORMULA"
          }
          

    * **Request location coordinates** : a location that's explicitly provided in the search request, such as a user's latitude and longitude. For example, you can provide the query as `Hotels` and provide a location using the latitude and longitude.
          
          {
            "query": "Hotels",
            "user_info": {
              "precise_location": {
                "point": {
                  "latitude": 52.23034637633789,
                  "longitude": 20.98339855121653
                }
              }
            },
            "ranking_expression": "geo_distance(request_loc, c.hotel_location)",
            "ranking_expression_backend": "RANK_BY_FORMULA"
          }
          

    * **Request location address** : an address that's explicitly provided in the search request. For example, you can provide the query as `Hotels` and provide an address for reference.
          
          {
            "query": "Hotels",
            "user_info": {
              "precise_location": {
                "address": "1800 Amphibious Blvd. Mountain View, CA 94045"
              }
            },
            "ranking_expression": "geo_distance(request_loc, c.hotel_location)",
            "ranking_expression_backend": "RANK_BY_FORMULA"
          }
          

  * The destination location or `destination_location`: The destination for calculating distance, which is a custom retrievable field such as `c.office_location` or `c.home_location`.




The order of these arguments within the function must remain the same. That is, the source location must always be the first argument within the `geo_distance()` function followed by the destination location. The function computes the distance, in meters, using the latitude and longitude of the source and destination locations.

### Ranking formula syntax

The custom ranking formula is a mathematical expression with the following components:

  * **Numbers (`double`)**: A positive or negative floating-point values that adds a weight to a signal or an expression.

  * **Signals (`signal`)**: The names of the signals listed in the Standard signals section.

  * **Arithmetic operators** : `+` (addition) and `*` (multiplication).

  * **Mathematical functions** :

    * `log(expression)`: The natural logarithm
    * `exp(expression)`: The natural exponent

Each of these expressions accepts exactly one argument, which is an expression written in terms of a signal.

Examples of a valid function: `exp(c.document_age)` and `log(keywordSimilarityScore * 0.2 + 1.0)`.

  * **Dense reciprocal rank transformation function (`drr`)**:

This function is expressed as `drr(expression, k, eps)`. It first sorts documents by the value of the `expression` in descending order and assigns the documents a rank. When the expression values are within `eps` apart, the values are considered equal. The function then calculates the final value using the expression `1 / (rank_i + k)`. In this expression, `rank_i` is the document's position in the sorted list starting from 0 and `k` is a positive floating-point number you provide.

The `drr()` function is typically used to transform all scores to the same scale and eliminate the need for additional normalization.

Google recommends that you use this function over the earlier reciprocal rank transformation function (`rr`) because it gives better results in cases where signals are tied for the top results, for example, if the search is for hotels in San Francisco, there are many hotels within the city limits, so many hotels share the same geodistance signal.

More about the `eps` parameter:

    * The `eps` parameter adds flexibility when determining if two signals are equal. Equivalent signals are most commonly found for signals of type: `boosting_factor`, `geo_distance`, categorical custom and integer custom.

    * The function determines if the expression value from one document is equal to the expression value from another doc. If `eps=0`, then the values must be exactly the same to be considered equal; if `eps>0`, then the values within the range specified by `eps` are considered equal.

    * More specifically, if `x1` and `x2` are signal values, they are considered to be the same value if the absolute difference between the two is less than or equal to `eps`, that is, if `abs(x1-x2) <= eps`. By default, `eps=0`, which means that the values are considered the same if `x1 == x2`. The default of `eps=0` works well for integers, but can fail in some cases for floats because of the imprecise nature of floating point arithmetic, for example, where 1/5 might evaluate to `0.20000000000001` or to `0.19999999999`.

  * **Reciprocal rank transformation function (`rr`)**: This function is expressed as `rr(expression, k)`. It first sorts documents by the value of the `expression` in descending order and assigns the documents a rank. It then calculates the final value using the expression `1 / (rank_i + k)`. In this expression, `rank_i` is the document's position in the sorted list starting from 0 and `k` is a positive floating-point number you provide.

The `rr()` function is typically used to transform all scores to the same scale and eliminate the need for additional normalization.

Although this function is supported, Google recommends the newer dense reciprocal rank transformation function (`drr`).

  * **Not a number (NaN) handling functions** :

    * `is_nan(expression)`: When the expression evaluates to being NaN, such as when a signal is missing for a document, `1` is returned. Otherwise, `0` is returned.
    * `fill_nan(arg_expression, fill_with_expression)`: If `arg_expression` evaluates to being a NaN, returns `fill_with_expression`. Otherwise, returns `arg_expression`. This is crucial for handling documents that might be missing certain signals.



### Ranking formula examples

Here are a few examples of ranking formula that you can use in the `rankingExpression` field of your search request:

  * An elementary linear combination:
        
        semantic_similarity_score * 0.7 + keyword_similarity_score * 0.3
        

  * A complex formula using dense reciprocal rank and NaN handling:
        
        drr(fill_nan(semantic_similarity_score, 0), 40) * 0.5 + drr(topicality_rank * -1, 40) * 0.5
        

  * A complex formula using dense reciprocal rank, exponential function, and NaN handling:
        
        drr(fill_nan(semantic_similarity_score, 0), 40) * 0.2 + exp(keyword_similarity_score) * 0.3 + is_nan(keyword_similarity_score) * 0.1
        

  * A complex formula using dense reciprocal rank with the `geo_distance()` function, illustrating the use of the `eps` parameter with the `geo_distance()` function:
        
        drr(keyword_similarity_score, 16) * 0.8 + drr(geo_distance(query_loc, c.office_location) * -1, 16, 0.00001) * 0.2
        

In this formula, the multiplication factor is a negative value so that a larger distance corresponds to smaller (more negative) expression value and, therefore, the reciprocal rank assigns a lower ranking score to greater distances.




### Signals in the response

When a document is returned in the search response, the search result lists the standard and custom signals that contribute to retrieving the document from the data store. The [`rankSignals`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SearchResult#RankSignals) field lists these signals.

### Text fields for keyword similarity

In structured data stores, to obtain the `keywordSimilarityScore` signal in your search response, you must [update your schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas#update-schema) to do the following:

  * Map the text fields essential for keyword matching to the key properties `title` and `description`
  * Update the annotation for the text fields as `Searchable`



## Customize ranking using ranking formula in search

To customize the ranking for your documents in your search results, manually draft a formula and add it to your [`search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) API call.

  1. Formulate a ranking expression.

  2. Get search results.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
         "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
         "query": "QUERY",
         "rankingExpression": "RANKING_EXPRESSION",
         "rankingExpressionBackend": "RANK_BY_FORMULA"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query.
     * `QUERY`: the query text to search.
     * `RANKING_EXPRESSION`: the custom ranking formula that you can write using the available signals with a valid ranking formula syntax.

       * For valid examples, see Ranking formula examples.
       * To tune the ranking formula, which can give you the best results, see Tune ranking formula using the Python library.

#### Example command and partial result
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:search" \
    -d '{
          "servingConfig": "projects/my-project-123/locations/us/collections/default_collection/dataStores/my-data-store/servingConfigs/default_config",
          "query": "psychologist",
          "userInfo": {
            "preciseLocation": {
              "point": {
                "latitude": 40.0193498,
                "longitude": -105.2684099
              }
            }
          },
          "rankingExpression": "drr(default_rank * -1, 16) + drr(geo_distance(request_loc, c.geolocation) * -1, 16, 0.00001) * 0.8",
          "rankingExpressionBackend": "RANK_BY_FORMULA",
          "customRankingParams": {
            "expressionsToPrecompute": ["geo_distance(request_loc, c.geolocation)"]
          }
        }'
        
    
    * * *
    
    
    {
      "results": [{
        "id": "123456789f35fe90f22612713a7e875c",
        "document": {
          "name": "projects/my-project-123/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/123456789f35fe90f22612713a7e875c",
          "id": "123456789f35fe90f22612713a7e875c",
          "structData": {
            ...
            "full_address": "5992 Maple St Franklin NM 87505",
            "generatedKey": "1234567-123456789-T-123456789CD9EAB7CC3FBECA9158B289",
            "geolocation": {
              "address": "5992 Maple St Franklin NM 87505"
            },
            ...
          }
        },
        "rankSignals": {
          "keywordSimilarityScore": 0.8188466,
          "semanticSimilarityScore": 0.6672727,
          "topicalityRank": 3.0,
          "boostingFactor": 0.0,
          "defaultRank": 1.0,
          "precomputedExpressionValues": [488792.47]
        },
        "retrievalSignals": {
          "retrievalSources": ["KEYWORD_SEARCH", "SEMANTIC_SEARCH"],
          "semanticRelevanceScore": 0.40226308
        }
      }, {
        "id": "123456789746002ab3a03501b2e1874f",
        "document": {
          "name": "projects/my-project-123/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/123456789746002ab3a03501b2e1874f",
          "id": "123456789746002ab3a03501b2e1874f",
          "structData": {
            ...
            "full_address": "6056 Elm Dr Springfield NM 87401",
            "generatedKey": "1234567-123456789-T-123456789761975E686DA90FBFD2BB89",
            "geolocation": {
              "address": "6056 Elm Dr Springfield NM 87401"
            },
            ...
          }
        },
        "rankSignals": {
          "keywordSimilarityScore": 0.8188466,
          "semanticSimilarityScore": 0.66934514,
          "topicalityRank": 2.0,
          "boostingFactor": 0.0,
          "defaultRank": 2.0,
          "precomputedExpressionValues": [443257.2]
        },
        "retrievalSignals": {
          "retrievalSources": ["KEYWORD_SEARCH", "SEMANTIC_SEARCH"],
          "semanticRelevanceScore": 0.37744346
        }
      ...
      }, {
        "id": "123456789474eac8327437f2ad81b103",
        "document": {
          "name": "projects/my-project-123/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/123456789474eac8327437f2ad81b103",
          "id": "123456789474eac8327437f2ad81b103",
          "structData": {
            ...
            "full_address": "4780 Main St Riverside NY 10011",
            "generatedKey": "1234567-123456789-T-123456789E9EEFB0A72810951FD36389",
            "geolocation": {
              "address": "4780 Main St Riverside NY 10011"
            },
            ...
          }
        },
        "rankSignals": {
          "keywordSimilarityScore": 0.0,
          "semanticSimilarityScore": 0.691086,
          "topicalityRank": 61.0,
          "boostingFactor": 0.0,
          "defaultRank": 47.0,
          "precomputedExpressionValues": [2635880.2]
        },
        "retrievalSignals": {
          "retrievalSources": ["SEMANTIC_SEARCH"],
          "semanticRelevanceScore": 0.4156605
        }
      }, {
        "id": "123456789c31f73ac73e9c8de9301217",
        "document": {
          "name": "projects/my-project-123/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/123456789c31f73ac73e9c8de9301217",
          "id": "123456789c31f73ac73e9c8de9301217",
          "structData": {
            ...
            "full_address": "5738 Main St Riverside NY 10016",
            "generatedKey": "1234567-123456789-T-12345678936C42C29E94F3F86EACA689",
            "geolocation": {
              "address": "5738 Main St Riverside NY 10016"
            },
            ...
          }
        },
        "rankSignals": {
          "keywordSimilarityScore": 0.0,
          "semanticSimilarityScore": 0.6795519,
          "topicalityRank": 38.0,
          "boostingFactor": 0.0,
          "defaultRank": 48.0,
          "precomputedExpressionValues": [2637175.0]
        },
        "retrievalSignals": {
          "retrievalSources": ["SEMANTIC_SEARCH"],
          "semanticRelevanceScore": 0.40063128
        }
      }, {
        "id": "1234567899a3eacea2d4960e60784e68",
        "document": {
          "name": "projects/my-project-123/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/1234567899a3eacea2d4960e60784e68",
          "id": "1234567899a3eacea2d4960e60784e68",
          "structData": {
            ...
            "full_address": "5738 Main St Riverside NY 10016",
            "generatedKey": "1234567-123456789-T-12345678936C42C29E94F3F86EACA689",
            "geolocation": {
              "address": "5738 Main St Riverside NY 10016"
            },
            ...
          }
        },
        "rankSignals": {
          "keywordSimilarityScore": 0.0,
          "semanticSimilarityScore": 0.6898086,
          "topicalityRank": 57.0,
          "boostingFactor": 0.0,
          "defaultRank": 49.0,
          "precomputedExpressionValues": [2637175.0]
        },
        "retrievalSignals": {
          "retrievalSources": ["SEMANTIC_SEARCH"],
          "semanticRelevanceScore": 0.41399607
        }
      }, {
        "id": "123456789e996d10a49bdfd9c560e1c5",
        "document": {
          "name": "projects/my-project-123/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/123456789e996d10a49bdfd9c560e1c5",
          "id": "123456789e996d10a49bdfd9c560e1c5",
          "structData": {
            ...
            "full_address": "3750 Elm Dr Georgetown OH 43065",
            "generatedKey": "1234567-123456789-T-123456789818D290812B3E1BC5999489",
            "geolocation": {
              "address": "3750 Elm Dr Georgetown OH 43065"
            },
            ...
          }
        },
        "rankSignals": {
          "keywordSimilarityScore": 0.8188466,
          "semanticSimilarityScore": 0.6374469,
          "topicalityRank": 17.0,
          "boostingFactor": 0.0,
          "defaultRank": 50.0,
          "precomputedExpressionValues": [1881946.8]
        },
        "retrievalSignals": {
          "retrievalSources": ["SEMANTIC_SEARCH"],
          "semanticRelevanceScore": 0.35366622
        }
      }],
      "totalSize": 2591,
      "attributionToken": "kAL0DwEKDAWZhdWx0...iN35rOBhCmlncy9kZX2NvbmZpZw",
      "nextPageToken": "QWZ2AjYzYDN0cDN30yNkNjYtIzM2ITLwADMw0SNhlzM2UWO2QiGCw71ceKEG4sqI7ICMIBM1IgC",
      "guidedSearchResult": {
      },
      "summary": {
      },
      "queryExpansionInfo": {
      },
      "queryInfo": {
        "isAnswerSeeking": false
      },
      "personalizationInfo": {
        "userEventCount": "0"
      },
      "semanticState": "ENABLED"
    }
    

For geolocation, this example includes the `userInfo`, `customRankingParams`, and `expressionsToPrecompute` parameters. 




## Tune ranking formula using the Python library

For more advanced use cases, finding the optimal weights for your formula can be challenging. To overcome this, you can use Agent Search's ranking tuning Python library, which is an open-source tool, and arrive at a suitable formula for your use case.

The general workflow is as follows:

  1. Prepare a dataset of queries with corresponding golden labels. These golden labels can be unique identifying fields, such as the document ID, that can help you associate the `SearchResult` object in the search response.
  2. For a set of representative queries, call the [`search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) API to get the available ranking signals for all returned documents. You can find this in the `SearchResult.rankSignals` field. Store this data along with your golden labels.
  3. Use the Python library to train a ranking model on this dataset. For more information, see [Clearbox Python library](https://github.com/GoogleCloudPlatform/clearbox).

To see an example of custom ranking using a tuned formula, run the "Custom ranking tuning" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/search/custom-ranking/clearbox.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/search/custom-ranking/clearbox.ipynb)

  4. Convert the formula from the training results into a ranking expression, which you can then use in your API calls.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
