---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/real-time-service/
title: Real-time service \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:42.260912+00:00
---

# Real-time service  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/real-time-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Real-time service

To provide better clarity on how Manufacturing Data Engine (MDE) is processing an ingested tag, the real-time service was introduced in release v1.4.0 onwards to give the users better real-time insights on which tags are being ingested and at what rate. The real-time service tracks each tag and it is able to store the last three values of the most recent tags that MDE observed. You can also check the relevant statistics of a recently observed tag such as the last minute, five minutes, and 30 minutes processing rate.

If you are using the Manufacturing Connect (MC) web interface, this feature is visible after you hold the mouse over a particular tag row in the tags screen:

![MC web interface to see real-time service](https://docs.cloud.google.com/static/manufacturing-data-engine/images/real-time-service.png)

## Known limitations

To optimize the cost of the deployment, this service utilizes the current infrastructure elements such as the Redis instance that is used throughout MDE. As a result, the service can only keep track of a limited number of tags based on the size of your deployment:

  * 1000 tags for small deployment
  * 2000 tags for medium deployment
  * 5000 tags for large deployments



The Real-Time service automatically keeps track of the most recent list of tags.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
