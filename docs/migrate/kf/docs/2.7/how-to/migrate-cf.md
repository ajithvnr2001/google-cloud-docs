---
url: https://docs.cloud.google.com/migrate/kf/docs/2.7/how-to/migrate-cf/
title: Assess and migrate Cloud Foundry \u00a0|\u00a0 Kf 2.7 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:52.537774+00:00
---

# Assess and migrate Cloud Foundry  |  Kf 2.7  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.7/how-to/migrate-cf/

Version 2.7

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.7 ](https://docs.cloud.google.com/migrate/kf/docs/2.7)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.7/getting-started)



Send feedback 

#  Assess and migrate Cloud Foundry Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to perform an assessment of your existing Cloud Foundry (CF) Foundation, and how to migrate the CF Foundation, Organization, Space, or App to Kf.

## Migration fit assessment

Use the [`kf migrate scan-cf-cluster`](https://docs.cloud.google.com/migrate/kf/docs/2.7/cli/kf-migrate-scan-cf-cluster) command to generate a report containing an assessment of the migration readiness of a CF Foundation. You can format the report as a spreadsheet (recommended) or text file.

**Note:** The report does not contain all the information retrieved from the CF API. Instead, it targets specific pieces of data that can be used to estimate portability to Kubernetes.

### Prerequisites

  * The Kf CLI. See [Install Kf CLI](https://docs.cloud.google.com/migrate/kf/docs/2.7/install-cli) for the installation instructions.
  * The [`cf` CLI](https://docs.cloudfoundry.org/cf-cli/install-go-cli.html) intalled as `cf`.
  * The `cf` CLI must be on your path.
  * The `cf` CLI must be authenticated with [admin read-only privileges](https://docs.cloudfoundry.org/uaa/uaa-user-management.html#admin-read-only) or higher on the CF Foundation.



### Perform an assessment

  1. Validate the Foundation to be targeted.
         
         cf curl /v2/info

  2. Run the command to generate a spreadsheet containing the assessment report.

**Note:** The assessment is run locally on your workstation using the Kf CLI, and no data is sent to Google.
         
         kf migrate scan-cf-cluster report.xlsx

  3. Review the assessment.

If you plan to share the assessment, you can redact any information that you do not want to share.




## Migration

Perform the following steps to migrate entities from CF:

  1. **Create migration plan** that describes the migration.

  2. **Edit the migration plan** to customize your migration.

  3. **Apply the migration plan** to perform the migration.




The following sections describe these steps in more detail.

### Migration scopes

Your first decision when performing a migration is to decide on the migration _scope_. The scope determines the CF entity you want to migrate and the privileges you need to perform the migration:

  * **Entire Foundation or Organization** : You must have [admin read-only privileges](https://docs.cloudfoundry.org/uaa/uaa-user-management.html#admin-read-only) or higher on the CF Foundation.

  * **Single Space or App** : You must have [Space Developer privileges](https://docs.cloudfoundry.org/concepts/roles.html#roles) or higher.

**Note:** If you have `scim.read` and `cloud_controller.admin_read_only` scopes, you can also query all Apps across all Spaces in an Organization.



### Prerequisites

To perform a migration, you require:

  * **To create the migration plan** : The Kf CLI. See [Install Kf CLI](https://docs.cloud.google.com/migrate/kf/docs/2.7/install-cli) for the installation instructions.
  * **To apply the migration plan** : A GKE cluster running Kf. See [Install Kf](https://docs.cloud.google.com/migrate/kf/docs/2.7/install) for the installation instructions.
  * Access to a cluster with a Cloud Foundry installation.
  * CF CLI that has targeted the CF Foundation.
  * The privileges on the CF Foundation required by your desired migration scope, as shown above.



### Create a migration plan

Use the `kf migrate plan` command to create the migration plan.

By default, the command writes the migration plan to standard out. You typically redirect the output to a yaml file so that you can customize the plan before applying it. For example, the following command writes the output to standard out:
    
    
    kf migrate plan

Redirect the output to a yaml file:
    
    
    kf migrate plan > plan.yaml

When you run the `kf migrate plan` command, you should see output in the command window in the form below listing the steps performed by the command and any warning or migration issues:
    
    
    kf migrate plan > plan.yaml
    
        Checking CF CLI is available
        Checking CF CLI is authenticated
        ...
    
        WARNING: plan has issues
        Issues with domain "apps.internal" in space "kf-team-acceptance":
            E04 - internal domains are not supported
    
        Issues with application "spring-music" in space "kf-team-app":
            E14 - app manifest must have a single process
    
        Issues with service instance "logspinner-1" in space "kf-team-app":
            E10 - syslog drain configuration is not supported
        ...

#### Generate a migration plan

  1. Ensure that you have logged in to your CF Foundation by using the CF CLI.

  2. Perform the migration based on your desired migration scope, where:

     * MY_ORG specifies the name of the Organization.
     * MY_SPACE specifies the name of the Space.
     * MY_APP specifies the name of the App.
     1. Generate a migration plan for an entire CF Foundation.
            
            kf migrate plan > plan.yaml

     2. Generate a migration plan for an Org.
            
            kf migrate plan --cf-org MY_ORG > plan.yaml

     3. Generate a migration plan for a Space
            
            kf migrate plan --cf-org MY_ORG --cf-space MY_SPACE > plan.yaml

     4. Generate a migration plan for an App.
            
            kf migrate plan --cf-org MY_ORG --cf-space MY_SPACE --cf-app MY_APP > plan.yaml




If you see the following error after running any of these commands:
    
    
    You are not authorized to perform the requested action CF-NotAuthorized 10003
    

You do not have required privileges to read the necessary CAPI endpoints.

### Edit the migration plan

Review and optionally modify the generated migration plan to resolve any errors.

### Apply the migration plan

Use the `kf migrate apply` command to apply the migration plan and migrate the CF entity:

  1. Ensure that you have set `.kubeconfig` to target your Kf cluster.

  2. Ensure that you have access to a GKE cluster running a full Kf installation. That means you have run the following command to connect to the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
            --project=CLUSTER_PROJECT_ID \
            --zone=CLUSTER_LOCATION

  3. Ensure that there are no existing Space names on your Kf cluster that will collide with a Space referenced in the migration plan.

Space names are of the form cf-org-cf-space. For example, if the Org name is `myorg` and the Space name is `myspace`, then the Kf space will be `myorg-myspace`.

  4. Apply the migration plan.
         
         kf migrate apply -v --plan plan.yaml

The verbose flag `-v` is recommended but not required. This flag causes the command to output the Kf commands used to perform the migration.

**Note:** You might see errors from the apply step. For example, `E04 - internal domains are not supported`. In some situations, you can ignore these errors by specifying the `--allow-issues` flag. Alternatively, you can edit the migration plan to address the error.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
