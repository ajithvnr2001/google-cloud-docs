---
url: https://docs.cloud.google.com/sql/docs/mysql/custom-dns-name/
title: Set up a custom DNS name for a Cloud SQL instance \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:38.141994+00:00
---

# Set up a custom DNS name for a Cloud SQL instance  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/custom-dns-name/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Set up a custom DNS name for a Cloud SQL instance Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/custom-dns-name "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/custom-dns-name "View this page for the SQL Server database engine")

This page describes how to set up a custom domain name system (DNS) name for your Cloud SQL instance.

## Overview

You can configure a Cloud SQL instance so that your applications can connect using a custom DNS name managed by your organization. If you want to use a custom DNS name to connect to a Cloud SQL instance instead of using an IP address, then configure a custom subject alternative name (SAN). You can configure a custom SAN when you create or update an instance.

When you add a custom DNS name as a custom SAN configuration to your instance, Cloud SQL inserts the custom DNS name to the SAN field of the server certificate of the instance. This customization lets you use the custom DNS name with [hostname validation](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#server-identity-verification) securely. You can add a comma-separated list of up to three custom DNS names to the custom SAN configuration. For security reasons, you can use a custom SAN configuration only for instances that you [configure with `CUSTOMER_MANAGED_CAS_CA`](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca) as the server CA mode.

After you configure the custom DNS name for your instance, you can use that custom DNS name to connect your database clients or applications, including [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/mysql/language-connectors) and the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy).

### Workflow

To set up a custom DNS name for an instance, do the following:

  1. Create an instance configured with customer-managed CA.
  2. Add custom SAN values to the instance. The custom SAN values are inserted into the SAN field of the server certificate of the instance.
  3. Determine the IP address of the instance.
  4. Create custom DNS records for your instance.
  5. Connect to the instance using the custom DNS name.



## Before you begin

Before you set up a custom DNS name for your instance, make sure you have the [required roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca#required-roles).

If you are creating a new Cloud SQL instance, then to use custom SAN, your instance must also use a [customer-managed certificate authority (CA)](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca) for its server CA mode.

## Create an instance with custom SAN values

To create an instance with custom SAN values, use the following `[gcloud sql instances create](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create)` command:

### gcloud
    
    
    gcloud sql instances create "INSTANCE_NAME" \
      --database-version=DATABASE_VERSION \
      --project=PROJECT_ID \
      --region=REGION \
      --server-ca-mode=CUSTOMER_MANAGED_CAS_CA \
      --server-ca-pool=projects/PROJECT_ID_CAS/locations/REGION/caPools/CA_POOL_ID
      --custom-subject-alternative-names=CUSTOM_DNS_NAME

Make the following replacements:

  * `INSTANCE_NAME` with the name of the Cloud SQL instance that you want to create.
  * `DATABASE_VERSION` with the [`enum` of the version](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion) of the Cloud SQL instance that you want to create. The customer-managed CA option is supported only on MySQL 8.0.30 and later.
  * `PROJECT_ID` with the ID of the project where you plan to create your Cloud SQL instances.
  * `PROJECT_ID_CAS` with the ID of the project where you created your CA_POOL_ID. This project might be the same or different from where you want to create your Cloud SQL instance. 
  * `REGION` with the region where you created the CA pool. You must create your instance in the same region as the CA pool.
  * `CA_POOL_ID` with the ID of the CA pool that you created.
  * `CUSTOM_DNS_NAME` with up to three custom DNS names, comma-separated with no spaces in between the values. For example, `develop.example.com,test.example.com,production.example.com`.



### Terraform

To create an instance with custom SAN values, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). The following sample also creates prerequisite resources for the new instance.
    
    
    resource "google_project_service_identity" "default" {
      provider = google-beta
      service  = "sqladmin.googleapis.com"
    }
    
    resource "random_string" "default" {
      length  = 10
      special = false
      upper   = false
    }
    
    resource "google_privateca_ca_pool" "default" {
      name     = "customer-ca-pool-${random_string.default.result}"
      location = "asia-northeast1"
      tier     = "DEVOPS"
      publishing_options {
        publish_ca_cert = false
        publish_crl     = false
      }
    }
    
    # This is required for setting up customer managed CAS (Certificate Authority Service) instances.
    resource "google_privateca_certificate_authority" "default" {
      pool                                   = google_privateca_ca_pool.default.name
      certificate_authority_id               = "my-certificate-authority"
      location                               = "asia-northeast1"
      lifetime                               = "86400s"
      type                                   = "SELF_SIGNED"
      deletion_protection                    = false # set to "true" in production
      skip_grace_period                      = true
      ignore_active_certificates_on_deletion = true
      config {
        subject_config {
          subject {
            organization = "my organization"
            common_name  = "my certificate authority name"
          }
        }
        x509_config {
          ca_options {
            is_ca = true
          }
          key_usage {
            base_key_usage {
              cert_sign = true
              crl_sign  = true
            }
            extended_key_usage {
              server_auth = false
            }
          }
        }
      }
      key_spec {
        algorithm = "RSA_PKCS1_4096_SHA256"
      }
    }
    
    resource "google_privateca_ca_pool_iam_member" "default" {
      ca_pool = google_privateca_ca_pool.default.id
      role    = "roles/privateca.certificateRequester"
    
      member = "serviceAccount:${google_project_service_identity.default.email}"
    }
    
    resource "google_sql_database_instance" "default" {
      name             = "mysql-instance"
      region           = "asia-northeast1"
      database_version = "MYSQL_8_4"
      settings {
        edition = "ENTERPRISE"
        tier    = "db-f1-micro"
        ip_configuration {
          # The following server CA mode lets the instance use customer-managed CAS CA to issue server certificates.
          # https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#ipconfiguration
          server_ca_mode                   = "CUSTOMER_MANAGED_CAS_CA"
          server_ca_pool                   = google_privateca_ca_pool.default.id
          custom_subject_alternative_names = ["customSan.test.com"]
        }
      }
    }

## Add or update custom SAN values for an instance

To add or update custom SAN values for an existing instance, do the following:

### gcloud
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --custom-subject-alternative-names=CUSTOM_DNS_NAME

**Caution** : If you're updating an instance that already has custom SAN values, then specify the existing custom SAN values or the existing values will be replaced.

Make the following replacements:

  * `INSTANCE_NAME` with the name of the Cloud SQL instance that you want to update.
  * `CUSTOM_DNS_NAME` with up to three custom DNS names, comma-separated with no spaces in between the values. For example, `develop.example.com,new-test.example.com,production.example.com`. 



### Terraform

To update an instance that already has custom SAN values, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "google_sql_database_instance" "default" {
      name             = "mysql-instance"
      region           = "asia-northeast1"
      database_version = "MYSQL_8_4"
      settings {
        edition = "ENTERPRISE"
        tier    = "db-f1-micro"
        ip_configuration {
          # The following server CA mode lets the instance use customer-managed CAS CA to issue server certificates.
          # https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#ipconfiguration
          server_ca_mode                   = "CUSTOMER_MANAGED_CAS_CA"
          server_ca_pool                   = google_privateca_ca_pool.default.id
          custom_subject_alternative_names = ["customSan.test.com"]
        }
      }
    }

**Caution** : If you're updating an instance that already has custom SAN values, then specify the existing custom SAN values or the existing values will be replaced.

## Clear all custom SAN values from an instance

To clear all custom SAN values from an instance, do the following:

### gcloud
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --clear-custom-subject-alternative-names

Replace `INSTANCE_NAME` with the name of the Cloud SQL instance that you want to update.

## Create custom DNS records

Before you can connect to the instance using the custom DNS name with your clients and applications, set up the mapping between the DNS name and the IP address. This mapping is known as DNS resolution. If you are connecting privately, then [create the DNS record in a private DNS zone](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name) in the corresponding Virtual Private Cloud (VPC) network.

To create custom DNS records for your instance, do the following:

  1. Retrieve the IP address for your instance. Run the following command:
         
         gcloud sql instances describe INSTANCE_NAME \
          --project=PROJECT_ID

Make the following replacements:

     * INSTANCE_NAME: the name of the Cloud SQL instance
     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  2. In the response, look for the `ipAddresses:` field.

For example:
         
         ipAddresses:
         - ipAddress: 192.0.2.4
           type: PRIVATE
         

You can retrieve the private IP address for an instance configured for [private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access), [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect), or [both](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access-and-private-service-connect).

**Warning** : For security reasons, we don't recommend setting up custom DNS records for the public IP address of an instance.
  3. Add two DNS records to a DNS zone used by your application. You can use a DNS server that you manage yourself or the [Cloud DNS private zone](https://docs.cloud.google.com/dns/docs/zones#create-private-zone) used by your application.

     * Create an `A` record for the IP address of the instance
     * Create a `TXT` record containing the instance connection name.

Standard database clients use the `A` record to look up the IP address to make the connection. Cloud SQL Language Connectors and the Cloud SQL Auth Proxy use the `TXT` record to look up the instance connection name.

For example, the connection string for your instance is `my-project:region:my-instance`, but you want to connect using the DNS name `prod-db.mycompany.example.com`. If the IP address of the instance on your company network is `192.0.2.4`, then create the following DNS records:
    
    Record type: A
    Name: prod-db.mycompany.example.com
    Value: 192.0.2.4
    TTL: 600
    
    Record type: TXT
    Name: prod-db.mycompany.example.com
    Value: my-project:region:my-instance
    TTL: 600
    




## Connect to an instance using a custom DNS name

When you connect to a Cloud SQL for MySQL instance, configure the custom DNS name as the hostname and enable server identity verification in your client. For example, when using the MySQL client, specify the flag `--ssl-mode=VERIFY_IDENTITY`. Other MySQL client drivers have similar configuration flags. 

If you're connecting to a private Cloud SQL instance from an external network, then you must configure your Cloud SQL instance and its Virtual Private Cloud (VPC) network to permit external connections and to let Cloud DNS communicate with on-premises systems. For more information about this configuration, see [Connect from an external source](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#vpn) and [Configure DNS for on-premises systems](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid#config-dns-onpremises).

## Limitations

  * You can't add more than three DNS names as custom SAN values to the server certificate of a Cloud SQL instance.
  * The maximum length of a DNS name that you can add to the certificate as a custom SAN value for an instance is 253 characters.
  * The DNS names that you add to the certificate for an instance can't have wildcard characters (`*`) or trailing dots. For example, `test.example.com.` isn't allowed.
  * The DNS names must be valid, as specified by [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034).
  * You can specify custom SAN values for `CUSTOMER_MANAGED_CAS_CA` instances only.



## What's next

  * [Manage](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance) SSL/TLS certificates on your Cloud SQL instance.
  * Learn more about [how encryption is handled in Google Cloud](https://docs.cloud.google.com/docs/security/encryption-in-transit).
  * [Connect](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip#connect-ssl) to your Cloud SQL instance using SSL/TLS certificates.
  * Learn more about [how MySQL uses SSL/TLS](https://dev.mysql.com/doc/refman/8.4/en/encrypted-connections.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
