---
url: https://docs.cloud.google.com/composer/docs/composer-2/known-issues/
title: Known issues \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:47.289146+00:00
---

# Known issues  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/known-issues/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/known-issues "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/known-issues "View this page for Managed Airflow \(Legacy Gen 1\)")

This page lists known Managed Airflow issues. For information about issue fixes, see [Release notes](https://docs.cloud.google.com/composer/docs/release-notes).

Some issues affect earlier versions, and can be fixed by [upgrading your environment](https://docs.cloud.google.com/composer/docs/composer-2/upgrade-environments).

## Non-RFC 1918 address ranges are partially supported for Pods and Services

Managed Airflow depends on GKE to deliver support for non-RFC 1918 addresses for Pods and Services. Only the following list of Non-RFC 1918 ranges is supported in Managed Airflow:

  * 100.64.0.0/10
  * 192.0.0.0/24
  * 192.0.2.0/24
  * 192.88.99.0/24
  * 198.18.0.0/15
  * 198.51.100.0/24
  * 203.0.113.0/24
  * 240.0.0.0/4



## Environment labels added during an update are not fully propagated

When you update environment labels, they aren't applied to Compute Engine VMs in the environment's cluster. As a workaround, you can apply the labels manually.

## Cannot create Managed Airflow environments with the organization policy constraints/compute.disableSerialPortLogging enforced

Managed Airflow environment creation fails if the `constraints/compute.disableSerialPortLogging` organization policy is enforced on the target project.

**Note:** This issue only occurs for clusters created before the [Managed Airflow November 9th 2020 release](https://docs.cloud.google.com/composer/docs/release-notes#November_09_2020). Managed Airflow environments created after November 9th 2020 have all GKE cluster nodes created with `serial-logging-enable=false` which prevents this issue from occurring.

**Diagnosis**

To determine if you're impacted by this issue, follow this procedure:

Go the GKE menu in Google Cloud console. [Visit the GKE menu](https://console.cloud.google.com/kubernetes/list)

Then, select your newly created cluster. Check for the following error:
    
    
    Not all instances running in IGM after 123.45s.
    Expect <number of desired instances in IGM>. Current errors:
    [CONDITION_NOT_MET]: Instance '<generated instance name>' creation failed:
    Constraint constraints/compute.disableSerialPortLogging violated for
    project <target project number>.
    

**Workarounds** :

  1. Disable the organization policy on the project where the Managed Airflow environment will be created.

An organization policy can always be disabled at the project level even if the parent resources (organization or folder) has it enabled. See the [Customizing policies for boolean constraints page](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies) for more details.

  2. Use exclusion filters

Using an exclusion filter for [serial port logs](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output#exclusion_filters). accomplishes the same goal as the disabling the org policy, as there will be serial console logs in Logging. For more details, see the [Exclusion filters](https://docs.cloud.google.com/logging/docs/exclusions#exclusion-filters) page.




## Usage of Deployment Manager to manage Google Cloud resources protected by VPC Service Controls

Managed Airflow (Legacy Gen 1) and Managed Airflow (Gen 2) versions 2.0.x use Deployment Manager to create components of Managed Airflow environments.

In December 2020, you may have received information that you may need to perform additional VPC Service Controls configuration to be able to use Deployment Manager to manage resources protected by VPC Service Controls.

We would like to clarify that **no action** is required on your side if you are using Managed Airflow and you **are not** using Deployment Manager directly to manage Google Cloud resources mentioned in the Deployment Manager's announcement.

## Deployment Manager displays information about an unsupported feature

You might see the following warning in the Deployment Manager tab:
    
    
    The deployment uses actions, which are an unsupported feature. We recommend
    that you avoid using actions.
    

For Deployment Manager's deployments owned by Managed Airflow, you can ignore this warning.

## Cannot delete an environment after its cluster is deleted

This issue applies to Managed Airflow (Legacy Gen 1) and Managed Airflow (Gen 2) versions 2.0.x.

If you delete your environment's GKE cluster before the environment itself, then attempts to delete your environment result in the following error:
    
    
     Got error "" during CP_DEPLOYMENT_DELETING [Rerunning Task. ]
    

To delete an environment when its cluster is already deleted:

  1. In the Google Cloud console, go to the **Deployment Manager** page.

[Go to Deployment Manager](https://console.cloud.google.com/dm/deployments)

  2. Find all deployments marked with labels:

     * `goog-composer-environment:<environment-name>`
     * `goog-composer-location:<environment-location>`.

You should see two deployments that are marked with the described labels:

     * A deployment named `<environment-location>-<environment-name-prefix>-<hash>-sd`
     * A deployment named `addons-<uuid>`
  3. Manually delete resources that are still listed in these two deployments and exist in the project (for example, Pub/Sub topics and subscriptions). To do so:

     1. Select the deployments.

     2. Click **Delete**.

     3. Select the **Delete 2 deployments and all resources created by them, such as VMs, load balancers and disks** option and click **Delete all**.

The deletion operation fails, but the leftover resources are deleted.

  4. Delete the deployments using one of these options:

     * In Google Cloud console, select both deployments again. Click **Delete** , then select the **Delete 2 deployments, but keep resources created by them** option.

     * Run a gcloud command to delete the deployments with the `ABANDON` policy:
           
           gcloud deployment-manager deployments delete addons-<uuid> \
               --delete-policy=ABANDON
           
           gcloud deployment-manager deployments delete <location>-<env-name-prefix>-<hash>-sd \
               --delete-policy=ABANDON
           

  5. [Delete your Managed Airflow environment](https://docs.cloud.google.com/composer/docs/composer-2/delete-environments).




## Warnings about duplicate entries of 'echo' task belonging to the 'echo-airflow_monitoring' DAG

You might see the following entry in the Airflow logs:
    
    
    in _query db.query(q) File "/opt/python3.6/lib/python3.6/site-packages/MySQLdb/
    connections.py", line 280, in query _mysql.connection.query(self, query)
    _mysql_exceptions.IntegrityError: (1062, "Duplicate entry
    'echo-airflow_monitoring-2020-10-20 15:59:40.000000' for key 'PRIMARY'")
    

You can ignore these log entries, because this error doesn't impact Airflow DAG and task processing.

We work on improving Managed Airflow service to remove these warnings from Airflow logs.

## Environment creation fails in projects with Identity-Aware Proxy APIs added to the VPC Service Controls perimeter

**Note:** This issue affects Managed Airflow versions 2.0.*.

In projects with VPC Service Controls enabled, the `cloud-airflow-prod@system.gserviceaccount.com` account requires explicit access in your security perimeter to create environments.

To create environments, you can use one of the following solutions:

  * Don't add **Cloud Identity-Aware Proxy API** and **Identity-Aware Proxy TCP API** to the security perimeter.

  * Add the `cloud-airflow-prod@system.gserviceaccount.com` service account [as the member of your security perimeter](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example) by using the following configuration in the YAML conditions file:
        
        - members:
            - serviceAccount:cloud-airflow-prod@system.gserviceaccount.com
        




## Managed Airflow environment creation or upgrade fails when the compute.vmExternalIpAccess policy is disabled

This issue applies to Managed Airflow (Legacy Gen 1) and Managed Airflow (Gen 2) environments.

Managed Airflow-owned GKE clusters configured in the Public IP mode require external connectivity for their VMs. Because of this, the `compute.vmExternalIpAccess` policy cannot forbid the creation of VMs with external IP addresses. For more information about this organizational policy, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

## First DAG run for an uploaded DAG file has several failed tasks

When you upload a DAG file, sometimes the first few tasks from the first DAG run for it fail with the `Unable to read remote log...` error. This problem happens because the DAG file is synchronized between your environment's bucket, Airflow workers, and Airflow schedulers of your environment. If the scheduler gets the DAG file and schedules it to be executed by a worker, and if the worker does not have the DAG file yet, then the task execution fails.

To mitigate this issue, environments with Airflow 2 are configured to perform two retries for a failed task by default. If a task fails, it is retried twice with 5 minute intervals.

## Announcements about the removal of support for deprecated Beta APIs from GKE versions

Managed Airflow manages underlying Managed Airflow-owned GKE clusters. Unless you explicitly use such APIs in your DAGs and your code, you can ignore announcements about GKE API deprecations. Managed Airflow takes care of any migrations, if necessary.

## Managed Airflow shouldn't be impacted by Apache Log4j 2 Vulnerability (CVE-2021-44228)

In response to [Apache Log4j 2 Vulnerability (CVE-2021-44228)](http://cloud.google.com/log4j2-security-advisory), Managed Airflow has conducted a detailed investigation and we believe that Managed Airflow is not vulnerable to this exploit.

## Airflow workers or schedulers might experience issues when accessing the environment's Cloud Storage bucket

Managed Airflow uses gcsfuse to access the `/data` folder in the environment's bucket and to save Airflow task logs to the `/logs` directory (if enabled). If gcsfuse is overloaded or the environment's bucket is unavailable, you might experience Airflow task instance failures and see `Transport endpoint is not connected` errors in Airflow logs.

**Solutions:**

  * Disable [saving logs to the environment's bucket](https://docs.cloud.google.com/composer/docs/composer-2/enable-saving-logs-to-environment-bucket). This option is already disabled by default if an environment is created using Managed Airflow 2.8.0 or later versions.
  * Upgrade to Managed Airflow 2.8.0 or later version.
  * Reduce [`[celery]worker_concurrency`](https://docs.cloud.google.com/composer/docs/composer-2/optimize-environments#synchronization_of_task_logs) and increase number of Airflow workers instead.
  * Reduce the amount of logs produced in DAG's code.
  * Follow [recommendations and best practices](https://docs.cloud.google.com/composer/docs/composer-2/write-dags) for implementing DAGs and enable task retries.



## Airflow UI might sometimes not re-load a plugin once it is changed

If a plugin consists of many files that import other modules, then the Airflow UI might not be able to recognize the fact that a plugin should be re-loaded. In such a case, [restart the Airflow web server](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface#restarting) of your environment.

## The environment's cluster has workloads in the Unschedulable state

This known issue applies only to Managed Airflow (Gen 2).

In Managed Airflow (Gen 2), after an environment is created, several workloads in the environment's cluster remain in the Unschedulable state.

When an environment scales up, new worker pods are created and Kubernetes tries to run them. If there are no free resources available to run them, the worker pods are marked as Unschedulable.

In this situation, the Cluster Autoscaler adds more nodes, which takes a couple of minutes. Until it is done, the pods stay in the Unschedulable state and don't run any tasks.

Unschedulable DaemonSet workloads named `composer-gcsfuse` and `composer-fluentd` that are not able to start on nodes where Airflow components are not present don't affect your environment.

If this problem persist for a long time (over 1 hour) then you can check the Cluster Autoscaler logs. You can find them in Logs Viewer with the following filter:
    
    
    resource.type="k8s_cluster"
    logName="projects/<project-name>/logs/container.googleapis.com%2Fcluster-autoscaler-visibility"
    resource.labels.cluster_name="<cluster-name>"
    

It contains information about decisions made by the Cluster Autoscaler: expand any noDecisionStatus to see the reason why the cluster cannot be scaled up or down.

## Error 504 when accessing the Airflow UI

You can get the `504 Gateway Timeout` error when accessing the Airflow UI. This error can have several causes:

  * Transient communication issue. In this case, attempt to access the Airflow UI later. You can also [restart the Airflow web server](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface#restarting).

  * (Managed Airflow (Gen 3) only) Connectivity issue. If Airflow UI is permanently unavailable, and timeout or 504 errors are generated, make sure that your environment can access `*.composer.googleusercontent.com`.

  * (Managed Airflow (Gen 2) only) Connectivity issue. If Airflow UI is permanently unavailable, and timeout or 504 errors are generated, make sure that your environment can access `*.composer.cloud.google.com`. If you use Private Google Access and send traffic over `private.googleapis.com` Virtual IPs, or VPC Service Controls and send traffic over `restricted.googleapis.com` Virtual IPs, make sure that your Cloud DNS is configured also for `*.composer.cloud.google.com` domain names.

  * Unresponsive Airflow web server. If the error 504 persists, but you can still access the Airflow UI at certain times, then the Airflow web server might be unresponsive because it's overwhelmed. Attempt to [increase the scale and performance parameters](https://docs.cloud.google.com/composer/docs/composer-2/scale-environments) of the web server.




## Error 502 when accessing Airflow UI

The error `502 Internal server exception` indicates that Airflow UI cannot serve incoming requests. This error can have several causes:

  * Transient communication issue. Try to access Airflow UI later.

  * Failure to start the web server. In order to start, the web server requires configuration files to be synchronized first. Check web server logs for log entries that look similar to: `GCS sync exited with 1: gcloud storage cp gs://<bucket-name>/airflow.cfg /home/airflow/gcs/airflow.cfg.tmp` or `GCS sync exited with 1: gcloud storage cp gs://<bucket-name>/env_var.json.cfg /home/airflow/gcs/env_var.json.tmp`. If you see these errors, check if files mentioned in error messages are still present in the environment's bucket.

In case of their accidental removal (for example, because a retention policy was configured), you can restore them:

    1. Set a new environment variable in your environment. You can use use any variable name and value.

    2. Override an Airflow configuration option. You can use a non-existent Airflow configuration option.




## Hovering over task instance in Tree view throws uncaught TypeError

In Airflow 2, the Tree view in the Airflow UI might sometimes not work properly when a non-default timezone is used. As a workaround for this issue, [configure the timezone explicitly](https://airflow.apache.org/docs/apache-airflow/stable/timezone.html) in the Airflow UI.

## Airflow UI in Airflow 2.2.3 or earlier versions is vulnerable to CVE-2021-45229

As pointed out in [CVE-2021-45229](https://nvd.nist.gov/vuln/detail/CVE-2021-45229), the "Trigger DAG with config" screen was susceptible to XSS attacks through the `origin` query argument.

**Recommendation** : Upgrade to the latest Managed Airflow version that supports Airflow 2.2.5.

## Workers require more memory than in previous Airflow versions

**Symptoms** :

  * In your Managed Airflow (Gen 2) environment, all environment's cluster workloads of Airflow workers are in the `CrashLoopBackOff` status and don't execute tasks. You can also see `OOMKilling` warnings that are generated if you are impacted by this issue.

  * This issue can prevent environment upgrades.




**Cause** :

  * If you use a custom value for the [`[celery]worker_concurrency`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#worker-concurrency) Airflow configuration option and custom memory settings for Airflow workers, you might experience this issue when resource consumption approaches the limit.
  * Airflow worker memory requirements in Airflow 2.6.3 with Python 3.11 are 10% higher compared to workers in earlier versions.
  * Airflow worker memory requirements in Airflow 2.3 and later versions are 30% higher compared to workers in Airflow 2.2 or Airflow 2.1.



**Solutions** :

  * Remove the override for `worker_concurrency`, so that Managed Airflow calculates this value automatically.
  * If you use a custom value for `worker_concurrency`, set it to a lower value. You can use the [automatically calculated value](https://docs.cloud.google.com/composer/docs/composer-2/optimize-environments#override-worker-concurrency) as a starting point.
  * As an alternative, you can increase the amount of memory available to Airflow workers.
  * If you can't upgrade your environment to a later version because of this issue, then apply one of the proposed solutions before upgrading.



## DAG triggering through private networks using Cloud Run functions

Triggering DAGs with Cloud Run functions through private networks with the use of VPC Connector is not supported by Managed Airflow.

**Recommendation** : Use Cloud Run functions to publish messages on Pub/Sub. Such events can actuate Pub/Sub Sensors to trigger Airflow DAGs or implement an approach based on [deferrable operators](https://docs.cloud.google.com/composer/docs/composer-2/use-deferrable-operators).

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

## Support for Google Campaign Manager 360 Operators

Google Campaign Manager Operators in Managed Airflow versions earlier than 2.1.13 are based on the Campaign Manager 360 v3.5 API that is deprecated and its sunset date is [May 1, 2023](https://developers.google.com/doubleclick-advertisers/deprecation).

If you use Google Campaign Manager operators, then upgrade your environment to Managed Airflow version 2.1.13 or later.

## Support for Google Display and Video 360 Operators

Google Display and Video 360 Operators in Managed Airflow versions earlier than 2.1.13 are based on the Display and Video 360 v1.1 API that is deprecated and its sunset date is April 27, 2023.

If you use Google Display and Video 360 operators, then upgrade your environment to Managed Airflow version 2.1.13 or later. In addition to that, you might need to change your DAGs because because some of the Google Display and Video 360 operators are deprecated and replaced with new ones.

  * `GoogleDisplayVideo360CreateReportOperator` is now deprecated. Instead, use `GoogleDisplayVideo360CreateQueryOperator`. This operator returns `query_id` instead of `report_id`.
  * `GoogleDisplayVideo360RunReportOperator` is now deprecated. Instead, use `GoogleDisplayVideo360RunQueryOperator`. This operator returns `query_id` and `report_id` instead of only `report_id`, and requires `query_id` instead of `report_id` as a parameter.
  * To check if a report is ready, use the new `GoogleDisplayVideo360RunQuerySensor` sensor that uses `query_id` and `report_id` parameters. The deprecated `GoogleDisplayVideo360ReportSensor` sensor required only `report_id`.
  * `GoogleDisplayVideo360DownloadReportV2Operator` now requires both `query_id` and `report_id` parameters.
  * In `GoogleDisplayVideo360DeleteReportOperator` there are no changes that can affect your DAGs.



## Secondary Range name restrictions

**Note:** The `gke-.*-(pods|services)-.*` naming convention is reserved for auto-created GKE cluster secondary ranges. You can't use secondary range names in this format while creating Managed Airflow instances.

## CVE-2023-29247 (Task instance details page in the UI is vulnerable to a stored XSS)

Airflow UI in Airflow versions from 2.0.x to 2.5.x is vulnerable to [CVE-2023-29247](https://nvd.nist.gov/vuln/detail/CVE-2023-29247).

**Note:** Managed Airflow version 2.4.2 fixes this issue in Airflow versions 2.4.3 and 2.5.3. We recommend to update your environment to Managed Airflow 2.4.2 or later version. This issue does not affect Airflow 2.6.x and later versions.

If you use an earlier version of Managed Airflow than 2.4.2 and suspect that your environment might be vulnerable to the exploit, please read the following description and possible solutions.

In Managed Airflow, access to the Airflow UI is [protected with IAM](https://docs.cloud.google.com/composer/docs/composer-2/access-control) and [Airflow UI access control](https://docs.cloud.google.com/composer/docs/composer-2/airflow-rbac).

This means that in order to exploit the Airflow UI vulnerability, attackers first need to gain access to your project along with the necessary IAM permissions and roles.

Solution:

  * Verify IAM permissions and roles in your project, including [Managed Service for Apache Airflow roles assigned to individual users](https://docs.cloud.google.com/composer/docs/composer-2/access-control). Make sure that only approved users can access Airflow UI.

  * Verify roles assigned to users through the [Airflow UI access control](https://docs.cloud.google.com/composer/docs/composer-2/airflow-rbac) mechanism (this is a separate mechanism that provides more granular access to Airflow UI). Make sure that only approved users can access Airflow UI and that all new users are registered with a proper role.

  * Consider additional hardening with [VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-2/configure-vpc-sc).




## Managed Airflow (Gen 2) Composer environment's airflow monitoring DAG is not re-created after deletion

The airflow monitoring DAG is not automatically re-created if deleted by the user or moved from the bucket in environments with composer-2.1.4-airflow-2.4.3.

Solution:

  * This has been fixed in later versions like composer-2.4.2-airflow-2.5.3. The suggested approach is to upgrade your environment to a newer version.
  * An alternative or temporary workaround to an environment upgrade would be, to copy the airflow_monitoring DAG from another environment with the same version.

**Note:** Don't delete the monitoring DAG, it is used by Managed Airflow to monitor the health of your environment.

## It's not possible to reduce Cloud SQL storage

Managed Airflow uses Cloud SQL to run Airflow database. Over time, disk storage for the Cloud SQL instance might grow because the disk is scaled up to fit the data stored by Cloud SQL operations when Airflow database grows.

It's not possible to scale down the Cloud SQL disk size.

As a workaround, if you want to use the smallest Cloud SQL disk size, you can re-create Managed Airflow environments with [snapshots](https://docs.cloud.google.com/composer/docs/composer-2/save-load-snapshots).

## Database Disk usage metric doesn't reduce after removing records from Cloud SQL

Relational databases, such as Postgres or MySQL, don't physically remove rows when they're deleted or updated. Instead, it marks them as "dead tuples" to maintain data consistency and avoid blocking concurrent transactions.

Both MySQL and Postgres implement mechanisms of reclaiming space after deleted records.

While it's possible to force the database to reclaim unused disk space, this is a resource hungry operation which additionally locks the database making Managed Airflow unavailable. Therefore it's recommended to rely on the building mechanisms for reclaiming the unused space.

## Access blocked: Authorization Error

If this issue affects a user, the **Access blocked: Authorization Error** dialog contains the `Error 400: admin_policy_enforced` message.

If the **API Controls** > **Unconfigured third-party apps** > **Don't allow users to access any third-party apps** option is enabled in Google Workspace and the Apache Airflow in Managed Airflow app is not explicitly allowed, users are not able to access the Airflow UI unless they explicitly allow the application.

To allow access, perform steps provided in [Allow access to Airflow UI in Google Workspace](https://docs.cloud.google.com/composer/docs/composer-2/access-control#airflow-ui-access-google-workspace).

## Login loop when accessing the Airflow UI

This issue might have the following causes:

  * If Chrome Enterprise Premium [Context-Aware Access bindings](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-console-and-apis) are used with access levels that rely on device attributes, and the Apache Airflow in Managed Airflow app is not exempted, then it's not possible to access the Airflow UI because of a login loop. To allow access, perform steps provided in [Allow access to Airflow UI in Context-Aware Access bindings](https://docs.cloud.google.com/composer/docs/composer-2/access-control#airflow-ui-access-caa-bindings).

  * If [ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) are configured in a VPC Service Controls perimeter that protects the project, and the ingress rule that allows access to the Managed Airflow service uses `ANY_SERVICE_ACCOUNT` or `ANY_USER_ACCOUNT` identity type, then users can't access the Airflow UI, ending up in a login loop. For more information about addressing this scenario, see [Allow access to Airflow UI in VPC Service Controls ingress rules](https://docs.cloud.google.com/composer/docs/composer-2/access-control#airflow-ui-access-vpcsc-ingress-rules).




## Task instances that succeeded in the past marked as FAILED

In some circumstances and rare scenarios, Airflow task instances that succeeded in the past can be marked as `FAILED`.

If it happens, usually it was either triggered by an environment update or upgrade operation, or by GKE maintenance.

**Note:** the issue itself doesn't indicate any problem in the environment and it doesn't cause any actual failures in task execution.

The issue is fixed in Managed Airflow version 2.6.5 or later.

## Airflow components have problems when communicating to other parts of Managed Airflow configuration

This issue applies only to Managed Airflow (Gen 2) versions 2.10.2 and earlier.

In very rare cases, the slowness of communication to Compute Engine Metadata server might lead to Airflow components not working optimally. For example, the Airflow scheduler might be restarted, Airflow tasks might need to be re-tried or task startup time might be longer.

**Symptoms:**

The following errors appear in Airflow components' logs (such as Airflow schedulers, workers or the web server):
    
    
    Authentication failed using Compute Engine authentication due to unavailable metadata server
    
    Compute Engine Metadata server unavailable on attempt 1 of 3. Reason: timed out
    ...
    Compute Engine Metadata server unavailable on attempt 2 of 3. Reason: timed out
    ...
    Compute Engine Metadata server unavailable on attempt 3 of 3. Reason: timed out
    

**Solution:**

  * Upgrade your environment to a later Managed Airflow version. This issue is fixed starting from Managed Airflow version 2.11.0.



## The /data folder is not available in Airflow web server

In Managed Airflow (Gen 2) and Managed Airflow (Gen 3), the Airflow web server is meant to be mostly read-only component and Managed Airflow does not synchronize the `data/` folder to this component.

Sometimes, you might want to share common files between all Airflow components, including the Airflow web server.

**Solution:**

  * Wrap the files to be shared with the web server into a PYPI module and install it as a regular PYPI package. After the PYPI module is installed in the environment, the files are added to the images of Airflow components and are available to them.

  * Add files to the `plugins/` folder. This folder is synchronized to the Airflow web server.




## Non-continuous DAG parse times and DAG bag size diagrams in monitoring

Non-continuous DAG parse times and DAG bag size diagrams on the monitoring dashboard indicate problems with long DAG parse times (more than 5 minutes).

[ ![Airflow DAG parse times and DAG bag size graphs showing a series of non-continuous intervals](https://docs.cloud.google.com/static/composer/docs/images/composer-non-continuous-dag-parse-times.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-non-continuous-dag-parse-times.png) **Figure 1.** Non-continuous DAG parse times and DAG bag size graphs (click to enlarge) 

**Solution:** We recommend keeping total DAG parse time under 5 minutes. To reduce DAG parsing time, follow [DAG writing guidelines](https://docs.cloud.google.com/composer/docs/composer-2/write-dags#guidelines).

## Managed Airflow components logs are missing in Cloud Logging

There is an issue in the environment's component responsible for uploading the logs of Airflow components to Cloud Logging. This bug sometimes leads to a situation where Managed Airflow-level log might be missing for an Airflow component. The same log is still available on the Kubernetes-component level.

Occurrence of the issue: very rare, sporadic

**Cause:**

Incorrect behaviour of the Managed Airflow component responsible for uploading logs to Cloud Logging.

**Solutions:**

  * Upgrade your environment to Managed Airflow version 2.10.0 or later.

  * In earlier versions of Managed Airflow, the temporary workaround when you encounter this situation, is to initiate a Managed Airflow operation that restarts the components for which the log is missing.




## Switching the environment's cluster to GKE Enterprise Edition is not supported

This note applies to Managed Airflow 1 and Managed Airflow 2.

Managed Airflow environment's GKE cluster is created within GKE Standard Edition.

As of December 2024, Managed Airflow service doesn't support creating Managed Airflow environments with clusters in the Enterprise Edition.

Managed Airflow environments were not tested with GKE Enterprise Edition and it has a different billing model.

**Caution:** **Don't upgrade Managed Airflow clusters to the Enterprise Edition.** Managed Airflow environments weren't tested with the Enterprise Edition and you might incur additional charges after upgrading to it. If you upgrade your environment's cluster to the Enterprise Edition, **it won't be supported by Google**.

Further communication related to GKE Standard Edition versus the Enterprise edition will be done in Q2 2025.

## Airflow components experiencing problems when communicating with other parts of Managed Airflow configuration

In some cases, because of a failed DNS resolution, Airflow components might experience problems when communicating to other Managed Airflow components or service endpoints outside of the Managed Airflow environment.

**Symptoms:**

The following errors might appear in Airflow components' logs (such as Airflow schedulers, workers or the web server):
    
    
    google.api_core.exceptions.ServiceUnavailable: 503 DNS resolution failed ...
    ... Timeout while contacting DNS servers
    

or
    
    
    Could not access *.googleapis.com: HTTPSConnectionPool(host='www.googleapis.com', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7c5ef5adba90>: Failed to resolve 'www.googleapis.com' ([Errno -3] Temporary failure in name resolution)"))
    

or
    
    
    redis.exceptions.ConnectionError: Error -3 connecting to
    airflow-redis-service.composer-system.svc.cluster.local:6379.
    Temporary failure in name resolution.
    

**Possible solutions:**

  * Upgrade to Managed Airflow 2.9.11 or

  * Set the following [environment variable](https://docs.cloud.google.com/composer/docs/composer-2/set-environment-variables): `GCE_METADATA_HOST=169.254.169.254`.




## Environment is in the ERROR state after the project's billing account was deleted or deactivated, or the Cloud Composer API was disabled

Managed Airflow environments affected by these problems are non-recoverable:

  * After the project's billing account was deleted or deactivated, even if another account was linked later.
  * After the Cloud Composer API [was disabled](https://docs.cloud.google.com/composer/docs/composer-2/enable-composer-service) in the project, even if it was enabled later.



You can do the following to address the problem:

  * You still can access data stored in your environment's buckets, but the environments themselves are no longer usable. You can create a new Managed Airflow environment and then transfer your DAGs and data.

  * If you want to perform any of the operations that make your environments non-recoverable, make sure to back up your data, for example, by [creating an environment's snapshot](https://docs.cloud.google.com/composer/docs/composer-2/save-load-snapshots). In this way, you can create another environment and transfer its data by loading this snapshot.




## Warnings about Pod Disruption Budget for environment clusters

You can see the following warnings in the GKE UI for Managed Airflow environment clusters:
    
    
    GKE can't perform maintenance because the Pod Disruption Budget allows
    for 0 Pod evictions. Update the Pod Disruption Budget.
    
    
    
    A StatefulSet is configured with a Pod Disruption Budget but without readiness
    probes, so the Pod Disruption Budget isn't as effective in gauging application
    readiness. Add one or more readiness probes.
    

It is not possible to eliminate these warnings. We work on stopping these warnings from being generated.

**Possible solutions:**

  * Ignore these warnings until the issue is fixed.



## A field value in an Airflow connection cannot be removed

**Cause:**

The Apache Airflow user interface has a limitation where it's not possible to update connection fields to empty values. When you attempt to do so, the system reverts to the previously saved settings.

**Possible solutions:**

While Apache Airflow version 2.10.4 includes a permanent fix, a temporary workaround exists for users on earlier versions. This involves deleting the connection and then recreating it, specifically leaving the required fields empty. The command-line interface is the recommended approach for deleting the connection:
    
    
    gcloud composer environments run ENVIRONMENT_NAME \
    --location LOCATION \
    connections delete -- \
    CONNECTION_ID
    

After deleting the connection, [recreate it using the Airflow UI](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#creating-a-connection-with-the-ui), ensuring that the fields you intend to leave empty are indeed left blank. You can also create the connection by running the [`connections add`](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#add) Airflow CLI command [with Google Cloud CLI](https://docs.cloud.google.com/composer/docs/composer-2/manage-airflow-connections#airflow-cli).

## Logs for Airflow tasks aren't collected if [core]execute_tasks_new_python_interpreter is set to True

Managed Airflow doesn't collect logs for Airflow tasks if the [`[core]execute_tasks_new_python_interpreter`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#execute-tasks-new-python-interpreter) Airflow configuration option is set to `True`.

**Possible solution:**

  * Remove the [override](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations) for this configuration option, or set its value to `False`.



## Missing data points in metrics, ValueError: Cannot determine path without bucket name

Environments with Managed Airflow (Gen 2) versions 2.16.0 and 2.16.1 might experience a known issue with the reporting of metrics. You can observe a few skipped data points in the reported metrics and see error messages about the `airflow-monitoring` pod restarts in the environment logs.

Example of an error message: `ValueError: Cannot determine path without bucket name error`.

This issue doesn't affect the environment's functionality. The environment is still operational and the environment health and monitoring information is reported correctly. You can ignore the error messages.

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

## What's next

  * [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-environment-creation)
  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-dags)
  * [Troubleshooting Airflow scheduler issues](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-scheduling)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
