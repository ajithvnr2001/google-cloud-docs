---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-proxyless-setup-legacy/
title: Set up service security with proxyless gRPC (legacy) \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:35.156940+00:00
---

# Set up service security with proxyless gRPC (legacy)  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-proxyless-setup-legacy/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up service security with proxyless gRPC (legacy)

This guide shows you how to configure a security service for proxyless gRPC service mesh.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This document applies to Cloud Service Mesh with the load balancing APIs only. This is a legacy document.

## Requirements

Before you configure service security for the gRPC proxyless service mesh, make sure that you meet the following requirements.

  * Your deployment meets the requirements in [Prepare to set up Cloud Service Mesh with proxyless gRPC](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gke#cluster_requirements).
  * You must use xDS v3.
  * You have access to the required xDS version and certificate provider function with one of the following languages: 
    * gRPC Java
    * gRPC C++
    * gRPC Python
    * gRPC Go You can find the required language versions on [github](https://github.com/grpc/grpc/blob/master/doc/grpc_xds_features.md)
  * You have access to the bootstrap generator, version 0.13.0. The bootstrap generator image is located [in the Google Cloud container repository](https://gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0).
  * You meet all of the prerequisites for [gRPC proxyless service mesh load balancing](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-overview#architecture-resources).
  * You have sufficient permissions to create or update the Cloud Service Mesh and Google Cloud service mesh resources to use proxyless service mesh (PSM) security. For complete information about the required permissions, see [Prepare to set up Cloud Service Mesh with proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/prepare-proxyless-grpc).
  * You have the required permissions to use Certificate Authority Service, which are described in Create certificate authorities to issue certificates



## Configure Identity and Access Management

You must have [the required permissions to use Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#predefined). At a minimum, you must have the following roles:

  * `roles/container.clusterAdmin` GKE role
  * `roles/compute.instanceAdmin` Compute Engine role
  * `roles/iam.serviceAccountUser` role



To create the resources required for the setup, you must have the `compute.NetworkAdmin` role. This role contains all the necessary permissions to create, update, delete, list, and use (that is, referencing this in other resources) the required resources. If you are the owner-editor of your project, you automatically have this role.

Note that the `networksecurity.googleapis.com.clientTlsPolicies.use` and `networksecurity.googleapis.com.serverTlsPolicies.use` are not enforced when you reference these resources in the backend service and target HTTPS proxy resources.

If this is enforced in the future and you are using the `compute.NetworkAdmin` role, then you won't notice any issues when this check is enforced.

If you are using custom roles and this check is enforced in the future, you must make sure to include the respective `.use` permission. Otherwise, in the future, you might find that your custom role does not have the necessary permissions to refer to `clientTlsPolicy` or `serverTlsPolicy` from the backend service or target HTTPS proxy, respectively.

## Prepare for setup

Proxyless service mesh (PSM) security adds security to a service mesh that is set up for load balancing per the [proxyless gRPC services documentation](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-overview). In a proxyless service mesh, a gRPC client uses the scheme `xds:` in the URI to access the service, which enables the PSM load balancing and endpoint discovery features.

### Update gRPC clients and servers to the correct version

Build or rebuild your applications using the minimum supported gRPC version for your language.

### Update the bootstrap file

gRPC applications use a single bootstrap file, which must have all of the fields that are required by gRPC client- and server-side code. A bootstrap generator automatically generates the bootstrap file to include flags and values that PSM security needs. For more information, see the Bootstrap file section, which includes a sample bootstrap file.

## Setup overview

This setup process is an extension of the [Cloud Service Mesh setup](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gke) with GKE and proxyless gRPC services. Existing unmodified steps of that setup procedure are referenced wherever they apply.

The main enhancements to the [Cloud Service Mesh setup](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gke) with GKE are as follows:

  1. Setting up CA Service, in which you create private CA pools and the required certificate authorities.
  2. Creating a GKE cluster with GKE Workload Identity Federation for GKE and mesh certificates features and CA Service integration.
  3. Configuring mesh certificate issuance on the cluster.
  4. Creating the client and server service accounts.
  5. Setting up the [example server](https://github.com/grpc/grpc-java/blob/master/examples/example-xds/src/main/java/io/grpc/examples/helloworldxds/XdsHelloWorldServer.java) that uses xDS APIs and xDS server credentials to acquire security configuration from Cloud Service Mesh.
  6. Setting up the [example client](https://github.com/grpc/grpc-java/blob/master/examples/example-xds/src/main/java/io/grpc/examples/helloworldxds/XdsHelloWorldClient.java) that uses xDS credentials.
  7. Updating the Cloud Service Mesh configuration to include security configuration.



You can see code examples for using xDS credentials at the following locations:

  * [Java](https://github.com/grpc/grpc-java/tree/v1.41.x/examples/example-xds).
  * [C++](https://github.com/grpc/grpc/tree/v1.41.x/examples/cpp/helloworld)
  * [Go](https://github.com/grpc/grpc-go/tree/1.41.x/examples/features/xds)
  * [Python](https://github.com/grpc/grpc/tree/1.41.x/examples/python/xds)



## Update the Google Cloud CLI

To update the Google Cloud CLI, run the following command:
    
    
    gcloud components update
    

## Set up environment variables

In this guide, you use Cloud Shell commands, and repeating information in the commands is represented by various environment variables. Set your specific values to the following environment variables in the shell environment before you execute the commands. Each comment line indicates the meaning of the associated environment variable.
    
    
    # Your project ID
    PROJECT_ID=YOUR_PROJECT_ID
    
    # GKE cluster name and zone for this example.
    CLUSTER_NAME="secure-psm-cluster"
    ZONE="us-east1-d"
    
    # GKE cluster URL derived from the above
    GKE_CLUSTER_URL="https://container.googleapis.com/v1/projects/${PROJECT_ID}/locations/${ZONE}/clusters/${CLUSTER_NAME}"
    
    # Workload pool to be used with the GKE cluster
    WORKLOAD_POOL="${PROJECT_ID}.svc.id.goog"
    
    # Kubernetes namespace to run client and server demo.
    K8S_NAMESPACE='default'
    DEMO_BACKEND_SERVICE_NAME='grpc-gke-helloworld-service'
    
    # Compute other values
    # Project number for your project
    PROJNUM=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
    
    # VERSION is the GKE cluster version. Install and use the most recent version
    # from the rapid release channel and substitute its version for
    # CLUSTER_VERSION, for example:
    # VERSION=latest available version
    # Note that the minimum required cluster version is 1.21.4-gke.1801.
    VERSION="CLUSTER_VERSION"
    SA_GKE=service-${PROJNUM}@container-engine-robot.iam.gserviceaccount.com
    

## Enable access to required APIs

This section tells you how to enable access to the necessary APIs.

  1. Run the following command to enable the Cloud Service Mesh and other APIs required for proxyless gRPC service mesh security.
         
         gcloud services enable \
             container.googleapis.com \
             cloudresourcemanager.googleapis.com \
             compute.googleapis.com \
             trafficdirector.googleapis.com \
             networkservices.googleapis.com \
             networksecurity.googleapis.com \
             privateca.googleapis.com \
             gkehub.googleapis.com
         

  2. Run the following command to allow the default service account to access the Cloud Service Mesh security API.
         
         GSA_EMAIL=$(gcloud iam service-accounts list --format='value(email)' \
             --filter='displayName:Compute Engine default service account')
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID} \
           --member serviceAccount:${GSA_EMAIL} \
            --role roles/trafficdirector.client
         




## Create or update a GKE cluster

Cloud Service Mesh service security depends on the CA Service integration with GKE. The GKE cluster must meet the following requirements in addition to the requirements for setup:

  * Use a minimum cluster version of 1.21.4-gke.1801. If you need features that are in a later version, you can obtain that version from the rapid release channel.
  * The GKE cluster must be enabled and configured with mesh certificates, as described in Creating certificate authorities to issue certificates.


  1. Create a new cluster that uses Workload Identity Federation for GKE. If you are updating an existing cluster, skip to the next step. The value you give for `--tags` must match the name passed to the `--target-tags` flag for the `firewall-rules create` command in the section [Configuring Cloud Service Mesh with Cloud Load Balancing components](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods-auto#configuring_with_components).
         
         # Create a GKE cluster with GKE managed mesh certificates.
         gcloud container clusters create CLUSTER_NAME \
           --release-channel=rapid \
           --scopes=cloud-platform \
           --image-type=cos_containerd \
           --machine-type=e2-standard-2 \
           --zone=ZONE \
           --workload-pool=PROJECT_ID.svc.id.goog \
           --enable-mesh-certificates \
           --cluster-version=CLUSTER_VERSION \
           --enable-ip-alias \
           --tags=allow-health-checks \
           --workload-metadata=GKE_METADATA
         

Cluster creation might take several minutes to complete.

  2. If you are using an existing cluster, turn on Workload Identity Federation for GKE and GKE mesh certificates. Make sure that the cluster was created with the `--enable-ip-alias` flag, which cannot be used with the `update` command.
         
         gcloud container clusters update CLUSTER_NAME \
           --enable-mesh-certificates
         

  3. Run the following command to switch to the new cluster as the default cluster for your `kubectl` commands:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
           --zone ZONE
         




## Register clusters with a fleet

Register the cluster that you created or updated in Creating a GKE cluster with a fleet. Registering the cluster makes it easier for you to configure clusters across multiple projects.

Note that these steps can take up to ten minutes each to complete.

  1. Register your cluster with the fleet:
         
         gcloud container fleet memberships register CLUSTER_NAME \
           --gke-cluster=ZONE/CLUSTER_NAME \
           --enable-workload-identity --install-connect-agent \
           --manifest-output-file=MANIFEST-FILE_NAME
         

Replace the variables as follows:

     * CLUSTER_NAME: Your cluster's name.
     * ZONE: Your cluster's zone.
     * MANIFEST-FILE_NAME: The path where these commands generate the manifest for registration.

When the registration process succeeds, you see a message such as the following:
    
    Finished registering the cluster CLUSTER_NAME with the fleet.

  2. Apply the generated manifest file to your cluster:
         
         kubectl apply -f MANIFEST-FILE_NAME
         

When the application process succeeds, you see messages such as the following:
         
         namespace/gke-connect created
         serviceaccount/connect-agent-sa created
         podsecuritypolicy.policy/gkeconnect-psp created
         role.rbac.authorization.k8s.io/gkeconnect-psp:role created
         rolebinding.rbac.authorization.k8s.io/gkeconnect-psp:rolebinding created
         role.rbac.authorization.k8s.io/agent-updater created
         rolebinding.rbac.authorization.k8s.io/agent-updater created
         role.rbac.authorization.k8s.io/gke-connect-agent-20210416-01-00 created
         clusterrole.rbac.authorization.k8s.io/gke-connect-impersonation-20210416-01-00 created
         clusterrolebinding.rbac.authorization.k8s.io/gke-connect-impersonation-20210416-01-00 created
         clusterrolebinding.rbac.authorization.k8s.io/gke-connect-feature-authorizer-20210416-01-00 created
         rolebinding.rbac.authorization.k8s.io/gke-connect-agent-20210416-01-00 created
         role.rbac.authorization.k8s.io/gke-connect-namespace-getter created
         rolebinding.rbac.authorization.k8s.io/gke-connect-namespace-getter created
         secret/http-proxy created
         deployment.apps/gke-connect-agent-20210416-01-00 created
         service/gke-connect-monitoring created
         secret/creds-gcp create
         

  3. Get the membership resource from the cluster:
         
         kubectl get memberships membership -o yaml
         

The output should include the Workoad Identity pool assigned by the fleet, where PROJECT_ID is your project ID:
         
         workload_identity_pool: PROJECT_ID.svc.id.goog
         

This means that the cluster registered successfully.




## Create certificate authorities to issue certificates

To issue certificates to your Pods, create a CA Service pool and the following certificate authorities (CAs):

  * Root CA. This is the root of trust for all issued mesh certificates. You can use an existing root CA if you have one. Create the root CA in the `enterprise` tier, which is meant for long-lived, low-volume certificate issuance.
  * Subordinate CA. This CA issues certificates for workloads. Create the subordinate CA in the region where your cluster is deployed. Create the subordinate CA in the `devops` tier, which is meant for short-lived, high-volume certificate issuance.



Creating a subordinate CA is optional, but we strongly recommend creating one rather than using your root CA to issue GKE mesh certificates. If you decide to use the root CA to issue mesh certificates, ensure that the default [config-based issuance mode](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rpc/google.cloud.security.privateca.v1#issuancemodes) remains permitted.

The subordinate CA can be in a different region from your cluster, but we strongly recommend creating it in the same region as your cluster to optimize performance. You can, however, create the root and subordinate CAs in different regions without any impact to performance or availability.

These regions are supported for CA Service:

Region name | Region description  
---|---  
`asia-east1` | Taiwan  
`asia-east2` | Hong Kong  
`asia-northeast1` | Tokyo  
`asia-northeast2` | Osaka  
`asia-northeast3` | Seoul  
`asia-south1` | Mumbai  
`asia-south2` | Delhi  
`asia-southeast1` | Singapore  
`asia-southeast2` | Jakarta  
`australia-southeast1` | Sydney  
`australia-southeast2` | Melbourne  
`europe-central2` | Warsaw  
`europe-north1` | Finland  
`europe-southwest1` | Madrid  
`europe-west1` | Belgium  
`europe-west2` | London  
`europe-west3` | Frankfurt  
`europe-west4` | Netherlands  
`europe-west6` | Zürich  
`europe-west8` | Milan  
`europe-west9` | Paris  
`europe-west10` | Berlin  
`europe-west12` | Turin  
`me-central1` | Doha  
`me-central2` | Dammam  
`me-west1` | Tel Aviv  
`northamerica-northeast1` | Montréal  
`northamerica-northeast2` | Toronto  
`southamerica-east1` | São Paulo  
`southamerica-west1` | Santiago  
`us-central1` | Iowa  
`us-east1` | South Carolina  
`us-east4` | Northern Virginia  
`us-east5` | Columbus  
`us-south1` | Dallas  
`us-west1` | Oregon  
`us-west2` | Los Angeles  
`us-west3` | Salt Lake City  
`us-west4` | Las Vegas  
  
The list of supported locations can also be checked by running the following command:
    
    
    gcloud privateca locations list
    

  1. Grant the IAM `roles/privateca.caManager` to individuals who create a CA pool and a CA. Note that for MEMBER, the correct format is `user:userid@example.com`. If that person is the current user, you can obtain the current user ID with the shell command `$(gcloud auth list --filter=status:ACTIVE --format="value(account)")`.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=MEMBER \
           --role=roles/privateca.caManager
         

  2. Grant the role `role/privateca.admin` for CA Service to individuals who need to modify IAM policies, where `MEMBER` is an individual who needs this access, specifically, any individuals who perform the steps that follow that grant the `privateca.auditor` and `privateca.certificateManager` roles:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=MEMBER \
           --role=roles/privateca.admin
         

  3. Create the root CA Service pool.
         
         gcloud privateca pools create ROOT_CA_POOL_NAME \
           --location ROOT_CA_POOL_LOCATION \
           --tier enterprise
         

  4. Create a root CA.
         
         gcloud privateca roots create ROOT_CA_NAME --pool ROOT_CA_POOL_NAME \
           --subject "CN=ROOT_CA_NAME, O=ROOT_CA_ORGANIZATION" \
           --key-algorithm="ec-p256-sha256" \
           --max-chain-length=1 \
           --location ROOT_CA_POOL_LOCATION
         

For this demonstration setup, use the following values for the variables:

     * ROOT_CA_POOL_NAME=td_sec_pool
     * ROOT_CA_NAME=pkcs2-ca
     * ROOT_CA_POOL_LOCATION=us-east1
     * ROOT_CA_ORGANIZATION="TestCorpLLC"
  5. Create the subordinate pool and subordinate CA. Ensure that the default [config-based issuance mode](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rpc/google.cloud.security.privateca.v1#issuancemodes) remains permitted.
         
         gcloud privateca pools create SUBORDINATE_CA_POOL_NAME \
           --location SUBORDINATE_CA_POOL_LOCATION \
           --tier devops
         
         
         gcloud privateca subordinates create SUBORDINATE_CA_NAME \
           --pool SUBORDINATE_CA_POOL_NAME \
           --location SUBORDINATE_CA_POOL_LOCATION \
           --issuer-pool ROOT_CA_POOL_NAME \
           --issuer-location ROOT_CA_POOL_LOCATION \
           --subject "CN=SUBORDINATE_CA_NAME, O=SUBORDINATE_CA_ORGANIZATION" \
           --key-algorithm "ec-p256-sha256" \
           --use-preset-profile subordinate_mtls_pathlen_0
         

For this demonstration setup, use the following values for the variables:

     * SUBORDINATE_CA_POOL_NAME="td-ca-pool"
     * SUBORDINATE_CA_POOL_LOCATION=us-east1
     * SUBORDINATE_CA_NAME="td-ca"
     * SUBORDINATE_CA_ORGANIZATION="TestCorpLLC"
     * ROOT_CA_POOL_NAME=td_sec_pool
     * ROOT_CA_POOL_LOCATION=us-east1
  6. Grant the IAM `privateca.auditor` role for the root CA pool to allow access from the GKE service account:
         
         gcloud privateca pools add-iam-policy-binding ROOT_CA_POOL_NAME \
          --location ROOT_CA_POOL_LOCATION \
          --role roles/privateca.auditor \
          --member="serviceAccount:service-PROJNUM@container-engine-robot.iam.gserviceaccount.com"
         

  7. Grant the IAM `privateca.certificateManager` role for the subordinate CA pool to allow access from the GKE service account:
         
         gcloud privateca pools add-iam-policy-binding SUBORDINATE_CA_POOL_NAME \
           --location SUBORDINATE_CA_POOL_LOCATION \
           --role roles/privateca.certificateManager \
           --member="serviceAccount:service-PROJNUM@container-engine-robot.iam.gserviceaccount.com"
         

  8. Save the following `WorkloadCertificateConfig` YAML configuration to tell your cluster how to issue mesh certificates:
         
         apiVersion: security.cloud.google.com/v1
         kind: WorkloadCertificateConfig
         metadata:
           name: default
         spec:
           # Required. The CA service that issues your certificates.
           certificateAuthorityConfig:
             certificateAuthorityServiceConfig:
               endpointURI: ISSUING_CA_POOL_URI
         
           # Required. The key algorithm to use. Choice of RSA or ECDSA.
           #
           # To maximize compatibility with various TLS stacks, your workloads
           # should use keys of the same family as your root and subordinate CAs.
           #
           # To use RSA, specify configuration such as:
           #   keyAlgorithm:
           #     rsa:
           #       modulusSize: 4096
           #
           # Currently, the only supported ECDSA curves are "P256" and "P384", and the only
           # supported RSA modulus sizes are 2048, 3072 and 4096.
           keyAlgorithm:
             rsa:
               modulusSize: 4096
         
           # Optional. Validity duration of issued certificates, in seconds.
           #
           # Defaults to 86400 (1 day) if not specified.
           validityDurationSeconds: 86400
         
           # Optional. Try to start rotating the certificate once this
           # percentage of validityDurationSeconds is remaining.
           #
           # Defaults to 50 if not specified.
           rotationWindowPercentage: 50
         
         

Replace the following:

     * The project ID of the project in which your cluster runs: 
           
           PROJECT_ID

     * The fully qualified URI of the CA that issues your mesh certificates (ISSUING_CA_POOL_URI). This can be either your subordinate CA (recommended) or your root CA. The format is: 
           
           //privateca.googleapis.com/projects/PROJECT_ID/locations/SUBORDINATE_CA_POOL_LOCATION/caPools/SUBORDINATE_CA_POOL_NAME

  9. Save the following `TrustConfig` YAML configuration to tell your cluster how to trust the issued certificates:
         
         apiVersion: security.cloud.google.com/v1
         kind: TrustConfig
         metadata:
           name: default
         spec:
           # You must include a trustStores entry for the trust domain that
           # your cluster is enrolled in.
           trustStores:
           - trustDomain: PROJECT_ID.svc.id.goog
             # Trust identities in this trustDomain if they appear in a certificate
             # that chains up to this root CA.
             trustAnchors:
             - certificateAuthorityServiceURI: ROOT_CA_POOL_URI
         

Replace the following:

     * The project ID of the project in which your cluster runs: 
           
           PROJECT_ID

     * The fully qualified URI of the root CA pool (ROOT_CA_POOL_URI). The format is: 
           
           //privateca.googleapis.com/projects/PROJECT_ID/locations/ROOT_CA_POOL_LOCATION/caPools/ROOT_CA_POOL_NAME

  10. Apply the configurations to your cluster:
         
         kubectl apply -f WorkloadCertificateConfig.yaml
         kubectl apply -f TrustConfig.yaml
         




## Create a proxyless gRPC service with NEGs

For PSM security, you need a proxyless gRPC server capable of using xDS to acquire security configuration from Cloud Service Mesh. This step is similar to [Configuring GKE services with NEGs](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gke#configuring_services_with_negs) in the PSM load balancing setup guide, but you use the xDS-enabled `helloworld` server in the [xDS example in the `grpc-java` repository](https://github.com/grpc/grpc-java/tree/v1.42.1/examples/example-xds) instead of the `java-example-hostname` image.

You build and run this server in a container built from an `openjdk:8-jdk` image. You also use the [named NEG feature](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-%0Aneg#naming_negs), which lets you specify a name for the NEG. This simplifies later steps because your deployment knows the name of the NEG without having to look it up.

The following is a complete example of the gRPC server Kubernetes spec. Note the following:

  * The spec creates a Kubernetes service account `example-grpc-server` that is used by the gRPC server Pod.
  * The spec uses the `name` field in the `cloud.google.com/neg` annotation of the service to specify the NEG name `example-grpc-server`.
  * The variable `${PROJNUM}` represents the project number of your project.
  * The spec uses the `initContainers` section to run a bootstrap generator to populate the bootstrap file that the proxyless gRPC library needs. This bootstrap file resides at `/tmp/grpc-xds/td-grpc-bootstrap.json` in the gRPC server container called `example-grpc-server`.



Add the following annotation to your Pod spec:
    
    
     annotations:
       security.cloud.google.com/use-workload-certificates: ""
    

You can see the correct placement in the full spec that follows.

On creation, each Pod gets a volume at `/var/run/secrets/workload-spiffe-credentials`. This volume contains the following:

  * `private_key.pem` is an automatically generated private key.
  * `certificates.pem` is a bundle of PEM-formatted certificates that can be presented to another Pod as the client certificate chain, or used as a server certificate chain.
  * `ca_certificates.pem` is a bundle of PEM-formatted certificates to use as trust anchors when validating the client certificate chain presented by another Pod, or the server certificate chain received when connecting to another Pod.



Note that `ca_certificates.pem` contains certificates for the local trust domain for the workloads, which is the cluster's workload pool.

The leaf certificate in `certificates.pem` contains the following plain-text SPIFFE identity assertion:
    
    
    spiffe://WORKLOAD_POOL/ns/NAMESPACE/sa/KUBERNETES_SERVICE_ACCOUNT
    

In this assertion:

  * WORKLOAD_POOL is the name of the cluster workload pool.
  * NAMESPACE is the namespace of your Kubernetes service account.
  * KUBERNETES_SERVICE_ACCOUNT is the name of your Kubernetes service account.



The following instructions for your language create the spec to use in this example.

###  Java 

  1. Run the following command to ensure that the project number is correctly set:
         
         if [ -z "$PROJNUM" ] ; then export PROJNUM=$(gcloud projects describe $(gcloud info --format='value(config.project)') --format="value(projectNumber)") ; fi ; echo $PROJNUM
         

  2. Create the spec:
         
         cat << EOF > example-grpc-server.yaml
         apiVersion: v1
         kind: ServiceAccount
         metadata:
          name: example-grpc-server
          namespace: default
          annotations:
            iam.gke.io/gcp-service-account: ${PROJNUM}-compute@developer.gserviceaccount.com
         ---
         apiVersion: v1
         kind: Service
         metadata:
          name: example-grpc-server
          namespace: default
          labels:
            k8s-app: example-grpc-server
          annotations:
            cloud.google.com/neg: '{"exposed_ports":{"8080":{"name": "example-grpc-server"}}}'
         spec:
          ports:
          - name: helloworld
            port: 8080
            protocol: TCP
            targetPort: 50051
          selector:
            k8s-app: example-grpc-server
          type: ClusterIP
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
          name: example-grpc-server
          namespace: default
          labels:
            k8s-app: example-grpc-server
         spec:
          replicas: 1
          selector:
            matchLabels:
              k8s-app: example-grpc-server
          strategy: {}
          template:
            metadata:
              annotations:
                 security.cloud.google.com/use-workload-certificates: ""
              labels:
                k8s-app: example-grpc-server
            spec:
              containers:
              - image: openjdk:8-jdk
                imagePullPolicy: IfNotPresent
                name: example-grpc-server
                command:
                - /bin/sleep
                - inf
                env:
                - name: GRPC_XDS_BOOTSTRAP
                  value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
                ports:
                - protocol: TCP
                  containerPort: 50051
                resources:
                  limits:
                    cpu: 800m
                    memory: 512Mi
                  requests:
                    cpu: 100m
                    memory: 512Mi
                volumeMounts:
                - name: grpc-td-conf
                  mountPath: /tmp/grpc-xds/
              initContainers:
              - name: grpc-td-init
                image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
                imagePullPolicy: Always
                args:
                - --output
                - "/tmp/bootstrap/td-grpc-bootstrap.json"
                - --node-metadata=app=helloworld
                resources:
                  limits:
                    cpu: 100m
                    memory: 100Mi
                  requests:
                    cpu: 10m
                    memory: 100Mi
                volumeMounts:
                - name: grpc-td-conf
                  mountPath: /tmp/bootstrap/
              serviceAccountName: example-grpc-server
              volumes:
              - name: grpc-td-conf
                emptyDir:
                  medium: Memory
         EOF
         




###  C++ 

  1. Run the following command to ensure that the project number is correctly set:
         
         if [ -z "$PROJNUM" ] ; then export PROJNUM=$(gcloud projects describe $(gcloud info --format='value(config.project)') --format="value(projectNumber)") ; fi ; echo $PROJNUM
         

  2. Create the spec:
         
         cat << EOF > example-grpc-server.yaml
         apiVersion: v1
         kind: ServiceAccount
         metadata:
          name: example-grpc-server
          namespace: default
          annotations:
            iam.gke.io/gcp-service-account: ${PROJNUM}-compute@developer.gserviceaccount.com
         ---
         apiVersion: v1
         kind: Service
         metadata:
          name: example-grpc-server
          namespace: default
          labels:
            k8s-app: example-grpc-server
          annotations:
            cloud.google.com/neg: '{"exposed_ports":{"8080":{"name": "example-grpc-server"}}}'
         spec:
          ports:
          - name: helloworld
            port: 8080
            protocol: TCP
            targetPort: 50051
          selector:
            k8s-app: example-grpc-server
          type: ClusterIP
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
          name: example-grpc-server
          namespace: default
          labels:
            k8s-app: example-grpc-server
         spec:
          replicas: 1
          selector:
            matchLabels:
              k8s-app: example-grpc-server
          strategy: {}
          template:
            metadata:
              annotations:
                 security.cloud.google.com/use-workload-certificates: ""
              labels:
                k8s-app: example-grpc-server
            spec:
              containers:
              - image: phusion/baseimage:18.04-1.0.0
                imagePullPolicy: IfNotPresent
                name: example-grpc-server
                command:
                - /bin/sleep
                - inf
                env:
                - name: GRPC_XDS_BOOTSTRAP
                  value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
                ports:
                - protocol: TCP
                  containerPort: 50051
                resources:
                  limits:
                    cpu: 8
                    memory: 8Gi
                  requests:
                    cpu: 300m
                    memory: 512Mi
                volumeMounts:
                - name: grpc-td-conf
                  mountPath: /tmp/grpc-xds/
              initContainers:
              - name: grpc-td-init
                image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
                imagePullPolicy: Always
                args:
                - --output
                - "/tmp/bootstrap/td-grpc-bootstrap.json"
                - --node-metadata=app=helloworld
                resources:
                  limits:
                    cpu: 100m
                    memory: 100Mi
                  requests:
                    cpu: 10m
                    memory: 100Mi
                volumeMounts:
                - name: grpc-td-conf
                  mountPath: /tmp/bootstrap/
              serviceAccountName: example-grpc-server
              volumes:
              - name: grpc-td-conf
                emptyDir:
                  medium: Memory
         EOF
         




###  Python 

  1. Run the following command to ensure that the project number is correctly set:
         
         if [ -z "$PROJNUM" ] ; then export PROJNUM=$(gcloud projects describe $(gcloud info --format='value(config.project)') --format="value(projectNumber)") ; fi ; echo $PROJNUM
         

  2. Create the spec:
         
         cat << EOF > example-grpc-server.yaml
         apiVersion: v1
         kind: ServiceAccount
         metadata:
          name: example-grpc-server
          namespace: default
          annotations:
            iam.gke.io/gcp-service-account: ${PROJNUM}-compute@developer.gserviceaccount.com
         ---
         apiVersion: v1
         kind: Service
         metadata:
          name: example-grpc-server
          namespace: default
          labels:
            k8s-app: example-grpc-server
          annotations:
            cloud.google.com/neg: '{"exposed_ports":{"8080":{"name": "example-grpc-server"}}}'
         spec:
          ports:
          - name: helloworld
            port: 8080
            protocol: TCP
            targetPort: 50051
          selector:
            k8s-app: example-grpc-server
          type: ClusterIP
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
          name: example-grpc-server
          namespace: default
          labels:
            k8s-app: example-grpc-server
         spec:
          replicas: 1
          selector:
            matchLabels:
              k8s-app: example-grpc-server
          strategy: {}
          template:
            metadata:
              annotations:
                 security.cloud.google.com/use-workload-certificates: ""
              labels:
                k8s-app: example-grpc-server
            spec:
              containers:
              - image: phusion/baseimage:18.04-1.0.0
                imagePullPolicy: IfNotPresent
                name: example-grpc-server
                command:
                - /bin/sleep
                - inf
                env:
                - name: GRPC_XDS_BOOTSTRAP
                  value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
                ports:
                - protocol: TCP
                  containerPort: 50051
                resources:
                  limits:
                    cpu: 8
                    memory: 8Gi
                  requests:
                    cpu: 300m
                    memory: 512Mi
                volumeMounts:
                - name: grpc-td-conf
                  mountPath: /tmp/grpc-xds/
              initContainers:
              - name: grpc-td-init
                image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
                imagePullPolicy: Always
                args:
                - --output
                - "/tmp/bootstrap/td-grpc-bootstrap.json"
                - --node-metadata=app=helloworld
                resources:
                  limits:
                    cpu: 100m
                    memory: 100Mi
                  requests:
                    cpu: 10m
                    memory: 100Mi
                volumeMounts:
                - name: grpc-td-conf
                  mountPath: /tmp/bootstrap/
              serviceAccountName: example-grpc-server
              volumes:
              - name: grpc-td-conf
                emptyDir:
                  medium: Memory
         EOF
         




###  Go 

  1. Run the following command to ensure that the project number is correctly set:
         
         if [ -z "$PROJNUM" ] ; then export PROJNUM=$(gcloud projects describe $(gcloud info --format='value(config.project)') --format="value(projectNumber)") ; fi ; echo $PROJNUM
         

  2. Create the spec:
         
         cat << EOF > example-grpc-server.yaml
         apiVersion: v1
         kind: ServiceAccount
         metadata:
          name: example-grpc-server
          namespace: default
          annotations:
            iam.gke.io/gcp-service-account: ${PROJNUM}-compute@developer.gserviceaccount.com
         ---
         apiVersion: v1
         kind: Service
         metadata:
          name: example-grpc-server
          namespace: default
          labels:
            k8s-app: example-grpc-server
          annotations:
            cloud.google.com/neg: '{"exposed_ports":{"8080":{"name": "example-grpc-server"}}}'
         spec:
          ports:
          - name: helloworld
            port: 8080
            protocol: TCP
            targetPort: 50051
          selector:
            k8s-app: example-grpc-server
          type: ClusterIP
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
          name: example-grpc-server
          namespace: default
          labels:
            k8s-app: example-grpc-server
         spec:
          replicas: 1
          selector:
            matchLabels:
              k8s-app: example-grpc-server
          strategy: {}
          template:
            metadata:
              annotations:
                 security.cloud.google.com/use-workload-certificates: ""
              labels:
                k8s-app: example-grpc-server
            spec:
              containers:
              - image: golang:1.16-alpine
                imagePullPolicy: IfNotPresent
                name: example-grpc-server
                command:
                - /bin/sleep
                - inf
                env:
                - name: GRPC_XDS_BOOTSTRAP
                  value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
                ports:
                - protocol: TCP
                  containerPort: 50051
                resources:
                  limits:
                    cpu: 8
                    memory: 8Gi
                  requests:
                    cpu: 300m
                    memory: 512Mi
                volumeMounts:
                - name: grpc-td-conf
                  mountPath: /tmp/grpc-xds/
              initContainers:
              - name: grpc-td-init
                image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
                imagePullPolicy: Always
                args:
                - --output
                - "/tmp/bootstrap/td-grpc-bootstrap.json"
                - --node-metadata=app=helloworld
                resources:
                  limits:
                    cpu: 100m
                    memory: 100Mi
                  requests:
                    cpu: 10m
                    memory: 100Mi
                volumeMounts:
                - name: grpc-td-conf
                  mountPath: /tmp/bootstrap/
              serviceAccountName: example-grpc-server
              volumes:
              - name: grpc-td-conf
                emptyDir:
                  medium: Memory
         EOF
         

Complete the process as follows.




  1. Apply the spec:
         
         kubectl apply -f example-grpc-server.yaml
         

  2. Grant the required roles to the service account:
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:${PROJECT_ID}.svc.id.goog[default/example-grpc-server]" \
           ${PROJNUM}-compute@developer.gserviceaccount.com
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID} \
           --member "serviceAccount:${PROJECT_ID}.svc.id.goog[default/example-grpc-server]" \
           --role roles/trafficdirector.client
         

  3. Run these commands to verify that the service and Pod are created correctly:
         
         kubectl get deploy/example-grpc-server
         kubectl get svc/example-grpc-server
         

  4. Verify that the NEG name is correct:
         
         gcloud compute network-endpoint-groups list \
             --filter "name=example-grpc-server" --format "value(name)"
         

The previous command is expected to return the NEG name `example-grpc-server`.




## Configure Cloud Service Mesh with Google Cloud load balancing components

The steps in this section are similar to those in [Configuring Cloud Service Mesh with load balancing components](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gke#configure-lb-components), but there are some changes, as described in the following sections.

### Create the health check, firewall rule, and backend service

When the gRPC server is configured to use mTLS, gRPC health checks don't work because the health checking client cannot present a valid client certificate to the servers. You can address this in one of two ways.

In the first approach, you have the server create an additional serving port that is designated as the health checking port. This is attached to a special [health check service](https://github.com/grpc/grpc/blob/master/doc/health-checking.md), as plain text or TLS to that port.

The xDS [`helloworld` example server](https://github.com/grpc/grpc-java/blob/master/examples/example-xds/src/main/java/io/grpc/examples/helloworldxds/XdsHelloWorldServer.java#L65) uses `PORT_NUMBER` \+ 1 as the plain text health checking port. The example uses 50052 as the health checking port because 50051 is the gRPC application server port.

In the second approach, you configure health checking to check only TCP connectivity to the application serving port. This checks only connectivity, and it also generates unnecessary traffic to the server when there are unsuccessful TLS handshakes. For this reason, we recommend that you use the first approach.

  1. Create the health check. Note that health checking does not start until you create and start the server.

     * If you are creating a designated serving port for health checking, which is the approach we recommend, use this command:
           
           gcloud compute health-checks create grpc grpc-gke-helloworld-hc \
            --enable-logging --port 50052
           

     * If you are creating a TCP health check, which we don't recommend, use this command:
           
           gcloud compute health-checks create tcp grpc-gke-helloworld-hc \
           --use-serving-port
           

  2. Create the firewall. Ensure that the value of `--target-tags` matches the value you provided for `--tags` in the section Create or update a GKE cluster.
         
         gcloud compute firewall-rules create grpc-gke-allow-health-checks \
           --network default --action allow --direction INGRESS \
           --source-ranges 35.191.0.0/16,130.211.0.0/22 \
           --target-tags allow-health-checks \
           --rules tcp:50051-50052
         

  3. Create the backend service:
         
         gcloud compute backend-services create grpc-gke-helloworld-service \
            --global \
            --load-balancing-scheme=INTERNAL_SELF_MANAGED \
            --protocol=GRPC \
            --health-checks grpc-gke-helloworld-hc
         

  4. Attach the NEG to the backend service:
         
         gcloud compute backend-services add-backend grpc-gke-helloworld-service \
            --global \
            --network-endpoint-group example-grpc-server \
            --network-endpoint-group-zone ${ZONE} \
            --balancing-mode RATE \
            --max-rate-per-endpoint 5
         




### Create the routing rule map

This is similar to how you [create a routing rule map](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gke#creating_the_routing_rule_map) in [Cloud Service Mesh setup with Google Kubernetes Engine and proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gke).

  1. Create the URL map:
         
         gcloud compute url-maps create grpc-gke-url-map \
            --default-service grpc-gke-helloworld-service
         

  2. Add the path matcher to the URL map:
         
         gcloud compute url-maps add-path-matcher grpc-gke-url-map \
            --default-service grpc-gke-helloworld-service \
            --path-matcher-name grpc-gke-path-matcher \
            --new-hosts helloworld-gke:8000
         

  3. Create the target gRPC proxy:
         
         gcloud compute target-grpc-proxies create grpc-gke-proxy \
            --url-map grpc-gke-url-map --validate-for-proxyless
         

  4. Create the forwarding rule:
         
         gcloud compute forwarding-rules create grpc-gke-forwarding-rule \
           --global \
           --load-balancing-scheme=INTERNAL_SELF_MANAGED \
           --address=0.0.0.0 \
           --target-grpc-proxy=grpc-gke-proxy \
           --ports 8000 \
           --network default
         




## Configure Cloud Service Mesh with proxyless gRPC Security

This example demonstrates how to configure mTLS on the client and server sides.

### Format for policy references

Note the following required format for referring to server TLS and client TLS policies:
    
    
    projects/PROJECT_ID/locations/global/[serverTlsPolicies|clientTlsPolicies]/[server-tls-policy|client-mtls-policy]
    

For example:
    
    
    projects/PROJECT_ID/locations/global/serverTlsPolicies/server-tls-policy
    
    
    
    projects/PROJECT_ID/locations/global/clientTlsPolicies/client-mtls-policy
    

### Configure mTLS on the server side

First, you create a server TLS policy. The policy asks the gRPC server side to use the `certificateProvicerInstance` plugin config identified by the name `google_cloud_private_spiffe` for the identity certificate, which is part of the `serverCertificate`. The `mtlsPolicy` section indicates mTLS security and uses the same `google_cloud_private_spiffe` as the plugin config for `clientValidationCa`, which is the root (validation) certificate specification.

Next, you create an endpoint policy. This specifies that a backend, for example a gRPC server, using port `50051` with any or no metadata labels, receives the attached server TLS policy named `server-mtls-policy`. You specify metadata labels using `MATCH_ALL`. You create the endpoint policy with a temporary file `ep-mtls-psms.yaml` that contains the values for the endpoint policy resource using the policy that you already defined.

  1. Create a temporary file `server-mtls-policy.yaml` in the current directory with the values of the server TLS policy resource:
         
         name: "projects/${PROJECT_ID}/locations/global/serverTlsPolicies/server-mtls-policy"
         serverCertificate:
           certificateProviderInstance:
             pluginInstance: google_cloud_private_spiffe
         mtlsPolicy:
           clientValidationCa:
           - certificateProviderInstance:
               pluginInstance: google_cloud_private_spiffe
         

  2. Create a server TLS policy resource called `server-mtls-policy` by importing the temporary file `server-mtls-policy.yaml`:
         
         gcloud network-security server-tls-policies import server-mtls-policy \
           --source=server-mtls-policy.yaml --location=global
         

  3. Create the endpoint policy by creating the temporary file `ep-mtls-psms.yaml`:
         
         name: "ep-mtls-psms"
         type: "GRPC_SERVER"
         serverTlsPolicy: "projects/${PROJECT_ID}/locations/global/serverTlsPolicies/server-mtls-policy"
         trafficPortSelector:
           ports:
           - "50051"
         endpointMatcher:
           metadataLabelMatcher:
             metadataLabelMatchCriteria: "MATCH_ALL"
             metadataLabels:
             - labelName: app
               labelValue: helloworld
         

  4. Create the endpoint policy resource by importing the file `ep-mtls-psms.yaml`:
         
         gcloud beta network-services endpoint-policies import ep-mtls-psms \
           --source=ep-mtls-psms.yaml --location=global
         




### Configure mTLS on the client side

The client-side security policy is attached to the backend service. When a client accesses a backend (the gRPC server) through the backend service, the attached client-side security policy is sent to the client.

  1. Create the client TLS policy resource contents in a temporary file called `client-mtls-policy.yaml` in the current directory:
         
         name: "client-mtls-policy"
         clientCertificate:
           certificateProviderInstance:
             pluginInstance: google_cloud_private_spiffe
         serverValidationCa:
         - certificateProviderInstance:
             pluginInstance: google_cloud_private_spiffe
         

  2. Create the client TLS policy resource called `client-mtls-policy` by importing the temporary file `client-mtls-policy.yaml`:
         
         gcloud network-security client-tls-policies import client-mtls-policy \
           --source=client-mtls-policy.yaml --location=global
         

  3. Create a snippet in a temporary file to reference this policy and add details for `subjectAltNames` in the `SecuritySettings` message as in the following example. Replace `${PROJECT_ID}` with your project ID value, which is the value of the `${PROJECT_ID}` environment variable described previously. Note that `example-grpc-server` in `subjectAltNames` is the Kubernetes service account name that is used for the gRPC server Pod in the deployment spec.
         
         if [ -z "$PROJECT_ID" ] ; then echo Please make sure PROJECT_ID is set. ; fi
         cat << EOF > client-security-settings.yaml
         securitySettings:
           clientTlsPolicy: projects/${PROJECT_ID}/locations/global/clientTlsPolicies/client-mtls-policy
           subjectAltNames:
             - "spiffe://${PROJECT_ID}.svc.id.goog/ns/default/sa/example-grpc-server"
         EOF
         

  4. Add the `securitySettings` message to the backend service you already created. These steps export the current backend service contents, add the client `securitySetting` message and re-importing the new content to update the backend service.
         
         gcloud compute backend-services export grpc-gke-helloworld-service --global \
           --destination=/tmp/grpc-gke-helloworld-service.yaml
         
         cat /tmp/grpc-gke-helloworld-service.yaml client-security-settings.yaml \
           >/tmp/grpc-gke-helloworld-service1.yaml
         
         gcloud compute backend-services import grpc-gke-helloworld-service --global \
           --source=/tmp/grpc-gke-helloworld-service1.yaml -q
         




## Verify the configuration

Cloud Service Mesh configuration is now complete, including server- and client-side security. Next, you prepare and run the server and client workloads. This completes the example.

### Create a proxyless gRPC client

This step is similar to the previous section Creating a proxyless gRPC service. You use the xDS-enabled `helloworld` client from the xDS example directory in the `grpc-java` repository. You build and run the client in a container built from an `openjdk:8-jdk` image. The gRPC client Kubernetes spec does the following.

  * It creates a Kubernetes service account `example-grpc-client` that is used by the gRPC client Pod.
  * `${PROJNUM}` represents the project number of your project and needs to be replaced with the actual number.



Add the following annotation to your Pod spec:
    
    
      annotations:
        security.cloud.google.com/use-workload-certificates: ""
    

On creation, each Pod gets a volume at `/var/run/secrets/workload-spiffe-credentials`. This volume contains the following:

  * `private_key.pem` is an automatically generated private key.
  * `certificates.pem` is a bundle of PEM-formatted certificates that can be presented to another Pod as the client certificate chain, or used as a server certificate chain.
  * `ca_certificates.pem` is a bundle of PEM-formatted certificates to use as trust anchors when validating the client certificate chain presented by another Pod, or the server certificate chain received when connecting to another Pod.



Note that `ca_certificates.pem` contains the root certificates for the local trust domain for the workloads, which is the cluster's workload pool.

The leaf certificate in `certificates.pem` contains the following plain-text SPIFFE identity assertion:
    
    
    spiffe://WORKLOAD_POOL/ns/NAMESPACE/sa/KUBERNETES_SERVICE_ACCOUNT
    

In this assertion:

  * WORKLOAD_POOL is the name of the cluster workload pool.
  * NAMESPACE is the name of your Kubernetes service account.
  * KUBERNETES_SERVICE_ACCOUNT is the namespace of your Kubernetes service account.



The following instructions for your language create the spec to use in this example.

###  Java 

  1. Run the following command to ensure that the project number is correctly set:
         
         if [ -z "$PROJNUM" ] ; then export PROJNUM=$(gcloud projects describe $(gcloud info --format='value(config.project)') --format="value(projectNumber)") ; fi ; echo $PROJNUM
         

  2. Create the following spec:
         
         cat << EOF > example-grpc-client.yaml
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: example-grpc-client
           namespace: default
           annotations:
             iam.gke.io/gcp-service-account: ${PROJNUM}-compute@developer.gserviceaccount.com
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: example-grpc-client
           namespace: default
           labels:
             k8s-app: example-grpc-client
         spec:
           replicas: 1
           selector:
             matchLabels:
               k8s-app: example-grpc-client
           strategy: {}
           template:
             metadata:
               annotations:
                 security.cloud.google.com/use-workload-certificates: ""
               labels:
                 k8s-app: example-grpc-client
             spec:
               containers:
               - image: openjdk:8-jdk
                 imagePullPolicy: IfNotPresent
                 name: example-grpc-client
                 command:
                 - /bin/sleep
                 - inf
                 env:
                 - name: GRPC_XDS_BOOTSTRAP
                   value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
                 resources:
                   limits:
                     cpu: 800m
                     memory: 512Mi
                   requests:
                     cpu: 100m
                     memory: 512Mi
                 volumeMounts:
                 - name: grpc-td-conf
                   mountPath: /tmp/grpc-xds/
               initContainers:
               - name: grpc-td-init
                 image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
                 imagePullPolicy: Always
                 args:
                 - --output
                 - "/tmp/bootstrap/td-grpc-bootstrap.json"
                 resources:
                   limits:
                     cpu: 100m
                     memory: 100Mi
                   requests:
                     cpu: 10m
                     memory: 100Mi
                 volumeMounts:
                 - name: grpc-td-conf
                   mountPath: /tmp/bootstrap/
               serviceAccountName: example-grpc-client
               volumes:
               - name: grpc-td-conf
                 emptyDir:
                   medium: Memory
         EOF
         




###  C++ 

  1. Run the following command to ensure that the project number is correctly set:
         
         if [ -z "$PROJNUM" ] ; then export PROJNUM=$(gcloud projects describe $(gcloud info --format='value(config.project)') --format="value(projectNumber)") ; fi ; echo $PROJNUM
         

  2. Create the following spec:
         
         cat << EOF > example-grpc-client.yaml
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: example-grpc-client
           namespace: default
           annotations:
             iam.gke.io/gcp-service-account: ${PROJNUM}-compute@developer.gserviceaccount.com
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: example-grpc-client
           namespace: default
           labels:
             k8s-app: example-grpc-client
         spec:
           replicas: 1
           selector:
             matchLabels:
               k8s-app: example-grpc-client
           strategy: {}
           template:
             metadata:
               annotations:
                 security.cloud.google.com/use-workload-certificates: ""
               labels:
                 k8s-app: example-grpc-client
             spec:
               containers:
               - image: phusion/baseimage:18.04-1.0.0
                 imagePullPolicy: IfNotPresent
                 name: example-grpc-client
                 command:
                 - /bin/sleep
                 - inf
                 env:
                 - name: GRPC_XDS_BOOTSTRAP
                   value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
                 resources:
                   limits:
                     cpu: 8
                     memory: 8Gi
                   requests:
                     cpu: 300m
                     memory: 512Mi
                 volumeMounts:
                 - name: grpc-td-conf
                   mountPath: /tmp/grpc-xds/
               initContainers:
               - name: grpc-td-init
                 image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
                 imagePullPolicy: Always
                 args:
                 - --output
                 - "/tmp/bootstrap/td-grpc-bootstrap.json"
                 resources:
                   limits:
                     cpu: 100m
                     memory: 100Mi
                   requests:
                     cpu: 10m
                     memory: 100Mi
                 volumeMounts:
                 - name: grpc-td-conf
                   mountPath: /tmp/bootstrap/
               serviceAccountName: example-grpc-client
               volumes:
               - name: grpc-td-conf
                 emptyDir:
                   medium: Memory
         EOF
         




###  Python 

  1. Run the following command to ensure that the project number is correctly set:
         
         if [ -z "$PROJNUM" ] ; then export PROJNUM=$(gcloud projects describe $(gcloud info --format='value(config.project)') --format="value(projectNumber)") ; fi ; echo $PROJNUM
         

  2. Create the following spec:
         
         cat << EOF > example-grpc-client.yaml
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: example-grpc-client
           namespace: default
           annotations:
             iam.gke.io/gcp-service-account: ${PROJNUM}-compute@developer.gserviceaccount.com
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: example-grpc-client
           namespace: default
           labels:
             k8s-app: example-grpc-client
         spec:
           replicas: 1
           selector:
             matchLabels:
               k8s-app: example-grpc-client
           strategy: {}
           template:
             metadata:
               annotations:
                 security.cloud.google.com/use-workload-certificates: ""
               labels:
                 k8s-app: example-grpc-client
             spec:
               containers:
               - image: phusion/baseimage:18.04-1.0.0
                 imagePullPolicy: IfNotPresent
                 name: example-grpc-client
                 command:
                 - /bin/sleep
                 - inf
                 env:
                 - name: GRPC_XDS_BOOTSTRAP
                   value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
                 resources:
                   limits:
                     cpu: 8
                     memory: 8Gi
                   requests:
                     cpu: 300m
                     memory: 512Mi
                 volumeMounts:
                 - name: grpc-td-conf
                   mountPath: /tmp/grpc-xds/
               initContainers:
               - name: grpc-td-init
                 image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
                 imagePullPolicy: Always
                 args:
                 - --output
                 - "/tmp/bootstrap/td-grpc-bootstrap.json"
                 resources:
                   limits:
                     cpu: 100m
                     memory: 100Mi
                   requests:
                     cpu: 10m
                     memory: 100Mi
                 volumeMounts:
                 - name: grpc-td-conf
                   mountPath: /tmp/bootstrap/
               serviceAccountName: example-grpc-client
               volumes:
               - name: grpc-td-conf
                 emptyDir:
                   medium: Memory
         EOF
         




###  Go 

  1. Run the following command to ensure that the project number is correctly set:
         
         if [ -z "$PROJNUM" ] ; then export PROJNUM=$(gcloud projects describe $(gcloud info --format='value(config.project)') --format="value(projectNumber)") ; fi ; echo $PROJNUM
         

  2. Create the following spec:
         
         cat << EOF > example-grpc-client.yaml
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: example-grpc-client
           namespace: default
           annotations:
             iam.gke.io/gcp-service-account: ${PROJNUM}-compute@developer.gserviceaccount.com
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: example-grpc-client
           namespace: default
           labels:
             k8s-app: example-grpc-client
         spec:
           replicas: 1
           selector:
             matchLabels:
               k8s-app: example-grpc-client
           strategy: {}
           template:
             metadata:
               annotations:
                 security.cloud.google.com/use-workload-certificates: ""
               labels:
                 k8s-app: example-grpc-client
             spec:
               containers:
               - image: golang:1.16-alpine
                 imagePullPolicy: IfNotPresent
                 name: example-grpc-client
                 command:
                 - /bin/sleep
                 - inf
                 env:
                 - name: GRPC_XDS_BOOTSTRAP
                   value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
                 resources:
                   limits:
                     cpu: 8
                     memory: 8Gi
                   requests:
                     cpu: 300m
                     memory: 512Mi
                 volumeMounts:
                 - name: grpc-td-conf
                   mountPath: /tmp/grpc-xds/
               initContainers:
               - name: grpc-td-init
                 image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
                 imagePullPolicy: Always
                 args:
                 - --output
                 - "/tmp/bootstrap/td-grpc-bootstrap.json"
                 resources:
                   limits:
                     cpu: 100m
                     memory: 100Mi
                   requests:
                     cpu: 10m
                     memory: 100Mi
                 volumeMounts:
                 - name: grpc-td-conf
                   mountPath: /tmp/bootstrap/
               serviceAccountName: example-grpc-client
               volumes:
               - name: grpc-td-conf
                 emptyDir:
                   medium: Memory
         EOF
         




Complete the process as follows.

  1. Apply the spec:
         
         kubectl apply -f example-grpc-client.yaml
         

  2. Grant the required roles to the service account:
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:${PROJECT_ID}.svc.id.goog[default/example-grpc-client]" \
           ${PROJNUM}-compute@developer.gserviceaccount.com
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID} \
           --member "serviceAccount:${PROJECT_ID}.svc.id.goog[default/example-grpc-client]" \
           --role roles/trafficdirector.client
         

  3. Verify that the client Pod is running:
         
         kubectl get pods
         

The command returns text similar to the following:
         
         NAMESPACE   NAME                                    READY   STATUS    RESTARTS   AGE
         default     example-grpc-client-7c969bb997-9fzjv    1/1     Running   0          104s
         [..skip..]
         




### Run the server

Build and run the xDS-enabled `helloworld` server in the server Pod you created earlier.

###  Java 

  1. Get the name of the Pod created for the `example-grpc-server` service:
         
         kubectl get pods | grep example-grpc-server
         

You see feedback such as the following:
         
         default    example-grpc-server-77548868d-l9hmf     1/1    Running   0     105s
         

  2. Open a shell to the server Pod:
         
         kubectl exec -it example-grpc-server-77548868d-l9hmf -- /bin/bash
         

  3. In the shell, verify that the bootstrap file at `/tmp/grpc-xds/td-grpc-bootstrap.json` matches the schema described in the section Bootstrap file.

  4. Download gRPC Java version 1.42.1 and build the `xds-hello-world` server application.
         
         curl -L https://github.com/grpc/grpc-java/archive/v1.42.1.tar.gz | tar -xz
         
         cd grpc-java-1.42.1/examples/example-xds
         
         ../gradlew --no-daemon installDist
         

  5. Run the server with the `--xds-creds` flag to indicate xDS-enabled security, using `50051` as the listening port, and `xds-server` as the server identification name:
         
         ./build/install/example-xds/bin/xds-hello-world-server --xds-creds 50051 xds-server
         

  6. After the server obtains the necessary configuration from Cloud Service Mesh, you see the following output:
         
         Listening on port 50051
         plain text health service listening on port 50052
         




###  C++ 

  1. Get the name of the Pod created for the `example-grpc-server` service:
         
         kubectl get pods | grep example-grpc-server
         

You see feedback such as the following:
         
         default    example-grpc-server-77548868d-l9hmf     1/1    Running   0     105s
         

  2. Open a shell to the server Pod:
         
         kubectl exec -it example-grpc-server-77548868d-l9hmf -- /bin/bash
         

  3. In the shell, verify that the bootstrap file at `/tmp/grpc-xds/td-grpc-bootstrap.json` matches the schema described in the section Bootstrap file.

  4. Download gRPC C++ and build the `xds-hello-world` server application.
         
         apt-get update -y && \
                 apt-get install -y \
                     build-essential \
                     clang \
                     python3 \
                     python3-dev
         
         curl -L https://github.com/grpc/grpc/archive/master.tar.gz | tar -xz
         
         cd grpc-master
         
         tools/bazel build examples/cpp/helloworld:xds_greeter_server
         

  5. Run the server using `50051` as the listening port, and `xds_greeter_server` as the server identification name:
         
         bazel-bin/examples/cpp/helloworld/xds_greeter_server --port=50051 --maintenance_port=50052 --secure
         

To run the server without credentials, you can specify the following:
         
         bazel-bin/examples/cpp/helloworld/xds_greeter_server --nosecure
         

  6. After the server obtains the necessary configuration from Cloud Service Mesh, you see the following output:
         
         Listening on port 50051
         plain text health service listening on port 50052
         




###  Python 

  1. Get the name of the Pod created for the `example-grpc-server` service:
         
         kubectl get pods | grep example-grpc-server
         

You see feedback such as the following:
         
         default    example-grpc-server-77548868d-l9hmf     1/1    Running   0     105s
         

  2. Open a shell to the server Pod:
         
         kubectl exec -it example-grpc-server-77548868d-l9hmf -- /bin/bash
         

  3. In the shell, verify that the bootstrap file at `/tmp/grpc-xds/td-grpc-bootstrap.json` matches the schema described in the section Bootstrap file.

  4. Download gRPC Python version 1.41.0 and build the example applicationn. 
         
         apt-get update -y
         
         
         apt-get install -y python3 python3-pip
         
         
         curl -L https://github.com/grpc/grpc/archive/v1.41.x.tar.gz | tar -xz
         
         
         cd grpc-1.41.x/examples/python/xds/
         
         
         python3 -m virtualenv venv
         
         
         source venv/bin/activate
         
         
         python3 -m pip install -r requirements.txt
         

  5. Run the server with the `--xds-creds` flag to indicate xDS-enabled security, using `50051` as the listening port.
         
         python3 server.py 50051 --xds-creds
         

  6. After the server obtains the necessary configuration from Cloud Service Mesh, you see the following output:
         
         2021-05-06 16:10:34,042: INFO     Running with xDS Server credentials
         2021-05-06 16:10:34,043: INFO     Greeter server listening on port 50051
         2021-05-06 16:10:34,046: INFO     Maintenance server listening on port 50052
         




###  Go 

  1. Get the name of the Pod created for the `example-grpc-server` service:
         
         kubectl get pods | grep example-grpc-server
         

You see feedback such as the following:
         
         default    example-grpc-server-77548868d-l9hmf     1/1    Running   0     105s
         

  2. Open a shell to the server Pod:
         
         kubectl exec -it example-grpc-server-77548868d-l9hmf -- /bin/sh
         

  3. In the shell, verify that the bootstrap file at `/tmp/grpc-xds/td-grpc-bootstrap.json` matches the schema described in the section Bootstrap file.

  4. Download gRPC Go version 1.41.0 and navigate to the directory containing the `xds-hello-world` server application.
         
         apk add curl
         
         curl -L https://github.com/grpc/grpc-go/archive/v1.42.0.tar.gz | tar -xz
         
         cd grpc-go-1.42.0/examples/features/xds/server
         
         

  5. Build and run the server with the `--xds_creds` flag to indicate xDS-enabled security, using `50051` as the listening port:
         
         GRPC_GO_LOG_VERBOSITY_LEVEL=2 GRPC_GO_LOG_SEVERITY="info" \
           go run main.go \
           -xds_creds \
           -port 50051
         

  6. After the server obtains the necessary configuration from Cloud Service Mesh, you see the following output:
         
         Using xDS credentials...
         Serving GreeterService on 0.0.0.0:50051 and HealthService on 0.0.0.0:50052
         




The health checking process takes from 3 to 5 minutes to show that your service is healthy after the server starts.

### Run the client and verify the configuration

Build and run the xDS-enabled `helloworld` client in the client Pod you created earlier.

###  Java 

  1. Get the name of the client Pod:
         
         kubectl get pods | grep example-grpc-client
         

You see feedback such as this:
         
         default    example-grpc-client-7c969bb997-9fzjv     1/1    Running   0     105s
         

  2. Open a shell to the client Pod:
         
         kubectl exec -it example-grpc-client-7c969bb997-9fzjv -- /bin/bash
         

  3. In the command shell, download gRPC Java version 1.42.1 and build the `xds-hello-world` client application.
         
         curl -L https://github.com/grpc/grpc-java/archive/v1.42.1.tar.gz | tar -xz
         
         cd grpc-java-1.42.1/examples/example-xds
         
         ../gradlew --no-daemon installDist
         

  4. Run the client with the `--xds-creds` flag to indicate xDS-enabled security, client name, and target connection string:
         
         ./build/install/example-xds/bin/xds-hello-world-client --xds-creds xds-client \
               xds:///helloworld-gke:8000
         

You should see output similar to this:
         
         Greeting: Hello xds-client, from xds-server
         




###  C++ 

  1. Get the name of the client Pod:
         
         kubectl get pods | grep example-grpc-client
         

You see feedback such as this:
         
         default    example-grpc-client-7c969bb997-9fzjv     1/1    Running   0     105s
         

  2. Open a shell to the client Pod:
         
         kubectl exec -it example-grpc-client-7c969bb997-9fzjv -- /bin/bash
         

  3. After you are inside the shell, download gRPC C++ and build the `xds-hello-world` client application.
         
         apt-get update -y && \
                 apt-get install -y \
                     build-essential \
                     clang \
                     python3 \
                     python3-dev
         
         
         curl -L https://github.com/grpc/grpc/archive/master.tar.gz | tar -xz
         
         
         cd grpc-master
         
         
         tools/bazel build examples/cpp/helloworld:xds_greeter_client
         

  4. Run the client with the `--xds-creds` flag to indicate xDS-enabled security, client name, and target connection string:
         
         bazel-bin/examples/cpp/helloworld/xds_greeter_client --target=xds:///helloworld-gke:8000
         

To run the client without credentials, use the following:
         
         bazel-bin/examples/cpp/helloworld/xds_greeter_client --target=xds:///helloworld-gke:8000 --nosecure
         

You should see output similar to this:
         
         Greeter received: Hello world
         




###  Python 

  1. Get the name of the client Pod:
         
         kubectl get pods | grep example-grpc-client
         

You see feedback such as this:
         
         default    example-grpc-client-7c969bb997-9fzjv     1/1    Running   0     105s
         

  2. Open a shell to the client Pod:
         
         kubectl exec -it example-grpc-client-7c969bb997-9fzjv -- /bin/bash
         

  3. After you are inside the shell, download gRPC Python version 1.41.0 and build the example client application.
         
         apt-get update -y
         apt-get install -y python3 python3-pip
         python3 -m pip install virtualenv
         curl -L https://github.com/grpc/grpc/archive/v1.41.x.tar.gz | tar -xz
         cd grpc-1.41.x/examples/python/xds/
         python3 -m virtualenv venv
         source venv/bin/activate
         python3 -m pip install -r requirements.txt
         

  4. Run the client with the `--xds-creds` flag to indicate xDS-enabled security, client name, and target connection string:
         
         python3 client.py xds:///helloworld-gke:8000 --xds-creds
         

You should see output similar to this:
         
         Greeter client received: Hello you from example-host!
         




###  Go 

  1. Get the name of the client Pod:
         
         kubectl get pods | grep example-grpc-client
         

You see feedback such as this:
         
         default    example-grpc-client-7c969bb997-9fzjv     1/1    Running   0     105s
         

  2. Open a shell to the client Pod:
         
         kubectl exec -it example-grpc-client-7c969bb997-9fzjv -- /bin/sh
         

  3. After you are inside the shell, download gRPC Go version 1.42.0 and navigate to the directory containing the `xds-hello-world` client application.
         
         apk add curl
         
         curl -L https://github.com/grpc/grpc-go/archive/v1.42.0.tar.gz | tar -xz
         
         cd grpc-go-1.42.0/examples/features/xds/client
         

  4. Build and run the client with the `--xds_creds` flag to indicate xDS-enabled security, client name, and target connection string:
         
         GRPC_GO_LOG_VERBOSITY_LEVEL=2 GRPC_GO_LOG_SEVERITY="info" \
           go run main.go \
           -xds_creds \
           -name xds-client \
           -target xds:///helloworld-gke:8000
         

You should see output similar to this:
         
         Greeting: Hello xds-client, from example-grpc-server-77548868d-l9hmf
         




## Configure service-level access with an authorization policy

gRFC A41 support is required for authorization policy support. You can find the required language versions on [github](https://github.com/grpc/grpc/blob/master/doc/grpc_xds_features.md)

Use these instructions to configure service-level access with authorization policies. Before you create authorization policies, read the caution in [Restrict access using authorization](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-%0Aoverview#restrict-access-authz).

To make it easier to verify the configuration, create an additional hostname that the client can use to refer to the `helloworld-gke` service.
    
    
    gcloud compute url-maps add-host-rule grpc-gke-url-map \
       --path-matcher-name grpc-gke-path-matcher \
       --hosts helloworld-gke-noaccess:8000
    

The following instructions create an authorization policy that allows requests that are sent by the `example-grpc-client` account in which the hostname is `helloworld-gke:8000` and the port is `50051`.

###  gcloud 

  1. Create an authorization policy by creating a file called `helloworld-gke-authz-policy.yaml`.
         
         action: ALLOW
         name: helloworld-gke-authz-policy
         rules:
         - sources:
           - principals:
             - spiffe://PROJECT_ID.svc.id.goog/ns/default/sa/example-grpc-client
           destinations:
           - hosts:
             - helloworld-gke:8000
             ports:
             - 50051
         

  2. Import the policy.
         
         gcloud network-security authorization-policies import \
           helloworld-gke-authz-policy \
           --source=helloworld-gke-authz-policy.yaml \
           --location=global
         

  3. Update the endpoint policy to reference the new authorization policy by appending the following to the file `ep-mtls-psms.yaml`.
         
         authorizationPolicy: projects/${PROJECT_ID}/locations/global/authorizationPolicies/helloworld-gke-authz-policy
         

The endpoint policy now specifies that both mTLS and the authorization policy must be enforced on inbound requests to Pods whose gRPC bootstrap files contain the label `app:helloworld`.

  4. Import the policy:
         
         gcloud network-services endpoint-policies import ep-mtls-psms \
           --source=ep-mtls-psms.yaml --location=global
         




### Validate the authorization policy

Use these instructions to confirm that the authorization policy is working correctly.

###  Java 

  1. Open a shell to the client pod you used previously.
         
         kubectl exec -it example-grpc-client-7c969bb997-9fzjv -- /bin/bash
         

  2. In the command shell, run the following commands to validate the setup.
         
         cd grpc-java-1.42.1/examples/example-xds
         ./build/install/example-xds/bin/xds-hello-world-client --xds-creds xds-client \
               xds:///helloworld-gke:8000
         

You should see output similar to this:
         
         Greeting: Hello xds-client, from xds-server
         

  3. Run the client again with the alternative server name. Note that this is a failure case. The request is invalid because the authorization policy only allows access to the `helloworld-gke:8000` hostname.
         
         ./build/install/example-xds/bin/xds-hello-world-client --xds-creds xds-client \
               xds:///helloworld-gke-noaccess:8000
         

You should see output similar to this:
         
         WARNING: RPC failed: Status{code=PERMISSION_DENIED}
         

If you don't see this output, the authorization policy might not be in use yet. Wait a few minutes and try the entire verification process again.




###  Go 

  1. Open a shell to the client pod you used previously.
         
         kubectl exec -it example-grpc-client-7c969bb997-9fzjv -- /bin/bash
         

  2. In the command shell, run the following commands to validate the setup.
         
         cd grpc-go-1.42.0/examples/features/xds/client
         GRPC_GO_LOG_VERBOSITY_LEVEL=2 GRPC_GO_LOG_SEVERITY="info" \
           go run main.go \
           -xds_creds \
           -name xds-client \
           -target xds:///helloworld-gke:8000
         

You should see output similar to this:
         
         Greeting: Hello xds-client, from example-grpc-server-77548868d-l9hmf
         

  3. Run the client again with the alternative server name. Note that this is a failure case. The request is invalid because the authorization policy only allows access to the `helloworld-gke:8000` hostname.
         
         GRPC_GO_LOG_VERBOSITY_LEVEL=2 GRPC_GO_LOG_SEVERITY="info" \
           go run main.go \
           -xds_creds \
           -name xds-client \
           -target xds:///helloworld-gke-noaccess:8000
         

You should see output similar to this:
         
         could not greet: rpc error: code = PermissionDenied desc = Incoming RPC is not allowed: rpc error: code = PermissionDenied desc = incoming RPC did not match an allow policy
         exit status 1
         

If you don't see this output, the authorization policy might not be in use yet. Wait a few minutes and try the entire verification process again.




## Use TLS instead of mTLS

Using TLS in this example requires only a small change.

  1. In the `ServerTlsPolicy`, drop the `mtlsPolicy`:
         
         cat << EOF > server-tls-policy.yaml
         name: "server-tls-policy"
         serverCertificate:
           certificateProviderInstance:
             pluginInstance: google_cloud_private_spiffe
         EOF
         

  2. Use this policy in the `EndpointPolicy` instead:
         
         cat << EOF > ep-tls-psms.yaml
         name: "ep-mtls-psms"
         type: "GRPC_SERVER"
         serverTlsPolicy: "projects/${PROJECT_ID}/locations/global/serverTlsPolicies/server-tls-policy"
         trafficPortSelector:
           ports:
           - "50051"
         endpointMatcher:
           metadataLabelMatcher:
             metadataLabelMatchCriteria: "MATCH_ALL"
             metadataLabels: []
         EOF
         

  3. The `ClientTlsPolicy` for mTLS also works in the TLS case but the `clientCertificate` section of the policy can be dropped since it is not required for TLS:
         
         cat << EOF > client-tls-policy.yaml
         name: "client-tls-policy"
         serverValidationCa:
         - certificateProviderInstance:
             pluginInstance: google_cloud_private_spiffe
         EOF
         




## Use service security with the Wallet example

This section provides a high-level overview of how to enable [the Wallet example](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management) with service security, for Java, C++, and Go.

###  Java 

You can find the example source code for Java at [github](https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples/tree/v2.x/java). The code already uses `XdsChannel` and`XdsServer` credentials when you configure proxyless security.

These instructions describe configuring the Wallet example with Go. The process is similar for Java. The instructions use a pre-existing Docker image that you obtain from the [Google Cloud container repository](https://console.cloud.google.com/artifacts/docker/trafficdirector-prod/us/gcr.io/td-grpc-wallet-example-java).

To create the example, follow these instructions:

  1. Clone the repository and get the files in the directory [gRPC examples](https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples/tree/master/gke-scripts).
  2. Edit the file `00-common-env.sh`. Comment out the existing line that sets the value of `WALLET_DOCKER_IMAGE` to the Go Docker image and uncomment the line that sets the value of `WALLET_DOCKER_IMAGE` to the Java Docker image.
  3. Create and configure Cloud Router instances, using the instructions in [Create and configure Cloud Router instances](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#create-cloud-router) or using the function `create_cloud_router_instances` in the script `10.apis.sh`.
  4. Create a cluster using [the instructions for the `hello world` example](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-proxyless-setup#create-cluster). or the function `create_cluster` in the script `20-cluster.sh`.
  5. Create private certificate authorities using [the instructions for CA Service](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-proxyless-setup#configure-cas) or using the script `30-private-ca-setup.sh`.
  6. Create Kubernetes resources, including service accounts, namespaces, Kubernetes services, NEGs, and server side deployment for all the services: `account`, `stats`, `stats_premium`, `wallet_v1`, `wallet_v2`, using the script `40-k8s-resources.sh`.
  7. For each of the services you created, create a health check and backend service using `create_health_check` and `create_backend_service` in the script `50-td-components.sh`.
  8. Create the Cloud Service Mesh routing components using `create_routing_components` in the script `60-routing-components.sh`.
  9. Create the Cloud Service Mesh security components for each backend service using `create_security_components` in the script `70-security-components.sh`.
  10. Create the Wallet client deployment using `create_client_deployment` in the script `75-client-deployment.sh`.
  11. Verify the configuration by launching your client as described in [Verify with grpc-wallet clients](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#verify-grpc-wallet-clients).



###  C++ 

You can find the example source code for C++ at [github](https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples/tree/v2.x/cpp). The code already uses `XdsChannel` and`XdsServer` credentials when you configure proxyless security.

These instructions describe configuring the Wallet example with Go. The process is similar for C++. The instructions use a pre-existing Docker image that you obtain from the [Google Cloud container repository](https://console.cloud.google.com/artifacts/docker/trafficdirector-prod/us/gcr.io/td-grpc-wallet-example-cpp).

To create the example, follow these instructions:

  1. Clone the repository and get the files in the directory [gRPC examples](https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples/tree/master/gke-scripts).
  2. Edit the file `00-common-env.sh`. Comment out the existing line that sets the value of `WALLET_DOCKER_IMAGE` to the Go Docker image and uncomment the line that sets the value of `WALLET_DOCKER_IMAGE` to the C++ Docker image.
  3. Create and configure Cloud Router instances, using the instructions in [Create and configure Cloud Router instances](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#create-cloud-router) or using the function `create_cloud_router_instances` in the script `10.apis.sh`.
  4. Create a cluster using [the instructions for the `hello world` example](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-proxyless-setup#create-cluster). or the function `create_cluster` in the script `20-cluster.sh`.
  5. Create private certificate authorities using [the instructions for CA Service](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-proxyless-setup#configure-cas) or using the script `30-private-ca-setup.sh`.
  6. Create Kubernetes resources, including service accounts, namespaces, Kubernetes services, NEGs, and server side deployment for all the services: `account`, `stats`, `stats_premium`, `wallet_v1`, `wallet_v2`, using the script `40-k8s-resources.sh`.
  7. For each of the services you created, create a health check and backend service using `create_health_check` and `create_backend_service` in the script `50-td-components.sh`.
  8. Create the Cloud Service Mesh routing components using `create_routing_components` in the script `60-routing-components.sh`.
  9. Create the Cloud Service Mesh security components for each backend service using `create_security_components` in the script `70-security-components.sh`.
  10. Create the Wallet client deployment using `create_client_deployment` in the script `75-client-deployment.sh`.
  11. Verify the configuration by launching your client as described in [Verify with grpc-wallet clients](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#verify-grpc-wallet-clients).



###  Go 

You can find example source code for Go at [github](https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples/tree/v2.x/go). The code already uses `XdsChannel` and`XdsServer` credentials when you configure proxyless security.

The instructions use a pre-existing Docker image that you obtain from the [Google Cloud container repository](https://console.cloud.google.com/artifacts/docker/trafficdirector-prod/us/gcr.io/td-grpc-wallet-example-go).

To create the example, follow these instructions:

  1. Clone the repository and get the files in the directory [gRPC examples](https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples/tree/master/gke-scripts).
  2. Edit the file `00-common-env.sh` to set the correct values for the environment variables.
  3. Create and configure Cloud Router instances, using the instructions in [Create and configure Cloud Router instances](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#create-cloud-router) or using the function `create_cloud_router_instances` in the script `10.apis.sh`.
  4. Create a cluster using [the instructions for the `hello world` example](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-proxyless-setup#create-cluster). or the function `create_cluster` in the script `20-cluster.sh`.
  5. Create private certificate authorities using [the instructions for CA Service](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-proxyless-setup#configure-cas) or using the script `30-private-ca-setup.sh`.
  6. Create Kubernetes resources, including service accounts, namespaces, Kubernetes services, NEGs, and server side deployment for all the services: `account`, `stats`, `stats_premium`, `wallet_v1`, `wallet_v2`, using the script `40-k8s-resources.sh`.
  7. For each of the services you created, create a health check and backend service using `create_health_check` and `create_backend_service` in the script `50-td-components.sh`.
  8. Create the Cloud Service Mesh routing components using `create_routing_components` in the script `60-routing-components.sh`.
  9. Create the Cloud Service Mesh security components for each backend service using `create_security_components` in the script `70-security-components.sh`.
  10. Create the Wallet client deployment using `create_client_deployment` in the script `75-client-deployment.sh`.
  11. Verify the configuration by launching your client as described in [Verify with grpc-wallet clients](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#verify-grpc-wallet-clients).



## Bootstrap file

The setup process in this guide uses a bootstrap generator to create the required bootstrap file. This section provides reference information about the bootstrap file itself.

The bootstrap file contains configuration information required by proxyless gRPC code, including connection information for the xDS server. The bootstrap file contains security configuration that is required by the proxyless gRPC security feature. The gRPC server requires one additional field, as described in the following sections. A sample bootstrap file looks like this:
    
    
    {
      "xds_servers": [
        {
          "server_uri": "trafficdirector.googleapis.com:443",
          "channel_creds": [
            {
              "type": "google_default"
            }
          ],
          "server_features": [
            "xds_v3"
          ]
        }
      ],
      "node": {
        "cluster": "cluster",
        "id": "projects/9876012345/networks/default/nodes/client1",
        "metadata": {
          "TRAFFICDIRECTOR_GCP_PROJECT_NUMBER": "9876012345",
          "TRAFFICDIRECTOR_NETWORK_NAME": "default",
          "INSTANCE_IP": "10.0.0.3"
        },
        "locality": {
          "zone": "us-central1-a"
        }
      },
      "server_listener_resource_name_template": "grpc/server?xds.resource.listening_address=%s",
      "certificate_providers": {
        "google_cloud_private_spiffe": {
          "plugin_name": "file_watcher",
          "config": {
            "certificate_file": "/var/run/secrets/workload-spiffe-credentials/certificates.pem",
            "private_key_file": "/var/run/secrets/workload-spiffe-credentials/private_key.pem",
            "ca_certificate_file": "/var/run/secrets/workload-spiffe-credentials/ca_certificates.pem",
            "refresh_interval": "600s"
          }
        }
      }
    }
    

### Updates to the bootstrap file for security service

The following fields reflect modifications related to security and xDS v3 usage:

The `id` field inside `node` provides a unique identity for the gRPC client to Cloud Service Mesh. You must provide the Google Cloud project number and network name using the node ID in the this format:

`projects/{project number}/networks/{network name}/nodes/[UNIQUE_ID]`

An example for project number 1234 and the default network is:

`projects/1234/networks/default/nodes/client1`

The `INSTANCE_IP` field is the IP address of the Pod, or `0.0.0.0` to indicate `INADDR_ANY`. This field is used by the gRPC server for fetching the Listener resource from Cloud Service Mesh for server side security.

### Security config fields in the bootstrap file

JSON key | Type | Value | Notes  
---|---|---|---  
`server_listener_resource_name_template` | String | `grpc/server?xds.resource.listening_address=%s` | Required for gRPC servers. gRPC uses this value to compose the resource name for fetching the `Listener` resource from Cloud Service Mesh for server side security and other configuration. gRPC uses this to form the resource name string   
`certificate_providers` | JSON struct | `google_cloud_private_spiffe` | Required. The value is a JSON struct representing a map of names to _certificate provider instances_. A certificate provider instance is used for fetching identity and root certificates. The example bootstap file contains one name: `google_cloud_private_spiffe` with the certificate provider instance JSON struct as the value. Each certificate provider instance JSON struct has two fields: 

  * `plugin_name`. Required value that identifies the certificate provider plugin to be used as required by gRPC's plugin architecture for certificate providers. gRPC has built-in support for the file-watcher plugin that is used in this setup. The plugin_name is `file_watcher`. 
  * `config`. Required value that identifies the JSON configuration blog for the `file_watcher` plugin. The schema and content depend on the plugin.

  
  
The contents of the `config` JSON structure for the `file_watcher` plugin are:

  * `certificate_file`: Required string. This value is the location of the identity certificate.
  * `private_key_file`: Required string. The value is the location of the private key file, which should match the identity certificate.
  * `ca_certificate_file`: Required string. The value is the location of the root certificate, which is also know as the trust bundle.
  * `refresh_interval`: Optional string. The value indicates the refresh interval, specified using the string representation of a Duration's JSON mapping. The default value is "600s", a duration of 10 minutes.



### Bootstrap generator

The bootstrap generator container image is available at `gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0`. Its source code is available at `https://github.com/GoogleCloudPlatform/traffic-director-grpc-bootstrap`. The most commonly used command line options are these:

  * `--output`: Use this option to specify where the output bootstrap file is written to, for example, the command `--output /tmp/bootstrap/td-grpc-bootstrap.json` generates the bootstrap file to `/tmp/bootstrap/td-grpc-bootstrap.json` in the Pod's file system.
  * `--node-metadata`: Use this flag to populate the node metadata in the bootstrap file. This is required when you use metadata label matchers in the `EndpointPolicy` where Cloud Service Mesh uses the label data provided in the node metadata section of the bootstrap file. The argument is supplied in the form key=value, for example: `--node-metadata version=prod --node-metadata type=grpc`



These options add the following in the node metadata section of the bootstrap file:
    
    
    {
      "node": {
    ...
        "metadata": {
          "version": "prod",
          "type": "grpc",
    ...
        },
    ...
      },
    ...
    }
    

**Note:** Per policy, we encourage users to check for updates of the TD gRPC bootstrap generator yearly.

## Delete the deployment

You can optionally run these commands to delete the deployment you created using this guide.

To delete the cluster, run this command:
    
    
    gcloud container clusters delete CLUSTER_NAME --zone ZONE --quiet
    

To delete the resources you created, run these commands:
    
    
    gcloud compute backend-services delete grpc-gke-helloworld-service --global --quiet
    cloud compute network-endpoint-groups delete example-grpc-server --zone ZONE --quiet
    gcloud compute firewall-rules delete grpc-gke-allow-health-checks --quiet
    gcloud compute health-checks delete grpc-gke-helloworld-hc --quiet
    gcloud network-services endpoint-policies delete ep-mtls-psms \
        --location=global --quiet
    gcloud network-security authorization-policies delete helloworld-gke-authz-policy \
       --location=global --quiet
    gcloud network-security client-tls-policies delete client-mtls-policy \
        --location=global --quiet
    gcloud network-security server-tls-policies delete server-tls-policy \
        --location=global --quiet
    gcloud network-security server-tls-policies delete server-mtls-policy \
        --location=global --quiet
    

## Troubleshooting

Use these instructions to help you resolve problems with your security deployment.

### Workloads are unable to get config from Cloud Service Mesh

If you see an error similar to this:

`PERMISSION_DENIED: Request had insufficient authentication scopes.`

Make sure of the following:

  * You created your GKE cluster with the argument `--scopes=cloud-platform` argument.
  * You assigned the `roles/trafficdirector.client` to your Kuberneters service accounts.
  * You assigned the `roles/trafficdirector.client` to your default Google Cloud service account (${GSA_EMAIL} above).
  * You enabled the `trafficdirector.googleapis.com` service (API).



### Your gRPC server does not use TLS or mTLS even with correct Cloud Service Mesh configuration

Make sure you specify `GRPC_SERVER` in your endpoint policies configuration. If you specified `SIDECAR_PROXY` gRPC ignores the configuration.

### You are unable to create the GKE cluster with the requested cluster version

The GKE cluster creation command might fail with an error something like this:

`Node version "1.20.5-gke.2000" is unsupported.`

Make sure that you are using the argument `--release-channel rapid` in your cluster creation command. You need to use the rapid release channel to get the correct version for this release.

### You see a `No usable endpoint` error

If a client can't communicate with the server because of a `No usable endpoint` error, the health checker might have marked the server backends as unhealthy. To check the health of the backends, run this `gcloud` command:
    
    
    gcloud compute backend-services get-health grpc-gke-helloworld-service --global
    

If the command returns the backend status unhealthy, it might be for one of these reasons:

  * The firewall was not created or does not contain the correct source IP range.
  * The target tags on your firewall don't match the tags on the cluster you created.



### Workloads are unable to communicate in the security setup

If your workloads are not able to communicate after you set up security for your proxyless service mesh, follow these instructions to determine the cause.

  1. Disable proxyless security and eliminate issues in the proxyless service mesh load balancing use-cases. To disable security in the mesh do one of the following: 
     1. Use plain text credentials on the client and server side OR
     2. don't configure security for the backend service and endpoint policy in the Cloud Service Mesh configuration.



Follow the steps in [Troubleshooting proxyless Cloud Service Mesh deployments](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/troubleshooting-proxyless), because there is no security setup in your deployment.

  1. Modify your workloads to use xDS credentials with plain text or insecure credentials as the fallback credentials. Keep the Cloud Service Mesh configuration with security disabled as discussed previously. In this case, although gRPC is allowing Cloud Service Mesh to configure security, Cloud Service Mesh does not send security information in which case gRPC should fall back to plain text (or insecure) credentials which should work similarly to the first case previously described. If this case does not work, do the following:

     1. Increase the logging level on both the client and server side so that you can see the xDS messages exchanged between gRPC and Cloud Service Mesh.
     2. Ensure that Cloud Service Mesh does not have security enabled in the CDS and LDS responses that are sent to the workloads.
     3. Ensure that the workloads are not using TLS or mTLS modes in their channels. If you see any log messages related to TLS handshakes, check your application source code and make sure that you are using insecure or plain text as your fallback credentials. If the application source code is correct, this might be a bug in the gRPC library
  2. Verify that the CA Service integration with GKE is working correctly for your GKE cluster by following the troubleshooting steps in that User Guide. Make sure that the certificates and keys provided by that feature are made available in the specified directory, `/var/run/secrets/workload-spiffe-credentials/`.

  3. Enable TLS (instead of mTLS) in your mesh, as described previously, and restart your client and server workloads.

     1. Increase the logging level on both the client and server side to be able to see the xDS messages exchanged between gRPC and Cloud Service Mesh.
     2. Ensure that Cloud Service Mesh has enabled security in the CDS and LDS responses that are sent to the workloads.



### Client fails with a `CertificateException` and a message `Peer certificate SAN check failed`

This indicates a problem with the `subjectAltNames` values in the `SecuritySettings` message. Note that these values are based on the Kubernetes services you created for your backend service. For every such Kubernetes service you created, there is an associated SPIFFE ID, in this format:

`spiffe://${WORKLOAD_POOL}/ns/${K8S_NAMESPACE}/sa/${SERVICE_ACCOUNT}`

These values are:

  * `WORKLOAD_POOL`: The workload pool for the cluster, which is `${PROJECT_ID}.svc.id.goog`
  * `K8S_NAMESPACE`: The Kubernetes namespace you used in the deployment of the service
  * `SERVICE_ACCOUNT`: The Kubernetes service account you used in the deployment of the service



For every Kubernetes service you attached to your backend service as a network endpoint group, make sure that you correctly computed the SPIFFE ID and added that SPIFFE ID to the `subjectAltNames` field in the `SecuritySettings` message.

### Applications cannot use the mTLS certificates with your gRPC library

If your applications are unable to use the mTLS certificates with your gRPC library, do the following:

  1. Verify that the Pod spec contains the `security.cloud.google.com/use-workload-certificates` annotation that is described in Creating a proxyless gRPC service with NEGs.

  2. Verify that the files containing the certificate chain along with the leaf certificate, private key, and the trusted CA certificates are accessible at the following paths from within the Pod:

     1. Certificate chain along with leaf cert: "/var/run/secrets/workload-spiffe-credentials/certificates.pem"
     2. Private key: "/var/run/secrets/workload-spiffe-credentials/private_key.pem"
     3. CA Bundle: "/var/run/secrets/workload-spiffe-credentials/ca_certificates.pem"
  3. If the certificates in the previous step are not available, do the following:
         
         gcloud privateca subordinates describe SUBORDINATE_CA_POOL_NAME   
         
             --location=LOCATION
           

     1. Verify that GKE's control plane has the correct IAM role binding, granting it access to CA Service:
            
            # Get the IAM policy for the CA
            gcloud privateca roots get-iam-policy ROOT_CA_POOL_NAME
            
            # Verify that there is an IAM binding granting access in the following format
            - members:
            - serviceAccount:service-projnumber@container-engine-robot.iam.gserviceaccount.com
            role: roles/privateca.certificateManager
            
            # Where projnumber is the project number (e.g. 2915810291) for the GKE cluster.
            

     2. Verify that the certificate has not expired. This is the certificate chain and leaf certificate at `/var/run/secrets/workload-spiffe-credentials/certificates.pem`. To check, run this command: 
            
            cat /var/run/secrets/workload-spiffe-credentials/certificates.pem | openssl x509 -text -noout | grep "Not After"
            

     3. Verify that the key type is supported by your application by running this command: 
            
            cat /var/run/secrets/workload-spiffe-credentials/certificates.pem | openssl x509 -text -noout | grep "Public Key Algorithm" -A 3
            

     4. Verify that your gRPC Java application has the following `keyAlgorithm` in the `WorkloadCertificateConfig` YAML file:
    
    keyAlgorithm:
        rsa:
          modulusSize: 4096
    

  4. Verify that the CA uses the same key family as the certificate key.




### An application's certificate is rejected by the client, server, or peer

  1. Verify that the peer application uses the same trust bundle to verify the certificate.
  2. Verify that the certificate in use is not expired (certificate chain along with leaf cert: "/var/run/secrets/workload-spiffe-credentials/certificates.pem").



### Pods remain in a pending state

If the Pods stay in a pending state during the setup process, increase the CPU and memory resources for the Pods in your deployment spec.

### Unable to create cluster with the `--enable-mesh-certificates` flag

Ensure that you are running the latest version of the gcloud CLI:
    
    
    gcloud components update
    

Note that the `--enable-mesh-certificates` flag works only with `gcloud beta`.

### Pods don't start

Pods that use GKE mesh certificates might fail to start if certificate provisioning is failing. This can happen in situations like the following:

  * The `WorkloadCertificateConfig` or the `TrustConfig` is misconfigured or missing.
  * CSRs aren't being approved.



You can check whether certificate provisioning is failing by checking the Pod events.

  1. Check the status of your Pod:
         
         kubectl get pod -n POD_NAMESPACE POD_NAME
         

Replace the following:

     * `POD_NAMESPACE`: the namespace of your Pod.
     * `POD_NAME`: the name of your Pod.
  2. Check recent events for your Pod:
         
         kubectl describe pod -n POD_NAMESPACE POD_NAME
         

  3. If certificate provisioning is failing, you will see an event with `Type=Warning`, `Reason=FailedMount`, `From=kubelet`, and a `Message` field that begins with `MountVolume.SetUp failed for volume "gke-workload-certificates"`. The `Message` field contains troubleshooting information.
         
         Events:
           Type     Reason       Age                From       Message
           ----     ------       ----               ----       -------
           Warning  FailedMount  13s (x7 over 46s)  kubelet    MountVolume.SetUp failed for volume "gke-workload-certificates" : rpc error: code = Internal desc = unable to mount volume: store.CreateVolume, err: unable to create volume "csi-4d540ed59ef937fbb41a9bf5380a5a534edb3eedf037fe64be36bab0abf45c9c": caPEM is nil (check active WorkloadCertificateConfig)
         

  4. See the following troubleshooting steps if the reason your Pods don't start is because of misconfigured objects, or because of rejected CSRs.




#### `WorkloadCertificateConfig` or `TrustConfig` is misconfigured

Ensure that you created the `WorkloadCertificateConfig` and `TrustConfig` objects correctly. You can diagnose misconfigurations on either of these objects using `kubectl`.

  1. Retrieve the current status.

For `WorkloadCertificateConfig`:
         
         kubectl get WorkloadCertificateConfig default -o yaml
         

For `TrustConfig`:
         
         kubectl get TrustConfig default -o yaml
         

  2. Inspect the status output. A valid object will have a condition with `type: Ready` and `status: "True"`.
         
         status:
           conditions:
           - lastTransitionTime: "2021-03-04T22:24:11Z"
             message: WorkloadCertificateConfig is ready
             observedGeneration: 1
             reason: ConfigReady
             status: "True"
             type: Ready
         

For invalid objects, `status: "False"` appears instead. The`reason`and `message` field contain additional troubleshooting details.




#### CSRs are not approved

If something goes wrong during the CSR approval process, you can check the error details in the `type: Approved` and `type: Issued` conditions of the CSR.

  1. List relevant CSRs using `kubectl`:
         
         kubectl get csr \
           --field-selector='spec.signerName=spiffe.gke.io/spiffe-leaf-signer'
         

  2. Choose a CSR that is either `Approved` and not `Issued`, or is not `Approved`.

  3. Get details for the selected CSR using kubectl:
         
         kubectl get csr CSR_NAME -o yaml
         

Replace `CSR_NAME` with the name of the CSR you chose.




A valid CSR has a condition with `type: Approved` and `status: "True"`, and a valid certificate in the `status.certificate` field:
    
    
    status:
      certificate: <base64-encoded data>
      conditions:
      - lastTransitionTime: "2021-03-04T21:58:46Z"
        lastUpdateTime: "2021-03-04T21:58:46Z"
        message: Approved CSR because it is a valid SPIFFE SVID for the correct identity.
        reason: AutoApproved
        status: "True"
        type: Approved
    

Troubleshooting information for invalid CSRs appears in the `message` and `reason` fields.

### Pods are missing certificates

  1. Get the Pod spec for your Pod:
         
         kubectl get pod -n POD_NAMESPACE POD_NAME -o yaml
         

Replace the following:

     * `POD_NAMESPACE`: the namespace of your Pod.
     * `POD_NAME`: the name of your Pod.
  2. Verify that the Pod spec contains the `security.cloud.google.com/use-workload-certificates` annotation described in Configure Pods to receive mTLS credentials.

  3. Verify that the GKE mesh certificates admission controller successfully injected a CSI driver volume of type `workloadcertificates.security.cloud.google.com` into your Pod spec:
         
         volumes:
         ...
         -csi:
           driver: workloadcertificates.security.cloud.google.com
           name: gke-workload-certificates
         ...
         

  4. Check for the presence of a volume mount in each of the containers:
         
         containers:
         - name: ...
           ...
           volumeMounts:
           - mountPath: /var/run/secrets/workload-spiffe-credentials
             name: gke-workload-certificates
             readOnly: true
           ...
         

  5. Verify that the following certificate bundles and the private key are available at the following locations in the Pod:

     * Certificate chain bundle: `/var/run/secrets/workload-spiffe-credentials/certificates.pem`
     * Private key: `/var/run/secrets/workload-spiffe-credentials/private_key.pem`
     * CA trust anchor bundle: `/var/run/secrets/workload-spiffe-credentials/ca_certificates.pem`
  6. If the files are not available, perform the following steps:

     1. Retrieve the CA Service ([Preview](https://cloud.google.com/products/#product-launch-stages)) instance for the cluster:
            
            kubectl get workloadcertificateconfigs default -o jsonpath '{.spec.certificateAuthorityConfig.certificateAuthorityServiceConfig.endpointURI}'
            

     2. Retrieve the status of the CA Service ([Preview](https://cloud.google.com/products/#product-launch-stages)) instance:
            
            gcloud privateca ISSUING_CA_TYPE describe ISSUING_CA_NAME \
              --location ISSUING_CA_LOCATION
            

Replace the following:

        * `ISSUING_CA_TYPE`: the issuing CA type, which must be either `subordinates` or `roots`.
        * `ISSUING_CA_NAME`: the name of the issuing CA.
        * `ISSUING_CA_LOCATION`: the region of the issuing CA.
     3. Get the IAM policy for the root CA:
            
            gcloud privateca roots get-iam-policy ROOT_CA_NAME
            

Replace `ROOT_CA_NAME` with the name of your root CA.

     4. In the IAM policy, verify that the `privateca.auditor` policy binding exists:
            
            ...
            - members:
              - serviceAccount:service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com
              role: roles/privateca.auditor
            ...
            

In this example, `PROJECT_NUMBER` is your cluster's project number.

     5. Get the IAM policy for the subordinate CA:
            
            gcloud privateca subordinates get-iam-policy SUBORDINATE_CA_NAME
            

Replace `SUBORDINATE_CA_NAME` with the subordinate CA name.

     6. In the IAM policy, verify that the `privateca.certificateManager` policy binding exists:
            
            ...
            - members:
              - serviceAccount: service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com
              role: roles/privateca.certificateManager
            ...
            

In this example, `PROJECT_NUMBER` is your cluster's project number. 




### Applications cannot use issued mTLS credentials

  1. Verify that the certificate has not expired:
         
         cat /var/run/secrets/workload-spiffe-credentials/certificates.pem | openssl x509 -text -noout | grep "Not After"
         

  2. Check that the key type you used is supported by your application.
         
         cat /var/run/secrets/workload-spiffe-credentials/certificates.pem | openssl x509 -text -noout | grep "Public Key Algorithm" -A 3
         

  3. Check that the issuing CA uses the same key family as the certificate key.

     1. Get the status of the CA Service ([Preview](https://cloud.google.com/products/#product-launch-stages)) instance:
            
            gcloud privateca ISSUING_CA_TYPE describe ISSUING_CA_NAME \
              --location ISSUING_CA_LOCATION
            

Replace the following:

        * `ISSUING_CA_TYPE`: the issuing CA type, which must be either `subordinates` or `roots`.
        * `ISSUING_CA_NAME`: the name of the issuing CA.
        * `ISSUING_CA_LOCATION`: the region of the issuing CA.
     2. Check that the `keySpec.algorithm` in the output is the same key algorithm you defined in the `WorkloadCertificateConfig` YAML manifest. The output looks like this:
            
            config:
              ...
              subjectConfig:
                commonName: td-sub-ca
                subject:
                  organization: TestOrgLLC
                subjectAltName: {}
            createTime: '2021-05-04T05:37:58.329293525Z'
            issuingOptions:
              includeCaCertUrl: true
            **keySpec:
              algorithm: RSA_PKCS1_2048_SHA256**
             ...
            




### Certificates get rejected

  1. Verify that the peer application uses the same trust bundle to verify the certificate.
  2. Verify that the certificate has not expired:
         
         cat /var/run/secrets/workload-spiffe-credentials/certificates.pem | openssl x509 -text -noout | grep "Not After"
         

  3. Verify that the client code, if not using the gRPC Go [Credentials Reloading API](https://github.com/grpc/grpc-go/tree/master/security/advancedtls), periodically refreshes the credentials from the file system.

  4. Verify that your workloads are in the same trust domain as your CA. GKE mesh certificates supports communication between workloads in a single trust domain.




## Limitations

Cloud Service Mesh service security is supported only with GKE. You cannot deploy service security with Compute Engine.

Cloud Service Mesh does not support scenarios where there are two or more endpoint policy resources that match equally to an endpoint, for example, two policies with the same labels and ports, or two or more policies with different labels that match equally with an endpoint's labels. For more information on how endpoint policys are matched to an endpoint's labels, see the [APIs for EndpointPolicy.EndpointMatcher.MetadataLabelMatcher](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#EndpointMatcher). In such situations, Cloud Service Mesh does not generate security configuration from any of the conflicting policies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
