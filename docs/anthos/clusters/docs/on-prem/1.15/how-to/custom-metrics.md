---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/custom-metrics/
title: Enabling user-defined custom metrics for Horizontal Pod autoscaling \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:01.713170+00:00
---

# Enabling user-defined custom metrics for Horizontal Pod autoscaling  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/custom-metrics/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Enabling user-defined custom metrics for Horizontal Pod autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/custom-metrics)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/custom-metrics)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This topic describes how to configure user-defined metrics for Horizontal Pod autoscaling (HPA) in Google Distributed Cloud.

## Enabling Logging and Monitoring for user applications

The configuration for Logging and Monitoring is held in a Stackdriver object named `stackdriver`.

  1. Open the `stackdriver` object for editing:
         
         kubectl --kubeconfig=USER_CLUSTER_KUBECONFIG --namespace kube-system edit stackdriver stackdriver
         

Replace USER_CLUSTER_KUBECONFIG with the path of your user cluster kubeconfig file.

  2. Under `spec`, set both `enableStackdriverForApplications` and `enableCustomMetricsAdapter` to `true`:
         
         apiVersion: addons.gke.io/v1alpha1
         kind: Stackdriver
         metadata:
         name: stackdriver
         namespace: kube-system
         spec:
         projectID: project-id
         clusterName: cluster-name
         clusterLocation: cluster-location
         proxyConfigSecretName: secret-name
         enableStackdriverForApplications: true
         enableCustomMetricsAdapter: true
         scalableMonitoring: true
         enableVPC: stackdriver-enable-VPC
         optimizedMetrics: true
         

  3. Save and close the edited file.




Once these steps are done, all the user application logs are sent to Cloud Logging.

The next step is to annotate the user application for metrics collection.

## Annotate a user application for metrics collection

To annotate a user application to be scraped and the logs sent to Cloud Monitoring, you must add corresponding `annotations` to the metadata for the service, Pod, and endpoints.
    
    
      metadata:
        name: "example-monitoring"
        namespace: "default"
        annotations:
          prometheus.io/scrape: "true"
          prometheus.io/path: "" - Overriding metrics path (default "/metrics")
      

## Deploy an example user application

In this section, you deploy a sample application with both logs and prometheus-compatible metrics.

  1. Save the following Service and Deployment manifests to a file named `my-app.yaml`. Notice that the Service has the annotation `prometheus.io/scrape: "true"`:


    
    
      kind: Service
      apiVersion: v1
      metadata:
        name: "example-monitoring"
        namespace: "default"
        annotations:
          prometheus.io/scrape: "true"
      spec:
        selector:
          app: "example-monitoring"
        ports:
          - name: http
            port: 9090
      ---
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: "example-monitoring"
        namespace: "default"
        labels:
          app: "example-monitoring"
      spec:
        replicas: 1
        selector: 
          matchLabels:
            app: "example-monitoring"
        template: 
          metadata: 
            labels:
              app: "example-monitoring"
          spec:
            containers:
            - image: gcr.io/google-samples/prometheus-example-exporter:latest
              name: prometheus-example-exporter
              imagePullPolicy: Always
              command:
              - /bin/sh
              - -c
              - ./prometheus-example-exporter --metric-name=example_monitoring_up --metric-value=1 --port=9090
              resources:
                requests:
                  cpu: 100m
    

  1. Create the Deployment and the Service:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG apply -f my-app.yaml
         




## Use the custom metrics in HPA

Deploy the HPA object to use the metric exposed in the previous step. See [Autoscaling on multiple metrics and custom metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-multiple-metrics-and-custom-metrics) for more advanced information about different type of custom metrics.
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: example-monitoring-hpa
      namespace: default
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: example-monitoring
      minReplicas: 1
      maxReplicas: 5
      metrics:
      - type: Pods
        pods:
          metric:
            name: example_monitoring_up
          target:
            type: AverageValue
            averageValue: 20
    

The Pods type metric has a default metric selector for the labels of the target Pods, which is how kube-controller-maneger works. In this example, you cna query the example_monitoring_up metric with a selector of `{matchLabels: {app: example-monitoring}}` as they are available in the target Pods. Any other selector specified is added to the list. To avoid the default selector, you canremove any labels on the target Pod or use the Object type metric.

## Check that the user-defined application metrics are used by HPA

Check that the user defined application metrics are used by HPA:
    
    
    kubectl --kubeconfig=USER_CLUSTER_KUBECONFIG describe hpa example-monitoring-hpa

The output will look like this:
    
    
    Name:                             example-monitoring-hpa
    Namespace:                        default
    Labels:                           
    Annotations:                      CreationTimestamp:  Mon, 19 Jul 2021 16:00:40 -0800
    Reference:                        Deployment/example-monitoring
    Metrics:                          ( current / target )
      "example_monitoring_up" on pods:  1 / 20
    Min replicas:                     1
    Max replicas:                     5
    Deployment pods:                  1 current / 1 desired
    Conditions:
      Type            Status  Reason              Message

* * *

AbleToScale True ReadyForNewScale recommended size matches current size ScalingActive True ValidMetricFound the HPA was able to successfully calculate a replica count from pods metric example_monitoring_up ScalingLimited False DesiredWithinRange the desired count is within the acceptable range 

## Costs

Using custom metrics for HPA does not incur any additional charges. Users are charged only for application metrics and logs. See [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing) for details. The Pod for enabling custom metrics consumes an extra 15m CPU and 20MB memory.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
