---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/view-custom-data/
title: View custom data from OS policies for your organization \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:19.291156+00:00
---

# View custom data from OS policies for your organization  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/view-custom-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  View custom data from OS policies for your organization Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use VM Manager, Cloud Asset Inventory, and BigQuery to view custom data and enforcement error messages from OS policies across your organization. Use this workflow when you need organization-wide reporting on custom VM configurations, script outputs, or policy execution failures that standard compliance states don't capture.

To collect custom data, you configure an [`outputFilePath`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#exec) in your OS policy, which is the local path on the VM where your policy script writes custom text or JSON output. VM Manager reads the output from this path and stores it in the OS policy assignment report. You can then export these reports to BigQuery by using Cloud Asset Inventory to query the results across your VM fleet.

## Before you begin

  * [Set up VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/setup).
  * Enable the [Cloud Asset Inventory API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com).
  * [Create a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset) to store the exported data.
  * [Create an OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment) that outputs custom data.
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




## Required roles

To get the permissions that you need to export resource data to BigQuery and query custom OS policy data, ask your administrator to grant you the following IAM roles on the project, folder, or organization: 

  * [Cloud Asset Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.viewer) (`roles/cloudasset.viewer`)
  * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)
  * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to export resource data to BigQuery and query custom OS policy data. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to export resource data to BigQuery and query custom OS policy data:

  * `cloudasset.assets.exportOSInventories`
  * `cloudasset.assets.exportResource`
  * `bigquery.datasets.get`
  * `bigquery.tables.create`
  * `bigquery.tables.update`
  * `bigquery.tables.get`
  * `bigquery.jobs.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Sample OS policies

Before you can export and query custom data in BigQuery, you must create and assign an OS policy that collects custom output from your VMs. For more information, see [Create an OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment).

To collect custom data, define an OS policy with an `exec` resource that includes the following sections:

  * **`validate`** : Checks whether the VM matches the selected state. In the following sample policies, the `validate` script exits with code `101` to indicate that the resource doesn't match the selected state. This exit code triggers the `enforce` script on every evaluation.
  * **`enforce`** : Specifies the `outputFilePath` field, runs the custom command, writes the output to the specified path, and exits with code `100` to indicate successful enforcement.



### OS policy that outputs a string

The following sample OS policy outputs a string that contains the kernel version of the VM instance:
    
    
    id: return-kernel-version-policy
    mode: ENFORCEMENT
    resourceGroups:
      - resources:
          id: return-kernel-version
          exec:
            validate:
              interpreter: SHELL
              script: exit 101
            enforce:
              interpreter: SHELL
              outputFilePath: policy-output.txt
              script: uname -r > policy-output.txt && exit 100
    

### OS policy that outputs a JSON file

The following sample OS policy outputs a JSON object that contains the operating system name and kernel version:
    
    
    id: return-kernel-version-js-policy
    mode: ENFORCEMENT
    resourceGroups:
      - resources:
          id: return-kernel-version-js
          exec:
            validate:
              interpreter: SHELL
              script: exit 101
            enforce:
              interpreter: SHELL
              outputFilePath: policy-output.json
              script: |-
                k=$(uname -r)
                o=$(uname -a)
                echo "{ \"name\": \""$o"\", \"kernel\": \""$k"\" }" > policy-output.json
                exit 100
    

## Export VM Manager data to BigQuery

After VM Manager enforces your OS policy, Cloud Asset Inventory collects the resulting OS inventory and OS policy assignment reports across your organization. When you export this data to BigQuery with the `--per-asset-type` flag, Cloud Asset Inventory creates a separate table for each asset type. The resulting `<prefix>_osconfig_googleapis_com_OSPolicyAssignmentReport` table stores your custom policy outputs and enforcement error messages.

To export OS inventory and resource data to BigQuery, follow these steps:

  1. To identify your organization ID, run the following command:
         
         gcloud projects get-ancestors PROJECT_ID
         

Replace `PROJECT_ID` with your project ID.

  2. To export the OS inventory data that VM Manager collects from your VM instances, run the following command:
         
         gcloud asset export \
             --content-type=os-inventory \
             --organization=ORGANIZATION_ID \
             --per-asset-type \
             --bigquery-table="projects/BQ_PROJECT_ID/datasets/DATASET_ID/tables/os"
         

Replace the following placeholders with your values:

     * `ORGANIZATION_ID`: your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
     * `BQ_PROJECT_ID`: the ID of the project that contains your BigQuery dataset.
     * `DATASET_ID`: the ID of your BigQuery dataset (for example, `cai_exp`).
  3. To export the resource metadata—including OS policy assignment reports—to BigQuery, run the following command:
         
         gcloud asset export \
             --content-type=resource \
             --organization=ORGANIZATION_ID \
             --per-asset-type \
             --bigquery-table="projects/BQ_PROJECT_ID/datasets/DATASET_ID/tables/res"
         

Replace the following placeholders with your values:

     * `ORGANIZATION_ID`: your organization ID.
     * `BQ_PROJECT_ID`: the ID of the project that contains your BigQuery dataset.
     * `DATASET_ID`: the ID of your BigQuery dataset (for example, `cai_exp`).

When the export completes, Cloud Asset Inventory creates the `res_osconfig_googleapis_com_OSPolicyAssignmentReport` table in your BigQuery dataset. For more information, see [Export asset snapshot](https://docs.cloud.google.com/asset-inventory/docs/export-bigquery#export).




## Query custom OS policy data in BigQuery

After you export your asset data to BigQuery, you can query the `res_osconfig_googleapis_com_OSPolicyAssignmentReport` table to view custom outputs and enforcement error messages from your OS policies.

To run a query in BigQuery, follow these steps:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, paste one of the following SQL queries:

     * **Query text output** :

The following query returns the kernel version that the OS policy collects for each VM instance:
           
           SELECT
             resource.data.instance as instance,
             ANY_VALUE(
               SAFE_CONVERT_BYTES_TO_STRING(FROM_BASE64(REPLACE(REPLACE(
                 resource_compliances.execResourceOutput.enforcementOutput
                 , '-', '+'), '_', '/')))
               HAVING MAX updateTime) as compliance_results
           FROM
             `DATASET_ID.res_osconfig_googleapis_com_OSPolicyAssignmentReport`,
             UNNEST(resource.data.osPolicyCompliances[OFFSET(0)].osPolicyResourceCompliances) as resource_compliances,
             UNNEST(resource_compliances.configSteps) as config_steps
           WHERE
             resource.data.osPolicyCompliances[OFFSET(0)].osPolicyId = "return-kernel-version-policy"
             AND resource_compliances.osPolicyResourceId = "return-kernel-version"
             AND config_steps.type = "VALIDATION"
           GROUP BY
             instance
           

Replace `DATASET_ID` with the ID of your BigQuery dataset (for example, `cai_exp`).

The query output is similar to the following table:

`instance` | `compliance_results`  
---|---  
`ubuntu-1` | `5.15.0-1036-gcp`  
`ubuntu-2` | `5.15.0-1044-gcp`  
`rhel9-1` | `5.14.0-162.18.1.el9_1.x86_64`  
     * **Query JSON output** :

The following query extracts the `name` and `kernel` fields from the JSON output and returns them as separate columns for each VM instance:
           
           WITH compliance_history AS (
             SELECT
               updateTime,
               resource.data.instance,
               SAFE_CONVERT_BYTES_TO_STRING(
                 FROM_BASE64(
                   REPLACE(
                     REPLACE(
                       resource_compliances.execResourceOutput.enforcementOutput, '-', '+'
                     ), '_', '/'
                   )
                 )
               ) as compliance_results
             FROM
               `DATASET_ID.res_osconfig_googleapis_com_OSPolicyAssignmentReport`,
               UNNEST(resource.data.osPolicyCompliances[OFFSET(0)].osPolicyResourceCompliances) as resource_compliances,
               UNNEST(resource_compliances.configSteps) as config_steps
             WHERE
               resource.data.osPolicyCompliances[OFFSET(0)].osPolicyId = "return-kernel-version-js-policy"
               AND resource_compliances.osPolicyResourceId = "return-kernel-version-js"
               AND config_steps.type = "VALIDATION"
           ),
           compliance_latest AS (
             SELECT
               instance,
               ANY_VALUE(compliance_results HAVING MAX updateTime) as compliance_results
             FROM compliance_history
             GROUP BY instance
           )
           SELECT
             instance,
             JSON_EXTRACT_SCALAR(compliance_results, "$.name") as os_name,
             JSON_EXTRACT_SCALAR(compliance_results, "$.kernel") as kernel_version
           FROM compliance_latest
           

Replace `DATASET_ID` with the ID of your BigQuery dataset (for example, `cai_exp`).

The query output is similar to the following table:

`instance` | `os_name` | `kernel_version`  
---|---|---  
`ubuntu-1` | `Linux ubuntu-1 5.15.0-1036-gcp #39-Ubuntu SMP` | `5.15.0-1036-gcp`  
`rhel9-1` | `Linux rhel9-1 5.14.0-162.18.1.el9_1.x86_64 #1 SMP` | `5.14.0-162.18.1.el9_1.x86_64`  
  3. To execute the query, click **Run**.




For more information, see [Run a query](https://docs.cloud.google.com/bigquery/docs/running-queries).

### Review enforcement error messages

When an OS policy resource fails validation or enforcement, VM Manager records the error message in the `configSteps.errorMessage` field of the `res_osconfig_googleapis_com_OSPolicyAssignmentReport` table. You can query this field in BigQuery to troubleshoot policy execution failures across your organization.

The following query returns the latest validation or enforcement error messages for each VM instance:
    
    
    SELECT
      resource.data.instance AS instance,
      resource.data.osPolicyCompliances[OFFSET(0)].osPolicyId AS policy_id,
      resource_compliances.osPolicyResourceId AS resource_id,
      config_steps.type AS step_type,
      ANY_VALUE(config_steps.errorMessage HAVING MAX updateTime) AS error_message
    FROM
      `DATASET_ID.res_osconfig_googleapis_com_OSPolicyAssignmentReport`,
      UNNEST(resource.data.osPolicyCompliances[OFFSET(0)].osPolicyResourceCompliances) AS resource_compliances,
      UNNEST(resource_compliances.configSteps) AS config_steps
    WHERE
      config_steps.errorMessage IS NOT NULL
      AND config_steps.errorMessage != ""
    GROUP BY
      instance,
      policy_id,
      resource_id,
      step_type
    

Replace `DATASET_ID` with the ID of your BigQuery dataset (for example, `cai_exp`).

The query output is similar to the following table:

`instance` | `policy_id` | `resource_id` | `step_type` | `error_message`  
---|---|---|---|---  
`ubuntu-2` | `return-kernel-version-policy` | `return-kernel-version` | `DESIRED_STATE_ENFORCEMENT` | `Error running enforce script: exit status 1`  
  
## What's next

For more information about managing OS policies and analyzing compliance data, see the following resources:

  * Review [best practices for using VM Manager across an organization](https://docs.cloud.google.com/compute/vm-manager/docs/best-practices).
  * Read the [OS policies overview](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies).
  * [View OS policy compliance reports](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/view-compliance).
  * [Export asset metadata to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-bigquery).
  * [Run interactive and batch queries in BigQuery](https://docs.cloud.google.com/bigquery/docs/running-queries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
