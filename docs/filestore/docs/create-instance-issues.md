---
url: https://docs.cloud.google.com/filestore/docs/create-instance-issues/
title: Troubleshoot instance creation \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:10.280839+00:00
---

# Troubleshoot instance creation  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/create-instance-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Troubleshoot instance creation Stay organized with collections  Save and categorize content based on your preferences. 

This page provides troubleshooting information to help address issues you might encounter while attempting to create a Filestore instance.

## `PERMISSION DENIED` when creating a Filestore instance

  1. Check if the Filestore API is enabled:
         
         gcloud services enable file.googleapis.com
         

  2. Each Filestore instance must have an IP address range associated with it that does not overlap with another range in use. For a detailed list of restrictions, see [Configuring a reserved IP address range](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_a_reserved_ip_address_range).

  3. Check if you have the `roles/file.editor` role. For details see [Access control](https://docs.cloud.google.com/filestore/docs/access-control) or [IAM roles and permissions](https://docs.cloud.google.com/filestore/docs/iam).

  4. If you are still encountering the error, then the Filestore [service account](https://docs.cloud.google.com/iam/docs/service-accounts) might have had its `file.serviceAgent` role removed. To check if this is the case, run:
         
         gcloud projects get-iam-policy project-id-or-number \
                 --flatten="bindings[].members" \
                 --format='table(bindings.role)' \
                 --filter="bindings.members:service-project-number@cloud-filer.iam.gserviceaccount.com"
         

where:

     * project-id-or-number is the ID or number of your Google Cloud project.
     * project-number is the number of your Google Cloud project.

The command should return something similar to the following:
    
    ROLE
    roles/file.serviceAgent
    

If `roles/file.serviceAgent` is not listed, you can restore it by running:
    
    gcloud projects add-iam-policy-binding project-id-or-number  \
          --member serviceAccount:service-project-number@cloud-filer.iam.gserviceaccount.com  \
          --role roles/file.serviceAgent
    




## `System limit for internal resources has been reached` error when creating an instance

This error is caused by Filestore reaching an internal network quota. For every VPC network that you create a Filestore instance on, Filestore must create an [internal network](https://docs.cloud.google.com/filestore/docs/networking#connectivity) that peers with that network. These internal networks are preserved even when the Filestore instances and VPC networks associated with them are deleted.

Once the number of internal networks reaches 49 for a project, Filestore is no longer able to create new internal networks, which prevents you from creating Filestore instances on new VPC networks. Attempting to do so results in one of the following errors:

`System limit for internal resources has been reached. Please request to adjust limit here: https://forms.gle/PFPJ2QD4KnCHzYEx9`

You can clear the internal networks by disabling and then re-enabling the Filestore API.

**Important:** Before you can disable the API, you must delete all Filestore related resources, such as Filestore instances and backups.**Caution:** Disabling the Filestore API removes previously granted quota increase requests.

Use the [`gcloud services disable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/disable) command to disable the Filestore API:
    
    
    gcloud services disable file.googleapis.com
    

Then, use the [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command to re-enable the Filestore API:
    
    
    gcloud services enable file.googleapis.com
    

If you can't disable the API because you have Filestore instances that you cannot delete or you don't want to lose quota that you've been granted through quota increase requests, then you can fill out the following form to have your network limits adjusted:
    
    
    https://forms.gle/PFPJ2QD4KnCHzYEx9
    

If you need to regularly delete and create VPC networks and Filestore instances, there are two ways to avoid running out of network quota:

  * When you create a VPC network, use the same name as a previous network that's been used for Filestore instance creation.

  * Cycle through a pool of no more than 49 VPC networks instead of deleting and then recreating them.




## What's next

  * [Known issues](https://docs.cloud.google.com/filestore/docs/known-issues)
  * [Troubleshoot slow performance](https://docs.cloud.google.com/filestore/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
