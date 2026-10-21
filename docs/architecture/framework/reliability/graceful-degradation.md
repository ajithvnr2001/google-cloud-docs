---
url: https://docs.cloud.google.com/architecture/framework/reliability/graceful-degradation/
title: Design for graceful degradation \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:19.437214+00:00
---

# Design for graceful degradation  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/reliability/graceful-degradation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Design for graceful degradation Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-30 UTC

This principle in the reliability pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) provides recommendations to help you to design your Google Cloud workloads to fail gracefully.

This principle is relevant to the _response_ [focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas) of reliability.

## Principle overview

Graceful degradation is a design approach where a system that experiences a high load continues to function, possibly with reduced performance or accuracy. Graceful degradation ensures continued availability of the system and prevents complete failure, even if the system's work isn't optimal. When the load returns to a manageable level, the system resumes full functionality.

For example, during periods of high load, Google Search prioritizes results from higher-ranked web pages, potentially sacrificing some accuracy. When the load decreases, Google Search recomputes the search results.

## Recommendations

To design your systems for graceful degradation, consider the recommendations in the following subsections.

### Implement throttling

Ensure that your replicas can independently handle overloads and can throttle incoming requests during high-traffic scenarios. This approach helps you to prevent cascading failures that are caused by shifts in excess traffic between zones.

Use tools like [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee) to control the rate of API requests during high-traffic times. You can configure policy rules to reflect how you want to scale back requests.

### Drop excess requests early

Configure your systems to drop excess requests at the frontend layer to protect backend components. Dropping some requests prevents global failures and enables the system to recover more gracefully.With this approach, some users might experience errors. However, you can minimize the impact of outages, in contrast to an approach like _circuit-breaking_ , where _all_ traffic is dropped during an overload.

### Handle partial errors and retries

Build your applications to handle partial errors and retries seamlessly. This design helps to ensure that as much traffic as possible is served during high-load scenarios.

### Test overload scenarios

To validate that the throttle and request-drop mechanisms work effectively, regularly simulate overload conditions in your system. Testing helps ensure that your system is prepared for real-world traffic surges.

### Monitor traffic spikes

Use analytics and monitoring tools to predict and respond to traffic surges before they escalate into overloads. Early detection and response can help maintain service availability during high-demand periods.

[ Previous arrow_back  Detect potential failures by using observability  ](https://docs.cloud.google.com/architecture/framework/reliability/observability)

[ Next Perform testing for recovery from failures  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/reliability/perform-testing-for-recovery-from-failures)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-30 UTC."],[],[]] 
