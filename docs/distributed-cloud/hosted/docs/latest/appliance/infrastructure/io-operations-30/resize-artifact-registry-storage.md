---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/resize-artifact-registry-storage/
title: Resize Artifact Registry storage \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:23.706865+00:00
---

# Resize Artifact Registry storage  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/resize-artifact-registry-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Resize Artifact Registry storage Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to check storage availability and resize the Artifact Registry storage if more capacity is required.

Follow these instructions if, during the upgrade process, there is not enough free storage space in the Artifact Registry, which results in operation failures.

## Before you begin

To check storage availability and resize the Artifact Registry storage, you must have the necessary identity and access roles:

  * System Artifact Registry Debugger: has read and write access to all Harbor resources. Ask your Security Admin to grant you the System Artifact Registry Debugger (`sar-debugger`) cluster role.



## Check the storage usage of the Artifact Registry in the org infrastructure cluster

You can check the current Artifact Registry storage usage in the org infrastructure cluster to determine next steps for storage allocation. Work through the following steps:

  1. Export the `kubeconfig` path for the org infrastructure cluster Artifact Registry:
         
         export ORG_INFRA_KUBECONFIG=KUBECONFIG_FILE_PATH
         

Replace `KUBECONFIG_FILE_PATH` with the path to the `kubeconfig` file for the org infrastructure cluster.

  2. Set the existing Artifact Registry pod as an environment variable:
         
         pod=$(kubectl --kubeconfig $ORG_INFRA_KUBECONFIG get pods -n harbor-system -l goharbor.io/operator-controller=registry -o name)
         

  3. Print the output for the Artifact Registry storage usage:
         
         kubectl --kubeconfig $ORG_INFRA_KUBECONFIG exec $pod -n harbor-system \
             -c registry -- df -h
         

Find the mounted path `/var/lib/registry` in the output to view the Artifact Registry storage usage. The following example output shows the Artifact Registry storage usage is 40% and there is 85G of free space:
         
         Filesystem                                    Size Used Avail Use% Mounted on
         overlay                                       484G  43G  441G   9% /
         tmpfs                                          64M    0   64M   0% /dev
         tmpfs                                          24G    0   24G   0% /sys/fs/cgroup
         /dev/sda1                                     484G  43G  441G   9% /storage
         tmpfs                                          43G  12K   43G   1% /harbor_cust_cert/ca.crt
         shm                                            64M    0   64M   0% /dev/shm
         tmpfs                                          43G 4.0K   43G   1% /etc/registry/auth
         /dev/mapper/3600a09807770457a795d5452356a3345 147G  54G   85G  40% /var/lib/registry
         tmpfs                                          24G    0   24G   0% /proc/acpi
         tmpfs                                          24G    0   24G   0% /proc/scsi
         tmpfs                                          24G    0   24G   0% /sys/firmware
         

Verify that the `Avail` size for the `/var/lib/registry` file system is larger than the size of the image file to be uploaded. If necessary, you can resize this storage by following the steps in the next section.




## Apply the new storage size

You can resize the storage of the Artifact Registry, if necessary. Work through the following steps:

  1. Create a new environment variable and set it to the new persistent volume claim (PVC) storage size:
         
         STORAGE_SIZE=400G
         

  2. Apply the new storage size to the Artifact Registry:
         
         kubectl --kubeconfig $ORG_INFRA_KUBECONFIG patch Persistentvolumeclaim/harbor-registry \
             -n harbor-system --type=merge \
             -p '{"spec": {"resources": {"requests": {"storage": "'$STORAGE_SIZE'"}}}}'
         

  3. Restart the Artifact Registry pod to implement the new storage size update:
         
         kubectl --kubeconfig $ORG_INFRA_KUBECONFIG rollout restart deployment \
             -n harbor-system harbor-harbor-harbor-registry
         

  4. Verify your usage amount and capacity increase by checking the Artifact Registry.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
