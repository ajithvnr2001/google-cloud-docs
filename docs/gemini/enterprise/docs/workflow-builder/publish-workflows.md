---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/publish-workflows/
title: Turn a workflow on or off \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:36.985993+00:00
---

# Turn a workflow on or off  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/publish-workflows/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Turn a workflow on or off Stay organized with collections  Save and categorize content based on your preferences. 

Turning on a workflow triggers the workflow logic and executes the sequence of steps that you have configured. After you create and test a workflow or a new version of a workflow, you can turn it on.

## Workflow versions

When you create a workflow, you can save it as a draft or turn it on. After the workflow is live, you can create additional versions of the workflow. Having multiple versions of a workflow can be useful in the following scenarios:

  * You can save a draft of the workflow if it is not yet ready to be turned on.
  * You can test a new version of the workflow without disrupting the current live version.
  * You can revert to an earlier version of the workflow if necessary.



## Turn on a workflow version

To turn on a workflow version, do the following:

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click ![Agents
icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents**.
  3. The **Agent Gallery** page appears displaying all the prebuilt available agents and workflows in your web app.
  4. Go to the **Your agents** section and click the workflow that contains the version that you want to turn on.

The workflow canvas appears with the last saved draft version of the workflow.

  5. Optional: To select another workflow version, click the **Turn on** or **Update** drop-down and select **Version history**. In the **Version history** pane, select the version that you want to turn on.

  6. Click **Turn on** (or **Update**).

  7. In the confirmation dialog, click **Turn on** (or **Update**). You can also choose to click **Save version only** to save the version but not turn it on.

After you make the workflow live, a new draft version of the workflow is created and the status of the existing one changes to **Live**. Open the **Version history** pane to view the live version of your workflow.




## Turn off a workflow version

To turn off a workflow version, do the following:

**Caution:** Turning off a workflow version removes its schedules and event triggers, so the workflow doesn't start any new runs. Runs that are already in progress, including simulations that you started from the **Preview** tab, continue until they complete. Also, the workflow stops running for everyone you shared the workflow with. 

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click ![Agents
icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents**.
  3. The **Agent Gallery** page appears displaying all the prebuilt available agents and workflows in your web app.
  4. Go to the **Your agents** section and click the workflow that contains the workflow version that you want to turn off.
  5. In the editor canvas, click the **Turn on** or **Update** drop-down and select **Version history**.
  6. In the **Version history** pane, locate the live version that you want to turn off.
  7. Click more_vert **Actions menu** , and select **Turn off**.
  8. In the confirmation dialog, click **Turn off**.

The status of the workflow version changes to **Draft**.




## What's next

  * Learn how to [view workflow runs](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflow-runs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
