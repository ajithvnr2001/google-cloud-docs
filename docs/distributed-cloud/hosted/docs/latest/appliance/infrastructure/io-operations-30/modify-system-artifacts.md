---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/modify-system-artifacts/
title: Modify system artifacts \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:58.316791+00:00
---

# Modify system artifacts  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/modify-system-artifacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Modify system artifacts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to modify your system artifacts in Google Distributed Cloud (GDC) air-gapped appliance.

Modify system artifacts in GDC to manage and refine your deployment,

## Before you begin

To modify system artifacts, you must get diagnostic access and have access to the necessary identity and access roles:

  * Diagnostic access is a privileged access mode required to securely support a customer when they encounter an issue. You must create a ticket to have this access granted.
  * System Artifact Registry Debugger: has read and write access to all Harbor resources. Ask your Security Admin to grant you the System Artifact Registry Debugger (`sar-debugger`) cluster role.
  * System Artifact Registry harbor-system secret Debugger: has debugger access in the `harbor-system` namespace. Ask your Security Admin to grant you the System Artifact Registry harbor-system secret Debugger (`sar-harbor-system-secret-debugger`) role.



## Upload Docker images

To modify system artifacts, you must upload new Docker images. The upload method depends on which of the following two registries you push your container images to:

  * Upload container images to the Artifact Registry in the bootstrap machine.
  * Upload container images to the Artifact Registry in the org infrastructure cluster.



The following sections show the upload instructions for the two registry types.

### Upload container image in the bootstrap machine

To upload container images to the Artifact Registry in the bootstrap machine, complete the following steps:

  1. Ensure you have the modified Docker image with the breaking issues fixed.

  2. Transfer the new image to the bootstrap node in your GDC environment.

  3. Sign in to the bootstrap node.

  4. Locate the address of the Artifact Registry in the bootstrap machine at bootstrap time and set it as the `REGISTRY_IP` environment variable:
         
         REGISTRY=$(kubectl get harborcluster harbor -n harbor-system -o=jsonpath='{.spec.externalURL}')
         
         REGISTRY_IP=${REGISTRY#https://}
         

  5. Retrieve the credential for accessing the Artifact Registry. Retrieve the administrator account and password:
         
         ADMIN_PASS=$(kubectl -n harbor-system get secret harbor-admin \
             -o jsonpath="{.data.secret}" | base64 -d)
         

  6. Sign in to the Artifact Registry:
         
         docker login $REGISTRY_IP -u admin -p $ADMIN_PASS
         

A `Login Succeeded` message prints to verify a successful login to the Artifact Registry.

  7. Tag the new image:
         
         docker image tag CONTAINER_IMAGE_URL \
             $REGISTRY_IP/PROJECT_NAME/IMAGE_NAME:TAG
         

Replace the following:

     * `CONTAINER_IMAGE_URL`: the local container image URL, such as `gcr.io/repository/image:tag`.
     * `PROJECT_NAME`: the Artifact Registry project name.
     * `IMAGE_NAME`: the container image name.
     * `TAG`: the container image tag.
  8. Push the new image to the Artifact Registry:
         
         docker image push $REGISTRY_IP/PROJECT_NAME/IMAGE_NAME:TAG
         




### Upload container image to the org infrastructure cluster

To upload container images to the Artifact Registry on a org infrastructure cluster, complete the following steps:

  1. Ensure you have the modified Docker image with the breaking issues fixed.

  2. Transfer the new image to a node that has root access with a root `kubeconfig` file to the org infrastructure cluster in your air-gapped environment.

  3. Export the org infrastructure cluster `kubeconfig` path as an environment variable:
         
         export ORG_INFRA_KUBECONFIG=KUBECONFIG_FILE_PATH
         

Replace `KUBECONFIG_FILE_PATH` with the path to the `kubeconfig` file.

  4. Locate the in-cluster Artifact Registry address and set it as the `REGISTRY_IP` environment variable:
         
         REGISTRY=$(kubectl --kubeconfig $ORG_INFRA_KUBECONFIG get harborcluster /
         harbor -n harbor-system -o=jsonpath='{.spec.externalURL}')
         
         REGISTRY_IP=${REGISTRY#https://}
         

  5. Ensure the `REGISTRY_IP` contains a valid URL, such as `10.200.0.36:10443`:
         
         echo ${REGISTRY_IP}
         

  6. Check whether the certificate authority (CA) certificate exists:
         
         ls -al /etc/docker/certs.d/${REGISTRY_IP}/ca.crt
         

If the certificate does not exist, create and configure it:
         
         mkdir -p /etc/docker/certs.d/${REGISTRY_IP}/
         
         chmod 755  /etc/docker/certs.d/${REGISTRY_IP}/
         
         echo $(kubectl get secret harbor-cert-secret -n istio-system -o jsonpath='{.data.ca\.crt}' --kubeconfig $ORG_INFRA_KUBECONFIG) | openssl base64 -A -d >  /etc/docker/certs.d/${REGISTRY_IP}/ca.crt
         
         chmod 755 /etc/docker/certs.d/${REGISTRY_IP}/ca.crt
         

  7. Retrieve the credential for accessing the Artifact Registry. Use the following command to retrieve the administrator account and password:
         
         ADMIN_PASS=$(kubectl --kubeconfig $ORG_INFRA_KUBECONFIG \
             -n harbor-system get secret harbor-admin \
             -o jsonpath="{.data.secret}" | base64 -d)
         

  8. Sign in to the Artifact Registry:
         
         docker login $REGISTRY_IP -u admin -p $ADMIN_PASS
         

A `Login Succeeded` message prints to verify a successful login to the Artifact Registry.

  9. Tag the new image:
         
         docker image tag CONTAINER_IMAGE_URL \
             $REGISTRY_IP/PROJECT_NAME/IMAGE_NAME:TAG
         

Replace the following:

     * `CONTAINER_IMAGE_URL`: the local container image URL, such as `gcr.io/repository/image:tag`.
     * `PROJECT_NAME`: the Artifact Registry project name.
     * `IMAGE_NAME`: the container image name.
     * `TAG`: the container image tag.
  10. Push the new image to the Artifact Registry:
         
         docker image push $REGISTRY_IP/PROJECT_NAME/IMAGE_NAME:TAG
         




## Modify system artifacts

Use the `gdcloud artifacts` commands to modify system artifacts in GDC. Update, customize, and secure your deployment by performing actions like replacing software packages, adjusting configurations, and applying patches.

Perform the following actions:

  * Manage `apt` packages.
  * Build and extract images from OCI packages.
  * List available versions of the root OCI image.
  * Patch existing packages.
  * Pull and push OCI packages to and from a registry.
  * Display the structure of an OCI bundle.
  * Unpack OCI bundles.



For more information, see [`gdcloud artifacts`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-artifacts).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
