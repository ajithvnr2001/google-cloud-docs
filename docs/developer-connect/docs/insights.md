---
url: https://docs.cloud.google.com/developer-connect/docs/insights/
title: Developer Connect insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:52.410503+00:00
---

# Developer Connect insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Developer Connect insights Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Developer Connect insights is [generally available](https://cloud.google.com/products#product-launch-stages) in all regions except `australia-southeast1`, `europe-west6`, `europe-west8`, `europe-west9`, and `southamerica-east1`.

This document describes Developer Connect insights and what benefits insights can provide.

Developer Connect insights let you diagnose problems with your applications that might cause outages, and thus help you remediate those problems.

Developer Connect insights are log entries from deployment events, sent from Developer Connect to Cloud Logging, to be consumed by Gemini Cloud Assist.

These insights provide Gemini Cloud Assist with information about application runtimes, artifacts deployed to those runtimes, the source files and dependencies used to build those artifacts.

## How does Developer Connect insights work?

Developer Connect Insights does the following:

  * When outages occur, Developer Connect insights can decrease the time it takes to discover the root cause and to recover
  * When there are problems with your running application in production, Developer Connect insights can help you identify root causes and quickly implement fixes



To make this happen, Developer Connect insights maps the relationships among the following components of your software development lifecycle (SDLC):

  * Application runtime environments
  * Application artifacts deployed to those runtimes
  * Build provenance



Developer Connect insights uses these relationships to aggregate relevant events from the SDLC and uses those relationships as context to help you solve problems and make decisions. Developer Connect insights logs these events to Cloud Logging.

## How can I use Developer Connect insights?

The following are some examples of information you can get from Developer Connect insights.

When outages and production problems occur, SREs can decrease the time it takes to discover the root cause and recover from the outage by getting answers to questions like these:

  * What changed for `my-app` in `us-east1` since Oct 10, 2024 10:10:10 EST?

  * Which artifacts were deployed, and when?

  * When were the artifacts built? From which source, and from which commits?

  * What deployments might have caused the production issue we're seeing?

  * Which artifacts, deployed to which application runtimes, have been affected by a deployment?




## What do I need in order to use Developer Connect insights?

Developer Connect insights requires the following Google Cloud products and tools:

  * An App Hub application (optional)

If you choose to scope your Developer Connect insights configuration to an App Hub application, you need an App Hub application.

Developer Connect insights supports all App Hub [setup models](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models) for applications. We recommend using a [folder configured for application management](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder) so that you can use Gemini Cloud Assist and other [application-centric features](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud)

  * A Google Cloud project (optional)

You can choose to scope the Developer Connect insights configuration to a Google Cloud project, instead of an App Hub application. This doesn't need to be the same project in which you create the Developer Connect insights configuration resource.

  * Developer Connect

You need to enable the Developer Connect API.

  * Build provenance

Your container image must have a corresponding build provenance that Developer Connect insights can find. See [Set up Developer Connect Developer Connect insights](https://docs.cloud.google.com/developer-connect/docs/set-up-insights#additional_prerequisites) for more information, including the sources from which Developer Connect insights can retrieve provenance.

  * Gemini Cloud Assist

You can enable Gemini Cloud Assist to use Developer Connect insights with Gemini Cloud Assist investigations. Developer Connect insights adds application deployment events to the Gemini Cloud Assist investigation context.




## What runtime environments does Developer Connect insights support

Developer Connect insights supports Google Kubernetes Engine and Cloud Run only.

## What's next

  * [Configure](https://docs.cloud.google.com/developer-connect/docs/set-up-insights) Developer Connect insights
  * Learn how to [use Developer Connect insights](https://docs.cloud.google.com/developer-connect/docs/use-insights)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
