---
url: https://docs.cloud.google.com/filestore/docs/editing-instances/
title: Edit instances \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:16.292072+00:00
---

# Edit instances  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/editing-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Edit instances Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to edit a Filestore instance using either the Google Cloud console or the gcloud CLI.

Once created, you can modify a Filestore instance in the following ways:

  * Increase its capacity
  * Decrease capacity for the following [service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers): 
    * Zonal
    * Regional
    * Enterprise
  * [Configure performance](https://docs.cloud.google.com/filestore/docs/custom-performance)
  * Change its description
  * Manage IP-based access control rules
  * Manage labels 
    * For more information, see [Managing labels](https://docs.cloud.google.com/filestore/docs/managing-labels).



For details on scaling capacity, see [Scale capacity](https://docs.cloud.google.com/filestore/docs/scale).

Certain specifications, such as the instance's IP address, are immutable.

## Instructions for editing an instance

###  Google Cloud console 

To edit Filestore instances using the Google Cloud console, navigate to the **Edit instance** page, where you can edit the instance description, manage IP-based access control rules, and scale the file share performance:

  1. In the Google Cloud console, go to the Filestore Instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click the instance ID of the instance you want to edit.

  3. On the **Instance details** page, click **Edit** to go to the **Edit instance** page.

  4. Change the instance description, IP-based access control rules, and capacity as needed. For details, see [Creating instances](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_ip-based_access_control).

  5. Click **Save**.




###  gcloud 

### Before you begin

To use the gcloud CLI, you must either [install the gcloud CLI](https://docs.cloud.google.com/sdk/downloads) or use the Cloud Shell that's built into the Google Cloud console:

[Go to the Google Cloud console](https://console.cloud.google.com/)

### `gcloud` command for editing an instance

You can edit a Filestore instance by running the [`instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/update) command. If you need to update the configuration rules for IP-based access control, you must use the `--flags-file` flag and specify a JSON configuration file. If you choose this method, you don't need to use the `--file-share` flag because it is already included in the JSON configuration file.
    
    
    gcloud filestore instances update INSTANCE_ID
        --[project="PROJECT_ID"]
        --[location=LOCATION]
        --[performance=PERFORMANCE] \
        --[file-share=name="FILE_SHARE_NAME",CAPACITY=FILE_SHARE_SIZE]
        --[description="DESCRIPTION"]
        --[flags-file=FILE_NAME.json]
    

where:

  * INSTANCE_ID is the instance ID of the Filestore instance you want to edit.
  * PROJECT_ID is the project ID of the Google Cloud project that contains the Filestore instance. You can skip this flag if the Filestore instance is in the `gcloud` default project. You can set the default project by running:
        
        gcloud config set project project-id
        

  * LOCATION is the location where the Filestore instance resides. For regional and enterprise instances, specify a region. For all other instances, specify a zone. Run the [`gcloud filestore zones list`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/zones/list) command to get a list of supported zones. You can skip this flag if the Filestore instance is in the `gcloud` default zone. You can set the default zone by running:
        
        gcloud config set filestore/zone zone
        

  * PERFORMANCE is the [performance configuration](https://docs.cloud.google.com/filestore/docs/custom-performance) used to specify custom performance settings independently of the chosen capacity. 

**Note:** After activating custom performance for an instance you can't deactivate it for that instance. Instances with activated custom performance are billed according to purchased IOPS. For details, see [ configure custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance#enable-custom-performance) and [ Filestore pricing](https://docs.cloud.google.com/filestore/pricing).

You can use only one of the following options:

    * `max-iops-per-tb` specifies an IOPS-per-TiB rate that scales linearly with instance capacity.
    * `max-iops` specifies fixed IOPS rate that doesn't scale with instance capacity.

The format looks as follows:
          
          --performance=max-iops-per-tb=17000
          

  * FILE_SHARE_NAME is the name of the file share that is served from the Filestore instance. File share names cannot be changed after instance creation.

  * FILE_SHARE_SIZE is the new size you want for the file share. You can specify the file share size in whole numbers using either `GiB` (default) or `TiB`.

To see your available quota, go to the Quotas page in the Google Cloud console:

[Go to the Quotas page](https://console.cloud.google.com/iam-admin/quotas)

  * DESCRIPTION is the optional Filestore instance description.

  * FILE_NAME is the name of the json configuration file for IP- based access control.

Example json configuration file:
        
        {
        "--file-share":
          {
            "capacity": "4096",
            "name": "my_vol",
            "nfs-export-options": [
              {
                "access-mode": "READ_WRITE",
                "ip-ranges": [
                  "10.0.0.0",
                  "10.2.0.0"
                ],
                "squash-mode": "ROOT_SQUASH",
                "anon_uid": 1003,
                "anon_gid": 1003
              },
               {
                "access-mode": "READ_ONLY",
                "ip-ranges": [
                  "10.0.1.0/28"
                ],
                "squash-mode": "NO_ROOT_SQUASH"
              }
            ],
          }
        }
        

where:

    * **ip-ranges** is the IP address or range to grant access to. You can specify multiple IP addresses or ranges by separating them with a comma. Only the following service tiers support configuration settings for [overlapping IP address ranges](https://docs.cloud.google.com/filestore/docs/access-control#overlapping-permissions): 
      * Zonal
      * Regional
      * Enterprise
    * **access-mode** is the access level to grant to clients whose IP address falls within **ip-range**. It can have the values of `READ_WRITE` or `READ_ONLY`. The default value is `READ_WRITE`.
    * **squash-mode** can have the values `ROOT_SQUASH` or `NO_ROOT_SQUASH`. `ROOT_SQUASH` removes root level access to the clients whose IP address falls within **ip-range** , while `NO_ROOT_SQUASH` enables root access. The default value is `NO_ROOT_SQUASH`.
    * **anon_uid** is the user ID value that you want to map to `anon_uid`. The default value is `65534`.
    * **anon_gid** is the group ID value that you want to map to `anon_gid`. The default value is `65534`.



##### Example

The following example updates the `nfs-server` instance by increasing the file share size to 3 `TiB`.
    
    
        gcloud filestore instances update nfs-server --zone=us-central1-c --file-share=name="vol1",capacity=3TiB
      ```
    

###  REST API 

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [Filestore API](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/patch):
         
         curl --request PATCH \
             'https://file.googleapis.com/v1/projects/PROJECT/locations/LOCATION/instances?instanceId=NAME?updateMask=performanceConfig%2CdeletionProtectionReason%2CdeletionProtectionEnabled&key=YOUR_API_KEY' \
             --header "Authorization: Bearer $(gcloud auth print-access-token)" \
             --header 'Accept: application/json' \
             --header 'Content-Type: application/json' \
             --data '{
                     "tier":"TIER",
                     "networks":[
                         {
                         "network":"NETWORK"
                         }
                       ],
                     "performanceConfig": {"PERFORMANCE"}
                     "fileShares":[
                       {"capacityGb":CAPACITY,"name":"SHARE_NAME"}
                       ],
                     "deletionProtectionEnabled": true,
                     "deletionProtectionReason": "PROTECTION_REASON"}' \
             --compressed
         
         

Where:

     * `PROJECT` is the name of the project where your instance will reside. For example, `my-genomics-project`.
     * `LOCATION` is the location where the instance will reside. For example, `us-east1` or `us-central1-a`.
     * `NAME` is the name of the instance you want to create. For example, `my-genomics-instance`.
     * `PERFORMANCE` is the [performance configuration](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#performanceconfig) used to specify custom performance settings. 

**Note:** After activating custom performance for an instance you can't deactivate it for that instance. Instances with activated custom performance are billed according to purchased IOPS. For details, see [ configure custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance#enable-custom-performance) and [ Filestore pricing](https://docs.cloud.google.com/filestore/pricing).

You can use only one of the provided options.

       * `iopsPerTB` enables custom performance with a user-defined IOPS rate that scales with instance capacity. To define IOPS per TiB, use the `maxIopsPerTb` field.
       * `fixedIops` enables custo, performance with a fixed IOPS rate that doesn't scale with instance capacity. To define fixed IOPS value, use the `maxIops` field.

The format is as follows:
             
             "performanceConfig": {
                 "iopsPerTb" : {
                     "maxIopsPerTb":17000
                 }
               }
             

     * `CAPACITY` is the size, in GiB, you want to allocate for the instance. For example, `1024`.

     * `SHARE_NAME` is the name of the file share. For example, `vol1`.

     * `PROTECTION_REASON` if you choose to use the `deletionProtectionEnabled` flag, you have the option of adding a note regarding the setting. To add the note, use the optional `deletionProtectionReason` flag and include a description of the justification for the setting you chose. For example, "All genomics data must adhere to current organization policies." For more information, see [Deletion protection](https://docs.cloud.google.com/filestore/docs/deletion-protection).

### Example

The following example updates the `nfs-server` instance by decreasing the IOPS per TiB ratio to `12000`.
    
    curl --request PATCH \
        'https://file.googleapis.com/v1/projects/my-project/locations/us-central1/instances?instanceId=nfs-server?updateMask=performanceConfig%2CdeletionProtectionReason&key=12334fr232' \
        --header "Authorization: Bearer $(gcloud auth print-access-token)" \
        --header 'Accept: application/json' \
        --header 'Content-Type: application/json' \
        --data '{
                  "performanceConfig":
                    {
                      "iopsPerTb":
                        {
                          "maxIopsPerTb":12000
                        }
                    },
                  "deletionProtectionReason":"Deletion+not+allowed"}' \
        --compressed
    
    




## What's next

  * [Create another instance](https://docs.cloud.google.com/filestore/docs/creating-instances).
  * [Mount the Filestore file share on a Compute Engine VM instance](https://docs.cloud.google.com/filestore/docs/mounting-fileshares).
  * [Access Filestore instances with the Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/csi-driver).
  * [Scale capacity](https://docs.cloud.google.com/filestore/docs/scale)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
