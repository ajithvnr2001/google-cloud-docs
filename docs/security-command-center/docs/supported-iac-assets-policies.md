---
url: https://docs.cloud.google.com/security-command-center/docs/supported-iac-assets-policies/
title: Supported asset types and policies for IaC validation \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:41.910616+00:00
---

# Supported asset types and policies for IaC validation  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/supported-iac-assets-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Supported asset types and policies for IaC validation Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document describes the asset types and policies that are supported in the [infrastructure as code (IaC) validation feature](https://docs.cloud.google.com/security-command-center/docs/validate-iac) in Security Command Center.

## Supported asset types

The following is the list of supported Google Cloud asset types:

  * `artifactregistry.googleapis.com/Repository`
  * `bigquery.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Table`
  * `cloudfunctions.googleapis.com/CloudFunction`
  * `cloudkms.googleapis.com/ImportJob`
  * `cloudkms.googleapis.com/KeyRing`
  * `cloudresourcemanager.googleapis.com/Folder`
  * `cloudresourcemanager.googleapis.com/Project`
  * `composer.googleapis.com/Environment`
  * `compute.googleapis.com/Autoscaler`
  * `compute.googleapis.com/BackendService`
  * `compute.googleapis.com/Disk`
  * `compute.googleapis.com/Firewall`
  * `compute.googleapis.com/ForwardingRule`
  * `compute.googleapis.com/GlobalForwardingRule`
  * `compute.googleapis.com/HealthCheck`
  * `compute.googleapis.com/Instance`
  * `compute.googleapis.com/InstanceGroup`
  * `compute.googleapis.com/Network`
  * `compute.googleapis.com/NodeGroup`
  * `compute.googleapis.com/NodeTemplate`
  * `compute.googleapis.com/ResourcePolicy`
  * `compute.googleapis.com/Route`
  * `compute.googleapis.com/Router`
  * `compute.googleapis.com/Snapshot`
  * `compute.googleapis.com/SslCertificate`
  * `compute.googleapis.com/SslPolicy`
  * `compute.googleapis.com/Subnetwork`
  * `compute.googleapis.com/TargetHttpProxy`
  * `compute.googleapis.com/TargetHttpsProxy`
  * `compute.googleapis.com/TargetPool`
  * `compute.googleapis.com/TargetSslProxy`
  * `compute.googleapis.com/UrlMap`
  * `compute.googleapis.com/VpnTunnel`
  * `container.googleapis.com/Cluster`
  * `container.googleapis.com/NodePool`
  * `dataflow.googleapis.com/Job`
  * `datastream.googleapis.com/ConnectionProfile`
  * `datastream.googleapis.com/PrivateConnection`
  * `datastream.googleapis.com/Stream`
  * `dns.googleapis.com/ManagedZone`
  * `dns.googleapis.com/Policy`
  * `file.googleapis.com/Instance`
  * `gkehub.googleapis.com/Membership`
  * `pubsub.googleapis.com/Subscription`
  * `pubsub.googleapis.com/Topic`
  * `run.googleapis.com/DomainMapping`
  * `run.googleapis.com/Job`
  * `run.googleapis.com/Service`
  * `serviceusage.googleapis.com/Service`
  * `spanner.googleapis.com/Database`
  * `spanner.googleapis.com/Instance`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`
  * `vpcaccess.googleapis.com/Connector`



Validations on the `disks[].initializeParams.sourceImage` field of `compute.googleapis.com/Instance` are not supported.

**Note:** If an IaC file contains both supported and unsupported asset types, [the IaC validation feature](https://docs.cloud.google.com/security-command-center/docs/validate-iac) ignores the unsupported asset types and validates only the supported asset types.

## Supported policies

This section describes the policies that are supported by IaC validation.

### Organization policies

The following is the list of supported organization policies:

  * `Allowed VPC egress settings` (`constraints/run.allowedVPCEgress`)
  * `Disable Guest Attributes of Compute Engine metadata` (`constraints/compute.disableGuestAttributesAccess`)
  * `Disable VM serial port access` (`constraints/compute.disableSerialPortAccess`)
  * `Disable VM serial port logging to Stackdriver` (`constraints/compute.disableSerialPortLogging`)
  * `Disable VPC External IPv6 usage` (`constraints/compute.disableVpcExternalIpv6`)
  * `Require OS Login` (`constraints/compute.requireOsLogin`)
  * `Restrict Authorized Networks on Cloud SQL instances` (`constraints/sql.restrictAuthorizedNetworks`)
  * `Require VPC Connector (Cloud Functions)` (`constraints/cloudfunctions.requireVPCConnector`)
  * `Disable VPC Internal IPv6 usage` (`constraints/compute.disableVpcInternalIpv6`)
  * `Allowed ingress settings (Cloud Run)` (`constraints/run.allowedIngress`)
  * `Enforce uniform bucket-level access` (`constraints/storage.uniformBucketLevelAccess`)
  * `Skip creation of default Compute Network` (`constraints/compute.skipDefaultNetworkCreation`)



### Organization policy custom constraint

All organization policy custom constraints are supported. However, you can't validate organization policies that include [tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy).

### Security Health Analytics custom modules

All Security Health Analytics custom modules are supported.

### Security Health Analytics built-in detectors

The following is the list of supported built-in detectors:

  * `ALPHA_CLUSTER_ENABLED`
  * `AUTO_BACKUP_DISABLED`
  * `AUTO_REPAIR_DISABLED`
  * `AUTO_UPGRADE_DISABLED`
  * `BIGQUERY_TABLE_CMEK_DISABLED`
  * `BUCKET_CMEK_DISABLED`
  * `BUCKET_LOGGING_DISABLED`
  * `BUCKET_POLICY_ONLY_DISABLED`
  * `CLUSTER_LOGGING_DISABLED`
  * `CLUSTER_MONITORING_DISABLED`
  * `CLUSTER_SECRETS_ENCRYPTION_DISABLED`
  * `CLUSTER_SHIELDED_NODES_DISABLED`
  * `COMPUTE_SECURE_BOOT_DISABLED`
  * `COMPUTE_SERIAL_PORTS_ENABLED`
  * `CONFIDENTIAL_COMPUTING_DISABLED`
  * `COS_NOT_USED`
  * `DATAPROC_CMEK_DISABLED`
  * `DATAPROC_IMAGE_OUTDATED`
  * `DEFAULT_SERVICE_ACCOUNT_USED`
  * `DISK_CMEK_DISABLED`
  * `DISK_CSEK_DISABLED`
  * `FIREWALL_RULE_LOGGING_DISABLED`
  * `FLOW_LOGS_DISABLED`
  * `FULL_API_ACCESS`
  * `VPC_FLOW_LOGS_SETTINGS_NOT_RECOMMENDED`
  * `INTEGRITY_MONITORING_DISABLED`
  * `INTRANODE_VISIBILITY_DISABLED`
  * `IP_ALIAS_DISABLED`
  * `IP_FORWARDING_ENABLED`
  * `KMS_KEY_NOT_ROTATED`
  * `KMS_PUBLIC_KEY`
  * `LEGACY_AUTHORIZATION_ENABLED`
  * `LEGACY_METADATA_ENABLED`
  * `LOAD_BALANCER_LOGGING_DISABLED`
  * `MASTER_AUTHORIZED_NETWORKS_DISABLED`
  * `NETWORK_POLICY_DISABLED`
  * `NODEPOOL_BOOT_CMEK_DISABLED`
  * `NODEPOOL_SECURE_BOOT_DISABLED`
  * `OPEN_CASSANDRA_PORT`
  * `OPEN_CISCOSECURE_WEBSM_PORT`
  * `OPEN_DIRECTORY_SERVICES_PORT`
  * `OPEN_DNS_PORT`
  * `OPEN_ELASTICSEARCH_PORT`
  * `OPEN_FIREWALL`
  * `OPEN_FTP_PORT`
  * `OPEN_HTTP_PORT`
  * `OPEN_LDAP_PORT`
  * `OPEN_MEMCACHED_PORT`
  * `OPEN_MONGODB_PORT`
  * `OPEN_MYSQL_PORT`
  * `OPEN_NETBIOS_PORT`
  * `OPEN_ORACLEDB_PORT`
  * `OPEN_POP3_PORT`
  * `OPEN_POSTGRESQL_PORT`
  * `OPEN_RDP_PORT`
  * `OPEN_REDIS_PORT`
  * `OPEN_SMTP_PORT`
  * `OPEN_SSH_PORT`
  * `OPEN_TELNET_PORT`
  * `OVER_PRIVILEGED_ACCOUNT`
  * `OVER_PRIVILEGED_SCOPES`
  * `OVER_PRIVILEGED_SERVICE_ACCOUNT_USER`
  * `PRIMITIVE_ROLES_USED`
  * `PRIVATE_CLUSTER_DISABLED`
  * `PRIVATE_GOOGLE_ACCESS_DISABLED`
  * `PUBLIC_BUCKET_ACL`
  * `PUBLIC_COMPUTE_IMAGE`
  * `PUBLIC_DATASET`
  * `PUBLIC_IP_ADDRESS`
  * `PUBLIC_SQL_INSTANCE`
  * `PUBSUB_CMEK_DISABLED`
  * `REDIS_ROLE_USED_ON_ORG`
  * `RELEASE_CHANNEL_DISABLED`
  * `RSASHA1_FOR_SIGNING`
  * `SERVICE_ACCOUNT_KEY_NOT_ROTATED`
  * `SHIELDED_VM_DISABLED`
  * `SSL_NOT_ENFORCED`
  * `SQL_CMEK_DISABLED`
  * `SQL_CONTAINED_DATABASE_AUTHENTICATION`
  * `SQL_CROSS_DB_OWNERSHIP_CHAINING`
  * `SQL_EXTERNAL_SCRIPTS_ENABLED`
  * `SQL_LOCAL_INFILE`
  * `SQL_LOG_CHECKPOINTS_DISABLED`
  * `SQL_LOG_CONNECTIONS_DISABLED`
  * `SQL_LOG_DISCONNECTIONS_DISABLED`
  * `SQL_LOG_DURATION_DISABLED`
  * `SQL_LOG_ERROR_VERBOSITY`
  * `SQL_LOG_EXECUTOR_STATS_ENABLED`
  * `SQL_LOG_HOSTNAME_ENABLED`
  * `SQL_LOG_LOCK_WAITS_DISABLED`
  * `SQL_LOG_MIN_DURATION_STATEMENT_ENABLED`
  * `SQL_LOG_MIN_ERROR_STATEMENT`
  * `SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY`
  * `SQL_LOG_MIN_MESSAGES`
  * `SQL_LOG_PARSER_STATS_ENABLED`
  * `SQL_LOG_PLANNER_STATS_ENABLED`
  * `SQL_LOG_STATEMENT`
  * `SQL_LOG_STATEMENT_STATS_ENABLED`
  * `SQL_LOG_TEMP_FILES`
  * `SQL_PUBLIC_IP`
  * `SQL_REMOTE_ACCESS_ENABLED`
  * `SQL_SKIP_SHOW_DATABASE_DISABLED`
  * `SQL_TRACE_FLAG_3625`
  * `SQL_USER_CONNECTIONS_CONFIGURED`
  * `SQL_USER_OPTIONS_CONFIGURED`
  * `USER_MANAGED_SERVICE_ACCOUNT_KEY`
  * `WEB_UI_ENABLED`
  * `WORKLOAD_IDENTITY_DISABLED`



## What's next

  * [Validate your IaC against your security posture](https://docs.cloud.google.com/security-command-center/docs/validate-iac).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
