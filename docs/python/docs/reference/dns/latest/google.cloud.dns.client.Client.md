---
url: https://docs.cloud.google.com/python/docs/reference/dns/latest/google.cloud.dns.client.Client
title: Class Client (0.37.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:26.202646+00:00
---

# Class Client (0.37.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dns/latest/google.cloud.dns.client.Client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Client (0.37.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.37.2 (latest)  0.37.1  0.36.1  0.35.1  0.34.2  0.33.1  0.32.3  0.31.0  0.30.2 
    
    
    Client(
        project=None, credentials=None, _http=None, client_info=None, client_options=None
    )

Client to bundle configuration needed for API requests.

## Parameters  
  
---  
**Name** | **Description**  
`project` |  `str`   
the project which the client acts on behalf of. Will be passed when creating a zone. If not passed, falls back to the default inferred from the environment.  
`credentials` |  ``google.auth.credentials.Credentials``   
(Optional) The OAuth2 Credentials to use for this client. If not passed (and if no `_http` object is passed), falls back to the default inferred from the environment.  
`_http` |  ``requests.Session``   
(Optional) HTTP object to make requests. Can be any object that defines `request()` with the same interface as `requests.Session.request`. If not passed, an `_http` object is created that is bound to the `credentials` for the current object. This parameter should be considered private, and could change in the future.  
`client_info` |  ``google.api_core.client_info.ClientInfo``   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own library or partner tool.  
`client_options` |  ``google.api_core.client_options.ClientOptions` or `dict``   
(Optional) Client options used to set user options on the client. API Endpoint should be set through client_options.  
  
## Methods 

### list_zones
    
    
    list_zones(max_results=None, page_token=None)

List zones for the project associated with this client.

See <https://cloud.google.com/dns/api/v1/managedZones/list>

**Parameters**  
---  
**Name** | **Description**  
`max_results` |  `int`   
maximum number of zones to return, If not passed, defaults to a value set by the API.  
`page_token` |  `str`   
Optional. If present, return the next batch of zones, using the value, which must correspond to the `nextPageToken` value returned in the previous response. Deprecated: use the `pages` property of the returned iterator instead of manually passing the token.  
**Returns**  
---  
**Type** | **Description**  
``google.api_core.page_iterator.Iterator`` | Iterator of [ManagedZone](https://docs.cloud.google.com/python/docs/reference/dns/latest/google.cloud.dns.zone.ManagedZone) belonging to this project.  
  
### quotas
    
    
    quotas()

Return DNS quotas for the project associated with this client.

See <https://cloud.google.com/dns/api/v1/projects/get>

**Returns**  
---  
**Type** | **Description**  
`mapping` | keys for the mapping correspond to those of the `quota` sub-mapping of the project resource. `kind` is stripped from the results.  
  
### zone
    
    
    zone(name, dns_name=None, description=None)

Construct a zone bound to this client.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `str`   
Name of the zone.  
`dns_name` |  `str`   
(Optional) DNS name of the zone. If not passed, then calls to `zone.create` will fail.  
`description` |  `str`   
(Optional) the description for the zone. If not passed, defaults to the value of 'dns_name'.  
**Returns**  
---  
**Type** | **Description**  
`[ManagedZone](https://docs.cloud.google.com/python/docs/reference/dns/latest/google.cloud.dns.zone.ManagedZone)` | a new `ManagedZone` instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
