---
url: https://docs.cloud.google.com/compute/docs/instances/access-overview/
title: Choose an access method \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:55.372348+00:00
---

# Choose an access method  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/access-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Choose an access method Stay organized with collections  Save and categorize content based on your preferences. 

If you have Linux virtual machine (VM) instances running on Google Cloud, you might need to share or restrict user or application access to your VMs.

  * If you need to manage user access to your Linux VM instances, you can use one of the following methods:

    * OS Login
    * Managing SSH keys in metadata
    * [Temporarily grant a user access to an instance](https://docs.cloud.google.com/compute/docs/access/managing-access-to-resources#bind-member)
  * If you need to manage application access to your VM instances, see [Use SSH with service accounts](https://docs.cloud.google.com/compute/docs/tutorials/service-account-ssh).


**Note:** When a user connects to a VM, that user can use all of the IAM permissions granted to the service account attached to the VM. 

## Managing user access

### OS Login

In most scenarios, we recommend using [OS Login](https://docs.cloud.google.com/compute/docs/oslogin). The OS Login feature lets you use Compute Engine IAM roles to manage SSH access to Linux instances. You can add an extra layer of security by [setting up OS Login with two-factor authentication](https://docs.cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication), and manage access at the organization level by [setting up organization policies](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#set-org-policy).

To learn how to enable OS Login, see [Set up OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access).

### Manage SSH keys in metadata

If you are running your own directory service for managing access, or are otherwise unable to set up OS Login, you can manually manage SSH keys in metadata.

**Note:** If you connect to Linux VMs using the Google Cloud console or the Google Cloud CLI, Compute Engine creates SSH keys on your behalf. For more information on how Compute Engine configures and stores keys, see [About SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh).

#### Risks of manual key management

Some of the risks of manual SSH key management include the following:

  * All users who connect to VMs using SSH keys stored in metadata have `sudo` access to VMs.
  * You must keep track of expired keys and delete keys for users who shouldn't have access to your VMs. For example, if a team member leaves your project, you must manually remove their keys from metadata, so they can't continue to access your VMs.
  * Specifying your gcloud CLI or API calls incorrectly can potentially wipe out all of the public SSH keys in your project or on your VMs, which disrupts connections for your project members.
  * Users and service accounts that have the ability to modify project metadata can add SSH keys for all VMs in the project except for VMs that [block project-level SSH keys](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys#block-keys).



If you aren't sure that you want to manage your own keys, [use Compute Engine tools to connect to your instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) instead.

## What's next?

  * Learn how to [set up OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access).
  * Learn how to [create SSH keys](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys).
  * Learn how to [add SSH keys to VMs](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys).
  * Learn how to [restrict SSH keys from VMs](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
