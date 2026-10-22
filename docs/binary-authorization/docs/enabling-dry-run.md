---
url: https://docs.cloud.google.com/binary-authorization/docs/enabling-dry-run/
title: Enable dry-run mode \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:12:00.568296+00:00
---

# Enable dry-run mode  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/enabling-dry-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Enable dry-run mode Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document or section includes references to one or more terms that Google considers disrespectful or offensive. The terms are used because they are keywords in the software that's described in the document. 

The terms: `whitelist`

This document explains how to enable dry-run mode.

When you enable dry-run mode, Binary Authorization allows all container images to be deployed, even if those images violate the Binary Authorization policy. Policy compliance status messages are logged to [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit). You can inspect the log to determine whether the images would have been disallowed and take corrective action. When the policy configuration works as you intend, you can disable dry-run mode to enable Binary Authorization enforcement; images that violate the policy are disallowed from being deployed.

You can set dry-run mode in the default rule or a specific rule.

## Before you begin

To use dry-run mode, [set up Binary Authorization for your platform](https://docs.cloud.google.com/binary-authorization/docs/set-up-platform).

## Enable dry run

**Caution:** Enabling dry run in your default admission rule, as shown, allows all container images to be deployed, even if they violate the deployment policy.

To enable dry run, do the following:

###  Console 

  1. Go to the Binary Authorization page in the Google Cloud console.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/).

  2. Click **Edit Policy**.

  3. In **Default Rule** or a specific rule, select **Dry-run mode**.

**Note:** To demonstrate dry-run mode, you can also set the rule to **Disallow all images**. With this setting, all images violate the policy, are disallowed from being deployed, and the violations are logged.
  4. Click **Save Policy**.




###  gcloud 

  1. Export the Binary Authorization policy to a YAML file:
         
         gcloud container binauthz policy export  > /tmp/policy.yaml
         

  2. In a text editor, set `enforcementMode` to `DRYRUN_AUDIT_LOG_ONLY` and save the file.

**Note:** To demonstrate dry-run mode, you can set `evaluationMode` to `ALWAYS_DENY`. With this setting, all images violate the policy, are disallowed from being deployed, and the violations are logged.
  3. To update the policy, import the file by executing the following command:
         
         gcloud container binauthz policy import /tmp/policy.yaml
         




**Note:** It can take a few minutes for the policy to take effect.

To test dry-run mode, deploy images that violate the policy and then view dry-run mode events from Binary Authorization for [GKE](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs#dry_run_events), [Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run#query_for_dry_run_events), or [Google Distributed Cloud](https://docs.cloud.google.com/binary-authorization/docs/viewing-on-prem-logs#view_dry_run_log_entries).

### Disable dry-run mode

To disable dry-run mode, update your policy as follows:

###  Console 

  1. Go to the Binary Authorization page in the Google Cloud console.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/)

  2. Click **Edit Policy**.

  3. In **Default Rule** or a specific rule, clear **Dry-run mode**.

  4. Click **Save Policy**.




###  gcloud 

  1. Export the Binary Authorization policy:
         
         gcloud container binauthz policy export  > /tmp/policy.yaml
         

  2. In a text editor, set `enforcementMode` to `ENFORCED_BLOCK_AND_AUDIT_LOG` and save the file.

  3. To update the policy, import the file by executing the following command:
         
         gcloud container binauthz policy import /tmp/policy.yaml
         




**Note:** It can take a few minutes for the policy to take effect.

## What's next

  * View dry-run mode events from Binary Authorization for [GKE](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs#dry_run_events) in Cloud Audit Logs.
  * View dry-run mode events from Binary Authorization for [Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run#query_for_dry_run_events) in Cloud Audit Logs.
  * View dry-run mode events from Binary Authorization for [Distributed Cloud](https://docs.cloud.google.com/binary-authorization/docs/viewing-on-prem-logs#view_dry_run_log_entries) in Cloud Audit Logs. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
