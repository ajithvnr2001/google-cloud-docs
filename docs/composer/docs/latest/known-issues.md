---
url: https://docs.cloud.google.com/composer/docs/latest/known-issues/
title: Known issues \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:46:44.279823+00:00
---

# Known issues  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/latest/known-issues/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/known-issues "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/known-issues "View this page for Managed Airflow \(Legacy Gen 1\)")

This page lists known Managed Airflow issues. For information about issue fixes, see [Release notes](https://docs.cloud.google.com/composer/docs/release-notes).

## First DAG run for an uploaded DAG file has several failed tasks

When you upload a DAG file, sometimes the first few tasks from the first DAG run for it fail with the `Unable to read remote log...` error. This problem happens because the DAG file is synchronized between your environment's bucket, Airflow workers, and Airflow schedulers of your environment. If the scheduler gets the DAG file and schedules it to be executed by a worker, and if the worker does not have the DAG file yet, then the task execution fails.

To mitigate this issue, environments with Airflow 2 are configured to perform two retries for a failed task by default. If a task fails, it is retried twice with 5 minute intervals.

## Managed Airflow shouldn't be impacted by Apache Log4j 2 Vulnerability (CVE-2021-44228)

In response to [Apache Log4j 2 Vulnerability (CVE-2021-44228)](http://cloud.google.com/log4j2-security-advisory), Managed Airflow has conducted a detailed investigation and we believe that Managed Airflow is not vulnerable to this exploit.

## Airflow UI might sometimes not re-load a plugin once it is changed

If a plugin consists of many files that import other modules, then the Airflow UI might not be able to recognize the fact that a plugin should be re-loaded. In such a case, [restart the Airflow web server](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface#restarting) of your environment.

## Error 504 when accessing the Airflow UI

You can get the `504 Gateway Timeout` error when accessing the Airflow UI. This error can have several causes:

  * Transient communication issue. In this case, attempt to access the Airflow UI later. You can also [restart the Airflow web server](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface#restarting).

  * (Managed Airflow (Gen 3) only) Connectivity issue. If Airflow UI is permanently unavailable, and timeout or 504 errors are generated, make sure that your environment can access `*.composer.googleusercontent.com`.

  * (Managed Airflow (Gen 2) only) Connectivity issue. If Airflow UI is permanently unavailable, and timeout or 504 errors are generated, make sure that your environment can access `*.composer.cloud.google.com`. If you use Private Google Access and send traffic over `private.googleapis.com` Virtual IPs, or VPC Service Controls and send traffic over `restricted.googleapis.com` Virtual IPs, make sure that your Cloud DNS is configured also for `*.composer.cloud.google.com` domain names.

  * Unresponsive Airflow web server. If the error 504 persists, but you can still access the Airflow UI at certain times, then the Airflow web server might be unresponsive because it's overwhelmed. Attempt to [increase the scale and performance parameters](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments) of the web server.




## Error 502 when accessing Airflow UI

The error `502 Internal server exception` indicates that Airflow UI cannot serve incoming requests. This error can have several causes:

  * Transient communication issue. Try to access Airflow UI later.

  * Failure to start the web server. In order to start, the web server requires configuration files to be synchronized first. Check web server logs for log entries that look similar to: `GCS sync exited with 1: gcloud storage cp gs://<bucket-name>/airflow.cfg /home/airflow/gcs/airflow.cfg.tmp` or `GCS sync exited with 1: gcloud storage cp gs://<bucket-name>/env_var.json.cfg /home/airflow/gcs/env_var.json.tmp`. If you see these errors, check if files mentioned in error messages are still present in the environment's bucket.

In case of their accidental removal (for example, because a retention policy was configured), you can restore them:

    1. Set a new environment variable in your environment. You can use use any variable name and value.

    2. Override an Airflow configuration option. You can use a non-existent Airflow configuration option.




## Hovering over task instance in Tree view throws uncaught TypeError

In Airflow 2, the Tree view in the Airflow UI might sometimes not work properly when a non-default timezone is used. As a workaround for this issue, [configure the timezone explicitly](https://airflow.apache.org/docs/apache-airflow/stable/timezone.html) in the Airflow UI.

## Empty folders in Scheduler and Workers

Managed Airflow does not actively remove empty folders from Airflow workers and schedulers. Such entities might be created as a result of the environment bucket synchronization process when these folders existed in the bucket and were eventually removed.

**Recommendation** : Adjust your DAGs so they are prepared to skip such empty folders.

Such entities are eventually removed from local storages of Airflow schedulers and workers when these components are restarted (for example, as a result of scaling down or maintenance operations in your environment's cluster).

## Support for Kerberos

Managed Airflow does not support [Airflow Kerberos configuration](https://airflow.apache.org/docs/apache-airflow/stable/security/kerberos.html).

## Support for compute classes in Managed Airflow (Gen 2) and Managed Airflow (Gen 3)

Managed Airflow (Gen 3) and Managed Airflow (Gen 2) support only _general-purpose_ [compute class](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes#when-to-use). It means that running Pods that request other compute classes (such as _Balanced_ or _Scale-Out_) is not possible.

The _general-purpose_ class allows for running Pods requesting up to 110 GB of memory and up to 30 CPU (as described in [Compute Class Max Requests](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#min-max-requests).

If you want to use ARM-based architecture or require more CPU and Memory, then you must use a different compute class, which is not supported within Managed Airflow (Gen 3) and Managed Airflow (Gen 2) clusters.

**Recommendation** : Use `GKEStartPodOperator` to run Kubernetes Pods on a different cluster that supports the selected compute class. If you run custom Pods requiring a different compute class, then they also must run on a non-Managed Airflow cluster.

## It's not possible to reduce Cloud SQL storage

Managed Airflow uses Cloud SQL to run Airflow database. Over time, disk storage for the Cloud SQL instance might grow because the disk is scaled up to fit the data stored by Cloud SQL operations when Airflow database grows.

It's not possible to scale down the Cloud SQL disk size.

As a workaround, if you want to use the smallest Cloud SQL disk size, you can re-create Managed Airflow environments with [snapshots](https://docs.cloud.google.com/composer/docs/composer-3/save-load-snapshots).

## Database Disk usage metric doesn't reduce after removing records from Cloud SQL

Relational databases, such as Postgres or MySQL, don't physically remove rows when they're deleted or updated. Instead, it marks them as "dead tuples" to maintain data consistency and avoid blocking concurrent transactions.

Both MySQL and Postgres implement mechanisms of reclaiming space after deleted records.

While it's possible to force the database to reclaim unused disk space, this is a resource hungry operation which additionally locks the database making Managed Airflow unavailable. Therefore it's recommended to rely on the building mechanisms for reclaiming the unused space.

## Access blocked: Authorization Error

If this issue affects a user, the **Access blocked: Authorization Error** dialog contains the `Error 400: admin_policy_enforced` message.

If the **API Controls** > **Unconfigured third-party apps** > **Don't allow users to access any third-party apps** option is enabled in Google Workspace and the Apache Airflow in Managed Airflow app is not explicitly allowed, users are not able to access the Airflow UI unless they explicitly allow the application.

To allow access, perform steps provided in [Allow access to Airflow UI in Google Workspace](https://docs.cloud.google.com/composer/docs/composer-3/access-control#airflow-ui-access-google-workspace).

## Login loop when accessing the Airflow UI

This issue might have the following causes:

  * If Chrome Enterprise Premium [Context-Aware Access bindings](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-console-and-apis) are used with access levels that rely on device attributes, and the Apache Airflow in Managed Airflow app is not exempted, then it's not possible to access the Airflow UI because of a login loop. To allow access, perform steps provided in [Allow access to Airflow UI in Context-Aware Access bindings](https://docs.cloud.google.com/composer/docs/composer-3/access-control#airflow-ui-access-caa-bindings).

  * If [ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) are configured in a VPC Service Controls perimeter that protects the project, and the ingress rule that allows access to the Managed Airflow service uses `ANY_SERVICE_ACCOUNT` or `ANY_USER_ACCOUNT` identity type, then users can't access the Airflow UI, ending up in a login loop. For more information about addressing this scenario, see [Allow access to Airflow UI in VPC Service Controls ingress rules](https://docs.cloud.google.com/composer/docs/composer-3/access-control#airflow-ui-access-vpcsc-ingress-rules).




## The /data folder is not available in Airflow web server

In Managed Airflow (Gen 2) and Managed Airflow (Gen 3), the Airflow web server is meant to be mostly read-only component and Managed Airflow does not synchronize the `data/` folder to this component.

Sometimes, you might want to share common files between all Airflow components, including the Airflow web server.

**Solution:**

  * Wrap the files to be shared with the web server into a PYPI module and install it as a regular PYPI package. After the PYPI module is installed in the environment, the files are added to the images of Airflow components and are available to them.

  * Add files to the `plugins/` folder. This folder is synchronized to the Airflow web server.




## Non-continuous DAG parse times and DAG bag size diagrams in monitoring

Non-continuous DAG parse times and DAG bag size diagrams on the monitoring dashboard indicate problems with long DAG parse times (more than 5 minutes).

[ ![Airflow DAG parse times and DAG bag size graphs showing a series of non-continuous intervals](https://docs.cloud.google.com/static/composer/docs/images/composer-non-continuous-dag-parse-times.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-non-continuous-dag-parse-times.png) **Figure 1.** Non-continuous DAG parse times and DAG bag size graphs (click to enlarge) 

**Solution:** We recommend keeping total DAG parse time under 5 minutes. To reduce DAG parsing time, follow [DAG writing guidelines](https://docs.cloud.google.com/composer/docs/composer-3/write-dags#guidelines).

## Task logs appear with delays

**Symptom:**

  * In Managed Airflow (Gen 3), Airflow task logs do not appear immediately and are delayed for a few minutes.
  * You might find `Logs not found for Cloud Logging filter` messages in the Airflow logs



**Cause:**

If your environment runs a large number of tasks at the same time, task logs can be delayed because the environment's infrastructure size is not enough to process all logs fast enough.

**Solutions:**

  * Consider increasing the environment's infrastructure size to increase performance.
  * Distribute DAG runs over time, so that tasks are not executed at the same time.



## Increased startup times for KubernetesPodOperator and KubernetesExecutor

Pods created with KubernetesPodOperator and tasks executed with KubernetesExecutor experience increased startup times. Managed Airflow team is working on a solution and will announce when the issue is resolved.

**Workarounds:**

  * Launch Pods with more CPU.
  * If possible, optimize images (less layers, smaller size).



## Environment is in the ERROR state after the project's billing account was deleted or deactivated, or the Cloud Composer API was disabled

Managed Airflow environments affected by these problems are non-recoverable:

  * After the project's billing account was deleted or deactivated, even if another account was linked later.
  * After the Cloud Composer API [was disabled](https://docs.cloud.google.com/composer/docs/composer-3/enable-composer-service) in the project, even if it was enabled later.



You can do the following to address the problem:

  * You still can access data stored in your environment's buckets, but the environments themselves are no longer usable. You can create a new Managed Airflow environment and then transfer your DAGs and data.

  * If you want to perform any of the operations that make your environments non-recoverable, make sure to back up your data, for example, by [creating an environment's snapshot](https://docs.cloud.google.com/composer/docs/composer-3/save-load-snapshots). In this way, you can create another environment and transfer its data by loading this snapshot.




## Logs for Airflow tasks aren't collected if [core]execute_tasks_new_python_interpreter is set to True

Managed Airflow doesn't collect logs for Airflow tasks if the [`[core]execute_tasks_new_python_interpreter`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#execute-tasks-new-python-interpreter) Airflow configuration option is set to `True`.

**Possible solution:**

  * Remove the [override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) for this configuration option, or set its value to `False`.



## Error while removing Network Attachment when an environment is deleted

If several environments that share the same network attachment are deleted at the same time, some deletion operations fail with an error.

**Symptoms:**

The following error is generated:
    
    
    Got error while removing Network Attachment: <error code>
    

The reported error code can be `Bad request: <resource> is not ready`, or `Precondition failed: Invalid fingerprint`.

**Possible workarounds:**

  * Delete environments that use the same network attachment one by one.

  * [Disable connection to a VPC network](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#disconnect) for your environments before deleting them. We recommend this workaround for automated environment deletion.




## Degraded environment performance in several google-api-core package versions

The `google-api-core` preinstalled package versions from 2.28.0 to 2.30.2 might cause degraded environment performance, which can result in longer times to execute a task and longer times to move a task from the queued to the executing state.

Affected [Managed Airflow (Gen 3) builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3):

  * composer-3-airflow-3.1.7-build.0 to composer-3-airflow-3.1.7-build.5
  * composer-3-airflow-3.1.0-build.5 to composer-3-airflow-3.1.0-build.10
  * composer-3-airflow-2.11.1-build.0
  * composer-3-airflow-2.10.5-build.22 to composer-3-airflow-2.10.5-build.33
  * composer-3-airflow-2.9.3-build.42 to composer-3-airflow-2.9.3-build.53



Affected [Managed Airflow (Gen 2) builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2):

  * composer-2.16.10-airflow-2.11.1
  * composer-2.16.0-airflow-2.10.5 to composer-2.16.10-airflow-2.10.5
  * composer-2.16.0-airflow-2.9.3 to composer-2.16.10-airflow-2.9.3



We recommend to upgrade your environment to the following versions, which contain a version of the package where the problem is fixed or isn't present:

  * composer-3-airflow-3.1.7-build.7 and later
  * composer-3-airflow-2.11.1-build.3 and later
  * composer-3-airflow-2.10.5-build.36 and later
  * composer-3-airflow-2.9.3-build.54 (contains 2.27.0)
  * composer-2.17.0-airflow-2.11.1 and later
  * composer-2.17.0-airflow-2.10.5 and later
  * composer-2.16.11-airflow-2.11.1 (contains 2.27.0)
  * composer-2.16.11-airflow-2.10.5 (contains 2.27.0)
  * composer-2.16.11-airflow-2.9.3 (contains 2.27.0)



As a workaround, you can manually install a later version of the `google-api-core` package to an affected environment by specifying `>=2.30.3` as the required version.

## TI is no longer in the running state and task should terminate and Task Not Found errors in Airflow 3

Airflow 3 has two issues issues related to the scheduler losing task state during scheduler restarts:

  * 409 Conflict status: A race condition in schedulers causes duplicate task instance scheduling ( [#59378](https://github.com/apache/airflow/issues/59378), resolved in [#60330](https://github.com/apache/airflow/pull/60330)).

This issue is fixed in Airflow 3.2.2.

  * 404 Not Found error: Airflow workers lose track of task instances during a regular scheduler loop restart, which happens after the scheduler reaches `[scheduler]num_runs`. This changes the existing task instance IDs and generates subsequent 404 errors from a worker that isn't aware of the change ( [#53140](https://github.com/apache/airflow/issues/53140), [#60330](https://github.com/apache/airflow/pull/60330#issuecomment-4087499991), resolved in [#61631](https://github.com/apache/airflow/pull/61631)).

This issue is fixed in Airflow 3.3.1.




**Symptoms**

  * 409 Conflict: A restarted scheduler's orphan cleanup state marks active tasks as `FAILED`, causing the workers to abnormally terminate:
        
        Server indicated the task shouldn't be running anymore [supervisor]
        detail={'detail': {'reason': 'not_running', 'message': 'TI is no longer in
        the running state and task should terminate', 'current_state': 'scheduled'}} status_code=409 ti_id=UUID('...')
        

  * 404 Not Found: A restarted scheduler loses task states and fails active worker pulse checks:
        
        Server indicated the task shouldn't be running anymore [detail={'detail':
        {'reason': 'not_found', 'message': 'Task Instance not found'}}]
        [status_code=404] [ti_id=...]
        




**Solution:**

  * Both issues are fixed in Airflow version 3.3.1 and later. [Upgrade](https://docs.cloud.google.com/composer/docs/composer-3/upgrade-environments) your environment to a version that uses Airflow 3.3.1.



**Possible workarounds:**

  * It isn't possible to completely mitigate the problem in versions of Airflow earlier than 3.3.1. Any external event that causes a single scheduler to unexpectedly restart will trigger 404 and 409 (in Airflow versions earlier than 3.2.2). Examples of such events are auto-upgrades of nodes in your environment's cluster, OOM conditions in Pods, or high memory and CPU consumption by schedulers.

  * Scaling your environment down to one scheduler and [setting](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the `[scheduler]num_runs` configuration option to `-1` mitigates the cause of race conditions in schedulers.

For a highly resilient (Highly Available) environment, it isn't possible to reduce the number of schedulers to one. You can still set the `[scheduler]num_runs` to `-1`.

  * Make sure that memory and CPU consumption by the scheduler are well within the available [resource limits](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments).




## What's next

  * [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-environment-creation)
  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dags)
  * [Troubleshooting Airflow scheduler issues](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-scheduling)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
