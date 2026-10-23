---
url: https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning/
title: Version 2.0: BigQuery Connector for SAP planning guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:48.499507+00:00
---

# Version 2.0: BigQuery Connector for SAP planning guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Version 2.0: BigQuery Connector for SAP planning guide Stay organized with collections  Save and categorize content based on your preferences. 

This planning guide provides SAP and Google Cloud administrators with the information they need to plan for the replication of SAP data into BigQuery by using **version 2.0 or 2.1** of the BigQuery Connector for SAP with SAP LT Replication Server.

BigQuery Connector for SAP installs into SAP Landscape Transformation Replication Server (SAP LT Replication Server) and enables near real time replication of SAP data directly into BigQuery.

With your data in BigQuery, you can perform real-time analytics with artificial intelligence or machine learning on live SAP application data. In BigQuery, you can also integrate your SAP data with data from other sources.

This guide covers the following topics:

  * Overview of BigQuery Connector for SAP
  * Installation architectures
  * Software requirements
  * Security
  * Networking
  * Performance planning
  * Table and field mapping options
  * Support lifecycle



For step-by-step instructions for installing and configuring SAP LT Replication Server replications with BigQuery Connector for SAP, see [BigQuery Connector for SAP installation and configuration guide](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config).

For information about BigQuery, see [What is BigQuery?](https://docs.cloud.google.com/bigquery/docs/introduction).

For information about solution accelerators for SAP data modeling in BigQuery, see the [Google Cloud Cortex Framework](https://cloud.google.com/solutions/cortex).

## Overview of BigQuery Connector for SAP

BigQuery Connector for SAP uses the standard interfaces and capabilities of [SAP Landscape Transformation Replication Server](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US) and supports all of the data sources that SAP LT Replication Server supports.

BigQuery Connector for SAP is provided by Google Cloud in the form of transport files that you install into SAP LT Replication Server.

Download the installation package that contains the transport files before you are ready to install BigQuery Connector for SAP. Although BigQuery Connector for SAP is currently offered at no cost, you do need a [Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account) to receive the installation package. For more information, see [Download the installation package](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-on-gc#download-install-pkg).

BigQuery Connector for SAP is a Google Cloud implementation of an SAP [Business Add In (BAdI)](https://help.sap.com/viewer/46a2cfc13d25463b8b9a3d2a3c3ba0d9/LATEST/en-US/8ff2e540f8648431e10000000a1550b0.html) for SAP LT Replication Server. BigQuery Connector for SAP is developed by Google Cloud by following [SAP LT Replication Server SDK process](https://help.sap.com/viewer/007c373fcacb4003b990c6fac29a26e4/LATEST/en-US/2a0e4839836e4c10a01b0ca172b64c6c.html).

BigQuery Connector for SAP leverages the change data capture functionality of SAP LT Replication Server.

### Data processing

BigQuery Connector for SAP sends the SAP records directly to BigQuery from SAP LT Replication Server without any intermediary data integration layers or tools.

Upon receiving the records, BigQuery appends them to the table in an insert-only mode. If BigQuery receives an update to a record that already exists in the BigQuery table, BigQuery inserts a new instance of the record into that table without modifying the existing instance. The most recently inserted instance of the record reflects the current state of the record in the source table.

BigQuery Connector for SAP allows only minimal data transformation, conforming to an _extract, load, transform_ model (ELT), as opposed to an _extract, transform, and load_ (ETL) model. For more information about these models, see [Procedures and patterns for data pipelines](https://docs.cloud.google.com/architecture/dw2bq/dw-bq-data-pipelines#procedures_and_patterns_for_data_pipelines).

BigQuery Connector for SAP automatically suggests the fields, field names, and data types for the target table based on the source data. Before the target BigQuery table is created, you can modify the suggested values as needed.

The suggested names for the target fields are based on the descriptions of the fields in the source table. For more information, see Default naming options for fields.

Although BigQuery Connector for SAP automatically suggests the BigQuery data types for most fields, boolean, timestamp, and hexadecimal values cannot be interpreted automatically, so you need to map them manually. For more information, see Data type mapping.

BigQuery Connector for SAP provides several enhancement spots where you can insert your own custom enhancements into BigQuery Connector for SAP code. For more information, see [Enhancement exits](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#enhancement-exits).

If a target table doesn't already exist in BigQuery, then BigQuery Connector for SAP creates one.

After replication begins, SAP records are added to BigQuery in an insert-only mode.

**Note:** In insert-only mode, any change to a record in the source table results in a new insert of the record in the BigQuery target table.

### Security

You control access to BigQuery Connector for SAP in SAP LT Replication Server by using the SAP LT Replication Server role-based authorization system. When you install BigQuery Connector for SAP, the transport files include custom roles for BigQuery Connector for SAP. For more information about the custom roles, see SAP security.

You control access to Google Cloud and BigQuery by using [Identity and Access Management authentication and authorization](https://docs.cloud.google.com/iam/docs/overview) and the [BigQuery API authentication](https://docs.cloud.google.com/bigquery/docs/authentication). For more information, see Google Cloud security.

For communication between BigQuery Connector for SAP and BigQuery, BigQuery Connector for SAP uses end-to-end HTTPS communication and SSL.

For information from SAP about authorization, see the _Security Guide_ for your version of SAP LT Replication Server in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

### Scalability

For very large volumes, such as billions of data records with millions of deltas, BigQuery Connector for SAP uses SAP LT Replication Server scaling and partitioning functions to parallelize the data extraction at scale. For more information, see the _Sizing Guide_ for your version of SAP LT Replication Server in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

On the BigQuery side, BigQuery Connector for SAP uses the [BigQuery streaming API](https://docs.cloud.google.com/bigquery/streaming-data-into-bigquery) to scale data loading.

## Installation architecture

You install BigQuery Connector for SAP as a Business Add-In (BAdI) within an SAP LT Replication Server instance.

The SAP LT Replication Server instance can be on Google Cloud, on premises, or on another cloud provider. Wherever SAP LT Replication Server is running, it should be as close to the source system as possible. Work with your network team to ensure low latency and high throughput between the source SAP system, SAP LT Replication Server, and your BigQuery dataset.

The following sections describe common, recommended architectures for BigQuery Connector for SAP.

### Architecture for SAP data sources on Google Cloud

The following diagram shows two example SAP LT Replication Server installations on Google Cloud with the SAP data source on Google Cloud.

To show an example of each architecture, one installation uses an SAP LT Replication Server _standalone_ architecture, in which SAP LT Replication Server is installed on a separate server, and the other uses an SAP LT Replication Server _embedded_ architecture, in which SAP LT Replication Server is installed in the SAP source system server.

Because the SAP LT Replication Server instances are installed on Google Cloud, BigQuery Connector for SAP connects to the BigQuery API endpoint directly, without requiring a Cloud Interconnect or Cloud VPN connection.

In the diagram, the SAP systems and BigQuery are shown in different Google Cloud projects, but you can use the same project for both, if necessary.

![Diagram is described in the preceding text](https://docs.cloud.google.com/sap/docs/images/bqc4sap-architecture-gc.svg)

### Architecture for SAP data sources on-premises or on another cloud provider

The following diagram shows two example SAP LT Replication Server installations that are running either on premises or on another cloud provider.

To show an example of each architecture, one installation uses an SAP LT Replication Server standalone architecture and the other uses an SAP LT Replication Server embedded architecture.

In both examples, SAP LT Replication Server is installed in the same environment as the SAP data source.

The connection from BigQuery Connector for SAP in SAP LT Replication Server to BigQuery is provided by either a Cloud Interconnect connection or a Cloud VPN connection.

![Diagram is described in the preceding text](https://docs.cloud.google.com/sap/docs/images/bqc4sap-architecture-off-platform.svg)

### Detailed architectural view of the data flow

The following diagram shows where BigQuery Connector for SAP fits into the SAP LT Replication Server data flow.

The numbers in the diagram are explained following the diagram.

![Diagram is described in the preceding text](https://docs.cloud.google.com/sap/docs/images/bqc4sap-architecture-replication-detail.svg)

The following numbered explanations correspond to the numbers in the diagram:

  1. After SAP LT Replication Server is initialized, when records in the source tables are inserted, updated, or deleted, the database trigger records the changes in the logging tables.
  2. SAP LT Replication Server continuously checks the logging tables for new entries via RFC calls.
  3. If SAP LT Replication Server finds new entries, then the Read engine reads the records and calls the Mapping and transformation engine.
  4. The Mapping and transformation engine calls the Write engine, which invokes BigQuery Connector for SAP.
  5. BigQuery Connector for SAP performs the following actions: 
     1. Maps the SAP data to the target table name, field names, and BigQuery data types.
     2. Creates the BigQuery table, if necessary.
     3. Sends the records to BigQuery in chunks through the [BigQuery streaming API](https://docs.cloud.google.com/bigquery/streaming-data-into-bigquery).
  6. Upon receiving the data, BigQuery takes the following actions: 
     1. Performs validation checks.
     2. Inserts the records into the target table.
     3. Sends an HTTP 200 (`OK`) status code back to BigQuery Connector for SAP.
  7. BigQuery Connector for SAP passes the HTTP `OK` status code back to SAP LT Replication Server, which deletes the replicated entries from the logging table and frees resources on the SAP source system.



## Software requirements

BigQuery Connector for SAP supports the major in-maintenance enterprise application versions as data sources, as well as older legacy applications. Some of the supported SAP applications include:

  * SAP Business Suite 7
  * S/4HANA
  * SAP applications running on SAP NetWeaver



You can install BigQuery Connector for SAP in SAP LT Replication Server on Google Cloud, on-premises, or on public clouds, such as AWS, Azure, and so forth.

### Licensing

BigQuery Connector for SAP is made available as "Software" under the agreement governing your use of Google Cloud Platform, including the Service Specific Terms available at <https://cloud.google.com/terms/service-terms>. Without limiting the generality of the above terms, you may not modify or distribute BigQuery Connector for SAP without express written permission from Google.

BigQuery Connector for SAP software is currently offered at no cost. For clarity, your use of other "Software" and "Services" under the agreement governing your use of Google Cloud Platform, such as BigQuery and BigQuery streaming API, may incur a cost.

BigQuery Connector for SAP does not include any license to SAP software, including without limitation SAP LT Replication Server; please separately procure an appropriate license to SAP software.

### SAP software version requirements

The required versions of SAP LT Replication Server and the SAP source systems differ depending on whether you install SAP LT Replication Server on its own server in a standalone architecture or within the source ABAP application system in an embedded architecture.

The SAP software requirements are also different depending on the SAP system that you are using as the data source: SAP S/4HANA or SAP ECC.

To see the SAP software versions that Google Cloud supports BigQuery Connector for SAP with, select the tab that corresponds to your SAP source system:

###  S/4HANA 

Installation architecture | System | Supported versions | User Interface (UI) Add-On  
---|---|---|---  
Standalone | Source system | 

  * **NetWeaver 7.5** or later or any version of **ABAP Platform**.  To ensure that the DMIS versions on the source and target systems are compatible, see [SAP Note 2577774](https://launchpad.support.sap.com/#/notes/2577774). 
  * **SLT add on** : DMIS 2011 SP15, DMIS 2018 SP00, DMIS 2020, or any version of S4CORE.

|  The SAP_UI component must be compatible with your SAP Netweaver version. **/UI2/CL_JSON** : PL12 or later.  For information about SAP add-on compatibility, see: 

  * [Master Guide for UI Add-On](https://help.sap.com/viewer/05410851eb894cac99df50a874e8a0b4/LATEST/en-US/21b69100cdbe4fd68fc614774eb9c97c.html)
  * [Software Component SAP_UI](https://help.sap.com/doc/saphelp_nw74/LATEST/en-us/35/828457ed26452db8d51c840813f1bb/content.htm?no_cache=true)
  * [SAP Note 2217489 - Maintenance and Update Strategy for SAP Fiori Front-End Server](https://launchpad.support.sap.com/#/notes/2217489)
  * [SAP Note 2211016 - UI add-on 2.0 for SAP NetWeaver: support package stack mapping to SAP_UI 7.50 & UI5 / UI2 versions](https://launchpad.support.sap.com/#/notes/2211016)

  
SAP LT Replication Server system | 

  * **NetWeaver** 7.0 (with EHP2) or later or any version of **ABAP Platform**.
  * **SLT add on** : DMIS 2011 SP15 or later, DMIS 2018 SP00 or later, or DMIS 2020 SP00 or later.

  
Embedded | Source system | 

  * **NetWeaver 7.5** or later or any version of **ABAP Platform**.
  * **SLT add on** : DMIS 2011 SP15 or later, DMIS 2018 SP00 or later, DMIS 2020 or later, or any version of S4CORE.

  
  
###  ECC 

Installation architecture | System | Supported versions | User Interface (UI) Add-On  
---|---|---|---  
Standalone | Source system | 

  * **NetWeaver** 7.0 (with EHP2) or later.  To ensure that the DMIS versions on the source and target systems are compatible, see [SAP Note 2577774](https://launchpad.support.sap.com/#/notes/2577774).  If the DMIS versions are compatible, you can use older versions of ECC. 
  * **SLT add on:** DMIS 2011 SP15 or later, or DMIS 2018 SP00 or later.

|  The SAP_UI component must be compatible with your SAP Netweaver version. **/UI2/CL_JSON** : PL12 or later.  For information about SAP add-on compatibility, see: 

  * [Master Guide for UI Add-On](https://help.sap.com/viewer/05410851eb894cac99df50a874e8a0b4/LATEST/en-US/21b69100cdbe4fd68fc614774eb9c97c.html)
  * [Software Component SAP_UI](https://help.sap.com/doc/saphelp_nw74/LATEST/en-us/35/828457ed26452db8d51c840813f1bb/content.htm?no_cache=true)
  * [SAP Note 2217489 - Maintenance and Update Strategy for SAP Fiori Front-End Server](https://launchpad.support.sap.com/#/notes/2217489)
  * [SAP Note 2211016 - UI add-on 2.0 for SAP NetWeaver: support package stack mapping to SAP_UI 7.50 & UI5 / UI2 versions](https://launchpad.support.sap.com/#/notes/2211016)

  
SAP LT Replication Server system | 

  * **NetWeaver 7.0** (with EHP2) or later.
  * **SLT add on** : DMIS 2011 SP15 or later, or DMIS 2018 SP00 or later.

  
Embedded | Source system | 

  * **NetWeaver 7.0** (with EHP2) or later.
  * **SLT add on** : DMIS 2011 SP15 or later, or DMIS 2018 SP00 or later.

  
  
### Operating system requirements

BigQuery Connector for SAP supports any operating system that is supported by SAP LT Replication Server.

For information about which operating systems SAP LT Replication Server supports, see the [SAP Product Availability Matrix](https://userapps.support.sap.com/sap/support/pam).

### gcloud CLI requirement

BigQuery Connector for SAP requires that the Google Cloud CLI is installed on the SAP LT Replication Server host.

If SAP LT Replication Server is running on Google Cloud and you are using an operating system image that is provided by Compute Engine, the gcloud CLI might be preinstalled for you.

To check which operating system images include the gcloud CLI, see the table for your operating system in [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

To check if the gcloud CLI is installed on an existing SAP LT Replication Server host, log into the server and issue any `gcloud` command. For example:
    
    
    gcloud version

If gcloud CLI is not already installed on your SAP LT Replication Server host, your SAP administrator can install it. For more information about installing the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-on-gc#cloud-sdk).

## Supported replication sources

BigQuery Connector for SAP supports most of the commonly used application and database source systems that are supported by SAP LT Replication Server.

### Supported SAP application sources

You can replicate data from the SAP application sources that SAP LT Replication Server supports.

However, SAP recommends against replicating data from SAP Business Warehouse by using SAP LT Replication Server. For more information from SAP, see [SAP Note 2525755](https://launchpad.support.sap.com/#/notes/2525755).

SAP Cloud applications, such as S/4HANA Cloud, SAP Ariba, SAP SuccessFactors, and others, are not supported.

### Supported data sources

You can replicate only transparent or cluster tables.

BigQuery Connector for SAP does not support the replication SAP Core Data Services (CDS) views. 

## Security

When implementing security for data replication from SAP LT Replication Server to BigQuery, you need to implement security controls in SAP LT Replication Server, the SAP LT Replication Server host operating system, and in Google Cloud.

### SAP security

To control who can configure and work with BigQuery Connector for SAP in SAP LT Replication Server, you use standard SAP role-based authorization.

BigQuery Connector for SAP provides the authorization object `ZGOOG_MTID` as a part of the transport installation.

To configure and run data replication jobs that use the BigQuery Connector for SAP, you can define a role that has administrative access within SAP LT Replication Server, as described in [Create SAP roles and authorizations for BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-on-gc#bqc4sap-define-authorized-sap-roles).

For example, you might define a role called `ZGOOGLE_BIGQUERY_ADMIN` that has all of the SAP authorizations and the `ZGOOG_MTID` authorizations that are required to configure and operate data replication to BigQuery by using the BigQuery Connector for SAP.

For more information from SAP about roles and authorization, see the _Security Guide_ for your version of SAP LT Replication Server in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

### Google Cloud security

Implementing security on Google Cloud for BigQuery Connector for SAP can involve the following security controls:

  * Identity and Access Management (IAM) permissions, roles, service accounts, and keys.
  * BigQuery controls that are set at the dataset or table level.
  * Virtual Private Cloud (VPC) service controls for API-based services like BigQuery.



#### Google Cloud Identity and Access Management

For the authentication and authorization of BigQuery Connector for SAP, you need an IAM service account in the Google Cloud project that contains your BigQuery dataset.

For authorization to interact with BigQuery resources, you grant roles to the service account that contains permissions to interact with BigQuery in the BigQuery project.

If you create the service account in the BigQuery project, you can grant the required roles when you create the service account and the service account becomes a principal in the BigQuery project automatically.

The permissions that BigQuery Connector for SAP needs to access BigQuery are contained in the following IAM roles:

  * **BigQuery Data Editor**
  * **BigQuery Job User**



If SAP LT Replication Server is running on a Compute Engine VM, you also need to grant the **Service Account Token Creator** role to the service account of the host VM.

If SAP LT Replication Server is running on premises or on another cloud platform, in addition to creating a service account, you also need to create a service account key for BigQuery Connector for SAP. Your SAP administrator installs the key on the SAP LT Replication Server host. When the BigQuery Connector for SAP connects to BigQuery, SAP LT Replication Server uses the service account key to authenticate with Google Cloud.

A service account key is not required when SAP LT Replication Server is running on Google Cloud.

For more information about IAM, service accounts, roles, and permissions, see:

  * [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts)
  * [Authenticating as a service account](https://docs.cloud.google.com/docs/authentication/production)
  * [Service account best practices](https://docs.cloud.google.com/iam/docs/understanding-service-accounts)
  * [BigQuery API introduction to authentication](https://docs.cloud.google.com/bigquery/docs/authentication)



#### BigQuery dataset and table access controls

In addition to IAM controls, you can also control access using BigQuery. For BigQuery Connector for SAP, you can set access controls on datasets and tables.

For more information, see:

  * [Controlling access to datasets](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls).
  * [Controlling access to tables](https://docs.cloud.google.com/bigquery/docs/table-access-controls-intro).



#### VPC service controls

On Google Cloud, the VPC firewall rules are not applicable to API-based interactions with BigQuery. Instead, you can use [Virtual Private Cloud (VPC) Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to restrict traffic.

If your SAP workload is running on Google Cloud, you can implement VPC service controls by defining service perimeters. For more information see, [Service perimeters](https://docs.cloud.google.com/bigquery/docs/data-governance#service_perimeters).

If your SAP workload is not running on Google Cloud, you can implement VPC service controls as a part of setting up [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

For more information about network security for BigQuery, see [Network security](https://docs.cloud.google.com/bigquery/docs/data-governance#network_security).

#### More information about Google Cloud security

For more information about security accounts, roles, and permissions, see:

  * [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts)
  * [Creating and enabling service accounts for instances](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)
  * [Overview of data security and governance](https://docs.cloud.google.com/bigquery/docs/data-governance)
    * [BigQuery authentication and authorization](https://docs.cloud.google.com/bigquery/docs/data-governance#authentication_and_authorization)



## Networking

When planning the network path for replication to BigQuery, consider the following points:

  * Bandwidth
  * Latency and its impact on resource consumption on the SAP LT Replication Server host
  * Data volume and its impact on any existing network load
  * If your SAP workload is not running on Google Cloud, which connection type to use: Cloud Interconnect or Cloud VPN



### Connecting to Google Cloud

If your SAP systems are not running on Google Cloud and you do not already have a connection from your SAP systems to Google Cloud, you need to establish a connection and configure private access to the Google Cloud APIs.

You can establish a connection to Google Cloud by using either Cloud Interconnect or Cloud VPN.

Cloud Interconnect typically provides higher bandwidth, lower latency, and lower network contention than Cloud VPN. For high-volume, performance-sensitive replication jobs, Google Cloud recommends Cloud Interconnect for BigQuery Connector for SAP.

With Cloud VPN, your replication data travels over the public internet, so network contention is less predictable and latencies are typically higher.

Regardless of which connection option you choose, you need to review all traffic that you expect the connection to support. Determine whether the connection has sufficient bandwidth and network speed to support the replication jobs and any other workloads without negatively affecting either.

Slow connections can increase resource consumption on both the SAP source server and the SAP LT Replication Server host by extending the time it takes resource jobs to complete, which keeps the resources that are required for replication tied up for longer periods of time.

For more information about your connection options:

  * [Connecting to Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#google-cloud)
  * [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)
  * [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



If you use a proxy server to send the HTTP requests to Google Cloud, then configure the proxy server in SAP transaction `SICF`. For the configuration steps, see the SAP documentation on [Configuring a Proxy](https://help.sap.com/doc/saphelp_nw73/7.3.16/en-US/48/d50d6b982b424be10000000a421937/frameset.htm).

### Bandwidth

Ensure that your network connection between SAP LT Replication Server and BigQuery has enough bandwidth to support your volume of data at the speed you require.

Slower network connections increase the latency of data replication, which increases the resources that replication uses in the source SAP system.

For productive installations, Google Cloud recommends a Cloud Interconnect connection. You can also use Cloud VPN.

### Latency

To reduce latency over your network connection, create your target BigQuery dataset as close to the SAP LT Replication Server system and the SAP source system as possible. If the source SAP system is running on Google Cloud, create your BigQuery dataset in the same Google Cloud region as the source SAP system.

Test your latency before migrating your installation to a production environment.

For more information about network performance, see Network connection performance.

### Network access controls

You can implement network access controls on both sides of the connection between SAP LT Replication Server and Google Cloud.

#### Google Cloud network access controls

BigQuery Connector for SAP communicates with BigQuery through an API endpoint, which is not subject to the Google Cloud VPC firewall rules.

Instead, use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to restrict traffic.

For more information about network security for BigQuery, see [Network security](https://docs.cloud.google.com/bigquery/docs/data-governance#network_security).

#### SAP LT Replication Server host network access controls

On the SAP LT Replication Server host, you need to ensure that any firewalls or proxies allow egress traffic from the server to the BigQuery API endpoint. Specifically, SAP LT Replication Server needs to be able to access the following Google Cloud APIs:

  * https://bigquery.googleapis.com 
  * https://iamcredentials.googleapis.com 



## Performance planning

The performance of initial loads and replication jobs between SAP LT Replication Server and BigQuery is affected by multiple factors at different points along the replication path.

However, certain basic factors, such as the distance between SAP LT Replication Server and your BigQuery dataset or the bandwidth of your connection to Google Cloud, have a greater impact on performance than most other factors.

### General performance best practices

For the best performance, incorporate the following recommendations into your SAP LT Replication Server configuration:

  * Run your SAP workload, including the SAP source system and SAP LT Replication Server, on Google Cloud.
  * If your SAP workload is on Google Cloud, create your BigQuery dataset in the same region as your SAP workload.
  * If you cannot run your SAP workload on Google Cloud: 
    * Create your BigQuery dataset in the Google Cloud region that is closest to your SAP workload.
    * Connect to Google Cloud by using Cloud Interconnect.
  * To avoid contention for resources, use separate dedicated hosts for both the SAP source system and SAP LT Replication Server.
  * Size your SAP LT Replication Server system optimally for your workload according to the _Sizing Guide_ for your version of SAP LT Replication Server in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).
  * Use the following SAP LT Replication Server replication settings: 
    * Parallel jobs.
    * _Reading Type 1_ , if at all possible. For more information, see Performance and the LTRS Advanced Replication Settings.
  * Configure BigQuery Connector for SAP with: 
    * Default record compression.
    * The maximum chunk size.
  * When mapping fields to your BigQuery table, avoid custom names, if possible.



For more information, see:

  * SAP LT Replication Server performance considerations
  * Network connection performance
  * Data transmission
  * Record compression



### Additional characteristics that can affect performance

Many characteristics of your configuration and data can affect performance. Some of these characteristics you might not be able to modify. These characteristics include:

  * On the source server: 
    * The number of CPUs.
    * The amount of memory.
    * The database that is used, such as SAP HANA, SAP ASE, IBM Db2, or others.
    * The number of columns in the source table.
    * The amount of data that each record holds.
    * The table metadata, such as the length of field names.
    * The number of dialog work processes.
  * On the SAP LT Replication Server: 
    * The number of CPUs.
    * The amount of memory.
    * Other workloads that the host might be running.
    * SAP dialog and background work processes.
    * The type of SAP LT Replication Server installation architecture. For more information, see Standalone (recommended) or embedded installation of SAP LT Replication Server.
    * The number of background jobs that are running on the SAP LT Replication Server system.
    * The number of background jobs that are allocated to the mass transfer on the **Administration** tab of the `LTRC` transaction.
    * The `LTRS` transaction performance settings, including **Reading Type** and **Portion Size**.
  * In the BigQuery replication configuration (transaction `/GOOG/SLT_SETTINGS`): 
    * Whether or not custom names are specified for the target fields. The processing of target BigQuery field names can have a slight impact on performance.
    * Whether record compression is enabled.
    * BigQuery Connector for SAP **Chunk Size**, which can affect the total number of HTTP requests sent.



### SAP LT Replication Server performance considerations

The following sections discuss the performance options that are related to the SAP LT Replication Server configuration.

#### Performance and the SAP LT Replication Server installation architecture

A standalone architecture, where SAP LT Replication Server is installed on its own dedicated server, usually provides better performance than an embedded architecture, where SAP LT Replication Server is installed on the same server as the source system.

In an embedded architecture, SAP LT Replication Server must share server resources with the SAP source system.

Even with a standalone architecture, the CPU and memory of the host, as well as any other workloads that might be running on the server, can impact the performance of an SAP LT Replication Server instance.

#### Performance and the `LTRS` Advanced Replication Settings

The performance of initial loads and replication is affected by the settings that you specify for the source table in the `LTRS` transaction under **Advanced Replication Settings**.

For guidance on performance tuning, especially for optimizing high volume initial loads or replication, see the SAP LT Replication Server _Performance Optimization Guide_ in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

Google Cloud recommends the following specifications in the **Advanced Replication Settings** > **General Performance** section of transaction `LTRS`:

For initial loads from most table types, specify **1 Range Calculation** as the **Reading Type**. For tables that are too large for **1 Range Calculation** , specify **Reading Type 5**.

For replications, under **Active Settings** :

  * For the fastest replications, specify **Auto Ranges**.
  * For more reliable replications, specify **No Ranges**.



The following table suggests settings for a few common scenarios.

Table type | Recommended reading type  
---|---  
Transparent (small to medium) | Reading Type 1 - Range Calculation  
Transparent (large) | Only if Reading Type 1 doesn't work, Reading Type 5 - Range Calculation  
Cluster table | Reading Type 4 - Sender Queue  
  
### Network connection performance

The bandwidth and latency of the connection between the SAP LT Replication Server system and BigQuery can affect the overall performance of replication to BigQuery.

The impact affects not only replication speed, but the amount of resources that are consumed by SAP LT Replication Server and the source system, because the longer it takes to receive the confirmation of replication from BigQuery, the longer SAP LT Replication Server and the source system hold the host resources.

If your SAP workload is running on premises or another cloud provider, Google Cloud recommends using a Cloud Interconnect connection, which provides high bandwidth and low latency without having to compete with traffic on the public internet.

You can use Cloud VPN to connect to Google Cloud and BigQuery, however, with a VPN connection, your replications have to compete with general internet traffic.

If your SAP workload is running on Google Cloud, Google Cloud recommends locating SAP LT Replication Server and your BigQuery dataset in the same region. If SAP LT Replication Server and BigQuery are in different regions, latency is typically higher and performance is typically worse. For more information about choosing a region, see [Choosing a region and zone](https://docs.cloud.google.com/compute/docs/regions-zones#choosing_a_region_and_zone).

### Data transmission

Generally, you want to send as much data as possible in each HTTP request so as to reduce the overall number of HTTP requests and the related processing overhead.

In some cases, however, you might need to reduce the amount of data sent, either because of the size of the records in a particular table, or because you are hitting a quota cap or other limit in BigQuery.

You can control the amount of data sent in each request in the following ways:

  * Adjust the amount of data (the _portion_ size) that SAP LT Replication Server sends to BigQuery Connector for SAP.
  * Adjust the amount of data (the _chunk_ size) that BigQuery Connector for SAP sends to BigQuery.
  * Adjust the quotas for streaming inserts in your BigQuery project.



#### Adjusting the amount of data sent by SAP LT Replication Server

SAP LT Replication Server sends records from the source system to the BigQuery Connector for SAP in _portions_. Each portion is handled as a separate load or replication job that consumes server resources until it completes.

Generally, if you increase the SAP LT Replication Server portion size, you decrease the number of SAP LT Replication Server processes, as well as the overhead that is associated with them.

##### Portion size and chunk size

SAP LT Replication Server portions are sized in bytes or as a product of bytes and records. BigQuery Connector for SAP chunks are sized by the number of records that they can contain. The byte size of a chunk varies depending on several factors, including the number of fields in the records and the amount of data each record holds.

If the SAP LT Replication Server portion size is larger than BigQuery Connector for SAP chunk size, then BigQuery Connector for SAP sends multiple chunks for each portion, until all records from the portion are sent.

If the portion size is smaller than the chunk size, then BigQuery Connector for SAP sends only one chunk per portion. Each chunk contains only the number of records sent in each portion, regardless of the chunk size set in BigQuery Connector for SAP.

Ideally, set a portion size in SAP LT Replication Server that allows BigQuery Connector for SAP to create the largest chunks possible without exceeding the BigQuery limit on the number of bytes in each HTTP request.

For more guidance on specifying a chunk size, see Chunk size in BigQuery Connector for SAP.

##### Portion size in the SAP LT Replication Server

To change the default portion size that SAP LT Replication Server uses, run transaction `LTRS` and adjust the value in the **Package Size** field in **Advanced Replication Settings** under **Performance Options**.

For more information, see the SAP LT Replication Server _Performance Optimization Guide_ in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

##### Chunk size in BigQuery Connector for SAP

BigQuery Connector for SAP sends data to BigQuery as _chunks_ of records. We recommend that you use the maximum chunk size that BigQuery Connector for SAP allows, which is 10,000 records. 10,000 records is also the default chunk size that is used by BigQuery Connector for SAP.

If the number of records in a given chunk resolves to a byte size that exceeds the BigQuery limit on the byte size for HTTP requests, you might receive either a `quotaExceeded` error or an `invalid` error.

This can happen if the records in a source table contain a lot of fields or the fields contain a lot of data.

If you get an error related to chunk size, try reducing the chunk size that is specified in the mass transfer configuration for that table.

For SAP source tables like `MSEG`, `ACDOCA`, and `MATDOC`, which can have large records with a lot of fields, you might need to specify a chunk size as low as 2,000.

You can specify a chunk size by running the `/GOOG/SLT_SETTINGS` transaction. The chunk size is specified in the **Chunk Size** field on the table attributes screen.

For more guidance on specifying a chunk size, see:

  * BigQuery Connector for SAP chunk size
  * [Specify table and chunk size attributes](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-on-gc#table-attributes)



For more information about BigQuery error messages, see [Error messages](https://docs.cloud.google.com/bigquery/docs/error-messages).

#### Processing overhead associated with the sending of portions

Each portion that is sent triggers the following actions, each of which incurs some processing overhead or resource consumption:

  1. A collection of changed records in the logging table on the source system are sent to SAP LT Replication Server in a single portion. The changed records are not yet deleted from the logging table.
  2. SAP LT Replication Server requests a new access token from Google Cloud.
  3. BigQuery Connector for SAP sends an HTTP request to BigQuery to check the structure of the target table.
  4. BigQuery Connector for SAP sends the records to BigQuery in as many chunks as are needed to send all of the records that it received in the single portion. Each chunk is sent in a separate HTTP request.
  5. BigQuery processes each chunk that it receives.
  6. An HTTP `OK` status code is returned to SAP LT Replication Server for each chunk.
  7. After BigQuery receives all of the records, SAP LT Replication Server deletes the sent records from the logging table, which finally frees resources on the source system.



For more information about portions and configuring SAP LT Replication Server for performance, see the SAP LT Replication Server _Performance Optimization Guide_ in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

#### BigQuery quotas

BigQuery streaming API quotas that are in effect for your project limit how much data you can stream into BigQuery over time and in any one HTTP request.

For example, BigQuery sets limits on metrics like:

  * The bytes per second per project that you can send.
  * The maximum number of records or rows you can send in a single HTTP request.
  * The maximum size of an HTTP request that you can send.



For streaming inserts, BigQuery fixes the size of HTTP requests to 10 MB and the number of records that you can send in a single HTTP request to 50,000.

In most cases, you can change quotas, but not limits.

You can see and edit the quotas that are in effect for your project in the Google Cloud console on the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page.

For more information about the BigQuery quotas and limits for streaming inserts, see:

  * [Quotas and limits](https://docs.cloud.google.com/bigquery/quotas)
  * [Streaming inserts](https://docs.cloud.google.com/bigquery/quotas#streaming_inserts)



### Record compression

By default, BigQuery Connector for SAP improves replication performance by compressing the records that it sends to BigQuery.

When record compression is enabled, which is the default, BigQuery Connector for SAP omits fields that are empty in the source record from the records that are sent to BigQuery. When the record is inserted into BigQuery, the fields that were omitted from the sent data, are initialized with `null` in the target table.

You can disable record compression by specifying **Send Uncompressed Flag** in the BigQuery table configuration, but doing so can have a negative impact on replication performance.

When the **Send Uncompressed Flag** is selected, BigQuery Connector for SAP sends records to BigQuery with all of their fields, including any empty fields. Except for date fields and timestamp fields, the empty fields retain whatever value they were initialized with in the source table. The initialized value for date and timestamp fields receive the following values:

  * **Date field initialization value:** `DATE 1970-01-01`
  * **Timestamp field initialization value:** `TIMESTAMP 1970-01-01 00:00:00 UTC`



## BigQuery replication configurations

When you configure replication with BigQuery Connector for SAP, you use several different SAP transactions, including a custom transaction that is provided by Google Cloud:

  * `SM30` \- Defines properties for connecting to Google Cloud, which are stored as a record in the custom configuration table `/GOOG/CLIENT_KEY`.
  * `LTRC` \- Defines BigQuery Connector for SAP replication application and mass transfer ID, among other properties
  * `/GOOG/SLT_SETTINGS` \- Defines properties for the target BigQuery dataset, table and fields. When entering `/GOOG/SLT_SETTINGS` in SAP LT Replication Server, you must add `/n` to escape the initial forward slash in the transaction name.



### Language support

BigQuery Connector for SAP version 2.1 only supports replication configurations in English. When you configure replication using the SAP transactions and the custom transaction that is provided by Google Cloud, use **English** as your logon language on the SAP logon screen.

However, BigQuery Connector for SAP supports execution of background jobs that are running on the SAP LT Replication Server in all languages that SAP SLT supports.

Any error messages that you might encounter when working with the BigQuery Connector for SAP are generated in English irrespective of the background job execution language.

### Target table properties

When you configure replication in SAP LT Replication Server by running the `/GOOG/SLT_SETTINGS` transaction, you can specify settings that apply when BigQuery Connector for SAP creates the target table in BigQuery.

For example, you can specify the following properties for a target BigQuery table:

  * Table name
  * The default naming option for fields
  * Extra fields to capture record changes and to enable record count queries
  * Table partitioning



#### Default naming options for fields

You can configure BigQuery Connector for SAP to create the names for the fields in the target BigQuery table either from the names of the source fields or the labels and descriptions of the source fields. The labels and descriptions are usually more informative about the contents of the field.

By default, BigQuery Connector for SAP uses the names of the source fields. You can change the default by specifying the **Custom Names** flag when you specify in table creation attributes in the mass transfer configuration of the `/GOOG/SLT_SETTINGS` transaction. This specification is stored in the `/GOOG/BQ_MASTR` configuration table.

When creating the names, BigQuery Connector for SAP modifies them to conform to the BigQuery naming convention.

Before a table is created, you can edit the field names in the field mapping screen of the `/GOOG/SLT_SETTINGS` transaction.

When the **Custom Names** flag is specified, the names that the BigQuery Connector for SAP connector is going to use when it creates the target table are shown in the **External Field Name** column of the field mapping screen.

BigQuery Connector for SAP creates the names in the **External Field Name** column from the _medium_ field label of each source field. If a medium field label is not specified in the source field definition, then the _short description_ of the field is used. If the short description isn't specified either, then the shortest specified label is used. If nothing is specified, then the name of the source field is used.

For more information about customizing target field names, see Customizing target field names.

#### Capturing record changes and enabling record counts

To capture the type of change in the source table that triggered replication and to be able to query record counts in the BigQuery table for comparison with SAP LT Replication Server or record counts in the source table, specify the **Extra Fields Flag** option in the `/GOOG/SLT_SETTINGS` transaction when you are configuring replication.

When the **Extra Fields Flag** option is specified, the following columns are added to the schema for the target BigQuery table:

Field name | Data type | Description  
---|---|---  
`operation_flag` |  `STRING` |  Identifies the type of change in the source table that triggered the load or replication of the record into BigQuery.  To count records that were inserted in replication mode, query records that have a value of `I`, `U`, or `D` in the `operation_flag` field. For an example query, see [Query the number of records inserted in replication mode](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#query-replicated-records).  To count records that were inserted in initial load mode, query records that have a value of `L` in the `operation_flag` field. For an example query, see [Query the count of records inserted in initial load mode](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#query-loaded-records).   
`is_deleted` |  `BOOLEAN` | When `true`, indicates that the source record was deleted from the source table.  To count only records in a BigQuery table that have not been deleted from the source table, use the `is_deleted` field to exclude deleted source records. For an example query, see [Query the total count of records in a BigQuery table](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#query-total-records).   
`recordstamp` |  `TIMESTAMP` |  The time at which SAP LT Replication Server sent the record to BigQuery.  To count the number of unique records in a BigQuery table, query only the most recently inserted instance of each record. For an example query, see [Query the total count of records in a BigQuery table](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#query-total-records).   
  
The current setting of the **Extra Fields Flag** option is stored in the `/GOOG/BQ_MASTR` configuration table.

For more information about how to specify the **Extra Fields Flag** , see:

  * If SAP LT Replication Server is running on a Compute Engine VM, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-on-gc#configure-connection).
  * If SAP LT Replication Server is running on a host that is external to Google Cloud, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-off-gc#configure-connection).



#### Table partitioning

You can create BigQuery tables that are partitioned by either a timestamp field in the source table, which creates a _time-unit column-partitioned_ table, or by the time at which the records are inserted into BigQuery, which creates an _ingestion-time partitioned_ table.

You enable partitioning by specifying a partition type in the **Partition Type** field in the `/GOOG/BQ_TABLE` when you configure the replication properties.

The partition types that you can specify adjust the granularity of the partitioning by hour, day, month, or year.

To use a timestamp from the source table for time-unit column partitioning, specify the name of the source field in the **Partition Field** field.

To use a BigQuery insertion time for ingestion-time partitioning, you can leave **Partition Field** blank. BigQuery Connector for SAP creates a field in the target table to store the insertion time.

### Target field properties

By default, BigQuery Connector for SAP uses the field names and data types in the SAP source table as the field names and data types in the target BigQuery.

Optionally, before the target table is created, you can customize field names or change the BigQuery data type.

#### Customizing target field names

Before a table is created, you can customize target field names.

If necessary, BigQuery Connector for SAP modifies the custom names that you specify to conform to the BigQuery naming convention.

When you configure replication, you can view the field names in the field mapping screen of the `/GOOG/SLT_SETTINGS` transaction. The BigQuery Connector for SAP stores your settings in the `/GOOG/BQ_FIELD` configuration table.

Before a table is created, you can specify a custom field name by editing the generated name in the **Temporary Field Name** column of the field mapping screen. If you delete a value and leave the **Temporary Field Name** field blank, then BigQuery Connector for SAP uses the name of the source field for the name of that target field.

After making any edits to the **Temporary Field Name** , when you click **Save** , BigQuery Connector for SAP validates the value, applies BigQuery naming conventions as necessary, and save the changes. You can validate a value without saving it by pressing **Enter**.

For information about setting the default naming method for the target fields, see Default naming options for fields.

#### Use a spreadsheet or text file to edit the BigQuery field map

Before you create a target BigQuery table, you can optionally save the default data types, names, and descriptions of the target fields to a spreadsheet or text file, so that BigQuery data engineers or administrators can edit the values easily without requiring access to SAP LT Replication Server.

After the values are edited, you need to convert the file and its contents to the comma-separated values (CSV) format. You can then apply the updates to the mass transfer settings by uploading the CSV file by using the custom transaction `/GOOG/SLT_SETTINGS`.

The process for editing the BigQuery field map by using a CSV file includes the following steps:

  1. Create a spreadsheet or text file of the default field mappings.
  2. Edit the values.
  3. Convert the spreadsheet or text file to CSV format.
  4. Upload the CSV file.



For detailed instructions for each of these steps, see [Edit the BigQuery field map in a CSV file](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#edit-fields-in-csv).

#### BigQuery naming convention for fields

The BigQuery naming convention uses only lowercase letters, numbers, and underscores.

BigQuery Connector for SAP applies the BigQuery naming conventions to any input value to be used for the name of a target field.

For example, if you enter `FIELD-@#!*123` as a custom field name, then the BigQuery Connector for SAP changes the name to `field_123`.

For more information about the BigQuery naming convention for fields, see [Column names](https://docs.cloud.google.com/bigquery/docs/schemas#column_names).

### Data type mapping

By default, BigQuery Connector for SAP assigns data types to the target BigQuery fields based on the _SAP type kind_ or the _SAP data type_ of the source SAP field.

When you configure replication, you can view the data types in the field mapping screen of the `/GOOG/SLT_SETTINGS` transaction. The BigQuery Connector for SAP stores your settings in the `/GOOG/BQ_FIELD` configuration table.

Before a table is created, you can change the default data type specification to a different BigQuery data type in the **External Data Element** column of the field mapping screen.

**Booleans and timestamps:** To accurately reflect the data types of booleans and timestamps in the target table, before the target table is created, you need to manually change their target data types to `BOOLEAN` and `TIMESTAMP`, respectively. For more information, see Data types that require special handling.

#### Data types that require special handling

Several SAP data types require special handling so that they are represented accurately in the target BigQuery table.

Some of these data types you have to handle yourself. The BigQuery Connector for SAP takes care of others for you.

##### Booleans

For booleans, SAP uses the data type `CHAR`, which by default, the BigQuery Connector for SAP maps to the `STRING` data type in the target BigQuery table.

Consequently, for booleans, when you configure replication by using the `/GOOG/SLT_SETTINGS` transaction, you need to change the default data type assignment for boolean fields from `STRING` to `BOOLEAN` in the field mapping screen.

##### Timestamps

For timestamps, SAP uses the data types `P` (packed decimal) or `DEC` (decimal), which by default, BigQuery Connector for SAP maps to `NUMERIC` in the target BigQuery table.

Consequently, for timestamps, when you configure replication by using the `/GOOG/SLT_SETTINGS` transaction, you need to change the default data type assignment for timestamp fields from `NUMERIC` to `TIMESTAMP` or `TIMESTAMP (LONG)` in the field mapping screen.

##### `X` SAP type kind

The `X` SAP type kind is a hexadecimal and is represented by the `RAW`, `RAWSTRING`, or `LRAW` SAP data types. By default, BigQuery Connector for SAP maps these data types to `STRING` in the source BigQuery table.

If you need a source field with the `X` SAP type kind to map to `BYTES` instead, you need to change the default data type assignment for the field in the field mapping screen of the `/GOOG/SLT_SETTINGS` transaction.

The `X` SAP type kind is also sometimes used in SAP to represent integers. In this case, BigQuery Connector for SAP checks the data type of the source field for one of the SAP data types for integers, `INT1`, `INT2`, `INT4`, `INT8` and assigns the `INTEGER` data type in the target BigQuery table.

##### `y` SAP type kind

The `y` SAP type kind is a byte string and is represented by the `RAW`, `RAWSTRING`, or `LRAW` SAP data types. By default, BigQuery Connector for SAP maps these data types to `STRING` in the source BigQuery table.

If you need a source field with the `y` SAP type kind to map to `BYTES` instead, you need to change the default data type assignment for the field in the field mapping screen of the `/GOOG/SLT_SETTINGS` transaction.

#### Default data type mapping

The following table shows the default data type conversion of the BigQuery Connector for SAP:

SAP type kind | SAP data type | BigQuery data type | Notes  
---|---|---|---  
`b` (1 byte integer)  
`s` (2 byte integer)  
`I` (4 byte Integer)  
`8` (8 byte integer)  | `INT1`  
`INT2`  
`INT4`  
`INT8` | `INTEGER` |   
`F` (float)  | `FLTP` | `FLOAT` |   
`P` (packed)  | `CURR`  
`DEC`  
`QUAN` | `NUMERIC` | By default, the SAP type kind `P` is mapped to the BigQuery data type `NUMERIC` and converted to a number in the external format.  
`N` (numeric) | `NUMC` | `STRING` |   
`X` (hexadecimal)  
`y` (byte string)  | `RAW`  
`RAWSTRING`  
`LRAW` | `STRING` | If the SAP type kind is `X`, but the data-type name covers pattern `'INT*'` (`INT1`, `INT2`, `INT4`), a source data element is replaced with a new data element `TYPINT8` with `TYPEKIND '8'`, which is mapped to the BigQuery data type `INTEGER`.  
`C` (character)  
`g` (character string)  
`?` (csequence)  
`&` (clike)  | `CHARSTRING` | `STRING` |   
`D` (date) | `DATS` | `DATE` |   
`T` (time) | `TIMS` | `TIME` |   
  
## Support lifecycle

Google Cloud supports and maintains the current major version of BigQuery Connector for SAP and, for a period of at least 12 months following the publication of a notice of deprecation at [Release Notes page for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/release-notes), the prior major version.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
