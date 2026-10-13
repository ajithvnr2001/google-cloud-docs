---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.services.network_security.pagers.ListGatewaySecurityPoliciesPager
title: Class ListGatewaySecurityPoliciesPager (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:27.346946+00:00
---

# Class ListGatewaySecurityPoliciesPager (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.services.network_security.pagers.ListGatewaySecurityPoliciesPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListGatewaySecurityPoliciesPager (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 
    
    
    ListGatewaySecurityPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.network_security_v1alpha1.types.gateway_security_policy.ListGatewaySecurityPoliciesResponse,
        ],
        request: google.cloud.network_security_v1alpha1.types.gateway_security_policy.ListGatewaySecurityPoliciesRequest,
        response: google.cloud.network_security_v1alpha1.types.gateway_security_policy.ListGatewaySecurityPoliciesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

A pager for iterating through `list_gateway_security_policies` requests.

This class thinly wraps an initial [ListGatewaySecurityPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListGatewaySecurityPoliciesResponse) object, and provides an `__iter__` method to iterate through its `gateway_security_policies` field.

If there are more pages, the `__iter__` method will make additional `ListGatewaySecurityPolicies` requests and continue to iterate through the `gateway_security_policies` field on the corresponding responses.

All the usual [ListGatewaySecurityPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListGatewaySecurityPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListGatewaySecurityPoliciesPager
    
    
    ListGatewaySecurityPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.network_security_v1alpha1.types.gateway_security_policy.ListGatewaySecurityPoliciesResponse,
        ],
        request: google.cloud.network_security_v1alpha1.types.gateway_security_policy.ListGatewaySecurityPoliciesRequest,
        response: google.cloud.network_security_v1alpha1.types.gateway_security_policy.ListGatewaySecurityPoliciesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

**Parameters**  
---  
**Name** | **Description**  
`method` |  `Callable`   
The method that was originally called, and which instantiated this pager.  
`request` |  `[google.cloud.network_security_v1alpha1.types.ListGatewaySecurityPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListGatewaySecurityPoliciesRequest)`   
The initial request object.  
`response` |  `[google.cloud.network_security_v1alpha1.types.ListGatewaySecurityPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListGatewaySecurityPoliciesResponse)`   
The initial response object.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
