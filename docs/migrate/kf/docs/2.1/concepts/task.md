---
url: https://docs.cloud.google.com/migrate/kf/docs/2.1/concepts/task/
title: Tasks \u00a0|\u00a0 Kf 2.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:27.643871+00:00
---

# Tasks  |  Kf 2.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.1/concepts/task/

Version 2.1

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
  * [ 2.1 ](https://docs.cloud.google.com/migrate/kf/docs/2.1)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.1/getting-started)



Send feedback 

#  Tasks Stay organized with collections  Save and categorize content based on your preferences. 

## About Tasks

In contrast to Apps (long-running processes), Tasks run for a finite amount of time and then stops. Tasks run in their own containers based on configuration on the parent App, and it could be configured to use limited resources (e.g. CPU/memory/ephermeral disk storage).

## Use Cases for Tasks

  * Migrating a database
  * Running a batch job (scheduled/unscheduled)
  * Sending an email
  * Transforming data (ETL)
  * Processing data (upload/backup/download)



## How Tasks work

Tasks are executed asynchronously and run independently from the parent App or other Tasks running on the same App. An App created for running Tasks does not have routes created or assigned, and the **Run** lifecycle is skipped. The **Source code upload** and **Build** lifecycles still proceed and result in a container image used for running Tasks after pushing the App (see App lifecycles at [Deploying an Application](https://docs.cloud.google.com/migrate/kf/docs/2.1/how-to/deploying-an-app)).

The lifecycle of a Task is as follows:

  1. You push an App for running tasks with the `kf push APP_NAME --task` command.
  2. You run a Task on the App with the `kf run-task APP_NAME` command. Task inherits the environment variables, service bindings, resource allocation, start-up command, and security groups bound to the App.
  3. Kf creates a Tekton [PipelineRun](https://github.com/tektoncd/pipeline/blob/master/docs/pipelineruns.md) with values from the App and parameters from the `run-task` command.
  4. The Tekton PipelineRun creates a Kubernetes Pod which launches a container based on the configurations on the App and Task.
  5. Task execution stops (Task exits or is terminated manually), the underlying Pod is either stopped or terminated. Pods of stopped Tasks are preserved and thus Task logs are accessible via the `kf logs APP_NAME --task` command.
  6. If you terminate a Task before it stops, the Tekton PipelineRun is cancelled (see [Cancelling a PipelineRun](https://github.com/tektoncd/pipeline/blob/master/docs/pipelineruns.md#cancelling-a-pipelinerun)), the underlying Pod together with the logs are deleted. The logs of termianted Tasks are delivered to the cluster level logging streams if configured (e.g. Stackdriver, Fluentd).
  7. If the number of Tasks run on an App is greater than 500, the oldest Tasks are automatically deleted.



## Tasks Retention Policy

Tasks are created as custom resources in the Kubernetes cluster, therefore, it is important not to exhaust the space of the underlying `etcd` database. By default, Kf only keeps the latest 500 Tasks per each App. Once the number of Tasks reach 500, the oldest Tasks (together with the underlying Pods and logs) will be automatically deleted.

## Task Logging and Execution History

Any data or messages the Task outputs to STDOUT or STDERR is available by using the `kf logs APP_NAME --task` command. Cluster level logging mechanism (such as Stackdriver, Fluentd) will deliver the Task logs to the configured logging destination.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
