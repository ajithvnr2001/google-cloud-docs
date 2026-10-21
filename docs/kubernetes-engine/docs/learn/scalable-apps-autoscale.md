---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-autoscale/
title: Learning Path: Scalable applications - Scaling \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:50.463541+00:00
---

# Learning Path: Scalable applications - Scaling  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-autoscale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Learning Path: Scalable applications - Scaling Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This set of tutorials is for IT administrators and Operators that want to deploy, run, and manage modern application environments that run on Google Kubernetes Engine (GKE). As you progress through this set of tutorials you learn how to configure monitoring and alerts, scale workloads, and simulate failure, all using the Cymbal Bank sample microservices application:

  1. [Create a cluster and deploy a sample application](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment)
  2. [Monitor with Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-monitor)
  3. Scale workloads (this tutorial)
  4. [Simulate a failure](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-failure)
  5. [Centralize change management](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-centralize)



## Overview and objectives

A consumer application like Cymbal Bank often has varying numbers of users at different times. Ideally your website is able to cope with surges in traffic without slowing down or having other issues, but without the organization having to spend money on Cloud resources that they don't actually need. A solution that Google Cloud provides for this is autoscaling.

In this tutorial, you learn how to configure clusters and workloads in a GKE cluster to scale using both built-in Kubernetes metrics and custom metrics from Cloud Monitoring and Cloud Trace. You learn how to complete the following tasks:

  * Enable custom metrics in Cloud Monitoring for Trace. 
    * Custom metrics let you scale using additional monitoring data or external inputs beyond the awareness of the Kubernetes cluster, like network traffic or HTTP response codes.
  * Configure the Horizontal Pod Autoscaler, a GKE feature that can automatically increase or decrease the number of Pods for a workload depending on specified metrics.
  * Simulate application load and view the cluster autoscaler and Horizontal Pod Autoscaler respond.



## Costs

Enabling GKE and deploying the Cymbal Bank sample application for this series of tutorials means that you incur per-cluster charges for GKE on Google Cloud as listed on our [Pricing page](https://cloud.google.com/kubernetes-engine/pricing) until you disable GKE or delete the project.

You are also responsible for other Google Cloud costs incurred while running the Cymbal Bank sample application, such as charges for Compute Engine VMs and Trace.

## Before you begin

To learn how to scale your deployments, you must complete the [first tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment) to create a GKE cluster that uses Autopilot and deploy the Cymbal Bank sample microservices-based application.

We recommend that you complete this set of tutorials for scalable apps in order. As you progress through the set of tutorials, you learn new skills and use additional Google Cloud products and services.

You also need to grant IAM permissions so that your workloads and the Horizontal Pod Autoscaler can write traces and read custom metrics:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --role=roles/cloudtrace.agent \
      --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/default/sa/default" \
      --condition=None
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --role=roles/monitoring.metricWriter \
      --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/default/sa/default" \
      --condition=None
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `PROJECT_NUMBER`: your Google Cloud project number.



The following access is granted to Pods that use the `default` Kubernetes ServiceAccount in the `default` namespace:

  * `roles/cloudtrace.agent`: Write trace data such as latency information to Trace.
  * `roles/monitoring.metricWriter`: Write metrics to Cloud Monitoring.



## Set up custom metrics collection

You can configure the Horizontal Pod Autoscaler to use basic built-in Kubernetes CPU and memory metrics, or you can use custom metrics from Cloud Monitoring like HTTP requests per second or the quantity of `SELECT` statements. Custom metrics can work without application changes, and give your cluster more insight into the overall performance and needs of the application. In this tutorial, you learn how to use both the built-in and custom metrics.

  1. To allow Horizontal Pod Autoscaler to read custom metrics from Monitoring, you must install the [Custom Metrics - Stackdriver Adapter](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/custom-metrics-stackdriver-adapter) adapter in your cluster.

Deploy the custom metrics Stackdriver adapter to your cluster:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/deploy/production/adapter.yaml
         

  2. To allow the Stackdriver adapter to get custom metrics from your cluster, grant the `custom-metrics-stackdriver-adapter` Kubernetes ServiceAccount the `roles/monitoring.viewer` role by using Workload Identity Federation for GKE:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/custom-metrics/sa/custom-metrics-stackdriver-adapter" \
             --role=roles/monitoring.viewer \
             --condition=None
         


**Objective:** Congratulations! You now have a Stackdriver adapter in your GKE cluster that's configured to read custom metrics from Monitoring.

## Configure the Horizontal Pod Autoscaler

GKE Autopilot can scale in a few different ways. In this tutorial, you see how your cluster can scale using the following methods:

  * Horizontal Pod Autoscaler: scales the number of Pods for a workload.
  * Cluster autoscaler: scales the node resources that are available in the cluster.



These two methods can work together so that as the number of Pods for your applications changes, the node resources to support those Pods also changes.

Other implementations are available to scale Pods that build on top of the Horizontal Pod Autoscaler, and you can also use the Vertical Pod Autoscaler to adjust a Pod's CPU and memory requests instead of the number of Pods.

In this tutorial, you configure the Horizontal Pod Autoscaler for the `userservice` Deployment using built-in metrics, and for the `frontend` Deployment using custom metrics.

For your own applications, work with your Application developers and Platform engineers to understand their needs and configure the Horizontal Pod Autoscaler rules.

### Scale the `userservice` Deployment

When the number of users of the Cymbal Bank sample application increases, the `userservice` Service consumes more CPU resources. You use a `HorizontalPodAutoscaler` object to control how you want your application to respond to load. In the YAML manifest for the `HorizontalPodAutoscaler`, you define what Deployment to for the Horizontal Pod Autoscaler to scale, what metrics to monitor, and the minimum and maximum number of replicas you want to run.

  1. Review the `HorizontalPodAutoscaler` sample manifest for the `userservice` Deployment:
         
         # Copyright 2022 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         ---
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: userservice
         spec:
           behavior:
             scaleUp:
               stabilizationWindowSeconds: 0
               policies:
                 - type: Percent
                   value: 100
                   periodSeconds: 5
               selectPolicy: Max
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: userservice
           minReplicas: 5
           maxReplicas: 50
           metrics:
             - type: Resource
               resource:
                 name: cpu
                 target:
                   type: Utilization
                   averageUtilization: 60
         

This manifest does the following:

     * Sets the maximum number of replicas during a scale-up to `50`.
     * Sets the minimum number of during a scale-down to `5`.
     * Uses a built-in Kubernetes metric to make scaling decisions. In this sample, the metric is CPU utilization, and the target utilization is 60%, which avoids both over- and under-utilization.
  2. Apply the manifest to the cluster:
         
         kubectl apply -f extras/postgres-hpa/hpa/userservice.yaml
         




### Scale the `frontend` Deployment

In the previous section, you configured the Horizontal Pod Autoscaler on the `userservice` Deployment based on built-in Kubernetes metrics for CPU utilization. For the `frontend` Deployment, you might want to instead scale based on the number of incoming HTTP requests. This approach uses the Stackdriver adapter to read custom metrics from Monitoring for the HTTP(S) Load Balancer Ingress object.

  1. Review the `HorizontalPodAutoscaler` manifest for the `frontend` Deployment:
         
         # Copyright 2022 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         ---
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: frontend
         spec:
           behavior:
             scaleUp:
               stabilizationWindowSeconds: 0
               policies:
                 - type: Percent
                   value: 100
                   periodSeconds: 5
               selectPolicy: Max
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: frontend
           minReplicas: 5
           maxReplicas: 25
           metrics:
             - type: External
               external:
                 metric:
                   name: loadbalancing.googleapis.com|https|request_count
                   selector:
                     matchLabels:
                       resource.labels.forwarding_rule_name: FORWARDING_RULE_NAME
                 target:
                   type: AverageValue
                   averageValue: "5"
         

This manifest uses the following fields:

     * `spec.scaleTargetRef`: The Kubernetes resource to scale.
     * `spec.minReplicas`: The minimum number of replicas, which is `5` in this sample.
     * `spec.maxReplicas`: The maximum number of replicas, which is `25` in this sample.
     * `spec.metrics.*`: The metric to use. In this sample, this is the number of HTTP requests per second, which is a custom metric from Monitoring provided by the adapter that you deployed.
     * `spec.metrics.external.metric.selector.matchLabels`: The specific resource label to filter when scaling.
  2. Find the name of the forwarding rule from the `frontend` Ingress load balancer:
         
         export FW_RULE=$(kubectl get ingress frontend -o=jsonpath='{.metadata.annotations.ingress\.kubernetes\.io/forwarding-rule}')
         echo $FW_RULE
         

The output is similar to the following:
         
         k8s2-fr-j76hrtv4-default-frontend-wvvf7381
         

  3. Add your forwarding rule to the manifest:
         
         sed -i "s/FORWARDING_RULE_NAME/$FW_RULE/g" "extras/postgres-hpa/hpa/frontend.yaml"
         

This command replaces `FORWARDING_RULE_NAME` with your saved forwarding rule.

  4. Apply the manifest to the cluster:
         
         kubectl apply -f extras/postgres-hpa/hpa/frontend.yaml
         


**Objective:** Congratulations! You now have Horizontal Pod Autoscaler rules configured for Deployments in your GKE cluster using built-in metrics from Kubernetes and custom metrics from Monitoring.

## Simulate load

In this section, you use a load generator to simulate spikes in traffic and observe your replica count and node count scale up to accommodate the increased load over time. You can then stop generating traffic and observe the replica and node count scale down in response.

  1. Before you start, check the status of the Horizontal Pod Autoscaler and look at the number of replicas in use.

Get the state of your `HorizontalPodAutoscaler` resources:
         
         kubectl get hpa
         

The output is similar to the following that shows there is 1 `frontend` replica and 5 `userservice` replicas:
         
         NAME                     REFERENCE                            TARGETS             MINPODS   MAXPODS   REPLICAS   AGE
         frontend                 Deployment/frontend                  <unknown>/5 (avg)   5         25        1          34s
         userservice              Deployment/userservice               0%/60%              5         50        5          4m56s
         

  2. The Cymbal Bank sample application includes a `loadgenerator` Service. This Service continuously sends requests imitating users to the frontend, and periodically creates new accounts and simulates transactions between them.

Expose the `loadgenerator` web interface locally. You use this interface to simulate load on the Cymbal Bank sample application:
         
         kubectl port-forward svc/loadgenerator 8080
         

If you see an error message, try again when the Pod is running.

  3. In a browser on your computer, open the load generator web interface:

     * If you're using a local shell, open a browser and go to http://127.0.0.1:8080.
     * If you're using Cloud Shell, click preview **Web preview** , and then click **Preview on port 8080**.
  4. In the load generator web interface, if the **Failures** value shows `100%`, complete the following steps to update the test settings:

     1. Click the **Stop** button next to the failure rate counter.
     2. Under **Status** , click the option for **New test**.
     3. Update the **Host** value to the IP address of your Cymbal Bank ingress.
     4. Click **Start swarming**.
  5. In the load generator web interface, click the **Charts** tab to observe performance over time. Look at the number of requests and resource utilization.

  6. Open a new terminal window and watch the replica count of your `frontend` and `userservice` Pods:
         
         kubectl get hpa -w
         

The number of replicas increases as the load increases. The scaleUp actions might take approximately ten minutes as the cluster recognizes that the configured metrics reach the defined threshold, and use the Horizontal Pod Autoscaler to scale up the number of Pods.

The following example output shows the number of replicas has increased as the load generator runs:
         
         NAME                     REFERENCE                            TARGETS          MINPODS   MAXPODS   REPLICAS
         frontend                 Deployment/frontend                  5200m/5 (avg)    5         25        13
         userservice              Deployment/userservice               71%/60%          5         50        17
         

  7. Open another terminal window and check the number of nodes in the cluster:
         
         gcloud container clusters list \
             --filter='name=scalable-apps' \
             --format='table(name, currentMasterVersion, currentNodeVersion, currentNodeCount)' \
             --location="CONTROL_PLANE_LOCATION"
         

Replace `CONTROL_PLANE_LOCATION` with the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.

The number of nodes has also increased from the starting quantity to accommodate the new replicas. This increase in the number of nodes is powered by GKE Autopilot. There's nothing you need to configure for this node scale.

  8. Open the load generator interface and click **Stop** to end the test.

  9. Check the replica count and node count again and observe as the numbers reduce with the reduced load. The scale down might take some time, because the default stabilization window for replicas in the Kubernetes `HorizontalPodAutoscaler` resource is five minutes.




In a real environment, both the number of nodes and Pods in your environment would automatically scale up and down in the same way as with this simulated load. The Cymbal Bank sample application is designed to accommodate this kind of scaling. Check with your App operators and site reliability engineering (SRE) or Application developers to see if their workloads can benefit from these scaling features.

**Objective:** Congratulations! You can now configure GKE to scale based on load, including using custom metrics from Monitoring.

## Clean up

The set of tutorials for Cymbal Bank is designed to be completed one after the other. As your progress through the set of tutorials, you learn new skills and use additional Google Cloud products and services.

If you want to take a break before you move on to the next tutorial and avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete the project you created.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

Learn how to [simulate a failure in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-failure) in the next tutorial.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
