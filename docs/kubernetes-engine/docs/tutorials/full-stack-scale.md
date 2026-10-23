---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/full-stack-scale/
title: Run full-stack workloads at scale on GKE \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:55.420456+00:00
---

# Run full-stack workloads at scale on GKE  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/full-stack-scale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Run full-stack workloads at scale on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This tutorial provides instructions for working with Helm version 3.9.3, PostgreSQL version 10.0.1, and the Locust load testing tool. The instructions might not represent newer versions of the app. For more information, refer to the app-specific documentation:

  * [Helm](https://helm.sh/docs/)
  * [PostgreSQL](https://www.postgresql.org/docs/)
  * [Locust](https://docs.locust.io/en/stable/)



This tutorial shows you how to run a web application that is backed by a highly-available relational database at scale in Google Kubernetes Engine (GKE).

The sample application used in this tutorial is Bank of Anthos, an HTTP-based web application that simulates a bank's payment processing network. Bank of Anthos uses multiple services to function. This tutorial focuses on the website frontend and the relational PostgreSQL databases that backs the Bank of Anthos services. To learn more about Bank of Anthos, including its architecture and the services it deploys, refer to [Bank of Anthos on GitHub](https://github.com/GoogleCloudPlatform/bank-of-anthos).

## Objectives

  * Create and configure a GKE cluster.
  * Deploy a sample web application and a highly-available PostgreSQL database.
  * Configure autoscaling of the web application and the database.
  * Simulate spikes in traffic using a load generator.
  * Observe how the services scale up and down.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/pricing#autopilot_mode)
  * [ Internal passthrough Network Load Balancer](https://docs.cloud.google.com/vpc/pricing#lb)
  * [ Cloud Trace](https://docs.cloud.google.com/stackdriver/pricing#trace-costs)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the GKE API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  14. Install the [Helm CLI](https://helm.sh/docs/intro/install/#from-script).



## Prepare the environment

  1. Clone the sample repository used in this tutorial:
         
         git clone https://github.com/GoogleCloudPlatform/bank-of-anthos.git
         cd bank-of-anthos/
         

  2. Set environment variables:
         
         PROJECT_ID=PROJECT_ID
         PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
         SERVICEACCOUNT_NAME=default
         

Replace `PROJECT_ID` with your Google Cloud project ID.




## Set up the cluster and permissions

  1. Create a cluster:
         
         gcloud container clusters create-auto bank-of-anthos --location=us-central1
         

The cluster might take up to five minutes to start.

  2. Grant IAM roles to the `default` Kubernetes ServiceAccount in the `default` namespace:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --role=roles/cloudtrace.agent \
           --member="principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/subject/ns/default/sa/$SERVICEACCOUNT_NAME" \
           --condition=None
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --role=roles/monitoring.metricWriter \
           --member="principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/subject/ns/default/sa/$SERVICEACCOUNT_NAME" \
           --condition=None
         

This step grants the following access to Pods that use the `default` Kubernetes ServiceAccount in the `default` namespace:

     * `roles/cloudtrace.agent`: Write trace data such as latency information to Trace.
     * `roles/monitoring.metricWriter`: Write metrics to Cloud Monitoring.



## Deploy Bank of Anthos and PostgreSQL

In this section, you install Bank of Anthos and a PostgreSQL database in highly-available (HA) mode, which lets you autoscale replicas of the database server. If you want to view the scripts, Helm chart, and Kubernetes manifests used in this section, check the [Bank of Anthos repository on GitHub](https://github.com/GoogleCloudPlatform/bank-of-anthos/tree/main/extras/postgres-hpa).

  1. Deploy the database schema and a data definition language (DDL) script:
         
         kubectl create configmap initdb \
             --from-file=src/accounts/accounts-db/initdb/0-accounts-schema.sql \
             --from-file=src/accounts/accounts-db/initdb/1-load-testdata.sql \
             --from-file=src/ledger/ledger-db/initdb/0_init_tables.sql \
             --from-file=src/ledger/ledger-db/initdb/1_create_transactions.sh
         

  2. Install PostgreSQL using the sample Helm chart:
         
         helm repo add bitnami https://charts.bitnami.com/bitnami
         helm install accounts-db bitnami/postgresql-ha \
             --version 10.0.1 \
             --values extras/postgres-hpa/helm-postgres-ha/values.yaml \
             --set="postgresql.initdbScriptsCM=initdb" \
             --set="postgresql.replicaCount=1" \
             --wait
         

This command creates a PostgreSQL cluster with a starting replica count of 1. Later in this tutorial, you'll scale the cluster based on incoming connections. This operation might take ten minutes or more to complete.

  3. Deploy Bank of Anthos:
         
         kubectl apply -f extras/jwt/jwt-secret.yaml
         kubectl apply -f extras/postgres-hpa/kubernetes-manifests
         

This operation might take a few minutes to complete.




## Checkpoint: Validate your setup

  1. Check that all Bank of Anthos Pods are running:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                                  READY   STATUS
         accounts-db-pgpool-57ffc9d685-c7xs8   3/3     Running
         accounts-db-postgresql-0              1/1     Running
         balancereader-57b59769f8-xvp5k        1/1     Running
         contacts-54f59bb669-mgsqc             1/1     Running
         frontend-6f7fdc5b65-h48rs             1/1     Running
         ledgerwriter-cd74db4cd-jdqql          1/1     Running
         pgpool-operator-5f678457cd-cwbhs      1/1     Running
         transactionhistory-5b9b56b5c6-sz9qz   1/1     Running
         userservice-f45b46b49-fj7vm           1/1     Running
         

  2. Check that you can access the website frontend:

     1. Get the external IP address of the `frontend` service:
            
            kubectl get ingress frontend
            

The output is similar to the following:
            
            NAME       CLASS    HOSTS   ADDRESS         PORTS   AGE
            frontend   <none>   *       203.0.113.9     80      12m
            

     2. In a browser, go to the external IP address. The Bank of Anthos sign in page displays. If you're curious, explore the application.

If you get a 404 error, wait a few minutes for the microservices to provision and try again.




## Autoscale the web app and PostgreSQL database

GKE Autopilot autoscales the cluster compute resources based on the number of workloads in the cluster. To automatically scale the number of Pods in the cluster based on resource metrics, you must implement Kubernetes [horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler). You can use the built-in Kubernetes CPU and memory metrics or you can use custom metrics such as HTTP requests per second or the quantity of SELECT statements, taken from Cloud Monitoring.

In this section, you do the following:

  1. Configure horizontal Pod autoscaling for the Bank of Anthos microservices using both built-in metrics and custom metrics.
  2. Simulate load to the Bank of Anthos application to trigger autoscaling events.
  3. Observe how the number of Pods and the nodes in your cluster automatically scale up and down in response to your load.



### Set up custom metrics collection

To read custom metrics from Monitoring, you must deploy the [Custom Metrics - Stackdriver Adapter](https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/custom-metrics-stackdriver-adapter) adapter in your cluster.

  1. Deploy the adapter:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/deploy/production/adapter.yaml
         

  2. Grant the `custom-metrics-stackdriver-adapter` Kubernetes ServiceAccount the `roles/monitoring.viewer` role by using Workload Identity Federation for GKE:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/subject/ns/custom-metrics/sa/custom-metrics-stackdriver-adapter" \
             --role=roles/monitoring.viewer \
             --condition=None
         




### Configure autoscaling for the database

When you deployed Bank of Anthos and PostgreSQL earlier in this tutorial,, you deployed the database as a StatefulSet with one primary read/write replica to handle all incoming SQL statements. In this section, you configure horizontal Pod autoscaling to add new standby read-only replicas to handle incoming SELECT statements. A good way to reduce the load on each replica is to distribute SELECT statements, which are read operations. The PostgreSQL deployment includes a tool named `Pgpool-II` that achieves this load balancing and improves the system's throughput.

PostgreSQL exports the SELECT statement metric as a [Prometheus metric](https://prometheus.io/docs/concepts/metric_types/). You'll use a lightweight metrics exporter named `prometheus-to-sd` to send these metrics to Cloud Monitoring in a supported format.

  1. Review the `HorizontalPodAutoscaler` object:
         
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
           name: accounts-db-postgresql
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
             kind: StatefulSet
             name: accounts-db-postgresql
           minReplicas: 1
           maxReplicas: 5
           metrics:
           - type: External
             external:
               metric:
                 name: custom.googleapis.com|mypgpool|pgpool2_pool_backend_stats_select_cnt
               target:
                   type: AverageValue
                   averageValue: "15"
         

This manifest does the following:

     * Sets the maximum number of replicas during a scale-up to `5`.
     * Sets the minimum number of during a scale-down to `1`.
     * Uses an external metric to make scaling decisions. In this sample, the metric is the number of SELECT statements. A scale-up event occurs if the incoming SELECT statement count surpasses 15.
  2. Apply the manifest to the cluster:
         
         kubectl apply -f extras/postgres-hpa/hpa/postgresql-hpa.yaml
         




### Configure autoscaling for the web interface

In Deploy Bank of Anthos and PostgreSQL, you deployed the Bank of Anthos web interface. When the number of users increases, the `userservice` Service consumes more CPU resources. In this section, you configure horizontal Pod autoscaling for the `userservice` Deployment when the existing Pods use more than 60% of their requested CPU, and for the `frontend` Deployment when the number of incoming HTTP requests to the load balancer is more than 5 per second.

#### Configure autoscaling for the userservice Deployment

  1. Review the `HorizontalPodAutoscaler` manifest for the `userservice` Deployment:
         
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
         




#### Configure autoscaling for the frontend deployment

  1. Review the `HorizontalPodAutoscaler` manifest for the `userservice` Deployment:
         
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
     * `spec.metrics.*`: The metric to use. In this sample, this is the number of HTTP requests per second, which is a custom metric from Cloud Monitoring provided by the adapter that you deployed.
     * `spec.metrics.external.metric.selector.matchLabels`: The specific resource label to filter when autoscaling.
  2. Find the name of the forwarding rule from the load balancer to the `frontend` Deployment:
         
         export FW_RULE=$(kubectl get ingress frontend -o=jsonpath='{.metadata.annotations.ingress\.kubernetes\.io/forwarding-rule}')
         echo $FW_RULE
         

The output is similar to the following:
         
         k8s2-fr-j76hrtv4-default-frontend-wvvf7381
         

  3. Add your forwarding rule to the manifest:
         
         sed -i "s/FORWARDING_RULE_NAME/$FW_RULE/g" "extras/postgres-hpa/hpa/frontend.yaml"
         

This command replaces `FORWARDING_RULE_NAME` with your saved forwarding rule.

  4. Apply the manifest to the cluster:
         
         kubectl apply -f extras/postgres-hpa/hpa/frontend.yaml
         




## Checkpoint: Validate autoscaling setup

Get the state of your `HorizontalPodAutoscaler` resources:
    
    
    kubectl get hpa
    

The output is similar to the following:
    
    
    NAME                     REFERENCE                            TARGETS             MINPODS   MAXPODS   REPLICAS   AGE
    accounts-db-postgresql   StatefulSet/accounts-db-postgresql   10905m/15 (avg)     1         5         2          5m2s
    contacts                 Deployment/contacts                  1%/70%              1         5         1          11m
    frontend                 Deployment/frontend                  <unknown>/5 (avg)   5         25        1          34s
    userservice              Deployment/userservice               0%/60%              5         50        5          4m56s
    

At this point, you've set up your application and configured autoscaling. Your frontend and database can now scale based on the metrics that you provided.

## Simulate load and observe GKE scaling

Bank of Anthos includes a `loadgenerator` Service that lets you simulate traffic to test your application scaling under load. In this section, you'll deploy the `loadgenerator` Service, generate a load, and observe the resulting scaling.

### Deploy the load testing generator

  1. Create an environment variable with the IP address of the Bank of Anthos load balancer:
         
         export LB_IP=$(kubectl get ingress frontend -o=jsonpath='{.status.loadBalancer.ingress[0].ip}')
         echo $LB_IP
         

The output is similar to the following:
         
         203.0.113.9
         

  2. Add the IP address of the load balancer to the manifest:
         
         sed -i "s/FRONTEND_IP_ADDRESS/$LB_IP/g" "extras/postgres-hpa/loadgenerator.yaml"
         

  3. Apply the manifest to the cluster:
         
         kubectl apply -f  extras/postgres-hpa/loadgenerator.yaml
         




The load generator begins adding one user every second, up to 250 users.

### Simulate load

In this section, you use a load generator to simulate spikes in traffic and observe your replica count and node count scale up to accommodate the increased load over time. You then end the test and observe the replica and node count scale down in response.

  1. Expose the load generator web interface locally:
         
         kubectl port-forward svc/loadgenerator 8080
         

If you see an error message, try again when the Pod is running.

  2. In a browser, open the load generator web interface.

     * If you're using a local shell, open a browser and go to http://127.0.0.1:8080.
     * If you're using Cloud Shell, click preview **Web preview** , and then click **Preview on port 8080**.
  3. Click the **Charts** tab to observe performance over time.

  4. Open a new terminal window and watch the replica count of your horizontal Pod autoscalers:
         
         kubectl get hpa -w
         

The number of replicas increases as the load increases. The scaleup might take approximately ten minutes.
         
         NAME                     REFERENCE                            TARGETS          MINPODS   MAXPODS   REPLICAS
         accounts-db-postgresql   StatefulSet/accounts-db-postgresql   8326m/15 (avg)   1         5         5
         contacts                 Deployment/contacts                  51%/70%          1         5         2
         frontend                 Deployment/frontend                  5200m/5 (avg)    5         25        13
         userservice              Deployment/userservice               71%/60%          5         50        17
         

  5. Open another terminal window and check the number of nodes in the cluster:
         
         gcloud container clusters list \
             --filter='name=bank-of-anthos' \
             --format='table(name, currentMasterVersion, currentNodeVersion, currentNodeCount)' \
             --location="us-central1"
         

  6. The number of nodes increased from the starting quantity of three nodes to accommodate the new replicas.

  7. Open the load generator interface and click **Stop** to end the test.

  8. Check the replica count and node count again and observe as the numbers reduce with the reduced load. The scale down might take some time, because the default stabilization window for replicas in the Kubernetes `HorizontalPodAutoscaler` resource is five minutes. For more information, refer to [Stabilization window](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#stabilization-window).




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete individual resources

Google Cloud creates resources, such as load balancers, based on the Kubernetes objects that you create. To delete all the resources in this tutorial, do the following:

  1. Delete the sample Kubernetes resources:
         
         kubectl delete \
             -f extras/postgres-hpa/loadgenerator.yaml \
             -f extras/postgres-hpa/hpa \
             -f extras/postgres-hpa/kubernetes-manifests \
             -f extras/jwt/jwt-secret.yaml \
             -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/deploy/production/adapter.yaml
         

  2. Delete the PostgreSQL database:
         
         helm uninstall accounts-db
         kubectl delete pvc -l "app.kubernetes.io/instance=accounts-db"
         kubectl delete configmaps initdb
         

  3. Delete the GKE cluster:
         
         gcloud container clusters delete "bank-of-anthos" --location="us-central1" --quiet
         




### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * Learn about [vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler), which you can use to automatically adjust resource requests for long-running workloads with recommendations that are based on historical usage.
  * Learn more about [horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
