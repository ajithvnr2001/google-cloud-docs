---
url: https://docs.cloud.google.com/compute/shielded-vm/docs/integrity-monitoring/
title: Monitoring integrity on Shielded VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:04:10.790574+00:00
---

# Monitoring integrity on Shielded VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/shielded-vm/docs/integrity-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Shielded VM ](https://docs.cloud.google.com/compute/shielded-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm)



Send feedback 

#  Monitoring integrity on Shielded VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to monitor the boot integrity of [Shielded VM instances](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) that have [integrity monitoring enabled](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm), identify the cause of an integrity validation failure, and update the integrity policy baseline.

## Monitoring VM boot integrity by using Monitoring

Use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to view integrity validation events and set alerts for them, and [Cloud Logging](https://docs.cloud.google.com/logging/docs) to review details of those events.

### Viewing integrity validation events

**Note:** The metrics chart shows Shielded VMs with [integrity monitoring disabled](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm) as **unknown**.

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Boot Validation` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **VM instance**.
     2. In the **Active metric categories** menu, select **Instance**.
     3. In the **Active metrics** menu, select **Early Boot Validation** or **Late Boot Validation**. 
        * **Early Boot Validation** : Shows the pass/fail status of the early boot portion of the last boot sequence. Early boot is the boot sequence from the start of the UEFI firmware until it passes control to the bootloader.
        * **Late Boot Validation** : Shows the pass/fail status of the late boot portion of the last boot sequence. Late boot is the boot sequence from the bootloader until completion. This includes the loading of the operating system kernel.
     4. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



### Setting alerts on integrity validation events

Set alerts on the values of the **Early Boot Validation** and **Late Boot Validation** metrics if you want to be notified when there is a boot validation failure on your VM instance. For information about alerting, see [Introduction to Alerting](https://docs.cloud.google.com/monitoring/alerts):

  * For early boot validation alerting policy settings, see [Compute Engine early boot validation](https://docs.cloud.google.com/monitoring/alerts/target-configuration-library#compute-early-boot).

  * For late boot validation alerting policy settings, see [Compute Engine late boot validation](https://docs.cloud.google.com/monitoring/alerts/target-configuration-library#compute-late-boot).




### Viewing integrity validation event details

  1. [Go to the VM instances page](https://console.cloud.google.com/compute/instances)
  2. Click the instance ID to open the **VM instance details** page.
  3. Under **Logs** , click **Cloud Logging**.
  4. Locate the `earlyBootReportEvent` or `lateBootReportEvent` log entry that you want to review.
  5. Expand the log entry > `jsonPayload` > `earlyBootReportEvent` or `lateBootReportEvent`, as appropriate. Within that section, the `policyEvaluationPassed` element identifies whether the given section of the boot sequence passed verification against the integrity policy baseline.
  6. Expand the `actualMeasurements` section and the numbered elements within it to see the [platform configuration register](https://link.springer.com/chapter/10.1007/978-1-4302-6584-9_12) (PCR) values saved from the latest boot sequence. The PCR values are saved in the `value` elements within the numbered elements. The PCR values identify the boot components and component load order used by the latest boot sequence, and are compared to the integrity policy baseline to determine if there has been any change in the VM instance boot sequence. For more information about what the PCRs represent, see [Integrity monitoring events](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring-events).
  7. Expand the `policyMeasurements` section to see the PCR values saved for the integrity policy baseline.



### Automating responses to integrity validation events

You can automate responses to boot validation events by exporting the Cloud Logging logs and processing them in another service like Cloud Run functions. For more information, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview) and [Automating responses to integrity validation failures](https://docs.cloud.google.com/compute/shielded-vm/docs/automating-responses-integrity-failures).

## Determining the cause of boot integrity validation failure

  1. [Go to the VM instances page](https://console.cloud.google.com/compute/instances)
  2. Click the instance ID to open the **VM instance details** page.
  3. Under **Logs** , click **Cloud Logging**.
  4. Locate the most recent `earlyBootReportEvent` and `lateBootReportEvent` log entries and see which one has a `policyEvaluationPassed` value of **false**.
  5. Expand the log entry > `jsonPayload` > `earlyBootReportEvent` or `lateBootReportEvent`, as appropriate.
  6. Expand the `actualMeasurements` and `policyMeasurements` sections and the numbered elements within them to see the [platform configuration register](https://link.springer.com/chapter/10.1007/978-1-4302-6584-9_12) (PCR) values saved from the latest boot sequence and the integrity policy baseline, respectively. The PCR values identify the boot components and component load order used by the latest boot sequence and the integrity policy baseline.
  7. Compare the PCR values in the `actualMeasurements` and `policyMeasurements` sections to determine where the variation between the latest boot sequence and the integrity policy baseline occurred. Whichever comparison produces dissimilar values is the issue that caused validation failure. Be aware that the element numbers in these sections seldom correspond to the PCR numbers, and similarly numbered elements in `actualMeasurements` and `policyMeasurements` might represent different PCRs. For example, in the early boot sequence for both Windows and Linux, the `3` element in `actualMeasurements` and the `2` element in `policyMeasurements` both represent PCR7.

**Important:** The elements representing PCR13 and PCR14 in the Windows boot sequence don't appear in `policyMeasurements` until after the first reboot following VM instance creation. During that reboot, those PCR values are captured and added to the integrity policy baseline. Until then, boot integrity validation uses only PCR4, PCR7, and PCR11 in `policyMeasurements`.

  8. Check [Integrity monitoring events](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring-events) to determine what the changed PCR represents, and investigate whether that is an expected change.




## Updating the integrity policy baseline

The initial integrity policy baseline is derived from the implicitly trusted boot image when the instance is created. Updating the baseline updates the integrity policy baseline using the current instance configuration. The VM instance must be running when you update the baseline.

You should update the baseline after any planned boot-specific changes in the instance configuration, like kernel updates or kernel driver installation, as these will cause integrity validation failures. If you have an unexpected integrity validation failure, you should investigate the reason for the failure and be prepared to stop the instance if necessary.

You must have the `setShieldedInstanceIntegrityPolicy` permission to be able to update the integrity policy baseline.

Use the following procedure to update the integrity policy baseline.

###  gcloud 

Update the VM instance's integrity policy baseline by using the `compute instances update` command with the `--shielded-learn-integrity-policy` flag.

The following example resets the integrity policy baseline for the **my-instance** VM instance:
    
    
    gcloud compute instances update INSTANCE_NAME \
        --zone=ZONE \
        --shielded-learn-integrity-policy
    

Replace the following:

  * INSTANCE_NAME: Name of the VM.
  * ZONE: Zone where the VM exists.



###  REST 

Update the VM instance's integrity policy baseline by using the `updateAutoLearnPolicy` request body item with the `setShieldedInstanceIntegrityPolicy` method.

The following example resets the integrity policy baseline for a VM instance.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/setShieldedInstanceIntegrityPolicy?key=YOUR_API_KEY
    {
      "updateAutoLearnPolicy": true
    }
    

Replace the following:

  * PROJECT_ID: Project ID of your project where VM exists.
  * INSTANCE_NAME: Name of the VM.
  * ZONE: Zone where the VM exists.
  * YOUR_API_KEY: An API key that lets you access the API.



## What's next

  * [Read more](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) about the security features offered by Shielded VM.
  * Learn more about [modifying options on a Shielded VM instance](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm).
  * [Learn about one approach to automating responses to integrity monitoring events](https://docs.cloud.google.com/compute/shielded-vm/docs/automating-responses-integrity-failures).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
