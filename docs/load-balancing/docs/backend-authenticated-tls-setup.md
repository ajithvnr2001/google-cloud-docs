---
url: https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-setup/
title: Set up backend authenticated TLS \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:36.942500+00:00
---

# Set up backend authenticated TLS  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up backend authenticated TLS Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions to set up backend authenticated TLS, also known as backend authentication, by using self-managed certificates.

To configure _backend authenticated TLS_ , you need to do the following. These steps are described in the following sections of this document.

  * Create a trust config resource that consists of root and intermediate certificates.
  * Create a backend authentication config resource that references the trust config.
  * Attach the backend authentication config resource to the backend service of the load balancer.



## Before you begin

  * Review the [Backend authenticated TLS and backend mTLS overview](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls).
  * Review [Manage trust configs](https://docs.cloud.google.com/certificate-manager/docs/trust-configs).
  * If you want to follow the instructions in this guide using the Google Cloud CLI, you need to [install](https://docs.cloud.google.com/sdk/docs/install) it. You can find commands related to load balancing in the [API and gcloud CLI references](https://docs.cloud.google.com/load-balancing/docs/apis).

If you haven't run the gcloud CLI previously, first run the [`gcloud init` command](https://docs.cloud.google.com/sdk/gcloud/reference/init) to authenticate.

  * Enable the following APIs: Compute Engine API, Certificate Manager API, Network Security, and Network Services API. To learn more, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

  * Configure a load balancer with any of the following supported backends:

    * VM instance group backends
    * Hybrid connectivity NEGs
    * Zonal NEGs



## Permissions

This section lists the permissions required to configure backend authenticated TLS. Operation | Permission  
---|---  
Create a trust config | `certificatemanager.trustconfigs.create` on the target Google Cloud project  
Create a backend authentication config resource | 
* `certificatemanager.certs.use` on the target certificate
* `certificatemanager.trustconfigs.use` on the target trust config
* `networksecurity.backendauthenticationconfigs.create` on the target Google Cloud project  
Attach the backend authentication config resource to the backend service of the load balancer | 
* `compute.backendservice.update` on the target backend service
* `networksecurity.backendauthenticationconfigs.use` on the target backend authentication config resource  
  
## Setup overview

The sections that follow describe the steps to configure backend authenticated TLS based on the architecture shown in the following diagram.

[ ![Components of backend authenticated TLS.](https://docs.cloud.google.com/static/load-balancing/images/setup_backend_authenticated_TLS.svg)](https://docs.cloud.google.com/static/load-balancing/images/setup_backend_authenticated_TLS.svg) Backend authenticated TLS components (click to enlarge).

## Create the root and intermediate certificates

**Note:**

If you already have certificates to upload to the trust store, you can skip this step and jump to Format the certificates.

This section uses the [OpenSSL](https://www.openssl.org/docs/) library to create the root certificate (trust anchor) and the intermediate certificate.

A root certificate is at the top of the certificate chain. An intermediate certificate is a part of the chain of trust back to the root certificate. The intermediate certificate is cryptographically signed by the root certificate. When the load balancer receives a server certificate, the load balancer validates it by establishing a chain of trust from the server certificate back to the configured trust anchor.

Use the following commands to create the root and intermediate certificates.

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
         extendedKeyUsage=serverAuth
         
         EOF
         

  2. Generate a new RSA private key (`root.key`) and use it to create a self-signed X.509 root CA certificate (`root.cert`), which serves as the root Certificate Authority (CA).
         
         openssl req -x509 \
             -new -sha256 -newkey rsa:2048 -nodes \
             -days 3650 -subj '/CN=root' \
             -config example.cnf \
             -extensions ca_exts \
             -keyout root.key -out root.cert
         

  3. Create a certificate signing request (CSR) (`int.req`) for the intermediate certificate.
         
         openssl req -new \
             -sha256 -newkey rsa:2048 -nodes \
             -subj '/CN=int' \
             -config example.cnf \
             -extensions ca_exts \
             -keyout int.key -out int.req
         

  4. Create the X.509 intermediate certificate (`int.cert`) from the CSR. The root CA uses its private key (`root.key`) and certificate (`root.cert`) to issue and sign the X.509 intermediate certificate.
         
         openssl x509 -req \
             -CAkey root.key -CA root.cert \
             -set_serial 1 \
             -days 3650 \
             -extfile example.cnf \
             -extensions ca_exts \
             -in int.req -out int.cert
         




## Format the certificates

To include new or existing certificates in a trust store, format the certificates into a single line and store them in environment variables so that they can be referenced by the trust config YAML file.
    
    
    export ROOT_CERT=$(cat root.cert | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
    
    
    
    export INTERMEDIATE_CERT=$(cat int.cert | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
    

## Create a trust config

A trust config is a resource that represents your public key infrastructure (PKI) configuration in Certificate Manager.

To create a trust config resource, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Trust Configs** tab, click **Add Trust Config**.

  3. Enter a name for the configuration.

  4. For **Location** , select **Global** or **Regional**.

The location denotes where the trust config resource is stored. For global external Application Load Balancers and cross-region internal Application Load Balancers, create a _global_ trust config resource. For regional external Application Load Balancers and regional internal Application Load Balancers, create a _regional_ trust config resource.

  5. In the **Trust store** section, click **Add trust anchor** and upload the PEM-encoded certificate file, or copy the contents of the certificate.

  6. Click **Add**.

  7. In the **Trust store** section, click **Add intermediate CA** and upload the PEM-encoded certificate file, or copy the contents of the certificate. This step lets you add another level of trust between the root certificate and your server certificate.

  8. Click **Add** to add the intermediary CA.

  9. To add the certificate that you added to the allowlist, click **Add**.

  10. Click **Create**.




Verify that the new trust config resource appears in the list of configurations.

###  gcloud 

  1. Create a trust config YAML file (`trust_config.yaml`) that specifies the trust config parameters. This example trust config resource contains a trust store with a trust anchor and an intermediate certificate. This example trust config resource reads the certificate content from the environment variables created in the previous Format the certificates step.
         
         cat << EOF > trust_config.yaml
         trustStores:
         - trustAnchors:
           - pemCertificate: "${ROOT_CERT}"
           intermediateCas:
           - pemCertificate: "${INTERMEDIATE_CERT}"
         EOF
         

To create a trust store with additional trust anchors or intermediate certificates, add `pemCertificate` rows in the appropriate section.

  2. To import the trust config YAML file, use the [`gcloud certificate-manager trust-configs import` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/import).

### global

For global external Application Load Balancers and cross-region internal Application Load Balancers, specify `global` as the location where the trust config resource is stored.
         
         gcloud certificate-manager trust-configs import TRUST_CONFIG_NAME  \
             --source=trust_config.yaml \
             --location=global
         

Replace `TRUST_CONFIG_NAME` with the name of the trust config.

### regional

For regional external Application Load Balancers and regional internal Application Load Balancers, specify the region where the trust config resource is stored.
         
         gcloud certificate-manager trust-configs import TRUST_CONFIG_NAME \
             --source=trust_config.yaml \
             --location=REGION
         

Replace the following:

     * `TRUST_CONFIG_NAME`: the name of the trust config resource
     * `REGION`: the region where the trust config resource is stored




## Create a backend authentication config resource

To create a backend authentication config ([`BackendAuthenticationConfig`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.backendAuthenticationConfigs)) resource, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Authentication Configuration** page. 

[Go to Authentication Configuration](https://console.cloud.google.com/net-security/authconfig)

  2. On the **Backend Authentication** tab, click **Create**.
  3. Enter a name for the backend authentication config resource.
  4. For **Location** , select **Global** or **Regional**.
  5. Optional: Select the public roots of trust.
  6. Select the trust config resource that you created earlier.
  7. Optional: Click **Equivalent code** to view the Terraform configuration for this resource.
  8. Click **Create**.



Verify that the backend authentication config resource is displayed.

###  gcloud 

  1. Create a YAML file that declaratively specifies the different attributes of the backend authentication config resource.

### global

For global external Application Load Balancers and cross-region internal Application Load Balancers, create a global backend authentication config resource.
         
         cat << EOF > BACKEND_AUTHENTICATION_CONFIG_RESOURCE_FILENAME.yaml
         name: projects/PROJECT_ID/locations/global/backendAuthenticationConfigs/BACKEND_AUTH_CONFIG_NAME
         trustConfig: projects/PROJECT_ID/locations/global/trustConfigs/TRUST_CONFIG_NAME
         wellKnownRoots: PUBLIC_ROOTS
         EOF
         

Replace the following:

     * `BACKEND_AUTHENTICATION_CONFIG_RESOURCE_FILENAME `: the name of the YAML file where the backend authentication config resource is defined
     * `PROJECT_ID`: the ID of your Google Cloud project
     * `BACKEND_AUTH_CONFIG_NAME`: the name of the backend authentication config resource
     * `TRUST_CONFIG_NAME`: the name of the trust config resource that you created earlier

### regional

For regional external Application Load Balancers and regional internal Application Load Balancers, create a regional backend authentication config resource.
    
    cat << EOF > BACKEND_AUTHENTICATION_CONFIG_RESOURCE_FILENAME.yaml
    name: projects/PROJECT_ID/locations/REGION/backendAuthenticationConfigs/BACKEND_AUTH_CONFIG_NAME
    trustConfig: projects/PROJECT_ID/locations/REGION/trustConfigs/TRUST_CONFIG_NAME
    wellKnownRoots: PUBLIC_ROOTS
    EOF
    

Replace the following:

     * `BACKEND_AUTHENTICATION_CONFIG_RESOURCE_FILENAME `: the name of the YAML file where the backend authentication config resource is defined
     * `PROJECT_ID`: the ID of your Google Cloud project
     * `REGION`: the name of the region
     * `BACKEND_AUTH_CONFIG_NAME`: the name of the backend authentication config resource
     * `TRUST_CONFIG_NAME`: the name of the trust config resource that you created earlier

  2. To import the backend authentication config, use the [`gcloud network-security backend-authentication-configs import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/backend-authentication-configs/import).

### global

For global external Application Load Balancers and cross-region internal Application Load Balancers, set the `--location` flag to `global`.
         
         gcloud network-security backend-authentication-configs import BACKEND_AUTH_CONFIG_NAME \
             --source=BACKEND_AUTHENTICATION_CONFIG_RESOURCE_FILENAME.yaml \
             --location=global
         

Replace the following:

     * `BACKEND_AUTH_CONFIG_NAME`: the name of the backend authentication config resource

     * `BACKEND_AUTHENTICATION_CONFIG_RESOURCE_FILENAME`: the name of the YAML file where the backend authentication config resource is defined

### regional

For regional external Application Load Balancers and regional internal Application Load Balancers, set the `--location` flag to the region where the load balancer is configured.
    
    gcloud network-security backend-authentication-configs import BACKEND_AUTH_CONFIG_NAME \
        --source=BACKEND_AUTHENTICATION_CONFIG_RESOURCE_FILENAME.yaml \
        --location=REGION
    

Replace the following:

     * `BACKEND_AUTH_CONFIG_NAME`: the name of the backend authentication config resource

     * `BACKEND_AUTHENTICATION_CONFIG_RESOURCE_FILENAME`: the name of the YAML file where the backend authentication config resource is defined

     * `REGION`: the region where the load balancer is configured




## Attach the backend authentication config resource to the backend service of the load balancer

To attach the backend authentication config ([`BackendAuthenticationConfig` resource](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.backendAuthenticationConfigs)) to the backend service of the load balancer, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. On the **Backends** tab, select the backend service for which you need to enable backend authenticated TLS and backend mTLS.

  3. Click edit**Edit**.

  4. Expand the **Advanced configurations** section.

  5. In the **Backend authentication** section, select the **Enable** checkbox.

  6. Optional: Specify the SNI hostname and accepted SANs to [validate the backend certificate](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls#backend_service).

  7. To attach the backend authentication config resource to the backend service, in the **Backend authentication config** list, select the backend authentication config resource.

  8. Click **Continue**.

  9. To update the backend service settings, click **Update**.




###  gcloud 

  1. To list all the backend service resources in your project, use the [`gcloud compute backend-services list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/list).
         
         gcloud compute backend-services list
         

Note the name of the backend service to attach the `BackendAuthenticationConfig` resource to. This name is referred to as `BACKEND_SERVICE_NAME` in the following steps.

  2. To export the backend service configuration to a file, use the [`gcloud compute backend-services export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/export).

### global

For global external Application Load Balancers and cross-region internal Application Load Balancers, set the `--location` flag to `global`.
         
         gcloud compute backend-services export BACKEND_SERVICE_NAME \
             --destination=BACKEND_SERVICE_FILENAME.yaml \
             --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service
     * `BACKEND_SERVICE_FILENAME`: the name and path to a YAML file where the backend service configuration is exported

### regional

For regional external Application Load Balancers and regional internal Application Load Balancers, set the `--location` flag to the region where the load balancer is configured.
    
    gcloud compute backend-services export BACKEND_SERVICE_NAME \
        --destination=BACKEND_SERVICE_FILENAME.yaml \
        --region=REGION
    

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service
     * `BACKEND_SERVICE_FILENAME`: the name and path to a YAML file where the backend service configuration is exported
     * `REGION`: the name of the Google Cloud region where the backend service is located

  3. Update the `tlsSettings` attribute of the backend service, pointing it to the backend authentication config resource. In addition, you can configure the SNI hostname and accepted SANs on the backend service to [validate the backend certificate](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls#backend_service).

### global

For global external Application Load Balancers and cross-region internal Application Load Balancers, attach the global backend authentication config resource to the backend service.

The SNI and SAN values in the following YAML declaration are intended as examples only. You can substitute them with real-world values that are relevant to your setup.
         
         cat << EOF >> BACKEND_SERVICE_FILENAME.yaml
           tlsSettings:
             authenticationConfig: //networksecurity.googleapis.com/projects/PROJECT_ID/locations/global/backendAuthenticationConfigs/BACKEND_AUTH_CONFIG_NAME
             sni: examplepetstore.com
             subjectAltNames:
             - dnsName: examplepetstore.com
             - dnsName: api.examplepetstore.com
           EOF
           

Replace the following:

     * `BACKEND_SERVICE_FILENAME`: the name of the YAML file where the backend service configuration is exported

     * `PROJECT_ID`: the ID of your Google Cloud project

     * `BACKEND_AUTH_CONFIG_NAME`: the name of the backend authentication config resource

### regional

For regional external Application Load Balancers and regional internal Application Load Balancers, attach the regional backend authentication config resource to the backend service.

The SNI and SAN values in the following YAML declaration are intended as examples only. You can substitute them with real-world values that are relevant to your setup.
    
    cat << EOF >> BACKEND_SERVICE_FILENAME.yaml
      tlsSettings:
        authenticationConfig: //networksecurity.googleapis.com/projects/PROJECT_ID/locations/REGION/backendAuthenticationConfigs/BACKEND_AUTH_CONFIG_NAME
        sni: examplepetstore.com
        subjectAltNames:
        - dnsName: examplepetstore.com
        - dnsName: api.examplepetstore.com
      EOF
      

Replace the following:

     * `BACKEND_SERVICE_FILENAME`: the name of the YAML file where the backend service configuration is exported

     * `PROJECT_ID`: the ID of your Google Cloud project

     * `REGION`: the name of the Google Cloud region where the backend authentication config is created

     * `BACKEND_AUTH_CONFIG_NAME`: the name of the backend authentication config resource

  4. To import the updated backend service configuration from a file, use the [`gcloud compute backend-services import` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/import).

### global

For global external Application Load Balancers and cross-region internal Application Load Balancers, use the `--global` flag.
         
         gcloud compute backend-services import BACKEND_SERVICE_NAME \
               --source=BACKEND_SERVICE_FILENAME.yaml \
               --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service
     * `BACKEND_SERVICE_FILENAME`: the name of the backend service configuration YAML file

### regional

For regional external Application Load Balancers and regional internal Application Load Balancers, set the `--region` flag to the region where the load balancer is located.
    
    gcloud compute backend-services import BACKEND_SERVICE_NAME \
          --source=BACKEND_SERVICE_FILENAME.yaml \
          --region=REGION
    

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service
     * `BACKEND_SERVICE_FILENAME`: the name of the backend service configuration YAML file
     * `REGION`: the name of the Google Cloud region where the backend service is located




## Create a backend server certificate

This section provides an additional configuration option to create a server (leaf) certificate that is signed by the intermediate certificate, which is a part of the trust config. This ensures that a chain of trust can be established from the server certificate back to the trust anchor.

If you have already created a trust config resource that contains an intermediate certificate, do the following:

  1. Create a configuration file to generate the CSR for the server certificate.

The following configuration file (`server.config`) contains the `[extension_requirements]` section, which specifies the X.509 extensions to include in the CSR. To learn more about the requirements for server certificates, see [Certificate requirements](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls#certificate-requirements).
         
         cat > server.config << EOF
         [req]
         default_bits              = 2048
         req_extensions            = extension_requirements
         distinguished_name        = dn_requirements
         prompt                    = no
         
         [extension_requirements]
         basicConstraints          = critical, CA:FALSE
         keyUsage                  = critical, nonRepudiation, digitalSignature, keyEncipherment
         extendedKeyUsage          = serverAuth
         subjectAltName            = @alt_names
         
         [alt_names]
         DNS.1 = examplepetstore.com
         DNS.2 = api.examplepetstore.com
         
         [dn_requirements]
         countryName               = US
         stateOrProvinceName       = California
         localityName              = San Francisco
         0.organizationName        = example
         organizationalUnitName    = test
         commonName                = examplepetstore.com
         emailAddress              = test@examplepetstore.com
         
         EOF
         

  2. Create the CSR (`server.csr`) for the server certificate.
         
         openssl req -new \
             -sha256 -newkey rsa:2048 -nodes \
             -config server.config \
             -keyout server.key -out server.csr
         

  3. Create the X.509 server certificate (`server.cert`) from the CSR. The intermediate CA uses its private key (`int.key`) and certificate (`int.cert`) to issue and sign the X.509 client certificate.
         
         openssl x509 -req \
             -CAkey int.key -CA int.cert \
             -days 365 \
             -extfile server.config \
             -extensions extension_requirements \
             -in server.csr -out server.cert
         

When the load balancer connects to the backend server, the backend server presents its certificate (`server.cert`) to authenticate itself to the load balancer, completing the backend authentication process.




## Additional SSL configuration options on an Apache web server

This optional section walks you through the process to update the SSL configuration options on an Apache server based on the server certificates that you created earlier. 

  1. Copy the server private key (`server.key`) and server certificate (`server.cert`) over to the Apache web server.
         
         cat > server.key << EOF
             -----BEGIN PRIVATE KEY-----
             [...]
             -----END PRIVATE KEY-----
             EOF
         
             sudo cp ./server.key /etc/ssl/private/server.key
             

Replace `[...]` with the PEM-encoded server private key that you created earlier.
         
         cat > server.cert << EOF
             -----BEGIN CERTIFICATE-----
             [...]
             -----END CERTIFICATE-----
             EOF
         
             sudo cp ./server.cert /etc/ssl/certs/server.cert
             

Replace `[...]` with the PEM-encoded server certificate that you created earlier.

  2. Update the SSL configuration of the Apache web server.

Update Apache's SSL configuration to enable HTTPS traffic using the specified SSL certificate and private key.
         
         sudo vi /etc/apache2/sites-available/default-ssl.conf
         
             ----
             SSLCertificateFile      /etc/ssl/certs/server.cert
             SSLCertificateKeyFile /etc/ssl/private/server.key
             ----
             

  3. Rehash the CA certificates.
         
         sudo c_rehash /etc/ssl/certs/
             

  4. Restart the Apache web server to apply the changes.
         
         sudo systemctl restart apache2.service
             




## What's next

  * [Set up backend mTLS](https://docs.cloud.google.com/load-balancing/docs/backend-mtls-setup)
  * [mTLS overview](https://docs.cloud.google.com/load-balancing/docs/mtls)
  * [Set up mTLS with a private CA](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ca-ccm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
