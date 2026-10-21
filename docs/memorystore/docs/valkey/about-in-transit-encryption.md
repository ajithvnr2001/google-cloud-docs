---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption/
title: About in-transit encryption \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:21.043245+00:00
---

# About in-transit encryption  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About in-transit encryption Stay organized with collections  Save and categorize content based on your preferences. 

You can encrypt all data that moves between your client applications and Memorystore for Valkey securely. This is _in-transit encryption_. By using in-transit encryption, all Valkey traffic is encrypted through the [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol. This ensures that all data that moves between your applications and Memorystore for Valkey remains confidential and untampered.

When in-transit encryption is enabled, Valkey clients communicate exclusively across a secure connection. Valkey clients that aren't configured for TLS are blocked. If you choose to use in-transit encryption, then you're responsible for ensuring that your Valkey client can use the TLS protocol.

The following are sample use cases for using in-transit encryption:

  * **Protect sensitive cached data** : If you use Memorystore for Valkey to store high-value information, such as session tokens, Personal Identifiable Information (PII), or API keys, then in-transit encryption prevents attackers with VPC access from accessing your data.
  * **Comply with industry standards** : Many security frameworks, including HIPAA for healthcare and PCI DSS for financial data, mandate that sensitive information be encrypted both at rest and in transit for regulatory and industry compliance purposes.
  * **Secure Identity and Access Management (IAM) authentication** : When you use [IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth) to manage access to your data, Memorystore for Valkey requires TLS to prevent the exposure or leaking of authentication tokens during transmission.
  * **Prevent person-in-the-middle attacks** : TLS authenticates the server endpoint using Certificate Authorities (CAs). CAs protect your application against server spoofing and unauthorized data modification as the data moves between your application and Memorystore for Valkey.

**Important:** For instances that have replicas, replicated data is encrypted fully at the network level, based on Google Cloud encryption standards. Memorystore for Valkey supports the TLS protocol, versions 1.2 and later.

## In-transit encryption prerequisites

To use in-transit encryption with Memorystore for Valkey, you need the following:

  1. A Valkey client that supports TLS or a third-party TLS sidecar.

  2. CA certificates that are installed on the client machine that accesses your instance.




Not every Valkey client library supports TLS. If you use a client that doesn't support TLS, then we recommend using a third-party plugin that enables TLS for your client. You can see an example of how to connect to a [Cluster Mode Enabled](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance#connect_to_an_in_transit_encryption_enabled_instance) or [Cluster Mode Disabled](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance#connect_to_cluster_disabled_in_transit_encryption_enabled_instance) instance in Memorystore for Valkey that has in-transit encryption enabled.

## Certificate Authorities (CAs)

An instance that uses in-transit encryption has Certificate Authorities (CAs) that authenticate the certificates of the machines in the instance. Memorystore for Valkey lets you choose a server CA mode. The CA mode determines which CA hierarchy is used to issue the digital certificates for an instance.

Memorystore for Valkey offers the following CA modes:

  * [**Per-instance CA**](https://docs.cloud.google.com/memorystore/docs/valkey/manage-in-transit-encryption): Memorystore for Valkey provisions each instance with its own, unique CA infrastructure. To access an instance securely, you must configure your clients to trust this CA hierarchy. This involves downloading and installing CA certificates on each client that accesses the instance.
  * [**Shared CA**](https://docs.cloud.google.com/memorystore/docs/valkey/use-shared-ca): a managed, regionalized CA infrastructure. For each region, you can download a single CA certificate bundle. This bundle is valid for all instances located in a region that you configure to use the shared CA. Using a shared CA reduces the number of certificates that clients need to manage.
  * [**Customer-managed CA**](https://docs.cloud.google.com/memorystore/docs/valkey/use-customer-managed-ca): use your own CA pool that's hosted on [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs). If your client applications are configured to trust this CA, then your applications can connect to an instance without you having to download and install additional CA certificates. This gives you greater control and helps you meet compliance requirements.



### Server certificate rotation

Every week, Memorystore for Valkey conducts server-side certificate rotation for instances that use the per-instance CA, shared CA, and customer-managed CA modes. New server certificates apply to new connections only, and existing connections remain alive during this rotation.

In addition to Memorystore for Valkey conducting a weekly server-side certificate rotation, for the customer-managed CA mode, you can rotate the certificates on-demand.

## Performance impact of enabling in-transit encryption

The in-transit encryption feature encrypts and decrypts data, which comes with a processing overhead. As a result, enabling in-transit encryption can reduce the performance of your clients. Also, when you use in-transit encryption, each additional connection comes with an associated resource cost.

To determine the latency associated with using in-transit encryption, compare the performance of your clients. To do this, benchmark the performance of an instance that has in-transit encryption enabled against an instance that has it deactivated.

### Guidelines to improve performance

To improve the performance of an instance, use the following guidelines:

  * When possible, decrease the number of client connections. Instead of creating on-demand, short-lived connections, establish and reuse long-running connections.

  * Increase the [size](https://docs.cloud.google.com/memorystore/docs/valkey/about-scaling-instance-capacity) of the instance.

  * Increase the CPU resources of your client's host machine. Client machines with a higher CPU count yield better performance. If you use a Compute Engine VM, then we recommend that you use optimized instances.

  * Decrease the payload size associated with the traffic of your client. Larger payloads require more round trips.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
