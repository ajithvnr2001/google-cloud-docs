---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitLabEnterpriseConfig
title: Class GitLabEnterpriseConfig (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:37.409965+00:00
---

# Class GitLabEnterpriseConfig (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitLabEnterpriseConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GitLabEnterpriseConfig (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    GitLabEnterpriseConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for connections to an instance of GitLab Enterprise.

## Attributes  
  
---  
**Name** | **Description**  
`host_uri` |  `str`   
Required. The URI of the GitLab Enterprise host this connection is for.   
`webhook_secret_secret_version` |  `str`   
Required. Immutable. SecretManager resource containing the webhook secret of a GitLab project, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). This is used to validate webhooks.   
`read_authorizer_credential` |  `[google.cloud.developerconnect_v1.types.UserCredential](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UserCredential)`   
Required. A GitLab personal access token with the minimum `read_api` scope access and a minimum role of `reporter`. The GitLab Projects visible to this Personal Access Token will control which Projects Developer Connect has access to.   
`authorizer_credential` |  `[google.cloud.developerconnect_v1.types.UserCredential](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UserCredential)`   
Required. A GitLab personal access token with the minimum `api` scope access and a minimum role of `maintainer`. The GitLab Projects visible to this Personal Access Token will control which Projects Developer Connect has access to.   
`service_directory_config` |  `[google.cloud.developerconnect_v1.types.ServiceDirectoryConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ServiceDirectoryConfig)`   
Optional. Configuration for using Service Directory to privately connect to a GitLab Enterprise instance. This should only be set if the GitLab Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitLab Enterprise server will be made over the public internet.   
`ssl_ca_certificate` |  `str`   
Optional. SSL Certificate Authority certificate to use for requests to GitLab Enterprise instance.   
`server_version` |  `str`   
Output only. Version of the GitLab Enterprise server running on the `host_uri`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
