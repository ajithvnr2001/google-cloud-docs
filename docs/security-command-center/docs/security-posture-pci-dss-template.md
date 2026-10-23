---
url: https://docs.cloud.google.com/security-command-center/docs/security-posture-pci-dss-template/
title: Predefined posture template for PCI DSS v3.2.1 and v1.0 \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:52.715792+00:00
---

# Predefined posture template for PCI DSS v3.2.1 and v1.0  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/security-posture-pci-dss-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Predefined posture template for PCI DSS v3.2.1 and v1.0 Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes the detective policies that are included in the v1.0 version of the predefined posture template for the [Payment Card Industry Data Security Standard (PCI DSS) version 3.2.1 and version 1.0](https://www.pcisecuritystandards.org/). This template includes a policy set that defines the Security Health Analytics detectors that apply to workloads that must be compliant with the PCI DSS standard.

You can deploy this posture template without making any changes.

## Security Health Analytics detectors

The following table describes the Security Health Analytics detectors that are included in this posture template.

Detector name | Description  
---|---  
`PUBLIC_DATASET` | This detector checks whether a dataset is configured to be open to public access. For more information, see [Dataset vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dataset-findings).  
`NON_ORG_IAM_MEMBER` | This detector checks whether a user isn't using organization credentials.  
`KMS_PROJECT_HAS_OWNER` | This detector checks whether a user has the **Owner** permission on a project that includes keys.  
`AUDIT_LOGGING_DISABLED` | This detector checks whether audit logging is turned off for a resource.  
`SSL_NOT_ENFORCED` | This detector checks whether a Cloud SQL database instance doesn't use SSL for all incoming connections. For more information, see [SQL vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#sql-findings).  
`LOCKED_RETENTION_POLICY_NOT_SET` | This detector checks whether the locked retention policy is set for logs.  
`KMS_KEY_NOT_ROTATED` | This detector checks whether rotation for the Cloud Key Management Service encryption is not turned on.  
`OPEN_SMTP_PORT` | This detector checks whether a firewall has an open SMTP port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`SQL_NO_ROOT_PASSWORD` | This detector checks whether a Cloud SQL database with a public IP address doesn't have a password for the root account.  
`OPEN_LDAP_PORT` | This detector checks whether a firewall has an open LDAP port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OPEN_ORACLEDB_PORT` | This detector checks whether a firewall has an open Oracle database port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OPEN_SSH_PORT` | This detector checks whether a firewall has an open SSH port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`MFA_NOT_ENFORCED` | This detector checks whether a user isn't using 2-step verification.  
`COS_NOT_USED` | This detector checks whether Compute Engine VMs aren't using the Container-Optimized OS. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`HTTP_LOAD_BALANCER` | This detector checks whether Compute Engine instance uses a load balancer that is configured to use a target HTTP proxy instead of a target HTTPS proxy. For more information, see [Compute instance vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#compute-instance-findings).  
`EGRESS_DENY_RULE_NOT_SET` | This detector checks whether an egress deny rule is not set on a firewall. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`PUBLIC_LOG_BUCKET` | This detector checks whether a bucket with a log sink is publicly accessible.  
`OPEN_DIRECTORY_SERVICES_PORT` | This detector checks whether a firewall has an open DIRECTORY_SERVICES port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OPEN_MYSQL_PORT` | This detector checks whether a firewall has an open MySQL port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OPEN_FTP_PORT` | This detector checks whether a firewall has an open FTP port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OPEN_FIREWALL` | This detector checks whether a firewall open to public access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`WEAK_SSL_POLICY` | This detector checks whether an instance has a weak SSL policy.  
`OPEN_POP3_PORT` | This detector checks whether a firewall has an open POP3 port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OPEN_NETBIOS_PORT` | This detector checks whether a firewall has an open NETBIOS port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`FLOW_LOGS_DISABLED` | This detector checks whether flow logs are enabled on the VPC subnetwork.  
`OPEN_MONGODB_PORT` | This detector checks whether a firewall has an open Mongo database port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`MASTER_AUTHORIZED_NETWORKS_DISABLED` | This detector checks whether Control Plane Authorized Networks is not enabled on GKE clusters. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`OPEN_REDIS_PORT` | This detector checks whether a firewall has an open REDIS port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OPEN_DNS_PORT` | This detector checks whether a firewall has an open DNS port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OPEN_TELNET_PORT` | This detector checks whether a firewall has an open TELNET port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OPEN_HTTP_PORT` | This detector checks whether a firewall has an open HTTP port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`CLUSTER_LOGGING_DISABLED` | This detector checks logging isn't enabled for a GKE cluster. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`FULL_API_ACCESS` | This detector checks whether an instance is using a default service account with full access to all Google Cloud APIs.  
`OBJECT_VERSIONING_DISABLED` | This detector checks whether object versioning is enabled on storage buckets with sinks.  
`PUBLIC_IP_ADDRESS` | This detector checks whether an instance has a public IP address.  
`AUTO_UPGRADE_DISABLED` | This detector checks whether a GKE cluster's auto upgrade feature is disabled. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`LEGACY_AUTHORIZATION_ENABLED` | This detector checks whether Legacy Authorization is enabled on GKE clusters. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`CLUSTER_MONITORING_DISABLED` | This detector checks whether monitoring is disabled on GKE clusters. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`OPEN_CISCOSECURE_WEBSM_PORT` | This detector checks whether a firewall has an open CISCOSECURE_WEBSM port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OPEN_RDP_PORT` | This detector checks whether a firewall has an open RDP port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`WEB_UI_ENABLED` | This detector checks whether the GKE web UI is enabled. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`FIREWALL_RULE_LOGGING_DISABLED` | This detector checks whether firewall rule logging is disabled. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OVER_PRIVILEGED_SERVICE_ACCOUNT_USER` | This detector checks whether a user has service account roles at the project level, instead of for a specific service account.  
`PRIVATE_CLUSTER_DISABLED` | This detector checks whether a GKE cluster has private cluster disabled. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`PRIMITIVE_ROLES_USED` | This detector checks whether a user has a basic role (Owner, Editor, or Viewer). For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings).  
`REDIS_ROLE_USED_ON_ORG` | This detector checks whether Redis IAM role is assigned to an organization or folder. For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings).  
`PUBLIC_BUCKET_ACL` | This detector checks whether a bucket is publicly accessible.  
`OPEN_MEMCACHED_PORT` | This detector checks whether a firewall has an open MEMCACHED port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OVER_PRIVILEGED_ACCOUNT` | This detector checks whether a service account has overly broad project access in a cluster. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`AUTO_REPAIR_DISABLED` | This detector checks whether a GKE cluster's auto repair feature is disabled. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`NETWORK_POLICY_DISABLED` | This detector checks whether the network policy is disabled on a cluster. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`CLUSTER_PRIVATE_GOOGLE_ACCESS_DISABLED` | This detector checks whether cluster hosts aren't configured to use only private, internal IP addresses to access Google APIs. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`OPEN_CASSANDRA_PORT` | This detector checks whether a firewall has an open Cassandra port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`TOO_MANY_KMS_USERS` | This detector checks whether there are more than three users of cryptographic keys. For more information, see [KMS vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#kms-findings).  
`OPEN_POSTGRESQL_PORT` | This detector checks whether a firewall has an open PostgreSQL port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`IP_ALIAS_DISABLED` | This detector checks whether a GKE cluster was created with the alias IP address range disabled. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings).  
`PUBLIC_SQL_INSTANCE` | This detector checks whether a Cloud SQL allows connections from all IP addresses.  
`OPEN_ELASTICSEARCH_PORT` | This detector checks whether a firewall has an open Elasticsearch port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
  
## View the posture template

To view the posture template for PCI DSS, do the following: 

### gcloud

Before using any of the command data below, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



Execute the [`gcloud scc posture-templates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc posture-templates describe \
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/pci_dss_v_3_2_1

#### Windows (PowerShell)
    
    
    gcloud scc posture-templates describe `
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/pci_dss_v_3_2_1

#### Windows (cmd.exe)
    
    
    gcloud scc posture-templates describe ^
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/pci_dss_v_3_2_1

The response contains the posture template.

### REST

Before using any of the request data, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



HTTP method and URL: 
    
    
    GET https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/pci_dss_v_3_2_1

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/pci_dss_v_3_2_1"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/pci_dss_v_3_2_1" | Select-Object -Expand Content

The response contains the posture template.

## What's next

  * [Create a security posture using this predefined posture template](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
