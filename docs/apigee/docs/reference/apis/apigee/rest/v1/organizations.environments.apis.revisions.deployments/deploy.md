---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/deploy/
title: Method: organizations.environments.apis.revisions.deployments.deploy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:50.256873+00:00
---

# Method: organizations.environments.apis.revisions.deployments.deploy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.apis.revisions.deployments.deploy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Deploys a revision of an API proxy.

If another revision of the same API proxy revision is currently deployed, set the `override` parameter to `true` to have this revision replace the currently deployed revision.

You cannot invoke an API proxy until it has been deployed to an environment. After you deploy an API proxy revision, you cannot edit it. To edit the API proxy, you must create and deploy a new revision.

For a request path `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments`, two permissions are required:

  * `apigee.deployments.create` on the resource `organizations/{org}/environments/{env}`
  * `apigee.proxyrevisions.deploy` on the resource `organizations/{org}/apis/{api}/revisions/{rev}`



All successful API proxy deployments to Apigee are [zero-downtime deployments](https://cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#zero-downtime-deployment).

Apigee hybrid validates the dependencies between shared flows and API proxies at deployment time. For example, if the Flow Callout policy in an API proxy references a shared flow that either doesn't exist or isn't deployed, the API proxy deployment fails.

### HTTP request

`POST https://apigee.googleapis.com/v1/{name=organizations/*/environments/*/apis/*/revisions/*}/deployments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the API proxy revision deployment in the following format: `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}`If the API proxy resource being deployed has the `space` attribute set, IAM permissions are checked differently . To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).  
  
### Query parameters

Parameters  
---  
`override` |  `boolean` Flag that specifies whether the new deployment replaces other deployed revisions of the API proxy in the environment. Set `override` to `true` to replace other deployed revisions. By default, `override` is `false` and the deployment is rejected if other revisions of the API proxy are deployed in the environment.  
`sequencedRollout` |  `boolean` Flag that specifies whether to enable sequenced rollout.If set to `true`, the routing rules for this deployment and the environment changes to add the deployment will be rolled out in a safe order. This reduces the risk of downtime that could be caused by changing the environment group's routing before the new destination for the affected traffic is ready to receive it. This should only be necessary if the new deployment will be capturing traffic from another environment under a shared environment group or if traffic will be rerouted to a different environment due to a base path removal.The [generateDeployChangeReport API][DeploymentService.GenerateDeployChangeReport] may be used to examine routing changes before issuing the deployment request, and its response will indicate if a sequenced rollout is recommended for the deployment.  
`serviceAccount` |  `string` Google Cloud IAM service account.The service account represents the identity of the deployed proxy, and determines what permissions it has. The format must be `{ACCOUNT_ID}@{PROJECT}.iam.gserviceaccount.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceAccount`:

  * `iam.serviceAccounts.actAs`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Deployment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#Deployment)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
