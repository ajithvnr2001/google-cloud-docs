---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/undeploy/
title: Method: organizations.environments.apis.revisions.deployments.undeploy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:50.778341+00:00
---

# Method: organizations.environments.apis.revisions.deployments.undeploy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/undeploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.apis.revisions.deployments.undeploy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Undeploys an API proxy revision from an environment.

For a request path `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}/deployments`, two permissions are required:

  * `apigee.deployments.delete` on the resource `organizations/{org}/environments/{env}`
  * `apigee.proxyrevisions.undeploy` on the resource `organizations/{org}/apis/{api}/revisions/{rev}`



### HTTP request

`DELETE https://apigee.googleapis.com/v1/{name=organizations/*/environments/*/apis/*/revisions/*}/deployments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the API proxy revision deployment in the following format: `organizations/{org}/environments/{env}/apis/{api}/revisions/{rev}`If the API proxy resource has the `space` attribute set, IAM permissions are checked differently . To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).  
  
### Query parameters

Parameters  
---  
`sequencedRollout` |  `boolean` Flag that specifies whether to enable sequenced rollout.If set to `true`, the environment group routing rules corresponding to this deployment will be removed before removing the deployment from the runtime. This is likely to be a rare use case; it is only needed when the intended effect of undeploying this proxy is to cause the traffic it currently handles to be rerouted to some other existing proxy in the environment group.The [deployments.generateUndeployChangeReport API][DeploymentService.GenerateUndeployChangeReport] may be used to examine routing changes before issuing the undeployment request, and its response will indicate if a sequenced rollout is recommended for the undeployment.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
