---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy/
title: Step 3: Configure and deploy an environment \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:52.843641+00:00
---

# Step 3: Configure and deploy an environment  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 3: Configure and deploy an environment Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Configure and deploy an environment that includes the `helloworld` API proxy.

**Note:** Before deploying an environment, ensure that you have [installed the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#install).

  1. Create an environment: 
     1. Position your cursor over the **environments** folder and click ![Create apigee environment icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png). 

![+ displays when you position the cursor over environments folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/vscode-environment.png)

The **Create environment** wizard opens.

     2. Enter **dev** for the environment name and press **Enter**. 

The environment is created.

     3. Expand the **dev** environment folder to view its contents. 

![Environments folder with deployments.json, flowhooks.json, and targetservers.json files](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-environment-folder.png)

When you create an environment, a set of configuration files are included by default in the `dev` environment folder for configuring your deployment and any required debug masks, flow hooks, or target servers.

  2. Configure the deployment details for the `helloworld` API proxy in the environment: 
     1. Position your cursor over the **deployments.json** file and click ![Configure deployment details icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-settings.png). 

![settings icon displays when you position the cursor over deployments.json folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-environment-configuration.png)

The Deployments wizard opens.

     2. Select the **helloworld** API proxy to add it to the deployment and click **OK**. 

The `deployments.json` file is opened in the editor. The file has been updated to include the `helloworld` API proxy in the `proxies` deployment array:
            
            {
              "proxies": [
                {
                  "name": "helloworld"
                }
              ],
              "sharedflows": []
            }

  3. Deploy the **dev** environment: 
     1. Position your cursor over the **dev** environment folder in the Apigee section and click ![Deploy Apigee environment icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-deploy.png). 

![Deploy icon displays when you position the cursor over dev environment folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-environment-deploy.png)

**Note:** If prompted to select a test bundle to export, click **Deploy without a test bundle**. This prompt displays only if you have created a test bundle in your Apigee workspace. You'll create and export a test bundle in the next step.  
![Prompt to export test bundle](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-testbundle-export.png)

The `dev` environment is deployed and the **Output** tab shows a success message.

The `helloworld` deployed application information is displayed in the **emulators** section:

![Apigee Emulator showing deployed helloworld application and active test resources](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-deploy-status.png)




**Congratulations!** You've deployed your first API proxy application. In the next step, you'll test the API proxy using curl.

[1](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-workspace) [2](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-proxy) [3](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy) [(NEXT) Step 4: Test your API](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-test) [5](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-change-target-endpoint) [6](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-attach-policy) [7](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy-apigee) [8](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-promote)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
