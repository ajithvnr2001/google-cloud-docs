---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-compute-profiles/
title: Manage compute profiles \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:55.660825+00:00
---

# Manage compute profiles  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-compute-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Manage compute profiles Stay organized with collections  Save and categorize content based on your preferences. 

A _compute profile_ specifies how and where a pipeline is executed. It encapsulates any information required to set up and delete the physical execution environment of a pipeline. A compute profile specifies a [provisioner](https://docs.cloud.google.com/data-fusion/docs/concepts/provisioners) name and the configuration settings for that provisioner.

Each compute profile has a scope: _system_ or _user_. You can use system compute profiles for any namespaces under it. User compute profiles exist within a namespace, and only pipelines in that namespace can use user compute profiles. Compute profiles can be assigned to batch pipelines. When a compute profile is assigned to a pipeline, the provisioner specified in the profile will be used to create a cluster where the pipeline will run.

For example, an administrator might decide to create small, medium, and large compute profiles. They configure each profile with the Google Cloud credentials required to create and delete Managed Service for Apache Spark clusters in the company's Google Cloud account.

  * The small profile is configured to create a 5-node cluster.
  * The medium profile is configured to create a 20-node cluster.
  * The large profile is configured to create a 50-node cluster.



The administrator assigns the small profile to pipelines that are scheduled to run every hour on small amounts of data. They assign the large profile to pipelines that are scheduled to run every day on a large amount of data.

## Default compute profile

By default, Cloud Data Fusion uses Autoscale as the compute profile. Estimating the appropriate number of cluster workers (nodes) for a workload is difficult, and a single cluster size for an entire pipeline is often not ideal. Managed Service for Apache Spark Autoscaling provides a mechanism for automating cluster resource management and enables cluster worker VM autoscaling. For more information, see [Autoscaling](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling).

On the **Compute config** page, where you can see a list of profiles, there is a **Total cores** column, which has the maximum vCPUs that the profile can scale up to, such as `Up to 84`.

**Note:** Autoscaling can increase costs. For example, it's not recommended for real-time pipelines or replication jobs because clusters only scale up and there might be increased costs from the additional clusters.

## System and user compute profiles

A compute profile indicates which provisioner to use when creating a cluster and specifies the cluster configuration. They also specify the provisioner configuration that should be used when creating a cluster.

  * To create a _system compute profile_ , go to the **System admin** page in Cloud Data Fusion Studio. This page lists all system compute profiles and lets you create new system compute profiles.
  * To create a _user compute profile_ , go to the **Namespace administration** page in Cloud Data Fusion Studio, and then select the namespace to create the profile in. Then, you can create a profile that exists only within that namespace.



## Compute profile assignment

You can assign compute profiles to batch pipelines in the following ways:

  * Assign a default profile for the Cloud Data Fusion instance.
  * Assign a default profile for a specific namespace.
  * Assign a profile to a batch pipeline to use for runs that are started manually.
  * Assign a profile to a pipeline schedule.



If a profile is set in the schedule that triggers a run, or if you manually run a pipeline and there's a profile assigned to that pipeline, Cloud Data Fusion uses that compute profile.

If no profile is set, Cloud Data Fusion uses the default profile for the namespace. If no default profile is set for the namespace,

Cloud Data Fusion uses the system default profile. If no system default is set, the built-in profile is used.

## Assign a default compute profile

To assign default profiles to a Cloud Data Fusion namespace or instance, go to the Cloud Data Fusion Studio and click **System admin** > **Configuration** > **System compute profiles**. To select the default, click the star  star by the profile name.

## Optional: use the Preferences Microservices to set default profiles

  * To set the default profile, set a preference on the Cloud Data Fusion instance with key system.profile.name and value `system:<profile-name>`.
  * To set the default profile for a namespace, set a preference on the chosen namespace with key `system.profile.name` and value `<scope>:<profile-name>`.



## Assign a compute profile for manual runs

To assign a profile to use for manual pipeline runs, follow these steps:

  1. Navigate to the pipeline detail page.
  2. Click **Configure > Compute config**.
  3. Select a profile and click **Save**. The selected profile is used whenever the pipeline runs manually.



Alternatively, you can use the Preferences Microservices to set the profile for manual runs by setting preference on the `DataPipelineWorkflow` entity with key `system.profile.name` and value `<scope>:<profile-name>`.

## Assign a compute profile to a schedule

Any time you create a schedule for a pipeline, you can assign a profile to it. Whenever the schedule triggers a pipeline run, it will use that profile for the run. This is true for time schedules and schedules that other pipelines trigger.

## Override a compute profile configuration

When a profile is created, each configuration setting can be made immutable by locking it. However, if configuration settings are not locked, they can be overridden at runtime. To override profile configuration, follow these steps:

  1. From the Pipeline List page, select the deployed pipeline you want to run.
  2. From the Pipeline Details page, click **Configure**.
  3. Choose a compute profile and click **Customize**.
  4. Change any settings and click **Save**.



You can use runtime arguments and schedule properties to modify the cluster size and other settings.

  * To override the profile used, set a runtime argument with the key `system.profile.name`and value `<scope>:<profile-name>`.
  * To override a profile property, set a runtime argument with key `system.profile.properties.<property-name>` and value equal to the value for that property.



For example, to override the `numWorkerssetting` to a value of `10`, set a preference or runtime argument with the key `system.profile.properties.numWorkers` and the value `10`.

## What's next

  * Learn more about [provisioners in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/provisioners).
  * Learn more about [Managed Service for Apache Spark cluster configuration](https://docs.cloud.google.com/data-fusion/docs/concepts/dataproc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
