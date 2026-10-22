---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/manage-metadata/
title: Manage features through metadata \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:08.727258+00:00
---

# Manage features through metadata  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/manage-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Notebooks ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/overview)



Send feedback 

#  Manage features through metadata Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage some Gemini Enterprise Agent Platform Workbench instance features by modifying the instance's metadata key-value pairs.

## Metadata keys

For information about features and their respective metadata keys, see the following table.

Feature | Description | Metadata key | Accepted values and defaults  
---|---|---|---  
Enables Cloud Storage FUSE on a container image |  Mounts `/dev/fuse` onto the container and enables `gcsfuse` for use on the container.  | `container-allow-fuse` | 

  * `true`: Enables Cloud Storage FUSE.
  * `false` (default): Doesn't enable Cloud Storage FUSE.

  
nbconvert |  Lets you export and download notebooks as a different file type. | `notebook-disable-nbconvert` | 

  * `true`: Turns off nbconvert.
  * `false` (default): Enables nbconvert.

  
Delete to trash |  Uses the operating system's trash behavior when deleting from JupyterLab.  | `notebook-enable-delete-to-trash` | 

  * `true`: Enables deleting to the trash.
  * `false` (default): Uses the default JupyterLab behavior.

  
Managed Service for Apache Spark |  Enables access to Managed Service for Apache Spark kernels. For more information, see [Create a Managed Service for Apache Spark-enabled instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-dataproc-enabled).  | `disable-mixer` | 

  * `true`: Turns off access to Managed Service for Apache Spark kernels.
  * `false` (default): Enables access to Managed Service for Apache Spark kernels.

  
BigQuery |  Enables the BigQuery JupyterLab plugin, which provides a dataset explorer, a SQL query editor, and query history in JupyterLab.  | `disable-bigquery` | 

  * `true`: Turns off the BigQuery JupyterLab plugin.
  * `false` (default): Enables the BigQuery JupyterLab plugin.

  
Idle shutdown |  Enables idle shutdown. For more information, see [Idle shutdown](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown).  | `idle-timeout-seconds` | An integer representing the idle time in seconds. The default value is `10800` seconds (180 minutes).   
Guest attributes |  Enables guest attributes. Required for running idle shutdown. For more information, see [Requirements for running idle shutdown](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown#requirements).  | `enable-guest-attributes` | 
* `true` (default): Enables guest attributes.
* `false`: Turns off guest attributes.  
Scheduled OS patches |  Schedules automatic OS updates of the instance. This enables Debian's [unattended upgrade service](https://wiki.debian.org/UnattendedUpgrades) and only applies to VM-based images.  | `install-unattended-upgrades` | 

  * `true`: Turns on automatic OS updates.
  * `false` (default): Turns off automatic OS updates.

  
Custom Jupyter user |  Specifies the name of the default Jupyter user. This setting determines the name of the folder for your notebooks. For example, instead of the default `/home/jupyter/` directory, you can change the directory to `/home/CUSTOM_NAME`. This metadata key doesn't affect access to the instance.  | `jupyter-user` | A string. The default value is `jupyter`.  
File downloading |  Lets you download files from JupyterLab. | `notebook-disable-downloads` | 

  * `true`: Turns off file downloading.
  * `false` (default): Enables file downloading.

  
Root access |  Enables root access. | `notebook-disable-root` | 

  * `true`: Turns off root access.
  * `false` (default): Enables root access.

  
Terminal access |  Enables terminal access. | `notebook-disable-terminal` | 

  * `true`: Turns off terminal access.
  * `false` (default): Enables terminal access.

  
Scheduled upgrades |  Schedules automatic upgrades of the instance. | `notebook-upgrade-schedule` |  The weekly or monthly schedule that you set, in [unix-cron format](https://man7.org/linux/man-pages/man5/crontab.5.html), for example, `00 19 * * MON` means weekly on Monday, at 1900 hours Greenwich Mean Time (GMT). This feature is off by default. To disable this feature or keep it turned off, omit the `notebook-upgrade-schedule` metadata key from your configuration or set its value to an empty string (`""`).   
Post-startup script |  Runs a custom script after other startup scripts have completed. For details on the execution order, see Startup script execution order. | `post-startup-script` |  The URI of a post-startup script in Cloud Storage, for example: `gs://bucket/hello.sh`. This feature is off by default.   
Post-startup script behavior |  Defines when and how the post-startup script runs. | `post-startup-script-behavior` | 

  * `run_once` (default): Runs the post-startup script once after instance creation or upgrade. 
  * `run_every_start`: Runs the post-startup script after every start. 
  * `download_and_run_every_start`: Redownloads the post-startup script from its source then runs the script after every start. 

  
Report event health |  Checks health every 30 seconds for VM metrics. | `report-event-health` | 

  * `true` (default): Enables event health reporting.
  * `false`: Turns off event health reporting.

  
Enable JupyterLab 4 or switch to JupyterLab 3 |  Enable JupyterLab 3. JupyterLab 4 is enabled, by default. | `enable-jupyterlab4` | 

  * `true` (default): Enables JupyterLab 4.
  * `false`: Enables JupyterLab 3.

  
  
## Startup script execution order

If you use multiple startup scripts for your Agent Platform Workbench instance, they run in the following order:

  1. `startup-script`: Runs first during each boot after the initial boot.
  2. `startup-script-url`: Runs second during each boot after the initial boot.
  3. `workbench-startup-scripts`: Runs after the Compute Engine boot scripts (`startup-script` and `startup-script-url`) complete.
  4. `post-startup-script`: Runs after the `workbench-startup-scripts` complete.



Note that for the `post-startup-script` metadata key, you must provide the script as a Cloud Storage URI. You cannot provide the script content directly as the value.

## Metadata managed by Compute Engine

Some of the metadata keys are predefined by Compute Engine. For more information, see [Predefined metadata keys](https://docs.cloud.google.com/compute/docs/metadata/predefined-metadata-keys).

## Protected metadata keys

Some metadata keys are reserved for system use only. If you assign values to these metadata keys, the new values will be overwritten by the system values.

Reserved metadata keys include and are not limited to:

  * `agent-health-check-interval-seconds`
  * `agent-health-check-path`
  * `cos-update-strategy`
  * `custom-container-image`
  * `custom-container-payload`
  * `data-disk-uri`
  * `dataproc-allow-custom-clusters`
  * `dataproc-cluster-name`
  * `dataproc-configs`
  * `dataproc-default-subnet`
  * `dataproc-locations-list`
  * `dataproc-machine-types-list`
  * `dataproc-notebooks-url`
  * `dataproc-region`
  * `dataproc-service-account`
  * `disable-check-xsrf`
  * `euc-enabled`
  * `framework`
  * `generate-diagnostics-bucket`
  * `generate-diagnostics-file`
  * `generate-diagnostics-options`
  * `google-logging-enabled`
  * `image-url`
  * `install-monitoring-agent`
  * `install-nvidia-driver`
  * `installed-extensions`
  * `last_updated_diagnostic`
  * `last_updated_diagnostics`
  * `notebooks-api`
  * `notebooks-api-version`
  * `notebooks-examples-location`
  * `notebooks-location`
  * `proxy-backend-id`
  * `proxy-byoid-url`
  * `proxy-mode`
  * `proxy-status`
  * `proxy-url`
  * `proxy-user-mail`
  * `report-container-health`
  * `report-event-url`
  * `report-notebook-metrics`
  * `report-system-health`
  * `report-system-status`
  * `resource-url`
  * `restriction`
  * `serial-port-logging-enable`
  * `service-account-mode`
  * `shutdown-script`
  * `title`
  * `use-collaborative`
  * `user-data`
  * `version`



## Create an instance with specific metadata

You can create a Agent Platform Workbench instance with specific metadata by using the Google Cloud console, the Google Cloud CLI, Terraform, or the Notebooks API.

###  Console 

When you create a Agent Platform Workbench instance, you can add metadata in the **Environment** section of **Advanced options**.

![The Add metadata button in the Environment section](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/notebooks/workbench/images/metadata-during-create.png)

###  gcloud 

When you create a Agent Platform Workbench instance, you can add metadata by using the following command:
    
    
    gcloud workbench instances create INSTANCE_NAME --metadata=KEY=VALUE

###  Terraform 

To add metadata, create the resource with metadata key-value pairs.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    resource "google_workbench_instance" "default" {
      name     = "workbench-instance-example"
      location = "us-central1-a"
    
      gce_setup {
        machine_type = "n1-standard-1"
        vm_image {
          project = "cloud-notebooks-managed"
          family  = "workbench-instances"
        }
        metadata = {
          key = "value"
        }
      }
    }

###  Notebooks API 

Use the [`instances.create`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/create) method with metadata values to manage the corresponding features.

## Update an instance's metadata

You can update the metadata of a Agent Platform Workbench instance by using the Google Cloud console, the Google Cloud CLI, Terraform, or the Notebooks API.

###  Console 

To update the metadata of a Agent Platform Workbench instance, do the following:

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances)

  2. In the list of instances, click the name of the instance that you want to update.

  3. On the **Instance details** page, click **Software and security**.

  4. In the **Metadata** section, update the metadata key-value pairs that you want to change.

  5. Click **Submit**.




###  gcloud 

You can update the metadata on a Agent Platform Workbench instance by using the following command:
    
    
    gcloud workbench instances update INSTANCE_NAME --metadata=KEY=VALUE

###  Terraform 

You can change the metadata key-value pairs to manage the corresponding features on Agent Platform Workbench instances.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    resource "google_workbench_instance" "default" {
      name     = "workbench-instance-example"
      location = "us-central1-a"
    
      gce_setup {
        machine_type = "n1-standard-1"
        vm_image {
          project = "cloud-notebooks-managed"
          family  = "workbench-instances"
        }
        metadata = {
          key = "updated_value"
        }
      }
    }

###  Notebooks API 

Use the [`instances.patch`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/patch) method with metadata values and `gce_setup.metadata` in the `updateMask` to manage the corresponding features.

## Remove metadata from an instance

You can remove metadata from a Agent Platform Workbench instance by using the Google Cloud console, the Google Cloud CLI, Terraform, or the Notebooks API.

###  Console 

To remove metadata from a Agent Platform Workbench instance, do the following:

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances)

  2. In the list of instances, click the name of the instance that you want to modify.

  3. On the **Instance details** page, click **Software and security**.

  4. In the **Metadata** section, to the right of a key-value pair that you want to delete, click delete **Delete**.

  5. Click **Submit**.




###  gcloud 

You can remove metadata from a Agent Platform Workbench instance by using the following command:
    
    
    gcloud workbench instances update INSTANCE_NAME --metadata=KEY

###  Terraform 

You can remove metadata key-value pairs to manage the corresponding features of a Agent Platform Workbench instance.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    resource "google_workbench_instance" "default" {
      name     = "workbench-instance-example"
      location = "us-central1-a"
    
      gce_setup {
        machine_type = "n1-standard-1"
        vm_image {
          project = "cloud-notebooks-managed"
          family  = "workbench-instances"
        }
        metadata = {
        }
      }
    }

###  Notebooks API 

Use the [`instances.patch`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/patch) method with the metadata value set to an empty string and `gce_setup.metadata` in the `updateMask` to remove the corresponding feature.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
