---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CorsPolicy
title: Class CorsPolicy (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:08.123621+00:00
---

# Class CorsPolicy (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CorsPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CorsPolicy (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    CorsPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The specification for allowing client-side cross-origin requests. For more information about the W3C recommendation for cross-origin resource sharing (CORS), see Fetch API Living Standard.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`allow_credentials` |  `bool`   
In response to a preflight request, setting this to true indicates that the actual request can include user credentials. This field translates to the Access-Control-Allow-Credentials header. Default is false. This field is a member of `oneof`_ `_allow_credentials`.   
`allow_headers` |  `MutableSequence[str]`   
Specifies the content for the Access-Control-Allow-Headers header.   
`allow_methods` |  `MutableSequence[str]`   
Specifies the content for the Access-Control-Allow-Methods header.   
`allow_origin_regexes` |  `MutableSequence[str]`   
Specifies a regular expression that matches allowed origins. For more information, see regular expression syntax. An origin is allowed if it matches either an item inallowOrigins or an item inallowOriginRegexes. Regular expressions can only be used when the loadBalancingScheme is set to INTERNAL_SELF_MANAGED.   
`allow_origins` |  `MutableSequence[str]`   
Specifies the list of origins that is allowed to do CORS requests. An origin is allowed if it matches either an item inallowOrigins or an item inallowOriginRegexes.   
`disabled` |  `bool`   
If true, disables the CORS policy. The default value is false, which indicates that the CORS policy is in effect. This field is a member of `oneof`_ `_disabled`.   
`expose_headers` |  `MutableSequence[str]`   
Specifies the content for the Access-Control-Expose-Headers header.   
`max_age` |  `int`   
Specifies how long results of a preflight request can be cached in seconds. This field translates to the Access-Control-Max-Age header. This field is a member of `oneof`_ `_max_age`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
