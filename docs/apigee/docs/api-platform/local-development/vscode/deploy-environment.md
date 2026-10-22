---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/deploy-environment/
title: Configure and deploy environments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:18.160498+00:00
---

# Configure and deploy environments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/deploy-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure and deploy environments Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

An _environment_ is a runtime execution context for the API proxies and shared flows that you want to deploy. You must deploy your API proxies and shared flows to one or more environments before they can be accessed for testing. For more information about environments, see [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview).

Configure and deploy environments as described in the following sections. See also [Manage folders and files in an Apigee workspace](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#manage-folders-files).

## Configure an environment

Before you deploy an environment, configure it to identify the API proxies and shared flows you want to deploy, and configure shared flow hooks or target servers, as required.

To configure an environment, create the environment and edit the configuration defined in the following table.

Configuration | Description| Debug masks (`debugmasks.json`) | Define mask configurations to mask specific data in trace and debug sessions.  
---|---  
Deployments (`deployments.json`) | Define the API proxies and shared flows in your deployment.  
Flow hooks (`flowhooks.json`) | Attach shared flows to flow hooks so that they execute at the same place for all API proxies deployed to the environment.  
Target servers (`targetservers.json`) | Decouple your concrete endpoints from your [target endpoints](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-apiproxies#managing_target_endpoints) to support load balancing and failover across multiple backend server instances.  
Key stores (`keystores.json`) | Add TLS support to your [target endpoints](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-apiproxies#managing_target_endpoints) and [target servers](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/deploy-environment#target-servers).  
  
In addition, if you use any policies that require resources, you can [manage resources](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-resources) at the environment level, as required.

### Create an environment

To create an environment in Apigee in Cloud Code:

  1. Perform one of the following actions:

     * Position your cursor over the **environments** folder in your Apigee workspace and click ![Create an environment icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).

![+ displays when you position the cursor over environments folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-environment.png)

     * Select **View > Command Palette** to open the Command palette and select **Cloud Code: Create Apigee environment**.

The **Create environment** wizard opens.

  2. Enter a name for the environment and press `Enter`.


**Note:** This name must match the name of the environment in your Apigee organization.

The environment is added to the **environments** folder in the Apigee section:

![Environments folder with deployments.json, flowhooks.json, and targetservers.json files](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-environment-folder.png)

Configure the environment, as described in the following sections.

### Configure debug masks (debugmask.json)

Apigee lets you define mask configurations to mask specific data in trace and debug sessions. When data is masked, it is replaced with asterisks in the trace output. For example:
    
    
    <description>**********</description>

For more information, see [Masking sensitive data](https://docs.cloud.google.com/apigee/docs/api-platform/security/data-masking#maskingsensitivedata).

To configure debug masks, update the `debugmask.json` file by [editing the file](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#edit) directly.

The following provides an example of the basic structure of a mask configuration in JSON format. For more information about the mask configuration fields shown in the example, see [DebugMask](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/DebugMask). 
    
    
    {
      "namespaces": {
        "myco": "https://example.com"
      },
      "requestXPaths": [
        "/myco:Greeting/myco:User"
      ],
      "responseXPaths": [
        "/myco:Greeting/myco:User"
      ],
      "faultXPaths": [
        "/myco:Greeting/myco:User"
      ],
      "requestJSONPaths": [
        "$.store.book[_].author"_
      ],
      "responseJSONPaths": [
        "$.store.book[].author"
      ],
      "faultJSONPaths": [
        "$.store.book[*].author"
      ],
      "variables": [
        "request.header.user-agent",
        "request.formparam.password"
      ]
    }

### Configure the deployments (deployments.json)

Configure the API proxies and shared flows that you want to include in the deployment.

To configure the deployments, update the `deployments.json` file using the configuration wizard or by [editing the file](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#edit) directly.

**Note:** Only the API proxies and shared flows that you include in the `deployments.json` file are deployed.

To configure the deployments using the configuration wizard:

  1. Position your cursor over the **deployments.json** file for the environment and click ![Wizard icon to configure a deployment](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-settings.png). 

![settings icon displays when you position the cursor over deployments.json folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-environment-configuration.png)

  2. Step through the configuration wizard to select the deployments and autopopulate fields in the `deployments.json` file. The **`deployments.json`** file is opened in the editor.
  3. Edit the configuration, as required.
  4. Select **File > Save** or ⌘S to save your edits.



The following example configures the deployment to include the `helloworld` API proxy and `mysharedflow` and `hw-sharedflow` shared flows:
    
    
    {
      "proxies" : [
         "helloworld"
      ],
      "sharedflows" : [
         "mysharedflow",
         "hw-sharedflow"
      ]
    }

#### Configure service accounts with proxy and shared flow deployments

**Note:** This feature requires an emulator version of 1.9.2 or later.

API proxies that depend on a Google service as a backend may require a Google Cloud service account to be associated with the deployment. See [Using Google authentication](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview).

When editing the `deployments.json` file, you can associate the API proxy or shared flow with a Google Cloud service account. For example: 
    
    
    {
      "name": "proxy-name",
      "serviceAccount": "associated-service-account"
    }

The following example shows a deployment configuration where service accounts are associated with the API proxy `helloworld` and shared flow `mysharedflow`, however the proxy `healthcheck` and shared flow `hw-sharedflow` are not associated with a service account:
    
    
    {
      "proxies": [
        {
          "name": "helloworld",
          "serviceAccount": "myserviceaccount@myorg.iam.gserviceaccount.com"
        },
        "healthcheck"
      ],
      "sharedflows": [
        {
          "name": "mysharedflow",
          "serviceAccount": "myserviceaccount@myorg.iam.gserviceaccount.com"
        },
        "hw-sharedflow"
      ]
    }

Learn more about how to [configure the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#customize-emulator-service-account) to test service account authentication features in your API proxy.

### Attach shared flows using flow hooks (flowhooks.json)

With a _flow hook_ , you attach a shared flow so that it executes at the same place for all API proxies deployed to a specific environment. This gives you a separately implemented and deployed sequence of logic that is not part of an API proxy's implementation code. Specifically, you can attach a shared flow at the following locations in the API proxy flow:

  * Before an API proxy endpoint executes (`PreProxyFlowHook`)
  * After the API proxy endpoint executes and right before the response is sent out to the client (`PostProxyFlowHook`)
  * Before a target endpoint executes (`PreTargetFlowHook`)
  * After the target response executes (`PostTargetFlowHook`)



For more information about flow hooks, see [Attaching shared flows using flow hooks](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-hooks).

**Note** : Attaching a shared flow to a flow hook is an action that has a very broad effect. The attached shared flow executes at the flow hook's point for every proxy deployed to that environment.

To attach shared flows using flow hooks, update the `flowhooks.json` file using the configuration wizard or by [editing the file](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#edit) directly.

To configure the flow hooks using the configuration wizard:

  1. Position your cursor over the **flowhooks.json** file for the environment and click ![Wizard icon to configure a flow hook](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-settings.png).
  2. Select the shared flow(s) to attach at specific locations in the API proxy flow and autopopulate fields in the `flowhooks.json` file. The **`flowhooks.json`** file is opened in the editor.
  3. Edit the configuration, as required.
  4. Select **File > Save** or ⌘S to save your edits.



The following example attaches the `mysharedflow` to the `PreProxyFlowHook` so that it executes before an API proxy endpoint executes:
    
    
    {
      "PreProxyFlowHook": {
        "continueOnError": true,
        "sharedFlow": "mysharedflow",
        "description": "Shared enforced before a proxy endpoint executes."
      }
    }

### Configure the target servers (targetservers.json)

Target servers (TargetServers) decouple concrete endpoint URLs from [target endpoint (TargetEndpoint)](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-apiproxies#managing_target_endpoints) configurations. Instead of defining a concrete URL in the configuration, you can configure one or more named TargetServers. Then, reference each TargetServer by name in a TargetEndpoint HTTPConnection.

For more information about target servers, refer to the following topics: 

  * [Load balancing across backend servers](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers)
  * [Antipattern: Load balance with a single target server with MaxFailures set to a no-zero value](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/load-balancing-maxfailures)



To configure target servers, update the `targetservers.json` file using the configuration wizard or by [editing the file](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#edit) directly. For a description of the fields in the `targetservers.json` file, see [Resource: TargetServer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers).

To configure the target servers using the configuration wizard:

  1. Position your cursor over the **targetservers.json** file for the environment and click ![Wizard icon to configure target servers](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-create.png).
  2. Step through the configuration wizard to configure the target server and autopopulate fields in the `targetservers.json` file. The **`targetservers.json`** file is opened in the editor.
  3. Edit the configuration, as required.
  4. Select **File > Save** or ⌘S to save your edits.



The following example adds a new target server in the environment:
    
    
    [
      {
        "enabled": true,
        "name": "mytargetserver",
        "description": "My first target server",
        "host": "localhost",
        "port": 80
      }
    ]

The following example configures a target server with mutual TLS using [keystores](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/deploy-environment#key-stores):

**Note:** This feature requires an emulator version of 1.9.2 or later.
    
    
    [
        {
            "name": "mtlsserver",
            "host": "mytargetserver.mydomain",
            "port": 443,
            "enabled": true,
            "protocol": "HTTP",
            "tlsInfo": {
                "enabled": true,
                "clientAuthEnabled": true,
                "keyStore": "mykeystore",
                "keyAlias": "mykeyandcert",
                "trustStore": "mytruststore"
            }
        }
    ]

### Configure the keystores (keystores.json)

**Note:** This feature requires an emulator version of 1.9.2 or later.

Keystores define repositories of security certificates used for TLS encryption in target endpoints and target servers.

For more information about TLS configuration, see [Options for configuring TLS](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/options-configuring-tls).

The keystores in Apigee local development are used only to test TLS for target backends that are deployed to the Apigee Emulator. The TLS keys and certs defined in the keystores must be present in the local file system.

To configure keystores:

  1. Open the **`keystores.json`** file for the environment in the editor. The file has two main elements 
     * `stores` \- A map of added keystore name and the aliases.
     * `references` \- A map of all the keystore reference names and the associated keystore name.
  2. Edit the configuration, as required.
  3. Select **File > Save** or ⌘S to save your edits.



The following example shows a keystore `mykeystore` with two aliases, `mycert-alias` and `mykeycert-alias`:
    
    
    {
        "stores": {
          "mykeystore": {
            "my-cert-alias": {
              "cert": "/Users/jdoe/testkeys/cert1.pem"
            },
            "my-keycert-alias": {
              "key": "/Users/jdoe/testkeys/key1.pem",
              "cert": "/Users/jdoe/testkeys/cert1.pem"
            }
          }
        }
      }

## Deploy an environment

Deploy your API proxies and shared flows configured for an environment so they can be accessed for testing.

**Note:** Before deploying an environment, ensure that you have [installed the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#install).

To deploy an environment:

  1. In the Apigee section, position your cursor over the folder of the environment that you want to deploy.
  2. Click ![Deploy icon for Apigee environment](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-deploy.png). 

![Deploy icon displays when you position the cursor over dev environment folder](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-environment-deploy.png)

  3. If multiple [containers for the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#add-container) are running, select the container to which you want to deploy the environment.
  4. Select the [test bundle](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/build-test-resources) that you want to export with the deployment or select **Deploy without a test bundle**. 

![Prompt to export test bundle](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-testbundle-export.png)

**Note:** This prompt displays only if you have created a test bundle in your Apigee workspace. 

You can export test resources later, as described in [Exporting test resources to the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/build-test-resources#exporting_test_resources_to_the_apigee_emulator).




The environment deploys and shows a success message in the **Output** tab.

**Note:** The deployed revision is incremented each time you deploy the same environment.

The deployed applications are displayed in the Apigee Emulator:

![Apigee Emulator showing deployed helloworld application and active test resources](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vscode-deploy-status.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
