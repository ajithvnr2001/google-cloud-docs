---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-change-target-endpoint/
title: Step 5: Change the target endpoint \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:01.052401+00:00
---

# Step 5: Change the target endpoint  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-change-target-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 5: Change the target endpoint Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Change your proxy's target endpoint to one that returns more meaningful data.

  1. Expand the **helloworld** API proxy bundle and click **default.xml** in the **targets** folder to open the file in the editor. 

![default.xml target endpoint file](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/vscode-select-target-endpoint.png)

  2. Update the `<URL>` element to append **xml** to the existing URL: 
         
         <TargetEndpoint name="default">
           <HTTPTargetConnection>
              <URL>https://mocktarget.apigee.net/**xml** </URL>
           </HTTPTargetConnection>
         </TargetEndpoint>

  3. Select **File > Save** or ⌘S to save your edits. 
  4. To redeploy the environment, position your cursor over the **dev** environment folder and click ![Deploy icon to redeploy an Apigee environment](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-deploy.png). 

![Deploy icon displays when you position the cursor over dev environment folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-environment-deploy.png)

  5. When prompted to select a test bundle to export, click **Deploy without a test bundle** because the test bundle has already been exported. 

![Prompt to export test bundle](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-testbundle-export.png)

  6. Run your API in the **Terminal** tab. 
         
         curl 0:8998/helloworld?apikey=ZQA5euYtNeJ7ZCGCJMpvd6F2BZOmxOzY

The following response is returned:
         
         <?xml version="1.0" encoding="UTF-8"?>
           <root>
             <city>San Jose</city>
             <firstName>John</firstName>
             <lastName>Doe</lastName>
             <state>CA</state>
           </root>
         




In the next step, you'll add a new policy to your API.

[1](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-workspace) [2](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-proxy) [3](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy) [4](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-test) [5](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-change-target-endpoint) [(NEXT) Step 6: Attach a policy](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-attach-policy) [7](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy-apigee) [8](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-promote)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
