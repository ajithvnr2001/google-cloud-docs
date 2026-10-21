---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/monitoring/
title: Monitoring system health with Node Problem Detector \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:16:40.786426+00:00
---

# Monitoring system health with Node Problem Detector  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Monitoring system health with Node Problem Detector Stay organized with collections  Save and categorize content based on your preferences. 

Starting with Milestone 77, Container-Optimized OS includes the [Node Problem Detector](https://github.com/kubernetes/node-problem-detector) agent. You can use this feature to monitor the system health of COS instances. Node Problem Detector monitors the instance health and reports health-related metrics to Cloud Monitoring, including capacity and error metrics that you can then visualize with [Google Cloud Observability dashboards](https://docs.cloud.google.com/monitoring/charts). Collected metrics from the default configuration are free. Google will use aggregated metrics to understand node problems and improve the reliability of Container-Optimized OS.

The agent is pre-configured with the set of metrics to export. Customizing reported metrics for the built-in agent is not supported at this time. Node Problem Detector is open-source software. You can review its [source code](https://github.com/kubernetes/node-problem-detector) and [configurations](https://cos.googlesource.com/cos/overlays/board-overlays/+/refs/heads/master/project-lakitu/app-admin/node-problem-detector/) in their respective source repositories.

**Note:** The Node Problem Detector monitors the VM and _not_ the docker containers hosted on the COS VM. You will see metrics for the entire VM and nothing specific to the containers.

## Enabling health monitoring

**Note:** Google Kubernetes Engine Container-Optimized OS nodes and Google Distributed Cloud cluster nodes from version 1.4.0+ have Node Problem Detector enabled by default.

The Node Problem Detector agent is disabled by default at boot time. You can enable this feature by using:

  * `cloud-init`
  * startup script
  * metadata
  * user-defined guest policies



### Using a startup script

You can enable Node Problem Detector by using a [startup script](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance#running_startup_scripts).

### Using cloud-init

The [`cloud-init` example](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance#using_cloud-init) explains the basics of configuring a Container-Optimized OS instance. You can use `cloud-init` to enable health monitoring with the following `cloud-config` example:
    
    
    #cloud-config
    
    runcmd:
    - systemctl start node-problem-detector
    

### Using metadata

In Container-Optimized OS Milestone 88 and later, the Node Problem Detector can also be enabled by setting the value of `google-monitoring-enabled` to `true` in the custom metadata section.

To enable monitoring when creating an instance:
    
    
    gcloud compute instances create VM_NAME \
        --image=IMAGE \
        --image-project=cos-cloud \
        --metadata=google-monitoring-enabled=true
    

Replace the following:

  * `VM_NAME`: name of the new VM
  * `IMAGE`: a specific version of a public Container-Optimized OS image. For example, `--image=cos-113-18244-85-29`.



To enable monitoring in an existing instance:
    
    
    gcloud compute instances add-metadata VM_NAME \
        --metadata=google-monitoring-enabled=true
    

Replace `VM_NAME` with the name of the VM.

Starting in [milestone 97](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m97), monitoring can be enabled in project metadata:
    
    
    gcloud compute project-info add-metadata \
        --metadata google-monitoring-enabled=true
    

**Note:** Metadata flags defined at the instance level take precedence over metadata flags defined at the project level.

After execution, the node-problem-detector service will be enabled.

### Using user-defined guest policies

Container-Optimized OS includes [OS Config agent](https://docs.cloud.google.com/container-optimized-os/docs/how-to/osconfig), that uses OS system utilities to maintain the state for the VM that is specified in the guest policy. For details about guest policies, see [Enable OS Config agent](https://docs.cloud.google.com/compute/docs/manage-os#overview) and [Create a guest policy](https://docs.cloud.google.com/compute/docs/os-config-management/create-guest-policy). The following guest policy enables the Node problem detector agent on all the instances.
    
    
    recipes:
    - name: recipe-enable-npd
      desiredState: INSTALLED
      installSteps:
      - scriptRun:
          interpreter: SHELL
          script: |-
            #!/bin/bash
            systemctl start node-problem-detector
    

## Viewing the collected metrics

Node Problem Detector reports a list of metrics against a [Compute Engine instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance) monitored resource. The metrics are documented on [Monitoring metrics list](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute), prefixed with `compute.googleapis.com/guest/`. You can view the collected metrics using [Monitoring Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer):

**Note:** To view the metrics, the minium version of the node-problem-detector is [v0.7.0](https://github.com/kubernetes/node-problem-detector/releases).

  1. In the Google Cloud console, go to **Monitoring** or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the Monitoring navigation pane, click **Metrics explorer**.

  3. For the resource type, select **Compute Engine VM instance**.

  4. Select a metric, for example "Problem Count".

  5. You should see charts and statistics on the right side. To view the result for a specific Container-Optimized OS instance, set the filter to `"instance_id=[INSTANCE_ID]"`, replacing [INSTANCE_ID] with the ID for the desired instance.




## Disabling health monitoring

To disable the service that has already been enabled through your [`cloud-config`](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance#using_cloud-init) or through your [startup script](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance#running_startup_scripts), remove the `systemctl start node-problem-detector` step, and then reboot the Container-Optimized OS instance. If enabled by metadata, make sure the `google-monitoring-enabled` key is set to `false`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
