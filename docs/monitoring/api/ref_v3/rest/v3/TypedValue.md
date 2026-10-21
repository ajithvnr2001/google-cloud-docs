---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue/
title: TypedValue \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:18.544456+00:00
---

# TypedValue  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  TypedValue Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Distribution
    * JSON representation
  * Range
    * JSON representation
  * BucketOptions
    * JSON representation
  * Linear
    * JSON representation
  * Exponential
    * JSON representation
  * Explicit
    * JSON representation
  * Exemplar
    * JSON representation



A single strongly-typed value.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "boolValue": boolean,
      "int64Value": string,
      "doubleValue": number,
      "stringValue": string,
      "distributionValue": {
        object ([Distribution](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The typed value field. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`boolValue` |  `boolean` A Boolean value: `true` or `false`.  
`int64Value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` A 64-bit integer. Its range is approximately ±9.2x1018.  
`doubleValue` |  `number` A 64-bit double-precision floating-point number. Its magnitude is approximately ±10±300 and it has 16 significant digits of precision.  
`stringValue` |  `string` A variable-length string value.  
`distributionValue` |  `object (`[Distribution](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution)`)` A distribution value.  
End of mutually exclusive fields.  
  
## Distribution

`Distribution` contains summary statistics for a population of values. It optionally contains a histogram representing the distribution of those values across a set of buckets.

The summary statistics are the count, mean, sum of the squared deviation from the mean, the minimum, and the maximum of the set of population of values. The histogram is based on a sequence of buckets and gives a count of values that fall into each bucket. The boundaries of the buckets are given either explicitly or by formulas for buckets of fixed or exponentially increasing widths.

Although it is not forbidden, it is generally a bad idea to include non-finite values (infinities or NaNs) in the population of values, as this will render the `mean` and `sumOfSquaredDeviation` fields meaningless.

JSON representation  
---  
      
    
    {
      "count": string,
      "mean": number,
      "sumOfSquaredDeviation": number,
      "range": {
        object ([Range](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Range))
      },
      "bucketOptions": {
        object ([BucketOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#BucketOptions))
      },
      "bucketCounts": [
        string
      ],
      "exemplars": [
        {
          object ([Exemplar](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Exemplar))
        }
      ]
    }  
  
Fields  
---  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of values in the population. Must be non-negative. This value must equal the sum of the values in `bucketCounts` if a histogram is provided.  
`mean` |  `number` The arithmetic mean of the values in the population. If `count` is zero then this field must be zero.  
`sumOfSquaredDeviation` |  `number` The sum of squared deviations from the mean of the values in the population. For values x_i this is:
    
    
    Sum[i=1..n]((x_i - mean)^2)
    

Knuth, "The Art of Computer Programming", Vol. 2, page 232, 3rd edition describes Welford's method for accumulating this sum in one pass.If `count` is zero then this field must be zero.  
`range` |  `object (`[Range](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Range)`)` If specified, contains the range of the population values. The field must not be present if the count is zero. This field is presently ignored by the Cloud Monitoring API v3.  
`bucketOptions` |  `object (`[BucketOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#BucketOptions)`)` Required in the Cloud Monitoring API v3. Defines the histogram bucket boundaries.  
`bucketCounts[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required in the Cloud Monitoring API v3. The values for each bucket specified in `bucketOptions`. The sum of the values in `bucketCounts` must equal the value in the count field of the `Distribution` object. The order of the bucket counts follows the numbering schemes described for the three bucket types. The underflow bucket has number 0; the finite buckets, if any, have numbers 1 through N-2; and the overflow bucket has number N-1. The size of `bucketCounts` must not be greater than N. If the size is less than N, then the remaining buckets are assigned values of zero.  
`exemplars[]` |  `object (`[Exemplar](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Exemplar)`)` Must be in increasing order of `value` field.  
  
## Range

The range of the population values.

JSON representation  
---  
      
    
    {
      "min": number,
      "max": number
    }  
  
Fields  
---  
`min` |  `number` The minimum of the population values.  
`max` |  `number` The maximum of the population values.  
  
## BucketOptions

`BucketOptions` describes the bucket boundaries used to create a histogram for the distribution. The buckets can be in a linear sequence, an exponential sequence, or each bucket can be specified explicitly. `BucketOptions` does not include the number of values in each bucket.

A bucket has an inclusive lower bound and exclusive upper bound for the values that are counted for that bucket. The upper bound of a bucket must be strictly greater than the lower bound. The sequence of N buckets for a distribution consists of an underflow bucket (number 0), zero or more finite buckets (number 1 through N - 2) and an overflow bucket (number N - 1). The buckets are contiguous: the lower bound of bucket i (i > 0) is the same as the upper bound of bucket i - 1. The buckets span the whole range of finite values: lower bound of the underflow bucket is -infinity and the upper bound of the overflow bucket is +infinity. The finite buckets are so-called because both bounds are finite.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "linearBuckets": {
        object ([Linear](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Linear))
      },
      "exponentialBuckets": {
        object ([Exponential](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Exponential))
      },
      "explicitBuckets": {
        object ([Explicit](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Explicit))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Exactly one of these three fields must be set. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`linearBuckets` |  `object (`[Linear](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Linear)`)` The linear bucket.  
`exponentialBuckets` |  `object (`[Exponential](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Exponential)`)` The exponential buckets.  
`explicitBuckets` |  `object (`[Explicit](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Explicit)`)` The explicit buckets.  
End of mutually exclusive fields.  
  
## Linear

Specifies a linear sequence of buckets that all have the same width (except overflow and underflow). Each bucket represents a constant absolute uncertainty on the specific value in the bucket.

There are `numFiniteBuckets + 2` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): offset + (width * i).

Lower bound (1 <= i < N): offset + (width * (i - 1)).

JSON representation  
---  
      
    
    {
      "numFiniteBuckets": integer,
      "width": number,
      "offset": number
    }  
  
Fields  
---  
`numFiniteBuckets` |  `integer` Must be greater than 0.  
`width` |  `number` Must be greater than 0.  
`offset` |  `number` Lower bound of the first bucket.  
  
## Exponential

Specifies an exponential sequence of buckets that have a width that is proportional to the value of the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket.

There are `numFiniteBuckets + 2` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): scale * (growthFactor ^ i).

Lower bound (1 <= i < N): scale * (growthFactor ^ (i - 1)).

JSON representation  
---  
      
    
    {
      "numFiniteBuckets": integer,
      "growthFactor": number,
      "scale": number
    }  
  
Fields  
---  
`numFiniteBuckets` |  `integer` Must be greater than 0.  
`growthFactor` |  `number` Must be greater than 1.  
`scale` |  `number` Must be greater than 0.  
  
## Explicit

Specifies a set of buckets with arbitrary widths.

There are `size(bounds) + 1` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): bounds[i] Lower bound (1 <= i < N); bounds[i - 1]

The `bounds` field must contain at least one element. If `bounds` has only one element, then there are no finite buckets, and that single element is the common boundary of the overflow and underflow buckets.

JSON representation  
---  
      
    
    {
      "bounds": [
        number
      ]
    }  
  
Fields  
---  
`bounds[]` |  `number` The values must be monotonically increasing.  
  
## Exemplar

Exemplars are example points that may be used to annotate aggregated distribution values. They are metadata that gives information about a particular value added to a Distribution bucket, such as a trace ID that was active when a value was added. They may contain further information, such as a example values and timestamps, origin, etc.

JSON representation  
---  
      
    
    {
      "value": number,
      "timestamp": string,
      "attachments": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`value` |  `number` Value of the exemplar point. This value determines to which bucket the exemplar belongs.  
`timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The observation (sampling) time of the above value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attachments[]` |  `object` Contextual information about the example value. Examples are:Trace: type.googleapis.com/google.monitoring.v3.SpanContextLiteral string: type.googleapis.com/google.protobuf.StringValueLabels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabelsThere may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
