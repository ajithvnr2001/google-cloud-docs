---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/github-dependabot-changelog/
title: Change log for GITHUB_DEPENDABOT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:13:28.000091+00:00
---

# Change log for GITHUB_DEPENDABOT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/github-dependabot-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GITHUB_DEPENDABOT

Date | Changes  
---|---  
2025-12-17 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped key-value pairs from `request_body` raw log field except for key `description` with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `request_body.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `external_identity_nameid` raw log field(s) with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `created_at` raw log field(s) with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `application_name` raw log field(s) with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `action` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.ip`,`event.idm.read_only_udm.principal.asset.ip`: Newly mapped `actor_ip` raw log field(s) with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `user_id`,`user` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field if `actor_id` is mapped to `event.idm.read_only_udm.principal.user.userid` UDM field and `actor` is mapped to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
-`event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field if `actor_id` is null.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `user` raw log field(s) with `event.idm.read_only_udm.principal.user.user_display_name` UDM field if `actor` is null.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `actor_location.country_code` raw log field(s) with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `operation_type` raw log field(s) with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `org` raw log field(s) with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- Added a gsub to replace `\`repository\`:\` with \`repository_field\`:\`` and `\`repository\`: \` with \`repository_field\`:\`` in message.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `route`, `repository_public` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `request_method` raw log field(s) with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `status_code` raw log field(s) with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url_path` raw log field(s) with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `transport_protocol_name` raw log field(s) with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`,`event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `user_agent` raw log field(s) with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_document_id`, `actor_is_agent`, `actor_is_bot`, `business`, `business_id`, `hashed_token`, `integration`, `org_id`, `programmatic_access_type`, `public_repo`, `rate_limit_remaining`, `request_id`, `repository_public`, `token_id`, `transport_protocol`, `repository.isArchived`, `repository.isDisabled`, `repository.diskUsage`, `repository.forkCount`, `repository.visibility`, `token_scopes`, `oauth_application_id` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `actor_is_agent`, `actor_is_bot` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `request_access_security_header` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
Update Field Mapping:  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `repo` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `repository_field` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field if `repo` is null.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `repository_field` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field if `repo` is mapped to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `repo_id` raw log field(s) with `event.idm.read_only_udm.target.resource.product_object_id` UDM field if `repo_id` is not null else mapped `repository_id` raw log field(s) with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- Use gsub to rename from `@timestamp` to `timestamp`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_user` is `true` and `has_target_resource` is `true`, updated to `USER_RESOURCE_ACCESS`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is `true`, updated to `STATUS_UPDATE`.  
\- Assigned the value of `repository.name` value to `repository_name` variable and used it as conditional check.  
\- Assigned the value of `repository.id` value to `repositoryId` variable and used it as conditional check.   
2025-03-04 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
