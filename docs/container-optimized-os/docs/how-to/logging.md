---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/logging/
title: Using Cloud Logging with Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:31:24.016347+00:00
---

# Using Cloud Logging with Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Using Cloud Logging with Container-Optimized OS Stay organized with collections  Save and categorize content based on your preferences. 

Container-Optimized OS includes a logging agent which exports some system and container logs to Cloud Logging. Up until Container-Optimized OS 101, x86-based Container-Optimized OS images used a containerized logging agent based on fluentd. Container-Optimized OS 105 started shipping an alternative logging agent implementation, fluent-bit. As of Container-Optimized OS 109, the fluent-bit logging agent is the default. The legacy logging agent, fluentd, will be removed in Container-Optimized OS 113.

All versions of Arm-based Container-Optimized OS images ship the fluent-bit logging agent.

**Note:** Logging is automatically available when you choose Container-Optimized OS as the node image for running your Google Kubernetes Engine clusters. These instructions are for when you are using Container-Optimized OS outside of GKE, such as in Compute Engine.

## Enable the logging agent

The logging agent is disabled by default. You can enable this feature when creating a new instance or by updating an existing instance.

### Access Requirements

Cloud Logging provides IAM [roles](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) that you can use to grant appropriate access. In order to view your logs in a project, you must have the `roles/logging.viewer` role and applications must have permission to write logs. You can grant this permission by assigning the IAM role `roles/logging.logWriter` to the service account for an application.

For more information about permissions and roles, see [Predefined roles](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles).

### Create an instance with a logging agent enabled

###  Console 

To run a Compute Engine instance on Container-Optimized OS with the fluent-bit logging agent enabled, perform the following:

  1. Open the Compute Engine instance creation page on Google Cloud console.

[Create a new Compute Engine instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify a **Name** for your instance.

  3. In the **Boot disk** section, select a Container-Optimized OS image.

  4. Click on **Management, security, disks, networking, sole tenancy** to expand additional options.

  5. Under the **Management** tab, scroll to the **Metadata** section. Add a new metadata entry, with **Key** as `google-logging-enabled` and **Value** as `true`.

  6. Optionally, specify any other options for your use case. See [Creating and configuring instances](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance) for more details.

  7. Click **Create** to create and boot the instance.




###  gcloud 

To run a Compute Engine instance on Container-Optimized OS with the logging agent enabled, use the `gcloud compute instances create` command, and include `google-logging-enabled=true` in the metadata. For example:
    
    
    gcloud compute instances create instance-name \
        --image image-name \
        --image-project cos-cloud \
        --zone compute-zone \
        --metadata google-logging-enabled=true
    

Replace the following:

  * instance-name: the name of your VM instance.
  * image-name: the name of the Container-Optimized OS image for the instance. For example, `--image=cos-113-18244-85-29`.
  * compute-zone: the [compute zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your instance.



For more information on the `gcloud` command, see the [gcloud compute instances create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) reference documentation. For more details on creating Container-Optimized OS instances, see [Creating and configuring instances](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance).

### Selecting the logging agent

x86-based Container-Optimized OS 105 and 109 images ship two implementations of the logging agent: fluentd (legacy) and fluent-bit. Container-Optimized OS 105 uses fluentd by default and Container-Optimized OS 109 uses fluent-bit by default. You can use the `google-logging-use-fluentbit` metadata entry to change the default behavior.

To use fluent-bit logging agent on Container-Optimized OS 105 set `google-logging-use-fluentbit` value to `true`.

To use fluentd logging agent on Container-Optimized OS 109 set `google-logging-use-fluentbit` value to `false`.

### Enable the logging agent in project metadata

Starting in [milestone 97](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m97), logging can be enabled in project metadata:
    
    
      gcloud compute project-info add-metadata \
        --metadata google-logging-enabled=true
    

**Note:** Metadata flags defined at instance level takes precedence over metadata flags defined at project level.

## Access logs

###  Console 

  1. Go to the VM instances page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click on the name of the Container-Optimized OS instance you want to access logs from.

  3. Under the **Logs** section, click Cloud Logging.

  4. This opens the Logs Explorer for the given instance. For more information, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).


**Note:** In the query builder, you can filter by log name. Click on **Log name** , and select the given log name. For example, **cos_audit** for Audit logs or **cos_containers** for docker container logs.

###  gcloud 

To access logs, use the `gcloud logging read` command. For example:
    
    
    gcloud logging read \
    "resource.type=gce_instance AND resource.labels.instance_id=instance-id" \
        --limit 10 \
        --format json \
        --freshness 30d
    

Replace the following:

  * instance-id: the id of your VM instance.



This command attempts to read logs from the VM instance with instance-id, limiting to 10 logs, in JSON format, from the last 30 days.

For more information on the `gcloud` command, see the [gcloud logging read](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) reference documentation.

## How does it work?

The logging agent is configured by default to send logs from certain system critical services and user application containers to the Cloud Logging backend. For example, logs from docker containers, selected systemd services, audit logs, journal log errors, etc. See Container-Optimized OS specific configuration source ([x86 images](https://cos.googlesource.com/cos/overlays/board-overlays/+/refs/heads/main-R105/project-lakitu/app-admin/stackdriver/files/logging_configs/fluentd-lakitu.conf) and [Arm images](https://cos.googlesource.com/cos/overlays/board-overlays/+/refs/heads/main-R105/project-lakitu/app-admin/fluent-bit/files/fluent-bit.conf)) for complete default logging configuration.

For x86 images of Container-Optimized OS 105 and older, the logging agent is Google Cloud Observability's containerized legacy Logging agent. The docker command that starts the logging agent is defined in the Container-Optimized OS [source for stackdriver-logging systemd service](https://cos.googlesource.com/cos/overlays/board-overlays/+/refs/heads/main-R105/project-lakitu/app-admin/stackdriver/files/stackdriver-logging.service). The version of the containerized agent being run is defined in the Container-Optimized OS [source app-admin/stackdriver directory](https://cos.googlesource.com/cos/overlays/board-overlays/+/refs/heads/main-R105/project-lakitu/app-admin/stackdriver/files/env_vars).

For Arm images of all versions and x86 images for Container-Optimized OS 109 and later, the logging agent is a built-in OS package called [fluent-bit](https://cos.googlesource.com/cos/overlays/board-overlays/+/refs/heads/master/project-lakitu/app-admin/fluent-bit). The agent is built into the OS and updated along with the OS images.

## Known Limitations

### Compatibility with `gcplogs` driver

Starting with [milestone 89](https://docs.cloud.google.com/container-optimized-os/docs/release-notes#release_schedule), if the logging agent included with Container-Optimized OS is enabled and Docker `gcplogs` logging driver is enabled for one or more containers, excessive warning logs may be output by the included logging agent. This may create log noise and/or increase Cloud Logging related charges.

A workaround is to not use `gcplogs` as a Docker logging driver, and to instead use the default driver as configured by Container-Optimized OS. Note that the logging agent included with Container-Optimized OS will export container logs to Cloud Logging, so using both solutions simultaneously is not necessary.

### Logging agent configuration compatibility

The logging agent is a fluentd-based container on x86-based Container-Optimized OS images and a fluent-bit binary on Arm-based Container-Optimized OS images. The configurations of the two agents are not compatible. This is not a problem if you only rely on the default logging configuration built into the OS images. However, if you have a custom logging configuration, you might experience breakage when migrating workloads to images that are based on a different architecture or to a newer version of Container-Optimized OS.

## References

  * Google Cloud Observability's legacy Logging agent [documentation](https://docs.cloud.google.com/logging/docs/agent/logging). The containerized logging agent included with Container-Optimized OS is a subset of the legacy Logging agent, so this documentation may provide context on the agent more generally, outside of the scope of Container-Optimized OS.
  * Google Cloud Observability [documentation](https://cloud.google.com/products/operations). Homepage for Google Cloud Observability documentation; may be useful for context.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
