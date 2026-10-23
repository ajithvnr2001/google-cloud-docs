---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-resources/
title: Manage resources \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:24.659099+00:00
---

# Manage resources  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage resources Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Many policy types rely on resources. Resources are the files that implement the code or configuration to be executed by a policy when attached to an API proxy or shared flow. For more information, examples of resources, and a list of supported resource types, see [About resources](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#about).

Create resources at the API proxy, shared flow, or environment level and then access them from the policy, as described in the following sections. See also [Manage folders and files in an Apigee workspace](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#managing_folders_and_files_in_an_apigee_workspace).

## Create a resource

To create a resource using Apigee in Cloud Code:

  1. In your Apigee workspace, perform one of the following actions based on the level at which you want to store the resource. For more information, see [Where resources are stored](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#stored).

Level | Step  
---|---  
API proxy | Perform one of the following actions: 
     * Position your cursor over one of the following folders, click ![Create Apigee resource icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png), and select **Create resource** : 
       * `apiproxy-name` proxy bundle
       * `apiproxy-name/apiproxy`
     * Position your cursor over the **`apiproxy-name /apiproxy/resources`** folder for the API proxy and click ![Create Apigee resource icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).  
Shared flow | Perform one of the following actions: 
     * Position your cursor over one of the following folders, click ![Create Apigee resource icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png), and select **Create resource** : 
       * `sharedflow-name` shared flow bundle
       * `sharedflow-name/sharedflowbundle`
     * Position your cursor over the **`sharedflow-name /sharedflowbundle/resources`** folder for the shared flow and click ![Create Apigee resource icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).   
Environment | Perform one of the following actions: 
     * Position your cursor over the `env-name` environment folder, click ![Create new policy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png), and select **Create resource**.
     * Position your cursor over the **`env-name /resources`** folder for the environment and click ![Create new policy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).  
  
The **Create** resource wizard opens.

  2. Select the resource type that you want to create from the list. For a description of the resource types supported, see [Resource types](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#resourcetypes).

**Note:** You must import JAR files.
  3. Enter a unique name for the resource and press **`Enter`**. **Note:** Don't specify the file extension. An extension will be appended automatically based on the resource type.

The resource is added to the `resources` folder in the `apiproxies`, `sharedflows`, or `environments` folder in the Apigee section and opened for editing.

  4. Edit the resource file, as required, and select **File > Save** or ⌘S to save your edits.




## Import a resource

To import a resource using Apigee in Cloud Code:

  1. In your Apigee workspace, perform one of the following actions based on the level at which you want to use the resource. For more information, see [Where resources are stored](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#stored).

Level | Step  
---|---  
API proxy | Perform one of the following actions: 
     * Position your cursor over the `apiproxy-name/apiproxy` folder and click ![Upload Apigee resource icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-upload.png).
     * Position your cursor over the **`apiproxy-name /apiproxy/resources`** folder for the API proxy and click ![Upload Apigee resource icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-upload.png).  
Shared flow | Perform one of the following actions: 
     * Position your cursor over the `sharedflow-name/sharedflowbundle` folder and click ![Upload Apigee resource icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-upload.png).
     * Position your cursor over the **`sharedflow-name /sharedflowbundle/resources`** folder for the shared flow and click ![Upload Apigee resource icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-upload.png).  
Environment | Perform one of the following actions: 
     * Position your cursor over the `env-name` environment folder and click ![Upload Apigee resource icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-upload.png).
     * Position your cursor over the **`env-name /resources`** folder for the environment and click ![Upload Apigee resource icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-upload.png).  
  
The **Import resource** wizard opens.

  2. Select the resource type that you want to import from the list. For a description of the resource types supported, see [Resource types](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#resourcetypes).

**Note:** For JAR files, select **javacallout jar**. 
  3. Navigate to the file in your local directory and click **Import**.

  4. Enter a unique name for the resource and press **`Enter`**. **Note:** Don't specify the file extension. An extension will be appended automatically based on the resource type.

The resource is added to the `resources` folder in the Apigee Explorer and opened for editing.




## Access the resource from a policy

How you access the resource from a policy depends on the [resource type](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#resourcetypes). For more information, refer to the [Policy reference overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy). For an example of accessing the resource from a policy, see [Accessing the resource](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#access-resource).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
