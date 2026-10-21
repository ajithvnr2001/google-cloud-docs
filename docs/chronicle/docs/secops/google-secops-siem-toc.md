---
url: https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc/
title: SIEM table of contents \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:26:24.541263+00:00
---

# SIEM table of contents  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SIEM table of contents

Click ![siem](https://docs.cloud.google.com/static/chronicle/images/siem.png) at the top of each SIEM document to return to this table of contents.

## Google SecOps SIEM

[Product overview](https://docs.cloud.google.com/chronicle/docs/overview)

[Sign in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui)

[Quickstart: Conduct a search](https://docs.cloud.google.com/chronicle/docs/review-security-alert)

[Quickstart: Investigate an alert](https://docs.cloud.google.com/chronicle/docs/review-alert)

[Configure user preferences (SIEM only)](https://docs.cloud.google.com/chronicle/docs/siem/user-prefs-siem)

## Onboarding to Google SecOps

[Overview of the process](https://docs.cloud.google.com/chronicle/docs/onboard)

[Understand your Google SecOps billing components](https://docs.cloud.google.com/chronicle/docs/onboard/understand-billing)

[Configure Google Cloud project for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project)

[Migrate a Google SecOps instance to a BYOP project](https://docs.cloud.google.com/chronicle/docs/administration/migrate-instance-from-one-project-to-another)

### Configure an identity provider

[Configure a Google Cloud identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication)

[Configure a third-party identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication)

[Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access)

[Configure data RBAC using IAM](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users)

[RBAC user guide for applications not using IAM](https://docs.cloud.google.com/chronicle/docs/administration/rbac)

[Google SecOps permissions in IAM](https://docs.cloud.google.com/chronicle/docs/reference/feature-rbac-permissions-roles)

[Link Google SecOps to Google Cloud services](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud)

## Ingest data

[Ingest entity data](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities)

[Overview of data ingestion](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow)

[Supported data sets and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers)

### Data processing

[Data Pipeline management](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline)

[Optimize high-volume log ingestion](https://docs.cloud.google.com/chronicle/docs/ingestion/optimize-ingestion)

## Ingest data to Google SecOps

[Ingest logs from specific sources](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration)

### Install and configure forwarders

[Overview of Google SecOps forwarders](https://docs.cloud.google.com/chronicle/docs/install)

[Google SecOps forwarder for Linux](https://docs.cloud.google.com/chronicle/docs/install/forwarder-linux)

[Google SecOps forwarder for Windows on Docker](https://docs.cloud.google.com/chronicle/docs/install/docker-forwarder-windows)

[Google SecOps forwarder executable for Windows](https://docs.cloud.google.com/chronicle/docs/install/forwarder-windows)

[Manage forwarder configurations through Google SecOps](https://docs.cloud.google.com/chronicle/docs/install/forwarder-management-configurations)

[Troubleshoot common Linux forwarder issues](https://docs.cloud.google.com/chronicle/docs/install/forwarder-management-configurations)

### Set up data feeds

[Feed management overview](https://docs.cloud.google.com/chronicle/docs/administration/feed-management-overview)

[Create and manage feeds using the feed management UI](https://docs.cloud.google.com/chronicle/docs/administration/feed-management)

[Create an Azure Event Hub feed](https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed)

[Create and manage feeds using the feed management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api)

[Use ingestion scripts deployed as Cloud Functions](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-using-cloud-functions)

[Use the Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api)

[DataTap Configuration API](https://docs.cloud.google.com/chronicle/docs/reference/datatapconfig-api)

[Use the Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent)

[Customer Management API](https://docs.cloud.google.com/chronicle/docs/reference/customer-management-api)

[Data Export API](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api)

[Data Export API (Enhanced)](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced)

### Monitor data ingestion

[Use Data Ingestion and Health dashboard](https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview#ingest)

[Use Cloud Monitoring for ingestion notifications](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics)

[View your billed ingestion volume](https://docs.cloud.google.com/chronicle/docs/ingestion/view-billed-ingestion-volume)

[Analyze feed activity with Cloud Logging](https://docs.cloud.google.com/chronicle/docs/ingestion/analyze-feed-activity-with-cloud-logging)

### Work with Google SecOps parsers

[Overview of log parsing](https://docs.cloud.google.com/chronicle/docs/event-processing/parsing-overview)

[Overview of the Unified Data Model](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview)

[Manage prebuilt parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates)

[Re-parse historical data (Log Replay)](https://docs.cloud.google.com/chronicle/docs/event-processing/reparse-historical-data)

[Configure custom parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/configure-custom-parsers)

[Request prebuilt and create custom log types](https://docs.cloud.google.com/chronicle/docs/event-processing/request-log-type)

[Parser extensions](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions)

[Parser extension examples](https://docs.cloud.google.com/chronicle/docs/event-processing/parser-extension-examples)

[Important UDM fields for parser data mapping](https://docs.cloud.google.com/chronicle/docs/reference/important-udm-fields)

[Tips and troubleshooting when writing parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/parser-tips-troubleshooting)

[Format log data as UDM](https://docs.cloud.google.com/chronicle/docs/unified-data-model/format-events-as-udm)

[Bypass log validation for parser extensions and custom parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/bypass-log-validations)

### Enrichment

[UDM enrichment and aliasing overview](https://docs.cloud.google.com/chronicle/docs/event-processing/overview-of-aliasing-and-enrichment)

[Aliasing](https://docs.cloud.google.com/chronicle/docs/event-processing/aliasing-overview)

[Enrichment](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment)

[How Google SecOps enriches event and entity data](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment)

[Block enrichment from specific flows](https://docs.cloud.google.com/chronicle/docs/event-processing/block-enrichment-flows)

[Using the Entity Context Graph (ECG)](https://docs.cloud.google.com/chronicle/docs/event-processing/entity-graph)

[Auto Extraction overview](https://docs.cloud.google.com/chronicle/docs/event-processing/auto-extraction)

## Detecting threats

[View alerts and IOCs](https://docs.cloud.google.com/chronicle/docs/investigation/alerts-iocs)

[Review potential security threats](https://docs.cloud.google.com/chronicle/docs/review-security-alert)

[Single event rules](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples#single-event-rule)

[Multiple event rules](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples#multiple_event_rule)

### Composite detections

[Overview of composite detections](https://docs.cloud.google.com/chronicle/docs/detection/composite-detections)

### Monitor for events using rules

[View rules in the Rules Dashboard](https://docs.cloud.google.com/chronicle/docs/detection/view-all-rules)

[Manage unified rules](https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/get-started)

[Analyze rule effectiveness and efficiency](https://docs.cloud.google.com/chronicle/docs/detection/rule-effectiveness)

[Understand rule quotas](https://docs.cloud.google.com/chronicle/docs/detection/rule-quotas)

[Troubleshoot rule runtime errors](https://docs.cloud.google.com/chronicle/docs/detection/troubleshoot-rule-errors)

[Risk-based alerting with entity only rules](https://docs.cloud.google.com/chronicle/docs/detection/risk-based-alerting)

[Understand threat coverage with the MITRE ATT&CK matrix](https://docs.cloud.google.com/chronicle/docs/detection/mitre-dashboard)

[View previous versions of a rule](https://docs.cloud.google.com/chronicle/docs/detection/view-rule-versions)

[Archive rules](https://docs.cloud.google.com/chronicle/docs/detection/view-all-rules)

[Download events](https://docs.cloud.google.com/chronicle/docs/detection/downloading-events)

[Run a rule against live data](https://docs.cloud.google.com/chronicle/docs/detection/run-rule-live-data)

[Understand rule run scheduling](https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency)

[Configure customized schedules for rules](https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule)

[Understand rule replays and MTTD](https://docs.cloud.google.com/chronicle/docs/detection/rule-replays)

[Understand rule detection delays](https://docs.cloud.google.com/chronicle/docs/detection/detection-delays)

[Run a rule against historical data](https://docs.cloud.google.com/chronicle/docs/detection/run-rule-historical-data)

[Optimize detection and reporting performance](https://docs.cloud.google.com/chronicle/docs/detection/optimize-detection-and-reporting-performance)

[Detection limits](https://docs.cloud.google.com/chronicle/docs/detection/detection-limits)

[Rule errors](https://docs.cloud.google.com/chronicle/docs/detection/rule-errors)

### Create context-aware analytics

[Overview of context-aware analytics](https://docs.cloud.google.com/chronicle/docs/detection/context-aware-analytics)

[Use Cloud Sensitive Data Protection data in context-aware analytics](https://docs.cloud.google.com/chronicle/docs/detection/usecase-dlp-high-risk-user-download)

[Use context-enriched data in rules](https://docs.cloud.google.com/chronicle/docs/detection/use-enriched-data-in-rules)

[Use default detection rules](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)

### Risk analytics

[Risk Analytics Quickstart guide](https://docs.cloud.google.com/chronicle/docs/detection/ueba-getting-started)

[Overview of Risk Analytics](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-overview)

[Use the Risk Analytics dashboard](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard)

[Metric functions for Risk Analytics rules](https://docs.cloud.google.com/chronicle/docs/detection/metrics-functions)

[Watchlist Quickstart guide](https://docs.cloud.google.com/chronicle/docs/detection/watchlist-getting-started)

[Specify entity risk score in rules](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-entity-risk-score)

[Watchlists FAQ](https://docs.cloud.google.com/chronicle/docs/detection/watchlist-faq)

[Risk Analytics FAQ](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-faq)

### Work with curated detections

[Use curated detections to identify threats](https://docs.cloud.google.com/chronicle/docs/detection/use-curated-detections)

[Use curated detection rules for third-party vendor alerts](https://docs.cloud.google.com/chronicle/docs/detection/third-party-vendor-alerts-category)

[Use the curated detections UI](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections)

[Cloud Threats category overview](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category)

[Composite Rules category overview](https://docs.cloud.google.com/chronicle/docs/detection/composite-rules-category)

[Non-prioritized IoC Matching threats category overview](https://docs.cloud.google.com/chronicle/docs/detection/non-prioritized-ioc-matching-threats-category)

[Chrome Enterprise Threats category overview](https://docs.cloud.google.com/chronicle/docs/detection/chrome-enterprise-threats-category)

[Linux Threats category overview](https://docs.cloud.google.com/chronicle/docs/detection/linux-threats-category)

[macOS Threats category overview](https://docs.cloud.google.com/chronicle/docs/detection/macos-threats-category)

[Mandiant Hunting Rules category overview](https://docs.cloud.google.com/chronicle/docs/detection/mandiant-hunt-category)

[Risk Analytics for UEBA category overview](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-ueba-category)

[Windows Threats category overview](https://docs.cloud.google.com/chronicle/docs/detection/windows-threats-category)

[Applied Threat Intelligence curated detections overview](https://docs.cloud.google.com/chronicle/docs/detection/ati-curated-detections)

[Verify data ingestion using test rules](https://docs.cloud.google.com/chronicle/docs/detection/verify-data-ingestion)

[Configure rule exclusions](https://docs.cloud.google.com/chronicle/docs/detection/rule-exclusions)

[Rules capacity](https://docs.cloud.google.com/chronicle/docs/detection/rule-quotas#curated-detections-capacity)

### Manage noisy alerts

[Configure alert suppression](https://docs.cloud.google.com/chronicle/docs/investigation/alert-suppression)

[Manage rule exclusion using API](https://docs.cloud.google.com/chronicle/docs/investigation/rule-exclusion-api)

### Applied Threat Intelligence

[Applied Threat Intelligence overview](https://docs.cloud.google.com/chronicle/docs/detection)

[Applied Threat Intelligence prioritization](https://docs.cloud.google.com/chronicle/docs/detection/ati-prioritization)

[View IOCs using Applied Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page)

[IC score overview](https://docs.cloud.google.com/chronicle/docs/detection/understand-ic-score)

[Applied Threat Intelligence fusion feed overview](https://docs.cloud.google.com/chronicle/docs/detection/ati-fusion-feed)

[Emerging Threats Center](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats)

[Emerging Threats Center detail view](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats-detailed-view)

[Answer Threat Intelligence questions with Gemini ](https://docs.cloud.google.com/chronicle/docs/detection/answer-threat-intelligence-questions-gemini)

[Gemini documentation summaries](https://docs.cloud.google.com/chronicle/docs/secops/gemini-docs)

[Use Triage and Investigation Agent to investigate alerts](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent)

[Triage and Investigation Agent dashboard](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent-dashboards)

## YARA-L 2.0

[Get Started](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started)

### Syntax

[Meta section](https://docs.cloud.google.com/chronicle/docs/yara-l/meta-syntax)

[Events section](https://docs.cloud.google.com/chronicle/docs/yara-l/events-syntax)

[Match section](https://docs.cloud.google.com/chronicle/docs/yara-l/match-syntax)

[Outcome section](https://docs.cloud.google.com/chronicle/docs/yara-l/outcome-syntax)

[Conditions section](https://docs.cloud.google.com/chronicle/docs/yara-l/condition-syntax)

[Options section](https://docs.cloud.google.com/chronicle/docs/yara-l/options-syntax)

[Expressions, operators, and other constructs](https://docs.cloud.google.com/chronicle/docs/yara-l/expressions)

[Nested if statements](https://docs.cloud.google.com/chronicle/docs/yara-l/nested-if)

[Use OR syntax in the condition section](https://docs.cloud.google.com/chronicle/docs/yara-l/multievent-or)

[Use N OF syntax with event variables](https://docs.cloud.google.com/chronicle/docs/yara-l/multievent-n-of)

[Repeated fields](https://docs.cloud.google.com/chronicle/docs/yara-l/repeated-fields)

[Reference list syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/reference-list-syntax)

[Detection event sampling](https://docs.cloud.google.com/chronicle/docs/yara-l/detection-event-sampling)

[YARA-L 2.0 windowing logic](https://docs.cloud.google.com/chronicle/docs/yara-l/windowing-logic)

### Functions

[Functions for Dashboards](https://docs.cloud.google.com/chronicle/docs/reference/yaral-functions-native-dashboards)

### Query and investigate

[Statistics and aggregations](https://docs.cloud.google.com/chronicle/docs/investigation/statistics-aggregations-in-udm-search)

[Use conditions in Search and Dashboards](https://docs.cloud.google.com/chronicle/docs/investigation/yara-l-2-0-conditions)

[Create and save visualizations in Search](https://docs.cloud.google.com/chronicle/docs/reports/visualization-in-search)

[Use metrics in Search](https://docs.cloud.google.com/chronicle/docs/investigation/yara-l-2-0-metrics-search)

[Use deduplication in Search and Dashboards](https://docs.cloud.google.com/chronicle/docs/investigation/deduplication-yaral)

[Create multi-stage queries](https://docs.cloud.google.com/chronicle/docs/investigation/multi-stage-yaral)

### Develop detection rules

[Use context-enriched data in rules](https://docs.cloud.google.com/chronicle/docs/detection/use-enriched-data-in-rules)

[Context-aware analysis overview](https://docs.cloud.google.com/chronicle/docs/detection/context-aware-analytics)

[Specify entity risk score in rules](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-entity-risk-score)

[Use metric functions for Risk Analytics rules](https://docs.cloud.google.com/chronicle/docs/detection/metrics-functions)

[Applied Threat Intelligence fusion feed overview](https://docs.cloud.google.com/chronicle/docs/detection/ati-fusion-feed)

[Composite detections overview](https://docs.cloud.google.com/chronicle/docs/detection/composite-detections)

[Construct composite detection rules](https://docs.cloud.google.com/chronicle/docs/yara-l/composite-detection-rules)

[Rule structure and best practices](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-best-practices)

### Manage and troubleshoot

[Run a rule against historical data](https://docs.cloud.google.com/chronicle/docs/detection/run-rule-historical-data)

[Configure rule exclusions](https://docs.cloud.google.com/chronicle/docs/detection/rule-exclusions)

[View and troubleshoot rule errors](https://docs.cloud.google.com/chronicle/docs/detection/rule-errors)

[Known issues and limitations](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-issues)

### Reference: Query libraries and transitions

[YARA-L 2.0 query reference library](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples)

[YARA-L 2.0 dashboard query library](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard)

[Transition from SPL to YARA-L 2.0](https://docs.cloud.google.com/chronicle/docs/yara-l/transition_spl_yaral)

[Generate search queries with Gemini](https://docs.cloud.google.com/chronicle/docs/investigation/generate-udm-search-queries-gemini)

[Generate a YARA-L 2.0 rule using Gemini](https://docs.cloud.google.com/chronicle/docs/detection/generate-yara-l-with-gemini)

## Investigating threats

### View Alerts

[Overview](https://docs.cloud.google.com/chronicle/docs/investigation/alerts-iocs)

[Manage alerts](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-alert)

[Investigate a GCTI alert](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-uppercase-alert)

[Investigate alerts and entity context](https://docs.cloud.google.com/chronicle/docs/investigation/Investigate-alert-entity-context)

### Searching for data

[Search for UDM event](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)

[Use context-enriched fields in UDM search](https://docs.cloud.google.com/chronicle/docs/investigation/use-enriched-data-in-search)

[Use UDM Search to investigate an entity](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-investigate-entity)

[Investigate detections in Search](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-detections-in-search)

[Use UDM Search time range and manage queries](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-time-range)

[Use conditions in search and dashboards](https://docs.cloud.google.com/chronicle/docs/investigation/yara-l-2-0-conditions)

[Use deduplication in search and dashboards](https://docs.cloud.google.com/chronicle/docs/investigation/deduplication-yaral)

[Metrics in UDM search using YARA-L 2.0](https://docs.cloud.google.com/chronicle/docs/investigation/yara-l-2-0-metrics-search)

[Use joins in Search](https://docs.cloud.google.com/chronicle/docs/investigation/search-joins)

[YARA-L 2.0 statistics and aggregations](https://docs.cloud.google.com/chronicle/docs/investigation/statistics-aggregations-in-udm-search)

[Use aggregations in YARA-L 2.0 queries](https://docs.cloud.google.com/chronicle/docs/investigation/use-aggregations-in-yaral-detection-rules)

[UDM search compared with Rule results](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-vs-rules-results)

[Generate UDM search queries with Gemini](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-best-practices)

[UDM search best practices](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-best-practices)

[Search raw logs](https://docs.cloud.google.com/chronicle/docs/investigation/search-raw-logs)

[Filter data in raw log search](https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-raw-log-scan-view)

[Create a reference list](https://docs.cloud.google.com/chronicle/docs/reference/reference-lists)

### Using investigative views

[Use investigative views](https://docs.cloud.google.com/chronicle/docs/investigation/investigation-views)

[Investigate an asset](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-asset)

[Work with asset namespaces](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

[Investigate a domain](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-domain)

[Investigate an IP address](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-ipaddress)

[Investigate a user](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-user)

[Investigate a file](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-file)

[View information from VirusTotal](https://docs.cloud.google.com/chronicle/docs/investigation/view-virustotal-information)

### Filtering data in investigative views

[Overview of procedural filtering](https://docs.cloud.google.com/chronicle/docs/investigation/filtering-overview)

[Filter data in User view](https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-user-view)

[Filter data in Asset view](https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-asset-view)

[Filter data in Domain view](https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-domain-view)

[Filter data in IP Address view](https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-ipaddress-view)

[Filter data in Hash view](https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-hash-view)

## Reporting

[Use context-enriched data in reports](https://docs.cloud.google.com/chronicle/docs/reports/use-enriched-data-in-reports)

[Dashboards overview](https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview)

### Work with custom dashboards

[Create a custom dashboard](https://docs.cloud.google.com/chronicle/docs/reports/create-custom-dashboard)

[Add a chart to a dashboard](https://docs.cloud.google.com/chronicle/docs/reports/create-chart-visualization)

[Share a personal dashboard](https://docs.cloud.google.com/chronicle/docs/reports/share-personal-dashboard)

[Schedule dashboard reports](https://docs.cloud.google.com/chronicle/docs/reports/schedule-reports)

[Import and export Google SecOps dashboards](https://docs.cloud.google.com/chronicle/docs/reports/import-export-dashboards)

### Work with Dashboards

[Dashboards overview](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards)

[Curated Dashboards](https://docs.cloud.google.com/chronicle/docs/reports/native-curated-dashboards)

[Manage Native Dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards)

[Manage charts in Native Dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts)

[Native Dashboard filters](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters)

[Visualizations in search](https://docs.cloud.google.com/chronicle/docs/reports/visualization-in-search)

[Configure scheduled reports](https://docs.cloud.google.com/chronicle/docs/reports/scheduled-email-reports)

## Data export

[Export to a Google-managed BigQuery project (legacy)](https://docs.cloud.google.com/chronicle/docs/reports/overview-chronicle-bigquery)

[Export to self-managed BigQuery project](https://docs.cloud.google.com/chronicle/docs/reports/export-to-customer-managed-project)

[Stream Data with Advanced BigQuery Export](https://docs.cloud.google.com/chronicle/docs/reports/bigquery-export)

[Understand BigQuery data schema](https://docs.cloud.google.com/chronicle/docs/reports/understand-bigquery-data-schema)

[Export raw logs to self-managed Google Cloud Storage bucket](https://docs.cloud.google.com/chronicle/docs/reports/export-rawLogs-to-self-managed-gcs-bucket)

## Administration

[Close alerts in bulk using the API.](https://docs.cloud.google.com/chronicle/docs/administration/bulk-close-alerts)

### Administer users

[Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access)

### Configure VPC Service Controls

[Configure VPC Service Controls for Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops)

### Configure data access control

[Overview of data RBAC](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview)

[Data RBAC impact on features](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-impact)

[Configure data RBAC for users](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users)

[Configure data RBAC for data tables](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-data-tables)

[Configure data RBAC for reference lists](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-reference-lists)

### Set up data feeds

[Feed management user guide](https://docs.cloud.google.com/chronicle/docs/administration/feed-management)

[CLI user guide](https://docs.cloud.google.com/chronicle/docs/administration/cli-user-guide)

[Configure audit logs](https://docs.cloud.google.com/chronicle/docs/administration/audit-logging)

[Data retention](https://docs.cloud.google.com/chronicle/docs/about/data-retention)

[Google Analytics in Google SecOps](https://docs.cloud.google.com/chronicle/docs/about/chronicle-google-analytics)

### Deprovision

[Self-service deprovisioning for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/customer-initiated-secops-deprovision)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
