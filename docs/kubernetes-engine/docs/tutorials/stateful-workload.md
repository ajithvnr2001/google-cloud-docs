---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workload/
title: Deploy a stateful workload with Filestore \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:44.603614+00:00
---

# Deploy a stateful workload with Filestore  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy a stateful workload with Filestore Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This tutorial shows how to deploy a simple reader/writer stateful workload using a [Persistent Volume (PV)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) and a [Persistent Volume Claim (PVC)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) on Google Kubernetes Engine (GKE). Follow this tutorial to learn how to design for scalability using [Filestore](https://docs.cloud.google.com/filestore/docs), Google Cloud's managed network filesystem. 

## Background

By nature, Pods are ephemeral. This means that GKE destroys the state and value stored in a Pod when it is deleted, evicted, or rescheduled.

As an application operator, you may want to maintain stateful workloads. Examples of such workloads include applications that process WordPress articles, messaging apps, and apps that process machine learning operations.

By using Filestore on GKE, you can perform the following operations:

  * Deploy stateful workloads that are scalable.
  * Enable multiple Pods to have `ReadWriteMany` as its `accessMode`, so that multiple Pods can read and write at the same time to the same storage.
  * Set up GKE to mount volumes into multiple Pods simultaneously.
  * Persist storage when Pods are removed.
  * Enable Pods to share data and easily scale.



## Objectives

This tutorial is for application operators and other users that want to set up a scalable stateful workload on GKE using PVC and NFS. 

![Stateful workload GKE diagram](https://docs.cloud.google.com/static/kubernetes-engine/images/stateful-workload-architecture.png)

This tutorial covers the following steps:

  1. Create a GKE cluster.
  2. Configure the managed file storage with Filestore using CSI.
  3. Create a reader and a writer Pod.
  4. Expose and access the reader Pod to a Service Load Balancer.
  5. Scale up the writer.
  6. Access data from the writer Pod. 



## Costs

This tutorial uses the following billable components of Google Cloud: 

  * [Filestore](https://cloud.google.com/filestore/pricing)
  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)



Use the [Pricing Calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

When you finish this tutorial, you can avoid continued billing by deleting the resources you created. For more information, see Clean up.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=kubernetes--stateful)

* * *

## Before you begin

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine, GKE, and Filestore APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,container.googleapis.com,file.googleapis.com)

  5. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine, GKE, and Filestore APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,container.googleapis.com,file.googleapis.com)




### Set defaults for the Google Cloud CLI

  1. In the Google Cloud console, start a Cloud Shell instance:   
[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Download the source code for this sample app:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         cd kubernetes-engine-samples/databases/stateful-workload-filestore
         

  3. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         gcloud config set compute/region COMPUTE_REGION
         gcloud config set compute/zone COMPUTE_ZONE
         gcloud config set filestore/zone COMPUTE_ZONE
         gcloud config set filestore/region COMPUTE_REGION
         

Replace the following values:

     * PROJECT_ID: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * COMPUTE_REGION: the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available).
     * COMPUTE_ZONE: the [Compute Engine zone](https://docs.cloud.google.com/compute/docs/regions-zones#available).



## Create a GKE cluster

  1. Create a GKE cluster:
         
         gcloud container clusters create-auto CLUSTER_NAME --location CONTROL_PLANE_LOCATION
         

Replace the following value:

     * CLUSTER_NAME: your cluster name.
     * CONTROL_PLANE_LOCATION: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
**Note:** This step can take up to five minutes to complete.

The outcome is similar to the following once the cluster is created:
    
    gcloud container clusters describe CLUSTER_NAME
      NAME: CLUSTER_NAME
      LOCATION: northamerica-northeast2
      MASTER_VERSION: 1.21.11-gke.1100
      MASTER_IP: 34.130.255.70
      MACHINE_TYPE: e2-medium
      NODE_VERSION: 1.21.11-gke.1100
      NUM_NODES: 3
      **STATUS: RUNNING**
    

Where the `STATUS` is `RUNNING`.




## Configure the managed file storage with Filestore using CSI

GKE provides a way to automatically deploy and manage the [Kubernetes Filestore CSI driver](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver) in your clusters. Using Filestore CSI allows you to dynamically create or delete Filestore instances and use them in Kubernetes workloads with a `StorageClass` or a `Deployment`.

You can create a new Filestore instance by creating a PVC that dynamically provisions a Filestore instance and the PV, or access pre-provisioned Filestore instances in Kubernetes workloads.

**Note:** To use the Filestore CSI driver, your clusters must use GKE version 1.21 or later.

### New instance

#### Create the Storage Class
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: filestore-sc
    provisioner: filestore.csi.storage.gke.io
    volumeBindingMode: WaitForFirstConsumer
    allowVolumeExpansion: true
    parameters:
      tier: standard
      network: default

  * `volumeBindingMode` is set to `WaitForFirstConsumer`, which delays provisioning the volume until a Pod uses it. This setting allows the control plane to know the location of the volume (Kubernetes calls this its _topology_), and lets this example work for new clusters with no nodes, where there is no topology yet.
  * `tier` is set to `standard` for faster Filestore instance creation time. If you need higher available NFS storage, snapshots for data backup, data replication over multiple zones and other enterprise level features, set `tier` to `enterprise` instead. Note: The reclaim policy for dynamically created PV defaults to `Delete` if the `reclaimPolicy` in the `StorageClass` is not set.


  1. Create the `StorageClass` resource:
         
         kubectl create -f filestore-storageclass.yaml
         

  2. Verify that the Storage Class is created:
         
         kubectl get sc
         

The output is similar to the following:
         
         NAME                     PROVISIONER                    RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
         **filestore-sc             filestore.csi.storage.gke.io   Delete          Immediate              true                   94m**
         




### Pre-provisioned instance

#### Create the Storage Class
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: filestore-sc
    provisioner: filestore.csi.storage.gke.io
    volumeBindingMode: Immediate
    allowVolumeExpansion: true

When `volumeBindingMode` is set to `Immediate`, it allows the provisioning of the volume to begin immediately.

  1. Create the `StorageClass` resource:
         
         kubectl create -f preprov-storageclass.yaml
         

  2. Verify that the Storage Class is created:
         
         kubectl get sc
         

The output is similar to the following:
         
         NAME                     PROVISIONER                    RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
           **filestore-sc             filestore.csi.storage.gke.io   Delete          Immediate              true                   94m**
         




#### Create a Persistent Volume for the Filestore instance
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: fileserver
      annotations:
        pv.kubernetes.io/provisioned-by: filestore.csi.storage.gke.io
    spec:
      storageClassName: filestore-sc
      capacity:
        storage: 1Ti
      accessModes:
        - ReadWriteMany
      persistentVolumeReclaimPolicy: Delete
      volumeMode: Filesystem
      csi:
        driver: filestore.csi.storage.gke.io
        # Modify this to use the zone, filestore instance and share name.
    ** volumeHandle: "modeInstance/<LOCATION>/<INSTANCE_NAME>/<FILE_SHARE_NAME>"**
        volumeAttributes:
    ** ip: <IP_ADDRESS> # Modify this to Pre-provisioned Filestore instance IP**
    ** volume: <FILE_SHARE_NAME> # Modify this to Pre-provisioned Filestore instance share name**

  1. Verify that the pre-existing Filestore instance is ready:
         
         gcloud filestore instances list
         

The output is similar to the following, where the `STATE` value is `READY`:
         
         **INSTANCE_NAME: stateful-filestore**
           **LOCATION: us-central1-a**
           TIER: ENTERPRISE
           CAPACITY_GB: 1024
           **FILE_SHARE_NAME: statefulpath**
           **IP_ADDRESS: 10.109.38.98**
           STATE: READY
           CREATE_TIME: 2022-04-05T18:58:28
         

Note the `INSTANCE_NAME`, `LOCATION`, `FILE_SHARE_NAME`, and `IP_ADDRESS` of the Filestore instance.

  2. Populate the Filestore instance console variables:
         
         INSTANCE_NAME=INSTANCE_NAME
           LOCATION=LOCATION
           FILE_SHARE_NAME=FILE_SHARE_NAME
           IP_ADDRESS=IP_ADDRESS
         

  3. Replace the placeholder variables with the console variables obtained above to the file `preprov-pv.yaml`:
         
         sed "s/<INSTANCE_NAME>/$INSTANCE_NAME/" preprov-pv.yaml > changed.yaml && mv changed.yaml preprov-pv.yaml
           sed "s/<LOCATION>/$LOCATION/" preprov-pv.yaml > changed.yaml && mv changed.yaml preprov-pv.yaml
           sed "s/<FILE_SHARE_NAME>/$FILE_SHARE_NAME/" preprov-pv.yaml > changed.yaml && mv changed.yaml preprov-pv.yaml
           sed "s/<IP_ADDRESS>/$IP_ADDRESS/" preprov-pv.yaml > changed.yaml && mv changed.yaml preprov-pv.yaml
         

  4. Create the PV
         
         kubectl apply -f preprov-pv.yaml
         

  5. Verify that the PV's `STATUS` is set to `Bound`:
         
         kubectl get pv
         

The output is similar to the following:
         
         NAME        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                STORAGECLASS    REASON   AGE
           fileserver  1Ti        RWX            Delete           Bound    default/fileserver   filestore-sc             46m
         




### Use a PersistentVolumeClaim to access the volume

The following `pvc.yaml` manifest references the Filestore CSI driver's `StorageClass` named `filestore-sc`.

In order to have multiple Pods reading and writing to the volume, the `accessMode` is set to `ReadWriteMany`.
    
    
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: fileserver
    spec:
      accessModes:
      - ReadWriteMany
      storageClassName: filestore-sc
      resources:
        requests:
          storage: 1Ti

  1. Deploy the PVC:
         
         kubectl create -f pvc.yaml
         

  2. Verify that the PVC is created:
         
         kubectl get pvc
         

The output is similar to the following:
         
         NAME         STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS        AGE
         fileserver   Bound    pvc-aadc7546-78dd-4f12-a909-7f02aaedf0c3   1Ti        RWX            filestore-sc        92m
         


**Note:** the filestore instance won't be created until it is used by a Pod in the next step.

## Create a reader and a writer Pod

In this section, you create a reader Pod and a writer Pod. This tutorial uses Kubernetes Deployments to create the Pods. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster..

### Create the reader Pod

The reader Pod will read the file that is being written by the writers Pods. The reader Pods will see what time and which writer Pod replica wrote to the file.
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: reader
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: reader
      template:
        metadata:
          labels:
            app: reader
        spec:
          containers:
          - name: nginx
            image: nginx:stable-alpine
            ports:
            - containerPort: 80
            volumeMounts:
            - name: fileserver
    ** mountPath: /usr/share/nginx/html # the shared directory **
              readOnly: true
          volumes:
          - name: fileserver
            persistentVolumeClaim:
              claimName: fileserver

The reader Pod will read from the path `/usr/share/nginx/html` which is shared between all the Pods.

  1. Deploy the reader Pod:
         
         kubectl apply -f reader-fs.yaml
         

  2. Verify that the newly created Filestore instance is ready:
         
         gcloud filestore instances list
         

The output is similar to the following:
         
         INSTANCE_NAME: pvc-5bc55493-9e58-4ca5-8cd2-0739e0a7b68c
         LOCATION: northamerica-northeast2-a
         TIER: STANDARD
         CAPACITY_GB: 1024
         FILE_SHARE_NAME: vol1
         IP_ADDRESS: 10.29.174.90
         STATE: READY
         CREATE_TIME: 2022-06-24T18:29:19
         

  3. Verify that the reader replicas are running by querying the list of Pods:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                      READY   STATUS    RESTARTS   AGE
         reader-66b8fff8fd-jb9p4   1/1     Running   0          3m30s
         


**Note:** The Filestore instance can take five minutes to create. The reader pod won't start running until the Filestore instance is created. Proceed to the next step while waiting.

### Create the writer Pod

The writer Pod will periodically write to a shared file that other writer and reader Pods can access. The writer Pod records its presence by writing its host name to the shared file.

The image used for the writer Pod is a custom image of Alpine Linux, which is used for utilities and production applications. It includes a script `indexInfo.html` that will obtain the metadata of the most recent writer, and keep count of all the unique writers and total writes.
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: writer
    spec:
    ** replicas: 2 # start with 2 replicas**
      selector:
        matchLabels:
          app: writer
      template:
        metadata:
          labels:
            app: writer
        spec:
          containers:
          - name: content
            image: us-docker.pkg.dev/google-samples/containers/gke/stateful-workload:latest
            volumeMounts:
            - name: fileserver
    ** mountPath: /html # the shared directory**
            command: ["/bin/sh", "-c"]
            args:
    ** - cp /htmlTemp/indexInfo.html /html/index.html;**
    ** while true; do**
    ** echo "<b> Date :</b> <text>$(date)</text> <b> Writer :</b> <text2> ${HOSTNAME} </text2> <br>  " >> /html/indexData.html;**
    ** sleep 30;  **
    ** done**
          volumes:
          - name: fileserver
            persistentVolumeClaim:
              claimName: fileserver

For this tutorial, the writer Pod writes every 30 seconds to the path `/html/index.html`. Modify the `sleep` number value to have a different write frequency.

  1. Deploy the writer Pod:
         
         kubectl apply -f writer-fs.yaml
         

  2. Verify that the writer Pods are running by querying the list of Pods:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                      READY   STATUS    RESTARTS   AGE
         reader-66b8fff8fd-jb9p4   1/1     Running   0          3m30s
         writer-855565fbc6-8gh2k   1/1     Running   0          2m31s
         writer-855565fbc6-lls4r   1/1     Running   0          2m31s
         

**Note:** Pod creation might take up to five minutes.



## Expose and access the reader workload to a Service Load Balancer

To expose a workload outside the cluster, create a Service of type `LoadBalancer`. This type of Service creates an external load balancer with an IP address reachable through the internet.

  1. Create a Service of type `LoadBalancer` named `reader-lb`:
         
         kubectl create -f loadbalancer.yaml
         

  2. Watch the deployment to see that GKE assigns an `EXTERNAL-IP` for `reader-lb` Service:
         
         kubectl get svc --watch
         

When the `Service` is ready, the `EXTERNAL-IP` column displays the public IP address of the load balancer:
         
         NAME         TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)        AGE
           kubernetes   ClusterIP      10.8.128.1    <none>          443/TCP        2d21h
           reader-lb    LoadBalancer   10.8.131.79   34.71.232.122   80:32672/TCP   2d20h
         

  3. Press **Ctrl+C** to terminate the watch process.

  4. Use a web browser to navigate to the `EXTERNAL-IP` assigned to the load balancer. The page refreshes every 30 seconds. The more writers Pods and shorter the frequency, the more entries it will show.




To see more details about the load balancer service, see [`loadbalancer.yaml`](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/databases/stateful-workload-filestore/loadbalancer.yaml).

## Scale up the writer

Because the PV `accessMode` was set to `ReadWriteMany`, GKE can scale up the number of Pods so that more writer Pods can write to this shared volume (or more readers can read to read them).

  1. Scale up the `writer` to five replicas:
         
         kubectl scale deployment writer --replicas=5
         

The output is similar to the following:
         
         deployment.extensions/writer scaled
         

**Note:** Scaling might take a few minutes while the cluster is allocating more resources.
  2. Verify the number of running replicas:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                      READY   STATUS    RESTARTS   AGE
         reader-66b8fff8fd-jb9p4   1/1     Running   0          11m
         writer-855565fbc6-8dfkj   1/1     Running   0          4m
         writer-855565fbc6-8gh2k   1/1     Running   0          10m
         writer-855565fbc6-gv5rs   1/1     Running   0          4m
         writer-855565fbc6-lls4r   1/1     Running   0          10m
         writer-855565fbc6-tqwxc   1/1     Running   0          4m
         

  3. Use a web browser to navigate again to the `EXTERNAL-IP` assigned to the load balancer.




At this point, you configured and scaled your cluster to support five stateful writer Pods. Where multiple writer Pods are writing to the same file simultaneously. The reader Pods can also be easily scaled up.

## Optional: Access data from the writer Pod

This section demonstrates how to use a command-line interface to access a reader or writer Pod. You can see the shared component that the writer is writing to and the reader is reading from.

  1. Obtain the writer Pod name:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                      READY   STATUS    RESTARTS   AGE
         writer-5465d65b46-7hxv4   1/1     Running   0          20d
         

Note the hostname of a writer Pod (Example: `writer-5465d65b46-7hxv4`).

  2. Run the following command to access the writer Pod:
         
         kubectl exec -it WRITER_HOSTNAME -- /bin/sh
         

  3. See the shared component in the file `indexData.html`:
         
         cd /html
         cat indexData.html
         

  4. Clear the `indexData.html` file:
         
         echo '' > indexData.html
         

Refresh the web browser hosting the `EXTERNAL-IP` address to see the change.

  5. Exit the environment:
         
         exit
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources

  1. Delete the load balancer Service:
         
         kubectl delete service reader-lb
         

Wait until the load balancer provisioned for the reader service is deleted

  2. Verify the list returns `Listed 0 items`:
         
         gcloud compute forwarding-rules list
         

  3. Delete the Deployments
         
         kubectl delete deployment writer
         kubectl delete deployment reader
         

  4. Verify the Pods are deleted and returns `No resources found in default namespace.`
         
         kubectl get pods
         

  5. Delete the PVC. This will also delete the PV and the Filestore instance due to the retention policy set to `delete`
         
         kubectl delete pvc fileserver
         

  6. Delete the GKE cluster:
         
         gcloud container clusters delete CLUSTER_NAME --location=CONTROL_PLANE_LOCATION
         

This deletes the resources that make up the GKE cluster, including the reader and writer Pods.




## What's next

  * Learn how to deploy [Cloud SQL with GKE](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-kubernetes#gcloud_3)
  * [Access Modes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#access_modes) for PV and PVC
  * Learn more about [GKE and Filestore](https://docs.cloud.google.com/filestore/docs/csi-driver)
  * Learn more about [Filestore CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver#console)
  * How to create a [Filestore instance](https://docs.cloud.google.com/filestore/docs/creating-instances)
  * [See how to access Filestore instances from GKE clusters](https://docs.cloud.google.com/filestore/docs/csi-driver)
  * Explore other [Kubernetes Engine tutorials](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials). 
  * Learn more about exposing apps using Services in GKE [Exposing applications using services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
