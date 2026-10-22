---
url: https://docs.cloud.google.com/data-transfer-essentials/docs/access-control/
title: Roles and permissions \u00a0|\u00a0 Data Transfer Essentials \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:49.657032+00:00
---

# Roles and permissions  |  Data Transfer Essentials  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-transfer-essentials/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Data Transfer Essentials ](https://docs.cloud.google.com/data-transfer-essentials/docs)
  * [ Guides ](https://docs.cloud.google.com/data-transfer-essentials/docs/overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) to let you provide more granular access to specific Google Cloud resources and prevent access to other resources. This page describes the roles and permissions for Data Transfer Essentials.

IAM lets you adopt the [security principle of least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege) so that you need to grant only the necessary access to your resources.

Roles are collections of IAM permissions. To make permissions available to principals, including users, groups, and service accounts, you grant roles to the principals. You can control _who_ has _what_ permissions to _which_ resources by setting IAM policies. IAM policies grant specific roles to principals, thereby giving them certain permissions.

For detailed information about IAM roles, see [Roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview).

## Predefined roles and permissions for Data Transfer Essentials

Data Transfer Essentials supports IAM permissions at the project level.

The following table lists Data Transfer Essentials IAM roles and the permissions that each role includes.

Roles | Permissions  
---|---  
Data Transfer Essentials Config Admin (`roles/networkconnectivity.multicloudDataTransferConfigAdmin`) Grants full control over Data Transfer Essentials resources | 
    
    
    networkconnectivity.multicloudDataTransferConfigs.*
    networkconnectivity.multicloudDataTransferDestinations.*
    networkconnectivity.multicloudDataTransferSupportedServices.*
    networkconnectivity.operations.get
    networkconnectivity.operations.list
    resourcemanager.projects.get
    resourcemanager.projects.list
    

|  Data Transfer Essentials Config Viewer (`roles/networkconnectivity.multicloudDataTransferConfigViewer`) Grants read-only access to all Data Transfer Essentials resources | 
    
    
    networkconnectivity.multicloudDataTransferConfigs.get
    networkconnectivity.multicloudDataTransferConfigs.list
    networkconnectivity.multicloudDataTransferDestinations.get
    networkconnectivity.multicloudDataTransferDestinations.list
    networkconnectivity.multicloudDataTransferSupportedServices.*
    networkconnectivity.operations.get
    networkconnectivity.operations.list
    resourcemanager.projects.get
    resourcemanager.projects.list
      
  
Destination Admin (`roles/networkconnectivity.multicloudDataTransferDestinationAdmin`) Grants full control over Data Transfer Essentials destinations | 
    
    
    networkconnectivity.multicloudDataTransferDestinations.*
    networkconnectivity.multicloudDataTransferSupportedServices.*
    networkconnectivity.operations.get
    networkconnectivity.operations.list
    resourcemanager.projects.get
    resourcemanager.projects.list
      
  
Destination Viewer (`roles/networkconnectivity.multicloudDataTransferDestinationViewer`) Grants read-only access to all Data Transfer Essentials destinations | 
    
    
    networkconnectivity.multicloudDataTransferDestinations.get
    networkconnectivity.multicloudDataTransferDestinations.list
    networkconnectivity.multicloudDataTransferSupportedServices.*
    networkconnectivity.operations.get
    networkconnectivity.operations.list
    resourcemanager.projects.get
    resourcemanager.projects.list
      
  
Ensure that you have the required permissions for the other Google Cloud products that you use with Data Transfer Essentials.

## Manage access control

To set access controls at the project level, follow these steps:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select your project.

  3. Click person_add**Grant access**.

  4. In the **New principals** field, enter the email address of a new principal.

  5. Click **Add roles** , and then select the required role.

  6. Click **Save**.

  7. Verify that the principal is listed with the role that you granted.




## Identify the permissions in a role

To determine whether one or more permissions are included in a role, use one of the following methods:

  * The [IAM permissions search reference](https://docs.cloud.google.com/iam/docs/permissions-reference)
  * The [`gcloud iam roles describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/describe)
  * The [`roles.get` method](https://docs.cloud.google.com/iam/reference/rest/v1/roles/get) in the IAM API



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
