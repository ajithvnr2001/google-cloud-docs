---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authn-types-kafka/
title: Authentication types for Kafka brokers \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:29.347908+00:00
---

# Authentication types for Kafka brokers  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authn-types-kafka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Authentication types for Kafka brokers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the supported authentication methods for client applications connecting to Google Cloud Managed Service for Apache Kafka brokers.

For Google Cloud Managed Service for Apache Kafka client applications running on Google Cloud services like Google Kubernetes Engine, Compute Engine, Cloud Run, or Cloud Run functions, you have the following authentication options:

  * **SASL/OAUTHBEARER (recommended)** : this is the most seamless and secure method for clients within Google Cloud. It uses [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to automatically find the service account identity associated with the environment. This eliminates the need to manage and distribute static credential files like service account keys.

  * **SASL/PLAIN** : this is a useful method for early development. The client authenticates by using a long-lived service account key.

  * **mTLS** : this is an option if your organization's standard is certificate-based authentication. Your application on Google Cloud is configured with a client certificate and key.




For client applications running outside of Google Cloud, such as in an on-premises data center or on another cloud provider, consider the following authentication methods. Choose the best method based on your organization's security posture and existing identity infrastructure.

  * **Workload Identity Federation with SASL/OAUTHBEARER (recommended)** : this is the most secure method for external clients. It lets you grant identities from external systems, such as AWS, Microsoft Azure, or an on-premises identity provider like ADFS, the ability to impersonate a Google Cloud service account. Instead of managing long-lived service account keys, the client uses its preferred credential to obtain a short-lived Google Cloud access token. The client then uses this token for authentication, which significantly reduces the security risk associated with static credential files.

  * **mTLS** : this method is provider-agnostic and is a good fit if your organization already uses a Public Key Infrastructure (PKI) to manage TLS certificates for service identity. It allows clients to authenticate without a Google Cloud-specific identity. However, similar to using service account keys, this approach requires you to manage the lifecycle and distribution of long-lived credentials, such as client certificates.

  * **SASL/PLAIN with a service account key** : this method provides a direct way for an external client to authenticate as a Google Cloud identity. You download a service account key JSON file and use it in your client's SASL/PLAIN configuration. This method is generally discouraged for production workloads because it requires managing and securing a long-lived static credential on the client-side.




## Feature comparison between SASL and mTLS

The primary authentication mechanism for Managed Service for Apache Kafka is SASL (Simple Authentication and Security Layer), which integrates directly with Google Cloud's identity services. As a baseline, SASL authenticates clients using a Google Cloud IAM principal, such as a service account. For authorization, SASL provides flexibility: you can manage access to clusters using granular IAM roles and Kafka's Access Control Lists (ACLs).

In contrast, mTLS offers a provider-agnostic authentication method that does not rely on Google Cloud IAM. Instead, mTLS authenticates a client based on its TLS certificate, where the identity is derived from the certificate's Subject Name.

This distinction leads to a key difference in how authorization is handled. Unlike SASL principals, mTLS principals must be authorized using Kafka ACLs exclusively; they cannot be managed with Google Cloud IAM roles.

We strongly recommend configuring Kafka ACLs for your cluster. If no ACLs are set, the default Kafka behavior grants all authenticated principals—whether using SASL or mTLS—full access to the cluster. For more information about how to configure Kafka ACLs, see [Create a Managed Service for Apache Kafka ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls).

Managed Service for Apache Kafka supports mTLS authentication with client certificates issued by Certificate Authorities found in the [CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/overview). If your organization uses an external root of trust, you can integrate it by creating a subordinate CA within CA Service that chains up to your [external CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-sub-ca-from-external-ca).

The following table compares the features of the authentication methods.

Feature | SASL/OAUTHBEARER | SASL/PLAIN | mTLS  
---|---|---|---  
**Primary identity** | Google Cloud IAM Principal | Google Cloud IAM Principal | Certificate Subject Name  
**Credential type** | Application Default Credentials (ADC) or OAuth 2.0 token | Base64-encoded service account key | Client certificate and private key  
**Authorization method** | Google Cloud IAM roles or Kafka ACLs | Google Cloud IAM roles or Kafka ACLs | Kafka ACLs only  
**Use case** | Clients on Google Cloud; external clients using Workload Identity Federation | Simple clients, testing scenarios, or legacy systems where using a service account key is required. | Provider-agnostic; ideal for on-premises, multi-cloud, or existing PKI applications.  
**Client configuration** | JAAS config with specialized login handler class (Java) or a local auth server (non-Java) | JAAS config with standard PlainLoginModule (Java) | Keystore and truststore properties (For example—`security.protocol=SSL`)  
**Cluster availability** | All clusters | All clusters | Clusters created after June 24, 2025  
  
### Choose SASL versus mTLS

Your choice of authentication method is guided by your organization's security policies and existing infrastructure. For most use cases, we recommend using SASL with Google Cloud IAM.

SASL with Google Cloud IAM or Workload Identity Federation provides the most flexible and integrated experience for authentication and authorization. It uses Google Cloud's identity system as the single source of truth for managing permissions. Choose this path if you want to:

  * Centrally manage permissions for your Kafka clients using familiar Google Cloud IAM roles.

  * Avoid managing static credentials on clients.

  * Enable clients from other clouds like AWS, Azure or on-premises identity providers like Okta or ADFS to authenticate using Workload Identity Federation This method provides a secure, cloud-agnostic identity solution without needing to switch to a different authentication protocol.




Choose mTLS if your organization has a strict requirement for certificate-based authentication. This need arises when you are migrating an existing on-premises Kafka deployment that already uses TLS certificates for identity, or when corporate policy mandates client certificates for all applications. While mTLS provides strong transport-level security, remember that authorization for mTLS clients must be managed exclusively with Kafka ACLs, which is separate from Google Cloud IAM.

## Workflow for configuring SASL/PLAIN or SASL/OAUTHBEARER

Configuring a client to use SASL authentication with Managed Service for Apache Kafka involves granting permissions to the client's identity and then configuring the client application based on the chosen SASL mechanism. The following is an overview of the required workflow. For detailed instructions on how to configure SASL, see [Configure SASL authentication](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka).

  1. **Grant IAM permissions**. You must first grant the **Managed Kafka Client** (`roles/managedkafka.client`) role to the service account that your client uses for authentication. This role provides the necessary `managedkafka.clusters.connect` permission to connect to Kafka clusters within the project.

  2. **Configure the Kafka client**. The specific client configuration depends on whether you use the SASL/OAUTHBEARER or SASL/PLAIN mechanism.

**For SASL/OAUTHBEARER (recommended)** : this mechanism uses Application Default Credentials ADC. The configuration depends on your client's language:

     * **Java clients** : add the specialized Google Cloud authentication library to your application's classpath. Then, configure the Kafka client properties to use the provided `GcpLoginCallbackHandler` class, which automatically handles authentication using ADC.

The `GcpLoginCallbackHandler` is a class used with Kafka's OAUTHBEARER authentication mechanism, specifically designed for use with Managed Service for Apache Kafka. It handles the process of obtaining a JSON Web Token (JWT) from Google's identity provider, enabling Kafka clients to authenticate with the service using ADC.

     * **Non-Java clients** : run a provided local authentication server on the client's machine. This server uses ADC to fetch credentials and provides them to the Kafka client. The client is then configured to get its authentication token from this local server's endpoint.

**For SASL/PLAIN**

This mechanism uses a username and password combination. The client application must be configured to use the SASL_SSL security protocol, the PLAIN mechanism, and a JAAS configuration that specifies the `PlainLoginModule` class.

The username is the service account's email address. The password can be generated in one of two ways:

     * By base64-encoding a service account key JSON file.

     * By obtaining a short-lived access token.

  3. **Configure authorization**. After a client successfully authenticates using SASL, its access is controlled by permissions defined in IAM roles or Kafka ACLs on the cluster.




### SASL limitations

The SASL authentication method has the following limitations:

  * SASL authentication is inherently tied to IAM principals. It is not suitable for organizations that require a strict separation from Google Cloud identity or that uses non-Google identities, unless you configure Workload Identity Federation.

  * SASL does not use client certificates for authentication. It is not a direct fit for organizations that rely on an existing PKI to identify applications.




## Workflow for configuring mTLS

Configuring mTLS for Managed Service for Apache Kafka involves configuring certificate authorities, the Kafka cluster, and your Kafka clients. For detailed instructions on how to configure mTLS, see [Configure mTLS authentication](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls).

  1. **Configure Certificate Authorities (CAs)**. You must first create and configure CA pools in Certificate Authority Service (CA Service). If you create CA pools that are in a different project, make sure to grant the Managed Service for Apache Kafka service agent (`service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com`) permission to access these pools. You must create root and subordinate certificates inside the CA pools.

  2. **Configure the Kafka cluster**. Create or update your cluster to enable mTLS by providing the resource identifiers of your configured CA pools. We also recommended configuring the `ssl.principal.mapping.rules` broker property to create simplified principal names for use in ACLs. You can do so using Google Cloud CLI commands.

  3. **Configure the Kafka clients**. Obtain client certificates from your CAs and install them in your client's environment, for example, in a Java keystore. The client application must then be configured with the correct security protocol (SSL) and the location of its keystore to connect to the cluster's dedicated mTLS bootstrap port which is `9192`.

  4. **Monitor mTLS**. After setup, monitor the `managedkafka.googleapis.com/mtls_truststore_update_count` metric to verify the cluster is successfully refreshing its CA certificates from the CA Service pools, which it attempts to do periodically. You can also use [Cloud logging](https://docs.cloud.google.com/logging/docs/overview).




### mTLS limitations

The mTLS feature has the following limitations:

  * You can only use the mTLS feature on Managed Service for Apache Kafka clusters created after June 24, 2025.

  * You must configure authorization for mTLS principals using Kafka ACLs. You cannot use IAM role bindings to authorize mTLS clients.

  * The service only authenticates clients that present certificates managed by CA Service. However, you can integrate an external root of trust by creating a subordinate CA within CA Service that chains up to your external CA.

  * You can configure a cluster to trust a maximum of 10 CA pools.




## What's next

  * [Configure SASL authentication](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka)

  * [Configure mTLS authentication](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls)

  * [RFC 6750 for SASL/OAUTHBEARER](https://datatracker.ietf.org/doc/html/rfc6750)

  * [RFC 4422 for SASL/PLAIN](https://datatracker.ietf.org/doc/html/rfc4422)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
