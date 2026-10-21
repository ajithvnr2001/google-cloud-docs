---
url: https://docs.cloud.google.com/contact-center/insights/docs/qai-setup-guide/
title: Get started with Quality AI \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:07:57.192059+00:00
---

# Get started with Quality AI  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/qai-setup-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Get started with Quality AI Stay organized with collections  Save and categorize content based on your preferences. 

This page walks you through the steps to set up and start using Quality AI.

## Prerequisites

The following steps confirm you can access Quality AI:

  1. [Enable Customer Experience Insights](https://docs.cloud.google.com/gemini-enterprise-cx/insights/before-you-begin) for your project and verify that you have access to the Customer Experience Insights API.
  2. [Enable Dialogflow runtime integration](https://docs.cloud.google.com/gemini-enterprise-cx/insights/enable-dialogflow-runtime-integration).



## Use Quality AI

  1. Open [Google Cloud CCAI](https://ccai.cloud.google.com/projects) and select your project where Customer Experience Insights is enabled.
  2. Click **Insights** ![](https://www.gstatic.com/dialogflow-console/common/assets/ccai-icon-family/insights-48-color.png) > insert_chart **Quality AI**.



### Make a scorecard

You can create different scorecards for different business units.

  1. Click article **Scorecards** > **\+ Add scorecard**.
  2. Click **Untitled Scorecard edit** and add a name for your scorecard > **Unspecified description edit**, and add a description of what the scorecard is for.
  3. Click **\+ Add question** > add a question to evaluate agent performance and an optional tag. For each question, you can select a tag: business, customer, or compliance.

_Example_

**Question** : Did the agent understand the customer's needs by asking thoughtful questions throughout the conversation?

**Tag** : Customer

  4. Add instructions to define the interpretation of each answer choice.

_Example_

**Instructions** :

**Yes** : The agent asked thoughtful questions. OR The agent demonstrated active reading skills.

**No** : The agent did not ask thoughtful questions. The customer had to repeat themselves multiple times due to the agent's lack of understanding toward the customer's needs. The agent only asked necessary questions, such as their zip code or product name.

**NA** : Unable to ask questions. The interaction was for transfer or was a non-sales related interaction.

  5. Enable **Tracing** to activate this feature.

  6. Select an answer type, enter the answer choices and their corresponding scores, and check the box to include `N/A`, if applicable. 

  7. Click **\+ Add answer choice** to include additional answer choices and their scores.

_Example_

**Answer type** : Yes/No

**Answer choice and score** : Yes 1, No 0

check_box **Add 'N/A' (not available) as an answer choice. If selected, the question will not be included in the total score calculation.**

  8. Click **Save**.

  9. Repeat steps 3-8 for each of your questions > click **Next**.




### Source menu

By default, Quality AI displays information based on the scorecard you most recently made or accessed. You can also set a default override for new users who haven't created or selected a scorecard. It lets them see data for a project when they first click a Quality AI page in the Customer Experience Insights console.

As an administrator, you have two options to set the default scorecard for your project.

  1. Choose one of the following options: 
     * Click article **Scorecards** > **Change**.
     * Click settings > **Scorecards**.
  2. Select a **Default scorecard** from the menu and click **Save**.



### Calibrate the AI model

You calibrate models using example conversations, which consist of conversations, associated questions, and expected answers. You must upload example conversations as a CSV file. For more details on formatting your example conversations, see the [Quality AI best practices page](https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-best-practices#example_conversation_format).

#### Prepare example conversations

Quality AI provides a template which automatically generates the alphanumeric conversation, scorecard, and question IDs for a specific scorecard. You can also filter which conversations to include. You must add the answers for each question.

Follow these steps to create your template for example conversations within the Quality AI console.

  1. Navigate to **Conversations** and add [filters](https://docs.cloud.google.com/gemini-enterprise-cx/insights/filtering) to select specific conversations.
  2. Click **Create example conversations template**.
  3. Click **Scorecard** and select the name of your scorecard.
  4. Click **Cloud Storage Destination** and enter the location of a file in your Cloud Storage bucket.



#### Upload example conversations

When you have a CSV file with your example conversations, you must upload it to facilitate model calibration.

  1. Within your Quality AI-enabled project, upload example conversations to your Cloud Storage bucket.

For a detailed walkthrough on how to use Google Cloud Storage with the Google Cloud console, see the [Cloud Storage documentation](https://docs.cloud.google.com/storage/docs/discover-object-storage-console).

  2. In the Quality AI console, navigate to **Scorecards** > select your scorecard > click **Next** to select example conversations.

  3. Click **\+ Add example conversations** and enter the path to your Cloud Storage bucket, then click **Add**.

  4. Click **Begin calibration** to initiate model calibration, which can take from four to eight hours. (Time increases for scorecards with more questions or example conversations.)

  5. After calibration, click **Launch new version**.




#### Edit example conversations

You can edit example conversations using the [FeedbackLabel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.feedbackLabels) resource. The API supports creating, updating and deleting existing example conversations. You can also bulk upload example conversations using the [bulkUploadFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/bulkUploadFeedbackLabels) method. Example conversations can always be updated by uploading the CSV file with the same IDs and updated answer label.

#### Edit scorecards and recalibrate the model

You can also edit an existing scorecard to change the questions associated with example conversations. Editing scorecards requires that you recalibrate the model to incorporate the changes.

  1. In the Quality AI console, navigate to **Scorecards** > select your scorecard > click **Edit**.
  2. Depending on whether you want to add or change a question, choose an option: 
     * Click **\+ Add question**.
     * Click **Edit** on the question.
  3. Fill in the form.
  4. To initiate model recalibration, click **Save** > **Next** > **Begin calibration**.
  5. Wait at least four to eight hours.
  6. After calibration, click **Launch new version**.



## What's next?

  * [Quality AI best practices](https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
