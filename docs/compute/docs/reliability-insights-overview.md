---
url: https://docs.cloud.google.com/compute/docs/reliability-insights-overview/
title: Compute Reliability Insights overview \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:59.429558+00:00
---

# Compute Reliability Insights overview  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reliability-insights-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Compute Reliability Insights overview Stay organized with collections  Save and categorize content based on your preferences. 

Compute Reliability Insights offers a suite of features to enhance your Compute Engine workload reliability. This tool provides visibility into potential risks, enabling effective risk management through detailed solutions and proactive recommendations. 

This page provides conceptual information on Compute Reliability Insights. For more information on how to view and apply reliability recommendations, see [View and apply reliability recommendations](https://docs.cloud.google.com/compute/docs/view-and-apply-reliability-recommendations).

## Understand reliability risks

A reliability risk is a situation where the misconfiguration of Compute Engine features or settings could adversely affect the stability and availability of your infrastructure. This can occur in the following ways:

  * **Unexpected cascading failures** : An outage in one zone or region of Google's infrastructure could unexpectedly disrupt your resources in other zones or regions.
  * **External dependencies** : Your resources might rely on the availability of specific Compute Engine regions located outside of your primary resource location.



### Risk types

Compute Reliability Insights identifies a subset of potential risks in your workloads:

  * [Global DNS](https://docs.cloud.google.com/compute/docs/networking/zonal-dns#benefits) , which is a risk that occurs when your Compute Engine projects have the [internal DNS configuration](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names) set to `Global DNS`.



### Risk severity and priority

Compute Reliability Insights prioritizes your risks by using the following severity and priority definitions.

**Severity** | **Priority** | **Description**  
---|---|---  
High | P1 | A misconfiguration or setting that, when a regional outage occurs, **disrupts frequently used services** across multiple regions (for example, VM creation).  
Medium | P2 | A misconfiguration or setting that, when a regional outage occurs, **disrupts less critical services** across multiple regions (for example, instance template creation).  
  
## Telemetry and latency

Compute Reliability Insights relies on telemetry data to identify risks. Consider the following behavior when using this feature:

  * **New projects and inactive resources** : For projects created in the last 7 days or projects with inactive VMs, recommendations might not be available because the pipeline requires more telemetry data.
  * **Mitigation delay** : After you mitigate a risk, the Google Cloud console and API might continue to display the recommendation for up to 24 hours. This is because the ingestion pipeline runs every 24 hours to clear resolved recommendations.



## What's next

  * Learn how to view and apply [reliability recommendations](https://docs.cloud.google.com/compute/docs/view-and-apply-reliability-recommendations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
