---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-cpu/
title: CPU load measurement \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:11.284155+00:00
---

# CPU load measurement  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-cpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  CPU load measurement Stay organized with collections  Save and categorize content based on your preferences. 

Returns the most recent Cloud Bigtable CPU load measurement.

## Code sample

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Timestamp now = timeXMinutesAgo(0);
    Timestamp fiveMinutesAgo = timeXMinutesAgo(5);
    TimeInterval interval =
        TimeInterval.newBuilder().setStartTime(fiveMinutesAgo).setEndTime(now).build();
    String filter = "metric.type=\"" + CPU_METRIC + "\"";
    ListTimeSeriesPagedResponse response =
        metricServiceClient.listTimeSeries(projectName, filter, interval, TimeSeriesView.FULL);
    return response.getPage().getValues().iterator().next().getPointsList().get(0);

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    client = monitoring_v3.MetricServiceClient()
    cpu_query = query.Query(
        client,
        project=PROJECT,
        metric_type="bigtable.googleapis.com/cluster/cpu_load",
        minutes=5,
    )
    cpu_query = cpu_query.select_resources(
        instance=bigtable_instance, cluster=bigtable_cluster
    )
    cpu = next(cpu_query.iter())
    return cpu.points[0].value.double_value

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
