---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/test/
title: Test APIs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:02.366611+00:00
---

# Test APIs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/test/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Test APIs Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Test APIs as described in the following sections. See also [Manage folders and files in an Apigee workspace](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#manage-folders-files).

**Note:** Before you test an API, you may need to build and export a set of test resources, such as API products, developers, or apps, that represent those same resources that might exist in your production environment. See [Build and export test resources](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/build-test-resources).

## Determine the URL of the API proxy endpoint

When you deploy your environment, the URL of the API proxy endpoint is displayed in the **emulators** section, under **Active deployments**.

![API proxy endpoint URL](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-deploy-status.png)

To copy the URL for the API proxy endpoint, position your cursor over the URL and click ![Copy API proxy endpoint URL](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-copy.png).

The URL for your API proxy endpoint is structured as follows:
    
    
    **https://0:8998/shopping/cart/addItem**
           |_____||____________||______|
              |        |           |
         host+port  basepath    resource
    

By default, the host and port (traffic) default to `0` and `8998`, respectively.

You define the port when installing the Apigee Emulator, and the basepath and resource values when [developing your API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-apiproxies).

## Use curl to test your APIs

To test your APIs using curl, open the **Terminal** tab and execute a call to your API.

For example:
    
    
    curl 0:8998/helloworld

## Authenticate using an API key

If your API requires API key-based authentication:

  * Build and export the API product, developer, and developer app test resources, as described in [Build test resources](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/build-test-resources)
  * Click **Active developer apps** in the **Active test resources** section of the Apigee Emulator and copy the `consumerKey` value (without the quotes) for the API product, as shown in the following figure.

![Developer apps with the consumerKey value highlighted.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-consumerkey.png)




Pass the API key in your curl call, as required by your API. For example, the following curl call passes the API key in the `apikey` query parameter:
    
    
    curl 0:8998/helloworld?**apikey=ZQA5euYtNeJ7ZCGCJMpvd6F2BZOmxOzY**

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
