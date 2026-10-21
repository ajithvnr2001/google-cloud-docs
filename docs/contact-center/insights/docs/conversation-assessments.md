---
url: https://docs.cloud.google.com/contact-center/insights/docs/conversation-assessments/
title: Conversation assessments \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:23:35.550056+00:00
---

# Conversation assessments  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/conversation-assessments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Conversation assessments Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Quality AI provides scorecards with questions to evaluate contact center agent performance during a conversation. A human can use those questions to evaluate an agent or Quality AI can perform automatic evaluations. Conversation assessments help humans evaluate the performance of a contact center agent and provide feedback.

Human evaluators can perform the following actions with conversation assessments.

  * Edit automatic scorecard results.
  * Create and attach notes to an assessment, a conversation turn, or a scorecard question result.
  * View assessments with all the scorecards and notes in the console.



## Assessment state

The state of a conversation assessment identifies the evaluation process. Conversation assessments can have one of the following possible states:

  * **Draft** : While an evaluator is working on an evaluation, the assessment has the draft state.
  * **Shared** : Evaluators can choose to share an evaluation with someone else who has access to the same authorized view. When you click **Share** , the evaluation status changes, but this action does not send the evaluation to anyone.
  * **Appealed** : If someone disagrees with the results of an assessment, they can submit an appeal to have the assessment reviewed again.
  * **Final** : The final state of an assessment indicates that the evaluation is complete. You cannot add, delete, or update notes on an assessment in the final state.



### View conversation assessments and states

Take the following steps:

  1. Go to the Customer Experience Insights console, sign in with your Google Account, and select your project.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Click **Quality AI** > **Your Tasks**.




## Filter conversations

You can use filters to view only the conversations a particular agent participated in. You can filter conversation assessments based on the agent they are for and the assessment state.

### View conversations and add filters

Take the following steps:

  1. Go to the Customer Experience Insights console, sign in with your Google Account, and select your project.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Click **Conversations** > **Filter Conversations** and enter your filter parameters.




## APIs

You can also use the following APIs to create assessments and notes.

API name | Description  
---|---  
`CreateNote` | Restricted to non-finalized assessments.  
`UpdateNote` | Allows updates of the note content field by the note creator only.  
`DeleteNote` | Limited to the note creator. Rejected if the assessment is `FINALIZED`.  
`ListNotes` | Supports listing the notes of a specific assessment.  
`CreateAssessment` | Create an assessment of a conversation.  
`GetAssessment` | Retrieve an assessment.  
`ListAssessments` | Supports listing assessments across all conversations in a location.  
`PublishAssessment` | Puts a `DRAFT` or `APPEALED` assessment in the `PUBLISHED` state.  
`AppealAssessment` | Puts a `PUBLISHED` assessment in the `APPEALED` state.  
`FinalizeAssessment` | Assessments can be finalized in any state.  
`DeleteAssessment` | Deletes an assessment and its notes if `force` is set to true.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
