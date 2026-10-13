---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-test/
title: Step 4: Test your API \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:01.401000+00:00
---

# Step 4: Test your API  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-test/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 4: Test your API Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

To test the deployed `helloworld` API, click the **Terminal** tab in Apigee in Cloud Code and enter the following curl call:
    
    
    curl 0:8998/helloworld

The following error message is displayed:

![Calling API in terminal tab and getting an authorization error](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-tutorial-api-error.png)

Because you enabled API key-based authentication when creating the API proxy, you need to pass an API key using the `apikey` query parameter when calling the API.

To obtain an API key, you need to create a test bundle and configure the following test resources:

  * **API product** used to bundle the API and make it available to developers.

  * **Developer** that will create an app to access the API.

  * **Developer app** that will enable access to the API using an API key.


**Note:** The examples in this section use `0` for the host value and `8998` for the port value. You can configure the port values, as described in [ Manage the Apigee Emulator.](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator) If you get an error when using `0`, substitute `localhost` for the `0`: 
    
    
    curl localhost:8998/helloworld

## Build and Export test resources

  1. Create a test bundle: 
     1. Position your cursor over the **test data** folder and click ![Create test bundle icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png). 

![+ displays when you position the cursor over tests folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-test.png)

The **Create test bundle** wizard opens.

     2. Enter **mytestbundle** for the test bundle name and press **Enter**. 

The test bundle is created.

     3. Expand the **mytestbundle** folder to view its contents. 

![Test folder with developerapps.json, developers.json, maps.json, and products.json files](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-test-folder.png)

  2. Configure the API product test resource: 
     1. Position your cursor over the **products.json** file and click ![Create API product icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png). 

![+ displays when you position the cursor over products.json](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-api-products.png)

The **Create API product** wizard opens.

![First page of the Create API product wizard](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-product-wizard.png)

     2. Enter **myproduct** for the name of the API product and press **`Enter`** to confirm and proceed.
     3. Enter **myproduct** for the description of the API product and press **`Enter`** to confirm and proceed.
     4. Select **helloworld** to add the API proxy to the API product and click **OK**. 

The `products.json` file is opened in the editor with the new API product configured:
            
            [
              {
                "attributes": [
                  {
                    "name": "sample_attribute_0",
                    "value": "sample_attribute_value_0"
                  }
                ],
                "scopes": [],
                "environments": [],
                "apiResources": [
                  "/",
                  "/*",
                  "/**"
                ],
                "quota": "100",
                "quotaInterval": "1",
                "quotaTimeUnit": "minute",
                "name": "myproduct",
                "displayName": "myproduct",
                "proxies": [
                  "helloworld"
                ]
              }
            ]

  3. Configure the developer test resource: 
     1. Position your cursor over the **developers.json** file and click ![Create Apigee developer icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png). 

![+ displays when you position the cursor over developers.json](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-developers.png)

The **Create developer** wizard opens. 

![First page of the Create API product wizard](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-developer-wizard.png)

     2. Enter the following values at the prompts and press **`Enter`** to confirm and proceed: 
        * Developer email: **ahamilton@example.com**
        * Username: **ahamilton**
        * First name: **Alex**
        * Last name: **Hamilton**

The `developers.json` file is opened in the editor with the new developer configured:
    
    [
        {
          "attributes": [
            {
              "name": "sample_attribute_0",
              "value": "sample_attribute_value_0"
            }
          ],
          "email": "ahamilton@example.com",
          "userName": "ahamilton",
          "firstName": "Alex",
          "lastName": "Hamilton"
        }
      ]

  4. Configure the developer app test resource: 
     1. Position your cursor over the **developerapps.json** file and click ![Create developer app icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png). 

![+ displays when you position the cursor over developerapps.json](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-developerapps.png)

The **Create developer app** wizard opens. 

![First page of the Create API product wizard](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-developerapp-wizard.png)

     2. Select **ahamilton@example.com** as the owner of the app.
     3. Enter the following values at the next set of prompts and press **Enter** to confirm and proceed: 
        * App name: **myapp**
        * Description: **myapp**
        * Callback URL: **Leave blank**
        * Select **myproduct** to add it to the app and click **OK**.
        * Select **never** for the expiry value.

The `developerapps.json` file is opened in the editor with the new app configured:
    
    [
      {
        "attributes": [
          {
            "name": "sample_attribute_0",
            "value": "sample_attribute_value_0"
          }
        ],
        "developerEmail": "ahamilton@example.com",
        "name": "myapp",
        "displayName": "myapp",
        "callbackUrl": "",
        "apiProducts": [
          "myproduct"
        ],
        "expiryType": "never"
      }
    ]

  5. Export the test resources to the Apigee Emulator. 

Position the cursor over the **mytestbundle** test bundle and click ![Export test resources icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-export-test-icon.png).

![Active test resources including API products, developers, and developer apps](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-export-test.png)

**Note:** If multiple [containers for the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#add-container) are running, you are prompted to select the container to which you want to deploy the environment.

The active test resources appears in the Apigee Emulators section, as shown in the following figure.

![Active test resources including API products, developers, and developer apps](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-testresources.png)




## Obtain the API key

Obtain the API key credentials for your developer app: 

  1. In the **emulators** section, under **Active test data** , click **Active developer apps**. 

The active developer apps configuration file is opened in the editor. The file contains credentials for `myproduct`, as highlighted in the following figure.

![Developer apps with the consumerKey value highlighted.](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/vscode_consumerkey.png)
  2. Copy the `consumerKey` value (without the quotes) for the `myproduct` API product. 



## Test your API

Test your API with the API key: 

  1. Pass the API key in your curl call using the `apikey` query parameter, as follows: 
         
         curl 0:8998/helloworld?**apikey= API_KEY**

The following response is returned:
         
         Hello, Guest!




**Congratulations!** You've successfully run an API in your local environment.

In the next step, you'll learn how to change the target endpoint.

[1](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-workspace) [2](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-proxy) [3](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy) [4](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-test) [(NEXT) Step 5: Change the target endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-change-target-endpoint) [6](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-attach-policy) [7](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy-apigee) [8](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-promote)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
