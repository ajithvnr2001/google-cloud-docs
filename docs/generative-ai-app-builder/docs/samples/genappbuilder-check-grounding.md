---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-check-grounding/
title: Check grounding \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:24.854929+00:00
---

# Check grounding  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-check-grounding/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  Check grounding Stay organized with collections  Save and categorize content based on your preferences. 

Check grounding

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Check grounding with RAG](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-grounding)



## Code sample

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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
