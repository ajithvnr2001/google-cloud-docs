---
url: https://docs.cloud.google.com/certificate-authority-service/docs/faqs/
title: Frequently asked questions \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:11.986864+00:00
---

# Frequently asked questions  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/faqs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Resources ](https://docs.cloud.google.com/certificate-authority-service/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Frequently asked questions

## What is Certificate Authority Service?

Certificate Authority Service is a highly available, scalable Google Cloud service that enables customers to simplify, automate, and customize the deployment, management, and security of private certificate authorities (CAs) while staying in control of their private keys.

## What are the common use cases for Certificate Authority Service?

Given below are some common use cases for CA Service.

  * **Workload identities** : Leverage APIs to get certificates for applications or use certificates in applications, containers, systems, and other resources.
  * **Enterprise scenarios** : Use certificates for VPN, Chrome Enterprise Premium, signing documents, WiFi access, email, smartcard, and more.
  * **Centralized certificate issuance and management** : Configure GKE Enterprise Service Mesh to use CA Service.
  * **IoT and mobile device identity** : Issue TLS certificates as identity for endpoints.
  * CI/CD channel, Binary Authorization, Istio, and Kubernetes.



## Which compliance standards does CA Service support?

For information, see [Security and Compliance](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-compliance).

## Which locations can we create CA Service resources in?

CA Service resources can be created in one of many locations. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).

## Does CA Service support a global PKI under a single root?

Yes, provided the root CA lives in a single region. However, you can create multiple issuing CAs in different regions that chain up to the same root.

## Are labels supported for CAs?

Yes, you can associate labels to CA pools and CAs during create and update operations.

For information on updating labels on a CA pool, see [Updating labels on a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/operations-ca-pool#update-labels).

For information on updating labels on a CA, see [Updating labels on a CA](https://docs.cloud.google.com/certificate-authority-service/docs/updating-certificate-authorities#update-labels).

## Is it possible to use Cloud Monitoring to track certificate creation and CA expiration? Is it possible to generate Pub/Sub events for them?

Yes, you can monitor all of these events. CA Service does not natively support [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) but you can configure it using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). For more information, see [Using Cloud Monitoring with CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/monitoring).

## How long are unactivated CAs retained?

Subordinate CAs are created in the `AWAITING_USER_ACTIVATION` state, and they are set to the `STAGED` state after activation. If a subordinate CA is still in the `AWAITING_USER_ACTIVATION` state 30 days after it has been created, it is deleted.

For information about the various states a CA is in through its lifecycle, see [Certificate authority states](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states).

## What access controls does CA Service support for certificate issuance?

CA Service supports setting IAM policies on a CA pool to control who can issue certificates. A CA admin can attach an issuance policy to a CA pool. This issuance policy defines restrictions on the type of certificates that the CAs in a CA pool can issue. These restrictions include placing limits on domain name, extensions, and certificate validity period, among other things.

For more information on how to configure an issuance policy on a CA pool, see [Using an issuance policy](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy).

For information on how to configure the necessary IAM policies for creating and managing CA Service resources, see [Configuring IAM policies](https://docs.cloud.google.com/certificate-authority-service/docs/configuring-iam).

## Does CA Service support multi-region Cloud KMS keys?

No, CA Service does not support multi-region Cloud KMS keys.

## Will CA Service ever throttle my requests? What is the target QPS for CA Service?

Yes, there exists a throttling mechanism for CA Service. For more information, see [Quotas and limits](https://docs.cloud.google.com/certificate-authority-service/quotas).

## Does CA Service support VPC Service Controls?

Yes, CA Service supports VPC Service Controls. For more information, see [Supported products and limitations > Certificate Authority Service](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cas) and [Security and Compliance](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-compliance).

## How are PEM encoded public keys supposed to be used with REST APIs?

PEM encoded public keys can only be used with REST APIs after they have been Base64 encoded.

## Can preview stage APIs still be used after CA Service announces general availability (GA)?

Yes, preview APIs can still be used for a short period after CA Service announces GA. This period is only intended for customers to smoothly transition to using the latest APIs and will be short-lived with limited support. We recommend that customers migrate to using the GA APIs as soon as they are available.

## How can resources created during the preview period be accessed after CA Service announces general availability (GA)?

You cannot view or manage resources created during the preview period using the Google Cloud console. To manage resources created during preview, use the preview APIs or the preview `gcloud` commands. The preview APIs are accessible through the `https://privateca.googleapis.com/v1beta1/` endpoint. The preview `gcloud` commands are accessible through `gcloud privateca beta`. For more information about `gcloud privateca beta` commands, see [gcloud privateca beta](https://docs.cloud.google.com/sdk/gcloud/reference/beta/privateca).

## Can a subordinate CA be created with the same subject and key as another CA in its chain?

No, a subordinate CA cannot have the same subject and key as the root CA, or any other CA in its chain. [RFC 4158](https://datatracker.ietf.org/doc/html/rfc4158#section-2.2) recommends that subject names and public key pairs are not repeated in paths.

## Are customer-managed Cloud KMS keys the same as CMEK?

No, the [customer-managed Cloud KMS keys](https://docs.cloud.google.com/certificate-authority-service/docs/managed-resources#customer-managed) supported in CA Service for the CA signing keys aren't the same as [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek#cmek) that are used to encrypt data at rest within supported Google Cloud services.

CA Service supports CMEK for encrypting certain fields in certificates, such as the certificate subject and Subject Alternative Names (SANs). For more information, see [Customer-managed encryption keys (CMEK) and CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool#cmek).

## Can resource names be reused after the resource is deleted?

No, resource names such as the names of CA pools, CAs, and certificate templates can't be reused in a new resource after the original resource is deleted. For example, if you create a CA pool called `projects/Charlie/locations/Location-1/caPools/my-pool`, and then delete the CA pool, you can't create another CA pool called `my-pool` in the project `Charlie` and location `Location-1`.

## Does CA Service generate key pairs for certificates?

No, CA Service doesn't generate key pairs for certificates. CA Service never interacts with your private keys, helping to enforce non-repudiation. Only the client that generated the certificate request should access the certificate's private key.

To request a certificate, you must perform the following steps on the client machine:

  1. Generate a new key pair consisting of a public key and a private key.
  2. Securely store the private key.
  3. Send only the public key to CA Service as part of the certificate request.



Some client tools, such as the gcloud CLI, provide a `--generate-key` flag that generates the key pair locally and sends only the public key to CA Service.

## What's next

  * Learn about the [known limitations](https://docs.cloud.google.com/certificate-authority-service/docs/known-limitations).
  * Read the [release notes](https://docs.cloud.google.com/certificate-authority-service/docs/release-notes).
  * Learn how you can [get support](https://docs.cloud.google.com/certificate-authority-service/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
