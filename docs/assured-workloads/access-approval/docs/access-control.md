---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Access Approval \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:22.941277+00:00
---

# Access control with IAM  |  Access Approval  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access control with IAM

This page describes the Identity and Access Management (IAM) roles required to use Access Approval.

## Required roles

The following sections mention the IAM roles and permissions required to perform various actions with Access Approval. The sections also provide instructions about granting the required roles.

### View Access Approval requests and configuration

The following table lists the IAM permissions required to view Access Approval requests and configuration:

Predefined IAM role  |  Required permissions and roles   
---|---  
` roles/accessapproval.viewer ` | 

  * accessapproval.requests.get
  * accessapproval.requests.list
  * accessapproval.serviceAccounts.get
  * accessapproval.settings.get
  * resourcemanager.projects.get
  * resourcemanager.projects.list

  
  
To grant the Access Approval Viewer (`roles/accessapproval.viewer`) role, do the following:

### Console

To grant this IAM role to yourself, do the following: 

  1. Go to the **IAM** page in the Google Cloud console. 

[Go to IAM ](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  2. In the **View by principals** tab, click person_add**Grant access**. 
  3. In the **New principals** field in the right pane, enter your email address. 
  4. Click the **Select a role** field, and select the **Access Approval Viewer** role from the menu. 
  5. Click **Save**. 



### gcloud

Run the following command:
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
      --member='user:EMAIL_ID' \
      --role='roles/accessapproval.viewer'
    

Replace the following:

  * ORGANIZATION_ID: The organization ID.
  * EMAIL_ID: The email ID of the user.



For more information about the command, see [gcloud organizations add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/add-iam-policy-binding).

### View and approve an Access Approval request

The following table lists the IAM permissions required to view and approve an Access Approval request:

Predefined IAM role  |  Required permissions and roles   
---|---  
`roles/accessapproval.approver` | 

  * accessapproval.requests.approve
  * accessapproval.requests.dismiss
  * accessapproval.requests.get
  * accessapproval.requests.invalidate
  * accessapproval.requests.list
  * accessapproval.serviceAccounts.get
  * accessapproval.settings.get
  * resourcemanager.projects.get
  * resourcemanager.projects.list

  
  
To grant the Access Approval Approver (`roles/accessapproval.approver`) role, do the following:

### Console

To grant this IAM role to yourself, do the following: 

  1. Go to the **IAM** page in the Google Cloud console. 

[Go to IAM ](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  2. In the **View by principals** tab, click person_add**Grant access**. 
  3. In the **New principals** field in the right pane, enter your email address. 
  4. Click the **Select a role** field, and select the **Access Approval Approver** role from the menu. 
  5. Click **Save**. 



### gcloud

Run the following command:
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
      --member='user:EMAIL_ID' \
      --role='roles/accessapproval.approver'
    

Replace the following:

  * ORGANIZATION_ID: The organization ID.
  * EMAIL_ID: The email ID of the user.



### Update the Access Approval configuration

The following table lists the IAM permissions required to update Access Approval configuration:

Predefined IAM role  |  Required permissions and roles   
---|---  
`roles/accessapproval.configEditor` | 

  * accessapproval.serviceAccounts.get
  * accessapproval.settings.delete
  * accessapproval.settings.get
  * accessapproval.settings.update
  * resourcemanager.projects.get
  * resourcemanager.projects.list

  
  
To grant the Access Approval Config Editor (`roles/accessapproval.configEditor`) role, do the following:

### Console

To grant this IAM role to yourself, do the following: 

  1. Go to the **IAM** page in the Google Cloud console. 

[Go to IAM ](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  2. In the **View by principals** tab, click person_add**Grant access**. 
  3. In the **New principals** field in the right pane, enter your email address. 
  4. Click the **Select a role** field, and select the **Access Approval Config Editor** role from the menu. 
  5. Click **Save**. 



### gcloud

Run the following command:
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
      --member='user:EMAIL_ID' \
      --role='roles/accessapproval.approver'
    

Replace the following:

  * ORGANIZATION_ID: The organization ID.
  * EMAIL_ID: The email ID of the user.



### Invalidate existing Access Approval requests

The following table lists the IAM permissions required to invalidate existing Access Approval requests that have been approved:

Predefined IAM role  |  Required permissions and roles   
---|---  
` roles/accessapproval.invalidator ` | 

  * accessapproval.requests.get
  * accessapproval.requests.list
  * accessapproval.serviceAccounts.get
  * accessapproval.settings.get
  * resourcemanager.projects.get
  * resourcemanager.projects.list

  
  
To grant the Access Approval Invalidator (`roles/accessapproval.invalidator`) role, do the following:

### Console

To grant this IAM role to yourself, do the following: 

  1. Go to the **IAM** page in the Google Cloud console. 

[Go to IAM ](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  2. In the **View by principals** tab, click person_add**Grant access**. 
  3. In the **New principals** field in the right pane, enter your email address. 
  4. Click the **Select a role** field, and select the **Access Approval Invalidator** role from the menu. 
  5. Click **Save**. 



### gcloud

Run the following command:
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
      --member='user:EMAIL_ID' \
      --role='roles/accessapproval.invalidator'
    

Replace the following:

  * ORGANIZATION_ID: The organization ID.
  * EMAIL_ID: The email ID of the user.



## What's next

  * [Grant or revoke a single IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role)
  * [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
