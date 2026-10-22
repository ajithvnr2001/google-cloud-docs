---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/vm-runtime/view-console-logs/
title: View console logs for VMs that use VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:48.961057+00:00
---

# View console logs for VMs that use VM Runtime on GDC  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/vm-runtime/view-console-logs/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)



Send feedback 

#  View console logs for VMs that use VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

This document is intended for application owners that run Google Distributed Cloud connected. This document shows you how to view console logs for virtual machines (VMs) that use VM Runtime on GDC. You can use the VM console logs to troubleshoot and diagnose problems in your cluster.

## Before you begin

To complete this document, you need access to the following resources:

  * A VM that runs in one of your clusters. If needed, [create a VM in Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines#create_a_virtual_machine).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines#install_the_virtctl_management_tool).



## Connect to VM

To make sure there are logs to review, connect to your VM and generate some log activity.

  1. To access a VM from the console, use `kubectl`:
         
         kubectl virt console VM_NAME
         

Replace `VM_NAME` with the name of the VM that you want to connect to.

  2. When prompted, enter the user credentials you specified when you created the VM.

  3. Run a command to check for updates, such as `apt-get` for Debian-based VMs or `yum check-update` for Red Hat-based VMs.

###  Debian-based 
         
         apt-get update
         

###  Red Hat-based 
         
         yum check-update
         

  4. After you have successfully generated some console log activity, exit the VM session and console:
         
         Ctrl + ]
         




## View VM console logs

You view VM console logs in the Google Cloud console. VM serial console logs are streamed to Cloud Logging and can be viewed in Logs Explorer. VMs that run using VM Runtime on GDC are classed as containers in the console logs.

  1. In the Google Cloud console, go to the **Logs Explorer** page in the **Logging** menu.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** field, enter the following basic query:
         
         resource.type="k8s_container"
         resource.labels.container_name="log"
         

  3. The **Query results** window shows the output of the console logs from your VMs, as shown in the following example screenshot:

![The output of the query displays the console logs](https://docs.cloud.google.com/static/distributed-cloud/images/vm-runtime-view-console-logs.png)

  4. You can further filter the results of your query to a particular VM by adding the cluster name and the name of the VM to your query:
         
         resource.type="k8s_container"
         resource.labels.container_name="log"
         resource.labels.cluster_name="CLUSTER_NAME"
         labels.k8s-pod/kubevirt/vm="VM_NAME"
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster that contains your VM.
     * `VM_NAME`: the name of your VM.



## What's next

  * To learn more about how to filter your console logs, see [Build queries in Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
