---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/set-up-integrations-and-connectors/
title: Configure remote execution \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:28.750076+00:00
---

# Configure remote execution  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/set-up-integrations-and-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure remote execution

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document provides the procedures necessary to configure Google Security Operations components to run remotely using the deployed Remote Agent. After the Remote Agent is created, you must explicitly configure integrations, connectors, and jobs to use the new remote infrastructure.

## Set up integrations

Configure integrations to let manual and Playbook actions run on cases to execute remotely:

  1. Go to the Content Hub.
  2. Select the required environment.
  3. Select the required integration and click **Configure Integration**.
  4. Select **Run Remotely** and click **Save**.



You can run actions from this environment remotely, including manual and playbook actions.

## Set up connectors

You can assign any number of connectors to a Remote Agent:

  1. Go to **SOAR Settings > Ingestion > Connectors**.
  2. Click add **Create New Connector**.
  3. Select **Remote Connector**.
  4. Click **Create**.  

  5. Select the required environment.
  6. Select the required Remote Agent. The Remote Agent's status appears on the top of the page.



## Set up jobs

Before you set up jobs to run on the Remote Agents, complete these prerequisites:

  1. Go to the **Integrations Setup** page.
  2. Create a new instance configured to run remotely with this Remote Agent.
  3. Go to the **Permissions Groups** page and make sure you have the required permissions for the **Jobs Scheduler** page and for **Remote Agents**.



### Configure a remote job

  1. Go to **Response > Jobs Scheduler**.
  2. Click add **Create New Job**.
  3. Select **Remote Job**.
  4. Click **Create**.
  5. From the menu, select the required Remote Agent. Only agents configured with a remote instance will be available. 

Jobs can access information in all environments.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
