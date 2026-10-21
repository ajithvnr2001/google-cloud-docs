---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-proxy/
title: Step 1: Create an API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:03.661062+00:00
---

# Step 1: Create an API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 1: Create an API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

In this step, you will create a simple API proxy that calls a mock target service.

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Be sure that your organization name is selected from the project picker in the **Google Cloud** pane. The organization name is the same as your Google Cloud project name.
  3. Click **\+ Create**.
  4. In the **Create a proxy** pane, under **Proxy template** , select **Reverse proxy (Most common)**. A reverse proxy simply routes incoming traffic to a backend service.
  5. Under **Proxy details** , enter the following: 
     * **Proxy name:** Enter `myproxy`. The remaining steps in this section assume that this is your proxy's name.
     * **Base Path** : Automatically set to the value you enter for `Proxy name`. The **Base Path** is part of the URL used to make requests to your API. Apigee uses the URL to match and route incoming requests to the proper API proxy.
     * **Description (Optional)** : Enter a description for your new API proxy, such as "Testing Apigee with a simple proxy."
     * **Target (Existing API)** : Enter `https://mocktarget.apigee.net`. This defines the target URL that Apigee invokes on a request to the API proxy. The mocktarget service is hosted at Apigee and returns simple data. It requires no API key or access token.
     * **Space (Optional)** : If your organization has Apigee Spaces enabled, you can associate the API proxy with a Space selected from the list of available options. For more information, see [Apigee Spaces overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).
     * Click **Next**.
  6. Under **Deploy (optional)** leave the **Deployment environments** field unchanged. In this example, you just create the proxy without deploying it at this stage. You can also ignore the **Service Account** field. Leave it blank.
  7. Click **Create**. 

Apigee creates the new proxy and displays a summary of the proxy details in the **Proxy summary** pane.

![myproxy summary pane.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/myproxy-summary.png)

The **Deployments** section is empty because the proxy has not yet been deployed.

  8. In the **Revisions** section under **Endpoint summary** , click **View**. 

The endpoints view pane displays:

     * **Proxy endpoints** : The basepath you set for the proxy, which in this example is `/myproxy`.
     * **Target endpoints** : The basepath you set for the target, which in this example is `https://mocktarget.apigee.net`.
  9. Click **Close** to return to the Proxy summary page.



Next you'll deploy the API proxy. A proxy must be deployed before it can be used by a client.

[1](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-proxy) [(NEXT) Step 2: Deploy the API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy) [3](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy) [4](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/change-endpoint) [5](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/add-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
