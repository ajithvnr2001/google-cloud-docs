---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-grounded-generation-inline-vais/
title: Grounded Generation with Inline and Vertex AI Search data \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:13.529534+00:00
---

# Grounded Generation with Inline and Vertex AI Search data  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-grounded-generation-inline-vais/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  Grounded Generation with Inline and Vertex AI Search data Stay organized with collections  Save and categorize content based on your preferences. 

Grounded Generation with Inline and Vertex AI Search data

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Generate grounded answers with RAG](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen)



## Code sample

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
