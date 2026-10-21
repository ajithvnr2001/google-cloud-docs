---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/networking-best-practices/
title: Networking best practices \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:01:17.043772+00:00
---

# Networking best practices  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/networking-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Networking best practices Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document describes best practices for creating a secure and resilient networking environment for AI Hypercomputer workloads. These recommendations are intended for network architects, network engineers, and developers who want to configure and deploy artificial intelligence (AI) and machine-learning (ML) workloads on AI Hypercomputer.

## Establish clear and restricted IAM roles

Configuring IAM correctly helps to improve the security and success of your AI Hypercomputer deployments. In production environments, inadequate or misconfigured permissions can lead to deployment failures. AI Hypercomputer deployments, especially those using [ Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview), often fail in environments with hardened security postures where the default Compute Engine service account does not have the broad `Editor` role.

To help mitigate deployment issues that might occur due to permission issues, follow best practices listed in this section.

### Use dedicated service accounts

For better security and control, avoid using the default Compute Engine service account. Instead, create a dedicated service account for your AI Hypercomputer deployment.

You can use Managed Workload Identity to authenticate and authorize workloads instead of using service account tokens. For more information, see [Authenticate workloads using mTLS](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls) for Compute Engine or [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy#workload-identity) for GKE.

### Grant necessary IAM roles

Grant the following IAM roles to the dedicated service account you created:

  * **Compute Admin** (`roles/compute.admin`): provides full control of Compute Engine resources.
  * **Service Account User** (`roles/iam.serviceAccountUser`): allows the service account to be attached to other resources, which is crucial for tools like Packer when building custom images.
  * **Storage Admin** (`roles/storage.admin`): requires access to and management of Cloud Storage buckets, for example, to store Packer images or other artifacts.
  * **Logging Admin** (`roles/logging.admin`): allows the service account to configure logging and view logs, which is essential for debugging.



### Verify permissions before deployment

Before you start a deployment, verify that your service account has the necessary permissions. Run the [`gcloud projects get-iam-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy):
    
    
    gcloud projects get-iam-policy PROJECT_ID \
        --flatten="bindings[].members" \ format='table(bindings.role)' \
        --filter="bindings.members:serviceAccount:SERVICE_ACCOUNT_EMAIL"
    

Replace the following:

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `SERVICE_ACCOUNT_EMAIL`: The email address of the service account you want to verify.



This command lists all the roles granted to your service account on the specified project. Ensure that the roles listed in Grant necessary IAM roles are shown in the output.

## Restrict public network access and harden firewall configurations

Restrict public network access and harden firewall configurations to improve security. This fundamental security practice mitigates the risk of overly permissive default firewall rules.

Virtual machine (VM) setup failures can occur in production environments due to restrictive firewall configurations not present in internal testing. Engineers might have difficulty diagnosing these failures without knowledge of specific firewall rules.

Review and update your firewall rules to minimize direct exposure to the internet. For more information about VPC firewall rules, see [ VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

## Standardize internal networking defaults

Standardize internal networking defaults to reduce risks and configuration challenges. Default networking behaviors can create risks or configuration challenges in complex or security-hardened environments. Google recommends the following configurations:

  * **Use Zonal DNS:** for new projects, set the internal Domain Name System (DNS) to Zonal DNS only. This approach helps reduce the impact of a potential global DNS outage. For more information about using Zonal DNS, see [Overview of using Zonal DNS](https://docs.cloud.google.com/compute/docs/networking/zonal-dns).
  * **Disable external IP addresses:** when possible, disable external IP addresses. Before you disable the IP addresses, you must carefully plan and test in a staging environment, as some services like managed instance groups (MIGs) or GKE clusters with public nodes rely on them. For more information about limiting public IP addresses, see [Limiting public IP addresses on Google Cloud](https://cloud.google.com/blog/topics/developers-practitioners/limiting-public-ips-google-cloud).



## Optimize networking by infrastructure

The networking best practices for your deployment vary depending on your choice of infrastructure: general GPUs or clustered GPUs.

### General GPU best practices

When you use general GPUs, follow these networking best practices:

  * **Use compact placement policies** : if your General GPU instances don't report a `physicalHost` ID, use compact placement policies to identify instance groupings and optimize performance for these resources. For more information, see [Define instance placement](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).
  * **Use Google Virtual NIC (gVNIC) for host communication** : for consistent performance, use standard TCP/IP over gVNIC for all host-to-host communication. For more information about gVNIC, see [Using Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).
  * **Simplify with a single-VPC architecture** : unless isolation requirements dictate otherwise, use a standard, single-VPC network for all communication. This single-VPC recommendation applies to G2, G4, A2, and N1 series; A3 Edge is an exception that requires four data VPCs and GPUDirect-TCPX. For more information, see [Maximize GPU network bandwidth in Standard mode clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx).



### Clustered GPU best practices

When you use clustered GPUs, follow these networking best practices:

  * **Implement a multi-VPC environment** : to help ensure GPU-to-GPU traffic is isolated onto dedicated high-bandwidth VPCs to prevent host or storage traffic from competing for bandwidth. For more information, see [Multi-VPC environment](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-overview#multi-vpc).
  * **Apply RDMA-optimized network profiles** : use Google-managed network profiles to automatically configure your VPC for the low latency required by RDMA over Converged Ethernet (RoCE). For more information, see [Network profiles for specific use cases](https://docs.cloud.google.com/vpc/docs/network-profiles).
  * **Offload infrastructure tasks** : use custom Titanium NICs to offload tasks, such as processing for network packets and virtualization for storage, reserving CPU cycles for your AI application.



## Summary of best practices

The following table summarizes the best practices recommended in this document:

Topic | Task  
---|---  
IAM | Establish clear and restricted IAM roles  
Firewall | Restrict public network access and harden firewall configurations  
Network Defaults | Standardize internal networking defaults  
Infrastructure | Optimize networking by infrastructure  
  
## What's next

  * Secure your deployments by learning more about the [best practices for using service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).
  * Harden your network by learning more about [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).
  * Understand accelerator connectivity by learning more about [ AI Hypercomputer network architecture](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
