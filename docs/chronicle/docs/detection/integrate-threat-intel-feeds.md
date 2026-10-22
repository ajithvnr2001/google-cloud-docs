---
url: https://docs.cloud.google.com/chronicle/docs/detection/integrate-threat-intel-feeds/
title: Integrate your own threat intelligence feeds \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:21.778023+00:00
---

# Integrate your own threat intelligence feeds  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/integrate-threat-intel-feeds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate your own threat intelligence feeds

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide is for security engineers and detection engineers who want to integrate custom Indicators of Compromise (IoCs) and third-party threat intelligence feeds into Google Security Operations. It explains how to ingest threat feeds, normalize indicators into the Unified Data Model (UDM) Entity Context Graph (ECG), and correlate indicator entities with streaming event telemetry. By following this method, you automate threat detection across your environment and eliminate manual indicator lookups. Successful integration reduces alert triage times and strengthens your organization's security posture through real-time and retroactive threat detection.

Integrating custom threat intelligence feeds lets your security operations team combine external indicator streams (such as Malware Information Sharing Platform (MISP), STIX/TAXII, or commercial feeds) with your internal security telemetry. Once normalized into the ECG, threat entities support both automated indicator matching and custom multi-event YARA-L 2.0 correlation rules.

## Key terminology

  * **Entity Context Graph (ECG)** : The contextual storage layer in Google SecOps that maintains stateful entity records (such as assets, users, and threat indicators) for correlation with security event logs.
  * **Unified Data Model (UDM)** : The standardized schema that Google SecOps uses to normalize raw event logs and contextual entity data.
  * **Indicator lifecycle interval (`metadata.interval`)**: The time-bounded validity window (`start_time` and `end_time`) that defines when a threat indicator is active in the ECG.
  * **Automatic IoC match** : A system-generated finding created when an incoming security event matches an active indicator entity in the ECG, displayed on the **IoC matches** page.
  * **YARA-L retrohunt** : An on-demand historical search that executes a YARA-L 2.0 detection rule against up to 30 days of past security telemetry.



## Common use cases

The following use cases show how bringing your own threat intelligence addresses common security operations objectives.

### Automated real-time indicator matching

  * **Objective** : Automatically evaluate streaming security events against ingested third-party indicators without maintaining custom correlation rules.
  * **Value** : Eliminates manual rule maintenance for high-volume threat feeds and surfaces immediate matches on the **IoC matches** page.



### Custom YARA-L correlation rules and retrohunting

  * **Objective** : Join threat intelligence entities in the ECG with multi-event telemetry and scan up to 30 days of historical data using retrohunts.
  * **Value** : Detects multi-stage attacks and uncovers historical compromises that occurred before an indicator was added to your threat feeds.



## Before you begin

Before you begin, confirm that the following prerequisites are met:

  * **Permissions** : You must have Identity and Access Management permissions to manage data feeds and author detection rules in Google SecOps (for example, `Chronicle API Admin` or `Chronicle API Editor`). For details on required roles, see [Configure feature access](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).
  * **Environment check** : Confirm that you have an active Google SecOps instance and valid API credentials or endpoint URLs for your external threat intelligence provider (such as MISP, STIX/TAXII, or Cloud Storage buckets).
  * **Search versus rule functionality** : UDM search lets you inspect raw entity records stored in the ECG regardless of their active window, whereas YARA-L detection rules and automatic matching only evaluate indicators whose `metadata.interval` encloses the event timestamp.
  * **Dashboard and search field prefixes** : When querying threat intelligence entities in UDM search, dashboards, or YARA-L rules, use the `graph.entity.` prefix for indicator values (such as `graph.entity.ip`) and the `graph.metadata.threat.` prefix for threat attribution fields.



## Ingest threat intelligence indicators

Select and configure an ingestion mechanism to bring external indicator streams into Google SecOps.

### Select a feed ingestion mechanism

You can ingest threat intelligence feeds using any of the following supported mechanisms:

  * **Prebuilt default parsers** : Google SecOps includes default parsers for many threat intelligence platforms. For a list of supported parsers categorized under **IOC** , see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers#with-default-parser). Supported vendors include MISP, ThreatConnect, Intel471, and Cyjax.
  * **Feed Management API** : Configure feeds in the Google SecOps console or using the [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api) to periodically pull indicators from external HTTPS, Cloud Storage, or Amazon S3 endpoints.
  * **Ingestion API** : Send pre-structured entity payloads directly to Google SecOps using the [Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api).
  * **Bindplane agent** : Collect and forward indicator logs from on-premises or cloud environments using the [Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent).
  * **Cloud Run functions** : Deploy serverless ingestion scripts using Cloud Run functions to fetch indicators from external APIs (such as STIX/TAXII or MISP) and stream them into Google SecOps. For details, see [Use ingestion scripts deployed as Cloud Run functions](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-using-cloud-functions).
  * **Google SecOps response integrations** : Ingest indicators through Content Hub connectors to synchronize threat lists as part of automated playbooks. For details, see [Use the Content Hub](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/using-the-marketplace).



### Onboard threat intelligence feeds

To ingest indicator logs from your threat intelligence provider into Google SecOps:

  1. Follow the onboarding procedure for your specific threat feed format or provider:

     * **STIX/TAXII** : See [Collect STIX threat intelligence logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stix) or deploy the serverless connector in [Use ingestion scripts deployed as Cloud Run functions (STIX/TAXII)](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-using-cloud-functions#stixtaxii) (log type `STIX`).
     * **MISP** : See [Collect MISP IoC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/misp-ioc) or [Use ingestion scripts deployed as Cloud Run functions (MISP)](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-using-cloud-functions#misp) (log type `MISP_IOC`).
     * **Custom CSV feeds** : See [Collect CSV custom IoC files](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/csv-custom-ioc) (log type `CSV_CUSTOM_IOC`).
     * **ThreatConnect** : See [Collect ThreatConnect IoC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc) or [Collect ThreatConnect IoC logs using the v3 API](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc-v3) (log types `THREATCONNECT_IOC` and `THREATCONNECT_IOC_V3`).
     * **Recorded Future** : See [Collect Recorded Future IoC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/recorded-future-ioc) (log type `RECORDED_FUTURE_IOC`).
     * **Anomali ThreatStream** : See [Collect Anomali ThreatStream IoC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/anomali-ioc) (log type `ANOMALI_IOC`).
     * **CrowdStrike Falcon Intelligence** : See [Collect CrowdStrike IoC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crowdstrike-ioc) (log type `CROWDSTRIKE_IOC`).
     * **Proofpoint Emerging Threats Pro** : See [Collect Proofpoint Emerging Threats Pro IoC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/et-pro-ioc) (log type `ET_PRO_IOC`).
     * **Other commercial and open source feeds** : Find the onboarding guide and log type for your vendor in [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers#with-default-parser).
  2. Assign the corresponding IoC log type (such as `STIX`, `MISP_IOC`, `CSV_CUSTOM_IOC`, or `THREATCONNECT_IOC`) to the incoming feed data so the default parser extracts indicator attributes into UDM entity fields.

**Caution:** If you assign an incorrect or generic event log type during feed setup, the ingestion pipeline fails to parse raw indicator payloads into UDM entity fields. Always select the matching IoC log type for your feed so the parser populates the ECG.
  3. Open the **Data ingestion** dashboard and verify that incoming log entries appear without unparsed log errors.




## Populate and validate the Entity Context Graph

When threat indicators enter Google SecOps, the parsing pipeline normalizes them into UDM entity records and populates the ECG. For details on how entity enrichment works, see [How Google SecOps enriches event and entity data](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment).

### Structured versus unstructured data mapping

Depending on how you send threat intelligence data to Google SecOps, follow the appropriate field mapping workflow:

  * **Structured data ingestion** : When sending pre-structured UDM entity records directly using the [Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api), format each payload according to the UDM `Entity` schema before ingestion.
  * **Unstructured and semi-structured data ingestion** : When sending raw logs (such as CSV, JSON, STIX, or CEF) using feeds, the Bindplane agent, or forwarders, assign a prebuilt default parser or create custom field mappings using [parser extensions](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions) to extract indicator values and map them to required UDM entity fields.



### What makes an entity an IoC

For an entity record in the ECG to be recognized as an actionable IoC by automatic matching and detection rules, the parser or API payload must populate the following five UDM field groups:

  * **Entity type (`metadata.entity_type`)**: The supported indicator entity type, such as `DOMAIN_NAME`, `IP_ADDRESS`, `FILE`, or `URL`.
  * **Source type (`metadata.source_type`)**: The data source classification, which must be set to `ENTITY_CONTEXT` for customer-ingested threat intelligence feeds.
  * **Artifact identifier (`entity.*`)**: The indicator value itself, such as `graph.entity.ip`, `graph.entity.hostname`, `graph.entity.domain.name`, `graph.entity.file.sha256` (or `md5` and `sha1`), or `graph.entity.url`.
  * **Threat metadata (`metadata.threat`)**: Contextual attributes describing the threat, including `threat_feed_name`, `threat_name`, `category`, `severity`, and `confidence`.
  * **Lifecycle interval (`metadata.interval`)**:

    * `metadata.interval.start_time`: The timestamp when the indicator becomes active.
    * `metadata.interval.end_time`: The timestamp when the indicator expires.
**Note:** The ECG enforces time-bounded validity. An indicator is active only if the query time or event timestamp falls between `metadata.interval.start_time` and `metadata.interval.end_time`. If an indicator lacks an end time or has expired, automatic matching and time-scoped YARA-L rules ignore it. Make sure your parser sets both start and end timestamps.



For schema definitions, see the [UDM field list for Entity](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#entity) and [EntityMetadata](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#entitymetadata).

### Verify ingested IoC data using UDM search

Indicators typically become searchable in UDM search within 2 to 5 minutes after ingestion and parsing. Verify that your indicators populate the ECG by running a UDM search:

  1. In the Google SecOps navigation menu, select **Investigation** > **Search**.
  2. In the search field, enter a query targeting the entity graph for an ingested indicator value:

     * **IP address** :
           
           graph.entity.ip = "<var>IP_ADDRESS</var>"
           

     * **Domain** :
           
           graph.entity.hostname = "<var>DOMAIN_NAME</var>"
           

     * **File hash (SHA-256)** :
           
           graph.entity.file.sha256 = "<var>SHA256_HASH</var>"
           

     * **Source product** :
           
           graph.metadata.source_product = "<var>SOURCE_PRODUCT_NAME</var>"
           

  3. Click **Search** or press **Enter**.

  4. Click the returned entity card and confirm that the `threat` and `interval` fields contain your expected metadata and active timestamps.

**Note:** If no entity records appear in search results after 5 minutes, check the **Data ingestion** dashboard for parser drop rates or schema validation errors.



## Correlate telemetry and detect threats

After your threat indicators populate the ECG, correlate them with incoming and historical security events.

### Enable automatic IoC matching

Google SecOps includes an automated matching engine that operates independently of custom detection rules. When event telemetry matches an active indicator in the ECG:

  * **System-generated matches** : The platform creates an **IoC match** record automatically without requiring custom rule maintenance.
  * **Estimated post-ingestion timing** (ballpark estimation): 
    * **Streaming events** : Once an indicator populates the ECG (typically 5 to 15 minutes after ingestion), Google SecOps evaluates incoming streaming events and surfaces matches on the **IoC matches** page within 5 to 15 minutes.
    * **Historical events** : The automated matching engine also evaluates newly ingested indicators retroactively against historical telemetry in batch cycles, with initial matches typically appearing within 1 to 4 hours (and full historical correlation completing within 24 hours).
  * **Interval enforcement** : The matching engine evaluates events strictly against active indicators where the event timestamp falls within `metadata.interval`.



### Author YARA-L 2.0 correlation rules

Write YARA-L 2.0 detection rules to join event telemetry (such as network connections, DNS queries, or process launches) with indicator entities in the ECG. Custom rules let you combine indicator matches with behavioral thresholds, asset context, and exclusion lists:

  1. In the Google SecOps navigation menu, select **Detection** > **Rules & Detections**, and then click **New**.
  2. In the `events:` section of your rule, define a placeholder variable to join a UDM event field (such as `$net.target.ip = $ip`) with the corresponding ECG entity field (such as `$ioc.graph.entity.ip = $ip`).
  3. Filter the entity variable by threat attributes (such as `$ioc.graph.metadata.threat.category`) and specify a correlation time window in the `match:` section (for example, `$ip over 5m`).

**Caution:** Joining high-volume event streams with ECG entities without filtering by `metadata.event_type` or threat metadata can cause rule timeouts or excessive false positives. Scope your rule to specific event types and exclude known benign internal scanners using reference lists.
  4. Click **Save New Rule**.




### Run a retrohunt to detect historical compromises

Threat intelligence feeds often contain indicators that adversaries used days or weeks before your organization ingested the feed. While live rules evaluate new incoming telemetry, a YARA-L retrohunt applies your rule logic retroactively against up to 30 days of historical security events:

  1. In the Google SecOps navigation menu, select **Detection** > **Rules & Detections**.
  2. Locate your custom threat intelligence rule in the rules list.
  3. Click more_vert for more rule options and select **YARA-L Retrohunt**.
  4. In the **YARA-L Retrohunt** dialog, select the start and end times for your historical search. Make sure the selected date range is greater than or equal to the match window specified in your rule.
  5. Click **Run**.
  6. Open the **Detections** tab for the rule to monitor progress and inspect historical matches.

**Note:** Running a retrohunt on a rule with alerting enabled generates a SOAR alert and case for every historical detection found, which can flood your queue. Keep the rule's alerting status disabled during initial retrohunts, review hits on the **Detections** page, and then enable alerting for real-time monitoring.



For more details, see [Run a rule against historical data](https://docs.cloud.google.com/chronicle/docs/detection/run-rule-historical-data).

## Investigate matches and alerts

Review findings generated by automatic matching and custom correlation rules across dedicated views in Google SecOps.

### Review automatic hits on the IoC matches page

To investigate automatic indicator matches:

  1. In the Google SecOps navigation menu, select **Detection** > **IoC matches**.
  2. Use the filter controls to scope findings by indicator type (domains, IP addresses, file hashes, or URLs).
  3. Click any indicator row to open the match details panel, which displays: 
     * Associated internal assets and usernames.
     * First seen and last seen event timestamps.
     * Threat intelligence feed source and confidence attribution.
  4. Click **View in UDM Search** to inspect all raw telemetry events associated with the indicator.



For more details, see [View IoCs using Applied Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page).

### Triage rule hits on the Alerts and Detections pages

Detections generated by custom YARA-L rules appear on the **Alerts** and **Detections** pages:

  1. In the Google SecOps navigation menu, select **Detection** > **Alerts & IoCs** to view prioritized rule alerts.
  2. Click an alert name to open the **Alert details** page and inspect the **Detections** table, which lists correlated event rows and ECG entity attributes.
  3. For silent rules (where alerting is disabled) or completed retrohunts, open **Detection** > **Rules & Detections**, click the rule name, and inspect the **Detections** tab.



### Correlate custom indicators with the Emerging Threats Center

You can also use the **Emerging Threats Center** to investigate how your custom IoC matches relate to broader adversary campaigns and malware families:

  1. In the Google SecOps navigation menu, select **Detection** > **Emerging Threats**.
  2. Review active threat campaigns and advisories, and pivot to UDM search to check whether indicators from your custom threat feeds overlap with observed campaign activity.



For more details, see [Emerging Threats Center overview](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats).

## Access advanced assets and references

Use the following YARA-L 2.0 snippets and reference resources when building custom threat intelligence rules.

### Outbound network connection matching a malicious IP address

This rule correlates outbound `NETWORK_CONNECTION` events with active IP indicators in the ECG:
    
    
    rule custom_ioc_network_connection {
      meta:
        author = "Security Operations"
        description = "Detects connections to IPs matching custom threat intel"
        severity = "HIGH"
        priority = "HIGH"
    
      events:
        $net.metadata.event_type = "NETWORK_CONNECTION"
        $net.target.ip = $ip
    
        $ioc.graph.entity.ip = $ip
        $ioc.graph.metadata.threat.category = "SUSPICIOUS_NETWORK"
    
      match:
        $ip over 5m
    
      outcome:
        $risk_score = max(85)
        $threat_name = array_distinct($ioc.graph.metadata.threat.threat_name)
        $source_feed = array_distinct($ioc.graph.metadata.source_product)
        $principal_hostname = array_distinct($net.principal.asset.hostname)
    
      condition:
        $net and $ioc
    }
    

### DNS query matching a malicious domain

This rule identifies `NETWORK_DNS` lookups for domains flagged as malicious in your ingested threat feeds:
    
    
    rule custom_ioc_malicious_domain_query {
      meta:
        author = "Security Operations"
        description = "Detects DNS queries for domains matching threat intel"
        severity = "MEDIUM"
        priority = "MEDIUM"
    
      events:
        $dns.metadata.event_type = "NETWORK_DNS"
        $dns.network.dns.questions.name = $domain
    
        $ioc.graph.entity.hostname = $domain
    
      match:
        $domain over 10m
    
      outcome:
        $threat_name = array_distinct($ioc.graph.metadata.threat.threat_name)
        $source_feed = array_distinct($ioc.graph.metadata.source_product)
        $client_ip = array_distinct($dns.principal.ip)
    
      condition:
        $dns and $ioc
    }
    

### Process execution matching a malicious SHA-256 file hash

This rule triggers when a `PROCESS_LAUNCH` event matches a known malicious SHA-256 file hash stored in the ECG:
    
    
    rule custom_ioc_malicious_file_execution {
      meta:
        author = "Security Operations"
        description = "Detects process launches matching malicious file hashes"
        severity = "CRITICAL"
        priority = "HIGH"
    
      events:
        $process.metadata.event_type = "PROCESS_LAUNCH"
        $process.target.process.file.sha256 = $sha256
    
        $ioc.graph.entity.file.sha256 = $sha256
    
      match:
        $sha256 over 5m
    
      outcome:
        $threat_name = array_distinct($ioc.graph.metadata.threat.threat_name)
        $file_path = array_distinct($process.target.process.file.full_path)
        $hostname = array_distinct($process.principal.asset.hostname)
        $user = array_distinct($process.principal.user.userid)
    
      condition:
        $process and $ioc
    }
    

### Community blogs and additional resources

For additional examples on authoring YARA-L rules and correlating custom threat intelligence feeds, see the following Google Cloud Community resources:

  * [Building rules with your own threat intelligence (Part 1)](https://www.googlecloudcommunity.com/gc/Community-Blog/New-to-Google-SecOps-Building-Rules-with-Your-Own-Threat-Intel/ba-p/733835)
  * [Building rules with your own threat intelligence (Part 2)](https://www.googlecloudcommunity.com/gc/Community-Blog/New-to-Google-SecOps-Building-Rules-with-Your-Own-Threat-Intel/ba-p/733857)
  * [YARA-L basics](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-know-Google-SecOps-SIEM-YARA-L-basics/ta-p/635468)
  * [YARA-L rule variables](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-know-Google-SecOps-SIEM-YARA-L-rule-variables/ta-p/635481)
  * [YARA-L operators and modifiers](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-know-Google-SecOps-SIEM-YARA-L-operators-and/ta-p/635489)
  * [Building a single event rule using a regular expression](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-SIEM-Building-a-single-event-rule/ta-p/635498)
  * [Building a multi-event rule: Joining events](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Chronicle-Building-a-Multi-Event-Rule-Joining/ta-p/665140)
  * [Rules editor navigation](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Chronicle-SIEM-Rules-Editor-Navigation/ta-p/659309)



## Troubleshooting

Use this section to manage performance expectations and resolve common issues when onboarding threat intelligence feeds and building correlation rules.

### Latency, service quota, and limits

  * **Ingestion and UDM search indexing** : Newly ingested indicators typically appear in UDM search within 2 to 5 minutes. Wait at least 5 minutes after feed ingestion before troubleshooting missing entity records.
  * **Automatic IoC matching latency** : Once an indicator populates the ECG, matches against incoming streaming events appear on the **IoC matches** page within 5 to 15 minutes. Retroactive batch matching against historical events typically takes 1 to 4 hours (and up to 24 hours for full historical correlation).
  * **Entity Context Graph correlation window** : Automatic IoC matching and YARA-L correlation rules evaluate indicators strictly within their active `metadata.interval` window. Indicators with expired `end_time` values don't generate matches.
  * **Retrohunt search window** : YARA-L retrohunts scan up to 30 days of historical telemetry per execution. Completion time depends on rule complexity and system resource availability.



### Error remediation

Use this table to diagnose and resolve issues during threat intelligence onboarding and detection rule authoring.

Issue | Issue description | Fix  
---|---|---  
Unparsed IoC logs | Feed status shows incoming data, but logs fail to parse into UDM entities. | Confirm that the feed log type matches your parser (for example, `STIX`, `MISP_IOC`, or `CSV_CUSTOM_IOC`). Check the **Data ingestion** dashboard for raw schema errors.  
Missing UDM search results | Indicator logs parse without errors, but UDM search returns no entity records. | Verify that your query targets `graph.entity.*` fields (such as `graph.entity.ip`) rather than `udm.principal.*` event fields.  
Rule fails to trigger on known indicator | Both the event and indicator exist in UDM search, but the YARA-L rule produces no detections. | Confirm that `metadata.interval.start_time` and `metadata.interval.end_time` on the indicator enclose the event timestamp.  
Alert flood during retrohunt | Running a retrohunt creates hundreds of duplicate SOAR cases and alerts. | Turn off the rule's alerting toggle before starting a retrohunt. Review detections on the **Detections** page before re-enabling live alerting.  
High volume of false positives | Noisy indicators trigger detections on benign internal scanners or administrative hosts. | Add a reference list exclusion to your rule (for example, `not $net.principal.ip in %benign_scanner_ips`) and require behavioral event context.  
  
### Validation and testing

Before enabling a custom threat intelligence rule in live alerting mode, verify its logic using the built-in **Test rule** feature:

  1. Open **Detection** > **Rules & Detections** and click your rule to open the Rules Editor.
  2. Click **Test rule** in the lower panel to evaluate the rule against recent historical event data and active ECG entities without generating alerts or SOAR cases.
  3. Inspect returned test detections to confirm that `outcome` variables (such as `$threat_name` and `$source_feed`) populate as expected.



## What's next

  * Learn more about [Entity context in search](https://docs.cloud.google.com/chronicle/docs/investigation/entity-context-in-search).
  * Explore [Get started with YARA-L](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started) and [Single and multiple event rules in YARA-L](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples).
  * Understand [Applied Threat Intelligence curated detections](https://docs.cloud.google.com/chronicle/docs/detection/ati-curated-detections).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
