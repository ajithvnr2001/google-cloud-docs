---
url: https://docs.cloud.google.com/filestore/docs/optimize-multishares/
title: Optimize storage with Filestore Multishares for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:56.439270+00:00
---

# Optimize storage with Filestore Multishares for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/optimize-multishares/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Optimize storage with Filestore Multishares for GKE Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to use Filestore multishares for Google Kubernetes Engine with the GKE Filestore CSI driver.

## Before you begin

  1. Before you begin, complete the [setup steps](https://docs.cloud.google.com/filestore/docs/install) needed to use Filestore.

  2. Enable the [GKE Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver), version 1.23 or later:

     * Driver versions 1.23 through 1.26 support up to 10 shares per instance.

     * Driver versions 1.27 or later support up to 80 shares per instance.

For the latest GKE Filestore CSI driver requirements, see [Access Filestore instances with the Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/csi-driver#requirements).




## Use Filestore multishares with multiple applications

This section shows you how to deploy two applications, one [Deployment](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/deployment) and one [Statefulset](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset), each using a Filestore multishares [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/). You'll also see how GKE [bin packs](https://cloud.google.com/blog/products/containers-kubernetes/gke-best-practices-to-lessen-over-provisioning) (a process to efficiently pack applications into your GKE nodes) all volumes in the same underlying Filestore enterprise instance.

  1. Use the GKE-provided StorageClass, `enterprise-multishare-rwx`, to create instances that support up to 10 shares.

     * If you want to create instances that support up to 80 shares, you'll need to create a custom StorageClass. For the purpose of this guide, you will use a StorageClass with a ten-share-per-instance limit.

After the GKE Filestore CSI driver is enabled, users can access the GKE-provided multishare StorageClass `enterprise-multishare-rwx` with the following configuration. Referencing this StorageClass, the GKE Filestore CSI driver uses [dynamic volume provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/) to automatically create Persistent Volumes (PVs) for new Persistent Volume Claims (PVCs) as GKE workload demand requires:
    
    kubectl describe sc enterprise-multishare-rwx
    Name:                  enterprise-multishare-rwx
    IsDefaultClass:        No
    Annotations:           components.gke.io/component-name=filestorecsi,components.gke.io/component-version=0.7.2,components.gke.io/layer=addon
    Provisioner:           filestore.csi.storage.gke.io
    Parameters:            instance-storageclass-label=enterprise-multishare-rwx,multishare=true,tier=enterprise
    AllowVolumeExpansion:  True
    MountOptions:          <none>
    ReclaimPolicy:         Delete
    VolumeBindingMode:     WaitForFirstConsumer
    Events:                <none>
    




### Create a custom StorageClass

If you want to take advantage of the latest capacity limit of up to 80 shares per Filestore instance, create a custom StorageClass based on the following template:
    
    
      apiVersion: storage.k8s.io/v1
      kind: StorageClass
      metadata:
        name: csi-filestore-multishare-128
      provisioner: filestore.csi.storage.gke.io
      parameters:
        tier: enterprise
        multishare: "true"
        max-volume-size: "128Gi"
        network: default
      allowVolumeExpansion: true
    

When renaming the StorageClass, consider the following requirements:

  * The StorageClass name must be a valid [DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

  * The multishare StorageClass name is also used as an instance label and should follow [label naming guidelines](https://docs.cloud.google.com/filestore/docs/managing-labels).

  * If your application requires immediate volume provisioning, include the `Immediate` volume binding mode:

`volumeBindingMode: Immediate`

Use this specification, for example, if you don't want volume provisioning to be dependent upon pod creation in the GKE cluster.

  * Beginning as of driver version 1.27, if you want to assign more than 10 shares per instance, include the `max-volume-size` parameter and assign it one of the accepted values from the first column:

Maximum volume size (share size) | Maximum number of shares per instance  
---|---  
128 GiB | 80  
256 GiB | 40  
512 GiB | 20  
1024 GiB | 10  
  
So for example, adding the key-value pair `max-volume-size: "128Gi"` ensures the StorageClass maps up to 80 shares—each ranging from 10 GiB to 128 GiB in size—to a single 10 TiB enterprise-tier instance.

    * This capability is backward compatibility with Filestore instances created by GKE Filestore CSI driver versions 1.23 through 1.26.

    * Existing instances can create new PVCs, or shares, with the extended minimum share size of 10 GiB.

    * GKE Filestore CSI driver version 1.27, or later, recognizes legacy enterprise instances and assigns them a default maximum share size of 1024 GiB (1 TiB). As a result, legacy instances are limited to a maximum share count of 10 shares per instance.

For more information, see [Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares).



  1. Create a Deployment with multiple pod replicas using a single PVC.

Create a YAML configuration file similar to the following:
         
         cat <<EOF | kubectl apply -f -
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: web-server-multishare
           labels:
             app: nginx
         spec:
           replicas: 5
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
                 image: nginx
                 volumeMounts:
                 - mountPath: /usr/share/nginx/html
                   name: mypvc
               volumes:
               - name: mypvc
                 persistentVolumeClaim:
                   claimName: test-pvc-fs
         ---
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: test-pvc-fs
         spec:
           accessModes:
             - ReadWriteMany
           storageClassName: enterprise-multishare-rwx
           resources:
             requests:
               storage: 100Gi
         
         EOF
         

  2. Check pod replicas.

a. From the command line, run the following command to check the PVC status:
         
         kubectl get pvc
         

You should see something similar to the following response:
         
         NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS               AGE
         test-pvc-fs   Bound    pvc-056d769d-a709-4bb2-b6d3-0361871b27a2   100Gi      RWX            enterprise-multishare-rwx  35m
         

b. From the command line, run the following command to check the pod status:
         
         kubectl get pod
         

You should see something similar to the following response:
         
         NAME                                     READY   STATUS    RESTARTS   AGE
         web-server-multishare-76c9ffb4b5-2dhml   1/1     Running   0          35m
         web-server-multishare-76c9ffb4b5-7mtcb   1/1     Running   0          35m
         web-server-multishare-76c9ffb4b5-csdbd   1/1     Running   0          35m
         web-server-multishare-76c9ffb4b5-rgx82   1/1     Running   0          35m
         web-server-multishare-76c9ffb4b5-zjl27   1/1     Running   0          35m
         

  3. Scale replicas.

a. From the command line, run the following command to edit the Deployment:
         
         kubectl edit deployment web-server-multishare
         

b. The file will open in the command line. Find the `spec.replicas` field and update the value to `10`.

c. From the command line, run the following command to see the applied change:
         
         kubectl get pod
         

You should see something similar to the following response:
         
         NAME                                     READY   STATUS    RESTARTS   AGE
         web-server-multishare-76c9ffb4b5-2dhml   1/1     Running   0          36m
         web-server-multishare-76c9ffb4b5-5ctkf   1/1     Running   0          3s
         web-server-multishare-76c9ffb4b5-7mtcb   1/1     Running   0          36m
         web-server-multishare-76c9ffb4b5-8dwmw   1/1     Running   0          2s
         web-server-multishare-76c9ffb4b5-csdbd   1/1     Running   0          36m
         web-server-multishare-76c9ffb4b5-lndcq   1/1     Running   0          2s
         web-server-multishare-76c9ffb4b5-rgx82   1/1     Running   0          36m
         web-server-multishare-76c9ffb4b5-vtd6p   1/1     Running   0          3s
         web-server-multishare-76c9ffb4b5-xm49s   1/1     Running   0          3s
         web-server-multishare-76c9ffb4b5-zjl27   1/1     Running   0          36m
         

Notice 10 pods are running.

d. From the command line, run the following command:
         
         kubectl get deployment
         

You should see something similar to the following response:
         
         NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
         web-server-multishare   10/10   10           10          36m
         

e. From the command line, run the following command to check the PVC bound status:
         
         kubectl get pvc
         

You should see something similar to the following response:
         
         NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS               AGE
         test-pvc-fs   Bound    pvc-056d769d-a709-4bb2-b6d3-0361871b27a2   100Gi      RWX            enterprise-multishare-rwx  37m
         

f. From the command line, run the following command to edit the Deployment:
         
         kubectl edit deployment web-server-multishare
         

g. The file will open in the command line. Find the `spec.replicas` field and update the value to `2`.

h. From the command line, run the following command to see the applied change:
         
         kubectl get pod
         

You should see something similar to the following response:
         
         NAME                                     READY   STATUS    RESTARTS   AGE
         web-server-multishare-76c9ffb4b5-2dhml   1/1     Running   0          38m
         web-server-multishare-76c9ffb4b5-7mtcb   1/1     Running   0          38m
         

  4. Deploy a Statefulset.

Deploy a second application that shares the underlying Filestore instance.

To do so, provision 200 GiB of space and validate that it uses the same underlying Filestore instance as the first application.

You'll then scale the application to nine replicas using 900 GiB in total (9 replicas using 100 GiB each) and verify that GKE uses the same Filestore instance by sharing the instance.

Create a YAML configuration file similar to the following:
         
         cat <<EOF | kubectl apply -f -
         
         apiVersion: apps/v1
         kind: StatefulSet
         metadata:
           name: web
         spec:
           serviceName: "nginx"
           replicas: 2
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
                 image: registry.k8s.io/nginx-slim:0.8
                 ports:
                 - containerPort: 80
                   name: web
                 volumeMounts:
                 - name: test-pvc-multishare
                   mountPath: /usr/share/nginx/html
           volumeClaimTemplates:
           - metadata:
               name: test-pvc-multishare
             spec:
               accessModes: [ "ReadWriteMany" ]
               storageClassName: enterprise-multishare-rwx
               resources:
                 requests:
                   storage: 100Gi
         
         EOF
         
         

  5. Check Statefulset replicas and volumes.

From the command line, run the following command:
         
         kubectl get pod
         

You should see something similar to the following response:
         
         NAME                                     READY   STATUS    RESTARTS   AGE
         web-0                                    1/1     Running   0          4m48s
         web-1                                    1/1     Running   0          3m32s
         web-server-multishare-76c9ffb4b5-2dhml   1/1     Running   0          57m
         web-server-multishare-76c9ffb4b5-7mtcb   1/1     Running   0          57m
         

Notice that the first two pods are associated with the Statefulset. The last two pods are associated with the Deployment.

From the command line, run the following command:
         
         kubectl get statefulset
         

You should see something similar to the following response:
         
         NAME   READY   AGE
         web    2/2     2m8s
         

From the command line, run the following command:
         
         kubectl get pvc
         

You should see something similar to the following response:
         
         NAME                        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS               AGE
         test-pvc-fs                 Bound    pvc-056d769d-a709-4bb2-b6d3-0361871b27a2   100Gi      RWX            enterprise-multishare-rwx   54m
         test-pvc-multishare-web-0   Bound    pvc-7aa21b5a-5343-4547-b7d7-414c16af15a7   100Gi      RWX            enterprise-multishare-rwx   114s
         test-pvc-multishare-web-1   Bound    pvc-8b37cd6e-d764-4d38-80d7-d74228536cfe   100Gi      RWX            enterprise-multishare-rwx   38s
         

The PVC `test-pvc-fs` is associated with the Deployment `web-server-multishare`.

The PVCs `test-pvc-multishare-web-0` and `test-pvc-multishare-web-1` are associated with the Statefulset.

  6. Scale the Statefulset replicas.

Increase the replica count to nine. As the count increases, the corresponding PVCs are created.

a. From the command line, run the following command:
         
         kubectl  edit statefulset web
         

b. The file will open in the command line. Find the `spec.replicas` field and update the value to `9`.

c. From the command line, run the following command to see the applied change:
         
         kubectl get statefulset
         

You should see something similar to the following response:
         
         NAME   READY   AGE
         web    9/9     13m
         

d. From the command line, run the following command:
         
         kubectl get deployment
         

You should see something similar to the following response:
         
         NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
         web-server-multishare   2/2     2            2           65m
         

e. From the command line, run the following command:
         
         kubectl get pvc
         

You should see something similar to the following response:
         
         NAME                        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS               AGE
         test-pvc-fs                 Bound    pvc-056d769d-a709-4bb2-b6d3-0361871b27a2   100Gi      RWX            enterprise-multishare-rwx   65m
         test-pvc-multishare-web-0   Bound    pvc-7aa21b5a-5343-4547-b7d7-414c16af15a7   100Gi      RWX            enterprise-multishare-rwx   13m
         test-pvc-multishare-web-1   Bound    pvc-8b37cd6e-d764-4d38-80d7-d74228536cfe   100Gi      RWX            enterprise-multishare-rwx   12m
         test-pvc-multishare-web-2   Bound    pvc-3fcbd132-939f-4364-807a-7c8ac6a3e64e   100Gi      RWX            enterprise-multishare-rwx   5m12s
         test-pvc-multishare-web-3   Bound    pvc-5894afa5-2502-4ee7-9d5c-b7378cb85479   100Gi      RWX            enterprise-multishare-rwx   4m57s
         test-pvc-multishare-web-4   Bound    pvc-ebbe452b-bc8f-4624-a830-a2094cce0d67   100Gi      RWX            enterprise-multishare-rwx   4m36s
         test-pvc-multishare-web-5   Bound    pvc-5a73a698-d174-44cb-a3a1-e767966c3417   100Gi      RWX            enterprise-multishare-rwx   4m20s
         test-pvc-multishare-web-6   Bound    pvc-102da6a9-2ca6-4f9e-9896-8fe14709db7a   100Gi      RWX            enterprise-multishare-rwx   3m55s
         test-pvc-multishare-web-7   Bound    pvc-160e81cd-c5bf-4ae6-966e-518e8249e02d   100Gi      RWX            enterprise-multishare-rwx   3m38s
         test-pvc-multishare-web-8   Bound    pvc-9b52d773-2e9a-40de-881c-dc06945ba3d7   100Gi      RWX            enterprise-multishare-rwx   118s
         

  7. Verify the Filestore instance state.

You now have a Deployment with two replica pods, and a Statefulset with nine replica pods, and a total of 10 PVCs, each 100 GiB in size. All of the volumes are packed onto a single Filestore multishare instance.

a. From the command line, run the following [`instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/instances/list) command:
         
         gcloud beta filestore instances list --project=YOUR_PROJECT_ID --region=REGION
         

where:

     * YOUR_PROJECT_ID is the name of the [project](https://docs.cloud.google.com/filestore/docs/install) being used. For example, `my-project`.

     * REGION is the name of the [region](https://docs.cloud.google.com/filestore/docs/regions) being used. For example, `us-central1`.

You should see something similar to the following response:
    
    INSTANCE_NAME                            LOCATION     TIER        CAPACITY_GB  FILE_SHARE_NAME  IP_ADDRESS   STATE  CREATE_TIME
    fs-a767cef8-738e-4c8e-b70b-09cbb872d016  us-central1  ENTERPRISE  1024         N/A              10.192.53.2  READY  2022-06-21T21:15:30
    

b. From the command line, run the following [`instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/instances/describe) command:
    
    gcloud filestore instances describe fs-a767cef8-738e-4c8e-b70b-09cbb872d016 --project=YOUR_PROJECT_ID --region=REGION
    capacityGb: '1024'
    capacityStepSizeGb: '256'
    createTime: '2022-06-21T21:15:30.464237089Z'
    labels:
      storage_gke_io_created-by: filestore_csi_storage_gke_io
      storage_gke_io_storage-class-id: enterprise-multishare-rwx
    maxCapacityGb: '10240'
    maxShareCount: '10'
    multiShareEnabled: true
    name: projects/YOUR_PROJECT_ID/locations/REGION/instances/fs-a767cef8-738e-4c8e-b70b-09cbb872d016
    networks:
    - connectMode: DIRECT_PEERING
      ipAddresses:
      - 10.192.53.2
      modes:
      - MODE_IPV4
      network: csi-filestore-test-network
      reservedIpRange: 10.192.53.0/26
    state: READY
    tier: ENTERPRISE
    
    

where:

     * YOUR_PROJECT_ID is the name of the [project](https://docs.cloud.google.com/filestore/docs/install) being used. For example, `my-project`.

     * REGION is the name of the [region](https://docs.cloud.google.com/filestore/docs/regions) being used. For example, `us-central1`.




## Expand a PVC and verify the Filestore instance

This section shows you how to expand an existing PVC and verify the Filestore instance size.

  1. Expand a PVC.

PVCs—backed by shares in a Filestore multishare instance— can grow to the maximum size specified in the `max-volume-size` parameter. To verify this, expand one of the volumes associated with the Statefulset while the pod is using it.

From the command line, run the following command to check the current PVC size of replica 0:
         
         kubectl get pvc test-pvc-multishare-web-0 -o json
         {
             "apiVersion": "v1",
             "kind": "PersistentVolumeClaim",
             "metadata": {
                 "annotations": {
                     "pv.kubernetes.io/bind-completed": "yes",
                     "pv.kubernetes.io/bound-by-controller": "yes",
                     "volume.beta.kubernetes.io/storage-provisioner": "filestore.csi.storage.gke.io",
                     "volume.kubernetes.io/storage-provisioner": "filestore.csi.storage.gke.io"
                 },
                 "creationTimestamp": "2022-06-21T22:07:42Z",
                 "finalizers": [
                     "kubernetes.io/pvc-protection"
                 ],
                 "labels": {
                     "app": "nginx"
                 },
                 "name": "test-pvc-multishare-web-0",
                 "namespace": "default",
                 "resourceVersion": "48395",
                 "uid": "7aa21b5a-5343-4547-b7d7-414c16af15a7"
             },
             "spec": {
                 "accessModes": [
                     "ReadWriteMany"
                 ],
                 "resources": {
                     "requests": {
                         "storage": "100Gi"
                     }
                 },
                 "storageClassName": "enterprise-multishare-rwx",
                 "volumeMode": "Filesystem",
                 "volumeName": "pvc-7aa21b5a-5343-4547-b7d7-414c16af15a7"
             },
             "status": {
                 "accessModes": [
                     "ReadWriteMany"
                 ],
                 "capacity": {
                     "storage": "100Gi"
                 },
                 "phase": "Bound"
             }
         }
         
         

  2. From the command line, run the following command to increase the size to 500 GiB:
         
         kubectl edit pvc test-pvc-multishare-web-0
         

  3. The file will open in the command line. Find the `spec.resources.requests.storage` field and update the value to `500Gi`.

  4. From the command line, run the following command to see the applied change:
         
         kubectl get pvc test-pvc-multishare-web-0
         

You should see something similar to the following response:
         
         NAME                        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS               AGE
         test-pvc-multishare-web-0   Bound    pvc-7aa21b5a-5343-4547-b7d7-414c16af15a7   500Gi      RWX            enterprise-multishare-rwx   28m
         

The Filestore CSI driver accepted the request, first expanding the underlying Filestore instance, and then expanding the share backing the PVC.

Specifically, the Filestore CSI driver automatically expanded the instance to 1536 Gi to accommodate the new share size of 500Gi.

  5. From the command line, run the following [`instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/instances/describe) command to verify the capacity of the Filestore instance:
         
         gcloud filestore instances describe fs-a767cef8-738e-4c8e-b70b-09cbb872d016 --project=YOUR_PROJECT_ID --region=REGION
         capacityGb: '1536'
         capacityStepSizeGb: '256'
         createTime: '2022-06-21T21:15:30.464237089Z'
         labels:
           storage_gke_io_created-by: filestore_csi_storage_gke_io
           storage_gke_io_storage-class-id: enterprise-multishare-rwx
         maxCapacityGb: '10240'
         maxShareCount: '10'
         multiShareEnabled: true
         name: projects/YOUR_PROJECT_ID/locations/us-central1/instances/fs-a767cef8-738e-4c8e-b70b-09cbb872d016
         networks:
         - connectMode: DIRECT_PEERING
           ipAddresses:
           - 10.192.53.2
           modes:
           - MODE_IPV4
           network: csi-filestore-test-network
           reservedIpRange: 10.192.53.0/26
         state: READY
         tier: ENTERPRISE
         

where:

     * YOUR_PROJECT_ID is the name of the [project](https://docs.cloud.google.com/filestore/docs/install) being used. For example, `my-project`.

     * REGION is the name of the [region](https://docs.cloud.google.com/filestore/docs/regions) being used. For example, `us-central1`.




## Dynamic provisioning on a Shared VPC

Filestore CSI driver for GKE supports [dynamic provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/) of volumes in a service project under a Shared VPC. The following section shows how to use the Filestore CSI driver to dynamically provision volumes on Filestore multishare instances in a service project under a Shared VPC network.

  1. Complete the [setup steps](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-xpn) for a Shared VPC network and private service access.

  2. Create a StorageClass to dynamically provision volumes backed by a Filestore multishares instance on a Shared VPC.

Run the following command to deploy a `StorageClass` resource:
         
         cat <<EOF | kubectl apply -f -
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: csi-filestore-multishare-sharedvpc
         provisioner: filestore.csi.storage.gke.io
         parameters:
           network: "projects/HOST_PROJECT_ID/global/networks/SHARED_VPC_NAME"
           connect-mode: PRIVATE_SERVICE_ACCESS
           tier: enterprise
           multishare: "true"
         allowVolumeExpansion: true
         
         EOF
         

where:

     * HOST_PROJECT_ID is the ID or name of the host [project](https://docs.cloud.google.com/filestore/docs/install) of the Shared VPC network. For example, `my-host-project`.

     * SHARED_VPC_NAME the name of the [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc). For example, `my-shared-vpc`.

If you want to deploy your resource within a reserved IP address range, add the following line to the parameters used in the command:
    
    reserved-ip-range: RESERVED_NAME
    

Where RESERVED_NAME is the name of the reserved IP address range within which a Filestore instance can be provisioned. For example, `filestore-reserved-ip-range`. If a reserved IP range is specified, it must be a named address range instead of a direct CIDR value.

For more information, see [Allocate IP address ranges](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#allocating-range) or [Configuring a reserved IP address range](https://docs.cloud.google.com/filestore/docs/creating-instances#configuring_a_reserved_ip_address_range). To see an example of how to create a reserved name using the Google Cloud console, see [Create an IP allocation](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#procedure).

  3. Create a Deployment.

Run the following command to create a `Deployment` resource:
         
         cat <<EOF | kubectl apply -f -
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: web-server-multishare
           labels:
             app: nginx
         spec:
           replicas: 5
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
                 image: nginx
                 volumeMounts:
                 - mountPath: /usr/share/nginx/html
                   name: mypvc
               volumes:
               - name: mypvc
                 persistentVolumeClaim:
                   claimName: test-pvc-fs-sharedvpc
         ---
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: test-pvc-fs-sharedvpc
         spec:
           accessModes:
             - ReadWriteMany
           storageClassName: csi-filestore-multishare-sharedvpc
           resources:
             requests:
               storage: 100Gi
         
         EOF
         




## CMEK-enabled Filestore instances

You can create GKE volumes hosted on CMEK-enabled Filestore multishare instances. In this section, you'll see how to setup a [customer-managed encryption key (CMEK) for your Filestore instance](https://docs.cloud.google.com/filestore/docs/cmek).

Customer-managed key details can be provided in the StorageClass. Any instance dynamically created by the Filestore CSI driver, which references this StorageClass, will have CMEK enabled.

  1. Create a CMEK-enabled StorageClass.

a. Run the following command:
         
         cat <<EOF | kubectl apply -f -
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: csi-filestore-multishare-cmek
         provisioner: filestore.csi.storage.gke.io
         parameters:
           tier: enterprise
           multishare: "true"
           instance-encryption-kms-key: projects/KEY_PROJECT_ID/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
         
         allowVolumeExpansion: true
         
         EOF
         

where:

     * KEY_PROJECT_ID is the name of the [project](https://docs.cloud.google.com/filestore/docs/install) where the key is located. For example, `my-key-project`.

     * REGION is the name of the [region](https://docs.cloud.google.com/filestore/docs/regions) being used. For example, `us-central1`.

     * RING_NAME the key ring name. For example, `my-key-ring-name`.

     * KEY_NAME the key name. For example, `my-key-name`.

  2. Create a Deployment.

b. Run the following command to create a `Deployment` resource:
         
         cat <<EOF | kubectl apply -f -
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: web-server-multishare
           labels:
             app: nginx
         spec:
           replicas: 5
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
                 image: nginx
                 volumeMounts:
                 - mountPath: /usr/share/nginx/html
                   name: mypvc
               volumes:
               - name: mypvc
                 persistentVolumeClaim:
                   claimName: test-pvc-fs-cmek
         ---
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: test-pvc-fs-cmek
         spec:
           accessModes:
             - ReadWriteMany
           storageClassName: csi-filestore-multishare-cmek
           resources:
             requests:
               storage: 100Gi
         
         EOF
         




## Map PVCs to Filestore instances

**Note:** Filestore multishare instances are managed using CSI dynamic provisioning. Instance or share creation can take several minutes to complete. Once the Filestore resource is created, Kubernetes creates the associated PV. This means the volume is not visible until the create operation initiated by the CSI driver completes.

In this section, you'll see how to map your PVCs to your Filestore instances.

With Filestore multishare instances, each PVC is hosted on a Filestore instance by the Filestore CSI driver. The details of the underlying Filestore instance hosting the volume and the share representing the Kubernetes volume, is captured in the `volumeHandle` field of the Persistent Volumes specification. The volume handle format is as follows:
    
    
    modeMultishare/<storageclass-prefix>/<project>/<region>/<filestore-instance-name>/<filestore-share-name>
    

The following `kubectl` command can be used to quickly determine the mappings between a PVC, PV, Filestore Instance, and a Filestore share.

From the command line, run the following command:
    
    
    kubectl get pv -o jsonpath='{range .items[*]}{"pv="}{.metadata.name}{",pvc="}{.spec.claimRef.name}{",volumeHandle="}{.spec.csi.volumeHandle}{"\n"}{end}'
    

You should see something similar to the following response:
    
    
    pv=pvc-67ad9abd-f25e-4130-b7ca-64d28bd29525,pvc=test-pvc-multishare,volumeHandle=modeMultishare/csi-filestore-multishare-sharedvpc/YOUR_PROJECT_ID/us-central1/fs-2109f680-3f04-4ada-b4bc-2a1c7fc47b88/pvc_67ad9abd_f25e_4130_b7ca_64d28bd29525
    
    pv=pvc-c80f4de0-9916-4957-b8ae-b21206650ac0,pvc=test-pvc-fs-sharedvpc,volumeHandle=modeMultishare/csi-filestore-multishare-sharedvpc/YOUR_PROJECT_ID/us-central1/fs-2109f680-3f04-4ada-b4bc-2a1c7fc47b88/pvc_c80f4de0_9916_4957_b8ae_b21206650ac0
    

where:

  * YOUR_PROJECT_ID is the name of the [project](https://docs.cloud.google.com/filestore/docs/install) being used. For example, `my-project`.



Notice that two persistent volumes in the cluster are hosted on a single Filestore instance.

## What's next

  * [Create an instance on a Shared VPC network in service projects.](https://docs.cloud.google.com/filestore/docs/shared-vpc)
  * [Compare the relative advantages of block, file, and object storage.](https://docs.cloud.google.com/architecture/storage-advisor#review_the_storage_options)
  * [Storage options for HPC workloads in Google Cloud.](https://docs.cloud.google.com/architecture/parallel-file-systems-for-hpc#storage-options-for-hpc-workloads-in-google-cloud)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
