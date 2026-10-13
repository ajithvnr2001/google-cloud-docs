---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AuthConfig
title: Class AuthConfig (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:30.110389+00:00
---

# Class AuthConfig (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AuthConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AuthConfig (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    AuthConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

AuthConfig represents the authentication information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`google_service_account_config` |  `[google.cloud.apihub_v1.types.GoogleServiceAccountConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GoogleServiceAccountConfig)`   
Google Service Account. This field is a member of `oneof`_ `config`.   
`user_password_config` |  `[google.cloud.apihub_v1.types.AuthConfig.UserPasswordConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AuthConfig.UserPasswordConfig)`   
User Password. This field is a member of `oneof`_ `config`.   
`api_key_config` |  `[google.cloud.apihub_v1.types.AuthConfig.ApiKeyConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AuthConfig.ApiKeyConfig)`   
Api Key Config. This field is a member of `oneof`_ `config`.   
`oauth2_client_credentials_config` |  `[google.cloud.apihub_v1.types.AuthConfig.Oauth2ClientCredentialsConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AuthConfig.Oauth2ClientCredentialsConfig)`   
Oauth2.0 Client Credentials. This field is a member of `oneof`_ `config`.   
`auth_type` |  `[google.cloud.apihub_v1.types.AuthType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AuthType)`   
Required. The authentication type.   
  
## Classes 

### ApiKeyConfig
    
    
    ApiKeyConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Config for authentication with API key.

### Oauth2ClientCredentialsConfig
    
    
    Oauth2ClientCredentialsConfig(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Parameters to support Oauth 2.0 client credentials grant authentication. See <https://tools.ietf.org/html/rfc6749#section-1.3.4> for more details.

### UserPasswordConfig
    
    
    UserPasswordConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Parameters to support Username and Password Authentication.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
