---
url: https://docs.cloud.google.com/composer/docs/composer-3/test-dags/
title: Test DAGs \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:39.730187+00:00
---

# Test DAGs  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/test-dags/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Test DAGs Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/test-dags "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/test-dags "View this page for Managed Airflow \(Legacy Gen 1\)")

**Note:** This page is **not yet revised for Managed Airflow (Gen 3)** and displays content for Managed Airflow (Gen 2).

Before deploying DAGs to production, you can [execute Airflow CLI sub-commands](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html) to parse DAG code in the same context under which the DAG is executed.

**Note:** Because Apache Airflow does not provide strong DAG isolation, we recommend that you maintain separate production and test environments to prevent DAG interference.

## Test DAGs locally with the Composer Local Development CLI tool

[Composer Local Development CLI tool](https://docs.cloud.google.com/composer/docs/composer-2/run-local-airflow-environments) streamlines Apache Airflow DAG development for Managed Airflow (Gen 2) by running an Airflow environment locally. This local Airflow environment uses an image of a specific Managed Airflow (Gen 2) version.

You can develop and test your DAGs using this local Airflow environment, and then transfer the DAGs to your testing Managed Airflow environment. The rest of this guide describes testing DAGs in a testing Managed Airflow environment.

**Note:** If you use Composer Local Development CLI tool to test your DAGs, you can run Airflow CLI commands described in this guide on your local Airflow environment [using a different syntax](https://docs.cloud.google.com/composer/docs/composer-2/run-local-airflow-environments#airflow-cli).

## Testing during DAG creation

You can run a single task instance locally and view the log output. Viewing the output enables you to check for syntax and task errors. Testing locally does not check dependencies or communicate status to the database.

We recommend that you put the DAGs in a `data/test` folder in your test environment.

### Create a test directory

In your environment's bucket, create a test directory and copy your DAGs to it.
    
    
    gcloud storage cp BUCKET_NAME/dags \
      BUCKET_NAME/data/test --recursive
    

Replace the following:

  * `BUCKET_NAME`: the name of the bucket associated with your Managed Airflow environment.



Example:
    
    
    gcloud storage cp gs://us-central1-example-environment-a12bc345-bucket/dags \
      gs://us-central1-example-environment-a12bc345-bucket/data/test --recursive
    

For more information about uploading DAGs, see [Add and update DAGs](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags).

### Check for syntax errors

To check for syntax errors in DAGs that you uploaded to the `/data/test` folder, enter the following `gcloud` command:
    
    
    gcloud composer environments run \
      ENVIRONMENT_NAME \
      --location ENVIRONMENT_LOCATION \
      dags list -- --subdir /home/airflow/gcs/data/test
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `ENVIRONMENT_LOCATION`: the region where the environment is located.



### Check for task errors

To check for task-specific errors in DAGs that you uploaded to the `/data/test` folder, run the following `gcloud` command:
    
    
    gcloud composer environments run \
      ENVIRONMENT_NAME \
      --location ENVIRONMENT_LOCATION \
      tasks test -- --subdir /home/airflow/gcs/data/test \
      DAG_ID TASK_ID \
      DAG_EXECUTION_DATE
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `ENVIRONMENT_LOCATION`: the region where the environment is located.
  * `DAG_ID`: the ID of the DAG.
  * `TASK_ID`: the ID of the task.
  * `DAG_EXECUTION_DATE`: the execution date of the DAG. This date is used for templating purposes. Regardless of the date you specify here, the DAG runs immediately.



Example:
    
    
    gcloud composer environments run \
      example-environment \
      --location us-central1 \
      tasks test -- --subdir /home/airflow/gcs/data/test \
      hello_world print_date 2021-04-22
    

## Updating and testing a deployed DAG

To test updates to your DAGs in your test environment:

  1. Copy the deployed DAG that you want to update to `data/test`.
  2. Update the DAG.
  3. Test the DAG. 
     1. Check for syntax errors.
     2. Check for task-specific errors.
  4. Make sure the DAG runs successfully.
  5. Turn off the DAG in your test environment. 
     1. Go to the Airflow UI > DAGs page.
     2. If the DAG you're modifying runs constantly, turn off the DAG.
     3. To expedite outstanding tasks, click the task and **Mark Success**.
  6. Deploy the DAG to your production environment. 
     1. Turn off the DAG in your production environment.
     2. [Upload the updated DAG](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#adding) to the `dags/` folder in your production environment.



## FAQs for testing DAGs

### How do I isolate DAG runs in my production and test environments?

For example, Airflow has a global repository of source code in the `dags/` folder that all DAG runs share. You want to update source code in production or test without interfering with running DAGs.

Airflow does not provide strong DAG isolation. We recommend that you maintain separate production and test Managed Airflow environments to prevent your test DAGs from interfering with your production DAGs.

### How do I avoid DAG interference when I run integration tests from different GitHub branches

Use unique task names to prevent interference. For example, you can prefix your task IDs with the branch name.

### What is a best practice for integration testing with Airflow?

We recommend that you use a dedicated environment for integration testing with Airflow. One way to signal the DAG run success is to write into a file in a Cloud Storage folder and then check the content in your own integration test cases.

### How do I collaborate efficiently with other DAG contributors?

Each contributor can have a subdirectory in the `data/` folder for development.

DAGs added to the `data/` folder are not picked up automatically by the Airflow scheduler or web server

DAG contributors can create manual DAG runs by using the `gcloud composer environments run` command and the `test` sub-command with the `--subdir` flag to specify the contributor's development directory.

For example:
    
    
    gcloud composer environments run test-environment-name \
      tasks test -- dag-id task-id execution-date \
      --subdir /home/airflow/gcs/data/alice_dev
    

### How do I keep my deployment and production environments in sync?

To manage access:

  * For authentication, use [service accounts](https://docs.cloud.google.com/composer/docs/composer-2/access-control#service-account).

  * For access control, use Identity and Access Management and Managed Airflow [roles and permissions](https://docs.cloud.google.com/composer/docs/composer-2/access-control#user-account).




To deploy from development to production:

  * Ensure consistent configuration, such as environment variables and PyPI packages.

  * Ensure consistent DAG arguments. To avoid hard-coding, we recommend that you use Airflow macros and variables.

For example:
        
        gcloud composer environments run test-environment-name \
          variables set -- DATA_ENDPOINT_KEY DATA_ENDPOINT_VALUE
        




## What's next

  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-dags)
  * [Adding and Updating DAGs](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags)
  * [Test, synchronize, and deploy your DAGs using version control](https://docs.cloud.google.com/composer/docs/composer-2/dag-cicd-github)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
