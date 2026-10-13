---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy/
title: Creating an API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:08.757166+00:00
---

# Creating an API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Creating an API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** In environments enabled for [archive deployments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#deployment-types), you cannot develop API proxies using the Apigee UI, API, or gcloud. To develop API proxies for archive deployments using Apigee in VS Code,see [Developing API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-apiproxies) using Apigee in VS Code.

Create a proxy in the Apigee UI, or using the API, as described in the following sections.

## API proxy primary fields

Follow these guidelines when creating an API proxy:

Field | Description  
---|---  
**API proxy name** | Name displayed for your API. Specify alphanumeric characters, dash (-), or underscore (_). **Note:** The name of the API proxy must not match the name of any API proxy in the organization that can be deployed to an [environment with Proxy deployment enabled](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/api-development-lifecycle#deploying-api-proxies).  
**API proxy base path** | URI fragment that appears after the `http://[host]` or `https://[host]` address of your API proxy. Apigee uses the base path URI to match and route incoming request messages to the proper API proxy. **Note:** The base path must be unique; you cannot deploy two API proxies with the same base path. If you edit a deployed API proxy and set the base path to the same value as the base path of another API proxy, Apigee automatically undeploys the API proxy when you save it. Before you can redeploy the API proxy, you must edit the base path so that it is unique.**Use wildcards in base paths** Use one or more wildcards in API proxy base paths to future-proof your API proxies. We allow specification of a single `*` wildcard character between two `/` forward slash characters: `/*/`. For example, a base path of `/team/*/members` allows clients to call `https://[host]/team/blue/members` and `https://[host]/team/green/members` without you needing to create new API proxies to support new teams. You can replace any number of tokens in the basepath following this pattern. Other patterns, including `/**`, `/something*`, or `/*something`, are not supported.  
**Description** | (Optional). A description for the API proxy.  
**Target/Backend target URL** | URL (including HTTP or HTTPS) of the backend service that this API proxy invokes.  
**Space** | (Optional) If your organization has Apigee Spaces enabled, you can associate the API proxy with a Space. For more information, see [Apigee Spaces overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).   
  
## Steps to create an API proxy

To create an API proxy using the UI or APIs:

### Apigee UI

To create a proxy in Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

**Note:** If you see the **Welcome to Apigee API Management** page, you need to [provision your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro) before proceeding further. 

After you have provisioned Apigee, close the UI and reopen the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee).

  2. In the **API Proxies** pane, click **\+ Create**.
  3. In the **Create a proxy** pane, under **Proxy template** , select **Reverse proxy (Most common)**.
  4. Under **Proxy details** , enter the following: 
     * **Proxy name:** Enter a name for the proxy, such as `myproxy`.
     * **Base Path** : Automatically set to the value you enter for `Proxy name`. The **Base Path** is part of the URL used to make requests to your API. Apigee uses the URL to match and route incoming requests to the appropriate API proxy.
     * **Description (Optional)** : Enter a description for your new API proxy, such as "Testing Apigee with a simple proxy."
     * **Target (Existing API):** Enter `https://mocktarget.apigee.net`. This defines the target URL that Apigee invokes on a request to the API proxy. The mocktarget service is hosted at Apigee and returns simple data. It requires no API key or access token.
     * **Space (Optional)** : If your organization has Apigee Spaces enabled, you can associate the API proxy with a Space selected from the list of available options. For more information, see [Apigee Spaces overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).
     * Click **Next**.
  5. **Deploy (optional)** : 
     * **Deployment environments** : Optional. Use the checkboxes to select one or more environments in which to deploy your proxy. If you prefer not to deploy the proxy at this point, leave the **Deployment environments** field empty. You can always deploy the proxy later.
     * **Service Account** : Optional. Attach a service account to your deployment to enable your proxy to access Google Cloud services, as specified in the service account's role and permissions.
  6. Click **Create**. 



Apigee creates the new proxy and displays a summary of the proxy details in the **Proxy summary** view.

![myproxy summary pane.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/myproxy-summary.png)

If you choose to deploy the proxy, the **Deployments** section displays the **Revision** number, which is 1 when you first deploy. The **Status** column displays the environments in which the proxy is deployed with a green status indicator.

### Apigee API

Create an API proxy in your Apigee organization by issuing a `POST` request to the following resource:
    
    
    https://apigee.googleapis.com/v1/organizations/**$ORG** /apis

You must define the name of the API proxy using the `name` query parameter. Restrict the characters used in the name to the following: `A-Za-z0-9._\-$ %`

Optionally, you can import an API proxy configuration bundle by performing the following steps: 

  * Set the `action` query parameter to `import`
  * Set the `Content-type` header to `multipart/form-data`
  * Pass the name of the API proxy configuration bundle on your local file system



The following example demonstrates how to create an API proxy by importing an API proxy configuration bundle (`helloworld-config.zip`) on your local file system using the API.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apis?name=helloworld&action=import" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: multipart/form-data" \
      -F "file=@helloworld-config.zip"

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output:
    
    
    {
      "basepaths": [
        "/helloworld"
      ],
      "configurationVersion": {
        "majorVersion": 4
      },
      "createdAt": "1559145292799",
      "displayName": "helloworld",
      "entityMetaDataAsProperties": {
        "bundle_type": "zip",
        "subType": "Proxy",
        "lastModifiedAt": "1559145292799",
        "createdAt": "1559145292799"
      },
      "lastModifiedAt": "1559145292799",
      "name": "helloworld",
      "policies": [
        "verify-api-key",
        "remove-query-param-apikey",
        "OAuth-v20-1"
      ],
      "proxies": [
        "default"
      ],
      "proxyEndpoints": [
        "default"
      ],
      "resourceFiles": {},
      "targetEndpoints": [
        "default"
      ],
      "targets": [
        "default"
      ],
      "type": "Application",
      "revision": "1",
      "description": "Hello world"
    }

For more information on creating an API proxy, see the [`apis.create` method](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/create) in the Apigee API. To see all the methods available for API proxies, see the [API proxies API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis).

## Next steps

After you create a simple API proxy, you typically do one of the following:

  * Add policies, security, and other features of the Apigee platform, as described in [Understanding APIs and API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies).
  * Deploy it to your cluster, as described in [Deploy an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
