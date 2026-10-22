---
url: https://docs.cloud.google.com/dialogflow/es/docs/agents-validation/
title: Agent validation \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:40.896452+00:00
---

# Agent validation  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/agents-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Agent validation Stay organized with collections  Save and categorize content based on your preferences. 

As discussed on the [Agent design](https://docs.cloud.google.com/dialogflow/docs/agents-design) page, the design of your agent can greatly influence the quality of your agent. To help agent designers create high-quality agents, Dialogflow provides a validation feature. Agent validation results are available automatically whenever agent training is performed and completed. You can access the results of validation from either the Dialogflow Console or the API.

The validation results are informational only. They provide a list of errors that you should correct to improve the quality and performance of your agent. If your agent has errors, you can choose to ignore them and launch your agent. Agent validation does not affect the behavior of an agent in any way.

Here are some example results that you might find:

  * Intent has training phrases which are too similar.
  * Intent contains a parameter that is not used in enough training phrases.
  * There are no negative examples for the fallback intent.
  * This text is annotated in some training phrases but not others.



## Enable and disable automatic validation

By default, agent validation is automatically performed whenever the agent is trained. You can enable and disable this setting:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select your agent.
  3. Click the settings _settings_ icon next to the agent name.
  4. Select the **ML Settings** tab.
  5. Toggle the **Agent Validation** setting on (default) or off.



![Agent validation screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/agent-validation-settings.png)

## Agent validation page

To access the validation data for your agent:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select your agent.
  3. Click **Validation** in the [sidebar menu](https://docs.cloud.google.com/dialogflow/docs/console#console_interface_layout).



![Agent validation screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/agent-validation-tab.png)

## Validation results for intents and entities

When you visit either the intents list or the entities list pages, any intents or entities with validation errors show an error _error_outline_ indicator next to the name.

![Agent validation error screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/agent-validation-list-indicator.png)

When you visit a page for a specific intent or entity that has validation errors, an error _error_outline_ indicator is shown near the **Save** button.

![Agent validation error screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/agent-validation-item-page-top-indicator.png)

Clicking this button shows a list of errors for the intent or entity. By default, only errors with a severity of `CRITICAL` or `ERROR` are shown. You can toggle the types of severities to also show `WARNING` and `INFO`.

![Agent validation error screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/agent-validation-item-page-top-details.png)

You may also see error indicators for specific training phrases and parameters, and you can hover over these indicators to see the details.

![Agent validation error screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/agent-validation-training-phrase.png)

## Validation results for versions and environments

When viewing [versions and environments](https://docs.cloud.google.com/dialogflow/docs/agents-versions), each agent version may have unique validation errors. If any errors are present, the validation icon appears next to the version.

![Agent validation error screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/agent-validation-version.png)

Clicking the icon will show the details.

![Agent validation error screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/agent-validation-version-details.png)

## Validation results with the API

In most cases, you will view validation results using the Dialogflow Console. However, you can access this data from the API as well.

### REST

Call the `getValidationResult` method on the [`Agents`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#agents) type. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID



HTTP method and URL: 
    
    
    GET https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/validationResult?languageCode=en

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/validationResult?languageCode=en"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent/validationResult?languageCode=en" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "validationErrors": [
        {
          "severity": "ERROR",
          "entries": [
            "projects/my-project/agent/intents/58b44b2d-4967-4a81-b017-12623dcd5d28/parameters/bf6fdf55-b862-4101-b5b1-36f1423629d0"
          ],
          "errorMessage": "Parameter 'test' has an empty value."
        },
        {
          "severity": "WARNING",
          "entries": [
            "projects/my-project/agent/intents/271e3808-3c91-4e6b-89e8-47951abcec8d"
          ],
          "errorMessage": "Intent 'app.current.update' does not have enough unique training phrases. Consider adding more different examples."
        },
        {
          "severity": "ERROR",
          "entries": [
            "projects/my-project/agent/intents/26e64b1b-eaa7-4ce2-be46-631a501fccbe/trainingPhrases/a650375e-083c-4bb5-9794-ba9453e51282",
            "projects/my-project/agent/intents/58b44b2d-4967-4a81-b017-12623dcd5d28/trainingPhrases/1d947780-22d3-4f80-8d7a-3f86efbf0be3"
          ],
          "errorMessage": "Multiple intents share training phrases which are too similar:\n - Intent 'app.notifications.open': training phrase 'open allo notifications settings'\n - Intent 'app.current.notifications.open': training phrase 'open notifications settings'"
        },
      ]
    }
    

## Severity States

Validation can show the following severity states:

Severity | Description  
---|---  
**INFO** | The agent doesn't follow the best practice.  
**WARNING** | The agent might not behave as expected.  
**ERROR** | The agent may experience partial failures.  
**CRITICAL** | The agent may completely fail.  
**SEVERITY_UNSPECIFIED** | Not specified. This value should never be used. (This severity is possible through the API)  
  
## Force validation

Agent validation results are available automatically whenever agent training is performed and completed. To force new validation results, you can disable automatic validation, and trigger it manually. See the [Agent ML settings](https://docs.cloud.google.com/dialogflow/docs/agents-settings#ml) page on the console.

## Handling many issues

When a large number of issues are found, you should consider the following:

  * Fix issues in small batches. If there are many similar issues, fixing one issue may fix similar issues after you retrain the agent.
  * At most 5000 issues are shown at a time. If you have over 5000 issues, you may not see a count reduction until less than 5000 remain.



[ Previous arrow_back  Audit logging  ](https://docs.cloud.google.com/dialogflow/es/docs/audit-logging)

[ Next Analytics  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/analytics)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
