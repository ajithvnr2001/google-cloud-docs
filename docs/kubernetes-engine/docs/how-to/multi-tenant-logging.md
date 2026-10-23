---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-tenant-logging/
title: Set up multi-tenant logging \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:27.421189+00:00
---

# Set up multi-tenant logging  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-tenant-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Set up multi-tenant logging Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to configure multi-tenant logging for Google Kubernetes Engine (GKE) clusters.

It's common for multiple teams to share a single GKE cluster. Sharing a cluster provides multiple advantages including easier service discovery, simplified security, and it means that cluster administrators have fewer clusters to maintain. Individual application teams often have their own separate [project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), however. This structure, having a main GKE cluster, but separate namespaces for each application team, is called multi-tenancy. The application team's project is called the _tenant_.

With Google Cloud, GKE cluster admins can create a system where logs for the cluster remain in the main GKE project, and tenant logs are distributed to tenant projects. To configure your logs this way, use the [Log Router](https://docs.cloud.google.com/logging/docs/routing/overview). The Log Router gives you control over how logs flow within your Google Cloud project and how logs are routed to supported destinations.

To create tenant-specific logs, the cluster admin creates a [sink](https://docs.cloud.google.com/logging/docs/export) to route log entries to each tenant's project. In each tenant project, individual teams can control how the logs are stored and used, such as monitoring the logs by configuring log-based metrics and log-based alerts.

We recommend that `_Default` sinks in main GKE projects include an [exclusion filter](https://docs.cloud.google.com/logging/docs/exclusions). The exclusion filter prevents tenant logs from being ingested in both the main GKE project and the tenant project.

## Prerequisites

  * Become familiar with the following documents about multi-tenancy and routing: 
    * [Best practices for enterprise multi-tenancy on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy)
    * [Route and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview)
    * [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2)
  * Ensure that you have an existing tenant project and main project.



## Configure multi-tenant logging

You can configure multi-tenant logging by using the Google Cloud CLI or the Google Cloud console.

### gcloud

To configure multi-tenant logging for GKE clusters, complete the following steps:

  1. Set the following environment variables:
         
         export TENANT_NAMESPACE="TENANT_NAMESPACE"
         export MAIN_PROJECT="MAIN_PROJECT_ID"
         export TENANT_PROJECT="TENANT_PROJECT_ID"
         

Replace the following:

     * `TENANT_NAMESPACE`: the name for the tenant project namespace
     * `MAIN_PROJECT_ID`: the project ID for your main project
     * `TENANT_PROJECT_ID`: the project ID for your tenant project
  2. Create a namespace in your multi-tenant cluster:
         
         kubectl create namespace $TENANT_NAMESPACE
         

  3. Create a log sink in the _main_ GKE project:
         
         gcloud logging sinks create gke-$TENANT_NAMESPACE-sink \
         logging.googleapis.com/projects/$TENANT_PROJECT \
             --project=$MAIN_PROJECT \
             --log-filter=resource.labels.namespace_name="$TENANT_NAMESPACE" \
             --description="Log sink to $TENANT_PROJECT for $TENANT_NAMESPACE namespace"
         

This command creates a log sink that sends all logs that are related to the `$TENANT_NAMESPACE` namespace to the tenant project.

You might need to use a more restrictive `--log-filter`. For example, if your cluster and tenant have the same namespace, then add a cluster filter.

For more information about these fields, see the [`gcloud logging sinks create` API documentation](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/create).

  4. Get the writer identity from the sink in the main project and assign it to an environment variable.
         
         export SERVICE_ACCOUNT=$(gcloud logging sinks describe gke-$TENANT_NAMESPACE-sink \
             --project=$MAIN_PROJECT \
             --format='value(writerIdentity)')
         

  5. Grant the [Logs Writer](https://docs.cloud.google.com/logging/docs/access-control#logging.logWriter) (`logging.bucketWriter`) role to the service account used by the sink. The following command grants the main project permissions to write logs to the tenant project:
         
         gcloud projects add-iam-policy-binding $TENANT_PROJECT \
              --member=$SERVICE_ACCOUNT --role='roles/logging.logWriter' \
              --condition="expression=resource.name.endsWith(\"projects/$TENANT_PROJECT\"),title=Log writer for $TENANT_NAMESPACE,description=Grants Logs Writer role to service account $SERVICE_ACCOUNT used by gke-$TENANT_NAMESPACE-sink"
         

For more information about these fields, see the [`gcloud projects add-iam-policy-binding` API documentation](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).

  6. Optionally, create an exclusion filter for the sink that routes logs to the `_Default` bucket of the main project. If you don't create an exclusion filter on the `_Default` bucket, then the routed logs appear in both the `_Default` bucket of the main project and the tenant log bucket. To create an exclusion filter, do the following:
         
         gcloud logging sinks update _Default --project=$MAIN_PROJECT \
             --add-exclusion="name=gke-$TENANT_NAMESPACE-default-exclusion,description=\"Exclusion filter on the _Default bucket for $TENANT_NAMESPACE\",filter=resource.labels.namespace_name=\"$TENANT_NAMESPACE\""
         

For more information about these fields, see the [`gcloud logging sinks update` API documentation](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update).




### Console

To implement multi-tenant logging for GKE, complete the following steps:

  1. Create the log sink in the main project:

     1. Use the Google Cloud console project picker to select the main GKE project.
     2. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

     3. In the **Log Router** page, click **Create sink**.
     4. Enter a **Name** and **Description** for your sink and then click **Next**.
     5. In the **Select sink service** menu, select **Other project**.
     6. In the **Sink destination** field, add the following destination:
            
            logging.googleapis.com/projects/TENANT_PROJECT_ID
            

Replace `TENANT_PROJECT_ID` with the project ID of your tenant project.

     7. Click **Next**.

     8. In the **Build inclusion filter** add the following filter:
            
            resource.labels.namespace_name="TENANT_NAMESPACE"
            

Replace TENANT_NAMESPACE with the name of your tenant project's namespace.

You might want a more restrictive inclusion filter. For example, when your cluster and tenant have the same namespace, consider adding a clause to include only log entries for a specific cluster.

     9. Click **Create sink**. Your new sink appears in the **Log Router Sinks** list.

  2. Copy the sink's writer identity to your clipboard:

     1. In the **Log Router** page, locate the log sink.
     2. For that sink, click more_vert **More** , and then select **View sink details**.
     3. In the **Sink details** pane, locate the **Writer identity** field, and then copy the value into your clipboard. Omit `serviceAccount:` from the copied value.
**Note:** If the **Writer identity** field for your sink lists the value of **None** , then the sink is routing log entries to a log bucket in the current Google Cloud project. That is, you haven't configured the sink to route log entries to a tenant project. For information about how to route log entries to a log bucket in the same Google Cloud project, see [Configure and manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).
  3. In the tenant project, grant the [Logs Writer](https://docs.cloud.google.com/logging/docs/access-control#logging.logWriter) (`roles/logging.logWriter`) role to the service account used by the main project's sink. The main project needs this permission to write logs to the tenant project.

     1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

     2. Click **Grant access**.
     3. In the **New principals** field, add the sink's service account.
     4. From the **Select a role** drop-down, select **Logging** and choose **Logs Writer**.
     5. Click **Save**.
  4. Optionally, create an exclusion filter in the `_Default` bucket of the main project to prevent logs that are routed to a tenant project from being written to the `_Default` log bucket in the main project:

     1. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

     2. Next to the `_Default` bucket, click more_vert **More** and select **Edit sink**.
     3. In the **Choose logs to filter out of sink** section, click **Add exclusion**.
     4. Add a filter name.
     5. In the **Build an exclusion filter** box, add the following:
            
            resource.labels.namespace_name="TENANT_NAMESPACE"
            

     6. Click **Update sink**.




## Verify tenant logs

After you have begun using workloads that use TENANT_NAMESPACE, you can verify that the tenant project is receiving tenant-specific logs:

  1. Select the tenant project by using the Google Cloud console project picker.
  2. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  3. In the query-editor field, run the following query:
         
         resource.labels.namespace_name="TENANT_NAMESPACE"
         

In the **Query results** pane, you should see tenant-specific logs that were routed from the main project.




## Use tenant logs

In the tenant projects, each team can control how the logs are routed, stored, and analyzed. After the logs are routed to the tenant projects, the individual application teams can choose to route their logs to supported destinations like Logging buckets, or to third-party destinations by using Pub/Sub. For information about routing log entries, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

Individual application teams can also set up alerts based on the contents of logs, or metrics derived from logs. For more information, see [Monitor your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs).

## Clean up

You can remove the objects you created for multi-tenant logging by using `gcloud` or the Google Cloud console.

**Important:** Make sure there are no Pods running in the tenant namespace before executing these commands.

### gcloud

To remove the objects you created for multi-tenant logging, complete the following steps:

  1. Set variables to simplify the following commands:
         
         export TENANT_NAMESPACE="TENANT_NAMESPACE"
         export MAIN_PROJECT="MAIN_PROJECT_ID"
         export TENANT_PROJECT="TENANT_PROJECT_ID"
         

Replace the following:

     * `TENANT_NAMESPACE`: the name for the tenant project namespace
     * `MAIN-PROJECT-ID`: the project ID for your main project
     * `TENANT-PROJECT-ID`: the project ID for your tenant project
  2. Remove the [Logs Writer](https://docs.cloud.google.com/logging/docs/access-control#logging.logWriter) (`roles/logging.logWriter`) role from the service account in the tenant project:
         
         export SERVICE_ACCOUNT=$(gcloud logging sinks describe gke-$TENANT_NAMESPACE-sink \
             --project=$MAIN_PROJECT | \
             --format='value(writerIdentity)'
         
         gcloud projects remove-iam-policy-binding $TENANT_PROJECT \
             --member=$SERVICE_ACCOUNT \
             --role='roles/logging.logWriter' \
             --all
         

  3. Delete the log sink:
         
         gcloud logging sinks delete gke-$TENANT_NAMESPACE-sink \
             --project=$MAIN_PROJECT
         

  4. Delete the namespace:
         
         kubectl delete namespace $TENANT_NAMESPACE
         




### Console

  1. In the tenant project, remove the [Logs Writer](https://docs.cloud.google.com/logging/docs/access-control#logging.logWriter) (`roles/logging.logWriter`) role from the service account:

     1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

     2. For the service account you want to delete, click _edit_ **Edit principal**.
     3. In the **Edit access** panel, click delete **Delete role** next to the Logs Writer role and click **Save**.
  2. In the main project, delete the log sink:

     1. Use the Google Cloud console project picker to select the tenant GKE project.
     2. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

     3. For the sink you want to delete, click _more_vert_ **More**.
     4. Select **Delete sink**.
     5. In the confirmation panel, click **Delete**.



## Limitations

Multi-tenant logging has the following limitations:

  * The quota for the number of log sinks per project is 200\. If you require more than 200 tenants, request a quota increase by opening a [support case](https://docs.cloud.google.com/support/docs/customer-care-procedures).
  * There is a limit of 50 exclusion filters per log bucket. If you intend to have more than 50 tenants, the exclusion filter approach for the `_Default` bucket needs to be revised. As an alternative, you might do the following:

    * Create a single exclusion filter that excludes all non-system or non-default namespaces using this command:
          
          gcloud logging sinks update _Default \
          --project=$MAIN_PROJECT \
          --add-exclusion="name=gke-all-tenant-default-exclusion,description=\"Exclusion filter on the _Default bucket for all tenants\",filter=resource.labels.namespace_name !~ \"kube\" AND resource.labels.namespace_name !~ \"system\ AND resource.labels.namespace_name != \"Default\""
          

    * Duplicate logs between the tenant project and the main project by not creating the exclusion filter.




## What's next

  * Learn about [Best practices for enterprise multi-tenancy on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
