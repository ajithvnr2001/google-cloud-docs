---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/deploy/
title: Deploy workloads \u00a0|\u00a0 Google Distributed Cloud connected, version 1.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:41:44.862749+00:00
---

# Deploy workloads  |  Google Distributed Cloud connected, version 1.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/deploy/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/overview)



Send feedback 

#  Deploy workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to deploy workloads on your Google Distributed Cloud connected hardware and the limitations that you must adhere to when configuring your workloads.

Before you complete these steps, you must [meet the Distributed Cloud connected installation requirements](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/requirements) and [order the Distributed Cloud hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/order).

When the Google Distributed Cloud connected hardware arrives at your chosen destination, it is pre-configured with hardware, Google Cloud, and some network settings that you specified when you ordered Distributed Cloud connected.

Google installers complete the physical installation, and your system administrator connects Distributed Cloud connected to your local network.

After the hardware is connected to your local network, it communicates with Google Cloud to download software updates and connect with your Google Cloud project. You are then ready to provision node pools and deploy workloads on Distributed Cloud connected.

## Deployment overview

To deploy a workload on your Distributed Cloud connected hardware, complete the following steps:

  1. Optional: [Enable the Distributed Cloud Edge Network API](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/networking#network-api-enable).

  2. Optional: [Initialize the network configuration of your Distributed Cloud connected zone](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/zones#init).

  3. Optional: [Configure Distributed Cloud networking](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/networking#network-configure).

  4. [Create a Distributed Cloud connected cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/clusters#create).

  5. Optional: [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/security#cmek) if you want to integrate with Cloud Key Management Service to enable support for CMEK for your workload data. For information about how Distributed Cloud connected encrypts workload data, see [Local storage security](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/security#storage).

  6. [Create a node pool](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/nodepools#create). In this step, you assign nodes to a node pool and optionally configure the node pool to use Cloud KMS to wrap and unwrap the Linux Unified Key Setup (LUKS) passphrase for encrypting workload data.

  7. [Obtain credentials for a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/clusters#credentials) to test the cluster.

  8. Grant users access to the cluster by assigning them the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) or the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) on the project.

  9. [Assign users granular role-based access to the cluster resources by using `RoleBinding` and `ClusterRoleBinding`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

  10. Optional: [Enable VM Runtime on Google Distributed Cloud support to run workloads on virtual machines on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/virtual-machines#enable-anthos-vm-runtime-support).

  11. Optional: [Enable GPU support to run GPU-based workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/gpu).

  12. Optional: Connect the Distributed Cloud connected cluster to Google Cloud:

     1. [Create a VPN connection to your Google Cloud project](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/vpn-connections#create).

     2. [Check that the VPN connection is operational](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/vpn-connections#status).

  13. Optional: [Configure Private Google Access to let your Pods access Google Cloud APIs and services by using Cloud VPN](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

  14. Optional: [Configure Private Service Connect to let your Pods access Google Cloud APIs and services by using Cloud VPN](https://docs.cloud.google.com/vpc/docs/private-service-connect).




## Deploy the NGINX load balancer as a service

The following example illustrates how to deploy the NGINX server and expose it as a service on a Distributed Cloud connected cluster:

  1. Create a YAML file named `nginx-deployment.yaml` with the following contents:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
         name: nginx
         labels:
           app: nginx
         spec:
         replicas: 1
         selector:
           matchLabels:
              app: nginx
         template:
           metadata:
              labels:
              app: nginx
           spec:
              containers:
              - name: nginx
              image: nginx:latest
              ports:
              - containerPort: 80 

  2. Apply the YAML file to the cluster using the following command:
         
         kubectl apply -f nginx-deployment.yaml
         

  3. Create a YAML file named `nginx-service.yaml` with the following contents:
         
         apiVersion: v1
         kind: Service
         metadata:
         name: nginx-service
         spec:
         type: LoadBalancer
         selector:
           app: nginx
           ports:
              - protocol: TCP
                port: 8080
                targetPort: 80

  4. Apply the YAML file to the cluster using the following command:
         
         kubectl apply -f nginx-deployment.yaml
         

  5. Obtain the external IP address assigned to the service by the MetalLB load balancer using the following command:
         
         kubectl get services
         

The command returns output similar to the following:
         
         NAME            TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)          AGE
         nginx-service   LoadBalancer   10.51.195.25   10.100.68.104   8080:31966/TCP   11d
         




## Deploy a container with SR-IOV functions

The following example illustrates how to deploy a Pod that uses the SR-IOV [network function operator](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/network-function) features of Distributed Cloud connected.

### Create the Distributed Cloud networking components

Create the required networking components for your Distributed Cloud connected deployment as follows. For more information on these components, see [Distributed Cloud connected networking features](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/networking).

  1. Create a network:
         
         gcloud edge-cloud networking networks create NETWORK_NAME \
             --location=REGION \
             --zone=ZONE_NAME \
             --mtu=MTU_SIZE
         

Replace the following:

     * `NETWORK_NAME`: a descriptive name that uniquely identifies this network.
     * `REGION`: the Google Cloud region to which the target Distributed Cloud zone belongs.
     * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
     * `MTU_SIZE`: the maximum transmission unit (MTU) size for this network. Valid values are 1500 and 9000. This value must match the MTU size of the `default` network and be the same for all networks.
  2. Create a subnetwork:
         
         gcloud edge-cloud networking subnets create SUBNETWORK_NAME \
             --network=NETWORK_NAME \
             --ipv4-range=IPV4_RANGE \
             --vlan-id=VLAN_ID \
             --location=REGION \
             --zone=ZONE_NAME
         

Replace the following:

     * `SUBNETWORK_NAME`: a descriptive name that uniquely identifies this subnetwork.
     * `NETWORK_NAME`: the network that encapsulates this subnetwork.
     * `IPV4_RANGE`: the IPv4 address range that this subnetwork covers in the IP address/prefix format.
     * `VLAN_ID`: the target VLAN ID for this subnetwork.
     * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
     * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  3. Monitor the subnetwork's status until it has been successfully created:
         
         watch -n 30 'gcloud edge-cloud networking subnets list \
             --location=REGION \
             --zone=ZONE_NAME
         

Replace the following:

     * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
     * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.

The status progresses from `PENDING` to `PROVISIONING` and finally to `RUNNING`.

Record the VLAN ID, subnetwork CIDR block, and the gateway IP address for the CIDR block. You will use these values later in this procedure.




### Configure the `NodeSystemConfigUpdate` resources

Configure a `NodeSystemConfigUpdate` network function operator resource for each node in the cluster as follows.

  1. List the nodes running in the target cluster's node pool using the following command:
         
         kubectl get nodes | grep -v master
         

The command returns output similar to the following:
         
         NAME                                 STATUS   ROLES       AGE     VERSION
         pool-example-node-1-01-b2d82cc7      Ready    <none>      2d      v1.22.8-gke.200
         pool-example-node-1-02-52ddvfc9      Ready    <none>      2d      v1.22.8-gke.200
         

Record the returned node names and derive their short names. For example, for the `pool-example-node-1-01-b2d82cc7` node, its short name is `node101`.

  2. For each node you've recorded in the previous step, create a dedicated `NodeSystemConfigUpdate` resource file with the following contents:
         
         apiVersion: networking.gke.io/v1
         kind: NodeSystemConfigUpdate
         metadata:
         name: nodesystemconfigupdate-NODE_SHORT_NAME
         namespace: nf-operator
         spec:
         kubeletConfig:
           cpuManagerPolicy: Static
           topologyManagerPolicy: SingleNumaNode
         nodeName: NODE_NAME
         osConfig:
           hugePagesConfig:
              ONE_GB: 2
              TWO_MB: 0
           isolatedCpusPerSocket:
              "0": 40
              "1": 40
         sysctls:
           nodeLevel:
              net.core.rmem_max: "8388608"
              net.core.wmem_max: "8388608"

Replace the following:

     * `NODE_NAME`: the full name of the target node. For example, `pool-example-node-1-01-b2d82cc7`.
     * `NODE_SHORT_NAME`: the short name of the target node derived from its full name. For example, `node101`.

Name each file `node-system-config-update-NODE_SHORT_NAME.yaml`.

  3. Apply each of the `NodeSystemConfigUpdate` resource files to the cluster using the following command:
         
         kubectl apply -f node-system-config-update-NODE_SHORT_NAME.yaml
         

Replace `NODE_SHORT_NAME` with the short name of the corresponding target node. 

When you apply the resources to the cluster, each affected node reboots, which can take up to 30 minutes.

     1. Monitor the status of the affected nodes until all have successfully rebooted:
    
    kubectl get nodes | grep -v master
    

The status of each node transitions from `not-ready` to `ready` as their reboots complete.




### Configure the ToR switches for SR-IOV network functions

Follow the steps in this section to configure the network interfaces in each Distributed Cloud ToR switch in the Distributed Cloud connected rack for SR-IOV network functions operation.

  1. Create a file named `mlnc6-pcie1-tor1-sriov.yaml` with the following contents. This file configures the first network interface on the first ToR switch.
         
         apiVersion: sriovnetwork.k8s.cni.cncf.io/v1
           kind: SriovNetworkNodePolicy
           metadata:
           name: mlnx6-pcie1-tor1-sriov
           namespace: sriov-network-operator
           spec:
           deviceType: netdevice
           isRdma: false
           linkType: eth
           mtu: 9000
           nicSelector:
              pfNames:
              - enp59s0f0np0
           nodeSelector:
              edgecontainer.googleapis.com/network-sriov.capable: "true"
           numVfs: 31
           priority: 99
           resourceName: mlnx6_pcie1_tor1_sriov

  2. Create a file named `mlnc6-pcie1-tor2-sriov.yaml` with the following contents. This file configures the second network interface on the first ToR switch.
         
         apiVersion: sriovnetwork.k8s.cni.cncf.io/v1
           kind: SriovNetworkNodePolicy
           metadata:
           name: mlnx6-pcie1-tor2-sriov
           namespace: sriov-network-operator
           spec:
           deviceType: netdevice
           isRdma: false
           linkType: eth
           mtu: 9000
           nicSelector:
              pfNames:
              - enp59s0f1np1
           nodeSelector:
              edgecontainer.googleapis.com/network-sriov.capable: "true"
           numVfs: 31
           priority: 99
           resourceName: mlnx6_pcie1_tor2_sriov

  3. Create a file named `mlnc6-pcie2-tor1-sriov.yaml` with the following contents. This file configures the first network interface on the second ToR switch.
         
         apiVersion: sriovnetwork.k8s.cni.cncf.io/v1
           kind: SriovNetworkNodePolicy
           metadata:
           name: mlnx6-pcie2-tor1-sriov
           namespace: sriov-network-operator
           spec:
           deviceType: netdevice
           isRdma: false
           linkType: eth
           mtu: 9000
           nicSelector:
              pfNames:
              - enp216s0f0np0
           nodeSelector:
              edgecontainer.googleapis.com/network-sriov.capable: "true"
           numVfs: 31
           priority: 99
           resourceName: mlnx6_pcie2_tor1_sriov

  4. Create a file named `mlnc6-pcie2-tor2-sriov.yaml` with the following contents. This file configures the second network interface on the second ToR switch.
         
         apiVersion: sriovnetwork.k8s.cni.cncf.io/v1
           kind: SriovNetworkNodePolicy
           metadata:
           name: mlnx6-pcie2-tor2-sriov
           namespace: sriov-network-operator
           spec:
           deviceType: netdevice
           isRdma: false
           linkType: eth
           mtu: 9000
           nicSelector:
              pfNames:
              - enp216s0f1np1
           nodeSelector:
              edgecontainer.googleapis.com/network-sriov.capable: "true"
           numVfs: 31
           priority: 99
           resourceName: mlnx6_pcie2_tor2_sriov

  5. Apply the ToR configuration files to the cluster using the following commands:
         
         kubectl apply -f mlnc6-pcie1-tor1-sriov.yaml
         kubectl apply -f mlnc6-pcie1-tor2-sriov.yaml
         kubectl apply -f mlnc6-pcie2-tor1-sriov.yaml
         kubectl apply -f mlnc6-pcie2-tor2-sriov.yaml
         

The affected nodes are cordoned off, drained, and rebooted.

  6. Monitor the status of the nodes using the following command:
         
         watch -n 5 'kubectl get sriovnetworknodestates -o yaml -A | \ 
         grep "syncStatus\|pool-"|sed "N;s/\n/ /"'
         

When all affected nodes show `syncStatus: Succeeded`, press Ctrl+C to exit the monitoring command loop.

The command returns output similar to the following, indicating that the SR-IOV network function features have been enabled on the ToR switches:
         
         Allocated resources:
         (Total limits may be over 100 percent, i.e., overcommitted.)
         Resource                       Requests     Limits
         --------                       --------     ------
         cpu                            2520m (3%)   7310m (9%)
         memory                         3044Mi (1%)  9774Mi (3%)
         ephemeral-storage              0 (0%)       0 (0%)
         hugepages-1Gi                  0 (0%)       0 (0%)
         hugepages-2Mi                  0 (0%)       0 (0%)
         devices.kubevirt.io/kvm        0            0
         devices.kubevirt.io/tun        0            0
         devices.kubevirt.io/vhost-net  0            0
         gke.io/mlnx6_pcie1_tor1_sriov  3            3
         gke.io/mlnx6_pcie1_tor2_sriov  0            0
         gke.io/mlnx6_pcie2_tor1_sriov  0            0
         gke.io/mlnx6_pcie2_tor2_sriov  0            0
         




### Configure a `NetworkAttachmentDefinition` resource

Configure a `NetworkAttachmentDefinition` resource for the cluster as follows:

  1. Create a file named `network-attachment-definition.yaml` with the following contents:
         
         apiVersion: "k8s.cni.cncf.io/v1"
         kind: NetworkAttachmentDefinition
         metadata:
         name: sriov-net1
         annotations:
           k8s.v1.cni.cncf.io/resourceName: gke.io/mlnx6_pcie1_tor1_sriov
         spec:
         config: '{
         "type": "sriov",
         "cniVersion": "0.3.1",
         "vlan": VLAN_ID,
         "name": "sriov-network",
         "ipam": {
           "type": "host-local",
           "subnet": "SUBNETWORK_CIDR",
           "routes": [{
              "dst": "0.0.0.0/0"
           }],
           "gateway": "GATEWAY_ADDRESS"
         }
         }'




Replace the following:

  * `VLAN_ID`: the VLAN ID of the subnetwork you created earlier in this guide.
  * `SUBNETWORK_CIDR`: the CIDR block for the subnetwork.
  * `GATEWAY_ADDRESS`: the gateway IP address for the subnetwork.


  1. Apply the resource to the cluster using the following command:
         
         kubectl apply -f network-attachment-definition.yaml
         




### Deploy a Pod with SR-IOV network functions

Complete the steps in this section to deploy a Pod with SR-IOV network functions on the cluster. The `annotations` field in the Pod's configuration file specifies the name of the `NetworkAttachmentDefinition` resource you created earlier in this guide and the namespace in which it has been deployed (`default` in this example).

  1. Create a Pod specification file named `sriovpod.yaml` with the following contents:
         
         apiVersion: v1
              kind: Pod
              metadata:
              name: sriovpod
              annotations:
                 k8s.v1.cni.cncf.io/networks: default/sriov-net1
              spec:
              containers:
              - name: sleeppodsriov
                 command: ["sh", "-c", "trap : TERM INT; sleep infinity & wait"]
                 image: busybox
                 securityContext:
                    capabilities:
                    add:
                       - NET_ADMIN

  2. Apply the Pod specification file to the cluster using the following command:
         
         kubectl apply -f sriovpod.yaml
         

  3. Verify that the Pod has successfully started using the following command:
         
         kubectl get pods
         

  4. Establish a command-line shell for the Pod using the following command:
         
         kubectl exec -it sriovpod -- sh
         

  5. Confirm that the Pod is communicating with the ToR switches using the SR-IOV network function operator feature using the following command in the Pod shell:
         
         ip addr
         

The command returns output similar to the following:
         
         1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue qlen 1000
            link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
            inet 127.0.0.1/8 scope host lo
               valid_lft forever preferred_lft forever
            inet6 ::1/128 scope host 
               valid_lft forever preferred_lft forever
         51: net1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 9000 qdisc mq qlen 1000
            link/ether 2a:af:96:a5:42:ab brd ff:ff:ff:ff:ff:ff
            inet 192.168.100.11/25 brd 192.168.100.127 scope global net1
               valid_lft forever preferred_lft forever
         228: eth0@if229: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue qlen 1000
            link/ether 46:c9:1d:4c:bf:32 brd ff:ff:ff:ff:ff:ff
            inet 10.10.3.159/32 scope global eth0
               valid_lft forever preferred_lft forever
            inet6 fe80::44c9:1dff:fe4c:bf32/64 scope link 
               valid_lft forever preferred_lft forever
         

The information returned for the `net1` interface denotes that network connectivity between the ToR switches and the Pod has been established.




## Configure a Pod for image caching

You can configure a Pod running on a Distributed Cloud connected cluster to cache its image. The Pod begins using the cached image after it's been pulled from the repository for the first time. If the node hosting the Pod runs out of storage, new images are not cached and the existing image cache is purged to ensure your workloads continue to run uninterrupted.

Your Pod configuration must meet the following prerequisites:

  * You must set the `gdce.baremetal.cluster.gke.io/cache-image: true` label on the Pod.
  * If you're using a private image repository, your `ImagePullSecret` resource must be of type `kubernetes.io/dockerconfigjson`.
  * You must set the Pod's pull policy to `IfNotPresent` to ensure the cached copy of the target image is always used. If a cached copy is not available locally, the image is then pulled from the repository.



The following example illustrates a Pod configuration with caching enabled:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: cached-image-pod
      labels:
        gdce.baremetal.cluster.gke.io/cache-image: "true"
    spec:
      containers:
        - name: my-container
          image: your-private-image-repo/your-image:tag
          imagePullPolicy: IfNotPresent
      imagePullSecrets:
        - name: my-image-secret  # If using a private registry
    

The next example illustrates a Deployment configuration with caching enabled:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: cached-image-deployment
    spec:
      template:
        metadata:
          labels:
            gdce.baremetal.cluster.gke.io/cache-image: "true"
        spec:
          containers:
            - name: my-container
              image: your-private-image-repo/your-image:tag
              imagePullPolicy: IfNotPresent
          imagePullSecrets:
            - name: my-image-secret  # If using a private registry
    

## Limitations for Distributed Cloud workloads

When you configure your Distributed Cloud connected workloads, you must adhere to the limitations described in this section. These limitations are enforced by Distributed Cloud connected on all the workloads that you deploy on your Distributed Cloud connected hardware.

### Linux workload limitations

Distributed Cloud connected supports only the following [Linux capabilities](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container) for workloads:

  * `AUDIT_READ`
  * `AUDIT_WRITE`
  * `CHOWN`
  * `DAC_OVERRIDE`
  * `FOWNER`
  * `FSETID`
  * `IPC_LOCK`
  * `IPC_OWNER`
  * `KILL`
  * `MKNOD`
  * `NET_ADMIN`
  * `NET_BIND_SERVICE`
  * `NET_RAW`
  * `SETFCAP`
  * `SETGID`
  * `SETPCAP`
  * `SETUID`
  * `SYS_CHROOT`
  * `SYS_NICE`
  * `SYS_PACCT`
  * `SYS_PTRACE`
  * `SYS_RESOURCE`
  * `SYS_TIME`



### Namespace restrictions

Distributed Cloud connected does not support the following namespaces:

  * `hostPID`
  * `hostIPC`
  * `hostNetwork`



### Resource type restrictions

Distributed Cloud connected does not support the `CertificateSigningRequest` resource type, which allows a client to ask for an X.509 certificate to be issued, based on a signing request.

### Security context restrictions

Distributed Cloud connected does not support the privileged mode security context.

### Pod binding restrictions

Distributed Cloud connected does not support binding Pods to host ports in the `HostNetwork` namespace. Additionally, the `HostNetwork` namespace is not available.

### `hostPath` volume restrictions

Distributed Cloud connected only allows the following `hostPath` volumes with read/write access:

  * `/dev/hugepages`
  * `/dev/infiniband`
  * `/dev/vfio`
  * `/dev/char`
  * `/sys/devices`



### `PersistentVolumeClaim` resource type restrictions

Distributed Cloud connected only allows the following `PersistentVolumeClaim` resource types:

  * `csi`
  * `nfs`
  * `local`



### Volume type restrictions

Distributed Cloud connected only allows the following volume types:

  * `configMap`
  * `csi`
  * `downwardAPI`
  * `emptyDir`
  * `hostPath`
  * `nfs`
  * `persistentVolumeClaim`
  * `projected`
  * `secret`



### Pod toleration restrictions

Distributed Cloud connected does not allow user-created Pods on control plane nodes. Specifically, Distributed Cloud connected does not allow scheduling Pods that have the following toleration keys:

  * `""`
  * `node-role.kubernetes.io/master`
  * `node-role.kubernetes.io/control-plane`



### Impersonation restrictions

Distributed Cloud connected does not support user or group impersonation.

### Management namespace restrictions

Distributed Cloud connected does not allow access to the following namespaces:

  * `ai-system`
  * `ai-speech-system`
  * `ai-ocr-system`
  * `ai-translation-system`
  * `anthos-identity-service`
  * `cert-manager`
  * `dataproc-system`
  * `dataproc-`PROJECT_ID
  * `dns-system`
  * `g-istio-system`
  * `gke-connect`
  * `gke-managed-metrics-server`
  * `gke-operators`
  * `g-ospf-servicecontrol-system`
  * `g-ospf-system`
  * `g-pspf-system`
  * `gke-system`
  * `gpc-backup-system`
  * `iam-system`
  * `kube-node-lease`
  * `kube-public`
  * `kube-system` with the exception of deleting `ippools.whereabouts.cni.cncf.io`
  * `metallb-system` with the exception of editing `configMap` resources to set load-balancing IP address ranges
  * `nf-operator`
  * `oclcm-system`
  * `prediction`
  * `rm-system`
  * `robinio`
  * `saas-system`
  * `sriov-fec-system`
  * `sriov-network-operator`
  * `vm-system`



`PROJECT_ID` denotes the ID of the target Google Cloud project.

Avoid the use of any namespace with the `g-` prefix in its name. Such namespaces are typically a reserved namespace used by Distributed Cloud connected.

### Webhook restrictions

Distributed Cloud connected restricts webhooks as follows:

  * Any mutating webhook that you create automatically excludes the `kube-system` namespace.
  * Mutating webhooks are disabled for the following resource types: 
    * `nodes`
    * `persistentvolumes`
    * `certificatesigningrequests`
    * `tokenreviews`



### Pod priority restrictions

Distributed Cloud connected requires that you set the priority of your workload Pods to a value lower than `500000000`.

## What's next

  * [Apply security best practices](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/security)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
