---
url: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/view-with-trace/
title: View message data with the Debug view \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:50.246284+00:00
---

# View message data with the Debug view  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/view-with-trace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  View message data with the Debug view Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**What you'll learn**

In this tutorial, you'll learn to:

  * See the response message's headers and body content.
  * See error messages.



**What you'll need**

Before you begin this tutorial, do the following:

  * Ensure that [`curl`](https://curl.haxx.se/) is installed on your machine to make API calls from the command line. 
  * Complete the steps in [Before you begin](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview). 
  * Add a [ SpikeArrest policy to your proxy](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/add-spike-arrest). The SpikeArrest policy is a policy that restricts the number of requests that can be sent to your API proxy. Your proxy must have at least one [policy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/add-policy). 



## View message data

The Debug view in the Apigee Proxy Editor lets you view headers, variables, objects, and other details such as response time in the API proxy request and response flow. The Debug view also lets you see how a request or response changes as it is processed by an API proxy. For a more detailed description of the debug view, see [Using Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace). 

This page describes how to use the Debug view to see what happens when the SpikeArrest policy rate is exceeded. 

**Note:** The Debug Tool is available in the Apigee UI and some debug actions can be performed using the API as described in the following tabs. 

To use the Debug view in the Apigee UI to see what happens when the SpikeArrest policy rate is exceeded: 

  1. In the Google Cloud console, go to the **Proxy development > API Proxies** page. 

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Be sure that your organization name is selected from the project picker in the Google Cloud console pane. The organization name is the same as your Google Cloud project name. 
  3. Click the name of the API proxy you want to debug.
  4. Click the **Develop** tab.
  5. Click the **Policies > SpikeArrest** policy.
  6. In the edit pane, change **Rate** to **1pm**.
  7. Click **Save**.This will allow you to see both successful and failed (over the limit) API calls.
  8. [ Deploy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new) the updated proxy.
  9. Click the **Debug** tab.
  10. Click **Start debug session**. 

In the dialog:

     1. Select the **Environment** in which you want to run the debug session. 
     2. (Optional) From the **Filter** list, select a filter to apply to all transactions in the debug session you are creating. The default is `None (All transactions)`, which includes all transactions in the debug data. 

For information on using filters, see [ Using filters in a debug session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#debugsession-filter). For information about the built-in filters, see [Using predefined filters](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#predefined-filters). 

     3. Click **Start**.
  11. [ Call the API](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy) proxy using `curl` (or with the URL in a web browser) several times until you see at least one `200` response and one `429` response in the **Transactions** pane. 

![Click for larger image view.](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/status-200-429-debug-v2.png)![Status 200 and 439 in debug view.](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/status-200-429-debug-v2.png)**Note:** The HTTP status code for exceeding the rate limit is `429 Too many requests`. 
  12. Click a `429` transaction. In the **Transaction map** pane, this displays a flow diagram including a SpikeArrest policy with an error icon. 

![Click for larger image view.](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/transaction-429-v2.png)![Transaction with status 429 displayed in Transaction map.](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/transaction-429-v2.png)
  13. Click the error **error** icon. The **Error Properties** pane is displayed. 

![Click for larger image view.](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/spike-arrest-error-details-v2.png)![Details of SpikeArrest policyerror.](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/spike-arrest-error-details-v2.png)



You can click the navigate_before **Previous** and navigate_next **Next** buttons to move between steps in the flow and see the details of each step. 

To download the entire debug session as a single document, click **Download Session**. A debug session is deleted within 24 hours of the time it is completed, so if you want to view the session after that time, you need to download it before then. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
