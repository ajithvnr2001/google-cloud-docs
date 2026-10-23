---
url: https://docs.cloud.google.com/spanner-omni/scale-vm-deployment/
title: Scale a VM deployment \u00a0|\u00a0 Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:47.133111+00:00
---

# Scale a VM deployment  |  Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/scale-vm-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Scale a VM deployment Stay organized with collections  Save and categorize content based on your preferences. 

To handle shifting database traffic or store more partitions, you can adjust the number of server nodes in your virtual machine environment. Use these procedures to manage VM deployments.

## Before you begin

To scale your VM deployment, follow these steps:

  * [Create Spanner Omni on a VM](https://docs.cloud.google.com/spanner-omni/deploy-on-vms).

  * Download and install the [Spanner Omni CLI](https://docs.cloud.google.com/spanner-omni/cli-quickstart#step-1-download-install-cli).

  * Familiarize yourself with the concepts described in [Create a deployment for Spanner Omni on VMs](https://docs.cloud.google.com/spanner-omni/deploy-on-vms) because scaling operations use similar Spanner Omni CLI patterns.




As a best practice, we recommend scaling vertically up to 32 GB of memory per server before adding more servers to scale horizontally.

## Add root servers

Add a new root server to a VM deployment by following these steps:

  1. Start a new server in a new VM in an existing zone. Initialize the server by using the `spanner start` command. The following example starts a root server:
         
         spanner start \
           --root \
           --server-address=HOSTNAME \
           --zone=ZONE \
           --base-dir=BASE_DIR
         

Replace the following:

     * `HOSTNAME`: The resolvable fully qualified domain name (FQDN) or hostname of the new VM—for example, `new-root-server.example.com`.
     * `ZONE`: The target zone—for example, `us-central1-a`.
     * `BASE_DIR`: The directory path where data is stored—for example, `/spanner`.
  2. Add the server to the existing deployment. Register the new root server with the primary deployment. Ensure that the hostname and port arguments match the parameters used in the `spanner start` command, and specify the zone to assign to the root server.
         
         spanner deployment servers create SERVER_ENDPOINT \
           --zone=ZONE \
           --deployment-endpoint=ENDPOINT
         

Replace the following:

     * `SERVER_ENDPOINT`: The address of the new root server—for example, `new-root-server.example.com:15000`.
     * `ZONE`: The target zone—for example, `us-central1-a`.
     * `ENDPOINT`: The endpoint of your primary deployment—for example, `my-spanner-deployment:15000`.

The `spanner deployment servers create` command starts a _long-running operation_ to add the server to the deployment. Long-running operations might take a substantial amount of time to complete. For more information, see [Manage and observe long-running operations](https://docs.cloud.google.com/spanner/docs/manage-and-observe-long-running-operations) in Spanner documentation.

  3. Verify that the server joined the deployment. List the servers to verify the server has been registered and has transitioned to the `Ready` state:
         
         spanner deployment servers list \
           --zone=ZONE \
           --deployment-endpoint=ENDPOINT
         




## Add non-root servers

To add a non-root server, start the `spanner` process on a VM and configure it to connect to one or more root servers in the cluster to join the deployment.

This example starts a non-root server and adds it to the deployment:
    
    
    spanner start \
      --server-address=HOSTNAME \
      --join-servers=JOIN_SERVERS \
      --zone=ZONE \
      --base-dir=BASE_DIR
    

Replace the following:

  * `HOSTNAME`: The hostname of the new VM—for example, `new-non-root-server.example.com`.
  * `JOIN_SERVERS`: A comma-separated list of existing root server endpoints—for example, `root-server1.example.com:15000`.
  * `ZONE`: The zone name—for example, `us-central1-a`.
  * `BASE_DIR`: The directory path where data is stored—for example, `/spanner`.



## Remove servers

Follow the same steps to remove either a root server or a non-root server. If you're removing a root server, ensure that you maintain an odd number of total root servers in the deployment (between 1 and 9).

To decommission a VM server, follow these steps:

  1. Delete the server from the deployment:
         
         spanner deployment servers delete SERVER_ENDPOINT \
           --zone=ZONE \
           --deployment-endpoint=ENDPOINT
         

Replace the following:

     * `SERVER_ENDPOINT`: The address of the server to remove—for example, `server-to-remove:15000`.
     * `ZONE`: The zone containing the server—for example, `us-central1-a`.
     * `ENDPOINT`: The endpoint of your primary deployment—for example, `my-spanner-deployment:15000`.
  2. Wait for data relocation to complete. Partition relocation takes time depending on the size of the datastore hosted on the server. Monitor the server status until the server is no longer listed in the output:
         
         spanner deployment servers list \
           --zone=ZONE \
           --deployment-endpoint=ENDPOINT
         

  3. Shut down the server process. Sign in to the VM, and stop the `spanner` process.

To avoid data corruption or causing disconnected servers to record conflicting updates, don't restart the `spanner` process on this VM using the same `base_dir` without first purging old data folders.




## Next steps

  * Learn how to [maintain a deployment](https://docs.cloud.google.com/spanner-omni/maintain-deployment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
