---
url: https://docs.cloud.google.com/service-health/docs/incident-lifecycle/
title: Lifecycle of an incident \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:52.049316+00:00
---

# Lifecycle of an incident  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/incident-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Lifecycle of an incident Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how the Google Cloud Support team and product engineering team work together to resolve an incident and provide you with updates.

The following diagram shows the responsibilities of the product engineering and support teams.

![Lifecycle Diagram](https://docs.cloud.google.com/static/service-health/images/incident-lifecycle.svg)

The following sections explain these responsibilities.

## Detection

Google Cloud uses internal and synthetic monitoring to detect incidents. For more information, see [Chapter 6 of the Site Reliability Engineering book](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/).

## Initial response

When an incident is detected, the Google Cloud Service Health team manages customer communications. Initial notification of an incident is often sparse, frequently only mentioning the product in question. This is because we prioritize fast notification over detail. Detail can be provided in subsequent updates.

To provide you as much information as possible without overwhelming you with issues that don't affect you, different communication channels are used depending on the scope and severity of an issue:

![Comms Diagram](https://docs.cloud.google.com/static/support/docs/images/comms-diagram.png)

## Investigate

Product engineering teams are responsible for investigating the root cause of incidents. Incident management is often done by Site Reliability Engineers but might be done by software engineers or others, depending on the situation and product. For more information, see [Chapter 12 of the Site Reliability Engineering Book](https://landing.google.com/sre/sre-book/chapters/effective-troubleshooting/).

## Mitigation and fix

An issue is considered _fixed_ only when changes have been made that Google is confident will end the impact indefinitely. For example, the fix could be rolling back a change that triggered an incident.

While an incident is in progress, Service Health and the product team attempt to _mitigate_ the issue. Mitigation is when the impact or scope of an issue can be reduced, for example, by temporarily providing additional resources to a product suffering overload.

If no mitigation has been found, when possible, the Service Health team finds and communicates _workarounds_. Workarounds are steps that you can take to solve the underlying need despite the incident. A workaround might be to use different settings for an API call to avoid a problematic code path.

## Follow up

While an incident is ongoing, the Service Health team provides regular updates. Updates typically provide:

  * More information about the incident, such as error messages, zones or regions affected, which features are affected, or percentages of impact.

  * Progress towards mitigation, including any workarounds.

  * Timelines for communication, tailored to the incident.

  * Changes in status, such as when an incident is fixed.




## Retrospective

All incidents undergo an internal retrospective to fully understand the incident and identify reliability improvements that Google can make. These improvements are then tracked and implemented. For more information, see [Chapter 15 of the Site Reliability Engineering Book](https://landing.google.com/sre/sre-book/chapters/postmortem-culture/).

## Incident report

When incidents have very wide and serious impact, Google provides incident reports that outline the symptoms, impact, root cause, remediation, and future prevention of incidents. As with retrospectives, we pay particular attention to the steps that we take to learn from the issue and improve reliability. Google's goal in writing and releasing retrospectives is to be transparent and demonstrate our commitment to building stable products for our customers.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
