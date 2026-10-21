---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/github-changelog/
title: Change log for GITHUB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:18:34.943040+00:00
---

# Change log for GITHUB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/github-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GITHUB

Date | Changes  
---|---  
2026-06-08 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `Timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `Body` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `service.name` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `host.name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `data.timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.business`, `data._document_id`, `data_old_permission`, `data_server_id`, `data_request_category`, `data_device_cookie`, `data_is_robot`, `data_actor_is_bot`, `code_namespace`, `code_function` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `data.category_type` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `data.external_identity_nameid`, `data_actor_session`, `data_client_id` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `TraceId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.roles.name`: Newly mapped `data.permission` raw log field with `event.idm.read_only_udm.target.user.attribute.roles.name` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `data.method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude`: Newly mapped `data.actor_location.location.lat` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude`: Newly mapped `data.actor_location.location.lon` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `data.request_id`, `SpanId` raw log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `data.user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `data.user_agent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `data.referrer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `data.url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `data_controller_action`, `gh_request_id`, `data_request_access_security_header`, `TraceFlags` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `gh_search_cache_key_value` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-05-18 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `invitee` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.src.user.userid`: Newly mapped `inviter` raw log field with `event.idm.read_only_udm.src.user.userid` UDM field.   
2026-04-02 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Removed mapping of `pull_request.user.login` from `event.idm.read_only_udm.principal.user.user_display_name` UDM field as `pull_request.user.login` is a primary unique identifier for the user recognized within the source system.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `pull_request.user.login` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Removed mapping of `pull_request.user.id` from `event.idm.read_only_udm.principal.user.attribute.labels` UDM field as `pull_request.user.id` is a product-specific unique identifier for the user entity.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Mapped `pull_request.user.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.src.user.user_display_name`: Removed mapping of `sender.login` from `event.idm.read_only_udm.src.user.user_display_name` UDM field as `sender.login` is a primary unique identifier for the user within the source system.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `sender.login` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when there is no existing value in `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.src.user.product_object_id`: Removed mapping of `sender.id` from `event.idm.read_only_udm.src.user.product_object_id` UDM field as `sender.id` is a product-specific unique identifier for the user entity.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Mapped `sender.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field when there is no existing value in `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.src.asset_id`, `event.idm.read_only_udm.src.asset.asset_id`: Removed mapping of `sender.node_id` from `event.idm.read_only_udm.src.asset_id` and `event.idm.read_only_udm.src.asset.asset_id` UDM fields as `sender.node_id` is a unique and stable identifier responsible for the event.  
\- `event.idm.read_only_udm.principal.asset_id`, `event.idm.read_only_udm.principal.asset.asset_id`: Mapped `sender.node_id` raw log field with `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` UDM fields when there is no existing value in `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.src.url`: Removed mapping of `sender.url` from `event.idm.read_only_udm.src.url` UDM field as `sender.url` provides details about the actor who initiated the event.  
\- `event.idm.read_only_udm.principal.url`: Mapped `sender.url` raw log field with `event.idm.read_only_udm.principal.url` UDM field when there is no existing value in `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS`, `USER_UNCATEGORIZED` and `GENERIC_EVENT` based on the availability of the required fields.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `repository.custom_properties.criticality` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `repository` sub fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field using map function.   
2026-03-27 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Added required conditional checks to update the value of `event.idm.read_only_udm.metadata.event_type` to NETWORK_HTTP.  
\- `event.idm.read_only_udm.principal.hostname`,`event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `host.name` and `host` raw log fields with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `logData.Level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `logData.Level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `logData.Method` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.ip`,`event.idm.read_only_udm.principal.asset.ip`: Newly mapped `logData.IdentityName` and `logData.IPAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `logData.IdentityName` and `logData.Username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `logData.HostId` and `logData.ServiceHost` raw log fields with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_deployment_id`: Newly mapped `logData.TenantId` raw log field with `event.idm.read_only_udm.metadata.product_deployment_id` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `logData.AuthenticationMechanism` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.type`: Updated the value of `event.idm.read_only_udm.extensions.auth.type` to MACHINE based on the value of `logData.AuthenticationMechanism` raw log field.  
\- `event.idm.read_only_udm.extensions.auth.mechanism`: Updated the value of `event.idm.read_only_udm.extensions.auth.mechanism` to SERVICE based on the value of `logData.AuthenticationMechanism` raw log field.  
\- `event.idm.read_only_udm.target.ip`,`event.idm.read_only_udm.target.asset.ip`: Newly mapped `logData.HttpRequestHost` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.hostname`,`event.idm.read_only_udm.target.asset.hostname`: Newly mapped `logData.HttpRequestHost` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `logData.HttpRemotePort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `logData.Command` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `logData.HttpRequestMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `logData.ResponseCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `logData.Status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `logData.PersistentSessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `logData.ActivityId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `logData.HttpRequestProtocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `logData.HttpRequestProtocol` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `logData.UserAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `logData.UserAgent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `logData.Referrer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `logData.Application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `logData.UriStem` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `logData.CUID` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped unhandled keys from `logData` map raw log field with `event.idm.read_only_udm.additional.fields` UDM field, with keys prefixed by `logData_`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped fields `AadExecutionCount`, `AadExecutionTime`, `AadGraphExecutionCount`, `AadGraphExecutionTime`, `AadTokenExecutionCount`, `AadTokenExecutionTime`, `ActivityStatus`, `AfdRefInfo`, `AnonymousIdentifier`, `ApplicationHash`, `Area`, `AuthorizationId`, `BlobStorageExecutionCount`, `BlobStorageExecutionTime`, `CPUCycles`, `CPUExecutionTime`, `CPUTime`, `CommandHash`, `CommandIdentifier`, `ConcurrencySemaphoreTime`, `ContextId`, `ControllerTime`, `CurrentAuthenticationSessionId`, `DelayTime`, `E2EID`, `ElapsedTime`, `ExceptionMessage`, `ExceptionType`, `ExecutionTime`, `ExecutionTimeThreshold`, `Feature`, `FinalSqlCommandExecutionTime`, `HostStartTime`, `HostType`, `HttpRequestTransferEncoding`, `HttpResponseArrProxyTarget`, `HttpResponseCacheControl`, `HttpResponseContentEncoding`, `HttpUriQuery`, `IsExceptionExpected`, `Layer`, `LogicalReads`, `Message`, `MethodInformationTimeout`, `OrchestrationId`, `ParentHostId`, `Path`, `PendingAuthenticationSessionId`, `PhysicalReads`, `PostControllerTime`, `PreControllerTime`, `PreciseTimeStamp`, `ProcessName`, `ProviderId`, `QueueTime`, `RedisExecutionCount`, `RedisExecutionTime`, `RelatedActivityId`, `Service`, `ServiceBusExecutionCount`, `ServiceBusExecutionTime`, `SqlExecutionCount`, `SqlExecutionTime`, `SqlReadOnlyExecutionCount`, `SqlReadOnlyExecutionTime`, `SqlRetryExecutionCount`, `SqlRetryExecutionTime`, `StartTime`, `SupportsPublicAccess`, `TSTUs`, `TableStorageExecutionCount`, `TableStorageExecutionTime`, `ThrottleReason`, `TimeToFirstPage`, `TraceId`, `Tracepoint`, `UniqueIdentifier`, `Uri`, `UserDefined`, `VSID`, `VssClientExecutionCount`, `VssClientExecutionTime` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-11-24 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page : https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/github   
2025-09-22 |  Enhancement:  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `invitation.email` raw log field(s) with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `invitation.created_at` raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `invitation.id` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `invitation.invitation_teams_url` raw log field(s) with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.target.user.attribute.roles: Newly mapped `invitation.role` raw log field(s) with `event.idm.read_only_udm.target.user.attribute.roles` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `invitation.inviter.id` raw log field(s) with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `invitation.inviter.login` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `invitation.inviter.html_url` raw log field(s) with `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `invitation.login` raw log field(s) with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `invitation.inviter.url`, `invitation.inviter.avatar_url`, `invitation.inviter.type` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `organization.url`, `invitation.invitation_source`, `invitation.team_count`, `invitation.node_id`, `invitation.failed_at`, `invitation.failed_reason`, `invitation.inviter.url`, `invitation.inviter.avatar_url`, `invitation.inviter.type`, `invitation.inviter.events_url`, `invitation.inviter.followers_url`, `invitation.inviter.following_url`, `invitation.inviter.gists_url`, `invitation.inviter.gravatar_id`, `invitation.inviter.node_id`, `invitation.inviter.organizations_url`, `invitation.inviter.received_events_url`, `invitation.inviter.repos_url`, `invitation.inviter.site_admin`, `invitation.inviter.starred_url`, `invitation.inviter.subscriptions_url`, `invitation.inviter.user_view_type` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-09-05 |  Enhancement:  
\- Added new grok patterns for the `message` and `content` fields to parse additional log formats.  
\- Added a gsub mutation to replace `=>` with `=` in the `kv_data` field before Key-Value processing to ensure correct parsing.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` : Newly mapped `job_type` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `metric` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Refactored the mapping of the `job_name`, `catalog_service` data field: The previous unconditional merge of `job_name`, `catalog_service` data field was removed and replaced with the conditional block described under `Dynamic Field Addition`, now including error handling.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `column7`, `column8` data fields to `event.idm.read_only_udm.additional.fields` UDM field when `process_type` data field is equal to `github_access` or `alambic_assets` or `alambic_avatars` values.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `gc_duration`, `db_cached_queries`, `db_queries`, `activerecord_duration`, `views_duration` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-09-02 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `membership.user.login` raw log field to `event.idm.read_only_udm.target.user.user_display_name`.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `membership.user.id` raw log field to `event.idm.read_only_udm.target.user.product_object_id`.  
\- `event.idm.read_only_udm.target.user.title`: Newly mapped `membership.user.type` raw log field to `event.idm.read_only_udm.target.user.title`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `membership.url`, `membership.state`, `membership.role`, `membership.organization_url`, `membership.user.node_id`, `membership.user.html_url`, `membership.user.site_admin`, `membership.user.avatar_url`, `membership.user.url`, `membership.user.followers_url`, `membership.user.following_url`, `membership.user.gists_url`, `membership.user.starred_url`, `membership.user.subscriptions_url`, `membership.user.organizations_url`, `membership.user.repos_url`, `membership.user.events_url`, `membership.user.received_events_url`, `membership.user.user_view_type` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Updated condition for adding repo label: value is added only if repo is not in ["`, `nil"].  
\- Updated condition for adding device_cookie label: value is added only if device_cookie is not in ["`, `nil"].  
\- Updated condition for mapping hashed_token: Mapped only if hashed_token is not in ["`, `nil"].  
\- Updated condition for mapping user_session_id: Mapped only if user_session_id is not in ["`, `nil"].  
\- Removed gsub transformation on the `message` field, so literal `nil` strings will no longer be replaced with empty strings during preprocessing.   
2025-07-23 |  Enhancement:  
\- event.idm.read_only_udm.security_result.rule_labels: Newly Mapped `check_run.check_suite.app.permissions`,check_run.app.permissions`,`check_suite.app.permissions`,`comment.performed_via_github_app.permissions` raw log fields with `event.idm.read_only_udm.security_result.rule_labels" UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `check_run.check_suite.app.owner`,check_run.head_sha`,`check_run.check_suite.head_sha` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels" UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly Mapped `issue.user`,`comment.user` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `check_run.status`,`check_run.check_suite.status`,`check_run.check_suite.head_branch` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly Mapped `check_run.html_url`, `check_run.details_url`,`check_run.url` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `check_run.id`,`check_run.name`,`check_run.node_id`,`check_run.external_id`,`check_run.check_suite.node_id`,`check_run.check_suite.before`,`check_run.check_suite.after` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-27 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Added support to parse unparsed `alert` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-22 |  Enhancement:  
\- event.idm.read_only_udm.metadata.description: Newly Mapped `commit_message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly Mapped `commit` value if message contains `committer` with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.src.user.title : Newly Mapped `sender.type` raw log field with `event.idm.read_only_udm.src.user.title` UDM field.  
\- event.idm.read_only_udm.target.file.sha1: Newly Mapped `sha` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field.  
\- event.idm.read_only_udm.target.url: Newly Mapped `target_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly Mapped `description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `avatar_url` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `context` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `commit_node_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `commit_committer_name` raw log field with `event.id.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `state` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `commit_committer_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.email: Newly Mapped `commit_committer_email` raw log field with `event.idm.read_only_udm.principal.email` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `commit_tree_sha` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `comment_count` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `html_url` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly Mapped `reason` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly Mapped `commit_url` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `comments_url` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly Mapped `commit_user_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped `commit_user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.asset_id: Newly Mapped `principal.assetid` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- event.idm.read_only_udm.src.user.user_display_name: Newly Mapped `sender_login` raw log field with `event.idm.read_only_udm.src.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.src.user.product_object_id: Newly Mapped `sender_id` raw log field with `event.idm.read_only_udm.src.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.src.asset_id : Newly Mapped `sender_assetid` raw log field with `event.idm.read_only_udm.src.asset_id` UDM field.  
\- event.idm.read_only_udm.src.url: Newly Mapped `sender_url` raw log field with `event.idm.read_only_udm.src.url` UDM field.   
2025-05-16 |  Enhancement: Fixed flakiness issue caused by repetition of keys in additional fields by appending an index to each key and modifying redundant variable names.   
2025-05-02 |  Enhancement:  
\- event.idm.read_only_udm.target.url: Newly mapped `alert.url` raw log filed with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `alert.created_at`, `alert.html_url`, `alert.locations_url`, `alert.multi_repo`, `alert.number`, `alert.publicly_leaked`, `alert.push_protection_bypassed`, `alert.secret_type`, `alert.secret_type_display_name`, `alert.updated_at`, `alert.validity` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-02-27 |  Enhancement:  
\- Mapped `repository_selection`, `user_programmatic_access_name`, and `permissions_added.*` to `additional.fields`.   
2025-02-20 |  Enhancement:  
\- If `external_identity_nameid` is present, then mapped `external_identity_nameid` to `principal.user.userid`.Otherwise, mapped `actor_id` to `principal.user.userid`.   
2025-02-12 |  Enhancement:  
\- Mapped `new_repo_permission`, `user`, and `actor` to `additional.fields`.   
2025-02-11 |  Enhancement:  
\- Mapped `secret_type_display_name` to `additional.fields`.  
\- Changed `metadata.vendor_name` mapping from `GITHUB` to `GitHub`.   
2025-01-24 |  Enhancement:  
\- Added support for new pattern of JSON logs.   
2024-12-16 |  Enhancement:  
\- Changed mapping of `user` from `principal.user.user_display_name` to `target.user.user_display_name`.  
\- Changed mapping of `actor` from `principal.user.userid` to `principal.user.user_display_name`.  
\- Changed mapping of `actor_id` from `target.user.userid` to `principal.user.userid`.  
\- Mapped `user_id` to `target.user.userid`.  
\- Removed the Grok pattern of `external_identity_nameid` as it is not required.   
2024-12-05 |  Enhancement:  
\- Mapped `push_protection_bypass_reason` to `security_result.detection_fields`.   
2024-11-14 |  Enhancement:  
\- Added support for new pattern of JSON logs.   
2024-11-06 |  Enhancement:  
\- Mapped `actor` to `principal.resource.attribute.labels`.  
\- Changed the mapping of `user` from `target.user.user_display_name` to `principal.user.user_display_name`.  
\- Changed the mapping of `external_identity_nameid` from `target.user.email_addresses` to `principal.user.email_addresses`.  
\- Changed the mapping of `userid` from `target.user.userid` to `principal.user.userid`.   
2024-09-18 |  Enhancement:  
\- Mapped `pull_request_url` to `target.url`.  
\- Mapped `pull_request_title`, `pull_request_id` ,and `previous_visibility` to `additional.fields`.   
2024-08-26 |  Enhancement:  
\- Mapped `explanation` to `additional.fields`.   
2024-08-13 |  Enhancement:  
\- Mapped `invitee_email` and `email` to `additional.fields`.   
2024-07-02 |  Enhancement:  
\- Fixed the mapping of `config_was`.  
\- Changed the mapping of `admin_enforced` from `security_result.action` to `additional.fields`.  
\- Mapped `required_status_checks_enforcement_level`, `events_were` and `old_permission` to `additional.fields`.   
2024-06-13 |  Enhancement:  
\- Mapped `name`, `manager`, `pull_request_reviews_enforcement_level`, `hook_id`, `events`, `config_was`, `key`, `fingerprint`, `permission`, and `title` to `additional.fields`.  
\- When `admin_enforced` is `true`, then mapped `security_result.action` to `ALLOW`.  
\- When `admin_enforced` is `false`, then mapped `security_result.action` to `BLOCK`.   
2023-12-18 |  Bug-Fix:  
\- If `process_type` is `github_production`, added a Grok pattern to extract `kv_data`.  
\- If `process_type` is `github_production`, mapped `user` to `target.user.user_display_name`.  
\- If `process_type` is `github_production`, mapped `user_id` to `target.user.userid`.  
\- Mapped `referrer` to `network.http.referral_url`.  
\- Mapped `user_session_id` to `network.session_id`.  
\- Mapped `ip` to `principal.ip`.  
\- Mapped `from` to `additional.fields`.  
\- Mapped `request_category` to `additional.fields`.  
\- Mapped `device_cookie` to `additional.fields`.  
\- Mapped `operation_type` to `additional.fields`.  
\- Mapped `category_type` to `additional.fields`.  
\- Mapped `note` to `additional.fields`.  
\- Mapped `read` to `additional.fields`.  
\- Mapped `pre_perform_allocation_count` to `additional.fields`.  
\- Mapped `backend` to `additional.fields`.  
\- Mapped `queue` to `additional.fields`.  
\- Mapped `class` to `additional.fields`.  
\- Mapped `success` to `additional.fields`.  
\- Mapped `controller_action` to `security_result.detection_fields`.  
\- Mapped `two_factor` to `security_result.detection_fields`.   
2023-10-25 |  Enhancement:  
\- When `public_repo` is `false`, set `target.location.name` to `PRIVATE`, else set to `PUBLIC`.   
2023-10-11 |  Enhancement:  
\- Mapped `user_agent` to `network.http.user_agent` and `network.http.parsed_user_agent`.  
\- Mapped `request_method` to `network.http.method`.  
\- Mapped `application_name` to `target.application`.  
\- Mapped `status_code` to `network.http.response_code`.  
\- Mapped `url_path` to `target.url`.  
\- Mapped `user_id` to `target.userid`.  
\- Mapped `transport_protocol_name` to `network.application_protocol`.  
\- Mapped `raw.now` to `metadata.event_timestamp`.  
\- Mapped `raw.ip` to `principal.ip`.  
\- Mapped `raw.request_id` to `metadata.product_log_id`.  
\- Mapped `raw.repo` to `target.url`.  
\- Mapped `raw.action` to `security_result.summary`.  
\- Mapped `raw.protocol` to `network.application_protocol`.  
\- Mapped `raw.message` to `metadata.description`.  
\- Mapped `raw.at` to `security_result.action`.  
\- Mapped `raw.login` to `target.user_display_name`.  
\- Mapped `raw.user_id` to `target.userid`.  
\- Mapped `raw.failure_reason`, `raw.failure_type`, `raw.raw_login` and `raw.from` to `additional.fields`.  
\- Mapped `programmatic_access_type`, `actor_id`, `token_id`, `token_scopes`, `integration`, `query_string`, `rate_limit_remaining`,  
`request_body`, `route`, `business`, `org_id`, `repo_id`, `public_repo`, `_document_id`, `operation_type`, `repository_public` to `additional.fields`.   
2023-07-31 |  Bug-Fix -  
\- Added `on_error` to Grok patterns.  
\- Mapped `workflow_run.id` to `target.resource.attribute.labels`.  
\- Mapped `workflow_run.event` to `additional.fields`.  
\- Mapped `workflow_run.actor.login` to `principal.user.userid`.  
\- Mapped `workflow_run.head_branch` to `security_result.about.labels`.  
\- Mapped `workflow_run.head_sha` to `target.file.sha256`.  
\- Mapped `enterprise.name` to `additional.fields`.  
\- Mapped `workflow.name` to `security_result.about.labels`.  
\- Mapped `workflow_run.workflow_id` to `security_result.about.labels`.   
2023-06-22 |  Enhancement-  
\- Added support for the `github_auth`, `haproxy`, `github_access`, `github_unicorn`, `github_production`, `hookshot-go`,  
`babeld`, `github_gitauth`, `babeld2hydro`, `authzd`, `gitrpcd`, `agent`, `git-daemon`,  
`github_resqued`, `sudo`, `systemd` and `github_audit` syslog log formats.   
2023-06-09 |  Enhancement-  
\- Mapped `external_identity_nameid` to `target.user.email_addresses` if in email format.  
\- Fetch the username from `external_identity_nameid` and map to `target.user.userid`.   
2023-01-13 |  Enhancement-  
\- Mapped `actor_ip` to` `principal.ip".  
\- Mapeed `hashed_token` to `network.session_id`.  
\- Mapped `external_identity_nameid` to `target.user.userid `  
\- Mapped `external_identity_username` to target.user.user_display_name".   
2022-11-28 |  Enhancement - Mapped `config.url` to `target.url`.   
2022-07-07 |  Enhancement - The newly ingested JSON format logs having action `git.clone`,`git.push` and `workflows.prepared_workflow_job` have been handled and parsed.  
\- `job_name` mapped to `target.resource.attribute.labels`.  
\- `job_workflow_ref` mapped to `target.resource.attribute.labels`.  
\- `runner_group_id` mapped to `target.resource.attribute.labels`.  
\- `runner_group_name` mapped to `target.resource.attribute.labels`.  
\- `runner_name` mapped to `target.resource.attribute.labels`.  
\- `runner_id` mapped to `target.resource.attribute.labels`.  
\- `workflow_run_id` mapped to `target.resource.attribute.labels`.  
\- `actor_location.country_code` mapped to `principal.location.country_or_region`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
