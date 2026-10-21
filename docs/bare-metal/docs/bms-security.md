---
url: https://docs.cloud.google.com/bare-metal/docs/bms-security/
title: Provide security for enterprise workloads in a Bare Metal Solution environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:36.968146+00:00
---

# Provide security for enterprise workloads in a Bare Metal Solution environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-security/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Provide security for enterprise workloads in a Bare Metal Solution environment

Because Bare Metal Solution enables you to bring traditional enterprise workloads closer to Google Cloud, a common question from enterprise architects and security architects is "How do I secure my workloads?" The goal of this guide is to provide you with the security and compliance design elements that you should consider when planning to bring your enterprise workloads, such as Oracle databases, to Bare Metal Solution. We'll also discuss Google Cloud's security controls and features that safeguard your enterprise assets, and point you to some of Oracle's security best practices.

## Security in a Bare Metal Solution environment

The Bare Metal Solution environment includes purpose-built, bare-metal servers hosted in _regional extensions_. As seen in Figure 1, a regional extension is a colocation facility placed near select Google Cloud regions and connected to Google Cloud with a managed high-performance connection and a low-latency network fabric.

**Figure 1: Bare Metal Solution - Regional Extension connected to Google Cloud**

![Regional Extension connected to Google Cloud](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-architecture-2.svg)

Because of this architecture, you need to consider ways to secure both your Bare Metal Solution servers and the Google Cloud components included in your design. Fortunately, Google Cloud provides and manages the following components for Bare Metal Solution:

  * Core infrastructure, including secure, controlled-environment facilities and power
  * Physical security
  * Network infrastructure and security
  * Hardware monitoring capabilities
  * Access to Google Cloud services
  * Provisioning and maintenance of sole-tenancy hardware
  * Local storage area network (SAN)
  * Smart hands support: Onsite support for activities like hardware replacements



In a Bare Metal Solution environment, security is a shared responsibility. The good news is that you can bring your own security best practices and supplement them with the built-in offerings that Bare Metal Solution provides. Figure 2 shows a summary of which security components that you need to supply, and which ones Google Cloud provides.

**Figure 2: Summary of security responsibilities - customer and Google Cloud**

![Summary of security responsibilities - customer and Google Cloud](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-security-2.svg)

## Plan security for your Bare Metal Solution environment

To plan your security strategy for Bare Metal Solution, you need to consider the following six _security pillars_ :

  1. Physical security
  2. Compliance
  3. Network security
  4. Data security
  5. Operational security
  6. Database security



Let's explore each of these security pillars in more detail.

### Physical security

The physical components of Bare Metal Solution reside in a regional extension (a colocation facility) run by a vendor. A high speed, low-latency [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) connection links the regional extension to the nearest Google Cloud region.

The vendor manages the regional extension and its facilities, such as power, cooling, racking and stacking, and storage management. The vendor also maintains industry standard physical security and safety features, including, but not limited to the following:

  * Cages have secure slab-to-slab walls or mesh tops.
  * Video cameras at each facility monitor the cages, aisles, and doors 24 hours a day, 7 days a week. The cameras have a clear view inside each cage, for every aisle, and for every entrance and exit door.
  * All doors in the facility have alarms to ensure that they are closed properly.
  * Anyone entering a cage must have prior approval from the regional extension coordination team, and appropriate access granted through the regional extension security team.
  * The regional extension coordination team manages all access with individual tickets per visit.
  * The facility requires authorized staff to use a biometric lock to enter the facility and a badge to exit.
  * All racks are locked. An electronic key locker distributes keys for specific racks to authorized staff on a limited "need-to-use" basis. The key locker also tracks rack access.
  * A colocation security team manages access and maintains reporting based on PCI and ISO compliance certification requirements.
  * Other physical security measures are consistent with industry best practices and applicable regulatory requirements.



### Compliance

Bare Metal Solution meets demanding compliance requirements with industry certifications such as ISO, PCI DSS, and HIPAA, plus regional certifications where applicable. For more information about compliance, please visit the [Compliance resource center](https://cloud.google.com/security/compliance).

### Network security

Network security is offered at two layers, as shown in Figure 3:

  1. Layer 3 VLAN attachments connect your Google Virtual Private Cloud to a unique virtual routing and forwarding instance (VRF) on the Bare Metal Solution edge routers.

  2. Within the Bare Metal Solution environment, Layer 2 VLANs provide the security and isolation necessary for your data. You use a _client subnet_ to connect to Google Cloud, and an optional _private subnet_ to host your own services and storage.




**Figure 3: Network security in a Bare Metal Solution environment**

![Network security in a Bare Metal Solution environment](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-security-3.svg)

If you use Google Cloud APIs from within the Bare Metal Solution environment to access Google Cloud services, Google Cloud encrypts the data transfer by default between Bare Metal Solution and the particular service per our encryption policies. For example, if you use the Google Cloud CLI or APIs to back up data in Cloud Storage, the transfer of the data from Bare Metal Solution to Cloud Storage uses data encryption by default.

#### Enforce a secure perimeter with Private Google Access

[Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid) (also known as _VPC service controls_) enables you to define security perimeters around sensitive data in Google Cloud services and offers the following benefits:

  * Mitigates _data exfiltration_ risks. Data exfiltration happens when an authorized person extracts data from a secured system where the data belongs, and either shares it with an unauthorized third party or moves it to an insecure system.
  * Accesses Google Cloud services privately from on-premises.
  * Enforces context-aware access from the internet.
  * Manages security policies from a central location.



With Bare Metal Solution, you can leverage Google Cloud's cloud-native and scalable services by way of the Partner Interconnect. Enabling a VPC Service controls-based perimeter further ensures that the access to all Google Cloud services, such as BigQuery and Cloud Storage, happens without any data exfiltration to the internet.

To set up private access to Google APIs, see [Configuring Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid). Figure 4 shows an example of Private Google Access:

**Figure 4: Private Google Access in a Bare Metal Solution environment**

![Private Google Access in a Bare Metal Solution environment](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-security-4.svg)

### Data security

When planning for data security in a Bare Metal Solution environment, you need to be aware of how encrypted data gets stored and how to secure your applications running on Google Cloud or in an on-premises data center.

#### Storage encryption

By default, Bare Metal Solution encrypts data at rest. Here are a few facts about storage encryption at rest in a Bare Metal Solution environment:

  * To provision storage, we create a Storage Virtual Machine (SVM) on a NetApp cluster for each customer, and associate the SVM with a reserved data volume before giving it to the customer.
  * When we create an encrypted data volume, the encryption process generates a unique XTSAES-256 data encryption key. We never pre-generate a key.
  * The SVMs provide isolation in a multitenant environment. Each SVM appears as a single independent server, which enables multiple SVMs to coexist in a cluster and ensures that no data flows between the SVMs.
  * We do not display the keys in plain text. The NetApp onboard key manager stores, manages, and protects the keys.
  * Neither Google Cloud nor the vendor have access to your keys.
  * The Netapp Storage Cluster stores and encrypts all data at rest, including the operating system and boot partitions.
  * If you choose to stop using Bare Metal Solution at the end of your contract, we cryptographically erase and quarantine your storage volumes for 7 days before they can be reused.



#### Application security

When working with Bare Metal Solution, you can secure your applications running in either Google Cloud or in an on-premises environment.

##### Applications running in Google Cloud

  * Bare Metal Solution runs in regional extensions; the only network path to or from the regional extension is through a Partner Interconnect to the associated Google Cloud region over customer-specific VLAN attachments.
  * By default, Bare Metal Solution servers do not have internet access. If you need internet access for operations like patching or updates, create a NAT instance. For more information, see [Accessing the internet](https://docs.cloud.google.com/bare-metal/docs/bms-setup#bms-access-internet).
  * A BGP session provides dynamic routing between the Cloud Routers in the VPC and the regional extension's routers. As a result, if you place resources in the VPC attached to the regional extension, these resources have direct access to the Bare Metal Solution servers. Similarly, resources running in newly added subnets also have access to the Bare Metal Solution servers. If you need to allow or deny access to specific resources, use firewall policies to restrict the default behavior that permits access to all Bare Metal Solution resources.
  * As shown in Figure 5, use _VPC peering_ to enable resources running in a different VPC in the same project or a different project to access the Bare Metal Solution servers. On the redundant Cloud Routers, add a custom advertisement pointing to the CIDR range of the peered network.

**Figure 5: VPC peering and the Bare Metal Solution environment**

![VPC peering and the Bare Metal Solution environment](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-security-5.svg)

  * As shown in Figure 6, use a _shared VPC_ architecture to allow resources from different projects to access the Bare Metal Solution servers. In this case, you must create VLAN attachments in the host project so that all resources can access the servers attached to the shared VPC.

**Figure 6: Shared VPC and the Bare Metal Solution environment**

![Shared VPC and the Bare Metal Solution environment](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-security-6.svg)

  * You can back up your databases with either Oracle Recovery Manager (RMAN) or backup solutions like Actifio. To learn how Actifio integrates natively with RMAN, see the following [Actifio guide](https://docs.actifio.com/10.0/PDFs/DBAOracle.pdf). You can store backup data in [Cloud Storage](https://docs.cloud.google.com/storage) and select different Cloud Storage tiers to satisfy your requirements for the Recovery Time Objective (RTO) and the Recovery Point Objective (RPO).




##### Applications running on-premises

  * As previously mentioned, the only network path to or from the Bare Metal Solution regional extension is through a Partner Interconnect to the associated Google Cloud region. To connect to your Bare Metal Solution servers from your on-premises environment, you must connect your on-premises data center to Google Cloud by using a [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview), [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview), or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview). For more information about these connection options, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).
  * To enable routes to your on-premises network, you must modify the redundant Cloud Routers with a custom advertisement pointing to the CIDR range of the on-premises subnet. Use firewall rules to allow or block access to the servers.



### Operational security

In the Physical Security section of this guide, you learned that we heavily restrict access to the Bare Metal Solution infrastructure within a regional extension. We provide access to authorized staff on a temporary, limited, "need-to-use" basis. We audit the access logs, analyze them to detect any anomalies, and use 24/7 monitoring and alerting to prevent unauthorized access.

For operational security, there are several options. One solution that integrates natively with Google Cloud is Blue Medora's [Bindplane](https://www.bluemedora.com/products/bindplane) product. [Bindplane](https://www.bluemedora.com/products/bindplane) integrates with [Google Cloud Observability agents](https://docs.cloud.google.com/stackdriver/docs/solutions/agents) and lets you to capture metrics and logs from the Bare Metal Solution infrastructure, including Oracle database and Oracle applications logs.

[Prometheus](https://prometheus.io/) is an open source monitoring solution that you can use to monitor the Bare Metal Solution infrastructure and the Oracle databases running on top of it. You can direct database and system audit trails into Prometheus, which acts as a single pane of glass to monitor and send alerts for any suspicious activity.

[Oracle Enterprise Manager](https://www.oracle.com/enterprise-manager/technologies/) is popular with those who use it in an on-premises environment. You can use OEM in a Bare Metal Solution environment to perform monitoring and alerting tasks in the same way as your on-premises data center.

### Database security

We designed Bare Metal Solution to be as similar as possible to your on-premises environment so that you can use it with the least amount of effort and learning. As a result, you can easily bring your existing security-related Oracle database features, security practices, and processes to Bare Metal Solution. You can supplement your security portfolio with the security features that Google Cloud provides.

For database security, let's review the Oracle's security controls that you should enable. This includes user authentication, authorization and access control, auditing, and encryption.

#### User authentication

  * Implement password policies, such as complexity and length, if using basic authentication.
  * Strengthen your authentication system by using TLS certificates, Kerberos, or RADIUS.
  * Use proxy-based authentication to enable authentication and auditing at the database level. This method is useful if you choose not to map application users to database users and you enable authentication at the application level.



For more authentication recommendations, see [Configuring Authentication](https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/configuring-authentication.html#GUID-00632C9C-5C01-4C8F-A4D0-5E575502A6AE) in the Oracle Database Security Guide.

#### Authorization and access control

  * Manage authorization through _object privileges_ , _system privileges_ , and _roles_ identified inside the database. You can also complement this practice with more advanced and secure features like Database Vault.
  * Manage users and groups with _Centrally Managed Users_ (CMU). With CMU, you can leverage your existing Active Directory infrastructure to centralize the management of database users and authorization across multiple Oracle databases.

For more information about CMU, see [Configuring Centrally Managed Users with Microsoft Active Directory](https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/integrating_mads_with_oracle_database.html#GUID-9739D541-FA9D-422A-95CA-799A4C6F488D) in the Oracle Database Security Guide.

  * Use _Database Vault_ to introduce separation of duties and access control for highly privileged users.

For more information about Database Vault, see the [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/en/database/oracle/oracle-database/21/dvadm/index.html).

  * Leverage additional tools and techniques, such as _privilege analysis_ and _data redaction_.

    * The privilege analysis tool helps you actively monitor the usage of privileges and roles by end users. For more information on privilege analysis, see [Performing Privilege Analysis to Find Privilege Use](https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/performing-privilege-analysis-find-privilege-use1.html#GUID-44CB644B-7B59-4B3B-B375-9F9B96F60186) in the Oracle Database Security Guide.
    * Data redaction removes sensitive column data and allows access only to required users. For more information on data redaction, see [Using Oracle Data Redaction](https://docs.oracle.com/en/database/oracle/oracle-database/21/asoag/asopart2.html) in the Oracle Database Advanced Security Guide.
  * Use _Virtual Private Database_ (VPD) and _Oracle Label Security_ (OLS) to create fine-grained access to data by modifying user queries dynamically. These tools exclude rows that are filtered by the VPD policy, and manage row and user labels to identify whether a user should have access to a specific row.

    * For more details on VPD, see [Using Oracle Virtual Private Database to Control Data Access](https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/using-oracle-vpd-to-control-data-access.html#GUID-06022729-9210-4895-BF04-6177713C65A7) in the Oracle Database Security Guide.
    * For more details on OLS, see the [Oracle Label Security Administrator's Guide](https://docs.oracle.com/en/database/oracle/oracle-database/21/olsag/).
  * Follow the principle of least privilege by assigning fine-grained role privileges to groups and users.




#### Auditing

  * Leverage _unified auditing_ , a feature that sends all audit data to a unified audit trail. Introduced in Release 12c to replace traditional database auditing, this feature creates a central trail file for all database-related audit events and enhances audit report performance.
  * Enable _fine grained auditing_ (FGA) to extend traditional auditing capabilities. This feature captures audit data only when a user accesses a specific column or meets a specific condition.
  * Use _audit vault database firewall_ (AVDF) to manage audit policies and captured events. One of the main use cases for ADVF is to prevent SQL injection attacks. You set up the database firewall to monitor all SQL statements issued against the database for a full application lifecycle. The database builds a set of trusted clusters, then blocks any SQL statement not known to the database firewall.

For more information, see the [Monitoring Database Activity with Auditing](https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/part_6.html) in the Oracle Database Security Guide and the [Audit Vault and Database Firewall Guide](https://docs.oracle.com/en/database/oracle/audit-vault-database-firewall/20/index.html).




#### Encryption for data at rest and in-transit

  * While Bare Metal Solution automatically encrypts user data at rest using a unique AES 256-bit key per data volume , you can also enable _Transparent Data Encryption_ (TDE) to gain more control over the encryption key lifecycle.
  * Use _native network encryption_ or _Transport Layer Security_ (TLS)-based encryption to secure data between the client and the database.
  * When using customer managed encryption keys (CMEK) for Oracle database data, use the _advanced security option_ (ASO) to enable encryption, cryptographic network checksums (different from log checksum during reads and writes), and authentication services between the primary and standby systems in Data Guard.

For more details on encryption options, see [Using Transparent Data Encryption](https://docs.oracle.com/en/database/oracle/oracle-database/21/asoag/asopart1.html) in the Oracle Database Advanced Security Guide.




The suggestions we've mentioned for Oracle Database security on Bare Metal Solution are not intended to be an exhaustive list. We strongly recommend that you follow the best practices and recommendations provided by Oracle, and implement appropriate controls that suit your specific business and security needs.

## Summary

Bare Metal Solution is your gateway to the world of Google Cloud. It enables you to migrate and run your critical workloads as-is and closer to the cloud, while you decide, design, and plan your cloud future. Coupled with the best practices, tools, and techniques shared in this guide, Bare Metal Solution provides a secure, robust, and powerful platform to run your critical workloads.

Most importantly, this endeavor does not need to be at the expense of security. When you subscribe to Bare Metal Solution, you receive bare-metal servers backed by multiple layers of built-in security, including the physical layer, the storage layer, and the network layer. As such, the Bare Metal Solution service integrates security at every stage within the infrastructure to meet your mission-critical needs for secure performance at scale.

**Key takeaways:**

  1. Security is a shared responsibility.
  2. Follow the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).
  3. Follow the principle of separation of duties.
  4. Prevent data exfiltration by accessing Google Cloud services through restricted.googleapis.com.
  5. Enable Private Google Access in your project to mitigate data exfiltration, unauthorized access, and to control security policies centrally.
  6. Follow the best practices laid out by Oracle for Oracle database security.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
