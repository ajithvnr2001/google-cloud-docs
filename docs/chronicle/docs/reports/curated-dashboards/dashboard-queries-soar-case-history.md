---
url: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-soar-case-history/
title: Query SOAR case history \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:10:56.179319+00:00
---

# Query SOAR case history  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-soar-case-history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query SOAR case history

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document is for Security Operations Center (SOC) managers and analysts who want to monitor threat landscapes and system health using curated dashboards— predefined dashboards designed for visibility across various security use cases. This document provides a collection of curated dashboards and their underlying queries for the **SOAR case history** source type.

You can use these queries in the query editor or as a baseline for custom widgets. For information on how to create and manage dashboards, see [Manage dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards).

CIS Controls Compliance OverviewCase & Incident Analytics (SOAR)SOC Workflow Monitoring (SOAR)Security Management Overview

Mean Time to Resolve (MTTR)Reopened CasesMTTA (Time to Acknowledge) - MinutesMTTR (Time to Resolution in mins) - Last 7 DaysMTTI (Time to Investigate in mins) - Last 7 DaysTotal Cases Exceeding SLAHandling Time by Case Stage - Last 7 DaysMTTA (Time to Acknowledge in mins) Last 7 DaysCase Creation vs. Closure Rate - Last 7 DaysMTTI (Time to Investigate in mins ) - Last 7 Days

Dashboard name  |  Description  |  Chart name  |  Query   
---|---|---|---  
CIS Controls Compliance Overview | Provides a central view of CIS compliance metrics, such as asset accuracy and backup reliability. use these insights to strengthen security governance and track remediation progress. | Mean Time to Resolve (MTTR) | 
    
    
    stage stage1{
    $case_id = case_history.case_response_platform_info.case_id
    match:
        $case_id
    outcome:
        $case_close_time = max(if(case_history.case_activity = "CLOSE_CASE", case_history.event_time.seconds, 0))
        $status = array_distinct(case_history.case_activity)
        $TTC = $case_close_time - min(case_history.event_time.seconds)
    condition:
        arrays.contains($status, "CREATE_CASE") and arrays.contains($status, "CLOSE_CASE")
        
        }
    outcome:
        $case_count = count($stage1.case_id)
        $MTTC = math.abs(math.round(avg($stage1.TTC)/60))
    
      
  
Case & Incident Analytics (SOAR) | Provides a centralized view of case management and incident response, enabling teams to resolve threats faster and continuously improve operational efficiency. | Reopened Cases | 
    
    
    case_history.case_activity = "REOPEN_CASE"
    
    outcome:
        $Count = count(case_history.name)  
  
SOC Workflow Monitoring (SOAR) | Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs. | MTTA (Time to Acknowledge) - Minutes | 
    
    
    stage stage1{
    $case_id = case_history.case_response_platform_info.case_id
    match:
        $case_id
    outcome:
        $case_assign_time = min(if(case_history.case_activity = "ASSIGNEE_CHANGE", case_history.event_time.seconds, 9999999999999999))
        $status = array_distinct(case_history.case_activity)
        $TTA = $case_assign_time - min(case_history.event_time.seconds)
        
    condition:
        arrays.contains($status, "CREATE_CASE") and arrays.contains($status, "ASSIGNEE_CHANGE") 
        }
    outcome:
        $case_count = count($stage1.case_id)
        $MTTA = (math.round((avg($stage1.TTA)/60)))
    
      
  
SOC Workflow Monitoring (SOAR) | Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs. | MTTR (Time to Resolution in mins) - Last 7 Days | 
    
    
    stage stage1{
    $case_id = case_history.case_response_platform_info.case_id
    match:
        $case_id
    outcome:
        $case_close_time = max(if(case_history.case_activity = "CLOSE_CASE", case_history.event_time.seconds, 0))
        $status = array_distinct(case_history.case_activity)
        $TTC = $case_close_time - min(case_history.event_time.seconds)
    condition:
        arrays.contains($status, "CREATE_CASE") and arrays.contains($status, "CLOSE_CASE")
        
        }
    outcome:
        $case_count = count($stage1.case_id)
        $MTTC = (math.round(avg($stage1.TTC)/60))
    
      
  
SOC Workflow Monitoring (SOAR) | Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs. | MTTI (Time to Investigate in mins) - Last 7 Days | 
    
    
    stage stage1{
    $case_id = case_history.case_response_platform_info.case_id
    match:
        $case_id
    outcome:
        $case_close_time = max(if(case_history.case_activity = "CLOSE_CASE", case_history.event_time.seconds, 0))
        $case_assign_time = min(if(case_history.case_activity = "ASSIGNEE_CHANGE", case_history.event_time.seconds, 9999999999999999))
        $status = array_distinct(case_history.case_activity)
        $TTI = $case_close_time - $case_assign_time
    condition:
        arrays.contains($status, "CREATE_CASE") and arrays.contains($status, "CLOSE_CASE")
        AND arrays.contains($status, "ASSIGNEE_CHANGE") 
        }
    outcome:
        $case_count = count($stage1.case_id)
    
        $MTTI = (math.round(avg($stage1.TTI)/60))  
  
SOC Workflow Monitoring (SOAR) | Provides centralized tracking of alert detection, incident handling, and case management metrics. Use these insights to optimize resources, improve response efficiency, and maintain adherence to SLAs. | Total Cases Exceeding SLA | 
    
    
    case_history.case_activity = "EXCEEDED_SLA"
    case_history.sla_type = "CASE_SLA"
    
    outcome:
       $Count = count(case_history.case_activity)  
  
Security Management Overview | Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture. | Handling Time by Case Stage - Last 7 Days | 
    
    
    case_history.assignee.soc_roles != ""
    
    $Case_ID = case_history.case_response_platform_info.case_id
    $Case_Stage = case_history.stage
    
    match:
        $Case_Stage
    
    outcome:
        $Handling_Time_Minutes = (max(case_history.event_time.seconds) - min(case_history.event_time.seconds)) / 60  
  
Security Management Overview | Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture. | MTTA (Time to Acknowledge in mins) Last 7 Days | 
    
    
    stage stage1{
    $case_id = case_history.case_response_platform_info.case_id
    match:
        $case_id
    outcome:
        $case_assign_time = min(if(case_history.case_activity = "ASSIGNEE_CHANGE", case_history.event_time.seconds, 9999999999999999))
        $status = array_distinct(case_history.case_activity)
        $TTA = $case_assign_time - min(case_history.event_time.seconds)
        
    condition:
        arrays.contains($status, "CREATE_CASE") and arrays.contains($status, "ASSIGNEE_CHANGE") 
        }
    outcome:
        $case_count = count($stage1.case_id)
        $MTTA = (math.round((avg($stage1.TTA)/60)))
    
      
  
Security Management Overview | Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture. | Case Creation vs. Closure Rate - Last 7 Days | 
    
    
    case_history.case_activity = "CREATE_CASE" 
    or case_history.case_activity = "CLOSE_CASE"
    
    $Case_Activity = case_history.case_activity
    $Date = timestamp.get_date(case_history.event_time.seconds) 
    
    match: 
        $Date, $Case_Activity
    
    outcome: 
        $Count = count_distinct(case_history.case_response_platform_info.case_id)
    
    order:
        $Date desc  
  
Security Management Overview | Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture. | MTTR (Time to Resolution in mins) - Last 7 Days | 
    
    
    stage stage1{
    $case_id = case_history.case_response_platform_info.case_id
    match:
        $case_id
    outcome:
        $case_close_time = max(if(case_history.case_activity = "CLOSE_CASE", case_history.event_time.seconds, 0))
        $status = array_distinct(case_history.case_activity)
        $TTC = $case_close_time - min(case_history.event_time.seconds)
    condition:
        arrays.contains($status, "CREATE_CASE") and arrays.contains($status, "CLOSE_CASE")
        
        }
    outcome:
        $case_count = count($stage1.case_id)
        $MTTC = (math.round(avg($stage1.TTC)/60))
    
      
  
Security Management Overview | Provides centralized visibility into response performance and operational trends. It helps security teams track progress and make informed decisions to strengthen the security posture. | MTTI (Time to Investigate in mins ) - Last 7 Days | 
    
    
    stage stage1{
    $case_id = case_history.case_response_platform_info.case_id
    match:
        $case_id
    outcome:
        $case_close_time = max(if(case_history.case_activity = "CLOSE_CASE", case_history.event_time.seconds, 0))
        $case_assign_time = min(if(case_history.case_activity = "ASSIGNEE_CHANGE", case_history.event_time.seconds, 9999999999999999))
        $status = array_distinct(case_history.case_activity)
        $TTI = $case_close_time - $case_assign_time
    condition:
        arrays.contains($status, "CREATE_CASE") and arrays.contains($status, "CLOSE_CASE")
        AND arrays.contains($status, "ASSIGNEE_CHANGE") 
        }
    outcome:
        $case_count = count($stage1.case_id)
    
        $MTTI = (math.round(avg($stage1.TTI)/60))  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
