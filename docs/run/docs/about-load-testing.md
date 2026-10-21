---
url: https://docs.cloud.google.com/run/docs/about-load-testing/
title: Load testing best practices \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:48.668565+00:00
---

# Load testing best practices  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/about-load-testing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Load testing best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page provides best practices for load testing your Cloud Run service to determine whether it scales successfully during production use, and to find any bottlenecks that prevent it from scaling.

## Tests to run **before** load testing

Identify and address concurrency problems in a development or small test environment before proceeding to load testing. Measure container concurrency before performing a load test, and make sure that your Cloud Run service starts up reliably.

Focus your container tests on small incremental counts in manually scaled runs. You can approximate manual scaling in Cloud Run by setting [maximum instances](https://docs.cloud.google.com/run/docs/about-instance-autoscaling#max-instances) to the value that you wish to scale to.

If you have only recently built your container image or recently changed the container image, test that independently before performing a load test.

You should also check other kinds of performance problems, such as excessive latency and CPU utilization, before running a large scale load test.

## Use `max instances` appropriately

Cloud Run enforces [a maximum instances](https://docs.cloud.google.com/run/docs/configuring/max-instances) to limit the scaling of a service. The default maximum number of instances is 100. If you expect your load test to exceed this default, make sure you work with your account team at Google and set a new maximum. If you do not yet have a relationship with an account team, [contact Google Cloud sales](https://cloud.google.com/contact).

The maximum number of instances that you can select depends on your [CPU limits](https://docs.cloud.google.com/run/docs/configuring/services/cpu) and [memory limits](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) as well as the region you are deploying to.

These limits are managed by a quota limit and can be increased by making a [quota limit increase request](https://docs.cloud.google.com/run/quotas#increase).

## Load test in the region `europe-west1`

The Google Cloud region `europe-west1` offers a high quota limit, so Google recommends load testing in `europe-west1`. Coordinate with your account team and submit a support case with details of the time and scale of the test if you expect to approach quota limits.

## Test an appropriate CPU utilization and service initialization profile

In an ideal scenario, you deploy a test version of your service to Cloud Run and load test it directly. However, in some cases, you might be unable to deploy a test version of your service. For example, your Cloud Run service might be part of a complex ecosystem that is hard to replicate in a test environment.

For these cases, you can approximate the performance of your service by simulating it with a simpler service that has comparable CPU usage and comparable initialization times. Initialization time is particularly important for rapid scaling. Keep in mind that testing with something too simple is also problematic. For example, avoid testing with a simple `hello world` service that returns received requests without any processing.

## Use a test harness to generate loads

You can generate test loads causing a controlled spike in traffic using a test harness, such as [JMeter](https://jmeter.apache.org/). You can use the number of JMeter thread groups and delay between requests in the JMeter test to increase the load.

You can also send simple HTTP requests or you can record a browser session with JMeter. Cloud Run lets you test your service without Internet access by using [Developer Authentication](https://docs.cloud.google.com/run/docs/authenticating/developers). This allows access from a test harness like JMeter, running on a Compute Engine virtual machine attached to a Virtual Private Cloud (VPC) associated with the project.

Do not generate load from tools where the rate and concurrency cannot be controlled. Pub/Sub is a poor choice of tool to generate load because you cannot control the rate of the traffic and number of clients. If you do not know the rate and concurrency, then you will not know what you are testing.

## Use detailed log analysis using exported logs

You need a second-by-second analysis of events to understand your Cloud Run service's response to rapid traffic spikes. Log analysis is needed to do this because the granularity of [monitoring data](https://docs.cloud.google.com/run/docs/monitoring) is not sufficiently fine grained. Log analysis also allows you to investigate the reasons for requests with high latency.

When you write logs, you can get better logging performance by writing directly to `stdout` instead of using a Cloud Logging client library.

To set up a log export before starting the test, create a [log sink](https://docs.cloud.google.com/logging/docs/routing/overview) with the destination BigQuery and an inclusion filter, such as:
    
    
    resource.type="cloud_run_revision"
    resource.labels.service_name="[your app]"
    

## Avoid spurious cold starts

To minimize [cold starts](https://docs.cloud.google.com/run/docs/tips/general#using_minimum_instances_to_reduce_cold_starts) experienced by users, set the [minimum number of instances](https://docs.cloud.google.com/run/docs/configuring/min-instances) to at least 1.

## Ensure that your service scales out linearly

Repeat the test at different loads to make sure that your Cloud Run service scales out linearly with load and does not reach a limiting bottleneck at a load less than you expect in production.

## Analyze and visualize the results in Colaboratory

Use the summary monitoring charts to get a high level understanding of results to supplement the detailed log analysis using exported logs.

The monitoring charts can help you discover:

  * How quickly, to the nearest second, are new instances created and initialized?
  * How evenly are requests distributed across different instances?
  * How quickly can the latency at different percentiles be drawn down to a steady-state value?



You can use the Google Cloud console user interface for BigQuery to introspect the exported log schema and preview results. Run the queries and plot results using [Colab](https://colab.sandbox.google.com/notebooks/bigquery.ipynb), which has ready integration with BigQuery, Pandas, and Matplotlab. Colab also integrates easily with rich data visualization tools like [Seaborn](https://seaborn.pydata.org/).

## Find bottlenecks

Load tests can help you discover the existence of both inefficient code and scaling bottlenecks. Inefficient code leads to higher costs as it needs to handle more traffic but does not necessarily prevent scaling. For example, a dependency on a database translation with table level locking can be a bottleneck that will prevent the Cloud Run service from scaling because only one transaction can execute at a time.

## Check performance as experienced by the client

You can query logs captured by [JMeter](https://jmeter.apache.org/), where the logs include latencies measured at the client. However, because server testing tools like JMeter are not the same as a browser or mobile client, you may also want to run a test with a browser-based framework, such as [Selenium Webdriver](https://www.selenium.dev/documentation/webdriver/), or a mobile client testing framework. Be careful of excessive maximum latencies due to TLS connection initialization that may skew results with outliers.

## Summary of best practices

Perform a load test to determine whether migrating to Cloud Run is the right choice and that your service can scale to the maximum expected traffic. Run the test with a harness like JMeter. Export the logs to BigQuery for detailed analysis.

### What's next

  * [Cloud Run Development Tips](https://docs.cloud.google.com/run/docs/tips/general)
  * [Use Cloud Trace with Cloud Run](https://docs.cloud.google.com/run/docs/trace)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
