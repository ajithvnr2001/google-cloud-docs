---
url: https://docs.cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos/patch/
title: Method: projects.repos.patch \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:36.470051+00:00
---

# Method: projects.repos.patch  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos/patch/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Reference ](https://docs.cloud.google.com/source-repositories/docs/apis)



Send feedback 

#  Method: projects.repos.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Updates information about a repo.

### HTTP request

`PATCH https://sourcerepo.googleapis.com/v1/{name=projects/*/repos/**}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The name of the requested repository. Values are of the form `projects/<project>/repos/<repo>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `source.repos.updateRepoConfig`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "repo": {
        object ([Repo](https://docs.cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos#Repo))
      },
      "updateMask": string
    }  
  
Fields  
---  
`repo` |  `object (`[Repo](https://docs.cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos#Repo)`)` The new configuration for the repository.  
`updateMask` |  `string (`[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)` format)` A FieldMask specifying which fields of the repo to modify. Only the fields in the mask will be modified. If no mask is provided, this request is no-op.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Response body

If successful, the response body contains an instance of `[Repo](https://docs.cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos#Repo)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
