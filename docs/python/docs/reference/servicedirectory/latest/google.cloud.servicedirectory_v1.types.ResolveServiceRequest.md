---
url: https://docs.cloud.google.com/python/docs/reference/servicedirectory/latest/google.cloud.servicedirectory_v1.types.ResolveServiceRequest
title: Class ResolveServiceRequest (1.19.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:15.149924+00:00
---

# Class ResolveServiceRequest (1.19.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/servicedirectory/latest/google.cloud.servicedirectory_v1.types.ResolveServiceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ResolveServiceRequest (1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.12.1  1.11.6  1.10.0  1.9.1  1.8.2  1.7.1  1.6.0  1.5.3  1.4.1  1.3.1  1.2.1  1.1.0  1.0.4  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    ResolveServiceRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The request message for LookupService.ResolveService. Looks up a service by its name, returns the service and its endpoints.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the service to resolve.   
`max_endpoints` |  `int`   
Optional. The maximum number of endpoints to return. Defaults to 25. Maximum is 100. If a value less than one is specified, the Default is used. If a value greater than the Maximum is specified, the Maximum is used.   
`endpoint_filter` |  `str`   
Optional. The filter applied to the endpoints of the resolved service. General `filter` string syntax: `` \- `` can be `name`, `address`, `port`, or `annotations.` for map field \- `` can be ``, `>`, `<>`, `>=`, `!=`, `=`, `:`. Of which `:` means `HAS`, and is roughly the same as `=` \- `` must be the same data type as field \- `` can be `AND`, `OR`, `NOT` Examples of valid filters: \- `annotations.owner` returns endpoints that have a annotation with the key `owner`, this is the same as `annotations:owner` \- `annotations.protocol=gRPC` returns endpoints that have key/value `protocol=gRPC` \- `address=192.108.1.105` returns endpoints that have this address \- `port>8080` returns endpoints that have port number larger than 8080 \- `name>projects/my-project/locations/us-east1/namespaces/my-namespace/services/my-service/endpoints/endpoint-c` returns endpoints that have name that is alphabetically later than the string, so "endpoint-e" is returned but "endpoint-a" is not \\* `name=projects/my-project/locations/us-central1/namespaces/my-namespace/services/my-service/endpoints/ep-1` returns the endpoint that has an endpoint_id equal to `ep-1` \- `annotations.owner!=sd AND annotations.foo=bar` returns endpoints that have `owner` in annotation key but value is not `sd` AND have key/value `foo=bar` \- `doesnotexist.foo=bar` returns an empty list. Note that endpoint doesn't have a field called "doesnotexist". Since the filter does not match any endpoint, it returns no results For more information about filtering, see `API Filtering   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
