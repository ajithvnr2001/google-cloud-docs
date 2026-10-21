---
url: https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-load-balancing/
title: Create managed workload identities for load balancers \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:02.674736+00:00
---

# Create managed workload identities for load balancers  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-load-balancing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Create managed workload identities for load balancers Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to configure a managed workload identity on the backend service of a load balancer. After you assign a managed identity, the load balancer and its backends can mutually authenticate each other by using backend mTLS.

## Process overview

To configure backend mTLS using a managed workload identity, you must have a configured workload identity pool.

If you don't have a configured workload identity pool, you need to set up a workload identity pool and then attach the managed workload identity to the backend service of the load balancer.

  1. Set up a workload identity pool.

     1. Configure a Certificate Authority Service certificate authority (CA) pool to issue X.509 certificates for managed workload identities.
     2. Configure a trust domain by creating a workload identity pool with a namespace, a managed identity, an attestation policy, an inline certificate issuance config resource, and an inline trust config resource.
     3. Authorize managed workload identities to request certificates from the CA pool.
  2. Attach the managed workload identity to the backend service of the load balancer.




This example in this document walks you through the process of setting up a new workload identity pool followed by attaching a managed workload identity to the backend service of the load balancer.

If you already have an existing workload identity pool, you can adhere to the following approach:

  1. You may add a new attestation policy for your load balancer's backend service resource to participate in the workload identity pool.

  2. Attach the managed workload identity to the backend service of the load balancer.




## Before you begin

  1. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  2. Review the [backend mTLS with managed workload identities overview](https://docs.cloud.google.com/load-balancing/docs/managed-workload-identities-load-balancers-overview) document.

  3. Learn about certificate issuance using [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service).

  4. Enable the IAM, Certificate Authority Service, Compute Engine, Certificate Manager, and Network Security APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable iam.googleapis.com privateca.googleapis.com compute.googleapis.com certificatemanager.googleapis.com  networksecurity.googleapis.com

  5. Configure the Google Cloud CLI to use the project that was added to the allowlist for billing and quota.
         
         gcloud config set billing/quota_project PROJECT_ID
         

Replace `PROJECT_ID` with your Google Cloud project name.

  6. Create a managed identity for the backend. To learn more, see [Managed workload identities overview](https://docs.cloud.google.com/iam/docs/managed-workload-identity).




### Required roles

To get the permissions that you need to create managed workload identities and provision managed workload identity certificates, ask your administrator to grant you the following IAM roles on the project: 

  * To create and configure managed workload identities: 
    * [IAM Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`)
    * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * To create and configure CA pools: [CA Service Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.admin) (`roles/privateca.admin`) 
  * To create load balancer resources such as `TargetHTTPSProxy`: [Compute Load Balancer Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`) 
  * To use Certificate Manager resources: [Certificate Manager Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.owner) (`roles/certificatemanager.owner`) 
  * To create security and networking components: 
    * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
    * [Compute Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)
  * To create a project (optional): [Project Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectCreator) (`roles/resourcemanager.projectCreator`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure CA Service to issue certificates for managed workload identities

You can use [CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool) to set up a root CA. A CA pool issues the X.509 certificates to managed workload identities.

Note the following CA pool location requirements:

  * For a global backend service, a CA pool can be in any region as there are no global CA pools.

  * For a regional backend service, a CA pool must be in the same region as the backend service.




### Create a root CA pool

To create a root CA pool in the _Enterprise_ tier, use the [`gcloud privateca pools create` command](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/create). This tier is meant for long-lived, low-volume certificate issuance.
    
    
    gcloud privateca pools create ROOT_CA_POOL_ID \
        --location=REGION \
        --project=PROJECT_ID \
        --tier=enterprise
    

Replace the following:

  * `ROOT_CA_POOL_ID`: a unique ID for the root CA pool

  * `REGION`: the region where the root CA pool is located

  * `PROJECT_ID`: the project ID




To learn more about CA pools, see [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).

### Create a root CA

Create a root CA in the root CA pool by using the [`gcloud privateca roots create` command](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/create).

To create a root CA, run the following command:
    
    
    gcloud privateca roots create ROOT_CA_ID \
        --pool=ROOT_CA_POOL_ID \
        --subject="CN=ROOT_CA_CN, O=ROOT_CA_ORGANIZATION" \
        --key-algorithm="KEY_ALGORITHM" \
        --location=REGION \
        --project=PROJECT_ID \
        --auto-enable
    

Replace the following:

  * `ROOT_CA_ID`: a unique name for the root CA. The CA name can be up to 64 characters in length and must contain only lowercase and uppercase alphanumeric characters, underscores, or hyphens. The CA name must be unique within the region.
  * `ROOT_CA_POOL_ID`: the ID of the root CA pool.
  * `ROOT_CA_CN`: the common name of the root CA.
  * `ROOT_CA_ORGANIZATION`: the organization of the root CA.
  * `KEY_ALGORITHM`: the algorithm to use for creating a Cloud KMS key. This flag is optional. If you don't include this flag, the key algorithm defaults to `rsa-pkcs1-4096-sha256`.
  * `REGION`: the region where the root CA pool is located.
  * `PROJECT_ID`: the project ID.

**Note:** This example uses a single root CA to issue workload certificates. In a production environment, the recommended best practice is to use a two-tier CA hierarchy—an Enterprise tier root CA that issues a certificate to a DevOps tier subordinate CA. The subordinate CA is then used to issue the high-volume, short-lived workload certificates.

To learn more about a root CA, see [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities).

## Configure a workload identity pool

When you use managed workload identities, Google Cloud can automatically provision and manage X.509 certificates from the [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service). Workload identities are defined within a workload identity pool, and are organized into administrative boundaries called _namespaces_.

### Create a workload identity pool

You must create a pool in `TRUST_DOMAIN` mode to create managed workload identities. To create a workload identity pool for managed workload identities, use the `gcloud iam workload-identity-pools create` command.
    
    
    gcloud iam workload-identity-pools create WORKLOAD_IDENTITY_POOL_ID \
        --location="global" \
        --mode="TRUST_DOMAIN"
    

Replace `WORKLOAD_IDENTITY_POOL_ID` with the unique ID for the pool. The ID must be between 4 and 32 characters, contain only lowercase alphanumeric characters and dashes, and must start and end with an alphanumeric character. After you create a workload identity pool, you can't change its ID.

To verify that your workload identity pool was created in `TRUST_DOMAIN` mode, use the `gcloud iam workload-identity-pools describe` command.
    
    
    gcloud iam workload-identity-pools describe WORKLOAD_IDENTITY_POOL_ID \
        --location="global"
    

The output is similar to the following:
    
    
    mode: TRUST_DOMAIN
    name: projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/WORKLOAD_IDENTITY_POOL_ID
    state: ACTIVE
    

This output includes the following values:

  * `PROJECT_NUMBER`: the project number of your Google Cloud project
  * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID



### Create a namespace

The `gcloud iam workload-identity-pools namespaces create` command lets you create a namespace in a workload identity pool.
    
    
    gcloud iam workload-identity-pools namespaces create NAMESPACE_ID \
        --workload-identity-pool="WORKLOAD_IDENTITY_POOL_ID" \
        --location="global"
    

Replace the following:

  * `NAMESPACE_ID`: the unique ID for the namespace. The ID must be between 2 and 63 characters, contain only lowercase alphanumeric characters and dashes, and must start and end with an alphanumeric character. After you create a namespace, you cannot change its ID.
  * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID that you created earlier.



### Create a managed workload identity

The `gcloud iam workload-identity-pools managed-identities create` command lets you create a managed workload identity in a workload identity pool namespace.
    
    
    gcloud iam workload-identity-pools managed-identities create MANAGED_IDENTITY_ID \
        --namespace="NAMESPACE_ID" \
        --workload-identity-pool="WORKLOAD_IDENTITY_POOL_ID" \
        --location="global"
    

Replace the following:

  * `MANAGED_IDENTITY_ID`: the unique ID for the managed identity. The ID must be between 2 and 63 characters, contain only lowercase alphanumeric characters and dashes, and must start and end with an alphanumeric character. After you create a managed workload identity, you cannot change its ID.
  * `NAMESPACE_ID`: the namespace ID that you created earlier.
  * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID that you created earlier.



Your managed workload identity ID is the SPIFFE identifier, which is formatted as follows:
    
    
    spiffe://WORKLOAD_IDENTITY_POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID
    

### Create an attestation policy

In this example, an attestation policy contains an attestation rule that verifies whether the backend service is a part of a specific project. If the attestation policy verification passes, IAM requests an X.509 certificate for the managed identity from the Certificate Authority Service.

To create an attestation policy, run the following command to add an attestation rule.
    
    
    gcloud iam workload-identity-pools managed-identities add-attestation-rule MANAGED_IDENTITY_ID \
        --namespace=NAMESPACE_ID \
        --workload-identity-pool=WORKLOAD_IDENTITY_POOL_ID \
        --google-cloud-resource='//compute.googleapis.com/projects/PROJECT_NUMBER/type/BackendService/*' \
        --location=global
    

Replace the following:

  * `MANAGED_IDENTITY_ID`: the unique ID for the managed identity. The ID must be between 2 and 63 characters, contain only lowercase alphanumeric characters and dashes, and must start and end with an alphanumeric character. After you create a managed workload identity, you cannot change its ID.
  * `NAMESPACE_ID`: the namespace ID that you created earlier.
  * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID that you created earlier.
  * `PROJECT_NUMBER`: the project number of the Google Cloud project.



### Create an inline certificate issuance config

To bind a CA to a workload identity pool, the workload identity pool needs to have an [inline certificate issuance config](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#inlinecertificateissuanceconfig).

To configure an inline certificate issuance config, create a JSON-formatted configuration file (`cic.json`).
    
    
    cat << EOF > cic.json
    {
      "inlineCertificateIssuanceConfig": {
          "caPools": {
            "REGION": "projects/PROJECT_NUMBER/locations/REGION/caPools/ROOT_CA_POOL_ID",
          },
          "lifetime": "CERTIFICATE_LIFETIME",
          "rotationWindowPercentage": ROTATION_WINDOW_PERCENTAGE,
          "keyAlgorithm": "ALGORITHM"
      }
    }
    EOF
    

Replace the following:

  * `REGION`: the region where the CA is located.

  * `PROJECT_NUMBER`: the project number. To get the project number from the project specified by the `PROJECT_ID` variable, run the following command:
        
        gcloud projects describe PROJECT_ID --format="value(projectNumber)"
        

  * `ROOT_CA_POOL_ID`: the ID of the root CA pool.

  * `CERTIFICATE_LIFETIME`: lifetime of the workload certificates issued by the CA pool in seconds—for example: 86400s (for 24h). `CERTIFICATE_LIFETIME` must be a value between 24 hours and 30 days. If `CERTIFICATE_LIFETIME` isn't specified, certificate lifetime defaults to 24 hours. `CERTIFICATE_LIFETIME` is optional.

  * `ROTATION_WINDOW_PERCENTAGE`: the percentage of the certificate's lifetime at which a renewal triggers. The value of `ROTATION_WINDOW_PERCENTAGE` must be between 50 and 80. The default is 50. `ROTATION_WINDOW_PERCENTAGE` is optional.

  * `ALGORITHM`: the encryption algorithm used to generate the private key. Valid values for `ALGORITHM` are `ECDSA_P256` (default), `ECDSA_P384`, `RSA_2048`, `RSA_3072`, and `RSA_4096`. `ALGORITHM` is optional.




After you create the inline certificate issuance configuration file, you need to update the workload identity pool with the CA's certificate issuance config.

### Create an inline trust config (Optional)

Workloads within the same workload identity pool trust domain receive certificates and trust anchors that enable authentication by default within the trust domain. If you want workloads that are in _different_ trust domains to mutually authenticate, then you need to explicitly declare the trust relationship in the workload identity pool. You do this by creating an [`inlineTrustConfig`](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools#inlinetrustconfig) that recognizes and accepts certificates from other trust domains, thereby enabling trust federation across different trust domains.

The trust domain can be one of the following:

  * _External trust domains (such as`example.com`)_: you can establish trust with external or custom systems (such as an on-premises environment, a third-party service, or custom PKI infrastructure), provided you have their PEM-encoded CA certificate.

  * _Different workload identity pool_ : you can configure trust with a different Google Cloud workload identity pool (for example, one located in a different project). If that pool uses a custom CA, you must have its PEM-encoded CA certificate. If it uses the Google-managed default CA, you can enable trust by setting the `trustDefaultSharedCa` field to `true` instead of providing certificates.

  * _Same workload identity pool_ : a trust domain automatically trusts itself, so you don't need to specify it here. However, if you explicitly add your own pool's trust domain to this configuration, the custom trust anchors are _appended_ to the trust bundle automatically derived from the CA pools specified in your certificate issuance configuration.




The trust config file maps these trust domains to a set of trust anchors (either PEM-encoded CA certificates or built-in Google-managed CAs) that managed workload identity uses to validate peer certificates from other trust domains.

To create an inline trust config, do the following:

  1. For a custom CA, download the certificates for a trust domain that uses a custom CA.
         
         gcloud privateca pools get-ca-certs ROOT_CA_POOL_ID \
             --output-file=CERTIFICATE_PATH \
             --location=REGION
         

Replace the following:

     * `ROOT_CA_POOL_ID`: the ID of the root CA pool
     * `CERTIFICATE_PATH`: the path to which to output the PEM-encoded certificate
     * `REGION`: the region of the root CA pool
  2. Create a JSON-formatted configuration file (`tc.json`) that contains your inline trust configuration, with PEM-encoded certificates that you downloaded in the preceding step.
         
         cat << EOF > tc.json
         {
           "inlineTrustConfig": {
             "additionalTrustBundles": {
               "TRUST_DOMAIN_NAME1": {
                 "trustDefaultSharedCa": true
               },
               "TRUST_DOMAIN_NAME2": {
                 "trustAnchors": [
                   {
                       "pemCertificate": "CERTIFICATE_MATERIAL1"
                   }
                 ]
               },
               "TRUST_DOMAIN_NAME3": {
                 "trustAnchors": [
                   {
                       "pemCertificate": "CERTIFICATE_MATERIAL2"
                   }
                 ]
               }
             }
           }
         }
         EOF
         

Replace the following:

     * `TRUST_DOMAIN_NAME1`: the name of the trust domain that uses the Google-managed default CA.

     * `TRUST_DOMAIN_NAME2` and `TRUST_DOMAIN_NAME3`: a SPIFFE trust domain name. It can be a custom domain (like `example.com`), a different workload identity pool's trust domain, or even the same workload identity pool's trust domain. If you specify the current workload identity pool's trust domain, the provided trust anchors are appended to the automatically derived trust bundle.

For a workload identity pool trust domain, the trust domain name is formatted as follows:
           
           WORKLOAD_IDENTITY_POOL_ID.global.PROJECT_NUMBER.workload.id.goog
           

In the format, replace the following:

       * `WORKLOAD_IDENTITY_POOL_ID`: the ID of the workload identity pool
       * `PROJECT_NUMBER`: the project number of the project that contains the workload identity pool
     * `CERTIFICATE_MATERIAL`: the PEM-encoded CA certificate trusted to issue certificates in the trust domain. To format a PEM-encoded certificate file into a one-line string, run the following command:
           
           cat trust-anchor.pem | sed 's/^[ ]*//g' | sed -z '$ s/\n$//' | tr '\n' $ | sed 's/\$/\\n/g'
           

After you create the inline trust config, you need to update the workload identity pool with the trust configuration.




### Update the workload identity pool

To bind the CA to the workload identity pool, you need to update the workload identity pool with the CA's certificate issuance config using the `--inline-certificate-issuance-config-file` flag. If you have created an inline trust config, you need to update the workload identity pool with the trust configuration using the `--inline-trust-config-file` flag.
    
    
    gcloud iam workload-identity-pools update WORKLOAD_IDENTITY_POOL_ID \
        --location="global" \
        --inline-certificate-issuance-config-file=CIC_JSON_FILE_PATH \
        --inline-trust-config-file=TC_JSON_FILE_PATH \
        --project=PROJECT_ID
    

Replace the following:

  * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID.

  * `CIC_JSON_FILE_PATH`: the path to the JSON-formatted configuration file (`cic.json`) for the inline certificate issuance config that you created earlier.

  * `TC_JSON_FILE_PATH`: the path to the JSON-formatted configuration file (`tc.json`) for the inline trust config that you created earlier. If your workloads authenticate across different trust domains, you must specify this file. Otherwise, you can omit `--inline-trust-config`.




**Verify that the workload identity pool was updated**

To verify that your workload identity pool was updated with the certificate issuance config and the trust config, run the following command:
    
    
    gcloud iam workload-identity-pools describe WORKLOAD_IDENTITY_POOL_ID \
        --location="global" \
        --project=PROJECT_ID
    

Replace the following:

  * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID.

  * `PROJECT_ID`: the project ID




The output is similar to the following:
    
    
    inlineCertificateIssuanceConfig:
        caPools:
          REGION: projects/PROJECT_NUMBER/locations/REGION1/caPools/ROOT_CA_POOL_ID
        keyAlgorithm: ALGORITHM
        lifetime: CERTIFICATE_LIFETIME
        rotationWindowPercentage: ROTATION_WINDOW_PERCENTAGE
    inlineTrustConfig:
        additionalTrustBundles:
          TRUST_DOMAIN_NAME1:
              trustAnchors:
              - pemCertificate: |-
                -----BEGIN CERTIFICATE-----
                CERTIFICATE_MATERIAL1
                -----END CERTIFICATE-----
              - pemCertificate: |-
                -----BEGIN CERTIFICATE-----
                CERTIFICATE_MATERIAL2
                -----END CERTIFICATE-----
          TRUST_DOMAIN_NAME2:
              trustAnchors:
              - pemCertificate: |-
                -----BEGIN CERTIFICATE-----
                CERTIFICATE_MATERIAL3
                -----END CERTIFICATE-----
              - pemCertificate: |-
                -----BEGIN CERTIFICATE-----
                CERTIFICATE_MATERIAL4
                -----END CERTIFICATE-----
    mode: TRUST_DOMAIN
    name: projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/WORKLOAD_IDENTITY_POOL_ID
    state: ACTIVE
    

This output includes the following values:

  * `PROJECT_NUMBER`: the project number
  * `REGION`: the region where the root CA pool is located
  * `ROOT_CA_POOL_ID`: the ID of the root CA pool
  * `ALGORITHM`: the encryption algorithm used to generate the private key
  * `CERTIFICATE_LIFETIME`: the lifetime of the workload certificates issued by the CA pool in seconds
  * `ROTATION_WINDOW_PERCENTAGE`: the percentage of the certificate's lifetime at which a renewal triggers.
  * `TRUST_DOMAIN_NAME`: the trust domain can be any trust domain (like "example.com"), including another (or even the same) workload identity pool trust domain.
  * `CERTIFICATE_MATERIAL`: the PEM-encoded CA certificate trusted to issue certificates in the trust domain
  * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID



If `inlineCertificateIssuanceConfig` or `inlineTrustConfig` isn't present in the output, verify that you've correctly configured your gcloud CLI to use the correct project for billing and quota. You might need to update to a newer version of the gcloud CLI.

## Authorize managed workload identities to request X.509 certificates from the CA pool

After you bind the CA to the workload identity pool, grant the necessary IAM permissions to its trust domain. This allows the managed workload identities to request X.509 certificates from the CA pool.

  1. Grant the [CA Service Workload Certificate Requester role](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.workloadCertificateRequester) (`roles/privateca.workloadCertificateRequester`) to the trust domain. This role authorizes the trust domain to request new certificates for its workloads from the CA Service.
         
         gcloud privateca pools add-iam-policy-binding ROOT_CA_POOL_ID \
             --location=REGION \
             --role=roles/privateca.workloadCertificateRequester \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/name/locations/global/workloadIdentityPools/WORKLOAD_IDENTITY_POOL_ID" \
             --project=PROJECT_ID
         

Replace the following:

     * `ROOT_CA_POOL_ID`: the ID for the root CA pool
     * `REGION`: the region of the root CA pool
     * `PROJECT_NUMBER`: the project number

To get `PROJECT_NUMBER` from `PROJECT_ID`, run the following command:
           
           gcloud projects describe PROJECT_ID --format="value(projectNumber)"
           

     * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID

     * `PROJECT_ID`: the project ID

  2. Grant the [CA Service Pool Reader role](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.poolReader) (`roles/privateca.poolReader`) to the trust domain. This role authorizes the trust domain to download the signed X.509 certificate chain, establishing the CA's trust anchor.
         
         gcloud privateca pools add-iam-policy-binding ROOT_CA_POOL_ID \
             --location=REGION \
             --role=roles/privateca.poolReader \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/name/locations/global/workloadIdentityPools/WORKLOAD_IDENTITY_POOL_ID" \
             --project=PROJECT_ID
         

Replace the following:

     * `ROOT_CA_POOL_ID`: the ID of the root CA pool
     * `REGION`: the region of the root CA pool
     * `PROJECT_NUMBER`: the project number
     * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID
     * `PROJECT_ID`: the project ID



## Create the load balancer and assign the managed identity to the backend service

Managed identity can only be assigned when creating the backend service.

The steps in this section only pertain to assigning a managed identity to the backend service of the load balancer. This is part of the _backend configuration_ of the load balancer.

To set up an Application Load Balancer, you can follow the steps as defined in one of the following setup pages:

  * [Set up a global external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute).

  * [Set up a regional external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-migs).

  * [Set up a cross-region internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-migs).

  * [Set up a regional internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs).




At the stage where you are setting up the _backend service_ of the load balancer, you need to additionally do the following:

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list/loadBalancers)

  2. In the **Backend configuration** section, add the [relevant details to create a backend service](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute#load-balancer).

  3. Expand the **Advanced configurations** section.

  4. In the **Backend authentication** section, select the **Managed Identity** option.

  5. To assign a managed identity to the backend service, in the **Managed Identity** field, enter the managed workload identity that you created earlier.

  6. Click **Create**.

  7. To finish configuring the load balancer, continue the steps as outlined in one of the aforementioned setup pages.




###  gcloud 

  1. To assign a managed identity to the backend service, add the `--identity` flag while using the [`gcloud compute backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create).

### global

For global external Application Load Balancers and cross-region internal Application Load Balancers, use the `--global` flag.
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --protocol=HTTPS \
               --health-checks=HEALTH_CHECK_NAME \
               --identity='//WORKLOAD_IDENTITY_POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID' \
               --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service
     * `HEALTH_CHECK_NAME`: the name of the health check
     * `WORKLOAD_IDENTITY_POOL_ID`: workload identity pool ID
     * `PROJECT_NUMBER`: the project number
     * `NAMESPACE_ID`: the namespace ID
     * `MANAGED_IDENTITY_ID`: the managed identity ID

### regional

For regional external Application Load Balancers and regional internal Application Load Balancers, use the `--region` flag.
    
    gcloud compute backend-services create BACKEND_SERVICE_NAME \
          --load-balancing-scheme=EXTERNAL_MANAGED \
          --protocol=HTTPS \
          --health-checks=HEALTH_CHECK_NAME \
          --identity='//WORKLOAD_IDENTITY_POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID' \
          --region=REGION
    

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service
     * `HEALTH_CHECK_NAME`: the name of the health check
     * `WORKLOAD_IDENTITY_POOL_ID`: workload identity pool ID
     * `PROJECT_NUMBER`: the project number
     * `NAMESPACE_ID`: the namespace ID
     * `MANAGED_IDENTITY_ID`: the managed identity ID
     * `REGION`: the name of the Google Cloud region where the backend service is located




## Automatically created resources

After a managed identity is configured on the backend service of the load balancer, the following resources are automatically created by managed workload identity:

  * Backend authentication config: attached to the backend service of the load balancer
  * Certificate Manager managed identity certificate: attached to the backend authentication config
  * Certificate Manager trust config: attached to the backend authentication config



The following sections are related to verifying your configuration to check whether the automatically created resources have been configured.

## Verify your configuration

Verify your configuration to check whether the automatically created resources have been configured.

The automatically created resources have an `mi` prefix, which indicates that the resource is created by managed workload identity.

### Verify the creation of the backend authentication config and managed identity

To verify the creation of the backend authentication config and managed identity, use the [`gcloud compute backend-services describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/describe) to describe the backend service.
    
    
    gcloud compute backend-services describe BACKEND_SERVICE_NAME --global
    

The output is similar to the following:
    
    
    affinityCookieTtlSec: 0
    connectionDraining:
      drainingTimeoutSec: 0
    creationTimestamp: '2025-11-06T02:15:43.680-08:00'
    description: ''
    enableCDN: false
    fingerprint: lTZwas8aylg=
    healthChecks:
    - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/healthChecks/HEALTH_CHECK_NAME
    id: '719352032'
    kind: compute#backendService
    loadBalancingScheme: EXTERNAL_MANAGED
    name: BACKEND_SERVICE_NAME
    port: 80
    portName: PORT_NAME
    protocol: HTTPS
    selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME
    sessionAffinity: NONE
    timeoutSec: 30
    tlsSettings:
      authenticationConfig: //networksecurity.googleapis.com/projects/PROJECT_ID/locations/global/backendAuthenticationConfigs/mi-bac-423b651f-d549-4a9f-a4f2-g2bcaa7108bd
      identity: //WORKLOAD_IDENTITY_POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID
    

This output includes the following values:

  * `PROJECT_ID`: the project ID
  * `HEALTH_CHECK_NAME`: the name of the health check
  * `BACKEND_SERVICE_NAME`: the name of the backend service
  * `PORT_NAME`: the port name
  * `REGION`: the region where the root CA pool is located
  * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID
  * `PROJECT_NUMBER`: the project number
  * `NAMESPACE_ID`: the namespace ID
  * `MANAGED_IDENTITY_ID`: the managed identity ID



The backend authentication config is created automatically and is attached to the `backendService.tlsSettings.authenticationConfig` field. The backend authentication config starting with the `mi` prefix is referred to as `MI_BACKEND_AUTHENTICATION_CONFIG_ID` in the following section.

The managed workload identity is also attached to the `backendService.tlsSettings.identity` field. It has the following format:
    
    
    //WORKLOAD_IDENTITY_POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID
    

**Note:** The `spiffe` prefix isn't used in the `identity` field of the backend service (`backendService.tlsSettings.identity`). However, the `spiffe` prefix is used when it is represented as a URI in the Subject Alternative Name (SAN) of an X.509 certificate.

### Verify the creation of the Certificate Manager managed identity certificate and the Certificate Manager trust config

To verify that the Certificate Manager managed identity certificate and the Certificate Manager trust config are attached to the backend authentication config resource, use the [`gcloud network-security backend-authentication-configs describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/backend-authentication-configs/describe).
    
    
    gcloud network-security backend-authentication-configs describe MI_BACKEND_AUTHENTICATION_CONFIG_ID \
        --location=global
    

The output is similar to the following:
    
    
    clientCertificate: projects/PROJECT_NUMBER/locations/global/certificates/mi-crt-181fa461-3b53-40fa-8515-507d47337c5d
    createTime: '2025-11-06T10:15:56.237734973Z'
    etag: xwyxl1VYVoh4QIwf3nhKhAVXgcuOqoN7xdqAiS8Esvs
    name: projects//locations/global/backendAuthenticationConfigs/mi-bac-477b381f-d349-4a8f-a6f2-f2bbaa7109bd
    trustConfig: projects/PROJECT_NUMBER/locations/global/trustConfigs/mi-tc-e4f05160-f20f-4109-aae3-4c1a68891742
    updateTime: '2025-11-06T10:16:01.964275141Z'
    

The `clientCertificate` and the `trustConfig` are automatically created by managed workload identity and attached to the backend authentication config resource.

The `clientCertificate` starting with the `mi` prefix is referred to as `MI_CLIENT_CERTIFICATE_ID` in the following section.

The `trustConfig` starting with the `mi` prefix is referred to as `MI_TRUST_CONFIG_ID` in the following section.

### Verify that the Certificate Manager certificate is a managed identity certificate

To view the details of the Certificate Manager managed identity certificate, use the [`gcloud certificate-manager certificates describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/describe).
    
    
    gcloud certificate-manager certificates describe MI_CLIENT_CERTIFICATE_ID
    

The output is similar to the following:
    
    
    createTime: '2025-11-06T10:15:46.187892797Z'
    expireTime: '2025-11-07T22:55:47Z'
    extendedKeyUsage:
      clientAuth: true
    managedIdentity:
      identity: //WORKLOAD_IDENTITY_POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID
      state: ACTIVE
    name: projects/PROJECT_ID/locations/global/certificates/mi-crt-181fa461-3b53-40fa-8515-507d47337c5d
    pemCertificate: -----BEGIN CERTIFICATE-----\nCERTIFICATE_MATERIAL\n-----END CERTIFICATE-----
    scope: CLIENT_AUTH
    updateTime: '2025-11-06T10:15:49.427339950Z'
    usedBy:
    - name: //networksecurity.googleapis.com/projects/PROJECT_NUMBER/locations/global/backendAuthenticationConfigs/mi-bac-477b381f-d349-4a8f-a6f2-f2bbaa7109bd
    

This output includes the following values:

  * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID
  * `PROJECT_NUMBER`: the project number
  * `NAMESPACE_ID`: the namespace ID
  * `MANAGED_IDENTITY_ID`: the managed identity ID
  * `CERTIFICATE_MATERIAL`: the X.509-SVID in a PEM-encoded format



The Certificate Manager managed identity certificate has a `managedIdentity` property, which identifies it as a managed identity certificate. If the state of the managed identity certificate is `FAILED`, verify that the attestation policy and the necessary IAM permissions are correctly configured.

The scope of the Certificate Manager managed identity certificate is `CLIENT_AUTH`, which indicates that this certificate is used as a client certificate in backend mTLS.

The Certificate Manager managed identity certificate resource stores the X.509-SVID in a PEM-encoded format.

### Verify that the SPIFFE ID is a part of the SAN in the X.509-SVID

The X.509-SVID contains the SPIFFE ID encoded as a URI in the SAN field. This SPIFFE ID corresponds to the managed identity in the workload identity pool.

**Note:** The `spiffe` prefix is not used in the `identity` field of the backend service (`backendService.tlsSettings.identity`). However, the `spiffe` prefix is used when it is represented as a URI in the SAN of an X.509 certificate.

To print a human-readable format of the certificate, run the following command:
    
    
    echo -e \
    "-----BEGIN CERTIFICATE-----\nCERTIFICATE_MATERIAL\n-----END CERTIFICATE-----" | openssl x509 -text -noout
    

The output is similar to the following (abridged):
    
    
    Certificate:
        Data:
            Version: 3 (0x2)
            Signature Algorithm: ecdsa-with-SHA256
            Issuer: O = example.com, CN = Example CA
            Validity
                Not Before: Nov  6 10:15:48 2025 GMT
                Not After : Nov  7 10:15:47 2025 GMT
            Subject:
            Subject Public Key Info:
                Public Key Algorithm: id-ecPublicKey
                    Public-Key: (256 bit)
            X509v3 extensions:
                X509v3 Subject Alternative Name: critical
                    URI:spiffe://WORKLOAD_IDENTITY_POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID
    

This output includes the following values:

  * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID
  * `PROJECT_NUMBER`: the project number
  * `NAMESPACE_ID`: the namespace ID
  * `MANAGED_IDENTITY_ID`: the managed identity ID



### Verify that the Certificate Manager trust config contains the `spiffeTrustStores` field

The Certificate Manager trust config contains a field called `spiffeTrustStores`. The `spiffeTrustStores` field contains the trust bundle associated with the trust domain of the workload identity pool (represented by ``WORKLOAD_IDENTITY_POOL_ID`.global.`PROJECT_NUMBER`.workload.id.goog` in the output) and any additional trust bundles specified by the `additionalTrustBundles` field in the workload identity pool's inline trust config.

To view the details of the Certificate Manager trust config, use the [`gcloud certificate-manager trust-configs describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/describe).
    
    
    gcloud certificate-manager trust-configs describe MI_TRUST_CONFIG_ID
    

Replace `MI_TRUST_CONFIG_ID` with the trust config automatically created by managed identity.

In the following example output, the host `example.com` is the additional trust domain to which trust is extended.

If the `spiffeTrustStores` field doesn't contain the expected trust bundles, verify that the attestation policy and the necessary IAM permissions are correctly configured.
    
    
    createTime: '2025-11-06T10:15:50.048030758Z'
    etag: kDoKfm5W6Il2HPvduKZWpuYpyrKrNVq4jqMEICE-6rQ
    name: projects/PROJECT_ID/locations/global/trustConfigs/mi-tc-e4f05160-f20f-4109-aae3-4c1a68891742
    spiffeTrustStores:
      example.com:
        trustAnchors:
        - pemCertificate: -----BEGIN CERTIFICATE-----\nCERTIFICATE_MATERIAL1\n-----END CERTIFICATE-----
      WORKLOAD_IDENTITY_POOL_ID.global.PROJECT_NUMBER.workload.id.goog:
        trustAnchors:
        - pemCertificate: -----BEGIN CERTIFICATE-----\nCERTIFICATE_MATERIAL2\n-----END CERTIFICATE-----
    updateTime: '2025-11-07T08:25:15.760754841Z'
    

This output includes the following values:

  * `PROJECT_ID`: the project ID
  * `CERTIFICATE_MATERIAL`: the PEM-encoded CA certificate trusted to issue certificates in the trust domain
  * `WORKLOAD_IDENTITY_POOL_ID`: the workload identity pool ID
  * `PROJECT_NUMBER`: the project number
  * `MANAGED_IDENTITY_ID`: the managed identity ID



To learn more about the Certificate Manager trust config, see [Certificate Manager trust config](https://docs.cloud.google.com/load-balancing/docs/managed-workload-identities-load-balancers-overview#certificate-manager-trust-config).

## What's next

  * [Configure managed workload identity authentication for Compute Engine](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities)
  * [Authenticate workloads to other workloads over mTLS](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
