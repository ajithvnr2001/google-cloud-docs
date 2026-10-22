---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-tags/
title: Create project tags \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:36.159717+00:00
---

# Create project tags  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create project tags Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This is a Preview feature that is available as-is and is not recommended for production environments. Google provides no Service-Level agreements (SLA) or technical support commitments for Preview features. For more information, see [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).

Tags provide a way to create business attributes for projects to logically organize them. You create tag key-value pairs to provide a mechanism to group projects based on characteristics you define. For example, you can create a tag with the key `ENV` and the value `prod` to indicate the project is in a production environment.

For more information about tags, see [Tags overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-tags).

This document is for IT administrators within the platform administrator group, who are responsible for organizing and managing projects in a Google Distributed Cloud (GDC) air-gapped universe. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

  * To get the permissions that you need to create a tag, ask your Organization IAM Admin to grant you the Tag Admin (`tag-admin`) role.

  * Set an environment variable for the zonal management API server kubeconfig file:
        
        export KUBECONFIG=MANAGEMENT_API_SERVER
        

Replace `MANAGEMENT_API_SERVER` with the path to the kubeconfig file for the zonal management API server. For more information about generating a kubeconfig file for the API server in your targeted zone, see [Zonal management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).

  * Review the following tag key-value pair rules before creating a tag:

    * Tag key names must be unique within a GDC zone.
    * Tag value names can be the same, as long as they're attached to different tag keys.
    * Tag key names must not contain the string `-tv`.
    * Tag value names must not contain the string `tv-`.
    * The following rules apply to both keys and values: 
      * Maximum of 25 characters in length.
      * Contains only letters, numbers, hyphens.
      * Starts with a letter.
      * Must not start with the prefix `g-`, such as `g-project`.
      * Must not contain the string `-tv-`.
      * Must not end with the string `-system`. The `-system` suffix is reserved for tags created by the GDC system.



## Create a tag key-value pair

To create a tag key-value pair, complete the following steps:

  1. Create and apply the `TagKey` custom resource to the `platform` namespace:
         
         kubectl apply -f --kubeconfig ${KUBECONFIG} - <<EOF
         apiVersion: resourcemanager.gdc.goog/v1alpha1
         kind: TagKey
         metadata:
           name: TAG_KEY_NAME
           namespace: platform
         spec: {}
         EOF
         

Replace `TAG_KEY_NAME` with the name of the tag key.

  2. Create and apply the `TagValue` custom resource to the tag key:
         
         kubectl apply -f --kubeconfig ${KUBECONFIG} - <<EOF
         apiVersion: resourcemanager.gdc.goog/v1alpha1
         kind: TagValue
         metadata:
           name: TAG_VALUE_NAME
           namespace: g-t-TAG_KEY_NAME
         spec: {}
         EOF
         

Replace the following:

     * `TAG_VALUE_NAME`: the name of the tag value.
     * `TAG_KEY_NAME`: the name of the tag key you created in the previous step. The namespace for the tag value must be set to the system-created tag key management namespace.
  3. Verify the new tag key is available:
         
         kubectl get tagkey TAG_KEY_NAME \
             --kubeconfig ${KUBECONFIG} \
             --namespace platform
         

The output is similar to the following:
         
         NAME          AGE
           my-tagkey     5m
         

  4. Verify the new tag value is available:
         
         kubectl get tagvalue TAG_VALUE_NAME \
             --kubeconfig ${KUBECONFIG} \
             --namespace g-t-TAG_KEY_NAME
         

The output is similar to the following:
         
         NAME          AGE
           my-tagvalue   6m
         




After you create a tag key-value pair, you must [add it to a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/add-remove-tags#add-tags) for the tag to take effect.

## What's next

  * [Manage project tags](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-tags)
  * [Design access boundaries between resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries)
  * [Design permissioning setup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/permissions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
