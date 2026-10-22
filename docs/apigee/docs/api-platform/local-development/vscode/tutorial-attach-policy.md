---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-attach-policy/
title: Step 6: Attach a policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:00.141772+00:00
---

# Step 6: Attach a policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-attach-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 6: Attach a policy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee policies can transform message formats, enforce access control, call remote services, authorize users, examine message content for potential threats, and do much more. For more information, see [What's a policy?](https://docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement)

Proxy and target endpoints define a pipeline for request and response message processing referred to as request and response _flows_. Flows are sequential stages along the API request processing path. Policies are attached at different points in the request and response message flows as processing _steps_.

In the following steps, you create a new policy and attach it to your API proxy in the `PreFlow` response flow to ensure the policy is applied before any other processing takes place. The [XMLtoJSON policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy) used in this tutorial converts the payload of the API's response message from XML to JSON.

  1. Create an XMLtoJSON policy. 
     1. Expand the **helloworld** API proxy bundle, position your cursor over the **policies** folder, and click ![Create icon for new policy](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png). 

![default.xml target endpoint file](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-policies.png)

The **Create policy** wizard opens.

     2. Select **Mediation** as the policy category.
     3. Select **XML to JSON** as the policy type.
     4. Enter **XMLtoJSON** as the policy name and click **Enter**. 

The policy is added to the `/policies` folder for the API proxy and opened in the editor.

     5. Click `XMLtoJSON.xml` to edit the policy. Set the `<OutputVariable>` and `<Source>` elements to `response` and save your changes. **Note** : You'll attach the policy to the **response** flow in the API proxy PreFlow in the next step.
            
            <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
            <XMLToJSON async="false" continueOnError="false" enabled="true" name="XMLtoJSON">
                <DisplayName>XMLtoJSON</DisplayName>
                <Properties/>
                <Format>yahoo</Format>
                <OutputVariable>**response** </OutputVariable>
                <Source>**response** </Source>
            </XMLToJSON>

  2. Attach the policy to the default proxy endpoint. 
     1. Expand the **proxies** folder in the **helloworld** API proxy bundle and click **default.xml** to open the file in the editor.
     2. Add a `<Step>` element that references the **XMLtoJSON** policy to the `<Response>` flow in the API proxy `<PreFlow>`: 
            
            <ProxyEndpoint name="default">
               **< PreFlow name="PreFlow">**
                  <Request>
                     <Step>
                        <Name>verify-api-key</Name>
                     </Step>
                     <Step>
                        <Name>remove-query-param-apikey</Name>
                     </Step>
                     <Step>
                        <Name>impose-quota</Name>
                     </Step>
                  </Request>
                  **< Response>
                     <Step>
                        <Name>XMLtoJSON</Name>
                     </Step>
                  </Response>**
               **< /PreFlow>**
             ...
            </ProxyEndpoint>

     3. Save your changes to the file.
  3. To redeploy the environment, position your cursor over the **dev** environment folder and click ![Deploy icon for an environment](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-deploy.png). 

![Deploy icon displays when you position the cursor over dev environment folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-environment-deploy.png)

  4. When prompted to select a test bundle to export, click **Deploy without a test bundle** because the test bundle has already been exported. 

![Prompt to export test bundle](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-testbundle-export.png)

  5. Call your API in the **Terminal** tab. 
         
         curl 0:8998/helloworld?apikey=ZQA5euYtNeJ7ZCGCJMpvd6F2BZOmxOzY

The XML response is converted to JSON, as follows:
         
         {
           "root": {
             "city": "San Jose",
             "firstName": "John",
             "lastName": "Doe",
             "state": "CA"
           }
         }




**Congratulations!** You've successfully attached the XMLtoJSON policy to your API proxy!

Next, you will deploy your API as an archive to an Apigee environment for integration testing and production release.

[1](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-workspace) [2](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-proxy) [3](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy) [4](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-test) [5](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-change-target-endpoint) [6](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-attach-policy) [(NEXT) Step 7: Deploy to an Apigee environment](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy-apigee) [8](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-promote)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
