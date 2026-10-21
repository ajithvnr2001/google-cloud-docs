---
url: https://docs.cloud.google.com/contact-center/insights/docs/troubleshooting/
title: Troubleshooting Dialogflow runtime integration \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:33:50.777515+00:00
---

# Troubleshooting Dialogflow runtime integration  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Troubleshooting Dialogflow runtime integration Stay organized with collections  Save and categorize content based on your preferences. 

If you have enabled Dialogflow runtime integration but the CX Insights console doesn't display conversations that were created in Dialogflow, take the following steps to troubleshoot.

  * Make sure that you have completed all of the feature [Prerequisites](https://docs.cloud.google.com/gemini-enterprise-cx/insights/enable-dialogflow-runtime-integration).
  * Check whether you are using project-wide or agent-specific security settings. V2 **Security settings** apply across the whole project and are only available in the global region. All other regions will use agent-specific or conversation profile specific security settings. ![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/dfcx-security-settings.png)

  * Run the following curl command to list all available security settings in your Dialogflow or Agent Assist project.
        
        curl -H "Content-Type: application/json" \
            -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
            -H "x-goog-user-project: PROJECT" \
           'https://LOCATION-dialogflow.googleapis.com/v3/projects/PROJECT/locations/LOCATION/securitySettings'

  * To edit existing security settings, get the setting ID from the response of the list command. For example, `projects/ccai-fishfood/locations/us-east1/securitySettings/729a8e06dfed549f`: `SECURITY_SETTINGS=729a8e06dfed549f`.

  * Run the following curl command to update your Dialogflow `SecuritySettings`. Set `enable_insights_export` to `true`.
        
        curl -H "Content-Type: application/json" \
            -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
            -H "x-goog-user-project: PROJECT" \
            -X PATCH https://LOCATION-dialogflow.googleapis.com/v3/projects/PROJECT/locations/LOCATION/securitySettings/SECURITY_SETTINGS?update_mask=insights_export_settings \
            --data '{"insights_export_settings": {"enable_insights_export": true}}'

  * Use the following command to create a security setting with CX Insights enabled.
        
        curl -H "Content-Type: application/json" \
            -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
            -H "x-goog-user-project: PROJECT" \
            -X POST https://LOCATION-dialogflow.googleapis.com/v3/projects/PROJECT/locations/LOCATION/securitySettings\
            --data '{ "display_name": "Insights export enabled", "insights_export_settings": {"enable_insights_export": true}}'

  * If you want to save the audio recordings for playback, run the following curl command to set the name of your Cloud Storage bucket and the format of your audio files.
        
        curl -H "Content-Type: application/json"\
            -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
            -H "x-goog-user-project: PROJECT" \
            -X PATCH https://LOCATION-dialogflow.googleapis.com/v3/projects/PROJECT/locations/LOCATION/securitySettings/SECURITY_SETTINGS?update_mask=audio_export_settings\
            --data '{"audio_export_settings":{"gcs_bucket": "BUCKET","audio_format": "FORMAT"}}'

  * If using Agent Assist, attach your security settings to all your conversation profiles in the **Conversation profile** page:




![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/aa-conversation-profile-security-settings.png)

  * If using Dialogflow, navigate to the **Agent Settings** page and attach security settings in the **Security** tab. Repeat this step for each virtual agent.



![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/dfcx-security-settings.png)

  * Make sure that some Dialogflow conversations have transpired after you enabled runtime integration. Dialogflow runtime integration does not apply retroactively to conversations.
  * Make sure that the conversation is closed if using `AnalyzeContent`.
  * Make sure that the Customer Experience Insights service agent has the [permissions to fetch conversations from Dialogflow](https://docs.cloud.google.com/gemini-enterprise-cx/insights/known-issues).
  * Check the [Cloud Monitoring Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer) to view metrics specific to the integration. Look for Resource Type **Customer Experience Insights Environment** and Metric **Notifications From Contact Center AI Runtime**. This metric shows whether Dialogflow is actually notifying CX Insights when conversations transpire.
  * Check the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) to find where something went wrong.
  * If none of the previous steps resolve your issue, reach out to your Google representative. You can send support requests and feedback directly to them.

**Note:** If you are filing a bug, include the results of the following curl commands in your bug.
    
    
    curl -H "Content-Type: application/json"\
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"\
         -H "x-goog-user-project: PROJECT"\
        'https://LOCATION-dialogflow.googleapis.com/v3/projects/PROJECT/locations/LOCATION/securitySettings'
    
    
    curl -H "Content-Type: application/json"\
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"\
         -H "x-goog-user-project: PROJECT"\
        'https://LOCATION-dialogflow.googleapis.com/v3/projects/PROJECT/locations/LOCATION/agents/AGENT-ID'
    
    
    curl -H "Content-Type: application/json"\
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"\
         -H "x-goog-user-project: PROJECT"\
        'https://LOCATION-dialogflow.googleapis.com/v2/projects/PROJECT/locations/LOCATION/conversationProfiles'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
