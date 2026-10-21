---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/root-ca-rotation/
title: About the Apigee root CA certificate and rotation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:07:12.615234+00:00
---

# About the Apigee root CA certificate and rotation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/root-ca-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  About the Apigee root CA certificate and rotation Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes the Apigee root certificate authority (CA) certificate that secures TLS connections to the Apigee runtime, and explains the rotation process. It also lists the access patterns that are affected by a rotation and the steps that you should take to prepare your applications.

**At a Glance:** Action is only required if your clients connect directly to the Apigee runtime (for example, using Internal routing TLS Option 2 or a direct TCP connection). If your traffic flows through a customer-managed external or internal load balancer that terminates TLS, no action is required. 

## About the root CA certificate

Each Apigee organization has a Google-managed root CA certificate that issues the server certificate used by the Apigee runtime ingress for TLS termination. When a client opens an HTTPS connection to an Apigee instance, the server presents a certificate that chains to this root CA. Clients that validate the server certificate must trust the root CA, either implicitly (when traffic flows through a customer-managed load balancer that terminates TLS) or explicitly (when the client connects directly to the Apigee runtime).

The root CA certificate is exposed in the [`organizations.get`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get) API response in the `caCertificates[]` field. The field is an array because, during a rotation, both the current and the upcoming root CA certificates are returned at the same time so that clients can trust both before the cutover.

**Note:** The deprecated `caCertificate` (singular) field returns only one certificate and does not surface the upcoming certificate during a rotation. Update any tooling that reads `caCertificate` to read `caCertificates[]` instead. 

## Why the root CA certificate is rotated

The Apigee root CA certificate has a long but finite validity period (typically 10 years). It is rotated before it expires so that:

  * The certificate that secures the Apigee runtime never expires while in use.
  * The internal communication channels between Apigee components continue to work without interruption.



Rotation is a routine, planned operation. Apigee runs it on a schedule that Google Cloud controls. You do not initiate the rotation, and the rotation does not, by itself, change the Apigee runtime endpoint or the Apigee API surface.

## Rotation stages and timeline

Apigee rotates the root CA certificate in four stages. Each stage is gradual: it is applied region-by-region across your organization and takes time to complete. The table below describes the customer-visible effect of each stage and the typical time at which it begins, measured relative to the expiry date of the current root CA.

Stage | Typical timing | What's in `caCertificates[]` | What happens  
---|---|---|---  
**1\. New certificate published** | About 1 year before the current certificate expires | Current and new (both) | Apigee generates the new root CA certificate and adds it to the truststore of every Apigee-owned component. The new certificate also appears in the [`organizations.get`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get) response so that you can fetch and stage it. The Apigee runtime continues to present a server certificate signed by the current root CA, so existing clients are not affected yet. Apigee sends a customer notification when this stage starts.  
**2\. Leaf certificate cutover** | About 60 days before the current certificate expires | Current and new (both) | The Apigee runtime starts presenting a new server (leaf) certificate that is signed by the new root CA. Clients that trust only the current root CA fail TLS validation after this stage completes in their region. Clients that trust both certificates (or only the new one) continue working. Apigee sends a customer notification when this stage starts.  
**3\. Old certificate withdrawn** | About 30 days before the current certificate expires | New only | Apigee removes the old root CA from internal truststores and stops returning it from [`organizations.get`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get). Clients that still trust only the old root CA cannot connect. Apigee sends a customer notification when this stage starts.  
**4\. Rotation complete** | At the original expiry date | New only | Apigee permanently deletes the old root CA and the rotation is finished. The new root CA is now the only root CA, and a new ~10-year cycle begins. Apigee sends a customer notification when this stage completes.  
**Note:** Each stage takes time to roll out across all instances and regions in your organization (typically minutes to a few hours per instance). During a stage rollout, instance management operations are paused for that organization. 

## Who is affected by a rotation

Whether a rotation requires action from you depends on how clients reach your Apigee runtime:

Access pattern | Action required? | Why  
---|---|---  
[External routing (MIG)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#externalmig) with a Google Cloud external Application Load Balancer  | No | Your external load balancer terminates TLS using a certificate that you manage. Clients trust your certificate, not the Apigee root CA. The rotation has no effect on these clients.  
[Internal routing (VPC)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#internal-routing-vpc), TLS Option 1 (internal HTTPS Application Load Balancer)  | No | Your internal load balancer terminates TLS using a certificate that you manage. Clients trust your certificate, not the Apigee root CA. The rotation has no effect on these clients.  
[Internal routing (VPC)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#internal-routing-vpc), TLS Option 2 (internal default fully qualified domain name)  | Yes | Clients connect directly to the Apigee-managed internal load balancer and validate the Apigee-issued server certificate. Each client must trust the new root CA before the rotation cutover.  
Direct TCP connection to the runtime instance ingress IP (for example, through an internal TCP load balancer)  | Yes | Clients validate the Apigee-issued server certificate. Each client must trust the new root CA before the rotation cutover.  
Non-TLS option (the `curl` `-k` flag, or any client that skips certificate validation)  | No | The client does not validate the server certificate, so the rotation has no functional effect. This option is not recommended outside of test environments.  
**Caution:** If your application stores the Apigee root CA in an OS truststore, an application-managed truststore, a sidecar, or a service mesh trust bundle, you must add the new root CA to every such truststore before the rotation cutover. Otherwise, the TLS handshake fails after the cutover and your client receives an error such as `x509: certificate signed by unknown authority` or `SSL_ERROR_BAD_CERT_DOMAIN`. 

## How to prepare for a rotation

If you use one of the access patterns that requires action, follow these steps before the rotation cutover date that you receive in your rotation notification.

**Prerequisites:** The command line examples below require the `curl`, `jq`, `awk`, `base64`, and `openssl` utilities to be installed on your system. 

### Step 1: Discover the Apigee runtime instances

List the Apigee runtime instances in your organization. Each instance has a dedicated ingress IP, which is the host that direct-connect clients reach.
    
    
    # Ensure $AUTH and $PROJECT_ID are set in your environment
    curl -H "$AUTH" \
      https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances \
      | jq -r '.instances[] | "\(.name)\t\(.host)"'

If your clients connect to a host other than these IPs (for example, your own DNS name in front of an internal load balancer), use that host instead.

### Step 2: Fetch the current and upcoming root CA certificates

Read the `caCertificates[]` field from `organizations.get`. During a rotation, this array contains both the current and the new root CA, each base64-encoded:
    
    
    curl -H "$AUTH" \
      https://apigee.googleapis.com/v1/organizations/$PROJECT_ID \
      | jq -r '.caCertificates[]' \
      | awk '/-----BEGIN/{i++}{print > ("ca_" i ".b64")}'

Decode each entry to PEM format and inspect the validity period to identify the new certificate:
    
    
    for f in ca_*.b64; do
      base64 -d "$f" > "${f%.b64}.crt"
      echo "==> ${f%.b64}.crt"
      openssl x509 -in "${f%.b64}.crt" -noout -subject -issuer -dates
    done

The certificate with the later `notAfter` date is the new root CA.

### Step 3: Add the new root CA to your truststores

Add the new root CA certificate to every client truststore that currently trusts the Apigee root CA. Keep the current root CA in place until the cutover is complete, so that connections continue to work through the cutover window. After the cutover, you can remove the old root CA from your truststores.

The exact procedure depends on the client. Common cases include:

  * Adding the certificate to the OS-level truststore (for example, `/etc/ssl/certs/` on Debian-based systems followed by `update-ca-certificates`).
  * Adding the certificate to an application-managed truststore (for example, a Java `cacerts` keystore, an Nginx `ssl_trusted_certificate` bundle, or an Envoy `validation_context` trust bundle).
  * Adding the certificate to a Kubernetes `Secret` or `ConfigMap` that is mounted into your workload pods.



### Step 4: Verify the connection works with the new root CA

After you stage the new root CA, verify that an HTTPS request to the Apigee runtime succeeds when you trust only the new certificate:
    
    
    # Ensure $ENV_GROUP_HOSTNAME and $INTERNAL_LOAD_BALANCER_IP are set
    curl -is -H "Host: $ENV_GROUP_HOSTNAME" \
      https://example.$PROJECT_ID.apigee.internal/PROXY_BASEPATH \
      --cacert NEW_CA_FILE \
      --resolve example.$PROJECT_ID.apigee.internal:443:$INTERNAL_LOAD_BALANCER_IP

If this command succeeds, your client is ready for the cutover. If it fails, the client does not yet trust the new root CA — revisit Step 3.

## Example: Internal routing (VPC), TLS Option 2

This example demonstrates the rotation steps for the access pattern documented in [Internal routing (VPC)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#internal-routing-vpc), TLS Option 2, where the client connects directly to the Apigee internal load balancer and validates the Apigee self-signed certificate. This is the access pattern most commonly affected by a rotation.

Before the cutover:

  1. Get the IP of the Apigee internal load balancer: 
         
         export INTERNAL_LOAD_BALANCER_IP=$(curl -H "$AUTH" \
           https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances -s \
           | jq -r '.instances[0].host')

  2. Fetch the current and new root CAs into separate files and identify the new one: 
         
         curl -H "$AUTH" \
           https://apigee.googleapis.com/v1/organizations/$PROJECT_ID \
           | jq -r '.caCertificates[]' \
           | awk '/-----BEGIN/{i++}{print > ("ca_" i ".b64")}'
         
         for f in ca_*.b64; do
           base64 -d "$f" > "${f%.b64}.crt"
         done
         
         # Identify the new root CA (latest notAfter):
         openssl x509 -in ca_1.crt -noout -dates
         openssl x509 -in ca_2.crt -noout -dates

  3. Build a combined truststore that contains both the current and the new root CA, and use it for your test request: 
         
         cat ca_1.crt ca_2.crt > cacert-combined.crt
         
         curl -is -H "Host: $ENV_GROUP_HOSTNAME" \
           https://example.$PROJECT_ID.apigee.internal/PROXY_BASEPATH \
           --cacert cacert-combined.crt \
           --resolve example.$PROJECT_ID.apigee.internal:443:$INTERNAL_LOAD_BALANCER_IP

If this request succeeds, deploy `cacert-combined.crt` as your client truststore. The combined truststore continues to validate the current certificate today and will validate the new certificate after the cutover.




After the cutover (typically within a few days of the cutover date), confirm the rotation by verifying that the connection still succeeds when you trust only the new certificate:
    
    
    curl -is -H "Host: $ENV_GROUP_HOSTNAME" \
      https://example.$PROJECT_ID.apigee.internal/PROXY_BASEPATH \
      --cacert NEW_CA_FILE \
      --resolve example.$PROJECT_ID.apigee.internal:443:$INTERNAL_LOAD_BALANCER_IP

When this request succeeds, you can safely remove the old root CA from your truststore.

## Notifications

Apigee sends a notification to the project owners and organization owners of your Google Cloud project at the start of each rotation stage. Each notification includes the stage name, the date the stage will be applied to your organization, and a link to this page.

Notification | Recommended customer action  
---|---  
**1\. New certificate published**  
(~1 year before expiry) | Fetch the new root CA from `caCertificates[]` and add it to every client truststore that currently trusts the Apigee root CA. See How to prepare for a rotation.  
**2\. Leaf certificate cutover**  
(~60 days before expiry) | Confirm that all of your clients trust the new root CA before this stage is applied to your region. After this stage, clients that trust only the old root CA cannot connect.  
**3\. Old certificate withdrawn**  
(~30 days before expiry) | Once this stage has been applied to all your regions, you can safely remove the old root CA from your client truststores.  
**4\. Rotation complete**  
(at the original expiry date) | No action required. The old root CA has been permanently deleted and the new root CA is the only root CA for your organization.  
  
If you do not receive rotation notifications and you use one of the access patterns listed in Who is affected by a rotation, contact [Apigee support](https://docs.cloud.google.com/apigee/docs/support) to confirm the notification recipients for your organization.

## What's next

  * Review the [Options for configuring TLS](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/options-configuring-tls) to understand all of the TLS termination options in Apigee.
  * Review [Calling an API proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies) for the full set of internal-access call patterns.
  * See the [`organizations.get`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get) API reference for the full schema of the `caCertificates[]` field.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
