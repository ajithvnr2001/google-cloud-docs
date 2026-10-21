---
url: https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job/
title: Create patch jobs \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:19.203414+00:00
---

# Create patch jobs  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Create patch jobs Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch) to apply operating system patches across a group of virtual machine (VM) instances.

To apply patches to your VMs, complete the following steps:

  1. Set up your VM.
  2. Run a patch job.



## Before you begin

  * Review [OS Config quotas](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas).
  * To generate audit logs for VM Manager events, [enable data access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).
  * Review [limitations](https://docs.cloud.google.com/compute/vm-manager/docs/patch#limitations) for Patch.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Set up your VM

To use the Patch feature, complete the following steps:

  1. For all VMs, [set up VM Manager](https://docs.cloud.google.com/compute/docs/manage-os).
  2. For Windows VMs, Google recommends [disabling automatic updates](https://docs.microsoft.com/en-us/windows/deployment/update/waas-wu-settings#configure-automatic-updates) on the VMs. This reduces conflicts between the Windows automatic updates and the Patch service.



## Permissions

Owners of a Google Cloud project have full access to run and manage patch jobs. For all other users, you need to grant permissions. You can grant one of the following granular roles:

**Caution:** The Patch Job Executor role includes the `osconfig.patchJobs.exec` permission that provides access to manage software packages on VMs. By granting this role, you risk granting users unintended access to run code on VMs. To mitigate this risk, we recommend that you follow [ the principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) and provide only the required access to each user and monitor the usage of this IAM permission by users. 

  * `roles/osconfig.patchJobExecutor`: Contains permissions to run, cancel, get, and list patch jobs. It also contains permissions to view instance details for a patch job.
  * `roles/osconfig.patchJobViewer`: Contains permissions for read-only access to get and list patch jobs. It also contains permissions to view instance details for a patch job.



For example, to grant a user access to run patch jobs, use the following command:
    
    
    gcloud projects add-iam-policy-binding project-id \
        --member user:user-id@gmail.com \
        --role roles/osconfig.patchJobExecutor
    

Replace the following:

  * `project-id`: The project ID.
  * `user-id`: The user's Google Workspace username.



## Run patch jobs

You can run a patch job by using either the [Google Cloud console](https://console.cloud.google.com/), [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/osconfig/rest).

When you run a patch job, the patching of the VMs starts simultaneously on all instances specified by the instance filter.

**Note:** You can patch a maximum of 500 VMs in a single patch job. All VMs targeted by a single patch job are patched simultaneously.

After you have started a patch job, you can monitor your patches using the [Patch dashboard](https://docs.cloud.google.com/compute/vm-manager/docs/patch#dashboard). It takes approximately 30 minutes after a patch job starts before the data is populated on the dashboard.

**Note:** Targeting all VMs in a single patch deployment might cause a reduction in system availability. We recommend that you keep this in consideration when planning your maintenance window or that you use instance filters and patch VMs in small batches.

###  Console 

  1. In the Google Cloud console, go to the **Compute Engine** > **VM Manager** > **Patch** page. 

[Go to the Patch page](https://console.cloud.google.com/compute/patch)

  2. Click **Create patch job**.
  3. In the **Target VMs** section, specify the criteria for selecting VMs for patching.

     1. Select the zone that contains the VMs that you want to patch. You can also choose to select all zones.

After you select the zones, you can then further filter the VMs within that zone.

**Note:** In the Google Cloud console, you can only filter by name prefix or label. If you need to apply other types of instance filters use either the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/osconfig/rest).

For example, to patch specific VMs in the zones you selected, enter the name and label filters similar to the following:

        * Name prefix: `test-`
        * Labels: `env=dev` and `app=web`
     2. In the **Other options** section, specify the following:

        * **Allow patching MIG instances** : If you select this option, the patch job runs on VMs that are part of a managed instance group (MIG).
        * **Skip unpatchable VMs** : If you select this option, the patch job skips any VM that cannot be patched (for example, VMs running Container-Optimized OS). For more information, see Settings for VMs in MIGs and unpatchable VMs.
  4. In the **Patch configuration** section, configure the patch.

     1. Specify a **Name** for your patch.
     2. Select the required updates for your operating system. For more information, see patch configuration.
  5. In the **Scheduling** section, complete the following:

     * Select a schedule. To run the patch job immediately, select **Start now**.
     * Optional: Set a duration or maintenance window.
  6. In the **Rollout options** section, configure the patch rollout options:

     * Select whether to patch one zone at a time or to patch zones concurrently.
     * Set a disruption budget. A disruption budget is the number or percentage of VMs in a zone that you want to be disrupted at one time by the patching process.
  7. Optional: In the **Advanced options** section, you can complete the following tasks:

     * Select a reboot option.
     * Upload pre-patch and post-patch scripts. For more information about pre-patch and post-patch scripts, see Specifying pre-patch and post-patch scripts.
  8. Click **Deploy**.




###  gcloud 

Use the [`os-config patch-jobs execute`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute) command to run a patch job. Replace `instance-filter` with the instance filter that you want. For more information about instance filters, see instance filters.
    
    
    gcloud compute os-config patch-jobs execute instance-filter

For more information about what updates get applied, see [what is included in an OS patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch#whats-in-a-patch). To customize your updates, use the [optional flags](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#OPTIONAL-FLAGS).

**Examples**

**Example 1** To run a patch job with the following configurations:

  * Instance name: `instance-1`
  * Zone: `us-east1-b`
  * Description: `patch for instance-1`

You would run the following command:



    
    
    gcloud compute os-config patch-jobs execute \
        --instance-filter-names="zones/us-east1-b/instances/instance-1" \
        --description "patch for instance-1"

**Example 2** Suppose you want to run a patch job asynchronously with the following configurations:

  * Patch must be run on all instances in the project.
  * Patch job must timeout and stop after 1 hour and 30 minutes.
  * Machines must reboot based on the system settings after installing the updates.
  * On VMs running Apt, patching is done using `apt dist-upgrade`.
  * On VMs running Windows, only apply patches for the `KB4339284` update.
  * On VMs running Yum, patching is done using the `yum update-minimal --security` utility.



You would run the following command:
    
    
    gcloud compute os-config patch-jobs execute \
        --instance-filter-all \
        --duration="1h30m" --reboot-config="DEFAULT" \
        --apt-dist --windows-exclusive-patches=4339284 \
        --yum-minimal --yum-security \
        --async

###  REST 

In the API, create a `POST` request to run a new patch job. You must explicitly define all of the required configuration fields as described in the [`patchJobs.execute`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/execute) API documentation.

For more information about what updates get applied, see [what is included in an OS patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch#whats-in-a-patch). To customize your updates, use the [`PatchConfig` parameters](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig).

For example, a patch job with only the required fields looks like the following.
    
    
    POST https://osconfig.googleapis.com/v1/projects/project-id/patchJobs:execute
    
    {
      "instanceFilter": instance-filter
    }
    

Replace the following:

  * `project-id`: Your project ID.
  * `instance-filter`: The filter parameters that you want. For more information about instance filters, see instance filters.



**Examples**

**Example 1** Suppose you want to run a patch job on an instance named `instance1` located in `us-east1-b`. In this example, we add a description and specify that the job runs for 1 hour 30 minutes. Replace `project-id` with your project ID.
    
    
    POST https://osconfig.googleapis.com/v1/projects/project-id/patchJobs:execute
    
    {
      "description":"patch instance1 in us-east1-b",
      "duration":"5400s",
      "instanceFilter":{
        "instances":[
          "zones/us-east1-b/instances/instance1"
        ]
      }
    }
    

**Example 2** The following patch job selects VMs that have the following configurations:

  * Have labels `env=dev` and `app=web`.
  * Are in either `asia-east1-b` or `asia-east1-c`.
  * Have the prefix `test-`.



In the following command, replace `project-id` with your project ID.
    
    
    POST https://osconfig.googleapis.com/v1/projects/project-id/patchJobs:execute
    
    {
      "instanceFilter":{
        "groupLabels":[
          {
            "labels":{
              "env":"dev",
              "app":"web"
            }
          }
        ],
        "instanceNamePrefixes":[
          "test-"
        ],
        "zones":[
          "asia-east1-b",
          "asia-east1-c"
        ]
      }
    }
    

**Example 3**

Suppose you want to run a patch job with the following configurations:

  * Patch must be run on all instances in the project.
  * Patch job must timeout and stop after 1 hour and 30 minutes. The API requires that time is expressed in seconds, so set this as 5400s.
  * Machines must reboot based on the system settings after installing the updates.
  * On VMs running Apt, patching is done using `apt dist-upgrade`.
  * On VMs running Windows, only apply patches for the `KB4339284` update.
  * On VMs running Yum, patching is done using the `yum update-minimal --security` utility.



You would create the following request:

In the following command, replace `project-id` with your project ID.
    
    
    POST https://osconfig.googleapis.com/v1/projects/project-id/patchJobs:execute
    
    {
     "duration":"5400s",
     "instanceFilter":{
       "all":true
     },
     "patchConfig":{
       "rebootConfig":"DEFAULT",
       "apt":{
         "type":"DIST"
       },
       "yum":{
         "security":true,
         "minimal":true
       },
       "windowsUpdate":{
         "exclusivePatches":"4339284"
       }
     }
    }
    

### Instance filters

You can specify the instances to be included in a patch job by using filters. The following filters are supported for patch jobs:

  * Filter by name: Limit patch job to instances with specific names. Instance names must be specified by using the full URI. Supported URI formats include the following:

    * zones/zone/instances/instance-name

    * projects/project-id/zones/zone/instances/instance-name

    * https://www.googleapis.com/compute/v1/projects/project-id/zones/zone/instances/instance-name

  * Filter by name prefix: Limit patch job to instances with a specific prefix in their name.

  * Filter by zone: Limit patch job to instances in a specific zone.

  * Filter by label: Limit patch job to instances with specific labels.




You can also run patch jobs on all instances in a Google Cloud project by setting the `all` field in `instanceFilter` to `true`. For more information, see example instance filters.

**Note:** Instance filters are resolved when the patch job starts. This means that a scheduled patch deployment that targets all VMs in a Google Cloud project patches all VMs that are available in the Google Cloud project at the time the patch starts running.

#### Example instance filters

**Scenario** | **gcloud filter** | **API filter**  
---|---|---  
All instances in a Google Cloud project | 
    
    
    --instance-filter-all
    

| 
    
    
    {
      "instanceFilter":{
        "all":"true"
      }
    }
      
  
An instance with the name `instance1` that is located in the zone `us-east1-b`. | 
    
    
    --instance-filter-names="zones/us-east1-b/instances/instance1"
    

| 
    
    
    {
      "instanceFilter":{
        "instances":[
          "zones/us-east1-b/instances/instance1"
        ]
      }
    }
      
  
Instances with the prefix `app-` | 
    
    
    --instance-filter-name-prefixes="app-"

| 
    
    
    {
      "instanceFilter":{
        "instanceNamePrefixes":[
          "app-"
        ]
      }
    }
      
  
Instances in zones `us-east1-b` or `us-east1-c` | 
    
    
    --instance-filter-zones="us-east1-b","us-east1-c"

| 
    
    
    {
      "instanceFilter":{
        "zones":[
          "us-east1-b",
          "us-east1-c"
        ]
      }
    }
      
  
Instances with the combination label of `env=dev` and `app=web` as well as instances with `env=dev` and `app=worker`.  | 
    
    
    --instance-filter-group-labels="env=dev,app=web"
    --instance-filter-group-labels="env=dev,app=worker"
    

| 
    
    
    {
      "instanceFilter":{
        "groupLabels":[
          {
            "labels":{
              "env":"dev",
              "app":"web"
            }
          },
          {
            "labels":{
              "env":"dev",
              "app":"worker"
            }
          }
        ]
      }
    }
      
  
**Combining instance filters**

Instance filters can also be combined. For example, to run a patch job for instances that have the prefix `test-`, that are located in the zone `us-east1-c`, and that have the labels `env=dev` and `app=web`, run the following command:
    
    
    gcloud compute os-config patch-jobs execute \
        --instance-filter-name-prefixes="test-" \
        --instance-filter-zones="us-east1-c" \
        --instance-filter-group-labels="env=prod,app=web"
    

### Patch configuration

When running a patch job, you can specify parameters to control the patches that are applied on the VM. The patch configuration parameters are platform dependent and are often passed through to the underlying system update tools. The actual patches are sourced from the package repositories (Linux) or the Windows Update server (Windows) that is configured on the VM.

You can specify the following patch configurations for your VMs:

  * For Windows, you specify the classification of patches to apply (eg. `Security` and `Critical`) or target specific KBs to exclude. For more information about patch classification, see the [Microsoft support documentation](https://support.microsoft.com/help/824684).
  * For RHEL, Rocky Linux, and CentOS, the underlying system is `yum`.

    * For patches that target RHEL and Rocky Linux VMs, you can specify `security` and `minimal` packages.
    * For CentOS VMs, there is no `security` metadata in the CentOS `yum` repository. Therefore, you need not specify the `security` option when updating security packages. If you don't specify any package, the patch job updates all packages, including those with security updates.
    * You can also exclude specific packages. For more information, see the [`yum` man pages](http://man7.org/linux/man-pages/man8/yum.8.html).
  * For Debian & Ubuntu, the underlying system is `apt`. For patches that target these VMs, you can specify `dist-upgrade` or a standard upgrade. You can also exclude specific packages. For more information, see either the [Debian man pages](https://manpages.debian.org/buster/apt/apt.8.en.html) or [Ubuntu man pages](http://manpages.ubuntu.com/manpages/focal/man8/apt.8.html).

  * For SuSE, the underlying system is `zypper`, specifically using [zypper patches](https://en.opensuse.org/SDB:Zypper_usage#Update_management). For patches that target these VMs, you can specify options such as:

    * `with update`: update all packages not covered by patches
    * `with optional`: optional patches are treated as needed
    * The categories or severities of patches to apply

You can also exclude specific patches.




Optionally, for all the supported operating systems, you can select to install approved patches only by specifying these updates. This lets you enter a list of approved packages or patches. When you select these approved patches, only the approved packages or patches are installed. All other patch configuration parameters are skipped during the update.

#### Examples

###  Console 

  1. Follow the steps outlined in the console tab for creating either a [patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#create-patch-console) or a [patch deployment](https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs#schedule-patch-console).
  2. In the **Patch configuration** section, select the parameters for your patch job.
  3. Make any additional configurations that are needed for your patch job or deployment.
  4. Click **Deploy**.



###  gcloud 

For example, to run a patch job on all instances in the zone `northamerica-northeast1-a` with specific patch configurations for different operating systems, run the [`gcloud compute os-config patch-jobs execute`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute) command:
    
    
    gcloud compute os-config patch-jobs execute \
        --instance-filter-zones="northamerica-northeast1-a" \
        --apt-dist \
        --yum-security \
        --yum-minimal \
        --zypper-categories=security \
        --windows-classifications=critical,security \
        --reboot-config=default \
        --skip-unpatchable-vms
    

To learn more about the supported options, run the following command:
    
    
    gcloud compute os-config patch-jobs execute --help

###  REST 

For example, to run a patch job on all instances in the zone `northamerica-northeast1-a` with specific patch configurations for different operating systems, run the following command:
    
    
    POST https://osconfig.googleapis.com/v1/projects/project-id/patchJobs:execute
    {
        "instanceFilter":{
            "zones":[
                "northamerica-northeast1-a"
            ]
        },
        "patchConfig":{
            "apt": {
                "type": "dist-upgrade"
            },
            "yum": {
                "security": true,
                "minimal": true
            },
            "zypper": {
                "categories": ["security"]
            },
            "windowsUpdate": {
                "classifications": ["CRITICAL", "SECURITY"]
            },
            "rebootConfig": "DEFAULT"
        },
        "skipUnpatchableVms": true
    }
    

To learn more about the supported parameters, review the [`PatchConfig API`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig) documentation.

### Settings for VMs in MIGs and unpatchable VMs

To specify how VM Manager handles VMs that are part of a managed instance group (MIG), or VMs that run operating systems that don't support patching, use the following boolean options in the [patch configuration](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig):

  * **Allow patching of MIG instances** : By default, VM Manager does not patch any VMs that are part of a MIG. If you want to patch VMs in MIGs, set `migInstancesAllowed` to `true`. For more information about limitations for patching VMs in a MIG, see [Limitations](https://docs.cloud.google.com/compute/vm-manager/docs/patch#limitations).
  * **Skip unpatchable VMs** : If you set `skipUnpatchableVms` to `true`, VM Manager skips patching a VM if any of the following conditions are met:

    * The VM's operating system does not support patching. For example, Container-Optimized OS. See [Supported operating systems](https://docs.cloud.google.com/compute/vm-manager/docs/patch#supported-os).
    * The VM is part of a MIG, and `migInstancesAllowed` is set to `false`.

For patch jobs that were created by using Google Cloud console, the **Skip unpatchable VMs** option is selected by default.

If `skipUnpatchableVms` is set to `true`, the patch job reports the patch status of unpatchable VMs as `SKIPPED`. Additionally, if no other errors occur, the patch job reports a state of `COMPLETED_WITH_INACTIVE_VMS` instead of `COMPLETED_WITH_ERRORS` for inactive VMs.




### Maintenance window

A maintenance window is the total length of time that you allow a patch job to run. Patch jobs will timeout if they don't complete within the specified maintenance window.

For example, if you set a maintenance window of `60 minutes`, then no new patch jobs will be initiated 60 minutes after the start time. Some processes such as downloading a file or rebooting might occur outside of this maintenance window, however no new patch jobs will be initiated.

### Reboot options

When running a patch job, you can specify the reboot options for the patch. The following options are available:

  * Default: The agent decides if a reboot is necessary by checking well known signals on each OS. Multiple reboots may occur during the patching and may occur before any patches are installed.
  * Always: The machine reboots after the update has completed.
  * Never: The machine does not reboot after the update has completed. In some cases, this might mean that not all patches are fully applied.



### Pre-patch and post-patch scripts

When running a patch job, you can specify scripts to be run as part of the patching process. These scripts are useful for performing tasks such as shutting down an application and performing health checks.

  * Pre-patch scripts run before patching starts. If a system reboot is required before patching starts, the pre-patch script runs before the reboot.
  * Post-patch scripts run after patching completes. If a system reboot is required as part of the patching, the post-patch script runs after the reboot.



A patch job accepts one pre-patch and one post-patch script for Linux, and one pre-patch and one post-patch script for Windows. Linux and Windows scripts must be provided using the appropriate flags, parameters, or sections when specified from the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), [REST](https://docs.cloud.google.com/compute/docs/osconfig/rest), or the [Google Cloud console](https://console.cloud.google.com/) respectively. Linux scripts run on Linux VMs only and Windows scripts run on Windows VMs only.

**Note:** Linux scripts must begin with a [shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29) line to specify which shell should execute the script. For example, add `#!/bin/bash` to specify the Bash shell.

These script files can either be stored on the VM or in a [versioned](https://docs.cloud.google.com/storage/docs/object-versioning) Cloud Storage bucket.

#### Store patch scripts in Cloud Storage buckets

If you want to use a Cloud Storage bucket to store your scripts, [create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-console) and [upload your scripts](https://docs.cloud.google.com/storage/docs/uploading-objects) to the bucket. When using a Cloud Storage bucket, consider the following:

  * If your Cloud Storage object is not publicly readable, ensure that [the service account attached to the instance](https://docs.cloud.google.com/compute/docs/instances/change-service-account#serviceaccountname) has the necessary IAM permissions to read the Cloud Storage objects. To ensure that you have the correct permissions, check the [permission settings](https://docs.cloud.google.com/storage/docs/access-control/iam) on the Cloud Storage object.
  * When you select a script from Cloud Storage using the Google Cloud console, the latest version of the specified Cloud Storage object is used by default.
  * If your organization enforces the [Resource Location Restriction constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations), then you must store your scripts in Cloud Storage buckets in regions and zones that your org policy permits.




###  Console 

  1. Follow the steps outlined in the console tab for creating either a [patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#create-patch-console) or a [patch deployment](https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs#schedule-patch-console).
  2. In the **Advanced options** section, for both the pre-patch and post-patch sections, click **Browse**. A Cloud Storage object page displays.
  3. From the Cloud Storage object page, select the Cloud Storage bucket that contains the script, then select the Cloud Storage object or file.
  4. Make any additional configurations that are needed for your patch job or deployment.
  5. Click **Deploy**.



###  gcloud 

For example, to run a patch job on all instances in the zone `northamerica-northeast1-a` with both pre and post patch script for Linux and Windows instances, run the following command:
    
    
    gcloud compute os-config patch-jobs execute \
        --instance-filter-zones="northamerica-northeast1-a" \
        --async \
        --pre-patch-linux-executable="/tmp/pre_patch_script.sh" \
        --post-patch-linux-executable="gs://my-patch-scripts/linux/post_patch_script#1523477886880" \
        --pre-patch-windows-executable="C:\\Users\\user\\pre-patch-script.cmd" \
        --post-patch-windows-executable="gs://my-patch-scripts/windows/post_patch_script.ps1#135920493447"
    

To learn more about acceptable file formats, run the following command:
    
    
    gcloud compute os-config patch-jobs execute --help

###  REST 

For example, to run a patch job on all instances in the zone `northamerica-northeast1-a` with both pre and post patch script for Linux and Windows instances, run the following command:
    
    
    POST https://osconfig.googleapis.com/v1/projects/project-id/patchJobs:execute
    
    {
      "instanceFilter":{
        "zones":[
          "northamerica-northeast1-a"
        ]
      },
      "patchConfig":{
        "preStep":{
          "linuxExecStepConfig":{
            "localPath":"/tmp/pre_patch_script.sh"
          },
          "windowsExecStepConfig":{
            "interpreter":"SHELL",
            "localPath":"C:\\Users\\user\\pre-patch-script.cmd"
          }
        },
        "postStep":{
          "linuxExecStepConfig":{
            "gcsObject":{
              "bucket":"my-patch-scripts",
              "generationNumber":"1523477886880",
              "object":"linux/post_patch_script"
            }
          },
          "windowsExecStepConfig":{
            "gcsObject":{
              "bucket":"my-patch-scripts",
              "generationNumber":"135920493447",
              "object":"windows/post_patch_script.ps1"
            },
            "interpreter":"POWERSHELL"
          }
        }
      }
    }
    

To learn more about acceptable file formats, review the [`ExecStepConfig`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig#execstepconfig) section of the `PatchConfig` API documentation.

### Patch rollout options

You can choose to either patch VMs one zone at a time (zone by zone), or to patch all zones at once (concurrent zones).

Along with making a selection for the zone roll out, you can also specify a zone disruption budget for your VMs.

#### Zone disruption budget

A disruption budget is the maximum number (or percentage) of VMs per zone to disrupt at any given moment.

#### What is considered a disrupted VM?

During patching, a VM is considered disrupted from the time the OS Config agent is notified to begin until patching has completed. This disruption time includes the time to complete reboot and any post-patch steps.

A VM is also counted as a part of the disruption budget if it meets any of the following conditions:

  * Patching operation fails when applying the patches
  * Patching operation fails when running pre or post patch steps
  * Patching operation fails to respond with a success notification before timing out

**Note:** VMs that are not running or those that don't have an active agent don't count toward this disruption budget.

#### How disruption budgets work

For zone-by-zone rollouts, if the disruption budget in a zone is exceeded, the patch job stops. This happens because continuing to the next zone requires completion of the patch process in the previous zone.

For example, if the disruption budget has a value of 10, and 8 VMs fail to patch in the current zone, the patch job continues to patch 2 VMs at a time until the zone is completed. When that zone is completed successfully, patching begins with 10 VMs at a time in the next zone. If 10 VMs in the next zone fail to patch, the patch job stops.

#### Examples

###  Console 

  1. Follow the steps outlined in the console tab for creating either a [patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#create-patch-console) or a [patch deployment](https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs#schedule-patch-console).
  2. In the **Rollout options** section, configure the rollout options: 
     * Select whether to patch one zone at a time or to patch all zones concurrently.
     * Set the disruption budget. A disruption budget is the number or percentage of VMs in a zone that you want to be disrupted at one time by the patching process.
  3. Make any additional configurations that are needed for your patch job or deployment.
  4. Click **Deploy**.



###  gcloud 

**Example 1**

This example shows the [`os-config patch-jobs execute` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute) for running a patch job with the following specifications:

  * Patching all VMs in your project
  * Patching VMs zone by zone
  * Ensuring that no more than 10 VMs in the same zone are disrupted at a given time


    
    
    gcloud compute os-config patch-jobs execute \
       --instance-filter-all \
       --rollout-mode=zone-by-zone \
       --rollout-disruption-budget=10
    

**Example 2**

This example shows the [`os-config patch-jobs execute` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute) for running a patch job with the following specifications:

  * Patching all VMs in your project
  * Patching zones concurrently
  * Ensuring that no more than 50 percent of the VMs in the same zone are disrupted at a given time


    
    
    gcloud compute os-config patch-jobs execute \
       --instance-filter-all \
       --rollout-mode=concurrent-zones \
       --rollout-disruption-budget-percent=50
    

###  REST 

This example shows the [`patchJobs.execute` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/execute) for running a patch job with the following specifications:

  * Patching all VMs in the zones `us-central1-a`, `us-central1-c`, and `us-central1-f`
  * Patching zones concurrently
  * Ensuring that no more than 25 percent of the instances in the same zone are disrupted at a given time


    
    
    POST https://osconfig.googleapis.com/v1/projects/project-id/patchJobs:execute
    
    {
      "instanceFilter":{
        "zones":[
          "us-central1-a",
          "us-central1-c",
          "us-central1-f"
        ]
      },
      "rollout": {
        "disruptionBudget": {
          "percent": 25
        },
        "mode": "CONCURRENT_ZONES"
      }
    }
    

To learn more about patch rollout, review the [`PatchRollout`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchRollout) API documentation.

## Enable patching Microsoft software on Windows VMs

When you run a patch job on Windows VMs, by default, Patch applies only the patches for the Windows operating system.

You can apply updates for Microsoft software such as Microsoft SQL Server, SharePoint Server, or .NET framework running on your Windows VMs when you run a patch job. By default, patching these applications is disabled to avoid disruption of service and to separate planned updates for these software. To enable patching Microsoft software automatically, you can either use the Windows UI or the PowerShell.

###  Windows UI 

  1. In the **Windows Start** menu, select **Settings** > **Update & Security** > **Windows Update**.
  2. In the **Advanced options** section, toggle on **Receive updates for other Microsoft products when you update Windows**.



###  PowerShell 
    
    
     $service_manager = New-Object -ComObject 'Microsoft.Update.ServiceManager'
     $service_manager.AddService2("7971f918-a847-4430-9279-4a52d1efe18d",7,"")
    

## Debug a patch job

If your patch fails, you can use the following steps to help find and resolve the issues.

  1. Review the [instance details](https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs#list-instance-details) for the affected patch job. This helps you to identify which instances failed or what state they are stuck in. The instance details list also contains a brief error message for each instance.

If a patch fails with a status of `NO_AGENT_DETECTED` or `TIMED_OUT`, this usually means that the service sent a request to the agent to begin patching but never heard back from the agent. Review the following possible causes and fixes:

     * The instance is not running. To fix this, [start the VM instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance).
     * Verify the setup by using the [verification checklist](https://docs.cloud.google.com/compute/docs/troubleshooting/vm-manager/verify-setup).
     * The network settings on the VPC network or the instance didn't allow the OS Config agent to communicate with the OS Config API. To fix this, check the network settings.
  2. If the [instance details](https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs#list-instance-details) don't provide enough information, review the Cloud Logging logs or [serial port console](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output#viewing_serial_port_output). The OS Config agent writes its log entries to both locations. In Cloud Logging, you can filter using the patch job ID to see all log entries related to that patch job. You can also enable debug logging by setting the `osconfig-log-level=debug` [metadata value](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#custom) at the VM or Google Cloud project level.




## What's next?

  * Learn more about [Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch).
  * [Manage your patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs).
  * [Schedule patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
