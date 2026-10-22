---
url: https://docs.cloud.google.com/netapp/volumes/docs/ontap/manage-ontap/
title: Manage ONTAP in ONTAP-mode \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:51.292593+00:00
---

# Manage ONTAP in ONTAP-mode  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/ontap/manage-ontap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage ONTAP in ONTAP-mode Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage ONTAP in [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview#about_ontap-mode).

For security and logging reasons, NetApp Volumes doesn't allow direct connections to the ONTAP management LIF. Therefore, you can't use tools such as SystemManager or SSH to manage the ONTAP system directly. Instead, you can submit ONTAP operations to your ONTAP-mode storage pool using the following methods:

  * The Google Cloud CLI ONTAP CLI proxy

  * A Google proxy API for ONTAP REST API calls




The management tools, such as Terraform, use the Google API proxy to manage ONTAP resources.

## Before you begin

Your Google Cloud CLI version must be at least **559.0.0** to manage ONTAP operations for your ONTAP-mode storage pool. If your version is older, Google Cloud CLI returns an error that the command or flag isn't defined.

## Use Google Cloud CLI ONTAP CLI proxy

While direct SSH access to the ONTAP CLI isn't available, you can send ONTAP CLI commands to your storage pool using Google Cloud CLI.

**Note:** The CLI command is routed through Google APIs. The system filters the CLI command to block disallowed ONTAP actions. For more information, see Allowed ONTAP actions. Cloud Logging logs the API call.

### gcloud

Run an ONTAP command:
    
    
    gcloud netapp storage-pools execute POOL-NAME ONTAP-COMMAND --project PROJECT \
      --location=LOCATION

Replace the following information:

  * `POOL-NAME`: the name of the Flex Unified ONTAP-mode storage pool.

  * `ONTAP-COMMAND`: the ONTAP command you want to run on the cluster or storage pool.

  * `PROJECT`: your project ID.

  * `LOCATION`: the location of your storage pool.




## Use a Google proxy API for ONTAP REST API calls

NetApp Volumes provides a Google API endpoint for each Flex Unified ONTAP-mode storage pool, which lets you send [ONTAP REST API calls](https://docs.netapp.com/us-en/ontap-restapi/getting_started_with_the_ontap_rest_api.html#using-the-ontap-rest-api-online-documentation) to the underlying ONTAP cluster. This lets you control ONTAP features using APIs.

**Note:** Some API actions are blocked. For more information, see Allowed ONTAP actions. All API calls to the Google API are logged in Cloud Logging.

Calls to the ONTAP proxy must use the following URL format:
    
    
      https://netapp.googleapis.com/v1/projects/PROJECT/locations/LOCATION/storagePools/POOL_NAME/ontap/ONTAP_REST_URL
     

This URL consists of following elements:

  * **Baseline URL** : `https://netapp.googleapis.com/v1`

  * **Google URN for the storage pool** : /projects/`PROJECT`/locations/`LOCATION`/storagePools/`POOL_NAME`

Replace the following information:

    * `PROJECT`: your project ID or number.

    * `LOCATION`: the zone name for zonal pools or the region for regional pools.

    * `POOL_NAME`: the name of your pool.

  * [**ONTAP REST API path**](https://docs.netapp.com/us-en/ontap-restapi/getting_started_with_the_ontap_rest_api.html#using-the-ontap-rest-api-online-documentation): /ontap/`ONTAP_REST_URL`. For more information, see the [ONTAP REST API](https://docs.netapp.com/us-en/ontap-restapi/getting_started_with_the_ontap_rest_api.html#using-the-ontap-rest-api-online-documentation) reference.




### List all volumes of a storage pool

The following example shows the full URL to list all volumes for the storage pool `mypool` in `us-central1-a` in project `myproject`.

`https://netapp.googleapis.com/v1/projects/myproject/locations/us-central1-a/storagePools/mypool/ontap/api/storage/volumes`

Like all Google API calls, this call must be authenticated. The following CLI example fetches an API token, and then calls the URL using `curl` to list all volumes in the pool:
    
    
       TOKEN=$(gcloud auth print-access-token)
       curl --location 'https://netapp.googleapis.com/v1/projects/myproject/locations/us-central1-a/storagePools/mypool/ontap/api/storage/volumes' \
       --header "Authorization: Bearer $TOKEN" \
       --header "Content-Type: application/json"
      

**Note:** Access tokens requested using [`gcloud auth print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token) expire after 3,600 seconds.

### List all snapshots of a volume

The following example shows the full URL to list all snapshots for the storage pool `mypool` and volume `volume-uuid` in `us-central1-a` in the project `myproject`.

`https://netapp.googleapis.com/v1/projects/myproject/locations/us-central1-a/storagePools/mypool/ontap/api/storage/volumes/volume-uuid/snapshots`

Like all Google API calls, this call must be authenticated. The following CLI example fetches an API token, and then calls the URL by using `curl` to list all snapshots for the volume:
    
    
       TOKEN=$(gcloud auth print-access-token)
       curl --location 'https://netapp.googleapis.com/v1/projects/myproject/locations/us-central1-a/storagePools/mypool/ontap/api/storage/volumes/volume-uuid/snapshots' \
       --header "Authorization: Bearer $TOKEN" \
       --header "Content-Type: application/json"
      

### Create a volume

This section shows how to create a volume named `myvolume` in an existing Flex Unified ONTAP-mode storage pool, identified by the URN: `/projects/myproject/locations/us-central1-a/storagePools/mypool`, using the ONTAP REST API.

To create a volume, see the [ONTAP REST API online documentation](https://docs.netapp.com/us-en/ontap-restapi/getting_started_with_the_ontap_rest_api.html#using-the-ontap-rest-api-online-documentation). In the documentation, navigate to the **Storage** section, and then expand [Manage storage volumes](https://docs.netapp.com/us-en/ontap-restapi/storage_overview.html). This section provides several examples.

**Note:** Volume names can't contain hyphens (`-`). Instead, use [supported characters](https://kb.netapp.com/on-prem/ontap/Ontap_OS/OS-KBs/Can_a_NetApp_volume_name_contain_a_hyphen_or_dash), such as letters, numbers, and underscores (`_`).

Use the following instructions to create a volume.

  1. Determine the ONTAP REST API endpoint.

Using the [basic example](https://docs.netapp.com/us-en/ontap-restapi/storage_volumes_endpoint_overview.html#creating-a-volume) in NetApp Volumes, the required ONTAP API endpoint is `/api/storage/volumes`. This endpoint creates the URL: `https://netapp.googleapis.com/v1/projects/myproject/locations/us-central1-a/storagePools/mypool/ontap/api/storage/volumes`.

  2. Construct the request payload.

Use the example payload from the ONTAP documentation to match your specific environment. For example:
         
         {
           "name": "vol1",
           "aggregates": [
             {
               "name": "aggr1"
             }
           ],
           "svm": {
             "name": "vs1"
           }
         }
         

When you create a volume, use the `name` field to assign the volume name. The volume creation payload requires the names of the aggregate and the storage virtual machine (SVM) assigned by NetApp Volumes during ONTAP-mode pool creation. In ONTAP-mode, each storage pool has one SVM and one storage aggregate. This information can be retrieved by querying ONTAP for [all SVMs](https://docs.netapp.com/us-en/ontap-restapi/get-svm-svms.html).

To retrieve the SVM and the aggregate names:

     1. **Use** `ontap_fields` **for field selection** : in NetApp Volumes ONTAP-mode pools, use the query parameter `ontap_fields=` instead of the standard ONTAP `fields=` parameter to [specify the requested fields](https://docs.netapp.com/us-en/ontap-restapi/getting_started_with_the_ontap_rest_api.html#Requesting_specific_fields).

     2. Optional: **Use**`jq` **to extract fields** : the following example uses the [jq](https://jqlang.org/tutorial/) open source tool to extract the `name` (SVM name) and `aggregates` from the JSON response, which is useful for processing in shell scripts.
            
            TOKEN=$(gcloud auth print-access-token)
            curl --location 'https://netapp.googleapis.com/v1/projects/myproject/locations/us-central1-a/storagePools/mypool/ontap/api/svm/svms?ontap_fields=name,aggregates' \
            --header "Authorization: Bearer $TOKEN" \
            --header "Content-Type: application/json" | jq '.rawResponse.records[] | {name: .name, aggregates: .aggregates[].name}'
            

Example response:
            
            {
             "name": "gcnv-7cf6ee41c1a94f0-svm-01",
             "aggregates": "aggr1"
            }
            

  3. Execute the volume creation API call.

With the aggregate name (`aggr1`) and the SVM name (`gcnv-7cf6ee41c1a94f0-svm-01`), create the final volume creation payload and submit the API call. Note that the ONTAP API payload must be enclosed within a `body: {}` envelope for NetApp Volumes.

The following example creates a volume named `myvolume` with a size of 2 GB:
         
         curl --location 'https://netapp.googleapis.com/v1/projects/myproject/locations/us-central1-a/storagePools/mypool/ontap/api/storage/volumes' \
         --header "Authorization: Bearer $TOKEN" \
         --header "Content-Type: application/json" \
         --data '{
           "body": {
             "name": "myvolume",
             "aggregates": [
               {
                 "name": "aggr1"
               }
             ],
             "svm": {
               "name": "gcnv-7cf6ee41c1a94f0-svm-01"
             },
             "size": "2GB"
           }
         }'
         

Volume creation supports many [optional parameters](https://docs.netapp.com/us-en/ontap-restapi/post-storage-volumes.html), such as `size`. For example, the payload specifies a 2 GB size. The resource's documentation page lists all available parameters, including required and optional parameters. It also provides detailed examples of payloads and response bodies.

To configure auto-tiering in the ONTAP REST API, include the `tiering` JSON object in the request body:

     * To set the volume's tiering policy to `all`, use `"tiering": {"policy": "all"}`.

     * Optional: To configure the cooling days, use `"tiering": {"policy": "auto", "min_cooling_days": 31}`.

You can specify a cooling threshold between 2 and 183 days in the `min_cooling_days` field. The default cooling threshold value is 31 days.

To bypass the hot tier and write data directly to the cloud tier on read-write (RW) volumes, use the Google Cloud CLI ONTAP CLI proxy with advanced privileges:
    
    set -privilege advanced; volume modify -vserver SVM_NAME -volume VOLUME_NAME -tiering-policy all -is-cloud-write-enabled true

  4. Monitor the ONTAP job.

Most ONTAP API calls, such as `POST` or `PATCH` operations that create or update resources, don't run synchronously. Instead, these calls return an ONTAP job resource, as shown in the volume creation example.

Example job response:
         
         {
           "body": {
             "job": {
               "_links": {
                 "self": {
                   "href": "curl --location
         'https://netapp.googleapis.com/v1/projects/myproject/locations/us-central1-a/storagePools/mypool/ontap/api/cluster/jobs/15be1c46-fd2c-11f0-b3c2-7f15697be61c' \
         --header "Authorization: Bearer $TOKEN" \
         --header "Content-Type: application/json""
                 }
               },
               "uuid": "15be1c46-fd2c-11f0-b3c2-7f15697be61c"
             }
           }
         }
         

To check the job's status, query the job resource using the returned `uuid`:
         
         curl --location 'https://netapp.googleapis.com/v1/projects/myproject/locations/us-central1-a/storagePools/mypool/ontap/api/cluster/jobs/15be1c46-fd2c-11f0-b3c2-7f15697be61c' \
         --header "Authorization: Bearer $TOKEN" \
         --header "Content-Type: application/json"
         

Example response:
         
         {
           "rawResponse": {
             "uuid": "15be1c46-fd2c-11f0-b3c2-7f15697be61c",
             "description": "POST
         /api/storage/volumes/15be0ad9-fd2c-11f0-b3c2-7f15697be61c",
             "state": "success",
             "message": "success",
             "code": 0,
             "start_time": "2026-01-29T16:03:43+00:00",
             "end_time": "2026-01-29T16:03:44+00:00",
             "svm": {
               "name": "gcnv-7cf6ee41c1a94f0-svm-01",
               "uuid": "8a29c15d-fb31-11f0-ab03-03e1bb49206d"
            }
           }
         }
         

If the `state` is `success`, the volume is created.

This example workflow guides you through looking up ONTAP actions in the ONTAP REST API documentation. It also shows you how to create the required payload format and submit it to the storage pool using a Google API. Finally, it demonstrates how to monitor an ONTAP job until the resource is created. With this approach, you can control most ONTAP settings for your storage pool.




## Use Terraform to manage ONTAP-mode

You can manage ONTAP-mode resources by using the CLI proxy. The CLI proxy is effective for interactive use, but automation can be more complex. Terraform consistently manages the lifecycle of cloud resources, and you can use it to manage both NetApp Volumes and ONTAP resources.

Use the [Feature management overview](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview#feature_management_overview) table to help you determine which provider to use.

  * The [Google](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/netapp_storage_pool) provider manages resources through the NetApp Volumes API.

  * The [NetApp-ONTAP](https://registry.terraform.io/providers/NetApp/netapp-ontap/latest/docs) provider manages resources through ONTAP REST APIs.




For example, you create an ONTAP-mode storage pool by using the Google provider, version 7.27.0 or later. And then, to create a volume in that ONTAP-mode pool, you use the NetApp-ONTAP provider, version 2.6.0 or later.

For more information about setup and examples, see [NetApp-ONTAP provider documentation](https://registry.terraform.io/providers/NetApp/netapp-ontap/latest/docs/guides/gcnv-ontap-mode).

## Allowed ONTAP actions

When you access an ONTAP-mode pool through the API or the CLI proxy, you don't have full permissions and can't run all ONTAP commands. This restriction help protect system integrity and prevent changes to underlying physical resources that are managed by the service.

For some APIs, the system filters API request and response payloads. For example, because NetApp Volumes bills for logical capacity, the system blocks parameters for configuring physical capacity. If you send a parameter that isn't allowed, the API returns an error.

For more information about how we bill, see [Billing: logical versus physical capacity](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#billing-logical-vs-physical).

### Supported ONTAP commands

You can manage ONTAP-mode by submitting ONTAP commands using the Google Cloud CLI ONTAP CLI proxy. NetApp Volumes supports most commands to manage SVMs, LUNs, volumes, and ONTAP features. Some commands are blocked to protect system integrity or because they manage physical resources that aren't relevant in a managed service such as NetApp Volumes.

You run commands at the ONTAP administrator privilege level. To switch the privilege level to advanced, add `set advanced;` or `set -privilege advanced;` to the start of your command. A limited set of commands also supports diagnostic (diag) privilege level, which you can access by adding `set diag;` to the start of your command. These privilege shifts aren't persistent.

Because the proxy isn't an interactive shell, you can only run one command at a time. This limitation means that the proxy doesn't support interactive commands that request additional information. For example, you can't create a CIFS or SMB vserver (SVM) that requires Active Directory administrator credentials. The CLI proxy also doesn't support cluster peering because it's an interactive command. To perform those operations, you must use the ONTAP REST API.

The following table lists the supported command families, commands, and limitations of the ONTAP CLI proxy:

Command family | Purpose | Supported commands | Notes  
---|---|---|---  
Cluster | Peer clusters for SnapMirror, FlexCache, and display select information about the cluster | **cluster peer** \- full access  
  
**cluster show** , **identity show** , **date show** , **ha show** , **statistics show** , and **time-service ntp server show** \- read-only | The CLI proxy doesn't support the interactive `cluster peer create` command; use the REST API instead. You can use other `cluster peer` commands, such as `show`.  
Debug | Support packet tracing (tcpdump), LUN, and lock troubleshooting | **debug network tcpdump** , **debug san lun** , and **debug lock persistence** \- full access | All allowed debug commands require the `diag` privilege level. These are common debug commands.  
Event | Create filters to send ONTAP events of interest to SMTP or syslog destinations | **event catalog show** and **event log show** \- read-only  
  
**event config** , **event filter** , and **event notification** \- full access | Lets you log events to custom destinations. You can use `event log show` to display log events by time or type.  
Job | Manage ONTAP jobs at the node and cluster level | **job show** , **job schedule** , **job private** , **job stop** , and **job resume** \- full access |   
LUN | Create and manage LUNs and initiator groups, and import foreign LUNs | **lun create** , **lun bind** , and **igroup** \- full access | While lun import is allowed, it isn't possible to connect foreign disks to an ONTAP-mode system.  
Network | Show network port, interface, route and ipspace configurations, run ping and traceroute to external IP addresses, and show client connections by protocol | **network ping** , **network traceroute** , **network port interface** , **network ipspace** , and **network connections** \- read-only |   
QoS | Create and manage QoS policy-groups and display performance for them | All QoS commands - read-only | QoS settings are view-only.  
Security | Show audit configuration, enable anti-ransomware feature, and create and install certificates | **security audit** \- read-only  
  
**security anti-ransomware volume** and **security certificate** \- full access | Anti-ransomware parameters can be set when creating the volume. You can create only server and client certificates.  
SnapLock | Manage SnapLock clock and logs, and control SnapLock event-based retention and legal hold operations | **snaplock compliance-clock** and **snaplock log** \- full access | Use **volume snaplock modify** command to configure SnapLock on individual volumes. You can manage the SnapLock commands **snaplock event-retention** and **snaplock legal-hold** only by using the ONTAP REST API.  
SnapMirror | Create and manage SnapMirror relationships | **snapmirror create** , **snapmirror initialize** , **snapmirror break** , and **snapmirror resync** \- full access |   
Statistics | Show periodic system statistics or create samples of specific statistics | **statistics samples** , **statistics start** , **statistics stop** , and **statistics show-periodic** \- full access  
  
**statistics volume** , **statistics lun** , **statistics aggregate** , **statistics qtree** , and **statistics SVM** \- read-only | Many commands need advanced mode to specify their parameters.  
System | System commands aren't generally supported, but AutoSupport and performance archive transmission can be invoked | **system node autosupport invoke** and **system node autosupport invoke-performance-archive** \- full access | AutoSupport files are available for NetApp Support.  
Volume | Create and manage volumes | **volume create** , **volume delete** , **volume modify** , **volume clone** , **volume expand** (FlexGroup), **volume flexcache** , **volume flexgroup** , **qtree** , **quota** , **snaplock** , **snapshot** \- full access | Some volume capabilities such as logical space reporting/enforcement and space-guarantee (none) are automatically managed by the system. Set the volume tiering policy to use auto-tiering set at pool level.  
Vserver | Manage the SVM (vserver) for file (SMB, NFS), block (iSCSI, NVMe), and object (S3) access to volumes.  
  
Manage policies used for volumes such as export policies for NFS.  
  
Enable SVM features such as audit logging (file access), consistency groups, policy, name services (DNS, LDAP), and antivirus (vscan).  
  
Peer SVMs for SnapMirror and FlexCache. | **vserver cifs create** (join to an Active Directory domain), **vserver nfs create** , **vserver iscsi create** , and **vserver nvme create** \- full access  
  
**vserver object-store-server** \- full access | Use the **vserver modify** command to set the default language, security style, and snapshot and quota policies for all volumes.  
  
**vserver create** isn't supported at this time.  
Password change commands can't be run as interactive and must be specified by using command parameters, or by using the REST API.  
Legacy commands |  | **timezone** and **version** \- full access |   
  
## Delete an ONTAP-mode pool

To delete an ONTAP-mode pool, you must first delete all volumes in the pool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
