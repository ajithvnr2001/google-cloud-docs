---
url: https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.Repository.GitRemoteSettings
title: Class GitRemoteSettings (0.11.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:38.452433+00:00
---

# Class GitRemoteSettings (0.11.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.Repository.GitRemoteSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GitRemoteSettings (0.11.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.4 (latest)  0.11.3  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.16  0.4.1  0.3.0  0.2.3  0.1.0 
    
    
    GitRemoteSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Controls Git remote configuration for a repository.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`url` |  `str`   
Required. The Git remote's URL.   
`default_branch` |  `str`   
Optional. The Git remote's default branch name. If not set, `main` will be used.   
`effective_default_branch` |  `str`   
Output only. The Git remote's effective default branch name. This is the default branch name of the Git remote if it is set, otherwise it is `main`.   
`authentication_token_secret_version` |  `str`   
Optional. The name of the Secret Manager secret version to use as an authentication token for Git operations. Must be in the format `projects/*/secrets/*/versions/*`.   
`ssh_authentication_config` |  `[google.cloud.dataform_v1.types.Repository.GitRemoteSettings.SshAuthenticationConfig](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.Repository.GitRemoteSettings.SshAuthenticationConfig)`   
Optional. Authentication fields for remote uris using SSH protocol.   
`git_repository_link` |  `str`   
Optional. Resource name for the `GitRepositoryLink` used for machine credentials. Must be in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*` This field is a member of `oneof`_ `_git_repository_link`.   
`token_status` |  `[google.cloud.dataform_v1.types.Repository.GitRemoteSettings.TokenStatus](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.Repository.GitRemoteSettings.TokenStatus)`   
Output only. Deprecated: The field does not contain any token status information.   
  
## Classes 

### SshAuthenticationConfig
    
    
    SshAuthenticationConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configures fields for performing SSH authentication.

### TokenStatus
    
    
    TokenStatus(value)

The status of the authentication token.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
