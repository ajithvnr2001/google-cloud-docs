---
url: https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha
title: Package google.cloud.ftp.v1alpha \u00a0|\u00a0 Cloud FTP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:43.639883+00:00
---

# Package google.cloud.ftp.v1alpha  |  Cloud FTP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ APIs & Reference ](https://docs.cloud.google.com/cloud-ftp/apis)



Send feedback 

#  Package google.cloud.ftp.v1alpha Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[CloudFtp](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.CloudFtp)` (interface)
  * `[CreateServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.CreateServerRequest)` (message)
  * `[CreateUserRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.CreateUserRequest)` (message)
  * `[DeleteServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.DeleteServerRequest)` (message)
  * `[DeleteUserRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.DeleteUserRequest)` (message)
  * `[ExternalServerConfig](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ExternalServerConfig)` (message)
  * `[GetServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.GetServerRequest)` (message)
  * `[GetUserRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.GetUserRequest)` (message)
  * `[InternalServerConfig](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.InternalServerConfig)` (message)
  * `[InternalServerConfig.AllowedConsumer](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.InternalServerConfig.AllowedConsumer)` (message)
  * `[InternalServerConfig.DeniedConsumer](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.InternalServerConfig.DeniedConsumer)` (message)
  * `[InternalServerConfig.PscEndpoint](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.InternalServerConfig.PscEndpoint)` (message)
  * `[ListServersRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ListServersRequest)` (message)
  * `[ListServersResponse](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ListServersResponse)` (message)
  * `[ListUsersRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ListUsersRequest)` (message)
  * `[ListUsersResponse](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ListUsersResponse)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.OperationMetadata)` (message)
  * `[Server](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.Server)` (message)
  * `[Server.AccessType](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.Server.AccessType)` (enum)
  * `[Server.State](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.Server.State)` (enum)
  * `[ServerCredential](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ServerCredential)` (message)
  * `[ServerView](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ServerView)` (enum)
  * `[StartServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.StartServerRequest)` (message)
  * `[StopServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.StopServerRequest)` (message)
  * `[StorageDirectoryMapping](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.StorageDirectoryMapping)` (message)
  * `[StorageDirectoryMapping.Permission](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.StorageDirectoryMapping.Permission)` (enum)
  * `[UpdateServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.UpdateServerRequest)` (message)
  * `[UpdateUserRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.UpdateUserRequest)` (message)
  * `[User](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.User)` (message)
  * `[User.State](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.User.State)` (enum)
  * `[UserCredential](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.UserCredential)` (message)
  * `[UserCredential.Type](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.UserCredential.Type)` (enum)
  * `[UserView](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.UserView)` (enum)



## CloudFtp

Service describing handlers for resources

CreateServer  
---  
` rpc CreateServer(`[CreateServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.CreateServerRequest)`) returns (`[Operation](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new Server in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ftp.servers.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateUser  
---  
` rpc CreateUser(`[CreateUserRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.CreateUserRequest)`) returns (`[Operation](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new User in a given project and location and Server.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ftp.users.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteServer  
---  
` rpc DeleteServer(`[DeleteServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.DeleteServerRequest)`) returns (`[Operation](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single Server.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ftp.servers.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteUser  
---  
` rpc DeleteUser(`[DeleteUserRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.DeleteUserRequest)`) returns (`[Operation](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single User.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ftp.users.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetServer  
---  
` rpc GetServer(`[GetServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.GetServerRequest)`) returns (`[Server](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.Server)`) ` Gets details of a single Server.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ftp.servers.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetUser  
---  
` rpc GetUser(`[GetUserRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.GetUserRequest)`) returns (`[User](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.User)`) ` Gets details of a single User.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ftp.users.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListServers  
---  
` rpc ListServers(`[ListServersRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ListServersRequest)`) returns (`[ListServersResponse](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ListServersResponse)`) ` Lists Servers in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ftp.servers.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListUsers  
---  
` rpc ListUsers(`[ListUsersRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ListUsersRequest)`) returns (`[ListUsersResponse](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ListUsersResponse)`) ` Lists Users in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ftp.users.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
StartServer  
---  
` rpc StartServer(`[StartServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.StartServerRequest)`) returns (`[Operation](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Starts a stopping/stopped Server.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ftp.servers.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
StopServer  
---  
` rpc StopServer(`[StopServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.StopServerRequest)`) returns (`[Operation](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Stops an active Server.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ftp.servers.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateServer  
---  
` rpc UpdateServer(`[UpdateServerRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.UpdateServerRequest)`) returns (`[Operation](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates the parameters of a single Server.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ftp.servers.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateUser  
---  
` rpc UpdateUser(`[UpdateUserRequest](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.UpdateUserRequest)`) returns (`[Operation](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates the parameters of a single User.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ftp.users.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## CreateServerRequest

Message for creating a Server

Fields  
---  
`parent` |  `string` Required. Value for parent.  
`server_id` |  `string` Required. A unique ID for the server. Must start with a lowercase letter, and end with a lowercase letter or number. Can contain lowercase letters, numbers, and hyphens. Maximum length is 30 characters.  
`server` |  `[Server](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.Server)` Required. The resource being created  
`request_id` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
## CreateUserRequest

Message for creating a User

Fields  
---  
`parent` |  `string` Required. Value for parent.  
`user_id` |  `string` Required. A unique user ID for the SFTP user. The user ID must start with a lowercase letter and can include lowercase letters, numbers, or hyphens.  
`user` |  `[User](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.User)` Required. The resource being created  
`request_id` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
## DeleteServerRequest

Message for deleting a Server Note: Cascading delete is not supported. Any nested User resources under this Server must be deleted before the Server itself can be deleted. Attempting to delete a Server with active User resources will result in an error.

Fields  
---  
`name` |  `string` Required. Name of the resource  
  
## DeleteUserRequest

Message for deleting a User

Fields  
---  
`name` |  `string` Required. Name of the resource  
`force` |  `bool` Optional. If set to true, the request will force the deletion of the User.  
  
## ExternalServerConfig

Configuration for external server.

Fields  
---  
`ip_address` |  `string` Output only. IP address of the LB via which clients will connect.  
`allowed_cidr_blocks[]` |  `string` Optional. List of CIDR blocks that are allowed to access the Server. A CIDR range consists of an IP Address and a prefix length to construct the subnet mask. By default, the prefix length is 32 (i.e. matches a single IP address). For now, only IPV4 addresses are supported. Examples: "203.0.113.0/24" - matches with the IP addresses in the range 203.0.113.0 - 203.0.113.255. "0.0.0.0/0" - matches against any IP address. This field must contain at least one entry if the access type is EXTERNAL. The number of allowed CIDR blocks cannot exceed 500. Example: 192.168.0.0/16  
  
## GetServerRequest

Message for getting a Server

Fields  
---  
`name` |  `string` Required. Name of the resource  
`view` |  `[ServerView](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ServerView)` Optional. The view of the Server resource to return.  
  
## GetUserRequest

Message for getting a User

Fields  
---  
`name` |  `string` Required. Name of the resource  
`view` |  `[UserView](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.UserView)` Optional. The view of the User resource to return.  
  
## InternalServerConfig

Configuration for private server accessible via PSC.

Fields  
---  
`service_attachment` |  `string` Output only. The resource name of the service attachment. Format: `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`  
`consumer_accept_list[]` |  `[AllowedConsumer](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.InternalServerConfig.AllowedConsumer)` Required. A list of projects that are permitted to connect. At least one project is required in the allow list.  
`consumer_reject_list[]` |  `[DeniedConsumer](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.InternalServerConfig.DeniedConsumer)` Optional. A list of projects that are denied connection. Format: "projects/sample_project_id" or "projects/1234567890" Projects in this list will be denied access, even if they are included in the `allow_list`. If this list is empty, no projects are explicitly rejected.  
`psc_endpoints[]` |  `[PscEndpoint](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.InternalServerConfig.PscEndpoint)` Output only. Details of endpoints created by the customer.  
  
## AllowedConsumer

A consumer project or network that is permitted to connect to the server via PSC.

Fields  
---  
`connection_limit` |  `int64` Required. The connection limit for the consumer. Value must be greater than 0.  
Union field `consumer_type`. Required. Specifies the type of consumer. `consumer_type` can be only one of the following:  
`project` |  `string` The project ID or number of the consumer project. Must be in the format: `projects/{project}`.  
  
## DeniedConsumer

A consumer project or network that is denied to connect to the server via PSC.

Fields  
---  
Union field `consumer_type`. Required. Specifies the type of consumer. `consumer_type` can be only one of the following:  
`project` |  `string` The project ID or number of the consumer project. Must be in the format: `projects/{project}`.  
  
## PscEndpoint

Details of PSC endpoint created by customer.

Fields  
---  
`endpoint` |  `string` Output only. This is a Resource name for Private Service Connect endpoint. Format: `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`  
`network` |  `string` Output only. The consumer network. Format: `projects/{project}/locations/{location}/networks/{network}`  
`status` |  `string` Output only. The status of the connected endpoint.  
  
## ListServersRequest

Message for requesting list of Servers

Fields  
---  
`parent` |  `string` Required. Parent value for ListServersRequest  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results  
`order_by` |  `string` Optional. Hint for how to order the results  
`view` |  `[ServerView](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ServerView)` Optional. The view of the Server resource to return.  
  
## ListServersResponse

Message for response to listing Servers

Fields  
---  
`servers[]` |  `[Server](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.Server)` The list of Server  
`next_page_token` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
## ListUsersRequest

Message for requesting list of Users

Fields  
---  
`parent` |  `string` Required. Parent value for ListUsersRequest  
`page_size` |  `int32` Optional. Requested page size. User may return fewer items than requested. The maximum value is 1000; The default value is 50 if the field is omitted (or set to 0).  
`page_token` |  `string` Optional. A token identifying a page of results the user should return.  
`filter` |  `string` Optional. Filtering results  
`order_by` |  `string` Optional. Hint for how to order the results  
`view` |  `[UserView](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.UserView)` Optional. The view of the User resource to return.  
  
## ListUsersResponse

Message for response to listing Users

Fields  
---  
`users[]` |  `[User](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.User)` The list of User  
`next_page_token` |  `string` A token identifying a page of results the user should return.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
## OperationMetadata

Represents the metadata of the long-running operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`target` |  `string` Output only. Server-defined resource path for the target of the operation.  
`verb` |  `string` Output only. Name of the verb executed by the operation.  
`status_message` |  `string` Output only. Human-readable status of the operation, if any.  
`requested_cancellation` |  `bool` Output only. Identifies whether the user has requested cancellation of the operation. Operations that have been cancelled successfully have `[google.longrunning.Operation.error](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.rpc.Status.google.longrunning.Operation.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of `1`, corresponding to `Code.CANCELLED`.  
`api_version` |  `string` Output only. API version used to start the operation.  
  
## Server

Message describing Server object

Fields  
---  
`name` |  `string` Identifier. name of resource  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. [Output only] Create time stamp  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. [Output only] Update time stamp  
`labels` |  `map<string, string>` Optional. Labels as key value pairs  
`display_name` |  `string` Optional. Display name of the Server  
`access_type` |  `[AccessType](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.Server.AccessType)` Required. The access type of the Server.  
`state` |  `[State](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.Server.State)` Output only. The state of the server.  
`google_managed_server_credential` |  `[ServerCredential](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ServerCredential)` Output only. Credentials of the FTP Server.  
`service_agent` |  `string` Output only. Service agent used to access the customer bucket.  
Union field `access_config`. Configuration for server access. If this is set, it must match the value in the `access_type` field. `access_config` can be only one of the following:  
`external_config` |  `[ExternalServerConfig](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.ExternalServerConfig)` Configuration for external access.  
`internal_config` |  `[InternalServerConfig](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.InternalServerConfig)` Configuration for internal access.  
  
## AccessType

The access type of the Server.

Enums  
---  
`ACCESS_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`EXTERNAL` | Server is assigned a public IP.  
`INTERNAL` | Server is assigned an internal IP.  
  
## State

Tracks Server status.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`CREATING` | Server is being created.  
`STARTING` | Server is starting.  
`ACTIVE` | Server is ready to be used.  
`STOPPING` | Server is stopping.  
`STOPPED` | Server is stopped.  
`DELETING` | Server is being deleted.  
`ERROR` | Server is in error state.  
`UPDATING` | Server is being updated.  
  
## ServerCredential

Represents credentials of an FTP Server.

Fields  
---  
`fingerprint` |  `string` Output only. The fingerprint is a hash of the public key, and is displayed when clients access the server for the first time to verify the server's identity.  
`asymmetric_algorithm` |  `string` Output only. Asymmetric algorithm used by the public key. Possible values (can be expanded in future): - ssh-ed25519  
  
## ServerView

View for Server resource.

Enums  
---  
`SERVER_VIEW_UNSPECIFIED` | Default value. Equivalent to SERVER_VIEW_BASIC.  
`SERVER_VIEW_BASIC` | Basic view. Excludes heavy configurations (internal_config, external_config, google_managed_server_credential).  
`SERVER_VIEW_FULL` | Full view. Includes all fields.  
  
## StartServerRequest

Request message for starting a Server.

Fields  
---  
`name` |  `string` Required. Name of the resource Format: `projects/{project}/locations/{location}/servers/{server}`  
  
## StopServerRequest

Request message for stopping a Server.

Fields  
---  
`name` |  `string` Required. Name of the resource. Format: `projects/{project}/locations/{location}/servers/{server}`  
  
## StorageDirectoryMapping

Mapping of backing Cloud Storage path to the directory where the user lands in the SFTP server. If directory is not specified, it'll default to '/'.

Eg 1 - (bucket_name: bucket, bucket_prefix: path1/path2, directory: /abc/def/username)

The user will land at /abcd/def/username, and the view there will match that of /bucket/path1/path2. The user will not be aware of Cloud Storage prefix '/bucket/path1' and there will be no such directory in the view.

Eg 2 - (bucket_name: bucket, bucket_prefix: path1/path2, directory: '')

The user will land at '/', and the view there will match that of /bucket/path1/path2. The user will not be aware of Cloud Storage prefix '/bucket/path1/path2' and there will be no such directory in the view.

Fields  
---  
`bucket` |  `string` Required. Name of the bucket.  
`bucket_prefix` |  `string` Optional. Prefix inside the bucket.  
`directory` |  `string` Required. Directory where the user lands in the SFTP server.  
`permission` |  `[Permission](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.StorageDirectoryMapping.Permission)` Required. Permission to the bucket.  
  
## Permission

Tracks read/write access to the bucket.

Enums  
---  
`PERMISSION_UNSPECIFIED` | Permission unspecified.  
`READ_ONLY` | Read only permission.  
`READ_WRITE` | Read write permission.  
  
## UpdateServerRequest

Message for updating a Server

Fields  
---  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to specify the fields to be overwritten in the Server resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields present in the request will be overwritten.  
`server` |  `[Server](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.Server)` Required. The resource being updated  
`request_id` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
## UpdateUserRequest

Message for updating a User

Fields  
---  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to specify the fields to be overwritten in the User resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields present in the request will be overwritten.  
`user` |  `[User](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.User)` Required. The resource being updated  
  
## User

Message describing User object

Fields  
---  
`name` |  `string` Identifier. User-friendly name via which User will be identified. projects/{project}/locations/{location}/servers/{server}/users/{user}  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. [Output only] Create time stamp  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. [Output only] Update time stamp  
`labels` |  `map<string, string>` Optional. Labels as key value pairs  
`username` |  `string` Output only. [Output only] The username of the user.  
`customer_service_account` |  `string` Required. Service account in customer project attached to this SFTP User.  
`state` |  `[State](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.User.State)` Output only. Tracks user creation.  
`user_credentials[]` |  `[UserCredential](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.UserCredential)` Required. User credential for the user. The maximum number of user credentials is 10.  
`storage_directory_mappings[]` |  `[StorageDirectoryMapping](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.StorageDirectoryMapping)` Required. Mapping of Cloud Storage buckets to directories where the user will land in the SFTP server.  
  
## State

Tracks user creation.

Enums  
---  
`STATE_UNSPECIFIED` | State unspecified.  
`CREATING` | User is being created.  
`ACTIVE` | User is ready to be used.  
`ERROR` | User creation failed.  
`UPDATING` | The resource is being updated.  
`DELETING` | The resource is being deleted.  
  
## UserCredential

Message describing UserCredential object

Fields  
---  
`credential_name` |  `string` Required. Name of the user credential.  
`credential_type` |  `[Type](https://docs.cloud.google.com/cloud-ftp/reference/rpc/google.cloud.ftp.v1alpha#google.cloud.ftp.v1alpha.UserCredential.Type)` Required. Type of credential.  
`ssh_public_key_body` |  `string` Optional. SSH public key body in OpenSSH format. Example: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ..."  
  
## Type

Type of credential.

Enums  
---  
`TYPE_UNSPECIFIED` | Type unspecified.  
`PUBLIC_KEY` | Public key credential.  
  
## UserView

View for User resource.

Enums  
---  
`USER_VIEW_UNSPECIFIED` | Default value. Equivalent to USER_VIEW_BASIC.  
`USER_VIEW_BASIC` | Basic view. Excludes heavy configurations (user_credentials, storage_directory_mappings).  
`USER_VIEW_FULL` | Full view. Includes all fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
