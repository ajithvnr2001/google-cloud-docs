---
url: https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview/
title: Deployment overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:47.774880+00:00
---

# Deployment overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Deployment overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** To deploy API proxies in environments enabled for [archive deployments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#deployment-types), see [Deploying and managing archives in an Apigee environment](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/manage-archive-deployments).

When you make a change to an API proxy, you can save it as a new revision and deploy it to your cluster.

**Quick Start:**

  * [Deploying an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new)
  * [Undeploying an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-undeploy)



## About deployment

The deployment lifecycle of an API proxy revision on Apigee is shown in the following figure.

**Note:** In Apigee, MPs act independently of one another and any given MP can be in a different state than the other MPs (such as active or disabled). This is known as an _eventually consistent_ deployment model for API proxies.

![Apigee API proxy deployment lifecycle showing management plane, runtime plane, and Cloud Operations title=](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/arch-deploylifecycle.png)

## API proxy revisions limitations

The following limitations apply to API proxy revisions:

  * If you make any changes to an API proxy, you must deploy it as a new revision.
  * After you deploy an API proxy, the revision is read-only. You cannot change an API proxy revision (such as to make incremental changes); the only way to _change_ a revision is to create a new revision and deploy it.
  * MPs can deploy a proxy bundle only in its entirety. If you make changes to individual fragments or policies, the MPs will still deploy the entire proxy bundle.
  * If your Apigee usage distinguishes between [Standard and Extensible proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types), when deploying a revision that changes an API proxy from a Standard proxy to an Extensible proxy: 
    * a cost might be incurred. If you are a Pay-as-you-go customer, see the [Pay-as-you-go entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-entitlements). If you are a Subscription customer, see your plan's details. 
    * the deployment requires additional time. During the deployment window the API call flow is not disrupted but you can't deploy, undeploy, or delete the proxy. Also, current or new revisions cannot be deleted during the deployment window. Changes to the API proxy and new revision creation are allowed.



## Zero-downtime deployment

All successful API proxy deployments to Apigee, are _zero-downtime deployments_. API proxy deployments happen in this order:

  1. Revision 1 of the API proxy `/hello` is deployed and handling traffic.
  2. Revision 2 of `/hello` is deployed.
  3. Revision 2 is deployed to the Message Processors in the runtime plane.
  4. Revision 1 is undeployed.



The API proxy revision deployment is now complete with no downtime.

**Note:** If the deployment of Revision 2 _fails_ for any reason, the previous version, Revision 1 is still undeployed. In this case, you can re-deploy the previous revision to restore it. Then, you can fix the new revision and deploy it.

## Viewing deployment status

Deploying an API proxy on Apigee does not make it immediately available. It takes time for the API proxy to be synchronized across all MPs in the runtime plane. However, Apigee provides tools that can give you some information about the status of your API proxy revisions.

### Apigee UI

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select the desired API proxy; the status is displayed in the **Deployments** section.

The Apigee UI uses the following icons to give a quick status for each API proxy:

![Gray dot icon indicates API proxy is not deployed to selected environment](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ui-gray-dot.png) Indicates that the API proxy has not been deployed to the selected environment.  
![Green dot icon indicates API proxy deployed without errors or warnings in selected environment](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ui-green-dot.png) Indicates that there are no errors or warnings for that proxy in the selected environment.  
![Yellow triange icon indicates that some routing did not update due to base path conflicts](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ui-yellow-triangle.png) Indicates that some routing did not update due to base path conflicts.  
![Red box icon indicates there was an error during deployment](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ui-red-box.png) Indicates that there was an error deploying the API proxy.




### Apigee API

To view the deployment status of your API proxy revision in an environment, use the following API call: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /apis/**$API** /revisions/**$REV** /deployments" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response. This examples shows deployment status for revision `1` of the `helloworld` API proxy that is deployed in the `test` environment:
    
    
    {
      "environment": "test",
      "apiProxy": "helloworld",
      "revision": "1",
      "deployStartTime": "1559149080457",
      "pods": [
        {
          "podName": "apigee-runtime-myorg-test-f8bdf9d-2s72w",
          "deploymentStatus": "deployed",
          "statusCodeDetails": "Deployment Success",
          "podStatus": "active",
          "podStatusTime": "1595357668001"
        }
      ],
      "state": "READY"
    }

For more information, see the [API proxy revision environment deployments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments).

### gcloud

To view the deployment status of your API proxy revision in an environment, use the following gcloud command: 
    
    
    gcloud alpha apigee deployments describe --api=**$API** --environment=**$ENV**
    

For more information and a description of the environment variables used in the examples, see [Getting started using gcloud with Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/gcloud-get-started).

The following provides an example of the response. This examples shows deployment status for revision `1` of the `helloworld` API proxy that is deployed in the `test` environment: 
    
    
    Using Apigee organization `my-org`
    Using deployed revision `1`
    apiProxy: helloworld
    deployStartTime: '1598032332802'
    environment: test
    pods:
    - deploymentStatus: deployed
      podName: apigee-runtime-myorg-test-f8bdf9d-2s72w
      podStatus: active
      podStatusTime: '1598302128087'
      statusCodeDetails: Deployment Success
    revision: '1'
    state: READY

For more information, see [Describe deployments CLI](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe).

## View proxy deployment usage

The usage of API proxies in your organization may be subject to a deployments quota, which is a limit on how many deployment units you can use at a time. See your entitlements ([Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-entitlements) or [Subscription](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements)) for details. You can view your organization's proxy deployment usage from several places within the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee), as described below. 

**Note** : If your organization is Apigee hybrid-enabled, only a sub-set of these usage metrics are displayed.

### View deployment usage on the Apigee Overview page

To view your API proxy deployment usage from the Apigee **Overview** page: 

  1. In the Google Cloud console, go to the **Apigee > Overview** page.

[Go to Overview](https://cloud.google.com/console/apigee/overview)

  2. You can view proxy deployment usage for your organization at a glance using the **Proxy Usage** card, which displays the following information for your organization: 
     * **Total proxies created** : The total number of API proxies created, including deployed and undeployed proxies.
     * **Proxies deployed** : The total number of API proxies deployed across all environment(s) in the organization.
     * **Proxy deployment units** : The total number of API proxy or shared flow revisions deployed in your organization. Each deployment per environment, per instance, is counted as one unit.
     * **Proxies and shared flows deployed against limit** : Total number of API proxies and shared flows deployed in the organization, against the limit for your organization type.
     * **Extensible deployment units** : The number of extensible API proxy revisions deployed in your organization. Each deployment per environment, per instance, is counted as one unit.
     * **Standard deployment units** : The number of standard API proxy revisions deployed in your organization. Each deployment per environment, per instance, is counted as one unit.



### View deployment usage on the API Proxies page

To view your API proxy deployment usage from the **API Proxies** page: 

  1. In the Google Cloud console, go to the **API Proxies** page.

[Go to API Proxies](https://cloud.google.com/console/apigee/proxies)

  2. The **API Proxies** page displays the following information: 
     * **Total proxies created** : The total number of API proxies developed in your organization, including deployed and undeployed proxies.
     * **Proxies deployed** : The total number of API proxy revisions deployed across all environments in your organization.
     * **Proxy deployment units** : The total number of API proxy or shared flow revisions deployed across all environments in your organization. Each deployment per environment, per instance, is counted as one unit.
     * **Extensible proxy deployment units** : The number of extensible API proxy revisions deployed across all environments in your organization. Each deployment per environment, per instance, is counted as one unit.
     * **Standard proxy deployment units** : The number of standard API proxy revisions deployed across all environments in your organization. Each deployment per environment, per instance, is counted as one unit.



### View deployment usage on the Environments page

To view your API proxy deployment usage from the **Environments** page: 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://cloud.google.com/console/apigee/environments)

  2. Select the **Environments** overview tab to display the following information for all of the environments: 
     * **Total proxy deployment units** : The total number of API proxy or shared flow revisions deployed across all environments in your organization.
     * **Extensible proxy deployment units** : The number of extensible API proxy revisions deployed across all environments in your organization. Each deployment per environment, per instance, is counted as one unit.
     * **Standard proxy deployment units** : The number of standard API proxy revisions deployed across all environments in your organization. Each deployment per environment, per instance, is counted as one unit.
     * **Shared flow deployment units** : The total number of shared flow revisions deployed across all environments in your organization. Each deployment per environment, per instance, is counted as one unit.
  3. To view proxy deployment usage for a single environment: 
     1. In the **Environments** list, select an environment name to view its details.
     2. Select the **Deployments** tab to view deployment unit usage for the selected environment.



## Next steps

Learn how to deploy: [Deploying an API Proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new) |  Learn how to undeploy: [Undeploying an API Proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-undeploy)  
---|---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
  *[MPs]: Message Processors
