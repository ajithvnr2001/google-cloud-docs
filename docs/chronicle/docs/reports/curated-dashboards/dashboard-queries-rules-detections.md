---
url: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-rules-detections/
title: Query rules and detections \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:59:34.084990+00:00
---

# Query rules and detections  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-rules-detections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query rules and detections

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document is for Security Operations Center (SOC) managers and analysts who want to monitor threat landscapes and system health using curated dashboards— predefined dashboards designed for visibility across various security use cases. This document provides a collection of curated dashboards and their underlying queries for the **SOAR cases** source type.

You can use these queries in the query editor or as a baseline for custom widgets. For information on how to create and manage dashboards, see [Manage dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards).

ISO 27001 – Technological ControlsChrome Enterprise Premium Security OverviewCloud Key Management OverviewCloud security posture OverviewCloud Storage Services OverviewData Ingestion and HealthGDPR Data GovernanceIdentity and Access Management (IAM) Security OperationsISO 27001 - Organizational ControlsLiving Off the Land ActivityMainMandiant Threat DefenseNIST 800-53 - Access ControlNetwork Traffic OverviewPCI - Alert OverviewPCI - Patch ManagementRule Detections OverviewRule ObservabilitySecurity Management OverviewSecurity Posture ManagementThreat Intelligence OverviewUser Lifecycle Audit

Alert Trends by Data SourceTop 10 High-Risk AssetsDetections from the Chrome Risks Curated Detection Rule PackAlerts Over TimeDetection Trend Over TimeDetections by CategoryDetections by SeverityTop Asset LocationsTop 10 Impacted ResourcesTop 10 DetectionsTop 10 Triggering UsersSeverity Distribution by Detection CategoryrulesAnomalous Data Transfer by UserIAM Alerts Over TimeRecent Cloud Threat DetectionsAlerts Over Time by SeverityLiving Off The Land Detections Over TimeLiving Off The Land Detections By SeverityLiving Off The Land DetectionsDetectionsAlertTop 100 Users by Detection CountMandiant Threat Defense Detections Over TimeDetections by Telemetry SourceTop 100 Hosts by Detection CountTop 100 Assets by Detection CountTop 100 Rules by Detection CountDetections by PlatformDetections by Event TypeTop 100 Domains by Detection CountTop 10 MITRE ATT&CK® Techniques (Log scale)Anomalous Login Location DetectionSuspicious Login ActivitiesGeo-Curated Detection UsersAlerts Over Time by ActionEvents by DescriptionTop 10 AlertsTop 10 Users (Generating Alerts)Alert CountEndpoint Count (Generating Alerts)Top 10 Endpoints (Generating Alerts)Systems Not Updating - Within 48 HoursRule Detection by Name Over TimeTop 10 Active RulesTop 10 Vendor Products Triggering DetectionsDetection Over Time by SeverityDetection by SeverityTop 10 IPs by Rule DetectionsTop 10 Devices by DetectionAverage Risk ScoreUsers at RiskTop 10 Destination IP by ActionLeast 10 Active RulesTop 10 Threat Signatures by Vendor ProductCommon MITRE ATT&CK Techniques and TacticsTop 10 Users by DetectionTop Users by Rule DetectionsTop 10 Rule Names by DetectionsDetection by Confidence LevelTop 10 Active Rule SetsTop 10 Source IP by ActionTop 10 Threat CategoriesTop 10 Hosts by Rule DetectionsRules Detection by Severity Over TimeRule detection over timeLeast 10 Active Rule SetsRule Detection by SeverityAssets at RiskP50 Ingestion Delay MinutesPer-Detection Latency Numbers - TOP 20P50 Ingestion to Detection Latency MinutesDetection LatencyP90 Ingestion to Detection Latency MinutesDetection Counts By Timing Details (primary or replay)Observed Threat Campaigns - Last 7 DaysObserved Threat Actors - Last 7 DaysTop 10 Threat Actors Targeting the OrganizationUEBA AlertsDetections Over TimeTop 10 Detections by NameTop 10 Cloud AlertsTop 10 Campaigns Targeting the OrganizationTop 10 Hosts by DetectionsThreat Campaigns by DetectionsDetections Over Time by Threat ActorDetections Over Time by IOCs TypeThreat Actors by DetectionsRecently Dormant Accounts

Dashboard name  |  Description  |  Chart name  |  Query   
---|---|---|---  
ISO 27001 – Technological Controls | Provides visibility into technological controls and encryption standards to support compliance and data-driven remediation.   
Note: Apply filters to refine the data. | Alert Trends by Data Source | 
    
    
    $Date = timestamp.get_date(detection.created_time.seconds)
    
    match:
        $Date
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Date desc  
  
ISO 27001 – Technological Controls | Provides visibility into technological controls and encryption standards to support compliance and data-driven remediation.   
Note: Apply filters to refine the data. | Top 10 High-Risk Assets | 
    
    
    detection.detection.risk_score > 0
    detection.collection_elements.references.event.principal.hostname != ""
    detection.collection_elements.references.event.metadata.product_name != ""
    detection.collection_elements.references.event.principal.ip != ""
    
    $Hostname = detection.collection_elements.references.event.principal.hostname
    $IP_Address = detection.collection_elements.references.event.principal.ip
    $Product_Name = detection.collection_elements.references.event.metadata.product_name
    
    match:
        $Hostname, $IP_Address, $Product_Name
    
    outcome:
        $Risk_Score = max(detection.detection.risk_score)
        $First_Time_Seen = timestamp.get_timestamp(min(detection.collection_elements.references.event.metadata.event_timestamp.seconds))
        $Last_Time_Seen = timestamp.get_timestamp(max(detection.collection_elements.references.event.metadata.event_timestamp.seconds))
    
    order:
        $Risk_Score desc
    
    limit:
        10  
  
Chrome Enterprise Premium Security Overview | Provides real-time insight into chrome-related security events, including sensitive data transfers, malware attempts, and password security issues.  | Detections from the Chrome Risks Curated Detection Rule Pack | 
    
    
    detection.detection.ruleset_category_display_name = "Chrome Enterprise Premium Threats"
    
    $Rule_Name = detection.detection.rule_name
    $User = strings.coalesce(detection.detection.outcomes["victim_name"], detection.detection.outcomes["victim_netid"], detection.collection_elements.references.event.principal.user.userid, detection.collection_elements.references.event.principal.user.user_display_name, detection.collection_elements.references.event.principal.user.email_addresses, detection.collection_elements.references.event.target.user.userid, detection.collection_elements.references.event.target.user.user_display_name, detection.collection_elements.references.event.target.user.email_addresses)
    $Hostname = strings.coalesce(detection.detection.outcomes["hostname"], detection.collection_elements.references.event.principal.hostname, detection.collection_elements.references.event.principal.asset.product_object_id)
    $IP = strings.coalesce(detection.collection_elements.references.event.principal.ip, detection.collection_elements.references.event.about.ip)
    $Severity = detection.detection.severity
    $File = strings.coalesce(detection.collection_elements.references.event.target.file.full_path, detection.collection_elements.references.event.target.resource.name, detection.collection_elements.references.event.target.url, detection.detection.outcomes["url"])
    $Risk_Score = detection.detection.outcomes["risk_score"]
    $Threat_Name = detection.collection_elements.references.event.security_result.threat_name
    
    match:
        $User, $Rule_Name, $Hostname, $IP, $File, $Risk_Score, $Severity, $Threat_Name
    
    outcome:
        $Description = array_distinct(detection.detection.description)
        $Count = count(detection.id)
    
    order:
        $Severity, $Count desc  
  
Cloud Key Management Overview | Provides centralized visibility into Cloud Key management, including Secrets and Certificates. Use these insights to track lifecycle changes and detect unauthorized activities. | Alerts Over Time | 
    
    
    detection.detection.ruleset_category_display_name = "Cloud Threats"
    detection.detection.alert_state = "ALERTING"
    detection.detection.rule_name = /Secrets|Key|KMS/ nocase
    
    $Date = timestamp.get_date(detection.collection_elements.references.event.metadata.event_timestamp.seconds)
    $Rule_Name = detection.detection.rule_name
    
    match:
      $Date, $Rule_Name
    
    outcome:
      $Count = count(detection.id)
    
    order:
      $Date desc  
  
Cloud security posture Overview | Provides Cloud security posture insights by tracking key metrics across Google Cloud, AWS and Azure. | Detection Trend Over Time | 
    
    
    $log_type = detection.collection_elements.references.event.metadata.log_type
    $log_type = /GCP|AWS|AZURE/
    $date = timestamp.get_date(detection.created_time.seconds)
    match:
    $date
    outcome:
    $event_count = count(detection.id)
    order:
    $date asc  
  
Cloud security posture Overview | Provides cloud security posture insights by tracking key metrics across Google Cloud, AWS and Azure. | Detections by Category | 
    
    
    $log_type = detection.collection_elements.references.event.metadata.log_type
    $log_type = /GCP|AWS|AZURE/
    $category = detection.collection_elements.references.event.security_result.category
    match:
    $category
    outcome:
    $event_count = count(detection.id)
    order:
    $event_count desc  
  
Cloud security posture Overview | Provides Cloud security posture insights by tracking key metrics across Google Cloud, AWS and Azure. | Detections by Severity | 
    
    
    $log_type = detection.collection_elements.references.event.metadata.log_type
    $log_type = /AWS|GCP|AZURE/
    $severity = detection.collection_elements.references.event.security_result.severity
    match:
    $severity
    outcome:
    $event_count = count(detection.id)
    order:
    $event_count desc  
  
Cloud security posture Overview | Provides Cloud security posture insights by tracking key metrics across Google Cloud, AWS and Azure. | Top Asset Locations | 
    
    
    $log_type = detection.collection_elements.references.event.metadata.log_type
    $log_type = /AWS|GCP|AZURE/
    $resource = detection.collection_elements.references.event.target.resource.name
    $location = detection.collection_elements.references.event.principal.ip_geo_artifact.location.country_or_region
    match:
    $location
    outcome:
    $event_count = count($resource)
    $latitude = max(detection.collection_elements.references.event.principal.ip_geo_artifact.location.region_latitude)
    $longitude = max(detection.collection_elements.references.event.principal.ip_geo_artifact.location.region_longitude)
    order:
    $event_count desc  
  
Cloud security posture Overview | Provides Cloud security posture insights by tracking key metrics across Google Cloud, AWS and Azure. | Top 10 Impacted Resources | 
    
    
    $log_type = detection.collection_elements.references.event.metadata.log_type
    $log_type = /AWS|GCP|AZURE/
    $targeted_resources = detection.collection_elements.references.event.target.resource.name
    $targeted_resources != ""
    match:
    $targeted_resources
    outcome:
    $event_count = count($targeted_resources)
    order:
    $event_count desc
    limit : 10
      
  
Cloud security posture Overview | Provides Cloud security posture insights by tracking key metrics across Google Cloud, AWS and Azure. | Top 10 Detections | 
    
    
    $log_type = detection.collection_elements.references.event.metadata.log_type
    $log_type = /GCP|AWS|AZURE/
    $rule_name = detection.detection.rule_name
    $rule_name != ""
    match:
    $rule_name
    outcome:
    $event_count = count(detection.id)
    order:
    $event_count desc
    limit:
    10  
  
Cloud security posture Overview | Provides Cloud security posture insights by tracking key metrics across Google Cloud, AWS and Azure. | Top 10 Triggering Users | 
    
    
    $log_type = detection.collection_elements.references.event.metadata.log_type
    $log_type = /GCP|AWS|AZURE/
    $user= detection.collection_elements.references.event.principal.user.userid
    $user != ""
    match:
    $user
    outcome:
    $event_count = count(detection.collection_elements.references.event.metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
Cloud security posture Overview | Provides Cloud security posture insights by tracking key metrics across Google Cloud, AWS and Azure. | Severity Distribution by Detection Category | 
    
    
    $log_type = detection.collection_elements.references.event.metadata.log_type
    $log_type = /GCP|AWS|AZURE/
    $category = detection.collection_elements.references.event.security_result.category
    $severity = detection.collection_elements.references.event.security_result.severity
    match:
    $severity,$category
    outcome:
    $event_count = count(detection.id)
    order:
    $event_count desc  
  
Cloud Storage Services Overview | Provides visibility into cloud storage activities and permission changes to help teams monitor alerts and maintain data integrity. Use these insights to track top users and identify unusual access patterns. | Alerts Over Time | 
    
    
    detection.detection.ruleset_category_display_name = "Cloud Threats"
    (detection.tags = /T1530|T1567.002/
    or detection.detection.rule_name = /storage|blob|bucket/ nocase)
    detection.detection.alert_state = "ALERTING"
    
    $Date = timestamp.get_date(detection.collection_elements.references.event.metadata.event_timestamp.seconds)
    $Rule_Name = detection.detection.rule_name
    
    match:
      $Date, $Rule_Name
    
    outcome:
      $Count = count(detection.id)
    
    order:
      $Date desc  
  
Data Ingestion and Health | Provides visibility into ingestion throughput and error counts to help teams quickly spot data flow issues. Use these metrics to monitor log distribution and ensure operational stability. | rules | 
    
    
    $a = rules.name
    match: $a  
  
GDPR Data Governance | Provides visibility into data access across EU regions, including access trends, non-EU access attempts, and top geolocations. It helps monitor compliance with GDPR regulations, detect unauthorized data access, and ensure secure handling of EU data. Note: Apply filters to display relevant results. | Anomalous Data Transfer by User | 
    
    
    strings.coalesce(detection.collection_elements.references.event.principal.location.country_or_region, detection.collection_elements.references.event.principal.ip_geo_artifact.location.country_or_region, detection.collection_elements.references.event.principal.location.name)
      = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    $Rule_Set = detection.detection.rule_set
    $Rule_Set = "Anomalous Total Bytes by User"
    $Employee_Name = strings.coalesce(detection.collection_elements.references.event.principal.user.userid,detection.collection_elements.references.event.principal.user.user_display_name,
    detection.collection_elements.references.event.principal.user.email_addresses)
    $Employee_ID = detection.collection_elements.references.event.principal.user.employee_id
    $Empolyee_Namespace = detection.collection_elements.references.event.principal.namespace
    
    match:
       $Employee_Name ,$Employee_ID, $Empolyee_Namespace,  $Rule_Set
    
    outcome:
        $Count = count_distinct(detection.id)
    
    order:
        $Count Desc  
  
IAM Security Operations | A high-level overview for daily monitoring. It focuses on real-time anomalies, active threats, and high-risk events to enable rapid incident detection and response. Use the available filters to narrow down the results as required. | IAM Alerts Over Time | 
    
    
    detection.detection.rule_set_display_name = "Admin Action"
    or detection.detection.rule_set_display_name = "Potential Workspace Account Compromise"
    or detection.detection.rule_set_display_name = "Suspicious Workspace Administrative Actions"
    or detection.detection.rule_set_display_name = "AWS - Identity"
    or detection.detection.rule_set_display_name = "AWS - Organization"
    or detection.detection.rule_set_display_name = "Azure - Identity"
    or detection.detection.rule_set_display_name = "Azure - Organization"
    or detection.detection.rule_set_display_name = "IAM Abuse"
    or detection.detection.rule_set_display_name = "New Login by User to Device"
    or detection.detection.rule_set_display_name = "Anomalous Authentication Events by User"
    or detection.detection.rule_set_display_name = "Failed Authentications by Device"
    or detection.detection.rule_set_display_name = "Failed Authentications by User"
    or detection.detection.rule_set_display_name = "Anomalous Inbound Bytes by User"
    or detection.detection.rule_set_display_name = "Anomalous Total Bytes by User"
    or detection.detection.rule_set_display_name = "Brute Force then Successful Login by User"
    or detection.detection.rule_set_display_name = "Anomalous or Excessive Logins for a Newly Created User"
    or detection.detection.rule_set_display_name = "Anomalous or Excessive Suspicious Actions for a Newly Created User"
    or detection.detection.rule_set_display_name = "Excessive Alerts by User"
    detection.detection.alert_state = "ALERTING"
    
    $Date = timestamp.get_date(detection.collection_elements.references.event.metadata.event_timestamp.seconds)
    $Rule_Name = detection.detection.rule_name
    
    match:
        $Date, $Rule_Name
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Date desc  
  
ISO 27001 - Organizational Controls | Provides visibility into organizational security controls and compliance performance based on ISO 27001 standards. It helps track audit results and identify areas for improvement.   
Note: Apply filters to refine the results. | Recent Cloud Threat Detections | 
    
    
    detection.detection.ruleset_category_display_name = "Cloud Threats"
    
    $Date = timestamp.get_timestamp(detection.collection_elements.references.event.metadata.event_timestamp.seconds)
    $Rule_Name = detection.detection.rule_name
    $User = strings.coalesce(detection.collection_elements.references.event.principal.user.userid, detection.collection_elements.references.event.principal.user.email_addresses)
    $Source_IP = strings.coalesce(detection.collection_elements.references.event.principal.asset.ip, detection.collection_elements.references.event.principal.ip)
    $Host = strings.coalesce(detection.collection_elements.references.event.principal.asset.hostname, detection.collection_elements.references.event.principal.hostname)
    
    match:
        $Date, $Rule_Name, $User, $Source_IP, $Host
    
    order:
        $Date desc  
  
ISO 27001 - Organizational Controls | Provides visibility into organizational security controls and compliance performance based on ISO 27001 standards. It helps track audit results and identify areas for improvement.   
Note: Apply filters to refine the results. | Alerts Over Time by Severity | 
    
    
    $Date = timestamp.get_date(detection.created_time.seconds)
    $Severity = detection.collection_elements.references.event.security_result.severity
    $Severity != "UNKNOWN_SEVERITY"
    
    match:
        $Date, $Severity
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Date desc  
  
Living Off the Land Activity | Provides critical insights into the potential misuse of trusted system tools like Rundll32 and Regsvr32. It tracks and visualizes activity commonly leveraged by advanced threats to evade detection and exploit system utilities. | Living Off The Land Detections Over Time | 
    
    
    detection.detection.rule_set = "89adf0db-5d29-0a04-c926-f8c2a58f5d1b"
    
    $Rule_Name = detection.detection.rule_name
    $Severity = detection.detection.severity
    $Risk_Score = detection.detection.risk_score
    $Date = timestamp.get_date(detection.collection_elements.references.event.metadata.event_timestamp.seconds)
    
    match:
        $Rule_Name, $Severity, $Risk_Score, $Date
    outcome:
        $Count = count(detection.detection.threat_id)
    order:
        $Count desc  
  
Living Off the Land Activity | Provides critical insights into the potential misuse of trusted system tools like Rundll32 and Regsvr32. It tracks and visualizes activity commonly leveraged by advanced threats to evade detection and exploit system utilities. | Living Off The Land Detections By Severity | 
    
    
    $event.detection.detection.rule_set = "89adf0db-5d29-0a04-c926-f8c2a58f5d1b"
    
    $Rule_Name = $event.detection.detection.rule_name
    $Severity = $event.detection.detection.severity
    $Risk_Score = $event.detection.detection.risk_score
    
    match:
        $Rule_Name, $Severity, $Risk_Score
    limit:
        50  
  
Living Off the Land Activity | Provides critical insights into the potential misuse of trusted system tools like Rundll32 and Regsvr32. It tracks and visualizes activity commonly leveraged by advanced threats to evade detection and exploit system utilities. | Living Off The Land Detections | 
    
    
    $event.detection.detection.rule_set = "89adf0db-5d29-0a04-c926-f8c2a58f5d1b"
    
    $Rule_Name = $event.detection.detection.rule_name
    
    match:
        $Rule_Name
    outcome:
        $Last_Detection = timestamp.get_timestamp(max($event.detection.collection_elements.references.event.metadata.event_timestamp.seconds))
    order:
        $Last_Detection desc  
  
Main | Provides a summary of data ingestion health and detected IoCs, and provides a global perspective on potential threats. | Detections | 
    
    
    detection.id != ""
    outcome:
       $count = count(detection.id)
      
  
Main | Provides a summary of data ingestion health and detected IoCs, and provides a global perspective on potential threats. | Alert | 
    
    
    detection.id != ""
    outcome:
       $count = count_distinct(detection.id)
      
  
Mandiant Threat Defense | Provides clear visibility into the proactive threat hunting performed by Mandiant in your environment. It details ongoing and completed hunt activities while highlighting trends uncovered through the hunting process. | Top 100 Users by Detection Count | 
    
    
    $rule_pack_name = detection.detection.rule_set_display_name
    $rule_name = detection.detection.rule_name
    $username = group(detection.collection_elements.references.event.principal.user.userid, detection.collection_elements.references.event.src.user.userid, detection.collection_elements.references.event.target.user.userid)
    
    $username != ""
    
    re.regex($rule_pack_name, `^Mandiant.*`)
    
    match:
        $username
    
    outcome:
        $count = count_distinct(detection.id)
        $unique_rules = count_distinct($rule_name)
    
    order:
        $count desc
    
    limit:
        100  
  
Mandiant Threat Defense | Provides clear visibility into the proactive threat hunting performed by Mandiant in your environment. It details ongoing and completed hunt activities while highlighting trends uncovered through the hunting process. | Mandiant Threat Defense Detections Over Time | 
    
    
    $rule_pack_name = detection.detection.rule_set_display_name
    $date = timestamp.get_date(detection.created_time.seconds)
    
    re.regex($rule_pack_name, `^Mandiant.*`)
    
    match:
        $date
    
    outcome:
        $count = count_distinct(detection.id)
    
    order:
        $date asc  
  
Mandiant Threat Defense | Provides clear visibility into the proactive threat hunting performed by Mandiant in your environment. It details ongoing and completed hunt activities while highlighting trends uncovered through the hunting process. | Detections by Telemetry Source | 
    
    
    $rule_pack_name = detection.detection.rule_set_display_name
    $rule_name = detection.detection.rule_name
    $vendor_name = detection.collection_elements.references.event.metadata.vendor_name
    $product_name = detection.collection_elements.references.event.metadata.product_name
    
    $vendor_name != ""
    $product_name != ""
    
    re.regex($rule_pack_name, `^Mandiant.*`)
    
    match:
        $vendor_name, $product_name
    
    outcome:
        $count = count_distinct(detection.id)
    
    order:
        $count desc
    
    limit:
        10  
  
Mandiant Threat Defense | Provides clear visibility into the proactive threat hunting performed by Mandiant in your environment. It details ongoing and completed hunt activities while highlighting trends uncovered through the hunting process. | Detections | 
    
    
    $rule_pack_name = detection.detection.rule_set_display_name
    re.regex($rule_pack_name, `^Mandiant.*`)
    
    outcome:
        $count = count_distinct(detection.id)
      
  
Mandiant Threat Defense | Provides clear visibility into the proactive threat hunting performed by Mandiant in your environment. It details ongoing and completed hunt activities while highlighting trends uncovered through the hunting process. | Top 100 Hosts by Detection Count | 
    
    
    $rule_pack_name = detection.detection.rule_set_display_name
    $rule_name = detection.detection.rule_name
    $hostname = group(detection.collection_elements.references.event.principal.hostname, detection.collection_elements.references.event.src.hostname, detection.collection_elements.references.event.target.hostname)
    
    $hostname != ""
    
    re.regex($rule_pack_name, `^Mandiant.*`)
    
    match:
        $hostname
    
    outcome:
        $count = count_distinct(detection.id)
        $unique_rules = count_distinct($rule_name)
    
    order:
        $count desc
    
    limit:
        100  
  
Mandiant Threat Defense | Provides clear visibility into the proactive threat hunting performed by Mandiant in your environment. It details ongoing and completed hunt activities while highlighting trends uncovered through the hunting process. | Top 100 Assets by Detection Count | 
    
    
    $rule_pack_name = detection.detection.rule_set_display_name
    $rule_name = detection.detection.rule_name
    $asset_id = group(detection.collection_elements.references.event.principal.asset_id, detection.collection_elements.references.event.src.asset_id, detection.collection_elements.references.event.target.asset_id)
    
    $asset_id != ""
    
    re.regex($rule_pack_name, `^Mandiant.*`)
    
    match:
        $asset_id
    
    outcome:
        $count = count_distinct(detection.id)
        $unique_rules = count_distinct($rule_name)
    
    order:
        $count desc
    
    limit:
        100  
  
Mandiant Threat Defense | Provides clear visibility into the proactive threat hunting performed by Mandiant in your environment. It details ongoing and completed hunt activities while highlighting trends uncovered through the hunting process. | Top 100 Rules by Detection Count | 
    
    
    $rule_pack_name = detection.detection.rule_set_display_name
    $rule_name = detection.detection.rule_name
    $asset_id = group(detection.collection_elements.references.event.principal.asset_id, detection.collection_elements.references.event.src.asset_id, detection.collection_elements.references.event.target.asset_id)
    
    re.regex($rule_pack_name, `^Mandiant.*`)
    
    match:
        $rule_name
    
    outcome:
        $count = count_distinct(detection.id)
        $asset_count = count_distinct($asset_id)
    
    order:
        $count desc
    
    limit:
        100  
  
Mandiant Threat Defense | Provides clear visibility into the proactive threat hunting performed by Mandiant in your environment. It details ongoing and completed hunt activities while highlighting trends uncovered through the hunting process. | Detections by Platform | 
    
    
    $rule_pack_name = detection.detection.rule_set_display_name
    $rule_name = detection.detection.rule_name
    $platform = detection.collection_elements.references.event.principal.asset.platform_software.platform
    
    $platform != "UNKNOWN_PLATFORM"
    
    re.regex($rule_pack_name, `^Mandiant.*`)
    
    match:
        $platform
    
    outcome:
        $count = count_distinct(detection.id)
    
    order:
        $count desc
    
    limit:
        10  
  
Mandiant Threat Defense | Provides clear visibility into the proactive threat hunting performed by Mandiant in your environment. It details ongoing and completed hunt activities while highlighting trends uncovered through the hunting process. | Detections by Event Type | 
    
    
    $rule_pack_name = detection.detection.rule_set_display_name
    $rule_name = detection.detection.rule_name
    $event_type = detection.collection_elements.references.event.metadata.event_type
    
    re.regex($rule_pack_name, `^Mandiant.*`)
    
    match:
        $event_type
    
    outcome:
        $count = count_distinct(detection.id)
    
    order:
        $count desc
    
    limit:
        10  
  
Mandiant Threat Defense | Provides clear visibility into the proactive threat hunting performed by Mandiant in your environment. It details ongoing and completed hunt activities while highlighting trends uncovered through the hunting process. | Top 100 Domains by Detection Count | 
    
    
    $rule_pack_name = detection.detection.rule_set_display_name
    $rule_name = detection.detection.rule_name
    
    $domain = group(detection.collection_elements.references.event.principal.administrative_domain, detection.collection_elements.references.event.target.administrative_domain, detection.collection_elements.references.event.about.administrative_domain, detection.collection_elements.references.event.principal.asset.network_domain, detection.collection_elements.references.event.target.asset.network_domain, detection.collection_elements.references.event.about.asset.network_domain)
    
    $domain != ""
    
    re.regex($rule_pack_name, `^Mandiant.*`)
    
    match:
        $domain
    
    outcome:
        $count = count_distinct(detection.id)
        $unique_rules = count_distinct($rule_name)
    
    order:
        $count desc
    
    limit:
        100  
  
Mandiant Threat Defense | Provides clear visibility into the proactive threat hunting performed by Mandiant in your environment. It details ongoing and completed hunt activities while highlighting trends uncovered through the hunting process. | Top 10 MITRE ATT&CK® Techniques (Log scale) | 
    
    
    $rule_pack_name = detection.detection.rule_set_display_name
    $rule_name = detection.detection.rule_name
    
    re.regex($rule_pack_name, `^Mandiant.*`)
    
    $mitre_technique = if(detection.detection.rule_labels["technique"] = "", "Unassigned", detection.detection.rule_labels["technique"])
    
    match:
        $mitre_technique
    
    outcome:
        $count = count_distinct(detection.id)
    
    order:
        $count desc
    
    limit:
        10  
  
NIST 800-53 - Access Control | Provides visibility into NIST 800-53 access control trends and geolocation risks. Ensure the `NIST_Compliance_Assets` reference list is created for charts to load and scope data. | Anomalous Login Location Detection | 
    
    
    detection.collection_elements.references.event.security_result.action = "ALLOW"
    detection.detection.rule_name = "Login from Country Never Before Seen for a User Group"
    
    $Country = strings.coalesce(detection.collection_elements.references.event.principal.location.country_or_region, detection.collection_elements.references.event.principal.ip_geo_artifact.location.country_or_region)
    $Rulename = detection.detection.rule_name
    $User = strings.coalesce(detection.collection_elements.references.event.principal.user.userid,detection.collection_elements.references.event.principal.user.user_display_name,
    detection.collection_elements.references.event.principal.user.email_addresses,detection.collection_elements.references.event.target.user.userid,detection.collection_elements.references.event.target.user.user_display_name,detection.collection_elements.references.event.target.user.email_addresses)
    
    match:
         $User, $Rulename, $Country
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc  
  
NIST 800-53 - Access Control | Provides visibility into NIST 800-53 access control trends and geolocation risks. Ensure the `NIST_Compliance_Assets` reference list is created for charts to load and scope data. | Suspicious Login Activities | 
    
    
    detection.detection.rule_name = "Brute Force then Successful Login by User"
    
    $Country = strings.coalesce(detection.collection_elements.references.event.principal.location.country_or_region, detection.collection_elements.references.event.principal.ip_geo_artifact.location.country_or_region)
    $Rulename = detection.detection.rule_name
    $User = strings.coalesce(detection.collection_elements.references.event.principal.user.userid,detection.collection_elements.references.event.principal.user.user_display_name,
    detection.collection_elements.references.event.principal.user.email_addresses,detection.collection_elements.references.event.target.user.userid,detection.collection_elements.references.event.target.user.user_display_name,detection.collection_elements.references.event.target.user.email_addresses)
    
    match:
         $User, $Rulename, $Country
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc  
  
Network Traffic Overview | Provides real-time monitoring of cloud and on-premises network traffic by IP, protocol, vendor alert and region, enabling effective analysis of traffic volume and potential issues | Geo-Curated Detection Users | 
    
    
    detection.collection_elements.references.event.security_result.action = "ALLOW"
    
    $Country = strings.coalesce(detection.collection_elements.references.event.principal.location.country_or_region, detection.collection_elements.references.event.principal.ip_geo_artifact.location.country_or_region)
    $Rulename = detection.detection.rule_name
    $Rulename = "Azure Multiple Geolocation Login Success" or $Rulename = "Login from Country Never Before Seen for a User Group"
    $User = strings.coalesce(detection.collection_elements.references.event.principal.user.userid,detection.collection_elements.references.event.principal.user.user_display_name,
    detection.collection_elements.references.event.principal.user.email_addresses,detection.collection_elements.references.event.target.user.userid,detection.collection_elements.references.event.target.user.user_display_name,detection.collection_elements.references.event.target.user.email_addresses)
    
    
    match:
        $Country, $Rulename, $User, detection.collection_elements.references.event.metadata.event_type
    
    outcome:
        $Count = count($Country)
    
    order:
        $Count desc
    
    limit:
        10  
  
PCI - Alert Overview | Provides a consolidated view of alerts and insights regarding potential security breaches affecting PCI standards.   
Note: Requires the `PCI_ASSETS` reference list to load and scope data correctly. | Alerts Over Time by Action | 
    
    
    (detection.collection_elements.references.event.principal.hostname in %PCI_Assets or detection.collection_elements.references.event.principal.asset.hostname in %PCI_Assets or detection.collection_elements.references.event.target.hostname in %PCI_Assets or detection.collection_elements.references.event.target.asset.hostname in %PCI_Assets)
    
    $Date = timestamp.get_date(detection.created_time.seconds)
    $Action = detection.collection_elements.references.event.security_result.action
    
    match:
        $Date,$Action
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Date asc  
  
PCI - Alert Overview | Provides a consolidated view of alerts and insights regarding potential security breaches affecting PCI standards.   
Note: Requires the `PCI_ASSETS` reference list to load and scope data correctly. | Events by Description | 
    
    
    (detection.collection_elements.references.event.principal.hostname in %PCI_Assets or detection.collection_elements.references.event.principal.asset.hostname in %PCI_Assets or detection.collection_elements.references.event.target.hostname in %PCI_Assets or detection.collection_elements.references.event.target.asset.hostname in %PCI_Assets)
    
    $Event_Name = detection.collection_elements.references.event.metadata.event_type
    $Description = strings.coalesce(detection.collection_elements.references.event.security_result.summary,detection.collection_elements.references.event.security_result.description,detection.collection_elements.references.event.metadata.description)
    $Log_Type = detection.collection_elements.references.event.metadata.log_type
    $Source_IP = strings.coalesce(detection.collection_elements.references.event.principal.ip, detection.collection_elements.references.event.principal.asset.ip)
    $Destination_IP = strings.coalesce(detection.collection_elements.references.event.target.ip, detection.collection_elements.references.event.target.asset.ip)
    $Action = detection.collection_elements.references.event.security_result.action
    $Destination_Hostname = strings.coalesce(detection.collection_elements.references.event.target.hostname, detection.collection_elements.references.event.target.asset.hostname)
    $File = detection.collection_elements.references.event.target.process.file.full_path
    $User = strings.coalesce(detection.collection_elements.references.event.principal.user.userid, detection.collection_elements.references.event.principal.user.user_display_name, detection.collection_elements.references.event.principal.user.email_addresses, detection.collection_elements.references.event.target.user.userid, detection.collection_elements.references.event.target.user.user_display_name, detection.collection_elements.references.event.target.user.email_addresses)
    
    match:
        $Description, $Event_Name,$User, $Source_IP, $Destination_IP, $Action, $Destination_Hostname, $File, $Log_Type
    
    outcome:
        $Count = count(detection.collection_elements.references.event.metadata.id)
    
    order:
        $Count desc  
  
PCI - Alert Overview | Provides a consolidated view of alerts and insights regarding potential security breaches affecting PCI standards.   
Note: Requires the `PCI_ASSETS` reference list to load and scope data correctly. | Top 10 Alerts | 
    
    
    (detection.collection_elements.references.event.principal.hostname in %PCI_Assets or detection.collection_elements.references.event.principal.asset.hostname in %PCI_Assets or detection.collection_elements.references.event.target.hostname in %PCI_Assets or detection.collection_elements.references.event.target.asset.hostname in %PCI_Assets)
    
    $Rule_Name = detection.detection.rule_name
    $Severity = detection.detection.severity
    
    match:
        $Rule_Name,$Severity
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
    
    limit:
        10  
  
PCI - Alert Overview | Provides a consolidated view of alerts and insights regarding potential security breaches affecting PCI standards.   
Note: Requires the `PCI_ASSETS` reference list to load and scope data correctly. | Top 10 Users (Generating Alerts) | 
    
    
    (detection.collection_elements.references.event.principal.hostname in %PCI_Assets or detection.collection_elements.references.event.principal.asset.hostname in %PCI_Assets or detection.collection_elements.references.event.target.hostname in %PCI_Assets or detection.collection_elements.references.event.target.asset.hostname in %PCI_Assets)
    
    $User = strings.coalesce(detection.collection_elements.references.event.principal.user.userid,detection.collection_elements.references.event.principal.user.user_display_name,detection.collection_elements.references.event.principal.user.email_addresses,detection.collection_elements.references.event.target.user.userid, detection.collection_elements.references.event.target.user.user_display_name,detection.collection_elements.references.event.target.user.email_addresses)
    
    match:
        $User
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
    
    limit:
        10  
  
PCI - Alert Overview | Provides a consolidated view of alerts and insights regarding potential security breaches affecting PCI standards.   
Note: Requires the `PCI_ASSETS` reference list to load and scope data correctly. | Alert Count | 
    
    
    (detection.collection_elements.references.event.principal.hostname in %PCI_Assets or detection.collection_elements.references.event.principal.asset.hostname in %PCI_Assets or detection.collection_elements.references.event.target.hostname in %PCI_Assets or detection.collection_elements.references.event.target.asset.hostname in %PCI_Assets)
    
    outcome:
        $Count = count(detection.id)  
  
PCI - Alert Overview | Provides a consolidated view of alerts and insights regarding potential security breaches affecting PCI standards.   
Note: Requires the `PCI_ASSETS` reference list to load and scope data correctly. | Endpoint Count (Generating Alerts) | 
    
    
    (detection.collection_elements.references.event.principal.hostname in %PCI_Assets or detection.collection_elements.references.event.principal.asset.hostname in %PCI_Assets or detection.collection_elements.references.event.target.hostname in %PCI_Assets or detection.collection_elements.references.event.target.asset.hostname in %PCI_Assets)
    
    $Hostname = strings.coalesce(detection.collection_elements.references.event.principal.hostname,detection.collection_elements.references.event.principal.asset.hostname,detection.collection_elements.references.event.target.hostname,detection.collection_elements.references.event.target.asset.hostname)
    
    outcome:
        $Count = count_distinct($Hostname)
    
      
  
PCI - Alert Overview | Provides a consolidated view of alerts and insights regarding potential security breaches affecting PCI standards.   
Note: Requires the `PCI_ASSETS` reference list to load and scope data correctly. | Top 10 Endpoints (Generating Alerts) | 
    
    
    (detection.collection_elements.references.event.principal.hostname in %PCI_Assets or detection.collection_elements.references.event.principal.asset.hostname in %PCI_Assets or detection.collection_elements.references.event.target.hostname in %PCI_Assets or detection.collection_elements.references.event.target.asset.hostname in %PCI_Assets)
    
    $Hostname = strings.coalesce(detection.collection_elements.references.event.principal.hostname,detection.collection_elements.references.event.principal.asset.hostname,detection.collection_elements.references.event.target.hostname,detection.collection_elements.references.event.target.asset.hostname)
    
    match:
        $Hostname
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
    
    limit:
        10  
  
PCI - Patch Management | Provides a comprehensive view of the patch management lifecycle to help you monitor and manage system updates effectively.  
Note: Requires the `Patch_UPDATES` and `PCI_ASSETS` reference lists to load and scope data correctly. | Systems Not Updating - Within 48 Hours | 
    
    
    strings.coalesce($event.detection.collection_elements.references.event.principal.asset.hostname, $event.detection.collection_elements.references.event.principal.hostname) in %PCI_Assets
    $Rule_Name = $event.detection.detection.rule_name
    $Rule_Name = "systems_not_updating_within_48_hours"
    $Hostname = strings.coalesce($event.detection.collection_elements.references.event.principal.asset.hostname, $event.detection.collection_elements.references.event.principal.hostname)
    
    
    match:
        $Hostname
    limit:
        50  
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Rule Detection by Name Over Time | 
    
    
    $rulename = detection.detection.rule_name
    $date = timestamp.get_date(detection.detection_time.seconds)
    match:
        $rulename, $date
    outcome:
        $detection_count = count_distinct(detection.id)
    order:
        $date
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 Active Rules | 
    
    
    $Rulename = detection.detection.rule_name
    
    match:
        $Rulename
    
    outcome:
        $Count = count_distinct(detection.id)
    
    order:
        $Count desc
    
    limit:
            10
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 Vendor Products Triggering Detections | 
    
    
    $Product_Name = detection.collection_elements.references.event.metadata.product_name
    
    match:
        $Product_Name
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
    
    limit:
        10  
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Detection Over Time by Severity | 
    
    
    $Severity = detection.detection.severity
    $Date = timestamp.get_date(detection.detection_time.seconds)
    
    match:
        $Date, $Severity
    
    outcome:
        $Count = count_distinct(detection.id)
    
    order:
        $Date asc
    
    
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Detection by Severity | 
    
    
    $Rulename = detection.detection.rule_name
    $Severity = detection.detection.severity
    
    match:
        $Rulename,$Severity
    
    outcome:
        $Count = count_distinct(detection.id)
    
    order:
        $Severity desc
    
    
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 IPs by Rule Detections | 
    
    
    $ip = group(
        detection.collection_elements.references.event.principal.ip,
        detection.collection_elements.references.event.target.ip,
        detection.collection_elements.references.event.src.ip
        )
    $ip != ""
    match:
      $ip
    outcome:
      $count = count(detection.id)
    order:
      $count desc
    limit: 10
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 Devices by Detection | 
    
    
    $Hostname = strings.coalesce(detection.collection_elements.references.event.principal.hostname, detection.collection_elements.references.event.principal.asset.hostname, detection.collection_elements.references.event.target.hostname,detection.collection_elements.references.event.target.asset.hostname)
    $Severity = detection.detection.severity
    
    match:
        $Hostname, $Severity
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
    
    limit:
        10  
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Average Risk Score | 
    
    
    $Rule_Set = detection.detection.rule_set_display_name
    
    match:
        $Rule_Set
    
    outcome:
        $Detection_Count = count(detection.id)
        $Average_Risk_Score = math.round(sum(detection.detection.risk_score)/count(detection.id),2)
    
    order:
        $Average_Risk_Score desc
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Users at Risk | 
    
    
    detection.detection.risk_score > 0
    detection.collection_elements.references.event.principal.user.userid != ""
    detection.collection_elements.references.event.metadata.product_name != ""
    
    $User = detection.collection_elements.references.event.principal.user.userid
    $Product_Name = detection.collection_elements.references.event.metadata.product_name
    
    match:
        $User, $Product_Name
    
    outcome:
        $Risk_Score = max(detection.detection.risk_score)
        $Count = count(detection.id)
        $First_Time_Seen = timestamp.get_timestamp(min(detection.collection_elements.references.event.metadata.event_timestamp.seconds))
        $Last_Time_Seen = timestamp.get_timestamp(max(detection.collection_elements.references.event.metadata.event_timestamp.seconds))
    
    order:
        $Risk_Score desc, $Count desc  
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 Destination IP by Action | 
    
    
    $Destination_IP = strings.coalesce(detection.collection_elements.references.event.target.ip,detection.collection_elements.references.event.target.asset.ip)
    $Action = detection.collection_elements.references.event.security_result.action
    
    match:
        $Destination_IP,$Action
    
     outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
    
    limit:
        10  
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Least 10 Active Rules | 
    
    
    $Rule_Name = detection.detection.rule_name
    
    match:
        $Rule_Name
    
    outcome:
        $Count = count_distinct(detection.id)
    
    order:
        $Count asc
    
    limit:
        10  
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 Threat Signatures by Vendor Product | 
    
    
    $Threat_Signature = strings.coalesce(detection.collection_elements.references.event.security_result.threat_name, detection.detection.detection_fields["threat_signature"])
    
    $Product_Name = detection.collection_elements.references.event.metadata.product_name
    
    match:
        $Threat_Signature, $Product_Name
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
    
    limit:
        10   
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Common MITRE ATT&CK Techniques and Tactics | 
    
    
    $Tactic_ID = detection.collection_elements.references.event.security_result.attack_details.tactics.id
    $Tactic_Name = detection.collection_elements.references.event.security_result.attack_details.tactics.name
    $Tactic_Name != ""
    $Technique_Name = detection.collection_elements.references.event.security_result.attack_details.techniques.name
    $Tectinque_ID = detection.collection_elements.references.event.security_result.attack_details.techniques.id
    $Sub_Technique = detection.collection_elements.references.event.security_result.attack_details.techniques.subtechnique_name
    
    match:
        $Tactic_Name, $Tactic_ID, $Technique_Name, $Tectinque_ID, $Sub_Technique
    
    outcome:
    
        $Ruleset_Count = count_distinct(detection.detection.rule_set_display_name)
        $Count = count_distinct(detection.id)
    
    
    order:
        $Count desc
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 Users by Detection | 
    
    
    $User = strings.coalesce(detection.collection_elements.references.event.principal.user.userid,detection.collection_elements.references.event.principal.user.user_display_name,
    detection.collection_elements.references.event.principal.user.email_addresses,detection.collection_elements.references.event.target.user.userid,detection.collection_elements.references.event.target.user.user_display_name,detection.collection_elements.references.event.target.user.email_addresses)
    $Severity = detection.detection.severity
    
    match:
        $User, $Severity
    
     outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
    
    limit:
        10  
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top Users by Rule Detections | 
    
    
    $user = group(
      detection.collection_elements.references.event.src.user.userid,
      detection.collection_elements.references.event.principal.user.userid,
      detection.collection_elements.references.event.target.user.userid
      )
    $user != ""
    match:
      $user
    outcome:
      $count = count(detection.id)
    order:
      $count desc
    limit: 10
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 Rule Names by Detections | 
    
    
    $rulename = detection.detection.rule_name
    match:
        $rulename
    outcome:
        $detection_count = count_distinct(detection.id)
    order:
        $detection_count desc
    limit:
        10
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Detection by Confidence Level | 
    
    
    $Rule_Name = detection.detection.rule_name
    $Confidence_Level = detection.detection.confidence
    $Risk_Score = detection.detection.risk_score
    $Threat_Name = detection.collection_elements.references.event.security_result.threat_name
    $Severity = detection.detection.severity
    
    match:
       $Rule_Name,$Severity,$Risk_Score, $Confidence_Level,$Threat_Name
    
    outcome:
       $Count = count_distinct(detection.id)
    
    order:
        $Risk_Score desc  
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 Active Rule Sets | 
    
    
    $Ruleset = detection.detection.rule_set_display_name
    
    match:
        $Ruleset
    
    outcome:
        $Count = count_distinct(detection.id)
    
    order:
        $Count desc
    
    limit:
        10
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 Source IP by Action | 
    
    
    $Action = detection.collection_elements.references.event.security_result.action
    $Source_IP = strings.coalesce(detection.collection_elements.references.event.principal.ip,detection.collection_elements.references.event.principal.asset.ip)
    
    
    match:
        $Action, $Source_IP
    
     outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
    
    limit:
        10  
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 Threat Categories | 
    
    
    $Category = detection.collection_elements.references.event.security_result.category
    $Category_Details= detection.collection_elements.references.event.security_result.category_details
    $Threat_Name = detection.collection_elements.references.event.security_result.threat_name
    
    match:
       $Category, $Category_Details
    
    outcome:
        $Threat_Type = array_distinct($Threat_Name)
        $Count = count_distinct(detection.id)
    
    order:
        $Count desc
    
    limit:
        10
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Top 10 Hosts by Rule Detections | 
    
    
    $host = group(detection.collection_elements.references.event.src.hostname,detection.collection_elements.references.event.principal.hostname,detection.collection_elements.references.event.target.hostname)
    $host != ""
    match:
      $host
    outcome:
      $count = count(detection.id)
    order:
      $count desc
    limit: 10
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Rules Detection by Severity Over Time | 
    
    
    $severity = detection.detection.rule_labels["severity"]
    $severity != ""
    $detection_time = timestamp.get_date(detection.detection_time.seconds)
    match:
       $severity, $detection_time
    outcome:
       $count = count_distinct(detection.id)
    
    order:
        $detection_time
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Rule detection over time | 
    
    
    $date = timestamp.get_date(detection.detection_time.seconds)
    match:
        $date
    outcome:
        $total=count_distinct(detection.id)
    order:
        $date
    
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Least 10 Active Rule Sets | 
    
    
    $Rule_Set = detection.detection.rule_set_display_name
    
    match:
        $Rule_Set
    
    outcome:
        $Count = count_distinct(detection.id)
    
    order:
        $Count asc
    
    limit:
        10  
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Rule Detection by Severity | 
    
    
    $severity = detection.detection.rule_labels["severity"]
    $severity != ""
    match:
       $severity
    outcome:
       $count = count_distinct(detection.id)
      
  
Rule Detections Overview | Provides an analysis of detection rules and threat patterns to improve visibility. Use these insights to evaluate rule performance and strengthen incident response.   
Note: Apply filters are to refine the results. | Assets at Risk | 
    
    
    detection.detection.risk_score > 0
    detection.collection_elements.references.event.principal.hostname != ""
    detection.collection_elements.references.event.metadata.product_name != ""
    
    $Hostname = detection.collection_elements.references.event.principal.hostname
    $IP_Address = detection.collection_elements.references.event.principal.ip
    $Product_Name = detection.collection_elements.references.event.metadata.product_name
    
    match:
        $Hostname, $IP_Address, $Product_Name
    
    outcome:
        $Risk_Score = max(detection.detection.risk_score)
        $Count = count(detection.id)
        $First_Time_Seen = timestamp.get_timestamp(min(detection.collection_elements.references.event.metadata.event_timestamp.seconds))
        $Last_Time_Seen = timestamp.get_timestamp(max(detection.collection_elements.references.event.metadata.event_timestamp.seconds))
    
    order:
        $Risk_Score desc, $Count desc  
  
Rule Observability | This dashboard showcases the underlying metrics emitted by rule executions. | P50 Ingestion Delay Minutes | 
    
    
    detection.type = "RULE_DETECTION"
    detection.latency_metrics.newest_ingestion_time.seconds - detection.latency_metrics.newest_event_time.seconds < 3600
    $rule_id = detection.detection.rule_id
    $rule_name = detection.detection.rule_name
    
    //detection.detection.rule_type = "MULTI_EVENT"
    
    $did = detection.id
    $day = timestamp.get_date(detection.created_time.seconds)
    
    
    detection.latency_metrics.newest_ingestion_time.seconds != 0
    detection.latency_metrics.newest_event_time.seconds != 0
    
    
    match:
        $day
    outcome:
        $p50_ingest_to_detection_delay = math.round(window.percentile(detection.latency_metrics.newest_ingestion_time.seconds - detection.latency_metrics.newest_event_time.seconds, 50) /60, 2)
    
    order:
        $p50_ingest_to_detection_delay desc  
  
Rule Observability | This dashboard showcases the underlying metrics emitted by rule executions. | Per-Detection Latency Numbers - TOP 20 | 
    
    
    $detect_id = detection.id
    $rule_name = detection.detection.rule_name
    $rule_id = detection.detection.rule_id
    $detectionTime = detection.created_time.seconds
    
    detection.type = "RULE_DETECTION"
    
    detection.latency_metrics.newest_ingestion_time.seconds != 0
    detection.latency_metrics.newest_event_time.seconds != 0
    
    detection.collection_elements.references.event.metadata.log_type != ""
    $logType = detection.collection_elements.references.event.metadata.log_type
    
    match:
      $rule_name, $detect_id
    
    outcome:
      $ingestion_deleay = math.round( (max(detection.latency_metrics.newest_ingestion_time.seconds) - max(detection.latency_metrics.newest_event_time.seconds)) / 60, 1)
      $ingestion_to_detection = math.round((max(detection.created_time.seconds) - max(detection.latency_metrics.newest_ingestion_time.seconds)) / 60, 1)
      $event_to_deteciton = math.round((max(detection.created_time.seconds) - max(detection.latency_metrics.newest_event_time.seconds)) / 60, 1)
    
    order:
      $ingestion_to_detection desc
    
    limit:
      20  
  
Rule Observability | This dashboard showcases the underlying metrics emitted by rule executions. | P50 Ingestion to Detection Latency Minutes | 
    
    
    detection.type = "RULE_DETECTION"
    detection.latency_metrics.newest_ingestion_time.seconds - detection.latency_metrics.newest_event_time.seconds < 3600
    $rule_id = detection.detection.rule_id
    $rule_name = detection.detection.rule_name
    
    //detection.detection.rule_type = "MULTI_EVENT"
    
    $did = detection.id
    $day = timestamp.get_date(detection.created_time.seconds)
    
    detection.created_time.seconds != 0
    detection.latency_metrics.newest_ingestion_time.seconds != 0
    detection.latency_metrics.newest_event_time.seconds != 0
    
    
    match:
        $day
    outcome:
        $p50_ingest_to_detection_delay = math.round(window.percentile(detection.created_time.seconds - detection.latency_metrics.newest_ingestion_time.seconds, 50) /60, 1)
    
    order:
        $p50_ingest_to_detection_delay desc  
  
Rule Observability | This dashboard showcases the underlying metrics emitted by rule executions. | Detection Latency | 
    
    
    detection.type = "RULE_DETECTION"
    //$rule_id = detection.detection.rule_id
    $rule_type = detection.detection.rule_type
    $rule_name = detection.detection.rule_name
    $rule_freq = detection.rule_run_frequency
    
    //detection.detection.rule_type = "MULTI_EVENT"
    
    detection.latency_metrics.newest_ingestion_time.seconds != 0
    detection.latency_metrics.newest_event_time.seconds != 0
    detection.created_time.seconds != 0
    
    $did = detection.id
    
    match:
        $rule_name, $rule_freq, $rule_type
    outcome:
        $detect_count = count_distinct($did)
    
        $avg_ingest_delay = math.round(window.percentile(detection.latency_metrics.newest_ingestion_time.seconds - detection.latency_metrics.newest_event_time.seconds, 50) / 60, 2)
        $p50_ingest_to_detection_delay = math.round(window.percentile(detection.created_time.seconds - detection.latency_metrics.newest_ingestion_time.seconds, 50) /60, 1)
        $p90_ingest_to_detection_delay = math.round(window.percentile(detection.created_time.seconds - detection.latency_metrics.newest_ingestion_time.seconds, 90) /60, 1)
    
        $p50_event_to_detection_delay = math.round(window.percentile(detection.created_time.seconds - detection.latency_metrics.newest_event_time.seconds, 50) / 60, 1)
        $p90_event_to_detection_delay = math.round(window.percentile(detection.created_time.seconds - detection.latency_metrics.newest_event_time.seconds, 90) /60, 1)
    
    order:
        $p50_ingest_to_detection_delay desc  
  
Rule Observability | This dashboard showcases the underlying metrics emitted by rule executions. | P90 Ingestion to Detection Latency Minutes | 
    
    
    detection.type = "RULE_DETECTION"
    $rule_id = detection.detection.rule_id
    $rule_name = detection.detection.rule_name
    
    
    $did = detection.id
    $day = timestamp.get_date(detection.created_time.seconds)
    
    detection.latency_metrics.newest_ingestion_time.seconds != 0
    detection.latency_metrics.newest_event_time.seconds != 0
    detection.created_time.seconds != 0
    
    match:
        $day
    outcome:
        $p90_ingest_to_detection_delay = math.round(window.percentile(detection.created_time.seconds - detection.latency_metrics.newest_ingestion_time.seconds, 90) /60, 1)
    
    order:
        $p90_ingest_to_detection_delay desc  
  
Rule Observability | This dashboard showcases the underlying metrics emitted by rule executions. | Detection Counts By Timing Details (primary or replay) | 
    
    
    $detection_timing_details = detection.detection_timing_details
    $detection_id = detection.id
    detection.created_time.seconds != 0
    $day = timestamp.get_date(detection.created_time.seconds)
    $detection_type = detection.type
    
    match:
        $day, $detection_timing_details
    
    outcome:
        $total_detections = count_distinct($detection_id)
    
    
    order:
        $day desc  
  
Security Management Overview | Provides key metrics on case activity and incident trends to help leaders monitor security progress. Use these insights to identify risks and drive data-driven improvements in security effectiveness. | Observed Threat Campaigns - Last 7 Days | 
    
    
    detection.detection.rule_name = /ioc/ nocase
    
    $Threat_Campaign = detection.collection_elements.references.entity.metadata.threat.campaigns
    $Threat_Campaign != ""
    
    match:
        $Threat_Campaign
    
    outcome:
        $Count = count_distinct(detection.id)
    
    order:
        $Count desc   
  
Security Management Overview | Provides key metrics on case activity and incident trends to help leaders monitor security progress. Use these insights to identify risks and drive data-driven improvements in security effectiveness. | Observed Threat Actors - Last 7 Days | 
    
    
    detection.detection.rule_name = /ioc/ nocase
    
    $Threat_Actor = detection.collection_elements.references.entity.metadata.threat.associations.name
    $Threat_Actor != ""
    
    match:
        $Threat_Actor
    
    outcome:
        $Count = count_distinct(detection.id)
    
    order:
        $Count desc
      
  
Security Management Overview | Provides key metrics on case activity and incident trends to help leaders monitor security progress. Use these insights to identify risks and drive data-driven improvements in security effectiveness. |  | 
    
    
    detection.detection.alert_state = "ALERTING"
    
    outcome:
        $total = count_distinct(detection.id)  
  
Security Management Overview | Provides key metrics on case activity and incident trends to help leaders monitor security progress. Use these insights to identify risks and drive data-driven improvements in security effectiveness. |  | 
    
    
    outcome:
        $Count = count_distinct(detection.id)   
  
Security Posture Management | Provides a real-time overview of threats, incidents, and vulnerabilities, including detections and asset monitoring. It enables security teams to assess risk posture and implement effective remediation strategies to streamline incident response. | Top 10 Threat Actors Targeting the Organization | 
    
    
    detection.detection.rule_name = /ioc/ nocase
    
    $Threat_Actor = detection.collection_elements.references.entity.metadata.threat.associations.name
    $Threat_Actor != ""
    match:
        $Threat_Actor
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
    
    limit:
        10  
  
Security Posture Management | Provides a real-time overview of threats, incidents, and vulnerabilities, including detections and asset monitoring. It enables security teams to assess risk posture and implement effective remediation strategies to streamline incident response. | UEBA Alerts | 
    
    
    detection.detection.ruleset_category_display_name = "Risk Analytics for UEBA"
    detection.detection.alert_state = "ALERTING"
    
    $Rule_Name = detection.detection.rule_name
    $Hostname = strings.coalesce(detection.collection_elements.references.event.principal.hostname, detection.collection_elements.references.event.principal.asset.hostname, detection.collection_elements.references.event.target.hostname, detection.collection_elements.references.event.target.asset.hostname)
    $User = strings.coalesce(detection.collection_elements.references.event.principal.user.user_display_name, detection.collection_elements.references.event.principal.user.email_addresses, detection.collection_elements.references.event.principal.user.userid,detection.collection_elements.references.event.target.user.user_display_name, detection.collection_elements.references.event.target.user.email_addresses, detection.collection_elements.references.event.target.user.userid)
    
    match:
      $Rule_Name, $Hostname, $User
    
    outcome:
      $Count = count(detection.id)
    
    order:
      $Count desc
    
             
  
Security Posture Management | Provides a real-time overview of threats, incidents, and vulnerabilities, including detections and asset monitoring. It enables security teams to assess risk posture and implement effective remediation strategies to streamline incident response. | Detections Over Time | 
    
    
    $Date = timestamp.get_date(detection.created_time.seconds)
    
    match:
        $Date
    
    outcome:
        $Detection_Count = count(detection.id)
    
    order:
        $Date asc  
  
Security Posture Management | Provides a real-time overview of threats, incidents, and vulnerabilities, including detections and asset monitoring. It enables security teams to assess risk posture and implement effective remediation strategies to streamline incident response. | Detections by Severity | 
    
    
    $Rule_Name = detection.detection.rule_name
    $Severity = detection.collection_elements.references.event.security_result.severity
    
    match:
        $Severity, $Rule_Name
    
    outcome:
        $Detection_Count = count(detection.id)
    
    order:
        $Severity desc  
  
Security Posture Management | Provides a real-time overview of threats, incidents, and vulnerabilities, including detections and asset monitoring. It enables security teams to assess risk posture and implement effective remediation strategies to streamline incident response. | Top 10 Detections by Name | 
    
    
    $Rule_Name = detection.detection.rule_name
    
    match:
        $Rule_Name
    
    outcome:
        $Detection_Count = count(detection.id)
    
    order:
        $Detection_Count desc
    
    limit:
        10  
  
Security Posture Management | Provides a real-time overview of threats, incidents, and vulnerabilities, including detections and asset monitoring. It enables security teams to assess risk posture and implement effective remediation strategies to streamline incident response. | Top 10 Cloud Alerts | 
    
    
    detection.detection.ruleset_category_display_name = "Cloud Threats"
    detection.detection.alert_state = "ALERTING"
    
    $Rule_Name = detection.detection.rule_name
    $Targeted_Resources = strings.coalesce(detection.collection_elements.references.event.target.application, detection.collection_elements.references.event.target.resource.name)
    $User = strings.coalesce(detection.collection_elements.references.event.principal.user.user_display_name, detection.collection_elements.references.event.principal.user.email_addresses, detection.collection_elements.references.event.principal.user.userid,detection.collection_elements.references.event.target.user.user_display_name, detection.collection_elements.references.event.target.user.email_addresses, detection.collection_elements.references.event.target.user.userid)
    
    match:
      $Rule_Name, $Targeted_Resources, $User
    
    outcome:
      $Count = count(detection.id)
    
    order:
      $Count desc
    
    limit:
          10                              
  
Security Posture Management | Provides a real-time overview of threats, incidents, and vulnerabilities, including detections and asset monitoring. It enables security teams to assess risk posture and implement effective remediation strategies to streamline incident response. | Top 10 Campaigns Targeting the Organization | 
    
    
    detection.detection.rule_name = /ioc/ nocase
    
    $Threat_Campaign = detection.collection_elements.references.entity.metadata.threat.campaigns
    $Threat_Campaign != ""
    match:
        $Threat_Campaign
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
    
    limit:
        10  
  
Security Posture Management | Provides a real-time overview of threats, incidents, and vulnerabilities, including detections and asset monitoring. It enables security teams to assess risk posture and implement effective remediation strategies to streamline incident response. | Top 10 Hosts by Detections | 
    
    
    $Rule_Name = detection.detection.rule_name
    $Hostname = strings.coalesce(detection.collection_elements.references.event.principal.hostname, detection.collection_elements.references.event.principal.asset.hostname, detection.collection_elements.references.event.target.hostname, detection.collection_elements.references.event.target.asset.hostname)
    $Hostname != ""
    match:
        $Hostname
    
    outcome:
        $Detection_Count = count_distinct(detection.id)
    
    order:
        $Detection_Count desc
    
    limit:
        10  
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | Threat Campaigns by Detections | 
    
    
    detection.detection.rule_name = /ioc/ nocase
    detection.collection_elements.references.entity.metadata.threat.campaigns !=""
    
    $Rule_Name = detection.detection.rule_name
    $Campaigns = detection.collection_elements.references.entity.metadata.threat.campaigns
    $Campaigns != ""
    match:
        $Campaigns, $Rule_Name
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc  
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | Detections Over Time by Threat Actor | 
    
    
    detection.detection.rule_name = /ioc/
    detection.collection_elements.references.entity.metadata.threat.associations.type = "THREAT_ACTOR"
    
    $Date = timestamp.get_date(detection.collection_elements.references.entity.metadata.event_metadata.event_timestamp.seconds)
    $Threat_Actor = detection.collection_elements.references.entity.metadata.threat.associations.name
    $Threat_Actor != ""
    match:
        $Date, $Threat_Actor
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count asc  
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | Detections Over Time by IOCs Type | 
    
    
    detection.detection.rule_name = /ioc/ nocase
    
    $Date = timestamp.get_date(detection.collection_elements.references.entity.metadata.event_metadata.event_timestamp.seconds)
    $IOC_Type = detection.collection_elements.references.entity.metadata.entity_type
    
    match:
        $Date , $IOC_Type
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc
      
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | Threat Actors by Detections | 
    
    
    detection.detection.rule_name = /ioc/ nocase
    detection.collection_elements.references.entity.metadata.threat.associations.type = "THREAT_ACTOR"
    
    $Rule_Name = detection.detection.rule_name
    $Threat_Actor = detection.collection_elements.references.entity.metadata.threat.associations.name
    $Threat_Actor != ""
    match:
        $Threat_Actor, $Rule_Name
    
    outcome:
        $Count = count(detection.id)
    
    order:
        $Count desc  
  
User Lifecycle Audit | Provides a detailed view of user account management activities. It helps ensure provisioning and de-provisioning policies are followed across the user lifecycle.   
Note: Apply filters to refine the results. | Recently Dormant Accounts | 
    
    
    detection.collection_elements.references.event.metadata.event_type = "USER_LOGIN"
    
    $User = strings.coalesce(detection.collection_elements.references.event.target.user.email_addresses, detection.collection_elements.references.event.target.user.userid, detection.collection_elements.references.event.target.user.windows_sid)
    $User != ""
    
    match:
        $User
    
    outcome:
        $Last_Login_Time = max(detection.collection_elements.references.event.metadata.event_timestamp.seconds)
        $Last_Login_Timestamp = timestamp.get_timestamp($Last_Login_Time, "%F %T ")
        $Days_Since_Login = math.round((timestamp.current_seconds() - $Last_Login_Time )/ 86400)
        $Status = if($Last_Login_Time != 0 AND ($Days_Since_Login >= 180), "Dormant Account (≥180 Days)", if($Last_Login_Time != 0 AND ($Days_Since_Login >= 90), "Dormant Account (≥90 Days)", "Recently Dormant Account"))
    
    order:
        $Days_Since_Login desc
    
    unselect:
        $Last_Login_Time  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
