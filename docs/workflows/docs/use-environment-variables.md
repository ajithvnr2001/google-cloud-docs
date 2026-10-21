---
url: https://docs.cloud.google.com/workflows/docs/use-environment-variables/
title: Use environment variables \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:36.375992+00:00
---

# Use environment variables  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/use-environment-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Use environment variables Stay organized with collections  Save and categorize content based on your preferences. 

You can define [environment variables](https://wikipedia.org/wiki/Environment_variable) for Workflows at deployment time. For example, you can create a workflow that is dynamically configured depending on the environment to which it is deployed. Or, you can create a workflow that can be reused as a template and configured according to separately maintained environment variables.

Environment variables are set as arbitrary key and value string pairs that are accessible by your workflow at runtime. They are stored in the Workflows backend, are scoped to the workflow execution, and are immutable during the execution of a workflow.

All environment variables are bound to a deployment of a workflow, and can only be set or changed with a deployment. Creating or changing an environment variable requires a successful deployment. If a deployment fails for any reason, any changes to environment variables are _not_ applied.

You can add, update, or remove user-defined environment variables using the Google Cloud CLI.

## Reserved names

The [built-in environment variables](https://docs.cloud.google.com/workflows/docs/reference/environment-variables) defined for Workflows are reserved and can't be set.

Note that you can't use the following when defining environment variables for Workflows:

Key | Description  
---|---  
Empty (`''`) | Keys can't be an empty string.  
`GOOGLE_` | Keys can't contain the prefix `GOOGLE_`.  
`WORKFLOWS_` | Keys can't contain the prefix `WORKFLOWS_`.  
  
## Set environment variables

You can define new variables or replace existing variables when deploying a workflow. To make additive changes, in this document, see Update environment variables instead.

### Console

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, click add**Create**.

  3. On the **Create workflow** page, complete the appropriate fields to configure your workflow definition.

  4. In the **Environment variables (optional)** section, click **Add variable**.

  5. In the **Name 1** field, specify the variable name.

  6. In the **Value 1** field, specify the variable value.

  7. To add another variable, click **Add variable**.

  8. Click **Next**.

  9. After defining your workflow, to deploy it, click **Deploy**.




### gcloud

To set an environment variable, use the `--set-env-vars` flag:
    
    
    gcloud workflows deploy WORKFLOW_NAME \
        --set-env-vars KEY1=VALUE1

Replace the following:

  * `WORKFLOW_NAME`: the ID of your workflow.
  * `KEY1=VALUE1`: the environment variable name and its value; for example, `MONTH=January`.



### Terraform

To create a workflow, use the [`google_workflows_workflow` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workflows_workflow) and modify your `main.tf` file as shown in the sample. For more information, see [Create a workflow by using Terraform](https://docs.cloud.google.com/workflows/docs/create-workflow-terraform).

Use the `user_env_vars` argument to associate an environment variable with the workflow revision.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Set multiple environment variables

To set multiple environment variables, use a comma-separated list:
    
    
    gcloud workflows deploy WORKFLOW_NAME \
          --set-env-vars KEY1=VALUE1,KEY2=VALUE2

### Escape comma characters

Since the comma character (`,`) is used to delimit environment variables, if your variable values include commas, you must specify a different delimiter character, for example, `@`:
    
    
    gcloud workflows deploy WORKFLOW_NAME \
          --set-env-vars ^@^KEY1=VALUE1,VALUE2,VALUE3@KEY2=VALUE2

### Store variables in a file

To store your variables in a file (for example, under source control), use a YAML file and the `--env-vars-file` flag:
    
    
    gcloud workflows deploy WORKFLOW_NAME \
          --env-vars-file FILE_PATH

Replace `FILE_PATH` with the path to a local YAML file that lists the definitions for your environment variables. Note that the variable names and values must be strings. All existing environment variables are removed by Workflows before the new environment variables are added.

For example, the contents of the YAML file might be the following:
    
    
    KEY1: "value1"
    KEY2: "value2"

For more information about the `deploy` command, see [`gcloud workflows deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/deploy).

## Access environment variables

To access an environment variable, make a call to the [`sys.get_env()`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/get_env) function in an expression, passing the name of the environment variable as a parameter. The name of the environment variable must be passed as a string.

For example, the following workflow assigns the value of the environment variable `KEY1` to a workflow variable called `keyValue`, and then outputs that value:
    
    
    main:
      steps:
        - init:
            assign:
              - keyValue: ${sys.get_env("KEY1")}
        - returnResult:
            return: ${keyValue}

## Update environment variables

You can update user-defined environment variables for existing workflows. This is a non-destructive approach that changes or adds environment variables, but doesn't delete variables.

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click the name of the workflow you want to update.

The **Workflow details** page appears.

  3. To edit an existing environment variable, do either of the following:

     * Click the **Details** tab.

       1. Beside **Environment variables** , click the edit icon.
       2. Make your changes.
       3. To deploy the updated workflow, click **Save**.
     * Click edit **Edit**.

       1. In the **Environment variables (optional)** section, make your changes.
       2. To deploy the updated workflow, click **Next** and then **Deploy**.



### gcloud

To update a variable, use the `--update-env-vars` flag:
    
    
    gcloud workflows deploy WORKFLOW_NAME \
        --update-env-vars KEY1=VALUE1

To update multiple environment variables, use a comma-separated list:
    
    
    gcloud workflows deploy WORKFLOW_NAME \
        --update-env-vars KEY1=VALUE1,KEY2=VALUE2

## Delete environment variables

You can delete user-defined environment variables for existing workflows.

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click the name of the workflow you want to update.

The **Workflow details** page appears.

  3. To delete an existing environment variable, do either of the following:

     * Click the **Details** tab.

       1. Click the appropriate edit.
       2. Beside the environment variable that you want to delete, click the delete icon.
       3. To deploy the updated workflow, click **Save**.
     * Click edit **Edit**.

       1. Beside the environment variable that you want to delete, click the delete icon.
       2. To deploy the updated workflow, click **Next** and then **Deploy**.



### gcloud

If you want to selectively remove environment variables, use the `--remove-env-vars` flag:
    
    
    gcloud workflows deploy WORKFLOW_NAME \
        --remove-env-vars KEY1,KEY2

Alternatively, you can clear all previously set environment variables with the `--clear-env-vars` flag:
    
    
    gcloud workflows deploy WORKFLOW_NAME \
        --clear-env-vars

## Best practices

As a best practice, we recommend that you don't depend on or modify any environment variables that you haven't set explicitly. If you modify environment variables other than those that you have set explicitly, it might lead to unintended consequences.

### Managing secrets

Environment variables can be used to configure workflows, but are not recommended as a way to store and consume secrets such as database credentials or API keys. These sensitive values should be stored separately from both your source code and environment variables, and not inadvertently sent to logs.

For storing secrets, we recommend that you review the best practices for [secret management](https://docs.cloud.google.com/secret-manager/docs/best-practices), and follow the instructions to [use Secret Manager with Workflows](https://docs.cloud.google.com/workflows/docs/use-secret-manager).

### Naming conventions

As a general rule, we recommend that environment variable keys consist solely of uppercase letters, digits, and underscores (`_`), and that they don't begin with a digit. Consider prefixing your user-defined environment variables with a unique key to avoid conflicts with other variables.

### Size limits

A maximum of 20 user-defined environment variables can be defined. Each definition string (`KEY=value`) is limited to 4 KiB.

## What's next

  * [Execute a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow).
  * [Pass runtime arguments in an execution request](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
