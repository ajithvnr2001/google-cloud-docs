---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListReportingDataAnnotationsRequest
title: Google Analytics Admin V1alpha Client - Class ListReportingDataAnnotationsRequest (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:21.014157+00:00
---

# Google Analytics Admin V1alpha Client - Class ListReportingDataAnnotationsRequest (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListReportingDataAnnotationsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class ListReportingDataAnnotationsRequest (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class ListReportingDataAnnotationsRequest.

Request message for ListReportingDataAnnotation RPC.

Generated from protobuf message `google.analytics.admin.v1alpha.ListReportingDataAnnotationsRequest`

## Namespace

Google \ Analytics \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. Resource name of the property. Format: properties/property_id Example: properties/123  
`↳ filter` |  `string`   
Optional. Filter that restricts which reporting data annotations under the parent property are listed. Supported fields are: * * 'name' * * `title` * * `description` * * `annotation_date` * * `annotation_date_range` * * `color` Additionally, this API provides the following helper functions: * * annotation_duration() : the duration that this annotation marks, [durations](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/duration.proto). expect a numeric representation of seconds followed by an `s` suffix. * * is_annotation_in_range(start_date, end_date) : if the annotation is in the range specified by the `start_date` and `end_date`. The dates are in ISO-8601 format, for example `2031-06-28`. Supported operations: * * `=` : equals * * `!=` : not equals * * `<` : less than * * `>` : greater than * * `<=` : less than or equals * * `>=` : greater than or equals * * `:` : has operator * * `=~` : [regular expression](https://github.com/google/re2/wiki/Syntax) match * * `!~` : [regular expression](https://github.com/google/re2/wiki/Syntax) does not match * * `NOT` : Logical not * * `AND` : Logical and * * `OR` : Logical or Examples: 1. `title="Holiday Sale"` 2\. `description=~"[Bb]ig [Gg]ame.*[Ss]ale"` 3\. `is_annotation_in_range("2025-12-25", "2026-01-16") = true` 4\. `annotation_duration() >= 172800s AND title:BOGO`  
`↳ page_size` |  `int`   
Optional. The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)  
`↳ page_token` |  `string`   
Optional. A page token, received from a previous `ListReportingDataAnnotations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListReportingDataAnnotations` must match the call that provided the page token.  
  
### getParent

Required. Resource name of the property.

Format: properties/property_id Example: properties/123

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. Resource name of the property.

Format: properties/property_id Example: properties/123

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

Optional. Filter that restricts which reporting data annotations under the parent property are listed.

Supported fields are:

  * 'name'
  * `title`
  * `description`
  * `annotation_date`
  * `annotation_date_range`
  * `color` Additionally, this API provides the following helper functions:
  * annotation_duration() : the duration that this annotation marks, [durations](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/duration.proto). expect a numeric representation of seconds followed by an `s` suffix.
  * is_annotation_in_range(start_date, end_date) : if the annotation is in the range specified by the `start_date` and `end_date`. The dates are in ISO-8601 format, for example `2031-06-28`. Supported operations:
    * `=` : equals
    * `!=` : not equals
    * `<` : less than
    * `>` : greater than
    * `<=` : less than or equals
    * `>=` : greater than or equals
    * `:` : has operator
    * `=~` : [regular expression](https://github.com/google/re2/wiki/Syntax) match
    * `!~` : [regular expression](https://github.com/google/re2/wiki/Syntax) does not match
    * `NOT` : Logical not
    * `AND` : Logical and
    * `OR` : Logical or Examples:
  * `title="Holiday Sale"`
  * `description=~"[Bb]ig [Gg]ame.*[Ss]ale"`
  * `is_annotation_in_range("2025-12-25", "2026-01-16") = true`
  * `annotation_duration() >= 172800s AND title:BOGO`



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

Optional. Filter that restricts which reporting data annotations under the parent property are listed.

Supported fields are:

  * 'name'
  * `title`
  * `description`
  * `annotation_date`
  * `annotation_date_range`
  * `color` Additionally, this API provides the following helper functions:
  * annotation_duration() : the duration that this annotation marks, [durations](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/duration.proto). expect a numeric representation of seconds followed by an `s` suffix.
  * is_annotation_in_range(start_date, end_date) : if the annotation is in the range specified by the `start_date` and `end_date`. The dates are in ISO-8601 format, for example `2031-06-28`. Supported operations:
    * `=` : equals
    * `!=` : not equals
    * `<` : less than
    * `>` : greater than
    * `<=` : less than or equals
    * `>=` : greater than or equals
    * `:` : has operator
    * `=~` : [regular expression](https://github.com/google/re2/wiki/Syntax) match
    * `!~` : [regular expression](https://github.com/google/re2/wiki/Syntax) does not match
    * `NOT` : Logical not
    * `AND` : Logical and
    * `OR` : Logical or Examples:
  * `title="Holiday Sale"`
  * `description=~"[Bb]ig [Gg]ame.*[Ss]ale"`
  * `is_annotation_in_range("2025-12-25", "2026-01-16") = true`
  * `annotation_duration() >= 172800s AND title:BOGO`



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Optional. The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Optional. The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

Optional. A page token, received from a previous `ListReportingDataAnnotations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListReportingDataAnnotations` must match the call that provided the page token.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

Optional. A page token, received from a previous `ListReportingDataAnnotations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListReportingDataAnnotations` must match the call that provided the page token.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameter**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. Resource name of the property. Format: properties/property_id Example: properties/123 Please see AnalyticsAdminServiceClient::propertyName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListReportingDataAnnotationsRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ListReportingDataAnnotationsRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
