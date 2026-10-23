---
url: https://docs.cloud.google.com/monitoring/api/v3/distribution-metrics/
title: Percentiles and distribution-valued metrics \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:24.239822+00:00
---

# Percentiles and distribution-valued metrics  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/v3/distribution-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Percentiles and distribution-valued metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to understand percentiles and the histogram model for a metric data with a [`Distribution`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution) value type. A distribution metric defines ranges of values, called _buckets_ , and records the count of measured values that falls into each bucket. Distribution metrics don't report the individual measure values; they report a histogram of counts in buckets. This value type is used by services when the individual measurements are too numerous to collect, but statistical information, such as averages or percentiles, about those measurements is valuable.

When you chart a distribution-valued metric on a heatmap, you can use an option in the chart toolbar to overlay the 50th, 95th, and 99th percentiles. To display a distribution-valued metric on a line chart, you must configure the chart to convert the distribution value into a numeric value. You can perform this conversion by using an [aligner](https://docs.cloud.google.com/monitoring/api/v3/aggregation#alignment-intro) that selects a percentile. 

The next section of this page uses a synthetic example to show how percentiles are determined. The example shows that the percentile values depend on the number of buckets, the width of the buckets, the distribution of the measurements, and the total count of samples. The percentile values don't depend on the actual measured values because those values aren't available in the histogram.

## Example with synthetic data

Consider an [`Exponential`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Exponential) bucket model with a scale of 1, a growth factor of 2, and 10 finite buckets. This histogram contains 12 buckets, the 10 finite buckets, 1 bucket that only specifies an upper bound, and 1 that only specifies a lower bound. For this example, the finite bucket with index _n+1_ is twice as wide as the finite bucket with index _n_.

The following examples show that the width of the bucket determines the maximum error between the computed percentile and the measurements. They also show that the number of samples in a histogram is important. For example, if the number of samples is less than 20, then the 95th and 99th percentiles are always in the same bucket.

### Case 1: The total number of samples is 1.

When there is a single measurement, the three percentile values differ but they only show the 50th, 95th, and 99th percentile of the same bucket. The error between the estimate and the actual measurements can't be determined because the measurement isn't known.

For example, assume that the histogram of measurements is as shown in the following table:

Bucket number | Lower bound | Upper bound | Count | Percentile range  
---|---|---|---|---  
0 |  | 1 | 0 | 0  
1 | 1 | 2 | 0 | 0  
2 | 2 | 4 | 0 | 0  
3 | 4 | 8 | 0 | 0  
4 | 8 | 16 | 0 | 0  
5 | 16 | 32 | 0 | 0  
6 | 32 | 64 | 0 | 0  
7 | 64 | 128 | 0 | 0  
8 | 128 | 256 | 1 | 0 - 100  
9 | 256 | 512 | 0 | 0  
10 | 512 | 1024 | 0 | 0  
11 | 1024 |  | 0 | 0  
  
To compute the 50th percentile, do the following:

  1. Use the bucket counts to determine the bucket that contains the 50th percentile. In this example, bucket number 8 contains the 50th percentile.
  2. Compute the estimate using the following rule:
         
         pth percentage = bucket_low +
                         (bucket_up - bucket_low)*(p - p_low)/(p_up - p_low)
         

In the previous expression, `p_low` and `p_up` are the lower and upper bounds of the percentile range for the bucket. Similarly, `bucket_low` and `bucket_up` are the lower and upper bounds of the bucket. The values for `p_low` and `p_up` depend on how the counts are distributed between the different buckets.




For example, the 50th percentile is computed as:
    
    
       50th percentile = 128 + (256-128)*(50-0)/(100-0)
                       = 128 + 128 * 50 / 100
                       = 128 + 64
                       = 192

To compute the 95th percentile, replace `50` with `95` in the previous expression. For this example where there is exactly one sample, the percentiles are as follows:

Percentile | Bucket number | Value  
---|---|---  
50th | 8 | 192  
95th | 8 | 249.6  
99th | 8 | 254.7  
  
The error between the estimate and the actual measurements can be bounded, but it can't be determined because the measurement isn't known.

### Case 2: The total number of samples is 10.

When there are 10 samples, the 50th percentile might be in a different bucket than the 95th and 99th percentiles. However, there aren't enough measurements to allow the 95th and 99th percentiles to be in different buckets.

For example, assume that the histogram of measurements is as shown in the following table:

Bucket number | Lower bound | Upper bound | Count | Percentile range  
---|---|---|---|---  
0 |  | 1 | 4 | 0 - 40  
1 | 1 | 2 | 2 | 40 - 60  
2 | 2 | 4 | 1 | 60 - 70  
3 | 4 | 8 | 1 | 70 - 80  
4 | 8 | 16 | 1 | 80 - 90  
5 | 16 | 32 | 0 | 0  
6 | 32 | 64 | 0 | 0  
7 | 64 | 128 | 0 | 0  
8 | 128 | 256 | 1 | 90 - 100  
9 | 256 | 512 | 0 | 0  
10 | 512 | 1024 | 0 | 0  
11 | 1024 |  | 0 | 0  
  
You can use the procedure described previously to compute the 50th, 95th, and 99th percentiles. For example, the 50th percentile, which is in bucket number 1, is computed as follows:
    
    
    50th percentile = 1 + (2-1)*(50-40)/(60-40)
                    = 1 + (1 * 10 / 20)
                    = 1 + 0.5
                    = 1.5
    

Similarly, the 95th percentile is computed as follows:
    
    
    95th percentile = 128 + (256-128)*(95-90)/(100-90)
                    = 128 + 128 * 5 / 10
                    = 128 + 64
                    = 192
    

By using the process described previously, the percentiles can be computed. Each row in the following table lists a percentile, the corresponding bucket, and the computed value:

Percentile | Bucket number | Value | Maximum error  
---|---|---|---  
50th | 1 | 1.5 | 0.5  
95th | 8 | 192 | 74  
99th | 8 | 243.2 | 115.2  
  
In this example and in the previous example, the 95th percentile is in bucket number 8; however, the percentile computation is different. The difference is due to how the samples are distributed. In the first example, all samples are in the same bucket, while in the most recent example, the samples are in different buckets.

## Example with real data

This section contains an example that illustrates how you can determine the bucket model used by a particular metric. This section also illustrates how you can evaluate the potential error in the computed percentile values.

### Identify the bucket model

To determine the buckets used for a metric over a specific time interval, call the Cloud Monitoring API's [`projects.timeSeries/list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method.

For example, to identify the bucket model for a metric, do the following:

  1. Go to the [`projects.timeSeries/list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) web page.
  2. In [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer), enter the filter that specifies the metric, a start time, and an end time.

For example, to get information about the metric that stores [API requests latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#serviceruntime/api/request_latencies), enter the following:
         
         metric.type="serviceruntime.googleapis.com/api/request_latencies"
         resource.type="consumed_api"
         

In this example, the filter field specifies a metric type and a resource type. For more information about these filters, see [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters).

  3. Click **Enter**.




The following is the `list` API response for a distribution-valued metric that is available on one Google Cloud project:
    
    
    {
      "timeSeries": [
        {
          "metric": {...},
          "resource": {...},
          },
          "metricKind": "DELTA",
          "valueType": "DISTRIBUTION",
          "points": [
            {
              "interval": {
                "startTime": "2020-11-03T15:05:00Z",
                "endTime": "2020-11-03T15:06:00Z"
              },
              "value": {
                "distributionValue": {
                  "count": "3",
                  "mean": 25.889,
                  "bucketOptions": {
                    "exponentialBuckets": {
                      "numFiniteBuckets": 66,
                      "growthFactor": 1.4,
                      "scale": 1
                    }
                  },
                  "bucketCounts": [
                    "0",
                    "0",
                    "0",
                    "0",
                    "0",
                    "0",
                    "0",
                    "0",
                    "0",
                    "0",
                    "3"
                  ]
                }
              }
            },
    

In the API response, the `value` field describes the data stored in the `points` array. The `count` and `mean` fields report that for the specified time interval there were 3 measurements and their average value was 25.889. The `bucketOptions` field shows that the exponential model is configured to have 66 buckets, a scale of 1, and a growth factor of 1.4.

To compute the lower and upper bounds for the bucket with index _n_ , use the following rules:

  * Lower bound (1 ≤ n < N) = scale * (growth factor)(n-1)
  * Upper bound (0 ≤ n < N-1) = scale * (growth factor)n



In the previous expressions, `N` is the total number of buckets.

The buckets for this metric, along with the midpoint of each bucket, are shown in the following table:

_n_ th bucket | Lower bound | Upper bound | Midpoint  
---|---|---|---  
0 |  | 1 | Not applicable  
1 | 1 | 1.40 | 1.20  
2 | 1.40 | 1.96 | 1.68  
... |  |  |   
9 | 14.76 | 20.66 | 17.71  
10 | 20.66 | 28.93 | 24.79  
11 | 28.93 | 40.50 | 34.71  
... |  |  |   
  
### Verify the percentile computations

Now that the bucket configuration is known, for any set of measurements you can predict the values of 50th, 95th, and 99th percentile values. For example, if there is one sample and it is in bucket number 10, then the 50th percentile value is 24.79.

To retrieve the 50th, 95th, and 99th percentile values of the metric, you can use the API method [`projects.timeSeries/list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list), and include an alignment period and aligner. In this example, the following settings were selected:

  * **Aligner** : `ALIGN_PERCENTILE_50`, `ALIGN_PERCENTILE_95`, or `ALIGN_PERCENTILE_99`
  * **Alignment Period** : 60 s



For the `ALIGN_PERCENTILE_50` selection, each value in the time series is the 50th percentile of a bucket:
    
    
    {
      "timeSeries": [
        {
          "metric": {...},
          "resource": {...},
          "metricKind": "GAUGE",
          "valueType": "DOUBLE",
          "points": [
            {
              "interval": {
                "startTime": "2020-11-03T15:06:36Z",
                "endTime": "2020-11-03T15:06:36Z"
              },
              "value": {
                "doubleValue": 24.793256140799986
              }
            },
            {
              "interval": {
                "startTime": "2020-11-03T15:05:36Z",
                "endTime": "2020-11-03T15:05:36Z"
              },
              "value": {
                "doubleValue": 34.710558597119977
              }
            },
            {
              "interval": {
                "startTime": "2020-11-03T15:04:36Z",
                "endTime": "2020-11-03T15:04:36Z"
              },
              "value": {
                "doubleValue": 24.793256140799986
              }
            }
          ]
        },
    

For two of the samples, the 50th percentile is in bucket 10, for the other sample it is in bucket 11.

The following table shows the results of executing the `projects.timeSeries/list` method with different aligners. The first row corresponds to the case where the aligner isn't specified. When you don't specify an aligner, the bucket model and mean values are returned. The next three rows list the data returned when the aligner is set to `ALIGN_PERCENTILE_50`, `ALIGN_PERCENTILE_95`, and `ALIGN_PERCENTILE_99`:

Statistic | Sample @ 15:06 | Sample @ 15:05 | Sample @ 15:04  
---|---|---|---  
mean | 25.889 | 33.7435 | Not available.  
50th percentile | 24.79 | 34.71 | 24.79  
95th percentile | 28.51 | 39.91 | 28.51  
99th percentile | 28.84 | 40.37 | 28.84  
  
As the two examples with synthetic data illustrate, the values of the percentiles dependent on how the samples are distributed. When all samples are in the sample bucket, then the 50th percentile is the midpoint of that bucket. However, when samples are in different buckets, that distribution affects the estimates.

To determine if the 50th percentile is a reasonable estimate of the mean, you can compare the mean value to the 50th percentile. The mean value is returned with the bucket details.

## What's next

For information about how to visualize distribution-valued metrics, see [About distribution-valued metrics](https://docs.cloud.google.com/monitoring/charts/charting-distribution-metrics). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
