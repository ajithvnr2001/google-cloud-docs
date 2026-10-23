---
url: https://docs.cloud.google.com/monitoring/uptime-checks/introduction/
title: Synthetic monitoring overview \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:04.879088+00:00
---

# Synthetic monitoring overview  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/uptime-checks/introduction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Synthetic monitoring overview Stay organized with collections  Save and categorize content based on your preferences. 

Synthetic monitors and uptime checks in Cloud Monitoring let you test the availability, consistency, and performance of your services, applications, web pages, and APIs. They periodically send simulated requests or run scripted tests, and record the outcome and latency of each execution. You can then create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts) to notify you whenever a test fails.

## Synthetic monitoring options

To test your services and applications, you can choose from the following approaches:

  * **Uptime checks** let you periodically query public or private endpoints that respond to HTTP, HTTPS, or TCP requests, and validate the response data.

  * **Custom and Mocha-based synthetic monitors** let you deploy a suite of tests for applications that respond to HTTP or HTTPS requests. You start with a custom or Mocha framework provided by Cloud Monitoring and then write your tests, or prompt Gemini Code Assist to generate the test code if you have access in your project.

  * **Broken-link checkers** let you periodically test a URI and a configurable number of links found at that URI.




The following table lists the tools that you can use to create uptime checks and synthetic monitors: 

| Google Cloud console | Cloud Monitoring API | Terraform | Client libraries  
---|---|---|---|---  
Uptime checks | Y | Y | Y | Y  
Synthetic monitors | Y | Y | Y |   
Broken-link checkers | Y | Y | Y |   
  
## About uptime checks

There are two types of uptime checks:

  * [Public uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks) issue requests from multiple locations throughout the world to _publicly available_ URLs or Google Cloud resources.
  * [Private uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks) issue requests to internal IP addresses of Google Cloud resources. Private uptime checks can send requests over a _private_ network to resources like a virtual machine (VM) or an L4 internal load balancer (ILB).



The requests made on behalf of uptime checks originate from _checkers_ that reside in several Google Cloud regions. When you create an uptime check, you specify the regions for the checkers.

The request-execution system for uptime checks, which is provided by Google Cloud, manages the following:

  * Execution of the configured checkers.
  * Validation of results.

The request issued by a checker succeeds if the resource responds and any requirements of the uptime-check configuration are met. Otherwise, the request fails. The queries by individual checkers are stateless; that is, each query is an independent action.

  * Collecting and storing the results in uptime-check metrics.

For more information about these metrics, see the `uptime_check` entries in the [`monitoring` metrics table](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/uptime_check/check_passed).

  * Writing log entries on failure.

If you create your uptime check by using the Google Cloud console, then you can configure the uptime check to also write a log entry when the check fails. If you've configured a public uptime check to send ICMP pings, then the results of those pings are written to Cloud Logging logs when the ping fails. For more information, see [Use ICMP pings](https://docs.cloud.google.com/monitoring/uptime-checks#ping).




## About broken-link checkers and other synthetic monitors

Synthetic monitors let you define what you are going to test and a sequence of tests. For example, you can test the login page of your application, the checkout process of your ecommerce store, or the API calls that your application makes to third-party services.

When you create a synthetic monitor, you deploy a [2nd gen Cloud Run function](https://docs.cloud.google.com/functions/docs/concepts/overview), which is built on [Cloud Run](https://docs.cloud.google.com/run). Your function must be written in Node.js and rely on the open source [Synthetics SDK framework](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs). Cloud Monitoring distributes and manages this framework.

Cloud Monitoring supports the following types of synthetic monitors:

  * [Custom or Mocha-based synthetic monitors](https://docs.cloud.google.com/monitoring/synthetic-monitors/create) let you deploy a fully configurable single-purpose Cloud Run function.

  * [Broken-link checkers](https://docs.cloud.google.com/monitoring/synthetic-monitors/broken-links) let you specify options, such as the origin URI, the number of links tested, and the number of retries, before deploying a preconfigured Cloud Run function.




The request-execution system for synthetic monitors, which is provided by Google Cloud, manages the following:

  * Periodic execution of your Cloud Run function.
  * Collecting and storing the results of each execution:

    * Success and failure information, such as the error message, error type, and line of code
    * Execution time
    * Logs
    * Metrics

For information about how to view execution results, see [Explore synthetic monitor results](https://docs.cloud.google.com/monitoring/synthetic-monitors/explore).




## Monitor and view results

You can observe the results of your synthetic monitors and uptime checks in the Google Cloud console:

  * For synthetic monitors, go to the **Synthetic monitors** page.
  * For uptime checks, go to the **Uptime checks** page.



To be notified when a synthetic monitor or uptime check fails, create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts) by using the Google Cloud console or the Google Cloud CLI.

**Tip:** If you create the alerting policy from the details page of a synthetic monitor or an uptime check, then most of the fields of the alerting policy are preconfigured.

## Troubleshooting failures

To assist you with troubleshooting, the request headers and logged data include the ID of the associated synthetic monitor or uptime check. For more information, see [Troubleshoot synthetic monitors or uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/troubleshoot).

## Data regionality

Don't use synthetic monitors or uptime checks when you have set up [Assured Workloads](https://cloud.google.com/security/products/assured-workloads) because you have data-residency or [Impact Level 4 (IL4)](https://cloud.google.com/security/compliance/disa) requirements.

Cloud Monitoring doesn't guarantee that the data in the uptime check request is kept in a specific geographic location.

For synthetic monitors that depend on a Cloud Run function, you can specify the region where your Cloud Run function is deployed. However, your function can be invoked from any region that is supported by the uptime check servers. This behavior isn't configurable.

## VPC Service Controls perimeters

When a Google Cloud project is in an enabled VPC Service Controls perimeter, the following behavior applies:

  * **Private uptime checks** : You can create, modify, view, and delete [private uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks).

  * **Public uptime checks and synthetic monitors** : You can't create or modify public uptime checks or synthetic monitors. However, any checks or synthetic monitors that existed before the Google Cloud project was added to the perimeter continue to operate, and you can still view and delete them.




## Pricing

To learn about pricing for Cloud Monitoring, see the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

## Limits

The following limits apply to your use of synthetic monitors:

Category | Value  
---|---  
Uptime checks [per metrics scope ](https://docs.cloud.google.com/monitoring/settings)* | 100  
Maximum number of [ICMP pings](https://docs.cloud.google.com/monitoring/uptime-checks#ping) per public uptime check | 3  
Synthetic monitors [per metrics scope ](https://docs.cloud.google.com/monitoring/settings) | 100†  
*This limit applies to the number of uptime-check configurations. Each uptime-check configuration includes the time interval between testing the status of the specified resource.  
†For information about how to increase this limit, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).  


## What's next

  * For information about uptime checks, see the following documents:

    * [Create public uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks)
    * [Create private uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks)
    * [Create alerting policies for uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/uptime-alerting-policies)
    * [List uptime-check server IP addresses](https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks)
  * For information about synthetic monitors, see the following documents:

    * [Create a synthetic monitor](https://docs.cloud.google.com/monitoring/synthetic-monitors/create)
    * [Create a broken-link checker](https://docs.cloud.google.com/monitoring/synthetic-monitors/broken-links)
    * [Manage synthetic monitors](https://docs.cloud.google.com/monitoring/synthetic-monitors/manage)
    * [Explore synthetic monitor results](https://docs.cloud.google.com/monitoring/synthetic-monitors/explore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
