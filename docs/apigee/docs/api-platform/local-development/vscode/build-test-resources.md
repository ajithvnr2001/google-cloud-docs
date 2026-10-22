---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/build-test-resources/
title: Build and export test resources \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:20.802561+00:00
---

# Build and export test resources  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/build-test-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Build and export test resources Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Before you [test APIs](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/test), you may need to build a set of test resources, such as API products, developers, or apps, that represent those same resources that might exist in the production environment in your Apigee organization.

Build and export test resources as described in the following sections. See also [Manage folders and files in an Apigee workspace](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#manage-folders-files).

**Before you begin:** Familiarize yourself with the concepts described in the following topics: 

  * [What is an API product?](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product)
  * [Registering app developers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product)
  * [Controlling access to your APIs by registering apps](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api)
  * [Using key value maps](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps)



## Build test resources

To build test resources, create a test bundle and edit the test resources defined in the following table.

Test resource | Description| API products (`products.json`) | Define the API products used to bundle APIs and make them available to developers.   
---|---  
Developers (`developers.json`) | Register the developers that will access your APIs.  
Developer apps (`developerapps.json`) | Register apps to control access to your APIs.  
Key value maps (`maps.json`) | Define the key value maps (KVMs) used by your APIs to store data for retrieval at runtime.  
  
### Create a test bundle

To create a test bundle in Cloud Code:

  1. Perform one of the following actions:

     * Position your cursor over the **test data** folder in your Apigee workspace and click ![Create test bundle icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png). ![+ displays when you position the cursor over tests folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-test.png)

     * Select **View > Command Palette** to open the Command palette and select **Cloud Code: Create Apigee test bundle**.

  2. Enter a unique name for the test bundle and press `Enter`.




The test bundle is added to the **test data** folder in the Apigee section.

![Test folder with developerapps.json, developers.json, maps.json, and products.json files](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-test-folder.png)

Configure the test resources, as described in the following sections.

### Define API products (products.json)

Define the API products used to bundle APIs and make them available to developers. For more information about API products, see [What is an API product?](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product)

To define API products, update the `products.json` file using the configuration wizard or by [editing](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#edit) the `products.json` configuration file directly. For a description of the fields in the `products.json` file, see [Resource: ApiProduct](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts).

To define API products using the configuration wizard:

  1. Position your cursor over the **products.json** file for the test bundle and click ![Wizard icon to define an API product](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png). The **Create API product** wizard opens.

![First page of the Create API product wizard](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-product-wizard.png)

  2. Enter a name for the API product and step through the configuration wizard to autopopulate fields in the `products.json` file. The **`products.json`** file is opened in the editor.

  3. Edit the configuration information, as required.

  4. Select **File > Save** or ⌘S to save your edits.




The following example defines the `myapiproduct` API product that contains the `helloworld` API proxy.
    
    
    [
      {
        "apiResources": [
          "/",
          "/*",
          "/**"
        ],
        "quota": "100",
        "quotaInterval": "1",
        "quotaTimeUnit": "minute",
        "name": "myapiproduct",
        "displayName": "My first API product",
        "proxies": [
          "helloworld"
        ]
      }
    ]

### Register developers (developers.json)

Register the developers that will access your APIs. For more information about developers, see [Registering app developers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product).

To register developers, update the `developers.json` file using the configuration wizard or by [editing](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#edit) the `developers.json` configuration file directly. For a description of the fields in the `developers.json` file, see [Resource: Developer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers).

To register developers using the configuration wizard:

  1. Position your cursor over the **developers.json** file for the test bundle and click ![Cloud Code Wizard icon to register developers](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).
  2. Enter the developer email and other values in the configuration wizard to autopopulate fields in the `developers.json` file. The **`developers.json`** file is opened in the editor.
  3. Edit the configuration, as required.
  4. Select **File > Save** or ⌘S to save your edits.



The following example defines the developer `ahamilton@example.com`:
    
    
    [
      {
        "email": "ahamilton@example.com",
        "userName": "ahamilton",
        "firstName": "Alex",
        "lastName": "Hamilton"
      }
    ]

### Register developer apps (developerapps.json)

Register developer apps to control access to your APIs. For more information about registering developer apps, see [Controlling access to your APIs by registering apps](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api).

**Note** : We recommend that you define API products and register developers before you register a developer app.

To register developers apps, update the `developerapps.json` file using the configuration wizard or by [editing](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#edit) the `developerapps.json` configuration file directly. For a description of the fields in the `developerapps.json` file, see [Resource: DeveloperApp](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps).

To register developer apps using the configuration wizard:

  1. Position your cursor over the **developerapps.json** file for the test bundle and click ![Wizard icon to register developer apps](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).
  2. Select the developer and other values to autopopulate fields in the `developerapps.json` file. The **`developerapps.json`** file is opened in the editor.

  3. Edit the configuration, as required.

  4. Select **File > Save** or ⌘S to save your edits.




The following example registers the developer app `myapp` for `ahamilton@example.com` and associates `myproduct`:
    
    
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
        "callbackUrl": "",
        "keyExpiresIn": "",
        "apiProducts": [
          "myproduct"
        ]
      }
    ]

### Define key value maps (maps.json)

Define the key value maps (KVMs) used by your APIs to store data for retrieval at runtime. For more information about KVMs, see [Using key value maps](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps).

To define key value maps, update the `maps.json` file using the configuration wizard or by [editing](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#edit) the `maps.json` configuration file directly. For a description of the fields in the `maps.json` file, see [KeyValueMap resource](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps).

To define KVMs using the configuration wizard:

  1. Position your cursor over the **maps.json** file for the test bundle and click ![Wizard icon to define key value maps](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).
  2. Select the scope and other values to autopopulate fields in the `maps.json` file. The **`maps.json`** file is opened in the editor.
  3. Edit the configuration, as required.
  4. Select **File > Save** or ⌘S to save your edits.



The following example defines the `mykvm` encrypted KVM:
    
    
    [
      {
        "name": "mykvm",
        "encrypted": true
      }
    ]

## Export test resources to the Apigee Emulator

To export the test resources to the Apigee Emulator: 

  1. Position the cursor over the test bundle that you want to export and click ![Export test resource icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-export-test-icon.png).

![Export icon displays when you position your cursor over the test bundle name](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-export-test.png)

  2. If multiple [containers for the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#add-container) are running, select the container to which you want to deploy the environment.



The active test resources appear in the Apigee Emulator, as shown in the following figure.

![Active test resources including API products, developers, and developer apps](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-testresources.png)

View the test resource contents to obtain specific resource information, such as an [API key](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/test#apikey) for testing which is generated automatically and included in the developer app test resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
