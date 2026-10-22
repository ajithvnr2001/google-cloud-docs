---
url: https://docs.cloud.google.com/dataflow/docs/guides/pipeline-workflows/
title: Design Dataflow pipeline workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:14.086845+00:00
---

# Design Dataflow pipeline workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/pipeline-workflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Design Dataflow pipeline workflows Stay organized with collections  Save and categorize content based on your preferences. 

Pipeline development involves different stages and tasks, such as code development, testing, and delivery into production. This document explains:

  * Considerations for continuous integration and continuous delivery (CI/CD) to support automated build, testing, and pipeline deployment into different environments.
  * Dataflow features to optimize performance and resource utilization in production.
  * Approaches and watchpoints for updating streaming pipelines in production.
  * Best practices for improving pipeline reliability in production.



## Continuous integration

[Continuous integration (CI)](https://docs.cloud.google.com/solutions/devops/devops-tech-continuous-integration) requires developers to merge code into a shared repository frequently, which is useful for applications that change a lot, such as websites that are updated frequently. Although data pipelines don't usually change as much as other types of applications, CI practices provide many benefits for pipeline development. For example, test automation provides rapid feedback when defects are encountered and reduces the likelihood that regressions enter the codebase.

Test automation is an important part of CI. When it's combined with appropriate [test coverage](https://docs.cloud.google.com/dataflow/docs/guides/develop-and-test-pipelines#test-your-pipeline), test automation run your test suite on each code commit. Your CI server can work in conjunction with a build automation tool like [Maven](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-java) to run your test suite as one or more steps of the CI pipeline. You can package code that successfully passes unit tests and integration tests into deployment artifacts from which pipelines are launched. This build is referred to as a _passing build_.

The number and types of deployment artifacts created from a passing build varies depending on how pipelines are launched. Using the Apache Beam Java SDK, you can package your pipeline code [into a self-executing JAR file](https://beam.apache.org/documentation/runners/dataflow/#self-executing-jar). You can then store the JAR file in a bucket that is hosted in the project for a [deployment environment](https://docs.cloud.google.com/dataflow/docs/guides/develop-and-test-pipelines#deployment-environment), such as the preproduction or production Google Cloud project. If you use Classic Templates (a type of templated execution), the deployment artifacts include a [JSON template file](https://docs.cloud.google.com/dataflow/docs/guides/templates/creating-templates), the JAR file for your pipeline, and an [optional metadata template](https://docs.cloud.google.com/dataflow/docs/guides/templates/creating-templates#use-metadata-in-your-pipeline-code). You can then deploy the artifacts into different deployment environments using continuous delivery, as explained in the following section.

## Continuous delivery and deployment

Continuous delivery (CD) copies deployment artifacts to one or more deployment environments that are ready to be launched manually. Typically, the artifacts built by the CI server are deployed to one or more preproduction environments for running end-to-end tests. The production environment is updated if all end-to-end tests pass successfully.

For batch pipelines, continuous deployment can directly launch the pipeline as a new Dataflow job. Alternatively, other systems can use the artifacts to launch batch jobs when required. For example, you can use [Managed Service for Apache Airflow](https://airflow.apache.org/docs/stable/integration.html#cloud-dataflow) to run batch jobs within a workflow, or Cloud Scheduler to schedule batch jobs.

Streaming pipelines can be more complex to deploy than batch pipelines, and therefore can be more difficult to automate using continuous deployment. For example, you might need to determine how to replace or update an existing streaming pipeline. If you can't update a pipeline, or if you choose not to update it, you can use other methods such as [coordinating multiple Dataflow jobs](https://docs.cloud.google.com/dataflow/docs/guides/upgrade-guide#run-parallel-pipelines) to minimize or prevent business disruption.

## Identities and roles required for CI/CD

Your CI/CD pipeline interacts with different systems to build, test, and deploy pipelines. For example, your pipeline needs access to your source code repository. To enable these interactions, ensure that your pipeline has the proper identities and roles. The following pipeline activities might also require your pipeline to have specific identities and roles.

### Integration testing with external services, including Google Cloud

When you use the Direct Runner for running ad hoc tests or system integration tests, your pipeline uses [Application Default Credentials (ADC))](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to obtain credentials. How you set up ADC depends on where your pipeline is running. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

Ensure that the service account that's used to obtain credentials for Google Cloud resources accessed by the pipeline has sufficient [roles and permissions](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#permissions).

### Deploy artifacts to different deployment environments

Where possible, use unique credentials for each environment (effectively for each project) and limit access to resources accordingly.

Use unique [service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) for each project to read and write deployment artifacts to storage buckets. Depending on whether your pipeline uses a [template](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates), your deployment process might need to stage multiple artifacts. For example, [creating and staging a Dataflow template](https://docs.cloud.google.com/dataflow/docs/guides/templates/creating-templates#create-and-stage-a-classic-template) requires permissions to write deployment artifacts that are needed to launch your pipeline, such as the pipeline's template file, to a Cloud Storage bucket.

### Deploy pipelines to different deployment environments

Where possible, use unique service accounts for each project to access and manage Google Cloud resources within the project, including accessing Dataflow itself.

The service account that you use to create and manage Dataflow jobs needs to have sufficient IAM permissions for job management. For details, see the [Dataflow service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#df-service-account) section in the Dataflow security and permissions page.

The worker service account that you use to run Dataflow jobs needs permission to manage Compute Engine resources while the job runs and to manage the interaction between the Apache Beam pipeline and the Dataflow service. For details, see the [Worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account) section in the Dataflow security and permissions page.

To specify a [user-managed worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#user-managed) for a job, use the `--serviceAccount` [pipeline option](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options). If you don't specify a worker service account when you create a job, Dataflow attempts to use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account). We recommend instead that you specify a user-managed worker service account for production environments, because the Compute Engine default service account usually has a broader set of permissions than the permissions that are required for your Dataflow jobs.

In production scenarios, we recommend that you use separate service accounts for Dataflow job management and for the worker service account, which provides improved security compared to using a single service account. For example, the service account that's used to create Dataflow jobs might not need to access data sources and sinks or to use other resources that are used by the pipeline. In this scenario, the worker service account that's used to run Dataflow jobs is granted permissions to use pipeline resources. A different service account for job creation is granted permissions to manage (including creating) Dataflow jobs.

## Example CI/CD pipeline

The following diagram provides a general and tool-agnostic view of CI/CD for data pipelines. Additionally, the diagram shows the relationship between development tasks, deployment environments, and the pipeline runners.

![Stages of a CI/CD pipeline.](https://docs.cloud.google.com/static/dataflow/images/building-production-ready-data-pipelines-using-dataflow-pipeline-cicd-for-dataflow-pipelines.svg)

The diagram shows the following stages:

  * **Code development** : During code development, a developer runs pipeline code locally using the Direct Runner. In addition, developers use a sandbox environment for ad hoc pipeline execution using the Dataflow Runner.

In typical CI/CD pipelines, the continuous integration process is triggered when a developer makes a change to the source control system, such as pushing new code to a repository.

  * **Build and test** : The continuous integration process compiles the pipeline code and then runs [unit tests](https://docs.cloud.google.com/dataflow/docs/guides/develop-and-test-pipelines#unit-tests) and [transform integration tests](https://docs.cloud.google.com/dataflow/docs/guides/develop-and-test-pipelines#integration-tests) using the Direct Runner. Optional system integration tests, which include integration testing with external sources and sinks using small test datasets, can also run.

If the tests succeed, the CI process stores the deployment artifacts, which might include JAR files, Docker images, and template metadata, required to launch the pipeline to locations that are accessible to the continuous delivery process. Depending on the types of deployment artifacts generated, you might use Cloud Storage and Artifact Registry to store the different artifact types.

  * **Deliver and deploy** : The continuous delivery process copies the deployment artifacts to a preproduction environment or makes these artifacts available for use within that environment. Developers can manually run [end-to-end tests](https://docs.cloud.google.com/dataflow/docs/guides/develop-and-test-pipelines#end-to-end-tests) using the Dataflow Runner, or they can use continuous deployment to initiate the test automatically. Typically, a continuous deployment approach is easier to enable for batch pipelines than for streaming pipelines. Because batch pipelines don't run continuously, it's easier to replace them with a new release.

The process of updating streaming pipelines might be simple or complex, and you should test updates in the preproduction environment. Update procedures might not always be consistent between releases. For example, a pipeline might change in such a way that makes in-place updates impossible. For this reason, it's sometimes difficult to automate pipeline updates using continuous deployment.




If all end-to-end tests pass, you can copy the deployment artifacts or make them available to the production environment as part of the continuous delivery process. If the new pipeline updates or replaces an existing streaming pipeline, use the procedures tested in the preproduction environment to deploy the new pipeline.

## Non-templated versus templated job execution

You can create a Dataflow job by using the Apache Beam SDK directly from a development environment. This type of job is called a _non-templated_ job. Although this approach is convenient for developers, you might prefer to separate the tasks of developing and running pipelines. To make this separation, you can use [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates), which allow you to stage and run your pipelines as independent tasks. After a template is staged, other users, including non-developers, can run the jobs from the template using the Google Cloud CLI, the Google Cloud console, or the Dataflow REST API.

Dataflow offers the following [types of job templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates):

  * **Classic Templates** : Developers use the Apache Beam SDK to run the pipeline code and save the JSON serialized execution graph as the template. The Apache Beam SDK stages the template file to a Cloud Storage location, along with any dependencies that are required by the pipeline code.
  * **Flex Templates** : Developers use the Google Cloud CLI to package the pipeline as a Docker image, which is then stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs). A Flex Template spec file is also automatically generated and stored to a user-specified Cloud Storage location. The Flex Template spec file contains metadata that describes how to run the template, such as pipeline parameters.



In addition to the [Flex Template features](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates#comparing-flex-templates-and-classic-templates) explained in the linked documentation, Flex Templates offer advantages over Classic Templates for managing templates.

  * With Classic Templates, multiple artifacts, such as JAR files, might be stored in a Cloud Storage staging location, but without any features to manage these multiple artifacts. In comparison, a Flex Template is encapsulated within a Docker image. The image packages all dependencies, aside from the Flex Template spec, that are needed for your pipeline into one deployment artifact that's managed by Artifact Registry.
  * You can use Docker image management features for your Flex Templates. For example, you can securely share Flex Templates by granting pull (and optionally push) permissions to Artifact Registry, and use Docker image tags for different versions of your Flex Templates.



Developers can use Classic Templates and Flex Templates to launch jobs in a project that's different from the project that owns the registry and the storage bucket that hosts the template assets, or just the storage bucket if you use Classic Templates. This feature is useful if you need to isolate data processing for multiple customers into different projects and pipeline jobs. Using Flex Templates, you can further specify different versions of a Docker image to use when you launch a pipeline. This feature simplifies phased replacement of batch pipelines or streaming pipelines over multiple projects when you update templates later.

## Dataflow features for optimizing resource usage

Dataflow provides the following runner-specific features to optimize resource usage, which can improve performance and lower costs:

  * **Streaming Engine** : Streaming Engine moves the execution of streaming pipelines out of VM workers and into a dedicated service. The benefits include improved autoscaling responsiveness, reductions in consumed worker VM resources, and automatic service updates without redeployment. In some cases, you can also reduce resource usage by using [at-least-once processing](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes) for use cases that can tolerate duplicates. Enabling Streaming Engine is recommended for streaming pipelines. The feature is enabled by default when you use the latest versions of the Apache Beam Java SDK or the Python SDK.
  * **Dataflow Shuffle** : Dataflow Shuffle moves shuffle operations for batch pipelines out of VM workers and into a dedicated service. The benefits include faster execution for most batch pipelines, reduced resource consumption by worker VMs, improved autoscaling responsiveness, and improved fault tolerance. Enabling Dataflow Shuffle is recommended for batch pipelines. The feature is enabled by default using the Apache Beam Java SDK and the latest Python SDK.
  * **Flexible resource scheduling (FlexRS)** : FlexRS reduces batch processing costs by using advanced scheduling techniques, the Dataflow Shuffle service, and a combination of preemptible VM instances and regular VMs.



## Update streaming pipelines in production

See [Upgrade a streaming pipeline](https://docs.cloud.google.com/dataflow/docs/guides/upgrade-guide).

## Life of a Dataflow job

A Dataflow job goes through a lifecycle that's represented by various [job states](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#jobstate). To run a Dataflow job, submit it to a [region](https://docs.cloud.google.com/dataflow/docs/resources/locations). The job is then routed to an available Dataflow backend in one of the zones within the region. Before Dataflow assigns a backend, it verifies that you have sufficient quota and permissions to run the job. When these preflight checks are complete and a backend has been assigned, the job moves to a `JOB_STATE_PENDING` state. For [FlexRS](https://docs.cloud.google.com/dataflow/docs/guides/flexrs) jobs, the backend assignment might be delayed to a future time, and these jobs enter a `JOB_STATE_QUEUED` state.

The assigned backend picks up the job to run and attempts to start Dataflow workers in your Google Cloud project. The zone that's chosen for the worker VMs depends on a number of factors. For batch jobs that use [Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch), the service also tries to ensure that the Dataflow backend and worker VMs are located in the same zone to avoid cross-zone traffic.

After the Dataflow workers start, they request work from the Dataflow backend. The backend is responsible for splitting the work into parallelizable chunks, called [bundles](https://beam.apache.org/documentation/runtime/model/#bundling-and-persistence), that are distributed among the workers. If the workers can't handle the existing work, and if autoscaling is enabled, the backend starts more workers in order to handle the work. Similarly, if more workers are started than are needed, some of the workers are shut down.

After the Dataflow workers start, the Dataflow backend acts as the control plane to orchestrate the job's execution. During processing, the job's data plane performs shuffle operations such as `GroupByKey`, `CoGroupByKey`, and `Combine`. Jobs use one the following data-plane implementations for shuffle operations:

  * The data plane runs on the Dataflow workers, and shuffle data is stored on [persistent disks](https://docs.cloud.google.com/compute/docs/disks).
  * The data plane runs as a service, externalized from the worker VMs. This implementation has two variants, which you specify when you create the job: [Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch) for batch pipelines and [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) for streaming pipelines. The service-based shuffle significantly improves the performance and scalability of data-shuffling operations compared to the worker-based shuffle.



Streaming jobs that enter a `JOB_STATE_RUNNING` state continue to run indefinitely until they're [cancelled](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#cancel) or [drained](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#drain), unless a job failure occurs. Batch jobs automatically stop when all processing is completed or if an unrecoverable error occurs. Depending on how the job is stopped, Dataflow sets the job's status to one of multiple terminal states, including `JOB_STATE_CANCELLED`, `JOB_STATE_DRAINED`, or `JOB_STATE_DONE`.

## Pipeline reliability best practices

This section discusses failures that might occur when you work with Dataflow and best practices for Dataflow jobs.

### Follow isolation principles

A general recommendation to improve overall pipeline reliability is to follow the isolation principles behind [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). Ensure that your pipelines don't have critical cross-region dependencies. If you have a pipeline that has critical dependency on services from multiple regions, a failure in any one of those regions can impact your pipeline. To help avoid this issue, deploy to multiple regions for redundancy and backup.

### Create Dataflow snapshots

Dataflow offers a snapshot feature that provides a backup of a pipeline's state. You can restore the pipeline snapshot into a new streaming Dataflow pipeline in another zone or region. You can then start the reprocessing of messages in the Pub/Sub or Kafka topics starting at the snapshot timestamp. If you set up regular snapshots of your pipelines, you can minimize Recovery Time Objective (RTO) time.

For more information about Dataflow snapshots, see [Use Dataflow snapshots](https://docs.cloud.google.com/dataflow/docs/guides/using-snapshots).

### Handle job submission failures

You submit non-template Dataflow jobs using the Apache Beam SDK. To submit the job, you [run the pipeline](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/Pipeline.html#run--) using the [Dataflow Runner](https://beam.apache.org/releases/javadoc/current/org/apache/beam/runners/dataflow/DataflowRunner.html), which is specified as part of the pipeline's [options](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/options/PipelineOptions.html). The Apache Beam SDK stages files in Cloud Storage, creates a job request file, and submits the file to Dataflow.

Alternatively, jobs created from Dataflow templates use [different submission methods](https://docs.cloud.google.com/dataflow/docs/guides/templates/running-templates), which commonly rely on the [templates API](https://docs.cloud.google.com/dataflow/docs/reference/rest#rest-resource-v1b3projectslocationstemplates).

You might see different errors returned by Dataflow that indicate job failure for template and non-template jobs. This section discusses different types of job submission failures and best practices for handling or mitigating them.

#### Retry job submissions after transient failures

If a job fails to start due to a Dataflow service issue, retry the job a few times. Retrying mitigates transient service issues.

#### Mitigate zonal failures by specifying a worker region

Dataflow provides [regional availability](https://docs.cloud.google.com/docs/geography-and-regions#regional_resources) and is available in multiple regions. When a user submits a job to a [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) without explicitly specifying a zone, Dataflow routes the job to a zone in the specified region based on resource availability.

The recommended option for job placement is to specify a worker region by using the `--region` flag instead of the `--zone` flag whenever possible. This step allows Dataflow to provide an additional level of fault tolerance for your pipelines by automatically choosing the best possible zone for that job. Jobs that specify an explicit zone don't have this benefit, and they fail if problems occur within the zone. If a job submission fails due to a zonal issue, you can often resolve the problem by retrying the job without explicitly specifying a zone.

#### Mitigate regional failures by storing data in multiple regions

If an entire region is unavailable, try the job in a different region. It's important to think about the availability of your data when jobs fail across regions. To protect against single-region failures without manually copying data to multiple regions, use Google Cloud resources that automatically store data in multiple regions. For example, use Cloud Storage [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) and [multi-region](https://docs.cloud.google.com/storage/docs/locations#location-mr) buckets. If one region becomes unavailable, you can rerun the pipeline in another region where the data is available.

For an example of using multi-regional services with Dataflow, see High availability and geographic redundancy.

### Handle failures in running pipelines

After a job is submitted and has been accepted, the only valid operations for the job are the following:

  * cancel for batch jobs
  * update, drain, or cancel for streaming jobs



You can't change the location of running jobs after you submit the job. If you're not using FlexRS, jobs usually start processing data within a few minutes after submission. FlexRS jobs can take up to six hours for data processing to begin.

This section discusses failures for running jobs and best practices for handling them.

#### Monitor jobs to identify and resolve issues caused by transient errors

For batch jobs, bundles that include a failing item are retried four times. Dataflow terminates the job when a single bundle has failed four times. This process takes care of many transient issues. However, if a prolonged failure occurs, the maximum retry limit is usually reached quickly, which allows the job to fail quickly.

For monitoring and incident management, configure alerting rules to detect failed jobs. If a job fails, [inspect the job logs](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#job-failed-four-times) to identify job failures caused by failed work items that exceeded the retry limit.

For streaming jobs, Dataflow retries failed work items indefinitely. The job is not terminated. However, the job might stall until the issue is resolved. Create [monitoring policies](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring) to detect signs of a stalled pipeline, such as an [increase in system latency and a decrease in data freshness](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf#data_freshness_streaming). Implement error logging in your pipeline code to help identify pipeline stalls caused by work items that fail repeatedly.

#### Restart jobs in a different zone if a zonal outage occurs

After a job starts, the Dataflow workers that run user code are constrained to a single zone. If a zonal outage occurs, Dataflow jobs are often impacted, depending on the extent of the outage.

For outages that impact only Dataflow backends, the backends are automatically migrated to a different zone by the managed service so that they can continue the job. If the job uses [Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch), the backend cannot be moved across zones. If a Dataflow backend migration occurs, jobs might be temporarily stalled.

If a zonal outage occurs, running jobs are likely to fail or stall until zone availability is restored. If a zone becomes unavailable for a long period, stop jobs ([cancel](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#cancel) for batch jobs and [drain](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#drain) for streaming jobs) and then restart them to let Dataflow choose a new, healthy zone.

#### Restart batch jobs in a different region if a regional outage occurs

If a regional outage occurs in a region where your Dataflow jobs are running, the jobs can fail or stall. For batch jobs, restart the job in a different region if possible. It's important to ensure that your data is available in different regions.

#### Mitigate regional outages by using high availability or failover

For streaming jobs, depending on the fault tolerance and budget for your application, you have different options for mitigating failures. For a regional outage, the simplest and most cost-effective option is to wait until the outage ends. However, if your application is latency-sensitive or if data processing must either not be disrupted or should be resumed with minimal delay, the following sections discuss options.

##### High-availability: Latency-sensitive with no data loss

If your application cannot tolerate data loss, run duplicate pipelines in parallel in two different regions, and have the pipelines consume the same data. The same data sources need to be available in both regions. The downstream applications that depend on the output of these pipelines must be able to switch between the output from these two regions. Due to the duplication of resources, this option involves the highest cost compared to other options. For an example deployment, see the section High availability and geographic redundancy.

##### Failover: Latency-sensitive with some potential data loss

If your application can tolerate potential data loss, make the streaming data source available in multiple regions. For example, using Pub/Sub, maintain two independent subscriptions for the same topic, one for each region. If a regional outage occurs, start a replacement pipeline in another region, and have the pipeline consume data from the backup subscription.

[Replay](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub#seek) the backup subscription to an appropriate time to keep data loss to a minimum without sacrificing latency. Downstream applications must know how to switch to the running pipeline's output, similar to the high-availability option. This option uses fewer resources than running duplicate pipelines because only the data is duplicated.

## High availability and geographic redundancy

You can run multiple streaming pipelines in parallel for high-availability data processing. For example, you can run two parallel streaming jobs in different regions, which provides geographical redundancy and fault tolerance for data processing.

By considering the geographic availability of data sources and sinks, you can operate end-to-end pipelines in a highly available, multi-region configuration. The following diagram shows an example deployment.

![2 regional pipelines use separate subscriptions to read from a global Pub/Sub topic. The pipelines write to separate multi-regional BigQuery tables, one in the US and one in Europe.](https://docs.cloud.google.com/static/dataflow/images/building-production-ready-data-pipelines-using-dataflow-pipeline-high-availability.svg)

The diagram shows the following flow:

  1. Pub/Sub runs in most regions around the world, which lets the service offer fast, global data access, while giving you control over where messages are stored. Pub/Sub can automatically store published messages in the Google Cloud region that's nearest to subscribers, or you can configure it to use a specific region or set of regions by using [message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction).

Pub/Sub then delivers the messages to subscribers across the world, regardless of where the messages are stored. Pub/Sub clients don't need to be aware of the server locations they are connecting to, because global load-balancing mechanisms direct traffic to the nearest Google Cloud data center where messages are stored.

  2. Dataflow runs in [specific Google Cloud regions](https://docs.cloud.google.com/dataflow/docs/resources/locations). By running parallel pipelines in separate Google Cloud regions, you can [isolate your jobs from failures that affect a single region](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints#resilience_and_geographic_separation). The diagram shows two instances of the same pipeline, each one running in a separate Google Cloud region.

  3. The parallel Dataflow pipelines write to two separate BigQuery regions, providing geographic redundancy. Within a region, BigQuery automatically stores copies of your data in two different Google Cloud zones. For more information, see [Disaster planning](https://docs.cloud.google.com/bigquery/docs/reliability-intro#disaster_planning) in the BigQuery documentation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
