---
url: https://docs.cloud.google.com/tpu/docs/tpu-iap/
title: Connect to a TPU VM without a public IP address \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:09.435829+00:00
---

# Connect to a TPU VM without a public IP address  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/tpu-iap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to a TPU VM without a public IP address

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

If your organization has a `constraints/compute.vmExternalIpAccess` organization policy constraint, you need to create TPU VMs that don't have an external IP address. To connect to a TPU VM without an external IP address, you need to:

  1. Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) for the subnet where you will create a TPU VM.
  2. Grant `roles/iap.tunnelResourceAccessor` and `roles/tpu.admin` to users who will connect to the TPU VMs.
  3. Create a TPU VM without a public IP address.
  4. Connect to your TPU VM using `--tunnel-through-iap` option.



## Enable Private Google Access

To use an IAP, you must enable Private Google Access which lets you connect to VMs that don't have external IP addresses. In the following command replace your-subnet with the name of the subnet where you will create the TPU VM and your-region with the region where the TPU VM will be located.
    
    
    gcloud compute networks subnets update your-subnet \
    --region=your-region \
    --enable-private-ip-google-access

## Grant permissions

Users that need to connect to the TPU VMs using SSH that don't have public IP addresses must be granted the iap.tunnelResourceAccessor role. For more information about granting a role, see [Granting an IAM Role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

## Create a TPU VM without a public IP address

The following command shows how to create a TPU VM with no public IP address.
    
    
    gcloud compute tpus tpu-vm create tpu-vm-name \
      --zone $ZONE \
      --project your-project \
      --internal-ips \
      --version tpu-vm-tf-2.17.1-pjrt \
      --accelerator-type v2-8 \
      --subnetwork your-subnet \

## Connect to your TPU VM using SSH with IAP tunneling

The following command shows how to connect to a TPU VM using IAP tunneling.
    
    
    gcloud alpha compute tpus tpu-vm ssh tpu-vm-name --tunnel-through-iap

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
