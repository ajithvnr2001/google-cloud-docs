---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-identity-issuance-usage/
title: Verify identity issuance and usage \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:31.395141+00:00
---

# Verify identity issuance and usage  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-identity-issuance-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Verify identity issuance and usage Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note:** This document uses a [general availability](https://cloud.google.com/products#product-launch-stages) feature named _GKE control plane authority_ that's only available for eligible Google Cloud customers. To request access to this feature, contact your Google Cloud account team.

This page shows you how to use logs to check the issuance and usage of Kubernetes identities, in the form of certificates and service account tokens, by the Google Kubernetes Engine (GKE) cluster control plane. **This verification is entirely optional and is not required to secure your control plane.**

This guide is intended for security administrators and platform owners who have specific organizational compliance or policy requirements for control over credential issuance and signing. You should already have [set up self-managed keys and CAs](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/run-your-own-cas-keys) with GKE control plane authority.

You should already be familiar with the following concepts:

  * [CA Service logs](https://docs.cloud.google.com/certificate-authority-service/docs/audit-logging)
  * [Cloud KMS logs](https://docs.cloud.google.com/kms/docs/audit-logging)
  * [Kubernetes audit logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging-container)
  * [X.509 certificates](https://en.wikipedia.org/wiki/X.509)



This page describes one part of a set of optional control plane features in GKE that lets you perform tasks like verifying your control plane security posture or configuring encryption and credential signing in the control plane using keys that you manage. For details, see [About GKE control plane authority](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority).

By default, Google Cloud applies various security measures to the managed control plane. This page describes _optional_ capabilities that give you more visibility or control over the GKE control plane.

## About identity issuance logs

The GKE identity issuance logs are [control plane audit logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#control-plane-logs) that record when the control plane issues credentials and when those credentials are used in the cluster. You can use these logs to track the lifetime of a credential, including issuance and usage, by correlating the identity issuance logs with Cloud KMS, Certificate Authority Service, and Kubernetes API logs. GKE identity issuance logs are enabled when using GKE control plane authority. These logs track the issuance and usage of the following types of credentials:

  * X.509 certificates
  * Cluster JSON Web Tokens (JWTs)



### X.509 certificates

Kubernetes uses X.509 certificates for [client certificate authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#x509-client-certificates). To issue certificates, the Kubernetes control plane sends an approved [CertificateSigningRequest](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/) to a certificate authority (CA) in CA Service. The CA then issues a certificate using the corresponding key in Cloud KMS to sign the certificate digest.

The **Kubernetes API server logs** contain certificate signature details for any Kubernetes API call that was authenticated with a certificate. The credential ID entry in the log has the following form:
    
    
    "authentication.k8s.io/credential-id": "X509SHA256=CERTIFICATE_HASH"
    

The `CERTIFICATE_HASH` value is the SHA256 hash for the certificate, which you can use to trace the lifecycle of the certificate.

You can use Kubernetes API server certificate logs to trace the lifecycle of the certificate by correlating logs from the following services:

  * **GKE identity issuance logs** : Use the `protoPayload.metadata.credentialId` query to find specific GKE identity issuance logs based on the credential ID from the Kubernetes API server logs. Then use the `protoPayload.metadata.certificateFingerprint` field from the GKE identity issuance log to correlate the identity issuance logs with the CA Service logs.
  * **CA Service logs** : Find the certificate issuance log entry, which contains the following IDs: 
    * `cert_fingerprint.sha256_hash`: the SHA256 hash of the signed certificate. Use this ID to match logs with GKE and Kubernetes API events.
    * `tbs_certificate_digest`: a hash of the certificate contents that were sent to be signed by a Cloud KMS key. Use this ID to match logs with Cloud KMS logs.
  * **Cloud KMS signing logs** : Use the `tbs_certificate_digest` value from the CA Service log to confirm that the expected Cloud KMS key signed the certificate.



### JSON Web Tokens (JWTs)

Signed JWTs (JSON Web Tokens) are used as [bearer tokens for entities in the cluster](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens), like Kubernetes service accounts, when authenticating requests to the Kubernetes API. When a Pod is created that uses a specific service account, Kubernetes creates a JWT and mounts it in the Pod. When you use GKE control plane authority to run your own keys and CAs, this JWT is signed and later verified using the service account signing key in Cloud KMS.

The Kubernetes API server logs contain token signature details for any Kubernetes API call that was authenticated with a JWT. The token signature entry in the log has the following form:
    
    
    "authentication.kubernetes.io/credential-id":"JTI=JWT_ID"
    

The `JWT_ID` value is a string that identifies the JWT that was used in the Kubernetes API call.

You can use the JWT ID from Kubernetes API server logs to trace the lifecycle of a JWT by correlating the following logs:

  * **GKE identity issuance logs** : Use the JWT ID from the Kubernetes API server logs to find specific JWT issuance entries. Each entry also contains the `toBeSignedDigest` field, the value of which can match Cloud KMS logs.
  * **Cloud KMS signing logs** : Use the value of the `toBeSignedDigest` field from the GKE identity issuance logs to confirm that the expected Cloud KMS key signed the JWT.



## Pricing

In this document, you use the following billable components of Google Cloud: 

  * [ GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [ Cloud KMS](https://docs.cloud.google.com/kms/pricing)
  * [ CA Service](https://docs.cloud.google.com/certificate-authority-service/pricing)
  * [ Cloud Logging](https://docs.cloud.google.com/stackdriver/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. [Configure your GKE cluster control plane with self-managed CAs or keys](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/run-your-own-cas-keys).

  2. Enable the following Cloud Audit Logging Service APIs:

     * For [Cloud KMS, turn on Data Access audit logs](https://docs.cloud.google.com/kms/docs/audit-logging#permission-type) of type _Data Read_.
     * For [CA Service, turn on Data Access audit logs](https://docs.cloud.google.com/certificate-authority-service/docs/audit-logging) of types _Admin Read_ and _Data Write_.



### Required roles

To get the permissions that you need to access identity issuance logs, ask your administrator to grant you the following IAM roles on your project: 

  * Perform all actions in Logging: **Logging Admin** (`roles/logging.admin`). 
  * View logs: **Private Logs Viewer** (`roles/logging.privateLogViewer`). 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Requirements and limitations

The following requirements and limitations apply:

  * You must use GKE version 1.31.1-gke.1846000 or later.
  * Identity issuance logs are recorded as Cloud Audit Logs logs and have a set retention period of 400 days. The retention period is not configurable, but you can [route your system event audit logs to other destinations](https://docs.cloud.google.com/logging/docs/routing/overview) for longer retention periods.



## Verify certificates

You can use GKE control plane authority identity issuance logs to confirm that a certificate was successfully issued or used. You can use any of the following logs, or a combination of logs, to confirm information about certificate issuance and use:

**Certificate logs**  
---  
Kubernetes API log for certificate use | Logs the certificate signature details whenever the certificate is used against the Kubernetes API.  
GKE log for certificate issuance operations | Logs all certificate issuance operations as a _System Event_ audit log. These logs are enabled by default on any cluster that uses GKE control plane authority user-managed keys or CAs.  
CA Service audit log | Logs an entry whenever a certificate is issued.  
Cloud KMS audit log | Logs an entry whenever a digest is signed, in response to a signing request from CA Service.  
  
### Verify certificate usage with Kubernetes API logs

To find log entries for API calls that were authenticated using certificates, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

  2. Paste the following expression into the query editor field:
         
         log_id("cloudaudit.googleapis.com/activity")
         resource.type="k8s_cluster"
         labels."authentication.kubernetes.io/credential-id":"X509SHA256="
         

  3. Click **Run query**.

This query returns all Kubernetes API server logs that have an associated X.509 certificate. Find specific log entries to investigate by using your security tooling or by checking the logs manually.




To correlate these logs with other log types, find the following field:
    
    
    "authentication.k8s.io/credential-id":"CREDENTIAL_ID"
    

The `CREDENTIAL_ID` value is the identifier that you can use to correlate logs from GKE, CA Service, and Cloud KMS. The `CREDENTIAL_ID` has the form `"X509SHA256=CERTIFICATE_HASH"`.

### Verify certificate issuance with GKE logs

To find GKE log entries for certificate issuance events, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Paste the following expression into the query editor field:
         
         logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
         resource.type="gke_cluster"
         protoPayload.serviceName="container.googleapis.com"
         protoPayload.metadata.credentialId="CREDENTIAL_ID"
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `CREDENTIAL_ID`: the `CREDENTIAL_ID` from the Verify certificate usage with Kubernetes API logs section.
  3. Click **Run query**.




### Verify certificate issuance with CA Service logs

To find CA Service logs that match the GKE certificate issuance events, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Paste the following expression into the query editor field:
         
         resource.type="audited_resource"
         protoPayload.serviceName="privateca.googleapis.com"
         protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificate"
         protoPayload.response.certificate_description.cert_fingerprint.sha256_hash="CERTIFICATE_HASH"
         

Replace `CERTIFICATE_HASH` with the `CERTIFICATE_HASH` from the Verify certificate usage with Kubernetes API logs section. Ensure that you omit the `X509SHA256=` prefix from the hash.

  3. Click **Run query**.

This query returns a log that contains a `tbs_certificate_digest: DIGEST_VALUE` field in the certificate description response section.




You can use the `DIGEST_VALUE` to match Cloud KMS signing logs for the certificate.

### Verify certificate issuance with Cloud KMS signing logs

To find Cloud KMS signing events for the CA Service certificate issuance events, complete the following steps:

**Note:** Cloud KMS logs don't distinguish between certificates and JWTs, so the log entries for both are identical.

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Paste the following expression into the query editor field:
         
         protoPayload.request.digest.sha256="DIGEST_VALUE"
         protoPayload.@type="type.googleapis.com/google.cloud.audit.AuditLog"
         protoPayload.methodName="AsymmetricSign"
         protoPayload.serviceName="cloudkms.googleapis.com"
         

Replace `DIGEST_VALUE` with the digest value from the Verify certificate issuance with CA Service logs section.

  3. Click **Run query**.

This query returns the logs for certificate issuance events. Cloud KMS logs don't distinguish between certificates and JWTs, so the log entries for both are identical.




## Verify tokens

You can use GKE control plane authority identity issuance logs and Cloud KMS signing logs to confirm that a JSON Web Token (JWT) was successfully issued.

Initiating the traceback of the token issuance event typically starts with monitoring the Kubernetes API log for service account activity. After you identity an activity log needing further investigation, you can use the following logs to confirm information about credential issuance and usage:

**JWT logs**  
---  
Kubernetes API log for JWT use | Logs the JWT signature details whenever a JWT is used against the Kubernetes API.  
GKE log for JWT issuance operations | Logs all token issuance operations as a System Event audit log. These logs are enabled by default on any cluster using GKE control plane authority user-managed keys or CAs.  
Cloud KMS audit log | Logs an entry whenever a token is signed and issued.  
  
### Verify token usage with Kubernetes API server logs

To find log entries for token usage events, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Paste the following expression into the query editor field:
         
         log_id("cloudaudit.googleapis.com/activity")
         resource.type="k8s_cluster"
         labels."authentication.kubernetes.io/credential-id":"JTI="
         

  3. Click **Run query**.

This query returns all Kubernetes API server logs that have an associated JWT. Find specific log entries to investigate by using your security tooling or by checking the logs manually.




To correlate these logs with other log types, find the following field:
    
    
    "authentication.k8s.io/credential-id": "JTI=JWT_ID"
    

The `JWT_ID` is the token identifier that you can use to correlate logs from GKE and Cloud KMS.

### Verify token issuance with GKE logs

To find log entries for token issuance events, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Paste the following expression into the query editor field:
         
         resource.type="gke_cluster"
         logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
         protoPayload.methodName="google.cloud.gkeauth.v1.Auth.SignServiceAccountJWT"
         protoPayload.metadata.credentialId="JTI=JWT_ID"
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `JWT_ID`: the JWT ID from the Verify token usage with Kubernetes API server logs section.
  3. Click **Run query**.

This query returns logs that contain a `toBeSignedDigest` field.




You can use the `toBeSignedDigest` value to find Cloud KMS signing events.

### Verify token issuance with Cloud KMS signing logs

To find log entries for signed digests, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

  2. Paste the following expression into the query editor field:
         
         protoPayload.request.digest.sha256="DIGEST_VALUE"
         protoPayload.@type="type.googleapis.com/google.cloud.audit.AuditLog"
         protoPayload.methodName="AsymmetricSign"
         protoPayload.serviceName="cloudkms.googleapis.com"
         

Replace `DIGEST_VALUE` with the value in the `toBeSignedDigest` field, from the Verify token issuance with GKE logs section.

  3. Click **Run query**.

This query returns the logs for certificate issuance events. Cloud KMS logs don't distinguish between certificates and JWTs, so the log entries for both are identical.




## What's next

  * Learn about [control plane security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/control-plane-security).
  * Learn about [administrative access for Google employees](https://docs.cloud.google.com/docs/security/overview/whitepaper#administrative_access_for_google_employees).
  * Learn how to [configure logging and monitoring for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/config-logging-monitoring).
  * Learn how to [configure field-level access to logs](https://docs.cloud.google.com/logging/docs/field-level-acl).
  * Learn about [logging usage limits](https://docs.cloud.google.com/logging/quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
