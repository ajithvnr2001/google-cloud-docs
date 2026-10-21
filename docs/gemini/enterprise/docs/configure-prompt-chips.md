---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-prompt-chips/
title: Configure prompt chips \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:48:23.143733+00:00
---

# Configure prompt chips  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-prompt-chips/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure prompt chips Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure your prompt chips for your web app using the Google Cloud console.

## Overview

A _prompt chip_ is a predefined category that's accessible from the Gemini Enterprise web app. When you click a prompt chip, suggested prompts display that you can immediately send to the model.

![Prompt chips on Gemini Enterprise page](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/prompt-chips-in-use.png)

## Before you begin

You must have an existing Gemini Enterprise web app. To create a new app, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

## Configure your prompt chips

To configure your prompt chips, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to **Gemini Enterprise**](https://console.cloud.google.com/gemini-enterprise/products)

  2. Select your project.

  3. Select your app from the **Name** column. The navigation menu updates.

  4. Click **Prompt chips**. The **Prompt chips** page displays all of the prompts created by Google and by you.

  5. If you want all of the prompt chips to display on your **Gemini Enterprise** web app, then select the **Automatically enable new prompts from Google** checkbox.

If you want to control which prompt chips display, then clear the checkbox.




## Create a prompt chip

  1. Click **\+ New prompt** , and the **Create prompt** page displays.

  2. Enter a prompt-chip name in the **Name** field, which can't be changed after it's saved and must follow this format: 

     * The name's length must be from 1 to 63 characters long.
     * The name only contains lowercase letters, numbers, or hyphens.
     * The name must begin and end with a letter or a number.
  3. Enter the name for your prompt chip in the **Display name** field. This name appears in the **Display name** column of the **Prompt chips** table.

  4. Enter a title in the **Title** field for your prompt chip. When the prompt chip is clicked, all prompts defined for this title display.

  5. Enter a brief description that explains what the user should enter as a prompt on the **Gemini Enterprise** web app in the **Prefix** field.

  6. To provide prompts that your user can choose from for a specific title, enter the text in the **Suggested prompt** field.

     1. Click **\+ Add suggested prompt**.

     2. To make the prompt chip available on the **Gemini Enterprise** web app, click the **Enabled** toggle.

     3. Optional: Continue to enter suggested prompts.

  7. Click **Create**. All of your prompts are stored in the **Our prompts** category. Delete unused suggested prompt fields.




## Edit or delete a prompt chip

To edit a prompt chip, do the following:

  1. Click the pencil icon for the prompt chip that you want to change. An **Edit Prompt** pane displays.

  2. Change the field(s). You can't change the prompt chip name.

  3. Click **Update**.




To delete a prompt chip, do the following:

  1. Click the trashcan icon, and a confirmation dialog displays.
  2. Click **Delete**.



## Filter prompt chips

To find a prompt chip from a list of prompt chips, you can filter two different ways:

  * You can select a prompt chips category, which include the following:

    * **All** : Displays both **Google-made** and **Our prompts** prompt chips.
    * **Google-made** : Displays the prompt chips provided by Google.
    * **Our prompts** : Displays the prompt chips that you create.
  * To find your prompt chip quickly, enter a few characters in the **Filter** field.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
