---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ClientSettings
title: Class ClientSettings (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:55.353681+00:00
---

# Class ClientSettings (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ClientSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ClientSettings (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 
    
    
    ClientSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for clients to protect with reCAPTCHA.

## Attributes  
  
---  
**Name** | **Description**  
`allowed_domains` |  `MutableSequence[str]`   
Optional. Domains or subdomains of websites allowed to use the policy. All subdomains of an allowed domain are automatically allowed. A valid domain requires a host and must not include any path, port, query or fragment. Examples: 'example.com' or 'subdomain.example.com' Each policy supports a maximum of 250 domains. To use a policy on more domains, set `allow_all_domains` to true. When this is set, you are responsible for validating the hostname by checking the `token_properties.hostname` field in each assessment response against your list of allowed domains.   
`allow_all_domains` |  `bool`   
Optional. If set to true, it means allowed_domains are not enforced.   
`protected_endpoint_group` |  `[google.cloud.recaptchaenterprise_v1.types.ProtectedEndpointGroup](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ProtectedEndpointGroup)`   
Optional. Configuration for all API endpoints to protect with reCAPTCHA. If this field is not set, reCAPTCHA will not automatically request tokens on any API endpoints.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
