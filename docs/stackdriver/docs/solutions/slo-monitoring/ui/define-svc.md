---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/define-svc/
title: Defining a microservice \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:42.061703+00:00
---

# Defining a microservice  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/define-svc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Defining a microservice Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create custom services and services for some resources like GKE and Cloud Run.

In Cloud Monitoring, a _service_ is a construct that you can associate with SLOs and alerting policies. Several of the resources for which you might create Monitoring services are also referred to as _services_ , but with different meanings, like [_GKE services_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) or [_Cloud Run services_](https://docs.cloud.google.com/run/docs/resource-model#services). 

Monitoring can recognize GKE- and Cloud Run-based services as _candidates_ for monitoring. To create services for them, you indicate which candidates you want to be treated as Monitoring services; Monitoring creates the necessary infrastructure for you.

You can also define arbitrary custom services.

## Identify or create a service

To identify candidate services, or to create custom services, go to the **Define service** pane:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/services-icon.png) **SLOs** page: 

[Go to **SLOs**](https://console.cloud.google.com/monitoring/services)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. On the **Services Overview** page, do one of the following:

     * Click _add_ **Define service**.

     * In the **Current status** pane, click the **Define service** link:

![Create custom and user-identified services by using **Define service**.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-msvc-define-svc.png)




From the **Define service** pane, you can do the following:

  * Create services from a list of candidate services.
  * Define custom services.



The following sections describe these options.

## Create services

Cloud Monitoring can identify potential services of the following types:

  * Cloud Service Mesh services
  * Istio on Google Kubernetes Engine services
  * App Engine services
  * GKE namespaces
  * GKE services
  * GKE workloads
  * Cloud Run service



Because there might be many of these potential services, Monitoring doesn't assume you want them all to be treated as services with SLOs. To indicate which of the potential services Monitoring should treat as services, you use either the Google Cloud console or the API.

### Use the Google Cloud console to create services

To create a service by using the Google Cloud console, do the following:

  1. On the **Services Overview** page, click **Define service**.

  2. Select **Service Candidates**.

![Potential services are listed on the **Service Candidates** tab.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-msvc-candidate-tab.png)

There might be a large number of candidate services in the list. You can filter the list as follows:

     1. Click _filter_list_ **Filter table**. A list of filter options is displayed.

     2. Select one of the options on the filter list. The selected option appears in the filter bar.

     3. Click next to the option in the filter bar and start typing. Values that match are provided on a list. Select a value from the list.

  3. Click a candidate service from the list of potential services.

When you click an entry, the following fields are filled in for you:

     * The display name is set to the name the entry in the list. You can change this value.

     * A block of JSON code for the configuration of the new service is generated from the candidate. Do not change this value.

  4. Click **Submit**. When your service is created, a **Success** notice is displayed.




### Use the API to create a service

You can also create services using the [SLO API](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services), which is part of the Cloud Monitoring API.

To create a service programmatically, post a configuration object like one of the following to the [`services.create` method](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/create):

###  GKE namespace 

Use the [`GkeNamespace`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#GkeNamespace) structure, for example:
    
    
    {
      "displayName": "test-kube-namespace",
      "gkeNamespace": {
        "location": "us-central1-c",
        "clusterName": "cluster-1",
        "namespaceName": "test-kube-namespace"
      }
    }
    

###  GKE service 

Use the [`GkeService`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#GkeService) structure, for example:
    
    
    {
      "displayName": "test-kube-service",
      "gkeService": {
        "location": "us-central1-c",
        "clusterName": "cluster-1",
        "namespaceName": "kube-system",
        "serviceName": "test-kube-service"
      }
    }
    

###  GKE workload 

Use the [`GkeWorkload`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#GkeWorkload) structure, for example:
    
    
    {
      "displayName": "frontend-a",
      "gkeWorkload": {
        "location": "us-central1-b",
        "clusterName": "cluster-2",
        "namespaceName": "default",
        "topLevelControllerType": "Deployment",
        "topLevelControllerName": "frontend-a"
      }
    }
    

###  Cloud Run 

Use the [`CloudRun`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#CloudRun) structure, for example:
    
    
    {
      "displayName": "test-cloudrun-service",
      "cloudRun": {
        "serviceName": "test-cloudrun-service",
        "location": "us-central1"
      }
    }
    

###  Cloud Service Mesh 

Use the [`MeshIstio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#MeshIstio) structure, for example:
    
    
    {
      "displayName": "test-mesh-istio-service",
      "meshIstio": {
        "meshUid": "mesh-identifier"
        "serviceName": "test-mesh-istio-service",
        "serviceNamespace": "default"
      }
    }
    

###  Istio on GKE 

Use the [`clusterIstio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#ClusterIstio) structure, for example:
    
    
    {
      "displayName": "test-cluster-istio-service",
      "clusterIstio": {
        "serviceName": "test-cloud-service",
        "clusterName": "cluster-2",
        "serviceNamespace": "default",
        "location": "us-central1"
      }
    }
    

###  App Engine 

Use the [`AppEngine`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#AppEngine) structure, for example:
    
    
    {
      "displayName": "test-mesh-istio-service",
      "appEngine": {
        ""moduleId": "id-of-the-service"
      }
    }
    

For more information about managing services programmatically, see the following documents:

  * [Constructs in the API](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures).
  * [Working with the API](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/using-api).



## Create a custom service

When no other service type meets your needs, create a custom service. With a custom service, you can arbitrarily group SLOs together in a way that is meaningful for your environment or create SLOs on business metrics that don't correspond to an existing microservice.

### Use the Google Cloud console to create a custom service

To define a custom service by using the Google Cloud console, do the following:

  1. Click **Define service** on the **Services Overview** page to bring up the **Define service** pane.

  2. Select **Custom Service**.

![Use the **Custom Service** tab to define arbitrary services.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-msvc-custom-tab.png)

  3. Enter a display name for your custom service.

  4. Click **Submit**. When your service is created, a **Success** notice is displayed.




### Use the API to create a custom service

To define a custom service by using the [SLO API](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services), post a [`Custom`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Custom) configuration object like the following to the [`services.create` method](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/create):
    
    
    {
      "displayName": "hello-world-service",
      "custom": {}
    }
    

For more information about managing services programmatically, see [Working with the API](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/using-api).

## What's next

After you identify or create a new service, you can do the following:

  * Create an SLO for your new service. You must define at least one SLO for your new service for the service to be useful. For more information, see [Creating an SLO](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo).
  * Go to the dashboard for your new service. For a new service, the dashboard is empty, but you can define SLOs from the dashboard. For more information, see [Using microservice dashboards](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-dashboard).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
