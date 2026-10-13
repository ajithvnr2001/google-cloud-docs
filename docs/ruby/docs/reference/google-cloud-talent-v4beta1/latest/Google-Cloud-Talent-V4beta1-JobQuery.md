---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobQuery/
title: Cloud Talent Solution V4beta1 API - Class Google::Cloud::Talent::V4beta1::JobQuery (v0.19.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:02.487769+00:00
---

# Cloud Talent Solution V4beta1 API - Class Google::Cloud::Talent::V4beta1::JobQuery (v0.19.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Talent Solution V4beta1 API - Class Google::Cloud::Talent::V4beta1::JobQuery (v0.19.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.1 (latest)  0.19.0  0.18.1  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.0  0.4.6 

Reference documentation and code samples for the Cloud Talent Solution V4beta1 API class Google::Cloud::Talent::V4beta1::JobQuery.

The query required to perform a search query.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #commute_filter
    
    
    def commute_filter() -> ::Google::Cloud::Talent::V4beta1::CommuteFilter

**Returns**

  * ([::Google::Cloud::Talent::V4beta1::CommuteFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CommuteFilter)) — Allows filtering jobs by commute time with different travel methods (for example, driving or public transit).

Note: This only works when you specify a [CommuteMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CommuteMethod "Google::Cloud::Talent::V4beta1::CommuteMethod \(module\)"). In this case, [location_filters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobQuery#Google__Cloud__Talent__V4beta1__JobQuery_location_filters_instance_ "Google::Cloud::Talent::V4beta1::JobQuery#location_filters \(method\)") is ignored.

Currently we don't support sorting by commute time. 




### #commute_filter=
    
    
    def commute_filter=(value) -> ::Google::Cloud::Talent::V4beta1::CommuteFilter

**Parameter**

  * **value** ([::Google::Cloud::Talent::V4beta1::CommuteFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CommuteFilter)) — Allows filtering jobs by commute time with different travel methods (for example, driving or public transit).

Note: This only works when you specify a [CommuteMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CommuteMethod "Google::Cloud::Talent::V4beta1::CommuteMethod \(module\)"). In this case, [location_filters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobQuery#Google__Cloud__Talent__V4beta1__JobQuery_location_filters_instance_ "Google::Cloud::Talent::V4beta1::JobQuery#location_filters \(method\)") is ignored.

Currently we don't support sorting by commute time. 




**Returns**

  * ([::Google::Cloud::Talent::V4beta1::CommuteFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CommuteFilter)) — Allows filtering jobs by commute time with different travel methods (for example, driving or public transit).

Note: This only works when you specify a [CommuteMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CommuteMethod "Google::Cloud::Talent::V4beta1::CommuteMethod \(module\)"). In this case, [location_filters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobQuery#Google__Cloud__Talent__V4beta1__JobQuery_location_filters_instance_ "Google::Cloud::Talent::V4beta1::JobQuery#location_filters \(method\)") is ignored.

Currently we don't support sorting by commute time. 




### #companies
    
    
    def companies() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — This filter specifies the company entities to search against.

If a value isn't specified, jobs are searched for against all companies.

If multiple values are specified, jobs are searched against the companies specified.

The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}". For example, "projects/foo/tenants/bar/companies/baz".

If tenant id is unspecified, the default tenant is used. For example, "projects/foo/companies/bar".

At most 20 company filters are allowed. 




### #companies=
    
    
    def companies=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — This filter specifies the company entities to search against.

If a value isn't specified, jobs are searched for against all companies.

If multiple values are specified, jobs are searched against the companies specified.

The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}". For example, "projects/foo/tenants/bar/companies/baz".

If tenant id is unspecified, the default tenant is used. For example, "projects/foo/companies/bar".

At most 20 company filters are allowed. 




**Returns**

  * (::Array<::String>) — This filter specifies the company entities to search against.

If a value isn't specified, jobs are searched for against all companies.

If multiple values are specified, jobs are searched against the companies specified.

The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}". For example, "projects/foo/tenants/bar/companies/baz".

If tenant id is unspecified, the default tenant is used. For example, "projects/foo/companies/bar".

At most 20 company filters are allowed. 




### #company_display_names
    
    
    def company_display_names() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — This filter specifies the company [Company.display_name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Company#Google__Cloud__Talent__V4beta1__Company_display_name_instance_ "Google::Cloud::Talent::V4beta1::Company#display_name \(method\)") of the jobs to search against. The company name must match the value exactly.

Alternatively, the value being searched for can be wrapped in different match operators. `SUBSTRING_MATCH([value])` The company name must contain a case insensitive substring match of the value. Using this function may increase latency.

Sample Value: `SUBSTRING_MATCH(google)`

`MULTI_WORD_TOKEN_MATCH([value])` The value will be treated as a multi word token and the company name must contain a case insensitive match of the value. Using this function may increase latency.

Sample Value: `MULTI_WORD_TOKEN_MATCH(google)`

If a value isn't specified, jobs within the search results are associated with any company.

If multiple values are specified, jobs within the search results may be associated with any of the specified companies.

At most 20 company display name filters are allowed. 




### #company_display_names=
    
    
    def company_display_names=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — This filter specifies the company [Company.display_name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Company#Google__Cloud__Talent__V4beta1__Company_display_name_instance_ "Google::Cloud::Talent::V4beta1::Company#display_name \(method\)") of the jobs to search against. The company name must match the value exactly.

Alternatively, the value being searched for can be wrapped in different match operators. `SUBSTRING_MATCH([value])` The company name must contain a case insensitive substring match of the value. Using this function may increase latency.

Sample Value: `SUBSTRING_MATCH(google)`

`MULTI_WORD_TOKEN_MATCH([value])` The value will be treated as a multi word token and the company name must contain a case insensitive match of the value. Using this function may increase latency.

Sample Value: `MULTI_WORD_TOKEN_MATCH(google)`

If a value isn't specified, jobs within the search results are associated with any company.

If multiple values are specified, jobs within the search results may be associated with any of the specified companies.

At most 20 company display name filters are allowed. 




**Returns**

  * (::Array<::String>) — This filter specifies the company [Company.display_name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Company#Google__Cloud__Talent__V4beta1__Company_display_name_instance_ "Google::Cloud::Talent::V4beta1::Company#display_name \(method\)") of the jobs to search against. The company name must match the value exactly.

Alternatively, the value being searched for can be wrapped in different match operators. `SUBSTRING_MATCH([value])` The company name must contain a case insensitive substring match of the value. Using this function may increase latency.

Sample Value: `SUBSTRING_MATCH(google)`

`MULTI_WORD_TOKEN_MATCH([value])` The value will be treated as a multi word token and the company name must contain a case insensitive match of the value. Using this function may increase latency.

Sample Value: `MULTI_WORD_TOKEN_MATCH(google)`

If a value isn't specified, jobs within the search results are associated with any company.

If multiple values are specified, jobs within the search results may be associated with any of the specified companies.

At most 20 company display name filters are allowed. 




### #compensation_filter
    
    
    def compensation_filter() -> ::Google::Cloud::Talent::V4beta1::CompensationFilter

**Returns**

  * ([::Google::Cloud::Talent::V4beta1::CompensationFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CompensationFilter)) — This search filter is applied only to [Job.compensation_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_compensation_info_instance_ "Google::Cloud::Talent::V4beta1::Job#compensation_info \(method\)"). For example, if the filter is specified as "Hourly job with per-hour compensation > $15", only jobs meeting these criteria are searched. If a filter isn't defined, all open jobs are searched. 



### #compensation_filter=
    
    
    def compensation_filter=(value) -> ::Google::Cloud::Talent::V4beta1::CompensationFilter

**Parameter**

  * **value** ([::Google::Cloud::Talent::V4beta1::CompensationFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CompensationFilter)) — This search filter is applied only to [Job.compensation_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_compensation_info_instance_ "Google::Cloud::Talent::V4beta1::Job#compensation_info \(method\)"). For example, if the filter is specified as "Hourly job with per-hour compensation > $15", only jobs meeting these criteria are searched. If a filter isn't defined, all open jobs are searched. 



**Returns**

  * ([::Google::Cloud::Talent::V4beta1::CompensationFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CompensationFilter)) — This search filter is applied only to [Job.compensation_info](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_compensation_info_instance_ "Google::Cloud::Talent::V4beta1::Job#compensation_info \(method\)"). For example, if the filter is specified as "Hourly job with per-hour compensation > $15", only jobs meeting these criteria are searched. If a filter isn't defined, all open jobs are searched. 



### #custom_attribute_filter
    
    
    def custom_attribute_filter() -> ::String

**Returns**

  * (::String) — This filter specifies a structured syntax to match against the [Job.custom_attributes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_custom_attributes_instance_ "Google::Cloud::Talent::V4beta1::Job#custom_attributes \(method\)") marked as `filterable`.

The syntax for this expression is a subset of SQL syntax.

Supported operators are: `=`, `!=`, `<`, `<=`, `>`, and `>=` where the left of the operator is a custom field key and the right of the operator is a number or a quoted string. You must escape backslash (\\) and quote (\") characters.

Supported functions are `LOWER([field_name])` to perform a case insensitive match and `EMPTY([field_name])` to filter on the existence of a key.

Boolean expressions (AND/OR/NOT) are supported up to 3 levels of nesting (for example, "((A AND B AND C) OR NOT D) AND E"), a maximum of 100 comparisons or functions are allowed in the expression. The expression must be < 10000 bytes in length.

Sample Query: `(LOWER(driving_license)="class \"a\"" OR EMPTY(driving_license)) AND driving_years > 10`




### #custom_attribute_filter=
    
    
    def custom_attribute_filter=(value) -> ::String

**Parameter**

  * **value** (::String) — This filter specifies a structured syntax to match against the [Job.custom_attributes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_custom_attributes_instance_ "Google::Cloud::Talent::V4beta1::Job#custom_attributes \(method\)") marked as `filterable`.

The syntax for this expression is a subset of SQL syntax.

Supported operators are: `=`, `!=`, `<`, `<=`, `>`, and `>=` where the left of the operator is a custom field key and the right of the operator is a number or a quoted string. You must escape backslash (\\) and quote (\") characters.

Supported functions are `LOWER([field_name])` to perform a case insensitive match and `EMPTY([field_name])` to filter on the existence of a key.

Boolean expressions (AND/OR/NOT) are supported up to 3 levels of nesting (for example, "((A AND B AND C) OR NOT D) AND E"), a maximum of 100 comparisons or functions are allowed in the expression. The expression must be < 10000 bytes in length.

Sample Query: `(LOWER(driving_license)="class \"a\"" OR EMPTY(driving_license)) AND driving_years > 10`




**Returns**

  * (::String) — This filter specifies a structured syntax to match against the [Job.custom_attributes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_custom_attributes_instance_ "Google::Cloud::Talent::V4beta1::Job#custom_attributes \(method\)") marked as `filterable`.

The syntax for this expression is a subset of SQL syntax.

Supported operators are: `=`, `!=`, `<`, `<=`, `>`, and `>=` where the left of the operator is a custom field key and the right of the operator is a number or a quoted string. You must escape backslash (\\) and quote (\") characters.

Supported functions are `LOWER([field_name])` to perform a case insensitive match and `EMPTY([field_name])` to filter on the existence of a key.

Boolean expressions (AND/OR/NOT) are supported up to 3 levels of nesting (for example, "((A AND B AND C) OR NOT D) AND E"), a maximum of 100 comparisons or functions are allowed in the expression. The expression must be < 10000 bytes in length.

Sample Query: `(LOWER(driving_license)="class \"a\"" OR EMPTY(driving_license)) AND driving_years > 10`




### #disable_spell_check
    
    
    def disable_spell_check() -> ::Boolean

**Returns**

  * (::Boolean) — This flag controls the spell-check feature. If false, the service attempts to correct a misspelled query, for example, "enginee" is corrected to "engineer".

Defaults to false: a spell check is performed. 




### #disable_spell_check=
    
    
    def disable_spell_check=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — This flag controls the spell-check feature. If false, the service attempts to correct a misspelled query, for example, "enginee" is corrected to "engineer".

Defaults to false: a spell check is performed. 




**Returns**

  * (::Boolean) — This flag controls the spell-check feature. If false, the service attempts to correct a misspelled query, for example, "enginee" is corrected to "engineer".

Defaults to false: a spell check is performed. 




### #employment_types
    
    
    def employment_types() -> ::Array<::Google::Cloud::Talent::V4beta1::EmploymentType>

**Returns**

  * (::Array<[::Google::Cloud::Talent::V4beta1::EmploymentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-EmploymentType)>) — The employment type filter specifies the employment type of jobs to search against, such as [EmploymentType.FULL_TIME](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-EmploymentType#Google__Cloud__Talent__V4beta1__EmploymentType__FULL_TIME "Google::Cloud::Talent::V4beta1::EmploymentType::FULL_TIME \(constant\)").

If a value isn't specified, jobs in the search results includes any employment type.

If multiple values are specified, jobs in the search results include any of the specified employment types. 




### #employment_types=
    
    
    def employment_types=(value) -> ::Array<::Google::Cloud::Talent::V4beta1::EmploymentType>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Talent::V4beta1::EmploymentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-EmploymentType)>) — The employment type filter specifies the employment type of jobs to search against, such as [EmploymentType.FULL_TIME](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-EmploymentType#Google__Cloud__Talent__V4beta1__EmploymentType__FULL_TIME "Google::Cloud::Talent::V4beta1::EmploymentType::FULL_TIME \(constant\)").

If a value isn't specified, jobs in the search results includes any employment type.

If multiple values are specified, jobs in the search results include any of the specified employment types. 




**Returns**

  * (::Array<[::Google::Cloud::Talent::V4beta1::EmploymentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-EmploymentType)>) — The employment type filter specifies the employment type of jobs to search against, such as [EmploymentType.FULL_TIME](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-EmploymentType#Google__Cloud__Talent__V4beta1__EmploymentType__FULL_TIME "Google::Cloud::Talent::V4beta1::EmploymentType::FULL_TIME \(constant\)").

If a value isn't specified, jobs in the search results includes any employment type.

If multiple values are specified, jobs in the search results include any of the specified employment types. 




### #excluded_jobs
    
    
    def excluded_jobs() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — This filter specifies a list of job names to be excluded during search.

At most 400 excluded job names are allowed. 




### #excluded_jobs=
    
    
    def excluded_jobs=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — This filter specifies a list of job names to be excluded during search.

At most 400 excluded job names are allowed. 




**Returns**

  * (::Array<::String>) — This filter specifies a list of job names to be excluded during search.

At most 400 excluded job names are allowed. 




### #job_categories
    
    
    def job_categories() -> ::Array<::Google::Cloud::Talent::V4beta1::JobCategory>

**Returns**

  * (::Array<[::Google::Cloud::Talent::V4beta1::JobCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobCategory)>) — The category filter specifies the categories of jobs to search against. See [JobCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobCategory "Google::Cloud::Talent::V4beta1::JobCategory \(module\)") for more information.

If a value isn't specified, jobs from any category are searched against.

If multiple values are specified, jobs from any of the specified categories are searched against. 




### #job_categories=
    
    
    def job_categories=(value) -> ::Array<::Google::Cloud::Talent::V4beta1::JobCategory>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Talent::V4beta1::JobCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobCategory)>) — The category filter specifies the categories of jobs to search against. See [JobCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobCategory "Google::Cloud::Talent::V4beta1::JobCategory \(module\)") for more information.

If a value isn't specified, jobs from any category are searched against.

If multiple values are specified, jobs from any of the specified categories are searched against. 




**Returns**

  * (::Array<[::Google::Cloud::Talent::V4beta1::JobCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobCategory)>) — The category filter specifies the categories of jobs to search against. See [JobCategory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobCategory "Google::Cloud::Talent::V4beta1::JobCategory \(module\)") for more information.

If a value isn't specified, jobs from any category are searched against.

If multiple values are specified, jobs from any of the specified categories are searched against. 




### #language_codes
    
    
    def language_codes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — This filter specifies the locale of jobs to search against, for example, "en-US".

If a value isn't specified, the search results can contain jobs in any locale.

Language codes should be in BCP-47 format, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47).

At most 10 language code filters are allowed. 




### #language_codes=
    
    
    def language_codes=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — This filter specifies the locale of jobs to search against, for example, "en-US".

If a value isn't specified, the search results can contain jobs in any locale.

Language codes should be in BCP-47 format, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47).

At most 10 language code filters are allowed. 




**Returns**

  * (::Array<::String>) — This filter specifies the locale of jobs to search against, for example, "en-US".

If a value isn't specified, the search results can contain jobs in any locale.

Language codes should be in BCP-47 format, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47).

At most 10 language code filters are allowed. 




### #location_filters
    
    
    def location_filters() -> ::Array<::Google::Cloud::Talent::V4beta1::LocationFilter>

**Returns**

  * (::Array<[::Google::Cloud::Talent::V4beta1::LocationFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-LocationFilter)>) — The location filter specifies geo-regions containing the jobs to search against. See [LocationFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-LocationFilter "Google::Cloud::Talent::V4beta1::LocationFilter \(class\)") for more information.

If a location value isn't specified, jobs fitting the other search criteria are retrieved regardless of where they're located.

If multiple values are specified, jobs are retrieved from any of the specified locations. If different values are specified for the [LocationFilter.distance_in_miles](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-LocationFilter#Google__Cloud__Talent__V4beta1__LocationFilter_distance_in_miles_instance_ "Google::Cloud::Talent::V4beta1::LocationFilter#distance_in_miles \(method\)") parameter, the maximum provided distance is used for all locations.

At most 5 location filters are allowed. 




### #location_filters=
    
    
    def location_filters=(value) -> ::Array<::Google::Cloud::Talent::V4beta1::LocationFilter>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Talent::V4beta1::LocationFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-LocationFilter)>) — The location filter specifies geo-regions containing the jobs to search against. See [LocationFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-LocationFilter "Google::Cloud::Talent::V4beta1::LocationFilter \(class\)") for more information.

If a location value isn't specified, jobs fitting the other search criteria are retrieved regardless of where they're located.

If multiple values are specified, jobs are retrieved from any of the specified locations. If different values are specified for the [LocationFilter.distance_in_miles](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-LocationFilter#Google__Cloud__Talent__V4beta1__LocationFilter_distance_in_miles_instance_ "Google::Cloud::Talent::V4beta1::LocationFilter#distance_in_miles \(method\)") parameter, the maximum provided distance is used for all locations.

At most 5 location filters are allowed. 




**Returns**

  * (::Array<[::Google::Cloud::Talent::V4beta1::LocationFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-LocationFilter)>) — The location filter specifies geo-regions containing the jobs to search against. See [LocationFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-LocationFilter "Google::Cloud::Talent::V4beta1::LocationFilter \(class\)") for more information.

If a location value isn't specified, jobs fitting the other search criteria are retrieved regardless of where they're located.

If multiple values are specified, jobs are retrieved from any of the specified locations. If different values are specified for the [LocationFilter.distance_in_miles](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-LocationFilter#Google__Cloud__Talent__V4beta1__LocationFilter_distance_in_miles_instance_ "Google::Cloud::Talent::V4beta1::LocationFilter#distance_in_miles \(method\)") parameter, the maximum provided distance is used for all locations.

At most 5 location filters are allowed. 




### #publish_time_range
    
    
    def publish_time_range() -> ::Google::Cloud::Talent::V4beta1::TimestampRange

**Returns**

  * ([::Google::Cloud::Talent::V4beta1::TimestampRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-TimestampRange)) — Jobs published within a range specified by this filter are searched against. 



### #publish_time_range=
    
    
    def publish_time_range=(value) -> ::Google::Cloud::Talent::V4beta1::TimestampRange

**Parameter**

  * **value** ([::Google::Cloud::Talent::V4beta1::TimestampRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-TimestampRange)) — Jobs published within a range specified by this filter are searched against. 



**Returns**

  * ([::Google::Cloud::Talent::V4beta1::TimestampRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-TimestampRange)) — Jobs published within a range specified by this filter are searched against. 



### #query
    
    
    def query() -> ::String

**Returns**

  * (::String) — The query string that matches against the job title, description, and location fields.

The maximum number of allowed characters is 255. 




### #query=
    
    
    def query=(value) -> ::String

**Parameter**

  * **value** (::String) — The query string that matches against the job title, description, and location fields.

The maximum number of allowed characters is 255. 




**Returns**

  * (::String) — The query string that matches against the job title, description, and location fields.

The maximum number of allowed characters is 255. 




### #query_language_code
    
    
    def query_language_code() -> ::String

**Returns**

  * (::String) — The language code of [query](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobQuery#Google__Cloud__Talent__V4beta1__JobQuery_query_instance_ "Google::Cloud::Talent::V4beta1::JobQuery#query \(method\)"). For example, "en-US". This field helps to better interpret the query.

If a value isn't specified, the query language code is automatically detected, which may not be accurate.

Language code should be in BCP-47 format, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47). 




### #query_language_code=
    
    
    def query_language_code=(value) -> ::String

**Parameter**

  * **value** (::String) — The language code of [query](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobQuery#Google__Cloud__Talent__V4beta1__JobQuery_query_instance_ "Google::Cloud::Talent::V4beta1::JobQuery#query \(method\)"). For example, "en-US". This field helps to better interpret the query.

If a value isn't specified, the query language code is automatically detected, which may not be accurate.

Language code should be in BCP-47 format, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47). 




**Returns**

  * (::String) — The language code of [query](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-JobQuery#Google__Cloud__Talent__V4beta1__JobQuery_query_instance_ "Google::Cloud::Talent::V4beta1::JobQuery#query \(method\)"). For example, "en-US". This field helps to better interpret the query.

If a value isn't specified, the query language code is automatically detected, which may not be accurate.

Language code should be in BCP-47 format, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
