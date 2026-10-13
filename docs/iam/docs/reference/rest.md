---
url: https://docs.cloud.google.com/iam/docs/reference/rest/
title: Identity and Access Management (IAM) API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:21.673409+00:00
---

# Identity and Access Management (IAM) API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Identity and Access Management (IAM) API Stay organized with collections  Save and categorize content based on your preferences. 

Manages identity and access control for Google Cloud resources, including the creation of service accounts, which you can use to authenticate to Google and make API calls. Enabling this API also enables the IAM Service Account Credentials API (iamcredentials.googleapis.com). However, disabling this API doesn't disable the IAM Service Account Credentials API.

  * REST Resource: v3beta.folders.locations.accessPolicies
  * REST Resource: v3beta.folders.locations.operations
  * REST Resource: v3beta.folders.locations.policyBindings
  * REST Resource: v3beta.organizations.locations.accessPolicies
  * REST Resource: v3beta.organizations.locations.operations
  * REST Resource: v3beta.organizations.locations.policyBindings
  * REST Resource: v3beta.organizations.locations.principalAccessBoundaryPolicies
  * REST Resource: v3beta.projects.locations.accessPolicies
  * REST Resource: v3beta.projects.locations.operations
  * REST Resource: v3beta.projects.locations.policyBindings
  * REST Resource: v3.folders.locations.operations
  * REST Resource: v3.folders.locations.policyBindings
  * REST Resource: v3.organizations.locations.operations
  * REST Resource: v3.organizations.locations.policyBindings
  * REST Resource: v3.organizations.locations.principalAccessBoundaryPolicies
  * REST Resource: v3.projects.locations.operations
  * REST Resource: v3.projects.locations.policyBindings
  * REST Resource: v2beta.policies
  * REST Resource: v2beta.policies.operations
  * REST Resource: v2.policies
  * REST Resource: v2.policies.operations
  * REST Resource: v1beta.projects.locations.workloadIdentityPools
  * REST Resource: v1beta.projects.locations.workloadIdentityPools.operations
  * REST Resource: v1beta.projects.locations.workloadIdentityPools.providers
  * REST Resource: v1beta.projects.locations.workloadIdentityPools.providers.operations
  * REST Resource: v1.iamPolicies
  * REST Resource: v1.locations.workforcePools
  * REST Resource: v1.locations.workforcePools.operations
  * REST Resource: v1.locations.workforcePools.providers
  * REST Resource: v1.locations.workforcePools.providers.keys
  * REST Resource: v1.locations.workforcePools.providers.operations
  * REST Resource: v1.locations.workforcePools.providers.scimTenants
  * REST Resource: v1.locations.workforcePools.providers.scimTenants.tokens
  * REST Resource: v1.locations.workforcePools.subjects
  * REST Resource: v1.organizations.roles
  * REST Resource: v1.permissions
  * REST Resource: v1.projects.locations.oauthClients
  * REST Resource: v1.projects.locations.oauthClients.credentials
  * REST Resource: v1.projects.locations.workloadIdentityPools
  * REST Resource: v1.projects.locations.workloadIdentityPools.namespaces
  * REST Resource: v1.projects.locations.workloadIdentityPools.namespaces.managedIdentities
  * REST Resource: v1.projects.locations.workloadIdentityPools.operations
  * REST Resource: v1.projects.locations.workloadIdentityPools.providers
  * REST Resource: v1.projects.locations.workloadIdentityPools.providers.keys
  * REST Resource: v1.projects.locations.workloadIdentityPools.providers.operations
  * REST Resource: v1.projects.roles
  * REST Resource: v1.projects.serviceAccounts
  * REST Resource: v1.projects.serviceAccounts.keys
  * REST Resource: v1.roles



## Service: iam.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://iam.googleapis.com/$discovery/rest?version=v3>
  * <https://iam.googleapis.com/$discovery/rest?version=v3beta>
  * <https://iam.googleapis.com/$discovery/rest?version=v2>
  * <https://iam.googleapis.com/$discovery/rest?version=v2beta>
  * <https://iam.googleapis.com/$discovery/rest?version=v1>
  * <https://iam.googleapis.com/$discovery/rest?version=v1beta>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://iam.googleapis.com`



## REST Resource: [v3beta.folders.locations.accessPolicies](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/create)` |  `POST /v3beta/{parent=folders/*/locations/*}/accessPolicies`   
Creates an access policy, and returns a long running operation.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/delete)` |  `DELETE /v3beta/{name=folders/*/locations/*/accessPolicies/*}`   
Deletes an access policy.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/get)` |  `GET /v3beta/{name=folders/*/locations/*/accessPolicies/*}`   
Gets an access policy.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/list)` |  `GET /v3beta/{parent=folders/*/locations/*}/accessPolicies`   
Lists access policies.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/patch)` |  `PATCH /v3beta/{accessPolicy.name=folders/*/locations/*/accessPolicies/*}`   
Updates an access policy.  
`[searchPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/searchPolicyBindings)` |  `GET /v3beta/{name=folders/*/locations/*/accessPolicies/*}:searchPolicyBindings`   
Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.  
  
## REST Resource: [v3beta.folders.locations.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.operations/get)` |  `GET /v3beta/{name=folders/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v3beta.folders.locations.policyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.policyBindings)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.policyBindings/create)` |  `POST /v3beta/{parent=folders/*/locations/*}/policyBindings`   
Creates a policy binding and returns a long-running operation.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.policyBindings/delete)` |  `DELETE /v3beta/{name=folders/*/locations/*/policyBindings/*}`   
Deletes a policy binding and returns a long-running operation.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.policyBindings/get)` |  `GET /v3beta/{name=folders/*/locations/*/policyBindings/*}`   
Gets a policy binding.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.policyBindings/list)` |  `GET /v3beta/{parent=folders/*/locations/*}/policyBindings`   
Lists policy bindings.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.policyBindings/patch)` |  `PATCH /v3beta/{policyBinding.name=folders/*/locations/*/policyBindings/*}`   
Updates a policy binding and returns a long-running operation.  
`[searchTargetPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.policyBindings/searchTargetPolicyBindings)` |  `GET /v3beta/{parent=folders/*/locations/*}/policyBindings:searchTargetPolicyBindings`   
Search policy bindings by target.  
  
## REST Resource: [v3beta.organizations.locations.accessPolicies](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/create)` |  `POST /v3beta/{parent=organizations/*/locations/*}/accessPolicies`   
Creates an access policy, and returns a long running operation.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/delete)` |  `DELETE /v3beta/{name=organizations/*/locations/*/accessPolicies/*}`   
Deletes an access policy.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/get)` |  `GET /v3beta/{name=organizations/*/locations/*/accessPolicies/*}`   
Gets an access policy.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/list)` |  `GET /v3beta/{parent=organizations/*/locations/*}/accessPolicies`   
Lists access policies.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/patch)` |  `PATCH /v3beta/{accessPolicy.name=organizations/*/locations/*/accessPolicies/*}`   
Updates an access policy.  
`[searchPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies/searchPolicyBindings)` |  `GET /v3beta/{name=organizations/*/locations/*/accessPolicies/*}:searchPolicyBindings`   
Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.  
  
## REST Resource: [v3beta.organizations.locations.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.operations/get)` |  `GET /v3beta/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v3beta.organizations.locations.policyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.policyBindings)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.policyBindings/create)` |  `POST /v3beta/{parent=organizations/*/locations/*}/policyBindings`   
Creates a policy binding and returns a long-running operation.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.policyBindings/delete)` |  `DELETE /v3beta/{name=organizations/*/locations/*/policyBindings/*}`   
Deletes a policy binding and returns a long-running operation.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.policyBindings/get)` |  `GET /v3beta/{name=organizations/*/locations/*/policyBindings/*}`   
Gets a policy binding.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.policyBindings/list)` |  `GET /v3beta/{parent=organizations/*/locations/*}/policyBindings`   
Lists policy bindings.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.policyBindings/patch)` |  `PATCH /v3beta/{policyBinding.name=organizations/*/locations/*/policyBindings/*}`   
Updates a policy binding and returns a long-running operation.  
`[searchTargetPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.policyBindings/searchTargetPolicyBindings)` |  `GET /v3beta/{parent=organizations/*/locations/*}/policyBindings:searchTargetPolicyBindings`   
Search policy bindings by target.  
  
## REST Resource: [v3beta.organizations.locations.principalAccessBoundaryPolicies](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/create)` |  `POST /v3beta/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies`   
Creates a principal access boundary policy, and returns a long running operation.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/delete)` |  `DELETE /v3beta/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}`   
Deletes a principal access boundary policy.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/get)` |  `GET /v3beta/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}`   
Gets a principal access boundary policy.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/list)` |  `GET /v3beta/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies`   
Lists principal access boundary policies.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/patch)` |  `PATCH /v3beta/{principalAccessBoundaryPolicy.name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}`   
Updates a principal access boundary policy.  
`[searchPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies/searchPolicyBindings)` |  `GET /v3beta/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}:searchPolicyBindings`   
Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.  
  
## REST Resource: [v3beta.projects.locations.accessPolicies](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.accessPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.accessPolicies/create)` |  `POST /v3beta/{parent=projects/*/locations/*}/accessPolicies`   
Creates an access policy, and returns a long running operation.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.accessPolicies/delete)` |  `DELETE /v3beta/{name=projects/*/locations/*/accessPolicies/*}`   
Deletes an access policy.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.accessPolicies/get)` |  `GET /v3beta/{name=projects/*/locations/*/accessPolicies/*}`   
Gets an access policy.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.accessPolicies/list)` |  `GET /v3beta/{parent=projects/*/locations/*}/accessPolicies`   
Lists access policies.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.accessPolicies/patch)` |  `PATCH /v3beta/{accessPolicy.name=projects/*/locations/*/accessPolicies/*}`   
Updates an access policy.  
`[searchPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.accessPolicies/searchPolicyBindings)` |  `GET /v3beta/{name=projects/*/locations/*/accessPolicies/*}:searchPolicyBindings`   
Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.  
  
## REST Resource: [v3beta.projects.locations.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.operations/get)` |  `GET /v3beta/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v3beta.projects.locations.policyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.policyBindings)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.policyBindings/create)` |  `POST /v3beta/{parent=projects/*/locations/*}/policyBindings`   
Creates a policy binding and returns a long-running operation.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.policyBindings/delete)` |  `DELETE /v3beta/{name=projects/*/locations/*/policyBindings/*}`   
Deletes a policy binding and returns a long-running operation.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.policyBindings/get)` |  `GET /v3beta/{name=projects/*/locations/*/policyBindings/*}`   
Gets a policy binding.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.policyBindings/list)` |  `GET /v3beta/{parent=projects/*/locations/*}/policyBindings`   
Lists policy bindings.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.policyBindings/patch)` |  `PATCH /v3beta/{policyBinding.name=projects/*/locations/*/policyBindings/*}`   
Updates a policy binding and returns a long-running operation.  
`[searchTargetPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.policyBindings/searchTargetPolicyBindings)` |  `GET /v3beta/{parent=projects/*/locations/*}/policyBindings:searchTargetPolicyBindings`   
Search policy bindings by target.  
  
## REST Resource: [v3.folders.locations.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.operations/get)` |  `GET /v3/{name=folders/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v3.folders.locations.policyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings/create)` |  `POST /v3/{parent=folders/*/locations/*}/policyBindings`   
Creates a policy binding and returns a long-running operation.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings/delete)` |  `DELETE /v3/{name=folders/*/locations/*/policyBindings/*}`   
Deletes a policy binding and returns a long-running operation.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings/get)` |  `GET /v3/{name=folders/*/locations/*/policyBindings/*}`   
Gets a policy binding.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings/list)` |  `GET /v3/{parent=folders/*/locations/*}/policyBindings`   
Lists policy bindings.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings/patch)` |  `PATCH /v3/{policyBinding.name=folders/*/locations/*/policyBindings/*}`   
Updates a policy binding and returns a long-running operation.  
`[searchTargetPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings/searchTargetPolicyBindings)` |  `GET /v3/{parent=folders/*/locations/*}/policyBindings:searchTargetPolicyBindings`   
Search policy bindings by target.  
  
## REST Resource: [v3.organizations.locations.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.operations/get)` |  `GET /v3/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v3.organizations.locations.policyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings/create)` |  `POST /v3/{parent=organizations/*/locations/*}/policyBindings`   
Creates a policy binding and returns a long-running operation.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings/delete)` |  `DELETE /v3/{name=organizations/*/locations/*/policyBindings/*}`   
Deletes a policy binding and returns a long-running operation.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings/get)` |  `GET /v3/{name=organizations/*/locations/*/policyBindings/*}`   
Gets a policy binding.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings/list)` |  `GET /v3/{parent=organizations/*/locations/*}/policyBindings`   
Lists policy bindings.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings/patch)` |  `PATCH /v3/{policyBinding.name=organizations/*/locations/*/policyBindings/*}`   
Updates a policy binding and returns a long-running operation.  
`[searchTargetPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings/searchTargetPolicyBindings)` |  `GET /v3/{parent=organizations/*/locations/*}/policyBindings:searchTargetPolicyBindings`   
Search policy bindings by target.  
  
## REST Resource: [v3.organizations.locations.principalAccessBoundaryPolicies](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/create)` |  `POST /v3/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies`   
Creates a principal access boundary policy, and returns a long running operation.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/delete)` |  `DELETE /v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}`   
Deletes a principal access boundary policy.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/get)` |  `GET /v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}`   
Gets a principal access boundary policy.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/list)` |  `GET /v3/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies`   
Lists principal access boundary policies.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/patch)` |  `PATCH /v3/{principalAccessBoundaryPolicy.name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}`   
Updates a principal access boundary policy.  
`[searchPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/searchPolicyBindings)` |  `GET /v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}:searchPolicyBindings`   
Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.  
  
## REST Resource: [v3.projects.locations.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.operations/get)` |  `GET /v3/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v3.projects.locations.policyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/create)` |  `POST /v3/{parent=projects/*/locations/*}/policyBindings`   
Creates a policy binding and returns a long-running operation.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/delete)` |  `DELETE /v3/{name=projects/*/locations/*/policyBindings/*}`   
Deletes a policy binding and returns a long-running operation.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/get)` |  `GET /v3/{name=projects/*/locations/*/policyBindings/*}`   
Gets a policy binding.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/list)` |  `GET /v3/{parent=projects/*/locations/*}/policyBindings`   
Lists policy bindings.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/patch)` |  `PATCH /v3/{policyBinding.name=projects/*/locations/*/policyBindings/*}`   
Updates a policy binding and returns a long-running operation.  
`[searchTargetPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings/searchTargetPolicyBindings)` |  `GET /v3/{parent=projects/*/locations/*}/policyBindings:searchTargetPolicyBindings`   
Search policy bindings by target.  
  
## REST Resource: [v2beta.policies](https://docs.cloud.google.com/iam/docs/reference/rest/v2beta/policies)

Methods  
---  
`[createPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v2beta/policies/createPolicy)` |  `POST /v2beta/{parent=policies/*/*}`   
Creates a policy.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v2beta/policies/delete)` |  `DELETE /v2beta/{name=policies/*/*/*}`   
Deletes a policy.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v2beta/policies/get)` |  `GET /v2beta/{name=policies/*/*/*}`   
Gets a policy.  
`[listPolicies](https://docs.cloud.google.com/iam/docs/reference/rest/v2beta/policies/listPolicies)` |  `GET /v2beta/{parent=policies/*/*}`   
Retrieves the policies of the specified kind that are attached to a resource.  
`[update](https://docs.cloud.google.com/iam/docs/reference/rest/v2beta/policies/update)` |  `PUT /v2beta/{policy.name=policies/*/*/*}`   
Updates the specified policy.  
  
## REST Resource: [v2beta.policies.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v2beta/policies.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v2beta/policies.operations/get)` |  `GET /v2beta/{name=policies/*/*/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v2.policies](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies)

Methods  
---  
`[createPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/createPolicy)` |  `POST /v2/{parent=policies/*/*}`   
Creates a policy.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/delete)` |  `DELETE /v2/{name=policies/*/*/*}`   
Deletes a policy.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/get)` |  `GET /v2/{name=policies/*/*/*}`   
Gets a policy.  
`[listPolicies](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/listPolicies)` |  `GET /v2/{parent=policies/*/*}`   
Retrieves the policies of the specified kind that are attached to a resource.  
`[update](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/update)` |  `PUT /v2/{policy.name=policies/*/*/*}`   
Updates the specified policy.  
  
## REST Resource: [v2.policies.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies.operations/get)` |  `GET /v2/{name=policies/*/*/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1beta.projects.locations.workloadIdentityPools](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/workloadIdentityPools`   
Creates a new `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/workloadIdentityPools/*}`   
Deletes a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/get)` |  `GET /v1beta/{name=projects/*/locations/*/workloadIdentityPools/*}`   
Gets an individual `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/workloadIdentityPools`   
Lists all non-deleted `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`s in a project.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/patch)` |  `PATCH /v1beta/{workloadIdentityPool.name=projects/*/locations/*/workloadIdentityPools/*}`   
Updates an existing `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/undelete)` |  `POST /v1beta/{name=projects/*/locations/*/workloadIdentityPools/*}:undelete`   
Undeletes a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1beta.projects.locations.workloadIdentityPools.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.operations/get)` |  `GET /v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1beta.projects.locations.workloadIdentityPools.providers](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/create)` |  `POST /v1beta/{parent=projects/*/locations/*/workloadIdentityPools/*}/providers`   
Creates a new `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)` in a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}`   
Deletes a `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/get)` |  `GET /v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}`   
Gets an individual `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/list)` |  `GET /v1beta/{parent=projects/*/locations/*/workloadIdentityPools/*}/providers`   
Lists all non-deleted `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`s in a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/patch)` |  `PATCH /v1beta/{workloadIdentityPoolProvider.name=projects/*/locations/*/workloadIdentityPools/*/providers/*}`   
Updates an existing `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/undelete)` |  `POST /v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}:undelete`   
Undeletes a `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1beta.projects.locations.workloadIdentityPools.providers.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers.operations/get)` |  `GET /v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.iamPolicies](https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies)

Methods  
---  
`[lintPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/lintPolicy)` |  `POST /v1/iamPolicies:lintPolicy`   
Lints, or validates, an IAM policy.  
`[queryAuditableServices](https://docs.cloud.google.com/iam/docs/reference/rest/v1/iamPolicies/queryAuditableServices)` |  `POST /v1/iamPolicies:queryAuditableServices`   
Returns a list of services that allow you to opt into audit logs that are not generated by default.  
  
## REST Resource: [v1.locations.workforcePools](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/create)` |  `POST /v1/{location=locations/*}/workforcePools`   
Creates a new `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/delete)` |  `DELETE /v1/{name=locations/*/workforcePools/*}`   
Deletes a `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/get)` |  `GET /v1/{name=locations/*/workforcePools/*}`   
Gets an individual `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
`[getIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/getIamPolicy)` |  `POST /v1/{resource=locations/*/workforcePools/*}:getIamPolicy`   
Gets IAM policies on a `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/list)` |  `GET /v1/{location=locations/*}/workforcePools`   
Lists all non-deleted `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`s under the specified parent.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/patch)` |  `PATCH /v1/{workforcePool.name=locations/*/workforcePools/*}`   
Updates an existing `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
`[setIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/setIamPolicy)` |  `POST /v1/{resource=locations/*/workforcePools/*}:setIamPolicy`   
Sets IAM policies on a `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
`[testIamPermissions](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/testIamPermissions)` |  `POST /v1/{resource=locations/*/workforcePools/*}:testIamPermissions`   
Returns the caller's permissions on the `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/undelete)` |  `POST /v1/{name=locations/*/workforcePools/*}:undelete`   
Undeletes a `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1.locations.workforcePools.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.operations/get)` |  `GET /v1/{name=locations/*/workforcePools/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.locations.workforcePools.providers](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create)` |  `POST /v1/{parent=locations/*/workforcePools/*}/providers`   
Creates a new `[WorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers#WorkforcePoolProvider)` in a `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/delete)` |  `DELETE /v1/{name=locations/*/workforcePools/*/providers/*}`   
Deletes a `[WorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers#WorkforcePoolProvider)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/get)` |  `GET /v1/{name=locations/*/workforcePools/*/providers/*}`   
Gets an individual `[WorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers#WorkforcePoolProvider)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/list)` |  `GET /v1/{parent=locations/*/workforcePools/*}/providers`   
Lists all non-deleted `[WorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers#WorkforcePoolProvider)`s in a `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/patch)` |  `PATCH /v1/{workforcePoolProvider.name=locations/*/workforcePools/*/providers/*}`   
Updates an existing `[WorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers#WorkforcePoolProvider)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/undelete)` |  `POST /v1/{name=locations/*/workforcePools/*/providers/*}:undelete`   
Undeletes a `[WorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers#WorkforcePoolProvider)`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1.locations.workforcePools.providers.keys](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/create)` |  `POST /v1/{parent=locations/*/workforcePools/*/providers/*}/keys`   
Creates a new `[WorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#WorkforcePoolProviderKey)` in a `[WorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers#WorkforcePoolProvider)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/delete)` |  `DELETE /v1/{name=locations/*/workforcePools/*/providers/*/keys/*}`   
Deletes a `[WorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#WorkforcePoolProviderKey)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/get)` |  `GET /v1/{name=locations/*/workforcePools/*/providers/*/keys/*}`   
Gets a `[WorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#WorkforcePoolProviderKey)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/list)` |  `GET /v1/{parent=locations/*/workforcePools/*/providers/*}/keys`   
Lists all non-deleted `[WorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#WorkforcePoolProviderKey)`s in a `[WorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers#WorkforcePoolProvider)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/undelete)` |  `POST /v1/{name=locations/*/workforcePools/*/providers/*/keys/*}:undelete`   
Undeletes a `[WorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys#WorkforcePoolProviderKey)`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1.locations.workforcePools.providers.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.operations/get)` |  `GET /v1/{name=locations/*/workforcePools/*/providers/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.locations.workforcePools.providers.scimTenants](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/create)` |  `POST /v1/{parent=locations/*/workforcePools/*/providers/*}/scimTenants`   
Gemini Enterprise only.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/delete)` |  `DELETE /v1/{name=locations/*/workforcePools/*/providers/*/scimTenants/*}`   
Gemini Enterprise only.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/get)` |  `GET /v1/{name=locations/*/workforcePools/*/providers/*/scimTenants/*}`   
Gemini Enterprise only.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/list)` |  `GET /v1/{parent=locations/*/workforcePools/*/providers/*}/scimTenants`   
Gemini Enterprise only.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/patch)` |  `PATCH /v1/{workforcePoolProviderScimTenant.name=locations/*/workforcePools/*/providers/*/scimTenants/*}`   
Gemini Enterprise only.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/undelete)` |  `POST /v1/{name=locations/*/workforcePools/*/providers/*/scimTenants/*}:undelete`   
Gemini Enterprise only.  
  
## REST Resource: [v1.locations.workforcePools.providers.scimTenants.tokens](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/create)` |  `POST /v1/{parent=locations/*/workforcePools/*/providers/*/scimTenants/*}/tokens`   
Gemini Enterprise only.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/delete)` |  `DELETE /v1/{name=locations/*/workforcePools/*/providers/*/scimTenants/*/tokens/*}`   
Gemini Enterprise only.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/get)` |  `GET /v1/{name=locations/*/workforcePools/*/providers/*/scimTenants/*/tokens/*}`   
Gemini Enterprise only.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/list)` |  `GET /v1/{parent=locations/*/workforcePools/*/providers/*/scimTenants/*}/tokens`   
Gemini Enterprise only.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/patch)` |  `PATCH /v1/{workforcePoolProviderScimToken.name=locations/*/workforcePools/*/providers/*/scimTenants/*/tokens/*}`   
Gemini Enterprise only.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/undelete)` |  `POST /v1/{name=locations/*/workforcePools/*/providers/*/scimTenants/*/tokens/*}:undelete`   
Gemini Enterprise only.  
  
## REST Resource: [v1.locations.workforcePools.subjects](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.subjects)

Methods  
---  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.subjects/delete)` |  `DELETE /v1/{name=locations/*/workforcePools/*/subjects/*}`   
Deletes a `WorkforcePoolSubject`.  
`[revokeSessions](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.subjects/revokeSessions)` |  `POST /v1/{name=locations/*/workforcePools/*/subjects/*}:revokeSessions`   
Revokes all sessions for the specified `WorkforcePoolSubject`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.subjects/undelete)` |  `POST /v1/{name=locations/*/workforcePools/*/subjects/*}:undelete`   
Undeletes a `WorkforcePoolSubject`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1.organizations.roles](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/create)` |  `POST /v1/{parent=organizations/*}/roles`   
Creates a new custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/delete)` |  `DELETE /v1/{name=organizations/*/roles/*}`   
Deletes a custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/get)` |  `GET /v1/{name=organizations/*/roles/*}`   
Gets the definition of a `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/list)` |  `GET /v1/{parent=organizations/*}/roles`   
Lists every predefined `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)` that IAM supports, or every custom role that is defined for an organization or project.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/patch)` |  `PATCH /v1/{name=organizations/*/roles/*}`   
Updates the definition of a custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/undelete)` |  `POST /v1/{name=organizations/*/roles/*}:undelete`   
Undeletes a custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
  
## REST Resource: [v1.permissions](https://docs.cloud.google.com/iam/docs/reference/rest/v1/permissions)

Methods  
---  
`[queryTestablePermissions](https://docs.cloud.google.com/iam/docs/reference/rest/v1/permissions/queryTestablePermissions)` |  `POST /v1/permissions:queryTestablePermissions`   
Lists every permission that you can test on a resource.  
  
## REST Resource: [v1.projects.locations.oauthClients](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/create)` |  `POST /v1/{parent=projects/*/locations/*}/oauthClients`   
Creates a new `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/delete)` |  `DELETE /v1/{name=projects/*/locations/*/oauthClients/*}`   
Deletes an `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/get)` |  `GET /v1/{name=projects/*/locations/*/oauthClients/*}`   
Gets an individual `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/list)` |  `GET /v1/{parent=projects/*/locations/*}/oauthClients`   
Lists all non-deleted `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`s in a project.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/patch)` |  `PATCH /v1/{oauthClient.name=projects/*/locations/*/oauthClients/*}`   
Updates an existing `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/undelete)` |  `POST /v1/{name=projects/*/locations/*/oauthClients/*}:undelete`   
Undeletes an `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1.projects.locations.oauthClients.credentials](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/create)` |  `POST /v1/{parent=projects/*/locations/*/oauthClients/*}/credentials`   
Creates a new `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/delete)` |  `DELETE /v1/{name=projects/*/locations/*/oauthClients/*/credentials/*}`   
Deletes an `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/get)` |  `GET /v1/{name=projects/*/locations/*/oauthClients/*/credentials/*}`   
Gets an individual `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/list)` |  `GET /v1/{parent=projects/*/locations/*/oauthClients/*}/credentials`   
Lists all `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`s in an `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/patch)` |  `PATCH /v1/{oauthClientCredential.name=projects/*/locations/*/oauthClients/*/credentials/*}`   
Updates an existing `[OauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials#OauthClientCredential)`.  
  
## REST Resource: [v1.projects.locations.workloadIdentityPools](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/create)` |  `POST /v1/{parent=projects/*/locations/*}/workloadIdentityPools`   
Creates a new `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/delete)` |  `DELETE /v1/{name=projects/*/locations/*/workloadIdentityPools/*}`   
Deletes a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/get)` |  `GET /v1/{name=projects/*/locations/*/workloadIdentityPools/*}`   
Gets an individual `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[getIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/getIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/workloadIdentityPools/*}:getIamPolicy`   
Gets the IAM policy of a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/list)` |  `GET /v1/{parent=projects/*/locations/*}/workloadIdentityPools`   
Lists all non-deleted `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`s in a project.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/patch)` |  `PATCH /v1/{workloadIdentityPool.name=projects/*/locations/*/workloadIdentityPools/*}`   
Updates an existing `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[setIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/workloadIdentityPools/*}:setIamPolicy`   
Sets the IAM policies on a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`  
`[testIamPermissions](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/workloadIdentityPools/*}:testIamPermissions`   
Returns the caller's permissions on a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/undelete)` |  `POST /v1/{name=projects/*/locations/*/workloadIdentityPools/*}:undelete`   
Undeletes a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1.projects.locations.workloadIdentityPools.namespaces](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/create)` |  `POST /v1/{parent=projects/*/locations/*/workloadIdentityPools/*}/namespaces`   
Creates a new `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)` in a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/delete)` |  `DELETE /v1/{name=projects/*/locations/*/workloadIdentityPools/*/namespaces/*}`   
Deletes a `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/get)` |  `GET /v1/{name=projects/*/locations/*/workloadIdentityPools/*/namespaces/*}`   
Gets an individual `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/list)` |  `GET /v1/{parent=projects/*/locations/*/workloadIdentityPools/*}/namespaces`   
Lists all non-deleted `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`s in a workload identity pool.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/patch)` |  `PATCH /v1/{workloadIdentityPoolNamespace.name=projects/*/locations/*/workloadIdentityPools/*/namespaces/*}`   
Updates an existing `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)` in a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/undelete)` |  `POST /v1/{name=projects/*/locations/*/workloadIdentityPools/*/namespaces/*}:undelete`   
Undeletes a `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1.projects.locations.workloadIdentityPools.namespaces.managedIdentities](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities)

Methods  
---  
`[addAttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/addAttestationRule)` |  `POST /v1/{resource=projects/*/locations/*/workloadIdentityPools/*/namespaces/*/managedIdentities/*}:addAttestationRule`   
Add an `[AttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/AttestationRule)` on a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/create)` |  `POST /v1/{parent=projects/*/locations/*/workloadIdentityPools/*/namespaces/*}/managedIdentities`   
Creates a new `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)` in a `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/delete)` |  `DELETE /v1/{name=projects/*/locations/*/workloadIdentityPools/*/namespaces/*/managedIdentities/*}`   
Deletes a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/get)` |  `GET /v1/{name=projects/*/locations/*/workloadIdentityPools/*/namespaces/*/managedIdentities/*}`   
Gets an individual `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/list)` |  `GET /v1/{parent=projects/*/locations/*/workloadIdentityPools/*/namespaces/*}/managedIdentities`   
Lists all non-deleted `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`s in a namespace.  
`[listAttestationRules](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/listAttestationRules)` |  `GET /v1/{resource=projects/*/locations/*/workloadIdentityPools/*/namespaces/*/managedIdentities/*}:listAttestationRules`   
List all `[AttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/AttestationRule)` on a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/patch)` |  `PATCH /v1/{workloadIdentityPoolManagedIdentity.name=projects/*/locations/*/workloadIdentityPools/*/namespaces/*/managedIdentities/*}`   
Updates an existing `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)` in a `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`.  
`[removeAttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/removeAttestationRule)` |  `POST /v1/{resource=projects/*/locations/*/workloadIdentityPools/*/namespaces/*/managedIdentities/*}:removeAttestationRule`   
Remove an `[AttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/AttestationRule)` on a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
`[setAttestationRules](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/setAttestationRules)` |  `POST /v1/{resource=projects/*/locations/*/workloadIdentityPools/*/namespaces/*/managedIdentities/*}:setAttestationRules`   
Set all `[AttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/AttestationRule)` on a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/undelete)` |  `POST /v1/{name=projects/*/locations/*/workloadIdentityPools/*/namespaces/*/managedIdentities/*}:undelete`   
Undeletes a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1.projects.locations.workloadIdentityPools.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.operations/get)` |  `GET /v1/{name=projects/*/locations/*/workloadIdentityPools/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.projects.locations.workloadIdentityPools.providers](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/create)` |  `POST /v1/{parent=projects/*/locations/*/workloadIdentityPools/*}/providers`   
Creates a new `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)` in a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/delete)` |  `DELETE /v1/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}`   
Deletes a `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/get)` |  `GET /v1/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}`   
Gets an individual `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/list)` |  `GET /v1/{parent=projects/*/locations/*/workloadIdentityPools/*}/providers`   
Lists all non-deleted `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`s in a `[WorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#WorkloadIdentityPool)`.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/patch)` |  `PATCH /v1/{workloadIdentityPoolProvider.name=projects/*/locations/*/workloadIdentityPools/*/providers/*}`   
Updates an existing `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/undelete)` |  `POST /v1/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}:undelete`   
Undeletes a `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1.projects.locations.workloadIdentityPools.providers.keys](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys/create)` |  `POST /v1/{parent=projects/*/locations/*/workloadIdentityPools/*/providers/*}/keys`   
Create a new `[WorkloadIdentityPoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys#WorkloadIdentityPoolProviderKey)` in a `[WorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys/delete)` |  `DELETE /v1/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*/keys/*}`   
Deletes an `[WorkloadIdentityPoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys#WorkloadIdentityPoolProviderKey)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys/get)` |  `GET /v1/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*/keys/*}`   
Gets an individual `[WorkloadIdentityPoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys#WorkloadIdentityPoolProviderKey)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys/list)` |  `GET /v1/{parent=projects/*/locations/*/workloadIdentityPools/*/providers/*}/keys`   
Lists all non-deleted `[WorkloadIdentityPoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys#WorkloadIdentityPoolProviderKey)`s in a project.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys/undelete)` |  `POST /v1/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*/keys/*}:undelete`   
Undeletes an `[WorkloadIdentityPoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys#WorkloadIdentityPoolProviderKey)`, as long as it was deleted fewer than 30 days ago.  
  
## REST Resource: [v1.projects.locations.workloadIdentityPools.providers.operations](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.operations/get)` |  `GET /v1/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.projects.roles](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/create)` |  `POST /v1/{parent=projects/*}/roles`   
Creates a new custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/delete)` |  `DELETE /v1/{name=projects/*/roles/*}`   
Deletes a custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/get)` |  `GET /v1/{name=projects/*/roles/*}`   
Gets the definition of a `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/list)` |  `GET /v1/{parent=projects/*}/roles`   
Lists every predefined `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)` that IAM supports, or every custom role that is defined for an organization or project.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/patch)` |  `PATCH /v1/{name=projects/*/roles/*}`   
Updates the definition of a custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/undelete)` |  `POST /v1/{name=projects/*/roles/*}:undelete`   
Undeletes a custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
  
## REST Resource: [v1.projects.serviceAccounts](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/create)` |  `POST /v1/{name=projects/*}/serviceAccounts`   
Creates a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/delete)` |  `DELETE /v1/{name=projects/*/serviceAccounts/*}`   
Deletes a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
`[disable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/disable)` |  `POST /v1/{name=projects/*/serviceAccounts/*}:disable`   
Disables a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)` immediately.  
`[enable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/enable)` |  `POST /v1/{name=projects/*/serviceAccounts/*}:enable`   
Enables a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)` that was disabled by `[DisableServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/disable#google.iam.admin.v1.IAM.DisableServiceAccount)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/get)` |  `GET /v1/{name=projects/*/serviceAccounts/*}`   
Gets a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
`[getIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy)` |  `POST /v1/{resource=projects/*/serviceAccounts/*}:getIamPolicy`   
Gets the IAM policy that is attached to a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/list)` |  `GET /v1/{name=projects/*}/serviceAccounts`   
Lists every `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)` that belongs to a specific project.  
`[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/patch)` |  `PATCH /v1/{serviceAccount.name=projects/*/serviceAccounts/*}`   
Patches a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
`[setIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy)` |  `POST /v1/{resource=projects/*/serviceAccounts/*}:setIamPolicy`   
Sets the IAM policy that is attached to a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
`[signBlob](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/signBlob)   
**(deprecated)**` |  `POST /v1/{name=projects/*/serviceAccounts/*}:signBlob`   
Signs a blob using the system-managed private key for a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
`[signJwt](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/signJwt)   
**(deprecated)**` |  `POST /v1/{name=projects/*/serviceAccounts/*}:signJwt`   
Signs a JSON Web Token (JWT) using the system-managed private key for a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
`[testIamPermissions](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/testIamPermissions)` |  `POST /v1/{resource=projects/*/serviceAccounts/*}:testIamPermissions`   
Tests whether the caller has the specified permissions on a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
`[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/undelete)` |  `POST /v1/{name=projects/*/serviceAccounts/*}:undelete`   
Restores a deleted `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
`[update](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/update)` |  `PUT /v1/{name=projects/*/serviceAccounts/*}`   
**Note:** We are in the process of deprecating this method.  
  
## REST Resource: [v1.projects.serviceAccounts.keys](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys)

Methods  
---  
`[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/create)` |  `POST /v1/{name=projects/*/serviceAccounts/*}/keys`   
Creates a `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.  
`[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/delete)` |  `DELETE /v1/{name=projects/*/serviceAccounts/*/keys/*}`   
Deletes a `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.  
`[disable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/disable)` |  `POST /v1/{name=projects/*/serviceAccounts/*/keys/*}:disable`   
Disable a `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.  
`[enable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/enable)` |  `POST /v1/{name=projects/*/serviceAccounts/*/keys/*}:enable`   
Enable a `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/get)` |  `GET /v1/{name=projects/*/serviceAccounts/*/keys/*}`   
Gets a `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/list)` |  `GET /v1/{name=projects/*/serviceAccounts/*}/keys`   
Lists every `[ServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)` for a service account.  
`[upload](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/upload)` |  `POST /v1/{name=projects/*/serviceAccounts/*}/keys:upload`   
Uploads the public key portion of a key pair that you manage, and associates the public key with a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.  
  
## REST Resource: [v1.roles](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles)

Methods  
---  
`[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles/get)` |  `GET /v1/{name=roles/*}`   
Gets the definition of a `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
`[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles/list)` |  `GET /v1/roles`   
Lists every predefined `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)` that IAM supports, or every custom role that is defined for an organization or project.  
`[queryGrantableRoles](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles/queryGrantableRoles)` |  `POST /v1/roles:queryGrantableRoles`   
Lists roles that can be granted on a Google Cloud resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
