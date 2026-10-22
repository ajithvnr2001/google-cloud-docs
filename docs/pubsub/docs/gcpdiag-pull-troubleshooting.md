---
url: https://docs.cloud.google.com/pubsub/docs/gcpdiag-pull-troubleshooting/
title: Troubleshoot pull delivery issues \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:40.036535+00:00
---

# Troubleshoot pull delivery issues  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/gcpdiag-pull-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshoot pull delivery issues Stay organized with collections  Save and categorize content based on your preferences. 

Use the `gcpdiag` tool to discover and fix potential delivery issues for pull subscriptions.

## Use the `gcpdiag` tool

[`gcpdiag`](https://gcpdiag.dev) is an open source tool. It is not an officially supported Google Cloud product. You can use the `gcpdiag` tool to help you identify and fix Google Cloud project issues. For more information, see the [gcpdiag project on GitHub](https://github.com/GoogleCloudPlatform/gcpdiag/#gcpdiag---diagnostics-for-google-cloud-platform).

The `gcpdiag` tool helps you discover Pub/Sub pull delivery issues by performing the following checks:

  * **Quota errors:** Evaluates Logs Explorer logs to check for any quota errors in regions and zones.
  * **Throughput qualification:** Performs checks on the [delivery latency health](https://docs.cloud.google.com/pubsub/docs/monitoring#delivery_latency_health) of a subscription.



For a list of `gcpdiag` pull delivery evaluation steps, see [Potential steps](https://gcpdiag.dev/runbook/diagnostic-trees/pubsub/pull-subscription-delivery/#potential-steps).

### Run the `gcpdiag` command

You can run the `gcpdiag` command from Google Cloud CLI or within a [Docker](https://www.docker.com/) container. 

## Google Cloud console

  1. Complete and then copy the following command. 
    
    gcpdiag runbook pubsub/pull-subscription-delivery \
      --project=PROJECT_ID \
      --parameter subscription_name=SUBSCRIPTION_NAME

  2. Open the Google Cloud console and activate Cloud Shell.
[Open Cloud console](https://console.cloud.google.com/cloudpubsub/topic/list?cloudshell=true%20?cloudshell=true)
  3. Paste the copied command.
  4. Run the `gcpdiag` command, which downloads the `gcpdiag` docker image, and then performs diagnostic checks. If applicable, follow the output instructions to fix failed checks. 



## Docker

You can [ run `gcpdiag` using a wrapper](https://github.com/GoogleCloudPlatform/gcpdiag?tab=readme-ov-file#installation) that starts `gcpdiag` in a [Docker](https://www.docker.com/) container. Docker or [Podman](https://podman.io/) must be installed.

  1. Copy and run the following command on your local workstation. 
         
         curl https://gcpdiag.dev/gcpdiag.sh >gcpdiag && chmod +x gcpdiag

  2. Execute the `gcpdiag` command. 
         
         ./gcpdiag runbook pubsub/pull-subscription-delivery \
           --project=PROJECT_ID \
           --parameter subscription_name=SUBSCRIPTION_NAME




View [available parameters](https://gcpdiag.dev/runbook/diagnostic-trees/pubsub/pull-subscription-delivery/#parameters) for this runbook.

Replace the following:

    * PROJECT_ID: The ID of the project to evaluate
    * SUBSCRIPTION_NAME: The name of the subscription to evaluate in your project



Useful flags:

  * `--universe-domain`: If applicable, the [Trusted Partner Sovereign Cloud](https://cloud.google.com/blog/products/identity-security/new-sovereign-controls-for-gcp-via-assured-workloads) domain hosting the resource
  * `--parameter` or `-p`: Runbook parameters



For a list and description of all `gcpdiag` tool flags, see the [`gcpdiag` usage instructions](https://github.com/GoogleCloudPlatform/gcpdiag?tab=readme-ov-file#usage).

## Read related information

  * [Pub/Sub pull subscription common issues](https://docs.cloud.google.com/pubsub/docs/pull-troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
