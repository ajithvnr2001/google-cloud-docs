---
url: https://docs.cloud.google.com/ull-solution/participants/configure-time-sync/
title: Configure accurate time for U4 Compute Engine instances \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:33.489462+00:00
---

# Configure accurate time for U4 Compute Engine instances  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/configure-time-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure accurate time for U4 Compute Engine instances

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page describes how to configure accurate time for a U4 Compute Engine instance and how to configure monitoring so that you can view the accuracy of the time synchronization.

## How it works

Google Cloud Ultra Low Latency (ULL) Solution uses the _Firefly_ clock synchronization protocol to provide nanosecond-level synchronization. Firefly automatically does the following:

  * Performs _internal synchronization_ to synchronize the physical network interface (NIC) clocks of all U4 instance host servers to each other.
  * Performs _external synchronization_ to synchronize the physical NIC clocks of all U4 instance host servers to Coordinated Universal Time (UTC).



Because the physical NIC clocks of host servers that run U4 instances are automatically synchronized by Firefly, you can configure accurate time for your instance by synchronizing the system clock of the instance to the physical NIC clock of its host server.

For more information about Firefly, see the following Google Cloud Blog post: [Understanding the Firefly clock synchronization protocol](https://cloud.google.com/blog/products/networking/understanding-the-firefly-clock-synchronization-protocol).

## Before you begin

Before you configure accurate time for U4 Compute Engine instances, you must meet the following requirements.

### Create a U4 instance

If you haven't already, create a U4 Compute Engine instance. See the procedure that corresponds to your use case:

  * To create a U4P or U4C instance, see [Create ULL Compute Engine instances](https://docs.cloud.google.com/ull-solution/participants/create-ull-instances).
  * To create a U4S instance, see [Create non-ULL Compute Engine instances for auxiliary workloads](https://docs.cloud.google.com/ull-solution/participants/create-non-ull-instances).



### Ensure that no other clock synchronization services are running

The procedures on this page use [`chrony`](https://chrony-project.org/) as the recommended clock synchronization client. Before you begin, ensure that there are no other clock synchronization services running on your instance, such as `ntpd`, `systemd-timesyncd` or `phc2sys`. Unexpected interactions with these services can cause errors with your `chrony` configuration.

In `chrony` version 4.7 and later, you can check the `chronyd` warnings log for other clock synchronization services by running the following command:
    
    
    journalctl -u chronyd
    

If another clock synchronization service is running, the output includes a warning message such as the following: `System clock interference detected (another NTP client?)`.

### Get network interface names

Get the names of your instance's virtual network interfaces (vNICs) as assigned by the guest OS. While Google Cloud uses names such as `nic0` and `nic1`, the guest OS naming format is different, such as `enp22s0f0` and `ens8f0`.

To list vNIC names in order, run the following command:
    
    
    find /sys/class/net -type l -not -lname '*virtual*' -printf '%l %f\n' | sort | awk '{print $2}'
    

### Configure `chrony` to load only after network drivers are stable

In some cases, `systemd` might load `chrony` before the network interface drivers finish initializing, which can result in `chrony` failing to start because it can't initialize the [PTP hardware clock (PHC)](https://docs.kernel.org/driver-api/ptp.html#ptp-hardware-clock-infrastructure-for-linux) device.

To avoid the preceding issue, override `chrony`'s `systemd` unit file to wait for PHC devices to be ready by following these steps. If you are using DPDK on a U4C instance, select the **DPDK configuration** tab.

###  Standard configuration 

  1. Run the edit command:
         
         systemctl edit chronyd
         

  2. Add the override that corresponds to your instance type:

     * For U4P and U4C instances:
           
           [Unit]
           After=dev-ptp0.device dev-ptp1.device dev-ptp2.device
           Requires=dev-ptp0.device dev-ptp1.device dev-ptp2.device
           

     * For U4S instances:
           
           [Unit]
           After=dev-ptp0.device
           Requires=dev-ptp0.device
           

  3. Restart the service. While the `systemctl edit` command that you ran previously automatically reloaded the daemon, we recommend that you run the following command to ensure that `chrony` is running after your changes.
         
         systemctl restart chronyd
         




###  DPDK configuration 

  1. If you are using DPDK on a U4C instance, get the index number of the PHC device associated with `nic0`.

Because DPDK binds the ULL network interfaces (`nic1` and `nic2`) to the user space, `nic0` is the only interface that exposes a PTP device to the kernel.

Run the following command, then record the value of `PTP Hardware Clock:NUMBER` for use in a later step.
         
         ethtool -T NIC0
         

Replace `NIC0` with the name of the `nic0` interface, such as `enp22s0f0`.

  2. Run the edit command:
         
         systemctl edit chronyd
         

  3. Add the following override:
         
         [Unit]
         After=dev-ptpNUMBER.device
         Requires=dev-ptpNUMBER.device
         

Replace `NUMBER` with the index number of the PHC device that you obtained in step 1.

  4. Restart the service. While the `systemctl edit` command that you ran previously automatically reloaded the daemon, we recommend that you run the following command to ensure that `chrony` is running after your changes.
         
         systemctl restart chronyd
         




## Configure `chrony` to use the Firefly-synced physical NIC clock

This section describes how to configure `chrony` to synchronize the system clock of your instance to the physical NIC clock on your instance's host server that is already synchronized by Firefly.

Your U4 instance's virtual network interfaces (vNICs) as shown in the guest OS (such as `enp22s0f0`) map to physical NICs on the instance's host server. A given vNIC can access the physical NIC clock by using the corresponding [PTP hardware clock (PHC)](https://docs.kernel.org/driver-api/ptp.html#ptp-hardware-clock-infrastructure-for-linux) device:

  * PHC device names in Linux have the following format: `/dev/ptpNUMBER`, where `NUMBER` is determined by the Linux kernel according to the device initialization order. For example, see the following PHC device names: `/dev/ptp0`, `/dev/ptp1`, `/dev/ptp2`.

  * To specify a physical NIC clock as the source for synchronization, the `chrony` configuration must use or resolve to the corresponding PHC device.




Each of the following sections provide examples of how to configure `chrony` according to the preceding requirements. See the section that corresponds to your instance type and `chrony` version:

  * Configure `chrony` 4.7 and later on U4P and U4C instances
  * Configure `chrony` 4.6.1 and earlier on U4P and U4C instances
  * Configure `chrony` 4.7 and later on U4S instances



### Configure `chrony` 4.7 and later on U4P and U4C instances

`chrony` version 4.7 and later supports specifying a vNIC name as the clock source and automatically resolves it to the corresponding PTP hardware clock (PHC) device that represents the physical NIC clock.

###  Standard configuration 

To configure `chrony` version 4.7 and later on a U4P or U4C instance, do the following:

  1. Add the following to the `chrony` configuration file, `/etc/chrony.conf`. The file must contain only the following configuration. Ensure that you remove or overwrite any pre-existing contents of the file.

**Note:** This example corresponds to a typical configuration of a U4P or U4C instance where one vNIC is attached to a general-purpose VPC network and two vNICs are attached to a ULL VPC network. These instances are backed by three physical NICs, and each vNIC maps to a different physical NIC.
         
         # Record the rate at which the system clock gains/loses time.
         driftfile /var/lib/chrony/drift
         
         # Allow the system clock to be stepped in the first three updates
         # if its offset is larger than 1 micro-second.
         makestep 0.0000001 3
         
         # Specify directory for log files.
         logdir /var/log/chrony
         
         # Select which information is logged.
         log measurements statistics tracking refclocks
         
         # U4 Compute Engine instance clocks are 200ppb accurate
         maxclockerror 0.2
         
         # Configure all clocks for tracking, but select only one of them as source.
         refclock PHC NIC0:nocrossts poll -1 noselect
         refclock PHC NIC1:nocrossts poll -1
         refclock PHC NIC2:nocrossts poll -1 noselect
         
         # The following lines opportunistically enable Precision Time Measurement (PTM) based clock synchronization.
         # Note that PTM can potentially result in a (constant) clock skew of up to 700 nanoseconds
         # which is not accounted for in chrony's accuracy metrics.
         refclock PHC NIC0 poll -1 noselect
         refclock PHC NIC1 poll -1 noselect
         refclock PHC NIC2 poll -1 noselect

Replace `NIC0`, `NIC1`, `NIC2` with the corresponding names that you got previously. If needed, see Get network interface names.

  2. To apply the configuration, restart `chrony` by running the following command:
         
         systemctl restart chronyd
         




`chrony` logs clock synchronization statistics to `/var/log/chrony/tracking.log` using the PTP hardware clock of `NIC1` as the time source.

###  DPDK configuration 

To configure `chrony` version 4.7 and later on a U4C instance that uses DPDK, do the following:

  1. Add the following to the `chrony` configuration file, `/etc/chrony.conf`. The file must contain only the following configuration. Ensure that you remove or overwrite any pre-existing contents of the file.

**Note:** This example corresponds to a U4C instance that uses DPDK. Because DPDK binds the ULL network interfaces (`nic1` and `nic2`) to the user space, they are not available to the kernel. This configuration uses the general-purpose interface (`nic0`) as the sole time source.
         
         # Record the rate at which the system clock gains/loses time.
         driftfile /var/lib/chrony/drift
         
         # Allow the system clock to be stepped in the first three updates
         # if its offset is larger than 1 micro-second.
         makestep 0.0000001 3
         
         # Specify directory for log files.
         logdir /var/log/chrony
         
         # Select which information is logged.
         log measurements statistics tracking refclocks
         
         # U4 Compute Engine instance clocks are 200ppb accurate
         maxclockerror 0.2
         
         # Configure the nic0 interface clock for tracking and select it as the source.
         refclock PHC NIC0:nocrossts poll -1
         
         # The following lines opportunistically enable Precision Time Measurement (PTM) based clock synchronization.
         # Note that PTM can potentially result in a (constant) clock skew of up to 700 nanoseconds
         # which is not accounted for in chrony's accuracy metrics.
         refclock PHC NIC0 poll -1 noselect

Replace `NIC0` with the corresponding name that you got previously. If needed, see Get network interface names.

  2. To apply the configuration, restart `chrony` by running the following command:
         
         systemctl restart chronyd
         




`chrony` logs clock synchronization statistics to `/var/log/chrony/tracking.log` using the PTP hardware clock of `NIC0` as the time source.

### Configure `chrony` 4.6.1 and earlier on U4P and U4C instances

`chrony` versions 4.6.1 and earlier require that you specify the PTP hardware clock (PHC) device name manually in your configuration file.

###  Standard configuration 

To configure `chrony` versions 4.6.1 and earlier on a U4P or U4C instance, do the following:

  1. Get the index number of the PHC device associated with a vNIC. The following example uses the first vNIC.
         
         ethtool -T NIC0
         

Replace `NIC0` with the corresponding name that you got previously, such as `enp22s0f0`. If needed, see Get network interface names.

     1. Review the output for `PTP Hardware Clock:NUMBER`

This example output shows `PTP Hardware Clock: 1`, which corresponds to `/dev/ptp1`.
            
            Time stamping parameters for enp22s0f0:
            Capabilities:
                  hardware-receive
                  software-receive
                  software-system-clock
                  hardware-raw-clock
            **PTP Hardware Clock: 1**
            Hardware Transmit Timestamp Modes:
                  off
            Hardware Receive Filter Modes:
                  none
                  all
            

  2. Add the following to the `chrony` configuration file, `/etc/chrony.conf`. The file must contain only the following configuration. Ensure that you remove or overwrite any pre-existing contents of the file.

The `ethtool` output in the preceding step showed that `enp22s0f0` uses `/dev/ptp1`. The following example synchronizes the system clock to the corresponding physical NIC clock for `enp22s0f0` by specifying: `refclock PHC /dev/ptp1:nocrossts poll -1`.

**Note:** This example corresponds to a typical configuration of a U4P or U4C instance where one vNIC is attached to a general-purpose VPC network and two vNICs are attached to a ULL VPC network. These instances are backed by three physical NICs, and each vNIC maps to a different physical NIC.
         
         # Record the rate at which the system clock gains/loses time.
         driftfile /var/lib/chrony/drift
         
         # Allow the system clock to be stepped in the first three updates
         # if its offset is larger than 1 micro-second.
         makestep 0.0000001 3
         
         # Enable kernel synchronization of the real-time clock (RTC).
         rtcsync
         
         # Save NTS keys and cookies.
         ntsdumpdir /var/lib/chrony
         
         # Specify directory for log files.
         logdir /var/log/chrony
         
         # Select which information is logged.
         log measurements statistics tracking refclocks
         
         # U4 Compute Engine instance clocks are 200ppb accurate
         maxclockerror 0.2
         
         # Configure all clocks for tracking, but select only one of them as source.
         refclock PHC /dev/ptp0:nocrossts poll -1 noselect
         refclock PHC /dev/ptp1:nocrossts poll -1
         refclock PHC /dev/ptp2:nocrossts poll -1 noselect
         
         # The following lines opportunistically enable Precision Time Measurement (PTM) based clock synchronization.
         # Note that PTM can potentially result in a (constant) clock skew of up to 700 nanoseconds
         # which is not accounted for in chrony's accuracy metrics.
         refclock PHC /dev/ptp0 poll -1 noselect
         refclock PHC /dev/ptp1 poll -1 noselect
         refclock PHC /dev/ptp2 poll -1 noselect

  3. To apply the configuration, restart `chrony` by running the following command:
         
         systemctl restart chronyd
         




`chrony` logs clock synchronization statistics to `/var/log/chrony/tracking.log` using the selected PTP hardware clock as the time source.

###  DPDK configuration 

To configure `chrony` versions 4.6.1 and earlier on a U4C instance that uses DPDK, do the following:

  1. Get the index number of the PHC device associated with your `nic0` vNIC.
         
         ethtool -T NIC0
         

Replace `NIC0` with the corresponding name that you got previously, such as `enp22s0f0`. If needed, see Get network interface names.

     1. Review the output for `PTP Hardware Clock:NUMBER`

This example output shows `PTP Hardware Clock: 0`, which corresponds to `/dev/ptp0`.
            
            Time stamping parameters for enp22s0f0:
            Capabilities:
                  hardware-receive
                  software-receive
                  software-system-clock
                  hardware-raw-clock
            **PTP Hardware Clock: 0**
            Hardware Transmit Timestamp Modes:
                  off
            Hardware Receive Filter Modes:
                  none
                  all
            

  2. Add the following to the `chrony` configuration file, `/etc/chrony.conf`. The file must contain only the following configuration. Ensure that you remove or overwrite any pre-existing contents of the file.

The `ethtool` output in the preceding step showed that `enp22s0f0` uses `/dev/ptp0`. The following example synchronizes the system clock to the corresponding physical NIC clock for `enp22s0f0` by specifying: `refclock PHC /dev/ptp0:nocrossts poll -1`.

**Note:** This example corresponds to a U4C instance that uses DPDK. Because DPDK binds the ULL network interfaces (`nic1` and `nic2`) to the user space, they are not available to the kernel. This configuration uses the `nic0` interface (`/dev/ptp0`) as the sole time source. If your `ethtool -T` output shows a different PTP hardware clock number (for example, `/dev/ptp1`), replace `/dev/ptp0` with that device.
         
         # Record the rate at which the system clock gains/loses time.
         driftfile /var/lib/chrony/drift
         
         # Allow the system clock to be stepped in the first three updates
         # if its offset is larger than 1 micro-second.
         makestep 0.0000001 3
         
         # Enable kernel synchronization of the real-time clock (RTC).
         rtcsync
         
         # Save NTS keys and cookies.
         ntsdumpdir /var/lib/chrony
         
         # Specify directory for log files.
         logdir /var/log/chrony
         
         # Select which information is logged.
         log measurements statistics tracking refclocks
         
         # U4 Compute Engine instance clocks are 200ppb accurate
         maxclockerror 0.2
         
         # Configure the nic0 interface clock for tracking and select it as the source.
         # If nic0 uses a PHC index other than 0 (such as /dev/ptp1), replace /dev/ptp0.
         refclock PHC /dev/ptp0:nocrossts poll -1
         
         # The following lines opportunistically enable Precision Time Measurement (PTM) based clock synchronization.
         # Note that PTM can potentially result in a (constant) clock skew of up to 700 nanoseconds
         # which is not accounted for in chrony's accuracy metrics.
         refclock PHC /dev/ptp0 poll -1 noselect

  3. To apply the configuration, restart `chrony` by running the following command:
         
         systemctl restart chronyd
         




`chrony` logs clock synchronization statistics to `/var/log/chrony/tracking.log` using the selected PTP hardware clock as the time source.

### Configure `chrony` 4.7 and later on U4S instances

We recommend that you use `chrony` versions 4.7 and later for U4S instances. Using earlier versions might result in frequent errors because the Compute Engine clock synchronization device for virtual machine (VM) instances (`ptp_kvm`) can cause changes to the index numbers of PTP hardware clock (PHC) devices.

This example configuration for U4S instances is similar to the one used for U4P and U4C instances, but has the following differences:

  * This example includes a single vNIC. A U4S instance can have multiple vNICs, but all of the vNICs are backed by the same physical NIC and access the same physical NIC clock.
  * [Precision Time Measurement (PTM)](https://pcisig.com/PCIExpress/ECN/Base/PrecisionTimeMeasurement_1.0a) isn't available.



To configure `chrony` versions 4.7 and later on a U4S instance, do the following:

  1. Add the following to the `chrony` configuration file, `/etc/chrony.conf`. The file must contain only the following configuration. Ensure that you remove or overwrite any pre-existing contents of the file.
         
         # Record the rate at which the system clock gains/loses time.
         driftfile /var/lib/chrony/drift
         
         # Allow the system clock to be stepped in the first three updates
         # if its offset is larger than 1 micro-second.
         makestep 0.0000001 3
         
         # Specify directory for log files.
         logdir /var/log/chrony
         
         # Select which information is logged.
         log measurements statistics tracking refclocks
         
         # U4 Compute Engine instance clocks are 200ppb accurate
         maxclockerror 0.2
         
         # Configure all clocks for tracking, but select only one of them as source.
         refclock PHC NIC0:nocrossts poll -1

Replace `NIC0` with the corresponding name that you got previously, such as `enp22s0f0`. If needed, see Get network interface names.

  2. To apply the configuration, restart `chrony` by running the following command:
         
         systemctl restart chronyd
         

`chrony` logs clock synchronization statistics to `/var/log/chrony/tracking.log` using the PTP hardware clock of `NIC0` as the time source.




### Verify the `chrony` configuration

To verify that `chrony` is configured correctly, run the following command:
    
    
    chronyc sourcestats
    

A successful configuration results in output similar to the following:
    
    
    Name/IP Address             NP  NR  Span  Frequency  Freq Skew  Offset  Std Dev
    ==============================================================================
    PHC0                        5   3     2     -0.002      0.014     +9ns     2ns
    PHC1                        5   3     2     -0.003      0.007     -0ns     1ns
    PHC2                        5   3     2     -0.004      0.016    +33ns     2ns
    PHC3                        5   5     2     +0.002      0.078   +135ns    10ns
    PHC4                        5   3     2     -0.005      0.077   +130ns     9ns
    PHC5                        5   5     2     -0.006      0.131   +123ns    16ns
    

**Note:** Although the physical NIC clocks are tightly synchronized, the offset that `chrony` reports between clocks might be larger than expected. This occurs because the CPU experiences variable read latencies across the PCIe and NUMA topologies when accessing the clocks. Additionally, because [Precision Time Measurement (PTM)](https://pcisig.com/PCIExpress/ECN/Base/PrecisionTimeMeasurement_1.0a) and non-PTM modes introduce different read-latency skews, you should expect an offset if you compare results between the two modes.

If the command returns unexpected output, see Troubleshoot.

### Modify the `chrony` configuration

If you want to modify which physical NIC to synchronize the system clock of your instance to, you can update your configuration as follows:

  1. Remove `noselect` from the line that includes the vNIC name for which you want to use the corresponding physical NIC clock.
  2. Add `noselect` to the line that includes the vNIC name for which you want to stop using the corresponding physical NIC clock.
  3. Apply the new configuration by restarting `chronyd`: `systemctl restart chronyd`.



## Monitor time synchronization

This section describes the metrics that are available for time synchronization and how to use them to monitor time synchronization accuracy.

### Available metrics for time synchronization

You can use the following metrics to monitor time synchronization:

Measurement | Available metric and description  
---|---  
Instance system clock to physical NIC clock |  `logging.googleapis.com/user/phc-clock-max-error` This metric measures the accuracy of the synchronization of the instance system clock to the physical NIC clock on its host server. You must configure this metric by collecting it from Ops Agent and creating a log-based metric as described in Configure a custom metric for the instance system clock, which also creates a custom dashboard. Additionally, you can use this metric in the procedures described in Use Cloud Monitoring metrics.   
Physical NIC clock to UTC  |  `compute.googleapis.com/instance/time/firefly_utc_traceable_uncertainty` This metric represents the maximum error bound of the physical NIC clock compared to the actual UTC time. It is automatically reported to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). You view this metric, define alerting policies, and create custom dashboards as described in Use Cloud Monitoring metrics. This metric is also included on the dashboard created by the script in Configure a custom metric for the instance system clock.   
General health status of the physical NIC clock  |  `compute.googleapis.com/instance/time/firefly_nic_sync_healthy` This boolean metric indicates the general health status of the physical NIC clock, including both NIC-to-NIC and NIC-to-UTC synchronization. It is automatically reported to Cloud Monitoring. You view this metric, define alerting policies, and create custom dashboards as described in Use Cloud Monitoring metrics.   
  
For information about the length of time that Cloud Monitoring retains metric data, see [Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy) in _Cloud Monitoring quotas and limits_. For information about exporting metrics for long-term analysis, see [Cloud Monitoring metric export](https://docs.cloud.google.com/architecture/monitoring-metric-export) in the Cloud Architecture Center documentation.

### Configure a custom metric for the instance system clock

This section provides an example monitoring configuration that does the following:

  * Configures Ops Agent to collect `chrony`'s log for synchronization accuracy from your instance
  * Configures Cloud Monitoring to ingest the corresponding log from all instances in your project as a [log-based metric](https://docs.cloud.google.com/logging/docs/logs-based-metrics)



#### Configure Google Cloud Ops Agent on your instance

To configure Ops Agent to collect the metric needed for monitoring, do the following:

  1. If you haven't already, [install Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation) on your instance.

  2. Add the following configuration to the `/etc/google-cloud-ops-agent/config.yaml` file:
         
         logging:
           receivers:
             chrony_tracking_receiver:
               type: files
               include_paths:
                 - /var/log/chrony/tracking.log
           processors:
             chrony_tracking_processor:
               type: parse_regex
               regex: "^.*PHC.*  (?<max_error>[-\d\.eE]+)$"
           service:
             pipelines:
               chrony_tracking_pipeline:
                 receivers: [chrony_tracking_receiver]
                 processors: [chrony_tracking_processor]

  3. Restart Ops Agent by running the following command:
         
         systemctl restart google-cloud-ops-agent
         




#### Configure a log-based metric and dashboard in your project

To configure time synchronization monitoring for the instances in your project, run the following logging and dashboard setup script. This script helps you to complete the following tasks:

  * It sets appropriate permissions on the service account associated with the project of your instance. The script assumes that the service account used for the instances is the default service account for the project. If needed, replace `SERVICE_ACCOUNT_EMAIL` with a different value.
  * It creates a log-based metric that measures the accuracy of the time synchronization between the instance's system clock and physical NIC clock on the instance's host server.
  * It creates a dashboard that displays individual and combined time synchronization accuracy for your instances based on the custom log-based metric and available Firefly metrics.



To accomplish the preceding tasks, run the following script. After the script completes running, use the dashboard it created to view clock accuracy data for your project's instances.

**Note:** Log-based metrics use a [distribution-valued metric](https://docs.cloud.google.com/monitoring/charts/charting-distribution-metrics) that groups data into ranges (buckets). To ensure the dashboard doesn't underreport the measurement error, it evaluates your data's [distribution percentiles](https://docs.cloud.google.com/monitoring/api/v3/distribution-metrics) and displays the highest possible value of the bucket containing your highest data point. As a result, the maximum error displayed on the dashboard is a slight overestimate of the actual maximum error.
    
    
    #!/bin/bash
    
    if [ -z "$1" ]; then
        echo "Usage: setup_logging.sh <project_id>" >&2
        exit 1
    fi
    
    PROJECT_ID="$1"
    PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID  --format="value(projectNumber)")
    SERVICE_ACCOUNT_EMAIL=${PROJECT_NUMBER}-compute@developer.gserviceaccount.com
    
    # Grant permissions:
    
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" \
        --role="roles/compute.instanceAdmin"
    
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" \
        --role="roles/monitoring.metricWriter"
    
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" \
        --role="roles/logging.logWriter"
    
    # Configure log-based metric
    METRIC_CONF='
    {
      "name": "phc-clock-max-error",
      "description": "Maximum error of the VM clock from the host clock exposed by ptp_kvm",
      "filter": "logName=~\".*/logs/chrony_tracking_receiver\"",
      "metricDescriptor": {
        "metricKind": "DELTA",
        "valueType": "DISTRIBUTION",
        "unit": "s",
        "labels": [ { "key": "instance_id", "valueType": "STRING",
              "description": "Instance ID for the source instance" } ]
      },
      "valueExtractor": "REGEXP_EXTRACT(jsonPayload.max_error, \"(.*)\")",
      "bucketOptions": {
        "explicitBuckets": {
          "bounds": [
            0.0, 1.0E-6, 5.0E-6, 1.0E-5, 1.0E-4, 0.001, 0.01, 0.1, 1.0
          ]
        }
      },
      "labelExtractors": {
        "instance_id": "REGEXP_EXTRACT(resource.labels.instance_id, \"(.*)\")"
      }
    }
    '
    echo "$METRIC_CONF" > /tmp/clock-error-metric.json
    gcloud logging metrics create --project=${PROJECT_ID} phc-clock-max-error --config-from-file=/tmp/clock-error-metric.json
    
    # Create a dashboard plotting the clock accuracy
    
    DASHBOARD_CONF='
    {
      "displayName": "Clock Accuracy",
      "dashboardFilters": [],
      "description": "",
      "labels": {},
      "mosaicLayout": {
        "columns": 48,
        "tiles": [
          {
            "height": 19,
            "width": 48,
            "widget": {
              "title": "Combined Accuracy With Threshold",
              "id": "",
              "xyChart": {
                "chartOptions": {
                  "displayHorizontal": false,
                  "mode": "COLOR",
                  "showLegend": false
                },
                "dataSets": [
                  {
                    "breakdowns": [],
                    "dimensions": [],
                    "legendTemplate": "",
                    "measures": [],
                    "plotType": "LINE",
                    "sort": [],
                    "targetAxis": "Y1",
                    "timeSeriesQuery": {
                      "outputFullDuration": false,
                      "prometheusQuery": "(\n  histogram_quantile(\n    1, \n    sum by (le, instance_id) (\n      increase({\"__name__\"=\"logging.googleapis.com/user/phc-clock-max-error_bucket\", monitored_resource=\"gce_instance\"}[${__interval}])\n    )\n  ) * 1e9\n) \n+ on(instance_id) \nmax by (instance_id) (\n  max_over_time({\"__name__\"=\"compute.googleapis.com/instance/time/firefly_utc_traceable_uncertainty\", monitored_resource=\"gce_instance\"}[${__interval}])\n)",
                      "unitOverride": "ns"
                    }
                  }
                ],
                "thresholds": [
                  {
                    "color": "COLOR_UNSPECIFIED",
                    "direction": "DIRECTION_UNSPECIFIED",
                    "label": "",
                    "targetAxis": "Y1",
                    "value": 30000
                  }
                ],
                "yAxis": {
                  "label": "",
                  "scale": "LINEAR"
                }
              }
            }
          },
          {
            "yPos": 19,
            "height": 16,
            "width": 24,
            "widget": {
              "title": "NIC-UTC sync accuracy",
              "id": "",
              "xyChart": {
                "chartOptions": {
                  "displayHorizontal": false,
                  "mode": "COLOR",
                  "showLegend": false
                },
                "dataSets": [
                  {
                    "breakdowns": [],
                    "dimensions": [],
                    "legendTemplate": "",
                    "measures": [],
                    "minAlignmentPeriod": "60s",
                    "plotType": "LINE",
                    "sort": [],
                    "targetAxis": "Y1",
                    "timeSeriesQuery": {
                      "outputFullDuration": false,
                      "timeSeriesFilter": {
                        "aggregation": {
                          "alignmentPeriod": "60s",
                          "crossSeriesReducer": "REDUCE_SUM",
                          "groupByFields": [
                            "metric.label.\"instance_name\"",
                            "metric.label.\"nic_id\"",
                            "resource.label.\"instance_id\""
                          ],
                          "perSeriesAligner": "ALIGN_MEAN"
                        },
                        "filter": "metric.type=\"compute.googleapis.com/instance/time/firefly_utc_traceable_uncertainty\" resource.type=\"gce_instance\""
                      },
                      "unitOverride": ""
                    }
                  }
                ],
                "thresholds": [],
                "yAxis": {
                  "label": "",
                  "scale": "LINEAR"
                }
              }
            }
          },
          {
            "yPos": 19,
            "xPos": 24,
            "height": 16,
            "width": 24,
            "widget": {
              "title": "VM-NIC sync Accuracy",
              "id": "",
              "xyChart": {
                "chartOptions": {
                  "displayHorizontal": false,
                  "mode": "COLOR",
                  "showLegend": false
                },
                "dataSets": [
                  {
                    "breakdowns": [],
                    "dimensions": [],
                    "legendTemplate": "",
                    "measures": [],
                    "minAlignmentPeriod": "60s",
                    "plotType": "LINE",
                    "sort": [],
                    "targetAxis": "Y1",
                    "timeSeriesQuery": {
                      "outputFullDuration": false,
                      "timeSeriesFilter": {
                        "aggregation": {
                          "alignmentPeriod": "60s",
                          "crossSeriesReducer": "REDUCE_PERCENTILE_99",
                          "groupByFields": [
                            "metric.label.\"instance_id\""
                          ],
                          "perSeriesAligner": "ALIGN_DELTA"
                        },
                        "filter": "metric.type=\"logging.googleapis.com/user/phc-clock-max-error\""
                      },
                      "unitOverride": ""
                    }
                  }
                ],
                "thresholds": [],
                "yAxis": {
                  "label": "",
                  "scale": "LINEAR"
                }
              }
            }
          }
        ]
      }
    }
    '
    
    echo "$DASHBOARD_CONF" > /tmp/metrics-dashboard.json
    
    gcloud monitoring dashboards create --project=${PROJECT_ID} --config-from-file=/tmp/metrics-dashboard.json

### Use Cloud Monitoring metrics

The following sections describe how to use [Cloud Monitoring](https://monitoring/docs) metrics. You can use each of the available metrics for time synchronization in the following sections.

In addition to the Google Cloud console, you can create custom dashboards, set up alerts, and query the metrics through the [Monitoring API](https://docs.cloud.google.com/monitoring/api).

#### View metrics in Monitoring

This section describes how to view metrics in Monitoring.

###  Console 

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `VM instance` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **VM instance**.
     2. To select a metric, use the **Active metric categories** and **Active metrics** menus. For a list of available metrics, see Available metrics for time synchronization. 
     3. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. Configure how the data is viewed. By default, the display aggregates the metrics from all instances and physical NICs. To show per-NIC, per-instance metrics, do the following: in the **Aggregation** element, select **Unaggregated**. 

For more information about configuring a chart, see [Select metrics when using Metrics Explorer.](https://docs.cloud.google.com/monitoring/charts/metrics-selector)




#### Define alerting policies

This section describes how to define alerting policies.

When configuring how Monitoring evaluates a condition when data stops arriving, we recommend the option **Missing data points treated as values that violate the policy condition** , which helps capture silent data loss. However, this setting causes false positive alerts when an instance is deleted.

###  Console 

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `VM Instance` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select **VM Instance**.
     3. For the **Metric category** , select **Instance**.
     4. For the **Metric** , select a metric from the list in Available metrics for time synchronization..
     5. Select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Select a condition type and, if necessary, specify a threshold. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). 
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

#### Create custom Monitoring dashboards

This section describes how to create custom dashboards. For a specific example that uses a PromQL query, see Example: Create a custom dashboard that combines accuracy metrics.

###  Console 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click **Create dashboard**
  3. Optional: Update the dashboard title with a descriptive name for your dashboard.
  4. For each widget that you want to add to your dashboard, click **Add widget** , complete the dialog, and then select **Apply**.

For more information about adding widgets, see the following pages:

     * [Add charts and tables](https://docs.cloud.google.com/monitoring/charts#add_chart).
     * [Display alerts and charts for alerting policies](https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents).
     * [Display logs](https://docs.cloud.google.com/monitoring/charts/view-logs).
     * [Add text and groupings](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping).



### Example: Create a custom dashboard that combines accuracy metrics

Monitoring lets you create custom dashboards. Dashboards can use any of the available metrics for time synchronization.

This section contains an example PromQL query that you can paste into a custom Monitoring dashboard. For more information about PromQL, see [PromQL for Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql).

The query in this section generates a total accuracy metric by combining the following:

  * the metric that measures the accuracy of the instance system clock to physical NIC clock (`phc-clock-max-error`)
  * the metric that measures the accuracy of the physical NIC clock to UTC (`firefly_utc_traceable_uncertainty`)




###  Console 

  1. Follow the steps to [Access the code editor](https://docs.cloud.google.com/monitoring/promql/promql-in-monitoring#goto-editor) for PromQL.

  2. Enter the following query in the text field:
         
         (
           histogram_quantile(
            1,
            sum by (le, instance_id) (
              increase({"__name__"="logging.googleapis.com/user/phc-clock-max-error_bucket", monitored_resource="gce_instance"}[${__interval}])
            )
           ) * 1e9
         )
         + on(instance_id)
         max by (instance_id) (
          max_over_time({"__name__"="compute.googleapis.com/instance/time/firefly_utc_traceable_uncertainty", monitored_resource="gce_instance"}[${__interval}])
         )
         

  3. Click **Run Query**.




For more information about how to use the editor and save your charts, see [Use the code editor for PromQL](https://docs.cloud.google.com/monitoring/promql/promql-in-monitoring).

## Troubleshoot

You might receive unexpected output when verifying your `chrony` configuration, such as the following output that indicates `chrony` failed to start:
    
    
    506 Cannot talk to daemon
    

To help troubleshoot, check the `journald` logs for `chrony`:
    
    
    journalctl -u chronyd.service
    

The following example output shows an error that occurs if you apply a configuration intended for `chrony` 4.7 and later while an earlier version of `chrony` is installed on your instance.
    
    
    Feb 19 06:19:42 host-name systemd[1]: Starting chronyd.service - NTP client/server...
    Feb 19 06:19:42 host-name chronyd[35160]: chronyd version 4.6.1 starting (+CMDMON +NTP +REFCLOCK +RTC +PRIVDROP +SCFILTER +SIGND +ASYNCDNS +NTS +SECHASH +IPV6 +DEBUG)
    Feb 19 06:19:42 host-name chronyd[35160]: Setting filter length for PHC0 to 1
    Feb 19 06:19:42 host-name chronyd[35160]: Could not open eth0 : No such file or directory
    Feb 19 06:19:42 host-name chronyd[35160]: Fatal error : Could not open PHC
    Feb 19 06:19:42 host-name chronyd[35157]: Could not open PHC
    Feb 19 06:19:42 host-name systemd[1]: chronyd.service: Control process exited, code=exited, status=1/FAILURE
    Feb 19 06:19:42 host-name systemd[1]: chronyd.service: Failed with result 'exit-code'.
    Feb 19 06:19:42 host-name systemd[1]: Failed to start chronyd.service - NTP client/server.
    

## Known issues

The following known issues might occur when configuring accurate time for U4 instances:

  * Accuracy metrics are reported only for network interfaces where non-zero traffic was observed during the lifetime of the instance. To work around this issue, you can use `nic0` as the clock source for synchronization to help ensure telemetry. Alternatively, ensure that there is traffic on all network interfaces. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
