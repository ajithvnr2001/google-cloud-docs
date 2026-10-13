---
url: https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity/
title: Entity \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:02.742549+00:00
---

# Entity  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Reference ](https://docs.cloud.google.com/natural-language/docs/apis)



Send feedback 

#  Entity Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Type
  * EntityMention
    * JSON representation
  * Type



Represents a phrase in the text that is a known entity, such as a person, an organization, or location. The API associates information, such as salience and mentions, with entities.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([Type](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity#Type)),
      "metadata": {
        string: string,
        ...
      },
      "salience": number,
      "mentions": [
        {
          object ([EntityMention](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity#EntityMention))
        }
      ],
      "sentiment": {
        object ([Sentiment](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Sentiment))
      }
    }  
  
Fields  
---  
`name` |  `string` The representative name for the entity.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity#Type)`)` The entity type.  
`metadata` |  `map (key: string, value: string)` Metadata associated with the entity.For most entity types, the metadata is a Wikipedia URL (`wikipedia_url`) and Knowledge Graph MID (`mid`), if they are available. For the metadata associated with other entity types, see the Type table below.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`salience` |  `number` The salience score associated with the entity in the [0, 1.0] range.The salience score for an entity provides information about the importance or centrality of that entity to the entire document text. Scores closer to 0 are less salient, while scores closer to 1.0 are highly salient.  
`mentions[]` |  `object (`[EntityMention](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity#EntityMention)`)` The mentions of this entity in the input document. The API currently supports proper noun mentions.  
`sentiment` |  `object (`[Sentiment](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Sentiment)`)` For calls to [AnalyzeEntitySentiment][] or if `[AnnotateTextRequest.Features.extract_entity_sentiment](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/annotateText#Features.FIELDS.extract_entity_sentiment)` is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.  
  
## Type

The type of the entity. For most entity types, the associated metadata is a Wikipedia URL (`wikipedia_url`) and Knowledge Graph MID (`mid`). The table below lists the associated fields for entities that have different metadata.

Enums  
---  
`UNKNOWN` | Unknown  
`PERSON` | Person  
`LOCATION` | Location  
`ORGANIZATION` | Organization  
`EVENT` | Event  
`WORK_OF_ART` | Artwork  
`CONSUMER_GOOD` | Consumer product  
`OTHER` | Other types of entities  
`PHONE_NUMBER` | Phone numberThe metadata lists the phone number, formatted according to local convention, plus whichever additional elements appear in the text:

  * `number` \- the actual number, broken down into sections as per local convention
  * `national_prefix` \- country code, if detected
  * `area_code` \- region or area code, if detected
  * `extension` \- phone extension (to be dialed after connection), if detected

  
`ADDRESS` | AddressThe metadata identifies the street number and locality plus whichever additional elements appear in the text:

  * `street_number` \- street number
  * `locality` \- city or town
  * `street_name` \- street/route name, if detected
  * `postal_code` \- postal code, if detected
  * `country` \- country, if detected<
  * `broad_region` \- administrative area, such as the state, if detected
  * `narrow_region` \- smaller administrative area, such as county, if detected
  * `sublocality` \- used in Asian addresses to demark a district within a city, if detected

  
`DATE` | DateThe metadata identifies the components of the date:

  * `year` \- four digit year, if detected
  * `month` \- two digit month number, if detected
  * `day` \- two digit day number, if detected

  
`NUMBER` | NumberThe metadata is the number itself.  
`PRICE` | PriceThe metadata identifies the `value` and `currency`.  
  
## EntityMention

Represents a mention for an entity in the text. Currently, proper noun mentions are supported.

JSON representation  
---  
      
    
    {
      "text": {
        object ([TextSpan](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/TextSpan))
      },
      "type": enum ([Type](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity#Type_1)),
      "sentiment": {
        object ([Sentiment](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Sentiment))
      }
    }  
  
Fields  
---  
`text` |  `object (`[TextSpan](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/TextSpan)`)` The mention text.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity#Type_1)`)` The type of the entity mention.  
`sentiment` |  `object (`[Sentiment](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Sentiment)`)` For calls to [AnalyzeEntitySentiment][] or if `[AnnotateTextRequest.Features.extract_entity_sentiment](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/annotateText#Features.FIELDS.extract_entity_sentiment)` is set to true, this field will contain the sentiment expressed for this mention of the entity in the provided document.  
  
## Type

The supported types of mentions.

Enums  
---  
`TYPE_UNKNOWN` | Unknown  
`PROPER` | Proper name  
`COMMON` | Common noun (or noun compound)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
