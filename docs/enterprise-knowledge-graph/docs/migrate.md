---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/migrate/
title: Migrate from legacy Google Knowledge Graph Search API \u00a0|\u00a0 Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:31.936279+00:00
---

# Migrate from legacy Google Knowledge Graph Search API  |  Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Guides ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview)



Send feedback 

#  Migrate from legacy Google Knowledge Graph Search API Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this product as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** The Google Knowledge Graph Search API returns only individual matching entities, rather than graphs of interconnected entities. If you need the interconnected entities, use data dumps from [Wikidata](https://www.wikidata.org) instead.

## Updates to the request

  1. New Google Knowledge Graph Search API introduces two editions, `Basic` and `Advanced`. For more information, see [Basic and Advanced editions](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/editions).

  2. To support security and compliance requirements, move to a new prediction endpoint. If planning to use the `Basic` edition, use a new access token or a service account for this API and replace your endpoint URL as shown here:




### Legacy
    
    
    https://kgsearch.googleapis.com/v1/entities
    

### Updated
    
    
    https://enterpriseknowledgegraph.googleapis.com/v1/projects/PROJECT_ID/locations/global/publicKnowledgeGraphEntities
    

## Updates to the response

  1. Cloud Knowledge Graph MID becomes the primary MID (`identifier`) for the entity. You can still find the Google Knowledge Graph MID in the `identifier` section for backward compatibility. For more information, see [Understand Machine ID (MID)](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/mid).
         
         "identifier": [
           {
             "@type": "PropertyValue",
             "propertyID": "googleKgMID",
             "value": "/m/06pwq"
           }
         ]
         

  2. The `additionalProperty` has been added to describe the license requirement for the `name` field.
         
         "additionalProperty": {
           "@type": "PropertyValue",
           "name": "nameLicense",
           "value": "https://cloud.google.com/maps-platform/terms"
         }
         

  3. The `resultScore` field has been removed from the response.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
