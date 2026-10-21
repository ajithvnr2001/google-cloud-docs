---
url: https://docs.cloud.google.com/stackdriver/docs/deprecations/mon-agent-install/
title: Legacy installation scripts for the Cloud Monitoring agent \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:25.348140+00:00
---

# Legacy installation scripts for the Cloud Monitoring agent  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/deprecations/mon-agent-install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Legacy installation scripts for the Cloud Monitoring agent Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** There will be no new feature development or support for new operating systems for the legacy Monitoring agent. We recommend that you use the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent) for new workloads and eventually transition your existing VMs to use the Ops Agent. We strongly recommend against using the Monitoring agent on Windows. 

The legacy installation scripts, `stack-install.sh` and `install-monitoring-agent.sh`, are deprecated and have been decommissioned.

  * `stack-install.sh` is not supported and cannot be used to install any version of the Cloud Monitoring agent.
  * `install-monitoring-agent.sh` is no longer available and cannot be used to install any version of the Cloud Monitoring agent.



You must migrate to the new installation script as soon as possible. For more information, refer to [Installing the Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation).

After migrating to the new script, you can temporarily pin to agent version 5.x.x to gauge the impact of the breaking changes in version 6.0.0 and later.

## Shutdown timetable

The following table lists the shutdown schedule for the legacy installation scripts for the Cloud Monitoring agent:

Event | Date  
---|---  
Legacy installation scripts deprecated | April 28, 2020  
Legacy installation scripts decommissioned | February 17, 2022  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
