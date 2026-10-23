---
url: https://docs.cloud.google.com/agent-registry/quickstart-register-agent/
title: Quickstart: Register an agent \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:15.916317+00:00
---

# Quickstart: Register an agent  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/quickstart-register-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Quickstart: Register an agent Stay organized with collections  Save and categorize content based on your preferences. 

Registering an agent in Agent Registry lets you turn an isolated component into a discoverable part of your AI ecosystem. By publishing your agent's [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a), you help other developers and orchestrator agents in your organization find and reuse your work.

In this quickstart, you manually register a mock agent in Agent Registry using the Google Cloud console. For more information about agent registration mechanisms in Agent Registry, see [Register agents](https://docs.cloud.google.com/agent-registry/register-agents).

## Before you begin

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. Get [the project ID](https://support.google.com/googleapi/answer/7014113) for the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled.



### Required roles

To get the permissions that you need to register agents in Agent Registry, ask your administrator to grant you the [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) IAM role on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Register a mock agent

To try out Agent Registry, you can manually register a mock agent by pasting a sample [Agent2Agent (A2A) Agent Card](https://agent2agent.info/docs/concepts/agentcard/).

Follow these steps to register the agent:

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

If prompted, click **Enable** to enable the Agent Registry API.

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Agents** tab.

  4. Click **Add agent**.

  5. In the **Agent details** panel, enter the following details:

     * **Type** : select **A2A**.
     * **Region** : select `global` (Global).
  6. Select the **Paste JSON** tab.

  7. Paste the following sample Agent Card content:
         
         {
           "supportedInterfaces": [
             {
               "url": "https://example.com/mock-travel-agent",
               "protocolBinding": "HTTP+JSON",
               "protocolVersion": "1.0.0"
             }
           ],
           "name": "mock-travel-agent",
           "description": "A mock agent that plans travel itineraries.",
           "version": "1.0.0",
           "capabilities": {
             "streaming": false,
             "pushNotifications": false
           },
           "defaultInputModes": ["text/plain"],
           "defaultOutputModes": ["text/plain"],
           "skills": [
             {
               "id": "BookFlight",
               "name": "BookFlight",
               "description": "Books a flight to a destination.",
               "tags": ["travel", "booking"]
             },
             {
               "id": "SearchHotels",
               "name": "SearchHotels",
               "description": "Searches for hotels in a destination city.",
               "tags": ["travel", "accommodation"]
             }
           ]
         }
         

  8. Click **Save**.




Agent Registry processes the Agent Card and registers the agent.

## Verify the registration

To confirm that your mock agent was registered successfully, do the following:

  1. On the **Agents** tab, locate the mock agent in the list.
  2. Click the agent's name to view its details.
  3. Verify that the `BookFlight` and `SearchHotels` A2A skills appear on the **Overview** tab.



## Clean up

To avoid leaving mock resources in your project, delete the registered agent:

  1. On the **Agents** tab, locate the mock agent in the list.
  2. Click the more_vert **More options** menu in the **Actions** column of the mock agent, and select **Delete**.
  3. In the confirmation dialog, enter `DELETE` to confirm the action.
  4. Click **Delete**.



## What's next

  * Learn how to [manage registered agents](https://docs.cloud.google.com/agent-registry/manage-agents).
  * Learn about [automatic registration](https://docs.cloud.google.com/agent-registry/automatic-registration), the recommended method to register agents deployed to managed runtimes.
  * Read [Agent Registry key concepts](https://docs.cloud.google.com/agent-registry/concepts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
