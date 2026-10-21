---
url: https://docs.cloud.google.com/dataflow/docs/guides/config-store-settings/
title: Manage job settings with Dataflow Config Store \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:24:54.932499+00:00
---

# Manage job settings with Dataflow Config Store  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/config-store-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Manage job settings with Dataflow Config Store Stay organized with collections  Save and categorize content based on your preferences. 

Use Dataflow Config Store to configure and manage job settings across Resource Manager resources, including Google Cloud organizations, folders, and projects.

With Dataflow Config Store, you can set configuration policies at scale without modifying individual pipeline code, job templates, or deployment scripts. For example, you can set a default launcher machine type across an entire organization or folder to mitigate Compute Engine machine type shortages, facilitate machine migrations, or standardize resource sizing.

## Supported settings and limitations

Dataflow Config Store supports the following settings:

  * **`default_launcher_machine_type`** : Specifies the default Compute Engine [machine type](https://docs.cloud.google.com/compute/docs/machine-types) (such as `e2-standard-2` or `n2-standard-2`) that is used by the template launcher VM for [Flex Template](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates#compare) jobs.



Dataflow Config Store has the following limitations:

  * The `default_launcher_machine_type` setting applies only to the template launcher VM for Flex Template jobs. It doesn't affect worker VMs or classic template jobs. To configure worker VM machine types, see [Configure Dataflow worker VMs](https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm).
  * When you target a project, you must specify the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). Project IDs aren't supported.
  * Config Store settings are regional and apply only to jobs running in the same [Dataflow region](https://docs.cloud.google.com/dataflow/docs/resources/locations).



## Setting resolution precedence

When a Dataflow job starts, settings are resolved using a hierarchical precedence model where the most specific configuration takes precedence:

  1. **Job-level configuration** : Settings explicitly passed during job submission (for example, through pipeline options or execution parameters).
  2. **Project-level setting** : A Config Store setting configured directly on the project where the job runs.
  3. **Folder or organization-level setting** : A Config Store setting configured on ancestor resources in the Resource Manager hierarchy. The nearest ancestor folder to the project takes precedence over higher folders and the organization.
  4. **Dataflow service-wide default** : Built-in service defaults used when no override is defined at the job or Resource Manager hierarchy levels.



## Before you begin

Before you manage or inspect Config Store settings, make sure that you have the required Identity and Access Management (IAM) permissions on the target project, folder, or organization.

### Required permissions

Operation | Required permission  
---|---  
Create or update a setting | `dataflow.configStoreSettings.create`  
View an explicitly configured setting | `dataflow.configStoreSettings.get`  
List settings on a resource | `dataflow.configStoreSettings.list`  
Resolve the effective setting | `dataflow.configStoreSettings.resolve`  
Delete a setting override | `dataflow.configStoreSettings.delete`  
  
### Predefined roles

You can grant the following predefined roles on the target project, folder, or organization, or create [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with the required permissions:

  * **Dataflow Admin** (`roles/dataflow.admin`): Includes permissions to create, get, list, resolve, and delete Config Store settings (`dataflow.configStoreSettings.*`).
  * **Dataflow Developer** (`roles/dataflow.developer`): Includes read-only permissions to get, list, and resolve Config Store settings.
  * **Dataflow Viewer** (`roles/dataflow.viewer`): Includes read-only permissions to get, list, and resolve Config Store settings.



For more information, see [Access control with IAM](https://docs.cloud.google.com/dataflow/docs/concepts/access-control).

## Manage settings using the gcloud CLI

You can manage Config Store settings using the gcloud CLI.

### Specify target resource scope

When you use `gcloud dataflow config-store-settings` commands, specify the target resource scope by using one of the following mutually exclusive flags. Don't combine them in the same command.

  * **Project** : `--project=PROJECT_NUMBER` (use your numeric Google Cloud project number, not the project ID)
  * **Folder** : `--folder=FOLDER_ID` (your numeric folder ID)
  * **Organization** : `--organization=ORGANIZATION_ID` (your numeric organization ID)



### Create or update a Config Store setting

To create a setting on a project, folder, or organization, run the `gcloud dataflow config-store-settings create` command. If the setting already exists on the target resource, running the `create` command again with a different `--value` overwrites the existing setting value:
    
    
    gcloud dataflow config-store-settings create SETTING_ID \
        --project=PROJECT_NUMBER \
        --location=REGION \
        --value="SETTING_VALUE"
    

Replace the following:

  * `SETTING_ID`: the ID of the supported setting to configure, such as `default_launcher_machine_type`.
  * `PROJECT_NUMBER`: your numeric Google Cloud project number. To target a folder or an organization instead of a project, replace `--project=PROJECT_NUMBER` with `--folder=FOLDER_ID` or `--organization=ORGANIZATION_ID`.
  * `REGION`: the Dataflow region where the setting applies, such as `us-central1`.
  * `SETTING_VALUE`: the value for the setting, such as `e2-standard-2` for `default_launcher_machine_type`.



### Retrieve a Config Store setting

To retrieve a setting that is configured directly on a resource, run the `gcloud dataflow config-store-settings describe` command:
    
    
    gcloud dataflow config-store-settings describe SETTING_ID \
        --project=PROJECT_NUMBER \
        --location=REGION
    

Replace the following:

  * `SETTING_ID`: the ID of the supported setting to retrieve, such as `default_launcher_machine_type`.
  * `PROJECT_NUMBER`: your numeric Google Cloud project number. To target a folder or an organization instead of a project, replace `--project=PROJECT_NUMBER` with `--folder=FOLDER_ID` or `--organization=ORGANIZATION_ID`.
  * `REGION`: the Dataflow region of the setting, such as `us-central1`.

**Note:** The `describe` command only returns settings that are configured directly on the specified resource. To view the effective value inherited from parent folders or organizations, use the `resolve` command.

### List Config Store settings

To list all Config Store settings that are configured directly on a resource, run the `gcloud dataflow config-store-settings list` command:
    
    
    gcloud dataflow config-store-settings list \
        --project=PROJECT_NUMBER \
        --location=REGION \
        --page-size=10
    

Replace the following:

  * `PROJECT_NUMBER`: your numeric Google Cloud project number. To target a folder or an organization instead of a project, replace `--project=PROJECT_NUMBER` with `--folder=FOLDER_ID` or `--organization=ORGANIZATION_ID`.
  * `REGION`: the Dataflow region to list settings from, such as `us-central1`.



### Resolve the effective setting

To evaluate which setting value applies to jobs started within a resource hierarchy, run the `gcloud dataflow config-store-settings resolve` command. This command acts as a dry run to confirm which setting value a job uses:
    
    
    gcloud dataflow config-store-settings resolve SETTING_ID \
        --project=PROJECT_NUMBER \
        --location=REGION
    

Replace the following:

  * `SETTING_ID`: the ID of the supported setting to resolve, such as `default_launcher_machine_type`.
  * `PROJECT_NUMBER`: your numeric Google Cloud project number. To target a folder or an organization instead of a project, replace `--project=PROJECT_NUMBER` with `--folder=FOLDER_ID` or `--organization=ORGANIZATION_ID`.
  * `REGION`: the Dataflow region where the job runs, such as `us-central1`.

**Note:** The `resolve` command only evaluates Config Store settings that are configured across the Resource Manager hierarchy, including project, folder, and organization levels. It doesn't show job-level configurations or Dataflow service-wide default settings.

The output returns the effective `setting`, along with all candidate `choices` in the hierarchy:
    
    
    setting:
      name: projects/123456789012/locations/us-central1/configStoreSettings/default_launcher_machine_type
      value:
        stringValue: e2-standard-2
    choices:
    - name: projects/123456789012/locations/us-central1/configStoreSettings/default_launcher_machine_type
      value:
        stringValue: e2-standard-2
    - name: organizations/987654321098/locations/us-central1/configStoreSettings/default_launcher_machine_type
      value:
        stringValue: n1-standard-1
    

In this example, both the project and the organization define a value, and the more specific project-level setting (`e2-standard-2`) takes precedence.

### Delete a Config Store setting

To remove a setting override from a resource, run the `gcloud dataflow config-store-settings delete` command:
    
    
    gcloud dataflow config-store-settings delete SETTING_ID \
        --project=PROJECT_NUMBER \
        --location=REGION
    

Replace the following:

  * `SETTING_ID`: the ID of the supported setting to delete, such as `default_launcher_machine_type`.
  * `PROJECT_NUMBER`: your numeric Google Cloud project number. To target a folder or an organization instead of a project, replace `--project=PROJECT_NUMBER` with `--folder=FOLDER_ID` or `--organization=ORGANIZATION_ID`.
  * `REGION`: the Dataflow region of the setting, such as `us-central1`.



When you delete a setting, Dataflow falls back to any setting that is configured on ancestor folders or organizations, or to service-wide defaults.

## Troubleshoot Config Store errors

The following list describes how to resolve common Config Store errors:

  * **`INVALID_ARGUMENT` (HTTP 400)**: The setting value is unsupported (such as an invalid [Compute Engine machine type](https://docs.cloud.google.com/compute/docs/machine-types)), `--project` specifies a project ID instead of a numeric project number, or `--location` isn't a valid [Dataflow region](https://docs.cloud.google.com/dataflow/docs/resources/locations).
  * **`NOT_FOUND` (HTTP 404)**: The setting hasn't been created directly on the specified resource. Run `gcloud dataflow config-store-settings list` to view settings on the resource, or `resolve` to check inherited settings.
  * **`PERMISSION_DENIED` (HTTP 403)**: The caller lacks the required IAM permissions at the target project, folder, or organization scope.
  * **`ABORTED` (HTTP 409)**: A concurrent update modified the setting during your request. Retry the command.
  * **Job fails after creating a setting** : Creating a Config Store setting validates the setting format, but doesn't check regional resource availability. A job can still fail at launch time if the configured resource isn't available. For example, a machine type might not be supported in the target region, or the zone might be experiencing a resource shortage. To resolve this issue, update the setting to use an available machine type. For more information, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) and [Launcher VM resource exhaustion](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-templates#launcher-resource-exhaustion).



## What's next

  * Learn how to [configure Dataflow worker VMs](https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm).
  * Learn how to [set Dataflow pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options).
  * Read the overview of [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * Learn about [Compute Engine machine types](https://docs.cloud.google.com/compute/docs/machine-types).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
