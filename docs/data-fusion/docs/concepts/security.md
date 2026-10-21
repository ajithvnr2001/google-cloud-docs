---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/security/
title: Security overview \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:36.244904+00:00
---

# Security overview  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Security overview Stay organized with collections  Save and categorize content based on your preferences. 

## Security recommendations

For workloads that require a strong security boundary or isolation, consider the following:

  * To enforce strict isolation, place security-sensitive workloads in a different Google Cloud project.

  * To control access to specific resources, enable [role-based access control](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac) in your Cloud Data Fusion instances.

  * To ensure that the instance isn't publicly accessible and to reduce the risk of sensitive data exfiltration, enable [internal IP addresses](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip) and [VPC service controls (VPC-SC)](https://docs.cloud.google.com/data-fusion/docs/how-to/using-vpc-sc) in your instances.




## Authentication

The Cloud Data Fusion web UI supports authentication mechanisms supported by Google Cloud console, with access controlled through [Identity and Access Management](https://docs.cloud.google.com/iam/docs).

## Networking controls

You can create a [private Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip), which can be connected to your VPC Network through [VPC peering](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip#set-up-vpc-peering) or [Private Service Connect](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect#configure-psc). Private Cloud Data Fusion instances have an internal IP address, and aren't exposed to the public internet. Additional security is available using [VPC Service Controls](https://docs.cloud.google.com/data-fusion/docs/how-to/using-vpc-sc) to establish a security perimeter around a Cloud Data Fusion private instance.

For more information, see the [Cloud Data Fusion networking overview](https://docs.cloud.google.com/data-fusion/docs/concepts/networking).

### Pipeline execution on pre-created internal IP Managed Service for Apache Spark clusters

You can use a private Cloud Data Fusion instance with the [remote Hadoop provisioner](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480313996). The Managed Service for Apache Spark cluster must be on the VPC network [peered](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip#set_up_network_peering) with Cloud Data Fusion. The remote Hadoop provisioner is configured with the internal IP address of the master node of the Managed Service for Apache Spark cluster.

## Access control

  * Managing access to the Cloud Data Fusion instance: RBAC-enabled instances support managing access at a namespace level through Identity and Access Management. RBAC-disabled instances only support managing access at an instance level. If you have access to an instance, you have access to all pipelines and metadata in that instance.

  * Pipeline access to your data: Pipeline access to data is provided by granting access to the service account, which can be a custom service account that you specify.




### Firewall rules

For a pipeline execution, you control ingress and egress by setting the appropriate firewall rules on the customer VPC on which the pipeline is being executed.

For more information, see [Firewall rules](https://docs.cloud.google.com/data-fusion/docs/concepts/networking#firewall-rules).

## Key storage

Passwords, keys, and other data are securely stored in Cloud Data Fusion and encrypted using keys stored in [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs). At runtime, Cloud Data Fusion calls Cloud Key Management Service to retrieve the key used to decrypt stored secrets.

## Encryption

By default, data is encrypted at rest using [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/default-keys), and in transit using TLS v1.2. You use [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/data-fusion/docs/how-to/customer-managed-encryption-keys) to control the data written by Cloud Data Fusion pipelines, including Managed Service for Apache Spark cluster metadata and Cloud Storage, BigQuery, and Pub/Sub data sources and sinks.

## Service accounts

Cloud Data Fusion pipelines execute in Managed Service for Apache Spark clusters in the customer project, and can be configured to run using a customer-specified (custom) service account. A custom service account must be granted the [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam) role.

## Projects

Cloud Data Fusion services are created in Google-managed tenant projects that users can't access. Cloud Data Fusion pipelines execute on Managed Service for Apache Spark clusters inside customer projects. Customers can access these clusters during their lifetime.

![Deploy the pipeline.](https://docs.cloud.google.com/static/data-fusion/docs/images/concepts/network_traffic_2x.png)

## Audit logs

Cloud Data Fusion audit logs are available from [Logging](https://docs.cloud.google.com/logging/docs).

## Plugins and artifacts

Operators and Admins should be wary of installing untrusted plugins or artifacts, as they might present a security risk.

## Workforce identity federation

[Workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) users can perform operations in Cloud Data Fusion, such as creating, deleting, upgrading, and listing instances. For more information about limitations, see [Workforce identity federation: supported products and limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services#data-fusion).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
