---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/dashboards/
title: Troubleshoot monitoring dashboards \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:29.804805+00:00
---

# Troubleshoot monitoring dashboards  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot monitoring dashboards Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When you can't see your Google Kubernetes Engine (GKE) monitoring dashboards in Cloud Monitoring, or they appear to be missing data, it can obstruct your ability to observe and respond to issues in your clusters and workloads.

Use this document to diagnose and resolve issues with GKE monitoring dashboards. Find guidance on verifying whether Cloud Monitoring is enabled, checking Google Cloud console and account settings, and troubleshooting logs and alerting policies for GKE resources.

This information is important for Platform admins and operators and Application developers who use Cloud Monitoring dashboards to understand the health and performance of their GKE clusters and applications. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

For more information about how to use these dashboards to troubleshoot your clusters and workloads, see [Assess cluster and workload health in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-console).

## GKE dashboards are not listed in Cloud Monitoring

By default Monitoring is enabled when you create a cluster. If you don't see GKE dashboards when you are [viewing provided Google Cloud dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards) in Monitoring, Monitoring is not enabled for clusters in the selected Google Cloud project. [Enable monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing) to view these dashboards.

**Note:** For GKE Autopilot clusters, you cannot disable the Cloud Monitoring and Cloud Logging integration.

## No Kubernetes resources are in my dashboard

If you don't see any Kubernetes resources in your GKE dashboard, then check the following:

### Selected Google Cloud project

Verify that you have selected the correct Google Cloud project from the drop-down list in the Google Cloud console menu bar to select a project. You must select the project whose data you want to see.

### Clusters activity

If you just created your cluster, wait a few minutes for it to populate with data. See [Configuring logging and monitoring for GKE](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing) for details.

### Time range

The selected time range might be too narrow. You can use the **Time** menu in the dashboard toolbar to select other time ranges or define a **Custom** range.

### Permissions to view the dashboard

If you see either of the following permission-denied error messages when viewing a service's deployment details or a Google Cloud project's metrics, you need to update your Identity and Access Management role to include **roles/monitoring.viewer** or **roles/viewer** :

  * `You do not have sufficient permissions to view this page`
  * `You don't have permissions to perform the action on the selected resources`



For more details, go to [Predefined roles](https://docs.cloud.google.com/monitoring/access-control#predefined_roles).

### Cluster and node service account permissions to write data to Monitoring and Logging

If you see high error rates in the **Enabled APIs and services** page in the Google Cloud console, then your service account might be missing the following roles:

  * `roles/logging.logWriter`: In the Google Cloud console, this role is named **Logs Writer**. For more information on Logging roles, see the [Logging access control guide](https://docs.cloud.google.com/logging/docs/access-control).

  * `roles/monitoring.metricWriter`: In the Google Cloud console, this role is named **Monitoring Metric Writer**. For more information on Monitoring roles, see the [Monitoring access control guide](https://docs.cloud.google.com/monitoring/access-control).

  * `roles/stackdriver.resourceMetadata.writer`: In the Google Cloud console, this role is named **Stackdriver Resource Metadata Writer**. This role permits write-only access to resource metadata, and it provides exactly the permissions needed by agents to send metadata. For more information on Monitoring roles, see the [Monitoring access control guide](https://docs.cloud.google.com/monitoring/access-control).




To list your service accounts, in the Google Cloud console go to **IAM and Admin** , and then select **Service Accounts**.

## Can't view logs

If you don't see your logs in dashboards, check the following:

### Agent is running and healthy

GKE version 1.17 and later use [Fluent Bit](https://fluentbit.io/) to capture logs. Fluent Bit is the Logging agent that runs on Kubernetes nodes. To check if the agent is running correctly, perform the following steps:

  1. Check whether the agent is restarting by running the following command:
         
         kubectl get pods -l k8s-app=fluentbit-gke -n kube-system
         

If there are no restarts, the output is similar to the following:
         
         NAME                  READY   STATUS    RESTARTS   AGE
         fluentbit-gke-6zr6g   2/2     Running   0          44d
         fluentbit-gke-dzh9l   2/2     Running   0          44d
         

  2. Check Pod status conditions by running the following command:
         
         JSONPATH='{range .items[*]};{@.metadata.name}:{range @.status.conditions[*]}{@.type}={@.status},{end}{end};'  \
          && kubectl get pods -l k8s-app=fluentbit-gke -n kube-system -o jsonpath="$JSONPATH" | tr ";" "\n"
         

If the deployment is healthy, the output is similar to the following:
         
         fluentbit-gke-nj4qs:Initialized=True,Ready=True,ContainersReady=True,PodScheduled=True,
         fluentbit-gke-xtcvt:Initialized=True,Ready=True,ContainersReady=True,PodScheduled=True,
         

  3. Check the Pod status, which can help determine if the deployment is healthy by running the following command:
         
         kubectl get daemonset -l k8s-app=fluentbit-gke -n kube-system
         

If the deployment is healthy, the output is similar to the following:
         
         NAME            DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
         fluentbit-gke   2         2         2       2            2           kubernetes.io/os=linux   5d19h
         

In this example output, the desired state matches the current state.




If the agent is running and healthy in these scenarios, and you still don't see all of your logs, the agent might be overloaded and dropping logs.

### Agent overloaded and dropping logs

One possible reason you're not seeing all of your logs is that the node's log volume is overloading the agent. The default Logging agent configuration in GKE is tuned for the rate of 100 kiB per second for each node, and the agent might start dropping logs if the volume exceeds that limit.

To detect if you might be hitting this limit, look for any of the following indicators:

  * View the `kubernetes.io/container/cpu/core_usage_time` metric with the filter `container_name=fluentbit-gke` to see if the CPU usage of the Logging agent is near or at 100%.

  * View the `logging.googleapis.com/byte_count` metric grouped by `metadata.system_labels.node_name` to see if any node reaches 100 kiB per second.




If you see any of these conditions, you can reduce the log volume of your nodes by adding more nodes to the cluster. If all of the log volume comes from a single pod, then you would need to reduce the volume from that pod.

For more information on investigating and resolving GKE logging related issues, see [Troubleshooting logging in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-gke-logging).

## Incident isn't matched to a GKE resource?

If you have an alerting policy condition that aggregates metrics across distinct GKE resources, you might need to edit the policy's condition to include more GKE hierarchy labels to associate incidents with specific entities.

For example, you might have two GKE clusters, one for production and one for staging, each with their own copy of service `lilbuddy-2`. When the alerting policy condition aggregates a metric across containers in both clusters, the GKE Monitoring dashboard isn't able to associate this incident uniquely with the production service or the staging service.

To resolve this situation, target the alerting policy to a specific service by adding `namespace`, `cluster`, and `location` to the policy's **Group By** field. On the event card for the alert, click the **Update alert policy** link to open the **Edit alerting policy** page for the relevant alert policy. From here, you can update the alerting policy with the additional information so that the dashboard can find the associated resource.

After you update the alerting policy, the GKE Monitoring dashboard is able to associate all future incidents with a unique service in a particular cluster, giving you additional information to diagnose the problem.

Depending on your use case, you might want to filter on some of these labels in addition to adding them to the **Group By** field. For example, if you only want alerts for your production cluster, you can filter on `cluster_name`.

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
