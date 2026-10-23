---
url: https://docs.cloud.google.com/filestore/docs/managing-labels/
title: Managing labels \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:43.980191+00:00
---

# Managing labels  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/managing-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Managing labels Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use [labels](https://docs.cloud.google.com/filestore/docs/tags-and-labels#labels) with your Filestore instances. Labels let you group related instances and store metadata about an instance.

## Adding or updating an instance's labels

You can add labels to a Filestore instance when you [create the instance](https://docs.cloud.google.com/filestore/docs/creating-instances). After an instance is created, you can add more labels to the instance, as well as update or delete existing labels.

###  Console 

  1. In the Google Cloud console, go to the Filestore Instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Select the checkbox next to each instance whose labels you want to modify.

  3. Click **Show info panel**.

  4. Add and update labels as needed:

Operation | Instructions  
---|---  
Add a label | Click **Add label** and type the key and value for the label.  
Update a label | Update the **Value** field. You cannot update the **Key** of an existing label.  
Delete a label | Click **Delete item** _delete_ next to the label.  
  5. Click **Save** to save your changes once you are finished with your updates.




###  gcloud 

You can edit the labels of a Filestore instance's by running the [`instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/update) command. To add new labels or change the values of existing labels, use the `--update-labels` flag. To delete one or more labels, use the `--remove-labels` flag. The `--clear-labels` flag removes all labels from an instance.
    
    
    gcloud filestore instances update instance-id \
        --project=project-id \
        --zone=zone \
        --update-labels key=value,[key=value,…] \
        --remove-labels key,[key,…] \
        --clear-labels
    

where:

  * instance-id is the instance ID of the instance you want to edit.
  * project-id is the project ID of the Google Cloud project that contains the Filestore instance. You can skip this flag if the Filestore instance is in the `gcloud` default project. You can set the default project by running:
        
        gcloud config set project project-id
        

  * zone is the zone where the Filestore instance resides. Run the [`gcloud filestore zones list`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/zones/list) command to get a list of supported zones. You can skip this flag if the Filestore instance is in the `gcloud` default zone. You can set the default zone by running:
        
        gcloud config set filestore/zone zone
        

  * key is a new label, or an existing label you want to change or remove.

  * value is the value for a label.




#### Example

The following example updates the nfs-server instance by adding the **status** label, updating the **dept** label value, and removing the **admin** label.
    
    
    gcloud filestore instances update nfs-server \
        --project=myproject \
        --zone=us-central1-c \
        --update-labels status=active \
        --update-labels dept=accounting \
        --remove-labels admin
    

## What's next

Learn how to [edit other properties of a Filestore instance](https://docs.cloud.google.com/filestore/docs/editing-instances).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
