---
url: https://docs.cloud.google.com/spanner-omni/maintain-deployment/
title: Maintain a Spanner Omni deployment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:42.292948+00:00
---

# Maintain a Spanner Omni deployment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/maintain-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Maintain a Spanner Omni deployment Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how you can maintain a Spanner Omni deployment. Maintaining a Spanner Omni deployment includes routine health checks, decommissioning unhealthy elements, and replacing server nodes or faulty disks to ensure cluster stability and consistency. Managing database health protects your databases from unplanned outages and maintains the redundancy of the underlying Paxos consensus group.

Performing maintenance helps you:

  * **Ensure high availability** : Reprovision unhealthy virtual machines (VMs) or pods to maintain database server redundancy. This helps you keep your applications running if hardware fails.

  * **Protect data safety and integrity** : Decommission nodes with faulty disks to prevent storage failures from spreading to other parts of the database. This also ensures that disconnected servers don't record conflicting updates.




## Before you begin

Before you perform maintenance on your Kubernetes deployment, you must do the following:

  * Create a Spanner Omni deployment. For more information, see [Create a deployment on Kubernetes](https://docs.cloud.google.com/spanner-omni/deploy-on-kubernetes) or [Create a deployment on VMs](https://docs.cloud.google.com/spanner-omni/deploy-on-vms).

  * Download and install the [Spanner Omni CLI](https://docs.cloud.google.com/spanner-omni/cli-quickstart#step-1-download-install-cli).

  * For deployments on Kubernetes, install [Helm](https://helm.sh/) and create a [Helm chart configuration](https://docs.cloud.google.com/spanner-omni/create-helm-configuration).




## Replace a server

You might need to replace a server in your deployment to resolve system or storage faults.

### Replace a root server

To replace a root server, select the tab for your environment:

###  Kubernetes 

To replace a root server in a Kubernetes deployment, perform the following steps. Although adding more root servers to an existing Kubernetes deployment isn't supported, you can replace existing root servers to resolve any irrecoverable errors that you experience.

  1. Delete the server that you want to replace:
         
         spanner deployment servers delete SERVER_ENDPOINT --zone=ZONE
         

Replace the following:

     * `SERVER_ENDPOINT`: The server pod endpoint to delete, in the format `SERVER.pod.NAMESPACE:PORT`—for example, `spanner-a-1.pod.spanner-ns:15000`. To find the server endpoints in your deployment, list the deployment servers by running `spanner deployment servers list --zone=ZONE`.
     * `ZONE`: The zone containing the server—for example, `us-central1-a`.

This step might take a few minutes depending on the volume of data on the server. Spanner Omni relocates the data from this server to other servers in the deployment. Ensure that the server deletion is complete before proceeding to the next step.

To track deletion progress, check the status of the server:
    
    spanner deployment servers describe SERVER_ENDPOINT --zone=ZONE
    

Wait until the command returns a `NOT_FOUND` error or indicates that the server is no longer registered.

  2. Delete the persistent volume claim (PVC) for the pod hosting the server:
         
         kubectl delete pvc DATA_VOLUME_NAME -n NAMESPACE
         

Replace the following:

     * `DATA_VOLUME_NAME`: The data volume name—for example, `data-volume-spanner-a-1`. To find the data volume name, list the PVCs in your namespace by running `kubectl get pvc -n NAMESPACE`.
     * `NAMESPACE`: The namespace of the deployment—for example, `spanner-ns`.
  3. Delete the pod:
         
         kubectl delete pod POD_NAME -n NAMESPACE
         

Replace `POD_NAME` with the name of the server pod to delete—for example, `spanner-a-1`.

Kubernetes automatically starts a new server in a replacement pod and attaches a new PVC.

  4. Add the new server to the deployment:
         
         spanner deployment servers create SERVER_ENDPOINT --zone=ZONE
         

Verify that arguments match the new pod endpoint and zone—for example, using `spanner-a-1.pod.spanner-ns:15000` as the endpoint and `us-central1-a` as the zone.




###  VM 

To replace a root server in a VM deployment, perform the following steps:

  1. Delete the server that you want to replace:
         
         spanner deployment servers delete SERVER_ENDPOINT --zone=ZONE
         

Replace the following:

     * `SERVER_ENDPOINT`: The server IP address or hostname and port—for example, `spanner-vm-1.example.com:15000`. To find the server endpoints, list the deployment servers by running `spanner deployment servers list --zone=ZONE`.
     * `ZONE`: The zone containing the server—for example, `us-central1-a`.

This step might take a few minutes depending on the volume of data on the server. Spanner Omni relocates the data from this server to other servers in the deployment. Ensure that the server deletion is complete before proceeding to the next step.

To track deletion progress, check the status of the server:
    
    spanner deployment servers describe SERVER_ENDPOINT --zone=ZONE
    

Wait until the command returns a `NOT_FOUND` error or indicates that the server is no longer registered.

  2. Reprovision the server with clean storage as explained in [Create a deployment for Spanner Omni on VMs](https://docs.cloud.google.com/spanner-omni/deploy-on-vms):
         
         spanner start \
           --root \
           --server-address=HOSTNAME \
           --zone=ZONE \
           --base-dir=BASE_DIR
         

Replace the following:

     * `HOSTNAME`: The resolvable FQDN or hostname of the new VM—for example, `spanner-vm-1.example.com`.
     * `ZONE`: The target zone—for example, `us-central1-a`.
     * `BASE_DIR`: The path where data is stored—for example, `./span-dir`.
  3. Add the new server to the deployment:
         
         spanner deployment servers create SERVER_ENDPOINT --zone=ZONE
         

Verify that arguments match the parameters of the new server—for example, using `spanner-vm-1.example.com:15000` as the endpoint and `us-central1-a` as the zone.




### Replace a non-root server

To replace a non-root server, select the tab for your environment:

###  Kubernetes 

To replace a non-root server in a Kubernetes deployment, perform the following steps:

  1. Delete the server that you want to replace:
         
         spanner deployment servers delete SERVER_ENDPOINT --zone=ZONE
         

Replace the following:

     * `SERVER_ENDPOINT`: The server pod endpoint to delete, in the format `SERVER.pod.NAMESPACE:PORT`—for example, `spanner-a-4.pod.spanner-ns:15000`. To find the server endpoints in your deployment, list the deployment servers by running `spanner deployment servers list --zone=ZONE`.
     * `ZONE`: The zone containing the server—for example, `us-central1-a`.

This step might take a few minutes depending on the volume of data on the server. Spanner Omni relocates the data from this server to other servers in the deployment. Ensure that the server deletion is complete before proceeding to the next step.

To track deletion progress, check the status of the server:
    
    spanner deployment servers describe SERVER_ENDPOINT --zone=ZONE
    

Wait until the command returns a `NOT_FOUND` error or indicates that the server is no longer registered.

  2. Delete the persistent volume claim (PVC) for the pod hosting the server:
         
         kubectl delete pvc DATA_VOLUME_NAME -n NAMESPACE
         

Replace the following:

     * `DATA_VOLUME_NAME`: The data volume name—for example, `data-volume-spanner-a-4`. To find the data volume name, list the PVCs in your namespace by running `kubectl get pvc -n NAMESPACE`.
     * `NAMESPACE`: The namespace of the deployment—for example, `spanner-ns`.
  3. Delete the pod:
         
         kubectl delete pod POD_NAME -n NAMESPACE
         

Replace `POD_NAME` with the name of the server pod to delete—for example, `spanner-a-4`.

Kubernetes automatically starts a new server in a replacement pod and attaches a new PVC. Spanner Omni automatically registers the new non-root server into the deployment.




###  VM 

To replace a non-root server in a VM deployment, perform the following steps:

  1. Delete the server that you want to replace:
         
         spanner deployment servers delete SERVER_ENDPOINT --zone=ZONE
         

Replace the following:

     * `SERVER_ENDPOINT`: The server IP address or hostname and port—for example, `spanner-vm-4.example.com:15000`. To find the server endpoints, list the deployment servers by running `spanner deployment servers list --zone=ZONE`.
     * `ZONE`: The zone containing the server—for example, `us-central1-a`.

This step might take a few minutes depending on the volume of data on the server. Spanner Omni relocates the data from this server to other servers in the deployment. Ensure that the server deletion is complete before proceeding to the next step.

To track deletion progress, check the status of the server:
    
    spanner deployment servers describe SERVER_ENDPOINT --zone=ZONE
    

Wait until the command returns a `NOT_FOUND` error or indicates that the server is no longer registered.

  2. Reprovision the non-root server with clean storage as explained in [Add non-root servers](https://docs.cloud.google.com/spanner-omni/scale-vm-deployment#add-non-root-servers). The server is automatically added to the deployment.




## Next steps

  * [Scale a Kubernetes deployment](https://docs.cloud.google.com/spanner-omni/scale-kubernetes-deployment).

  * [Scale a VM deployment](https://docs.cloud.google.com/spanner-omni/scale-vm-deployment).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
