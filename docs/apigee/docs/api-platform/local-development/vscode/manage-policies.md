---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-policies/
title: Add features using policies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:04.992971+00:00
---

# Add features using policies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Add features using policies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee lets you program API behavior without writing any code by using _policies_. A policy is like a module that implements a specific, limited management function. Policies are designed to let you efficiently and reliably add common types of management capabilities to an API.

Policies provide features like security, rate-limiting, transformation, and mediation capabilities, saving you from having to build and maintain the code on your own. You're not limited to the set of policy types provided by Apigee. You can also write custom scripts and code (such as JavaScript applications) that extend API proxy functionality and enable you to innovate on top of the basic management capabilities supported by Apigee policies.

Create and attach policies to API proxies and shared flows using Apigee in Cloud Code as described in the following sections. Depending on the policy type, you may need to create a resource, as described in [Manage resources](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-resources). See also [Manage folders and files in an Apigee workspace](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#manage-folders-files).

**Before you begin** : Familiarize yourself with the concepts described in the following topics: 

  * [What's a policy?](https://docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement)
  * [Policy reference overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy)
  * [FlowCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy)



### Create a policy

To create a policy using Apigee in Cloud Code:

  1. In your Apigee workspace, perform one of the following actions based on where you want to attach the policy:

Attach to | Action  
---|---  
API proxy | Perform one of the following actions: 
     * Position your cursor over one of the following folders, click ![Create Apigee policy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png), and select **Create policy** : 
       * `apiproxy-name` proxy bundle
       * `apiproxy-name/apiproxy`
     * Position your cursor over the **`apiproxy-name /apiproxy/policies`** folder for the API proxy and click ![Create API proxy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).  
Shared flow | Perform one of the following actions: 
     * Position your cursor over one of the following folders, click ![Create shared flow icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png), and select **Create policy** : 
       * `sharedflow-name` shared flow bundle
       * `sharedflow-name/sharedflowbundle`
     * Position your cursor over the **`sharedflow-name /sharedflowbundle/policies`** folder for the shared flow and click ![Create shared flow icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).  



The Create policy wizard opens.

  1. Select the category of the policy that you want to create from the list. For a description of the policy categories, see [Policy reference overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy).

  2. Enter a unique name for the policy and press **`Enter`**. The policy is added to the `/policies` folder for the API proxy or shared flow in the Apigee section and opened in the editor.

  3. Edit the file, as required, and select **File > Save** or ⌘S to save your edits. For more information about configuring the policy, see [Policy reference overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy).

  4. Create resources if required by the policy type, as described in [Manage resources](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-resources).




### Attach a policy to a flow

Policies are not executed until they are attached to a flow. You can attach a policy to a flow by adding the **< Step>** element to the appropriate request or response flow element in a ProxyEndpoint or TargetEndpoint configuration, as described in the following topics:

  * [Attaching a policy to a ProxyEndpoint or TargetEndpoint flow](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-policy-proxyendpoint-or-targetendpoint-flow)
  * [FlowCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy)



For example, the following configuration attaches a [QuotaPolicy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) to the `<PreFlow>` of the ProxyEndpoint to configure the number of request messages that an API proxy allows over a period of time.
    
    
    <ProxyEndpoint name="default">
      <PreFlow>
        <Request>
          <Step><Name>QuotaPolicy</Name></Step>
        </Request>
      </PreFlow>
      <HTTPProxyConnection>
        <BasePath>/weather</BasePath>
      </HTTPProxyConnection>
      <RouteRule name="default">
        <TargetEndpoint>default</TargetEndpoint>
      </RouteRule>
    </ProxyEndpoint>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
