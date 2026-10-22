---
url: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-ioc-matches/
title: View IOC matches \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:52.680016+00:00
---

# View IOC matches  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-ioc-matches/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View IOC matches

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document is for Security Operations Center (SOC) managers and analysts who want to monitor threat landscapes and system health using curated dashboards— predefined dashboards designed for visibility across various security use cases. This document provides a collection of curated dashboards and their underlying queries for the **SOAR cases** source type.

You can use these queries in the query editor or as a baseline for custom widgets. For information on how to create and manage dashboards, see [Manage dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards).

CIS Controls Compliance OverviewMainNetwork Traffic OverviewThreat Intelligence OverviewTop 10 Asset communicating with IOCsGlobal Threat Map - IOC IP MatchesIOCs by SeverityIOCs by CategorySuspicious IP AccessesTop 10 Domain IndicatorsNew IOCs Ingestion by typeHosts Communicating with IOCsTop 10 IP IndicatorsIOCs Count Over TimeLatest IOCsIOCs Geolocation Overview Dashboard name  |  Description  |  Chart name  |  Query example   
---|---|---|---  
CIS Controls Compliance Overview | Monitors adherence to CIS Critical Security Controls, including asset accuracy, vulnerability remediation, and access enforcement. | Top 10 Asset communicating with IOCs | 
    
    
    $IOC_Value = ioc.ioc_value
    $IOC_Type = ioc.ioc_type
    $Asset = strings.coalesce(ioc.asset.hostname,ioc.asset.asset_ip_address, ioc.asset.mac)
    $Asset !=""
    
    match:
      $Asset, $IOC_Value, $IOC_Type
    
    outcome:
      $IOC_Severity = array_distinct(ioc.severity)
      $IOC_Category = array_distinct(ioc.category)
      $IOC_Feed =array_distinct(ioc.feed_name)
      $IOC_Count = count(ioc.ioc_value)
    
    order:
      $IOC_Count desc
    
    limit:
        10  
  
Main | Provides a summary of data ingestion health and detected IoCs, and provides a global perspective on potential threats.  | Global Threat Map - IOC IP Matches | 
    
    
    ioc.ioc_value != ""
    ioc.ioc_type = "IOC_TYPE_IP"
    $ioc_value = ioc.ioc_value
    $latitude = ioc.location.region_coordinates.latitude
    $longitude = ioc.location.region_coordinates.longitude
    
    match:
      $ioc_value, $latitude, $longitude
    
    outcome:
      $count = count_distinct(ioc.ioc_value)
    
    order:
      $count desc
      
  
Main | Provides a summary of data ingestion health and detected IoCs, and provides a global perspective on potential threats. | Global Threat Map - IOC IP Matches | 
    
    
    ioc.ioc_value != ""
    ioc.ioc_type = "IOC_TYPE_IP"
    
    $ioc_value = ioc.ioc_value
    
    $location = strings.concat(ioc.location.region_coordinates.latitude, "," ioc.location.region_coordinates.longitude)
    
    match:
      $ioc_value, $location
    
    outcome:
      $count = count_distinct(ioc.ioc_value)
    
    order:
      $count desc
      
  
Network Traffic Overview | Network Traffic Dashboard offers real-time Real-time monitoring of cloud and on-prem traffic by IP, protocol, and region. | Top 10 Asset communicating with IOCs | 
    
    
    strings.coalesce(ioc.asset.hostname,ioc.asset.asset_ip_address, ioc.asset.mac ) != ""
    
    $IOC_Value = ioc.ioc_value
    $IOC_Type = ioc.ioc_type
    $Asset = strings.coalesce(ioc.asset.hostname,ioc.asset.asset_ip_address, ioc.asset.mac)
    
    match:
      $Asset, $IOC_Value, $IOC_Type
    
    outcome:
      $IOC_Severity = array_distinct(ioc.severity)
      $IOC_Category = array_distinct(ioc.category)
      $IOC_Count = count(ioc.ioc_value)
    
    order:
      $IOC_Count desc
    
    limit:
        10  
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | IOCs by Severity | 
    
    
    $Severity = strings.to_upper(ioc.severity)
    $Severity != ""
    match:
      $Severity
    
    outcome:
      $IOC_Count = count(ioc.ioc_value)   
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | IOCs by Category | 
    
    
    $Category = ioc.category
    $Category != ""
    match:
      $Category
    
    outcome:
      $IOC_Count = count(ioc.ioc_value)   
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | Suspicious IP Accesses | 
    
    
    ioc.ioc_type =  "IOC_TYPE_IP"
    strings.coalesce( ioc.asset.hostname,ioc.asset.asset_ip_address, ioc.asset.mac ) != ""
    ioc.severity !=""
    
    $IOC_Value = ioc.ioc_value
    $IOC_Type = ioc.ioc_type
    $User = strings.coalesce( ioc.asset.hostname,ioc.asset.asset_ip_address, ioc.asset.mac )
    
    match:
      $IOC_Value, $User
    
    outcome:
      $IOC_Severity = array_distinct(ioc.severity)
      $IOC_Category = array_distinct(ioc.category)
      $IOC_Count = count(ioc.ioc_value)
    
    order:
      $IOC_Count desc
      
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | Top 10 Domain Indicators | 
    
    
    ioc.ioc_type = "IOC_TYPE_DOMAIN"
    
    $IOC_Value = ioc.ioc_value
    
    match:
      $IOC_Value
    
    outcome:
      $IOC_Count = count(ioc.ioc_value)
    
    order:
      $IOC_Count desc
    
    limit:
        10  
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | New IOCs Ingestion by type | 
    
    
    $IOC_Type = ioc.ioc_type
    $Date =  timestamp.get_date(ioc.commit_timestamp.seconds)
    
    match:
      $IOC_Type
    
    outcome:
      $IOC_Count = count(ioc.ioc_value)
    
    order:
      $IOC_Count desc  
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | Hosts Communicating with IOCs | 
    
    
    $Hostname = ioc.asset.hostname
    $Hostname != ""
    
    match:
      $Hostname
    
    outcome:
      $IOC_Count = count(ioc.ioc_value)
    
    order:
      $IOC_Count desc   
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | Top 10 IP Indicators | 
    
    
    ioc.ioc_type = "IOC_TYPE_IP"
    
    $IOC_Value = ioc.ioc_value
    
    match:
      $IOC_Value
    
    outcome:
      $IOC_Count = count(ioc.ioc_value)
    
    order:
      $IOC_Count desc
    
    limit:
        10  
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | IOCs Count Over Time | 
    
    
    $IOC_Type = ioc.ioc_type
    $Date = timestamp.get_date(ioc.day_bucket_seconds)
    
    match:
      $Date, $IOC_Type
    
    outcome:
      $IOC_Count = count(ioc.ioc_value)
    
    order:
      $Date asc  
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | Latest IOCs | 
    
    
    $IOC_Value = ioc.ioc_value
    $IOC_Type = ioc.ioc_type
    $Date = timestamp.get_date(ioc.commit_timestamp.seconds)
    
    match:
      $Date, $IOC_Value, $IOC_Type
    
    outcome:
      $IOC_Count = count(ioc.ioc_value)
      $IOC_Feed =array_distinct(ioc.feed_name)
    
    order:
      $Date desc   
  
Threat Intelligence Overview | Provides real-time insights into IOCs and risk scores, enabling faster detection of emerging infrastructure threats. | IOCs Geolocation Overview | 
    
    
    $IOC_Country= ioc.location.country_or_region
    
    match:
      $IOC_Country
    
    outcome:
      $IOC_Count = count(ioc.ioc_value)
      $Latitude = max(ioc.location.region_coordinates.latitude)
      $Longitude = max(ioc.location.region_coordinates.longitude)
    
    order:
      $IOC_Count desc  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
