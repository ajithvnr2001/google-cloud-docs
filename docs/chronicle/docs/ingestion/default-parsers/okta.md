---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta/
title: Collect Okta logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:41.064248+00:00
---

# Collect Okta logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Okta logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Okta logs to Google Security Operations using the Okta API. The parser extracts system logs, handling both single events and batched events within a JSON array. It normalizes the data into the UDM format, mapping Okta fields to UDM equivalents, enriching the data with parsed user agents, geographical information, and authentication details, and generating security result events based on outcomes and risk information.

## Before you begin

  * **Google SecOps** instance
  * Privileged access to **Okta**



## How to configure Okta

To configure Okta SSO, complete the following tasks:

### Create Okta Administrative user with read-only privileges

  1. Sign in to the Okta administrator console.
  2. Create a Standard User.

     * Go to **Directory > People**.
     * Click **Add person** and complete the required fields.
**Note:** If you already have an existing standard user who you want to make a read-only administrator, proceed to the next step.
  3. Select **Security > Administrators**.

  4. Click **Add Administrator**.

  5. In the **Administrator assignment by admin** field, find the Standard User.

  6. In the **roles** section, select **Read-Only Administrator** from the list.

  7. Sign out from the administrator account.




### Get API key

  1. Sign in to the **Okta Administrator Console** with the **read-only administrator** user.
  2. Go to **Security > API > Tokens**.
  3. Click **Create Token**.
  4. Provide a meaningful name for the token.
  5. Provide the IP zone, where the API will be used (you can select **any IP** if you are not sure). 
  6. Click **Create Token**.
  7. Copy the API key.
  8. Click **OK, got it**.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the Okta feed

To configure this log type, follow these steps:

  1. Click the **Okta** pack.
  2. Locate the **Okta** logtype.
  3. Specify values for the following fields:

     * **Source Type** : Third party API (recommended)
     * **Authentication HTTP header** : Enter Okta API Key in the following format: `Authorization:<API_KEY>`.
     * **API Hostname** : Specify the domain name of your Okta host (for example, `<your-domain>.okta.com`).
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : [Namespace associated with the feed](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion Labels** : Labels applied to all events from this feed.
  4. Click **Create Feed**.


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`user_email` | `event.idm.read_-only_udm.network.email.from` | Mapped from changelog  
`debugContext.debugData.zoneData.cidr_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`debugContext.debugData.zoneData.cidr_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`debugContext.debugData.zoneData.range` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`debugContext.debugData.zoneData.CIDR` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`debugContext.debugData.requestId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`debugContext.debugData.targetEventHookIds` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`id` | `event1.idm.read_only_udm.additional.fields` | Mapped from changelog  
`details.type` | `event1.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`details.actor.name` | `event1.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`details.actor.details.full_name` | `event1.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`details.actor.details.first_name` | `event1.idm.read_only_udm.principal.user.first_name` | Mapped from changelog  
`details.actor.details.last_name` | `event1.idm.read_only_udm.principal.user.last_name` | Mapped from changelog  
`details.actor.id` | `event1.idm.read_only_udm.principal.user.employee_id` | Mapped from changelog  
`details.client.hostname` | `event1.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`details.client.hostname` | `event1.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`details.client.id` | `event1.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`details.client.description` | `event1.idm.read_only_udm.principal.application` | Mapped from changelog  
`details.client.os` | `event1.idm.read_only_udm.principal.platform` | Mapped from changelog  
`details.client.os` | `event1.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`details.team_id` | `event1.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`details.team_id` | `event1.idm.read_only_udm.principal.resource.id` | Mapped from changelog  
`details.team_name` | `event1.idm.read_only_udm.additional.fields` | Mapped from changelog  
`details.client.state` | `event1.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`details.target_server` | `event1.idm.read_only_udm.target.application` | Mapped from changelog  
`details.via` | `event1.idm.read_only_udm.network.session_id` | Mapped from changelog  
`details_session_type` | `event1.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`details.actor.details.user_type` | `event1.idm.read_only_udm.principal.user.attribute.roles` | Mapped from changelog  
`details.trace_id` | `event1.idm.read_only_udm.network.session_id` | Mapped from changelog  
`details.client.encrypted` | `event1.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`details.client.user_name` | `event1.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`details.client_ip` | `event1.idm.read_only_udm.principal.ip` | Mapped from changelog  
`details.client_ip` | `event1.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`details.project.id` | `event1.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`details.project.team` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.project.create_server_users` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.project.force_shared_ssh_users` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.project.forward_traffic` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.project.rdp_session_recording` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.project.require_preauth_for_creds` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.project.ssh_certificate_type` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.project.ssh_session_recording` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.project.next_unix_gid` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.project.next_unix_uid` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.server_hostnames` | `event1.idm.read_only_udm.target.hostname` | Mapped from changelog  
`details.server_hostnames` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`server_cloud_provider` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`server_instance_type` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`server_instance_id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`server_network` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`server_project_id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`server_zone_id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`detailsserver_os` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`server_services` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`server_sftd_version` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`server_source` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.cloud_provider` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.instance_details._type` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.instance_details.instance_id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.instance_details.internal_ip` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.instance_details.network` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.instance_details.project_id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.instance_id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.os` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.source` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.project_name` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.source_details.cloud_account` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.source_details.cloud_provider` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.servers.source_details.instance_id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.cloud_provider` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.instance_details._type` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.instance_details.instance_id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.instance_details.internal_ip` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.instance_details.network` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.instance_details.project_id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.instance_id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.os` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.source` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.project_name` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.source_details.cloud_account` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.source_details.cloud_provider` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`details.server.source_details.instance_id` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`server_source_details` | `event1.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`detailsserver.team_name` | `event1.idm.read_only_udm.intermediary.user.department` | Mapped from changelog  
`details.username` | `event1.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`details.ssh_key_fingerprint` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.unix_user_name` | `event1.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`details.ssh_algorithm` | `event1.idm.read_only_udm.network.tls.cipher` | Mapped from changelog  
`details.servers.alt_names` | `event1.idm.read_only_udm.target.hostname` | Mapped from changelog  
`details.servers.alt_names` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.server.alt_names` | `event1.idm.read_only_udm.target.hostname` | Mapped from changelog  
`details.server.alt_names` | `event1.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`details.servers.access_address` | `event1.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`details.server.access_address` | `event1.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`details.servers.external_ip` | `event1.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`details.server.external_ip` | `event1.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`details.server.sftd_version` | `event1.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`details.servers.sftd_version` | `event1.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`details.server.instance_details.zone_id` | `event1.idm.read_only_udm.intermediary.location.country_or_region` | Mapped from changelog  
`details.servers.instance_details.zone_id` | `event1.idm.read_only_udm.intermediary.location.country_or_region` | Mapped from changelog  
`debugContext.debugData.authType" and "debugContext.debugData.factorType` | `additional.fields` | Mapped from changelog  
`risk.level` | `security_result.severity_details` | Mapped from changelog  
`risk.reasons` | `security_result.description` | Mapped from changelog  
`actor.displayName" and "target.displayName` | `additional.fields` | Mapped from changelog  
`anonymous", "operator", and "type` | `security_result.detection_fields` | Mapped from changelog  
`tunnels" and "policyRuleFactorMode` | `security_result.detection_fields` | Mapped from changelog  
`profile.displayName` | `principal.user.user_display_name` | Mapped from changelog  
`profile.email` | `principal.user.email_addresses` | Mapped from changelog  
`target.0.alternateId` | `target.user.userid` | Mapped from changelog  
`target.1.alternateId` | `target.user.userid` | Mapped from changelog  
`securityContext.asNumber` | `security_result.detection_fields` | Mapped from changelog  
`legacyEventType` | `security_result.detection_fields` | Mapped from changelog  
`target.displayName` | `target.resource_ancestors.name` | Mapped from changelog  
`targetfield.detailEntry.methodTypeUsed` | `target.resource_ancestors.attribute.labels` | Mapped from changelog  
`targetfield.detailEntry.methodUsedVerifiedProperties` | `target.resource_ancestors.attribute.labels` | Mapped from changelog  
`debugContext.debugData.changedAttributes` | `security_result.detection_fields` | Mapped from changelog  
`client.userAgent.os` | `principal.platform` | Mapped from changelog  
`client.device` | `principal.asset.type` | Mapped from changelog  
`target.0.detailEntry.clientAppId` | `target.asset_id` | Mapped from changelog  
Log field | UDM mapping | Remark  
:--- | :--- | :---  
`actor.displayName` | `principal.resource.attribute.labels` |   
`assigned_group[]` | `security_result.detection_fields` |   
`created` | `target.resource.attribute.labels` |   
`credentials.oauthClient.autoKeyRotation` | `security_result.detection_fields` |   
`credentials.oauthClient.pkce_required` | `security_result.detection_fields` |   
`credentials.oauthClient.token_endpoint_auth_method` | `security_result.detection_fields` |   
`credentials.signing.kid` | `security_result.detection_fields` |   
`credentials.userNameTemplate.pushStatus` | `security_result.detection_fields` |   
`credentials.userNameTemplate.template` | `metadata.product_event_type` |   
`credentials.userNameTemplate.type` | `security_result.detection_fields` |   
`id` | `principal.user.userid` |   
`label` | `target.resource.attribute.labels` |   
`lastUpdated` | `target.resource.attribute.labels` |   
`orn` | `target.resource.attribute.labels` |   
`settings.implicitAssignment` | `security_result.detection_fields` |   
`settings.manualProvisioning` | `security_result.detection_fields` |   
`settings.notifications.vpn.network.connection` | `security_result.detection_fields` |   
`settings.notifications.vpn.network.helpUrl` | `security_result.detection_fields` |   
`settings.notifications.vpn.network.message` | `security_result.detection_fields` |   
`settings.oauthClient.application_type` | `security_result.detection_fields` |   
`settings.oauthClient.client_uri` | `security_result.detection_fields` |   
`settings.oauthClient.consent_method` | `security_result.detection_fields` |   
`settings.oauthClient.dpop_bound_access_tokens` | `security_result.detection_fields` |   
`settings.oauthClient.grant_types[]` | `security_result.detection_fields` |   
`settings.oauthClient.idp_initiated_login.mode` | `security_result.detection_fields` |   
`settings.oauthClient.initiate_login_uri` | `security_result.detection_fields` |   
`settings.oauthClient.issuer_mode` | `security_result.detection_fields` |   
`settings.oauthClient.logo_uri` | `security_result.detection_fields` |   
`settings.oauthClient.pkce_required` | `security_result.detection_fields` |   
`settings.oauthClient.redirect_uris[]` | `security_result.detection_fields` |   
`settings.oauthClient.response_types[]` | `security_result.detection_fields` |   
`settings.oauthClient.token_endpoint_auth_method` | `security_result.detection_fields` |   
`settings.oauthClient.wildcard_redirect` | `security_result.detection_fields` |   
`settings.signOn.acsUrl` | `security_result.detection_fields` |   
`settings.signOn.assertionSigned` | `security_result.detection_fields` |   
`settings.signOn.attributeStatements[0].filterType` | `security_result.detection_fields` |   
`settings.signOn.attributeStatements[0].filterValue` | `security_result.detection_fields` |   
`settings.signOn.attributeStatements[0].name` | `security_result.detection_fields` |   
`settings.signOn.attributeStatements[0].namespace` | `security_result.detection_fields` |   
`settings.signOn.attributeStatements[0].type` | `security_result.detection_fields` |   
`settings.signOn.audience` | `security_result.detection_fields` |   
`settings.signOn.authnContextClassRef` | `security_result.detection_fields` |   
`settings.signOn.defaultRelayState` | `security_result.detection_fields` |   
`settings.signOn.destination` | `security_result.detection_fields` |   
`settings.signOn.digestAlgorithm` | `security_result.detection_fields` |   
`settings.signOn.idpIssuer` | `security_result.detection_fields` |   
`settings.signOn.recipient` | `security_result.detection_fields` |   
`settings.signOn.responseSigned` | `security_result.detection_fields` |   
`settings.signOn.signatureAlgorithm` | `security_result.detection_fields` |   
`settings.signOn.subjectNameIdFormat` | `security_result.detection_fields` |   
`settings.signOn.subjectNameIdTemplate` | `security_result.detection_fields` |   
`signOnMode` | `security_result.detection_fields` |   
`status` | `security_result.detection_fields` |   
`visibility.appLinks.oidc_client_link` | `security_result.detection_fields` |   
`visibility.autoSubmitToolbar` | `security_result.detection_fields` |   
`visibility.hide.iOS` | `security_result.detection_fields` |   
`visibility.hide.web` | `security_result.detection_fields` |   
N/A | `metadata.vendor_name` | Set to `Okta`.  
N/A | `metadata.product_name` | Set to `Okta`.  
N/A | `extensions.auth.type` | Set to `SSO`.  
  
## Array mapping table

The following table lists the mapping of Okta array elements to [repeated UDM fields](https://docs.cloud.google.com/chronicle/docs/yara-l/repeated-fields).

Array of logs | Array of events | Remark  
---|---|---  
`actor.alternateId` | `TBD` |   
`actor.displayName` | `principal.user.user_display_name` | When eventType is `application.user_membership.update`, `policy.rule.update`, or `user.authentication.auth_via_radius`.  
`actor.displayName` | `principal.user.user_display_name` | When eventType is _not_ `application.user_membership.update`, `policy.rule.update`, or `user.authentication.auth_via_radius`.  
`actor.type` | `principal.user.attribute.roles.name` | When eventType is `application.user_membership.update`, `policy.rule.update`, or `user.authentication.auth_via_radius`.  
`actor.type` | `principal.user.attribute.roles.name` | When eventType is _not_ `application.user_membership.update`, `policy.rule.update`, or `user.authentication.auth_via_radius`.  
`anonymous` | `security_result.detection_fields` |   
`authenticationContext.externalSessionId` | `network.parent_session_id` |   
`client.device` | `principal.asset.type` | Supports: LINUX, WINDOWS, MAC, IOS, ANDROID, CHROME_OS  
`client.device` | `additional.fields` | Event_type  
`client.geographicalContext.city` | `principal.location.city` |   
`client.geographicalContext.country` | `principal.location.country_or_region` |   
`client.geographicalContext.geolocation.lat` | `principal.location.region_latitude` |   
`client.geographicalContext.geolocation.lon` | `principal.location.region_longitude` |   
`client.geographicalContext.postalCode` | `additional.fields` |   
`client.geographicalContext.postalCode` | `target.resource.attribute.labels` |   
`client.ipAddress` | `principal.ip` |   
`client.userAgent` | `network.http.user_agent`  
`network.http.parsed_user_agent` |   
`client.userAgent.browser` | `target.resource.attribute.labels` |   
`client.userAgent.os` | `principal.platform` |   
`client.userAgent.os` | `principal.platform` |   
`client.userAgent.rawUserAgent` | `network.http.user_agent`  
`network.http.parsed_user_agent` |   
`client.zone` | `additional.fields` | Event_type  
`debugContext.debugData.behaviors.New City` | `security_result.detection_fields` |   
`debugContext.debugData.behaviors.New Country` | `security_result.detection_fields` |   
`debugContext.debugData.behaviors.New Device` | `security_result.detection_fields` |   
`debugContext.debugData.behaviors.New Geo-Location` | `security_result.detection_fields` |   
`debugContext.debugData.behaviors.New IP` | `security_result.detection_fields` |   
`debugContext.debugData.behaviors.New State` | `security_result.detection_fields` |   
`debugContext.debugData.behaviors.Velocity` | `security_result.detection_fields` |   
`debugContext.debugData.clientAddress` | `principal.ip`  
`principal.asset.ip` |   
`debugContext.debugData.dtHash` | `security_result.detection_fields` |   
`debugContext.debugData.factor` | `security_result.detection_fields` |   
`debugContext.debugData.factorIntent` | `security_result.detection_fields` |   
`debugContext.debugData.logOnlySecurityData.behaviors` | `security_result.description` |   
`debugContext.debugData.logOnlySecurityData.behaviors.New City` | `security_result.detection_fields` |   
`debugContext.debugData.logOnlySecurityData.behaviors.New Country` | `security_result.detection_fields` |   
`debugContext.debugData.logOnlySecurityData.behaviors.New Device` | `security_result.detection_fields` |   
`debugContext.debugData.logOnlySecurityData.behaviors.New Geo-Location` | `security_result.detection_fields` |   
`debugContext.debugData.logOnlySecurityData.behaviors.New IP` | `security_result.detection_fields` |   
`debugContext.debugData.logOnlySecurityData.behaviors.New State` | `security_result.detection_fields` |   
`debugContext.debugData.logOnlySecurityData.behaviors.Velocity` | `security_result.detection_fields` |   
`debugContext.debugData.logOnlySecurityData.risk.reasons` | `security_result.detection_fields` |   
`debugContext.debugData.logOnlySecurityData.risk.reasons` | `security_result.description` |   
`debugContext.debugData.logOnlySecurityData.risk.level` | `security_result.severity_details` |   
`debugContext.debugData.logOnlySecurityData.url` | `target.url` |   
`debugContext.debugData.privilegeGranted[]` | `target.user.attribute.roles.name`  
`target.user.attribute.roles.description` |   
`debugContext.debugData.pushOnlyResponseType` | `security_result.detection_fields` |   
`debugContext.debugData.pushWithNumberChallengeResponseType` | `security_result.detection_fields` |   
`debugContext.debugData.requestUri` | `extensions.auth.auth_details` |   
`debugContext.debugData.requestUri` | `target.url` |   
`debugContext.debugData.risk` | `security_result.detection_fields` | Mapped reasons to `security_result.detection_fields`.  
`debugContext.debugData.suspiciousActivityEventId` | `security_result.detection_fields` |   
`debugContext.debugData.suspiciousActivityEventType` | `security_result.detection_fields` |   
`debugContext.debugData.threatDetections` | `security_result.detection_fields` |   
`debugContext.debugData.threatSuspected` | `security_result.detection_fields`  
`security_result.threat_status` |   
`debugContext.debugData.threatSuspected` | `security_result.detection_fields`  
`security_result.threat_status` |   
`debugContext.debugData.tunnels[].anonymous` | `security_result.detection_fields` |   
`debugContext.debugData.tunnels[].operator` | `security_result.detection_fields` |   
`debugContext.debugData.tunnels[].type` | `security_result.detection_fields` |   
`debugContext.debugData.tunnels.n.anonymous` | `security_result.detection_fields` |   
`debugContext.debugData.tunnels.n.operator` | `security_result.detection_fields` |   
`debugContext.debugData.tunnels.n.type` | `security_result.detection_fields` |   
`detail.actor.id` | `principal.user.product_object_id` | When eventType is `application.user_membership.update`, `policy.rule.update`, or `user.authentication.auth_via_radius`.  
`detail.actor.id` | `principal.user.product_object_id` | When eventType is _not_ `application.user_membership.update`, `policy.rule.update`, or `user.authentication.auth_via_radius`.  
`detail.authenticationContext.externalSessionId` | `network.parent_session_id` |   
`detail.client.ipChain.0.ip`  
`client.ipAddress` | `principal.ip`  
`principal.asset.ip` |   
`detail.debugContext.debugData.dtHash` | `security_result.detection_fields` |   
`detail.debugContext.debugData.factor` | `security_result.detection_fields` |   
`detail.debugContext.debugData.factorIntent` | `security_result.detection_fields` |   
`detail.debugContext.debugData.pushOnlyResponseType` | `security_result.detection_fields` |   
`detail.debugContext.debugData.pushWithNumberChallengeResponseType` | `security_result.detection_fields` |   
`detail.debugContext.debugData.requestUri` | `target.url` |   
`detail.eventType` | `metadata.product_event_type` |   
`detail.outcome.reason` | `security_result.category_details` |   
`detail.outcome.result` | `security_result.action` |   
`detail.request.ipChain.0.geographicalContext.city` | `principal.location.city` |   
`detail.request.ipChain.0.geographicalContext.country` | `principal.location.country_or_region` |   
`detail.request.ipChain.0.geographicalContext.state` | `principal.location.state` |   
`detail.severity` | `security_result.severity` |   
`detail.target.0.alternateId` | _See the remark._ | `tgtuser_id` => `target.user.userid`  
`%{tgtusername}@%{tgtdomain}` => `target.user.email_addresses`  
`detail.target.0.displayName` | `target.application`  
`target.resource.name` |   
`detail.target.0.displayName` | `target.user.user_display_name` |   
`detail.target.0.detailEntry.policyType}` | `target.resource_ancestors.attribute.labels` |   
`detail.target.0.id` | `target.resource.product_object_id` |   
`detail.target.0.id` | `target.resource_ancestors.product_object_id` |   
`detail.target.0.type` | `target.resource.resource_subtype` |   
`detail.target.0.type` | `target.resource_ancestors.resource_subtype` |   
`detail.uuid` | `metadata.product_log_id` |   
`displayMessage` | `security_result.summary` |   
`extensions.auth.type` | `SSO` | Event_type  
`extensions.auth.type` | `SSO` | When `msg.target.type` is any case other than `AppInstance`, `PolicyEntity`, `PolicyRule`, or `User`.  
`eventType` | `metadata.product_event_type` |   
`eventType`  
`detail.eventType` | `metadata.product_event_type` |   
`json_array.n.actor.id` | `principal.user.product_object_id` |   
`mapped data.fields to fields` |  |   
`metadata.product_name` | `Okta` | Event_type  
`metadata.vendor_name` | `Okta` | Event_type  
`msg.actor.alternateId` | _See the remark._ | If parsing fails, this is mapped to `principal.user.userid` or else maps the username to `principal.user.userid`  
or username@domain to `principal.user.email_addresses`.  
`msg.actor.displayName` | `principal.user.user_display_name` |   
`msg.actor.type` | `principal.user.attribute.roles.name` |   
`msg.authenticationContext.authenticationProvider` | `security_result.detection_fields` | Event_type  
`msg.authenticationContext.credentialProvider` | `security_result.detection_fields` | Event_type  
`msg.authenticationContext.externalSessionId` | `network.parent_session_id` |   
`msg.client.device` | `principal.asset.type` | Supports: MOBILE, WORKSTATION, LAPTOP, IOT, NETWORK_ATTACHED_STORAGE, PRINTER, SCANNER, SERVER, TAPE_LIBRARY  
`msg.client.geographicalContext.city` | `principal.location.city` |   
`msg.client.geographicalContext.country` | `principal.location.country_or_region` |   
`msg.client.geographicalContext.geolocation.lat` | `principal.location.region_latitude` |   
`msg.client.geographicalContext.geolocation.lon` | `principal.location.region_longitude` |   
`msg.client.geographicalContext.postalCode` | `additional.fields` |   
`msg.client.geographicalContext.state` | `principal.location.state` |   
`msg.client.ipAddress` | `principal.ip` |   
`msg.client.userAgent.browser` | `target.resource.attribute.labels` |   
`msg.client.userAgent.os` | `principal.platform` | Supports: LINUX, WINDOWS, MAC, IOS, ANDROID, CHROME_OS  
`msg.client.userAgent.rawUserAgent` | `network.http.user_agent`  
`network.http.parsed_user_agent` |   
`msg.debugContext.debugData.dtHash` | `security_result.detection_fields` |   
`msg.debugContext.debugData.factor` | `security_result.detection_fields` |   
`msg.debugContext.debugData.factorIntent` | `security_result.detection_fields` |   
`msg.debugContext.debugData.logOnlySecurityData.behaviors` | `security_result.description` |   
`msg.debugContext.debugData.logOnlySecurityData.risk.reasons` | `security_result.detection_fields` |   
`msg.debugContext.debugData.logOnlySecurityData.url` | `target.url` |   
`msg.debugContext.debugData.pushOnlyResponseType` | `security_result.detection_fields` |   
`msg.debugContext.debugData.pushWithNumberChallengeResponseType` | `security_result.detection_fields` |   
`msg.debugContext.debugData.requestUri` | `extensions.auth.auth_details` |   
`msg.debugContext.debugData.threatSuspected` | `security_result.detection_fields`  
`security_result.threat_status` |   
`msg.displayMessage` | `security_result.summary` |   
`msg.eventType` | `metadata.product_event_type` |   
`msg.legacyEventType` | `security_result.detection_fields` |   
`msg.outcome.reason` | `security_result.category_details` |   
`msg.outcome.result` | `security_result.action` |   
`msg.published` | `metadata.event_timestamp` |   
`msg.request.ipChain.n.geographicalContext.city` | `intermediary[n].location.city` |   
`msg.request.ipChain.n.geographicalContext.country` | `intermediary[n].location.country_or_region` |   
`msg.request.ipChain.n.geographicalContext.geolocation.lat` | `intermediary[n].location.region_latitude` |   
`msg.request.ipChain.n.geographicalContext.geolocation.lon` | `intermediary[n].location.region_longitude` |   
`msg.request.ipChain.n.geographicalContext.state` | `intermediary[n].location.state` |   
`msg.request.ipChain.n.ip` | `intermediary[n].ip` |   
`msg.securityContext.asNumber` | `security_result.detection_fields` |   
`msg.securityContext.asOrg` | `security_result.detection_fields` |   
`msg.securityContext.domain` | `security_result.detection_fields` |   
`msg.securityContext.isProxy` | `security_result.detection_fields` |   
`msg.securityContext.isp` | `security_result.detection_fields` |   
`msg.severity` | `security_result.severity` |   
`msg.target.alternateId (when msg.target.type == User)` | `target.user.email_addresses` | When `msg.target.type` = `User`. However, if parsing fails, this is mapped to `target.user.userid`  
or else  
`target_user_name` is mapped `target.user.userid`.  
`msg.target.detailEntry.policyType` | `target.resource_ancestors.attribute.labels` | When `msg.target.type` = `PolicyEntity`.  
`msg.target.detailEntry.signOnModeType` | `security_result.detection_fields` | When `msg.target.type` is any case other than `AppInstance`, `PolicyEntity`, `PolicyRule`, or `User`.  
`msg.target.displayName` | `additional.fields` |   
`msg.target.displayName` | `about.resource.name` | When `msg.target.type` is any case other than `AppInstance`, `PolicyEntity`, `PolicyRule`, or `User`.  
`msg.target.displayName` | `principal.user.user_display_name` | When `msg.target.type` = `User`.  
`msg.target.displayName` | `target.application` | When `msg.target.type` = `AppInstance`.  
`msg.target.displayName` | `target.resource.name` | When `msg.target.type` = `AppInstance`.  
`msg.target.displayName` | `target.resource.name` | When `msg.target.type` = `PolicyRule`.  
`msg.target.displayName` | `target.resource_ancestors.name` | When `msg.target.type` = `PolicyEntity`.  
`msg.target.id` | `about.resource.product_object_id` | When `msg.target.type` is any case other than `AppInstance`, `PolicyEntity`, `PolicyRule`, or `User`.  
`msg.target.id` | `target.resource.product_object_id` | When `msg.target.type` = `AppInstance`.  
`msg.target.id` | `target.resource.product_object_id` | When `msg.target.type` = `PolicyRule`.  
`msg.target.id` | `target.resource_ancestors.product_object_id` | When `msg.target.type` = `PolicyEntity`.  
`msg.target.id` | `target.user.product_object_id` | When `msg.target.type` = `User`.  
`msg.target.type` | `about.resource.resource_subtype` | When `msg.target.type` is any case other than `AppInstance`, `PolicyEntity`, `PolicyRule`, or `User`.  
`msg.target.type` | `target.resource.resource_subtype` | When `msg.target.type` = `AppInstance`.  
`msg.target.type` | `target.resource.resource_subtype` | When `msg.target.type` = `PolicyRule`.  
`msg.target.type` | `target.resource_ancestors.resource_subtype` | When `msg.target.type` = `PolicyEntity`.  
`msg.target.type` | `target.user.attribute.roles.name` | When `msg.target.type` = `User`.  
`msg.transaction.id` | `network.session_id` |   
`msg.transaction.type` | `additional.fields` | Event_type  
`msg.uuid` | `metadata.product_log_id` |   
`operator` | `security_result.detection_fields` |   
`outcome.reason`  
`detail.outcome.reason` | `security_result.category_details` |   
`outcome.result`  
`detail.outcome.result` | `security_result.action` |   
`profile.displayName` | `principal.user.user_display_name` |   
`profile.email` | `principal.user.email_addresses` |   
`profile.login` | `principal.user.userid` | username => `principal.user.userid`  
`published` | `metadata.event_timestamp` |   
`published` | `metadata.event_timestamp` |   
`request.ipChain.0.geographicalContext.city`  
`detail.request.ipChain.0.geographicalContext.city` | `principal.location.city` |   
`request.ipChain.0.geographicalContext.country`  
`detail.request.ipChain.0.geographicalContext.country` | `principal.location.country_or_region` |   
`request.ipChain.0.geographicalContext.state`  
`detail.request.ipChain.0.geographicalContext.state` | `principal.location.state` |   
`request.ipChain.0.ip` | `principal.ip`  
`principal.asset.ip` |   
`request.ipChain.1.geographicalContext.city` | `intermediary.location.city` |   
`request.ipChain.1.geographicalContext.country` | `intermediary.location.country_or_region` |   
`request.ipChain.1.geographicalContext.state` | `intermediary.location.state` |   
`securityContext.asNumber` | `security_result.detection_fields` |   
`securityContext.asOrg` | `security_result.detection_fields` |   
`securityContext.domain` | `security_result.detection_fields` |   
`securityContext.isProxy` | `security_result.detection_fields` |   
`securityContext.isProxy` | `security_result.detection_fields`  
`additional.fields` |   
`securityContext.isp` | `security_result.detection_fields` |   
`severity`  
`detail.severity` | `security_result.severity` |   
`target[].alternateId` | `target.resource.attribute.labels` |   
`target[].detailEntry.methodTypeUsed` | `target.resource_ancestors.attribute.labels` |   
`target[].detailEntry.methodUsedVerifiedProperties` | `target.resource_ancestors.attribute.labels` |   
`target[].detailEntry.policyRuleFactorMode` | `security_result.detection_fields` |   
`target[].detailEntry.policyType` | `target.resource_ancestors.attribute.labels` |   
`target[].detailEntry.signOnModeType` | `security_result.detection_fields` |   
`target[].displayName` | `additional.fields` |   
`target[].displayName` | `target.application`  
`target.resource.name` |   
`target[].displayName` | `target.resource.name` |   
`target[].displayName` | `target.resource_ancestors.name` |   
`target[].id` | `target.resource.product_object_id` |   
`target[].id` | `target.resource_ancestors.product_object_id` |   
`target[].type` | `target.resource.resource_subtype` |   
`target[].type` | `target.resource_ancestors.resource_subtype` |   
`target.0.alternateId` | _See the remark._ | `tgtuser_id` => `target.user.userid`  
`%{tgtusername}@%{tgtdomain}` => `target.user.email_addresses`  
`target.0.detailEntry.clientAppId` | `target.asset_id` |   
`target.0.displayName`  
`detail.target.0.displayName` | `target.user.user_display_name` |   
`target.0.displayName` / `target.1.displayName` | `target.user.group_identifiers` |   
`target.0.id` | `target.user.product_object_id` |   
`target.0.type`  
`detail.target.0.type` | `target.user.attribute.roles.name` |   
`target.1.alternateId` | _See the remark._ | `tgtuser_id` => `target.user.userid`  
`%{tgtusername}@%{tgtdomain}` => `target.user.email_addresses`  
`target.1.detailEntry.clientAppId` | `target.asset_id` |   
`target.1.displayName` | `target.user.user_display_name` |   
`target.1.id` | `target.user.product_object_id` |   
`target.1.type` | `target.user.attribute.roles.name` |   
`transaction.id` | `network.session_id` |   
`type` | `security_result.detection_fields` |   
`user_agent.browser` | `target.resource.attribute.labels` |   
`user_email` | `principal.user.email_addresses` | When eventType is `application.user_membership.update`, `policy.rule.update`, or `user.authentication.auth_via_radius`.  
`user_email` | `principal.user.email_addresses` | When eventType is _not_ `application.user_membership.update`, `policy.rule.update`, or `user.authentication.auth_via_radius`.  
`user_id` | `principal.user.userid` | When eventType is `application.user_membership.update`, `policy.rule.update`, or `user.authentication.auth_via_radius`.  
`user_id` | `principal.user.userid` | When eventType is _not_ `application.user_membership.update`, `policy.rule.update`, or `user.authentication.auth_via_radius`.  
`uuid` | `metadata.product_log_id` |   
`uuid` | `metadata.product_log_id` |   
  
## UDM mapping delta reference

On August 26, 2025, Google SecOps released a new version of the Okta parser, which includes significant changes to the mapping of Okta log fields to UDM fields and changes to the mapping of event types.

### Log-field mapping delta

The following table lists the mapping delta for Okta log-to-UDM fields exposed prior to August 26, 2025 and subsequently (listed in the **Old mapping** and **Current mapping** columns respectively). 

Log field | Old mapping | Current mapping  
---|---|---  
`client.geographicalContext.geolocation.lat` | `target.location.region_latitude` | `principal.location.region_coordinates.latitude`  
`client.geographicalContext.geolocation.lon` | `target.location.region_longitude` | `principal.location.region_coordinates.longitude`  
`created` | `target.resource.attribute.labels` | `metadata.event_timestamp`  
`debugContext.debugData.authnRequestId` | `additional.fields` | `security_result.detection_fields`  
`debugContext.debugData.factorType` | `additional.fields` | `security_result.detection_fields`  
`debugContext.debugData.traceId` | `additional.fields` | `security_result.detection_fields`  
`debugContext.debugData.tunnels.anonymous` | `security_result.detection_fields` | `network.proxy_info.anonymous`  
`lastUpdated` | `target.resource.attribute.labels` | `target.resource.attribute.last_update_time`  
`platform` when platform is iOS | `principal.platform` = `MAC` | `principal.platform` = `IOS`  
`securityContext.asOrg` | `security_result.detection_fields` | `network.organization_name`  
`securityContext.isProxy` | `additional.fields` | `network.is_proxy`  
`target.detailEntry.methodTypeUsed` | `target.resource.attribute.labels` | `security_result.detection_fields`  
`target.detailEntry.methodUsedVerifiedProperties` | `target.resource.attribute.labels` | `security_result.detection_fields`  
  
### Event-type mapping delta

Multiple events that were classified before as generic event are now properly classified with meaningful event types.

The following table lists the delta for the handling of Okta event types prior to August 26, 2025 and subsequently (listed in the **Old event_type** and **Current event-type** columns respectively).

eventType from log | Old event_type | Current event_type  
---|---|---  
`app.oauth2.as.authorize` | `USER_UNCATEGORIZED` | `USER_LOGIN`  
`app.oauth2.as.authorize.code` | `USER_UNCATEGORIZED` | `USER_LOGIN`  
`app.oauth2.as.authorize.implicit.access_token` | `USER_UNCATEGORIZED` | `USER_LOGIN`  
`app.oauth2.as.authorize.implicit.id_token` | `USER_UNCATEGORIZED` | `USER_LOGIN`  
`app.oauth2.authorize.code` | `USER_UNCATEGORIZED` | `USER_LOGIN`  
`app.oauth2.token.grant` | `USER_UNCATEGORIZED` | `USER_LOGIN`  
`application.user_membership.remove` | `USER_UNCATEGORIZED` | `USER_CHANGE_PERMISSIONS`  
`application.user_membership.update` | `STATUS_UPDATE` | `USER_CHANGE_PERMISSIONS`  
`user.authentication.auth_via_AD_agent` | `STATUS_UPDATE` | `USER_UNCATEGORIZED`  
`user.authentication.slo` | `USER_UNCATEGORIZED` | `USER_LOGOUT`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
