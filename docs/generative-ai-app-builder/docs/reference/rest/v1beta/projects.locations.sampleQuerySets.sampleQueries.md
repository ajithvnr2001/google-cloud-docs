---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries
title: REST Resource: projects.locations.sampleQuerySets.sampleQueries \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:10.066028+00:00
---

# REST Resource: projects.locations.sampleQuerySets.sampleQueries  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  REST Resource: projects.locations.sampleQuerySets.sampleQueries Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SampleQuery
    * JSON representation
  * QueryEntry
    * JSON representation
  * Target
    * JSON representation
  * Methods



## Resource: SampleQuery

Sample Query captures metadata to be used for evaluation.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "queryEntry": {
        object ([QueryEntry](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries#QueryEntry))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The full resource name of the sample query, in the format of `projects/{project}/locations/{location}/sampleQuerySets/{sampleQuerySet}/sampleQueries/{sampleQuery}`.This field must be a UTF-8 encoded string with a length limit of 1024 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the `[SampleQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)` was created at.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
The content of the sample query. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`queryEntry` |  `object (`[QueryEntry](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries#QueryEntry)`)` The query entry.  
End of mutually exclusive fields.  
  
## QueryEntry

Query Entry captures metadata to be used for search evaluation.

JSON representation  
---  
      
    
    {
      "query": string,
      "targets": [
        {
          object ([Target](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries#Target))
        }
      ]
    }  
  
Fields  
---  
`query` |  `string` Required. The query.  
`targets[]` |  `object (`[Target](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries#Target)`)` List of targets for the query.  
  
## Target

Defines the parameters of the query's expected outcome.

JSON representation  
---  
      
    
    {
      "uri": string,
      "pageNumbers": [
        integer
      ],
      "score": number
    }  
  
Fields  
---  
`uri` |  `string` Expected uri of the target.This field must be a UTF-8 encoded string with a length limit of 2048 characters.Example of valid uris: `https://example.com/abc`, `gcs://example/example.pdf`.  
`pageNumbers[]` |  `integer` Expected page numbers of the target.Each page number must be non negative.  
`score` |  `number` Relevance score of the target.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries/create)`

|  Creates a `[SampleQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`  
  
### `[delete](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries/delete)`

|  Deletes a `[SampleQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`.  
  
### `[get](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries/get)`

|  Gets a `[SampleQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`.  
  
### `[import](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries/import)`

|  Bulk import of multiple `[SampleQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`s.  
  
### `[list](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries/list)`

|  Gets a list of `[SampleQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`s.  
  
### `[patch](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries/patch)`

|  Updates a `[SampleQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.sampleQuerySets.sampleQueries#SampleQuery)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-14 UTC."],[],[]] 
