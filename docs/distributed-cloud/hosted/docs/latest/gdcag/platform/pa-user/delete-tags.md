---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-tags/
title: Delete project tags \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:32:59.554715+00:00
---

# Delete project tags  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Delete project tags Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This is a Preview feature that is available as-is and is not recommended for production environments. Google provides no Service-Level agreements (SLA) or technical support commitments for Preview features. For more information, see [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).

This document explains how to delete a tag from Google Distributed Cloud (GDC) air-gapped if you no longer need it for organizing projects. You can delete a tag as long as it's not attached to any projects.

For more information about tags, see [Tags overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-tags).

This document is for IT administrators within the platform administrator group, who are responsible for organizing and managing projects in a GDC universe. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

  * To get the permissions that you need to delete a tag from GDC, ask your Organization IAM Admin to grant you the Tag Admin (`tag-admin`) role.

  * Set an environment variable for the zonal management API server kubeconfig file:
        
        export KUBECONFIG=MANAGEMENT_API_SERVER
        

Replace `MANAGEMENT_API_SERVER` with the path to the kubeconfig file for the zonal management API server. For more information about generating a kubeconfig file for the API server in your targeted zone, see [Zonal management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).

  * Make sure that you've already [removed the tag from all projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/add-remove-tags#remove-tags). You cannot delete a tag key-value pair that is still attached to a project.




## Delete a tag key-value pair

  1. Delete the tag value:
         
         kubectl delete tagvalue TAG_VALUE_NAME \
             --kubeconfig ${KUBECONFIG} \
             --namespace g-t-TAG_KEY_NAME
         

Replace the following:

     * `TAG_VALUE_NAME`: the name of the tag value to delete.
     * `TAG_KEY_NAME`: the name of the tag key paired with the tag value. The namespace for the tag value must be set to the system-created tag key management namespace.

You must delete the tag value before deleting the corresponding tag key.

  2. Delete the tag key:
         
         kubectl delete tagkey TAG_KEY_NAME \
             --kubeconfig ${KUBECONFIG} \
             --namespace platform
         

Replace `TAG_KEY_NAME` with the name of the tag key to delete.

  3. Verify the tag key-value pair is deleted:
         
         kubectl get tagkey TAG_KEY_NAME \
             --kubeconfig ${KUBECONFIG} \
             --namespace platform
         kubectl get tagvalue TAG_VALUE_NAME \
             --kubeconfig ${KUBECONFIG} \
             --namespace g-t-TAG_KEY_NAME
         

The output must not return your tag key or tag value.




## What's next

  * [Delete a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-a-project)
  * [Configure organization policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-policy)
  * [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
