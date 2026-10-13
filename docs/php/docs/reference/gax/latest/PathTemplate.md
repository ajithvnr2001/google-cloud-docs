---
url: https://docs.cloud.google.com/php/docs/reference/gax/latest/PathTemplate/
title: Google API Core Client - Class PathTemplate (1.51.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:17.305218+00:00
---

# Google API Core Client - Class PathTemplate (1.51.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/gax/latest/PathTemplate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Core Client - Class PathTemplate (1.51.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.51.0 (latest)  1.46.0  1.43.0  1.42.5  1.40.0  1.38.2  1.36.1  1.35.1 

Reference documentation and code samples for the Google API Core Client class PathTemplate.

Represents a path template.

Templates use the syntax of the API platform; see the protobuf of HttpRule for details. A template consists of a sequence of literals, wildcards, and variable bindings, where each binding can have a sub-path. A string representation can be parsed into an instance of PathTemplate, which can then be used to perform matching and instantiation.

## Namespace

Google \ ApiCore

## Implements

\Google\ApiCore\ResourceTemplate\ResourceTemplateInterface

## Methods 

### __construct

PathTemplate constructor.

**Parameter**  
---  
**Name** | **Description**  
`path` |  `string`   
A path template string  
  
### __toString

**Returns**  
---  
**Type** | **Description**  
`string` | A string representation of the path template  
  
### render

Renders a path template using the provided bindings.

**Parameters**  
---  
**Name** | **Description**  
`bindings` |  `array`   
An array matching var names to binding strings.  
`urlEncode` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | A rendered representation of this path template.  
  
### matches

Check if $path matches a resource string.

**Parameter**  
---  
**Name** | **Description**  
`path` |  `string`   
A resource string.  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### match

Matches a fully qualified path template string.

**Parameter**  
---  
**Name** | **Description**  
`path` |  `string`   
A fully qualified path template string.  
**Returns**  
---  
**Type** | **Description**  
`array` | Array matching var names to binding values.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
