---
url: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-udm-/
title: Run UDM queries \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:24:28.182161+00:00
---

# Run UDM queries  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-udm-/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run UDM queries

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document is for Security Operations Center (SOC) managers and analysts who want to monitor threat landscapes and system health using curated dashboards— predefined dashboards designed for visibility across various security use cases in Google Security Operations. This document provides a collection of curated dashboards and their underlying queries for the **UDM** source type.

The following tables provide a list of charts and their query examples for each curated dashboard. You can use these queries in the query editor or as a baseline for custom widgets. For information on how to create and manage dashboards, see [Manage dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards).

## Application Control

This dashboard provides insights on application security, helping security teams detect unauthorized software and enforce usage policies. It supports visibility into risky behaviors, blocked attempts, and unusual activity patterns.

**Note:** Apply the available filters to refine the data and display relevant results.

Application Executions Over TimeTop 10 Unapproved Application Executions (Audit/Allow Mode)Top 10 Applications Executing from Removable MediaTop 10 Blocked Application Executions By ReasonApplication Executions Status Over TimeTop 10 Blocked Application ExecutionsApplications Executing from Atypical LocationsTop 10 Hosts by Blocked ExecutionTop 10 Users by Blocked ExecutionBlocked Executions - Hourly

Chart name | Query example  
---|---  
Application Executions Over Time | 
    
    
    metadata.product_event_type = /(execution|application) (allow|block)/ nocase
    or security_result.threat_name = /application control/ nocase
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F")
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Unapproved Application Executions (Audit/Allow Mode) | 
    
    
    metadata.product_event_type != /(execution|application) block/ nocase
    metadata.product_event_type = /unapproved/ nocase
    
    $Application = strings.coalesce(about.file.full_path, target.process.file.full_path, additional.fields["fname"])
    
    match:
      $Application
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Applications Executing from Removable Media | 
    
    
    metadata.product_event_type = /(execution|application) (allow|block)/ nocase
    or security_result.threat_name = /application control/ nocase
    strings.coalesce(about.file.full_path, target.process.file.full_path, additional.fields["fname"]) = /(^(D|E|F|G):)|\/\/removable|usb/ nocase
    
    $Application = strings.coalesce(about.file.full_path, target.process.file.full_path, additional.fields["fname"])
    
    match:
      $Application
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Blocked Application Executions By Reason | 
    
    
    metadata.product_event_type = /(execution|application) block/ nocase
    or security_result.threat_name = /application control/ nocase
    security_result.action = "BLOCK"
    
    $Application = strings.coalesce(about.file.full_path, target.process.file.full_path, additional.fields["fname"])
    $Reason = strings.coalesce(target.resource.attribute.labels["categoryTupleDescription"], security_result.action_details, metadata.product_event_type)
    
    match:
      $Application, $Reason
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Application Executions Status Over Time | 
    
    
    metadata.product_event_type = /(execution|application) (allow|block)/ nocase
    or security_result.threat_name = /application control/ nocase
    
    $Action = strings.coalesce(if(security_result.action = "BLOCK", "BLOCK", "ALLOW"), if(metadata.product_event_type = /(execution|application) block/ nocase, "BLOCK", "ALLOW"))
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds,"%F")
    
    match:
      $Action, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc   
  
Top 10 Blocked Application Executions | 
    
    
    metadata.product_event_type = /(execution|application) block/ nocase
    or security_result.threat_name = /application control/ nocase
    security_result.action = "BLOCK"
    
    $Application = strings.coalesce(about.file.full_path, target.process.file.full_path, additional.fields["fname"])
    
    match:
      $Application
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Applications Executing from Atypical Locations | 
    
    
    strings.coalesce(about.file.full_path, target.process.file.full_path, additional.fields["fname"]) = /C\:\\(?:Users|Temp|Windows)\\(?:.*\\(?:AppData|Downloads)?|Temp)?/ nocase
    
    $File_Path = strings.coalesce(about.file.full_path, target.process.file.full_path, additional.fields["fname"])
    
    match:
      $File_Path  
  
Top 10 Hosts by Blocked Execution | 
    
    
    metadata.product_event_type = /(execution|application) block/ nocase
    or security_result.threat_name = /application control/ nocase
    security_result.action = "BLOCK"
    
    $Host = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname)
    
    match:
      $Host
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users by Blocked Execution | 
    
    
    metadata.product_event_type = /(execution|application) block/ nocase
    or security_result.threat_name = /application control/ nocase
    security_result.action = "BLOCK"
    
    $User = strings.coalesce(target.user.userid, target.user.user_display_name, principal.user.userid, principal.user.user_display_name)
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Blocked Executions - Hourly | 
    
    
    metadata.product_event_type = /(execution|application) block/ nocase
    or security_result.threat_name = /application control/ nocase
    security_result.action = "BLOCK"
    
    $Hours = timestamp.get_timestamp(metadata.event_timestamp.seconds,"%F %H:00")
    
    match:
      $Hours
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Hours desc   
  
## Cloud Access Security Broker

This dashboard provides an overview of cloud application usage, security events, threats, and unauthorized access. It monitors top alerts, user activities and actions, and source and destination IP addresses to enhance policy enforcement and risk response.

Top 10 User AgentsTop 10 ApplicationsTop 10 CASB ActivitiesTop 10 Destination IPsTop 10 Destination HostnamesEvents by Action: Allow vs. BlockAuthentication Type DistributionTop 10 Vendor AlertsTop 10 Source HostnamesOS DistributionTop 10 UsersTop 10 Blocked UsersEvents Over Time by Log TypeTop 10 Source IPsTop 10 Event TypesTop 10 URLsTop 10 CASB Events Source Locations

Chart name | Query example  
---|---  
Top 10 User Agents | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $User_Agent = network.http.user_agent
    $Log_Type = metadata.log_type
    
    match:
      $User_Agent, $Log_Type
    
    outcome:
      $Count = count(network.http.user_agent)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Applications | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $Application = target.application
    $Log_Type = metadata.log_type
    $Application != ""
    match:
      $Application, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 CASB Activities | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $Activity = strings.coalesce(security_result.summary, metadata.description)
    $Log_Type = metadata.log_type
    $Activity != ""
    match:
      $Activity, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Destination IPs | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $IP_Address = target.ip
    $Log_Type = metadata.log_type
    $IP_Address != ""
    match:
      $IP_Address, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Destination Hostnames | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $Hostname = target.hostname
    $Log_Type = metadata.log_type
    
    match:
      $Hostname, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Events by Action: Allow vs. Block | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    security_result.action = "ALLOW"
    or security_result.action = "BLOCK"
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Action, $Date
    
    outcome:
      $Count = count(security_result.action)  
  
Authentication Type Distribution | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $Log_Type = metadata.log_type
    $Product_Event = metadata.product_event_type
    $Authentication = extensions.auth.type
    
    match:
      $Log_Type, $Product_Event, $Authentication
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Vendor Alerts | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $Rule_Name = security_result.rule_name
    $Log_Type = metadata.log_type
    $Rule_Name != ""
    match:
      $Rule_Name, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 CASB Activities | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $Activity = strings.coalesce(security_result.summary, metadata.description)
    $Log_Type = metadata.log_type
    
    match:
      $Activity, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Vendor Alerts | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $Rule_Name = security_result.rule_name
    $Log_Type = metadata.log_type
    
    match:
      $Rule_Name, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source Hostnames | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $Hostname = principal.hostname
    $Log_Type = metadata.log_type
    $Hostname != ""
    match:
      $Hostname, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
OS Distribution | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $Platform = principal.platform
    
    match:
      $Platform
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Users | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $User = principal.user.userid
    $Log_Type = metadata.log_type
    
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Destination Hostnames | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $Hostname = target.hostname
    $Log_Type = metadata.log_type
    $Hostname != ""
    match:
      $Hostname, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Blocked Users | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    security_result.action = "BLOCK"
    
    $User = principal.user.userid
    $Log_Type = metadata.log_type
    
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Events Over Time by Log Type | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 User Agents | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $User_Agent = network.http.user_agent
    $Log_Type = metadata.log_type
    
    match:
      $User_Agent, $Log_Type
    
    outcome:
      $Count = count(network.http.user_agent)
    
    order:
      $Count desc
    
    limit:
        10  
  
Events by Action: Allow vs. Block | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    security_result.action = "ALLOW"
    or security_result.action = "BLOCK"
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Action, $Date
    
    outcome:
      $Count = count(security_result.action)  
  
Top 10 Applications | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $Application = target.application
    $Log_Type = metadata.log_type
    
    match:
      $Application, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $IP_Address = principal.ip
    $Log_Type = metadata.log_type
    
    match:
      $IP_Address, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $IP_Address = principal.ip
    $Log_Type = metadata.log_type
    $IP_Address != ""
    match:
      $IP_Address, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Event Types | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $Event_Type = metadata.event_type
    $Log_Type = metadata.log_type
    
    match:
      $Event_Type, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
OS Distribution | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $Platform = principal.platform
    
    match:
      $Platform
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Event Types | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $Event_Type = metadata.event_type
    $Log_Type = metadata.log_type
    
    match:
      $Event_Type, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 URLs | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $URL = target.url
    $Log_Type = metadata.log_type
    $URL != ""
    match:
      $URL, $Log_Type
    
    outcome:
      $Count = count(target.url)
    
    order:
      $Count desc
    
    limit:
        10  
  
Events Over Time by Log Type | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 CASB Events Source Locations | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $Country = principal.location.country_or_region
    $Latitude = principal.location.region_latitude
    $Latitude != 0
    $Longitude = principal.location.region_longitude
    $Longitude != 0
    
    match:
      $Country, $Latitude, $Longitude
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 CASB Events Source Locations | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $Country = principal.location.country_or_region
    $Latitude = principal.location.region_latitude
    $Latitude != 0
    $Longitude = principal.location.region_longitude
    $Longitude != 0
    
    match:
      $Country, $Latitude, $Longitude
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Blocked Users | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    security_result.action = "BLOCK"
    
    $User = principal.user.userid
    $Log_Type = metadata.log_type
    $User != ""
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 URLs | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $URL = target.url
    $Log_Type = metadata.log_type
    
    match:
      $URL, $Log_Type
    
    outcome:
      $Count = count(target.url)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/
    
    $User = principal.user.userid
    $Log_Type = metadata.log_type
    $User != ""
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Authentication Type Distribution | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $Log_Type = metadata.log_type
    $Product_Event = metadata.product_event_type
    $Authentication = extensions.auth.type
    
    match:
      $Log_Type, $Product_Event, $Authentication
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Source Hostnames | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $Hostname = principal.hostname
    $Log_Type = metadata.log_type
    
    match:
      $Hostname, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Destination IPs | 
    
    
    metadata.log_type = /_CASB|SMARTSHEET|CISCO_SDWAN|NETSKOPE_CLIENT|ORACLE_NETSUITE|TAILSCALE/ nocase
    
    $IP_Address = target.ip
    $Log_Type = metadata.log_type
    
    match:
      $IP_Address, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
## Chrome Enterprise Premium Operations

This dashboard provides an overview of the Chrome Enterprise Premium integration with Google SecOps. This includes information about browsers and profiles under management.

Side-loaded Browser ExtensionsMost Installed Browser ExtensionsChrome EventsChrome Telemetry HealthTop 10 Managed Browsers by Chrome VersionTop 10 Managed Browsers by Operating SystemManagement OrganizationsMost Used Browser ExtensionsTop 10 Users with Most Installed Browser ExtensionsBrowser Extensions by PermissionLeast Installed Browser Extensions

Chart name | Query example  
---|---  
Side-loaded Browser Extensions | 
    
    
    metadata.log_type = "CHROME_MANAGEMENT"
    metadata.product_event_type = "browserExtensionInstallEvent"
    target.resource.attribute.labels["extension_source"] != "CHROME_WEBSTORE"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Source_Store = target.resource.attribute.labels["extension_source"]
    $Browser_Extension = target.resource.name
    $Browser_Extension_ID = target.resource.product_object_id
    
    match:
      $Date, $Source_Store, $Browser_Extension, $Browser_Extension_ID  
  
Most Installed Browser Extensions | 
    
    
    metadata.log_type = "CHROME_MANAGEMENT"
    metadata.product_event_type = "browserExtensionInstallEvent"
    target.resource.attribute.labels["extension_action"] = "INSTALL"
    
    $Browser_Extension = target.resource.name
    $Browser_Extension_ID = target.resource.product_object_id
    $Extension_Version = target.resource.attribute.labels["extension_version"]
    $Extension_Source = target.resource.attribute.labels["extension_source"]
    
    match:
      $Browser_Extension, $Browser_Extension_ID, $Extension_Version, $Extension_Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc   
  
Chrome Events | 
    
    
    metadata.log_type = "CHROME_MANAGEMENT"
    metadata.product_event_type != ""
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Event_Type = metadata.product_event_type
    
    match:
      $Date, $Event_Type
    
    outcome:
      $Count = count(metadata.id)  
  
Chrome Telemetry Health | 
    
    
    metadata.log_type = "CHROME_MANAGEMENT"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Managed Browsers by Chrome Version | 
    
    
    metadata.log_type = "CHROME_MANAGEMENT"
    network.http.parsed_user_agent.browser_version != ""
    principal.application != ""
    
    $Browser_Version = network.http.parsed_user_agent.browser_version
    $Application = principal.application
    
    match:
      $Browser_Version, $Application
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Managed Browsers by Operating System | 
    
    
    metadata.log_type = "CHROME_MANAGEMENT"
    network.http.parsed_user_agent.os != ""
    principal.application != ""
    
    $OS = network.http.parsed_user_agent.os
    $Application = principal.application
    
    match:
      $OS, $Application
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Management Organizations | 
    
    
    metadata.log_type = "CHROME_MANAGEMENT"
    target.domain.name != ""
    
    $Organization = target.domain.name
    
    match:
      $Organization
    
    outcome:
      $Count = count(principal.user.email_addresses)
    
    order:
      $Count desc   
  
Most Used Browser Extensions | 
    
    
    metadata.log_type = "CHROME_MANAGEMENT"
    metadata.product_event_type = "browserExtensionInstallEvent"
    target.resource.attribute.labels["extension_action"] = "INSTALL"
    or target.resource.attribute.labels["extension_action"] = "UPDATE"
    
    $Browser_Extension = target.resource.name
    $Browser_Extension_ID = target.resource.product_object_id
    $Extension_Version = target.resource.attribute.labels["extension_version"]
    $Extension_Source = target.resource.attribute.labels["extension_source"]
    
    match:
      $Browser_Extension, $Browser_Extension_ID, $Extension_Version, $Extension_Source
    
    outcome:
      $Total_Unique_Instances = count(metadata.id)
    
    order:
      $Total_Unique_Instances desc   
  
Top 10 Users with Most Installed Browser Extensions | 
    
    
    metadata.log_type = "CHROME_MANAGEMENT"
    metadata.product_event_type = "browserExtensionInstallEvent"
    
    $User = principal.user.email_addresses
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Browser Extensions by Permission | 
    
    
    metadata.log_type = "CHROME_MANAGEMENT"
    metadata.product_event_type = "extensionTelemetryEvent"
    target.resource.name = "COOKIES_GET_ALL_INFO"
    or target.resource.name = "COOKIES_GET_INFO"
    or target.resource.name = "TABS_API_INFO"
    
    $Browser_Extension = target.resource_ancestors.name
    $Browser_Extension_ID = target.resource_ancestors.product_object_id
    $Extension_Version = target.resource_ancestors.attribute.labels["extension_version"]
    $Extension_Source = target.resource_ancestors.attribute.labels["extension_source"]
    $Severity = security_result.severity
    
    match:
      $Browser_Extension, $Browser_Extension_ID, $Extension_Version, $Extension_Source, $Severity
    
    outcome:
      $Permissions = array_distinct(target.resource.name)
      $Count = count(metadata.id)
    
    order:
      $Browser_Extension asc   
  
Least Installed Browser Extensions | 
    
    
    metadata.log_type = "CHROME_MANAGEMENT"
    metadata.product_event_type = "browserExtensionInstallEvent"
    target.resource.attribute.labels["extension_action"] = "INSTALL"
    
    $Browser_Extension = target.resource.name
    $Browser_Extension_ID = target.resource.product_object_id
    $Extension_Version = target.resource.attribute.labels["extension_version"]
    $Extension_Source = target.resource.attribute.labels["extension_source"]
    
    match:
      $Browser_Extension, $Browser_Extension_ID, $Extension_Version, $Extension_Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count asc  
  
## Chrome Enterprise Premium Security

This dashboard provides real-time insights into Chrome-related security events such as sensitive data transfers, access to high-risk domains, data protection events, malware and phishing attempts, and password security issues. It enables security teams to monitor, investigate, and respond to Chrome-based threats.

Chrome DLP : Data InsightsChrome DLP : Total Sensitive Web TransferChrome DLP : Total Sensitive File PrintsChrome DLP : Total Sensitive File UploadsPassword Reuse EventsChrome High-Risk DomainsPassword Breach EventsMalware EventsUnsafe Site VisitsPhishing EventsChrome DLP : Total Sensitive Content TransferChrome DLP : Total Sensitive File DownloadsChrome DLP: Users with Sensitive Content DetectionsChrome DLP : Sensitive Content Domains

Chart name | Query example  
---|---  
Chrome DLP : Data Insights | 
    
    
    metadata.product_event_type = /sensitiveDataEvent|contentTransferEvent/ nocase
    security_result.summary = /CONTENT_MATCHED_SENSITIVE_DATA_TYPES/ nocase or extracted.fields["reason"] = /CONTENT_MATCHED_SENSITIVE_DATA_TYPES/ nocase
    
    $Sensitive_Data_Type = extracted.fields["matched_detectors[0].detector_id"]
    $Trigger_Type = security_result.about.labels.value
    
    match:
      $Sensitive_Data_Type, $Trigger_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Chrome DLP : Total Sensitive Web Transfer | 
    
    
    metadata.product_event_type = /Sensitive data transfer|SENSITIVE_DATA_TRANSFER|sensitiveDataEvent|sensitiveDataTransferEvent/ nocase
    security_result.about.labels.value = /web_content_upload/ nocase
    
    outcome:
      $Sensitive_Web_Transfer = count(metadata.id)
      
  
Chrome DLP : Total Sensitive File Prints | 
    
    
    metadata.product_event_type = /Sensitive data transfer|SENSITIVE_DATA_TRANSFER|sensitiveDataEvent|sensitiveDataTransferEvent/ nocase
    security_result.about.labels.value = /print/ nocase
    
    outcome:
      $Sensitive_File_Print = count(metadata.id)
      
  
Chrome DLP : Total Sensitive File Uploads | 
    
    
    metadata.product_event_type = /Sensitive data transfer|SENSITIVE_DATA_TRANSFER|sensitiveDataEvent|sensitiveDataTransferEvent/ nocase
    security_result.about.labels.value = /file_upload/ nocase
    
    outcome:
      $Sensitive_File_Upload = count(metadata.id)
      
  
Password Reuse Events | 
    
    
    metadata.product_event_type = /PASSWORD_REUSE|passwordReuseEvent/ nocase
    
    $Action = security_result.action_details
    $Severity = security_result.severity
    $User = strings.coalesce(principal.user.userid , principal.user.user_display_name, principal.user.email_addresses)
    $Summary = strings.coalesce(security_result.summary, security_result.description, metadata.product_event_type, security_result.category_details)
    $URL = target.url
    
    match:
      $User, $Summary, $Severity, $Action, $URL
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
Chrome High-Risk Domains | 
    
    
    extracted.fields["url_info.risk_infos[0].risk_level"] = "HIGH"
    target.url != ""
    
    $URL = target.url
    $Category = security_result.category
    $Action = security_result.action_details
    $Severity = principal.security_result.severity
    $Risk_Level = extracted.fields["url_info.risk_infos[0].risk_level"]
    $Threat_Type = extracted.fields["url_info.risk_infos[0].threat_type"]
    $Domain = re.capture(target.url, `^(?:https?:\/\/)?(?:www\.)?([^\/:]+)`)
    
    match:
      $URL, $Domain, $Category, $Severity, $Risk_Level, $Threat_Type, $Action
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Password Breach Events | 
    
    
    metadata.product_event_type = /passwordBreachEvent/ nocase
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Summary = strings.coalesce(security_result.summary, security_result.description, metadata.product_event_type, security_result.category_details)
    $URL = target.url
    $Action = security_result.action_details
    $Severity = security_result.severity
    
    match:
      $User, $Summary, $URL, $Severity, $Action
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Malware Events | 
    
    
    metadata.product_event_type = /dangerousDownloadEvent|contentTransferEvent/ nocase
    (extracted.fields["content_risk[0].risk_level"] = "HIGH" or extracted.fields["content_risk_level"] = "HIGH")
    (extracted.fields["content_risk[0].threat_type"] = "MALWARE")
    
    $File_Hash = target.file.sha256
    $File_Path = target.file.full_path
    $Category = security_result.category
    $Severity = security_result.severity
    $Risk_Level = strings.coalesce(extracted.fields["content_risk[0].risk_level"],extracted.fields["content_risk_level"])
    
    match:
      $File_Path, $File_Hash, $Category, $Severity, $Risk_Level
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Summary = array_distinct(security_result.summary)
      $Action = array_distinct(security_result.action_details)
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Unsafe Site Visits | 
    
    
    metadata.product_event_type = /badNavigationEvent/ nocase
    (extracted.fields["url_info.risk_infos[0].risk_level"] = "HIGH" OR extracted.fields["url_info.risk_level"] = "HIGH")
    //(extracted.fields["content_risk[0].threat_type"] = "MALWARE" or extracted.fields["tab_url_info.threat_type"] = "MALWARE")
    
    $URL = target.url
    $Category = security_result.category
    $Threat_Type = extracted.fields["url_info.risk_infos[0].threat_type"]
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Risk_Level = strings.coalesce(extracted.fields["url_info.risk_infos[0].risk_level"], extracted.fields["url_info.risk_level"])
    
    match:
      $User, $URL, $Category, $Threat_Type, $Risk_Level
    
    outcome:
      $Action = array_distinct(security_result.action_details)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
Phishing Events | 
    
    
    extracted.fields["url_info.risk_infos[0].threat_type"] = "SOCIAL_ENGINEERING"
    
    $URL = target.url
    $Category = security_result.category
    $Action = security_result.action_details
    $Severity = principal.security_result.severity
    $Risk_Level = extracted.fields["url_info.risk_infos[0].risk_level"]
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    match:
      $User, $URL, $Category, $Severity, $Risk_Level, $Action
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Chrome DLP : Total Sensitive Content Transfer | 
    
    
    metadata.product_event_type = /Sensitive data transfer|SENSITIVE_DATA_TRANSFER|sensitiveDataEvent|sensitiveDataTransferEvent/ nocase
    
    outcome:
      $Total_Sensitive_Content_Transfer = count(metadata.id)
      
  
Chrome DLP : Total Sensitive File Downloads | 
    
    
    metadata.product_event_type = /Sensitive data transfer|SENSITIVE_DATA_TRANSFER|sensitiveDataEvent|sensitiveDataTransferEvent/ nocase
    security_result.about.labels.value = /file_download/ nocase
    
    outcome:
      $Sensitive_File_Download = count(metadata.id)
      
  
Chrome DLP: Users with Sensitive Content Detections | 
    
    
    metadata.product_event_type = /sensitiveDataEvent/ nocase or security_result.summary = /CONTENT_MATCHED_SENSITIVE_DATA_TYPES/ nocase
    
    $Device_IP = extracted.fields["remote_ip"]
    $Device_ID = extracted.fields["device_id"]
    $Action = security_result.action_details
    $Severity = principal.security_result.severity
    $Trigger_Type = security_result.about.labels.value
    $Sensitive_Data_Type = extracted.fields["matched_detectors[0].display_name"]
    $Device_User = strings.coalesce(extracted.fields["device_user"], extracted.fields["profile_user"])
    
    match:
      $Device_User, $Device_IP, $Device_ID, $Trigger_Type, $Sensitive_Data_Type, $Action, $Severity
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Chrome DLP : Sensitive Content Domains | 
    
    
    metadata.product_event_type = /Sensitive data transfer|SENSITIVE_DATA_TRANSFER|sensitiveDataEvent|sensitiveDataTransferEvent/ nocase
    or security_result.summary = /CONTENT_MATCHED_SENSITIVE_DATA_TYPES/ nocase
    target.url != ""
    
    $Domain = target.url
    $Action = security_result.action_details
    $Severity = security_result.severity
    $Sensitive_Data_Type = extracted.fields["matched_detectors[0].display_name"]
    
    match:
      $Domain, $Action, $Severity, $Sensitive_Data_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
## CIS Controls Compliance Overview

This dashboard strengthens security governance by offering clear visibility into adherence with CIS Critical Security Controls. It tracks essential compliance metrics such as asset inventory accuracy, vulnerability remediation progress, backup reliability, access control enforcement, and incident response preparedness.

Inactive Users (More Than 7 Days)Recent Blocked Application ExecutionsSSO Authentication SummaryIDS / IPS Events DistributionPrivileged Account MFA Events Over TimeTop 10 Systems with Critical/High VulnerabilitiesRecent Phishing EventsWeak Encryption Algorithms Over TimePermission Changes Over TimeRecent User Account CreationsUser Account Creations Over TimeVPN Connection Success v/s Failure Trends Over TimeMalware Detections Over TimeHigh/Critical Vulnerability by AgeTop 10 Service Accounts by LoginsMalware File DetailsNetwork-Based Malicious ActivitiesPrivileged Account Activities & ModificationsLogin Events Over Time by ActionData Security Events DistributionData Deletion and Purge EventsVulnerability Scans Over TimePhishing Events Over TimeRecent Backup EventsTop 10 Email Threats by SeverityBackup Events Over Time Total Devices Over TimeTop 10 Blocked Application ExecutionsBlocked MFA Attempts for Privileged Accounts

Chart name | Query example  
---|---  
Inactive Users (More Than 7 Days) | 
    
    
    stage inactive_users {
        (metadata.event_type = "USER_UNCATEGORIZED"
        or metadata.event_type = "USER_LOGIN"
        or metadata.event_type = "USER_LOGOUT"
        or metadata.event_type = "USER_CREATION"
        or metadata.event_type = "USER_CHANGE_PASSWORD"
        or metadata.event_type = "USER_CHANGE_PERMISSIONS"
        or metadata.event_type = "USER_BADGE_IN"
        or metadata.event_type = "USER_DELETION"
        or metadata.event_type = "USER_RESOURCE_CREATION"
        or metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT"
        or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
        or metadata.event_type = "USER_COMMUNICATION"
        or metadata.event_type = "USER_RESOURCE_ACCESS"
        or metadata.event_type = "USER_RESOURCE_DELETION")
        principal.user.last_login_time.seconds > 0
    
      $Event_Type = metadata.event_type
      $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
      $User != ""
      $Log_Type = metadata.log_type
    
        match:
          $User, $Event_Type, $Log_Type
    
            outcome:
               $Logtime = max(metadata.event_timestamp.seconds)
               $Lastime = max(principal.user.last_login_time.seconds)
              $Time_Difference = cast.as_int(max(metadata.event_timestamp.seconds - principal.user.last_login_time.seconds)/86400)
    
                 condition:
                  $Time_Difference > 7
    
    }
    $User = $inactive_users.User
    $Event_Type = $inactive_users.Event_Type
    $Log_Type = $inactive_users.Log_Type
    
    match:
      $User, $Event_Type, $Log_Type
    
    outcome:
      $Last_Login = timestamp.get_timestamp(max($inactive_users.Lastime))
      $Latest_Login = timestamp.get_timestamp(max($inactive_users.Logtime))
      $Time_Difference = max($inactive_users.Time_Difference)
    
    order:
      $Time_Difference desc  
  
Recent Blocked Application Executions | 
    
    
    (metadata.product_event_type = /(execution|application) block/ nocase or security_result.summary = /(execution|application) block/ or metadata.description = /(execution|application) block/ nocase or security_result.threat_name = /application control/ nocase)
    (security_result.action = "BLOCK" or security_result.action_details = /block/ nocase or (target.resource.attribute.labels.key = "categoryBehavior" and target.resource.attribute.labels.value = /blocked/ nocase))
    
    $Application = strings.coalesce(about.file.full_path, target.process.file.full_path, additional.fields["fname"], principal.application, target.application)
    $Description = strings.coalesce(target.resource.attribute.labels["categoryTupleDescription"], security_result.summary, metadata.product_event_type, security_result.description, metadata.description, security_result.action_details)
    $Log_Type = metadata.log_type
    $Severity = security_result.severity
    
    match:
      $Application, $Description, $Severity, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
    
      
  
SSO Authentication Summary | 
    
    
    extensions.auth.type = "SSO"
    (metadata.event_type = "USER_LOGIN" or metadata.event_type = "USER_LOGOUT")
    
    $Description = strings.coalesce(security_result.summary, metadata.description, security_result.description, metadata.product_event_type)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses,target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Source_Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Source_IP = strings.coalesce(principal.ip,principal.asset.ip)
    $Action = security_result.action
    $Severity = security_result.severity
    
    match:
      $User, $Description, $Source_Hostname, $Source_IP, $Action, $Severity
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Severity desc, $Date desc  
  
IDS / IPS Events Distribution | 
    
    
    metadata.log_type = /_IDS|_IPS|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    (metadata.event_type = "SCAN_UNCATEGORIZED"
    or metadata.event_type = "SCAN_NETWORK"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP")
    
    $Category = security_result.category
    
    match:
      $Category
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Privileged Account MFA Events Over Time | 
    
    
    (re.regex(metadata.product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex(additional.fields["AuthenticationRequirement"], `multiFactorAuthentication`) nocase or re.regex(security_result.detection_fields.value, `MFA`) nocase or re.regex(metadata.product_event_type, `mfa(?:\S)?auth|auth(?:.*)?mfa`) nocase)
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name,target.user.email_addresses)
    $User = /admin|root|administrator|security|support|default/ nocase //It will be updated as per the client's environment.
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Systems with Critical/High Vulnerabilities | 
    
    
    metadata.log_type = /ARMIS_VULNERABILITIES|FINGERPRINT_JS|NUCLEUS_VULNERABILITY|QUALYS_ASSET_CONTEXT|QUALYS_SCAN|QUALYS_VIRTUAL_SCANNER|QUALYS_VM|RAPID7_INSIGHT|RAPID7_NEXPOSE|SNYK_SDLC|SPUR_FEEDS|STACKHAWK|SUBLIMESECURITY|SYMANTEC_SA|TENABLE_IO|TENABLE_OT|TENABLE_SC|UPGUARD|URLSCAN_IO/ nocase
    
    (principal.asset.vulnerabilities.severity = "HIGH" or  extensions.vulns.vulnerabilities.severity = "HIGH" or security_result.severity = "HIGH"
    or target.asset.vulnerabilities.severity = "HIGH") or (principal.asset.vulnerabilities.severity = "CRITICAL" or  extensions.vulns.vulnerabilities.severity = "CRITICAL"
    or security_result.severity = "CRITICAL" or target.asset.vulnerabilities.severity = "CRITICAL")
    
    $Severity =
        if (principal.asset.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            principal.asset.vulnerabilities.severity,
        if (target.asset.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            target.asset.vulnerabilities.severity,
        if (extensions.vulns.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            extensions.vulns.vulnerabilities.severity,
        "UNKNOWN_SEVERITY")))
    
    $Vulnerability = strings.coalesce(
      if(principal.asset.vulnerabilities.name != "" and principal.asset.vulnerabilities.description != "",
        strings.concat(principal.asset.vulnerabilities.name, " : ", principal.asset.vulnerabilities.description),
        strings.coalesce(principal.asset.vulnerabilities.name, principal.asset.vulnerabilities.description)),
      if(additional.fields["ScanReference"] != "" and metadata.description != "",
        strings.concat(additional.fields["ScanReference"], " : ", metadata.description),
        strings.coalesce(additional.fields["ScanReference"], metadata.description)),
      if(extensions.vulns.vulnerabilities.vendor_vulnerability_id != "" and extensions.vulns.vulnerabilities.description != "",
        strings.concat(extensions.vulns.vulnerabilities.vendor_vulnerability_id, " : ", extensions.vulns.vulnerabilities.description),
        strings.coalesce(extensions.vulns.vulnerabilities.vendor_vulnerability_id, extensions.vulns.vulnerabilities.description)
      )
    )
    ($Vulnerability != " : " and $Vulnerability != "")
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname, target.hostname, target.asset.hostname)
    $Log_Type = metadata.log_type
    
    match:
      $Hostname, $Vulnerability, $Severity, $Log_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(strings.coalesce(extensions.vulns.vulnerabilities.name, extensions.vulns.vulnerabilities.description, extensions.vulns.vulnerabilities.vendor_vulnerability_id,
                                        principal.asset.vulnerabilities.name, target.asset.vulnerabilities.name, additional.fields["ScanReference"]))
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Phishing Events | 
    
    
    metadata.log_type = /MAIL|ABNORMAL_SECURITY|AREA1|COFENSE_TRIAGE|FIREEYE|FORCEPOINT|FORTINET|KNOWBE4_PHISHER|MICROSOFT_GRAPH_ALERT|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|PHISHLABS|PROOFPOINT|SYMANTEC_VIP|VOLTAGE|WORKSPACE_ALERTS/ nocase
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`)nocase)
    security_result.threat_name != "NOT_PHISHING"
    
    $Security_Event_Type = metadata.product_event_type
    $Summary = strings.coalesce(security_result.summary, metadata.description, security_result.description)
    $Sender = strings.coalesce(network.email.from, principal.user.email_addresses)
    $Subject = network.email.subject
    $File_Path = strings.coalesce(target.file.full_path, about.file.full_path, target.file.names)
    $File_Type = strings.coalesce(about.file.mime_type, target.file.mime_type)
    
    match:
      $Security_Event_Type, $Sender, $Subject, $File_Path, $File_Type, $Summary
    
    outcome:
      $Count = count(metadata.id)
      $Receiver_Count = count_distinct(strings.coalesce(network.email.to, network.email.reply_to, target.user.email_addresses))
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
Weak Encryption Algorithms Over Time | 
    
    
    (((target.resource.attribute.labels.key  = "keyProperties_type" or target.resource.attribute.labels.key  = "requestParameters.keySpec" or target.resource.attribute.labels.key = /key/ nocase) and target.resource.attribute.labels.value  = /^(RSA-)|DES|RC4|MD5|SHA1|SHA-1/) or network.tls.cipher = /^(RSA-)|DES|RC4|MD5|SHA1|SHA-1/)
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Permission Changes Over Time | 
    
    
    (metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" or metadata.event_type = "USER_CHANGE_PERMISSIONS" or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS")
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc
      
  
Recent User Account Creations | 
    
    
    metadata.event_type = "USER_CREATION"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Source_IP = strings.coalesce(principal.ip,principal.asset.ip)
    $Source_Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, principal.mac, principal.asset.mac, extracted.fields["access_device.hostname"],
    if(target.resource.attribute.labels.key = "Private DnsName",target.resource.attribute.labels.value, ""),
    principal.resource.product_object_id, target.resource.product_object_id,
    if(security_result.detection_fields.key = "actor_2",security_result.detection_fields.value, "")
    )
    $Initiator = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $User_Created = strings.coalesce(target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    match:
      $Log_Type, $Source_IP, $Source_Hostname, $Initiator, $User_Created
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T ")
    
    order:
      $Date desc  
  
User Account Creations Over Time | 
    
    
    metadata.event_type = "USER_CREATION"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
VPN Connection Success v/s Failure Trends Over Time | 
    
    
    metadata.log_type = /VPN|ZSCALER_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/ nocase
    
    $Action = if ((strings.coalesce(security_result.summary, metadata.product_event_type, extracted.fields["connection-attempt-status"]) = /Success|Authenticated/ nocase), "SUCCESS", "FAIL")
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
          
  
Malware Detections Over Time | 
    
    
    (metadata.product_event_type = /malware/ nocase or security_result.summary = /malware/ nocase or security_result.category_details = /malware/ nocase or metadata.description = /malware/ nocase or security_result.threat_name = /malware/ nocase or security_result.rule_name = /malware/ nocase or security_result.category = "SOFTWARE_MALICIOUS")
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Action = security_result.action
    
    match :
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc
    
      
  
High/Critical Vulnerability by Age | 
    
    
    (principal.asset.vulnerabilities.severity = "CRITICAL" or  extensions.vulns.vulnerabilities.severity = "CRITICAL"
    or security_result.severity = "CRITICAL" or target.asset.vulnerabilities.severity = "CRITICAL") OR
    (principal.asset.vulnerabilities.severity = "HIGH" or  extensions.vulns.vulnerabilities.severity = "HIGH"
    or security_result.severity = "HIGH" or target.asset.vulnerabilities.severity = "HIGH")
    
    (timestamp.as_unix_seconds(additional.fields["first_found"]) > 0 or extensions.vulns.vulnerabilities.first_found.seconds > 0)
    
    $Severity =
        if (principal.asset.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            principal.asset.vulnerabilities.severity,
        if (target.asset.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            target.asset.vulnerabilities.severity,
        if (extensions.vulns.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            extensions.vulns.vulnerabilities.severity,
        "UNKNOWN_SEVERITY")))
    
    $Vulnerability = strings.coalesce(
      if(principal.asset.vulnerabilities.name != "" and principal.asset.vulnerabilities.description != "",
        strings.concat(principal.asset.vulnerabilities.name, " : ", principal.asset.vulnerabilities.description),
        strings.coalesce(principal.asset.vulnerabilities.name, principal.asset.vulnerabilities.description)),
      if(additional.fields["ScanReference"] != "" and metadata.description != "",
        strings.concat(additional.fields["ScanReference"], " : ", metadata.description),
        strings.coalesce(additional.fields["ScanReference"], metadata.description)),
      if(extensions.vulns.vulnerabilities.vendor_vulnerability_id != "" and extensions.vulns.vulnerabilities.description != "",
        strings.concat(extensions.vulns.vulnerabilities.vendor_vulnerability_id, " : ", extensions.vulns.vulnerabilities.description),
        strings.coalesce(extensions.vulns.vulnerabilities.vendor_vulnerability_id, extensions.vulns.vulnerabilities.description)
      )
    )
    ($Vulnerability != " : " and $Vulnerability != "")
    $Log_Type = metadata.log_type
    
    match:
      $Vulnerability, $Log_Type, $Severity
    
    outcome:
      $Age_Max = max(cast.as_int((metadata.event_timestamp.seconds - if(timestamp.as_unix_seconds(additional.fields["first_found"]) > 0,
                      timestamp.as_unix_seconds(additional.fields["first_found"]), if(extensions.vulns.vulnerabilities.first_found.seconds > 0,
                      extensions.vulns.vulnerabilities.first_found.seconds, metadata.event_timestamp.seconds))) / 86400))
      $Count = count(strings.coalesce(extensions.vulns.vulnerabilities.name, extensions.vulns.vulnerabilities.description, extensions.vulns.vulnerabilities.vendor_vulnerability_id,
                                              principal.asset.vulnerabilities.name, target.asset.vulnerabilities.name, additional.fields["ScanReference"]))
    
    order:
      $Age_Max desc
      
  
Top 10 Service Accounts by Logins | 
    
    
    metadata.event_type = "USER_LOGIN"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, principal.user.user_display_name, principal.user.email_addresses,target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid, target.user.user_display_name, target.user.email_addresses) =  /(?i)service.*(?:account|^principal$)/  nocase
    
    $Service_Account = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Service_Account != ""
    $Action = security_result.action
    
    match:
      $Service_Account, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Malware File Details | 
    
    
    (metadata.product_event_type = /malware/ nocase or security_result.summary = /malware/ nocase or security_result.category_details = /malware/ nocase or metadata.description = /malware/ nocase or security_result.threat_name = /malware/ nocase or security_result.rule_name = /malware/ nocase or security_result.category = "SOFTWARE_MALICIOUS")
    
    $Source_User = strings.coalesce(principal.user.user_display_name, principal.user.userid, principal.user.email_addresses)
    $File_Name = strings.coalesce(target.file.full_path, about.file.full_path)
    $File_Name != ""
    $File_Type = strings.coalesce(target.file.mime_type, about.file.mime_type)
    $Severity = security_result.severity
    $Action = security_result.action
    
    match :
      $File_Name, $File_Type, $Source_User, $Severity, $Action
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
    
      
  
Network-Based Malicious Activities | 
    
    
    (metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP")
    (security_result.category = "NETWORK_DENIAL_OF_SERVICE" or security_result.category = "NETWORK_MALICIOUS" or security_result.category = "NETWORK_SUSPICIOUS" or
    security_result.category = "SOFTWARE_MALICIOUS" or security_result.category = "SOFTWARE_SUSPICIOUS" or security_result.category = "NETWORK_RECON")
    
    $Log_Type = metadata.log_type
    $Category = security_result.category
    $Summary = strings.coalesce(security_result.description, security_result.summary, metadata.description, security_result.rule_name, metadata.product_event_type)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname, principal.mac, principal.asset.mac, target.hostname, target.asset.hostname, target.mac, target.asset.mac,
    target.resource.product_object_id, principal.group.product_object_id, principal.ip, principal.asset.ip, target.ip, target.asset.ip)
    $Action = security_result.action
    
    match:
      $Summary, $Category, $Hostname, $Log_Type, $Action
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
Privileged Account Activities & Modifications | 
    
    
    metadata.event_type = "GROUP_CREATION" or metadata.event_type = "GROUP_MODIFICATION" or metadata.event_type = "GROUP_DELETION" or metadata.event_type = "USER_LOGIN" or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid,target.user.user_display_name,target.user.email_addresses)
    ($User = /admin|root|svc|adm|privilege/ nocase or principal.user.attribute.roles.type = "SERVICE_ACCOUNT" or principal.user.attribute.roles.type = "ADMINISTRATOR" or principal.user.account_type = "DOMAIN_ACCOUNT_TYPE" or principal.user.account_type = "SERVICE_ACCOUNT_TYPE")
    $Event_Type = metadata.event_type
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip, principal.hostname, principal.asset.hostname, principal.mac)
    $Target_Resource = strings.coalesce(target.resource.name, target.file.full_path, target.resource.product_object_id, target.group.product_object_id, target.user.group_identifiers, target.group.group_display_name)
    $Target_Resourcetype = target.resource.resource_type
    $Action = security_result.action
    $Security_Event_Type = metadata.product_event_type
    $Summary = strings.coalesce(additional.fields["Message"], security_result.summary, security_result.description, metadata.description)
    
    match:
       $Event_Type, $User,$Source_IP, $Target_Resource, $Action, $Security_Event_Type, $Summary
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %H:%M:%S")
    
    order:
       $Count desc
    
      
  
Login Events Over Time by Action | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Data Security Events Distribution | 
    
    
    metadata.log_type = /ARUBA_CENTRAL|CLOUDFLARE_WARP|DELL_CYBERSENSE|FORGEROCK_OPENIDM|IMPERVA_DRA|IMPERVA_SECURESPHERE|IBM_OPENPAGES|INTEL471_WATCHER_ALERTS|METABASE|OKERA_DAP|OPENCANARY|RUBRIK_POLARIS|SENTRY|TINES|TINTRI|VARONIS/ nocase
    
    $Event_Type = metadata.event_type
    
    match:
      $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
       
  
Data Deletion and Purge Events | 
    
    
    (metadata.event_type = "FILE_DELETION"
    or metadata.event_type = "RESOURCE_DELETION"
    or metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE"
    or metadata.event_type = "REGISTRY_DELETION"
    or metadata.event_type = "SETTING_DELETION"
    or metadata.event_type = "USER_RESOURCE_DELETION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.event_type = "SERVICE_DELETION"
    or metadata.event_type = "SCHEDULED_TASK_DELETION"
    or strings.coalesce(metadata.product_event_type, security_result.summary, security_result.description, security_result.action_details) = /delet(?:e|ed|ion|ing)|purge/ nocase)
    security_result.action = "ALLOW"
    
    $Description = strings.coalesce(security_result.summary, security_result.description, metadata.description, security_result.action_details)
    $Product_Event_Type = metadata.product_event_type
    $Event_Type = metadata.event_type
    $Log_Type = metadata.log_type
    $Target_Resource = strings.coalesce(target.resource.name, target.file.full_path, target.resource.product_object_id, target.group.product_object_id, target.user.group_identifiers)
    $User = strings.coalesce(principal.user.user_display_name, principal.user.userid, principal.user.email_addresses, target.user.userid,target.user.user_display_name,target.user.email_addresses)
    
    match:
      $User, $Log_Type, $Description, $Product_Event_Type, $Event_Type, $Target_Resource
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Date desc, $Count desc  
  
Vulnerability Scans Over Time | 
    
    
    metadata.log_type = /ARMIS_VULNERABILITIES|FINGERPRINT_JS|NUCLEUS_VULNERABILITY|QUALYS_ASSET_CONTEXT|QUALYS_SCAN|QUALYS_VIRTUAL_SCANNER|QUALYS_VM|RAPID7_INSIGHT|RAPID7_NEXPOSE|SNYK_SDLC|SPUR_FEEDS|STACKHAWK|SUBLIMESECURITY|SYMANTEC_SA|TENABLE_IO|TENABLE_OT|TENABLE_SC|UPGUARD|URLSCAN_IO/ nocase
    
    (metadata.event_type = "SCAN_VULN_HOST" or additional.fields["Type"] = "Scan" or security_result.detection_fields.key = /scan/ nocase or security_result.detection_fields.value = /scan/ nocase)
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Phishing Events Over Time | 
    
    
    metadata.log_type = /MAIL|ABNORMAL_SECURITY|AREA1|COFENSE_TRIAGE|FIREEYE|FORCEPOINT|FORTINET|KNOWBE4_PHISHER|MICROSOFT_GRAPH_ALERT|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|PHISHLABS|PROOFPOINT|SYMANTEC_VIP|VOLTAGE|WORKSPACE_ALERTS/ nocase
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`)nocase)
    security_result.threat_name != "NOT_PHISHING"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Severity = security_result.severity
    
    match:
      $Date, $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Recent Backup Events | 
    
    
    (metadata.log_type = /COHESITY|DRUVA_BACKUP|VEEAM|VERITAS_NETBACKUP/ nocase or metadata.log_type = "RUBRIK")
    
    $Description = strings.coalesce(metadata.description, security_result.description, security_result.summary)
    
    $Log_Type = metadata.log_type
    $Event_Type = metadata.event_type
    $Security_Event_Type = metadata.product_event_type
    $Action = security_result.action
    
    match:
      $Description, $Security_Event_Type, $Event_Type, $Action, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T ")
    
    order:
      $Count desc  
  
Top 10 Email Threats by Severity | 
    
    
    metadata.log_type = /MAIL|ABNORMAL_SECURITY|AREA1|COFENSE_TRIAGE|FIREEYE|FORCEPOINT|FORTINET|KNOWBE4_PHISHER|MICROSOFT_GRAPH_ALERT|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|PHISHLABS|PROOFPOINT|SYMANTEC_VIP|VOLTAGE|WORKSPACE_ALERTS/ nocase
    security_result.category = "MAIL_SPAM"
    or security_result.category = "MAIL_SPOOFING"
    or security_result.category = "SOFTWARE_MALICIOUS"
    or (security_result.category = "MAIL_PHISHING" and security_result.threat_name!= "NOT_PHISHING")
    or strings.coalesce(security_result.threat_name, security_result.category_details) = /Phish|Mail/ nocase
    
    $Severity = security_result.severity
    $Threat_Name = strings.coalesce(security_result.threat_name, security_result.category_details)
    $Threat_Name != ""
    
    match:
      $Threat_Name, $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Backup Events Over Time  | 
    
    
    (metadata.log_type = /COHESITY|DRUVA_BACKUP|VEEAM|VERITAS_NETBACKUP/ nocase or metadata.log_type = "RUBRIK")
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Total Devices Over Time | 
    
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count_distinct(strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname))
    
    order:
      $Date asc
    
       
  
Top 10 Blocked Application Executions | 
    
    
    (metadata.product_event_type = /(execution|application) block/ nocase or security_result.summary = /(execution|application) block/ or metadata.description = /(execution|application) block/ nocase or security_result.threat_name = /application control/ nocase)
    (security_result.action = "BLOCK" or security_result.action_details = /block/ nocase or (target.resource.attribute.labels.key = "categoryBehavior" and target.resource.attribute.labels.value = /blocked/ nocase))
    
    $Application = strings.coalesce(about.file.full_path, target.process.file.full_path, additional.fields["fname"], principal.application, target.application)
    $Description = strings.coalesce(target.resource.attribute.labels["categoryTupleDescription"], security_result.summary, metadata.product_event_type, security_result.description, metadata.description, security_result.action_details)
    
    match:
      $Application, $Description, metadata.log_type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Blocked MFA Attempts for Privileged Accounts | 
    
    
    (re.regex(metadata.product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex(additional.fields["AuthenticationRequirement"], `multiFactorAuthentication`) nocase or re.regex(security_result.detection_fields.value, `MFA`) nocase or re.regex(metadata.product_event_type, `mfa(?:\S)?auth|auth(?:.*)?mfa`) nocase)
    security_result.action = "BLOCK"
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name,target.user.email_addresses)
    $User = /admin|root|administrator|security|support|default/ nocase //It will be updated as per the client's environment.
    $Reason = strings.coalesce(security_result.summary, metadata.product_event_type)
    $Location = strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region)
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Log_Type = metadata.log_type
    $Severity = security_result.severity
    
    match:
      $Reason, $User, $Source_IP, $Location, $Severity, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
## Cloud Key Management Overview

This dashboard offers a detailed view of key management activities within your organization's cloud infrastructure. The dashboard monitors the status of Keys, Certificates, and Secrets across their lifecycle-created, deleted, enabled, rotated, and disabled-enabling the detection of anomalies or unauthorized activities.

Objects Disabled Over TimeTotal Event Count by Log TypeTop 10 Users Creating ObjectsObjects Deleted Over TimeObjects Created Over timeTop 10 Source IPs Enabling ObjectsTop 10 Users Rotating ObjectsObjects Rotated Over TimeTop 10 Source IPs Rotating ObjectsTop 10 Users Deleting objectsTop 10 Objects RotatedTop 10 Objects DisabledTop 10 Blocked UsersTop 10 Users Enabling ObjectsRecent Objects Created (Last 24 Hours)Top 10 Objects EnabledTop 10 User AgentsTop 10 Source IPs Creating ObjectsTop 10 Object LocationsObjects Enabled Over TimeTop 10 Blocked Source IPsObjects Created by GeolocationTop 10 Users Disabling ObjectsTop 10 Source IPs Disabling ObjectsRecent Objects Deleted(Last 24 Hours)Top 10 Source IPs Deleting Objects

Chart name | Query example  
---|---  
Objects Disabled Over Time | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Disable/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /UpdateCryptoKeyVersion|Disable/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase  and
    target.resource.attribute.labels.value = /DISABLED/ nocase and security_result.action = "ALLOW"))
    
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
       $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Total Event Count by Log Type | 
    
    
    (metadata.log_type = /AZURE_KEYVAULT_AUDIT|GCP_CLOUDAUDIT/ nocase or target.application = "kms.amazonaws.com")
    
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
Top 10 Users Creating Objects | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Create/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /Create/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase and
    metadata.product_event_type != /version/ nocase  and security_result.action = "ALLOW"))
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, principal.user.group_identifiers)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
          
  
Objects Deleted Over Time | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Delete/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /Delete|Destroy/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase
    and security_result.action = "ALLOW"))
    
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
       $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Objects Created Over time | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and ((additional.fields["resultType"] = /Allow|Success/ nocase) or (security_result.action = "ALLOW"))) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Create/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /Create/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase and
    metadata.product_event_type != /version/ nocase  and security_result.action = "ALLOW"))
    
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Source IPs Enabling Objects | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Enable/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /UpdateCryptoKeyVersion|Enable/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase and
    target.resource.attribute.labels.value = /ENABLED/ nocase and security_result.action = "ALLOW"))
    
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $Source_IP, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
          
  
Top 10 Users Rotating Objects | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Rotate|KeyRotation/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /CreateCryptoKeyVersion|updateCryptoKeyPrimaryVersion|Rotate/ nocase and  metadata.product_event_type = /key|secret|certificate/ nocase  and security_result.action = "ALLOW"))
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, principal.user.group_identifiers)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
          
  
Objects Rotated Over Time | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Rotate|KeyRotation/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /CreateCryptoKeyVersion|updateCryptoKeyPrimaryVersion|Rotate/ nocase and  metadata.product_event_type = /key|secret|certificate/ nocase  and security_result.action = "ALLOW"))
    
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Source IPs Rotating Objects | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Rotate|KeyRotation/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /CreateCryptoKeyVersion|updateCryptoKeyPrimaryVersion|Rotate/ nocase and  metadata.product_event_type = /key|secret|certificate/ nocase  and security_result.action = "ALLOW"))
    
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $Source_IP, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Deleting objects | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Delete/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /Delete|Destroy/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase
    and security_result.action = "ALLOW"))
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, principal.user.group_identifiers)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
          
  
Top 10 Objects Rotated | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Rotate|KeyRotation/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /CreateCryptoKeyVersion|updateCryptoKeyPrimaryVersion|Rotate/ nocase and  metadata.product_event_type = /key|secret|certificate/ nocase  and security_result.action = "ALLOW"))
    
    $Object_ID = strings.coalesce(target.resource.product_object_id, principal.user.product_object_id, principal.resource.product_object_id)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $Object_ID, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
          
  
Top 10 Objects Disabled | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Disable/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /UpdateCryptoKeyVersion|Disable/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase  and
    target.resource.attribute.labels.value = /DISABLED/ nocase and security_result.action = "ALLOW"))
    
    $Object_ID = strings.coalesce(target.resource.product_object_id, principal.user.product_object_id, principal.resource.product_object_id)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
       $Object_ID, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
          
  
Top 10 Blocked Users | 
    
    
    ((metadata.log_type = /AZURE_KEYVAULT_AUDIT|GCP_CLOUDAUDIT/ nocase and (additional.fields["resultType"] = /Fail/ nocase or security_result.action = "BLOCK")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "BLOCK"))
    
    $Event_Type = metadata.event_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, principal.user.group_identifiers)
    
    match:
      $User, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Enabling Objects | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Enable/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /UpdateCryptoKeyVersion|Enable/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase and
    target.resource.attribute.labels.value = /ENABLED/ nocase and security_result.action = "ALLOW"))
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, principal.user.group_identifiers)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
          
  
Recent Objects Created (Last 24 Hours) | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Create/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /Create/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase and
    metadata.product_event_type != /version/ nocase  and security_result.action = "ALLOW"))
    
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Security_Event_Type = metadata.product_event_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, principal.user.group_identifiers)
    $Object_ID = strings.coalesce(target.resource.product_object_id, principal.user.product_object_id, principal.resource.product_object_id)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    $Location = principal.location.country_or_region
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
       $Date , $Log_Type, $Object_ID, $Security_Event_Type, $User, $Source_IP, $Location
    
    order:
      $Date desc
          
  
Top 10 Objects Enabled | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Enable/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /UpdateCryptoKeyVersion|Enable/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase and
    target.resource.attribute.labels.value = /ENABLED/ nocase and security_result.action = "ALLOW"))
    
    $Object_ID = strings.coalesce(target.resource.product_object_id, principal.user.product_object_id, principal.resource.product_object_id)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $Object_ID, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
          
  
Top 10 User Agents | 
    
    
    (metadata.log_type = /AZURE_KEYVAULT_AUDIT|GCP_CLOUDAUDIT/ nocase or target.application = "kms.amazonaws.com")
    
    $User_Agent = network.http.user_agent
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $User_Agent, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs Creating Objects | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Create/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /Create/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase and
    metadata.product_event_type != /version/ nocase  and security_result.action = "ALLOW"))
    
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $Source_IP, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Object Locations | 
    
    
    (metadata.log_type = /AZURE_KEYVAULT_AUDIT|GCP_CLOUDAUDIT/ nocase or target.application = "kms.amazonaws.com")
    
    $Object_ID = strings.coalesce(target.resource.product_object_id, principal.user.product_object_id, principal.resource.product_object_id)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    $Location = target.location.name
    
    match:
      $Location, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
          
  
Objects Enabled Over Time | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Enable/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /UpdateCryptoKeyVersion|Enable/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase and
    target.resource.attribute.labels.value = /ENABLED/ nocase and security_result.action = "ALLOW"))
    
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Blocked Source IPs | 
    
    
    ((metadata.log_type = /AZURE_KEYVAULT_AUDIT|GCP_CLOUDAUDIT/ nocase and (additional.fields["resultType"] = /Fail/ nocase or security_result.action = "BLOCK")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "BLOCK"))
    
    $Event_Type = metadata.event_type
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    
    match:
      $Source_IP, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
          
  
Objects Created by Geolocation | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Create/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /Create/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase and
    metadata.product_event_type != /version/ nocase  and security_result.action = "ALLOW"))
    
    $Country = principal.ip_geo_artifact.location.country_or_region
    $Country != ""
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(principal.ip_geo_artifact.location.region_coordinates.latitude)
      $Longitude = max(principal.ip_geo_artifact.location.region_coordinates.longitude)
    
    order:
      $Count desc
      
  
Top 10 Users Disabling Objects | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Disable/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /UpdateCryptoKeyVersion|Disable/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase  and
    target.resource.attribute.labels.value = /DISABLED/ nocase and security_result.action = "ALLOW"))
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, principal.user.group_identifiers)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
          
  
Top 10 Source IPs Disabling Objects | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Disable/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /UpdateCryptoKeyVersion|Disable/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase  and
    target.resource.attribute.labels.value = /DISABLED/ nocase and security_result.action = "ALLOW"))
    
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $Source_IP, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
      
  
Recent Objects Deleted(Last 24 Hours) | 
    
    
    ((metadata.log_type = "AZURE_KEYVAULT_AUDIT" and additional.fields["resultType"] = /Allow|Success/ nocase) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW"))
    metadata.product_event_type = /Delete/ nocase
    
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Security_Event_Type = metadata.product_event_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, principal.user.group_identifiers)
    $Object_ID = strings.coalesce(target.resource.product_object_id, principal.user.product_object_id, principal.resource.product_object_id)
    $Location = principal.location.country_or_region
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
       $Date, $Log_Type, $Object_ID, $Security_Event_Type, $User, $Source_IP, $Location
    
    order:
      $Date desc
    
    limit:
        10
          
  
Top 10 Source IPs Deleting Objects | 
    
    
    ((((metadata.log_type = /AZURE_KEYVAULT_AUDIT/ nocase and (additional.fields["resultType"] = /Allow|Success/ nocase or security_result.action = "ALLOW")) or
    (target.application = "kms.amazonaws.com" and security_result.action = "ALLOW")) and metadata.product_event_type = /Delete/ nocase) or
    (metadata.log_type = /GCP_CLOUDAUDIT/ nocase and metadata.product_event_type = /Delete|Destroy/ nocase and metadata.product_event_type = /key|secret|certificate/ nocase
    and security_result.action = "ALLOW"))
    
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $Source_IP, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
## Cloud Security Posture Overview

This dashboard provides Cloud Security posture insights by tracking key metrics across Google Cloud, AWS, and Azure.

Top 10 Triggering Rules

Chart name | Query example  
---|---  
Top 10 Triggering Rules | 
    
    
    $log_type = metadata.log_type
    $log_type = /AWS|AZURE/
    $rule_name = security_result.rule_name
    $rule_name != ""
    match:
    $rule_name
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
## Cloud Storage Services Overview

This dashboard provides valuable insights on cloud storage activities such as resources created, deleted, accessed, updated, and permissions changed. It includes trend visualizations of events and alerts over time and highlights top users, IP addresses, user agents, and resource locations. This information helps identify unusual patterns, monitor alerts, and maintain data integrity while protecting cloud environments.

Top 10 Source IPs Accessing ResourcesResources Accessed by GeolocationTop 10 User AgentsTop 10 Source IPs Updating ResourcesTop 10 Resources AccessedResources Deleted Over TimeTop 10 Blocked UsersRecent Resources Created (Last 24 Hours)Resources Accessed Over TimeTop 10 Source IPs Changing Resource PermissionsRecent Resources Deleted (Last 24 Hours)Top 10 Blocked Source IPsEvents Over TimeTop 10 Resource LocationsTop 10 Source IPs Deleting ResourcesResource Permissions Changed Over TimeTop 10 Source IPs Creating ResourcesTop 10 Users Accessing ResourcesTop 10 Resources with Permission ChangedTop 10 Users Updating ResourcesTop 10 Users Changing Resource PermissionsResources Created Over TimeTop 10 Resources UpdatedTop 10 Users Deleting ResourcesTop 10 Users Creating ResourcesResources Updated Over TimePublicly Shared Buckets

Chart name | Query example  
---|---  
Top 10 Source IPs Accessing Resources | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_READ"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/read/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Resources Accessed by Geolocation | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_READ"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/read/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Country = principal.location.country_or_region
    $Country != ""
    $Latitude = principal.location.region_coordinates.latitude
    $Longitude = principal.location.region_coordinates.longitude
    
    match:
      $Country, $Latitude, $Longitude
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 User Agents | 
    
    
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.product_event_type = /storage|bucket/ nocase
     and (metadata.event_type = "RESOURCE_CREATION"
     or metadata.event_type = "RESOURCE_DELETION"
     or metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
     or metadata.event_type = "RESOURCE_READ"
     or metadata.event_type = "RESOURCE_WRITTEN"))
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/(?:write|delete|read)/ nocase)
    network.http.user_agent != ""
    
    $Log_Type = metadata.log_type
    $User_Agent = network.http.user_agent
    
    match:
      $Log_Type, $User_Agent
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs Updating Resources | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_WRITTEN"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/(?:write|.*\/write)?/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Resources Accessed | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_READ"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/(?:write|.*\/write)?/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Resource_Name = target.resource.name
    
    match:
      $Log_Type, $Resource_Name
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Resources Deleted Over Time | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_DELETION"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/delete/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Blocked Users | 
    
    
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.product_event_type = /storage|bucket/ nocase
     and (metadata.event_type = "RESOURCE_CREATION"
     or metadata.event_type = "RESOURCE_DELETION"
     or metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
     or metadata.event_type = "RESOURCE_READ"
     or metadata.event_type = "RESOURCE_WRITTEN"))
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/(?:write|delete|read)/ nocase)
    security_result.action = "BLOCK"
    
    $Event_Type = metadata.event_type
    $User = principal.user.userid
    
    match:
      $Event_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Resources Created (Last 24 Hours) | 
    
    
    (
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.event_type = "RESOURCE_CREATION"
    and metadata.product_event_type = /storage|bucket/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/write/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    $User = principal.user.userid
    $Resource_Name = target.resource.name
    $Location = principal.location.country_or_region
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $IP_Address, $User, $Location, $Resource_Name
    
    order:
      $Date desc  
  
Resources Accessed Over Time | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_READ"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/read/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Source IPs Changing Resource Permissions | 
    
    
    (
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    and metadata.product_event_type = /storage|bucket/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.authorization\/(?:policyassignments|roledefinitions)?\/write/ nocase
    and target.resource.resource_type = "STORAGE_BUCKET")
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Resources Deleted (Last 24 Hours) | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_DELETION"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/delete/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    $User = principal.user.userid
    $Resource_Name = target.resource.name
    $Location = principal.location.country_or_region
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $IP_Address, $User, $Location, $Resource_Name
    
    order:
      $Date desc  
  
Top 10 Blocked Source IPs | 
    
    
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.product_event_type = /storage|bucket/ nocase
     and (metadata.event_type = "RESOURCE_CREATION"
     or metadata.event_type = "RESOURCE_DELETION"
     or metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
     or metadata.event_type = "RESOURCE_READ"
     or metadata.event_type = "RESOURCE_WRITTEN"))
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/(?:write|delete|read)/ nocase)
    security_result.action = "BLOCK"
    
    $Event_Type = metadata.event_type
    $IP_Address = principal.ip
    
    match:
      $Event_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Events Over Time | 
    
    
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.product_event_type = /storage|bucket/ nocase
     and (metadata.event_type = "RESOURCE_CREATION"
     or metadata.event_type = "RESOURCE_DELETION"
     or metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
     or metadata.event_type = "RESOURCE_READ"
     or metadata.event_type = "RESOURCE_WRITTEN"))
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/(?:write|delete|read)/ nocase)
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Resource Locations | 
    
    
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.product_event_type = /storage|bucket/ nocase
     and (metadata.event_type = "RESOURCE_CREATION"
     or metadata.event_type = "RESOURCE_DELETION"
     or metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
     or metadata.event_type = "RESOURCE_READ"
     or metadata.event_type = "RESOURCE_WRITTEN"))
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage[\/\.]storageaccounts[\/\.](?:write|delete|read)/ nocase)
    target.location.name != ""
    security_result.action = "ALLOW"
    
    $Location = target.location.name
    $Log_Type = metadata.log_type
    
    match:
      $Location, $Log_Type
    
    outcome:
      $Count = count_distinct(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs Deleting Resources | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_DELETION"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/delete/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Resource Permissions Changed Over Time | 
    
    
    (
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    and metadata.product_event_type = /storage|bucket/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.authorization\/(?:policyassignments|roledefinitions)?\/write/ nocase
    and target.resource.resource_type = "STORAGE_BUCKET")
    )
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Source IPs Creating Resources | 
    
    
    (
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.event_type = "RESOURCE_CREATION"
    and metadata.product_event_type = /storage|bucket/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/write/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Accessing Resources | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_READ"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/read/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = principal.user.userid
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Resources with Permission Changed | 
    
    
    (
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    and metadata.product_event_type = /storage|bucket/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.authorization\/(?:policyassignments|roledefinitions)?\/write/ nocase
    and target.resource.resource_type = "STORAGE_BUCKET")
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Resource_Name = target.resource.name
    
    match:
      $Log_Type, $Resource_Name
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Updating Resources | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_WRITTEN"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/(?:write|.*\/write)?/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = principal.user.userid
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Changing Resource Permissions | 
    
    
    (
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    and metadata.product_event_type = /storage|bucket/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.authorization\/(?:policyassignments|roledefinitions)?\/write/ nocase
    and target.resource.resource_type = "STORAGE_BUCKET")
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = principal.user.userid
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Resources Created Over Time | 
    
    
    (
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.event_type = "RESOURCE_CREATION"
    and metadata.product_event_type = /storage|bucket/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/write/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Resources Updated | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_WRITTEN"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/(?:write|.*\/write)?/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Resource_Name = target.resource.name
    
    match:
      $Log_Type, $Resource_Name
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Deleting Resources | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_DELETION"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/delete/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = principal.user.userid
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Creating Resources | 
    
    
    (
    (metadata.log_type = /AWS_CLOUDTRAIL|GCP_CLOUDAUDIT/ nocase
    and metadata.event_type = "RESOURCE_CREATION"
    and metadata.product_event_type = /storage|bucket/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/write/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = principal.user.userid
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Resources Updated Over Time | 
    
    
    (
    (metadata.log_type = /(AWS_CLOUDTRAIL|GCP_CLOUDAUDIT)/ nocase
    and metadata.event_type = "RESOURCE_WRITTEN"
    and metadata.product_event_type = /(storage|bucket)/ nocase)
    or
    (metadata.log_type = /AZURE/ nocase
    and metadata.product_event_type = /microsoft\.storage\/storageaccounts\/(?:write|.*\/write)?/ nocase)
    )
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)  
  
Publicly Shared Buckets | 
    
    
    (metadata.log_type = "AZURE_ACTIVITY"
    and metadata.product_event_type = "Microsoft.Storage/storageAccounts/write" nocase
    and security_result.detection_fields["allowBlobPublicAccess"] = "true")
    or
    (metadata.log_type = "GCP_CLOUDAUDIT"
    and metadata.product_event_type = "storage.setIamPermissions"
    and target.application = "storage.googleapis.com"
    and security_result.action = "ALLOW"
    and target.resource.attribute.labels["ser_binding_deltas_action"] = "ADD"
    and target.resource.attribute.labels["ser_binding_deltas_role"] = /roles\/storage.*/
    and target.resource.attribute.labels["ser_binding_deltas_member"] = /allUsers|allAuthenticatedUsers/
    and target.resource.resource_type = "STORAGE_BUCKET"
    )
    or
    (metadata.log_type = "AWS_CLOUDTRAIL"
    and metadata.ingestion_labels["EventSource"] = "s3.amazonaws.com" nocase
    and metadata.product_event_type = /PutBucketPublicAccessBlock/ nocase
    and (target.resource.attribute.labels["BlockPublicAcls"] = "false"
    or target.resource.attribute.labels["BlockPublicPolicy"] = "false"
    or target.resource.attribute.labels["IgnorePublicAcls"] = "false"
    or target.resource.attribute.labels["RestrictPublicBuckets"] = "false")
    )
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Log_Type = metadata.log_type
    $User = principal.user.userid
    $Resource_Name = target.resource.name
    
    match:
      $Date, $Log_Type, $User, $Resource_Name  
  
## DDOS Overview

This dashboard provides a comprehensive analysis of Distributed Denial-of-Service (DDoS) activities, offering insights into attack trends, patterns, and behaviors. It helps identify threat vectors and high-risk areas within the network, empowering security teams to effectively detect, respond to, and mitigate DDoS attacks.

Top 10 Vendor AlertsTop 10 Source IPs by ActionEvents by Event TypeVendor Alerts Over Time by Log TypeEvents Over Time by Log TypeEvents by DescriptionSource Geolocation Overview

Chart name | Query example  
---|---  
Top 10 Vendor Alerts | 
    
    
    (metadata.log_type = /ddos/ nocase or (security_result.description  = /ddos/ nocase or security_result.summary  = /ddos/ nocase or metadata.description = /ddos/ nocase))
    
    $Rule_Name = security_result.rule_name
    $Rule_Name != ""
    $Log_Type = metadata.log_type
    $Action = security_result.action
    
    match:
      $Rule_Name, $Log_Type, $Action
    
    outcome:
    
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs by Action | 
    
    
    (metadata.log_type = /ddos/ nocase or (security_result.description  = /ddos/ nocase or security_result.summary  = /ddos/ nocase or metadata.description = /ddos/ nocase))
    
    $Source_Ip = strings.coalesce(principal.ip, principal.asset.ip)
    $Action = security_result.action
    
    match:
      $Source_Ip, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
      
  
Events by Event Type | 
    
    
    (metadata.log_type = /ddos/ nocase or (security_result.description  = /ddos/ nocase or security_result.summary  = /ddos/ nocase or metadata.description = /ddos/ nocase))
    
    $Event_Type = metadata.event_type
    
    match:
      $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Vendor Alerts Over Time by Log Type | 
    
    
    (metadata.log_type = /ddos/ nocase or (security_result.description  = /ddos/ nocase or security_result.summary  = /ddos/ nocase or metadata.description = /ddos/ nocase))
    security_result.rule_name != ""
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
    
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Events Over Time by Log Type | 
    
    
    (metadata.log_type = /ddos/ nocase or (security_result.description  = /ddos/ nocase or security_result.summary  = /ddos/ nocase or metadata.description = /ddos/ nocase))
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Events by Description | 
    
    
    (metadata.log_type = /ddos/ nocase or (security_result.description  = /ddos/ nocase or security_result.summary  = /ddos/ nocase or metadata.description = /ddos/ nocase))
    
    $Description = strings.coalesce(metadata.description,security_result.summary,security_result.description)
    $Log_Type = metadata.log_type
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Destination_IP = strings.coalesce(target.ip, target.asset.ip)
    $Action = security_result.action
    $Destination_Hostname = strings.coalesce(target.hostname, target.asset.hostname)
    $File = principal.process.file.full_path
    
    match:
       $Description, $Source_IP, $Destination_IP, $Destination_Hostname, $Action, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
Source Geolocation Overview | 
    
    
    (metadata.log_type = /ddos/ nocase or (security_result.description  = /ddos/ nocase or security_result.summary  = /ddos/ nocase or metadata.description = /ddos/ nocase))
    
    $Country = principal.ip_geo_artifact.location.country_or_region
    $Country !=""
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(principal.ip_geo_artifact.location.region_latitude)
      $Longitude = max(principal.ip_geo_artifact.location.region_longitude)
    
    order:
      $Count desc
      
  
## DNS Monitoring

This dashboard provides a detailed overview of DNS activity and network health, featuring insights into DNS events, query trends, and the distribution of allowed and blocked queries. It enables efficient monitoring, threat detection, and troubleshooting through visualizations of anomalies, locations, and DNS failures.

**Note:** Apply the available filters to refine the data and display relevant results.

Top 10 Allowed DNS QueriesTop 10 DNS Allowed CategoriesTotal DNS EventsReporting HostsTop 10 DNS QuestionsTotal DNS Events by Log TypeTop 10 DNS Blocked CategoriesSuccessful DNS Response Over TimeCommon DNS ActivitiesTop 10 Blocked DNS QueriesDNS Queries by Action: Allow vs BlockDNS Events by Log Type Over TimeDNS Record Types BreakupFailed DNS Response Over TimeTop 10 Source IPsDNS Record Types over TimeTotal Log Volume of DNS Events Over TimeDNS Queries by Record TypeTotal Reporting HostsDNS Queries Over TimeTop 10 DNS Queries by Location

Chart name | Query example  
---|---  
Top 10 Allowed DNS Queries | 
    
    
    metadata.event_type = "NETWORK_DNS"
    network.dns.questions.name != ""
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $DNS_Questions_Name = network.dns.questions.name
    
    match:
      $DNS_Questions_Name, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 DNS Allowed Categories | 
    
    
    metadata.event_type = "NETWORK_DNS"
    security_result.action = "ALLOW"
    security_result.category_details != ""
    
    $Log_Type = metadata.log_type
    $Category = security_result.category_details
    
    match:
      $Category, $Log_Type
    
    outcome:
      $Count = count($Category)
    
    order:
      $Count desc
    
    limit:
        10  
  
Total DNS Events | 
    
    
    metadata.event_type = "NETWORK_DNS"
    
    outcome:
      $Count = count(metadata.id)  
  
Reporting Hosts | 
    
    
    metadata.event_type = "NETWORK_DNS"
    
    $Hostname = principal.hostname
    
    match:
      $Hostname  
  
Top 10 DNS Questions | 
    
    
    $event.metadata.log_type = /EXTRAHOP_DNS|UMBRELLA_DNS/ nocase
    $event.metadata.event_type = "NETWORK_DNS"
    
    $Questions_Name = $event.network.dns.questions.name
    
    match:
      $Questions_Name
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Total DNS Events | 
    
    
    $event.metadata.log_type = /EXTRAHOP_DNS|UMBRELLA_DNS/ nocase
    $event.metadata.event_type = "NETWORK_DNS"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Total DNS Events by Log Type | 
    
    
    $event.metadata.log_type = /EXTRAHOP_DNS|UMBRELLA_DNS/ nocase
    $event.metadata.event_type = "NETWORK_DNS"
    
    $Log_Type = $event.metadata.log_type
    $Event_Type = $event.metadata.event_type
    
    match:
      $Log_Type, $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count asc  
  
Top 10 DNS Blocked Categories | 
    
    
    metadata.event_type = "NETWORK_DNS"
    security_result.action = "BLOCK"
    security_result.category_details != ""
    
    $Log_Type = metadata.log_type
    $Category = security_result.category_details
    
    match:
      $Category, $Log_Type
    
    outcome:
      $Count = count($Category)
    
    order:
      $Count desc
    
    limit:
        10  
  
Successful DNS Response Over Time | 
    
    
    $event.metadata.log_type = /EXTRAHOP_DNS|UMBRELLA_DNS/ nocase
    $event.metadata.event_type = "NETWORK_DNS"
    $event.network.dns.response = true
    $event.network.application_protocol = "DNS"
    
    $Answered = $event.network.dns.response
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Answered
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc   
  
Common DNS Activities | 
    
    
    metadata.event_type = "NETWORK_DNS"
    
    $Log_Type = metadata.log_type
    $Source_IP = principal.ip
    $Description = strings.coalesce(metadata.description, security_result.summary)
    $DNS_Questions_Name = network.dns.questions.name
    
    match:
      $Source_IP, $Log_Type, $Description, $DNS_Questions_Name
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Blocked DNS Queries | 
    
    
    metadata.event_type = "NETWORK_DNS"
    network.dns.questions.name != ""
    security_result.action = "BLOCK"
    
    $Log_Type = metadata.log_type
    $DNS_Questions_Name = network.dns.questions.name
    
    match:
      $DNS_Questions_Name, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
DNS Queries by Action: Allow vs Block | 
    
    
    metadata.event_type = "NETWORK_DNS"
    network.dns.questions.name != ""
    security_result.action = "ALLOW"
    or security_result.action = "BLOCK"
    
    $Action = security_result.action
    
    match:
      $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc   
  
DNS Events by Log Type Over Time | 
    
    
    metadata.event_type = "NETWORK_DNS"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc   
  
DNS Record Types Breakup | 
    
    
    $event.metadata.log_type = /EXTRAHOP_DNS|UMBRELLA_DNS/ nocase
    $event.metadata.event_type = "NETWORK_DNS"
    
    $Log_Type = $event.metadata.log_type
    $Event_Type = $event.metadata.event_type
    $DNS_Record_Type = $event.additional.fields["dns_record_type"]
    $DNS_Record_Type != ""
    $Return_Message = $event.additional.fields["dns_return_message"]
    $Date = timestamp.get_timestamp($event.metadata.event_timestamp.seconds)
    $Description = $event.metadata.description
    
    match:
      $Date, $Log_Type, $DNS_Record_Type, $Description, $Return_Message
    order:
      $Date desc
    limit:
        50  
  
Failed DNS Response Over Time | 
    
    
    metadata.event_type = "NETWORK_DNS"
    network.dns.response_code = 3
    or network.dns.response_code = 5
    
    $Denied = strings.concat(network.dns.response_code, " ")
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Denied, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Source IPs | 
    
    
    $event.metadata.log_type = /EXTRAHOP_DNS|UMBRELLA_DNS/ nocase
    $event.metadata.event_type = "NETWORK_DNS"
    
    $Log_Type = $event.metadata.log_type
    $Event_Type = $event.metadata.event_type
    $Source_IP = $event.principal.ip
    $Source_IP != ""
    
    match:
      $Source_IP, $Event_Type, $Log_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
DNS Record Types over Time | 
    
    
    $event.metadata.log_type = /EXTRAHOP_DNS|UMBRELLA_DNS/ nocase
    $event.metadata.event_type = "NETWORK_DNS"
    
    $Record_Types = $event.additional.fields["dns_record_type"]
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Record_Types, $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Total DNS Events by Log Type | 
    
    
    metadata.event_type = "NETWORK_DNS"
    
    $Log_Type = metadata.log_type
    
    match:
      $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Total Log Volume of DNS Events Over Time | 
    
    
    $event.metadata.log_type = /EXTRAHOP_DNS|UMBRELLA_DNS/ nocase
    $event.metadata.event_type = "NETWORK_DNS"
    
    $Log_Type = $event.metadata.log_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc   
  
Failed DNS Response Over Time | 
    
    
    $event.metadata.log_type = /EXTRAHOP_DNS|UMBRELLA_DNS/ nocase
    $event.network.dns.response_code = 3
    or $event.network.dns.response_code = 5
    $event.metadata.event_type = "NETWORK_DNS"
    
    $Denied = $event.network.dns.response_code
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Denied, $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
DNS Record Types Breakup | 
    
    
    metadata.event_type = "NETWORK_DNS"
    
    $Log_Type = metadata.log_type
    $Event_Type = metadata.event_type
    $Source_IP = principal.ip
    $Hostname = principal.hostname
    $DNS_Record_Type = strings.coalesce(additional.fields["dns_record_type"], extracted.fields["query_type"], extracted.fields["qtype_name"])
    $Return_Message = additional.fields["dns_return_message"]
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    $Description = strings.coalesce(metadata.description, security_result.summary)
    
    match:
      $Date, $Log_Type, $Source_IP, $Hostname, $DNS_Record_Type, $Description, $Return_Message
    
    order:
      $Date desc  
  
Top 10 Source IPs | 
    
    
    metadata.event_type = "NETWORK_DNS"
    
    $Log_Type = metadata.log_type
    $Source_IP = principal.ip
    
    match:
      $Source_IP, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
DNS Queries by Record Type | 
    
    
    metadata.event_type = "NETWORK_DNS"
    network.dns.questions.name != ""
    
    $Record_Types = strings.coalesce(additional.fields["dns_record_type"], extracted.fields["query_type"], extracted.fields["qtype_name"])
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Record_Types
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Total Reporting Hosts | 
    
    
    metadata.event_type = "NETWORK_DNS"
    
    outcome:
      $Count = count_distinct(principal.hostname)  
  
DNS Queries Over Time | 
    
    
    metadata.event_type = "NETWORK_DNS"
    network.dns.questions.name != ""
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(network.dns.questions.name)
    
    order:
      $Date desc  
  
Successful DNS Response Over Time | 
    
    
    metadata.event_type = "NETWORK_DNS"
    network.dns.response = true
    
    $Answered = network.dns.response
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Answered
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc   
  
Common DNS Activities | 
    
    
    $event.metadata.log_type = /EXTRAHOP_DNS|UMBRELLA_DNS/ nocase
    $event.metadata.event_type = "NETWORK_DNS"
    
    $Log_Type = $event.metadata.log_type
    $Source_IP = $event.principal.ip
    $Description = $event.metadata.description
    $DQ_Name = $event.network.dns.questions.name
    
    match:
      $Source_IP, $Description, $DQ_Name
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        50  
  
Top 10 DNS Queries by Location | 
    
    
    metadata.event_type = "NETWORK_DNS"
    network.dns.questions.name != ""
    
    $Questions_Name = network.dns.questions.name
    $Country = principal.ip_geo_artifact.location.country_or_region
    $Latitude = principal.ip_geo_artifact.location.region_latitude
    $Longitude = principal.ip_geo_artifact.location.region_longitude
    
    match:
      $Questions_Name, $Country, $Latitude, $Longitude
    
    outcome:
      $Count = count(metadata.id)
    
    limit:
        10  
  
## Data Ingestion and Health

This dashboard provides critical insights into data flow, displaying ingested events and error counts for clear visibility into potential issues. It includes visualizations for log type distribution and the status of ingested events, along with recent ingestion activity and daily log information. By tracking ingestion throughput over various timeframes, the dashboard helps spot trends and issues, improving your organization's ability to manage data ingestion and maintain smooth operations.

Bindplane Agent Logging - Logs by Severity over TimeNumber of Days Since Hosts Reported an Event (Last 7 Days)Bindplane Agent Logging - Messages by Count

Chart name | Query example  
---|---  
Bindplane Agent Logging - Logs by Severity over Time | 
    
    
    metadata.log_type = "BINDPLANE_AGENT"
    metadata.ingestion_labels.key = "ingestion_source"
    metadata.ingestion_labels.value = $agent
    metadata.description = $message
    security_result.severity = $severity
    timestamp.get_timestamp(metadata.event_timestamp.seconds) = $timestamp
    match:
      $severity, $timestamp
    outcome:
      $total = count(metadata.id)
    order :
      $severity
      
  
Number of Days Since Hosts Reported an Event (Last 7 Days) | 
    
    
    $host = principal.hostname
    $event_time = metadata.event_timestamp.seconds
    match:
      $host
    outcome:
      $last_seen_timestamp = timestamp.get_timestamp(max($event_time))
      $days_since_last_seen = math.round((timestamp.current_seconds() - max($event_time)) / 86400, 0)
    order:
      $days_since_last_seen desc  
  
Bindplane Agent Logging - Messages by Count | 
    
    
    metadata.log_type = "BINDPLANE_AGENT"
    metadata.ingestion_labels.key = "ingestion_source"
    metadata.ingestion_labels.value = $agent
    metadata.description = $message
    security_result.severity = $severity
    match:
      $severity, $message
    outcome:
      $total = count(metadata.id)
      $first_seen = timestamp.get_timestamp(min(metadata.event_timestamp.seconds))
      $last_seen = timestamp.get_timestamp(max(metadata.event_timestamp.seconds))  
  
## Data Loss Prevention (DLP)

This dashboard provides key metrics related to DLP events.

Top 10 UsersSensitive Data Access AttemptsDLP Event Trend Over TimeEvents By ActionDLP Violations by SeverityTop 10 DLP Policy Violation Event TypesDLP Violations over TimeTop 10 HostsTop 10 DLP RulesTop 10 Users by Data Exfiltration AttemptsTop 10 Files

Chart name | Query example  
---|---  
Top 10 Users | 
    
    
    $log_type = metadata.log_type
    $log_type = /DLP/ nocase
    $user= strings.coalesce(principal.user.user_display_name,principal.user.userid)
    $user != ""
    match:
    $user
    outcome:
    $user_count = count(metadata.id)
    order:
    $user_count desc
    limit: 10  
  
Sensitive Data Access Attempts | 
    
    
    $log_type = metadata.log_type
    $log_type = /DLP/ nocase
    $event_type = metadata.event_type
    $security_event_type = metadata.product_event_type
    $security_event_type = /Sensitive/
    $user = strings.coalesce(principal.user.user_display_name,principal.user.userid)
    $action = security_result.action_details
    $hostname = principal.hostname
    $src_ip = principal.ip
    $file_path = target.file.full_path
    
    match:
      $user,$action,$src_ip,$hostname,$file_path
    outcome:
       $event_count = count(metadata.id)
    
    order:
    $event_count desc  
  
DLP Event Trend Over Time | 
    
    
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    $log_type = metadata.log_type
    $log_type = /DLP/ nocase
    match:
    $date
    outcome:
    $event_count = count(metadata.id)  
  
Events By Action | 
    
    
    $log_type = metadata.log_type
    $log_type = /DLP/ nocase
    $action = security_result.action_details
    $action != ""
    match:
    $action
    outcome:
    $event_count = count(metadata.id)
    order:
    $action asc  
  
DLP Violations by Severity | 
    
    
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    $log_type=metadata.log_type
    $log_type = /DLP/ nocase
    $severity =security_result.severity
    $security_event_type=metadata.product_event_type
    $security_event_type = /Violation/ nocase
    match:
      $severity
    outcome:
       $count = count(metadata.id)
    order:
    $severity desc  
  
Top 10 DLP Policy Violation Event Types | 
    
    
    $log_type = metadata.log_type
    $log_type = /DLP/ nocase
    $event_type = metadata.product_event_type
    $user = principal.user.user_display_name
    $reason = strings.coalesce(security_result.summary,metadata.description,metadata.product_event_type)
    $reason = /violation/ nocase
    match:
    $event_type
    outcome:
    $event_count = count(metadata.id)
    $Count_user = count_distinct($user)
    order:
    $event_count desc
    limit:
    10  
  
DLP Violations over Time | 
    
    
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    $log_type=metadata.log_type
    $log_type = /DLP/ nocase
    $security_event_type=metadata.product_event_type
    $security_event_type = /Violation/ nocase
    
    match:
    $date
    
    outcome:
    $count = count(metadata.id)
    
    order:
    $date  asc  
  
Top 10 Hosts | 
    
    
    $log_type = metadata.log_type
    $log_type = /DLP/ nocase
    $hostname= strings.coalesce(principal.hostname, principal.asset.hostname)
    $hostname != ""
    
    match:
    $hostname
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit: 10  
  
Top 10 DLP Rules | 
    
    
    $log_type = metadata.log_type
    $log_type = /DLP/
    $rule_name = security_result.rule_name
    $rule_name != ""
    match:
    $rule_name
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit: 10  
  
Top 10 Users by Data Exfiltration Attempts | 
    
    
    $log_type = metadata.log_type
    $log_type = /DLP/ nocase
    $user = strings.coalesce(principal.user.user_display_name,principal.user.userid)
    $user !=""
    $reason = strings.coalesce(metadata.product_event_type,security_result.summary,metadata.description)
    $reason = /exfiltration/ nocase
    $action = security_result.action_details
    match:
      $user
    outcome:
       $Action = array_distinct($action)
       $Reason = array_distinct($reason)
       $event_count = count(metadata.id)
    order:
     $event_count desc
     limit:
     10   
  
Top 10 Files | 
    
    
    $log_type = metadata.log_type
    $log_type = /DLP/
    $file_name = strings.coalesce(target.file.full_path, additional.fields["fname"])
    match:
    $file_name
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit: 10
      
  
## Data Security Monitoring

This dashboard provides a comprehensive view of security events provided by data security tools, focusing on metrics like event severity, actions taken, and triggering rules. It tracks top hosts, users, and geographical patterns to identify emerging threats and trends.

Events by SeverityEvents Over Time By Log TypeEvents by ActionSource Geolocation HeatmapEvent Types DistributionTotal EventsTop 10 Events by DescriptionTop 10 Source HostnamesTop 10 Source UsernamesTop 10 Data Security Product Rules Triggered

Chart name | Query example  
---|---  
Events by Severity | 
    
    
    metadata.log_type = /ARUBA_CENTRAL|CLOUDFLARE_WARP|DELL_CYBERSENSE|FORGEROCK_OPENIDM|IMPERVA_DRA|IMPERVA_SECURESPHERE|IBM_OPENPAGES|INTEL471_WATCHER_ALERTS|OKERA_DAP|OPENCANARY|RUBRIK_POLARIS|SENTRY|TINES|TINTRI|VARONIS/ nocase
    
    $Severity = security_result.severity
    
    match:
      $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Events Over Time By Log Type | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type =  /ARUBA_CENTRAL|CLOUDFLARE_WARP|DELL_CYBERSENSE|FORGEROCK_OPENIDM|IMPERVA_DRA|IMPERVA_SECURESPHERE|IBM_OPENPAGES|INTEL471_WATCHER_ALERTS|OKERA_DAP|OPENCANARY|RUBRIK_POLARIS|SENTRY|TINES|TINTRI|VARONIS/ nocase
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Events by Action | 
    
    
    metadata.log_type = /ARUBA_CENTRAL|CLOUDFLARE_WARP|DELL_CYBERSENSE|FORGEROCK_OPENIDM|IMPERVA_DRA|IMPERVA_SECURESPHERE|IBM_OPENPAGES|INTEL471_WATCHER_ALERTS|OKERA_DAP|OPENCANARY|RUBRIK_POLARIS|SENTRY|TINES|TINTRI|VARONIS/ nocase
    
    $Action = security_result.action
    
    match:
      $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Source Geolocation Heatmap | 
    
    
    metadata.log_type = /ARUBA_CENTRAL|CLOUDFLARE_WARP|DELL_CYBERSENSE|FORGEROCK_OPENIDM|IMPERVA_DRA|IMPERVA_SECURESPHERE|IBM_OPENPAGES|INTEL471_WATCHER_ALERTS|OKERA_DAP|OPENCANARY|RUBRIK_POLARIS|SENTRY|TINES|TINTRI|VARONIS/ nocase
    
    $Country = principal.ip_geo_artifact.location.country_or_region
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(principal.ip_geo_artifact.location.region_latitude)
      $Longitude = max(principal.ip_geo_artifact.location.region_longitude)
    
    order:
      $Count desc  
  
Event Types Distribution | 
    
    
    metadata.log_type =  /ARUBA_CENTRAL|CLOUDFLARE_WARP|DELL_CYBERSENSE|FORGEROCK_OPENIDM|IMPERVA_DRA|IMPERVA_SECURESPHERE|IBM_OPENPAGES|INTEL471_WATCHER_ALERTS|OKERA_DAP|OPENCANARY|RUBRIK_POLARIS|SENTRY|TINES|TINTRI|VARONIS/ nocase
    
    $Event_Type = metadata.event_type
    
    match:
      $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
Total Events | 
    
    
    metadata.log_type = /ARUBA_CENTRAL|CLOUDFLARE_WARP|DELL_CYBERSENSE|FORGEROCK_OPENIDM|IMPERVA_DRA|IMPERVA_SECURESPHERE|IBM_OPENPAGES|INTEL471_WATCHER_ALERTS|OKERA_DAP|OPENCANARY|RUBRIK_POLARIS|SENTRY|TINES|TINTRI|VARONIS/
    
    outcome:
       $Count = count(metadata.id)  
  
Top 10 Events by Description | 
    
    
    metadata.log_type = /ARUBA_CENTRAL|CLOUDFLARE_WARP|DELL_CYBERSENSE|FORGEROCK_OPENIDM|IMPERVA_DRA|IMPERVA_SECURESPHERE|IBM_OPENPAGES|INTEL471_WATCHER_ALERTS|OKERA_DAP|OPENCANARY|RUBRIK_POLARIS|SENTRY|TINES|TINTRI|VARONIS/ nocase
    
    $Summary = strings.coalesce(metadata.description,security_result.description,security_result.summary)
    $Summary != ""
    match:
      $Summary
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source Hostnames | 
    
    
    metadata.log_type = /ARUBA_CENTRAL|CLOUDFLARE_WARP|DELL_CYBERSENSE|FORGEROCK_OPENIDM|IMPERVA_DRA|IMPERVA_SECURESPHERE|IBM_OPENPAGES|INTEL471_WATCHER_ALERTS|OKERA_DAP|OPENCANARY|RUBRIK_POLARIS|SENTRY|TINES|TINTRI|VARONIS/ nocase
    
    $Hostname= strings.coalesce(principal.hostname, principal.asset.hostname)
    $Hostname!=""
    match:
      $Hostname
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source Usernames | 
    
    
    metadata.log_type = /ARUBA_CENTRAL|CLOUDFLARE_WARP|DELL_CYBERSENSE|FORGEROCK_OPENIDM|IMPERVA_DRA|IMPERVA_SECURESPHERE|IBM_OPENPAGES|INTEL471_WATCHER_ALERTS|OKERA_DAP|OPENCANARY|RUBRIK_POLARIS|SENTRY|TINES|TINTRI|VARONIS/ nocase
    
    $User = strings.coalesce(principal.user.user_display_name, principal.user.userid, principal.user.email_addresses)
    $User != ""
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Data Security Product Rules Triggered | 
    
    
    metadata.log_type = /ARUBA_CENTRAL|CLOUDFLARE_WARP|DELL_CYBERSENSE|FORGEROCK_OPENIDM|IMPERVA_DRA|IMPERVA_SECURESPHERE|IBM_OPENPAGES|INTEL471_WATCHER_ALERTS|OKERA_DAP|OPENCANARY|RUBRIK_POLARIS|SENTRY|TINES|TINTRI|VARONIS/ nocase
    
    $Rule_Name = security_result.rule_name
    $Rule_Name !=""
    match:
      $Rule_Name
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
## Database Monitoring

This dashboard provides in-depth visibility into database operations, security, performance, and health by tracking user activities, executed SQL statements, login trends, and event severities. This helps you identify unusual behaviors, ensure operational efficiency, and proactively manage risks across database environments.

**Note:** Apply filters based on specific log types to display relevant results on the dashboard.

Events by ActionObjects by SeverityFailed Login Attempts Over TimeTop 10 Users by CREATE StatementsPrivileged Access GrantedTop 10 Users by DROP StatementsTop 10 Database-Related File PathsRecent File OperationsRecent Users by CREATE StatementsRecent Failed Login AttemptsDDL StatementsTop 10 Statements ExecutedRecent Successful Login AttemptsRecent Users by Database ConnectionsSuccessful Login Attempts Over TimeGrant Events Over TimeApplication Traffic Over TimeRecent Users by DROP StatementsDDL Statements Over Time by Log TypeDatabase Events by ApplicationSeverity Distribution

Chart name | Query example  
---|---  
Events by Action | 
    
    
    $Action = security_result.action
    
    match:
      $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
Objects by Severity | 
    
    
    $Object_id = strings.coalesce(target.resource.product_object_id, principal.resource.product_object_id)
    $Object_id != ""
    $Severity = security_result.severity
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Summary = strings.coalesce(target.process.command_line, security_result.action_details, security_result.description, extracted.fields["textPayload"], extracted.fields["cmd_line"])
    $IP = strings.coalesce(principal.ip, principal.asset.ip, target.ip, target.asset.ip)
    $Log_Type = metadata.log_type
    
    match:
      $Object_id, $Summary, $User, $IP, $Severity, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
Failed Login Attempts Over Time | 
    
    
    ((metadata.event_type = "USER_LOGIN" and security_result.action = "BLOCK") or (metadata.event_type = "GENERIC_EVENT" and (extracted.fields["token_metadata.event_type"] = "DB_LOGIN_FAILED")))
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc
    
      
  
Top 10 Users by CREATE Statements | 
    
    
    (target.process.command_line = /create/ nocase or extracted.fields["textPayload"] = /create/ nocase or additional.fields["statement"] = /create/ nocase or security_result.description = /create/ nocase or metadata.product_event_type = /create/ nocase)
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Log_Type = metadata.log_type
    
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Privileged Access Granted | 
    
    
    $Summary = strings.coalesce(if (target.process.command_line = /grant|revoke|(alter|create|drop|delete)\s+(user|role|database|server\s+role|login|table|trigger|function)|set\s+(role|password)|rename|backup|restore|impersonate|superuser/ nocase,target.process.command_line, ""),
      if (extracted.fields["textPayload"] = /grant|revoke|(alter|create|drop|delete)\s+(user|role|database|server\s+role|login|table|trigger|function)|set\s+(role|password)|rename|backup|restore|impersonate|superuser/ nocase,extracted.fields["textPayload"], ""),
      if (additional.fields["statement"] = /grant|revoke|(alter|create|drop|delete)\s+(user|role|database|server\s+role|login|table|trigger|function)|set\s+(role|password)|rename|backup|restore|impersonate|superuser/ nocase,additional.fields["statement"], ""),
      if (security_result.description = /grant|revoke|(alter|create|drop|delete)\s+(user|role|database|server\s+role|login|table|trigger|function)|set\s+(role|password)|rename|backup|restore|impersonate|superuser/ nocase,security_result.description,  ""),
      if (metadata.product_event_type = /grant|revoke|(alter|create|drop|delete)\s+(user|role|database|server\s+role|login|table|trigger|function)|set\s+(role|password)|rename|backup|restore|impersonate|superuser/ nocase, strings.concat(metadata.product_event_type, " : ", extracted.fields["cmd_line"]),  ""))
    $Summary != ""
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname, target.resource.name)
    $Log_Type = metadata.log_type
    
    match:
      $User, $Hostname, $Summary, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
    
      
  
Top 10 Users by DROP Statements | 
    
    
    (target.process.command_line = /drop/ nocase or extracted.fields["textPayload"] = /drop/ nocase or additional.fields["statement"] = /drop/ nocase or security_result.description = /drop/ nocase or metadata.product_event_type = /drop/ nocase)
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Log_Type = metadata.log_type
    
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Database-Related File Paths | 
    
    
    $File_Path = target.file.full_path
    $File_Path != ""
    $Log_Type = metadata.log_type
    
    match:
      $File_Path, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent File Operations | 
    
    
    $File = target.file.full_path
    $File != ""
    $Summary = strings.coalesce(target.process.command_line, security_result.description, security_result.action_details, extracted.fields["textPayload"], extracted.fields["cmd_line"])
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Log_Type = metadata.log_type
    
    match:
      $User, $File, $Summary, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
    
      
  
Recent Users by CREATE Statements | 
    
    
    $Summary = strings.coalesce(if (target.process.command_line = /create/ nocase, target.process.command_line, ""),
                                if (extracted.fields["textPayload"] = /create/ nocase, extracted.fields["textPayload"], ""),
                                if (additional.fields["statement"] = /create/ nocase, additional.fields["statement"], ""),
                                if (security_result.description = /create/ nocase, security_result.description, "" ),
                                if (metadata.product_event_type = /create/ nocase, strings.concat(metadata.product_event_type, " : " ,extracted.fields["cmd_line"]), ""))
    $Summary != ""
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname, target.resource.name)
    $Log_Type = metadata.log_type
    
    match:
      $User, $Hostname, $Summary, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
    
      
  
Recent Failed Login Attempts | 
    
    
    ((metadata.event_type = "USER_LOGIN" and security_result.action = "BLOCK") or (metadata.event_type = "GENERIC_EVENT" and (extracted.fields["token_metadata.event_type"] = "DB_LOGIN_FAILED")))
    
    $Log_Type = metadata.log_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname, target.resource.name)
    $Summary = strings.coalesce(extracted.fields["textPayload"], extracted.fields["cmd_line"], principal.user.attribute.permissions.name, security_result.action_details, security_result.description)
    
    match:
      $User, $Hostname, $Summary, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
    
      
  
DDL Statements | 
    
    
    $DDL_Statements = strings.coalesce(if (target.process.command_line = /alter|create|drop|rename|truncate|comment/ nocase, target.process.command_line, ""),
                                       if (extracted.fields["textPayload"] = /alter|create|drop|rename|truncate|comment/ nocase, extracted.fields["textPayload"], ""),
                                       if (additional.fields["statement"] = /alter|create|drop|rename|truncate|comment/ nocase, additional.fields["statement"], ""),
                                       if (security_result.description = /alter|create|drop|rename|truncate|comment/ nocase, security_result.description, "" ),
                                       if (metadata.product_event_type = /alter|create|drop|rename|truncate|comment/ nocase, strings.concat(metadata.product_event_type, " : " ,extracted.fields["cmd_line"]), ""))
    $DDL_Statements != ""
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname, target.resource.name)
    $Log_Type = metadata.log_type
    
    match:
      $DDL_Statements, $User, $Hostname, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
Top 10 Statements Executed | 
    
    
    $Command_Line = strings.coalesce(target.process.command_line, extracted.fields["textPayload"], additional.fields["statement"], extracted.fields["cmd_line"] security_result.description)
    $Log_Type = metadata.log_type
    
    match:
       $Command_Line ,$Log_Type
    
    outcome:
       $Count = count(metadata.id)
    
    order:
       $Count desc
    
    limit:
        10  
  
Recent Successful Login Attempts | 
    
    
    ((metadata.event_type = "USER_LOGIN" and security_result.action = "ALLOW") or (metadata.event_type = "GENERIC_EVENT" and (extracted.fields["token_metadata.event_type"] = "DB_LOGIN_SUCCESS")))
    
    $Log_Type = metadata.log_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname, target.resource.name)
    $Summary = strings.coalesce(extracted.fields["textPayload"], extracted.fields["cmd_line"], principal.user.attribute.permissions.name, security_result.action_details, security_result.description)
    
    match:
      $User, $Hostname, $Summary, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
    
      
  
Recent Users by Database Connections | 
    
    
    (metadata.product_event_type = /connection/ nocase or security_result.description = /Connection/ nocase or additional.fields["operation_name"]= /Connection/ nocase or extracted.fields["textPayload"] = /connection/ nocase or additional.fields["ctx"] = /conn/ nocase)
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Summary  = strings.coalesce(extracted.fields["textPayload"], security_result.description, security_result.action_details, metadata.description)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname, target.resource.name)
    $Log_Type = metadata.log_type
    
    match:
       $User, $Hostname, $Summary, $Log_Type
    
    outcome:
       $Count = count(metadata.id)
       $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
       $Count desc  
  
Successful Login Attempts Over Time | 
    
    
    ((metadata.event_type = "USER_LOGIN" and security_result.action = "ALLOW") or (metadata.event_type = "GENERIC_EVENT" and (extracted.fields["token_metadata.event_type"] = "DB_LOGIN_SUCCESS")))
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc
    
      
  
Grant Events Over Time | 
    
    
    (target.process.command_line = /grant/ nocase or extracted.fields["textPayload"] = /grant/ nocase or additional.fields["statement"] = /grant/ nocase or security_result.description = /grant/ nocase or metadata.product_event_type = /grant/ nocase)
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Application Traffic Over Time | 
    
    
    $Application = target.application
    $Application != ""
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
       $Application, $Date
    
    outcome:
       $Count = count(metadata.id)
    
    order:
       $Date asc  
  
Recent Users by DROP Statements | 
    
    
    $Summary = strings.coalesce(if (target.process.command_line = /drop/ nocase, additional.fields["statement"], ""),
                                if (extracted.fields["textPayload"] = /drop/ nocase, extracted.fields["textPayload"], ""),
                                if (additional.fields["statement"] = /drop/ nocase, additional.fields["statement"], ""),
                                if (security_result.description = /drop/ nocase, security_result.description, "" ),
                                if (metadata.product_event_type = /drop/ nocase, strings.concat(metadata.product_event_type, " : " ,extracted.fields["cmd_line"]), ""))
    $Summary != ""
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname, target.resource.name)
    $Log_Type = metadata.log_type
    
    match:
       $User, $Hostname, $Summary, $Log_Type
    
    outcome:
       $Count = count(metadata.id)
       $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
       $Count desc
      
  
DDL Statements Over Time by Log Type | 
    
    
    (target.process.command_line = /alter|create|drop|rename|truncate|comment/ nocase or extracted.fields["textPayload"] = /alter|create|drop|rename|truncate|comment/ nocase or additional.fields["statement"] = /alter|create|drop|rename|truncate|comment/ nocase or security_result.description = /alter|create|drop|rename|truncate|comment/ nocase or  metadata.product_event_type = /alter|create|drop|rename|truncate|comment/ nocase)
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Database Events by Application | 
    
    
    $Application = target.application
    $Application != ""
    $Log_Type = metadata.log_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname, target.resource.name)
    $Summary = strings.coalesce(extracted.fields["textPayload"], extracted.fields["cmd_line"],target.process.command_line, security_result.action_details, security_result.description)
    
    match:
      $Application, $Summary, $User, $Hostname, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
Severity Distribution | 
    
    
    $Severity = security_result.severity
    
    match:
      $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
## Deception Monitoring

This dashboard provides a comprehensive overview of deception-related activities, offering insights into event trends, patterns, and behaviors. It also highlights high-risk areas within decoy networks, enabling security teams to analyze, monitor, and respond to threats effectively.

**Note:** Apply filters based on specific log types to display relevant results on the dashboard.

Top 10 Destination IPsTop 10 Source IPsEvents Over Time by Log TypeTop 10 Ports and ProtocolsSource Geolocation OverviewTop 10 Destination HostnamesDecoy's Kill Chain Phase Breakdown (Zscaler Deception)Top 10 Source UsersTop 10 Event Types by Log TypeTop 10 Targeted Decoy Resource Types (Zscaler Deception)Top 10 Decoys with High-Risk Scores (Zscaler Deception)Activity Breakdown by Decoy Network (Zscaler Deception)Events by Severity

Chart name | Query example  
---|---  
Top 10 Destination IPs | 
    
    
    $Destination_IP = strings.coalesce(target.ip, target.asset.ip)
    $Log_Type = metadata.log_type
    
    match:
      $Destination_IP, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    Order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs | 
    
    
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Log_Type = metadata.log_type
    
    match:
      $Source_IP, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    Order:
      $Count desc
    
    limit:
        10  
  
Events Over Time by Log Type | 
    
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Ports and Protocols | 
    
    
    $Port = target.port
    
    match:
      $Port
    
    outcome:
      $Protocol = array_distinct(network.application_protocol)
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Source Geolocation Overview | 
    
    
    $Country = principal.ip_geo_artifact.location.country_or_region
    $Country != ""
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(principal.ip_geo_artifact.location.region_latitude)
      $Longitude = max(principal.ip_geo_artifact.location.region_longitude)
    
    order:
      $Count desc  
  
Top 10 Destination Hostnames | 
    
    
    $Destination_Hostname = strings.coalesce(target.hostname,target.asset.hostname)
    $Log_Type = metadata.log_type
    
    match:
      $Destination_Hostname, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Decoy's Kill Chain Phase Breakdown (Zscaler Deception) | 
    
    
    $Kill_Chain = strings.coalesce(additional.fields["kill_chain_phase"],extracted.fields["kill_chain_phase"])
    $Decoy_Server = strings.coalesce(additional.fields["decoy_recon_server_type"],extracted.fields["decoy_recon_server_type"])
    $Attack_Type = strings.coalesce(additional.fields["decoy_recon_dataset_type"],extracted.fields["decoy_recon_dataset_type"])
    $Source_User = strings.coalesce(principal.user.user_display_name, principal.user.userid, principal.user.email_addresses)
    $Destination_Hostname = strings.coalesce(target.hostname, target.asset.hostname)
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Destination_IP = strings.coalesce(target.ip, target.asset.ip)
    $Log_Type = metadata.log_type
    
    match:
      $Kill_Chain ,$Decoy_Server ,$Attack_Type, $Destination_Hostname, $Source_User, $Source_IP, $Destination_IP, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
Top 10 Source Users | 
    
    
    $Source_User = strings.coalesce(principal.user.userid, principal.user.email_addresses, principal.user.user_display_name)
    $Log_Type = metadata.log_type
    
    match:
      $Source_User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Event Types by Log Type | 
    
    
    $Log_Type = metadata.log_type
    $Event_Type = metadata.event_type
    
    match:
      $Event_Type, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Targeted Decoy Resource Types (Zscaler Deception) | 
    
    
    $Resource_Type = target.resource.type
    $Destination_Hostname = strings.coalesce(target.hostname, target.asset.hostname)
    
    match:
      $Resource_Type, $Destination_Hostname
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Decoys with High-Risk Scores (Zscaler Deception) | 
    
    
    $Decoy_Server = strings.coalesce(additional.fields["decoy_recon_server_type"], extracted.fields["decoy_recon_server_type"])
    $Attack_Type = strings.coalesce(additional.fields["decoy_recon_dataset_type"], extracted.fields["decoy_recon_dataset_type"])
    $Risk_Score = security_result.risk_score
    $Log_Type = metadata.log_type
    
    match:
      $Decoy_Server, $Attack_Type , $Risk_Score, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Risk_Score desc
    
    limit :
        10  
  
Activity Breakdown by Decoy Network (Zscaler Deception) | 
    
    
    $Decoy_Network = strings.coalesce(additional.fields["decoy_network_name"],extracted.fields["decoy_network_name"])
    $Attack_Type = strings.coalesce(additional.fields["decoy_recon_dataset_type"],extracted.fields["decoy_recon_dataset_type"])
    $Log_Type = metadata.log_type
    
    match:
      $Decoy_Network, $Attack_Type, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
Events by Severity | 
    
    
    $Severity = security_result.severity
    
    match:
      $Severity
    
    outcome:
      $Count = count(metadata.id)  
  
## EDR Alerts Overview

This dashboard provides a comprehensive view of assets, events, and active threat detections which offers enhanced visibility and control.

Top 10 EDR AlertsTotal EDR AlertsActive EDR SensorsTop 10 Hosts based on EDR AlertsNumber of EDR SensorsTop 10 TechniquesSeverity based on EDR AlertsTop 10 TacticsTotal EDR Alerts Over TimeTop 10 Users based on EDR Alerts

Chart name | Query example  
---|---  
Top 10 EDR Alerts | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $Log_Type = $event.metadata.log_type
    $Detection = $event.security_result.summary
    $Detection != ""
    
    match:
      $Detection, $Log_Type
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Top 10 EDR Alerts | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $Log_Type = $event.metadata.log_type
    $Detection = $event.security_result.summary
    $Detection != ""
    
    match:
      $Detection, $Log_Type
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Total EDR Alerts | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    outcome:
      $Count = count($event.security_result.summary)  
  
Active EDR Sensors | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $EDR_Asset = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    $EDR_Asset != ""
    
    match:
      $EDR_Asset
    limit:
        50  
  
Top 10 Hosts based on EDR Alerts | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $Hostname = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    $Hostname != ""
    
    match:
      $Hostname
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Number of EDR Sensors | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    outcome:
      $Count = count_distinct(strings.coalesce($event.principal.asset.hostname, $event.principal.hostname))
      
  
Top 10 Techniques | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $Technique_ID = strings.coalesce($event.security_result.attack_details.techniques.id, $event.security_result.detection_fields["Technique ID"])
    $Technique  = strings.coalesce($event.security_result.attack_details.techniques.name, $event.security_result.detection_fields["Technique"])
    $Technique_ID != ""
    $Technique  != ""
    
    match:
      $Technique_ID, $Technique
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Severity based on EDR Alerts | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    $event.security_result.summary != ""
    
    $Severity = $event.security_result.severity
    
    match:
      $Severity
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Severity asc
    limit:
        10  
  
Severity based on EDR Alerts | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    $event.security_result.summary != ""
    
    $Severity = $event.security_result.severity
    
    match:
      $Severity
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Severity asc
    limit:
        10  
  
Top 10 Tactics | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $Tactic_ID = strings.coalesce($event.security_result.attack_details.tactics.id, $event.security_result.detection_fields["Tactic ID"])
    $Tactic_Name = strings.coalesce($event.security_result.attack_details.tactics.name, $event.security_result.detection_fields["Tactic"])
    $Tactic_ID != ""
    $Tactic_Name != ""
    
    match:
      $Tactic_ID, $Tactic_Name
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Total EDR Alerts Over Time | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $Log_Type = $event.metadata.log_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Date asc  
  
Active EDR Sensors | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $EDR_Asset = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    $EDR_Asset != ""
    
    match:
      $EDR_Asset
    limit:
        50  
  
Total EDR Alerts Over Time | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $Log_Type = $event.metadata.log_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Date asc  
  
Top 10 Techniques | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $Technique_ID = strings.coalesce($event.security_result.attack_details.techniques.id, $event.security_result.detection_fields["Technique ID"])
    $Technique  = strings.coalesce($event.security_result.attack_details.techniques.name, $event.security_result.detection_fields["Technique"])
    $Technique_ID != ""
    $Technique  != ""
    
    match:
      $Technique_ID, $Technique
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Users based on EDR Alerts | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $User = $event.principal.user.user_display_name
    $User != ""
    
    match:
      $User
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Users based on EDR Alerts | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $User = $event.principal.user.user_display_name
    $User != ""
    
    match:
      $User
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Tactics | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $Tactic_ID = strings.coalesce($event.security_result.attack_details.tactics.id, $event.security_result.detection_fields["Tactic ID"])
    $Tactic_Name = strings.coalesce($event.security_result.attack_details.tactics.name, $event.security_result.detection_fields["Tactic"])
    $Tactic_ID != ""
    $Tactic_Name != ""
    
    match:
      $Tactic_ID, $Tactic_Name
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Total EDR Alerts | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    outcome:
      $Count = count($event.security_result.summary)  
  
Number of EDR Sensors | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    outcome:
      $Count = count_distinct(strings.coalesce($event.principal.asset.hostname, $event.principal.hostname))
      
  
Top 10 Hosts based on EDR Alerts | 
    
    
    $event.metadata.log_type = /LIMACHARLIE_EDR|CS_EDR|CS_DETECTS|ESET_EDR|CHECKPOINT_EDR|SOPHOS_EDR|OSQUERY_EDR|DIGITALGUARDIAN_EDR|SENTINEL_DV|MICROSOFT_DEFENDER_ENDPOINT|SENTINEL_EDR|UPTYCS_EDR|SYMANTEC_EDR|FORTINET_FORTIEDR|REDCANARY_EDR|CYBEREASON_EDR|MICROSOFT_DEFENDER_IDENTITY|DEEP_INSTINCT_EDR|CB_EDR|PAN_EDR|FIREEYE_HX|WATCHGUARD_EDR/ nocase
    
    $Hostname = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    $Hostname != ""
    
    match:
      $Hostname
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
## Email Activity Overview

This dashboard provides a detailed summary of email traffic, including total volumes, allowed versus blocked emails, unique senders, unique recipients, and key statistics on top senders and recipients. It provides valuable insights into communication patterns and enhances email security, filtering effectiveness, and overall email management.

Recent Email EventsBlocked EmailsTop 5 Recipients by Log TypeAllowed Email EventsTotal Email EventsTop 10 Email Log Source by Event TypeTop 5 Senders by Log TypeUnique SendersUnique Recipients

Chart name | Query example  
---|---  
Recent Email Events | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    $Sender = $event.network.email.from
    $Recipient = $event.network.email.to
    $Subject = $event.network.email.subject
    $Subject != ""
    $Date = timestamp.get_timestamp($event.metadata.event_timestamp.seconds)
    $Action = $event.security_result.action
    
    match:
      $Date, $Sender, $Recipient, $Subject, $Action
    order:
      $Date desc
    limit:
        50  
  
Blocked Emails | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    $event.security_result.action = "BLOCK"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Top 5 Recipients by Log Type | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    $Log_Type = $event.metadata.log_type
    $Recipients = $event.network.email.to
    $Recipients != ""
    
    match:
      $Log_Type, $Recipients
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        5   
  
Allowed Email Events | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    $event.security_result.action = "ALLOW"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Top 5 Recipients by Log Type | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    $Log_Type = $event.metadata.log_type
    $Recipients = $event.network.email.to
    $Recipients != ""
    
    match:
      $Log_Type, $Recipients
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        5   
  
Total Email Events | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Top 10 Email Log Source by Event Type | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    $Event_Type = $event.metadata.event_type
    $Log_Type = $event.metadata.log_type
    
    match:
      $Log_Type, $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Allowed Email Events | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    $event.security_result.action = "ALLOW"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Top 5 Senders by Log Type | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    $Log_Type = $event.metadata.log_type
    $Sender = $event.network.email.from
    $Sender != ""
    
    match:
      $Log_Type, $Sender
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        5  
  
Unique Senders | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    outcome:
      $Count = count_distinct($event.network.email.from)  
  
Unique Senders | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    outcome:
      $Count = count_distinct($event.network.email.from)  
  
Total Email Events | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Top 5 Senders by Log Type | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    $Log_Type = $event.metadata.log_type
    $Sender = $event.network.email.from
    $Sender != ""
    
    match:
      $Log_Type, $Sender
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        5  
  
Recent Email Events | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    $Sender = $event.network.email.from
    $Recipient = $event.network.email.to
    $Subject = $event.network.email.subject
    $Subject != ""
    $Date = timestamp.get_timestamp($event.metadata.event_timestamp.seconds)
    $Action = $event.security_result.action
    
    match:
      $Date, $Sender, $Recipient, $Subject, $Action
    order:
      $Date desc
    limit:
        50  
  
Unique Recipients | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    outcome:
      $Count = count_distinct($event.network.email.to)  
  
Blocked Emails | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    $event.security_result.action = "BLOCK"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Unique Recipients | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    outcome:
      $Count = count_distinct($event.network.email.to)  
  
Top 10 Email Log Source by Event Type | 
    
    
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    
    $Event_Type = $event.metadata.event_type
    $Log_Type = $event.metadata.log_type
    
    match:
      $Log_Type, $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
## Email Security Overview

This dashboard provides information anout email threats like phishing, malware, ransomware, and Business Email Compromise (BEC). It provides an overview of security related events, malicious senders, source IPs, and targeted email addresses.

Top 10 Identified DomainsTotal Phishing DetectedEmail Category Over TimeTop 10 Suspicious URLsPhishing DetectedTop 10 Malicious Source IPsEmail Threats by CategoryAction Taken Over TimeEmail Threat Identified Over TimeRecent Active ThreatsBlocked vs. Permitted URLsTop 10 Malicious SendersRecent Malicious AttachmentsTop 10 Targeted EmailsTop 10 High Severity ThreatsTop 10 Malicious LocationsTop 10 Email Threats by SeverityThreat Status DistributionSecurity Results Action Distribution

Chart name | Query example  
---|---  
Top 10 Identified Domains | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.principal.administrative_domain != ""
    
    $Domain = $event.principal.administrative_domain
    
    match:
      $Domain
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Total Phishing Detected | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.category = "MAIL_PHISHING"
    
    outcome:
      $Count = count_distinct($event.principal.user.email_addresses)  
  
Email Category Over Time | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Category = $event.security_result.category
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Category
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Top 10 Suspicious URLs | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $event.security_result.category = "MAIL_PHISHING"
    or $event.security_result.category = "MAIL_SPAM"
    or $event.security_result.category = "MAIL_SPOOFING"
    or $event.security_result.category = "SOFTWARE_MALICIOUS"
    strings.coalesce($event.target.url, $event.security_result.about.url,$event.security_result.detection_fields["detectedUrls"]) != ""
    
    $URL = strings.coalesce($event.target.url, $event.security_result.about.url,$event.security_result.detection_fields["detectedUrls"])
    
    match:
      $URL
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Phishing Detected | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.category = "MAIL_PHISHING"
    
    $Email = $event.principal.user.email_addresses
    
    match:
      $Email  
  
Top 10 Malicious Source IPs | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.detection_fields["judgement"] = /MALICIOUS/ nocase
    $event.principal.ip != ""
    
    $Source_IP = $event.principal.ip
    
    match:
      $Source_IP
    outcome:
      $Count = count($event.principal.ip)
    order:
      $Count desc
    limit:
        10  
  
Email Threats by Category | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    
    $Threat_Name = $event.security_result.category_details
    $Category = $event.security_result.category
    
    match:
      $Threat_Name, $Category
    outcome:
      $Count = count($event.security_result.threat_name)
    order:
      $Count desc
    limit:
        50   
  
Action Taken Over Time | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Action = $event.security_result.action
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc
    
      
  
Email Threat Identified Over Time | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Threat_Name = $event.security_result.threat_name
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Threat_Name
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc   
  
Email Threat Identified Over Time | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Threat_Name = $event.security_result.threat_name
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Threat_Name
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc   
  
Recent Active Threats | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Threat_Name = $event.security_result.threat_name
    $Status = $event.security_result.threat_status
    
    match:
      $Threat_Name, $Status
    outcome:
      $Count = count($event.metadata.id)
      $Date = timestamp.get_timestamp(max($event.metadata.event_timestamp.seconds))
    order:
      $Date desc
    limit:
        50
      
  
Blocked vs. Permitted URLs | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.action = "ALLOW"
    or $event.security_result.action = "BLOCK"
    
    $Action = $event.security_result.action
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    outcome:
      $Count = count($event.target.url)
    order:
      $Count desc  
  
Phishing Detected | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.category = "MAIL_PHISHING"
    
    $Email = $event.principal.user.email_addresses
    
    match:
      $Email  
  
Top 10 Malicious Senders | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.detection_fields["judgement"] = /MALICIOUS/ nocase
    $event.network.email.from != ""
    
    $Sender = $event.network.email.from
    
    match:
      $Sender
    outcome:
      $Count = count($event.network.email.from)
    order:
      $Count desc
    limit:
        10  
  
Recent Malicious Attachments | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    strings.coalesce($event.about.file.full_path, $event.security_result.detection_fields["attachmentNames"]) != ""
    
    $Attachment = strings.coalesce($event.about.file.full_path, $event.security_result.detection_fields["attachmentNames"])
    $Category = $event.security_result.category
    $Sender = $event.network.email.from
    $Receiver = $event.network.email.to
    $Status = $event.additional.fields["remediationStatus"]
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Sender, $Receiver, $Attachment, $Category, $Status
    order:
      $Date desc
    limit:
        50  
  
Total Phishing Detected | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.category = "MAIL_PHISHING"
    
    outcome:
      $Count = count_distinct($event.principal.user.email_addresses)  
  
Top 10 Targeted Emails | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.target.user.email_addresses != ""
    
    $Target = $event.target.user.email_addresses
    
    match:
      $Target
    outcome:
      $Count = count($event.target.user.email_addresses)
    order:
      $Count desc
    limit:
        10  
  
Email Category Over Time | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Category = $event.security_result.category
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Category
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Top 10 Suspicious URLs | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $event.security_result.category = "MAIL_PHISHING"
    or $event.security_result.category = "MAIL_SPAM"
    or $event.security_result.category = "MAIL_SPOOFING"
    or $event.security_result.category = "SOFTWARE_MALICIOUS"
    strings.coalesce($event.target.url, $event.security_result.about.url,$event.security_result.detection_fields["detectedUrls"]) != ""
    
    $URL = strings.coalesce($event.target.url, $event.security_result.about.url,$event.security_result.detection_fields["detectedUrls"])
    
    match:
      $URL
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Action Taken Over Time | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Action = $event.security_result.action
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc
    
      
  
Top 10 High Severity Threats | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.category_details != ""
    $event.security_result.severity = "HIGH"
    
    $Category = $event.security_result.category_details
    $Category != ""
    
    match:
       $Category
    outcome:
       $Count = count($event.metadata.id)
    order:
       $Count desc
    limit:
        10   
  
Top 10 Malicious Source IPs | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.detection_fields["judgement"] = /MALICIOUS/ nocase
    $event.principal.ip != ""
    
    $Source_IP = $event.principal.ip
    
    match:
      $Source_IP
    outcome:
      $Count = count($event.principal.ip)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Malicious Senders | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.detection_fields["judgement"] = /MALICIOUS/ nocase
    $event.network.email.from != ""
    
    $Sender = $event.network.email.from
    
    match:
      $Sender
    outcome:
      $Count = count($event.network.email.from)
    order:
      $Count desc
    limit:
        10  
  
Blocked vs. Permitted URLs | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.action = "ALLOW"
    or $event.security_result.action = "BLOCK"
    
    $Action = $event.security_result.action
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    outcome:
      $Count = count($event.target.url)
    order:
      $Count desc  
  
Recent Malicious Attachments | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    strings.coalesce($event.about.file.full_path, $event.security_result.detection_fields["attachmentNames"]) != ""
    
    $Attachment = strings.coalesce($event.about.file.full_path, $event.security_result.detection_fields["attachmentNames"])
    $Category = $event.security_result.category
    $Sender = $event.network.email.from
    $Receiver = $event.network.email.to
    $Status = $event.additional.fields["remediationStatus"]
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Sender, $Receiver, $Attachment, $Category, $Status
    order:
      $Date desc
    limit:
        50  
  
Top 10 Malicious Locations | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.detection_fields["judgement"] = /MALICIOUS/ nocase
    $event.principal.location.country_or_region != ""
    
    $Countries = $event.principal.location.country_or_region
    $Latitude = $event.principal.location.region_coordinates.latitude
    $Longitude = $event.principal.location.region_coordinates.longitude
    
    match:
      $Countries, $Latitude, $Longitude
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Email Threats by Category | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    
    $Threat_Name = $event.security_result.category_details
    $Category = $event.security_result.category
    
    match:
      $Threat_Name, $Category
    outcome:
      $Count = count($event.security_result.threat_name)
    order:
      $Count desc
    limit:
        50   
  
Top 10 Email Threats by Severity | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.category_details != ""
    
    $Severity = $event.security_result.severity
    $Threat_Name = $event.security_result.category_details
    $Threat_Name != ""
    
    match:
      $Threat_Name, $Severity
    outcome:
      $Count = count($event.security_result.severity)
    order:
      $Count desc
    limit:
        10  
  
Recent Active Threats | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Threat_Name = $event.security_result.threat_name
    $Status = $event.security_result.threat_status
    
    match:
      $Threat_Name, $Status
    outcome:
      $Count = count($event.metadata.id)
      $Date = timestamp.get_timestamp(max($event.metadata.event_timestamp.seconds))
    order:
      $Date desc
    limit:
        50
      
  
Threat Status Distribution | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Status = $event.security_result.threat_status
    
    match:
      $Status
    outcome:
      $Count = count($event.security_result.threat_name)
    order:
      $Count desc   
  
Security Results Action Distribution | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Action = $event.security_result.action
    
    match:
      $Action
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc  
  
Security Results Action Distribution | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Action = $event.security_result.action
    
    match:
      $Action
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc  
  
Top 10 Targeted Emails | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.target.user.email_addresses != ""
    
    $Target = $event.target.user.email_addresses
    
    match:
      $Target
    outcome:
      $Count = count($event.target.user.email_addresses)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Malicious Locations | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.detection_fields["judgement"] = /MALICIOUS/ nocase
    $event.principal.location.country_or_region != ""
    
    $Countries = $event.principal.location.country_or_region
    $Latitude = $event.principal.location.region_coordinates.latitude
    $Longitude = $event.principal.location.region_coordinates.longitude
    
    match:
      $Countries, $Latitude, $Longitude
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 High Severity Threats | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.category_details != ""
    $event.security_result.severity = "HIGH"
    
    $Category = $event.security_result.category_details
    
    match:
       $Category
    outcome:
       $Count = count($event.metadata.id)
    order:
       $Count desc
    limit:
        10   
  
Threat Status Distribution | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    
    $Status = $event.security_result.threat_status
    
    match:
      $Status
    outcome:
      $Count = count($event.security_result.threat_name)
    order:
      $Count desc   
  
Top 10 Email Threats by Severity | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.category_details != ""
    
    $Severity = $event.security_result.severity
    $Threat_Name = $event.security_result.category_details
    
    match:
      $Threat_Name, $Severity
    outcome:
      $Count = count($event.security_result.severity)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Identified Domains | 
    
    
    $event.metadata.log_type = /ABNORMAL_SECURITY|AREA1|AVANAN_EMAIL|BARRACUDA_EMAIL|CISCO_EMAIL_SECURITY|COFENSE_TRIAGE|EXCHANGE_MAIL|FIREEYE_EMPS|FIREEYE_ETP|FORCEPOINT_EMAILSECURITY|FORCEPOINT_MAIL_RELAY|FORTINET_FORTIMAIL|KNOWBE4_PHISHER|MAILMARSHAL|MICROSOFT_DEFENDER_MAIL|MIMECAST_MAIL|MIMECAST_URL_LOGS|OBSERVEIT|OFFICE_365|POSTFIX_MAIL|PROOFPOINT_MAIL|PROOFPOINT_MAIL_FILTER|PROOFPOINT_ON_DEMAND|PROOFPOINT_SENDMAIL_SENTRION|PROOFPOINT_SER|PROOFPOINT_TAP_FORENSICS|PROOFPOINT_TRAP|SENDMAIL|SEPPMAIL|SYMANTEC_VIP|VIRTRU_EMAIL_ENCRYPTION|VOLTAGE|WORKSPACE_ALERTS|ZIX_EMAIL_ENCRYPTION|PHISHLABS/ nocase
    $event.metadata.event_type = "EMAIL_UNCATEGORIZED"
    or $event.metadata.event_type = "EMAIL_TRANSACTION"
    or $event.metadata.event_type = "NETWORK_HTTP"
    $event.principal.administrative_domain != ""
    
    $Domain = $event.principal.administrative_domain
    
    match:
      $Domain
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
## FEDRAMP Continuous Monitoring

This dashboard provides a clear view of system compliance and security posture. It tracks vulnerabilities, and control effectiveness against FedRAMP standards, helping you stay compliant and prioritize remediation efforts.

Total Inbound Connections Systems with Available UpdatesRecent Media Protection Vendor AlertsTop 10 Blocked DomainsNetwork Traffic Over Time by DirectionVulnerabilities by SeverityTop 10 Blocked Application Executions By ReasonWeak TLS Version Usage Over TimeSign Ins by Status Over TimeMFA Enrollment StatusTop 10 Endpoints by High Severity AlertsTop 10 Inbound IP AddressMedia Protection Vendor Alerts by Action Over TimeTop 10 Recent User Badge-InsHigh Severity Endpoint Detections Over TimeTotal Outbound ConnectionsTop 10 Users by Failed Sign InsTLS Cipher DistributionDLP Violations by SeverityVulnerabilities by AgeUser Accounts Change PermissionsTop 10 Outbound IP AddressTop 10 Users by Privileged Actions

Chart name | Query example  
---|---  
Total Inbound Connections  | 
    
    
    metadata.event_type = "NETWORK_CONNECTION"
    network.direction = "INBOUND"
    
    outcome:
      $Count = count_distinct(principal.ip)  
  
Systems with Available Updates | 
    
    
    metadata.product_event_type = "40"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    
    match:
      $Hostname, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Recent Media Protection Vendor Alerts | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary) = /\busb|removable|drive\b/ nocase
    
    $Vendor_Alert = strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary)
    $User = strings.coalesce(principal.user.user_display_name, target.user.user_display_name)
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $File_Name = target.file.full_path
    $Action = security_result.action
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Vendor_Alert, $Source_IP, $User, $File_Name, $Action
    
    order:
      $Date desc  
  
Top 10 Blocked Domains | 
    
    
    security_result.action = "BLOCK"
    
    $Destination_Domain = strings.coalesce(target.administrative_domain, about.administrative_domain, target.ip_geo_artifact.network.dns_domain)
    $Destination_Domain != ""
    
    match:
      $Destination_Domain
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Network Traffic Over Time by Direction | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Direction = network.direction
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Direction, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Vulnerabilities by Severity | 
    
    
    $Severity =
        if (principal.asset.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            principal.asset.vulnerabilities.severity,
        if (target.asset.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            target.asset.vulnerabilities.severity,
        if (extensions.vulns.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            extensions.vulns.vulnerabilities.severity,
        "UNKNOWN_SEVERITY")))
    
    match:
      $Severity
    
    outcome:
      $Event_Count = count(strings.coalesce(extensions.vulns.vulnerabilities.name, extensions.vulns.vulnerabilities.description, extensions.vulns.vulnerabilities.vendor_vulnerability_id, principal.asset.vulnerabilities.name, target.asset.vulnerabilities.name, additional.fields["ScanReference"]))
    
    order:
      $Severity desc  
  
Top 10 Blocked Application Executions By Reason | 
    
    
    metadata.product_event_type = /(execution|application) block/ nocase
    or security_result.threat_name = /application control/ nocase
    security_result.action = "BLOCK"
    
    $Application = strings.coalesce(about.file.full_path, target.process.file.full_path, additional.fields["fname"])
    $Reason = strings.coalesce(target.resource.attribute.labels["categoryTupleDescription"], security_result.action_details, metadata.product_event_type)
    
    match:
      $Application, $Reason
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Weak TLS Version Usage Over Time | 
    
    
    network.tls.version != /1(\.|_)?(2|3)/ nocase
    
    $Cipher_Version = network.tls.version
    $Cipher_Version != ""
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Cipher_Version, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Sign Ins by Status Over Time | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Action, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
MFA Enrollment Status | 
    
    
    metadata.product_name  = "MULTI-FACTOR_AUTHENTICATION"
    or strings.coalesce(additional.fields["AuthenticationRequirement"], security_result.detection_fields.value) = /mfa|multi(?:\s|\S)?factor(?:\s|\S)?authentication|/ nocase
    
    metadata.product_event_type = "enrollment"
    or target.resource_ancestors.resource_subtype = "AuthenticatorEnrollment"
    
    $Result = security_result.summary
    
    match:
      $Result
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Endpoints by High Severity Alerts | 
    
    
    principal.hostname != ""
    
    $Hostname = principal.hostname
    $Severity = security_result.severity
    $Severity = "CRITICAL" or $Severity = "HIGH"
    
    match:
      $Hostname, $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Inbound IP Address | 
    
    
    network.direction = "INBOUND"
    
    $Log_Type = metadata.log_type
    $Source_IP = principal.ip
    
    match:
      $Log_Type, $Source_IP
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Media Protection Vendor Alerts by Action Over Time | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary) = /\busb|removable|drive\b/ nocase
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Recent User Badge-Ins | 
    
    
    (metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_UNCATEGORIZED")
    strings.coalesce(metadata.description, security_result.action_details, security_result.description, security_result.summary, additional.fields["plasectrxEvtypename"]) = /(?:access\sgranted|badge\sin)/ nocase
    
    $User = strings.coalesce(principal.user.user_display_name, principal.user.email_addresses, additional.fields["person"], principal.user.userid)
    $Location = strings.coalesce(security_result.rule_labels["Place"], additional.fields["site"], target.location.name, principal.resource.name)
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %H:%M:%S ")
    
    match:
      $Date, $User, $Location
    
    order:
      $Date desc
    
    limit:
        10  
  
High Severity Endpoint Detections Over Time | 
    
    
    principal.hostname != ""
    
    $Severity = security_result.severity
    $Severity = "CRITICAL" or $Severity = "HIGH"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
       $Severity, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Total Outbound Connections | 
    
    
    metadata.event_type = "NETWORK_CONNECTION"
    network.direction = "OUTBOUND"
    
    outcome:
      $Count = count_distinct(target.ip)  
  
Top 10 Users by Failed Sign Ins | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "BLOCK"
    target.user.userid != ""
    
    $User = target.user.userid
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
TLS Cipher Distribution | 
    
    
    network.tls.cipher != /1(\.|_)?(2|3)/ nocase
    
    $TLS_Cipher = network.tls.cipher
    $TLS_Cipher != ""
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $TLS_Cipher, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
DLP Violations by Severity | 
    
    
    metadata.log_type = /DLP/ nocase
    metadata.product_event_type = /Violation/ nocase
    
    $Severity = security_result.severity
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Severity desc  
  
Vulnerabilities by Age | 
    
    
    (timestamp.as_unix_seconds(additional.fields["first_found"]) > 0
    or extensions.vulns.vulnerabilities.first_found.seconds > 0
    or principal.asset.vulnerabilities.first_found.seconds > 0)
    
    $Vulnerability = strings.coalesce(
      if(principal.asset.vulnerabilities.name != "" and principal.asset.vulnerabilities.description != "",
        strings.concat(principal.asset.vulnerabilities.name, " : ", principal.asset.vulnerabilities.description),
        strings.coalesce(principal.asset.vulnerabilities.name, principal.asset.vulnerabilities.description)),
      if(additional.fields["ScanReference"] != "" and metadata.description != "",
        strings.concat(additional.fields["ScanReference"], " : ", metadata.description),
        strings.coalesce(additional.fields["ScanReference"], metadata.description)),
      if(extensions.vulns.vulnerabilities.vendor_vulnerability_id != "" and extensions.vulns.vulnerabilities.description != "",
        strings.concat(extensions.vulns.vulnerabilities.vendor_vulnerability_id, " : ", extensions.vulns.vulnerabilities.description),
        strings.coalesce(extensions.vulns.vulnerabilities.vendor_vulnerability_id, extensions.vulns.vulnerabilities.description)
      )
    )
    
    $Vulnerability != " : "
    $Vulnerability != ""
    $Log_Type = metadata.log_type
    
    match:
      $Vulnerability, $Log_Type
    
    outcome:
      $Age = max(cast.as_int((metadata.event_timestamp.seconds - if(timestamp.as_unix_seconds(additional.fields["first_found"]) > 0, timestamp.as_unix_seconds(additional.fields["first_found"]), if(extensions.vulns.vulnerabilities.first_found.seconds > 0, extensions.vulns.vulnerabilities.first_found.seconds, if(principal.asset.vulnerabilities.first_found.seconds > 0, principal.asset.vulnerabilities.first_found.seconds, metadata.event_timestamp.seconds)))) / 86400))
      $Days_Range = if($Age <= 30, "0-30 Days",
                     if($Age <= 60, "31-60 Days",
                     if($Age <= 90, "61-90 Days", "> 90 Days")))
      $Count = count(strings.coalesce(extensions.vulns.vulnerabilities.name, extensions.vulns.vulnerabilities.description, extensions.vulns.vulnerabilities.vendor_vulnerability_id, principal.asset.vulnerabilities.name, additional.fields["ScanReference"]))
    
    order:
      $Age desc  
  
User Accounts Change Permissions | 
    
    
    metadata.event_type = "USER_CHANGE_PERMISSIONS"
    principal.user.userid != ""
    
    outcome:
      $Count = count_distinct(metadata.id)  
  
Top 10 Outbound IP Address | 
    
    
    network.direction = "OUTBOUND"
    
    $Log_Type = metadata.log_type
    $Destination_IP = target.ip
    
    match:
      $Log_Type, $Destination_IP
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users by Privileged Actions | 
    
    
    principal.user.attribute.roles.type = "ADMINISTRATOR"
    or strings.coalesce(principal.user.attribute.roles.name, principal.user.userid) = /Admin|Root|Super/ nocase
    
    $User = principal.user.userid
    $Action = metadata.product_event_type
    
    match:
      $User, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
## Firewall Activity Monitoring

This dashboard provides information about firewall activity to enhance security and performance management. It provides real-time insights into network security by tracking various metrics and events related to firewall activity, helping users to effectively manage and respond to potential threats.

Rare Firewall Rules TriggeredTop 10 Firewall Rules TriggeredConnections by Geo LocationTop Connection DestinationsData Inflow by IPData Outflow by IPTop Connection sourcesBlocked vs. Allowed TrafficTop 10 Blocked IPs

Chart name | Query example  
---|---  
Rare Firewall Rules Triggered | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $rule_name !=""
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $rule_name
    outcome:
    $Count = count($rule_name)
    order: $Count asc
    limit: 10  
  
Top 10 Firewall Rules Triggered | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $rule_name !=""
    match:
    $rule_name
    outcome:
    $Count = count(metadata.id)
    order: $Count desc
    limit: 10  
  
Connections by Geo Location | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $rule_name !=""
    $country = principal.location.country_or_region
    $country != ""
    $direction = network.direction
    match:
    $country
    outcome:
    $event_count = count_distinct($country)
    $latitude = max(principal.location.region_coordinates.latitude)
    $longitude = max(principal.location.region_coordinates.longitude)  
  
Top Connection Destinations | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $Dest_IP = target.ip
    $Dest_IP != ""
    match:
    $Dest_IP
    outcome:
    $event_count = count(metadata.id)
    order: $event_count desc
    limit: 10
      
  
Data Inflow by IP | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $ruleN = security_result.rule_name
    $IP = principal.ip
    $byte = network.received_bytes
    $byte != 0
    $Vendor = metadata.vendor_name
    $Vendor != ""
    match:
    $IP, $Vendor
    outcome:
    $byte_sum=sum($byte)
    $Data_in_mb = math.round($byte_sum/1048576)
    order: $Data_in_mb desc
    limit: 10  
  
Connections by Geo Location | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $rule_name !=""
    $country = principal.location.country_or_region
    $country != ""
    $direction = network.direction
    match:
    $country
    outcome:
    $event_count = count_distinct($country)
    $latitude = max(principal.location.region_coordinates.latitude)
    $longitude = max(principal.location.region_coordinates.longitude)  
  
Data Outflow by IP | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $IP = principal.ip
    $byte = network.sent_bytes
    $byte != 0
    $Vendor = metadata.vendor_name
    metadata.vendor_name != ""
    match:
    $IP, $Vendor
    outcome:
    $byte_sum=sum($byte)
    $data_in_mb = math.round($byte_sum/1048576)
    order: $data_in_mb desc
    limit:10
      
  
Rare Firewall Rules Triggered | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $rule_name !=""
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $rule_name
    outcome:
    $Count = count($rule_name)
    order: $Count asc
    limit: 10  
  
Top Connection sources | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $Src_IP = principal.ip
    match:
    $Src_IP
    outcome:
    $event_count = count(metadata.id)
    order: $event_count desc
    limit: 10
      
  
Blocked vs. Allowed Traffic | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $action = security_result.action
    $action = "BLOCK" OR $action = "ALLOW"
    match:
    $action
    outcome:
    $event_count = count(metadata.id)
    order: $event_count desc  
  
Top 10 Firewall Rules Triggered | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $rule_name !=""
    match:
    $rule_name
    outcome:
    $Count = count(metadata.id)
    order: $Count desc
    limit: 10  
  
Blocked vs. Allowed Traffic | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $action = security_result.action
    $action = "BLOCK" OR $action = "ALLOW"
    match:
    $action
    outcome:
    $event_count = count(metadata.id)
    order: $event_count desc  
  
Data Outflow by IP | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $IP = principal.ip
    $byte = network.sent_bytes
    $byte != 0
    $Vendor = metadata.vendor_name
    metadata.vendor_name != ""
    match:
    $IP, $Vendor
    outcome:
    $byte_sum=sum($byte)
    $data_in_mb = math.round($byte_sum/1048576)
    order: $data_in_mb desc
    limit:10
      
  
Data Inflow by IP | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $ruleN = security_result.rule_name
    $IP = principal.ip
    $byte = network.received_bytes
    $byte != 0
    $Vendor = metadata.vendor_name
    $Vendor != ""
    match:
    $IP, $Vendor
    outcome:
    $byte_sum=sum($byte)
    $Data_in_mb = math.round($byte_sum/1048576)
    order: $Data_in_mb desc
    limit: 10  
  
Top Connection sources | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $Src_IP = principal.ip
    $Src_IP != ""
    match:
    $Src_IP
    outcome:
    $event_count = count(metadata.id)
    order: $event_count desc
    limit: 10
      
  
Top Connection Destinations | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $Dest_IP = target.ip
    $Dest_IP != "EMPTY"
    match:
    $Dest_IP
    outcome:
    $event_count = count(metadata.id)
    order: $event_count desc
    limit: 10
      
  
Top 10 Blocked IPs | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $action = security_result.action
    $action = "BLOCK"
    $IP = principal.ip
    match:
    $IP, $action
    outcome:
    $event_count = count_distinct(metadata.id)
    order: $event_count desc
    limit: 10  
  
Top 10 Blocked IPs | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $log_type = metadata.log_type
    $rule_name = security_result.rule_name
    $action = security_result.action
    $action = "BLOCK"
    $IP = principal.ip
    match:
    $IP, $action
    outcome:
    $event_count = count_distinct(metadata.id)
    order: $event_count desc
    limit: 10  
  
## GDPR Data Governance

This dashboard provides visibility into data access across EU regions, including access trends, non-EU access attempts, and top geolocations. It helps monitor compliance with GDPR regulations, detect unauthorized data access, and ensure secure handling of EU data.

**Note:** Apply filters to display relevant results.

Privileged Accounts Accessing EU ResourcesWeak TLS Version DistributionTop 10 Non EU IPs Accessing EU ResourcesTop 10 Users Accessing EU ResourcesEU Data Access by Source GeolocationData Deletion and Purge Events on EU Resources Over TimeWeak Encryption On EU Resources Over TimeData Deletion and Purge Events on EU ResourcesTop 10 Privileged Accounts Accessing EU ResourcesEU-Based DLP EventsTop 10 External Domains Receiving EU DataMalware File SummaryEU-Based DLP Events Over TimeEU Data Access Events Over TimeTop 10 Policies TriggeredUnauthorized Access to EU ResourcesAccess to EU Resources from Non-EU CountriesTop 10 Non-EU Countries Accessing EU DataPrivileged Access to EU Resources Over TimeThreat Detection Over TimeSensitive Data Access Events

Chart name | Query example  
---|---  
Privileged Accounts Accessing EU Resources | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.log_type = "GENERIC_EVENT" OR metadata.event_type ="USER_LOGIN" or metadata.log_type = "USER_CHANGE_PERMISSIONS")
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid,target.user.user_display_name,target.user.email_addresses)
    ($User = /admin|root|svc|adm|privilege/ nocase or principal.user.attribute.roles.type = "SERVICE_ACCOUNT" or principal.user.attribute.roles.type = "ADMINISTRATOR" or principal.user.account_type = "DOMAIN_ACCOUNT_TYPE" or principal.user.account_type = "SERVICE_ACCOUNT_TYPE")
    $Target_EU_Country =  strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name)
    $Event_Type = metadata.event_type
    $Source_IP = strings.coalesce(principal.ip,principal.asset.ip)
    $Target_Resource = strings.coalesce(target.resource.name, target.file.full_path, target.resource.product_object_id, target.group.product_object_id, target.user.group_identifiers)
    $Target_Resourcetype = target.resource.resource_type
    $Action = security_result.action
    
    match:
       $Event_Type, $User,$Source_IP, $Target_EU_Country, $Target_Resource, $Target_Resourcetype, $Action
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds))
    
    order:
       $Count desc
    
      
  
Weak TLS Version Distribution | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT")
    
    network.tls.version != /1(\.|_)?(2|3)/ nocase
    
    $TLS_Version = network.tls.version
    $TLS_Version != ""
    
    match:
      $TLS_Version
    
    outcome:
      $Count = count(metadata.id)
       
  
Top 10 Non EU IPs Accessing EU Resources | 
    
    
    (strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    and strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region, principal.location.name) != /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase)
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.log_type = "GENERIC_EVENT" OR metadata.event_type ="USER_LOGIN" or metadata.log_type = "USER_CHANGE_PERMISSIONS")
    
    $Principal_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Principal_IP != ""
    $Principal_Country = strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region, principal.location.name)
    
    match:
      $Principal_IP, $Principal_Country
    
    outcome:
      $Count = count(metadata.id)
    
    order :
      $Count desc
    
    limit:
       10  
  
Top 10 Users Accessing EU Resources | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT")
    
    $User = strings.coalesce(principal.user.user_display_name, principal.user.userid,  principal.user.email_addresses,target.user.userid,target.user.user_display_name,target.user.email_addresses)
    $Source_Country = strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region, principal.location.name)
    $User != ""
    
    match:
      $User, $Source_Country
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
EU Data Access by Source Geolocation | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    principal.ip_geo_artifact.location.region_coordinates.latitude != 0
    principal.ip_geo_artifact.location.region_coordinates.longitude != 0
    
    $Source_Country = strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region, principal.location.name)
    
    match:
      $Source_Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(principal.ip_geo_artifact.location.region_coordinates.latitude)
      $Longitude = max(principal.ip_geo_artifact.location.region_coordinates.longitude)  
  
Data Deletion and Purge Events on EU Resources Over Time | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "FILE_DELETION" or metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" or metadata.event_type = "USER_RESOURCE_DELETION"
     or metadata.product_event_type = /delete|purge/ nocase or security_result.summary = /delete|purge/ nocase or security_result.description = /delete|purge/ nocase)
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Weak Encryption On EU Resources Over Time | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (((target.resource.attribute.labels.key  = "keyProperties_type" or target.resource.attribute.labels.key  = "requestParameters.keySpec" or target.resource.attribute.labels.key = /key/ nocase) and target.resource.attribute.labels.value  = /^(RSA-)|DES|RC4|MD5|SHA1|SHA-1/) or network.tls.cipher = /^(RSA-)|DES|RC4|MD5|SHA1|SHA-1/)
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Data Deletion and Purge Events on EU Resources | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "FILE_DELETION" or metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" or metadata.event_type = "USER_RESOURCE_DELETION"
     or metadata.product_event_type = /delete|purge/ nocase or security_result.summary = /delete|purge/ nocase or security_result.description = /delete|purge/ nocase)
    security_result.action = "ALLOW"
    
    $Description = strings.coalesce(security_result.summary, security_result.description, metadata.description, security_result.action_details)
    $Product_Event_Type = metadata.product_event_type
    $Event_Type = metadata.event_type
    $Log_Type = metadata.log_type
    $Target_Resource = strings.coalesce(target.resource.name, target.file.full_path, target.resource.product_object_id, target.group.product_object_id, target.user.group_identifiers)
    $User = strings.coalesce(principal.user.user_display_name, principal.user.userid, principal.user.email_addresses, target.user.userid,target.user.user_display_name,target.user.email_addresses)
    
    match:
      $User, $Log_Type, $Target_Resource, $Description, $Product_Event_Type, $Event_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds))
      $Count = count(metadata.id)
    
    order:
      $Date desc, $Count desc  
  
Top 10 Privileged Accounts Accessing EU Resources | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT" OR metadata.event_type ="USER_LOGIN" or metadata.event_type = "USER_CHANGE_PERMISSIONS")
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid,target.user.user_display_name,target.user.email_addresses)
    ($User = /admin|root|svc|adm|privilege/ nocase or principal.user.attribute.roles.type = "SERVICE_ACCOUNT" or principal.user.attribute.roles.type = "ADMINISTRATOR" or principal.user.account_type = "DOMAIN_ACCOUNT_TYPE" or principal.user.account_type = "SERVICE_ACCOUNT_TYPE")
    $Target_EU_Country =  strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name)
    
    match:
      $User, $Target_EU_Country
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
EU-Based DLP Events | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT" OR metadata.event_type = "NETWORK_UNCATEGORIZED" OR metadata.event_type = "NETWORK_FLOW" OR metadata.event_type = "NETWORK_CONNECTION" OR metadata.event_type = "NETWORK_FTP" OR metadata.event_type = "NETWORK_DHCP" OR metadata.event_type = "NETWORK_DNS" OR metadata.event_type = "NETWORK_HTTP" OR metadata.event_type = "NETWORK_SMTP")
    
    (metadata.log_type = /DLP|ACCELLION|CODE42_INCYDR|GUARDIUM|TRIPWIRE_FIM/ nocase OR metadata.product_event_type = /dlp/  nocase OR security_result.outcomes.value = /dlp/  nocase OR security_result.rule_type = /dlp/  nocase OR security_result.rule_name = /dlp/  nocase OR security_result.category_details = /dlp|data loss prevention/ nocase OR security_result.category = "DATA_EXFILTRATION" or security_result.category = "DATA_DESTRUCTION")
    
    outcome:
      $Count = count(metadata.id)
      
  
Top 10 External Domains Receiving EU Data | 
    
    
    strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region, principal.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT" OR metadata.event_type = "NETWORK_UNCATEGORIZED" OR metadata.event_type = "NETWORK_FLOW" OR metadata.event_type = "NETWORK_CONNECTION" OR metadata.event_type = "NETWORK_FTP" OR metadata.event_type = "NETWORK_DHCP" OR metadata.event_type = "NETWORK_DNS" OR metadata.event_type = "NETWORK_HTTP"
    OR metadata.event_type = "NETWORK_SMTP")
    network.direction = "OUTBOUND"
    network.sent_bytes > 0
    
    $Target_Domain = re.capture(strings.coalesce(target.url, target.administrative_domain), `^(?:https?:\/\/)?(?:www\.)?([^\/:]+)`)
    $Target_Domain != ""
    $Target_EU_Country = strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name)
    
    match:
      $Target_Domain, $Target_EU_Country
    
    outcome:
      $Size_in_MB = math.round((sum(network.sent_bytes)/1000000), 2)
    
    order :
      $Size_in_MB desc
    
    limit:
       10  
  
Malware File Summary | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT")
    
    (metadata.product_event_type = /malware/ nocase or security_result.summary = /malware/ nocase or security_result.category_details = /malware/ nocase or metadata.description = /malware/ nocase or security_result.threat_name = /malware/ nocase or security_result.rule_name = /malware/ nocase or security_result.category = "SOFTWARE_MALICIOUS")
    
    $Source_User = strings.coalesce(principal.user.user_display_name, principal.user.userid, principal.user.email_addresses)
    $File_Name = strings.coalesce(target.file.full_path, about.file.full_path)
    $File_Name != ""
    $File_Type = target.file.file_type
    $Severity = security_result.severity
    $Action = security_result.action
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Threat_Name = security_result.threat_name
    
    match :
      $Hostname,$File_Name, $File_Type, $Threat_Name, $Source_User, $Severity, $Action
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
EU-Based DLP Events Over Time | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT" OR metadata.event_type = "NETWORK_UNCATEGORIZED" OR metadata.event_type = "NETWORK_FLOW" OR metadata.event_type = "NETWORK_CONNECTION" OR metadata.event_type = "NETWORK_FTP" OR metadata.event_type = "NETWORK_DHCP" OR metadata.event_type = "NETWORK_DNS" OR metadata.event_type = "NETWORK_HTTP" OR metadata.event_type = "NETWORK_SMTP")
    
    (metadata.log_type = /DLP|ACCELLION|CODE42_INCYDR|GUARDIUM|TRIPWIRE_FIM/ nocase OR metadata.product_event_type = /dlp/  nocase OR security_result.outcomes.value = /dlp/  nocase OR security_result.rule_type = /dlp/  nocase OR security_result.rule_name = /dlp/  nocase OR security_result.category_details = /dlp|data loss prevention/ nocase OR security_result.category = "DATA_EXFILTRATION" or security_result.category = "DATA_DESTRUCTION")
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
EU Data Access Events Over Time | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT")
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Action = security_result.action
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Policies Triggered | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT")
    security_result.rule_name = /Policy/ nocase
    
    $Policy = security_result.rule_name
    $Policy != ""
    $Target_EU_Country = strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name)
    
    match:
      $Policy, $Target_EU_Country
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Unauthorized Access to EU Resources | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT")
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses,target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Action = security_result.action
    $Action != "ALLOW"
    $Summary = strings.coalesce(security_result.summary, metadata.description, security_result.description)
    $Severity = security_result.severity
    
    match:
      $Summary, $User, $Source_IP ,$Action , $Severity, $Hostname
    
    outcome :
      $Count  = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds))
    
    order:
       $Count desc  
  
Access to EU Resources from Non-EU Countries | 
    
    
    (strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    and strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region, principal.location.name) != /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase)
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT")
    
    $Source_Country = strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region, principal.location.name)
    $Target_EU_Country = strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name)
    $Target_EU_Resource = strings.coalesce(target.resource.name, target.file.full_path, target.resource.product_object_id, target.group.product_object_id, target.user.group_identifiers)
    $Event_Type = metadata.event_type
    $Description = strings.coalesce(metadata.description,security_result.description,security_result.summary,metadata.product_event_type)
    $HTTP_Method = network.http.method
    $Log_Type = metadata.log_type
    $Action = security_result.action
    $User = strings.coalesce(principal.user.user_display_name, principal.user.userid, principal.user.email_addresses,target.user.userid,target.user.user_display_name,target.user.email_addresses)
    $Source_Country != ""
    
    match:
      $User, $Description, $Event_Type,  $Log_Type, $Source_Country, $Target_EU_Resource, $Target_EU_Country, $HTTP_Method, $Action
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds))
    
    order:
      $Count desc  
  
Top 10 Non-EU Countries Accessing EU Data | 
    
    
    (strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    and strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region, principal.location.name) != /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase)
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT")
    
    $Source_Country = strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region, principal.location.name)
    $Log_Type = metadata.log_type
    $Source_Country != ""
    
    match:
      $Source_Country, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Privileged Access to EU Resources Over Time | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT" OR metadata.event_type ="USER_LOGIN" or metadata.event_type = "USER_CHANGE_PERMISSIONS")
    
    $User = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses,target.user.userid,target.user.user_display_name,target.user.email_addresses)
    ($User = /admin|root|svc|adm|privilege/ nocase or principal.user.attribute.roles.type = "SERVICE_ACCOUNT" or principal.user.attribute.roles.type = "ADMINISTRATOR" or principal.user.account_type = "DOMAIN_ACCOUNT_TYPE" or principal.user.account_type = "SERVICE_ACCOUNT_TYPE")
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Target_EU_Country = strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name)
    
    match:
       $Target_EU_Country, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Threat Detection Over Time | 
    
    
    strings.coalesce(target.location.country_or_region, target.ip_geo_artifact.location.country_or_region, target.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.event_type = "GENERIC_EVENT")
    
    $Threat_Name = security_result.threat_name
    $Threat_Name != ""
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Threat_Name, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Sensitive Data Access Events | 
    
    
    strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region, principal.location.name) = /Austria|Belgium|Bulgaria|Croatia|Cyprus|Czechia|Denmark|Estonia|Finland|France|Germany|Greece|Hungary|Ireland|Italy|Latvia|Lithuania|Luxembourg|Malta|Netherlands|Poland|Portugal|Romania|Slovakia|Slovenia|Spain|Sweden|eu-(west-1|west-3|central-1|north-1|south-1|south-2)|europe-(west1|west3|west4|west8|west9|west10|west12|central2|north1|north2|southwest1)|austriaeast|denmarkeast|francecentral|germanywestcentral|greececentral|italynorth|northeurope|spaincentral|swedencentral|westeurope|polandcentral/ nocase
    
    (metadata.event_type = "RESOURCE_READ" OR metadata.event_type = "RESOURCE_WRITTEN" OR metadata.event_type = "RESOURCE_CREATION" OR metadata.event_type = "RESOURCE_DELETION" OR metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" OR metadata.event_type = "FILE_UNCATEGORIZED" OR metadata.event_type = "FILE_CREATION" OR metadata.event_type = "FILE_DELETION" OR metadata.event_type = "FILE_MODIFICATION" OR metadata.event_type = "FILE_READ" OR metadata.event_type = "FILE_COPY" OR metadata.event_type = "FILE_OPEN" OR metadata.event_type = "FILE_MOVE" OR metadata.event_type = "FILE_SYNC" OR metadata.event_type = "EVENTTYPE_UNSPECIFIED" OR metadata.event_type = "SETTING_UNCATEGORIZED" OR metadata.event_type = "USER_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" OR metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE" OR metadata.event_type = "USER_RESOURCE_CREATION" OR metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT" OR metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS" OR metadata.event_type = "USER_RESOURCE_ACCESS" OR metadata.event_type = "USER_RESOURCE_DELETION" OR metadata.log_type = "GENERIC_EVENT" OR metadata.event_type ="USER_LOGIN" or metadata.log_type = "USER_CHANGE_PERMISSIONS")
    
    (metadata.product_event_type = /SENSITIVE/ nocase OR security_result.rule_name = /SENSITIVE/ nocase OR metadata.description = /SENSITIVE/ nocase OR security_result.summary = /SENSITIVE/ nocase OR                      security_result.description = /SENSITIVE/ nocase)
    
    $Description = strings.coalesce(security_result.summary, security_result.description,metadata.description)
    $Source_User = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $Target_User = strings.coalesce(target.user.userid,target.user.user_display_name,target.user.email_addresses)
    $Source_Country = strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region, principal.location.name)
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Destination_IP = strings.coalesce(target.ip, target.asset.ip)
    $Protocol = network.application_protocol
    $Action = security_result.action
    $Log_Type = metadata.log_type
    
    match:
       $Description,$Source_User, $Target_User, $Source_IP,$Source_Country, $Destination_IP ,$Protocol , $Log_Type, $Action
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds))
    
    order:
       $Count desc    
  
## Google Workspace Alerts

This dashboard provides an overview of security events and potential threats, tracking critical alerts and trends related to user activity from workspace.

Top 10 High Severity AlertsTop 10 AlertsAlerts Over TimeRecent Alert DetailsAlert by SeverityTop 10 Users by Alert Count

Chart name | Query example  
---|---  
Top 10 High Severity Alerts | 
    
    
    metadata.log_type = "WORKSPACE_ALERTS"
    security_result.severity = "HIGH"
    security_result.summary != ""
    
    $Alert = security_result.summary
    $Alert != ""
    
    match:
      $Alert
    outcome:
      $Count = count(metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Top 10 Alerts | 
    
    
    metadata.log_type = "WORKSPACE_ALERTS"
    security_result.summary != ""
    
    $Alert = security_result.summary
    $Alert != ""
    
    match:
      $Alert
    outcome:
      $Count = count(security_result.summary)
    order:
      $Count desc
    limit:
        10   
  
Alerts Over Time | 
    
    
    metadata.log_type = "WORKSPACE_ALERTS"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    outcome:
      $Count = count(metadata.id)
    order:
      $Date desc  
  
Recent Alert Details | 
    
    
    metadata.log_type = "WORKSPACE_ALERTS"
    
    $Alert = security_result.summary
    $Category_Details = security_result.category_details
    $Category = security_result.category
    $Severity = security_result.severity
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Alert, $Category, $Category_Details, $Severity
    outcome:
      $Count = count(metadata.id)
    order:
      $Date desc
    limit:
        50   
  
Alert by Severity | 
    
    
    metadata.log_type = "WORKSPACE_ALERTS"
    
    $Severity = security_result.severity
    
    match:
      $Severity
    outcome:
      $Count = count(metadata.id)
    order:
      $Count desc  
  
Top 10 Users by Alert Count | 
    
    
    metadata.log_type = "WORKSPACE_ALERTS"
    target.user.userid != ""
    $User = target.user.userid
    
    match:
      $User
    outcome:
      $Count = count(metadata.id)
    order:
      $Count desc
    limit:
        10   
  
## Google Workspace Drive

This dashboard provides a comprehensive view of user activity and resource management. It highlights key security events, users, and access patterns across various locations, enabling security teams to ensure compliance and mitigate potential risks.

**Note:** Apply filters to refine the results for targeted insights.

DLP Summary for Download EventsDownload Events Over TimeTop 10 Users in Download EventsResource Deletion Events Over TimeTop 10 EventsResource Creation Events Over TimeTop 10 LocationsSource Geolocation OverviewDLP Summary for Upload EventsEvents Over Time by ActionTop 10 Accessed ResourcesTop 10 Users in Upload EventsTop 10 Users

Chart name | Query example  
---|---  
DLP Summary for Download Events | 
    
    
    metadata.product_event_type = "download"
    target.resource.attribute.labels.key = "dlp_info"
    
    $DLP_Signature = target.resource.attribute.labels.value
    $URL = target.url
    $Source_IP = principal.ip
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    
    match:
      $DLP_Signature,$User,$Source_IP, $URL
    
    outcome:
    
      $Storage_Used_in_MB = max(math.round(cast.as_float(additional.fields["storage_usage_in_bytes"])/(1000*1000), 2))
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Download Events Over Time | 
    
    
    metadata.product_event_type = "download"
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date,$User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Users in Download Events | 
    
    
    metadata.product_event_type = "download"
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    
    match:
      $User
    
    outcome:
    
      $Storage_Used_in_MB = sum(math.round(cast.as_float(additional.fields["storage_usage_in_bytes"])/(1000*1000), 2))
    
    order:
      $Storage_Used_in_MB desc
    
    limit:
        10  
  
Resource Deletion Events Over Time | 
    
    
    (metadata.event_type = "RESOURCE_DELETION" or metadata.event_type = "USER_RESOURCE_DELETION")
    (metadata.product_event_type = "trash" or metadata.product_event_type = "delete")
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date,$User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Events | 
    
    
    $Security_Event_Type = metadata.product_event_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    match:
      $Security_Event_Type,$User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Resource Creation Events Over Time | 
    
    
    (metadata.event_type  = "RESOURCE_CREATION" or metadata.event_type  = "USER_RESOURCE_CREATION")
    metadata.product_event_type = "create"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    
    match:
      $Date,$User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Locations | 
    
    
    $Location = strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region)
    
    match:
      $Location
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
    
      
  
Source Geolocation Overview | 
    
    
    (metadata.event_type = "USER_RESOURCE_ACCESS" or metadata.event_type = "RESOURCE_READ" or metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT")
    
    $Country = principal.ip_geo_artifact.location.country_or_region
    $Country !=""
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(principal.ip_geo_artifact.location.region_coordinates.latitude)
      $Longitude = max(principal.ip_geo_artifact.location.region_coordinates.longitude)
    
    order:
      $Count desc  
  
DLP Summary for Upload Events | 
    
    
    metadata.product_event_type = "upload"
    target.resource.attribute.labels.key = "dlp_info"
    
    $DLP_Signature = target.resource.attribute.labels.value
    $URL = target.url
    $Source_IP = principal.ip
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    
    match:
      $DLP_Signature,$User,$Source_IP, $URL
    
    outcome:
    
      $Storage_Used_in_MB = max(math.round(cast.as_float(additional.fields["storage_usage_in_bytes"])/(1000*1000), 2))
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Events Over Time by Action | 
    
    
    $Security_Event_Type = metadata.product_event_type
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date ,$Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc
    
      
  
Top 10 Accessed Resources | 
    
    
    (metadata.event_type  = "USER_RESOURCE_ACCESS" or  metadata.event_type  = "RESOURCE_READ" or  metadata.event_type  = "USER_RESOURCE_UPDATE_CONTENT")
    
    $Security_Event_Type = metadata.product_event_type
    $Resource_Id = target.resource.product_object_id
    $Resource_Id != ""
    $Source_User = strings.coalesce(principal.user.email_addresses, principal.user.userid, principal.user.user_display_name)
    $Source_IP = strings.coalesce(principal.ip,principal.asset.ip)
    $Action = security_result.action
    
    match:
      $Resource_Id,$Source_User,$Source_IP ,$Security_Event_Type, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users in Upload Events | 
    
    
    metadata.product_event_type = "upload"
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    
    match:
      $User
    
    outcome:
    
      $Storage_Used_in_MB = sum(math.round(cast.as_float(additional.fields["storage_usage_in_bytes"])/(1000*1000), 2))
    
    order:
      $Storage_Used_in_MB desc
    
    limit:
        10  
  
Top 10 Users | 
    
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Action = security_result.action
    
    match:
      $User, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
## Google Workspace Identity Management

This dashboard provides an overview of user and group activities, offering insights into login patterns, modifications, and permission changes, while also tracking trends over time.

Group Modifications Events Over TimeUser Deletion Events Over TimePermission Changes Events Over TimeSuccessful vs. Failed LoginsTop 10 Admins Handling Management TasksTop 10 Failed User Login TrendUser Creation Events Over TimeTop 10 Successful User Login Trend

Chart name | Query example  
---|---  
Group Modifications Events Over Time | 
    
    
    metadata.log_type = "WORKSPACE_ACTIVITY"
    metadata.product_event_type = /modify_group/ nocase
    
    $Event = metadata.product_event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Event
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
User Deletion Events Over Time | 
    
    
    metadata.log_type = "WORKSPACE_ACTIVITY"
    metadata.product_event_type = /delete_user/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(target.user.email_addresses)
    
    order:
      $Count desc  
  
Permission Changes Events Over Time | 
    
    
    metadata.log_type  = "WORKSPACE_ACTIVITY"
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    
    $Permission = metadata.event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Permission, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Successful vs. Failed Logins | 
    
    
    metadata.log_type = "WORKSPACE_ACTIVITY"
    metadata.product_event_type = "LOGIN_SUCCESS"
    or metadata.product_event_type = "LOGIN_FAILURE"
    
    $User_Login = metadata.product_event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $User_Login
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Admins Handling Management Tasks | 
    
    
    metadata.log_type = "WORKSPACE_ACTIVITY"
    target.application = /admin/ nocase
    
    $Event = metadata.event_type
    $Admin = principal.user.email_addresses
    
    match:
      $Admin, $Event
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Failed User Login Trend | 
    
    
    metadata.log_type = "WORKSPACE_ACTIVITY"
    metadata.product_event_type = "LOGIN_FAILURE"
    principal.user.email_addresses != ""
    
    $User_Account = principal.user.email_addresses
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
      $User_Account, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
User Creation Events Over Time | 
    
    
    metadata.log_type = "WORKSPACE_ACTIVITY"
    metadata.product_event_type = /create_user/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(target.user.email_addresses)
    
    order:
      $Count desc  
  
Top 10 Successful User Login Trend | 
    
    
    metadata.log_type = "WORKSPACE_ACTIVITY"
    metadata.product_event_type = "LOGIN_SUCCESS"
    principal.user.email_addresses != ""
    
    $User_Account = principal.user.email_addresses
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $User_Account, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
## Group Activity Summary

This dashboard provides a detailed view of user and group interactions, tracking distinct users, groups, and membership changes. It highlights the most active users and groups, group changes, and monitors group activity trends.

**Note:** Apply filters to refine the results for targeted insights.

Groups Created Over TimeTop 10 Hosts by Group Management EventGroups CreatedUsers Removed from GroupsRecent Groups DeletedBlocked Group Events Over TimeUsers Added to Admin GroupRecent Users Removed from GroupsGroup Change Activity CountTop 10 Blocked Users in Group EventsGroups DeletedRecent Groups CreatedTop 10 Active HostsTop 10 Users Deleting GroupsTop 10 Group ActionsTop 10 Users by Login EventNo. of Users Added to GroupsTop 10 Blocked Source IPs in Group EventsUnique Users in Login EventsTop 10 Source IPs Modifying GroupsTotal Users Added to Admin GroupGroup Activity Over TimeNew Groups AddedRecent Users Added to GroupsGroups Modified Over TimeRecent Groups ModifiedTop 10 Users Creating GroupsTop 10 Users Modifying GroupsUsers Added to GroupsTop 10 Source IPs Deleting GroupsCount of Unique User LoginsTop 10 Source IPs Creating GroupsTop 10 Active GroupsNo. of Users Removed from GroupsGroups Deleted Over TimeTop 10 Groups by Event CountTop 10 Active User Logins

Chart name | Query example  
---|---  
Groups Created Over Time | 
    
    
    metadata.event_type = "GROUP_CREATION"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Hosts by Group Management Event | 
    
    
    metadata.event_type = "GROUP_UNCATEGORIZED"
    or metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.event_type = "GROUP_MODIFICATION"
    
    $Hostname = principal.hostname
    $Hostname != ""
    $Event_Type = metadata.event_type
    
    match:
      $Hostname, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Groups Created | 
    
    
    metadata.event_type = "GROUP_CREATION"
    
    outcome:
      $Count = count_distinct(target.group.group_display_name)  
  
Users Removed from Groups | 
    
    
    $event.metadata.product_event_type = /4733|4729|4757/
    or $event.metadata.product_event_type = /remove.*(?:user|member).*(?:from|to).*group/ nocase
    
    $Initiator = strings.coalesce($event.principal.user.windows_sid, $event.principal.user.userid)
    $AffectedUser = strings.coalesce($event.target.user.windows_sid, $event.target.user.userid)
    $Group = $event.target.group.group_display_name
    $Description = strings.coalesce($event.metadata.description, $event.security_result.summary)
    
    match:
      $Initiator, $Group, $AffectedUser, $Description
    outcome:
      $Date = timestamp.get_timestamp(max($event.metadata.event_timestamp.seconds))
    order:
      $Date desc
    limit:
        50  
  
Recent Groups Deleted | 
    
    
    metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /delete(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Group = target.group.group_display_name
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $IP_Address = principal.ip
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $Group
    
    order:
      $Date desc  
  
Blocked Group Events Over Time | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /add group/ nocase
    or metadata.product_event_type = /delete group/ nocase
    or metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "BLOCK"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc   
  
Users Added to Admin Group | 
    
    
    metadata.product_event_type = /4732|4728|4756/
    or metadata.product_event_type = /add.*(?:user|member).*to.*group/ nocase
    
    $Initiator = strings.coalesce(principal.user.user_display_name, principal.user.userid, principal.user.windows_sid, target.user.userid, re.capture(additional.fields["Message"], `Account Name:(?:\W?)([A-Za-z0-9._%+-]+)`))
    $Affected_User = strings.coalesce(re.capture(additional.fields["Message"], `Member Name:(?:\W?)([A-Za-z0-9._%+-]+)`), re.capture(security_result.description, `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+`), target.user.user_display_name, target.user.userid, target.user.windows_sid)
    $Group = strings.coalesce(target.group.group_display_name, re.capture(security_result.description, `group\W([A-Za-z0-9._%+-]+\W+[A-Za-z0-9._%+-]+)`), re.capture(additional.fields["Message"], `Group Name:(?:\W?)([A-Za-z0-9._%+-]+)`))
    $Group = /admin/ nocase
    $Description = strings.coalesce(metadata.description, security_result.summary)
    $Date = timestamp.get_timestamp((metadata.event_timestamp.seconds))
    
    match:
      $Date, $Initiator, $Group, $Affected_User, $Description
    
    order:
      $Date desc  
  
Recent Users Removed from Groups | 
    
    
    metadata.product_event_type = /4733|4729|4757/
    or metadata.product_event_type = /remove.*(?:user|member).*(?:from|to).*group/ nocase
    
    $Initiator = strings.coalesce(principal.user.user_display_name, principal.user.userid, principal.user.windows_sid, target.user.userid, re.capture(additional.fields["Message"], `Account Name:(?:\W?)([A-Za-z0-9._%+-]+)`))
    $Affected_User = strings.coalesce(re.capture(additional.fields["Message"], `Member Name:(?:\W?)([A-Za-z0-9._%+-]+)`), re.capture(security_result.description, `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+`), target.user.user_display_name, target.user.userid, target.user.windows_sid)
    $Group = strings.coalesce(target.group.group_display_name, re.capture(security_result.description, `group\W([A-Za-z0-9._%+-]+\W+[A-Za-z0-9._%+-]+)`), re.capture(additional.fields["Message"], `Group Name:(?:\W?)([A-Za-z0-9._%+-]+)`))
    $Description = strings.coalesce(metadata.description, security_result.summary)
    $Date = timestamp.get_timestamp((metadata.event_timestamp.seconds))
    
    match:
      $Date, $Initiator, $Group, $Affected_User, $Description
    
    order:
      $Date desc  
  
Group Change Activity Count | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.event_type = "GROUP_MODIFICATION"
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Blocked Users in Group Events | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /add group/ nocase
    or metadata.product_event_type = /delete group/ nocase
    or metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "BLOCK"
    
    $Event_Type = metadata.event_type
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Event_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Groups Deleted | 
    
    
    $event.metadata.event_type = "GROUP_DELETION"
    
    outcome:
      $Count = count_distinct($event.target.group.group_display_name)  
  
Recent Groups Created | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.product_event_type = /(?:add|create)(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Group = target.group.group_display_name
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $IP_Address = principal.ip
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $Group
    
    order:
      $Date desc   
  
Top 10 Active Hosts | 
    
    
    $event.metadata.event_type = "GROUP_UNCATEGORIZED"
    or $event.metadata.event_type = "GROUP_CREATION"
    or $event.metadata.event_type = "GROUP_DELETION"
    or $event.metadata.event_type = "GROUP_MODIFICATION"
    
    $Hostname = $event.principal.hostname
    $Hostname != ""
    $Event_Type = $event.metadata.event_type
    $Log_type = $event.metadata.log_type
    
    match:
      $Hostname, $Event_Type, $Log_type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Top 10 Users Deleting Groups | 
    
    
    metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /delete(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Group Actions | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.event_type = "GROUP_MODIFICATION"
    
    $Description = strings.coalesce(metadata.description, security_result.summary)
    $Description != ""
    
    match:
      $Description
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users by Login Event | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $User = strings.concat(target.user.userid, " ")
    $User !=  " "
    
    match:
      $User
    
    outcome:
      $Count = count(target.user.userid)
    
    order:
      $Count desc
    
    limit:
        10  
  
No. of Users Added to Groups | 
    
    
    $event.metadata.event_type = "GROUP_MODIFICATION"
    $event.metadata.product_event_type = /4720|4728|4732|4746|4751|4756|4761|4785/
    or $event.metadata.product_event_type = /add.*(?:user|member).*to.*group/ nocase
    
    outcome:
      $Count = count($event.metadata.id)
      
  
Top 10 Blocked Source IPs in Group Events | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /add group/ nocase
    or metadata.product_event_type = /delete group/ nocase
    or metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "BLOCK"
    
    $Event_Type = metadata.event_type
    $IP_Address = principal.ip
    
    match:
      $Event_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Unique Users in Login Events | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    outcome:
      $Count = count_distinct(principal.user.userid)  
  
Top 10 Source IPs Modifying Groups | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $IP_Address, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Total Users Added to Admin Group | 
    
    
    metadata.product_event_type = /4732|4728|4756/
    or metadata.product_event_type = /add.*(?:user|member).*to.*group/ nocase
    
    $Group = strings.coalesce(target.group.group_display_name, re.capture(security_result.description, `group\W([A-Za-z0-9._%+-]+\W+[A-Za-z0-9._%+-]+)`), re.capture(additional.fields["Message"], `Group Name:(?:\W?)([A-Za-z0-9._%+-]+)`))
    $Group = /admin/ nocase
    
    outcome:
      $Count = count(metadata.id)  
  
Group Activity Over Time | 
    
    
    $event.metadata.event_type = "GROUP_CREATION"
    or $event.metadata.event_type = "GROUP_DELETION"
    or $event.metadata.event_type = "GROUP_MODIFICATION"
    or $event.metadata.event_type = "GROUP_UNCATEGORIZED"
    
    $User = $event.target.user.windows_sid
    $Hostname = $event.principal.hostname
    $Group = $event.target.group.group_display_name
    $Event = $event.metadata.event_type
    $Action = $event.metadata.description
    $Action != "A security-enabled local group membership was enumerated"
    
    match:
      $Event, $User, $Hostname, $Group, $Action
    outcome:
      $Date = timestamp.get_timestamp(max($event.metadata.event_timestamp.seconds))
    order:
      $Date desc
    limit:
        50  
  
New Groups Added | 
    
    
    $event.metadata.event_type = "GROUP_CREATION"
    
    outcome:
      $Count = count_distinct($event.target.group.group_display_name)  
  
Groups Deleted | 
    
    
    metadata.event_type = "GROUP_DELETION"
    
    outcome:
      $Count = count_distinct(target.group.group_display_name)  
  
Recent Users Added to Groups | 
    
    
    metadata.product_event_type = /4732|4728|4756/
    or metadata.product_event_type = /add.*(?:user|member).*to.*group/ nocase
    
    $Initiator = strings.coalesce(principal.user.user_display_name, principal.user.userid, principal.user.windows_sid, target.user.userid, re.capture(additional.fields["Message"], `Account Name:(?:\W?)([A-Za-z0-9._%+-]+)`))
    $Affected_User = strings.coalesce(re.capture(additional.fields["Message"], `Member Name:(?:\W?)([A-Za-z0-9._%+-]+)`), re.capture(security_result.description, `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+`), target.user.user_display_name, target.user.userid, target.user.windows_sid)
    $Group = strings.coalesce(target.group.group_display_name, re.capture(security_result.description, `group\W([A-Za-z0-9._%+-]+\W+[A-Za-z0-9._%+-]+)`), re.capture(additional.fields["Message"], `Group Name:(?:\W?)([A-Za-z0-9._%+-]+)`))
    $Description = strings.coalesce(metadata.description, security_result.summary)
    $Date = timestamp.get_timestamp((metadata.event_timestamp.seconds))
    
    match:
      $Date, $Initiator, $Group, $Affected_User, $Description
    
    order:
      $Date desc  
  
Groups Modified Over Time | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Recent Groups Modified | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Event = metadata.product_event_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $IP_Address = principal.ip
    $User = strings.coalesce(target.user.userid, target.user.email_addresses)
    $Group = target.group.group_display_name
    $Description = strings.coalesce(metadata.description, security_result.summary)
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $User, $Group, $Event, $Description
    
    order:
      $Date desc  
  
Users Removed from Groups | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    metadata.product_event_type = /4729|4733|4747|4752|4757|4762|4786/
    or metadata.product_event_type = /remove.*(?:user|member).*to.*group/ nocase
    
    outcome:
      $Count = count(metadata.id)
          
  
Top 10 Users Creating Groups | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.product_event_type = /(?:add|create)(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Modifying Groups | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    
    $Log_Type = metadata.log_type
    $User = principal.user.userid
    
    match:
      $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Users Added to Admin Group | 
    
    
    $event.metadata.product_event_type = /4732|4728|4756/
    or $event.metadata.product_event_type = /add.*(?:user|member).*to.*group/ nocase
    
    $Initiator = strings.coalesce($event.principal.user.windows_sid, $event.principal.user.userid)
    $User = strings.coalesce($event.target.user.windows_sid, $event.target.user.userid)
    $Group = $event.target.group.group_display_name
    $Group = /admin/ nocase
    $Description = strings.coalesce($event.metadata.description, $event.security_result.summary)
    
    match:
      $Initiator, $User, $Group, $Description
    outcome:
      $Date = timestamp.get_timestamp(max($event.metadata.event_timestamp.seconds))
    order:
      $Date desc
    limit:
        50  
  
Group Change Activity Count | 
    
    
    $event.metadata.event_type = "GROUP_CREATION"
    or $event.metadata.event_type = "GROUP_DELETION"
    or $event.metadata.event_type = "GROUP_MODIFICATION"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Users Added to Groups | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    metadata.product_event_type = /4720|4728|4732|4746|4751|4756|4761|4785/
    or metadata.product_event_type = /add.*(?:user|member).*to.*group/ nocase
    
    outcome:
      $Count = count(metadata.id)
      
  
Top 10 Group Actions | 
    
    
    $event.metadata.event_type = "GROUP_CREATION"
    or $event.metadata.event_type = "GROUP_DELETION"
    or $event.metadata.event_type = "GROUP_MODIFICATION"
    
    $Description = strings.coalesce($event.metadata.description, $event.security_result.summary)
    $Group_Name = $event.target.group.group_display_name
    
    match:
      $Description, $Group_Name
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Source IPs Deleting Groups | 
    
    
    metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /delete(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Count of Unique User Logins | 
    
    
    $event.metadata.event_type = "USER_LOGIN"
    
    outcome:
      $Count = count_distinct($event.principal.user.userid)  
  
Top 10 Source IPs Creating Groups | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.product_event_type = /(?:add|create)(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Active Groups | 
    
    
    $event.metadata.event_type = "GROUP_UNCATEGORIZED"
    or $event.metadata.event_type = "GROUP_CREATION"
    or $event.metadata.event_type = "GROUP_DELETION"
    or $event.metadata.event_type = "GROUP_MODIFICATION"
    
    $Log_Type = $event.metadata.log_type
    $Event = $event.metadata.event_type
    $Group_Name = $event.target.group.group_display_name
    $Group_Name != ""
    
    match:
      $Group_Name, $Event, $Log_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
No. of Users Removed from Groups | 
    
    
    $event.metadata.event_type = "GROUP_MODIFICATION"
    $event.metadata.product_event_type = /4729|4733|4747|4752|4757|4762|4786/
    or $event.metadata.product_event_type = /remove.*(?:user|member).*to.*group/ nocase
    
    outcome:
      $Count = count($event.metadata.id)
          
  
Groups Deleted Over Time | 
    
    
    metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /delete(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Groups by Event Count | 
    
    
    metadata.event_type = "GROUP_UNCATEGORIZED"
    or metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.event_type = "GROUP_MODIFICATION"
    
    $Event_Type = metadata.event_type
    $Group_Name = target.group.group_display_name
    $Group_Name != ""
    
    match:
      $Group_Name, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Active User Logins | 
    
    
    $event.metadata.event_type = "USER_LOGIN"
    
    $Event_Type = $event.metadata.event_type
    $User = strings.concat($event.target.user.userid, " ")
    $User != " "
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $User, $Event_Type, $Date over every day
    outcome:
      $Count = count($event.target.user.userid)
    order:
      $Date desc, $Count desc
    limit:
        10  
  
Users Added to Groups | 
    
    
    $event.metadata.product_event_type = /4732|4728|4756/
    or $event.metadata.product_event_type = /add.*(?:user|member).*to.*group/ nocase
    
    $Initiator = strings.coalesce($event.principal.user.windows_sid, $event.principal.user.userid)
    $AffectedUser = strings.coalesce($event.target.user.windows_sid, $event.target.user.userid)
    $Group = $event.target.group.group_display_name
    $Description = strings.coalesce($event.metadata.description, $event.security_result.summary)
    
    match:
      $Initiator, $Group, $AffectedUser, $Description
    outcome:
      $Date = timestamp.get_timestamp(max($event.metadata.event_timestamp.seconds))
    order:
      $Date desc
    limit:
        50  
  
## Group Management Audit

This is a dedicated dashboard for auditing the entire lifecycle of user groups. It helps ensure that group creations, modifications, and deletions are properly managed, preventing unintended access rights at scale.

Top 10 Users Creating GroupsTop 10 Source IPs Creating GroupsTop 10 Users Modifying GroupsRecent Group ModificationsTotal Unique Groups ModifiedGroups Deleted Over TimeGroups Created Over TimeGroups Modified Over TimeGroup Events Over TimeTop 10 Source IPs Deleting GroupsTotal Unique Groups CreatedRecent Group DeletionsTop 10 Source IPs Modifying GroupsTop 10 Blocked Users in Group EventsTop 10 Users Deleting GroupsRecent Group CreationsTop 10 Blocked Source IPs in Group EventsTotal Unique Groups Deleted

Chart name | Query example  
---|---  
Top 10 Users Creating Groups | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.product_event_type = /(?:add|create)(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs Creating Groups | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.product_event_type = /(?:add|create)(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Modifying Groups | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Group Modifications | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Event = metadata.product_event_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $IP_Address = principal.ip
    $User = strings.coalesce(target.user.userid, target.user.email_addresses)
    $Group = target.group.group_display_name
    $Description = strings.coalesce(metadata.description, security_result.summary)
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $User, $Group, $Event, $Description
    
    order:
      $Date desc  
  
Total Unique Groups Modified | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "ALLOW"
    
    outcome:
      $Count = count_distinct(target.group.group_display_name)  
  
Groups Deleted Over Time | 
    
    
    metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /delete(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Groups Created Over Time | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.product_event_type = /(?:add|create)(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Groups Modified Over Time | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Group Events Over Time | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /(?:add|create|delete)(?:\s)?group/ nocase
    or metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Event = metadata.event_type
    
    match:
      $Date, $Event
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Source IPs Deleting Groups | 
    
    
    metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /delete(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Total Unique Groups Created | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.product_event_type = /(?:add|create)(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    outcome:
      $Count = count_distinct(target.group.group_display_name)  
  
Recent Group Deletions | 
    
    
    metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /delete(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Group = target.group.group_display_name
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $IP_Address = principal.ip
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $Group
    
    order:
      $Date desc  
  
Top 10 Source IPs Modifying Groups | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Blocked Users in Group Events | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /add group/ nocase
    or metadata.product_event_type = /delete group/ nocase
    or metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "BLOCK"
    
    $Event_Type = metadata.event_type
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Event_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Deleting Groups | 
    
    
    metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /delete(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Group Creations | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.product_event_type = /(?:add|create)(?:\s)?group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Group = target.group.group_display_name
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $IP_Address = principal.ip
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $Group
    
    order:
      $Date desc   
  
Top 10 Blocked Source IPs in Group Events | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /add group/ nocase
    or metadata.product_event_type = /delete group/ nocase
    or metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "BLOCK"
    
    $Event_Type = metadata.event_type
    $IP_Address = principal.ip
    
    match:
      $Event_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Total Unique Groups Deleted | 
    
    
    metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /delete group/ nocase
    security_result.action = "ALLOW"
    
    outcome:
      $Count = count_distinct(target.group.group_display_name)  
  
## HIPAA Dashboard

This dashboard provides real-time monitoring of security and compliance metrics to ensure adherence to HIPAA regulations. It provides visibility into potential risks, violations, and data access activities involving Protected Health Information (PHI). This enables proactive risk management and helps maintain the confidentiality, integrity, and availability of sensitive health data. This dashboard uses the `ePHI_assets.Hostname` data table to scope data according to HIPAA standards. The charts on this dashboard don't load until the required data tables are created.

Vulnerabilities by SeverityPermission Changes Over Time by Log TypeMFA Events Over Time by ActionLogin Events Over Time by ActionTop 10 ePHI Hosts by DLP ViolationsEDR Alerts Over Time by SeverityBackup Events Over Time by ActionPassword Changes Over Time by ActionRecent Backup Events (Last 24 Hours)Recent EDR Alerts (Last 24 Hours)Recent User Account Creations (Last 24 Hours)Weak Encrypted Communication Over Time by Log TypeRecent User Change Password (Last 24 Hours)Top 10 SaaS ApplicationsTop 10 Key Operations

Chart name | Query example  
---|---  
Vulnerabilities by Severity | 
    
    
    metadata.log_type = /ARMIS_VULNERABILITIES|FINGERPRINT_JS|NUCLEUS_VULNERABILITY|QUALYS_ASSET_CONTEXT|QUALYS_SCAN|QUALYS_VIRTUAL_SCANNER|QUALYS_VM|RAPID7_INSIGHT|RAPID7_NEXPOSE|SNYK_SDLC|SPUR_FEEDS|STACKHAWK|SUBLIMESECURITY|SYMANTEC_SA|TENABLE_IO|TENABLE_OT|TENABLE_SC|TRENDMICRO_VISION_ONE_CONTAINER_VULNERABILITIES|UPGUARD|URLSCAN_IO/ nocase
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Severity =
        if (principal.asset.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            principal.asset.vulnerabilities.severity,
        if (target.asset.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            target.asset.vulnerabilities.severity,
        if (extensions.vulns.vulnerabilities.severity != "UNKNOWN_SEVERITY",
            extensions.vulns.vulnerabilities.severity,
        "UNKNOWN_SEVERITY")))
    
    match:
      $Severity
    
    outcome:
      $Count = count(strings.coalesce(extensions.vulns.vulnerabilities.name, extensions.vulns.vulnerabilities.description, extensions.vulns.vulnerabilities.vendor_vulnerability_id,
                                              principal.asset.vulnerabilities.name, target.asset.vulnerabilities.name, additional.fields["ScanReference"]))
    
    order:
      $Severity desc  
  
Permission Changes Over Time by Log Type | 
    
    
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
MFA Events Over Time by Action | 
    
    
    (re.regex(metadata.product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex(additional.fields["AuthenticationRequirement"], `multiFactorAuthentication`) nocase or re.regex(security_result.detection_fields.value, `MFA`) nocase )
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname,target.asset.hostname) in %ePHI_assets.Hostname
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Login Events Over Time by Action | 
    
    
    metadata.event_type = "USER_LOGIN"
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 ePHI Hosts by DLP Violations | 
    
    
    metadata.log_type = /DLP|ACCELLION|CODE42_INCYDR|GUARDIUM|TRIPWIRE_FIM/ nocase
    metadata.product_event_type = /Violation/ nocase
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Severity = security_result.severity
    $Hostname= strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    
    match:
      $Hostname, $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
EDR Alerts Over Time by Severity | 
    
    
    metadata.log_type = /EDR|CS_ALERTS|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce(security_result.rule_name, security_result.threat_name) != ""
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Severity = security_result.severity
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Backup Events Over Time by Action | 
    
    
    (metadata.log_type = /COHESITY|DRUVA_BACKUP|VEEAM|VERITAS_NETBACKUP/ nocase or metadata.log_type = "RUBRIK")
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Action = security_result.action
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Password Changes Over Time by Action | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Log_Type = metadata.log_type
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match :
      $Date, $Action
    
    outcome :
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Recent Backup Events (Last 24 Hours) | 
    
    
    (metadata.log_type = /COHESITY|DRUVA_BACKUP|VEEAM|VERITAS_NETBACKUP/ nocase or metadata.log_type = "RUBRIK")
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Description = strings.coalesce(metadata.description, security_result.description, security_result.summary)
    $Log_Type = metadata.log_type
    $Event_Type = metadata.event_type
    $Security_Event_Type = metadata.product_event_type
    $Action = security_result.action
    
    match:
      $Description, $Security_Event_Type, $Event_Type, $Action, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T ")
    
    order:
      $Date desc  
  
Recent EDR Alerts (Last 24 Hours) | 
    
    
    metadata.log_type = /EDR|CS_ALERTS|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Log_Type = metadata.log_type
    $EDR_Alerts = strings.coalesce(security_result.rule_name, security_result.threat_name)
    $EDR_Alerts != ""
    $Severity = security_result.severity
    $User = strings.coalesce(principal.user.user_display_name, principal.user.email_addresses, principal.user.userid, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    
    match:
      $EDR_Alerts, $Hostname, $User, $Severity, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Date desc
      
  
Recent User Account Creations (Last 24 Hours) | 
    
    
    metadata.event_type = "USER_CREATION"
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Log_Type = metadata.log_type
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Source_Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Initiator = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $User_Created = strings.coalesce(target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Action = security_result.action
    
    match:
      $Initiator, $User_Created, $Source_Hostname, $Source_IP, $Action, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T ")
    
    order:
      $Date desc  
  
Weak Encrypted Communication Over Time by Log Type | 
    
    
    (((target.resource.attribute.labels.key  = "keyProperties_type" or target.resource.attribute.labels.key  = "requestParameters.keySpec" or target.resource.attribute.labels.key = /key/ nocase) and target.resource.attribute.labels.value  = /^(RSA-)|DES|RC4|MD5|SHA1|SHA-1/) or network.tls.cipher = /^(RSA-)|DES|RC4|MD5|SHA1|SHA-1/)
    strings.coalesce(principal.hostname, principal.asset.hostname,  target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Recent User Change Password (Last 24 Hours) | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Log_Type = metadata.log_type
    $Security_Event_Type = metadata.product_event_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Source_Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Action = security_result.action
    
    match :
      $User, $Source_Hostname, $Source_IP, $Security_Event_Type, $Action, $Log_Type
    
    outcome :
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds ), "%F %T")
      $Count = count(metadata.id)
    
    order :
      $Date desc
    
      
  
Top 10 SaaS Applications | 
    
    
    strings.coalesce(security_result.category_details, security_result.rule_name) = /saas/ nocase
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Application = target.application
    $Log_Type = metadata.log_type
    
    match:
       $Application, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Key Operations | 
    
    
    (metadata.log_type  = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT|GCP_CLOUDAUDIT/ or target.application = "kms.amazonaws.com")
    strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname) in %ePHI_assets.Hostname
    
    $Security_Event_Type = metadata.product_event_type
    $Log_Type = strings.coalesce(metadata.log_type, target.application)
    
    match:
      $Security_Event_Type, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
## Host Investigation

This dashboard provides a comprehensive overview of host activities and security events. Key widgets track network communication, authentication changes, malware, top events, and rare processes. It also monitors service and scheduled task creation, and potential security threats.

**Note:** Hostname must be specified in the filter for the charts to populate appropriately.

Top 10 EventsEvents Trend Over TimeMalware and IntrusionNetwork Communication Outbound MapRare ProcessesService CreationNetwork CommunicationAuthentication and ChangesNetwork Communication Inbound MapScheduled Task Creation

Chart name | Query example  
---|---  
Top 10 Events | 
    
    
    $Event_Type = metadata.event_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    
    match:
      $Event_Type,$User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Events Trend Over Time | 
    
    
    $Event_Type = metadata.event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Malware and Intrusion | 
    
    
    $Log_Type = metadata.log_type
    $Category = security_result.category
    ($Category = "UNKNOWN_CATEGORY" or $Category = "SOFTWARE_MALICIOUS" or $Category = "SOFTWARE_SUSPICIOUS" or $Category = "SOFTWARE_PUA" or $Category = "NETWORK_MALICIOUS"or $Category = "NETWORK_SUSPICIOUS" or $Category = "NETWORK_CATEGORIZED_CONTENT" or $Category = "NETWORK_DENIAL_OF_SERVICE" or $Category = "NETWORK_RECON" or $Category = "NETWORK_COMMAND_AND_CONTROL" or $Category = "ACL_VIOLATION" or $Category = "AUTH_VIOLATION" or $Category = "EXPLOIT" or $Category = "DATA_EXFILTRATION" or $Category = "DATA_AT_REST" or $Category = "DATA_DESTRUCTION" or $Category = "TOR_EXIT_NODE" or $Category = "MAIL_SPAM" or $Category = "MAIL_PHISHING" or $Category = "MAIL_SPOOFING" or $Category = "POLICY_VIOLATION" or $Category = "SOCIAL_ENGINEERING" or $Category = "PHISHING")
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname,intermediary.hostname,target.hostname,target.asset.hostname)
    $Hostname !=""
    $Description = strings.coalesce(metadata.description,security_result.summary)
    $Action = security_result.action
    $File_Path = target.file.full_path
    
    match:
    $Hostname, $Log_Type, $Category, $Description, $Action,$File_Path
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Network Communication Outbound Map | 
    
    
    (metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP")
    network.direction = "OUTBOUND"
    
    $Hostname = strings.coalesce(principal.hostname, intermediary.hostname, observer.hostname, principal.asset.hostname, principal.asset.ip)
    $Country = target.ip_geo_artifact.location.country_or_region
    
    match:
      $Country
    
    outcome:
      $Latitude = max(target.ip_geo_artifact.location.region_coordinates.latitude)
      $Longitude = max(target.ip_geo_artifact.location.region_coordinates.longitude)
      $Count = count(metadata.id)  
  
Rare Processes | 
    
    
    (metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD")
    
    $Process_Name = strings.coalesce(if(principal.application != "", principal.application, ""), if(re.capture(target.process.file.full_path, `.*\\(\S+\.\w+)`) != "", re.capture(target.process.file.full_path, `.*\\(\S+\.\w+)`), ""))
    $Process_Name != ""
    $Severity = security_result.severity
    $Action = security_result.action
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    match:
      $Process_Name,$User,$Severity,$Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count asc
      
  
Service Creation | 
    
    
    (metadata.event_type = "SERVICE_CREATION" or metadata.event_type = "SERVICE_UNSPECIFIED")
    
    $Username = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname,intermediary.hostname,target.hostname,target.asset.hostname)
    $Application = target.application
    $Path = target.process.file.full_path
    
    match:
      $Hostname, $Application, $Username, $Path
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Network Communication | 
    
    
    (metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP")
    
    $Source_Port = principal.port
    $Destination_Port = target.port
    $Source_IP = principal.ip
    $Destination_IP = target.ip
    $Direction = network.direction
    $Direction != "UNKNOWN_DIRECTION"
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname,intermediary.hostname,target.hostname,target.asset.hostname)
    $Hostname != ""
    $Bytes_Sent = network.sent_bytes
    $Bytes_Received = network.received_bytes
    
    match:
    $Hostname, $Source_IP, $Source_Port, $Direction, $Destination_IP, $Destination_Port,$Bytes_Sent,$Bytes_Received
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Authentication and Changes | 
    
    
    $Event_Type = metadata.event_type
    ($Event_Type = "USER_LOGIN" or $Event_Type = "USER_LOGOUT" or $Event_Type = "USER_BADGE_IN" or $Event_Type= "USER_CHANGE_PASSWORD" or $Event_Type = "USER_CHANGE_PERMISSIONS" or $Event_Type = "USER_CREATION" or $Event_Type = "USER_DELETION" or $Event_Type = "USER_RESOURCE_CREATION" or $Event_Type = "USER_RESOURCE_DELETION" or $Event_Type= "USER_RESOURCE_UPDATE_CONTENT" or $Event_Type = "USER_RESOURCE_UPDATE_PERMISSIONS" or $Event_Type = "SERVICE_CREATION" or $Event_Type = "SERVICE_DELETION" or $Event_Type = "SERVICE_MODIFICATION" or $Event_Type = "SETTING_CREATION" or $Event_Type = "SETTING_DELETION" or $Event_Type = "SETTING_MODIFICATION" or $Event_Type = "DEVICE_CONFIG_UPDATE")
    $Log_Type = metadata.log_type
    $Security_Event_Type = metadata.product_event_type
    $Description = strings.coalesce(metadata.description,security_result.description)
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname,intermediary.hostname,target.hostname,target.asset.hostname)
    $Hostname !=""
    $Action = security_result.action
    
    match:
      $Hostname, $Log_Type, $Event_Type,$Security_Event_Type, $Description, $Action
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
      
  
Network Communication Inbound Map | 
    
    
    (metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP")
    network.direction = "INBOUND"
    
    $Country = principal.ip_geo_artifact.location.country_or_region
    
    match:
      $Country
    
    outcome:
      $Latitude = max(principal.ip_geo_artifact.location.region_coordinates.latitude)
      $Longitude = max(principal.ip_geo_artifact.location.region_coordinates.longitude)
      $Count = count(metadata.id)  
  
Scheduled Task Creation | 
    
    
    metadata.event_type = "SCHEDULED_TASK_CREATION"
    
    $Username = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname,intermediary.hostname,target.hostname,target.asset.hostname)
    $Task_Name = target.resource.name
    
    match:
    $Hostname, $Task_Name, $Username
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
## IAM Security Operations

This dashboard is a high-level overview for daily monitoring. It focuses on real-time anomalies, active threats, and high-risk events to enable rapid incident detection and response.

**Note:** Use the available filters to narrow down the results as required.

Recent Users Account DeletedPrivileged Account Login Failures & SuccessesTotal Unique Users Account ModifiedTop 10 User Account LoginsRecent Roles DeletedTop 10 Blocked Source IPs in User EventsFirst-Time Access from New SourceTop 10 User-Accessed ApplicationsUser Lifecycle KPITop 10 Blocked Users in User EventsPassword Changes Over TimeTop 10 Blocked Users in Role EventsImpossible TravelTotal Unique Users Account DeletedTotal Unique Users Account Created

Chart name | Query example  
---|---  
Recent Users Account Deleted | 
    
    
    metadata.event_type = "USER_DELETION"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $User = strings.coalesce(target.user.userid, target.user.email_addresses)
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $IP_Address = principal.ip
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $User
    
    order:
      $Date desc  
  
Privileged Account Login Failures & Successes | 
    
    
    metadata.event_type = "USER_LOGIN"
    strings.coalesce(principal.user.attribute.roles.name, principal.resource.name, target.user.attribute.roles.name, target.resource.name) = /admin/ nocase
    if(security_result.action = "ALLOW", "Success", if(security_result.action = "BLOCK", "Failed", "Unknown")) != ""
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $User = if(strings.coalesce(principal.user.attribute.roles.name, principal.resource.name) = /admin/ nocase, strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses),
            if(strings.coalesce(target.user.attribute.roles.name, target.resource.name) = /admin/ nocase, strings.coalesce(target.user.windows_sid, target.user.userid, target.user.email_addresses), ""))
    $Login_Status = if(security_result.action = "ALLOW", "Success", if(security_result.action = "BLOCK", "Failed", "Unknown"))
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Privilege_Type = principal.user.attribute.roles.name
    $Privilege_Type != ""
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    
    match:
      $Date, $User, $Login_Status, $Privilege_Type,  $Hostname, $Source_IP
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Total Unique Users Account Modified | 
    
    
    metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    outcome:
      $Count = count_distinct(strings.coalesce(target.user.userid, target.user.email_addresses))  
  
Top 10 User Account Logins | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = target.user.userid
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(target.user.userid)
    
    order:
      $Count desc
    
    limit:
        10    
  
Recent Roles Deleted | 
    
    
    metadata.product_event_type = /\bDelete.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /delete role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $IP_Address = principal.ip
    $Role = strings.coalesce(target.user.attribute.roles.name, target.resource.name)
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $Role
    
    order:
      $Date desc    
  
Top 10 Blocked Source IPs in User Events | 
    
    
    metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "BLOCK"
    
    $Event_Type = metadata.event_type
    $IP_Address = principal.ip
    
    match:
      $Event_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
First-Time Access from New Source | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "ALLOW"
    
    $Source_IP = principal.ip
    $User = target.user.userid
    $Country = principal.location.country_or_region
    $City = principal.location.city
    $City != ""
    $ASN = principal.ip_geo_artifact.network.asn
    $ASN != ""
    
    match:
       $Source_IP, $User, $Country, $City, $ASN
    
    outcome:
      $Count = count(metadata.id)
      $FirstTime_Access = earliest(metadata.event_timestamp)
    
    order:
      $FirstTime_Access desc  
  
Top 10 User-Accessed Applications | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Application = target.application
    $Application != ""
    
    match:
      $Log_Type, $Application
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
User Lifecycle KPI | 
    
    
    metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_RESOURCE_DELETION"
    or metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    
    $User_Action = if(metadata.event_type = "USER_CREATION", "Total Creation", if(metadata.event_type = "USER_DELETION" or metadata.event_type = "USER_RESOURCE_DELETION", "Total Deletion", if(metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE" or metadata.event_type = "USER_CHANGE_PERMISSIONS" or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS", "Total Modification")))
    
    match:
      $User_Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count asc
       
  
Top 10 Blocked Users in User Events | 
    
    
    metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "BLOCK"
    
    $Event_Type = metadata.event_type
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Event_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Password Changes Over Time | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Blocked Users in Role Events | 
    
    
    (metadata.product_event_type = /Create.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /add role definition/ nocase))
    or
    (metadata.product_event_type = /Update.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /update role definition/ nocase))
    or
    (metadata.product_event_type = /\bDelete.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /delete role definition/ nocase))
    security_result.action = "BLOCK"
    
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $Event = metadata.product_event_type
    
    match:
      $User, $Event
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Impossible Travel | 
    
    
    $first_login.metadata.event_type = "USER_LOGIN"
    $first_login.security_result.action = "ALLOW"
    $first_login.principal.ip_geo_artifact.location.state != "" and $Country1 = $first_login.principal.ip_geo_artifact.location.state
    $Time = timestamp.get_timestamp($first_login.metadata.event_timestamp.seconds, "%F %T ")
    
    $User = strings.coalesce($first_login.target.user.userid, $first_login.target.user.email_addresses)
    $User != ""
    $Latitude1  =  $first_login.principal.ip_geo_artifact.location.region_coordinates.latitude
    $Longitude1 =  $first_login.principal.ip_geo_artifact.location.region_coordinates.longitude
    
    $second_login.metadata.event_type = "USER_LOGIN"
    $second_login.security_result.action = "ALLOW"
    $second_login.principal.ip_geo_artifact.location.state != "" and $Country2 = $second_login.principal.ip_geo_artifact.location.state
    $Time2 = timestamp.get_timestamp($second_login.metadata.event_timestamp.seconds, "%F %T ")
    
    $User = strings.coalesce($second_login.target.user.userid, $second_login.target.user.email_addresses)
    $User != ""
    $Latitude2  =  $second_login.principal.ip_geo_artifact.location.region_coordinates.latitude
    $Longitude2 =  $second_login.principal.ip_geo_artifact.location.region_coordinates.longitude
    $first_login.metadata.event_timestamp.seconds < $second_login.metadata.event_timestamp.seconds
    
    ($Latitude1 != $Latitude2)
    ($Longitude1 != $Longitude2)
    
    match:
      $User, $Time, $Country1, $Time2, $Country2 over 1h
    
    outcome:
      $distance_kilometers = math.ceil(max(math.geo_distance($Latitude1, $Longitude1, $Latitude2, $Longitude2)) /1000)
    
    condition:
      $first_login and $second_login and $distance_kilometers != 0  
  
Total Unique Users Account Deleted | 
    
    
    metadata.event_type = "USER_DELETION"
    security_result.action = "ALLOW"
    
    outcome:
      $Count = count_distinct(strings.coalesce(target.user.userid, target.user.email_addresses))  
  
Total Unique Users Account Created | 
    
    
    metadata.event_type = "USER_CREATION"
    security_result.action = "ALLOW"
    
    outcome:
      $Count = count_distinct(strings.coalesce(target.user.userid, target.user.email_addresses))  
  
## IDS / IPS Event Overview

This dashboard provides a comprehensive snapshot of security events detected by intrusion detection and prevention systems.

IDS / IPS Events by CategoriesTop 10 IPs by Event CountIDS / IPS Events by DestinationIDS / IPS Events by SourceTop IDS / IPS Events by Rule and ActionIDS / IPS Events over Time by SeverityTop 10 IDS / IPS High Severity EventsIDS / IPS Events by Signature

Chart name | Query example  
---|---  
IDS / IPS Events by Categories | 
    
    
    $event_type = metadata.event_type
    (($event_type = "SCAN_UNCATEGORIZED" or $event_type = "SCAN_NETWORK") or ($event_type >= 16000 and $event_type <= 16007))
    $category = security_result.category
    $category != "UNKNOWN_CATEGORY"
    match:
    $category
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
Top 10 IPs by Event Count | 
    
    
    $event_type = metadata.event_type
    (($event_type = "SCAN_UNCATEGORIZED" or $event_type = "SCAN_NETWORK" or $event_type = "SCAN_VULN_NETWORK") or ($event_type >= 16000 and $event_type <= 16007))
    $source_ip = principal.ip
    $rule_name = security_result.rule_name
    $rule_name != ""
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $rule_name, $source_ip
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
IDS / IPS Events by Destination | 
    
    
    $event_type = metadata.event_type
    (($event_type = "SCAN_UNCATEGORIZED" or $event_type = "SCAN_NETWORK" or $event_type = "SCAN_VULN_NETWORK") or ($event_type >= 16000 and $event_type <= 16007))
    $vendor = metadata.vendor_name
    $destination_ip = target.ip
    $action = security_result.action
    $rule_name = security_result.rule_name
    $rule_name != ""
    $security_event_type = metadata.product_event_type
    $security_event_type != ""
    $security_event_type != /NetworkSecurityGroupFlowEvents|fileinfo|flow/ nocase
    match:
    $destination_ip, $rule_name, $vendor, $action
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
IDS / IPS Events by Source | 
    
    
    $event_type = metadata.event_type
    (($event_type = "SCAN_UNCATEGORIZED" or $event_type = "SCAN_NETWORK" or $event_type = "SCAN_VULN_NETWORK") or ($event_type >= 16000 and $event_type <= 16007))
    $action = security_result.action
    $action != "UNKNOWN_ACTION"
    $hostname = principal.hostname
    $rule_name = strings.coalesce(security_result.rule_name, metadata.description)
    $rule_name != ""
    $vendor = metadata.vendor_name
    $security_event_type = metadata.product_event_type
    $security_event_type != ""
    $security_event_type != /NetworkSecurityGroupFlowEvents|fileinfo|flow/ nocase
    match:
    $hostname, $rule_name, $vendor, $action
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
Top IDS / IPS Events by Rule and Action | 
    
    
    $event_type = metadata.event_type
    (($event_type = "SCAN_UNCATEGORIZED" or $event_type = "SCAN_NETWORK") or ($event_type >= 16000 and $event_type <= 16007))
    $rule_name = security_result.rule_name
    not $rule_name in %known_signatures
    $rule_name != ""
    $action = security_result.action
    $action != "UNKNOWN_ACTION"
    match:
    $rule_name, $action
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
IDS / IPS Events over Time by Severity | 
    
    
    $event_type = metadata.event_type
    (($event_type = "SCAN_UNCATEGORIZED" or $event_type = "SCAN_NETWORK") or ($event_type >= 16000 and $event_type <= 16007))
    $severity = security_result.severity
    $severity != "UNKNOWN_SEVERITY"
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $severity, $date
    outcome:
    $event_count = count(metadata.id)
    order:
    $date asc  
  
Top 10 IDS / IPS High Severity Events | 
    
    
    $event_type = metadata.event_type
    (($event_type = "SCAN_UNCATEGORIZED" or $event_type = "SCAN_NETWORK") or ($event_type >= 16000 and $event_type <= 16007))
    $action = security_result.action
    $rule_name = strings.coalesce(security_result.rule_name, metadata.description)
    $rule_name != ""
    $severity = security_result.severity
    $severity = "HIGH"
    match:
    $rule_name, $action
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
IDS / IPS Events by Signature | 
    
    
    $event_type = metadata.event_type
    (($event_type = "SCAN_UNCATEGORIZED" or $event_type = "SCAN_NETWORK") or ($event_type >= 16000 and $event_type <= 16007))
    $destination_ip = target.ip
    $source_ip = principal.ip
    $action = security_result.action
    $rule_name = security_result.rule_name
    $rule_name != ""
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $rule_name , $source_ip , $destination_ip , $action
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
## ISO27001 - Organizational Controls

This dashboard provides visibility into organizational security controls and compliance performance based on iso 27001 standards. It helps security teams monitor control implementation, track audit results, and identify areas for improvement. By centralizing key compliance metrics, the dashboard supports ongoing alignment with `ISO 27001` requirements and strengthens the organization's overall information security management. Note: this dashboard requires the use of filters.

**Note:** Apply the available filters to refine the results.

DLP Violations by SeverityTop 10 DLP RulesRecent Role Creations, Modifications, and DeletionsRecent Permission ChangesBlocked Network Traffic Over Time by ReasonUser Events Over TimeTop 10 Applications AccessedTop 10 Outbound IPs by Traffic VolumeDevices Over TimePassword Changes Over Time

Chart name | Query example  
---|---  
DLP Violations by Severity | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary, metadata.description) = /Violation/ nocase
    
    $Severity = security_result.severity
    $Severity != "UNKNOWN_SEVERITY"
    
    match:
      $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 DLP Rules | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary, metadata.description) = /Violation/ nocase
    
    $Violation = strings.coalesce(security_result.rule_name, metadata.product_event_type, security_result.summary, metadata.description)
    
    match:
      $Violation
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
      10  
  
Recent Role Creations, Modifications, and Deletions | 
    
    
    metadata.product_event_type = /CreateRole|add role definition/ nocase
    or metadata.product_event_type = /UpdateRole|update role(?: definition)?/ nocase
    or metadata.product_event_type = /DeleteRole|delete role definition/ nocase
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    $Product_Event = metadata.product_event_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Initiator = principal.user.userid
    $Role = strings.coalesce(target.user.attribute.roles.name, target.resource.product_object_id, target.resource.name)
    
    match:
      $Date, $Product_Event, $Source_IP, $Hostname, $Initiator, $Role
    
    order:
      $Date desc  
  
Recent Permission Changes | 
    
    
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    $Log_Source = metadata.log_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Initiator = principal.user.userid
    $Description = metadata.description
    
    match:
      $Date, $Log_Source, $Source_IP, $Hostname, $Initiator, $Description
    
    order:
      $Date desc  
  
Blocked Network Traffic Over Time by Reason | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    security_result.action = "BLOCK"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Reason = security_result.summary
    
    match:
      $Date, $Reason
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
User Events Over Time | 
    
    
    metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Event_Type = metadata.event_type
    
    match:
      $Date, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Applications Accessed | 
    
    
    $Log_Type = metadata.log_type
    $Application = target.application
    $Application != ""
    
    match:
      $Log_Type, $Application
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Outbound IPs by Traffic Volume | 
    
    
    network.direction = "OUTBOUND"
    
    $Log_Type = metadata.log_type
    $Destination_IP = target.ip
    
    match:
      $Log_Type, $Destination_IP
    
    outcome:
      $Total_Bytes = sum(network.received_bytes + network.sent_bytes)/(1000*1000*1000)
    
    order:
      $Total_Bytes desc
    
    limit:
        10  
  
Devices Over Time | 
    
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Device = group(principal.asset.hostname, principal.hostname, target.asset.hostname, target.hostname)
    
    match:
      $Date
    
    outcome:
      $Count = count_distinct($Device)
    
    order:
      $Date desc  
  
Password Changes Over Time | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
## ISO27001 - Physical Controls

This dashboard centralizes data on compliance with physical security categories, offering security teams a clear view of control effectiveness. It presents key metrics on access control efficacy and removable media events, which are crucial for quickly identifying vulnerabilities and prioritizing remediation efforts. The dashboard enables data-driven decision-making to mitigate risks and continuously improve your organization's physical security posture in alignment with `ISO 27001` standards.

**Note:** Apply the available filters to refine the results.

Remote Access by SeverityRecent Removable Media EventsUser Badge-Ins Over TimeTop 10 Recent User Badge-InsTop 10 Sensor LocationsSensor Locations Over Time

Chart name | Query example  
---|---  
Remote Access by Severity | 
    
    
    metadata.event_type = "NETWORK_CONNECTION"
    target.port = 22
    or target.port = 3389
    
    $Severity = security_result.severity
    $Severity != "UNKNOWN_SEVERITY"
    
    match:
      $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Recent Removable Media Events | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.summary) = /\busb\b/ nocase
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    $USB_Event = strings.coalesce(metadata.product_event_type, security_result.summary)
    $Category = strings.coalesce(security_result.category_details, security_result.detection_fields["Category"])
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    match:
      $Date, $USB_Event, $User, $Hostname, $Source_IP, $Category
    
    order:
      $Date desc  
  
User Badge-Ins Over Time | 
    
    
    metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_UNCATEGORIZED"
    strings.coalesce(metadata.description, security_result.action_details, security_result.description, security_result.summary, additional.fields["plasectrxEvtypename"]) = /(?:access\sgranted|badge\sin)/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Recent User Badge-Ins | 
    
    
    metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_UNCATEGORIZED"
    strings.coalesce(metadata.description, security_result.action_details, security_result.description, security_result.summary, additional.fields["plasectrxEvtypename"]) = /(?:access\sgranted|badge\sin)/ nocase
    
    $User = strings.coalesce(principal.user.user_display_name, principal.user.email_addresses, additional.fields["person"], principal.user.userid)
    $Location = strings.coalesce(security_result.rule_labels["Place"], additional.fields["site"], target.location.name, principal.resource.name)
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    
    match:
      $Date, $User, $Location
    
    order:
      $Date desc
    
    limit:
        10  
  
Top 10 Sensor Locations | 
    
    
    metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_UNCATEGORIZED"
    
    $Location = strings.coalesce(security_result.rule_labels["Place"], additional.fields["site"], target.location.name, principal.resource.name)
    $Location != ""
    
    match:
      $Location
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Sensor Locations Over Time | 
    
    
    metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_UNCATEGORIZED"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Location = strings.coalesce(security_result.rule_labels["Place"], additional.fields["site"], target.location.name, principal.resource.name)
    $Location != ""
    
    match:
      $Date, $Location
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
## Living Off the Land Activity

This dashboard provides critical insights into potential misuse of trusted system tools and processes by attackers. This dashboard tracks and visualizes activity related to system utilities like `rundll32`, `regsvr32`, `mshta.exe`, and others, which are commonly leveraged by advanced threats to evade detection.

Suspicious msiexec ExecutionSuspicious mshta.exe Process CreationSuspicious Execution of Regsvr32Outbound Connections Initiated by Rundll32.exeSuspicious Execution of Rundll32Suspicious CertUtil CommandsSuspicious WMI ScriptsSuspicious Regsvr32 Network Connections

Chart name | Query example  
---|---  
Suspicious msiexec Execution | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    target.process.file.full_path = /msiexec/
    target.process.command_line = /:\/\//
    
    $Hostname = principal.hostname
    $Parent_Process = principal.process.file.full_path
    $Target_Process = target.process.file.full_path
    $Command_Line = target.process.command_line
    $Timestamp = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    
    match:
      $Hostname, $Parent_Process, $Target_Process, $Command_Line, $Timestamp
    order:
      $Timestamp desc
    limit:
        50  
  
Suspicious mshta.exe Process Creation | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    principal.process.file.full_path = /(cmd|cscript|powershell|pwsh|regsvr32|rundll32|wscript)\.exe/
    target.process.file.full_path = /mshta.exe/
    
    $Hostname = principal.hostname
    $Parent_Process = principal.process.file.full_path
    $Target_Process = target.process.file.full_path
    $Command_Line = target.process.command_line
    $timestamp = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    
    match:
      $Hostname, $Parent_Process, $Target_Process, $Command_Line, $timestamp
    order:
      $timestamp desc
    limit:
        50  
  
Suspicious Execution of Regsvr32 | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    target.process.command_line = /regsvr32/ nocase
    target.process.command_line = /ProgramData|Temp\b|Users\\Public|Windows\\Temp|AppData\\Local\\Temp|AppData\\Roaming/ nocase
    
    $Hostname = principal.hostname
    $Parent_Process = principal.process.file.full_path
    $Target_Process = target.process.file.full_path
    $Command_Line = target.process.command_line
    $timestamp = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    
    match:
      $Hostname, $Parent_Process, $Target_Process, $Command_Line, $timestamp
    order:
      $timestamp desc
    limit:
        50  
  
Outbound Connections Initiated by Rundll32.exe | 
    
    
    metadata.event_type = "NETWORK_CONNECTION"
    principal.process.file.full_path = /rundll32/ nocase
    network.direction = "OUTBOUND"
    target.ip != /^(10\b|127|192\.168|172\.(1[6-9]|2[0-9]|3[01]))/
    principal.process.command_line != /PcaSvc\.dll|PcaPatchSdbTask/ nocase
    
    $Hostname = principal.hostname
    $Process_Name = principal.process.file.full_path
    $Destination_IP = target.ip
    $Command_Line = principal.process.command_line
    $timestamp = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    
    match:
      $Hostname, $Process_Name, $Destination_IP, $Command_Line, $timestamp
    order:
      $timestamp desc
    limit:
        50  
  
Suspicious Execution of Rundll32 | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    principal.process.command_line != /Shell32\.dll|Control_RunDLL|\.cpl/ nocase
    target.process.command_line = /rundll32.*(javascript|\.RegisterXLL|OpenURL|OpenURLA|FileProtocolHandler|(url|zipfldr|shell32|mshtml|advpack|ieadvpack|ieframe|shdocvw|syssetup|setupapi|pcwutl|dfshim|scrobj|shimgvw|comsvcs)\.dll|RouteTheCall|Control_RunDLL|ShellExec_RunDLL|PrintHTML|LaunchINFSection|RegisterOCX|SetupInfObjectInstallAction|InstallHinfSection|LaunchApplication|ShOpenVerbApplication|http|ImageView_Fullscreen|MiniDump)/ nocase
    
    $Hostname = principal.hostname
    $Parent_Process = strings.coalesce(principal.process.file.full_path, principal.file.full_path)
    $Target_Process = strings.coalesce(target.process.file.full_path, target.file.full_path)
    $Command_Line = target.process.command_line
    $timestamp = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    
    match:
      $Hostname, $Parent_Process, $Target_Process, $Command_Line, $timestamp
    order:
      $timestamp desc
    limit:
        50  
  
Suspicious CertUtil Commands | 
    
    
    target.process.command_line = /certutil.*(decode|encode|urlcache|verifyctl|encodehex|decodehex)/
    
    $Hostname = principal.hostname
    $Parent_Process = principal.process.file.full_path
    $Target_Process = target.process.file.full_path
    $Command_Line = target.process.command_line
    $Timestamp = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    
    match:
      $Hostname, $Parent_Process, $Target_Process, $Command_Line, $Timestamp
    order:
      $Timestamp desc
    limit:
        50  
  
Suspicious WMI Scripts | 
    
    
    target.process.command_line = /(jscript|vbscript)\.dll|format:/
    target.process.file.full_path = /wmi.*\.exe/ nocase
    
    $Hostname = principal.hostname
    $Parent_Process = principal.process.file.full_path
    $Target_Process = target.process.file.full_path
    $Command_Line = target.process.command_line
    $Timestamp = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    
    match:
      $Hostname, $Parent_Process, $Target_Process, $Command_Line, $Timestamp
    order:
      $Timestamp
    limit:
        50  
  
Suspicious Regsvr32 Network Connections | 
    
    
    metadata.event_type = "NETWORK_CONNECTION"
    principal.process.file.full_path = /regsvr32/
    target.ip != /^(10\b|127|169\.254|172\.16|224|100\.64|198\.(18|51\.100)|203\.0\.113|240|192\.(0\.2|0\.0\.(8|9|10|170|171)|0|31\.196|52\.193|168|88\.99|175\.48))/
    
    $Hostname = principal.hostname
    $Process_Name = principal.process.file.full_path
    $Command_Line = principal.process.command_line
    $Destination_IP = target.ip
    $timestamp = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    
    match:
      $Hostname, $Process_Name, $Destination_IP,  $Command_Line, $timestamp
    order:
      $timestamp desc
    limit:
        50  
  
## MITRE ATT&CK Tagged Events

This dashboard provides an overview of detection activities based on the MITRE ATT&CK framework, tracking detections and highlighting trends to identify emerging threats. It helps an organization and security teams better understand their environment by showcasing and mapping tactics, techniques and procedures (TTPs), enhancing threat detection and response, and ensuring proactive defense against cyber threats.

New Tactics & Techniques - Last 7 DaysTechniques Trend Over TimeTop 10 Identified TechniquesTactics Trend Over TimeTotal Vendor Alerts by TacticsTactics Identified by UserTechniques Identified by HostnameTactics Identified by HostnameTechniques Identified by UserSeverity Distribution of MITRE EventsEvents by Tactic and Technique

Chart name | Query example  
---|---  
New Tactics & Techniques - Last 7 Days | 
    
    
    strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"]) != ""
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) != ""
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    
    $Tactic = strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    $Tactic != "-"
    $Technique = strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    $Technique != "-"
    
    match:
      $Tactic, $Technique
    
    outcome:
      $First_Seen = timestamp.get_timestamp(min(metadata.event_timestamp.seconds), "%F %T")
      $Last_Seen = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Diff_First_Seen = timestamp.diff(timestamp.current_seconds(), min(metadata.event_timestamp.seconds), "DAY")
    
    order:
      $Diff_First_Seen asc  
  
Techniques Trend Over Time | 
    
    
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    
    $Technique = strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    $Technique != "-"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Technique
    
    outcome:
      $Count = count(strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    
    order:
      $Date asc   
  
Top 10 Identified Techniques | 
    
    
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    
    $Technique = strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    $Technique != "-"
    
    match:
      $Technique
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"])))
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 Identified Techniques | 
    
    
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    
    $Technique = strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    $Technique != "-"
    
    match:
      $Technique
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"])))
    
    order:
      $Count desc
    
    limit:
        10   
  
Tactics Trend Over Time | 
    
    
    strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"]) != ""
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) != ""
    
    $Tactic = strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    $Tactic != "-"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Tactic
    
    outcome:
      $Count = count(strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    
    order:
      $Date asc   
  
Tactics Trend Over Time | 
    
    
    strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"]) != ""
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) != ""
    
    $Tactic = strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    $Tactic != "-"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Tactic
    
    outcome:
      $Count = count(strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    
    order:
      $Date asc   
  
Total Vendor Alerts by Tactics | 
    
    
    strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"]) != ""
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) != ""
    
    $Tactic = strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    $Tactic != "-"
    $Alert = strings.coalesce(security_result.rule_name, security_result.threat_name, security_result.summary, security_result.description)
    
    match:
      $Tactic, $Alert
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"])))
    
    order:
      $Tactic asc  
  
Tactics Identified by User | 
    
    
    strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"]) != ""
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) != ""
    
    $Tactic = strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    $Tactic != "-"
    $Username = strings.coalesce(principal.user.user_display_name, principal.user.userid)
    $Username != ""
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Hostname != ""
    
    match:
      $Username, $Hostname, $Tactic
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"])))
    
    order:
      $Count desc   
  
Techniques Identified by Hostname | 
    
    
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    
    $Technique = strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    $Technique != "-"
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Hostname != ""
    $IP_Address = strings.coalesce(principal.ip, principal.asset.ip)
    
    match:
      $Hostname, $IP_Address, $Technique
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"])))
    
    order:
      $Count desc  
  
Techniques Identified by Hostname | 
    
    
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    
    $Technique = strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    $Technique != "-"
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Hostname != ""
    $IP_Address = strings.coalesce(principal.ip, principal.asset.ip)
    
    match:
      $Hostname, $IP_Address, $Technique
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"])))
    
    order:
      $Count desc  
  
Tactics Identified by Hostname | 
    
    
    strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"]) != ""
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) != ""
    
    $Tactic = strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    $Tactic != "-"
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Hostname != ""
    $IP_Address = strings.coalesce(principal.ip, principal.asset.ip)
    
    match:
      $Hostname, $IP_Address, $Tactic
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"])))
    
    order:
      $Count desc   
  
Techniques Identified by User | 
    
    
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    strings.coalesce(principal.user.user_display_name, principal.user.userid) != ""
    strings.coalesce(principal.hostname, principal.asset.hostname) != ""
    
    $Technique = strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    $Technique != "-"
    $Username = strings.coalesce(principal.user.user_display_name, principal.user.userid)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    
    match:
      $Username, $Hostname, $Technique
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"])))
    
    order:
      $Count desc  
  
Techniques Identified by User | 
    
    
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    strings.coalesce(principal.user.user_display_name, principal.user.userid) != ""
    strings.coalesce(principal.hostname, principal.asset.hostname) != ""
    
    $Technique = strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    $Technique != "-"
    $Username = strings.coalesce(principal.user.user_display_name, principal.user.userid)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    
    match:
      $Username, $Hostname, $Technique
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"])))
    
    order:
      $Count desc  
  
Total Vendor Alerts by Tactics | 
    
    
    strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"]) != ""
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) != ""
    
    $Tactic = strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    $Tactic != "-"
    $Alert = strings.coalesce(security_result.rule_name, security_result.threat_name, security_result.summary, security_result.description)
    
    match:
      $Tactic, $Alert
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"])))
    
    order:
      $Tactic asc  
  
New Tactics & Techniques - Last 7 Days | 
    
    
    strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"]) != ""
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) != ""
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    
    $Tactic = strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    $Tactic != "-"
    $Technique = strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    $Technique != "-"
    
    match:
      $Tactic, $Technique
    
    outcome:
      $First_Seen = timestamp.get_timestamp(min(metadata.event_timestamp.seconds), "%F %T")
      $Last_Seen = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $First_Seen_Time = min(metadata.event_timestamp.seconds)
      $Last_Seen_Time = max(metadata.event_timestamp.seconds)
      $Diff_First_Seen = math.round(($Last_Seen_Time - $First_Seen_Time)/86400)
    
    order:
      $Diff_First_Seen asc
    
    unselect:
      $First_Seen_Time, $Last_Seen_Time  
  
Tactics Identified by Hostname | 
    
    
    strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"]) != ""
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) != ""
    
    $Tactic = strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    $Tactic != "-"
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Hostname != ""
    $IP_Address = strings.coalesce(principal.ip, principal.asset.ip)
    
    match:
      $Hostname, $IP_Address, $Tactic
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"])))
    
    order:
      $Count desc   
  
Severity Distribution of MITRE Events | 
    
    
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    
    $Severity = security_result.severity
    
    match:
      $Severity
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"])))
    
    order:
      $Count desc  
  
Techniques Trend Over Time | 
    
    
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    
    $Technique = strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    $Technique != "-"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Technique
    
    outcome:
      $Count = count(strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    
    order:
      $Date asc   
  
Events by Tactic and Technique | 
    
    
    strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"]) != ""
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) != ""
    strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"]) != ""
    strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]) != ""
    
    $Tactic = strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    $Tactic != "-"
    $Technique = strings.concat(strings.coalesce(security_result.attack_details.techniques.id, security_result.detection_fields["Technique ID"])," - ", strings.coalesce(security_result.attack_details.techniques.name, security_result.detection_fields["Technique"]))
    $Technique != "-"
    
    match:
      $Tactic, $Technique
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Tactic asc  
  
Tactics Identified by User | 
    
    
    strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"]) != ""
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) != ""
    
    $Tactic = strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]))
    $Tactic != "-"
    $Username = strings.coalesce(principal.user.user_display_name, principal.user.userid)
    $Username != ""
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Hostname != ""
    
    match:
      $Username, $Hostname, $Tactic
    
    outcome:
      $Count = count(strings.concat(strings.coalesce(security_result.attack_details.tactics.id, security_result.detection_fields["Tactic ID"])," - ", strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"])))
    
    order:
      $Count desc   
  
## Microsoft 365 - SharePoint & OneDrive

This dashboard offers a detailed view of user activity, data access, and security events across both platforms. It provides organizations with valuable insights to track file operations, access trends, and user behavior. This dashboard aids in identifying unauthorized access or unusual activity, such as unexpected login locations or anomalies in user patterns.

**Note:** Apply the available filters to refine the results.

User ActivitiesModification of Sharing PoliciesTop 10 SharePoint Sites AccessedTop 10 Active UsersTop 10 Privileged Account ActivityTop 10 File OperationsGeolocation Map on User AccessTop 10 Source IP AddressActivity Trends Over TimeNumber of File Downloads Over TimeFile Downloads

Chart name | Query example  
---|---  
User Activities | 
    
    
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Security_Event_Type = metadata.product_event_type
    $User = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $Application = strings.coalesce(principal.application, target.application, intermediary.application)
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date,$User,$Source_IP, $Application,$Security_Event_Type
    
    outcome:
    
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Modification of Sharing Policies | 
    
    
    metadata.product_event_type = "SharingPolicyChanged"
    
    $Application = strings.coalesce(principal.application, target.application, intermediary.application)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Role = principal.user.attribute.roles.name
    $Policy = target.labels.key
    $Action = target.labels.value
    ($Action = "True" or $Action = "False")
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $User, $Role, $Policy, $Action, $Application
    
    outcome:
      $Count = count(metadata.id)
    order:
      $Count desc  
  
Top 10 SharePoint Sites Accessed | 
    
    
    $Sites = strings.coalesce(target.url,network.http.referral_url,principal.url)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    
    match:
      $Sites, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Active Users | 
    
    
    $User = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $Application = strings.coalesce(principal.application, target.application, intermediary.application)
    
    match:
      $User, $Application
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Privileged Account Activity | 
    
    
    principal.user.attribute.roles.name = /Admin|DcAdmin|Administrator|Root/ nocase //It will be updated as per the client's environment.
    
    $Role = principal.user.attribute.roles.name
    $Security_Event_Type = metadata.product_event_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Resource = if(target.resource.name = "Unknown",target.url,target.resource.name)
    $Application = strings.coalesce(principal.application, target.application, intermediary.application)
    
    match:
      $Role, $Security_Event_Type, $Application
    
    outcome:
      $Username = array_distinct($User)
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 File Operations | 
    
    
    metadata.product_event_type = /File/ nocase
    
    $Security_Event_Type = metadata.product_event_type
    $Action = security_result.action
    
    match:
      $Security_Event_Type, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Geolocation Map on User Access | 
    
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Country = strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region)
    $Country != ""
    
    match:
      $Country
    
    outcome:
        $Count = count($User)
        $Latitude = max(principal.ip_geo_artifact.location.region_latitude)
        $Longitude = max(principal.ip_geo_artifact.location.region_longitude)
    
    order:
        $Count desc  
  
Top 10 Source IP Address | 
    
    
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    
    match:
      $Source_IP, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Activity Trends Over Time | 
    
    
    $Application = strings.coalesce(principal.application, target.application, intermediary.application)
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Application, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Number of File Downloads Over Time | 
    
    
    metadata.product_event_type = "FileDownloaded"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    
    match:
      $Date, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
File Downloads | 
    
    
    metadata.product_event_type = "FileDownloaded"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Downloaded_File = strings.coalesce(src.url,src.file.full_path)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Role = principal.user.attribute.roles.name
    
    match:
      $Date, $User,$Role,$Downloaded_File
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count asc  
  
## Microsoft 365 Alerts

This dashboard provides an overview of security events and potential threats, tracking critical alerts and trends related to user activity.

Top 10 Users by AlertsTop 10 AlertsTop 10 High Severity AlertsRecent Alert DetailsAlerts Severity DistributionAlerts over Time

Chart name | Query example  
---|---  
Top 10 Users by Alerts | 
    
    
    metadata.log_type = "MICROSOFT_GRAPH_ALERT"
    metadata.product_name = "Office 365 Security and Compliance"
    security_result.summary = /threat(?:\s)?management/ nocase
    target.user.userid != ""
    
    $User = target.user.userid
    
    match:
      $User
    outcome:
      $Count = count(metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Top 10 Alerts | 
    
    
    metadata.log_type = "MICROSOFT_GRAPH_ALERT"
    metadata.product_name = "Office 365 Security and Compliance"
    security_result.summary = /threat(?:\s)?management/ nocase
    security_result.rule_name != ""
    
    $Alert = security_result.rule_name
    
    match:
      $Alert
    outcome:
      $Count = count(metadata.id)
    order:
      $Count desc
    limit:
        10
      
  
Top 10 High Severity Alerts | 
    
    
    metadata.log_type = "MICROSOFT_GRAPH_ALERT"
    metadata.product_name = "Office 365 Security and Compliance"
    security_result.severity = "HIGH"
    security_result.summary = /threat(?:\s)?management/ nocase
    security_result.rule_name != ""
    
    $Alert = security_result.rule_name
    
    match:
      $Alert
    outcome:
      $Count = count(metadata.id)
    order:
      $Count desc
    limit:
        10
      
  
Recent Alert Details | 
    
    
    metadata.log_type = "MICROSOFT_GRAPH_ALERT"
    metadata.product_name = "Office 365 Security and Compliance"
    security_result.summary = /threat(?:\s)?management/ nocase
    
    $Alert = security_result.rule_name
    $Description = security_result.description
    $Severity = security_result.severity
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Alert, $Description, $Severity
    outcome:
      $Count = count(metadata.id)
    order:
      $Date desc
    limit:
        50
      
  
Alerts Severity Distribution | 
    
    
    metadata.log_type = "MICROSOFT_GRAPH_ALERT"
    metadata.product_name = "Office 365 Security and Compliance"
    security_result.summary = /threat(?:\s)?management/ nocase
    
    $Severity = security_result.severity
    
    match:
      $Severity
    outcome:
      $Count = count(metadata.id)
    order:
      $Severity desc  
  
Alerts over Time | 
    
    
    metadata.log_type = "MICROSOFT_GRAPH_ALERT"
    metadata.product_name = "Office 365 Security and Compliance"
    security_result.summary = /threat(?:\s)?management/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    outcome:
      $Count = count(metadata.id)
    order:
      $Date asc
      
  
## Mobile Device Management

This dashboard helps security teams monitor organizational mobile devices by providing insights into compliance, threat trends, severity distributions, and user activity to understand the overall security posture. It enables informed decision-making to address vulnerabilities, enforce security policies, and mitigate emerging threats effectively.

**Note:** Apply the available filters to refine the results.

Devices with Outdated / Vulnerable OS VersionsTop 10 Modified ResourcesOS DistributionTop 10 Device ThreatsTop 10 Locations of DevicesNon-Compliant Devices Over TimeTop 10 Users by Login FailureDevices with Recent Threats Over TimePatched Devices Over TimeCritical Devices Over TimeDetected Threats Over TimeDevice Severity DistributionDevice Onboard/Offboard Over TimeEvents Over Time

Chart name | Query example  
---|---  
Devices with Outdated / Vulnerable OS Versions | 
    
    
    (principal.asset.platform_software.platform_version = /Android|IOS|Windows|mac(?:os)?/ nocase
    and not principal.asset.platform_software.platform_version = /Android(?:\s|\/)1[3-6]|IOS(?:\s|\/)1[5-8]|Windows(?:\s|\/)1[0-1]|mac(?:OS)?(?:\s|\/)1[3-5]/ nocase)
    or (target.resource.attribute.labels["OS"] = /Android/ nocase
        and not (target.resource.attribute.labels["Version"] = /1[3-6]/
        or target.resource.attribute.labels["OSversion"] = /1[3-6]/))
    or (target.resource.attribute.labels["OS"] = /IOS/ nocase
        and not (target.resource.attribute.labels["Version"] = /1[5-8]/
        or target.resource.attribute.labels["OSversion"] = /(15|16|17|18).*/))
    or (target.resource.attribute.labels["OS"] = /Windows/ nocase
        and not (target.resource.attribute.labels["Version"] = /10|11/
        or target.resource.attribute.labels["OSversion"] = /10|11/))
    or (target.resource.attribute.labels["OS"] = /mac(?:OS)?/ nocase
        and not (target.resource.attribute.labels["Version"] = /1[3-5]/
        or target.resource.attribute.labels["OSversion"] = /1[3-5]/))
    
    $Device = strings.coalesce(principal.asset.hostname, principal.hostname)
    $OS = strings.coalesce(principal.asset.platform_software.platform_version, target.resource.attribute.labels["OS"])
    $Version = strings.coalesce(target.resource.attribute.labels["Version"], target.resource.attribute.labels["OSversion"])
    
    match:
      $Device, $OS, $Version  
  
Top 10 Modified Resources | 
    
    
    metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    metadata.product_event_type = /Patch MobileApp|Patch ManagedDevice|Patch DeviceConfiguration|(Application|Profile)Modified/ nocase
    
    $Resource_Name = principal.hostname
    $Resource_Name != ""
    
    match:
      $Resource_Name
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
OS Distribution | 
    
    
    $Platform = principal.platform
    
    match:
      $Platform
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Device Threats | 
    
    
    metadata.product_event_type = "THREAT_DETECTED"
    or additional.fields["CompromisedStatus"] = /^Compromised/ nocase
    or security_result.description = /Threat|Compromised/ nocase
    
    $Threat_Event = strings.coalesce(metadata.product_event_type, security_result.category_details, security_result.description)
    
    match:
      $Threat_Event
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Locations of Devices | 
    
    
    $Country = principal.ip_geo_artifact.location.country_or_region
    $Latitude = principal.ip_geo_artifact.location.region_coordinates.latitude
    $Latitude != 0
    $Longitude = principal.ip_geo_artifact.location.region_coordinates.longitude
    $Longitude != 0
    
    match:
      $Country, $Latitude, $Longitude
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Non-Compliant Devices Over Time | 
    
    
    additional.fields["ComplianceState"] = /Not Compliant/ nocase
    or target.resource.attribute.labels["Status"] = /NonCompliant/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count_distinct(principal.hostname)
    
    order:
      $Date desc   
  
Top 10 Users by Login Failure | 
    
    
    (metadata.event_type = "USER_LOGIN"
    or metadata.product_event_type = /user(?:\s|\S|)?login/ nocase
    and security_result.action = "BLOCK" or target.resource.attribute.labels["Status"] = /Failure/ nocase)
    or metadata.product_event_type = /user(?:\s|\S)?login.*(?:failed)?/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $User = principal.user.userid
    $User != ""
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Devices with Recent Threats Over Time | 
    
    
    metadata.product_event_type = "THREAT_DETECTED"
    or additional.fields["CompromisedStatus"] = /^Compromised/ nocase
    or security_result.description = /Threat|Compromised/ nocase
    
    $Device = principal.hostname
    $Device != ""
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Device
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Patched Devices Over Time | 
    
    
    metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    metadata.product_event_type = /Patch MobileApp|Patch ManagedDevice|Patch DeviceConfiguration|(Application|Profile)Modified/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Critical Devices Over Time | 
    
    
    security_result.severity = "CRITICAL"
    or security_result.severity = "HIGH"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count_distinct(principal.hostname)
    
    order:
      $Date desc  
  
Detected Threats Over Time | 
    
    
    metadata.product_event_type = "THREAT_DETECTED"
    or additional.fields["CompromisedStatus"] = /^Compromised/ nocase
    or security_result.description = /Threat|Compromised/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Threat_Event = strings.coalesce(metadata.product_event_type, security_result.category_details, security_result.description)
    
    match:
      $Date, $Threat_Event
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Device Severity Distribution | 
    
    
    $Severity = security_result.severity
    
    match:
      $Severity
    
    outcome:
      $Count = count_distinct(principal.hostname)
    
    order:
      $Count desc  
  
Device Onboard/Offboard Over Time | 
    
    
    metadata.event_type = "USER_RESOURCE_CREATION"
    or metadata.product_event_type = /DEVICE_ENROLLMENT|DeviceEnrolled/ nocase
    or metadata.event_type = "USER_RESOURCE_DELETION"
    or metadata.product_event_type = /^(Deviceun(?:enrolled|enrollment)|BreakMDMConfirmed|Delete\s?(?:ManagedDevice|Device)(?:Requested)?|Retire\s?ManageDevice|DeviceWipeRequested)$/ nocase
    
    $Enrollment = if(metadata.product_event_type = /DEVICE_ENROLLMENT|DeviceEnrolled/ nocase, "Onboard", if(metadata.product_event_type = /^(Deviceun(?:enrolled|enrollment)|BreakMDMConfirmed|Delete\s?(?:ManagedDevice|Device)(?:Requested)?|Retire\s?ManageDevice|DeviceWipeRequested)$/ nocase, "Offboard"))
    $Enrollment != ""
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Enrollment
    
    outcome:
      $Count = count_distinct(principal.hostname)
    
    order:
      $Date desc  
  
Events Over Time | 
    
    
    $Event_Type = metadata.event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
## Multi-Factor Authentication (MFA) Monitoring

This dashboard provides a detailed analysis of MFA implementation and effectiveness across your organization. It offers real-time and historical insights into MFA usage trends, failure alerts, and enrollment status. By monitoring these key aspects, the dashboard helps organizations identify potential vulnerabilities, track authentication performance, and ensure compliance with security protocols, ultimately strengthening overall access security and user management.

Okta MFA Bypass DetectionMFA Failure RateBlocked MFA Attempts by ReasonMFA Attempts Over TimeMFA Attempts by LocationTop 5 Users by Failed MFA AttemptsMFA Usage TrendsTop 5 Applications Accessed via MFAMFA Success RateMFA Enrollment StatusMFA Failure Alerts

Chart name | Query example  
---|---  
Okta MFA Bypass Detection | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_UNCATEGORIZED"
    $vendor = metadata.vendor_name
    $vendor = /Okta/ nocase
    $security_event_type = metadata.product_event_type
    $security_event_type = "user.mfa.attempt_bypass"
    $User = principal.user.user_display_name
    $Summary = security_result.summary
    $Action = security_result.action
    $Action != "UNKNOWN_ACTION"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $User, $Action, $Date,$Summary, $security_event_type
    outcome:
    $Count = count(metadata.id)  
  
MFA Failure Rate | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) or re.regex($requirement, `multiFactorAuthentication`) or re.regex($result_value, `MFA`))
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id =strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $Date
    outcome:
    $total_attempts = count(metadata.id)
    $failure_attempts = sum(if(any security_result.action = "BLOCK", 1, 0))  // Sums only failure MFA attempts
    $failure_rate = (($failure_attempts / $total_attempts) * 100 )
    order:
    $Date asc   
  
Blocked MFA Attempts by Reason | 
    
    
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) nocase or re.regex($requirement, `multiFactorAuthentication`) nocase or re.regex($result_value, `MFA`) nocase)
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $action = security_result.action
    $action = "BLOCK"
    $Reason = security_result.summary
    $Reason != ""
    $Location = principal.location.country_or_region
    match:
    $Reason, $Location
    outcome:
    $Count = count(metadata.id)
    order:
    $Count desc  
  
MFA Attempts Over Time | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) nocase or re.regex($requirement, `multiFactorAuthentication`) nocase or re.regex($result_value, `MFA`) nocase)
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id = strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $action = security_result.action
    $action != "UNKNOWN_ACTION"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Location = principal.location.country_or_region
    match:
    $Date, $Location
    outcome:
    $Count = count(metadata.id)
    order:
    $Date asc  
  
MFA Attempts by Location | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) or re.regex($requirement, `multiFactorAuthentication`) or re.regex($result_value, `MFA`))
    $User = target.user.userid
    $User != ""
    $Action = security_result.action
    $Action !="UNKNOWN_ACTION"
    $Vendor = metadata.vendor_name
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Latitude = principal.location.region_coordinates.latitude
    $Longitude = principal.location.region_coordinates.longitude
    $Location = strings.coalesce(target.location.country_or_region, principal.location.country_or_region)
    match:
    $Vendor, $Date, $Location, $Latitude, $Longitude
    outcome:
    $Count = count(metadata.id)  
  
MFA Attempts by Location | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) nocase or re.regex($requirement, `multiFactorAuthentication`) nocase or re.regex($result_value, `MFA`) nocase)
    $User = target.user.userid
    $User != ""
    $Action = security_result.action
    $Action !="UNKNOWN_ACTION"
    $Vendor = metadata.vendor_name
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Latitude = principal.location.region_coordinates.latitude
    $Longitude = principal.location.region_coordinates.longitude
    $Location = strings.coalesce(target.location.country_or_region, principal.location.country_or_region)
    match:
    $Vendor, $Date, $Location, $Latitude, $Longitude
    outcome:
    $Count = count(metadata.id)  
  
Top 5 Users by Failed MFA Attempts | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) nocase or re.regex($requirement, `multiFactorAuthentication`) nocase or re.regex($result_value, `MFA`) nocase)
    $User = strings.coalesce(target.user.userid, principal.user.userid)
    $User != ""
    $email_id = strings.coalesce(target.user.email_addresses,principal.user.email_addresses)
    $Action = security_result.action
    $Action = "BLOCK"
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $User, $Action
    outcome:
    $Count = count(metadata.id)
    order:
    $Count desc
    limit:5  
  
MFA Usage Trends | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) nocase or re.regex($requirement, `multiFactorAuthentication`) nocase or re.regex($result_value, `MFA`) nocase)
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id = strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $action = security_result.action
    $action != "UNKNOWN_ACTION"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $event_type, $Date
    outcome:
    $Count = count($event_type)
    order:
    $Date asc   
  
Top 5 Applications Accessed via MFA | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) or re.regex($requirement, `multiFactorAuthentication`) or re.regex($result_value, `MFA`))
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id = strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $Application = target.application
    $Application != ""
    match:
    $Application
    outcome:
    $Count = count(metadata.id)
    order:
    $Count desc
    limit : 5  
  
MFA Success Rate | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) nocase or re.regex($requirement, `multiFactorAuthentication`) nocase or re.regex($result_value, `MFA`) nocase)
    $user = strings.coalesce(target.user.userid,principal.user.userid)
    $user !=""
    $email_id =strings.coalesce(target.user.email_addresses,principal.user.email_addresses)
    $action = security_result.action
    $vendor = metadata.vendor_name
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $date
    outcome:
      $total_attempts = count(metadata.id)
      $successful_attempts = sum(if(any security_result.action = "ALLOW", 1, 0))  // Sums only successful MFA attempts
      $success_rate = (($successful_attempts / $total_attempts) * 100 )
    order: $date asc  
  
MFA Success Rate | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) or re.regex($requirement, `multiFactorAuthentication`) or re.regex($result_value, `MFA`))
    $user = strings.coalesce(target.user.userid,principal.user.userid)
    $user !=""
    $email_id =strings.coalesce(target.user.email_addresses,principal.user.email_addresses)
    $action = security_result.action
    $vendor = metadata.vendor_name
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $date
    outcome:
      $total_attempts = count(metadata.id)
      $successful_attempts = sum(if(any security_result.action = "ALLOW", 1, 0))  // Sums only successful MFA attempts
      $success_rate = (($successful_attempts / $total_attempts) * 100 )
    order: $date asc  
  
Top 5 Applications Accessed via MFA | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) nocase or re.regex($requirement, `multiFactorAuthentication`) nocase or re.regex($result_value, `MFA`) nocase)
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id = strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $Application = target.application
    match:
    $Application
    outcome:
    $Count = count(metadata.id)
    order:
    $Count desc
    limit : 5  
  
Blocked MFA Attempts by Reason | 
    
    
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) or re.regex($requirement, `multiFactorAuthentication`) or re.regex($result_value, `MFA`))
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $action = security_result.action
    $action = "BLOCK"
    $Reason = security_result.summary
    $Reason != ""
    $Location = principal.location.country_or_region
    match:
    $Reason, $Location
    outcome:
    $Count = count(metadata.id)
    order:
    $Count desc  
  
MFA Enrollment Status | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_CREATION"
    $security_event_type = metadata.product_event_type
    $security_event_type = "enrollment"
    $product_name = metadata.product_name
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($requirement, `multiFactorAuthentication`) or re.regex($result_value, `MFA`))
    $summary = security_result.summary
    $summary != ""
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id = strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $action = security_result.action
    $vendor = metadata.vendor_name
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $summary
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
MFA Failure Rate | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) nocase or re.regex($requirement, `multiFactorAuthentication`) nocase or re.regex($result_value, `MFA`) nocase)
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id =strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $Date
    outcome:
    $total_attempts = count(metadata.id)
    $failure_attempts = sum(if(any security_result.action = "BLOCK", 1, 0))  // Sums only failure MFA attempts
    $failure_rate = (($failure_attempts / $total_attempts) * 100 )
    order:
    $Date asc   
  
Okta MFA Bypass Detection | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_UNCATEGORIZED"
    $vendor = metadata.vendor_name
    $vendor = /Okta/
    $security_event_type = metadata.product_event_type
    $security_event_type = "user.mfa.attempt_bypass"
    $User = principal.user.user_display_name
    $Summary = security_result.summary
    $Action = security_result.action
    $Action != "UNKNOWN_ACTION"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $User, $Action, $Date,$Summary, $security_event_type
    outcome:
    $Count = count(metadata.id)
    order:
    $Count desc  
  
Top 5 Users by Failed MFA Attempts | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) or re.regex($requirement, `multiFactorAuthentication`) or re.regex($result_value, `MFA`))
    $User = strings.coalesce(target.user.userid, principal.user.userid)
    $User != ""
    $email_id = strings.coalesce(target.user.email_addresses,principal.user.email_addresses)
    $Action = security_result.action
    $Action = "BLOCK"
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $User, $Action
    outcome:
    $Count = count(metadata.id)
    order:
    $Count desc
    limit:5  
  
MFA Attempts Over Time | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) or re.regex($requirement, `multiFactorAuthentication`) or re.regex($result_value, `MFA`))
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id = strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $action = security_result.action
    $action != "UNKNOWN_ACTION"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Location = principal.location.country_or_region
    match:
    $Date, $Location
    outcome:
    $Count = count(metadata.id)
    order:
    $Date asc  
  
MFA Failure Alerts | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) or re.regex($requirement, `multiFactorAuthentication`) or re.regex($result_value, `MFA`))
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id = strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $action = security_result.action
    $action = "BLOCK"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $Date
    outcome:
    $Count = count(metadata.id)
    $Action = array_distinct($action)
    order:
    $Date asc  
  
MFA Failure Alerts | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) nocase or re.regex($requirement, `multiFactorAuthentication`) nocase or re.regex($result_value, `MFA`) nocase)
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id = strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $action = security_result.action
    $action = "BLOCK"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $Date
    outcome:
    $Count = count(metadata.id)
    $Action = array_distinct($action)
    order:
    $Date asc  
  
MFA Enrollment Status | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_CREATION"
    $security_event_type = metadata.product_event_type
    $security_event_type = "enrollment"
    $product_name = metadata.product_name
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($requirement, `multiFactorAuthentication`) nocase or re.regex($result_value, `MFA`) nocase)
    $summary = security_result.summary
    $summary != ""
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id = strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $action = security_result.action
    $vendor = metadata.vendor_name
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $summary
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
MFA Usage Trends | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $product_name = metadata.product_name
    $security_event_type = metadata.product_event_type
    $requirement = additional.fields["AuthenticationRequirement"]
    $result_value = security_result.detection_fields.value
    (re.regex($product_name, "MULTI-FACTOR_AUTHENTICATION") or re.regex($security_event_type, `user.mfa`) or re.regex($requirement, `multiFactorAuthentication`) or re.regex($result_value, `MFA`))
    $user = strings.coalesce(target.user.userid, principal.user.userid)
    $user != ""
    $email_id = strings.coalesce(target.user.email_addresses, principal.user.email_addresses)
    $action = security_result.action
    $action != "UNKNOWN_ACTION"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $event_type, $Date
    outcome:
    $Count = count($event_type)
    order:
    $Date asc   
  
## NIST 800-53 - Access Control

This dashboard provides a comprehensive overview of access control activities aligned with `NIST 800-53` standards. It tracks access trends across sources, policies, and geolocations to identify risks, streamline monitoring, and strengthen access control management. This dashboard uses the reference list `nist_compliance_assets` to scope data to the NIST environment.

**Note:** The charts in this dashboard don't load until the required reference lists are created.

User Account LockoutsRecent Failed Logins (Last 24 Hours)

Chart name | Query example  
---|---  
User Account Lockouts | 
    
    
    metadata.description =  /locked out/ nocase
    
    $Summary = metadata.description
    $Log_Type = metadata.log_type
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname,target.hostname,target.asset.hostname)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses,target.user.userid,target.user.user_display_name,target.user.email_addresses )
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
       $Summary, $User, $Hostname, $Log_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds ), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Recent Failed Logins (Last 24 Hours) | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "BLOCK"
    
    $Log_Type = metadata.log_type
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Summary = strings.coalesce(security_result.summary, security_result.description, metadata.description, security_result.rule_name)
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname,target.hostname,target.asset.hostname)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses,target.user.userid,target.user.user_display_name,target.user.email_addresses )
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Destination_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP, $Destination_IP) in %NIST_Compliance_Assets
    
    match:
       $Summary, $User,$Hostname, $Source_IP, $Log_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds ), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
## NIST 800-53 - Audit and Accountability

This dashboard provides a comprehensive overview of log management, aligned with `NIST 800-53` standards, enabling you to effectively monitor and manage audit logs for security and compliance purposes.

Audit Log Clearing(Windows Events)

Chart name | Query example  
---|---  
Audit Log Clearing(Windows Events) | 
    
    
    (metadata.product_event_type = "104" OR metadata.product_event_type = "1102" )
    
    $Description = metadata.description
    $Event_Type = metadata.event_type
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname)
    $Log_Event = additional.fields["Channel"]
    match:
      $Hostname,$Event_Type,$Description,$Log_Event
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds ), "%F %T")
      $Count = count(metadata.id)
    
    order :
      $Count desc
    
      
  
## NIST 800-53 - Identification & Authentication

This dashboard provides a comprehensive overview of identity and authentication activities, aligned with `NIST 800-53` standards. It tracks key metrics such as password changes, account management, permission updates, and multi-factor authentication (MFA) activity. This tool helps you enforce compliance to identity and authentication processes, ensuring the protection of sensitive systems and data.

MFA Success RatePermission Changes Over TimeTop 10 Initiators Creating User AccountsTop 10 Initiators Deleting User AccountsTop 10 Initiators Creating GroupsUser Events Over TimeEvents Over TimeRecent Role ModificationsRecent Group CreationsTop 10 Initiators Deleting RolesRecent User Account DeletionsTop 10 Initiators Deleting GroupsMFA Failure RateRecent Permission ChangesRecent Group DeletionsTop 10 Initiators Modifying RolesRecent User Account CreationsRecent Role DeletionsTop 10 Initiators Creating RolesRecent Users Account ModificationsPassword Changes Over TimeTop 10 Initiators Modifying GroupsRecent Role CreationsMFA Enrollment StatusTop 10 Initiators Modifying User AccountsRole Events Over TimeRecent Group ModificationsGroup Events Over Time

Chart name | Query example  
---|---  
MFA Success Rate | 
    
    
    metadata.product_name  = "MULTI-FACTOR_AUTHENTICATION"
    or metadata.product_event_type = /mfa(?:\S)?auth|auth(?:.*)?mfa/ nocase
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Successful_Attempts = sum(if(security_result.action = "ALLOW", 1, 0))
      $Success_Rate = (($Successful_Attempts / $Count) * 100)
    
    order:
      $Date desc  
  
Permission Changes Over Time | 
    
    
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Initiators Creating User Accounts | 
    
    
    metadata.event_type = "USER_CREATION"
    security_result.action = "ALLOW"
    
    $Log_Source = metadata.log_type
    $Initiator = principal.user.userid
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Initiator, $Log_Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Initiators Deleting User Accounts | 
    
    
    metadata.event_type = "USER_DELETION"
    security_result.action = "ALLOW"
    
    $Log_Source = metadata.log_type
    $Initiator = principal.user.userid
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Initiator, $Log_Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Initiators Creating Groups | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.product_event_type = /add group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Source = metadata.log_type
    $Initiator = principal.user.userid
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Initiator, $Log_Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
User Events Over Time | 
    
    
    metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Event_Type = metadata.event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Events Over Time | 
    
    
    metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    or metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.event_type = "GROUP_MODIFICATION"
    security_result.action = "ALLOW"
    
    $Event_Type = metadata.event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Recent Role Modifications | 
    
    
    metadata.product_event_type = /UpdateRole|update role(?: definition)?/ nocase
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Log_Source = metadata.log_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Initiator = principal.user.userid
    $Role_Modified = strings.coalesce(target.user.attribute.roles.name, target.resource.product_object_id, target.resource.name)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Source, $Source_IP, $Hostname, $Initiator, $Role_Modified
    
    order:
      $Date desc  
  
Recent Group Creations | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.product_event_type = /add group/ nocase
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Log_Source = metadata.log_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Product_Event = metadata.product_event_type
    $Group_Name = target.group.group_display_name
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Source, $Source_IP, $Hostname, $Product_Event, $Group_Name
    
    order:
      $Date desc   
  
Top 10 Initiators Deleting Roles | 
    
    
    metadata.product_event_type = /DeleteRole|delete role definition/ nocase
    security_result.action = "ALLOW"
    
    $Log_Source = metadata.log_type
    $Initiator = principal.user.userid
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Initiator, $Log_Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent User Account Deletions | 
    
    
    metadata.event_type = "USER_DELETION"
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Log_Source = metadata.log_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Initiator = principal.user.userid
    $User_Deleted = target.user.userid
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Source, $Source_IP, $Hostname, $Initiator, $User_Deleted
    
    order:
      $Date desc   
  
Top 10 Initiators Deleting Groups | 
    
    
    metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /delete group/ nocase
    security_result.action = "ALLOW"
    
    $Log_Source = metadata.log_type
    $Initiator = principal.user.userid
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Initiator, $Log_Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
MFA Failure Rate | 
    
    
    metadata.product_name  = "MULTI-FACTOR_AUTHENTICATION"
    or metadata.product_event_type = /mfa(?:\S)?auth|auth(?:.*)?mfa/ nocase
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Failed_Attempts = sum(if(security_result.action = "BLOCK", 1, 0))
      $Failure_Rate = (($Failed_Attempts / $Count) * 100 )
    
    order:
      $Date desc  
  
Recent Permission Changes | 
    
    
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Log_Source = metadata.log_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Initiator = principal.user.userid
    $Description = metadata.description
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Source, $Source_IP, $Hostname, $Initiator, $Description
    
    order:
      $Date desc  
  
Recent Group Deletions | 
    
    
    metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /delete group/ nocase
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Log_Source = metadata.log_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Product_Event = metadata.product_event_type
    $Group_Name = target.group.group_display_name
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Source, $Source_IP, $Hostname, $Product_Event, $Group_Name
    
    order:
      $Date desc  
  
Top 10 Initiators Modifying Roles | 
    
    
    metadata.product_event_type = /UpdateRole|update role(?: definition)?/ nocase
    security_result.action = "ALLOW"
    
    $Log_Source = metadata.log_type
    $Initiator = principal.user.userid
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Initiator, $Log_Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent User Account Creations | 
    
    
    metadata.event_type = "USER_CREATION"
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Log_Source = metadata.log_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Initiator = principal.user.userid
    $User_Created = target.user.userid
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Source, $Source_IP, $Hostname, $Initiator, $User_Created
    
    order:
      $Date desc   
  
Recent Role Deletions | 
    
    
    metadata.product_event_type = /DeleteRole|delete role definition/ nocase
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Log_Source = metadata.log_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Initiator = principal.user.userid
    $Role_Deleted = strings.coalesce(target.user.attribute.roles.name, target.resource.product_object_id, target.resource.name)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Source, $Source_IP, $Hostname, $Initiator, $Role_Deleted
    
    order:
      $Date desc  
  
Top 10 Initiators Creating Roles | 
    
    
    metadata.product_event_type = /CreateRole|add role definition/ nocase
    security_result.action = "ALLOW"
    
    $Log_Source = metadata.log_type
    $Initiator = principal.user.userid
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Initiator, $Log_Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Users Account Modifications | 
    
    
    metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Log_Source = metadata.log_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Initiator = principal.user.userid
    $User_Modified = target.user.userid
    $Event_Type = metadata.event_type
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Source, $Source_IP, $Hostname, $Initiator, $Event_Type, $User_Modified
    
    order:
      $Date desc   
  
Password Changes Over Time | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Initiators Modifying Groups | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    and metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "ALLOW"
    
    $Log_Source = metadata.log_type
    $Initiator = principal.user.userid
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Initiator, $Log_Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Role Creations | 
    
    
    metadata.product_event_type = /CreateRole|add role definition/ nocase
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Log_Source = metadata.log_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Initiator = principal.user.userid
    $Role_Created = strings.coalesce(target.user.attribute.roles.name, target.resource.product_object_id, target.resource.name)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Source, $Source_IP, $Hostname, $Initiator, $Role_Created
    
    order:
      $Date desc  
  
MFA Enrollment Status | 
    
    
    metadata.product_name  = "MULTI-FACTOR_AUTHENTICATION"
    or strings.coalesce(additional.fields["AuthenticationRequirement"], security_result.detection_fields.value) = /mfa|multi(?:\s|\S)?factor(?:\s|\S)?authentication|/ nocase
    
    metadata.product_event_type = "enrollment"
    or target.resource_ancestors.resource_subtype = "AuthenticatorEnrollment"
    
    $Result = security_result.summary
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Result
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Initiators Modifying User Accounts | 
    
    
    metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Log_Source = metadata.log_type
    $Initiator = principal.user.userid
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Initiator, $Log_Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Role Events Over Time | 
    
    
    metadata.product_event_type = /CreateRole|add role definition/ nocase
    or metadata.product_event_type = /DeleteRole|delete role definition/ nocase
    or metadata.product_event_type = /UpdateRole|update role(?: definition)?/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Product_Event = metadata.product_event_type
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date,  $Product_Event
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Recent Group Modifications | 
    
    
    metadata.event_type = "GROUP_MODIFICATION"
    and metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Log_Source = metadata.log_type
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $Product_Event = metadata.product_event_type
    $Group_Name = target.group.group_display_name
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Source, $Source_IP, $Hostname, $Product_Event, $Group_Name
    
    order:
      $Date desc  
  
Group Events Over Time | 
    
    
    metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /add group/ nocase
    or metadata.product_event_type = /delete group/ nocase
    or (metadata.event_type = "GROUP_MODIFICATION"
    and metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase)
    
    $Event_Type = metadata.event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc   
  
## NIST 800-53 - Media Protection

This dashboard provides a comprehensive overview of media protection activities, aligned with `NIST 800-53` standards. It tracks security events by action, and frequency, highlighting key trends such as frequently triggered rules, top hosts, IP addresses, and users. This tool helps you enforce compliance to protect sensitive media assets.

Top 10 Users by ActionTop 10 Source Hostnames by ActionTop 10 Vendor Alert LocationsRecent Vendor AlertsTop 10 Vendor Alerts by ActionTop 10 Source IPs by ActionEvents Over Time by Action

Chart name | Query example  
---|---  
Top 10 Users by Action | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary) = /\busb|removable|drive\b/ nocase
    
    $Action = security_result.action
    $User = principal.user.userid
    $User != ""
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $User, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source Hostnames by Action | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary) = /\busb|removable|drive\b/ nocase
    
    $Action = security_result.action
    $Hostname = principal.hostname
    $Hostname != ""
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Hostname, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Vendor Alert Locations | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary) = /\busb|removable|drive\b/ nocase
    
    $Alert = strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary)
    $Country = target.location.country_or_region
    $Latitude = target.location.region_coordinates.latitude
    $Longitude = target.location.region_coordinates.longitude
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Alert, $Country, $Latitude, $Longitude
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Vendor Alerts | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary) = /\busb|drive\b/ nocase
    
    $Vendor_Alert = strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary)
    $User = strings.coalesce(principal.user.user_display_name, target.user.user_display_name)
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $File_Name = target.file.full_path
    $Action = security_result.action
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Vendor_Alert, $Source_IP, $User, $File_Name, $Action
    
    order:
      $Date desc  
  
Top 10 Vendor Alerts by Action | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary) = /\busb|removable|drive\b/ nocase
    
    $Action = security_result.action
    $Alerts = strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Alerts, $Action
    
    outcome:
      $Count = count_distinct(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs by Action | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary) = /\busb|removable|drive\b/ nocase
    
    $Action = security_result.action
    $IP_Address = principal.ip
    $IP_Address != ""
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $IP_Address, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Events Over Time by Action | 
    
    
    strings.coalesce(metadata.product_event_type, security_result.rule_name, security_result.summary) = /\busb|removable|drive\b/ nocase
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
## NIST 800-53 - System and Communication Protection

This dashboard enhances security and compliance by providing insights into system and network defenses. It monitors EDR sensor activity, IDS/IPS events, DDOs and network traffic anomalies to detect potential threats, ensuring adherence to NIST security standards. It uses the reference list `nist_compliance_assets` to scope data to the NIST environment.

**Note:** The charts in this dashboard don't load until the required reference lists are created.

IDS / IPS Events by CategoryDDOS ActivitiesNetwork Traffic Over Time by ActionInbound Blocked Traffic by GeolocationUSB EventsNetwork-based Malicious ActivitiesEDR Vendor AlertsWeak Encrypted Communication Over Time by Log TypeTop 10 IDS / IPS Vendor Alert by SeverityTop 10 Hosts in EDR Events by Log TypeOutbound Blocked Traffic by GeolocationNetwork traffic Over Time by Direction

Chart name | Query example  
---|---  
IDS / IPS Events by Category | 
    
    
    metadata.event_type = "SCAN_UNCATEGORIZED"
    or metadata.event_type = "SCAN_NETWORK"
    or metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Category = security_result.category
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname, target.asset.hostname, target.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Destination_IP = strings.coalesce(target.asset.ip, target.ip)
    //strings.coalesce($Hostname, $Destination_IP, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Category
    
    outcome:
      $Count = count(metadata.id)
    
      
  
DDOS Activities | 
    
    
    (metadata.log_type = /ddos/ nocase or (security_result.description  = /ddos/ nocase or security_result.summary  = /ddos/ nocase or metadata.description = /ddos/ nocase or security_result.rule_name = /ddos/ nocase or metadata.product_event_type = /ddos/ nocase))
    
    $Summary = strings.coalesce(security_result.description, security_result.summary, metadata.description, security_result.rule_name, metadata.product_event_type)
    $Action = security_result.action
    $Log_Type = metadata.log_type
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.asset.hostname, target.hostname)
    $Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    $Destination_IP = strings.coalesce(target.asset.ip, target.ip)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $Source_IP, $Destination_IP) in %NIST_Compliance_Assets
    
    match:
      $Summary, $Hostname, $Source_IP, $Destination_IP, $Action, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
      
  
Network Traffic Over Time by Action | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname,target.hostname, target.asset.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Destination_IP = strings.coalesce(target.asset.ip, target.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
          
  
Inbound Blocked Traffic by Geolocation | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    security_result.action = "BLOCK"
    network.direction = "INBOUND"
    
    $Country = principal.location.country_or_region
    $Country != ""
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname, target.asset.hostname, target.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Destination_IP = strings.coalesce(target.asset.ip, target.ip)
    //strings.coalesce($Hostname, $Source_IP, $Destination_IP) in %NIST_Compliance_Assets
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(principal.location.region_coordinates.latitude)
      $Longitude = max(principal.location.region_coordinates.longitude)
    
    order:
      $Count desc  
  
USB Events | 
    
    
    (metadata.product_event_type = /usb/ nocase or security_result.summary = /usb/ nocase )
    
    $Log_Type = metadata.log_type
    $USB_Event = strings.coalesce(metadata.product_event_type, security_result.summary)
    $Category = security_result.category_details
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Log_Type, $USB_Event, $User, $Hostname, $Source_IP, $Category
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
      
  
Network-based Malicious Activities | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    (security_result.category = "NETWORK_DENIAL_OF_SERVICE" or security_result.category = "NETWORK_MALICIOUS" or security_result.category = "NETWORK_SUSPICIOUS" or security_result.category = "SOFTWARE_MALICIOUS" or security_result.category = "SOFTWARE_SUSPICIOUS" or security_result.category = "NETWORK_RECON")
    
    $Log_Type = metadata.log_type
    $Category = security_result.category
    $Summary = strings.coalesce(security_result.description, security_result.summary, metadata.description, security_result.rule_name, metadata.product_event_type)
    $Hostname = strings.coalesce(principal.asset.hostname, principal.hostname, target.hostname, target.asset.hostname)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Destination_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP, $Destination_IP) in %NIST_Compliance_Assets
    
    match:
      $Summary, $Category, $Hostname, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
    
      
  
EDR Vendor Alerts | 
    
    
    $Log_Type = metadata.log_type
    $Rule_Name = security_result.rule_name
    $Severity = security_result.severity
    $User = strings.coalesce(principal.user.user_display_name, principal.user.email_addresses, principal.user.userid, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Rule_Name, $Severity, $User, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
      
  
Weak Encrypted Communication Over Time by Log Type | 
    
    
    network.tls.cipher = /RSA|DES|RC4|SHA-1|3DES|MD5/ nocase
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname, target.asset.hostname, target.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Destination_IP = strings.coalesce(target.asset.ip, target.ip)
    //strings.coalesce($Hostname, $Source_IP, Destination_IP) in %NIST_Compliance_Assets
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
      
  
Top 10 IDS / IPS Vendor Alert by Severity | 
    
    
    metadata.event_type = "SCAN_UNCATEGORIZED"
    or metadata.event_type = "SCAN_NETWORK"
    or metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    (security_result.severity = "HIGH" or security_result.severity = "CRITICAL")
    
    $Rule_Name = security_result.rule_name
    $Rule_Name != ""
    $Severity = security_result.severity
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname, target.asset.hostname, target.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Destination_IP = strings.coalesce(target.asset.ip, target.ip)
    //strings.coalesce($Hostname, $Destination_IP, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Rule_Name, $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Hosts in EDR Events by Log Type | 
    
    
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Hostname != ""
    $Log_Type = metadata.log_type
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //strings.coalesce($Hostname, $Source_IP) in %NIST_Compliance_Assets
    
    match:
      $Hostname, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Outbound Blocked Traffic by Geolocation | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    security_result.action = "BLOCK"
    network.direction = "OUTBOUND"
    
    $Country = principal.location.country_or_region
    $Country != ""
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname, target.asset.hostname, target.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Destination_IP = strings.coalesce(target.asset.ip, target.ip)
    //strings.coalesce($Hostname, $Source_IP, $Destination_IP) in %NIST_Compliance_Assets
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(principal.location.region_coordinates.latitude)
      $Longitude = max(principal.location.region_coordinates.longitude)
    
    order:
      $Count desc  
  
Network traffic Over Time by Direction | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    //If the user requires any inclusions for specific assets, these lines will need to be enabled in the query and update the NIST_Compliance_Assets reference list as needed.
    //$Hostname = strings.coalesce(principal.asset.hostname, principal.hostname, target.asset.hostname, target.hostname)
    //$Source_IP = strings.coalesce(principal.asset.ip, principal.ip)
    //$Destination_IP = strings.coalesce(target.asset.ip, target.ip)
    //strings.coalesce($Hostname, $Source_IP, $Destination_IP) in %NIST_Compliance_Assets
    
    $Direction = network.direction
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Direction, $Date
    
    outcome:
      $Total_Volume = sum(network.sent_bytes) + sum(network.received_bytes)
      $Total_Volume_GB = math.round($Total_Volume/ (1000 * 1000 * 1000), 2)
          
  
## Network Traffic Overview

This dashboard offers real-time monitoring of cloud and on-premises network traffic by IP address, protocol, vendor, alert, and region, enabling effective analysis of traffic volume and potential issues.

Network EventsTop 10 Source IPs in Vendor AlertsTop 10 Blocked UsersTop 10 Events by Bytes SentVendor Alerts Over Time by ActionEvents Over Time by Log TypeTop 10 Outbound IPs by Traffic VolumeVendor alerts over time by Log TypeTop 10 Source IP AddressTop 10 Vendor AlertsDistinct Destination IPsWeak TLS Version Usage Over TimeTop 10 Users by Traffic VolumeTop 10 Applications by Bytes SentInbound vs. Outbound Traffic Volume Over TimeMean BytesTraffic Volume by IP Over TimeTop 10 Traffic Volume Source LocationsEvents by SeverityInbound Traffic Location HeatmapTop 10 Services by Traffic VolumeTop 10 Ports by Traffic - OutboundDistinct Source IPsTraffic Volume by Log Type Over TimeTotal Bytes SentStandard Deviation BytesOutbound Traffic Location HeatmapTop 10 Blocked Source Ip to Destination IPTop 10 Ports by Traffic - InboundTop 10 Blocked CountriesTop 10 Destination IP AddressNetwork Protocol Distribution Over TimeTop 10 Suspicious Target FilesTop 10 Users in Vendor AlertsTop 10 URLsAllowed vs. Blocked Network TrafficTop 10 Hosts by Traffic SizeTarget port by ProtocolTop 10 Allowed ConnectionsInbound Traffic Over Time by ActionAverage BytesTop 10 Blocked countriesOutbound Traffic Over Time by ActionTop 10 events categoryTop 10 Inbound IPs by Traffic VolumeTop 10 Network ConnectionsTop 10 Blocked Source IP Address

Chart name | Query example  
---|---  
Network Events | 
    
    
    $event.metadata.event_type = "NETWORK_FLOW"
    or $event.metadata.event_type = "NETWORK_CONNECTION"
    or $event.metadata.event_type = "NETWORK_FTP"
    or $event.metadata.event_type = "NETWORK_DHCP"
    or $event.metadata.event_type = "NETWORK_DNS"
    or $event.metadata.event_type = "NETWORK_HTTP"
    or $event.metadata.event_type = "NETWORK_SMTP"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Top 10 Source IPs in Vendor Alerts | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    security_result.rule_name != ""
    
    $Source_IP =  strings.coalesce(principal.ip, principal.asset.ip)
    
    match:
      $Source_IP
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Blocked Users | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    (security_result.action = "BLOCK" or security_result.action = "FAIL" or security_result.action_details = /fail|block/ nocase)
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Events by Bytes Sent | 
    
    
    $Source_IP = principal.ip
    $Event_Type = metadata.event_type
    
    match:
      $Event_Type, $Source_IP
    
    outcome:
      $Bytes_Sent = sum(network.sent_bytes) / (1000*1000*1000)
    
    order:
      $Bytes_Sent desc
    
    limit:
        10  
  
Vendor Alerts Over Time by Action | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    security_result.rule_name != ""
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Events Over Time by Log Type | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Log_type = metadata.log_type
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Outbound IPs by Traffic Volume | 
    
    
    network.direction = "OUTBOUND"
    
    $Log_Type = metadata.log_type
    $Destination_IP = target.ip
    
    match:
      $Log_Type, $Destination_IP
    
    outcome:
      $Total_Bytes = sum(network.received_bytes + network.sent_bytes) / (1000*1000*1000)
    
    order:
      $Total_Bytes desc
    
    limit:
        10  
  
Vendor alerts over time by Log Type | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    security_result.rule_name != ""
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date , $Log_Type
    
    outcome:
      $Count = count(security_result.rule_name)
    
    order:
      $Date asc  
  
Top 10 Source IP Address | 
    
    
    $event.metadata.event_type = "NETWORK_FLOW"
     or $event.metadata.event_type = "NETWORK_CONNECTION"
     or $event.metadata.event_type = "NETWORK_FTP"
     or $event.metadata.event_type = "NETWORK_DHCP"
     or $event.metadata.event_type = "NETWORK_DNS"
     or $event.metadata.event_type = "NETWORK_HTTP"
     or $event.metadata.event_type = "NETWORK_SMTP"
    
    $Event_Type = $event.metadata.event_type
    $Source_IP = $event.principal.ip
    $Source_IP != ""
    
    match:
       $Source_IP, $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Vendor Alerts | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Rule_Name = security_result.rule_name
    
    match:
      $Rule_Name
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Distinct Destination IPs | 
    
    
    $event.metadata.event_type = "NETWORK_FLOW"
    or $event.metadata.event_type = "NETWORK_CONNECTION"
    or $event.metadata.event_type = "NETWORK_FTP"
    or $event.metadata.event_type = "NETWORK_DHCP"
    or $event.metadata.event_type = "NETWORK_DNS"
    or $event.metadata.event_type = "NETWORK_HTTP"
    or $event.metadata.event_type = "NETWORK_SMTP"
    
    outcome:
      $Count = count_distinct($event.target.ip)  
  
Weak TLS Version Usage Over Time | 
    
    
    network.tls.version != /1(\.|_)?(2|3)/ nocase
    
    $Cipher_Version = network.tls.version
    $Cipher_Version != ""
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Cipher_Version, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Users by Traffic Volume | 
    
    
    $User = principal.user.userid
    
    match:
      $User
    
    outcome:
      $Total_Bytes = sum(network.sent_bytes + network.received_bytes) / (1000*1000*1000)
    
    order:
      $Total_Bytes desc
    
    limit:
      10  
  
Top 10 Applications by Bytes Sent | 
    
    
    $Source_IP = principal.ip
    $Application = target.application
    
    match:
      $Application, $Source_IP
    
    outcome:
      $Total_Bytes = sum(network.sent_bytes) / (1000*1000*1000)
    
    order:
      $Total_Bytes desc
    
    limit:
        10  
  
Inbound vs. Outbound Traffic Volume Over Time | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Direction = network.direction
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Direction, $Date
    
    outcome:
      $Total_Volume = sum(network.sent_bytes) + sum(network.received_bytes)
      $Total_Volume_GB = $Total_Volume/ (1000 * 1000 * 1000)
    
    order:
      $Date desc  
  
Mean Bytes | 
    
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Total_Bytes = sum(network.sent_bytes + network.received_bytes) / 2
      $Mean_GB_Total = math.round($Total_Bytes / 1073741824, 2)
    
    order:
      $Date desc  
  
Traffic Volume by IP Over Time | 
    
    
    $IP_Address = principal.ip
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $IP_Address, $Date
    
    outcome:
      $Total_Bytes = sum(network.sent_bytes + network.received_bytes) / (1000*1000*1000)
    
    order:
      $Date desc  
  
Top 10 Traffic Volume Source Locations | 
    
    
    $Country = principal.location.country_or_region
    $Country != ""
    $Latitude = principal.location.region_coordinates.latitude
    $Longitude = principal.location.region_coordinates.longitude
    
    match:
      $Country, $Latitude, $Longitude
    
    outcome:
      $Total_Bytes = sum(network.received_bytes + network.sent_bytes) / (1000*1000*1000)
    
    order:
      $Total_Bytes desc
    
    limit:
        10  
  
Events by Severity | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Severity = security_result.severity
    
    match:
      $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Inbound Traffic Location Heatmap | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    network.direction = "INBOUND"
    
    $Country = principal.ip_geo_artifact.location.country_or_region
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(principal.ip_geo_artifact.location.region_coordinates.latitude)
      $Longitude = max(principal.ip_geo_artifact.location.region_coordinates.longitude)
    
    order:
      $Count desc  
  
Top 10 Services by Traffic Volume | 
    
    
    target.port != 0
    network.ip_protocol != "UNKNOWN_IP_PROTOCOL"
    
    $Service = strings.concat(target.port, "")
    $Protocol = network.ip_protocol
    
    match:
      $Service, $Protocol
    
    outcome:
      $Total_Bytes = sum(network.received_bytes + network.sent_bytes) / (1000*1000*1000)
    
    order:
      $Total_Bytes desc
    
    limit:
        10  
  
Top 10 Ports by Traffic - Outbound | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    network.direction = "OUTBOUND"
    
    $Port = strings.concat(target.port, "")
    
    match:
      $Port
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Distinct Source IPs | 
    
    
    $event.metadata.event_type = "NETWORK_FLOW"
    or $event.metadata.event_type = "NETWORK_CONNECTION"
    or $event.metadata.event_type = "NETWORK_FTP"
    or $event.metadata.event_type = "NETWORK_DHCP"
    or $event.metadata.event_type = "NETWORK_DNS"
    or $event.metadata.event_type = "NETWORK_HTTP"
    or $event.metadata.event_type = "NETWORK_SMTP"
    
    outcome:
      $Count = count_distinct($event.principal.ip)  
  
Traffic Volume by Log Type Over Time | 
    
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Total_Bytes = sum(network.sent_bytes + network.received_bytes) / (1000*1000*1000)
    
    order:
      $Date desc  
  
Total Bytes Sent | 
    
    
    outcome:
      $Total_Bytes_Sent_GB = math.round(sum(network.sent_bytes) / (1000*1000*1000), 2)  
  
Standard Deviation Bytes | 
    
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Stdev_Bytes = stddev(network.sent_bytes + network.received_bytes) / (1000*1000*1000)
    
    order:
      $Date desc  
  
Outbound Traffic Location Heatmap | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    network.direction = "OUTBOUND"
    
    $Country = target.ip_geo_artifact.location.country_or_region
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(target.ip_geo_artifact.location.region_coordinates.latitude)
      $Longitude = max(target.ip_geo_artifact.location.region_coordinates.longitude)
    
    order:
      $Count desc  
  
Top 10 Blocked Source Ip to Destination IP | 
    
    
    $event.metadata.event_type = "NETWORK_FLOW"
     or $event.metadata.event_type = "NETWORK_CONNECTION"
     or $event.metadata.event_type = "NETWORK_FTP"
     or $event.metadata.event_type = "NETWORK_DHCP"
     or $event.metadata.event_type = "NETWORK_DNS"
     or $event.metadata.event_type = "NETWORK_HTTP"
     or $event.metadata.event_type = "NETWORK_SMTP"
    
    $Event_Type = $event.metadata.event_type
    $Source_IP = $event.principal.ip
    $Destination_IP = $event.target.ip
    $Block = $event.security_result.action
    $Block = "BLOCK"
    
    match:
      $Event_Type, $Source_IP, $Block, $Destination_IP
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Ports by Traffic - Inbound | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    network.direction = "INBOUND"
    
    $Port = strings.concat(target.port, "")
    
    match:
      $Port
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Blocked Countries | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    security_result.action = "BLOCK"
    
    $Country = strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region)
    
    match:
      $Country
    
    outcome:
      $Count = count($Country)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Destination IP Address | 
    
    
    $event.metadata.event_type = "NETWORK_FLOW"
     or $event.metadata.event_type = "NETWORK_CONNECTION"
     or $event.metadata.event_type = "NETWORK_FTP"
     or $event.metadata.event_type = "NETWORK_DHCP"
     or $event.metadata.event_type = "NETWORK_DNS"
     or $event.metadata.event_type = "NETWORK_HTTP"
     or $event.metadata.event_type = "NETWORK_SMTP"
    
    $Event_Type = $event.metadata.event_type
    $Log_Type = $event.metadata.log_type
    $Destination_IP = $event.target.ip
    $Destination_IP != ""
    
    match:
      $Destination_IP, $Event_Type, $Log_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Network Protocol Distribution Over Time | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Protocol = network.application_protocol
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Protocol
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Suspicious Target Files | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Files = target.file.full_path
    $Files = /\.exe|\.scr|\.com|\.pif|\.dll|\.js|\.vbs|\.ps1|\.bat|\.cmd|\.wsf|\.hta|\.docm|\.xlsm|\.pptm|\.dotm|\.pdf|\.zip|\.rar|\.iso|\.img|\.lnk|\.url/ nocase
    
    match:
      $Files
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users in Vendor Alerts | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    security_result.rule_name != ""
    
    $Source_User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    
    match:
      $Source_User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 URLs | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $URL = target.url
    
    match:
      $URL
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Allowed vs. Blocked Network Traffic | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Action = security_result.action
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Action, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Hosts by Traffic Size | 
    
    
    $Hostname = principal.hostname
    
    match:
      $Hostname
    
    outcome:
      $Total_Bytes = sum(network.sent_bytes + network.received_bytes) / (1000*1000*1000)
    
    order:
      $Total_Bytes desc
    
    limit:
        10   
  
Target port by Protocol | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Port = strings.concat(target.port, "")
    $Protocol = network.application_protocol
    
    match:
      $Port, $Protocol
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Allowed Connections | 
    
    
    $event.metadata.event_type = "NETWORK_FLOW"
     or $event.metadata.event_type = "NETWORK_CONNECTION"
     or $event.metadata.event_type = "NETWORK_FTP"
     or $event.metadata.event_type = "NETWORK_DHCP"
     or $event.metadata.event_type = "NETWORK_DNS"
     or $event.metadata.event_type = "NETWORK_HTTP"
     or $event.metadata.event_type = "NETWORK_SMTP"
    
    $Event_Type = $event.metadata.event_type
    $Hostname = $event.principal.hostname
    $Asset_Type = $event.principal.asset.type
    $OS_Version = $event.target.asset.platform_software.platform_version
    $Source_IP = $event.principal.ip
    $Mac_Add = $event.principal.mac
    $Nat_IP = $event.principal.nat_ip
    $Destination_IP = $event.target.ip
    $Destination_IP != ""
    $Connection = $event.security_result.action
    $Connection = "ALLOW"
    
    match:
      $Event_Type, $Hostname, $OS_Version, $Source_IP, $Mac_Add, $Nat_IP, $Connection, $Destination_IP
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Inbound Traffic Over Time by Action | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    network.direction = "INBOUND"
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Action, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Average Bytes | 
    
    
    outcome:
      $Average_Bytes = sum(network.sent_bytes + network.received_bytes) / 2
      $Average_Bytes_GB = math.round($Average_Bytes / (1000*1000*1000), 2)
      
  
Top 10 Blocked countries | 
    
    
    $event.metadata.event_type = "NETWORK_FLOW"
     or $event.metadata.event_type = "NETWORK_CONNECTION"
     or $event.metadata.event_type = "NETWORK_FTP"
     or $event.metadata.event_type = "NETWORK_DHCP"
     or $event.metadata.event_type = "NETWORK_DNS"
     or $event.metadata.event_type = "NETWORK_HTTP"
     or $event.metadata.event_type = "NETWORK_SMTP"
    $event.security_result.action = "BLOCK"
    
    $Countries = $event.principal.location.country_or_region
    $Latitude = $event.principal.location.region_coordinates.latitude
    $Longitude = $event.principal.location.region_coordinates.longitude
    
    match:
      $Countries, $Latitude, $Longitude
    outcome:
      $Count = count_distinct($Countries)
    limit:
        10  
  
Outbound Traffic Over Time by Action | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    network.direction = "OUTBOUND"
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Action, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 events category | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    
    $Category = security_result.category
    
    match:
       $Category
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Inbound IPs by Traffic Volume | 
    
    
    network.direction = "INBOUND"
    
    $Log_Type = metadata.log_type
    $Source_IP = principal.ip
    
    match:
      $Log_Type, $Source_IP
    
    outcome:
      $Total_Bytes = sum(network.received_bytes + network.sent_bytes) / (1000*1000*1000)
    
    order:
      $Total_Bytes desc
    
    limit:
        10  
  
Top 10 Network Connections | 
    
    
    $event.metadata.event_type = "NETWORK_FLOW"
     or $event.metadata.event_type = "NETWORK_CONNECTION"
     or $event.metadata.event_type = "NETWORK_FTP"
     or $event.metadata.event_type = "NETWORK_DHCP"
     or $event.metadata.event_type = "NETWORK_DNS"
     or $event.metadata.event_type = "NETWORK_HTTP"
     or $event.metadata.event_type = "NETWORK_SMTP"
    
    $Source_Port = $event.principal.port
    $Destination_Port = $event.target.port
    $Source_IP = $event.principal.ip
    $Destination_IP = $event.target.ip
    $OS = $event.target.asset.platform_software.platform_version
    $Direction = $event.network.direction
    $Hostname = $event.principal.hostname
    $Direction != "UNKNOWN_DIRECTION"
    $OS != ""
    $Hostname != ""
    
    match:
      $Hostname, $OS, $Source_IP, $Source_Port, $Direction, $Destination_IP, $Destination_Port
    outcome:
      $Time = timestamp.get_timestamp(max($event.metadata.event_timestamp.seconds))
    order:
      $Time desc
    limit:
        10  
  
Top 10 Blocked Source IP Address | 
    
    
    $event.metadata.event_type = "NETWORK_FLOW"
     or $event.metadata.event_type = "NETWORK_CONNECTION"
     or $event.metadata.event_type = "NETWORK_FTP"
     or $event.metadata.event_type = "NETWORK_DHCP"
     or $event.metadata.event_type = "NETWORK_DNS"
     or $event.metadata.event_type = "NETWORK_HTTP"
     or $event.metadata.event_type = "NETWORK_SMTP"
    
    $Event_Type = $event.metadata.event_type
    $Source_IP = $event.principal.ip
    $Source_IP != ""
    $Destination_IP = $event.target.ip
    $Log_Type = $event.metadata.log_type
    $Block = $event.security_result.action
    $Block = "BLOCK"
    
    match:
      $Source_IP, $Block, $Destination_IP, $Log_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
## OT Security

This dashboard provides an in-depth view of security within an OT environment, allowing you to track and evaluate security events. It identifies trends, key assets, users, and services, while monitoring network and geographic activity. This enables you to prioritize threats, optimize response strategies, and enhance the security of OT systems.

Top 10 Non-OT Protocols by Log TypeTop 10 Assets Using Cleartext ProtocolTop 10 CVEsOT Sniffers Over TimeTop 10 Entities Targeted by External NetworkVendor Alerts Over Time by AssetCleartext Protocol DistributionTop 10 Vendor Alerts by UserTop 10 Entities Initiating External NetworksTop 10 Vendor Alerts by SeverityApplication Protocols Over TimeNew OT AssetsVendor Alerts Over TimeTotal New OT AssetsTop 10 Source AssetsVendor Alerts by ActionTotal OT AssetsVendor Alerts Over Time by Log TypeTop 10 Vendor Alerts by Category

Chart name | Query example  
---|---  
Top 10 Non-OT Protocols by Log Type | 
    
    
    network.application_protocol != "COAP"
    network.application_protocol != "DNP3"
    network.application_protocol != "MODBUS"
    network.application_protocol != "MQTT"
    network.application_protocol != "SNMP"
    
    $Log_Type = metadata.log_type
    $Protocol = network.application_protocol
    
    match:
      $Protocol, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Assets Using Cleartext Protocol | 
    
    
    network.application_protocol = "MODBUS"
    or network.application_protocol = "DNP3"
    or network.application_protocol = "CIP"
    or network.application_protocol = "IEC104"
    or network.application_protocol = "SNMP"
    or network.application_protocol = "COTP"
    or network.application_protocol = "GOOSE"
    or network.application_protocol = "SV"
    or network.application_protocol = "DEVICE_NET"
    or network.application_protocol = "PTP"
    or network.application_protocol = "HTTP"
    or network.application_protocol = "RLOGIN"
    or network.application_protocol = "FINGER"
    or network.application_protocol = "SMTP"
    
    $Protocol = network.application_protocol
    $Asset = strings.coalesce(target.asset.hostname, target.asset.ip, target.asset.mac, target.hostname)
    $Asset != ""
    
    match:
      $Asset, $Protocol
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 CVEs | 
    
    
    $CVE = principal.asset.vulnerabilities.cve_id
    $CVE != ""
    $Asset = principal.asset.hostname
    
    match:
      $CVE, $Asset
    
    outcome:
      $Count = count(principal.asset.vulnerabilities.cve_id)
    
    order:
      $Count desc
    
    limit:
        10  
  
OT Sniffers Over Time | 
    
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(observer.hostname)
    
    order:
      $Date desc  
  
Top 10 Entities Targeted by External Network | 
    
    
    principal.ip != /^10\..|^172\.(1[6-9]|2\d|3[0-1])\..*|^192\.168\../
    principal.ip != ""
    
    $Entity = group(target.asset.hostname, target.asset.ip, target.asset.mac, target.user.userid)
    $Entity != ""
    
    match:
      $Entity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Vendor Alerts Over Time by Asset | 
    
    
    (metadata.log_type = /CLAROTY_CTD|CLAROTY_EMC/ nocase
    and security_result.threat_id != "")
    or (metadata.log_type = /NOZOMI_GUARDIAN/ nocase
    and additional.fields["IsSecurity"] = "true")
    or (metadata.log_type = /TENABLE_OT/ nocase
    and security_result.category_details = /NetworkThreats/ nocase)
    metadata.product_event_type != "Event"
    metadata.product_event_type != "HealthCheck"
    metadata.product_event_type != "Insight"
    
    $Device = strings.coalesce(target.asset.hostname, target.asset.ip, target.asset.mac, target.hostname)
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Vendor_Alert = metadata.product_event_type
    
    match:
      $Date, $Device
    
    outcome:
      $Count = count($Vendor_Alert)
    
    order:
      $Count desc  
  
Cleartext Protocol Distribution | 
    
    
    network.application_protocol = "MODBUS"
    or network.application_protocol = "DNP3"
    or network.application_protocol = "CIP"
    or network.application_protocol = "IEC104"
    or network.application_protocol = "SNMP"
    or network.application_protocol = "COTP"
    or network.application_protocol = "GOOSE"
    or network.application_protocol = "SV"
    or network.application_protocol = "DEVICE_NET"
    or network.application_protocol = "PTP"
    or network.application_protocol = "HTTP"
    or network.application_protocol = "RLOGIN"
    or network.application_protocol = "FINGER"
    or network.application_protocol = "SMTP"
    
    $Protocol = network.application_protocol
    
    match:
      $Protocol
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Vendor Alerts by User | 
    
    
    (metadata.log_type = /CLAROTY_CTD|CLAROTY_EMC/ nocase
    and security_result.threat_id != "")
    or (metadata.log_type = /NOZOMI_GUARDIAN/ nocase
    and additional.fields["IsSecurity"] = "true")
    or (metadata.log_type = /TENABLE_OT/ nocase
    and security_result.category_details = /NetworkThreats/ nocase)
    metadata.product_event_type != "Event"
    metadata.product_event_type != "HealthCheck"
    metadata.product_event_type != "Insight"
    
    $Event = metadata.product_event_type
    $User = principal.user.user_display_name
    
    match:
      $User, $Event
    
    outcome:
      $Count = count(if((metadata.log_type = /claroty/ nocase and security_result.threat_id != "") or (metadata.log_type = /nozomi/ nocase and additional.fields["IsSecurity"] = "true") or (metadata.log_type = /TENABLE_OT/ nocase and security_result.category_details = /NetworkThreats/ nocase), 1, 0))
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Entities Initiating External Networks | 
    
    
    target.ip != /^10\..|^172\.(1[6-9]|2\d|3[0-1])\..*|^192\.168\../
    
    $Entity = group(principal.asset.hostname, principal.asset.ip, principal.asset.mac, principal.user.windows_sid, principal.user.userid)
    $Entity != ""
    
    match:
      $Entity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Vendor Alerts by Severity | 
    
    
    (metadata.log_type = /CLAROTY_CTD|CLAROTY_EMC/ nocase
    and security_result.threat_id != "")
    or (metadata.log_type = /NOZOMI_GUARDIAN/ nocase
    and additional.fields["IsSecurity"] = "true")
    or (metadata.log_type = /TENABLE_OT/ nocase
    and security_result.category_details = /NetworkThreats/ nocase)
     metadata.product_event_type != "Event"
     metadata.product_event_type != "HealthCheck"
     metadata.product_event_type != "Insight"
    
    $Vendor_Alert = metadata.product_event_type
    $Severity = security_result.severity
    
    match:
      $Severity, $Vendor_Alert
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Application Protocols Over Time | 
    
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Application_Protocol = network.application_protocol
    
    match:
      $Application_Protocol, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
New OT Assets | 
    
    
    metadata.product_event_type = /New Asset|SIGN:DHCP-OPERATION/ nocase
    
    $Hostname = strings.coalesce(target.asset.hostname, target.asset.ip, target.asset.mac, target.hostname)
    $Hostname != ""
    
    match:
      $Hostname   
  
Vendor Alerts Over Time | 
    
    
    (metadata.log_type = /CLAROTY_CTD|CLAROTY_EMC/ nocase
    and security_result.threat_id != "")
    or (metadata.log_type = /NOZOMI_GUARDIAN/ nocase
    and additional.fields["IsSecurity"] = "true")
    or (metadata.log_type = /TENABLE_OT/ nocase
    and security_result.category_details = /NetworkThreats/ nocase)
    metadata.product_event_type != "Event"
    metadata.product_event_type != "HealthCheck"
    metadata.product_event_type != "Insight"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Vendor_Alert = metadata.product_event_type
    
    match:
      $Date, $Vendor_Alert
    
    outcome:
      $Count = count(if((metadata.log_type = /claroty/ nocase and security_result.threat_id != "") or (metadata.log_type = /nozomi/ nocase and additional.fields["IsSecurity"] = "true") or (metadata.log_type = /TENABLE_OT/ nocase and security_result.category_details = /NetworkThreats/ nocase), 1, 0))
    
    order:
      $Count desc  
  
Total New OT Assets | 
    
    
    metadata.product_event_type = /New Asset|SIGN:DHCP-OPERATION/ nocase
    strings.coalesce(target.asset.hostname, target.asset.ip, target.asset.mac, target.hostname) != ""
    
    outcome:
      $Count = count_distinct(strings.coalesce(target.asset.hostname, target.asset.ip, target.asset.mac, target.hostname))  
  
Top 10 Source Assets | 
    
    
    $Hostname = strings.coalesce(principal.asset.hostname, principal.asset.ip, principal.asset.mac, principal.hostname)
    $Hostname != ""
    
    match:
      $Hostname
    
    outcome:
      $Count = count_distinct(strings.coalesce(target.asset.ip, target.ip))
    
    order:
      $Count desc
    
    limit:
        10  
  
Vendor Alerts by Action | 
    
    
    (metadata.log_type = /CLAROTY_CTD|CLAROTY_EMC/ nocase
    and security_result.threat_id != "")
    or (metadata.log_type = /NOZOMI_GUARDIAN/ nocase
    and additional.fields["IsSecurity"] = "true")
    or (metadata.log_type = /TENABLE_OT/ nocase
    and security_result.category_details = /NetworkThreats/ nocase)
     metadata.product_event_type != "Event"
     metadata.product_event_type != "HealthCheck"
     metadata.product_event_type != "Insight"
    security_result.action_details = "Succeeded"
    or security_result.action_details = "Failed"
    
    $Action = security_result.action_details
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(if((metadata.log_type = /claroty/ nocase and security_result.threat_id != "") or (metadata.log_type = /nozomi/ nocase and additional.fields["IsSecurity"] = "true") or (metadata.log_type = /TENABLE_OT/ nocase and security_result.category_details = /NetworkThreats/ nocase), 1, 0))
    
    order:
      $Date desc  
  
Total OT Assets | 
    
    
    outcome:
      $Count = count_distinct(strings.coalesce(target.asset.hostname, target.asset.ip, target.asset.mac, target.hostname))  
  
Vendor Alerts Over Time by Log Type | 
    
    
    (metadata.log_type = /CLAROTY_CTD|CLAROTY_EMC/ nocase
    and security_result.threat_id != "")
    or (metadata.log_type = /NOZOMI_GUARDIAN/ nocase
    and additional.fields["IsSecurity"] = "true")
    or (metadata.log_type = /TENABLE_OT/ nocase
    and security_result.category_details = /NetworkThreats/ nocase)
      metadata.product_event_type != "Event"
     metadata.product_event_type != "HealthCheck"
     metadata.product_event_type != "Insight"
    
    $Log_Type =  metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Vendor_Alert = metadata.product_event_type
    
    match:
      $Date, $Vendor_Alert, $Log_Type
    
    outcome:
      $Count = count(if((metadata.log_type = /claroty/ nocase and security_result.threat_id != "") or (metadata.log_type = /nozomi/ nocase and additional.fields["IsSecurity"] = "true") or (metadata.log_type = /TENABLE_OT/ nocase and security_result.category_details = /NetworkThreats/ nocase), 1, 0))
    
    order:
      $Date desc  
  
Top 10 Vendor Alerts by Category | 
    
    
    (metadata.log_type = /CLAROTY_CTD|CLAROTY_EMC/ nocase
    and security_result.threat_id != "")
    or (metadata.log_type = /NOZOMI_GUARDIAN/ nocase
    and additional.fields["IsSecurity"] = "true")
    or (metadata.log_type = /TENABLE_OT/ nocase
    and security_result.category_details = /NetworkThreats/ nocase)
     metadata.product_event_type != "Event"
     metadata.product_event_type != "HealthCheck"
     metadata.product_event_type != "Insight"
    
    $Event = metadata.product_event_type
    $Category = security_result.category_details
    
    match:
      $Category, $Event
    
    outcome:
      $Count = count(if((metadata.log_type = /claroty/ nocase and security_result.threat_id != "") or (metadata.log_type = /nozomi/ nocase and additional.fields["IsSecurity"] = "true") or (metadata.log_type = /TENABLE_OT/ nocase and security_result.category_details = /NetworkThreats/ nocase), 1, 0))
    
    order:
      $Count desc
    
    limit:
        10  
  
## PCI - Anti-Malware

This dashboard gives a view of Payment Card Industry (PCI) assets and active threat detections. It uses the reference list `pci_assets` to scope data to the PCI environment. Note: The charts in this dashboard don't load until the required reference lists are created.

Blocked Events by TypeAllowed Events By UserEvents Summary by ActionTotal EventsTotal EDR Alerts by SeverityTop 10 Event TypesTotal EDR AlertsEDR Alerts by TacticsTotal EDR Alerts Over TimeEvents by SeverityOther EventsTotal Events by Type Over TimeAllowed Events By IP AddressEvent Actions by Log TypeBlocked Events By IP AddressBlocked Events By UserQuarantined EventsTop 10 Endpoints by LocationBlocked EventsTotal Events Over TimeAllowed Events by TypeAllowed Events

Chart name | Query example  
---|---  
Blocked Events by Type | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.security_result.action = "BLOCK"
    
    $Event_Type = $event.metadata.event_type
    
    match:
      $Event_Type
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc  
  
Allowed Events By User | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.security_result.action = "ALLOW"
    
    $Event_Type = $event.metadata.event_type
    $User = strings.coalesce($event.principal.user.user_display_name, $event.principal.user.userid)
    
    match:
      $User, $Event_Type
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc
    limit:
        50  
  
Events Summary by Action | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Action = $event.security_result.action
    
    match:
      $Action
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc  
  
Total Events | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    outcome:
      $Count = count($event.security_result.action)
      
  
Total EDR Alerts by Severity | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Log_Type = $event.metadata.log_type
    $Severity = $event.security_result.severity
    $Rule_Name = strings.coalesce($event.security_result.rule_name, $event.security_result.description)
    $Rule_Name != ""
    $Description = $event.metadata.description
    
    match:
      $Rule_Name, $Description, $Log_Type, $Severity
    outcome:
      $Count = count($event.security_result.rule_name)
    order:
      $Severity desc
    limit:
        50   
  
Top 10 Event Types | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Event_Type = $event.metadata.event_type
    
    match:
      $Event_Type
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc
    limit:
        10  
  
Total EDR Alerts | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    outcome:
      $Count = count($event.security_result.rule_name)  
  
EDR Alerts by Tactics | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Log_Type = $event.metadata.log_type
    $Tactic_ID = strings.coalesce($event.security_result.attack_details.tactics.id, $event.security_result.detection_fields["Tactic ID"])
    $Tactic_ID != ""
    $Tactic_Name = strings.coalesce($event.security_result.attack_details.tactics.name, $event.security_result.detection_fields["Tactic"])
    $Tactic_Name != ""
    $Severity = $event.security_result.severity
    
    match:
      $Tactic_ID, $Tactic_Name, $Severity
    outcome:
      $Count = count($event.security_result.rule_name)
    order:
      $Severity desc
    limit:
        50  
  
Total EDR Alerts Over Time | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Log_Type = $event.metadata.log_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    outcome:
      $Count = count($event.security_result.rule_name)
    order:
      $Date asc  
  
Events by Severity | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Event_Type = $event.metadata.event_type
    $Log_Type = $event.metadata.log_type
    $Severity = $event.security_result.severity
    
    match:
      $Event_Type, $Log_Type, $Severity
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Severity desc
    limit:
        50   
  
Other Events | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    outcome:
      $Count = sum(if($event.security_result.action = "UNKNOWN_ACTION", 1, 0) + if($event.security_result.action = "FAIL", 1, 0) + if($event.security_result.action = "CHALLENGE", 1, 0))  
  
Total Events by Type Over Time | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Event_Type = $event.metadata.event_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Event_Type, $Date
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Date asc  
  
Allowed Events By IP Address | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.security_result.action = "ALLOW"
    
    $Event_Type = $event.metadata.event_type
    $IP = $event.principal.ip
    
    match:
      $IP, $Event_Type
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc
    limit:
        50  
  
Event Actions by Log Type | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Log_Type = $event.metadata.log_type
    $Action = $event.security_result.action
    
    match:
      $Action, $Log_Type
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc
    limit:
        10  
  
Blocked Events By IP Address | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.security_result.action = "BLOCK"
    
    $Event_Type = $event.metadata.event_type
    $IP = $event.principal.ip
    
    match:
      $IP, $Event_Type
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc
    limit:
        50  
  
Blocked Events By User | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.security_result.action = "BLOCK"
    
    $Event_Type = $event.metadata.event_type
    $User = strings.coalesce($event.principal.user.user_display_name, $event.principal.user.userid)
    
    match:
      $User, $Event_Type
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc
    limit:
        50  
  
Quarantined Events | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.security_result.action = "QUARANTINE"
    
    outcome:
      $Count = count($event.security_result.action)  
  
Top 10 Endpoints by Location | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Countries = $event.principal.location.country_or_region
    $Countries != ""
    $Latitude = $event.principal.location.region_coordinates.latitude
    $Longitude = $event.principal.location.region_coordinates.longitude
    $Hostname = $event.target.asset.hostname
    
    match:
      $Countries, $Latitude, $Longitude, $Hostname
    outcome:
      $Count = count($event.principal.location.country_or_region)
    limit:
        10  
  
Blocked Events | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.security_result.action = "BLOCK"
    
    outcome:
      $Count = count($event.security_result.action)  
  
Total Events Over Time | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Log_Type = $event.metadata.log_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Date asc  
  
Allowed Events by Type | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.security_result.action = "ALLOW"
    or $event.security_result.action = "ALLOW_WITH_MODIFICATION"
    
    $Event_Type = $event.metadata.event_type
    
    match:
      $Event_Type
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc  
  
Allowed Events | 
    
    
    $event.metadata.log_type = /_AV|EDR|BEYONDTRUST_ENDPOINT|BITDEFENDER|CISCO_AMP|CISCO_SECURE_WORKLOAD|CS_DETECTS|CS_IDP|CYBERARK_EPM|CYNET_360_AUTOXDR|ENDPOINT_PROTECTOR_DLP|FIREEYE_HX|HALCYON|IBM_SECURITY_VERIFY|JAMF_PRO|JAMF_PROTECT|JAMF_TELEMETRY|KOLIDE|LOOKOUT_MOBILE_ENDPOINT_SECURITY|MACOS|MACOS_ENDPOINT_SECURITY|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_ENDPOINT_IOS|MICROSOFT_DEFENDER_IDENTITY|MICROSOFT_GRAPH_ALERT|MICROSOFT_IAS|MICROSOFT_SCEP|MOBILEIRON|OPENPATH|PASSWORDSTATE|SAVIYNT_EIP|SENTINEL_DV|SENTINELONE_ALERT|SEP|SEQRITE_ENDPOINT|SOPHOS_CENTRAL|SPYCLOUD|TRENDMICRO_APEX_CENTRAL|TRENDMICRO_APEX_ONE|TRENDMICRO_DEEP_SECURITY|TRENDMICRO_STELLAR|TRENDMICRO_VISION_ONE|VENAFI_ZTPKI|WINDOWS_DEFENDER_ATP|WINEVTLOG|WINEVTLOG_XML/
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.security_result.action = "ALLOW"
    or $event.security_result.action = "ALLOW_WITH_MODIFICATION"
    
    outcome:
      $Count = count($event.security_result.action)  
  
## PCI - Data Encryption

This dashboard provides an overview of encryption practices across PCI assets. This dashboard enhances visibility into encryption key usage, offering insights into Key Management Service (KMS) activities, Azure key vault logs, and Akeyless vault logs. It uses reference list `pci_network_ranges` to scope data to the PCI environment.

**Note:** The charts in this dashboard don't load until the required reference lists are created.

Key Rotation more than 30 days agoKey Decrypt FailedKey DeletionWeak Encrypted / Unencrypted CommunicationWeak Encrypted/ Unencrypted Communication by PortKey RotatedKey EnabledKey Decrypt SuccessNew KeyWeak Encrypted / Unencrypted Communication Over TimeKey Disabled for more than 30 daysWeak Encrypted/ Unencrypted Communication Top 10 UsersTop 10 Key OperationsWeak Encrypted / Unencrypted Communication Top 10 Hosts

Chart name | Query example  
---|---  
Key Rotation more than 30 days ago | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $security_event_type = metadata.product_event_type
    ($security_event_type = "RotateKeyOnDemand" or $security_event_type = "RotateKey" or $security_event_type = "KeyRotate" or $security_event_type = /KeyRotationPolicy/ nocase or $security_event_type = "KeyRotateIfDue")
    $difference = timestamp.diff(timestamp.current_seconds(), metadata.ingested_timestamp.seconds, "DAY")
    $difference > 30
    $label = principal.user.attribute.labels.key
    $value = principal.user.attribute.labels.value
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $key = target.resource.name
    $target_key = target.resource.attribute.labels.key
    $target_key = "Recipient Account Id"
    $account_Id = target.resource.attribute.labels.value
    $date = timestamp.get_date(metadata.ingested_timestamp.seconds)
    match:
    $date, $account_Id, $user, $IP, $key, $label, $value
    outcome:
    $age = max($difference)
    order:
    $age desc  
  
Key Decrypt Failed | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $security_event_type = metadata.product_event_type
    ($security_event_type = "Decrypt" or $security_event_type = "KeyDecrypt")
    $summary = security_result.summary
    $description = metadata.description
    $result_type = additional.fields["resultType"]
    (re.regex($summary, `Fail`) nocase or re.regex($result_type, `Fail`) nocase)
    $message = strings.coalesce(security_result.summary, metadata.description)
    $key = target.resource.name
    $label = principal.user.attribute.labels.key
    $label = "principalId"
    $value = principal.user.attribute.labels.value
    $role = principal.user.role_name
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    match:
    $user, $IP, $key, $role, $message, $label, $value
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
Key Deletion | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $security_event_type = metadata.product_event_type
    ($security_event_type = "KeyDelete" or $security_event_type = "ScheduleKeyDeletion" or $security_event_type = "Delete")
    $label = principal.user.attribute.labels.key
    $user = strings.coalesce(principal.user.attribute.labels.value, principal.user.userid, principal.user.user_display_name,principal.user.email_addresses)
    $key = target.resource.name
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $user, $IP, $key, $label, $date
    outcome:
    $event_count = count(metadata.id)
    order:
    $date, $event_count desc  
  
Weak Encrypted / Unencrypted Communication | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $target_key = target.resource.attribute.labels.key
    ($target_key = "keyProperties_type" or $target_key = "requestParameters.keySpec")
    $target_value = target.resource.attribute.labels.value
    $target_value != /RSA|AES_256/ nocase
    outcome:
    $event_count = count_distinct(metadata.id)   
  
Weak Encrypted/ Unencrypted Communication by Port | 
    
    
    $IP = principal.ip
    principal.ip in cidr %PCI_Network_Ranges
    $event_type = metadata.event_type
    ($event_type >= 16000 and $event_type <= 16007)
    $port = strings.concat(target.port, "")
    $port = /(80|69|23|21|110|143|161|79|88)/
    $direction = network.direction
    match:
    $port, $direction, $event_type
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
Key Rotated | 
    
    
    principal.ip in cidr %PCI_Network_Ranges
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    $log_type = metadata.log_type
    $app = target.application
    $IP = principal.ip
    $security_event_type = metadata.product_event_type
    ($security_event_type = "RotateKeyOnDemand" or $security_event_type = "RotateKey" or $security_event_type = "KeyRotate" or $security_event_type = /KeyRotationPolicy/ nocase or $security_event_type = "KeyRotateIfDue")
    $label = principal.user.attribute.labels.key
    $value = principal.user.attribute.labels.value
    $user = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $key = target.resource.name
    match:
    $user, $IP, $key, $label, $value
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
Key Enabled | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $security_event_type = metadata.product_event_type
    ($security_event_type = "EnableKey" or $security_event_type = "KeyEnable")
    outcome:
    $event_count = count(metadata.id)   
  
Key Decrypt Success | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $security_event_type = metadata.product_event_type
    ($security_event_type = "Decrypt" or $security_event_type = "KeyDecrypt")
    $summary = security_result.summary
    $description = metadata.description
    $result_type = additional.fields["resultType"]
    (re.regex($summary, `Success`) nocase or re.regex($result_type, `Success`) nocase)
    $message = strings.coalesce(security_result.summary, metadata.description)
    $key = target.resource.name
    $label = principal.user.attribute.labels.key
    $value = principal.user.attribute.labels.value
    $role = principal.user.role_name
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    match:
    $user, $IP, $key, $role, $message, $label, $value
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    50  
  
New Key | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $security_event_type = metadata.product_event_type
    ($security_event_type = "CreateKey" or $security_event_type = "KeyCreate")
    outcome:
    $event_count = count(metadata.id)  
  
Weak Encrypted / Unencrypted Communication Over Time | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $target_key = target.resource.attribute.labels.key
    ($target_key = "keyProperties_type" or $target_key = "requestParameters.keySpec")
    $target_value = target.resource.attribute.labels.value
    $target_value != /RSA|AES_256/ nocase
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $date
    outcome:
    $event_count = count(metadata.id)
    order:
    $date asc   
  
Key Disabled for more than 30 days | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $security_event_type = metadata.product_event_type
    ($security_event_type = "DisableKey" or $security_event_type = "Disable")
    $difference = timestamp.diff(timestamp.current_seconds(), metadata.ingested_timestamp.seconds, "DAY")
    $difference > 30
    $account_id = target.resource.attribute.labels.value
    $user = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $key = target.resource.name
    match:
    $account_id, $user, $IP, $key
    outcome:
    $age = max($difference)
    order:
    $age desc  
  
Weak Encrypted/ Unencrypted Communication Top 10 Users | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $target_key = target.resource.attribute.labels.key
    ($target_key = "keyProperties_type" or $target_key = "requestParameters.keySpec")
    $target_value = target.resource.attribute.labels.value
    $target_value != /RSA|AES_256/ nocase
    $user = strings.coalesce(principal.user.attribute.labels.value, principal.user.userid, principal.user.user_display_name,principal.user.email_addresses)
    match:
    $user
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit :
    10  
  
Top 10 Key Operations | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $security_event_type = metadata.product_event_type
    match:
    $security_event_type
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
Weak Encrypted / Unencrypted Communication Top 10 Hosts | 
    
    
    $log_type = metadata.log_type
    $app = target.application
    ($log_type = /AZURE_KEYVAULT_AUDIT|AKEYLESS_VAULT/ or $app = "kms.amazonaws.com")
    principal.ip in cidr %PCI_Network_Ranges
    $IP = principal.ip
    $target_key = target.resource.attribute.labels.key
    ($target_key = "keyProperties_type" or $target_key = "requestParameters.keySpec")
    $target_value = target.resource.attribute.labels.value
    $target_value != /RSA|AES_256/
    $hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $hostname != ""
    match:
    $hostname
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10   
  
## PCI - EDR Alerts Overview

This dashboard offers a detailed view of critical elements such as assets, events, and active threat detections. It uses the reference list `pci_assets` to scope data to the PCI environment.

**Note:** The charts in this dashboard don't load until the required reference lists are created.

Number of EDR SensorsTop 10 TechniquesSeverity based on EDR AlertsTotal EDR Alerts Over TimeTop 10 Users based on EDR AlertsTop 10 TacticsTop 10 EDR AlertsTop 10 Hosts based on EDR AlertsActive EDR SensorsTotal EDR Alerts

Chart name | Query example  
---|---  
Number of EDR Sensors | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    outcome:
      $Count = count_distinct($event.principal.asset.hostname)  
  
Top 10 Techniques | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Technique_ID = strings.coalesce($event.security_result.attack_details.techniques.id, $event.security_result.detection_fields["Technique ID"])
    $Technique_Name  = strings.coalesce($event.security_result.attack_details.techniques.name, $event.security_result.detection_fields["Technique"])
    $Technique_ID != ""
    $Technique_Name  != ""
    
    match:
      $Technique_Name
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        107  
  
Severity based on EDR Alerts | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.security_result.summary != ""
    
    $Severity = $event.security_result.severity
    
    match:
      $Severity
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Severity asc
    limit:
        10  
  
Total EDR Alerts Over Time | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Log_Type = $event.metadata.log_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Date asc  
  
Top 10 Users based on EDR Alerts | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $User = $event.principal.user.user_display_name
    $User != ""
    
    match:
      $User
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Tactics | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Tactic_ID = strings.coalesce($event.security_result.attack_details.tactics.id, $event.security_result.detection_fields["Tactic ID"])
    $Tactic_Name = strings.coalesce($event.security_result.attack_details.tactics.name, $event.security_result.detection_fields["Tactic"])
    $Tactic_ID != ""
    $Tactic_Name != ""
    
    match:
      $Tactic_Name
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Top 10 EDR Alerts | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Log_Type = $event.metadata.log_type
    $Detection = $event.security_result.summary
    $Detection != ""
    
    match:
      $Detection, $Log_Type
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Hosts based on EDR Alerts | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $Hostname = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    $Hostname != ""
    
    match:
      $Hostname
    outcome:
      $Count = count($event.security_result.summary)
    order:
      $Count desc
    limit:
        10  
  
Active EDR Sensors | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    $EDR_Asset = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    
    match:
      $EDR_Asset
    limit:
        50  
  
Total EDR Alerts | 
    
    
    $event.metadata.log_type = /EDR|CS_DETECTS|FIREEYE_HX|MICROSOFT_DEFENDER_ENDPOINT|MICROSOFT_DEFENDER_IDENTITY|SENTINEL_DV/ nocase
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    
    outcome:
      $Count = count($event.security_result.summary)  
  
## PCI - Identity and Access

This dashboard provides a detailed, real-time overview of access management and identity-related activities to support PCI-DSS compliance. It consolidates key metrics and insights, including user access permissions, password changes, and authentication events. It uses the reference list `pci_assets` to scope data to the PCI environment.

**Note:** The charts in this dashboard don't load until the required reference lists are created.

Accounts with password never expiresUser Accounts Change PermissionsUser Accounts CreatedUser Accounts DeletedPassword Changes Attempts by Top 10 UserPassword Changes over time

Chart name | Query example  
---|---  
Accounts with password never expires | 
    
    
    $event_type = metadata.event_type
    $event_type  >= 15000 and $event_type  <= 15014
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $hostname = strings.coalesce(principal.hostname,principal.asset.hostname,target.hostname,target.asset.hostname)
    $vendor = metadata.vendor_name
    $security_event_type = metadata.product_event_type
    $key = principal.user.attribute.labels.key
    $value = principal.user.attribute.labels.value
    ($key = /Password Never Expires/ nocase and $value = /true/ nocase)
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $action = security_result.action
    match:
    $user, $hostname, $vendor, $action, $security_event_type
    outcome:
    $event_count = count_distinct(metadata.id)
    order:
    $event_count desc  
  
User Accounts Change Permissions | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_CHANGE_PERMISSIONS"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $hostname = strings.coalesce(principal.hostname,principal.asset.hostname,target.hostname,target.asset.hostname)
    $vendor = metadata.vendor_name
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $action = security_result.action
    match:
    $user, $hostname, $vendor, $action
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
User Accounts Created | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_CREATION"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    outcome:
    $event_count = count(metadata.id)  
  
User Accounts Created | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_CREATION"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $hostname = strings.coalesce(principal.hostname,principal.asset.hostname,target.hostname,target.asset.hostname)
    $vendor = metadata.vendor_name
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $action = security_result.action
    match:
    $user, $hostname, $vendor, $action
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
User Accounts Deleted | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_DELETION"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $hostname = strings.coalesce(principal.hostname,principal.asset.hostname,target.hostname,target.asset.hostname)
    $vendor = metadata.vendor_name
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $action = security_result.action
    match:
    $user, $hostname, $vendor, $action
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
Password Changes Attempts by Top 10 User | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_CHANGE_PASSWORD"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $hostname = strings.coalesce(principal.hostname,principal.asset.hostname,target.hostname,target.asset.hostname)
    $vendor = metadata.vendor_name
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $action = security_result.action
    match:
    $user, $hostname, $vendor, $action
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
User Accounts Deleted | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_DELETION"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    outcome:
    $event_count = count(metadata.id)  
  
User Accounts Change Permissions | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_CHANGE_PERMISSIONS"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    outcome:
    $event_count = count(metadata.id)  
  
Password Changes over time | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_CHANGE_PASSWORD"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $hostname = strings.coalesce(principal.hostname,principal.asset.hostname,target.hostname,target.asset.hostname)
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $date
    outcome:
    $event_count = count(metadata.id)
    order:
    $date asc  
  
## PCI - Monitoring and Testing

This dashboard provides monitoring and tracking of access to payment cardholder data within the PCI environment. It utilizes the reference lists `pci_assets` and `default_users` to scope data.

**Note:** The charts in this dashboard don't load until the required reference lists are created.

Events Over Time by Event TypeTop Resource Access by SourceAudit Logs AccessAdministrative Access to SystemsTop 10 Users by ActionInactive Users (Last 7 days)Log Clear Detection (Windows Events)Audit Policy ChangesFailed EventsTotal Failed Events by Source IP AddressTotal Events by Event Type

Chart name | Query example  
---|---  
Events Over Time by Event Type | 
    
    
    (metadata.event_type = "USER_UNCATEGORIZED"
    or metadata.event_type = "USER_LOGIN"
    or metadata.event_type = "USER_LOGOUT"
    or metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_RESOURCE_CREATION"
    or metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    or metadata.event_type = "USER_COMMUNICATION"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_RESOURCE_DELETION")
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    
    $Event_Type = metadata.event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top Resource Access by Source | 
    
    
    (metadata.event_type = "USER_UNCATEGORIZED"
    or metadata.event_type = "USER_LOGIN"
    or metadata.event_type = "USER_LOGOUT"
    or metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_RESOURCE_CREATION"
    or metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    or metadata.event_type = "USER_COMMUNICATION"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_RESOURCE_DELETION")
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    $Vendor = metadata.vendor_name
    $Action = security_result.action
    $Source_User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Destination_User = strings.coalesce(target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    match:
      $Source_IP, $Hostname, $Source_User, $Destination_User, $Vendor, $Action
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc
      
  
Audit Logs Access | 
    
    
    (metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" or metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE")
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    
    $Vendor = metadata.vendor_name
    $Source_User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Destination_User = strings.coalesce(target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    match:
      $Source_User, $Destination_User, $Vendor
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds ), "%F %T")
    
    order:
      $Count desc  
  
Administrative Access to Systems | 
    
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    
    $Event_Type = metadata.event_type
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    $Vendor = metadata.vendor_name
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $User in %Default_Users
    
    match:
      $User, $Hostname, $Vendor, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds ), "%F %T")
    
    order:
      $Count desc  
  
Top 10 Users by Action | 
    
    
    (metadata.event_type = "USER_UNCATEGORIZED"
    or metadata.event_type = "USER_LOGIN"
    or metadata.event_type = "USER_LOGOUT"
    or metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_RESOURCE_CREATION"
    or metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    or metadata.event_type = "USER_COMMUNICATION"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_RESOURCE_DELETION")
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Action = security_result.action
    
    match:
      $User, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Inactive Users (Last 7 days) | 
    
    
    (metadata.event_type = "USER_UNCATEGORIZED"
    or metadata.event_type = "USER_LOGIN"
    or metadata.event_type = "USER_LOGOUT"
    or metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_RESOURCE_CREATION"
    or metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    or metadata.event_type = "USER_COMMUNICATION"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_RESOURCE_DELETION")
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    principal.user.last_login_time.seconds > 0
    
    $Event_Type = metadata.event_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Time_Difference = cast.as_int((metadata.event_timestamp.seconds-principal.user.last_login_time.seconds)/86400)
    
    match:
      $User, $Time_Difference
    
    outcome:
      $Logtime = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Lastime = timestamp.get_timestamp(max(principal.user.last_login_time.seconds), "%F %T")
    
    order:
      $Time_Difference desc
         
  
Log Clear Detection (Windows Events) | 
    
    
    metadata.log_type = "WINEVTLOG"
    (metadata.product_event_type = "1102" or metadata.product_event_type = "104" or metadata.event_type = "SYSTEM_AUDIT_LOG_WIPE")
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    
    $Event_Type = metadata.event_type
    $Security_Event_Type = metadata.product_event_type
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname,target.hostname,target.asset.hostname)
    $Summary = strings.coalesce(metadata.description, security_result.summary, security_result.description)
    
    match:
      $Hostname, $Event_Type, $Security_Event_Type, $Summary
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds ), "%F %T")
    
    order:
      $Count desc  
  
Audit Policy Changes | 
    
    
    metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" or metadata.event_type = "STATUS_UPDATE"
    (security_result.category_details = /AuditPolicyChanges/ nocase or strings.coalesce(metadata.description, security_result.description, security_result.summary, metadata.product_event_type) = /policy change/ nocase)
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    
    $Security_Event_Type = metadata.product_event_type
    $Policy_Change = strings.coalesce(metadata.description, security_result.description, security_result.summary, security_result.category_details)
    $Source_User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Destination_User = strings.coalesce(target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    match:
      $Source_User, $Destination_User, $Security_Event_Type, $Policy_Change
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds ), "%F %T")
    
    order:
      $Count desc  
  
Audit Policy Changes | 
    
    
    (metadata.event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" or metadata.event_type = "STATUS_UPDATE")
    (security_result.category_details = /AuditPolicyChanges/ nocase or strings.coalesce(metadata.description, security_result.description, security_result.summary, metadata.product_event_type) = /policy change/ nocase)
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    
    outcome:
      $Count = count(metadata.id)  
  
Failed Events | 
    
    
    (metadata.event_type = "USER_UNCATEGORIZED"
    or metadata.event_type = "USER_LOGIN"
    or metadata.event_type = "USER_LOGOUT"
    or metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_RESOURCE_CREATION"
    or metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    or metadata.event_type = "USER_COMMUNICATION"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_RESOURCE_DELETION")
    security_result.action = "BLOCK"
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    
    outcome:
      $Count = count(metadata.id)  
  
Total Failed Events by Source IP Address | 
    
    
    (metadata.event_type = "USER_UNCATEGORIZED"
    or metadata.event_type = "USER_LOGIN"
    or metadata.event_type = "USER_LOGOUT"
    or metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_RESOURCE_CREATION"
    or metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    or metadata.event_type = "USER_COMMUNICATION"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_RESOURCE_DELETION")
    security_result.action = "BLOCK"
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    $Vendor = metadata.vendor_name
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Source_User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Destination_User = strings.coalesce(target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    match:
      $Source_IP, $Source_User, $Destination_User, $Hostname, $Vendor, metadata.event_type
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds ), "%F %T")
    
    order:
      $Count desc  
  
Total Events by Event Type | 
    
    
    (metadata.event_type = "USER_UNCATEGORIZED"
    or metadata.event_type = "USER_LOGIN"
    or metadata.event_type = "USER_LOGOUT"
    or metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_RESOURCE_CREATION"
    or metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    or metadata.event_type = "USER_COMMUNICATION"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_RESOURCE_DELETION")
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    
    $Event_Type = metadata.event_type
    $Vendor = metadata.vendor_name
    $Action = security_result.action
    
    match:
      $Event_Type, $Vendor, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
## PCI - Network

This dashboard provides insights to network performance of a particular interface (source or destination), real-time visibility to top network activities, and traffic trends and analysis. It uses the reference list `pci_network_ranges` to scope data to the PCI environment.

**Note:** The charts in this dashboard don't load until the required reference lists are created.

Traffic Total CountTop 10 Destination Traffic by LocationTraffic by Top 10 DestinationsTop 10 Triggered Network RulesTraffic by Top 10 Destination PortsTop 10 Network ActivitiesPort Activity SummaryTraffic by Top 10 ProtocolsNetwork Data Processed Over Time (Sent Bytes)Network Data Processed Over Time (Received Bytes)Network Traffic Over TimeTraffic by Top 10 Source PortsNetwork Asset CountTraffic Over Time by ProtocolTraffic Over Time by ActionTraffic by Top 10 Sources

Chart name | Query example  
---|---  
Traffic Total Count | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    outcome:
      $Count = count($event.network.direction)  
  
Top 10 Destination Traffic by Location | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    $event.target.ip != ""
    
    $Countries = $event.target.location.country_or_region
    $Latitude = $event.target.location.region_coordinates.latitude
    $Longitude = $event.target.location.region_coordinates.longitude
    $Countries != ""
    
    match:
      $Countries, $Latitude, $Longitude
    outcome:
      $Count = count($event.target.ip)
    limit:
        10  
  
Traffic by Top 10 Destinations | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $IP_Address = $event.target.ip
    
    match:
      $IP_Address
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Triggered Network Rules | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $event.metadata.event_type = "NETWORK_UNCATEGORIZED"
    or $event.metadata.event_type = "NETWORK_FLOW"
    or $event.metadata.event_type = "NETWORK_CONNECTION"
    or $event.metadata.event_type = "NETWORK_FTP"
    or $event.metadata.event_type = "NETWORK_DHCP"
    or $event.metadata.event_type = "NETWORK_DNS"
    or $event.metadata.event_type = "NETWORK_HTTP"
    or $event.metadata.event_type = "NETWORK_SMTP"
    or $event.metadata.event_type = "SCAN_NETWORK"
    
    $Log_Type = $event.metadata.log_type
    $Event_Type = $event.metadata.event_type
    $Product_Network_Event = $event.security_result.rule_name
    $Direction = $event.network.direction
    $Product_Network_Event != ""
    
    match:
      $Event_Type, $Log_Type, $Direction, $Product_Network_Event
    outcome:
      $Count = count_distinct($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Traffic by Top 10 Destination Ports | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $Ports = strings.concat($event.target.port, " ")
    
    match:
      $Ports
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Network Activities | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $Log_Type = $event.metadata.log_type
    $Event_Type = $event.metadata.event_type
    $Security_Action = $event.security_result.action
    
    match:
      $Event_Type, $Log_Type, $Security_Action
    outcome:
      $Count = count($event.metadata.event_type)
    order:
      $Count desc
    limit:
        10  
  
Port Activity Summary | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $Source_Port = $event.principal.port
    $Target_Port = $event.target.port
    $Direction = $event.network.direction
    $Event_Type = $event.metadata.event_type
    
    match:
      $Source_Port, $Direction, $Target_Port, $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        50  
  
Traffic by Top 10 Protocols | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $Log_Type = $event.metadata.log_type
    $Protocol = $event.network.ip_protocol
    $Direction = $event.network.direction
    
    match:
      $Protocol, $Direction
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Network Data Processed Over Time (Sent Bytes) | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $Log_Type = $event.metadata.log_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    outcome:
      $Total_Bytes = sum($event.network.sent_bytes)
      $GB = math.ceil($Total_Bytes / 1073741824)
    order:
      $Date asc
    limit:
        50  
  
Network Data Processed Over Time (Received Bytes) | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $Log_Type = $event.metadata.log_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    outcome:
      $Total_Bytes = sum($event.network.received_bytes)
      $GB = math.ceil($Total_Bytes / 1073741824)
    order:
      $Date asc
    limit:
        50  
  
Network Traffic Over Time | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $Direction = $event.network.direction
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Direction
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Traffic by Top 10 Source Ports | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $Ports = strings.concat($event.principal.port, " ")
    
    match:
      $Ports
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Network Asset Count | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $Network_Asset = strings.coalesce($event.principal.ip, $event.principal.asset.ip)
    
    outcome:
      $Count = count_distinct(strings.coalesce($event.principal.ip, $event.principal.asset.ip))  
  
Traffic Over Time by Protocol | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $Protocol = $event.network.ip_protocol
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Protocol
    outcome:
      $Count = count_distinct($event.metadata.id)
    order:
      $Date asc  
  
Traffic Over Time by Action | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    $Security_Result = $event.security_result.action
    
    match:
      $Date, $Security_Result
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Date asc  
  
Traffic by Top 10 Sources | 
    
    
    $event.metadata.log_type = /ROUTER|SWITCH|DHCP|PROXY|NETWORK|VPN|FIREWALL|_FLOW|VPC|WIRELESS|IPS|IDS|ARUBA_EDGECONNECT_SDWAN|ARUBA_SWITCH|CISCO_APIC|CISCO_CALL_MANAGER|CISCO_DNAC|CISCO_ESTREAMER|CISCO_IOS|CISCO_PRIME|EFFICIENTIP_DDI|EXTREME_SWITCH|FORTINET_FORTIDDOS|FORTINET_FORTIMANAGER|ARUBA_CENTRAL|JUNIPER_JUNOS|JUNIPER_MIST|JUNIPER_SDWAN|NAGIOS|ARBOR_EDGE_DEFENSE|MICROSOFT_NPS|STEELHEAD|SHRUBBERY_TACACS|TRENDMICRO_DDI|VMWARE_NSX|WINDOWS_NET_POLICY_SERVER|ZYWALL|IMPERVA_FLEXPROTECT|PAN_IOT|NOZOMI_GUARDIAN|SURICATA_EVE|UMBRELLA_DNS|WINDOWS_SYSMON|COHESITY|RUBRIK|CISCO_MERAKI|CLAROTY_EMC|CLAROTY_CTD|HONEYD|AIRWATCH|IMPERVA_SECURESPHERE|SECURELINK|WALLIX_BASTION|CHECKPOINT_HARMONY|UNIFI_AP|DIGI_MODEMS|DESYNOVA_CONTIDO|CLOUDGENIX_SDWAN|JUNIPER_MX|SAP_WEBDISP|ADVA_FSP|HP_PROCURVE|VYOS|RSA_SECURID|HCNET_ACCOUNT_ADAPTER|INFOBLOX|VITALQIP|ASSET_STATIC_IP|BLUECAT_DDI|TWINGATE|SYMANTEC_VIP_AUTHHUB|ZSCALER_DECEPTION|BROCADE_SERVERIRON|KEMP_LOADBALANCER|A10_LOAD_BALANCER|AWS_ELB|F5_BIGIP_LTM|RADWARE_ALTEON|CITRIX_NETSCALER|AKAMAI_CLOUD_MONITOR|CISCO_ACE|GCP_LOADBALANCING|KERIOCONTROL|EXTRAHOP|NETFILTER_IPTABLES|CISCO_UMBRELLA_AUDIT|F5_AFM|NUTANIX_PRISM|SANGFOR_NGAF|VERCEL_WAF|PEPLINK_FW|NETDOCUMENTS|PAN_PANORAMA|PFSENSE|AZION|FIREEYE_PX|OPNSENSE|CISCO_FWSM|FORTINET_FORTIWEB|BARRACUDA_WAF|SYMANTEC_WSS|MENLO_SECURITY|DIGITALARTS_IFILTER|WEBMARSHAL|UMBRELLA_IP|AWS_SECURITY_HUB|EXTRAHOP|GUARDDUTY|MICROSOFT_ATA|ORCA|OSSEC|SURICATA_EVE|VMWARE_TANZU/ nocase
    $event.principal.ip in cidr %PCI_Network_Ranges
    or $event.principal.asset.ip in cidr %PCI_Network_Ranges
    
    $IP_Address = $event.principal.ip
    
    match:
      $IP_Address
    outcome:
      $Count = count_distinct($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
## PCI - Patch Management

This dashboard provides a comprehensive view of the patch management lifecycle, enabling organizations to monitor and manage their system updates effectively. It uses the reference lists `patch_updates` and `pci_assets` to scope data to the PCI environment.

**Note:** The charts in this dashboard don't load until the required reference lists are created.

Top 10 Successful Installations by HostsFailed Installations Over TimeSystems with Available UpdatesCancelled installations Over TimeFailed Downloads Over TimeSuccessful Downloads Over TimeStarted Downloads Over TimeLatest Updates InstalledSuccessful Installations over TimeTop 10 Failed Installations by Hosts

Chart name | Query example  
---|---  
Top 10 Successful Installations by Hosts | 
    
    
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.metadata.product_event_type = "19"
    
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    $Hostname = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    
    match:
      $Date, $Hostname
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date desc
    limit:
        10  
  
Failed Installations Over Time | 
    
    
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.metadata.product_event_type = "20"
    
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    $Event = $event.metadata.product_event_type
    
    match:
      $Event, $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Systems with Available Updates | 
    
    
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.metadata.product_event_type = "40"
    
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    $Hostname = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    
    match:
      $Hostname, $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc
    limit:
        10  
  
Cancelled installations Over Time | 
    
    
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.metadata.product_event_type = "21"
    
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    $Hostname = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    
    match:
      $Hostname, $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Failed Downloads Over Time | 
    
    
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.metadata.product_event_type = "31"
    
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    $Hostname = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    
    match:
      $Hostname, $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Successful Downloads Over Time | 
    
    
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.metadata.product_event_type = "16"
    
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    $Hostname = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    
    match:
      $Hostname, $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Started Downloads Over Time | 
    
    
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.metadata.product_event_type = "41"
    
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    $Hostname = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    
    match:
      $Hostname, $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Latest Updates Installed | 
    
    
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.metadata.description in regex %Patch_Updates
    $event.metadata.product_event_type = "19"
    
    $Hostname = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    $Hostname != ""
    $Update = $event.metadata.description
    
    match:
      $Hostname, $Update
    limit:
        50  
  
Successful Installations over Time | 
    
    
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.metadata.product_event_type = "19"
    
    $Event = $event.metadata.product_event_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Event, $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Top 10 Failed Installations by Hosts | 
    
    
    strings.coalesce($event.principal.asset.hostname, $event.principal.hostname) in %PCI_Assets
    $event.metadata.product_event_type = "20"
    
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    $Hostname = strings.coalesce($event.principal.asset.hostname, $event.principal.hostname)
    
    match:
      $Date, $Hostname
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date desc
    limit:
        10  
  
## PCI - Secure Configurations

This dashboard provides real-time monitoring of secure configuration practices. It tracks key metrics, highlights risks, and helps maintain critical configurations. It uses the reference lists `pci_assets` and `default_users` to scope data to the PCI environment.

**Note:** The charts in this dashboard don't load until the required reference lists are created.

Failed Login AttemptsTotal Policy ChangesDefault Account Usage Over TimeTop 10 Default UsernamesFailed Login Attempts Over TimePolicy Changes by UserFailed Login Attempts by top 10 HostFailed Login Attempts by UserDefault Account Usage by HostnameTotal Default Username AuthenticationPolicy Changes by Log SourcesPolicy Changes Over TimeDefault Usernames Authentication Summary

Chart name | Query example  
---|---  
Failed Login Attempts | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $action = security_result.action
    $action = "BLOCK"
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
Total Policy Changes | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" or $event_type = "STATUS_UPDATE")
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $policy_change = strings.coalesce(security_result.description,metadata.product_event_type,security_result.about.registry.registry_key)
    $policy_change = /policy change/ nocase
    outcome:
    $event_count = count(metadata.id)  
  
Default Account Usage Over Time | 
    
    
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $user in %Default_Users
    match:
    $date, $user
    outcome:
    $event_count = count(metadata.id)
    order:
    $date asc  
  
Top 10 Default Usernames | 
    
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $user in %Default_Users
    $event_type = metadata.event_type
    match:
    $user
    outcome:
    $event_types = array_distinct(metadata.event_type)
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
Failed Login Attempts Over Time | 
    
    
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $action = security_result.action
    $action = "BLOCK"
    match:
    $date,$action
    outcome:
    $event_count = count(metadata.id)
    order:
    $date asc  
  
Policy Changes by User | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" or $event_type = "STATUS_UPDATE")
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $policy_change = strings.coalesce(security_result.description,metadata.product_event_type,security_result.about.registry.registry_key)
    $policy_change = /policy change/ nocase
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    match:
    $user
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
Failed Login Attempts by top 10 Host | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $hostname = strings.coalesce(principal.hostname,principal.asset.hostname,target.hostname,target.asset.hostname)
    $hostname != ""
    $action = security_result.action
    $action = "BLOCK"
    match:
    $hostname
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
Failed Login Attempts by User | 
    
    
    $vendor = metadata.vendor_name
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $hostname = strings.coalesce(principal.hostname,principal.asset.hostname,target.hostname,target.asset.hostname)
    $action = security_result.action
    $action = "BLOCK"
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $user != ""
    match:
    $user, $hostname, $vendor
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
Default Account Usage by Hostname | 
    
    
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $hostname = strings.coalesce(principal.hostname, principal.asset.hostname,target.hostname,target.asset.hostname)
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $user in %Default_Users
    match:
    $hostname
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
Total Default Username Authentication | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $user in %Default_Users
    outcome:
    $event_count = count(metadata.id)  
  
Policy Changes by Log Sources | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" or $event_type = "STATUS_UPDATE")
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $policy_change = strings.coalesce(security_result.description,metadata.product_event_type,security_result.about.registry.registry_key)
    $policy_change = /policy change/ nocase
    $log_source = metadata.log_type
    match:
    $log_source
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
Policy Changes Over Time | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SYSTEM_AUDIT_LOG_UNCATEGORIZED" or $event_type = "STATUS_UPDATE")
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $policy_change = strings.coalesce(security_result.description,metadata.product_event_type,security_result.about.registry.registry_key)
    $policy_change = /policy change/ nocase
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $date, $policy_change
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
Default Usernames Authentication Summary | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $log_type = metadata.log_type
    (principal.hostname in %PCI_Assets or principal.asset.hostname in %PCI_Assets or target.hostname in %PCI_Assets or target.asset.hostname in %PCI_Assets)
    $hostname = strings.coalesce(principal.hostname, principal.asset.hostname,target.hostname,target.asset.hostname)
    $action = security_result.action
    $user = strings.coalesce(principal.user.userid,principal.user.user_display_name,principal.user.email_addresses)
    $user  in %Default_Users
    match:
    $user, $hostname, $log_type, $action
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
## PCI - Vulnerability Management

This dashboard provides real-time monitoring and tracking of vulnerabilities. It supports broader compliance efforts, helping to identify, assess, and manage risks to maintain secure payment environments while streamlining reporting. It uses the reference lists `pci_assets` and `pci_network_ranges` to scope data to the PCI environment.

**Note:** The charts in this dashboard don't load until the required reference lists are created.

Vulnerabilities by AgeTop 10 Vulnerable HostsTop 10 VulnerabilitiesNew VulnerabilitiesTotal VulnerabilitiesVulnerable SystemsVulnerabilities by SeverityVulnerable Systems (Percentage)Vulnerability Per System

Chart name | Query example  
---|---  
Vulnerabilities by Age | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SCAN_VULN_HOST" or $event_type = "SCAN_VULN_NETWORK")
    (principal.hostname in %PCI_Assets) or (principal.asset.hostname in %PCI_Assets) or (principal.ip in cidr %PCI_Network_Ranges) or (principal.asset.ip in cidr %PCI_Network_Ranges)
    $vulnerability = extensions.vulns.vulnerabilities.description
    $First_Found = timestamp.get_date(extensions.vulns.vulnerabilities.first_found.seconds)
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Time_difference = timestamp.diff(metadata.event_timestamp.seconds, extensions.vulns.vulnerabilities.first_found.seconds, "DAY")
    match:
    $Time_difference,$vulnerability
    outcome:
    $Range = if(max($Time_difference) <= 30, "0-30Days", if(max($Time_difference) <= 60, "31-60Days", if(max($Time_difference) <= 90, "61-90Days", ">90Days")))
    $event_count = count(metadata.id)
    order:
    $Time_difference desc  
  
Top 10 Vulnerable Hosts | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SCAN_VULN_HOST" or $event_type = "SCAN_VULN_NETWORK")
    $asset = strings.coalesce(principal.hostname,principal.asset.hostname,principal.ip,principal.asset.ip)
    (principal.hostname in %PCI_Assets) or (principal.asset.hostname in %PCI_Assets) or (principal.ip in cidr %PCI_Network_Ranges) or (principal.asset.ip in cidr %PCI_Network_Ranges)
    $platform = principal.platform
    match:
    $asset, $platform
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
Top 10 Vulnerabilities | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SCAN_VULN_HOST" or $event_type = "SCAN_VULN_NETWORK")
    (principal.hostname in %PCI_Assets) or (principal.asset.hostname in %PCI_Assets) or (principal.ip in cidr %PCI_Network_Ranges) or (principal.asset.ip in cidr %PCI_Network_Ranges)
    $vulnerability = extensions.vulns.vulnerabilities.description
    $platform = principal.platform
    match:
    $vulnerability,$platform
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
New Vulnerabilities | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SCAN_VULN_HOST" or $event_type = "SCAN_VULN_NETWORK")
    (principal.hostname in %PCI_Assets) or (principal.asset.hostname in %PCI_Assets) or (principal.ip in cidr %PCI_Network_Ranges) or (principal.asset.ip in cidr %PCI_Network_Ranges)
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    $First_Found = timestamp.get_date(extensions.vulns.vulnerabilities.first_found.seconds)
    $vulnerability = extensions.vulns.vulnerabilities.description
    $severity = extensions.vulns.vulnerabilities.severity
    $Time_difference = timestamp.diff(metadata.event_timestamp.seconds, extensions.vulns.vulnerabilities.first_found.seconds, "DAY")
    $Time_difference < 30
    match:
    $vulnerability, $severity
    outcome:
    $event_count = count(metadata.id)
    $age = max($Time_difference)
    order:
    $severity desc  
  
Total Vulnerabilities | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SCAN_VULN_HOST" or $event_type = "SCAN_VULN_NETWORK")
    (principal.hostname in %PCI_Assets) or (principal.asset.hostname in %PCI_Assets) or (principal.ip in cidr %PCI_Network_Ranges) or (principal.asset.ip in cidr %PCI_Network_Ranges)
    outcome:
    $event_count = count(metadata.id)  
  
Vulnerable Systems | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SCAN_VULN_HOST" or $event_type = "SCAN_VULN_NETWORK")
    (principal.hostname in %PCI_Assets) or (principal.asset.hostname in %PCI_Assets) or (principal.ip in cidr %PCI_Network_Ranges) or (principal.asset.ip in cidr %PCI_Network_Ranges)
    $asset = strings.coalesce(principal.hostname,principal.asset.hostname,principal.ip,principal.asset.ip)
    outcome:
    $event_count = count_distinct($asset)  
  
Vulnerabilities by Severity | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SCAN_VULN_HOST" or $event_type = "SCAN_VULN_NETWORK")
    (principal.hostname in %PCI_Assets) or (principal.asset.hostname in %PCI_Assets) or (principal.ip in cidr %PCI_Network_Ranges) or (principal.asset.ip in cidr %PCI_Network_Ranges)
    $severity = extensions.vulns.vulnerabilities.severity
    match:
    $severity
    outcome:
    $event_count = count(metadata.id)
    order:
    $severity desc  
  
Vulnerable Systems (Percentage) | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SCAN_VULN_HOST" or $event_type = "SCAN_VULN_NETWORK")
    (principal.hostname in %PCI_Assets) or (principal.asset.hostname in %PCI_Assets) or (principal.ip in cidr %PCI_Network_Ranges) or (principal.asset.ip in cidr %PCI_Network_Ranges)
    $platform = principal.platform
    match:
    $platform
    outcome:
    $event_count = count($platform)  
  
Vulnerability Per System | 
    
    
    $event_type = metadata.event_type
    ($event_type = "SCAN_VULN_HOST" or $event_type = "SCAN_VULN_NETWORK")
    $asset = strings.coalesce(principal.hostname,principal.asset.hostname,principal.ip,principal.asset.ip)
    (principal.hostname in %PCI_Assets) or (principal.asset.hostname in %PCI_Assets) or (principal.ip in cidr %PCI_Network_Ranges) or (principal.asset.ip in cidr %PCI_Network_Ranges)
    $platform = principal.platform
    match:
    $asset
    outcome:
    $operating_system = array_distinct($platform)
    $event_count = count(metadata.id)
    order:
    $event_count desc  
  
## Password Change Monitoring Dashboard

This dashboard tracks and logs password changes and provides a comprehensive view of password change events, including date and time of password change. It visualizes trends, identifies risks such as suspicious IP addresses, users, and locations, and helps detect and respond to potential security incidents such as unauthorized password changes.

Top 10 Source IPs by UserTop 10 Password ResetEvents Over Time by Log TypeEvents By ActionSource Geolocation HeatmapTop 10 Users by actionTop 10 Event DescriptionRecent User Change Password (24 hours)Events By Severity

Chart name | Query example  
---|---  
Top 10 Source IPs by User | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    
    $Source_IP =  strings.coalesce(principal.ip, principal.asset.ip)
    $Source_IP != ""
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses,target.user.userid,target.user.user_display_name,target.user.email_addresses )
    
    match :
      $Source_IP,$User
    
    outcome :
      $Count = count(metadata.id)
    
    order :
      $Count desc
    
     limit:10
    
      
  
Top 10 Password Reset | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    
    $Log_Type = metadata.log_type
    $Password_Event_Type = metadata.product_event_type
    $Description = metadata.description
    ($Password_Event_Type = /Reset/ nocase OR $Description = /Reset/ nocase)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses,target.user.userid,target.user.user_display_name,target.user.email_addresses )
    
    match :
       $User
    
    outcome :
      $Count = count(metadata.id)
    
    order :
      $Count desc
    
    limit: 10  
  
Events Over Time by Log Type | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    
    $Log_Type = metadata.log_type
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match :
      $Date,$Log_Type
    
    outcome :
      $Count = count(metadata.id)
    
      
  
Events By Action | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    
    $Action =  security_result.action
    
    match :
      $Action
    
    outcome :
      $Count = count(metadata.id)
    
      
  
Source Geolocation Heatmap | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    
    $Country = principal.ip_geo_artifact.location.country_or_region
    
    match :
      $Country
    
    outcome :
      $Count = count(metadata.id)
      $Latitude = max(principal.ip_geo_artifact.location.region_coordinates.latitude)
      $Longitude = max(principal.ip_geo_artifact.location.region_coordinates.longitude)
    
    order :
      $Count desc  
  
Top 10 Users by action | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses,target.user.userid,target.user.user_display_name,target.user.email_addresses )
    $Action =  security_result.action
    
    match :
      $User,$Action
    
    outcome :
      $Count = count(metadata.id)
    
    order :
      $Count desc
    
    limit :
        10  
  
Top 10 Event Description | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    
    $Description = strings.coalesce(metadata.description,security_result.description,metadata.product_event_type)
    
    match :
      $Description
    
    outcome :
    
      $Count = count(metadata.id)
    
    order :
      $Count desc
    
    limit :
        10
    
      
  
Recent User Change Password (24 hours) | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    
    $Log_Type = metadata.log_type
    $Password_Event_Type = metadata.product_event_type
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses,target.user.userid,target.user.user_display_name,target.user.email_addresses )
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname)
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    
    match :
      $User,$Hostname,$Source_IP,$Password_Event_Type,$Log_Type
    
    outcome :
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds ), "%F %T")
      $Count = count(metadata.id)
    
    order :
      $Count desc
    
      
  
Events By Severity | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    
    $Severity =  security_result.severity
    
    match :
      $Severity
    
    outcome :
      $Count = count(metadata.id)
    
      
  
## Phishing Monitoring

This dashboard provides insights into phishing threats, email security, and attack trends. It offers visibility to the security team into phishing attempts, allowing teams to monitor malicious email activity, identify suspicious senders and targeted users, and flag potentially harmful indicators.

**Note:** Apply filters based on specific log types to display relevant results on the dashboard.

Top 10 Users in Vendor AlertsTop 10 Phishing URLs AccessedTop 10 Phishing Email SubjectsEvents by ActionEvents Over Time by Log TypeTotal Phishing Events DetectedTop 10 Associated DomainsVendor Alerts Over Time by ActionRecent Phishing EventsTop 10 Vendor AlertsTop 10 Threat NamesEvents Over Time by ActionTop 10 Phishing Email SendersPhishing File DetailsEvents by File typeVendor Alerts Over Time by Log TypeTop 10 Phishing URLsTop 10 Phishing Email RecipientsSource Geolocation OverviewEvents by Severity

Chart name | Query example  
---|---  
Top 10 Users in Vendor Alerts | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`)nocase)
    security_result.threat_name != "NOT_PHISHING"
    security_result.rule_name != ""
    
    $User = strings.coalesce(network.email.from, principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Phishing URLs Accessed | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name!= "NOT_PHISHING"
    metadata.product_event_type = /permit/ nocase
    
    $URL = strings.coalesce (target.url, principal.process.file.embedded_urls, security_result.about.url, network.http.referral_url, principal.url)
    $URL != ""
    $User = strings.coalesce(network.email.from, principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Action = security_result.action
    
    match:
      $URL, $Action
    
    outcome:
      $User_List = array_distinct($User)
      $Count = count($URL)
    
    order:
      $URL desc
    
    //limit:
    //10  
  
Top 10 Phishing Email Subjects | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name!= "NOT_PHISHING"
    
    $Subject = network.email.subject
    $Action = security_result.action
    
    match:
      $Subject, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Events by Action | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name != "NOT_PHISHING"
    
    $Action = security_result.action
    
    match:
      $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Action desc
      
  
Events Over Time by Log Type | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`)nocase)
    security_result.threat_name!= "NOT_PHISHING"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Total Phishing Events Detected | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name != "NOT_PHISHING"
    
    outcome:
      $Count = count(metadata.id)
      
  
Top 10 Associated Domains | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name!= "NOT_PHISHING"
    
    $Domain = strings.coalesce(principal.administrative_domain, target.administrative_domain, about.administrative_domain)
    $Action = security_result.action
    
    match:
      $Domain, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Vendor Alerts Over Time by Action | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`)nocase)
    security_result.threat_name != "NOT_PHISHING"
    security_result.rule_name != ""
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Action = security_result.action
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Recent Phishing Events | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`)nocase)
    security_result.threat_name!= "NOT_PHISHING"
    
    $Security_Event_Type = metadata.product_event_type
    $Summary = strings.coalesce(security_result.summary, metadata.description, security_result.description)
    $Sender = strings.coalesce(network.email.from, principal.user.email_addresses)
    $Subject = network.email.subject
    
    match:
      $Security_Event_Type, $Summary, $Subject, $Sender
    
    outcome:
      $Count = count(metadata.id)
      $Receiver_Count = count_distinct(strings.coalesce(network.email.to, network.email.reply_to, target.user.email_addresses))
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
Top 10 Vendor Alerts | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`)nocase)
    security_result.threat_name != "NOT_PHISHING"
    security_result.rule_name != ""
    
    $Rule_Name = security_result.rule_name
    
    match:
      $Rule_Name
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Threat Names | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name!= "NOT_PHISHING"
    
    $Threat_Name = strings.coalesce(security_result.threat_name,security_result.category_details)
    $Log_Type = metadata.log_type
    
    match:
      $Threat_Name, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Events Over Time by Action | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name != "NOT_PHISHING"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Action = security_result.action
    
    match:
      $Date, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Action asc  
  
Top 10 Phishing Email Senders | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name != "NOT_PHISHING"
    
    $Sender = strings.coalesce(network.email.from,principal.user.email_addresses)
    $Action = security_result.action
    
    match:
      $Sender, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Phishing File Details | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name!= "NOT_PHISHING"
    strings.coalesce(target.file.full_path, about.file.full_path, target.file.names) != ""
    
    $File_Path = strings.coalesce(target.file.full_path, about.file.full_path, target.file.names)
    $File_Type = strings.coalesce(about.file.mime_type, target.file.mime_type)
    $Action = security_result.action
    $Receiver = strings.coalesce(network.email.to, network.email.reply_to,target.user.email_addresses)
    $Sender = strings.coalesce(network.email.from,principal.user.email_addresses)
    $File_Hash = strings.coalesce(about.file.md5, about.file.sha256, security_result.about.file.sha256)
    
    match:
      $File_Path, $File_Type, $File_Hash, $Sender, $Receiver, $Action
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Count desc  
  
Events by File type | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name!= "NOT_PHISHING"
    
    $File_Type = strings.coalesce(about.file.mime_type, target.file.mime_type)
    
    match:
      $File_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $File_Type desc  
  
Vendor Alerts Over Time by Log Type | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`)nocase)
    security_result.threat_name != "NOT_PHISHING"
    security_result.rule_name != ""
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Phishing URLs | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name!= "NOT_PHISHING"
    
    $URL = strings.coalesce(target.url, security_result.about.url, network.http.referral_url, principal.process.file.embedded_urls, principal.url)
    $URL != ""
    
    match:
      $URL
    
    outcome:
      $Threat_Names = array_distinct(strings.coalesce(security_result.threat_name,security_result.category_details))
      $Categories = array_distinct(security_result.category)
      $Count = count($URL)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Phishing Email Recipients | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name!= "NOT_PHISHING"
    
    $Receiver = strings.coalesce(network.email.to, network.email.reply_to, target.user.email_addresses)
    $Action = security_result.action
    
    match:
      $Receiver, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Source Geolocation Overview | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name != "NOT_PHISHING"
    
    $Country = principal.ip_geo_artifact.location.country_or_region
    $Country != ""
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(principal.ip_geo_artifact.location.region_coordinates.latitude)
      $Longitude = max(principal.ip_geo_artifact.location.region_coordinates.longitude)
    
    order:
      $Count desc
      
  
Events by Severity | 
    
    
    (security_result.category = "MAIL_PHISHING" or re.regex(security_result.threat_name,`Phish`) nocase or re.regex(security_result.category_details,`Phish`) nocase)
    security_result.threat_name != "NOT_PHISHING"
    
    $Severity = security_result.severity
    
    match:
      $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Severity desc
      
  
## Port Scanning Detection

This dashboard provides insights into port scanning activities and other related network reconnaissance techniques that may indicate potential threats or malicious activity within the network infrastructure. By tracking and visualizing this type of behavior, it enables you to detect, investigate, and mitigate any unauthorized or suspicious network access attempts.

Events Over Time by Log TypeRecent Failed Connection Attempts to Standard PortsSeverity DistributionPort Scan Events Over Time by UserTop 10 Destination IPsRecent Port Scan EventsTop 10 Source CountriesTop 10 Targeted Internal SubnetsRecent Failed Connection Attempts to Non-Standard PortsTop 10 Targeted PortsTop 10 Port Scan SourcesTop 10 Source IPsPort/IP RatioProtocol DistributionPort Scan Events Over Time by Hostname

Chart name | Query example  
---|---  
Events Over Time by Log Type | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Log_Type = metadata.log_type
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc   
  
Recent Failed Connection Attempts to Standard Ports | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    security_result.action = "BLOCK"
    target.port > 19
    target.port < 1025
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Principal_IP = principal.ip
    $Target_IP = target.ip
    $Protocol = network.ip_protocol
    $Port = target.port
    
    match:
      $Date, $Principal_IP, $Protocol, $Port, $Target_IP
    
    order:
      $Date desc  
  
Severity Distribution | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    
    $Severity = security_result.severity
    
    match:
      $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Port Scan Events Over Time by User | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $User = group(principal.user.userid, principal.user.email_addresses, target.user.userid, target.user.email_addresses)
    
    match:
      $Date, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc   
  
Top 10 Destination IPs | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    
    $IP_Address = target.ip
    $Log_Type = metadata.log_type
    
    match:
      $IP_Address, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Port Scan Events | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    principal.ip != ""
    target.ip != ""
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Description = strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description)
    $Source_IP = principal.ip
    $Target_IP = target.ip
    
    match:
      $Date, $Source_IP, $Description, $Target_IP
    
    outcome:
      $Port = array_distinct(target.port)
    
    order:
      $Date desc   
  
Top 10 Source Countries | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    
    $Country = principal.location.country_or_region
    $Country != ""
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Targeted Internal Subnets | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    net.ip_in_range_cidr(target.ip, "10.0.0.0/8")
    or net.ip_in_range_cidr(target.ip, "172.16.0.0/12")
    or net.ip_in_range_cidr(target.ip, "192.168.0.0/16")
    or net.ip_in_range_cidr(target.ip, "fc00::/7")
    
    $IP_Range = if(net.ip_in_range_cidr(target.ip, "192.168.0.0/16"), strings.concat(re.capture(target.ip, /^\d+\.\d+\.\d+\./), "0/16"),
                if(net.ip_in_range_cidr(target.ip, "172.16.0.0/12"), strings.concat(re.capture(target.ip, /^\d+\.\d+\./), "0.0/12"),
                if(net.ip_in_range_cidr(target.ip, "10.0.0.0/8"), strings.concat(re.capture(target.ip, /^\d+\./), "0.0.0/8"),
                if(net.ip_in_range_cidr(target.ip, "fc00::/7"), strings.concat(re.capture(target.ip, /^(?:[0-9A-Fa-f]{1,4}:){3}[0-9A-Fa-f]{1,4}/), "/64"), "Unknown IP address range"))))
    
    match:
      $IP_Range
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Failed Connection Attempts to Non-Standard Ports | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    security_result.action = "BLOCK"
    target.port < 19
    or target.port > 1025
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Principal_IP = principal.ip
    $Target_IP = target.ip
    $Protocol = network.ip_protocol
    $Port = target.port
    
    match:
      $Date, $Principal_IP, $Protocol, $Port, $Target_IP
    
    order:
      $Date desc  
  
Top 10 Targeted Ports | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    
    $Port = strings.concat(target.port, " ")
    $Log_Type = metadata.log_type
    
    match:
      $Port, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Port Scan Sources | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    
    $Country = principal.location.country_or_region
    $Latitude = principal.location.region_coordinates.latitude
    $Latitude != 0
    $Longitude = principal.location.region_coordinates.longitude
    $Longitude != 0
    
    match:
      $Country, $Latitude, $Longitude
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc   
  
Top 10 Source IPs | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    
    $IP_Address = principal.ip
    $Log_Type = metadata.log_type
    
    match:
      $IP_Address, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Port/IP Ratio | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    
    $Port = target.port
    $Source_IP = principal.ip
    
    outcome:
      $Ratio = math.round(count_distinct(target.port) / count_distinct(principal.ip), 2)  
  
Protocol Distribution | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    
    $Protocol = network.ip_protocol
    
    match:
      $Protocol
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Port Scan Events Over Time by Hostname | 
    
    
    metadata.event_type = "SCAN_NETWORK"
    or strings.coalesce(security_result.threat_name, security_result.rule_name, security_result.description, security_result.summary, metadata.product_event_type, metadata.description) = /port(?:\s|\_)?scan(?:ning|ner)?/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Hostname = group(principal.hostname, target.hostname)
    
    match:
      $Date, $Hostname
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc   
  
## Port and Protocol Overview

This dashboard offers real-time and historical insights into network port activity and protocol usage. It identifies active and inactive ports, potential vulnerabilities, and helps optimize network security and performance while ensuring policy compliance.

New Port Activity - InboundAllowed vs Blocked Ports TrafficTop 10 Ports by Traffic - OutboundProtocol DistributionTraffic on Commonly Prohibited PortsTop 10 Ports by Traffic - Inbound

Chart name | Query example  
---|---  
New Port Activity - Inbound | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $Direction = network.direction
    $Direction = "INBOUND"
    $policy = security_result.rule_name
    $port = strings.concat(target.port, "")
    $port != /(40202|40203|40462|41611|41612|41620|41629|41674|41684|41685|41694|41703|41712|41721|41730|41747|43448|44924|44925|45071|52818|53025|54736|443|57903|58254|62977|80|88)/
    $source_ip = principal.ip
    $location = principal.ip_geo_artifact.location.country_or_region
    $action = security_result.action
    $action != "BLOCK"
    match:
      $port, $action
    outcome:
      $Source_IP = array_distinct($source_ip)
      $event_count = count(metadata.id)
    
    order:
      $event_count desc
      
  
Allowed vs Blocked Ports Traffic | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $action = security_result.action
    $action != "UNKNOWN_ACTION"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
      $action, $Date
    outcome:
      $Event_Count = count(metadata.id)
    order:
      $Date asc  
  
Top 10 Ports by Traffic - Outbound | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $Logtype = metadata.log_type
    $Direction = network.direction
    $Direction = "OUTBOUND"
    $Port = target.port
    match:
      $Port
    outcome:
      $event_count = count(metadata.id)
      $logtype = array_distinct($Logtype)
    order:
      $event_count desc
    limit:
        10  
  
Protocol Distribution | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $Protocol = network.ip_protocol
    $Protocol != "UNKNOWN_IP_PROTOCOL"
    match:
      $Protocol
    outcome:
      $Event_Count = count(metadata.id)
      
  
Protocol Distribution | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $Protocol = network.ip_protocol
    $Protocol != "UNKNOWN_IP_PROTOCOL"
    match:
      $Protocol
    outcome:
      $Event_Count = count(metadata.id)
      
  
Traffic on Commonly Prohibited Ports | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $policy = security_result.rule_name
    $port = strings.concat(target.port, "")
    $port != /(443|53|8080|8081|34622|34756|35406|35466|35546|36602|37276|38976|41394|41672|41926|45432|46354|47416|48678|51664|51824|52086|52818|54052|54958|55276|55890|57488|57666|58546|58914|59388|60388|61000|64450|64482|64498|64598|64674|64707|64735|64739|64740|64795|64828|64880|64905|64945|64962|65004|65019|65050|65094|65114|65169|65202|65223|65264|65287|65323|65346|65378|65392|65456|8728|3389|6379|5555|2222|5060|3128|8888|27017|8088|1080)/
    match:
      $port
    outcome:
      $event_count = count(metadata.id)
    order:
      $event_count desc
    limit:
        20  
  
Top 10 Ports by Traffic - Inbound | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $Direction = network.direction
    $Direction = "INBOUND"
    $Port = target.port
    $Logtype = metadata.log_type
    match:
      $Port
    outcome:
      $event_count = count(metadata.id)
      $logtype = array_distinct($Logtype)
    order:
      $event_count desc
    limit:
        10  
  
Traffic on Commonly Prohibited Ports | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $policy = security_result.rule_name
    $port = strings.concat(target.port, "")
    $port != /(443|53|8080|8081|34622|34756|35406|35466|35546|36602|37276|38976|41394|41672|41926|45432|46354|47416|48678|51664|51824|52086|52818|54052|54958|55276|55890|57488|57666|58546|58914|59388|60388|61000|64450|64482|64498|64598|64674|64707|64735|64739|64740|64795|64828|64880|64905|64945|64962|65004|65019|65050|65094|65114|65169|65202|65223|65264|65287|65323|65346|65378|65392|65456|8728|3389|6379|5555|2222|5060|3128|8888|27017|8088|1080)/
    match:
      $port
    outcome:
      $event_count = count(metadata.id)
    order:
      $event_count desc
    limit:
        20  
  
Top 10 Ports by Traffic - Outbound | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $Logtype = metadata.log_type
    $Direction = network.direction
    $Direction = "OUTBOUND"
    $Port = target.port
    match:
      $Port
    outcome:
      $event_count = count(metadata.id)
      $logtype = array_distinct($Logtype)
    order:
      $event_count desc
    limit:
        10  
  
Allowed vs Blocked Ports Traffic | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $action = security_result.action
    $action != "UNKNOWN_ACTION"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
      $action, $Date
    outcome:
      $Event_Count = count(metadata.id)
    order:
      $Date asc  
  
Top 10 Ports by Traffic - Inbound | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $Direction = network.direction
    $Direction = "INBOUND"
    $Port = target.port
    $Logtype = metadata.log_type
    match:
      $Port
    outcome:
      $event_count = count(metadata.id)
      $logtype = array_distinct($Logtype)
    order:
      $event_count desc
    limit:
        10  
  
New Port Activity - Inbound | 
    
    
    $event_type = metadata.event_type
    $event_type >= 16000 and $event_type <= 16007
    $Direction = network.direction
    $Direction = "INBOUND"
    $policy = security_result.rule_name
    $port = strings.concat(target.port, "")
    $port != /(40202|40203|40462|41611|41612|41620|41629|41674|41684|41685|41694|41703|41712|41721|41730|41747|43448|44924|44925|45071|52818|53025|54736|443|57903|58254|62977|80|88)/
    $source_ip = principal.ip
    $location = principal.ip_geo_artifact.location.country_or_region
    $action = security_result.action
    $action != "BLOCK"
    match:
      $port, $action
    outcome:
      $Source_IP = array_distinct($source_ip)
      $event_count = count(metadata.id)
    
    order:
      $event_count desc
      
  
## PowerShell

This dashboard is designed to analyze and monitor Powershell activity within your organization. It provides insights into command execution, user interactions, and potential security risks. By aggregating and visualizing this data, the dashboard aids in identifying potential issues, tracking threats, and enhancing overall security.

Powershell Execution by Process Event TypeLeast Common File PathsLeast Common HostsLeast Common Command LinesTop 10 UsersPowerShell Events by Security Result ActionLeast Common UsersPowerShell Outbound Network ConnectionsPowershell Activity SummaryTop 10 Command LinesPowerShell Events by SeverityChar Variable ObfuscationTop 10 HostsFile Downloads via PowerShellTop 10 Event Types Containing PowerShellTop 10 File Paths

Chart name | Query example  
---|---  
Powershell Execution by Process Event Type | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Event_Type = $event.metadata.event_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Event_Type, $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Least Common File Paths | 
    
    
    $event.principal.process.file.full_path = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Full_Path = group($event.principal.process.file.full_path, $event.target.process.file.full_path)
    $Full_Path != ""
    
    match:
      $Full_Path
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count asc
    limit:
        100  
  
Least Common Hosts | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Hostname = $event.principal.hostname
    
    match:
      $Hostname
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count asc
    limit:
        100
    
      
  
Least Common Command Lines | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    match:
      $Command_Line
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count asc
    limit:
        10  
  
Least Common Command Lines | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    match:
      $Command_Line
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count asc
    limit:
        10  
  
Top 10 Users | 
    
    
    $event.principal.user.userid != /\$$/
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $User = $event.principal.user.userid
    $User != ""
    
    match:
      $User
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10
    
      
  
PowerShell Events by Security Result Action | 
    
    
    $Powershell = group($event.principal.process.command_line, $event.target.process.command_line)
    $Powershell = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Action = $event.security_result.action
    
    match:
      $Action
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc   
  
PowerShell Events by Security Result Action | 
    
    
    $Powershell = group($event.principal.process.command_line, $event.target.process.command_line)
    $Powershell = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Action = $event.security_result.action
    
    match:
      $Action
    outcome:
      $Count = count($event.security_result.action)
    order:
      $Count desc   
  
Least Common Users | 
    
    
    $event.principal.user.userid != /\$$/
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $User = $event.principal.user.userid
    
    match:
      $User
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count asc
    limit:
        100
    
      
  
PowerShell Outbound Network Connections | 
    
    
    $event.metadata.event_type = "NETWORK_CONNECTION"
    $event.network.direction = "OUTBOUND"
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Destination_IP = $event.target.ip
    $Source_IP = $event.principal.ip
    $Direction = $event.network.direction
    
    match:
      $Source_IP, $Direction, $Destination_IP, $Command_Line
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        50  
  
PowerShell Outbound Network Connections | 
    
    
    $event.metadata.event_type = "NETWORK_CONNECTION"
    $event.network.direction = "OUTBOUND"
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Destination_IP = $event.target.ip
    $Source_IP = $event.principal.ip
    $Direction = $event.network.direction
    
    match:
      $Source_IP, $Direction, $Destination_IP, $Command_Line
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        50  
  
Powershell Activity Summary | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Event_Type = $event.metadata.event_type
    $Log_Type = $event.metadata.log_type
    $Direction = $event.network.direction
    
    match:
      $Event_Type, $Log_Type, $Direction, $Command_Line
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        50
    
      
  
Top 10 Command Lines | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    match:
      $Command_Line
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
PowerShell Events by Severity | 
    
    
    $Powershell = group($event.principal.process.command_line, $event.target.process.command_line)
    $Powershell = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Severity = $event.security_result.severity
    
    match:
      $Severity
    outcome:
      $Count = count($event.security_result.severity)
    order:
      $Count desc  
  
Powershell Execution by Process Event Type | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Event_Type = $event.metadata.event_type
    
    match:
      $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc  
  
Char Variable Obfuscation | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:powershell(?:\.exe)?).*\[char(?:\]|\[)/ nocase
    or $Command_Line = /(?:powershell(?:\.exe)?).*(?:iex|invoke-expression)/ nocase
    or $Command_Line = /(?:powershell(?:\.exe)?).*(?:tochararray)/ nocase
    
    $Registry_Value = $event.target.registry.registry_value_data
    
    match:
      $Command_Line, $Registry_Value
    outcome:
      $Count = count($event.metadata.id)
    limit:
        50  
  
Top 10 Hosts | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Hostname = $event.principal.hostname
    $Hostname != ""
    
    match:
      $Hostname
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Users | 
    
    
    $event.principal.user.userid != /\$$/
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $User = $event.principal.user.userid
    
    match:
      $User
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10
    
      
  
File Downloads via PowerShell | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:powershell(?:\.exe)?).*?(?:Invoke\-(?:WebRequest|RestMethod)|Start\-BitsTransfer)/ nocase
    or $Command_Line = /(?:powershell(?:\.exe)?).*?(?:system\.net\.(?:http\.httpclient|webclient).*?(?:downloadfile|writeallbytes))/ nocase
    
    match:
      $Command_Line
    outcome:
      $Count = count($event.metadata.id)
    limit:
        50  
  
Top 10 Event Types Containing PowerShell | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Event_Type = $event.metadata.event_type
    
    match:
      $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Powershell Activity Summary | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Event_Type = $event.metadata.event_type
    $Log_Type = $event.metadata.log_type
    $Direction = $event.network.direction
    
    match:
      $Event_Type, $Log_Type, $Direction, $Command_Line
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        50
    
      
  
Top 10 Command Lines | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    match:
      $Command_Line
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Least Common Users | 
    
    
    $event.principal.user.userid != /\$$/
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $User = $event.principal.user.userid
    
    match:
      $User
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count asc
    limit:
        100
    
      
  
Top 10 Hosts | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Hostname = $event.principal.hostname
    
    match:
      $Hostname
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Event Types Containing PowerShell | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Event_Type = $event.metadata.event_type
    
    match:
      $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Least Common File Paths | 
    
    
    $event.principal.process.file.full_path = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Full_Path = group($event.principal.process.file.full_path, $event.target.process.file.full_path)
    $Full_Path != ""
    
    match:
      $Full_Path
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count asc
    limit:
        100  
  
Powershell Execution by Process Event Type | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Event_Type = $event.metadata.event_type
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Event_Type, $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 File Paths | 
    
    
    $event.principal.process.file.full_path = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Full_Path = group($event.principal.process.file.full_path, $event.target.process.file.full_path)
    $Full_Path != ""
    
    match:
      $Full_Path
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Char Variable Obfuscation | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:powershell(?:\.exe)?).*\[char(?:\]|\[)/ nocase
    or $Command_Line = /(?:powershell(?:\.exe)?).*(?:iex|invoke-expression)/ nocase
    or $Command_Line = /(?:powershell(?:\.exe)?).*(?:tochararray)/ nocase
    
    $Registry_Value = $event.target.registry.registry_value_data
    
    match:
      $Command_Line, $Registry_Value
    outcome:
      $Count = count($event.metadata.id)
    limit:
        50  
  
File Downloads via PowerShell | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:powershell(?:\.exe)?).*?(?:Invoke\-(?:WebRequest|RestMethod)|Start\-BitsTransfer)/ nocase
    or $Command_Line = /(?:powershell(?:\.exe)?).*?(?:system\.net\.(?:http\.httpclient|webclient).*?(?:downloadfile|writeallbytes))/ nocase
    
    match:
      $Command_Line
    outcome:
      $Count = count($event.metadata.id)
    limit:
        50  
  
Powershell Execution by Process Event Type | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Event_Type = $event.metadata.event_type
    
    match:
      $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc  
  
PowerShell Events by Severity | 
    
    
    $Powershell = group($event.principal.process.command_line, $event.target.process.command_line)
    $Powershell = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Severity = $event.security_result.severity
    
    match:
      $Severity
    outcome:
      $Count = count($event.security_result.severity)
    order:
      $Count desc  
  
Top 10 File Paths | 
    
    
    $event.principal.process.file.full_path = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Full_Path = group($event.principal.process.file.full_path, $event.target.process.file.full_path)
    $Full_Path != ""
    
    match:
      $Full_Path
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Least Common Hosts | 
    
    
    $Command_Line = group($event.principal.process.command_line, $event.target.process.command_line)
    $Command_Line = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    $Hostname = $event.principal.hostname
    
    match:
      $Hostname
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count asc
    limit:
        100
    
      
  
## Privileged Access Management

This dashboard tracks privileged access activities, identifying sources like users, hostnames, and IP addresses, while highlighting key assets. It helps security teams monitor access trends and manage risks, ensuring only authorized individuals access sensitive systems and data.

**Note:** Apply filters to display relevant results on the dashboard.

Top 10 AdministratorsTop 10 AssetsEvents Over TimeTop 10 User AccountsEvent Types DistributionTop 10 Targeted HostnamesTop 10 Source IPsTop 10 Source Usernames

Chart name | Query example  
---|---  
Top 10 Administrators | 
    
    
    principal.user.attribute.roles.type = "ADMINISTRATOR"
    
    $Admin = principal.user.userid
    
    match:
      $Admin
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 Assets | 
    
    
    $Asset = target.asset.hostname
    $Asset != ""
    
    match:
      $Asset
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Events Over Time | 
    
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 User Accounts | 
    
    
    $Account = target.user.userid
    $Account != ""
    
    match:
      $Account
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Event Types Distribution | 
    
    
    $Event_Type = metadata.event_type
    
    match:
      $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        50  
  
Top 10 Targeted Hostnames | 
    
    
    $Hostname = target.hostname
    $Hostname != ""
    
    match:
      $Hostname
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 Source IPs | 
    
    
    $Source_IP = principal.ip
    $Source_IP != ""
    
    match:
      $Source_IP
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 Source Usernames | 
    
    
    $Username = principal.user.userid
    $Username != ""
    
    match:
      $Username
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
## Process Event Summary

This dashboard gives you a comprehensive view of network activity by collecting and visualizing data on various process occurrences, hosts, users, and events. It highlights key metrics, charts, and anomalies to provide essential insights into event frequency and process performance. It is useful for proactively monitoring system health, detecting potential security threats through anomalous behavior, and identifying areas needing efficiency improvements.

Total Powershell EventsTop 10 Parent ProcessesTop 10 UsersTotal Command Shell EventsTotal Distinct UsersTotal Blocked EventsTop 10 Powershell EventsTop 10 HashesProcess EventsTop 10 Shell Commands by UserProcess Events Over TimeTop 10 HostnamesProcess Termination Events Over TimeTotal Process EventsTop 10 HostsTotal Distinct HostsTotal Distinct HostnamesEvent Type DistributionRecent Process EventsTop 10 Command Shell Events

Chart name | Query example  
---|---  
Total Powershell Events | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Powershell = group($event.principal.process.command_line, $event.target.process.command_line)
    $Powershell = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    outcome:
      $Count = count($Powershell)  
  
Top 10 Parent Processes | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Event_Type = metadata.event_type
    $Parent_Process = re.capture(principal.process.file.full_path, `\w+.exe$`)
    $Parent_Process != ""
    
    match:
      $Parent_Process, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Event_Type = $event.metadata.event_type
    $User = strings.concat($event.principal.user.userid, " ")
    
    match:
      $User, $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Total Command Shell Events | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Command_Shell = principal.process.command_line
    $Command_Shell = /(?:cmd|shell)\.exe/ nocase or $Command_Shell = /\/(bash|sh|zsh)/ nocase
    
    outcome:
      $Count = count($Command_Shell)  
  
Total Distinct Users | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    outcome:
      $Count = count_distinct($event.principal.user.userid)  
  
Total Blocked Events | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $event.security_result.action = "BLOCK"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Total Powershell Events | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Powershell = group(principal.process.command_line, target.process.command_line)
    $Powershell = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    outcome:
      $Count = count($Powershell)  
  
Top 10 Powershell Events | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Powershell = group($event.principal.process.command_line, $event.target.process.command_line)
    $Powershell = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    
    match:
      $Powershell
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Hashes | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Event_Type = metadata.event_type
    $Hash = group(principal.process.file.md5, principal.process.file.sha1, principal.process.file.sha256, target.process.file.md5, target.process.file.sha1, target.process.file.sha256)
    $Hash != ""
    
    match:
      $Hash, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Process Events | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Hostname = $event.principal.hostname
    $User = $event.principal.user.userid
    $Parent_Process = $event.principal.process.file.full_path
    $Parent_Command_Line = $event.principal.process.command_line
    $Target_Process =  $event.target.process.file.full_path
    $Target_Command_Line = $event.target.process.command_line
    
    match:
      $Hostname, $User, $Parent_Process, $Parent_Command_Line, $Target_Process, $Target_Command_Line
    outcome:
      $Time = timestamp.get_timestamp(max($event.metadata.event_timestamp.seconds))
    order:
      $Time desc
    limit:
        50  
  
Top 10 Shell Commands by User | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Shell = principal.process.command_line
    $Shell = /(?:pwsh|powershell(?:_ise)?)\.exe/ nocase
    or $Shell = /(?:cmd|shell)\.exe/ nocase
    or $Shell = /\/(bash|sh|zsh)/ nocase
    $User = principal.user.userid
    
    match:
      $Shell, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Process Events Over Time | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Hostnames | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Event_Type = metadata.event_type
    $Hostname = principal.hostname
    
    match:
      $Hostname, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Event_Type = metadata.event_type
    $User = strings.concat(principal.user.userid, " ")
    
    match:
      $User, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Process Termination Events Over Time | 
    
    
    metadata.event_type = "PROCESS_TERMINATION"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Total Blocked Events | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    security_result.action = "BLOCK"
    
    outcome:
      $Count = count(metadata.id)  
  
Total Distinct Users | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    outcome:
      $Count = count_distinct(principal.user.userid)  
  
Total Process Events | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Hosts | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Event_Type = $event.metadata.event_type
    $Hostname = $event.principal.hostname
    
    match:
      $Hostname, $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Total Process Events | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Total Distinct Hosts | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    outcome:
      $Count = count_distinct($event.principal.hostname)  
  
Total Distinct Hostnames | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    outcome:
      $Count = count_distinct(principal.hostname)  
  
Total Command Shell Events | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Command_Shell = $event.principal.process.command_line
    $Command_Shell = /(?:cmd|shell)\.exe/ nocase or $Command_Shell = /\/(bash|sh|zsh)/ nocase
    
    outcome:
      $Count = count($Command_Shell)  
  
Event Type Distribution | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Event_Type = metadata.event_type
    
    match:
      $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Recent Process Events | 
    
    
    metadata.event_type = "PROCESS_UNCATEGORIZED"
    or metadata.event_type = "PROCESS_LAUNCH"
    or metadata.event_type = "PROCESS_INJECTION"
    or metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or metadata.event_type = "PROCESS_TERMINATION"
    or metadata.event_type = "PROCESS_OPEN"
    or metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Hostname = principal.hostname
    $User = principal.user.userid
    $Parent_Process = principal.process.file.full_path
    $Parent_Command_Line = principal.process.command_line
    $Target_Process =  target.process.file.full_path
    $Target_Command_Line = target.process.command_line
    
    match:
      $Hostname, $User, $Parent_Process, $Parent_Command_Line, $Target_Process, $Target_Command_Line
    
    outcome:
      $Time = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Time desc
      
  
Top 10 Command Shell Events | 
    
    
    $event.metadata.event_type = "PROCESS_UNCATEGORIZED"
    or $event.metadata.event_type = "PROCESS_LAUNCH"
    or $event.metadata.event_type = "PROCESS_INJECTION"
    or $event.metadata.event_type = "PROCESS_PRIVILEGE_ESCALATION"
    or $event.metadata.event_type = "PROCESS_TERMINATION"
    or $event.metadata.event_type = "PROCESS_OPEN"
    or $event.metadata.event_type = "PROCESS_MODULE_LOAD"
    
    $Command_Shell = $event.principal.process.command_line
    $Command_Shell = /(?:cmd|shell)\.exe/ nocase or $Command_Shell = /\/(bash|sh|zsh)/ nocase
    
    match:
      $Command_Shell
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
## Ransomware Spotlight Monitoring

This dashboard provides a comprehensive view of ransomware-related activity detected by various security tools and data sources. It helps security teams quickly identify and respond to ransomware threats by highlighting the recent events, affected devices, and sources of detection.

Recent Ransomware Email Events by URLs/AttachmentsRecent Ransomware VM EventsRecent Ransomware DLP EventsRecent Endpoint Ransomware EventsTop 10 Ransomware Log SourcesRansomware Events Over Time by ProductRecent Ransomware NDR EventsRecent Ransomware Events by Hostname

Chart name | Query example  
---|---  
Recent Ransomware Email Events by URLs/Attachments | 
    
    
    security_result.summary = /ransom/ nocase
    
    $Subject = network.email.subject
    $Sender = network.email.from
    $Receiver = network.email.to
    $Log_Type = metadata.log_type
    $Attachments = strings.coalesce(about.file.full_path, security_result.detection_fields["attachmentNames"])
    $Summary = security_result.summary
    $Url = target.url
    $Action = security_result.action
    $Severity = security_result.severity
    
    match:
      $Sender, $Receiver, $Subject, $Summary, $Url , $Attachments, $Action, $Severity, $Log_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
Recent Ransomware VM Events | 
    
    
    extensions.vulns.vulnerabilities.description = /ransom/ nocase
    
    $Log_Type = metadata.log_type
    $Summary = extensions.vulns.vulnerabilities.description
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    
    match:
      $Summary, $Hostname, $Log_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
    
      $Count desc
      
  
Recent Ransomware DLP Events | 
    
    
    (security_result.rule_name = /ransom/ nocase or security_result.category_details = /ransom/ nocase or security_result.threat_name = /ransom/ nocase or security_result.summary = /ransom/ nocase
    or security_result.description = /ransom/ nocase or metadata.description = /ransom/ nocase or metadata.product_event_type = /ransom/ nocase)
    
    $Log_Type = metadata.log_type
    $Summary = strings.coalesce(metadata.description, metadata.product_event_type, security_result.summary, security_result.rule_name, security_result.description, security_result.threat_name, security_result.category_details)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    $File = strings.coalesce(target.file.full_path, about.file.full_path, target.url)
    $Action = security_result.action
    $Severity = security_result.severity
    
    match:
      $Summary, $File, $Hostname, $Action, $Severity, $Log_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
Recent Endpoint Ransomware Events | 
    
    
    (security_result.rule_name = /ransom/ nocase or security_result.category_details = /ransom/ nocase or security_result.threat_name = /ransom/ nocase or security_result.summary = /ransom/ nocase or security_result.description = /ransom/ nocase or metadata.description = /ransom/ nocase or metadata.product_event_type = /ransom/ nocase)
    
    $Log_Type = metadata.log_type
    $Summary = strings.coalesce(security_result.description, security_result.rule_name, security_result.threat_name, security_result.category_details, security_result.summary, metadata.description, metadata.product_event_type)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    $IP = strings.coalesce(principal.ip, principal.asset.ip, target.ip, target.asset.ip)
    $File = strings.coalesce(target.file.full_path, about.file.full_path, target.url)
    $Action = security_result.action
    $Severity = security_result.severity
    
    match:
      $Summary, $File, $Hostname, $IP, $Action, $Severity, $Log_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
Top 10 Ransomware Log Sources | 
    
    
    (security_result.rule_name = /ransom/ nocase or security_result.category_details = /ransom/ nocase or security_result.threat_name = /ransom/ nocase or extensions.vulns.vulnerabilities.description = /ransom/ nocase or metadata.product_event_type = /ransom/ nocase or security_result.summary = /ransom/ nocase or metadata.description = /ransom/ nocase or security_result.description = /ransom/ nocase)
    
    $Log_Type = metadata.log_type
    
    match:
      $Log_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Ransomware Events Over Time by Product | 
    
    
    (security_result.rule_name = /ransom/ nocase or security_result.category_details = /ransom/ nocase or security_result.threat_name = /ransom/ nocase or extensions.vulns.vulnerabilities.description = /ransom/ nocase or metadata.product_event_type = /ransom/ nocase or security_result.summary = /ransom/ nocase or metadata.description = /ransom/ nocase or security_result.description = /ransom/ nocase)
    
    $Product = metadata.product_name
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Product, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc
      
  
Recent Ransomware NDR Events | 
    
    
    (metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    or metadata.event_type = "NETWORK_UNCATEGORIZED")
    (security_result.rule_name = /ransom/ nocase or security_result.category_details = /ransom/ nocase or security_result.threat_name = /ransom/ nocase or security_result.summary = /ransom/ nocase
    or security_result.description = /ransom/ nocase or metadata.description = /ransom/ nocase or metadata.product_event_type = /ransom/ nocase)
    
    $Log_Type = metadata.log_type
    $Summary = strings.coalesce(metadata.product_event_type, metadata.description, security_result.summary, security_result.description, security_result.rule_name, security_result.category_details, security_result.threat_name)
    $Threat_Name = security_result.threat_name
    $Category = security_result.category_details
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    $File = strings.coalesce(target.file.full_path, about.file.full_path, target.url)
    $Action = security_result.action
    $Severity = security_result.severity
    
    match:
      $Summary, $File, $Threat_Name, $Category, $Hostname, $Action, $Severity, $Log_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
Recent Ransomware Events by Hostname | 
    
    
    (security_result.rule_name = /ransom/ nocase or security_result.category_details = /ransom/ nocase or security_result.threat_name = /ransom/ nocase or extensions.vulns.vulnerabilities.description = /ransom/ nocase or metadata.product_event_type = /ransom/ nocase or security_result.summary = /ransom/ nocase or metadata.description = /ransom/ nocase or security_result.description = /ransom/ nocase)
    
    $Log_Type = metadata.log_type
    $Summary = strings.coalesce(security_result.summary, security_result.description, metadata.description, metadata.product_event_type, security_result.rule_name , extensions.vulns.vulnerabilities.description, security_result.threat_name, security_result.category_details)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    $User = strings.coalesce(principal.user.userid, principal.user.email_addresses, principal.user.user_display_name, target.user.userid, target.user.email_addresses, target.user.user_display_name)
    $File = strings.coalesce(target.file.full_path, about.file.full_path, target.url)
    $Action = security_result.action
    $Severity = security_result.severity
    
    match:
      $Summary, $File, $Hostname, $User, $Action, $Severity, $Log_Type
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
## Role & Permission Audit

This dashboard is a deep-dive dashboard for auditing the management of roles and direct resource permissions.

**Note:** Apply filters to display relevant results on the dashboard.

Top 10 Users Creating RolesTop 10 Users Changing Resource PermissionsTop 10 Users Modifying RolesRecent Roles CreatedTop 10 Resources with Changed PermissionsTop 10 Blocked Source IPs in Role EventsResource Permissions Changed Over TimeIAM Actions Over TimeTotal Roles ModifiedTop 10 Source IPs Modifying RolesRoles Deleted Over TimeActivity on Critical RolesTotal Roles CreatedRoles Created Over TimeRecent Roles ModifiedTop 10 Source IPS Creating RolesRole Lifecycle KPIRoles Modified Over TimeTop 10 Source IPs Changing Resource PermissionsTotal Roles DeletedTop 10 Source IPs Deleting RolesTop 10 Users Deleting Roles

Chart name | Query example  
---|---  
Top 10 Users Creating Roles | 
    
    
    metadata.product_event_type = /Create.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /add role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Log_Type, $Initiator
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Changing Resource Permissions | 
    
    
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    security_result.action = "ALLOW"
    
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $Log_Type = metadata.log_type
    
    match:
      $Log_Type, $Initiator
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Modifying Roles | 
    
    
    metadata.product_event_type = /Update.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /update role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Log_Type, $Initiator
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Recent Roles Created | 
    
    
    metadata.product_event_type = /Create.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /add role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $IP_Address = principal.ip
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $Role = strings.coalesce(target.user.attribute.roles.name, target.resource.name)
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $Role
    
    order:
      $Date desc  
  
Top 10 Resources with Changed Permissions | 
    
    
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Resource_Name = target.resource.name
    
    match:
      $Log_Type, $Resource_Name
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Blocked Source IPs in Role Events | 
    
    
    (metadata.product_event_type = /Create.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /add role definition/ nocase))
    or
    (metadata.product_event_type = /Update.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /update role definition/ nocase))
    or
    (metadata.product_event_type = /Delete.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /delete role definition/ nocase))
    security_result.action = "BLOCK"
    
    $IP_Address = principal.ip
    $Event = metadata.product_event_type
    
    match:
      $IP_Address, $Event
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Resource Permissions Changed Over Time | 
    
    
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
IAM Actions Over Time | 
    
    
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    or metadata.event_type = "USER_UNCATEGORIZED"
    or metadata.event_type = "USER_BADGE_IN"
    or metadata.event_type = "USER_COMMUNICATION"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_LOGIN"
    or metadata.event_type = "USER_LOGOUT"
    or metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    or metadata.event_type = "USER_RESOURCE_ACCESS"
    or metadata.event_type = "USER_RESOURCE_CREATION"
    or metadata.event_type = "USER_RESOURCE_DELETION"
    or metadata.event_type = "USER_RESOURCE_UPDATE_CONTENT"
    or metadata.event_type = "GROUP_UNCATEGORIZED"
    or metadata.event_type = "GROUP_CREATION"
    or metadata.event_type = "GROUP_DELETION"
    or metadata.product_event_type = /(add|delete) group/ nocase
    or metadata.event_type = "GROUP_MODIFICATION"
    or metadata.product_event_type = /(RemoveUserFrom|AddUserTo|Add member to |Remove member from )|(?:group)/ nocase
    or metadata.product_event_type = /(Create|Update|\bDelete).?Role/ nocase
    or (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /(add|update|delete) role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Event = metadata.event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Event
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Total Roles Modified | 
    
    
    metadata.product_event_type = /Update.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /update role definition/ nocase)
    security_result.action = "ALLOW"
    
    outcome:
      $Count = count_distinct(strings.coalesce(target.user.attribute.roles.name, target.resource.name))  
  
Top 10 Source IPs Modifying Roles | 
    
    
     metadata.product_event_type = /Update.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /update role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count
    
    limit:
        10   
  
Roles Deleted Over Time | 
    
    
    metadata.product_event_type = /Delete.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /delete role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Activity on Critical Roles | 
    
    
    metadata.product_event_type = /Create|Remove|Add|Update/ nocase
    strings.coalesce(principal.user.attribute.roles.name, principal.resource.name, target.user.attribute.roles.name, target.resource.name) = /admin/ nocase
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Role = strings.coalesce(principal.user.attribute.roles.name, principal.resource.name, target.user.attribute.roles.name, target.resource.name)
    $Event = metadata.product_event_type
    $User = if(strings.coalesce(principal.user.attribute.roles.name, principal.resource.name) = /admin/ nocase, strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses),
            if(strings.coalesce(target.user.attribute.roles.name, target.resource.name) = /admin/ nocase, strings.coalesce(target.user.windows_sid, target.user.userid, target.user.email_addresses), ""))
    $IP = principal.ip
    
    match:
      $Role, $Event, $Log_Type, $User, $IP
    
    outcome:
      $Date = latest(metadata.event_timestamp)
    
    dedup:
      $Role
    
    order:
      $Date desc  
  
Total Roles Created | 
    
    
    metadata.product_event_type = /Create.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /add role definition/ nocase)
    security_result.action = "ALLOW"
    
    outcome:
      $Count = count_distinct(strings.coalesce(target.user.attribute.roles.name, target.resource.name))  
  
Roles Created Over Time | 
    
    
    metadata.product_event_type = /Create.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /add role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Recent Roles Modified | 
    
    
    (metadata.event_type = "RESOURCE_WRITTEN"
    and metadata.product_event_type = /UpdateRole/ nocase)
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /update role(?: definition)?/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    $IP_Address = principal.ip
    $Role = strings.coalesce(target.user.attribute.roles.name, target.resource.name)
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $Role
    
    order:
      $Date desc  
  
Top 10 Source IPS Creating Roles | 
    
    
    metadata.product_event_type = /Create.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /add role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Role Lifecycle KPI | 
    
    
    (metadata.product_event_type = /Create.?Role/ nocase
        or
        (security_result.category_details = /RoleManagement/ nocase and metadata.product_event_type = /add role definition/ nocase)
        and security_result.action = "ALLOW")
    or
    (metadata.product_event_type = /Update.?Role/ nocase
        or
        (security_result.category_details = /RoleManagement/ nocase and metadata.product_event_type = /update role definition/ nocase)
        and security_result.action = "ALLOW")
    or
    (metadata.product_event_type = /Delete.?Role/ nocase
        or (security_result.category_details = /RoleManagement/ nocase and metadata.product_event_type = /delete role definition/ nocase)
        and security_result.action = "ALLOW")
    
    $Event = if((metadata.product_event_type = /Create.?Role/ nocase or (security_result.category_details = /RoleManagement/ nocase and metadata.product_event_type = /add role definition/ nocase)), "Total Creation",
                if (metadata.product_event_type = /Update.?Role/ nocase or (security_result.category_details = /RoleManagement/ nocase and metadata.product_event_type = /update role definition/ nocase), "Total Modification", "Total Deletion"))
    
    match:
      $Event
    
    outcome:
      $Count = count_distinct(strings.coalesce(target.user.attribute.roles.name, target.resource.name))
    
    order:
      $Count desc  
  
Roles Modified Over Time | 
    
    
    metadata.product_event_type = /Update.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /update role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Log_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Source IPs Changing Resource Permissions | 
    
    
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Total Roles Deleted | 
    
    
    metadata.product_event_type = /Delete.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /delete role definition/ nocase)
    security_result.action = "ALLOW"
    
    outcome:
      $Count = count_distinct(strings.coalesce(target.user.attribute.roles.name, target.resource.name))  
  
Top 10 Source IPs Deleting Roles | 
    
    
    metadata.product_event_type = /Delete.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /delete role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 Users Deleting Roles | 
    
    
    metadata.product_event_type = /Delete.?Role/ nocase
    or
    (security_result.category_details = /RoleManagement/ nocase
    and metadata.product_event_type = /delete role definition/ nocase)
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Initiator =  strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Log_Type, $Initiator
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
## SMB Enumeration

This dashboard provides you with actionable insights into SMB-related activities, including enumeration trends, authentication attempts, and access patterns across users and IP addresses. By identifying suspicious behaviors and potential threats, it helps mitigate risks effectively.

Top 10 SMB Enumeration Attempts by UserRecent Failed SMB Authentication AttemptsSMB Enumeration Attempts Protocol DistributionEnumeration Tools Detected DistributionTop 10 Targeted IPs in SMB EnumerationSMB Enumeration Status DistributionSource IPs Over TimeSMB Commands Over TimeTop 10 Source IPsAverage Enumeration RateTop 10 Commands Used in SMB EnumerationSMB Enumeration Detections Over TimeSMB Authentication Status Distribution

Chart name | Query example  
---|---  
Top 10 SMB Enumeration Attempts by User | 
    
    
    security_result.rule_name = /smb.*enumeration/ nocase
    or (target.process.command_line = /(?:nmap.*(?:\-p(?:\s)?(?:137|138|139|445|139,445)?)(?:(?:\s)?--script smb)?|smbmap|smbclient --list|enum4linux)/ nocase
    and (target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445))
    
    $Command_Line = target.process.command_line
    $User = target.user.userid
    
    match:
      $User, $Command_Line
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Failed SMB Authentication Attempts | 
    
    
    metadata.event_type = "NETWORK_CONNECTION"
    or metadata.product_event_type = /5157/
    target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445
    security_result.action = "BLOCK"
    or security_result.summary = /failed/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Hostname = principal.hostname
    $Source_IP = principal.ip
    $User = strings.coalesce(principal.user.userid, target.user.userid)
    $Port = target.port
    
    match:
      $Date, $Hostname, $Source_IP, $Port, $User
    
    order:
      $Date desc  
  
SMB Enumeration Attempts Protocol Distribution | 
    
    
    security_result.rule_name = /smb.*enumeration/ nocase
    or (target.process.command_line = /(?:nmap.*(?:\-p(?:\s)?(?:137|138|139|445|139,445)?)(?:(?:\s)?--script smb)?|smbmap|smbclient --list|enum4linux)/ nocase
    and (target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445))
    
    $Protocol = network.ip_protocol
    
    match:
      $Protocol
    
    outcome:
      $Count = count(network.ip_protocol)
    
    order:
      $Count desc  
  
Enumeration Tools Detected Distribution | 
    
    
    security_result.rule_name = /smb.*enumeration/ nocase
    or (target.process.command_line = /(?:\bnmap\b.*(?:\-p(?:\s)?(?:137|138|139|445|139,445)?)(?:(?:\s)?--script smb)?|smbmap|smbclient --list|enum4linux)/ nocase
    and (target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445))
    
    $Tool = re.capture(target.process.command_line, `^\w+`)
    
    match:
      $Tool
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Targeted IPs in SMB Enumeration | 
    
    
    security_result.rule_name = /smb.*enumeration/ nocase
    or (target.process.command_line = /(?:nmap.*(?:\-p(?:\s)?(?:137|138|139|445|139,445)?)(?:(?:\s)?--script smb)?|smbmap|smbclient --list|enum4linux)/ nocase
    and (target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445))
    
    $Hostname = principal.hostname
    $Target_IP = target.ip
    
    match:
      $Target_IP, $Hostname
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
SMB Enumeration Status Distribution | 
    
    
    security_result.rule_name = /smb.*enumeration/ nocase
    or (target.process.command_line = /(?:nmap.*(?:\-p(?:\s)?(?:137|138|139|445|139,445)?)(?:(?:\s)?--script smb)?|smbmap|smbclient --list|enum4linux)/ nocase
    and (target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445))
    
    $Status = if(security_result.action = "ALLOW", security_result.action, "BLOCK")
    
    match:
      $Status
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Source IPs Over Time | 
    
    
    target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count_distinct(principal.ip)
    
    order:
      $Date desc  
  
SMB Commands Over Time | 
    
    
    target.process.command_line = /(?:nmap.*(?:\-p(?:\s)?(?:137|138|139|445|139,445)?)(?:(?:\s)?--script smb)?|smb(?:client|map|status)|enum4linux|(?:get|new|remove|set|close)\-smb)|\bnet\s+(?:use|view|share|session|file|user|group|localgroup|accounts|config|start|stop)\b/ nocase
    target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Source IPs | 
    
    
    target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445
    
    $Hostname = principal.hostname
    $Source_IP = principal.ip
    $Source_IP != ""
    
    match:
      $Source_IP, $Hostname
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Average Enumeration Rate | 
    
    
    stage Enumeration{
    security_result.rule_name = /smb.*enumeration/ nocase
    or (target.process.command_line = /(?:nmap.*(?:\-p(?:\s)?(?:137|138|139|445|139,445)?)(?:(?:\s)?--script smb)?|smbmap|smbclient --list|enum4linux)/ nocase
    and (target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445))
    
    $Target_IP = target.ip
    $Hour_Bucket = timestamp.get_hour(metadata.event_timestamp.seconds)
    
    match:
      $Hour_Bucket
    
    outcome:
      $Ip_Count = count_distinct($Target_IP)
    }
    
    outcome:
      $Avg_Enumeration_Rate = math.round(avg($Enumeration.Ip_Count), 2)  
  
Top 10 Commands Used in SMB Enumeration | 
    
    
    security_result.rule_name = /smb.*enumeration/ nocase
    or (target.process.command_line = /(?:nmap.*(?:\-p(?:\s)?(?:137|138|139|445|139,445)?)(?:(?:\s)?--script smb)?|smbmap|smbclient --list|enum4linux)/ nocase
    and (target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445))
    
    $Command_Line = target.process.command_line
    
    match:
      $Command_Line
    
    outcome:
      $Count = count(target.process.command_line)
    
    order:
      $Count desc
    
    limit:
        10  
  
SMB Enumeration Detections Over Time | 
    
    
    security_result.rule_name = /smb.*enumeration/ nocase
    or (target.process.command_line = /(?:nmap.*(?:\-p(?:\s)?(?:137|138|139|445|139,445)?)(?:(?:\s)?--script smb)?|smbmap|smbclient --list|enum4linux)/ nocase
    and (target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445))
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
SMB Authentication Status Distribution | 
    
    
    metadata.event_type = "NETWORK_CONNECTION"
    or metadata.product_event_type = /5156|5157/
    target.port = 137
    or target.port = 138
    or target.port = 139
    or target.port = 445
    
    $Status = if(security_result.summary = /failed/, "BLOCK", security_result.action)
    
    match:
      $Status
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
## SecOps Audit & Activity Monitoring

This dashboard provides essential insights into security posture, tracks events, user activities, and blocked actions within Chronicle Google APIs.

Events Over TimeTop 10 Event TypesRecent Blocked ActionsTop 10 Source IPs by Event TypeBlocked Events Over TimeOff Hours Unusual EventsRecent Risky ActionsTop 10 Users by Risky ActionTop 10 Users by Event TypeBlocked SecOps Events by LocationAction by Event Types: Allow vs. BlockOff Hours Unusual Actions by Category

Chart name | Query example  
---|---  
Events Over Time | 
    
    
    target.application = /(?:chronicle|backstory).googleapis\.com/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Event Types | 
    
    
    target.application = /(?:chronicle|backstory).googleapis\.com/ nocase
    
    $Event_Type = metadata.event_type
    
    match:
      $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Blocked Actions | 
    
    
    target.application = /(?:chronicle|backstory).googleapis.com/ nocase
    security_result.action = "BLOCK"
    
    $Date = timestamp.get_timestamp((metadata.event_timestamp.seconds), "%F %T ")
    $Description = metadata.description
    $Event_Type = metadata.event_type
    $User = principal.user.userid
    
    match:
      $Date, $Event_Type, $Description, $User
    
    order:
      $Date desc  
  
Top 10 Source IPs by Event Type | 
    
    
    target.application = /(?:chronicle|backstory).googleapis\.com/ nocase
    
    $Event_Type = metadata.event_type
    $Source_IP = principal.ip
    
    match:
      $Event_Type, $Source_IP
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Blocked Events Over Time | 
    
    
    target.application = /(?:chronicle|backstory).googleapis.com/ nocase
    security_result.action = "BLOCK"
    
    $Date = timestamp.get_date((metadata.event_timestamp.seconds))
    $Event_Type = re.capture(metadata.product_event_type, `\b[A-Za-z]+$`)
    
    match:
      $Date, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Off Hours Unusual Events | 
    
    
    target.application = /(?:chronicle|backstory).googleapis.com/ nocase
    
    (
        (timestamp.get_day_of_week(metadata.event_timestamp.seconds, "UTC") = 1 or timestamp.get_day_of_week(metadata.event_timestamp.seconds, "UTC") = 7)
        or
        ((timestamp.get_day_of_week(metadata.event_timestamp.seconds, "UTC") >= 2 and timestamp.get_day_of_week(metadata.event_timestamp.seconds, "UTC") <= 6)
        and
        ((timestamp.get_hour(metadata.event_timestamp.seconds, "UTC") >= 0 and timestamp.get_hour(metadata.event_timestamp.seconds, "UTC") <= 8) or timestamp.get_hour(metadata.event_timestamp.seconds, "UTC") > 19))
    )
    
    $Event_Type = metadata.event_type
    $Product_Event = metadata.product_event_type
    
    match:
      $Event_Type, $Product_Event
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T ")
    
    order:
      $Date desc  
  
Recent Risky Actions | 
    
    
    target.application = /(?:chronicle|backstory).googleapis.com/ nocase
    metadata.product_event_type = /\b(?:Delete|Remove|Disable|Update)/ nocase
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    $Event_Type = re.capture(metadata.product_event_type, `\b(?:Delete|Remove|Disable|Update)[A-Za-z]+`)
    $Description = metadata.description
    $User = re.capture(principal.user.userid, `subject\/([^\/]+)`)
    
    match:
      $Date, $Event_Type, $Description, $User
    
    order:
      $Date desc  
  
Top 10 Users by Risky Action | 
    
    
    target.application = /(?:chronicle|backstory).googleapis.com/ nocase
    metadata.product_event_type = /\b(?:Delete|Remove|Disable|Update)/ nocase
    
    $Event_Type = re.capture(metadata.product_event_type, `\b(?:Delete|Remove|Disable|Update)[A-Za-z]+`)
    $User = re.capture(principal.user.userid, `subject\/([^\/]+)`)
    
    match:
      $User, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Users by Event Type | 
    
    
    target.application = /(?:chronicle|backstory).googleapis\.com/ nocase
    
    $Event_Type = metadata.event_type
    $User = principal.user.userid
    
    match:
      $User, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Blocked SecOps Events by Location | 
    
    
    target.application = /(?:chronicle|backstory).googleapis.com/ nocase
    security_result.action = "BLOCK"
    
    $Countries = principal.location.country_or_region
    $Latitude = principal.location.region_coordinates.latitude
    $Longitude = principal.location.region_coordinates.longitude
    
    match:
      $Countries, $Latitude, $Longitude
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Action by Event Types: Allow vs. Block | 
    
    
    target.application = /(?:chronicle|backstory).googleapis\.com/ nocase
    security_result.action = "ALLOW"
    or security_result.action = "BLOCK"
    
    $Event_Type = metadata.event_type
    $Action = security_result.action
    
    match:
      $Event_Type, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Off Hours Unusual Actions by Category | 
    
    
    target.application = /(?:chronicle|backstory).googleapis.com/ nocase
    
    (
        (timestamp.get_day_of_week(metadata.event_timestamp.seconds, "UTC") = 1 or timestamp.get_day_of_week(metadata.event_timestamp.seconds, "UTC") = 7)
        or
        ((timestamp.get_day_of_week(metadata.event_timestamp.seconds, "UTC") >= 2 and timestamp.get_day_of_week(metadata.event_timestamp.seconds, "UTC") <= 6)
        and
        ((timestamp.get_hour(metadata.event_timestamp.seconds, "UTC") >= 0 and timestamp.get_hour(metadata.event_timestamp.seconds, "UTC") <= 8) or timestamp.get_hour(metadata.event_timestamp.seconds, "UTC") > 19))
    )
    
    $Event_Type = metadata.event_type
    $Product_Event = metadata.product_event_type
    $Service = re.capture(metadata.product_event_type, `([A-Za-z]+Service)`)
    
    match:
      $Product_Event, $Service
    
    outcome:
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T ")
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
## SecOps Log Monitoring

This dashboard provides insights into Log Data Management, highlighting ingestion latency, and component status. It helps you optimize performance, reduce data loss, and enhance security monitoring.

Average Log Ingestion Time by Log Type

Chart name | Query example  
---|---  
Average Log Ingestion Time by Log Type | 
    
    
    $Log_Type = metadata.log_type
    
    $Ingestion_Time = math.abs(metadata.ingested_timestamp.seconds - metadata.event_timestamp.seconds)
    
    match:
      $Log_Type
    
    outcome:
      $Avg_Ingestion_Time_ = math.ceil(avg($Ingestion_Time))
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Date desc  
  
## Security Posture Management

This dashboard provides a real-time overview of your organization's security status, highlighting threats, incidents, and vulnerabilities. It includes detections, security, and system update summary and asset monitoring, enabling security teams to assess risks and threat posture and implement remediation strategies effectively. This centralized view helps enhance overall security posture and streamline incident response.

## Service Account Overview

This dashboard helps security teams and administrators monitor service account activity by providing insights into usage patterns, login attempts, and account modifications. It enables informed decision-making to identify security risks, address vulnerabilities, and ensure system integrity. Note: use the available filters to narrow down the results as required.

Top 10 ActionsRecent Permissions ModifiedSuccessful Logins Over TimeTop 10 User Permissions ModifiedRecent Password ChangesService Accounts Deleted Over TimeFailed Logins Over TimeUsage Over TimeRecent Service Accounts DeletedTop 10 Service Accounts by LoginRecent Service Accounts CreatedTop 10 Service AccountsService Accounts Created Over TimeHigh Volume Kerberos Service Ticket RequestsTop 10 Source IPs by Failed LoginTop 10 Source IPs by Interactive LoginInteractive Logins Over TimePassword Changes Over Time

Chart name | Query example  
---|---  
Top 10 Actions | 
    
    
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Product_Event = metadata.product_event_type
    $Product_Event != ""
    
    match:
      $Product_Event
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Permissions Modified | 
    
    
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Log_Type = metadata.log_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $User = strings.coalesce(target.user.userid, target.user.email_addresses)
    $IP_Address = principal.ip
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $User
    
    order:
      $Date desc  
  
Successful Logins Over Time | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "ALLOW"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc   
  
Top 10 User Permissions Modified | 
    
    
    metadata.event_type = "RESOURCE_PERMISSIONS_CHANGE"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $User = strings.coalesce(target.user.userid, target.user.email_addresses)
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Password Changes | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Log_Type = metadata.log_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $User = strings.coalesce(target.user.userid, target.user.email_addresses)
    $IP_Address = principal.ip
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $User
    
    order:
      $Date desc  
  
Service Accounts Deleted Over Time | 
    
    
    metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_RESOURCE_DELETION"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Failed Logins Over Time | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "BLOCK"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Usage Over Time | 
    
    
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Recent Service Accounts Deleted | 
    
    
    metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_RESOURCE_DELETION"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Log_Type = metadata.log_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $User = strings.coalesce(target.user.userid, target.user.email_addresses)
    $IP_Address = principal.ip
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $User
    
    order:
      $Date desc  
  
Top 10 Service Accounts by Login | 
    
    
    metadata.event_type = "USER_LOGIN"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Service_Account = group(principal.user.userid, target.user.userid)
    $Service_Account != ""
    
    match:
      $Service_Account
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Service Accounts Created | 
    
    
    metadata.event_type = "USER_CREATION"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Log_Type = metadata.log_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $User = strings.coalesce(target.user.userid, target.user.email_addresses)
    $IP_Address = principal.ip
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $User
    
    order:
      $Date desc  
  
Top 10 Service Accounts | 
    
    
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Service_Account = group(principal.user.userid, target.user.userid)
    $Service_Account != ""
    
    match:
      $Service_Account
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Service Accounts Created Over Time | 
    
    
    metadata.event_type = "USER_CREATION"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
High Volume Kerberos Service Ticket Requests | 
    
    
    metadata.product_event_type = /4769/ nocase
    target.application != /\$$/ nocase
    additional.fields["TicketEncryptionType"] = /0x(1|2|3|12|17)/ nocase
    additional.fields["TicketOptions"] = /0x408(1000|0000|1001)0/ nocase
    
    $Host = principal.hostname
    
    match:
      $Host over 1h
    
    outcome:
      $Count = count_distinct(target.application)
    
    condition:
      $Count >= 10
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs by Failed Login | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "BLOCK"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Source_IP = principal.ip
    $Source_IP != ""
    
    match:
      $Source_IP
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs by Interactive Login | 
    
    
    metadata.event_type = "USER_LOGIN"
    extensions.auth.mechanism = "INTERACTIVE"
    or extensions.auth.mechanism = "CACHED_INTERACTIVE"
    or extensions.auth.mechanism = "CACHED_REMOTE_INTERACTIVE"
    or extensions.auth.mechanism = "REMOTE_INTERACTIVE"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Source_IP = principal.ip
    
    match:
      $Source_IP
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Interactive Logins Over Time | 
    
    
    metadata.event_type = "USER_LOGIN"
    extensions.auth.mechanism = "INTERACTIVE"
    or extensions.auth.mechanism = "CACHED_INTERACTIVE"
    or extensions.auth.mechanism = "CACHED_REMOTE_INTERACTIVE"
    or extensions.auth.mechanism = "REMOTE_INTERACTIVE"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Password Changes Over Time | 
    
    
    metadata.event_type = "USER_CHANGE_PASSWORD"
    principal.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or principal.resource.resource_type = "SERVICE_ACCOUNT"
    or principal.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or target.user.account_type = "SERVICE_ACCOUNT_TYPE"
    or target.resource.resource_type = "SERVICE_ACCOUNT"
    or target.user.attribute.roles.type = "SERVICE_ACCOUNT"
    or strings.coalesce(principal.resource.type, principal.user.attribute.roles.name, principal.resource.resource_subtype, principal.user.userid, target.resource.type, target.user.attribute.roles.name, target.resource.resource_subtype, target.user.userid) = /(?i)service.*(?:account|^principal$)/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
## Single Sign-On (SSO) Monitoring

This dashboard helps security teams track sso activity, detect unauthorized access, and optimize authentication to improve security and ensure compliance.

SSO Security AlertsSSO Logins Over Time by ActionUnauthorized SSO AccessSSO Success vs. Failure RateFailed Login Attempts by UserSSO Events Over Time by SeverityTotal SSO LoginsSSO Activity LogsSSO Logins by Top 10 ApplicationSSO Usage TrendSSO Anomalous Login LocationsSource Geolocation OverviewTop 10 Users by LoginsTop 10 Applications by Failed LoginTop 10 Vendor Alerts

Chart name | Query example  
---|---  
SSO Security Alerts | 
    
    
    $auth_type = extensions.auth.type
    $auth_type = "SSO"
    $alert_state = security_result.alert_state
    $alert_state = "ALERTING"
    $user = strings.coalesce(target.user.user_display_name, principal.user.user_display_name)
    $user != ""
    $action = security_result.action
    $action != "UNKNOWN_ACTION"
    $event_name = security_result.summary
    $severity = security_result.severity
    $category = security_result.category_details
    
    match:
    $event_name, $severity, $category
    outcome :
    $count  = count($event_name)
    
      
  
SSO Logins Over Time by Action | 
    
    
    extensions.auth.type = "SSO"
    
    $Action = security_result.action
    $Event_Type = metadata.event_type
    $Event_Type = "USER_LOGIN"
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Action
    
    outcome :
      $Count  = count(metadata.id)
    
      
  
Unauthorized SSO Access | 
    
    
    extensions.auth.type = "SSO"
    
    $User = strings.coalesce(target.user.userid, target.user.user_display_name, target.user.email_addresses, principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Action = security_result.action
    $Action != "ALLOW"
    $Summary = strings.coalesce(security_result.summary, metadata.description, security_result.description)
    $Severity = security_result.severity
    $Category = security_result.category_details
    
    match:
      $Summary,$User, $Severity, $Action,$Category
    
    outcome :
      $Count  = count(metadata.id)
    
      
  
SSO Success vs. Failure Rate | 
    
    
    $auth_type = extensions.auth.type
    $auth_type = "SSO"
    $user = strings.coalesce(target.user.user_display_name, principal.user.user_display_name)
    $user != ""
    $action = security_result.action
    $action != "UNKNOWN_ACTION"
    
    match:
    $action
    
    outcome :
    $count  = count($action)
      
  
Failed Login Attempts by User | 
    
    
    metadata.event_type = "USER_LOGIN"
    extensions.auth.type = "SSO"
    security_result.action = "BLOCK"
    
    $User = strings.coalesce(target.user.userid, target.user.user_display_name, target.user.email_addresses, principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $User != ""
    match:
      $User
    
    outcome :
      $Count  = count(metadata.id)
    
    order:
      $Count desc  
  
SSO Events Over Time by Severity | 
    
    
    extensions.auth.type = "SSO"
    $Severity = security_result.severity
    (security_result.severity = "CRITICAL" or security_result.severity = "HIGH")
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
    $Date, $Severity
    
    outcome :
    $Count = count(metadata.id)
    
    order:
    $Date asc  
  
Total SSO Logins | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $auth_type = extensions.auth.type
    $auth_type = "SSO"
    $user = strings.coalesce(target.user.user_display_name, principal.user.user_display_name)
    $user != ""
    
    outcome :
    $count  = count($user)
    
      
  
SSO Activity Logs | 
    
    
    $auth_type = extensions.auth.type
    $auth_type = "SSO"
    $user = strings.coalesce(target.user.user_display_name, principal.user.user_display_name)
    $user != ""
    $location = principal.ip_geo_artifact.location.country_or_region
    $summary = security_result.summary
    $summary != ""
    $action = security_result.action
    
    match:
    $summary, $location, $action
    
    outcome :
    $count  = count($summary)
    order:
    $count desc
    
      
  
SSO Logins by Top 10 Application | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $auth_type = extensions.auth.type
    $auth_type = "SSO"
    $user = strings.coalesce(target.user.user_display_name, principal.user.user_display_name)
    $user != ""
    $application = target.application
    $application != ""
    
    match:
    $application
    
    outcome :
    $count  = count($application)
    order:
    $count desc
    limit: 10
      
  
SSO Usage Trend | 
    
    
    $auth_type = extensions.auth.type
    $auth_type = "SSO"
    $user = target.user.user_display_name
    $user != ""
    $location = principal.ip_geo_artifact.location.country_or_region
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
    $auth_type, $date
    
    outcome :
    $count  = count($auth_type)
    
      
  
Unauthorized SSO Access | 
    
    
    $auth_type = extensions.auth.type
    $auth_type = "SSO"
    $alert_state = security_result.alert_state
    $user = strings.coalesce(target.user.user_display_name, principal.user.user_display_name)
    $user != ""
    $action = security_result.action
    $action != "UNKNOWN_ACTION"
    $event_name = security_result.summary
    $event_name != ""
    $severity = security_result.severity
    $category = security_result.category_details
    $category != ""
    
    match:
    $event_name,$user, $severity, $action,$category
    outcome :
    $count  = count($event_name)
    
      
  
SSO Anomalous Login Locations | 
    
    
    $auth_type = extensions.auth.type
    $auth_type = "SSO"
    $user = strings.coalesce(target.user.user_display_name, principal.user.user_display_name)
    $user != ""
    $location = principal.ip_geo_artifact.location.country_or_region
    $location != ""
    $location != "United States"
    match:
    $location
    
    outcome :
    $count  = count($location)
    $latitude = max(principal.ip_geo_artifact.location.region_coordinates.latitude)
    $longitude = max(principal.ip_geo_artifact.location.region_coordinates.longitude)
    
      
  
Source Geolocation Overview | 
    
    
    metadata.event_type = "USER_LOGIN"
    extensions.auth.type = "SSO"
    
    $Location = principal.ip_geo_artifact.location.country_or_region
    
    match:
      $Location
    
    outcome :
      $Count  = count(metadata.id)
      $Latitude = max(principal.ip_geo_artifact.location.region_coordinates.latitude)
      $Longitude = max(principal.ip_geo_artifact.location.region_coordinates.longitude)
    
      
  
Top 10 Users by Logins | 
    
    
    $event_type = metadata.event_type
    $event_type = "USER_LOGIN"
    $auth_type = extensions.auth.type
    $auth_type = "SSO"
    $user = strings.coalesce(target.user.user_display_name, principal.user.user_display_name)
    $user != ""
    
    match:
    $user
    
    outcome :
    $count  = count($user)
    order:
    $count desc
    limit:
    10
      
  
Top 10 Applications by Failed Login | 
    
    
    metadata.event_type = "USER_LOGIN"
    extensions.auth.type = "SSO"
    security_result.action = "BLOCK"
    
    $Application = target.application
    $Application != ""
    match:
      $Application
    
    outcome :
      $Count  = count(metadata.id)
    
    Order:
      $Count desc
    
    limit:
        10
      
  
Top 10 Vendor Alerts | 
    
    
    extensions.auth.type = "SSO"
    
    $Rule_Name = security_result.rule_name
    $Rule_Name != ""
    
    match:
      $Rule_Name
    
    outcome :
      $Count  = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
      
  
## Sysmon Monitoring

This dashboard is used to analyze and monitor logs generated by sysmon. It provides insights into system activity, including process creations, network connections, and file changes. By aggregating and visualizing this data, the dashboard helps security analysts identify suspicious behavior, track potential threats, and respond accordingly.

Recent Service EventsTop 10 HostsTop 10 Sysmon Event IDsAutorun Registry Changes Over TimeRecent WMI EventsImage Load Events Over Time by Signature StatusEvent Type DistributionDistinct HostsTop 10 Command LinesTop 10 Processes Initiating Network ConnectionEvent Types BreakdownTop 10 Files CreatedTop 10 DNS Queried Domains by Source ProcessDistinct UsersTop 10 Parent ProcessesTop 10 UsersProcess Access Events with Injection Rights Over TimeTotal Sysmon EventsTop 10 ProcessesDriver Load Events Over Time by Signature StatusSysmon Events TrendTotal Distinct HostsSysmon Events Over TimeTop 10 Modified Registry KeysTotal Distinct Users

Chart name | Query example  
---|---  
Recent Service Events | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    metadata.product_event_type = "4"
    or metadata.product_event_type = "5"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Hosts | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    
    $Hostname = $event.principal.hostname
    $Hostname != ""
    
    match:
      $Hostname
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Top 10 Sysmon Event IDs | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    
    $Event_ID = metadata.product_event_type
    
    match:
      $Event_ID
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Autorun Registry Changes Over Time | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    metadata.product_event_type = "12"
    or metadata.product_event_type = "13"
    or metadata.product_event_type = "14"
    target.registry.registry_key = /(?:HKCU|HKLM)\\Software\\Microsoft\\Windows(?:\sNT)?\\CurrentVersion\\(?:Run(?:Once)?|Winlogon\\(?:Shell|Userinit))/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Recent WMI Events | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    metadata.product_event_type = "19"
    or metadata.product_event_type = "20"
    or metadata.product_event_type = "21"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Image Load Events Over Time by Signature Status | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    metadata.product_event_type = "7"
    
    $Signature_Status = target.resource.attribute.labels["SignatureStatus"]
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Signature_Status
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Event Type Distribution | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    
    $Event_Type = metadata.event_type
    
    match:
      $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Distinct Hosts | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    
    outcome:
      $Count = count_distinct($event.principal.hostname)  
  
Top 10 Command Lines | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    
    $Command = target.process.command_line
    $Command != ""
    
    match:
      $Command
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Processes Initiating Network Connection | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    metadata.event_type = "NETWORK_CONNECTION"
    
    $Process = principal.process.file.full_path
    
    match:
      $Process
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Event Types Breakdown | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    
    $Event_Type = $event.metadata.event_type
    
    match:
      $Event_Type
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc  
  
Top 10 Files Created | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    $event.metadata.event_type = "FILE_CREATION"
    
    $File = $event.target.file.full_path
    
    match:
      $File
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 DNS Queried Domains by Source Process | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    metadata.product_event_type = "22"
    
    $Source_Process = strings.coalesce(principal.process.file.full_path, principal.hostname)
    $Domain = network.dns.questions.name
    
    match:
      $Domain, $Source_Process
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Distinct Users | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    
    outcome:
      $Count = count_distinct($event.principal.user.userid)  
  
Top 10 Hosts | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    
    $Hostname = principal.hostname
    $Hostname != ""
    
    match:
      $Hostname
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 Parent Processes | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    
    $Process = principal.process.file.full_path
    $Process != ""
    
    match:
      $Process
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 Users | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    
    $User = $event.principal.user.userid
    $User != ""
    
    match:
      $User
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Process Access Events with Injection Rights Over Time | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    metadata.product_event_type = "10"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Target_Process = target.process.file.full_path
    
    match:
      $Date, $Target_Process
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Total Sysmon Events | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    
    outcome:
      $Count = count($event.metadata.id)  
  
Top 10 Processes | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    
    $Process = target.process.file.full_path
    $Process != ""
    
    match:
      $Process
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Processes | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    
    $Process = $event.target.process.file.full_path
    $Process != ""
    
    match:
      $Process
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Command Lines | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    
    $Command = $event.target.process.command_line
    $Command != ""
    
    match:
      $Command
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Sysmon Event IDs | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    
    $Event_ID = $event.metadata.product_event_type
    
    match:
      $Event_ID
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Driver Load Events Over Time by Signature Status | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    metadata.product_event_type = "6"
    
    $Signature_Status = target.resource.attribute.labels["SignatureStatus"]
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Signature_Status
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Sysmon Events Trend | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Top 10 Processes Initiating Network Connection | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    $event.metadata.event_type = "NETWORK_CONNECTION"
    
    $Process = $event.principal.process.file.full_path
    
    match:
      $Process
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Files Created | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    metadata.event_type = "FILE_CREATION"
    
    $Source = principal.process.file.full_path
    $File = target.file.full_path
    
    match:
      $File, $Source
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    
    $User = principal.user.userid
    $User != ""
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Total Sysmon Events | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    
    outcome:
      $Count = count(metadata.id)  
  
Total Distinct Hosts | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    
    outcome:
      $Count = count_distinct(principal.hostname)  
  
Sysmon Events Over Time | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Modified Registry Keys | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    metadata.product_event_type = "13"
    
    $Registry = target.registry.registry_key
    
    match:
      $Registry
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Total Distinct Users | 
    
    
    metadata.log_type = "WINDOWS_SYSMON"
    
    outcome:
      $Count = count_distinct(principal.user.userid)  
  
Top 10 Parent Processes | 
    
    
    $event.metadata.log_type = "WINDOWS_SYSMON"
    
    $Process = $event.principal.process.file.full_path
    $Process != ""
    
    match:
      $Process
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10   
  
## User Lifecycle Audit

This dashboard is a detailed dashboard for security managers and auditors to review user account management activities. It provides a comprehensive view of the user lifecycle, helping ensure that provisioning and de-provisioning policies are followed correctly.

**Note:** Apply filters to display relevant results on the dashboard.

Top 10 Source IPs Creating UsersRecent Users Account CreatedUsers Deleted Over TimeActivity from Disabled or Deleted AccountsTop 10 Source IPs Deleting UsersTop 10 Users Modifying UsersUser Events Over TimeUsers Created Over TimeRecent Users Account ModifiedUsers Modified Over TimeTop 10 Users Deleting UsersTop 10 Source IPs Modifying UsersTop 10 Users Creating Users

Chart name | Query example  
---|---  
Top 10 Source IPs Creating Users | 
    
    
    metadata.event_type = "USER_CREATION"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Recent Users Account Created | 
    
    
    metadata.event_type = "USER_CREATION"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $User = strings.coalesce(target.user.userid, target.user.email_addresses)
    $IP_Address = principal.ip
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $User
    
    order:
      $Date desc  
  
Users Deleted Over Time | 
    
    
    metadata.event_type = "USER_DELETION"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Activity from Disabled or Deleted Accounts | 
    
    
    $User = strings.coalesce(target.user.userid, target.user.email_addresses, target.user.windows_sid)
    $User != ""
    
    match:
      $User
    
    outcome:
      $Deletion_Time = max(if(metadata.event_type = "USER_DELETION", metadata.event_timestamp.seconds, 0))
      $Deletion_Timestamp = timestamp.get_timestamp($Deletion_Time, "%F %T ")
      $Recent_Activity = max(metadata.event_timestamp.seconds)
      $Recent_Activity_Timestamp = timestamp.get_timestamp($Recent_Activity, "%F %T ")
      $Status = if($Deletion_Time != 0 AND ($Recent_Activity > $Deletion_Time), "Active Deleted Account", "Inactive Deleted Account")
      $Event_Activities = array_distinct(metadata.event_type)
    
    condition:
        arrays.contains($Event_Activities, "USER_DELETION") AND $Status != "Inactive Deleted Account"
    
    order:
      $User desc
    
    unselect:
      $Event_Activities, $Deletion_Time, $Recent_Activity  
  
Top 10 Source IPs Deleting Users | 
    
    
    metadata.event_type = "USER_DELETION"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Modifying Users | 
    
    
    metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
User Events Over Time | 
    
    
    metadata.event_type = "USER_CREATION"
    or metadata.event_type = "USER_DELETION"
    or metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $Event = metadata.event_type
    
    match:
      $Date, $Event
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Users Created Over Time | 
    
    
    metadata.event_type = "USER_CREATION"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Recent Users Account Modified | 
    
    
    metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Event_Type = metadata.event_type
    $Log_Type = metadata.log_type
    $User = strings.coalesce(target.user.userid, target.user.email_addresses)
    $Initiator = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    $IP_Address = principal.ip
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds, "%F %T ")
    
    match:
      $Date, $Log_Type, $Initiator, $IP_Address, $User, $Event_Type
    
    order:
      $Date desc  
  
Users Modified Over Time | 
    
    
    metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Top 10 Users Deleting Users | 
    
    
    metadata.event_type = "USER_DELETION"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Source IPs Modifying Users | 
    
    
    metadata.event_type = "USER_CHANGE_PERMISSIONS"
    or metadata.event_type = "USER_CHANGE_PASSWORD"
    or metadata.event_type = "USER_RESOURCE_UPDATE_PERMISSIONS"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $IP_Address = principal.ip
    
    match:
      $Log_Type, $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Users Creating Users | 
    
    
    metadata.event_type = "USER_CREATION"
    security_result.action = "ALLOW"
    
    $Log_Type = metadata.log_type
    $User = strings.coalesce(principal.user.windows_sid, principal.user.userid, principal.user.email_addresses)
    
    match:
      $Log_Type, $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
## User Sign In Overview

This dashboard provides a comprehensive analysis of authentication activities, helping you identify and monitor sign-in events. This helps you detect potentially risky users, analyze sign-in statuses and trends, and understand geographical activity and associated hosts. You can also investigate unusual login behaviors, respond to potential security breaches, and maintain robust security through continuous monitoring and proactive threat detection.

Sign Ins by CountryNumber of Successful Logins in the Past DayTop 10 IPs by Sign In StatusTop 10 Src/Dest Talkers Over the Past Day - BytesTop 10 Applications by Sign InsSign-ins by ApplicationTop 10 Source Target Pair by Event CountNumber of Successful Sign InsSign-ins by StatusTop 10 Users by Failed Sign InsUsers by Sign In StatusSign In Location MapSign Ins by Status Over TimeHostnames by Sign In StatusAbu Event Count by Target IPSign Ins by ApplicationTop 10 IPs by Failed Sign InsTop 5 Src/Dest Talkers Over the Past DayTop 10 Hostnames by Successful Sign InsCredential Access Sign In EventsNumber of Failed Sign InsIPs by Sign In StatusFailed Logins by Count (Last 24 Hours)Top 10 IPs by Successful Sign InsTop 10 Countries by Sign InsEvent Count by Log Type by DateSign Ins by StatusTop 10 Hostnames by Failed Sign InsTop 10 Src/Dest Talkers Over the Past DayInitial Access Sign In EventsTop 10 Users by Sign In StatusLogin Failure RateTop 10 Users by Successful Sign Ins

Chart name | Query example  
---|---  
Sign Ins by Country | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $Country = principal.location.country_or_region
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Number of Successful Logins in the Past Day | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = $action
    $action = "ALLOW"
    match:
      $action
    outcome:
      $event_count = count_distinct(metadata.id)
      
  
Top 10 IPs by Sign In Status | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $IP_Address = principal.ip
    
    match:
      $IP_Address
    
    outcome:
      $Count = count(metadata.id)
      $Failed_Login_Count = sum(if(security_result.action = "BLOCK", 1, 0))
      $Successful_Login_Count = sum(if(security_result.action = "ALLOW", 1, 0))
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Src/Dest Talkers Over the Past Day - Bytes | 
    
    
    metadata.event_type = "NETWORK_CONNECTION"
    $pip = principal.ip
    $tip = target.ip
    match:
      $pip, $tip
    outcome:
      $event_count = count_distinct(metadata.id)
      $bytes_sent = sum(network.sent_bytes)
      $bytes_received = sum(network.received_bytes)
    order:
      $bytes_sent desc
    limit:
        10  
  
Top 10 Applications by Sign Ins | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $Application = target.application
    
    match:
      $Application
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Sign-ins by Application | 
    
    
    target.application != ""
    $application = target.application
    $login_status = security_result.action
    match:
      $application, $login_status
    outcome:
      $event_count = count_distinct(metadata.id)
    order:
      $event_count desc  
  
Top 10 Source Target Pair by Event Count | 
    
    
    principal.hostname != ""
    target.ip != ""
    $source = principal.hostname
    $target = target.ip
    match:
      $source, $target
    outcome:
      $event_count = count_distinct(metadata.id)
    order:
      $event_count desc
    limit:
        10  
  
Number of Successful Sign Ins | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "ALLOW"
    
    outcome:
      $Count = count(metadata.id)  
  
Sign-ins by Status | 
    
    
    metadata.event_type = "USER_LOGIN"
    $security_result = security_result.action
    match:
      $security_result
    outcome:
      $event_count = count_distinct(metadata.id)  
  
Top 10 Users by Failed Sign Ins | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "BLOCK"
    
    $User = target.user.userid
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
    10  
  
Users by Sign In Status | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $User = target.user.userid
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
      $Failed_Login_Count = sum(if(security_result.action = "BLOCK", 1, 0))
      $Successful_Login_Count = sum(if(security_result.action = "ALLOW", 1, 0))
    
    order:
      $Count desc  
  
Sign In Location Map | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $IP_Address = principal.ip
    $Latitude = principal.location.region_latitude
    $Latitude != 0
    $Longitude = principal.location.region_longitude
    $Longitude != 0
    
    match:
      $IP_Address, $Latitude, $Longitude
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
      
  
Sign Ins by Status Over Time | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Action, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count asc  
  
Hostnames by Sign In Status | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $Hostname = principal.hostname
    
    match:
      $Hostname
    
    outcome:
      $Count = count(metadata.id)
      $Failed_Login_Count = sum(if(security_result.action = "BLOCK", 1, 0))
      $Successful_Login_Count = sum(if(security_result.action = "ALLOW", 1, 0))
    
    order:
      $Count desc  
  
Abu Event Count by Target IP | 
    
    
    principal.hostname = "abu"
    $target = target.ip
    match:
      $target
    outcome:
      $event_count = count_distinct(metadata.id)  
  
Sign Ins by Application | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $Application = target.application
    
    match:
      $Application
    
    outcome:
      $Count = count(metadata.id)
      $Failed_Login_Count = sum(if(security_result.action = "BLOCK", 1, 0))
      $Successful_Login_Count = sum(if(security_result.action = "ALLOW", 1, 0))
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 IPs by Failed Sign Ins | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "BLOCK"
    
    $IP_Address = principal.ip
    
    match:
      $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 5 Src/Dest Talkers Over the Past Day | 
    
    
    metadata.event_type = "NETWORK_CONNECTION"
    $ip_pair = strings.concat(principal.ip,"/",target.ip)
    principal.ip != "10.9.8.7"
    match:
      $ip_pair
    outcome:
      $event_count = count_distinct(metadata.id)
    order:
      $event_count desc
    limit:
        5  
  
Top 10 Hostnames by Successful Sign Ins | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "ALLOW"
    
    $Hostname = principal.hostname
    
    match:
      $Hostname
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Credential Access Sign In Events | 
    
    
    metadata.event_type = "USER_LOGIN"
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) = /Credential Access/ nocase
    
    outcome:
      $Count = count(metadata.id)  
  
Number of Failed Sign Ins | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "BLOCK"
    
    outcome:
      $Count = count(metadata.id)  
  
IPs by Sign In Status | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $IP_Address = principal.ip
    
    match:
      $IP_Address
    
    outcome:
      $Count = count(metadata.id)
      $Failed_Login_Count = sum(if(security_result.action = "BLOCK", 1, 0))
      $Successful_Login_Count = sum(if(security_result.action = "ALLOW", 1, 0))
    
    order:
      $Count desc  
  
Failed Logins by Count (Last 24 Hours) | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "BLOCK"
    
    $Date = timestamp.get_timestamp(metadata.event_timestamp.seconds)
    $Hostname = principal.hostname
    $IP_Address = principal.ip
    $User = strings.coalesce(target.user.userid, target.user.user_display_name, principal.user.userid, principal.user.user_display_name)
    
    match:
      $Date, $User, $Hostname, $IP_Address
    
    outcome:
      $Failed_Logins = count(metadata.id)
    
    order:
      $Failed_Logins desc  
  
Top 10 IPs by Successful Sign Ins | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "ALLOW"
    
    $IP_Address = principal.ip
    
    match:
      $IP_Address
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Countries by Sign Ins | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $Country = principal.location.country_or_region
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Event Count by Log Type by Date | 
    
    
    $log_type = metadata.log_type
    $date = timestamp.get_date(metadata.event_timestamp.seconds, "America/Los_Angeles")
    match:
      $date, $log_type
    outcome:
      $event_count = count_distinct(metadata.id)
    order:
      $event_count desc  
  
Sign Ins by Status | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $Action = security_result.action
    
    match:
      $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 Hostnames by Failed Sign Ins | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "BLOCK"
    
    $Hostname = principal.hostname
    
    match:
      $Hostname
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Src/Dest Talkers Over the Past Day | 
    
    
    metadata.event_type = "NETWORK_CONNECTION"
    $pip = principal.ip
    $tip = target.ip
    match:
      $pip, $tip
    outcome:
      $event_count = count_distinct(metadata.id)
    order:
      $event_count desc
    limit:
        10  
  
Initial Access Sign In Events | 
    
    
    metadata.event_type = "USER_LOGIN"
    strings.coalesce(security_result.attack_details.tactics.name, security_result.detection_fields["Tactic"]) = /Initial Access/ nocase
    
    outcome:
      $Count = count(metadata.id)  
  
Top 10 Users by Sign In Status | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $User = target.user.userid
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
      $Failed_Login_Count = sum(if(security_result.action = "BLOCK", 1, 0))
      $Successful_Login_Count = sum(if(security_result.action = "ALLOW", 1, 0))
    
    order:
      $Count desc
    
    limit:
        10  
  
Login Failure Rate | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    outcome:
      $Total_Logins = count(metadata.id)
      $Failed_Logins = sum(if(security_result.action = "BLOCK", 1, 0))
      $Failure_Rate = math.round(($Failed_Logins / $Total_Logins), 2) * 100  
  
Top 10 Users by Successful Sign Ins | 
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "ALLOW"
    
    $User = target.user.userid
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
## VPN Activity Monitoring

This dashboard provides insights into VPN events as they relate to security.

Geographical Connection SourcesTop 10 Failed VPN Attempts By User and IPVPN Usage TrendsVPN Bandwidth Usage over TimeSource Platform DistributionTop 10 VPN Users by Event CountTop 10 Target IPsActive VPN ConnectionsVPN Connection Success vs. Failure

Chart name | Query example  
---|---  
Geographical Connection Sources | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $location = principal.location.country_or_region
    $location != ""
    match:
    $location
    outcome:
    $event_count = count($location)
    $latitude = max(principal.location.region_coordinates.latitude)
    $longitude = max(principal.location.region_coordinates.longitude)  
  
Top 10 Failed VPN Attempts By User and IP | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $summary = security_result.summary
    ($summary = /fail/ or additional.fields["connection-attempt-status"] = /fail/ or metadata.product_event_type = /fail/)
    $user = principal.user.user_display_name
    $src_ip = principal.ip
    match:
    $user,$src_ip
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit :
    10  
  
VPN Usage Trends | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $date
    outcome:
    $event_count = count(metadata.id)
    order:
    $date asc   
  
VPN Bandwidth Usage over Time | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    $sent_bytes = network.sent_bytes
    $received_bytes = network.received_bytes
    match:
    $date
    outcome:
    $total_sent_bytes = sum($sent_bytes)
    $total_received_bytes = sum($received_bytes)
    $total_bandwidth = $total_sent_bytes + $total_received_bytes
    $total_bandwidth_kb = $total_bandwidth/ 1024
    order:
    $date asc  
  
VPN Usage Trends | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $date
    outcome:
    $event_count = count(metadata.id)
    order:
    $date asc   
  
Source Platform Distribution | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $platform = principal.platform
    match:
      $platform
    outcome:
    $event_count = count(metadata.id)    
  
Top 10 VPN Users by Event Count | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $user = strings.coalesce(principal.user.user_display_name,target.user.user_display_name)
    $user != ""
    match:
    $user
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
Top 10 Target IPs | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $dest_ip = target.ip
    $dest_ip != ""
    match:
    $dest_ip
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
VPN Bandwidth Usage over Time | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    $sent_bytes = network.sent_bytes
    $received_bytes = network.received_bytes
    match:
    $date
    outcome:
    $total_sent_bytes = sum($sent_bytes)
    $total_received_bytes = sum($received_bytes)
    $total_bandwidth = $total_sent_bytes + $total_received_bytes
    $total_bandwidth_kb = $total_bandwidth/ 1024
    order:
    $date asc  
  
Active VPN Connections | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $src_ip = principal.ip
    $dest_ip = target.ip
    $end_time = additional.fields["connection-end-time"]
    $end_time = "NA"
    $user = target.user.user_display_name
    $session_duration = timestamp.diff(metadata.ingested_timestamp.seconds,timestamp.as_unix_seconds(additional.fields["connection-start-time"]))
    $session_duration > 100
    match:
      $user,$src_ip,$dest_ip,$session_duration
    outcome:
    $event_count = count(metadata.id)
    order:
    $session_duration desc,$user asc  
  
Geographical Connection Sources | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $location = principal.location.country_or_region
    $location != ""
    match:
    $location
    outcome:
    $event_count = count($location)
    $latitude = max(principal.location.region_coordinates.latitude)
    $longitude = max(principal.location.region_coordinates.longitude)  
  
Top 10 Failed VPN Attempts By User and IP | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $summary = security_result.summary
    ($summary = /fail/ or additional.fields["connection-attempt-status"] = /fail/ or metadata.product_event_type = /fail/)
    $user = principal.user.user_display_name
    $src_ip = principal.ip
    match:
    $user,$src_ip
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit :
    10  
  
Source Platform Distribution | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $platform = principal.platform
    match:
      $platform
    outcome:
    $event_count = count(metadata.id)    
  
Active VPN Connections | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $src_ip = principal.ip
    $dest_ip = target.ip
    $end_time = additional.fields["connection-end-time"]
    $end_time = "NA"
    $user = target.user.user_display_name
    $session_duration = timestamp.diff(metadata.ingested_timestamp.seconds,timestamp.as_unix_seconds(additional.fields["connection-start-time"]))
    $session_duration > 100
    match:
      $user,$src_ip,$dest_ip,$session_duration
    outcome:
    $event_count = count(metadata.id)
    order:
    $session_duration desc,$user asc  
  
VPN Connection Success vs. Failure | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $summary = strings.coalesce(security_result.summary, metadata.product_event_type, additional.fields["connection-attempt-status"])
    ($summary = /fail/ or $summary = /success/)
    match:
    $summary
    outcome:
    $event_count = count(metadata.id)    
  
VPN Connection Success vs. Failure | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $summary = strings.coalesce(security_result.summary, metadata.product_event_type, additional.fields["connection-attempt-status"])
    ($summary = /fail/ or $summary = /success/)
    match:
    $summary
    outcome:
    $event_count = count(metadata.id)    
  
Top 10 VPN Users by Event Count | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $user = strings.coalesce(principal.user.user_display_name,target.user.user_display_name)
    $user != ""
    match:
    $user
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
Top 10 Target IPs | 
    
    
    $log_type = metadata.log_type
    $log_type = /VPN|Zscaler_ZPA|ZSCALER_DECEPTION|TWINGATE|SYMANTEC_VIP_AUTHHUB/nocase
    $dest_ip = target.ip
    $dest_ip != ""
    match:
    $dest_ip
    outcome:
    $event_count = count(metadata.id)
    order:
    $event_count desc
    limit:
    10  
  
## Web Application Firewall (WAF) Monitoring

This dashboard is designed to monitor and analyze web application firewall activity to enhance security and threat management. It provides real-time insights into web application security by tracking various metrics and events related to WAF operations, helping you effectively manage and respond to potential web-based threats.

Anomalous Traffic DetectionTop 10 WAF Rule HitsTop 10 Source IPsBlocked vs. Allowed RequestsGeolocation of AttacksTop 10 Attack TypesTop 10 URL Hits

Chart name | Query example  
---|---  
Anomalous Traffic Detection | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/ nocase
    $Action = security_result.action
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $date
    
    outcome:
    
    $count = count(metadata.id)
      
  
Top 10 WAF Rule Hits | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/ nocase
    $Rule_Name = security_result.rule_name
    
    match:
    $Rule_Name, $Log_Type
    
    outcome:
    
    $count = count(metadata.id)
    
    order:
    $count desc
    
    limit:
    10  
  
Top 10 Source IPs | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/ nocase
    $Source_IP = principal.ip
    $Geolocation = principal.location.country_or_region
    
    match:
    $Source_IP, $Geolocation
    
    outcome:
    
    $Action = array_distinct(security_result.action)
    $count = count(metadata.id)
    
    Order:
    $count desc
    
    limit:
    10
      
  
Blocked vs. Allowed Requests | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/ nocase
    $Action = security_result.action
    
    match:
    $Action
    
    outcome:
    
    $count = count(metadata.id)
      
  
Blocked vs. Allowed Requests | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/
    $Action = security_result.action
    
    match:
    $Action
    
    outcome:
    
    $count = count(metadata.id)
      
  
Geolocation of Attacks | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/
    $Geolocation = principal.location.country_or_region
    
    match:
    $Geolocation
    
    outcome:
    $Latitude = max(principal.location.region_latitude)
    $Longitude = max(principal.location.region_longitude)
    
    $count = count(metadata.id)
      
  
Top 10 Source IPs | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/
    $Source_IP = principal.ip
    $Source_IP != ""
    $Geolocation = principal.location.country_or_region
    
    match:
    $Source_IP, $Geolocation
    
    outcome:
    
    $Action = array_distinct(security_result.action)
    $count = count(metadata.id)
    
    Order:
    $count desc
    
    limit:
    10
      
  
Top 10 Attack Types | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/ nocase
    $Description = security_result.description
    
    match:
    $Description, $Log_Type
    
    outcome:
    
    $Action = array_distinct(security_result.action)
    $count = count(metadata.id)
    
    order:
    $count desc
    
    limit:
    10  
  
Anomalous Traffic Detection | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/
    $Action = security_result.action
    $date = timestamp.get_date(metadata.event_timestamp.seconds)
    match:
    $date
    
    outcome:
    
    $count = count(metadata.id)
      
  
Top 10 Attack Types | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/
    $Description = security_result.description
    $Description != ""
    
    match:
    $Description, $Log_Type
    
    outcome:
    
    $Action = array_distinct(security_result.action)
    $count = count(metadata.id)
    
    order:
    $count desc
    
    limit:
    10  
  
Geolocation of Attacks | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/ nocase
    $Geolocation = principal.location.country_or_region
    
    match:
    $Geolocation
    
    outcome:
    $Latitude = max(principal.location.region_latitude)
    $Longitude = max(principal.location.region_longitude)
    
    $count = count(metadata.id)
      
  
Top 10 URL Hits | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/
    $URL = target.url
    $URL != ""
    
    match:
    $URL, $Log_Type
    
    outcome:
    
    $count = count(metadata.id)
    
    order:
    $count desc
    
    limit:
    10  
  
Top 10 WAF Rule Hits | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/
    $Rule_Name = security_result.rule_name
    $Rule_Name != ""
    
    match:
    $Rule_Name, $Log_Type
    
    outcome:
    
    $count = count(metadata.id)
    
    order:
    $count desc
    
    limit:
    10  
  
Top 10 URL Hits | 
    
    
    $Log_Type = metadata.log_type
    $Log_Type = /WAF/ nocase
    $URL = target.url
    
    match:
    $URL, $Log_Type
    
    outcome:
    
    $count = count(metadata.id)
    
    order:
    $count desc
    
    limit:
    10  
  
## Web Center Overview

This dashboard monitors and analyzes web traffic patterns and user activity across the network. It provides insights into the top user agents, sources, destinations, and URLs, helping you track usage and detect potential risks.

Weak TLS Version Usage Over TimeTLS Cipher DistributionTop 10 URLsLeast Common URLsUnencrypted Communication DistributionEvents Over Time By HTTP MethodTop 10 Destination IPsTop 10 Web CategoriesTop 10 Users by HTTP MethodTop 10 HTTP User AgentsTop 10 Source IPsTop 10 Users by Downloaded BytesTop 10 UsersTop 10 Countries by Blocked URLEvents Over Time By HTTP Response CodeBlocked URL Based on LocationTop 10 Blocked URLsWeb Failure RateBlocked HTTP Events by LocationTop 10 Principal IPsTop 10 Users by Uploaded Bytes

Chart name | Query example  
---|---  
Weak TLS Version Usage Over Time | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    network.tls.version = /^tls/ nocase
    
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    $TLS_Version = network.tls.version
    $TLS_Version != ""
    
    match:
      $Date, $TLS_Version
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
TLS Cipher Distribution | 
    
    
    network.tls.cipher = /^tls/ nocase
    
    $TLS = network.tls.cipher
    $TLS != ""
    
    match:
      $TLS
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Top 10 URLs | 
    
    
    $event.metadata.event_type = "NETWORK_HTTP"
    
    $URL = $event.target.url
    $URL != ""
    
    match:
      $URL
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Least Common URLs | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    
    $URL = target.url
    $URL != ""
    
    match:
      $URL
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count asc
    
    limit:
        10  
  
Unencrypted Communication Distribution | 
    
    
    metadata.event_type = "NETWORK_UNCATEGORIZED"
    or metadata.event_type = "NETWORK_FLOW"
    or metadata.event_type = "NETWORK_CONNECTION"
    or metadata.event_type = "NETWORK_FTP"
    or metadata.event_type = "NETWORK_DHCP"
    or metadata.event_type = "NETWORK_DNS"
    or metadata.event_type = "NETWORK_HTTP"
    or metadata.event_type = "NETWORK_SMTP"
    network.application_protocol = "HTTP"
    or network.application_protocol = "SMTP"
    or network.application_protocol = "DNS"
    
    $Protocol = network.application_protocol
    
    match:
      $Protocol
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Events Over Time By HTTP Method | 
    
    
    $event.metadata.event_type = "NETWORK_HTTP"
    
    $Log_Type = $event.metadata.log_type
    $Event_Type = $event.metadata.event_type
    $HTTP_Method = $event.network.http.method
    $HTTP_Method != ""
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type, $Event_Type, $HTTP_Method
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Top 10 Destination IPs | 
    
    
    $event.metadata.event_type = "NETWORK_HTTP"
    
    $Destination_IP = $event.target.ip
    
    match:
      $Destination_IP
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Top 10 Web Categories | 
    
    
    $event.metadata.event_type = "NETWORK_HTTP"
    
    $Log_Type = $event.metadata.log_type
    $Event_Type = $event.metadata.event_type
    $Categories = $event.security_result.category_details
    $Categories != ""
    
    match:
      $Event_Type, $Log_Type, $Categories
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Top 10 Users by HTTP Method | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    
    $User = principal.user.userid
    $User != ""
    $HTTP_Method = network.http.method
    $HTTP_Method = /PUT|POST|DELETE/ nocase
    
    match:
      $User, $HTTP_Method
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 HTTP User Agents | 
    
    
    $event.metadata.event_type = "NETWORK_HTTP"
    
    $User_Agent = $event.network.http.user_agent
    $User_Agent != ""
    
    match:
      $User_Agent
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10  
  
Top 10 Source IPs | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    
    $Source_IP = principal.ip
    
    match:
      $Source_IP
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Events Over Time By HTTP Method | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    
    $Log_Type = metadata.log_type
    $Event_Type = metadata.event_type
    $HTTP_Method = network.http.method
    $HTTP_Method != ""
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Log_Type, $Event_Type, $HTTP_Method
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Users by Downloaded Bytes | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    network.http.method = "GET"
    
    $User = principal.user.userid
    $User != ""
    
    match:
      $User
    
    outcome:
      $Count = sum(network.received_bytes)
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 Users | 
    
    
    $event.metadata.event_type = "NETWORK_HTTP"
    
    $User = $event.principal.user.userid
    $User != ""
    
    match:
      $User
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Least Common URLs | 
    
    
    $event.metadata.event_type = "NETWORK_HTTP"
    
    $URL = $event.target.url
    $URL != ""
    
    match:
      $URL
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count asc
    limit:
        10   
  
Top 10 URLs | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    
    $URL = target.url
    $URL != ""
    
    match:
      $URL
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 Destination IPs | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    
    $Destination_IP = target.ip
    
    match:
      $Destination_IP
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 HTTP User Agents | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    
    $User_Agent = network.http.user_agent
    $User_Agent != ""
    
    match:
      $User_Agent
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Top 10 Countries by Blocked URL | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    security_result.action = "BLOCK"
    
    $URL = target.url
    $URL != ""
    $Country = target.location.country_or_region
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10  
  
Events Over Time By HTTP Response Code | 
    
    
    $event.metadata.event_type = "NETWORK_HTTP"
    
    $Response_Code = strings.concat($event.network.http.response_code, " ")
    $Date = timestamp.get_date($event.metadata.event_timestamp.seconds)
    
    match:
      $Date, $Response_Code
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Date asc  
  
Blocked URL Based on Location | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    security_result.action = "BLOCK"
    
    $URL = target.url
    $URL != ""
    
    $Latitude = target.location.region_latitude
    $Longitude = target.location.region_longitude
    
    match:
      $Latitude, $Longitude
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc   
  
Top 10 Blocked URLs | 
    
    
    $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.action = "BLOCK"
    
    $Blocked_URL = $event.target.url
    
    match:
      $Blocked_URL
    outcome:
      $Event_Count = count($event.metadata.id)
    order:
      $Event_Count desc
    limit:
        10  
  
Events Over Time By HTTP Response Code | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    
    $Response_Code = strings.concat(network.http.response_code, " ")
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Response_Code
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Top 10 Blocked URLs | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    security_result.action = "BLOCK"
    
    $Blocked_URL = target.url
    
    match:
      $Blocked_URL
    
    outcome:
      $Event_Count = count(metadata.id)
    
    order:
      $Event_Count desc
    
    limit:
        10  
  
Web Failure Rate | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    
    $Response_Code = strings.concat(network.http.response_code, " ")
    
    outcome:
      $Total_Count = count(metadata.id)
      $Failure_Count = sum(if($Response_Code = /^(4|5)/, 1, 0))
      $Failure_Rate = math.round($Failure_Count / $Total_Count, 2) * 100  
  
Top 10 Web Categories | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    
    $Log_Type = metadata.log_type
    $Event_Type = metadata.event_type
    $Categories = security_result.category_details
    $Categories != ""
    
    match:
      $Event_Type, $Log_Type, $Categories
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Blocked HTTP Events by Location | 
    
    
    $event.metadata.event_type = "NETWORK_HTTP"
    $event.security_result.action = "BLOCK"
    
    $URL = $event.target.url
    $URL != ""
    
    $Latitude = $event.target.location.region_latitude
    $Longitude = $event.target.location.region_longitude
    
    match:
      $Latitude, $Longitude
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc   
  
Top 10 Principal IPs | 
    
    
    $event.metadata.event_type = "NETWORK_HTTP"
    
    $Source_IP = $event.principal.ip
    
    match:
      $Source_IP
    outcome:
      $Count = count($event.metadata.id)
    order:
      $Count desc
    limit:
        10   
  
Top 10 Users | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    
    $User = principal.user.userid
    $User != ""
    
    match:
      $User
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10   
  
Top 10 Users by Uploaded Bytes | 
    
    
    metadata.event_type = "NETWORK_HTTP"
    network.http.method = "POST"
    
    $User = principal.user.userid
    $User != ""
    
    match:
      $User
    
    outcome:
      $Count = sum(network.sent_bytes)
    
    order:
      $Count desc
    
    limit:
        10   
  
## Windows Security Overview

This dashboard analyzes user and system activities such as account management, login patterns, threat details, and configuration changes to provide a comprehensive view of Windows security posture and enhance threat detection and response capabilities.

**Note:** Apply filters to display relevant results on the dashboard.

Recent Scheduled Tasks CreatedSuccessful vs Failed Logon Over TimeUser Account DeletionTop 10 User Accounts by Logon FailuresDistribution of Alerts by Host (Defender ATP)Windows Defender ATP ThreatsThreat Action DistributionSecurity Event Log ClearedEndpoint Protection Status Over Time (Defender Antivirus)Account Creations & Deletions Over TimeRecent Audit Policy ChangesThreat Detections Over TimeAccount Lockout SummaryPrivileged Group ModificationsRecent Services InstalledThreat Detection SummaryTop 10 Threat File pathEndpoint Protection Summary (Defender Antivirus)Logon Type DistributionTop Processes Spawned on Servers (Windows Sysmon)Distinct Remote Logon CountriesAntivirus Version Distribution (Defender Antivirus)User Account Creation

Chart name | Query example  
---|---  
Recent Scheduled Tasks Created | 
    
    
    metadata.product_event_type = "4698"
    metadata.event_type = "SCHEDULED_TASK_CREATION"
    
    $Description = strings.coalesce(metadata.description,security_result.description,security_result.summary)
    $Event_Type = metadata.event_type
    $Source_Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Source_User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses )
    $Severity = security_result.severity
    
    match:
      $Source_User, $Source_Hostname, $Description ,$Source_IP , $Event_Type, $Severity
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order :
      $Date desc, $Count desc  
  
Successful vs Failed Logon Over Time | 
    
    
    (metadata.product_event_type = "4625" OR metadata.product_event_type = "4624")
    
    $Action = security_result.action
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Action, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    Order:
      $Date asc
    
      
  
User Account Deletion | 
    
    
    (metadata.event_type = "USER_DELETION" OR metadata.product_event_type = "4726")
    
    $Action = security_result.action
    $Source_IP = strings.coalesce(principal.ip,principal.asset.ip)
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname, principal.asset.asset_id,intermediary.hostname)
    $Source_User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Target_User = strings.coalesce(target.user.userid, target.user.user_display_name, target.user.email_addresses)
    
    match:
      $Source_IP, $Hostname, $Source_User, $Target_User,$Action
    
    outcome :
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Date desc   
  
Top 10 User Accounts by Logon Failures | 
    
    
    metadata.product_event_type = "4625"
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, intermediary.hostname, target.hostname, target.asset.hostname)
    
     match:
      $User, $Hostname
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
      
  
Distribution of Alerts by Host (Defender ATP) | 
    
    
    metadata.product_event_type = "DeviceAlertEvents"
    
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    
    match:
       $Hostname
    
    outcome:
      $Critical = sum(if(security_result.severity = "CRITICAL", 1, 0))
      $High = sum(if(security_result.severity = "HIGH", 1, 0))
      $Medium = sum(if(security_result.severity = "MEDIUM", 1, 0))
      $Low = sum(if(security_result.severity = "LOW", 1, 0))
      $Information = sum(if(security_result.severity = "INFORMATIONAL", 1, 0))
      $Error = sum(if(security_result.severity = "ERROR", 1, 0))
      $Unknown_Severity = sum(if(security_result.severity = "UNKNOWN_SEVERITY", 1, 0))
      $Count = count(security_result.severity)
    
    order :
      $Count desc
      
  
Windows Defender ATP Threats | 
    
    
    metadata.product_event_type = "DeviceAlertEvents"
    
    $Threat_Name = security_result.threat_name
    $Threat_Category = security_result.category_details
    $Threat_Summary = security_result.summary
    $Threat_Severity = security_result.severity
    $Threat_Action = security_result.action
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    $Threat_Name != ""
    
    match:
      $Threat_Name, $Threat_Category, $Threat_Severity, $Threat_Action, $Hostname, $Threat_Summary
    
    outcome:
      $Count = count(metadata.id)
    
    order :
      $Count desc
      
  
Threat Action Distribution | 
    
    
    security_result.threat_name != ""
    $Action = security_result.action
    
    match:
      $Action
    
    outcome:
      $Count = count(metadata.id)  
  
Security Event Log Cleared | 
    
    
    (metadata.product_event_type = "104" OR metadata.product_event_type = "1102" )
    
    $Description = strings.coalesce(metadata.description,security_result.description,security_result.summary)
    $Source_Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Severity = security_result.severity
    
    match:
      $Source_Hostname, $Description, $Severity
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order :
      $Count desc  
  
Endpoint Protection Status Over Time (Defender Antivirus) | 
    
    
    (metadata.product_event_type = "MALWAREPROTECTION_RTP_DISABLED" OR metadata.product_event_type = "MALWAREPROTECTION_RTP_ENABLED")
    
    $Event_Type = metadata.product_event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Date, $Event_Type
    
    outcome:
      $Count = count(metadata.id)
    
    order :
      $Date asc  
  
Account Creations & Deletions Over Time | 
    
    
    (metadata.event_type = "USER_CREATION" OR metadata.event_type = "USER_DELETION" OR metadata.product_event_type = "4726" OR metadata.product_event_type = "4720")
    
    $Event_Type = metadata.event_type
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Event_Type, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc
      
  
Recent Audit Policy Changes | 
    
    
    metadata.product_event_type= "4719"
    
    $Description = metadata.description
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Source_Domain = principal.administrative_domain
    $Category = extracted.fields["AuditPolicyChanges"]
    $Changes = extracted.fields["Changes"]
    $Severity = security_result.severity
    
    match:
       $User, $Source_Domain, $Hostname, $Description,$Severity, $Category, $Changes
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
       $Severity desc, $Count desc  
  
Threat Detections Over Time | 
    
    
    $Threat_Name = security_result.threat_name
    $Threat_Name != ""
    $Date = timestamp.get_date(metadata.event_timestamp.seconds)
    
    match:
      $Threat_Name, $Date
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Date asc  
  
Account Lockout Summary | 
    
    
    metadata.product_event_type = "4740"
    
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses, target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    
    match:
      $User, $Hostname
    
    outcome:
    
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds))
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Privileged Group Modifications | 
    
    
    (metadata.product_event_type = "4728" OR metadata.product_event_type = "4729" OR metadata.product_event_type = "4730" OR metadata.product_event_type = "4731" OR metadata.product_event_type = "4732" OR metadata.product_event_type = "4733")
    
    $Event_Type = metadata.event_type
    $Description = metadata.description
    $Source_User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Target_User = strings.coalesce(target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Target_Domain_Group = target.group.group_display_name
    $Severity = security_result.severity
    $Summary = additional.fields["Message"]
    
    match:
      $Source_User, $Target_User, $Target_Domain_Group, $Event_Type, $Description, $Severity, $Summary
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Severity desc, $Count desc  
  
Recent Services Installed | 
    
    
    metadata.product_event_type = "7045"
    
    $Description = metadata.description
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Service_Name = extracted.fields["ServiceName"]
    $Service_Filepath = target.process.file.full_path
    $Service_Account = extracted.fields["ServiceAccount"]
    $Service_Type = additional.fields["ServiceType"]
    $Service_StartType = extracted.fields["ServiceStartType"]
    $Severity = security_result.severity
    
    match:
      $User, $Hostname, $Description, $Service_Name, $Service_Filepath, $Service_Account, $Service_Type, $Service_StartType, $Severity
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Severity desc, $Count desc  
  
Threat Detection Summary | 
    
    
    $Threat_Name = security_result.threat_name
    $Threat_Name != ""
    $Log_Type = metadata.log_type
    $Event_Type = metadata.product_event_type
    $Action = security_result.action
    $Severity = security_result.severity
    $Description = strings.coalesce(metadata.description, security_result.description, security_result.summary)
    $Source_Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $File_Path = strings.coalesce(target.file.full_path, target.registry.registry_key, principal.process.file.full_path)
    
    match:
      $Log_Type, $Description, $Threat_Name, $Event_Type, $Source_Hostname, $File_Path, $Action, $Severity
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Date desc,$Count desc
    
      
  
Top 10 Threat File path | 
    
    
    security_result.action = "ALLOW" OR security_result.action = "ALLOW_WITH_MODIFICATION" OR security_result.action = "UNKNOWN_ACTION"
    security_result.threat_name != ""
    
    $Severity = security_result.severity
    $File_Path = strings.coalesce(target.file.full_path, target.registry.registry_key, principal.process.file.full_path)
    
    match:
      $File_Path, $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
      
  
Endpoint Protection Summary (Defender Antivirus) | 
    
    
    (metadata.product_event_type = "MALWAREPROTECTION_RTP_DISABLED" OR metadata.product_event_type = "MALWAREPROTECTION_RTP_ENABLED")
    
    $Description = strings.coalesce(metadata.description, security_result.description, security_result.summary)
    $Severity = security_result.severity
    $Action = security_result.action
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname, target.hostname, target.asset.hostname)
    $Source_User = strings.coalesce(principal.user.user_display_name, principal.user.userid, principal.user.email_addresses)
    $Version = metadata.product_version
    
    match:
      $Description, $Hostname, $Source_User, $Severity, $Action, $Version
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order :
      $Count desc, $Date desc
      
  
Logon Type Distribution | 
    
    
    metadata.product_event_type = "4624"
    
    $Logon_type = extensions.auth.mechanism
    
    match:
      $Logon_type
    
    outcome:
      $Count = count(metadata.id)
    
      
  
Top Processes Spawned on Servers (Windows Sysmon) | 
    
    
    metadata.product_event_type = "1"
    
    $Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Severity = security_result.severity
    $Description = security_result.summary
    $Principal_Process_Path = principal.process.file.full_path
    $Target_Process_Path = target.process.file.full_path
    
    match :
      $Hostname, $User, $Severity, $Principal_Process_Path, $Target_Process_Path
    
    outcome:
    
      $Count = count(metadata.id)
    
    order:
      $Count desc  
  
Distinct Remote Logon Countries | 
    
    
    metadata.event_type = "USER_LOGIN"
    metadata.product_event_type = "4624"
    extensions.auth.mechanism = "REMOTE_INTERACTIVE"
    
    $Logon = extensions.auth.mechanism
    $Logon_type = extensions.auth.auth_details
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip)
    $Source_Hostname = strings.coalesce(principal.hostname, principal.asset.hostname)
    $Source_User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses )
    
    match:
      $Source_User, $Source_IP, $Source_Hostname, $Logon, $Logon_type
    
    outcome:
      $Country = array_distinct(principal.ip_geo_artifact.location.country_or_region)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
      $Count = count(metadata.id)
    
    order:
      $Date desc  
  
Antivirus Version Distribution (Defender Antivirus) | 
    
    
    $Anti_Virus_Version = metadata.product_version
    
    match:
      $Anti_Virus_Version
    
    outcome:
      $Count = count_distinct(principal.hostname)
    
    limit:
        50  
  
User Account Creation | 
    
    
    (metadata.event_type = "USER_CREATION" OR metadata.product_event_type = "4720")
    
    $Source_IP = strings.coalesce(principal.ip,principal.asset.ip)
    $Hostname = strings.coalesce(principal.hostname,principal.asset.hostname, principal.asset.asset_id,intermediary.hostname)
    $Source_User = strings.coalesce(principal.user.userid, principal.user.user_display_name, principal.user.email_addresses)
    $Target_User = strings.coalesce(target.user.userid, target.user.user_display_name, target.user.email_addresses)
    $Action = security_result.action
    
    match:
      $Source_IP, $Hostname, $Source_User, $Target_User,$Action
    
    outcome :
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order:
      $Date desc   
  
## Wireless Network Security

This dashboard offers insights into network activity and security, including authentication distributions, failed logins, rogue AP detections, and client connection behavior. It helps track security events by severity, identify suspicious ids, and optimize network performance for proactive risk management.

**Note:** Apply filters to display relevant results on the dashboard.

Rogue Access Points DetectionsTop 10 Authentication Types by ActionTop 10 SSIDs by Source MAC(Cisco Meraki)Top 10 Access Point by Source MACTop 10 Event Types by ActionTop 10 MAC Address by Failed AuthenticationRecent Failed Authentication (Last 24 Hours)Total Source DevicesTop 10 DescriptionsTop 10 Client IPs Detected on Rogue Access PointsAuthentication Type DistributionAd-Hoc Network Activity Detected (CISCO MERAKI)Suspicious Wireless ActivitiesSSIDs by Failed Authentications(Cisco Meraki)Severity DistributionRogue Access Point Detections CountSource Geolocation Overview

Chart name | Query example  
---|---  
Rogue Access Points Detections | 
    
    
    $Rogue = strings.coalesce(
                           if (extracted.fields["description"] = /Rogue|AP Detection|Spoof/ nocase, extracted.fields["description"], ""),
                           if (security_result.description = /Rogue|AP Detection|Spoof/ nocase, security_result.description, ""),
                           if (security_result.summary = /Rogue|AP Detection|Spoof/ nocase, security_result.summary, ""),
                           if (metadata.description = /Rogue|AP Detection|Spoof/ nocase, metadata.description,""))
    $Rogue != ""
    $Source_MAC = strings.coalesce(principal.mac, principal.asset.mac)
    $ID = strings.coalesce(extracted.fields["ssid"], principal.resource.name)
    $Description = strings.coalesce(metadata.description, security_result.summary)
    $Source_IP= strings.coalesce(principal.ip, principal.asset.ip,extracted.fields["clientIp"])
    $Log_Source = metadata.log_type
    $Severity = security_result.severity
    $Action = security_result.action
    $Target_MAC = strings.coalesce(target.mac, target.asset.mac)
    
    match:
       $Log_Source, $Description,$Source_MAC, $Source_IP, $ID, $Target_MAC,$Severity,$Action
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order :
      $Severity desc,$Date desc
      
  
Top 10 Authentication Types by Action | 
    
    
    metadata.event_type = "USER_LOGIN"
    
    $Logon_type = extensions.auth.type
    $Action = security_result.action
    
    match:
      $Action,$Logon_type
    
    outcome:
      $Count = count(metadata.id)
    
    order :
      $Count desc
    
    limit:
        10
      
  
Top 10 SSIDs by Source MAC(Cisco Meraki) | 
    
    
    $SSID = extracted.fields["ssid"]
    $Log_Type = metadata.log_type
    $SSID != ""
    $Action = security_result.action
    
    match:
       $SSID, $Action
    
    outcome:
      $Count = count_distinct(strings.coalesce(principal.mac, principal.asset.mac))
    
    order:
       $Count desc
    
    limit:
       10
         
  
Top 10 Access Point by Source MAC | 
    
    
     $Access_Point = strings.coalesce(target.hostname, target.asset.hostname, principal.user.company_name, observer.hostname,intermediary.hostname)
     $Log_Type = metadata.log_type
    
    match:
      $Access_Point, $Log_Type
    
    outcome:
      $Count = count_distinct(strings.coalesce(principal.mac, principal.asset.mac))
    
    order :
       $Count desc
    
    limit :
        10
      
  
Top 10 Event Types by Action | 
    
    
    $Event_Type = metadata.event_type
    $Action = security_result.action
    
    match:
      $Event_Type,$Action
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
      
  
Top 10 MAC Address by Failed Authentication | 
    
    
    $Authentication_Failed = strings.coalesce(
                           if (extracted.fields["description"] = /authentication failed/ nocase, extracted.fields["description"], ""),
                           if (security_result.description = /failed to connect/ nocase, security_result.description, ""),
                           if (security_result.summary = /Failed Authentication|authentication failed/ nocase, security_result.summary, ""),
                           if (metadata.description = /Authentication failed|verification failed/ nocase, metadata.description,""))
    ($Authentication_Failed != "" OR (metadata.event_type= "USER_LOGIN"  AND  security_result.action ="BLOCK"))
    $MAC_Address = strings.coalesce(principal.mac, principal.asset.mac, target.mac, target.asset.mac)
    $Severity = security_result.severity
    
    match:
      $MAC_Address, $Severity
    
    outcome:
      $Count = count(metadata.id)
    
    order:
      $Count desc
    
    limit:
        10
      
  
Recent Failed Authentication (Last 24 Hours) | 
    
    
    $Authentication_Failed = strings.coalesce(
                           if (extracted.fields["description"] = /authentication failed/ nocase, extracted.fields["description"], ""),
                           if (security_result.description = /failed to connect/ nocase, security_result.description, ""),
                           if (security_result.summary = /Failed Authentication|authentication failed/ nocase, security_result.summary, ""),
                           if (metadata.description = /Authentication failed|verification failed/ nocase, metadata.description, ""))
    ($Authentication_Failed != "" OR (metadata.event_type= "USER_LOGIN"  AND  security_result.action ="BLOCK"))
    $Log_Source = metadata.log_type
    $Source_MAC = strings.coalesce(principal.mac, principal.asset.mac)
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip,extracted.fields["clientIp"])
    $Severity = security_result.severity
    $Action = security_result.action
    $Security_Event_Type = metadata.product_event_type
    $Target_MAC = strings.coalesce(target.mac, target.asset.mac)
    $Description = strings.coalesce(metadata.description,extracted.fields["description"], security_result.description,security_result.summary)
     $Access_Point = strings.coalesce(target.hostname, target.asset.hostname, principal.user.company_name, observer.hostname,intermediary.hostname)
    
    match:
      $Log_Source,$Description, $Source_MAC, $Source_IP, $Access_Point, $Target_MAC, $Action, $Severity
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order :
      $Date desc, $Severity desc
    
      
  
Total Source Devices | 
    
    
    outcome:
      $Count = count_distinct(strings.coalesce(principal.mac, principal.asset.mac))
        
  
Top 10 Descriptions | 
    
    
    $Description = strings.coalesce(metadata.description,security_result.description,security_result.summary,extracted.fields["description"])
    $Log_Type = metadata.log_type
    $Description != ""
    
    match:
      $Log_Type, $Description
    
    outcome :
      $Count = count(metadata.id)
    
    order :
      $Count desc
    
    limit:
        10
      
  
Top 10 Client IPs Detected on Rogue Access Points | 
    
    
     $Rogue = strings.coalesce(
                           if (extracted.fields["description"] = /Rogue|AP Detection|Spoof/ nocase, extracted.fields["description"], ""),
                           if (security_result.description = /Rogue|AP Detection|Spoof/ nocase, security_result.description, ""),
                           if (security_result.summary = /Rogue|AP Detection|Spoof/ nocase, security_result.summary, ""),
                           if (metadata.description = /Rogue|AP Detection|Spoof/ nocase, metadata.description,""))
    $Rogue != ""
    $Client_IP = strings.coalesce(principal.ip,principal.asset.ip,extracted.fields["clientIp"])
    $Action = security_result.action
    
    match:
       $Client_IP, $Action
    
    outcome:
      $Count = count(metadata.id)
    
    order :
      $Count desc
    
    limit :
        10
      
  
Authentication Type Distribution | 
    
    
    $Logon_type = extensions.auth.type
    
    match:
      $Logon_type
    
    outcome:
      $Count = count(metadata.id)
      
  
Ad-Hoc Network Activity Detected (CISCO MERAKI) | 
    
    
    extracted.fields["type"] = "adhoc_network_detected"
    
    $Detection_Type = extracted.fields["type"]
    $SSID = extracted.fields["ssid"]
    $SSID != ""
    $Source_IP = extracted.fields["clientIp"]
    $Source_MAC = strings.coalesce(principal.mac, principal.asset.mac)
    $Category = security_result.category
    $Security_Description = security_result.description
    
    match:
      $Security_Description, $Detection_Type, $SSID, $Source_MAC, $Source_IP, $Category
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order :
      $Count desc
    
      
  
Suspicious Wireless Activities | 
    
    
    (security_result.category = "NETWORK_MALICIOUS" OR security_result.category = "NETWORK_SUSPICIOUS" OR security_result.category = "NETWORK_CATEGORIZED_CONTENT" OR security_result.category = "NETWORK_COMMAND_AND_CONTROL" OR security_result.category = "NETWORK_DENIAL_OF_SERVICE" OR security_result.category = "NETWORK_RECON" OR  security_result.category = "AUTH_VIOLATION")
    
    $Log_Source = metadata.log_type
    $Source_MAC = strings.coalesce(principal.mac, principal.asset.mac)
    $ID = strings.coalesce(extracted.fields["ssid"], principal.resource.name)
    $Source_IP = strings.coalesce(principal.ip, principal.asset.ip,extracted.fields["clientIp"])
    $Severity = security_result.severity
    $Action = security_result.action
    $Target_MAC = strings.coalesce(target.mac, target.asset.mac)
    $Description = strings.coalesce(metadata.description,extracted.fields["description"], security_result.description,security_result.summary)
    
    match:
      $Log_Source, $Description, $Source_IP, $Source_MAC, $ID,  $Target_MAC , $Severity, $Action
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order :
       $Severity desc,$Date desc  
  
SSIDs by Failed Authentications(Cisco Meraki) | 
    
    
    $Authentication_Failed = strings.coalesce(
                           if (extracted.fields["description"] = /authentication failed/ nocase, extracted.fields["description"], ""),
                           if (security_result.description = /failed to connect/ nocase,security_result.description, ""),
                           if (security_result.summary = /Failed Authentication/ nocase, security_result.summary, ""),
                           if (metadata.description = /Authentication failed|verification failed/ nocase, metadata.description,""))
    ($Authentication_Failed != "" OR (metadata.event_type= "USER_LOGIN"  AND  security_result.action ="BLOCK"))
    $SSID = extracted.fields["ssid"]
    $Source_IP = extracted.fields["clientIp"]
    $SSID != ""
    $Source_MAC = strings.coalesce(principal.mac, principal.asset.mac)
    $Access_Point = strings.coalesce(target.hostname, target.asset.hostname, principal.user.company_name, observer.hostname,intermediary.hostname)
    $AP_Model = target.asset.hardware.model
    $Target_Url = target.url
    $Source_Hostname = principal.hostname
    $Resource_Name = principal.resource.name
    
    match:
       $SSID, $Source_MAC, $Source_IP, $Access_Point, $AP_Model, $Target_Url, $Source_Hostname, $Resource_Name
    
    outcome:
      $Count = count(metadata.id)
      $Date = timestamp.get_timestamp(max(metadata.event_timestamp.seconds), "%F %T")
    
    order :
      $Count desc
    
      
  
Severity Distribution | 
    
    
    $Severity = security_result.severity
    
    match:
      $Severity
    
    outcome:
      $Count = count(metadata.id)
      
  
Rogue Access Point Detections Count | 
    
    
    $Rogue = strings.coalesce(
                           if (extracted.fields["description"] = /Rogue|AP Detection|Spoof/ nocase, extracted.fields["description"], ""),
                           if (security_result.description = /Rogue|AP Detection|Spoof/ nocase, security_result.description, ""),
                           if (security_result.summary = /Rogue|AP Detection|Spoof/ nocase, security_result.summary, ""),
                           if (metadata.description = /Rogue|AP Detection|Spoof/ nocase, metadata.description,""))
    $Rogue != ""
    
    outcome:
      $Count = count_distinct(strings.coalesce(target.hostname, target.asset.hostname, principal.user.company_name, observer.hostname,intermediary.hostname))  
  
Source Geolocation Overview | 
    
    
    $Country = strings.coalesce(principal.location.country_or_region, principal.ip_geo_artifact.location.country_or_region)
    $Country != ""
    
    match:
      $Country
    
    outcome:
      $Count = count(metadata.id)
      $Latitude = max(principal.location.region_latitude)
      $Longitude = max(principal.location.region_longitude)
    
    order:
      $Count desc
      
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
