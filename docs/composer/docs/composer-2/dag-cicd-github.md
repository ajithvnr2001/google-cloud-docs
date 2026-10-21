---
url: https://docs.cloud.google.com/composer/docs/composer-2/dag-cicd-github/
title: Test, synchronize, and deploy your DAGs from GitHub \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:04.961011+00:00
---

# Test, synchronize, and deploy your DAGs from GitHub  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/dag-cicd-github/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Test, synchronize, and deploy your DAGs from GitHub Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/dag-cicd-github "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/dag-cicd-github "View this page for Managed Airflow \(Legacy Gen 1\)")

This guide explains how to create a CI/CD pipeline to test, synchronize, and deploy DAGs to your Managed Airflow environment from your GitHub repository.

If you want to only synchronize data from other services, see [Transfer data from other services](https://docs.cloud.google.com/composer/docs/composer-2/transfer-data-with-transfer-operators).

## CI/CD pipeline overview

[ ![Architecture diagram showing the steps of the flow. The presubmit and PR review are in the GitHub section, and the DAG sync and manual DAG verification are in the Google Cloud section.](https://docs.cloud.google.com/static/composer/docs/images/dag-cicd-integration-architecture.png)](https://docs.cloud.google.com/static/composer/docs/images/dag-cicd-integration-architecture.png) **Figure 1.** Architecture diagram showing the steps of the flow (click to enlarge) 

The CI/CD pipeline that to test, synchronize, and deploys DAGs has the following steps:

  1. You make a change to a DAG and push that change to a development branch in your repository.

  2. You open a pull request against the main branch of your repository.

  3. Cloud Build runs unit tests to check that your DAG is valid.

  4. Your pull request is approved and merged to the main branch of your repository.

  5. Cloud Build synchronizes your development Managed Airflow environment with these new changes.

  6. You verify that the DAG works as expected in your development environment.

  7. If your DAG works as expected, you upload the DAG to your production Managed Airflow environment.




## Objectives

  * Run an automated presubmit check using Cloud Build. This check runs unit tests for a DAG.
  * Synchronize DAGs in your development Managed Service for Apache Airflow environment with DAGs in your GitHub repository.



## Before you begin

  * This guide assumes that you are working with two identical Managed Airflow environments: a development environment and a production environment.

For the purposes of this guide, you are configuring a CI/CD pipeline only for the development environment. Make sure that the environment you use isn't a production environment.

  * This guide assumes that you have your DAGs and their tests stored in a GitHub repository.

The [example CI/CD pipeline](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/composer/cicd_sample) demonstrates the contents of an example repository. DAGs and tests are stored in the `dags/` directory, with requirements files, the constraints file, and Cloud Build configuration files stored at the top level. The DAG synchronization utility and its requirements are located in the `utils` directory.




## Create a presubmit check job and unit tests

The first Cloud Build job runs a presubmit check, which executes unit tests for your DAGs.

### Add unit tests

If you haven't already, author [unit tests](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#unit-tests) for your DAGs. Save these tests alongside the DAGs in your repository, each with the `_test` suffix. For example, the test file for the DAG in `example_dag.py` is `example_dag_test.py`. These are the tests that run as a presubmit check in your repository.

### Create Cloud Build YAML configuration for the presubmit check

In your repository, create a YAML file named `test-dags.cloudbuild.yaml` that configures your Cloud Build job for presubmit checks. In it, there are three steps:

  1. Install the dependencies needed by your DAGs.
  2. Install the dependencies needed by your unit tests.
  3. Execute the DAG tests.


    
    
    steps:
      # install dependencies
      - name: python:3.8-slim
        entrypoint: pip
        args: ["install", "-r", "requirements.txt", "-c", "constraints.txt", "--user"]
    
      - name: python:3.8-slim
        entrypoint: pip
        args: ["install", "-r", "requirements-test.txt", "--user"]
    
      # run in python 3.8 which is latest version in Cloud Composer
      - name: python:3.8-slim
        entrypoint: python3.8
        args: ["-m", "pytest", "-s", "dags/"]
    

**Note:** Cloud Build pulls the Python image from Docker Hub and you can specify the [tag](https://hub.docker.com/_/python?tab=tags) in the `name` field of each step. If you are using `python` as your `entrypoint`, make sure that your `entrypoint` matches the version specified in your tag, otherwise `entrypoint` defaults to `latest`. 

### Create the Cloud Build trigger for the presubmit check

Follow the [Building repositories from GitHub](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-github) guide to create a GitHub app based trigger with the following configurations:

  * **Name** : `test-dags`

  * **Event** : Pull Request

  * **Source** \- Repository: choose your repository

  * **Source** \- Base branch: `^main$` (change `main` to the name of your repository's base branch, if required)

  * **Source** \- Comment Control: not required

**Caution:** Setting Comment Control to be not required means that any user can submit a Pull Request that triggers the build. For larger repositories or repositories with untrusted contributors, requiring Comment Control is recommended.
  * **Build Configuration** \- Cloud build configuration file: `/test-dags.cloudbuild.yaml` (the path to your build file)




## Create a DAG sync job and add DAGs utility script

Next, configure a Cloud Build job that runs a DAGs utility script. The utility script in this job synchronizes your DAGs with your Managed Airflow environment after they are merged to the main branch in your repository.

**Note:** Managed Airflow parses all DAGs on a repeated interval. This happens even if DAGs didn't change since the last parse. Because of this behavior, this utility uploads all DAGs to Managed Airflow, not just those that have changed.

### Add the DAGs utility script

Add the DAG utility script to your repository. This utility script copies all DAG files in the `dags/` directory of your repository to a temporary directory, ignoring all non-DAG Python files. The script then uses the Cloud Storage client library to upload all files from that temporary directory to the `dags/` directory in your Managed Airflow environment's bucket.
    
    
    from __future__ import annotations
    
    import argparse
    import glob
    import os
    from shutil import copytree, ignore_patterns
    import tempfile
    
    # Imports the Google Cloud client library
    from google.cloud import storage
    
    
    def _create_dags_list(dags_directory: str) -> tuple[str, list[str]]:
        temp_dir = tempfile.mkdtemp()
    
        # ignore non-DAG Python files
        files_to_ignore = ignore_patterns("__init__.py", "*_test.py")
    
        # Copy everything but the ignored files to a temp directory
        copytree(dags_directory, f"{temp_dir}/", ignore=files_to_ignore, dirs_exist_ok=True)
    
        # The only Python files left in our temp directory are DAG files
        # so we can exclude all non Python files
        dags = glob.glob(f"{temp_dir}/*.py")
        return (temp_dir, dags)
    
    
    def upload_dags_to_composer(
        dags_directory: str, bucket_name: str, name_replacement: str = "dags/"
    ) -> None:
        """
        Given a directory, this function moves all DAG files from that directory
        to a temporary directory, then uploads all contents of the temporary directory
        to a given cloud storage bucket
        Args:
            dags_directory (str): a fully qualified path to a directory that contains a "dags/" subdirectory
            bucket_name (str): the GCS bucket of the Cloud Composer environment to upload DAGs to
            name_replacement (str, optional): the name of the "dags/" subdirectory that will be used when constructing the temporary directory path name Defaults to "dags/".
        """
        temp_dir, dags = _create_dags_list(dags_directory)
    
        if len(dags) > 0:
            # Note - the GCS client library does not currently support batch requests on uploads
            # if you have a large number of files, consider using
            # the Python subprocess module to run gcloud storage cp --recursive on your dags
            # See https://cloud.google.com/storage/docs/gsutil/commands/cp for more info
            storage_client = storage.Client()
            bucket = storage_client.bucket(bucket_name)
    
            for dag in dags:
                # Remove path to temp dir
                dag = dag.replace(f"{temp_dir}/", name_replacement)
    
                try:
                    # Upload to your bucket
                    blob = bucket.blob(dag)
                    blob.upload_from_filename(dag)
                    print(f"File {dag} uploaded to {bucket_name}/{dag}.")
                except FileNotFoundError:
                    current_directory = os.listdir()
                    print(
                        f"{name_replacement} directory not found in {current_directory}, you may need to override the default value of name_replacement to point to a relative directory"
                    )
                    raise
    
        else:
            print("No DAGs to upload.")
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
        )
        parser.add_argument(
            "--dags_directory",
            help="Relative path to the source directory containing your DAGs",
        )
        parser.add_argument(
            "--dags_bucket",
            help="Name of the DAGs bucket of your Composer environment without the gs:// prefix",
        )
    
        args = parser.parse_args()
    
        upload_dags_to_composer(args.dags_directory, args.dags_bucket)

### Create Cloud Build YAML configuration for synchronizing DAGs

In your repository, create a YAML file named `add-dags-to-composer.cloudbuild.yaml` that configures your Cloud Build job for synchronizing DAGs. In it, there are two steps:

  1. Install the dependencies needed by the DAGs utility script.

  2. Run the utility script to synchronize the DAGs in your repository with your Managed Airflow environment.



    
    
    steps:
      # install dependencies
      - name: python
        entrypoint: pip
        args: ["install", "-r", "utils/requirements.txt", "--user"]
    
      # run
      - name: python
        entrypoint: python
        args: ["utils/add_dags_to_composer.py", "--dags_directory=${_DAGS_DIRECTORY}", "--dags_bucket=${_DAGS_BUCKET}"]
    

**Note:** Cloud Build pulls the Python image from Docker Hub and you can specify the [tag](https://hub.docker.com/_/python?tab=tags) in the `name` field of each step. If you are using `python` as your `entrypoint`, make sure that your `entrypoint` matches the version specified in your tag, otherwise `entrypoint` defaults to `latest`. 

### Create the Cloud Build trigger

Follow the [Building repositories from GitHub](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-github) guide to create a GitHub app based trigger with the following configurations:

  * **Name** : `add-dags-to-composer`

  * **Event** : Push to a branch

  * **Source** \- Repository: choose your repository

  * **Source** \- Base branch: `^main$` (change `main` to the name of your repository's base branch, if required)

  * **Source** \- Included files filter (glob): `dags/**`

  * **Build Configuration** \- Cloud build configuration file: `/add-dags-to-composer.cloudbuild.yaml` (the path to your build file)




In the Advanced configuration, add two [substitution variables](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values):

  * `_DAGS_DIRECTORY` \- the directory where dags are located in your repository. If you are using the example repository from this guide, it is `dags/`.

  * `_DAGS_BUCKET` \- the Cloud Storage bucket that contains the `dags/` directory in your development Managed Airflow environment. Omit the `gs://` prefix. For example: `us-central1-example-env-1234ab56-bucket`.


**Caution:** If you do not remove the `dags/` suffix from the Cloud Storage bucket name in the `_DAGS_BUCKET` substitution variable, the DAG sync job fails with a `NotFound` error. This happens because in Cloud Storage, `dags/` is a [folder](https://docs.cloud.google.com/storage/docs/objects#namespace), which is considered part of the object name, not part of the bucket name.

## Test your CI/CD pipeline

In this section, follow a DAG development flow that utilizes your newly created Cloud Build triggers.

### Run a presubmit job

Create a pull request to your main branch to test your build. Locate your presubmit check on the page. Click **Details** and choose **View more details on Google Cloud Build** to see your build logs in the Google Cloud console.

**Important:** Cloud Build runs unit tests with packages specified in `requirements.txt` and `requirements-test.txt`, which include a public version of Airflow. Your Managed Airflow environment might have a different set of [PyPI packages](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies) and [preinstalled packages](https://docs.cloud.google.com/composer/docs/composer-versions#images). We recommend to [run a local Airflow environment](https://docs.cloud.google.com/composer/docs/composer-2/run-local-airflow-environments) while developing your DAGs.[ ![Screenshot of a github check called test-dags with a red arrow pointing to the project name in parenthesis](https://docs.cloud.google.com/static/composer/docs/images/dag-cicd-integration-github-check.png)](https://docs.cloud.google.com/static/composer/docs/images/dag-cicd-integration-github-check.png) **Figure 2.** Screenshot of the Cloud Build presubmit check status on GitHub (click to enlarge) 

If your presubmit check failed, see Addressing build failures.

### Validate that your DAG works in your development environment

After your pull request is approved, merge it to your main branch. Use the Google Cloud console to [view your build results](https://docs.cloud.google.com/build/docs/view-build-results). If you have many Cloud Build triggers, you can filter your builds on the trigger name `add-dags-to-composer`.

After the Cloud Build sync job succeeds, the synchronized DAG appears in your development Managed Airflow environment. There, you can validate that the DAG functions as expected.

### Add the DAG to your production environment

After the DAG performs as expected, manually add it to your production environment. To do so, [upload the DAG file](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#add) to the `dags/` directory in your production Managed Airflow environment's bucket.

If your DAG sync job failed or if your DAG is not behaving as expected in your development Managed Airflow environment, see Addressing build failures.

## Addressing build failures

This section explains how to address common build failure scenarios.

### What if my presubmit check failed?

From your pull request, click **Details** and choose **View more details on Google Cloud Build** to see your build logs in the Google Cloud console. Use these logs to help you debug the problem with your DAG. Once you have resolved the issues, commit the fix and push to your branch. The presubmit check runs again, and you can continue to iterate using the logs as a debugging tool.

### What if my DAG sync job failed?

Use the Google Cloud console to [view your build results](https://docs.cloud.google.com/build/docs/view-build-results). If you have many Cloud Build triggers, you can filter your builds on the trigger name `add-dags-to-composer`. Examine the logs of the build job and resolve the errors. If you need additional help resolving the errors, utilize [support channels](https://docs.cloud.google.com/composer/docs/getting-support).

### What if my DAG does not work properly in my Managed Airflow environment?

If your DAG does not function as expected in your development Managed Airflow environment, do not manually promote the DAG to your production Managed Airflow environment. Instead, do one of the following:

  * [Revert the pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/reverting-a-pull-request) with the changes that broke your DAG to restore it to the state immediately prior to your changes (this also reverts all other files in that pull request).
  * Create a new pull request to manually revert changes to the broken DAG.
  * Create a new pull request the fix the errors in your DAG.



Following any of these steps triggers a new presubmit check and upon merge, the DAG sync job.

## What's next

  * [Run local Airflow environments](https://docs.cloud.google.com/composer/docs/composer-2/run-local-airflow-environments)
  * [Write DAGs](https://docs.cloud.google.com/composer/docs/composer-2/write-dags)
  * [Schedule and trigger DAGs](https://docs.cloud.google.com/composer/docs/composer-2/schedule-and-trigger-dags)
  * [Test DAGs](https://docs.cloud.google.com/composer/docs/composer-2/test-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
