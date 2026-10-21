---
url: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-udm-datatable/
title: View UDM and datatable queries \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:02:00.010257+00:00
---

# View UDM and datatable queries  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-udm-datatable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View UDM and datatable queries

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document is for Security Operations Center (SOC) managers and analysts who want to monitor threat landscapes and system health using curated dashboards— predefined dashboards designed for visibility across various security use cases. This document provides a collection of curated dashboards and their underlying queries for the **UDM and datatable** source type.

You can use these queries in the query editor or as a baseline for custom widgets. For information on how to create and manage dashboards, see [Manage dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards).

HIPAA Dashboard

Vulnerabilities by SeverityPermission Changes Over Time by Log TypeMFA Events Over Time by ActionLogin Events Over Time by ActionTop 10 ePHI Hosts by DLP ViolationsEDR Alerts Over Time by SeverityBackup Events Over Time by ActionPassword Changes Over Time by ActionRecent Backup Events (Last 24 Hours)Recent EDR Alerts (Last 24 Hours)Recent User Account Creations (Last 24 Hours)Weak Encrypted Communication Over Time by Log TypeRecent User Change Password (Last 24 Hours)Top 10 SaaS ApplicationsTop 10 Key Operations

Dashboard name  |  Description  |  Chart name  |  Query   
---|---|---|---  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Vulnerabilities by Severity | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Permission Changes Over Time by Log Type | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | MFA Events Over Time by Action | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Login Events Over Time by Action | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Top 10 ePHI Hosts by DLP Violations | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | EDR Alerts Over Time by Severity | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Backup Events Over Time by Action | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Password Changes Over Time by Action | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Recent Backup Events (Last 24 Hours) | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Recent EDR Alerts (Last 24 Hours) | 
    
    
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
      
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Recent User Account Creations (Last 24 Hours) | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Weak Encrypted Communication Over Time by Log Type | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Recent User Change Password (Last 24 Hours) | 
    
    
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
    
      
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Top 10 SaaS Applications | 
    
    
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
  
HIPAA Dashboard | Monitors HIPAA compliance and security metrics in real-time. Provides visibility into PHI access and potential risks to ensure data confidentiality and integrity.   
Note: Requires the `ePHI_assets.Hostname` data table to be created before charts populate. | Top 10 Key Operations | 
    
    
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
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
