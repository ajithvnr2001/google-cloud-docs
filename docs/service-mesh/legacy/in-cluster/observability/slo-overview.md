---
url: https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/slo-overview/
title: Service level objectives overview \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:27.899734+00:00
---

# Service level objectives overview  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/slo-overview/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Service level objectives overview

Service Level Objectives (SLOs) are a core tool in the Google service monitoring toolkit. SLOs can give you a concise and low-noise signal as to the overall health of your services. Cloud Service Mesh lets you set SLOs for your services, and monitor and alert on your services in terms of those SLOs.

To monitor the health of a service, you need to understand which behaviors matter for that service and how to measure and evaluate those behaviors. A service level indicator (SLI) is a quantitative measure of some aspect of the service. Typical SLIs are:

  * Latency: How long it takes to return a response to a request, usually measured in milliseconds (ms). Latency is typically presented as an aggregate. That is, the raw data is collected over a period of time and calculated as percentiles. Cloud Service Mesh displays a Latency graph on the **Metrics** page for each of your services. The Latency graph shows you the latency over time, which can help you determine a latency threshold or upper bound for a service.
  * Availability: The fraction of the time that a service responds successfully. This is typically presented as a ratio of the number of successful responses over the total number of responses. The Error rate graph on the **Metrics** page can help you determine the availability of each service.



An SLO is a target value for a service level that is measured by an SLI. An SLO can be represented as: `SLI ≤ upper_bound` or `SLI ≥ lower_bound`. SLOs are measurable goals for performance over a period of time. For example, you might have requirements like the following for some of your services:

  * Latency can exceed 300ms in only 5 percent of the requests over a rolling 30-day period.
  * The system must have 99% availability measured over a calendar week.



You can set and view SLOs for your services based on their telemetry data on the **Health** page. You can then create alerts in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/alerts) to warn you if a service isn't performing as expected.

## What's next

  * Learn more about SLOs from Site Reliability Engineering at Google:

    * [Site Reliability Engineering](https://sre.google/sre-book/service-level-objectives/)
    * [The Site Reliability Workbook](https://sre.google/workbook/implementing-slos/)
  * [Designing SLOs](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/design-slo)

  * [Creating SLOs](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/create-slo)

  * [Monitoring SLOs](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/monitor-slo)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
