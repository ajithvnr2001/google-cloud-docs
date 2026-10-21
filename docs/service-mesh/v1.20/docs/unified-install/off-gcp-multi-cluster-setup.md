---
url: https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/off-gcp-multi-cluster-setup/
title: Set up a multi-cluster mesh outside Google Cloud \u00a0|\u00a0 Cloud Service Mesh v1.20 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:32.347948+00:00
---

# Set up a multi-cluster mesh outside Google Cloud  |  Cloud Service Mesh v1.20  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/off-gcp-multi-cluster-setup/

You are viewing archived v1.20 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.20 ](https://docs.cloud.google.com/service-mesh/v1.20/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.20/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a multi-cluster mesh outside Google Cloud

This guide explains how to set up a multi-cluster mesh for the following platforms:

  * Google Distributed Cloud
  * Google Distributed Cloud
  * GKE on Azure
  * GKE on AWS
  * Attached clusters, including Amazon EKS clusters and Microsoft AKS clusters



This guide shows how to set up two clusters, but you can extend this process to incorporate any number of clusters into your mesh.

**Platform note:** The `asmcli create-mesh` command that you use to enable endpoint discovery requires all the clusters to be on the same platform. Currently, `asmcli create-mesh` only supports hybrid mesh in preview. 

## Before you begin

This guide assumes you installed Cloud Service Mesh using [`asmcli install`](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/asmcli-overview). You need `asmcli` and the configuration package that `asmcli` downloads to the directory that you specified in `--output_dir` when you ran `asmcli install`. If need to get set up, follow the steps in [Install dependent tools and validate cluster](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-dependent-tools) to:

  * [Install required tools](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-dependent-tools)
  * [Download `asmcli`](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-dependent-tools#download_asmcli)
  * [Grant cluster admin permissions](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-dependent-tools#grant_cluster_admin_permissions)
  * [Validate your project and cluster](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/install-dependent-tools#validate_project_and_cluster)



You need access to the kubeconfig files for all the clusters that you are setting up in the mesh.

**Warning:** Only use kubeconfig files from trusted sources. Using a specially-crafted kubeconfig file could result in malicious code execution or file exposure. If you must use an untrusted kubeconfig file, inspect it carefully first, much as you would a shell script.

### Set up environment variables and placeholders

You need the following environment variables when you install the east-west gateway.

  1. Create an environment variable for the project number. In the following command, replace FLEET_PROJECT_ID with the the project ID of the [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project).
         
         export PROJECT_NUMBER=$(gcloud projects describe FLEET_PROJECT_ID \
         --format="value(projectNumber)")
         

  2. Create an environment variable for the mesh identifier.
         
         export MESH_ID="proj-${PROJECT_NUMBER}"
         

  3. Create environment variables for the cluster names in the format that `asmcli` requires.
         
         export CLUSTER_1="cn-FLEET_PROJECT_ID-global-CLUSTER_NAME_1"
         export CLUSTER_2="cn-FLEET_PROJECT_ID-global-CLUSTER_NAME_2"
         

  4. Get the context name for the clusters by using the values under the `NAME` column in the output of this command:
         
         kubectl config get-contexts

  5. Set the environment variables to the cluster context names, which this guide uses in many steps later:
         
         export CTX_1=CLUSTER1_CONTEXT_NAME
         export CTX_2=CLUSTER2_CONTEXT_NAME
         




## Install the east-west gateway

In the following commands:

  * Replace `CLUSTER_NAME_1` and `CLUSTER_NAME_2` with the names of your clusters.

  * Replace `PATH_TO_KUBECONFIG_1` and `PATH_TO_KUBECONFIG_2` with the kubeconfig files for your clusters.




### Anthos Clusters

### Mesh CA or CA Service

  1. Install a gateway in cluster1 that is dedicated to [east-west traffic](https://en.wikipedia.org/wiki/East-west_traffic) to `$CLUSTER_2`. By default, this gateway will be public on the Internet. Production systems might require additional access restrictions, for example firewall rules, to prevent external attacks.

**Note:** If you installed Cloud Service Mesh using different values for `--network_id`, then you should pass the same values into `gen-eastwest-gateway.sh` with the `--network` flag.
         
         asm/istio/expansion/gen-eastwest-gateway.sh \
             --mesh ${MESH_ID}  \
             --cluster ${CLUSTER_1}  \
             --network default \
             --revision asm-1311-19 | \
             ./istioctl --kubeconfig=PATH_TO_KUBECONFIG_1 \
             install -y --set spec.values.global.pilotCertProvider=kubernetes -f -
         

  2. Install a gateway in `$CLUSTER_2` that is dedicated to east-west traffic for `$CLUSTER_1`.
         
         asm/istio/expansion/gen-eastwest-gateway.sh \
             --mesh ${MESH_ID}  \
             --cluster ${CLUSTER_2}  \
             --network default \
             --revision asm-1311-19 | \
             ./istioctl --kubeconfig=PATH_TO_KUBECONFIG_2 \
             install -y --set spec.values.global.pilotCertProvider=kubernetes -f -
         




### Istio CA

  1. Install a gateway in cluster1 that is dedicated to [east-west traffic](https://en.wikipedia.org/wiki/East-west_traffic) to `$CLUSTER_2`. By default, this gateway will be public on the Internet. Production systems might require additional access restrictions, for example firewall rules, to prevent external attacks.

**Note:** If you installed Cloud Service Mesh using different values for `--network_id`, then you should pass the same values into `gen-eastwest-gateway.sh` with the `--network` flag.
         
         asm/istio/expansion/gen-eastwest-gateway.sh \
             --mesh ${MESH_ID}  \
             --cluster ${CLUSTER_1}  \
             --network default \
             --revision asm-1311-19 | \
             ./istioctl --kubeconfig=PATH_TO_KUBECONFIG_1 \
             install -y --set spec.values.global.pilotCertProvider=istiod -f -
         

  2. Install a gateway in `$CLUSTER_2` that is dedicated to east-west traffic for `$CLUSTER_1`.
         
         asm/istio/expansion/gen-eastwest-gateway.sh \
             --mesh ${MESH_ID}  \
             --cluster ${CLUSTER_2}  \
             --network default \
             --revision asm-1311-19 | \
             ./istioctl --kubeconfig=PATH_TO_KUBECONFIG_2 \
             install -y --set spec.values.global.pilotCertProvider=istiod -f -
         




### Azure, AWS, & Attached

### Mesh CA

  1. Install a gateway in cluster1 that is dedicated to [east-west traffic](https://en.wikipedia.org/wiki/East-west_traffic) to `$CLUSTER_2`. By default, this gateway will be public on the Internet. Production systems might require additional access restrictions, for example firewall rules, to prevent external attacks.

**Note:** If you installed Cloud Service Mesh using different values for `--network_id`, then you should pass the same values into `gen-eastwest-gateway.sh` with the `--network` flag.
         
         asm/istio/expansion/gen-eastwest-gateway.sh \
             --mesh ${MESH_ID}  \
             --cluster ${CLUSTER_1}  \
             --network default \
             --revision asm-1311-19 | \
             ./istioctl --kubeconfig=PATH_TO_KUBECONFIG_1 \
             install -y --set spec.values.global.pilotCertProvider=istiod -f -
         

  2. Install a gateway in `$CLUSTER_2` that is dedicated to east-west traffic for `$CLUSTER_1`.
         
         asm/istio/expansion/gen-eastwest-gateway.sh \
             --mesh ${MESH_ID}  \
             --cluster ${CLUSTER_2}  \
             --network default \
             --revision asm-1311-19 | \
             ./istioctl --kubeconfig=PATH_TO_KUBECONFIG_2 \
             install -y --set spec.values.global.pilotCertProvider=istiod -f -
         




### Istio CA

  1. Install a gateway in cluster1 that is dedicated to [east-west traffic](https://en.wikipedia.org/wiki/East-west_traffic) to `$CLUSTER_2`. By default, this gateway will be public on the Internet. Production systems might require additional access restrictions, for example firewall rules, to prevent external attacks.

**Note:** If you installed Cloud Service Mesh using different values for `--network_id`, then you should pass the same values into `gen-eastwest-gateway.sh` with the `--network` flag.
         
         asm/istio/expansion/gen-eastwest-gateway.sh \
             --mesh ${MESH_ID}  \
             --cluster ${CLUSTER_1}  \
             --network default \
             --revision asm-1311-19 | \
             ./istioctl --kubeconfig=PATH_TO_KUBECONFIG_1 \
             install -y --set spec.values.global.pilotCertProvider=istiod -f -
         

  2. Install a gateway in `$CLUSTER_2` that is dedicated to east-west traffic for `$CLUSTER_1`.
         
         asm/istio/expansion/gen-eastwest-gateway.sh \
             --mesh ${MESH_ID}  \
             --cluster ${CLUSTER_2}  \
             --network default \
             --revision asm-1311-19 | \
             ./istioctl --kubeconfig=PATH_TO_KUBECONFIG_2 \
             install -y --set spec.values.global.pilotCertProvider=istiod -f -
         




**Platform note:** For Google Distributed Cloud, an external IP address won't be assigned until later, when you complete the steps described in [Configure external IP addresses for Google Distributed Cloud](https://docs.cloud.google.com/service-mesh/v1.20/docs/unified-install/external-ip-load-balance). 

## Exposing services

Since the clusters are on separate networks, you need to expose all services (`*.local`) on the east-west gateway in both clusters. While this gateway is public on the Internet, services behind it can only be accessed by services with a trusted mTLS certificate and workload ID, just as if they were on the same network.

  1. Expose services via the east-west gateway for `CLUSTER_NAME_1`.
         
         kubectl --kubeconfig=PATH_TO_KUBECONFIG_1 apply -n istio-system -f \
             asm/istio/expansion/expose-services.yaml
         

  2. Expose services via the east-west gateway for `CLUSTER_NAME_2`.
         
         kubectl --kubeconfig=PATH_TO_KUBECONFIG_2 apply -n istio-system -f \
             asm/istio/expansion/expose-services.yaml
         




## Enable endpoint discovery

**Note:** For more information on endpoint discovery, refer to [Endpoint discovery with multiple control planes](https://istio.io/v1.31/docs/ops/deployment/deployment-models/#endpoint-discovery-with-multiple-control-planes).

Run the `asmcli create-mesh` command to enable endpoint discovery. This example only shows two clusters, but you can run the command to enable endpoint discovery on additional clusters, subject to the [GKE Hub service limit](https://docs.cloud.google.com/anthos/fleet-management/docs/quotas).
    
    
      ./asmcli create-mesh \
          FLEET_PROJECT_ID \
          PATH_TO_KUBECONFIG_1 \
          PATH_TO_KUBECONFIG_2
    

## Verify multicluster connectivity

This section explains how to deploy the sample `HelloWorld` and `Sleep` services to your multi-cluster environment to verify that cross-cluster load balancing works.

**Note:** These sample services are located in the [Istio `samples` directory](https://github.com/istio/istio/tree/master/samples) included in the `istioctl` tarball (located in `OUTPUT_DIR/istio-${ASM_VERSION%+*}/samples`) and not the `samples` directory downloaded by `asmcli` (located in `OUTPUT_DIR/samples`).

### Enable sidecar injection

Locate the revision label value, which you use in later steps.

**Note:** If your clusters each have different versions of Cloud Service Mesh you must run the following command for each cluster.

Use the following command to locate the revision label, which you will use in later steps.
    
    
    kubectl -n istio-system get pods -l app=istiod --show-labels

The output looks similar to the following:
    
    
    NAME                                READY   STATUS    RESTARTS   AGE   LABELS
    istiod-asm-173-3-5788d57586-bljj4   1/1     Running   0          23h   app=istiod,istio.io/rev=asm-173-3,istio=istiod,pod-template-hash=5788d57586
    istiod-asm-173-3-5788d57586-vsklm   1/1     Running   1          23h   app=istiod,istio.io/rev=asm-173-3,istio=istiod,pod-template-hash=5788d57586

In the output, under the `LABELS` column, note the value of the `istiod` revision label, which follows the prefix `istio.io/rev=`. In this example, the value is `asm-173-3`. Use the revision value in the steps in the next section.

### Install the HelloWorld service

**Note:** The **HelloWorld service** example uses [Docker Hub](https://hub.docker.com/). In a private cluster, the container runtime can pull container images from [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) by default. The container runtime cannot pull images from any other container image registry on the internet. You can download the image and push to Artifact Registry or use [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to provide outbound internet access for certain private nodes. For more information, see [Migrate external containers](https://docs.cloud.google.com/container-registry/docs/migrate-external-containers) and [Creating a private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#pulling_images).

  1. Create the sample namespace and the Service Definition in each cluster. In the following command, substitute REVISION with the `istiod` revision label that you noted from the previous step.
         
         for CTX in ${CTX_1} ${CTX_2}
         do
             kubectl create --context=${CTX} namespace sample
             kubectl label --context=${CTX} namespace sample \
                 istio-injection- istio.io/rev=REVISION --overwrite
         done
         

where REVISION is the `istiod` revision label that you previously noted.

The output is:
         
         label "istio-injection" not found.
         namespace/sample labeled
         

You can safely ignore `label "istio-injection" not found.`

  2. Create the HelloWorld service in both clusters:
         
         kubectl create --context=${CTX_1} \
             -f ${SAMPLES_DIR}/samples/helloworld/helloworld.yaml \
             -l service=helloworld -n sample
         
         
         kubectl create --context=${CTX_2} \
             -f ${SAMPLES_DIR}/samples/helloworld/helloworld.yaml \
             -l service=helloworld -n sample
         




### Deploy HelloWorld v1 and v2 to each cluster

  1. Deploy `HelloWorld v1` to `CLUSTER_1` and `v2` to `CLUSTER_2`, which helps later to verify cross-cluster load balancing:
         
         kubectl create --context=${CTX_1} \
           -f ${SAMPLES_DIR}/samples/helloworld/helloworld.yaml \
           -l version=v1 -n sample
         
         kubectl create --context=${CTX_2} \
           -f ${SAMPLES_DIR}/samples/helloworld/helloworld.yaml \
           -l version=v2 -n sample

  2. Confirm `HelloWorld v1` and `v2` are running using the following commands. Verify that the output is similar to that shown.:
         
         kubectl get pod --context=${CTX_1} -n sample
         
         NAME                            READY     STATUS    RESTARTS   AGE
         helloworld-v1-86f77cd7bd-cpxhv  2/2       Running   0          40s
         
         kubectl get pod --context=${CTX_2} -n sample
         
         NAME                            READY     STATUS    RESTARTS   AGE
         helloworld-v2-758dd55874-6x4t8  2/2       Running   0          40s




### Deploy the Sleep service

  1. Deploy the `Sleep` service to both clusters. This pod generates artificial network traffic for demonstration purposes:
         
         for CTX in ${CTX_1} ${CTX_2}
         do
             kubectl apply --context=${CTX} \
                 -f ${SAMPLES_DIR}/samples/sleep/sleep.yaml -n sample
         done
         

  2. Wait for the `Sleep` service to start in each cluster. Verify that the output is similar to that shown:
         
         kubectl get pod --context=${CTX_1} -n sample -l app=sleep
         
         NAME                             READY   STATUS    RESTARTS   AGE
         sleep-754684654f-n6bzf           2/2     Running   0          5s
         
         kubectl get pod --context=${CTX_2} -n sample -l app=sleep
         
         NAME                             READY   STATUS    RESTARTS   AGE
         sleep-754684654f-dzl9j           2/2     Running   0          5s




### Verify cross-cluster load balancing

Call the `HelloWorld` service several times and check the output to verify alternating replies from v1 and v2:

  1. Call the `HelloWorld` service:
         
         kubectl exec --context="${CTX_1}" -n sample -c sleep \
             "$(kubectl get pod --context="${CTX_1}" -n sample -l \
             app=sleep -o jsonpath='{.items[0].metadata.name}')" \
             -- /bin/sh -c 'for i in $(seq 1 20); do curl -sS helloworld.sample:5000/hello; done'
         

The output is similar to that shown:
         
         Hello version: v2, instance: helloworld-v2-758dd55874-6x4t8
         Hello version: v1, instance: helloworld-v1-86f77cd7bd-cpxhv
         ...

  2. Call the `HelloWorld` service again:
         
         kubectl exec --context="${CTX_2}" -n sample -c sleep \
             "$(kubectl get pod --context="${CTX_2}" -n sample -l \
             app=sleep -o jsonpath='{.items[0].metadata.name}')" \
             -- /bin/sh -c 'for i in $(seq 1 20); do curl -sS helloworld.sample:5000/hello; done'
         

The output is similar to that shown:
         
         Hello version: v2, instance: helloworld-v2-758dd55874-6x4t8
         Hello version: v1, instance: helloworld-v1-86f77cd7bd-cpxhv
         ...




Congratulations, you've verified your load-balanced, multi-cluster Cloud Service Mesh!

## Clean up

When you finish verifying load balancing, remove the `HelloWorld` and `Sleep` service from your cluster.
    
    
    kubectl delete ns sample --context ${CTX_1}
    kubectl delete ns sample --context ${CTX_2}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
