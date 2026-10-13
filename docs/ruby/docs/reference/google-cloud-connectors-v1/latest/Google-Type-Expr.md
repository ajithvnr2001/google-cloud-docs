---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Type-Expr/
title: Connectors V1 API - Class Google::Type::Expr (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:34.522225+00:00
---

# Connectors V1 API - Class Google::Type::Expr (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Type-Expr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Connectors V1 API - Class Google::Type::Expr (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Connectors V1 API class Google::Type::Expr.

Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at <https://github.com/google/cel-spec>.

Example (Comparison):
    
    
    title: "Summary size limit"
    description: "Determines if a summary is less than 100 chars"
    expression: "document.summary.size() < 100"
    

Example (Equality):
    
    
    title: "Requestor is owner"
    description: "Determines if requestor is the document owner"
    expression: "document.owner == request.auth.claims.email"
    

Example (Logic):
    
    
    title: "Public documents"
    description: "Determine whether the document should be publicly visible"
    expression: "document.type != 'private' && document.type != 'internal'"
    

Example (Data Manipulation):
    
    
    title: "Notification string"
    description: "Create a notification string with a timestamp."
    expression: "'New message received at ' + string(document.create_time)"
    

The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. 



**Returns**

  * (::String) — Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. 



### #expression
    
    
    def expression() -> ::String

**Returns**

  * (::String) — Textual representation of an expression in Common Expression Language syntax. 



### #expression=
    
    
    def expression=(value) -> ::String

**Parameter**

  * **value** (::String) — Textual representation of an expression in Common Expression Language syntax. 



**Returns**

  * (::String) — Textual representation of an expression in Common Expression Language syntax. 



### #location
    
    
    def location() -> ::String

**Returns**

  * (::String) — Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. 



### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. 



**Returns**

  * (::String) — Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. 



### #title
    
    
    def title() -> ::String

**Returns**

  * (::String) — Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. 



### #title=
    
    
    def title=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. 



**Returns**

  * (::String) — Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
