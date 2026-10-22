---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/packer/
title: Build custom images with Packer \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:23.933391+00:00
---

# Build custom images with Packer  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/packer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Build custom images with Packer Stay organized with collections  Save and categorize content based on your preferences. 

The `packer` module lets you build custom virtual machine (VM) images in your Cluster Toolkit deployments.

By using this module, you can automate the creation of standardized boot disks, which helps to improve consistency and saves time across your cluster environments. The module provisions a short-lived Compute Engine instance in Google Cloud, runs customization scripts, and saves the resulting boot disk for repeated use. By default, the module uses the [high performance computing (HPC) VM image](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm) as the source image for the boot disk.

To customize the image, you can use one or more of the following approaches:

  * **[Metadata startup scripts](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux)** : Provide a raw string or a file.
  * **Shell scripts** : Upload scripts from the [Packer](https://www.packer.io/) execution environment to the compute instance by using the [`shell_scripts`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_shell_scripts) field.
  * **Ansible playbooks** : Upload playbooks from the Packer execution environment to the compute instance by using the [`ansible_playbooks`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_ansible_playbooks) field.



If you don't supply any scripts, then the module copies the source boot disk to your project without customization. This approach is useful if you require increased control over the image maintenance lifecycle, or if organizational policies restrict the use of images to internal projects.

For the complete list of inputs and outputs for this module, see the [`packer` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `packer` module, see the [`examples/image-builder.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/image-builder.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `packer` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select software or resource** menu and then select **Packer**.
  * The `packer` module does not create a continuous long-running workload or a full cluster. It provisions a short-lived compute instance to execute customization scripts, and it generates a customized boot disk image for repeated use.



### Network access requirements

To build custom images successfully, your network must support specific access requirements:

  * **Outbound internet access:** Most customization scripts require access to resources on the public internet. You can provide this access by using one of the following methods:

    * **Public IP address:** Assign a public IP address to the compute instance by setting the [`omit_external_ip`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_omit_external_ip) variable to the `false` value.
    * **Cloud NAT:** Configure a VPC network with a [Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/overview) in the same region as the compute instance. You can use the [`vpc` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/vpc) to automate the NAT creation.
  * **Inbound SSH access:** Depending on your customization solution, Packer might require inbound Secure Shell (SSH) access to the compute instance from the execution environment. If your environment restricts SSH access, then you must use the metadata-based startup script solution. To authorize inbound SSH access, you can use the [`vpc` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/vpc) and set the `allowed_ssh_ip_ranges` variable to the `0.0.0.0/0` value.




### Required roles

To get the permissions that you need to build custom images by using Packer, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [IAP-secured Tunnel User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelResourceAccessor) (`roles/iap.tunnelResourceAccessor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** If you set the [`use_iap`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_use_iap) variable to the `true` value, then the account must have the IAP-secured Tunnel User role.

To ensure that the compute instance service account has the necessary permissions to customize the temporary build compute instance, ask your administrator to grant the following IAM roles to the compute instance service account on your project: 

**Important:** You must grant these roles to the compute instance service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`)
  * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`)
  * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the compute instance service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Scripting approaches and execution

When you customize the image, the module executes the different scripting methods in the following order:

  1. The module executes all shell scripts in the order that you configure them.
  2. After the shell scripts finish running, the module executes all Ansible playbooks in the order that you configure them.



The metadata startup script executes in parallel with the shell scripts and Ansible playbooks. If you specify both the [`startup_script`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_startup_script) field and the [`startup_script_file`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_startup_script_file) field, then the `startup_script_file` field takes precedence.

### Recommended scripting strategies

Because the metadata startup script executes in parallel with the other methods, conflicts can occur, particularly when package managers lock their databases during installation. To avoid these conflicts, we recommend that you choose only one of the following approaches:

  * **Startup scripts:** specify either the [`startup_script`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_startup_script) field or the [`startup_script_file`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_startup_script_file) field. Don't specify the `shell_scripts` field or the `ansible_playbooks` field. This approach is especially useful in environments that restrict SSH access.
  * **Shell scripts and Ansible playbooks:** specify any combination of the [`shell_scripts`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_shell_scripts) field and the [`ansible_playbooks`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_ansible_playbooks) field. Don't specify the `startup_script` field or the `startup_script_file` field.



If any startup script approach fails and returns a non-zero exit code, then Packer determines that the build failed and doesn't save the image.

## SSH access considerations

Your choice of scripting strategy directly impacts your SSH configuration requirements.

### External access with SSH

The shell scripts and Ansible playbooks customization solutions both require SSH access to the compute instance from the Packer execution environment. You can authorize SSH access by using one of the following methods:

  1. **IAP tunnels (Recommended):** create the compute instance without a public IP address and use [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) to create SSH tunnels. To use this method, retain the [`use_iap`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_use_iap) field at its default `true` value.
  2. **Public IP address:** create the compute instance with a public IP address and configure firewall rules to authorize SSH access from the Packer execution environment. To use this method, set the [`omit_external_ip`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_omit_external_ip) field to the `false` value and add the necessary firewall rules.



The Packer template defaults to the IAP-based solution because it prevents exposure to the public internet. The IAP-based solution also uses a `vpc` module that automatically provisions the necessary firewall rules for SSH tunneling and outbound-only access through Cloud NAT.

In either SSH solution, you supply your customization scripts as files in the `shell_scripts` field and the `ansible_playbooks` field.

### Configure environments that restrict SSH access

Many network environments restrict SSH access to compute instances entirely. In these environments, you must use metadata-based startup scripts because they execute independently of the Packer execution environment.

To use this approach, provide a single script as a string to the [`startup_script`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_startup_script) field. This solution integrates with Cluster Toolkit runners, which operate by using a single startup script that downloads and executes additional runners from Cloud Storage.

**Note:** Packer attempts to use SSH if you populate either the `shell_scripts` field or the `ansible_playbooks` field. Keep these fields at their default empty values to help ensure that the module disables SSH access.

## Example configurations

The following sections provide examples that demonstrate how to configure the `packer` module.

### Use the image builder blueprint

We recommend that you use the Terraform-based [`startup-script` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/startup-script) alongside this `packer` module to build images.

The [`examples/image-builder.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/image-builder.yaml) file demonstrates this pattern. This example blueprint builds the following resources:

  * An image by using the HPC VM image as a base
  * A VPC network with firewall rules that authorize IAP-based SSH tunnels
  * A Cluster Toolkit runner that installs a custom script



### Supply a startup script as a string

The [`startup_script`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_startup_script) field accepts scripts that are formatted as strings. You can specify multi-line strings by using [here document syntax](https://en.wikipedia.org/wiki/Here_document) in your [input Packer variables file](https://www.packer.io/guides/hcl/variables#from-a-file) (`*.pkrvars.hcl`).

In a blueprint, the syntax resembles the following example. The script installs packages, and the module sets the [`disk_size`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#input_disk_size) to 100 GiB.
    
    
    ...
        settings:
          startup_script: |
            #!/bin/bash
            yum install -y epel-release
            yum install -y jq
          disk_size: 100
    ...
    

## Monitor startup script execution

When you customize the startup script, Packer prints limited output to the terminal. The output resembles the following example:
    
    
    example.googlecompute.toolkit_image: Waiting for any running startup script to finish...
    example.googlecompute.toolkit_image: Startup script not finished yet. Waiting...
    example.googlecompute.toolkit_image: Startup script not finished yet. Waiting...
    example.googlecompute.toolkit_image: Startup script, if any, has finished running.
    

If the Packer image build fails, then the module outputs a `gcloud` command. To review the startup script execution logs and debug the failure, use the provided `gcloud` command.

**Note:** Log propagation from the compute instance to [Cloud Logging](https://console.cloud.google.com/logs/) can experience delays. You might need to wait a few minutes to view the complete logs.

## What's next

  * For the complete list of inputs and outputs for this module, see the [`packer` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/packer/custom-image/README.md#inputs) page in the Cluster Toolkit GitHub repository.
  * For a complete list of supported modules, see the [compatibility matrix](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/network_storage.md#compatibility-matrix) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
