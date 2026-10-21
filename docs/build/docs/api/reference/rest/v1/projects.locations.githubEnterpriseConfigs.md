---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs
title: REST Resource: projects.locations.githubEnterpriseConfigs \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:21.500733+00:00
---

# REST Resource: projects.locations.githubEnterpriseConfigs  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  REST Resource: projects.locations.githubEnterpriseConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GitHubEnterpriseConfig
    * JSON representation
  * Methods



## Resource: GitHubEnterpriseConfig

GitHubEnterpriseConfig represents a configuration for a GitHub Enterprise server.

JSON representation  
---  
      
    
    {
      "name": string,
      "hostUrl": string,
      "appId": string,
      "createTime": string,
      "webhookKey": string,
      "peeredNetwork": string,
      "secrets": {
        object ([GitHubEnterpriseSecrets](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.githubEnterpriseConfigs#GitHubEnterpriseConfig.GitHubEnterpriseSecrets))
      },
      "displayName": string,
      "sslCa": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The full resource name for the GitHubEnterpriseConfig For example: "projects/{$projectId}/locations/{$locationId}/githubEnterpriseConfigs/{$configId}"  
`hostUrl` |  `string` The URL of the github enterprise host the configuration is for.  
`appId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The GitHub app id of the Cloud Build app on the GitHub Enterprise server.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the installation was associated with the project.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`webhookKey` |  `string` The key that should be attached to webhook calls to the v1.webhook endpoint.  
`peeredNetwork` |  `string` Optional. The network to be used when reaching out to the GitHub Enterprise server. The VPC network must be enabled for private service connection. This should be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, no network peering will occur and calls to the GitHub Enterprise server will be made over the public internet. Must be in the format `projects/{project}/global/networks/{network}`, where {project} is a project number or id and {network} is the name of a VPC network in the project.  
`secrets` |  `object (`[GitHubEnterpriseSecrets](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.githubEnterpriseConfigs#GitHubEnterpriseConfig.GitHubEnterpriseSecrets)`)` Optional. Names of secrets in Secret Manager.  
`displayName` |  `string` Optional. Name to display for this config.  
`sslCa` |  `string` Optional. SSL certificate to use for requests to GitHub Enterprise.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/create)`

|  Create an association between a GCP project and a GitHub Enterprise server.  
  
### `[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/delete)`

|  Delete an association between a GCP project and a GitHub Enterprise server.  
  
### `[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/get)`

|  Retrieve a GitHubEnterpriseConfig.  
  
### `[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/list)`

|  List all GitHubEnterpriseConfigs for a given project.  
  
### `[patch](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/patch)`

|  Update an association between a GCP project and a GitHub Enterprise server.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-22 UTC."],[],[]] 
