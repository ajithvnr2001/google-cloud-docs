---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/admin-workflow/
title: Configure a cluster and workload for staging \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:35:19.866354+00:00
---

# Configure a cluster and workload for staging  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/admin-workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure a cluster and workload for staging Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

While GKE clusters in Autopilot mode provide reasonable defaults for most settings, it's likely that you'll need different settings in your development, staging, and production environments. 

## Objectives

Learn some basic tasks for configuring a staging and testing cluster: 

  1. Limit access to the cluster's administrative service, which is called the _control plane_. This prevents unauthorized users from viewing or changing cluster and workload settings.

  2. Specify that your app needs computing resources that efficiently scale up and down to meet demand.

  3. Test autoscaling, which automatically replicates Pods when demand increases beyond a threshold you specify.

  4. Adjust log retention so you only keep the logs you need.

  5. Enable the GKE security posture dashboard.




These are just some of the tasks for promoting a cluster from development to staging. Read the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs) for the full list of tasks to consider.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/kubernetes/list/overview?journey_id=kubernetes--admin-workflow--intro)

* * *

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Create a Kubernetes cluster and deploy a workload. [Create a cluster and deploy a workload](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster) shows you how.

## Limit access to the control plane

To improve your security posture, allow only an authorized network and Google Cloud console and Cloud Shell to access your cluster's control plane.

### Configure an authorized network

  1. In the Google Cloud console, go to the GKE **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. In the **Name** column, click the name of your cluster, **hello-world-cluster**.

  3. In the **Control plane authorized networks** row of the Networking table, click edit **Edit**.

  4. In the Edit control plane authorized networks dialog, select **Enable control plane authorized networks**.

  5. Select **Allow access through Google Cloud public IP addresses**.

This lets you manage the cluster from Google Cloud console and Cloud Shell

  6. Click **Add authorized network**.

  7. Enter a name, such as **My example on-prem network**.

  8. In **Network** , enter the range of IP addresses that you want to grant access to your cluster's control plane. Use CIDR notation.

For example, enter the following range:
         
         198.51.100.0/24
         

  9. Click **Done**.

  10. Click **Save changes**.

This operation takes a few minutes to complete.

  11. Click the Notifications button and wait until you see a green check mark next to **Update control plane authorized networks setting in Kubernetes Engine cluster "hello-world-cluster"**.




You have configured a cluster control plane that is accessible only from your authorized network and from Google Cloud public IP addresses (which lets you manage the cluster from Google Cloud console and Cloud Shell).

To see the IP address of your cluster's control plane and confirm the addresses of the authorized network, click **Next**.

### View IP addresses

  1. Go to the GKE **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. In the **Name** column, click the name of your cluster, **hello-world-cluster**.

  3. In the **Cluster basics** table, the **External endpoint** row shows the IP address of the cluster's control plane.

  4. In the **Networking** table, the **Control plane authorized networks** row shows the IP addresses of your authorized network.




Your cluster's control plane can now only be accessed from an authorized network, Google Cloud console, and Cloud Shell.

## Specify a compute class

By default, GKE Autopilot Pods use compute resources that are optimized for general-purpose workloads. For workloads that need to scale optimally or that have other unique requirements, you can specify a different compute class.

### Update the Deployment specification

  1. In the Google Cloud console, go to the GKE **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. In the **Name** column, click the name of the app you deployed, **hello-world-app**.

  3. Click Edit to edit the deployment specification.

  4. In the **YAML** tab, find the line that starts with `containers:`

  5. Just above this line, add the following lines:
         
         nodeSelector:
           cloud.google.com/compute-class: "Scale-Out"
         

Make sure your file matches the indentation in the following example:
         
         apiVersion: apps/v1
          kind: Deployment
          ...
          spec:
          ...
            template:
            ...
              spec:
                nodeSelector:
                  cloud.google.com/compute-class: "Scale-Out"
                containers:
                - name: hello-app
                  image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
         

  6. To download this file and use it as the basis for other workload configurations, click Download.

  7. Click **Save**.




Any Pod replicas that are created to run your workload will use the compute class you specified.

## Test autoscaling

Now that you have a workload that can scale efficiently, update autoscaling settings to more easily cause your workload to scale up. Then generate load to trigger autoscaling.

### Update Pod autoscaling settings

  1. Go to the GKE **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. In the **Name** column, click the name of your deployment, **hello-world-app**.

  3. Click Actions.

  4. Select **Autoscale** and click **Horizontal pod autoscaling**.

  5. In the **Configure Horizontal Pod Autoscaler** dialog, under **Autoscaling metrics** , click **CPU**.

  6. Change the value of **Target** to 2, which automatically scales up your Pods when they use at least 2% of their configured CPU resources. This low target value ensures that you can easily trigger autoscaling in the next step.

  7. Click **Save**.




To trigger autoscaling, click **Next**.

### Generate load to trigger autoscaling

  1. Open Cloud Shell by clicking **Cloud Shell**.

  2. Paste the following command into Cloud Shell:
         
         for i in $(seq -s' ' 1 10000); do wget -q -O- <var>external-IP-address</var>; done
         

Replace external-IP-address with the IP address that appears in the Endpoints column.

  3. Press Enter to run the command and send 10,000 requests to hello-world-app.

  4. Wait for the `wget` command to finish running and the command-line prompt to reappear.

  5. You can close Cloud Shell when the `wget` command finishes.




To watch your workload scale to accommodate the increased traffic, click **Next**.

### Watch your workload scale

  1. On the **Deployment details** page for your workload, look in the CPU chart for a spike in CPU usage.

You might need to wait up to 5 minutes to see the spike.

  2. Click refreshRefresh to make sure the **Deployment details** page shows the latest data.

  3. Look in the **Managed Pods** table to see that three replicas of your workload are now running.

You might initially see errors about unschedulable Pods, but these messages are transient as the replicas start up.

  4. You can wait for about 10 minutes, click refresh**Refresh** , and see that CPU usage has dropped and so the number of Pods in **Managed Pods** returns to one.




You have tested autoscaling and watched your workload scale.

## Adjust logs retention

By default, Cloud Logging ingests all logs from your GKE clusters. Ingesting large amounts of logs data could result in a fee. To ensure that you're only ingesting the logs data that you need for the staging environment, adjust logs retention.

### Create a logs filter

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

Notice that the Query results pane shows logs from all resources in your project.

  2. Above the query results:

     1. Click Resource.

     2. Search for **Kubernetes cluster** , then click it.

     3. Click **us-central-1**.

     4. Click **hello-world-cluster**.

     5. Click **Apply**.

  3. Click Severity and select **Info** (which changes to **Info and higher** on hover).

  4. Click Run query.

  5. Note that **Query results** now only contains INFO messages from your staging cluster.

  6. Copy the query from the query editor. You'll paste this query when you create a filter for your log sink.




To create a log sink and storage bucket, click **Next**.

### Create a log sink and storage bucket

  1. Go to the Logging **Log router** page.

[Go to Log router](https://console.cloud.google.com/logs/router)

  2. Click Create sink.

  3. In **Name** , enter the following name:
         
         hello-world-cluster-sink
         

  4. Click **Next**.

  5. In **Select sink service** , select **Logging bucket**.

  6. In **Select a log bucket** , select **Create new log bucket**.

  7. In **Bucket details** , enter a unique name, such as:
         
         hello-world-bucket-<var>user-id</var>
         

  8. Click **Create bucket**.

  9. Under **Sink destination** , click **Next**.

  10. In **Build inclusion filter** , paste the query you created in the Logs Explorer.

  11. Click **Create sink**.




To view your cluster's logs, which are stored in the log bucket you created, click **Next**.

### View your cluster's logs

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Click Refine scope.

  3. Select **Log View**.

  4. Select the **_AllLogs** view for your log bucket.

  5. Click **Apply**.

**Query results** shows only the logs that are stored in your log bucket.




You have adjusted the logs retention so your staging cluster doesn't store DEBUG messages. You can [set permissions](https://docs.cloud.google.com/logging/docs/logs-views) so that only certain users can view the logs in your cluster's bucket.

## Enable the security posture dashboard

The security posture dashboard scans your GKE clusters and workloads to provide you with opinionated, actionable recommendations to improve your security posture.

### Explore any concerns

  1. Go to the GKE **Security posture** page.

[Go to Security posture](https://console.cloud.google.com/kubernetes/security/dashboard)

  2. If you are asked to enable the Container Security API, click **Enable**.

  3. The **Dashboards** tab summarizes concerns for your project's clusters and workloads.

  4. Click the **Concerns** tab.

  5. If any concerns appear on the tab, click the concern for more information.




You have completed some of the basic tasks for configuring a cluster for staging and testing your app.

## What's next

  * [Guidelines for creating scalable clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/scalability)

  * [Clean up to avoid billing charges](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/learning-path-cleanup). If you plan to take additional tutorials, wait until you finish those tutorials before you clean up. You can use the sample Kubernetes cluster in most GKE tutorials.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
