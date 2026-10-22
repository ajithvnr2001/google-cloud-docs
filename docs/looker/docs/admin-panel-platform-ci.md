---
url: https://docs.cloud.google.com/looker/docs/admin-panel-platform-ci/
title: Admin settings - Continuous Integration \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:55.487320+00:00
---

# Admin settings - Continuous Integration  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-platform-ci/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Continuous Integration Stay organized with collections  Save and categorize content based on your preferences. 

The **Continuous Integration** page in the **Platform** section of the **Admin** menu lets you configure settings for the Looker [Continuous Integration (CI)](https://docs.cloud.google.com/looker/docs/continuous-integration) feature. Configure Looker (Google Cloud core) CI settings to ensure the quality and reliability of your LookML projects. CI prevents query errors and identifies issues with SQL, data tests, content, and LookML before they reach production. You can also configure CI validators to run automatically when a pull request is submitted to your LookML repository, streamlining your development workflow.

**Note:** For [Looker (Google Cloud core) instances](https://docs.cloud.google.com/looker/docs/looker-core-overview), Continuous Integration is supported on instances that are configured with [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) or with [private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) or [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip) that use [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc). In addition, Continuous Integration is supported on Looker (Google Cloud core) instances that are enabled for [CMEK](https://docs.cloud.google.com/looker/docs/looker-core-cmek) or that are within a [VPC Service Controls perimeter](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc). Continuous Integration is not supported on Looker (Google Cloud core) instances that are configured with private connections or hybrid connections that use [private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa).

## Compliance capabilities of Continuous Integration

Looker CI is not included in the [FedRAMP High, FedRAMP Moderate, or DoD Impact Level 5 (IL5) authorization boundaries](https://docs.cloud.google.com/assured-workloads/docs/control-packages#regulatory-data-boundaries).

Prior to enabling the Looker CI setting for your Looker instance, consult with your authorizing body to determine whether Looker CI's compliance offerings meet your organization's specific security and regulatory requirements.

For Looker (Google Cloud core) instances, each [Assured Workloads control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages) that becomes available will add Looker CI features as default offerings as that package's change requirements and processes are met.

## Enable Continuous Integration

The Looker [Continuous Integration (CI)](https://docs.cloud.google.com/looker/docs/continuous-integration) feature lets you run tests on your LookML project to deliver more reliable, efficient, and user-friendly data experiences. You can use the CI validators to identify issues with SQL, data tests, content, and LookML before they hit production to verify your LookML and prevent query errors for your users. You can also configure the CI validators to run automatically on a [schedule](https://docs.cloud.google.com/looker/docs/ci-create-suite#schedule-trigger) or [when a pull request is submitted](https://docs.cloud.google.com/looker/docs/ci-create-suite#pr-trigger) to your LookML repository.

A Looker admin can use the **Enable Continuous Integration** toggle to enable CI on your instance.

**Note:** For Looker (original) instances that use an [IP allowlist](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist) to specify a list of IP addresses that can access your Looker instance, you must manually add an IP address for Continuous Integration. [Contact Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) to get the IP address. (For Looker (Google Cloud core) instances that use an IP allowlist, CI functionality is housed within the Google Cloud network, so you don't need to manually add an IP address for CI.)

## Looker CI users

When you enable Continuous Integration on your instance, Looker automatically creates 10 Looker CI users in the [**Looker CI Users** user group](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#ci-users) with the [**Looker CI Users** role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#ci-users). A Looker admin can view the Looker CI users from the **Service Accounts** tab of the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) Admin page.

If your instance uses [access grants](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) to control access to Explores, the Looker CI users must be included in those access grants. You can include the CI users by assigning the relevant user attribute values to the **Looker CI Users** group, as described on the [Admin settings - User attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#assigning_values_to_user_groups) documentation page.

## Integrations

Continuous Integration lets you run CI suites automatically when pull requests or commits occur in your remote Git repository. You can configure Continuous Integration to integrate with the following Git providers:

  * GitHub (use the Looker CI GitHub app)
  * GitLab (use the Looker API and GitLab CI)
  * Bitbucket (use the Looker API and Bitbucket Pipelines)
  * GitHub Actions (use the Looker API and GitHub Actions)



### GitHub

If you have a cloud-based GitHub repository as a remote repository for your LookML project, you can configure Continuous Integration to [automatically run CI suites when LookML developers submit pull requests to your LookML repository](https://docs.cloud.google.com/looker/docs/ci-create-suite#triggers).

**Note:** Continuous Integration supports only cloud-based GitHub and doesn't support self-hosted GitHub Enterprise servers. In addition, CI doesn't support GitHub Enterprise configurations that use single sign-on (SSO) for login or that use GitHub's IP allowlist feature.

For Looker (Google Cloud core) instances that use [private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) or [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip) with Private Service Connect, or for instances within a [VPC Service Controls perimeter](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc), your networking configuration must allow ingress and egress traffic to and from GitHub. In most cases, this networking configuration is already set up when you configure your Looker (Google Cloud core) instance to connect to GitHub. For more information about configuring outbound connections, see the [Looker (Google Cloud core) outbound access to external services using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-southbound) documentation page.

To automatically run CI suites on your repository, Continuous Integration needs the following permissions:

  * Read access to your repository's metadata and pull requests
  * Read and write access to your repository's commit statuses, repository hooks, and workflows



These permissions are not set up when you set up a Git connection for your LookML project in the Looker IDE. If you want to use pull request triggering for CI runs, your LookML project must be set up with a Git connection (as described on the [Setting up and testing a Git connection](https://docs.cloud.google.com/looker/docs/setting-up-git-connection) page), and you must also configure the CI GitHub app as described in the Configuring the CI GitHub app section.

#### GitHub table

The **GitHub** table on the **Continuous Integration** Admin page lists the GitHub repositories that are configured for the LookML projects on your Looker instance. These GitHub repositories were configured by your LookML developers as described on the [Setting up and testing a Git connection](https://docs.cloud.google.com/looker/docs/setting-up-git-connection) documentation page.

For each GitHub repository that's listed, the table shows whether the repository has been configured with the CI GitHub app:

  * **Installed** : The repository has been granted the Looker CI GitHub application which enables [CI to be automatically run when LookML developers submit pull requests to your LookML repository](https://docs.cloud.google.com/looker/docs/ci-create-suite#triggers).
  * **Not Installed** : The repository hasn't been set up for pull request integration with Looker CI. To configure the repository for CI pull request integration, see the Configuring the CI GitHub app section.



#### Configuring the CI GitHub app

To grant the CI GitHub application for a repository, follow these steps:

  1. On the **Continuous Integration** Admin page in Looker, click the **Configure GitHub App** button. This will open a browser window to the GitHub apps webpage.
  2. Select the GitHub account where your LookML is stored.
  3. In the **Repository access** section, select **All repositories** to allow CI integrations for all of the Git repositories owned by the resource owner, or select **Only select repositories** to choose the repositories with which you want to use Continuous Integration.
  4. Click **Save**.



If the Looker CI GitHub application is successfully granted to the repository, Looker displays **Installed** for the repository in the **GitHub** table on the **Continuous Integration** Admin page.

### GitLab

You can trigger Looker Continuous Integration runs from GitLab CI by using the Looker API and the official Looker Python SDK (`looker-sdk`).

To trigger a Looker CI run from a GitLab CI pipeline, complete the following steps:

  1. Configure CI/CD variables in GitLab.
  2. Create the Python script for GitLab CI.
  3. Configure the GitLab CI workflow.



#### Configure CI/CD variables in GitLab

In your GitLab project, go to **Settings > CI/CD > Variables** and create the following CI/CD variables. Set each variable to **Masked** to protect sensitive values:

  * `LOOKERSDK_BASE_URL`: the API URL of your Looker instance (for example, `https://example.cloud.looker.com`)
  * `LOOKERSDK_CLIENT_ID`: the API3 Client ID generated from the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#api_keys) Admin page in Looker
  * `LOOKERSDK_CLIENT_SECRET`: the corresponding API3 Client Secret generated from the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#api_keys) Admin page in Looker



#### Create the Python script for GitLab CI

Create a Python script named `run_looker_ci.py` in your repository. This script uses the Looker SDK to trigger the CI run and poll until the run finishes:
    
    
    import os
    import sys
    import time
    import looker_sdk
    from looker_sdk import models as mdls
    
    # Retrieve required settings from environment variables
    project_id = os.getenv("LOOKER_PROJECT_ID")
    suite_id = os.getenv("LOOKER_SUITE_ID")
    
    # GitLab CI specific environment variables
    branch = os.getenv("CI_COMMIT_REF_NAME")
    commit = os.getenv("CI_COMMIT_SHA")
    
    if not all([project_id, suite_id, branch, commit]):
        print("Error: Missing required environment variables (LOOKER_PROJECT_ID, LOOKER_SUITE_ID, or GitLab vars).")
        sys.exit(1)
    
    # Initialize the Looker SDK.
    # The SDK automatically picks up LOOKERSDK_BASE_URL, LOOKERSDK_CLIENT_ID, and LOOKERSDK_CLIENT_SECRET.
    print("Initializing Looker SDK...")
    try:
        sdk = looker_sdk.init40()
    except Exception as e:
        print(f"Failed to initialize Looker SDK: {e}")
        sys.exit(1)
    
    # Configure the request body
    print(f"Starting Looker CI run for project '{project_id}', suite '{suite_id}'...")
    print(f"Branch: {branch} | Commit: {commit}")
    
    request_body = mdls.CreateContinuousIntegrationRunRequest(
        suite_id=suite_id,
        branch=branch,
        commit=commit
    )
    
    # Trigger the CI run
    try:
        run = sdk.create_continuous_integration_run(
            project_id=project_id,
            body=request_body
        )
        run_id = getattr(run, "run_id", getattr(run, "id", None))
        print(f"Looker CI run created successfully. Run ID: {run_id}")
    except looker_sdk.error.SDKError as e:
        print(f"Failed to create Looker CI run: {e}")
        sys.exit(1)
    
    # Poll for completion
    run_status = run.status
    terminal_statuses = ["cancelled", "error", "passed", "failed"]
    
    while run_status not in terminal_statuses:
        print(f"Run {run_id} status is '{run_status}'. Waiting 15 seconds...")
        time.sleep(15)
        
        try:
            run = sdk.get_continuous_integration_run(
                project_id=project_id,
                run_id=run_id
            )
            run_status = run.status
        except looker_sdk.error.SDKError as e:
            print(f"Error while polling Looker CI run status: {e}")
            sys.exit(1)
    
    print(f"Final Looker CI run status: {run_status}")
    
    if run_status != "passed":
        print("Looker CI run did not pass. Failing the GitLab CI job.")
        sys.exit(1)
    
    print("Looker CI run passed successfully!")
    

#### Configure the GitLab CI workflow

In the root directory of your repository, create or update your `.gitlab-ci.yml` pipeline configuration file to install `looker-sdk` and execute `run_looker_ci.py`:
    
    
    stages:
      - test
    
    looker-ci:
      stage: test
      image: python:3.10
      variables:
        LOOKER_PROJECT_ID: "LOOKER_PROJECT_ID"
        LOOKER_SUITE_ID: "LOOKER_SUITE_ID"
      script:
        - pip install looker-sdk
        - python run_looker_ci.py
      rules:
        - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    

Replace the following:

  * `LOOKER_PROJECT_ID`: the ID of the Looker project that you want to test
  * `LOOKER_SUITE_ID`: the ID of the CI suite that you want to run



### Bitbucket

You can trigger Looker Continuous Integration runs from Bitbucket Pipelines by using the Looker API and the official Looker Python SDK (`looker-sdk`).

To trigger a Looker CI run from Bitbucket Pipelines, complete the following steps:

  1. Configure repository variables in Bitbucket.
  2. Create the Python script for Bitbucket Pipelines.
  3. Configure the Bitbucket Pipelines workflow.



#### Configure repository variables in Bitbucket

In your Bitbucket repository, go to **Repository settings > Repository variables** and create the following repository variables. Set each variable to **Secured** to protect sensitive values:

  * `LOOKERSDK_BASE_URL`: the API URL of your Looker instance (for example, `https://example.cloud.looker.com`)
  * `LOOKERSDK_CLIENT_ID`: the API3 Client ID generated from the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#api_keys) Admin page in Looker
  * `LOOKERSDK_CLIENT_SECRET`: the corresponding API3 Client Secret that's generated from the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#api_keys) Admin page in Looker



#### Create the Python script for Bitbucket Pipelines

Create a Python script named `run_looker_ci.py` in your repository. This script uses the Looker SDK to trigger the CI run and poll until the run finishes:
    
    
    import os
    import sys
    import time
    import looker_sdk
    from looker_sdk import models as mdls
    
    # Retrieve required settings from environment variables
    project_id = os.getenv("LOOKER_PROJECT_ID")
    suite_id = os.getenv("LOOKER_SUITE_ID")
    
    # Bitbucket Pipelines specific environment variables
    branch = os.getenv("BITBUCKET_BRANCH")
    commit = os.getenv("BITBUCKET_COMMIT")
    
    if not all([project_id, suite_id, branch, commit]):
        print("Error: Missing required environment variables (LOOKER_PROJECT_ID, LOOKER_SUITE_ID, or Bitbucket vars).")
        sys.exit(1)
    
    # Initialize the Looker SDK.
    # The SDK automatically picks up LOOKERSDK_BASE_URL, LOOKERSDK_CLIENT_ID, and LOOKERSDK_CLIENT_SECRET.
    print("Initializing Looker SDK...")
    try:
        sdk = looker_sdk.init40()
    except Exception as e:
        print(f"Failed to initialize Looker SDK: {e}")
        sys.exit(1)
    
    # Configure the request body
    print(f"Starting Looker CI run for project '{project_id}', suite '{suite_id}'...")
    print(f"Branch: {branch} | Commit: {commit}")
    
    request_body = mdls.CreateContinuousIntegrationRunRequest(
        suite_id=suite_id,
        branch=branch,
        commit=commit
    )
    
    # Trigger the CI run
    try:
        run = sdk.create_continuous_integration_run(
            project_id=project_id,
            body=request_body
        )
        run_id = getattr(run, "run_id", getattr(run, "id", None))
        print(f"Looker CI run created successfully. Run ID: {run_id}")
    except looker_sdk.error.SDKError as e:
        print(f"Failed to create Looker CI run: {e}")
        sys.exit(1)
    
    # Poll for completion
    run_status = run.status
    terminal_statuses = ["cancelled", "error", "passed", "failed"]
    
    while run_status not in terminal_statuses:
        print(f"Run {run_id} status is '{run_status}'. Waiting 15 seconds...")
        time.sleep(15)
        
        try:
            run = sdk.get_continuous_integration_run(
                project_id=project_id,
                run_id=run_id
            )
            run_status = run.status
        except looker_sdk.error.SDKError as e:
            print(f"Error while polling Looker CI run status: {e}")
            sys.exit(1)
    
    print(f"Final Looker CI run status: {run_status}")
    
    if run_status != "passed":
        print("Looker CI run did not pass. Failing the Bitbucket Pipeline.")
        sys.exit(1)
    
    print("Looker CI run passed successfully!")
    

#### Configure the Bitbucket Pipelines workflow

In the root directory of your repository, create or update your `bitbucket-pipelines.yml` file to install `looker-sdk` and execute `run_looker_ci.py`:
    
    
    image: python:3.10
    
    pipelines:
      pull-requests:
        '**':
          - step:
              name: Looker CI
              script:
                - export LOOKER_PROJECT_ID="LOOKER_PROJECT_ID"
                - export LOOKER_SUITE_ID="LOOKER_SUITE_ID"
                - pip install looker-sdk
                - python run_looker_ci.py
    

Replace the following:

  * `LOOKER_PROJECT_ID`: the ID of the Looker project that you want to test
  * `LOOKER_SUITE_ID`: the ID of the CI suite that you want to run



### GitHub Actions

You can trigger Looker Continuous Integration runs from GitHub Actions by using the Looker API and the official Looker Python SDK (`looker-sdk`).

To trigger a Looker CI run from a GitHub Actions workflow, complete the following steps:

  1. Configure repository secrets in GitHub.
  2. Create the Python script for GitHub Actions.
  3. Configure the GitHub Actions workflow.



#### Configure repository secrets in GitHub

In your GitHub repository, go to **Settings > Secrets and variables > Actions** and create the following repository secrets:

  * `LOOKERSDK_BASE_URL`: the API URL of your Looker instance (for example, `https://example.cloud.looker.com`)
  * `LOOKERSDK_CLIENT_ID`: the API3 Client ID generated from the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#api_keys) Admin page in Looker
  * `LOOKERSDK_CLIENT_SECRET`: the corresponding API3 Client Secret that's generated from the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#api_keys) Admin page in Looker



#### Create the Python script for GitHub Actions

Create a Python script named `run_looker_ci.py` in your repository. This script uses the Looker SDK to trigger the CI run and poll until the run finishes:
    
    
    import os
    import sys
    import time
    import looker_sdk
    from looker_sdk import models as mdls
    
    # Retrieve required settings from environment variables
    project_id = os.getenv("LOOKER_PROJECT_ID")
    suite_id = os.getenv("LOOKER_SUITE_ID")
    
    # GitHub Actions specific environment variables
    # GITHUB_HEAD_REF is the branch name for PRs. 
    # GITHUB_REF_NAME can be used as a fallback for non-PR events.
    branch = os.getenv("GITHUB_HEAD_REF") or os.getenv("GITHUB_REF_NAME")
    # GITHUB_PR_SHA is the head commit SHA for PRs.
    # GITHUB_SHA can be used as a fallback for non-PR events.
    commit = os.getenv("GITHUB_PR_SHA") or os.getenv("GITHUB_SHA")
    
    if not all([project_id, suite_id, branch, commit]):
        print("Error: Missing required environment variables (LOOKER_PROJECT_ID, LOOKER_SUITE_ID, or GitHub vars).")
        sys.exit(1)
    
    # Initialize the Looker SDK.
    # The SDK automatically picks up LOOKERSDK_BASE_URL, LOOKERSDK_CLIENT_ID, and LOOKERSDK_CLIENT_SECRET.
    print("Initializing Looker SDK...")
    try:
        sdk = looker_sdk.init40()
    except Exception as e:
        print(f"Failed to initialize Looker SDK: {e}")
        sys.exit(1)
    
    # Configure the request body
    print(f"Starting Looker CI run for project '{project_id}', suite '{suite_id}'...")
    print(f"Branch: {branch} | Commit: {commit}")
    
    request_body = mdls.CreateContinuousIntegrationRunRequest(
        suite_id=suite_id,
        branch=branch,
        commit=commit
    )
    
    # Trigger the CI run
    try:
        run = sdk.create_continuous_integration_run(
            project_id=project_id,
            body=request_body
        )
        run_id = getattr(run, "run_id", getattr(run, "id", None))
        print(f"Looker CI run created successfully. Run ID: {run_id}")
    except looker_sdk.error.SDKError as e:
        print(f"Failed to create Looker CI run: {e}")
        sys.exit(1)
    
    # Poll for completion
    run_status = run.status
    terminal_statuses = ["cancelled", "error", "passed", "failed"]
    
    while run_status not in terminal_statuses:
        print(f"Run {run_id} status is '{run_status}'. Waiting 15 seconds...")
        time.sleep(15)
        
        try:
            run = sdk.get_continuous_integration_run(
                project_id=project_id,
                run_id=run_id
            )
            run_status = run.status
        except looker_sdk.error.SDKError as e:
            print(f"Error while polling Looker CI run status: {e}")
            sys.exit(1)
    
    print(f"Final Looker CI run status: {run_status}")
    
    if run_status != "passed":
        print("Looker CI run did not pass. Failing the GitHub Action.")
        sys.exit(1)
    
    print("Looker CI run passed successfully!")
    

#### Configure the GitHub Actions workflow

In your repository, create a workflow file at `.github/workflows/looker-ci.yml` with the following configuration:
    
    
    name: Looker CI
    on:
      pull_request:
        branches:
          - main
    
    jobs:
      run-looker-ci:
        runs-on: ubuntu-latest
    
    
        env:
          # Automatically picked up by the Looker SDK
          LOOKERSDK_BASE_URL: ${{ secrets.LOOKERSDK_BASE_URL }}
          LOOKERSDK_CLIENT_ID: ${{ secrets.LOOKERSDK_CLIENT_ID }}
          LOOKERSDK_CLIENT_SECRET: ${{ secrets.LOOKERSDK_CLIENT_SECRET }}
    
    
          # Passed directly to the script
          LOOKER_PROJECT_ID: "LOOKER_PROJECT_ID"
          LOOKER_SUITE_ID: "LOOKER_SUITE_ID"
          GITHUB_PR_SHA: ${{ github.event.pull_request.head.sha }}
    
        steps:
          - name: Checkout Code
            uses: actions/checkout@v4
    
          - name: Set up Python
            uses: actions/setup-python@v5
            with:
              python-version: '3.10'
    
          - name: Install Dependencies
            run: |
              python -m pip install --upgrade pip
              pip install looker-sdk
    
          - name: Run Looker CI
            run: python run_looker_ci.py
    

Replace the following:

  * `LOOKER_PROJECT_ID`: the ID of the Looker project that you want to test
  * `LOOKER_SUITE_ID`: the ID of the CI suite that you want to run



## dbt Cloud Configuration

If you use [dbt Cloud](https://docs.getdbt.com/docs/deploy/continuous-integration?version=2.0), you can configure Continuous Integration to [automatically run CI suites when a dbt Cloud CI job finishes](https://docs.cloud.google.com/looker/docs/ci-create-suite#dbt-trigger). The CI suite run helps ensure that changes to your dbt models don't break your LookML project.

**Note:** For Looker (Google Cloud core) instances that use [private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) or [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip) with Private Service Connect, or for instances within a [VPC Service Controls perimeter](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc), you must update your networking configuration to allow ingress and egress traffic to and from your dbt Cloud host URL. For more information about configuring outbound connections, see the [Looker (Google Cloud core) outbound access to external services using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-southbound) documentation page.

To configure the dbt Cloud integration, follow these steps in the **dbt Cloud Configuration** section:

  1. In the **dbt Cloud Host URL** field, enter the URL to your dbt Cloud account.
  2. In the **dbt Cloud API Key** field, enter a [dbt Cloud service account token](https://docs.getdbt.com/docs/dbt-apis/service-tokens?version=2.0#generate-service-account-tokens).
  3. Click **Test Connection**. Looker will verify that it can connect to your dbt Cloud account and then retrieve your **dbt Cloud Account ID**.
  4. Click **Save**.



### User Attributes

You can configure user attributes that Continuous Integration can override during validation runs. User attributes are used in conjunction with the dbt Cloud integration to point Looker to temporary schemas created by dbt Cloud CI jobs.

To configure user attribute defaults for CI, follow these steps in the **User Attributes** section:

  1. In the **User Attribute** field, select a user attribute from the drop-down list. If no user attribute is selected, Looker will use the user attribute that's defined in the [**Primary Dataset**](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#dataset) field in your [database connection](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) for CI runs.
  2. In the **Value for CI run** field, enter the value that should be used with this user attribute for CI runs.
  3. Click **Save**.



You can add multiple user attribute and value pairs. Each user attribute configured in the **User Attributes** section will be available for selection as an override in your [CI Suite configurations](https://docs.cloud.google.com/looker/docs/ci-create-suite#dbt-trigger).

To delete a user attribute and value pair, click **Remove**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
