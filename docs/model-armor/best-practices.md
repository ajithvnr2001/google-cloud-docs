---
url: https://docs.cloud.google.com/model-armor/best-practices/
title: Best practices for scaling and high traffic \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:05.000645+00:00
---

# Best practices for scaling and high traffic  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Best practices for scaling and high traffic Stay organized with collections  Save and categorize content based on your preferences. 

As you scale your AI applications and encounter high traffic volumes, it's crucial to design for resilience and performance. This section outlines best practices for using Model Armor effectively in demanding environments.

## Quotas and system limits

Model Armor includes quotas and system limits to ensure fair usage and system stability.

  * Request quota increases: If you anticipate higher traffic, contact [Cloud Customer Care](https://cloud.google.com/support-hub) to request a Model Armor API quota adjustment.
  * Understand system limits: Design your application to handle these limits gracefully, potentially by chunking larger inputs if necessary. For specific values, see [Quotas and system limits](https://docs.cloud.google.com/model-armor/quotas).



## Design for high traffic and resilience

  * Client-side retries with exponential backoff: Implement robust error handling in your clients. For errors that you can retry, for example, rate limits or server errors, use an exponential backoff strategy. This prevents overwhelming the service during transient issues. For more information, see [Retry strategy](https://docs.cloud.google.com/model-armor/retry-strategy).
  * Caching strategies: If applicable, cache Model Armor responses for identical prompts, especially for common or less sensitive interactions. Be mindful of data freshness and security implications when caching.
  * Asynchronous processing: For non-interactive workloads, consider processing requests asynchronously. Queue requests and process them at a rate that respects API limits and smooths out traffic spikes.
  * Graceful degradation: Design your application to handle potential Model Armor unavailability or errors. Consider implementing a fallback mechanism or temporarily bypassing certain checks while logging the failure.



## Optimize performance

  * Minimize payload size: Only send the necessary data to Model Armor for analysis. Avoid unnecessarily large prompts or files.
  * Optimize template configuration: Configure your Model Armor templates to only include the filters and settings essential for your use case. Enabling unnecessary detectors can increase latency.
  * Keep the application, data, and requests in the same region: Deploy your application and use Model Armor endpoints in the same region to minimize network latency. For more information, see [Model Armor locations](https://docs.cloud.google.com/model-armor/locations).



## Monitoring and alerting

  * Set up alerts: Configure [alerts](https://docs.cloud.google.com/monitoring/alerts) in Cloud Monitoring to notify you when you are approaching quota limits or experiencing high error rates from the Model Armor API.
  * Analyze logs: Use Cloud Logging to analyze Model Armor usage patterns, errors, and performance metrics. Analyzing logs can help identify bottlenecks or areas for optimization. For more information, see [Filter logs](https://docs.cloud.google.com/model-armor/configure-logging#filter-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
