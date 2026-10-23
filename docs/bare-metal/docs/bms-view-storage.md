---
url: https://docs.cloud.google.com/bare-metal/docs/bms-view-storage/
title: View storage volumes \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:24.225996+00:00
---

# View storage volumes  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-view-storage/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View storage volumes

Paying attention to your storage resources in the Bare Metal Solution environment helps you determine if your servers have enough storage capacity for applications and workloads.

To view the details of your storage volumes, follow these steps:

###  Console 

  1. Go to the **Volumes** page.

[Go to Volumes](https://console.cloud.google.com/compute/bareMetalSolution/volumes)

The **Volumes** page lists all your storage volumes with the following details:

**Field** | **Description** | **Example**  
---|---|---  
**Status** | Indicates the availability of a storage volume | A green circle with a check mark indicates that the storage volume is ready.  
**ID** | Identifier assigned to your storage volume.  

     * Click the ID to view basic information about the storage volume, including LUNs and snapshots.
     * Share the ID with Google Cloud support when troubleshooting this resource.
| 
     * Boot volume:   
`at-1234567-svr001-vol000-b1`
     * Fibre Channel volume:   
`at-1111111-vol001`
     * NFS share:   
`at-2222222-nfs001-vol000`  
**Name** | Storage volume name. Click the name to view additional information about the storage volume, including LUNs and snapshots.  
  
**Note:** If you did not enter a name when you provisioned your storage volume, the **ID** appears in this field. | 
     * Boot volume:   
`boot-volume-1`
     * Fibre Channel volume:   
`fibre-channel-volume-5`
     * NFS share:   
`nfs-share-7`  
**Location** | Region where the storage volume is located | `asia-southeast1`  
**Pod** | Pod that contains your storage volume. A pod is a unit of isolation that contains your Bare Metal Solution resources. Resources in different pods cannot be connected. A region can have multiple pods. The **Pod** column is disabled by default. To enable it, do the following:
     1. Click **Column display options** view_column.
     2. Select the **Pod** checkbox.
     3. Click **OK**.
If you don't want to enable the **Pod** column, you can view the pod of a storage volume by clicking the storage volume name. | `asia-southeast1-pod1`  
**Type** | Hard drive or solid-state drive | `HDD - Hard drive`  
**Labels** | Displays any labels you added to this storage resource  
  
You can use labels to filter the console output by copying the text of a label and pasting it in the **Filter** box just above the **Status** field. | `environment:test`  



###  gcloud 

  1. To view all storage volumes in your Bare Metal Solution environment and see their status, enter your project ID and issue the `gcloud bms volumes list` command:
         
         gcloud bms volumes list --project=PROJECT_ID
         

The following output example shows three storage volumes, the project ID, region, volume size and storage type. 
         
         NAME                         PROJECT              REGION           REQUESTED_SIZE_GIB  STORAGE_TYPE  STATE
         at-1234567-svr001-vol000-b1  PROJECT_ID         REGION         200                 SSD           READY
         at-1111111-vol001            PROJECT_ID         REGION         1024                SSD           READY
         at-2222222-nfs001-vol000     PROJECT_ID         REGION         400                 HDD           READY
         

  2. To view a single storage volume, enter your storage volume name, project ID, and region, and issue the `gcloud bms volumes describe` command:
         
         gcloud bms volumes describe VOLUME_NAME --project=PROJECT_ID --region=REGION
         

The following output example shows the storage volume size, name, snapshot auto deletion policy, state, and storage type. 
         
         currentSizeGib: '250'
         name: projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME
         requestedSizeGib: '250'
         snapshotAutoDeleteBehavior: OLDEST_FIRST
         snapshotReservationDetail:
           reservedSpaceGib: '50'
           reservedSpaceRemainingGib: '50'
         state: READY
         storageType: SSD
         

  3. To view all LUNs for your storage volume, enter your project ID, region, and storage volume name, and issue the `gcloud bms volumes luns list` command:
         
         gcloud bms volumes luns list --project=PROJECT_ID --region=REGION --volume=VOLUME_NAME
         

The following output example shows the names of the LUNs, region, storage volume name, volume size, and the state. 
         
         NAME                         REGION           VOLUME       SIZE_GB  STATE
         at-11111111-vol001-lun000    REGION        VOLUME_NAME 200      READY
         

  4. To view details for a single LUN, enter your project ID, region, and LUN name, and issue the `gcloud bms volumes luns describe` command:
         
         gcloud bms volumes luns describe LUN_NAME --project=PROJECT_ID --region=REGION --volume=VOLUME_NAME
         

The following output example shows the LUN name and storage volume information, such as size, state, storage type, name, and ID. 
         
         bootLun: true
         name: projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME/luns/LUN_NAME
         sizeGb: '200'
         state: READY
         storageType: SSD
         storageVolume: VOLUME_NAME
         wwid: 600a09803831434434244f774d616b94
         




###  API 

  1. Open a Cloud Shell terminal window in your Google Cloud console.

  2. To view all storage volumes in your Bare Metal Solution environment and see their status, enter your project ID and region into the following `curl` command. Copy the command, paste it into the Cloud Shell prompt, and press the **Enter** or **Return** key:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         -H "Content-Type: application/json" \
         "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes"
         

**Note:** When a volume update is in process, the state field appears as **Creating**. When the volume update completes, the state field appears as **Ready**.
  3. To view a single storage volume, enter your project ID, region, and storage volume name and issue the following command:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         -H "Content-Type: application/json" \
         "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME"
         

  4. To view all logical unit numbers (LUNs) for your storage volume, enter your project ID, region, and storage volume name, then issue the following command:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         -H "Content-Type: application/json" \
         "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME/luns
         

  5. To view details for a single LUN, enter your project ID, region, storage volume name, and LUN name and issue the following command:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         -H "Content-Type: application/json" \
         "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME/luns/LUN_NAME"
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
