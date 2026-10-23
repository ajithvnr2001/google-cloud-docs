---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/updating-private-registry/
title: Update Config Sync using a private registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:34.055355+00:00
---

# Update Config Sync using a private registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/updating-private-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Update Config Sync using a private registry Stay organized with collections  Save and categorize content based on your preferences. 

Each version of Config Sync requires a specific set of versioned images to run. If you are using a private registry, you must pull, tag, and push these images to your private registry _before_ you can [install Config Sync components](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync) or [upgrade the Config Sync version](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#upgrade).

**Note:** A private registry is configured as part of the Google Distributed Cloud admin cluster setup process. Config Sync automatically detects when a private registry has been configured, and ensures the private registry is used by Config Sync. To learn more, see [Create an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/how-to/create-admin-cluster) in the Google Distributed Cloud documentation.

## Add images to a private registry

To push version-specific Config Sync images to a private registry, click the plus icon for the version that you want to use and complete the listed steps.

**Note:** Use a client from which you can pull from `gcr.io` and push to your private registry.

### 1.25.1

To add the images to a private registry, complete the following steps:

  1. Pull the Config Sync images: 
         
         docker pull gcr.io/config-management-release/admission-webhook:v1.25.1-rc.2
         docker pull gcr.io/config-management-release/gcenode-askpass-sidecar:v1.25.1-rc.2
         docker pull gcr.io/config-management-release/git-sync:v4.4.2-gke.35__linux_amd64
         docker pull gcr.io/config-management-release/helm-sync:v1.25.1-rc.2
         docker pull gcr.io/config-management-release/hydration-controller:v1.25.1-rc.2
         docker pull gcr.io/config-management-release/oci-sync:v1.25.1-rc.2
         docker pull gcr.io/config-management-release/otelcontribcol:v0.152.0-gke.16
         docker pull gcr.io/config-management-release/reconciler-manager:v1.25.1-rc.2
         docker pull gcr.io/config-management-release/reconciler:v1.25.1-rc.2
         docker pull gcr.io/config-management-release/resource-group-controller:v1.25.1-rc.2
         

  2. Create a variable for your private registry URL: 
         
         export PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL
         

Replace `PRIVATE_REGISTRY_URL` with your private registry URL. 
  3. Tag the images with your private registry URL: 
         
         docker tag gcr.io/config-management-release/admission-webhook:v1.25.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.25.1-rc.2
         docker tag gcr.io/config-management-release/gcenode-askpass-sidecar:v1.25.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.25.1-rc.2
         docker tag gcr.io/config-management-release/git-sync:v4.4.2-gke.35__linux_amd64 \
          ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.35__linux_amd64
         docker tag gcr.io/config-management-release/helm-sync:v1.25.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/helm-sync:v1.25.1-rc.2
         docker tag gcr.io/config-management-release/hydration-controller:v1.25.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.25.1-rc.2
         docker tag gcr.io/config-management-release/oci-sync:v1.25.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/oci-sync:v1.25.1-rc.2
         docker tag gcr.io/config-management-release/otelcontribcol:v0.152.0-gke.16 \
          ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.152.0-gke.16
         docker tag gcr.io/config-management-release/reconciler-manager:v1.25.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.25.1-rc.2
         docker tag gcr.io/config-management-release/reconciler:v1.25.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/reconciler:v1.25.1-rc.2
         docker tag gcr.io/config-management-release/resource-group-controller:v1.25.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.25.1-rc.2
         

  4. Push the tagged images to your private registry: 
         
         docker push ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.25.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.25.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.35__linux_amd64
         docker push ${PRIVATE_REGISTRY_URL}/helm-sync:v1.25.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.25.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/oci-sync:v1.25.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.152.0-gke.16
         docker push ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.25.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/reconciler:v1.25.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.25.1-rc.2
         




If you can pull the tagged images from your private registry, then the procedure was successful. 

### 1.25.0

To add the images to a private registry, complete the following steps:

  1. Pull the Config Sync images: 
         
         docker pull gcr.io/config-management-release/admission-webhook:v1.25.0-rc.1
         docker pull gcr.io/config-management-release/gcenode-askpass-sidecar:v1.25.0-rc.1
         docker pull gcr.io/config-management-release/git-sync:v4.4.2-gke.31__linux_amd64
         docker pull gcr.io/config-management-release/helm-sync:v1.25.0-rc.1
         docker pull gcr.io/config-management-release/hydration-controller:v1.25.0-rc.1
         docker pull gcr.io/config-management-release/oci-sync:v1.25.0-rc.1
         docker pull gcr.io/config-management-release/otelcontribcol:v0.152.0-gke.9
         docker pull gcr.io/config-management-release/reconciler-manager:v1.25.0-rc.1
         docker pull gcr.io/config-management-release/reconciler:v1.25.0-rc.1
         docker pull gcr.io/config-management-release/resource-group-controller:v1.25.0-rc.1
         

  2. Create a variable for your private registry URL: 
         
         export PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL
         

Replace `PRIVATE_REGISTRY_URL` with your private registry URL. 
  3. Tag the images with your private registry URL: 
         
         docker tag gcr.io/config-management-release/admission-webhook:v1.25.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.25.0-rc.1
         docker tag gcr.io/config-management-release/gcenode-askpass-sidecar:v1.25.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.25.0-rc.1
         docker tag gcr.io/config-management-release/git-sync:v4.4.2-gke.31__linux_amd64 \
          ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.31__linux_amd64
         docker tag gcr.io/config-management-release/helm-sync:v1.25.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/helm-sync:v1.25.0-rc.1
         docker tag gcr.io/config-management-release/hydration-controller:v1.25.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.25.0-rc.1
         docker tag gcr.io/config-management-release/oci-sync:v1.25.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/oci-sync:v1.25.0-rc.1
         docker tag gcr.io/config-management-release/otelcontribcol:v0.152.0-gke.9 \
          ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.152.0-gke.9
         docker tag gcr.io/config-management-release/reconciler-manager:v1.25.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.25.0-rc.1
         docker tag gcr.io/config-management-release/reconciler:v1.25.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/reconciler:v1.25.0-rc.1
         docker tag gcr.io/config-management-release/resource-group-controller:v1.25.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.25.0-rc.1
         

  4. Push the tagged images to your private registry: 
         
         docker push ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.25.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.25.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.31__linux_amd64
         docker push ${PRIVATE_REGISTRY_URL}/helm-sync:v1.25.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.25.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/oci-sync:v1.25.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.152.0-gke.9
         docker push ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.25.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/reconciler:v1.25.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.25.0-rc.1
         




If you can pull the tagged images from your private registry, then the procedure was successful. 

### 1.24.3

To add the images to a private registry, complete the following steps:

  1. Pull the Config Sync images: 
         
         docker pull gcr.io/config-management-release/admission-webhook:v1.24.3-rc.2
         docker pull gcr.io/config-management-release/gcenode-askpass-sidecar:v1.24.3-rc.2
         docker pull gcr.io/config-management-release/git-sync:v4.4.2-gke.28__linux_amd64
         docker pull gcr.io/config-management-release/helm-sync:v1.24.3-rc.2
         docker pull gcr.io/config-management-release/hydration-controller:v1.24.3-rc.2
         docker pull gcr.io/config-management-release/oci-sync:v1.24.3-rc.2
         docker pull gcr.io/config-management-release/otelcontribcol:v0.152.0-gke.7
         docker pull gcr.io/config-management-release/reconciler-manager:v1.24.3-rc.2
         docker pull gcr.io/config-management-release/reconciler:v1.24.3-rc.2
         docker pull gcr.io/config-management-release/resource-group-controller:v1.24.3-rc.2
         

  2. Create a variable for your private registry URL: 
         
         export PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL
         

Replace `PRIVATE_REGISTRY_URL` with your private registry URL. 
  3. Tag the images with your private registry URL: 
         
         docker tag gcr.io/config-management-release/admission-webhook:v1.24.3-rc.2 \
          ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.24.3-rc.2
         docker tag gcr.io/config-management-release/gcenode-askpass-sidecar:v1.24.3-rc.2 \
          ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.24.3-rc.2
         docker tag gcr.io/config-management-release/git-sync:v4.4.2-gke.28__linux_amd64 \
          ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.28__linux_amd64
         docker tag gcr.io/config-management-release/helm-sync:v1.24.3-rc.2 \
          ${PRIVATE_REGISTRY_URL}/helm-sync:v1.24.3-rc.2
         docker tag gcr.io/config-management-release/hydration-controller:v1.24.3-rc.2 \
          ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.24.3-rc.2
         docker tag gcr.io/config-management-release/oci-sync:v1.24.3-rc.2 \
          ${PRIVATE_REGISTRY_URL}/oci-sync:v1.24.3-rc.2
         docker tag gcr.io/config-management-release/otelcontribcol:v0.152.0-gke.7 \
          ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.152.0-gke.7
         docker tag gcr.io/config-management-release/reconciler-manager:v1.24.3-rc.2 \
          ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.24.3-rc.2
         docker tag gcr.io/config-management-release/reconciler:v1.24.3-rc.2 \
          ${PRIVATE_REGISTRY_URL}/reconciler:v1.24.3-rc.2
         docker tag gcr.io/config-management-release/resource-group-controller:v1.24.3-rc.2 \
          ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.24.3-rc.2
         

  4. Push the tagged images to your private registry: 
         
         docker push ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.24.3-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.24.3-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.28__linux_amd64
         docker push ${PRIVATE_REGISTRY_URL}/helm-sync:v1.24.3-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.24.3-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/oci-sync:v1.24.3-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.152.0-gke.7
         docker push ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.24.3-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/reconciler:v1.24.3-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.24.3-rc.2
         




If you can pull the tagged images from your private registry, then the procedure was successful. 

### 1.24.2

To add the images to a private registry, complete the following steps:

  1. Pull the Config Sync images: 
         
         docker pull gcr.io/config-management-release/admission-webhook:v1.24.2-rc.2
         docker pull gcr.io/config-management-release/gcenode-askpass-sidecar:v1.24.2-rc.2
         docker pull gcr.io/config-management-release/git-sync:v4.4.2-gke.28__linux_amd64
         docker pull gcr.io/config-management-release/helm-sync:v1.24.2-rc.2
         docker pull gcr.io/config-management-release/hydration-controller:v1.24.2-rc.2
         docker pull gcr.io/config-management-release/oci-sync:v1.24.2-rc.2
         docker pull gcr.io/config-management-release/otelcontribcol:v0.152.0-gke.4
         docker pull gcr.io/config-management-release/reconciler-manager:v1.24.2-rc.2
         docker pull gcr.io/config-management-release/reconciler:v1.24.2-rc.2
         docker pull gcr.io/config-management-release/resource-group-controller:v1.24.2-rc.2
         

  2. Create a variable for your private registry URL: 
         
         export PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL
         

Replace `PRIVATE_REGISTRY_URL` with your private registry URL. 
  3. Tag the images with your private registry URL: 
         
         docker tag gcr.io/config-management-release/admission-webhook:v1.24.2-rc.2 \
          ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.24.2-rc.2
         docker tag gcr.io/config-management-release/gcenode-askpass-sidecar:v1.24.2-rc.2 \
          ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.24.2-rc.2
         docker tag gcr.io/config-management-release/git-sync:v4.4.2-gke.28__linux_amd64 \
          ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.28__linux_amd64
         docker tag gcr.io/config-management-release/helm-sync:v1.24.2-rc.2 \
          ${PRIVATE_REGISTRY_URL}/helm-sync:v1.24.2-rc.2
         docker tag gcr.io/config-management-release/hydration-controller:v1.24.2-rc.2 \
          ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.24.2-rc.2
         docker tag gcr.io/config-management-release/oci-sync:v1.24.2-rc.2 \
          ${PRIVATE_REGISTRY_URL}/oci-sync:v1.24.2-rc.2
         docker tag gcr.io/config-management-release/otelcontribcol:v0.152.0-gke.4 \
          ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.152.0-gke.4
         docker tag gcr.io/config-management-release/reconciler-manager:v1.24.2-rc.2 \
          ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.24.2-rc.2
         docker tag gcr.io/config-management-release/reconciler:v1.24.2-rc.2 \
          ${PRIVATE_REGISTRY_URL}/reconciler:v1.24.2-rc.2
         docker tag gcr.io/config-management-release/resource-group-controller:v1.24.2-rc.2 \
          ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.24.2-rc.2
         

  4. Push the tagged images to your private registry: 
         
         docker push ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.24.2-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.24.2-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.28__linux_amd64
         docker push ${PRIVATE_REGISTRY_URL}/helm-sync:v1.24.2-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.24.2-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/oci-sync:v1.24.2-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.152.0-gke.4
         docker push ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.24.2-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/reconciler:v1.24.2-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.24.2-rc.2
         




If you can pull the tagged images from your private registry, then the procedure was successful. 

### 1.24.1

To add the images to a private registry, complete the following steps:

  1. Pull the Config Sync images: 
         
         docker pull gcr.io/config-management-release/admission-webhook:v1.24.1-rc.1
         docker pull gcr.io/config-management-release/gcenode-askpass-sidecar:v1.24.1-rc.1
         docker pull gcr.io/config-management-release/git-sync:v4.4.2-gke.24__linux_amd64
         docker pull gcr.io/config-management-release/helm-sync:v1.24.1-rc.1
         docker pull gcr.io/config-management-release/hydration-controller:v1.24.1-rc.1
         docker pull gcr.io/config-management-release/oci-sync:v1.24.1-rc.1
         docker pull gcr.io/config-management-release/otelcontribcol:v0.150.0-gke.5
         docker pull gcr.io/config-management-release/reconciler-manager:v1.24.1-rc.1
         docker pull gcr.io/config-management-release/reconciler:v1.24.1-rc.1
         docker pull gcr.io/config-management-release/resource-group-controller:v1.24.1-rc.1
         

  2. Create a variable for your private registry URL: 
         
         export PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL
         

Replace `PRIVATE_REGISTRY_URL` with your private registry URL. 
  3. Tag the images with your private registry URL: 
         
         docker tag gcr.io/config-management-release/admission-webhook:v1.24.1-rc.1 \
          ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.24.1-rc.1
         docker tag gcr.io/config-management-release/gcenode-askpass-sidecar:v1.24.1-rc.1 \
          ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.24.1-rc.1
         docker tag gcr.io/config-management-release/git-sync:v4.4.2-gke.24__linux_amd64 \
          ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.24__linux_amd64
         docker tag gcr.io/config-management-release/helm-sync:v1.24.1-rc.1 \
          ${PRIVATE_REGISTRY_URL}/helm-sync:v1.24.1-rc.1
         docker tag gcr.io/config-management-release/hydration-controller:v1.24.1-rc.1 \
          ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.24.1-rc.1
         docker tag gcr.io/config-management-release/oci-sync:v1.24.1-rc.1 \
          ${PRIVATE_REGISTRY_URL}/oci-sync:v1.24.1-rc.1
         docker tag gcr.io/config-management-release/otelcontribcol:v0.150.0-gke.5 \
          ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.150.0-gke.5
         docker tag gcr.io/config-management-release/reconciler-manager:v1.24.1-rc.1 \
          ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.24.1-rc.1
         docker tag gcr.io/config-management-release/reconciler:v1.24.1-rc.1 \
          ${PRIVATE_REGISTRY_URL}/reconciler:v1.24.1-rc.1
         docker tag gcr.io/config-management-release/resource-group-controller:v1.24.1-rc.1 \
          ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.24.1-rc.1
         

  4. Push the tagged images to your private registry: 
         
         docker push ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.24.1-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.24.1-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.24__linux_amd64
         docker push ${PRIVATE_REGISTRY_URL}/helm-sync:v1.24.1-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.24.1-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/oci-sync:v1.24.1-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.150.0-gke.5
         docker push ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.24.1-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/reconciler:v1.24.1-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.24.1-rc.1
         




If you can pull the tagged images from your private registry, then the procedure was successful. 

### 1.24.0

To add the images to a private registry, complete the following steps:

  1. Pull the Config Sync images: 
         
         docker pull gcr.io/config-management-release/admission-webhook:v1.24.0-rc.4
         docker pull gcr.io/config-management-release/gcenode-askpass-sidecar:v1.24.0-rc.4
         docker pull gcr.io/config-management-release/git-sync:v4.4.2-gke.19__linux_amd64
         docker pull gcr.io/config-management-release/helm-sync:v1.24.0-rc.4
         docker pull gcr.io/config-management-release/hydration-controller:v1.24.0-rc.4
         docker pull gcr.io/config-management-release/oci-sync:v1.24.0-rc.4
         docker pull gcr.io/config-management-release/otelcontribcol:v0.133.0-gke.11
         docker pull gcr.io/config-management-release/reconciler-manager:v1.24.0-rc.4
         docker pull gcr.io/config-management-release/reconciler:v1.24.0-rc.4
         docker pull gcr.io/config-management-release/resource-group-controller:v1.24.0-rc.4
         

  2. Create a variable for your private registry URL: 
         
         export PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL
         

Replace `PRIVATE_REGISTRY_URL` with your private registry URL. 
  3. Tag the images with your private registry URL: 
         
         docker tag gcr.io/config-management-release/admission-webhook:v1.24.0-rc.4 \
          ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.24.0-rc.4
         docker tag gcr.io/config-management-release/gcenode-askpass-sidecar:v1.24.0-rc.4 \
          ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.24.0-rc.4
         docker tag gcr.io/config-management-release/git-sync:v4.4.2-gke.19__linux_amd64 \
          ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.19__linux_amd64
         docker tag gcr.io/config-management-release/helm-sync:v1.24.0-rc.4 \
          ${PRIVATE_REGISTRY_URL}/helm-sync:v1.24.0-rc.4
         docker tag gcr.io/config-management-release/hydration-controller:v1.24.0-rc.4 \
          ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.24.0-rc.4
         docker tag gcr.io/config-management-release/oci-sync:v1.24.0-rc.4 \
          ${PRIVATE_REGISTRY_URL}/oci-sync:v1.24.0-rc.4
         docker tag gcr.io/config-management-release/otelcontribcol:v0.133.0-gke.11 \
          ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.133.0-gke.11
         docker tag gcr.io/config-management-release/reconciler-manager:v1.24.0-rc.4 \
          ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.24.0-rc.4
         docker tag gcr.io/config-management-release/reconciler:v1.24.0-rc.4 \
          ${PRIVATE_REGISTRY_URL}/reconciler:v1.24.0-rc.4
         docker tag gcr.io/config-management-release/resource-group-controller:v1.24.0-rc.4 \
          ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.24.0-rc.4
         

  4. Push the tagged images to your private registry: 
         
         docker push ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.24.0-rc.4
         docker push ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.24.0-rc.4
         docker push ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.19__linux_amd64
         docker push ${PRIVATE_REGISTRY_URL}/helm-sync:v1.24.0-rc.4
         docker push ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.24.0-rc.4
         docker push ${PRIVATE_REGISTRY_URL}/oci-sync:v1.24.0-rc.4
         docker push ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.133.0-gke.11
         docker push ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.24.0-rc.4
         docker push ${PRIVATE_REGISTRY_URL}/reconciler:v1.24.0-rc.4
         docker push ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.24.0-rc.4
         




If you can pull the tagged images from your private registry, then the procedure was successful. 

### 1.23.3

To add the images to a private registry, complete the following steps:

  1. Pull the Config Sync images: 
         
         docker pull gcr.io/config-management-release/admission-webhook:v1.23.3-rc.1
         docker pull gcr.io/config-management-release/gcenode-askpass-sidecar:v1.23.3-rc.1
         docker pull gcr.io/config-management-release/git-sync:v4.4.2-gke.17__linux_amd64
         docker pull gcr.io/config-management-release/helm-sync:v1.23.3-rc.1
         docker pull gcr.io/config-management-release/hydration-controller:v1.23.3-rc.1
         docker pull gcr.io/config-management-release/oci-sync:v1.23.3-rc.1
         docker pull gcr.io/config-management-release/otelcontribcol:v0.133.0-gke.4
         docker pull gcr.io/config-management-release/reconciler-manager:v1.23.3-rc.1
         docker pull gcr.io/config-management-release/reconciler:v1.23.3-rc.1
         docker pull gcr.io/config-management-release/resource-group-controller:v1.23.3-rc.1
         

  2. Create a variable for your private registry URL: 
         
         export PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL
         

Replace `PRIVATE_REGISTRY_URL` with your private registry URL. 
  3. Tag the images with your private registry URL: 
         
         docker tag gcr.io/config-management-release/admission-webhook:v1.23.3-rc.1 \
          ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.23.3-rc.1
         docker tag gcr.io/config-management-release/gcenode-askpass-sidecar:v1.23.3-rc.1 \
          ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.23.3-rc.1
         docker tag gcr.io/config-management-release/git-sync:v4.4.2-gke.17__linux_amd64 \
          ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.17__linux_amd64
         docker tag gcr.io/config-management-release/helm-sync:v1.23.3-rc.1 \
          ${PRIVATE_REGISTRY_URL}/helm-sync:v1.23.3-rc.1
         docker tag gcr.io/config-management-release/hydration-controller:v1.23.3-rc.1 \
          ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.23.3-rc.1
         docker tag gcr.io/config-management-release/oci-sync:v1.23.3-rc.1 \
          ${PRIVATE_REGISTRY_URL}/oci-sync:v1.23.3-rc.1
         docker tag gcr.io/config-management-release/otelcontribcol:v0.133.0-gke.4 \
          ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.133.0-gke.4
         docker tag gcr.io/config-management-release/reconciler-manager:v1.23.3-rc.1 \
          ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.23.3-rc.1
         docker tag gcr.io/config-management-release/reconciler:v1.23.3-rc.1 \
          ${PRIVATE_REGISTRY_URL}/reconciler:v1.23.3-rc.1
         docker tag gcr.io/config-management-release/resource-group-controller:v1.23.3-rc.1 \
          ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.23.3-rc.1
         

  4. Push the tagged images to your private registry: 
         
         docker push ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.23.3-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.23.3-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.17__linux_amd64
         docker push ${PRIVATE_REGISTRY_URL}/helm-sync:v1.23.3-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.23.3-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/oci-sync:v1.23.3-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.133.0-gke.4
         docker push ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.23.3-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/reconciler:v1.23.3-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.23.3-rc.1
         




If you can pull the tagged images from your private registry, then the procedure was successful. 

### 1.23.2

To add the images to a private registry, complete the following steps:

  1. Pull the Config Sync images: 
         
         docker pull gcr.io/config-management-release/admission-webhook:v1.23.2-rc.1
         docker pull gcr.io/config-management-release/gcenode-askpass-sidecar:v1.23.2-rc.1
         docker pull gcr.io/config-management-release/git-sync:v4.4.2-gke.14__linux_amd64
         docker pull gcr.io/config-management-release/helm-sync:v1.23.2-rc.1
         docker pull gcr.io/config-management-release/hydration-controller:v1.23.2-rc.1
         docker pull gcr.io/config-management-release/oci-sync:v1.23.2-rc.1
         docker pull gcr.io/config-management-release/otelcontribcol:v0.127.0-gke.6
         docker pull gcr.io/config-management-release/reconciler-manager:v1.23.2-rc.1
         docker pull gcr.io/config-management-release/reconciler:v1.23.2-rc.1
         docker pull gcr.io/config-management-release/resource-group-controller:v1.23.2-rc.1
         

  2. Create a variable for your private registry URL: 
         
         export PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL
         

Replace `PRIVATE_REGISTRY_URL` with your private registry URL. 
  3. Tag the images with your private registry URL: 
         
         docker tag gcr.io/config-management-release/admission-webhook:v1.23.2-rc.1 \
          ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.23.2-rc.1
         docker tag gcr.io/config-management-release/gcenode-askpass-sidecar:v1.23.2-rc.1 \
          ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.23.2-rc.1
         docker tag gcr.io/config-management-release/git-sync:v4.4.2-gke.14__linux_amd64 \
          ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.14__linux_amd64
         docker tag gcr.io/config-management-release/helm-sync:v1.23.2-rc.1 \
          ${PRIVATE_REGISTRY_URL}/helm-sync:v1.23.2-rc.1
         docker tag gcr.io/config-management-release/hydration-controller:v1.23.2-rc.1 \
          ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.23.2-rc.1
         docker tag gcr.io/config-management-release/oci-sync:v1.23.2-rc.1 \
          ${PRIVATE_REGISTRY_URL}/oci-sync:v1.23.2-rc.1
         docker tag gcr.io/config-management-release/otelcontribcol:v0.127.0-gke.6 \
          ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.127.0-gke.6
         docker tag gcr.io/config-management-release/reconciler-manager:v1.23.2-rc.1 \
          ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.23.2-rc.1
         docker tag gcr.io/config-management-release/reconciler:v1.23.2-rc.1 \
          ${PRIVATE_REGISTRY_URL}/reconciler:v1.23.2-rc.1
         docker tag gcr.io/config-management-release/resource-group-controller:v1.23.2-rc.1 \
          ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.23.2-rc.1
         

  4. Push the tagged images to your private registry: 
         
         docker push ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.23.2-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.23.2-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.14__linux_amd64
         docker push ${PRIVATE_REGISTRY_URL}/helm-sync:v1.23.2-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.23.2-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/oci-sync:v1.23.2-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.127.0-gke.6
         docker push ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.23.2-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/reconciler:v1.23.2-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.23.2-rc.1
         




If you can pull the tagged images from your private registry, then the procedure was successful. 

### 1.23.1

To add the images to a private registry, complete the following steps:

  1. Pull the Config Sync images: 
         
         docker pull gcr.io/config-management-release/admission-webhook:v1.23.1-rc.2
         docker pull gcr.io/config-management-release/gcenode-askpass-sidecar:v1.23.1-rc.2
         docker pull gcr.io/config-management-release/git-sync:v4.4.2-gke.10__linux_amd64
         docker pull gcr.io/config-management-release/helm-sync:v1.23.1-rc.2
         docker pull gcr.io/config-management-release/hydration-controller:v1.23.1-rc.2
         docker pull gcr.io/config-management-release/oci-sync:v1.23.1-rc.2
         docker pull gcr.io/config-management-release/otelcontribcol:v0.127.0-gke.4
         docker pull gcr.io/config-management-release/reconciler-manager:v1.23.1-rc.2
         docker pull gcr.io/config-management-release/reconciler:v1.23.1-rc.2
         docker pull gcr.io/config-management-release/resource-group-controller:v1.23.1-rc.2
         

  2. Create a variable for your private registry URL: 
         
         export PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL
         

Replace `PRIVATE_REGISTRY_URL` with your private registry URL. 
  3. Tag the images with your private registry URL: 
         
         docker tag gcr.io/config-management-release/admission-webhook:v1.23.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.23.1-rc.2
         docker tag gcr.io/config-management-release/gcenode-askpass-sidecar:v1.23.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.23.1-rc.2
         docker tag gcr.io/config-management-release/git-sync:v4.4.2-gke.10__linux_amd64 \
          ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.10__linux_amd64
         docker tag gcr.io/config-management-release/helm-sync:v1.23.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/helm-sync:v1.23.1-rc.2
         docker tag gcr.io/config-management-release/hydration-controller:v1.23.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.23.1-rc.2
         docker tag gcr.io/config-management-release/oci-sync:v1.23.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/oci-sync:v1.23.1-rc.2
         docker tag gcr.io/config-management-release/otelcontribcol:v0.127.0-gke.4 \
          ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.127.0-gke.4
         docker tag gcr.io/config-management-release/reconciler-manager:v1.23.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.23.1-rc.2
         docker tag gcr.io/config-management-release/reconciler:v1.23.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/reconciler:v1.23.1-rc.2
         docker tag gcr.io/config-management-release/resource-group-controller:v1.23.1-rc.2 \
          ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.23.1-rc.2
         

  4. Push the tagged images to your private registry: 
         
         docker push ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.23.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.23.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.10__linux_amd64
         docker push ${PRIVATE_REGISTRY_URL}/helm-sync:v1.23.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.23.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/oci-sync:v1.23.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.127.0-gke.4
         docker push ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.23.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/reconciler:v1.23.1-rc.2
         docker push ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.23.1-rc.2
         




If you can pull the tagged images from your private registry, then the procedure was successful. 

### 1.23.0

To add the images to a private registry, complete the following steps:

  1. Pull the Config Sync images: 
         
         docker pull gcr.io/config-management-release/admission-webhook:v1.23.0-rc.1
         docker pull gcr.io/config-management-release/gcenode-askpass-sidecar:v1.23.0-rc.1
         docker pull gcr.io/config-management-release/git-sync:v4.4.2-gke.5__linux_amd64
         docker pull gcr.io/config-management-release/helm-sync:v1.23.0-rc.1
         docker pull gcr.io/config-management-release/hydration-controller:v1.23.0-rc.1
         docker pull gcr.io/config-management-release/oci-sync:v1.23.0-rc.1
         docker pull gcr.io/config-management-release/otelcontribcol:v0.119.0-gke.2
         docker pull gcr.io/config-management-release/reconciler-manager:v1.23.0-rc.1
         docker pull gcr.io/config-management-release/reconciler:v1.23.0-rc.1
         docker pull gcr.io/config-management-release/resource-group-controller:v1.23.0-rc.1
         

  2. Create a variable for your private registry URL: 
         
         export PRIVATE_REGISTRY_URL=PRIVATE_REGISTRY_URL
         

Replace `PRIVATE_REGISTRY_URL` with your private registry URL. 
  3. Tag the images with your private registry URL: 
         
         docker tag gcr.io/config-management-release/admission-webhook:v1.23.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.23.0-rc.1
         docker tag gcr.io/config-management-release/gcenode-askpass-sidecar:v1.23.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.23.0-rc.1
         docker tag gcr.io/config-management-release/git-sync:v4.4.2-gke.5__linux_amd64 \
          ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.5__linux_amd64
         docker tag gcr.io/config-management-release/helm-sync:v1.23.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/helm-sync:v1.23.0-rc.1
         docker tag gcr.io/config-management-release/hydration-controller:v1.23.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.23.0-rc.1
         docker tag gcr.io/config-management-release/oci-sync:v1.23.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/oci-sync:v1.23.0-rc.1
         docker tag gcr.io/config-management-release/otelcontribcol:v0.119.0-gke.2 \
          ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.119.0-gke.2
         docker tag gcr.io/config-management-release/reconciler-manager:v1.23.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.23.0-rc.1
         docker tag gcr.io/config-management-release/reconciler:v1.23.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/reconciler:v1.23.0-rc.1
         docker tag gcr.io/config-management-release/resource-group-controller:v1.23.0-rc.1 \
          ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.23.0-rc.1
         

  4. Push the tagged images to your private registry: 
         
         docker push ${PRIVATE_REGISTRY_URL}/admission-webhook:v1.23.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/gcenode-askpass-sidecar:v1.23.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/git-sync:v4.4.2-gke.5__linux_amd64
         docker push ${PRIVATE_REGISTRY_URL}/helm-sync:v1.23.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/hydration-controller:v1.23.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/oci-sync:v1.23.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/otelcontribcol:v0.119.0-gke.2
         docker push ${PRIVATE_REGISTRY_URL}/reconciler-manager:v1.23.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/reconciler:v1.23.0-rc.1
         docker push ${PRIVATE_REGISTRY_URL}/resource-group-controller:v1.23.0-rc.1
         




If you can pull the tagged images from your private registry, then the procedure was successful. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
