---
url: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-soar-playbooks/
title: Query SOAR playbooks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:01:27.451347+00:00
---

# Query SOAR playbooks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-soar-playbooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query SOAR playbooks

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document is for Security Operations Center (SOC) managers and analysts who want to monitor threat landscapes and system health using curated dashboards— predefined dashboards designed for visibility across various security use cases. This document provides a collection of curated dashboards and their underlying queries for the **SOAR playbooks** source type.

You can use these queries in the query editor or as a baseline for custom widgets. For information on how to create and manage dashboards, see [Manage dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards).

Playbook Dashboard (SOAR)

Failed Playbooks DistributionAutomation Distribution by EnvironmentFailed RunsFailed Playbook Runs per PlaybookAlerts Closed per PlaybookFailed ActionsFailed Playbook SummaryTotal Playbook RunsFailed Playbooks Over TimeTotal Failed Playbook RunsAverage Runtime in MinutesAlerts Closed by AutomationFailed Actions DistributionFailed ActionsAverage Runtime per PlaybookAlerts Closed by Automation per EnvironmentAlerts Handled per Playbook by StatusTotal PlaybooksPlaybook Trigger TrendPlaybook DistributionManual ActionsTotal Cases with Failed Playbook RunsTop 10 Playbook ActionsPlaybook QueueTotal Failed Playbooks

Dashboard name  |  Description  |  Chart name  |  Query   
---|---|---|---  
Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Failed Playbooks Distribution | 
    
    
    playbook.status = "FAILED"
    
    $Playbook_Name = playbook.display_name
    
    match:
       $Playbook_Name
    
    outcome:
       $Total_Playbook_Runs = count(playbook.name)
    
    order:
       $Total_Playbook_Runs desc  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Automation Distribution by Environment | 
    
    
    $Automatic = playbook.metadata.automatic
    $Environment = playbook.metadata.environments
    
    match:
        $Environment, $Automatic
    
    outcome:
        $Total_Playbook_Runs = count(playbook.name)
    
    order:
        $Total_Playbook_Runs desc  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Failed Runs | 
    
    
    outcome:
       $Total_Playbook_Runs = count(playbook.name)
       $Playbook_Failed = sum(if(playbook.status = "FAILED", 1, 0))
       $Percentage = math.round(($Playbook_Failed/$Total_Playbook_Runs) *100, 2)  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Failed Playbook Runs per Playbook | 
    
    
    $Playbook_Name = playbook.display_name
    
    match:
        $Playbook_Name
    
    outcome:
        $Total_Playbook_Runs = count(playbook.name)
        $Playbook_Failed = sum(if(playbook.status = "FAILED", 1,0))
        $Percentage = math.round(($Playbook_Failed/$Total_Playbook_Runs) *100, 2)
    
    order:
        $Percentage desc  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Alerts Closed per Playbook | 
    
    
    $Playbook_Name = playbook.display_name
    
    match:
        $Playbook_Name
    
    outcome:
        $Total_Playbook_Runs = count(playbook.name)
        $Alerts_Closed = sum(if(playbook.status = "COMPLETED" and playbook.action.action = /close/ nocase, 1,0))
        $Percentage = math.round(($Alerts_Closed/$Total_Playbook_Runs) *100, 2)
    
    order:
        $Percentage desc  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Failed Actions | 
    
    
    $Action_Name =  playbook.action.action
    
    match:
       $Action_Name
    
    outcome:
       $Total_Actions = count(playbook.action.name)
       $Faulted_Action = sum(if(playbook.action.status="FAULTED", 1, 0))
       $Percentage = math.round(($Faulted_Action/$Total_Actions)*100, 2)
    
    order:
       $Percentage desc
      
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Failed Playbook Summary | 
    
    
    playbook.status = "FAILED"
    
    $Environment = playbook.metadata.environments
    $CaseID = playbook.action.case_metadata.case_id
    $Playbook_Name = playbook.display_name
    $Playbook_Status = playbook.status
    $Action_Name = playbook.action.action
    $Action_Status = playbook.action.status
    $Action_Status = "FAULTED"
    $Action_Message = playbook.action.result_message
    
    match:
        $Environment, $CaseID, $Playbook_Name, $Playbook_Status, $Action_Name, $Action_Status, $Action_Message
    
    outcome:
        $Playbook_Triggered_Time = timestamp.get_timestamp(max(playbook.start_time.seconds), "%F %T")
    
    order:
        $Playbook_Triggered_Time desc  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Total Playbook Runs | 
    
    
    outcome:
       $Total_Playbook_Runs = count(playbook.name)
      
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Failed Playbooks Over Time | 
    
    
    playbook.status = "FAILED"
    
    $Playbook_Name = playbook.display_name
    $Date = timestamp.get_date(playbook.start_time.seconds)
    
    match:
        $Date, $Playbook_Name
    
    outcome:
        $Total_Playbook_Runs = count(playbook.name)
    
    order:
        $Date asc  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Total Failed Playbook Runs | 
    
    
    playbook.status = "FAILED"
    
    outcome:
       $Total_Playbook_Runs = count(playbook.name)  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Average Runtime in Minutes | 
    
    
    outcome:
        $Average = math.round(avg((playbook.end_time.seconds  - playbook.start_time.seconds)/60), 2)
    
          
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Alerts Closed by Automation | 
    
    
    playbook.metadata.automatic = true
    playbook.action.automatic = true
    
    outcome:
        $Total_Playbook_Runs = count(playbook.name)
        $Alerts_Closed = sum(if(playbook.status = "COMPLETED" and playbook.action.action = /close/ nocase, 1,0))
        $Percentage = math.round(($Alerts_Closed/$Total_Playbook_Runs) *100, 2)  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Failed Actions Distribution | 
    
    
    playbook.action.status = "FAULTED"
    
    $Action_Name = playbook.action.action
    
    match:
        $Action_Name
    
    outcome:
        $Total_Actions = count(playbook.action.name)
    
    order:
        $Total_Actions desc  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Failed Actions | 
    
    
    outcome:
       $Total_Actions = count(playbook.action.name)
       $Faulted_Actions = sum(if(playbook.action.status = "FAULTED", 1, 0))
       $Percentage = math.round(($Faulted_Actions/$Total_Actions)*100, 2)  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Average Runtime per Playbook | 
    
    
    $Playbook_Name = playbook.display_name
    
    match:
        $Playbook_Name
    
    outcome:
        $Average = math.round(window.avg((playbook.end_time.seconds  - playbook.start_time.seconds)/60), 2)
    
    order:
        $Average desc
      
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Alerts Closed by Automation per Environment | 
    
    
    playbook.metadata.automatic = true
    playbook.action.automatic = true
    
    $Environment = playbook.metadata.environments
    
    match:
        $Environment
    
    outcome:
        $Total_Alerts = count(playbook.name)
        $Alerts_Closed = sum(if(playbook.status = "COMPLETED" and playbook.action.action = /close/ nocase, 1,0))
        $Percentage = math.round(($Alerts_Closed/$Total_Alerts) *100, 2)
    
    order:
        $Percentage desc  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Alerts Handled per Playbook by Status | 
    
    
    $Playbook_Name = playbook.display_name
    $Playbook_Status = playbook.status
    
    match:
        $Playbook_Name, $Playbook_Status
    
    outcome:
        $Total_Alerts = count(playbook.name)
    
    order:
        $Total_Alerts desc
      
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Total Playbooks | 
    
    
    outcome:
       $Playbook_Count = count_distinct(playbook.display_name)  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Playbook Trigger Trend | 
    
    
    playbook.start_time.seconds > 0
    
    $Playbook_Name = playbook.display_name
    $Date = timestamp.get_date(playbook.start_time.seconds)
    
    match:
        $Date, $Playbook_Name
    
    outcome:
        $Total_Playbook_Runs = count(playbook.name)
    
    order:
        $Date asc
      
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Playbook Distribution | 
    
    
    $Playbook_Name = playbook.display_name
    
    match:
        $Playbook_Name
    
    outcome:
        $Total_Playbook_Runs = count(playbook.name)
    
    order:
        $Total_Playbook_Runs desc  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Manual Actions | 
    
    
    outcome:
        $Total_Playbook_Actions = count(playbook.action.automatic)
        $Manual_Action = sum(if(playbook.action.automatic = false, 1,0))
        $Percentage = math.round(($Manual_Action/$Total_Playbook_Actions)*100, 2)  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Total Cases with Failed Playbook Runs | 
    
    
    playbook.status = "FAILED"
    
    outcome:
        $Total_Case_IDs = count_distinct(playbook.action.case_metadata.case_id)
    
      
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Top 10 Playbook Actions | 
    
    
    $Playbook_Name = playbook.display_name
    $Action_Name = playbook.action.action
    $Action_Automatic = playbook.action.automatic
    $Action_Status = playbook.action.status
    $Action_Message = playbook.action.result_message
    
    match:
        $Playbook_Name, $Action_Name, $Action_Automatic, $Action_Status, $Action_Message
    
    outcome:
        $Total_Playbook_Runs = count(playbook.name)
        $Playbook_Triggered_Time = timestamp.get_timestamp(max(playbook.start_time.seconds), "%F %T")
    
    order:
        $Total_Playbook_Runs desc
    
    limit:
        10  
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Playbook Queue | 
    
    
    playbook.status = "PENDING_IN_QUEUE"
    
    $Environment = playbook.metadata.environments
    $Playbook_Name = playbook.display_name
    $Playbook_Status = playbook.status
    
    match:
       $Playbook_Name, $Playbook_Status, $Environment
    
    outcome:
        $Total_Playbook_Runs = count(playbook.name)
    
    order:
        $Total_Playbook_Runs desc
      
  

Playbook Dashboard (SOAR) | Provides insights into playbook performance and automation efficiency, including metrics on alerts handled, average run times, and execution errors.   
Note: Apply filters to display relevant results. | Total Failed Playbooks | 
    
    
    playbook.status = "FAILED"
    
    outcome:
        $Total_Failed_Playbooks = count_distinct(playbook.display_name)  
  

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
