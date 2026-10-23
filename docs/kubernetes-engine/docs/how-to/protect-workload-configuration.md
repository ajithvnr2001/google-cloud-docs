---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protect-workload-configuration/
title: Automatically audit workloads for configuration issues \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:12.672105+00:00
---

# Automatically audit workloads for configuration issues  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protect-workload-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Automatically audit workloads for configuration issues Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to automatically audit your workload configurations for security concerns and get actionable recommendations to improve the security posture of your Google Kubernetes Engine (GKE) Autopilot and Standard clusters. This guides you through how to enable workload configuration auditing, deploy a test workload, view and action configuration audit results, and disable workload configuration auditing. It also covers the pricing, requirements, and limitations of workload configuration auditing.

This page is for Security specialists who monitor the security of their GKE clusters and want to learn more about how to automatically audit workload configurations in GKE Autopilot and Standard clusters. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, because workload configuration auditing is a feature of the security posture dashboard, ensure that you're familiar with the following concepts:

  * [General overview of the security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard)
  * [About workload configuration auditing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning)



## Pricing

The security posture dashboard is offered at no extra charge in GKE through the Container Security API.

Entries added to Cloud Logging use [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing#logging-costs).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable the Container Security API.

[Enable Container Security API](https://console.cloud.google.com/apis/enableflow?apiid=containersecurity.googleapis.com)

  * Ensure that you have an Autopilot or Standard cluster that runs version 1.21 or later. To create a new cluster, see [Creating an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).




### Requirements

  * To get the permissions that you need to use workload configuration auditing, ask your administrator to grant you the [Security Posture Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containersecurity#containersecurity.viewer) (`roles/containersecurity.viewer`) IAM role on your Google Cloud project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to use workload configuration auditing. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use workload configuration auditing:

    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`
    * `containersecurity.locations.list`
    * `containersecurity.locations.get`
    * `containersecurity.clusterSummaries.list`
    * `containersecurity.findings.list`

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * Workload configuration auditing requires GKE version 1.21 and later.

**Note:** Workload configuration auditing is automatically enabled when you create new Autopilot or Standard clusters running version 1.27 and later. For these cluster versions, skip to Deploy a test workload.

## Enable workload configuration auditing

Workload configuration auditing is enabled by default in new Autopilot and Standard clusters running version 1.27 and later. You can also manually enable this feature using the gcloud CLI or the Google Cloud console.

### Enable configuration auditing on an existing cluster

### gcloud

Update the cluster: 
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        **--security-posture =standard**

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional Standard and Autopilot clusters, or a zone for zonal Standard clusters. 



### Console

  1. Go to the **Security Posture** page in the Google Cloud console.

[Go to Security Posture](https://console.cloud.google.com/kubernetes/security/dashboard)
  2. Click the **Settings** tab.
  3. In the **Configuration audit enabled clusters** section, click **Select clusters**.
  4. Select the checkboxes for the clusters that you want to add.
  5. In the **Select action** drop-down menu, select **Set to Basic**.
  6. Click **Apply**.



You can also configure fleet-level configuration auditing settings that apply to all member clusters. For instructions, see [Configure GKE security posture dashboard features at fleet-level](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fleet-security-posture).

## Deploy a test workload

Deploy a sample application that intentionally violates the Pod Security Standards.

  1. Save the following manifest as `misconfig-sample.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: helloweb
           labels:
             app: hello
         spec:
           selector:
             matchLabels:
               app: hello
               tier: web
           template:
             metadata:
               labels:
                 app: hello
                 tier: web
             spec:
               containers:
               - name: hello-app
                 image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
                 ports:
                 - containerPort: 8080
                 **securityContext :
                   runAsNonRoot: false**
                 resources:
                   requests:
                     cpu: 200m
         

  2. Deploy the application to your cluster:
         
         kubectl apply -f misconfig-sample.yaml
         




If you want to try other violations, modify `misconfig-sample.yaml` with the corresponding "bad" configuration.

## View and action configuration audit results

The initial audit takes up to 15 minutes to return results. GKE displays the results on the security posture dashboard and automatically adds entries to the cluster logs.

### View results

To see an overview of discovered concerns across your project's clusters and workloads, do the following:

  1. Go to the **Security Posture** page in the Google Cloud console.

[Go to Security Posture](https://console.cloud.google.com/kubernetes/security/dashboard)

  2. Click the **Concerns** tab.

  3. In the **Filter concerns** pane, in the **Concern type** section, select the **Configuration** checkbox.




### View concern details and recommendations

To view detailed information about a specific configuration concern, click the row containing that concern.

The **Configuration Concern** pane shows the following information:

  * **Description:** a description of the concern.
  * **Recommended action:** an overview of actions that you can take to fix the configuration issue. This section includes the following details: 
    * Which resources need the fix
    * Sample commands that you can run to apply the fix to affected resources
    * The Google Cloud console instructions, if applicable, to fix the issue



### View logs for discovered concerns

GKE adds entries to the `_Default` log bucket in Logging for each discovered concern. These logs are only retained for a specific period. For details, see [Logs retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods).

  1. In the Google Cloud console, go to the **Logs Explorer** :

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)
  2. In the **Query** field, specify the following query:
         
         resource.type="k8s_cluster"
         jsonPayload.@type="type.googleapis.com/cloud.kubernetes.security.containersecurity_logging.Finding"
         jsonPayload.type="FINDING_TYPE_MISCONFIG"

  3. Click **Run query**.




To receive notifications when GKE adds new findings to Logging, set up log-based alerts for this query. For more information, see [Configure log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition).

## Clean up

  1. Delete the sample workload that you deployed.
         
         kubectl delete deployment helloweb
         

  2. Optionally, delete the cluster that you used.
         
         gcloud container clusters delete CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         




## Disable workload configuration auditing

You can disable workload configuration auditing using either the gcloud CLI or the Google Cloud console.

### gcloud

Run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        **--security-posture =disabled**

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional Standard and Autopilot clusters, or a zone for zonal Standard clusters. 



### Console

  1. Go to the **Security Posture** page in the Google Cloud console.

[Go to Security Posture](https://console.cloud.google.com/kubernetes/security/dashboard)
  2. Click the **Settings** tab.
  3. In the **Configuration audit enabled clusters** section, click **Select clusters**.
  4. In the **Audit enabled** tab, select the checkboxes for the clusters that you want to remove.
  5. Click **Disable audit** , then click **Confirm** to disable auditing on those clusters.



## Limitations of workload configuration auditing

  * Windows Server node pools aren't supported.
  * Workload configuration auditing doesn't scan GKE-managed workloads, such as workloads in the `kube-system` namespace.
  * Workload configuration auditing is only available for clusters with less than 1,000 nodes.
  * The security posture dashboard supports up to 150,000 active workload configuration auditing findings for each cluster. When the number of findings for a cluster exceeds this maximum, the security posture dashboard stops showing configuration findings for that cluster.

To resolve this issue, use the logs in Logging to identify configuration issues and deploy updated manifests. When the number of configuration findings is less than 150,000, the security posture dashboard starts displaying findings for the cluster.

  * For each cluster, the GKE security posture database tracks all of the top-level workload objects in the Kubernetes API. For example, a Deployment that manages 20 replicas is tracked as a single object. A static Pod is also a single object.

The database can process up to 5,000 object deletion and creation operations in a single transaction. For example, deleting a Deployment is a single operation, and re-creating a static Pod is two operations (deletion and creation). If the number of operations exceeds 5,000, the security posture dashboard stops showing findings for that cluster.

If your dashboard isn't updating, and you recently scaled the number of top-level workloads in your cluster, you can [create a support case with Cloud Customer Care](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case) to reset the database state.




## What's next

  * [Learn more about the security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard).
  * [Learn more about how configuration auditing works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning).
  * [Learn how to secure your clusters based on Google's recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
