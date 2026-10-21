---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/gke-install-multi-cluster/
title: Set up a multi-cluster mesh on GKE \u00a0|\u00a0 Cloud Service Mesh v1.19 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:02.018629+00:00
---

# Set up a multi-cluster mesh on GKE  |  Cloud Service Mesh v1.19  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/gke-install-multi-cluster/

You are viewing archived v1.19 Service Mesh documentation.

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
  * [ v1.19 ](https://docs.cloud.google.com/service-mesh/v1.19/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.19/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a multi-cluster mesh on GKE

This guide explains how to join two clusters into a single Cloud Service Mesh using [Mesh CA](https://docs.cloud.google.com/service-mesh/v1.19/docs/security/security-overview#features) or [Istio CA](https://istio.io/v1.19/docs/tasks/security/cert-management/plugin-ca-cert/), and enable cross-cluster load balancing. You can easily extend this process to incorporate any number of clusters into your mesh.

A multi-cluster Cloud Service Mesh configuration can solve several crucial enterprise scenarios, such as scale, location, and isolation. For more information, see [Multi-cluster use cases](https://docs.cloud.google.com/anthos/fleet-management/docs/multi-cluster-use-cases).

## Prerequisites

This guide assumes that you have two or more Google Cloud GKE clusters that meet the following requirements:

  * Cloud Service Mesh version 1.11 or later installed on the clusters using [`asmcli install`](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/asmcli-overview). You need `asmcli`, the `istioctl` tool, and samples that `asmcli` downloads to the directory that you specified in `--output_dir` when you ran `asmcli install` If need to get set up, follow the steps in [Install dependent tools and validate cluster](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools) to:

    * [Install required tools](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools)
    * [Download `asmcli`](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools#download_asmcli)
    * [Grant cluster admin permissions](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools#grant_cluster_admin_permissions)
    * [Validate your project and cluster](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-dependent-tools#validate_project_and_cluster)
  * Clusters in your mesh must have connectivity between all pods before you configure Cloud Service Mesh. Additionally, if you join clusters that are not in the same project, they must be registered to the same [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project), and the clusters must be in a [shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) configuration together on the same network. We also recommend that you have one project to host the shared VPC, and two service projects for creating clusters. For more information, see [Setting up clusters with Shared VPC](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc).

  * If you use Istio CA, use the same custom root certificate for both clusters.

  * If your Cloud Service Mesh is built on private clusters, we recommend [creating a single subnet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#custom_subnet) in the same VPC, otherwise, you must ensure that:

    1. The control planes can reach the remote private cluster control planes via the [cluster private IPs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#view_endpoint).
    2. You can add the calling control planes' IP ranges to the remote private clusters' [authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks). For more information, see Configure endpoint discovery between private clusters.
  * The API server must be reachable by the other instances of the Cloud Service Mesh control plane in the multi-cluster mesh.

    * Ensure the clusters have [global access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#enabling_control_plane_private_endpoint_global_access) enabled.
    * Ensure the Cloud Service Mesh control plane IP has been properly allowed via the allow list with the [Master Authorized Network](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).



## Setting project and cluster variables

  1. Create the following environment variables for the project ID, cluster zone or region, cluster name, and context.
         
         export PROJECT_1=PROJECT_ID_1
         export LOCATION_1=CLUSTER_LOCATION_1
         export CLUSTER_1=CLUSTER_NAME_1
         export CTX_1="gke_${PROJECT_1}_${LOCATION_1}_${CLUSTER_1}"
         
         export PROJECT_2=PROJECT_ID_2
         export LOCATION_2=CLUSTER_LOCATION_2
         export CLUSTER_2=CLUSTER_NAME_2
         export CTX_2="gke_${PROJECT_2}_${LOCATION_2}_${CLUSTER_2}"
         

  2. If these are newly created clusters, ensure to fetch credentials for each cluster with the following `gcloud` commands otherwise their associated `context` will not be available for use in the next steps of this guide.

The commands depend on your cluster type, either regional or zonal:

### Regional
         
         gcloud container clusters get-credentials ${CLUSTER_1} --region ${LOCATION_1}
         gcloud container clusters get-credentials ${CLUSTER_2} --region ${LOCATION_2}
         

### Zonal
         
         gcloud container clusters get-credentials ${CLUSTER_1} --zone ${LOCATION_1}
         gcloud container clusters get-credentials ${CLUSTER_2} --zone ${LOCATION_2}
         




## Create firewall rule

In some cases, you need to create a firewall rule to allow cross-cluster traffic. For example, you need to create a firewall rule if:

  * You use different subnets for the clusters in your mesh.
  * Your Pods open ports other than 443 and 15002.



GKE automatically adds firewall rules to each node to allow traffic within the same subnet. If your mesh contains multiple subnets, you must explicitly set up the firewall rules to allow cross-subnet traffic. You must [add a new firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#add_firewall_rules) for each subnet to allow the source IP CIDR blocks and targets ports of all the incoming traffic.

The following instructions allow communication between all clusters in your project or only between `$CLUSTER_1` and `$CLUSTER_2`.

  1. Gather information about your clusters' network.

### All project clusters

If the clusters are in the same project, you can use the following command to allow communication between all clusters in your project. If there are clusters in your project that you don't want to expose, use the command in the **Specific clusters** tab.
         
         function join_by { local IFS="$1"; shift; echo "$*"; }
         ALL_CLUSTER_CIDRS=$(gcloud container clusters list --project $PROJECT_1 --format='value(clusterIpv4Cidr)' | sort | uniq)
         ALL_CLUSTER_CIDRS=$(join_by , $(echo "${ALL_CLUSTER_CIDRS}"))
         ALL_CLUSTER_NETTAGS=$(gcloud compute instances list --project $PROJECT_1 --format='value(tags.items.[0])' | sort | uniq)
         ALL_CLUSTER_NETTAGS=$(join_by , $(echo "${ALL_CLUSTER_NETTAGS}"))
         

### Specific clusters

The following command allows communication between `$CLUSTER_1` and `$CLUSTER_2` and doesn't expose other clusters in your project.
         
         function join_by { local IFS="$1"; shift; echo "$*"; }
         ALL_CLUSTER_CIDRS=$(for P in $PROJECT_1 $PROJECT_2; do gcloud --project $P container clusters list --filter="name:($CLUSTER_1,$CLUSTER_2)" --format='value(clusterIpv4Cidr)'; done | sort | uniq)
         ALL_CLUSTER_CIDRS=$(join_by , $(echo "${ALL_CLUSTER_CIDRS}"))
         ALL_CLUSTER_NETTAGS=$(for P in $PROJECT_1 $PROJECT_2; do gcloud --project $P compute instances list  --filter="name:($CLUSTER_1,$CLUSTER_2)" --format='value(tags.items.[0])' ; done | sort | uniq)
         ALL_CLUSTER_NETTAGS=$(join_by , $(echo "${ALL_CLUSTER_NETTAGS}"))
         

  2. Create the firewall rule.

### GKE
         
         gcloud compute firewall-rules create istio-multicluster-pods \
             --allow=tcp,udp,icmp,esp,ah,sctp \
             --direction=INGRESS \
             --priority=900 \
             --source-ranges="${ALL_CLUSTER_CIDRS}" \
             --target-tags="${ALL_CLUSTER_NETTAGS}" --quiet \
             --network=YOUR_NETWORK
         

### Autopilot
         
         TAGS=""
         for CLUSTER in ${CLUSTER_1} ${CLUSTER_2}
         do
             TAGS+=$(gcloud compute firewall-rules list --filter="Name:$CLUSTER*" --format="value(targetTags)" | uniq) && TAGS+=","
         done
         TAGS=${TAGS::-1}
         echo "Network tags for pod ranges are $TAGS"
         
         gcloud compute firewall-rules create asm-multicluster-pods \
             --allow=tcp,udp,icmp,esp,ah,sctp \
             --network=gke-cluster-vpc \
             --direction=INGRESS \
             --priority=900 --network=VPC_NAME \
             --source-ranges="${ALL_CLUSTER_CIDRS}" \
             --target-tags=$TAGS
         




## Configure endpoint discovery

**Note:** For more information on endpoint discovery, refer to [Endpoint discovery with multiple control planes](https://istio.io/v1.19/docs/ops/deployment/deployment-models/#endpoint-discovery-with-multiple-control-planes).

The steps required to configure endpoint discovery depend on whether you prefer to use the declarative API across clusters in a fleet, or enable it manually on public clusters or private clusters.

**Warning:** If endpoint discovery is enabled between clusters, inter-cluster services are not able to communicate with each other without proper DNS configuration. This is because GKE services depend on each service's fully qualified domain name (FQDN) for traffic routing. You can enable [DNS proxy](https://istio.io/latest/docs/ops/configuration/traffic-management/dns-proxy/), to allow inter-cluster discovery. DNS proxy captures all DNS requests and resolves them using information from the Control Plane.

### Enable endpoint discovery between public or private clusters with declarative API (preview)

**Preview — Enable endpoint discovery**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can enable endpoint discovery across public or private clusters in a fleet by applying the config `"multicluster_mode":"connected"` in the in the `asm-options` configmap. Clusters with this config enabled in the same fleet will have cross-cluster service discovery automatically enabled between each other.

**Warning:** Don't use this method if your clusters already use existing in-cluster remote secrets.

This method is available for managed Cloud Service Mesh installations on all release channels. This is also the preferred way to configure multi-cluster endpoint discovery if you provisioned managed Cloud Service Mesh using the [**Enable Cloud Service Mesh** feature when creating a new GKE cluster in the Google Cloud console](https://docs.cloud.google.com/service-mesh/docs/managed/install-anthos-service-mesh-console).

Before proceeding, you must have created a firewall rule.

For multiple projects, you must manually add `FLEET_PROJECT_ID.svc.id.goog` to `trustDomainAliases` in the revison's `meshConfig` if it's not already present.

### Enable

If the `asm-options` configmap _already exists_ in your cluster, then enable endpoint discovery for the cluster:
    
    
    kubectl patch configmap/asm-options -n istio-system --type merge -p '{"data":{"multicluster_mode":"connected"}}'
    

If the `asm-options` configmap _does not yet exist_ in your cluster, then create it with the associated data and enable endpoint discovery for the cluster:
    
    
    kubectl --context ${CTX_1} create configmap asm-options -n istio-system --from-file <(echo '{"data":{"multicluster_mode":"connected"}}')
    

### Disable

Disable endpoint discovery for a cluster:
    
    
    kubectl patch configmap/asm-options -n istio-system --type merge -p '{"data":{"multicluster_mode":"manual"}}'
    

If you unregister a cluster from the fleet without disabling endpoint discovery, secrets could remain in the cluster. You must manually clean up any remaining secrets.

  1. Run the following command to find secrets requiring cleanup:
         
         kubectl get secrets -n istio-system -l istio.io/owned-by=mesh.googleapis.com,istio/multiCluster=true
         

  2. Delete each secret:
         
         kubectl delete secret SECRET_NAME -n istio-system
         

Repeat this step for each remaining secret.




### Configure endpoint discovery between public clusters

To configure endpoint discovery between GKE clusters, you run `asmcli create-mesh`. This command:

  * Registers all clusters to the same fleet.
  * Configures the mesh to trust the fleet workload identity.
  * Creates remote secrets.



You can either specify the URI for each cluster or the path the [kubeconfig file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/).

### Cluster URI

In the following command, replace `FLEET_PROJECT_ID` with the project ID of the fleet host project and the cluster URI with the cluster name, zone or region, and project ID for each cluster. This example only shows two clusters, but you can run the command to enable endpoint discovery on additional clusters, subject to the [maximum permitted number of clusters that you can add to your fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/quotas).
    
    
    ./asmcli create-mesh \
        FLEET_PROJECT_ID \
        ${PROJECT_1}/${LOCATION_1}/${CLUSTER_1} \
        ${PROJECT_2}/${LOCATION_2}/${CLUSTER_2}
    

### kubeconfig file

In the following command, replace `FLEET_PROJECT_ID` with the project ID of the [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project) and `PATH_TO_KUBECONFIG` with the path to each `kubeconfig` file. This example only shows two clusters, but you can run the command to enable endpoint discovery on additional clusters, subject to the [maximum permitted number of clusters that you can add to your fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/quotas).
    
    
    ./asmcli create-mesh \
        FLEET_PROJECT_ID \
        PATH_TO_KUBECONFIG_1 \
        PATH_TO_KUBECONFIG_2
    

### Configure endpoint discovery between private clusters

  1. Configure remote secrets to allow API server access to the cluster to the other cluster's Cloud Service Mesh control plane. The commands depend on your Cloud Service Mesh type (either in-cluster or managed):

**Note:** Ensure you run the following commands using the `istioctl` from the `--output_dir` location you specified when running `asmcli install` by executing `istioctl` commands in a way `../output_dir/istioctl`.

A. For in-cluster Cloud Service Mesh, you must configure the private IPs instead of public IPs because the public IPs are not accessible:
         
         PRIV_IP=`gcloud container clusters describe "${CLUSTER_1}" --project "${PROJECT_1}" \
          --zone "${LOCATION_1}" --format "value(privateClusterConfig.privateEndpoint)"`
         
         ./istioctl x create-remote-secret --context=${CTX_1} --name=${CLUSTER_1} --server=https://${PRIV_IP} > ${CTX_1}.secret
         
         
         PRIV_IP=`gcloud container clusters describe "${CLUSTER_2}" --project "${PROJECT_2}" \
          --zone "${LOCATION_2}" --format "value(privateClusterConfig.privateEndpoint)"`
         
         ./istioctl x create-remote-secret --context=${CTX_2} --name=${CLUSTER_2} --server=https://${PRIV_IP} > ${CTX_2}.secret
         

B. For Managed Cloud Service Mesh:
         
         PUBLIC_IP=`gcloud container clusters describe "${CLUSTER_1}" --project "${PROJECT_1}" \
          --zone "${LOCATION_1}" --format "value(privateClusterConfig.publicEndpoint)"`
         
         ./istioctl x create-remote-secret --context=${CTX_1} --name=${CLUSTER_1} --server=https://${PUBLIC_IP} > ${CTX_1}.secret
         
         
         PUBLIC_IP=`gcloud container clusters describe "${CLUSTER_2}" --project "${PROJECT_2}" \
          --zone "${LOCATION_2}" --format "value(privateClusterConfig.publicEndpoint)"`
         
         ./istioctl x create-remote-secret --context=${CTX_2} --name=${CLUSTER_2} --server=https://${PUBLIC_IP} > ${CTX_2}.secret
         

  2. Apply the new secrets into the clusters:
         
         kubectl apply -f ${CTX_1}.secret --context=${CTX_2}
         
         
         kubectl apply -f ${CTX_2}.secret --context=${CTX_1}
         




## Configure authorized networks for private clusters

Follow this section only if all of the following conditions apply to your mesh:

  * You are using [private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters).
  * The clusters do not belong to the same [subnet](https://docs.cloud.google.com/vpc/docs/vpc#subnets_vs_subnetworks).
  * The clusters have enabled [authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).



When deploying multiple private clusters, the Cloud Service Mesh control plane in each cluster needs to call the GKE control plane of the remote clusters. To allow traffic, you need to add the Pod address range in the calling cluster to the authorized networks of the remote clusters.

  1. Get the Pod IP CIDR block for each cluster:
         
         POD_IP_CIDR_1=`gcloud container clusters describe ${CLUSTER_1} --project ${PROJECT_1} --zone ${LOCATION_1} \
           --format "value(ipAllocationPolicy.clusterIpv4CidrBlock)"`
         
         
         POD_IP_CIDR_2=`gcloud container clusters describe ${CLUSTER_2} --project ${PROJECT_2} --zone ${LOCATION_2} \
           --format "value(ipAllocationPolicy.clusterIpv4CidrBlock)"`
         

  2. Add the Kubernetes cluster Pod IP CIDR blocks to the remote clusters:
         
         EXISTING_CIDR_1=`gcloud container clusters describe ${CLUSTER_1} --project ${PROJECT_1} --zone ${LOCATION_1} \
          --format "value(masterAuthorizedNetworksConfig.cidrBlocks.cidrBlock)"`
         gcloud container clusters update ${CLUSTER_1} --project ${PROJECT_1} --zone ${LOCATION_1} \
         --enable-master-authorized-networks \
         --master-authorized-networks ${POD_IP_CIDR_2},${EXISTING_CIDR_1//;/,}
         
         
         EXISTING_CIDR_2=`gcloud container clusters describe ${CLUSTER_2} --project ${PROJECT_2} --zone ${LOCATION_2} \
          --format "value(masterAuthorizedNetworksConfig.cidrBlocks.cidrBlock)"`
         gcloud container clusters update ${CLUSTER_2} --project ${PROJECT_2} --zone ${LOCATION_2} \
         --enable-master-authorized-networks \
         --master-authorized-networks ${POD_IP_CIDR_1},${EXISTING_CIDR_2//;/,}
         

For more information, see [Creating a cluster with authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#create_cluster).

  3. Verify that the authorized networks are updated:
         
         gcloud container clusters describe ${CLUSTER_1} --project ${PROJECT_1} --zone ${LOCATION_1} \
          --format "value(masterAuthorizedNetworksConfig.cidrBlocks.cidrBlock)"
         
         
         gcloud container clusters describe ${CLUSTER_2} --project ${PROJECT_2} --zone ${LOCATION_2} \
          --format "value(masterAuthorizedNetworksConfig.cidrBlocks.cidrBlock)"
         




## Enable control plane global access

Follow this section only if all of the following conditions apply to your mesh:

  * You are using private clusters.
  * You use different regions for the clusters in your mesh.



You must [enable control plane global access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#cp-global-access) to allow Cloud Service Mesh control plane in each cluster to call the GKE control plane of the remote clusters.

  1. Enable control plane global access:
         
         gcloud container clusters update ${CLUSTER_1} --project ${PROJECT_1} --zone ${LOCATION_1} \
          --enable-master-global-access
         
         
         gcloud container clusters update ${CLUSTER_2} --project ${PROJECT_2} --zone ${LOCATION_2} \
          --enable-master-global-access
         

  2. Verify that control plane global access in enabled:
         
         gcloud container clusters describe ${CLUSTER_1} --project ${PROJECT_1} --zone ${LOCATION_1}
         
         
         gcloud container clusters describe ${CLUSTER_2} --project ${PROJECT_2} --zone ${LOCATION_2}
         

The `privateClusterConfig` section in the output displays the status of `masterGlobalAccessConfig`.




## Verify multicluster connectivity

**Platform note:** These steps are only applicable if you are using an in-cluster control plane. For managed Cloud Service Mesh, see [Injecting sidecar proxies](https://docs.cloud.google.com/service-mesh/v1.19/docs/anthos-service-mesh-proxy-injection#enabling_automatic_sidecar_injection) or [Apply the managed data plane](https://docs.cloud.google.com/service-mesh/docs/managed/service-mesh#managed-data-plane). 

This section explains how to deploy the sample `HelloWorld` and `Sleep` services to your multi-cluster environment to verify that cross-cluster load balancing works.

**Note:** These sample services are located in the [Istio `samples` directory](https://github.com/istio/istio/tree/master/samples) included in the `istioctl` tarball (located in `OUTPUT_DIR/istio-${ASM_VERSION%+*}/samples`) and not the `samples` directory downloaded by `asmcli` (located in `OUTPUT_DIR/samples`).

### Set variable for samples directory

  1. Navigate to where `asmcli` was downloaded, and run the following command to set `ASM_VERSION`
         
         export ASM_VERSION="$(./asmcli --version)"
         

  2. Set a working folder to the samples that you use to verify that cross-cluster load balancing works. The samples are located in a subdirectory in the `--output_dir` directory that you specified in the `asmcli install` command. In the following command, change `OUTPUT_DIR` to the directory that you specified in `--output_dir`.
         
         export SAMPLES_DIR=OUTPUT_DIR/istio-${ASM_VERSION%+*}
         




### Enable sidecar injection

  1. Locate the revision label value, which you use in later steps. The step depends on your Cloud Service Mesh type (either managed or in-cluster).

**Note:** If your clusters each have different versions of Cloud Service Mesh you must run the following command for each cluster.

### Managed

Use the following command to locate the revision label, which you will use in later steps.
         
         kubectl get controlplanerevision -n istio-system

The output looks similar to the following:
         
         NAME                RECONCILED   STALLED   AGE
          asm-managed-rapid   True         False     89d
          

In the output, under the `NAME` column, note the value of the revision label. In this example, the value is `asm-managed-rapid`. Use the revision value in the steps in the next section.

### In-cluster

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

**Important:** If you are using Cloud Service Mesh managed control plane, replace REVISION with `asm-managed` in the following steps.
         
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

## Clean up HelloWorld service

When you finish verifying load balancing, remove the `HelloWorld` and `Sleep` service from your cluster.
    
    
    kubectl delete ns sample --context ${CTX_1}
    kubectl delete ns sample --context ${CTX_2}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
