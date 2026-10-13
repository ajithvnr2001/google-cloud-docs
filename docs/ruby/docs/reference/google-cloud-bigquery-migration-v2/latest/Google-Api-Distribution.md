---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution/
title: BigQuery Migration V2 API - Class Google::Api::Distribution (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:53.673368+00:00
---

# BigQuery Migration V2 API - Class Google::Api::Distribution (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Api::Distribution (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Api::Distribution.

`Distribution` contains summary statistics for a population of values. It optionally contains a histogram representing the distribution of those values across a set of buckets.

The summary statistics are the count, mean, sum of the squared deviation from the mean, the minimum, and the maximum of the set of population of values. The histogram is based on a sequence of buckets and gives a count of values that fall into each bucket. The boundaries of the buckets are given either explicitly or by formulas for buckets of fixed or exponentially increasing widths.

Although it is not forbidden, it is generally a bad idea to include non-finite values (infinities or NaNs) in the population of values, as this will render the `mean` and `sum_of_squared_deviation` fields meaningless.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bucket_counts
    
    
    def bucket_counts() -> ::Array<::Integer>

**Returns**

  * (::Array<::Integer>) — The number of values in each bucket of the histogram, as described in `bucket_options`. If the distribution does not have a histogram, then omit this field. If there is a histogram, then the sum of the values in `bucket_counts` must equal the value in the `count` field of the distribution.

If present, `bucket_counts` should contain N values, where N is the number of buckets specified in `bucket_options`. If you supply fewer than N values, the remaining values are assumed to be 0.

The order of the values in `bucket_counts` follows the bucket numbering schemes described for the three bucket types. The first value must be the count for the underflow bucket (number 0). The next N-2 values are the counts for the finite buckets (number 1 through N-2). The N'th value in `bucket_counts` is the count for the overflow bucket (number N-1). 




### #bucket_counts=
    
    
    def bucket_counts=(value) -> ::Array<::Integer>

**Parameter**

  * **value** (::Array<::Integer>) — The number of values in each bucket of the histogram, as described in `bucket_options`. If the distribution does not have a histogram, then omit this field. If there is a histogram, then the sum of the values in `bucket_counts` must equal the value in the `count` field of the distribution.

If present, `bucket_counts` should contain N values, where N is the number of buckets specified in `bucket_options`. If you supply fewer than N values, the remaining values are assumed to be 0.

The order of the values in `bucket_counts` follows the bucket numbering schemes described for the three bucket types. The first value must be the count for the underflow bucket (number 0). The next N-2 values are the counts for the finite buckets (number 1 through N-2). The N'th value in `bucket_counts` is the count for the overflow bucket (number N-1). 




**Returns**

  * (::Array<::Integer>) — The number of values in each bucket of the histogram, as described in `bucket_options`. If the distribution does not have a histogram, then omit this field. If there is a histogram, then the sum of the values in `bucket_counts` must equal the value in the `count` field of the distribution.

If present, `bucket_counts` should contain N values, where N is the number of buckets specified in `bucket_options`. If you supply fewer than N values, the remaining values are assumed to be 0.

The order of the values in `bucket_counts` follows the bucket numbering schemes described for the three bucket types. The first value must be the count for the underflow bucket (number 0). The next N-2 values are the counts for the finite buckets (number 1 through N-2). The N'th value in `bucket_counts` is the count for the overflow bucket (number N-1). 




### #bucket_options
    
    
    def bucket_options() -> ::Google::Api::Distribution::BucketOptions

**Returns**

  * ([::Google::Api::Distribution::BucketOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions)) — Defines the histogram bucket boundaries. If the distribution does not contain a histogram, then omit this field. 



### #bucket_options=
    
    
    def bucket_options=(value) -> ::Google::Api::Distribution::BucketOptions

**Parameter**

  * **value** ([::Google::Api::Distribution::BucketOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions)) — Defines the histogram bucket boundaries. If the distribution does not contain a histogram, then omit this field. 



**Returns**

  * ([::Google::Api::Distribution::BucketOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions)) — Defines the histogram bucket boundaries. If the distribution does not contain a histogram, then omit this field. 



### #count
    
    
    def count() -> ::Integer

**Returns**

  * (::Integer) — The number of values in the population. Must be non-negative. This value must equal the sum of the values in `bucket_counts` if a histogram is provided. 



### #count=
    
    
    def count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of values in the population. Must be non-negative. This value must equal the sum of the values in `bucket_counts` if a histogram is provided. 



**Returns**

  * (::Integer) — The number of values in the population. Must be non-negative. This value must equal the sum of the values in `bucket_counts` if a histogram is provided. 



### #exemplars
    
    
    def exemplars() -> ::Array<::Google::Api::Distribution::Exemplar>

**Returns**

  * (::Array<[::Google::Api::Distribution::Exemplar](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-Exemplar)>) — Must be in increasing order of `value` field. 



### #exemplars=
    
    
    def exemplars=(value) -> ::Array<::Google::Api::Distribution::Exemplar>

**Parameter**

  * **value** (::Array<[::Google::Api::Distribution::Exemplar](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-Exemplar)>) — Must be in increasing order of `value` field. 



**Returns**

  * (::Array<[::Google::Api::Distribution::Exemplar](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-Exemplar)>) — Must be in increasing order of `value` field. 



### #mean
    
    
    def mean() -> ::Float

**Returns**

  * (::Float) — The arithmetic mean of the values in the population. If `count` is zero then this field must be zero. 



### #mean=
    
    
    def mean=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The arithmetic mean of the values in the population. If `count` is zero then this field must be zero. 



**Returns**

  * (::Float) — The arithmetic mean of the values in the population. If `count` is zero then this field must be zero. 



### #range
    
    
    def range() -> ::Google::Api::Distribution::Range

**Returns**

  * ([::Google::Api::Distribution::Range](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-Range)) — If specified, contains the range of the population values. The field must not be present if the `count` is zero. 



### #range=
    
    
    def range=(value) -> ::Google::Api::Distribution::Range

**Parameter**

  * **value** ([::Google::Api::Distribution::Range](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-Range)) — If specified, contains the range of the population values. The field must not be present if the `count` is zero. 



**Returns**

  * ([::Google::Api::Distribution::Range](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-Range)) — If specified, contains the range of the population values. The field must not be present if the `count` is zero. 



### #sum_of_squared_deviation
    
    
    def sum_of_squared_deviation() -> ::Float

**Returns**

  * (::Float) — The sum of squared deviations from the mean of the values in the population. For values x_i this is:
        
        Sum[i=1..n]((x_i - mean)^2)
        

Knuth, "The Art of Computer Programming", Vol. 2, page 232, 3rd edition describes Welford's method for accumulating this sum in one pass.

If `count` is zero then this field must be zero. 




### #sum_of_squared_deviation=
    
    
    def sum_of_squared_deviation=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The sum of squared deviations from the mean of the values in the population. For values x_i this is:
        
        Sum[i=1..n]((x_i - mean)^2)
        

Knuth, "The Art of Computer Programming", Vol. 2, page 232, 3rd edition describes Welford's method for accumulating this sum in one pass.

If `count` is zero then this field must be zero. 




**Returns**

  * (::Float) — The sum of squared deviations from the mean of the values in the population. For values x_i this is:
        
        Sum[i=1..n]((x_i - mean)^2)
        

Knuth, "The Art of Computer Programming", Vol. 2, page 232, 3rd edition describes Welford's method for accumulating this sum in one pass.

If `count` is zero then this field must be zero. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
