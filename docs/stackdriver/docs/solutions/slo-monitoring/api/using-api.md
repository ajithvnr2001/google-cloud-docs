---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/using-api/
title: Working with the API \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:12.227316+00:00
---

# Working with the API  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/using-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Working with the API Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to manage services and service-level objectives (SLOs) by using the Cloud Monitoring API.

Service Monitoring adds the following resources to the Monitoring API:

  * [`services`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services)
  * [`services.serviceLevelObjectives`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives)



This document refers to these additions collectively as the SLO API and illustrates the primary uses. For a general overview of the structures in the SLO API, see [Constructs in the API](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures). Comprehensive reference material appears under [Cloud Monitoring API v3](https://docs.cloud.google.com/monitoring/api/ref_v3/rest).

You can use the SLO API to do the following:

  * Create and manage services.

  * Create service-level objectives (SLOs) based on custom or predefined service-level indicators (SLIs) for any of your services.




## Valid identifiers

Several methods in the SLO API use identifiers for different elements, particularly identifiers for project and services. These IDs adhere to the following rules:

  * Length: 1–63 characters
  * Characters: only lower-case letters, number, and hyphens
  * Initial character: lower-case letter
  * Terminal character: lower-case letter or a number, but not a hyphen



The regular expression for these rules is as follows: `[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?`

## Examples using `curl`

This section describes the conventions and setup used for invoking the SLO API by using the `curl` tool. If you are using this API through a client library, you can skip this section.

The examples on this page access the SLO API by using the `curl` tool to send HTTP requests to REST endpoints. Use the following information about authentication and about invoking `curl` to set the variables used in the invocations.

### Authentication

  1. Create an environment variable to hold the ID of your scoping project of a metrics scope: These examples use `PROJECT_ID`:
         
         PROJECT_ID=my-test-service
         

  2. Authenticate to the Google Cloud CLI:
         
         gcloud auth login
         

  3. To avoid having to specify your project ID with each command, set it as the default by using gcloud CLI:
         
         gcloud config set project ${PROJECT_ID}
         

  4. Create an authorization token and capture it in an environment variable. These examples call the variable `ACCESS_TOKEN`:
         
         ACCESS_TOKEN=`gcloud auth print-access-token`
         

You have to periodically refresh the access token. If commands that worked suddenly report that you are unauthenticated, re-issue this command.

  5. To verify that you got an access token, echo the `ACCESS_TOKEN` variable:
         
         echo ${ACCESS_TOKEN}
         ya29.GluiBj8o....
         




### Invoking `curl`

Each `curl` invocation includes a set of arguments, followed by the URL of a SLO API resource. The common arguments include values specified by the `PROJECT_ID` and `ACCESS_TOKEN` environment variables. You might also have to specify other arguments, for example, to specify the type of the HTTP request (for example, `-X DELETE`). The default request is `GET`, so the examples don't specify it.

Each `curl` invocation has this general structure:

`curl --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" <other_args> https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/<request>`

For example, to list all the services in your project, issue the following `GET` request:
    
    
    curl  --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/services
    

This request returns an array of service descriptions, with entries like the following, a GKE workload service with the service ID “my-test-service”:
    
    
    {
      "services": [
        {
          "name": "projects/PROJECT_NUMBER/services/my-test-service",
          "displayName": "My Test GKE Workload Service",
          "basicService": {
            "serviceType": "GKE_WORKLOAD",
            "serviceLabels": {
              "cluster_name": "workload-test",
              "location": "us-central1-c",
              "namespace_name": "kube-system",
              "project_id": "lesser-weevil",
              "top_level_controller_name": "gke-metrics-controller",
              "top_level_controller_type": "DaemonSet"
            }
          },
          "gkeWorkload": {
            "projectId": "lesser-weevil",
            "location": "us-central1-c",
            "clusterName": "workload-test",
            "namespaceName": "kube-system",
            "topLevelControllerType": "DaemonSet",
            "topLevelControllerName": "gke-metrics-controller"
          },
          "source": "USER",
          "telemetry": {
            "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/us-central1-c/clusters/workload-test/k8s/namespaces/kube-system/apps/daemonsets/gke-metrics-controller"
          }
        },
       ...
      ]
    }
    

To see the configuration used to create this service, see Creating a service. Note that the `gkeWorkload` structure in this listing is derived from the `basicService` structure used to create the service. See [`Service`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Service) for more information about the structure of a service.

## Managing services

The [`Service`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Service) resource acts as the root element for organizing your services. Aspects of a particular service, like its SLOs for example, are organized under the name of the service. The following service types are supported:

  * App Engine service: `APP_ENGINE`
  * Cloud Endpoints service: `CLOUD_ENDPOINTS`
  * Canonical Istio service: `ISTIO_CANONICAL_SERVICE`
  * Cluster Istio service: `CLUSTER_ISTIO`
  * Cloud Run service: `CLOUD_RUN`
  * A set of Google Kubernetes Engine-based services: 
    * GKE service: `GKE_SERVICE`
    * GKE namespace: `GKE_NAMESPACE`
    * GKE workload: `GKE_WORKLOAD`
  * Custom services: `CUSTOM`



For more information, see [Basic service types](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli) or [Basic GKE service types](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-wo-basic-sli).

You can add SLOs to any service in your project by using the API. Managing SLOs covers commands to manipulate SLOs.

### Service IDs

Each service has a fully qualified identifier called the _resource name_. This identifier is stored in the `name` field of the service description, for example:
    
    
    "name": "projects/PROJECT_NUMBER/services/PROJECT_ID-zone-us-central1-a-cloudrun-istio-system-cluster-local-gateway",
    

Embedded in the resource name is a shorter ID for the service, the part of the resource name after the substring `projects/PROJECT_NUMBER/services/`

If you created your own service with the resource name `projects/PROJECT_NUMBER/services/my-test-service`, the service ID is `my-test-service`.

For brevity and accuracy, many `curl` examples assume the service ID is held in the environment variable `SERVICE_ID` so you can refer to it repeatedly.

### Listing services

To retrieve information about all the services in your project, invoke the [`services.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/list) method. To retrieve information about a specific service by service ID, use the [`services.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/get) method:

For example, to list information about services by using `curl`, invoke the [`services.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/list) or [`services.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/get) method by sending a `GET` request to:

  * `https://monitoring.googleapis.com/v3/projects/[PROJECT_ID]/services` to list all services
  * `https://monitoring.googleapis.com/v3/projects/[PROJECT_ID]/services/SERVICE_ID` to get a specific service



For example, the following request retrieves information about the service identified by the value stored in the environment variable `SERVICE_ID`:
    
    
    curl  --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/services/${SERVICE_ID}
    

### Creating a service

To create a service, you specify a representation of the service type and send it to the [`services.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/create) method. You can the service-type structures described in [Basic service types](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli) and [Basic GKE service types](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-wo-basic-sli).

The structures vary, but the process for calling the API is the same. You must specify a display name for the service and a `basicService` field holding the service representation.

You can optionally specify the service ID you want the service to have. The following example shows the creation of a GKE workload service:

For example, to create the service by using `curl`, send a `POST` message to the `https://monitoring.googleapis.com/v3/projects/[PROJECT_ID]/services` endpoint:

  1. If you want to provide an ID for the service, create a variable for the service ID:
         
         SERVICE_ID=my-test-service
         

This value is supplied in the URL query parameter `service_id`.

  2. Create a variable to hold the request body that describes the service:
         
         CREATE_SERVICE_POST_BODY=$(cat <<EOF
         {
           "displayName": "My Test GKE Workload Service",
           "basicService": {
             "serviceType": "GKE_WORKLOAD",
             "serviceLabels": {
               "cluster_name": "workload-test",
               "location": "us-central1-c",
               "namespace_name": "kube-system",
               "project_id": "PROJECT_ID",
               "top_level_controller_name": "gke-metrics-controller",
               "top_level_controller_type": "DaemonSet"
             }
           }
         }
         EOF
         )
         

  3. Post the request body to the endpoint, and specify the service ID as the value of the `service_id` query parameter:
         
         curl  --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" --header "Content-Type: application/json" -X POST -d "${CREATE_SERVICE_POST_BODY}" https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/services?service_id=${SERVICE_ID}
         




For examples of the structures associated with other services, see [Basic service types](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli) or [Basic GKE service types](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-wo-basic-sli).

### Deleting a service

To delete a service you created, invoke the [`services.delete`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/delete) method and specify the service ID.

For example, to delete a service by using `curl`, send a `DELETE` request to the `https://monitoring.googleapis.com/v3/projects/[PROJECT_ID]/services/SERVICE_ID` endpoint:
    
    
    curl  --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" -X DELETE https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/services/${SERVICE_ID}
    

## Managing SLOs

You can create, delete, and retrieve SLOs by using the SLO API. You can have up to 500 SLOs for each service.

To manage SLOs for a service, you must have the service ID. SLOs are named based on the service they belong to. For information about identifying service IDs, see Service IDs.

### Listing SLOs

To retrieve information about all the SLOs associated with a service, invoke the [`services.serviceLevelObjectives.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/list) method. To retrieve information about a specific SLO by name, use the [`services.serviceLevelObjectives.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/get) method:

To list information about services by using `curl`, invoke the [`services.serviceLevelObjectives.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/list) or [`services.serviceLevelObjectives.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/get) method by sending a `GET` request to:

  * `https://monitoring.googleapis.com/v3/projects/[PROJECT_ID]/services/[SERVICE_ID]/serviceLevelObjectives` to list all SLOs
  * `https://monitoring.googleapis.com/v3/projects/[PROJECT_ID]/services/[SERVICE_ID]/serviceLevelObjectives/SLO_ID` to get a specific SLO



For example, the following request lists all SLOs associated with the service ID stored in the environment variable `SERVICE_ID`:
    
    
    curl  --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/services/${SERVICE_ID}/serviceLevelObjectives
    

The following is an availability SLO retrieved from the “currencyservice” service: 
    
    
    {
      "name": "projects/PROJECT_NUMBER/services/PROJECT_ID-zone-us-central1-c-csm-main-default-currencyservice/serviceLevelObjectives/3kavNVTtTMuzL7KcXAxqCQ",
      "displayName": "98% Availability in Calendar Week"
      "serviceLevelIndicator": {
        "basicSli": {
          "availability": {},
          "location": [
            "us-central1-c"
          ]
        }
      },
      "goal": 0.98,
      "calendarPeriod": "WEEK",
    },
    

This SLO is built on an availability SLI, it sets a target performance goal of 98 percent, and it measures compliance over a calendar week. For more information on availability SLIs, see [Service-level indicators](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring#defn-sli).

See [`ServiceLevelObjective`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#ServiceLevelObjective) for more information about the structure of SLOs.

#### Retrieving a specific SLO

Each SLO has a unique identifier within the service, consisting of the string following `serviceLevelObjectives` in the SLO's `name` field. In the following example:
    
    
    "name": "projects/PROJECT_NUMBER/services/PROJECT_ID-zone-us-central1-c-csm-main-default-currencyservice/serviceLevelObjectives/3kavNVTtTMuzL7KcXAxqCQ",
    

the SLO ID is the string `3kavNVTtTMuzL7KcXAxqCQ`.

To retrieve information about this particular SLO, request the SLO by ID.

For example, to get a specific SLO by using `curl`, invoke the [`services.serviceLevelObjectives.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/get) method by sending a `GET` request to `https://monitoring.googleapis.com/v3/projects/[PROJECT_ID]/services/SERVICE_ID/serviceLevelObjectives/SLO_ID`:
    
    
    SLO_ID=dhefHDM4TwSRZEKIV4ZYEg
    
    curl  --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/services/${SERVICE_ID}/serviceLevelObjectives/${SLO_ID}
    

### Creating an SLO

To create an SLO by using the SLO API, you must create a [`ServiceLevelObjective`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#ServiceLevelObjective) object and pass it to the [`serviceLevelObjectives.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/create) method.

The structure of an SLO has many embedded structures, including one for the value of the `serviceLevelIndicator` field.

  * For Cloud Service Mesh, Istio on Google Kubernetes Engine, and App Engine services, the SLIs are predefined. You can use the Cloud Service Mesh console to create SLOs; all you have to do is specify the performance goals and compliance periods.

  * For other services, you must define SLOs by using the SLO API. To specify an SLO, you must create a value for the `serviceLevelIndicator` field, as well. See [Creating a service-level indicator](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/identifying-custom-sli) for some techniques, and [Creating SLIs from metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/overview) for a set of examples based on various sources.




You can also create SLIs by using the Google Cloud console. For more information, see [Creating an SLO](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo).

#### Skeleton of a SLO

The basic skeleton for building the SLO is as follows:
    
    
    {
      "displayName": string,
      "serviceLevelIndicator": {
        object (ServiceLevelIndicator)
      },
      "goal": number,
    
      // Union field period can be only one of the following:
      "rollingPeriod": string,
      "calendarPeriod": enum (CalendarPeriod)
      // End of list of possible types for union field period.
    }
    

You must specify the following:

  * Display name: a description of the SLO
  * A service-level indicator, which is one of the three types: 
    * [`BasicSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#BasicSli)
    * [`RequestBasedSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#RequestBasedSli)
    * [`WindowsBasedSli`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#WindowsBasedSli)
  * The performance goal (a percentage)
  * The compliance period, which one of two types: 
    * A rolling period of some length (in seconds)
    * A calendar period



For more information about SLIs, performance goals, and compliance periods, see [Concepts in service monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring).

For Cloud Service Mesh, Istio on Google Kubernetes Engine, and App Engine services, the SLI type is the basic SLI.

For other services, you have to create a request-based SLI or a windows-based SLI. See [Creating a service-level indicator](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/identifying-custom-sli) for some techniques.

#### Example

After you have the SLI, you can build the SLO. The following example defines an SLO for a service that uses a basic SLI. You might have several SLOs on a single SLI, for example, one for 95% availability and one for 99% availability. The following example is an SLO for 95% availability over a calendar week: 
    
    
    {
      "serviceLevelIndicator": {
        "basicSli": {
          "availability": {},
          "location": [
            "us-central1-c"
          ]
        }
      },
      "goal": 0.95,
      "calendarPeriod": "WEEK",
      "displayName": "95% Availability in Calendar Week"
    }
    

This example specifies an SLO for 75% availability over a rolling 3-day period: 
    
    
    {
      "serviceLevelIndicator": {
        "basicSli": {
          "availability": {},
          "location": [
            "us-central1-c"
          ]
        }
      },
      "goal": 0.75,
      "rollingPeriod": "259200s",
      "displayName": "75% Availability in Rolling 3 Days"
    }
    

For example, to create an SLO by using `curl`, send a `POST` message to the `https://monitoring.googleapis.com/v3/projects/[PROJECT_ID]/services/SERVICE_ID/serviceLevelObjectives` endpoint:

  1. Create a variable for the service ID:
         
         SERVICE_ID=custom:my-test-service
         

  2. Create a variable to hold the request body, an instance of the `ServiceLevelObjective` object. This example uses one of the SLOs described previously:
         
         CREATE_SLO_POST_BODY=$(cat <<EOF
         {
           "serviceLevelIndicator": {
             "basicSli": {
               "availability": {},
               "location": [
                 "us-central1-c"
               ]
             }
           },
           "goal": 0.75,
           "rollingPeriod": "259200s",
           "displayName": "75% Availability in Rolling 3 Days"
         }
         EOF
         )
         

  3. Post the request body to the endpoint:
         
         curl  --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" --header "Content-Type: application/json" -X POST -d "${CREATE_SLO_POST_BODY}" https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/services/${SERVICE_ID}/serviceLevelObjectives
         

Optionally, you can also specify an ID for the SLO as the value of the `service_level_objective_id` query parameter:
         
         SLO_ID=test-slo-id
         
         curl  --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" --header "Content-Type: application/json" -X POST -d "${CREATE_SLO_POST_BODY}" https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/services/${SERVICE_ID}/serviceLevelObjectives?service_level_objective_id=${SLO_ID}
         




### Deleting an SLO

To delete an SLO, invoke the [`services.serviceLevelObjectives.delete`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/delete) method and specify the ID of the SLO in your project:

For example, to delete an SLO by using `curl`, send a `DELETE` request to the `https://monitoring.googleapis.com/v3/projects/[PROJECT_ID]/services/SERVICE_ID/serviceLevelObjectives/SLO_ID` endpoint:
    
    
    curl  --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" -X DELETE https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/services/${SERVICE_ID}/serviceLevelObjectives/${SLO_ID}
    

## Accessing SLO time series

SLO data is stored in time series, so you can use the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method to retrieve it. However, this data isn't stored in standard metric types, so you can't use the standard mechanism of specifying a metric-type filter to the `timeSeries.list` method.

Instead, SLO time series are retrieved by specifying another type of filter, a **time-series selector** , to the `timeSeries.list` method in the `filter` parameter. See [Retrieving SLO data](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/timeseries-selectors) for information on using these selectors.

You also use time-series selectors to set up alerting policies programmatically. See [Alerting on your burn rate](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
