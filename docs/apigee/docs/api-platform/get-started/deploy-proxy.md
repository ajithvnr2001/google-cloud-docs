---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy/
title: Step 2: Deploy an API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:48.222285+00:00
---

# Step 2: Deploy an API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 2: Deploy an API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

An API proxy must be deployed before developers can access and use it.

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page. 

[Go to API proxies](https://console.cloud.google.com//apigee/proxies)

  2. Make sure the same Google Cloud project where you created the API proxy is selected from the dropdown at the top of the page.
  3. Select **myproxy** in the proxies list. 
  4. Click **Deploy** to display the **Deploy** dialog, and enter the following information: 
     * **Revision** : Select the revision number of the proxy you want to deploy. If you're doing this tutorial from scratch, there's only one revision to choose from.
     * **Environment** : Select the environment where you want to deploy the proxy. An environment is a runtime execution context for the API proxies in an Apigee organization. You must deploy an API proxy to an environment before it can be accessed. 
     * **Service account** (optional): A [service account](https://cloud.google.com/iam/docs/service-accounts) for the proxy. The service account represents the identity of the deployed proxy, and determines what permissions it has. This is an advanced feature, and for the purpose of this tutorial, you can ignore it.
  5. Click **Deploy**.

**Note:** It may take a few moments for Apigee to deploy the new proxy.

When the proxy is deployed, the **Status** column in the **Deployments** section displays a green icon to show that the API proxy revision is deployed. You can hover the cursor over the status icon to see more information about the deployment.

The next step explains how to call the API proxy you just deployed.

[1](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-proxy) [2](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy) [(NEXT) Step 3: Test the API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy) [4](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/change-endpoint) [5](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/add-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
