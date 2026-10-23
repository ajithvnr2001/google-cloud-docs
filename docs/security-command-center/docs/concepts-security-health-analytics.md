---
url: https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics/
title: Overview of Security Health Analytics \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:31.271690+00:00
---

# Overview of Security Health Analytics  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Overview of Security Health Analytics Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Security Health Analytics is a managed service of Security Command Center that scans your cloud environments for common misconfigurations that might expose you to attack.

Security Health Analytics is disabled for new activations of Security Command Center on the Standard-legacy, Premium, and Enterprise tiers. For these organizations, use Compliance Manager to scan your environment for misconfigurations.

## Security Health Analytics features by tier

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The Security Health Analytics features that are available to you differ depending on the [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) at which Security Command Center is enabled. You can view which findings are available with which tiers at [Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors).

### Standard-legacy tier features

Standard-legacy [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

In the Standard-legacy tier, Security Health Analytics can detect only a basic group of medium-severity and high-severity vulnerabilities.

### Standard tier features

Standard [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

If the Standard tier is newly activated in your organization, meaning the organization was not migrated from the Standard-legacy tier, Security Health Analytics isn't available. Use the Compliance Manager [Security Essentials framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials) and [Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud) to scan your environment for misconfigurations and vulnerabilities that might expose you to attack.

If your organization was migrated from the Standard-legacy tier to the Standard tier, the following Security Health Analytics detectors are migrated to Compliance Manager controls in the Security Essentials framework:

  * [`DATAPROC_IMAGE_OUTDATED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dataproc-image-outdated)
  * [`LEGACY_AUTHORIZATION_ENABLED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#legacy-authorization-enabled)
  * [`OPEN_CISCOSECURE_WEBSM_PORT`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#open-ciscosecure-websm-port)
  * [`OPEN_DIRECTORY_SERVICES_PORT`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#open-directory-services-port)
  * [`OPEN_FIREWALL`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#open-firewall)
  * [`OPEN_RDP_PORT`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#open-rdp-port)
  * [`OPEN_SSH_PORT`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#open-ssh-port)
  * [`OPEN_TELNET_PORT`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#open-telnet-port)
  * [`PUBLIC_DATASET`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#public-dataset)
  * [`PUBLIC_IP_ADDRESS`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#public-ip-address)
  * [`PUBLIC_SQL_INSTANCE`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#public-sql-instance)
  * [`SSL_NOT_ENFORCED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ssl-not-enforced)
  * [`WEB_UI_ENABLED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#web-ui-enabled)



Security Health Analytics is enabled and all detectors continue to generate findings, but findings created by the Security Health Analytics version of the migrated detectors are labeled with the field-value identifier: `launch_state="LAUNCH_STATE_DEPRECATED"` and aren't displayed in some Google Cloud console pages.

Most SHA detectors have equivalent Compliance Manager controls. For more information, see [Mapping of Security Health Analytics detectors to cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#mapping-sha-cloud-control).

To view findings created by the Compliance Manager version of the migrated detectors, use the following:

  * **Findings** page
  * **Compliance** page > **Monitor** tab



To view the findings generated by the Security Health Analytics version of the migrated detectors, use the following:

  * **Findings** page and remove the `launch_state="LAUNCH_STATE_DEPRECATED"` term from the query.
  * Legacy [Vulnerabilities](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#vulnerabilities-page)



The following detectors are not migrated to the Security Essentials framework in Compliance Manager:

  * [`MFA_NOT_ENFORCED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#mfa-not-enforced)
  * [`NON_ORG_IAM_MEMBER`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#non-org-iam-member)
  * [`OPEN_GROUP_IAM_MEMBER`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#open-group-iam-member)
  * [`PUBLIC_BUCKET_ACL`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#public-bucket-acl)
  * [`PUBLIC_COMPUTE_IMAGE`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#public-compute-image)
  * [`PUBLIC_LOG_BUCKET`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#public-log-bucket)



You can enable these detectors in the **Settings > Security Health Analytics > Modules** tab.

To view findings created by these Security Health Analytics detectors, use the following:

  * **Findings** page
  * **Risk Overview** > **All risk** dashboard:

    * **Top misconfigurations** panel
    * **Misconfigurations by date** panel



Findings generated by these Security Health Analytics detectors don't appear on the **Compliance** page.

### Premium tier features

Premium [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

If the Premium tier is newly activated in your organization, meaning the organization was not migrated from the Standard tier, Security Health Analytics isn't available and can't be enabled. For these organizations, use Compliance Manager to scan your environment for misconfigurations.

If the Premium tier is migrated from the Standard tier, Security Health Analytics includes the following features:

  * All [detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors) for Google Cloud, as well as a number of other vulnerability detection features, such as the ability to create custom detection modules.
  * Findings are mapped to compliance controls for compliance reporting. For more information, see [Detectors and compliance](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#detectors_and_compliance).
  * Security Command Center attack path simulations calculate attack exposure scores and potential attack paths for most Security Health Analytics findings. For more information, see [Overview of attack exposure scores and attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_path_nodes).



If your organization was upgraded from the Standard tier to the Premium tier, see Switching tiers for information about the modified set of Security Health Analytics detector capabilities.

### Enterprise tier features

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

If the Enterprise tier is newly activated in your organization, meaning the organization was not migrated from the Standard tier, Security Health Analytics isn't available and can't be enabled. For these organizations, use Compliance Manager to scan your environment for misconfigurations.

If your organization was upgraded from the Standard tier to the Enterprise tier, see Switching tiers for information about the modified set of Security Health Analytics detector capabilities.

### Switching tiers

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Command Center in the Premium tier and Enterprise tiers has more detectors than in the Standard-legacy tier. If you are using the Premium or Enterprise tier and plan to downgrade to the Standard or Standard-legacy tier, we recommend that you resolve all findings before changing your tier.

When a Premium or Enterprise trial ends, or you downgrade from one of these tiers to the Standard or Standard-legacy tier, the state of the findings that were generated at the higher tier is set to `INACTIVE`.

If your organization didn't have Security Command Center and was [automatically activated with the Standard tier](https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy), then you upgraded to the Premium or Enterprise tier, use the Security Essentials framework in [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview) to configure detections.

If your organization was migrated to the Standard tier from the Standard-legacy tier, and then you upgraded to the Premium or Enterprise tier, Security Health Analytics remains partially enabled. You cannot enable Premium or Enterprise tier Security Health Analytics detectors. You must use the [ Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview) frameworks available with Premium and Enterprise tiers to configure detections.

Most of the Security Health Analytics detectors in the Premium and Enterprise tier are migrated to the Security Essentials framework in Compliance Manager.

For more information about Compliance Manager frameworks and cloud controls, see [Compliance Manager frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks).

For information about how Security Health Analytics detectors map to Compliance Manager cloud controls, see [Mapping of Security Health Analytics} detectors to cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#mapping-sha-cloud-control).

## Multicloud support

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Health Analytics can detect misconfigurations in your deployments on other cloud platforms.

Security Health Analytics supports the following other cloud service providers:

  * Amazon Web Services (AWS): To run the detectors on AWS data, you first need to connect Security Command Center to AWS, as described in [Connect to AWS for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws).

  * Microsoft Azure: To run the detectors on Microsoft Azure data, you first need to connect Security Command Center to Microsoft Azure, as described in [Connect to Microsoft Azure for vulnerability detection and risk assessment](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure).




## Supported Google Cloud services

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Health Analytics managed vulnerability assessment scanning for Google Cloud monitors specific resource types within supported services for common vulnerabilities and misconfigurations. Security Health Analytics doesn't scan all resource types within a service.

Security Health Analytics built-in detectors scan the following Google Cloud services and resources:

  * **AlloyDB for PostgreSQL** : 
    * Resources: clusters and database instances
    * Configurations: 
      * Backups
      * CMEK
      * SSL
      * Logging flags
  * **BigQuery** : 
    * Resources: datasets and tables
    * Configurations: 
      * Public data access
      * CMEK encryption
  * **Cloud Asset Inventory** : 
    * Resources: project-level Cloud Asset API enablement
  * **Cloud DNS** : 
    * Resources: managed zones and DNS policies
    * Configurations: 
      * DNSSEC
      * Query logging
  * **Cloud Key Management Service (Cloud KMS)** : 
    * Resources: key rings, CryptoKeys, and key import jobs
    * Configurations and policies: 
      * Key rotation
      * Public access
      * Separation of duties
  * **Cloud Logging** : 
    * Resources: log buckets, audit logging configurations, and log sink exports
  * **Cloud Monitoring** : 
    * Resources: alert policies and notification channels for metric thresholds on sensitive changes
  * **Pub/Sub** : 
    * Resources: topics
    * Configurations: 
      * CMEK encryption
  * **Cloud SQL** : 
    * Resources: Cloud SQL instances
    * Configurations and settings: 
      * Public IPs
      * SSL enforcement
      * Backups
      * Database flags
  * **Cloud Storage** : 
    * Resources: storage buckets (individual objects within buckets are not scanned)
    * Configurations and policies: 
      * Public ACLs
      * Uniform bucket-level access
      * CMEK
      * Retention policies
      * Object versioning
  * **Compute Engine** : 
    * Resources: 
      * VM instances
      * Persistent disks
      * Custom images
      * VPC networks and subnetworks
      * Firewall rules
      * SSL policies
      * Load balancer backend services and proxies
  * **Managed Service for Apache Spark** : 
    * Resources: clusters
    * Configurations: 
      * Image version status
      * CMEK encryption
  * **Google Kubernetes Engine** : 
    * Resources: GKE clusters and node pools
    * Features and settings: 
      * Auto-repair
      * Auto-upgrade
      * Workload Identity
      * Shielded nodes
      * Private cluster settings
  * **Identity and Access Management (IAM)** : 
    * Resources and settings: 
      * Service accounts
      * User-managed service account keys
      * Primitive role grants
      * MFA enforcement
  * **Resource Manager** : 
    * Resources: organizations, folders, and projects
    * Settings and policies: 
      * API key restrictions
      * Essential Contacts
      * Organization policies
  * **Services scanned by Organization Policy detectors** : 
    * Resources in the following services are scanned for compliance with organization policies, including Resource Location Restriction: 
      * **Gemini Enterprise Agent Platform** : datasets, models, and endpoints
      * **Artifact Registry** : repositories
      * **Managed Service for Apache Airflow** : environments
      * **Dataflow** : jobs



For a detailed list of all supported resource types and detectors, see the [Security Health Analytics finding reference](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors).

## Security Health Analytics scan types

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Health Analytics scans run in three modes:

  * **Batch scan:** all detectors are scheduled to run for all enrolled organizations or projects periodically.

For information about the frequency of scans, see Security Health Analytics scan latency.

  * **Real-time scan:** for Google Cloud deployments only, supported detectors start scans whenever a change is detected in a resource's configuration. Findings are written to Security Command Center. Real-time scans are not supported for deployments on other cloud platforms.

  * **Mixed-mode:** some detectors that support real-time scans might not detect changes in real time for all supported resource types. In those cases, configuration changes for some resource types are captured immediately and others are captured in batch scans. Exceptions are noted in the [tables of Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#sha-findings).




Security Health Analytics scans resources on other cloud platforms in batch mode only.

## Security Health Analytics scan latency

The following sections describe the amount of time before findings are generated by the initial scan and the frequency of subsequent scans.

**Note:** Batch scan schedules are performance objectives, not service guarantees.

### Initial scan

On the Premium and Enterprise tiers, the initial scan starts approximately one hour after the service is enabled. The first Security Health Analytics scans can take up to 12 hours to complete.

On the Security Command Center Standard and Standard-legacy tiers, scans run every 48 hours, which can result in an initial finding latency of 72 hours.

You might see some findings in the Google Cloud console while initial scans are taking place but before the onboarding process is complete. Preliminary findings are accurate and actionable, but they are not comprehensive. Using these findings for a compliance assessment within the first 24 hours is not recommended. 

### Subsequent scans

After the initial scan, detections run periodically in batch mode.

  * On the Premium and Enterprise tiers, batch scans run every day.
  * On the Standard and Standard-legacy tiers, batch scans run every 48 hours.



A detector might run in batch mode, real-time mode, or mixed- mode. For more information about these modes, see Security Health Analytics scan types.

With real-time scanning, relevant Google Cloud resource configuration changes might result in updated findings. The update might take several minutes, depending on the asset type and the change. A detector might not support real-time scanning if the detection uses information outside of a resource's configuration.

For information about whether a detector supports real-time scanning, see the **Asset scan settings** column for the detector in the [Security Health Analytics finding reference](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors) section of [Vulnerabilities findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

## Security Health Analytics detector enablement

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Health Analytics uses _detectors_ to identify vulnerabilities and misconfigurations in your cloud environment. Each detector corresponds to a finding category.

Security Health Analytics comes with many built-in detectors that check for vulnerabilities and misconfigurations across a large number of categories and resource types.

For the Premium and Enterprise (Deprecated) service tiers, you can also create your own custom detectors that can check for vulnerabilities or misconfigurations that are not covered by the built-in detectors or that are specific to your environment.

For more information about the built-in Security Health Analytics detectors, see Security Health Analytics built-in detectors.

For more information about creating and using custom modules, see Security Health Analytics custom modules.

### Enable and disable detectors

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Not all Security Health Analytics built-in detectors are enabled by default.

To turn on inactive built-in detectors, see [Enable and disable detectors](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#enable_and_disable_detectors).

To enable or disable a Security Health Analytics custom detection module, you can update the custom module by using the Google Cloud console, the gcloud CLI, or the Security Command Center API.

For more information about updating Security Health Analytics custom modules, see [Update a custom module](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create#update_a_custom_module).

### Built-in detectors and project-level activations

Standard-legacy, Standard, and Premium [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

When you activate Security Command Center for a project only, certain built-in Security Health Analytics detectors are not supported because they require organization-level permissions.

Of the built-in detectors that require an organization-level activation, you can enable those that are available with the Standard-legacy tier of Security Command Center for project-level activations by enabling the Standard-legacy tier for your organization.

Built-in detectors that require both the Premium tier and organization-level permissions are not supported with project-level activations.

For a list of the built-in Standard-legacy tier detectors that require an organization-level activation of Security Command Center Standard-legacy before they can be used with a project-level activation, see [Organization-level Standard tier finding categories](https://docs.cloud.google.com/security-command-center/docs/activate-scc-project-level-limitations#pla-standard-org-features-findings).

For a list of built-in Premium tier detectors that aren't supported with project-level activations, see [Unsupported Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/activate-scc-project-level-limitations#pla-unavailable-premium-features-sha-findings).

### Custom module detectors and project-level activations

Premium [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The scans of custom module detectors that you create in a project are limited to the scope of the project, regardless of the activation level of Security Command Center. Custom module detectors can scan only the resources that are available to the project in which they are created.

For more information about custom modules, see Security Health Analytics custom modules.

## Security Health Analytics built-in detectors

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

This section describes the high-level categories of the detectors, listed by cloud platform and the finding category that they generate.

**Note:** Not all detectors are enabled by default. To turn on inactive detectors, see [ Enable and disable detectors](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#enable_and_disable_detectors). 

### Built-in detectors for Google Cloud by high-level category

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The Security Health Analytics detectors for Google Cloud, and the findings that they generate, are grouped into the following high-level categories.

Security Health Analytics detectors monitor a subset of the Google Cloud resource types that are supported by [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types).

To see the individual detectors that are included in each category, click the category name.

  * [API key vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#api-findings)
  * [Cloud Asset Inventory vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#cloud-findings)
  * [Compute image vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#compute-image-findings)
  * [Compute instance vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#compute-instance-findings)
  * [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings)
  * [Managed Service for Apache Spark vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dataproc-findings)
  * [Dataset vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dataset-findings)
  * [DNS vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dns-findings)
  * [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings)
  * [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings)
  * [KMS vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#kms-findings)
  * [Logging vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#logging-findings)
  * [Monitoring vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#monitoring-findings)
  * [Multi-factor authentication vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#mfa-findings)
  * [Network vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#network-findings)
  * [Organization policy vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#org-findings)
  * [Pub/Sub vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#pubsub-findings)
  * [SQL vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#sql-findings)
  * [Storage vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#storage-findings)
  * [Subnetwork vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#subnetwork-findings)



### Built-in detectors for AWS

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

For a list of all of the Security Health Analytics detectors for AWS, see [AWS findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#aws-findings).

## Security Health Analytics custom modules

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Health Analytics custom modules are custom detectors for Google Cloud that extend the detection capabilities of Security Health Analytics beyond those provided by the built-in detectors.

Custom modules are not supported for other cloud platforms.

You can create custom modules by using the guided workflow in the Google Cloud console, or you can create the custom module definition yourself in a YAML file and then upload it to Security Command Center by using Google Cloud CLI commands or the Security Command Center API.

For more information, see [Overview of custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview).

## Detectors and compliance

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The Security Command Center measurement of compliance with security benchmarks is based in a large part on the findings produced by the Security Health Analytics vulnerability detectors.

Security Health Analytics monitors your compliance with detectors that are mapped to the controls of a wide variety of security standards. 

For each supported security standard, Security Health Analytics checks a subset of the controls. For the controls checked, Security Command Center shows you how many are passing. For the controls that are not passing, Security Command Center shows you a list of findings that describe the control failures. 

CIS reviews and certifies the mappings of Security Health Analytics detectors to each supported version of the CIS Google Cloud Foundations Benchmark. Additional compliance mappings are included for reference purposes only. 

Security Health Analytics adds support for new benchmark versions and standards periodically. Older versions remain supported, but are eventually deprecated. We recommend that you use the latest supported benchmark or standard available. 

With the [security posture service](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview), you can map organization policies and Security Health Analytics detectors to the standards and controls that apply to your business. After you create a security posture, you can monitor for any changes to the environment that could affect your business's compliance. 

With [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview), you can deploy frameworks that map regulatory controls to cloud controls. After you create a framework, you can monitor for any changes to the environment that might affect your business's compliance and audit your environment. 

For more information about managing compliance, see [Assess and report compliance with security standards](https://docs.cloud.google.com/security-command-center/docs/compliance-management). 

### Supported security standards

**Note:** These standards are supported if you have't enabled Compliance Manager. For information about the frameworks that you can use with Compliance Manager, see the [Compliance Manager overview](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#built-in-frameworks).

### Google Cloud

Security Health Analytics maps detectors for Google Cloud to one or more of the following compliance standards: 

  * [ Center for Information Security (CIS) Controls 8.0](https://www.cisecurity.org/controls/v8)
  * [ CIS Google Cloud Computing Foundations Benchmark](https://www.cisecurity.org/benchmark/google_cloud_computing_platform) v2.0.0, v1.3.0, v1.2.0, v1.1.0, and v1.0.0 
  * [ CIS Kubernetes Benchmark v1.5.1](https://www.cisecurity.org/benchmark/kubernetes)
  * [ Cloud Controls Matrix (CCM) 4](https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4)
  * [ Health Insurance Portability and Accountability Act (HIPAA)](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
  * [ International Organization for Standardization (ISO) 27001, 2022 and 2013](https://www.iso.org/standard/27001)
  * [ National Institute of Standards and Technology (NIST) 800-53 R5 and R4](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#/)
  * [National Institute of Standards and Technology (NIST) Cybersecurity Framework (CSF) 1.0](https://www.nist.gov/cyberframework/framework-version-10)
  * [ Open Web Application Security Project (OWASP) Top Ten, 2021 and 2017](https://owasp.org/www-project-top-ten/)
  * [ Payment Card Industry Data Security Standard (PCI DSS) 4.0 and 3.2.1](https://www.pcisecuritystandards.org/document_library/)
  * System and Organization Controls (SOC) 2 [ 2017 Trust Services Criteria (TSC)](https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022)



### AWS

In the Enterprise (Deprecated) service tier, Security Health Analytics maps detectors for Amazon Web Services (AWS) to one or more of the following compliance standards:

  * [CIS Amazon Web Services Foundations](https://www.cisecurity.org/benchmark/amazon_web_services) 2.0.0
  * [CIS Critical Security Controls Version 8.0](https://www.cisecurity.org/controls/v8)
  * [Cloud Controls Matrix (CCM) 4](https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4)
  * [Health Insurance Portability and Accountability Act (HIPAA)](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
  * [International Organization for Standardization (ISO) 27001, 2022](https://www.iso.org/standard/27001)
  * [National Institute of Standards and Technology (NIST) 800-53 R5](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#/)
  * National Institute of Standards and Technology (NIST) [ Cybersecurity Framework (CSF) 1.0](https://www.nist.gov/cyberframework/framework-version-10)
  * [Payment Card Industry Data Security Standard (PCI DSS) 4.0 and 3.2.1](https://www.pcisecuritystandards.org/document_library/)
  * System and Organization Controls (SOC) 2 [ 2017 Trusted Services Criteria (TSC)](https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022)



For more information about compliance, see [Assess and report security benchmark compliance](https://docs.cloud.google.com/security-command-center/docs/compliance-management).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
