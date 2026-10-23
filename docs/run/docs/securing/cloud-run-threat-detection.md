---
url: https://docs.cloud.google.com/run/docs/securing/cloud-run-threat-detection/
title: Use Cloud Run Threat Detection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:54.887037+00:00
---

# Use Cloud Run Threat Detection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/securing/cloud-run-threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Use Cloud Run Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview) is a built-in service of Security Command Center that continuously monitors the state of Cloud Run resources to detect the most common runtime attacks. If Cloud Run Threat Detection detects an attack, it generates a finding in Security Command Center in near-real time.

Cloud Run Threat Detection's runtime detectors monitor the scanned resources for suspicious binaries and libraries and uses natural language processing (NLP) to detect malicious Bash and Python code. These runtime detectors support only Cloud Run resources that run on the [second generation execution environment](https://docs.cloud.google.com/run/docs/about-execution-environments). If you don't specify an execution environment and use Cloud Run Threat Detection, Cloud Run sets the second generation environment by default for your resources.

For instructions on how to configure threat detection in your Cloud Run resources, see [Use Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/use-cloud-run-threat-detection) in the Security Command Center documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
