---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/known-issues/
title: Troubleshooting service account access \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:44:49.172007+00:00
---

# Troubleshooting service account access  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Troubleshooting service account access Stay organized with collections  Save and categorize content based on your preferences. 

CX Insights uses per-project [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) to access resources in the customer project—such as audio and transcript files in your Google Cloud storage bucket—during analysis. Each project's service account is automatically created the first time you access any user resources. By default, the service account is automatically given some default access—such as Google Cloud storage access—to the project.

After you create your first conversation, you should see the service account permissions in your project's IAM settings. If you accidentally remove or don't see the service account permissions, then you can manually give it access to the correct permissions. The account always has the form `service-<project_number>@gcp-sa-contactcenterinsights.iam.gserviceaccount.com`.

To change an account's permissions manually, navigate to the IAM panel of the CX Insights console and give that user the [contactcenterinsights.serviceAgent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) permission. The service account can also be given fine-grained permissions, though too many of these can lead to instability.

If you see an error message like the following, first verify that your CX Insights service account exists in your IAM configuration.

`"message": "IAM permission 'dialogflow.participants.suggest' on 'projects/<project>/locations/global/conversations/fake_conversation_id/participants/fake_participant_id' denied."`

Then, make sure **Include Google-provided role grants** is checked:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/iampermissions.png)

## Audio export

To export audio from Agent Assist or Dialogflow to CX Insights, verify that `service-<project_number>@gcp-sa-dialogflow.iam.gserviceaccount.com` has the [dialogflow.serviceAgent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) role.

## Manual service agent creation

You can create the Customer Experience Insights service agent with the following command:
    
    
    gcloud beta services identity create --service=contactcenterinsights.googleapis.com --project=<project_id>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
