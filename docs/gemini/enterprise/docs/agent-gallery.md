---
url: https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery/
title: Browse agents with Agent Gallery \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:58.920500+00:00
---

# Browse agents with Agent Gallery  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Browse agents with Agent Gallery Stay organized with collections  Save and categorize content based on your preferences. 

Agent Gallery lets you discover, run, and organize prebuilt and custom agents in Gemini Enterprise.

To open the gallery, go to your Gemini Enterprise web app and click ![Agents icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents** in the app navigation menu.

Feature | Action | Where it appears  
---|---|---  
**Search bar** | Find agents by name or description keyword in real time. | Top of the gallery.  
**Filter chips** | Filter visible agents by category (`All`, `Pinned`, `Made by Google`, `From your organization`, `Your agents`, `Marketplace`). | Below the search bar.  
**Pinned agents** | Pin frequently used agents for rapid one-click access. | **Pinned** gallery section and the left navigation menu.  
**\+ New agent** | Open Workflow Builder to build a new custom agent. | Upper-right corner of the gallery.  
  
The following image shows the Agent Gallery layout:

![Gemini Enterprise Agents gallery showing the search bar, category filter chips, and pinned agents section.](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/agent-gallery.png)

![Gemini Enterprise Agents gallery showing the search bar, category filter chips, and pinned agents section.](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/agent-gallery.png)

## Find agents in the gallery

You can find agents using the search bar, category filter chips, or a combination of both.

### Search for agents

  1. In Agent Gallery, click the search bar.
  2. Enter the name, function, or keyword for the agent you want to find.
  3. The gallery updates the visible agents in real time. Matching agents remain grouped by category.



**Note:** When a search query is active, the filter chip row dynamically updates to display only the categories that contain matching agents.

### Filter agents by category

Select a filter chip below the search bar to restrict the gallery view to a single category:

  * **All** : Displays all accessible agents across all categories (default view).
  * **Pinned** : Displays only agents that you have pinned for quick access.
  * **Made by Google** : Ready-to-use first-party agents created by Google, such as [Deep Research](https://docs.cloud.google.com/gemini/enterprise/docs/research-assistant), Gemini Notebook Enterprise, and Co-Scientist.
  * **From your organization** : Custom agents created by colleagues and shared with your team or workspace.
  * **Your agents** : Custom agents created by you in [Workflow Builder](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder). Cards display their current status (such as **Draft** or **Live**).
  * **Marketplace** : Third-party partner agents available to request from your administrator.



When viewing a specific category, click **Show more** or **Show less** to expand or collapse the section grid.

**Note:** In the Gemini Enterprise Frontline edition, access to agents created by your organization is limited to agents provisioned by your administrator. Full access to organizational agents requires Gemini Enterprise Standard or Gemini Enterprise Plus editions.

Made by Google agents aren't available in the Gemini Enterprise Frontline edition.

## Pin agents for quick access

You can pin frequently used agents so they are always accessible without searching the gallery.

  * **To pin an agent:** On any agent card, click the **Pin** icon.
  * **To unpin an agent:** Click the active **Pin** icon on the card, or hover over the agent in the navigation menu and click the **unpin** icon.



When you pin an agent: 1\. The agent card appears in the **Pinned** section at the top of Agent Gallery. 2\. The agent is added to the left navigation menu under the **Agents** heading, allowing you to open the agent directly from anywhere in Gemini Enterprise.

Pin selections persist across your web sessions.

## Create and manage custom agents

  * **Run an agent:** Click any agent card to start a conversation. You can also run an agent in conversation using `@agent_name`.
  * **Create a custom agent:** Click **\+ New agent** in the upper-right corner of the gallery (or in the navigation menu) to open [Workflow Builder](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder). You can build: 
    * [Chat agents](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-chat-agent): Conversational agents for dialog and specialized queries.
    * [Workflows](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflows): Multi-step automated workflows configured with triggers and connector actions.
  * **Edit or delete an agent:** On any card in **Your agents** , click the more options menu (**⋮**) to [edit](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-chat-agent), **share** , or [delete](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/delete-chat-agent) the agent.



## Request access to agents from Google Cloud Marketplace

In Agent Gallery, you can browse available agents from partner vendors listed on Google Cloud Marketplace.

To request access to an agent:

  1. In the Gemini Enterprise web app, click ![Agents icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents** in the app navigation menu.
  2. Select the **Marketplace** filter chip or go to the **Marketplace** section.
  3. Click the agent card you want to access.
  4. Click **Request access** to send a request to your administrator for review.



When your administrator approves the request:

  * You receive a notification at the bell icon in the web app.
  * The agent appears in the **From your organization** section of Agent Gallery.
  * You can run the agent by typing `@agent_name` in conversation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
