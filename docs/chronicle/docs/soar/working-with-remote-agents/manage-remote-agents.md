---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/manage-remote-agents/
title: Monitor and manage Remote Agents \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:13.045965+00:00
---

# Monitor and manage Remote Agents  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/manage-remote-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor and manage Remote Agents

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document provides a reference for the **Remote Agents** page, detailing the information displayed for agent monitoring and the actions available for agent lifecycle management.

  * **Name** : The configured name of the agent.
  * **Agent Status** : The current operational state of the agent. 
    * **Live** : The agent is active and communicating.
    * **Failed** : The agent has experienced a connection or operational issue.
    * **Pending** : The agent has been provisioned but isn't yet connected.
    * **Disabled** : The agent has been manually disabled and can't perform tasks.
  * **Environment** : The specific environment associated with the agent.
  * **Agent Version** : The current version of the agent software.
  * **Last Communication** : The timestamp of the agent's last successful communication.
  * **High Availability** : Displays if the agent is configured as a primary or secondary high availability component. For more details about HA, see [Deploy high availability for Remote Agents](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-high-availability-for-remote-agents).
  * **Available update** : Notification if a new version of the agent software is available to install.



## Available management actions

For more detailed information and actions, click more_vert **More**.

  * **Send installer/docker command** : Generates a unique download link for the agent installer or the Docker command string, necessary for deployment on a remote machine.
  * **Edit** : Modify the agent's name or its log level.
  * **Download logs** : Download agent's log for troubleshooting.
  * **Disable agent** : Temporarily prevent the agent from running actions or connectors and stop it from communicating with Google Security Operations.
  * **Delete agent** : Permanently remove the agent from the platform.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
