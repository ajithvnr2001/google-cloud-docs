---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/redeploy-agent/
title: Redeploy remote agents \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:14.231803+00:00
---

# Redeploy remote agents  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/redeploy-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Redeploy remote agents

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

You can redeploy a Remote Agent to copy all the integrations and connectors from one agent to another. For example, if you need to change your agent from an installer to a Docker image.

To redeploy the agent, Google recommends to create a new agent and then redeploy from an existing agent. 

  1. On the **Remote Agents** page, create a new Remote Agent and make sure it's live. For more information on creating new agents, see: 
     * [ Create agent with installer using RHEL](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-for-rhel)
     * [ Create agent with installer using CentOS](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-on-centos)
     * [ Create agent with Docker](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-docker)
  2. Click **Redeploy**.
  3. Select the source agent and the destination agent. A list of the integrations and connectors appears.
  4. Click **Redeploy**. After the successful redeployment, a small **Details** box appears next to the Remote Agent. 
  5. Click **Details** to view the redeployment details including the list of integrations and connectors. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
