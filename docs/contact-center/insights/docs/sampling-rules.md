---
url: https://docs.cloud.google.com/contact-center/insights/docs/sampling-rules/
title: Sampling rules \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:01:06.145042+00:00
---

# Sampling rules  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/sampling-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Sampling rules Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Quality AI offers contact centers the ability to automatically evaluate millions of conversations instantaneously. However, many contact centers still require human oversight of the automated evaluations to verify when human agents meet customer service and compliance standards, and virtual agents follow instructions to deliver quality service.

Sampling rules simplify the human review process. With these rules, you can define criteria for how Quality AI selects a subset of conversations for manual evaluation. Then, managers or quality analysts can manually review only this portion of conversations, which saves time and resources when conducting conversation assessments.

## Create a rule

Define your sampling rule according to how you want to sample the conversations. For example, you can choose to sample conversations based on their attributes, such as duration and CSAT, or the agents who handled them.

You can set sampling rules for your entire project.

### Console

  1. Sign in to the Customer Experience Insights console, then select your project and location.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Click **settings** > the **Sampling rules** tab > **\+ New rule**.

  3. Fill in the form. For guidance, see the rule details in the next section.

  4. Click **Save**.




### REST API

Use the `CreateAssessmentRule` command. 
    
    
      curl -X POST   
    
      -H "Authorization: Bearer $(gcloud auth print-access-token)"    
    
      -H "Content-Type: application/json; charset=utf-8"   
    
      -d "{ display_name: 'test_assessment_rule', active: true,sample_rule: {sample_row: 10},schedule_info: { schedule: 'every 1440 hours', time_zone: 'UTC'}}"   
    
      "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/assessmentRules"
      

## Rule details

Sampling rules consist of the following details.

  * **Rule name**. Enter a name to identify the rule.
  * **Status**. Toggle active or inactive.
  * **Filter**. Optionally select one or more of the following criteria for choosing conversations. See the [filter conversations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/filtering) page to learn more. 
    * Agent ID
    * Agent type
    * Analysis status
    * Conversation channel
    * Conversation import time
    * Conversation label
    * Conversation language
    * Conversation start time
    * Conversation update time
    * CSAT score
    * Custom highlight
    * Data source Dialogflow
    * Duration
    * Latest analysis time
    * Live agent handoff
    * Playbook ID
    * Playbook name
    * Primary topic name
    * Quality business score
    * Quality compliance score
    * Quality customer score
    * Quality score
    * Scorecard
    * Sentiment
    * Silence time
    * Smart highlight
    * Speech model
    * Summary
    * Summary status
    * Team
    * Tool ID
    * Tool name
    * Transcript
    * Transcript alternative language
    * Transcription language
    * Turn count
    * Uses [Pub/Sub intermediate transcription](https://docs.cloud.google.com/agent-assist/docs/pubsub-intermediate-transcription)
    * Uses [speech adaptation](https://docs.cloud.google.com/agent-assist/docs/adaptation-model-guide)
  * **Quantity**. Select how many conversations to choose that meet the filter criteria. You can enter a number or percentage for one of the following categories: 
    * Across conversations
    * Every agent
  * **Schedule**. Enter the date and time when sampling begins and select how often it repeats. Repetition options include: 
    * Every 24 hours
    * Every 7 days
    * Every 30 days
    * Every 90 days



### Schedule

Quality AI selects sample conversations on the schedule you define. Quality AI first selects sample conversations on the start date you choose, then selects more sample conversations at the time interval you choose.

For example, you could choose the start date April 7, at 8:00 AM, and the schedule every 7 days. In this case, Quality AI selects some sample conversations that took place on April 7, then selects additional sample conversations that took place on April 14, at 8:00 AM.

## API commands

You can also use the following API commands with sampling rules:

  * Find the sampling rule with `GetAssessmentRule`. 
        
        curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)"   
        
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/assessmentRules/ASSESSMENT_RULE_ID"
        

  * List all the sampling rules with `ListAssessmentRule`. 
        
        curl -X GET   
        
        -H "Authorization: Bearer $(gcloud auth print-access-token)"   
        
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/assessmentRules"
        

  * Update or activate the sampling rule with `UpdateAssessmentRule`. 
        
        curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json; charset=utf-8" -d '{active: true}' "https://contactcenterinsights.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION_ID}/assessmentRules/ASSESSMENT_RULE_ID?updateMask=active"
        

  * Delete an sampling rule with `DeleteAssessmentRule`. 
        
        curl -X DELETE   
        
        -H "Authorization: Bearer $(gcloud auth print-access-token)"   
        
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/assessmentRules/ASSESSMENT_RULE_ID"
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
