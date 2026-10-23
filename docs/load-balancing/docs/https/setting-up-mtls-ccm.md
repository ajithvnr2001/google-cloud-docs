---
url: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm/
title: Set up frontend mTLS with user-provided certificates \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:10.059679+00:00
---

# Set up frontend mTLS with user-provided certificates  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up frontend mTLS with user-provided certificates Stay organized with collections  Save and categorize content based on your preferences. 

A valid client certificate must show a chain of trust back to the trust anchor (root certificate) in the trust store. This page provides instructions for creating your own trust chain by configuring your own root and intermediate certificates using the [OpenSSL](https://www.openssl.org/docs/) library.

After creating the roots of trust, this document outlines the process to upload them to the trust store of the Certificate Manager `TrustConfig` resource. This is followed by linking the trust config to the Client Authentication (`ServerTLSPolicy`) resource and then attaching the Client Authentication resource to the target HTTPS proxy resource of the load balancer.

## Before you begin

  * Review the [Mutual TLS overview](https://docs.cloud.google.com/load-balancing/docs/mtls).
  * Review the guide to [Manage trust configs](https://docs.cloud.google.com/certificate-manager/docs/trust-configs).
  * Install the Google Cloud CLI. For a complete overview of the tool, see the [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). You can find commands related to load balancing in the [API and gcloud CLI reference](https://docs.cloud.google.com/load-balancing/docs/apis).

If you haven't run the gcloud CLI previously, first run the [`gcloud init` command](https://docs.cloud.google.com/sdk/gcloud/reference/init) to authenticate.

  * Enable the following APIs: Compute Engine API, Certificate Manager API, Network Security, and Network Services API. To learn more, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

  * If you are using global external Application Load Balancer or classic Application Load Balancer, make sure you have set up a load balancer with any of the following supported backends:

    * VM instance group backends
    * Cloud Storage buckets (Supported only if there is at least one backend service also attached to the load balancer, in addition to the backend bucket)
    * Cloud Run, App Engine, or Cloud Run functions
    * Hybrid connectivity
    * Private Service Connect backends
  * If you are using regional external Application Load Balancer, cross-region internal Application Load Balancer, or regional internal Application Load Balancer, make sure you have set up a load balancer with any of the following supported backends:

    * VM instance group backends
    * Cloud Run
    * Hybrid connectivity
    * Private Service Connect backends
  * Set your project.

###  gcloud 
        
        gcloud config set project PROJECT_ID
        




## Permissions

To get the permissions that you need to complete this guide, ask your administrator to grant you the following IAM roles on the project: 

  * To create load balancer resources such as `TargetHTTPSProxy`: [Compute Load Balancer Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`) 
  * To use Certificate Manager resources: [Certificate Manager Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.owner) (`roles/certificatemanager.owner`) 
  * To create security and networking components: Compute Network Admin (`roles/compute.networkAdmin`) and Compute Security Admin (`roles/compute.securityAdmin`) 
  * To create a project (optional): [Project Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectCreator) (`roles/resourcemanager.projectCreator`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete this guide. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Create the root and intermediate certificates

**Note:**

If you already have certificates to upload to the trust store, you can skip this step and jump to Format the certificates.

If you need to use a self-signed, expired, or otherwise invalid certificate, or if root and intermediate certificates are unavailable, you can create a self-signed certificate and then add it to an allowlist in the trust config.

This section uses the [OpenSSL](https://www.openssl.org/docs/) library to create the root certificate (trust anchor) and the intermediate certificate.

A root certificate is at the top of the certificate chain. An intermediate certificate is a part of the chain of trust back to the root certificate. The intermediate certificate is cryptographically signed by the root certificate. When the load balancer receives a client certificate, the load balancer validates it by establishing a chain of trust from the client certificate back to the configured trust anchor.

Use the following commands to create the root and intermediate certificates. The creation of the intermediate certificate is optional. However, in this setup, we are using the intermediate certificate to sign the client certificate.

  1. Create an [OpenSSL configuration file](https://github.com/openssl/openssl/blob/master/apps/openssl.cnf).

In the following example, the configuration file (`example.cnf`) contains the `[ca_exts]` section, which specifies X.509 extensions that mark the certificate as suitable for a CA. To learn more about the requirements for root and intermediate certificates, see [Certificate requirements](https://docs.cloud.google.com/load-balancing/docs/mtls#certificate-requirements).
         
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
         

  2. Create a self-signed X.509 root certificate (`root.cert`). The root certificate is self-signed with its own private key (`root.key`).
         
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
         

  4. Sign the CSR to create the X.509 intermediate certificate (`int.cert`). The CSR is signed using the root certificate.
         
         openssl x509 -req \
             -CAkey root.key -CA root.cert \
             -set_serial 1 \
             -days 3650 \
             -extfile example.cnf \
             -extensions ca_exts \
             -in int.req -out int.cert
         




### Create a self-signed certificate that can be added to an allowlist

**Note:**

If you already have certificates to upload to the trust store, you can skip this step and jump to Format the certificates.

You can create a self-signed certificate and add it to an [allowlist in the trust config](https://docs.cloud.google.com/certificate-manager/docs/how-it-works#allowlisted-certs).

Use the following OpenSSL command to create a self-signed X.509 certificate.
    
    
       openssl req -x509 \
           -new -sha256 -newkey rsa:2048 -nodes \
           -days 3650 -subj '/CN=localhost' \
           -keyout allowlisted.key -out allowlisted.cert
    

This certificate is then added to an `allowlistedCertificates` field in the trust config.

## Format the certificates

To include new or existing certificates in a `TrustStore`, format the certificates into a single line and store them in environment variables, so that they can be referenced by the trust config YAML file.
    
    
    export ROOT_CERT=$(cat root.cert | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
    
    
    
    export INTERMEDIATE_CERT=$(cat int.cert | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
    

To include new or existing certificates that are added to an allowlist in a trust config, format the certificates into a single line and store them in environment variables, so that they can be read into the YAML file. For certificates that are on an allowlist, use the following command to format the certificates into a single line and store them in the `ALLOWLISTED_CERT` environment variable.
    
    
    export ALLOWLISTED_CERT=$(cat allowlisted.cert | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
    

## Create a trust config resource

A trust config is a resource that represents your Public Key Infrastructure (PKI) configuration in Certificate Manager.

To create a trust config resource, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Trust Configs** tab, click **Add Trust Config**.

  3. Enter a name for the configuration.

  4. For **Location** , select **Global** or **Regional**.

The location denotes where the trust config resource is stored. For global external Application Load Balancers, classic Application Load Balancers, and cross-region internal Application Load Balancers, create a _global_ trust config resource. For regional external Application Load Balancers and regional internal Application Load Balancers, create a _regional_ trust config resource.

If you selected **Regional** , select the region.

  5. In the **Trust store** section, click **Add trust anchor** and upload the PEM-encoded certificate file, or copy the contents of the certificate.

  6. Click **Add**.

  7. In the **Trust store** section, click **Add intermediate CA** and upload the PEM-encoded certificate file, or copy the contents of the certificate.

This step lets you add another level of trust between the root certificate and your server certificate.

  8. Click **Add** to add the intermediary CA.

  9. Optional: In the **Allowlisted certificates** section, click **Add certificate** and upload the PEM-encoded certificate file, or copy the contents of the certificate.

  10. Click **Add** to add the allowlisted certificate.

  11. Click **Create**.




Verify that the new trust config resource appears in the list of configurations.

###  gcloud 

  1. Create a trust config YAML file (`trust_config.yaml`) that specifies the trust config parameters. This example trust config resource contains a trust store with a trust anchor and an intermediate certificate. It reads the certificate content from the environment variables created in the previous Format the certificates step.
         
         cat << EOF > trust_config.yaml
         trustStores:
         - trustAnchors:
           - pemCertificate: "${ROOT_CERT?}"
           intermediateCas:
           - pemCertificate: "${INTERMEDIATE_CERT?}"
         EOF
         

To create a trust store with additional trust anchors or intermediate certificates, add `pemCertificate` rows in the appropriate section.

  2. Optional: Specify the certificate that is added to the trust config YAML file in the `allowlistedCertificates` field. You don't need a trust store to add a certificate to an allowlist.
         
         cat << EOF >> trust_config.yaml
         allowlistedCertificates:
         - pemCertificate: "${ALLOWLISTED_CERT?}"
         EOF
         

A [certificate that is added to an allowlist](https://docs.cloud.google.com/certificate-manager/docs/core-components#allowlisted-certs) represents any certificate that can be encapsulated within the trust config so that it is always considered valid. You can specify multiple certificates in an allowlist by using multiple instances of the `pemCertificate` field.

  3. To import the trust config YAML file, use the [`gcloud certificate-manager trust-configs import` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs):

### global

For global external Application Load Balancers, classic Application Load Balancers, and cross-region internal Application Load Balancers, specify `global` as the location where the trust config resource is stored.
         
         gcloud certificate-manager trust-configs import TRUST_CONFIG_NAME  \
             --source=trust_config.yaml \
             --location=global
         

Replace the following:

     * `TRUST_CONFIG_NAME`: the name of the trust config resource.

### regional

For regional external Application Load Balancers and regional internal Application Load Balancers, specify the region where the trust config resource is stored.
    
    gcloud certificate-manager trust-configs import TRUST_CONFIG_NAME  \
        --source=trust_config.yaml \
        --location=LOCATION
    

Replace the following:

     * `TRUST_CONFIG_NAME`: the name of the trust config resource.
     * `LOCATION`: the region where the trust config resource is stored. The default location is `global`.




## Create a Client Authentication resource

A Client Authentication (also called `ServerTLSPolicy`) resource lets you specify the server-side TLS mode and the trust config resource to use when validating client certificates. When the client presents an invalid certificate or no certificate to the load balancer, the [`clientValidationMode`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies#mtlspolicy) specifies how the client connection is handled. For more information, see [mTLS client validation modes](https://docs.cloud.google.com/load-balancing/docs/mtls#mtls_errors).

  * When the `clientValidationMode` is set to `ALLOW_INVALID_OR_MISSING_CLIENT_CERT`, all requests are passed to the backend even if the validation fails or the client certificate is missing.
  * When the `clientValidationMode` is set to `REJECT_INVALID`, only requests that supply a client certificate that can be validated against a `TrustConfig` resource are passed to the backend.



To create a Client Authentication (`ServerTlsPolicy`) resource, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Authentication Configuration** page.

[Go to Authentication Configuration](https://console.cloud.google.com/net-security/authconfig)

  2. On the **Client Authentication** tab, click **Create**.

  3. Enter a name for the Client Authentication resource.

  4. For **Location** , select **Global** or **Regional**.

For global external Application Load Balancers, classic Application Load Balancers, and cross-region internal Application Load Balancers, set the location to global. For regional external Application Load Balancers and regional internal Application Load Balancers, set the location to the region where the load balancer is configured.

  5. For **Client Authentication mode** , select **Load balancing**.

  6. Select a client validation mode.

  7. Select the trust config resource that you created earlier.

  8. Optional: Click **Equivalent code** to view the Terraform configuration for this resource.

  9. Click **Create**.




Verify that the Client Authentication (`ServerTlsPolicy`) is displayed.

###  gcloud 

  1. Based on how you want to handle the connection, select one of the following options to define the Client Authentication (`ServerTlsPolicy`) resource in YAML format.

     * **Option 1:** `clientValidationMode` is set to `ALLOW_INVALID_OR_MISSING_CLIENT_CERT`.

### global

For global external Application Load Balancers, classic Application Load Balancers, and cross-region internal Application Load Balancers, create a YAML file that declaratively specifies the client validation mode and a global trust config resource:
           
           cat << EOF > server_tls_policy.yaml
           name: SERVER_TLS_POLICY_NAME
           mtlsPolicy:
               clientValidationMode: ALLOW_INVALID_OR_MISSING_CLIENT_CERT
               clientValidationTrustConfig: projects/PROJECT_ID/locations/global/trustConfigs/TRUST_CONFIG_NAME
           EOF
           

### regional

For regional external Application Load Balancers and regional internal Application Load Balancers, create a YAML file that declaratively specifies the client validation mode and a regional trust config resource:
           
           cat << EOF > server_tls_policy.yaml
           name: SERVER_TLS_POLICY_NAME
           mtlsPolicy:
               clientValidationMode: ALLOW_INVALID_OR_MISSING_CLIENT_CERT
               clientValidationTrustConfig: projects/PROJECT_ID/locations/REGION/trustConfigs/TRUST_CONFIG_NAME
           EOF
           

     * **Option 2:** `clientValidationMode` is set to `REJECT_INVALID`.

### global

For global external Application Load Balancers, classic Application Load Balancers, and cross-region internal Application Load Balancers, create a YAML file that declaratively specifies the client validation mode and a global trust config resource:
           
           cat << EOF > server_tls_policy.yaml
           name: SERVER_TLS_POLICY_NAME
           mtlsPolicy:
               clientValidationMode: REJECT_INVALID
               clientValidationTrustConfig: projects/PROJECT_ID/locations/global/trustConfigs/TRUST_CONFIG_NAME
           EOF
           

### regional

For regional external Application Load Balancers and regional internal Application Load Balancers, create a YAML file that declaratively specifies the client validation mode and a regional trust config resource:
           
           cat << EOF > server_tls_policy.yaml
           name: SERVER_TLS_POLICY_NAME
           mtlsPolicy:
                 clientValidationMode: REJECT_INVALID
                 clientValidationTrustConfig: projects/PROJECT_ID/locations/REGION/trustConfigs/TRUST_CONFIG_NAME
           EOF
           

Replace the following:

`SERVER_TLS_POLICY_NAME`: the name of the Client Authentication (`ServerTlsPolicy`) resource.

`PROJECT_ID`: the ID of your Google Cloud project.

`LOCATION`: for global external Application Load Balancers, classic Application Load Balancers, and cross-region internal Application Load Balancers, use `global`. For regional external Application Load Balancer or regional internal Application Load Balancer, use the region where you configured the load balancer.

`TRUST_CONFIG_NAME`: the name of the trust config resource that you created earlier.

  2. To import the Client Authentication `ServerTlsPolicy` resource, use the [`gcloud network-security server-tls-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/server-tls-policies/import):

### global

For global external Application Load Balancers, classic Application Load Balancers, and cross-region internal Application Load Balancers, set the `--location` flag to `global`.
         
         gcloud network-security server-tls-policies import SERVER_TLS_POLICY_NAME \
           --source=server_tls_policy.yaml \
           --location=global
         

Replace the following:

`SERVER_TLS_POLICY_NAME`: the name of the Client Authentication (`ServerTlsPolicy`) resource.

### regional

For regional external Application Load Balancers and regional internal Application Load Balancers, set the `--location` flag to the region where the load balancer is configured.
         
         gcloud network-security server-tls-policies import SERVER_TLS_POLICY_NAME \
           --source=server_tls_policy.yaml \
           --location=LOCATION
         

Replace the following:

`SERVER_TLS_POLICY_NAME`: the name of the Client Authentication (`ServerTlsPolicy`) resource.

  3. Optional: To list all the Client Authentication (`ServerTlsPolicies`) resources, use the [ `gcloud network-security server-tls-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/server-tls-policies/list):
         
         gcloud network-security server-tls-policies list \
           --location=LOCATION
         

Replace the following:

`LOCATION`: For global external Application Load Balancers, classic Application Load Balancers, and cross-region internal Application Load Balancers, use `global`. For regional external Application Load Balancer or regional internal Application Load Balancer, use the region where you configured the load balancer.




**Note:** To modify the Client Authentication (`ServerTlsPolicy`) resource, you must first delete the existing Client Authentication resource and then create a new Client Authentication resource. You can then attach the Client Authentication resource to the target HTTPS proxy of the load balancer.

## Attach the Client Authentication resource to the load balancer

For mutual TLS authentication to work, after you set up your load balancer, you need to attach the Client Authentication (`ServerTLSPolicy`) resource to the target HTTPS proxy resource of the load balancer.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. From the list of load balancers, select the load balancer to which you need to attach the Client Authentication (`ServerTLSPolicy`) resource to.

  3. Click edit**Edit**.

  4. In the **Frontend configuration** section for an HTTPS frontend, expand the **Show Advanced features** section.

  5. From the **Client Authentication** list, select the Client Authentication resource.

  6. Click **Done**.

  7. Click **Update**.




###  gcloud 

  1. To list all the target HTTPS proxy resources in your project, use the [ `gcloud compute target-https-proxies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/list):
         
         gcloud compute target-https-proxies list
         

Note the name of the target HTTPS proxy to attach the `ServerTLSPolicy` resource to. This name is referred to as `TARGET_HTTPS_PROXY_NAME` in the following steps.

  2. To export a target HTTPS proxy's configuration to a file, use the [ `gcloud compute target-https-proxies export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/export).

### global
         
         gcloud compute target-https-proxies export TARGET_HTTPS_PROXY_NAME \
               --destination=TARGET_PROXY_FILENAME \
               --global
           

Replace the following:

     * `TARGET_HTTPS_PROXY_NAME`: the name of the target proxy.
     * `TARGET_PROXY_FILENAME`: the name of the target proxy's configuration file in YAML format. For example, `mtls_target_proxy.yaml`.

### regional
    
    gcloud compute target-https-proxies export TARGET_HTTPS_PROXY_NAME \
        --destination=TARGET_PROXY_FILENAME \
        --region=REGION
    

Replace the following:

     * `TARGET_HTTPS_PROXY_NAME`: the name of the target proxy.
     * `TARGET_PROXY_FILENAME`: the name of the target proxy's configuration file in YAML format. For example, `mtls_target_proxy.yaml`
     * `REGION`: the region where you configured the load balancer.

  3. To list all the Client Authentication (`ServerTlsPolicy`) resources, use the [ `gcloud network-security server-tls-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/server-tls-policies/list):
         
         gcloud network-security server-tls-policies list \
             --location=LOCATION
         

Replace the following:

`LOCATION`: for cross-region internal Application Load Balancer, global external Application Load Balancer, or classic Application Load Balancer, use `global`. For regional external Application Load Balancer or regional internal Application Load Balancer, use the region where you configured the load balancer.

Note the name of the Client Authentication (`ServerTLSPolicy`) resource to configure mTLS. This name is referred to as `SERVER_TLS_POLICY_NAME` in the next step.

  4. Append the Client Authentication (`ServerTlsPolicy`) to the target HTTPS proxy.
         
         echo "serverTlsPolicy: //networksecurity.googleapis.com/projects/PROJECT_ID/locations/LOCATION/serverTlsPolicies/SERVER_TLS_POLICY_NAME" >> TARGET_PROXY_FILENAME

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: for global external Application Load Balancers or classic Application Load Balancers, andcross-region internal Application Load Balancers, use `global`. For regional external Application Load Balancer or regional internal Application Load Balancer, use the region where you configured the load balancer.
     * `SERVER_TLS_POLICY_NAME`: the name of the Client Authentication (`ServerTLSPolicy`) resource.
     * `TARGET_PROXY_FILENAME`: the name of the target proxy's configuration file in YAML format.
  5. To import a target HTTPS proxy's configuration from a file, use the [`gcloud compute target-https-proxies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/import).

### global
         
         gcloud compute target-https-proxies import TARGET_HTTPS_PROXY_NAME \
               --source=TARGET_PROXY_FILENAME \
               --global
           

Replace the following:

     * `TARGET_HTTPS_PROXY_NAME`: the name of the target proxy.
     * `TARGET_PROXY_FILENAME`: the name of the target proxy's configuration file in YAML format. For example, `mtls_target_proxy.yaml`.

### regional
    
    gcloud compute target-https-proxies import TARGET_HTTPS_PROXY_NAME \
          --source=TARGET_PROXY_FILENAME \
          --region=REGION
      

Replace the following:

     * `TARGET_HTTPS_PROXY_NAME`: the name of the target proxy.
     * `TARGET_PROXY_FILENAME`: the name of the target proxy's configuration file in YAML format. For example, `mtls_target_proxy.yaml`
     * `REGION`: the region where you configured the load balancer.




## Add mTLS custom headers

When you enable mTLS, you can pass information about the mTLS connection using custom headers. You can also enable logging so that [mTLS connection failures](https://docs.cloud.google.com/load-balancing/docs/mtls#mtls_errors) are captured in your logs. For more information about how to configure logging, see one of the following:

  * [Global external Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring)
  * [Regional external Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-reg-logging-monitoring)



### Add mTLS custom headers to backend services

For global external Application Load Balancers or classic Application Load Balancers, you can use [ custom headers](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-global) to pass information about the mTLS connection to _backend services_.

  1. To list all the backend services in the project, use the [`gcloud compute backend-services list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/list):
         
         gcloud compute backend-services list
         

Note the name of the backend service to enable custom headers. This name is referred to as `BACKEND_SERVICE` in the following step.

  2. To update the backend service, use the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update):
         
         gcloud compute backend-services update BACKEND_SERVICE \
           --global \
           --custom-request-header='X-Client-Cert-Present:{client_cert_present}' \
           --custom-request-header='X-Client-Cert-Chain-Verified:{client_cert_chain_verified}' \
           --custom-request-header='X-Client-Cert-Error:{client_cert_error}' \
           --custom-request-header='X-Client-Cert-Hash:{client_cert_sha256_fingerprint}' \
           --custom-request-header='X-Client-Cert-Serial-Number:{client_cert_serial_number}' \
           --custom-request-header='X-Client-Cert-SPIFFE:{client_cert_spiffe_id}' \
           --custom-request-header='X-Client-Cert-URI-SANs:{client_cert_uri_sans}' \
           --custom-request-header='X-Client-Cert-DNSName-SANs:{client_cert_dnsname_sans}' \
           --custom-request-header='X-Client-Cert-Valid-Not-Before:{client_cert_valid_not_before}' \
           --custom-request-header='X-Client-Cert-Valid-Not-After:{client_cert_valid_not_after}'
         


**Note:**

You can provide your own custom header names. The names used in the `--custom-request-header` options are just examples.

You can enable some or all of the mTLS custom headers.

### Add mTLS custom headers to URL map

For cross-region internal Application Load Balancer, regional external Application Load Balancer, or regional internal Application Load Balancer, you can use [ custom headers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/custom-headers) to pass information about the mTLS connection to the _URL map_.

To list all the URL maps in the project, use the [ `gcloud compute url-maps list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/list):
    
    
       gcloud compute url-maps list
       

Note the name of the URL map to enable custom headers. This name is referred to as `URL_MAP_NAME` in the following step.

### global

To edit the URL map for a cross-region internal Application Load Balancer, use the [`gcloud compute url-maps edit`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit) command:
    
    
       gcloud compute url-maps edit URL_MAP_NAME --global
       

Following is a sample YAML file that shows you how to use variables in custom request headers (`requestHeadersToAdd`). You can use the same variables to send custom response headers (`responseHeadersToAdd`).
    
    
       headerAction:
          requestHeadersToAdd:
          - headerName: "X-Client-Cert-Present"
            headerValue: "{client_cert_present}"
          - headerName: "X-Client-Cert-Chain-Verified"
            headerValue: "{client_cert_chain_verified}"
          - headerName: "X-Client-Cert-Error"
            headerValue: "{client_cert_error}"
          - headerName: "X-Client-Cert-Hash"
            headerValue: "{client_cert_sha256_fingerprint}"
          - headerName: "X-Client-Cert-Serial-Number"
            headerValue: "{client_cert_serial_number}"
          - headerName: "X-Client-Cert-SPIFFE"
            headerValue: "{client_cert_spiffe_id}"
          - headerName: "X-Client-Cert-URI-SANs"
            headerValue: "{client_cert_uri_sans}"
          - headerName: "X-Client-Cert-DNSName-SANs"
            headerValue: "{client_cert_dnsname_sans}"
          - headerName: "X-Client-Cert-Valid-Not-Before"
            headerValue: "{client_cert_valid_not_before}"
          - headerName: "X-Client-Cert-Valid-Not-After"
            headerValue: "{client_cert_valid_not_after}"
          - headerName: "X-Client-Cert-Issuer-Dn"
            headerValue: "{client_cert_issuer_dn}"
          - headerName: "X-Client-Cert-Subject-Dn"
            headerValue: "{client_cert_subject_dn}"
          - headerName: "X-Client-Cert-Leaf"
            headerValue: "{client_cert_leaf}"
          - headerName: "X-Client-Cert-Chain"
            headerValue: "{client_cert_chain}"
       

### regional

To edit the URL map for a regional external Application Load Balancer or a regional internal Application Load Balancer, use the [`gcloud compute url-maps edit`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit) command:
    
    
       gcloud compute url-maps edit URL_MAP_NAME --region=REGION
       

Following is a sample YAML file that shows you how to use variables in custom request headers (`requestHeadersToAdd`). You can use the same variables to send custom response headers (`responseHeadersToAdd`).
    
    
       defaultService: regions/REGION/backendServices/BACKEND_SERVICE_1
          name: regional-lb-map
          region: region/REGION
       headerAction:
          requestHeadersToAdd:
          - headerName: "X-Client-Cert-Present"
            headerValue: "{client_cert_present}"
          - headerName: "X-Client-Cert-Chain-Verified"
            headerValue: "{client_cert_chain_verified}"
          - headerName: "X-Client-Cert-Error"
            headerValue: "{client_cert_error}"
          - headerName: "X-Client-Cert-Hash"
            headerValue: "{client_cert_sha256_fingerprint}"
          - headerName: "X-Client-Cert-Serial-Number"
            headerValue: "{client_cert_serial_number}"
          - headerName: "X-Client-Cert-SPIFFE"
            headerValue: "{client_cert_spiffe_id}"
          - headerName: "X-Client-Cert-URI-SANs"
            headerValue: "{client_cert_uri_sans}"
          - headerName: "X-Client-Cert-DNSName-SANs"
            headerValue: "{client_cert_dnsname_sans}"
          - headerName: "X-Client-Cert-Valid-Not-Before"
            headerValue: "{client_cert_valid_not_before}"
          - headerName: "X-Client-Cert-Valid-Not-After"
            headerValue: "{client_cert_valid_not_after}"
          - headerName: "X-Client-Cert-Issuer-Dn"
            headerValue: "{client_cert_issuer_dn}"
          - headerName: "X-Client-Cert-Subject-Dn"
            headerValue: "{client_cert_subject_dn}"
          - headerName: "X-Client-Cert-Leaf"
            headerValue: "{client_cert_leaf}"
          - headerName: "X-Client-Cert-Chain"
            headerValue: "{client_cert_chain}"
       

## Sign the client certificate with the intermediate certificate

This section provides an additional configuration option to generate a client (leaf) certificate. If you have already [created a TrustConfig resource](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm#trustconfig) that contains an intermediate certificate, do the following:

  1. Create a configuration file to generate the CSR for the client certificate.

The following configuration file (`client.config`) contains the `[extension_requirements]` section, which specifies the X.509 extensions to include in the CSR. To learn more about the requirements for client certificates, see [Certificate requirements](https://docs.cloud.google.com/load-balancing/docs/mtls#certificate-requirements).

**Note:** If the key is used on a server, you can add `serverAuth` to the `extendedKeyUsage` field.
         
         cat > client.config << EOF
         [req]
         default_bits              = 2048
         req_extensions            = extension_requirements
         distinguished_name        = dn_requirements
         prompt                    = no
         
         [extension_requirements]
         basicConstraints          = critical, CA:FALSE
         keyUsage                  = critical, nonRepudiation, digitalSignature, keyEncipherment
         extendedKeyUsage          = clientAuth
         
         [dn_requirements]
         countryName               = US
         stateOrProvinceName       = California
         localityName              = San Francisco
         0.organizationName        = example
         organizationalUnitName    = test
         commonName                = test.example.com
         emailAddress              = test@example.com
         
         EOF
         

If you want to attach a [SPIFFE identity](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/#spiffe-id) to the configuration file, do the following:

     * Add a `subjectAltName` field to the `[extension_requirements]` section as follows:
           
           subjectAltName            = @sans_list
           

     * Add a new section (`[sans_list]`) at the bottom of the `client.config` file as follows:
           
           [sans_list]
           URI.1                     = spiffe://example.com/test-identity
           

  2. Create the CSR (`client.csr`) for the client certificate.
         
         openssl req -new \
             -config client.config \
             -keyout client.key -out client.csr
         

  3. Sign the CSR to issue the X.509 client certificate (`client.cert`). The CSR is signed by the intermediate certificate.
         
         openssl x509 -req \
             -CAkey int.key -CA int.cert \
             -days 365 \
             -extfile client.config \
             -extensions extension_requirements \
             -in client.csr -out client.cert
         

  4. Send a secure HTTPS request to the load balancer's IP address using the client-side SSL certificate. The client presents its certificate (`client.cert`) to authenticate itself to the load balancer.
         
         curl -v --key client.key --cert client.cert https://IP_ADDRESS
         

Replace IP_ADDRESS with the load balancer's IP address.




## What's next

  * [Set up mutual TLS with a private CA](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ca-ccm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
