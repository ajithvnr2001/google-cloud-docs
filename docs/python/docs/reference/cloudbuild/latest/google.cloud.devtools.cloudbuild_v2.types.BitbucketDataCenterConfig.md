---
url: https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BitbucketDataCenterConfig
title: Class BitbucketDataCenterConfig (3.40.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:38:13.624610+00:00
---

# Class BitbucketDataCenterConfig (3.40.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BitbucketDataCenterConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BitbucketDataCenterConfig (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.1  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.3  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.2  3.23.3  3.22.0  3.21.0  3.20.1  3.19.0  3.18.0  3.17.1  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.1  3.10.0  3.9.3  3.8.3  3.7.1  3.6.0  3.5.2  3.4.0  3.3.2  3.2.1  3.1.1  3.0.2  2.0.2  1.1.2  1.0.0  0.1.0 
    
    
    BitbucketDataCenterConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for connections to Bitbucket Data Center.

## Attributes  
  
---  
**Name** | **Description**  
`host_uri` |  `str`   
Required. The URI of the Bitbucket Data Center instance or cluster this connection is for.   
`webhook_secret_secret_version` |  `str`   
Required. Immutable. SecretManager resource containing the webhook secret used to verify webhook events, formatted as `projects/*/secrets/*/versions/*`.   
`read_authorizer_credential` |  `[google.cloud.devtools.cloudbuild_v2.types.UserCredential](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.UserCredential)`   
Required. A http access token with the `REPO_READ` access.   
`authorizer_credential` |  `[google.cloud.devtools.cloudbuild_v2.types.UserCredential](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.UserCredential)`   
Required. A http access token with the `REPO_ADMIN` scope access.   
`service_directory_config` |  `[google.cloud.devtools.cloudbuild_v2.types.ServiceDirectoryConfig](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ServiceDirectoryConfig)`   
Optional. Configuration for using Service Directory to privately connect to a Bitbucket Data Center. This should only be set if the Bitbucket Data Center is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the Bitbucket Data Center will be made over the public internet.   
`ssl_ca` |  `str`   
Optional. SSL certificate to use for requests to the Bitbucket Data Center.   
`server_version` |  `str`   
Output only. Version of the Bitbucket Data Center running on the `host_uri`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
