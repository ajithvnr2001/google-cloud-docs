---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DerivedTable/graph_derived_tables_for_model/
title: Get Derived Table graph for model \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:58.299893+00:00
---

# Get Derived Table graph for model  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DerivedTable/graph_derived_tables_for_model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get Derived Table graph for model Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Discover information about derived tables

## Request

GET /derived_table/graph/model/{model} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

model

string 

The name of the Lookml model.

query

HTTP Query 

Expand HTTP Query definition... 

format

string 

The format of the graph. Valid values are [dot]. Default is `dot`

color

string 

Color denoting the build status of the graph. Grey = not built, green = built, yellow = building, red = error.

## Response

### 200: Derived Table

Datatype

Description

(object)

[DependencyGraph](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DependencyGraph)

graph_text

_lock_

string 

The graph structure in the dot language that can be rendered into an image.

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 404: Not Found

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 429: Too Many Requests

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

## Examples

### TypeScript

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/typescript/dependencyGraph.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/typescript/dependencyGraph.ts#L11 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/typescript/dependencyGraph.ts")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
