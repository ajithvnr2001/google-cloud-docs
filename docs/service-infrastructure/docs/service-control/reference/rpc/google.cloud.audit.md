---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit
title: Package google.cloud.audit \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:35.046247+00:00
---

# Package google.cloud.audit  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Package google.cloud.audit Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AuditLog](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.AuditLog)` (message)
  * `[AuthenticationInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.AuthenticationInfo)` (message)
  * `[AuthorizationInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.AuthorizationInfo)` (message)
  * `[RequestMetadata](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.RequestMetadata)` (message)
  * `[ResourceLocation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.ResourceLocation)` (message)
  * `[ServiceAccountDelegationInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.ServiceAccountDelegationInfo)` (message)
  * `[ServiceAccountDelegationInfo.FirstPartyPrincipal](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.ServiceAccountDelegationInfo.FirstPartyPrincipal)` (message)
  * `[ServiceAccountDelegationInfo.ThirdPartyPrincipal](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.ServiceAccountDelegationInfo.ThirdPartyPrincipal)` (message)



## AuditLog

Common audit log format for Google Cloud Platform API operations.

Fields  
---  
`service_name` |  `string` The name of the API service performing the operation. For example, `"compute.googleapis.com"`.  
`method_name` |  `string` The name of the service method or operation. For API calls, this should be the name of the API method. For example,
    
    
    "google.cloud.bigquery.v2.TableService.InsertTable"
    "google.logging.v2.ConfigServiceV2.CreateSink"
      
  
`resource_name` |  `string` The resource or collection that is the target of the operation. The name is a scheme-less URI, not including the API service name. For example:
    
    
    "projects/PROJECT_ID/zones/us-central1-a/instances"
    "projects/PROJECT_ID/datasets/DATASET_ID"
      
  
`resource_location` |  ``[ResourceLocation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.ResourceLocation)`` The resource location information.  
`resource_original_state` |  ``[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)`` The resource's original state before mutation. Present only for operations which have successfully modified the targeted resource(s). In general, this field should contain all changed fields, except those that are already been included in `request`, `response`, `metadata` or `service_data` fields. When the JSON object represented here has a proto equivalent, the proto name will be indicated in the `@type` property.  
`num_response_items` |  `int64` The number of items returned from a List or Query API method, if applicable.  
`status` |  ``[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc#google.rpc.Status)`` The status of the overall operation.  
`authentication_info` |  ``[AuthenticationInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.AuthenticationInfo)`` Authentication information.  
`authorization_info[]` |  ``[AuthorizationInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.AuthorizationInfo)`` Authorization information. If there are multiple resources or permissions involved, then there is one AuthorizationInfo element for each {resource, permission} tuple.  
`request_metadata` |  ``[RequestMetadata](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.RequestMetadata)`` Metadata about the operation.  
`request` |  ``[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)`` The operation request. This may not include all request parameters, such as those that are too large, privacy-sensitive, or duplicated elsewhere in the log record. It should never include user-generated data, such as file contents. When the JSON object represented here has a proto equivalent, the proto name will be indicated in the `@type` property.  
`response` |  ``[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)`` The operation response. This may not include all response elements, such as those that are too large, privacy-sensitive, or duplicated elsewhere in the log record. It should never include user-generated data, such as file contents. When the JSON object represented here has a proto equivalent, the proto name will be indicated in the `@type` property.  
`metadata` |  ``[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)`` Other service-specific data about the request, response, and other information associated with the current audited event.  
`service_data  
**(deprecated)**` |  ``[Any](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` This item is deprecated!Deprecated. Use the `metadata` field instead. Other service-specific data about the request, response, and other activities.  
  
## AuthenticationInfo

Authentication information for the operation.

Fields  
---  
`principal_email` |  `string` The email address of the authenticated user (or service account on behalf of third party principal) making the request. For third party identity callers, the `principal_subject` field is populated instead of this field. For privacy reasons, the principal email address is sometimes redacted. For more information, see [Caller identities in audit logs](https://cloud.google.com/logging/docs/audit#user-id).  
`authority_selector` |  `string` The authority selector specified by the requestor, if any. It is not guaranteed that the principal was allowed to use this authority.  
`third_party_principal` |  ``[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)`` The third party identification (if any) of the authenticated user making the request. When the JSON object represented here has a proto equivalent, the proto name will be indicated in the `@type` property.  
`service_account_key_name` |  `string` The name of the service account key used to create or exchange credentials for authenticating the service account making the request. This is a scheme-less URI full resource name. For example:"//iam.googleapis.com/projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}"  
`service_account_delegation_info[]` |  ``[ServiceAccountDelegationInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.ServiceAccountDelegationInfo)`` Identity delegation history of an authenticated service account that makes the request. It contains information on the real authorities that try to access GCP resources by delegating on a service account. When multiple authorities present, they are guaranteed to be sorted based on the original ordering of the identity delegation events.  
`principal_subject` |  `string` String representation of identity of requesting party. Populated for both first and third party identities.  
  
## AuthorizationInfo

Authorization information for the operation.

Fields  
---  
`resource` |  `string` The resource being accessed, as a REST-style string. For example:
    
    
    bigquery.googleapis.com/projects/PROJECTID/datasets/DATASETID
      
  
`permission` |  `string` The required IAM permission.  
`granted` |  `bool` Whether or not authorization for `resource` and `permission` was granted.  
`resource_attributes` |  ``[Resource](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Resource)`` Resource attributes used in IAM condition evaluation. This field contains resource attributes like resource type and resource name.To get the whole view of the attributes used in IAM condition evaluation, the user must also look into `AuditLog.request_metadata.request_attributes`.  
  
## RequestMetadata

Metadata about the request.

Fields  
---  
`caller_ip` |  `string` The IP address of the caller. For caller from internet, this will be public IPv4 or IPv6 address. For caller from a Compute Engine VM with external IP address, this will be the VM's external IP address. For caller from a Compute Engine VM without external IP address, if the VM is in the same organization (or project) as the accessed resource, `caller_ip` will be the VM's internal IPv4 address, otherwise the `caller_ip` will be redacted to "gce-internal-ip". See <https://cloud.google.com/compute/docs/vpc/> for more information.  
`caller_supplied_user_agent` |  `string` The user agent of the caller. This information is not authenticated and should be treated accordingly. For example:

  * `google-api-python-client/1.4.0`: The request was made by the Google API client for Python.
  * `Cloud SDK Command Line Tool apitools-client/1.0 gcloud/0.9.62`: The request was made by the Google Cloud SDK CLI (gcloud).
  * `AppEngine-Google; (+http://code.google.com/appengine; appid: s~my-project`: The request was made from the `my-project` App Engine app. NOLINT

  
`caller_network` |  `string` The network of the caller. Set only if the network host project is part of the same GCP organization (or project) as the accessed resource. See <https://cloud.google.com/compute/docs/vpc/> for more information. This is a scheme-less URI full resource name. For example:
    
    
    "//compute.googleapis.com/projects/PROJECT_ID/global/networks/NETWORK_ID"
      
  
`request_attributes` |  ``[Request](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Request)`` Request attributes used in IAM condition evaluation. This field contains request attributes like request time and access levels associated with the request.To get the whole view of the attributes used in IAM condition evaluation, the user must also look into `AuditLog.authentication_info.resource_attributes`.  
`destination_attributes` |  ``[Peer](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext.Peer)`` The destination of a network activity, such as accepting a TCP connection. In a multi hop network activity, the destination represents the receiver of the last hop. Only two fields are used in this message, Peer.port and Peer.ip. These fields are optionally populated by those services utilizing the IAM condition feature.  
  
## ResourceLocation

Location information about a resource.

Fields  
---  
`current_locations[]` |  `string` The locations of a resource after the execution of the operation. Requests to create or delete a location based resource must populate the 'current_locations' field and not the 'original_locations' field. For example:
    
    
    "europe-west1-a"
    "us-east1"
    "nam3"
      
  
`original_locations[]` |  `string` The locations of a resource prior to the execution of the operation. Requests that mutate the resource's location must populate both the 'original_locations' as well as the 'current_locations' fields. For example:
    
    
    "europe-west1-a"
    "us-east1"
    "nam3"
      
  
## ServiceAccountDelegationInfo

Identity delegation history of an authenticated service account.

Fields  
---  
Union field `Authority`. Entity that creates credentials for service account and assumes its identity for authentication. `Authority` can be only one of the following:  
`first_party_principal` |  ``[FirstPartyPrincipal](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.ServiceAccountDelegationInfo.FirstPartyPrincipal)`` First party (Google) identity as the real authority.  
`third_party_principal` |  ``[ThirdPartyPrincipal](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.ServiceAccountDelegationInfo.ThirdPartyPrincipal)`` Third party identity as the real authority.  
  
## FirstPartyPrincipal

First party identity principal.

Fields  
---  
`principal_email` |  `string` The email address of a Google account. .  
`service_metadata` |  ``[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)`` Metadata about the service that uses the service account. .  
  
## ThirdPartyPrincipal

Third party identity principal.

Fields  
---  
`third_party_claims` |  ``[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)`` Metadata about third party identity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
