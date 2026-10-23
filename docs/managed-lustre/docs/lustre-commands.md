---
url: https://docs.cloud.google.com/managed-lustre/docs/lustre-commands/
title: Lustre commands \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:29.486320+00:00
---

# Lustre commands  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/lustre-commands/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Lustre commands Stay organized with collections  Save and categorize content based on your preferences. 

## Version information

Google Cloud Managed Lustre is based on Lustre 2.14, but includes additional features.

## Sensitive information in the `jobid_var` parameter

The Lustre client software can track I/O statistics by "jobid" if the `jobid_var` Lustre configuration parameter is set (e.g. `lctl get_param jobid_var`). By default, this is disabled.

If you choose to enable this client-side feature, avoid including potentially sensitive information in this field, as the data is categorized as [resource fields data](https://cloud.google.com/terms/service-terms), and not as Customer data.

For example, setting `jobid_var` to `procname_uid` will send the name of the writing process and its UID from the client to the server. If the process name is potentially sensitive to your organization, consider using a different setting. See <https://doc.lustre.org/lustre_manual.xhtml#jobstats> for detailed instructions for configuring jobstats on Lustre clients.

## Unsupported Lustre features

The following Lustre features are not supported:

  * Client-side data compression
  * Persistent client caching
  * Unsigned or open-source Lustre clients



## Unsupported Lustre commands

The following Lustre commands are not supported:

  * `lfs changelog`
  * `lctl network up`/`down`
  * `lctl conf_param <device> <params>`
  * `lctl deactivate`
  * `lctl abort_recovery`
  * `lctl debug` commands
  * `lctl debug_daemon`
  * `lctl debug_kernel [file] [raw]`
  * `lctl debug_file`
  * `lctl clear`
  * `lctl mark`
  * `lctl filter`
  * `lctl show`
  * `lctl debug_list`
  * `lctl modules`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
