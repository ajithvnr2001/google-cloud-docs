---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-high-availability-for-remote-agents/
title: Deploy high availability for Remote Agents \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:15.470626+00:00
---

# Deploy high availability for Remote Agents  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-high-availability-for-remote-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy high availability for Remote Agents

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes how to configure a secondary Remote Agent as a backup to achieve high availability. By doing so, it eliminates a single point of failure in your execution environment.

## Failover mechanism and configuration

To ensure system resilience, the following rules apply:

  * **Automatic takeover** : If the primary agent becomes unavailable, the secondary agent automatically takes over the remote execution of actions, jobs, and connectors after a 30-second downtime.
  * **Task failure** : If the primary agent fails during a task execution, that specific task fails and must be manually re-run. All other pending tasks are immediately routed to the secondary agent.



## Set up high availability

Follow these steps to configure a secondary agent for high availability: 

  1. Go to **SOAR settings** > **Advanced** > **Remote Agents**.
  2. On the primary agent, click **View more** to view the agent's details.
  3. Click **Add secondary agent**.
**Note** : You can create one secondary agent for each primary agent. You can't use the same secondary agent for two different primary agents. To update the primary agent to the latest version, click **Update**. 

If your connectors are an older version, you must redeploy them to support the high availability configuration. For more information, see [Redeploy connectors.](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/redeploy-connectors-remote-agents)

     1. To update the primary agent to the latest version, click **Update**
     2. If your connectors are an older version, you must deploy them to support high availability. For more information, see [Redeploy connectors](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/redeploy-connectors-remote-agents). 
  4. Follow the process to set up a secondary agent (using either manual installation or Docker).

  5. Check the status of the secondary agent on the **Remote Agents** page, under the **High Availability** column.




## Operational notes (high availability)

This section details the system's operational behavior following the high availability setup, including the _failover rules for configuration deployment_ and the _default notification settings_ for agent status and downtime.

### Failover and configuration

  * **Primary agent focus** : After setting up high availability, continue to interact and work primarily with the designated Primary Agent across the platform.
  * **Secondary configuration role** : If the primary agent is inactive, the secondary agent automatically becomes active to ensure any configuration deployment tasks are completed successfully.



### Agent notifications

  * **Default behavior** : Agent notifications are enabled by default for events, such as new agent versions and agent downtime.
  * **Downtime trigger** : Notifications for agent downtime are specifically triggered when a Remote Agent has been down for more than 90 seconds.
  * **Opt-out** : You can opt out of these notifications at any time from your user preferences.



For more detailed information on configuring notifications, see [Agent notifications](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/what-is-a-remote-agent#agent-notifications).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
