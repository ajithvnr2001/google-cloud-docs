---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/check-grounding/
title: Check grounding with RAG \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:43.510519+00:00
---

# Check grounding with RAG  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/check-grounding/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Check grounding with RAG Stay organized with collections  Save and categorize content based on your preferences. 

As part of your Retrieval Augmented Generation (RAG) experience in Agent Search, you can check grounding to determine how grounded a piece of text (called an _answer candidate_) is in a given set of reference texts (called _facts_).

The check grounding API returns an overall support score of 0 to 1, which indicates how much the answer candidate agrees with the given facts. The response also includes _citations_ to the facts supporting each claim in the answer candidate.

Perfect grounding requires that every claim in the answer candidate must be supported by one or more of the given facts. In other words, the claim is wholly entailed by the facts. If the claim is only partially entailed, it is not considered grounded. For example, the claim "Google was founded by Larry Page and Sergey Brin in 1975" is only partially correct—the names of the founders are correct but the date is wrong—and as such the whole claim is considered ungrounded. In this version of the check grounding API, a sentence is considered a single claim.

You can use the check grounding API to check any piece of text. It can be a human-generated blurb or a machine-generated response. A typical use case is to check an LLM-generated response against a given set of facts. The check grounding API is designed to be fast, with latency less than 500ms. This speed allows chat bots to call the check grounding API during each inference, without incurring a significant slowdown. The check grounding API can also provide references to support its findings, so that users can tell which parts of the generated response are reliable. The API also provides a support score to indicate the overall accuracy of the response. By setting a citation threshold, chat bots can filter out responses at inference time that are likely to contain hallucinated claims.

This page describes how to check grounding using the check grounding API.

## Terms defined and explained

Before you use the check grounding API, it helps to understand the inputs and outputs, and how to structure your grounding facts for best results.

### Input data

The check grounding API requires the following inputs in the request.

  * **Answer candidate:** An answer candidate can be any piece of text whose grounding you want to check. For example, in the context of Agent Search, the answer candidate might be the generated search summary that answers a query. The API would then determine how grounded the summary is in the input facts. An answer candidate can have a maximum length of 4096 tokens, where a token is defined as a word in a sentence or a period (a punctuation mark used to end the sentence). For example, the sentence "They wore off-the-rack clothes in 2024." is seven tokens long, including six words and a period.

  * **Facts:** A set of text segments to be used as references for grounding. A set of metadata attributes (key-value pairs) can be supplied with each text segment. For example, "Author" and "Title" are typical attribute keys.

The service supports up to 200 facts, each with a maximum of 10k characters.

Google recommends against supplying one very large fact that contains all of the information. Instead, you can get better results by breaking large facts into smaller facts and supplying appropriate attributes for the smaller facts. For example, you can break up a large fact by title, author, or URL, and supply this information in attributes.

  * **Citation threshold** : A float value from 0 to 1 that controls the confidence for the citations that support the answer candidate. A higher threshold imposes stricter confidence. Therefore, a higher threshold yields fewer but stronger citations.




### Output data

The check grounding API returns the following for an answer candidate:

  * **Support score:** The support score is a number from 0 to 1 that indicates how grounded an answer candidate is in the provided set of facts. It loosely approximates the fraction of claims in the answer candidate that were found to be grounded in one or more of the given facts.

  * **Cited chunks:** Cited chunks are portions of the input facts that support the answer candidate.

  * **Claims and citations:** The claims and citations connect a claim (typically a sentence) of the answer candidate to one or more of the cited chunks that corroborate the claim.

A claim is demarcated using its start and end positions. These are the byte positions of the UTF-8 encoded claim string. Note that this is not measured in characters and, therefore, must be rendered in the user interface keeping in mind that some characters take more than one byte. For example, if the claim text contains non-ASCII characters, the start and end positions vary when measured in characters (programming-language-dependent) and when measured in bytes (programming-language-independent).

  * **Claim-level support score:** When the claim-level score is enabled, with each claim, a support score is returned as a number from 0 to 1 that indicates how grounded the claim is in the provided set of facts. For more information, see Obtain claim-level scores for an answer candidate.

  * **Grounding check required** : With each claim, a grounding-check-required boolean is returned. When this returns as `False`, it means that the system deems that the claim doesn't require grounding, and, therefore, citations aren't returned. For example, a sentence like "Here is what I found." isn't a fact by itself and, thus, doesn't require a grounding check.

When the grounding-check-required returns as `true`, it means that a grounding check was performed and support scores, citations, if any, are returned.




## Obtain a support score for an answer candidate

To find out how grounded an answer candidate is in a set of facts, follow these steps:

  1. Prepare your set of facts. For more information and examples, see Terms defined and explained.

  2. Call the [`check`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.groundingConfigs/check) method using the following code:




### REST
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/groundingConfigs/default_grounding_config:check" \
    -d '{
      "answerCandidate": "CANDIDATE",
      "facts": [
      {
        "factText": "TEXT_0",
        "attributes": {"ATTRIBUTE_A": "VALUE_A0","ATTRIBUTE_B": "VALUE_B0"}
      },
      {
        "factText": "TEXT_1",
        "attributes": {"ATTRIBUTE_A": "VALUE_A1","ATTRIBUTE_B": "VALUE_B1"}
      },
      {
        "factText": "TEXT_2",
        "attributes": {"ATTRIBUTE_A": "VALUE_A2","ATTRIBUTE_B": "VALUE_B2"}
      }
      ],
      "groundingSpec": {
        "citationThreshold": "CITATION_THRESHOLD"
      }
    }'
    

Replace the following:

  * `PROJECT_ID`: the project number or ID of your Google Cloud project.

  * `CANDIDATE`: the answer candidate string for which you want to get a support score—for example, `Titanic was directed by James Cameron. It was released in 1997.` An answer candidate can have a maximum length of 4096 tokens, where a token is defined as a word in a sentence or a period (a punctuation mark used to end the sentence). For example, the sentence "They wore off-the-rack clothes in 2024." is seven tokens long, including six words and a period.

  * `TEXT`: the text segment to be used for grounding—for example, `Titanic is a 1997 American epic... Academy Awards.` (See the full text in Examples of facts.)

  * `ATTRIBUTE`: the name of a metadata attribute associated with the fact—for example, `author` or `title`. This is a user-defined label to add more information to the fact text. For example, if the fact text `Toronto is the capital of Ontario` has an `author` attribute with its value as `Wikipedia`, then the following claims are considered grounded in the fact:

    * `Wikipedia cites that Toronto is the capital of Ontario`
    * `Toronto is the capital of Ontario`

However, the claim that `Government of Ontario claims that Toronto is the capital of Ontario` is not as grounded as the first two claims.

  * `VALUE`: the value for the attribute—for example, `Simple Wikipedia` or `Titanic (1997 film)`.

  * `CITATION_THRESHOLD`: a float value from 0 through 1 that determines whether a fact must be cited for a claim in the answer candidate. A higher threshold leads to fewer but stronger citations and a lower threshold leads to more but weakier citations. If unset, the default threshold value is `0.6`.




### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    
    client = discoveryengine.GroundedGenerationServiceClient()
    
    # The full resource name of the grounding config.
    # Format: projects/{project_id}/locations/{location}/groundingConfigs/default_grounding_config
    grounding_config = client.grounding_config_path(
        project=project_id,
        location="global",
        grounding_config="default_grounding_config",
    )
    
    request = discoveryengine.CheckGroundingRequest(
        grounding_config=grounding_config,
        answer_candidate="Titanic was directed by James Cameron. It was released in 1997.",
        facts=[
            discoveryengine.GroundingFact(
                fact_text=(
                    "Titanic is a 1997 American epic romantic disaster movie. It was directed, written,"
                    " and co-produced by James Cameron. The movie is about the 1912 sinking of the"
                    " RMS Titanic. It stars Kate Winslet and Leonardo DiCaprio. The movie was released"
                    " on December 19, 1997. It received positive critical reviews. The movie won 11 Academy"
                    " Awards, and was nominated for fourteen total Academy Awards."
                ),
                attributes={"author": "Simple Wikipedia"},
            ),
            discoveryengine.GroundingFact(
                fact_text=(
                    'James Cameron\'s "Titanic" is an epic, action-packed romance'
                    "set against the ill-fated maiden voyage of the R.M.S. Titanic;"
                    "the pride and joy of the White Star Line and, at the time,"
                    "the largest moving object ever built. "
                    'She was the most luxurious liner of her era -- the "ship of dreams" -- '
                    "which ultimately carried over 1,500 people to their death in the "
                    "ice cold waters of the North Atlantic in the early hours of April 15, 1912."
                ),
                attributes={"author": "Simple Wikipedia"},
            ),
        ],
        grounding_spec=discoveryengine.CheckGroundingSpec(citation_threshold=0.6),
    )
    
    response = client.check_grounding(request=request)
    
    # Handle the response
    print(response)

### Examples of facts

The following are a couple of examples of facts and their attributes. These examples are to help you understand the grounding response and the format of the curl command.

  * **Fact 0**

    * Text: `"Titanic is a 1997 American epic romantic disaster movie. It was directed, written, and co-produced by James Cameron. The movie is about the 1912 sinking of the RMS Titanic. It stars Kate Winslet and Leonardo DiCaprio. The movie was released on December 19, 1997. It received positive critical reviews. The movie won 11 Academy Awards, and was nominated for fourteen total Academy Awards."`

    * Attributes: `{"Author": "Simple Wikipedia"}`

  * **Fact 1**

    * Text: `"James Cameron's "Titanic" is an epic, action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic; the pride and joy of the White Star Line and, at the time, the largest moving object ever built. She was the most luxurious liner of her era -- the "ship of dreams" -- which ultimately carried over 1,500 people to their death in the ice cold waters of the North Atlantic in the early hours of April 15, 1912."`

    * Attributes: `{"Author": "Rotten Tomatoes"}`




### Example request

After preparing the facts, you can send the following request, replacing the CANDIDATE field with different strings whose grounding you want to check.
    
    
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/groundingConfigs/default_grounding_config:check" \
        -d '{
        "answerCandidate": "CANDIDATE",
        "facts": [
         {
          "factText": "Titanic is a 1997 American epic romantic disaster movie. It was directed, written, and co-produced by James Cameron. The movie is about the 1912 sinking of the RMS Titanic. It stars Kate Winslet and Leonardo DiCaprio. The movie was released on December 19, 1997. It received positive critical reviews. The movie won 11 Academy Awards, and was nominated for fourteen total Academy Awards.",
          "attributes": {"author":"Simple Wikipedia"}
         },
         {
          "factText": "James Cameron&#39;s \"Titanic\" is an epic, action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic; the pride and joy of the White Star Line and, at the time, the largest moving object ever built. She was the most luxurious liner of her era -- the \"ship of dreams\" -- which ultimately carried over 1,500 people to their death in the ice cold waters of the North Atlantic in the early hours of April 15, 1912.",
          "attributes": {"author":"Simple Wikipedia"}
         }
        ],
        "groundingSpec": {
          "citationThreshold": "0.6"
        }
        }'
    

**Note:** The double quotes are escaped with the backslash character, and the apostrophe is replaced by its HTML character entity.

### Examples of answer candidates and grounding responses

The following table shows examples of different answer candidates and responses when you send the example request, based on the example facts.

Answer candidate | Check grounding response  
---|---  
`Here is what I found. Titanic was directed by James Cameron.` |  Support score: `0.99`  
  
Cited chunks: 

  0. `[From FACT 0]....Titanic is a 1997 American epic romantic disaster movie. It was directed, written, and co-produced by James Cameron. It stars Kate Winslet and Leonardo DiCaprio. The movie was released on December 19, 1997. It received positive critical reviews. The movie won 11 Academy Awards, and was nominated for fourteen total Academy Awards.....`

Claims and citations:
  * 0\. `Here is what I found.`  
Grounding check required: `false`
  * 1\. `Titanic was directed by James Cameron.`  
Citations: `[0]`  
Grounding check required: `true`

  
`Titanic was directed by James Cameron. It was released in 1997.` |  Support score: `0.99`  
  
Cited chunks: 

  0. `[From FACT 0]....Titanic is a 1997 American epic romantic disaster movie. It was directed, written, and co-produced by James Cameron. It stars Kate Winslet and Leonardo DiCaprio. The movie was released on December 19, 1997. It received positive critical reviews. The movie won 11 Academy Awards, and was nominated for fourteen total Academy Awards.....`
  1. `[From FACT 1]...Titanic is an epic, action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic; the pride and joy of the White Star Line and, at the time, the largest moving object ever built. She was the most luxurious liner of her era which ultimately carried over 1,500 people to their death in the ice cold waters of the North Atlantic in the early hours of April 15, 1912....`

Claims and citations:
  * 0\. `Titanic was directed by James Cameron.`  
Citations: `[0]`  
Grounding check required: `true`
  * 1\. `It was released in 1997.`  
Citations: `[1]`  
Grounding check required: `true`

  
`Titanic was directed by James Cameron. It was based on the sinking of the RMS Titanic that led to the death of 1500 people.` |  Support score: `0.95`  
  
Cited chunks: 

  0. `[From FACT 0]....Titanic is a 1997 American epic romantic disaster movie. It was directed, written, and co-produced by James Cameron. It stars Kate Winslet and Leonardo DiCaprio. The movie was released on December 19, 1997. It received positive critical reviews. The movie won 11 Academy Awards, and was nominated for fourteen total Academy Awards.....`
  1. `[From FACT 1]...Titanic is an epic, action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic; the pride and joy of the White Star Line and, at the time, the largest moving object ever built. She was the most luxurious liner of her era which ultimately carried over 1,500 people to their death in the ice cold waters of the North Atlantic in the early hours of April 15, 1912....`

Claims and citations:
  * 0\. `Cited chunks: Titanic was directed by James Cameron.`   
Citations: `[0]`  
Grounding check required: `true`
  * 1\. `Cited chunks: It was based on the sinking of the RMS Titanic that led to the death of 1500 people.`  
Citations: `[1]`  
Grounding check required: `true`

  
`Titanic was directed by James Cameron. It starred Brad Pitt and Kate Winslet` |  Support score: `0.54`  
  
Cited chunks: 

  0. `[From FACT 0]....Titanic is a 1997 American epic romantic disaster movie. It was directed, written, and co-produced by James Cameron. It stars Kate Winslet and Leonardo DiCaprio. The movie was released on December 19, 1997. It received positive critical reviews. The movie won 11 Academy Awards, and was nominated for fourteen total Academy Awards.....`
  1. `[From FACT 1]...Titanic is an epic, action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic; the pride and joy of the White Star Line and, at the time, the largest moving object ever built. She was the most luxurious liner of her era which ultimately carried over 1,500 people to their death in the ice cold waters of the North Atlantic in the early hours of April 15, 1912....`

Claims and citations:
  * 0\. `Titanic was directed by James Cameron.`  
Citations: `[0]`  
Grounding check required: `true`
  * 1\. `It starred Brad Pitt and Kate Winslet`  
Citations: `[]`  
Grounding check required: `true`

**Note:** Even though Kate Winslet starred in the movie, because the claim `"It starred Brad Pitt and Kate Winslet"` is not wholly true, it gets no citations.  
  
  
**Note:** The raw input and output from the API calls don't look exactly like this. For example, in addition to the claim text the method also returns the start and end positions of where the claim text appears in the answer candidate. For more information, see Obtain a support score for an answer candidate.

## Obtain claim-level scores for an answer candidate

In addition to the answer-level support score, you can obtain a claim-level support score for each claim in an answer candidate.

To obtain the claim-level scores, follow these steps:

  1. Prepare your set of facts. For more information and examples, see Terms defined and explained.

  2. Call the [`check`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.groundingConfigs/check) method, using the following curl command:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/groundingConfigs/default_grounding_config:check" \
         -d '{
         "answerCandidate": "CANDIDATE",
         "facts": [
          {
           "factText": "TEXT_0",
           "attributes": {"ATTRIBUTE_A": "VALUE_A0","ATTRIBUTE_B": "VALUE_B0"}
          },
          {
           "factText": "TEXT_1",
           "attributes": {"ATTRIBUTE_A": "VALUE_A1","ATTRIBUTE_B": "VALUE_B1"}
          },
          {
           "factText": "TEXT_2",
           "attributes": {"ATTRIBUTE_A": "VALUE_A2","ATTRIBUTE_B": "VALUE_B2"}
          },
         ],
         "groundingSpec": {
           "citationThreshold": "CITATION_THRESHOLD",
           "enableClaimLevelScore": "ENABLE_CLAIM_LEVEL_SCORE",
         }
         }'
         

Replace the following:

     * `PROJECT_ID`: the project number or ID of your Google Cloud project.

     * `CANDIDATE`: the answer candidate string for which you want to get a support score—for example, `Titanic was directed by James Cameron. It was released in 1997.` An answer candidate can have a maximum length of 4096 tokens, where a token is defined as a word in a sentence or a period (a punctuation mark used to end the sentence). For example, the sentence "They wore off-the-rack clothes in 2024." is seven tokens long, including six words and a period.

     * `TEXT`: the text segment to be used for grounding—for example, `Titanic is a 1997 American epic... Academy Awards.` (See the full text in Examples of facts.)

     * `ATTRIBUTE`: the name of a metadata attribute associated with the fact—for example, `author` or `title`. It is a user-defined label to add more information to the fact text. For example, if the fact text `Toronto is the capital of Ontario` has an `author` attribute with its value as `Wikipedia`, then the following claims are well-grounded:

       * `Wikipedia cites that Toronto is the capital of Ontario`
       * `Toronto is the capital of Ontario`

However, the claim that `Government of Ontario claims that Toronto is the capital of Ontario` is not as well-grounded.

     * `VALUE`: the value for the attribute—for example, `Simple Wikipedia` or `Titanic (1997 film)`.

     * `CITATION_THRESHOLD`: a float value from 0 through 1 that determines whether a fact must be cited for a claim in the answer candidate. A higher threshold leads to fewer but stronger citations to support the claim, and a lower threshold leads to more but weaker citations. If unset, the default threshold value is 0.6.

     * `ENABLE_CLAIM_LEVEL_SCORE`: a boolean value. Set this field to `true` to enable the claim-level score feature. To turn off this feature, remove this field or set this field to `false`.




### Example request

Using the example facts from the previous section, you can send the following request. Replace the `CANDIDATE` field with different strings whose per-claim grounding you want to check.
    
    
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/groundingConfigs/default_grounding_config:check" \
        -d '{
        "answerCandidate": "CANDIDATE",
        "facts": [
         {
          "factText": "Titanic is a 1997 American epic romantic disaster movie. It was directed, written, and co-produced by James Cameron. The movie is about the 1912 sinking of the RMS Titanic. It stars Kate Winslet and Leonardo DiCaprio. The movie was released on December 19, 1997. It received positive critical reviews. The movie won 11 Academy Awards, and was nominated for fourteen total Academy Awards.",
          "attributes": {"author":"Simple Wikipedia"}
         },
         {
          "factText": "James Cameron&#39;s \"Titanic\" is an epic, action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic; the pride and joy of the White Star Line and, at the time, the largest moving object ever built. She was the most luxurious liner of her era -- the \"ship of dreams\" -- which ultimately carried over 1,500 people to their death in the ice cold waters of the North Atlantic in the early hours of April 15, 1912.",
          "attributes": {"author":"Simple Wikipedia"}
         }
        ],
        "groundingSpec": {
          "citationThreshold": "0.6",
          "enableClaimLevelScore": true,
        }
        }'
    

**Note:** The double quotes are escaped with the backslash character, and the apostrophe is replaced by its HTML character entity.

### Example of responses with claim-level scores

The following table shows an example answer candidate and its response when you send the example request, based on the example facts.

Answer candidate | Check grounding response  
---|---  
`Here is what I found. Titanic was directed by James Cameron. It starred Kate Winslet and Leonardo DiCaprio.` |  Support score: `0.99`  
  
Cited chunks: 

  0. `[From FACT 0]....Titanic is a 1997 American epic romantic disaster movie. It was directed, written, and co-produced by James Cameron. It stars Kate Winslet and Leonardo DiCaprio. The movie was released on December 19, 1997. It received positive critical reviews. The movie won 11 Academy Awards, and was nominated for fourteen total Academy Awards.....`

Claims and citations:
  * 0\. `Here is what I found.`  
Grounding check required: `false`
  * 1\. `Titanic was directed by James Cameron.`  
Citations: `[0]`  
Grounding check required: `true`  
Score: `0.99`
  * 2\. `It starred Kate Winslet and Leonardo DiCaprio.`  
Citations: `[0]`  
Grounding check required: `true`  
Score: `0.99`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
