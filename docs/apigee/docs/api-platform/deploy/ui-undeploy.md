---
url: https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-undeploy/
title: Undeploying an API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:48.657335+00:00
---

# Undeploying an API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-undeploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Undeploying an API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** To undeploy API proxies in environments enabled for [archive deployments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#deployment-types), see [Deploying and managing archives in an Apigee environment](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/manage-archive-deployments).

Undeploy an API proxy revision from your cluster as described in the following sections.

Note that when you undeploy a revision:

  * Apigee does not roll the revision back to the previously deployed revision.
  * After undeploying, no revisions of the API proxy are deployed in the environment.



Undeploying an API proxy is similar to [deleting an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-delete-proxy), except that when you undeploy a revision you can choose to edit it in the UI and later re-deploy it. If you _delete_ the API proxy, it is no longer available to edit.

### Apigee UI

To undeploy an API proxy using the UI:

  1. In the Google Cloud console, go to the **Apigee > Proxy Development > API Proxies** page.

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select the API proxy that you want to undeploy. The UI displays the API proxy's **Overview** view.

  3. In the **Deployments** section, click **Undeploy**. 

![Undeploy screenshot](https://docs.cloud.google.com/static/apigee/docs/api-platform/develop/images/undeploy.png)

  4. In the **Undeploy** dialog, click **Confirm**. 



### Apigee API

To undeploy an API proxy, use the following API call:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /apis/**$API** /revisions/**$REV** /deployments" \
      -X DELETE \
      -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output (an empty response):
    
    
    {}

For more information, see the [Undeploy API proxy revision API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/undeploy).

### gcloud

The following sections provide examples of using `gcloud alpha apigee` CLI commands to undeploy API proxy revisions and validate the undeployment. 

  * Undeploying an API proxy revision using the gcloud CLI
  * Validating the undeployment of an API proxy revision using the gcloud CLI



For more information and a description of the environment variables used in the examples, see [Getting started using gcloud with Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/gcloud-get-started).

#### Undeploying an API proxy revision using the gcloud CLI

To undeploy an API proxy revision, use the following gcloud command: 
    
    
    gcloud alpha apigee apis undeploy **$REV** --api=**$API** --environment=**$ENV**
    

The following provides an example of the response: 
    
    
    Using Apigee organization `my-org`

#### Validating the undeployment of an API proxy revision using the gcloud CLI

To validate that the API proxy revision has been undeployed from the environment, use the following gcloud command: 
    
    
    gcloud alpha apigee deployments list --api=**$API** --environment=**$ENV**
    

The following provides an example of the response: 
    
    
    Using Apigee organization `my-org`
    Listed 0 items.

For more information, see [List deployments CLI](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/list). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
