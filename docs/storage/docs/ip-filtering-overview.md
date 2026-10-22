---
url: https://docs.cloud.google.com/storage/docs/ip-filtering-overview/
title: Bucket IP filtering \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:31.542139+00:00
---

# Bucket IP filtering  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/ip-filtering-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Bucket IP filtering Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of bucket IP filtering including its benefits, how it works, supported locations, and limitations to consider.

## Overview

Cloud Storage offers bucket IP filtering to manage access to your data stored in buckets.

Bucket IP filtering is a network security mechanism that restricts access to a bucket based on the source IP address of the request and secures your data from unauthorized access.

The bucket IP filtering feature for Cloud Storage enables fine-grained access control based on IPv4 or IPv6 address ranges or the Google Cloud Virtual Private Cloud. You can configure a list of IP ranges at the bucket level and all incoming requests to the bucket are restricted to the configured IP ranges and VPCs. This feature provides a way to secure sensitive data in Cloud Storage buckets and prevent unauthorized access from specific IP addresses or VPCs.

## Benefits

Bucket IP filtering for Cloud Storage offers the following benefits:

  * **Fine-grained access control** : Restrict access to your Cloud Storage buckets based on the specific IP address (IPv4 or IPv6) or Google Cloud Virtual Private Cloud of the requester. Bucket IP filtering acts as a strong network-level security layer, preventing unauthorized access from unknown or untrusted sources.

  * **Enhanced security** : By limiting access to authorized IP addresses or VPCs, you can reduce the risk of unauthorized access, data breaches, and malicious activity.

  * **Flexible configuration** : You can configure and manage lists of IP ranges at the bucket level, tailoring the access control to your specific requirements.




## IP filtering configurations

Bucket IP filtering helps you control access to your buckets by defining rules that permit requests from specific IPv4 and IPv6 addresses. Incoming requests are evaluated against these rules to determine access permissions.

When you configure IP filtering, you define rules based on the following settings:

  * **Public internet access** : You can define rules to manage requests originating from the public internet (outside any configured Virtual Private Cloud). These rules specify allowed IPv4 or IPv6 addresses using CIDR ranges, authorizing inbound traffic from those sources.

  * **Virtual private cloud (VPC) access** : For granular control over access from specific VPC networks, you can define rules for each network. These rules include allowed IP ranges, enabling precise management of access from your virtual network infrastructure.

  * **Service agent access** : Google Cloud service agents retain access to buckets, even with an active IP filtering configuration. You can set up a configuration that allows Google Cloud services such as BigLake, Storage Insights, Vertex AI, and BigQuery to bypass the IP filter validation when accessing your buckets.

  * **Cross-organization VPC access** : To securely share data with trusted VPC networks located in different Google Cloud organizations, you can define rules to permit their access to your bucket.




## Limitations

Bucket IP filtering has the following limitations:

  * **Maximum number of IP CIDR blocks** : You can specify a maximum of 200 IP CIDR blocks across public and VPC networks in the IP filter rule for a bucket.

  * **Maximum number of VPC networks** : You can specify a maximum of 25 VPC networks in the IP filter rules for a bucket.

  * **Regional endpoints** : [Regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints) work with IP filtering only when you use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).

  * **IPv6 support** : IP filtering with gRPC direct path is not supported on an IPv4 VM. When you use IP filtering with gRPC direct path, you must enable [IPv6 support](https://docs.cloud.google.com/vpc/docs/ipv6-support) on the VPC network.

  * **Blocked Google Cloud services** : Enabling IP filtering on Cloud Storage buckets restricts access for some Google Cloud services, regardless of whether they use a [service agent](https://docs.cloud.google.com/iam/docs/service-agents) to interact with Cloud Storage. For example, services such as BigQuery use Cloud Storage for importing and exporting data. To prevent service disruptions, we recommend not using IP filtering on Cloud Storage buckets accessed by the following services:

    * BigQuery interactions with Cloud Storage: 
      * [Load data](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv) from Cloud Storage to BigQuery.
      * [Export table data](https://docs.cloud.google.com/bigquery/docs/exporting-data) from BigQuery to Cloud Storage.
      * [Export query results](https://docs.cloud.google.com/bigquery/docs/writing-results#downloading-saving-results-console) from BigQuery to Cloud Storage.
      * Query from an [external Cloud Storage table](https://docs.cloud.google.com/bigquery/docs/external-data-cloud-storage#query_external_tables) with BigQuery.
    * If your [App Engine applications access data in Cloud Storage](https://docs.cloud.google.com/appengine/docs/standard/using-cloud-storage), we recommend [using App Engine through a Virtual Private Cloud](https://docs.cloud.google.com/appengine/docs/legacy/standard/python/connecting-vpc).
    * IP filtering doesn't support Cloud Shell.



## What's next

  * [Create IP filtering rules on a bucket](https://docs.cloud.google.com/storage/docs/create-ip-filter).
  * [Update the IP filtering rules on a bucket](https://docs.cloud.google.com/storage/docs/update-ip-filter).
  * [List the IP filtering rules on a bucket](https://docs.cloud.google.com/storage/docs/list-ip-filter).
  * [Disable the IP filtering rules on a bucket](https://docs.cloud.google.com/storage/docs/disable-ip-filtering).
  * [Bypass the IP filtering rules on a bucket](https://docs.cloud.google.com/storage/docs/bypass-ip-filter).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
