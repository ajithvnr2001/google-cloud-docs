---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-gke-volume-populator/
title: Troubleshooting GKE Volume Populator data transfer issues \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:53.661638+00:00
---

# Troubleshooting GKE Volume Populator data transfer issues  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-gke-volume-populator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshooting GKE Volume Populator data transfer issues Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

The [GKE Volume Populator](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-volume-populator) helps transfer data to GKE clusters. However, issues can arise during the data transfer process that prevent PersistentVolumeClaims (PVCs) from being created or data from being populated correctly.

Use this document to resolve common issues encountered when using the GKE Volume Populator. Learn how to troubleshoot data transfer issues by inspecting component status, validating configurations, and resolving resource or permission errors.

This information is important for Application developers and Platform admins and operators who use the GKE Volume Populator to seed data into their GKE volumes. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Inspect temporary Kubernetes resources

Here's how GKE Volume Populator uses temporary resources:

  1. A temporary PVC is created in the `gke-managed-volumepopulator` namespace.
  2. For each zone involved in the transfer, a transfer Job, PVs, and PVCs are created in your PVC's namespace.
  3. After the data transfer is done, GKE Volume Populator automatically removes all these temporary resources.



To inspect the temporary resources, follow these steps:

  1. Store the environment variables:
         
         export PVC_NAME=PVC_NAME
         export NAMESPACE=NAMESPACE
         

Replace the following values:

     * `PVC_NAME`: the name of your `PersistentVolumeClaim` resource.
     * `NAMESPACE`: the namespace where your workloads run.
  2. Check the status:
         
         export PVC_UID=$(kubectl get pvc ${PVC_NAME} -n ${NAMESPACE} -o jsonpath='{.metadata.uid}')
         export TEMP_PVC=prime-${PVC_UID}
         echo ${TEMP_PVC}
         

  3. Inspect the temporary PVC in the `gke-managed-volumepopulator` namespace:
         
         kubectl describe pvc ${TEMP_PVC} -n gke-managed-volumepopulator
         

  4. Get the names of the temporary PVCs in your namespace:
         
         export TEMP_PVC_LIST=($(kubectl get pvc -n "$NAMESPACE" -o json | grep -Eo "\"name\":\s*\"$TEMP_PVC[^\"]*\"" | awk -F'"' '{print $4}'))
         
         for pvc in "${TEMP_PVC_LIST[@]}"; do
           echo "$pvc"
         done
         

  5. Inspect the temporary PVCs:
         
         kubectl describe pvc "${TEMP_PVC_LIST[0]}" -n $NAMESPACE
         

  6. GKE Volume Populator creates a transfer Job in each zone (one in case of a single zone Hyperdisk ML volume and multiple in case of multi-zone Hyperdisk ML volumes). Get the transfer Job name by using the following command:
         
         export TRANSFER_JOB=$(kubectl get pvc "${TEMP_PVC_LIST[0]}" -n "$NAMESPACE" -o "jsonpath={.metadata.annotations['volume-populator\.datalayer\.gke\.io/pd-transfer-requestid']}")
         
         echo $TRANSFER_JOB
         

  7. Inspect the transfer Job:
         
         kubectl describe job $TRANSFER_JOB -n $NAMESPACE
         

  8. Get the Pod name from the transfer Job:
         
         export TRANSFER_POD=$(kubectl get pods -n "$NAMESPACE" -l "job-name=$TRANSFER_JOB" -o jsonpath='{.items[0].metadata.name}')
         
         echo $TRANSFER_POD
         

  9. Inspect the Pod:
         
         kubectl describe pod $TRANSFER_POD -n $NAMESPACE
         

If you create a PVC across multiple zones, the GKE Volume Populator creates distinct temporary PVCs and the transfer Job resources for each specified zone. To inspect the resources for every zone involved in the transfer, replace the `0` of the index for `TEMP_PVC_LIST` with other numbers.




## Check if Workload Identity Federation is enabled

Workload Identity Federation allows transfer pods to securely access Google Cloud services. If the transfer Pods are unable to authenticate to Google Cloud, verify that Workload Identity Federation for GKE is enabled on your cluster.

  1. To check if the `workloadIdentityConfig` is enabled on your cluster, run the following command:
         
         gcloud container clusters describe CLUSTER_NAME
         --location=LOCATION \
         --project=PROJECT_ID \
         --format="value(workloadIdentityConfig)"
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `LOCATION`: the compute region or zone of your cluster.
     * `PROJECT_ID`: your Google Cloud project ID.
  2. Look for the following output in the command:
         
         PROJECT_ID.svc.id.goog
         

  3. If `workloadIdentityConfig` is missing from the output, enable [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_clusters_and_node_pools).




## Invalid transfer path

If you encounter an error similar to the following, the transfer path specified on the `GCPDatasource` resource is incorrect, and the transfer will fail.
    
    
    ERROR: (gcloud.storage.cp) The following URLs matched no objects or files:
    gs://datasets-pd/llama2-7b-hfa/
    

To resolve this issue, delete the `GCPDatasource` resource, update the `uri` field with the correct value, and re-create the resource.

## Insufficient permission to access the bucket

If the Kubernetes service account doesn't have access to the bucket URI that's specified in the `GCPDatasource` resource, the transfer job will fail. The error might look similar to the following:
    
    
    ERROR: (gcloud.storage.cp) [test-gke-dev.svc.id.goog] does not have permission to access b instance [small-bucket-7] (or it may not exist): Caller does not have storage.objects.list access to the Google Cloud Storage bucket. Permission 'storage.objects.list' denied on resource (or it may not exist). This command is authenticated as test-gke-dev.svc.id.goog which is the active account specified by the [core/account] property.
    

To resolve the issue, [grant the necessary permissions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-populator-hdml#permissions) to transfer data from the bucket to the disk.
    
    
    gcloud storage buckets \
        add-iam-policy-binding gs://GCS_BUCKET \
         --member "principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME" \
        --role "ROLE"
    

Replace the following:

  * `GCS_BUCKET`: your Cloud Storage bucket name.
  * `PROJECT_NUMBER`: your Google Cloud project number.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `NAMESPACE`: the namespace where your workloads run.
  * `KSA_NAME`: the name of your Kubernetes service account.
  * `ROLE`: the [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles) that provides the necessary permissions to access the bucket. For example, use `roles/storage.objectViewer` to grant read-only access to the bucket.



## Error: `error generating accessibility requirements`

You might see the following transient error when you check the PVC in the `gke-managed-volumepopulator` namespace:
    
    
    Error: error generating accessibility requirements: no available topology found.
    

If you use a GKE Autopilot cluster or a Standard cluster with node auto-provisioning enabled, this error can occur because no nodes might be `Ready` in your cluster. The error should resolve itself within a few minutes after node auto-provisioning scales up a new node.

## Transfer Pod is `Pending` scheduling for a long time

Your PVC event might show that the status of the transfer Pod is `Pending` for a long time.

To check the transfer Job events to verify if the scheduling failed for the Job, follow these steps:

  1. Describe the PVC:
         
         kubectl describe pvc $PVC_NAME -n $NAMESPACE
         

The output is similar to the following:
         
         Events:
           Type     Reason             Age                From                Message
           ----     ------             ----               ----                -------
         Normal   TransferInProgress              1s (x2 over 2s)    gkevolumepopulator-populator                                                                      populateCompleteFn: For PVC pd-pvc79 in namespace default, job with request ID populator-job-0b93fec4-5490-4e02-af32-15b16435d559 is still active with pod status as - Phase: Pending
         

  2. To inspect the transfer Pod, follow the steps in Inspect temporary Kubernetes resources.

The output is similar to the following:
         
         Events:
           Type     Reason             Age                From                Message
           ----     ------             ----               ----                -------
           Warning  FailedScheduling   2m50s              default-scheduler   0/3 nodes are available: 1 Insufficient cpu, 2 node(s) had volume node affinity conflict. preemption: 0/3 nodes are available: 1 No preemption victims found for incoming pod, 2 Preemption is not helpful for scheduling.
           Warning  FailedScheduling   37s (x2 over 39s)  default-scheduler   0/3 nodes are available: 1 Insufficient cpu, 2 node(s) had volume node affinity conflict. preemption: 0/3 nodes are available: 1 No preemption victims found for incoming pod, 2 Preemption is not helpful for scheduling.
           Normal   NotTriggerScaleUp  2m40s              cluster-autoscaler  pod didn't trigger scale-up:
         

  3. If you see the `NotTriggerScaleUp` message, check if your cluster has node auto-provisioning enabled:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=LOCATION \
             --format="value(autoscaling.enableNodeAutoprovisioning)"
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `LOCATION`: the compute region or zone of your cluster.
  4. If the output shows as 'False', enable node auto-provisioning by using the following command:
         
         gcloud container clusters update CLUSTER_NAME \
             --enable-autoprovisioning \
             --location=LOCATION \
             --project=PROJECT_ID \
             --min-cpu MINIMUM_CPU \
             --min-memory MINIMUM_MEMORY \
             --max-cpu MAXIMUM_CPU \
             --max-memory MAXIMUM_MEMORY \
             --autoprovisioning-scopes=https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/devstorage.read_only
         

Replace the following:

     * `CLUSTER_NAME`: the name for the cluster that you're updating to enable node auto-provisioning.
     * `LOCATION`: the compute zone or region for your cluster. For example, `us-central1-a` or `us-central1`.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `MINIMUM_CPU`: the minimum number of vCPUs to auto-provision. For example, `10`.
     * `MINIMUM_MEMORY`: the minimum amount of memory in GiB to auto-provision. For example, `200`.
     * `MAXIMUM_CPU`: the maximum number of vCPUs to auto-provision. For example, `100`. This limit is the total of the CPU resources across all existing manually created node pools and all the node pools that GKE might automatically create.
     * `MAXIMUM_MEMORY`: the maximum amount of memory to auto-provision. For example, `1000`. This limit is the total of the memory resources across all existing, manually created node pools and all the node pools that GKE might automatically create.
  5. If node auto-provisioning is enabled, verify that [node auto-provisioning has sufficient autoscaling `resourceLimits`](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-up#noscaleup-reasons) to scale up the transfer Job. The transfer Job uses 24 vCPUs by default.
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=LOCATION \
             --format="value(autoscaling.resourceLimits)"
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `LOCATION`: the compute region or zone of your cluster.

The output is similar to the following:
    
    {'maximum': '1000000000', 'resourceType': 'cpu'};{'maximum': '1000000000', 'resourceType': 'memory'};
    

  6. If node auto-provisioning does not have sufficient autoscaling limits, update the cluster with the correct configuration.
         
         gcloud container clusters update CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             --enable-autoprovisioning \
             --max-cpu MAXIMUM_CPU \
             --max-memory MAXIMUM_MEMORY
         

Replace the following:

     * `CLUSTER_NAME`: the name for the cluster that you're updating to enable node auto-provisioning.
     * `LOCATION`: the compute zone or region for your cluster. For example, `us-central1-a` or `us-central1`.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `MAXIMUM_CPU`: the maximum number of vCPUs to auto-provision. For example, `100`. This limit is the total of the CPU resources across all existing manually created node pools and all the node pools that GKE might automatically create.
     * `MAXIMUM_MEMORY`: the maximum amount of memory to auto-provision. For example, `1000`. This limit is the total of the memory resources across all existing, manually created node pools and all the node pools that GKE might automatically create.
  7. For Standard clusters without node auto-provisioning enabled, verify that the node you created for the transfer Job has the required compute class label:
         
         kubectl get node -l cloud.google.com/compute-class=gcs-to-hdml-compute-class
         

  8. If the output doesn't list the node that you created for the transfer Job, add the `gcs-to-hdml-compute-class` compute class label to the node:
         
         kubectl label node NODE_NAME cloud.google.com/compute-class=gcs-to-hdml-compute-class
         

Replace the `NODE_NAME` with the name of the node where you want to add the compute class label.




## `GCE quota exceeded` error

You might encounter an error message similar to the following when you check the Pod for the transfer Job:
    
    
    Node scale up in zones us-west1-b associated with this pod failed: GCE quota exceeded. Pod is at risk of not being scheduled.
    

  1. To inspect the transfer Pod, follow the steps in Inspect temporary Kubernetes resources.

  2. To resolve the error, increase the quota or delete existing resources that might be preventing scale-up. For more information, see [Troubleshoot quota errors](https://docs.cloud.google.com/docs/quotas/troubleshoot).




## Hyperdisk ML `HDML_TOTAL_THROUGHPUT` exceeded error

If the temporary PVC in the `gke-managed-volumepopulator` namespace fails to provision the Hyperdisk ML volume, it's possible that the regional quota for creating the new Hyperdisk ML volume for your data transfer is exceeded.

To confirm that the provisioning of the Hyperdisk ML volume failed because of a regional quota issue, inspect the event logs associated with the temporary PVC that was created by the GKE Volume Populator. Follow these steps:

  1. Store the relevant environment variables:
         
         export PVC_NAME=PVC_NAME
         export NAMESPACE=NAMESPACE
         

Replace the following values:

     * `PVC_NAME`: the name of your `PersistentVolumeClaim` resource.
     * `NAMESPACE`: the namespace where your workloads run.
  2. Check the status of the temporary PVC:
         
         export PVC_UID=$(kubectl get pvc ${PVC_NAME} -n ${NAMESPACE} -o jsonpath='{.metadata.uid}')
         export TEMP_PVC=prime-$PVC_UID
         echo $TEMP_PVC
         kubectl describe pvc $TEMP_PVC -n gke-managed-volumepopulator
         

  3. Check the PVC events to find the `QUOTA_EXCEEDED error`, which is similar to the following:
         
         Events:
           Type     Reason                Age                 From                                                                                              Message
           ----     ------                ----                ----                                                                                              -------
           Warning  ProvisioningFailed    105s                pd.csi.storage.gke.io_gke-3ef909a7688d424b94a2-d0d9-b185-vm_6a77d057-54e3-415a-8b39-82b666516b6b  failed to provision volume with StorageClass "pd-sc": rpc error: code = Unavailable desc = CreateVolume failed: rpc error: code = Unavailable desc = CreateVolume failed to create single zonal disk pvc-73c69fa8-d23f-4dcb-a244-bcd120a3c221: failed to insert zonal disk: unknown error when polling the operation: rpc error: code = ResourceExhausted desc = operation operation-1739194889804-62dc9dd9a1cae-9d24a5ad-938e5299 failed (QUOTA_EXCEEDED): Quota 'HDML_TOTAL_THROUGHPUT' exceeded.  Limit: 30720.0 in region us-central1
         




To resolve this issue:

  1. [Request additional quota](https://docs.cloud.google.com/docs/quotas/view-manage) to create new Hyperdisk ML volumes in your project.
  2. Delete any unused Hyperdisk ML disks in your project.



## No space left on device

If you see the `No space left on device` error message on your PVC, it means that the Hyperdisk ML volume is full and no more data can be written to it. The error might look similar to the following:
    
    
    Events:
      Type     Reason                   Age   From                          Message
      ----     ------                   ----  ----                          -------
      Warning  TransferContainerFailed  57m   gkevolumepopulator-populator  populateCompleteFn: For PVC vp-pvc in namespace default, job with request ID populator-job-c2a2a377-6168-4ff1-afc8-c4ca713c43e2 for zone us-central1-c has a failed pod container with message:  on device
    ERROR: Failed to download one or more components of sliced download.
    ERROR: [Errno 28] No space left on device
    

To resolve this issue, delete your PVC, increase the value for `spec.resources.requests.storage` field in your PVC manifest, and re-create the PVC to start the transfer process again.

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
