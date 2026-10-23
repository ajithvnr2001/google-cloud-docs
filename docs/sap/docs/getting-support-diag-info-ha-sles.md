---
url: https://docs.cloud.google.com/sap/docs/getting-support-diag-info-ha-sles/
title: High-availability clusters on SLES diagnostic information \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:33.516045+00:00
---

# High-availability clusters on SLES diagnostic information  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/getting-support-diag-info-ha-sles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Support ](https://docs.cloud.google.com/sap/docs/getting-support)



Send feedback 

#  High-availability clusters on SLES diagnostic information Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the diagnostic information that helps Cloud Customer Care troubleshoot issues related to SUSE Linux Enterprise Server (SLES) high-availability (HA) clusters running SAP solutions on Google Cloud. Sharing these details when you create a support case helps Customer Care quickly isolate the root cause and reduce the overall resolution time.

Include the following details in your support case:

  * A complete and detailed description of the problem or error, including the following:

    * The current application or system state.
    * The date and time when the error occurred.
    * If you're facing a performance issue with your SAP workload, then [gather diagnostic information about SAP workload performance](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-performance).
  * If you're using [Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning), then generate and share the [support bundle](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/getting-support-diag-info#support_bundle).

  * If you aren't using [Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning), then collect information about the cluster, which includes the following:

    * From each node in the HA cluster, the TAR archive of the system report that you generate by running the SUSE `supportconfig` utility:
          
          supportconfig -l

    * The TAR archive of log files and node configurations that you generate by running the `hb_report` utility.

Specify a start time (_from time_) that is approximately 1 hour before the issue occurred. Specify an end time (_to time_) that is at least an hour after the issue was resolved.

Use the following command to run the `hb_report` utility, specifying the _from time_ and _to time_ on the '-f' and '-t' flags, respectively.
          
          hb_report -f "yyyy/mm/dd hh:mm" -t "yyyy/mm/dd hh:mm"

For more information from SUSE about the `supportconfig` tool and the `hb_report` utility, see [Indepth HANA Cluster Debug Data Collection (PACEMAKER, SAP)](https://www.suse.com/support/kb/doc/?id=000019142).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
