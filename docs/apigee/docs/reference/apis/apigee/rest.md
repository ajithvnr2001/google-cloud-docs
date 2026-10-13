---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/
title: Apigee API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:09.603087+00:00
---

# Apigee API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Apigee API Stay organized with collections  Save and categorize content based on your preferences. 

Use the Apigee API to programmatically develop and manage APIs with a set of RESTful operations. Develop and secure API proxies, deploy and undeploy API proxy revisions, monitor APIs, configure environments, manage users, and more.

Note: This product is available as a free trial for a time period of 60 days.

  * REST Resource: v1.organizations
  * REST Resource: v1.organizations.analytics.datastores
  * REST Resource: v1.organizations.apimServiceExtensions
  * REST Resource: v1.organizations.apiproducts
  * REST Resource: v1.organizations.apiproducts.attributes
  * REST Resource: v1.organizations.apiproducts.rateplans
  * REST Resource: v1.organizations.apis
  * REST Resource: v1.organizations.apis.debugsessions
  * REST Resource: v1.organizations.apis.deployments
  * REST Resource: v1.organizations.apis.keyvaluemaps
  * REST Resource: v1.organizations.apis.keyvaluemaps.entries
  * REST Resource: v1.organizations.apis.revisions
  * REST Resource: v1.organizations.apis.revisions.deployments
  * REST Resource: v1.organizations.appgroups
  * REST Resource: v1.organizations.appgroups.apps
  * REST Resource: v1.organizations.appgroups.apps.keys
  * REST Resource: v1.organizations.appgroups.apps.keys.apiproducts
  * REST Resource: v1.organizations.appgroups.balance
  * REST Resource: v1.organizations.appgroups.subscriptions
  * REST Resource: v1.organizations.apps
  * REST Resource: v1.organizations.datacollectors
  * REST Resource: v1.organizations.deployments
  * REST Resource: v1.organizations.developers
  * REST Resource: v1.organizations.developers.apps
  * REST Resource: v1.organizations.developers.apps.attributes
  * REST Resource: v1.organizations.developers.apps.keys
  * REST Resource: v1.organizations.developers.apps.keys.apiproducts
  * REST Resource: v1.organizations.developers.apps.keys.create
  * REST Resource: v1.organizations.developers.attributes
  * REST Resource: v1.organizations.developers.balance
  * REST Resource: v1.organizations.developers.subscriptions
  * REST Resource: v1.organizations.dnsZones
  * REST Resource: v1.organizations.endpointAttachments
  * REST Resource: v1.organizations.envgroups
  * REST Resource: v1.organizations.envgroups.attachments
  * REST Resource: v1.organizations.environments
  * REST Resource: v1.organizations.environments.addonsConfig
  * REST Resource: v1.organizations.environments.analytics.admin
  * REST Resource: v1.organizations.environments.analytics.exports
  * REST Resource: v1.organizations.environments.apis.deployments
  * REST Resource: v1.organizations.environments.apis.revisions
  * REST Resource: v1.organizations.environments.apis.revisions.debugsessions
  * REST Resource: v1.organizations.environments.apis.revisions.debugsessions.data
  * REST Resource: v1.organizations.environments.apis.revisions.deployments
  * REST Resource: v1.organizations.environments.archiveDeployments
  * REST Resource: v1.organizations.environments.caches
  * REST Resource: v1.organizations.environments.deployments
  * REST Resource: v1.organizations.environments.flowhooks
  * REST Resource: v1.organizations.environments.keystores
  * REST Resource: v1.organizations.environments.keystores.aliases
  * REST Resource: v1.organizations.environments.keyvaluemaps
  * REST Resource: v1.organizations.environments.keyvaluemaps.entries
  * REST Resource: v1.organizations.environments.optimizedStats
  * REST Resource: v1.organizations.environments.queries
  * REST Resource: v1.organizations.environments.references
  * REST Resource: v1.organizations.environments.resourcefiles
  * REST Resource: v1.organizations.environments.securityActions
  * REST Resource: v1.organizations.environments.securityIncidents
  * REST Resource: v1.organizations.environments.securityReports
  * REST Resource: v1.organizations.environments.securityStats
  * REST Resource: v1.organizations.environments.sharedflows.deployments
  * REST Resource: v1.organizations.environments.sharedflows.revisions
  * REST Resource: v1.organizations.environments.stats
  * REST Resource: v1.organizations.environments.targetservers
  * REST Resource: v1.organizations.environments.traceConfig.overrides
  * REST Resource: v1.organizations.hostQueries
  * REST Resource: v1.organizations.hostSecurityReports
  * REST Resource: v1.organizations.hostStats
  * REST Resource: v1.organizations.instances
  * REST Resource: v1.organizations.instances.attachments
  * REST Resource: v1.organizations.instances.natAddresses
  * REST Resource: v1.organizations.keyvaluemaps
  * REST Resource: v1.organizations.keyvaluemaps.entries
  * REST Resource: v1.organizations.operations
  * REST Resource: v1.organizations.optimizedHostStats
  * REST Resource: v1.organizations.reports
  * REST Resource: v1.organizations.securityAssessmentResults
  * REST Resource: v1.organizations.securityFeedback
  * REST Resource: v1.organizations.securityMonitoringConditions
  * REST Resource: v1.organizations.securityProfiles
  * REST Resource: v1.organizations.securityProfiles.environments
  * REST Resource: v1.organizations.securityProfilesV2
  * REST Resource: v1.organizations.sharedflows
  * REST Resource: v1.organizations.sharedflows.deployments
  * REST Resource: v1.organizations.sharedflows.revisions
  * REST Resource: v1.organizations.sharedflows.revisions.deployments
  * REST Resource: v1.organizations.sites.apicategories
  * REST Resource: v1.organizations.sites.apidocs
  * REST Resource: v1.organizations.spaces
  * REST Resource: v1.projects



## Service: apigee.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://apigee.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://apigee.googleapis.com`



## REST Resource: [v1.organizations](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/create)` |  `POST /v1/organizations`   
Creates an Apigee organization.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete)` |  `DELETE /v1/{name=organizations/*}`   
Delete an Apigee organization.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get)` |  `GET /v1/{name=organizations/*}`   
Gets the profile for an Apigee organization.  
`[getControlPlaneAccess](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/getControlPlaneAccess)` |  `GET /v1/{name=organizations/*/controlPlaneAccess}`   
Lists the service accounts allowed to access Apigee control plane directly for limited functionality.  
`[getProjectMapping](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/getProjectMapping)` |  `GET /v1/{name=organizations/*}:getProjectMapping`   
Gets the project ID and region for an Apigee organization.  
`[getSecuritySettings](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/getSecuritySettings)` |  `GET /v1/{name=organizations/*/securitySettings}`   
GetSecuritySettings gets the security settings for API Security.  
`[getSyncAuthorization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/getSyncAuthorization)` |  `POST /v1/{name=organizations/*}:getSyncAuthorization`   
Lists the service accounts with the permissions required to allow the Synchronizer to download environment data from the control plane.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/list)` |  `GET /v1/{parent=organizations}`   
Lists the Apigee organizations and associated Google Cloud projects that you have permission to access.  
`[setAddons](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setAddons)` |  `POST /v1/{org=organizations/*}:setAddons`   
Configures the add-ons for the Apigee organization.  
`[setSyncAuthorization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setSyncAuthorization)` |  `POST /v1/{name=organizations/*}:setSyncAuthorization`   
Sets the permissions required to allow the Synchronizer to download environment data from the control plane.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/update)` |  `PUT /v1/{name=organizations/*}`   
Updates the properties for an Apigee organization.  
`[updateControlPlaneAccess](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/updateControlPlaneAccess)` |  `PATCH /v1/{controlPlaneAccess.name=organizations/*/controlPlaneAccess}`   
Updates the permissions required to allow Apigee runtime-plane components access to the control plane.  
`[updateSecuritySettings](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/updateSecuritySettings)` |  `PATCH /v1/{securitySettings.name=organizations/*/securitySettings}`   
UpdateSecuritySettings updates the current security settings for API Security.  
  
## REST Resource: [v1.organizations.analytics.datastores](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/create)` |  `POST /v1/{parent=organizations/*}/analytics/datastores`   
Create a Datastore for an org  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/delete)` |  `DELETE /v1/{name=organizations/*/analytics/datastores/*}`   
Delete a Datastore from an org.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/get)` |  `GET /v1/{name=organizations/*/analytics/datastores/*}`   
Get a Datastore  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/list)` |  `GET /v1/{parent=organizations/*}/analytics/datastores`   
List Datastores  
`[test](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/test)` |  `POST /v1/{parent=organizations/*}/analytics/datastores:test`   
Test if Datastore configuration is correct.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/update)` |  `PUT /v1/{name=organizations/*/analytics/datastores/*}`   
Update a Datastore  
  
## REST Resource: [v1.organizations.apimServiceExtensions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions/create)` |  `POST /v1/{parent=organizations/*}/apimServiceExtensions`   
Creates an APIM ServiceExtension in an organization.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions/delete)` |  `DELETE /v1/{name=organizations/*/apimServiceExtensions/*}`   
Deletes APIM service extension from an organization.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions/get)` |  `GET /v1/{name=organizations/*/apimServiceExtensions/*}`   
Gets APIM service extension details.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions/list)` |  `GET /v1/{parent=organizations/*}/apimServiceExtensions`   
Lists all APIM service extensions in an organization.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions/patch)` |  `PATCH /v1/{apimServiceExtension.name=organizations/*/apimServiceExtensions/*}`   
Updates an APIM service extension in an organization.  
  
## REST Resource: [v1.organizations.apiproducts](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts)

Methods  
---  
`[attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/attributes)` |  `POST /v1/{name=organizations/*/apiproducts/*}/attributes`   
Updates or creates API product attributes.  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/create)` |  `POST /v1/{parent=organizations/*}/apiproducts`   
Creates an API product in an organization.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/delete)` |  `DELETE /v1/{name=organizations/*/apiproducts/*}`   
Deletes an API product from an organization.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/get)` |  `GET /v1/{name=organizations/*/apiproducts/*}`   
Gets configuration details for an API product.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/list)` |  `GET /v1/{parent=organizations/*}/apiproducts`   
Lists all API product names for an organization.  
`[move](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/move)` |  `POST /v1/{name=organizations/*/apiproducts/*}:move`   
Moves an API product to a different space.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/update)` |  `PUT /v1/{name=organizations/*/apiproducts/*}`   
Updates an existing API product.  
  
## REST Resource: [v1.organizations.apiproducts.attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts/attributes)

Methods  
---  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes/delete)` |  `DELETE /v1/{name=organizations/*/apiproducts/*/attributes/*}`   
Deletes an API product attribute.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes/get)` |  `GET /v1/{name=organizations/*/apiproducts/*/attributes/*}`   
Gets the value of an API product attribute.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes/list)` |  `GET /v1/{parent=organizations/*/apiproducts/*}/attributes`   
Lists all API product attributes.  
`[updateApiProductAttribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes/updateApiProductAttribute)` |  `POST /v1/{name=organizations/*/apiproducts/*/attributes/*}`   
Updates the value of an API product attribute.  
  
## REST Resource: [v1.organizations.apiproducts.rateplans](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/create)` |  `POST /v1/{parent=organizations/*/apiproducts/*}/rateplans`   
Create a rate plan that is associated with an API product in an organization.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/delete)` |  `DELETE /v1/{name=organizations/*/apiproducts/*/rateplans/*}`   
Deletes a rate plan.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/get)` |  `GET /v1/{name=organizations/*/apiproducts/*/rateplans/*}`   
Gets the details of a rate plan.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/list)` |  `GET /v1/{parent=organizations/*/apiproducts/*}/rateplans`   
Lists all the rate plans for an API product.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/update)` |  `PUT /v1/{name=organizations/*/apiproducts/*/rateplans/*}`   
Updates an existing rate plan.  
  
## REST Resource: [v1.organizations.apis](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/create)` |  `POST /v1/{parent=organizations/*}/apis`   
Creates an API proxy.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/delete)` |  `DELETE /v1/{name=organizations/*/apis/*}`   
Deletes an API proxy and all associated endpoints, policies, resources, and revisions.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/get)` |  `GET /v1/{name=organizations/*/apis/*}`   
Gets an API proxy including a list of existing revisions.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/list)` |  `GET /v1/{parent=organizations/*}/apis`   
Lists the names of all API proxies in an organization.  
`[move](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/move)` |  `POST /v1/{name=organizations/*/apis/*}:move`   
Moves an API proxy to a different space.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/patch)` |  `PATCH /v1/{name=organizations/*/apis/*}`   
Updates an existing API proxy.  
  
## REST Resource: [v1.organizations.apis.debugsessions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.debugsessions)

Methods  
---  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.debugsessions/list)` |  `GET /v1/{parent=organizations/*/apis/*}/debugsessions`   
Lists debug sessions that are currently active in the given API Proxy.  
  
## REST Resource: [v1.organizations.apis.deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.deployments)

Methods  
---  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.deployments/list)` |  `GET /v1/{parent=organizations/*/apis/*}/deployments`   
Lists all deployments of an API proxy.  
  
## REST Resource: [v1.organizations.apis.keyvaluemaps](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps/create)` |  `POST /v1/{parent=organizations/*/apis/*}/keyvaluemaps`   
Creates a key value map in an API proxy.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps/delete)` |  `DELETE /v1/{name=organizations/*/apis/*/keyvaluemaps/*}`   
Deletes a key value map from an API proxy.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps/get)` |  `GET /v1/{name=organizations/*/apis/*/keyvaluemaps/*}`   
Get the key value map scoped to an organization, environment, or API proxy.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps/list)` |  `GET /v1/{parent=organizations/*/apis/*}/keyvaluemaps`   
Lists key value maps in an API proxy.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps/update)` |  `PUT /v1/{name=organizations/*/apis/*/keyvaluemaps/*}`   
Update the key value map scoped to an organization, environment, or API proxy.  
  
## REST Resource: [v1.organizations.apis.keyvaluemaps.entries](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/create)` |  `POST /v1/{parent=organizations/*/apis/*/keyvaluemaps/*}/entries`   
Creates key value entries in a key value map scoped to an organization, environment, or API proxy.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/delete)` |  `DELETE /v1/{name=organizations/*/apis/*/keyvaluemaps/*/entries/*}`   
Deletes a key value entry from a key value map scoped to an organization, environment, or API proxy.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/get)` |  `GET /v1/{name=organizations/*/apis/*/keyvaluemaps/*/entries/*}`   
Get the key value entry value for a key value map scoped to an organization, environment, or API proxy.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/list)` |  `GET /v1/{parent=organizations/*/apis/*/keyvaluemaps/*}/entries`   
Lists key value entries for key values maps scoped to an organization, environment, or API proxy.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/update)` |  `PUT /v1/{name=organizations/*/apis/*/keyvaluemaps/*/entries/*}`   
Update key value entry scoped to an organization, environment, or API proxy for an existing key.  
  
## REST Resource: [v1.organizations.apis.revisions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/delete)` |  `DELETE /v1/{name=organizations/*/apis/*/revisions/*}`   
Deletes an API proxy revision and all policies, resources, endpoints, and revisions associated with it.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/get)` |  `GET /v1/{name=organizations/*/apis/*/revisions/*}`   
Gets an API proxy revision.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/list)` |  `GET /v1/{parent=organizations/*/apis/*}/revisions`   
Lists all revisions for an API proxy.  
`[updateApiProxyRevision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/updateApiProxyRevision)` |  `POST /v1/{name=organizations/*/apis/*/revisions/*}`   
Updates an existing API proxy revision by uploading the API proxy configuration bundle as a zip file from your local machine.  
  
## REST Resource: [v1.organizations.apis.revisions.deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions.deployments)

Methods  
---  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions.deployments/list)` |  `GET /v1/{parent=organizations/*/apis/*/revisions/*}/deployments`   
Lists all deployments of an API proxy revision.  
  
## REST Resource: [v1.organizations.appgroups](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/create)` |  `POST /v1/{parent=organizations/*}/appgroups`   
Creates an AppGroup.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/delete)` |  `DELETE /v1/{name=organizations/*/appgroups/*}`   
Deletes an AppGroup.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/get)` |  `GET /v1/{name=organizations/*/appgroups/*}`   
Returns the AppGroup details for the provided AppGroup name in the request URI.  
`[getBalance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/getBalance)` |  `GET /v1/{name=organizations/*/appgroups/*/balance}`   
Gets the account balance for the AppGroup.  
`[getMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/getMonetizationConfig)` |  `GET /v1/{name=organizations/*/appgroups/*/monetizationConfig}`   
Gets the monetization configuration for the AppGroup.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/list)` |  `GET /v1/{parent=organizations/*}/appgroups`   
Lists all AppGroups in an organization.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/update)` |  `PUT /v1/{name=organizations/*/appgroups/*}`   
Updates an AppGroup.  
`[updateMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/updateMonetizationConfig)` |  `PUT /v1/{name=organizations/*/appgroups/*/monetizationConfig}`   
Updates the monetization configuration for the AppGroup.  
  
## REST Resource: [v1.organizations.appgroups.apps](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/create)` |  `POST /v1/{parent=organizations/*/appgroups/*}/apps`   
Creates an app and associates it with an AppGroup.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/delete)` |  `DELETE /v1/{name=organizations/*/appgroups/*/apps/*}`   
Deletes an AppGroup app.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/get)` |  `GET /v1/{name=organizations/*/appgroups/*/apps/*}`   
Returns the details for an AppGroup app.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/list)` |  `GET /v1/{parent=organizations/*/appgroups/*}/apps`   
Lists all apps created by an AppGroup in an Apigee organization.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/update)` |  `PUT /v1/{name=organizations/*/appgroups/*/apps/*}`   
Updates the details for an AppGroup app.  
  
## REST Resource: [v1.organizations.appgroups.apps.keys](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys/create)` |  `POST /v1/{parent=organizations/*/appgroups/*/apps/*}/keys`   
Creates a custom consumer key and secret for a AppGroup app.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys/delete)` |  `DELETE /v1/{name=organizations/*/appgroups/*/apps/*/keys/*}`   
Deletes an app's consumer key and removes all API products associated with the app.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys/get)` |  `GET /v1/{name=organizations/*/appgroups/*/apps/*/keys/*}`   
Gets details for a consumer key for a AppGroup app, including the key and secret value, associated API products, and other information.  
`[updateAppGroupAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys/updateAppGroupAppKey)` |  `POST /v1/{name=organizations/*/appgroups/*/apps/*/keys/*}`   
Adds an API product to an AppGroupAppKey, enabling the app that holds the key to access the API resources bundled in the API product.  
  
## REST Resource: [v1.organizations.appgroups.apps.keys.apiproducts](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys.apiproducts)

Methods  
---  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys.apiproducts/delete)` |  `DELETE /v1/{name=organizations/*/appgroups/*/apps/*/keys/*/apiproducts/*}`   
Removes an API product from an app's consumer key.  
`[updateAppGroupAppKeyApiProduct](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys.apiproducts/updateAppGroupAppKeyApiProduct)` |  `POST /v1/{name=organizations/*/appgroups/*/apps/*/keys/*/apiproducts/*}`   
Approves or revokes the consumer key for an API product.  
  
## REST Resource: [v1.organizations.appgroups.balance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.balance)

Methods  
---  
`[adjust](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.balance/adjust)` |  `POST /v1/{name=organizations/*/appgroups/*/balance}:adjust`   
Adjust the prepaid balance for the AppGroup.  
`[credit](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.balance/credit)` |  `POST /v1/{name=organizations/*/appgroups/*/balance}:credit`   
Credits the account balance for the AppGroup.  
  
## REST Resource: [v1.organizations.appgroups.subscriptions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions/create)` |  `POST /v1/{parent=organizations/*/appgroups/*}/subscriptions`   
Creates a subscription to an API product.  
`[expire](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions/expire)` |  `POST /v1/{name=organizations/*/appgroups/*/subscriptions/*}:expire`   
Expires an API product subscription immediately.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions/get)` |  `GET /v1/{name=organizations/*/appgroups/*/subscriptions/*}`   
Get an api product subscription for an appgroup.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions/list)` |  `GET /v1/{parent=organizations/*/appgroups/*}/subscriptions`   
List all api product subscriptions for an appgroup.  
  
## REST Resource: [v1.organizations.apps](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps)

Methods  
---  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps/get)` |  `GET /v1/{name=organizations/*/apps/*}`   
Gets the app profile for the specified app ID.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps/list)` |  `GET /v1/{parent=organizations/*}/apps`   
Lists IDs of apps within an organization that have the specified app status (approved or revoked) or are of the specified app type (developer or company).  
  
## REST Resource: [v1.organizations.datacollectors](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/create)` |  `POST /v1/{parent=organizations/*}/datacollectors`   
Creates a new data collector.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/delete)` |  `DELETE /v1/{name=organizations/*/datacollectors/*}`   
Deletes a data collector.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/get)` |  `GET /v1/{name=organizations/*/datacollectors/*}`   
Gets a data collector.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/list)` |  `GET /v1/{parent=organizations/*}/datacollectors`   
Lists all data collectors.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/patch)` |  `PATCH /v1/{name=organizations/*/datacollectors/*}`   
Updates a data collector.  
  
## REST Resource: [v1.organizations.deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.deployments)

Methods  
---  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.deployments/list)` |  `GET /v1/{parent=organizations/*}/deployments`   
Lists all deployments of API proxies or shared flows.  
  
## REST Resource: [v1.organizations.developers](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers)

Methods  
---  
`[attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/attributes)` |  `POST /v1/{parent=organizations/*/developers/*}/attributes`   
Updates developer attributes.  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/create)` |  `POST /v1/{parent=organizations/*}/developers`   
Creates a developer.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/delete)` |  `DELETE /v1/{name=organizations/*/developers/*}`   
Deletes a developer.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/get)` |  `GET /v1/{name=organizations/*/developers/*}`   
Returns the developer details, including the developer's name, email address, apps, and other information.  
`[getBalance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/getBalance)` |  `GET /v1/{name=organizations/*/developers/*/balance}`   
Gets the account balance for the developer.  
`[getMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/getMonetizationConfig)` |  `GET /v1/{name=organizations/*/developers/*/monetizationConfig}`   
Gets the monetization configuration for the developer.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/list)` |  `GET /v1/{parent=organizations/*}/developers`   
Lists all developers in an organization by email address.  
`[setDeveloperStatus](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/setDeveloperStatus)` |  `POST /v1/{name=organizations/*/developers/*}`   
Sets the status of a developer.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/update)` |  `PUT /v1/{name=organizations/*/developers/*}`   
Updates a developer.  
`[updateMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/updateMonetizationConfig)` |  `PUT /v1/{name=organizations/*/developers/*/monetizationConfig}`   
Updates the monetization configuration for the developer.  
  
## REST Resource: [v1.organizations.developers.apps](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps)

Methods  
---  
`[attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/attributes)` |  `POST /v1/{name=organizations/*/developers/*/apps/*}/attributes`   
Updates attributes for a developer app.  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/create)` |  `POST /v1/{parent=organizations/*/developers/*}/apps`   
Creates an app associated with a developer.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/delete)` |  `DELETE /v1/{name=organizations/*/developers/*/apps/*}`   
Deletes a developer app.  
`[generateKeyPairOrUpdateDeveloperAppStatus](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/generateKeyPairOrUpdateDeveloperAppStatus)` |  `POST /v1/{name=organizations/*/developers/*/apps/*}`   
Manages access to a developer app by enabling you to:

  * Approve or revoke a developer app
  * Generate a new consumer key and secret for a developer app

To approve or revoke a developer app, set the `action` query parameter to `approve` or `revoke`, respectively, and the `Content-Type` header to `application/octet-stream`.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/get)` |  `GET /v1/{name=organizations/*/developers/*/apps/*}`   
Returns the details for a developer app.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/list)` |  `GET /v1/{parent=organizations/*/developers/*}/apps`   
Lists all apps created by a developer in an Apigee organization.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/update)` |  `PUT /v1/{name=organizations/*/developers/*/apps/*}`   
Updates the details for a developer app.  
  
## REST Resource: [v1.organizations.developers.apps.attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/attributes)

Methods  
---  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.attributes/delete)` |  `DELETE /v1/{name=organizations/*/developers/*/apps/*/attributes/*}`   
Deletes a developer app attribute.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.attributes/get)` |  `GET /v1/{name=organizations/*/developers/*/apps/*/attributes/*}`   
Returns a developer app attribute.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.attributes/list)` |  `GET /v1/{parent=organizations/*/developers/*/apps/*}/attributes`   
Returns a list of all developer app attributes.  
`[updateDeveloperAppAttribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.attributes/updateDeveloperAppAttribute)` |  `POST /v1/{name=organizations/*/developers/*/apps/*/attributes/*}`   
Updates a developer app attribute.  
  
## REST Resource: [v1.organizations.developers.apps.keys](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/create)` |  `POST /v1/{parent=organizations/*/developers/*/apps/*}/keys`   
Creates a custom consumer key and secret for a developer app.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/delete)` |  `DELETE /v1/{name=organizations/*/developers/*/apps/*/keys/*}`   
Deletes an app's consumer key and removes all API products associated with the app.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/get)` |  `GET /v1/{name=organizations/*/developers/*/apps/*/keys/*}`   
Gets details for a consumer key for a developer app, including the key and secret value, associated API products, and other information.  
`[replaceDeveloperAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/replaceDeveloperAppKey)` |  `PUT /v1/{name=organizations/*/developers/*/apps/*/keys/*}`   
Updates the scope of an app.  
`[updateDeveloperAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/updateDeveloperAppKey)` |  `POST /v1/{name=organizations/*/developers/*/apps/*/keys/*}`   
Adds an API product to a developer app key, enabling the app that holds the key to access the API resources bundled in the API product.  
  
## REST Resource: [v1.organizations.developers.apps.keys.apiproducts](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys.apiproducts)

Methods  
---  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys.apiproducts/delete)` |  `DELETE /v1/{name=organizations/*/developers/*/apps/*/keys/*/apiproducts/*}`   
Removes an API product from an app's consumer key.  
`[updateDeveloperAppKeyApiProduct](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys.apiproducts/updateDeveloperAppKeyApiProduct)` |  `POST /v1/{name=organizations/*/developers/*/apps/*/keys/*/apiproducts/*}`   
Approves or revokes the consumer key for an API product.  
  
## REST Resource: [v1.organizations.developers.apps.keys.create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/create)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys.create/create)` |  `POST /v1/{parent=organizations/*/developers/*/apps/*}/keys/create`   
Creates a custom consumer key and secret for a developer app.  
  
## REST Resource: [v1.organizations.developers.attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/attributes)

Methods  
---  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.attributes/delete)` |  `DELETE /v1/{name=organizations/*/developers/*/attributes/*}`   
Deletes a developer attribute.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.attributes/get)` |  `GET /v1/{name=organizations/*/developers/*/attributes/*}`   
Returns the value of the specified developer attribute.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.attributes/list)` |  `GET /v1/{parent=organizations/*/developers/*}/attributes`   
Returns a list of all developer attributes.  
`[updateDeveloperAttribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.attributes/updateDeveloperAttribute)` |  `POST /v1/{name=organizations/*/developers/*/attributes/*}`   
Updates a developer attribute.  
  
## REST Resource: [v1.organizations.developers.balance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.balance)

Methods  
---  
`[adjust](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.balance/adjust)` |  `POST /v1/{name=organizations/*/developers/*/balance}:adjust`   
Adjust the prepaid balance for the developer.  
`[credit](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.balance/credit)` |  `POST /v1/{name=organizations/*/developers/*/balance}:credit`   
Credits the account balance for the developer.  
  
## REST Resource: [v1.organizations.developers.subscriptions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/create)` |  `POST /v1/{parent=organizations/*/developers/*}/subscriptions`   
Creates a subscription to an API product.  
`[expire](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/expire)` |  `POST /v1/{name=organizations/*/developers/*/subscriptions/*}:expire`   
Expires an API product subscription immediately.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/get)` |  `GET /v1/{name=organizations/*/developers/*/subscriptions/*}`   
Gets details for an API product subscription.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/list)` |  `GET /v1/{parent=organizations/*/developers/*}/subscriptions`   
Lists all API product subscriptions for a developer.  
  
## REST Resource: [v1.organizations.dnsZones](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones/create)` |  `POST /v1/{parent=organizations/*}/dnsZones`   
Creates a new DNS zone.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones/delete)` |  `DELETE /v1/{name=organizations/*/dnsZones/*}`   
Deletes a previously created DNS zone.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones/get)` |  `GET /v1/{name=organizations/*/dnsZones/*}`   
Fetches the representation of an existing DNS zone.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones/list)` |  `GET /v1/{parent=organizations/*}/dnsZones`   
Enumerates DNS zones that have been created but not yet deleted.  
  
## REST Resource: [v1.organizations.endpointAttachments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/create)` |  `POST /v1/{parent=organizations/*}/endpointAttachments`   
Creates an endpoint attachment.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/delete)` |  `DELETE /v1/{name=organizations/*/endpointAttachments/*}`   
Deletes an endpoint attachment.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/get)` |  `GET /v1/{name=organizations/*/endpointAttachments/*}`   
Gets the endpoint attachment.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/list)` |  `GET /v1/{parent=organizations/*}/endpointAttachments`   
Lists the endpoint attachments in an organization.  
  
## REST Resource: [v1.organizations.envgroups](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/create)` |  `POST /v1/{parent=organizations/*}/envgroups`   
Creates a new environment group.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/delete)` |  `DELETE /v1/{name=organizations/*/envgroups/*}`   
Deletes an environment group.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/get)` |  `GET /v1/{name=organizations/*/envgroups/*}`   
Gets an environment group.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/list)` |  `GET /v1/{parent=organizations/*}/envgroups`   
Lists all environment groups.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/patch)` |  `PATCH /v1/{name=organizations/*/envgroups/*}`   
Updates an environment group.  
  
## REST Resource: [v1.organizations.envgroups.attachments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments/create)` |  `POST /v1/{parent=organizations/*/envgroups/*}/attachments`   
Creates a new attachment of an environment to an environment group.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments/delete)` |  `DELETE /v1/{name=organizations/*/envgroups/*/attachments/*}`   
Deletes an environment group attachment.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments/get)` |  `GET /v1/{name=organizations/*/envgroups/*/attachments/*}`   
Gets an environment group attachment.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments/list)` |  `GET /v1/{parent=organizations/*/envgroups/*}/attachments`   
Lists all attachments of an environment group.  
  
## REST Resource: [v1.organizations.environments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/create)` |  `POST /v1/{parent=organizations/*}/environments`   
Creates an environment in an organization.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/delete)` |  `DELETE /v1/{name=organizations/*/environments/*}`   
Deletes an environment from an organization.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/get)` |  `GET /v1/{name=organizations/*/environments/*}`   
Gets environment details.  
`[getAddonsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getAddonsConfig)` |  `GET /v1/{name=organizations/*/environments/*/addonsConfig}`   
Gets the add-ons config of an environment.  
`[getApiSecurityRuntimeConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getApiSecurityRuntimeConfig)` |  `GET /v1/{name=organizations/*/environments/*/apiSecurityRuntimeConfig}`   
Gets the API Security runtime configuration for an environment.  
`[getDebugmask](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getDebugmask)` |  `GET /v1/{name=organizations/*/environments/*/debugmask}`   
Gets the debug mask singleton resource for an environment.  
`[getIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getIamPolicy)` |  `GET /v1/{resource=organizations/*/environments/*}:getIamPolicy`   
Gets the IAM policy on an environment.  
`[getSecurityActionsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getSecurityActionsConfig)` |  `GET /v1/{name=organizations/*/environments/*/securityActionsConfig}`   
GetSecurityActionConfig returns the current SecurityActions configuration.  
`[getTraceConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getTraceConfig)` |  `GET /v1/{name=organizations/*/environments/*/traceConfig}`   
Get distributed trace configuration in an environment.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/list)` |  `GET /v1/{parent=organizations/*}/environments`   
Lists all environments in an organization.  
`[modifyEnvironment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/modifyEnvironment)` |  `PATCH /v1/{name=organizations/*/environments/*}`   
Updates properties for an Apigee environment with patch semantics using a field mask.  
`[setIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/setIamPolicy)` |  `POST /v1/{resource=organizations/*/environments/*}:setIamPolicy`   
Sets the IAM policy on an environment, if the policy already exists it will be replaced.  
`[testIamPermissions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/testIamPermissions)` |  `POST /v1/{resource=organizations/*/environments/*}:testIamPermissions`   
Tests the permissions of a user on an environment, and returns a subset of permissions that the user has on the environment.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/update)` |  `PUT /v1/{name=organizations/*/environments/*}`   
Updates an existing environment.  
`[updateDebugmask](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/updateDebugmask)` |  `PATCH /v1/{debugMask.name=organizations/*/environments/*/debugmask}`   
Updates the debug mask singleton resource for an environment.  
`[updateEnvironment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/updateEnvironment)` |  `POST /v1/{name=organizations/*/environments/*}`   
Updates an existing environment.  
`[updateSecurityActionsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/updateSecurityActionsConfig)` |  `PATCH /v1/{securityActionsConfig.name=organizations/*/environments/*/securityActionsConfig}`   
UpdateSecurityActionConfig updates the current SecurityActions configuration.  
`[updateTraceConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/updateTraceConfig)` |  `PATCH /v1/{name=organizations/*/environments/*/traceConfig}`   
Updates the trace configurations in an environment.  
  
## REST Resource: [v1.organizations.environments.addonsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.addonsConfig)

Methods  
---  
`[setAddonEnablement](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.addonsConfig/setAddonEnablement)` |  `POST /v1/{name=organizations/*/environments/*/addonsConfig}:setAddonEnablement`   
Updates an add-on enablement status of an environment.  
  
## REST Resource: [v1.organizations.environments.analytics.admin](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin)

Methods  
---  
`[getSchemav2](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin/getSchemav2)` |  `GET /v1/{name=organizations/*/environments/*/analytics/admin/schemav2}`   
Gets a list of metrics and dimensions that can be used to create analytics queries and reports.  
  
## REST Resource: [v1.organizations.environments.analytics.exports](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.exports)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.exports/create)` |  `POST /v1/{parent=organizations/*/environments/*}/analytics/exports`   
Submit a data export job to be processed in the background.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.exports/get)` |  `GET /v1/{name=organizations/*/environments/*/analytics/exports/*}`   
Gets the details and status of an analytics export job.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.exports/list)` |  `GET /v1/{parent=organizations/*/environments/*}/analytics/exports`   
Lists the details and status of all analytics export jobs belonging to the parent organization and environment.  
  
## REST Resource: [v1.organizations.environments.apis.deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.deployments)

Methods  
---  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.deployments/list)` |  `GET /v1/{parent=organizations/*/environments/*/apis/*}/deployments`   
Lists all deployments of an API proxy in an environment.  
  
## REST Resource: [v1.organizations.environments.apis.revisions.debugsessions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/create)` |  `POST /v1/{parent=organizations/*/environments/*/apis/*/revisions/*}/debugsessions`   
Creates a debug session for a deployed API Proxy revision.  
`[deleteData](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/deleteData)` |  `DELETE /v1/{name=organizations/*/environments/*/apis/*/revisions/*/debugsessions/*}/data`   
Deletes the data from a debug session.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/get)` |  `GET /v1/{name=organizations/*/environments/*/apis/*/revisions/*/debugsessions/*}`   
Retrieves a debug session.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/list)` |  `GET /v1/{parent=organizations/*/environments/*/apis/*/revisions/*}/debugsessions`   
Lists debug sessions that are currently active in the given API Proxy revision.  
  
## REST Resource: [v1.organizations.environments.apis.revisions.debugsessions.data](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data)

Methods  
---  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data/get)` |  `GET /v1/{name=organizations/*/environments/*/apis/*/revisions/*/debugsessions/*/data/*}`   
Gets the debug data from a transaction.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data/list)` |  `GET /v1/{parent=organizations/*/environments/*/apis/*/revisions/*/debugsessions/*}/data`   
Lists the transaction IDs from a debug session.  
  
## REST Resource: [v1.organizations.environments.apis.revisions.deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments)

Methods  
---  
`[deploy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/deploy)` |  `POST /v1/{name=organizations/*/environments/*/apis/*/revisions/*}/deployments`   
Deploys a revision of an API proxy.  
`[generateDeployChangeReport](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/generateDeployChangeReport)` |  `POST /v1/{name=organizations/*/environments/*/apis/*/revisions/*}/deployments:generateDeployChangeReport`   
Generates a report for a dry run analysis of a DeployApiProxy request without committing the deployment.  
`[generateUndeployChangeReport](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/generateUndeployChangeReport)` |  `POST /v1/{name=organizations/*/environments/*/apis/*/revisions/*}/deployments:generateUndeployChangeReport`   
Generates a report for a dry run analysis of an UndeployApiProxy request without committing the undeploy.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/get)` |  `GET /v1/{name=organizations/*/environments/*/apis/*/revisions/*}/deployments`   
Gets the deployment of an API proxy revision and actual state reported by runtime pods.  
`[undeploy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/undeploy)` |  `DELETE /v1/{name=organizations/*/environments/*/apis/*/revisions/*}/deployments`   
Undeploys an API proxy revision from an environment.  
  
## REST Resource: [v1.organizations.environments.archiveDeployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/create)` |  `POST /v1/{parent=organizations/*/environments/*}/archiveDeployments`   
Creates a new ArchiveDeployment.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/delete)` |  `DELETE /v1/{name=organizations/*/environments/*/archiveDeployments/*}`   
Deletes an archive deployment.  
`[generateDownloadUrl](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/generateDownloadUrl)` |  `POST /v1/{name=organizations/*/environments/*/archiveDeployments/*}:generateDownloadUrl`   
Generates a signed URL for downloading the original zip file used to create an Archive Deployment.  
`[generateUploadUrl](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/generateUploadUrl)` |  `POST /v1/{parent=organizations/*/environments/*}/archiveDeployments:generateUploadUrl`   
Generates a signed URL for uploading an Archive zip file to Google Cloud Storage.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/get)` |  `GET /v1/{name=organizations/*/environments/*/archiveDeployments/*}`   
Gets the specified ArchiveDeployment.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/list)` |  `GET /v1/{parent=organizations/*/environments/*}/archiveDeployments`   
Lists the ArchiveDeployments in the specified Environment.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/patch)` |  `PATCH /v1/{archiveDeployment.name=organizations/*/environments/*/archiveDeployments/*}`   
Updates an existing ArchiveDeployment.  
  
## REST Resource: [v1.organizations.environments.caches](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.caches)

Methods  
---  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.caches/delete)` |  `DELETE /v1/{name=organizations/*/environments/*/caches/*}`   
Deletes a cache.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.caches/list)` |  `GET /v1/{parent=organizations/*/environments/*}/caches`   
Lists all caches in an environment.  
  
## REST Resource: [v1.organizations.environments.deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments)

Methods  
---  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/get)` |  `GET /v1/{name=organizations/*/environments/*/deployments/*}`   
Gets a particular deployment of Api proxy or a shared flow in an environment  
`[getIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/getIamPolicy)` |  `GET /v1/{resource=organizations/*/environments/*/deployments/*}:getIamPolicy`   
Gets the IAM policy on a deployment.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/list)` |  `GET /v1/{parent=organizations/*/environments/*}/deployments`   
Lists all deployments of API proxies or shared flows in an environment.  
`[setIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/setIamPolicy)` |  `POST /v1/{resource=organizations/*/environments/*/deployments/*}:setIamPolicy`   
Sets the IAM policy on a deployment, if the policy already exists it will be replaced.  
`[testIamPermissions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.deployments/testIamPermissions)` |  `POST /v1/{resource=organizations/*/environments/*/deployments/*}:testIamPermissions`   
Tests the permissions of a user on a deployment, and returns a subset of permissions that the user has on the deployment.  
  
## REST Resource: [v1.organizations.environments.flowhooks](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks)

Methods  
---  
`[attachSharedFlowToFlowHook](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks/attachSharedFlowToFlowHook)` |  `PUT /v1/{name=organizations/*/environments/*/flowhooks/*}`   
Attaches a shared flow to a flow hook.  
`[detachSharedFlowFromFlowHook](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks/detachSharedFlowFromFlowHook)` |  `DELETE /v1/{name=organizations/*/environments/*/flowhooks/*}`   
Detaches a shared flow from a flow hook.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks/get)` |  `GET /v1/{name=organizations/*/environments/*/flowhooks/*}`   
Returns the name of the shared flow attached to the specified flow hook.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks/list)` |  `GET /v1/{parent=organizations/*/environments/*}/flowhooks`   
Lists the flow hooks attached to an environment.  
  
## REST Resource: [v1.organizations.environments.keystores](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores/create)` |  `POST /v1/{parent=organizations/*/environments/*}/keystores`   
Creates a keystore or truststore.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores/delete)` |  `DELETE /v1/{name=organizations/*/environments/*/keystores/*}`   
Deletes a keystore or truststore.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores/get)` |  `GET /v1/{name=organizations/*/environments/*/keystores/*}`   
Gets a keystore or truststore.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores/list)` |  `GET /v1/{parent=organizations/*/environments/*}/keystores`   
Lists all keystores and truststores.  
  
## REST Resource: [v1.organizations.environments.keystores.aliases](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases/create)` |  `POST /v1/{parent=organizations/*/environments/*/keystores/*}/aliases`   
Creates an alias from a key/certificate pair.  
`[csr](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases/csr)` |  `GET /v1/{name=organizations/*/environments/*/keystores/*/aliases/*}/csr`   
Generates a PKCS #10 Certificate Signing Request for the private key in an alias.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases/delete)` |  `DELETE /v1/{name=organizations/*/environments/*/keystores/*/aliases/*}`   
Deletes an alias.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases/get)` |  `GET /v1/{name=organizations/*/environments/*/keystores/*/aliases/*}`   
Gets an alias.  
`[getCertificate](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases/getCertificate)` |  `GET /v1/{name=organizations/*/environments/*/keystores/*/aliases/*}/certificate`   
Gets the certificate from an alias in PEM-encoded form.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases/list)` |  `GET /v1/{parent=organizations/*/environments/*/keystores/*}/aliases`   
Lists all aliases.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases/update)` |  `PUT /v1/{name=organizations/*/environments/*/keystores/*/aliases/*}`   
Updates the certificate in an alias.  
  
## REST Resource: [v1.organizations.environments.keyvaluemaps](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps/create)` |  `POST /v1/{parent=organizations/*/environments/*}/keyvaluemaps`   
Creates a key value map in an environment.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps/delete)` |  `DELETE /v1/{name=organizations/*/environments/*/keyvaluemaps/*}`   
Deletes a key value map from an environment.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps/get)` |  `GET /v1/{name=organizations/*/environments/*/keyvaluemaps/*}`   
Get the key value map scoped to an organization, environment, or API proxy.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps/list)` |  `GET /v1/{parent=organizations/*/environments/*}/keyvaluemaps`   
Lists key value maps in an environment.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps/update)` |  `PUT /v1/{name=organizations/*/environments/*/keyvaluemaps/*}`   
Update the key value map scoped to an organization, environment, or API proxy.  
  
## REST Resource: [v1.organizations.environments.keyvaluemaps.entries](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps.entries)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps.entries/create)` |  `POST /v1/{parent=organizations/*/environments/*/keyvaluemaps/*}/entries`   
Creates key value entries in a key value map scoped to an organization, environment, or API proxy.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps.entries/delete)` |  `DELETE /v1/{name=organizations/*/environments/*/keyvaluemaps/*/entries/*}`   
Deletes a key value entry from a key value map scoped to an organization, environment, or API proxy.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps.entries/get)` |  `GET /v1/{name=organizations/*/environments/*/keyvaluemaps/*/entries/*}`   
Get the key value entry value for a key value map scoped to an organization, environment, or API proxy.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps.entries/list)` |  `GET /v1/{parent=organizations/*/environments/*/keyvaluemaps/*}/entries`   
Lists key value entries for key values maps scoped to an organization, environment, or API proxy.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps.entries/update)` |  `PUT /v1/{name=organizations/*/environments/*/keyvaluemaps/*/entries/*}`   
Update key value entry scoped to an organization, environment, or API proxy for an existing key.  
  
## REST Resource: [v1.organizations.environments.optimizedStats](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.optimizedStats)

Methods  
---  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.optimizedStats/get)` |  `GET /v1/{name=organizations/*/environments/*/optimizedStats/**}`   
Similar to `[GetStats](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.stats/get#google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetStats)` except that the response is less verbose.  
  
## REST Resource: [v1.organizations.environments.queries](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.queries)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.queries/create)` |  `POST /v1/{parent=organizations/*/environments/*}/queries`   
Submit a query to be processed in the background.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.queries/get)` |  `GET /v1/{name=organizations/*/environments/*/queries/*}`   
Get query status If the query is still in progress, the `state` is set to "running" After the query has completed successfully, `state` is set to "completed"  
`[getResult](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.queries/getResult)` |  `GET /v1/{name=organizations/*/environments/*/queries/*/result}`   
After the query is completed, use this API to retrieve the results.  
`[getResulturl](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.queries/getResulturl)` |  `GET /v1/{name=organizations/*/environments/*/queries/*/resulturl}`   
After the query is completed, use this API to retrieve the results.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.queries/list)` |  `GET /v1/{parent=organizations/*/environments/*}/queries`   
Return a list of Asynchronous Queries  
  
## REST Resource: [v1.organizations.environments.references](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.references)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.references/create)` |  `POST /v1/{parent=organizations/*/environments/*}/references`   
Creates a Reference in the specified environment.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.references/delete)` |  `DELETE /v1/{name=organizations/*/environments/*/references/*}`   
Deletes a Reference from an environment.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.references/get)` |  `GET /v1/{name=organizations/*/environments/*/references/*}`   
Gets a Reference resource.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.references/list)` |  `GET /v1/{parent=organizations/*/environments/*}/references`   
Lists all References in an environment as a JSON array.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.references/update)` |  `PUT /v1/{name=organizations/*/environments/*/references/*}`   
Updates an existing Reference.  
  
## REST Resource: [v1.organizations.environments.resourcefiles](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/create)` |  `POST /v1/{parent=organizations/*/environments/*}/resourcefiles`   
Creates a resource file.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/delete)` |  `DELETE /v1/{parent=organizations/*/environments/*}/resourcefiles/{type}/{name}`   
Deletes a resource file.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/get)` |  `GET /v1/{parent=organizations/*/environments/*}/resourcefiles/{type}/{name}`   
Gets the contents of a resource file.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/list)` |  `GET /v1/{parent=organizations/*/environments/*}/resourcefiles`   
Lists all resource files, optionally filtering by type.  
`[listEnvironmentResources](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/listEnvironmentResources)` |  `GET /v1/{parent=organizations/*/environments/*}/resourcefiles/{type}`   
Lists all resource files, optionally filtering by type.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles/update)` |  `PUT /v1/{parent=organizations/*/environments/*}/resourcefiles/{type}/{name}`   
Updates a resource file.  
  
## REST Resource: [v1.organizations.environments.securityActions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions/create)` |  `POST /v1/{parent=organizations/*/environments/*}/securityActions`   
CreateSecurityAction creates a SecurityAction.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions/delete)` |  `DELETE /v1/{name=organizations/*/environments/*/securityActions/*}`   
Delete a SecurityAction.  
`[disable](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions/disable)` |  `POST /v1/{name=organizations/*/environments/*/securityActions/*}:disable`   
Disable a SecurityAction.  
`[enable](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions/enable)` |  `POST /v1/{name=organizations/*/environments/*/securityActions/*}:enable`   
Enable a SecurityAction.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions/get)` |  `GET /v1/{name=organizations/*/environments/*/securityActions/*}`   
Get a SecurityAction by name.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions/list)` |  `GET /v1/{parent=organizations/*/environments/*}/securityActions`   
Returns a list of SecurityActions.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions/patch)` |  `PATCH /v1/{securityAction.name=organizations/*/environments/*/securityActions/*}`   
Update a SecurityAction.  
  
## REST Resource: [v1.organizations.environments.securityIncidents](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents)

Methods  
---  
`[batchUpdate](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents/batchUpdate)` |  `POST /v1/{parent=organizations/*/environments/*}/securityIncidents:batchUpdate`   
BatchUpdateSecurityIncident updates multiple existing security incidents.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents/get)` |  `GET /v1/{name=organizations/*/environments/*/securityIncidents/*}`   
GetSecurityIncident gets the specified security incident.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents/list)` |  `GET /v1/{parent=organizations/*/environments/*}/securityIncidents`   
ListSecurityIncidents lists all the security incident associated with the environment.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityIncidents/patch)` |  `PATCH /v1/{securityIncident.name=organizations/*/environments/*/securityIncidents/*}`   
UpdateSecurityIncidents updates an existing security incident.  
  
## REST Resource: [v1.organizations.environments.securityReports](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityReports)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityReports/create)` |  `POST /v1/{parent=organizations/*/environments/*}/securityReports`   
Submit a report request to be processed in the background.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityReports/get)` |  `GET /v1/{name=organizations/*/environments/*/securityReports/*}`   
Get security report status If the query is still in progress, the `state` is set to "running" After the query has completed successfully, `state` is set to "completed"  
`[getResult](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityReports/getResult)` |  `GET /v1/{name=organizations/*/environments/*/securityReports/*/result}`   
After the query is completed, use this API to retrieve the results as file.  
`[getResultView](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityReports/getResultView)` |  `GET /v1/{name=organizations/*/environments/*/securityReports/*/resultView}`   
After the query is completed, use this API to view the query result when result size is small.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityReports/list)` |  `GET /v1/{parent=organizations/*/environments/*}/securityReports`   
Return a list of Security Reports  
  
## REST Resource: [v1.organizations.environments.securityStats](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats)

Methods  
---  
`[queryTabularStats](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats/queryTabularStats)` |  `POST /v1/{orgenv=organizations/*/environments/*}/securityStats:queryTabularStats`   
Retrieve security statistics as tabular rows.  
`[queryTimeSeriesStats](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats/queryTimeSeriesStats)` |  `POST /v1/{orgenv=organizations/*/environments/*}/securityStats:queryTimeSeriesStats`   
Retrieve security statistics as a collection of time series.  
  
## REST Resource: [v1.organizations.environments.sharedflows.deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.deployments)

Methods  
---  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.deployments/list)` |  `GET /v1/{parent=organizations/*/environments/*/sharedflows/*}/deployments`   
Lists all deployments of a shared flow in an environment.  
  
## REST Resource: [v1.organizations.environments.sharedflows.revisions.deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.revisions.deployments)

Methods  
---  
`[deploy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.revisions.deployments/deploy)` |  `POST /v1/{name=organizations/*/environments/*/sharedflows/*/revisions/*}/deployments`   
Deploys a revision of a shared flow.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.revisions.deployments/get)` |  `GET /v1/{name=organizations/*/environments/*/sharedflows/*/revisions/*}/deployments`   
Gets the deployment of a shared flow revision and actual state reported by runtime pods.  
`[undeploy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.revisions.deployments/undeploy)` |  `DELETE /v1/{name=organizations/*/environments/*/sharedflows/*/revisions/*}/deployments`   
Undeploys a shared flow revision from an environment.  
  
## REST Resource: [v1.organizations.environments.stats](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.stats)

Methods  
---  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.stats/get)` |  `GET /v1/{name=organizations/*/environments/*/stats/**}`   
Retrieve metrics grouped by dimensions.  
  
## REST Resource: [v1.organizations.environments.targetservers](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers/create)` |  `POST /v1/{parent=organizations/*/environments/*}/targetservers`   
Creates a `[TargetServer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers#TargetServer)` in the specified environment.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers/delete)` |  `DELETE /v1/{name=organizations/*/environments/*/targetservers/*}`   
Deletes a `[TargetServer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers#TargetServer)` from an environment.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers/get)` |  `GET /v1/{name=organizations/*/environments/*/targetservers/*}`   
Gets a TargetServer resource.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers/list)` |  `GET /v1/{parent=organizations/*/environments/*}/targetservers`   
Lists all TargetServers in an environment as a JSON array.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers/update)` |  `PUT /v1/{name=organizations/*/environments/*/targetservers/*}`   
Updates an existing TargetServer.  
  
## REST Resource: [v1.organizations.environments.traceConfig.overrides](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.traceConfig.overrides)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.traceConfig.overrides/create)` |  `POST /v1/{parent=organizations/*/environments/*/traceConfig}/overrides`   
Creates a trace configuration override.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.traceConfig.overrides/delete)` |  `DELETE /v1/{name=organizations/*/environments/*/traceConfig/overrides/*}`   
Deletes a distributed trace configuration override.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.traceConfig.overrides/get)` |  `GET /v1/{name=organizations/*/environments/*/traceConfig/overrides/*}`   
Gets a trace configuration override.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.traceConfig.overrides/list)` |  `GET /v1/{parent=organizations/*/environments/*/traceConfig}/overrides`   
Lists all of the distributed trace configuration overrides in an environment.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.traceConfig.overrides/patch)` |  `PATCH /v1/{name=organizations/*/environments/*/traceConfig/overrides/*}`   
Updates a distributed trace configuration override.  
  
## REST Resource: [v1.organizations.hostQueries](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostQueries)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostQueries/create)` |  `POST /v1/{parent=organizations/*}/hostQueries`   
Submit a query at host level to be processed in the background.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostQueries/get)` |  `GET /v1/{name=organizations/*/hostQueries/*}`   
Get status of a query submitted at host level.  
`[getResult](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostQueries/getResult)` |  `GET /v1/{name=organizations/*/hostQueries/*/result}`   
After the query is completed, use this API to retrieve the results.  
`[getResultView](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostQueries/getResultView)` |  `GET /v1/{name=organizations/*/hostQueries/*/resultView}`   
  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostQueries/list)` |  `GET /v1/{parent=organizations/*}/hostQueries`   
Return a list of Asynchronous Queries at host level.  
  
## REST Resource: [v1.organizations.hostSecurityReports](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostSecurityReports)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostSecurityReports/create)` |  `POST /v1/{parent=organizations/*}/hostSecurityReports`   
Submit a query at host level to be processed in the background.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostSecurityReports/get)` |  `GET /v1/{name=organizations/*/hostSecurityReports/*}`   
Get status of a query submitted at host level.  
`[getResult](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostSecurityReports/getResult)` |  `GET /v1/{name=organizations/*/hostSecurityReports/*/result}`   
After the query is completed, use this API to retrieve the results.  
`[getResultView](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostSecurityReports/getResultView)` |  `GET /v1/{name=organizations/*/hostSecurityReports/*/resultView}`   
After the query is completed, use this API to view the query result when result size is small.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostSecurityReports/list)` |  `GET /v1/{parent=organizations/*}/hostSecurityReports`   
Return a list of Security Reports at host level.  
  
## REST Resource: [v1.organizations.hostStats](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostStats)

Methods  
---  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostStats/get)` |  `GET /v1/{name=organizations/*/hostStats/**}`   
Retrieve metrics grouped by dimensions in host level.  
  
## REST Resource: [v1.organizations.instances](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/create)` |  `POST /v1/{parent=organizations/*}/instances`   
Creates an Apigee runtime instance.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/delete)` |  `DELETE /v1/{name=organizations/*/instances/*}`   
Deletes an Apigee runtime instance.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/get)` |  `GET /v1/{name=organizations/*/instances/*}`   
Gets the details for an Apigee runtime instance.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/list)` |  `GET /v1/{parent=organizations/*}/instances`   
Lists all Apigee runtime instances for the organization.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/patch)` |  `PATCH /v1/{name=organizations/*/instances/*}`   
Updates an Apigee runtime instance.  
  
## REST Resource: [v1.organizations.instances.attachments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments/create)` |  `POST /v1/{parent=organizations/*/instances/*}/attachments`   
Creates a new attachment of an environment to an instance.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments/delete)` |  `DELETE /v1/{name=organizations/*/instances/*/attachments/*}`   
Deletes an attachment.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments/get)` |  `GET /v1/{name=organizations/*/instances/*/attachments/*}`   
Gets an attachment.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments/list)` |  `GET /v1/{parent=organizations/*/instances/*}/attachments`   
Lists all attachments to an instance.  
  
## REST Resource: [v1.organizations.instances.natAddresses](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.natAddresses)

Methods  
---  
`[activate](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.natAddresses/activate)` |  `POST /v1/{name=organizations/*/instances/*/natAddresses/*}:activate`   
Activates the NAT address.  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.natAddresses/create)` |  `POST /v1/{parent=organizations/*/instances/*}/natAddresses`   
Creates a NAT address.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.natAddresses/delete)` |  `DELETE /v1/{name=organizations/*/instances/*/natAddresses/*}`   
Deletes the NAT address.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.natAddresses/get)` |  `GET /v1/{name=organizations/*/instances/*/natAddresses/*}`   
Gets the details of a NAT address.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.natAddresses/list)` |  `GET /v1/{parent=organizations/*/instances/*}/natAddresses`   
Lists the NAT addresses for an Apigee instance.  
  
## REST Resource: [v1.organizations.keyvaluemaps](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps/create)` |  `POST /v1/{parent=organizations/*}/keyvaluemaps`   
Creates a key value map in an organization.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps/delete)` |  `DELETE /v1/{name=organizations/*/keyvaluemaps/*}`   
Deletes a key value map from an organization.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps/get)` |  `GET /v1/{name=organizations/*/keyvaluemaps/*}`   
Get the key value map scoped to an organization, environment, or API proxy.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps/list)` |  `GET /v1/{parent=organizations/*}/keyvaluemaps`   
Lists key value maps in an organization.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps/update)` |  `PUT /v1/{name=organizations/*/keyvaluemaps/*}`   
Update the key value map scoped to an organization, environment, or API proxy.  
  
## REST Resource: [v1.organizations.keyvaluemaps.entries](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps.entries)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps.entries/create)` |  `POST /v1/{parent=organizations/*/keyvaluemaps/*}/entries`   
Creates key value entries in a key value map scoped to an organization, environment, or API proxy.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps.entries/delete)` |  `DELETE /v1/{name=organizations/*/keyvaluemaps/*/entries/*}`   
Deletes a key value entry from a key value map scoped to an organization, environment, or API proxy.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps.entries/get)` |  `GET /v1/{name=organizations/*/keyvaluemaps/*/entries/*}`   
Get the key value entry value for a key value map scoped to an organization, environment, or API proxy.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps.entries/list)` |  `GET /v1/{parent=organizations/*/keyvaluemaps/*}/entries`   
Lists key value entries for key values maps scoped to an organization, environment, or API proxy.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps.entries/update)` |  `PUT /v1/{name=organizations/*/keyvaluemaps/*/entries/*}`   
Update key value entry scoped to an organization, environment, or API proxy for an existing key.  
  
## REST Resource: [v1.organizations.operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.operations/get)` |  `GET /v1/{name=organizations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.operations/list)` |  `GET /v1/{name=organizations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.organizations.optimizedHostStats](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.optimizedHostStats)

Methods  
---  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.optimizedHostStats/get)` |  `GET /v1/{name=organizations/*/optimizedHostStats/**}`   
Similar to `[GetHostStats](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.hostStats/get#google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetHostStats)` except that the response is less verbose.  
  
## REST Resource: [v1.organizations.reports](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.reports)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.reports/create)` |  `POST /v1/{parent=organizations/*}/reports`   
Creates a Custom Report for an Organization.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.reports/delete)` |  `DELETE /v1/{name=organizations/*/reports/*}`   
Deletes an existing custom report definition  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.reports/get)` |  `GET /v1/{name=organizations/*/reports/*}`   
Retrieve a custom report definition.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.reports/list)` |  `GET /v1/{parent=organizations/*}/reports`   
Return a list of Custom Reports  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.reports/update)` |  `PUT /v1/{name=organizations/*/reports/*}`   
Update an existing custom report definition  
  
## REST Resource: [v1.organizations.securityAssessmentResults](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityAssessmentResults)

Methods  
---  
`[batchCompute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityAssessmentResults/batchCompute)` |  `POST /v1/{name=organizations/*/securityAssessmentResults}:batchCompute`   
Compute RAV2 security scores for a set of resources.  
  
## REST Resource: [v1.organizations.securityFeedback](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityFeedback)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityFeedback/create)` |  `POST /v1/{parent=organizations/*}/securityFeedback`   
Creates a new report containing customer feedback.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityFeedback/delete)` |  `DELETE /v1/{name=organizations/*/securityFeedback/*}`   
Deletes a specific feedback report.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityFeedback/get)` |  `GET /v1/{name=organizations/*/securityFeedback/*}`   
Gets a specific customer feedback report.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityFeedback/list)` |  `GET /v1/{parent=organizations/*}/securityFeedback`   
Lists all feedback reports which have already been submitted.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityFeedback/patch)` |  `PATCH /v1/{securityFeedback.name=organizations/*/securityFeedback/*}`   
Updates a specific feedback report.  
  
## REST Resource: [v1.organizations.securityMonitoringConditions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityMonitoringConditions)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityMonitoringConditions/create)` |  `POST /v1/{parent=organizations/*}/securityMonitoringConditions`   
Create a security monitoring condition.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityMonitoringConditions/delete)` |  `DELETE /v1/{name=organizations/*/securityMonitoringConditions/*}`   
Delete a security monitoring condition.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityMonitoringConditions/get)` |  `GET /v1/{name=organizations/*/securityMonitoringConditions/*}`   
Get a security monitoring condition.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityMonitoringConditions/list)` |  `GET /v1/{parent=organizations/*}/securityMonitoringConditions`   
List security monitoring conditions.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityMonitoringConditions/patch)` |  `PATCH /v1/{securityMonitoringCondition.name=organizations/*/securityMonitoringConditions/*}`   
Update a security monitoring condition.  
  
## REST Resource: [v1.organizations.securityProfiles](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles/create)` |  `POST /v1/{parent=organizations/*}/securityProfiles`   
CreateSecurityProfile create a new custom security profile.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles/delete)` |  `DELETE /v1/{name=organizations/*/securityProfiles/*}`   
DeleteSecurityProfile delete a profile with all its revisions.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles/get)` |  `GET /v1/{name=organizations/*/securityProfiles/*}`   
GetSecurityProfile gets the specified security profile.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles/list)` |  `GET /v1/{parent=organizations/*}/securityProfiles`   
ListSecurityProfiles lists all the security profiles associated with the org including attached and unattached profiles.  
`[listRevisions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles/listRevisions)` |  `GET /v1/{name=organizations/*/securityProfiles/*}:listRevisions`   
ListSecurityProfileRevisions lists all the revisions of the security profile.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles/patch)` |  `PATCH /v1/{securityProfile.name=organizations/*/securityProfiles/*}`   
UpdateSecurityProfile update the metadata of security profile.  
  
## REST Resource: [v1.organizations.securityProfiles.environments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles.environments)

Methods  
---  
`[computeEnvironmentScores](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles.environments/computeEnvironmentScores)` |  `POST /v1/{profileEnvironment=organizations/*/securityProfiles/*/environments/*}:computeEnvironmentScores`   
ComputeEnvironmentScores calculates scores for requested time range for the specified security profile and environment.  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles.environments/create)` |  `POST /v1/{parent=organizations/*/securityProfiles/*}/environments`   
CreateSecurityProfileEnvironmentAssociation creates profile environment association i.e.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfiles.environments/delete)` |  `DELETE /v1/{name=organizations/*/securityProfiles/*/environments/*}`   
DeleteSecurityProfileEnvironmentAssociation removes profile environment association i.e.  
  
## REST Resource: [v1.organizations.securityProfilesV2](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2/create)` |  `POST /v1/{parent=organizations/*}/securityProfilesV2`   
Create a security profile v2.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2/delete)` |  `DELETE /v1/{name=organizations/*/securityProfilesV2/*}`   
Delete a security profile v2.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2/get)` |  `GET /v1/{name=organizations/*/securityProfilesV2/*}`   
Get a security profile v2.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2/list)` |  `GET /v1/{parent=organizations/*}/securityProfilesV2`   
List security profiles v2.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2/patch)` |  `PATCH /v1/{securityProfileV2.name=organizations/*/securityProfilesV2/*}`   
Update a security profile V2.  
  
## REST Resource: [v1.organizations.sharedflows](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows/create)` |  `POST /v1/{parent=organizations/*}/sharedflows`   
Uploads a ZIP-formatted shared flow configuration bundle to an organization.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows/delete)` |  `DELETE /v1/{name=organizations/*/sharedflows/*}`   
Deletes a shared flow and all it's revisions.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows/get)` |  `GET /v1/{name=organizations/*/sharedflows/*}`   
Gets a shared flow by name, including a list of its revisions.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows/list)` |  `GET /v1/{parent=organizations/*}/sharedflows`   
Lists all shared flows in the organization.  
`[move](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows/move)` |  `POST /v1/{name=organizations/*/sharedflows/*}:move`   
Moves an shared flow to a different space.  
  
## REST Resource: [v1.organizations.sharedflows.deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.deployments)

Methods  
---  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.deployments/list)` |  `GET /v1/{parent=organizations/*/sharedflows/*}/deployments`   
Lists all deployments of a shared flow.  
  
## REST Resource: [v1.organizations.sharedflows.revisions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.revisions/delete)` |  `DELETE /v1/{name=organizations/*/sharedflows/*/revisions/*}`   
Deletes a shared flow and all associated policies, resources, and revisions.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.revisions/get)` |  `GET /v1/{name=organizations/*/sharedflows/*/revisions/*}`   
Gets a revision of a shared flow.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.revisions/list)` |  `GET /v1/{parent=organizations/*/sharedflows/*}/revisions`   
Lists all revisions for a shared flow.  
`[updateSharedFlowRevision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.revisions/updateSharedFlowRevision)` |  `POST /v1/{name=organizations/*/sharedflows/*/revisions/*}`   
Updates a shared flow revision.  
  
## REST Resource: [v1.organizations.sharedflows.revisions.deployments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.revisions.deployments)

Methods  
---  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.revisions.deployments/list)` |  `GET /v1/{parent=organizations/*/sharedflows/*/revisions/*}/deployments`   
Lists all deployments of a shared flow revision.  
  
## REST Resource: [v1.organizations.sites.apicategories](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apicategories)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apicategories/create)` |  `POST /v1/{parent=organizations/*/sites/*}/apicategories`   
Creates a new API category.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apicategories/delete)` |  `DELETE /v1/{name=organizations/*/sites/*/apicategories/*}`   
Deletes an API category.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apicategories/get)` |  `GET /v1/{name=organizations/*/sites/*/apicategories/*}`   
Gets an API category.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apicategories/list)` |  `GET /v1/{parent=organizations/*/sites/*}/apicategories`   
Returns the API categories associated with a portal.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apicategories/patch)` |  `PATCH /v1/{name=organizations/*/sites/*/apicategories/*}`   
Updates an API category.  
  
## REST Resource: [v1.organizations.sites.apidocs](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs/create)` |  `POST /v1/{parent=organizations/*/sites/*}/apidocs`   
Creates a new catalog item.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs/delete)` |  `DELETE /v1/{name=organizations/*/sites/*/apidocs/*}`   
Deletes a catalog item.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs/get)` |  `GET /v1/{name=organizations/*/sites/*/apidocs/*}`   
Gets a catalog item.  
`[getDocumentation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs/getDocumentation)` |  `GET /v1/{name=organizations/*/sites/*/apidocs/*/documentation}`   
Gets the documentation for the specified catalog item.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs/list)` |  `GET /v1/{parent=organizations/*/sites/*}/apidocs`   
Returns the catalog items associated with a portal.  
`[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs/update)` |  `PUT /v1/{name=organizations/*/sites/*/apidocs/*}`   
Updates a catalog item.  
`[updateDocumentation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs/updateDocumentation)` |  `PATCH /v1/{name=organizations/*/sites/*/apidocs/*/documentation}`   
Updates the documentation for the specified catalog item.  
  
## REST Resource: [v1.organizations.spaces](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces/create)` |  `POST /v1/{parent=organizations/*}/spaces`   
Create a space under an organization.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces/delete)` |  `DELETE /v1/{name=organizations/*/spaces/*}`   
Deletes an organization space.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces/get)` |  `GET /v1/{name=organizations/*/spaces/*}`   
Get a space under an Organization.  
`[getIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces/getIamPolicy)` |  `GET /v1/{resource=organizations/*/spaces/*}:getIamPolicy`   
Callers must have apigee.spaces.getIamPolicy.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces/list)` |  `GET /v1/{parent=organizations/*}/spaces`   
Lists spaces under an organization.  
`[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces/patch)` |  `PATCH /v1/{name=organizations/*/spaces/*}`   
Updates a space.  
`[setIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces/setIamPolicy)` |  `POST /v1/{resource=organizations/*/spaces/*}:setIamPolicy`   
IAM META APIs Callers must have apigee.spaces.setIamPolicy.  
`[testIamPermissions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.spaces/testIamPermissions)` |  `POST /v1/{resource=organizations/*/spaces/*}:testIamPermissions`   
Callers don't need any permissions.  
  
## REST Resource: [v1.projects](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/projects)

Methods  
---  
`[provisionOrganization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/projects/provisionOrganization)` |  `POST /v1/{project=projects/*}:provisionOrganization`   
Provisions a new Apigee organization with a functioning runtime.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
