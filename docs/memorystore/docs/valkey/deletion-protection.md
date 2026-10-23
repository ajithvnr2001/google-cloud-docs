---
url: https://docs.cloud.google.com/memorystore/docs/valkey/deletion-protection/
title: Prevent deletion of an instance \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:31.960401+00:00
---

# Prevent deletion of an instance  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/deletion-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Prevent deletion of an instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to protect Memorystore for Valkey instances from accidental deletion.

## Overview

Instance deletion protection lets you prevent the accidental removal of existing and new instances. Using instance deletion protection, you can safeguard instances that are important to your applications and services.

You can set the deletion protection option when you create an instance. Additionally, you can set this option on an existing instance. In both cases, deletion is prevented at the instance level. By default, the deletion protection option is disabled unless you use Terraform to create an instance.

## Plan for deletion protection

If you are planning to create an instance, decide whether you want to protect the new instance from accidental deletion. For example, a critical instance should be protected in this way.

Also consider whether there are existing instances you want to protect from accidental deletion. If you have multiple instances to protect, set the option on each instance.

### Plan to delete an instance

If you are planning to delete an instance, first do the following:

  * Confirm that it is safe to delete the instance
  * Confirm that deletion protection is disabled; if necessary, edit the instance to disable deletion protection



### Limitations of deletion protection

Deletion protection on an instance does not prevent:

  * Editing the instance
  * Suspending the instance due to billing issues
  * Deleting the suspended instance due to billing issues
  * Deleting the instance due to a project deletion



## Required permissions

To set deletion protection on an instance, you must have the `memorystore.instances.update` permission.

## Set deletion protection on a new instance

The following are the ways to set the deletion protection option. By default, the deletion protection option is disabled unless you use Terraform to create an instance.

If deletion protection is enabled, an attempt to delete the instance fails.

### gcloud

To turn on deletion protection while creating an instance, follow the instructions at [Create a multi-zone instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances#gcloud) and add the following flag:
    
    
    gcloud memorystore instances create INSTANCE \
      --deletion-protection-enabled \
      --location=REGION_ID \
    

Replace the following:

  * INSTANCE is the ID of your instance.
  * REGION_ID is the region where your instance is located.



## Set or remove deletion protection on an existing instance

The following are the ways to edit an instance for deletion protection. If you enable the option, a subsequent attempt to delete the instance fails.

### gcloud

To enable deletion protection for an existing instance, use a command similar to the following:
    
    
    gcloud memorystore instances update INSTANCE \
      --deletion-protection-enabled \
      --location=REGION_ID \
    

To disable deletion protection for an existing instance, use a command similar to the following:
    
    
    gcloud memorystore instances update INSTANCE \
      --no-deletion-protection-enabled \
      --location=REGION_ID \
    

Replace the following:

  * INSTANCE is the ID of the your instance.
  * REGION_ID is the region where your instance is located.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
