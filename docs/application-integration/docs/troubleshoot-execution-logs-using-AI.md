---
url: https://docs.cloud.google.com/application-integration/docs/troubleshoot-execution-logs-using-AI/
title: Troubleshoot failed execution logs using AI \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:05.479314+00:00
---

# Troubleshoot failed execution logs using AI  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/troubleshoot-execution-logs-using-AI/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot failed execution logs using AI

Application Integration provides AI-powered troubleshooting for failed executions. This feature uses Google Gemini to analyze execution logs, determine root causes, and generate actionable recommendations. You can access this feature from the [Execution Logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs#view-integration-execution-logs) page within Application Integration.

**Note:** Your data is not stored in the Gemini AI. 

## Key benefits

By using the Gemini AI-powered troubleshooting feature, you can:

  * Gain a clear understanding of complex error messages. AI turns technical logs into clear, actionable insights.
  * Receive precise resolution steps tailored to your unique integration logic and specific errors encountered.
  * Reduce debugging time by identifying root causes and remediation steps for the fixes.



## Before you begin

Before you can use the Gemini AI troubleshooting feature, you must:

  * Enable AI capabilities for the specific Google Cloud region where you deploy your integration. For more information on how to enable AI capabilities for a new or existing region, see Enable AI capabilities for troubleshooting.



## Enable AI capabilities for troubleshooting

To use Gemini AI for troubleshooting failed executions, enable AI capabilities for the specific Google Cloud region where you deploy your integration.

### Enable AI for a new region

To enable AI for a new region in Application Integration, perform the following steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Regions**. The **Regions** page appears listing all the regions provisioned in your project.
  3. Click **Provision new region**.
  4. Expand **Advanced settings**.
  5. Click the **Enable AI features** toggle under **AI Features**.



### Enable AI in an existing region

To enable AI for an existing region in Application Integration, perform the following steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Regions**. The **Regions** page appears listing all the regions provisioned in your project.
  3. For the existing region you want to edit, in the **Actions** column, click  more_vert **Region actions** and select **Edit**. 

The **Edit region** pane appears.

  4. Expand the **Advanced settings** section.
  5. Click the **Enable AI features** toggle under **AI Features**.



## Troubleshoot failed executions using AI

**Note:** Only failed executions of _published_ integrations can be troubleshooted using this feature. 

To troubleshoot a failed execution log using Gemini AI, do the following:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Logs**. 

The **Execution Logs** page appears listing the execution logs generated for the integrations in the default region.

  3. On the **Execution Logs** page, locate an entry that shows a error **Failed** status.
  4. Click the chat_spark icon next to the failed log entry. 
     * Alternatively, expand the specific row and click **Explain this log entry**.

This opens the **Error Summary** page, which displays the Gemini-generated error summary, including the following sections:

     * **Error message** : Displays the technical error description and points to where the error occurs in the code. 
     * **Root cause** : Explains why the error occurred. 
     * **Detailed analysis** : _(Expand this section)_ Provides more details about the error's impact, specific code areas involved, and how to fix it. 
     * **Steps to fix the error** : Provides remediation instructions specific to the identified root cause. 
**Note:** You might receive more detailed debugging responses for failed logs from the following task types: **Rest Caller Task** , **Connectors Task** , **Javascript Task** , **Data Mapping Task** , **Cloud Function Task** , and **Data Transformer Task**. This is because additional instructions are provided to the Gemini model for these specific task types. **Note:** When troubleshooting is retried, you might get a different response, since responses are generated by a Gemini model. **Note:** If AI features were disabled, the **Enable AI features** button displays the first time you try to access the **Error Summary** page. **Loading time:** The **Error Summary** page can take up to 20 seconds to load on its initial access because of the AI analysis. 
  5. After you review the error summary and understand the issue, click **Close** to return to the **Execution Logs** page. 



## Resolve issues using AI recommendations

After reviewing the error summary, resolve the issue by completing the following steps:

  1. **Follow recommendations** : Implement the recommended steps and make all necessary changes to your integration logic or connector configuration as advised in the **Steps to fix the error** section in the **Error Summary** page. 
  2. **Test and republish** : After completing the modifications, [test and republish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations) the updated integration to confirm that the issue is fully resolved. 



### Example error summary

The following example describes an AI-generated error summary of a failed execution:

  * **Error message:**
        
        RUNTIME ERROR: Index 0 out of bounds, not within [0, 0)
        template:16:2-59 function
        template:17:40-78 function
        :259:50-62 function
        :259:55-61 thunk from>
        template:20:39-40 thunk from>
        :1613:20-21 thunk from>
        :32:25-26 thunk from>
        :32:16-27 function
        :1613:8-22 function

  * **Root cause:** The error `Index 0 out of bounds, not within [0, 0)` indicates an attempt to access the first element (index 0) of an empty array. This issue occurs on line 16 of your code, specifically within these parts of your script: 
    * `getMergedObject(orderId)` function: This function returns an empty array `[]` when it cannot find a matching order in `ordersSalesforce`.
    * `local orders = std.map(...);` line: This line causes an `index 0 out of bounds` error when it tries to access the first element of the result returned by `getMergedObject(orderId)` because the result is an empty array `[]`.
  * **Detailed analysis:**
    * `getMergedObject(orderId)` function: This function looks for a matching order in the `ordersSalesforce` array. If no match is found, it returns an empty array `[]`. This is an expected behavior when the `orderId` is not found in the `ordersSalesforce` array.
    * `local orders = std.map (...);` line: This line uses the `std.map` function to process data. However, it directly attempts to access the first element of the array returned by `getMergedObject(orderId)` without checking if the array is empty. When the array is empty, this results in an `index 0 out of bounds` error.
**Steps to fix the error:**
      * Go to the **Authentication** section in your Salesforce connection.
      * Verify the access token and secret version.
      * Provide valid values for the access token and secret version.
      * [Test and republish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations) the integration to apply the changes.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
