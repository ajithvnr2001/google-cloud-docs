---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection/
title: Use Event Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:50.521214+00:00
---

# Use Event Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Event Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page shows you how to review Event Threat Detection findings in the Google Cloud console and includes examples of Event Threat Detection findings.

Event Threat Detection is a built-in service that monitors the Cloud Logging logging streams for your organization or projects and detects threats in near-real time. If you activate Security Command Center at the organization level, Event Threat Detection can also monitor your organization's Google Workspace logging streams. To learn more, see [Event Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).

## Enable or disable Event Threat Detection

By default, Event Threat Detection is enabled. For general information about how to enable or disable a built-in service or its modules, see [Configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center).

## Reviewing findings

To view Event Threat Detection findings, the service must be enabled in Security Command Center [Services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) settings. After you enable Event Threat Detection, Event Threat Detection generates findings by scanning specific logs. Some of the logs Event Threat Detection can scan are turned off by default, so you might need to turn them on.

For more information about the built-in detection rules that Event Threat Detection uses and the logs that Event Threat Detection scans, see the following topics:

  * [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules)
  * [Log types and activation requirements](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#log_types)



You can view Event Threat Detection findings in Security Command Center. If you [configured Continuous Exports](https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging) to write logs, you can also view findings in Cloud Logging. Continuous Exports to Cloud Logging are only available when you activate Security Command Center at the organization level. To generate a finding and verify your configuration, you can intentionally trigger a detector and [test Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-test-event-threat-detection).

Event Threat Detection activation occurs within seconds. Detection latencies are generally less than 15 minutes from the time a log is written to when a finding is available in Security Command Center. For more information on latency, see [Security Command Center latency overview](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview).

### Reviewing findings in Security Command Center

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

Use the following procedure to review findings in the Google Cloud console:

  1. In the Google Cloud console, go to the Security Command Center **Findings** page. 

[ Go to Findings](https://console.cloud.google.com/security/command-center/findings)

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for your organization, you must access the page using the jurisdictional console. For more information, see [Use the console with data residency enabled](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#console-jconsole).

  2. If necessary, select your Google Cloud project or organization.

  3. In the **Quick filters** section, in the **Source display name** subsection, select one or both of the following:

     * **Event Threat Detection** : to filter for findings generated by [built-in Event Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules)
     * **Event Threat Detection Custom Modules** : to filter for findings generated by [custom modules for Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview)

The table is populated with Event Threat Detection findings.

  4. To view details of a specific finding, click the finding name under **`Category`**. The finding details pane expands to display information including the following:

     * When the event occurred
     * The source of the finding data
     * The detection severity, for example **High**
     * The actions taken, like adding an Identity and Access Management (IAM) role to a Gmail user
     * The user who took the action, listed next to **Principal email**
  5. To display all findings that were caused by the same user's actions:

     1. On the finding details pane, copy the email address next to **Principal email**.
     2. Close the pane.
     3. In query editor, enter the following query:
            
            access.principal_email="USER_EMAIL"
            

Replace USER_EMAIL with the email address you previously copied.

Security Command Center displays all findings that are associated with actions taken by the user you specified.




### Viewing findings in Cloud Logging

If you configure [Continuous Exports](https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging) to write logs, you can view Event Threat Detection findings in Cloud Logging. This feature is only available if you activate Security Command Center Premium tier at the organization level.

To view Event Threat Detection findings in Cloud Logging, do the following:

  1. Go to **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select the Google Cloud project or other Google Cloud resource where you are storing your Event Threat Detection logs.

  3. Use the **Query** pane to build your query in one of the following ways:

     * In the **All resources** list, do the following: 
       1. Select **Threat Detector** to display a list of all the detectors.
       2. To view findings from all detectors, select **all detector_name**. To view findings from a specific detector, select its name.
       3. Click **Apply**. The **Query results** table is updated with the logs you selected.
     * Enter the following query in the query editor and click **Run query** :
           
           resource.type="threat_detector"

The **Query results** table is updated with the logs you selected.

  4. To view a log, select a table row, and then click **Expand nested fields**.




You can create [advanced log queries](https://docs.cloud.google.com/logging/docs/view/advanced-queries) to specify a set of log entries from any number of logs.

## Example finding formats

This section provides links to examples of JSON output for Event Threat Detection findings. You see this output when you [export findings](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#export-console) using the Google Cloud console or [list findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings) using the Security Command Center API or the Google Cloud CLI.

The examples on this page show different types of findings. Each example includes only the fields that are most relevant to that type of finding. For a complete list of fields that are available in a finding, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings) resource.

To see example findings, select one of the following links.

Threat Finding | JSON Example  
---|---  
`Active Scan: Log4j Vulnerable to RCE` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/log4j-active-scan-success#example_json)  
`Brute force SSH` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ssh-brute-force#example_json)  
`Cloud IDS: THREAT_IDENTIFIER` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloud-ids-threat-activity#example_json)  
`Defense Evasion: Breakglass Workload Deployment Created` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/binary-authorization-breakglass-workload-create#example_json)  
`Defense Evasion: Breakglass Workload Deployment Updated` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/binary-authorization-breakglass-workload-update#example_json)  
`Defense Evasion: Folder Level TokenCreator Role Granted to AI Agent` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-folder#example_json)  
`Defense Evasion: Modify VPC Service Control` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/vpcsc-change-reduces-perimeter-protection#example_json)  
`Defense Evasion: Organization Level TokenCreator Role Granted to AI Agent` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-org#example_json)  
`Defense Evasion: Project Level TokenCreator Role Granted to AI Agent` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-project#example_json)  
`Discovery: AI Agent Service Account Self-Investigation` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-iam-anomalous-behavior-service-account-gets-own-iam-policy#example_json)  
`Discovery: AI Agent Unauthorized Service Account API Call` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-unauthorized-service-account-api-call#example_json)  
`Discovery: Can get sensitive Kubernetes object check` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-can-get-sensitive-object#example_json)  
`Discovery: Service Account Self-Investigation` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/iam-anomalous-behavior-service-account-gets-own-iam-policy#example_json)  
`Evasion: Access from Anonymizing Proxy` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-ip-google-proxy-intel#example_json)  
`Execution: Cryptomining Docker Image` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloud-run-cryptomining-docker-images#example_json)  
`Exfiltration: AI Agent Initiated BigQuery Data Exfiltration to External Table` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-exfil#example_json)  
`Exfiltration: AI Agent Initiated BigQuery Data Extraction` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-exfil-to-cloud-storage#example_json)  
`Exfiltration: AI Agent Initiated BigQuery VPC Perimeter Violation` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-vpc-violation#example_json)  
`Exfiltration: AI Agent Initiated CloudSQL Exfiltration to External Bucket` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-cloudsql-exfil-export-external#example_json)  
`Exfiltration: AI Agent Initiated CloudSQL Exfiltration to Public Bucket` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-cloudsql-exfil-export-public#example_json)  
`Exfiltration: BigQuery Data Exfiltration` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/big-query-exfil#example_json)  
`Exfiltration: BigQuery Data Extraction` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/big-query-exfil-to-cloud-storage#example_json)  
`Exfiltration: BigQuery Data to Google Drive` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/big-query-exfil-to-google-drive#example_json)  
`Exfiltration: Cloud SQL Data Exfiltration` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloudsql-exfil-export#example_json)  
`Exfiltration: Cloud SQL Over-Privileged Grant` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloudsql-exfil-user-granted-all-permissions#example_json)  
`Exfiltration: Cloud SQL Restore Backup to External Organization` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloudsql-exfil-restore-backup-to-external-instance#example_json)  
`Impact: Cryptomining Commands` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloud-run-jobs-cryptomining-commands#example_json)  
`Impact: Deleted Google Cloud Backup and DR Backup` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-delete-vault-backup#example_json)  
`Impact: Deleted Google Cloud Backup and DR host` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-hosts-delete-host#example_json)  
`Impact: Deleted Google Cloud Backup and DR plan association` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-delete-backup-plan-association#example_json)  
`Impact: Deleted Google Cloud Backup and DR Vault` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-delete-vault#example_json)  
`Impact: Google Cloud Backup and DR delete policy` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-templates-delete-policy#example_json)  
`Impact: Google Cloud Backup and DR delete profile` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-profiles-delete-profile#example_json)  
`Impact: Google Cloud Backup and DR delete storage pool` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-storage-pools-delete#example_json)  
`Impact: Google Cloud Backup and DR delete template` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-templates-delete-template#example_json)  
`Impact: Google Cloud Backup and DR expire all images` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-expire-images-all#example_json)  
`Impact: Google Cloud Backup and DR expire image` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-expire-image#example_json)  
`Impact: Google Cloud Backup and DR reduced backup expiration` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-reduce-backup-expiration#example_json)  
`Impact: Google Cloud Backup and DR reduced backup frequency` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-reduce-backup-frequency#example_json)  
`Impact: Google Cloud Backup and DR remove appliance` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-appliances-remove-appliance#example_json)  
`Impact: Google Cloud Backup and DR remove plan` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-remove-plan#example_json)  
`Initial Access: Account Disabled Hijacked` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-account-disabled-hijacked#example_json)  
`Initial Access: AI Agent Identity Excessive Permission Denied Actions` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-excessive-failed-attempt#example_json)  
`Initial Access: Database Superuser Writes to User Tables` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloudsql-superuser-writes-to-user-tables#example_json)  
`Initial Access: Disabled Password Leak` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-disabled-password-leak#example_json)  
`Initial Access: Dormant Service Account Action` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/dormant-service-account-used-in-action#example_json)  
`Initial Access: Dormant Service Account Activity in AI Service` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-dormant-service-account-used-in-action#example_json)  
`Initial Access: Dormant Service Account Key Created` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/dormant-service-account-key-created#example_json)  
`Initial Access: Excessive Permission Denied Actions` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/excessive-failed-attempt#example_json)  
`Initial Access: Government Based Attack` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-government-backed-attack#example_json)  
`Initial Access: Leaked Service Account Key Used` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/leaked-sa-key-used#example_json)  
`Initial Access: Log4j Compromise Attempt` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/log4j-compromise-attempt#example_json)  
`Initial Access: Suspicious Login Blocked` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-suspicious-login-blocked#example_json)  
`Lateral Movement: Modified Boot Disk Attached to Instance` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/modify-boot-disk-attach-to-instance#example_json)  
`Malware: bad domain` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-domain-live-google-intel#example_json)  
`Malware: bad IP` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-ip-live-google-intel#example_json)  
`Malware: Cryptomining Bad Domain` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-domain-google-crypto-intel#example_json)  
`Malware: Cryptomining Bad IP` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-ip-google-crypto-intel#example_json)  
`Persistence: GCE Admin Added SSH Key` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gce-admin-add-ssh-key#example_json)  
`Persistence: GCE Admin Added Startup Script` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gce-admin-add-startup-script#example_json)  
`Persistence: IAM Anomalous Grant` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/iam-anomalous-grant#example_json)  
`Persistence: New AI API Method` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-behavior-new-api-method#example_json)  
`Persistence: New API Method` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-behavior-new-api-method#example_json)  
`Persistence: New Geography` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/iam-anomalous-behavior-ip-geolocation#example_json)  
`Persistence: New Geography for AI Service` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-iam-anomalous-behavior-ip-geolocation#example_json)  
`Persistence: New User Agent` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/iam-anomalous-behavior-user-agent#example_json)  
`Persistence: Sensitive AI Permission Added to Custom Role` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/sensitive-ai-permission-added-to-custom-role#example_json)  
`Persistence: Sensitive Role Granted by AI Agent` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/sensitive-role-granted-by-ai-agent#example_json)  
`Persistence: Sensitive Role Granted to External AI Agent` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/external-ai-agent-granted-sensitive-role#example_json)  
`Persistence: SSO Enablement Toggle` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-sso-enablement-toggle#example_json)  
`Persistence: SSO Settings Changed` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-sso-settings-changed#example_json)  
`Persistence: Strong Authentication Disabled` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-strong-authentication-disabled#example_json)  
`Persistence: Two Step Verification Disabled` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-two-step-verification-disabled#example_json)  
`Privilege Escalation: AI Agent Cross-Project Access Token Generation` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-cross-project-access-token#example_json)  
`Privilege Escalation: AI Agent Cross-Project OpenID Token Generation` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-cross-project-openid#example_json)  
`Privilege Escalation: AI Agent Token Generation Using Implicit Delegation` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-implicit-delegation#example_json)  
`Privilege Escalation: AI Agent Token Generation Using signJwt` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-sign-jwt#example_json)  
`Privilege Escalation: AlloyDB Database Superuser Writes to User Tables` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/alloydb-superuser-writes-to-user-tables#example_json)  
`Privilege Escalation: AlloyDB Over-Privileged Grant` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/alloydb-user-granted-all-permissions#example_json)  
`Privilege Escalation: Anomalous Impersonation of Service Account for Admin Activity` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-sa-delegation-impersonation-of-sa-admin-activity#example_json)  
`Privilege Escalation: Anomalous Impersonation of Service Account for AI Admin Activity` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonation-of-sa-admin-activity#example_json)  
`Privilege Escalation: Anomalous Multistep Service Account Delegation for Admin Activity` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-sa-delegation-multistep-admin-activity#example_json)  
`Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Admin Activity` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-multistep-admin-activity#example_json)  
`Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Data Access` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-multistep-data-access#example_json)  
`Privilege Escalation: Anomalous Multistep Service Account Delegation for Data Access` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-sa-delegation-multistep-data-access#example_json)  
`Privilege Escalation: Anomalous Service Account Impersonator for Admin Activity` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-sa-delegation-impersonator-admin-activity#example_json)  
`Privilege Escalation: Anomalous Service Account Impersonator for AI Admin Activity` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonator-admin-activity#example_json)  
`Privilege Escalation: Anomalous Service Account Impersonator for AI Data Access` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonator-data-access#example_json)  
`Privilege Escalation: Anomalous Service Account Impersonator for Data Access` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-sa-delegation-impersonator-data-access#example_json)  
`Privilege Escalation: Changes to sensitive Kubernetes RBAC objects` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-edit-sensitive-rbac-object#example_json)  
`Privilege Escalation: Create Kubernetes CSR for master cert` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-csr-for-master-cert#example_json)  
`Privilege Escalation: Creation of sensitive Kubernetes bindings` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-create-sensitive-binding#example_json)  
`Privilege Escalation: Default Compute Engine Service Account SetIAMPolicy` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloud-run-services-set-iam-policy#example_json)  
`Privilege Escalation: Dormant Service Account Granted Sensitive Role` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/dormant-service-account-added-in-iam-role#example_json)  
`Privilege Escalation: External Member Added To Privileged Group` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/external-member-added-to-privileged-group#example_json)  
`Privilege Escalation: Get Kubernetes CSR with compromised bootstrap credentials` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-get-csr-with-compromised-bootstrap-credentials#example_json)  
`Privilege Escalation: Impersonation Role Granted For Dormant Service Account` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/dormant-service-account-impersonation-role-granted#example_json)  
`Privilege Escalation: Launch of privileged Kubernetes container` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-launch-privileged-container#example_json)  
`Privilege Escalation: Privileged Group Opened To Public` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/privileged-group-opened-to-public#example_json)  
`Privilege Escalation: Sensitive Role Granted To Hybrid Group` | [View JSON Example](https://docs.cloud.google.com/security-command-center/docs/findings/threats/sensitive-role-to-group-with-external-member#example_json)  
  
## What's next

  * Learn more about [how Event Threat Detection works](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).
  * Learn how to [investigate and develop response plans](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats) for threats.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
