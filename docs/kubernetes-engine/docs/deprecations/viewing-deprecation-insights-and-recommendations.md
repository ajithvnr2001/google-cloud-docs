---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations/
title: Viewing deprecation insights and recommendations \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:23:25.231830+00:00
---

# Viewing deprecation insights and recommendations  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Viewing deprecation insights and recommendations Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to view _insights_ and _recommendations_ about Kubernetes deprecations for your Google Kubernetes Engine (GKE) clusters. To learn more about how to manage Kubernetes deprecations with GKE, see [Feature and API deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations).

## What are deprecation insights and recommendations?

When GKE detects that a cluster is using a Kubernetes feature or API that is deprecated and will be removed in an upcoming minor version, the following happens:

  * [Automatic upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#upgrading_automatically) to the upcoming minor version is paused. To learn more about how this works, see [What happens when GKE pauses automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#auto-upgrade-pause).
  * An insight and recommendation are generated so that you can assess and mitigate your cluster's exposure to the deprecation.



Deprecation insights and recommendations are available from [Recommender](https://docs.cloud.google.com/recommender/docs/overview), a service that provides insights and recommendations for using resources on Google Cloud. To learn more about how Recommender works with GKE, see [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).

For the deprecations topic with Recommender:

  * An _insight_ explains that your cluster uses a feature or API that is deprecated and will be removed in an upcoming minor version.
  * A _recommendation_ provides guidance on what to do to mitigate your cluster's exposure to the deprecation.



For example, an insight might explain that your cluster is using a beta API that is deprecated and will be removed in the next minor version. The recommendation explains that you should migrate your workloads from using the beta APIs to using v1 APIs. Each recommendation includes a reference to a migration guide for the deprecated feature or API. This migration guide is also available in the [corresponding table for Kubernetes deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#deprecations-information).

When GKE generates an insight and recommendation pair, it covers usage of any deprecated Kubernetes APIs or features in a particular insight subtype for one cluster in your project. For example, if any user agents call any of the APIs addressed by the `DEPRECATION_K8S_1_22_V1BETA1_API` subtype, one insight and recommendation appear to recommend that you migrate this cluster from using these APIs. If another cluster is also using these APIs, GKE generates another insight and recommendation.

### Use of deprecated Kubernetes features and APIs detected by GKE

Deprecation | Removed in GKE version | Insight subtype  
---|---|---  
[Exec probe timeouts](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/exec-probe-timeouts) | 1.35 | `EXEC_PROBE_TIMEOUT`  
[Containerd 1.7 features](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/migrate-containerd-2) | 1.33 | `DEPRECATION_CONTAINERD_V1_SCHEMA_IMAGES`,  
`DEPRECATION_CONTAINERD_V1ALPHA2_CRI_API`  
[Kubernetes 1.32 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-32) | 1.32 | `DEPRECATION_K8S_1_32_API`  
[TLS certificates signed with SHA-1 algorithm](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/sha1-1-29) | 1.29 | `DEPRECATION_K8S_SHA_1_CERTIFICATE`  
[Kubernetes 1.29 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-29) | 1.29 | `DEPRECATION_K8S_1_29_API`  
[Kubernetes 1.27 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-27) | 1.27 | `DEPRECATION_K8S_1_27_API`  
[Kubernetes 1.26 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-26) | 1.26 | `DEPRECATION_K8S_1_26_API`  
[Kubernetes 1.25 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-25) | 1.25 | `DEPRECATION_K8S_1_25_API`  
[PodSecurityPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/podsecuritypolicy) | 1.25 | `DEPRECATION_K8S_1_25_PODSECURITYPOLICY`  
[Docker-based node images](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/docker-containerd) | 1.24 | `DEPRECATION_K8S_1_24_DOCKERSHIM`  
[X.509 Common Name field in webhook certificates](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/webhookcompatibility) | 1.23 | `DEPRECATION_K8S_1_23_CERTIFICATE`  
[Kubernetes 1.22 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-22),   
[Kubernetes Ingress Beta APIs removed in GKE 1.23](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-23) | 1.22, 1.23 | `DEPRECATION_K8S_1_22_V1BETA1_API`  
  
Remember that for [upcoming deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#deprecations-information), you must independently assess your cluster environment's exposure and mitigate any issues.

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




#### Example: Insight

A deprecation insight includes details about the timing and amount of usage of a deprecated feature or API. The information included in the insight depends on for what type of deprecation the insight is providing information.

This is an example insight for the `DEPRECATION_K8S_1_22_V1BETA1_API` insight subtype:
    
    
      name: projects/<PROJECT-NUMBER>/locations/us-central1/insightTypes/google.container.DiagnosisInsight/insights/<INSIGHT-ID>
      observationPeriod: 2592000s
      severity: HIGH
      category: RELIABILITY
      stateInfo:
        state: ACTIVE
      insightSubtype: DEPRECATION_K8S_1_22_V1BETA1_API
      description: Your API clients have used deprecated APIs in the last 30 days that are removed in Kubernetes v1.22. Upgrading your cluster before migrating to the updated APIs supported by v1.22 could cause it to break. [Learn more](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-22).
      targetResources:
        - //container.googleapis.com/projects/<PROJECT-NUMBER>/locations/us-central1/clusters/c1
      associatedRecommendations:
        - recommendation: projects/<PROJECT-NUMBER>/locations/us-central1/recommenders/google.container.DiagnosisRecommender/recommendations/<RECOMMENDATION-ID>
      etag: '"2147dd8e1e302ed7"'
      lastRefreshTime: "2022-01-30T08:00:00Z"
      content:
      targetClusters:
        - clusterId: <CLUSTER-ID>
          clusterUri: //container.googleapis.com/projects/<PROJECT-NUMBER>/locations/us-central1/clusters/c1
      apiDeprecationInsight:
        - api: /apis/networking.k8s.io/v1beta1/Ingress
          stopServingVersion: 1.22
          deprecatedClientStats:
            userAgent: kubectl
            numberOfRequestsLast30Days: 288
            lastRequestTime: "2022-03-02T08:00:18Z"
        - api: /apis/rbac.authorization.k8s.io/v1beta1/ClusterRole
          stopServingVersion: 1.22
          deprecatedClientStats:
            userAgent: kubectl
            numberOfRequestsLast30Days: 126
            lastRequestTime: "2022-02-01T06:45:25Z"
    

#### Example: Recommendation

A deprecation recommendation includes a description of the deprecation with a link to the migration guide for the deprecation. You can also find these migration guides in the [GKE feature deprecations table](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#feature_deprecations) and [Kubernetes API deprecations table](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#kubernetes_api_deprecations).

This is an example recommendation for the `DEPRECATION_K8S_1_22_V1BETA1_API` recommendation subtype:
    
    
      name: projects/<PROJECT-NUMBER>/locations/us-central1/recommenders/google.container.DiagnosisRecommender/recommendations/<RECOMMENDATION-ID>
      description: Update manifests and API clients to use v1 API before upgrading to Kubernetes 1.22 by following the [instructions](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-22).
      primaryImpact:
        category: RELIABILITY
        reliabilityProjection:
          risks:
          - SERVICE_DISRUPTION
      priority: P2
      recommenderSubtype: DEPRECATION_K8S_1_22_V1BETA1_API
      stateInfo:
        state: ACTIVE
      targetResources:
        - //container.googleapis.com/projects/<PROJECT-NUMBER>/locations/us-central1/clusters/c1
      associatedInsights:
        - insight: projects/<PROJECT-NUMBER>/locations/us-central1/insightTypes/google.container.DiagnosisInsight/insights/<INSIGHT-ID>
      etag: '"4dc0f7b33594072f"'
      lastRefreshTime: "2022-01-30T08:00:00Z"
      content:
        overview:
          targetClusters:
            - clusterId: <CLUSTER-ID>
              clusterUri: //container.googleapis.com/projects/<PROJECT-NUMBER>/locations/us-central1/clusters/c1
          apiDeprecationRecommendation:
            - api: /apis/networking.k8s.io/v1beta1/Ingress
              apiReplacement: /apis/networking.k8s.io/v1/Ingress
              stopServingVersion: 1.22
            - api: /apis/rbac.authorization.k8s.io/v1beta1/ClusterRole
              apiReplacement: /apis/rbac.authorization.k8s.io/v1/ClusterRole
              stopServingVersion: 1.22
    

## Export insights and recommendations to BigQuery

You can use BigQuery to export and analyze insights and recommendations for your entire organization. To learn more, see [Export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

## Dismiss or restore deprecation recommendations

If you don't want to see a deprecation recommendation for a cluster in the Google Cloud console anymore, dismiss it. You might do this, for example, to dismiss recommendations that apply to temporary, short-lived clusters.

If you dismiss the recommendation, it doesn't appear for any user viewing the cluster in the console. After you dismiss the recommendation, it doesn't appear again even if a user agent calls the deprecated API or feature in this subtype after dismissal.

However, the recommendation remains discoverable with the Google Cloud CLI and the Recommender API.

When you dismiss a recommendation, you only hide it for all users. Automatic upgrades [remain paused](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#auto-upgrade-pause) until you migrate from the deprecated feature or API and GKE does not detect usage of the deprecated APIs for 30 consecutive days, or until the cluster's version reaches [end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle). To learn more, see [When does GKE resume automatic upgrades?](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#auto-upgrades-resume).

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

  * To learn more about how deprecations work with GKE, see [Feature and API deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations).
  * To learn more about the Recommender API, see [Using the API - Recommendations](https://docs.cloud.google.com/recommender/docs/using-api).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
