---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-sharedflows/
title: Develop shared flows \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:03.177445+00:00
---

# Develop shared flows  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-sharedflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Develop shared flows Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Combine policies and resources into a shared flow that you can consume from multiple API proxies, and even from other shared flows. Although it's like a proxy, a shared flow has no endpoint. It can be used only from an API proxy or shared flow that's in the same organization as the shared flow itself.

Develop your shared flows using Apigee in Cloud Code as described in the following sections. See also [Manage folders and files in an Apigee workspace](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#manage-folders-files).

**Before you begin** : Familiarize yourself with the concepts described in the following topics: 

  * [Creating reusable shared flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows)
  * [Attaching a shared flow using a flow hook](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-hooks)



## Create a shared flow

To create a shared flow using Apigee in Cloud Code:

  1. Perform one of the following steps:

     * Position your cursor over the **sharedflows** folder in your local workspace and click ![Create shared flow icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).

     * Select **View > Command Palette** to open the Command palette and select **Cloud Code: Create Apigee shared flow bundle**.

The Create shared flow wizard opens.

  2. Enter a unique name for the shared flow at the prompt and press `Enter`.




After you complete the steps in the wizard, the new shared flow name appears under **sharedflows** in the Apigee section. Each shared flow folder is structured as described in [Shared flow bundle directory structure](https://docs.cloud.google.com/apigee/docs/api-platform/reference/shared-flow-bundle-configuration-reference#sharedflowbundlestructure)

## Upload a shared flow bundle

To upload a shared flow bundle using Apigee in Cloud Code:

  1. Perform one of the following actions:

     * In your local workspace, position your cursor over the **sharedflows** folder and click ![Upload shared flow bundle icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-upload.png).

     * Select **View > Command Palette** to open the Command palette and select **Cloud Code: Import Apigee shared flow bundle**.

  2. Navigate to the shared flow bundle that you want to upload and click **Import shared flow**. The shared flow bundle must be structured as described in [Shared flow bundle directory structure](https://docs.cloud.google.com/apigee/docs/api-platform/reference/shared-flow-bundle-configuration-reference#sharedflowbundlestructure).

  3. (Optional) By default, the name of the zip file minus its extension is used for the name of the shared flow. If this name is not unique, you are prompted to enter a unique name.




The uploaded shared flow folder is added under **sharedflows** in your Apigee workspace.

## Configure shared flows

Configure shared flows as described in the following topics:

  * [Creating reusable shared flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows)
  * [Add features using policies](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-policies)
  * [Manage resources](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-resources)



## Use shared flows

You can call a shared flow using the FlowCallout policy, as described in [FlowCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy).

In addition, by attaching a shared flow to a flow hook you can execute the shared flow before a proxy or target request, or after a proxy or target response. For more information, see: 

  * [Attaching a shared flow using a flow hook](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-hooks) (conceptual overview)
  * [Attaching shared flows using flow hooks (flowhooks.json)](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/deploy-environment#attaching_shared_flows_using_flow_hooks_flowhooksjson) (steps using Apigee in Cloud Code)

**Note:** Apigee does not validate the dependencies between shared flows and API proxies at deploy time. For example, if the FlowCallout policy in an API proxy references a shared flow that either doesn't exist or isn't deployed, API proxy deployment still succeeds. When Apigee checks the dependency at runtime and validation fails, Apigee throws an API proxy error with a `500` HTTP status code.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
