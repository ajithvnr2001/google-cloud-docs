---
url: https://docs.cloud.google.com/migrate/containers/docs/review-deployment-files/
title: Review the migration artifacts \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:32.706596+00:00
---

# Review the migration artifacts  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/review-deployment-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Review the migration artifacts

This page describes the migration artifacts that the Migrate to Containers CLI generates as part of your migration.

## Before you begin

  * You should have first [created a migration plan](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan) and [executed the migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/execute-the-migration-plan).



## About the generated artifact files

The artifact files generated during the migration include the following:

  * `deployment_spec.yaml`: The YAML file that configures your workload. You can use `kubectl apply` with this file to deploy the workload to another cluster, such as a production or test cluster.

  * Dockerfile: The Dockerfile used to build the image for your migrated VM.




Some plugins might generate more than one Dockerfile and `deployment_spec.yaml` file, for example if you have a VM running multiple Tomcat servers at the same time.

Additionally, when you run the migration to a Linux system container, Migrate to Containers CLI also generates the following files: 

  * `migration.yaml`: A copy of the migration plan. You can use this file to verify what was done as part of the migration.

  * `blocklist.yaml`: The list of container services to disable based on your settings in the migration plan. Edit this file to control the list of services. For more information, see [Customize the services list](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/linux/customizing-a-migration-plan#customize_the_services_list).

  * `logs.yaml`: A list of log files detected on the source VM. Data written to these log files by the migrated workload is forwarded to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview). Edit this file to control log writing. For more information, see [Customize log data written to Cloud Logging](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/linux/customizing-a-migration-plan#log-files).




### The `deployment_spec.yaml` file

This file is a YAML file that you can use to deploy your workload to another cluster, such as a test or production cluster. If you don't configure a data migration, you will generate a `Deployment` object. When the data migration is configured, you generate a stateful set object.

### Dockerfile

Use this file if you need to generate a new version of the image. For example, you might want to install a package and capture a new image afterward. Rebuilding the image can also be useful when the Migrate to Containers CLI is upgraded, for example to implement a bug fix, and you want to rebuild the image with the new Migrate to Containers CLI runtime. The upgraded runtime is available in the Container Registry.

You can edit this file like any other Dockerfile to customize your image. For tips, see [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/). For information on how to edit the Dockerfile, see [Post-migration image updates](https://docs.cloud.google.com/migrate/containers/docs/post-migration-image-updates).

## What's next

  * Learn how to [migrate data](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/migrate-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
