---
url: https://docs.cloud.google.com/workstations/docs/clone-workstation/
title: Clone a workstation \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:40.004369+00:00
---

# Clone a workstation  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/clone-workstation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Clone a workstation Stay organized with collections  Save and categorize content based on your preferences. 

You can quickly clone the content of an existing workstation when creating a new workstation. This can be helpful in certain cases when the region of the source workstation is experiencing instability.

**Note:** Cloning a workstation _preserves_ the size of the _source_ workstation's home disk.

## Before you begin

Before you clone a workstation, make sure you have the right permissions to the source workstation:

  1. You must have the `workstations.workstations.use` permission on the source workstation.
  2. The [**Cloud Workstations Service Agent**](https://docs.cloud.google.com/workstations/docs/service-accounts#workstations-service-agent) for the project where you are creating the new workstation must have `compute.disks.createSnapshot` and `compute.snapshots.useReadOnly` on the project containing the source workstation. If cloning from a different project, the [**Cloud Workstations Service Agent**](https://docs.cloud.google.com/workstations/docs/service-accounts#workstations-service-agent) must also have the `compute.disks.get` permission on the project containing the source workstation.



## Clone a workstation

To clone a workstation, create a new workstation and specify the source workstation to copy files from:
    
    
        gcloud workstations create WORKSTATION \
          --project=PROJECT \
          --region=REGION \
          --cluster=CLUSTER_NAME \
          --config=CONFIG_NAME \
          --source-workstation=SOURCE_WORKSTATION
    

Replace the following:

  * `WORKSTATION`: the ID or fully qualified identifier for the new workstation

  * `PROJECT`: the project that will contain the new workstation

  * `REGION`: the region where the new workstation will reside—for example, `us-central1`

  * `CLUSTER_NAME`: the name of the workstation cluster that will contain the new workstation

  * `CONFIG_NAME`: the name of the workstation configuration that will contain the new workstation

  * `SOURCE_WORKSTATION`: the fully qualified identifier of the source workstation from which the new workstation's persistent directories will be copied

Your source workstation's identifier might be similar to the following:
        
        projects/SOURCE_PROJECT/locations/SOURCE_REGION/workstationClusters/SOURCE_CLUSTER/workstationConfigs/SOURCE_CONFIG/workstations/SOURCE_WORKSTATION
        

Replace the following:

    * `SOURCE_PROJECT`: the project containing the source workstation
    * `SOURCE_REGION`: the location where the source workstation resides
    * `SOURCE_CLUSTER`: the name of the workstation cluster that contains the source workstation
    * `SOURCE_CONFIG`: the name of the workstation configuration that contains the source workstation
    * `SOURCE_WORKSTATION`: the ID of the source workstation



For more information, see [`gcloud workstations create`](https://cloud.google.com/sdk/gcloud/reference/workstations/create).

For API reference information, see [REST](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs.workstations#resource:-workstation), and [RPC](https://docs.cloud.google.com/workstations/docs/reference/rpc/google.cloud.workstations.v1#workstation).

## Copy a workstation's files to a new workstation with a larger disk

When you clone a workstation, the new workstation retains the size of the source disk. If you need more storage, you can copy a workstation's files to a new workstation with a larger disk:

  1. Create a new destination workstation using a configuration that specifies a larger persistent disk.

  2. Start both the source workstation and the destination workstation.

  3. Access a terminal on the destination workstation by launching it in the Google Cloud console or connecting to it using SSH.

  4. From the terminal on the destination workstation, create a TCP tunnel to the source workstation using [`gcloud workstations start-tcp-tunnel`](https://cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel).
         
         gcloud workstations start-tcp-tunnel \
           --project=SOURCE_PROJECT \
           --region=SOURCE_REGION \
           --cluster=SOURCE_CLUSTER \
           --config=SOURCE_CONFIG \
           SOURCE_WORKSTATION \
           WORKSTATION_PORT \
           --local-host-port=:LOCAL_PORT
         

Replace the following:

     * `WORKSTATION_PORT`: the port on the source workstation to which traffic should be sent (default: `22`).
     * `LOCAL_PORT` (Optional): the localhost port from which traffic will be sent. Valid port numbers are `1024` to `65535`. If you omit the `--local-host-port` flag or specify a port of `0` an unused port is selected automatically.

When the tunnel is ready it will display the port number:
    
    Listening on port [LOCAL_PORT].
    

  5. In another terminal on the destination workstation, run `scp` and specify the port where the TCP tunnel is listening to copy the files from the source workstation.
         
         scp -rP LOCAL_PORT \
             user@localhost:~/SOURCE_DIRECTORY \
             ~/DESTINATION_DIRECTORY
         

Replace the following:

     * `SOURCE_DIRECTORY`: the path to the directory to copy from the source workstation
     * `DESTINATION_DIRECTORY`: the path to the destination directory on the new workstation



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
