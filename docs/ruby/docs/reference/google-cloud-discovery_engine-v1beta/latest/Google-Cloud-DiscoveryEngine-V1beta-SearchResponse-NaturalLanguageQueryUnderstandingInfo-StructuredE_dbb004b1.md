---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-Expression/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::Expression (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:02.135747+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::Expression (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-Expression/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::Expression (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::Expression.

The expression denoting the filter that was extracted from the input query.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #and_expr
    
    
    def and_expr() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::AndExpression

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::AndExpression](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-AndExpression)) — Logical "And" compound operator connecting multiple expressions.

Note: The following fields are mutually exclusive: `and_expr`, `string_constraint`, `number_constraint`, `geolocation_constraint`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #and_expr=
    
    
    def and_expr=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::AndExpression

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::AndExpression](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-AndExpression)) — Logical "And" compound operator connecting multiple expressions.

Note: The following fields are mutually exclusive: `and_expr`, `string_constraint`, `number_constraint`, `geolocation_constraint`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::AndExpression](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-AndExpression)) — Logical "And" compound operator connecting multiple expressions.

Note: The following fields are mutually exclusive: `and_expr`, `string_constraint`, `number_constraint`, `geolocation_constraint`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #geolocation_constraint
    
    
    def geolocation_constraint() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::GeolocationConstraint

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::GeolocationConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-GeolocationConstraint)) — Geolocation constraint expression.

Note: The following fields are mutually exclusive: `geolocation_constraint`, `string_constraint`, `number_constraint`, `and_expr`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #geolocation_constraint=
    
    
    def geolocation_constraint=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::GeolocationConstraint

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::GeolocationConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-GeolocationConstraint)) — Geolocation constraint expression.

Note: The following fields are mutually exclusive: `geolocation_constraint`, `string_constraint`, `number_constraint`, `and_expr`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::GeolocationConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-GeolocationConstraint)) — Geolocation constraint expression.

Note: The following fields are mutually exclusive: `geolocation_constraint`, `string_constraint`, `number_constraint`, `and_expr`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #number_constraint
    
    
    def number_constraint() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::NumberConstraint

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::NumberConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-NumberConstraint)) — Numerical constraint expression.

Note: The following fields are mutually exclusive: `number_constraint`, `string_constraint`, `geolocation_constraint`, `and_expr`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #number_constraint=
    
    
    def number_constraint=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::NumberConstraint

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::NumberConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-NumberConstraint)) — Numerical constraint expression.

Note: The following fields are mutually exclusive: `number_constraint`, `string_constraint`, `geolocation_constraint`, `and_expr`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::NumberConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-NumberConstraint)) — Numerical constraint expression.

Note: The following fields are mutually exclusive: `number_constraint`, `string_constraint`, `geolocation_constraint`, `and_expr`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #or_expr
    
    
    def or_expr() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::OrExpression

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::OrExpression](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-OrExpression)) — Logical "Or" compound operator connecting multiple expressions.

Note: The following fields are mutually exclusive: `or_expr`, `string_constraint`, `number_constraint`, `geolocation_constraint`, `and_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #or_expr=
    
    
    def or_expr=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::OrExpression

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::OrExpression](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-OrExpression)) — Logical "Or" compound operator connecting multiple expressions.

Note: The following fields are mutually exclusive: `or_expr`, `string_constraint`, `number_constraint`, `geolocation_constraint`, `and_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::OrExpression](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-OrExpression)) — Logical "Or" compound operator connecting multiple expressions.

Note: The following fields are mutually exclusive: `or_expr`, `string_constraint`, `number_constraint`, `geolocation_constraint`, `and_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #string_constraint
    
    
    def string_constraint() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::StringConstraint

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::StringConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-StringConstraint)) — String constraint expression.

Note: The following fields are mutually exclusive: `string_constraint`, `number_constraint`, `geolocation_constraint`, `and_expr`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #string_constraint=
    
    
    def string_constraint=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::StringConstraint

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::StringConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-StringConstraint)) — String constraint expression.

Note: The following fields are mutually exclusive: `string_constraint`, `number_constraint`, `geolocation_constraint`, `and_expr`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo::StructuredExtractedFilter::StringConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo-StructuredExtractedFilter-StringConstraint)) — String constraint expression.

Note: The following fields are mutually exclusive: `string_constraint`, `number_constraint`, `geolocation_constraint`, `and_expr`, `or_expr`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
