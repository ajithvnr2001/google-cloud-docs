---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-lists-configure/
title: Configure nested disposition lists \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:09:03.214708+00:00
---

# Configure nested disposition lists  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-lists-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)



Send feedback 

#  Configure nested disposition lists Stay organized with collections  Save and categorize content based on your preferences. 

You can create nested disposition code lists, similar to a folder structure, to organize interaction outcomes in a logical hierarchy. This simplifies the disposition process for agents, especially when dealing with a large number of codes, by guiding them through a structured selection path.

To use dispositions for calls and chats, Automatic Wrap-up must be enabled. You can enable this at **Settings > Operation Management > Wrap-up**.

## Managing individual disposition codes

The first step is to create the individual codes that will populate your lists.

### Create a disposition code

Location: **Settings > Operation Management > Wrap-up > Manage Disposition Codes > Codes** tab

Configuration:

  1. Click the **Create disposition code** button.

  2. Enter a unique **Name** for the code (max 150 characters).

  3. Enter a **Custom ID** for reporting and integration purposes.

  4. Click **Save**. The code is available to add to any disposition list.




The newly created code appears in the main code directory under the **Codes** tab and is active by default.

## Manage hierarchical disposition lists

This section explains creating and organizing your lists into a hierarchy. You can manage everything from the **Lists** tab.

### Creating a top-level list

Location: **Settings > Operation Management > Wrap-up > Manage Disposition Codes > Lists** tab

Configuration:

  1. Click the **Create disposition list** button.

  2. Enter a unique **Name** for the list (max 150 characters).

  3. Enter a **Custom ID**.

  4. Click **Save**.




A new, empty top-level list (or "root" folder) is created. You can navigate to this list to add codes or other lists to it.

### Build a list hierarchy

Location: Navigate to an existing disposition list from the **Lists** tab.

Configuration:

When viewing a list, the following options are available for building out its structure:

  * To add an individual code: Select **Add disposition code** to choose from your existing codes, or select **Create disposition code** to create a new code.

  * To create a new sub-list: Select **Create Disposition List**. This creates a new, empty list inside the current list.

  * To add an existing list as a sub-list: Click **Add Disposition List** and select a list from the menu. This is how you create shared lists that can be accessed from multiple places.




The codes and lists you add appear inside the parent list, forming a nested structure. The system prevents you from adding lists in a way that creates a loop or exceeds the 5-level depth limit, displaying an error message if you attempt to do so.

### About shared lists

When you add a list to multiple parent lists, it becomes a shared list.

  * A warning icon appears next to shared lists to indicate that changes will have a widespread effect.

  * Any modification, such as changing a list's status or adding or removing codes, applies to that list everywhere it appears in your hierarchy.




### Use the tree view

Location: **Settings > Operation Management > Wrap-up > Manage Disposition Codes > Tree** tab

The **Tree** tab provides a read-only view of your entire disposition code hierarchy. You can expand and collapse each top-level list to see its full structure. This is useful for verifying complex nesting and understanding relationships between lists without having to navigate through each folder individually. Selecting any list (folder) in the tree takes you directly to that list's configuration page in the **Lists** tab.

## Assign a disposition list

After you've built your list hierarchy, you need to assign a starting list to be used for interactions.

### Assign a list globally or to a queue

Location: **Settings > Operation Management > Wrap-up** (for global) or **Settings > Queues > [Queue Name] > Wrap-up** (for queue-level)

Configuration:

  1. Navigate to the appropriate **Wrap-up** settings page.
  2. Select a list from the **Disposition Code List** menu.
  3. Click **Save**.



When selecting a list to assign, the menu only shows top-level (root) lists. You can't assign a nested sub-list directly. Agents must always start from a designated top-level list.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
