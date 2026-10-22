---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/logging/
title: Troubleshoot missing logs in GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:44.575879+00:00
---

# Troubleshoot missing logs in GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot missing logs in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Issues with the logging pipeline in Google Kubernetes Engine (GKE) can prevent your cluster logs from appearing in Cloud Logging, hindering your monitoring and debugging efforts.

Use this document to learn how to verify configurations and permissions, resolve resource and performance issues, investigate filters and application behavior, and address platform or service problems affecting your logs.

This information is important for Platform admins and operators who maintain cluster observability and for anyone who uses Cloud Logging to troubleshoot GKE operations. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

For more information about how to use logs to troubleshoot your workloads and clusters, see [Conduct historical analysis with Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-logging).

## Find your solution by symptom

If you've identified a specific symptom related to your missing logs, use the following table to find troubleshooting advice:

Category | Symptom or observation | Potential cause | Troubleshooting steps  
---|---|---|---  
**Configuration** | No logs from _any_ cluster in the project are visible. | The Cloud Logging API is disabled for the project. | Verify the Cloud Logging API status  
Logs are missing from a _specific cluster_ , or only certain log types are missing. | Cluster-level logging is disabled for the required log types. | Verify cluster logging configuration  
Logs are missing from nodes in a _specific node pool_. | The node pool's nodes lack the required access scope. | Verify node pool access scopes  
Permission errors (`401` or `403`) appear in logging agent logs. | The node's service account is missing the required permission. | Verify node service account permissions  
**Resource and performance** | Logs are missing intermittently, or you see `RESOURCE_EXHAUSTED` errors. | The project is exceeding the Cloud Logging API write quota. | Investigate Cloud Logging API quota usage  
Some logs from a specific node are missing, often during high traffic or load. | The node is exceeding logging agent throughput limits, or lacks resources (CPU or memory) to process logs. | Investigate node throughput and resource usage  
**Filtering and application behavior** | Specific logs that match a certain pattern are consistently missing. | A log exclusion filter in Cloud Logging is unintentionally dropping the logs. | Investigate log exclusion filters  
Logs from a container are significantly delayed or appear only after the container exits. | The application's output is fully buffered, often due to piping `stdout`. | Investigate container log buffering and delays  
Expected logs don't appear in search results. | Query filters in Logs Explorer might be too restrictive. | Investigate Logs Explorer queries  
No logs are visible from a specific application Pod, but other cluster logs are present. | The application inside the container isn't writing to `stdout` or `stderr`. | Investigate application-specific logging behavior  
**Platform and service** | Logs older than a certain date don't appear. | The logs have passed their retention period and have been deleted by Cloud Logging. | Investigate log retention periods  
Widespread log loss or delays across projects or clusters. | Cloud Logging service issue or ingestion delay. | Investigate Cloud Logging service issues and delays  
Logging issues coincide with cluster version limitations. | Unsupported GKE version. | Investigate cluster version  
  
## Use automated diagnostic tools

The following sections cover tools that can automatically inspect your cluster for common misconfigurations and help investigate complex problems.

### Debug GKE logging issues with `gcpdiag`

If you are missing or getting incomplete logs from your GKE cluster, use the `gcpdiag` tool for troubleshooting. 

[`gcpdiag`](https://gcpdiag.dev) is an open source tool. It is not an officially supported Google Cloud product. You can use the `gcpdiag` tool to help you identify and fix Google Cloud project issues. For more information, see the [gcpdiag project on GitHub](https://github.com/GoogleCloudPlatform/gcpdiag/#gcpdiag---diagnostics-for-google-cloud-platform).

When logs from the GKE cluster are missing or incomplete, investigate potential causes by focusing on the following core configuration settings: 

  * **Project-level logging:** helps ensure that the Google Cloud project housing the GKE cluster has the Cloud Logging API enabled.
  * **Cluster-level logging:** verifies that logging is explicitly enabled within the configuration of the GKE cluster.
  * **Node pool permissions:** confirms that the nodes within the cluster's node pools have the `Cloud Logging Write` scope enabled, allowing them to send log data.
  * **Service account permissions:** validates that the service account used by the node pools possesses the necessary IAM permissions to interact with Cloud Logging. Specifically, the `roles/logging.logWriter` role is typically required.
  * **Cloud logging API write quotas:** verifies that Cloud Logging API Write quotas have not been exceeded within the specified timeframe.



## Google Cloud console

  1. Complete and then copy the following command. 
    
    gcpdiag runbook gke/logs \
        --parameter project_id=PROJECT_ID \
        --parameter name=CLUSTER_NAME \
        --parameter location=LOCATION

  2. Open the Google Cloud console and activate Cloud Shell.
[Open Cloud console](https://console.cloud.google.com/logs?cloudshell=true)
  3. Paste the copied command.
  4. Run the `gcpdiag` command, which downloads the `gcpdiag` docker image, and then performs diagnostic checks. If applicable, follow the output instructions to fix failed checks. 



## Docker

You can [ run `gcpdiag` using a wrapper](https://github.com/GoogleCloudPlatform/gcpdiag?tab=readme-ov-file#installation) that starts `gcpdiag` in a [Docker](https://www.docker.com/) container. Docker or [Podman](https://podman.io/) must be installed.

  1. Copy and run the following command on your local workstation. 
         
         curl https://gcpdiag.dev/gcpdiag.sh >gcpdiag && chmod +x gcpdiag

  2. Execute the `gcpdiag` command. 
         
         ./gcpdiag runbook gke/logs \
             --parameter project_id=PROJECT_ID \
             --parameter name=CLUSTER_NAME \
             --parameter location=LOCATION




View [available parameters](https://gcpdiag.dev/runbook/diagnostic-trees/gke/logs/#parameters) for this runbook.

Replace the following:

  * `PROJECT_ID`: the ID of the project containing the resource.
  * `CLUSTER_NAME`: the name of the GKE cluster.
  * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a` ) for the cluster.



Useful flags:

  * `--universe-domain`: If applicable, the [Trusted Partner Sovereign Cloud](https://cloud.google.com/blog/products/identity-security/new-sovereign-controls-for-gcp-via-assured-workloads) domain hosting the resource
  * `--parameter` or `-p`: Runbook parameters



For a list and description of all `gcpdiag` tool flags, see the [`gcpdiag` usage instructions](https://github.com/GoogleCloudPlatform/gcpdiag?tab=readme-ov-file#usage).

### Use Gemini Cloud Assist investigations

Consider using [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations) to gain additional insights into your logs and resolve issues. For more information about different ways to initiate an investigation by using the Logs Explorer, see [Troubleshoot issues with Gemini Cloud Assist Investigations](https://docs.cloud.google.com/cloud-assist/investigations#entry-points) in the Gemini documentation.

## Verify logging configuration and permissions

Incorrect settings are a common reason for missing GKE logs. Use the following sections to verify your Cloud Logging configuration.

### Verify the Cloud Logging API status

For logs to be collected from any cluster in your project, the Cloud Logging API must be enabled.

**Symptoms** :

No logs from any GKE resources in your project are visible in Cloud Logging.

**Cause** :

The Cloud Logging API is disabled for the Google Cloud project, preventing the logging agent on the nodes from sending logs.

**Resolution** :

To verify that the Cloud Logging API is enabled and enable it if necessary, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Logging API** page.

[Go to the **Cloud Logging API page**](https://console.cloud.google.com/apis/library/logging.googleapis.com)

  2. Select your project.

  3. The Cloud Logging API is enabled if you see **API enabled** in the page header. If you don't see **API enabled** , then click the **Enable** button.




###  gcloud 

  1. Check if the API is enabled:
         
         gcloud services list --enabled --filter="NAME=logging.googleapis.com"
         

The output should be the following:
         
         NAME: logging.googleapis.com
         TITLE: Cloud Logging API
         

  2. If the API isn't listed in the enabled services, enable it:
         
         gcloud services enable logging.googleapis.com \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with your Google Cloud project ID.




### Verify cluster logging configuration

GKE lets you configure which log types (such as `SYSTEM` or `WORKLOAD`) are collected from a cluster.

**Symptoms** :

No logs are appearing in Cloud Logging from a specific GKE cluster, or only certain types of logs (like `SYSTEM`) are missing.

**Cause** :

Cluster-level logging is disabled for the required log types. If you're using an Autopilot cluster, this isn't the cause of your logging issues. This setting is configurable for Standard clusters, but is always enabled by default on Autopilot clusters and can't be disabled.

**Resolution** :

To check and update the cluster's logging configuration, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster that you want to investigate.

  3. Click the **Details** tab and navigate to the **Features** section.

  4. In the **Logging** row, review which log types, such as **System** or **Workloads** , are enabled.

  5. If the log types that you want to collect are disabled or incorrect, click edit **Edit Logging**.

  6. In the **Components** list, select the checkboxes for the log types that you want to collect and click **OK**. For more information about available log types, see [About GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#available-logs).

  7. Click **Save Changes**.




###  gcloud 

  1. To check the logging configuration, describe the cluster:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             --format="value(name,loggingConfig.componentConfig.enableComponents)"
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a` ) for the cluster.
     * `PROJECT_ID`: your Google Cloud project ID.

If logging is enabled, the output is similar to the following:
    
    example-cluster    SYSTEM_COMPONENTS;WORKLOADS
    

If the output is `NONE`, then logging is disabled.

  2. If the log types that you want are disabled or incorrect, update the logging configuration:
         
         gcloud container clusters update CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             --logging=LOGGING_TYPE
         

Replace `LOGGING_TYPE` with `SYSTEM`, `WORKLOAD`, or both. To collect any logs, `SYSTEM` must be enabled. `WORKLOAD` logs can't be collected on their own. For more information about available log types, see [About GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#available-logs).




### Verify node pool access scopes

**Note:** This section applies only to Standard GKE clusters. If you are troubleshooting an Autopilot cluster, skip this section.

Nodes in a GKE cluster use OAuth access scopes to get permission to interact with Google Cloud APIs, including Cloud Logging.

**Symptoms** :

Logs are missing from nodes in a specific node pool.

**Cause** :

The nodes in the node pool don't have the necessary OAuth access scope. One of the following scopes is required for nodes to write logs to Cloud Logging:

  * `https://www.googleapis.com/auth/logging.write`: grants permission to write logs. This is the minimum scope required.
  * `https://www.googleapis.com/auth/logging.admin`: grants full access to the Cloud Logging API, which includes the permissions from `logging.write`.
  * `https://www.googleapis.com/auth/cloud-platform`: grants full access to all enabled Google Cloud APIs, which includes the permissions from `logging.write`.



**Resolution** :

To verify the permissions and grant the required roles if missing, select one of the following options:

###  Console 

  1. Verify the node pool's access scopes:

     1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

     2. To open the cluster's details page, click the name of the cluster that you want to investigate.

     3. Click the **Nodes** tab.

     4. In the **Node Pools** section, click the name of the node pool that you want to investigate.

     5. Navigate to the **Security** section.

     6. Review the scopes listed in the **Access scopes** field. Ensure that at least one of the required scopes is present:

        * **Stackdriver Logging API - Write Only**
        * **Stackdriver Logging API - Full**
        * **Cloud Platform - Enabled**

If the required scopes are missing, re-create the node pool. You can't change access scopes on an existing node pool.

  2. If needed, create a new node pool with the required scope:

     1. Navigate back to the cluster details page for the cluster that you want to modify.
     2. Click the **Nodes** tab.
     3. Click _add_box_ **Create user-managed node pool**.
     4. Fill in the **Node pool details** section.
     5. In the left-hand navigation, click **Security**.
     6. In the **Access scopes** section, select the roles that you want to add: 
        * To add specific scopes, select **Set access for each API**.
        * To allow full access, select **Allow full access to all Cloud APIs**.
     7. Configure any other sections as needed.
     8. Click **Create**.
  3. [Migrate your workloads to the new node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-nodes). After you migrate workloads to the new node pool, your applications run on nodes that have the necessary scopes to send logs to Cloud Logging.

  4. Delete the old node pool:

     1. Navigate back to the cluster details page and select the **Nodes** tab.
     2. In the **Node Pools** section, find the old node pool.
     3. Next to the node pool, click delete **Delete** .
     4. When prompted, confirm deletion by typing the node pool name and click **Delete**.



###  gcloud 

  1. Verify the node pool's access scopes:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             --format="value(nodePools[].name,nodePools[].config.oauthScopes)"
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a` ) for the cluster.
     * `PROJECT_ID`: your Google Cloud project ID.

Review the output for each node pool. Ensure that at least one of the required scopes (`https://www.googleapis.com/auth/logging.write`, `https://www.googleapis.com/auth/cloud-platform`, or `https://www.googleapis.com/auth/logging.admin`) is listed. If the required scopes are missing, re-create the node pool. You can't change access scopes on an existing node pool.

  2. If needed, create a new node pool with the required scope:
         
         gcloud container node-pools create NEW_NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             --scopes=https://www.googleapis.com/auth/logging.write,OTHER_SCOPES
         

Replace the following:

     * `NEW_NODE_POOL_NAME`: a name for the new node pool.
     * `OTHER_SCOPES`: a comma-separated list of any other scopes that your nodes require. If you don't need other scopes, omit this placeholder and the preceding comma.
  3. [Migrate your workloads to the new node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-nodes). After you migrate workloads to the new node pool, your applications run on nodes that have the necessary scopes to send logs to Cloud Logging.

  4. Delete the old node pool:
         
         gcloud container node-pools delete OLD_NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID
         




### Verify node service account permissions

Nodes use a service account to authenticate with Google Cloud services, and this account needs specific IAM permissions to write logs.

**Symptoms** :

  * Logs are missing from nodes.
  * Inspecting logging agent logs (for example, Fluent Bit) might show permission-related errors, such as `401` or `403` codes when trying to write to Cloud Logging.
  * You might see a `Grant Critical Permissions to Node Service Account` notification for the cluster in the Google Cloud console.



**Cause** :

This issue is caused by one of the following service accounts:

  * **Node service account** : the service account used by the node pool's nodes lacks the necessary IAM permissions to write logs to Cloud Logging. The node service account must have a role that includes the `logging.logEntries.create` permission.

  * **GKE node service agent** : in GKE version 1.33 and later, the GKE [node service agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#default-node-service-agent) (`service-PROJECT_NUMBER@gcp-sa-gkenode.iam.gserviceaccount.com`) must have the [Kubernetes Default Node Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAgent) (`roles/container.defaultNodeServiceAgent`) role. This role gives GKE access to manage node resources and operations, including logging components.




You can identify service accounts that don't have the required access by using [recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders). To use recommendations to check for missing permissions, select one of the following options:

###  Console 

  1. In the **Kubernetes clusters** page, locate the **Notifications** column.
  2. Check the **Notifications** column for the **Grant critical permissions** recommendation. This recommendation means that the `NODE_SA_MISSING_PERMISSIONS` check has failed.
  3. If the recommendation is present, click it. A details panel opens, explaining the missing permissions and providing the steps to fix it.



###  gcloud 

  1. List recommendations for missing service account permissions:
         
         gcloud recommender recommendations list \
             --recommender=google.container.DiagnosisRecommender \
             --location LOCATION \
             --project PROJECT_ID \
             --format yaml \
             --filter="recommenderSubtype:NODE_SA_MISSING_PERMISSIONS"
         

  2. Analyze the command output:

     * If the command returns an empty list, then the recommender hasn't found any active `NODE_SA_MISSING_PERMISSIONS` recommendations. The service accounts it checked appear to have the required permissions.

     * If the command returns one or more YAML blocks, then the recommender has identified a permission issue. Review the output for the following key fields:

       * `description`: provides a summary of the issue, such as specifying that your node service account is missing the `roles/logging.logWriter` role or that the GKE service agent is missing the `roles/container.defaultNodeServiceAgent` role.
       * `resource`: specifies the cluster that's affected.
       * `content.operations`: contains the recommended resolution. This section provides the exact `gcloud projects add-iam-policy-binding` command required to grant the specific missing role.



The recommender can take up to 24 hours to reflect recent changes.

**Resolution** :

To resolve this issue, try these steps:

  1. Grant the `roles/container.defaultNodeServiceAccount` role on the cluster project to the node service account. This role includes the permissions that GKE needs to write logs. For more information, see [Grant the minimum required role for GKE](https://docs.cloud.google.com/kubernetes-engine/security/configure-node-service-accounts#grant-minimum-role).
  2. After you complete the preceding step, if logs are still missing and the cluster uses version 1.33 or later, grant the `roles/container.defaultNodeServiceAgent` role on the project to the GKE node service agent:

     1. Get your project number:
            
            gcloud projects describe PROJECT_ID --format="value(projectNumber)"
            

Replace `PROJECT_ID` with your project ID.

     2. To grant the `roles/container.defaultNodeServiceAgent` role to the node service agent, select one of the following options:

###  Console 

        1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

        2. Select the **Include Google-provided role grants** checkbox.

        3. In the  filter_list **Filter** field, specify the following service agent email address:
               
               service-PROJECT_NUMBER@gcp-sa-gkenode.iam.gserviceaccount.com
               

Replace `PROJECT_NUMBER` with the project number from the output of the preceding step.

        4. Press `Enter`.

        5. Click edit **Edit principal**.

        6. Click add **Add roles**.

        7. In the search field, enter `Kubernetes Engine Default Node Service Agent` and select the role.

        8. Click **Save**.

###  gcloud 

        1. Verify if the `roles/container.defaultNodeServiceAgent` role is bound to the service agent:
               
               gcloud projects get-iam-policy PROJECT_ID \
                   --flatten="bindings[].members" \
                   --format='table(bindings.role)' \
                   --filter="bindings.members:serviceAccount:service-PROJECT_NUMBER@gcp-sa-gkenode.iam.gserviceaccount.com"
               

Replace `PROJECT_NUMBER` with the project number from the output of the preceding step.

In the output, look for `roles/container.defaultNodeServiceAgent`.

        2. If the role is missing, grant it:
               
               gcloud projects add-iam-policy-binding PROJECT_ID \
                   --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-gkenode.iam.gserviceaccount.com" \
                   --role="roles/container.defaultNodeServiceAgent"
               




## Troubleshoot resource and performance issues

If logs are missing intermittently or are dropped from high-traffic nodes, the cause might not be a misconfiguration, but a performance issue. Use the following sections to investigate whether your project is exceeding API quotas or if high log volume is overwhelming the agents on specific nodes.

### Investigate Cloud Logging API quota usage

To protect the service, Cloud Logging enforces a write quota on all projects, limiting the total volume of logs that Cloud Logging can ingest per minute.

**Symptoms** :

  * Logs are intermittently or completely missing.
  * You see `RESOURCE_EXHAUSTED` errors related to `logging.googleapis.com` in node or logging agent logs.



**Cause** :

The project is exceeding the Cloud Logging API write requests quota. This issue prevents the logging agent from sending logs.

**Resolution** :

To check the quota usage and request an increase, do the following:

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the  filter_list **Filter** field, type `Cloud Logging API` and press `Enter`.

  3. In the filtered list, find the quota for **Log write bytes per minute per region** for the region that your cluster is in.

  4. Review the values in the **Current usage percentage** column. If usage is at or near the limit, you've likely exceeded the quota.

  5. To request an increase, click **Edit quota** , and follow the prompts. For more information, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).




To reduce usage, consider [excluding logs](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) or reducing log verbosity from applications. You can also set up [alerting policies](https://docs.cloud.google.com/docs/quota_detail/monitor#quota_alerts) to be notified before reaching the limit.

### Investigate node throughput and resource usage

The GKE logging agent on each node has its own throughput limit, which can be exceeded.

**Symptoms** :

Logs from specific nodes are intermittently missing or delayed, particularly during periods of high cluster activity or heavy node resource usage.

**Cause** :

The GKE logging agent has a default throughput limit (approximately 100 KBps per node). If applications on a node generate logs faster than this limit, the agent might drop logs, even if the project's overall API quota isn't exceeded. You can monitor node logging throughput by using the `kubernetes.io/node/logs/input_bytes` metric in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

Logs might also be missing if the node is under heavy CPU or memory pressure, leaving insufficient resources for the agent to process logs.

**Resolution** :

To reduce throughput, select one of the following options:

###  Standard clusters 

Try the following solutions:

  * **Enable high throughput logging** : this feature increases the per-node capacity. For more information, see [Adjust Cloud Logging agent throughput](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/adjust-log-throughput).

  * **Reduce log volume** : analyze application logging patterns. Reduce unnecessary or excessively verbose logging.

  * **Deploy a custom logging agent** : you can deploy and manage your own customized Fluent Bit DaemonSet, but you are then responsible for its configuration and maintenance.

  * **Check node resource usage** : even if the log volume is within limits, ensure the nodes aren't under heavy CPU or memory pressure. Insufficient node resources can hinder the logging agent's ability to process and send logs. You can check metrics like `kubernetes.io/node/cpu/core_usage_time` and `kubernetes.io/node/memory/used_bytes` in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).




###  Autopilot clusters 

Try the following solutions:

  * **Reduce log volume** : analyze your application logging patterns. Reduce unnecessary or excessively verbose logging. Ensure logs are structured where possible, because these types of logs can help with efficient processing. Exclude logs that aren't essential.

  * **Optimize application performance** : because node resources are managed in Autopilot clusters, ensure your applications aren't excessively consuming CPU or memory, which could indirectly affect the performance of node components like the logging agent. Although you don't manage nodes directly, application efficiency affects overall node health.




## Troubleshoot filtering and application issues

When your application successfully generates logs, but they still don't appear in Cloud Logging, the issue is often caused by filtering or the application's logging behavior. The following sections explore issues like log exclusion filters, container-level buffering, restrictive search queries, and applications not writing to `stdout` or `stderr`.

### Investigate log exclusion filters

The Logs Explorer only shows logs that match all filters in your query and the selected time range.

**Symptoms** :

Specific logs that match certain criteria are missing from Cloud Logging, but other logs from the same sources are present.

**Cause** :

Log exclusion filters are defined in your Cloud Logging sinks (often the `_Default` sink). These rules silently drop logs that match specific criteria, even if they were successfully sent by the node.

**Resolution** :

To review and modify exclusion filters, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Logs Router** page.

[Go to Logs Router](https://console.cloud.google.com/logs/router)

  2. Identify the problematic filter:

     1. For each sink (besides the `_Required` sink, which can't have exclusion filters) click more_vert **More actions** and select **View sink details**.
     2. Review the queries in the **Exclusion filters** section. Compare the filter logic against the attributes of your missing logs (for example, resource type, labels, or keywords).
     3. Copy the exclusion filter query.
     4. Go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

     5. Paste the exclusion filter query into the query pane and click **Run query**.

     6. Review the results. The logs displayed are what the filter _would exclude_. If your missing logs appear in these results, then this filter is likely the cause.

  3. Disable or edit the filter:

     1. Return to the **Logs Router** page.
     2. Click more_vert **More actions** for the sink with the suspect filter and select **Edit sink**.
     3. Locate the **Choose logs to filter out of sink** section and find the exclusion filter.
     4. You can either click **Disable** to disable the filter, or modify its query to be more specific.
     5. Click **Update sink**. Changes apply to new logs.



###  gcloud 

  1. List all sinks in the project:
         
         gcloud logging sinks list --project=PROJECT_ID
         

  2. View each sink's exclusion filters:
         
         gcloud logging sinks describe SINK_NAME --project=PROJECT_ID
         

In the output, review the `exclusions` section. Compare the filter logic against the attributes of your missing logs (for example, resource type, labels, or keywords).

  3. To modify exclusions, update the sink's configuration:

     1. Export the sink's configuration to a local file (for example, `sink-config.yaml`):
            
            gcloud logging sinks describe SINK_NAME \
                --format=yaml > sink-config.yaml
            

     2. Open the `sink-config.yaml` file in a text editor.

     3. Find the `exclusions:` section and remove or modify the problematic filter.

     4. Update the modified sink:
            
            gcloud logging sinks update SINK_NAME sink-config.yaml \
                --project=PROJECT_ID
            

For more information about this command, see the [`gcloud logging sinks update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update) documentation.




### Investigate container log buffering and delays

Applications and operating systems often use buffering to write data in chunks instead of line-by-line, which can improve performance.

**Symptoms** :

  * Logs from specific containers appear in Cloud Logging only after the container exits, or there's a significant delay in the logs appearing.
  * Sometimes, logs are incomplete.



**Cause** :

This issue is often caused by log buffering. Although standard output (`stdout`) is typically line-buffered when connected to a terminal, this behavior changes when output is piped. If an application's logs or startup scripts within a container pipe `stdout` to other commands (for example, `my-app | grep ...`), the output might become fully buffered. As a result, logs are held until the buffer is full or the pipe closes. This behavior can cause delays or data loss if the container terminates unexpectedly. Application-internal buffering can also cause delays.

**Resolution** :

To resolve the issue, try the following solutions:

  * **Avoid piping`stdout`**: if possible, modify container entry points or application commands to write logs directly to `stdout` or `stderr` without piping through other commands like `grep` or `sed` within the container.
  * **Ensure line buffering** : 
    * If piping is unavoidable, use tools that support line buffering. For example, use `grep --line-buffered`.
    * For custom applications, ensure they flush logs frequently, ideally after each line, when they write to `stdout`. Many logging libraries have settings to control buffering.
  * **Test buffering behavior** : deploy the following Pod manifest and observe the effects in the logs by using the `kubectl logs -f buffered-pod` command. Experiment by commenting and uncommenting the different `command` arrays in the `buffered-container` manifest:
        
        # buffered.yaml
        apiVersion: v1
        kind: ConfigMap
        metadata:
        name: run-script
        data:
        run.sh: |
            #!/bin/bash
            echo "Starting..."
            for i in $(seq 3600); do
            echo "Log ${i}"
            sleep 1
            done
            echo "Exiting."
        ---
        apiVersion: v1
        kind: Pod
        metadata:
        name: buffered-pod
        spec:
        containers:
            - name: buffered-container
            image: ubuntu  # Or any other image with bash
        
            # Case 1: Direct execution - line buffered by default to TTY
            # Logs appear immediately.
            command: ['/bin/bash', '-c', '/mnt/run.sh']
        
            # Case 2: Piped to grep - fully buffered by default
            # Logs might be delayed or appear in chunks.
            # command: ['/bin/bash', '-c', '/mnt/run.sh | grep Log']
        
            # Case 3: Piped to grep with --line-buffered
            # Logs appear immediately.
            # command: ['/bin/bash', '-c', '/mnt/run.sh | grep --line-buffered Log']
        
            volumeMounts:
                - name: scripts
                mountPath: /mnt
        volumes:
            - name: scripts
            configMap:
                name: run-script
                defaultMode: 0777
        restartPolicy: Never
        




### Investigate Logs Explorer queries

If you are confident your logs are being collected but you can't find them, your search query or time range might be the issue.

**Symptoms** :

Expected logs aren't appearing in search results, even though you know the application is generating them.

**Cause** :

Your query in the Logs Explorer might have filters (for example, on namespaces, labels, resource types, or text) that inadvertently exclude the logs that you're looking for.

**Resolution** :

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logging/logs)

  2. Click **Pick time range**. Even if you think you know when the logs occurred, try a significantly broader range to rule out timing issues.

  3. Simplify the query:

     1. Clear all filters.
     2. Try filtering by your cluster only:
            
            resource.type="k8s_container"
            resource.labels.cluster_name="CLUSTER_NAME"
            resource.labels.location="LOCATION"
            

Replace the following:

        * `CLUSTER_NAME`: the name of your cluster.
        * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a` ) for the cluster.
     3. Click **Run query**.

  4. If the broad query works, re-introduce your original filters one by one:

     * **Resource type** : make sure that you use the correct resource type. For example, are you filtering by `k8s_container` when you should be filtering by `k8s_node`?
     * **Labels** : double-check spellings for `resource.labels` such as `namespace_name`, `container_name`, or custom labels.
     * **Severity** : make sure the severity level (for example, `severity=ERROR`) isn't too restrictive.
     * **Text payload** : check for spelling mistakes and overly restrictive strings in search terms. For example, use `:` for "contains" instead of `=` for an exact match (`jsonPayload.message:"error"` instead of `jsonPayload.message="error"`).
  5. Verify that your filters account for case sensitivity (text is usually case-insensitive, but labels might not be), ensure values have no hidden characters or extra spaces, and check if terms with special characters need to be enclosed in quotes.

  6. Review the **Timeline**. Sudden drops when adding a filter can help you to identify the problematic part of the query.




For more advice about effective logging queries, see [Finding log entries quickly](https://docs.cloud.google.com/logging/docs/view/logging-query-language#finding-quickly) in the Cloud Logging documentation.

If you still can't find the logs after you refine your query, the issue might not be the query, but a problem described in other sections of this document.

### Investigate application-specific logging behavior

The GKE logging agent only collects logs written to the `stdout` and `stderr` streams.

**Symptoms** :

No logs for a specific Pod or container are visible in Cloud Logging, even though other logs from the cluster are present.

**Cause** :

The application isn't writing to `stdout` or `stderr`. It might be misconfigured to write logs to a file inside the container, where the logging agent can't collect them.

The application might also be mixing JSON and non-JSON text in its output. The logging agent's parser expects a consistent format (JSON or text) from a single stream. If an application configured for JSON logging outputs a plain-text line, it can break the parser, causing logs to be dropped or ingested incorrectly.

**Resolution** :

  1. Determine the Pod name and namespace of the application whose logs are missing:
         
         kubectl get pods -n NAMESPACE_NAME
         

  2. Check container logs:

     * If the Pod has a single container, run the following command:
           
           kubectl logs POD_NAME \
               -n NAMESPACE_NAME
           

Replace the following:

       * `POD_NAME`: the name of your Pod.
       * `NAMESPACE_NAME`: the namespace of your Pod.
     * If the Pod has multiple containers, specify the container name:
           
           kubectl logs POD_NAME \
               -c CONTAINER_NAME \
               -n NAMESPACE_NAME
           

Replace `CONTAINER_NAME` with the name of the container within the Pod.

     * To follow logs in real-time, run the following command:
           
           kubectl logs -f POD_NAME \
               -c CONTAINER_NAME \
               -n NAMESPACE_NAME
           

Replace the following:

       * `POD_NAME`: the name of your Pod.
       * `CONTAINER_NAME`: the name of the container within the Pod.
       * `NAMESPACE_NAME`: the namespace of your Pod.
  3. Analyze the output:

     * If the `kubectl logs` command has no output or if the command output doesn't contain the expected logs, then the problem is with the application itself. The `kubectl logs` command reads directly from the `stdout` and `stderr` streams captured by the container runtime. If logs aren't here, GKE's logging agent can't see them.

Change your application's code or configuration to stop writing to a file and instead log all messages directly to `stdout` (for regular logs) and `stderr` (for error logs).

     * If you see a mix of JSON strings and plain text lines, this output indicates a mixed-format issue. Configure your application to only write valid, single-line JSON objects to `stdout` and `stderr`.

     * If the `kubectl logs` command _does_ show the expected logs, then the issue is likely further down the logging pipeline (for example, agent, permissions, or Cloud Logging service).




## Troubleshoot platform and service issues

The following sections help you investigate issues external to your immediate configuration, such as log retention policies, Cloud Logging health, or unsupported GKE versions.

### Investigate log retention periods

Logs are stored in buckets, and each bucket has a retention period that defines how long its logs are kept before being automatically deleted.

**Symptoms** :

Logs older than a certain date are missing.

**Cause** :

The logs that you're searching for are older than the retention period for the log bucket that they were routed to.

**Resolution** :

To identify and update the retention period, select one of the following options:

###  Console 

  1. Identify the bucket to which your GKE logs are routed to:

     1. In the Google Cloud console, go to the **Logs Router** page.

[Go to Logs Router](https://console.cloud.google.com/logs/router)

     2. Review the **Destination** column, which shows where the logs are being routed.

The destination looks similar to the following:
            
            logging.googleapis.com/projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID
            

Note the `PROJECT_ID`, `LOCATION`, and `BUCKET_ID`.

Logs are often routed to the `_Default` bucket, but might also be routed to other buckets if you have custom sinks configured.

  2. Check the log bucket retention period:

     1. In the Google Cloud console, go to the **Logs Storage** page.

[Go to Logs Storage](https://console.cloud.google.com/logs/storage)

     2. Find the buckets matching the `BUCKET_ID`, `LOCATION`, and `PROJECT_ID` from the sink's destination.

     3. For each relevant bucket, view the **Retention period** column.

     4. If the logs that you want to view are older than the retention period, then Cloud Logging has deleted them. If you need a longer retention period, do the following:

        1. For the bucket whose retention period you want to extend, click more_vert **More actions**.
        2. Select **Edit bucket** , and update the retention period. Be aware of [potential cost implications](https://cloud.google.com/stackdriver/pricing#logs-storage).



###  gcloud 

  1. Identify the bucket to which your GKE logs are routed to:
         
         gcloud logging sinks list --project=PROJECT_ID
         

Review the output. The `destination` field for each sink shows where the logs are being routed. The destination format for a log bucket is:
         
         logging.googleapis.com/projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID
         

Note the `PROJECT_ID`, `LOCATION`, and `BUCKET_ID`.

Logs are often routed to the `_Default` bucket.

  2. Check the log bucket retention period:
         
         gcloud logging buckets describe BUCKET_ID \
             --location=LOCATION \
             --project=PROJECT_ID
         

In the output, look for the `retentionDays` field. If the logs that you need are older than the value listed for `retentionDays`, then Cloud Logging has deleted them.

  3. If you need a longer retention period, update it:
         
         gcloud logging buckets update BUCKET_ID \
             --location=LOCATION \
             --retention-days=RETENTION_DAYS \
             --project=PROJECT_ID
         

Replace the following:

     * `BUCKET_ID`: the ID of the log bucket.
     * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a` ) for the bucket.
     * `RETENTION_DAYS`: the number of days to retain logs. Be aware of [potential cost implications](https://cloud.google.com/stackdriver/pricing#logs-storage) for increasing the retention period.
     * `PROJECT_ID`: your Google Cloud project ID.



### Investigate Cloud Logging service issues and ingestion delays

Sometimes, the logging pipeline itself might experience issues, either from a service-wide disruption or a temporary, large-scale ingestion delay.

**Symptoms** :

  * Widespread or intermittent log loss across multiple projects or clusters.
  * Logs are significantly delayed in appearing in Logs Explorer.



**Cause** :

  * **Cloud Logging service disruption** : a rare, service-wide disruption can prevent log ingestion, leading to widespread delays or total log loss.
  * **High log volume** : even without an official disruption, high log volume from your project or region can temporarily overwhelm the ingestion service, causing logs to be delayed in appearing.



**Resolution** :

  * Check the status of Google Cloud services by visiting the [Google Cloud Service Health dashboard](https://status.cloud.google.com/). Look for any open incidents related to Cloud Logging or GKE.

  * Account for potential ingestion delays. If logs aren't immediately visible, and there are no active incidents, allow some time for ingestion, especially if the log volume is high. Check again after a few minutes.




### Investigate cluster version

GKE regularly releases new versions that include bug fixes and performance improvements for components, including the logging agent.

**Symptoms** :

Logging issues coincide with cluster version limitations.

**Cause** :

The cluster might be running an older or unsupported GKE version that has known logging agent issues or lacks certain logging features.

**Resolution** :

To resolve this issue, do the following:

  1. Check your cluster's version:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location LOCATION \
             --format="value(currentMasterVersion)"
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a` ) for the cluster.
  2. To ensure it's a supported version, compare this version against the [GKE Release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).

  3. If the cluster is using an unsupported version, [upgrade your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).




## Verify that the logs are collected

Verify that the logs you expect are collected. For a description of collected logs, see [What logs are collected](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#what_logs).

For example, in the audit logs, the `command.gke.io/dryRun` label helps you distinguish between logs from dry run requests and logs from requests that modified resources.

The logs with these labels are produced when you run a `kubectl` command with the [`--dry-run=server`](https://github.com/kubernetes/enhancements/blob/master/keps/sig-api-machinery/576-dry-run/README.md#kubectl) flag. However, `kubectl` commands with the `--dry-run=client` flag don't produce logs because they don't make requests to the Kubernetes API server.

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
