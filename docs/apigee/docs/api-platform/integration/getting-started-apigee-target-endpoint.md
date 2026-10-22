---
url: https://docs.cloud.google.com/apigee/docs/api-platform/integration/getting-started-apigee-target-endpoint/
title: Getting started with Application Integration and Apigee proxy Integration targets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:54:49.705432+00:00
---

# Getting started with Application Integration and Apigee proxy Integration targets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/integration/getting-started-apigee-target-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Getting started with Application Integration and Apigee proxy Integration targets Stay organized with collections  Save and categorize content based on your preferences. 

**Announcement:** Application Integration is now available for your Google Cloud project. All Apigee subscription users who had enabled the _Apigee Integrations_ add-on, will now be redirected to Application Integration at no additional cost. [Learn more](https://docs.cloud.google.com/apigee/docs/api-platform/integration/using-application-integration)

This tutorial shows you how to use the Apigee proxy wizard to create a proxy with an [ Integration target](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies). The proxy utilizes an API trigger reference from an existing integration to initiate the sequence of steps in the integration.

The steps below describe how to configure the **Integration target** proxy to run a successful integration when the proxy is called.

##  Before you begin 

  * Confirm your Apigee login credentials and organization details. This information is required to access the Application Integration feature and proxy wizard within the Apigee UI.
  * Create and publish an integration with an **API Trigger** and _at least one_ task. 
    * If you have not yet created an integration that uses an API Trigger, follow the steps in [ Retrieve API payload and send an email](https://docs.cloud.google.com/application-integration/docs/retrieve-api-payload-send-email).
    * Note the name of the integration you create, or the existing integration that you would like to use, as this is used in a later step.
  * [Create a Google service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) in the same Google Cloud project where your Apigee organization was created, and do the following: 
    * Assign the **Application Integration Invoker** role `(roles/integrations.applicationIntegrationInvokerRole)` to the service account. For information about the predefined Application Integration roles, see [Predefined IAM roles](https://docs.cloud.google.com/application-integration/docs/predefined-iam-roles-permissions).
    * Allow your user account (principal) to attach service accounts to resources with the `iam.serviceAccounts.actAs` permission. For information on service account permissions, see [Roles for service account authentication ](https://docs.cloud.google.com/iam/docs/service-account-permissions).

You must provide this service account when you deploy the API proxy. 

  * If you want to use Application Integrations without any limitations, you can pay for the integrations. Application Integration is available as an add-on service for your subscription. If you have already purchased the Application Integration entitlement, and want to enable the entitlement to your Google Cloud project or Apigee organization, contact Apigee support. However, if you want to purchase the Application Integration entitlement, contact Apigee sales. After Application Integration has been enabled for you, perform the following tasks: 
    1. Enable the following APIs: 
       * Apigee API (apigee.googleapis.com)
       * Application Integration API (integrations.googleapis.com)
       * Secret Manager API (secretmanager.googleapis.com)
       * Connectors API (connectors.googleapis.com)

For information on how to enable the APIs, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

    2. Enable the Integration and the Connectors add-ons for your [Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure). 
       * If you are creating a new organization to use for Integration, run the following command:
             
             curl -H "Authorization: Bearer $TOKEN" -X POST -H "content-type:application/json" -d '{"name":"${ORG_ID}", "analyticsRegion":"us-west1", "authorized_network":"${NETWORK_ID}", "runtimeType":"CLOUD", "runtimeDatabaseEncryptionKeyName":"${ENCRYPTION_KEY_NAME}", "addonsConfig": {"integrationConfig": {"enabled": true}, "connectorsPlatformConfig":{"enabled":true}}}' "https://apigee.googleapis.com/v1/organizations?parent=projects/${PROJECT_ID}"

       * If you are using an existing organization, run the following command:
             
             curl -H "Authorization: Bearer $TOKEN" -H "content-type:application/json" "https://apigee.googleapis.com/v1/organizations/${ORG_ID}:setAddons" -XPOST -d '{"addonsConfig":{"integrationConfig":{"enabled":true},"connectorsPlatformConfig":{"enabled":true}}}'

    3. Verify if the add-ons are successfully enabled using the following command: 
           
           curl -H "Authorization: Bearer $TOKEN"  -H "content-type:application/json" "https://apigee.googleapis.com/v1/organizations/${ORG_ID}"

Running the command, should display a message similar to the following:
           
           {
             "name": "Test....",
             "createdAt": "1615483867669",
             "lastModifiedAt": "1615483873468",
             …...
             "addonsConfig": {
               "integrationConfig": {
                 "enabled": true,
               "connectorsPlatformConfig": {
                 "enabled": true
               }
             }
             }

**Note:**
       * When you run an add-on command, it overwrites any existing add-ons. Therefore, if you have any existing add-ons, include them in the add-on command.
       * Disabling an add-on, deletes all configurations of the add-on (feature). For example, if you disable the Integrations add-on, all integrations are deleted.
    4. Assign the following IAM roles to your default Apigee service account(`service-PROJECT_NUMBER@gcp-sa-apigee.iam.gserviceaccount.com`): 
       * Application Integration Invoker (`roles/integrations.applicationIntegrationInvokerRole`)

For information about granting additional roles or permissions to a service account, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## Create an Application Integration target proxy

Do the following to create an **Integration target** proxy in the Apigee UI: 

### Apigee in Cloud console

  1. In the Google Cloud console, go to the **Apigee > Proxy Development > API Proxies** page.

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select your organization from the project picker in the **Google Cloud** pane.
  3. Click **+Create**.
  4. Select **Integration target** from the display of proxy types.

The **Create a Proxy** wizard starts.

  5. In the **Proxy details** configuration page, provide the following details: 
     * **Name** : Enter a name for the proxy. 

Proxy names can contain alphanumeric characters, dashes, and underscores. 

     * **Base Path** : This is autopopulated based on the proxy name. 

The **Base Path** is part of the URL used to make requests to your API. Apigee uses the URL to match and route incoming requests to the proper API proxy. 

     * **Description** : (_Optional_) Enter a brief description of the proxy. 

For example, `Proxy test for Application Integration`. 

     * **Integration region** : Select the region of the integration from the list.
     * **Integration target** : Select the name of the integration target from the list. Note that the integration target list is populated based on the integration region selected.
     * **Trigger** : Select the API trigger associated with the integration from the list.
     * **Endpoint type** : Select **Sync**.
  6. Click **Next**.
  7. **(Optional)** In the **Deploy** area: 
     * Select one or more **Deployment environments**.
     * Enter a **Service account**.
  8. Click **Create**.



### Classic UI

  1. Go to the [Apigee UI](https://apigee.google.com) and sign in.
  2. Select your organization using the drop-down menu in the upper left corner of the UI.
  3. Click **API Proxies** in the main view. 

Alternatively, you can select **Develop > API Proxies** in the left navigation menu. 

  4. From the **Environment** drop-down list, select the environment in which you want to create a new API proxy. 
  5. Click **Create New**. 
  6. Select **Integration target** from the display of proxy types. 

The Create Proxy wizard starts.

  7. In the **Proxy details** configuration page, provide the following details: 
     * **Name** : Enter a name for the proxy. 

Proxy names can contain alphanumeric characters, dashes, and underscores. 

     * **Base Path** : This is autopopulated based on the proxy name. 

The **Base Path** is part of the URL used to make requests to your API. Apigee uses the URL to match and route incoming requests to the proper API proxy. 

     * **Description** : (_Optional_) Enter a brief description of the proxy. 

For example, `Proxy test for Application Integration`. 

     * **Integration region** : Select the region of the integration from the drop-down list.
     * **Integration target** : Select the name of the integration target from the drop-down list. Note that the integration target list is populated based on the integration region selected.
     * **Trigger** : Select the API trigger associated with the integration from the drop-down list.
     * **Endpoint type** : Select **Sync**.
  8. Click **Next**. 
  9. In the **Common policies** configuration page, leave the default selections and click **Next**.
  10. In the **Summary** page, click **Create**. 

An **Integration target** proxy is created successfully. 




## Deploy the proxy

Perform the following steps to deploy the newly created proxy: 

### Apigee in Cloud console

  1. In the Google Cloud console, go to the **Apigee > Proxy Development > API Proxies** page.

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Click the recently created proxy that you want to deploy. The UI displays the **Overview** tab by default.
  3. Click **Deploy**.
  4. Enter the following details: 
     * **Revision** : The revision number of the proxy you want to deploy.
     * **Environment** : The environment where you want to deploy the proxy.
     * **Service account** : The created service account for the proxy.
  5. Click **Deploy**.



### Classic UI

  1. In the [Apigee UI](https://apigee.google.com), select **Develop > API Proxies**. 

The UI displays a list of API proxies and their deployment status.

  2. From the **Environment** drop-down list, select the environment to which you want to deploy the API proxy.
  3. Click the recently created proxy that you want to deploy. The UI displays the **Overview** page by default.

  4. To deploy your changes, first click **Deploy** to display the **Deploy** dialog.
  5. Enter the following: 
     * **Revision** : The revision number of the proxy you want to deploy.
     * **Environment** : The environment where you want to deploy the proxy.
     * **Service account** : The created service account for the proxy. 
  6. Click **Deploy**.



The UI begins the process of deploying the selected revision. It can take up to a minute for the proxy deployment to complete.

When the proxy is deployed, the **Status** column in the **Deployments** section displays a green icon to show that revision 1 of the proxy is deployed. **Note** : There is no explicit `Authentication` element in the **Set Integration Request** policy definition of the proxy. Apigee adds an authentication token to the request automatically. 

For the **Set Integration Request** policy to successfully authenticate, you must deploy your **Integration target** with a service account that has the required IAM roles to run an integration. For more details on deploying an API proxy, see [Deploy on Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview#deploy-on-apigee). 

## Test the Integration target proxy

Run the following command from the terminal window to invoke the proxy and trigger the integration: 
    
    
    curl -v https://YOUR_ENV_GROUP_HOSTNAME/PROXY_NAME

where `YOUR_ENV_GROUP_HOSTNAME` is the hostname for an environment group that contains the environment in which your proxy is deployed. 

For example: 
    
    
    curl -v https://**my-org** -**prod**.hybrid.e2e.apigeeks.net/**my-proxy**

To confirm that the integration was triggered by invoking the proxy: 

### Apigee in Cloud console

  1. In the Google Cloud console, go to the **Application Integration** page.

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Logs**. The **Execution Logs** page appears, listing the execution logs generated for the integrations in the default region. **Note:** To view execution logs for a specific region, change the region in the **Region** list.
  3. Verify that an execution log exists for the triggered integration.
  4. To see the log details, click the arrow_right expander arrow to expand the integration details. 
     * To view the execution details of a specific task, click the **Task ID**. The **Task Execution Details** pane appears displaying the execution details of the task. **Key Point:** The **Task Execution Details** pane displays the complete, untruncated values of task variables, allowing you to debug effectively. ![task execution details](https://docs.cloud.google.com/static/application-integration/images/task-execution-details.png)![task execution details](https://docs.cloud.google.com/static/application-integration/images/task-execution-details.png)
     * To view the request and response parameters of the task, click **Request Parameters** or **Response Parameters**. 

![execution logs request params](https://docs.cloud.google.com/static/application-integration/images/view-logs-request-params.png)![execution logs request params](https://docs.cloud.google.com/static/application-integration/images/view-logs-request-params.png)

     * To view the execution logs of a sub-integration, expand the **Task ID** and click the sub-integration name. This applies to [Call Integration task](https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task), [For Each Parallel task](https://docs.cloud.google.com/application-integration/docs/configure-for-each-parallel-task), [For Each Loop task](https://docs.cloud.google.com/application-integration/docs/configure-for-each-loop-task), and the [While Loop task](https://docs.cloud.google.com/application-integration/docs/configure-while-loop-task). 



### Classic UI

  1. Open the Apigee UI. 
  2. Click **Develop > Integrations**. 
  3. Search for or select the name of the integration created in the steps above and click the integration name. 
  4. Click **Logs**. 
  5. Verify that an execution log exists for the triggered integration. To see the log details, click the row to expand the execution details. 



### Update the proxy request payload (Optional) 

Use the following steps to update the proxy request payload:

### Apigee in Cloud console

  1. In the Google Cloud console, go to the **Proxy Development > API Proxies** page.

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Click the recently created proxy that you want to update.

By default, the UI displays the **Overview** tab for that proxy in the Proxy Editor. 

  3. Click the **Develop** tab.
  4. In the **Navigator** pane, under the **Policies** heading, select **Set Integration Request**.
  5. Uncomment the `<Parameters>` block, and enter your parameter details.

To specify individual parameters, use the `<Parameter>` element. To specify parameter arrays, use the `<ParameterArray>` element.

**Note** : The `<Parameters>` block is left commented in this tutorial for simplicity only. Application Integration supports a number of parameters that can be passed as part of the **Set Integration Request** policy. For more information and examples, see [SetIntegrationRequest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-integration-request-policy#parameters).
  6. Click **Save**.



### Classic UI

  1. In the [Apigee UI](https://apigee.google.com), select **Develop > API Proxies** in the left navigation menu.
  2. Click the recently created proxy. 

By default, the UI displays the **Overview** tab for that proxy in the Proxy Editor. 

  3. Click the **Develop** tab.
  4. In the **Navigator** pane, select **Set Integration Request** under the **Policies** heading. 
  5. Uncomment the `<Parameters>` block, and enter your parameter details. 

To specify individual parameters, use the `<Parameter>` element. To specify parameter arrays, use the `<ParameterArray>` element. 

**Note** : The `Parameters` block is left commented in this tutorial for simplicity only. Application Integration supports a number of parameters that can be passed as part of the **Set Integration Request** policy. For more information and examples, see [SetIntegrationRequest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-integration-request-policy#parameters).
  6. Click **Save**.



## What's next 

Explore the [Integration designer layout](https://docs.cloud.google.com/apigee/docs/api-platform/integration/integrations-ui-layout) and understand the various integration concepts described in [All concepts](https://docs.cloud.google.com/apigee/docs/api-platform/integration/concepts).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
