---
url: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nvme-tcp-clients/
title: Connect NVMe/TCP clients \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:01.186745+00:00
---

# Connect NVMe/TCP clients  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nvme-tcp-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Connect NVMe/TCP clients Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** NetApp Volumes provides block storage with iSCSI and NVMe/TCP protocols for the Flex Unified service level. You can only use NVMe/TCP with ONTAP-mode.

This page describes how to connect NVMe/TCP clients.

Use the following instructions to configure an NVMe subsystem and connect your clients.

  1. Obtain the NVMe qualified name (NQN) from the NVMe client.

  2. Create an [NVMe subsystem](https://docs.netapp.com/us-en/ontap-cli/vserver-nvme-subsystem-create.html).
         
         gcloud netapp storage-pools execute POOL_NAME \
            --project=PROJECT_ID \
            --location=LOCATION \
            "vserver nvme subsystem create -vserver VSERVER_NAME -subsystem SUBSYSTEM_NAME -ostype OS_TYPE"

  3. Attach the [host to the NVMe subsystem](https://docs.netapp.com/us-en/ontap-cli/vserver-nvme-subsystem-host-add.html) by using the NQN obtained in the previous step.
         
         gcloud netapp storage-pools execute POOL_NAME \
            --project=PROJECT_ID \
            --location=LOCATION \
            "vserver nvme subsystem host add -vserver VSERVER_NAME -subsystem SUBSYSTEM_NAME -host-nqn HOST_NQN -proximal-vservers VSERVER_NAME"

  4. Attach the [NVMe namespace to the subsystem](https://docs.netapp.com/us-en/ontap-cli/vserver-nvme-subsystem-map-add.html).
         
         gcloud netapp storage-pools execute POOL_NAME \
            --project=PROJECT_ID \
            --location=LOCATION \
            "vserver nvme subsystem map add -vserver VSERVER_NAME -subsystem SUBSYSTEM_NAME -path NAMESPACE_PATH"

  5. Find the IP address for the NVMe interface by looking up all network interfaces for the data protocol `nvme`.
         
         gcloud netapp storage-pools execute POOL_NAME \
            --project=PROJECT_ID \
            --location=LOCATION \
            "net int show -data-protocol nvme"

  6. On the NVMe client, perform the following steps to discover and connect to the NVMe namespace:

The following example commands show how to perform NVMe/TCP discovery and connection on Linux NVMe/TCP clients. For more information about advanced options, see the vendor documentation.

     1. Discover the NVMe controllers using the NVMe interface IP address found in the previous step.
            
            sudo nvme discover -t tcp -a NVME_IP_ADDRESS -s 8009

     2. Connect to the discovered NVMe controllers.
            
            sudo nvme connect -t tcp -a NVME_IP_ADDRESS -s 4420 -n SUBSYSTEM_NQN




Replace the following information:

  * `POOL_NAME`: the name of the storage pool.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the storage pool.

  * `VSERVER_NAME`: the name of the vserver.

  * `SUBSYSTEM_NAME`: the name of the NVMe subsystem.

  * `OS_TYPE`: the operating system type of the host, for example `linux`.

  * `HOST_NQN`: the NVMe qualified name (NQN) of the NVMe client.

  * `NAMESPACE_PATH`: the path to the NVMe namespace, for example, `/vol/my_volume/my_namespace`.

  * `NVME_IP_ADDRESS`: the IP address of the NVMe interface.

  * `SUBSYSTEM_NQN`: the NQN of the NVMe subsystem that you created.




After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## Firewall rules for access to NVMe/TCP volumes

For NVMe/TCP access, NetApp Volumes uses specific network ports to enable communication between initiators (clients) and targets (storage volumes). For communication between Google Compute Engine and NetApp Volumes, these ports aren't blocked by default. If you use a firewall, you must enable access to the following ports for the full [NetApp Volume PSA CIDR](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking#configure_private_services_access) or the individual volume IP addresses:

  * `4420 TCP NVMe/TCP I/O Controller`

  * `8009 TCP NVMe/TCP Discovery Controller`




## What's next

  * [Protect your data](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/protect-your-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
