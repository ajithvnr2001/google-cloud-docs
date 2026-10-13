---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitHubEnterpriseConfig
title: Class GitHubEnterpriseConfig (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:36.816101+00:00
---

# Class GitHubEnterpriseConfig (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitHubEnterpriseConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GitHubEnterpriseConfig (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    GitHubEnterpriseConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for connections to an instance of GitHub Enterprise.

## Attributes  
  
---  
**Name** | **Description**  
`host_uri` |  `str`   
Required. The URI of the GitHub Enterprise host this connection is for.   
`app_id` |  `int`   
Optional. ID of the GitHub App created from the manifest.   
`app_slug` |  `str`   
Output only. The URL-friendly name of the GitHub App.   
`private_key_secret_version` |  `str`   
Optional. SecretManager resource containing the private key of the GitHub App, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location).   
`webhook_secret_secret_version` |  `str`   
Optional. SecretManager resource containing the webhook secret of the GitHub App, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location).   
`app_installation_id` |  `int`   
Optional. ID of the installation of the GitHub App.   
`installation_uri` |  `str`   
Output only. The URI to navigate to in order to manage the installation associated with this GitHubEnterpriseConfig.   
`service_directory_config` |  `[google.cloud.developerconnect_v1.types.ServiceDirectoryConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ServiceDirectoryConfig)`   
Optional. Configuration for using Service Directory to privately connect to a GitHub Enterprise server. This should only be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitHub Enterprise server will be made over the public internet.   
`server_version` |  `str`   
Output only. GitHub Enterprise version installed at the host_uri.   
`ssl_ca_certificate` |  `str`   
Optional. SSL certificate to use for requests to GitHub Enterprise.   
`organization` |  `str`   
Optional. Immutable. GitHub Enterprise organization in which the GitHub App is created.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
