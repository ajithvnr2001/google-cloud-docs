---
url: https://docs.cloud.google.com/deep-learning-vm/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Deep Learning VM Images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:26:17.389327+00:00
---

# Troubleshooting  |  Deep Learning VM Images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-vm/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Deep Learning VM Images ](https://docs.cloud.google.com/deep-learning-vm/docs)
  * [ Support ](https://docs.cloud.google.com/deep-learning-vm/docs/troubleshooting)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page describes problems that can come up when creating Deep Learning VM Images instances, and tells you how to address the problems.

## Quota exceeded

**Symptom** : `- Quota 'NVIDIA_P4_GPUS' exceeded. Limit: 0.0 in region us-east1.`

**Problem** : You do not have enough quota.

**Solution** : You must have GPU quota before you can create instances with GPUs. Check the [quotas page](https://console.cloud.google.com/iam-admin/quotas) to ensure that you have enough GPUs available in your project. If GPUs are not listed on the quotas page or you require additional GPU quota, [request a quota increase](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota). If your project has an established billing history, it will receive quota automatically after you submit the request. Free Trial accounts do not receive GPU quota by default.

Keep in mind that preemptible GPUs and normal GPUs require separate quota requests. You can't use preemptible GPU quota for normal GPUs. Also, quota is per region, so be sure that you are creating the instance in the region where you have quota.

## Resource not found

**Symptom** : `- The resource 'projects/deeplearning-platform/zones/europe-west4-c/acceleratorTypes/nvidia-tesla-p4' was not found`

**Problem** : You are trying to create an instance with one or more GPUs in a region where GPUs are not available (for example, an instance with a P4 GPU in `europe-west4-c`).

**Solution** : To determine which region has the required GPU, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

## Preemptible instances

**Symptom** : I can't create preemptible instance from the UI, even though I have quota.

**Solution** : At this time, a preemptible instance can't be created from Google Cloud Marketplace. You must use the CLI. Be sure to add `--preemptible` when setting up your new instance.

## Unable to use SSH port forwarding to connect to JupyterLab

**Symptom** : When [using SSH port forwarding to connect to JupyterLab](https://docs.cloud.google.com/deep-learning-vm/docs/jupyter), you are unable to connect to the instance.

**Problem** : You are trying to connect to the wrong TCP socket.

**Solution** :

  * On some Linux clients, the localhost resolves to the IPv6 loopback address (`::1`). Check this by using `ping -c 1 localhost`. If this command returns the IPv6 address, use `-L 8080:127.0.0.1:8080` (rather than `-L 8080:localhost:8080`) in the `gcloud compute ssh` command.

  * Ensure that you connect to `http://localhost:8080` (instead of `https://localhost:8080`) on your local client.




## Community support

Ask a question about Deep Learning VM on [Stack Overflow](https://stackoverflow.com/questions/tagged/google-dl-platform) or join the [google-dl-platform](https://groups.google.com/forum/#!forum/google-dl-platform) Google group to discuss Deep Learning VM.

[Learn more about getting support from the community](https://docs.cloud.google.com/deep-learning-vm/docs/getting-support#get_support_from_the_community).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
