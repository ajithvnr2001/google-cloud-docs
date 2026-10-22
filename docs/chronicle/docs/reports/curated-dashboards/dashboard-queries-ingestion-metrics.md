---
url: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-ingestion-metrics/
title: Query ingestion metrics \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:04.296171+00:00
---

# Query ingestion metrics  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-ingestion-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query ingestion metrics

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document is for Security Operations Center (SOC) managers and analysts who want to monitor threat landscapes and system health using curated dashboards— predefined dashboards designed for visibility across various security use cases.

You can use these queries in the query editor or as a baseline for custom widgets. For information on how to create and manage dashboards, see [Manage dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards).

ISO 27001 – Technological ControlsCIS Controls Compliance OverviewData Ingestion and HealthFEDRAMP Continuous MonitoringHIPAA DashboardMainMandiant HuntingNIST 800-53 - Audit and AccountabilityPCI - Monitoring and TestingSecOps Audit & Activity MonitoringSecOps Log MonitoringSecurity Management OverviewUser Sign In Overview

Last Heartbeat Time by Log TypeIngestion Throughput Over TimeIngested Events by Log TypeEvent Count (Last 7 Days)Ingestion - Throughput WeeklyIngestion - Events by StatusRecently Ingested LogsBurst Rejection GraphIngestion - Throughput (Last 6 Months)Ingested Events CountEvent Size (Last 3 Months)Burst Limit Graph - Quota LimitEvent Count (Last 3 Months)Log Type Distribution by ThroughputEvent Count (Last 24 Hours)Event Size (Last 7 Days)Ingestion - Throughput (All-Time)Ingestion - Throughput HourlyIngestion Error CountLog Type Distribution by Events CountBurst Limit Graph - Ingestion RateDaily Log InformationIngestion - Events by Log TypeEvent Size (Last 24 Hours)ThroughputIngested EventsEvents Over TimeTotal Events IngestedLog Ingestion LatencyParsing Rate by Log TypeLog Ingestion Volume by Log TypeSIEM Log Source HeartbeatIngestion Health StatusIngestion Throughput (GB) by Log TypeMonthly Year-To-Date Log IngestionIngestion Throughput (GB)Ingested Logs by Log TypeTop 10 Ingested Logs by Log TypeParsing Success Rate by Log TypeYear-to-Date Daily Log IngestionYear-To-Date Log IngestionForwarder Container UsageActive Log Source TrendRecent Pipeline Latency CountRecent Component StatusTotal Year-To-Date Log IngestionIngested Logs by Event TypeIngested Logs by ComponentIngestion by Log Source (24 Hours)

Dashboard name  |  Description  |  Chart name  |  Query example   
---|---|---|---  
ISO 27001 – Technological Controls  |  Provides visibility into technological controls and encryption standards to support compliance and data-driven remediation.   
Note: Filters are required to refine the data.  |  Last Heartbeat Time by Log Type  | 
    
    
    $Log_Type = ingestion.log_type
    $Component = ingestion.component
    
    match:
      $Log_Type, $Component
    
    outcome:
      $Date = timestamp.get_timestamp(max(ingestion.last_heartbeat_time))
    
    order:
      $Date desc  
  
CIS Controls Compliance Overview  |  Provides visibility into CIS critical security controls to strengthen governance. It tracks key metrics like asset accuracy, vulnerability progress, and backup reliability to ensure operational preparedness.  |  Ingestion Throughput Over Time  | 
    
    
    $Date = timestamp.get_date(ingestion.end_time)
    
    match:
      $Date
    
    outcome:
      $Total_Size_Bytes = sum(if(ingestion.component = "Ingestion API", ingestion.log_volume, 0))  
  
CIS Controls Compliance Overview  |  Provides visibility into CIS critical security controls to strengthen governance. It tracks key metrics like asset accuracy, vulnerability progress, and backup reliability to ensure operational preparedness.  |  Ingested Events by Log Type  | 
    
    
    $Log_Type = ingestion.log_type
    
    match:
      $Log_Type
    
    outcome:
      $Total_Size_Bytes = sum(if(ingestion.component = "Ingestion API", ingestion.log_volume, 0))
      $Total_Logs = sum(if(ingestion.component = "Ingestion API", ingestion.log_count, 0))
      $Total_Normalized_Events = sum(if(ingestion.component = "Normalizer" AND ingestion.state = "validated", ingestion.event_count, 0))
      $Total_Parsing_Error_Events = sum(if(ingestion.component = "Normalizer" AND ingestion.state = "failed_parsing", ingestion.log_count, 0))
      $Total_Validation_Error_Events = sum(if(ingestion.component = "Normalizer" AND ingestion.state = "failed_validation", ingestion.event_count, 0))
      $Total_Indexing_Error_Events = sum(if(ingestion.component = "Normalizer" AND ingestion.state = "failed_indexing", ingestion.log_count, 0))
    
    order:
      $Total_Size_Bytes desc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Count (Last 7 Days)  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Days = timestamp.get_timestamp($event.ingestion.end_time, "%Y-%m-%d")
    
    match:
      $Days
    outcome:
      $Count = sum($event.ingestion.log_count)
    order:
      $Days asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Throughput Weekly  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Timestamp_Week = timestamp.get_timestamp($event.ingestion.end_time, "Week %W")
    
    match:
      $Log_Type, $Timestamp_Week
    outcome:
      $Count = sum($event.ingestion.log_volume)
    order:
      $Timestamp_Week asc  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Events by Status  | 
    
    
    $Date = timestamp.get_date($event.ingestion.end_time)
    
    match:
      $Date
    outcome:
      $Total_Logs = sum(if($event.ingestion.component = "Ingestion API", $event.ingestion.log_count, 0))
      $Total_Normalized_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "validated", $event.ingestion.event_count, 0))
      $Total_Parsing_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_parsing", $event.ingestion.log_count, 0))
      $Total_Validation_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_validation", $event.ingestion.event_count, 0))
      $Total_Indexing_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_indexing", $event.ingestion.log_count, 0))
    order:
      $Date desc
    limit:
        50  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Throughput Weekly  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Timestamp_Week = timestamp.get_timestamp($event.ingestion.end_time, "Week %W")
    $Log_Type != ""
    match:
      $Log_Type, $Timestamp_Week
    outcome:
      $Count = sum($event.ingestion.log_volume)
    order:
      $Timestamp_Week asc  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Count (Last 7 Days)  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Days = timestamp.get_timestamp($event.ingestion.end_time, "%d-%h")
    
    match:
      $Days
    outcome:
      $Count = sum($event.ingestion.log_count)
    order:
      $Days asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Recently Ingested Logs  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Log_Type != ""
    
    match:
      $Log_Type
    outcome:
      $Time = timestamp.get_timestamp(max($event.ingestion.end_time))
    order:
      $Time desc
    limit:
        50  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Burst Rejection Graph  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Timestamp_Hour = timestamp.get_timestamp($event.ingestion.end_time, "%d-%h %k:00 %p")
    
    match:
      $Timestamp_Hour
    outcome:
      $Max_Of_Quota_Rejected_Log_Volume = strings.concat(sum($event.ingestion.quota_rejected_short_term_log_volume), " GB")
    order:
      $Timestamp_Hour asc  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Recently Ingested Logs  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Log_Type != ""
    
    match:
      $Log_Type
    outcome:
      $Time = timestamp.get_timestamp(max($event.ingestion.end_time))
    order:
      $Time desc
    limit:
        50  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Throughput (Last 6 Months)  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Timestamp_Month = timestamp.get_timestamp($event.ingestion.end_time, "%m %h")
    
    match:
      $Log_Type, $Timestamp_Month
    outcome:
      $Count = sum($event.ingestion.log_volume)
    order:
      $Timestamp_Month asc  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingested Events Count  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    outcome:
      $Count = sum($event.ingestion.log_count)
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Size (Last 3 Months)  | 
    
    
    ingestion.component = "Ingestion API"
    
    $Date = timestamp.get_timestamp(ingestion.end_time, "%m-%h")
    
    match:
      $Date
    outcome:
      $Event_Size = math.round(sum(ingestion.log_volume) / 1073741824, 2)
    order:
      $Date asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Burst Limit Graph - Quota Limit  | 
    
    
    $event.ingestion.component = "Ingestion API"
    $Timestamp_Hour = timestamp.get_timestamp($event.ingestion.end_time, "%Y-%m-%d %H")
    
    match:
      $Timestamp_Hour
    outcome:
      $Max_Quota_Limit_MB_Per_Second = math.round(max($event.ingestion.quota_limit_per_second) / 1000000, 2)
    order:
      $Timestamp_Hour asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Count (Last 3 Months)  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Months = timestamp.get_timestamp($event.ingestion.end_time, "%Y-%m")
    
    match:
      $Months
    outcome:
      $Count = sum($event.ingestion.log_count)
    order:
      $Months asc
    
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Log Type Distribution by Throughput  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Log_Type = $event.ingestion.log_type
    $Log_Type != ""
    match:
      $Log_Type
    outcome:
      $Count = sum($event.ingestion.log_volume)
    order:
      $Count desc
    limit:
        50  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Burst Limit Graph - Quota Limit  | 
    
    
    $event.ingestion.component = "Ingestion API"
    $Timestamp_Hour = timestamp.get_timestamp($event.ingestion.end_time, "%d/%h %l%p")
    
    match:
      $Timestamp_Hour
    outcome:
      $Max_Quota_Limit_MB_Per_Second = math.round(max($event.ingestion.quota_limit_per_second) / 1000000, 2)
    order:
      $Timestamp_Hour asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Count (Last 24 Hours)  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Hours = timestamp.get_timestamp($event.ingestion.end_time, "%Y-%m-%d %H")
    
    match:
      $Hours
    outcome:
      $Count = sum($event.ingestion.log_count)
    order:
      $Hours asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Log Type Distribution by Throughput  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Log_Type = $event.ingestion.log_type
    
    match:
      $Log_Type
    outcome:
      $Count = sum($event.ingestion.log_volume)
    order:
      $Count desc
    limit:
        50  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Size (Last 7 Days)  | 
    
    
    ingestion.component = "Ingestion API"
    
    $Days = timestamp.get_timestamp(ingestion.end_time, "%Y-%m-%d")
    
    match:
      $Days
    outcome:
      $Event_Size = math.round(sum(ingestion.log_volume) / 1073741824, 2)
    order:
      $Days asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Count (Last 3 Months)  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Months = timestamp.get_timestamp($event.ingestion.end_time, "%m-%h")
    
    match:
      $Months
    outcome:
      $Count = sum($event.ingestion.log_count)
    order:
      $Months asc
    
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingested Events Count  | 
    
    
    ingestion.component = "Ingestion API"
    
    outcome:
      $Count = math.round(sum(ingestion.log_count)/(1000*1000), 2)
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Throughput (All-Time)  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Timestamp_Year = timestamp.get_timestamp($event.ingestion.end_time, "%Y")
    
    match:
      $Log_Type, $Timestamp_Year
    outcome:
      $Count = sum($event.ingestion.log_volume)
    order:
      $Timestamp_Year asc  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Burst Rejection Graph  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Timestamp_Hour = timestamp.get_timestamp($event.ingestion.end_time, "%Y-%m-%d %H")
    
    match:
      $Timestamp_Hour
    outcome:
      $Max_Of_Quota_Rejected_Log_Volume = math.round(sum($event.ingestion.quota_rejected_short_term_log_volume) / 1073741824, 2)
    order:
      $Timestamp_Hour asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Size (Last 7 Days)  | 
    
    
    ingestion.component = "Ingestion API"
    
    $Days = timestamp.get_timestamp(ingestion.end_time, "%d-%h")
    
    match:
      $Days
    outcome:
      $Event_Size = math.round(sum(ingestion.log_volume) / 1073741824, 2)
    order:
      $Days asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Throughput Hourly  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Timestamp_Hour = timestamp.get_timestamp($event.ingestion.end_time, "%k:00 %p")
    
    match:
      $Log_Type, $Timestamp_Hour
    outcome:
      $Count = sum($event.ingestion.log_volume)
    order:
      $Timestamp_Hour asc  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Throughput (Last 6 Months)  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Timestamp_Month = timestamp.get_timestamp($event.ingestion.end_time, "%Y-%m")
    $Log_Type != ""
    match:
      $Log_Type, $Timestamp_Month
    outcome:
      $Count = sum($event.ingestion.log_volume)
    order:
      $Timestamp_Month asc  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion Error Count  | 
    
    
    outcome:
      $Count = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_validation", $event.ingestion.event_count, 0)+if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_parsing", $event.ingestion.log_count, 0))
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Events by Status  | 
    
    
    $Date = timestamp.get_date($event.ingestion.end_time)
    
    match:
      $Date
    outcome:
      $Total_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "validated", $event.ingestion.event_count, 0))
      $Total_Normalized_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "validated", $event.ingestion.event_count, 0))
      $Total_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_validation", $event.ingestion.event_count, 0)+if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_parsing", $event.ingestion.log_count, 0))
      $Total_Parsing_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_parsing", $event.ingestion.log_count, 0))
      $Total_Validation_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_validation", $event.ingestion.event_count, 0))
    order:
      $Date desc
    limit:
        50  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Log Type Distribution by Events Count  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Log_Type = $event.ingestion.log_type
    $Log_Type != ""
    match:
      $Log_Type
    outcome:
      $Count = sum($event.ingestion.log_count)
    order:
      $Count desc
    limit:
        50  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion Error Count  | 
    
    
    outcome:
      $Count = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_validation", $event.ingestion.event_count, 0)+if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_parsing", $event.ingestion.log_count, 0))
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Burst Limit Graph - Ingestion Rate  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Timestamp_Hour = timestamp.get_timestamp($event.ingestion.end_time, "%Y-%m-%d %H")
    
    match:
      $Timestamp_Hour
    outcome:
      $Total_Log_Volume_MB_Per_Hour = math.round(sum($event.ingestion.log_volume)/ 3600000000, 2)
    order:
      $Timestamp_Hour asc  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Throughput (All-Time)  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Timestamp_Year = timestamp.get_timestamp($event.ingestion.end_time, "%Y")
    $Log_Type != ""
    match:
      $Log_Type, $Timestamp_Year
    outcome:
      $Count = sum($event.ingestion.log_volume)
    order:
      $Timestamp_Year asc  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Log Type Distribution by Events Count  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Log_Type = $event.ingestion.log_type
    
    match:
      $Log_Type
    outcome:
      $Count = sum($event.ingestion.log_count)
    order:
      $Count desc
    limit:
        50  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Burst Limit Graph - Ingestion Rate  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Timestamp_Hour = timestamp.get_timestamp($event.ingestion.end_time, "%d/%h %l%p")
    
    match:
      $Timestamp_Hour
    outcome:
      $Total_Log_Volume_MB_Per_Hour = math.round(sum($event.ingestion.log_volume)/ 3600000000, 2)
    order:
      $Timestamp_Hour asc  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Daily Log Information  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Log_Type != ""
    
    match:
      $Log_Type by day
    outcome:
      $Count = sum($event.ingestion.event_count)
    order:
      $Count desc
    limit:
        50  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Events by Log Type  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Log_Type != ""
    match:
      $Log_Type
    outcome:
      $Total_Size_Bytes = sum(if($event.ingestion.component = "Ingestion API", $event.ingestion.log_volume, 0))
      $Total_Logs = sum(if($event.ingestion.component = "Ingestion API", $event.ingestion.log_count, 0))
      $Total_Normalized_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "validated", $event.ingestion.event_count, 0))
      $Total_Parsing_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_parsing", $event.ingestion.log_count, 0))
      $Total_Validation_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_validation", $event.ingestion.event_count, 0))
      $Total_Indexing_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_indexing", $event.ingestion.log_count, 0))
    order:
      $Total_Size_Bytes desc
    limit:
        50
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Size (Last 3 Months)  | 
    
    
    ingestion.component = "Ingestion API"
    
    $Date = timestamp.get_timestamp(ingestion.end_time, "%Y-%m")
    
    match:
      $Date
    outcome:
      $Event_Size = math.round(sum(ingestion.log_volume) / 1073741824, 2)
    order:
      $Date asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Size (Last 24 Hours)  | 
    
    
    ingestion.component = "Ingestion API"
    
    $Hours = timestamp.get_timestamp(ingestion.end_time, "%k:00 %p")
    
    match:
      $Hours
    outcome:
      $Event_Size = math.round(sum(ingestion.log_volume) / 1073741824, 2)
    order:
      $Hours asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Size (Last 24 Hours)  | 
    
    
    ingestion.component = "Ingestion API"
    
    $Hours = timestamp.get_timestamp(ingestion.end_time, "%Y-%m-%d %H")
    
    match:
      $Hours
    outcome:
      $Event_Size = math.round(sum(ingestion.log_volume) / 1073741824, 2)
    order:
      $Hours asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Event Count (Last 24 Hours)  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    $Hours = timestamp.get_timestamp($event.ingestion.end_time, "%k:00 %p")
    
    match:
      $Hours
    outcome:
      $Count = sum($event.ingestion.log_count)
    order:
      $Hours asc
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Throughput  | 
    
    
    ingestion.component = "Ingestion API"
    outcome:
      $throughput = math.round(sum(ingestion.log_volume) / (1000 * 1000 * 1000), 2)
      
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Throughput Hourly  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Timestamp_Hour = timestamp.get_timestamp($event.ingestion.end_time, "%Y-%m-%d %H")
    $Log_Type != ""
    match:
      $Log_Type, $Timestamp_Hour
    outcome:
      $Count = sum($event.ingestion.log_volume)
    order:
      $Timestamp_Hour asc  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Daily Log Information  | 
    
    
    $Log_Type = $event.ingestion.log_type
    $Log_Type != ""
    
    match:
      $Log_Type by day
    outcome:
      $Count = sum($event.ingestion.event_count)
    order:
      $Count desc
    limit:
        50  
  
Data Ingestion and Health  |  Monitors data flow, error counts, and log distributions. Tracks ingestion throughput and activity over time to identify trends and streamline troubleshooting.  |  Ingestion - Events by Log Type  | 
    
    
    $Log_Type = $event.ingestion.log_type
    
    match:
      $Log_Type
    outcome:
      $Total_Size_Bytes = sum(if($event.ingestion.component = "Ingestion API", $event.ingestion.log_volume, 0))
      $Total_Logs = sum(if($event.ingestion.component = "Ingestion API", $event.ingestion.log_count, 0))
      $Total_Normalized_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "validated", $event.ingestion.event_count, 0))
      $Total_Parsing_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_parsing", $event.ingestion.log_count, 0))
      $Total_Validation_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_validation", $event.ingestion.event_count, 0))
      $Total_Indexing_Error_Events = sum(if($event.ingestion.component = "Normalizer" AND $event.ingestion.state = "failed_indexing", $event.ingestion.log_count, 0))
    order:
      $Total_Size_Bytes desc
    limit:
        50   
  
FEDRAMP Continuous Monitoring  |  Provides Security and Compliance Teams a real-time view of system posture. Tracks vulnerabilities and control effectiveness against FedRAMP standards to prioritize remediation and maintain continuous compliance.  |  Last Heartbeat Time by Log Type  | 
    
    
    $Log_Type = ingestion.log_type
    $Component = ingestion.component
    
    match:
      $Log_Type, $Component
    
    outcome:
      $Date = timestamp.get_timestamp(max(ingestion.last_heartbeat_time), "%F %T")
    
    order:
      $Date desc  
  
HIPAA Dashboard  |  Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate.  |  Last Heartbeat Time by Log Type  | 
    
    
    $Log_Type = ingestion.log_type
    $Component = ingestion.component
    
    match:
      $Log_Type, $Component
    
    outcome:
      $Date = timestamp.get_timestamp(max(ingestion.last_heartbeat_time), "%F %T")
    
    order:
      $Date desc  
  
Main  |  The Main dashboard offers a summary of data ingestion health and detected IoCs, and provides a global perspective on potential threats.  |  Ingested Events  | 
    
    
    ingestion.component = "Ingestion API"
    outcome:
      $event_count = sum(ingestion.log_count)
      
  
Main  |  The Main dashboard offers a summary of data ingestion health and detected IoCs, and provides a global perspective on potential threats.  |  Ingested Events  | 
    
    
    ingestion.component = "Ingestion API"
    ingestion.log_type != ""
    outcome:
      $event_count = math.round(sum(ingestion.log_count)/(1000*1000), 2)
      
  
Main  |  The Main dashboard offers a summary of data ingestion health and detected IoCs, and provides a global perspective on potential threats.  |  Events Over Time  | 
    
    
    $log_type = ingestion.log_type
    $log_type != ""
    ingestion.component = "Ingestion API"
    ingestion.log_type != "FORWARDER_HEARTBEAT"
    ingestion.start_time != 0
    $date = timestamp.get_date(ingestion.start_time)
    $date != ""
    
    match:
      $log_type, $date
    
    outcome:
      $log_count = sum(ingestion.log_count)
    
    order:
      $date desc
      
  
Main  |  The Main dashboard offers a summary of data ingestion health and detected IoCs, and provides a global perspective on potential threats.  |  Throughput  | 
    
    
    ingestion.component = "Ingestion API"
    outcome:
      $throughput = math.round(sum(ingestion.log_volume) / (1000 * 1000 * 1000), 2)  
  
Main  |  The Main dashboard offers a summary of data ingestion health and detected IoCs, and provides a global perspective on potential threats.  |  Throughput  | 
    
    
    ingestion.component = "Ingestion API"
    ingestion.log_type != "FORWARDER_HEARTBEAT"
    outcome:
      $throughput = math.round(sum(ingestion.log_volume) / (1000 * 1000 * 1000), 1)  
  
Main  |  The Main dashboard offers a summary of data ingestion health and detected IoCs, and provides a global perspective on potential threats.  |  Events Over Time  | 
    
    
    ingestion.log_type != ""
    ingestion.component = "Ingestion API"
    ingestion.log_type != "FORWARDER_HEARTBEAT"
    $log_type = ingestion.log_type
    ingestion.start_time != 0
    $date = timestamp.get_date(ingestion.start_time)
    $date != ""
    match:
      $log_type, $date
    outcome:
      $log_count = sum(ingestion.log_count)
    order:
      $date
      
  
Mandiant Hunting  |  Provides visibility into proactive Mandiant threat hunting. Tracks ongoing and completed activities while highlighting security trends discovered during the hunting process.  |  Total Events Ingested  | 
    
    
    $event.ingestion.component = "Ingestion API"
    
    outcome:
      $count = sum($event.ingestion.log_count)  
  
NIST 800-53 - Audit and Accountability  |  Monitors log management and audit activities aligned with NIST 800-53 standards. Lets SOC teams manage audit logs to ensure security and continuous compliance.  |  Log Ingestion Latency  | 
    
    
    $Log_Type = ingestion.log_type
    $Latency = ingestion.latency_count
    $Date = timestamp.get_date(ingestion.end_time)
    
    match:
      $Date, $Log_Type, $Latency
    
      
  
NIST 800-53 - Audit and Accountability  |  Monitors log management and audit activities aligned with NIST 800-53 standards. Empowers SOC teams to manage audit logs effectively for continuous security and compliance.  |  Parsing Rate by Log Type  | 
    
    
    $Log_Type = ingestion.log_type
    
    match:
      $Log_Type
    
    outcome:
      $Ingested_Log_Count = sum(ingestion.event_count)
      $Total_Failed_Count = sum(if(ingestion.state = "failed_parsing" or ingestion.state = "failed_indexing" or ingestion.state = "failed_validation", ingestion.event_count,0))
      $Parsed_Event_Count = math.round(($Ingested_Log_Count - $Total_Failed_Count))
      $Parsing_Success_Rate = math.round(($Parsed_Event_Count/$Ingested_Log_Count) * 100,2)
      $Parsing_Failed_Rate = math.round(($Total_Failed_Count/$Ingested_Log_Count) * 100,2)
    
    order:
      $Parsing_Success_Rate desc  
  
NIST 800-53 - Audit and Accountability  |  Monitors log management and audit activities aligned with NIST 800-53 standards. Empowers SOC teams to manage audit logs effectively for continuous security and compliance.  |  Log Ingestion Volume by Log Type  | 
    
    
    $Log_Type = ingestion.log_type
    
    match:
      $Log_Type
    
    outcome:
      $Log_Volume = math.round(sum(ingestion.log_volume) / (1000 * 1000 * 1000), 2)
    
    order:
      $Log_Volume desc  
  
NIST 800-53 - Audit and Accountability  |  Monitors log management and audit activities aligned with NIST 800-53 standards. Empowers SOC teams to manage audit logs effectively for continuous security and compliance.  |  Last Heartbeat Time by Log Type  | 
    
    
    $Log_Type = ingestion.log_type
    $Component = ingestion.component
    
    match:
      $Log_Type, $Component
    
    outcome:
      $Date = timestamp.get_timestamp(max(ingestion.last_heartbeat_time), "%F %T")
    
    order:
      $Date desc
      
  
PCI - Monitoring and Testing  |  Monitors and tracks access to cardholder data within the PCI environment. Uses the `PCI_Assets` and `Default_Users` reference lists to scope data.   
Note: Required reference lists must be created before charts populate.  |  SIEM Log Source Heartbeat  | 
    
    
    $Log_Type = ingestion.log_type
    $Component = ingestion.component
    
    match:
      $Log_Type, $Component
    
    outcome:
      $Date = timestamp.get_timestamp(max(ingestion.last_heartbeat_time), "%F %T")
    
    order:
      $Date asc  
  
SecOps Audit & Activity Monitoring  |  Monitors security posture, events, and user activities within Chronicle Google APIs. Tracks blocked actions to provide visibility into potential threats and system health.  |  Ingestion Health Status  | 
    
    
    $Date = timestamp.get_date(ingestion.start_time)
    $Collector_Type = ingestion.component
    
    match:
      $Date, $Collector_Type
    
    outcome:
      $Count = sum(ingestion.log_count)
    
    order:
      $Date desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Ingestion Throughput (GB) by Log Type  | 
    
    
    ingestion.component = "Ingestion API"
    ingestion.log_type != ""
    ingestion.log_type != "FORWARDER_HEARTBEAT"
    
    $Date = timestamp.get_date(ingestion.end_time)
    $Log_Type = ingestion.log_type
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Throughput_GB = math.round(sum(ingestion.log_volume) / (1000 * 1000 * 1000), 2)
    
    order:
      $Throughput_GB desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Monthly Year-To-Date Log Ingestion  | 
    
    
    ingestion.component = "Ingestion API"
    
    $Timestamp_Month = timestamp.get_timestamp(ingestion.end_time, "%Y-%m")
    
    match:
      $Timestamp_Month
    
    outcome:
      $Total_Log_Volume = math.round(sum(ingestion.log_volume) / (1000 * 1000 * 1000), 2)
    
    order:
      $Timestamp_Month asc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Ingestion Throughput (GB)  | 
    
    
    ingestion.component = "Ingestion API"
    ingestion.log_type != ""
    ingestion.log_type != "FORWARDER_HEARTBEAT"
    
    $Date = timestamp.get_date(ingestion.end_time)
    
    match:
      $Date
    
    outcome:
      $Throughput_GB = math.round(sum(ingestion.log_volume) / (1000 * 1000 * 1000), 2)
    
    order:
      $Date desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Log Ingestion Latency  | 
    
    
    ingestion.component = "Normalizer"
    ingestion.log_type != ""
    
    $Log_Type = ingestion.log_type
    $Latency = ingestion.latency_count
    $Date = timestamp.get_date(ingestion.end_time)
    
    match:
      $Date, $Log_Type, $Latency
    
    order:
      $Date desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Ingested Logs by Log Type  | 
    
    
    ingestion.component = "Ingestion API"
    
    $Log_Type = ingestion.log_type
    $Date = timestamp.get_date(ingestion.start_time)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = sum(ingestion.log_count)
    
    order:
      $Date desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Top 10 Ingested Logs by Log Type  | 
    
    
    ingestion.component = "Ingestion API"
    ingestion.log_type != ""
    
    $Log_Type = ingestion.log_type
    
    match:
      $Log_Type
    
    outcome:
      $Count = sum(ingestion.log_count)
    
    order:
      $Count desc
    
    limit:
        10  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Parsing Success Rate by Log Type  | 
    
    
    ingestion.log_type != ""
    
    $Log_Type = ingestion.log_type
    
    match:
      $Log_Type
    
    outcome:
      $Ingested_Log_Count = sum(if(ingestion.component = "Ingestion API" and ingestion.state = "", ingestion.log_count,0))
      $Event_Count = sum(ingestion.event_count)
      $Total_Failed_Count = sum(if(ingestion.state = "failed_parsing" or ingestion.state = "failed_indexing" or ingestion.state = "failed_validation", ingestion.log_count,0))
      $Total_Normalized_Events = sum(if(ingestion.component = "Normalizer" AND ingestion.state = "validated", ingestion.event_count, 0))
      $Parsing_Success_Rate = math.round(($Total_Normalized_Events/$Event_Count) * 100,2)
    
    order:
      $Parsing_Success_Rate desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Year-to-Date Daily Log Ingestion  | 
    
    
    ingestion.component = "Ingestion API"
    
    $Date = timestamp.get_date(ingestion.end_time)
    
    match:
      $Date
    
    outcome:
      $Total_Log_Volume = math.round(sum(ingestion.log_volume)/ (1000*1000*1000), 2)
    
    order:
      $Date desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Year-To-Date Log Ingestion  | 
    
    
    ingestion.component = "Ingestion API"
    
    $Log_Type = ingestion.log_type
    
    match:
      $Log_Type
    
    outcome:
      $Recent_Ingestion_Time = timestamp.get_timestamp(max(ingestion.end_time), "%F %T")
      $Total_Log_Volume = math.round(sum(ingestion.log_volume) / (1000 * 1000 * 1000), 2)
    
    order:
      $Recent_Ingestion_Time desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Forwarder Container Usage  | 
    
    
    ingestion.component = "Forwarder"
    ingestion.disk_used > 0
    
    $Log_Type = ingestion.log_type
    $Date = timestamp.get_date(ingestion.end_time)
    
    match:
      $Date
    
    outcome:
      $Usage_Rate = sum(ingestion.disk_used)
    
    order:
      $Date desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Active Log Source Trend  | 
    
    
    ingestion.component = "Ingestion API"
    
    $Date = timestamp.get_date(ingestion.end_time)
    
    match:
      $Date
    
    outcome:
      $Count = count_distinct(ingestion.log_type)
    
    order:
      $Date desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Recent Pipeline Latency Count  | 
    
    
    ingestion.component = "Normalizer"
    ingestion.log_type != ""
    
    $Log_Type = ingestion.log_type
    $Latency_Count = ingestion.latency_count
    $OverFlow = ingestion.latency_overflow
    $UnderFlow = ingestion.latency_underflow
    
    match:
      $Log_Type, $Latency_Count, $OverFlow, $UnderFlow
    
    outcome:
      $End_Time = timestamp.get_timestamp(max(ingestion.end_time), "%F %T")
    
    order:
      $End_Time desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Log Ingestion Volume by Log Type  | 
    
    
    ingestion.component = "Ingestion API"
    ingestion.log_type != ""
    $Log_Type = ingestion.log_type
    $Date = timestamp.get_date(ingestion.end_time)
    
    match:
      $Log_Type
    
    outcome:
      $Count = math.round(sum(ingestion.log_volume) / (1000 * 1000 * 1000), 2)
    
    order:
      $Count desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Last Heartbeat Time by Log Type  | 
    
    
    ingestion.log_type != ""
    
    $Component = ingestion.component
    $Log_Type = ingestion.log_type
    
    match:
      $Log_Type, $Component
    outcome:
    
      $Time = timestamp.get_timestamp(max(ingestion.last_heartbeat_time), "%F %T")
    order:
    
      $Time desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Recent Component Status  | 
    
    
    $Log_Type = if(ingestion.log_type = "", "UNPARSED LOGS", ingestion.log_type)
    $Component = ingestion.component
    
    match:
      $Log_Type, $Component
    
    outcome:
      $Count = sum(ingestion.log_count)
      $Start_Time = timestamp.get_timestamp(max(ingestion.start_time), "%F %T")
      $End_Time = timestamp.get_timestamp(max(ingestion.end_time), "%F %T")  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Total Year-To-Date Log Ingestion  | 
    
    
    ingestion.component = "Ingestion API"
    
    outcome:
      $Total_Log_Volume = math.round(sum(ingestion.log_volume) / (1000 * 1000 * 1000), 2)  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Ingested Logs by Event Type  | 
    
    
    $Event_Type = ingestion.event_type
    $Date = timestamp.get_date(ingestion.start_time)
    
    match:
      $Date, $Event_Type
    
    outcome:
      $Count = sum(ingestion.event_count)
    
    order:
      $Date desc  
  
SecOps Log Monitoring  |  Monitors log ingestion latency and component status to optimize performance. Helps reduce data loss and ensures high-fidelity security monitoring across the environment.  |  Ingested Logs by Component  | 
    
    
    $Collector_Type = ingestion.component
    $Date = timestamp.get_date(ingestion.start_time)
    
    match:
      $Collector_Type, $Date
    
    outcome:
      $Count = sum(ingestion.log_count)
    
    order:
      $Date desc  
  
Security Management Overview  |  Provides a centralized view of security operations by tracking case activity, incident trends, and response performance. Helps teams monitor progress and identify risks to improve overall security effectiveness. |  | 
    
    
    ingestion.component = "Ingestion API"
    
    outcome:
      $total = count_distinct(ingestion.log_type)  
  
User Sign In Overview  |  Monitors authentication activities to identify and track sign-in events. Analyzes geographical activity, associated hosts, and sign-in trends to detect risky users and unusual login behaviors for proactive threat detection.  |  Ingestion by Log Source (24 Hours)  | 
    
    
    $ingestion_metrics_log_type = ingestion.log_type
    match:
      $ingestion_metrics_log_type
    
    outcome:
      $ingestion_metrics_total_events = sum(ingestion.event_count)
      $ingestion_metrics_drop_count = sum(ingestion.drop_count)
      $ingestion_metrics_log_count = sum(ingestion.log_count)
    
    order:
      $ingestion_metrics_total_events desc
      
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
