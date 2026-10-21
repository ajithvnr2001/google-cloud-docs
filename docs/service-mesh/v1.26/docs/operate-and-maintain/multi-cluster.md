---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/operate-and-maintain/multi-cluster/
title: Set up a multi-cluster mesh on managed Cloud Service Mesh \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:30.942994+00:00
---

# Set up a multi-cluster mesh on managed Cloud Service Mesh  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/operate-and-maintain/multi-cluster/

You are viewing archived v1.26 Service Mesh documentation.

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
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a multi-cluster mesh on managed Cloud Service Mesh

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview).

This guide explains how to join two clusters into a single Cloud Service Mesh using [Mesh CA](https://docs.cloud.google.com/service-mesh/v1.26/docs/security/security-overview#features) or Certificate Authority Service and enable cross-cluster load balancing. You can easily extend this process to incorporate any number of clusters into your mesh.

A multi-cluster Cloud Service Mesh configuration can solve several crucial enterprise scenarios, such as scale, location, and isolation. For more information, see [Multi-cluster use cases](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/multi-cluster-use-cases).

## Prerequisites

This guide assumes that you have two or more Google Cloud GKE clusters that meet the following requirements:

  * Cloud Service Mesh installed on the clusters. You need `asmcli`, the `istioctl` tool, and samples that `asmcli` downloads to the directory that you specified in `--output_dir`.
  * Clusters in your mesh must have connectivity between all pods before you configure Cloud Service Mesh. Additionally, if you join clusters that are not in the same project, they must be registered to the same [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project), and the clusters must be in a [shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) configuration together on the same network. We also recommend that you have one project to host the Shared VPC, and two service projects for creating clusters. For more information, see [Setting up clusters with Shared VPC](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc).
  * If you use Certificate Authority Service, all clusters must have their respective subordinate CA pools chain to the same root CA pool. Otherwise, all of them will need to use the same CA pool. 



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

**Note:** For more information on endpoint discovery, refer to [Endpoint discovery with multiple control planes](https://istio.io/v1.26/docs/ops/deployment/deployment-models/#endpoint-discovery-with-multiple-control-planes).**Warning:** If endpoint discovery is enabled between clusters, intercluster services are not able to communicate with each other without proper DNS configuration. This is because GKE services depend on each service's fully qualified domain name (FQDN) for traffic routing. You can enable [DNS proxy](https://istio.io/latest/docs/ops/configuration/traffic-management/dns-proxy/), to allow intercluster discovery. DNS proxy captures all DNS requests and resolves them using information from the Control Plane.

### Enable endpoint discovery between public or private clusters with declarative API

Enabling managed Cloud Service Mesh with the fleet API will enable endpoint discovery for this cluster. If you provisioned managed Cloud Service Mesh with a different tool, you can manually enable endpoint discovery across public or private clusters in a fleet by applying the config `"multicluster_mode":"connected"` in the `asm-options` configmap. Clusters with this config enabled in the same fleet will have cross-cluster service discovery automatically enabled between each other.

**Warning:** Don't use this method if your clusters use existing in-cluster remote secrets.

This is the only way to configure multi-cluster endpoint discovery if you have the Managed (TD) [control plane implementation](https://docs.cloud.google.com/service-mesh/v1.26/docs/supported-features-managed#identify_control_plane_implementation), and the recommended way to configure it if you have the Managed (Istiod) implementation.

Before proceeding, you must have created a firewall rule.

### Enable

If the `asm-options` configmap _already exists_ in your cluster, then enable endpoint discovery for the cluster:
    
    
          kubectl patch configmap/asm-options -n istio-system --type merge -p '{"data":{"multicluster_mode":"connected"}}'
    

If the `asm-options` configmap _doesn't yet exist_ in your cluster, then create it with the associated data and enable endpoint discovery for the cluster:
    
    
          kubectl --context ${CTX_1} create configmap asm-options -n istio-system --from-file <(echo '{"data":{"multicluster_mode":"connected"}}')
    

### Disable

Disable endpoint discovery for a cluster:
    
    
          kubectl patch configmap/asm-options -n istio-system --type merge -p '{"data":{"multicluster_mode":"manual"}}'
    

If you unregister a cluster from the fleet without disabling endpoint discovery, secrets could remain in the cluster. You must manually clean up any remaining secrets.

  1. Run the following command to find secrets requiring cleanup:
         
         kubectl get secrets -n istio-system -l istio.io/owned-by=mesh.googleapis.com,istio/multiCluster=true
         

  2. Delete each secret:
         
         kubectl delete secret SECRET_NAME
         

Repeat this step for each remaining secret.




## Verify multi-cluster connectivity

This section explains how to deploy the sample `HelloWorld` and `Sleep` services to your multi-cluster environment to verify that cross-cluster load balancing works.

**Note:** These sample services are located in the [Istio `samples` directory](https://github.com/istio/istio/tree/master/samples) included in the `istioctl` tar file (located in `OUTPUT_DIR/istio-${ASM_VERSION%+*}/samples`) and not the `samples` directory downloaded by `asmcli` (located in `OUTPUT_DIR/samples`).

### Set variable for samples directory

  1. Navigate to where `asmcli` was downloaded, and run the following command to set `ASM_VERSION`
         
         export ASM_VERSION="$(./asmcli --version)"
         

  2. Set a working folder to the samples that you use to verify that cross-cluster load balancing works. The samples are located in a subdirectory in the `--output_dir` directory that you specified in the `asmcli install` command. In the following command, change `OUTPUT_DIR` to the directory that you specified in `--output_dir`.
         
         export SAMPLES_DIR=OUTPUT_DIR/istio-${ASM_VERSION%+*}
         




### Enable sidecar injection

  1. Create the sample namespace in each cluster.
         
         for CTX in ${CTX_1} ${CTX_2}
         do
             kubectl create --context=${CTX} namespace sample
         done
         

  2. Enable the namespace for injection. The steps depend on your [control plane implementation](https://docs.cloud.google.com/service-mesh/v1.26/docs/check-control-plane-implementation).

### Managed (TD)

     1. Apply the default injection label to the namespace:
    
    for CTX in ${CTX_1} ${CTX_2}
    do
       kubectl label --context=${CTX} namespace sample \
          istio.io/rev- istio-injection=enabled --overwrite
    done
    

### Managed (Istiod)

**Recommended:** Run the following command to apply the default injection label to the namespace:
    
    for CTX in ${CTX_1} ${CTX_2}
     do
        kubectl label --context=${CTX} namespace sample \
           istio.io/rev- istio-injection=enabled --overwrite
     done
    

**If you are an existing user with the Managed Istiod control plane:** We recommend that you use default injection, but revision-based injection is supported. Use the following instructions:

     1. Run the following command to locate the available release channels:
            
            kubectl -n istio-system get controlplanerevision
            

The output is similar to the following:
            
            NAME                AGE
            asm-managed-rapid   6d7h
            

**Note:** If two control plane revisions appear in the earlier list, remove one. Having multiple control plane channels in the cluster is not supported.

In the output, the value under the `NAME` column is the revision label that corresponds to the available [release channel](https://docs.cloud.google.com/service-mesh/v1.26/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) for the Cloud Service Mesh version.

     2. Apply the revision label to the namespace:
            
            for CTX in ${CTX_1} ${CTX_2}
            do
              kubectl label --context=${CTX} namespace sample \
                 istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            done
            




### Install the HelloWorld service

**Note:** The **HelloWorld service** example uses [Docker Hub](https://hub.docker.com/). In a private cluster, the container runtime can pull container images from [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) by default. The container runtime cannot pull images from any other container image registry on the internet. You can download the image and push to Artifact Registry or use [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to provide outbound internet access for certain private nodes. For more information, see [Migrate external containers](https://docs.cloud.google.com/container-registry/docs/migrate-external-containers) and [Creating a private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#pulling_images).

  * Create the HelloWorld service in both clusters:
        
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

## Keeping traffic in-cluster

In some cases the default cross-cluster load balancing behavior is not desirable. To keep traffic "cluster-local" (i.e. traffic sent from `cluster-a` will only reach destinations in `cluster-a`), mark hostnames or wildcards as `clusterLocal` using `MeshConfig.serviceSettings`.

For example, you can enforce cluster-local traffic for an individual service, all services in a particular namespace, or globally for all services in the mesh, as follows:

### per-service
    
    
    serviceSettings:
    - settings:
        clusterLocal: true
      hosts:
      - "mysvc.myns.svc.cluster.local"
    

### per-namespace
    
    
    serviceSettings:
    - settings:
        clusterLocal: true
      hosts:
      - "*.myns.svc.cluster.local"
    

### global
    
    
    serviceSettings:
    - settings:
        clusterLocal: true
      hosts:
      - "*"
    

You can also refine service access by setting a global cluster-local rule and adding explicit exceptions, which can be specific or wildcard. In the following example, all services in the cluster will be kept cluster-local, except any service in the myns namespace:
    
    
    serviceSettings:
    - settings:
        clusterLocal: true
      hosts:
      - "*"
    - settings:
        clusterLocal: false
      hosts:
      - "*.myns.svc.cluster.local"
    

### Enable the Local Cluster Service

  1. Check the MeshConfig config map in the cluster
         
         kubectl get configmap -n istio-system
         

You should see a config map with one of the names `istio-asm-managed`, `istio-asm-managed-rapid` or `istio-asm-managed-stable`.

If you have migrated from the `ISTIOD` implementation to the `TRAFFIC_DIRECTOR` implementation, you might see more than one config map. In this case, you can determine the channel by running the following command:
         
         kubectl get controlplanerevision -n istio-system
         

The channel of the reconciled Control Plane Revision is the one you want to pick.

  2. Update the Config Map
         
         cat <<EOF > config.yaml
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: CONFIGMAP_NAME
           namespace: istio-system
         data:
           mesh: |-
             serviceSettings:
             - settings:
                 clusterLocal: true
               hosts:
               - "*"
         EOF
         

Replace `CONFIGMAP_NAME` with the name of the Config Map you found in step 1 and update the config map.
         
         kubectl apply --context=${CTX_1} -f config.yaml
         

  3. Confirm the Local Cluster feature are working as expected using the following commands. The output for calling `HelloWorld` with `CTX_1` is similar to:
         
         kubectl exec --context="${CTX_1}" -n sample -c sleep \
             "$(kubectl get pod --context="${CTX_1}" -n sample -l \
             app=sleep -o jsonpath='{.items[0].metadata.name}')" \
             -- /bin/sh -c 'for i in $(seq 1 20); do curl -sS helloworld.sample:5000/hello; done'
         

You should see **Only v1 is response** in the output:
         
         Hello version: v1, instance: helloworld-v2-758dd55874-6x4t8
         Hello version: v1, instance: helloworld-v1-86f77cd7bd-cpxhv
         ...
         

If you call the `HelloWorld` with `CTX_2`:
         
         kubectl exec --context="${CTX_2}" -n sample -c sleep \
             "$(kubectl get pod --context="${CTX_2}" -n sample -l \
             app=sleep -o jsonpath='{.items[0].metadata.name}')" \
             -- /bin/sh -c 'for i in $(seq 1 20); do curl -sS helloworld.sample:5000/hello; done'
         

You should see alternating replies from v1 and v2 in the output.
         
         Hello version: v2, instance: helloworld-v2-758dd55874-6x4t8
         Hello version: v1, instance: helloworld-v1-86f77cd7bd-cpxhv
         ...
         




## Clean up HelloWorld service

When you finish verifying load balancing, remove the `HelloWorld` and `Sleep` service from your cluster.
    
    
    kubectl delete ns sample --context ${CTX_1}
    kubectl delete ns sample --context ${CTX_2}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
