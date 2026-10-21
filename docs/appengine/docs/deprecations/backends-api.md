---
url: https://docs.cloud.google.com/appengine/docs/deprecations/backends-api/
title: App Engine Backends API Shutdown \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:56:21.663519+00:00
---

# App Engine Backends API Shutdown  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/deprecations/backends-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)



Send feedback 

#  App Engine Backends API Shutdown Stay organized with collections  Save and categorize content based on your preferences. 

The Backends API was originally introduced as way to provide non user-facing compute, with longer timeouts, different instance sizes, etc.

Beginning in 2014, we started recommending Modules, which were eventually renamed to Services. During that time, we added [backend instances](https://docs.cloud.google.com/appengine/docs/standard#instance_classes) (`B_*`) and [scaling controls](https://docs.cloud.google.com/appengine/docs/standard/python/config/appref#scaling_elements) to all Services, thus removing much of the need for a separate Backends API.

On **March 13, 2019** , we will shut down the Backends API and all existing Backend versions. You will no longer be able to deploy new Backends or modify existing Backends, and these versions will stop serving traffic.

## Migration

Please follow our migration guides for [Python](https://docs.cloud.google.com/appengine/docs/standard/python/modules/converting), [Java](https://docs.cloud.google.com/appengine/docs/standard/java/modules/converting), and [Go](https://docs.cloud.google.com/appengine/docs/standard/go/modules/converting) to convert your Backends to Services.

If you need to run code for longer than 60 seconds, consider migrating to [Cloud Tasks](https://docs.cloud.google.com/tasks) (10 minute timeout), [Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine), or [Compute Engine](https://docs.cloud.google.com/compute) (indefinite).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
