---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/search-api/
title: Google Knowledge Graph Search API \u00a0|\u00a0 Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:24:01.113149+00:00
---

# Google Knowledge Graph Search API  |  Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/search-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Guides ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview)



Send feedback 

#  Google Knowledge Graph Search API Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this product as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** The Google Knowledge Graph Search API returns only individual matching entities, rather than graphs of interconnected entities. If you need the latter, we recommend using data dumps from [Wikidata](https://www.wikidata.org) instead.**Note:** The Google Knowledge Graph Search API might return data with license restrictions, which attach to either `license` or `additionalProperty` fields. For more information, see [Additional Product Requirements](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/ckg-policies) on how you can leverage the data for your use case.

This quickstart introduces you to the Google Knowledge Graph Search API. In this quickstart, use the API to search or look up entities in Google Knowledge Graph.

If you're planning a new project, build your application with Cloud Knowledge Graph [Advanced edition](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/editions#-_advanced) to take advantage of new features and service improvements. The [Basic edition](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/editions#-_basic) remains available, but doesn't support new features, high QPS, or additional security and compliance standards. 

## Search Cloud Knowledge Graph entities

The following samples show how to search an entity against the knowledge graph.

### Advanced

### REST

To search the knowledge graph for the Advanced edition, call the [`projects.locations.cloudKnowledgeGraphEntities.search`](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.cloudKnowledgeGraphEntities/search) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: Knowledge Graph location. 
    * Options: `global` \- Global Endpoint
  * SEARCH_QUERY: The literal query string for search.
  * LANGUAGES: (Optional) The list of [language codes](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/languages) (defined in ISO 693) to run the query with. The default value is `en` if not specified.
  * TYPES: (Optional) Restricts returned entities with these types, as defined by `https://schema.org`. If multiple types are specified, returned entities will contain one or more of these types. The default value is empty, which will return entities with no type restrictions. Refer to the [Schema.org full hierarchy](https://schema.org/docs/full.html) for supported types. **Tip:** If you know what you are looking for, use the **types** filter to narrow down your search.
  * LIMIT: (Optional) Limits the number of entities to be returned. The default is `20`.



HTTP method and URL: 
    
    
    GET https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cloudKnowledgeGraphEntities:Search?query=SEARCH_QUERY&limit=LIMIT

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cloudKnowledgeGraphEntities:Search?query=SEARCH_QUERY&limit=LIMIT"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cloudKnowledgeGraphEntities:Search?query=SEARCH_QUERY&limit=LIMIT" | Select-Object -Expand Content

The response contains a list of entities, presented in [JSON-LD](https://json-ld.org) format and compatible with [schema.org](https://schema.org) schemas with limited external extensions.

Refer to Entity Response Structure for more information about the response structure.

The following JSON-LD example shows how the response body is structured:
    
    
    {
      "@context": {
        "@vocab": "http://schema.org/"
      },
      "@type": "ItemList",
      "itemListElement": [
        {
          "result": {
            "@id": "c-07xuup16g",
            "name": "Stanford University",
            "description": "Private university in Stanford, California",
            "detailedDescription": {
              "articleBody": "Stanford University, officially Leland Stanford Junior University, is a private research university in Stanford, California. The campus occupies 8,180 acres, among the largest in the United States, and enrolls over 17,000 students. ",
              "url": "https://en.wikipedia.org/wiki/Stanford_University",
              "license": "https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License"
            },
            "url": "http://www.stanford.edu/",
            "image": {
              "contentUrl": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTfPPf-ker0y_892m1wu8-U89furQgQ67foDFncY3r9sREpeWxV",
              "url": "https://es.wikipedia.org/wiki/Archivo:Logo_of_Stanford_University.png"
            },
            "identifier": [
              {
                "@type": "PropertyValue",
                "propertyID": "googleKgMID",
                "value": "/m/06pwq"
              },
              {
                "@type": "PropertyValue",
                "propertyID": "googlePlaceID",
                "value": "ChIJneqLZyq7j4ARf2j8RBrwzSk"
              },
              {
                "@type": "PropertyValue",
                "propertyID": "wikidataQID",
                "value": "Q41506"
              }
            ],
            "@type": [
              "Place",
              "Organization",
              "MovieTheater",
              "Corporation",
              "EducationalOrganization",
              "Thing",
              "CollegeOrUniversity"
            ]
          }
        }
      ]
    }
    

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
    
    

### Basic

### REST

To search the knowledge graph for the Basic edition, call the [`projects.locations.publicKnowledgeGraphEntities.search`](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.publicKnowledgeGraphEntities/search) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: Knowledge Graph location. 
    * Options: `global` \- Global Endpoint
  * SEARCH_QUERY: The literal query string for search.
  * LANGUAGES: (Optional) The list of [language codes](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/languages) (defined in ISO 693) to run the query with. The default value is `en` if not specified.
  * TYPES: (Optional) Restricts returned entities with these types, as defined by `https://schema.org`. If multiple types are specified, returned entities will contain one or more of these types. The default value is empty, which will return entities with no type restrictions. Refer to the [Schema.org full hierarchy](https://schema.org/docs/full.html) for supported types. **Tip:** If you know what you are looking for, use the **types** filter to narrow down your search.
  * LIMIT: (Optional) Limits the number of entities to be returned. The default is `20`.



HTTP method and URL: 
    
    
    GET https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publicKnowledgeGraphEntities:Search?query=SEARCH_QUERY&limit=LIMIT

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publicKnowledgeGraphEntities:Search?query=SEARCH_QUERY&limit=LIMIT"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publicKnowledgeGraphEntities:Search?query=SEARCH_QUERY&limit=LIMIT" | Select-Object -Expand Content

The response contains a list of entities, presented in [JSON-LD](https://json-ld.org) format and compatible with [schema.org](https://schema.org) schemas with limited external extensions.

Refer to Entity Response Structure for more information about the response structure.

The following JSON-LD example shows how the response body is structured:
    
    
    {
      "@context": {
        "@vocab": "http://schema.org/"
      },
      "@type": "ItemList",
      "itemListElement": [
        {
          "result": {
            "@id": "c-07xuup16g",
            "name": "Stanford University",
            "description": "Private university in Stanford, California",
            "detailedDescription": {
              "license": "https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License",
              "url": "https://en.wikipedia.org/wiki/Stanford_University",
              "articleBody": "Stanford University, officially Leland Stanford Junior University, is a private research university in Stanford, California. The campus occupies 8,180 acres, among the largest in the United States, and enrolls over 17,000 students. "
            },
            "url": "http://www.stanford.edu/",
            "identifier": [
              {
                "@type": "PropertyValue",
                "propertyID": "googleKgMID",
                "value": "/m/06pwq"
              }
            ],
            "image": {
              "contentUrl": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTfPPf-ker0y_892m1wu8-U89furQgQ67foDFncY3r9sREpeWxV",
              "url": "https://es.wikipedia.org/wiki/Archivo:Logo_of_Stanford_University.png"
            },
            "@type": [
              "EducationalOrganization",
              "CollegeOrUniversity",
              "Thing",
              "Place",
              "Corporation",
              "MovieTheater",
              "Organization"
            ]
          }
        }
      ]
    }
    

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
    
    
    def search_public_kg_sample(
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
        request = ekg.SearchPublicKgRequest(
            parent=parent,
            query=search_query,
            languages=languages,
            types=types,
            limit=limit,
        )
    
        # Make the request
        response = client.search_public_kg(request=request)
    
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
    
    

## Look up entities from Cloud Knowledge Graph MID

Google Knowledge Graph Search API introduces the new [machine ID (MID)](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/mid) format for easier product and application integration. The `lookup` API works for both the new Cloud Knowledge Graph MID (starts with `c-`), as well as the Google Knowledge Graph MID (starts with `/m`).

### Advanced

### REST

To look up an entity by [MID](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/mid) for the Advanced edition, call the [`projects.locations.cloudKnowledgeGraphEntities.lookup`](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.cloudKnowledgeGraphEntities/lookup) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: Knowledge Graph location. 
    * Options: `global` \- Global Endpoint
  * LOOKUP_IDS: The list of entity IDs to be used for lookup. 
    * Example: `/m/0dl567`
  * LANGUAGES: (Optional) The list of [language codes](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/languages) (defined in ISO 693) to run the query with. The default value is `en` if not specified.



HTTP method and URL: 
    
    
    GET https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cloudKnowledgeGraphEntities:Lookup?ids=LOOKUP_IDS

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cloudKnowledgeGraphEntities:Lookup?ids=LOOKUP_IDS"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cloudKnowledgeGraphEntities:Lookup?ids=LOOKUP_IDS" | Select-Object -Expand Content

The response contains a list of entities, presented in [JSON-LD](https://json-ld.org) format and compatible with [schema.org](https://schema.org) schemas with limited external extensions.

Refer to Entity Response Structure for more information about the response structure.

The following JSON-LD example shows how the response body is structured:
    
    
    {
      "@context": {
        "@vocab": "http://schema.org/"
      },
      "@type": "ItemList",
      "itemListElement": [
        {
          "result": {
            "description": "American singer-songwriter",
            "@type": [
              "Person",
              "Thing"
            ],
            "name": "Taylor Swift",
            "@id": "c-0260160kc",
            "url": "http://www.taylorswift.com/",
            "identifier": [
              {
                "@type": "PropertyValue",
                "propertyID": "googleKgMID",
                "value": "/m/0dl567"
              },
              {
                "@type": "PropertyValue",
                "propertyID": "wikidataQID",
                "value": "Q26876"
              }
            ],
            "detailedDescription": {
              "articleBody": "Taylor Alison Swift is an American singer-songwriter. Her discography spans multiple genres and her narrative songwriting—often inspired by her personal life—has received critical praise and widespread media coverage. ",
              "license": "https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License",
              "url": "https://en.wikipedia.org/wiki/Taylor_Swift"
            },
            "image": {
              "contentUrl": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSnsjOArwgD-bhyRslj_Qa7Z2tIPLRFU3VnEuLr1ybcyned49Pt",
              "url": "https://pt.wikipedia.org/wiki/Ficheiro:191125_Taylor_Swift_at_the_2019_American_Music_Awards_(cropped).png"
            }
          }
        }
      ]
    }
    

To look up multiple entities from Cloud Knowledge Graph, provide multiple ids. The URL should look like this. 
    
    
    https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cloudKnowledgeGraphEntities:Lookup?ids=LOOKUP_IDS&ids=LOOKUP_IDS
    

### Python

For more information, see the [Enterprise Knowledge Graph Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/enterpriseknowledgegraph/latest). 

To authenticate to Enterprise Knowledge Graph, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections.abc import Sequence
    
    from google.cloud import enterpriseknowledgegraph as ekg
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_GRAPH_LOCATION'      # Values: 'global'
    # ids = ['YOUR_LOOKUP_MID']             # https://cloud.google.com/enterprise-knowledge-graph/docs/mid
    # languages = ['en']                    # Optional: List of ISO 639-1 Codes
    
    
    def lookup_sample(
        project_id: str,
        location: str,
        ids: Sequence[str],
        languages: Sequence[str] = None,
    ):
        # Create a client
        client = ekg.EnterpriseKnowledgeGraphServiceClient()
    
        # The full resource name of the location
        # e.g. projects/{project_id}/locations/{location}
        parent = client.common_location_path(project=project_id, location=location)
    
        # Initialize request argument(s)
        request = ekg.LookupRequest(
            parent=parent,
            ids=ids,
            languages=languages,
        )
    
        # Make the request
        response = client.lookup(request=request)
    
        print(f"Lookup IDs: {ids}\n")
    
        print(response)
    
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
    
    

### Basic

### REST

To look up an entity by [MID](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/mid) for the Basic edition, call the [`projects.locations.publicKnowledgeGraphEntities.lookup`](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.publicKnowledgeGraphEntities/lookup) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: Knowledge Graph location. 
    * Options: `global` \- Global Endpoint
  * LOOKUP_IDS: The list of entity IDs to be used for lookup. 
    * Example: `/m/0dl567`
  * LANGUAGES: (Optional) The list of [language codes](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/languages) (defined in ISO 693) to run the query with. The default value is `en` if not specified.



HTTP method and URL: 
    
    
    GET https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publicKnowledgeGraphEntities:Lookup?ids=LOOKUP_IDS

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publicKnowledgeGraphEntities:Lookup?ids=LOOKUP_IDS"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publicKnowledgeGraphEntities:Lookup?ids=LOOKUP_IDS" | Select-Object -Expand Content

The response contains a list of entities, presented in [JSON-LD](https://json-ld.org) format and compatible with [schema.org](https://schema.org) schemas with limited external extensions.

Refer to Entity Response Structure for more information about the response structure.

The following JSON-LD example shows how the response body is structured:
    
    
    {
      "@context": {
        "@vocab": "http://schema.org/"
      },
      "@type": "ItemList",
      "itemListElement": [
        {
          "result": {
            "description": "American singer-songwriter",
            "@type": [
              "Person",
              "Thing"
            ],
            "name": "Taylor Swift",
            "@id": "c-0260160kc",
            "url": "http://www.taylorswift.com/",
            "identifier": [
              {
                "@type": "PropertyValue",
                "propertyID": "googleKgMID",
                "value": "/m/0dl567"
              }
            ],
            "detailedDescription": {
              "articleBody": "Taylor Alison Swift is an American singer-songwriter. Her discography spans multiple genres and her narrative songwriting—often inspired by her personal life—has received critical praise and widespread media coverage. ",
              "license": "https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License",
              "url": "https://en.wikipedia.org/wiki/Taylor_Swift"
            },
            "image": {
              "contentUrl": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSnsjOArwgD-bhyRslj_Qa7Z2tIPLRFU3VnEuLr1ybcyned49Pt",
              "url": "https://pt.wikipedia.org/wiki/Ficheiro:191125_Taylor_Swift_at_the_2019_American_Music_Awards_(cropped).png"
            }
          }
        }
      ]
    }
    

To look up multiple entities from Cloud Knowledge Graph, provide multiple ids. The URL should look like this. 
    
    
    https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publicKnowledgeGraphEntities:Lookup?ids=LOOKUP_IDS&ids=LOOKUP_IDS
    

### Python

For more information, see the [Enterprise Knowledge Graph Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/enterpriseknowledgegraph/latest). 

To authenticate to Enterprise Knowledge Graph, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections.abc import Sequence
    
    from google.cloud import enterpriseknowledgegraph as ekg
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_GRAPH_LOCATION'      # Values: 'global'
    # ids = ['YOUR_LOOKUP_MID']             # https://cloud.google.com/enterprise-knowledge-graph/docs/mid
    # languages = ['en']                    # Optional: List of ISO 639-1 Codes
    
    
    def lookup_public_kg_sample(
        project_id: str,
        location: str,
        ids: Sequence[str],
        languages: Sequence[str] = None,
    ):
        # Create a client
        client = ekg.EnterpriseKnowledgeGraphServiceClient()
    
        # The full resource name of the location
        # e.g. projects/{project_id}/locations/{location}
        parent = client.common_location_path(project=project_id, location=location)
    
        # Initialize request argument(s)
        request = ekg.LookupPublicKgRequest(
            parent=parent,
            ids=ids,
            languages=languages,
        )
    
        # Make the request
        response = client.lookup_public_kg(request=request)
    
        print(f"Lookup IDs: {ids}\n")
    
        print(response)
    
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
    
    

## Entity Structure

**Note:** Image URLs are provided to help you confirm that you have selected the correct entity. As with all content you obtain through Google APIs, you are responsible for ensuring that your use of the images complies with applicable law.Field name | Type | Description  
---|---|---  
`@id` | `string` | The canonical URI for the entity.  
`name` | `string` | The name of the entity.  
`@type` | `array` | The list of supported [schema.org](https://schema.org) types that match the entity.  
`description` | `string` | A short description of the entity.  
`image` | `URL` | An image to help identify the entity.  
`detailedDescription` | `string` | A detailed description of the entity.  
`url` | `URL` | The official website URL of the entity, if available.  
`identifier` | `array` | A list of other linked ids. e.g. WikidataQID.  
  
### JSON-LD keywords

Refer to the [JSON-LD specification](https://www.w3.org/TR/json-ld/) for JSON-LD keywords such as:

  * [`@context`](https://www.w3.org/TR/json-ld/#the-context)
  * [`@vocab`](https://www.w3.org/TR/json-ld/#default-vocabulary)
  * [`@type`](https://www.w3.org/TR/json-ld/#specifying-the-type)
  * [`@id`](https://www.w3.org/TR/json-ld/#node-identifiers)



### Schema.org compatibility

For each of the Schema.org types (such as `Person`) and properties (such as `name`) there is a corresponding full URI, as in the following examples:

Class | Name | URI  
---|---|---  
type | `Person` | [`https://schema.org/Person`](https://schema.org/Person)  
type | `Thing` | [`https://schema.org/Thing`](https://schema.org/Thing)  
property | `name` | [`https://schema.org/name`](https://schema.org/name)  
property | `description` | [`https://schema.org/description`](https://schema.org/description)  
  
### Schema extensions

Types and properties used in this API are hosted at [`https://schema.googleapis.com`](https://schema.googleapis.com) as [external extensions](https://schema.org/docs/extension.html).

The documentation for each type and property is available at the corresponding URI.

Class | Name | URI  
---|---|---  
type | `EntitySearchResult` | [`https://schema.googleapis.com/EntitySearchResult`](https://schema.googleapis.com/EntitySearchResult)  
property | `detailedDescription` | [`https://schema.googleapis.com/detailedDescription`](https://schema.googleapis.com/detailedDescription)  
  
## Knowledge Graph entities

The Knowledge Graph has millions of entries that describe real-world entities like people, places, and things. These entities form the nodes of the graph.

The following are some of the common types of entities found in the Cloud Knowledge Graph:

  * [`Book`](http://schema.org/Book)
  * [`BookSeries`](http://schema.org/BookSeries)
  * [`EducationalOrganization`](http://schema.org/EducationalOrganization)
  * [`Event`](http://schema.org/Event)
  * [`GovernmentOrganization`](http://schema.org/GovernmentOrganization)
  * [`LocalBusiness`](http://schema.org/LocalBusiness)
  * [`Movie`](http://schema.org/Movie)
  * [`MovieSeries`](http://schema.org/MovieSeries)
  * [`MusicAlbum`](http://schema.org/MusicAlbum)
  * [`MusicGroup`](http://schema.org/MusicGroup)
  * [`MusicRecording`](http://schema.org/MusicRecording)
  * [`Organization`](http://schema.org/Organization)
  * [`Periodical`](http://schema.org/Periodical)
  * [`Person`](http://schema.org/Person)
  * [`Place`](http://schema.org/Place)
  * [`SportsTeam`](http://schema.org/SportsTeam)
  * [`TVEpisode`](http://schema.org/TVEpisode)
  * [`TVSeries`](http://schema.org/TVSeries)
  * [`VideoGame`](http://schema.org/VideoGame)
  * [`VideoGameSeries`](http://schema.org/VideoGameSeries)
  * [`WebSite`](http://schema.org/WebSite)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
