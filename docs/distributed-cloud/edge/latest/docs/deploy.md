---
url: https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/deploy/
title: Deploy workloads \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:27:44.308346+00:00
---

# Deploy workloads  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/deploy/

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
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)



Send feedback 

#  Deploy workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to deploy workloads on your Google Distributed Cloud connected hardware and the limitations that you must adhere to when configuring your workloads.

Before you complete these steps, you must [meet the Distributed Cloud connected installation requirements](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/requirements) and [order the Distributed Cloud hardware](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/order).

When the Google Distributed Cloud connected hardware arrives at your chosen destination, it is pre-configured with hardware, Google Cloud, and some network settings that you specified when you ordered Distributed Cloud connected.

Your Google-certified systems integrator completes the physical installation, and your system administrator connects Distributed Cloud connected to your local network.

After the hardware is connected to your local network, it communicates with Google Cloud to download software updates and connect with your Google Cloud project. You are then ready to provision node pools and deploy workloads on Distributed Cloud connected.

## Deployment overview

To deploy a workload on your Distributed Cloud connected hardware, complete the following steps:

  1. Optional: [Enable the Distributed Cloud Edge Network API](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networking#network-api-enable).

  2. Optional: [Initialize the network configuration of your Distributed Cloud connected zone](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/zones#init).

  3. Optional: [Configure Distributed Cloud networking](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networking#network-configure).

  4. [Create a Distributed Cloud connected cluster](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/clusters#create). You can [monitor the provisioning progress](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/clusters#monitor-provisioning) to ensure the cluster is ready before proceeding.

  5. Optional: [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/security#cmek) if you want to integrate with Cloud Key Management Service to enable support for CMEK for your workload data. For information about how Distributed Cloud connected encrypts workload data, see [Local storage security](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/security#storage).

  6. [Create a node pool](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/nodepools#create). In this step, you assign nodes to a node pool and optionally configure the node pool to use Cloud KMS to wrap and unwrap the Linux Unified Key Setup (LUKS) passphrase for encrypting workload data.

  7. [Obtain credentials for a cluster](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/clusters#credentials) to test the cluster.

  8. Grant users access to the cluster by assigning them the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) or the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) on the project.

  9. [Assign users granular role-based access to the cluster resources by using `RoleBinding` and `ClusterRoleBinding`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

  10. Optional: [Configure VM Runtime on GDC to run workloads on virtual machines on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/overview).

  11. Optional: [Enable GPU support to run GPU-based workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/gpu).




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
  * `anthos-creds`
  * `anthos-identity-service`
  * `capi-system`
  * `capi-kubeadm-bootstrap-system`
  * `cert-manager`
  * `cert-manager-cluster-resources`
  * `dataproc-system`
  * `dataproc-`PROJECT_ID
  * `dns-system`
  * `g-istio-system`
  * `gke-connect`
  * `gke-managed-metrics-server`
  * `gke-operators`
  * `gke-system`
  * `gpu-system`
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
  * `prom-monitoring`
  * `rm-system`
  * `robinio`
  * `robin-admin`
  * `saas-system`
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



## Configure the runtime class for a Pod

Distributed Cloud connected lets you specify the runtime class for a Pod in its configuration using the `runtimeClassName` field. This overrides the default runtime class specified at cluster level. The available runtime classes are `runc` and `gvisor`. For example:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: myPod
    spec:
      runtimeClassName: gvisor
      containers:
      - name: myPod
        image: myPodImage
      restartPolicy: OnFailure
    

If you omit this in your Pod configuration, the Pod uses the class specified at the cluster level. The default cluster-level runtime class is `runc` unless you configure a default runtime class using the `--default-container-runtime` parameter as described in [Create and manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/clusters).

If you change the runtime class at either Pod or cluster level, you must restart the affected Pods for the change to take effect.

### `gvisor` runtime class

Specifying the `gvisor` runtime class switches the Pod to the Open Container Initiative (OCI) secure runtime based on [gVisor](https://gvisor.dev/). gVisor is a sandboxing solution that introduces strong isolation between the workload and its host.

## Configure VPC Service Controls integration

Complete the steps in this section to configure the integration of the Distributed Cloud Edge Container API with VPC Service Controls. For more information, see the following:

  * [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview)

  * [Access levels: IP address](https://docs.cloud.google.com/access-context-manager/docs/overview#ip-address)

  * [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies)




## Specify the runtime priority for a Pod

Distributed Cloud connected lets you specify a priority class for a Pod in its configuration using the `priorityClassName` field. This field accepts the name of a `PriorityClass` resource that specifies the target priority. For example:
    
    
    kind: PriorityClass
    metadata:
      name: high-priority-class
    value: 5100000
    globalDefault: false
    description: "High priority class for user workloads."
    

Specify the name of the priority class in your Pod configuration as shown in the following example:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: myPod
    spec:
      priorityClassName: high-priority-class
      containers:
      - name: myPod
        image: myPodImage 
      restartPolicy: OnFailure
    

Specifying a priority class overrides the default Pod priority of 0. For critical workloads, set their priority to a value between `5000001` and `1000000000`. Distributed Cloud connected automatically preempts lower priority workloads.

## Required egress rules

You must configure the egress rules described in this section to integrate the Distributed Cloud Edge Container API with VPC Service Controls. For information about egress rule syntax, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

### Access to the machine zone and Google Cloud project

This rule allows the calling identity to access the machine zone and Google Cloud project when making calls using the Distributed Cloud Edge Container API. This rule applies when the machine and the cluster don't reside in the same Google Cloud project and the machine Google Cloud project is outside the perimeter. This rule is required if you've restricted the Distributed Cloud Edge Container API inside the perimeter using VPC Service Controls.

The following is an example of an `egressFrom` configuration for this rule in JSON format:
    
    
    egressFrom:
      identityType: ANY_SERVICE_ACCOUNT
      sources:
        - accessLevel: "*"
    

The following is an example of an `egressTo` configuration for this rule:
    
    
    egressTo:
     resources:
     - "projects/280968151686"
     operations:
       - serviceName: "edgecontainer.googleapis.com"
         methodSelectors:
           - method: "*"
    

## Required ingress rules

You must configure the ingress rules described in this section to integrate the Distributed Cloud Edge Container API with VPC Service Controls. For information about ingress rule syntax, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

### Access to the Distributed Cloud Edge Container API

This rule allows specific identities to access and interact with the Distributed Cloud Edge Container API. You must configure this rule if you've restricted the Distributed Cloud Edge Container API inside the perimeter using VPC Service Controls and the identity calling the Distributed Cloud Edge Container API is outside the perimeter.

The following is an example of an `ingressFrom` configuration for this rule:
    
    
    ingressFrom:
       sources:
         - accessLevel: '*'
       identities:
         - serviceAccount:testuser@kubernetesedge-e2e-testing.iam.gserviceaccount.com
    

The following is an example of an `ingressTo` configuration for this rule:
    
    
    ingressTo:
     resources:
     - "*"
     operations:
       - serviceName: "edgecontainer.googleapis.com"
         methodSelectors:
           - method: "*"
    

### Access to the Connect API and the Security Token Service API

This rule allows workloads to access the Connect API and the Security Token Service API. You must configure this rule if you've restricted access to the Connect API and the Security Token Service API inside the perimeter using VPC Service Controls. For information about setting up access policies at the IP address level, see [IP address](https://docs.cloud.google.com/access-context-manager/docs/overview#ip-address).

The following is an example of an `ingressFrom` configuration for this rule:
    
    
    - ingressFrom:
       identityType: ANY_IDENTITY
       sources:
         - accessLevel: "accessPolicies/100637171436/accessLevels/fwi"
    

The following is an example of an `ingressTo` configuration for this rule:
    
    
    ingressTo:
       resources:
       - "*"
       operations:
         - serviceName: "gkeconnect.googleapis.com"
           methodSelectors:
             - method: "*"
         - serviceName: "sts.googleapis.com"
           methodSelectors:
             - method: "*"
    

## What's next

  * [Apply security best practices](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/security)
  * [Use fleet packages in Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/fleet-packages-guide)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
