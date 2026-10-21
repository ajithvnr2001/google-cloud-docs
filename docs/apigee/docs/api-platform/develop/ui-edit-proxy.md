---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-edit-proxy/
title: Editing an API proxy (create a proxy revision) \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:09.233083+00:00
---

# Editing an API proxy (create a proxy revision)  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-edit-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Editing an API proxy (create a proxy revision) Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**More Information**  
For more information, see:

  * [Best practices for API proxy design and development](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development)



Use the Apigee UI or API to edit an API proxy. Editing an API proxy can include configuring [policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy), configuring [ proxy endpoints](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-routes#determiningtheurloftheapiproxyendpoint), [ target endpoints](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-routes#determiningtheurlofthetargetendpoint), and [integration endpoints](https://docs.cloud.google.com/apigee/docs/api-platform/integration/getting-started-apigee-target-endpoint), adding or removing [flow hooks](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-hooks), and [deploying the proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new). 

When you edit an API proxy, you can decide which of the following to do with the resulting changes:

  1. Save your changes on the server but do not create a new revision. You do this when you do not want to deploy your saved changes, but just want to ensure that they are not lost if you end the session.  


**OR**

  2. Create a new API proxy revision and deploy it to the cluster. You cannot deploy changes to an API proxy without creating a new revision of it.



### Apigee UI

To edit an API proxy and save your changes using the Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select the proxy that you want to edit from the list of proxies. The UI displays the **Overview** tab for that proxy in the Google Cloud console.

![Overview tab in the Proxy Editor](https://docs.cloud.google.com/static/apigee/docs/api-platform/develop/images/overview-tab-with-deployed-proxy.png)
  3. Click the **Develop** tab to make your changes to the proxy.  
  
For example, to add a policy, click the **+** icon next to **Policies** , select the policy to add, enter a name and an optional display name, click **Create** , and configure the policy in the interface.   
![Add policy using the UI](https://docs.cloud.google.com/static/apigee/docs/api-platform/develop/images/edit-proxy-add-policy.png)
  4. When you are done making changes, you can do one of the following: 
     * To save your changes but _not_ create a new revision, click the **Save** button. (You should do this periodically to ensure that your changes are not lost if you end the session). 
     * To save your changes as a new revision (when you are getting ready to deploy and test), click the drop-down menu next to the **Save** button and select **Save as new revision** : 

![Save changes as new revision in the Save menu.](https://docs.cloud.google.com/static/apigee/docs/api-platform/develop/images/save-as-new-revision.png)

The Apigee UI saves your changes and generates a new revision of the proxy for you. It does not deploy the new bundle to the runtime; you must explicitly do that, as described in [Deploying an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new). 




### Apigee API

Edit an API proxy to create a revision in your Apigee organization by issuing a `POST` request to the following resource:
    
    
    https://apigee.googleapis.com/v1/organizations/**$ORG** /apis

You must define the name of the API proxy using the `name` query parameter. Restrict the characters used in the name to the following: `A-Za-z0-9._\-$ %`

Optionally, you can import an API proxy configuration bundle by performing the following steps: 

  * Set the `action` query parameter to `import`
  * Set the `Content-type` header to `multipart/form-data`
  * Pass the name of the API proxy configuration bundle on your local file system



The following example demonstrates how to edit an API proxy by importing an API proxy configuration bundle (`helloworld-config.zip`) on your local file system using the API.
    
    
    export TOKEN=$(gcloud auth print-access-token)
    export ORG=ORGANIZATION_NAME
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apis?name=helloworld&action=import" \
      -X POST \
      -H "Authorization: Bearer **$TOKEN** " \
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

For more information on editing an API proxy, see the [`apis.create` method](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/create) in the Apigee API. To see all the methods available for API proxies, see the [API proxies API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
