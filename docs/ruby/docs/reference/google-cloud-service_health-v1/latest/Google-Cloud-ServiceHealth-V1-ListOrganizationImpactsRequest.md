---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ListOrganizationImpactsRequest/
title: Service Health V1 API - Class Google::Cloud::ServiceHealth::V1::ListOrganizationImpactsRequest (v2.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:56.346294+00:00
---

# Service Health V1 API - Class Google::Cloud::ServiceHealth::V1::ListOrganizationImpactsRequest (v2.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ListOrganizationImpactsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Health V1 API - Class Google::Cloud::ServiceHealth::V1::ListOrganizationImpactsRequest (v2.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.5.1 (latest)  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.1  1.1.0  1.0.2  0.2.0  0.1.2 

Reference documentation and code samples for the Service Health V1 API class Google::Cloud::ServiceHealth::V1::ListOrganizationImpactsRequest.

Requests list of projects under an organization affected by an event.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. A filter expression that filters resources listed in the response. The expression is in the form of `field:value` for checking if a repeated field contains a value.

Example: `events:organizations%2F{organization_id}%2Flocations%2Fglobal%2ForganizationEvents%2Fevent-id`

To get your `{organization_id}`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

Multiple filter queries are separated by spaces.

By default, each expression is an AND expression. However, you can include AND and OR expressions explicitly. Filter is supported for the following fields: `events`. 




### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A filter expression that filters resources listed in the response. The expression is in the form of `field:value` for checking if a repeated field contains a value.

Example: `events:organizations%2F{organization_id}%2Flocations%2Fglobal%2ForganizationEvents%2Fevent-id`

To get your `{organization_id}`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

Multiple filter queries are separated by spaces.

By default, each expression is an AND expression. However, you can include AND and OR expressions explicitly. Filter is supported for the following fields: `events`. 




**Returns**

  * (::String) — Optional. A filter expression that filters resources listed in the response. The expression is in the form of `field:value` for checking if a repeated field contains a value.

Example: `events:organizations%2F{organization_id}%2Flocations%2Fglobal%2ForganizationEvents%2Fevent-id`

To get your `{organization_id}`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

Multiple filter queries are separated by spaces.

By default, each expression is an AND expression. However, you can include AND and OR expressions explicitly. Filter is supported for the following fields: `events`. 




### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of events that should be returned. Acceptable values are `1` to `100`, inclusive. The default value is `10`.

If more results are available, the service returns a `next_page_token` that can be used to get the next page of results in subsequent list requests. The service may return fewer [impacts](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts#OrganizationImpact) than the requested `page_size`. 




### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of events that should be returned. Acceptable values are `1` to `100`, inclusive. The default value is `10`.

If more results are available, the service returns a `next_page_token` that can be used to get the next page of results in subsequent list requests. The service may return fewer [impacts](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts#OrganizationImpact) than the requested `page_size`. 




**Returns**

  * (::Integer) — Optional. The maximum number of events that should be returned. Acceptable values are `1` to `100`, inclusive. The default value is `10`.

If more results are available, the service returns a `next_page_token` that can be used to get the next page of results in subsequent list requests. The service may return fewer [impacts](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts#OrganizationImpact) than the requested `page_size`. 




### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A token identifying a page of results the server should return.

Provide `page_token` returned by a previous `ListOrganizationImpacts` call to retrieve the next page of results.

When paginating, all other parameters provided to `ListOrganizationImpacts` must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A token identifying a page of results the server should return.

Provide `page_token` returned by a previous `ListOrganizationImpacts` call to retrieve the next page of results.

When paginating, all other parameters provided to `ListOrganizationImpacts` must match the call that provided the page token. 




**Returns**

  * (::String) — Optional. A token identifying a page of results the server should return.

Provide `page_token` returned by a previous `ListOrganizationImpacts` call to retrieve the next page of results.

When paginating, all other parameters provided to `ListOrganizationImpacts` must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Parent value using the form `organizations/{organization_id}/locations/{location}/organizationImpacts`.

`organization_id` \- ID (number) of the project that contains the event. To get your `organization_id`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). 




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Parent value using the form `organizations/{organization_id}/locations/{location}/organizationImpacts`.

`organization_id` \- ID (number) of the project that contains the event. To get your `organization_id`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). 




**Returns**

  * (::String) — Required. Parent value using the form `organizations/{organization_id}/locations/{location}/organizationImpacts`.

`organization_id` \- ID (number) of the project that contains the event. To get your `organization_id`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
