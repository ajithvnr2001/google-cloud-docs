---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/security/certificate-authority-service/
title: Configure Certificate Authority Service for Managed Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:29:34.225512+00:00
---

# Configure Certificate Authority Service for Managed Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/security/certificate-authority-service/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Certificate Authority Service for Managed Cloud Service Mesh

This guide describes how to configure Certificate Authority Service for managed Cloud Service Mesh. For information on in-cluster Cloud Service Mesh, see [Install default features and Certificate Authority (CA) Service](https://docs.cloud.google.com/service-mesh/v1.30/docs/unified-install/install-anthos-service-mesh#install_ca_service).

**Note:** Using Certificate Authority Service (CA Service) is not supported when using the [fleet-default configuration](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/provision-control-plane#configure_your_fleet) in GKE Enterprise and registering clusters to the fleet during cluster creation. To use CA Service we recommend that you [configure Cloud Service Mesh per cluster](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/provision-control-plane#configure_per_cluster).

In addition to [Cloud Service Mesh certificate authority](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/security-overview#features), you can configure Cloud Service Mesh to use [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs). This guide provides you an opportunity to integrate with CA Service, which is recommended for the following use cases:

  * If you need different certificate authorities to sign workload certificates on different clusters.
  * If you need to back your signing keys in a [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm).
  * If you are in a highly regulated industry and are subject to compliance.
  * If you want to chain up your Cloud Service Mesh CA to a custom enterprise root certificate to sign workload certificates.



The cost of Cloud Service Mesh certificate authority is included in the [Cloud Service Mesh pricing](https://cloud.google.com/service-mesh/pricing). The CA Service isn't included in the base Cloud Service Mesh price and is [charged separately](https://cloud.google.com/certificate-authority-service/pricing). Additionally, CA Service comes with an [explicit SLA](https://cloud.google.com/certificate-authority-service/sla), but the Cloud Service Mesh certificate authority does not.

## Prerequisites

As a starting point, this guide assumes that you have:

  * [A Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects)
  * [A Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account)
  * Obtained the [required permissions](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/provision-control-plane#roles-required) to provision Cloud Service Mesh
  * Enabled [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on your clusters and node pools.
  * One or more clusters with a [supported version of GKE](https://docs.cloud.google.com/service-mesh/v1.30/docs/managed/supported-features-mcp#environments), in one of the supported [regions](https://docs.cloud.google.com/service-mesh/v1.30/docs/managed/supported-features-mcp#regions). To learn how to create a Google Kubernetes Engine cluster with Cloud Service Mesh enabled, see the per cluster configuration in the [Provision a managed Cloud Service Mesh control plane on Google Kubernetes Engine](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/provision-control-plane#configure_per_cluster) document. Enabling managed Cloud Service Mesh as a default configuration for your fleet and registering clusters to the fleet during cluster creation only supports [Mesh CA](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/security-overview#features). You must configure Cloud Service Mesh per cluster and enable CA Service explicitly for each cluster. 




## Requirements

Enable the required API in the project where the CA pool will be configured.
    
    
     gcloud services enable privateca.googleapis.com \
          --project=CA_PROJECT_ID
    

## Configure CA Service

  1. Create the [CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool) in the tier `DevOps` and in the same region as the cluster that it serves to avoid excessive latency issues or potential cross-region outages. For more information, see [Workload-optimized tiers](https://docs.cloud.google.com/certificate-authority-service/docs/tiers).
  2. [Create the CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities) to have at least one active certificate authority in the CA pool in the same project as the GKE cluster. Use subordinate CA's to sign Cloud Service Mesh workload certificates. Note down the [CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool) corresponding to the subordinate CA.
  3. If it is meant to only service certificates for Cloud Service Mesh workloads, set up the following issuance policy for the CA pool:

### policy.yaml
         
         baselineValues:
           keyUsage:
             baseKeyUsage:
               digitalSignature: true
               keyEncipherment: true
             extendedKeyUsage:
               serverAuth: true
               clientAuth: true
           caOptions:
             isCa: false
         identityConstraints:
           allowSubjectPassthrough: false
           allowSubjectAltNamesPassthrough: true
           celExpression:
             expression: subject_alt_names.all(san, san.type == URI && san.value.startsWith("spiffe://PROJECT_ID.svc.id.goog/ns/") )
         

**Note:** As a best practice for multi-cluster meshes, set one subordinate CA pool per unique cluster region. All the subordinate CA pools should chain to the same root CA pool. 
  4. To update the CA pool's issuance policy, use the following command:
         
         gcloud privateca pools update CA_POOL --location ca_region --issuance-policy policy.yaml
         

For information on setting a policy on a pool, see [Using a certificate issuance policy](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy).

  5. If you are using a [certificate template](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-template), then configure it now. For more information, follow the [CA Service guide](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-template#workload-identity) for workload identity certificates. Ensure the certificate template is created in the same region as the CA pool. If there are multiple regions for CA pools, then create a certificate template per region.




### Roles required to use CA service

For this integration, all workloads in Cloud Service Mesh require the following [IAM roles](https://docs.cloud.google.com/certificate-authority-service/docs/reference/permissions-and-roles). These roles-bindings need to be explicitly applied for Cloud Service Mesh workloads:
    
    
        WORKLOAD_IDENTITY="FLEET_PROJECT_ID.svc.id.goog:/allAuthenticatedUsers/"
    
        gcloud privateca pools add-iam-policy-binding CA_POOL \
          --project FLEET_PROJECT_ID \
          --location ca_region \
          --member "group:${WORKLOAD_IDENTITY}" \
          --role "roles/privateca.workloadCertificateRequester"
    
        gcloud privateca pools add-iam-policy-binding CA_POOL \
          --project FLEET_PROJECT_ID \
          --location ca_region \
          --member "group:${WORKLOAD_IDENTITY}" \
          --role "roles/privateca.auditor"
    

If using certificate templates:
    
    
        gcloud privateca templates add-iam-policy-binding CERT_TEMPLATE_ID \
            --member "group:${WORKLOAD_IDENTITY}" \
            --role "roles/privateca.templateUser"
    

## Limitations

  * Configure and pick the CA before provisioning your Cloud Service Mesh control plane. Changing CA is not supported.



## Configure managed Cloud Service Mesh to use CA Service

**Note:** Make sure to complete all the following steps before you [enable automatic management](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/provision-control-plane#enable_automatic_management).

  1. Verify that the `istio-system` namespace exists, or create it if it is missing:
         
         kubectl create ns istio-system
         

  2. Check if `asm-options` configmap exists in the `istio-system` namespace:
         
         kubectl get configmap/asm-options -n istio-system
         

  3. Create the configmap if it does not exist:
         
         kubectl create configmap -n istio-system asm-options
         

  4. Patch the configmap to add CAS configuration:
         
         kubectl patch configmap/asm-options -n istio-system --type merge \
           -p '{"data":{"ASM_OPTS": "CA=PRIVATECA;CAAddr=projects/CA_PROJECT_ID/locations/ca_region/caPools/CA_POOL"}}'
         

If a certificate template is needed, append the template ID to the CA Pool address using `:` as a separator:
         
         kubectl patch configmap/asm-options -n istio-system --type merge \
           -p '{"data":{"ASM_OPTS": "CA=PRIVATECA;CAAddr=projects/CA_PROJECT_ID/locations/ca_region/caPools/CA_POOL:projects/PROJECT_ID/locations/ca_region/certificateTemplates/CERT_TEMPLATE_ID"}}'
         




After completing the configuration steps, continue the installation of managed Cloud Service Mesh by [enabling automatic management](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/provision-control-plane#enable_automatic_management).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
