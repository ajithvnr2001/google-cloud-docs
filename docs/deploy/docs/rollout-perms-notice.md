---
url: https://docs.cloud.google.com/deploy/docs/rollout-perms-notice/
title: New permission required for rollbacks \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:51:49.332599+00:00
---

# New permission required for rollbacks  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/rollout-perms-notice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)



Send feedback 

#  New permission required for rollbacks Stay organized with collections  Save and categorize content based on your preferences. 

This document describes a newly required permission, for rollbacks, to be added to Cloud Deploy in 2026.

## What is being added

Starting September 15, 2026, initiating rollbacks through either the Google Cloud console or the Google Cloud CLI will require the `clouddeploy.rollouts.rollback` permission. Before this change, only the `clouddeploy.rollouts.create` permission is required.

This permission already exists, and IAM roles such as `roles/clouddeploy.releaser` and `roles/clouddeploy.operator` already include it. But it's not yet required for rollbacks initiated through the Google Cloud console or the Google Cloud CLI.

## What do I need to do?

Built-in [Cloud Deploy roles](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions) that are relevant for performing rollbacks already have this permission. If you grant only built-in roles for users and service account that perform rollbacks, then you don't need to do anything.

If you have users or service accounts performing rollbacks using Google Cloud console or gcloud CLI, and you're granting them custom roles for this purpose, you must edit those roles, before September 15, 2026, to include the `clouddeploy.rollouts.rollback` permission.

### Find custom roles that need to be updated

Run the following command to find custom roles for your organization that need the `clouddeploy.rollouts.rollback` permission:

###  Project level 

This command finds custom roles, defined in your project, that need the `clouddeploy.rollouts.rollback` permission:
    
    
       gcloud asset search-all-resources \
         --scope=projects/PROJECT_ID \
         --asset-types='iam.googleapis.com/Role' \
         --filter="additionalAttributes.includedPermissions:clouddeploy.rollouts.create AND NOT additionalAttributes.includedPermissions:clouddeploy.rollouts.rollback" \
         --format="table(name, additionalAttributes.includedPermissions)"
    

###  Organization level 

This command finds custom roles in your organization, defined at the organization level, that need `clouddeploy.rollouts.rollback` permission:
    
    
       gcloud asset search-all-resources \
         --scope=organizations/ORG_NUMBER \
         --asset-types='iam.googleapis.com/Role' \
         --filter="additionalAttributes.includedPermissions:clouddeploy.rollouts.create AND NOT additionalAttributes.includedPermissions:clouddeploy.rollouts.rollback" \
         --format="table(name, additionalAttributes.includedPermissions)"
    

### Add the permission to the role

For each custom role you find that needs the new permission added, run the following command:

###  Project level 

This command adds the `clouddeploy.rollouts.rollback` to a custom role that's defined at the project level:
    
    
       gcloud iam roles update CUSTOM_ROLE_ID \
         --project=PROJECT_ID \
         --add-permissions=clouddeploy.rollouts.rollback
    

###  Organization level 

This command adds the `clouddeploy.rollouts.rollback` to a custom role that's defined at the organization level:
    
    
       gcloud iam roles update CUSTOM_ROLE_ID \
         --organization=ORG_NUMBER \
         --add-permissions=clouddeploy.rollouts.rollback
    

See [IAM roles and permissions](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
