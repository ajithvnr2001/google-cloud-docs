---
url: https://docs.cloud.google.com/compute/docs/disks/configure-recycle-bin/
title: Configure the recycle bin retention policy \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:20:45.743248+00:00
---

# Configure the recycle bin retention policy  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/configure-recycle-bin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure the recycle bin retention policy Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Recycle bin for Compute Engine snapshots**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, Compute Engine retains deleted standard snapshots in the [recycle bin](https://docs.cloud.google.com/compute/docs/disks/retain-deleted-resources) for a three-day _retention period_ before permanently erasing the snapshots. You can configure a shorter retention period or disable the recycle bin by modifying the _recycle bin retention policy_.

This document describes how to view and configure the recycle bin retention policy.

To view the contents of a recycle bin or to recover a snapshot from the recycle bin, see [Manage the recycle bin](https://docs.cloud.google.com/compute/docs/disks/manage-recycle-bin).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles and permissions

To get the permissions that you need to view and manage the recycle bin retention policy, ask your administrator to grant you the [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view and manage the recycle bin retention policy. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view and manage the recycle bin retention policy:

  * To set, modify, and delete rules in the recycle bin retention policy: `compute.snapshotRecycleBinPolicy.patch`
  * To view the recycle bin retention policy: `compute.snapshotRecycleBinPolicy.get`
  * To view the recycle bin retention policy for a standard snapshot: `compute.snapshots.getEffectiveRecycleBinRule` on the snapshot 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## How the recycle bin retention policy works

The recycle bin retention policy is a global collection of rules that define the retention period for standard snapshots across all projects and organizations.

The recycle bin retention policy has the following features:

  * The three-day default retention period is called the _system default rule_. You can't remove the system default rule, but you can override it.

  * To override the system default rule, you can add _project or organization default rules_ that apply to a project or organization, respectively. You can also add tag-based rules to the recycle bin retention policy. 

  * Rule conflicts in the retention policy are resolved as follows:

    1. Tag-based rules override both project and organization default rules.
    2. If multiple tag-based rules apply to a standard snapshot, then the rule with the longest retention period applies. However, a project default rule won't override a tag-based rule even if the former has a longer retention period.
    3. Project default rules override the organization default rule.
    4. If no rules apply to a standard snapshot, then the system default rule applies.

For more information, see [Hierarchy of rules within the recycle bin retention policy](https://docs.cloud.google.com/compute/docs/disks/retain-deleted-resources#hierarchy-of-rules).

  * Although Google doesn't recommend disabling the recycle bin, you can do so for a project, organization, or tag by creating a rule with a zero-day retention period. All standard snapshots that are subject to the rule are immediately erased when you delete them.

  * Changes to the recycle bin retention policy don't apply to existing recoverable snapshots, that is, existing deleted standard snapshots that are in the recycle bin. 




## Limitations

  * Only standard snapshots are supported. Archive snapshots, instant snapshots, disks, and images are immediately permanently erased upon deletion. 
  * Changes to the recycle bin retention policy don't apply to existing recoverable snapshots, that is, existing deleted standard snapshots that are in the recycle bin. 
  * To specify a retention policy rule for a tag, the tag must already exist.
  * You can set retention policy rules for only projects, organizations, or tags.
  * If you set a retention policy rule for a tag, the retention policy only applies to standard snapshots that have that tag. Archive snapshots, instant snapshots, disks, and any other resources that have that tag aren't compatible with the recycle bin and are permanently erased when you delete them.



## Set or remove the default retention period for a project or organization

To override the three-day system default rule within a project or organization or to disable the recycle bin, set the default retention policy rule for the project or organization.

**Important:** Only standard snapshots are supported. Archive snapshots, instant snapshots, disks, and images are immediately permanently erased upon deletion. Changes to the recycle bin retention policy don't apply to existing recoverable snapshots, that is, existing deleted standard snapshots that are in the recycle bin. 

You can use the gcloud CLI or REST.

###  gcloud CLI 

Use the [`gcloud beta compute snapshot-recycle-bin-policy update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshot-recycle-bin-policy/update). Use the `--set-rule=default` flag to set the default retention policy rule and the `--standard-snapshots-retention-duration-days` flag to specify the retention period for the rule.

  * To set the default retention policy for an organization, use the following command:
        
        gcloud beta compute snapshot-recycle-bin-policy update \
          --set-rule=default \
          --standard-snapshots-retention-duration-days=DEFAULT_RETENTION_PERIOD_DAYS \
          --organization=ORGANIZATION_ID
        

Replace the following with the corresponding values:

    * `DEFAULT_RETENTION_PERIOD_DAYS`: the retention period, in days, for the project or organization. Specify a value from `0` to `7`. To disable the recycle bin, specify `0`.
    * `ORGANIZATION_ID`: optional. [The ID of the organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id), for which you want to set the default retention rule. For example, `123456789012`. You must specify the organization ID or the project ID, but not both.

To set the default retention policy for a project, replace the `--organization` flag with `--project=<var>PROJECT_ID</var>` in the preceding command, where `PROJECT_ID` is the ID of the project.

  * To remove the default retention rule for a project or organization, use the same command, but specify `--remove-rule=default` instead of `--set-rule=default`.

For example, to remove the default retention policy rule for an organization:
        
        gcloud beta compute snapshot-recycle-bin-policy update \
          --organization=ORGANIZATION_ID \
          **--remove-rule=default**
        

Replace `ORGANIZATION_ID` with the ID of the organization.




###  REST 

Construct a `PATCH` request to the [`snapshotRecycleBinPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/snapshotRecycleBinPolicy).

In the request body, include a `rules` object that specifies the default recycle bin period, in days.

  * To add or modify a retention policy for a project:
        
        PATCH  https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/snapshotRecycleBinPolicy
        {
        "rules": {
          "default": {
            "standardSnapshots": {
              "retentionDurationDays": DEFAULT_RETENTION_PERIOD_DAYS
            }
          }
        }
        }
        

Replace the following with the corresponding values:

    * `PROJECT_ID`: the project ID, for example, `dev-project`.
    * `DEFAULT_RETENTION_PERIOD_DAYS`: the default retention period, in days. Specify a value from `0` to `7`. To disable the recycle bin, specify `0`.
  * To add or modify a retention policy for an organization, make a `PATCH` request as in the preceding example, but use the following URL. 
        
        PATCH https://compute.googleapis.com/compute/beta/organizations/ORGANIZATION_ID/global/snapshotRecycleBinPolicy/
        
        

The request body is the same as in the preceding example.

Replace the `ORGANIZATION_ID` with the [ID of the organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). For example, `123456789012`. 

  * To remove the default retention rule for a project or organization, make a similar `PATCH` request, but specify `null` for the `default` rule.

For example, to remove the default retention rule for an organization:
        
        PATCH https://compute.googleapis.com/compute/beta/organizations/ORGANIZATION_ID/global/snapshotRecycleBinPolicy/
        {
        "rules": {
           "default": null
         }
        }
        

Replace `ORGANIZATION_ID` with the ID of the organization.




## Set or remove the retention policy for a tag

To set a specific retention period for standard snapshots that have a specific tag, set a tag-based rule at the project or organization level. Tag based rules override the default rule for a project or organization and have the following characteristics:

  * Tag-based rules at the organization or project level apply to all the standard snapshots within the organization or project, respectively, that have the tag.
  * Project-level tag rules override organization-level tag rules only if the project-level rule has a longer retention period.

For example, an organization-level tag rule with a two-day retention period overrides a one-day project-level tag rule.




For more information, see [Hierarchy of rules within the recycle bin retention policy](https://docs.cloud.google.com/compute/docs/disks/retain-deleted-resources#hierarchy-of-rules).

You can use the gcloud CLI or REST.

**Important:** Only standard snapshots are supported. Archive snapshots, instant snapshots, disks, and images are immediately permanently erased upon deletion. Changes to the recycle bin retention policy don't apply to existing recoverable snapshots, that is, existing deleted standard snapshots that are in the recycle bin. 

###  gcloud CLI 

To **set a retention policy rule for a tag** , use the [`gcloud beta compute snapshot-recycle-bin-policy update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshot-recycle-bin-policy/update). Use the `--set-rule` flag to specify the name of the tag and the `--standard-snapshots-retention-duration-days` flag to specify the recycle bin retention period, in days, for the tag.
    
    
    gcloud beta compute snapshot-recycle-bin-policy update \
      --set-rule=TAG_NAMESPACED_NAME \
      --standard-snapshots-retention-duration-days=RETENTION_PERIOD_DAYS \
      --organization=ORGANIZATION_ID
    

Replace the following with the corresponding values:

  * `TAG_NAMESPACED_NAME`: the namespaced name of the tag, including its value. For example, `my-project-id/tag-key/tag-value` or `my-organization-id/tag-key/tag-value`.
  * `RETENTION_PERIOD_DAYS`: the retention period in days, from `0` to `7`. To disable the recycle bin for snapshots with this tag, specify `0`.
  * `ORGANIZATION_ID`: optional. [The ID of the organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id), that the rule applies to. For example, `123456789012`. You must specify either the organization ID or the project ID, but not both.



To set the default retention policy for a project, replace the `--organization` flag with `--project=<var>PROJECT_ID</var>` in the preceding command, where `PROJECT_ID` is the ID of the project.

To **remove a retention policy rule for a tag** , use the same command, but specify `--remove-rule=TAG_NAMESPACED_NAME` instead of `--set-rule`. For example, to remove a tag-based rule for an organization:
    
    
    gcloud beta compute snapshot-recycle-bin-policy update \
      --organization=ORGANIZATION_ID \
      --remove-rule=TAG_NAMESPACED_NAME
    

###  REST 

To set a retention policy rule for a tag, construct a `PATCH` request to the [`snapshotRecycleBinPolicy` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/snapshotRecycleBinPolicy). In the request body, include a `rules` object that specifies the name of the tag and the retention period, in days.

  * To set or update a retention policy rule for a tag in a project:


    
    
    PATCH https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/snapshotRecycleBinPolicy/
    {
      "rules": {
        "TAG_NAMESPACED_NAME_1": {
          "standardSnapshots": { 
            "retentionDurationDays": RETENTION_PERIOD_DAYS
          }
        }
      }
    }
    

Replace the following with the corresponding values:

  * `PROJECT_ID`: the ID of the project.
  * `TAG_NAMESPACED_NAME`: the namespaced name of the tag, including its value. For example, `my-project-id/env/prod` or `my-organization-id/env/build`.
  * `RETENTION_PERIOD_DAYS`: the retention period in days, from `0` to `7`. To disable the recycle bin for snapshots with this tag, specify `0`.

  * To set or update a retention policy rule for a tag in an organization, make a `PATCH` request as in the preceding example, but use the following URL.



    
    
    PATCH https://compute.googleapis.com/compute/beta/organizations/ORGANIZATION_ID/global/snapshotRecycleBinPolicy/
    
    

Replace `ORGANIZATION_ID` with the organization's ID. The request body is as described in the previous example.

  * To remove a retention policy rule for a tag, construct a `PATCH` request as in the preceding examples, but specify `null` for the tag-based rule. For example, to remove the retention policy rule for a tag-based rule in a project:


    
    
    PATCH https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/snapshotRecycleBinPolicy
    {
      "rules": {
        "TAG_NAMESPACED_NAME_1": null
      }
    }
    

## View the recycle bin retention policy for a project or organization

To determine if a project or organization has custom rules for the recycle bin, view any tag-based rules, or check if the recycle bin is disabled, view the rules in the project or organization's recycle bin retention policy.

**Note:** If you don't have the required permissions to view a project or organization's recycle bin retention policy, then you can't view any organization-level rules in the retention policy. So if no rules are visible, this does not always mean that no rules are configured. To obtain the needed permissions, contact your organization's administrator.

To view the rules in a project or organization's recycle bin retention policy, use the gcloud CLI or REST.

###  gcloud CLI 

To view the recycle bin retention policy for a project or an organization, including the tag-based rules, use the [`gcloud beta compute snapshot-recycle-bin-policy describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshot-recycle-bin-policy/describe):

  * To view the recycle bin retention policy for an organization:
        
        gcloud beta compute snapshot-recycle-bin-policy describe \
          --organization=ORGANIZATION_ID
        

Replace `ORGANIZATION_ID` with the organization's ID.

  * To view the recycle bin retention policy for a project:
        
        gcloud beta compute snapshot-recycle-bin-policy describe \
        --project=PROJECT_ID
        

Replace `PROJECT_ID` with the project's ID.




The output is a list of rule objects similar to the following. The three-day system default rule is included in the output.
    
    
      rules:
        default:
          standardSnapshots:
            retentionDurationDays: '2'
        database-project/Testing-tag-key/build:
          standardSnapshots:
            retentionDurationDays: '0'
        database-project/Testing-tag-key/critical:
          standardSnapshots:
            retentionDurationDays: '5'
        systemRules:
          default:
            standardSnapshots:
              retentionDurationDays: '3'
    

The `retentionDurationDays` field for each rule indicates the rule's retention period, in days. In this example, the project, `database-project`, has three rules:

  * a five-day rule for all snapshots with the tag `Testing-tag-key/critical`. 
  * immediate deletion for all snapshots with the tag `Testing-tag-key/build`.
  * a two-day default retention for all other snapshots in the project.



###  REST 

To view all the retention policy rules for a project or organization, including the tag-based rules, construct a `GET` request to the [`snapshotRecycleBinPolicy.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/snapshotRecycleBinPolicy).

  * To view an organization's retention policy:
        
        GET https://compute.googleapis.com/compute/beta/organizations/ORGANIZATION_ID/global/snapshotRecycleBinPolicy
        

Replace `ORGANIZATION_ID` with the organization's ID.

  * To view a project's retention policy:
        
        GET https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/snapshotRecycleBinPolicy
        

Replace `PROJECT_ID` with the ID of the project.




The response is similar to the following. The three-day system default rule is included in the output.
    
    
      {
        "rules": {
         "default": {
          "standardSnapshots": {
            "retentionDurationDays": "2"
          }
        },
        "database-project/Testing-tag-key/build": {
          "standardSnapshots": {
            "retentionDurationDays": "0"
          }
        },
        "database-project/Testing-tag-key/critical": {
          "standardSnapshots": {
            "retentionDurationDays": "5"
          }
        },
         "systemRules": {
          "default": {
           "standardSnapshots": {
             "retentionDurationDays": "3"
          }
         }
        }
      }
     }
    

The `retentionDurationDays` field for each rule indicates the rule's retention period, in days. In this example, the project, `database-project`, has three rules:

  * a five-day rule for all snapshots with the tag `Testing-tag-key/critical`. 
  * immediate deletion for all snapshots with the tag `Testing-tag-key/build`.
  * a two-day default retention for all other snapshots in the project.



If the retention period is zero, then Compute Engine will permanently erase the snapshot immediately after it is deleted. Otherwise, the retention period indicates how long Compute Engine will retain the snapshot in the recycle bin before permanently erasing it.

## View the recycle bin retention period for a tag

To view the retention policy for a tag, retrieve the retention policy for the project or organization where the tag is defined.

## Check the recycle bin retention period for a specific snapshot

To determine if a standard snapshot will be retained in the recycle bin, if it is deleted, and for how long, check its retention period. If the retention period is zero, then the snapshot will be permanently erased immediately after it is deleted. Otherwise, the retention period indicates how long the snapshot will be retained in the recycle bin if it is deleted.

You can check the retention period for a specific snapshot by using the Google Cloud console, gcloud CLI, or REST.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Snapshots** page.



[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  1. On the **Snapshots** tab, view the list of snapshots in the project.

  2. In the **Name** column, click the name of the standard snapshot. The **Snapshot details** page for the selected snapshot appears.

  3. The **Recycle bin retention** property shows the snapshot's recycle bin retention period snapshot.




###  gcloud CLI 

To view the retention period for a specific snapshot, use the [`gcloud beta compute snapshots get-effective-recycle-bin-rule` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshots/get-effective-recycle-bin-rule).
    
    
    gcloud beta compute snapshots get-effective-recycle-bin-rule \
      SNAPSHOT_NAME \
      --project=PROJECT_ID
    

Replace the following with the corresponding values:

  * `PROJECT_ID`: the ID of the project that contains the snapshot.
  * `SNAPSHOT_NAME`: the name of the snapshot.



The output is similar to the following:
    
    
    retentionDurationDays: '5'
    

The `retentionDurationDays` field indicates the snapshots' recycle bin retention period, in days.

###  REST 

To view the retention period for a specific snapshot, construct a `GET` request to the [`getEffectiveRecycleBinRule` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/snapshots/getEffectiveRecycleBinRule).
    
    
    GET https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/snapshots/SNAPSHOT_NAME/getEffectiveRecycleBinRule
    

Replace the following with the corresponding values:

  * `PROJECT_ID`: the ID of the project that contains the snapshot.
  * `SNAPSHOT_NAME`: the name of the snapshot.



The response is similar to the following:
    
    
    {
      "retentionDurationDays": "5"
    }
    

The `retentionDurationDays` field indicates the snapshots' recycle bin retention period, in days.

If the retention period is zero, then Compute Engine will permanently erase the snapshot immediately after it is deleted. Otherwise, the retention period indicates how long Compute Engine will retain the snapshot in the recycle bin before permanently erasing it.

To determine which rules in the retention policy apply to the snapshot, compare the snapshot's tags to the tags and the default rule in the retention policy for the project and organization.

To change the retention period for a standard snapshot, choose one of the following options:

  * Create a tag-based rule for one of the snapshot's tags
  * If an appropriate tag-based rule already exists, add that tag to the snapshot by following the instructions in [Add tags to a resource](https://docs.cloud.google.com/compute/docs/tag-resources#adding_tags_to_a_resource).
  * Change the default recycle bin retention rule for the project or organization, but note that this will apply to all other standard snapshots in the project or organization.



## What's next

  * [Recover a snapshot from the recycle bin](https://docs.cloud.google.com/compute/docs/disks/manage-recycle-bin)
  * To manage tags for a standard snapshot, see [Adding tags to a resource](https://docs.cloud.google.com/compute/docs/tag-resources#adding_tags_to_a_resource)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
