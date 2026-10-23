---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders/
title: Optimize your usage of GKE with insights and recommendations \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:14.557342+00:00
---

# Optimize your usage of GKE with insights and recommendations  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Optimize your usage of GKE with insights and recommendations Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

With Google Kubernetes Engine (GKE), you can receive prescriptive guidance for how to optimize your clusters.

GKE monitors your clusters and if there are potential optimizations, guidance is delivered through [Recommender](https://docs.cloud.google.com/recommender/docs/overview), a Google Cloud service that generates insights and recommendations for using resources on Google Cloud. For GKE, Recommenders deliver two types of information:

  * An _insight_ explains that GKE detected your cluster usage can be optimized in some way.
  * A _recommendation_ explains how to optimize your cluster usage.



GKE delivers this information in the Google Cloud console and you can also find it with the Google Cloud CLI and the Recommender API. GKE provides Recommenders for topics including:

  * **[Deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations):** Mitigate exposure to deprecated Kubernetes features or APIs.
  * **[Operations and connectivity](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types#gke-insight):** Fix issues related to control plane and node connectivity, and IP address utilization.
  * **[Cost optimization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations)** : Implement cost-optimized configurations and practices. For example, identify [idle GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/idle-clusters), [overprovisioned GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-cluster-utilization), and [overprovisioned workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-workload-resource-utilization).
  * **Scalability** : Implement reliability improvement practices, such as scaling up [underprovisioned GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-cluster-utilization) and [underprovisioned workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-workload-resource-utilization).
  * **[Resource requests and limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#identify-workloads)** : Set resource requests and limits to avoid abrupt Pod termination under node [resource pressure](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) and improve accuracy of cost allocation.
  * **[Agones](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-agones-controller-gke):** Isolate the Agones controller in your cluster.
  * **[Disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-disruption-readiness)** : Ensure workloads' continuity and recoverability during maintenance.
  * **[Webhooks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-webhooks):** Ensure control plane stability when using webhooks.
  * **[Data protection](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/data-protection-recommendations):** Ensure workloads are protected from disruptive events.
  * **[Cluster credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#gke-notification-for-expiring):** Rotate cluster credentials to prevent disruption.
  * **[Release channels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#identify-recommend):** Enroll clusters in a release channel.
  * **[Maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#recommender-maintenance-window):** Choose a recurring window of time in which GKE cluster maintenance occurs.
  * **[Supported versions](https://docs.cloud.google.com/kubernetes-engine/versioning):** Ensure that clusters run a supported version that also adheres to the GKE version skew policy. For details, see the _Automatic upgrades at the end of support_ and _GKE version skew policy_ sections in the referenced page.
  * **[Node service account permissions](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/logging#identify-fix-permissions-in-all-clusters):** Ensure that node service accounts have the critical permissions that are required for normal GKE operations.
  * **[CRDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/crd-with-invalid-caBundle)** : Ensure stable cluster operations by fixing misconfigured CRDs with an invalid CA bundle.
  * **[etcd usage](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/scalability#identify-fix-etcd-usage):** Ensure that the etcd database has sufficient storage to prevent cluster instability.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Required roles

Ensure that you have the necessary permissions for Kubernetes insights and recommendations, either with the following [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) or [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions):

  * View insights and recommendations with one of the following roles:

    * [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic)
    * [GKE Diagnosis Recommender Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.containerDiagnosisViewer)
  * View and update the state of insights and recommendations (for example, dismiss a recommendation):

    * [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic)
    * [Kubernetes Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin)
    * [Kubernetes Engine Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer)
    * [GKE Diagnosis Recommender Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.containerDiagnosisAdmin)



## View insights and recommendations

You can view insights and recommendations with the Google Cloud CLI, in the Google Cloud console, or with the [Recommender API](https://docs.cloud.google.com/recommender/docs/reference/rest).

### Console

When you view recommendations in the console, you have two options. You can use the high-level scorecard at the top of the view to see aggregate results for health, upgrade, and cost optimization recommendations across all clusters in your project.

Or, you can view a list of per-cluster recommendations.

To view recommendations using the scorecard, do these steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console:

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. To view the number of clusters impacted by individual recommendations, click **View recommendations** under the category you want to view - either Health, Upgrade, or Cost. In the revealed sidebar panel, a list of recommendations indicates how many clusters are impacted by each recommendation.

  3. To view more information, including the names of the impacted clusters, click the recommendation name.

  4. To view more details for each impacted cluster, click the recommendation again.




To view per-cluster recommendations, do these steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console:

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Check the **Notifications** column for specific clusters to find insights and recommendations.

  3. To reveal more information, click on the insight. In the revealed sidebar panel, you can see details about this insight, including any associated recommendation.




### gcloud

An insight typically has a corresponding recommendation. Insights are fetched with [`gcloud recommender insights`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights) and recommendations are fetched with [`gcloud recommender recommendations`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations).

  1. View the list of insights for the clusters of a specific zone (for zonal clusters) or a specific region (for regional clusters):
         
         gcloud recommender insights list \
             --insight-type=google.container.DiagnosisInsight \
             --location=LOCATION \
             --project=PROJECT_ID \
             --format=FORMAT \
             --filter="insightSubtype:SUBTYPE"
         

Replace the following:

     * `PROJECT_ID`: the Google Cloud project ID for the project where the cluster(s) are located.
     * `LOCATION`: the exact region or zone of the cluster. For [zonal clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#zonal_clusters), you must provide the exact zone (e.g. `us-central1-c`). For [regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#regional_clusters), you must provide the exact region (e.g. `us-central1`).
     * `FORMAT`: change the output format to YAML. This flag is optional.
     * `SUBTYPE`: an [insight subtype](https://docs.cloud.google.com/recommender/docs/insights/using-insights#insight_subtype), for example, `DEPRECATION_K8S_1_23_CERTIFICATE`. This limits the output to insights of a specified subtype. This flag is optional.

Or, if you already have an insight ID, you can see details about the insight by running the following command:
    
    gcloud recommender insights describe INSIGHT \
        --insight-type=google.container.DiagnosisInsight \
        --location=LOCATION \
        --project=PROJECT_ID \
        --format=FORMAT
    

Replace the `INSIGHT` with the value of insight ID, specified at the end of the URL from the `name` field for the insight.

**Note:** To view the associated recommendation, save the **recommendation ID** value of the `associatedRecommendations.recommendation` from the command output for Step 2.

The output includes additional details about what behavior GKE has detected with your cluster.

  2. View the list of recommendations for the clusters of a specific zone (for zonal clusters) or a specific region (for regional clusters):

**Note:** Use the `describe` command instead if you already have a **recommendation ID** from Step 1 and want to see a specific recommendation.
         
         gcloud recommender recommendations list \
             --recommender=google.container.DiagnosisRecommender \
             --location=LOCATION \
             --project=PROJECT_ID \
             --format=FORMAT \
             --filter="recommenderSubtype:SUBTYPE"
         

Replace `SUBTYPE` with a [recommender subtype](https://docs.cloud.google.com/recommender/docs/key-concepts#recommender_subtype), for example, `DEPRECATION_K8S_1_23_CERTIFICATE`. This limits the output to recommendations of a specified subtype. This flag is optional.

Or, if you already have a recommendation ID, you can view the recommendation by running the following command:
         
         gcloud recommender recommendations describe RECOMMENDATION_ID \
             --recommender=google.container.DiagnosisRecommender \
             --location=LOCATION \
             --project=PROJECT_ID \
             --format=FORMAT
         

Replace the `RECOMMENDATION_ID` with the saved value of `associatedRecommendations.recommendation` from the command output in Step 1.

The output provides guidance on what action you might need to take to optimize your cluster's usage of GKE.




### API

Each insight has a corresponding recommendation. Insights are fetched with [REST Resource: projects.locations.insightTypes.insights](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights) and recommendations are fetched with [REST Resource: projects.locations.recommenders.recommendations](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations).

  1. View the list of insights for the clusters of a specific zone (for zonal clusters) or a specific region (for regional clusters):
         
         GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.container.DiagnosisInsight/insights?filter=insightSubtype%20%3D%20SUBTYPE
         

Replace the following:

     * `PROJECT_ID`: the Google Cloud project ID for the project where the cluster(s) are located.
     * `LOCATION`: the exact region or zone of the cluster. For [zonal clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#zonal_clusters), you must provide the exact zone (e.g. `us-central1-c`). For [regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#regional_clusters), you must provide the exact region (e.g. `us-central1`).
     * `SUBTYPE`: an [insight subtype](https://docs.cloud.google.com/recommender/docs/insights/using-insights#insight_subtype), for example, `DEPRECATION_K8S_1_23_CERTIFICATE`. This limits the output to insights of a specified subtype. This flag is optional.

Or, if you already have an insight ID, you can see details about the insight by making the following request:
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.container.DiagnosisInsight/insights/INSIGHT
    

Replace the `INSIGHT` with the value of insight ID, specified at the end of the URL from the `name` field for the insight.

**Note:** To view the associated recommendation, save the **recommendation ID** value of the `associatedRecommendations.recommendation` from the response body for Step 2.

The response body includes details about what behavior GKE has detected with your cluster.

  2. View the list of recommendations for the clusters of a specific zone (for zonal clusters) or a specific region (for regional clusters):

**Note:** Use the `recommendations.get` request instead if you already have a **recommendation ID** from Step 1 and want to see a specific recommendation.
         
         GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.container.DiagnosisRecommender/recommendations?filter=recommenderSubtype%20%3D%20SUBTYPE
         

Replace `SUBTYPE`with a [recommender subtype](https://docs.cloud.google.com/recommender/docs/key-concepts#recommender_subtype), for example, `DEPRECATION_K8S_1_23_CERTIFICATE`. This limits the output to recommendations of a specified subtype. This flag is optional.

Or, if you already have a recommendation ID, you can view the recommendation by making the following request:
         
         GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.container.DiagnosisRecommender/recommendations/RECOMMENDATION_ID
         

Replace the `RECOMMENDATION_ID` with the saved value of `associatedRecommendations.recommendation` from the response body in Step 1.

The response body provides guidance on what action you might need to take to optimize your cluster's usage of GKE.




## Export insights and recommendations to BigQuery

You can use BigQuery to export and analyze insights and recommendations for your entire organization. To learn more, see [Export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

## Dismiss or restore recommendations

If you don't want to see a recommendation for a cluster in the Google Cloud console anymore, dismiss it. You might do this, for example, if you have assessed the recommendation and you have decided not to implement it.

If you dismiss the recommendation, it doesn't appear for any user viewing the cluster in the console. After you dismiss the recommendation, it doesn't appear again even if GKE detects the same behavior.

When you dismiss a recommendation, you only hide it for all users in the console. The recommendation remains discoverable with the Google Cloud CLI and the Recommender API.

### Dismiss a recommendation

To dismiss the recommendation, follow the instructions for Viewing insights and recommendations in the Google Cloud console to open the sidebar panel, which has more details. In that panel, click the **Dismiss** button.

### Dismiss recommendations using the Google Cloud CLI

To dismiss a recommendation using the gcloud CLI, you must locate the active recommendation's "`etag` value" and then mark it as dismissed.

  1. List active recommendations: To find the recommendation you want to dismiss, list the active recommendations for your cluster. To exclude recommendations that are already dismissed, or have succeeded or failed, use the `--filter` flag:
         
         gcloud recommender recommendations list \
             --recommender=RECOMMENDER_ID \
             --project=PROJECT_ID \
             --location=LOCATION \
             --filter="stateInfo.state=ACTIVE"
         

Replace the following:

     * `RECOMMENDER_ID`: the ID of the recommender.
     * `PROJECT_ID`: the Google Cloud project ID for the project where the clusters are located.
     * `LOCATION`: the exact region or zone of the cluster. For zonal clusters, you must provide the exact zone (such as `us-central1-c`). For regional clusters, you must provide the exact region (such as `us-central1`).
  2. Fetch the etag: Find the `RECOMMENDATION_ID` from the previous output and describe it to retrieve its current state and `etag`:
         
         gcloud recommender recommendations describe RECOMMENDATION_ID \
             --recommender=RECOMMENDER_ID \
             --project=PROJECT_ID \
             --location=LOCATION
         

Replace the following:

     * `RECOMMENDATION_ID`: the ID of the recommendation you want to dismiss.

Note the `etag` value in the output (for example, `"a770e444b0088a35"`).

  3. Mark as dismissed: Run the `mark-dismissed` command. The Recommender API requires the exact `etag` to prevent race conditions.

**Note:** The API returns the `etag` wrapped in literal double quotes. In most shells, you must pass these double quotes by wrapping them in single quotes (`'"..."'`) to prevent the shell from stripping them out:
         
         gcloud recommender recommendations mark-dismissed RECOMMENDATION_ID \
             --recommender=RECOMMENDER_ID \
             --project=PROJECT_ID \
             --location=LOCATION \
             --etag='"ETAG_VALUE"'
         

Replace the following:

     * `ETAG_VALUE`: the `etag` value returned from the describe command.



### Restore a dismissed recommendation

You can restore a dismissed recommendation by following the instructions for [Restoring a recommendation](https://docs.cloud.google.com/recommender/docs/recommendation-hub/changing-applying-recommendations#restoring_a_recommendation).

## What's next

  * Learn more about [Recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
