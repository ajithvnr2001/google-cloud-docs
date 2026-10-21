---
url: https://docs.cloud.google.com/migrate/containers/docs/mcdc-aws-collection-tutorial/
title: Collect guest data from EC2 VMs for offline assessment \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:47:03.497085+00:00
---

# Collect guest data from EC2 VMs for offline assessment  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/mcdc-aws-collection-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback 

#  Collect guest data from EC2 VMs for offline assessment Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial walks you through the process of discovering and collecting data on EC2 virtual machine (VM) instances, to be used for offline technical assessment using the Migration Center discovery client CLI.

## Objectives

In this tutorial, you will learn how to:

  * Download the `mcdc` CLI to assess your AWS EC2 VMs.
  * Perform AWS EC2 inventory discovery.
  * Collect guest-level information on all the VMs in an EC2 region using AWS Session Manager or SSH.
  * Generate an offline assessment report.
  * (Advanced) Modify the scripts to suit your needs.
  * (Advanced) Write an orchestration script from scratch.



## Costs

This tutorial incurs no Google Cloud costs.

It is unlikely to impact your AWS costs.

## Before you begin

The prerequisites depend on which way you connect to your EC2 VMs.

###  Session Manager 

  1. Prepare a Linux machine to download and run the `mcdc` CLI. The Linux machine must have the following minimum requirements:

     * Linux kernel versions 2.6.23 or later
     * 4 GB RAM and 10 GB disk space
     * AWS CLI installed
  2. Ensure that the AWS CLI has the following permissions:

     * Can call `aws ssm describe-instance-information`
     * Can call `aws ssm start-session`



###  SSH 

  1. Prepare a Linux machine to download and run the `mcdc` CLI. The Linux machine must satisfy the following minimum requirements:

     * Linux kernel versions 2.6.23 or later
     * 4 GB RAM and 10 GB disk space
     * AWS CLI installed
     * Network connectivity to EC2 instances (possibly through a proxy)
  2. Ensure that the AWS CLI has the following permissions:

     * Can call `aws ec2 describe-instances`
     * [Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html#ec2-instance-connect-configure-IAM-role)



## Download the `mcdc` CLI

  1. Connect to the Linux machine: 
         
         ssh MACHINE_IP

Replace MACHINE_IP with the IP address of your Linux machine.

  2. Download the latest version of the `mcdc` CLI and make it executable: 
         
         curl -O "https://mc-release.storage.googleapis.com/mcdc/$(curl -s https://mc-release.storage.googleapis.com/mcdc/latest)/mcdc"
           chmod +x mcdc

  3. Add the `mcdc` CLI to your shell path: 
         
         PATH=$PATH:`pwd`




## Perform an AWS inventory discovery

  * Run the inventory discovery:
        
        ./mcdc discover aws -r REGION
        

Replace REGION with the region of your EC2 VMs.

The `mcdc` CLI prompts you for your [access key ID and secret access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

The output of the discover command looks similar to the following:
        
        Collected 166 VMs
        [✓] Collection completed.
        




## Perform guest discovery

You can perform guest discovery using Session Manager or SSH.

###  Session Manager 

This method uses the [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) to perform guest discovery on all VMs with the [SSM agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) installed. The SSM agent is installed by default on most Amazon provided AMIs, and can be manually installed on others.

  1. Ensure that all VMs have an IAM role which allows connecting using Session Manager. For more information, see the [AWS documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-instance-profile.html).

  2. Ensure all VMs you want to collect are turned on.

  3. Run guest discovery using the [ssm guest collection script](https://github.com/GoogleCloudPlatform/migrate-to-containers/blob/main/scripts/mcdc/mcdc_collect_aws_guest_ssm.sh) from the Migrate to Containers repository on GitHub.

a. Download the script:
         
         curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/migrate-to-containers/main/scripts/mcdc/mcdc_collect_aws_guest_ssm.sh
          chmod +x mcdc_collect_aws_guest_ssm.sh
         

b. Run the script and save the output to a file:
         
         ./mcdc_collect_aws_guest_ssm.sh --region REGION
         

Replace REGION with the region of your EC2 VMs.

All flags are passed directly to `aws ssm describe-instance-information`. To collect from a specific VM, run the following command:
         
         ./mcdc_collect_aws_guest_ssm.sh --region REGION --filters "Key=InstanceIds,Values=VM_ID"
         

Replace VM_ID with the VM ID.

For more information about all the flags allowed for the `describe-instance-information` command, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-instance-information.html).




###  SSH 

This method uses SSH to perform guest discovery on Linux VMs. It connects to the [public IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses) of each VM. However, it should be straightforward to modify the script. For example, to connect to the [private IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-private-addresses).

The script uses [EC2 instance connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html) for authentication. Instance connect is only available on Amazon Linux and Ubuntu VMs, and [may require installation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html#ec2-instance-connect-install). However, it should be straightforward to adjust the script to use an alternative authentication method, such as password authentication using [sshpass](https://linux.die.net/man/1/sshpass), or a private key.

  1. Ensure that you have network access to the VMs. You may need to [adjust the inbound rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html#add-rule-authorize-access) for your security groups, or use a proxy to connect.

  2. Ensure that all VMs you want to collect from are turned on.

  3. Run guest discovery using the [ssh guest collection script](https://github.com/GoogleCloudPlatform/migrate-to-containers/blob/main/scripts/mcdc/mcdc_collect_aws_guest_ssh.sh) from the Migrate to Containers repository on GitHub.

     1. Download the script:
            
            curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/migrate-to-containers/main/scripts/mcdc/mcdc_collect_aws_guest_ssh.sh
            chmod +x mcdc_collect_aws_guest_ssh.sh
            

     2. Run the script and save the output to a file:
            
            ./mcdc_collect_aws_guest_ssh.sh --region REGION
            

Replace REGION with the region of your EC2 VMs.

Any flag named `-a` or `--ssh-arg` is passed directly to SSH. To disable strict host key authentication, run the following command:
            
            ./mcdc_collect_aws_guest_ssh.sh --region REGION -a '-o StrictHostKeyChecking=no'
            

All other flags are passed directly to `aws ssh describe-instances`. To collect from a specific VM, run the following command:
            
            ./mcdc_collect_aws_guest_ssm.sh --region REGION --instance-ids VM_ID
            

Replace VM_ID with the VM ID.

To learn about all the allowed flags, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html).

It is possible to use a proxy to connect to an VM using SSH `ProxyCommand` option. For example to use an existing socks5 proxy on port PROXY_PORT, run the following command:
            
            ./mcdc_collect_aws_guest_ssh.sh --region REGION -a '-o ProxyCommand=nc -X 5 -x 127.0.0.1:PROXY_PORT %h %p'
            

Replace PROXY_PORT with the port number.

  4. If you adjusted the inbound rules in step 1, then consider reverting your changes.




## Generate an offline assessment report

  * After all the data is collected, you can produce a detailed HTML report:
        
        ./mcdc report --format html --full > REPORT_NAME.html
         




## (Advanced) Modify the scripts to suit your needs

It is possible that neither of the scripts exactly suit your needs. For example, you might not have either the SSM agent, or instance connect, installed on some of your VMs.

In such cases, you usually have a standard way of connecting to your machines. We recommend that you write scripts which allow you to orchestrate these methods at scale. In some cases you may need to write these scripts from scratch, but in others you may be able to modify the existing scripts.

For example, you can modify the [SSH collect script](https://github.com/GoogleCloudPlatform/migrate-to-containers/blob/main/scripts/mcdc/mcdc_collect_aws_guest_ssh.sh) to use private instead of public IP addresses.

The scripts are heavily commented to make them easy to understand.

## (Advanced) Write an orchestration script from scratch

To orchestrate guest discovery and data collection at scale, do the following:

  1. Identify all VMs you want to collect from.
  2. Upload the guest collection script to each VM. Linux and Windows VMS require different guest collection scripts.
  3. Run the guest collection script on each VM.
  4. Download the created artifact from each VM.
  5. Import the downloaded guest collection script into the `mcdc` CLI.



While you may often have to write much of this from scratch, there are some useful building blocks in the example scripts which may be able to help you with some of these tasks. For example:

  * [Iterating over all VMs in EC2](https://github.com/GoogleCloudPlatform/migrate-to-containers/blob/main/scripts/mcdc/mcdc_collect_aws_guest_ssh.sh#L37).
  * Downloading the [Windows](https://github.com/GoogleCloudPlatform/migrate-to-containers/blob/main/scripts/mcdc/mcdc_collect_aws_guest_ssm.sh#L18) and [Linux](https://github.com/GoogleCloudPlatform/migrate-to-containers/blob/main/scripts/mcdc/mcdc_collect_aws_guest_ssm.sh#L1-L3) guest collection scripts.
  * Sometimes you won't be able to upload and download files. In such cases it is possible to include the collect scripts in the sent commands, and write the base64 encoded artifacts to stdout. The [SSM collect script](https://github.com/GoogleCloudPlatform/migrate-to-containers/blob/main/scripts/mcdc/mcdc_collect_aws_guest_ssm.sh) may serve as a useful example of how to do this.
  * [Importing the collected artifact to the `mcdc` CLI](https://github.com/GoogleCloudPlatform/migrate-to-containers/blob/main/scripts/mcdc/mcdc_collect_aws_guest_ssm.sh#L93).



## What's next

  * Learn more about the [`mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/discovery-client-cli-overview).
  * Look [through scripts samples](https://github.com/GoogleCloudPlatform/migrate-to-containers/tree/main/scripts/mcdc).
  * To learn how to migrate a more complex application, see the [Migrating a Spring framework application tutorial](https://github.com/GoogleCloudPlatform/migrate-to-containers/tree/main/guides/petclinic) available in the Migrate to Containers GitHub repository.
  * Learn about the [planning best practices](https://docs.cloud.google.com/migrate/containers/docs/planning-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
