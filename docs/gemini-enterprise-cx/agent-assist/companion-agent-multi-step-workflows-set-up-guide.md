---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-multi-step-workflows-set-up-guide/
title: Multistep workflows set up guide \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:59.803680+00:00
---

# Multistep workflows set up guide  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-multi-step-workflows-set-up-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Multistep workflows set up guide Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature has limited access. Contact your Google Cloud representative to access private GA features.

Multistep workflows provide human agents with structured step-by-step instructions from the beginning till the end of a conversation. These workflows help agents stay oriented and tackle broader tasks at hand.

The following steps explain how to create a workflow, attach it to a companion agent and use it while conversing with the customer.

## Create a workflow

Follow these steps to create and publish a multistep workflow in the [Agent Assist console](https://agentassist.cloud.google.com/).

  1. Navigate to **Companion Agents** > **Workflows** > **Create workflow**.
  2. Enter following details: 
     * **Display name** : Enter a display name up to 63 characters.
     * **Description** : Add a description to specify when the companion agent should suggest this workflow. For example, _Use this workflow when a customer reports a damaged item and wants a replacement or refund_.
  3. Designate a starting step, then add the following steps and connect them with decision branches. 
     * Collect information
     * Tool call
     * Tell customer
     * Manual task
     * End workflow
  4. Use the simulator to test your draft workflow in sample customer chats.
  5. Click **Mark as version** and select **Set as live version** to use the live version.
  6. Navigate back to the **Companion Agents** page and select the companion agent you created.
  7. Select **End of utterance** as the companion agent trigger.
  8. Click **Add** in the **Workflows** section.
  9. Select the workflow you created and click **Add**.
  10. Click **Save**.



## Decision branching

You can guide how the workflow moves from one task to the next using one of the following two approaches:

  * **Default path** : The system automatically moves to the next standard step unless you set up a specific rule for a different direction.
  * **Conditional transition** : You can set rules so the workflow adapts based on what the customer chooses or says. For example, a rule can tell the workflow to automatically move to a refund step if the customer asks for money back.



## User guide

Follow these steps to use the multistep workflows feature.

  1. Start a conversation with the customer.
  2. Click the most relevant card to launch the workflow. The workflow displays a list of steps to carry out in a sequence and a completion status progress tracker.
  3. After you complete a step, it is automatically marked as completed and you can move on to the next step. You can go back to a previous step or restart the workflow from the beginning. You can also check suggested replies, edit entities, and run tools in the workflow window.
  4. After you complete all the steps, the message **Workflow completed** appears and the workflow collapses.
  5. Click **Exit** to dismiss any of the workflows.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
