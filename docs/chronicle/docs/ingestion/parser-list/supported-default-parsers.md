---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers/
title: Supported log types and default parsers \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:24.606267+00:00
---

# Supported log types and default parsers  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supported log types and default parsers

**Caution:** The Ingestion API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. To ingest logs into Google SecOps, use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

This document contains information about Google Security Operations integrations for data ingestion. It summarizes the devices and the associated ingestion label (`log_type`) field in the Ingestion API and `data_type` in a Forwarder configuration that Google SecOps supports.

For information on how to request or create log types, see [Request prebuilt and create custom log types](https://docs.cloud.google.com/chronicle/docs/event-processing/request-log-type).

  * Supported log types with a default parser

  * Supported log types without a default parser




## Supported log types with a default parser

Parsers normalize raw log data into structured Unified Data Model (UDM) format. This section lists supported devices, and the associated `log_type` field in the Ingestion API and `data_type` in a Forwarder configuration, that also have a prebuilt default parser. The default parser is supported by Google SecOps as long as the device's raw logs are received in the required format.

For a list of supported log types without a default parser, see Supported log types without a default parser.

The **Format** column indicates the high-level structure of the raw log, as:

  * CSV: Comma Separated Values
  * JSON: JavaScript Object Notation
  * SYSLOG: syslog formatted message
  * KV: key-value pair
  * XML: Extensible Markup Language
  * SYSLOG + KV: syslog header with key-value body
  * SYSLOG + JSON: syslog header with JSON body
  * SYSLOG + XML: syslog header with XML body
  * LEEF: Log Event Extended Format
  * CEF: Common Event Format

**Note:** Parsers with an 'N/A' log type are for data sources that support direct ingestion only.

These changes are applied to newly ingested logs. Parser changes are not applied retroactively to previously ingested logs.

Vendor / Product | Category | Log type | Format | Latest Update  
---|---|---|---|---  
[A10 Load Balancer](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/a10-load-balancer) | LOAD BALANCER | `A10_LOAD_BALANCER` | SYSLOG | [2025-12-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/a10-load-balancer-changelog)  
[Abnormal Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/abnormal-security) | Email Server | `ABNORMAL_SECURITY` | JSON , SYSLOG | [2026-03-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/abnormal-security-changelog)  
Absolute Mobile Device Management | Mobile Device Management | `ABSOLUTE` | SYSLOG + KV (CEF) | [2024-12-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/absolute-changelog)  
[Acalvio](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/acalvio) | Deception Software | `ACALVIO` | SYSLOG + KV | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/acalvio-changelog)  
[Accellion](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/accellion) | DLP | `ACCELLION` | SYSLOG | [2022-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/accellion-changelog)  
[ManageEngine ADAudit Plus](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/adaudit-plus) | Active Directory Audit | `ADAUDIT_PLUS` | SYSLOG + KV (CEF), JSON | [2026-06-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/adaudit-plus-changelog)  
Microsoft AD FS | LDAP | `ADFS` | JSON | [2026-01-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/adfs-changelog)  
[ManageEngine ADManager Plus](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/admanager-plus) | Miscellaneous Windows-specific log types. | `ADMANAGER_PLUS` | KV, SYSLOG + KV | [2026-04-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/admanager-plus-changelog)  
[ADVA Fiber Service Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/adva-fsp) | Switches and Routers | `ADVA_FSP` | SYSLOG+KV | [2023-12-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/adva-fsp-changelog)  
[Agiloft](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/agiloft) | SAAS Application | `AGILOFT` | JSON, Syslog | [2025-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/agiloft-changelog)  
[Advanced Intrusion Detection Environment](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aide) | Alert | `AIDE` | SYSLOG | [2025-03-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aide-changelog)  
[Airlock Digital Application Allowlisting](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/airlock-digital) | Application Whitelisting | `AIRLOCK_DIGITAL` | SYSLOG,JSON | [2026-07-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/airlock-digital-changelog)  
[VMware AirWatch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/airwatch) | Wireless | `AIRWATCH` | SYSLOG + KV | [2025-06-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/airwatch-changelog)  
[AIX system](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aix-system) | OS | `AIX_SYSTEM` | SYSLOG | [2026-09-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aix-system-changelog)  
[Active Countermeasures](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ai-hunter) | Alert | `AI_HUNTER` | SYSLOG, SYSLOG + JSON | [2026-06-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ai-hunter-changelog)  
[Akamai Cloud Monitor](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-cloud-monitor) | Load Balancer, Traffic Shaper, ADC | `AKAMAI_CLOUD_MONITOR` | JSON | [2026-01-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-cloud-monitor-changelog)  
[Akamai DataStream 2](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-datastream-2) | SaaS Applications | `AKAMAI_DATASTREAM_2` | JSON | [2026-07-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-datastream-2-changelog)  
[Akamai DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-dns) | DNS | `AKAMAI_DNS` | CSV, JSON | [2024-11-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-dns-changelog)  
[Akamai Enterprise Application Access](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-eaa) | Enterprise Application Access | `AKAMAI_EAA` | JSON | [2025-07-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-eaa-changelog)  
[Akamai SIEM Connector](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-siem-connector) | Log Aggregation and SIEM Systems | `AKAMAI_SIEM_CONNECTOR` | JSON | [2026-07-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-siem-connector-changelog)  
[Akamai WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-waf) | WAF | `AKAMAI_WAF` | SYSLOG, JSON | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-waf-changelog)  
[Akeyless Vault Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akeyless-vault) | Akeyless Vault Platform | `AKEYLESS_VAULT` | KV + JSON, Syslog + JSON | [2026-04-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akeyless-vault-changelog)  
[Alcatel Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/alcatel-switch) | Privileged Account Activity | `ALCATEL_SWITCH` | SYSLOG | [2024-03-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/alcatel-switch-changelog)  
[AlgoSec Security Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/algosec) | Policy Management | `ALGOSEC` | SYSLOG + KV (CEF) | [2025-12-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/algosec-changelog)  
[Alveo Risk Data Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/alveo-rdm) | SaaS Applications | `ALVEO_RDM` | JSON | [2026-08-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/alveo-rdm-changelog)  
[AMD Pensando DSS Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/amd-dss-firewall) | Firewall | `AMD_DSS_FIREWALL` | SYSLOG + CSV | [2023-05-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/amd-dss-firewall-changelog)  
[Anomali](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/anomali-ioc) | IOC | `ANOMALI_IOC` | JSON, CEF | [2026-08-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/anomali-ioc-changelog)  
[Ansible AWX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ansible-awx) | Automation and DevOps Tools | `ANSIBLE_AWX` | JSON | [2024-06-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ansible-awx-changelog)  
[Apache](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/apache) | Security | `APACHE` | SYSLOG + JSON, SYSLOG, JSON, KV | [2026-07-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/apache-changelog)  
[Appian Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/appian-cloud) | Collaboration log types | `APPIAN_CLOUD` | SYSLOG | [2026-05-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/appian-cloud-changelog)  
[AppOmni](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/appomni) | SAAS Security Application | `APPOMNI` | JSON | [2026-08-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/appomni-changelog)  
[Aqua Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aqua-security) | IaaS Applications | `AQUA_SECURITY` | JSON | [2025-07-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aqua-security-changelog)  
[Netscout](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-edge-defense) | NETWORK | `ARBOR_EDGE_DEFENSE` | SYSLOG + KV | [2025-10-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arbor-edge-defense-changelog)  
[Netscout Arbor Sightline](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-sightline) | Monitoring | `ARBOR_SIGHTLINE` | SYSLOG + JSON | [2025-04-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arbor-sightline-changelog)  
[Archer Integrated Risk Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/archer-irm) | Risk Management Solution | `ARCHER_IRM` | SYSLOG | [2024-08-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/archer-irm-changelog)  
[Arcsight CEF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arcsight-cef) | Security log | `ARCSIGHT_CEF` | CEF Syslog | [2026-07-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arcsight-cef-changelog)  
[Area1 Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/area1) | Email server | `AREA1` | JSON | [2024-09-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/area1-changelog)  
[Arista Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arista-switch) | Switches | `ARISTA_SWITCH` | JSON+SYSLOG | [2025-12-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arista-switch-changelog)  
[Armis Activities](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-activities) | ACTIVITIES | `ARMIS_ACTIVITIES` | JSON | [2026-08-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/armis-activities-changelog)  
[Armis Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-alerts) | ALERTS | `ARMIS_ALERTS` | JSON | [2026-07-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/armis-alerts-changelog)  
[Armis Devices](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-devices) | DEVICES | `ARMIS_DEVICES` | JSON | [2023-03-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/armis-devices-changelog)  
[Armis Vulnerabilities](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-vulnerabilities) | VULNERABILITIES | `ARMIS_VULNERABILITIES` | JSON | [2023-03-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/armis-vulnerabilities-changelog)  
[Array Networks SSL VPN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arraynetworks-vpn) | VPN | `ARRAYNETWORKS_VPN` | SYSLOG, SYSLOG + KV | [2026-08-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arraynetworks-vpn-changelog)  
[Aruba Airwave](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-airwave) | Wireless | `ARUBA_AIRWAVE` | XML | [2025-12-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-airwave-changelog)  
[HPE Aruba Networking Central](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-central) | Data Security | `ARUBA_CENTRAL` | SYSLOG , JSON | [2025-03-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-central-changelog)  
[Aruba EdgeConnect SD-WAN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-edgeconnect-sdwan) | Network Security | `ARUBA_EDGECONNECT_SDWAN` | SYSLOG + CSV, JSON | [2026-05-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-edgeconnect-sdwan-changelog)  
[Aruba IPS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-ips) | IPS | `ARUBA_IPS` | JSON | [2022-06-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-ips-changelog)  
[Aruba Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-switch) | Network Infrastructure | `ARUBA_SWITCH` | SYSLOG | [2026-07-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-switch-changelog)  
[Aruba](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-wireless) | Wireless | `ARUBA_WIRELESS` | SYSLOG | [2026-04-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-wireless-changelog)  
[AlphaSOC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asoc-alert) | Alert | `ASOC_ALERT` | JSON | 2021-06-21  
[Asset Panda](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asset-panda) | SaaS Applications | `ASSET_PANDA` | JSON | [2025-02-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/asset-panda-changelog)  
[Static IP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asset-static-ip) | DHCP | `ASSET_STATIC_IP` | CSV | [2023-06-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/asset-static-ip-changelog)  
[Atlassian Cloud Admin Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-audit) | Audit | `ATLASSIAN_AUDIT` | JSON | [2026-09-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-audit-changelog)  
[Atlassian Bitbucket](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-bitbucket) | Atlassian Bitbucket | `ATLASSIAN_BITBUCKET` | JSON, SYSLOG | [2026-09-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-bitbucket-changelog)  
[Atlassian Confluence](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-confluence) | Knowledge base | `ATLASSIAN_CONFLUENCE` | SYSLOG, JSON | [2024-07-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-confluence-changelog)  
[Atlassian Jira](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-jira) | Ticketing Application | `ATLASSIAN_JIRA` | SYSLOG, JSON | [2026-07-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-jira-changelog)  
[Attivo Networks](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/attivo) | NETWORK | `ATTIVO` | SYSLOG + KV (CEF) | [2026-01-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/attivo-changelog)  
[Linux Auditing System (AuditD)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/auditd) | OS | `AUDITD` | SYSLOG, JSON, XML, KV | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/auditd-changelog)  
[Auth0](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/auth-zero) | Authentication log | `AUTH_ZERO` | JSON | [2026-04-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/auth-zero-changelog)  
[Automation Anywhere](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/automation-anywhere) | Automation Tools | `AUTOMATION_ANYWHERE` | SYSLOG + KV, JSON | [2026-01-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/automation-anywhere-changelog)  
Avanan Email Security | Email Server | `AVANAN_EMAIL` | JSON | [2025-11-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/avanan-email-changelog)  
[Avatier Password Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/avatier) | SaaS Application | `AVATIER` | SYSLOG + KV | 2021-08-05  
[Avaya Aura Experience Portal](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/avaya-aura) | Telephone software | `AVAYA_AURA` | SYSLOG | [2026-07-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/avaya-aura-changelog)  
[Avigilon Access Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/avigilon-access-logs) | IaaS Applications | `AVIGILON_ACCESS_LOGS` | XML | [2024-12-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/avigilon-access-logs-changelog)  
Awake NDR | NDR | `AWAKE_NDR` | JSON | [2024-01-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/awake-ndr-changelog)  
[Aware Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aware-audit) | Application server logs | `AWARE_AUDIT` | JSON | [2025-02-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aware-audit-changelog)  
[Aware Signals](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aware-signals) | SaaS Applications | `AWARE_SIGNALS` | JSON | [2025-01-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aware-signals-changelog)  
[Amazon API Gateway](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-api-gateway) | AWS-specific log types | `AWS_API_GATEWAY` | JSON | [2026-05-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-api-gateway-changelog)  
[AWS Aurora](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-aurora) | AWS | `AWS_AURORA` | JSON, SYSLOG | [2026-04-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-aurora-changelog)  
[AWS CloudFront](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudfront) | CDN | `AWS_CLOUDFRONT` | SYSLOG, JSON, SYSLOG + KV | [2026-04-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudfront-changelog)  
[AWS Cloudtrail](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudtrail) | Cloud Log Aggregator | `AWS_CLOUDTRAIL` | JSON | [2026-09-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudtrail-changelog)  
[AWS CloudWatch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudwatch) | Cloud service monitoring | `AWS_CLOUDWATCH` | JSON, SYSLOG, JSON+KV, XML | [2026-08-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudwatch-changelog)  
[AWS Config](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-config) | AWS Specific | `AWS_CONFIG` | JSON | [2025-09-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-config-changelog)  
[AWS Control Tower](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-control-tower) | Identity and Access Management | `AWS_CONTROL_TOWER` | JSON | [2026-07-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-control-tower-changelog)  
[AWS EC2 Hosts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ec2-hosts) | AWS Specific | `AWS_EC2_HOSTS` | JSON | [2024-01-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-ec2-hosts-changelog)  
[AWS EC2 Instances](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ec2-instances) | AWS Specific | `AWS_EC2_INSTANCES` | JSON | [2024-01-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-ec2-instances-changelog)  
AWS EC2 VPCs | AWS Specific | `AWS_EC2_VPCS` | JSON | [2024-01-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-ec2-vpcs-changelog)  
[AWS ECS Metrics](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ecs-metrics) | Security | `AWS_ECS_METRICS` | SYSLOG + KV | [2026-08-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-ecs-metrics-changelog)  
[AWS Elastic Load Balancer](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-elb) | AWS Specific | `AWS_ELB` | SYSLOG, JSON | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-elb-changelog)  
[AWS EMR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-emr) | AWS Specific | `AWS_EMR` | SYSLOG, SYSLOG+JSON, JSON | [2023-12-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-emr-changelog)  
[AWS Identity and Access Management (IAM)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-iam) | AWS Specific | `AWS_IAM` | JSON | [2023-12-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-iam-changelog)  
[AWS Inspector](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-inspector) | AWS-specific log types | `AWS_INSPECTOR` | JSON, SYSLOG | [2026-08-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-inspector-changelog)  
[AWS Key Management Service](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-kms) | AWS Specific | `AWS_KMS` | JSON | [2022-05-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-kms-changelog)  
[AWS Lambda Function](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-lambda-function) | Web Proxy log types. | `AWS_LAMBDA_FUNCTION` | SYSLOG | [2025-07-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-lambda-function-changelog)  
[AWS Macie](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-macie) | AWS-specific logs | `AWS_MACIE` | JSON | [2025-05-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-macie-changelog)  
[AWS Network Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-network-firewall) | Firewall | `AWS_NETWORK_FIREWALL` | JSON | [2026-06-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-network-firewall-changelog)  
[AWS RDS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-rds) | Database | `AWS_RDS` | SYSLOG,JSON, CSV | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-rds-changelog)  
[AWS Redshift](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-redshift) | AWS | `AWS_REDSHIFT` | JSON + CSV + SYSLOG | [2025-04-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-redshift-changelog)  
[AWS Route 53 DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-route-53) | AWS Specific | `AWS_ROUTE_53` | JSON + SYSLOG | [2025-04-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-route-53-changelog)  
[AWS S3 Server Access](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-s3-server-access) | AWS Specific | `AWS_S3_SERVER_ACCESS` | SYSLOG | [2025-06-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-s3-server-access-changelog)  
[AWS Security Hub](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-security-hub) | IDS/IPS | `AWS_SECURITY_HUB` | JSON | [2026-06-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-security-hub-changelog)  
[AWS Session Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-session-manager) | AWS Specific | `AWS_SESSION_MANAGER` | SYSLOG/JSON | [2025-04-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-session-manager-changelog)  
[AWS VPC Flow](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-flow) | AWS Specific | `AWS_VPC_FLOW` | SYSLOG+JSON, JSON, CSV, SYSLOG+CSV | [2026-06-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpc-flow-changelog)  
AWS VPC Flow (CSV) | AWS Specific | `AWS_VPC_FLOW_CSV` | CSV | [2026-06-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpc-flow-csv-changelog)  
[Amazon VPC Transit Gateway Flow Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-transit-gateway) | Network | `AWS_VPC_TRANSIT_GATEWAY` | JSON | [2025-09-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpc-transit-gateway-changelog)  
[AWS VPN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpn) | VPN | `AWS_VPN` | JSON | [2024-07-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpn-changelog)  
[AWS WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-waf) | AWS Specific | `AWS_WAF` | JSON | [2026-08-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-waf-changelog)  
[Azion](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azion) | Firewall | `AZION` | JSON | [2023-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azion-changelog)  
[Microsoft Azure Activity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-activity) | Misc Windows Specific | `AZURE_ACTIVITY` | JSON | [2026-10-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-activity-changelog)  
[Azure AD](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad) | LDAP | `AZURE_AD` | JSON | [2026-08-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-changelog)  
[Azure AD Directory Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-audit) | Audit | `AZURE_AD_AUDIT` | JSON, Syslog+JSON | [2026-10-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-audit-changelog)  
[Azure AD Organizational Context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-context) | LDAP | `AZURE_AD_CONTEXT` | JSON | [2026-08-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-context-changelog)  
[Azure AD Sign-In](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-signin) | Misc Windows Specific | `AZURE_AD_SIGNIN` | JSON | [2026-09-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-signin-changelog)  
[Azure API Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-api-management) | Schema | `AZURE_API_MANAGEMENT` | JSON | [2025-01-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-api-management-changelog)  
[Azure App Service](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-app-service) | SAAS | `AZURE_APP_SERVICE` | JSON | [2026-08-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-app-service-changelog)  
[Azure Cosmos DB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-cosmos-db) | Database | `AZURE_COSMOS_DB` | JSON | [2025-01-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-cosmos-db-changelog)  
[Azure DevOps Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-devops) | Automation and DevOps Tools | `AZURE_DEVOPS` | JSON | [2025-03-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-devops-changelog)  
[Azure Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-firewall) | Azure Firewall Application Rule | `AZURE_FIREWALL` | JSON | [2026-08-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-firewall-changelog)  
Azure Front Door | Web server logs | `AZURE_FRONT_DOOR` | JSON | [2026-04-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-front-door-changelog)  
[Azure Application Gateway](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-gateway) | GATEWAY | `AZURE_GATEWAY` | JSON | [2026-09-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-gateway-changelog)  
[Azure Key Vault logging](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-keyvault-audit) | Audit | `AZURE_KEYVAULT_AUDIT` | JSON | [2026-09-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-keyvault-audit-changelog)  
[Microsoft Intune](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune) | Mobile Device Management | `AZURE_MDM_INTUNE` | JSON | [2026-08-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-mdm-intune-changelog)  
[Microsoft Intune Context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune-context) | Mobile Device Management | `AZURE_MDM_INTUNE_CONTEXT` | Json | [2024-09-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-mdm-intune-context-changelog)  
[Microsoft Azure NSG Flow](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-nsg-flow) | Network Flow | `AZURE_NSG_FLOW` | JSON | [2026-07-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-nsg-flow-changelog)  
[Microsoft Azure Resource](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-resource-logs) | Log Aggregator | `AZURE_RESOURCE_LOGS` | JSON | [2026-07-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-resource-logs-changelog)  
Azure SQL | Database | `AZURE_SQL` | JSON | [2026-04-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-sql-changelog)  
[Azure Storage Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-storage-audit) | Storage | `AZURE_STORAGE_AUDIT` | JSON | [2026-07-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-storage-audit-changelog)  
Azure VNET Flow | Netflow log type | `AZURE_VNET_FLOW` | JSON | [2025-07-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-vnet-flow-changelog)  
[Azure VPN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-vpn) | VPN | `AZURE_VPN` | JSON | [2024-10-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-vpn-changelog)  
[Azure WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-waf) | Log Aggregator | `AZURE_WAF` | JSON | [2024-08-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-waf-changelog)  
[Barracuda CloudGen Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-cloudgen-firewall) | SaaS Applications | `BARRACUDA_CLOUDGEN_FIREWALL` | Syslog | [2026-04-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-cloudgen-firewall-changelog)  
[Barracuda Email](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-email) | Email Server | `BARRACUDA_EMAIL` | SYSLOG+JSON, JSON | [2026-02-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-email-changelog)  
Barracuda Firewall | Firewall | `BARRACUDA_FIREWALL` | SYSLOG | [2026-02-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-firewall-changelog)  
[Barracuda WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-waf) | Firewall | `BARRACUDA_WAF` | JSON, SYSLOG + KV, SYSLOG + CSV | [2026-06-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-waf-changelog)  
[Barracuda Web Filter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-webfilter) | Webfilter | `BARRACUDA_WEBFILTER` | SYSLOG | [2024-11-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-webfilter-changelog)  
[BeyondTrust BeyondInsight](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-beyondinsight) | Privileged Account Activity | `BEYONDTRUST_BEYONDINSIGHT` | KV , SYSLOG + JSON | [2026-03-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-beyondinsight-changelog)  
[BeyondTrust Endpoint Privilege Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-endpoint) | Privileged Account Activity | `BEYONDTRUST_ENDPOINT` | JSON | [2026-01-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-endpoint-changelog)  
[BeyondTrust Privileged Identity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-pi) | Privilege Account Activity | `BEYONDTRUST_PI` | SYSLOG | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-pi-changelog)  
BeyondTrust Secure Remote Access | Remote Access Tools | `BEYONDTRUST_REMOTE_ACCESS` | SYSLOG + KV | [2025-12-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-remote-access-changelog)  
[Big Switch BigCloudFabric](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bigswitch-bcf) | Switches, Routers | `BIGSWITCH_BCF` | SYSLOG | 2021-04-20  
Bindplane Agent | Log Aggregation and SIEM Systems | `BINDPLANE_AGENT` | JSON | [2025-11-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bindplane-agent-changelog)  
BIND | DNS | `BIND_DNS` | SYSLOG | [2026-01-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bind-dns-changelog)  
[Bitdefender](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bitdefender) | AV / Endpoint | `BITDEFENDER` | CSV, SYSLOG, SYSLOG + JSON | [2026-09-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bitdefender-changelog)  
Bitwarden Events | Password Manager | `BITWARDEN_EVENTS` | JSON | [2023-11-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bitwarden-events-changelog)  
[BloxOne Threat Defense](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bloxone) | DNS | `BLOXONE` | SYSLOG + JSON | [2025-01-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bloxone-changelog)  
[Bluecat DDI](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-ddi) | DDI (DNS, DHCP, IPAM) | `BLUECAT_DDI` | SYSLOG | [2026-08-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bluecat-ddi-changelog)  
[Bluecat Edge DNS Resolver](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-edge) | DNS | `BLUECAT_EDGE` | JSON, KV, SYSLOG | 2022-01-18  
[Blue Coat Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecoat-webproxy) | Web Proxy | `BLUECOAT_WEBPROXY` | SYSLOG + JSON, SYSLOG + KV, KV, SYSLOG | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bluecoat-webproxy-changelog)  
[BMC AMI Defender](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-ami-defender) | Mainframe | `BMC_AMI_DEFENDER` | SYSLOG | [2024-05-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bmc-ami-defender-changelog)  
[BMC Client Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-client-management) | Security | `BMC_CLIENT_MANAGEMENT` | SYSLOG | [2024-11-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bmc-client-management-changelog)  
[BMC Helix Discovery](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-helix-discovery) | bmc helix discovery | `BMC_HELIX_DISCOVERY` | SYSLOG | [2022-08-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bmc-helix-discovery-changelog)  
[BeyondTrust](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bomgar) | Privilege Account Activity | `BOMGAR` | SYSLOG | [2026-07-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bomgar-changelog)  
[Box](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/box) | Collaboration | `BOX` | JSON | [2026-09-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/box-changelog)  
[CA Privileged Access Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ca-pam) | NA | `BROADCOM_CA_PAM` | SYSLOG | [2024-11-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/broadcom-ca-pam-changelog)  
[Broadcom SSL Visibility Appliance](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ssl-va) | SSL Visibility | `BROADCOM_SSL_VA` | SYSLOG | [2024-06-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/broadcom-ssl-va-changelog)  
[Broadcom Support Portal Audit Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-support-portal) | Security | `BROADCOM_SUPPORT_PORTAL` | SYSLOG + KV,SYSLOG,JSON | [2026-03-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/broadcom-support-portal-changelog)  
[Brocade ServerIron ADX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/brocade-serveriron) | Load Balancer | `BROCADE_SERVERIRON` | SYSLOG | 2022-01-13  
[Brocade Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/brocade-switch) | Switches | `BROCADE_SWITCH` | SYSLOG, CSV | [2025-06-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/brocade-switch-changelog)  
[Zeek JSON](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bro-json) | DNS | `BRO_JSON` | JSON | [2026-10-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bro-json-changelog)  
[Zeek TSV](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bro-tsv) | Format Specific | `BRO_TSV` | SYSLOG + TSV | [2024-05-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bro-tsv-changelog)  
[Cambium Networks](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cambium-networks) | Switches and Routers Log Type | `CAMBIUM_NETWORKS` | SYSLOG | [2025-10-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cambium-networks-changelog)  
[Apache Cassandra](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cassandra) | Web server | `CASSANDRA` | JSON,SYSLOG+JSON | [2026-03-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cassandra-changelog)  
[Cato Networks](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cato-networks) | NDR | `CATO_NETWORKS` | JSON | [2026-08-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cato-networks-changelog)  
CA Access Control | Access Management | `CA_ACCESS_CONTROL` | JSON+SYSLOG, SYSLOG | [2023-07-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-access-control-changelog)  
[CA ACF2](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-acf2) | Mainframe | `CA_ACF2` | LEEF | [2022-05-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-acf2-changelog)  
[CA LDAP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-ldap) | Web server | `CA_LDAP` | JSON | [2022-08-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-ldap-changelog)  
[SiteMinder Web Access Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-sso-web) | SSO | `CA_SSO_WEB` | JSON, SYSLOG + KV | [2026-04-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-sso-web-changelog)  
[Carbon Black App Control](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cb-app-control) | Security log | `CB_APP_CONTROL` | CEF, JSON | [2025-08-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cb-app-control-changelog)  
[Carbon Black](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cb-edr) | EDR | `CB_EDR` | JSON, SYSLOG | [2025-12-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cb-edr-changelog)  
[CENSYS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/censys) | NDR | `CENSYS` | SYSLOG + KV | [2024-02-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/censys-changelog)  
[Centrify](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/centrify-sso) | SSO | `CENTRIFY_SSO` | JSON | [2022-08-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/centrify-sso-changelog)  
[Centripetal Networks IOC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/centripetal-ioc) | IOC | `CENTRIPETAL_IOC` | SYSLOG + KV | 2022-01-06  
[Cequence Bot Defense](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cequence-bot-defense) | Log Aggregator | `CEQUENCE_BOT_DEFENSE` | JSON | [2025-08-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cequence-bot-defense-changelog)  
[Checkpoint Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-audit) | AUDIT | `CHECKPOINT_AUDIT` | SYSLOG + KV (CEF) | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-audit-changelog)  
[Check Point Sandblast](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-edr) | EDR | `CHECKPOINT_EDR` | SYSLOG + KV and SYSLOG + CEF | [2026-08-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-edr-changelog)  
[Check Point](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-firewall) | Firewall | `CHECKPOINT_FIREWALL` | SYSLOG + KV, JSON | [2026-07-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-firewall-changelog)  
[Check Point Harmony](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-harmony) | Remote Access Tools | `CHECKPOINT_HARMONY` | SYSLOG+KV, JSON, SYSLOG + JSON | [2026-07-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-harmony-changelog)  
[Checkpoint SmartDefense](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-smartdefense) | SmartDefences | `CHECKPOINT_SMARTDEFENSE` | SYSLOG + CEF, SYSLOG + KV | [2026-04-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-smartdefense-changelog)  
[ChromeOS XDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chromeos-xdr) | SaaS Applications | `CHROMEOS_XDR` | JSON | [2026-07-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/chromeos-xdr-changelog)  
[Chrome Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-management) | Browser | `CHROME_MANAGEMENT` | JSON | [2026-09-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/chrome-management-changelog)  
Chronicle SOAR Audit | SOAR | `CHRONICLE_SOAR_AUDIT` | JSON | [2026-04-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/chronicle-soar-audit-changelog)  
Ciena Router logs | Application server logs | `CIENA_ROUTER` | SYSLOG | [2025-01-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ciena-router-changelog)  
[Cimcor | File Integrity Monitoring](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cimcor) | Monitoring | `CIMCOR` | SYSLOG + KV | [2024-06-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cimcor-changelog)  
[CipherTrust Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ciphertrust-manager) | Physical Security log types | `CIPHERTRUST_MANAGER` | SYSLOG + CEF + JSON, SYSLOG + JSON | [2026-08-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ciphertrust-manager-changelog)  
[CircleCI](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/circleci) | Automation and DevOps Tools | `CIRCLECI` | CSV + JSON | [2026-08-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/circleci-changelog)  
[Cisco Application Control Engine](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ace) | Load Balancer, Traffic Shaper, ADC | `CISCO_ACE` | SYSLOG | [2022-09-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ace-changelog)  
[Cisco Application Centric Infrastructure](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-aci) | CISCO ACI | `CISCO_ACI` | JSON, SYSLOG | [2026-04-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-aci-changelog)  
[Cisco ACS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-acs) | Authentication | `CISCO_ACS` | SYSLOG + KV , JSON + KV + SYSLOG | [2026-08-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-acs-changelog)  
[Cisco AMP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-amp) | AV / Endpoint | `CISCO_AMP` | JSON | [2025-10-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-amp-changelog)  
[Cisco APIC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-apic) | Software-defined Networking (SDN) | `CISCO_APIC` | SYSLOG | [2024-11-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-apic-changelog)  
[Cisco ASA](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-asa-firewall) | firewall | `CISCO_ASA_FIREWALL` | SYSLOG | [2026-09-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-asa-firewall-changelog)  
[Cisco Call Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-call-manager) | NETWORKING | `CISCO_CALL_MANAGER` | SYSLOG | [2024-10-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-call-manager-changelog)  
[Cisco CloudLock](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-cloudlock-casb) | CASB | `CISCO_CLOUDLOCK_CASB` | JSON | 2021-10-04  
[Cisco CTS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-cts) | Telephone Software | `CISCO_CTS` | SYSLOG + KV | 2021-05-20  
Cisco DHCP | DHCP | `CISCO_DHCP` | SYSLOG + CSV | 2022-02-07  
[Cisco DNA Center Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-dnac) | Network Management and Optimization | `CISCO_DNAC` | SYSLOG+JSON | [2025-08-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-dnac-changelog)  
[Cisco Email Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-email-security) | Email Server | `CISCO_EMAIL_SECURITY` | SYSLOG + KV, JSON | [2026-09-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-email-security-changelog)  
[Cisco EStreamer](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-estreamer) | Network Monitoring | `CISCO_ESTREAMER` | SYSLOG + KV | [2025-03-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-estreamer-changelog)  
[Cisco Firepower NGFW](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-firepower-firewall) | Firewall | `CISCO_FIREPOWER_FIREWALL` | SYSLOG + KV, SYSLOG + JSON, JSON, SYSLOG | [2026-09-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-firepower-firewall-changelog)  
[Cisco FireSIGHT Management Center](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-firesight) | SaaS Application | `CISCO_FIRESIGHT` | KV, SYSLOG+KV,SYSLOG | [2026-08-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-firesight-changelog)  
[Cisco Firewall Services Module](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-fwsm) | Firewall | `CISCO_FWSM` | SYSLOG | [2025-10-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-fwsm-changelog)  
[Cisco Internetwork Operating System](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ios) | OS logs | `CISCO_IOS` | SYSLOG , SYSLOG+KV, SYSLOG+JSON | [2026-05-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ios-changelog)  
[Cisco IronPort](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ironport) | Gateway Security | `CISCO_IRONPORT` | SYSLOG + CSV, SYSLOG | [2026-09-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ironport-changelog)  
[Cisco ISE](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ise) | Identity and Access Management | `CISCO_ISE` | SYSLOG , CSV, JSON | [2026-07-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ise-changelog)  
[Cisco Meraki](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-meraki) | Wireless | `CISCO_MERAKI` | SYSLOG, JSON | [2026-08-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-meraki-changelog)  
Cisco NX-OS | OS | `CISCO_NX_OS` | SYSLOG | [2025-07-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-nx-os-changelog)  
[Cisco PIX Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-pix-firewall) | Firewall | `CISCO_PIX_FIREWALL` | SYSLOG | [2025-12-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-pix-firewall-changelog)  
[Cisco Prime](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-prime) | Network Management and Optimization | `CISCO_PRIME` | SYSLOG | [2025-04-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-prime-changelog)  
[Cisco Router](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-router) | Switches, Routers | `CISCO_ROUTER` | SYSLOG, SYSLOG+KV | [2026-07-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-router-changelog)  
[Cisco vManage SD-WAN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-sdwan) | Switches and Routers | `CISCO_SDWAN` | JSON, SYSLOG | [2026-06-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-sdwan-changelog)  
[Cisco Secure Access](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-secure-access) | Remote Access Tools | `CISCO_SECURE_ACCESS` | CSV | [2026-06-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-secure-access-changelog)  
[Cisco Secure Workload](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-secure-workload) | AV and Endpoint | `CISCO_SECURE_WORKLOAD` | JSON, KV, SYSLOG, SYSLOG+KV+JSON | [2026-05-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-secure-workload-changelog)  
[Cisco Vision Dynamic Signage Director](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-stadiumvision) | Content and Delivery Management | `CISCO_STADIUMVISION` | SYSLOG, SYSLOG+KV | [2026-08-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-stadiumvision-changelog)  
[Cisco Stealthwatch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-stealthwatch) | Log Aggregator | `CISCO_STEALTHWATCH` | JSON, CEF | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-stealthwatch-changelog)  
[Cisco Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-switch) | Switches, Routers | `CISCO_SWITCH` | SYSLOG | [2026-07-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-switch-changelog)  
Cisco TACACS+ | Authentication | `CISCO_TACACS` | SYSLOG + KV | [2026-06-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-tacacs-changelog)  
Cisco UCM | Communication Manager | `CISCO_UCM` | SYSLOG + KV | [2026-07-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ucm-changelog)  
[Cisco UCS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ucs) | OS logs | `CISCO_UCS` | SYSLOG | [2022-07-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ucs-changelog)  
[Cisco Umbrella Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-umbrella-audit) | Firewall and Security Management | `CISCO_UMBRELLA_AUDIT` | CSV | [2026-08-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-umbrella-audit-changelog)  
Cisco Umbrella SWG DLP | DLP | `CISCO_UMBRELLA_SWG_DLP` | CSV | [2025-10-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-umbrella-swg-dlp-changelog)  
Cisco Unity Connection | Administration and Management | `CISCO_UNITY_CONNECTION` | SYSLOG + KV | [2025-05-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-unity-connection-changelog)  
[Cisco VCS Expressway](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-vcs) | Telephone software | `CISCO_VCS` | SYSLOG | [2025-08-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-vcs-changelog)  
[Cisco VPN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-vpn) | VPN | `CISCO_VPN` | SYSLOG | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-vpn-changelog)  
[Cisco Wireless IPS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wips) | Cisco Wips | `CISCO_WIPS` | SYSLOG + KV | [2023-11-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wips-changelog)  
[Cisco WLC/WCS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless) | Wireless | `CISCO_WIRELESS` | SYSLOG | [2026-09-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wireless-changelog)  
[Cisco WSA](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsa) | WSA | `CISCO_WSA` | SYSLOG, SYSLOG+CSV, JSON | [2026-03-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wsa-changelog)  
[Cisco Web Services Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsm) | CISCO_WSM | `CISCO_WSM` | SYSLOG | [2023-10-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wsm-changelog)  
[CIS Albert Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cis-albert-alert) | Alerts | `CIS_ALBERT_ALERT` | SYSLOG, JSON | [2025-05-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cis-albert-alert-changelog)  
[Citrix Analytics](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-analytics) | Monitoring of DaaS | `CITRIX_ANALYTICS` | JSON | [2024-06-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/citrix-analytics-changelog)  
[Citrix Monitor](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-monitor) | Monitoring of DaaS | `CITRIX_MONITOR` | JSON | [2022-11-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/citrix-monitor-changelog)  
[Citrix Netscaler](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-netscaler) | Load Balancer, Traffic Shaper, ADC | `CITRIX_NETSCALER` | SYSLOG + KV | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/citrix-netscaler-changelog)  
[Citrix Storefront](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-storefront) | Remote Access Tools | `CITRIX_STOREFRONT` | JSON | [2025-02-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/citrix-storefront-changelog)  
[ClamAV](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/clam-av) | AV / Endpoint | `CLAM_AV` | JSON | 2022-02-07  
[Claroty Continuous Threat Detection](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/claroty-ctd) | IoT | `CLAROTY_CTD` | KV, SYSLOG | [2026-02-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claroty-ctd-changelog)  
Claroty Enterprise Management Console | Cyber Security | `CLAROTY_EMC` | SYSLOG+KV | [2026-02-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claroty-emc-changelog)  
[Claroty Xdome](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/claroty-xdome) | SaaS Applications | `CLAROTY_XDOME` | SYSLOG , JSON , KV, CEF | [2026-08-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claroty-xdome-changelog)  
Claude Compliance Logs | Application server logs | `CLAUDE_COMPLIANCE_LOGS` | JSON, Syslog + JSON | [2026-09-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claude-compliance-logs-changelog)  
[HP Aruba (ClearPass)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/clearpass) | Identity and Access Management | `CLEARPASS` | SYSLOG + KV, JSON + SYSLOG | [2026-08-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/clearpass-changelog)  
Clearswift | Information Security | `CLEARSWIFT` | SYSLOG | [2023-11-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/clearswift-changelog)  
[Cloudflare](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare) | SaaS Application | `CLOUDFLARE` | JSON | [2026-08-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-changelog)  
Cloudflare Audit | SaaS Application | `CLOUDFLARE_AUDIT` | JSON | [2026-08-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-audit-changelog)  
Cloudflare Network Analytics | SaaS Application | `CLOUDFLARE_NETWORK_ANALYTICS` | JSON | [2025-09-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-network-analytics-changelog)  
[Cloudflare Pageshield](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare-pageshield) | OS Logs | `CLOUDFLARE_PAGESHIELD` | JSON | [2025-03-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-pageshield-changelog)  
[Cloudflare WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare-waf) | Cloud Log | `CLOUDFLARE_WAF` | JSON | [2026-01-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-waf-changelog)  
Cloudflare Warp | Data Security | `CLOUDFLARE_WARP` | JSON | [2026-05-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-warp-changelog)  
[CloudGenix SD-WAN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudgenix-sdwan) | Switches, Routers | `CLOUDGENIX_SDWAN` | SYSLOG + KV | [2022-09-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudgenix-sdwan-changelog)  
[Cloudian hyperstore](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudian-hyperstore) | Storage Solutions | `CLOUDIAN_HYPERSTORE` | SYSLOG | 2021-05-05  
[CloudM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudm) | Identity and Access Management | `CLOUDM` | JSON | [2022-06-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudm-changelog)  
[Google Cloud Identity Context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-identity-context) | Identity and Access Management | `CLOUD_IDENTITY_CONTEXT` | JSON | [2024-12-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloud-identity-context-changelog)  
[Cloud Passage](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-passage) | SaaS Application | `CLOUD_PASSAGE` | JSON | [2022-06-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloud-passage-changelog)  
[Code42 Incydr](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/code42-incydr) | Data loss prevention (DLP) | `CODE42_INCYDR` | JSON | [2026-03-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/code42-incydr-changelog)  
[Cofense](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cofense-triage) | Email Server | `COFENSE_TRIAGE` | SYSLOG + KV (CEF) | [2024-06-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cofense-triage-changelog)  
[Cohesity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cohesity) | Backup Software | `COHESITY` | SYSLOG | [2024-09-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cohesity-changelog)  
[Comforte SecurDPS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/comforte-securdps) | Data loss prevention | `COMFORTE_SECURDPS` | SYSLOG + KV, JSON | [2024-06-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/comforte-securdps-changelog)  
[CommVault](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/commvault) | Alert System | `COMMVAULT` | KV , SYSLOG | [2026-06-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/commvault-changelog)  
CommVault Commcell | Alert System | `COMMVAULT_COMMCELL` | KV , SYSLOG | [2024-01-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/commvault-commcell-changelog)  
[Comodo](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/comodo-av) | AV / Endpoint | `COMODO_AV` | SYSLOG + KV (CEF) | 2021-04-09  
[Corelight](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/corelight) | NDR | `CORELIGHT` | JSON | [2026-10-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/corelight-changelog)  
[Palo Alto Cortex XDR Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cortex-xdr) | NDR | `CORTEX_XDR` | JSON, SYSLOG + KV | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cortex-xdr-changelog)  
[COVID-19 Cyber Threat Coalition](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/covid-ctc-ioc) | IOC | `COVID_CTC_IOC` | Value Entry | 2020-06-02  
[Cribl Stream](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cribl-stream) | Log Aggregation and SIEM Systems | `CRIBL_STREAM` | JSON | [2024-06-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cribl-stream-changelog)  
[Crowdstrike IOC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crowdstrike-ioc) | IOC | `CROWDSTRIKE_IOC` | JSON | [2026-08-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/crowdstrike-ioc-changelog)  
[CrushFTP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crushftp) | Application server | `CRUSHFTP` | SYSLOG+KV | [2025-01-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/crushftp-changelog)  
[Citrix Receiver](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/csg-citrix-rx) | Application Server Logs | `CSG_CITRIX_RX` | CSV | [2025-03-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/csg-citrix-rx-changelog)  
[CSV Custom IOC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/csv-custom-ioc) | IOC | `CSV_CUSTOM_IOC` | CSV | [2025-08-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/csv-custom-ioc-changelog)  
CrowdStrike Alerts API | EDR | `CS_ALERTS` | JSON | [2026-10-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-alerts-changelog)  
CrowdStrike Detection Monitoring | EDR | `CS_DETECTS` | JSON | [2026-02-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-detects-changelog)  
[CrowdStrike Falcon](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-edr) | EDR | `CS_EDR` | JSON | [2026-08-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-edr-changelog)  
[CrowdStrike Filevantage](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-filevantage) | IT infrastructure | `CS_FILEVANTAGE` | JSON | [2025-04-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-filevantage-changelog)  
[Crowdstrike Identity Protection Services](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-idp) | AV AND ENDPOINT LOGS | `CS_IDP` | JSON | [2025-01-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-idp-changelog)  
[CrowdStrike Falcon Stream](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-stream) | Alerts | `CS_STREAM` | KV (LEEF, CEF), JSON | [2026-08-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-stream-changelog)  
Cyware Threat Intelligence Exchange | Threat Intelligence | `CTIX` | JSON | [2026-08-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ctix-changelog)  
[Colinet Trotta GAUS SEGUROS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ct-gaus-seguros) | Alert | `CT_GAUS_SEGUROS` | CSV | [2024-12-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ct-gaus-seguros-changelog)  
[Custom Application Access Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-application-access) | Security | `CUSTOM_APPLICATION_ACCESS` | JSON | [2025-02-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/custom-application-access-changelog)  
[Custom DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-dns) | DNS | `CUSTOM_DNS` | JSON | [2022-08-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/custom-dns-changelog)  
[Custom Security Data Analytics](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-security-data-analytics) | Log Aggregation | `CUSTOM_SECURITY_DATA_ANALYTICS` | JSON | [2025-05-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/custom-security-data-analytics-changelog)  
[CyberArk](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark) | Privilege Account Management | `CYBERARK` | KV (CEF), JSON, SYSLOG+KV | [2026-09-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-changelog)  
[CyberArk Endpoint Privilege Manager (EPM)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-epm) | EPM | `CYBERARK_EPM` | JSON | [2025-09-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-epm-changelog)  
[CyberArk Privileged Access Manager (PAM)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-pam) | CyberArk Privileged Access Manager | `CYBERARK_PAM` | SYSLOG, JSON, SYSLOG + KV, JSON + CEF, SYSLOG + JSON, CEF, SYSLOG + CEF | [2026-09-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-pam-changelog)  
[Cyberark Privilege Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-privilege-cloud) | Identity & Access Management | `CYBERARK_PRIVILEGE_CLOUD` | SYSLOG + KV | [2025-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-privilege-cloud-changelog)  
[CyberArk PTA Privileged Threat Analytics](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-pta) | Privileged Account Activity | `CYBERARK_PTA` | SYSLOG + KV (CEF) , LEEF | [2026-07-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-pta-changelog)  
[Cybereason EDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cybereason-edr) | EDR | `CYBEREASON_EDR` | JSON | [2026-02-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cybereason-edr-changelog)  
[Cybergatekeeper NAC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cybergatekeeper-nac) | Security | `CYBERGATEKEEPER_NAC` | SYSLOG + KV | [2024-04-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cybergatekeeper-nac-changelog)  
[Microsoft CyberX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberx) | IoT | `CYBERX` | SYSLOG+KV | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberx-changelog)  
[Cyber 2.0 IDS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyber-2-ids) | IDS | `CYBER_2_IDS` | SYSLOG+JSON | [2025-09-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyber-2-ids-changelog)  
CYJAX Threat Intelligence | Threat Intelligence | `CYJAX_THREAT_INTELLIGENCE` | JSON | [2026-03-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyjax-threat-intelligence-changelog)  
[Cylance Protect](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cylance-protect) | Alerts | `CYLANCE_PROTECT` | SYSLOG + KV | [2025-05-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cylance-protect-changelog)  
[Cynet 360 AutoXDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cynet-360-autoxdr) | AV and endpoint logs | `CYNET_360_AUTOXDR` | JSON / CEF | [2026-06-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cynet-360-autoxdr-changelog)  
[Cyolo Secure Remote Access for OT](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyolo-ot) | Remote Access Tools | `CYOLO_OT` | SYSLOG + KV , SYSLOG + KV + JSON | [2025-12-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyolo-ot-changelog)  
[D3 Banking](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/d3-banking) | BANKING | `D3_BANKING` | JSON | [2022-03-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/d3-banking-changelog)  
[Darktrace](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/darktrace) | NDR | `DARKTRACE` | SYSLOG + KV (CEF), SYSLOG + JSON | [2026-09-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/darktrace-changelog)  
Databricks | Storage solutions | `DATABRICKS` | JSON | [2026-03-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/databricks-changelog)  
[Datadog](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/datadog) | NDR | `DATADOG` | JSON | [2025-08-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/datadog-changelog)  
[Dataminr Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dataminr-alert) | SAAS Security Application | `DATAMINR_ALERT` | JSON | [2024-02-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dataminr-alert-changelog)  
[Datto File Protection](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/datto-file-protection) | DATTO_FILE_PROTECTION | `DATTO_FILE_PROTECTION` | SYSLOG | [2022-08-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/datto-file-protection-changelog)  
[IBM DB2](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/db2-db) | Database | `DB2_DB` | LEEF,Syslog+KV,JSON | [2026-07-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/db2-db-changelog)  
[Deep Instinct EDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/deep-instinct-edr) | EDR | `DEEP_INSTINCT_EDR` | LEEF | [2023-12-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/deep-instinct-edr-changelog)  
[Delinea Distributed Engine](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-distributed-engine) | Application server logs | `DELINEA_DISTRIBUTED_ENGINE` | SYSLOG | [2024-12-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/delinea-distributed-engine-changelog)  
[Delinea PAM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-pam) | Access Management | `DELINEA_PAM` | SYSLOG + CSV | [2023-11-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/delinea-pam-changelog)  
[Delinea Secret Server](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-secret-server) | Privileged Account Activity | `DELINEA_SECRET_SERVER` | KV | [2025-12-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/delinea-secret-server-changelog)  
[Dell CyberSense](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-cybersense) | Data Security | `DELL_CYBERSENSE` | SYSLOG | [2025-02-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-cybersense-changelog)  
[Dell ECS Enterprise Object Storage](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-ecs) | ECS | `DELL_ECS` | SYSLOG | [2026-01-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-ecs-changelog)  
[Dell EMC Data Domain](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-data-domain) | Storage system | `DELL_EMC_DATA_DOMAIN` | SYSLOG + KV | [2026-08-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-emc-data-domain-changelog)  
[Dell EMC Isilon NAS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-nas) | Storage | `DELL_EMC_NAS` | SYSLOG | [2023-07-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-emc-nas-changelog)  
[Dell EMC PowerStore](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-powerstore) | DATA STORAGE | `DELL_EMC_POWERSTORE` | SYSLOG + KV | [2024-11-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-emc-powerstore-changelog)  
[Dell OpenManage](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-openmanage) | Systems Management Application | `DELL_OPENMANAGE` | SYSLOG + KV | [2025-05-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-openmanage-changelog)  
[Dell Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-switch) | Switches, Routers | `DELL_SWITCH` | SYSLOG | [2026-05-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-switch-changelog)  
[Desynova Contido](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/desynova-contido) | Switches | `DESYNOVA_CONTIDO` | SYSLOG + JSON | [2023-09-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/desynova-contido-changelog)  
[Department of Homeland Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dhs-ioc) | Threat detection | `DHS_IOC` | XML | [2023-07-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dhs-ioc-changelog)  
[Digicert](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digicert) | IT infrastructure | `DIGICERT` | JSON | [2025-02-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digicert-changelog)  
[DigitalArts i-Filter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalarts-ifilter) | Web Proxy | `DIGITALARTS_IFILTER` | SYSLOG | [2025-10-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digitalarts-ifilter-changelog)  
[Digital Guardian DLP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalguardian-dlp) | DLP | `DIGITALGUARDIAN_DLP` | JSON,SYSLOG+XML | [2025-03-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digitalguardian-dlp-changelog)  
[Digital Guardian EDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalguardian-edr) | EDR | `DIGITALGUARDIAN_EDR` | KV | [2025-11-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digitalguardian-edr-changelog)  
[Digital Shadows Indicators](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-ioc) | IOC | `DIGITAL_SHADOWS_IOC` | JSON | 2022-04-23  
[Digital Shadows SearchLight](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-searchlight) | Threat Intelligence | `DIGITAL_SHADOWS_SEARCHLIGHT` | JSON | 2022-05-02  
[Digi modems](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digi-modems) | Switches and Routers | `DIGI_MODEMS` | SYSLOG | [2023-06-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digi-modems-changelog)  
[DMP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dmp-entre) | Physical Security | `DMP_ENTRE` | SYSLOG | 2020-09-23  
[DNSFilter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dnsfilter) | Data Transfer | `DNSFILTER` | CSV | [2023-10-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dnsfilter-changelog)  
[DomainTools Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/domaintools-threatintel) | Threat intelligence | `DOMAINTOOLS_THREATINTEL` | JSON | [2023-12-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/domaintools-threatintel-changelog)  
[Dope Security SWG](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dope-swg) | Secure Access Service Edge | `DOPE_SWG` | CSV,JSON | [2025-03-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dope-swg-changelog)  
[Druva Backup](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/druva-backup) | Security | `DRUVA_BACKUP` | JSON | [2024-12-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/druva-backup-changelog)  
Dummy LogType | DNS | `DUMMY_LOGTYPE` | CSV | [2024-07-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dummy-logtype-changelog)  
[Duo Activity Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-activity) | Activity | `DUO_ACTIVITY` | JSON | [2024-08-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/duo-activity-changelog)  
[Duo Administrator Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-admin) | Authentication | `DUO_ADMIN` | JSON | [2026-06-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/duo-admin-changelog)  
[Duo Auth](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-auth) | Authentication | `DUO_AUTH` | JSON | [2026-03-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/duo-auth-changelog)  
[Duo Entity context data](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-context) | Identity and Access Management | `DUO_CONTEXT` | JSON | 2022-03-14  
[Duo Telephony Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-telephony) | Identity and Access Management | `DUO_TELEPHONY` | JSON | [2023-08-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/duo-telephony-changelog)  
[Duo User Context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-user-context) | Identity and Access Management | `DUO_USER_CONTEXT` | JSON | [2024-05-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/duo-user-context-changelog)  
[Edgio WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/edgio-waf) | Web Application Firewall | `EDGIO_WAF` | JSON | [2025-02-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/edgio-waf-changelog)  
[EfficientIP DDI](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/efficientip-ddi) | Network | `EFFICIENTIP_DDI` | SYSLOG + KV | [2026-07-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/efficientip-ddi-changelog)  
[Elastic Audit Beats](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-auditbeat) | ALERTING | `ELASTIC_AUDITBEAT` | JSON | [2026-04-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-auditbeat-changelog)  
[Elastic Defend](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-defend) | Network Monitoring | `ELASTIC_DEFEND` | JSON | [2026-03-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-defend-changelog)  
[Elastic Packet Beats](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-packetbeats) | Log Aggregator | `ELASTIC_PACKETBEATS` | SYSLOG + JSON , JSON | [2025-02-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-packetbeats-changelog)  
[Elastic Search](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-search) | Log Aggregator | `ELASTIC_SEARCH` | JSON | [2023-11-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-search-changelog)  
[Elastic Windows Event Log Beats](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-winlogbeat) | Log Aggregator | `ELASTIC_WINLOGBEAT` | SYSLOG + JSON, JSON + XML, JSON | [2026-06-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-winlogbeat-changelog)  
[CoSoSys Protector](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/endpoint-protector-dlp) | Endpoint Detection | `ENDPOINT_PROTECTOR_DLP` | SYSLOG + KV | [2025-09-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/endpoint-protector-dlp-changelog)  
[Entrust nShield HSM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/entrust-hsm) | Hardware Security Module | `ENTRUST_HSM` | SYSLOG | [2024-10-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/entrust-hsm-changelog)  
[EPIC Systems](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/epic) | Discovery and Monitoring | `EPIC` | LEEF + KV | [2026-04-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/epic-changelog)  
[Ergon Informatik Airlock IAM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ergon-informatik-airlock-iam) | Application Whitelisting | `ERGON_INFORMATIK_AIRLOCK_IAM` | SYSLOG | [2024-08-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ergon-informatik-airlock-iam-changelog)  
[ESET AV](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-av) | ESET_AV | `ESET_AV` | SYSLOG + JSON | [2026-08-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/eset-av-changelog)  
[ESET](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-edr) | EDR | `ESET_EDR` | SYSLOG + JSON | [2025-08-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/eset-edr-changelog)  
[ESET Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-ioc) | IOC | `ESET_IOC` | JSON | [2023-10-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/eset-ioc-changelog)  
[Emerging Threats Pro](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/et-pro-ioc) | IOC | `ET_PRO_IOC` | CSV | [2022-11-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/et-pro-ioc-changelog)  
[Evision FircoSoft](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/evision-fircosoft) | Infrastructure | `EVISION_FIRCOSOFT` | SYSLOG | [2023-10-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/evision-fircosoft-changelog)  
[Microsoft Exchange](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/exchange-mail) | Email Server | `EXCHANGE_MAIL` | SYSLOG | [2025-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/exchange-mail-changelog)  
[ExtraHop RevealX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop) | Firewall IDS/IPS | `EXTRAHOP` | JSON, SYSLOG | [2025-12-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/extrahop-changelog)  
[ExtraHop DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop-dns) | DNS | `EXTRAHOP_DNS` | JSON | 2021-12-13  
[Extreme Networks Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-switch) | Security | `EXTREME_SWITCH` | SYSLOG | [2025-09-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/extreme-switch-changelog)  
[Extreme Wireless](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-wireless) | Network Management and Optimization software | `EXTREME_WIRELESS` | SYSLOG | [2025-11-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/extreme-wireless-changelog)  
[F5 Advanced Firewall Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-afm) | Firewall | `F5_AFM` | SYSLOG + CSV, SYSLOG + KV | [2026-08-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-afm-changelog)  
[F5 ASM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-asm) | WAF | `F5_ASM` | SYSLOG, CSV, JSON, SYSLOG + KV, CEF, JSON + XML | [2026-07-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-asm-changelog)  
[F5 BIGIP Access Policy Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-apm) | Access Policy Manager | `F5_BIGIP_APM` | SYSLOG, JSON | [2026-04-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-bigip-apm-changelog)  
[F5 BIGIP LTM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-ltm) | Load Balancer, Traffic Shaper, ADC | `F5_BIGIP_LTM` | SYSLOG, KV, CSV, JSON+SYSLOG, JSON, SYSLOG+KV | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-bigip-ltm-changelog)  
[F5 Distributed Cloud Services](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-dcs) | SaaS Applications | `F5_DCS` | JSON | [2026-04-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-dcs-changelog)  
[F5 DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-dns) | DNS | `F5_DNS` | SYSLOG | [2026-02-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-dns-changelog)  
[F5 Shape](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-shape) | Security log | `F5_SHAPE` | JSON | [2026-08-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-shape-changelog)  
[F5 Silverline](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-silverline) | Application | `F5_SILVERLINE` | SYSLOG, SYSLOG + KV , JSON | [2025-11-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-silverline-changelog)  
[F5 VPN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-vpn) | VPN | `F5_VPN` | SYSLOG, KV | [2026-09-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-vpn-changelog)  
[Falco IDS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/falco-ids) | IDS/IPS | `FALCO_IDS` | JSON | [2024-03-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/falco-ids-changelog)  
[Fastly CDN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fastly-cdn) | WAF | `FASTLY_CDN` | JSON | [2026-07-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fastly-cdn-changelog)  
[Fastly WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fastly-waf) | WAF | `FASTLY_WAF` | JSON | [2025-05-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fastly-waf-changelog)  
[Fidelis Network](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fidelis-network) | NDR | `FIDELIS_NETWORK` | SYSLOG + KV, JSON | [2025-08-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fidelis-network-changelog)  
[FileZilla](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/filezilla-ftp) | File tranfser | `FILEZILLA_FTP` | SYSLOG | [2024-06-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/filezilla-ftp-changelog)  
[File Scanning Framework](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/file-scanning-framework) | File scanning | `FILE_SCANNING_FRAMEWORK` | JSON | 2021-09-27  
[FingerprintJS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fingerprint-js) | Vulnerability scanners | `FINGERPRINT_JS` | JSON | [2024-11-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fingerprint-js-changelog)  
[FireEye](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-alert) | Alerts | `FIREEYE_ALERT` | SYSLOG + JSON, JSON, KV, SYSLOG | [2025-08-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-alert-changelog)  
[FireEye eMPS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-emps) | Email server log types. | `FIREEYE_EMPS` | JSON, CEF, SYSLOG+KV | [2026-08-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-emps-changelog)  
[FireEye ETP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-etp) | Email Server | `FIREEYE_ETP` | JSON + SYSLOG | [2026-06-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-etp-changelog)  
[FireEye HX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx) | EDR | `FIREEYE_HX` | JSON,SYSLOG | [2026-08-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-hx-changelog)  
[FireEye HX Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx-audit) | Audits | `FIREEYE_HX_AUDIT` | XML | [2023-05-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-hx-audit-changelog)  
[FireEye NX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx) | NDR | `FIREEYE_NX` | JSON, SYSLOG+KV, SYSLOG+JSON | [2026-10-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-nx-changelog)  
[FireEye NX Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx-audit) | AUDIT | `FIREEYE_NX_AUDIT` | Syslog | [2024-05-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-nx-audit-changelog)  
[FireEye PX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-px) | Firewall | `FIREEYE_PX` | JSON | [2024-01-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-px-changelog)  
[Fivetran](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fivetran) | SIEM Systems | `FIVETRAN` | JSON | [2024-06-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fivetran-changelog)  
[Fluentd Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fluentd) | Log Aggregator | `FLUENTD` | SYSLOG + JSON | [2025-10-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fluentd-changelog)  
[Forcepoint CASB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-casb) | CASB | `FORCEPOINT_CASB` | SYSLOG + CEF | [2022-08-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-casb-changelog)  
[Forcepoint DLP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-dlp) | Forcepoint DLP | `FORCEPOINT_DLP` | CEF, Syslog | [2026-09-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-dlp-changelog)  
[Forcepoint Email Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-emailsecurity) | Email Server | `FORCEPOINT_EMAILSECURITY` | JSON | [2025-12-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-emailsecurity-changelog)  
[Forcepoint NGFW](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-firewall) | Network | `FORCEPOINT_FIREWALL` | SYSLOG+JSON, SYSLOG+KV | [2026-02-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-firewall-changelog)  
[Forcepoint Mail Relay](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-mail-relay) | Email Server | `FORCEPOINT_MAIL_RELAY` | JSON | [2025-04-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-mail-relay-changelog)  
[Forcepoint Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-webproxy) | Web Proxy | `FORCEPOINT_WEBPROXY` | SYSLOG + KV (CEF), LEEF, CSV | [2026-08-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-webproxy-changelog)  
[Forescout eyeInspect](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forescout-eyeinspect) | Network Monitoring | `FORESCOUT_EYEINSPECT` | SYSLOG, CEF | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forescout-eyeinspect-changelog)  
[Forescout NAC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forescout-nac) | NAC | `FORESCOUT_NAC` | SYSLOG, CEF, JSON | [2026-03-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forescout-nac-changelog)  
[ForgeRock Identity Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-identity-cloud) | Cloud Security | `FORGEROCK_IDENTITY_CLOUD` | JSON | [2026-03-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forgerock-identity-cloud-changelog)  
[Forgerock OpenIdM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-openidm) | DATA SECURITY | `FORGEROCK_OPENIDM` | JSON | [2025-02-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forgerock-openidm-changelog)  
[Forseti Open Source](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forseti) | Google Cloud Specific | `FORSETI` | JSON | 2021-12-23  
[Fortinet](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-dhcp) | DHCP | `FORTINET_DHCP` | KV | [2022-11-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-dhcp-changelog)  
[FortiGate](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-firewall) | FIREWALL | `FORTINET_FIREWALL` | SYSLOG+KV, CEF | [2026-07-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-firewall-changelog)  
[Fortinet FortiAnalyzer](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortianalyzer) | Fortinet FortiAnalyzer | `FORTINET_FORTIANALYZER` | JSON, KV, SYSLOG+KV+JSON | [2026-09-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortianalyzer-changelog)  
[Fortinet FortiAuthenticator](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiauthenticator) | Security | `FORTINET_FORTIAUTHENTICATOR` | SYSLOG + KV, KV | [2025-05-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortiauthenticator-changelog)  
[Fortinet FortiClient](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-forticlient) | Security | `FORTINET_FORTICLIENT` | KV | [2026-07-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-forticlient-changelog)  
[Fortinet FortiDDoS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiddos) | Network | `FORTINET_FORTIDDOS` | KV | [2026-07-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortiddos-changelog)  
[Fortinet FortiEDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiedr) | EDR | `FORTINET_FORTIEDR` | SYSLOG + KV | [2026-04-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortiedr-changelog)  
[FortiMail Email Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortimail) | Email Security | `FORTINET_FORTIMAIL` | KV | [2026-05-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortimail-changelog)  
[Fortinet Fortimanager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortimanager) | Network Management and Optimization software. | `FORTINET_FORTIMANAGER` | KV + SYSLOG | [2026-08-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortimanager-changelog)  
[Fortinet FortiNAC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortinac) | NAC | `FORTINET_FORTINAC` | SYSLOG,CSV | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortinac-changelog)  
[Fortinet Web Application Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiweb) | WEB | `FORTINET_FORTIWEB` | KV , KV+SYSLOG | [2026-08-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortiweb-changelog)  
[Fortinet FortiSandbox](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-sandbox) | AV and endpoint logs | `FORTINET_SANDBOX` | SYSLOG + KV | [2026-08-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-sandbox-changelog)  
[Fortinet Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-switch) | Switches and Routers | `FORTINET_SWITCH` | KV | [2026-08-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-switch-changelog)  
[Fortinet Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-webproxy) | Web Proxy | `FORTINET_WEBPROXY` | SYSLOG + KV | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-webproxy-changelog)  
[Fortra Powertech SIEM Agent](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortra-powertech-siem-agent) | STATUS_UPDATE | `FORTRA_POWERTECH_SIEM_AGENT` | SYSLOG, CEF | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortra-powertech-siem-agent-changelog)  
[GCP Abuse Events Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-abuse-events) | Google Cloud Specific | `GCP_ABUSE_EVENTS` | JSON | [2025-08-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-abuse-events-changelog)  
Apigee | Google Cloud Specific | `GCP_APIGEE` | JSON | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-apigee-changelog)  
[Apigee](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-apigee-x) | Google Cloud Specific | `GCP_APIGEE_X` | JSON | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-apigee-x-changelog)  
[GCP_APP_ENGINE](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-app-engine) | Cloud Computing | `GCP_APP_ENGINE` | JSON and KV | [2025-12-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-app-engine-changelog)  
BigQuery | Google Cloud Resources Contexts | `GCP_BIGQUERY_CONTEXT` | JSON | [2024-04-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-bigquery-context-changelog)  
[GCP Cloud Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudaudit) | Google Cloud Specific | `GCP_CLOUDAUDIT` | JSON | [2026-10-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloudaudit-changelog)  
[Cloud Identity Devices](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudidentity-devices) | Google Cloud Specific | `GCP_CLOUDIDENTITY_DEVICES` | JSON | [2024-07-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloudidentity-devices-changelog)  
[Cloud Identity Device Users](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudidentity-deviceusers) | Google Cloud Specific | `GCP_CLOUDIDENTITY_DEVICEUSERS` | JSON | [2023-03-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloudidentity-deviceusers-changelog)  
[Cloud IoT](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudiot) | Google Cloud Specific | `GCP_CLOUDIOT` | JSON | [2022-06-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloudiot-changelog)  
[Cloud SQL](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudsql) | Google Cloud Specific | `GCP_CLOUDSQL` | JSON | [2026-03-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloudsql-changelog)  
GCP_CLOUD_ASSET_INVENTORY | OS Logs | `GCP_CLOUD_ASSET_INVENTORY` | JSON | [2026-05-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloud-asset-inventory-changelog)  
Cloud Functions Context | Google Cloud Specific | `GCP_CLOUD_FUNCTIONS_CONTEXT` | JSON | [2023-07-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloud-functions-context-changelog)  
[Cloud NAT](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloud-nat) | Google Cloud Specific | `GCP_CLOUD_NAT` | JSON | [2024-05-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloud-nat-changelog)  
[Compute Engine](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-compute) | Google Cloud Specific | `GCP_COMPUTE` | JSON | [2026-01-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-compute-changelog)  
Compute Context | Google Cloud Specific | `GCP_COMPUTE_CONTEXT` | JSON | [2026-05-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-compute-context-changelog)  
Cloud Data Loss Prevention | Google Cloud Specific | `N/A` | JSON | [2025-01-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-dlp-context-changelog)  
[Cloud DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-dns) | Google Cloud Specific | `GCP_DNS` | JSON | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-dns-changelog)  
[Google Cloud DNS Threat Detector](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-dns-atd) | DNS Security | `GCP_DNS_ATD` | JSON | [2025-07-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-dns-atd-changelog)  
[Firewall Rule Logging](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-firewall) | Google Cloud Specific | `GCP_FIREWALL` | JSON | [2024-05-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-firewall-changelog)  
Google Cloud IAM Analysis | Google Cloud Resources Contexts | `GCP_IAM_ANALYSIS` | JSON | [2023-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-iam-analysis-changelog)  
IAM Context | Google Cloud Specific | `GCP_IAM_CONTEXT` | JSON | [2024-03-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-iam-context-changelog)  
[Cloud Intrusion Detection System](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-ids) | Google Cloud Specific | `GCP_IDS` | JSON | [2026-08-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-ids-changelog)  
GCP_KUBERNETES_CONTEXT | Computer Inventory | `GCP_KUBERNETES_CONTEXT` | JSON | [2023-07-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-kubernetes-context-changelog)  
[Cloud Load Balancing](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-loadbalancing) | Google Cloud Specific | `GCP_LOADBALANCING` | JSON | [2026-06-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-loadbalancing-changelog)  
GCP_MODEL_ARMOR | GCP-specific log types | `GCP_MODEL_ARMOR` | JSON | [2026-04-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-model-armor-changelog)  
[GCP_MONITORING_ALERTS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-monitoring-alerts) | Application server logs | `GCP_MONITORING_ALERTS` | JSON | [2026-01-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-monitoring-alerts-changelog)  
GCP_NETWORK_CONNECTIVITY | Computer Inventory | `GCP_NETWORK_CONNECTIVITY_CONTEXT` | JSON | [2023-06-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-network-connectivity-context-changelog)  
[NGFW Enterprise](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-ngfw-enterprise) | Google Cloud Specific | `GCP_NGFW_ENTERPRISE` | JSON | [2026-04-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-ngfw-enterprise-changelog)  
[reCAPTCHA Enterprise](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-recaptcha-enterprise) | Access Management | `GCP_RECAPTCHA_ENTERPRISE` | JSON | [2024-02-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-recaptcha-enterprise-changelog)  
Resource Manager Context | Google Cloud Specific | `GCP_RESOURCE_MANAGER_CONTEXT` | JSON | [2023-07-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-resource-manager-context-changelog)  
Cloud Run | Google Cloud Specific | `GCP_RUN` | JSON | [2026-08-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-run-changelog)  
Security Command Center Chokepoint | Google Cloud Specific | `GCP_SECURITYCENTER_CHOKEPOINT` | JSON | [2025-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-chokepoint-changelog)  
Security Command Center Error | Google Cloud Specific | `GCP_SECURITYCENTER_ERROR` | JSON | [2026-03-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-error-changelog)  
Security Command Center External Exposure | Google Cloud Specific | `GCP_SECURITYCENTER_EXTERNAL_EXPOSURE` | JSON | [2026-07-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-external-exposure-changelog)  
Security Command Center Misconfiguration | Google Cloud Specific | `GCP_SECURITYCENTER_MISCONFIGURATION` | JSON | [2026-03-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-misconfiguration-changelog)  
Security Command Center Observation | Google Cloud Specific | `GCP_SECURITYCENTER_OBSERVATION` | JSON | [2026-03-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-observation-changelog)  
[Security Command Center Posture Violation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-securitycenter-posture-violation) | Google Cloud Specific | `GCP_SECURITYCENTER_POSTURE_VIOLATION` | JSON | [2025-11-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-posture-violation-changelog)  
Security Command Center Secret | Google Cloud Specific | `GCP_SECURITYCENTER_SECRET` | JSON | [2026-06-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-secret-changelog)  
Security Command Center Sensitive Data Risk | Google Cloud Specific | `GCP_SECURITYCENTER_SENSITIVE_DATA_RISK` | JSON | [2025-11-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-sensitive-data-risk-changelog)  
Security Command Center Threat | Google Cloud Specific | `GCP_SECURITYCENTER_THREAT` | JSON | [2026-10-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-threat-changelog)  
Security Command Center Toxic Combination | Google Cloud Specific | `GCP_SECURITYCENTER_TOXIC_COMBINATION` | JSON | [2026-02-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-toxic-combination-changelog)  
Security Command Center Unspecified | Google Cloud Specific | `GCP_SECURITYCENTER_UNSPECIFIED` | JSON | [2026-05-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-unspecified-changelog)  
Security Command Center Vulnerability | Google Cloud Specific | `GCP_SECURITYCENTER_VULNERABILITY` | JSON | [2026-03-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-vulnerability-changelog)  
Cloud SQL Context | Google Cloud Specific | `GCP_SQL_CONTEXT` | JSON | [2023-07-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-sql-context-changelog)  
Cloud Storage Context | Google Cloud Specific | `GCP_STORAGE_CONTEXT` | JSON | [2024-05-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-storage-context-changelog)  
[GCP Secure Web Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-swp) | CLOUD | `GCP_SWP` | JSON | [2026-09-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-swp-changelog)  
Google Threat Intelligence | Threat Intel | `GCP_THREATINTEL` | JSON | [2025-11-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-threatintel-changelog)  
[VPC Flow Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-vpc-flow) | Google Cloud Specific | `GCP_VPC_FLOW` | JSON | [2026-09-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-vpc-flow-changelog)  
Gemini Code Assist | Google Cloud Specific | `GEMINI_CODE_ASSIST` | JSON | [2026-09-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gemini-code-assist-changelog)  
[GitGuardian Enterprise](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gitguardian-enterprise) | SaaS Applications | `GITGUARDIAN_ENTERPRISE` | JSON | [2024-10-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gitguardian-enterprise-changelog)  
[GitHub](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/github) | SaaS Application | `GITHUB` | JSON,SYSLOG, SYSLOG+JSON, SYSLOG+KV, KV | [2026-06-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/github-changelog)  
GitHub Dependabot | Application server logs | `GITHUB_DEPENDABOT` | JSON | [2025-12-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/github-dependabot-changelog)  
[Gitlab](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gitlab) | SAAS | `GITLAB` | JSON,SYSLOG + JSON | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gitlab-changelog)  
[GMAIL Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gmail-logs) | Google Cloud Specific | `GMAIL_LOGS` | JSON | [2024-05-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gmail-logs-changelog)  
GMV Checker ATM Security | ATM Audit | `GMV_CHECKER` | SYSLOG, SYSLOG + KV | [2025-11-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gmv-checker-changelog)  
GreyNoise | Threat Intel | `GREYNOISE` | JSON | [2026-01-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/greynoise-changelog)  
GTB Technologies DLP | Security | `GTB_DLP` | SYSLOG+KV, SYSLOG+JSON | [2026-05-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gtb-dlp-changelog)  
[AWS GuardDuty](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardduty) | IDS/IPS | `GUARDDUTY` | JSON | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardduty-changelog)  
[Guardicore Centra](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardicore-centra) | Deception Software | `GUARDICORE_CENTRA` | JSON, SYSLOG+JSON | [2026-04-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardicore-centra-changelog)  
[IBM Guardium](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardium) | Database DLP | `GUARDIUM` | CSV, CEF, LEEF | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardium-changelog)  
[H3C Comware Platform Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/h3c-switch) | Switches, Routers | `H3C_SWITCH` | SYSLOG | [2026-01-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/h3c-switch-changelog)  
[Hackerone](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hackerone) | IT infrastructure | `HACKERONE` | JSON | [2025-02-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hackerone-changelog)  
[Apache Hadoop](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hadoop) | open-source software | `HADOOP` | SYSLOG + KV | [2026-02-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hadoop-changelog)  
[Halcyon Anti Ransomware](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/halcyon) | AV and endpoint logs | `HALCYON` | JSON | [2026-02-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/halcyon-changelog)  
[HAProxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/haproxy) | Load balancing | `HAPROXY` | SYSLOG, SYSLOG+KV | [2026-06-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/haproxy-changelog)  
[Harness IO](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/harness-io) | Automation and DevOps Tools | `HARNESS_IO` | JSON | [2025-04-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/harness-io-changelog)  
[Hashicorp Vault](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hashicorp) | Privileged Account Activity | `HASHICORP` | JSON, SYSLOG, SYSLOG+JSON, SYSLOG+KV | [2025-12-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hashicorp-changelog)  
[HCL BigFix](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hcl-bigfix) | Network Management and Optimization | `HCL_BIGFIX` | JSON | [2023-12-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hcl-bigfix-changelog)  
HCNET Account Adapter Plus | DHCP | `HCNET_ACCOUNT_ADAPTER` | SYSLOG | [2024-11-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hcnet-account-adapter-changelog)  
[HID DigitalPersona](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hid-digitalpersona) | Audit Log | `HID_DIGITALPERSONA` | JSON, SYSLOG + KV | [2024-05-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hid-digitalpersona-changelog)  
[Hillstone Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hillstone-ngfw) | Application server logs | `HILLSTONE_NGFW` | SYSLOG + KV | [2025-02-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hillstone-ngfw-changelog)  
[Hitachi Cloud Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hitachi-cloud-platform) | Hitachi Cloud Platform | `HITACHI_CLOUD_PLATFORM` | SYSLOG | [2023-05-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hitachi-cloud-platform-changelog)  
[Honeyd](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/honeyd) | Deception Software | `HONEYD` | SYSLOG | [2024-05-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/honeyd-changelog)  
[HPE BladeSystem C7000](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-bladesystem-c7000) | BladeSystem C7000 | `HPE_BLADESYSTEM_C7000` | SYSLOG | [2024-04-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hpe-bladesystem-c7000-changelog)  
[HPE ILO](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-ilo) | Server Management | `HPE_ILO` | SYSLOG | [2023-11-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hpe-ilo-changelog)  
[HP Linux](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hp-linux) | OS | `HP_LINUX` | SYSLOG | [2025-10-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hp-linux-changelog)  
[HP Procurve Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hp-procurve) | Switches | `HP_PROCURVE` | SYSLOG | [2025-11-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hp-procurve-changelog)  
[Huawei Switches](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/huawei-switch) | Switches and Routers | `HUAWEI_SWITCH` | JSON+SYSLOG, JSON+KV, SYSLOG+KV, SYSLOG | [2026-08-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/huawei-switch-changelog)  
[HYPR MFA](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hypr-mfa) | Security SSO | `HYPR_MFA` | CSV | [2024-04-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hypr-mfa-changelog)  
[IBM AS/400](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-as400) | Application System | `IBM_AS400` | SYSLOG + KV, SYSLOG + JSON, CSV | [2026-09-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-as400-changelog)  
[IBM CICS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-cics) | Service Bus | `IBM_CICS` | LEEF | 2021-10-27  
IBM Cloud Activity Tracker | Security Log | `IBM_CLOUD_ACTIVITY_TRACKER` | JSON | [2025-05-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-cloud-activity-tracker-changelog)  
IBM DataPower Gateway | API Gateway | `IBM_DATAPOWER` | JSON, SYSLOG, SYSLOG+JSON | [2026-03-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-datapower-changelog)  
IBM DS8000 Storage | Audit Logs | `IBM_DS8000` | Syslog, CSV | [2024-07-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-ds8000-changelog)  
IBM-i Operating System | I Operating System | `IBM_I` | Syslog CEF | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-i-changelog)  
IBM Tape Storages | Monitoring | `IBM_LTO` | Syslog | [2026-06-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-lto-changelog)  
[IBM MaaS360](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-maas360) | Security | `IBM_MAAS360` | JSON | [2024-11-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-maas360-changelog)  
[IBM Mainframe Storage](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-mainframe-storage) | Monitoring | `IBM_MAINFRAME_STORAGE` | SYSLOG | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-mainframe-storage-changelog)  
[IBM OpenPages](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-openpages) | Data Security | `IBM_OPENPAGES` | SYSLOG | [2024-10-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-openpages-changelog)  
[IBM Security QRadar SIEM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-qradar) | Security Log | `IBM_QRADAR` | SYSLOG | [2024-06-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-qradar-changelog)  
IBM Safenet | IT infrastructure | `IBM_SAFENET` | SYSLOG | [2026-03-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-safenet-changelog)  
[IBM Security Access Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sam) | WAF | `IBM_SAM` | SYSLOG | [2026-07-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-sam-changelog)  
IBM Security Verify | Endpoint Security | `IBM_SECURITY_VERIFY` | SYSLOG,SYSLOG+XML | [2024-05-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-security-verify-changelog)  
[IBM Security Verify SaaS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-security-verify-saas) | SaaS Application | `IBM_SECURITY_VERIFY_SAAS` | JSON | [2023-10-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-security-verify-saas-changelog)  
[IBM Security Identity Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sim) | Security | `IBM_SIM` | JSON + KV | [2024-03-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-sim-changelog)  
IBM Security QRadar SOAR | Security | `IBM_SOAR` | SYSLOG + KV | [2024-10-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-soar-changelog)  
[IBM Security Verify Access ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sva) | Security | `IBM_SVA` | Syslog | [2025-08-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-sva-changelog)  
[IBM Tivoli](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-tivoli) | Monitoring | `IBM_TIVOLI` | JSON, SYSLOG | [2024-03-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-tivoli-changelog)  
IBM WebSEAL | Web server | `IBM_WEBSEAL` | JSON, SYSLOG | [2025-10-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-webseal-changelog)  
[IBM Websphere Application Server](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-websphere-app-server) | Web server | `IBM_WEBSPHERE_APP_SERVER` | JSON, SYSLOG | [2026-05-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-websphere-app-server-changelog)  
IBM z/OS | OS | `IBM_ZOS` | LEEF | [2026-04-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-zos-changelog)  
IBM zSecure Alert | Alert log types | `IBM_ZSECURE_ALERT` | SYSLOG | [2025-06-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-zsecure-alert-changelog)  
[iBoss Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iboss-webproxy) | Webproxy | `IBOSS_WEBPROXY` | SYSLOG + JSON | [2023-08-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/iboss-webproxy-changelog)  
[Microsoft IIS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iis) | Web Server | `IIS` | SYSLOG + KV, JSON, XML | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/iis-changelog)  
[Illumio Core](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/illumio-core) | Policy Management | `ILLUMIO_CORE` | JSON, SYSLOG, SYSLOG+JSON, SYSLOG+CEF and SYSLOG+KV+JSON. | [2026-09-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/illumio-core-changelog)  
[Imperva Advanced Bot Protection](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-abp) | Bot Protection | `IMPERVA_ABP` | JSON | [2026-02-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-abp-changelog)  
[Imperva Attack Analytics](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-attack-analytics) | WAF | `IMPERVA_ATTACK_ANALYTICS` | KV | [2024-11-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-attack-analytics-changelog)  
[Imperva Audit Trail](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-audit-trail) | IT infrastructure | `IMPERVA_AUDIT_TRAIL` | JSON, SYSLOG | [2025-04-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-audit-trail-changelog)  
[Imperva CEF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-cef) | CEF | `IMPERVA_CEF` | SYSLOG + KV, CEF + KV | [2026-08-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-cef-changelog)  
[Imperva Database](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-db) | Cloud Application and Edge Security | `IMPERVA_DB` | SYSLOG, SYSLOG+JSON | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-db-changelog)  
[Imperva DRA](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-dra) | Data Security | `IMPERVA_DRA` | SYSLOG,json | [2026-04-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-dra-changelog)  
[Imperva FlexProtect](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-flexprotect) | Cloud App & Network Security | `IMPERVA_FLEXPROTECT` | CEF + KV | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-flexprotect-changelog)  
[Imperva SecureSphere Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-securesphere) | Data Security / Insider Threat | `IMPERVA_SECURESPHERE` | SYSLOG + KV (CEF), SYSLOG | [2026-09-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-securesphere-changelog)  
[Imperva](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-waf) | WAF | `IMPERVA_WAF` | SYSLOG+KV, JSON, CEF | [2026-08-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-waf-changelog)  
Infoblox | DHCP, DNS | `INFOBLOX` | SYSLOG | [2026-08-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-changelog)  
Infoblox DHCP | DHCP | `INFOBLOX_DHCP` | SYSLOG | [2026-07-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-dhcp-changelog)  
[Infoblox DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/infoblox-dns) | DNS | `INFOBLOX_DNS` | SYSLOG, CEF | [2026-05-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-dns-changelog)  
[Infoblox RPZ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/infoblox-rpz) | RPZ | `INFOBLOX_RPZ` | SYSLOG | [2024-02-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-rpz-changelog)  
[IBM Informix](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/informix) | DATABASE | `INFORMIX` | JSON + SYSLOG, SYSLOG + CSV | [2026-07-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/informix-changelog)  
Ingrian Networks DataSecure Appliance | System and Audit Logs | `INGRIAN_NETWORKS_DATASECURE_APPLIANCE` | Syslog | [2024-10-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ingrian-networks-datasecure-appliance-changelog)  
[Intel 471 Malware Intelligence](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel471-malware-intel) | Vulnerability scanners | `INTEL471_MALWARE_INTEL` | JSON | [2026-08-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/intel471-malware-intel-changelog)  
[INTEL471 Watcher Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel471-watcher-alerts) | Data Security | `INTEL471_WATCHER_ALERTS` | JSON | [2025-04-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/intel471-watcher-alerts-changelog)  
[Intel Endpoint Management Assistant](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel-ema) | Security | `INTEL_EMA` | SYSLOG | [2025-02-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/intel-ema-changelog)  
[InterSystems Cache](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intersystems-cache) | Database | `INTERSYSTEMS_CACHE` | SYSLOG + KV | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/intersystems-cache-changelog)  
[Ionix](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ionix) | SECURITY | `IONIX` | JSON | [2025-10-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ionix-changelog)  
[ION Spectrum](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ion-spectrum) | Automation | `ION_SPECTRUM` | CSV | [2026-08-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ion-spectrum-changelog)  
[Ipswitch MOVEit Transfer](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ipswitch-moveit-transfer) | Switches | `IPSWITCH_MOVEIT_TRANSFER` | SYSLOG + CSV | [2025-11-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ipswitch-moveit-transfer-changelog)  
Ipswitch SFTP | Data Transfer | `IPSWITCH_SFTP` | SYSLOG+KV, JSON | [2025-05-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ipswitch-sftp-changelog)  
[Precisely Ironstream IBM z/OS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ironstream-zos) | ZOS | `IRONSTREAM_ZOS` | JSON | [2024-11-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ironstream-zos-changelog)  
ISC DHCP | DHCP | `ISC_DHCP` | JSON + SYSLOG + KV | [2024-11-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/isc-dhcp-changelog)  
[Island Browser logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/island-browser) | Web Browser | `ISLAND_BROWSER` | JSON, SYSLOG + KV (CEF), SYSLOG + KV(CEF) + JSON | [2026-06-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/island-browser-changelog)  
JAMF CMDB | Computer Inventory | `JAMF` | JSON | [2024-05-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-changelog)  
JAMF Pro | Mac Endpoint Management System | `JAMF_PRO` | SYSLOG + KV, JSON | [2025-10-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-pro-changelog)  
[Jamf Protect Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-protect) | Endpoint Security | `JAMF_PROTECT` | JSON | [2026-06-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-protect-changelog)  
[Jamf pro context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-pro-context) | Mobile Device Management | `JAMF_PRO_CONTEXT` | JSON | [2026-07-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-pro-context-changelog)  
[JAMF Security Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-security-cloud) | Automation and DevOps Tools | `JAMF_SECURITY_CLOUD` | JSON | [2025-03-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-security-cloud-changelog)  
[Jamf Protect Telemetry](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-telemetry) | Endpoint Security | `JAMF_TELEMETRY` | JSON | [2024-05-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-telemetry-changelog)  
[Jamf Protect Telemetry V2](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-telemetry-v2) | Endpoint Security | `JAMF_TELEMETRY_V2` | JSON | [2025-11-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-telemetry-v2-changelog)  
[Jamf Protect Threat Events](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-threat-events) | Threat Events Stream | `JAMF_THREAT_EVENTS` | JSON | [2023-03-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-threat-events-changelog)  
[Jenkins](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jenkins) | Automation and DevOps | `JENKINS` | JSON, SYSLOG | [2026-08-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jenkins-changelog)  
[JFrog Artifactory](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jfrog-artifactory) | DevOps | `JFROG_ARTIFACTORY` | SYSLOG | [2026-08-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jfrog-artifactory-changelog)  
Journald | Log Aggregation and SIEM Systems | `JOURNALD` | JSON | [2026-09-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/journald-changelog)  
[JumpCloud Directory Insights](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jumpcloud-directory-insights) | CLOUD | `JUMPCLOUD_DIRECTORY_INSIGHTS` | JSON | [2026-06-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jumpcloud-directory-insights-changelog)  
[Juniper](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/juniper-firewall) | Firewall | `JUNIPER_FIREWALL` | SYSLOG + KV + JSON, SYSLOG + KV | [2026-08-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-firewall-changelog)  
Juniper IPS | IDS/IPS | `JUNIPER_IPS` | SYSLOG + KV | [2022-05-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-ips-changelog)  
[Juniper Junos](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/juniper-junos) | Network Device | `JUNIPER_JUNOS` | SYSLOG + KV, JSON+SYSLOG | [2026-09-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-junos-changelog)  
Juniper Mist | Network Management and Optimization software | `JUNIPER_MIST` | JSON | [2026-05-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-mist-changelog)  
Juniper MX Router | Routers and Switches | `JUNIPER_MX` | SYSLOG + KV | [2025-11-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-mx-changelog)  
Juniper Software Defined Wide Area Network | SYSLOG | `JUNIPER_SDWAN` | SYSLOG | [2023-07-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-sdwan-changelog)  
[Kaspersky AV](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kaspersky-av) | AV / Endpoint | `KASPERSKY_AV` | KV + CEF | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kaspersky-av-changelog)  
Kaspersky Endpoint | Security | `KASPERSKY_ENDPOINT` | SYSLOG | [2025-09-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kaspersky-endpoint-changelog)  
[Kea DHCP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kea-dhcp) | DHCP | `KEA_DHCP` | SYSLOG | [2022-04-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kea-dhcp-changelog)  
[Keeper Enterprise Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/keeper) | Security | `KEEPER` | JSON | [2024-12-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/keeper-changelog)  
[Kemp Load Balancer](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kemp-loadbalancer) | Load Balancer, Traffic Shaper, ADC | `KEMP_LOADBALANCER` | SYSLOG + KV, SYSLOG | [2026-05-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kemp-loadbalancer-changelog)  
KerioControl Firewall | Threat Management Firewall | `KERIOCONTROL` | SYSLOG | [2024-02-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/keriocontrol-changelog)  
[Keycloak](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/keycloak) | Identity and Access Management | `KEYCLOAK` | JSON | [2026-01-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/keycloak-changelog)  
Kisi Access Management | Physical Security | `KISI` | JSON | [2023-06-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kisi-changelog)  
Kiteworks | Network | `KITEWORKS` | SYSLOG, CSV, SYSLOG+JSON, SYSLOG+KV, JSON | [2026-08-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kiteworks-changelog)  
KnowBe4 PhishER | Email server log types. | `KNOWBE4_PHISHER` | JSON | [2025-12-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/knowbe4-phisher-changelog)  
Kolide Endpoint Security | Security | `KOLIDE` | JSON | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kolide-changelog)  
[Kong API Gateway](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kong-gateway) | Microservice management | `KONG_GATEWAY` | SYSLOG + JSON | [2022-09-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kong-gateway-changelog)  
Kubernetes Audit | K8s cluster audit logs | `KUBERNETES_AUDIT` | JSON,JSON+KV,JSON+SYSLOG | [2026-03-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kubernetes-audit-changelog)  
Kubernetes Audit Azure | Log Aggregator | `KUBERNETES_AUDIT_AZURE` | JSON | [2024-12-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kubernetes-audit-azure-changelog)  
[Kubernetes Auth Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kubernetes-auth-proxy) | Kubernetes Specific | `KUBERNETES_AUTH_PROXY` | JSON | [2022-09-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kubernetes-auth-proxy-changelog)  
[Kubernetes Node](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kubernetes-node) | Kubernetes Container | `KUBERNETES_NODE` | JSON | [2026-06-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kubernetes-node-changelog)  
[Kyriba Treasury Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kyriba) | SaaS Application | `KYRIBA` | CSV | 2021-02-24  
[Lacework Cloud Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lacework) | Cloud Security | `LACEWORK` | JSON | [2025-06-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lacework-changelog)  
LastPass Password Management | Identity and Access Management | `LASTPASS` | JSON | [2026-05-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lastpass-changelog)  
[Lenel Onguard Badge Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lenel-onguard) | Access Control System | `LENEL_ONGUARD` | JSON | [2024-11-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lenel-onguard-changelog)  
[LimaCharlie](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/limacharlie-edr) | EDR | `LIMACHARLIE_EDR` | JSON | 2023-08-07  
[Linkshadow NDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/linkshadow-ndr) | NDR | `LINKSHADOW_NDR` | SYSLOG + KV | [2025-01-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/linkshadow-ndr-changelog)  
Linux DHCP | DHCP | `LINUX_DHCP` | SYSLOG | [2024-09-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/linux-dhcp-changelog)  
Linux Sysmon | DNS | `LINUX_SYSMON` | XML | [2026-02-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/linux-sysmon-changelog)  
[LogonBox](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/logonbox) | Authentication | `LOGONBOX` | SYSLOG + KV | [2024-02-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/logonbox-changelog)  
[Looker Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/looker-audit) | endpoints | `LOOKER_AUDIT` | JSON | [2025-03-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/looker-audit-changelog)  
[Mobile Endpoint Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lookout-mobile-endpoint-security) | Mobile Endpoint Security | `LOOKOUT_MOBILE_ENDPOINT_SECURITY` | CEF, JSON | [2026-07-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lookout-mobile-endpoint-security-changelog)  
[Lucid](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lucid) | Authentication log types. | `LUCID` | JSON | [2024-06-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lucid-changelog)  
[Apple macOS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/macos) | AV / Endpoint | `MACOS` | SYSLOG, JSON | [2026-07-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/macos-changelog)  
macOS Endpoint Security | AV and endpoint logs | `MACOS_ENDPOINT_SECURITY` | SYSLOG + KV | [2023-07-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/macos-endpoint-security-changelog)  
Trustwave SEC MailMarshal | Email server | `MAILMARSHAL` | SYSLOG | [2023-04-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mailmarshal-changelog)  
[Malwarebytes](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/malwarebytes-edr) | EDR | `MALWAREBYTES_EDR` | JSON | [2024-08-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/malwarebytes-edr-changelog)  
[ManageEngine AD360](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-ad360) | Identity and Access Management | `MANAGE_ENGINE_AD360` | SYSLOG + KV | [2025-08-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/manage-engine-ad360-changelog)  
[ManageEngine Log360](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-log360) | Alert Log | `MANAGE_ENGINE_LOG360` | SYSLOG+KV | [2024-10-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/manage-engine-log360-changelog)  
[ManageEngine Reporter Plus](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-reporter-plus) | SaaS Application | `MANAGE_ENGINE_REPORTER_PLUS` | JSON | [2022-08-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/manage-engine-reporter-plus-changelog)  
[Mandiant Custom IOC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mandiant-custom-ioc) | IOC | `MANDIANT_CUSTOM_IOC` | JSON | [2023-12-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mandiant-custom-ioc-changelog)  
Maria Database | Database | `MARIA_DB` | SYSLOG | [2026-03-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/maria-db-changelog)  
Mattermost | Alerts | `MATTERMOST` | JSON , SYSLOG | [2023-12-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mattermost-changelog)  
[McAfee DLP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-dlp) | DLP | `MCAFEE_DLP` | CSV | [2025-12-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-dlp-changelog)  
McAfee ePolicy Orchestrator | Policy Management | `MCAFEE_EPO` | SYSLOG + XML, CSV, KV, JSON | [2026-07-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-epo-changelog)  
[McAfee Enterprise Security Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-esm) | Log Aggregator | `MCAFEE_ESM` | SYSLOG + JSON | 2026-02-27  
McAfee IPS | IDS/IPS | `MCAFEE_IPS` | SYSLOG, JSON, SYSLOG+KV | [2026-09-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-ips-changelog)  
McAfee MVISION CASB | CLOUD SECURITY | `MCAFEE_MVISION_CASB` | KV | [2023-06-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-mvision-casb-changelog)  
[McAfee Skyhigh CASB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-skyhigh-casb) | CASB | `MCAFEE_SKYHIGH_CASB` | SYSLOG + KV, SYSLOG + CSV | [2026-03-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-skyhigh-casb-changelog)  
McAfee Unified Cloud Edge | SaaS Application | `MCAFEE_UCE` | JSON | 2021-07-20  
[McAfee Web Gateway](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-webproxy) | Web Proxy | `MCAFEE_WEBPROXY` | SYSLOG + KV (CEF), JSON, JSON + CEF | [2026-04-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-webproxy-changelog)  
[McAfee Web Protection](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-web-protection) | SaaS Application | `MCAFEE_WEB_PROTECTION` | JSON | [2025-04-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-web-protection-changelog)  
[Medigate IoT](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/medigate-iot) | IoT | `MEDIGATE_IOT` | SYSLOG + JSON | [2025-08-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/medigate-iot-changelog)  
Men and Mice DNS | DNS | `MENANDMICE_DNS` | SYSLOG | 2021-11-12  
[Menlo Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/menlo-security) | Web Proxy | `MENLO_SECURITY` | JSON | [2025-07-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/menlo-security-changelog)  
[Metabase](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/metabase) | Data Security | `METABASE` | JSON | [2025-02-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/metabase-changelog)  
Micro Focus iManager | Network Management and Optimization | `MICROFOCUS_IMANAGER` | SYSLOG, SYSLOG + KV | [2026-07-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microfocus-imanager-changelog)  
Microsoft ATA | IDS/IPS | `MICROSOFT_ATA` | SYSLOG + KV | [2024-01-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-ata-changelog)  
Microsoft CASB | CASB | `MICROSOFT_CASB` | SYSLOG + KV (CEF) | [2025-03-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-casb-changelog)  
[Microsoft Defender For Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-cloud-alerts) | Automation and DevOps Tools | `MICROSOFT_DEFENDER_CLOUD_ALERTS` | JSON | [2026-08-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-cloud-alerts-changelog)  
[Microsoft Defender for Endpoint](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint) | EDR | `MICROSOFT_DEFENDER_ENDPOINT` | JSON | [2026-10-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-endpoint-changelog)  
[Microsoft Defender Endpoint for iOS Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint-ios) | Data Security | `MICROSOFT_DEFENDER_ENDPOINT_IOS` | JSON | [2026-08-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-endpoint-ios-changelog)  
[Microsoft Defender for Identity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-identity) | EDR | `MICROSOFT_DEFENDER_IDENTITY` | JSON | [2026-09-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-identity-changelog)  
[Microsoft Defender for Office 365](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-mail) | Email server log types. | `MICROSOFT_DEFENDER_MAIL` | JSON, JSON+CSV | [2026-08-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-mail-changelog)  
[Microsoft Dynamics 365 User Activity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-dynamics-365) | Authentication logs | `MICROSOFT_DYNAMICS_365` | CSV | [2024-12-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-dynamics-365-changelog)  
[Microsoft Graph Activity Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-graph-activity-logs) | AUDIT | `MICROSOFT_GRAPH_ACTIVITY_LOGS` | JSON | [2024-10-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-graph-activity-logs-changelog)  
[Microsoft Graph API Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-graph-alert) | Gateway to data and intelligence | `MICROSOFT_GRAPH_ALERT` | JSON | [2026-07-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-graph-alert-changelog)  
[Microsoft IAS Server](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-ias) | Endpoint Security | `MICROSOFT_IAS` | CSV + KV | 2024-04-25  
[Windows Local Administrator Password Solution](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-laps) | Local Administrator Password Solution | `MICROSOFT_LAPS` | JSON | [2024-08-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-laps-changelog)  
Microsoft Netlogon | Authentication | `MICROSOFT_NETLOGON` | SYSLOG | [2024-12-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-netlogon-changelog)  
[Network Policy Server](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-nps) | Network Policy Server | `MICROSOFT_NPS` | JSON + XML, JSON + CSV | [2025-12-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-nps-changelog)  
[Microsoft System Center Endpoint Protection](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-scep) | Malware Detection | `MICROSOFT_SCEP` | KV | [2025-02-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-scep-changelog)  
[Microsoft Sentinel](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-sentinel) | Microsoft Sentinel | `MICROSOFT_SENTINEL` | JSON | [2026-09-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-sentinel-changelog)  
[Microsoft SQL Server](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-sql) | Database | `MICROSOFT_SQL` | SYSLOG + KV, JSON, SYSLOG + JSON, CSV, XML, SYSLOG + XML, SYSLOG, KV | [2026-09-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-sql-changelog)  
[Microstrategy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microstrategy) | Application server logs | `MICROSTRATEGY` | SYSLOG | [2025-03-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microstrategy-changelog)  
Mikrotik Router | Router | `MIKROTIK_ROUTER` | SYSLOG + Grok | [2025-09-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mikrotik-router-changelog)  
[Mimecast](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mimecast-mail) | Email Server | `MIMECAST_MAIL` | KV,KV+JSON | [2025-07-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mimecast-mail-changelog)  
[Mimecast Mail V2](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mimecast-mail-v2) | Email Server | `MIMECAST_MAIL_V2` | SYSLOG + JSON | [2026-03-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mimecast-mail-v2-changelog)  
Mimecast URL Logs | Email server log types. | `MIMECAST_URL_LOGS` | JSON | [2026-07-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mimecast-url-logs-changelog)  
[MISP Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/misp-ioc) | Cybersecurity | `MISP_IOC` | JSON, CSV | [2026-07-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/misp-ioc-changelog)  
[Mobileiron](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mobileiron) | ENDPOINT MANAGEMENT | `MOBILEIRON` | JSON , SYSLOG, SYSLOG+KV | [2026-05-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mobileiron-changelog)  
[Mongo Database](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mongo-db) | DATABASE | `MONGO_DB` | JSON | [2026-05-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mongo-db-changelog)  
[MySQL](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mysql) | Database | `MYSQL` | SYSLOG, JSON, CSV | [2026-07-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mysql-changelog)  
[Nagios Infrastructure Monitoring](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nagios) | NETWORK MONITORING | `NAGIOS` | CSV | [2024-08-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nagios-changelog)  
[Nasuni File Services Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nasuni-file-services) | Data Transfer | `NASUNI_FILE_SERVICES` | SYSLOG + JSON , CSV | [2025-03-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nasuni-file-services-changelog)  
[Neo4j](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/neo4j) | Database management system | `NEO4J` | JSON | [2023-12-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/neo4j-changelog)  
Neosec | Security | `NEOSEC` | JSON | [2023-07-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/neosec-changelog)  
[NetApp BlueXP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-bluexp) | Security | `NETAPP_BLUEXP` | JSON | [2023-11-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netapp-bluexp-changelog)  
[NetApp ONTAP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-ontap) | Rest api | `NETAPP_ONTAP` | SYSLOG, XML, JSON, SYSLOG+XML, SYSLOG+KV | [2026-07-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netapp-ontap-changelog)  
[NetApp SAN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-san) | Rest api | `NETAPP_SAN` | SYSLOG | [2023-04-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netapp-san-changelog)  
Netapp Storagegrid | Security | `NETAPP_STORAGEGRID` | SYSLOG + KV | [2026-05-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netapp-storagegrid-changelog)  
[NetDocuments Solutions](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netdocuments) | Threat Management Firewall | `NETDOCUMENTS` | Cloud-Based Document Management System | [2024-05-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netdocuments-changelog)  
Netfilter IPtables | Firewall | `NETFILTER_IPTABLES` | SYSLOG + KV | [2025-11-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netfilter-iptables-changelog)  
[OpenTelemetry Netflow Receiver](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netflow-otel) | OpenTelemetry Netflow Receiver | `NETFLOW_OTEL` | JSON | [2025-04-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netflow-otel-changelog)  
[NetIQ Access Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netiq-access-manager) | Security | `NETIQ_ACCESS_MANAGER` | SYSLOG + KV | [2026-01-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netiq-access-manager-changelog)  
NetIQ eDirectory | Identity management deployments | `NETIQ_EDIRECTORY` | Syslog, CEF | [2026-06-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netiq-edirectory-changelog)  
[Netscout OCI](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netscout-oci) | Alert log | `NETSCOUT_OCI` | SYSLOG + KV | [2024-02-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netscout-oci-changelog)  
[Netskope](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-alert) | Cloud Security | `NETSKOPE_ALERT` | JSON | [2024-08-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-alert-changelog)  
[Netskope V2](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-alert-v2) | Cloud Security | `NETSKOPE_ALERT_V2` | JSON, CSV | [2026-07-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-alert-v2-changelog)  
Netskope CASB | CASB | `NETSKOPE_CASB` | JSON, SYSLOG+JSON | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-casb-changelog)  
[Netscope Client](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-client) | CASB | `NETSKOPE_CLIENT` | JSON | [2024-10-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-client-changelog)  
[Netskope Web Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-webproxy) | Web Proxy | `NETSKOPE_WEBPROXY` | SYSLOG, SYSLOG+JSON, JSON, CSV | [2026-08-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-webproxy-changelog)  
[Netwrix](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netwrix) | Web Server | `NETWRIX` | JSON, XML | [2026-09-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netwrix-changelog)  
Netwrix StealthAudit | N/A | `NETWRIX_STEALTHAUDIT` | SYSLOG + KV | [2025-01-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netwrix-stealthaudit-changelog)  
[Net Suite](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/net-suite) | WAF | `NET_SUITE` | kv | [2023-08-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/net-suite-changelog)  
Nexus Sonatype | Storage | `NEXUS_SONATYPE` | JSON+SYSLOG | [2025-11-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nexus-sonatype-changelog)  
[NGINX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nginx) | Server Management | `NGINX` | JSON + SYSLOG, SYSLOG + KV, KV | [2026-09-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nginx-changelog)  
[NIMBLE OS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nimble-os) | OS | `NIMBLE_OS` | SYSLOG | [2025-08-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nimble-os-changelog)  
[Unix system](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nix-system) | OS | `NIX_SYSTEM` | SYSLOG, JSON | [2026-09-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nix-system-changelog)  
[Nokia Router](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nokia-router) | Switches and Routers | `NOKIA_ROUTER` | SYSLOG + KV | [2025-05-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nokia-router-changelog)  
Noname API Security | Security | `NONAME_API_SECURITY` | JSON | [2026-05-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/noname-api-security-changelog)  
Nozomi Networks Scada Guardian | Network Monitoring | `NOZOMI_GUARDIAN` | CEF and JSON, SYSLOG | [2026-01-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nozomi-guardian-changelog)  
[Ntopng](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ntopng) | NDR | `NTOPNG` | SYSLOG + JSON | [2024-02-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ntopng-changelog)  
[Nucleus Asset Metadata](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nucleus-asset) | Nucleus Specific | `NUCLEUS_ASSET` | JSON | 2021-08-05  
[Nucleus Unified Vulnerability Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nucleus-vulnerability) | Nucleus Specific | `NUCLEUS_VULNERABILITY` | JSON | 2021-06-30  
[Nutanix Prism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nutanix-prism) | Firewall | `NUTANIX_PRISM` | JSON, SYSLOG | [2025-12-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nutanix-prism-changelog)  
NXLog Manager | Log Aggregator | `NXLOG_MANAGER` | SYSLOG | 2022-01-13  
[Nyansa Events](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nyansa-events) | IoT | `NYANSA_EVENTS` | SYSLOG + KV | [2023-03-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nyansa-events-changelog)  
Proofpoint Observeit | Email Server | `OBSERVEIT` | JSON, KV | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/observeit-changelog)  
Obsidian | SaaS Application | `OBSIDIAN` | JSON | [2026-03-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/obsidian-changelog)  
[Oracle Cloud Infrastructure Audit Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oci-audit) | Oracle Cloud Infrastructure | `OCI_AUDIT` | JSON | [2026-05-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oci-audit-changelog)  
[Oracle Cloud Guard](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oci-cloudguard) | Cloud | `OCI_CLOUDGUARD` | JSON | [2025-02-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oci-cloudguard-changelog)  
Oracle Cloud Infrastructure VCN Flow Logs | Oracle Cloud Infrastructure | `OCI_FLOW` | JSON | [2026-06-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oci-flow-changelog)  
[Open Cybersecurity Schema Framework (OCSF)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ocsf) | Schema | `OCSF` | JSON | [2025-11-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ocsf-changelog)  
[Office 365](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365) | SaaS Application | `OFFICE_365` | JSON | [2026-09-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/office-365-changelog)  
[Office 365 Message Trace](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365-messagetrace) | OFFICE_365 Specific | `OFFICE_365_MESSAGETRACE` | JSON | [2026-04-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/office-365-messagetrace-changelog)  
[Okera Dynamic Access Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okera-dap) | Data Security | `OKERA_DAP` | JSON | [2023-01-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okera-dap-changelog)  
[Okta](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta) | Identity and Access Management | `OKTA` | JSON | [2026-09-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-changelog)  
Okta Access Gateway | OKTA specific | `OKTA_ACCESS_GATEWAY` | SYSLOG + KV | [2023-02-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-access-gateway-changelog)  
[Okta Scaleft](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta-scaleft) | Identity and Access Management | `OKTA_SCALEFT` | JSON | [2026-05-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-scaleft-changelog)  
[Okta User Context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta-user-context) | Identity and Access Management | `OKTA_USER_CONTEXT` | JSON | [2026-08-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-user-context-changelog)  
[Onapsis](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onapsis) | SAP | `ONAPSIS` | JSON , SYSLOG , KV | [2026-07-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onapsis-changelog)  
[One Identity TPAM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oneidentity-tpam) | Privileged Account Activity | `ONEIDENTITY_TPAM` | KV ,CEF | [2025-12-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oneidentity-tpam-changelog)  
[OneLogin](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onelogin-sso) | SSO | `ONELOGIN_SSO` | JSON | [2026-01-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onelogin-sso-changelog)  
[1Password](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword) | Identity and Access Management | `ONEPASSWORD` | JSON | [2025-10-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onepassword-changelog)  
[1Password Audit Events](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword-audit-events) | Identity and Access Management | `ONEPASSWORD_AUDIT_EVENTS` | JSON | [2026-05-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onepassword-audit-events-changelog)  
[One Identity Identity Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/one-identity-identity-manager) | unified identity security | `ONE_IDENTITY_IDENTITY_MANAGER` | kv , SYSLOG + JSON | [2025-07-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/one-identity-identity-manager-changelog)  
[Onfido](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onfido) | Authentication | `ONFIDO` | SYSLOG + JSON | [2023-03-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onfido-changelog)  
[Oort Security Tool](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oort) | Identity and Access Management | `OORT` | JSON | [2026-03-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oort-changelog)  
Open Policy Agent | NA | `OPA` | JSON | [2025-01-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opa-changelog)  
[OpenAI AuditLog](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openai-auditlog) | NDR | `OPENAI_AUDITLOG` | JSON | 2025-03-20  
[ForgeRock OpenAM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openam) | Identity and Access Management | `OPENAM` | CSV, SYSLOG + KV | [2024-11-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openam-changelog)  
[OpenCanary](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/opencanary) | Data Security | `OPENCANARY` | SYSLOG + JSON | [2024-03-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opencanary-changelog)  
[ForgeRock OpenDJ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/opendj) | LDAP | `OPENDJ` | SYSLOG + KV | 2020-10-01  
Opengear Remote Management | Secure Remote Access | `OPENGEAR` | SYSLOG | [2024-09-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opengear-changelog)  
[Open LDAP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openldap) | LDAP | `OPENLDAP` | SYSLOG | [2025-11-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openldap-changelog)  
Openpath | AV / Endpoint | `OPENPATH` | SYSLOG | [2025-06-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openpath-changelog)  
OpenSSH | Logging and Troubleshooting | `OPENSSH` | SYSLOG | [2024-01-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openssh-changelog)  
OpenVPN | Network | `OPEN_VPN` | SYSLOG + KV + JSON | [2026-07-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/open-vpn-changelog)  
[Opnsense](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/opnsense) | Firewall and Routing Platform | `OPNSENSE` | Syslog, Syslog + CSV | [2025-09-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opnsense-changelog)  
Opswat Metadefender | Threat Protection | `OPSWAT_METADEFENDER` | SYSLOG + KV (CEF) | [2025-10-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opswat-metadefender-changelog)  
Ops Genie | Web Proxy log types | `OPS_GENIE` | JSON | [2025-02-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ops-genie-changelog)  
[Oracle Cloud Infrastructure](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-cloud-audit) | Oracle Cloud Infrastructure | `ORACLE_CLOUD_AUDIT` | JSON | [2025-05-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-cloud-audit-changelog)  
[Oracle](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-db) | DATABASE | `ORACLE_DB` | SYSLOG + KV, SYSLOG, JSON | [2026-09-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-db-changelog)  
[Oracle Fusion](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-fusion) | SaaS Application | `ORACLE_FUSION` | JSON | [2026-07-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-fusion-changelog)  
[Oracle NetSuite](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-netsuite) | CASB | `ORACLE_NETSUITE` | JSON | [2026-06-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-netsuite-changelog)  
[Oracle Unified Directory](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-oud) | ORACLE OUD | `ORACLE_OUD` | SYSLOG | [2023-09-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-oud-changelog)  
Oracle WebLogic Server | Web server logs | `ORACLE_WEBLOGIC` | SYSLOG | [2025-01-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-weblogic-changelog)  
Orca Cloud Security Platform | IDS/IPS log types | `ORCA` | JSON | [2026-04-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/orca-changelog)  
[Ordr IoT](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ordr-iot) | IoT | `ORDR_IOT` | SYSLOG + JSON | [2024-03-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ordr-iot-changelog)  
[OSQuery](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/osquery-edr) | EDR | `OSQUERY_EDR` | SYSLOG + JSON | [2024-05-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/osquery-edr-changelog)  
[OSSEC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ossec) | IDS/IPS | `OSSEC` | SYSLOG | [2024-04-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ossec-changelog)  
Palantir | Foundry SaaS | `PALANTIR` | JSON | [2024-12-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/palantir-changelog)  
[Palo Alto Prisma Access](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-casb) | Cloud Security | `PAN_CASB` | JSON, SYSLOG + CSV, SYSLOG | [2026-05-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-casb-changelog)  
[Palo Alto Cortex XDR Events](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-cortex-xdr-events) | Monitoring and Threat Detection | `PAN_CORTEX_XDR_EVENTS` | JSON | [2026-02-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-cortex-xdr-events-changelog)  
[Palo Alto Networks Traps](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-edr) | EDR | `PAN_EDR` | CSV + KV | [2022-08-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-edr-changelog)  
[Palo Alto Networks Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-firewall) | Firewall | `PAN_FIREWALL` | CSV + CEF + LEEF + JSON | [2026-10-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-firewall-changelog)  
[PAN Autofocus](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-ioc) | IOC | `PAN_IOC` | JSON | 2021-08-09  
Palo Alto Networks IoT Security | IoT | `PAN_IOT` | SYSLOG | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-iot-changelog)  
Palo Alto Panorama | Firewall | `PAN_PANORAMA` | CSV, JSON + CSV | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-panorama-changelog)  
[Palo Alto Prisma Cloud Alert payload](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-ca) | Alert log types | `PAN_PRISMA_CA` | JSON | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-prisma-ca-changelog)  
[Palo Alto Prisma Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-cloud) | SECURITY PLATFORM | `PAN_PRISMA_CLOUD` | JSON | [2024-11-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-prisma-cloud-changelog)  
[Passive DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/passive-dns) | DNS | `PASSIVE_DNS` | JSON | 2021-05-19  
Passwordstate | below is a catch all for tokens, phones, groups, and endpoints | `PASSWORDSTATE` | SYSLOG | [2025-10-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/passwordstate-changelog)  
Peplink Firewall | Firewall | `PEPLINK_FW` | SYSLOG + KV | [2023-08-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/peplink-fw-changelog)  
[PerimeterX Bot Protection](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/perimeterx-bot-protection) | Security | `PERIMETERX_BOT_PROTECTION` | JSON | [2024-03-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/perimeterx-bot-protection-changelog)  
[pfSense](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pfsense) | FIREWALL | `PFSENSE` | SYSLOG | [2025-07 -18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pfsense-changelog)  
[Pharos](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pharos) | NA | `PHAROS` | JSON | 2025-02-18  
[Phishlabs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/phishlabs) | Digital Risk Protection | `PHISHLABS` | JSON | [2024-03-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/phishlabs-changelog)  
Ping Identity | Authentication | `PING` | JSON, SYSLOG + KV, CEF | [2026-07-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-changelog)  
PingIdentity Directory Server Logs | Security | `PING_DIRECTORY` | SYSLOG + KV, JSON, SYSLOG+JSON | [2026-07-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-directory-changelog)  
Ping Federate | Authentication | `PING_FEDERATE` | CSV | [2026-08-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-federate-changelog)  
Ping One | NA | `PING_ONE` | JSON | [2026-09-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-one-changelog)  
Pivotal | PaaS Application | `PIVOTAL` | SYSLOG + KV | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pivotal-changelog)  
Portnox CEF | Privileged Account Activity | `PORTNOX_CEF` | CEF Syslog | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/portnox-cef-changelog)  
PostFix Mail | Email Server | `POSTFIX_MAIL` | SYSLOG | [2026-01-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/postfix-mail-changelog)  
PostgreSQL | Database | `POSTGRESQL` | JSON,KV,SYSLOG | [2026-02-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/postgresql-changelog)  
[Microsoft PowerShell](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/powershell) | Misc. Windows-specific | `POWERSHELL` | SYSLOG + JSON, XML | [2026-09-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/powershell-changelog)  
[Preempt Alert](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/preempt) | Identity and Access Management | `PREEMPT` | SYSLOG + KV (CEF) | [2022-06-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/preempt-changelog)  
[Preempt Auth](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/preempt-auth) | Identity and Access Management | `PREEMPT_AUTH` | SYSLOG + JSON | 2021-06-16  
[Privacy-I](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/privacy-i) | NA | `PRIVACY_I` | CSV + KV | [2025-02-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/privacy-i-changelog)  
ProFTPD | Web Server | `PROFTPD` | SYSLOG | [2025-01-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proftpd-changelog)  
Proofpoint CASB | CASB | `PROOFPOINT_CASB` | JSON | [2026-01-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-casb-changelog)  
[Proofpoint Tap Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail) | Email Server | `PROOFPOINT_MAIL` | SYSLOG+KV, JSON, SYSLOG+JSON | [2026-09-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-mail-changelog)  
[Proofpoint Email Filter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail-filter) | Email Server | `PROOFPOINT_MAIL_FILTER` | SYSLOG + KV, SYSLOG + JSON | [2025-12-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-mail-filter-changelog)  
[Proofpoint On Demand](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-on-demand) | Email Server | `PROOFPOINT_ON_DEMAND` | JSON | [2026-06-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-on-demand-changelog)  
[Proofpoint Sendmail Sentrion](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-sendmail-sentrion) | Email server | `PROOFPOINT_SENDMAIL_SENTRION` | SYSLOG | [2026-07-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-sendmail-sentrion-changelog)  
[ProofPoint Secure Email Relay](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-ser) | Email server | `PROOFPOINT_SER` | JSON | [2025-01-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-ser-changelog)  
[Proofpoint Tap Forensics](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-tap-forensics) | Email Server | `PROOFPOINT_TAP_FORENSICS` | JSON | [2024-11-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-tap-forensics-changelog)  
[Proofpoint Tap Threats](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-tap-threats) | Email Server | `PROOFPOINT_TAP_THREATS` | JSON | [2025-01-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-tap-threats-changelog)  
[Proofpoint Threat Response](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-trap) | Email Server | `PROOFPOINT_TRAP` | SYSLOG, JSON | [2026-04-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-trap-changelog)  
[Proofpoint Web Browser Isolation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-web-browser-isolation) | ATTACK PROTECTION ISOLATION | `PROOFPOINT_WEB_BROWSER_ISOLATION` | JSON | [2023-05-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-web-browser-isolation-changelog)  
[Pulse Secure](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pulse-secure-vpn) | VPN | `PULSE_SECURE_VPN` | SYSLOG | [2025-12-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pulse-secure-vpn-changelog)  
Pulse Secure Virtual Traffic Manager | Traffic Shapers | `PULSE_SECURE_VTM` | SYSLOG | [2023-11-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pulse-secure-vtm-changelog)  
[Pure Storage](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pure-storage) | Data Storage | `PURE_STORAGE` | SYSLOG + KV | [2026-08-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pure-storage-changelog)  
QNAP Systems NAS | Storage solutions | `QNAP_NAS` | SYSLOG, KV | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qnap-nas-changelog)  
[Qualys Asset Context](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-asset-context) | Vulnerability Scanner | `QUALYS_ASSET_CONTEXT` | JSON | [2023-07-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qualys-asset-context-changelog)  
[Qualys Continuous Monitoring](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-continuous-monitoring) | Monitoring | `QUALYS_CONTINUOUS_MONITORING` | JSON | [2022-08-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qualys-continuous-monitoring-changelog)  
[Qualys Scan](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-scan) | Vulnerability scanner | `QUALYS_SCAN` | JSON | [2023-04-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qualys-scan-changelog)  
[Qualys Virtual Scanner](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-virtual-scanner) | Vulnerability Scanner | `QUALYS_VIRTUAL_SCANNER` | JSON | [2023-08-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qualys-virtual-scanner-changelog)  
[Qualys VM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-vm) | Vulnerability Scanner | `QUALYS_VM` | KV + JSON | [2025-07-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qualys-vm-changelog)  
Quest Active Directory | Authentication log | `QUEST_AD` | CEF SYSLOG + JSON | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/quest-ad-changelog)  
[Quest Change Auditor for EMC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/quest-change-auditor-emc) | Alert | `QUEST_CHANGE_AUDITOR_EMC` | JSON | [2024-06-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/quest-change-auditor-emc-changelog)  
[Quest File Access Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/quest-file-audit) | Alert | `QUEST_FILE_AUDIT` | JSON | [2024-01-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/quest-file-audit-changelog)  
Qumulo FS | File System | `QUMULO_FS` | SYSLOG | [2024-05-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qumulo-fs-changelog)  
[Radware Alteon](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/radware-alteon) | Load Balancer | `RADWARE_ALTEON` | SYSLOG | [2024-06-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/radware-alteon-changelog)  
[Radware Web Application Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/radware-firewall) | Firewall | `RADWARE_FIREWALL` | SYSLOG, JSON, SYSLOG+KV | [2026-05-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/radware-firewall-changelog)  
[Rapid7 Insight](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rapid7-insight) | Vulnerability Scanner | `RAPID7_INSIGHT` | SYSLOG, JSON | [2026-04-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rapid7-insight-changelog)  
[Rapid7](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rapid7-nexpose) | Vulnerability Scanner | `RAPID7_NEXPOSE` | JSON | [2024-05-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rapid7-nexpose-changelog)  
[Recorded Future](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/recorded-future-ioc) | IOC | `RECORDED_FUTURE_IOC` | JSON | [2026-01-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/recorded-future-ioc-changelog)  
[Recordia](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/recordia) | Telephone software | `RECORDIA` | JSON | [2024-01-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/recordia-changelog)  
[Red Canary](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/redcanary-edr) | EDR | `REDCANARY_EDR` | JSON | [2022-09-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/redcanary-edr-changelog)  
[Red Hat Directory Server LDAP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/redhat-directory-server) | Identity and Access Management | `REDHAT_DIRECTORY_SERVER` | JSON + SYSLOG + KV | [2026-05-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/redhat-directory-server-changelog)  
Red Hat OpenShift | Kubernetes Container | `REDHAT_OPENSHIFT` | SYSLOG, JSON, SYSLOG+KV+JSON | [2026-09-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/redhat-openshift-changelog)  
[Remediant SecureONE](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/remediant-secureone) | Privileged Account Activity | `REMEDIANT_SECUREONE` | SYSLOG + JSON | [2025-07-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/remediant-secureone-changelog)  
Reserved LogType2 | LDAP | `RESERVED_LOG_TYPE_2` | JSON | [2024-12-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/reserved-log-type-2-changelog)  
[ReviveSec](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/revivesec) | Application server logs | `REVIVESEC` | SYSLOG | [2025-02-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/revivesec-changelog)  
[RH-ISAC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rh-isac-ioc) | IOC | `RH_ISAC_IOC` | JSON | [2024-03-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rh-isac-ioc-changelog)  
[Ribbon Analytics Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ribbon-analytics-platform) | Telephone Software | `RIBBON_ANALYTICS_PLATFORM` | SYSLOG | [2022-09-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ribbon-analytics-platform-changelog)  
[Rippling Activity Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rippling-activitylogs) | ACTIVITY_LOGS | `RIPPLING_ACTIVITYLOGS` | JSON | [2024-08-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rippling-activitylogs-changelog)  
[RSA](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rsa-auth-manager) | Identity and Access Management | `RSA_AUTH_MANAGER` | CSV, SYSLOG, SYSLOG+KV | [2026-06-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rsa-auth-manager-changelog)  
RSA NetWitness | PLATFORM CONFIGURATION | `RSA_NETWITNESS` | SYSLOG, CEF, JSON | [2026-09-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rsa-netwitness-changelog)  
[RSA SecurID Access Identity Router](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rsa-securid) | SECURITY | `RSA_SECURID` | SYSLOG + CSV | [2024-12-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rsa-securid-changelog)  
Rubrik | Backup software | `RUBRIK` | SYSLOG | [2025-01-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rubrik-changelog)  
Rubrik Polaris | Data Security | `RUBRIK_POLARIS` | JSON | [2024-05-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rubrik-polaris-changelog)  
[Rubrik Security Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rubrik-security-cloud) | Security Violation, Login, Anomaly, Threat Monitoring, Threat Hunt | `RUBRIK_SECURITY_CLOUD` | JSON | [2026-02-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rubrik-security-cloud-changelog)  
Ruckus Networks | Wireless | `RUCKUS_WIRELESS` | SYSLOG + KV | [2025-10-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ruckus-wireless-changelog)  
[SailPoint IAM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sailpoint-iam) | Identity and Access Management | `SAILPOINT_IAM` | JSON, SYSLOG | [2026-09-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sailpoint-iam-changelog)  
[SailPoint IdentityIQ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sailpoint-iiq) | Identity and Access Management | `SAILPOINT_IIQ` | SYSLOG, KV+XML, KV | [2026-02-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sailpoint-iiq-changelog)  
[Saiwall VPN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/saiwall-vpn) | VPN | `SAIWALL_VPN` | KV | [2026-08-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/saiwall-vpn-changelog)  
[Salesforce](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/salesforce) | SaaS Application | `SALESFORCE` | KV (LEEF), CSV, JSON | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/salesforce-changelog)  
[Salesforce Commerce Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/salesforce-commerce-cloud) | SaaS Application | `SALESFORCE_COMMERCE_CLOUD` | SYSLOG, JSON | [2024-10-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/salesforce-commerce-cloud-changelog)  
Sangfor Next Generation Firewall | Firewall | `SANGFOR_NGAF` | SYSLOG + KV, JSON + CEF | [2026-08-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sangfor-ngaf-changelog)  
[Sangfor Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sangfor-proxy) | Application server logs | `SANGFOR_PROXY` | SYSLOG | [2025-02-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sangfor-proxy-changelog)  
[SAP Sybase Adaptive Server Enterprise Database](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-ase) | Database | `SAP_ASE` | SYSLOG+KV, SYSLOG + CSV | [2026-01-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-ase-changelog)  
[Sap Business Technology Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-btp) | SaaS Applications | `SAP_BTP` | JSON | [2026-09-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-btp-changelog)  
[SAP Change Document](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-change-document) | Alert log types | `SAP_CHANGE_DOCUMENT` | JSON | [2026-08-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-change-document-changelog)  
[SAP Gateway](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-gateway) | Alert log types | `SAP_GATEWAY` | SYSLOG,SYSLOG+KV | [2026-04-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-gateway-changelog)  
SAP HANA | Database log types | `SAP_HANA` | CSV | [2026-02-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-hana-changelog)  
[SAP Hana Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-hana-audit) | Alert log types | `SAP_HANA_AUDIT` | CSV , JSON+CSV, JSON+SYSLOG,JSON, SYSLOG, SYSLOG+KV | [2026-04-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-hana-audit-changelog)  
[SAP Internet Communication Manager](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-icm) | SaaS Applications | `SAP_ICM` | SYSLOG | [2026-02-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-icm-changelog)  
[SAP Identity and Authentication Data](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-identity-and-auth-data) | SaaS Applications | `SAP_IDENTITY_AND_AUTH_DATA` | JSON | [2026-02-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-identity-and-auth-data-changelog)  
[SAP Netweaver](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-netweaver) | Database | `SAP_NETWEAVER` | JSON | [2023-05-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-netweaver-changelog)  
SAP SAST Suite | Security | `SAP_SAST` | SYSLOG | [2023-12-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-sast-changelog)  
[SAP Security Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-security-audit) | N/A | `SAP_SECURITY_AUDIT` | JSON | [2026-03-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-security-audit-changelog)  
[SAP SM20](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-sm20) | Security Audit Log | `SAP_SM20` | JSON | [2025-07-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-sm20-changelog)  
[SAP SuccessFactors](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-successfactors) | Audit Log | `SAP_SUCCESSFACTORS` | CSV | [2024-04-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-successfactors-changelog)  
[SAP Webdispatcher](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-webdisp) | Software WebSwitch | `SAP_WEBDISP` | SYSLOG | [2026-01-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-webdisp-changelog)  
[Saviynt Enterprise Identity Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/saviynt-eip) | Endpoints | `SAVIYNT_EIP` | JSON, JSON+KV | [2023-06-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/saviynt-eip-changelog)  
[SecureAuth](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/secureauth-sso) | SSO | `SECUREAUTH_SSO` | SYSLOG, XML, JSON+KV | [2026-04-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/secureauth-sso-changelog)  
[SecureLink](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/securelink) | Remote Access Tools | `SECURELINK` | SYSLOG | [2026-09-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/securelink-changelog)  
[Semperis DSP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/semperis-dsp) | LDAP | `SEMPERIS_DSP` | SYSLOG | [2025-09-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/semperis-dsp-changelog)  
Sendmail | Email Server | `SENDMAIL` | SYSLOG + KV | [2026-07-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sendmail-changelog)  
[Sentinelone Activity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinelone-activity) | Endpoint Security | `SENTINELONE_ACTIVITY` | JSON, SYSLOG+KV | [2026-06-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinelone-activity-changelog)  
[Sentinelone Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinelone-alert) | Endpoint Security | `SENTINELONE_ALERT` | JSON, CEF | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinelone-alert-changelog)  
[SentinelOne Singularity Cloud Funnel](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinelone-cf) | EVENTS | `SENTINELONE_CF` | JSON | [2026-06-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinelone-cf-changelog)  
[SentinelOne Deep Visibility](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinel-dv) | EDR | `SENTINEL_DV` | JSON | [2026-04-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinel-dv-changelog)  
[SentinelOne EDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinel-edr) | EDR | `SENTINEL_EDR` | SYSLOG + JSON | [2025-08-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinel-edr-changelog)  
[Sentry](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentry) | Data Security | `SENTRY` | JSON | [2025-01-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentry-changelog)  
[Symantec Endpoint Protection](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sep) | AV / Endpoint | `SEP` | SYSLOG, KV, JSON, SYSLOG + JSON | [2026-05-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sep-changelog)  
SEPPmail Secure Email | email encryption and signature solutions | `SEPPMAIL` | SYSLOG + KV | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/seppmail-changelog)  
Seqrite Endpoint Security (EPS) | AV and endpoint logs | `SEQRITE_ENDPOINT` | LEEF | [2023-03-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/seqrite-endpoint-changelog)  
[ServiceNow Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-audit) | SaaS Application | `SERVICENOW_AUDIT` | JSON, Syslog, kv | [2026-07-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/servicenow-audit-changelog)  
[ServiceNow CMDB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-cmdb) | Policy Management | `SERVICENOW_CMDB` | JSON | [2026-08-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/servicenow-cmdb-changelog)  
[ServiceNow Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-security) | SaaS Application | `SERVICENOW_SECURITY` | JSON | [2026-07-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/servicenow-security-changelog)  
[Microsoft SharePoint](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sharepoint) | Collaboration log types | `SHAREPOINT` | SYSLOG,CSV,JSON | [2025-03-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sharepoint-changelog)  
Shibboleth IDP | Identity and Access Management | `SHIBBOLETH_IDP` | SYSLOG, JSON | [2024-11-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/shibboleth-idp-changelog)  
Shrubbery TACACS+ | NETWORK MANAGEMENT | `SHRUBBERY_TACACS` | SYSLOG + KV | [2022-11-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/shrubbery-tacacs-changelog)  
Sierra Wireless | IOT Devices | `SIERRA_WIRELESS` | SYSLOG | [2023-11-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sierra-wireless-changelog)  
[Signal Sciences WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/signal-sciences-waf) | WAF | `SIGNAL_SCIENCES_WAF` | JSON | [2024-05-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/signal-sciences-waf-changelog)  
Silverfort Authentication Platform | Identity and Access Management | `SILVERFORT` | CEF SYSLOG + KV, SYSLOG + JSON | [2026-04-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/silverfort-changelog)  
Layer7 SiteMinder | SSO | `SITEMINDER_SSO` | KV+JSON, SYSLOG, JSON | [2025-02-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/siteminder-sso-changelog)  
Skybox Firewall Assurance | Firewall | `SKYBOX_FIREWALL_ASSURANCE` | SYSLOG + KV | [2023-09-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/skybox-firewall-assurance-changelog)  
[Slack Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/slack-audit) | Productivity | `SLACK_AUDIT` | JSON | [2026-09-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/slack-audit-changelog)  
[Smartsheet](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/smartsheet) | CASB | `SMARTSHEET` | JSON | [2024-12-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/smartsheet-changelog)  
Samba SMBD | Privileged Account Activity | `SMBD` | Syslog | [2023-03-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/smbd-changelog)  
Snare System Diagnostic Logs | Security | `SNARE_SOLUTIONS` | SYSLOG + KV , SYSLOG + JSON | [2025-11-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snare-solutions-changelog)  
[Snipe-IT](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snipe-it) | SaaS Applications | `SNIPE_IT` | JSON | [2025-02-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snipe-it-changelog)  
Snoopy Logger | Log Aggregator | `SNOOPY_LOGGER` | SYSLOG | [2022-08-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snoopy-logger-changelog)  
[Snort](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snort-ids) | IDS/IPS | `SNORT_IDS` | SYSLOG + JSON | [2024-12-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snort-ids-changelog)  
[Snowflake](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snowflake) | Database | `SNOWFLAKE` | JSON, CSV | [2026-08-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snowflake-changelog)  
[Snyk Group level audit/issues logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-issues) | Security | `SNYK_ISSUES` | JSON | [2025-12-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snyk-issues-changelog)  
[Snyk Group level audit Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-sdlc) | Vulnerability Scanners | `SNYK_SDLC` | JSON | [2026-03-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snyk-sdlc-changelog)  
Solaris system | OS | `SOLARIS_SYSTEM` | SYSLOG | [2025-12-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/solaris-system-changelog)  
Solarwinds Kiwi Syslog Server | Security Log | `SOLARWINDS_KSS` | SYSLOG + KV | [2024-06-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/solarwinds-kss-changelog)  
Sonicwall Secure Mobile Access | Authentication | `SONICWALL_SMA` | SYSLOG + KV, JSON | [2025-03-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sonicwall-sma-changelog)  
[SonicWall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sonic-firewall) | Firewall | `SONIC_FIREWALL` | SYSLOG + KV | [2026-07-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sonic-firewall-changelog)  
[Sonrai Enterprise Cloud Security Solution](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sonrai) | Cloud Security Solution | `SONRAI` | JSON | [2024-06-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sonrai-changelog)  
[Sophos AV](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-av) | AV / Endpoint | `SOPHOS_AV` | CSV, JSON | [2024-08-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-av-changelog)  
[Sophos Capsule8](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-capsule8) | Container Security | `SOPHOS_CAPSULE8` | JSON | 2021-12-22  
[Sophos Central](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-central) | AV / Endpoint | `SOPHOS_CENTRAL` | JSON | [2026-02-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-central-changelog)  
[Sophos DHCP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-dhcp) | DHCP | `SOPHOS_DHCP` | SYSLOG + KV | 2022-02-10  
[Sophos Intercept EDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-edr) | EDR logs | `SOPHOS_EDR` | JSON | [2024-06-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-edr-changelog)  
[Sophos Firewall (Next Gen)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-firewall) | Firewall | `SOPHOS_FIREWALL` | KV, SYSLOG + KV | [2026-06-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-firewall-changelog)  
[Sophos UTM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-utm) | Unified Threat Management | `SOPHOS_UTM` | KV | [2025-07-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-utm-changelog)  
[SOTI MobiControl](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/soti-mobicontrol) | Mobile Device Management | `SOTI_MOBICONTROL` | SYSLOG | [2023-09-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/soti-mobicontrol-changelog)  
Sourcefire | IDS/IPS | `SOURCEFIRE_IDS` | JSON, CEF | [2026-10-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sourcefire-ids-changelog)  
[Splunk Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/splunk) | Security log | `SPLUNK` | JSON | [2024-05-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/splunk-changelog)  
[Splunk Attack Analyzer](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/splunk-attack-analyzer) | CLOUD SECURITY | `SPLUNK_ATTACK_ANALYZER` | JSON | [2024-08-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/splunk-attack-analyzer-changelog)  
Spur data feeds | Vulnerability Management | `SPUR_FEEDS` | JSON | [2024-05-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/spur-feeds-changelog)  
[SpyCloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/spycloud) | AV / Endpoint | `SPYCLOUD` | SYSLOG + JSON , JSON | [2025-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/spycloud-changelog)  
Squid Web Proxy | Web Proxy | `SQUID_WEBPROXY` | SYSLOG | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/squid-webproxy-changelog)  
StackHawk | Vulnerability scanners | `STACKHAWK` | JSON | [2025-02-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stackhawk-changelog)  
[Stealthbits Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stealthbits-audit) | File system monitoring | `STEALTHBITS_AUDIT` | JSON | 2021-11-09  
[Stealthbits Defend](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stealthbits-defend) | Security System for Active Directory and File Systems. | `STEALTHBITS_DEFEND` | SYSLOG + KV (LEEF, CEF) | [2026-08-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stealthbits-defend-changelog)  
Stealthbits PAM | Privileged Access Management Solution | `STEALTHBITS_PAM` | CEF + KV | [2023-11-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stealthbits-pam-changelog)  
[Riverbed Steelhead](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/steelhead) | Network Management and Optimization | `STEELHEAD` | JSON , SYSLOG | [2025-06-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/steelhead-changelog)  
[STIX Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stix) | Cybersecurity Threats | `STIX` | SYSLOG + KV (CEF), JSON | [2026-09-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stix-changelog)  
Stormshield Firewall | FIREWALL | `STORMSHIELD_FIREWALL` | SYSLOG + KV | [2026-02-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stormshield-firewall-changelog)  
Strong Swan VPN | VPN | `STRONGSWAN_VPN` | JSON | 2023-05-25  
Sublime Security | Vulnerability scanners | `SUBLIMESECURITY` | JSON | [2026-09-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sublimesecurity-changelog)  
[Suricata EVE](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/suricata-eve) | IPS IDS | `SURICATA_EVE` | JSON | [2026-05-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/suricata-eve-changelog)  
Suricata IDS | IDS/IPS | `SURICATA_IDS` | JSON | [2024-12-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/suricata-ids-changelog)  
[Swift Alliance Messaging Hub](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/swift-amh) | Finance | `SWIFT_AMH` | JSON | [2025-11-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/swift-amh-changelog)  
[Swimlane Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/swimlane) | SOAR Tools | `SWIMLANE` | JSON | [2025-02-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/swimlane-changelog)  
[Symantec CloudSOC CASB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-casb) | CASB | `SYMANTEC_CASB` | SYSLOG + JSON, JSON | [2024-10-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-casb-changelog)  
[Symantec DLP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-dlp) | DLP | `SYMANTEC_DLP` | SYSLOG + KV (CEF), XML, CEF | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-dlp-changelog)  
[Symantec EDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-edr) | EDR | `SYMANTEC_EDR` | JSON | [2026-06-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-edr-changelog)  
[Symantec Event export](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-event-export) | SEP | `SYMANTEC_EVENT_EXPORT` | JSON, SYSLOG | [2026-09-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-event-export-changelog)  
[Symantec Messaging Gateway](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-mail) | Email server log types. | `SYMANTEC_MAIL` | JSON | [2025-12-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-mail-changelog)  
[Symantec Security Analytics](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-sa) | Vulnerability scanners | `SYMANTEC_SA` | SYSLOG + KV | [2025-05-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-sa-changelog)  
[Symantec VIP Gateway](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-vip) | Email Server | `SYMANTEC_VIP` | SYSLOG | [2023-03-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-vip-changelog)  
[Symantec VIP Authentication Hub](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-vip-authhub) | VPN | `SYMANTEC_VIP_AUTHHUB` | JSON | [2025-03-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-vip-authhub-changelog)  
[Symantec Web Isolation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-web-isolation) | Secure Access Service Edge | `SYMANTEC_WEB_ISOLATION` | JSON | [2023-11-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-web-isolation-changelog)  
[Symantec Web Security Service](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-wss) | Web Proxy | `SYMANTEC_WSS` | JSON | [2025-07-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-wss-changelog)  
[Synology](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/synology) | DATA STORAGE | `SYNOLOGY` | SYSLOG , JSON | [2026-09-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/synology-changelog)  
[Sysdig](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sysdig) | Security | `SYSDIG` | JSON | [2026-05-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sysdig-changelog)  
[Tableau](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tableau) | Web server | `TABLEAU` | JSON, KV, SYSLOG | [2026-08-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tableau-changelog)  
TACACS Plus | Authentication log types | `TACACS_PLUS` | SYSLOG | [2025-03-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tacacs-plus-changelog)  
[Tailscale](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tailscale) | CASB | `TAILSCALE` | JSON | [2024-11-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tailscale-changelog)  
[Talon](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/talon) | Security | `TALON` | JSON | 2023-12-21  
[Tanium Asset](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-asset) | Tanium Specific | `TANIUM_ASSET` | JSON, SYSLOG + KV | [2025-01-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-asset-changelog)  
[Tanium Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-audit) | SCAN NETWORK | `TANIUM_AUDIT` | JSON | [2025-11-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-audit-changelog)  
[Tanium Comply](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-comply) | Tanium Specific | `TANIUM_COMPLY` | JSON | [2023-10-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-comply-changelog)  
[Tanium Discover](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-discover) | Tanium Specific | `TANIUM_DISCOVER` | JSON | [2022-11-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-discover-changelog)  
[Tanium Insight](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-insight) | Tanium Specific | `TANIUM_INSIGHT` | SYSLOG + KV | 2021-03-10  
[Tanium Integrity Monitor](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-integrity-monitor) | Tanium Specific | `TANIUM_INTEGRITY_MONITOR` | JSON | [2025-10-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-integrity-monitor-changelog)  
[Tanium Patch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-patch) | Tanium Specific | `TANIUM_PATCH` | JSON | 2022-02-08  
[Tanium Question](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-question) | TANIUM Logs | `TANIUM_QUESTION` | JSON | [2025-05-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-question-changelog)  
[Tanium Reveal](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-reveal) | Tanium Specific | `TANIUM_REVEAL` | JSON | 2021-11-15  
[Tanium Stream](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-th) | Tanium Specific | `TANIUM_TH` | JSON | [2026-09-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-th-changelog)  
[Tanium Threat Response](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-threat-response) | Tanium Specific | `TANIUM_THREAT_RESPONSE` | JSON | [2026-07-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-threat-response-changelog)  
[TCPWave DDI](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi) | Secure ddi | `TCPWAVE_DDI` | SYSLOG + JSON, SYSLOG | [2026-09-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tcpwave-ddi-changelog)  
[TeamViewer](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teamviewer) | Remote Support | `TEAMVIEWER` | JSON | [2025-12-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teamviewer-changelog)  
[Team Cymru Scout Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/team-cymru-scout-threatintel) | Threat Intel | `TEAM_CYMRU_SCOUT_THREATINTEL` | JSON | [2024-08-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/team-cymru-scout-threatintel-changelog)  
[Teleport Access Plane](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teleport-access-plane) | Remote Access | `TELEPORT_ACCESS_PLANE` | SYSLOG, JSON, SYSLOG+JSON | [2026-09-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teleport-access-plane-changelog)  
Tenable Active Directory Security | Tenable Active Directory Security | `TENABLE_ADS` | SYSLOG + KV | [2026-03-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-ads-changelog)  
[Tenable Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tenable-audit) | Application server | `TENABLE_AUDIT` | JSON | [2024-08-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-audit-changelog)  
[Tenable CSPM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tenable-cspm) | Cloud Security | `TENABLE_CSPM` | JSON | [2025-02-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-cspm-changelog)  
[tenable.io](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tenable-io) | Vulnerability Scanner | `TENABLE_IO` | JSON | [2026-08-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-io-changelog)  
Tenable OT | Vulnerability Scanners | `TENABLE_OT` | SYSLOG+CEF | [2025-11-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-ot-changelog)  
Tenable Security Center | Vulnerability Scanner | `TENABLE_SC` | SYSLOG, JSON+SYSLOG, JSON | [2026-09-16  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-sc-changelog)  
[Teradata DB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teradata-db) | Database log types | `TERADATA_DB` | SYSLOGgcert | [2025-06-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teradata-db-changelog)  
[Terraform Enterprise Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/terraform-enterprise) | IT infrastructure | `TERRAFORM_ENTERPRISE` | JSON, KV, SYSLOG | [2025-03-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/terraform-enterprise-changelog)  
[Tetragon Ebpf Audit Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tetragon-ebpf-audit-logs) | OS | `TETRAGON_EBPF_AUDIT_LOGS` | JSON | [2024-03-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tetragon-ebpf-audit-logs-changelog)  
Thales Digital Identity and Security | Digital Identity & Security | `THALES_DIS` | SYSLOG | 2022-03-17  
Thales Luna Hardware Security Module | THALES_LUNA_HSM specific | `THALES_LUNA_HSM` | JSON/SYSLOG | [2025-09-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thales-luna-hsm-changelog)  
Thales MFA | Authentication | `THALES_MFA` | SYSLOG + KV (CEF) | [2025-11-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thales-mfa-changelog)  
[Thinkst Canary](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/thinkst-canary) | Deception Software | `THINKST_CANARY` | JSON, SYSLOG+KV | [2026-07-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thinkst-canary-changelog)  
[ThreatConnect](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc) | IOC | `THREATCONNECT_IOC` | JSON | 2022-01-13  
[ThreatConnect IOC V3](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc-v3) | IOC | `THREATCONNECT_IOC_V3` | JSON | [2026-07-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/threatconnect-ioc-v3-changelog)  
[ThreatLocker Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatlocker) | THREATLOCKER | `THREATLOCKER` | JSON | [2026-07-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/threatlocker-changelog)  
[ThreatX WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatx-waf) | WAF | `THREATX_WAF` | SYSLOG, JSON | [2025-01-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/threatx-waf-changelog)  
Thycotic | Identity and Access Management | `THYCOTIC` | SYSLOG + KV (CEF) | [2024-10-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thycotic-changelog)  
[Tines](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tines) | Data Security | `TINES` | JSON | [2024-10-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tines-changelog)  
[TINTRI](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tintri) | Data Security | `TINTRI` | syslog | [2024-09-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tintri-changelog)  
Trend Micro | SMS, UNITY_ONE | `TIPPING_POINT` | SYSLOG | [2026-02-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tipping-point-changelog)  
[Apache Tomcat](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tomcat) | Web server | `TOMCAT` | JSON | [2025-02-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tomcat-changelog)  
Trellix EDRF Trace Data and Telemetry | Application server logs | `TRELLIX_EDRF` | JSON | [2026-05-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-edrf-changelog)  
[Trellix HX Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-alerts) | EDR | `TRELLIX_HX_ALERTS` | JSON | [2026-09-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-alerts-changelog)  
[Trellix HX Audit Events](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-audit) | AV and endpoint logs | `TRELLIX_HX_AUDIT` | XML | [2026-10-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-audit-changelog)  
Trellix HX Event Streamer | Cybersecurity | `TRELLIX_HX_ES` | SYSLOG + KV, KV+JSON | [2026-08-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-es-changelog)  
[Trellix HX Hosts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-hosts) | EDR | `TRELLIX_HX_HOSTS` | JSON | [2024-11-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-hosts-changelog)  
[TrendMicro Apex Central](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-apex-central) | Endpoint | `TRENDMICRO_APEX_CENTRAL` | CEF | [2026-09-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-apex-central-changelog)  
[Trend Micro Apex one](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-apex-one) | Endpoint Security | `TRENDMICRO_APEX_ONE` | SYSLOG + KV | [2026-04-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-apex-one-changelog)  
Trend Micro AV | AV / Endpoint | `TRENDMICRO_AV` | SYSLOG + KV, CEF | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-av-changelog)  
[Trend Micro Cloud one](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-cloudone) | Cloud Security | `TRENDMICRO_CLOUDONE` | SYSLOG, JSON | [2025-07-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-cloudone-changelog)  
[TrendMicro Deep Discovery Inspector](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-ddi) | Physical and virtual network | `TRENDMICRO_DDI` | SYSLOG | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-ddi-changelog)  
[Trend Micro Deep Security](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-deep-security) | AV / Endpoint | `TRENDMICRO_DEEP_SECURITY` | LEEF + CEF | [2026-04-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-deep-security-changelog)  
[Trend Micro Email Security Advanced](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-email-security) | Email Security | `TRENDMICRO_EMAIL_SECURITY` | CEF | [2026-10-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-email-security-changelog)  
TXOne Stellar | AV and Endpoint logs | `TRENDMICRO_STELLAR` | SYSLOG , JSON, SYSLOG+KV | [2026-03-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-stellar-changelog)  
[Trend Micro Vision One](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one) | AV and endpoint logs | `TRENDMICRO_VISION_ONE` | SYSLOG + KV, CEF, JSON | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-changelog)  
[Trend Micro Vision One Activity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-activity) | Schema | `TRENDMICRO_VISION_ONE_ACTIVITY` | JSON | [2025-08-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-activity-changelog)  
[Trend Micro Vision One Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-audit) | Schema | `TRENDMICRO_VISION_ONE_AUDIT` | JSON | [2026-09-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-audit-changelog)  
Trend Micro Vision One Container Vulnerabilities | Schema | `TRENDMICRO_VISION_ONE_CONTAINER_VULNERABILITIES` | JSON | [2025-04-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-container-vulnerabilities-changelog)  
[Trend Micro Vision One Detections](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-detections) | Schema | `TRENDMICRO_VISION_ONE_DETECTIONS` | JSON | [2026-05-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-detections-changelog)  
Trend Micro Vision One Endpoint Vulnerabilities | schema | `TRENDMICRO_VISION_ONE_ENDPOINT_VULNERABILITIES` | JSON | [2026-03-14  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-endpoint-vulnerabilities-changelog)  
Trend Micro Vision One Observerd Attack Techniques | Schema | `TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES` | JSON | [2026-10-05  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-observerd-attack-techniques-changelog)  
[Trend Micro Vision One Workbench](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-workbench) | Schema | `TRENDMICRO_VISION_ONE_WORKBENCH` | JSON | [2026-08-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-workbench-changelog)  
TrendMicro Web Proxy | Web Proxy | `TRENDMICRO_WEBPROXY` | SYSLOG + KV | [2024-03-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-webproxy-changelog)  
[Tripwire](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tripwire-fim) | DLP | `TRIPWIRE_FIM` | SYSLOG | [2026-02-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tripwire-fim-changelog)  
[Twingate](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/twingate) | VPN | `TWINGATE` | JSON | [2024-12-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/twingate-changelog)  
[UberAgent](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/uberagent) | Security | `UBERAGENT` | CSV | [2024-12-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/uberagent-changelog)  
Ubika WAAP | WAF | `UBIKA_WAAP` | SYSLOG | [2024-06-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ubika-waap-changelog)  
[Ubika Waf](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ubika-waf) | WAF | `UBIKA_WAF` | JSON + SYSLOG, SYSLOG | [2026-03-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ubika-waf-changelog)  
[Ubiquiti UniFi Switch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ubiquiti-switch) | Switch | `UBIQUITI_SWITCH` | SYSLOG | [2026-08-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ubiquiti-switch-changelog)  
[UKG](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ukg) | NA | `UKG` | JSON | [2025-02-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ukg-changelog)  
[Cisco Umbrella DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-dns) | DNS | `UMBRELLA_DNS` | CSV, JSON | [2026-03-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-dns-changelog)  
[Cisco Umbrella Cloud Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-firewall) | Firewall | `UMBRELLA_FIREWALL` | CSV | [2026-06-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-firewall-changelog)  
[Cisco Umbrella IP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-ip) | Web Proxy | `UMBRELLA_IP` | SYSLOG | [2025-10-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-ip-changelog)  
[Cisco Umbrella Web Proxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-webproxy) | Web Proxy | `UMBRELLA_WEBPROXY` | CSV | [2026-06-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-webproxy-changelog)  
Unbound DNS | DNS | `UNBOUND_DNS` | SYSLOG | 2020-06-09  
Unifi AP | Switches and Routers | `UNIFI_AP` | SYSLOG + KV, SYSLOG + JSON | [2025-11-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/unifi-ap-changelog)  
UpGuard | Vulnerability scanners | `UPGUARD` | JSON | [2024-11-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/upguard-changelog)  
Upstream Vehicle SOC Alerts | Schema | `UPSTREAM_VSOC_ALERTS` | JSON | [2025-09-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/upstream-vsoc-alerts-changelog)  
[Uptycs EDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/uptycs-edr) | Endpoint detection and response | `UPTYCS_EDR` | JSON | [2026-08-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/uptycs-edr-changelog)  
Upwind | Cloud Security | `UPWIND` | JSON | [2026-08-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/upwind-changelog)  
[UPX AntiDDoS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/upx-antiddos) | DDOS Mitigation | `UPX_ANTIDDOS` | JSON | [2025-02-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/upx-antiddos-changelog)  
[URLScan IO](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/urlscan-io) | Vulnerability scanners | `URLSCAN_IO` | JSON | [2024-10-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/urlscan-io-changelog)  
[VanDyke SFTP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vandyke-sftp) | Data Transfer | `VANDYKE_SFTP` | JSON, SYSLOG | [2025-05-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vandyke-sftp-changelog)  
[Varonis](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/varonis) | Data Security / Insider Threat | `VARONIS` | SYSLOG + KV (CEF), LEEF, JSON | [2026-07-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/varonis-changelog)  
[Vectra Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-alerts) | Content Management Software | `VECTRA_ALERTS` | JSON | [2025-02-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-alerts-changelog)  
[Vectra Detect](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-detect) | NDR | `VECTRA_DETECT` | JSON + SYSLOG + CEF | [2025-12-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-detect-changelog)  
[Vectra Stream](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-stream) | NDR | `VECTRA_STREAM` | JSON + SYSLOG + CEF | [2025-08-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-stream-changelog)  
[Vectra XDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-xdr) | NDR | `VECTRA_XDR` | JSON | [2026-04-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-xdr-changelog)  
[Veeam](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veeam) | Backup software | `VEEAM` | SYSLOG+KV | [2026-05-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/veeam-changelog)  
[Velo Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/velo-firewall) | FIREWALL | `VELO_FIREWALL` | SYSLOG + KV, SYSLOG | [2026-02-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/velo-firewall-changelog)  
[Venafi ZTPKI](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/venafi-ztpki) | AV and Endpoint logs | `VENAFI_ZTPKI` | SYSLOG , JSON , CSV | [2026-09-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/venafi-ztpki-changelog)  
[Verba Recording System](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/verba-rec) | Recording System | `VERBA_REC` | CSV | [2024-05-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/verba-rec-changelog)  
[Vercel WAF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vercel-waf) | Firewall log | `VERCEL_WAF` | JSON | 2024-12-20  
[VeridiumID by Veridium](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veridium-id) | Authentication Software | `VERIDIUM_ID` | Syslog + KV | [2024-06-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/veridium-id-changelog)  
[Veritas NetBackup](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veritas-netbackup) | Backup software | `VERITAS_NETBACKUP` | SYSLOG | [2026-02-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/veritas-netbackup-changelog)  
[Versa Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/versa-firewall) | FIREWALL | `VERSA_FIREWALL` | SYSLOG + KV | [2026-01-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/versa-firewall-changelog)  
[Virtru Email Encryption](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/virtru-email-encryption) | EMAIL SERVER | `VIRTRU_EMAIL_ENCRYPTION` | JSON | [2024-12-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/virtru-email-encryption-changelog)  
[Nokia VitalQIP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vitalqip) | DDI (DNS, DHCP, IPAM) | `VITALQIP` | SYSLOG | 2022-03-01  
Vmware Avinetworks iWAF | Server | `VMWARE_AVINETWORKS_IWAF` | SYSLOG, SYSLOG+JSON | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-avinetworks-iwaf-changelog)  
[VMware ESXi](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-esx) | Hypervisor | `VMWARE_ESX` | SYSLOG, JSON, SYSLOG+KV | [2026-08-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-esx-changelog)  
[VMware Horizon](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-horizon) | VDI | `VMWARE_HORIZON` | SYSLOG, KV | [2026-03-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-horizon-changelog)  
[VMware NSX](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-nsx) | Network and Security Virtualization | `VMWARE_NSX` | KV | [2026-01-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-nsx-changelog)  
[VMware Tanzu Kubernetes Grid](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-tanzu) | IDS/IPS | `VMWARE_TANZU` | JSON + SYSLOG+JSON | [2023-09-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-tanzu-changelog)  
[VMware vCenter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vcenter) | Server | `VMWARE_VCENTER` | SYSLOG + JSON, LEEF | [2026-09-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-vcenter-changelog)  
[VMware vRealize Suite (VMware Aria)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vrealize) | Cloud | `VMWARE_VREALIZE` | SYSLOG | [2026-09-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-vrealize-changelog)  
[VMWare VSphere](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vsphere) | virtualization | `VMWARE_VSPHERE` | SYSLOG + CSV | [2026-06-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-vsphere-changelog)  
[VMware Workspace ONE](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-workspace-one) | Logging and Troubleshooting | `VMWARE_WORKSPACE_ONE` | SYSLOG | [2023-08-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-workspace-one-changelog)  
[Voltage](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/voltage) | Email Server | `VOLTAGE` | SYSLOG | [2025-06-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/voltage-changelog)  
Thales Vormetric | Encryption | `VORMETRIC` | SYSLOG, SYSLOG+JSON | [2026-07-31  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vormetric-changelog)  
[Vsftpd](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vsftpd) | FTP Server | `VSFTPD` | GROK | [2023-11-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vsftpd-changelog)  
[VyOS Open Source Router](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vyos) | DHCP | `VYOS` | SYSLOG | [2022-10-12  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vyos-changelog)  
[Wallix Bastion](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wallix-bastion) | Privileged Account Activity | `WALLIX_BASTION` | SYSLOG, SYSLOG + KV | [2026-09-24  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wallix-bastion-changelog)  
[WatchGuard](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/watchguard) | Syslog and KV | `WATCHGUARD` | JSON, LEEF, SYSLOG | [2026-08-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/watchguard-changelog)  
[Watchguard EDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/watchguard-edr) | EDR | `WATCHGUARD_EDR` | JSON | [2026-02-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/watchguard-edr-changelog)  
[Wazuh](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wazuh) | Log Aggregator | `WAZUH` | SYSLOG + JSON | [2025-03-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wazuh-changelog)  
Trustwave webmarshal | Proxy Server | `WEBMARSHAL` | SYSLOG + CSV | [2023-04-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/webmarshal-changelog)  
[WindChill](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windchill) | Lifecycle Management Software | `WINDCHILL` | SYSLOG | [2024-11-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windchill-changelog)  
[Microsoft AD](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-ad) | LDAP | `WINDOWS_AD` | JSON | [2026-08-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-ad-changelog)  
[Windows Applocker](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-applocker) | Application Locker | `WINDOWS_APPLOCKER` | SYSLOG + KV + JSON + XML | [2023-10-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-applocker-changelog)  
[Windows Defender ATP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-defender-atp) | AV / Endpoint | `WINDOWS_DEFENDER_ATP` | SYSLOG + JSON, XML, JSON | [2024-10-15  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-defender-atp-changelog)  
[Windows Defender AV](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-defender-av) | AV / Endpoint | `WINDOWS_DEFENDER_AV` | SYSLOG + JSON, XML, JSON | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-defender-av-changelog)  
[Windows DHCP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-dhcp) | DHCP | `WINDOWS_DHCP` | JSON, SYSLOG, CSV | [2025-08-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-dhcp-changelog)  
[Windows DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-dns) | DNS | `WINDOWS_DNS` | JSON, XML, SYSLOG + KV | [2026-09-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-dns-changelog)  
[Windows Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-firewall) | Firewall | `WINDOWS_FIREWALL` | Space Separated Value | 2021-08-26  
[Windows Hyper-V](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-hyperv) | Virtualization Software | `WINDOWS_HYPERV` | JSON | [2025-06-17  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-hyperv-changelog)  
[Windows Network Policy Server](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-net-policy-server) | Authentication | `WINDOWS_NET_POLICY_SERVER` | SYSLOG, JSON, SYSLOG + XML | [2024-12-26  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-net-policy-server-changelog)  
[Windows Sysmon](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-sysmon) | DNS | `WINDOWS_SYSMON` | JSON, XML | [2026-09-01  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-sysmon-changelog)  
[Windows Event](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/winevtlog) | Endpoint | `WINEVTLOG` | JSON,XML,SYSLOG+KV,SYSLOG+JSON,SYSLOG+XML | [2026-09-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/winevtlog-changelog)  
[Windows Event (XML)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/winevtlog-xml) | AV / Endpoint | `WINEVTLOG_XML` | SYSLOG + XML, KV, SYSLOG + JSON, SYSLOG + CSV | [2026-09-04  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/winevtlog-xml-changelog)  
[Winscp](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/winscp) | Data Transfer | `WINSCP` | SYSLOG, CSV | [2024-05-22  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/winscp-changelog)  
[wiz.io](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wiz-io) | Identity and Access Management | `WIZ_IO` | JSON | [2026-09-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wiz-io-changelog)  
[WordPress](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wordpress-cms) | Configuration Management | `WORDPRESS_CMS` | JSON | [2024-05-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wordpress-cms-changelog)  
[Workday](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday) | SaaS Application | `WORKDAY` | JSON, CSV | [2024-06-25  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workday-changelog)  
[Workday Audit Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday-audit) | Audit And Compliance | `WORKDAY_AUDIT` | CSV | [2026-02-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workday-audit-changelog)  
[Workday User Activity](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday-user-activity) | N/A | `WORKDAY_USER_ACTIVITY` | SYSLOG + JSON , JSON | [2026-05-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workday-user-activity-changelog)  
[Workspace Activities](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workspace-activity) | Google Cloud Specific | `WORKSPACE_ACTIVITY` | JSON | [2026-09-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-activity-changelog)  
Workspace Alerts | Google Cloud Specific | `WORKSPACE_ALERTS` | JSON | [2026-01-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-alerts-changelog)  
Workspace ChromeOS Devices | Google Cloud Specific | `WORKSPACE_CHROMEOS` | JSON | [2024-12-03  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-chromeos-changelog)  
Workspace Groups | Google Cloud Specific | `WORKSPACE_GROUPS` | JSON | [2023-11-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-groups-changelog)  
Workspace Mobile Devices | Google Cloud Specific | `WORKSPACE_MOBILE` | JSON | [2023-11-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-mobile-changelog)  
Workspace Privileges | Google Cloud Specific | `WORKSPACE_PRIVILEGES` | JSON | [2023-11-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-privileges-changelog)  
Workspace Users | Google Cloud Specific | `WORKSPACE_USERS` | JSON | [2025-08-27  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workspace-users-changelog)  
[WPEngine](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wpengine) | Firewall log types | `WPENGINE` | SYSLOG | [2025-02-11  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wpengine-changelog)  
[XAMS by Xiting](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/xiting-xams) | Log Aggregator | `XITING_XAMS` | SYSLOG | [2026-08-23  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/xiting-xams-changelog)  
[YAMAHA ROUTER RTX1200](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/yamaha-router) | Switches AND Routers | `YAMAHA_ROUTER` | SYSLOG | [2024-04-19  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/yamaha-router-changelog)  
[Yubico OTP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/yubico-otp) | Audit event | `YUBICO_OTP` | SYSLOG, JSON, CSV | [2023-02-20  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/yubico-otp-changelog)  
[Zendesk CRM](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zendesk-crm) | Ticketing Applications | `ZENDESK_CRM` | JSON | [2025-09-02  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zendesk-crm-changelog)  
[ZeroFox Platform](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zerofox-platform) | Database | `ZEROFOX_PLATFORM` | JSON | [2025-03-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zerofox-platform-changelog)  
[Zero Networks](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zero-networks) | Security | `ZERO_NETWORKS` | JSON | [2025-03-13  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zero-networks-changelog)  
Zimperium | Mobile Device Management | `ZIMPERIUM` | SYSLOG + JSON | [2026-06-18  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zimperium-changelog)  
[Zix Email Encryption](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zix-email-encryption) | Email Server | `ZIX_EMAIL_ENCRYPTION` | SYSLOG | [2024-05-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zix-email-encryption-changelog)  
[Zoom Operation Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zoom-operation-logs) | Operation-Specific | `ZOOM_OPERATION_LOGS` | SYSLOG, JSON+SYSLOG | [2026-09-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zoom-operation-logs-changelog)  
[Zscaler CASB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-casb) | CASB | `ZSCALER_CASB` | JSON | [2026-05-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-casb-changelog)  
[ZScaler Deception](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-deception) | VPN | `ZSCALER_DECEPTION` | SYSLOG+JSON | [2026-06-29  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-deception-changelog)  
[Zscaler DLP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-dlp) | Data Loss Prevention | `ZSCALER_DLP` | JSON | [2026-04-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-dlp-changelog)  
[ZScaler DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-dns) | DNS | `ZSCALER_DNS` | JSON | [2026-01-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-dns-changelog)  
[Zscaler Email DLP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-email-dlp) | Email DLP | `ZSCALER_EMAIL_DLP` | JSON | [2026-04-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-email-dlp-changelog)  
[ZScaler NGFW](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-firewall) | Firewall | `ZSCALER_FIREWALL` | JSON | [2026-05-28  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-firewall-changelog)  
[Zscaler Internet Access Audit Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-internet-access) | Security Service Edge (SSE) | `ZSCALER_INTERNET_ACCESS` | JSON | [2026-01-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-internet-access-changelog)  
[Zscaler NSS Feeds for Alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-nss-feeds) | Alert log types | `ZSCALER_NSS_FEEDS` | JSON | [2024-10-21  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-nss-feeds-changelog)  
[Zscaler Tunnel](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-tunnel) | N/A | `ZSCALER_TUNNEL` | JSON | [2026-01-06  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-tunnel-changelog)  
[ZScaler VPN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-vpn) | VPN | `ZSCALER_VPN` | SYSLOG + CSV, JSON | [2026-02-10  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-vpn-changelog)  
[Zscaler](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-webproxy) | Web Proxy | `ZSCALER_WEBPROXY` | JSON | [2026-06-09  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-webproxy-changelog)  
[Zscaler Private Access](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-zpa) | Security Service Edge | `ZSCALER_ZPA` | JSON | [2026-06-30  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-zpa-changelog)  
[Zscaler Secure Private Access Audit Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-zpa-audit) | AUDIT | `ZSCALER_ZPA_AUDIT` | JSON | [2026-01-07  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-zpa-audit-changelog)  
[Zywall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zywall) | Network infrastructure | `ZYWALL` | KV | [2025-12-08  
View Change](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zywall-changelog)  
  
## Supported log types without a default parser

Google Security Operations SIEM does not provide a default parser for these log types. You can ingest raw logs from these devices using the Google Security Operations SIEM Ingestion API or the Google Security Operations SIEM forwarder. Google Security Operations SIEM will not normalize the data to structured Unified Data Model format.

You can create a [custom parser](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates) to normalize these logs. You can also [search raw logs](https://docs.cloud.google.com/chronicle/docs/investigation/search-raw-logs).

Vendor / Product | Log type  
---|---  
Absolute Secure Endpoint | `ABSOLUTE_SECURE_ENDPOINT`  
Accenture Synthetic | `ACCENTURE_SYNTHETIC`  
Accops Hysecure VPN | `ACCOPS_HYSECURE_VPN`  
Acquia Cloud Platform | `ACQUIA_CLOUD_PLATFORM`  
Acronis Backup | `ACRONIS`  
Action1 | `ACTION1`  
Active Identity HID | `ACTIVE_IDENTITY_HID`  
Microsoft ActiveSync | `ACTIVE_SYNC`  
Adaptive Shield | `ADAPTIVE_SHIELD`  
Adaxes | `ADAXES`  
Addigy MDM | `ADDIGY_MDM`  
Admin by request PAM | `ADMIN_BY_REQUEST`  
Adobe Commerce | `ADOBE_COMMERCE`  
Adobe Experience Manager | `ADOBE_EXPERIENCE_MANAGER`  
Adobe Experience Platform | `ADOBE_EXPERIENCE_PLATFORM`  
Adobe I/O Runtime | `ADOBE_IO_RUNTIME`  
ManageEngine ADSelfService Plus | `ADSELFSERVICE_PLUS`  
ADTRAN NetVanta router | `ADTRAN_NETVANTA`  
Adyen Platform | `ADYEN`  
Agari Phishing Defense | `AGARI_PHISHING_DEFENSE`  
Aikido | `AIKIDO`  
Airbus Security Logging (ACD AISD) | `AIRBUS_SECURITY_LOG`  
Extreme Networks AirDefense | `AIRDEFENSE`  
Airwatch Context | `AIRWATCH_CONTEXT`  
Air Table | `AIR_TABLE`  
Akamai API Security | `AKAMAI_API_SECURITY`  
Akamai Prolexic | `AKAMAI_DDOS`  
Akamai DHCP | `AKAMAI_DHCP`  
Akamai Enterprise Threat Protector | `AKAMAI_ETP`  
Akamai Event Viewer | `AKAMAI_EVT_VWR`  
Akamai Guardicore | `AKAMAI_GUARDICORE`  
Akamai Kona Edge Grid | `AKAMAI_KONA_EDGE_GRID`  
Akamai Log Delivery Service | `AKAMAI_LDS`  
Akamai MFA | `AKAMAI_MFA`  
AlertLogic Notifications | `ALERTLOGIC_NOTIFICATIONS`  
Alert Enterprise Guardian | `ALERT_GUARDIAN`  
Alibaba Security Center | `ALIBABA_SECURITY_CENTER`  
AliCloud ActionTrail | `ALICLOUD_ACTIONTRAIL`  
AliCloud Anti DDos | `ALICLOUD_ANTI_DDOS`  
Alicloud ApsaraDB | `ALICLOUD_APSARADB`  
AliCloud Firewall | `ALICLOUD_FIREWALL`  
AliCloud WAF | `ALICLOUD_WAF`  
AlienVault Open Threat Exchange | `ALIENVAULT_OTX`  
Alkira IP Flow | `ALKIRA_IP_FLOW`  
Allot NetEnforcer | `ALLOT_NETENFORCER`  
Altiris Logs | `ALTIRIS_LOGS`  
Amavis | `AMAVIS`  
Amazon Bedrock Model Invocation Logging | `AMAZON_BEDROCK_MODEL_INVOCATION_LOGGING`  
Analyst1 IOC | `ANALYST1_IOC`  
Anzenna | `ANZENNA`  
Apache Airflow | `APACHE_AIRFLOW`  
Apache Kafka Audit | `APACHE_KAFKA_AUDIT`  
Apache SpamAssassin | `APACHE_SPAMASSASSIN`  
APC Automatic Transfer Switch | `APC_ATS`  
APC Netbotz | `APC_NETBOTZ`  
APC Power Distribution Unit | `APC_PDU`  
APC Smart-UPS | `APC_SMART_UPS`  
APC StruxureWare Portal | `APC_STRUXUREWARE`  
Apiiro Cloud Application Security Platform | `APIIRO`  
Appgate Software-defined Perimeter | `APPGATE_SDP`  
Appsentinels | `APPSENTINELS`  
AppSmith Audit | `APPSMITH_AUDIT`  
AppViewX | `APPVIEWX`  
Aptos Enterprise Order Management | `APTOS_EOM`  
Arcon PAM | `ARCON_PAM`  
Arctic Security Arctic Node | `ARCTIC_NODE`  
Argo CD | `ARGO_CD`  
Argo Workflows | `ARGO_WORKFLOWS`  
Arista Guardian For Network Identity | `ARISTA_AGNI`  
Arista CorvilNet DANZ Integration | `ARISTA_CORVILNET`  
Arista CloudVision Portal | `ARISTA_CVP`  
Arista Extensible Operating System | `ARISTA_EOS`  
Arista NDR | `ARISTA_NDR`  
Arize Cloud | `ARIZE_CLOUD`  
Arkime Packet Capture | `ARKIME_PCAP`  
Armis | `ARMIS`  
Armorblox Email Security | `ARMORBLOX_ESC`  
Armor Anywhere | `ARMOR_ANYWHERE`  
Array Networks WAF | `ARRAY_NETWORKS_WAF`  
Aruba Access Point | `ARUBA_AP`  
Aruba Orchestrator | `ARUBA_ORCHESTRATOR`  
Aruba Switches | `ARUBA_SWT`  
Arxan Threat Analytics | `ARXAN_THREAT_ANALYTICS`  
Asana | `ASANA`  
Ascertia | `ASCERTIA`  
Asimily | `ASIMILY`  
AssetNote | `ASSETNOTE`  
AstriX | `ASTRIX`  
Atlan | `ATLAN`  
Atlassian Beacon | `ATLASSIAN_BEACON`  
Atlassian Jira Confluence Json | `ATLASSIAN_CONFLUENCE_JSON`  
Atlassian Guard Detect | `ATLASSIAN_GUARD_DETECT`  
Atlassian Jira Json | `ATLASSIAN_JIRA_JSON`  
Attack IQ | `ATTACK_IQ`  
AT&T Netbond | `ATT_NETBOND`  
AudioCodes Voice DNA | `AUDIOCODES`  
AudioCodes Session Border Controller | `AUDIOCODES_SBC`  
Authentic8 Silo | `AUTHENTIC8_SILO`  
AuthMind | `AUTHMIND`  
Authx Identity Management | `AUTHX`  
Authx User Context | `AUTHX_USER_CONTEXT`  
Autodesk Cad Cam | `AUTODESK_CAD_CAM`  
Autodesk Vault | `AUTODESK_VAULT`  
Automox | `AUTOMOX_EPM`  
Avast Business | `AVAST_HUB`  
Avaya Aura Session Manager | `AVAYA_AURA_SESSION_MANAGER`  
Avaya Session Border Controller | `AVAYA_BORDER`  
Avaya Interactive Voice Response | `AVAYA_IVR`  
Avaya VSP Switch | `AVAYA_VSP`  
Avaya Wireless | `AVAYA_WIRELESS`  
Avaza | `AVAZA`  
AvePoint EnPower | `AVEPOINT_ENPOWER`  
Aviatrix Cloud Network Platform | `AVIATRIX`  
Avigilon Alta Cloud Security | `AVIGILON_ALTA_CLOUD_SECURITY`  
Avigilon Ava Security Camera | `AVIGILON_AVA_SECURITY_CAMERA`  
AppTrana Web Application Firewall | `AWS_APPTRANA`  
AWS Dasha | `AWS_DASHA`  
AWS Dynamo DB | `AWS_DYNAMO_DB`  
AWS Elastic Kubernetes Service | `AWS_EKS`  
Amazon ElastiCache | `AWS_ELASTI_CACHE`  
Amazon FSx for Windows File Server | `AWS_FSX`  
AWS Inspector2 | `AWS_INSPECTOR2`  
AWS NGINX | `AWS_NGINX`  
AWS PY Tools | `AWS_PY_TOOLS`  
AWS Simple Email Service | `AWS_SES`  
AWS Shield | `AWS_SHIELD`  
Axis Atmos | `AXIS_ATMOS`  
Axis Camera | `AXIS_CAMERA`  
Axis License Plate Reader | `AXIS_LPR`  
Axis Security Audit | `AXIS_OS`  
Axonius Cybersecurity Asset Management | `AXONIUS`  
Axway | `AXWAY`  
Microsoft Azure | `AZURE`  
Azure AD Password Protection | `AZURE_AD_PASSWORD_PROTECTION`  
Azure AD Provisioning | `AZURE_AD_PROVISIONING`  
Azure App Configuration | `AZURE_APPCONFIGURATION`  
Azure App Platform | `AZURE_APPPLATFORM`  
Azure ArcData | `AZURE_ARCDATA`  
Azure ATP | `AZURE_ATP`  
Azure Authorization | `AZURE_AUTHORIZATION`  
Azure Bastion | `AZURE_BASTION`  
Azure Change Analysis | `AZURE_CHANGEANALYSIS`  
Azure Compute | `AZURE_COMPUTE`  
Azure Container Registry | `AZURE_CONTAINER_REGISTRY`  
Azure DataFactory | `AZURE_DATAFACTORY`  
Azure DNS logs | `AZURE_DNS`  
Azure DocumentDB | `AZURE_DOCUMENTDB`  
Azure Event Grid | `AZURE_EVENTGRID`  
Azure Event Hub | `AZURE_EVENTHUB`  
Azure Application Gateway for Containers | `AZURE_GATEWAY_CONTAINERS`  
Azure Hybrid Compute | `AZURE_HYBRIDCOMPUTE`  
Azure Logic Apps | `AZURE_LOGIC_APPS`  
Azure Log Analytics Workspace | `AZURE_LOG_ANALYTICS_WORKSPACE`  
Azure Machine Learning | `AZURE_MACHINE_LEARNING`  
Azure NAT Gateway Flow | `AZURE_NATGW_FLOW`  
Azure Nix System | `AZURE_NIX_SYSTEM`  
Azure Network Security Group Event | `AZURE_NSG_EVENT`  
Azure Org Context | `AZURE_ORG_CONTEXT`  
Azure PostgreSQL | `AZURE_POSTGRESQL`  
Azure Recovery Services Vaults | `AZURE_RECOVERY_SERVICES_VAULTS`  
Azure Risky Users | `AZURE_RISKY_USERS`  
Azure Risk Events | `AZURE_RISK_EVENTS`  
Azure Security Center | `AZURE_SECURITY_CENTER`  
Azure Service Principal Logins | `AZURE_SERVICE_PRINCIPAL_LOGINS`  
Azure Software Vulnerabilities | `AZURE_SOFTWARE_VULNERABILITIES`  
Azure Windows Virtual Desktop Connections Logs | `AZURE_WVD_CONNECTIONS`  
Azure Windows Virtual Desktop Management Logs | `AZURE_WVD_MANAGEMENT`  
Babelforce | `BABELFORCE`  
Backbase Engagement Banking Platform | `BACKBASE`  
Backbox | `BACKBOX`  
Backstage | `BACKSTAGE`  
OneIdentity Balabit | `BALABIT`  
BambooHR | `BAMBOO_HR`  
Banner dd | `BANNER_DD`  
Baramundi | `BARAMUNDI`  
Barracuda CloudGen Access | `BARRACUDA_CLOUDGEN_ACCESS`  
Barracuda Impersonation Protection | `BARRACUDA_IMPERSONATION`  
Barracuda Incident Response | `BARRACUDA_INCIDENTRESPONSE`  
Barracuda Load Balancer ADC | `BARRACUDA_LOAD_BALANCER`  
Barracuda Content Shield | `BARRACUDA_SHIELD`  
Behavox | `BEHAVOX`  
Belden Switch | `BELDEN_SWITCH`  
Bettercloud | `BETTERCLOUD`  
BetterStack Uptime | `BETTERSTACK_UPTIME`  
BeyondTrust Cloud Privilege Broker | `BEYONDTRUST_CPB`  
BeyondTrust Management console | `BEYONDTRUST_MC`  
Beyond Identity | `BEYOND_IDENTITY`  
BindPlane Audit Logs | `BINDPLANE`  
Bitsight | `BITSIGHT`  
Bitstamp | `BITSTAMP`  
Bitvise SFTP | `BITVISE_SFTP`  
Bitvise SSHd | `BITVISE_SSHD`  
Bitwarden Password Manager User Context | `BITWARDEN_USER_CONTEXT`  
Biztalk | `BIZTALK`  
Blackberry Workspaces | `BLACKBERRY_WORKSPACES`  
BlinkOps | `BLINKOPS`  
Blockdaemon API | `BLOCKDAEMON_API`  
BloodHound | `BLOODHOUND`  
BloxOne Threat Defense DHCP | `BLOXONE_DHCP`  
Bluecat Address Manager | `BLUECAT_AM`  
Bluecat Micetro IP Address Management | `BLUECAT_MICETRO_IPAM`  
Blue Prism | `BLUE_PRISM`  
Blue Voyant | `BLUE_VOYANT`  
BMC Control-M | `BMC_CONTROL_M`  
Boeing Onboard Network System Logging | `BOEING_ONS`  
Core Privileged Access Manager (BoKS) | `BOKS`  
Boomi App | `BOOMI`  
Bravura Security | `BRAVURA`  
Bricata NDR | `BRICATA_NDR`  
Britive Audit API | `BRITIVE_AUDIT_API`  
BRIVO | `BRIVO`  
Broadcom Compliance Event Manager | `BROADCOM_CEM`  
Broadcom DX NetOps Spectrum | `BROADCOM_DX_NETOPS_SPECTRUM`  
Broadcom Edge Secure Web Gateway | `BROADCOM_EDGE_SWG`  
Brocade Fabric OS | `BROCADE_FOS`  
Brocade SANnav Management Portal | `BROCADE_SANNAV`  
Zeek DHCP | `BRO_DHCP`  
Zeek HTTP  | `BRO_HTTP`  
BT IPControl | `BT_IPCONTROL`  
Buildkite Audit | `BUILDKITE_AUDIT`  
Burpsuite Application Security testing tool | `BURPSUITE`  
Caller Verify | `CALLER_VERIFY`  
CallTower Audio Conferencing | `CALLTOWER_AUDIO`  
Cameyo Activity Logs | `CAMEYO_ACTIVITY_LOGS`  
Cameyo Bring Your Own Cloud | `CAMEYO_BYO_CLOUD`  
Canary Audit Trail | `CANARY_AUDIT_TRAIL`  
Canon Printers | `CANON_PRINTERS`  
Canvas LMS | `CANVAS_LMS`  
Carto Activity | `CARTO_ACTIVITY`  
CATO SD-WAN | `CATO_SDWAN`  
Cayosoft Audit Logs | `CAYOSOFT_AUDIT_LOGS`  
Cayosoft Guardian Alerts | `CAYOSOFT_GUARDIAN_ALERTS`  
CDNetworks Cloud Security | `CDNETWORKS_CLOUD_SECURITY`  
Celonis Audit Logs | `CELONIS`  
Censornet CASB | `CENSORNET_CASB`  
Cerberus FTP Server | `CERBERUS_FTP`  
CertSecure Log | `CERTSECURE_LOG`  
ChatGPT Audit Logs | `CHATGPT_AUDIT_LOGS`  
Checkmarx One | `CHECKMARX_ONE`  
Check Point CloudGuard | `CHECKPOINT_CLOUDGUARD`  
Check Point Email | `CHECKPOINT_EMAIL`  
Check Point FDE | `CHECKPOINT_FDE`  
Checkpoint Gaia | `CHECKPOINT_GAIA`  
Chopin PrePay Solutions | `CHOPIN_PPS`  
Chronicle Feed | `CHRONICLE_FEED`  
Cilium | `CILIUM`  
Cisco Aironet | `CISCO_AIRONET`  
Cisco Cyber Vision | `CISCO_CYBER_VISION`  
Cisco DNS | `CISCO_DNS`  
Cisco Firepower Threat Defense | `CISCO_FIREPOWER_THREAT_DEFENSE`  
Cisco Meraki Camera | `CISCO_MERAKI_CAMERA`  
Cisco MultiCloud Defense Firewall | `CISCO_MULTICLOUD_DEFENSE_FIREWALL`  
Cisco Nexus Dashboard Orchestrator | `CISCO_NDO`  
Cisco NetFlow | `CISCO_NETFLOW`  
Cisco Remote Access VPN | `CISCO_RAVPN`  
Cisco Secure Access Enrollment | `CISCO_SECURE_ACCESS_ENROLLMENT`  
Cisco Secure Access Zero Trust Access Flow | `CISCO_SECURE_ACCESS_FLOW`  
Cisco Secure Access Network | `CISCO_SECURE_ACCESS_NETWORK`  
Cisco Secure Email Threat Defense | `CISCO_SECURE_EMAIL_THREAT_DEFENSE`  
Cisco Secure Endpoint | `CISCO_SECURE_ENDPOINT`  
Cisco Secure Malware Analytics | `CISCO_SECURE_MALWARE_ANALYTICS`  
Cisco Security Cloud Control | `CISCO_SECURITY_CLOUD_CONTROL`  
Cisco Content Security Management Appliance | `CISCO_SMA`  
Cisco SNMP Trapd | `CISCO_SNMP`  
Cisco StarOS | `CISCO_STAR_OS`  
Cisco Umbrella Firewall | `CISCO_UMBRELLA_FIREWALL`  
Cisco Umbrella IPS | `CISCO_UMBRELLA_IPS`  
Cisco Viptela | `CISCO_VIPTELA`  
Cisco Vulnerability Management | `CISCO_VULNERABILITY_MANAGEMENT`  
CiscoXDR | `CISCO_XDR`  
Citadel Identity360 | `CITADEL_IDENTITY360`  
Citrix Netscaler Web Logs | `CITRIX_NETSCALER_WEB_LOGS`  
Citrix SD-WAN | `CITRIX_SDWAN`  
Citrix Session Metadata | `CITRIX_SESSION_METADATA`  
Citrix Virtual Desktop Infrastructure | `CITRIX_VDI`  
Citrix WAF | `CITRIX_WAF`  
Citrix Web Gateway | `CITRIX_WEB_GATEWAY`  
Citrix Workspace | `CITRIX_WORKSPACE`  
Citrix XenCenter | `CITRIX_XENCENTER`  
Claroty xDome Secure Access | `CLAROTY_XDOME_SECURE_ACCESS`  
Claude Code Observability | `CLAUDE_CODE_OBSERVABILITY`  
Clavistier Firewall | `CLAVISTER_FIREWALL`  
Cleafy | `CLEAFY`  
Clear Bank Portal Audit | `CLEARBANK_PORTAL`  
Clearsense Healthcare Analytics | `CLEARSENSE`  
ClickHouse | `CLICKHOUSE`  
Click Studios Passwordstate | `CLICK_STUDIOS_PASSWORDSTATE`  
Cloud 9 | `CLOUD9`  
Cloudaware | `CLOUDAWARE`  
CloudBees | `CLOUDBEES`  
CloudBolt | `CLOUDBOLT`  
Cloudera Ranger | `CLOUDERA_RANGER`  
Cloudflare Access | `CLOUDFLARE_ACCESS`  
Cloudflare Bot Management | `CLOUDFLARE_BOT_MANAGEMENT`  
Cloudflare Brand Protection | `CLOUDFLARE_BRAND_PROTECTION`  
Cloudflare Browser Isolation | `CLOUDFLARE_BROWSER_ISOLATION`  
CloudFlare CASB Findings | `CLOUDFLARE_CASB_FINDINGS`  
Cloudflare Device posture results | `CLOUDFLARE_DEVICE_POSTURE_RESULTS`  
Cloudflare DLP Forensic Copies | `CLOUDFLARE_DLP_FORENSIC_COPIES`  
Cloudflare DNS Firewall Logs | `CLOUDFLARE_DNS_FIREWALL_LOGS`  
Cloudflare DNS logs | `CLOUDFLARE_DNS_LOGS`  
CloudFlare Email Security Alerts | `CLOUDFLARE_EMAIL_SECURITY_ALERTS`  
Cloudflare Firewall Events | `CLOUDFLARE_FIREWALL_EVENTS`  
Cloudflare Gateway DNS | `CLOUDFLARE_GATEWAY_DNS`  
Cloudflare Gateway HTTP | `CLOUDFLARE_GATEWAY_HTTP`  
Cloudflare Gateway Network | `CLOUDFLARE_GATEWAY_NETWORK`  
Cloudflare HTTP requests | `CLOUDFLARE_HTTP_REQUESTS`  
Cloudflare Magic IDS Detections | `CLOUDFLARE_MAGIC_IDS_DETECTIONS`  
Cloudflare NEL reports | `CLOUDFLARE_NEL_REPORTS`  
Cloudflare Sinkhole HTTP Logs | `CLOUDFLARE_SINKHOLE_HTTP_LOGS`  
Cloudflare Spectrum | `CLOUDFLARE_SPECTRUM`  
Cloudflare SSH Logs | `CLOUDFLARE_SSH_LOGS`  
Cloudflare Workers Trace Events | `CLOUDFLARE_WORKERS_TRACE_EVENTS`  
Cloudflare Zero Trust Network Session | `CLOUDFLARE_ZERO_TRUST_NETWORK_SESSION`  
Cloud Passage (CSM) | `CLOUDPASSAGE_CSM`  
Cloud Passage (FIM) | `CLOUDPASSAGE_FIM`  
Cloud Passage (LIDS) | `CLOUDPASSAGE_LIDS`  
Cloud Passage (SVM) | `CLOUDPASSAGE_SVM`  
Cloudsek Alerts | `CLOUDSEK_ALERTS`  
CloudWave Honeypot | `CLOUDWAVE_HONEYPOT`  
cmd.com | `CMD`  
Coalition Control API | `COALITION`  
Cockroach DB | `COCKROACH_DB`  
Coda Io | `CODA_IO`  
Code42 CrashPlan | `CODE42`  
Code Worldwide | `CODE_WORLDWIDE`  
Cofense Vision | `COFENSE_VISION`  
Cohesity Helios | `COHESITY_HELIOS`  
Cohesity Smartfiles | `COHESITY_SMARTFILES`  
ColorTokens | `COLORTOKENS`  
Commvault Metallic | `COMMVAULT_METALLIC`  
Conductor One | `CONDUCTOR_ONE`  
Confluent Audit | `CONFLUENT_AUDIT`  
ConnectWise Automate | `CONNECTWISE_AUTOMATE`  
ConnectWise Control | `CONNECTWISE_CONTROL`  
Contrast Security | `CONTRAST_SECURITY`  
Control D DNS | `CONTROL_D`  
Control Plane | `CONTROL_PLANE`  
Control UP | `CONTROL_UP`  
Conversational Agents and Dialogflow | `CONVERSATIONAL_AGENT`  
Corero SmartWall One | `CORERO_SMARTWALL_ONE`  
CoreView Audit-log SIEM integration | `COREVIEW`  
Corrata | `CORRATA`  
Palo Alto Cortex Xpanse | `CORTEX_XPANSE`  
Pico Corvilnet Engine | `CORVILNET_ENGINE`  
Cradlepoint Router Logs | `CRADLEPOINT`  
Cradlepoint NetCloud | `CRADLEPOINT_NETCLOUD`  
Cribl AppScope | `CRIBL_APPSCOPE`  
Cribl Cloud | `CRIBL_CLOUD`  
Cribl Edge | `CRIBL_EDGE`  
Cribl Search | `CRIBL_SEARCH`  
CrowdStrike Cloud Security | `CROWDSTRIKE_CSPM`  
CrowdStrike DLP | `CROWDSTRIKE_DLP`  
CrowdStrike Falcon Shield | `CROWDSTRIKE_FALCON_SHIELD`  
Crowdstrike Recon (TI) | `CROWDSTRIKE_RECON`  
Crowdstrike Spotlight | `CROWDSTRIKE_SPOTLIGHT`  
ProLion CryptoSpike | `CRYPTOSPIKE`  
CSG Custom Rules Engine | `CSG_CUSTOMENGINE`  
CSG Singleview | `CSG_SINGLEVIEW`  
CSV Custom CMDB | `CSV_CUSTOM_CMDB`  
CrowdStrike Falcon CEF | `CS_CEF_EDR`  
Crowdstrike Endpoint Security API | `CS_ENDPOINT_SECURITY_API`  
CTERA Drive | `CTERA_DRIVE`  
Cubist Audit | `CUBIST_AUDIT`  
Culture AI | `CULTURE_AI`  
Cursor | `CURSOR`  
Customer Alerts | `CUSTOMER_ALERT`  
Custom CSV Log | `CUSTOM_CSV_LOG`  
Custom Host Forensics | `CUSTOM_HOST_FORENSICS`  
CyberArk Certificate Manager SaaS | `CYBERARK_CERTIFICATE_MANAGER_SAAS`  
Cyberark Identity | `CYBERARK_IDENTITY`  
Cyberark Identity Audit | `CYBERARK_IDENTITY_AUDIT`  
CyberArk Secure Cloud Access | `CYBERARK_SCA`  
CyberArk Identity Single Sign-On | `CYBERARK_SSO`  
Connectsecure | `CYBERCNS`  
Cyberhaven Data Detection and Response | `CYBERHAVEN_DDR`  
Cyberhaven | `CYBERHAVEN_EVENTS`  
Cyberint | `CYBERINT`  
Cybersixgill | `CYBERSIXGILL`  
Cyble Attack Surface Management | `CYBLE_ASM`  
Cyble Brand Intelligence & Protection | `CYBLE_BIP`  
Cycode Platform | `CYCODE`  
CyCognito ASM | `CYCOGNITO_ASM`  
Insider threat detection and response | `CYDERES_INSIDER`  
Cyderes IOC | `CYDERES_IOC`  
Cyfirma DeCYFIR ServiceNow | `CYFIRMA_DECYFIR`  
Cyfirma | `CYFIRMA_DECYFIR_LOG`  
Cylance | `CYLANCE`  
Cylera IOT | `CYLERA_IOT`  
Cymulate | `CYMULATE`  
Cynerio Healthcare NDR | `CYNERIO_NDR_H`  
Cyolo Zero Trust | `CYOLO_ZTNA`  
Cyral | `CYRAL`  
Cytracom Control One | `CYTRACOM_CONTROL_ONE`  
C Zentrix | `C_ZENTRIX`  
D3 Security | `D3_SECURITY`  
Darkweb IQ | `DARKWEB_IQ`  
Databahn | `DATABAHN`  
Datadog Application Security Management | `DATADOG_ASM`  
Dataiku DSS Logging | `DATAIKU_DSS_LOGS`  
DataLocker SafeConsole | `DATALOCKER_SAFECONSOLE`  
Datalust | `DATALUST`  
Datasunrise Dam | `DATASUNRISE_DAM`  
Datawatch | `DATAWATCH`  
DATEV | `DATEV`  
DBT Cloud | `DBT_CLOUD`  
DealCloud | `DEAL_CLOUD`  
Deepfence Network Monitoring | `DEEPFENCE`  
DefectDojo | `DEFECTDOJO`  
Delinea Cloud Platform | `DELINEA_CLOUD_PLATFORM`  
Delinea PBA | `DELINEA_PBA`  
Delinea Privilege Manager | `DELINEA_PRIVILEGE_MANAGER`  
Delinea Server Suite | `DELINEA_SERVER_SUITE`  
Dell Compellent | `DELL_COMPELLENT`  
Dell Cyber Recovery Manager | `DELL_CRM`  
Dell EMC Avamar | `DELL_EMC_AVAMAR`  
Dell EMC Cloudlink | `DELL_EMC_CLOUDLINK`  
Dell Core Switch | `DELL_EMC_NETWORKING`  
Dell EMC Unity | `DELL_EMC_UNITY`  
Dell EMC UnityVSA | `DELL_EMC_UNITY_VSA`  
Dell RecoverPoint | `DELL_RECOVERPOINT`  
Dell VxRail | `DELL_VXRAIL`  
Dell SonicWALL WAF | `DELL_WAF`  
Design Profit Central Server | `DESIGN_PROFIT_CENTRAL_SERVER`  
Device 42 | `DEVICE_42`  
Devolutions Remote Desktop Manager | `DEVOLUTIONS_RDM`  
Divvy Cloud | `DIVVY_CLOUD`  
DLink Switch | `DLINK_SWITCH`  
Dmarcian | `DMARCIAN`  
Docker | `DOCKER`  
Docker Hub Activity | `DOCKER_HUB_ACTIVITY`  
DocuSign | `DOCUSIGN`  
DOMO Business Cloud | `DOMO`  
Doppel | `DOPPEL`  
Dragos | `DRAGOS`  
Draytek Firewall | `DRAYTEK`  
Draytek Router | `DRAYTEK_ROUTER`  
Dremio Data Lakehouse | `DREMIO_DATA_LAKEHOUSE`  
Dropbox | `DROPBOX`  
Drupal Logging | `DRUPAL`  
Druva | `DRUVA`  
DSP Toolkit audit | `DSP_AUDIT`  
Dtex Audit | `DTEX_AUDIT`  
Dtex Intercept | `DTEX_INTERCEPT`  
Cisco Duo Authentication Proxy | `DUO_AUTH_PROXY`  
Duo Access Gateway | `DUO_CASB`  
Duo Network Gateway | `DUO_NETWORK_GATEWAY`  
Duo Trust Monitor | `DUO_TRUST_MONITOR`  
Dynatrace | `DYNATRACE`  
E2 Guardian | `E2_GUARDIAN`  
CWT SatoTravel | `E2_SOLUTIONS`  
Easy NAC | `EASY_NAC`  
Eaton UPS | `EATON_UPS`  
eCAR | `ECAR`  
eCAR Bro | `ECAR_BRO`  
Edgecore Networks | `EDGECORE_NETWORKS`  
Edgio CDN | `EDGIO_CDN`  
Edgio Rate Limiting | `EDGIO_RL`  
Efax | `EFAX`  
Egnyte | `EGNYTE`  
Egress Defend | `EGRESS_DEFEND`  
Egress Prevent | `EGRESS_PREVENT`  
EclecticIQ EDR | `EIQ_EDR`  
Elastic Security | `ELASTIC_EDR`  
Elastic File Beats | `ELASTIC_FILEBEAT`  
Elastic Metric Beats | `ELASTIC_METRICBEAT`  
Ellio Threat Intelligence | `ELLIO_THREAT_INTEL`  
ELO | `ELO`  
Emerson Smart Firewall | `EMERSON_FIREWALL`  
Emsisoft AntiVirus | `EMSISOFT_ANTIVIRUS`  
Endgame | `ENDGAME_EDR`  
Ensono Cloud Mainframe Solution | `ENSONO`  
Entrust NTP Server | `ENTRUST_NTP_SERVER`  
Entrust Secrets Vault | `ENTRUST_SECRETS_VAULT`  
Entrust DataControl Audit | `ENTR_DATACTRL_AUDIT`  
Erlang Shell Logs | `ERLANG_SHELL`  
Ermes Web Protection | `ERMES`  
Ermetic | `ERMETIC`  
Eset Protect Platform | `ESET_PROTECT_PLATFORM`  
E-Share platform | `ESHARE_PLATFORM`  
Estar | `ESTAR`  
ETQ Reliance | `ETQ_RELIANCE`  
Evidos Firewall | `EVIDOS_FIREWALL`  
Exabeam Fusion XDR | `EXABEAM_FUSION_XDR`  
Exeon NDR | `EXEON_NDR`  
Exim Internet Mailer | `EXIM_INTERNET_MAILER`  
Express NodeJS | `EXPRESS_NODEJS`  
Exterro FTK Central | `EXTERRO_FTK_CENTRAL`  
ExtraHop DHCP | `EXTRAHOP_DHCP`  
ExtremeWare Operating System (OS) | `EXTREMEWARE_NETWORKS`  
xtreme Networks ExtremeControl NAC Solution | `EXTREME_CONTROL`  
Extreme Management Center | `EXTREME_MANAGEMENT`  
EzProxy | `EZPROXY`  
F5 Bot | `F5_BOT`  
F5 Distributed Cloud WAF | `F5_DCS_WAF`  
F5 F5OS-A Logging | `F5_F5OS_A`  
F5 IP Intelligence | `F5_IP_INTELLIGENCE`  
F5 System Logs | `F5_SYSTEM_LOGS`  
Fail2Ban Scan | `FAIL2BAN`  
FairXchange Horizon | `FAIRXCHANGE_HORIZON`  
Farsight DNSDB | `FARSIGHT_DNSDB`  
FA Solutions | `FA_SOLUTIONS`  
Featurespace Aric | `FEATURESPACE_ARIC`  
Feenics Access Control | `FEENICS_ACCESS_CONTROL`  
Fidelis Endpoint | `FIDELIS_ENDPOINT`  
Figma Developers | `FIGMA`  
FileMage SFTP | `FILEMAGE_SFTP`  
Files dot com | `FILES_DOT_COM`  
Firebase | `FIREBASE`  
Fireblocks | `FIREBLOCKS`  
FireEye CMS | `FIREEYE_CMS`  
FireEye Helix | `FIREEYE_HELIX`  
FireMon Firewall | `FIREMON_FIREWALL`  
Fisglobal Quantum | `FISGLOBAL_QUANTUM`  
Flare Darkweb Alerts | `FLARE_DARKWEB_ALERTS`  
Flashpoint IOC | `FLASHPOINT_IOC`  
Fleet DM | `FLEET_DM`  
FM Systems Workplace Management | `FM_SYSTEMS`  
Forcepoint Insider Threat | `FORCEPOINT_FIT`  
Forcepoint One | `FORCEPOINT_ONE`  
Forcepoint Secure Web Gateway | `FORCEPOINT_SWG`  
Forcepoint V Series | `FORCEPOINT_VSERIES`  
Fortanix Data Security Manager | `FORTANIX_DSM`  
Fortinet ADC | `FORTINET_ADC`  
Fortinet Wireless Access Point | `FORTINET_AP`  
Fortinet FortiAppSec Cloud | `FORTINET_FORTIAPPSEC`  
Fortinet FortiDeceptor | `FORTINET_FORTIDECEPTOR`  
Fortinet FortiDLP | `FORTINET_FORTIDLP`  
Fortinet FortiMail Workspace | `FORTINET_FORTIMAIL_WORKSPACE`  
Fortinet Network Detection and Response | `FORTINET_FORTINDR`  
Fortinet FortiSASE | `FORTINET_FORTISASE`  
Fortinet FortiGate IPS | `FORTINET_IPS`  
Fortra Vulnerability Management | `FORTRA_VM`  
Foundry Fastiron | `FOUNDRY_FASTIRON`  
FoxPass Audit Logs | `FOXPASS_AUDIT_LOGS`  
Fox-IT | `FOX_IT_STIX`  
FreeIPA | `FREEIPA`  
FreeRADIUS | `FREERADIUS`  
Front | `FRONT`  
Digital Defense Frontline VM | `FRONTLINE_VM`  
FS-ISAC IOC | `FS_ISAC_IOC`  
Fusion Auth | `FUSION_AUTH`  
Futurex HSM | `FUTUREX_HSM`  
GateWatcher NDR | `GATEWATCHER_NDR`  
GCP Artifact Registry | `GCP_ARTIFACT_REGISTRY`  
GCP Identity Toolkit | `GCP_IDENTITYTOOLKIT`  
GCP Google Kubernetes Container Security | `GCP_KUBERNETES_CONTAINER_SECURITY`  
GCP Threat Detection | `GCP_THREAT_DETECTION`  
Gemini Enterprise Agent Platform | `GEMINI_ENTERPRISE_AGENT_PLATFORM`  
Gene6 FTP Server | `GENE6_FTP`  
Genea Access Control | `GENEA_ACCESS_CONTROL`  
Genesys Audit | `GENESYS_AUDIT`  
Genetec Audit | `GENETEC_AUDIT`  
Genetec Synergis | `GENETEC_SYNERGIS`  
Genian NAC | `GENIAN_NAC`  
Schneider Electric GeoScada OT | `GEOSCADA_OT`  
Ghangor DLP | `GHANGOR_DLP`  
Gigamon | `GIGAMON`  
Gigya CIAM | `GIGYA_CIAM`  
Github Events | `GITHUB_EVENTS`  
Glean | `GLEAN`  
Globalscape SFTP | `GLOBALSCAPE_SFTP`  
GlusterFS | `GLUSTER_FS`  
GluWare Network Automation | `GLUWARE_NETWORK_AUTOMATION`  
GL TRADE | `GL_TRADE`  
GMV Checker User Context | `GMV_CHECKER_CONTEXT`  
GoAnywhere MFT | `GOANYWHERE_MFT`  
GoDaddy DNS | `GODADDY_DNS`  
GoldiLock | `GOLDILOCK`  
Gong | `GONG`  
Google Ads | `GOOGLE_ADS`  
Grafana | `GRAFANA`  
Gravitee | `GRAVITEE`  
GrayhatWarfare | `GRAYHATWARFARE`  
Graylog Operations | `GRAYLOG`  
GreatHorn Email Security | `GREATHORN`  
Greenhouse Harvest | `GREENHOUSE_HARVEST`  
Group-IB Threat Intelligence | `GROUP_IB`  
Guidewire Billing Center | `GUIDEWIRE_BILLING_CENTER`  
Guidewire Claim Center | `GUIDEWIRE_CLAIM_CENTER`  
Guidewire Policy Center | `GUIDEWIRE_POLICY_CENTER`  
Gurucul Risk Analytics | `GURUCUL`  
H3C Router | `H3C_ROUTER`  
Halcyon Webhook | `HALCYON_WEBHOOK`  
Halo | `HALO`  
Halo Sensor | `HALO_SENSOR`  
HaProxy LoadBalancer | `HAPROXY_LOADBALANCER`  
Harbor | `HARBOR`  
Harfanglab EDR | `HARFANGLAB_EDR`  
Hashcast | `HASHCAST`  
Hashicorp Boundary | `HASHICORP_BOUNDARY`  
Hashicorp Nomad | `HASHICORP_NOMAD`  
Hashicorp Terraform | `HASHICORP_TERRAFORM`  
HAVI Connect | `HAVI_CONNECT`  
Perforce Helix Core | `HELIX_CORE`  
Heroku | `HEROKU`  
Hex | `HEX`  
HiBob | `HIBOB`  
HaveIBeenPwned | `HIBP`  
Hikvision Network Video Recorders | `HIKVISION_NVR`  
Hillstone NDR | `HILLSTONE_NDR`  
Hirschmann Switch | `HIRSCHMANN_SWITCH`  
Hitachi PAM | `HITACHI_ID_PAM`  
HL7 | `HL7`  
Honeywell Cyber Proactive Defense | `HONEYWELL_CPD`  
Honeywell Cyber Insights | `HONEYWELL_CYBERINSIGHTS`  
HoopDev | `HOOPDEV`  
Hornet Email Security | `HORNET_SECURITY`  
Hoxhunt | `HOXHUNT`  
HPE Alletra | `HPE_ALLETRA`  
Hewlett Packard Enterprise SAN | `HPE_SAN`  
HP Inc MFP | `HP_INC_MFP`  
HPE Oneview | `HP_ONEVIEW`  
HP Poly | `HP_POLY`  
HP Printer logs | `HP_PRINTER`  
HP Router | `HP_ROUTER`  
HP Tandem | `HP_TANDEM`  
HP Wolf Pro Security | `HP_WOLF`  
Huawei Campus Switch | `HUAWEI_CAMPUS_SWITCH`  
Huawei CloudEngine | `HUAWEI_CLOUDENGINE`  
Huawei Cloud Trace Service Audit | `HUAWEI_CTS_AUDIT`  
Huawei NextGen Firewall | `HUAWEI_FIREWALL`  
Huawei Fusion Sphere Hypervisor | `HUAWEI_FUSIONSPHERE`  
Huawei NAC | `HUAWEI_NAC`  
Huawei SecMaster | `HUAWEI_SECMASTER`  
Huawei Versatile Routing Platform | `HUAWEI_VRP`  
Huawei Wireless | `HUAWEI_WIRELESS`  
HubSpot Activity Logs | `HUBSPOT_ACTIVITY`  
HubSpot CRM Platform | `HUBSPOT_CRM`  
HubSpot Authentication Logs | `HUBSPOT_LOGIN`  
Human Security | `HUMAN_SECURITY`  
Huntress EDR | `HUNTRESS_EDR`  
Health ISAC | `H_ISAC`  
3Com 8800 Series Switch | `IBM_3COM`  
IBM B2B Integrator | `IBM_B2B_INTEGRATOR`  
IBM Cleversafe Object Storage | `IBM_CLEVERSAFE`  
IBM Cloud Alert Notification | `IBM_CLOUD_ALERT_NOTIFICATION`  
IBM Cloud System | `IBM_CLOUD_SYSTEM`  
IBM Cognos Analytics | `IBM_COGNOS`  
IBM Copy Services Manager | `IBM_CSM`  
IBM ILO | `IBM_ILO`  
IBM Security Guardium Insights | `IBM_INSIGHTS`  
IBM KNS | `IBM_KNS`  
IBM MQ File Transfer | `IBM_MQ_FILE_TRANSFER`  
IBM NS1 | `IBM_NS1`  
IBM Planning Analytics | `IBM_PA`  
IBM Sense | `IBM_SENSE`  
IBM Spectrum Protect | `IBM_SPECTRUM_PROTECT`  
IBM Storwize | `IBM_STORWIZE`  
IBM Switch | `IBM_SWITCH`  
IBM Tririga | `IBM_TRIRIGA`  
IBM InfoSphere Virtual Data Pipeline | `IBM_VDP`  
IBM WinCollect | `IBM_WINCOLLECT`  
Idecsi | `IDECSI`  
Identity Security Cloud | `IDENTITY_SECURITY_CLOUD`  
Dell iDRAC | `IDRAC`  
IIJ_LanScope | `IIJ_LANSCOPE`  
ImageNow | `IMAGENOW`  
iManage Cloud Platform | `IMANAGE_CLOUD`  
iManage Threat Manager | `IMANAGE_THREAT_MANAGER`  
Imperva Account TakeOver | `IMPERVA_ATO`  
Imperva Cloud WAF | `IMPERVA_CLOUD_WAF`  
Imperva Client Side Protection | `IMPERVA_CSP`  
Imperva Data Risk Analytics | `IMPERVA_DATA_ANALYTICS`  
Imperva DNS | `IMPERVA_DNS`  
Imperva Network Security | `IMPERVA_NETWORK_SECURITY`  
Imperva Sonar | `IMPERVA_SONAR`  
Imprivata Confirm ID | `IMPRIVATA_CONFIRM_ID`  
Imprivata Identity Governance | `IMPRIVATA_IDG`  
Imprivata OneSign | `IMPRIVATA_ONESIGN`  
IM Express | `IM_EXPRESS`  
Incident Io | `INCIDENT_IO`  
Indefend DLP | `INDEFEND_DLP`  
Indusface WAF | `INDUSFACE_WAF`  
INFINICO NetWyvern Series Appliance | `INFINICO_NETWYVERN`  
Infinidat | `INFINIDAT`  
Infisical | `INFISICAL`  
Infoblox Loadbalancer | `INFOBLOX_LOADBALANCER`  
Infoblox NetMRI | `INFOBLOX_NETMRI`  
Informatica | `INFORMATICA`  
Informatica Powercenter | `INFORMATICA_POWERCENTER`  
INKY Secure Email | `INKY`  
Intezer | `INTEZER`  
Intruder.IO | `INTRUDER_IO`  
Invicti | `INVICTI`  
inWebo MFA | `INWEBO_MFA`  
IPFire | `IPFIRE`  
Ipswitch MOVEit Automation | `IPSWITCH_MOVEIT_AUTOMATION`  
Ironclad | `IRONCLAD`  
Ironscales | `IRONSCALES`  
iSecurity | Security Services and Remediation | `ISECURITY`  
Isonline ISL Light | `ISL_LIGHT`  
Itential Pronghorn | `ITENTIAL_PRONGHORN`  
iTop | `ITOP`  
Ivanti Application Control | `IVANTI_APP_CONTROL`  
Ivanti Connect Secure | `IVANTI_CONNECT_SECURE`  
Ivanti Device Control | `IVANTI_DEVICE_CONTROL`  
Ivanti Endpoint Manager Mobile | `IVANTI_ENDPOINT_MANAGER_MOBILE`  
ISM Xtraction | `IVANTI_XTRACTION`  
iverify | `IVERIFY`  
Jamf Compliance Reporter | `JAMF_COMPLIANCE_REPORTER`  
Jamf Connect | `JAMF_CONNECT`  
Jamf Protect Network Traffic | `JAMF_NETWORK_TRAFFIC`  
Jamf Protect Alerts V2 | `JAMF_PROTECT_V2`  
Jamf Pro MDM | `JAMF_PRO_MDM`  
JBoss Web | `JBOSS_WEB`  
IBM JDE | `JDE`  
JiranSecurity MailScreen | `JIRANSECURITY_MAILSCREEN`  
Jit | `JIT`  
Joblogic | `JOBLOGIC`  
JSCAPE SFTP | `JSCAPE_SFTP`  
JumpCloud Directory as a Service | `JUMPCLOUD_DAAS`  
JumpCloud Desktop | `JUMPCLOUD_DESKTOP`  
Jumpcloud IAM | `JUMPCLOUD_IAM`  
JumpServer PAM | `JUMPSERVER_PAM`  
Juniper Edge | `JUNIPER_EDGE`  
Juniper SSR Conductor | `JUNIPER_SSR_CONDUCTOR`  
Juniper Secure Connect VPN | `JUNIPER_VPN`  
Jupiter One | `JUPITER_ONE`  
KACE Service Desk | `KACE_SERVICE_DESK`  
KACE Systems Management Appliance | `KACE_SMA`  
Kamailio | `KAMAILIO`  
Kandji | `KANDJI`  
Kandji Context | `KANDJI_CONTEXT`  
Kaseya IT Management | `KASEYA`  
Kaspersky anti targeted attack | `KASPERSKY_ANTI_TARGETED_ATTACK`  
Kaspersky for Microsoft Office 365 | `KASPERSKY_O365_EVENTS`  
Keepalived Routing software | `KEEPALIVED`  
Keep Aware | `KEEP_AWARE`  
Kentik DDoS Detection | `KENTIK_ALERTS`  
Keyfactor | `KEYFACTOR`  
Keysight Packet Brokers | `KEYSIGHT`  
Kibana audit logs | `KIBANA`  
Kion | `KION`  
KnowBe4 Audit Log | `KNOWBE4`  
Kodem Security | `KODEM_SECURITY`  
Kustomer CRM | `KUSTOMER_CRM`  
Kyverno | `KYVERNO`  
LangSmith Audit | `LANGSMITH_AUDIT`  
Lansweeper Asset Management | `LANSWEEPER`  
Lark Suite | `LARK_SUITE`  
LaunchDarkly | `LAUNCH_DARKLY`  
LayerX | `LAYERX`  
LOAD_BALANCER_ADC | `LB_ADC`  
LeanIX Enterprise | `LEANIX`  
Leanix CMDB | `LEANIX_CMDB`  
LeapXpert Audit Logs | `LEAPXPERT_AUDIT`  
Lenels2 Elements Secure | `LENELS2_ELEMENTS_SECURE`  
Lepide | `LEPIDE`  
Lever | `LEVER`  
Lexmark Printer logs | `LEXMARK_PRINTER`  
Liaison NuBridges Platform | `LIAISON_NUBRIDGES`  
Libraesva Email Security | `LIBRAESVA_EMAIL`  
LinOTP | `LIN_OTP`  
Lira | `LIRA`  
Lockself Lockpass | `LOCKSELF_LOCKPASS`  
Apache LOG4J Java Application Log | `LOG4J`  
LogicGate | `LOGICGATE`  
Logic Monitor | `LOGICMONITOR`  
LookingGlass Aenoik IDPS | `LOOKINGGLASS_IPS`  
Looking Glass | `LOOKING_GLASS_IOC`  
LSI Badge Management System | `LSI_BMS`  
Lumen DDoS Hyper | `LUMEN_DDOS_HYPER`  
Lumeta Spectre | `LUMETA`  
Lumos | `LUMOS`  
Lumu Universal SIEM | `LUMU`  
Lenovo XClarity Orchestrator | `LXC_ORCHESTRATOR`  
Macmon | `MACMON`  
MacStadium | `MACSTADIUM`  
Magento Cloud | `MAGENTO_CLOUD`  
Magic Collaboration Studio | `MAGIC_CS`  
MailScanner | `MAILSCANNER`  
Maltiverse IOC | `MALTIVERSE_IOC`  
Mambu | `MAMBU`  
Mamori Database Activity Monitoring | `MAMORI_DAM`  
Manage Engine Endpoint | `MANAGEENGINE_ENDPOINT`  
ManageEngine NCM | `MANAGEENGINE_NCM`  
ManageEngine Remote Access Plus | `MANAGEENGINE_RAP`  
ManageEngine Asset Explorer | `MANAGE_ENGINE_ASSET_EXPLR`  
ManageEngine Endpoint Central | `MANAGE_ENGINE_ENDPT_CNTRL`  
ManageEngine OpUtils | `MANAGE_ENGINE_OPUTILS`  
ManageEngine PAM360 | `MANAGE_ENGINE_PAM360`  
ManageEngine Password Manager Pro | `MANAGE_ENGINE_PASSWORD_MANAGER`  
Mandiant Attack Surface Management Entity | `MANDIANT_ASM_ENTITY`  
Mandiant Attack Surface Management Discovered Issue | `MANDIANT_ASM_ISSUE`  
Mandiant Attack Surface Management Technology | `MANDIANT_ASM_TECHNOLOGY`  
Mandiant Digital Threat Monitoring | `MANDIANT_DTM_ALERTS`  
Mango Apps | `MANGOAPPS`  
Manhattan Warehouse Management System | `MANHATTAN_WMS`  
Material Security | `MATERIAL_SECURITY`  
Matrix Frontier Badge Management | `MATRIX_FRONTIER`  
Mandiant Advantage Security Validation | `MA_SV`  
McAfee Application Control | `MCAFEE_APP_CONTROL`  
McAfee Advanced Threat Defense | `MCAFEE_ATD`  
McAfee MVISION EDR | `MCAFEE_EDR`  
McAfee Network Security Platform | `MCAFEE_NSP`  
McAfee Solid Core | `MCAFEE_SOLID_CORE`  
Model Context Protocol Dev | `MCPDEV`  
Model Context Protocol Modify | `MCPMODIFY`  
Model Context Protocol View | `MCPVIEW`  
Medigate CMDB | `MEDIGATE_CMDB`  
Melissa | `MELISSA`  
Mellanox Switch | `MELLANOX_SWITCH`  
Mend IO | `MEND_IO`  
Metaswitch Perimeta | `METASWITCH_PERIMETA`  
Meta Marketing | `META_MARKETING`  
Meter Firewall NIDS | `METER_FIREWALL_NIDS`  
Miasma SecretScanner | `MIASMA_SECRETSCANNER`  
MicroSemi NTP | `MICROSEMI_NTP`  
Microsoft Ads | `MICROSOFT_ADS`  
Microsoft CASB Files & Entities | `MICROSOFT_CASB_CONTEXT`  
Microsoft Copilot Interaction | `MICROSOFT_COPILOT_INTERACTION`  
Microsoft Azure Databricks | `MICROSOFT_DATABRICKS_WORKSPACES`  
Microsoft Defender for Cloud Apps | `MICROSOFT_DEFENDER_CLOUD_APPS`  
Microsoft Defender XDR | `MICROSOFT_DEFENDER_XDR`  
Microsoft Dotnet Log Files | `MICROSOFT_DOTNET`  
Microsoft Defender External Attack Surface Management | `MICROSOFT_EASM`  
Microsoft Entra ID Protection | `MICROSOFT_ENTRA_ID_PROTECTION`  
Microsoft Graph Incident | `MICROSOFT_GRAPH_INCIDENT`  
Microsoft Graph Risky Users | `MICROSOFT_GRAPH_RISKY_USERS`  
Microsoft Identity Protection | `MICROSOFT_IDENTITY_PROTECTION`  
Microsoft Insights/Components | `MICROSOFT_INSIGHTS_COMPONENTS`  
Power BI Activity Log | `MICROSOFT_POWERBI_ACTIVITY_LOG`  
Microsoft Purview | `MICROSOFT_PURVIEW`  
Microsoft Azure AD Risk Detections | `MICROSOFT_RISK_DETECTIONS`  
Microsoft Security Actions | `MICROSOFT_SECURITY_ACTIONS`  
Microsoft Security Advisories Alerts | `MICROSOFT_SECURITY_ALERTS`  
Microsoft ServiceBus/Namespaces | `MICROSOFT_SERVICEBUS_NAMESPACES`  
Microsoft Azure SQL Managed Instances | `MICROSOFT_SQL_MANAGED_INSTANCES`  
Microsoft SSTP VPN | `MICROSOFT_SSTP`  
Microsoft Threat Indicators | `MICROSOFT_THREAT_INDICATORS`  
Mimecast Attachment Logs | `MIMECAST_ATTACHMENT_LOGS`  
Mimecast Audit Logs | `MIMECAST_AUDIT_LOGS`  
Mimecast DLP Logs | `MIMECAST_DLP_LOGS`  
Mimecast impersonation Logs | `MIMECAST_IMPERSONATION_LOGS`  
Mimecast Web Security | `MIMECAST_WEBPROXY`  
Minerva AV | `MINERVA_AV`  
Minsait Sigefi | `MINSAIT_SIGEFI`  
Miro | `MIRO`  
Miro Cloud | `MIRO_CLOUD`  
Mirth OnPrem Appliances NextGen | `MIRTH_NEXTGEN`  
Mitel Communications Director | `MITEL_MCD`  
Mode Analytics | `MODE_ANALYTICS`  
ModSecurity | `MODSECURITY`  
Monday | `MONDAY`  
Mongo Atlas Audit | `MONGO_ATLAS_AUDIT`  
Mosyle | `MOSYLE`  
Moveworks | `MOVEWORKS`  
Microsoft Entra Recommendations | `MS_ENTRA_RECOMMENDATIONS`  
Windows Performance Monitor | `MS_PERFMON`  
Mulesoft | `MULESOFT`  
Multicom Switch | `MULTICOM_SWITCH`  
MultiPay | `MULTIPAY`  
N8N Security Audit Logs | `N8N_SECURITY_AUDIT_LOGS`  
Nakivo Backup and Recovery | `NAKIVO_BACKUP`  
NCC Scout Suite | `NCC_SCOUTSUITE`  
NCR Digital Insight FSG | `NCR_DIGITAL_INSIGHT_FSG`  
NCR Digital Insight Global Logging | `NCR_DIGITAL_INSIGHT_GL`  
Nessus | `NESSUS`  
Nessus Network Monitor | `NESSUS_NETWORK_MONITOR`  
NetApp ONTAP Audit | `NETAPP_ONTAP_AUDIT`  
NetApp Ransomware Resilience | `NETAPP_RANSOMWARE_RESILIENCE`  
NetBrain | `NETBRAIN`  
Netcraft Takedown | `NETCRAFT_TAKEDOWN`  
NetDisco | `NETDISCO`  
Netenrich Entity Behaviour | `NETENRICH_ENTITY_BEHAVIOR`  
Netenrich Entity Context | `NETENRICH_ENTITY_CONTEXT`  
Netgate Firewall | `NETGATE_FIREWALL`  
Netgear Switch | `NETGEAR_SWITCH`  
Netlify Log Drains | `NETLIFY_LOGDRAINS`  
Netmotion | `NETMOTION`  
Netography Fusion | `NETOGRAPHY_FUSION`  
Netscout Arbor Threat Mitigation System | `NETSCOUT_TMS`  
Netskope Log Streaming | `NETSKOPE_LOG_STREAMING`  
Netskope One Secure SD-WAN | `NETSKOPE_SDWAN`  
Netsurion ProtectWise | `NETSURION_PROTECTWISE`  
Network Box Unified Threat Management+ | `NETWORKBOX_UTM`  
Netwrix Activity Monitor | `NETWRIX_ACTIVITY_MONITOR`  
Netwrix Privilege Secure | `NETWRIX_PRIVILEGE_SECURE`  
Netwrix Stealth Intercept | `NETWRIX_STEALTH_INTERCEPT`  
Netwrix Threat Manager | `NETWRIX_THREAT_MANAGER`  
Neustar SiteProtect | `NEUSTAR_SITEPROTECT`  
NeuVector SUSE | `NEUVECTOR`  
New Relic Platform | `NEW_RELIC`  
Nextcloud Hub | `NEXTCLOUD_HUB`  
Nextthink Finder | `NEXTTHINK_FINDER`  
Ne Silent Log | `NE_SILENT_LOG`  
Nightfall DLP | `NIGHTFALL`  
Ninja One | `NINJAONE`  
NIST National Vulnerability Database | `NIST_NVD`  
NNT File Integrity monitoring | `NNT_FIM`  
Nokia Home Device Manager | `NOKIA_HDM`  
NordLayer VPN | `NORD_LAYER`  
Nortel Secure Router | `NORTEL_SR`  
Nortel Contivity VPN Switch | `NORTEL_SWITCH`  
Notion | `NOTION`  
Novidea Insurance Management System | `NOVIDEA_CLAIM_HISTORY`  
NSFOCUS Next Generation Intrusion Prevention System | `NSFOCUS_NGIPS`  
Nucleus Vulnerability Scan Delta | `NUCLEUS_VULNERABILITY_DELTA`  
Nutanix Frame | `NUTANIX_FRAME`  
Nxlog Agent | `NXLOG_AGENT`  
Nxlog Fim | `NXLOG_FIM`  
Next Level Performance Amplify | `NXL_AMPLIFY`  
N-Able N-Central RMM | `N_ABLE_N_CENTRAL_RMM`  
Oracle Cloud Infrastructure API Gateway | `OCI_APIGATEWAY`  
Oracle Cloud Infrastructure Network Firewall | `OCI_FIREWALL`  
Oracle Cloud Infrastructure Identity Cloud Service | `OCI_IDENTITY_CLOUD_SERVICE`  
Oracle Cloud Infrastructure LoadBalancer | `OCI_LOADBALANCER`  
Oracle Cloud Infrastructure Web Application Firewall | `OCI_WAF`  
Okta RADIUS | `OKTA_RADIUS`  
Okta Workflows | `OKTA_WORKFLOWS`  
OnBase CMS | `ONBASE_CMS`  
One Identity Active Role Service | `ONEIDENTITY_ARS`  
One Identity Change Auditor | `ONEIDENTITY_CHANGE_AUDITOR`  
One Identity Defender | `ONEIDENTITY_DEFENDER`  
OneIdentity Safeguard | `ONEIDENTITY_SAFEGUARD`  
1KOSMOS | Identity and Authentication | `ONEKOSMOS`  
OneLogin User Context | `ONELOGIN_USER_CONTEXT`  
OneTrust | `ONETRUST`  
Oomnitza | `OOMNITZA`  
Open CTI Platform | `OPENCTI`  
Openpath Context | `OPENPATH_CONTEXT`  
Opentelemetry | `OPENTELEMETRY`  
OpenText Cordy | `OPENTEXT_CORDY`  
Opentext Exstream | `OPENTEXT_EXSTREAM`  
OpenText Fax2Mail | `OPENTEXT_FAX2MAIL`  
OpenText Self Service Password Reset | `OPENTEXT_SSPR`  
IDnomic Public Key Infrastructure | `OPENTRUST`  
OpenVAS | `OPENVAS`  
OpsRamp | `OPSRAMP`  
Opswat Kiosk | `OPSWAT_KIOSK`  
Opus Codec | `OPUS`  
Oracle Access Manager | `ORACLE_AM`  
Oracle Audit Vault Database Firewall | `ORACLE_AVDF`  
Oracle CPQ | `ORACLE_CPQ`  
Oracle EBS | `ORACLE_EBS`  
Oracle Exadata Database Machine | `ORACLE_EXADATA`  
Oracle HCM Human resources platform solution | `ORACLE_HCM`  
Oracle Key Vault Audit Logs | `ORACLE_KEY_VAULT_AUDIT_LOGS`  
Oracle Enterprise Manager | `ORACLE_OEM`  
Oracle SSO Audit Logging | `ORACLE_SSO_AUDIT`  
Oracle Zero Data Loss Recovery Appliance | `ORACLE_ZDLRA`  
Oscar Claims | `OSCAR_CLAIMS`  
Open Source Intelligence | `OSINT_IOC`  
Osirium PAM | `OSIRIUM_PAM`  
OSTTRA MarkitWire | `OSTTRA_MARKITWIRE`  
Outline Activity Logs | `OUTLINE_ACTIVITY_LOGS`  
Outpost24 | `OUTPOST24`  
OutSystems Cloud | `OUTSYSTEMS_CLOUD`  
OVHcloud | `OVHCLOUD`  
OX Security | `OX_SECURITY`  
Packetlight Dwdm | `PACKETLIGHT_DWDM`  
Packet Viper | `PACKET_VIPER`  
PACOM Systems | `PACOM_SYSTEMS`  
PAGELY | `PAGELY`  
PagerDuty | `PAGERDUTY`  
Pagerduty Audit | `PAGERDUTY_AUDIT`  
Panorays | `PANORAYS`  
Palo Alto Cortex IIS | `PAN_CORTEX_XDR_IIS`  
Palo Alto DNS Security | `PAN_DNS_SECURITY`  
Palo Alto Networks Global Protect | `PAN_GLOBAL_PROTECT`  
Palo Alto Global Protect SVC | `PAN_GPSVC`  
Palo Alto Networks Prisma Access | `PAN_PRISMA_ACCESS`  
Palo Alto Prisma Cloud Workload Protection | `PAN_PRISMA_CWP`  
Palo Alto Prisma Dig Cloud DSPM | `PAN_PRISMA_DIG_CLOUD_DSPM`  
Palo Alto SSLVPN Access | `PAN_SSLVPN_ACCESS`  
Palo Alto Telemetry | `PAN_TELEMETRY`  
Palo Alto Cortex XDR Management Audit | `PAN_XDR_MGMT_AUDIT`  
Palo Alto Networks XSOAR Audit | `PAN_XSOAR`  
PaperCut Printing Management System | `PAPER_CUT`  
Passfort | `PASSFORT`  
Pathlock Identity Security Platform | `PATHLOCK`  
Pave | `PAVE`  
Paxton Access Control Systems | `PAXTON_ACS`  
SSL pcap | `PCAP_SSL_CLIENT_HELLO`  
Pega Automation | `PEGA`  
Penta Security Wapples | `PENTA_WAPPLES`  
Pentera | `PENTERA`  
Pentera ASV | `PENTERA_ASV`  
Pentera Leef | `PENTERA_LEEF`  
PeopleSoft | `PEOPLESOFT`  
People Strong | `PEOPLE_STRONG`  
Peplink Loadbalancer | `PEPLINK_LOADBALANCER`  
Peplink Router | `PEPLINK_ROUTER`  
Peplink Switch | `PEPLINK_SWITCH`  
Perception Point XRay | `PERCEPTION_POINT_XRAY`  
Perimeter 81 | `PERIMETER_81`  
Perplexity | `PERPLEXITY`  
PhishAlarm | `PHISHALARM`  
Domain Tools Phisheye | `PHISHEYE_ALERT`  
Phosphorus | `PHOSPHORUS`  
Pingcap TIDB | `PINGCAP_TIDB`  
Pingdom | `PINGDOM`  
PingOne Advanced Identity Cloud | `PINGONE_AIC`  
PingOne Protect | `PINGONE_PROTECT`  
Pingsafe | `PINGSAFE`  
Ping Access | `PING_ACCESS`  
Ping SDK | `PING_SDK`  
Plaso Super Timeline | `PLASO`  
Pleasant Password Server | `PLEASANT_PASSWORD_SERVER`  
Plixer Scrutinizer | `PLIXER_SCRUTINIZER`  
Pomerium | `POMERIUM`  
Portnox Audit | `PORTNOX_AUDIT`  
MS PowerShell Transcript | `POWERSHELL_TRANSCRIPT`  
Power DNS | `POWER_DNS`  
Preveil Enterprise | `PREVEIL_ENTERPRISE`  
Prismatic IO | `PRISMATIC_IO`  
Prisma SD-WAN | `PRISMA_SD_WAN`  
Procore | `PROCORE`  
Prompt Security | `PROMPT_SECURITY`  
ProofID | `PROOFID`  
Proofpoint Adaptive Email Security | `PROOFPOINT_ADAPTIVE_EMAIL_SECURITY`  
Proofpoint DLP | `PROOFPOINT_DLP`  
ProofPoint Email Protection | `PROOFPOINT_EMAIL_PROTECTION`  
Proofpoint Endpoint Data Loss Prevention | `PROOFPOINT_ENDPOINT_DLP`  
Proofpoint Identity Threat Platform | `PROOFPOINT_IDENTITY_THREAT_PLATFORM`  
Proofpoint Meta | `PROOFPOINT_META`  
Proofpoint Secure Share | `PROOFPOINT_SECURE_SHARE`  
Proofpoint Security Awareness Training | `PROOFPOINT_SECURITY_AWARENESS_TRAINING`  
Proofpoint Tap Campaign | `PROOFPOINT_TAP_CAMPAIGN`  
Proofpoint Tap People | `PROOFPOINT_TAP_PEOPLE`  
Proofpoint Tis IOC | `PROOFPOINT_TIS_IOC`  
Protegrity Defiance | `PROTEGRITY_DEFIANCE`  
Provision Asset Context | `PROVISION_ASSET_CONTEXT`  
Honeywell Pro-Watch | `PROWATCH`  
ProxMax | `PROXMAX`  
Proxmox | `PROXMOX`  
PRTG Network Monitor | `PRTG_NETWORKMONITOR`  
Puppet | `PUPPET`  
PureAuth ID | `PUREAUTH`  
Push Security | `PUSH_SECURITY`  
Pylon Audit Logs | `PYLON_LOGS`  
QLIK Audit | `QLIK_AUDIT`  
Qualtrics Audit | `QUALTRICS_AUDIT`  
Qualys User Activity | `QUALYS_ACTIVITY`  
Qualys File Integrity Monitoring | `QUALYS_FIM`  
Qualys Knowledgebase | `QUALYS_KNOWLEDGEBASE`  
Quest CA Audit | `QUEST_CA_AUDIT`  
Rabbit MQ | `RABBITMQ`  
Rackspace | `RACKSPACE`  
Radiantone | `RADIANTONE`  
RadiFlow IDS | `RADIFLOW_IDS`  
RSA RADIUS | `RADIUS`  
Radware Cloud WAF Service Access | `RADWARE_ACCESS`  
Radware Bot | `RADWARE_BOT`  
Radware DDoS Protection | `RADWARE_DDOS`  
RAD ETX | `RAD_ETX`  
Rancher API Audit Log | `RANCHER_API_AUDIT_LOG`  
Ransomcare | `RANSOMCARE`  
Rapid7 Cloud Security | `RAPID7_CLOUDSEC`  
Rapid7 Insights Threat Command | `RAPID7_INSIGHTS_THREAT_COMMAND`  
Rapid7 Security Onion | `RAPID7_SECURITY_ONION`  
Rapid Identity | `RAPID_IDENTITY`  
Raritan Dominion SX II | `RARITAN_DOMINION`  
Raven DB | `RAVEN_DB`  
RealiteQ | `REALITEQ`  
Reblaze Web Application Firewall | `REBLAZE_WAF`  
Recordedfuture Alerts | `RECORDEDFUTURE_ALERTS`  
Reco AI CSPM | `RECO_CSPM`  
Red Canary Cloud Protection | `REDCANARY_CLOUD_PROTECTION_RAW`  
Red Hat Identity Management | `REDHAT_IM`  
Redhat Jboss | `REDHAT_JBOSS`  
Red Hat Keycloak | `REDHAT_KEYCLOAK`  
RedHat Satellite Server | `REDHAT_SATELLITE`  
RedHat StackRox | `REDHAT_STACKROX`  
Redis | `REDIS`  
Redmine | `REDMINE`  
RedSift BrandTrust | `REDSIFT_BRANDTRUST`  
Red Access Browsing Security | `RED_ACCESS`  
Relativity | `RELATIVITY`  
ReliaQuest | `RELIAQUEST`  
Research and Education Networks Information Sharing and Analysis Center | `REN_ISAC`  
Reserved LogType1 | `RESERVED_LOG_TYPE_1`  
Reserved LogType10 | `RESERVED_LOG_TYPE_10`  
Reserved LogType11 | `RESERVED_LOG_TYPE_11`  
Reserved LogType12 | `RESERVED_LOG_TYPE_12`  
Reserved LogType13 | `RESERVED_LOG_TYPE_13`  
Reserved LogType14 | `RESERVED_LOG_TYPE_14`  
Reserved LogType15 | `RESERVED_LOG_TYPE_15`  
Reserved LogType16 | `RESERVED_LOG_TYPE_16`  
Reserved LogType17 | `RESERVED_LOG_TYPE_17`  
Reserved LogType18 | `RESERVED_LOG_TYPE_18`  
Reserved LogType19 | `RESERVED_LOG_TYPE_19`  
Reserved LogType20 | `RESERVED_LOG_TYPE_20`  
Reserved LogType21 | `RESERVED_LOG_TYPE_21`  
Reserved LogType22 | `RESERVED_LOG_TYPE_22`  
Reserved LogType23 | `RESERVED_LOG_TYPE_23`  
Reserved LogType24 | `RESERVED_LOG_TYPE_24`  
Reserved LogType25 | `RESERVED_LOG_TYPE_25`  
Reserved LogType26 | `RESERVED_LOG_TYPE_26`  
Reserved LogType27 | `RESERVED_LOG_TYPE_27`  
Reserved LogType28 | `RESERVED_LOG_TYPE_28`  
Reserved LogType29 | `RESERVED_LOG_TYPE_29`  
Reserved LogType3 | `RESERVED_LOG_TYPE_3`  
Reserved LogType30 | `RESERVED_LOG_TYPE_30`  
Reserved LogType31 | `RESERVED_LOG_TYPE_31`  
Reserved LogType32 | `RESERVED_LOG_TYPE_32`  
Reserved LogType33 | `RESERVED_LOG_TYPE_33`  
Reserved LogType34 | `RESERVED_LOG_TYPE_34`  
Reserved LogType35 | `RESERVED_LOG_TYPE_35`  
Reserved LogType36 | `RESERVED_LOG_TYPE_36`  
Reserved LogType37 | `RESERVED_LOG_TYPE_37`  
Reserved LogType38 | `RESERVED_LOG_TYPE_38`  
Reserved LogType39 | `RESERVED_LOG_TYPE_39`  
Reserved LogType4 | `RESERVED_LOG_TYPE_4`  
Reserved LogType40 | `RESERVED_LOG_TYPE_40`  
Reserved LogType41 | `RESERVED_LOG_TYPE_41`  
Reserved LogType42 | `RESERVED_LOG_TYPE_42`  
Reserved LogType43 | `RESERVED_LOG_TYPE_43`  
Reserved LogType44 | `RESERVED_LOG_TYPE_44`  
Reserved LogType45 | `RESERVED_LOG_TYPE_45`  
Reserved LogType46 | `RESERVED_LOG_TYPE_46`  
Reserved LogType47 | `RESERVED_LOG_TYPE_47`  
Reserved LogType48 | `RESERVED_LOG_TYPE_48`  
Reserved LogType49 | `RESERVED_LOG_TYPE_49`  
Reserved LogType5 | `RESERVED_LOG_TYPE_5`  
Reserved LogType50 | `RESERVED_LOG_TYPE_50`  
Reserved LogType6 | `RESERVED_LOG_TYPE_6`  
Reserved LogType7 | `RESERVED_LOG_TYPE_7`  
Reserved LogType8 | `RESERVED_LOG_TYPE_8`  
Reserved LogType9 | `RESERVED_LOG_TYPE_9`  
Retool | `RETOOL`  
Ribbon Session Border Controller | `RIBBON_SBC`  
Ring Central | `RING_CENTRAL`  
RiskIQ Digital Footprint | `RISKIQ_DIGITAL_FOOTPRINT`  
Risk Resecurity | `RISK_RESECURITY`  
Riverbed | `RIVERBED`  
RSA Cloud | `RSA_CLOUD`  
Rublon | `RUBLON`  
Rumble Network Discovery | `RUMBLE_NETWORK_DISCOVERY`  
S2W Quaxar | `S2W_QUAXAR`  
SafeBreach | `SAFEBREACH`  
SafeConnect NAC | `SAFECONNECT_NAC`  
SafeNet Network HSM | `SAFENET_HSM`  
Safe Cyber Risk Quantification | `SAFE_CRQ`  
SailPoint IdentityNow | `SAILPOINT_IDENTITYNOW`  
Salesforce Context | `SALESFORCE_CONTEXT`  
Salesforce Marketing Cloud Audit | `SALESFORCE_MARKETING_CLOUD_AUDIT`  
Salesforce Shield | `SALESFORCE_SHIELD`  
Salt Security API Protection Platform | `SALT_SECURITY`  
Sangfor IAG | `SANGFOR_IAG`  
Sangfor Network Detection and Response | `SANGFOR_NDR`  
Saporo | `SAPORO`  
SAP Business Warehouse | `SAP_BW`  
SAP Cloud for Customer | `SAP_C4C`  
SAP ERP | `SAP_ERP`  
SAP Enterprise Threat Detection | `SAP_ETD`  
SAP Commerce Cloud | `SAP_HAC`  
SAP IAS Context | `SAP_IAS_CONTEXT`  
SAP Identity Management | `SAP_IDM`  
SAP Insurance | `SAP_INSURANCE`  
SAP Leasing | `SAP_LEASING`  
SAS Institute | `SAS_INSTITUTE`  
SAS Metadata Server log | `SAS_METADATA_SERVER_LOG`  
Saturn Cloud | `SATURN_CLOUD`  
Savvy Security | `SAVVY_SECURITY`  
ScaleFusion for Windows MDM | `SCALEFUSION`  
Scale Computing | `SCALE_COMPUTING`  
Scality Ring Audit | `SCALITY_RING_AUDIT`  
Microsoft System Center Configuration Manager | `SCCM`  
Scylla | `SCYLLA`  
Secberus Cloud Security Governance | `SECBERUS`  
Secomea GateManager | `SECOMEA_GATEMANAGER`  
Sectigo SCM | `SECTIGO_SCM`  
Secui Bluemax NGF | `SECUI_BLUEMAX_NGF`  
Securden | `SECURDEN`  
SecurEnvoy SecurAccess | `SECURENVOY_MFA`  
Securesoft Sniper IPS | `SECURESOFT_SNIPER_IPS`  
Fiserv SecureNow | `SECURE_NOW`  
SecurityBridge Dev | `SECURITYBRIDGE_DEV`  
SecurityScorecard Platform | `SECURITYSCORECARD`  
SecurityBridge | `SECURITY_BRIDGE`  
Sekoia Ioc | `SEKOIA_IOC`  
Schweitzer Engineering Laboratories Port Server | `SEL_PORT_SERVER`  
Semperis ADFR | `SEMPERIS_ADFR`  
Sendgrid Api | `SENDGRID`  
Sendsafely | `SENDSAFELY`  
Senhasegura PAM | `SENHASEGURA_PAM`  
CloudWaves Sensato Nightingale Honeypot | `SENSATO_HONEYPOT`  
Senseon Alerts | `SENSEON_ALERTS`  
SensorFu Beacon | `SENSORFU_BEACON`  
SentinelOne Application | `SENTINELONE_APPLICATION`  
Sentra Data Loss Prevention | `SENTRA_DLP`  
Sentrigo | `SENTRIGO`  
Serpico | `SERPICO`  
Servertech PDUs | `SERVERTECH_PDUS`  
ServiceNow Antivirus Activity | `SERVICENOW_ANTIVIRUS_ACTIVITY`  
ServiceNow Attachment | `SERVICENOW_ATTACHMENT`  
ServiceNow Certificate Logs | `SERVICENOW_CERTIFICATE`  
ServiceNow Email | `SERVICENOW_EMAIL`  
ServiceNow Node | `SERVICENOW_NODE`  
ServiceNow Outbound HTTP | `SERVICENOW_OUTBOUNDHTTP`  
ServiceNow Roles | `SERVICENOW_ROLES`  
ServiceNow System log | `SERVICENOW_SYSLOG`  
ServiceNow Transaction | `SERVICENOW_TRANSACTION`  
ServiceNow User Logs | `SERVICENOW_USER`  
ServiceNow User Login History | `SERVICENOW_USER_LOGIN_HISTORY`  
Seti S4 | `SETI_S4`  
Sevco Security CMDB | `SEVCO_CMDB`  
Sharefile Logs | `SHAREFILE_LOGS`  
Sharepoint Unified Logging Service (ULS) | `SHAREPOINT_ULS`  
Shield IoT | `SHIELD_IOT`  
shodan.io | `SHODAN_IO`  
Siebel Monitoring | `SIEBEL`  
Siemens Desigo | `SIEMENS_DESIGO`  
Siemens Simatic S7 PLC SNMP | `SIEMENS_S7_PLC_SNMP`  
Siemens Simatic S7 PLC SYSLOG | `SIEMENS_S7_PLC_SYSLOG`  
Siemens SiPass | `SIEMENS_SIPASS`  
Siga Level Zero OT Resilience | `SIGA`  
Silver Peak Firewall | `SILVERPEAK_FIREWALL`  
Single Store | `SINGLE_STORE`  
Site24x7 | `SITE24X7`  
SiteGuard Server | `SITEGUARD_SERVER`  
SKYSEA Client View | `SKYSEA`  
Slack API | `SLACK_API`  
Smartsheet User Context | `SMARTSHEET_USER_CONTEXT`  
Smart Simple | `SMART_SIMPLE`  
Snapattack | `SNAPATTACK`  
Winevtlog Snare | `SNARE_WINEVTLOG`  
Snowflake Access | `SNOWFLAKE_ACCESS`  
Snowplow | `SNOWPLOW`  
Socomec UPS | `SOCOMEC_UPS`  
SOCRadar Incidents | `SOCRADAR_INCIDENTS`  
SoftEther VPN | `SOFTETHER_VPN`  
Software House Access Control | `SOFTWARE_HOUSE_ACS`  
Software House Ccure9000 | `SOFTWARE_HOUSE_CCURE9000`  
Solace PubSub Cloud | `SOLACE_AUDIT`  
SolarWinds Network Performance Monitor | `SOLARWINDS_NPM`  
SolarWinds Serv-U | `SOLARWINDS_SERV_U`  
Solar System | `SOLAR_SYSTEM`  
SolidServer | `SOLIDSERVER`  
SonarQube | `SONARQUBE`  
Sonatype Lifecycle | `SONATYPE_LIFECYCLE`  
Sonic Switch | `SONIC_SWITCH`  
Sophos Email Appliance | `SOPHOS_EMAIL`  
Sophos URL filtering | `SOPHOS_URL`  
Spacelift | `SPACELIFT`  
Spamhaus | `SPAMHAUS`  
Symantec Protection Engine | `SPE`  
SpecterX | `SPECTERX`  
Spirion | `SPIRION`  
Splashtop Remote Access and Support software | `SPLASHTOP`  
Splunk DNS | `SPLUNK_DNS`  
Splunk Phantom | `SPLUNK_PHANTOM`  
Splunk Intel Management | `SPLUNK_TRUSTAR`  
Sprinkledata(DWH) | `SPRINKLEDATA_DWH`  
Staffbase Audit | `STAFFBASE_AUDIT`  
Stairwell Inception | `STAIRWELL_INCEPTION`  
Statsig | `STATSIG`  
Statusgator | `STATUSGATOR`  
Stealthbits DLP | `STEALTHBITS_DLP`  
Stellar Cyber | `STELLAR_CYBER`  
Sterling Order Management System Data | `STERLING_OMS_DATA`  
Strata Maverics Identity Orchestration Platform | `STRATA_MAVERICKS`  
Stream Alert | `STREAMALERT`  
Stripe Payments | `STRIPE`  
Strivacity | `STRIVACITY`  
StrongDM | `STRONGDM`  
Supermicro IPMI | `SUPERMICRO_IPMI`  
Superna Eyeglass | `SUPERNA_EYEGLASS`  
SureView Systems Activity | `SUREVIEW_SYSTEMS`  
Suridata | `SURIDATA`  
Swift | `SWIFT`  
Symantec Advanced Threat Protection | `SYMANTEC_ATP`  
Symantec Data Center Security | `SYMANTEC_DCS`  
Symphony Summit AI | `SYMPHONYAI`  
Syncplify SFTP 2 Events | `SYNCPLIFY_SFTP`  
Syxsense | `SYXSENSE`  
Tanium Deploy | `TANIUM_DEPLOY`  
Tanium TanOS | `TANIUM_TANOS`  
TeamT5 ThreatSonar EDR | `TEAMT5_THREATSONAR_EDR`  
TeamViewer Tensor | `TEAMVIEWER_TENSOR`  
Technitium DNS | `TECHNITIUM_DNS`  
Tehtris EDR | `TEHTRIS_EDR`  
Temenos Journey Manager System Event Publisher | `TEMENOS_MANAGER_SYSTEMEVENT`  
Temporal Cloud Audit Logs | `TEMPORAL_CLOUD_AUDIT_LOGS`  
Tenable Vulnerabilities Management | `TENABLE_VMGNT`  
Tenable Web App Scanning | `TENABLE_WAS`  
Tencent CloudAudit | `TENCENT_CLOUD_AUDIT`  
Tencent Cloud Firewall | `TENCENT_CLOUD_FIREWALL`  
Tencent Cloud Waf | `TENCENT_CLOUD_WAF`  
Tencent Cloud Workload Protection | `TENCENT_CLOUD_WORKLOAD_PROTECTION`  
Teqtivity Assets | `TEQTIVITY_ASSETS`  
Teradata Access | `TERADATA_ACCESS`  
Teradata Aster | `TERADATA_ASTER`  
Teradici PCoIP | `TERADICI_PCOIP`  
Teramind | `TERAMIND`  
Tessian Cloud Email Security Platform | `TESSIAN_PLATFORM`  
TGDetect | `TGDETECT`  
Thales payShield 10K HSM | `THALES_PS10K_HSM`  
ThousandEyes | `THOUSAND_EYES`  
ThreatQuotient | `THREATQ_IOC`  
Thycotic devops secret vault | `THYCOTIC_DEVOPS_SECRETVAULT`  
Tiktok for Developers | `TIKTOK`  
Titan MFT | `TITAN_MFT`  
Titan SFTP Server | `TITAN_SFTP`  
Torq Audit Logs | `TORQ_AUDIT_LOGS`  
Tosi Hub | `TOSI_HUB`  
TP Link Network Switches | `TPLINK_SWITCH`  
Traceable API Security | `TRACEABLE_PLATFORM`  
Traefik Labs | `TRAEFIK`  
Transmit BindID | `TRANSMIT_BINDID`  
Transmit Security FlexID | `TRANSMIT_FLEXID`  
Transmit Security Mosaic CIAM | `TRANSMIT_MOSAIC_CIAM`  
Transmit Security Mosaic Fraud Prevention | `TRANSMIT_MOSAIC_FRAUD_PREVENTION`  
Transmit Security Mosaic Identity Verification | `TRANSMIT_MOSAIC_IDENTITY_VERIFICATION`  
Transmit Security Mosaic Management | `TRANSMIT_MOSAIC_MANAGEMENT`  
FIS Trax Payment Factory | `TRAX`  
Trellix Malware Analysis | `TRELLIX_AX`  
Trellix EX | `TRELLIX_EX`  
Trellix Network Detection and Response | `TRELLIX_NDR`  
Trend Micro Cloud App Security | `TRENDMICRO_CLOUDAPPSECURITY`  
TrendMicro Cloud Email Gateway Protection | `TRENDMICRO_CLOUD_EMAIL_GATEWAY_PROTECTION`  
Trend Micro EdgeIPS | `TRENDMICRO_EDGEIPS`  
TrendMicro EDR | `TRENDMICRO_EDR`  
Trend Micro Server Protect | `TRENDMICRO_SERVER_PROTECT`  
Trend Micro Vision One Risk Event | `TRENDMICRO_VISION_ONE_RISK_EVENT`  
TrendMicro Webproxy DSM | `TRENDMICRO_WEBPROXY_DSM`  
Trend Micro TippingPoint Security Management System | `TREND_MICRO_TIPPING_POINT`  
Tridium Niagara Framework | `TRIDIUM_NIAGARA_FRAMEWORK`  
Tripp Lite | `TRIPP_LITE`  
Tripwire Security Configuration Management | `TRIPWIRE_SCM`  
TrueFort Platform | `TRUEFORT`  
TrueNAS | `TRUENAS`  
E-Motional Transparent Screen Lock TSL RFID | `TSL_PRO`  
TT D365 | `TT_D365`  
TT MSAN DSLAM | `TT_MSAN_DSLAM`  
TT Trio Chordiant | `TT_TRIO_CHORDIANT`  
Tufin | `TUFIN`  
Tufin Secure Track | `TUFIN_SECURE_TRACK`  
Twilio Audit | `TWILIO_AUDIT`  
Twilio Authy | `TWILIO_AUTHY`  
Twilio Segment | `TWILIO_SEGMENT`  
TXOne EdgeIPS | `TXONE_EDGEIPS`  
Tyk IO | `TYK_IO`  
Ubiquiti Accesspoint | `UBIQUITI_ACCESSPOINT`  
Ubiquiti UDM Firewall | `UBIQUITI_FIREWALL`  
UDM | `UDM`  
Uipath | `UIPATH`  
Everfox ULTRA | `ULTRA`  
UltraDNS | `ULTRADNS`  
Ultra Electronics CyberFence | `ULTRA_CYBERFENCE`  
Unifi Router | `UNIFI_ROUTER`  
Unifi Switch | `UNIFI_SWITCH`  
Unifi System | `UNIFI_SYSTEM`  
Unit 21 | `UNIT21`  
UpGuard Incidents | `UPGUARD_INCIDENTS`  
Uptivity | `UPTIVITY`  
USBAV Koramis | `USBAV_KORAMIS`  
Valence Security | `VALENCE`  
Valimail | `VALIMAIL`  
Vanguard Active Alerts | `VANGUARD`  
Vanta Context | `VANTA_CONTEXT`  
Varnish Cache | `VARNISH_CACHE`  
Vector Dev | `VECTOR_DEV`  
Vectra AI | `VECTRA_AI`  
Vectra Protect | `VECTRA_PROTECT`  
Vectra Respond UX | `VECTRA_RUX`  
Velociraptor - digital forensic & incident response tool | `VELOCIRAPTOR`  
VMware VeloCloud SD-WAN | `VELOCLOUD_SDWAN`  
Venafi | `VENAFI`  
Vercara | `VERCARA`  
Veriato Cerebral | `VERIATO_CEREBRAL`  
Verizon Network Detection and Response | `VERIZON_NDR`  
Verkada | `VERKADA`  
Versa Director | `VERSA_DIRECTOR`  
Vertica Audit | `VERTICA_AUDIT`  
Vertiv UPS | `VERTIV_UPS`  
Very Good Security | `VERY_GOOD_SECURITY`  
Veza Access Control Platform | `VEZA`  
ViaControl Server Application | `VIACONTROL`  
Vicarious VRX Events | `VICARIUS_VRX_EVENTS`  
Virsec Event Logs | `VIRSEC_EVENT`  
Virsec Attack and Threat Logs | `VIRSEC_THREAT`  
Virtual Browser | `VIRTUAL_BROWSER`  
Virtual Network Flow Logs | `VIRTUAL_NETWORK_FLOW_LOGS`  
VirusTotal Threat Hunter | `VIRUSTOTAL_THREAT_HUNTER`  
VMRay Analyzer | `VMRAY_FLOG_XML`  
VMware Aria Logs | `VMWARE_ARIA_LOGS`  
VMware Avi Vantage Platform | `VMWARE_AVI_VANTAGE`  
VMware Cloud Director | `VMWARE_CD`  
VMware HCX | `VMWARE_HCX`  
VMware NSX AVI | `VMWARE_NSX_AVI`  
VMware SDDC | `VMWARE_SDDC`  
VMware SDWN Events | `VMWARE_SDWN_EVENTS`  
VMware Unified Access Gateway | `VMWARE_UNIFIED_ACCESS_GATEWAY`  
VMware vShield | `VMWARE_VSHIELD`  
Vonage | `VONAGE`  
VSFTPD Audit | `VSFTPD_AUDIT`  
Wallarm Webhook Notifications | `WALLARM_NOTIFICATIONS`  
Wallix Endpoint Privilege Management | `WALLIX_EPM`  
Wallix Privileged Access Management | `WALLIX_PAM`  
Waterfall Data Security Manager | `WATERFALL_DSM`  
WebEx | `WEBEX_SAAS`  
Web Methods Api Gateway | `WEBMETHODS_API_GATEWAY`  
Webroot Endpoint Protection | `WEBROOT`  
Webroot Identity Protection | `WEBROOT_IDENTITY_PROTECTION`  
White Cloud | `WHITECLOUD_EDR`  
WideField | `WIDEFIELD_SECURITY`  
Windows Bindplane | `WINDOWS_BINDPLANE`  
Windows NTP | `WINDOWS_NTP`  
Windows Filtering Platform | `WINDOWS_WFP`  
Winget Autoupdate | `WINGET_AUTOUPDATE`  
Wing Security | `WING_SECURITY`  
WireGuard VPN Logs | `WIREGUARD_VPN`  
WithSecure Cloud Protection | `WITHSECURE_CLOUD`  
WithSecure Elements Connector | `WITHSECURE_ELEMENTS`  
Witness AI Control | `WITNESS_AI_CONTROL`  
Wiz Audit | `WIZ_AUDIT`  
Wiz Runtime Execution Data | `WIZ_RUNTIME_EXECUTION_DATA`  
Wiz Vulnerabilities | `WIZ_VULNERABILITIES`  
Wolters Kluwer Teammate | `WOLTERS_KLUWER_TEAMMATE`  
Wordpress Simple History | `WORDPRESS_SIMPLE_HISTORY`  
Workato Audit Logs | `WORKATO`  
WorkDay User Sign In | `WORKDAY_USER_SIGNIN`  
Workiva Wdesk | `WORKIVA_WDESK`  
Workspot Control | `WORKSPOT_CONTROL`  
WPass | `WPASS`  
WP Engine | `WP_ENGINE`  
Wrike | `WRIKE`  
WSO2 IS AM | `WSO2_IS_AM`  
WS Ftp | `WS_FTP`  
Western Telematic Inc Console Servers | `WTI_CONSOLE_SERVERS`  
XDR.Net Digital Twin | `XDRNET_DIGITALTWIN`  
Xirrus Wireless Controller | `XIRRUS`  
XL Release | `XLR`  
XM Cyber | `XM_CYBER`  
Ysoft Data Security Manager | `YSOFT_DSM`  
Konica Minolta YSoft SafeQ | `YSOFT_SAFEQ`  
Yugabyte Database | `YUGABYTE_DATABASE`  
Zabbix | `ZABBIX`  
Zafran | `ZAFRAN`  
Zendesk Advanced Data Privacy and Protection | `ZENDESK_ADPP`  
Zimbra Mail | `ZIMBRA_MAIL`  
Zoho Assist | `ZOHO_ASSIST`  
Zoho Analytics Audits | `ZOHO_AUDIT`  
Zoho CRM | `ZOHO_CRM`  
ZoomInfo | `ZOOMINFO`  
Zoom Activity Logs | `ZOOM_ACTIVITY`  
ZPE Systems NodeGrid | `ZPE_SYSTEMS_NODEGRID`  
Zscaler Digital Experience | `ZSCALER_DIGITAL_EXPERIENCE`  
Zscaler Email DLP Insights | `ZSCALER_EMAIL_DLP_INSIGHTS`  
ZScaler NSS VM | `ZSCALER_NSS_VM`  
Zscaler Sandbox | `ZSCALER_SANDBOX`  
Zscaler Client Connector | `ZSCALER_ZCC`  
Zscaler ZDX | `ZSCALER_ZDX`  
Zuora App Logs | `ZUORA_APP_LOGS`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
