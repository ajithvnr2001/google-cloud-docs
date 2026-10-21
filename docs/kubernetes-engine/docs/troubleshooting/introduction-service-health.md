---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-service-health/
title: Review service health and incidents \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:28:03.246211+00:00
---

# Review service health and incidents  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-service-health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Review service health and incidents Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When your Google Kubernetes Engine (GKE) clusters or applications experience issues, it's crucial to quickly determine if the cause is internal or related to a wider Google Cloud service disruption. Spending time on local debugging is inefficient if the root cause is a known platform incident.

Use this page to determine if an issue with your GKE cluster is caused by a wider Google Cloud service disruption. Learn where to find official status updates, personalized health events, and service incident insights from the following sources:

  * **Google Cloud Service Health** : status information for Google Cloud services, by region.
  * **Personalized Service Health** : service disruptions relevant to your projects.
  * **Service incident insights and recommendations** : GKE clusters that are affected by an ongoing service incident.



This information is important for Platform admins and operators and Application developers who are troubleshooting and need to understand if observed issues are linked to a broader Google Cloud service health event. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Review Google Cloud service health

The [Google Cloud Service Health](https://status.cloud.google.com/) page provides status information about the services that are part of Google Cloud.

To review incidents related to GKE, go to the **Google Cloud Service Health** page.

[Go to all incidents reported for Google Kubernetes Engine](https://status.cloud.google.com/products/LCSbT57h59oR4W98NHuz/history)

## Review Personalized Service Health

[Personalized Service Health](https://docs.cloud.google.com/service-health/docs/overview) lets you identify Google Cloud service disruptions that are relevant to _your projects_. These disruptions are called _service health events_ , and information about them is available in the Google Cloud console and a [variety of integration points](https://docs.cloud.google.com/service-health/docs/how-to-integrate).

To review incidents related to GKE that are relevant to your projects, view service health events in the Personalized Service Health dashboard in the Google Cloud console.

[Go to Personalized Service Health](https://console.cloud.google.com/servicehealth)

You can filter incidents by service, location, relevance, and status. The dashboard also provides incident details such as scope of impact, symptoms, workarounds, and resolution progress updates. To get started, see [Quickstart: View service health events in the Google Cloud console](https://docs.cloud.google.com/service-health/docs/view-events).

## Review service incident insights and recommendations

Service incident insights and recommendations let you identify GKE clusters that are impacted by an ongoing service incident.

To get service incident insights, view insights and recommendations for the `GKE_RELIABILITY_INCIDENT` subtype. You can get insights by using the Google Cloud console, the Google Cloud CLI, or the Recommender API. For more information, see [View insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs).

Insights and recommendations include the following information:

  * **Impacted cluster** : a cluster that's impacted by the incident.
  * **Incident name** : an incident identifier for reference when you communicate with Cloud Customer Care.
  * **Incident description** : information about the incident from the incident response team.
  * **Last effective time** : the last time that information about the incident was updated.
  * **Mitigation action** : mitigation action that's recommended by the incident response team, if available.



The service incident insight remains visible until the Google Cloud incident response team mitigates the incident and determines that the insight is no longer relevant. There will be a delay between the time the incident is mitigated and no longer impacts your resources, and the time the insight is removed. If you implemented a workaround and no longer want to see the insight, you can dismiss it.

## What's next

  * Read [Assess cluster and workload health in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-console) (the next page in this series).

  * For advice about resolving specific problems, review [GKE's troubleshooting guides](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
