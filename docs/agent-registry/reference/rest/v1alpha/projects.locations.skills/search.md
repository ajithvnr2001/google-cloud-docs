---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/search/
title: Method: projects.locations.skills.search \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:44.755727+00:00
---

# Method: projects.locations.skills.search  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  Method: projects.locations.skills.search Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * SearchType
  * Try it!



Custom deep-search method to filter by frontmatter or query SKILL.md text blobs.

### HTTP request

`GET https://agentregistry.googleapis.com/v1alpha/{parent=projects/*/locations/*}/skills:search`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for SearchSkillsRequest. Format: `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`searchType` |  `enum (`[SearchType](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/search#SearchType)`)` Optional. The type of search.  
`searchString` |  `string` Optional. Search criteria used to select the Skills to return. If no search criteria is specified then all accessible Skills will be returned.Search expressions can be used to restrict results based upon searchable fields, where the operators can be used along with the suffix wildcard symbol `*`. See [instructions](https://docs.cloud.google.com/agent-registry/search-agents-and-tools) for more details.Allowed operators: `=`, `:`, `NOT`, `AND`, `OR`, and `()`.Searchable fields: | Field  | `=` | `:` | `*` | Keyword Search   
---|---|---|---|---  
skillId  | Yes  | Yes  | Yes  | Included   
name  | No  | Yes  | Yes  | Included   
displayName  | No  | Yes  | Yes  | Included   
description  | No  | Yes  | No  | Included   
frontmatter.name  | No  | Yes  | No  | Included   
frontmatter.description  | No  | Yes  | No  | Included   
frontmatter.compatibility  | No  | Yes  | No  | Included   
frontmatter.license  | No  | Yes  | No  | Included   
  
Examples:

  * `skillId="urn:skill:projects-1234:locations:global:private-important-skill"` to find the skill with the specified skill ID.
  * `name:important` to find skills whose name contains `important` as a word.
  * `displayName:works*` to find skills whose display name contains words that start with `works`.

  
`filter` |  `string` Optional. Use this field to specify additional filter criteria on search results. Filter expressions can be used to restrict results based upon filterable fields, where equality operators can be used. See [instructions](https://docs.cloud.google.com/agent-registry/search-agents-and-tools) for more details.Allowed operators: `=`, `<`, `>`, `NOT`, `AND`, `OR`, and `()`. | Field  | `=` | `<`, `>`  
---|---|---  
state  | Yes  | No   
targetState  | Yes  | No   
createTime  | Yes  | Yes   
updateTime  | Yes  | Yes   
  
Examples:

  * `state=ACTIVE` to restrict results to skills in the `ACTIVE` state.

  
`pageSize` |  `integer` Optional. The maximum number of search results to return per page. The page size is capped at `100`, even if a larger value is specified. A negative value will result in an `INVALID_ARGUMENT` error. If unspecified or set to `0`, a default value of `20` will be used. The server may return fewer results than requested.  
`pageToken` |  `string` Optional. If present, retrieve the next batch of results from the preceding call to this method. `pageToken` must be the value of `nextPageToken` from the previous response. The values of all other method parameters, must be identical to those in the previous call.  
  
### Request body

The request body must be empty.

### Response body

Response listing searched Skills.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "skills": [
        {
          object ([Skill](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills#Skill))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`skills[]` |  `object (`[Skill](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills#Skill)`)` Matched Skills list.  
`nextPageToken` |  `string` Query page offset continuation token.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.skills.search`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## SearchType

The type of search to perform. Additional search types may be supported in the future.

Enums  
---  
`SEARCH_TYPE_UNSPECIFIED` | Invalid search type.  
`KEYWORD` | Search for a keyword across all searchable fields.  
`SEMANTIC` | Search based on the meaning and intent of a natural language query.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-24 UTC."],[],[]] 
