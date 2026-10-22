---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-answer-query/
title: Answer Query \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:44.532065+00:00
---

# Answer Query  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-answer-query/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  Answer Query Stay organized with collections  Save and categorize content based on your preferences. 

Answer Query

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get answers and follow-ups](https://docs.cloud.google.com/gemini/enterprise/docs/answer)
  * [Get answers and follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer)



## Code sample

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
    # engine_id = "YOUR_APP_ID"
    
    
    def answer_query_sample(
        project_id: str,
        location: str,
        engine_id: str,
    ) -> discoveryengine.AnswerQueryResponse:
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
    
        # The full resource name of the Search serving config
        serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"
    
        # Optional: Options for query phase
        # The `query_understanding_spec` below includes all available query phase options.
        # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
        query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
            query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
                disable=False,  # Optional: Disable query rephraser
                max_rephrase_steps=1,  # Optional: Number of rephrase steps
            ),
            # Optional: Classify query types
            query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
                types=[
                    discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                    discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
                ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
            ),
        )
    
        # Optional: Options for answer phase
        # The `answer_generation_spec` below includes all available query phase options.
        # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
        answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
            ignore_adversarial_query=False,  # Optional: Ignore adversarial query
            ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
            ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
            model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            # Use the 2026 stable production model for answer generation
            model_version="gemini-2.5-flash/answer_gen/stable",
            ),
            prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
                preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
            ),
            include_citations=True,  # Optional: Include citations in the response
            answer_language_code="en",  # Optional: Language code of the answer
        )
    
        # Initialize request argument(s)
        request = discoveryengine.AnswerQueryRequest(
            serving_config=serving_config,
            query=discoveryengine.Query(text="What is Vertex AI Search?"),
            session=None,  # Optional: include previous session ID to continue a conversation
            query_understanding_spec=query_understanding_spec,
            answer_generation_spec=answer_generation_spec,
            user_pseudo_id="user-pseudo-id",  # Optional: Add user pseudo-identifier for queries.
        )
    
        # Make the request
        response = client.answer_query(request)
    
        # Handle the response
        print(response)
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
