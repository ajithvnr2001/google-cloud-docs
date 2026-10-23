---
url: https://docs.cloud.google.com/dataform/docs/manage-repository/
title: Manage a repository \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:28.318876+00:00
---

# Manage a repository  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/manage-repository/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Manage a repository Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to do the following in Dataform:

  * Configure Dataform workflow settings.
  * Manage the Dataform core package.
  * Version control your code.



## Before you begin

  1. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).

**Note:** The Dataform repositories list includes only repositories created for Dataform workflow development. Repositories for BigQuery Studio assets, such as notebooks or saved queries, are managed separately and don't appear in this list.
  2. Optional: [Connect your repository to a third-party Git repository](https://docs.cloud.google.com/dataform/docs/connect-repository).

  3. [Create and initialize a development workspace in your repository](https://docs.cloud.google.com/dataform/docs/create-workspace).




### Required roles

To get the permissions that you need to complete the tasks in this document, ask your administrator to grant you the following IAM roles: 

  * Configure Dataform settings and manage the location of the Dataform core package: [Dataform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.admin) (`roles/dataform.admin`) on repositories. 
  * Update the Dataform core package and use version control in Dataform: [Dataform Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.editor) (`roles/dataform.editor`) on workspaces. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure Dataform workflow settings

This section shows you how to edit the Dataform workflow processing settings for a specific repository.

You might want to edit the settings file to rename the schemas or add custom compilation variables to your repository.

### About repository settings

For all repositories, a custom service account is required for workflow execution and [strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode) is enforced. You can't use the default Dataform service agent to run workflows.

Each Dataform repository contains a unique workflow settings file. The file contains the Google Cloud project ID and the schema in which Dataform publishes assets in BigQuery. Dataform uses default settings that you can override to best suit your needs by editing the settings file.

As of [Dataform core 3.0.0](https://github.com/dataform-co/dataform/releases/tag/3.0.0), workflow settings are stored in the `workflow_settings.yaml` file by default. In earlier versions of Dataform core, workflow settings are stored in the `dataform.json` file. Both of these configuration files must be in the root directory of your repository. The Dataform core 3.0 `workflow_settings.yaml` file is backward compatible with the `dataform.json` file. You can continue to use the `dataform.json` file to store workflow settings. As a best practice, you should migrate your repository workflow settings to the `workflow_settings.yaml` format for future compatibility.

#### About `workflow_settings.yaml`

The `workflow_settings.yaml` file, introduced in [Dataform core 3.0](https://github.com/dataform-co/dataform/releases/tag/3.0.0), stores Dataform workflow settings in the `YAML` format.

The following code sample shows a sample `workflow_settings.yaml` file:
    
    
      defaultProject: my-gcp-project-id
      defaultDataset: dataform
      defaultLocation: australia-southeast2
      defaultAssertionDataset: dataform_assertions
      dataformCoreVersion: 3.0.62
      preserveGovernanceControls: true
    

In the preceding code sample, the key-value pairs are described as follows:

  * `defaultProject` (optional): your BigQuery Google Cloud project ID. If you don't set the `defaultProject` parameter, Dataform uses the Google Cloud project in which the Dataform repository is located.
  * `defaultDataset`: the BigQuery dataset in which Dataform creates assets, called `dataform` by default.
  * `defaultLocation` (optional): your default BigQuery dataset location. Dataform uses this location to process your code and store the results. This processing location must match the location of your BigQuery datasets. However, it doesn't need to match the Dataform repository location.

If you don't set the `defaultLocation` parameter, Dataform determines the location based on the datasets that your SQL query references. This works as follows:

    * If your query references datasets from the same location, Dataform uses that location.
    * If your query references datasets from two or more different locations, an error occurs. For details about this limitation, see [Cross-region dataset replication](https://docs.cloud.google.com/bigquery/docs/data-replication).
    * If your query doesn't reference any datasets, the default location for Dataform is the `US` multi-region. To choose a different location, set the default location. Alternatively, use the [`@@location` system variable](https://docs.cloud.google.com/bigquery/docs/reference/system-variables) in your query. For more information, see [Specify locations](https://docs.cloud.google.com/bigquery/docs/locations#specify_locations).
  * `defaultAssertionDataset`: the BigQuery dataset in which Dataform creates views with assertion results, called `dataform_assertions` by default.

  * `dataformCoreVersion`: the version of the Dataform core package installed in your repository. For more information, see Manage the Dataform core package.

  * `preserveGovernanceControls` (optional): a boolean value that specifies whether Dataform automatically preserves existing BigQuery data policies and data governance tags (Preview) when recreating tables across workflow executions. For more information, see [Preserve access controls metadata](https://docs.cloud.google.com/dataform/docs/create-tables#preserve-access-controls).




For more information about `workflow_settings.yaml` properties, see [WorkflowSettings](https://dataform-co.github.io/dataform/docs/reference/configs#workflowsettings) in GitHub.

You can access the properties defined in `workflow_settings.yaml` in your Dataform code as properties of the [`dataform.projectConfig`](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference#iprojectconfig) object.

The following mappings from the `workflow_settings.yaml` options to the code-accessible `dataform.projectConfig` options apply:

  * `defaultProject` => `defaultDatabase`
  * `defaultDataset` => `defaultSchema`
  * `defaultAssertionDataset` => `assertionSchema`
  * `projectSuffix` => `databaseSuffix`
  * `datasetSuffix` => `schemaSuffix`
  * `namePrefix` => `tablePrefix`



The following code sample shows the `dataform.projectConfig` object referenced in a `SELECT` statement in a view:
    
    
      config { type: "view" }
      SELECT ${when(
        !dataform.projectConfig.tablePrefix,
        "table prefix is set!",
        "table prefix is not set!"
      )}
    

#### About `dataform.json`

The `dataform.json` file stores Dataform workflow settings in the `JSON` format.

The following code sample shows a sample `dataform.json` file:
    
    
      {
        "warehouse": "bigquery",
        "defaultDatabase": "my-gcp-project-id",
        "defaultSchema": "dataform",
        "defaultLocation": "australia-southeast2",
        "assertionSchema": "dataform_assertions"
      }
    

In the preceding code sample, the key-value pairs are described as follows:

  * `warehouse`: a pointer to BigQuery, where Dataform creates assets.
  * `defaultDatabase` (optional): your BigQuery Google Cloud project ID. If you don't set the `defaultDatabase` parameter, Dataform uses the Google Cloud project in which the Dataform repository is located.
  * `defaultSchema`: the BigQuery dataset in which Dataform creates assets.
  * `defaultLocation` (optional): your default BigQuery dataset location. Dataform uses this location to process your code and store the results. This processing location must match the location of your BigQuery datasets. However, it doesn't need to match the Dataform repository location.

If you don't set the `defaultLocation` parameter, Dataform determines the location based on the datasets that your SQL query references. This works as follows:

    * If your query references datasets from the same location, Dataform uses that location.
    * If your query references datasets from two or more different locations, an error occurs. For details about this limitation, see [Cross-region dataset replication](https://docs.cloud.google.com/bigquery/docs/data-replication).
    * If your query doesn't reference any datasets, the default location for Dataform is the `US` multi-region. To choose a different location, set the default location. Alternatively, use the [`@@location` system variable](https://docs.cloud.google.com/bigquery/docs/reference/system-variables) in your query. For more information, see [Specify locations](https://docs.cloud.google.com/bigquery/docs/locations#specify_locations).
  * `assertionSchema`: the BigQuery dataset in which Dataform creates views with assertion results, called `dataform_assertions` by default.




You can access the properties defined in the `dataform.json` file in your project code as properties of the [`dataform.projectConfig`](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference#iprojectconfig) object.

### Configure schema names

To configure schema names, you need to edit the `defaultDataset` and `defaultAssertionSchema` properties in the `workflow_settings.yaml` file, or the `defaultSchema` and `assertionSchema` properties in the `dataform.json` file.

To configure the name of a schema, follow these steps:

### `workflow_settings.yaml`

  1. In your development workspace, in the **Files** pane, click the `workflow_settings.yaml` file.

  2. Edit the value of `defaultDataset`, `defaultAssertionSchema`, or both.




The following code sample shows a custom `defaultDataset` name defined in the `workflow_settings.yaml` file:
    
    
      ...
      defaultDataset: mytables
      ...
    

### `dataform.json`

  1. In your development workspace, in the **Files** pane, click the `dataform.json` file.

  2. Edit the value of `defaultSchema`, `assertionSchema`, or both.




The following code sample shows a custom `defaultSchema` name defined in the `dataform.json` file:
    
    
    {
      ...
      "defaultSchema": "mytables",
      ...
    }
    

#### Create custom compilation variables

Compilation variables contain values that you can modify with compilation overrides in a release configuration or in a Dataform API request.

After you define a compilation variable in `workflow_settings.yaml` and add it to selected tables, you can modify its value in a release configuration or [Dataform API compilation overrides](https://docs.cloud.google.com/dataform/docs/configure-compilation#configure-compilation-overrides-with-api) to execute tables conditionally.

For more information about executing tables conditionally by using compilation variables, see [Introduction to code lifecycle in Dataform](https://docs.cloud.google.com/dataform/docs/configure-compilation#intro-code-lifecycle).

To create a compilation variable that you can use across a repository, follow these steps:

### `workflow_settings.yaml`

  1. Go to your Dataform development workspace.
  2. In the **Files** pane, select the `workflow_settings.yaml` file.
  3. Enter the following code snippet:
         
         "vars": {
           "VARIABLE":"VALUE"
         }
         

Replace the following:

     * `VARIABLE`: a name for the variable
     * `VALUE`: the default value of the compilation variable



The following code sample shows the `myVariableName` compilation variable set to `myVariableValue` in the `workflow_settings.yaml` file:
    
    
    ...
    vars:
      myVariableName: myVariableValue
    ...
    

The following code sample shows the `workflow_settings.yaml` file with the `executionSetting` compilation variable set to `dev`:
    
    
    defaultProject: default_bigquery_database
    defaultLocation: us-west1
    defaultDataset: dataform_data,
    vars:
    executionSetting: dev
    

### `dataform.json`

  1. Go to your Dataform development workspace.
  2. In the **Files** pane, select the `dataform.json` file.
  3. Enter the following code snippet:
         
         "vars": {
           "VARIABLE":"VALUE"
         }
         

Replace the following:

     * `VARIABLE`: a name for the variable
     * `VALUE`: the default value of the compilation variable



The following code sample shows the `myVariableName` compilation variable set to `myVariableValue` in the `dataform.json` file:
    
    
    {
      ...
      "vars": {
        "myVariableName": "myVariableValue"
      },
      ...
    }
    

The following code sample shows the `dataform.json` file with the `executionSetting` compilation variable set to `dev`:
    
    
    {
    "warehouse": "bigquery",
    "defaultSchema": "dataform_data",
    "defaultDatabase": "default_bigquery_database",
    "defaultLocation": "us-west-1",
    "vars": {
    "executionSetting":"dev"
    }
    }
    

##### Add a compilation variable to a table

To add a compilation variable to a SQLX table definition file, follow these steps:

  1. Go to your Dataform development workspace.
  2. In the **Files** pane, select a SQLX table definition file.
  3. In the file, enter a `when` clause in the following format:
         
         ${when(dataform.projectConfig.vars.VARIABLE === "SET_VALUE", "CONDITION")}
         

Replace the following:

     * `VARIABLE`: the name of your variable—for example `executionSetting`
     * `SET_VALUE`: a value for the variable—for example, `staging`
     * `CONDITION`: a condition for execution of the table



The following code sample shows a table definition SQLX file with a `when` clause and the `executionSetting` variable that executes 10% of data in the staging execution setting:
    
    
      select
        *
      from ${ref("data")}
      ${when(
        dataform.projectConfig.vars.executionSetting === "staging",
        "where mod(farm_fingerprint(id) / 10) = 0",
      )}
    

The following code sample shows a view definition SQLX file with a `when` clause and the `myVariableName` variable:
    
    
      config { type: "view" }
      SELECT ${when(
        dataform.projectConfig.vars.myVariableName === "myVariableValue",
        "myVariableName is set to myVariableValue!",
        "myVariableName is not set to myVariableValue!"
      )}
    

### Configure workflow-level defaults for Iceberg tables

You can provide workflow-level defaults for Apache Iceberg managed tables in the `workflow_settings.yaml` file. You can set default values for the bucket name, table folder root, and table folder subpath.

Dataform uses these default values to construct the storage URI for an Iceberg managed table if you don't set these values in the `config` block of the table definition file.

To configure workflow-level defaults for the tables, add the `defaultIcebergConfig` block with the following fields to your `workflow_settings.yaml` file:

  * `bucketName`: Optional. The default name for the Cloud Storage bucket.
  * `tableFolderRoot`: Optional. The default name for the first-level folder inside the Cloud Storage bucket.
  * `tableFolderSubpath`: Optional. The default name for a sub-folder within the `tableFolderRoot`.



The following code sample shows a `workflow_settings.yaml` file with workflow-level defaults for Iceberg managed tables:
    
    
    defaultProject: "defaultProject"
    defaultDataset: "defaultDataset"
    defaultLocation: "us-central1"
    defaultIcebergConfig:
      bucketName: "wsDefaultBucketName"
      tableFolderRoot: "wsDefaultTableFolderRoot"
      tableFolderSubpath: "wsDefaultTableFolderSubpath"
    

You can access these fields in your Dataform code as properties of the `ProjectConfig` object:
    
    
    dataform.ProjectConfig.defaultIcebergConfig.bucketName
    dataform.ProjectConfig.defaultIcebergConfig.tableFolderRoot
    dataform.ProjectConfig.defaultIcebergConfig.tableFolderSubpath
    

For more information, see [Create Apache Iceberg managed tables](https://docs.cloud.google.com/dataform/docs/create-tables#create-iceberg-table) and the [`iceberg` block properties](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference#iceberg).

### Migrate workflow settings to `workflow_settings.yaml`

To ensure your workflow settings file is compatible with future Dataform core framework versions, you should migrate your workflow settings from the `dataform.json` file to the `workflow_settings.yaml` file.

The `workflow_settings.yaml` file replaces the `dataform.json` file.

If Dataform core is the only dependency package in your repository, then the `workflow_settings.yaml` file also replaces the `package.json` file. For more information about replacing the `package.json` file with the `workflow_settings.yaml` file, see Manage the Dataform core package.

The following table shows mapping of workflow settings properties from the `dataform.json` file to the `workflow_settings.yaml` file:

Property in `dataform.json` | Property in `workflow_settings.yaml` | Description  
---|---|---  
`assertionSchema` | `defaultAssertionDataset` | Required. The default dataset for assertions.  
`defaultDatabase` | `defaultProject` | Optional. The default Google Cloud project name. If unset, Dataform uses the Google Cloud project in which the Dataform repository is located.  
`defaultLocation` | `defaultLocation` | Optional. The default BigQuery location where Dataform creates tables. If unset, Dataform determines the location based on the datasets that your SQL query references. For more information, see [Specify locations](https://docs.cloud.google.com/bigquery/docs/locations#specify_locations).  
`defaultSchema` | `defaultDataset` | Required. The default dataset.  
`databaseSuffix` | `projectSuffix` | Optional. The suffix to append to all Google Cloud project references.  
`schemaSuffix` | `datasetSuffix` | Optional. The suffix to append to all action datasets.  
`tablePrefix` | `namePrefix` | Optional. The prefix to prepend to all action names.  
`vars` | `vars` | Optional. User-defined variables that are made available to project code during compilation. An object containing a list of `key: value` pairs.  
`warehouse` | - | Required in `dataform.json`. Must be set to `bigquery`. Not available in `workflow_settings.yaml`.  
- | `dataformCoreVersion` | Not available in `dataform.json`. Installed in `workflow_settings.yaml` by default for new repositories. For more information, see Manage the Dataform core package.  
  
To migrate workflow settings to `workflow_settings.yaml`, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select a repository, and then select a workspace.

  3. In the **Files** pane, click add**Add** , and then click **Create file**.

  4. In the **Add a file path** field, enter `workflow_settings.yaml`.

  5. Click **Create file**.

  6. In the `workflow_settings.yaml` file, add the settings from your `dataform.json` file, mapped to the YAML format.

  7. In the **Files** pane, click the **More** menu next to `dataform.json`, and then click **Delete**.

  8. To confirm deletion of `dataform.json`, click **Delete**.




The following code sample shows workflow settings defined in a `dataform.json` file:
    
    
    {
      "warehouse": "bigquery",
      "defaultDatabase": "dataform-demos",
      "defaultLocation": "US",
      "defaultSchema": "dataform",
      "assertionSchema": "dataform_assertions",
      "vars": {
        "environmentName": "development"
      }
    }
    

The following code sample shows the preceding `dataform.json` file converted to `workflow_settings.yaml`:
    
    
    defaultProject: dataform-demos
    defaultLocation: US
    defaultDataset: dataform
    defaultAssertionDataset: dataform_assertions
    vars:
        environmentName: "development"
    

## Manage the Dataform core package

This section shows you how to manage the Dataform core framework dependency package and update it to the latest version.

Dataform core is the open source Dataform framework for developing workflows with SQL, SQLX, and JavaScript. As a best practice, always use the latest available version of the Dataform core framework. For information about releases of the Dataform core framework, see [Dataform releases on GitHub](https://github.com/dataform-co/dataform/releases).

### Manage Dataform core package location

When you initialize the first workspace in a repository, Dataform automatically sets Dataform core as a dependency package. As of [Dataform core `3.0.0`](https://github.com/dataform-co/dataform/releases/tag/3.0.0), Dataform installs the Dataform core package in the `workflow_settings.yaml` file by default. In earlier versions of Dataform core, Dataform core was set in the `package.json` file.

In Dataform core `3.0.0` and later, if Dataform core is the only package in your repository, then you should set it in the `workflow_settings.yaml` file. For repositories created with earlier versions of Dataform core, move the Dataform core package to `workflow_settings.yaml`.

The `package.json` file is required to install additional packages in Dataform. If your repository uses additional packages, set the Dataform core package in `package.json` so that all packages are set in one place. If your repository doesn't have the `package.json` file, create the `package.json` file and move the Dataform core package to install additional packages. The `package.json` file must be in the root directory of your repository.

#### Move Dataform core to `workflow_settings.yaml`

For repositories created with versions of Dataform core earlier than `3.0.0`, if you don't have dependency packages other than Dataform core, then you should move the Dataform core package from the `package.json` file to the `workflow_settings.yaml` file, and delete the redundant `package.json` file.

To migrate the Dataform core package from the `package.json` file to the `workflow_settings.yaml` file, do the following:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select a repository, and then select a workspace.

  3. In the **Files** pane, select the `workflow_settings.yaml` file.

  4. In the `workflow_settings.yaml` file, add the Dataform core package in the following format:
         
         dataformCoreVersion: "VERSION"
         
         

Replace `VERSION` with the latest version of Dataform, for example, `3.0.0`.

  5. In the **Files** pane, click the **More** menu next to the `package.json` file, and then click **Delete**.

  6. To confirm deletion of the `dataform.json` file, click **Delete**.

  7. Click **Install packages**.




#### Move Dataform core to `package.json`

The `package.json` file is required to [install additional packages](https://docs.cloud.google.com/dataform/docs/use-packages#install-package) in a repository. If your repository uses additional packages, then you should store all packages, including the Dataform core package, in the `package.json` file.

If your repository doesn't contain the `package.json` file because the Dataform core package is set in the `workflow_settings.yaml` file, you must create the `package.json` file to install additional packages, and then move the Dataform core package from the `workflow_settings.yaml` file to the newly created `package.json` file.

To create the `package.json` file and move the Dataform core package, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select a repository, and then select a workspace.

  3. In the **Files** pane, click add**Add** , and then click **Create file**.

  4. In the **Add a file path** field, enter `package.json`.

  5. Click **Create file**.

  6. In the `package.json` file, add the Dataform core package in the following format:
         
         {
             "dependencies": {
                 "@dataform/core": "VERSION"
             }
         }
         

Replace `VERSION` with the latest version of Dataform, for example, `3.0.0`.

  7. Click **Install packages**.

  8. In the **Files** pane, select `workflow_settings.yaml`.

  9. In the `workflow_settings.yaml` file, delete the `dataformCoreVersion` property.




### Update Dataform core

Always test new package versions in a non-production environment before deploying in your production environment.

To update the Dataform core dependency package, follow these steps:

  1. Look up the latest version of `@dataform/core` on the [Dataform releases page on GitHub](https://github.com/dataform-co/dataform/releases).

  2. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  3. Select a repository, and then select a workspace.

  4. In the **Files** pane, select the `package.json` file or the `workflow_settings.yaml` file.

The location where the Dataform core dependency package is set depends on your version of Dataform core and your use of packages. For more information, see Manage Dataform core package location.

  5. Update the Dataform core dependency package with the latest version:

### `package.json`
         
         {
             "dependencies": {
                 "@dataform/core": "VERSION"
             }
         }
         

Replace `VERSION` with the latest version of Dataform, for example, `3.0.0`. To prevent issues with package installation, explicitly specify the Dataform core package version. Don't use other [`dependencies` options](https://docs.npmjs.com/cli/v10/configuring-npm/package-json#dependencies) of the `package.json` file, for example, `>version`.

### `workflow_settings.yaml`
         
         dataformCoreVersion: "VERSION"
         

Replace `VERSION` with the latest version of Dataform, for example, `3.0.0`.

  6. Click **Install packages**.

  7. Commit the changes.

  8. Push the changes to your repository.




The following code sample shows the `@dataform/core` dependency updated to the `3.0.0` version in the `package.json` file:
    
    
    {
        "dependencies": {
            "@dataform/core": "3.0.0"
        }
    }
    

## Version control your code

This section shows you how to use version control in Dataform to keep track of development.

Dataform uses Git to keep track of each change made to the files inside a repository.

In a Dataform repository, you interact directly with the Git repository.

In a connected repository, you interact with the tracking branch of the remote repository that you configured while [connecting the repository](https://docs.cloud.google.com/dataform/docs/connect-repository).

Dataform displays version control options based on the status of changes in your development workspace. For example, Dataform displays the commit option only when there are uncommitted local changes in your workspace. When the files in your workspace are an exact copy of your default or tracking branch, Dataform displays the **Workspace is up to date** status.

Dataform displays the following version control options:

Commit X change(s)
    Commit the X number of local changes in your workspace or selected changed files. Dataform displays the uncommitted changes.
Push to default branch
    Push your committed changes to your default branch. This option is available in a Dataform repository if you have no uncommitted changes in your workspace.
Push to `your-branch-name`
    Push your committed changes to `your-branch-name`. This option is available in a repository [connected to a third-party Git repository](https://docs.cloud.google.com/dataform/docs/connect-repository) if you have no uncommitted changes in your workspace.
Pull from default branch
    Update your workspaces with recent changes from your default branch. This option is available in a Dataform repository if you have no uncommitted or unpushed committed changes in your workspace.
Pull from `your-branch-name`
    Update your workspace with recent changes from `your-branch-name`. This option is available in a repository [connected to a third-party Git repository](https://docs.cloud.google.com/dataform/docs/connect-repository) if you have no uncommitted or unpushed committed changes in your workspace.
Revert to last commit
    Restore the files in your workspace to their state from your last commit.

### Pull changes

If your development workspace is out of sync with your repository, Dataform displays the **Pull** option. To pull changes from your repository to your development workspace, follow these steps:

  1. On the **Dataform** page, select a repository.
  2. In the **Development workspaces** tab, select a development workspace.
  3. On the development workspace page, do the following: 
     1. If you are in a Dataform repository, click **Pull from default branch**.
     2. If you are in a repository [connected to a third-party Git repository](https://docs.cloud.google.com/dataform/docs/connect-repository), click **Pull from`your-branch-name`**.



### Commit changes

After you make a change in a development workspace, Dataform displays the **Commit** option. You can commit all local changes or selected files.

**Note:** Dataform defaults to using the authenticated Google Cloud user's email address for the commit author, but the Dataform API allows setting a custom email address for the commit author. This behavior is similar to the [`git commit --author` command](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---authorauthor) and affects only the Git commit history. The commit author identity is not cryptographically verified.

In the **New commit** dialog, Dataform displays the uncommitted changes.

To commit changes from your development workspace to your repository, follow these steps:

  1. On the **Dataform** page, select a repository.
  2. On the repository page, select a development workspace.
  3. On the development workspace page, click **Commit**.
  4. In the **New commit** pane, do the following:

     1. In the **Add a commit message** field, enter a description for your commit.
     2. Select the changed files that you want to commit.

If you don't select any files, Dataform commits all local changes. You can filter changed files by file state, filename, and path.

     3. Click **Commit All changes** , or **Commit X changes**.

The button name depends on your selection of files to commit.




### Push changes

Dataform displays the **Push** option after you commit changes. To push changes from your development workspace to your repository, follow these steps:

  1. On the **Dataform** page, select a repository.
  2. On the repository page, select a development workspace.
  3. Commit changes.
  4. On the development workspace page, do the following: 
     1. If you are in a Dataform repository, click **Push to default branch**.
     2. If you are in a repository [connected to a third-party Git repository](https://docs.cloud.google.com/dataform/docs/connect-repository), click **Push to`your-branch-name`**.



### Revert uncommitted changes

To revert uncommitted changes, follow these steps:

  1. On the **Dataform** page, select a repository.
  2. On the repository page, select a development workspace.
  3. Above the **Files** pane, click the **More** menu, and then select **Revert to last commit**.



### Resolve merge conflicts

A merge conflict can happen when a local change in your development workspace is incompatible with a change that has been made to the default tracking branch of your repository. Merge conflicts usually occur when multiple users simultaneously edit the same file.

You encounter a merge conflict usually when you pull from a branch after a different user has pushed a conflicting change to the same branch. You need to resolve a merge conflict manually by editing the affected file.

The following code sample shows a merge conflict displayed in a SQLX file:
    
    
        <<<<<<< HEAD
        SELECT 1 as CustomerOrders
        =======
        SELECT 1 as Orders
        >>>>>>> refs/heads/main
    

To resolve a merge conflict, follow these steps:

  1. In your development workspace, in the **Files** pane, select an affected file.
  2. Edit the file with your chosen changes.
  3. Commit changes.
  4. Optional: Push changes.



## Identifying repositories for BigQuery assets

Dataform repositories automatically created and managed by another BigQuery feature, such as notebooks or saved queries, are hidden in Dataform in Google Cloud console to reduce clutter and prevent accidental modification of feature-specific logic. These repositories might appear in Cloud Asset Inventory searches or IAM permission audits, but they don't appear in Dataform in Google Cloud console.

You can identify the origin of a Dataform repository by inspecting its resource labels. The following table describes the labels used by various BigQuery features:

Feature | Label key | Label value  
---|---|---  
[BigQuery repositories](https://docs.cloud.google.com/bigquery/docs/repository-intro) | `origin` | `bigquery-studio`  
[BigQuery Studio Git repositories](https://docs.cloud.google.com/bigquery/docs/git-repositories) | `origin` | `bigquery-studio-git-folder`  
[Data canvases](https://docs.cloud.google.com/bigquery/docs/data-canvas) | `single-file-asset-type` | `data_canvas`  
[Data preparations](https://docs.cloud.google.com/bigquery/docs/data-prep-introduction) | `single-file-asset-type` | `data_preparation` or `data_preparation_sqlx`  
[Notebooks](https://docs.cloud.google.com/bigquery/docs/notebooks-introduction) | `single-file-asset-type` | `notebook`  
[Pipelines](https://docs.cloud.google.com/bigquery/docs/pipelines-introduction) | `bigquery-workflow` | (Any value)  
[Saved queries](https://docs.cloud.google.com/bigquery/docs/saved-queries-introduction) | `single-file-asset-type` | `sql`  
  
To retrieve the labels from a repository that doesn't appear in Dataform, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Asset Inventory** page.

[Go to Asset Inventory](https://console.cloud.google.com/iam-admin/asset-inventory/)

  2. Click the **Resource** tab.

  3. In the **Filter results** pane, next to **Resource type** , click **View more** , and then enter `dataform.googleapis.com/Repository`.

  4. Select **`dataform.Repository`** and then click **Apply**.

  5. In the results table, locate your repository and check the **Labels** column. Match the labels found against the table describing the labels used by various BigQuery features to identify the source feature.




###  API 

To retrieve labels, use the [`projects.locations.repositories.get` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/get). Run the API request with the following information:

  * **Endpoint** : `GET https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID`



Alternatively, in your terminal, run the following `curl` command:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID"
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the region in which the Dataform resources are located.
  * `REPOSITORY_ID`: the unique identifier for the Dataform repository you're querying.



The [`projects.locations.repositories` resource](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories) that's returned in the response contains a labels map with the metadata used to identify the originating feature.

###  gcloud 

Run the following command in Google Cloud CLI to retrieve the labels for a specific repository:
    
    
    gcloud asset search-all-resources \
        --asset-types=dataform.googleapis.com/Repository \
        --query="name:projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID" \
        --format="yaml(labels)"
    

Replace the following:

  * `PROJECT_ID`: the unique identifier of your Google Cloud project.
  * `LOCATION`: the Google Cloud region where your repository is located.
  * `REPOSITORY_ID`: the unique identifier for your new Dataform repository.



To locate the resource corresponding to the output label, navigate to the matching feature page in Google Cloud console—for example, the **Notebooks** or **Data canvases** folders in the **Explorer** tab of the left pane in BigQuery Studio.

## What's next

  * To learn more about Dataform project settings, see [`IProjectConfig` reference](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference#iprojectconfig).
  * To learn how to install additional packages, see [Install a package in Dataform](https://docs.cloud.google.com/dataform/docs/use-packages#install-package).
  * To learn how to create a table, see [Create a table](https://docs.cloud.google.com/dataform/docs/define-table).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
