---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/shared-responsibility/
title: AlloyDB Omni shared responsibility \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:57:12.277907+00:00
---

# AlloyDB Omni shared responsibility  |  AlloyDB Omni using the RPM orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/shared-responsibility/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/resources)



Send feedback 

#  AlloyDB Omni shared responsibility Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/shared-responsibility)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/shared-responsibility)

This page describes what you, as an AlloyDB Omni customer, are responsible for, and what Google is responsible for when using the RPM orchestrator deployment option. 

As an AlloyDB Omni customer, you are responsible for configuring and operating AlloyDB Omni so that your workloads get the most value from the service.

## Shared responsibility matrix

The following table summarizes the responsibilities of Google and the customer across each layer of an AlloyDB Omni RPM orchestrator deployment:

Layer | Google's responsibility | Customer responsibility  
---|---|---  
**Hardware and host** | Physical infrastructure | Provide minimum and recommended requirements where applicable. | Provision physical servers, VMs, or edge devices including power, cooling, and hardware.  
| Host operating system (OS) | Provide minimum and recommended requirements where applicable. | Manage the Linux kernel, apply OS security patches, and harden the host nodes (such as RHEL 9 or Rocky Linux 9).  
**Infrastructure and OS components** | Storage | Provide minimum and recommended requirements where applicable. | Provision local disks or SAN volumes. AlloyDB Omni requires a block device configured with a supported file system such as XFS or ext4.  
| Networking | Provide minimum and recommended requirements where applicable. | Provision and manage the network layer—such as IP routing, load balancers, and firewall rules using `firewalld` or `iptables`—to open required ports such as `5432` for PostgreSQL and `2379` and `2380` for `etcd`.  
| Host access control | Provide the service accounts and roles required for the AlloyDB Omni orchestrator components. | Manage SSH access, `sudo` privileges, SELinux policies, and Linux user accounts to align with your internal security policies.  
| Secret management | Read standard variables and inventory files to provision resources, such as the initial `postgres` user. | Securely store passwords, SSH keys, and tokens used for Ansible orchestration and database access.  
| Certificate management | Provide configuration options for certificate integration. | Generate, distribute, and manage the lifecycle of Transport Layer Security (TLS) and SSL certificates on the host machines.  
**Orchestrator software** | Development and release | Develop the AlloyDB Omni orchestrator, including CLI and Ansible collections, and publish RPM packages. | None. You can use artifacts from the provided Yum repository for your deployments.  
| Installation and lifecycle | Provide documentation, RPM artifacts, and deployment inventory templates. |  Verify compatibility before installation. Follow instructions to install or upgrade AlloyDB Omni by using the `alloydbctl` orchestrator CLI or Ansible playbooks.  
**Database engine** | Database binary | Provide the AlloyDB Omni RPM packages with proprietary optimizations such as the columnar engine and AI acceleration. | None.  
| Patching | Release security patches and minor and major version updates for the engine. Provide upgrade instructions. | Schedule upgrades as soon as possible, depending on the criticality of each release.  
| User management |  Provision the initial administrative users. Provision the user-facing `postgres` superuser. Provide instructions for Lightweight Directory Access Protocol (LDAP) and Active Directory (AD) integration. |  Provide the password for the initial superuser. Create and manage all other roles and users.  
**Data management** | Backups | Provide the automation to manage backups using `pgBackRest` with S3-compatible integration. | Configure backup schedules and retention, and provision the local, S3, or Cloud Storage target bucket.  
| High availability (HA) | Provide the auto-failover logic and healing mechanisms using `etcd` and the Cluster Manager. | Provision sufficient nodes—such as a control node, `etcd` nodes, and primary and standby database nodes—to support failover and high-availability architectures.  
| Encryption at rest | Support deployments on block-level encrypted volumes. | Manage storage-layer encryption, such as Linux Unified Key Setup (LUKS) and `dm-crypt`, to meet your security requirements.  
| Encryption in transit | Configure server-side TLS for user-to-database connections and internal cluster communications. | Connect to the database by using secure TLS clients and manage the underlying certificate infrastructure.  
**Observability** | Metrics | Expose internal database metrics using a Prometheus-compatible endpoint. | Deploy and manage the scraper using Prometheus, OpenTelemetry, or other compatible solutions and their storage stack. Monitor the overall health of the system.  
| Logging | Write PostgreSQL and audit logs to files on disk and manage rotation. | Deploy log collectors, such as Fluent Bit or Vector, to ship logs to a storage backend such as Splunk or the ELK stack. Preserve logs for a recommended minimum of one month.  
| Visualization | Provide sample metrics and dashboards to monitor standard workloads. | Deploy and monitor the health of a visualization tool, such as Grafana. Create dashboards and incorporate them in your daily operational tasks.  
| Alerting | None. | Manage the alerting pipeline, such as by using a PagerDuty integration.  
**Support** | Troubleshooting | Provide support for software bugs and engine errors. To obtain this support, you need a [subscription](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/run-alloydb-omni-production). | Provide initial support through documentation and knowledge base. Debug infrastructure-related issues.  
  
## Security and FIPS compliance

To secure your data, AlloyDB Omni uses Federal Information Processing Standards (FIPS) 140-2 or 140-3 validated cryptographic modules. FIPS compliance is a shared responsibility between Google and the customer, as described in the following table:

FIPS boundary layer | Responsibility | Description  
---|---|---  
FIPS-compliant hardware | Customer | Physical hardware and cryptographic components must be NIST-certified and configured in a FIPS-approved state.  
Host OS | Customer | The VM or bare-metal host operating system (such as RHEL 9) must run in FIPS mode. Verify that the `cat /proc/sys/crypto/fips_enabled` command returns `1`.  
Orchestrator control plane | Customer | The control node running the Ansible orchestrator or CLI must use a FIPS-validated OS configuration.  
Orchestrator components | Google | Developed by Google, distributed as RPMs compatible with a FIPS-enabled base OS, securely managing cluster operations.  
Database binaries | Google | Link against FIPS-validated host OpenSSL cryptographic modules and enforce FIPS-approved algorithms for password hashing (`SCRAM-SHA-256`) and TLS cipher suites.  
Certificates from custom CA | Shared | Digital certificates must meet FIPS standards for key strength and signature algorithms. The certificate chain must trace back to a FIPS-compliant Root CA.  
  
## STIG shared responsibility

The Defense Information Systems Agency (DISA) publishes Security Technical Implementation Guides (STIGs) to establish cybersecurity standards and hardening requirements for software, operating systems, and databases.

Hardening your environment according to STIG requirements is essential for obtaining an Authorization to Operate (ATO) in highly secure or government sectors. While AlloyDB Omni implements many database-level security controls by default, achieving full STIG compliance is a shared responsibility that requires the customer to configure and verify infrastructure-level settings.

The following table lists the STIG vulnerability IDs that require action, validation, or configuration by the customer. For comprehensive information, see the [PostgreSQL 9.x on Red Hat Enterprise Linux Security Technical Implementation Guide (STIG) compliance checklist](https://ncp.nist.gov/checklist/802).

STIG or SRG ID | Security control description | Platform and operator default behavior | Required customer action or configuration  
---|---|---|---  
V-233535 | Alert support staff immediately on audit log failures. | Standard error diagnostics are written to `stdout` and `stderr`. | Customer must configure SIEM or log forwarder metrics to trigger when ingestion drops.  
V-233599 | Alert support staff when audit storage reaches 75% capacity. | File system metrics are exposed through standard Prometheus endpoints. | Customer must set up alerting rules in Prometheus and Grafana to notify support when the log disk space exceeds 75%.  
V-233610 | Off-load audit data to a separate continuous log facility. | Audit logs are persistently written to the local log directory. | Customer must configure a log forwarder to stream log files continuously to a central SIEM.  
V-233603 | Only trust end entity certificates issued by Public Key Infrastructure (PKI) or approved Certificate Authorities (CA). | Orchestrator uses local TLS configurations. | Customer must supply their PKI Root and Intermediate CA certificates to establish the chain of trust.  
V-233520 | Enforce approved logical access authorizations. | Rejects plain-text passwords and the Message-Digest algorithm 5 (MD5). Permits `SCRAM-SHA-256` over SSL. | Customer must configure clients to use `SCRAM-SHA-256` with `sslmode=verify-full` in their connection strings.  
V-233522 | Limit concurrent session thresholds per user. | Default database roles have infinite limits bounded by `max_connections`. | Customer must explicitly alter connection limits by using `ALTER ROLE ... CONNECTION LIMIT` for custom application roles.  
V-233584 | Use NSA-approved cryptography for classified information at rest. | RPM packages rely on secure, hardened RHEL 9 libraries. | Customer must verify that the underlying host Linux kernel has FIPS 140 mode enabled.  
V-233515 | Integrate with AD and LDAP organization-level authentication mechanisms. | Database supports custom authentication configurations. | Customer must map AD and LDAP identities into the database cluster configuration.  
V-233583 | Use FIPS-validated cryptographic modules for hashes. | RPMs rely on host OpenSSL FIPS modules for hashing functions. | Customer must activate FIPS mode on the host OS.  
V-233585 | Use FIPS-validated crypto to protect unclassified information. | Encrypts communication and storage by using FIPS-capable ciphers. | Customer must verify that host machines are FIPS-validated.  
V-233619 | Use FIPS-validated crypto modules for all operations. | Enforces FIPS-ready RPM binaries. | Customer must enable FIPS mode on the host kernel.  
V-233623 | Run the DBMS on a host with a certified OpenSSL FIPS module. | Database relies on host OpenSSL FIPS configurations. | Customer must verify that the host OpenSSL module matches the NIST-certified FIPS list.  
V-233615 | Map PKI-authenticated identities to associated user accounts. | Database uses secure `SCRAM-SHA-256` password authentication for identities. | Customer must map external organizational directory roles to database roles if they don't use direct password sign-in.  
V-233540 | Restrict database installation account to authorized users only. | RPM restricts file permissions and execution to the `postgres` user. | Customer must lock down host node access, such as with SSH restrictions, to prevent unauthorized terminal access to the VMs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
