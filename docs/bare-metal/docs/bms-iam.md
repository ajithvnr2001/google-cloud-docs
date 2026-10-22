---
url: https://docs.cloud.google.com/bare-metal/docs/bms-iam/
title: Configure IAM for Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:10.152441+00:00
---

# Configure IAM for Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-iam/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure IAM for Bare Metal Solution

When you want a [principal](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity), such as a Google Cloud project user or service account, to gain access to the resources in your Bare Metal Solution environment, you need to grant them appropriate roles and permissions. To grant access, you can create an Identity and Access Management (IAM) policy and grant predefined roles specific to Bare Metal Solution.

Grant roles with enough permissions for your principals to be able do their job but no more, so that you can follow the Google Cloud security principle of least privilege.

## Predefined roles for Bare Metal Solution

Each IAM role for Bare Metal Solution contains permissions that give the principal access to specific resources as shown in the following table.

Role | Permissions  
---|---  
  
#### Bare Metal Solution Admin 

(`roles/baremetalsolution.admin`) Administrator of Bare Metal Solution resources  |  `baremetalsolution.instancequotas.list` `baremetalsolution.instances.*`

  * `baremetalsolution.instances.attachNetwork`
  * `baremetalsolution.instances.attachVolume`
  * `baremetalsolution.instances.create`
  * `baremetalsolution.instances.detachLun`
  * `baremetalsolution.instances.detachNetwork`
  * `baremetalsolution.instances.detachVolume`
  * `baremetalsolution.instances.disableInteractiveSerialConsole`
  * `baremetalsolution.instances.enableInteractiveSerialConsole`
  * `baremetalsolution.instances.get`
  * `baremetalsolution.instances.list`
  * `baremetalsolution.instances.rename`
  * `baremetalsolution.instances.reset`
  * `baremetalsolution.instances.start`
  * `baremetalsolution.instances.stop`
  * `baremetalsolution.instances.update`

`baremetalsolution.luns.create` `baremetalsolution.luns.delete` `baremetalsolution.luns.evict` `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.luns.update` `baremetalsolution.maintenanceevents.*`

  * `baremetalsolution.maintenanceevents.addProposal`
  * `baremetalsolution.maintenanceevents.approve`
  * `baremetalsolution.maintenanceevents.get`
  * `baremetalsolution.maintenanceevents.list`

`baremetalsolution.networkquotas.list` `baremetalsolution.networks.*`

  * `baremetalsolution.networks.create`
  * `baremetalsolution.networks.delete`
  * `baremetalsolution.networks.get`
  * `baremetalsolution.networks.list`
  * `baremetalsolution.networks.rename`
  * `baremetalsolution.networks.update`

`baremetalsolution.nfsshares.*`

  * `baremetalsolution.nfsshares.create`
  * `baremetalsolution.nfsshares.delete`
  * `baremetalsolution.nfsshares.get`
  * `baremetalsolution.nfsshares.list`
  * `baremetalsolution.nfsshares.rename`
  * `baremetalsolution.nfsshares.update`

`baremetalsolution.operations.get` `baremetalsolution.osimages.list` `baremetalsolution.pods.list` `baremetalsolution.procurements.*`

  * `baremetalsolution.procurements.create`
  * `baremetalsolution.procurements.get`
  * `baremetalsolution.procurements.list`

`baremetalsolution.skus.list` `baremetalsolution.snapshotschedulepolicies.*`

  * `baremetalsolution.snapshotschedulepolicies.create`
  * `baremetalsolution.snapshotschedulepolicies.delete`
  * `baremetalsolution.snapshotschedulepolicies.get`
  * `baremetalsolution.snapshotschedulepolicies.list`
  * `baremetalsolution.snapshotschedulepolicies.update`

`baremetalsolution.sshKeys.*`

  * `baremetalsolution.sshKeys.create`
  * `baremetalsolution.sshKeys.delete`
  * `baremetalsolution.sshKeys.list`

`baremetalsolution.storageaggregatepools.list` `baremetalsolution.volumequotas.list` `baremetalsolution.volumes.create` `baremetalsolution.volumes.delete` `baremetalsolution.volumes.evict` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumes.rename` `baremetalsolution.volumes.resize` `baremetalsolution.volumes.update` `baremetalsolution.volumesnapshots.*`

  * `baremetalsolution.volumesnapshots.create`
  * `baremetalsolution.volumesnapshots.delete`
  * `baremetalsolution.volumesnapshots.get`
  * `baremetalsolution.volumesnapshots.list`
  * `baremetalsolution.volumesnapshots.restore`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Bare Metal Solution Editor 

(`roles/baremetalsolution.editor`) Editor of Bare Metal Solution resources  |  `baremetalsolution.instancequotas.list` `baremetalsolution.instances.*`

  * `baremetalsolution.instances.attachNetwork`
  * `baremetalsolution.instances.attachVolume`
  * `baremetalsolution.instances.create`
  * `baremetalsolution.instances.detachLun`
  * `baremetalsolution.instances.detachNetwork`
  * `baremetalsolution.instances.detachVolume`
  * `baremetalsolution.instances.disableInteractiveSerialConsole`
  * `baremetalsolution.instances.enableInteractiveSerialConsole`
  * `baremetalsolution.instances.get`
  * `baremetalsolution.instances.list`
  * `baremetalsolution.instances.rename`
  * `baremetalsolution.instances.reset`
  * `baremetalsolution.instances.start`
  * `baremetalsolution.instances.stop`
  * `baremetalsolution.instances.update`

`baremetalsolution.luns.create` `baremetalsolution.luns.delete` `baremetalsolution.luns.evict` `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.luns.update` `baremetalsolution.maintenanceevents.*`

  * `baremetalsolution.maintenanceevents.addProposal`
  * `baremetalsolution.maintenanceevents.approve`
  * `baremetalsolution.maintenanceevents.get`
  * `baremetalsolution.maintenanceevents.list`

`baremetalsolution.networkquotas.list` `baremetalsolution.networks.*`

  * `baremetalsolution.networks.create`
  * `baremetalsolution.networks.delete`
  * `baremetalsolution.networks.get`
  * `baremetalsolution.networks.list`
  * `baremetalsolution.networks.rename`
  * `baremetalsolution.networks.update`

`baremetalsolution.nfsshares.*`

  * `baremetalsolution.nfsshares.create`
  * `baremetalsolution.nfsshares.delete`
  * `baremetalsolution.nfsshares.get`
  * `baremetalsolution.nfsshares.list`
  * `baremetalsolution.nfsshares.rename`
  * `baremetalsolution.nfsshares.update`

`baremetalsolution.operations.get` `baremetalsolution.osimages.list` `baremetalsolution.pods.list` `baremetalsolution.procurements.*`

  * `baremetalsolution.procurements.create`
  * `baremetalsolution.procurements.get`
  * `baremetalsolution.procurements.list`

`baremetalsolution.skus.list` `baremetalsolution.snapshotschedulepolicies.*`

  * `baremetalsolution.snapshotschedulepolicies.create`
  * `baremetalsolution.snapshotschedulepolicies.delete`
  * `baremetalsolution.snapshotschedulepolicies.get`
  * `baremetalsolution.snapshotschedulepolicies.list`
  * `baremetalsolution.snapshotschedulepolicies.update`

`baremetalsolution.sshKeys.*`

  * `baremetalsolution.sshKeys.create`
  * `baremetalsolution.sshKeys.delete`
  * `baremetalsolution.sshKeys.list`

`baremetalsolution.storageaggregatepools.list` `baremetalsolution.volumequotas.list` `baremetalsolution.volumes.create` `baremetalsolution.volumes.delete` `baremetalsolution.volumes.evict` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumes.rename` `baremetalsolution.volumes.resize` `baremetalsolution.volumes.update` `baremetalsolution.volumesnapshots.*`

  * `baremetalsolution.volumesnapshots.create`
  * `baremetalsolution.volumesnapshots.delete`
  * `baremetalsolution.volumesnapshots.get`
  * `baremetalsolution.volumesnapshots.list`
  * `baremetalsolution.volumesnapshots.restore`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Bare Metal Solution Viewer 

(`roles/baremetalsolution.viewer`) Viewer of Bare Metal Solution resources  |  `baremetalsolution.instancequotas.list` `baremetalsolution.instances.get` `baremetalsolution.instances.list` `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.maintenanceevents.get` `baremetalsolution.maintenanceevents.list` `baremetalsolution.networkquotas.list` `baremetalsolution.networks.get` `baremetalsolution.networks.list` `baremetalsolution.nfsshares.get` `baremetalsolution.nfsshares.list` `baremetalsolution.operations.get` `baremetalsolution.osimages.list` `baremetalsolution.pods.list` `baremetalsolution.procurements.get` `baremetalsolution.procurements.list` `baremetalsolution.skus.list` `baremetalsolution.snapshotschedulepolicies.get` `baremetalsolution.snapshotschedulepolicies.list` `baremetalsolution.sshKeys.list` `baremetalsolution.storageaggregatepools.list` `baremetalsolution.volumequotas.list` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumesnapshots.get` `baremetalsolution.volumesnapshots.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Bare Metal Solution Instances Admin 

(`roles/baremetalsolution.instancesadmin`) Admin of Bare Metal Solution Instance resources  |  `baremetalsolution.instances.*`

  * `baremetalsolution.instances.attachNetwork`
  * `baremetalsolution.instances.attachVolume`
  * `baremetalsolution.instances.create`
  * `baremetalsolution.instances.detachLun`
  * `baremetalsolution.instances.detachNetwork`
  * `baremetalsolution.instances.detachVolume`
  * `baremetalsolution.instances.disableInteractiveSerialConsole`
  * `baremetalsolution.instances.enableInteractiveSerialConsole`
  * `baremetalsolution.instances.get`
  * `baremetalsolution.instances.list`
  * `baremetalsolution.instances.rename`
  * `baremetalsolution.instances.reset`
  * `baremetalsolution.instances.start`
  * `baremetalsolution.instances.stop`
  * `baremetalsolution.instances.update`

`baremetalsolution.operations.get` `baremetalsolution.osimages.list` `baremetalsolution.pods.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Bare Metal Solution Instances Viewer 

(`roles/baremetalsolution.instancesviewer`) Viewer of Bare Metal Solution Instance resources  |  `baremetalsolution.instancequotas.list` `baremetalsolution.instances.get` `baremetalsolution.instances.list` `baremetalsolution.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Luns Admin 

(`roles/baremetalsolution.lunsadmin`) Administrator of Bare Metal Solution Lun resources  |  `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.operations.get`  
  
#### Luns Viewer 

(`roles/baremetalsolution.lunsviewer`) Viewer of Bare Metal Solution Lun resources  |  `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.operations.get`  
  
#### Maintenance Events Admin 

(`roles/baremetalsolution.maintenanceeventsadmin`) Administrator of Bare Metal Solution maintenance events resources  |  `baremetalsolution.maintenanceevents.*`

  * `baremetalsolution.maintenanceevents.addProposal`
  * `baremetalsolution.maintenanceevents.approve`
  * `baremetalsolution.maintenanceevents.get`
  * `baremetalsolution.maintenanceevents.list`

  
  
#### Maintenance Events Editor 

(`roles/baremetalsolution.maintenanceeventseditor`) Editor of Bare Metal Solution maintenance events resources  |  `baremetalsolution.maintenanceevents.*`

  * `baremetalsolution.maintenanceevents.addProposal`
  * `baremetalsolution.maintenanceevents.approve`
  * `baremetalsolution.maintenanceevents.get`
  * `baremetalsolution.maintenanceevents.list`

  
  
#### Maintenance Events Viewer 

(`roles/baremetalsolution.maintenanceeventsviewer`) Viewer of Bare Metal Solution maintenance events resources  |  `baremetalsolution.maintenanceevents.get` `baremetalsolution.maintenanceevents.list`  
  
#### Networks Admin 

(`roles/baremetalsolution.networksadmin`) Admin of Bare Metal Solution networks resources  |  `baremetalsolution.networkquotas.list` `baremetalsolution.networks.*`

  * `baremetalsolution.networks.create`
  * `baremetalsolution.networks.delete`
  * `baremetalsolution.networks.get`
  * `baremetalsolution.networks.list`
  * `baremetalsolution.networks.rename`
  * `baremetalsolution.networks.update`

`baremetalsolution.operations.get` `baremetalsolution.pods.list`  
  
#### NFS Shares Admin 

(`roles/baremetalsolution.nfssharesadmin`) Administrator of Bare Metal Solution NFS Share resources  |  `baremetalsolution.nfsshares.*`

  * `baremetalsolution.nfsshares.create`
  * `baremetalsolution.nfsshares.delete`
  * `baremetalsolution.nfsshares.get`
  * `baremetalsolution.nfsshares.list`
  * `baremetalsolution.nfsshares.rename`
  * `baremetalsolution.nfsshares.update`

`baremetalsolution.operations.get` `baremetalsolution.pods.list`  
  
#### NFS Shares Editor 

(`roles/baremetalsolution.nfsshareseditor`) Editor of Bare Metal Solution NFS Share resources  |  `baremetalsolution.nfsshares.*`

  * `baremetalsolution.nfsshares.create`
  * `baremetalsolution.nfsshares.delete`
  * `baremetalsolution.nfsshares.get`
  * `baremetalsolution.nfsshares.list`
  * `baremetalsolution.nfsshares.rename`
  * `baremetalsolution.nfsshares.update`

`baremetalsolution.operations.get` `baremetalsolution.pods.list`  
  
#### NFS Shares Viewer 

(`roles/baremetalsolution.nfssharesviewer`) Viewer of Bare Metal Solution NFS Share resources  |  `baremetalsolution.nfsshares.get` `baremetalsolution.nfsshares.list` `baremetalsolution.operations.get`  
  
#### OS Images Viewer 

(`roles/baremetalsolution.osimagesviewer`) Viewer of Bare Metal Solution OS images resources  |  `baremetalsolution.osimages.list`  
  
#### Bare Metal Solution Procurements Admin 

(`roles/baremetalsolution.procurementsadmin`) Administrator of Bare Metal Solution Procurements  |  `baremetalsolution.pods.list` `baremetalsolution.procurements.*`

  * `baremetalsolution.procurements.create`
  * `baremetalsolution.procurements.get`
  * `baremetalsolution.procurements.list`

`baremetalsolution.skus.list`  
  
#### Bare Metal Solution Procurements Editor 

(`roles/baremetalsolution.procurementseditor`) Editor of Bare Metal Solution Procurements  |  `baremetalsolution.pods.list` `baremetalsolution.procurements.*`

  * `baremetalsolution.procurements.create`
  * `baremetalsolution.procurements.get`
  * `baremetalsolution.procurements.list`

`baremetalsolution.skus.list`  
  
#### Bare Metal Solution Procurements Viewer 

(`roles/baremetalsolution.procurementsviewer`) Viewer of Bare Metal Solution Procurements  |  `baremetalsolution.procurements.get` `baremetalsolution.procurements.list` `baremetalsolution.skus.list`  
  
#### Bare Metal Solution Storage Admin 

(`roles/baremetalsolution.storageadmin`) Administrator of Bare Metal Solution storage resources  |  `baremetalsolution.luns.create` `baremetalsolution.luns.delete` `baremetalsolution.luns.evict` `baremetalsolution.luns.get` `baremetalsolution.luns.list` `baremetalsolution.luns.update` `baremetalsolution.nfsshares.*`

  * `baremetalsolution.nfsshares.create`
  * `baremetalsolution.nfsshares.delete`
  * `baremetalsolution.nfsshares.get`
  * `baremetalsolution.nfsshares.list`
  * `baremetalsolution.nfsshares.rename`
  * `baremetalsolution.nfsshares.update`

`baremetalsolution.operations.get` `baremetalsolution.pods.list` `baremetalsolution.snapshotschedulepolicies.*`

  * `baremetalsolution.snapshotschedulepolicies.create`
  * `baremetalsolution.snapshotschedulepolicies.delete`
  * `baremetalsolution.snapshotschedulepolicies.get`
  * `baremetalsolution.snapshotschedulepolicies.list`
  * `baremetalsolution.snapshotschedulepolicies.update`

`baremetalsolution.storageaggregatepools.list` `baremetalsolution.volumequotas.list` `baremetalsolution.volumes.create` `baremetalsolution.volumes.delete` `baremetalsolution.volumes.evict` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumes.rename` `baremetalsolution.volumes.resize` `baremetalsolution.volumes.update` `baremetalsolution.volumesnapshots.*`

  * `baremetalsolution.volumesnapshots.create`
  * `baremetalsolution.volumesnapshots.delete`
  * `baremetalsolution.volumesnapshots.get`
  * `baremetalsolution.volumesnapshots.list`
  * `baremetalsolution.volumesnapshots.restore`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Volume Admin 

(`roles/baremetalsolution.volumesadmin`) Administrator of Bare Metal Solution volume resources  |  `baremetalsolution.operations.get` `baremetalsolution.pods.list` `baremetalsolution.volumes.create` `baremetalsolution.volumes.delete` `baremetalsolution.volumes.evict` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumes.rename` `baremetalsolution.volumes.resize` `baremetalsolution.volumes.update`  
  
#### Volumes Editor 

(`roles/baremetalsolution.volumeseditor`) Editor of Bare Metal Solution volumes resources  |  `baremetalsolution.operations.get` `baremetalsolution.pods.list` `baremetalsolution.volumequotas.list` `baremetalsolution.volumes.create` `baremetalsolution.volumes.delete` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list` `baremetalsolution.volumes.rename` `baremetalsolution.volumes.resize` `baremetalsolution.volumes.update`  
  
#### Snapshots Admin 

(`roles/baremetalsolution.volumesnapshotsadmin`) Administrator of Bare Metal Solution snapshots resources  |  `baremetalsolution.operations.get` `baremetalsolution.volumesnapshots.*`

  * `baremetalsolution.volumesnapshots.create`
  * `baremetalsolution.volumesnapshots.delete`
  * `baremetalsolution.volumesnapshots.get`
  * `baremetalsolution.volumesnapshots.list`
  * `baremetalsolution.volumesnapshots.restore`

  
  
#### Snapshots Editor 

(`roles/baremetalsolution.volumesnapshotseditor`) Editor of Bare Metal Solution snapshots resources  |  `baremetalsolution.operations.get` `baremetalsolution.volumesnapshots.create` `baremetalsolution.volumesnapshots.delete` `baremetalsolution.volumesnapshots.get` `baremetalsolution.volumesnapshots.list`  
  
#### Snapshots Viewer 

(`roles/baremetalsolution.volumesnapshotsviewer`) Viewer of Bare Metal Solution snapshots resources  |  `baremetalsolution.operations.get` `baremetalsolution.volumesnapshots.get` `baremetalsolution.volumesnapshots.list`  
  
#### Volumes Viewer 

(`roles/baremetalsolution.volumessviewer`) Viewer of Bare Metal Solution volumes resources  |  `baremetalsolution.operations.get` `baremetalsolution.volumes.get` `baremetalsolution.volumes.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Bare Metal Solution Service Agent 

(`roles/baremetalsolution.serviceAgent`) Gives permission to manage network resources such as interconnect pairing keys, required for Bare Metal Solution.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.interconnectAttachments.get` `compute.interconnectAttachments.list` `compute.interconnects.get` `compute.interconnects.list` `compute.networks.get` `compute.networks.list` `compute.projects.get` `resourcemanager.projects.get`  
  
We recommend applying the roles as follows:

  * **Filling out an intake form**

    * Bare Metal Solution roles: Admin, Editor, or Instances Admin AND Compute Network Viewer
    * Basic roles: Owner or Editor
  * **Restarting a Bare Metal Solution server**

    * Bare Metal Solution roles: Admin or Editor
    * Basic roles: Owner or Editor
  * **Listing servers or requesting status**

    * Bare Metal Solution roles: Viewer or Instances Viewer
    * Basic role: Viewer
  * **Managing storage components**

    * Bare Metal Solution roles: Admin, Editor, or Storage Admin
    * Basic roles: Owner or Editor
  * **Managing networking components**

    * Bare Metal Solution roles: Admin, Editor, or Networks Admin
    * Basic roles: Owner or Editor



For a full list of Bare Metal Solution roles, see [Predefined roles](https://cloud.google.com/iam/docs/roles-permissions) and enter `baremetalsolution.` in the search box.

For a full list of Bare Metal Solution permissions, see [Search for a permission](https://cloud.google.com/iam/docs/roles-permissions) and enter `baremetalsolution.` in the search box.

## Grant an IAM role

Add an IAM policy to grant a Bare Metal Solution role to a principal. The role contains permissions which enable the principal to perform certain actions. To grant a role:

###  Console 

  1. Make sure that you have a role that contains the proper IAM permissions to grant roles to others, such as **Owner** , **Project IAM Admin** , or **Security Admin**. For more information about this requirement, see [Required Roles](https://cloud.google.com/iam/docs/granting-changing-revoking-access#required-permissions).

  2. In the Google Cloud console, go to the IAM permissions page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  3. Click **Grant access**.

  4. Enter the following information:

     * For **Add principals** , enter your users. You can add individual users, Google groups, service accounts, or Google Workspace domains.

     * For **Assign roles** , choose a role from the **Select a role** menu to grant this role to the principals.

     * Click **add Add another role** if you need to assign multiple roles to your principals.

     * Click **Save**.

Your principals and their assigned roles appear in the [IAM permissions](https://console.cloud.google.com/iam-admin/iam) status page.




###  gcloud 

  1. Make sure that you have a role that contains the proper IAM permissions to grant roles to others, such as **Owner** , **Project IAM Admin** , or **Security Admin**. For more information about this requirement, see [Required Roles](https://cloud.google.com/iam/docs/granting-changing-revoking-access#required-permissions).

  2. Open a Cloud Shell window in your Google Cloud project.

  3. Add your Google Cloud project ID, email address for your principal's Google Cloud account, and the desired Bare Metal Solution role path into the following command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
          --member=user:username@example.com \
          --role=roles/baremetalsolution.admin
          

  4. Copy the command and paste it into your Cloud Shell window.

  5. Press the **Enter** or **Return** key.

  6. In some cases, an **Authorize Cloud Shell** window opens, requesting you to allow an API call. If you see this, click **Authorize**.

  7. When you've entered the commands successfully, the output looks like this:
         
         Updated IAM policy for project [PROJECT_ID].
           bindings:
           - members:
            - user:username@example.com
            role: roles/baremetalsolution.admin
           - members:
            - serviceAccount:service-PROJECT_NUMBER@compute-system.
            role: roles/compute.serviceAgent
           - members:
            - serviceAccount:PROJECT_NUMBER-compute@
            - serviceAccount:PROJECT_NUMBER@cloudservices.
            role: roles/editor
           - members:
            - user:username@example.com
            role: roles/owner
           etag: ETAG_NUMBER
           version: 1
          




To learn more about IAM, see [Identity and Access Management](https://docs.cloud.google.com/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
