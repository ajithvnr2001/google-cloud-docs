---
url: https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new/
title: Deploying an API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:39.385045+00:00
---

# Deploying an API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Deploying an API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** To deploy API proxies in environments enabled for [archive deployments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#deployment-types), see [Deploying and managing archives in an Apigee environment](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/manage-archive-deployments).

You cannot invoke an API proxy until it has been deployed. After you create a new API proxy or make a change to an existing one, you can deploy it to your cluster. 

When you create a new revision of an API proxy without changing its base path, then deploy it to an environment in which it's already deployed, the previous revision is undeployed and the new revision is deployed in its place. 

**Note:** You cannot make incremental changes to an API proxy revision and redeploy that same revision to Apigee. To deploy changes to an API proxy, you must [save it as a new revision](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-edit-proxy) and deploy it.

## Deploy an API proxy

Deploy an API proxy revision as described for one of the following methods. 

### Apigee UI

To deploy an API proxy:

  1. In the Google Cloud console, go to the **Apigee > Proxy Development > API Proxies** page.

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Click the API proxy that you want to deploy. The UI displays the **Overview** page:

![API proxy details including the deployment status per environment,
      the proxy endpoint details, and the target endpoint details.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/myproxy-in-overview.png)

  3. To deploy your changes, click **Deploy** to display the **Deploy** dialog: 

![Target endpoints selected in the Proxy Explorer.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/deploy-dialog.png)

  4. Enter the following: 
     * **Revision** : The revision number of the proxy you want to deploy.
     * **Environment** : The environment where you want to deploy the proxy.
     * **Service account** (optional): A [service account](https://cloud.google.com/iam/docs/service-accounts) for the proxy.
  5. Click **Deploy**.



The UI begins the process of deploying the selected revision.

**Note:** It may take a few minutes for Apigee to deploy the new proxy.

When the proxy is deployed, the **Status** column in the **Deployments** section displays a green icon to show that revision 1 of the proxy is deployed.

![Deployed proxy status icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/deployed-status.png)

### Apigee API

The following sections provide examples of using the Apigee API to deploy API proxy revisions and list the deployments for your organization.

  * Create a deployment change report before deploying
  * Deploying an API proxy revision using the API
  * Listing deployments of an API proxy using the API



See also [Viewing deployment status](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#viewing-deployment-status). 

**Note:** Apigee restricts the number of deployment requests processed per second. If you attempt a large number of deployment requests simultaneously, you may see deployment failures due to timeout errors.

#### Create a deployment change report before deploying

Deploying a proxy in more than one environment in the same environment group may lead to undefined behavior. To determine whether this will occur, you can generate a report using the [ `generateDeployChangeReport`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/generateDeployChangeReport#google.cloud.apigee.v1.DeploymentService.GenerateDeployChangeReport) method as follows:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /apis/**$API** /revisions/**$REV** /deployments:generateDeployChangeReport" \
    -X POST \
    -H "Authorization: Bearer $TOKEN"

This returns a [ deployment change report](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/DeploymentChangeReport) that warns you if a base path in the proxy you want to deploy will not receive traffic due to an existing deployment that is already using that base path.

####  Deploying an API proxy revision using the API 

To deploy an API proxy revision, use the following API call:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /apis/**$API** /revisions/**$REV** /deployments" \
      -X POST \
      -H "Authorization: Bearer $TOKEN"

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

**Key Point:** If an existing API proxy revision is deployed, set the `override` query parameter to `true`. In this case, Apigee deploys the new revision fully before undeploying the existing revision, as described in [Zero-downtime deployment](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#zero-downtime-deployment).

The following shows an example of the response output. In this example, revision `1` of the `helloworld` API proxy was deployed successfully to the `test` environment:
    
    
    {
      "environment": "test",
      "apiProxy": "helloworld",
      "revision": "1",
      "deployStartTime": "1559149080457"
    }

For more information, see [Deploy API proxy revision API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/deploy). 

####  Listing deployments using the API 

To list all deployments of API proxies and shared flows for your organization, enter the following API call:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /deployments" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

**Key Point:** When viewing a list of deployments, deployment status will not be provided. To view deployment status for an individual API proxy revision, see [Viewing deployment status](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#viewing-deployment-status).

The following provides an example of the response. In this example, there are three API proxies deployed, including `helloworld` which was deployed in the previous section.
    
    
    {
      "deployments": [
        {
          "environment": "test",
          "apiProxy": "helloworld",
          "revision": "1",
          "deployStartTime": "1559149080457"
        },
        {
          "environment": "test",
          "apiProxy": "weather",
          "revision": "1",
          "deployStartTime": "1558620435217"
        },
        {
          "environment": "test",
          "apiProxy": "testproxy",
          "revision": "2",
          "deployStartTime": "1558635113086"
        }
      ]
    }

  


### gcloud

The following sections provide examples of using `gcloud apigee` CLI commands to deploy API proxy revisions and list the deployments for your organization. 

  * Deploying an API proxy revision using the gcloud CLI
  * Listing deployments of an API proxy using the gcloud CLI



See also [Viewing deployment status](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#viewing-deployment-status). 

For more information and a description of the environment variables used in the examples, see [Getting started using gcloud with Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/gcloud-get-started).

#### Deploying an API proxy revision using the gcloud CLI

To deploy an API proxy revision, use the following `gcloud` command: 
    
    
    gcloud apigee apis deploy **$REV** --api=**$API** --environment=**$ENV**

**Key Point** : If an existing API proxy revision is deployed, set the `override` flag to `true`. In this case, Apigee deploys the new revision fully before undeploying the existing revision, as described in [Zero-downtime deployment](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#zero-downtime-deployment).

The following shows an example of the response output. In this example, revision `1` of the `helloworld` API proxy was deployed successfully to the `test` environment:
    
    
    Using Apigee organization 'my-org'
    apiProxy: helloworld
    deployStartTime: '1598032332802'
    environment: test
    revision: '1'

For more information, see [Deploy API proxy revision CLI](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/deploy).

#### Listing deployments using the gcloud CLI

To list all deployments of API proxies and shared flows for your organization, use the following `gcloud` command: 
    
    
    gcloud apigee deployments list

**Key Point:** When viewing a list of deployments, deployment status will not be provided. To view deployment status for an individual API proxy, see [Viewing deployment status](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#viewing-deployment-status).

The following provides an example of the response. In this example, there are three API proxies deployed, including `helloworld` which was deployed in the previous section.
    
    
    Using Apigee organization `my-org`
     - apiProxy: helloworld
       deployStartTime: 1598032332802
       environment: test
       revision: 1
     - apiProxy: weather
       deployStartTime: 1558620435217
       environment: test
       revision: 1
     - apiProxy: testproxy
       deployStartTime: 1558635113086
       environment: test
       revision: 2

For more information, see [List deployments CLI](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/list). 

## Troubleshooting

If you are unable to deploy your API proxy, check to see if one of the following common scenarios may apply.

### Naming restrictions for environment groups

If the name of your environment group does not comply with naming restrictions your proxy will not deploy. In some cases, it is possible to create an environment group and add environments to it without having to meet these restrictions. However, this will prevent proxy deployment.

See [Creating environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#groups) for a description of naming guidelines and restrictions.

### Environment created with a previously used environment name

If you create an environment with the same name as an environment that was previously deleted, your proxy will not deploy. For example, if you created an environment named `prod-1` after previously creating and deleting a `prod-1` environment, you will need to remove it. You can use the following steps to resolve this issue: 

  1. Detach the `prod-1` environment from your environment group using the [ API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments/delete).
  2. Delete the `prod-1` environment using the [API](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/delete).
  3. Create a new environment. For example, `prod-2`.
  4. Attach the new `prod-2` environment to your environment group using the [ API.](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments/create)

**Note:** To resolve deployment issues, see [deployment errors](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/deployment/apigee-serving-cert-not-found-or-expired). For policy related issues, see [policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/introduction).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
