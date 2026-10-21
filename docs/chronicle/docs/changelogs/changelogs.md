---
url: https://docs.cloud.google.com/chronicle/docs/changelogs/changelogs/
title: Documentation changelog \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:09:31.228464+00:00
---

# Documentation changelog  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/changelogs/changelogs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Support ](https://docs.cloud.google.com/chronicle/docs/secops/release-notes)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Documentation changelog

This page tracks major updates to the Google SecOps documentation including new user guides, feature and parser updates.

## September 2026

Added a **Migrate SOAR integrations** section to the [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api) guide and its [API reference version](https://docs.cloud.google.com/chronicle/docs/reference/migrate-from-legacy-api-to-chronicle-api), explaining that Google SecOps SOAR integrations and connectors must also be migrated to the Chronicle API.

Updated the [Microsoft Defender for Endpoint default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint) to expand the `AdditionalFields` mapping reference, correct the `target.resource.resource_type` mapping to use the `properties.ActionType` log field, and add UDM mappings for Advanced Hunting fields, including `properties.ActionType` to `security_result.action`, `ProcessUniqueId` and `InitiatingProcessUniqueId` to `additional.fields`, and `MachineGroup` to `principal.asset.attribute.labels`.

Updated the [Microsoft 365 default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365) with new UDM mappings for common fields such as `Members.UPN`, Microsoft Teams and Power BI fields, and additional OneDrive, Azure Active Directory, Exchange, and Yammer operations such as `ManagedSyncClientAllowed` and `Remove-MigrationUser`.

Added the [Understand search syntax](https://docs.cloud.google.com/chronicle/docs/investigation/search-syntax-reference) page, covering data value formatting, string escaping, regular expressions, and key-value searches, and restructured the [Understand search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) and related investigation pages to reflect the SIEM Search page's **Alerts & Detections** and **Results** tabs.

Added security bulletin [GCP-2026-063](https://docs.cloud.google.com/chronicle/docs/security-bulletins#gcp-2026-063) to the Security bulletins page, describing a critical Improper Privilege Management vulnerability (`CVE-2026-15587`) in Google SecOps SOAR that was patched in version 6.3.85 and requires no customer action.

Updated the [Workday User Activity default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday-user-activity) to remove the Pre-GA notice, revise the Cloud Run function setup for Eventarc Pub/Sub triggers and Cloud Storage IAM permissions, and update the UDM mapping table and collector script, which now deduplicates events.

Updated the [Wiz integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/wiz) to clarify that the `API Root` and `Wiz API Root` parameters must use the regional GraphQL endpoint format `api.<region>.app.wiz.io/graphql` (or `.wiz.us` for Wiz for Gov), where the region is your Wiz data center, such as `us1` or `eu1`.

Updated the [Active Directory integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/active-directory) with rewritten prerequisites that cover network and DNS requirements (LDAP port `389` and LDAPS port `636`), creating a least-privilege service account, minimum required permissions per action, and delegating permissions on organizational units.

Standardized the Workload Identity steps across the Google Cloud and Google Workspace integrations, such as [Google Cloud API](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-api), [Gmail](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/gmail), and [Secret Manager](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/secret-manager), and corrected the step that grants the instance identity email the `roles/iam.serviceAccountTokenCreator` role on your service account.

Added the `chronicle.legacySoarUsers.get` permission to the required baseline permissions in the [Map SOAR permissions to IAM](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/map-soar-permissions-to-iam) page and aligned the minimum custom role permissions in the [Enable SOAR access](https://docs.cloud.google.com/chronicle/docs/secops/enable-soar-access) page, which now links to that baseline permissions list.

Updated the [Netskope web proxy default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-webproxy) to clarify the Cloud Storage setup, including the service account key format, VPC Service Controls ingress requirements, and the required Storage Legacy Bucket roles, and consolidated the UDM mapping tables into a single table.

Added IP allowlisting prerequisites by feed type to the [Feed Management](https://docs.cloud.google.com/chronicle/docs/administration/feed-management) and [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api) documentation, and domain allowlisting guidance for push-based ingestion to the [ingestion methods](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) and [Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api) references.

Updated the [ArcSight integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/arcsight) to list the permissions required by the integration, and reworked the Security Events Connector prerequisites and shared folder configuration content.

Added documentation for general quantified comparisons to the GoogleSQL [Operators reference](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/operators#general_quantified_comparisons), covering the `ANY`, `SOME`, and `ALL` quantifiers with standard comparison operators, their semantic rules, and examples, and added a [general quantified comparison subqueries](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/subqueries#general_quantified_comparison_subquery_concepts) section to the Subqueries reference.

Updated the [Akamai SIEM Connector default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-siem-connector) to remove duplicated steps and code blocks, improve error handling in the Cloud Run and AWS Lambda samples, and clarify the Eventarc trigger configuration and Cloud Storage permissions.

Updated the [Proofpoint TAP Threats default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-tap-threats) to clarify that the `PROOFPOINT_TAP_THREATS` log type ingests Threat API summaries rather than SIEM API events, and revised the Cloud Run collection function, setup steps, and UDM mappings accordingly.

Updated the [Chronicle API reference](https://docs.cloud.google.com/chronicle/docs/reference/rest) across the v1, v1beta, and v1alpha versions, adding the [`ObjectAccessMetadata`](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/ObjectAccessMetadata) type returned for dashboards and search queries, the `caseObjectRbacSettings` field on [cases](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases), the `expand` query parameter for case wall records, and the `AZURE_BLOBSTORE_EVENT_DRIVEN` feed source type.

Updated the [UDM search documentation](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) and the [service limits page](https://docs.cloud.google.com/chronicle/docs/reference/service-limits) with the new way to set the maximum number of search results (**Settings** next to **Run search** , then **Maximum Results**), and corrected the default value to 30,000.

Updated the GoogleSQL [date](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/date_functions), [datetime](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/datetime_functions), [time](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/time_functions), [timestamp](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/timestamp_functions), and [array](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/array_functions) function references to use `step_size` and `step_unit` as the `INTERVAL` parameters of functions such as `DATE_ADD` and `TIMESTAMP_SUB`, and clarified the maximum array size limit for `GENERATE_DATE_ARRAY`.

Added the [Integrate your own threat intelligence feeds](https://docs.cloud.google.com/chronicle/docs/detection/integrate-threat-intel-feeds) guide, which explains how to ingest custom or third-party IoC feeds such as MISP and STIX/TAXII into the Entity Context Graph and use them for IoC matching and YARA-L rules.

Added the [MSSP multi-tenant operations](https://docs.cloud.google.com/chronicle/docs/secops/mssp-multi-tenant-operations) guide, which explains how managed security service providers use Federated Search to configure instance groups and run UDM and statistical queries across multiple managed Google SecOps instances, including the required `federationAdmin` and `federationViewer` IAM roles.

Updated the [Windows AppLocker default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-applocker) with two new ingestion methods, NXLog forwarding to a Bindplane agent (`WINDOWS_APPLOCKER`) and direct Bindplane agent channel reads (`WINEVTLOG`), plus Linux installation steps and an updated UDM mapping table, and removed the Pre-GA notice.

Published reference pages for the Chronicle API v1beta SearchService, covering the [`instances.search` method](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/search) and the [`searchSessions.searchedResults.list` method](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.searchSessions.searchedResults/list), and regenerated the related v1, v1alpha, and v1beta pages of the [REST API reference](https://docs.cloud.google.com/chronicle/docs/reference/rest) with updated methods, resources, and shared types.

Added the [Re-parse historical data (Log Replay)](https://docs.cloud.google.com/chronicle/docs/event-processing/reparse-historical-data) page, which explains how to request re-parsing of up to 180 days of historical logs, and added notes to the [parser syntax reference](https://docs.cloud.google.com/chronicle/docs/reference/parser-syntax) and related pages distinguishing parser syntax from YARA-L rules and clarifying `drop {}` filter behavior.

Updated the [Siemplify integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify) to document the new **Attach Playbook to Case** action, including its required `Playbook Name` parameter, output messages, and script result.

Updated the [Palo Alto Cortex XDR integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-cortex-xdr) with a new action parameter and JSON result example, and restructured the page with a **Before you begin** section and standardized action input and output tables.

Updated the [Microsoft Graph Mail](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-graph-mail) and [Microsoft Graph Mail Delegated](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-graph-mail-delegated) integration documentation with new S/MIME parameters for the Send Mail action, such as `Base64 Encoded Recipient Certificate`, an S/MIME configuration quick reference, commands to convert certificate files to Base64, and new connector parameters.

Updated the [CyberArk PAM integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberark-pam) with the new **Sync Integration Credentials Job** , which synchronizes CyberArk PAM account credentials into Google SecOps SOAR integration instances, connectors, and jobs, marked the `Verify SSL` parameter as optional, and listed CyberArk PAM among the [supported secret managers](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/working-with-an-external-vault-system).

Updated the [Amazon EC2](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-elastic-compute-cloud-ec2), [AWS IAM](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-iam), and [AWS S3](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-s3) integration documentation with network and authentication prerequisites and tables of the minimum AWS IAM permissions required for each action, such as `ec2:DescribeRegions`, `iam:GetAccountSummary`, and `s3:ListAllMyBuckets`.

Updated the [Microsoft 365 Defender integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-365-defender) with the new `Sync Direction` and `Closed Reason Mapping` parameters for Sync Alerts, which control the direction of status and comment synchronization and map Google SecOps closure reasons to Microsoft Defender XDR classifications and determinations.

Updated the relative time range operator labels in the [UDM search documentation](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#relative_time_range) to match the current UI: **Past (rolling)** , **Previous (completed)** , and **Current (to date)**.

Added the [Visualize data flows with Sankey charts](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts-sankey) guide, which covers use cases, data requirements, configuration steps, and sample YARA-L 2.0 queries, and added a [Sankey chart](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts#sankey_chart) section to the Manage charts in dashboards page and a corresponding entry to the [use cases](https://docs.cloud.google.com/chronicle/docs/use-cases) list.

Updated the [MuleSoft Anypoint ingestion documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mulesoft-anypoint) to create the Cloud Run function with an Eventarc Pub/Sub trigger, change the Cloud Scheduler job frequency from daily to hourly, and clarify the Google SecOps feed configuration steps and required Cloud Storage IAM roles.

Added an **Out-of-the-box dashboards catalog** section to the [Curated queries overview](https://docs.cloud.google.com/chronicle/docs/reports/native-curated-dashboards), listing predefined dashboards by data source such as Entities, IoC matches, Ingestion metrics, Rules and detections, and SOAR cases, and linked each dashboard in the [Common curated dashboards overview](https://docs.cloud.google.com/chronicle/docs/reports/native-curated-dashboards-overview) to its widget queries.

Updated the [Proofpoint TAP alerts default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail) with restructured and expanded UDM mapping tables, and clarified the `quarantineFolder` mapping descriptions in the mapping delta table.

Updated the [Microsoft Intune Context default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune-context) so that the Microsoft Intune diagnostic settings steps select only the **AuditLogs** category, removing **OperationalLogs** , **DeviceComplianceOrg** , and **Devices** because the `AZURE_MDM_INTUNE_CONTEXT` parser supports only audit logs.

Updated the [Microsoft IIS default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iis) with a revised UDM mapping table and a new mapping delta table for the parser version released on July 16, 2026, which compares old and current mappings (for example, HTTP transactions now use `NETWORK_HTTP` instead of `USER_LOGIN`).

Added the [Authenticate Remote Agent with Workload Identity Federation](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/authenticate-remote-agent-with-workload-identity-federation) guide, which explains how to configure keyless authentication for Google SecOps SOAR remote agents (version 2.6.2 or later) on AWS, Azure, Kubernetes, CI/CD pipelines, and other identity providers.

Updated the [ChromeOS XDR default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chromeos-xdr) to use Pub/Sub push feeds instead of the deprecated Ingestion API, adding steps for project binding, topic and push subscription setup, publisher IAM permissions, and Google Admin console provider configuration, and refreshed the UDM field mapping table.

Updated the [Palo Alto Prisma Cloud alert default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-ca) with a consolidated UDM mapping table and a mapping delta reference for the September 15, 2026 parser release, which moves aggregated alert and audit fields such as `aggregatedAlerts.host` and `audits.command` from `principal` to `about`.

Updated the [VMware vCenter default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vcenter) with a restructured UDM mapping table and a mapping delta for the September 15, 2026 parser release, which remaps `appname` to `principal.application` and `username` to `principal.user.userid` and adds mappings for previously unmapped fields such as `syslog_host`.

Updated the [Microsoft Windows Event default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/winevtlog#event-id-8002) with UDM field mappings for Event ID `8002`.

Updated the [Snowflake ingestion documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snowflake) to add Cloud Storage V2 as the recommended ingestion method alongside Amazon S3 V2, with steps for granting access to `SNOWFLAKE.ACCOUNT_USAGE` views, creating storage integrations, and scheduling tasks that unload `LOGIN_HISTORY` and `QUERY_HISTORY` data.

Updated the [GitHub audit logs default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/github) to specify the Cloud Storage IAM roles that the Google SecOps service account needs: `roles/storage.objectViewer` plus `roles/storage.legacyBucketReader` or `roles/storage.legacyBucketWriter`, depending on the source deletion option.

Added the [Translate YARA-L 2.0 Search queries to GoogleSQL](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/yara-l-google-sql-translate) page, which maps YARA-L Search concepts such as single-event and multi-event searches, tumbling and sliding time windows, and repeated fields to their GoogleSQL equivalents, with example query translations.

Added the [Get started with GoogleSQL](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/getting-started-googlesql) page, which introduces GoogleSQL as an alternative to YARA-L 2.0 for querying Google SecOps data, covering structural differences, the `events`, `graph`, `detections`, `cases`, and `case_history` tables, and how statistical and event queries affect the interactive interface widgets.

Added the GoogleSQL reference documentation for Google SecOps, including the [query syntax](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/query-syntax) and [data types](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/data-types) pages and an [alphabetical function list](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/functions-all), plus reference pages for operators, conditional expressions, arrays, subqueries, and pipe query syntax.

Clarified in the [Understand search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) documentation that the maximum search window is 365 days for YARA-L 2.0 searches and 90 days for GoogleSQL searches.

Added the [Data encryption at rest and in transit](https://docs.cloud.google.com/chronicle/docs/secops/data-encryption) page, which explains how Google SecOps protects customer data with default AES-256 encryption at rest and TLS encryption in transit, and describes the requirements and limitations for using customer-managed encryption keys (CMEK) with Cloud KMS.

Updated the [Oracle NetSuite default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-netsuite) and collection script to add the required System Notes permissions, improve Cloud Storage state file handling, and deduplicate audit log records across poll intervals.

Added a **Detect threats with Curated Rules** section to the [BYOL Threat Intelligence integration documentation](https://docs.cloud.google.com/chronicle/docs/detection/gti-byol) with steps to enable the prebuilt Google Threat Intelligence (BYOL) rule set, and listed that rule set and its `GCP_THREATINTEL` log type in the [third-party vendor alerts category](https://docs.cloud.google.com/chronicle/docs/detection/third-party-vendor-alerts-category) documentation.

Updated the [Trend Vision One integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-vision-one) to mark the `Description` parameter as required for the endpoint isolation and unisolation actions, document its default values, and refresh the example action output.

Added the [Mandiant Recommended rules](https://docs.cloud.google.com/chronicle/docs/detection/mandiant-recommended) page, which explains how to subscribe to the `google.mandiant.recommended` tag to automatically deploy a curated, quota-free detection baseline built on composite detections and Applied Threat Intelligence, and added the corresponding curated saved view to the [unified rules guide](https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/get-started).

Corrected the casing of the `dateFormat` function in the [Expression Builder documentation](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder), clarified that it standardizes dates to the `YYYY-MM-DD hh:mm:ss` format, and added the list of supported pattern tokens for year, month, day, time, time zone, and AM/PM.

Added the [LegacySearchCuratedDetections](https://docs.cloud.google.com/chronicle/docs/reference/parity/curatedRule/legacy-search-curated-detections) and [ListCuratedRules](https://docs.cloud.google.com/chronicle/docs/reference/parity/curatedRule/list-curated-rules) API parity mapping pages, which detail the field-by-field request and response mappings and key differences for migrating from the legacy Backstory Rules Engine `ListCuratedRuleDetections` and `ListCuratedRules` methods to the Chronicle API.

Updated the [Google Chronicle integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chronicle) with the new **Is Value In Data Table Async** action, which asynchronously checks whether values exist in a data table, including its input parameters, JSON result example, and output messages.

Updated the [Splunk integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/splunk) with a refactored prerequisites section that clarifies the push-based and pull-based methods for ingesting Splunk cases and the permissions each requires, and retitled the page to Integrate Splunk with Google SecOps.

Clarified in the [feed management documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management) that enabling and disabling feeds is equivalent to resuming and pausing them, and added a section on backfillability that explains data recovery for pull-based versus push-based feeds, the 90-day internal buffer, and backfill rate limits.

Added a network access and domain allowlist section to the [Log in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui) page, listing the mandatory Google SecOps and SOAR domains (such as `*.backstory.chronicle.security` and `*-chronicle.googleapis.com`), required Google infrastructure domains, and optional telemetry domains to allow through egress firewalls and corporate proxies.

Updated the [Imperva WAF default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-waf) with a new ingestion method that uses the Imperva Generic HTTP Push Connector (Beta) to stream logs to a Google SecOps webhook feed, including setup steps, authentication header requirements, and the architectural limitations to consider.

Added a Data Pipeline Management (DPM) metrics schema section to the [ingestion metrics table reference](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-metrics-schema), documenting the pipeline byte and log count metrics, such as `/ingested_bytes_count` and `/emitted_log_count`, the `/processing_latencies` metric, and their `pipeline_id` and `processor_id` fields.

Added API feed reference sections for the `TRELLIX_HX_ALERTS`, `TRELLIX_HX_AUDIT`, and `TRELLIX_HX_HOSTS` log types to the [feed management API documentation](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api), including prerequisites, type-specific request fields, and sample create feed requests.

Updated the [ServiceNow integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/servicenow) with revised authentication requirements for the Sync Incidents job and corrected the formatting of parameter and output tables throughout the page.

Updated the [Cloud Armor](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-armor), [Compute Engine](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-compute), [IAM](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-iam), [BigQuery](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-big-query), and [Google Alert Center](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-alert-center) integration documentation with restructured **Before you begin** sections that list each integration's prerequisites, such as creating a service account and choosing between Workload Identity (recommended) and a JSON key for authentication.

Updated the [Google Chronicle integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chronicle) with the new **Execute UDM Query Async** action and its parameters, such as `Query`, `Time Frame`, and `Max Results To Return`, and added a note about UDM search rate limits to the Execute UDM Query action.

Updated the [Case playbooks overview](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/case-playbooks), [Use reaction triggers in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-reaction-triggers-in-playbooks), and [Manage playbook triggers](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-triggers-in-playbooks) pages for the public preview of case playbooks and reaction triggers, adding manual case-scope actions, the reaction chain limit, and simulator testing, and documented how to attach case-scoped playbooks when you [create a case manually](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-manual-case).

Added a Set up a Custom API feed section to the [feed management documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management), introducing Custom API feeds (Codeless Connectors), a Preview feature, with configuration steps, supported authentication methods, sequential and parent-child connector models with sample JSON, and troubleshooting guidance.

Added the total and multi-event custom rule quotas for the Standard, Enterprise, and Enterprise Plus packages to the [Understand rule quotas](https://docs.cloud.google.com/chronicle/docs/detection/rule-quotas) and [Service limits](https://docs.cloud.google.com/chronicle/docs/reference/service-limits) pages, and merged the former Rules capacity reference into Understand rule quotas as a new Curated detections capacity section.

Added a **Context-aware analytics** section to the [YARA-L rule examples documentation](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples) with rules that match file hashes, IP addresses, domains, and URLs against IoC feeds, including Tor exit node detection.

Updated the [Recommended Google Unified Security products](https://docs.cloud.google.com/chronicle/docs/secops/google-unified-security-recommended) page to add the Exabeam, Proofpoint Targeted Attack Protection (TAP), and SentinelOne Singularity Endpoint partner integrations and to revise the categories of existing partners such as CrowdStrike, Palo Alto Networks, and Fortinet.

Corrected the outcome variable syntax in the [composite detection rules documentation](https://docs.cloud.google.com/chronicle/docs/yara-l/composite-detection-rules) and its examples to use `detection.detection.variables["NAME"].string_val` instead of `detection.detection.outcomes["NAME"]`.

Updated the [Enable SOAR access](https://docs.cloud.google.com/chronicle/docs/secops/enable-soar-access) documentation with ten newly required IAM permissions, including `chronicle.instances.generateSoarAuthJwt`, `chronicle.socRoles.get`, `chronicle.integrations.get`, and `chronicle.environmentGroups.get`.

Clarified in the [feed management documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management) and the [feed management API reference](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api) that you can obtain the Google SecOps service account for Cloud Storage feeds either in the Google SecOps console or programmatically with the `fetchFeedServiceAccount` method, and cross-referenced the two guides.

Updated the [Pub/Sub](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/pubsub), [Vertex AI](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vertex-ai), [Google Kubernetes Engine](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-gke), and [Policy Intelligence](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-policy-intelligence) integration documentation with restructured prerequisite sections that cover service account creation, the required IAM roles, and Workload Identity (recommended) or JSON key authentication, plus refreshed use cases.

Updated the [Cloud Logging](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cloud-logging), [Gmail](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/gmail), [Web Risk](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/web-risk), and [GRR Rapid Response](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-rapid-response-grr) integration documentation with use cases and expanded prerequisite sections that cover service account creation and Workload Identity (recommended) or JSON key authentication, and made minor wording fixes to the [Google Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-threat-intelligence) integration documentation.

Updated the [Chrome Enterprise ingestion documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-management#check-off-events) with a new **Check off events in Event Reporting** section that explains how to select the event types to ingest in the Google Admin console and confirm that the `OnSecurityEventEnterpriseConnector` policy is enabled.

Added July and August 2026 entries to the change logs of more than 90 default parsers listed on the [supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers) page, covering new and corrected UDM field mappings and newly supported log formats, and added a change log for the [IBM Informix default parser](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/informix).

Updated the [UDM field dictionary reference](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#Metadata.ProductLogLevel) with the new `metadata.product_log_level` field and its `Metadata.ProductLogLevel` enum, and the new `working_directory` string field for process-related fields.

Updated the [Tools power-up documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/tools) to recommend the **Close Cases Based On Search** job for closing more than 50 cases, clarify how to retrieve the `Search Payload` from the `CaseSearchEverything` API call, and document the new **Tag Untouched Cases** job.

Clarified the example Chronicle API root in the [Google Chronicle integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chronicle) by using the `{api_root}`, `{project_id}`, `{location}`, and `{customer_id}` placeholder variables.

Added a **Reaction trigger priority** section to the [Use reaction triggers in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-reaction-triggers-in-playbooks) documentation, explaining execution order when multiple playbooks match an event, and noted there and in the [Case playbooks overview](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/case-playbooks) that these playbook executions are excluded from Legacy Monitoring dashboards and SOAR data exports.

Updated the [Wiz integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/wiz) to clarify that the Wiz and Google SecOps Bi-directional Sync Job only processes Google SecOps cases that have the `Wiz` tag.

Added the [Upgrade cloud storage data feeds to the v2 connector framework](https://docs.cloud.google.com/chronicle/docs/administration/upgrade-data-feeds-v2) guide, covering the migration milestones for Cloud Storage, Amazon S3, Amazon SQS, and Azure feeds and updated the v1 end-of-support date to October 1, 2026.

Updated the [Applied Threat Intelligence curated detections](https://docs.cloud.google.com/chronicle/docs/detection/ati-curated-detections), [Fusion Feed](https://docs.cloud.google.com/chronicle/docs/detection/ati-fusion-feed), and related pages to reflect the migration of Mandiant Threat Intelligence feeds to Google Threat Intelligence, removed `MANDIANT_FUSION_IOC` from the Fusion Feed rule example, and added Google Threat Intelligence feeds to the [Google SecOps packages overview](https://docs.cloud.google.com/chronicle/docs/secops/secops-packages).

Updated the [Palo Alto Next Gen Firewall integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-next-gen-firewall) to standardize references to the required PAN-OS custom administrator role in the **Before you begin** and integration-level permissions sections.

Added the [Supported compliance standards](https://docs.cloud.google.com/chronicle/docs/secops/compliance) page, which covers Google SecOps data residency boundaries (DRZ), FedRAMP and DoD impact levels, HIPAA and PCI DSS compliance, and CMEK and VPC Service Controls.

Added a **Field dependencies** section to the [Risk Analytics for UEBA documentation](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-ueba-category) with tables that map each metric (for example, `AUTH_ATTEMPTS_FAIL` and `DNS_BYTES_OUTBOUND`) to the UDM search query defining its contributing events, and list the UDM field options for each dimension.

## August 2026

Updated the [parser reference documentation](https://docs.cloud.google.com/chronicle/docs/reference/parser-syntax) with additional information about Grok and JSON filters, and usage best practices.

Updated the [F5 ASM default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-asm) with UDM mapping table and CSV log mappings.

Updated the [Bindplane agent documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent) with Chronicle Ingestion API network prerequisites.

Updated the [parser syntax reference documentation](https://docs.cloud.google.com/chronicle/docs/event-processing/parser-tips-troubleshooting) with information about the Grok `match_all` option that allows for extracting all non-overlapping occurrences of a pattern within a field.

Updated the [BeyondTrust Endpoint Privilege Management default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-endpoint) and collector script.

Added documentation for the new [Threat Hunt Agent](https://docs.cloud.google.com/chronicle/docs/detection/threat-hunt-agent).

Windows DNS mapping delta. For details, see the [Microsoft Windows DNS default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-dns).

Updated the [Tenable Audit default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tenable-audit) and collector script.

Updated the [timestamp documentation](https://docs.cloud.google.com/chronicle/docs/detection/timestamp-definitions) to clarify the distinction between collection and ingestion latencies.

Updated the [1Password audit events default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword-audit-events) and collector script.

Added a new entry to the [Troubleshoot ingestion issues documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/troubleshooting-ingestion) for the 206 Partial Content (REMOTE_SERVER_ERROR) status code.

Added a section of nested fields from `AdditionalFields` raw log fields for `EntityType Process` within `AlertEvidence` and `DeviceEvent` categories in the [Microsoft Defender for Endpoint default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint).

Added Google Vault to Workspace [Google Workspace activity ingestion documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workspace-activity).

Added [a deprecation notice](https://docs.cloud.google.com/chronicle/docs/deprecations) for Mandiant legacy feeds. The feeds for MANDIANT_ACTIVE_BREACH_IOC, MANDIANT_FUSION_IOC, and OPEN_SOURCE_INTEL_IOC are being deprecated and will be replaced by the GTI_IOC feed, effective March 18, 2027.

Added documentation on configuring the Google SecOps MCP server with Antigravity and Gemini Enterprise. For details, see [Configure MCP](https://docs.cloud.google.com/chronicle/docs/secops/use-google-secops-mcp).

Updated [Chronicle Tenant API reference documentation](https://docs.cloud.google.com/chronicle/docs/reference/rest) for v1alpha and v1beta.

Updated the Google SecOps ingestion [pipeline documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline) to include the Unroll processor.

Updated the [Bindplane Enterprise documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent) to include details about the Enterprise tier and self-service license downloads.

Added supported log formats and sample logs to the [Zscaler CASB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-casb) and [Zscaler Deception](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-deception) default parser documentation.

Added supported log formats and sample logs to the [Jamf Telemetry V2 default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-telemetry-v2).

Updated log format and sample log for the [AWS EC2 Instance default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ec2-instances).

Updated the [alert suppression and rule exclusions documentation](https://docs.cloud.google.com/chronicle/docs/investigation/alert-suppression) to clarify that UDM-field exclusions are evaluated against raw events and don't apply directly to composite rules.

Updated the [SAP BTP default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-btp) and collector script.

Updated the [BeyondTrust Endpoint Privilege Management (EPM) default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-endpoint).

Updated the [Rubrik Security Cloud ingestion documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rubrik-security-cloud) to use the correct `v1alpha` endpoint and query parameters for authentication.

Added a new guide for the [Microsoft Defender for Office 365 default parser](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-mail).

Updated the [Thinkst Canary default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/thinkst-canary) to reflect the latest setup procedures and parser mappings.

Updated the [Analyze feed activity with Cloud Logging guide](https://docs.cloud.google.com/chronicle/docs/ingestion/analyze-feed-activity-with-cloud-logging) to highlight that a Bring Your Own Project (BYOP) configuration is a requirement for analyzing feed activity with Cloud Logging.

Updated the [SOAR and detection schema documentation](https://docs.cloud.google.com/chronicle/docs/reference/soar-data-dashboard) to cover both dashboards and search and clarify that SOAR data (cases, alerts, case history) and detection schemas apply to both dashboards and SIEM Search.

Updated the [search documentation](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-detections-in-search) to reflect that the maximum result limit for statistical searches has increased from 10,000 to 100,000 for the UI and long-running operation API.

Added the Log Field, UDM Mapping, and Logic table headers to the UDM mapping tables in the [Cisco Firepower NGFW](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-firepower-firewall), [GitHub audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/github), and [Okta parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta).

Updated the [Health Hub documentation](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard) to include latency monitoring and troubleshooting.

Updated the [Proofpoint Secure Email Relay default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-ser) to describe aggregated usage and throughput reporting, clarifying that the Proofpoint SER Reporting API does not expose per-message details like subjects or recipients.

Updated the [Microsoft Entra ID default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad) with information details on log collection methods, permissions, and mappings.

Added a new guide for [Simsafe Threat Simulation](https://docs.cloud.google.com/chronicle/docs/secops/event-simulation). 

Updated the [Analyze ingestion with Cloud Monitoring](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics) guide to provide more accurate descriptions for special collector IDs.

Updated the [secret management documentation](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/working-with-an-external-vault-system) to detail the new method for managing secrets using secret managers and the Sync Integration Credentials job instead of the deprecated vaults method.

Added a new guide for the [Detection Engineering Agent](https://docs.cloud.google.com/chronicle/docs/secops/agentic-detection-engineering).

Updated the following documentation with dashboard limitations, SOAR data source constraints, and report security details.

  * [Apply joins in search and dashboards](https://docs.cloud.google.com/chronicle/docs/investigation/search-joins)
  * [YARA-L 2.0 dashboard query library](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard)
  * [SOAR data foundations for dashboards and search](https://docs.cloud.google.com/chronicle/docs/reference/soar-data-dashboard)
  * [SIEM dashboard overview](https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview)
  * [Manage charts in dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts)
  * [Configure dashboard filters](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters)
  * [Configure scheduled reports](https://docs.cloud.google.com/chronicle/docs/reports/scheduled-email-reports)



Updated the [Fortinet firewall default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-firewall).

Updated the [Investigation and Case Management overview documentation](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/investigation-management-overview) to include details about the new side-by-side view capability added to the **Alerts and Detections** tab in the **Cases** page.

Updated the [UDM search documentation](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) to document changes to how relative time filters calculate data ranges.

Added a VPC Service Controls step to the [Google SecOps onboarding documentation](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud).

Updated the list of high-performance UDM fields recommended for query filters in the [UDM search best practices guide](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-best-practices).

Updated the [Remote Agent troubleshooting guide](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting) for DNS networking and image pulling.

Updated the [VPCSC documentation](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops) to include a new VPC-SC ingress rule for the Case Management service to access Traffic Director on the BYOP.

Updated references from Google Threat Intelligence Enterprise to Google Threat Intelligence Enterprise Plus in the [Google SecOps packages documentation](https://docs.cloud.google.com/chronicle/docs/secops/secops-packages) to reflect current product naming and availability.

Updated the deprecation date for Mandiant legacy feeds (MANDIANT_ACTIVE_BREACH_IOC, MANDIANT_FUSION_IOC, and OPEN_SOURCE_INTEL_IOC) from March 18, 2026 to September 14, 2026 in the [deprecations documentation](https://docs.cloud.google.com/chronicle/docs/deprecations). The shutdown date remains unchanged.

Standardized the SOAR service account and group mapping instructions across the following administration and migration documentation to match the latest UI fields.

  * [Authentication reference](https://docs.cloud.google.com/chronicle/docs/reference/authentication)
  * [Migrate to Chronicle API](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/api-migration-guide)
  * [SOAR migration overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp)
  * [Map users with Cloud Identity](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party)
  * [Map users with third-party identity](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform)
  * [Migrate remote agent authentication infrastructure](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/migrate-remote-agent-to-google)



Updated the [Dashboards and charts documentation](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts) to include the chart library feature.

Updated the [UDM search documentation](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) to include UDM Lookup search, matching behavior, and field coverage boundaries.

Removed the obsolete limitations regarding Chronicle API search query and operation support from the [data tables investigation](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables) and [service limits reference](https://docs.cloud.google.com/chronicle/docs/reference/service-limits) documentation.

Updated the [Event Simulation documentation](https://docs.cloud.google.com/chronicle/docs/secops/event-simulation) with API, proto, and architecture fixes.

Updated the supported entity context log types in the [Ingestion data types documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/data-types) by replacing the high-level categorized list of sources with a comprehensive list of specific entity context log type identifiers for ingestion configuration.

Updated the [PAN Cortex XDR Events default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-cortex-xdr-events) with instructions to prevent an infinite rsync ingestion loop and quota exhaustion.

Updated the [Ingest Google Cloud logs documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs) to add `networkmanagement.googleapis.com/vpc_flows` to the list of supported log IDs under the `GCP_VPC_FLOW` log type.

Standardized log type naming conventions and feed configurations for the [Microsoft Azure Activity and Azure AD Directory Audit default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-activity).

Updated the example Trellix HX Endpoint URL across trellix-hx-alerts, trellix-hx-hosts, and trellix-hx-audit feed setup instructions in the default parser documentation for [Trellix Endpoint Security (HX) Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-alerts), [Trellix Endpoint Security (HX) Bulk Acquisition Result Packages](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-audit), and [Trellix Endpoint Security (HX) Host Inventory](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-hosts).

Updated the [Triage and Investigation (TIN) Agent documentation](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent) to clarify that it supports single-tenant configurations as well as MSSP customers with a single SOAR tenant connected to multiple SIEM tenants.

Consolidated, restructured, and updated the [Rule execution frequency and scheduling documentation](https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency).

Added a new [Google SecOps architecture overview page](https://docs.cloud.google.com/chronicle/docs/secops/secops-architecture) to provide a unified technical explanation of how the platform handles security telemetry from ingestion to automated response.

## July 2026

Updated the [Stream data with advanced BigQuery export](https://docs.cloud.google.com/chronicle/docs/reports/bigquery-export) documentation with new features and removed limitations.

Added and updated mappings for the [Microsoft 365 default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365).

Added `curl` command examples with fully formatted requests to the [SIEM HTTPS webhook documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/setup-siem-webhook).

Updated the [Proofpoint PS ](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/proofpoint-ps) documentation for the Marketplace 36.5 release.

Added CMEK feature availability, compliance status table, and performance details to the [Google SecOps CMEK documentation](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops).

Updated the [Security Tokens documentation](https://docs.cloud.google.com/chronicle/docs/agentic-soc/security-tokens).

Updated the [Remote agent authentication infrastructure migration](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/migrate-remote-agent-to-google) documentation to include a note about avoiding API rate limit issues.

Updated the [Palo Alto Networks IOC ingestion documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-ioc) to use STIX/TAXII, deprecating the legacy PAN_IOC/AutoFocus method.

Removed `target.hostname` and `target.asset.hostname` mappings for TRAFFIC events from the [Palo Alto Networks firewall default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-firewall).

Added a new [Control access to 1P cases and alerts](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-impact-cases) guide explaining how to use data RBAC to only view cases and alerts in your assigned data scopes.

Updated the [Data RBAC impact on features overview](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-impact) page.

Added Mandiant legacy IOC feed deprecations (shutdown March 18, 2027) to the [Product deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations) page.

Added instructions for verifying migration success to the [SOAR migration guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp) and updated the [FAQ](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-faq).

Added a new guide explaining how to use API to [Bypass Log Validation for parser extensions and custom parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/bypass-log-validations).

Updated the [Timestamp definitions](https://docs.cloud.google.com/chronicle/docs/detection/timestamp-definitions) guide to include details on indexing latency, data availability timestamps, and how to monitor for processing delays.

Updated the [Ingest data with API connectors](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api) and [Understand data availability for search](https://docs.cloud.google.com/chronicle/docs/investigation/expected-data-availability-for-search) documentation to include data delays for existing log types.

Updated the [Ingest data with API connectors](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api) guide to include details on SQSv2 message ACks functionality.

Added the Legacy SIEM APIs deprecation information to the [Product deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations) page.

Added a note on the [Configure enrichment](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment) guide with information on using specific permissions if you use custom roles.

Added `FindingsRefinement` and `FindingsRefinementDeployment` resources to the [Terraform documentation](https://docs.cloud.google.com/chronicle/docs/terraform).

Added Data Tables API rate limits (QPM) quotas to the [Search data tables guide](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables).

Fixed Bindplane configuration example in the [Windows DNS ETW default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-dns).

Added [webhook JSON schema documentation](https://docs.cloud.google.com/chronicle/docs/soar/ingest/webhooks/setting-up-a-webhook) for ingesting alerts into Google SecOps.

Refined [Unified Rules documentation](https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/get-started), adding Data RBAC requirements, troubleshooting common errors, and describing default Saved Views.

Added documentation for Advanced Filtering capabilities in dashboards. For details, see [Configure dashboard filters](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters).

Updated deprecation details and key dates for Legacy Backstory and Ingestion APIs to the [Product deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations) page.

Added a note that certain scripts are provided as examples and not officially supported in the default parser documentation for: [OneLogin by One Identity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onelogin-sso), [Armis Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-alerts), [Duo administrator](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-admin), [Citrix Monitor Service](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-monitor), [Box JSON](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/box), [Armis Devices](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-devices) and [Armis Activities](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-activities).

Clarified behavior of key columns with repeated fields in data tables. For details, see [Search data tables](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables).

Updated permissions for Bindplane in the [Manage data processing pipelines](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline) guide.

Added a guide for monitoring and troubleshooting ingestion pipelines using Cloud Logging - [Analyze feed activity with Cloud Logging](https://docs.cloud.google.com/chronicle/docs/ingestion/analyze-feed-activity-with-cloud-logging).

Update the [Understand the rules dashboard page](https://docs.cloud.google.com/chronicle/docs/detection/view-all-rules) to reflect the latest UI.

Added [migration guide](https://docs.cloud.google.com/chronicle/docs/administration/migrate-legacy-siem-infra) and mapping table for transitioning from legacy SIEM APIs to the Chronicle API. For details, see: [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api), [Google SecOps APIs and libraries overview](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview), [Product deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations) and [SIEM API endpoint mapping](https://docs.cloud.google.com/chronicle/docs/administration/siem-endpoint-mapping-table).

Added AI-related fields and types (for example, AiType, EntityType for AI) to the [UDM field dictionary reference](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list).

Updated the field mapping in the [Google Workspace default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workspace-activity) with new events, restructured tables, and removed deprecated label fields.

Updated [Jamf Pro Context default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-pro-context) and the Cloud Run function to improve performance and data handling.

Updated feed migration details in the [Migrate a Google SecOps instance to a BYOP project](https://docs.cloud.google.com/chronicle/docs/administration/migrate-instance-from-one-project-to-another) guide.

Updated the [Azure AD Context default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-context).

Updated [CMEK key rotation guidance](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops) and [SOAR migration checks](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp).

Added Redirect URIs section to the [Use Google SecOps MCP](https://docs.cloud.google.com/chronicle/docs/secops/use-google-secops-mcp) documentation.

Updated Cloud Audit Log field mappings in documentation with new UDM mappings. For details, see [Collect Google Cloud Audit Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudaudit).

Updated the [Search cases overview](https://docs.cloud.google.com/chronicle/docs/investigation/search-and-search-case-history) page to include custom field sample queries and removed related limitations.

Updated the delta field mapping to the existing cfd in the [Office 365 default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365).

Updated the [Imperva WAF default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-waf) to clarify API and Amazon S3 collection methods.

Added documentation for the Repeated Fields selector in the [Develop parser extensions](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions) guide.

Updated [Cisco IOS default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ios) with updated mappings and release deltas.

Added a new [Work with Chronicle API list operations](https://docs.cloud.google.com/chronicle/docs/reference/api-list-operations) guide.

Updated [Jamf Security Cloud default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-security-cloud) to support Google Cloud Storage and Amazon S3 collection methods.

Updated UDM entity validation requirements for various entity types in the [UDM usage guide](https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage).

Marked legacy Ingestion and Backstory APIs as legacy, added caution banners with discontinuation date (July 20, 2027), and prioritized modern Chronicle API in guides.

Add VPC Service Controls prerequisite to the [Google SecOps onboarding](https://docs.cloud.google.com/chronicle/docs/onboard) documentation.

Added a note in the [Ingest data with API connectors](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api) and [Create an Azure Event Hub feed](https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed) guides clarifying that ingestion from Azure sovereign clouds is unsupported.

Updated the [Google Cloud Audit Logs default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudaudit) with two new field mappings.

Updated the [Security Command Center findings](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-security-command-center-findings) documentation to support new finding categories (SECRET, EXTERNAL_EXPOSURE, etc.).

Updated the [FireEye alert default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-alert), including Bindplane agent path, forwarding config, and UDM mapping cleanup.

Added eight missing Chronicle API Terraform resources to the [Provision Terraform](https://docs.cloud.google.com/chronicle/docs/terraform) documentation.

Added field mapping for `properties.ActionType` to `security_result.action` for the [Microsoft Defender for Endpoint default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint).

Updated the [BeyondTrust Endpoint Privilege Management (EPM) default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-endpoint) and collector script.

Added documentation for [Managing integration dependencies in Google SecOps SOAR](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/managing-integration-dependencies).

Updated [Chronicle API migration guide](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api) to recommend Workload Identity Federation and added troubleshooting steps. For details, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/migrate-from-legacy-api-to-chronicle-api).

Improve Docker agent redeploy and configuration. For details, see [Troubleshoot common issues](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting).

Added a new guide - [UDM search compared with Rule results](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-vs-rules-results), comparing UDM search and YARA-L detection rule results. Other related documentation - [Analyze search data with statistics](https://docs.cloud.google.com/chronicle/docs/investigation/statistics-aggregations-in-udm-search), [Use aggregations in YARA-L queries](https://docs.cloud.google.com/chronicle/docs/investigation/use-aggregations-in-yaral-detection-rules), [Understand search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) and [Monitor rule performance](https://docs.cloud.google.com/chronicle/docs/detection/rule-effectiveness).

Added troubleshooting steps to the [Configure third-party identity](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication) guide for large JWTs in Workforce Identity Federation.

## June 2026

Updates to the [Oracle NetSuite default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-netsuite).

Updates to the [ Office 365 Message Trace default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365-messagetrace).

Updates to the [SentinelOne Alert default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinelone-alert).

Add Google Cloud Storage ingestion method for [Akamai SIEM Connector default parser](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-siem-connector).

New guide for [Google security tokens](https://docs.cloud.google.com/chronicle/docs/agentic-soc/tokens).

Restructured the UDM mapping table for the [Netskope Webproxy default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-webproxy).

Restructure [Health Hub documentation](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard) into a scenario-driven workflow and CUJ structure.

New documentation for [default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration) including: [Agiloft](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/agiloft), [Airlock Digital](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/airlock-digital), [Alveo RDM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/alveo-rdm), [AppOmni](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/appomni), [Armis Activities](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-activities), [Armis Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-alerts), [Armis Devices](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-devices), [Aruba AirWave](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-airwave), [Asset Panda](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asset-panda), [Aware Signals](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aware-signals), [AWS ECS Metrics](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ecs-metrics), [AWS Inspector](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-inspector), [AWS Lambda Function](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-lambda-function), [AWS RedShift](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-redshift), [Azure Cosmos DB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-cosmos-db), and [Cisco Secure Access](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-secure-access).

[Add information about out-of-the-box ingestion quota alerts to the burst limits documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/burst-limits).

Update the UDM mapping table for the [Palo Alto Prisma Cloud alert default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-ca).

Added a new guide for [Investigating detections in Search](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-detections-in-search).

Updated parameter documentation for the [Microsoft Azure Sentinel response integration](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-azure-sentinel).

Updated documentation for 29 default parsers, including: [Azure AD Signin](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-signin), [Azure AD](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad), [Azure API Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-api-management), [Barracuda Email](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-email), [BeyondTrust SRA](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-sra), [BlueCat DDI](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-ddi), [Bomgar](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bomgar), [Broadcom CA PAM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ca-pam), [CA SSO Web](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-sso-web), [CB App Control](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cb-app-control), [Centrify SSO](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/centrify-sso), [Cisco AMP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-amp), [Cisco Cloudlock CASB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-cloudlock-casb), [Cisco eStreamer](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-estreamer), [Cisco SDWAN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-sdwan), [Cisco Umbrella Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-umbrella-audit), [Cisco WSA](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsa), [Cisco WSM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsm), [Citrix Storefront](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-storefront), [CS Stream](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-stream), [Cylance Protect](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cylance-protect), [Digital Shadows Searchlight](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-searchlight), [Imperva WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-waf), [Kaspersky AV](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kaspersky-av), [macOS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/macos), [McAfee Webproxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-webproxy), [MobileIron](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mobileiron), and [Nasuni File Services](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nasuni-file-services).

Added documentation for Google Search grounding and citations in [Gemini for SecOps](https://docs.cloud.google.com/chronicle/docs/secops/gemini-docs).

Refactored the [Qualys Asset Context default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-asset-context) to describe a new ingestion method and updated the UDM mapping table and corrected the API path in the [Qualys VM default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-vm).

Updated the [Azure AD Sign-in default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-signin) to include ingesting AD FS Sign-in Logs and detailed instructions for configuring Azure Blob Storage feeds.

Updated the [tech partner integration page](https://docs.cloud.google.com/chronicle/docs/reference/partner-hosted-siem-integrations).

Refined steps for finding SubjectID in [AWS CloudTrail default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudtrail).

Added deprecation notice for reference lists, to be replaced by data tables. Refer to [Data RBAC reference lists](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-reference-lists) and [Reference lists](https://docs.cloud.google.com/chronicle/docs/reference/reference-lists) for details.

Added support for querying SOAR custom fields in dashboards. Updated [sample YARA-L for dashboard guide](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard) and [SOAR data dashboard reference](https://docs.cloud.google.com/chronicle/docs/reference/soar-data-dashboard).

Updated [Reaction Triggers document](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-reaction-triggers-in-playbooks) to include cases.

New guides for [Case Playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/case-playbooks), [Attaching playbooks to an alert or case](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/attach-playbooks-to-alerts-cases).

Updated the [Cisco ASA Firewall default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-asa-firewall) to add mapping event_type for `722032`, `722033`, `722034`.

Updated the [CISCO_ASA_FIREWALL default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-asa-firewall) to add mapping event_type for `109210`.

Updated `302013` and `302015` mappings in the [CISCO_ASA_FIREWALL default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-asa-firewall).

Updated [Google Cloud log export filter limitations](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs) with details on character limits and filter scoping.

Added Data RBAC requirement for enrichment blocks and viewing enriched fields. See [Block Enrichment Flows](https://docs.cloud.google.com/chronicle/docs/event-processing/block-enrichment-flows), [Data Enrichment](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment), [Overview of Aliasing and Enrichment](https://docs.cloud.google.com/chronicle/docs/event-processing/overview-of-aliasing-and-enrichment), and [UDM Search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search).

Updated [AWS IAM default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-iam) to focus on Third Party API for configuration data and revised the UDM mapping table.

Updated [Infoblox DNS parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/infoblox-dns), clarifying Bindplane agent use, updating paths, adding BloxOne configuration, and revising the UDM mapping table.

Added a new alert title and updated logic in the [Microsoft Graph Alert CFD default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-graph-alert).

Refactored [Azure Activity and Entra ID default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-activity) to recommend the Event Hub method.

Updated [Use joins in Search page](https://docs.cloud.google.com/chronicle/docs/investigation/search-joins) to include applications in Dashboards.

Updated the `DistributionList`, `EmailDirection` and `ThreatType` raw log field in the [Microsoft Defender Endpoint default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint).

Add documentation for [Asynchronous Search APIs](https://docs.cloud.google.com/chronicle/docs/investigation/search-lro-api).

Add documentation for [searching Cases and Case History in SIEM Search](https://docs.cloud.google.com/chronicle/docs/investigation/search-and-search-case-history).

Removing reference to deprecated feature/documentation for [BigQuery export](https://docs.cloud.google.com/chronicle/docs/reports/overview-chronicle-bigquery).

Update [Office 365 Message Trace default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365-messagetrace) with minor corrections and certificate permission details.

Refactored [Google Cloud VPC Flow Logs ingestion guide](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-vpc-flow) for accuracy and detail on setup via Google Cloud Storage.

Updates to the [Salesforce default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/salesforce).

Update [Agentic SOC trial](https://docs.cloud.google.com/chronicle/docs/agentic-soc/trial) and [investigation limits](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent).

Add content for migrating Mandiant legacy feeds to GTI in [ATI Fusion Feed documentation](https://docs.cloud.google.com/chronicle/docs/detection/ati-fusion-feed).

New guide for [optimizing log ingestion in Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/optimize-ingestion).

Add instructions for configuring UDM search query editor auto-collapse to the [UDM Search documentation](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search).

Updated [bulk case closure documentation](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/how-to-close-cases) to use Tools integration job.

Updates to the [BeyondTrust Endpoint default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-endpoint).

Updated 24 default parser documentation files, including [Accellion](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/accellion), [ADVA FSP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/adva-fsp), [AI Hunter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ai-hunter), [Akamai Cloud Monitor](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-cloud-monitor), [Akamai DataStream 2](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-datastream-2), [Akamai DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-dns), [Akamai EAA](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-eaa), [Akamai SIEM Connector](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-siem-connector), [Akamai WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-waf), [Akeyless Vault](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akeyless-vault), [AMD Pensando DSS Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/amd-dss-firewall), [Ansible AWX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ansible-awx), [Arbor Edge Defense](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-edge-defense), [Atlassian Cloud Admin Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-audit), [Atlassian Bitbucket](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-bitbucket), [Atlassian Confluence](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-confluence), [Attivo](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/attivo), [AWS Config](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-config), [AWS VPC Transit Gateway](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-transit-gateway), [Azure Ad Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-audit), [Azure Ad Context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-context), [IBM AIX System](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aix-system), [Linux auditd](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/auditd), and [Omnissa Workspace ONE UEM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/airwatch).

Backfill missing UDM mappings from changelogs across all default parser guides.

Updates to default parser documentation for: [GCP Cloud IoT](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudiot), [WinSCP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/winscp), [Zero networks](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zero-networks), [Zix Email Encryption](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zix-email-encryption), [Zscaler NSS Feeds for Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-nss-feeds), and [Zywall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zywall)..

Update Linux configuration file path for [FireEye NX default parser](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx).

Updates to default parser documentation for [ServiceNow audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-audit) and [Snipe-IT](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snipe-it).

Add UDM mapping tables to multiple default parser documentation files including [OCI Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oci-audit), [OnePassword Audit Events](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword-audit-events), [Rippling Activity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rippling-activitylogs), [Sentry](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentry), [ServiceNow Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-audit), [Snipe-IT](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snipe-it), [Snowflake](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snowflake), [Snyk Group Issues](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-issues), [Swimlane](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/swimlane), [Tailscale](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tailscale), [Tanium Question](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-question), [Tanium Reveal](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-reveal), [Team Cymru Scout Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/team-cymru-scout-threatintel), [ThreatConnect IOC (v3 API)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc-v3), [ThreatConnect IOC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc), [Tines](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tines), [Trellix Endpoint Security (HX) alert](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-alerts), [Trellix Endpoint Security (HX) audit event](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-audit), [Trellix Endpoint Security (HX) host inventory](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-hosts), [Trend Micro Vision One](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one), [Trend Micro Vision One Activity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-activity), [Trend Micro Vision One Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-audit), [Trend Micro Vision One Container Vulnerability](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-container-vulnerability), [Trend Micro Vision One Detections](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-detections), [Trend Micro Vision One Observed Attack Techniques](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-observed-attack-techniques), [Trend Micro Vision One Workbench](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-workbench), [](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/urlscan-io), [Virtru Email Encryption](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/virtru-email-encryption), [Windows Network Policy Server](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-net-policy-server), [Zendesk CRM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zendesk-crm), and [Zerofox Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zerofox-platform).

New response integration documentation for [Secret Manager](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/secret-manager).

Added a deprecation notice to documentation for several connectors in [Microsoft Defender For Cloud](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/azure-security-center), [Microsoft Sentinel](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-azure-sentinel), [Microsoft Defender for Endpoint](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-defender-atp), and [Microsoft Graph Security](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-graph-security) integrations.

Update [expected data availability for search](https://docs.cloud.google.com/chronicle/docs/investigation/expected-data-availability-for-search) and add troubleshooting information.

Updates to the [Armis Activities parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-activities).

Update Trellix Network Security syslog forwarding configuration in the [Trellix Network Security (NX, EX, FX) default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx) to recommend JSON-extended format.

Add a video to the [Data RBAC overview page](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview).

Updates to the [Workday HCM default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday).

Added troubleshooting and verification strategies for Health Hub. See [Ingestion overview](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-overview) and [Health Hub dashboard](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard).

Fixing sample MAC addresses in [UDM usage documentation](https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage).

Add troubleshooting and performance optimization tips to the [Dashboards Overview documentation](https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview).

Updates description of Google Threat Intelligence in the [Google SecOps packages documentation](https://docs.cloud.google.com/chronicle/docs/secops/secops-packages).

Updates to the [EmailV2](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-helix), [FireEye ETP](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/email-v2), and [FireEye Helix](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-etp) integrations for Marketplace 36.4.

Updates to the [Office 365 default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365).

Added Change Account Password action to the [CyberArk PAM](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberark-pam) and Download File action to [Palo Alto Cortex XDR](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-cortex-xdr) integration guides.

New [use cases page to help you find the relevant content for your use case](https://docs.cloud.google.com/chronicle/docs/use-cases).

Updates to the [Feed Management Overview](https://docs.cloud.google.com/chronicle/docs/administration/feed-management-overview), [Feed Management](https://docs.cloud.google.com/chronicle/docs/administration/feed-management), and [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api) documentation to clarify that IP allow listing doesn't support regions.

New default parser guide for [Tenable.io](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tenable-io).

Update [Advanced BQ documentation](https://docs.cloud.google.com/chronicle/docs/reports/bigquery-export) to use clustering columns in events.

Add limitations for renaming and deleting [data tables](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables).

Updates to the Google SecOps [Ingestion Methods](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) and [Service Limits](https://docs.cloud.google.com/chronicle/docs/reference/service-limits) documentation.

Updates to the [Composite Detection Rules](https://docs.cloud.google.com/chronicle/docs/yara-l/composite-detection-rules) and [Windowing Logic](https://docs.cloud.google.com/chronicle/docs/yara-l/windowing-logic) documentation.

Add `google_chronicle_feed` to the list of supported Terraform resources in the [Google SecOps Terraform documentation](https://docs.cloud.google.com/chronicle/docs/terraform).

Updates to the [Workspace Activity default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workspace-activity).

Updates to [Required and optional fields for each event type documentation](https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage).

Updates to the [Azure AD Context default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-context).

Updates to the [Proofpoint Mail default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail).

Added network security configuration details to [Create Azure Feed documentation](https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed).

Updated [AWS VPC Flow UDM mapping table](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-flow) and added release delta.

## May 2026

The [Query Joiner action for the SiemplifyUtilities integration](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify-utilities#query_joiner) has two new parameters - `Add Backticks` and `Delimiter`. 

New documentation for [default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration) including: [Preempt](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/preempt), [Preempt Auth](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/preempt-auth), [Privacy-i](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/privacy-i), [Proofpoint Mail Filter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail-filter), [Proofpoint Sendmail Sentrion](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-sendmail-sentrion), [Proofpoint Secure Email Relay](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-ser), [Proofpoint TRAP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-trap), [Proofpoint Web Browser Isolation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-web-browser-isolation), [Pure Storage](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pure-storage), [Quest Change Auditor for EMC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/quest-change-auditor-emc), [Quest File Access Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/quest-file-audit), [Radware Alteon](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/radware-alteon), [Rapid7 Nexpose](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rapid7-nexpose), [Recordia](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/recordia), [Red Canary EDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/redcanary-edr), [ReviveSec](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/revivesec), [Ribbon Analytics Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ribbon-analytics-platform), [RSA SecurID](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rsa-securid), [Sailpoint IdentityIQ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sailpoint-iiq), and [Salesforce Commerce Cloud.](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/salesforce-commerce-cloud)

Instructions for configuring Azure storage accounts for [ Microsoft Defender for Endpoint default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint).

New documentation for [default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration) including: [HPE Nimble Storage OS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nimble-os), [HUMAN Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/perimeterx-bot-protection), [ForgeRock OpenDJ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/opendj), [LogonBox](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/logonbox), [ManageEngine Log360](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-log360), [MicroStrategy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microstrategy), [MongoDB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mongo-db), [NetDocuments](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netdocuments), [Netscout OCI](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netscout-oci), [Netskope Client](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-client), [Nucleus Asset Metadata](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nucleus-asset), [One Identity Identity Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/one-identity-identity-manager), [OpenLDAP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openldap), [Oracle Unified Directory](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-oud), [Ordr IoT](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ordr-iot), [Passive DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/passive-dns), [Pharos](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pharos), and [PhishLabs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/phishlabs).

New documentation for [default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration) including: [Halcyon Anti-Ransomware](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/halcyon), [Honeyd](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/honeyd), [HP Linux](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hp-linux), [Huawei Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/huawei-switch), [IBM CICS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-cics), [IBM QRadar](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-qradar), [IBM Security Verify SaaS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-security-verify-saas), [IBM Tivoli](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-tivoli), [IBM WebSphere Application Sserver](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-websphere-app-server), [Infoblox RPZ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/infoblox-rpz), [Intel471 Malware Intelligence](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel471-malware-intel), [InterSystems Caché](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intersystems-cache), [ION Spectrum](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ion-spectrum), [JAMF Security Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-security-cloud), [JumpCloud Directory Insights](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jumpcloud-directory-insights), [Kea DHCP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kea-dhcp), [Keeper Enterprise Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/keeper), [Kyriba Treasury Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kyriba), [LinkShadow NDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/linkshadow-ndr), and [Precisely Ironstream for IBM z/OS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ironstream-zos).

New guide for [automating data enrichment using calculated fields](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/calculated-fields).

New [response integration for Cloud Identity](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cloud-identity).

New documentation for [default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration) including: [Comforte SecurDPS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/comforte-securdps), [COVID-19 Cyber Threat Coalition IOC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/covid-ctc-ioc), [Citrix Receiver](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/csg-citrix-rx), [Colinet Trotta GAUS SEGUROS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ct-gaus-seguros), [Custom DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-dns), [CyberGatekeeper NAC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cybergatekeeper-nac), [D3 Banking](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/d3-banking), [Desynova Contido](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/desynova-contido), [DHS IOC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dhs-ioc), [DigitalArts i-Filter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalarts-ifilter),[DMP Entre](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dmp-entre), [Evision FircoSoft](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/evision-fircosoft), [FireEye alert](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-alert), [FireEye PX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-px), [Forescout eyeInspect](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forescout-eyeinspect), [Fortinet DHCP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-dhcp), [Fortinet FortiNAC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortinac), [Fortinet FortiSandbox](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-sandbox), [Fortinet Web Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-webproxy), and [Google Cloud Identity Context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-identity-context).

New guide for [mapping SOAR permissions to Google Cloud IAM](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/map-soar-permissions-to-iam).

New guide for [migrating a Google SecOps instance to a new Google Cloud project](https://docs.cloud.google.com/chronicle/docs/administration/migrate-instance-from-one-project-to-another).

Added field mappings for the title `Microsoft Teams chat initiated by a suspicious external user` in CFD for [Microsoft Graph alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-graph-alert). 

Updates to the [SOAR pre-validation guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/soar-pre-validation) to include OIDC troubleshooting. 

Updates to SQS section with supported SQS message body formats in the [Feed Management API documentation](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api). 

Added new connector parameter - `Validate Dynamic List Entries` to the [Google Chronicle integration documentation](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chronicle). 

Add new SOAR API endpoint mappings under `cases`, `settings`, and `store` to their corresponding Chronicle API methods, including legacy playbook and user endpoints. 

[Deprecation](https://docs.cloud.google.com/chronicle/docs/deprecations) announcements for the [legacy Data Export API reference](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api). 

Updates to the [Export Raw Logs to Self-Managed GCS Bucket documentation](https://docs.cloud.google.com/chronicle/docs/reports/export-rawLogs-to-self-managed-gcs-bucket). 

Updates to the [Enhanced Data Export API documentation](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced). 

Updated [Cloud Audit field map](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudaudit) with new protoPayload fields within `protoPayload.request.ruleDeployment` and `protoPayload.response` to `target.resource.attribute.labels`. 

Support for two new Google SecOps Terraform resources - `chronicle_native_dashboard` and `chronicle_dashboard_chart`. 

Revamped time and date range picker in the [UDM Search documentation](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search). 

New row in the SCC field map table. `finding.sourceProperties.severity` now maps to `security_result.severity`. See [Field mapping reference](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-security-command-center-findings#field_mapping_reference_unspecified). 

[VPC-SC](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops) includes new service accounts for Advanced BQ datasets. 

New Ingestion Data Plane API V1 Endpoints. See [Ingestion Methods](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods). 

Updated permissions for Unified Rules Dashboard and added a Saved Views section. See [Detect threats](https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/get-started). 

Update rule testing section to include curated rules in [Test your rule](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules#test_your_rule). 

Updated deprecation dates for Reference lists to May 2027. The removal date is July 2027. See [Deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations). 

Enhanced Data Export API GA and deprecation of the legacy Data Export API and related items. See [Google SecOps Release Notes](https://docs.cloud.google.com/chronicle/docs/secops/release-notes). 

New documentation for [default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration) including: [Arista VeloCloud SD-WAN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/velo-firewall), [Microsoft Defender for Endpoint](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-defender-atp), [Sangfor Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sangfor-proxy), [SAP Sybase ASE](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-ase), [SAP BTP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-btp), [SAP NetWeaver](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-netweaver), [SAP SM20](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-sm20), [SAP SuccessFactors](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-successfactors), [Saviynt EIP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/saviynt-eip), [SecureLink](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/securelink), [Semperis DSP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/semperis-dsp), [Sonrai Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sonrai), [SOTI MobiControl](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/soti-mobicontrol), [Splunk Attack Analyzer](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/splunk-attack-analyzer), [SpyCloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/spycloud), [Stealthbits Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stealthbits-audit), [Stealthbits Defend](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stealthbits-defend), [Riverbed SteelHead](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/steelhead), [STIX Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stix). 

Clarify that [Azure AD Context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-context) provides directory information on users, removing mention of groups and devices. 

Updates to Zscaler default parsers: [Zscaler CASB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-casb), [Zscaler DLP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-dlp), and [Zscaler Web Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-webproxy). 

Updated documentation for 44 default parsers including: [Imperva SecureSphere](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-securesphere), [JFrog Artifactory](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jfrog-artifactory), [ManageEngine AD360](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-ad360), and others. 

Update [Azure AD Context documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-context) to clarify entity generation. 

Updated documentation for default parsers including: [FireEye HX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx), [Fivetran](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fivetran), [Juniper Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/juniper-firewall), and others. 

Updated documentation for default parsers including: [Cisco DNAC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-dnac), [Cloudflare](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare), [CyberArk PAM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-pam), and others. 

Updated the HTTP Header name in the sample script for [Office 365 Message Trace](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365-messagetrace). 

Corrected ingestion method for [Microsoft Defender for Cloud alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-cloud-alerts) to Third Party API. 

Newly mapped `events.parameters[device_compromised_state]` raw log field with `target.resource.attribute.labels[device_compromised_state]` UDM field in the [Workspace Activity default parser](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workspace-activity). 

Added new `TELNET`, `SFTP`, `IMAP`, `POP3`, and `IRC` enums to the `network.application_protocol` UDM field for [Corelight sensors](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/corelight). 

Refactored [ServiceNow Security parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-security). 

Updates to the [F5 BIG-IP LTM default parser](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-ltm). 

Updates to the [Microsoft Intune](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune) and [Microsoft Intune Context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune-context) default parser documentation. 

New [Self-serviced public-preview feature management guide](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage).

New [Standard Parser Support Policy documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/standard-parser-support-policy).

New documentation for [default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration) including: [Static IP asset context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asset-static-ip), [BMC Client Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-client-management), [Zeek (Bro) TSV](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bro-tsv), [Centripetal Networks IOC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/centripetal-ioc), [Cequence Bot Defense](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cequence-bot-defense), [Cimcor CimTrak](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cimcor), [CIS Albert alert](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cis-albert-alert), [Cisco Secure Workload](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-secure-workload), [Oracle Cloud Infrastructure Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-cloud-audit), [Palo Alto Prisma Access CASB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-casb), [Proofpoint TAP Forensics](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-tap-forensics), [Proofpoint TAP Threats](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-tap-threats), [Red Hat Directory Server LDAP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/redhat-directory-server), [Netwrix Privilege Secure for Discovery](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/remediant-secureone), [Rubrik Security Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rubrik-security-cloud), [Saiwall VPN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/saiwall-vpn), [SAP Cloud Identity Services](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-identity-and-auth-data), [SentinelOne Activity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinelone-activity), and [Smartsheet](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/smartsheet).

Updated the [Salesforce default parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/salesforce) for feed configuration and UDM mapping.

Added permissions section to [Office 365 parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365).

Updated custom header in [Falco Sidekick parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/falco-ids) to `X-Webhook-Access-Key`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
