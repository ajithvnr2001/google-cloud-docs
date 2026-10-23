---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshooting/
title: Troubleshoot the Ops Agent \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:48.968561+00:00
---

# Troubleshoot the Ops Agent  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Troubleshoot the Ops Agent Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The `localhost:2020/api/v1/metrics` endpoint mentioned at 3:18 in this video is no longer available in the Ops Agent. For other options, see [Agent is running but data is not ingested](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-run-ingest#data-not-ingested).

This document describes resources available to help you troubleshoot problems with the installation, start-up, and running of the Ops Agent. Troubleshooting information is organized into the following sections:

  * [Find troubleshooting information](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-find-info): This document describes where can you find information that can help you determine what the problem is.

  * [Troubleshoot credentials ](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-credentials): This document describes what to do when you encounter authorization or credentials problems with the Ops Agent running on Compute Engine VMs.

  * [Troubleshoot installation and start-up](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-install-startup): This document describes what to do if the installation of the agent fails, or if the agent installs but fails to start.

  * [Troubleshoot data ingestion](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-run-ingest): This document describes what to do when the Ops Agent is running, but logs or metrics are not being ingested into Cloud Logging or Cloud Monitoring as you expect.




For information about using the Ops Agent on Bare Metal Solution servers, see [Set up Ops Agent for Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs/set-up-ops-agent-for-bms).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
