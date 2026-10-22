---
url: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-entities/
title: Query entities \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:09.299456+00:00
---

# Query entities  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-entities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query entities

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document is for Security Operations Center (SOC) managers and analysts who want to monitor threat landscapes and system health using curated dashboards— predefined dashboards designed for visibility across various security use cases.

You can use these queries in the query editor or as a baseline for custom widgets. For information on how to create and manage dashboards, see [Manage dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards).

PCI - Alert OverviewRansomware Spotlight MonitoringThreat Intelligence OverviewHIPAA DashboardTop PCI Assets by RiskRecent Ransomware Intel Sources EventsIOCs with High Risk ScoreTop Assets by Risk Dashboard name  |  Description  |  Chart name  |  Query example   
---|---|---|---  
PCI - Alert Overview | Provides a consolidated view of alerts and insights regarding security breaches and events affecting PCI standards. **Required** : The `PCI_Assets` (Payment Card Industry Assets) reference list must be created to scope data; otherwise, charts don't load. | Top PCI Assets by Risk | 
    
    
    graph.metadata.entity_type = "ASSET"
    graph.entity.hostname in %PCI_Assets
    $Hostname = graph.entity.hostname
    $Risk_Score = graph.risk_score.risk_score
    
    match:
      $Hostname, $Risk_Score
    
    order:
      $Risk_Score desc
      
  
Ransomware Spotlight Monitoring | Provides a comprehensive view of ransomware-related detections across all security tools. Highlights recent events, affected devices, and detection sources to accelerate incident response. | Recent Ransomware Intel Sources Events | 
    
    
    graph.metadata.threat[0].description = /ransom/ nocase
    strings.coalesce(if(graph.entity.ip != "", graph.entity.ip, ""), if(graph.entity.url != "", graph.entity.url, ""), if($Hash != "", $Hash, "")) != ""
    
    $IOC_Type = graph.metadata.entity_type
    $Threat = graph.metadata.threat[0].description
    $Hash = group(graph.entity.file.sha256,graph.entity.file.md5)
    $IOC_Value = strings.coalesce(if(graph.entity.ip != "", graph.entity.ip, ""), if(graph.entity.url != "", graph.entity.url, ""), if($Hash != "", $Hash, ""))
    $Date = timestamp.get_date(graph.metadata.collected_timestamp.seconds)
    
    match:
      $Date, $Threat, $IOC_Value, $IOC_Type
    
    outcome:
      $Count = count(graph.metadata.event_metadata.id)
    
    order:
      $Count desc
      
  
Threat Intelligence Overview | Provides real-time and historical tracking of top threats, IOCs, and targeted systems. Monitors risk scores, severity, and indicator metrics to detect emerging infrastructure threats. | IOCs with High Risk Score | 
    
    
    $IOC_Type = graph.metadata.entity_type
    $Risk_Score = graph.metadata.threat.risk_score
    $Date = timestamp.get_date(graph.metadata.collected_timestamp.seconds)
    $Hash = group(graph.entity.file.sha256,graph.entity.file.md5)
    $IOC_Value = strings.coalesce(if(graph.entity.ip != "", graph.entity.ip, ""), if(graph.entity.url != "", graph.entity.url, ""), if($Hash != "", $Hash, ""))
    $IOC_Value !=""
    
    match:
      $Date, $IOC_Type, $IOC_Value
    
    outcome:
      $Total_Risk_Score =  math.round(avg($Risk_Score), 2)
      $Count = count(graph.metadata.event_metadata.id)
    
    
    order:
      $Total_Risk_Score desc  
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity. | Top Assets by Risk | 
    
    
    graph.metadata.entity_type = "ASSET"
    graph.entity.hostname in %ePHI_assets.Hostname
    
    $Hostname = graph.entity.hostname
    $Risk_Score = graph.risk_score.risk_score
    
    match:
      $Hostname, $Risk_Score
    
    order:
      $Risk_Score desc  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
