---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/add-remove-tags/
title: Add and remove tags \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:41.494866+00:00
---

# Add and remove tags  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/add-remove-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Add and remove tags Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This is a Preview feature that is available as-is and is not recommended for production environments. Google provides no Service-Level agreements (SLA) or technical support commitments for Preview features. For more information, see [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).

Tags provide a way to create business attributes for projects to logically organize them. You add and remove tag key-value pairs to group and ungroup projects based on the changing structure of your project hierarchy.

For more information about tags, see [Tags overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-tags).

This document is for IT administrators within the platform administrator group, who are responsible for organizing projects based on existing tag key-value pairs in a GDC universe. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

  * To get the permissions that you need to add a tag to a project and to remove a tag from a project, ask your IAM Org Admin to grant you the following roles:

    * TagKey User (`tagkey-user`)
    * TagValue User (`tagvalue-user`)
    * Project Editor (`project-editor`)
  * Set an environment variable for the zonal management API server kubeconfig file:
        
        export KUBECONFIG=MANAGEMENT_API_SERVER
        

Replace `MANAGEMENT_API_SERVER` with the path to the kubeconfig file for the zonal management API server. For more information about generating a kubeconfig file for the API server in your targeted zone, see [Zonal management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).

  * Confirm you [created a tag key-value pair](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-tags).




## Add tags to a project

To add a tag to your project, you must bind an existing tag key-value pair that's available in the `platform` namespace to your project.

  1. Bind the tag key-value pair to your project:
         
         kubectl label project PROJECT_NAME \
             --kubeconfig ${KUBECONFIG} \
             --namespace platform \
             tag.resourcemanager.gdc.goog/TAG_KEY_NAME=TAG_VALUE_NAME
         

Replace the following:

     * `PROJECT_NAME`: the name of your project to bind the tag key-value pair to.
     * `TAG_KEY_NAME`: the name of the tag key. The namespace for the tag value must be set to the system-created tag key management namespace.
     * `TAG_VALUE_NAME`: the name of the tag value.
  2. Verify the tag key-value pair binding is available in your project:
         
         kubectl get project --kubeconfig ${KUBECONFIG} \
             --namespace platform \
             --label tag.resourcemanager.gdc.goog/TAG_KEY_NAME=TAG_VALUE_NAME
         

The output is similar to the following:
         
         NAME           AGE
         my-project     23m
         




## Remove tags from a project

To remove a tag from your project, you must remove the tag key label from the project:

  * Remove the tag key label from the project:
        
        kubectl label project PROJECT_NAME \
            --kubeconfig ${KUBECONFIG} \
            --namespace platform \
            tag.resourcemanager.gdc.goog/TAG_KEY_NAME-
        

Replace the following:

    * `PROJECT_NAME`: the name of the project.
    * `TAG_KEY_NAME`: the name of the tag key to remove from the project.

The output is similar to the following:
    
    project.resourcemanager.gdc.goog/my-project unlabeled
    




## What's next

  * [Manage project tags](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-tags)
  * [Delete project tags](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-tags)
  * [Design permissioning setup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/permissions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
