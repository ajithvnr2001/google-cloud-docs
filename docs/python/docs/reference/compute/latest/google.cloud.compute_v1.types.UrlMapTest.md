---
url: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.UrlMapTest
title: Class UrlMapTest (1.56.0rc1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:53.468979+00:00
---

# Class UrlMapTest (1.56.0rc1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.UrlMapTest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UrlMapTest (1.56.0rc1) Stay organized with collections  Save and categorize content based on your preferences. 

1.56.0-rc1  1.55.0 (latest)  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.2  1.18.0  1.17.0  1.16.1  1.15.0  1.14.1  1.13.0  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 
    
    
    UrlMapTest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message for the expected URL mappings.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`description` |  `str`   
Description of this test case. This field is a member of `oneof`_ `_description`.   
`expected_output_url` |  `str`   
The expected output URL evaluated by the load balancer containing the scheme, host, path and query parameters. For rules that forward requests to backends, the test passes only whenexpectedOutputUrl matches the request forwarded by the load balancer to backends. For rules with urlRewrite, the test verifies that the forwarded request matcheshostRewrite and pathPrefixRewrite in theurlRewrite action. When service is specified,expectedOutputUrl`s scheme is ignored. For rules with urlRedirect, the test passes only ifexpectedOutputUrl matches the URL in the load balancer's redirect response. If urlRedirect specifieshttps_redirect, the test passes only if the scheme inexpectedOutputUrl is also set to HTTPS. If urlRedirect specifies strip_query, the test passes only if expectedOutputUrl does not contain any query parameters. expectedOutputUrl is optional whenservice is specified. This field is a member of `oneof`_ `_expected_output_url`.   
`expected_redirect_response_code` |  `int`   
For rules with urlRedirect, the test passes only ifexpectedRedirectResponseCode matches the HTTP status code in load balancer's redirect response. expectedRedirectResponseCode cannot be set whenservice is set. This field is a member of `oneof`_ `_expected_redirect_response_code`.   
`headers` |  `MutableSequence[[google.cloud.compute_v1.types.UrlMapTestHeader](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.UrlMapTestHeader)]`   
HTTP headers for this request. If headers contains a host header, then host must also match the header value.   
`host` |  `str`   
Host portion of the URL. If headers contains a host header, then host must also match the header value. This field is a member of `oneof`_ `_host`.   
`path` |  `str`   
Path portion of the URL. This field is a member of `oneof`_ `_path`.   
`service` |  `str`   
Expected BackendService or BackendBucket resource the given URL should be mapped to. The service field cannot be set if expectedRedirectResponseCode is set. This field is a member of `oneof`_ `_service`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
