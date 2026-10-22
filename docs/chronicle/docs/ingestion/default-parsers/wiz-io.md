---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wiz-io/
title: Collect Wiz logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:00.359292+00:00
---

# Collect Wiz logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wiz-io/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Wiz logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** The legacy Chronicle Ingestion API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. To ingest logs into Google SecOps, use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

This document explains how to ingest Wiz logs into Google Security Operations. The parser transforms Wiz JSON formatted logs into a Unified Data Model (UDM). It first initializes default values for UDM fields, then parses the JSON message, extracts relevant fields like user information, location, device details, and security outcomes. 

Wiz is a cloud security platform that delivers agentless, end-to-end visibility and risk prioritization across Google Cloud, AWS, Azure, OCI, and Kubernetes environments.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to Wiz



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Configure the integration in Wiz

  1. [Click the Google SecOps (Chronicle) integration](https://docs.wiz.io/docs/chronicle-integration) in your Wiz tenant. 
     1. Alternatively, sign in to the **Wiz** web UI.
     2. Go to the **Connect to Wiz** page.
     3. Click **Google SecOps (Chronicle)**.
  2. Enter a name for the Google SecOps integration.
  3. Select the **Scope**.
  4. Enter your Google SecOps Customer ID.
  5. Enter the **Project ID** containing your Google SecOps instance.
  6. Select the **Location** where your Google SecOps data is stored.
  7. Optional: Enter the environment **Namespace** to identify the data domain (default is `WIZ`).
  8. Upload the **Service Account Key (.JSON)** file.
  9. Ensure the service account has been granted the `roles/chronicle.editor` role in the parent project, then select **I granted Chronicle API Editor**.
  10. Click **Save**.

**Note:** For more information, access the [Google SecOps guide](https://docs.wiz.io/docs/chronicle-integration) in your Wiz tenant. 

## Add an automation rule for Google Security Operations

Add an automation rule to push Wiz **Issues** or **Detections** to Google SecOps when specified criteria are met. 

**Note:** The volume of actions triggered by automation rules are subject to [service limits](https://docs.cloud.google.com/chronicle/docs/reference/service-limits) and [burst limits](https://docs.cloud.google.com/chronicle/docs/ingestion/burst-limits).

To add an automation rule, do the following:

  1. On the **Policies > Automation Rules** page, click **Add Rule**.
  2. Enter a short but meaningful **Name**.
  3. Optional: Enter a longer **Description**.
  4. Select a **Scope**.
  5. Under **Rule Conditions** , select when the rule should be triggered:

     * **Issues** trigger
     * **Detection** trigger
  6. Choose the **Native** data format.

     * **Native** : this is the option that Google recommends. The **Native** data format is a Wiz schema that includes fields like category, trigger source, projects.
     * **OCSF** : output events in the Open Cybersecurity Schema Framework format. 
  7. We recommend that you select the **Include the Issue's evidence** checkbox.

  8. Optional: Under **Labels** , click **Add**.

  9. **IF** : Click **Add filter** , then define the filter criteria. Repeat for each additional filter.

  10. **THEN** : Do the following to trigger the **Automated Platform Action** for the automation rule:

     1. Click **Add action**.
     2. From the list of configured integrations, select the integrations that apply to the trigger you selected.
     3. Optional: Modify the default **Action Configuration**. If the selected integration supports **Action Configuration** , you're able to:

        * **Use** an existing **Action template** by clicking **Load from template** , selecting an **Action template** , and then clicking **Use template**.
        * **Modify** the **Action parameters**.
     4. Save your modifications by clicking **Save as template** , entering a **Template name** , selecting a **Project Scope** , and clicking **Save**.

     5. Optional: Click **Test** to validate the **Automation Rule** using the selected integration and mock data.

     6. Click **Add Action**.

     7. Optional: Click **Add Action** again to add up to ten **Actions**.

  11. We recommend that you go to the bottom of the page to preview past matches for the selected `IF` filters. Verify that the filter results match your expectations.

**Note:** The new automation rule won't run for all existing matches shown in the preview, only for future matches that meet the selected criteria. Using some filter conditions, like the **IS NOT** operator, won't generate a preview of matches.
  12. Click **Add Rule**.


**Note:** If the automation rule uses the **Native** data format, you can find the logs in your instance under the `WIZ_IO` log type. If the automation rule uses the **OCSF** data format, you can find the logs in your instance under the `OCSF` log type.

## UDM mapping table

The following table applies to the `WIZ_IO` log type. For the `OCSF` log type, refer to [Collect OCSF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ocsf#field-mapping).

Log field | UDM mapping | Comment  
---|---|---  
`account.cloudPlatform` | `additional.fields` (key = "cloudAccount_cloudPlatform") | Inside for account in cloudAccounts loop  
`account.externalId` | `target.cloud.project.id` | Inside for account in cloudAccounts loop  
`account.id` | `target.resource.attribute.labels` (key = "cloudAccount_id") | Inside for account in cloudAccounts loop  
`account.name` | `target.cloud.project.name` | Inside for account in cloudAccounts loop  
`action` | `metadata.product_event_type` | If has_user == "true" and action == "Login": metadata.event_type is set to USER_LOGIN, extensions.auth.type is set to AUTHTYPE_UNSPECIFIED  
`actionParameters.clientID` | `additional.fields` (key = "client ID") |   
`actionParameters.clientID` | `principal.group.product_object_id` |   
`actionParameters.groups` | `security_result.detection_fields` (key = "service_account_group") | Iterates through the array  
`actionParameters.input.patch.portalVisitHistory.dateTime` | `additional.fields` (key = "dateTime {index}") | Iterated within the array.  
`actionParameters.input.patch.portalVisitHistory.id` | `principal.resource.attribute.labels` (key = "id {index}") | Iterated within the array.  
`actionParameters.input.patch.portalVisitHistory.name` | `principal.resource.attribute.labels` (key = "name {index}") | Iterated within the array.  
`actionParameters.input.patch.portalVisitHistory.resourceName` | `principal.resource.attribute.labels` (key = "resourceName {index}") | Iterated within the array.  
`actionParameters.input.patch.portalVisitHistory.resourceType` | `principal.resource.attribute.labels` (key = "resourceType {index}") | Iterated within the array.  
`actionParameters.input.patch.portalVisitHistory.ruleType` | `principal.resource.attribute.labels` (key = "ruleType {index}") | Iterated within the array.  
`actionParameters.input.patch.portalVisitHistory.type` | `additional.fields` (key = "type {index}") | Iterated within the array.  
`actionParameters.name` | `target.user.user_display_name` |   
`actionParameters.products` | `security_result.detection_fields` (key = "service_account_product") | Iterates through the array, skipping empty or "*" values  
`actionParameters.role` | `target.user.attribute.roles` |   
`actionParameters.scopes` | `security_result.detection_fields` (key = "service_account_scope") | Iterated, each scope added as a separate key-value pair.  
`actionParameters.selection.preferences` | `additional.fields` (key = "Preferences") | Iterated, values are added as a list of strings.  
`actionParameters.userEmail` | `target.user.email_addresses` |   
`actionParameters.userID` | `target.user.userid` |   
`actionParameters.userpoolID` | `additional.fields` (key = "UserPool ID") |   
`actionParameters.userPoolType` | `additional.fields` (key = "UserPool Type") |   
`actor.displayName` | `target.user.user_display_name` |   
`actor.id` | `target.user.userid` |   
`actors.externalId` | `intermediary.ip`, `intermediary.asset.ip` | Iterates through actors.  
`actors.id` | `additional.fields` (key = "actor_id: %{index}") | Iterates through actors.  
`actors.name` | `target.ip`, `target.asset.ip` | Iterates through actors.  
`actors.type` | `target.resource.attribute.labels` (key = "actor_type: %{index}") | Iterates through actors.  
`authenticationContext.authenticationProvider` | `security_result.detection_fields` (key = "authenticationProvider") | Merged into security_result.detection_fields.  
`authenticationContext.credentialProvider` | `security_result.detection_fields` (key = "credentialProvider") | Merged into security_result.detection_fields.  
`authenticationContext.credentialType` | `extensions.auth.mechanism` | Logic: "OTP" for SMS/EMAIL, "USERNAME_PASSWORD" for PASSWORD.  
`authenticationContext.externalSessionId` | `network.parent_session_id` |   
`client.device` | `principal.asset.type` | Conditionally mapped based on regex.  
`client.geographicalContext.city` | `principal.location.city` |   
`client.geographicalContext.country` | `principal.location.country_or_region` |   
`client.geographicalContext.geolocation.lat` | `principal.location.region_latitude` |   
`client.geographicalContext.geolocation.lon` | `principal.location.region_longitude` |   
`client.geographicalContext.postalCode` | `additional.fields` (key = "Postal code") |   
`client.geographicalContext.state` | `principal.location.state` |   
`client.ipAddress` | `principal.ip`, `principal.asset.ip` |   
`client.userAgent.browser` | `target.resource.attribute.labels` (key = "Browser") |   
`client.userAgent.os` | `principal.platform` | Mapped to LINUX, WINDOWS, or MAC.  
`client.userAgent.rawUserAgent` | `network.http.user_agent`, `network.http.parsed_user_agent` |   
`control.description` | `security_result.detection_fields` (key = "control_description") |   
`control.id` | `security_result.detection_fields` (key = "control_id") |   
`control.IssueURL` | `security_result.url_back_to_product` |   
`control.name` | `security_result.detection_fields` (key = "control_name") |   
`control.resolutionRecommendation` | `security_result.detection_fields` (key = "control_resolution") |   
`control.risks` | `security_result.detection_fields` (key = "risk {i}") | Iterates through the array  
`control.securitySubCategories.category.framework.name` | `security_result.detection_fields` (key = "framework_name") | Loop processes subcategories array.  
`control.securitySubCategories.category.name` | `security_result.category_details` | Loop processes subcategories array.  
`control.securitySubCategories.title` | `security_result.summary` | Loop processes subcategories array.  
`control.severity` | `security_result.severity` | Conditionally sets HIGH, MEDIUM, or LOW.  
`createdAt` | `metadata.event_timestamp` |   
`debugContext.debugData.behaviors` | `security_result.description` |   
`debugContext.debugData.deviceFingerprint` | `target.asset.asset_id` | Prepended with "device_finger_print:"  
`debugContext.debugData.dtHash` | `security_result.detection_fields` (key = "dtHash") |   
`debugContext.debugData.factor` | `security_result.detection_fields` (key = "factor") |   
`debugContext.debugData.promptingPolicyTypes` | `security_result.detection_fields` (key = "promptingPolicyTypes") |   
`debugContext.debugData.requestUri` | `extensions.auth.auth_details` |   
`description` | `security_result.description` |   
`detection.actors.externalId` | `principal.user.userid` | iterating over detection.actors  
`detection.actors.externalId` | `target.user.userid` | iterating over detection.actors  
`detection.actors.id` | `principal.user.product_object_id` | iterating over detection.actors  
`detection.actors.id` | `target.user.product_object_id` | iterating over detection.actors  
`detection.actors.name` | `principal.user.user_display_name` | iterating over detection.actors  
`detection.actors.name` | `target.user.user_display_name` | iterating over detection.actors  
`detection.actors.nativeType` | `principal.user.attribute.labels` (key = "actor_nativeType {index}") | iterating over detection.actors  
`detection.actors.nativeType` | `target.user.attribute.labels` (key = "primaryActor_nativeType {index}") | iterating over detection.actors  
`detection.actors.type` | `security_result.detection_fields` (key = "actor_type {index}") | iterating over detection.actors  
`detection.actors.type` | `security_result.detection_fields` (key = "primary_actor_type {index}") | iterating over detection.actors  
`detection.cloudAccounts.cloudPlatform` | `additional.fields` (key = "detection_cloudAccount_cloudPlatform {i}") | Iterates through the array  
`detection.cloudAccounts.externalId` | `additional.fields` (key = "detection_cloudAccount_externalId {i}") | Iterates through the array  
`detection.cloudAccounts.id` | `additional.fields` (key = "detection_cloudAccount_id {i}") | Iterates through the array  
`detection.cloudAccounts.name` | `additional.fields` (key = "detection_cloudAccount_name {i}") | Iterates through the array  
`detection.cloudOrganizations` | `principal.resource.attribute.labels` (key = "detection _cloudOrganization_{index}") |   
`detection.createdAt` | `additional.fields` (key = "detection_createdAt") |   
`detection.description` | `security_result.description` |   
`detection.detectionURL` | `security_result.url_back_to_product` |   
`detection.id` | `metadata.product_log_id` |   
`detection.mitreTactics` | `additional.fields` (key = "mitre_tactic {i}") | Iterates through the array  
`detection.mitreTechniques` | `additional.fields` (key = "mitre_technique {i}") | Iterates through the array  
`detection.primaryActor.actingAs.externalId` | `principal.resource.attribute.labels` (key = "detection_primaryActor_actingAs_externalId") |   
`detection.primaryActor.actingAs.id` | `principal.resource.attribute.labels` (key = "detection_primaryActor_actingAs_id") |   
`detection.primaryActor.actingAs.name` | `principal.resource.attribute.labels` (key = "detection_primaryActor_actingAs_name") |   
`detection.primaryActor.actingAs.providerUniqueId` | `principal.resource.attribute.labels` (key = "detection_primaryActor_actingAs_providerUniqueId") |   
`detection.primaryActor.actingAs.type` | `principal.resource.attribute.labels` (key = "detection_primaryActor_actingAs_type") |   
`detection.primaryResource.externalId` | `target.resource.product_object_id` |   
`detection.primaryResource.id` | `additional.fields` (key = "detection_primaryResource_id") |   
`detection.primaryResource.name` | `target.hostname`, `target.asset.hostname` |   
`detection.primaryResource.type` | `additional.fields` (key = "detection_primaryResource_type") |   
`detection.primaryResource.type` | `target.resource.resource_type` | Set to VIRTUAL_MACHINE if type matches criteria.  
`detection.resources.cloudProviderURL` | `target.resource.attribute.labels` (key = "detection_resource_cloudProviderURL {i}") | Iterates through detection.resources array  
`detection.resources.externalId` | `security_result.about.resource.attribute.labels` (key = "detection_resource_externalId {i}") | Iterates through detection.resources array  
`detection.resources.id` | `security_result.about.resource.attribute.labels` (key = "detection_resource_id {i}") | Iterates through detection.resources array  
`detection.resources.kubernetesCluster.externalId` | `target.resource.attribute.labels` (key = "kubernetesCluster _externalId_{i}") | Iterates through detection.resources array  
`detection.resources.kubernetesCluster.id` | `target.resource.attribute.labels` (key = "kubernetesCluster _id_{i}") | Iterates through detection.resources array  
`detection.resources.kubernetesnamespace.id` | `additional.fields` (key = "kubernetesnamespace _id_{i}") | Iterates through detection.resources array  
`detection.resources.name` | `security_result.about.resource.attribute.labels` (key = "detection_resource_name {i}") | Iterates through detection.resources array  
`detection.resources.nativeType` | `security_result.about.resource.attribute.labels` (key = "detection_resource_nativeType {i}") | Iterates through detection.resources array  
`detection.resources.region` | `security_result.about.resource.attribute.labels` (key = "detection_resource_region {i}") | Iterates through detection.resources array  
`detection.resources.status` | `target.resource.attribute.labels` (key = "detection_resource_status {i}") | Iterates through detection.resources array  
`detection.resources.type` | `security_result.about.resource.attribute.labels` (key = "detection_resource_type {i}") | Iterates through detection.resources array  
`detection.tdrId` | `additional.fields` (key = "detection_tdr_id") |   
`detection.tdrSource` | `additional.fields` (key = "detection_tdr_source") |   
`detection.threatId` | `security_result.threat_id` |   
`detection.threatURL` | `security_result.detection_fields` (key = "threatURL") |   
`detection.timeframe.end` | `metadata.collected_timestamp` |   
`detection.timeframe.start` | `metadata.event_timestamp` |   
`detection.title` | `security_result.rule_name` |   
`detection.triggeringEvents.actor.externalId` | `security_result.detection_fields` (key = "detection_triggeringEvent_actor_externalId {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.actor.id` | `security_result.detection_fields` (key = "detection_triggeringEvent_actor_id {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.actor.name` | `security_result.detection_fields` (key = "detection_triggeringEvent_actor_name {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.actor.type` | `security_result.detection_fields` (key = "detection_triggeringEvent_actor_type {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.actorIP` | `principal.ip` & `principal.asset.ip` | Iterates through triggeringEvents.  
`detection.triggeringEvents.actorIP` | `principal.resource.attribute.labels` (key = "detection_triggeringEvent_actorIP {index}") | Iterates through triggeringEvents.  
`detection.triggeringEvents.actorIPMeta.autonomousSystemNumber` | `additional.fields` (key = "detection_triggeringEvent_actorIPMeta_autonomousSystemNumber {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.actorIPMeta.autonomousSystemOrganization` | `additional.fields` (key = "detection_triggeringEvent_actorIPMeta_autonomousSystemOrganization {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.actorIPMeta.country` | `additional.fields` (key = "detection_triggeringEvent_actorIPMeta_country {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.actorIPMeta.isForeign` | `additional.fields` (key = "detection_triggeringEvent_actorIPMeta_isForeign {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.actorIPMeta.reputation` | `security_result.about.resource.attribute.labels` (key = "detection_triggeringEvent_actorIPMeta_reputation {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.actorIPMeta.reputationSource` | `additional.fields` (key = "detection_triggeringEvent_actorIPMeta_reputationSource {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.category` | `additional.fields` (key = "detection_triggeringEvent_category {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.cloudPlatform` | `additional.fields` (key = "detection_triggeringEvent_cloudPlatform {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.cloudProviderUrl` | `target.url` | Iterates through triggeringEvents  
`detection.triggeringEvents.description` | `metadata.description` | Iterates through triggeringEvents  
`detection.triggeringEvents.eventTime` | `additional.fields` (key = "detection_triggeringEvent_eventTime {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.externalId` | `additional.fields` (key = "detection_triggeringEvent_externalId {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.id` | `additional.fields` (key = "detection_triggeringEvent_id {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.name` | `additional.fields` (key = "detection_triggeringEvent_name {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.origin` | `additional.fields` (key = "detection_triggeringEvent_origin {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.runtimeDetails.currentWorkingDirectory` | `additional.fields` (key = "detection_triggeringEvent_runtimeDetails_currentWorkingDirectory {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.runtimeDetails.processTree[0].path` | `principal.process.file.full_path` | Iterates through triggeringEvents. Overwrites index 0/1 logic.  
`detection.triggeringEvents.runtimeDetails.processTree[0].username` | `additional.fields` (key = "detection_triggeringEvent_runtimeDetails_username {index}") | Iterates through triggeringEvents.  
`detection.triggeringEvents.runtimeDetails.processTree[1].hash` | `additional.fields` (key = "detection_triggeringEvent_runtimeDetails_hash {index}") | Iterates through triggeringEvents.  
`detection.triggeringEvents.runtimeDetails.processTree[2].path` | `principal.process.parent_process.file.full_path` | Iterates through triggeringEvents  
`detection.triggeringEvents.source` | `additional.fields` (key = "detection_triggeringEvent_source {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents.status` | `additional.fields` (key = "detection_triggeringEvent_status {index}") | Iterates through triggeringEvents  
`detection.triggeringEvents[0].runtimeDetails.processTree[0].command` | `target.process.command_line` | Only for first triggeringEvent and first processTree element  
`detection.triggeringEvents[0].runtimeDetails.processTree[0].hash` | `target.process.file.sha1` | Only for first triggeringEvent and first processTree element  
`detection.triggeringEvents[0].runtimeDetails.processTree[0].path` | `target.process.file.full_path` | Only for first triggeringEvent and first processTree element  
`detection.triggeringEvents[0].runtimeDetails.processTree[0].size` | `target.process.file.size` | Only for first triggeringEvent and first processTree element  
`detection.triggeringEvents[0].runtimeDetails.processTree[0].username` | `principal.user.userid` | Only for first triggeringEvent and first processTree element  
`detection.triggeringEvents[0].runtimeDetails.processTree[1].command` | `principal.process.command_line` | Only for first triggeringEvent and second processTree element.  
`detection.triggeringEvents[0].runtimeDetails.processTree[1].hash` | `principal.process.file.sha1` | Only for first triggeringEvent and second processTree element.  
`detection.triggeringEvents[0].runtimeDetails.processTree[1].path` | `principal.process.file.full_path` | Only for first triggeringEvent and second processTree element.  
`detection.triggeringEvents[0].runtimeDetails.processTree[1].size` | `principal.process.file.size` | Only for first triggeringEvent and second processTree element.  
`detection.triggeringEventsCount` | `additional.fields` (key = "triggering_events_count") |   
`DetectionURL` | `security_result.url_back_to_product` |   
`dueAt` | `additional.fields` (key = "due_at") |   
`entitySnapshot.cloudPlatform` | `principal.cloud.vpc.name` |   
`entitySnapshot.externalId` | `principal.group.product_object_id` |   
`entitySnapshot.id` | `principal.asset_id` |   
`entitySnapshot.name` | `principal.cloud.project.name` |   
`entitySnapshot.nativeType` | `principal.cloud.project.resource_subtype` |   
`entitySnapshot.providerId` | `principal.cloud.vpc.id` |   
`entitySnapshot.status` | `security_result.action_details` |   
`entitySnapshot.tags.io.cri-containerd.kind` | `target.resource.attribute.labels` (key = "Containerd Kind") |   
`entitySnapshot.tags.io.kubernetes.container.name` | `target.resource.attribute.labels` (key = "Container Name") |   
`entitySnapshot.tags.io.kubernetes.pod.name` | `target.resource.attribute.labels` (key = "Pod Name") |   
`entitySnapshot.tags.io.kubernetes.pod.namespace` | `principal.namespace` |   
`entitySnapshot.tags.io.kubernetes.pod.namespace` | `target.resource.attribute.labels` (key = "Pod Namespace") |   
`entitySnapshot.tags.io.kubernetes.pod.uid` | `target.resource.attribute.labels` (key = "Pod Id") |   
`entitySnapshot.tags.maintainer` | `target.resource.attribute.labels` (key = "Maintainer") |   
`entitySnapshot.type` | `principal.cloud.project.id` |   
`eventType` | `metadata.product_event_type` |   
`eventType` (specific values) | `extensions.auth.mechanism` | Merged with auth_type for login types.  
`Hardcoded to "WIZ_IO"` | `metadata.product_name` |   
`Hardcoded to "WIZ_IO"` | `metadata.vendor_name` |   
`id` | `metadata.product_log_id` |   
`issue.created` | `metadata.event_timestamp` |   
`issue.id` | `metadata.product_log_id` |   
`issue.projects` | `additional.fields` (key = "issue_projects") |   
`issue.severity` | `Sets intermediate variable severity` | Sets to INFORMATIONAL if condition matches.  
`issue.status` | `security_result.action_details` |   
`issue.status` | `security_result.action_details` | Mapped only if status is "OPEN"  
`metadata_data.version` | `metadata.product_version` |   
`mitreTactics` (array element) | `additional.fields` (key = "mitre_tactic %{i}") | Iterates through the array.  
`mitreTechniques` (array element) | `additional.fields` (key = "mitre_technique %{i}") | Iterates through the array.  
`outcome.reason` | `security_result.category_details` |   
`outcome.result` | `security_result.action` | Indirect mapping to ALLOW, CHALLENGE, or BLOCK.  
`primaryActor.actingAs` | `additional.fields` (key = "primaryActor_actingAs") |   
`primaryActor.email` | `additional.fields` (key = "primaryActor_email") |   
`primaryActor.externalId` | `principal.ip`, `principal.asset.ip` |   
`primaryActor.id` | `additional.fields` (key = "primaryActor_id") |   
`primaryActor.name` | `target.ip`, `target.asset.ip` |   
`primaryActor.nativeType` | `additional.fields` (key = "primaryActor_nativeType") |   
`primaryActor.providerUniqueId` | `additional.fields` (key = "primaryActor_providerUniqueId") |   
`primaryActor.type` | `principal.resource.type` |   
`primaryResource.cloudAccount.cloudPlatform` | `additional.fields` (key = "primaryResourceCloudPlatform") |   
`primaryResource.cloudAccount.externalId` | `target.cloud.project.id` |   
`primaryResource.cloudAccount.id` | `additional.fields` (key = "primaryResourceCloudAccountId") |   
`primaryResource.cloudAccount.name` | `target.cloud.project.name` |   
`primaryResource.cloudProviderURL` | `target.url` |   
`primaryResource.externalId` | `additional.fields` (key = "primaryResourceExternalId") |   
`primaryResource.id` | `target.resource.id` |   
`primaryResource.name` | `target.resource.name` |   
`primaryResource.nativeType` | `additional.fields` (key = "primaryResourceNativeType") |   
`primaryResource.region` | `target.asset.location.country_or_region` |   
`primaryResource.type` | `target.resource.type` |   
`process.command` | `target.resource.attribute.labels` (key = "process _command_{process_index}") |   
`process.container.externalId` | `target.resource.attribute.labels` (key = "container _externalId_{process_index}") |   
`process.container.id` | `target.resource.attribute.labels` (key = "process_container _id_{process_index}") |   
`process.container.imageExternalId` | `target.resource.attribute.labels` (key = "container _imageExternalId_{process_index}") |   
`process.container.imageId` | `target.resource.attribute.labels` (key = "container _imageId_{process_index}") |   
`process.container.name` | `target.resource.attribute.labels` (key = "process_container _name_{process_index}") |   
`process.currentWorkingDirectory` | `target.resource.attribute.labels` (key = "currentWorkingDirectory_{process_index}") |   
`process.hash` | `target.resource.attribute.labels` (key = "process _hash_{process_index}") |   
`process.id` | `target.resource.attribute.labels` (key = "process _id_{process_index}") |   
`process.path` | `target.resource.attribute.labels` (key = "process _path_{process_index}") |   
`process.size` | `target.process.file.size` |   
`process.userId` | `target.resource.attribute.labels` (key = "process _userId_{process_index}") |   
`process.username` | `target.resource.attribute.labels` (key = "process _username_{process_index}") |   
`requestId` | `metadata.product_log_id` |   
`resource.cloudAccount.cloudPlatform` | `additional.fields` (key = "cloudPlatform") | Part of object merged into repeated about field.  
`resource.cloudAccount.externalId` | `additional.fields` (key = "cloudAccountExternalId") | Part of object merged into repeated about field.  
`resource.cloudAccount.id` | `additional.fields` (key = "cloudAccountId") | Part of object merged into repeated about field.  
`resource.cloudAccount.name` | `cloudAccountName` |   
`resource.cloudPlatform` | `additional.fields` (key = "resource_cloudPlatform") |   
`resource.cloudProviderURL` | `about.url` | Part of object merged into repeated about field.  
`resource.cloudProviderURL` | `target.url` |   
`resource.externalId` | `additional.fields` (key = "externalId") | Part of object merged into repeated about field.  
`resource.id` | `about.resource.product_object_id` | Part of object merged into repeated about field.  
`resource.id` | `target.resource.id` |   
`resource.name` | `about.resource.name` | Part of object merged into repeated about field.  
`resource.name` | `target.resource.name` |   
`resource.nativeType` | `about.resource.resource_subtype` | Part of object merged into repeated about field.  
`resource.region` | `about.location.country_or_region` | Part of object merged into repeated about field.  
`resource.region` | `target.asset.location.country_or_region` |   
`resource.region` | `target.location.country_or_region` |   
`resource.status` | `about.resource.attribute.labels` (key = "status") | Part of object merged into repeated about field.  
`resource.status` | `target.resource.attribute.labels` (key = "status") |   
`resource.subscriptionId` | `target.cloud.project.id` |   
`resource.subscriptionName` | `target.cloud.project.name` |   
`resource.type` | `about.resource.type` | Part of object merged into repeated about field.  
`resource.type` | `target.resource.type` |   
`serviceAccount.name` | `principal.application` | Only if action is "Report"  
`sourceIP` | `principal.ip`, `principal.asset.ip` |   
`sourceRule.id` | `principal.user.userid` |   
`status` | `security_result.summary` |   
`statusChangedAt` | `additional.fields` (key = "status_changed_at") |   
`tdrId` | `security_result.detection_fields` (key = "tdrId") |   
`tdrSource` | `security_result.detection_fields` (key = "tdrSource") |   
`The detection.severity variable` | `security_result.severity` | Normalized (e.g., INFO -> LOW) then mapped.  
`threat.actors.externalId` | `principal.user.email_addresses` | Iterates through threat.actors.  
`threat.actors.id` | `principal.resource.attribute.labels` (key = "actor_id:%{index}") | Mapped for elements after first (index > 0).  
`threat.actors.id` | `principal.resource.product_object_id` | Mapped for the first element (index 0).  
`threat.actors.name` | `principal.user.email_addresses` | Iterates through threat.actors.  
`threat.actors.nativeType` | `principal.resource.attribute.labels` (key = "actor_nativeType:%{index}") | Mapped for elements after first (index > 0).  
`threat.actors.nativeType` | `principal.resource.resource_subtype` | Mapped for the first element (index 0).  
`threat.actors.type` | `additional.fields` (key = "actor_type") | Iterates through threat.actors.  
`threat.cloudAccounts` | `target.resource.attribute.labels` (key = "threat_cloudAccounts") |   
`threat.cloudOrganizations.cloudProvider` | `target.resource.attribute.labels` (key = "org_cloudProvider:%{index}") | Iterates through threat.cloudOrganizations.  
`threat.cloudOrganizations.externalId` | `target.resource.attribute.labels` (key = "org_externalId:%{index}") | Iterates through threat.cloudOrganizations.  
`threat.cloudOrganizations.id` | `target.resource.attribute.labels` (key = "org_id:%{index}") | Iterates through threat.cloudOrganizations.  
`threat.cloudOrganizations.name` | `target.resource.attribute.labels` (key = "org_name:%{index}") | Iterates through threat.cloudOrganizations.  
`threat.cloudPlatform` | `additional.fields` (key = "threat_cloudPlatform") |   
`threat.created` | `metadata.event_timestamp` |   
`threat.description` | `security_result.description` |   
`threat.detectionIds` | `additional.fields` (key = "detectionId") | Comma-separated string split into list.  
`threat.id` | `metadata.product_log_id` |   
`threat.mitreTactics` | `additional.fields` (key = "tactic_val _label_{index}") | Iterates through the array.  
`threat.mitreTechniques` | `additional.fields` (key = "technique_val _label_{i}") | Iterates through the array  
`threat.notes` | `additional.fields` (key = "threat_notes") |   
`threat.projects` | `additional.fields` (key = "threat_projects") |   
`threat.resolutionNote` | `additional.fields` (key = "threat_resolutionNote") |   
`threat.resolvedAt` | `additional.fields` (key = "threat_resolvedAt") |   
`threat.resources.externalId` | `target.resource.attribute.labels` (key = "resource_externalId:%{index}") | Mapped for elements after first (index > 0).  
`threat.resources.externalId` | `target.resource.product_object_id` | Mapped for the first element (index 0).  
`threat.resources.id` | `target.resource.attribute.labels` (key = "resource_id:%{index}") | Iterates through threat.resources.  
`threat.resources.name` | `target.resource.attribute.labels` (key = "resource_name:%{index}") | Mapped for elements after first (index > 0).  
`threat.resources.name` | `target.resource.name` | Mapped for the first element (index 0).  
`threat.resources.nativeType` | `target.resource.attribute.labels` (key = "resource_nativeType:%{index}") | Mapped for elements after first (index > 0).  
`threat.resources.nativeType` | `target.resource.resource_subtype` | Mapped for the first element (index 0).  
`threat.resources.type` | `additional.fields` (key = "resource_type") | Iterates through threat.resources.  
`threat.severity` | `security_result.severity` | Indirectly normalized (e.g., INFO -> LOW).  
`threat.status` | `security_result.action_details` |   
`threat.tdrNames` | `additional.fields` (key = "tdrName") | Comma-separated string split into list.  
`threat.threatURL` | `security_result.url_back_to_product` |   
`threat.title` | `metadata.description` |   
`threat.updatedAt` | `additional.fields` (key = "threat_updatedAt") |   
`threatId` | `security_result.threat_id` |   
`threatURL` | `security_result.detection_fields` (key = "threatURL") |   
`timeframe.end` | `additional.fields` (key = "timeframe_end") |   
`timeframe.start` | `metadata.collected_timestamp` |   
`timestamp` | `metadata.event_timestamp` |   
`title` | `security_result.summary` |   
`trigger.changedBy` | `principal.user.product_object_id` |   
`trigger.ruleId` | `security_result.rule_id` |   
`trigger.ruleName` | `additional.fields` (key = "rule_name") |   
`trigger.source` | `metadata.product_event_type` |   
`trigger.type` | `additional.fields` (key = "trigger_type") |   
`trigger.updatedFields` | `additional.fields` (key = "updated_fields") |   
`triggeringEvents.actor.id` | `principal.user.userid` | Mapped within the triggeringEvents loop.  
`triggeringEvents.actor.name` | `about.user.user_display_name` | Mapped within triggeringEvents loop; merged.  
`triggeringEvents.actor.type` | `about.resource.type` | Mapped within triggeringEvents loop; merged.  
`triggeringEvents.actorIP` | `observer.ip` | Mapped within the triggeringEvents loop.  
`triggeringEvents.actorIPMeta.autonomousSystemNumber` | `principal.labels` (key = "actorIP_autonomousSystemNumber") | Mapped within the triggeringEvents loop.  
`triggeringEvents.actorIPMeta.autonomousSystemOrganization` | `principal.labels` (key = "actorIP_autonomousSystemOrganization") | Mapped within the triggeringEvents loop.  
`triggeringEvents.actorIPMeta.country` | `principal.asset.location.country_or_region` | Mapped within the triggeringEvents loop.  
`triggeringEvents.actorIPMeta.isForeign` | `principal.labels` (key = "actorIP_isForeign") | Mapped within the triggeringEvents loop.  
`triggeringEvents.actorIPMeta.reputation` | `principal.labels` (key = "actorIP_reputation") | Mapped within the triggeringEvents loop.  
`triggeringEvents.actorIPMeta.reputationSource` | `principal.labels` (key = "actorIP_reputationSource") | Mapped within the triggeringEvents loop.  
`triggeringEvents.category` | `about.resource.attribute.labels` (key = "triggeringEvent_category") | Mapped within triggeringEvents loop; merged.  
`triggeringEvents.cloudPlatform` | `security_result.detection_fields` (key = "triggeringEvent_cloudPlatform") | Mapped within the triggeringEvents loop.  
`triggeringEvents.cloudProviderUrltarget.url` | `Mapped within the triggeringEvents loop.` |   
`triggeringEvents.description` | `metadata.description` | Mapped within the triggeringEvents loop.  
`triggeringEvents.eventTime` | `about.resource.attribute.labels` (key = "triggeringEvent_eventTime") | Mapped within triggeringEvents loop; merged.  
`triggeringEvents.externalId` | `principal.resource.product_object_id` | Mapped within the triggeringEvents loop.  
`triggeringEvents.id` | `metadata.product_log_id` | Mapped within the triggeringEvents loop.  
`triggeringEvents.name` | `security_result.summary` | Mapped within the triggeringEvents loop.  
`triggeringEvents.origin` | `about.resource.attribute.labels` (key = "triggeringEvent_origin") | Mapped within triggeringEvents loop; merged.  
`triggeringEvents.resources.externalId` | `about.resource.attribute.labels` (key = "externalId") | Mapped within loops; merged into about array.  
`triggeringEvents.resources.id` | `about.resource.product_object_id` | Mapped within loops; merged into about array.  
`triggeringEvents.resources.name` | `about.resource.name` | Mapped within loops; merged into about array.  
`triggeringEvents.resources.nativeType` | `about.resource.resource_subtype` | Mapped within loops; merged into about array.  
`triggeringEvents.resources.region` | `about.location.country_or_region` | Mapped within loops; merged into about array.  
`triggeringEvents.resources.type` | `about.resource.type` | Mapped within loops; merged into about array.  
`triggeringEvents.source` | `additional.fields` (key = "triggeringEvent_source") | Mapped within the triggeringEvents loop.  
`triggeringEvents.status` | `security_result.action_details` | Mapped within the triggeringEvents loop.  
`triggeringEventsCount` | `additional.fields` (key = "triggeringEventsCount") |   
`type` | `metadata.product_event_type` |   
`updatedAt` | `additional.fields` (key = "updated_at") |   
`version` | `security_result.detection_fields` (key = "version") |   
`detection.primaryActor.id` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`detection.actors.type` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`detection.actors.externalId` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`detection.actors.id` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`detection.actors.name` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`detection.primaryActor.email` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`detection.primaryActor.friendlyName` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`detection.primaryActor.nativeType` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`detection.primaryActor.providerUniqueId` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`detection.actors` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`detection.tdrId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detection.tdrSource` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detection.cloudAccounts.externalId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`detection.cloudAccounts.id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`detection.cloudAccounts.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`detection.primaryResource.type` | `event.idm.read_only_udm.target.resource.resource_type` | Mapped from changelog  
`detection.primaryResource.type` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`detection.triggeringEvents.actor.id` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`detection.triggeringEvents.actorIPMeta.country` | `event.idm.read_only_udm.principal.asset.location.country_or_region` | Mapped from changelog  
`detection.triggeringEvents.actorIPMeta.country` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`detection.triggeringEvents.cloudPlatform` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detection.triggeringEvents.cloudProviderUrl` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`detection.triggeringEvents.cloudProviderUrl` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`detection.triggeringEvents.description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`detection.triggeringEvents.description` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.triggeringEvents.externalId` | `event.idm.read_only_udm.principal.resource.product_object_id` | Mapped from changelog  
`detection.triggeringEvents.externalId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.triggeringEvents.name` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`detection.triggeringEvents.name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detection.triggeringEvents.status` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`detection.triggeringEvents.status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`title` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`createdAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`timeframe.start` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`timeframe.end` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`actors.externalId` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`actors.externalId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`actors.id` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`actors.name` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`actors.name` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`actors.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`primaryActor.externalId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`primaryResource.externalId` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`primaryResource.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primaryResource.name` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`triggeringEvents.actor.name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`triggeringEvents.actor.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`triggeringEvents.actorIP` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`triggeringEvents.actorIPMeta.reputation` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`triggeringEvents.category` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvents.eventTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvents.origin` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.primaryActor.type` | `event.idm.read_only_udm.principal.resource.resource_type` | Mapped from changelog  
`detection.primaryActor.type` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`triggeringEvents.actor.externalId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detection.triggeringEvents.actorIPMeta.reputationDescription` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`triggeringEvents.actorIPMeta.reputationDescription` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`detection.primaryActor.externalId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`detection.primaryActor.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`detection.primaryActor.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.mitreTactics` | `event.idm.read_only_udm.security_result.attack_details.tactics` | Mapped from changelog  
`mitreTactics` | `event.idm.read_only_udm.security_result.attack_details.tactics` | Mapped from changelog  
`entitySnapshot.cloudPlatform` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`entitySnapshot.providerId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`entitySnapshot.type` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`entitySnapshot.nativeType` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`entitySnapshot.name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`resource.id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`resource.subscriptionId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`resource.subscriptionName` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`account.externalId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`account.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`primaryActor.type` | `event.idm.read_only_udm.principal.resource.resource_type` | Mapped from changelog  
`primaryResource.id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`primaryResource.type` | `event.idm.read_only_udm.target.resource.resource_type` | Mapped from changelog  
`primaryResource.cloudAccount.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`primaryResource.cloudAccount.externalId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`triggeringEvent.actorIPMeta.autonomousSystemOrganization` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.actorIPMeta.autonomousSystemNumber` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.actorIPMeta.isForeign` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.actorIPMeta.reputation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.actorIPMeta.reputationSource` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.actor.type` | `event.idm.read_only_udm.about.resource.resource_type` | Mapped from changelog  
`client.geographicalContext.geolocation.lat` | `event.idm.read_only_udm.principal.location.region_coordinates.latitude` | Mapped from changelog  
`client.geographicalContext.geolocation.lon` | `event.idm.read_only_udm.principal.location.region_coordinates.longitude` | Mapped from changelog  
`triggeringEvent.resources.type` | `event.idm.read_only_udm.about.resource.resource_type` | Mapped from changelog  
`resource.type` | `event.idm.read_only_udm.target.resource.resource_type` | Mapped from changelog  
`resources.type` | `event.idm.read_only_udm.about.resource.resource_type` | Mapped from changelog  
`actor.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.executionTime` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`primaryResource.nativeType` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`primaryResource.kubernetesCluster.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`primaryActor.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`primaryResource.kubernetesCluster.externalId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`primaryResource.kubernetesCluster.id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`primaryResource.kubernetesNamespace.externalId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`primaryResource.kubernetesNamespace.id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`primaryResource.kubernetesNamespace.providerUniqueId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`primaryResource.kubernetesNamespace.name` | `event.idm.read_only_udm.target.namespace` | Mapped from changelog  
`primaryResource.kubernetesCluster.name` | `event.idm.read_only_udm.about.resource.attribute.labels` | Mapped from changelog  
`detection.primaryResource.externalId` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`detection.primaryResource.name` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.n.currentWorkingDirectory` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.1.command` | `event.idm.read_only_udm.principal.process.command_line` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.1.path` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.1.hash` | `event.idm.read_only_udm.principal.process.file.sha1` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.1.size` | `event.idm.read_only_udm.principal.process.file.size` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.0.username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.0.command` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.0.path` | `event.idm.read_only_udm.target.process.file.full_path` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.0.hash` | `event.idm.read_only_udm.target.process.file.sha1` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.0.size` | `event.idm.read_only_udm.target.process.file.size` | Mapped from changelog  
`detection.title` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`trigger.ruleName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection_cloudOrganizations` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`detection_triggeringEvent_actorIP` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`detection.primaryActor.actingAs.externalId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`detection.primaryActor.actingAs.id` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`detection.primaryActor.actingAs.name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`detection.primaryActor.actingAs.type` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`detection.primaryActor.actingAs.providerUniqueId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`det_resource.status` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`det_resource.cloudProviderURL` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`actor_externalId` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`actor_name` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`actor_id` | `event.idm.read_only_udm.principal.resource.product_object_id` | Mapped from changelog  
`actor_nativeType` | `event.idm.read_only_udm.principal.resource.resource_subtype` | Mapped from changelog  
`actor_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`threat_cloudPlatform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`threat_resolutionNote` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`threat_resolvedAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`threat_projects` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`threat_notes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tactic_val` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`technique_val` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`threat.updatedAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tdrName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detectionId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource_externalId` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`resource_nativeType` | `event.idm.read_only_udm.target.resource.resource_subtype` | Mapped from changelog  
`org_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`org_name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`org_cloudProvider` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`org_externalId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`resource_externalId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`resource_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`resource_nativeType` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`resource_name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`threat.threatURL` | `event.idm.read_only_udm.security_result.url_back_to_product` | Mapped from changelog  
`threat.id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`threat.title` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`threat.description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`threat.status` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`threat.created` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`threat.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`resource_name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`actor_id` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`actor_nativeType` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`det_resource.kubernetesCluster.id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`det_resource.kubernetesCluster.externalId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`process_command` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`process_container_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`process_container_name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`process.container.externalId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`process.container.imageId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`process.container.imageExternalId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`process_hash` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`process_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`process_path` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`process.username` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`process.userId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`det_resource.kubernetesnamespace.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.1.hash` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.0.username` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.runtimeDetails.currentWorkingDirectory` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.0.path` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`triggeringEvent.runtimeDetails.processTree.2.path` | `event.idm.read_only_udm.principal.process.parent_process.file.full_path` | Mapped from changelog  
`process.size` | `event.idm.read_only_udm.target.process.file.size` | Mapped from changelog  
`detection.id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`detection.threatId` | `event.idm.read_only_udm.security_result.threat_id` | Mapped from changelog  
`detection.detectionURL` | `event.idm.read_only_udm.security_result.url_back_to_product` | Mapped from changelog  
`detection.threatURL` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`actor.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`primaryActor.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`triggeringEvent.actor.externalId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`triggeringEvent.actor.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`triggeringEvent.actor.name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`triggeringEvent.actor.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detection.title` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`detection.description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`detection.severity` | `event.idm.read_only_udm.severity` | Mapped from changelog  
`detection.tdrId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.tdrSource` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.mitreTactics` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.mitreTechniques` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`account.cloudPlatform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`account.externalId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`account.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`account.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.createdAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.primaryResource.externalId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.primaryResource.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.primaryResource.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.primaryResource.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.triggeringEventsCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.actorIPMeta.country` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.category` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.cloudPlatform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.eventTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.externalId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.origin` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.source` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEvent.status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detection.timeframe.start` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`detection.timeframe.end` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`actor.externalId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`actor.id` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`actor.name` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`primaryActor.externalId` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`primaryActor.id` | `event.idm.read_only_udm.target.user.product_object_id` | Mapped from changelog  
`primaryActor.name` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`metadata_data.version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`triggeringEvent.cloudProviderUrl` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`triggeringEvent.actorIPMeta.reputation` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`det_resource.type` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`det_resource.externalId` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`det_resource.id` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`det_resource.name` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`det_resource.nativeType` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`det_resource.region` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`triggeringEvent.actorIP` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`actor.nativeType` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`primaryActor.nativeType` | `event.idm.read_only_udm.target.user.attribute.labels` | Mapped from changelog  
`triggeringEvent.description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`actor.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`trigger.source` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`trigger.updatedFields` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`issue.projects` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.cloudPlatform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`control.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`threatURL` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tdrId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tdrSource` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primaryActor.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primaryActor.actingAs` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primaryActor.email` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primaryActor.nativeType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primaryActor.providerUniqueId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.externalId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.cloudAccount.cloudPlatform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.cloudAccount.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.cloudAccount.externalId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.cloudAccount.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primaryResource.nativeType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primaryResource.externalId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primaryResource.cloudAccount.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primaryResource.cloudAccount.cloudPlatform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`triggeringEventsCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mitreTactics` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mitreTechniques` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`trigger.type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`trigger.ruleId` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`trigger.ruleName` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`trigger.changedBy` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`issue.id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`triggeringEvent.id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`issue.status` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`triggeringEvent.status` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`issue.created` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`createdAt` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`resource.id` | `event.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`primaryResource.id` | `event.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`resource.name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`primaryResource.name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`resource.type` | `event.idm.read_only_udm.target.resource.type` | Mapped from changelog  
`primaryResource.type` | `event.idm.read_only_udm.target.resource.type` | Mapped from changelog  
`resource.subscriptionId` | `event.idm.read_only_udm.target.cloud.project.id` | Mapped from changelog  
`primaryResource.cloudAccount.externalId` | `event.idm.read_only_udm.target.cloud.project.id` | Mapped from changelog  
`resource.subscriptionName` | `event.idm.read_only_udm.target.cloud.project.name` | Mapped from changelog  
`primaryResource.cloudAccount.name` | `event.idm.read_only_udm.target.cloud.project.name` | Mapped from changelog  
`resource.region` | `event.idm.read_only_udm.target.asset.location.country_or_region` | Mapped from changelog  
`primaryResource.region` | `event.idm.read_only_udm.target.asset.location.country_or_region` | Mapped from changelog  
`resource.status` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`resource.cloudProviderURL` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`primaryResource.cloudProviderURL` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`control.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`risk` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`triggeringEvent.cloudPlatform` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`control.description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`control.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`issue.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`control.IssueURL` | `event.idm.read_only_udm.security_result.url_back_to_product` | Mapped from changelog  
`DetectionURL` | `event.idm.read_only_udm.security_result.url_back_to_product` | Mapped from changelog  
`threatId` | `event.idm.read_only_udm.security_result.threat_id` | Mapped from changelog  
`title` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`triggeringEvent.name` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`primaryActor.externalId` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`primaryActor.type` | `event.idm.read_only_udm.principal.resource.type` | Mapped from changelog  
`primaryActor.name` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`resource.nativeType` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`actor.type` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`resource.status` | `event.idm.read_only_udm.resource_obj.resource.attribute.labels` | Mapped from changelog  
`resource.region` | `event.idm.read_only_udm.target.location.country_or_region` | Mapped from changelog  
`resource.cloudProviderURL` | `event.idm.read_only_udm.resource_obj.url` | Mapped from changelog  
`triggeringEvent.actorIP` | `event.idm.read_only_udm.observer.ip` | Mapped from changelog  
`triggeringEvent.actor.id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`triggeringEvent.actor.name` | `event.idm.read_only_udm.about_obj.user.user_display_name` | Mapped from changelog  
`triggeringEvent.actor.type` | `event.idm.read_only_udm.about_obj.resource.type` | Mapped from changelog  
`triggeringEvent.actorIPMeta.country` | `event.idm.read_only_udm.principal.asset.location.country_or_region` | Mapped from changelog  
`triggeringEvent.actorIPMeta.reputation` | `event.idm.read_only_udm.principal.labels` | Mapped from changelog  
`triggeringEvent.actorIPMeta.reputationSource` | `event.idm.read_only_udm.principal.labels` | Mapped from changelog  
`triggeringEvent.actorIPMeta.autonomousSystemOrganization` | `event.idm.read_only_udm.principal.labels` | Mapped from changelog  
`triggeringEvent.actorIPMeta.autonomousSystemNumber` | `event.idm.read_only_udm.principal.labels` | Mapped from changelog  
`triggeringEvent.actorIPMeta.isForeign` | `event.idm.read_only_udm.principal.labels` | Mapped from changelog  
`triggeringEvent.category` | `event.idm.read_only_udm.about_obj.resource.attribute.labels` | Mapped from changelog  
`triggeringEvent.eventTime` | `event.idm.read_only_udm.about_obj.resource.attribute.labels` | Mapped from changelog  
`triggeringEvent.origin` | `event.idm.read_only_udm.about_obj.resource.attribute.labels` | Mapped from changelog  
`triggeringEvent.externalId` | `event.idm.read_only_udm.principal.resource.product_object_id` | Mapped from changelog  
`actor_name_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`actor_externalId_ip` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`record.trigger.source` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.cloudOrganizations` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.trigger.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.triggeringEventsCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.trigger.updatedFields` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.control.risks` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.resource.cloudPlatform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.control.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.DetectionURL` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.threatURL` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.tdrId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.tdrSource` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mitreTactic` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cloudAccounts.cloudPlatform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cloudAccounts.externalId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cloudAccounts.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cloudAccounts.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.PrimaryResource.cloudAccount.cloudPlatform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.PrimaryResource.externalId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.primaryResource.nativeType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.PrimaryResource.cloudAccount.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.PrimaryResource.providerUniqueId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.PrimaryResource.status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.PrimaryResource.VCSRepository` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.PrimaryResource.cloudOrganization` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.PrimaryResource.kubernetesNamespace` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.PrimaryResource.kubernetesCluster` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.trigger.ruleId` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`record.trigger.ruleName` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`record.trigger.changedBy` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`record.issue.id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`record.issue.status` | `event.idm.read_only_udm.security_result.alert_state` | Mapped from changelog  
`record.issue.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`record.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`record.issue.created` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`record.timeframe.start` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`record.resource.id` | `event.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`record.PrimaryResource.id` | `event.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`record.resource.name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`record.PrimaryResource.name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`record.resource.type` | `event.idm.read_only_udm.target.resource.type` | Mapped from changelog  
`record.PrimaryResource.type` | `event.idm.read_only_udm.target.resource.type` | Mapped from changelog  
`record.resource.subscriptionId` | `event.idm.read_only_udm.target.cloud.project.id` | Mapped from changelog  
`record.PrimaryResource.cloudAccount.externalId` | `event.idm.read_only_udm.target.cloud.project.id` | Mapped from changelog  
`record.resource.subscriptionName` | `event.idm.read_only_udm.target.cloud.project.name` | Mapped from changelog  
`record.PrimaryResource.cloudAccount.name` | `event.idm.read_only_udm.target.cloud.project.name` | Mapped from changelog  
`record.resource.region` | `event.idm.read_only_udm.target.asset.location.country_or_region` | Mapped from changelog  
`record.PrimaryResource.region` | `event.idm.read_only_udm.target.asset.location.country_or_region` | Mapped from changelog  
`record.resource.status` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`record.resource.cloudProviderURL` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`record.PrimaryResource.cloudProviderURL` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`record.control.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`record.issue.projects` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`triggeringEvent.actorIPMeta.category` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`record.control.description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`record.control.IssueURL` | `event.idm.read_only_udm.security_result.about.url` | Mapped from changelog  
`record.threatId` | `event.idm.read_only_udm.security_result.threat_id` | Mapped from changelog  
`record.title` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`record.description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`record.timeframe.end` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`act.externalId` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`pactor.externalId` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`triggeringEvents.actor.id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`createdAt` | `event.idm.read_only_udm.metadata.timestamp` | Mapped from changelog  
`entitySnapshot.tags.io.kubernetes.pod.uid` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`entitySnapshot.tags.io.kubernetes.pod.namespace` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`entitySnapshot.tags.io.kubernetes.container.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`entitySnapshot.tags.io.cri-containerd.kind` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`entitySnapshot.tags.io.kubernetes.pod.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`entitySnapshot.tags.maintainer` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`entitySnapshot.externalId` | `event.idm.read_only_udm.principal.group.product_object_id` | Mapped from changelog  
`actionParameters.clientID` | `event.idm.read_only_udm.principal.group.product_object_id` | Mapped from changelog  
`type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`entitySnapshot.tags.io.kubernetes.pod.namespace` | `event.idm.read_only_udm.principal.namespace` | Mapped from changelog  
`entitySnapshot.id` | `event.idm.read_only_udm.principal.asset_id` | Mapped from changelog  
`entitySnapshot.cloudPlatform` | `event.idm.read_only_udm.principal.cloud.vpc.name` | Mapped from changelog  
`entitySnapshot.providerId` | `event.idm.read_only_udm.principal.cloud.vpc.id` | Mapped from changelog  
`entitySnapshot.type` | `event.idm.read_only_udm.principal.cloud.project.id` | Mapped from changelog  
`entitySnapshot.nativeType` | `event.idm.read_only_udm.principal.cloud.project.resource_subtype` | Mapped from changelog  
`entitySnapshot.name` | `event.idm.read_only_udm.principal.cloud.project.name` | Mapped from changelog  
`entitySnapshot.status` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`updatedAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dueAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`statusChangedAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sourceRule.id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`control.name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`control.description` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`control.resolutionRecommendation` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`subcategories.title` | `event.idm.read_only_udm.security_result.category` | Mapped from changelog  
`subcategories.category.name` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`subcategories.category.framework.name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`actionParameters.userPoolType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`actionParameters.userpoolID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`actionParameters.clientID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`actionParameters.selection.preferences", "actionParameters.input.patch.portalVisitHistory.dateTime", and "actionParameters.input.patch.portalVisitHistory.type` | `additional.fields` | Mapped from changelog  
`actionParameters.input.patch.portalVisitHistory.name", "actionParameters.input.patch.portalVisitHistory.resourceName", "actionParameters.input.patch.portalVisitHistory.resourceType", "actionParameters.input.patch.portalVisitHistory.ruleType", and "actionParameters.input.patch.portalVisitHistory.id` | `principal.resource.attribute.labels` | Mapped from changelog  
`user.id` | `target.user.id` | Mapped from changelog  
`user.name` | `target.user.user_display_name` | Mapped from changelog  
`actionParameters.groups" and "actionParameters.products` | `security_result.detection_fields` | Mapped from changelog  
  
### Event mapping table

eventType from log | Old event_type | Current event_type  
---|---|---  
`if [eventType] == "user.session.end"` | `metadata.event_type` | `"USER_LOGOUT"`  
`if [eventType] in ["user.authentication.auth_via_AD_agent" , "user.authentication.auth_via_LDAP_agent"]` | `metadata.event_type` | `STATUS_UPDATE`  
`if [eventType] in ["user.authentication.auth_via_mfa", "user.authentication.sso", "user.session.start","user.session.access_admin_app"]` | `metadata.event_type` | `USER_LOGIN`  
`if [has_principal] == "true"` | `metadata.event_type` | `"STATUS_UPDATE"`  
`if [has_resource] == "true"` | `metadata.event_type` | `USER_RESOURCE_ACCESS`  
`if [has_user] == "true"` | `metadata.event_type` | `USER_UNCATEGORIZED`  
`if [has_user] == "true" and [action] == "Login"` | `metadata.event_type` | `"USER_LOGIN"`  
`if [has_user] == "true" and [action] == "Login"` | `event.idm.read_only_udm.extensions.auth.type` | `"AUTHTYPE_UNSPECIFIED"`  
`if [has_user] == "true" and [event][idm][read_only_udm][metadata][event_type] == "GENERIC_EVENT"` | `metadata.event_type` | `USER_UNCATEGORIZED`  
`else` | `metadata.event_type` | `GENERIC_EVENT`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wiz-io-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
