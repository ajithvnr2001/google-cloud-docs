---
url: https://docs.cloud.google.com/oracle/database/docs/generate-ssh-keys/
title: Generate SSH keys \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:10.458101+00:00
---

# Generate SSH keys  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/generate-ssh-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Generate SSH keys Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to generate SSH keys for your Oracle Database@Google Cloud resources.

To authenticate your Oracle Database@Google Cloud connection, you need to generate an SSH key pair. You need to create an SSH key pair at least once in your project. You can reuse the same key pair for multiple Exadata VM Clusters or create a new key pair for each Exadata VM Cluster. You can generate an SSH key pair using the `ssh-keygen` command.

## Generate an SSH key pair

To generate an SSH key pair, run the following command:
    
    
    ssh-keygen -b 4096 -f SSH_KEY_ID -N PASSPHRASE -t rsa
    

Replace the following:

  * SSH_KEY_ID: this is the root name of your SSH key file used to generate the public and private keys
  * PASSPHRASE: this is the passphrase used when accessing your resources using Google Cloud console



The `ssh-keygen` command saves your private key to a file called SSH_KEY_ID and your public key to a file called SSH_KEY_ID.pub in your home directory.

## What's next

  * [Configure a VPC network](https://docs.cloud.google.com/oracle/database/docs/configure-vpc) for your resources.
  * [Create a Exadata VM Cluster](https://docs.cloud.google.com/oracle/database/docs/create-clusters).
  * [Learn more about Oracle Database@Google Cloud](https://docs.cloud.google.com/oracle/database/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
