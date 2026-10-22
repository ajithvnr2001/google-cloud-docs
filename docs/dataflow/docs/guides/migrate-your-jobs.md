---
url: https://docs.cloud.google.com/dataflow/docs/guides/migrate-your-jobs/
title: Migrate pipeline jobs to another Google Cloud project \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:14.770411+00:00
---

# Migrate pipeline jobs to another Google Cloud project  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/migrate-your-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Migrate pipeline jobs to another Google Cloud project Stay organized with collections  Save and categorize content based on your preferences. 

A common task you might complete is to move a Dataflow job from one Google Cloud project to another. For example, you might want to move jobs from a testing environment to a production environment. Dataflow jobs are bound to the project they were created in and can't be directly migrated to a different project. To move a job, you must stop the job in the old project and recreate it in the new project.

To move a job, you need to do the following:

  1. [Stop or drain the job](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline) in the old project.
  2. Recreate the job in the new project. For example, use the same pipeline code, template, and configuration.
  3. Ensure that all necessary permissions, service accounts, and resources are correctly set up in the new project for the job to access. This includes: 
     * **Permissions:** Ensure the user or service account running the pipeline has the necessary Identity and Access Management (IAM) roles in the new project, such as `roles/dataflow.admin` and `roles/dataflow.worker`.
     * **Service Accounts:** The Dataflow worker service account will be different in the new project. Ensure this new service account has access to all the resources the pipeline needs, such as Cloud Storage buckets, BigQuery datasets, and Pub/Sub topics.
     * **Resources:** If your pipeline uses resources like Cloud Storage buckets, BigQuery datasets, or Pub/Sub topics, you need to ensure they exist in the new project or are accessible from the new project. You might need to create new resources or grant cross-project permissions.
     * **VPC Service Controls:** If you are using VPC Service Controls, ensure that the new project is part of the same service perimeter or that you have configured the necessary bridges to allow access to the required resources.



When you recreate the job, it starts as a new job and does not preserve the state of the old job.

To avoid hardcoding project-specific parameters, such as the project ID, use [pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options) to pass these values into your pipeline.

For more information about the permissions and security of your Dataflow jobs, see [Dataflow security and permissions](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions).

## What's next

  * For best practices for developing, deploying, and managing your Dataflow pipelines, see [Pipeline best practices](https://docs.cloud.google.com/dataflow/docs/guides/pipeline-best-practices).
  * To review the process of deploying your pipeline after configuring your new project, see [Deploy pipelines](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
