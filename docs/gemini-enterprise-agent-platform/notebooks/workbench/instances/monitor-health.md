---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/monitor-health/
title: Monitor health status \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:45:12.667568+00:00
---

# Monitor health status  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/monitor-health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Notebooks ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/overview)



Send feedback 

#  Monitor health status Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Agent Platform Workbench instances provide several methods for monitoring the health of your notebooks. This page describes how to use each method.

## Methods for monitoring health status

You can monitor the health of your Agent Platform Workbench instances in a few different ways. This page describes how to use the following methods:

  * Use guest attributes to report system health

  * Report custom metrics to Cloud Monitoring

  * Report system and application metrics to Monitoring by installing Monitoring on a Agent Platform Workbench instance

  * Use the diagnostic tool




### Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Notebooks API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=notebooks.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Notebooks API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=notebooks.googleapis.com&redirect=https%3A//console.cloud.google.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Use guest attributes to report system health

You can use guest attributes to report the system health of the following core services:

  * Docker service
  * Docker reverse proxy agent
  * Jupyter service
  * Jupyter API



_Guest attributes_ are a specific type of custom metadata that applications can write to while running on your Agent Platform Workbench instance. To learn more about guest attributes, see [About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview#guest_attributes).

### How instances use guest attributes to report system health

The `notebooks-collection-agent` service runs a Python process in the background that verifies the status of the Agent Platform Workbench instance's core services and updates the guest attributes as either `1` if no problems are detected or `-1` if a failure is detected.

To use the `notebooks-collection-agent` service to report on your Agent Platform Workbench instance's health, you must enable the following guest attributes _while creating_ a Agent Platform Workbench instance:

  * `enable-guest-attributes=TRUE`: This enables guest attributes on your Agent Platform Workbench instance. All new instances enable this attribute by default.
  * `report-event-health=TRUE`: This records system health check results to your guest attributes.



The `notebooks-collection-agent` service doesn't need any special permissions to write to the instance's guest attributes.

**Note:** The `notebooks-collection-agent` service uses approximately 50 MB of memory to run in the background.

### Create a Agent Platform Workbench instance with system health guest attributes enabled

To use system health guest attributes to report on your Agent Platform Workbench instance's health, you must select the **Enable system health report** checkbox when you create a Agent Platform Workbench instance.

You can enable the system health report by using the Google Cloud console or the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances?project=)

  2. Click add_box **Create new**.

  3. In the **New instance** dialog, click **Advanced options**.

  4. In the **Create instance** dialog, in the **Details** section, provide the following information for your new instance:

     * **Name** : Provide a name for your new instance.

     * **Region** and **Zone** : Select a region and zone for the new instance. For best network performance, select the region that is geographically closest to you. See the available [Agent Platform Workbench locations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations#workbench-locations).

  5. In the **System health** section, in **Reporting** , select **Report system health**.

  6. Complete the rest of the instance creation dialog, and then click **Create**.




###  gcloud 

  1. From [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) or any environment where the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) is installed, enter the following [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) command:
         
         gcloud workbench instances create INSTANCE_NAME \
             --vm-image-project=cloud-notebooks-managed \
             --vm-image-family=IMAGE_FAMILY \
             --machine-type=MACHINE_TYPE \
             --location=ZONE \
             --metadata=enable-guest-attributes=TRUE,report-event-health=TRUE
         

Replace the following:

     * `INSTANCE_NAME`: the name of your new instance
     * `IMAGE_FAMILY`: the image family name that you want to use to create your instance
     * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) of your instance's VM; for example, `n1-standard-4`
     * `ZONE`: the zone where you want your new instance to be located, for example, `us-west1-a`
  2. Access your instance from the [Google Cloud console](https://console.cloud.google.com/agent-platform/workbench/instances?project=).




### Monitor system health through guest attributes

For Agent Platform Workbench instances that have the related guest attributes enabled, you can retrieve the values of your system health guest attributes by using either the Google Cloud console, the Google Cloud CLI with Compute Engine commands, or the Google Cloud CLI with Gemini Enterprise Agent Platform Workbench commands.

###  Console 

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances?project=)

  2. Click the instance name that you want to view the system health status of.

  3. On the **Instance details** page, click the **Health** tab. Review the status of your instance and its core services.




###  gcloud with Compute Engine
    
    
    gcloud compute instances get-guest-attributes INSTANCE_NAME \
        --zone ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of your instance
  * `ZONE`: the zone where your instance is located



If your core services are healthy, the results look like the following. A value of `1` means no failure was detected.
    
    
     NAMESPACE   KEY                         VALUE
     notebooks   docker_proxy_agent_status   1
     notebooks   docker_status               1
     notebooks   jupyterlab_api_status       1
     notebooks   jupyterlab_status           1
     notebooks   system-health               1
     notebooks   updated                     2023-06-20 17:00:00.12345
    

If any of the four core services fail, system-health reports a `-1` value to indicate system failure. In most cases, a system failure means that JupyterLab is not accessible.

An example of a failure result might look like the following.
    
    
     NAMESPACE   KEY                         VALUE
     notebooks   docker_proxy_agent_status   -1
     notebooks   docker_status               -1
     notebooks   jupyterlab_api_status       1
     notebooks   jupyterlab_status           1
     notebooks   system-health               -1
     notebooks   updated                     2023-06-20 17:00:00.12345
    

## Report custom metrics to Monitoring

Agent Platform Workbench instances let you collect system status and JupyterLab metrics and report them to Cloud Monitoring. These custom metrics are different from the standard metrics that are reported when you install Monitoring on your Agent Platform Workbench instance.

The custom metrics reported to Monitoring include the following:

  * The system health of these Agent Platform Workbench core services:

    * Docker service
    * Docker reverse proxy agent
    * Jupyter service
    * Jupyter API
  * The following JupyterLab metrics:

    * Number of kernels
    * Number of terminals
    * Number of connections
    * Number of sessions
    * Maximum memory
    * High memory
    * Current memory



### How instances report custom metrics to Monitoring

To report custom metrics to Monitoring, you must enable the `report-notebook-metrics` metadata setting _while creating_ a Agent Platform Workbench instance.

You must also make sure that the Agent Platform Workbench instance's service account has Monitoring Metric Writer (`roles/monitoring.metricWriter`) permissions. For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Create a Gemini Enterprise Agent Platform Workbench instance that reports custom metrics to Monitoring

To report custom metrics to Monitoring, you must select the **Report custom metrics to Cloud Monitoring** checkbox when you create a Agent Platform Workbench instance.

You can enable reporting custom metrics to Cloud Monitoring by using the Google Cloud console or the gcloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances?project=)

  2. Click add_box **Create new**.

  3. In the **New instance** dialog, click **Advanced options**.

  4. In the **Create instance** dialog, in the **Details** section, provide the following information for your new instance:

     * **Name** : Provide a name for your new instance.
     * **Region** and **Zone** : Select a region and zone for the new instance. For best network performance, select the region that is geographically closest to you. See the available [Agent Platform Workbench locations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations#workbench-locations).
  5. In the **System health** section, in **Reporting** , select **Report custom metrics to Cloud Monitoring**.

  6. Complete the rest of the instance creation dialog, and then click **Create**.




###  gcloud 

  1. From [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) or any environment where the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) is installed, enter the following [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) command:
         
         gcloud workbench instances create INSTANCE_NAME \
             --vm-image-project=cloud-notebooks-managed \
             --vm-image-family=IMAGE_FAMILY \
             --machine-type=MACHINE_TYPE \
             --location=ZONE \
             --metadata=report-notebook-metrics=TRUE
         

Replace the following:

     * `INSTANCE_NAME`: the name of your new instance
     * `IMAGE_FAMILY`: the image family name that you want to use to create your instance
     * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) of your instance's VM, for example, `n1-standard-4`
     * `ZONE`: the zone where you want your new instance to be located, for example, `us-west1-a`
  2. Access your instance from the [Google Cloud console](https://console.cloud.google.com/agent-platform/workbench/instances?project=).




### Grant Monitoring Metric Writer permissions to the service account

After you've created your new Agent Platform Workbench instance, grant Monitoring Metric Writer permissions (`roles/monitoring.metricWriter`) to the service account for the Agent Platform Workbench instance. For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Monitor custom metrics through Monitoring

For Agent Platform Workbench instances that have reporting custom metrics enabled, you can monitor your custom metrics by using the Google Cloud console.

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances?project=)

  2. Click the instance name that you want to view the custom metrics of.

  3. On the **Instance details** page, click the **Monitoring** tab. Review the custom metrics for your instance.




## Install Monitoring on an instance

This option automatically installs Monitoring. The installation requires 256 MB of disk space. An internet connection is required for the metrics to be reported to Monitoring.

### How instances report system and application metrics

To report system and application metrics by installing Cloud Monitoring on your Agent Platform Workbench instance, you must select the **Install Cloud Monitoring agent** checkbox when you create a Agent Platform Workbench instance. These metrics are different from the custom metrics that are reported when you enable the `report-notebook-metrics` metadata setting.

### Create a Agent Platform Workbench instance that reports system and application metrics to Monitoring

To install Monitoring on your Agent Platform Workbench instance, you can use the Google Cloud console or the gcloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances?project=)

  2. Click add_box **Create new**.

  3. In the **New instance** dialog, click **Advanced options**.

  4. In the **Create instance** dialog, in the **Details** section, provide the following information for your new instance:

     * **Name** : Provide a name for your new instance.
     * **Region** and **Zone** : Select a region and zone for the new instance. For best network performance, select the region that is geographically closest to you. See the available [Agent Platform Workbench locations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations#workbench-locations).
  5. In the **System health** section, in **Reporting** , select **Install Cloud Monitoring**.

  6. Complete the rest of the instance creation dialog, and then click **Create**.




###  gcloud 

  1. From [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) or any environment where the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) is installed, enter the following [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) command:
         
         gcloud workbench instances create INSTANCE_NAME \
             --vm-image-project=cloud-notebooks-managed \
             --vm-image-family=IMAGE_FAMILY \
             --machine-type=MACHINE_TYPE \
             --location=ZONE \
             --metadata=install-monitoring-agent=TRUE
         

Replace the following:

     * `INSTANCE_NAME`: the name of your new instance
     * `IMAGE_FAMILY`: the image family name that you want to use to create your instance
     * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) of your instance's VM; for example, `n1-standard-4`
     * `ZONE`: the zone where you want your new instance to be located, for example, `us-west1-a`
  2. Access your instance from the [Google Cloud console](https://console.cloud.google.com/agent-platform/workbench/instances?project=).




### Monitor system and application metrics through Monitoring

For Agent Platform Workbench instances that have Monitoring installed, you can monitor your system and application metrics by using the Google Cloud console:

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances?project=)

  2. Click the instance name that you want to view the system and application metrics of.

  3. On the **Instance details** page, click the **Monitoring** tab. Review the system and application metrics for your instance. To learn how to interpret these metrics, see [Review resource metrics](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms#review_resource_metrics).




## Use the diagnostic tool to monitor system health

Agent Platform Workbench instances include a built-in diagnostic tool that can help you monitor the system health of your instances.

### Tasks performed by the diagnostic tool

The diagnostic tool performs the following tasks:

  * Verifies the status of the following Agent Platform Workbench core services:

    * Docker service
    * Docker reverse proxy agent
    * Jupyter service
    * Jupyter API
  * Checks whether the disk space for boot and data disks is used beyond an 85% threshold.

  * Installs [`lsof`](https://github.com/lsof-org/lsof) (internet connection required).

  * Collects the following instance logs:

    * Network information (`ifconfig`, `netstat`)
    * Logs in the `/var/log/` folder
    * Docker status information
    * `lsof` (open files) data
    * Docker service status
    * Proxy reverse agent status
    * Jupyter service status
    * Jupyter API status
    * Proxy agent configuration file
    * Python processes
  * Runs the following commands and collects the results:

    * pip freeze
    * conda list
    * gcloud compute instances describe `INSTANCE_NAME`
    * gcloud config list



### Run the diagnostic tool

If your instance uses a custom container, see [Run the diagnostic tool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-custom-container#run-diagnostic-tool) in the Agent Platform Workbench custom container documentation.

To run the diagnostic tool in an instance that doesn't use a custom container, complete the following steps:

  1. [Use ssh to connect to your Agent Platform Workbench instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/ssh-access).

  2. In the SSH terminal, run the following commands:
         
         sudo -i
         cd /opt/deeplearning/bin/
         ./diagnostic_tool.sh

The diagnostic tool collects the logs, compresses them in a `.tar.gz` file, and places the file in the `/tmp/` folder.

  3. Extract the file and then evaluate the contents. The contents include:

     * **`log` folder**: Logs from the `var/log/` folder
     * **`report.log`** : Output for all commands collected
     * **`proxy-agent-config.json`** : Proxy configuration information
     * **Docker log** : A `-json.log` file that includes Docker container logs



You can use the following options with the diagnostic tool.

Option | Description  
---|---  
-r |  A repair option that tries to restore failed Agent Platform Workbench core services status   
-s | Runs without a confirmation  
-b |  Uploads the `.tar.gz` file to a Cloud Storage bucket.   
-v |  A debug option for troubleshooting the tool in case of failures   
-c |  Captures 30 seconds of packet traffic into your Agent Platform Workbench instance, filtering SSH   
-d | A destination folder in which to save the logs   
-h | Help  
  
## What's next

  * [Learn more about VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).

  * [Learn more about Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
