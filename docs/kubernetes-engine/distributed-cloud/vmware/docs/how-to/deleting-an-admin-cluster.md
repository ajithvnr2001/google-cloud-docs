---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-an-admin-cluster/
title: Deleting an admin cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:52.355387+00:00
---

# Deleting an admin cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-an-admin-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Deleting an admin cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete an admin cluster created with Google Distributed Cloud (software only) for VMware.

## Before you begin

Before you delete an admin cluster, complete the following steps:

  * Delete its user clusters. See [Deleting a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-a-user-cluster).
  * Delete any workloads that use [PodDisruptionBudgets](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) from the admin cluster.
  * Delete all external objects, such as PersistentVolumes, from the admin cluster.
  * On your admin workstation, set a `KUBECONFIG` environment variable that points to the kubeconfig of the admin cluster that you want to delete:
        
        export KUBECONFIG=ADMIN_CLUSTER_KUBECONFIG
        

where `ADMIN_CLUSTER_KUBECONFIG` is the path of the admin cluster's kubeconfig file.

  * Optionally, run the following command on your admin workstation to get the admin cluster name:
        
        kubectl get -n=kube-system onpremadmincluster
        




## Unenrolling the admin cluster

If the admin cluster is enrolled in the GKE On-Prem API, you need to unenroll it from the API before you delete any other cluster resources. Unenrolling the cluster removes the GKE On-Prem API resources from Google Cloud. If you don't unenroll the cluster, it will continue to be displayed in the Google Cloud console on the **Kubernetes Engine** > **Clusters** page.

If you created the admin cluster using the Google Cloud console or Terraform, the cluster is automatically enrolled in the GKE On-Prem API. Admin clusters created with version 1.16 or higher using the `gkectl` command-line tool are automatically enrolled with the GKE On-Prem API. If your admin cluster was created using `gkectl` with an earlier version, the cluster is enrolled in the API in the following cases:

  * You [explicitly enrolled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) the cluster.
  * You [upgraded a user cluster using the Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#gcloud-cli), which automatically enrolls the admin cluster.


  1. List all enrolled admin clusters in your project:
         
         gcloud container vmware admin-clusters list \
              --project=PROJECT_ID \
              --location=-
         

Replace `PROJECT_ID` with the ID of the fleet host project.

The command outputs the name of each admin cluster that is enrolled in the GKE On-Prem API in the project, along with the Google Cloud region.

When you set `--location=-`, that means to list all clusters in all regions. If you need to scope down the list, set `--location` to the region you specified when you enrolled the cluster.

  2. Unenroll the cluster from the GKE On-Prem API:
         
         gcloud container vmware admin-clusters unenroll  ADMIN_CLUSTER_NAME \
             --project=PROJECT_ID \
             --location=REGION \
             --allow-missing \
             --ignore-errors
         

Replace the following:

     * `ADMIN_CLUSTER_NAME`: The name of the admin cluster.
     * `PROJECT_ID`: The ID of the fleet host project.
     * `REGION`: The Google Cloud region.

The `--allow-missing` flag returns success if the cluster isn't found.

The `--ignore-errors` flag ensures that the unenrollment of an admin cluster resource succeeds even if errors occur during unenrollment.




## Deleting logging and monitoring

Skip this section if your cluster is at version 1.30 or higher. Because the logging and monitoring custom resources aren't deployed on clusters at version 1.30 and higher, if you run the commands, they won't return.

Google Distributed Cloud's logging and monitoring Pods, deployed from StatefulSets, use PDBs that can prevent nodes from draining properly. To properly delete an admin cluster, you need to delete these Pods.

To delete logging and monitoring Pods, run the following commands:
    
    
    kubectl delete monitoring --all -n kube-system
    kubectl delete stackdriver --all -n kube-system

Deleting monitoring cleans up the PersistentVolumes (PVs) associated with StatefulSets, but the PersistentVolume for Stackdriver needs to be deleted separately.

Deletion of the Stackdriver PV is optional. If you choose not to delete the PV, record the location and name of the associated PV in an external location outside of the user cluster.

Deletion of the PV will get propagated through deleting the Persistent Volume Claim (PVC).

To find the Stackdriver PVC, run the following command:
    
    
    kubectl get pvc -n kube-system

To delete the PVC, run the following command:
    
    
    kubectl delete pvc -n kube-system PVC_NAME
    

### Verifying logging & monitoring are removed

To verify that logging and monitoring have been removed, run the following commands:
    
    
    kubectl get pvc -n kube-system
    kubectl get statefulsets -n kube-system

## Cleaning up an admin cluster's F5 partition

Skip this section if you aren't using the F5 load balancer.

Deleting the `gke-system` namespace from the admin cluster ensures proper cleanup of the F5 partition, allowing you to reuse the partition for another admin cluster.

To delete the `gke-system` namespace, run the following command:
    
    
    kubectl delete ns gke-system

Then delete any remaining Services of type LoadBalancer. To list all Services, run the following command:
    
    
    kubectl get services --all-namespaces

**Note:** The kube-apiserver Service should be the last Service you delete. After you delete this service, you will no longer be able to use kubectl to reach your cluster.

For each Service of type LoadBalancer, delete it by running the following command:
    
    
    kubectl delete service SERVICE_NAME -n SERVICE_NAMESPACE
    

Then, from the F5 BIG-IP console:

  1. In the top-right corner of the console, switch to the partition to clean up.
  2. Select **Local Traffic** > **Virtual Servers** > **Virtual Server List**.
  3. In the **Virtual Servers** menu, remove all the virtual IPs.
  4. Select **Pools** , then delete all the pools.
  5. Select **Nodes** , then delete all the nodes.



### Verifying F5 partition is clean

### CLI

Check that the VIP is down by running the following command:
    
    
    ping -c 1 -W 1 F5_LOAD_BALANCER_IP; echo $?

which will return `1` if the VIP is down.

### F5 UI

To check that the partition has been cleaned up from the F5 user interface, perform the following steps:

  1. From the upper-right corner, click the **Partition** drop-down menu. Select your admin cluster's partition.
  2. From the left-hand **Main** menu, select **Local Traffic** > **Network Map**. There should be nothing listed below the Local Traffic Network Map.
  3. From **Local Traffic** > **Virtual Servers** , select **Nodes** , then select **Nodes List**. There should be nothing listed here as well.



If there are any entries remaining, delete them manually from the UI.

## Powering off admin node machines

First, run this command to get the names of the machines, before you power them off.
    
    
    kubectl get machines -o wide
    

The output lists the names of the machines. You can now find them in the vSphere UI.

To delete the admin control plane node machines, you need to power off each of the remaining admin VMs in your vSphere resource pool.

### vSphere UI

Perform the following steps:

  1. From the vSphere menu, select the VM from the vSphere resource pool.
  2. From the top of the VM menu, click **Actions**.
  3. Select **Power** > **Power Off**. It may take a few minutes for the VM to power off.



## Deleting admin node machines

After the VM has powered off, you can delete the VM.

### vSphere UI

Perform the following steps:

  1. From the vSphere menu, select the VM from the vSphere resource pool.
  2. From the top of the VM menu, click **Actions**.
  3. Click **Delete from Disk**.



## Deleting the data disk

After you have deleted the VMs, you can delete the data disk. The steps differ slightly depending on whether you have a highly-available (HA) or non-HA admin cluster.

Do the following steps in the vSphere UI:

### Non-HA

  1. From the vSphere menu, select the data disk from the datastore as specified in the `vCenter.dataDisk` field in the admin cluster configuration file.
  2. From the middle of the datastore menu, click **Delete**.



### HA

The data disk paths for the 3 admin control plane machines are auto generated under `/anthos/ADMIN_CLUSTER/default/`, for example:
    
    
    /anthos/ADMIN_CLUSTER_NAME/default/MACHINE_NAME-0-data.vmdk
    /anthos/ADMIN_CLUSTER_NAME/default/MACHINE_NAME-1-data.vmdk
    /anthos/ADMIN_CLUSTER_NAME/default/MACHINE_NAME-2-data.vmdk
    

Do the following steps to delete each data disk:

  1. From the vSphere menu, select the data disk from the datastore.
  2. From the middle of the datastore menu, click **Delete**.



## Deleting the `checkpoint.yaml` file

If you are deleting a HA admin cluster, skip this step because HA admin clusters don't support the checkpoint file.

The DATA_DISK_NAME-checkpoint.yaml [file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster#managing_the_checkpointyaml_file), where DATA_DISK_NAME is the name of the data disk, is located in the same folder as the data disk. Delete this file.

**Note:** If DATA_DISK_NAME is too long, the file is instead called DATA_DISK_NAME.yaml.

## Unregistering the admin cluster

When you create an admin cluster, it is automatically registered to a Google Cloud fleet. You need to unregister the cluster after you delete the admin node machines; otherwise, a controller in the cluster automatically re-registers the cluster.

Unregistering the cluster removes the fleet membership resources from Google Cloud. If you don't unregister the cluster, it will continue to be displayed in the Google Cloud console on the **Kubernetes Engine** > **Clusters** page.

  1. Run the following command and note the location:
         
         gcloud container fleet memberships list \
             --project=PROJECT_ID
         

  2. Run the following command to delete the fleet membership, which unregisters the cluster:
         
         gcloud container fleet memberships delete ADMIN_CLUSTER_NAME \
             --project=PROJECT_ID \
             --location=MEMBERSHIP_REGION
         

Replace `MEMBERSHIP_REGION` with the location output from the `gcloud container fleet memberships list` command. This could be `global` or a Google Cloud region.




## After you have finished

After you have finished deleting the admin cluster, delete its kubeconfig.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
