---
url: https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups
title: REST Resource: projects.locations.codeRepositoryIndexes.repositoryGroups \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:34.717289+00:00
---

# REST Resource: projects.locations.codeRepositoryIndexes.repositoryGroups  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ API and references ](https://docs.cloud.google.com/gemini/docs/api-and-reference)



Send feedback 

#  REST Resource: projects.locations.codeRepositoryIndexes.repositoryGroups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: RepositoryGroup
    * JSON representation
  * Repository
    * JSON representation
  * Methods



## Resource: RepositoryGroup

Message describing RepositoryGroup object

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "repositories": [
        {
          object ([Repository](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups#Repository))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. name of resource  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time stampUses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time stampUses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`repositories[]` |  `object (`[Repository](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups#Repository)`)` Required. List of repositories to group  
  
## Repository

Repository contains RAG indexing settings for the provided Git repository

JSON representation  
---  
      
    
    {
      "resource": string,
      "branchPattern": string
    }  
  
Fields  
---  
`resource` |  `string` Required. The DeveloperConnect repository full resource name, relative resource name or resource URL to be indexed.  
`branchPattern` |  `string` Required. The Git branch pattern used for indexing in RE2 syntax. See <https://github.com/google/re2/wiki/syntax> for syntax.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups/create)`

|  Creates a new RepositoryGroup in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups/delete)`

|  Deletes a single RepositoryGroup.  
  
### `[get](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups/get)`

|  Gets details of a single RepositoryGroup.  
  
### `[getIamPolicy](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups/list)`

|  Lists RepositoryGroups in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups/patch)`

|  Updates the parameters of a single RepositoryGroup.  
  
### `[setIamPolicy](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
