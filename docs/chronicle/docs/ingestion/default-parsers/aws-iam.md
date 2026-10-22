---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-iam/
title: Collect AWS IAM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:34.108047+00:00
---

# Collect AWS IAM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS IAM logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Identity and Access Management (IAM) configuration data to Google Security Operations using the Third Party API feed.

The AWS IAM parser transforms the IAM entity data (users, groups, roles, and policies) into the structured Unified Data Model (UDM), extracting fields like user details, role information, permissions, and timestamps for consistent security analysis.

**Note:** The AWS IAM log type collects IAM _configuration_ state (entity context), not IAM _activity_. To collect IAM activity events (who performed which API actions), use AWS CloudTrail and the [Collect AWS CloudTrail logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudtrail) guide (log type `AWS_CLOUDTRAIL`). The AWS IAM parser does not parse CloudTrail events.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to AWS Console
  * Permissions to create IAM users and policies



## Get Google SecOps IP ranges

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Make a note of the IP ranges displayed at the top of the page. 
     * Alternatively, retrieve IP ranges programmatically using the [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api).



## Create an IAM user with required permissions

**CRITICAL:** To allow Google SecOps to retrieve AWS IAM data using the API, you must create an IAM user with appropriate read permissions.

### Option A: Use an AWS managed policy (Recommended)

  1. Create a **User** following the instructions in this guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  2. Select the created **User**.
  3. Select the **Security credentials** tab.
  4. Click **Create Access Key** in the **Access Keys** section.
  5. Select **Third-party service** as **Use case**.
  6. Click **Next**. 
     * Optional: Add a description tag.
  7. Click **Create access key**.
  8. Click **Download .csv file** to save the **Access Key ID** and **Secret Access Key** for future reference.
  9. Click **Done**.
  10. Select the **Permissions** tab.
  11. Click **Add permissions** in the **Permissions policies** section.
  12. Select **Add permissions**.
  13. Select **Attach policies directly**.
  14. Search for **IAMReadOnlyAccess** (AWS managed policy).
  15. Select the policy.
  16. Click **Next**.
  17. Click **Add permissions**.



**Important:** The **IAMReadOnlyAccess** policy includes all required permissions:

  * `iam:GetUser`
  * `iam:ListUsers`
  * `iam:GetGroup`
  * `iam:ListGroups`
  * `iam:GetPolicy`
  * `iam:ListPolicies`
  * `iam:GetRole`
  * `iam:ListRoles`
  * `iam:ListAttachedUserPolicies`
  * `iam:ListAttachedGroupPolicies`
  * `iam:ListAttachedRolePolicies`
  * `iam:GetAccountSummary`



### Option B: Create a custom policy (least privilege)

If your security policy requires minimal permissions instead of the managed policy:

  1. In the AWS console, go to **IAM > Policies > Create policy > JSON tab**.
  2. Paste the following policy:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": [
                 "iam:GetUser",
                 "iam:ListUsers",
                 "iam:GetGroup",
                 "iam:ListGroups",
                 "iam:GetPolicy",
                 "iam:ListPolicies",
                 "iam:GetRole",
                 "iam:ListRoles",
                 "iam:ListAttachedUserPolicies",
                 "iam:ListAttachedGroupPolicies",
                 "iam:ListAttachedRolePolicies",
                 "iam:GetAccountSummary"
               ],
               "Resource": "*"
             }
           ]
         }
         

  3. Click **Next**.

  4. Name the policy `chronicle-iam-api-read-policy`.

  5. Click **Create policy**.

  6. Create a **User** following the instructions in this guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).

  7. Select the created **User**.

  8. Select the **Security credentials** tab.

  9. Click **Create Access Key** in the **Access Keys** section.

  10. Select **Third-party service** as **Use case**.

  11. Click **Next**.

     * Optional: Add a description tag.
  12. Click **Create access key**.

  13. Click **Download .csv file** to save the **Access Key ID** and **Secret Access Key** for future reference.

  14. Click **Done**.

  15. Select the **Permissions** tab.

  16. Click **Add permissions** in the **Permissions policies** section.

  17. Select **Add permissions**.

  18. Select **Attach policies directly**.

  19. Search for and select `chronicle-iam-api-read-policy`.

  20. Click **Next**.

  21. Click **Add permissions**.


**Note:** All actions are read-only and don't modify AWS resources.

## Configure a feed in Google SecOps to ingest IAM configuration data

The AWS IAM feed collects one IAM entity list per feed, selected by the **API type** field (**Users** , **Roles** , or **Groups**). To collect all IAM entities, create one feed for each API type, all using the **AWS IAM** log type.

### Using the Content Hub (recommended)

**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

  1. Go to **Content Hub > Content Packs > Get Started**.
  2. Click the **Amazon Cloud Platform** pack.
  3. Find the **AWS IAM** log type in the list.
  4. Select **Third party API** from the **Source Type** drop-down.
  5. Provide the following configuration details: 
     * **Username** : The Access Key ID from the IAM user created earlier.
     * **Secret** : The Secret Access Key from the IAM user created earlier.
     * **API type** : Select the IAM entity list to collect: **Users** , **Roles** , or **Groups**.
     * **Feed Name** : A prepopulated value that identifies the feed (for example, `AWS IAM Users`).
     * **Asset Namespace** : Namespace associated with the feed.
     * **Ingestion Labels** : Labels applied to all events from this feed.
  6. Click **Create feed**.



For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

### Using SIEM settings

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `AWS IAM API Configuration`).
  5. Select **Third party API** as the **Source type**.
  6. Select **AWS IAM** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Username** : The Access Key ID from the IAM user created earlier.
     * **Secret** : The Secret Access Key from the IAM user created earlier.
     * **API type** : Select the IAM entity list to collect: **Users** , **Roles** , or **Groups**.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Group.CreateDate` | `entity.group.attribute.creation_time` | Parsed as `ISO8601`  
`Group.Path` | `entity.group.attribute.labels.value` | Directly mapped  
`IsTruncated` | `entity.group.attribute.labels.value` | Directly mapped  
`Marker` | `entity.group.attribute.labels.value` | Directly mapped  
`Group.GroupName` | `entity.group.email_addresses` | Merged  
`Group.GroupName` | `entity.group.group_display_name` | Directly mapped  
`Group.GroupID` | `entity.group.product_object_id` | Directly mapped  
`RoleLastUsed.Region` | `entity.location.name` | Directly mapped  
`CreateDate` | `entity.resource.attribute.creation_time` | Parsed as `ISO8601`  
`MaxSessionDuration` | `entity.resource.attribute.labels.value` | Directly mapped  
`Path` | `entity.resource.attribute.labels.value` | Directly mapped  
`RoleLastUsed.LastUsedDate` | `entity.resource.attribute.labels.value` | Directly mapped  
`AssumeRolePolicyDocument` | `entity.resource.attribute.permissions.name` | Directly mapped  
`Description` | `entity.resource.attribute.roles.description` | Directly mapped  
`RoleName` | `entity.resource.attribute.roles.name` | Directly mapped  
`Arn` | `entity.resource.name` | Directly mapped  
`Group.Arn` | `entity.resource.name` | Directly mapped  
`RoleID` | `entity.resource.product_object_id` | Directly mapped  
`CreateDate` | `entity.user.attribute.creation_time` | Parsed as `ISO8601`  
`PasswordLastUsed` | `entity.user.last_login_time` | Parsed as `ISO8601`  
`UserID` | `entity.user.product_object_id` | Directly mapped  
`UserName` | `entity.user.userid` | Directly mapped  
`PermissionsBoundary.PermissionsBoundaryArn` | `relations.entity.resource.attribute.labels.value` | Directly mapped  
`PermissionsBoundary.PermissionsBoundaryType` | `relations.entity.resource.attribute.labels.value` | Directly mapped  
`user.PermissionsBoundary.PermissionsBoundaryArn` | `relations.entity.resource.attribute.labels.value` | Directly mapped  
`user.PermissionsBoundary.PermissionsBoundaryType` | `relations.entity.resource.attribute.labels.value` | Directly mapped  
`user.Arn` | `relations.entity.resource.name` | Directly mapped  
`user.CreateDate` | `relations.entity.user.attribute.creation_time` | Parsed as `ISO8601`  
`tag.Key` | `relations.entity.user.attribute.labels.key` | Directly mapped  
`Path` | `relations.entity.user.attribute.labels.value` | Directly mapped  
`tag.Value` | `relations.entity.user.attribute.labels.value` | Directly mapped  
`user.Path` | `relations.entity.user.attribute.labels.value` | Directly mapped  
`user.PasswordLastUsed` | `relations.entity.user.last_login_time` | Parsed as `ISO8601`  
`user.UserID` | `relations.entity.user.product_object_id` | Directly mapped  
`user.UserName` | `relations.entity.user.userid` | Directly mapped  
N/A | `entity.group.attribute.labels.key` | Constant: `is_truncated`  
N/A | `entity.resource.attribute.cloud.environment` | Constant: `AMAZON_WEB_SERVICES`  
N/A | `entity.resource.attribute.labels.key` | Constant: `max_session_duration`  
N/A | `entity.resource.resource_subtype` | Constant: `User`  
N/A | `entity.resource.resource_type` | Constant: `ACCESS_POLICY`  
N/A | `metadata.entity_type` | Constant: `USER`  
N/A | `metadata.product_name` | Constant: `AWS IAM`  
N/A | `metadata.vendor_name` | Constant: `AWS`  
N/A | `relations.direction` | Constant: `UNIDIRECTIONAL`  
N/A | `relations.entity.resource.attribute.labels.key` | Constant: `permissions_boundary_arn`  
N/A | `relations.entity.resource.resource_subtype` | Constant: `User`  
N/A | `relations.entity.user.attribute.labels.key` | Constant: `path`  
N/A | `relations.entity_type` | Constant: `USER`  
N/A | `relations.relationship` | Constant: `MEMBER`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-iam-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
