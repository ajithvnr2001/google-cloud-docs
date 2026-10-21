---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/source-message-class/
title: Create message classes \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:36.993233+00:00
---

# Create message classes  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/source-message-class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create message classes

Manufacturing Data Engine (MDE) lets you transform a series of source messages into records of a specific type by means of [parsing](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/parser).

Source message classes are configuration entities that represent the _source_ of the parsing operation, and describe a set of structurally and semantically similar source messages.

![source-to-target](https://docs.cloud.google.com/static/manufacturing-data-engine/images/source-to-target.png)

Source message classes provide a predictable message schema to parsers so that transformations, mappings, and data extraction can be performed on known fields.

## Source message classification

Each message class has an associated _message class expression_ and a priority. The priority of a message class is an integer from 0 to 65535 , inclusive. Lower integers indicate higher priorities.

A source message is associated to a source message class when the first source message class expression evaluates to `true` after the classes are sorted on priority.

Source message class expressions are written in [Spring Expression Language (SpEL)](https://docs.spring.io/spring-framework/docs/5.3.0/reference/html/core.html#expressions-language-ref).

![source-message-class](https://docs.cloud.google.com/static/manufacturing-data-engine/images/smc-illustration.png)

SpEL expressions can access [source message attributes (Pub/Sub attributes)](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) and data. The message attributes are exposed under the `#root.headers` key, and data is exposed under the `#root.event` key.

The following are examples of SpEL expressions for a source message class:
    
    
    #root.event['MessageType'] != null && #root.event['MessageType'] matches 'Sensor.*'
    
    
    
    #root.headers['source'] != null && #root.headers['source'] == 'MCe'
    

### Naming restrictions for message classes

A message class name can contain the following:

  * Letters (uppercase and lowercase), numbers, and the special characters `-` and `_`.
  * Can be up to 255 characters long.



You can use the following regular expression for validation: `^[a-z][a-z0-9\\-_]{1,255}$`

If you try to create an entity violating the naming restrictions you will get a `400 error`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
