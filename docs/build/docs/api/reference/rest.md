---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/
title: Cloud Build API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:01:44.263991+00:00
---

# Cloud Build API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  Cloud Build API Stay organized with collections  Save and categorize content based on your preferences. 

Creates and manages builds on Google Cloud Platform.

  * REST Resource: v1
  * REST Resource: v1.githubDotComWebhook
  * REST Resource: v1.locations
  * REST Resource: v1.operations
  * REST Resource: v1.projects.builds
  * REST Resource: v1.projects.githubEnterpriseConfigs
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.bitbucketServerConfigs
  * REST Resource: v1.projects.locations.bitbucketServerConfigs.connectedRepositories
  * REST Resource: v1.projects.locations.bitbucketServerConfigs.repos
  * REST Resource: v1.projects.locations.builds
  * REST Resource: v1.projects.locations.githubEnterpriseConfigs
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.triggers
  * REST Resource: v1.projects.locations.workerPools
  * REST Resource: v1.projects.triggers



## Service: cloudbuild.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://cloudbuild.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://cloudbuild.googleapis.com`



### Regional service endpoint

A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 europe-west15 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8

  

* `https://cloudbuild.googleapis.com`

## REST Resource: [v1](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/TopLevel)

Methods  
---  
`[webhook](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/TopLevel/webhook)` |  `POST /v1/webhook`   
ReceiveWebhook is called when the API receives a GitHub webhook.  
  
## REST Resource: [v1.githubDotComWebhook](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/githubDotComWebhook)

Methods  
---  
`[receive](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/githubDotComWebhook/receive)` |  `POST /v1/githubDotComWebhook:receive`   
ReceiveGitHubDotComWebhook is called when the API receives a github.com webhook.  
  
## REST Resource: [v1.locations](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/locations)

Methods  
---  
`[regionalWebhook](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/locations/regionalWebhook)` |  `POST /v1/{location=locations/*}/regionalWebhook`   
ReceiveRegionalWebhook is called when the API receives a regional GitHub webhook.  
  
## REST Resource: [v1.operations](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/operations/cancel)` |  `POST /v1/{name=operations/**}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/operations/get)` |  `GET /v1/{name=operations/**}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.projects.builds](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds)

Methods  
---  
`[approve](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/approve)` |  `POST /v1/{name=projects/*/builds/*}:approve`   
Approves or rejects a pending build.  
`[cancel](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/cancel)` |  `POST /v1/projects/{projectId}/builds/{id}:cancel`   
Cancels a build in progress.  
`[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/create)` |  `POST /v1/projects/{projectId}/builds`   
Starts a build with the specified configuration.  
`[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/get)` |  `GET /v1/projects/{projectId}/builds/{id}`   
Returns information about a previously requested build.  
`[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/list)` |  `GET /v1/projects/{projectId}/builds`   
Lists previously requested builds.  
`[retry](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/retry)` |  `POST /v1/projects/{projectId}/builds/{id}:retry`   
Creates a new build based on the specified build.  
  
## REST Resource: [v1.projects.githubEnterpriseConfigs](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.githubEnterpriseConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.githubEnterpriseConfigs/create)` |  `POST /v1/{parent=projects/*}/githubEnterpriseConfigs`   
Create an association between a GCP project and a GitHub Enterprise server.  
`[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.githubEnterpriseConfigs/delete)` |  `DELETE /v1/{name=projects/*/githubEnterpriseConfigs/*}`   
Delete an association between a GCP project and a GitHub Enterprise server.  
`[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.githubEnterpriseConfigs/get)` |  `GET /v1/{name=projects/*/githubEnterpriseConfigs/*}`   
Retrieve a GitHubEnterpriseConfig.  
`[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.githubEnterpriseConfigs/list)` |  `GET /v1/{parent=projects/*}/githubEnterpriseConfigs`   
List all GitHubEnterpriseConfigs for a given project.  
`[patch](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.githubEnterpriseConfigs/patch)` |  `PATCH /v1/{githubEnterpriseConfig.name=projects/*/githubEnterpriseConfigs/*}`   
Update an association between a GCP project and a GitHub Enterprise server.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations)

Methods  
---  
`[getDefaultServiceAccount](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations/getDefaultServiceAccount)` |  `GET /v1/{name=projects/*/locations/*/defaultServiceAccount}`   
Returns the `DefaultServiceAccount` used by the project.  
  
## REST Resource: [v1.projects.locations.bitbucketServerConfigs](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/create)` |  `POST /v1/{parent=projects/*/locations/*}/bitbucketServerConfigs`   
Creates a new `BitbucketServerConfig`.  
`[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/bitbucketServerConfigs/*}`   
Delete a `BitbucketServerConfig`.  
`[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/get)` |  `GET /v1/{name=projects/*/locations/*/bitbucketServerConfigs/*}`   
Retrieve a `BitbucketServerConfig`.  
`[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/list)` |  `GET /v1/{parent=projects/*/locations/*}/bitbucketServerConfigs`   
List all `BitbucketServerConfigs` for a given project.  
`[patch](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/patch)` |  `PATCH /v1/{bitbucketServerConfig.name=projects/*/locations/*/bitbucketServerConfigs/*}`   
Updates an existing `BitbucketServerConfig`.  
`[removeBitbucketServerConnectedRepository](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs/removeBitbucketServerConnectedRepository)` |  `POST /v1/{config=projects/*/locations/*/bitbucketServerConfigs/*}:removeBitbucketServerConnectedRepository`   
Remove a Bitbucket Server repository from a given BitbucketServerConfig's connected repositories.  
  
## REST Resource: [v1.projects.locations.bitbucketServerConfigs.connectedRepositories](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs.connectedRepositories)

Methods  
---  
`[batchCreate](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs.connectedRepositories/batchCreate)` |  `POST /v1/{parent=projects/*/locations/*/bitbucketServerConfigs/*}/connectedRepositories:batchCreate`   
Batch connecting Bitbucket Server repositories to Cloud Build.  
  
## REST Resource: [v1.projects.locations.bitbucketServerConfigs.repos](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs.repos)

Methods  
---  
`[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs.repos/list)` |  `GET /v1/{parent=projects/*/locations/*/bitbucketServerConfigs/*}/repos`   
List all repositories for a given `BitbucketServerConfig`.  
  
## REST Resource: [v1.projects.locations.builds](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.builds)

Methods  
---  
`[approve](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.builds/approve)` |  `POST /v1/{name=projects/*/locations/*/builds/*}:approve`   
Approves or rejects a pending build.  
`[cancel](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.builds/cancel)` |  `POST /v1/{name=projects/*/locations/*/builds/*}:cancel`   
Cancels a build in progress.  
`[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.builds/create)` |  `POST /v1/{parent=projects/*/locations/*}/builds`   
Starts a build with the specified configuration.  
`[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.builds/get)` |  `GET /v1/{name=projects/*/locations/*/builds/*}`   
Returns information about a previously requested build.  
`[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.builds/list)` |  `GET /v1/{parent=projects/*/locations/*}/builds`   
Lists previously requested builds.  
`[retry](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.builds/retry)` |  `POST /v1/{name=projects/*/locations/*/builds/*}:retry`   
Creates a new build based on the specified build.  
  
## REST Resource: [v1.projects.locations.githubEnterpriseConfigs](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/create)` |  `POST /v1/{parent=projects/*/locations/*}/githubEnterpriseConfigs`   
Create an association between a GCP project and a GitHub Enterprise server.  
`[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/githubEnterpriseConfigs/*}`   
Delete an association between a GCP project and a GitHub Enterprise server.  
`[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/get)` |  `GET /v1/{name=projects/*/locations/*/githubEnterpriseConfigs/*}`   
Retrieve a GitHubEnterpriseConfig.  
`[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/list)` |  `GET /v1/{parent=projects/*/locations/*}/githubEnterpriseConfigs`   
List all GitHubEnterpriseConfigs for a given project.  
`[patch](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/patch)` |  `PATCH /v1/{githubEnterpriseConfig.name=projects/*/locations/*/githubEnterpriseConfigs/*}`   
Update an association between a GCP project and a GitHub Enterprise server.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.projects.locations.triggers](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers)

Methods  
---  
`[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/create)` |  `POST /v1/{parent=projects/*/locations/*}/triggers`   
Creates a new `BuildTrigger`.  
`[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/delete)` |  `DELETE /v1/{name=projects/*/locations/*/triggers/*}`   
Deletes a `BuildTrigger` by its project ID and trigger ID.  
`[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/get)` |  `GET /v1/{name=projects/*/locations/*/triggers/*}`   
Returns information about a `BuildTrigger`.  
`[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/list)` |  `GET /v1/{parent=projects/*/locations/*}/triggers`   
Lists existing `BuildTrigger`s.  
`[patch](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/patch)` |  `PATCH /v1/{trigger.resourceName=projects/*/locations/*/triggers/*}`   
Updates a `BuildTrigger` by its project ID and trigger ID.  
`[run](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/run)` |  `POST /v1/{name=projects/*/locations/*/triggers/*}:run`   
Runs a `BuildTrigger` at a particular source revision.  
`[webhook](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/webhook)` |  `POST /v1/{name=projects/*/locations/*/triggers/*}:webhook`   
ReceiveTriggerWebhook [Experimental] is called when the API receives a webhook request targeted at a specific trigger.  
  
## REST Resource: [v1.projects.locations.workerPools](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools)

Methods  
---  
`[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/create)` |  `POST /v1/{parent=projects/*/locations/*}/workerPools`   
Creates a `WorkerPool`.  
`[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/delete)` |  `DELETE /v1/{name=projects/*/locations/*/workerPools/*}`   
Deletes a `WorkerPool`.  
`[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/get)` |  `GET /v1/{name=projects/*/locations/*/workerPools/*}`   
Returns details of a `WorkerPool`.  
`[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/list)` |  `GET /v1/{parent=projects/*/locations/*}/workerPools`   
Lists `WorkerPool`s.  
`[patch](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/patch)` |  `PATCH /v1/{workerPool.name=projects/*/locations/*/workerPools/*}`   
Updates a `WorkerPool`.  
  
## REST Resource: [v1.projects.triggers](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers)

Methods  
---  
`[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/create)` |  `POST /v1/projects/{projectId}/triggers`   
Creates a new `BuildTrigger`.  
`[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/delete)` |  `DELETE /v1/projects/{projectId}/triggers/{triggerId}`   
Deletes a `BuildTrigger` by its project ID and trigger ID.  
`[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/get)` |  `GET /v1/projects/{projectId}/triggers/{triggerId}`   
Returns information about a `BuildTrigger`.  
`[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/list)` |  `GET /v1/projects/{projectId}/triggers`   
Lists existing `BuildTrigger`s.  
`[patch](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/patch)` |  `PATCH /v1/projects/{projectId}/triggers/{triggerId}`   
Updates a `BuildTrigger` by its project ID and trigger ID.  
`[run](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/run)` |  `POST /v1/projects/{projectId}/triggers/{triggerId}:run`   
Runs a `BuildTrigger` at a particular source revision.  
`[webhook](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers/webhook)` |  `POST /v1/projects/{projectId}/triggers/{trigger}:webhook`   
ReceiveTriggerWebhook [Experimental] is called when the API receives a webhook request targeted at a specific trigger.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
