---
url: https://docs.cloud.google.com/model-armor/retry-strategy/
title: Retry strategy \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:37:54.028849+00:00
---

# Retry strategy  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/retry-strategy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Retry strategy Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for retrying failed requests to the Model Armor API.

For requests that are safe to retry, we recommend using truncated exponential backoff with introduced jitter.

## Overview of truncated exponential backoff

Each request to the Model Armor API can succeed or fail. If your application retries failed requests without waiting, it might send a large number of retries to Model Armor in a short period of time. As a result, you might exceed [quotas and limits](https://docs.cloud.google.com/model-armor/quotas) that apply to every Model Armor resource in your Google Cloud project. 

To avoid triggering this issue, we strongly recommend that you use [truncated exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) with introduced [jitter](https://en.wikipedia.org/wiki/Jitter), which is a standard error-handling strategy for network applications. In this approach, a client periodically retries a failed request with exponentially increasing delays between retries. A small, random delay, known as jitter, is also added between retries. This random delay helps prevent a synchronized wave of retries from multiple clients, also known as the [thundering herd problem](https://en.wikipedia.org/wiki/Thundering_herd_problem). 

## Exponential backoff algorithm

The following algorithm implements truncated exponential backoff with jitter: 

  1. Send a request to Model Armor. 
  2. If the request fails, wait 1 + `random-fraction` seconds, then retry the request. 
  3. If the request fails, wait 2 + `random-fraction` seconds, then retry the request. 
  4. If the request fails, wait 4 + `random-fraction` seconds, then retry the request. 
  5. Continue this pattern, waiting 2n \+ `random-fraction` seconds after each retry, up to a `maximum-backoff` time. 
  6. After `deadline` seconds, stop retrying the request. 



Use the following values as you implement the algorithm: 

  * Before each retry, the wait time is `min((2n + random-fraction), maximum-backoff)`, with `n` starting at 0 and incremented by 1 for each retry. 
  * Replace `random-fraction` with a random fractional value less than or equal to 1. Use a different value for each retry. Adding this random value prevents clients from becoming synchronized and sending large numbers of retries at the same time. 
  * Replace `maximum-backoff` with the maximum amount of time, in seconds, to wait between retries. Typical values are 32 or 64 (25 or 26) seconds. Choose the value that works best for your use case. 
  * Replace `deadline` with the maximum number of seconds to keep sending retries. Choose a value that reflects your use case. For example, in a continuous integration/continuous deployment (CI/CD) pipeline that is not highly time-sensitive, you might set `deadline` to 300 seconds (5 minutes). 



## Types of errors to retry

Use this retry strategy for all requests to the Model Armor API that return the error codes `500`, `502`, `503`, or `504`.

Optionally, you can use this retry strategy for requests to the Model Armor API that return the error code `429`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
