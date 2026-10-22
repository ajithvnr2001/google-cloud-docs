---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-remote-agents/
title: Perform a standard upgrade of Remote Agents \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:06.193160+00:00
---

# Perform a standard upgrade of Remote Agents  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-remote-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Perform a standard upgrade of Remote Agents

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to perform a **standard** upgrade of Remote Agents. The standard upgrade procedure may take up to five minutes.

For information on performing a **major** upgrade of Remote Agents, which requires extra steps, see:

  * [Perform a major upgrade of a Docker image ](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-docker-image)
  * [Perform a major upgrade using installer for RHEL ](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-requirements-for-rhel)
  * [Perform a major upgrade using installer for CentOS ](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-requirements-for-centos)
  * [Perform a major upgrade of a Podman image ](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image)



## Upgrade Remote Agent (1.4.2 and above)

  1. Go to **Soar Settings** > **Advanced** > **Remote Agents**.
  2. Click **Update Available**.
  3. Click info **Info** to confirm the updated version. 



## Upgrade Remote Agent (1.4.1 and below)

  1. Go to **Settings** > **Advanced** > **Remote Agents**.
  2. Double-click the agent.
  3. Disable the agent and then refresh the page.
  4. After the status is disabled, double-click the agent to enable it.
  5. When the agent is live, click info to confirm the updated version. 

**Note:** When you use high availability, upgrade the primary agent first, then the secondary agent.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
