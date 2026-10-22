---
url: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-soar-cases/
title: Query SOAR cases \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:47.151280+00:00
---

# Query SOAR cases  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-soar-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query SOAR cases

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document is for Security Operations Center (SOC) managers and analysts who want to monitor threat landscapes and system health using curated dashboards— predefined dashboards designed for visibility across various security use cases. This document provides a collection of curated dashboards and their underlying queries for the **SOAR cases** source type.

You can use these queries in the query editor or as a baseline for custom widgets. For information on how to create and manage dashboards, see [Manage dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards).

CIS Controls Compliance OverviewCase & Incident Analytics (SOAR)FEDRAMP Continuous MonitoringHIPAA DashboardISO27001 - Organizational ControlsSOC Workflow Monitoring (SOAR)Security Management Overview

Case Distribution by Priority - Open CasesTop 10 MITRE Tactics by IncidentTop 10 Incidents by Case StageCase Tags DistributionTotal EnvironmentsTotal Important CasesIncident Statuses DistributionCase Statuses DistributionHigh Priority CasesTop 10 Incidents by Case TagCase Distribution by Priority - Closed CasesRecent Incident DetailsCases Over TimeCase StatisticsIncident Closure Reasons DistributionIncident Severities DistributionIncidents Over TimeIncident Priorities DistributionTop 10 MITRE Techniques by IncidentTop 10 Case TagsList of EnvironmentsTop 10 Incidents by Root CauseTop 10 Cases ClosedLow Priority CasesCase Actions Over TimeTotal Open IncidentsCase Priorities DistributionTotal Closed IncidentsCase Closure Reason DistributionOpen Cases Distribution by PriorityTop 10 Analysts by Incident ClosuresAverage Case Closure Time by PriorityCase Closure TimeTotal Incidents Handled AutomaticallyAnalyst's PerformanceAutomatically vs Manually Handled Incidents Over TimeCase Closure SummaryTotal Incidents Handled ManuallyTop 10 Analysts by Incident ClosureTop 10 Users by CaseCase Assignments Over TimeAlert Detection SummaryOpen Cases by AgeCases Last Update more than 7 Days AgoOpen Case Tags Overview - 7 daysAnalyst Productivity (Closed Cases) - 7 daysOpen Cases by Environment - Last 7 DaysAnalyst Workloads% Automated Closure - Last 7 DaysCases Priority - Last 24 HoursMTTR by SOC Role - Last 7 DaysOpen Critical/High Cases - Last 24 HoursAnalyst Backlog (Open Cases) - 7 daysTop 10 MITRE ATT&CK Tactics - Last 7 DaysTop 10 MITRE ATT&CK Techniques - Last 7 Days

Dashboard name  |  Description  |  Chart name  |  Query   
---|---|---|---  
CIS Controls Compliance Overview  |  Provides a central view of CIS compliance metrics, such as asset accuracy and backup reliability. use these insights to strengthen security governance and track remediation progress.  |  Case Distribution by Priority - Open Cases  | 
    
    
    case.status = "OPENED"
    
    $Priority = case.priority
    
    match:
        $Priority
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Top 10 MITRE Tactics by Incident  | 
    
    
    case.incident = true
    case.alerts.metadata.tags = /TA[0-9]+/
    
    $Tactic = case.alerts.metadata.tags
    
    match:
        $Tactic
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc
    
    limit:
        10   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Top 10 Incidents by Case Stage  | 
    
    
    case.incident = true
    
    $Stage = case.stage
    
    match:
        $Stage
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc
    
    limit:
        10   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Case Tags Distribution  | 
    
    
    $Case_Tag = case.tags.name
    
    match:
        $Case_Tag
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Total Environments  | 
    
    
    outcome:
        $Count = count_distinct(case.environment)   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Total Important Cases  | 
    
    
    case.important = true
    outcome:
        $Count = count(case.name)   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Incident Statuses Distribution  | 
    
    
    case.incident = true
    
    $Status = case.status
    
    match:
        $Status
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Case Statuses Distribution  | 
    
    
    $Status = case.status
    
    match:
        $Status
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  High Priority Cases  | 
    
    
    case.priority = "PRIORITY_CRITICAL"
    or case.priority = "PRIORITY_HIGH"
    
    $Timestamp_Daily = timestamp.get_date(case.create_time.seconds)
    $Priority = case.priority
    
    match:
        $Timestamp_Daily, $Priority
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Timestamp_Daily desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Top 10 Incidents by Case Tag  | 
    
    
    case.incident = true
    
    $Case_Tag = case.tags.name
    
    match:
        $Case_Tag
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc
    
    limit:
        10   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Case Distribution by Priority - Closed Cases  | 
    
    
    case.status = "CLOSED"
    
    $Priority = case.priority
    
    match:
        $Priority
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Recent Incident Details  | 
    
    
    case.incident = true
    
    $Case_ID = case.response_platform_info.response_platform_id
    $Case_Name = case.display_name
    $Case_Creation_Time = timestamp.get_timestamp(case.create_time.seconds, "%F %T ")
    $Last_Stage = case.stage
    $Case_Status = case.status
    $Last_Handled_Analyst = strings.concat(case.last_modifying_user.given_name, " ", case.last_modifying_user.family_name)
    $Case_Closed = case.closure_details.reason
    $Root_Cause = case.closure_details.root_cause
    
    match:
        $Case_ID, $Case_Name, $Case_Creation_Time, $Last_Stage, $Case_Status, $Last_Handled_Analyst, $Case_Closed, $Root_Cause
    
    order:
        $Case_Creation_Time desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Cases Over Time  | 
    
    
    $Date = timestamp.get_date(case.create_time.seconds)
    
    match:
        $Date
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Date desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Case Statistics  | 
    
    
    $Timestamp_Month = timestamp.get_timestamp(case.create_time.seconds, "%Y-%m")
    
    match:
        $Timestamp_Month
    
    outcome:
        $Alert_Count = count(case.alerts.metadata.id)
        $Cases_Count = count_distinct(case.name)
        $High_Priority_Case_Count = sum(if(case.priority = "PRIORITY_HIGH" or case.priority = "PRIORITY_CRITICAL", 1, 0))
        $Incident_Count = sum(if(case.incident = true, 1, 0))
        $High_Priority_Incident_Count = sum(if(case.incident = true and (case.priority = "PRIORITY_HIGH" or case.priority = "PRIORITY_CRITICAL"), 1, 0))
    
    order:
        $Timestamp_Month desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Incident Closure Reasons Distribution  | 
    
    
    case.incident = true
    
    $Reason = case.closure_details.reason
    
    match:
        $Reason
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Incident Severities Distribution  | 
    
    
    case.incident = true
    
    $Severity = case.alerts.metadata.detection.severity
    
    match:
        $Severity
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Incidents Over Time  | 
    
    
    case.incident = true
    
    $Date = timestamp.get_date(case.create_time.seconds)
    
    match:
        $Date
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Date desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Incident Priorities Distribution  | 
    
    
    case.incident = true
    
    $Priority = case.priority
    
    match:
        $Priority
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Top 10 MITRE Techniques by Incident  | 
    
    
    case.incident = true
    case.alerts.metadata.tags = /T[0-9]+/
    
    $Technique = case.alerts.metadata.tags
    
    match:
        $Technique
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc
    
    limit:
        10   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Top 10 Case Tags  | 
    
    
    $Case_Tag = case.tags.name
    
    match:
        $Case_Tag
    
    outcome:
        $Count = count(case.tags.name)
    
    order:
        $Count desc
    
    limit:
        10   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  List of Environments  | 
    
    
    $Environment = case.environment
    
    match:
        $Environment   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Top 10 Incidents by Root Cause  | 
    
    
    case.incident = true
    
    $Root_Cause = case.closure_details.root_cause
    
    match:
        $Root_Cause
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc
    
    limit:
        10   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Top 10 Cases Closed  | 
    
    
    case.status = "CLOSED"
    
    $Case = case.display_name
    
    match:
        $Case
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc
    
    limit:
        10   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Low Priority Cases  | 
    
    
    case.priority = "PRIORITY_MEDIUM"
    or case.priority = "PRIORITY_LOW"
    or case.priority = "PRIORITY_INFO"
    
    $Timestamp_Daily = timestamp.get_date(case.create_time.seconds)
    $Priority = case.priority
    
    match:
        $Timestamp_Daily, $Priority
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Timestamp_Daily desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Case Actions Over Time  | 
    
    
    $Date = timestamp.get_date(case.create_time.seconds)
    $Stage = case.stage
    
    match:
        $Date, $Stage
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Date desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Case Distribution by Priority - Open Cases  | 
    
    
    case.status = "OPENED"
    
    $Priority = case.priority
    
    match:
        $Priority
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Total Open Incidents  | 
    
    
    case.incident = true
    case.status = "OPENED"
    
    outcome:
        $Count = count(case.name)   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Case Priorities Distribution  | 
    
    
    $Priority = case.priority
    
    match:
        $Priority
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Total Closed Incidents  | 
    
    
    case.incident = true
    case.status = "CLOSED"
    
    outcome:
        $Count = count(case.name)   
  
Case & Incident Analytics (SOAR)  |  Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency.  |  Case Closure Reason Distribution  | 
    
    
    $Reason = case.closure_details.reason
    
    match:
        $Reason
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
FEDRAMP Continuous Monitoring  |  Provides visibility into Fedramp compliance metrics and vulnerability tracking. Use these insights to prioritize remediation efforts and ensure a strong security posture.  |  Case Distribution by Priority - Closed Cases  | 
    
    
    case.status = "CLOSED"
    
    $Priority = case.priority
    
    match:
        $Priority
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
FEDRAMP Continuous Monitoring  |  Provides visibility into Fedramp compliance metrics and vulnerability tracking. Use these insights to prioritize remediation efforts and ensure a strong security posture.  |  Case Distribution by Priority - Open Cases  | 
    
    
    case.status = "OPENED"
    
    $Priority = case.priority
    
    match:
        $Priority
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
HIPAA Dashboard  |  Provides visibility into PHI access and potential HIPAA violations to support proactive risk management. ensure the `ePHI_assets.Hostname` data table is created for charts to load.  |  Open Cases Distribution by Priority  | 
    
    
    case.status = "OPENED"
    
    $Priority = case.priority
    
    match:
        $Priority
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc   
  
ISO27001 - Organizational Controls  |  Provides real-time tracking of ISO 27001 audit metrics and security controls to identify gaps and maintain compliance. Note: Filters are required to refine results.  |  Top 10 Analysts by Incident Closures  | 
    
    
    case.status = "CLOSED"
    case.incident = true
    
    $Analyst = strings.concat(case.assignee.given_name, " ", case.assignee.family_name)
    
    match:
        $Analyst
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc
    
    limit:
        10   
  
ISO27001 - Organizational Controls  |  Provides real-time tracking of ISO 27001 audit metrics and security controls to identify gaps and maintain compliance. Note: Filters are required to refine results.  |  Average Case Closure Time by Priority  | 
    
    
    case.status = "CLOSED"
    
    $Case_Closed_Time = if(case.status = "CLOSED", case.update_time.seconds, 0)
    $Priority = case.priority
    
    match:
        $Priority
    
    outcome:
        $Case_Create_Time = min(case.create_time.seconds)
        $Case_Close_Time = min($Case_Closed_Time)
        $Closure_Time = math.round((($Case_Close_Time - $Case_Create_Time)/60), 2)
    
    order:
        $Priority desc
    
    unselect:
        $Case_Create_Time, $Case_Close_Time   
  
SOC Workflow Monitoring (SOAR)  |  Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs.  |  Case Closure Time  | 
    
    
    $Case_ID = case.response_platform_info.response_platform_id
    $Case_Close_Time_ = if(case.status = "CLOSED", case.update_time.seconds, 0)
    $Priority = case.priority
    
    match:
        $Case_ID, $Priority
    
    outcome:
        $Case_Create_Time = min(case.create_time.seconds)
        $Case_Close_Time = min($Case_Close_Time_)
        $Closure_Time = ($Case_Close_Time - $Case_Create_Time)/60
    
    order:
        $Closure_Time desc
    
    unselect:
        $Case_Create_Time, $Case_Close_Time   
  
SOC Workflow Monitoring (SOAR)  |  Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs.  |  Total Incidents Handled Automatically  | 
    
    
    case.closure_details.case_closed_action = "AUTOMATIC"
    case.incident = true
    
    outcome:
        $Count = count(case.incident)   
  
SOC Workflow Monitoring (SOAR)  |  Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs.  |  Analyst's Performance  | 
    
    
    case.assignee.email != ""
    
    $User = case.assignee.email
    
    match:
        $User
    
    outcome:
        $Open_Cases_Count = sum(if(case.status="OPENED", 1, 0))
        $Closed_Cases_Count = sum(if(case.status="CLOSED", 1, 0))   
  
SOC Workflow Monitoring (SOAR)  |  Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs.  |  Automatically vs Manually Handled Incidents Over Time  | 
    
    
    case.closure_details.case_closed_action = "MANUALLY"
    or case.closure_details.case_closed_action = "AUTOMATIC"
    
    case.incident = true
    
    $Date = timestamp.get_date(case.create_time.seconds)
    
    match:
        $Date, case.closure_details.case_closed_action
    
    outcome:
        $Count = count(case.incident)   
  
SOC Workflow Monitoring (SOAR)  |  Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs.  |  Case Closure Summary  | 
    
    
    case.status = "CLOSED"
    
    $Case_ID = case.response_platform_info.response_platform_id
    $Case_Create_Timestamp = timestamp.get_timestamp(case.create_time.seconds, "%F %T ")
    $Case_Close_Timestamp = timestamp.get_timestamp(case.update_time.seconds, "%F %T ")
    $Case_Close_Time_ = if(case.status = "CLOSED", case.update_time.seconds, 0)
    
    match:
        $Case_ID, $Case_Create_Timestamp, $Case_Close_Timestamp
    
    outcome:
        $Case_Create_Time = min(case.create_time.seconds)
        $Case_Close_Time = min($Case_Close_Time_)
        $Closure_Time = ($Case_Close_Time - $Case_Create_Time)/60
    
    order:
        $Case_ID desc
    
    unselect:
        $Case_Create_Time, $Case_Close_Time   
  
SOC Workflow Monitoring (SOAR)  |  Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs.  |  Total Incidents Handled Manually  | 
    
    
    case.closure_details.case_closed_action = "MANUALLY"
    case.incident = true
    
    outcome:
        $Count = count(case.incident)   
  
SOC Workflow Monitoring (SOAR)  |  Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs.  |  Top 10 Analysts by Incident Closure  | 
    
    
    case.status = "CLOSED"
    case.incident = true
    
    $Analyst = strings.concat(case.assignee.given_name, " ", case.assignee.family_name)
    
    match:
        $Analyst
    
    outcome:
        $Count = count(case.name)
    
    order:
        $Count desc
    
    limit:
        10   
  
SOC Workflow Monitoring (SOAR)  |  Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs.  |  Top 10 Users by Case  | 
    
    
    case.alerts.entities.type = "USERUNIQNAME"
    
    match:
        case.alerts.entities.type, case.alerts.entities.identifier
    
    outcome:
        $Count = count_distinct(case.alerts.metadata.id)
    
    order:
        $Count desc
    
    limit:
        10   
  
SOC Workflow Monitoring (SOAR)  |  Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs.  |  Average Case Closure Time by Priority  | 
    
    
    case.status = "CLOSED"
    
    $Case_Close_Time_ = if(case.status = "CLOSED", case.update_time.seconds, 0)
    $Priority = case.priority
    
    match:
        $Priority
    
    outcome:
        $Case_Create_Time = min(case.create_time.seconds)
        $Case_Close_Time = min($Case_Close_Time_)
        $Closure_Time = ($Case_Close_Time - $Case_Create_Time)/60
    
    order:
        $Priority desc
    
    unselect:
        $Case_Create_Time, $Case_Close_Time   
  
SOC Workflow Monitoring (SOAR)  |  Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs.  |  Case Assignments Over Time  | 
    
    
    case.assignee.email != ""
    
    $User = case.assignee.email
    $Date = timestamp.get_date(case.create_time.seconds)
    
    match:
        $User, $Date
    
    outcome:
        $Count = count_distinct(case.response_platform_info.response_platform_id)
    
    order:
        $Count desc   
  
SOC Workflow Monitoring (SOAR)  |  Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs.  |  Alert Detection Summary  | 
    
    
    $Case_ID = case.response_platform_info.response_platform_id
    $Alert = strings.coalesce(case.alerts.metadata.detection.threat_name, case.alerts.metadata.detection.rule_name)
    $Alert_Generation_Timestamp = timestamp.get_timestamp(case.alerts.metadata.detection_time.seconds, "%F %T ")
    $Alert_Detection_Timestamp = timestamp.get_timestamp(case.alerts.metadata.created_time.seconds, "%F %T ")
    
    match:
        $Case_ID, $Alert, $Alert_Generation_Timestamp, $Alert_Detection_Timestamp
    
    outcome:
        $Alert_Generation_Time = min(case.alerts.metadata.detection_time.seconds)
        $Alert_Detection_Time = min(case.alerts.metadata.created_time.seconds)
        $Detection_Delay = math.abs(($Alert_Detection_Time- $Alert_Generation_Time)/60)
    
    order:
        $Alert_Generation_Time desc
    
    unselect:
        $Alert_Generation_Time, $Alert_Detection_Time   
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  Open Cases by Age  | 
    
    
    case.status = "OPENED"
    
    match:
    case.display_name, case.environment
    
    outcome:
    $Age = max(timestamp.current_seconds() - case.create_time.seconds)/86400
    $Day_Range = if($Age >= 21, "> 3 Weeks",
    if($Age >= 14 and $Age < 21, "2 Weeks",
    if($Age >= 7 and $Age < 14, "1 Week",
    if($Age <= 2 and $Age > 1, "2 Days",
    if($Age < 1, "Same Day")))))
    
    order:
    $Age desc  
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  Cases Last Update more than 7 Days Ago  | 
    
    
    case.status = "OPENED"
    
    match:
        case.environment
    
    outcome:
        $Age = (timestamp.current_seconds() - max(case.update_time.seconds))/86400
        $Day_Range = if($Age >= 21, ">3 Weeks",
                      if($Age >= 14, "2 Weeks",
                      if($Age >= 7, "1 Week")))
        $Count = count_distinct(case.name)
    
    condition:
        $Age >= 7   
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  Open Case Tags Overview - 7 days  | 
    
    
    case.status = "OPENED"
    $Tag = case.tags.name
    $Tag !=""
    
    match:
        $Tag
    
    outcome:
        $Count = count(case.response_platform_info.response_platform_id)
    
    order:
        $Count desc
    
       
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  Analyst Productivity (Closed Cases) - 7 days  | 
    
    
    case.assignee.email != ""
    
    $User = case.assignee.email
    
    match:
        $User
    
    outcome:
        $Closed_Cases_Count = sum(if(case.status="CLOSED", 1, 0))
    
    order:
        $Closed_Cases_Count desc    
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  Open Cases by Environment - Last 7 Days  | 
    
    
    case.status = "OPENED"
    
    $Date = timestamp.get_date(case.create_time.seconds)
    
    match:
        $Date, case.environment
    
    outcome:
        $count = count_distinct(case.response_platform_info.response_platform_id)   
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  | 
    
    
    case.status = "CLOSED"
    
    outcome:
     $Count = count(case.name)  
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  Analyst Workloads  | 
    
    
    case.assignee.email != ""
    
    $User = case.assignee.email
    $Date = timestamp.get_date(case.create_time.seconds)
    
    match:
        $User, $Date
    
    outcome:
        $Count = count(case.response_platform_info.response_platform_id)   
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  | 
    
    
    case.status = "OPENED"
    or case.status = "CLOSED"
    
    outcome:
        $total = count_distinct(case.response_platform_info.response_platform_id)   
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  % Automated Closure - Last 7 Days  | 
    
    
    case.status = "CLOSED"
    
    outcome:
        $TotalClosedCases = count_distinct(case.name)
        $AutoClosedCases = sum(if(case.closure_details.case_closed_action = "AUTOMATIC", 1, 0))
        $Automation_Rate = if($TotalClosedCases > 0, math.round(($AutoClosedCases / $TotalClosedCases) * 100, 0), 0)
       
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  Cases Priority - Last 24 Hours  | 
    
    
    case.status = "OPENED"
    
    $Priority = case.priority
    
    match:
        $Priority
    
    outcome:
        $Count = count_distinct(case.response_platform_info.response_platform_id)
    
    order:
        $Priority desc   
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  MTTR by SOC Role - Last 7 Days  | 
    
    
    case.status = "CLOSED"
    case.assignee.soc_roles != ""
    
    $SOC_Role = case.assignee.soc_roles
    $Date = timestamp.get_date(case.create_time.seconds)
    
    match:
        $SOC_Role, $Date
    
    outcome:
        $MTTR = math.round(avg((case.update_time.seconds - case.create_time.seconds) / 60) ,2)   
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  Open Critical/High Cases - Last 24 Hours  | 
    
    
    case.status = "OPENED"
    case.priority = "PRIORITY_CRITICAL" or case.priority = "PRIORITY_HIGH"
    
    outcome:
        $count = count_distinct(case.response_platform_info.response_platform_id)   
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  Analyst Backlog (Open Cases) - 7 days  | 
    
    
    case.assignee.email != ""
    case.status = "OPENED"
    
    $User = case.assignee.email
    
    match:
        $User
    
    outcome:
        $Open_Cases_Count = sum(if(case.status="OPENED", 1, 0))
    
    order:
        $Open_Cases_Count desc
       
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  | 
    
    
    case.status = "OPENED"
    
    outcome:
        $total = count_distinct(case.response_platform_info.response_platform_id)   
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  Top 10 MITRE ATT&CK Tactics - Last 7 Days  | 
    
    
    $Tactic = case.alerts.metadata.tags
    $Tactic = /^TA+/
    
    match:
        $Tactic
    
    outcome:
        $Count = count_distinct(case.name)
    
    order:
        $Count desc
    
    limit:
        10
       
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  | 
    
    
    case.incident = true
    case.status = "OPENED"
    
    outcome:
        $Count = count(case.name)   
  
Security Management Overview  |  Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture.  |  Top 10 MITRE ATT&CK Techniques - Last 7 Days  | 
    
    
    $Technique = case.alerts.metadata.tags
    $Technique = /^T1+/
    
    match:
        $Technique
    
    outcome:
        $Count = count_distinct(case.name)
    
    order:
    $Count desc
    
    limit:
    10  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
