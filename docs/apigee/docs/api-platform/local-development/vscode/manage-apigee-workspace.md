---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace/
title: Manage the Apigee workspace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:00.530379+00:00
---

# Manage the Apigee workspace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage the Apigee workspace Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Before you can develop your Apigee APIs locally using Cloud Code, you must create a new or open an existing **Apigee workspace** in Cloud Code. An Apigee workspace contains the directory structure required for local development.

The following sections describe how to create, open, and manage an Apigee workspace.

## Create an Apigee workspace

To create an Apigee workspace:

  1. Perform one of the following actions:

     * Click **Create Apigee workspace** in the **Apigee** section if no Apigee workspace is open.

![Create Apigee workspace button in UI](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create-apigee-workspace.png)

     * Select **View > Command Palette** to open the Command palette and select **Cloud Code: Create Apigee workspace**.

  2. Select the workspace type that matches your preferred development style. You can choose between a single-repository workspace or a multi-repository workspace.

  3. Enter a name for the Apigee workspace.

  4. Navigate to the directory where you want to save the Apigee workspace. If you are using source control management, select a location in your source control repository.

  5. Click **Select workspace folder**. The Apigee workspace is created, stored in the specified local directory, and opened in the VS Code Explorer.

  6. Click the ![Apigee in Cloud Code icon](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-icon.png) Cloud Code icon in the Activity Bar.




The Apigee workspace displays in the **Apigee** section:

![Apigee Explorer showing Apigee workspace folders, including apiproxies, sharedflows, environments, and tests.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-workspace.png)

Based on the type of workspace selected, the following content is created:

  * For a single-repository workspace, a set of folders is created under `your-workspace-location`. For more information, see Understanding the structure of an Apigee single-repository workspace. 
  * For a multi-repository workspace, a file named `your-workspace-location.code-workspace` is created with the required JSON content. For more information, see Understanding the structure of an Apigee multi-repository workspace. 



## Open an Apigee workspace

**Note:** When you open an Apigee workspace the structure will be validated. For more information, see Understanding the structure of an Apigee workspace.

To open an existing Apigee workspace:

  1. Perform one of the following actions:

     * Click **Open Apigee workspace** on the Apigee Explorer **Local development** node if no Apigee workspace is open.

![Open Apigee workspace button in UI](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-open-apigee-workspace.png)

     * Select **View > Command Palette** to open the Command palette and select **Cloud Code: Open Apigee Workspace**.

  2. Navigate to the Apigee workspace in your local environment.

     * If you are opening a single-repository workspace, select the top level folder of your Apigee workspace that _contains_ the `src/main/apigee` folder.
     * If you are opening a multi-repository workspace, select the workspace file with the extension `.code-workspace`.
  3. Click **Select workspace folder or multi-repository workspace file**. The Apigee workspace is opened in Cloud Code where you are able to explore the workspace contents.

  4. Click the ![Apigee in Cloud Code icon](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-icon.png) Cloud Code icon in the Activity Bar.




The Apigee workspace displays in the Apigee Explorer:

![Apigee Explorer showing Apigee workspace folders, including apiproxies, sharedflows, environments, and tests.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-workspace.png)

## Understand the structure of an Apigee single-repository workspace

When you create a single-repository Apigee workspace in Apigee in Google Cloud, a set of folders is created to enable you to develop API proxies and shared flows, configure and deploy environments, and build and export test resources. The Apigee workspace is stored at `your-workspace-folder/src/main/apigee` in your local environment.

The following table summarizes the structure of an Apigee workspace at a high level.

**Note:** When managing an Apigee workspace outside of Apigee in Cloud Code, ensure you maintain the following structure to avoid validation errors.Folder  | Description   
---|---  
`apiproxies` | Contains a separate `apiproxy-name/apiproxy` folder for each API proxy configuration, structured as described in [API proxy configuration directory structure](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#apiproxystructure). For example: `helloworld/apiproxy` For more information, see [Developing API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-apiproxies).  
`environments` | Defines the runtime execution contexts for the API proxies and shared flows that you want to deploy, including: 

  * API proxy and shared flow deployment definitions
  * Environment-level resources
  * Shared flow hooks
  * Target servers
  * Key stores

For more information, see [Configuring and deploying environments](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/deploy-environment).  
`sharedflows` | Contains a separate `sharedflow-name/sharedflowbundle` folder for each shared flow configuration, structured as described in [Shared flow bundle configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/shared-flow-bundle-configuration-reference).  For example: `mysharedflow/sharedflowbundle` For more information, see [Developing shared flows](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-sharedflows).  
`tests` | Provides a set of test resources, such as API products or developers, required for testing your APIs locally. For more information, see [Building and exporting test resources](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/build-test-resources).  
  
See this example of the structure of an Apigee workspace in your local environment, where `src/main/apigee` is the root:

![Apigee workspace structure in Cloud Code](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-apigee-workspace-structure.png)

## Understand the structure of an Apigee multi-repository workspace

A multi-repository workspace works similarly to a [multi-root workspace](https://code.visualstudio.com/docs/editor/multi-root-workspaces) in Cloud Code. It provides users with flexibility to choose individual storage locations for their artifacts yet develop them together using a single workspace. For example when user prefers one source code management repository per proxy.

A multi-repository workspace is JSON text file with a `.code-workspace` extension.

This is an example content of a multi-repository workspace which contains two API proxies (authentication-proxy, products-proxy), one shared flow (SF-threat-protection), two environments (dev, test) and one test bundle (test-products):
    
    
    {
      "folders": [
        {
          "name": "authentication-proxy",
          "type": "proxy",
          "path": "/work/quickdemo/multi/authentication-proxy"
        },
        {
          "name": "products-proxy",
          "type": "proxy",
          "path": "/work/quickdemo/multi/products-proxy"
        },
        {
          "name": "SF-threat-protection",
          "type": "sharedflow",
          "path": "/work/quickdemo/multi/SF-threat-protection"
        },
        {
          "name": "dev",
          "type": "environment",
          "path": "/work/quickdemo/multi/dev"
        },
        {
          "name": "test",
          "type": "environment",
          "path": "/work/quickdemo/multi/test"
        },
        {
          "name": "test-products",
          "type": "test",
          "path": "/work/quickdemo/multi/test-products"
        }
      ]
    }

These requirements are for each type of folder that can be added to a multi-repository workspace:

Folder type | Required folder structure  
---|---  
`environment` | Defines the environment configuration, as described in [Configure an environment](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/deploy-environment#configuring_an_environment). The name of the folder is used as the name of the environment.  
`proxy` | Defines the API proxy structure, as described in [API proxy configuration directory structure](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#apiproxystructure). The name of the folder is used as the name of the API proxy.  
`sharedflow` | Defines the Shared flow with structure, as described in [Shared flow bundle configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/shared-flow-bundle-configuration-reference). The name of the folder is used as the name of the shared flow.  
`test` | Defines a set of test resources, as described in [Build test resources](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/build-test-resources#building_test_resources).The name of the folder is used as the name of the test resource.  
  
## Edit an Apigee multi-repository workspace

Edit a multi-repository workspace by opening the `your-workspace.code-workspace` file in Cloud Code or your preferred editor.

To open the file from the Apigee extension in Cloud Code:

  * Click **Edit workspace** on the Apigee Explorer **Local development** node.

![Open Apigee workspace button in UI](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-edit-workspace.png)

  * Select **View > Command Palette** to open the Command palette and select **Cloud Code: Edit Workspace**.




## Manage folders and files in an Apigee workspace

The following sections describe how to manage folders and files in an Apigee workspace.

### Edit files in an Apigee workspace

To edit a file in an Apigee workspace:

  1. Click the name of the file that you want to edit in the Apigee Explorer. The contents display in the editor.

  2. Edit the file, as required.

  3. Select **File > Save** or ⌘S to save your edits.




### Copy folders and files in an Apigee workspace

To copy a folder or file in an Apigee workspace:

  1. Right-click the folder or file that you want to copy in the Apigee Explorer and select **Copy**.

  2. Enter a unique name for the folder or file and press **`Enter`**.




The copied folder or file appears in the Apigee workspace.

### Rename folders and files in an Apigee workspace

To rename a folder or file in an Apigee workspace:

  1. Right-click the folder or file that you want to copy in the Apigee Explorer and select **Rename**.

  2. Enter a unique name for the folder or file and press **`Enter`**.




The folder or file is renamed in the Apigee Explorer.

### Delete folders and files from an Apigee workspace

To delete a folder or file from an Apigee workspace, right-click the folder or file that you want to copy in the Apigee Explorer and select **Delete**. The folder or file is removed from the Apigee workspace.

## Refresh the Apigee workspace view

To refresh the Apigee workspace view and synchronize any recent changes made (possibly outside of Cloud Code), perform one of the following actions:

  * Position your cursor over the **Apigee Explorer** title bar and click ![Refresh icon for Apigee Explorer](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-refresh.png).

  * Select **View > Command Palette** to open the Command palette and select **Cloud Code: Refresh Apigee Explorer view**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
