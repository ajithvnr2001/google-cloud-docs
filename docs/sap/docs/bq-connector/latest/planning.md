---
url: https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning/
title: BigQuery Connector for SAP planning guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:24.090411+00:00
---

# BigQuery Connector for SAP planning guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  BigQuery Connector for SAP planning guide Stay organized with collections  Save and categorize content based on your preferences. 

description: Plan for replicating SAP data to BigQuery by using the BigQuery Connector for SAP.

This planning guide provides SAP and Google Cloud administrators with the information they need to plan for the replication of SAP data to Google Cloud by using **version 2.15(latest)** of the BigQuery Connector for SAP with SAP LT Replication Server.

This guide covers the following topics:

  * Software requirements
  * Security
  * Networking
  * Performance planning
  * Replication configurations
  * Target table and field properties for BigQuery
  * Target bucket and data conversion properties for Cloud Storage
  * Language support
  * Licensing
  * Support lifecycle



For information about solution accelerators for SAP data modeling in BigQuery, see the [Google Cloud Cortex Framework](https://cloud.google.com/solutions/cortex).

## Software requirements

This section describes the software requirements for BigQuery Connector for SAP.

You can install BigQuery Connector for SAP in SAP LT Replication Server on Google Cloud, on-premises, or on public clouds, such as AWS, Azure, and so forth.

### SAP software version requirements

The required versions of SAP LT Replication Server and the SAP source systems differ depending on whether you install SAP LT Replication Server on its own server in a standalone architecture or within the source ABAP application system in an embedded architecture.

The SAP software requirements are also different depending on the SAP system that you are using as the data source: SAP S/4HANA or SAP ECC.

To see the SAP software versions that Google Cloud supports BigQuery Connector for SAP with, select the tab that corresponds to your SAP source system:

###  S/4HANA 

Installation architecture | System | Supported versions | User Interface (UI) Add-On  
---|---|---|---  
Standalone | Source system | 

  * **NetWeaver 7.5** or later or any version of **ABAP Platform**.  To make sure that the DMIS versions on the source and target systems are compatible, see [SAP Note 2577774](https://launchpad.support.sap.com/#/notes/2577774). 
  * **SLT add on** : DMIS 2011 SP15 or later, DMIS 2018 SP00 or later, DMIS 2020 SP00 or later, DMIS 2025 SP00 or later, or any version of S4CORE.

|  Make sure that the UI Add-On is the most recent version compatible with your SAP NetWeaver version, as recommended by SAP. **/UI2/CL_JSON** : PL12 or later.  For information about the minimum required version of UI Add-On, see the "Support Package" section in the [SAP Note 22798102 - /UI2/CL_JSON corrections - PL12](https://me.sap.com/notes/2798102/E). For information about UI Add-On compatibility with SAP NetWeaver, see: 

  * [Master Guide for UI Add-On](https://help.sap.com/viewer/05410851eb894cac99df50a874e8a0b4/LATEST/en-US/21b69100cdbe4fd68fc614774eb9c97c.html)
  * [Software Component SAP_UI](https://help.sap.com/doc/saphelp_nw74/LATEST/en-us/35/828457ed26452db8d51c840813f1bb/content.htm?no_cache=true)
  * [SAP Note 2217489 - Maintenance and Update Strategy for SAP Fiori Front-End Server](https://launchpad.support.sap.com/#/notes/2217489)
  * [SAP Note 2211016 - UI add-on 2.0 for SAP NetWeaver: support package stack mapping to SAP_UI 7.50 & UI5 / UI2 versions](https://launchpad.support.sap.com/#/notes/2211016)

  
SAP LT Replication Server system | 

  * **NetWeaver** 7.0 (with EHP2) or later or any version of **ABAP Platform**.
  * **SLT add on** : DMIS 2011 SP15 or later, DMIS 2018 SP00 or later, DMIS 2020 SP00 or later, or DMIS 2025 SP00 or later.

  
Embedded | Source system | 

  * **NetWeaver 7.5** or later or any version of **ABAP Platform**.
  * **SLT add on** : DMIS 2011 SP15 or later, DMIS 2018 SP00 or later, DMIS 2020 SP00 or later, DMIS 2025 SP00 or later, or any version of S4CORE.

  
  
###  ECC 

Installation architecture | System | Supported versions | User Interface (UI) Add-On  
---|---|---|---  
Standalone | Source system | 

  * **NetWeaver** 7.0 (with EHP2) or later.  To make sure that the DMIS versions on the source and target systems are compatible, see [SAP Note 2577774](https://launchpad.support.sap.com/#/notes/2577774).  If the DMIS versions are compatible, then you can use earlier versions of ECC. 
  * **SLT add on:** DMIS 2011 SP15 or later, or DMIS 2018 SP00 or later.

|  Make sure that the UI Add-On is the most recent version compatible with your SAP NetWeaver version, as recommended by SAP.  **/UI2/CL_JSON** : PL12 or later.  For information about the minimum required version of UI Add-On, see the "Support Package" section in the [SAP Note 22798102 - /UI2/CL_JSON corrections - PL12](https://me.sap.com/notes/2798102/E). For information about UI Add-On compatibility with SAP NetWeaver, see: 

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

### Cloud Billing account requirement

Although BigQuery Connector for SAP is offered at no cost, you do need a [Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account) to receive the installation package.

### Scalability

For very large volumes, such as billions of data records with millions of deltas, BigQuery Connector for SAP uses SAP LT Replication Server scaling and partitioning functions to parallelize the data extraction at scale. For more information, see the _Sizing Guide_ for your version of SAP LT Replication Server in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

On the Google Cloud side, depending on your replication path, the BigQuery Connector for SAP uses different Google Cloud services to scale data loading:

  * For CDC replication through Pub/Sub to BigQuery, BigQuery Connector for SAP uses the [Pub/Sub API](https://docs.cloud.google.com/pubsub/docs/reference/rest) and the [Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api).
  * For streaming data replication to BigQuery, BigQuery Connector for SAP uses the [BigQuery streaming API](https://docs.cloud.google.com/bigquery/streaming-data-into-bigquery).
  * For file-based replication to Cloud Storage, BigQuery Connector for SAP uses the [Cloud Storage JSON API](https://docs.cloud.google.com/storage/docs/json_api).



## Supported replication sources

BigQuery Connector for SAP supports most of the commonly used application and database source systems that are supported by SAP LT Replication Server.

### Supported SAP application sources

You can replicate data from the SAP application sources that SAP LT Replication Server supports. BigQuery Connector for SAP supports the major in-maintenance enterprise application versions as data sources, as well as earlier legacy applications. Some of the supported SAP applications include:

  * SAP Business Suite 7
  * S/4HANA
  * SAP applications running on SAP NetWeaver



For replicating data from SAP Business Warehouse, SAP recommends against using SAP LT Replication Server. For more information from SAP, see [SAP Note 2525755](https://launchpad.support.sap.com/#/notes/2525755).

SAP Cloud applications, such as S/4HANA Cloud, SAP Ariba, SAP SuccessFactors, and others, are not supported.

### Supported data sources

You can replicate only transparent or cluster tables.

BigQuery Connector for SAP does not support the replication SAP Core Data Services (CDS) views. 

In the Information Design Tool, BigQuery is supported starting from SAP BusinessObjects Business Intelligence 4.3 as data source. You can query stored data on BigQuery from the SAP BusinessObjects reporting tools such as SAP BusinessObjects Web Intelligence and SAP Crystal Reports for Enterprise among others.

For more information about the compatibility check SAP Note [2750723 - Support of Google BigQuery in SAP BI platform products](https://me.sap.com/notes/0002750723).

## Security

When implementing security for data replication from SAP LT Replication Server to Google Cloud, you need to implement security controls in SAP LT Replication Server, the SAP LT Replication Server host operating system, and in Google Cloud.

For communication between BigQuery Connector for SAP and Google Cloud, BigQuery Connector for SAP uses end-to-end HTTPS communication and SSL.

### SAP security

To control who can configure and work with BigQuery Connector for SAP in SAP LT Replication Server, you use standard SAP role-based authorization.

BigQuery Connector for SAP provides the authorization object `ZGOOG_MTID` as a part of the transport installation.

To configure and run data replication jobs that use the BigQuery Connector for SAP, you can define a role that has administrative access within SAP LT Replication Server, as described in [Create SAP roles and authorizations for BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api#bqc4sap-define-authorized-sap-roles).

For example, you might define a role called `ZGOOGLE_BIGQUERY_ADMIN` that has all of the SAP authorizations and the `ZGOOG_MTID` authorizations that are required to configure and operate data replication to BigQuery by using the BigQuery Connector for SAP.

For more information from SAP about roles and authorization, see the _Security Guide_ for your version of SAP LT Replication Server in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

### Google Cloud security

Implementing security on Google Cloud for BigQuery Connector for SAP can involve the following security controls:

  * Identity and Access Management (IAM) permissions, roles, service accounts, and keys.
  * BigQuery controls that are set at the dataset or table level.
  * Virtual Private Cloud (VPC) service controls for API-based services like BigQuery.
  * Private Service Connect endpoints that allow private consumption of services, like BigQuery, across VPC networks.



#### Google Cloud Identity and Access Management

For the authentication and authorization of BigQuery Connector for SAP, you need an IAM service account in the Google Cloud project that contains your BigQuery dataset or Cloud Storage bucket.

For authorization to interact with Google Cloud resources, you grant roles to the service account that contains permissions to interact with BigQuery, Pub/Sub, and Cloud Storage services.

For streaming data replication to BigQuery (insert-only), the permissions that BigQuery Connector for SAP needs to access BigQuery are contained in the following IAM roles:

  * [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor)
  * [BigQuery Job User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser)



For CDC replication to BigQuery through Pub/Sub, the permissions that BigQuery Connector for SAP needs to access Pub/Sub and BigQuery are contained in the following IAM roles:

  * [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor)
  * [BigQuery Job User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser)
  * [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor)



For CDC replication through Pub/Sub, you also need to grant the following IAM roles to the Pub/Sub service agent:

  * [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor)
  * [Pub/Sub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher)
  * [Pub/Sub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.subscriber)



For file-based replication to Cloud Storage, the permissions that BigQuery Connector for SAP needs to access Cloud Storage are contained in the following IAM roles:

  * [Storage Object Creator](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles)
  * [Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles)



If SAP LT Replication Server is running on a Compute Engine VM, you also need to grant the **Service Account Token Creator** role to the service account of the host VM.

If SAP LT Replication Server is running on premises or on another cloud platform, in addition to creating a service account, you also need to create a service account key for BigQuery Connector for SAP. Your SAP administrator installs the key on the SAP LT Replication Server host. When the BigQuery Connector for SAP connects to Pub/Sub, BigQuery, or Cloud Storage, SAP LT Replication Server uses the service account key to authenticate with Google Cloud.

A service account key is not required when SAP LT Replication Server is running on Google Cloud.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

For more information about IAM, service accounts, roles, and permissions, see:

  * [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts)
  * [Authenticating as a service account](https://docs.cloud.google.com/docs/authentication/production)
  * [Best practices for using service accounts securely](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)
  * [BigQuery authentication and authorization](https://docs.cloud.google.com/bigquery/docs/authentication)



#### BigQuery dataset and table access controls

For replication to BigQuery, in addition to IAM controls, you can also control access using BigQuery. For BigQuery Connector for SAP, you can set access controls on datasets and tables.

For more information, see:

  * [Controlling access to datasets](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls).
  * [Controlling access to tables](https://docs.cloud.google.com/bigquery/docs/table-access-controls-intro).



#### VPC service controls

On Google Cloud, the VPC firewall rules are not applicable to API-based interactions with BigQuery. Instead, you can use [Virtual Private Cloud (VPC) Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to restrict traffic.

If your SAP workload is running on Google Cloud, you can implement VPC service controls by defining service perimeters. For more information see, [Service perimeters](https://docs.cloud.google.com/bigquery/docs/data-governance#service_perimeters).

If your SAP workload is not running on Google Cloud, you can implement VPC service controls as a part of setting up [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

For more information about network security for BigQuery, see [Network security](https://docs.cloud.google.com/bigquery/docs/data-governance#network_security).

#### Private Service Connect endpoints

If you want to set up endpoints in your VPC network that allow private consumption of Google-managed services like BigQuery, then you can use Private Service Connect.

Private Service Connect lets you create private endpoints that use internal IP addresses from a VPC CIDR range to access Google APIs and services. You can also use Private Service Connect to create a custom private DNS name for the BigQuery streaming API. For more information, see [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).

For the BigQuery Connector for SAP that is running on a host outside of Google Cloud, Private Service Connect is not supported.

#### More information about Google Cloud security

For more information about security accounts, roles, and permissions, see:

  * [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts)
  * [Creating and enabling service accounts for instances](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)
  * [Overview of data security and governance](https://docs.cloud.google.com/bigquery/docs/data-governance)
  * [BigQuery authentication and authorization](https://docs.cloud.google.com/bigquery/docs/data-governance#authentication_and_authorization)



## Networking

When planning the network path for replication to Google Cloud, consider the following points:

  * Bandwidth
  * Latency and its impact on resource consumption on the SAP LT Replication Server host
  * Data volume and its impact on any existing network load
  * If your SAP workload is not running on Google Cloud, which connection type to use: Cloud Interconnect or Cloud VPN



### Connecting to Google Cloud

If your SAP systems are not running on Google Cloud and you don't already have a connection from your SAP systems to Google Cloud, you need to establish a connection and configure private access to the Google Cloud APIs.

You can establish a connection to Google Cloud by using either Cloud Interconnect or Cloud VPN.

Cloud Interconnect typically provides higher bandwidth, lower latency, and lower network contention than Cloud VPN. For high-volume, performance-sensitive replication jobs, Google Cloud recommends Cloud Interconnect for BigQuery Connector for SAP.

With Cloud VPN, your replication data travels over the public internet, so network contention is less predictable and latencies are typically higher.

Regardless of which connection option you choose, you need to review all traffic that you expect the connection to support. Determine whether the connection has sufficient bandwidth and network speed to support the replication jobs and any other workloads without negatively affecting either.

Slow connections can increase resource consumption on both the SAP source server and the SAP LT Replication Server host by extending the time it takes resource jobs to complete, which keeps the resources that are required for replication tied up for longer periods of time.

For more information about your connection options, see the following:

  * [Connecting to Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#google-cloud)
  * [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)
  * [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



To use a proxy server to send the HTTP requests to Google Cloud, we recommend that you use RFC destinations defined in transaction `SM59`.

#### RFC destinations

The transport files of the BigQuery Connector for SAP contain the following sample RFC destinations in transaction `SM59`. These RFC destinations are HTTP connections to External Servers (Type `G`) and connect to the respective service's public API endpoint.

Sample RFC destination name | Target host (API endpoint) | Path prefix | Notes  
---|---|---|---  
`GOOG_BIGQUERY` | `https://bigquery.googleapis.com` | `/bigquery/v2/` | This RFC destination targets the BigQuery API.  
`GOOG_PUBSUB` | `https://pubsub.googleapis.com` | `/` | This RFC destination targets the Pub/Sub API. To avoid inter-region data transfer costs, we recommend that you create an RFC destination for the [regional Pub/Sub endpoint](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#list_regional_endpoints) where your SAP system and BigQuery dataset are located.  
`GOOG_STORAGE` | `https://storage.googleapis.com` | `/v1/` | This RFC destination targets the Cloud Storage JSON API.  
`GOOG_IAMCREDENTIALS` | `https://iamcredentials.googleapis.com` | `/v1/` | This RFC destination targets the IAM API.  
`GOOG_OAUTH2_TOKEN` | `https://googleapis.com/oauth2` | `/oauth2/v4/token` | This RFC destination targets Google Cloud endpoint for OAuth 2.0 based authentication. You use this for SAP workloads that are running outside of Google Cloud and only when you want to authenticate to Google Cloud using JSON Web Token (JWT).  
**Note:** We recommend that you use these sample RFC destinations as templates and don't modify them because importing new transport for the BigQuery Connector for SAP overwrites these sample destinations. You can copy these samples to create your own custom RFC destinations.

Using RFC destinations to connect to Google Cloud offers the following advantages:

  * If you use a proxy server in your SAP landscape and want to use the same to send the HTTP requests to Google Cloud, then you can configure the proxy server in the RFC destination.

  * If you want to enable access to Google Cloud APIs and services through [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoints, then you can create those endpoints in your Google Cloud project and then specify the endpoints in your RFC destinations.

  * You can use HTTP compression, which Google Cloud recommends for cross-region replications, where your SAP source system and BigQuery dataset are placed in different Compute Engine regions.




To use RFC destinations to connect to Google Cloud APIs or services, you need to create entries in the `/GOOG/SERVIC_MAP` table that map the RFC destinations to the Google service and client key. For configuration steps, see [JWT: Configure RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt#configure_rfc_destinations) or [Access tokens: Configure RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-access-token#configure_rfc_destinations).

#### HTTP compression

When you use RFC destinations to set up the connection between BigQuery Connector for SAP and Google Cloud APIs, you can use the _Compression_ option to compress the HTTP request body. HTTP compression is available only when you configure your RFC destinations to use `HTTP 1.1`.

**Note:** We recommend that you use HTTP compression only for cross-region data replications, where your BigQuery dataset and SAP source system are placed in different Compute Engine regions.

Before you enable HTTP compression in your production environment, analyze the profile parameters that impact HTTP compression in a test environment. For more information from SAP, see [SAP Note 1037677 - HTTP compression compresses certain documents only](https://launchpad.support.sap.com/#/notes/1037677).

### Bandwidth

Make sure that your network connection between SAP LT Replication Server and Google Cloud has enough bandwidth to support your volume of data at the speed you require.

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

On the SAP LT Replication Server host, you need to make sure that any firewalls or proxies allow egress traffic from the server to the BigQuery and Pub/Sub API endpoints. Specifically, make sure that your SAP LT Replication Server can access the following Google Cloud APIs:

  * `https://bigquery.googleapis.com`
  * `https://pubsub.googleapis.com`
  * `https://iamcredentials.googleapis.com`
  * `https://storage.googleapis.com`



If you want to use Private Service Connect endpoints to access the BigQuery, Pub/Sub, and Cloud Storage APIs, then you must configure the Private Service Connect endpoints in the table `/GOOG/SERVIC_MAP`.

## Performance planning

The guidance in this section applies only to replicating SAP data to BigQuery by using the BigQuery Connector for SAP.

For replication to Cloud Storage, the connector offers delivery of JSON files to Cloud Storage. Because this replication path is decoupled from BigQuery, loading data into BigQuery is a separate step. Consequently, your end-to-end replication performance is driven by the custom ingestion tools and configuration that you use for your post-Cloud Storage pipeline.

For replication to BigQuery, the performance of initial loads and replication jobs between SAP LT Replication Server and BigQuery is affected by multiple factors at different points along the replication path.

However, certain basic factors, such as the distance between SAP LT Replication Server and your BigQuery dataset or the bandwidth of your connection to Google Cloud, have a greater impact on performance than most other factors.

### General performance best practices

For the best performance, incorporate the following recommendations into your SAP LT Replication Server configuration:

  * Run your SAP workload, including the SAP source system and SAP LT Replication Server, on Google Cloud.
  * If your SAP workload is on Google Cloud, create your BigQuery dataset in the same region as your SAP workload.
  * For CDC replication through Pub/Sub, use a regional Pub/Sub endpoint to keep traffic within the same region.
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
    * Default chunk size.
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
    * Chunk size, which can affect the total number of HTTP requests sent.



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

The bandwidth and latency of the connection between the SAP LT Replication Server system and Google Cloud can affect the overall performance of replication to Google Cloud.

The impact affects not only replication speed, but the amount of resources that are consumed by SAP LT Replication Server and the source system, because the longer it takes to receive the confirmation of replication from Google Cloud, the longer SAP LT Replication Server and the source system hold the host resources.

If your SAP workload is running on-premises or another cloud provider, Google Cloud recommends using a Cloud Interconnect connection, which provides high bandwidth and low latency without having to compete with traffic on the public internet.

You can use Cloud VPN to connect to Google Cloud and BigQuery, however, with a VPN connection, your replications have to compete with general internet traffic.

If your SAP workload is running on Google Cloud, Google Cloud recommends locating SAP LT Replication Server and your BigQuery dataset in the same region. If SAP LT Replication Server and BigQuery are in different regions, latency is typically higher and performance is typically worse. For more information about choosing a region, see [Choosing a region and zone](https://docs.cloud.google.com/compute/docs/regions-zones#choosing_a_region_and_zone).

### Data transmission

Generally, you want to send as much data as possible in each HTTP request so as to reduce the overall number of HTTP requests and the related processing overhead.

In some cases, however, you might need to reduce the amount of data sent, either because of the size of the records in a particular table, or because you are hitting a quota cap or other limit in Pub/Sub or BigQuery.

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

Ideally, set a portion size in SAP LT Replication Server that allows BigQuery Connector for SAP to create the largest chunks possible without exceeding the Pub/Sub or BigQuery limit on the number of bytes in each HTTP request.

For more guidance on specifying a chunk size, see Chunk size in BigQuery Connector for SAP.

##### Portion size in the SAP LT Replication Server

To change the default portion size that SAP LT Replication Server uses, run transaction `LTRS` and adjust the value in the **Package Size** field in **Advanced Replication Settings** under **Performance Options**.

For more information, see the SAP LT Replication Server _Performance Optimization Guide_ in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

##### Chunk size in BigQuery Connector for SAP

BigQuery Connector for SAP sends data to BigQuery as _chunks_ of records.

For CDC replication through Pub/Sub to BigQuery, we recommend that you use the default chunk size with BigQuery Connector for SAP, which is 1,000 records. This is the maximum number of records that Pub/Sub allows.

For streaming data replication to BigQuery, we recommend that you use the default chunk size with BigQuery Connector for SAP, which is 10,000 records. However, if the records in a source table contain very few fields or the fields contain very small size data values, then you can use a larger chunk size up to the maximum chunk size that BigQuery allows, which is 50,000 records.

For file-based replication to Cloud Storage, we recommend that you use the default chunk size with BigQuery Connector for SAP, which is 50,000 records.

If the number of records in a given chunk resolves to a byte size that exceeds the allowed limit on the byte size for HTTP requests, you might receive either a `quotaExceeded` error or an `invalid` error.

This can happen if the records in a source table contain a lot of fields or the fields contain a lot of data.

If you get an error related to chunk size, try reducing the chunk size that is specified in the mass transfer configuration for that table. Alternatively, you can enable dynamic chunk size for that table to automatically adjust the chunk size. For more information, see [Dynamic chunk size](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#dynamic-chunk-size).

If you have not enabled dynamic chunk size, then for SAP source tables like `MSEG`, `ACDOCA`, and `MATDOC`, which can have large records with a lot of fields per record, you might need to specify a lower chunk size.

You can specify a chunk size by running the `/GOOG/SLT_SETTINGS` transaction. The chunk size is specified in the **Chunk Size** field on the table attributes screen.

For more guidance on specifying a chunk size, see:

  * For CDC replication to BigQuery through Pub/Sub, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api#configure-connection).
  * For streaming data replication to BigQuery, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#configure-connection).
  * For file-based replication to Cloud Storage, see [Specify table attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-gcs-file-replication#table-attributes).



For more information about BigQuery error messages, see [Error messages](https://docs.cloud.google.com/bigquery/docs/error-messages).

#### Processing overhead associated with the sending of portions

Each portion that is sent triggers the following actions, each of which incurs some processing overhead or resource consumption:

  1. A collection of changed records in the logging table on the source system are sent to SAP LT Replication Server in a single portion. The changed records are not yet deleted from the logging table.
  2. SAP LT Replication Server requests a new access token from Google Cloud.
  3. BigQuery Connector for SAP sends an HTTP request to Google Cloud to check the structure of the target table.
  4. BigQuery Connector for SAP sends the records to Google Cloud in as many chunks as are needed to send all of the records that it received in the single portion. Each chunk is sent in a separate HTTP request.
  5. Google Cloud processes each chunk that it receives.
  6. An HTTP `OK` status code is returned to SAP LT Replication Server for each chunk.
  7. After Google Cloud receives all of the records, SAP LT Replication Server deletes the sent records from the logging table, which finally frees resources on the source system.



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



#### Pub/Sub quotas

Pub/Sub API quotas that are in effect for your project limit how much data you can stream into BigQuery over time and in any one HTTP request.

For example, Pub/Sub sets limits on metrics like:

  * The bytes per second per project that you can send.
  * The maximum number of records or rows you can send in a single HTTP request.
  * The maximum size of an HTTP request that you can send.



For CDC data, Pub/Sub fixes the size of HTTP requests to 10 MB and the number of records that you can send in a single HTTP request to 1,000.

In most cases, you can change quotas, but not limits.

You can see and edit the quotas that are in effect for your project in the Google Cloud console on the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page.

For more information about the Pub/Sub quotas and resource limits, see:

  * [Quotas and limits](https://docs.cloud.google.com/pubsub/quotas)
  * [Resource limits](https://docs.cloud.google.com/pubsub/quotas#resource_limits)



#### Cloud Storage quotas

Cloud Storage quotas that are in effect for your project can impact file-based replication.

For example, Cloud Storage sets limits on metrics like:

  * The maximum size of an object.
  * The number of object uploads per second per bucket.



For Cloud Storage, the maximum object size is 5 TiB. If your file size exceeds 5TiB, then the upload fails.

In most cases, you can change quotas, but not limits.

You can see and edit the quotas that are in effect for your project in the Google Cloud console on the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page.

For more information about the Cloud Storage quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/storage/quotas).

### Record compression

For CDC replication to BigQuery through Pub/Sub and file-based replication to Cloud Storage, the record compression feature is not supported.

For streaming data replication to BigQuery, by default, BigQuery Connector for SAP improves replication performance by compressing the records that it sends to BigQuery. From version 2.8 and later of BigQuery Connector for SAP, the record compression option is available at the table level and as well as the field level.

When record compression is enabled at table level, which is the default setting, BigQuery Connector for SAP omits all fields that are empty in the source record from the records that are sent to BigQuery. When the record is inserted into BigQuery, the fields that were omitted from the sent data, are initialized with `null` in the target table in BigQuery.

However, if you need to replicate some empty fields with their initial values to BigQuery while still using record compression at the table level, then you can change the record compression setting for those specific fields. This means that the empty values in the specified fields are not omitted from the sent data, and retain whatever value they are initialized in the source table.

You can control the record compression behavior by using the **Send Uncompressed Flag** setting available at the table level and field level. The following table summarizes the record compression behavior:

Send Uncompressed Flag at table level | Send Uncompressed Flag at field level | Record compression behavior  
---|---|---  
Yes | No | All fields are sent as uncompressed.  
Yes | Yes | All fields are sent as uncompressed.  
No | Yes | Only the selected fields at the field level are sent as uncompressed.  
No | No | All fields are sent as compressed.  
  
When the uncompressed data is sent for replication, except for date fields and timestamp fields, the empty fields retain whatever value they were initialized with in the source table. The initialized value for date and timestamp fields receive the following values:

  * **Date field initialization value:** `DATE 1970-01-01`
  * **Timestamp field initialization value:** `TIMESTAMP 1970-01-01 00:00:00 UTC`



The following screenshot shows an example of the record compression behavior:

  * **Row #1** : All fields are uncompressed. The **Send Uncompressed Flag** is selected at table level.
  * **Row #2** : All fields are compressed. The **Send Uncompressed Flag** is clear at table level.
  * **Row #3** : The following fields are uncompressed: `int2_value`, `curr_value_154`, `currency`, `float_value`, and `lang_value`. For these fields, **Send Uncompressed Flag** is selected at field level.



![Diagram is described in the preceding text](https://docs.cloud.google.com/static/sap/docs/images/record-compression-example.png)

For better performance, don't disable record compression by selecting **Send Uncompressed Flag** at the table level. It can have a negative impact on replication performance. If you need to send uncompressed data for only specific fields, then select **Send Uncompressed Flag** for those specific fields at the field level. For more information on how record compression affects your data that is transferred from SAP LT Replication Server to BigQuery, see [Understanding BigQuery Connector for SAP Compression Feature](https://medium.com/google-cloud/understanding-bigquery-connector-for-saps-compression-feature-969a438c668d).

### Data transfer costs and regional Pub/Sub endpoints

To avoid inter-region data transfer costs for CDC replication through Pub/Sub, explicitly configure the BigQuery Connector for SAP to use a regional Pub/Sub endpoint.

By default, the connector uses the global Pub/Sub endpoint. This means that your data might route through a different Google Cloud region before reaching your BigQuery dataset, resulting in significant costs even when your SAP system and BigQuery dataset are in the same region. Using a regional endpoint ensures that your data is processed in the same region as your SAP and BigQuery resources, which can also improve replication performance.

For a list of available Pub/Sub regional endpoints, see [List of regional endpoints](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#list_regional_endpoints).

For information about Pub/Sub data transfer pricing, see [Data transfer costs](https://cloud.google.com/pubsub/pricing#egress_costs).

To use a regional Pub/Sub endpoint, do the following:

  1. In transaction `SM59`, create a new RFC destination for the regional Pub/Sub endpoint of your choice. For more information, see [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations).
  2. In the service mapping table `/GOOG/SERVIC_MAP`, create an entry that maps the `pubsub:v1` service to the new RFC destination.



## Replication configurations

When you configure replication with BigQuery Connector for SAP, you use several different SAP transactions, including a custom transaction that is provided by Google Cloud:

  * `SM30` \- Defines properties for connecting to Google Cloud, which are stored as a record in the custom configuration table `/GOOG/CLIENT_KEY`. Optionally, when you use RFC destinations to connect to Google Cloud APIs and services, some connection properties are stored in the custom configuration table `/GOOG/SERVIC_MAP`.
  * `LTRC` \- Defines BigQuery Connector for SAP replication application and mass transfer ID, among other properties.
  * `SM59` \- Defines RFC destinations that enable connecting to Google Cloud APIs and services like BigQuery and IAM.
  * `/GOOG/SLT_SETTINGS` \- Defines properties for the target BigQuery dataset, table, and fields, or Cloud Storage bucket. When entering `/GOOG/SLT_SETTINGS` in SAP LT Replication Server, you must add `/n` to escape the initial forward slash in the transaction name.



## Target table and field properties for BigQuery

When you configure replication in transaction `/GOOG/SLT_SETTINGS`, you can define configurations for target tables in BigQuery, which include settings for tables, fields, and data type mapping.

### Table properties

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

When the **Custom Names** flag is specified, the names that the BigQuery Connector for SAP connector is going to use when it creates the target table are shown in the **External Field Name** column of the field definitions screen.

BigQuery Connector for SAP creates the names in the **External Field Name** column from the _medium_ field label of each source field. If a medium field label is not specified in the source field definition, then the _short description_ of the field is used. If the short description isn't specified either, then the shortest specified label is used. If nothing is specified, then the name of the source field is used.

For more information about customizing target field names, see Customizing target field names.

#### Capturing record changes and enabling record counts

To capture the type of change in the source table that triggered replication and to be able to query record counts in the BigQuery table for comparison with SAP LT Replication Server or record counts in the source table, specify the **Extra Fields Flag** option in the `/GOOG/SLT_SETTINGS` transaction when you are configuring replication.

When the **Extra Fields Flag** option is specified, the following columns are added to the schema for the target BigQuery table:

Field name | Data type | Description  
---|---|---  
`operation_flag` |  `STRING` |  Identifies the type of change in the source table that triggered the load or replication of the record into BigQuery.  To count records that were inserted in replication mode, query records that have a value of `I`, `U`, or `D` in the `operation_flag` field. For an example query, see [Query the number of records inserted in replication mode](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#query-replicated-records).  To count records that were inserted in initial load mode, query records that have a value of `L` in the `operation_flag` field. For an example query, see [Query the count of records inserted in initial load mode](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#query-loaded-records).   
`is_deleted` |  `BOOLEAN` | When `true`, indicates that the source record was deleted from the source table.  To count only records in a BigQuery table that have not been deleted from the source table, use the `is_deleted` field to exclude deleted source records. For an example query, see [Query the total count of records in a BigQuery table](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#query-total-records).   
`recordstamp` |  `TIMESTAMP` |  The time at which SAP LT Replication Server sent the record to BigQuery.  To count the number of unique records in a BigQuery table, query only the most recently inserted instance of each record. For an example query, see [Query the total count of records in a BigQuery table](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#query-total-records).   
  
The current setting of the **Extra Fields Flag** option is stored in the `/GOOG/BQ_MASTR` configuration table.

For more information about how to specify the **Extra Fields Flag** , see:

  * For CDC replication through Pub/Sub to BigQuery, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api#configure-connection).
  * For streaming data replication to BigQuery, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#configure-connection).



#### Table partitioning

You can create BigQuery tables that are partitioned by either a timestamp field in the source table, which creates a _time-unit column-partitioned_ table, or by the time at which the records are inserted into BigQuery, which creates an _ingestion-time partitioned_ table.

You enable partitioning by specifying a partition type in the **Partition Type** field in the `/GOOG/BQ_TABLE` when you configure the replication properties.

The partition types that you can specify adjust the granularity of the partitioning by hour, day, month, or year.

To use a timestamp from the source table for time-unit column partitioning, specify the name of the source field in the **Partition Field** field.

To use a BigQuery insertion time for ingestion-time partitioning, you can leave **Partition Field** blank. BigQuery Connector for SAP creates a field in the target table to store the insertion time.

### Field properties

By default, BigQuery Connector for SAP uses the field names and data types in the SAP source table as the field names and data types in the target BigQuery.

Optionally, before the target table is created, you can customize field names or change the BigQuery data type.

#### Customizing target field names

Before a table is created, you can customize target field names.

If necessary, BigQuery Connector for SAP modifies the custom names that you specify to conform to the BigQuery naming convention.

When you configure replication, you can view the field names in the field mapping screen of the `/GOOG/SLT_SETTINGS` transaction. The BigQuery Connector for SAP stores your settings in the `/GOOG/BQ_FIELD` configuration table.

Before a table is created, you can specify a custom field name by editing the generated name in the **Temporary Field Name** column of the field definitions screen. If you delete a value and leave the **Temporary Field Name** field blank, then BigQuery Connector for SAP uses the name of the source field for the name of that target field.

After making any edits to the **Temporary Field Name** , when you click **Save** , BigQuery Connector for SAP validates the value, applies BigQuery naming conventions as necessary, and saves the changes. You can validate a value without saving it by pressing **Enter**.

For information about setting the default naming method for the target fields, see Default naming options for fields.

#### Use a spreadsheet or text file to edit the BigQuery field definition

Before you create a target BigQuery table, you can optionally save the default data types, names, and descriptions of the target fields to a spreadsheet or text file, so that BigQuery data engineers or administrators can edit the values without requiring access to SAP LT Replication Server.

After the values are edited, you need to convert the file and its contents to the comma-separated values (CSV) format. You can then apply the updates to the mass transfer settings by uploading the CSV file by using the custom transaction `/GOOG/SLT_SETTINGS`.

The process for editing the BigQuery field map by using a CSV file includes the following steps:

  1. Create a spreadsheet or text file of the default field definitions.
  2. Edit the values.
  3. Convert the spreadsheet or text file to CSV format.
  4. Upload the CSV file.



For detailed instructions for each of these steps, see [Edit field definitions in a CSV file](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#edit-field-definitions-in-csv).

#### BigQuery naming convention for fields

The BigQuery naming convention uses only lowercase letters, numbers, and underscores.

BigQuery Connector for SAP applies the BigQuery naming conventions to any input value to be used for the name of a target field.

For example, if you enter `FIELD-@#!*123` as a custom field name, then the BigQuery Connector for SAP changes the name to `field_123`.

For more information about the BigQuery naming convention for fields, see [Column names](https://docs.cloud.google.com/bigquery/docs/schemas#column_names).

### Data type mapping

By default, BigQuery Connector for SAP assigns data types to the target BigQuery fields based on the _SAP type kind_ or the _SAP data type_ of the source SAP field.

For CDC replication through Pub/Sub to BigQuery, the process involves an intermediate step in data type mapping:

  1. BigQuery Connector for SAP to Pub/Sub: When BigQuery Connector for SAP sends data to a Pub/Sub topic, SAP data types are initially converted to Pub/Sub Avro data types.

  2. Pub/Sub to BigQuery: The Pub/Sub Avro-formatted data is then streamed to BigQuery using a BigQuery subscription. At this point, Pub/Sub assigns the final BigQuery data types.




To ensure smooth data flow and accurate interpretation, the Pub/Sub Avro data types and the final BigQuery data types must be compatible. For information about schema compatibility between a Pub/Sub topic and a BigQuery table, see [Schema compatibility](https://docs.cloud.google.com/pubsub/docs/bigquery#schema_compatibility).

When you configure replication, you can view the data types in the field mapping screen of the `/GOOG/SLT_SETTINGS` transaction. The BigQuery Connector for SAP stores your settings in the `/GOOG/BQ_FIELD` configuration table.

Before a table is created, you can change the default data type specification to a different BigQuery data type and Pub/Sub Avro data type.

**Booleans and timestamps:** To accurately reflect the data types of booleans and timestamps in the target table, before the target table is created, you need to manually change their target data types to `BOOLEAN` and `TIMESTAMP`, respectively. For more information, see Data types that require special handling.

#### Data types that require special handling

Several SAP data types require special handling so that they are represented accurately in the target BigQuery table.

Some of these data types you have to handle yourself. The BigQuery Connector for SAP takes care of others for you.

##### Booleans

For booleans, SAP uses the data type `CHAR`, which by default, the BigQuery Connector for SAP maps to the `STRING` data type in the target BigQuery table.

Consequently, for booleans, when you configure replication by using the `/GOOG/SLT_SETTINGS` transaction, you need to change the default data type assignment for boolean fields from `STRING` to `BOOLEAN` in the field definitions screen.

##### Timestamps

For timestamps, SAP uses the data types `P` (packed decimal) or `DEC` (decimal), which by default, BigQuery Connector for SAP maps to `NUMERIC` in the target BigQuery table.

Consequently, for timestamps, when you configure replication by using the `/GOOG/SLT_SETTINGS` transaction, you need to change the default data type assignment for timestamp fields from `NUMERIC` to `TIMESTAMP` or `TIMESTAMP (LONG)` in the field definitions screen.

##### `X` SAP type kind

The `X` SAP type kind is a hexadecimal value and is represented by the `RAW`, `RAWSTRING`, or `LRAW` SAP data types. By default, BigQuery Connector for SAP maps these data types to `STRING` in the source BigQuery table.

If you need a source field with the `X` SAP type kind to map to `BYTES` instead, then you need to change the default data type assignment for the field in the field definitions screen of the `/GOOG/SLT_SETTINGS` transaction.

The `X` SAP type kind is also sometimes used in SAP to represent integers. In this case, BigQuery Connector for SAP checks the data type of the source field for one of the SAP data types for integers, `INT1`, `INT2`, `INT4`, `INT8` and assigns the `INTEGER` data type in the target BigQuery table.

##### `y` SAP type kind

The `y` SAP type kind is a byte string and is represented by the `RAW`, `RAWSTRING`, or `LRAW` SAP data types. By default, BigQuery Connector for SAP maps these data types to `STRING` in the source BigQuery table.

If you need a source field with the `y` SAP type kind to map to `BYTES` instead, then you need to change the default data type assignment for the field in the field definitions screen of the `/GOOG/SLT_SETTINGS` transaction.

##### `LRAW` SAP data type

BigQuery Connector for SAP stores `LRAW` data types in BigQuery as `Base64` encoded strings.

If you're using CDC replication through Pub/Sub to BigQuery, then the connector converts `LRAW` fields into `UTF-8` encoding before sending them to Pub/Sub. Despite this conversion, the connector still stores the data as `Base64` in BigQuery.

The connector's `UTF-8` conversion of an `LRAW` field's value considers only the initial bytes that its preceding length column indicates. This adheres to [SAP standards](https://help.sap.com/doc/saphelp_snc70/7.0/en-US/cf/21f2e5446011d189700000e8322d00/content.htm?no_cache=true), where the preceding length field (an `INT2` or `INT4` type) defines the valid length of the `LRAW` content.

#### Default data type mapping

The following table shows the default data type conversion of the BigQuery Connector for SAP:

SAP type kind | SAP data type | BigQuery data type | Pub/Sub Avro data type | Notes  
---|---|---|---|---  
`b` (1 byte integer)  
`s` (2 byte integer)  
`I` (4 byte Integer)  
`8` (8 byte integer)  | `INT1`  
`INT2`  
`INT4`  
`INT8` | `INTEGER` | `INT` |   
`F` (float)  | `FLTP` | `FLOAT` | `FLOAT` |   
`P` (packed)  | `CURR`  
`DEC`  
`QUAN` | `NUMERIC` | `DOUBLE` | By default, the SAP type kind `P` is mapped to the BigQuery data type `NUMERIC` and converted to a number in the external format.  
`a` (decimal floating number, 16 places)  | `DECFLOAT16`  
| `NUMERIC` | `DOUBLE` |   
`e` (decimal floating number, 16 places)  | `DECFLOAT34`  
| `NUMERIC` | `DOUBLE` |   
`N` (numeric) | `NUMC` | `STRING` | `STRING` |   
`X` (hexadecimal)  
`y` (byte string)  | `RAW`  
`RAWSTRING`  
`LRAW` | `STRING` | `STRING` | If the SAP type kind is `X`, but the data-type name covers pattern `'INT*'` (`INT1`, `INT2`, `INT4`), a source data element is replaced with a new data element `TYPINT8` with `TYPEKIND '8'`, which is mapped to the BigQuery data type `INTEGER`.  
`C` (character)  
`g` (character string)  
`?` (csequence)  
`&` (clike)  | `CHARSTRING` | `STRING` | `STRING` |   
`D` (date) | `DATS` | `DATE` | `STRING` |   
`T` (time) | `TIMS` | `TIME` | `STRING` |   
  
## Target bucket and data conversion properties for Cloud Storage

When you configure replication in transaction `/GOOG/SLT_SETTINGS`, you can define configurations for the target bucket in Cloud Storage.

### Bucket and folder properties

You specify the destination for your replicated data using a Cloud Storage URI. Note the following requirements for the target path:

  * **URI format** : You can specify the target in the format `BUCKET_NAME/FOLDER_NAME` or `gs://BUCKET_NAME/FOLDER_NAME`.
  * **Path limit** : The full path to your target bucket and folder structure must not exceed 255 characters.



### Field properties

By default, BigQuery Connector for SAP uses the field names and data types in the SAP source table as the field definitions in the target JSON files.

Optionally, before the target JSON files are created, you can customize field names or change the data type conversion.

#### Customizing target field names

When you configure replication, you can view the field names in the field definitions screen of the `/GOOG/SLT_SETTINGS` transaction. The BigQuery Connector for SAP stores your settings in the `/GOOG/BQ_FIELD` configuration table.

You can specify a custom field name by editing the generated name in the **Temporary Field Name** column of the field definitions screen. If you delete a value and leave the **Temporary Field Name** field blank, then BigQuery Connector for SAP uses the name of the source field for the name of that target field.

After making any edits to the **Temporary Field Name** , when you click **Save** , BigQuery Connector for SAP validates the value and saves the changes. You can validate a value without saving it by pressing **Enter**.

For information about how to customize field definitions, see [Customize the default field definitions](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-gcs-file-replication#field-definitions).

#### Use a spreadsheet or text file to edit the field definition

Before you create the target JSON files, you can optionally save the default data types and names of the target fields to a spreadsheet or text file, so that data engineers or administrators can edit the values without requiring access to SAP LT Replication Server.

After the values are edited, you need to convert the file and its contents to the comma-separated values (CSV) format. You can then apply the updates to the mass transfer settings by uploading the CSV file by using the custom transaction `/GOOG/SLT_SETTINGS`.

The process for editing the field definitions by using a CSV file includes the following steps:

  1. Create a spreadsheet or text file of the default field definitions.
  2. Edit the values.
  3. Convert the spreadsheet or text file to CSV format.
  4. Upload the CSV file.



For detailed instructions for each of these steps, see [Edit field definitions in a CSV file](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#edit-field-definitions-in-csv).

### Data type conversion

Before a JSON file is created, you can change the default data type specification to a different JSON format.

**Booleans and timestamps:** To accurately reflect the data types of booleans and timestamps in the target JSON files, before the files are delivered, you need to manually change their target data types to `BOOLEAN` and `TIMESTAMP`, respectively. For more information, see Data types that require special handling.

#### Data types that require special handling

Several SAP data types require special handling so that they are represented accurately in the target JSON files.

Some of these data types you have to handle yourself. The BigQuery Connector for SAP takes care of others for you.

##### Booleans

For booleans, SAP uses the data type `CHAR`, which by default, the BigQuery Connector for SAP maps to the `STRING` data type in the target JSON files.

Consequently, for booleans, when you configure replication by using the `/GOOG/SLT_SETTINGS` transaction, you need to change the default data type assignment for boolean fields from `STRING` to `BOOLEAN`.

##### Timestamps

For timestamps, SAP uses the data types `P` (packed decimal) or `DEC` (decimal), which by default, BigQuery Connector for SAP maps to `NUMERIC` in the target JSON files.

Consequently, for timestamps, when you configure replication by using the `/GOOG/SLT_SETTINGS` transaction, you need to change the default data type assignment for timestamp fields from `NUMERIC` to `TIMESTAMP` or `TIMESTAMP (LONG)`.

##### `X` SAP type kind

The `X` SAP type kind is a hexadecimal value and is represented by the `RAW`, `RAWSTRING`, or `LRAW` SAP data types. By default, BigQuery Connector for SAP maps these data types to `STRING` in the target JSON files.

If you need a source field with the `X` SAP type kind to map to `BYTES` instead, then you need to change the default data type assignment for the field in the field definitions screen of the `/GOOG/SLT_SETTINGS` transaction.

The `X` SAP type kind is also sometimes used in SAP to represent integers. In this case, BigQuery Connector for SAP checks the data type of the source field for one of the SAP data types for integers, `INT1`, `INT2`, `INT4`, `INT8` and assigns the `INTEGER` data type in the target JSON files.

##### `y` SAP type kind

The `y` SAP type kind is a byte string and is represented by the `RAW`, `RAWSTRING`, or `LRAW` SAP data types. By default, BigQuery Connector for SAP maps these data types to `STRING` in the target JSON files.

If you need a source field with the `y` SAP type kind to map to `BYTES` instead, then you need to change the default data type assignment for the field in the field definitions screen of the `/GOOG/SLT_SETTINGS` transaction.

##### `LRAW` SAP data type

BigQuery Connector for SAP stores `LRAW` data types in the JSON files as `Base64` encoded strings.

By default, BigQuery Connector for SAP converts source SAP data types into JSON-compatible formats based on the _SAP type kind_ or the _SAP data type_ of the source SAP field.

The following table shows the default data type conversion of BigQuery Connector for SAP for file-based replication to Cloud Storage:

SAP type kind | SAP data type | JSON representation | Notes  
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
`QUAN` | `NUMERIC` | By default, the SAP type kind `P` is converted to a numeric value in the target JSON files.  
`a` (decimal floating number, 16 places)  | `DECFLOAT16`  
| `NUMERIC` |   
`e` (decimal floating number, 16 places)  | `DECFLOAT34`  
| `NUMERIC` |   
`N` (numeric) | `NUMC` | `STRING` |   
`X` (hexadecimal)  
`y` (byte string)  | `RAW`  
`RAWSTRING`  
`LRAW` | `STRING` | If the SAP type kind is `X`, but the data-type name covers pattern `'INT*'` (`INT1`, `INT2`, `INT4`), a source data element is replaced with a new data element `TYPINT8` with `TYPEKIND '8'`. This ensures that the field is converted to a numeric value in the target JSON files.  
`C` (character)  
`g` (character string)  
`?` (csequence)  
`&` (clike)  | `CHARSTRING` | `STRING` |   
`D` (date) | `DATS` | `DATE` |   
`T` (time) | `TIMS` | `TIME` |   
  
## Language support

BigQuery Connector for SAP only supports replication configurations in English. When you configure replication using the SAP transactions and the custom transaction that is provided by Google Cloud, use **English** as your logon language on the SAP logon screen.

However, BigQuery Connector for SAP supports execution of background jobs that are running on the SAP LT Replication Server in all languages that SAP SLT supports.

Any error messages that you might encounter when working with the BigQuery Connector for SAP are generated in English , irrespective of the background job execution language.

## Licensing

BigQuery Connector for SAP is made available as "Software" under the agreement governing your use of Google Cloud Platform, including the Service Specific Terms available at <https://cloud.google.com/terms/service-terms>. Without limiting the generality of the preceding terms, you may not modify or distribute BigQuery Connector for SAP without express written permission from Google.

BigQuery Connector for SAP software is offered at no cost. For clarity, your use of other "Software" and "Services" under the agreement governing your use of Google Cloud Platform, such as BigQuery, Pub/Sub, Pub/Sub API, Storage Write API (gRPC), and BigQuery streaming API, Cloud Storage may incur a cost.

BigQuery Connector for SAP does not include any license to SAP software, including without limitation SAP LT Replication Server; you need to separately procure an appropriate license to SAP software.

## Support lifecycle

Google Cloud supports and maintains the latest major version of BigQuery Connector for SAP for a period of at least 12 months following the publication of a notice of deprecation at [Release Notes page for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/release-notes), the prior major version.

## What's next

For information about how to install the BigQuery Connector for SAP, see the [Install the BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/install).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
