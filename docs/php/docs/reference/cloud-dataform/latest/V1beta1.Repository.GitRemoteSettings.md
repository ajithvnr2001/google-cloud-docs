---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.Repository.GitRemoteSettings
title: Google Cloud Dataform V1beta1 Client - Class GitRemoteSettings (0.17.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:16.973276+00:00
---

# Google Cloud Dataform V1beta1 Client - Class GitRemoteSettings (0.17.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.Repository.GitRemoteSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataform V1beta1 Client - Class GitRemoteSettings (0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.3  0.12.0  0.11.0  0.10.1  0.9.2  0.8.1  0.7.0  0.6.0  0.5.1  0.4.7  0.3.0  0.2.3  0.1.6 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataform V1beta1 Client class GitRemoteSettings.

Controls Git remote configuration for a repository.

Generated from protobuf message `google.cloud.dataform.v1beta1.Repository.GitRemoteSettings`

## Namespace

Google \ Cloud \ Dataform \ V1beta1 \ Repository

## Methods 

### __construct

Constructor.

**Parameter**  
---  
**Name** | **Description**  
`data` |  `mixed`   
  
  
### getUrl

Required. The Git remote's URL.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setUrl

Required. The Git remote's URL.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDefaultBranch

Optional. The Git remote's default branch name.

If not set, `main` will be used.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDefaultBranch

Optional. The Git remote's default branch name.

If not set, `main` will be used.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEffectiveDefaultBranch

Output only. The Git remote's effective default branch name.

This is the default branch name of the Git remote if it is set, otherwise it is `main`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEffectiveDefaultBranch

Output only. The Git remote's effective default branch name.

This is the default branch name of the Git remote if it is set, otherwise it is `main`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAuthenticationTokenSecretVersion

Optional. The name of the Secret Manager secret version to use as an authentication token for Git operations. Must be in the format `projects/*/secrets/*/versions/*`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setAuthenticationTokenSecretVersion

Optional. The name of the Secret Manager secret version to use as an authentication token for Git operations. Must be in the format `projects/*/secrets/*/versions/*`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSshAuthenticationConfig

Optional. Authentication fields for remote uris using SSH protocol.

**Returns**  
---  
**Type** | **Description**  
`GitRemoteSettings\SshAuthenticationConfig|null` |   
  
### hasSshAuthenticationConfig

### clearSshAuthenticationConfig

### setSshAuthenticationConfig

Optional. Authentication fields for remote uris using SSH protocol.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `GitRemoteSettings\SshAuthenticationConfig`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGitRepositoryLink

Optional. Resource name for the `GitRepositoryLink` used for machine credentials. Must be in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasGitRepositoryLink

### clearGitRepositoryLink

### setGitRepositoryLink

Optional. Resource name for the `GitRepositoryLink` used for machine credentials. Must be in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTokenStatus

Output only. Deprecated: The field does not contain any token status information. Instead use <https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/computeAccessTokenStatus>

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [TokenStatus](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.Repository.GitRemoteSettings.TokenStatus).  
  
### setTokenStatus

Output only. Deprecated: The field does not contain any token status information. Instead use <https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/computeAccessTokenStatus>

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [TokenStatus](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.Repository.GitRemoteSettings.TokenStatus).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
