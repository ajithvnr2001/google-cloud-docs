---
url: https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp/
title: Use frontend mTLS with Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:08.877133+00:00
---

# Use frontend mTLS with Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Use frontend mTLS with Secure Web Proxy Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can configure frontend mutual TLS (mTLS) on Secure Web Proxy to enhance the security of your workloads, such as AI agents. Secure Web Proxy uses frontend mTLS to verify client identities through certificates.

This integration lets you use validated client identities in Secure Web Proxy [authorization policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies) to enforce granular access control for outbound traffic.

**Important:** Secure Web Proxy supports frontend mTLS for client authentication only when you deploy the proxy in explicit proxy routing mode.

## How it works

The following steps explain how Secure Web Proxy uses frontend mTLS to secure outbound traffic:

  * **Explicit proxy connection** : you can configure the client to use Secure Web Proxy as its explicit proxy. The client initiates an HTTPS CONNECT request to the Secure Web Proxy frontend, instead of directly connecting to the internet.

  * **Mutual TLS handshake** : during the connection setup, Secure Web Proxy and the client perform a mTLS handshake at the proxy frontend. The proxy uses a configured `TrustConfig` resource to validate the client's certificate, whereas the client validates the proxy's server certificate.

  * **Identity extraction** : after a successful handshake, Secure Web Proxy extracts unique identity attributes, such as `URI_SAN`, directly from the validated client certificate.

  * **Identity-based authorization** : Secure Web Proxy evaluates the outbound request against your configured authorization policies. To determine whether the request is authorized, the proxy uses the client's identity, which was cryptographically verified during the mTLS handshake.

  * **Secure outbound traffic** : once authorized and if there's a matching rule for an external destination, Secure Web Proxy fulfills the request to the destination.




## Key benefits

Configuring frontend mTLS on Secure Web Proxy provides the following security and operational benefits:

  * **Enhanced security** : achieve zero-trust access by requiring frontend mTLS authentication for all outbound traffic. This ensures that only workloads with a verified identity can establish a connection with the proxy to access external services.

  * **Simplified workload configuration** : use the explicit proxy routing mode for Secure Web Proxy to leverage the proxy's ability to intercept and authenticate requests.

  * **Granular control** : enforce detailed, identity-aware policies to determine what external services each specific workload can access.




## Example use case: Validate the identity of your workloads

In compliance-heavy and regulated industries such as the banking sector, verifying a request's network location isn't sufficient to prevent unauthorized data access. By configuring frontend mTLS on Secure Web Proxy, organizations can move to a cryptographically verified identity model. This ensures that every workload, whether a virtual machine (VM) instance or an AI agent, must prove its specific identity by using a trusted certificate.

This approach lets administrators enforce identity-based guardrails that protect sensitive outbound paths. For example, a bank can ensure that only a specific authenticated payment-processing workload can reach an external financial gateway.

## Configure frontend mTLS authentication for Secure Web Proxy

This section describes the steps to configure frontend mTLS authentication for your Secure Web Proxy instance.

### Before you begin

  * Review the [Manage trust configs](https://docs.cloud.google.com/certificate-manager/docs/trust-configs) page.

  * [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk)

  * [Enable the required APIs](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#enable-apis)

  * Request your Identity and Access Management administrator to grant you the following roles:

    * [Certificate Manager Owner role](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.owner) (`roles/certificatemanager.owner`)
    * [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
    * [Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)
    * [Networksecurity Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.admin) (`roles/networksecurity.admin`)
  * You must have a [Secure Web Proxy instance that you've deployed in explicit proxy routing mode](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart).




### Create the root and intermediate certificates

This section shows how to use [OpenSSL](https://www.openssl.org/docs/) to generate a root certificate authority (CA) certificate (the trust anchor) and an optional intermediate CA certificate. Secure Web Proxy uses these certificates to verify the client certificates that workloads present during the frontend mTLS handshake process. This manual process is intended for testing and development environments to provide the trust anchor that Secure Web Proxy needs to verify client certificates.

**Important:** For production environments, we recommend that you don't use self-signed certificates. Instead, use a managed certificate authority, such as Certificate Authority Service, to issue and manage certificates.

A root certificate resides at the top of the certificate chain, whereas an intermediate certificate acts as a bridge in the chain of trust back to the root. The intermediate certificate is cryptographically signed by the root certificate. When Secure Web Proxy receives a client certificate, it validates the identity by establishing a chain of trust from the client certificate back to the configured trust anchor.

Use the following commands to create the root and intermediate certificates. Although the intermediate certificate is optional, this configuration uses it to [sign the client certificate](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm#sign-client-cert) to show a multi-tier certificate hierarchy.

  1. Create an [OpenSSL configuration file](https://github.com/openssl/openssl/blob/master/apps/openssl.cnf).
         
         cat > example.cnf << EOF
         [req]
         distinguished_name = empty_distinguished_name
         
         [empty_distinguished_name]
         # Kept empty to allow setting via -subj command-line argument.
         
         [ca_exts]
         basicConstraints=critical,CA:TRUE
         keyUsage=keyCertSign
         extendedKeyUsage=clientAuth
         EOF
         

  2. Create a self-signed X.509 root certificate (`root.cert`) and private key (`root.key`).
         
         openssl req -x509 \
             -new -sha256 -newkey rsa:2048 -nodes \
             -days 3650 -subj '/CN=root' \
             -config example.cnf \
             -extensions ca_exts \
             -keyout root.key -out root.cert
         

  3. Create the certificate signing request (`int.req`) for the intermediate certificate.
         
         openssl req -new \
             -sha256 -newkey rsa:2048 -nodes \
             -subj '/CN=int' \
             -config example.cnf \
             -extensions ca_exts \
             -keyout int.key -out int.req
         

  4. Sign the certificate signing request (CSR) to create the X.509 intermediate certificate (`int.cert`).
         
         openssl x509 -req \
             -CAkey root.key -CA root.cert \
             -set_serial 1 \
             -days 3650 \
             -extfile example.cnf \
             -extensions ca_exts \
             -in int.req -out int.cert
         




### Create a client certificate for testing

Create a leaf certificate and private key for your test client workload. During the mTLS handshake process with your Secure Web Proxy instance, the client provides this leaf certificate to prove its identity.

The following example uses OpenSSL to generate a client key and a CSR, and then signs the CSR with the intermediate CA key that you created in the Create the root and intermediate certificates section.

  1. Run the following [OpenSSL](https://openssl-library.org/source/) command to generate an RSA private key named `client.key`:
         
         openssl genpkey -algorithm RSA -out client.key
         

  2. Create a configuration file named `client.cnf` that specifies a DNS name for the Subject Alternative Name (SAN). This helps ensure that the certificate is compatible with modern security requirements.
         
         cat > client.cnf << EOF
         [req]
         distinguished_name = req_distinguished_name
         req_extensions = v3_req
         prompt = no
         
         [req_distinguished_name]
         CN = my-client.example.com
         
         [v3_req]
         keyUsage = critical, digitalSignature, keyEncipherment
         extendedKeyUsage = clientAuth
         subjectAltName = @alt_names
         
         [alt_names]
         DNS.1 = my-client.example.com
         
         EOF
         

You can modify the `CN` and `DNS.1` values as required for testing.

  3. Run the OpenSSL request command by using the private key and configuration file that you created to generate a `client.req` file.
         
         openssl req -new -key client.key -out client.req -config client.cnf
         

  4. Use the OpenSSL `x509` command to sign the request by using your intermediate certificate (`int.cert`) and key (`int.key`). Set a validity period, such as 365 days, and make sure that the extensions from your configuration file are applied to the generated `client.cert` file.
         
         openssl x509 -req -in client.req -CA int.cert -CAkey int.key \
           -set_serial 02 -days 365 -out client.cert \
           -extfile client.cnf -extensions v3_req
         

This process creates the `client.cert` file. Record the value used in the DNS SAN (for example, `my-client.example.com`) as your client identity. You can use this value to identify the workload when you create your Secure Web Proxy authorization policies.




### Format the certificates

Format the root and intermediate certificates into environment variables to be used in the `trust_config.yaml` file.
    
    
      export ROOT_CERT=$(cat root.cert | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
      export INTERMEDIATE_CERT=$(cat int.cert | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
    

### Create a trust config resource

A [trust config](https://docs.cloud.google.com/certificate-manager/docs/core-components#trust-configs) represents your public key infrastructure (PKI) in Certificate Manager. The trust config indicates to your Secure Web Proxy instance which Certificate Authority (CA) certificates to trust when verifying client certificates presented during a frontend mTLS handshake.

This sample trust config resource contains a trust store with a single trust store with a trust anchor (root CA) and an intermediate CA. It uses the certificate content from the environment variables that you created in the previous Format the certificates section.

  1. Create a `trust_config.yaml` file.
         
         cat << EOF > trust_config.yaml
         trustStores:
           TRUST_CONFIG_NAME:
             trustAnchors:
               - pemCertificate: |
                 -----BEGIN CERTIFICATE-----
                 <certificate content>
                 -----END CERTIFICATE-----
             intermediateCAs:
               - pemCertificate: |
                 -----BEGIN CERTIFICATE-----
                 <certificate content>
                 -----END CERTIFICATE-----
         
         EOF
         

Replace `TRUST_CONFIG_NAME` with the name of your trust config resource.

  2. Import the `trust config.yaml` file by using the [`gcloud certificate-manager trust-configs import` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs).
         
         gcloud certificate-manager trust-configs import TRUST_CONFIG_NAME\
           --source=trust_config.yaml \
           --location=LOCATION
         

Replace the following:

     * `TRUST_CONFIG_NAME`: name of your trust config resource

     * `LOCATION`: region where your trust config resource is stored




### Create a `ServerTlsPolicy` resource

A `ServerTlsPolicy` resource—also known as a client authentication resource—defines how Secure Web Proxy validates client certificates. It lets you specify the server-side TLS mode and the trust config resource for certificate verification.

The [`clientValidationMode` attribute](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies#ClientValidationMode) determines how the connection is handled when a client provides either an invalid certificate or no certificate at all. For more information, see [frontend mTLS client validation modes](https://docs.cloud.google.com/load-balancing/docs/mtls#client-validation-mode).

The values of the `clientValidationMode` attribute are as follows:

  * `REJECT_INVALID`: Secure Web Proxy allows only the connections from clients that present a valid certificate signed by a CA in your trust config. Connections with invalid or missing certificates are rejected.

  * `ALLOW_INVALID_OR_MISSING_CLIENT_CERT`: Secure Web Proxy allows the connection request even if the client certificate is invalid, can't be validated against your trust config, or is missing entirely.

**Note:** If you select this mode, your Secure Web Proxy instance extracts the `SPIFFE_ID` and other certificate attributes if a valid certificate is provided. However, if the certificate is invalid or missing, then these specific identity attributes are unavailable. You can still create authorization policies based on the presence of a certificate or its fingerprint.



To create a `ServerTlsPolicy` resource, follow these steps:

  1. Create a `server_tls_policy.yaml` file. Choose one of the following options for `clientValidationMode`:

     * **Option 1: ALLOW_INVALID_OR_MISSING_CLIENT_CERT**
    
    name: SERVER_TLS_POLICY_NAME
    mtlsPolicy:
      clientValidationMode: ALLOW_INVALID_OR_MISSING_CLIENT_CERT
      clientValidationTrustConfig: projects/PROJECT_ID/locations/LOCATION/trustConfigs/TRUST_CONFIG_NAME
    

     * **Option 2: REJECT_INVALID**
    
    name: SERVER_TLS_POLICY_NAME
    mtlsPolicy:
      clientValidationMode: REJECT_INVALID
      clientValidationTrustConfig: projects/PROJECT_ID/locations/LOCATION/trustConfigs/TRUST_CONFIG_NAME
    

Replace the following:

     * `SERVER_TLS_POLICY_NAME`: name of your `ServerTlsPolicy` resource

     * `PROJECT_ID`: ID of your Google Cloud project

     * `TRUST_CONFIG_NAME`: name of your trust config resource

     * `LOCATION`: region where your Secure Web Proxy instance is configured

  2. Import the `ServerTlsPolicy` resource by using the [`gcloud network-security server-tls-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/server-tls-policies/import).
         
         gcloud network-security server-tls-policies import SERVER_TLS_POLICY_NAME\
           --source=server_tls_policy.yaml \
           --location=LOCATION
         

Replace the following:

     * `SERVER_TLS_POLICY_NAME`: name of your `ServerTlsPolicy` resource

     * `LOCATION`: region where your Secure Web Proxy instance is configured

  3. Optional: To list all your `ServerTlsPolicies` resources, use the [`gcloud network-security server-tls-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/server-tls-policies/list).
         
         gcloud network-security server-tls-policies list \
           --location=LOCATION
         

Replace `LOCATION` with the region where your Secure Web Proxy instance is configured.




### Associate the `ServerTlsPolicy` resource with your Secure Web Proxy instance

  1. Append the `ServerTlsPolicy` resource to the `gateway.yaml` file of your Secure Web Proxy instance.
         
         echo "serverTlsPolicy:
         //networksecurity.googleapis.com/projects/PROJECT_ID/locations/
         LOCATION/serverTlsPolicies/SERVER_TLS_POLICY_NAME"
         >> gateway.yaml
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project

     * `LOCATION`: region where your Secure Web Proxy instance is configured

  2. Import the configuration of your Secure Web Proxy instance from the `gateway.yaml` file by using the [`gcloud network-services gateways import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/gateways/import).
         
         gcloud network-services gateways import GATEWAY_NAME\
             --source=gateway.yaml \
             --location=LOCATION
         

Replace the following:

     * `GATEWAY_NAME`: name of your Secure Web Proxy instance

     * `LOCATION`: region where your Secure Web Proxy instance is configured




## Configure authorization policies

For more information, see [Set up authorization policies for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies).

## Logging

For more information, see [frontend mTLS error handling and logging](https://docs.cloud.google.com/load-balancing/docs/mtls#error_handling_and_logging).

## Limitations

  * Secure Web Proxy supports configuring frontend mTLS only in [explicit proxy routing mode](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart).

  * To create a frontend mTLS-based security rule, use [authorization policies](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies) for Secure Web Proxy. [Gateway security policy rules](https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules) aren't supported.




For more information, see [frontend mTLS limitations](https://docs.cloud.google.com/load-balancing/docs/mtls#limitations).

## What's next

  * [Deploy Secure Web Proxy as a Private Service Connect service](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
