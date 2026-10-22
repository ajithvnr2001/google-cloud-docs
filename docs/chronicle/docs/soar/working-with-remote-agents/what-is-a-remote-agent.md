---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/what-is-a-remote-agent/
title: Remote agents overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:25.223464+00:00
---

# Remote agents overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/what-is-a-remote-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Remote agents overview

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

The Remote Agent is a lightweight application installed on your remote environment. It connects to the Google Security Operations platform, giving your security team access to execute actions and playbooks on the remote environment.

The agent communicates with Google SecOps through the Publisher, a managed proxy server. This connection automatically syncs the agent with the Google SecOps platform, fetching and executing tasks from configured connectors and integrations.

The Remote agent securely connects a cloud Google SecOps instance to remote sites. This provides Managed Security Service Provider (MSSP) and enterprise SOC with the following capabilities:

  * Execute actions and playbooks on remote sites directly from Google SecOps.
  * Pull alerts and security data from remote sites with remote connectors.
  * Connect to remote networks to pull data for incident response purposes.



## Infrastructure

The Remote Agent infrastructure consists of the following two main components:

  * **Google SecOps platform** : Deploy Google SecOps platform to consolidate all security alerts in one place, and orchestrate security and network products with automated workflows.
  * **Google SecOps agent** : Deploy a Remote Agent on the remote site. The agent pulls new tasks from Google SecOps, executes remotely (on the remote or separate network) and updates Google SecOps with the results.

**Note:** Enterprise and MSSP end-customers can deploy the agents. The agent can initiate communication with Google SecOps to get new commands and to send new alerts and data.

## Agent notifications

Agent notifications, such as alerts for new agent versions and agent downtime, are enabled by default. Notifications for agent downtime trigger when a Remote Agent has been down for more than 90 seconds. You can opt out of these notifications at any time from your user preferences.

For more information about downtime notifications and high availability, see [Deploy high availability in Remote Agents](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-high-availability-for-remote-agents).

### Opt out of notifications

To opt out of notifications, follow these steps:

  1. Click your user avatar > **User Preferences**.
  2. Click **Notifications**.
  3. Optional: Clear the **Remote Agent** checkbox to stop receiving notification alerts.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
