---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentsRequest/
title: Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::ListDeploymentsRequest (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:33.237533+00:00
---

# Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::ListDeploymentsRequest (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::ListDeploymentsRequest (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.1  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1  1.3.0  1.2.1  1.1.0  1.0.2  0.6.0  0.5.0  0.4.0  0.3.1  0.2.1  0.1.0 

Reference documentation and code samples for the Infrastructure Manager V1 API class Google::Cloud::ConfigService::V1::ListDeploymentsRequest.

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

  * (::String) — 

Lists the Deployments that match the filter expression. A filter expression filters the resources listed in the response. The expression must be of the form '{field} {operator} {value}' where operators: '<', '>', '<=', '>=', '!=', '=', ':' are supported (colon ':' represents a HAS operator which is roughly synonymous with equality). {field} can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.

Examples:

    * Filter by name: name = "projects/foo/locations/us-central1/deployments/bar

    * Filter by labels:

      * Resources that have a key called 'foo' labels.foo:*
      * Resources that have a key called 'foo' whose value is 'bar' labels.foo = bar
    * Filter by state:

      * Deployments in CREATING state. state=CREATING



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Lists the Deployments that match the filter expression. A filter expression filters the resources listed in the response. The expression must be of the form '{field} {operator} {value}' where operators: '<', '>', '<=', '>=', '!=', '=', ':' are supported (colon ':' represents a HAS operator which is roughly synonymous with equality). {field} can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.

Examples:

    * Filter by name: name = "projects/foo/locations/us-central1/deployments/bar

    * Filter by labels:

      * Resources that have a key called 'foo' labels.foo:*
      * Resources that have a key called 'foo' whose value is 'bar' labels.foo = bar
    * Filter by state:

      * Deployments in CREATING state. state=CREATING



**Returns**

  * (::String) — 

Lists the Deployments that match the filter expression. A filter expression filters the resources listed in the response. The expression must be of the form '{field} {operator} {value}' where operators: '<', '>', '<=', '>=', '!=', '=', ':' are supported (colon ':' represents a HAS operator which is roughly synonymous with equality). {field} can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.

Examples:

    * Filter by name: name = "projects/foo/locations/us-central1/deployments/bar

    * Filter by labels:

      * Resources that have a key called 'foo' labels.foo:*
      * Resources that have a key called 'foo' whose value is 'bar' labels.foo = bar
    * Filter by state:

      * Deployments in CREATING state. state=CREATING



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Field to use to sort the list. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Field to use to sort the list. 



**Returns**

  * (::String) — Field to use to sort the list. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — When requesting a page of resources, 'page_size' specifies number of resources to return. If unspecified, at most 500 will be returned. The maximum value is 1000. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — When requesting a page of resources, 'page_size' specifies number of resources to return. If unspecified, at most 500 will be returned. The maximum value is 1000. 



**Returns**

  * (::Integer) — When requesting a page of resources, 'page_size' specifies number of resources to return. If unspecified, at most 500 will be returned. The maximum value is 1000. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Token returned by previous call to 'ListDeployments' which specifies the position in the list from where to continue listing the resources. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Token returned by previous call to 'ListDeployments' which specifies the position in the list from where to continue listing the resources. 



**Returns**

  * (::String) — Token returned by previous call to 'ListDeployments' which specifies the position in the list from where to continue listing the resources. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent in whose context the Deployments are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}'. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent in whose context the Deployments are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}'. 



**Returns**

  * (::String) — Required. The parent in whose context the Deployments are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}'. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
