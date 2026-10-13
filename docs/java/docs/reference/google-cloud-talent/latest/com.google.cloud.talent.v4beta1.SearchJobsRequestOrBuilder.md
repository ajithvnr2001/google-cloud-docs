---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.SearchJobsRequestOrBuilder
title: Interface SearchJobsRequestOrBuilder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:56.522707+00:00
---

# Interface SearchJobsRequestOrBuilder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.SearchJobsRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchJobsRequestOrBuilder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.6  2.2.9 
    
    
    public interface SearchJobsRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCustomRankingInfo()
    
    
    public abstract SearchJobsRequest.CustomRankingInfo getCustomRankingInfo()

Controls over how job documents get ranked on top of existing relevance score (determined by API algorithm).

` .google.cloud.talent.v4beta1.SearchJobsRequest.CustomRankingInfo custom_ranking_info = 14; `

**Returns**  
---  
**Type** | **Description**  
`[SearchJobsRequest.CustomRankingInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.SearchJobsRequest.CustomRankingInfo)` | The customRankingInfo.  
  
### getCustomRankingInfoOrBuilder()
    
    
    public abstract SearchJobsRequest.CustomRankingInfoOrBuilder getCustomRankingInfoOrBuilder()

Controls over how job documents get ranked on top of existing relevance score (determined by API algorithm).

` .google.cloud.talent.v4beta1.SearchJobsRequest.CustomRankingInfo custom_ranking_info = 14; `

**Returns**  
---  
**Type** | **Description**  
`[SearchJobsRequest.CustomRankingInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.SearchJobsRequest.CustomRankingInfoOrBuilder)` |   
  
### getDisableKeywordMatch()
    
    
    public abstract boolean getDisableKeywordMatch()

This field is deprecated. Please use SearchJobsRequest.keyword_match_mode going forward.

To migrate, disable_keyword_match set to false maps to KeywordMatchMode.KEYWORD_MATCH_ALL, and disable_keyword_match set to true maps to KeywordMatchMode.KEYWORD_MATCH_DISABLED. If SearchJobsRequest.keyword_match_mode is set, this field is ignored.

Controls whether to disable exact keyword match on Job.title, Job.description, Job.company_display_name, Job.addresses, Job.qualifications. When disable keyword match is turned off, a keyword match returns jobs that do not match given category filters when there are matching keywords. For example, for the query "program manager," a result is returned even if the job posting has the title "software developer," which doesn't fall into "program manager" ontology, but does have "program manager" appearing in its description.

For queries like "cloud" that don't contain title or location specific ontology, jobs with "cloud" keyword matches are returned regardless of this flag's value.

Use Company.keyword_searchable_job_custom_attributes if company-specific globally matched custom field/attribute string values are needed. Enabling keyword match improves recall of subsequent search requests.

Defaults to false.

`bool disable_keyword_match = 16;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disableKeywordMatch.  
  
### getDiversificationLevel()
    
    
    public abstract SearchJobsRequest.DiversificationLevel getDiversificationLevel()

Controls whether highly similar jobs are returned next to each other in the search results. Jobs are identified as highly similar based on their titles, job categories, and locations. Highly similar results are clustered so that only one representative job of the cluster is displayed to the job seeker higher up in the results, with the other jobs being displayed lower down in the results.

Defaults to DiversificationLevel.SIMPLE if no value is specified.

` .google.cloud.talent.v4beta1.SearchJobsRequest.DiversificationLevel diversification_level = 13; `

**Returns**  
---  
**Type** | **Description**  
`[SearchJobsRequest.DiversificationLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.SearchJobsRequest.DiversificationLevel)` | The diversificationLevel.  
  
### getDiversificationLevelValue()
    
    
    public abstract int getDiversificationLevelValue()

Controls whether highly similar jobs are returned next to each other in the search results. Jobs are identified as highly similar based on their titles, job categories, and locations. Highly similar results are clustered so that only one representative job of the cluster is displayed to the job seeker higher up in the results, with the other jobs being displayed lower down in the results.

Defaults to DiversificationLevel.SIMPLE if no value is specified.

` .google.cloud.talent.v4beta1.SearchJobsRequest.DiversificationLevel diversification_level = 13; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for diversificationLevel.  
  
### getEnableBroadening()
    
    
    public abstract boolean getEnableBroadening()

Controls whether to broaden the search when it produces sparse results. Broadened queries append results to the end of the matching results list.

Defaults to false.

`bool enable_broadening = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableBroadening.  
  
### getHistogramQueries(int index)
    
    
    public abstract HistogramQuery getHistogramQueries(int index)

An expression specifies a histogram request against matching jobs.

Expression syntax is an aggregation function call with histogram facets and other options.

Available aggregation function calls are:

  * `count(string_histogram_facet)`: Count the number of matching entities, for each distinct attribute value.
  * `count(numeric_histogram_facet, list of buckets)`: Count the number of matching entities within each bucket.

A maximum of 200 histogram buckets are supported.

Data types:

  * Histogram facet: facet names with format `a-zA-Z+`.

  * String: string like "any string with backslash escape for quote(\")."
  * Number: whole number and floating point number like 10, -1 and -0.01.
  * List: list of elements with comma(,) separator surrounded by square brackets, for example, [1, 2, 3] and ["one", "two", "three"].

Built-in constants:

  * MIN (minimum number similar to java Double.MIN_VALUE)

  * MAX (maximum number similar to java Double.MAX_VALUE)

Built-in functions:

  * bucket(start, end[, label]): bucket built-in function creates a bucket with range of start, end). Note that the end is exclusive, for example, bucket(1, MAX, "positive number") or bucket(1, 10).

Job histogram facets:

  * company_display_name: histogram by [Job.company_display_name.

  * employment_type: histogram by Job.employment_types, for example, "FULL_TIME", "PART_TIME".
  * company_size (DEPRECATED): histogram by CompanySize, for example, "SMALL", "MEDIUM", "BIG".
  * publish_time_in_day: histogram by the Job.posting_publish_time in days. Must specify list of numeric buckets in spec.
  * publish_time_in_month: histogram by the Job.posting_publish_time in months. Must specify list of numeric buckets in spec.
  * publish_time_in_year: histogram by the Job.posting_publish_time in years. Must specify list of numeric buckets in spec.
  * degree_types: histogram by the Job.degree_types, for example, "Bachelors", "Masters".
  * job_level: histogram by the Job.job_level, for example, "Entry Level".
  * country: histogram by the country code of jobs, for example, "US", "FR".
  * admin1: histogram by the admin1 code of jobs, which is a global placeholder referring to the state, province, or the particular term a country uses to define the geographic structure below the country level, for example, "CA", "IL".
  * city: histogram by a combination of the "city name, admin1 code". For example, "Mountain View, CA", "New York, NY".
  * admin1_country: histogram by a combination of the "admin1 code, country", for example, "CA, US", "IL, US".
  * city_coordinate: histogram by the city center's GPS coordinates (latitude and longitude), for example, 37.4038522,-122.0987765. Since the coordinates of a city center can change, customers may need to refresh them periodically.
  * locale: histogram by the Job.language_code, for example, "en-US", "fr-FR".
  * language: histogram by the language subtag of the Job.language_code, for example, "en", "fr".
  * category: histogram by the JobCategory, for example, "COMPUTER_AND_IT", "HEALTHCARE".
  * base_compensation_unit: histogram by the CompensationInfo.CompensationUnit of base salary, for example, "WEEKLY", "MONTHLY".
  * base_compensation: histogram by the base salary. Must specify list of numeric buckets to group results by.
  * annualized_base_compensation: histogram by the base annualized salary. Must specify list of numeric buckets to group results by.
  * annualized_total_compensation: histogram by the total annualized salary. Must specify list of numeric buckets to group results by.
  * string_custom_attribute: histogram by string Job.custom_attributes. Values can be accessed via square bracket notations like string_custom_attribute["key1"].
  * numeric_custom_attribute: histogram by numeric Job.custom_attributes. Values can be accessed via square bracket notations like numeric_custom_attribute["key1"]. Must specify list of numeric buckets to group results by.

Example expressions:

  * `count(admin1)`

  * `count(base_compensation, [bucket(1000, 10000), bucket(10000, 100000), bucket(100000, MAX)])`
  * `count(string_custom_attribute["some-string-custom-attribute"])`
  * `count(numeric_custom_attribute["some-numeric-custom-attribute"], [bucket(MIN, 0, "negative"), bucket(0, MAX, "non-negative")])`



`repeated .google.cloud.talent.v4beta1.HistogramQuery histogram_queries = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HistogramQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.HistogramQuery)` |   
  
### getHistogramQueriesCount()
    
    
    public abstract int getHistogramQueriesCount()

An expression specifies a histogram request against matching jobs.

Expression syntax is an aggregation function call with histogram facets and other options.

Available aggregation function calls are:

  * `count(string_histogram_facet)`: Count the number of matching entities, for each distinct attribute value.
  * `count(numeric_histogram_facet, list of buckets)`: Count the number of matching entities within each bucket.

A maximum of 200 histogram buckets are supported.

Data types:

  * Histogram facet: facet names with format `a-zA-Z+`.

  * String: string like "any string with backslash escape for quote(\")."
  * Number: whole number and floating point number like 10, -1 and -0.01.
  * List: list of elements with comma(,) separator surrounded by square brackets, for example, [1, 2, 3] and ["one", "two", "three"].

Built-in constants:

  * MIN (minimum number similar to java Double.MIN_VALUE)

  * MAX (maximum number similar to java Double.MAX_VALUE)

Built-in functions:

  * bucket(start, end[, label]): bucket built-in function creates a bucket with range of start, end). Note that the end is exclusive, for example, bucket(1, MAX, "positive number") or bucket(1, 10).

Job histogram facets:

  * company_display_name: histogram by [Job.company_display_name.

  * employment_type: histogram by Job.employment_types, for example, "FULL_TIME", "PART_TIME".
  * company_size (DEPRECATED): histogram by CompanySize, for example, "SMALL", "MEDIUM", "BIG".
  * publish_time_in_day: histogram by the Job.posting_publish_time in days. Must specify list of numeric buckets in spec.
  * publish_time_in_month: histogram by the Job.posting_publish_time in months. Must specify list of numeric buckets in spec.
  * publish_time_in_year: histogram by the Job.posting_publish_time in years. Must specify list of numeric buckets in spec.
  * degree_types: histogram by the Job.degree_types, for example, "Bachelors", "Masters".
  * job_level: histogram by the Job.job_level, for example, "Entry Level".
  * country: histogram by the country code of jobs, for example, "US", "FR".
  * admin1: histogram by the admin1 code of jobs, which is a global placeholder referring to the state, province, or the particular term a country uses to define the geographic structure below the country level, for example, "CA", "IL".
  * city: histogram by a combination of the "city name, admin1 code". For example, "Mountain View, CA", "New York, NY".
  * admin1_country: histogram by a combination of the "admin1 code, country", for example, "CA, US", "IL, US".
  * city_coordinate: histogram by the city center's GPS coordinates (latitude and longitude), for example, 37.4038522,-122.0987765. Since the coordinates of a city center can change, customers may need to refresh them periodically.
  * locale: histogram by the Job.language_code, for example, "en-US", "fr-FR".
  * language: histogram by the language subtag of the Job.language_code, for example, "en", "fr".
  * category: histogram by the JobCategory, for example, "COMPUTER_AND_IT", "HEALTHCARE".
  * base_compensation_unit: histogram by the CompensationInfo.CompensationUnit of base salary, for example, "WEEKLY", "MONTHLY".
  * base_compensation: histogram by the base salary. Must specify list of numeric buckets to group results by.
  * annualized_base_compensation: histogram by the base annualized salary. Must specify list of numeric buckets to group results by.
  * annualized_total_compensation: histogram by the total annualized salary. Must specify list of numeric buckets to group results by.
  * string_custom_attribute: histogram by string Job.custom_attributes. Values can be accessed via square bracket notations like string_custom_attribute["key1"].
  * numeric_custom_attribute: histogram by numeric Job.custom_attributes. Values can be accessed via square bracket notations like numeric_custom_attribute["key1"]. Must specify list of numeric buckets to group results by.

Example expressions:

  * `count(admin1)`

  * `count(base_compensation, [bucket(1000, 10000), bucket(10000, 100000), bucket(100000, MAX)])`
  * `count(string_custom_attribute["some-string-custom-attribute"])`
  * `count(numeric_custom_attribute["some-numeric-custom-attribute"], [bucket(MIN, 0, "negative"), bucket(0, MAX, "non-negative")])`



`repeated .google.cloud.talent.v4beta1.HistogramQuery histogram_queries = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHistogramQueriesList()
    
    
    public abstract List<HistogramQuery> getHistogramQueriesList()

An expression specifies a histogram request against matching jobs.

Expression syntax is an aggregation function call with histogram facets and other options.

Available aggregation function calls are:

  * `count(string_histogram_facet)`: Count the number of matching entities, for each distinct attribute value.
  * `count(numeric_histogram_facet, list of buckets)`: Count the number of matching entities within each bucket.

A maximum of 200 histogram buckets are supported.

Data types:

  * Histogram facet: facet names with format `a-zA-Z+`.

  * String: string like "any string with backslash escape for quote(\")."
  * Number: whole number and floating point number like 10, -1 and -0.01.
  * List: list of elements with comma(,) separator surrounded by square brackets, for example, [1, 2, 3] and ["one", "two", "three"].

Built-in constants:

  * MIN (minimum number similar to java Double.MIN_VALUE)

  * MAX (maximum number similar to java Double.MAX_VALUE)

Built-in functions:

  * bucket(start, end[, label]): bucket built-in function creates a bucket with range of start, end). Note that the end is exclusive, for example, bucket(1, MAX, "positive number") or bucket(1, 10).

Job histogram facets:

  * company_display_name: histogram by [Job.company_display_name.

  * employment_type: histogram by Job.employment_types, for example, "FULL_TIME", "PART_TIME".
  * company_size (DEPRECATED): histogram by CompanySize, for example, "SMALL", "MEDIUM", "BIG".
  * publish_time_in_day: histogram by the Job.posting_publish_time in days. Must specify list of numeric buckets in spec.
  * publish_time_in_month: histogram by the Job.posting_publish_time in months. Must specify list of numeric buckets in spec.
  * publish_time_in_year: histogram by the Job.posting_publish_time in years. Must specify list of numeric buckets in spec.
  * degree_types: histogram by the Job.degree_types, for example, "Bachelors", "Masters".
  * job_level: histogram by the Job.job_level, for example, "Entry Level".
  * country: histogram by the country code of jobs, for example, "US", "FR".
  * admin1: histogram by the admin1 code of jobs, which is a global placeholder referring to the state, province, or the particular term a country uses to define the geographic structure below the country level, for example, "CA", "IL".
  * city: histogram by a combination of the "city name, admin1 code". For example, "Mountain View, CA", "New York, NY".
  * admin1_country: histogram by a combination of the "admin1 code, country", for example, "CA, US", "IL, US".
  * city_coordinate: histogram by the city center's GPS coordinates (latitude and longitude), for example, 37.4038522,-122.0987765. Since the coordinates of a city center can change, customers may need to refresh them periodically.
  * locale: histogram by the Job.language_code, for example, "en-US", "fr-FR".
  * language: histogram by the language subtag of the Job.language_code, for example, "en", "fr".
  * category: histogram by the JobCategory, for example, "COMPUTER_AND_IT", "HEALTHCARE".
  * base_compensation_unit: histogram by the CompensationInfo.CompensationUnit of base salary, for example, "WEEKLY", "MONTHLY".
  * base_compensation: histogram by the base salary. Must specify list of numeric buckets to group results by.
  * annualized_base_compensation: histogram by the base annualized salary. Must specify list of numeric buckets to group results by.
  * annualized_total_compensation: histogram by the total annualized salary. Must specify list of numeric buckets to group results by.
  * string_custom_attribute: histogram by string Job.custom_attributes. Values can be accessed via square bracket notations like string_custom_attribute["key1"].
  * numeric_custom_attribute: histogram by numeric Job.custom_attributes. Values can be accessed via square bracket notations like numeric_custom_attribute["key1"]. Must specify list of numeric buckets to group results by.

Example expressions:

  * `count(admin1)`

  * `count(base_compensation, [bucket(1000, 10000), bucket(10000, 100000), bucket(100000, MAX)])`
  * `count(string_custom_attribute["some-string-custom-attribute"])`
  * `count(numeric_custom_attribute["some-numeric-custom-attribute"], [bucket(MIN, 0, "negative"), bucket(0, MAX, "non-negative")])`



`repeated .google.cloud.talent.v4beta1.HistogramQuery histogram_queries = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[HistogramQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.HistogramQuery)>` |   
  
### getHistogramQueriesOrBuilder(int index)
    
    
    public abstract HistogramQueryOrBuilder getHistogramQueriesOrBuilder(int index)

An expression specifies a histogram request against matching jobs.

Expression syntax is an aggregation function call with histogram facets and other options.

Available aggregation function calls are:

  * `count(string_histogram_facet)`: Count the number of matching entities, for each distinct attribute value.
  * `count(numeric_histogram_facet, list of buckets)`: Count the number of matching entities within each bucket.

A maximum of 200 histogram buckets are supported.

Data types:

  * Histogram facet: facet names with format `a-zA-Z+`.

  * String: string like "any string with backslash escape for quote(\")."
  * Number: whole number and floating point number like 10, -1 and -0.01.
  * List: list of elements with comma(,) separator surrounded by square brackets, for example, [1, 2, 3] and ["one", "two", "three"].

Built-in constants:

  * MIN (minimum number similar to java Double.MIN_VALUE)

  * MAX (maximum number similar to java Double.MAX_VALUE)

Built-in functions:

  * bucket(start, end[, label]): bucket built-in function creates a bucket with range of start, end). Note that the end is exclusive, for example, bucket(1, MAX, "positive number") or bucket(1, 10).

Job histogram facets:

  * company_display_name: histogram by [Job.company_display_name.

  * employment_type: histogram by Job.employment_types, for example, "FULL_TIME", "PART_TIME".
  * company_size (DEPRECATED): histogram by CompanySize, for example, "SMALL", "MEDIUM", "BIG".
  * publish_time_in_day: histogram by the Job.posting_publish_time in days. Must specify list of numeric buckets in spec.
  * publish_time_in_month: histogram by the Job.posting_publish_time in months. Must specify list of numeric buckets in spec.
  * publish_time_in_year: histogram by the Job.posting_publish_time in years. Must specify list of numeric buckets in spec.
  * degree_types: histogram by the Job.degree_types, for example, "Bachelors", "Masters".
  * job_level: histogram by the Job.job_level, for example, "Entry Level".
  * country: histogram by the country code of jobs, for example, "US", "FR".
  * admin1: histogram by the admin1 code of jobs, which is a global placeholder referring to the state, province, or the particular term a country uses to define the geographic structure below the country level, for example, "CA", "IL".
  * city: histogram by a combination of the "city name, admin1 code". For example, "Mountain View, CA", "New York, NY".
  * admin1_country: histogram by a combination of the "admin1 code, country", for example, "CA, US", "IL, US".
  * city_coordinate: histogram by the city center's GPS coordinates (latitude and longitude), for example, 37.4038522,-122.0987765. Since the coordinates of a city center can change, customers may need to refresh them periodically.
  * locale: histogram by the Job.language_code, for example, "en-US", "fr-FR".
  * language: histogram by the language subtag of the Job.language_code, for example, "en", "fr".
  * category: histogram by the JobCategory, for example, "COMPUTER_AND_IT", "HEALTHCARE".
  * base_compensation_unit: histogram by the CompensationInfo.CompensationUnit of base salary, for example, "WEEKLY", "MONTHLY".
  * base_compensation: histogram by the base salary. Must specify list of numeric buckets to group results by.
  * annualized_base_compensation: histogram by the base annualized salary. Must specify list of numeric buckets to group results by.
  * annualized_total_compensation: histogram by the total annualized salary. Must specify list of numeric buckets to group results by.
  * string_custom_attribute: histogram by string Job.custom_attributes. Values can be accessed via square bracket notations like string_custom_attribute["key1"].
  * numeric_custom_attribute: histogram by numeric Job.custom_attributes. Values can be accessed via square bracket notations like numeric_custom_attribute["key1"]. Must specify list of numeric buckets to group results by.

Example expressions:

  * `count(admin1)`

  * `count(base_compensation, [bucket(1000, 10000), bucket(10000, 100000), bucket(100000, MAX)])`
  * `count(string_custom_attribute["some-string-custom-attribute"])`
  * `count(numeric_custom_attribute["some-numeric-custom-attribute"], [bucket(MIN, 0, "negative"), bucket(0, MAX, "non-negative")])`



`repeated .google.cloud.talent.v4beta1.HistogramQuery histogram_queries = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HistogramQueryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.HistogramQueryOrBuilder)` |   
  
### getHistogramQueriesOrBuilderList()
    
    
    public abstract List<? extends HistogramQueryOrBuilder> getHistogramQueriesOrBuilderList()

An expression specifies a histogram request against matching jobs.

Expression syntax is an aggregation function call with histogram facets and other options.

Available aggregation function calls are:

  * `count(string_histogram_facet)`: Count the number of matching entities, for each distinct attribute value.
  * `count(numeric_histogram_facet, list of buckets)`: Count the number of matching entities within each bucket.

A maximum of 200 histogram buckets are supported.

Data types:

  * Histogram facet: facet names with format `a-zA-Z+`.

  * String: string like "any string with backslash escape for quote(\")."
  * Number: whole number and floating point number like 10, -1 and -0.01.
  * List: list of elements with comma(,) separator surrounded by square brackets, for example, [1, 2, 3] and ["one", "two", "three"].

Built-in constants:

  * MIN (minimum number similar to java Double.MIN_VALUE)

  * MAX (maximum number similar to java Double.MAX_VALUE)

Built-in functions:

  * bucket(start, end[, label]): bucket built-in function creates a bucket with range of start, end). Note that the end is exclusive, for example, bucket(1, MAX, "positive number") or bucket(1, 10).

Job histogram facets:

  * company_display_name: histogram by [Job.company_display_name.

  * employment_type: histogram by Job.employment_types, for example, "FULL_TIME", "PART_TIME".
  * company_size (DEPRECATED): histogram by CompanySize, for example, "SMALL", "MEDIUM", "BIG".
  * publish_time_in_day: histogram by the Job.posting_publish_time in days. Must specify list of numeric buckets in spec.
  * publish_time_in_month: histogram by the Job.posting_publish_time in months. Must specify list of numeric buckets in spec.
  * publish_time_in_year: histogram by the Job.posting_publish_time in years. Must specify list of numeric buckets in spec.
  * degree_types: histogram by the Job.degree_types, for example, "Bachelors", "Masters".
  * job_level: histogram by the Job.job_level, for example, "Entry Level".
  * country: histogram by the country code of jobs, for example, "US", "FR".
  * admin1: histogram by the admin1 code of jobs, which is a global placeholder referring to the state, province, or the particular term a country uses to define the geographic structure below the country level, for example, "CA", "IL".
  * city: histogram by a combination of the "city name, admin1 code". For example, "Mountain View, CA", "New York, NY".
  * admin1_country: histogram by a combination of the "admin1 code, country", for example, "CA, US", "IL, US".
  * city_coordinate: histogram by the city center's GPS coordinates (latitude and longitude), for example, 37.4038522,-122.0987765. Since the coordinates of a city center can change, customers may need to refresh them periodically.
  * locale: histogram by the Job.language_code, for example, "en-US", "fr-FR".
  * language: histogram by the language subtag of the Job.language_code, for example, "en", "fr".
  * category: histogram by the JobCategory, for example, "COMPUTER_AND_IT", "HEALTHCARE".
  * base_compensation_unit: histogram by the CompensationInfo.CompensationUnit of base salary, for example, "WEEKLY", "MONTHLY".
  * base_compensation: histogram by the base salary. Must specify list of numeric buckets to group results by.
  * annualized_base_compensation: histogram by the base annualized salary. Must specify list of numeric buckets to group results by.
  * annualized_total_compensation: histogram by the total annualized salary. Must specify list of numeric buckets to group results by.
  * string_custom_attribute: histogram by string Job.custom_attributes. Values can be accessed via square bracket notations like string_custom_attribute["key1"].
  * numeric_custom_attribute: histogram by numeric Job.custom_attributes. Values can be accessed via square bracket notations like numeric_custom_attribute["key1"]. Must specify list of numeric buckets to group results by.

Example expressions:

  * `count(admin1)`

  * `count(base_compensation, [bucket(1000, 10000), bucket(10000, 100000), bucket(100000, MAX)])`
  * `count(string_custom_attribute["some-string-custom-attribute"])`
  * `count(numeric_custom_attribute["some-numeric-custom-attribute"], [bucket(MIN, 0, "negative"), bucket(0, MAX, "non-negative")])`



`repeated .google.cloud.talent.v4beta1.HistogramQuery histogram_queries = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.talent.v4beta1.HistogramQueryOrBuilder>` |   
  
### getJobQuery()
    
    
    public abstract JobQuery getJobQuery()

Query used to search against jobs, such as keyword, location filters, etc.

`.google.cloud.talent.v4beta1.JobQuery job_query = 4;`

**Returns**  
---  
**Type** | **Description**  
`[JobQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.JobQuery)` | The jobQuery.  
  
### getJobQueryOrBuilder()
    
    
    public abstract JobQueryOrBuilder getJobQueryOrBuilder()

Query used to search against jobs, such as keyword, location filters, etc.

`.google.cloud.talent.v4beta1.JobQuery job_query = 4;`

**Returns**  
---  
**Type** | **Description**  
`[JobQueryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.JobQueryOrBuilder)` |   
  
### getJobView()
    
    
    public abstract JobView getJobView()

The desired job attributes returned for jobs in the search response. Defaults to JobView.JOB_VIEW_SMALL if no value is specified.

`.google.cloud.talent.v4beta1.JobView job_view = 8;`

**Returns**  
---  
**Type** | **Description**  
`[JobView](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.JobView)` | The jobView.  
  
### getJobViewValue()
    
    
    public abstract int getJobViewValue()

The desired job attributes returned for jobs in the search response. Defaults to JobView.JOB_VIEW_SMALL if no value is specified.

`.google.cloud.talent.v4beta1.JobView job_view = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for jobView.  
  
### getKeywordMatchMode()
    
    
    public abstract SearchJobsRequest.KeywordMatchMode getKeywordMatchMode()

Controls what keyword match options to use.

Defaults to KeywordMatchMode.KEYWORD_MATCH_ALL if no value is specified.

`.google.cloud.talent.v4beta1.SearchJobsRequest.KeywordMatchMode keyword_match_mode = 18; `

**Returns**  
---  
**Type** | **Description**  
`[SearchJobsRequest.KeywordMatchMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.SearchJobsRequest.KeywordMatchMode)` | The keywordMatchMode.  
  
### getKeywordMatchModeValue()
    
    
    public abstract int getKeywordMatchModeValue()

Controls what keyword match options to use.

Defaults to KeywordMatchMode.KEYWORD_MATCH_ALL if no value is specified.

`.google.cloud.talent.v4beta1.SearchJobsRequest.KeywordMatchMode keyword_match_mode = 18; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for keywordMatchMode.  
  
### getOffset()
    
    
    public abstract int getOffset()

An integer that specifies the current offset (that is, starting result location, amongst the jobs deemed by the API as relevant) in search results. This field is only considered if page_token is unset.

The maximum allowed value is 5000. Otherwise an error is thrown.

For example, 0 means to return results starting from the first matching job, and 10 means to return from the 11th job. This can be used for pagination, (for example, pageSize = 10 and offset = 10 means to return from the second page).

`int32 offset = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The offset.  
  
### getOrderBy()
    
    
    public abstract String getOrderBy()

The criteria determining how search results are sorted. Default is `"relevance desc"`.

Supported options are:

  * `"relevance desc"`: By relevance descending, as determined by the API algorithms. Relevance thresholding of query results is only available with this ordering.
  * `"posting_publish_time desc"`: By Job.posting_publish_time descending.
  * `"posting_update_time desc"`: By Job.posting_update_time descending.
  * `"title"`: By Job.title ascending.
  * `"title desc"`: By Job.title descending.
  * `"annualized_base_compensation"`: By job's CompensationInfo.annualized_base_compensation_range ascending. Jobs whose annualized base compensation is unspecified are put at the end of search results.
  * `"annualized_base_compensation desc"`: By job's CompensationInfo.annualized_base_compensation_range descending. Jobs whose annualized base compensation is unspecified are put at the end of search results.
  * `"annualized_total_compensation"`: By job's CompensationInfo.annualized_total_compensation_range ascending. Jobs whose annualized base compensation is unspecified are put at the end of search results.
  * `"annualized_total_compensation desc"`: By job's CompensationInfo.annualized_total_compensation_range descending. Jobs whose annualized base compensation is unspecified are put at the end of search results.
  * `"custom_ranking desc"`: By the relevance score adjusted to the SearchJobsRequest.CustomRankingInfo.ranking_expression with weight factor assigned by SearchJobsRequest.CustomRankingInfo.importance_level in descending order.
  * Location sorting: Use the special syntax to order jobs by distance:<br> `"distance_from('Hawaii')"`: Order by distance from Hawaii.<br> `"distance_from(19.89, 155.5)"`: Order by distance from a coordinate.<br> `"distance_from('Hawaii'), distance_from('Puerto Rico')"`: Order by multiple locations. See details below.<br> `"distance_from('Hawaii'), distance_from(19.89, 155.5)"`: Order by multiple locations. See details below.<br> The string can have a maximum of 256 characters. When multiple distance centers are provided, a job that is close to any of the distance centers would have a high rank. When a job has multiple locations, the job location closest to one of the distance centers will be used. Jobs that don't have locations will be ranked at the bottom. Distance is calculated with a precision of 11.3 meters (37.4 feet). Diversification strategy is still applied unless explicitly disabled in diversification_level.



`string order_by = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The orderBy.  
  
### getOrderByBytes()
    
    
    public abstract ByteString getOrderByBytes()

The criteria determining how search results are sorted. Default is `"relevance desc"`.

Supported options are:

  * `"relevance desc"`: By relevance descending, as determined by the API algorithms. Relevance thresholding of query results is only available with this ordering.
  * `"posting_publish_time desc"`: By Job.posting_publish_time descending.
  * `"posting_update_time desc"`: By Job.posting_update_time descending.
  * `"title"`: By Job.title ascending.
  * `"title desc"`: By Job.title descending.
  * `"annualized_base_compensation"`: By job's CompensationInfo.annualized_base_compensation_range ascending. Jobs whose annualized base compensation is unspecified are put at the end of search results.
  * `"annualized_base_compensation desc"`: By job's CompensationInfo.annualized_base_compensation_range descending. Jobs whose annualized base compensation is unspecified are put at the end of search results.
  * `"annualized_total_compensation"`: By job's CompensationInfo.annualized_total_compensation_range ascending. Jobs whose annualized base compensation is unspecified are put at the end of search results.
  * `"annualized_total_compensation desc"`: By job's CompensationInfo.annualized_total_compensation_range descending. Jobs whose annualized base compensation is unspecified are put at the end of search results.
  * `"custom_ranking desc"`: By the relevance score adjusted to the SearchJobsRequest.CustomRankingInfo.ranking_expression with weight factor assigned by SearchJobsRequest.CustomRankingInfo.importance_level in descending order.
  * Location sorting: Use the special syntax to order jobs by distance:<br> `"distance_from('Hawaii')"`: Order by distance from Hawaii.<br> `"distance_from(19.89, 155.5)"`: Order by distance from a coordinate.<br> `"distance_from('Hawaii'), distance_from('Puerto Rico')"`: Order by multiple locations. See details below.<br> `"distance_from('Hawaii'), distance_from(19.89, 155.5)"`: Order by multiple locations. See details below.<br> The string can have a maximum of 256 characters. When multiple distance centers are provided, a job that is close to any of the distance centers would have a high rank. When a job has multiple locations, the job location closest to one of the distance centers will be used. Jobs that don't have locations will be ranked at the bottom. Distance is calculated with a precision of 11.3 meters (37.4 feet). Diversification strategy is still applied unless explicitly disabled in diversification_level.



`string order_by = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for orderBy.  
  
### getPageSize()
    
    
    public abstract int getPageSize()

A limit on the number of jobs returned in the search results. Increasing this value above the default value of 10 can increase search response time. The value can be between 1 and 100.

`int32 page_size = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pageSize.  
  
### getPageToken()
    
    
    public abstract String getPageToken()

The token specifying the current offset within search results. See SearchJobsResponse.next_page_token for an explanation of how to obtain the next set of query results.

`string page_token = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageToken.  
  
### getPageTokenBytes()
    
    
    public abstract ByteString getPageTokenBytes()

The token specifying the current offset within search results. See SearchJobsResponse.next_page_token for an explanation of how to obtain the next set of query results.

`string page_token = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageToken.  
  
### getParent()
    
    
    public abstract String getParent()

Required. The resource name of the tenant to search within.

The format is "projects/{project_id}/tenants/{tenant_id}". For example, "projects/foo/tenant/bar". If tenant id is unspecified, a default tenant is created. For example, "projects/foo".

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The resource name of the tenant to search within.

The format is "projects/{project_id}/tenants/{tenant_id}". For example, "projects/foo/tenant/bar". If tenant id is unspecified, a default tenant is created. For example, "projects/foo".

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getRelevanceThreshold()
    
    
    public abstract SearchJobsRequest.RelevanceThreshold getRelevanceThreshold()

Optional. The relevance threshold of the search results.

Default to Google defined threshold, leveraging a balance of precision and recall to deliver both highly accurate results and comprehensive coverage of relevant information.

` .google.cloud.talent.v4beta1.SearchJobsRequest.RelevanceThreshold relevance_threshold = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchJobsRequest.RelevanceThreshold](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.SearchJobsRequest.RelevanceThreshold)` | The relevanceThreshold.  
  
### getRelevanceThresholdValue()
    
    
    public abstract int getRelevanceThresholdValue()

Optional. The relevance threshold of the search results.

Default to Google defined threshold, leveraging a balance of precision and recall to deliver both highly accurate results and comprehensive coverage of relevant information.

` .google.cloud.talent.v4beta1.SearchJobsRequest.RelevanceThreshold relevance_threshold = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for relevanceThreshold.  
  
### getRequestMetadata()
    
    
    public abstract RequestMetadata getRequestMetadata()

Required. The meta information collected about the job searcher, used to improve the search quality of the service. The identifiers (such as `user_id`) are provided by users, and must be unique and consistent.

` .google.cloud.talent.v4beta1.RequestMetadata request_metadata = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[RequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.RequestMetadata)` | The requestMetadata.  
  
### getRequestMetadataOrBuilder()
    
    
    public abstract RequestMetadataOrBuilder getRequestMetadataOrBuilder()

Required. The meta information collected about the job searcher, used to improve the search quality of the service. The identifiers (such as `user_id`) are provided by users, and must be unique and consistent.

` .google.cloud.talent.v4beta1.RequestMetadata request_metadata = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[RequestMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.RequestMetadataOrBuilder)` |   
  
### getRequirePreciseResultSize() (deprecated)
    
    
    public abstract boolean getRequirePreciseResultSize()

**Deprecated.** _google.cloud.talent.v4beta1.SearchJobsRequest.require_precise_result_size is deprecated. See google/cloud/talent/v4beta1/job_service.proto;l=615_

This field is deprecated.

`bool require_precise_result_size = 6 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The requirePreciseResultSize.  
  
### getSearchMode()
    
    
    public abstract SearchJobsRequest.SearchMode getSearchMode()

Mode of a search.

Defaults to SearchMode.JOB_SEARCH.

`.google.cloud.talent.v4beta1.SearchJobsRequest.SearchMode search_mode = 2;`

**Returns**  
---  
**Type** | **Description**  
`[SearchJobsRequest.SearchMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.SearchJobsRequest.SearchMode)` | The searchMode.  
  
### getSearchModeValue()
    
    
    public abstract int getSearchModeValue()

Mode of a search.

Defaults to SearchMode.JOB_SEARCH.

`.google.cloud.talent.v4beta1.SearchJobsRequest.SearchMode search_mode = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for searchMode.  
  
### hasCustomRankingInfo()
    
    
    public abstract boolean hasCustomRankingInfo()

Controls over how job documents get ranked on top of existing relevance score (determined by API algorithm).

` .google.cloud.talent.v4beta1.SearchJobsRequest.CustomRankingInfo custom_ranking_info = 14; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customRankingInfo field is set.  
  
### hasJobQuery()
    
    
    public abstract boolean hasJobQuery()

Query used to search against jobs, such as keyword, location filters, etc.

`.google.cloud.talent.v4beta1.JobQuery job_query = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the jobQuery field is set.  
  
### hasRequestMetadata()
    
    
    public abstract boolean hasRequestMetadata()

Required. The meta information collected about the job searcher, used to improve the search quality of the service. The identifiers (such as `user_id`) are provided by users, and must be unique and consistent.

` .google.cloud.talent.v4beta1.RequestMetadata request_metadata = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the requestMetadata field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
