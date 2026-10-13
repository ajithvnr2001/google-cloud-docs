---
url: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1MessageBuilder/
title: Class MessageBuilder (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:19.379721+00:00
---

# Class MessageBuilder (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1MessageBuilder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class MessageBuilder (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Constructs [`Message`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1Message) objects. 

## Constructors 

### MessageBuilder()

## Functions 

### Build() &&

Creates a new message. 

**Returns**  
---  
**Type** | **Description**  
`Message` |   
  
### SetData(std::string) &

Sets the message payload to `data`. 

**Parameter**  
---  
**Name** | **Description**  
`data` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &` |   
  
### SetData(std::string) &&

Sets the message payload to `data`. 

**Parameter**  
---  
**Name** | **Description**  
`data` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &&` |   
  
### SetOrderingKey(std::string) &

Sets the ordering key to `key`. 

**Parameter**  
---  
**Name** | **Description**  
`key` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &` |   
  
### SetOrderingKey(std::string) &&

Sets the ordering key to `key`. 

**Parameter**  
---  
**Name** | **Description**  
`key` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &&` |   
  
### InsertAttribute(std::string const &, std::string const &) &

Inserts an attribute to the message, leaving the message unchanged if `key` is already present. 

**Parameters**  
---  
**Name** | **Description**  
`key` |  `std::string const &`   
  
`value` |  `std::string const &`   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &` |   
  
### InsertAttribute(std::string const &, std::string const &) &&

Inserts an attribute to the message, leaving the message unchanged if `key` is already present. 

**Parameters**  
---  
**Name** | **Description**  
`key` |  `std::string const &`   
  
`value` |  `std::string const &`   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &&` |   
  
### SetAttribute(std::string const &, std::string) &

Inserts or sets an attribute on the message. 

**Parameters**  
---  
**Name** | **Description**  
`key` |  `std::string const &`   
  
`value` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &` |   
  
### SetAttribute(std::string const &, std::string) &&

Inserts or sets an attribute on the message. 

**Parameters**  
---  
**Name** | **Description**  
`key` |  `std::string const &`   
  
`value` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &&` |   
  
### SetAttributes(Iterator, Iterator) &

Sets the attributes in the message to the attributes from the range [`begin`, `end`) 

**Parameters**  
---  
**Name** | **Description**  
`begin` |  `Iterator`   
  
`end` |  `Iterator`   
  
`typename Iterator` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &` |   
  
### SetAttributes(Iterator, Iterator) &&

Sets the attributes in the message to the attributes from the range [`begin`, `end`) 

**Parameters**  
---  
**Name** | **Description**  
`begin` |  `Iterator`   
  
`end` |  `Iterator`   
  
`typename Iterator` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &&` |   
  
### SetAttributes(std::vector< std::pair< std::string, std::string > >) &

Sets the attributes in the message to `v`. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `std::vector< std::pair< std::string, std::string > >`   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &` |   
  
### SetAttributes(std::vector< std::pair< std::string, std::string > >) &&

Sets the attributes in the message to `v`. 

**Parameter**  
---  
**Name** | **Description**  
`v` |  `std::vector< std::pair< std::string, std::string > >`   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &&` |   
  
### SetAttributes(std::vector< Pair >) &

Sets the attributes in the message to `v`. 

**Parameters**  
---  
**Name** | **Description**  
`v` |  `std::vector< Pair >`   
  
`typename Pair` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &` |   
  
### SetAttributes(std::vector< Pair >) &&

Sets the attributes in the message to `v`. 

**Parameters**  
---  
**Name** | **Description**  
`v` |  `std::vector< Pair >`   
  
`typename Pair` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`MessageBuilder &&` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
