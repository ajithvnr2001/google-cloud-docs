---
url: https://docs.cloud.google.com/dataform/docs/troubleshooting/
title: Troubleshoot Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:41.135284+00:00
---

# Troubleshoot Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Troubleshoot Dataform Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to resolve issues with Dataform.

## Access to BigQuery is denied

The following error occurs when you trigger a pipeline invocation before granting Dataform access to BigQuery:
    
    
    Access Denied: Project PROJECT_ID: User does not have bigquery.jobs.create permission in project PROJECT_ID.
    

To resolve this error, [grant Dataform access to BigQuery](https://docs.cloud.google.com/dataform/docs/access-control#grant-dataform-required-access).

## Access token for a remote repository is rejected

The following error occurs when your authentication token for a connected third-party repository does not have access to that repository:
    
    
    The access token for remote repository REPOSITORY_NAME was rejected
    

To resolve this error, check required permissions in your Git provider and update the Secret Manager authentication token accordingly. For more information about authenticating third-party Git repositories in Dataform, see [Connect to a third-party Git repository](https://docs.cloud.google.com/dataform/docs/connect-repository).

## Secure Source Manager connection lacks Developer Connect proxy

The following error occurs when you link a Dataform repository to a Secure Source Manager [(Preview)](https://cloud.google.com/products#product-launch-stages) repository using a Developer Connect connection that does not have the proxy enabled:
    
    
    This repository uses a Secure Source Manager connection that does not have the Developer Connect proxy enabled. Dataform cannot access it. Select a different repository, or link a new repository using a connection with the proxy enabled.
    

To resolve this error, select a different repository, link a new repository using a connection with the proxy enabled, or update the existing Developer Connect connection to enable the proxy. For more information, see [Connect a remote repository using Developer Connect](https://docs.cloud.google.com/dataform/docs/connect-repository#dev-connect).

## BigQuery query concurrency limit is exceeded

The following error occurs when the number of concurrent queries run to BigQuery exceeds the [BigQuery query concurrency limit](https://docs.cloud.google.com/bigquery/quotas#query_jobs):
    
    
    Exceeded rate limits: too many concurrent queries for this project_and_region
    

To resolve this error, reduce the number of parallel queries to less than 250 in the following ways:

  * In Dataform, [categorize actions with tags](https://docs.cloud.google.com/dataform/docs/configure-additional-actions#add-execution-tags), and [run only selected tags](https://docs.cloud.google.com/dataform/docs/trigger-execution#run-actions-selected-tags) at a time.
  * In Dataform, introduce dependencies between actions.
  * In Dataform, divide executions of actions between different Google Cloud projects.



For instructions to resolve this error in BigQuery, see [Troubleshoot quota and limit errors](https://docs.cloud.google.com/bigquery/docs/troubleshoot-quotas#ts-concurrent-queries-quota).

## BigQuery quota is exceeded

The following error occurs when the number of API requests that Dataform sends to BigQuery exceeds the BigQuery quota:
    
    
    Quota exceeded: Your user_method exceeded quota for concurrent api requests
    per user per method.
    

To resolve this error, reduce the number of parallel queries to less than 250 in the following ways:

  * In Dataform, [categorize actions with tags](https://docs.cloud.google.com/dataform/docs/configure-additional-actions#add-execution-tags), and [run only selected tags](https://docs.cloud.google.com/dataform/docs/trigger-execution#run-actions-selected-tags) at a time.
  * In Dataform, introduce dependencies between actions.
  * In Dataform, divide executions of actions between different Google Cloud projects.



For instructions to resolve this error in BigQuery, see [Troubleshoot quota and limit errors](https://docs.cloud.google.com/bigquery/docs/troubleshoot-quotas#ts-concurrent-queries-quota).

## BigQuery pipeline invocation errors

The following errors occur during execution of a workflow to BigQuery:

  * Pipeline invocation errors that begin with [BigQuery error messages](https://docs.cloud.google.com/bigquery/docs/error-messages).



To resolve these errors, see [BigQuery error messages](https://docs.cloud.google.com/bigquery/docs/error-messages).

## Compilation is failing

The following errors occur during compilation due to size or number of compiled queries:

  * `Compilation timed out. Reduce the complexity of your project to ensure it can compile within limits.`
  * `Compilation exceeded its allowed heap memory limits. Reduce the complexity of your project to ensure it can compile within limits.`
  * `Compilation exceeded its allowed ArrayBuffer or string memory limits. Reduce the complexity of your project to ensure it can compile within limits.`
  * `Compilation cancelled because it exceeded size limits.`

**Note:** The `Compilation cancelled because it exceeded size limits.` error occurs when the total serialized size of the compiled workflow graph exceeds the 20 MB [compilation resource limit](https://docs.cloud.google.com/dataform/docs/quotas#compilation-limits). This size limit includes all compiled SQL queries, actions, and any compilation error messages. For more information about estimating your compiled graph size, see [Estimate the compilation resource usage of your repository](https://docs.cloud.google.com/dataform/docs/best-practices-repositories#estimate-comp-resource-usage-of-repo).

To resolve these errors, follow these steps:

  1. [Update Dataform core](https://docs.cloud.google.com/dataform/docs/manage-repository#manage-dataform-core-package) to the latest version.
  2. Inspect your workflow to identify and reduce inefficiencies.
  3. Reduce the size of SQL queries.
  4. Reduce the amount of JavaScript operations in memory, for example:
         
         config { config {type: "table" }}
         js {
             const tooBig = new Uint8Array(110_000_000);
         }
         SELECT ...
         

  5. [Split the repository](https://docs.cloud.google.com/dataform/docs/best-practices-repositories#splitting-repos).




For more information about Dataform compilation resource limits, see [Quotas and limits](https://docs.cloud.google.com/dataform/docs/quotas).

## Conflicting `includeDependentAssertions` properties

The following error occurs during compilation when the `includeDependentAssertions` parameter is set for the same action with different values within one file:
    
    
    Conflicting "includeDependentAssertions" properties are not allowed. Dependency
    dependencyName has different values set for this property.
    

To resolve this error, edit the file and remove conflicting repetitions of the `includeDependentAssertions` parameter.

For more information about using the `includeDependentAssertions` parameter to set assertions as dependencies, see [Set the assertions of a selected action as dependencies](https://docs.cloud.google.com/dataform/docs/dependencies#selected-action-assertions).

## Cross-project service account attachment is blocked

The following error occurs when you attempt to use a custom service account from a different project than your Dataform repository, and the operation is blocked by an organization policy constraint:
    
    
    The caller does not have permission to act as service account: SERVICE_ACCOUNT_EMAIL
    

To resolve this error, do the following:

  1. Identify the Google Cloud project where the custom service account is located.
  2. In that project, deactivate the `iam.disableCrossProjectServiceAccountUsage` organization policy constraint. For more information, see [Enable service accounts to be attached across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).
  3. Ensure that the caller principal has the [Service Account User role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the custom service account.



For more information, see [Handle cross-project service account attachment](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode#cross-project-sa-attachment).

## `@dataform/core` dependency errors

The following errors occur during compilation if the `dataform-core` dependency in `package.json` is outdated:
    
    
    Failed to resolve @dataform/core
    
    
    
    @dataform/core version should be X.X.X or newer
    

The `@dataform/core` dependency is required in the `package.json`. When you initialize the first workspace in your repository, Dataform automatically populates `package.json` with the current version of `@dataform/core`. You need to update `@dataform/core` to the latest version as it comes out.

To resolve these errors, [update `@dataform/core` to the latest version](https://docs.cloud.google.com/dataform/docs/manage-repository#manage-dataform-core-package).

## End user credentials permission denied

The following error occurs when you run your workload using user credentials for a Google Account, but Dataform doesn't have the necessary permissions:
    
    
    Dataform does not have the necessary permissions to run your workload using end user credentials. Error details: Account restricted: https://accounts.google.com/info/servicerestricted?...
    

This error can occur if your organization uses Context-Aware Access rules that restrict access to Google Cloud services based on user identity and context.

To resolve this error, you might need to update your Context-Aware Access configuration to allow Dataform to use Google Account user credentials. To do this, you need to exempt Dataform's OAuth client ID in your access level configuration. For details on exempting applications, see [Configure access levels for supported applications](https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups#define_configurations_for_specific_applications).

To obtain the OAuth client ID for Dataform, contact Cloud Customer Care.

## Failure to resolve `dataform.json`

The following error occurs when you initialize a Dataform workspace, but the initialization process fails to install all packages:
    
    
    Uncaught Error: Failed to resolve dataform.json
    

To resolve this error, in your workspace, open `package.json` and click **Install packages**.

## Failure to resolve `workflow_settings.yaml`

The following error occurs when you initialize a Dataform workspace, but the initialization process fails to install all packages:
    
    
    Uncaught Error: Failed to resolve workflow_settings.yaml
    

To resolve this error, in your workspace, open `workflow_settings.yaml` and click **Install packages**.

## `git+` package targets are not supported

The following error occurs when you define packages in `package.json` with targets prefixed with `git+`:
    
    
    'git+' prefixed package targets are not currently supported. However,
    in most cases they can be used via a '.tar.gz' suffixed target instead.
    

Dataform does not support package targets prefixed with `git+`.

To resolve this error, generate a `tar.gz` URL of the package and update the package target in `package.json`. For more information about installing packages in Dataform, see [Install a package](https://docs.cloud.google.com/dataform/docs/use-packages#install-package).

## Package installation times out

The following error occurs when the size of packages defined in `package.json` exceeds the [maximum size of NPM dependencies](https://docs.cloud.google.com/dataform/docs/quotas#compilation-limits):
    
    
    API request error: Package installation timed out
    

To resolve this error, remove redundant packages from `package.json`. Make sure the `package.json` file does not contain `@dataform/cli`, and that the total size of defined NPM dependencies does not exceed 200Mb.

If your [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration) reference Git commitishes, make sure that the `package.json` files at their targets are valid.

## Permission denied to act as a service account

The following error occurs when the principal performing the action lacks the `iam.serviceAccounts.actAs` permission on the effective service account:
    
    
    Permission denied: Principal CALLER_EMAIL is missing 'iam.serviceAccounts.actAs' permission on service account SERVICE_ACCOUNT_EMAIL.
    

This error can occur during the following actions:

  * Creating or updating a repository.
  * Creating or updating a workflow configuration.
  * Creating a workflow invocation.
  * Updating a release configuration.



To resolve this error, grant the [Service Account User role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) to the principal on the effective service account. For more information, see [Grant the required IAM roles](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode#grant-iam-roles).

## Private package registry cannot be reached

The following error occurs when Dataform authentication for a private package expires:
    
    
    Permission denied when fetching one or more npm packages. Please verify that
    private registry authentication details are valid for each npm registry
    

To resolve this error, verify that private registry authentication details are valid for each NPM registry. For more information, see [Authenticate a private package](https://docs.cloud.google.com/dataform/docs/use-packages#authenticate-private-package).

## Remote repository cannot be reached

One of the following errors occurs when Dataform cannot connect to your remote Git repository:
    
    
    Remote repository 'REMOTE_REPOSITORY_URL' could not be reached.
    
    
    
    Error during remote operation: SSH connection to remote repository 'REMOTE_REPOSITORY_URL' timed out.
    
    
    
    Error during remote operation: `Read timed out`.
    
    
    
    Error during remote operation: `Connection time out`.
    
    
    
    Error during remote operation: The remote repository 'REMOTE_REPOSITORY_URL' closed connection during remote operation.
    

The way to resolve these connection errors depends on whether the failure is permanent or transient.

### Permanent connection failures

If the error occurs consistently on every compilation attempt or during initial repository setup, the connection failure is permanent. The connection is not configured correctly or credentials have expired. To resolve this error, follow these steps:

  1. Confirm that your Git repository host is accessible from the public internet.
  2. If your remote Git repository is not accessible through the public internet, use [Developer Connect](https://docs.cloud.google.com/dataform/docs/connect-repository#dev-connect) to connect securely from Dataform.
  3. Validate that your authentication token or SSH keys are valid, unexpired, and have access to the repository.
  4. Follow all steps in [Connect to a third-party Git repository](https://docs.cloud.google.com/dataform/docs/connect-repository).



### Transient or intermittent connection failures

If the error occurs sporadically during scheduled executions or when multiple workflows trigger simultaneously, the connection failure is transient. Your external network connection to the remote repository may be temporarily unreliable.

To optimize production reliability and prevent transient connection errors, follow these best practices:

  1. **Avoid frequent commitish compilations in production** : Calling `CreateCompilationResult` directly on a Git commitish, such as `main` or a specific Git tag, requires Dataform to perform a fresh Git clone and install packages over the network on every execution. Triggering frequent commitish compilations across multiple pipelines increases external network dependency and execution latency.
  2. **Use release configurations** : For production execution, use [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration). A release configuration compiles your repository on a controlled schedule and saves the immutable compilation result. Downstream workflow executions use this cached result instantly without querying your external Git repository.
  3. **Stagger scheduled executions** : When scheduling multiple compilations or release triggers, stagger their cron schedules to distribute network load. For example, offset the schedules by 5–10 minutes instead of running all jobs at the same time.
  4. **Add retries in orchestration workflows** : When orchestrating Dataform compilations from external schedulers such as Managed Service for Apache Airflow, configure automated retries with exponential backoff on your operator to gracefully handle temporary network unreliability. For example, in an Airflow DAG using `DataformCreateCompilationResultOperator`, configure retries in the following way:


    
    
    from datetime import timedelta
    from airflow.providers.google.cloud.operators.dataform import (
        DataformCreateCompilationResultOperator,
    )
    
    create_compilation_result = DataformCreateCompilationResultOperator(
        task_id="create_compilation_result",
        project_id="PROJECT_ID",
        region="REGION",
        repository_id="REPOSITORY_ID",
        compilation_result={
            "git_commitish": "GIT_COMMITISH",
        },
        retries=5,
        retry_delay=timedelta(minutes=2),
        retry_exponential_backoff=True,
    )
    

## Repositories not visible in Dataform

Some Dataform repositories might appear in Cloud Asset Inventory searches or IAM permission audits, but they don't appear in Dataform in Google Cloud console.

To learn how to identify the origin of these repositories using labels, see [Identifying repositories for BigQuery assets](https://docs.cloud.google.com/dataform/docs/manage-repository#repositories-for-assets).

## Secret for a remote repository is inaccessible

The following error occurs when the Dataform service agent can't access your Secret Manager secret for a connected third-party repository:
    
    
    Dataform's service account is unable to reach the configured secret.
    Make sure the secret exists and is shared with your Dataform service account:
    SERVICE_ACCOUNT_ID.
    

To resolve this error, verify that the Dataform service agent has [access to the secret](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

## Service account not visible in the drop-down menu

When configuring a repository or workflow invocation, the **Service account** menu might not list an existing custom service account.

Dataform uses the Identity and Access Management API to list service accounts. This requires the `iam.serviceAccounts.list` permission at the project level.

To resolve this issue, do one of the following:

  * Click **Enter manually** and enter the service account ID.
  * Ask your project administrator to grant you the [View Service Accounts role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountViewer) (`roles/iam.serviceAccountViewer`) or another role that includes the `iam.serviceAccounts.list` permission on the project.



## Unknown argument: tags

The following error occurs when your version of the [Dataform CLI](https://docs.cloud.google.com/dataform/docs/use-dataform-cli) doesn't recognize the `tags` argument:
    
    
    Unknown argument: tags
    

To resolve this error, do the following:

  * Update the version of the [CLI](https://docs.cloud.google.com/dataform/docs/use-dataform-cli#update-dataform-cli) to `3.0.0` or later. Always test new package versions in a non-production environment before deploying in your production environment.
  * As a best practice, always use the latest available version of the Dataform core package.
  * Explicitly specify the package version in `package.json`, for example, `3.0.0`. Don't use other [`dependencies` options](https://docs.npmjs.com/cli/v10/configuring-npm/package-json#dependencies) of `package.json`, for example, `>version`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
