---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/remote-agent-scaling-strategy/
title: Remote Agent scaling strategy \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:03:01.173149+00:00
---

# Remote Agent scaling strategy  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/remote-agent-scaling-strategy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Remote Agent scaling strategy

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document provides a detailed overview of the scalability of the Google Security Operations platform. It outlines the performance metrics for different agent configurations, demonstrating the Remote Agent framework's ability to handle high volumes of traffic with minimal infrastructure. The data presented reflects average results from a 10-minute end-to-end flow test.

## Prerequisites

  * **Connector or Action Execution Time (avg)** : 7-10 seconds
  * **Connector or Action Result Size (avg)** : 500 KB-1 MB
  * **Request** : An end-to-end flow of sending a request to the agent and getting the response back into Google SecOps. 

A single request equals a single action execution or a single connector run.




## Basic agent

The basic agent consists of 4 cores, 8 GB RAM, and 100 GB storage.

  * **Actions Rate** : 96 actions per minute
  * **Connectors Rate** : 96 runs per minute 

For example, 16 connectors, each connector runs every 10 seconds and returns a result.

  * **Combined Rate** : 96 requests per minute 

For example, 60 actions + 6 connectors, each connector runs every 10 seconds and returns a result.




## Scaled up agent

The scaled up agent consists of 8 cores, 16 GB RAM, and 100 GB storage.

  * **Actions Rate** : 144 actions per minute (completed full run)
  * **Connectors Rate** : 144 runs per minute 

For example, 24 connectors, each connector runs every 10 seconds and returns a result.

  * **Combined Rate** : 144 requests per minute 

For example, 90 actions + 9 connectors, each connector runs every 10 seconds and returns a result.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
