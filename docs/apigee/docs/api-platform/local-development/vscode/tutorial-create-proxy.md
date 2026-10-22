---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-proxy/
title: Step 2: Create an API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:04.118295+00:00
---

# Step 2: Create an API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 2: Create an API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Next, create an API proxy.

  1. Position your cursor over the **apiproxies** folder in your workspace and click ![Create API proxy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).

![+ displays when you position the cursor over apiproxies folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/vscode-create-proxy.png)

The **Create API proxy** wizard opens.

![First page of the Create proxy wizard](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create-proxy-wizard.png)

  2. Click **API key based authentication**.

  3. Enter the following values for the next set of prompts. Press **Enter** after each to confirm and proceed.

Field | Value | Description  
---|---|---  
`API proxy name` | **helloworld** | Name used to identify the API proxy.  
`API proxy base path` | **helloworld** | Part of the URL used to make requests to your API. Apigee uses the URL to match and route incoming requests to the proper API proxy.  
`Backend target URL` | **https://mocktarget.apigee.net** | Target URL that Apigee invokes on a request to the API proxy. The `mocktarget` service is hosted at Apigee and returns simple data.  
  
The API proxy is created.

  4. Expand the **helloworld** folder to view the contents of the API proxy bundle.

![Shows the folder structure of a reverse proxy in the Apigee section.](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/vscode-reverseproxy-structure.png)

Default API proxy and target endpoints, and a set of policies to manage API key based authentication, are added to the API proxy configuration based on your selections using the wizard.




In the next step, you configure and deploy an environment that includes your `helloworld` API proxy.

[1](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-workspace) [2](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-proxy) [(NEXT) Step 3: Configure and deploy an environment](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy) [4](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-test) [5](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-change-target-endpoint) [6](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-attach-policy) [7](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy-apigee) [8](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-promote)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
