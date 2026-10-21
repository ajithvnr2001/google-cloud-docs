---
url: https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl/
title: Authorize with SSL/TLS certificates \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:25.702342+00:00
---

# Authorize with SSL/TLS certificates  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Authorize with SSL/TLS certificates Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl "View this page for the SQL Server database engine")

This page describes how you can use _Secure Socket Layer_ (SSL), now _Transport Layer Security_ (TLS), from your application to encrypt connections to Cloud SQL instances.

## Overview

Cloud SQL supports connecting to an instance using the SSL/TLS protocol. SSL/TLS connections provide a layer of security by encrypting data-in-transit between your client and the database in your Cloud SQL instance. Optionally, your SSL/TLS connection can perform server identity verification by validating the server certificate installed on the Cloud SQL instance and client identity verification by validating the client certificate installed on the client.

### Server certificates

When you create an instance, Cloud SQL automatically creates and installs a server certificate that is signed by a certificate authority (CA). You can download the CA certificate to the client host machine and use it to verify the CA and server Cloud SQL identity. Optionally, you can choose the type of CA that Cloud SQL uses to sign the server certificate.

### Client certificates

You can optionally create and download client certificates along with keys to the client's host machine for mutual authentication (server and client identity verification). You can't choose the type of CA that Cloud SQL uses to sign the client certificate.

#### Connect using SSL/TLS

When connecting to a Cloud SQL instance from clients, you can use SSL/TLS for direct connections as well as for connections that use [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy) or [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/mysql/connect-connectors).

  * For direct connections, Google strongly recommends enforcing SSL/TLS encryption using the SSL mode setting in Cloud SQL. Optionally, you can also enforce client certificate verification. For more information, see [Enforce SSL/TLS encryption](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#enforcing-ssl).

  * For connections that use Cloud SQL Auth Proxy or Cloud SQL Language Connectors, the connections are automatically encrypted with SSL/TLS along with client and server identity verification without requiring you to download a server CA certificate and client certificate.




For more information about Cloud SQL connectivity options, see [About Cloud SQL connections](https://docs.cloud.google.com/sql/docs/mysql/connect-overview).

For more information about client-side SSL/TLS configuration, see [the documentation for your database engine](https://dev.mysql.com/doc/refman/8.0/en/using-encrypted-connections.html#using-encrypted-connections-client-side-configuration). 

## Certificate authority (CA) hierarchies

This section describes the three types of server certificate authority (CA) that you can choose for your Cloud SQL instances. You have three options:

  * **Per-instance CA** : with this option, an internal CA dedicated to each Cloud SQL instance signs the server certificate for that instance. Cloud SQL creates and manages these CAs. To choose per-instance CA, select **Google managed internal certificate authority** (Google Cloud console) or specify `GOOGLE_MANAGED_INTERNAL_CA` for the `serverCaMode` setting (Cloud SQL Admin API) or the `--server-ca-mode` flag ([gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)) when you [create the instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen). If you leave the setting or flag unspecified when you create an instance, then this option is the default value for the instance. You can't update an instance to use the per-instance CA option if the instance is configured to use a shared CA or customer-managed CA.

  * **Shared CA** : with this option, a CA hierarchy consisting of a root CA and subordinate server CAs is used. The subordinate server CAs in a region sign the server certificates and are shared across instances in the region. Using a shared CA hierarchy is helpful as you increase the number of instances in a region because you don't need to manage unique CAs for individual instances. By switching to a shared CA (`GOOGLE_MANAGED_CAS_CA`), you can use a single regional CA bundle for all your instances in the region, which can simplify your client-side configuration. Cloud SQL hosts and manages the root CA and subordinate server CAs on Google Cloud Certificate Authority Service (CA Service). Cloud SQL also handles the rotation of root CA and subordinate server CAs and provides publicly available links to the [CA certificate bundles](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#download-root-regional-ca-bundles) for download. To choose shared CA, select **Google managed CAS certificate authority** in the Google Cloud console or specify `GOOGLE_MANAGED_CAS_CA` for the `serverCaMode` setting (Cloud SQL Admin API) or the `--server-ca-mode` flag ([gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)) when you [create](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen) or [edit](https://docs.cloud.google.com/sql/docs/mysql/edit-instance) the instance. You can update an existing instance to use a shared CA hierarchy if you're using either the per-instance CA or the customer-managed CA option.

  * **Customer-managed CA** : with this option, you [create and manage](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca) your own CA hierarchy. Choose this option if you want to manage your own CAs and certificates. By using a customer-managed CA (`CUSTOMER_MANAGED_CAS_CA`), you can manage your own CA hierarchy and rotation policies with CA Service. This configuration gives you greater control and helps you meet compliance requirements. To choose customer-managed CA, you need to create a CA pool and CA in CA Service. In Cloud SQL, specify the CA pool and **Customer managed CAS certificate authority** (Google Cloud console), `CUSTOMER_MANAGED_CAS_CA` for the `serverCaMode` setting (Cloud SQL Admin API), or the `--server-ca-mode` flag ([gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)) when you [create](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen) or [edit](https://docs.cloud.google.com/sql/docs/mysql/edit-instance) the instance. You can update an existing instance to use a customer-managed CA hierarchy if you're using either the per-instance CA or the shared CA option.




After you create or update instance, you can view which CA hierarchy is configured for a Cloud SQL instance by using the `gcloud sql instances describe` command or in the Google Cloud console. For more information, see [View instance information](https://docs.cloud.google.com/sql/docs/mysql/instance-info).

The following table compares the three CA hierarchy options.

**Feature** | **Per-instance CA** | **Shared CA** | **Customer-managed CA**  
---|---|---|---  
**CA structure** | Separate CA for each instance | Root CA and subordinate CAs shared across instances in the same region  | CA hierarchy that you create and manage  
**Cryptographic attributes** | RSA 2048-bit key with SHA256 algorithm |  Elliptic Curve Digital Signature Algorithm (ECDSA) with 384-bit key with SHA384 algorithm  |  Elliptic Curve Digital Signature Algorithm (ECDSA) with 384-bit key with SHA384 algorithm   
**CA validity period** | 10 years | 25 years for root CA and 10 years for subordinate CAs | Configurable *  
**Server certificate validity period** | 10 years | 1 year | 1 year**  
**User-initiated rotation of CA?** | Yes | No. CA rotation is managed by Cloud SQL | Yes  
**User-initiated rotation of server certificate?** | Yes | Yes | Yes  
**Automatic rotation of server certificate?** | No | Yes | Yes  
**CA trust anchor for TLS connections** | The unique per-instance CA is the trust anchor for the corresponding instance. | Root CA and subordinate CAs are the trust anchors for all instances in a given region. | The CAs that you create and manage are the trust anchors.  
**Server identity verification** | Verifying the CA verifies the server identity since each instance has a unique CA. | Verifying the hostname along with verifying the CA is required for server identity verification since server CAs are shared across instances. | Although the CA might not be shared across instances, you might want to verify the hostname along with verifying the CA.  
**Subject Alternative Name (SAN) field in server certificates** | The SAN field contains the hostname (DNS name of the instance) only for instances enabled with [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect). Hostname can be used for server identity verification. If you are connecting to a Cloud SQL instance using the DNS name as the hostname, then you need to set up DNS resolution. | The SAN field contains the hostname (DNS name of the instance) for _all types_ of instances. Hostname can be used for server identity verification. If you are connecting to a Cloud SQL instance using the DNS name as the hostname, then you need to set up DNS resolution. | The SAN field contains the hostname (DNS name of the instance) for _all types_ of instances. Hostname can be used for server identity verification.   
**[Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) version support** | Supports all versions of the Cloud SQL Auth Proxy, v1 and later. | Requires the Cloud SQL Auth Proxy version 2.13.0 or later. | Requires the Cloud SQL Auth Proxy version 2.14.3 or later.  
**Service connection limitations** | None |  Doesn't support connections from the following Google Cloud services: 

  * [App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard)
  * [App Engine flexible environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-flexible)
  * [Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run) services that run in a [first generation execution environment](https://docs.cloud.google.com/run/docs/about-execution-environments#choose)

|  Doesn't support connections from the following Google Cloud services: 

  * App Engine standard environment
  * App Engine flexible environment
  * Cloud Run services that run in a first generation execution environment

  
  
* For the customer-managed CA option, the default validity period of a CA certificate in CA Service is 10 years. You have the option to configure a different validity period for your CA certificates. A shorter validity period for the CA might require more frequent CA rotations and a validity period shorter than one year might affect the validity period of your server certificates. For more information, see [Managing CA rotation](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-rotation).

** For the customer-managed CA option, the default validity period of a server certificate is one year. However, if you configure a validity period that is shorter than one year for your CA certificate, then your server certificate has a shorter validity period. For more information about configuring the validity period of your CA certificate upon creation, see [CA certificate settings](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-settings#ca_certificate_settings) and [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#create-root-ca).

### Per-instance CA hosted by Cloud SQL

The per-instance CA hierarchy is the default server CA mode configuration when you create an instance using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Cloud SQL Admin API, or Terraform.

Cloud SQL creates a new self-signed server CA for each instance when you create the instance. To use this setting, configure `serverCaMode` to `GOOGLE_MANAGED_INTERNAL_CA` when you create the instance. You can either leave the `serverCaMode` configuration setting unspecified using Cloud SQL Admin API or [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or select the **Google internal Certificate Authority** option in the Google Cloud console.

You can't update the `serverCaMode` of an instance that uses a shared CA or customer-managed CA hierarchy to use the per-instance CA hierarchy.

The following diagram shows the per-instance CA hierarchy.

![Diagram of per-instance internal CA hierarchy.](https://docs.cloud.google.com/static/sql/images/internal-ca.svg)

### Shared CAs hosted by CA Service

This server CA mode consists of a root CA and subordinate server CAs in each region. The subordinate server CAs issue server certificates and are shared across instances in the region. Cloud SQL handles the rotation of the shared regional server CAs and provides publicly available links to download the [CA certificate bundles](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#download-root-regional-ca-bundles).

You can configure an instance to use a server CA hierarchy where the issuing CAs are shared across the instances in the same region. To use this setting, configure `serverCaMode` to `GOOGLE_MANAGED_CAS_CA` when you create or edit the instance. You can also select **Google Managed CAS Certificate Authority** in the Google Cloud console.

The following diagram shows the shared CA hierarchy.

![Diagram of a shared CA hierarchy](https://docs.cloud.google.com/static/sql/images/regional-shared-ca.svg)

### Customer-managed CAs

This server CA mode lets you set up your own CA hierarchy in CA Service.

To use the customer-managed CA option in Cloud SQL, you create a CA pool in the same region as your Cloud SQL instances. Then you create at least one CA. When you create the Cloud SQL instance, specify the ID of the CA pool in the `serverCaPool` field and configure the `serverCaMode` field with the `CUSTOMER_MANAGED_CAS_CA` value. CA Service provides a CA from the CA pool and uses that CA to issue the server certificate for the instance.

When you create CAs in CA Service, you can create either a root CA or a subordinate CA depending on your use case. For example, you might want to create a subordinate CA if you plan to set up a root CA hierarchy or chain up to an external CA.

Select the customer-managed CA option only if you want to manage your own CAs and certificates. For more information, see [Use a customer-managed CA](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca).

## How server certificate rotation works

Cloud SQL provides ways to rotate your server certificate, so the new certificate can be seamlessly swapped in before the old certificate expires.

Instances using the shared CA or customer-managed CA hierarchy can enable [automatic server certificate rotation](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#automatic-server-certificate-rotation-cas) to run during [maintenance updates](https://docs.cloud.google.com/sql/docs/mysql/maintenance) up to 180 days before expiry.

For instances that use the per-instance CA, shared CA, or customer-managed CA hierarchies, about three months before the server certificate expires for a Cloud SQL instance, the project owners receive an email from Cloud SQL, stating that the certificate rotation process has begun for that instance. The email provides the name of the instance, and says that Cloud SQL has added a new server certificate to the project. The existing server certificate continues to function normally. In effect, the instance has two server certificates during this period.

The server certificate rotation command to use depends on whether you are using a server certificate issued by a per-instance CA or a server certificate issued by the shared CA or customer-managed CA.

Before the current server certificate expires, download the new `server-ca.pem` file, which contains the certificate information for both the current and the new server certificates. Update your MySQL clients to use the new file, by copying it to all of your MySQL client host machines, replacing the existing file.

After all of your MySQL clients have been updated, send a [rotate command (for per-instance CA)](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#rotate) or [rotate command (for shared CA or customer-managed CA)](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#rotate-server-certificate-cas) to the Cloud SQL instance to rotate to the new server certificate. After that is done, the old server certificate is no longer recognized, and only the new server certificate can be used.

Client certificates are not affected by server certificate rotation. 

### SSL certificate expiration

For Cloud SQL instances that use per-instance CAs (`serverCaMode` is set to `GOOGLE_MANAGED_INTERNAL_CA`), the SSL certificates come with an expiration period of 10 years. Before these certificates expire, perform [server CA certificate rotation](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#rotate).

For instances that use shared CAs (`serverCaMode` is set to `GOOGLE_MANAGED_CAS_CA`), the expiration period of the server certificates is 1 year. Before expiration, perform a [server certificate rotation](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#rotate-server-certificate-cas) or [enable automatic server certificate rotation](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#automatic-server-certificate-rotation-cas). The root certificate authority (CA) certificate has an expiration period of 25 years and the subordinate shared CA certificate has an expiration period of 10 years. Cloud SQL handles their rotation.

If you're using a customer-managed CA (`serverCaMode` is set to `CUSTOMER_MANAGED_CAS_CA`), then you can perform CA certificate rotation by rotating the CAs in the CA pool that you created. The expiration period of a CA is typically 10 years, but you can configure a shorter validity period for your CA in CA Service.

To rotate the CAs, use the CA rotation process in CA Service. For more information, see [Managing CA rotation](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-rotation).

If a client is configured to verify the CA or verify the hostname in the server certificate, then that client's connections to Cloud SQL instances with expired server certificates will fail. To prevent disruption to client connections, rotate the server certificate before the certificate expires.

Whether you use the per-instance CA, the shared CA, or the customer-managed CA server mode, you can [reset](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#reset) the SSL configuration of your Cloud SQL instance at any time.

## Limitations

This section covers limitations with SSL/TLS certificate configuration and Cloud SQL.

### Service connection limitations

  * If your instance uses the shared CA (`GOOGLE_MANAGED_CAS_CA`) or customer-managed CA (`CUSTOMER_MANAGED_CAS_CA`) option for its `serverCaMode` configuration, then the instance can't support connections from the following Google Cloud services: 
    * [App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard)
    * [App Engine flexible environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-flexible)
    * [Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run) services that run in a [first generation execution environment](https://docs.cloud.google.com/run/docs/about-execution-environments#choose)



## What's next

  * [Configure SSL/TLS](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance) on your Cloud SQL instance.

  * Learn more about [how encryption is handled in Google Cloud](https://cloud.google.com/security/encryption-in-transit).



  * [Connect using SSL/TLS](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip#connect-ssl) to your Cloud SQL instance.


  * [Manage SSL/TLS](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance) on your Cloud SQL instance.


  * Learn more about [how MySQL uses SSL/TLS](https://dev.mysql.com/doc/refman/8.4/en/encrypted-connections.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
