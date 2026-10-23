---
url: https://docs.cloud.google.com/mainframe-connector/docs/get-started/
title: Get started with Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:40.031110+00:00
---

# Get started with Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/get-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Get started with Mainframe Connector Stay organized with collections  Save and categorize content based on your preferences. 

Before you install Mainframe Connector, you must perform the initial configuration steps:

  * Grant the required roles to your service account.
  * Configure security for your assets.
  * Configure network connectivity between your mainframe and Google Cloud.



Then, you can download the installation package and verify its authenticity using OpenSSL.

The following sections describe each task in detail.

## Grant service account permissions

Ensure that the following roles are granted to your service account. You can [grant multiple roles to your service account using the Google Cloud console](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#multiple-roles-console) or [grant the roles programmatically](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#multiple-roles-programmatic).

  * At the project level, assign the following roles: 
    * [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter)
    * [BigQuery Job User](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * On your Cloud Storage bucket, assign the following roles: 
    * [Storage Object Admin](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)
    * [BigQuery Data Editor](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
    * [BigQuery Read Session User](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.readSessionUser)



## Set up security for your assets

Ensure that the following permissions required by Java Cryptography Extension Common Cryptographic Architecture (IBMJCECCA) ([Java 8](https://www.ibm.com/docs/en/sdk-java-technology/8?topic=components-ibmjcecca) or [Java 17](https://www.ibm.com/docs/en/semeru-runtime-ce-z/17.0.0?topic=guide-ibmjcecca)) are granted for your mainframe. Transport layer security (TLS) is used on all requests made from your mainframe to Google Cloud APIs. If these permissions are not granted, you will see an `INSUFFICIENT ACCESS AUTHORITY` error message.

  * ICSF Query Facility (CSFIQF)
  * Random Number Generate (CSFRNG)
  * Random Number Generate Long (CSFRNGL)
  * PKA Key Import (CSFPKI)
  * Digital Signature Generate (CSFDSG)
  * Digital Signature Verify (CSFDSV)



## Set up network connectivity

Mainframe Connector interacts with Cloud Storage, BigQuery, and Cloud Logging APIs. Ensure [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) and [VPC Service Controls (VPC-SC)](https://docs.cloud.google.com/vpc-service-controls/docs/overview) is configured to allow access to specific BigQuery, Cloud Storage, and Cloud Logging resources from specified IP ranges, based on your enterprise policy. You can also use Pub/Sub, Dataflow, and Managed Service for Apache Spark APIs for additional integration between IBM z/OS batch jobs and data pipelines on Google Cloud.

Ensure that your network administration team has access to the following:

  * IP subnets assigned to the IBM z/OS logical partitions (LPARs)
  * Google Cloud service accounts used by IBM z/OS batch jobs
  * Google Cloud project IDs containing resources accessed by IBM z/OS batch jobs



## Configure firewalls, routers, and Domain Name Systems

Configure your mainframe IP files to include rules in firewalls, routers, and Domain Name Systems (DNSs) to allow traffic to and from Google Cloud. You can install either _userid.ETC.IPNODES_ or _userid.HOSTS.LOCAL_ as hosts file to resolve the standard Cloud Storage API endpoints as the VPC-SC endpoint. The sample file _userid.TCPIP.DATA_ is deployed to configure DNS to use the hosts file entries.
    
    
    - ETC.IPNODES
      - 199.36.153.4 www.googleapis.com
      - 199.36.153.5 www.googleapis.com
      - 199.36.153.6 www.googleapis.com
      - 199.36.153.7 www.googleapis.com
      - 199.36.153.4 oauth2.googleapis.com
      - 199.36.153.5 oauth2.googleapis.com
      - 199.36.153.6 oauth2.googleapis.com
      - 199.36.153.7 oauth2.googleapis.com
      - 127.0.0.1 LPAR1 (based on LPAR configuration)
      - 127.0.0.1 LPAR2
      - 127.0.0.1 LPAR3
    - HOSTS.LOCAL
      - HOST : 199.36.153.4, 199.36.153.5, 199.36.153.6, 199.36.153.7 : WWW.GOOGLEAPIS.COM ::::
      - HOST : 199.36.153.4, 199.36.153.5, 199.36.153.6, 199.36.153.7 : OAUTH2.GOOGLEAPIS.COM ::::
    - TCPIP.DATA
      - LOOKUP LOCAL DNS
    

### Configure your network to enforce VPC-SC

To enforce VPC-SC on your on-premises network, configure it as follows:

  * Configure the on-premises routers to route IBM z/OS outbound traffic to destination subnets within the VPC networks and the `restricted.googleapis.com` special domain using Cloud Interconnect or a virtual private network (VPN).
  * Configure the on-premises firewalls to allow outbound traffic to VPC subnets or VM instances and Google API endpoints - `restricted.googleapis.com 199.36.153.4/30`.
  * Configure the on-premises firewalls to deny all other outbound traffic to prevent bypass of VPC-SC.
  * Configure the on-premises firewalls to allow outbound traffic to `https://www.google-analytics.com`.



## Download and verify the installation package

To start using Mainframe Connector, download the latest installation package. Then, you can verify its integrity against the official signature using OpenSSL.

To download and verify Mainframe Connector, follow these steps:

  1. Download the prebuilt [Mainframe Connector JAR file](https://docs.cloud.google.com/mainframe-connector/docs/get-started/) to a directory that your user account has write permissions.

### Important

Be aware that Mainframe Connector uses Google Analytics to collect usage data. This helps us improve the software and provide a better user experience. By default, Google Analytics is enabled. However, you can opt out by configuring an [environment variable](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#disable_analytics) when running Mainframe Connector.   
  
The use of Google Analytics is subject to the Google Analytics [Terms of Service and Privacy Policy](https://www.google.com/analytics/terms). By downloading Mainframe Connector, you acknowledge that you have read, understood, and accepted the terms and conditions.

[Download](https://storage.googleapis.com/mainframe-connector-release/latest/mainframe-connector.tgz) Cancel

  2. Save the public key to a file named `mfc-key.pub`:
         
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         

  3. [Download the digital signature file](https://storage.googleapis.com/mainframe-connector-release/latest/mainframe-connector.tgz.1.sig) for the release artifact you downloaded.

  4. Run the OpenSSL command to verify the signature:
         
         openssl dgst -sha256 -verify mfc-key.pub \
           -signature mainframe-connector.tgz.1.sig mainframe-connector.tgz
         

The expected output of this command is `Verified OK`.




## What's next

  * [Install Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/installation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
