---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments
title: REST Resource: organizations.environments.deployments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:52.401757+00:00
---

# REST Resource: organizations.environments.deployments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.environments.deployments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Deployment
    * JSON representation
  * PodStatus
    * JSON representation
  * RuntimeState
  * RoutingConflict
    * JSON representation
  * RoutingDeployment
    * JSON representation
  * InstanceDeploymentStatus
    * JSON representation
  * DeployedRevision
    * JSON representation
  * DeployedRoute
    * JSON representation
  * ProxyDeploymentType
  * Methods



## Resource: Deployment

Deployment represents a deployment of an API proxy or shared flow.

JSON representation  
---  
      
    
    {
      "environment": string,
      "apiProxy": string,
      "revision": string,
      "deployStartTime": string,
      "pods": [
        {
          object ([PodStatus](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#PodStatus))
        }
      ],
      "state": enum ([RuntimeState](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#RuntimeState)),
      "errors": [
        {
          object ([Status](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Status))
        }
      ],
      "routeConflicts": [
        {
          object ([RoutingConflict](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#RoutingConflict))
        }
      ],
      "instances": [
        {
          object ([InstanceDeploymentStatus](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#InstanceDeploymentStatus))
        }
      ],
      "serviceAccount": string,
      "proxyDeploymentType": enum ([ProxyDeploymentType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#ProxyDeploymentType))
    }  
  
Fields  
---  
`environment` |  `string` Environment.  
`apiProxy` |  `string` API proxy.  
`revision` |  `string` API proxy revision.  
`deployStartTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time the API proxy was marked `deployed` in the control plane in millisconds since epoch.  
`pods[]` |  `object (`[PodStatus](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#PodStatus)`)` Status reported by runtime pods.**Note** : **This field is deprecated**. Runtime versions 1.3 and above report instance level status rather than pod status.  
`state` |  `enum (`[RuntimeState](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#RuntimeState)`)` Current state of the deployment.**Note** : This field is displayed only when viewing deployment status.  
`errors[]` |  `object (`[Status](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Status)`)` Errors reported for this deployment. Populated only when state == ERROR.**Note** : This field is displayed only when viewing deployment status.  
`routeConflicts[]` |  `object (`[RoutingConflict](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#RoutingConflict)`)` Conflicts in the desired state routing configuration. The presence of conflicts does not cause the state to be `ERROR`, but it will mean that some of the deployment's base paths are not routed to its environment. If the conflicts change, the state will transition to `PROGRESSING` until the latest configuration is rolled out to all instances.**Note** : This field is displayed only when viewing deployment status.  
`instances[]` |  `object (`[InstanceDeploymentStatus](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#InstanceDeploymentStatus)`)` Status reported by each runtime instance.**Note** : This field is displayed only when viewing deployment status.  
`serviceAccount` |  `string` The full resource name of Cloud IAM Service Account that this deployment is using, eg, `projects/-/serviceAccounts/{email}`.  
`proxyDeploymentType` |  `enum (`[ProxyDeploymentType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#ProxyDeploymentType)`)` Output only. The type of the deployment (standard or extensible) Deployed proxy revision will be marked as extensible in following 2 cases. 1. The deployed proxy revision uses extensible policies. 2. If a environment supports flowhooks and flow hook is configured.  
  
## PodStatus

JSON representation  
---  
      
    
    {
      "podName": string,
      "appVersion": string,
      "podStatus": string,
      "podStatusTime": string,
      "deploymentStatusTime": string,
      "deploymentTime": string,
      "deploymentStatus": string,
      "statusCode": string,
      "statusCodeDetails": string
    }  
  
Fields  
---  
`podName` |  `string` Name of the pod which is reporting the status.  
`appVersion` |  `string` Version of the application running in the pod.  
`podStatus` |  `string` Overall status of the pod (not this specific deployment). Valid values include: - `active`: Up to date. - `stale` : Recently out of date.Pods that have not reported status in a long time are excluded from the output.  
`podStatusTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time the pod status was reported in milliseconds since epoch.  
`deploymentStatusTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time the deployment status was reported in milliseconds since epoch.  
`deploymentTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time the proxy was deployed in milliseconds since epoch.  
`deploymentStatus` |  `string` Status of the deployment. Valid values include: - `deployed`: Successful. - `error` : Failed. - `pending` : Pod has not yet reported on the deployment.  
`statusCode` |  `string` Code associated with the deployment status.  
`statusCodeDetails` |  `string` Human-readable message associated with the status code.  
  
## RuntimeState

State of the resource in the runtime.

Enums  
---  
`RUNTIME_STATE_UNSPECIFIED` | This value should never be returned.  
`READY` | Runtime has loaded the deployment.  
`PROGRESSING` | Deployment is not fully ready in the runtime.  
`ERROR` | Encountered an error with the deployment that requires intervention.  
  
## RoutingConflict

Describes a routing conflict that may cause a deployment not to receive traffic at some base path.

JSON representation  
---  
      
    
    {
      "environmentGroup": string,
      "conflictingDeployment": {
        object ([RoutingDeployment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#RoutingDeployment))
      },
      "description": string
    }  
  
Fields  
---  
`environmentGroup` |  `string` Name of the environment group in which this conflict exists.  
`conflictingDeployment` |  `object (`[RoutingDeployment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#RoutingDeployment)`)` Existing base path/deployment causing the conflict.  
`description` |  `string` Human-readable description of this conflict.  
  
## RoutingDeployment

Tuple representing a base path and the deployment containing it.

JSON representation  
---  
      
    
    {
      "basepath": string,
      "environment": string,
      "apiProxy": string,
      "revision": string
    }  
  
Fields  
---  
`basepath` |  `string` Base path receiving traffic.  
`environment` |  `string` Name of the environment in which the proxy is deployed.  
`apiProxy` |  `string` Name of the deployed API proxy revision containing the base path.  
`revision` |  `string` Name of the deployed API proxy revision containing the base path.  
  
## InstanceDeploymentStatus

The status of a deployment as reported by a single instance.

JSON representation  
---  
      
    
    {
      "instance": string,
      "deployedRevisions": [
        {
          object ([DeployedRevision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#DeployedRevision))
        }
      ],
      "deployedRoutes": [
        {
          object ([DeployedRoute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#DeployedRoute))
        }
      ]
    }  
  
Fields  
---  
`instance` |  `string` ID of the instance reporting the status.  
`deployedRevisions[]` |  `object (`[DeployedRevision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#DeployedRevision)`)` Revisions currently deployed in MPs.  
`deployedRoutes[]` |  `object (`[DeployedRoute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments#DeployedRoute)`)` Current routes deployed in the ingress routing table. A route which is missing will appear in `missingRoutes`.  
  
## DeployedRevision

Revisions deployed in the MPs.

JSON representation  
---  
      
    
    {
      "revision": string,
      "percentage": integer
    }  
  
Fields  
---  
`revision` |  `string` API proxy revision reported as deployed.  
`percentage` |  `integer` Percentage of MP replicas reporting this revision.  
  
## DeployedRoute

Route deployed in the ingress routing table.

JSON representation  
---  
      
    
    {
      "basepath": string,
      "envgroup": string,
      "environment": string,
      "percentage": integer
    }  
  
Fields  
---  
`basepath` |  `string` Base path in the routing table.  
`envgroup` |  `string` Environment group where this route is installed.  
`environment` |  `string` Destination environment. This will be empty if the route is not yet reported.  
`percentage` |  `integer` Percentage of ingress replicas reporting this route.  
  
## ProxyDeploymentType

ProxyDeploymentType specifies whether deployments contains only STANDARD type of proxies or both

Enums  
---  
`PROXY_DEPLOYMENT_TYPE_UNSPECIFIED` | Default value till public preview. After public preview this value should not be returned.  
`STANDARD` | Deployment will be of type Standard if only Standard proxies are used  
`EXTENSIBLE` | Proxy will be of type Extensible if deployments uses one or more Extensible proxies  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/get)`

|  Gets a particular deployment of Api proxy or a shared flow in an environment  
  
### `[getIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/getIamPolicy)`

|  Gets the IAM policy on a deployment.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/list)`

|  Lists all deployments of API proxies or shared flows in an environment.  
  
### `[setIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/setIamPolicy)`

|  Sets the IAM policy on a deployment, if the policy already exists it will be replaced.  
  
### `[testIamPermissions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/testIamPermissions)`

|  Tests the permissions of a user on a deployment, and returns a subset of permissions that the user has on the deployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
