---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.domainMappings/create/
title: Method: apps.domainMappings.create \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:00.735574+00:00
---

# Method: apps.domainMappings.create  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.domainMappings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  Method: apps.domainMappings.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * DomainOverrideStrategy
  * Try it!



Maps a domain to an application. A user must be authorized to administer a domain in order to map it to an application. For a list of available authorized domains, see [`AuthorizedDomains.ListAuthorizedDomains`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.domainMappings/create/).

### HTTP request

`POST https://appengine.googleapis.com/v1beta/{parent=apps/*}/domainMappings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Name of the parent Application resource. Example: `apps/myapp`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.applications.update`

  
  
### Query parameters

Parameters  
---  
`overrideStrategy` |  `enum (`[DomainOverrideStrategy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.domainMappings/create#DomainOverrideStrategy)`)` Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected.  
  
### Request body

The request body contains an instance of `[DomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.domainMappings#DomainMapping)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## DomainOverrideStrategy

Override strategy for mutating an existing mapping.

Enums  
---  
`UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY` | Strategy unspecified. Defaults to `STRICT`.  
`STRICT` | Overrides not allowed. If a mapping already exists for the specified domain, the request will return an ALREADY_EXISTS (409).  
`OVERRIDE` | Overrides allowed. If a mapping already exists for the specified domain, the request will overwrite it. Note that this might stop another Google product from serving. For example, if the domain is mapped to another App Engine application, that app will no longer serve from that domain.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
