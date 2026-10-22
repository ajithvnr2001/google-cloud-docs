---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/samples/enterpriseknowledgegraph-search/
title: Search for an entity (Advanced) \u00a0|\u00a0 Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:29.219217+00:00
---

# Search for an entity (Advanced)  |  Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/samples/enterpriseknowledgegraph-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Samples ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/samples)



#  Search for an entity (Advanced) Stay organized with collections  Save and categorize content based on your preferences. 

Search for an entity in the Knowledge Graph using Advanced Edition.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Google Knowledge Graph Search API](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/search-api)



## Code sample

### Python

For more information, see the [Enterprise Knowledge Graph Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/enterpriseknowledgegraph/latest). 

To authenticate to Enterprise Knowledge Graph, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections.abc import Sequence
    
    from google.cloud import enterpriseknowledgegraph as ekg
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_GRAPH_LOCATION'      # Values: 'global'
    # search_query = 'YOUR_SEARCH_QUERY'
    # languages = ['en']                    # Optional: List of ISO 639-1 Codes
    # types = ['']                          # Optional: List of schema.org types to return
    # limit = 20                            # Optional: Number of entities to return
    
    
    def search_sample(
        project_id: str,
        location: str,
        search_query: str,
        languages: Sequence[str] = None,
        types: Sequence[str] = None,
        limit: int = 20,
    ):
        # Create a client
        client = ekg.EnterpriseKnowledgeGraphServiceClient()
    
        # The full resource name of the location
        # e.g. projects/{project_id}/locations/{location}
        parent = client.common_location_path(project=project_id, location=location)
    
        # Initialize request argument(s)
        request = ekg.SearchRequest(
            parent=parent,
            query=search_query,
            languages=languages,
            types=types,
            limit=limit,
        )
    
        # Make the request
        response = client.search(request=request)
    
        print(f"Search Query: {search_query}\n")
    
        # Extract and print date from response
        for item in response.item_list_element:
            result = item.get("result")
    
            print(f"Name: {result.get('name')}")
            print(f"- Description: {result.get('description')}")
            print(f"- Types: {result.get('@type')}\n")
    
            detailed_description = result.get("detailedDescription")
    
            if detailed_description:
                print("- Detailed Description:")
                print(f"\t- Article Body: {detailed_description.get('articleBody')}")
                print(f"\t- URL: {detailed_description.get('url')}")
                print(f"\t- License: {detailed_description.get('license')}\n")
    
            print(f"- Cloud MID: {result.get('@id')}")
            for identifier in result.get("identifier"):
                print(f"\t- {identifier.get('name')}: {identifier.get('value')}")
    
            print("\n")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=enterpriseknowledgegraph). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
