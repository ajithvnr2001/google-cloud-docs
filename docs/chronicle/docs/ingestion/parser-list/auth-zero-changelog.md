---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/auth-zero-changelog/
title: Change log for AUTH_ZERO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:34:23.091453+00:00
---

# Change log for AUTH_ZERO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/auth-zero-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AUTH_ZERO

Date | Changes  
---|---  
2026-04-22 |  Enhancement:  
\- Added gsub to remove malformed character from `user_agent` and `detail.js_data.user_agent` fields in order to parse the raw log without error.  
\- Modified the conditional check to avoid parsing null values for `user_agent` and `detail.js_data.user_agent` fields.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` from `USER_LOGOUT` to `NETWORK_CONNECTION` for `slo` events if they do not contain any user details.   
2026-03-23 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `record.js_data.details.identifier.value` log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `record.js_data.details.identifier.type`, `record.js_data.details.session.cookie.mode`, `record.js_data.security_context.ja4` log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.ja3`: Newly mapped `record.js_data.security_context.ja3` log field with `event.idm.read_only_udm.network.tls.client.ja3` UDM field.  
\- Added a grok pattern on `user_name` to extract appropriate value of `user_name`.   
2026-01-13 |  Enhancement:  
\- event.idm.read_only_udm.target.asset.product_object_id: Newly mapped `record.detail.js_data.details.response.body.client_id` raw log field(s) with `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `record.detail.js_data.details.response.body.name` raw log field(s) with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record.detail.js_data.details.response.body.app_type` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field with key `app_type`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record.detail.js_data.details.response.body.grant_types` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field with key `body_grant_types`.  
\- event.idm.read_only_udm.additional.fields: Changed mapping for `event.idm.read_only_udm.additional.fields` with key `cookie_mode` from `record.js_data.details.session.cookie.mode` to `record.detail.js_data.details.session.cookie.mode`.   
2025-12-17 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `detail.js_data.details.prompts.user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `detail.js_data.details.prompts.user_name` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.user.phone_numbers: Newly mapped `detail.js_data.details.prompts.user_name` raw log field with `event.idm.read_only_udm.principal.user.phone_numbers` UDM field.  
\- event.idm.read_only_udm.extensions.auth.mechanism: Newly mapped `detail.js_data.connection` raw log field with `event.idm.read_only_udm.extensions.auth.mechanism` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `detail.js_data.connection_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `detail.js_data.client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.group.product_object_id: Newly mapped `detail.js_data.organization_id` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.group.group_display_name: Newly mapped `detail.js_data.organization_name` raw log field with `event.idm.read_only_udm.principal.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `detail.js_data.audience` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.network.tls.client.ja3: Newly mapped `detail.js_data.security_context.ja3` raw log field with `event.idm.read_only_udm.network.tls.client.ja3` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.js_data.details.prompts.name` (Key: `NAME`), `detail.js_data.details.prompts.initiatedAt` (Key: `INITIATED AT`), `detail.js_data.details.prompts.completedAt` (Key: `COMPLETED AT`), `detail.js_data.details.prompts.identity` (Key: `IDENTITY`), `detail.js_data.details.prompts.elapsedTime` (Key: `ELAPSED TIME`), `detail.js_data.details.prompts.flow` (Key: `PROMPT_FLOW`), `detail.js_data.details.prompts.stats.loginsCount` (Key: `PROMPT_LOGIN_COUNT`), `detail.js_data.details.prompts.timers.rules` (Key: `PROMPT_RULES`), `detail.js_data.connection` (Key: `connection`), `detail.js_data.details.requested_scope` (Key: `requested_scope`), `detail.js_data.details.actions.executions` (Key: `executions`), `detail.js_data.auth0_client.env.python` (Key: `auth0_client_env_python`), `detail.js_data.security_context.ja4` (Key: `ja4`), `detail.js_data.details.elapsedTime` (Key: `elapsedTime`), `detail.js_data.details.stats.loginsCount` (Key: `loginsCount_record`), `detail.js_data.details.session.cookie.mode` (Key: `session_cookie_mode`), `detail.js_data.session_connection` (Key: `session_connection`), `detail.js_data.details.request.auth.user` (Key: `auth_user`), `detail.js_data.details.request.auth.credentials` (Key: `auth_credentials`), `detail.js_data.details.accessedSecrets` (Key: `AccessedSecrets`), `record.detail.js_data.auth0_client.env.node` (Key: `auth0_client_node`), `detail.js_data.details.requested_scope` (Key: `requested_scope`) raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `detail.js_data.details.prompts.connection_id` (Key: `PROMPT_CONNECTION_ID`), `detail.js_data.details.prompts.connection` (Key: `PROMPT_CONNECTION`), `detail.js_data.details.prompts.strategy` (Key: `PROMPT_STRATEGY`), `detail.js_data.scope` (Key: `scope`), `detail.js_data.strategy` (Key: `STRATEGY_RECORD`), `detail.js_data.strategy_type` (Key: `STRATEGY_TYPE_RECORD`), `detail.js_data.details.response.body.id` (Key: `body_id`), `detail.js_data.details.request.body.name` (Key: `body_req_name`), `detail.js_data.details.request.body.description` (Key: `body_req_description`), `detail.js_data.details.request.body.app_type` (Key: `body_req_app_type`), `detail.js_data.details.description` (Key: `body_details_description`) raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-10-18 |  Enhancement:  
\- event.idm.read_only_udm.target.asset.product_object_id: Newly mapped `detail.js_data.details.response.body.client_id` raw log field to `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `detail.js_data.details.response.body.name` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `detail.js_data.details.response.body.app_type`, `detail.js_data.details.response.body.description`, `detail.js_data.details.response.body.is_first_party`, `detail.js_data.details.response.body.oidc_conformant`, `detail.js_data.details.response.body.jwt_configuration.lifetime_in_seconds`, `detail.js_data.details.response.body.cross_origin_authentication`, `detail.js_data.auth0_client.env.Terraform-Provider-Auth0`, `detail.js_data.auth0_client.env.go`, `detail.js_data.details.accessedSecrets`, `detail.js_data.details.response.body.token_endpoint_auth_method`, `detail.js_data.details.response.body.cross_origin_auth`, `detail.js_data.details.response.body.sso_disabled`, `detail.js_data.details.response.body.client_secret`,`detail.js_data.details.response.body.is_token_endpoint_ip_header_trusted`, `detail.js_data.details.response.body.jwt_configuration.secret_encoded`, `detail.js_data.details.response.body.refresh_token` and `detail.js_data.details.response.body.custom_login_page_on` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.js_data.details.response.body.grant_types` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-09-16 |  Enhancement:  
\- Added support for the events f, fu, fp and relevant corresponding raw log fields.  
\- Modified grok patterns to validate IP addresses before mapping.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `js_data.details.error.oauthError`, `js_data.details.error.message`, `js_data.details.error.type`, `record.js_data.details.error.oauthError`, `record.js_data.details.error.message and `record.js_data.details.error.type` raw log field to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `js_data.details.qs.state`, `record.js_data.scope` and `js_data.environment_name` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `js_data.tenant_name` raw log field to event.idm.read_only_udm.target.resource.attribute.labels.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `js_data.$event_schema.version` raw log field to event.idm.read_only_udm.principal.platform_version.   
2025-09-04 |  Enhancement:  
\- Modified event type mapping logic for `slo` and `s` event types to correctly identify USER_LOGOUT and USER_LOGIN events.  
\- event.idm.read_only_udm.principal.application: Newly mapped record.js_data.auth0_client.name raw log field to event.idm.read_only_udm.principal.application.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped record.js_data.details.code raw log field to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped record.js_data.auth0_client.env.java, record.js_data.details.allowed_logout_url, and record.js_data.environment_name raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.extensions.auth.mechanism: Newly mapped record.js_data.connection raw log field to event.idm.read_only_udm.extensions.auth.mechanism.  
\- event.idm.read_only_udm.target.url: Newly mapped record.js_data.details.return_to raw log field to event.idm.read_only_udm.target.url.   
2025-08-28 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record.detail.js_data.session_connection` , `record.detail.js_data.environment_name`, `record.detail.js_data.details.endCount`, `record.detail.js_data.details.removedCount`, `record.detail.js_data.details.resource`, `record.detail.js_data.details.startCount` and `record.detail.js_data.security_context.ja4` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.tls.client.ja3: Newly mapped `record.detail.js_data.security_context.ja3` raw log field with `event.idm.read_only_udm.network.tls.client.ja3` UDM field.  
\- Added drop tag for invalid json logs.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `record.detail.js_data.details.session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record.detail.js_data.strategy_type`, `record.detail.js_data.details.request.channel`, `record.detail.js_data.details.request.auth.strategy` and `record.detail.js_data.details.body.is_signup` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `record.detail.js_data.hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.   
2025-08-14 |  Enhancement:  
\- event.idm.read_only_udm.target.user.userid: Removed mapping of `user_id`, `prompt.user_id`, `js_data.details.response.body.user_id`, and `details.response.body.user_id` from event.idm.read_only_udm.target.user.userid UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user_id`, `prompt.user_id`, `js_data.details.response.body.user_id`, and `details.response.body.user_id` raw log field to event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Removed mapping of `user_name` and `prompt.user_name` from event.idm.read_only_udm.target.user.email_addresses UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.principal.user.email_addresses and event.idm.read_only_udm.principal.user.phone_numbers: Newly mapped `user_name` or `prompt.user_name` if raw log field contains a valid email address then map to event.idm.read_only_udm.principal.user.email_addresses UDM field else map to event.idm.read_only_udm.principal.user.phone_numbers UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `record.detail.js_data.details.request.method` raw log field to event.idm.read_only_udm.network.http.method UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `record.detail.js_data.details.request.path` raw log field to event.idm.read_only_udm.network.http.referral_url UDM field.  
\- event.idm.read_only_udm.target.user.attribute.roles: Newly mapped `record.detail.js_data.details.request.body.roles` raw log field to event.idm.read_only_udm.target.user.attribute.roles UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `record.detail.js_data.details.response.statusCode` raw log field to event.idm.read_only_udm.network.http.response_code UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record.detail.js_data.details.stats.loginsCount` and `record.detail.js_data.details.requested_scope` raw log fields to event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Modified conditions for setting USER_LOGIN and USER_LOGOUT. These event types are now set based on the `has_target_user` flag instead of the `has_user` flag.  
\- event.idm.read_only_udm.metadata.event_type: Changing USER_LOGIN and USER_LOGOUT to USER_UNCATEGORIZED due to the user details mapping shifting from target to principal.  
\- event.idm.read_only_udm.metadata.event_type: Modified conditions for setting USER_UNCATEGORIZED. The event type is now set if `has_user` is true, removing the previous additional requirement for `has_principal` to also be true.   
2025-07-08 |  Enhancement:  
\- event.idm.read_only_udm.target.user.userid: Removed mapping of `detail.js_data.user_id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field in order to introduce a more accurate mapping for the raw log field..  
\- event.idm.read_only_udm.principal.user.userid: Mapped `detail.js_data.user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.phone_numbers: Newly Mapped `detail.js_data.user_name` raw log field with `event.idm.read_only_udm.principal.user.phone_numbers` UDM field when it is not a valid email address.  
\- event.idm.read_only_udm.target.user.email_addresses: Removed mapping of `detail.js_data.user_name` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field in order to introduce a more accurate mapping for the raw log field..  
\- event.idm.read_only_udm.principal.user.email_addresses: Mapped `detail.js_data.user_name` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.js_data.environment_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-12 |  Enhancement:  
\- Added a gsub to replace `}{` with `},{` in message field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `record_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.id: Newly mapped `record_id` raw log field with `event.idm.read_only_udm.metadata.id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record_detail_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.file.full_path: Newly mapped `record_source` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record_account` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `record_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `record_region` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `record_detail_log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `connection_` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- Replaced `record.detail.js_data.auth0_client.name` raw log field with `auth0_client_name`.  
\- Replaced `record.detail.js_data.auth0_client.version` raw log field with `auth0_client_version`.  
\- Replaced `record.detail.js_data.auth0_client.env.python` raw log field with `auth0_client_env_python`.  
\- Replaced `record.detail.js_data.audience` raw log field with `js_data_audience`.  
\- Replaced `record.detail.js_data.scope` raw log field with `js_data_scope`.  
\- Replaced `record.detail.js_data.tenant_name` raw log field with `js_data_tenant_name`.  
\- Replaced `record.detail.js_data.date` raw log field with `date`.  
\- Replaced `record.detail.js_data.type` raw log field with `type`.  
\- Replaced `record.detail.js_data.description` raw log field with `description`.  
\- Replaced `record.detail.js_data.connection_id` raw log field with `connection_id`.  
\- Replaced `record.detail.js_data.client_id` raw log field with `client_id`.  
\- Replaced `record.detail.js_data.client_name` raw log field with `client_name`.  
\- Replaced `record.detail.js_data.ip` raw log field with `ip`.  
\- Replaced `record.detail.js_data.client_ip` raw log field with `js_data_client_ip`.  
\- Replaced `record.detail.js_data.user_agent` raw log field with `user_agent`.  
\- Replaced `record.detail.js_data.user_id` raw log field with `user_id`.  
\- Replaced `record.detail.js_data.user_name` raw log field with `user_name`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `js_data_audience` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `js_data_scope` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `auth0_client_env_python` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `js_data_tenant_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `auth0_client_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `auth0_client_version` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `js_data_client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Added `has_principal` flag for `js_data_client_ip`, `ip` raw log fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `execution` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `record.detail.js_data.$event_schema.version` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- Removed `has_principal` flag where `event.idm.read_only_udm.metadata.event_type` is `USER_UNCATEGORIZED`.   
2025-04-24 |  Enhancement:  
\- Added support for the new pattern of JSON logs.   
2025-04-21 |  Enhancement:  
\- When `event.idm.read_only_udm.metadata.product_event_type = `s` then set the `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN".  
\- When `event.idm.read_only_udm.metadata.product_event_type = `s` then set the `event.idm.read_only_udm.extensions.auth.type` to `MACHINE".   
2025-01-12 |  Enhancement:  
\- Added support for a new log array pattern.   
2024-11-21 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-10-10 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-09-12 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-06-25 |  Bug-Fix:  
\- Mapped `data.scope` to `additional.fields`.   
2024-03-07 |  Bug-Fix:  
\- Mapped `data.user_name` to `target.user.email_addresses`.  
\- Mapped `data.details.body.email_verified`, `data.details.body.is_signup` to `security_result.detection_fields`.  
\- Mapped `data.details.body.transaction.redirect_uri` to `target.url`.   
2023-06-19 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
