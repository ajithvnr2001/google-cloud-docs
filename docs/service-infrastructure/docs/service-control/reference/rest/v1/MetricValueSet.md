---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet/
title: MetricValueSet \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:33.244203+00:00
---

# MetricValueSet  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  MetricValueSet Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * MetricValue
    * JSON representation
  * Distribution
    * JSON representation
  * LinearBuckets
    * JSON representation
  * ExponentialBuckets
    * JSON representation
  * ExplicitBuckets
    * JSON representation
  * Exemplar
    * JSON representation



Represents a set of metric values in the same metric. Each metric value in the set should have a unique combination of start time, end time, and label values.

JSON representation  
---  
      
    
    {
      "metricName": string,
      "metricValues": [
        {
          object ([MetricValue](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#MetricValue))
        }
      ]
    }  
  
Fields  
---  
`metricName` |  `string` The metric name defined in the service configuration.  
`metricValues[]` |  `object (`[MetricValue](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#MetricValue)`)` The values in this metric.  
  
## MetricValue

Represents a single metric value.

JSON representation  
---  
      
    
    {
      "labels": {
        string: string,
        ...
      },
      "startTime": string,
      "endTime": string,
    
      // Union field value can be only one of the following:
      "boolValue": boolean,
      "int64Value": string,
      "doubleValue": number,
      "stringValue": string,
      "distributionValue": {
        object ([Distribution](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#Distribution))
      }
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
`labels` |  `map (key: string, value: string)` The labels describing the metric value. See comments on `[google.api.servicecontrol.v1.Operation.labels](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#FIELDS.labels)` for the overriding relationship. Note that this map must not contain monitored resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`startTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The start of the time period over which this metric value's measurement applies. The time period has different semantics for different metric types (cumulative, delta, and gauge). See the metric definition documentation in the service configuration for details. If not specified, `[google.api.servicecontrol.v1.Operation.start_time](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#FIELDS.start_time)` will be used.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The end of the time period over which this metric value's measurement applies. If not specified, `[google.api.servicecontrol.v1.Operation.end_time](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#FIELDS.end_time)` will be used.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
Union field `value`. The value. The type of value used in the request must agree with the metric definition in the service configuration, otherwise the MetricValue is rejected. `value` can be only one of the following:  
`boolValue` |  `boolean` A boolean value.  
`int64Value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` A signed 64-bit integer value.  
`doubleValue` |  `number` A double precision floating point value.  
`stringValue` |  `string` A text string value.  
`distributionValue` |  `object (`[Distribution](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#Distribution)`)` A distribution value.  
  
## Distribution

Distribution represents a frequency distribution of double-valued sample points. It contains the size of the population of sample points plus additional optional information:

  * the arithmetic mean of the samples
  * the minimum and maximum of the samples
  * the sum-squared-deviation of the samples, used to compute variance
  * a histogram of the values of the sample points

JSON representation  
---  
      
    
    {
      "count": string,
      "mean": number,
      "minimum": number,
      "maximum": number,
      "sumOfSquaredDeviation": number,
      "bucketCounts": [
        string
      ],
      "exemplars": [
        {
          object ([Exemplar](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#Exemplar))
        }
      ],
    
      // Union field bucket_option can be only one of the following:
      "linearBuckets": {
        object ([LinearBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#LinearBuckets))
      },
      "exponentialBuckets": {
        object ([ExponentialBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#ExponentialBuckets))
      },
      "explicitBuckets": {
        object ([ExplicitBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#ExplicitBuckets))
      }
      // End of list of possible types for union field bucket_option.
    }  
  
Fields  
---  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of samples in the distribution. Must be >= 0.  
`mean` |  `number` The arithmetic mean of the samples in the distribution. If `count` is zero then this field must be zero.  
`minimum` |  `number` The minimum of the population of values. Ignored if `count` is zero.  
`maximum` |  `number` The maximum of the population of values. Ignored if `count` is zero.  
`sumOfSquaredDeviation` |  `number` The sum of squared deviations from the mean: Sum[i=1..count]((x_i - mean)^2) where each x_i is a sample values. If `count` is zero then this field must be zero, otherwise validation of the request fails.  
`bucketCounts[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of samples in each histogram bucket. `bucketCounts` are optional. If present, they must sum to the `count` value.The buckets are defined below in `bucket_option`. There are N buckets. `bucketCounts[0]` is the number of samples in the underflow bucket. `bucketCounts[1]` to `bucketCounts[N-1]` are the numbers of samples in each of the finite buckets. And `bucketCounts[N] is the number of samples in the overflow bucket. See the comments of`bucket_option` below for more details.Any suffix of trailing zeros may be omitted.  
`exemplars[]` |  `object (`[Exemplar](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#Exemplar)`)` Example points. Must be in increasing order of `value` field.  
Union field `bucket_option`. Defines the buckets in the histogram. `bucket_option` and `bucket_counts` must be both set, or both unset.Buckets are numbered in the range of [0, N], with a total of N+1 buckets. There must be at least two buckets (a single-bucket histogram gives no information that isn't already provided by `count`).The first bucket is the underflow bucket which has a lower bound of -inf. The last bucket is the overflow bucket which has an upper bound of +inf. All other buckets (if any) are called "finite" buckets because they have finite lower and upper bounds. As described below, there are three ways to define the finite buckets.(1) Buckets with constant width. (2) Buckets with exponentially growing widths. (3) Buckets with arbitrary user-provided widths.In all cases, the buckets cover the entire real number line (-inf, +inf). Bucket upper bounds are exclusive and lower bounds are inclusive. The upper bound of the underflow bucket is equal to the lower bound of the smallest finite bucket; the lower bound of the overflow bucket is equal to the upper bound of the largest finite bucket. `bucket_option` can be only one of the following:  
`linearBuckets` |  `object (`[LinearBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#LinearBuckets)`)` Buckets with constant width.  
`exponentialBuckets` |  `object (`[ExponentialBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#ExponentialBuckets)`)` Buckets with exponentially growing width.  
`explicitBuckets` |  `object (`[ExplicitBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet#ExplicitBuckets)`)` Buckets with arbitrary user-provided width.  
  
## LinearBuckets

Describing buckets with constant width.

JSON representation  
---  
      
    
    {
      "numFiniteBuckets": integer,
      "width": number,
      "offset": number
    }  
  
Fields  
---  
`numFiniteBuckets` |  `integer` The number of finite buckets. With the underflow and overflow buckets, the total number of buckets is `numFiniteBuckets` \+ 2. See comments on `bucketOptions` for details.  
`width` |  `number` The i'th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to numFiniteBuckets, inclusive. Must be strictly positive.  
`offset` |  `number` The i'th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to numFiniteBuckets, inclusive.  
  
## ExponentialBuckets

Describing buckets with exponentially growing width.

JSON representation  
---  
      
    
    {
      "numFiniteBuckets": integer,
      "growthFactor": number,
      "scale": number
    }  
  
Fields  
---  
`numFiniteBuckets` |  `integer` The number of finite buckets. With the underflow and overflow buckets, the total number of buckets is `numFiniteBuckets` \+ 2. See comments on `bucketOptions` for details.  
`growthFactor` |  `number` The i'th exponential bucket covers the interval [scale * growthFactor^(i-1), scale * growthFactor^i) where i ranges from 1 to numFiniteBuckets inclusive. Must be larger than 1.0.  
`scale` |  `number` The i'th exponential bucket covers the interval [scale * growthFactor^(i-1), scale * growthFactor^i) where i ranges from 1 to numFiniteBuckets inclusive. Must be > 0.  
  
## ExplicitBuckets

Describing buckets with arbitrary user-provided width.

JSON representation  
---  
      
    
    {
      "bounds": [
        number
      ]
    }  
  
Fields  
---  
`bounds[]` |  `number` 'bound' is a list of strictly increasing boundaries between buckets. Note that a list of length N-1 defines N buckets because of fenceposting. See comments on `bucketOptions` for details.The i'th finite bucket covers the interval [bound[i-1], bound[i]) where i ranges from 1 to bound_size() - 1. Note that there are no finite buckets at all if 'bound' only contains a single element; in that special case the single bound defines the boundary between the underflow and overflow buckets.bucket number lower bound upper bound i == 0 (underflow) -inf bound[i] 0 < i < bound_size() bound[i-1] bound[i] i == bound_size() (overflow) bound[i-1] +inf  
  
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
`timestamp` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The observation (sampling) time of the above value.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`attachments[]` |  `object` Contextual information about the example value. Examples are:Trace: type.googleapis.com/google.monitoring.v3.SpanContextLiteral string: type.googleapis.com/google.protobuf.StringValueLabels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabelsThere may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
