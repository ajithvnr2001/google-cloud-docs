---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/
title: Analyze conversations using Custom Highlights \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:20.634098+00:00
---

# Analyze conversations using Custom Highlights  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Analyze conversations using Custom Highlights Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

Custom Highlights functions in a similar way as the [Smart Highlights](https://docs.cloud.google.com/gemini-enterprise-cx/insights/smart-highlights) feature. A **highlight** contains key words or phrases that CX Insights recognizes as being important to determining the user's intent. If highlights are present, they are labeled in the returned transcript. Smart Highlights automatically detects highlights based on a range of pre-set scenarios, while Custom Highlights lets you specify custom criteria that should be recognized as highlights.

A custom highlight can be made up of one or more **phrase match rule groups**. A phrase match rule group contains one or more **rules**. You can use the following parameters to customize the behavior of your rules.

### Rules to determine a match

You can specify whether a highlight should be detected if only one of the rule groups resolves to `true`, or if all of the rule groups resolve to `true`. Similarly, you can specify that a rule group should resolve to `true` if only one of its rules is met, or if conditions for all rules in the rule group must be met.

## Create a custom highlight using the console

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.phraseMatchers.create`



  1. Navigate to the [CX Insights console](https://ccai.cloud.google.com/insights).
  2. If prompted, sign in using your Google Account.
  3. Enter your project ID.
  4. Select **_Conversation Highlights_** from the navigation menu on the left and go to the **_Custom Highlights_** tab.
  5. Click **_Add New_** , then type in the highlight name and the key words to be detected.

**Note:** The user interface supports a subset of total possible configurations. To access all possible configurations, you must [use the REST API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-api).

The configuration in the console assumes the following:

  * There are at most two phrase match rule groups in the highlight and `ALL_OF` logic is applied at highlight level.
  * One of the phrase match rule groups must contain positive conditions and default to `ANY_OF` logic (represented by **_Keywords to match_**). You can add a second phrase match rule group that only contains negative conditions and defaults to `ALL_OF` logic (represented by **_Keywords to exclude_**).
  * Keywords are case insensitive.



## Analyze a CX Insights conversation

After a custom highlight is created, you can use it to analyze your conversations. See the how-to section to learn [how to analyze a conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-ui).

When an analysis has completed, you can view your custom highlights annotations in the **_Annotations_** panel along with other types of annotations in each conversation.

In the **_Custom Highlights_** tab, you can also find a chart and a table that display the number of each highlight present in the analyzed conversations for different time windows.

**Note:** A conversation can have multiple custom highlights of the same name. The Custom Highlights feature is applied at the conversation segment level rather than the entire conversation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
