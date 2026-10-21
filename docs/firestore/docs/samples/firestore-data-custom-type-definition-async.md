---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-custom-type-definition-async/
title: Use a custom type on the client for Firestore documents (async) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:06.895922+00:00
---

# Use a custom type on the client for Firestore documents (async)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-custom-type-definition-async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Use a custom type on the client for Firestore documents (async) Stay organized with collections  Save and categorize content based on your preferences. 

Use a custom type on the client for Firestore documents (async).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Add and update data](https://docs.cloud.google.com/firestore/native/docs/manage-data/add-data)
  * [Query and filter data](https://docs.cloud.google.com/firestore/native/docs/query-data/queries)



## Code sample

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    class City:
        def __init__(self, name, state, country, capital=False, population=0, regions=[]):
            self.name = name
            self.state = state
            self.country = country
            self.capital = capital
            self.population = population
            self.regions = regions
    
        @staticmethod
        def from_dict(source):
            # ...
    
        def to_dict(self):
            # ...
    
        def __repr__(self):
            return f"City(\
                    name={self.name}, \
                    country={self.country}, \
                    population={self.population}, \
                    capital={self.capital}, \
                    regions={self.regions}\
                )"
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
