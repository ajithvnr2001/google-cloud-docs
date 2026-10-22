---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/overview/
title: Overview \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:07.201376+00:00
---

# Overview  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

This section reviews the concept of service-level indicators (SLIs), defines what makes for a good or useful SLI, and provides examples of SLI implementations for selected services. This page is intended for people who want examples that implement service-specific SLIs.

## Introduction to SLIs

The reliability of a service is an abstract notion; what _reliability_ means depends on the service and the needs of its users. A _service-level indicator_ (SLI) is a measure of that reliability to be used for both communicating about the reliability of the service and to manage the service.

SLIs are measured over a time window. The size of the window typically depends upon the decision the information is being used to make. For example, you might measure a single SLI in the following ways:

  * Over the most recent hour, for creating alerting policies.
  * Over weeks, for making tactical decisions.
  * Over months, for making strategic decisions.



We recommend 28 days as a starting point for measuring your SLI; this value provides a good balance between the strategic and tactical use cases.

For more information, see the following sections of the [ Site Reliability Engineering Workbook](https://landing.google.com/sre/workbook/toc):

  * [Implementing SLOs](https://landing.google.com/sre/workbook/chapters/implementing-slos)
  * [Alerting on SLOs](https://landing.google.com/sre/workbook/chapters/alerting-on-slos)



## Properties of a good SLI

We consider "good" SLIs to be those measures that meet the following criteria:

  * **SLIs are good proxy measures for user happiness.**

A good SLI correlates strongly with user happiness. You use the SLI as the basis for a _service-level objective_ (SLO), a threshold set on the SLI. You set the SLO so that, when the SLI is within a defined range, most of your users are happy. For this relationship to hold, the SLI must be a good proxy measure for user happiness.

If the SLI is a good proxy for user happiness, then when there is an event that affects user happiness, the SLI changes in some direction. Likewise, when there are no events that affect user happiness, the SLI doesn't change.

  * **SLIs scale monotonically and linearly with user happiness.**

A good SLI scales monotonically, and linearly, with user happiness. If the SLI improves, then user happiness improves. Similarly, if the SLI decreases, then user happiness decreases. The amount of improvement in the value of a good SLI corresponds to the amount of improvement in user happiness.

  * **SLIs produce measurements that range from 0% to 100%.**

A good SLI produces a performance measurement that ranges from 0% to 100%: this range is intuitive and easy to work with. For example, SLI performance of 100% means that everything is working, and SLI performance of 0% means that nothing is working.

Having a SLI that ranges from 0% to 100% makes setting a SLO on the SLI easy and clear: assign a percentage target such as 99.9%, and the SLI performance must be at or higher than that target for the service to be meeting its SLO.




## Promises

One way of implementing an SLI that has these properties is to think of the SLI in terms of promises made to your users. By counting the promises that you made and upheld over a time window, you can derive a number that ranges from 0% to 100%. Such SLIs also translate well into error budgets: for a given SLO, your error budget is the number of promises you can fail to uphold over a time window while still meeting your SLO.

Examples of promises include:

  * To return a response with an HTTP `200` status code to a customer's request.
  * To respond to a gRPC request in under 100 ms.
  * To complete the "Create Virtual Machine" workflow successfully.
  * To serve data that has been refreshed within the past 10 minutes.
  * To start running the scheduled batch job within one minute of its starting time.



## SLI specifications and implementations

An SLI _specification_ is _what_ you want to measure. The specification doesn't include the exact technical details of _how_ you are going to measure it. For example, the following is a specification of an SLI for page-loading time:

  * The percentage of home page requests that load in under 100 ms.



There can be many ways to measure an SLI, each with trade-offs and benefits. The ways of measuring the SLI are the SLI **Implementations**. For example, you might implement the page-loading specification as one of the following:

  * The latency field of the application server's request log.
  * Metrics exported by the application server.
  * Metrics exported by a load balancer in front of the application servers.
  * A black-box monitoring service that sends artificial requests to the system and times how long it takes to receive valid responses.
  * Application-specific code executed in the customer's browser that records timing information and sends it back to a collection service.



Each of these choices involves trade-offs between the following characteristics:

  * Fidelity: how accurately it captures user experience.
  * Coverage: what proportion of user interactions are measured.
  * Cost: the amount of both money and engineering time required to build and maintain the solution.



Fidelity to user experience usually improves when the SLI is measured closer to the user. For example, the implementation that uses code in the user's browser results in a more accurate measurement of latency than the latency perceived by the user or by other measurement choices.

The tradeoff is that the browser-based measurement also includes any latency introduced by the user's connection to your service. For example, when a service is used over the public internet, this latency might vary significantly with geographic location or network conditions.

The result is that the browser-based signal is a good proxy for user happiness. However, this signal might not provide actionable information you can use to improve the reliability of your service.

For information about combining multiple measurements to balance this tradeoff, see this [post from The Telegraph](https://medium.com/the-telegraph-engineering/putting-customers-first-with-slis-and-slos-part-2-6b5c2452aecd).

## Bucketing

You might need multiple SLIs for a service when your service performs different kinds of work for different users, or when it performs a particular task with different possible outcomes.

### Different tasks

Services that perform multiple types of work, for different categories of users, and in which each type of work influences user happiness differently benefit from multiple SLIs.

For example, if your service handles both read and write requests, users performing those tasks might have different requirements:

  * Read requests have to be fast.
  * Write requests have to be successful.



To capture these different requirements, your SLI must be able to distinguish between these two cases. Typically, the SLI metric has a label that you can use to classify values into one of several buckets.

### One task with different outcomes

Services that perform a single type of work but where user expectations differ based on the response benefit from multiple SLIs.

For example, if your service offers only read access to data, users might have different tolerance for latency depending on the outcome of the request:

  * Users might be tolerant of errors that are returned quickly, because users can then immediately retry the request.
  * Users might be less tolerant of successful requests that take a long time.
  * Users are least tolerant of the worst-case scenario: requests that take a long time to return an error.



In this case, your latency SLI needs to be able to distinguish between successful and unsuccessful requests.

## What's next

For information about implementing SLIs for Google Cloud services using Google Cloud metrics, see the following:

  * [Using Cloud Load Balancing metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/lb-metrics)
  * [Using Google Cloud platform and service metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/platform-svc-metrics)
    * [Data storage and retrieval services](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/data-storage-metrics)
    * [Data-processing services](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/data-proc-metrics)



For information about implementing application-specific SLIs, see the following:

  * [Using logs-based metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/logs-based-metrics)
  * [Using Prometheus](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/prometheus)
  * [Using OpenCensus](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/open-census)



For an example that illustrates how to create a SLI for services that report custom metrics, see [Setting SLOs: observability using custom metrics](https://cloud.google.com/blog/products/management-tools/observability-using-custom-metrics).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
