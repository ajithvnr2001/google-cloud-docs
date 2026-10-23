---
url: https://docs.cloud.google.com/bare-metal/docs/bms-ssh-keys/
title: Set up SSH keys for a server \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:41.767561+00:00
---

# Set up SSH keys for a server  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-ssh-keys/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up SSH keys for a server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can set up SSH keys for your Bare Metal Solution server.

It's optional to set up SSH keys. You can set them while provisioning a new server or while reimaging an existing one.

This feature is available only for the [Linux OSes supported by Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs/bms-planning#linux).

## Before you begin

  1. Create SSH keys.

Before initiating the server provisioning process, you must have the SSH keys. The public SSH keys that you provide are used as the authorized keys to log in to your Bare Metal Solution server.

You must create the Cloud KMS key in the same project that contains your Bare Metal Solution server.

If you choose to use SSH keys, you need at least one public SSH key. The public key must have an `ssh-rsa` type signature:
         
         ssh-rsa public_key optional comment
         

To learn how to create SSH keys, see [Create SSH keys](https://docs.cloud.google.com/bare-metal/docs/troubleshooting/configure-serial-console#generate-ssh-key).

To learn how to manage your SSH keys, see [Manage SSH keys](https://docs.cloud.google.com/bare-metal/docs/troubleshooting/configure-serial-console#manage-ssh-keys).

  2. In the project that contains your Bare Metal Solution server, register your SSH keys. Follow the steps in [Register the SSH keys](https://docs.cloud.google.com/bare-metal/docs/troubleshooting/configure-serial-console#register-ssh-key).




## Set up SSH keys while provisioning a server

You can set up SSH keys for a new Bare Metal Solution server while provisioning it through the [Google Cloud console intake form](https://docs.cloud.google.com/bare-metal/docs/bms-deploy#use_the_console_intake_form_to_enter_your_selections).

You can only select the SSH keys that exist in the same project as that of your server.

To set up SSH keys while provisioning a server, see [Use the Google Cloud console intake form to enter your selections](https://docs.cloud.google.com/bare-metal/docs/bms-deploy#use_the_console_intake_form_to_enter_your_selections).

## Set up SSH keys while reimaging a server

To set up SSH keys while reimaging a server, see [Change the OS for a server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#change-os-for-server).

## View SSH keys of a server

To view SSH keys of a server, follow these steps:

###  Console 

  1. Go to the **Servers** page.

[Go to Servers](https://console.cloud.google.com/compute/bareMetalSolution/servers)

  2. Click the server name.

On the **Server details** page, view the SSH keys in **SSH keys** field.




###  gcloud 

Use the `gcloud alpha bms instances auth-info` command:
    
    
    gcloud alpha bms instances auth-info SERVER_NAME --project=PROJECT_ID --region=REGION
    

Replace the following:

  * SERVER_NAME: The name of the Bare Metal Solution server.
  * PROJECT_ID: The ID of the project.
  * REGION: The location of the Bare Metal Solution server.



## Access a server using the SSH keys

SSH keys are associated with the `customeradmin` user. Therefore, while logging in through SSH, use `customeradmin` as the username.

To learn how to log in to your Bare Metal Solution server, see [Logging in to a Bare Metal Solution server for the first time](https://docs.cloud.google.com/bare-metal/docs/bms-setup#bms-first-logon).

## What's next

  * [Operate your Bare Metal Solution server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#operate_a_server).
  * [Check the status of a server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#check_the_status_of_a_server).
  * [Manage servers](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#manage_servers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
