---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest/
title: Package google.cloud.healthcare.v1.fhir.rest \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:54.732455+00:00
---

# Package google.cloud.healthcare.v1.fhir.rest  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)



Send feedback 

#  Package google.cloud.healthcare.v1.fhir.rest Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[FhirService](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.FhirService)` (interface)
  * `[CreateResourceRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.CreateResourceRequest)` (message)
  * `[DeleteResourceRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.DeleteResourceRequest)` (message)
  * `[DeleteResourceVersionsRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.DeleteResourceVersionsRequest)` (message)
  * `[ExecuteBundleRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.ExecuteBundleRequest)` (message)
  * `[GetCapabilityStatementRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.GetCapabilityStatementRequest)` (message)
  * `[GetPatientEverythingRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.GetPatientEverythingRequest)` (message)
  * `[GetResourceRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.GetResourceRequest)` (message)
  * `[GetResourceVersionRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.GetResourceVersionRequest)` (message)
  * `[ListResourceVersionsRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.ListResourceVersionsRequest)` (message)
  * `[PatchResourceRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.PatchResourceRequest)` (message)
  * `[SearchResourcesRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.SearchResourcesRequest)` (message)
  * `[UpdateResourceRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/fhir/rest#google.cloud.healthcare.v1.fhir.rest.UpdateResourceRequest)` (message)



## CreateResourceRequest

Creates a resource in the specified FHIR store.

Fields  
---  
`parent` |  `string` The name of the FHIR store this resource belongs to. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `healthcare.fhirResources.create`

  
`type` |  `string` The FHIR resource type to create, such as Patient or Observation. For a complete list, see the FHIR Resource Index ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/resourcelist.html), [STU3](http://hl7.org/implement/standards/fhir/STU3/resourcelist.html), [R4](http://hl7.org/implement/standards/fhir/R4/resourcelist.html)). Must match the resource type in the provided content.  
`request_body` |  ``[HttpBody](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.api#google.api.HttpBody)`` Raw body of the request.  
  
## DeleteResourceRequest

Deletes a resource from the specified FHIR store.

Fields  
---  
`name` |  `string` The name of the resource to delete. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.fhirResources.delete`

  
  
## DeleteResourceVersionsRequest

Deletes all the historical versions of a resource (excluding current version) from the FHIR store.

Fields  
---  
`name` |  `string` The name of the resource to purge. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.fhirResources.purge`

  
  
## ExecuteBundleRequest

Request to execute all included operations in a Bundle.

Fields  
---  
`parent` |  `string` Name of the FHIR store in which this bundle will be executed.  
`request_body` |  ``[HttpBody](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.api#google.api.HttpBody)`` The bundle to execute.  
  
## GetCapabilityStatementRequest

Request the capabilities of the system.

Fields  
---  
`name` |  `string` Name of the FHIR store to retrieve the capabilities for.  
  
## GetPatientEverythingRequest

Request all the information related to the patient.

Fields  
---  
`name` |  `string` Name of the `Patient` resource for which the information is required.  
`start` |  `string` The response includes records subsequent to the start date. If no start date is provided, all records prior to the end date are in scope.  
`end` |  `string` The response includes records prior to the end date. If no end date is provided, all records subsequent to the start date are in scope.  
`page_token` |  `string` Used to retrieve the next or previous page of results when using pagination. Set `_page_token` to the value of _page_token set in next or previous page links' url. Next and previous page are returned in the response bundle's links field, where `link.relation` is "previous" or "next".Omit `_page_token` if no previous request has been made.  
`count` |  `int32` Maximum number of resources in a page. Defaults to 100.  
`since` |  `string` If provided, only resources updated after this time are returned. The time uses the format YYYY-MM-DDThh:mm:ss.sss+zz:zz. For example, `2015-02-07T13:28:17.239+02:00` or `2017-01-01T00:00:00Z`. The time must be specified to the second and include a time zone.  
`type` |  `string` String of comma-delimited FHIR resource types. If provided, only resources of the specified resource type(s) are returned.  
  
## GetResourceRequest

Gets a resource from the specified FHIR store.

Fields  
---  
`name` |  `string` The name of the resource to retrieve. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.fhirResources.get`

  
  
## GetResourceVersionRequest

Gets a specific version of a resource from the specified FHIR store.

Fields  
---  
`name` |  `string` The name of the resource version to retrieve. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.fhirResources.get`

  
  
## ListResourceVersionsRequest

Lists all the versions of a resource from the specified FHIR store.

Fields  
---  
`name` |  `string` The name of the resource to retrieve. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.fhirResources.get`

  
`count` |  `int32` The maximum number of search results on a page. Default value is 100. Maximum value is 1,000.  
`since` |  `string` Only include resource versions that were created at or after the given instant in time. The instant in time uses the format YYYY-MM-DDThh:mm:ss.sss+zz:zz (for example 2015-02-07T13:28:17.239+02:00 or 2017-01-01T00:00:00Z). The time must be specified to the second and include a time zone.  
`at` |  `string` Only include resource versions that were current at some point during the time period specified in the date time value. The date parameter format is yyyy-mm-ddThh:mm:ss[Z|(+|-)hh:mm]Clients may specify any of the following:

  * An entire year: `_at=2019`
  * An entire month: `_at=2019-01`
  * A specific day: `_at=2019-01-20`
  * A specific second: `_at=2018-12-31T23:59:58Z`

  
`page_token` |  `string` Used to retrieve the first, previous, next, or last page of resource versions when using pagination. Value should be set to the value of `_page_token` set in next or previous page links' URLs. Next and previous page are returned in the response bundle's links field, where `link.relation` is "previous" or "next".Omit `_page_token` if no previous request has been made.  
  
## PatchResourceRequest

Request to patch the given resource.

Fields  
---  
`name` |  `string` The name of the resource to update.  
`request_body` |  ``[HttpBody](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.api#google.api.HttpBody)`` The request body needs to be in JSON Patch format, as detailed in <http://www.jsonpatch.com>  
  
## SearchResourcesRequest

Request to search the resources in the specified FHIR store.

Fields  
---  
`parent` |  `string` Name of the FHIR store to retrieve resources from. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `healthcare.fhirStores.searchResources`

  
`resource_type` |  `string` The FHIR resource type to search, such as Patient or Observation. For a complete list, see the FHIR Resource Index ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/resourcelist.html), [STU3](http://hl7.org/implement/standards/fhir/STU3/resourcelist.html), [R4](http://hl7.org/implement/standards/fhir/R4/resourcelist.html)).  
  
## UpdateResourceRequest

Request to update the given resource, or create it with the client-specified ID if it does not exist and the FhirStore has EnableUpdateCreate set.

Fields  
---  
`name` |  `string` The name of the resource to update. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.fhirResources.update`

  
`request_body` |  ``[HttpBody](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.api#google.api.HttpBody)`` The updated resource to store. The entire resource is updated.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
