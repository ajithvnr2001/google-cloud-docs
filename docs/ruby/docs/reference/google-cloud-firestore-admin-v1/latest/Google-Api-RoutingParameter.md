---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Api-RoutingParameter/
title: Cloud Firestore Admin V1 API - Class Google::Api::RoutingParameter (v1.14.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:35.361519+00:00
---

# Cloud Firestore Admin V1 API - Class Google::Api::RoutingParameter (v1.14.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Api-RoutingParameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Firestore Admin V1 API - Class Google::Api::RoutingParameter (v1.14.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.2 (latest)  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.18.0  0.17.1  0.16.0  0.15.0  0.14.3  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Cloud Firestore Admin V1 API class Google::Api::RoutingParameter.

A projection from an input message to the GRPC or REST header.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #field
    
    
    def field() -> ::String

**Returns**

  * (::String) — A request field to extract the header key-value pair from. 



### #field=
    
    
    def field=(value) -> ::String

**Parameter**

  * **value** (::String) — A request field to extract the header key-value pair from. 



**Returns**

  * (::String) — A request field to extract the header key-value pair from. 



### #path_template
    
    
    def path_template() -> ::String

**Returns**

  * (::String) — A pattern matching the key-value field. Optional. If not specified, the whole field specified in the `field` field will be taken as value, and its name used as key. If specified, it MUST contain exactly one named segment (along with any number of unnamed segments) The pattern will be matched over the field specified in the `field` field, then if the match is successful:

    * the name of the single named segment will be used as a header name,
    * the match value of the segment will be used as a header value; if the match is NOT successful, nothing will be sent.

Example:
    
    -- This is a field in the request message
             |   that the header value will be extracted from.
             |
             |                     -- This is the key name in the
             |                    |   routing header.
             V                    |
    field: "table_name"           v
    path_template: "projects/*/{table_location=instances/*}/tables/*"
                                               ^            ^
                                               |            |
      In the {} brackets is the pattern that --             |
      specifies what to extract from the                    |
      field as a value to be sent.                          |
                                                            |
     The string in the field must match the whole pattern --
     before brackets, inside brackets, after brackets.
    

When looking at this specific example, we can see that:

    * A key-value pair with the key `table_location` and the value matching `instances/*` should be added to the x-goog-request-params routing header.
    * The value is extracted from the request message's `table_name` field if it matches the full pattern specified: `projects/*/instances/*/tables/*`.

**NB:** If the `path_template` field is not provided, the key name is equal to the field name, and the whole field should be sent as a value. This makes the pattern for the field and the value functionally equivalent to `**`, and the configuration
    
    {
      field: "table_name"
    }
    

is a functionally equivalent shorthand to:
    
    {
      field: "table_name"
      path_template: "{table_name=**}"
    }
    

See Example 1 for more details. 




### #path_template=
    
    
    def path_template=(value) -> ::String

**Parameter**

  * **value** (::String) — A pattern matching the key-value field. Optional. If not specified, the whole field specified in the `field` field will be taken as value, and its name used as key. If specified, it MUST contain exactly one named segment (along with any number of unnamed segments) The pattern will be matched over the field specified in the `field` field, then if the match is successful:

    * the name of the single named segment will be used as a header name,
    * the match value of the segment will be used as a header value; if the match is NOT successful, nothing will be sent.

Example:
    
    -- This is a field in the request message
             |   that the header value will be extracted from.
             |
             |                     -- This is the key name in the
             |                    |   routing header.
             V                    |
    field: "table_name"           v
    path_template: "projects/*/{table_location=instances/*}/tables/*"
                                               ^            ^
                                               |            |
      In the {} brackets is the pattern that --             |
      specifies what to extract from the                    |
      field as a value to be sent.                          |
                                                            |
     The string in the field must match the whole pattern --
     before brackets, inside brackets, after brackets.
    

When looking at this specific example, we can see that:

    * A key-value pair with the key `table_location` and the value matching `instances/*` should be added to the x-goog-request-params routing header.
    * The value is extracted from the request message's `table_name` field if it matches the full pattern specified: `projects/*/instances/*/tables/*`.

**NB:** If the `path_template` field is not provided, the key name is equal to the field name, and the whole field should be sent as a value. This makes the pattern for the field and the value functionally equivalent to `**`, and the configuration
    
    {
      field: "table_name"
    }
    

is a functionally equivalent shorthand to:
    
    {
      field: "table_name"
      path_template: "{table_name=**}"
    }
    

See Example 1 for more details. 




**Returns**

  * (::String) — A pattern matching the key-value field. Optional. If not specified, the whole field specified in the `field` field will be taken as value, and its name used as key. If specified, it MUST contain exactly one named segment (along with any number of unnamed segments) The pattern will be matched over the field specified in the `field` field, then if the match is successful:

    * the name of the single named segment will be used as a header name,
    * the match value of the segment will be used as a header value; if the match is NOT successful, nothing will be sent.

Example:
    
    -- This is a field in the request message
             |   that the header value will be extracted from.
             |
             |                     -- This is the key name in the
             |                    |   routing header.
             V                    |
    field: "table_name"           v
    path_template: "projects/*/{table_location=instances/*}/tables/*"
                                               ^            ^
                                               |            |
      In the {} brackets is the pattern that --             |
      specifies what to extract from the                    |
      field as a value to be sent.                          |
                                                            |
     The string in the field must match the whole pattern --
     before brackets, inside brackets, after brackets.
    

When looking at this specific example, we can see that:

    * A key-value pair with the key `table_location` and the value matching `instances/*` should be added to the x-goog-request-params routing header.
    * The value is extracted from the request message's `table_name` field if it matches the full pattern specified: `projects/*/instances/*/tables/*`.

**NB:** If the `path_template` field is not provided, the key name is equal to the field name, and the whole field should be sent as a value. This makes the pattern for the field and the value functionally equivalent to `**`, and the configuration
    
    {
      field: "table_name"
    }
    

is a functionally equivalent shorthand to:
    
    {
      field: "table_name"
      path_template: "{table_name=**}"
    }
    

See Example 1 for more details. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
