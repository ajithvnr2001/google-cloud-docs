---
url: https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-gke/
title: Configure managed workload identity authentication for GKE \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:58.915188+00:00
---

# Configure managed workload identity authentication for GKE  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure managed workload identity authentication for GKE Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure [managed workload identities](https://docs.cloud.google.com/iam/docs/managed-workload-identity) for Google Kubernetes Engine (GKE) in your GKE fleet-managed clusters. It also describes how to deploy a workload and verify the workload's identity and certificate.

To set up and use managed workload identities for GKE, complete the following steps:

  1. Choose a certificate authority (CA) option

  2. Configure your certificate authority

  3. Deploy workloads with managed workload identities

  4. Optional: Enable trust federation between workload identity pools




### Google-managed workload identity pool

When you add clusters to GKE fleets, GKE automatically creates a Google-managed workload identity pool, which serves as the root of trust, also known as the SPIFFE trust domain for your workloads. All workloads within the trust domain receive certificates and trust anchors that enable authentication by default within the trust domain. If you have multiple trust domains, you can enable trust federation between them to enable cross-trust domain communication.

The Google-managed workload identity pool has the following characteristics:

  * **Identity management:** Google fully manages the pool. You cannot create any subresources, such as namespaces, identities, or identity providers.

  * **Workload support:** You can use the pool only for GKE workloads. You cannot add other types of workloads, such as Compute Engine VMs, to the pool.

  * **Fleet integration:** All clusters in the pool are subject to the standard Kubernetes namespace sameness model. This means that all clusters in the pool are equivalently privileged, and workloads on any cluster in the pool can use any identity within that pool.




### Self-managed workload identity pool

In mixed-trust environments, such as multi-tenant fleets, you can configure a separate self-managed workload identity pool for a subset of your workloads and clusters. A self-managed workload identity pool has the following characteristics:

  * **Identity management:** By defining your own workload identity pool, you gain full control of identity management in the pool. Under the pool, you can define your own identity hierarchy, such as namespaces and identities. You can define attestation policies to specify which workloads can attest identities under the pool or namespaces.

  * **Workload support:** Any workload (for example, VMs, containers, and serverless workloads) can be placed under the pool.

  * **Fleet integration:** For workloads managed by GKE fleets, fleets provide an integrated interface to manage identities. You can configure your workload identity pool as the fleet scope-tenancy pool. Fleets automatically create workload identity pool namespaces corresponding to the fleet namespaces, and assign identities to the workloads.




To use a self-managed workload identity pool, you must configure fleet team management features like team scopes and fleet namespaces, and set up the self-managed pool as the scope-tenancy pool. For instructions about creating and configuring a self-managed pool, see [Authenticate to Google Cloud APIs from mixed-trust fleet workloads](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/authenticate-mixed-trust-workloads).

### Multi-project configuration

Google Cloud resources that you use in this document, such as GKE clusters, the root CA, and subordinate CAs, can exist in separate projects. When you refer to these resources, use the `--project` flag to specify the correct project for each resource.

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

  2. Understand [managed workload identities](https://docs.cloud.google.com/iam/docs/managed-workload-identity).

  3. Ensure your clusters run version 1.33.0-gke.2248000 or later.

  4. Add your clusters to GKE fleets. If your cluster is an Autopilot cluster, omit the `--enable-workload-identity` flag. Fleets automatically creates a Google-managed workload identity pool, which serves as a _trust domain_.

Enable GKE fleets by running the following command:
         
         gcloud container clusters update CLUSTER_NAME \
         --workload-pool=PROJECT_ID.svc.id.goog \
         --enable-fleet \
         --fleet-project=PROJECT_ID
         

Replace these values:

     * `CLUSTER_NAME`: the name of the GKE cluster to register with the GKE fleet
     * `PROJECT_ID`: the GKE fleet host project ID
  5. Enable the IAM and Certificate Authority Service APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com,iam.googleapis.com,privateca.googleapis.com&redirect=https%3A//console.cloud.google.com)

  6. Configure the Google Cloud CLI to use your billing and quota project.
         
         gcloud config set billing/quota_project PROJECT_ID
         

Replace PROJECT_ID with the ID of the fleet project.




## Required roles

To get the permissions that you need to create managed workload identities and provision managed workload identity certificates, ask your administrator to grant you the following IAM roles on the project: 

  * To create and configure managed workload identities: [IAM Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`) 
  * To create and configure CA pools: [CA Service Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.admin) (`roles/privateca.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Choose a CA option

To sign your workload certificates, choose the certificate authority (CA) option that best fits your use case:

  * **Google-managed default CA** : Use this option for a fully managed, no-cost solution. The default CA provides a shared root of trust for all Google Cloud users.

  * **Custom CA** : Use this option to configure your own public key infrastructure (PKI) through Certificate Authority Service. This option is appropriate if you require a custom root of trust or if you must store signing keys in a hardware security module (HSM) to meet compliance requirements. Certificate Authority Service is charged separately from managed workload identity. For more information, see [CA Service pricing](https://cloud.google.com/certificate-authority-service/pricing).




## Configure a CA

### Default CA

To bind the default CA to the workload identity pool, update the workload identity pool with the `use-default-shared-ca` flag.
    
    
      gcloud iam workload-identity-pools update TRUST_DOMAIN_NAME \
          --location="global" \
          --use-default-shared-ca \
          --project=PROJECT_ID
    

Replace the following:

  * `TRUST_DOMAIN_NAME`: 

The name of the trust domain. Depending on your pool type, format the name as follows:

    * **Google-managed pool:** `PROJECT_ID.svc.id.goog`
    * **Self-managed pool:** `POOL_NAME.global.POOL_HOST_PROJECT_NUMBER.workload.id.goog`
  * `PROJECT_ID`: The project ID of your fleet host project. 



### Custom CA

  1. Configure CA Service to issue certificates for managed workload identities.
  2. Bind the CAs to the workload identity pool.
  3. Authorize managed workload identities to request certificates from the CA pool.



### Configure CA Service to issue certificates for managed workload identities

To configure managed workload identities for GKE, you first need to configure a certificate authority (CA) and one or more subordinate CAs. This configuration is known as a _CA hierarchy_.

You can use [CA Service pools](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool) to set up this hierarchy. With this hierarchy, the subordinate CA pool issues the X.509 workload identity certificates to your workloads.

The CA pools configured to issue certificates for workloads using managed workload identities must reside in the same region as the workload. If you want to design a [multi-region architecture for resilience to regional outages](https://docs.cloud.google.com/architecture/framework/reliability/design-scale-high-availability#design_a_multi-region_architecture_for_resilience_to_regional_outages), we recommend that you configure a subordinate Certificate Authority Service CA pool for each region where you run workloads. By doing this, each of your workloads can reference an in-region subordinate Certificate Authority Service CA pool.

**Caution:** If you also [attach certificate issuance policies to your CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy), the issuance policy must [comply with certificate requirements for mTLS](https://docs.cloud.google.com/load-balancing/docs/mtls#certificate-requirements) to ensure that the provisioned certificates can be used for mTLS. Otherwise, the certificates might be provisioned successfully but fail when used for mTLS connections.**Note:** When you update or rotate a self-managed CA, there is a propagation latency of approximately 5 minutes before the updates take effect on the GKE clusters. This is because the `gke-spiffe-controller` checks membership and fetches trust bundles every five minutes. This latency does not occur if you use the Google-managed CA.

#### Configure your root CA pool

To create the root CA pool, do the following:

**Important:** You [cannot move or export a CA pool after it has been created](https://docs.cloud.google.com/certificate-authority-service/docs/locations#choosing-best-location).

Create the root CA pool in the _Enterprise_ tier using [`gcloud privateca pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/create). This tier is meant for long-lived, low-volume certificate issuance.
    
    
    gcloud privateca pools create ROOT_CA_POOL_ID \
        --location=REGION \
        --project=CA_PROJECT_ID \
        --tier=enterprise
    

Replace the following:

  * `ROOT_CA_POOL_ID`: A unique ID for the root CA pool. The ID can be up to 64 characters in length and must contain only lower and uppercase alphanumeric characters, underscores, or hyphens. The pool ID must be unique within the region.

  * `REGION`: The region where the root CA pool is located.

  * `CA_PROJECT_ID`: The project ID that you want to create the root CA in.




To learn more about CA pools, tiers, and regions, see [Creating CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).

#### Configure your root CA

Create a root CA in the root CA pool using [`gcloud privateca roots create`](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/create). You might be prompted to [enable the root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#enable-root) if this is the only CA in the root CA Pool.

To create a root CA, run the following command:
    
    
    gcloud privateca roots create ROOT_CA_ID \
        --pool=ROOT_CA_POOL_ID \
        --subject="CN=ROOT_CA_CN, O=ROOT_CA_ORGANIZATION" \
        --key-algorithm="KEY_ALGORITHM" \
        --max-chain-length=1 \
        --location=REGION \
        --project=CA_PROJECT_ID \
        --auto-enable
    

Replace the following:

  * `ROOT_CA_ID`: A unique name for the root CA. The CA name can be up to 64 characters in length and must contain only lower and uppercase alphanumeric characters, underscores, or hyphens. The CA name must be unique within the region.
  * `ROOT_CA_POOL_ID`: The ID of the root CA pool.
  * `ROOT_CA_CN`: The common name of the root CA.
  * `ROOT_CA_ORGANIZATION`: The organization of the root CA.
  * `KEY_ALGORITHM`: The key algorithm—for example, `ec-p256-sha256`.
  * `REGION`: The region where the root CA pool is located.
  * `CA_PROJECT_ID`: The project ID where you created the root CA.



For more information about the `subject` fields for the CA, see [Subject](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel#subject).

Optionally, you create additional root CAs in your root CA pool. Doing so can be useful for [root CA rotation](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-rotation).

#### Configure subordinate CAs

Optionally, you can configure subordinate CAs. Configuring subordinate CAs can help with the following:

  * Multiple certificate issuance scenarios: If you have multiple certificate issuance scenarios, then you can create a subordinate CA for each scenario.

  * Better load balancing: Adding multiple subordinate CAs in a CA pool helps you achieve better load balancing of certificate requests.




To create a subordinate CA pool and subordinate CA, do the following:

  1. Create the subordinate CA pool in the _DevOps_ tier, which is meant for high volume, short-lived certificate issuance.
         
         gcloud privateca pools create SUBORDINATE_CA_POOL_ID \
             --location=REGION \
             --project=CA_PROJECT_ID \
             --tier=devops
         

Replace the following:

     * `SUBORDINATE_CA_POOL_ID`: A unique ID for the subordinate CA pool. The ID can be up to 64 characters in length and must contain only lowercase and uppercase alphanumeric characters, underscores, or hyphens. The pool ID must be unique within the region.
     * `REGION`: The region in which to create the subordinate CA pool.
     * `CA_PROJECT_ID`: The ID of the project where you created the subordinate CA.

For more information, see [Creating CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).

  2. Create a subordinate CA in the subordinate CA pool. Don't change the default [config-based issuance mode](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#issuancemodes).
         
         gcloud privateca subordinates create SUBORDINATE_CA_ID \
             --pool=SUBORDINATE_CA_POOL_ID \
             --location=REGION \
             --issuer-pool=ROOT_CA_POOL_ID \
             --issuer-location=REGION \
             --subject="CN=SUBORDINATE_CA_CN, O=SUBORDINATE_CA_ORGANIZATION" \
             --key-algorithm="KEY_ALGORITHM" \
             --use-preset-profile=subordinate_mtls_pathlen_0 \
             --project=CA_PROJECT_ID \
             --auto-enable
         

Replace the following:

     * `SUBORDINATE_CA_ID`: A unique name for the subordinate CA. The name can be up to 64 characters in length and must contain only lowercase and uppercase alphanumeric characters, underscores, or hyphens. The pool name must be unique within the region.
     * `SUBORDINATE_CA_POOL_ID`: The name of the subordinate CA pool.
     * `REGION`: The region where the subordinate CA pool is located.
     * `ROOT_CA_POOL_ID`: The ID of the root CA pool.
     * `REGION`: The region of the root CA pool.
     * `SUBORDINATE_CA_CN`: The common name of the subordinate CA.
     * `SUBORDINATE_CA_ORGANIZATION`: The name of the subordinate CA issuing organization.
     * `KEY_ALGORITHM`: The key algorithm—for example, `ec-p256-sha256`.
     * `CA_PROJECT_ID`: The ID of the project where you created the subordinate CA.

For more information about the `subject` fields for the CA, see [Subject](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel#subject).




#### Create a certificate issuance configuration file

Binding CAs to workload identity pools requires a [certificate issuance config](https://docs.cloud.google.com/certificate-manager/docs/core-components#issuance-configs). If you need your workloads to authenticate across multiple trust domains, see Enable trust federation between workload identity pools (Optional).

To configure the [certificate issuance config](https://docs.cloud.google.com/certificate-manager/docs/how-it-works#issuance-configs), you create a certificate issuance config file named `cic.json`. The format of the file is similar to the following:
    
    
    {
      "inlineCertificateIssuanceConfig": {
          "caPools": {
            "REGION1": "projects/CA_PROJECT_NUMBER1/locations/REGION1/caPools/SUBORDINATE_CA_POOL_ID1",
            "REGION2": "projects/CA_PROJECT_NUMBER2/locations/REGION2/caPools/SUBORDINATE_CA_POOL_ID2"
          },
          "lifetime": "DURATION",
          "rotationWindowPercentage": ROTATION_WINDOW_PERCENTAGE,
          "keyAlgorithm": "ALGORITHM"
      }
    }
    

Replace the following:

  * `REGION`: The regions where the CAs are located.

  * `CA_PROJECT_NUMBER`: The project number of the project that in which you created the subordinate CA pool. To get the project number from CA_PROJECT_ID project, run the following command:
        
        gcloud projects describe CA_PROJECT_ID --format="value(projectNumber)"
        

  * `SUBORDINATE_CA_POOL_ID`: The name of the subordinate CA pool.

  * `ALGORITHM`: Optional. The encryption algorithm used to generate the private key. Valid values are `ECDSA_P256`, `ECDSA_P384`, `RSA_2048`, `RSA_3072`, `RSA_4096`. If not specified, `ECDSA_P256` is used as the default algorithm.

  * `DURATION`: Optional. The leaf certificate validity duration, in seconds. The value must be between 86400 (1 day) and 2592000 (30 days). If not specified, the default value of 86400 (1 day) is used. The actual validity of the issued certificate also depends on the issuing CA, because it can restrict the lifetime of the issued certificate.

  * `ROTATION_WINDOW_PERCENTAGE`: Optional: The percentage of the certificate's lifetime at which a renewal triggers. The value must be between 50 and 80. If not specified, 50 is used as the default value.




### Bind the CAs to the workload identity pool

After you create your CA hierarchy and create certificate issuance configs for each CA, you bind the CAs to the workload identity pool. To bind a CA to the workload identity pool, you update the workload identity pool with the CA's certificate issuance config. Then, you can verify that the pool was updated.

#### Update the workload identity pool

To update the pool, run the following command:
    
    
    gcloud iam workload-identity-pools update TRUST_DOMAIN_NAME \
        --location="global" \
        --inline-certificate-issuance-config-file=CIC_JSON_FILE_PATH \
        --project=PROJECT_ID
    

Replace the following:

  * `TRUST_DOMAIN_NAME`: The name of the trust domain. Depending on your pool type, format the name as follows:

    * **Google-managed pool:** `PROJECT_ID.svc.id.goog`
    * **Self-managed pool:** `POOL_NAME.global.POOL_HOST_PROJECT_NUMBER.workload.id.goog`
  * `CIC_JSON_FILE_PATH`: The path to the JSON-formatted certificate issuance config file (`cic.json`) that you created earlier.




#### Verify that the workload identity pool was updated

To verify that your workload identity pool was updated with the certificate issuance config, run the following command:
    
    
    gcloud iam workload-identity-pools describe TRUST_DOMAIN_NAME \
        --location="global" \
        --project=PROJECT_ID
    

Replace `TRUST_DOMAIN_NAME` with the trust domain name that you used to update the workload identity pool earlier in this document.

The command output is similar to the following:
    
    
    inlineCertificateIssuanceConfig:
        caPools:
          REGION1: projects/PROJECT_NUMBER1/locations/REGION1/caPools/SUBORDINATE_CA_POOL_ID1,
          REGION2: projects/PROJECT_NUMBER2/locations/REGION2/caPools/SUBORDINATE_CA_POOL_ID2
        keyAlgorithm: ALGORITHM
        lifetime: DURATION
        rotationWindowPercentage: ROTATION_WINDOW_PERCENTAGE
    mode: TRUST_DOMAIN
    name: TRUST_DOMAIN_NAME
    state: ACTIVE
    

If `inlineCertificateIssuanceConfig` isn't present in the command output, verify that you've correctly configured your gcloud CLI to use the correct project for billing and quota. You might need to update to a newer version of the gcloud CLI.

## Authorize managed workload identities to request certificates from the CA pool

After you bind the CAs to the workload identity pool, authorize managed workload identities to request certificates from the CA pool. To authorize these identities:

  1. Grant the [**CA Service Workload Certificate Requester** (`roles/privateca.workloadCertificateRequester`)](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.workloadCertificateRequester) IAM role on each subordinate CA pool to the trust domain. The following `gcloud privateca pools add-iam-policy-binding` command authorizes the trust domain to request certificates from the CA Service certificate chains.
         
         gcloud privateca pools add-iam-policy-binding SUBORDINATE_CA_POOL_ID \
             --location=REGION \
             --role=roles/privateca.workloadCertificateRequester \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/name/locations/global/workloadIdentityPools/TRUST_DOMAIN_NAME" \
             --project=CA_PROJECT_ID
         

Replace the following:

     * `SUBORDINATE_CA_POOL_ID`: The ID of the subordinate CA pool.
     * `REGION`: The region of the subordinate CA pool.
     * `PROJECT_NUMBER`: The project number of the project that contains the GKE workload identity pool.

To get `PROJECT_NUMBER` from your workload identity pool project, run the following command.
           
           gcloud projects describe WORKLOAD_IDENTITY_POOL_PROJECT_ID --format="value(projectNumber)"
           

     * `WORKLOAD_IDENTITY_POOL_PROJECT_ID`: The project ID containing the workload identity pool.

     * `TRUST_DOMAIN_NAME`: The name of the trust domain. Depending on your pool type, format the name as follows:

       * **Google-managed pool:** `PROJECT_ID.svc.id.goog`
       * **Self-managed pool:** `POOL_NAME.global.POOL_HOST_PROJECT_NUMBER.workload.id.goog`
     * `CA_PROJECT_ID`: The ID of the project where you created the subordinate CA.

  2. Grant the [CA Service Pool Reader (`roles/privateca.poolReader`)](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.poolReader) role on the subordinate CA pools to the managed workload identity. Doing so authorizes the managed workload identity to get the signed X.509 certificates from the CA's certificate chains.
         
         gcloud privateca pools add-iam-policy-binding SUBORDINATE_CA_POOL_ID \
             --location=REGION \
             --role=roles/privateca.poolReader \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/name/locations/global/workloadIdentityPools/TRUST_DOMAIN_NAME" \
             --project=CA_PROJECT_ID
         

Replace the following:

     * `SUBORDINATE_CA_POOL_ID`: The ID of the subordinate CA pool.
     * `REGION`: The region of the subordinate CA pool.
     * `PROJECT_NUMBER`: The project number of the project that contains the GKE workload identity pool.
     * `TRUST_DOMAIN_NAME`: The name of the trust domain. Depending on your pool type, format the name as follows: 
       * **Google-managed pool:** `PROJECT_ID.svc.id.goog`
       * **Self-managed pool:** `POOL_NAME.global.POOL_HOST_PROJECT_NUMBER.workload.id.goog`
     * `CA_PROJECT_ID`: The ID of the project where you created the subordinate CA.



## Deploy workloads with managed workload identities

After you configure your CA pools to issue certificates for managed workload identities, you can deploy workloads that have managed workload identities.

This section shows you how to deploy a test workload that has a managed workload identity. To do this, you deploy a Pod, check that credentials were generated, and view the certificate and the SPIFFE ID.

### Deploy a Pod

You can deploy a Pod that gets its managed workload identity from a Google-managed workload identity pool or a self-managed workload identity pool.

### Google-managed pool

To deploy a test Pod in your cluster, do the following:

  1. Get the cluster credentials.
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CLUSTER_ZONE \
             --project=CLUSTER_PROJECT_ID
         

  2. Create the Kubernetes namespace.
         
         kubectl create namespace KUBERNETES_NAMESPACE
         

  3. Deploy a test PodSpec.

**Note:** If you use an Autopilot cluster, you can omit the `nodeSelector` from your PodSpec.
         
         cat <<EOF | kubectl apply -f -
         apiVersion: v1
         kind: Pod
         metadata:
           namespace: KUBERNETES_NAMESPACE
           name: example-pod
         spec:
           containers:
           - name: main
             image: debian
             command: ['sleep', 'infinity']
             volumeMounts:
             - name: fleet-spiffe-credentials
               mountPath: /var/run/secrets/workload-spiffe-credentials
               readOnly: true
           nodeSelector:
             iam.gke.io/gke-metadata-server-enabled: "true"
           volumes:
           - name: fleet-spiffe-credentials
             csi:
               driver: podcertificate.gke.io
               volumeAttributes:
                 signerName: spiffe.gke.io/fleet-svid
                 trustDomain: fleet-project/svc.id.goog
         EOF
         




### Self-managed pool

To deploy a test Pod in your cluster using a self-managed workload identity pool, do the following:

  1. [Set up a self-managed workload identity pool and configure the fleet clusters to use this pool](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/authenticate-mixed-trust-workloads).

  2. Get the cluster credentials.
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CLUSTER_ZONE \
             --project=CLUSTER_PROJECT_ID
         

  3. Create the Kubernetes namespace.

**Note:** The Kubernetes namespace must match the fleet namespace in the team scope that you created when configuring the self-managed pool.
         
         kubectl create namespace KUBERNETES_NAMESPACE
         

  4. Deploy a test PodSpec.

The following PodSpec configures the `trustDomain` volume attribute for a self-managed workload identity pool:

**Note:** If you use an Autopilot cluster, you can omit the `nodeSelector` from your PodSpec.
         
         cat <<EOF | kubectl apply -f -
         apiVersion: v1
         kind: Pod
         metadata:
           namespace: KUBERNETES_NAMESPACE
           name: example-pod
         spec:
           containers:
           - name: main
             image: debian
             command: ['sleep', 'infinity']
             volumeMounts:
             - name: fleet-spiffe-credentials
               mountPath: /var/run/secrets/workload-spiffe-credentials
               readOnly: true
           nodeSelector:
             iam.gke.io/gke-metadata-server-enabled: "true"
           volumes:
           - name: fleet-spiffe-credentials
             csi:
               driver: podcertificate.gke.io
               volumeAttributes:
                 signerName: spiffe.gke.io/fleet-svid
                 trustDomain: fleet-project/tenancy-scope
         EOF
         




### List the workload credentials

To list the workload credentials, run the following command. It can take a few minutes to create the credentials.
    
    
    kubectl exec -it example-pod -n KUBERNETES_NAMESPACE -- ls  /var/run/secrets/workload-spiffe-credentials
    

The command output lists the following files:

  * `ca_certificates.pem`: Contains the root CA certificate that signs the workload certificate.
  * `certificates.pem`: Contains the workload's X.509 certificate.
  * `private_key.pem`: Contains the workload's private key.
  * `trust_bundles.json`: Contains a map of trust domains and CA certificates to trust for the given workload. Each entry contains the trust domain string as a key, and the CA certificates corresponding to that trust domain.
  * `credential-bundle.pem`: Contains the private key and certificate concatenated, providing a single file for mTLS credentials. This file is only available in GKE versions after 1.35.2-gke.1291000.



### View the certificate

To view the certificate, do the following:

  1. Export the certificate to a certificate file.
         
         kubectl exec -it example-pod --namespace=KUBERNETES_NAMESPACE -- cat /var/run/secrets/workload-spiffe-credentials/certificates.pem | openssl x509 -noout -text > certfile
         

  2. View the certificate file.
         
         cat certfile
         

In the certificate, in the `X509v3 Subject Alternative Name` attribute, you see the SPIFFE ID, with a format similar to the following depending on your workload identity pool type:

     * **Google-managed pool:** `spiffe://PROJECT_ID.svc.id.goog/ns/KUBERNETES_NAMESPACE/sa/default`
     * **Self-managed pool:** `spiffe://POOL_NAME.global.POOL_HOST_PROJECT_NUMBER.workload.id.goog/ns/KUBERNETES_NAMESPACE/sa/default`

`default` refers to the default Kubernetes ServiceAccount.




### Test workload-to-workload authentication

To test workload-to-workload authentication, see [Test mTLS authentication using Go](https://github.com/grpc/grpc-go/tree/master/examples/features/encryption#readme).

The sample code in the repository creates _client_ and _server_ workloads. You can test mutual authentication between the workloads using the certificates that you generated earlier in this document.

## Enable trust federation between workload identity pools (Optional)

To enable mutual authentication for workloads in different trust domains, you must configure trust federation between the workload identity pools. This step is only required if your workloads need to authenticate with workloads in a different workload identity pool.

To enable trust federation, complete the following steps:

  1. Create the trust configuration file.
  2. Update the workload identity pool with trust configuration.



### Create the trust configuration file

Create the trust configuration file with an `inlineTrustConfig` section that specifies the certificates for each domain.

The trust config file contains a set of trust anchors that managed workload identity uses to validate peer certificates. The trust config file maps the SPIFFE trust domain to CA certificates.

  1. For custom CA, download the certificates for a trust domain that uses a custom CA.
         
         gcloud privateca pools get-ca-certs ROOT_CA_POOL_ID \
             --output-file=CERTIFICATE_PATH \
             --location=REGION
         

Replace the following:

     * `ROOT_CA_POOL_ID`: The ID of the root CA pool.
     * `CERTIFICATE_PATH`: The output path for the PEM-encoded certificate.
     * `REGION`: The region of the root CA pool.
  2. Create a file named `tc.json` that contains your inline trust configuration. If a domain uses the Google-managed default CA, use the `trustDefaultSharedCa` field. If a domain uses a custom CA, use the PEM-encoded certificates that you previously downloaded.

The file looks similar to the following:

In this example, TRUST_DOMAIN_A uses the Google-managed default CA, and TRUSTED_DOMAIN_B uses a custom CA with the downloaded root certificates.
         
         {
           "inlineTrustConfig": {
             "additionalTrustBundles": {
               "TRUST_DOMAIN_A": {
                 "trustDefaultSharedCa": true
               },
               "TRUSTED_DOMAIN_B": {
                 "trustAnchors": [
                   {
                       "pemCertificate": "-----BEGIN CERTIFICATE-----\nCERTIFICATE_MATERIAL1\n-----END CERTIFICATE-----"
                   },
                   {
                       "pemCertificate": "-----BEGIN CERTIFICATE-----\nCERTIFICATE_MATERIAL2\n-----END CERTIFICATE-----"
                   }
                 ]
               }
             }
           }
         }
         

Replace the following:

     * TRUST_DOMAIN_A: The name of the trust domain that uses the Google-managed default CA.
     * TRUST_DOMAIN_B: The name of the trust domain that uses a custom CA.
     * CERTIFICATE_MATERIAL: A set of PEM-formatted CA certificates trusted to issue certificates in the trust domain.



### Update the workload identity pool with trust configuration
    
    
    gcloud iam workload-identity-pools update TRUST_DOMAIN_NAME \
        --location="global" \
        --inline-trust-config-file=TC_JSON_FILE_PATH \
        --project=PROJECT_ID
    

Replace the following:

  * TRUST_DOMAIN_NAME: The name of the trust domain.
  * TC_JSON_FILE_PATH: The path to the JSON-formatted trust config file (`tc.json`) that you created.
  * PROJECT_ID: The project ID.



## What's next

  * [Troubleshoot managed workload identity for GKE](https://docs.cloud.google.com/iam/docs/troubleshoot-managed-workload-identities-gke).
  * Learn more about [creating CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
