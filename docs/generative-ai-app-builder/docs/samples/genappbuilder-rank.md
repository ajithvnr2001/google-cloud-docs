---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-rank/
title: Rank documents \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:53.897090+00:00
---

# Rank documents  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-rank/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  Rank documents Stay organized with collections  Save and categorize content based on your preferences. 

Rank documents

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Improve search and RAG quality with ranking API](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking)



## Code sample

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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
