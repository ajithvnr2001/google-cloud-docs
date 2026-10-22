---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/elk-stack/
title: Set up Elastic Stack on GKE \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:08.541118+00:00
---

# Set up Elastic Stack on GKE  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/elk-stack/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Set up Elastic Stack on GKE Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot 

This tutorial shows you how to run [Elastic Stack](https://www.elastic.co/elastic-stack) on GKE using the Elastic Cloud on Kubernetes (ECK) operator.

Elastic Stack is a popular open source solution used for logging, monitoring, and analyzing data in real-time. Using Elastic Stack on GKE, you can benefit from the scalability and reliability provided by GKE Autopilot and the powerful Elastic Stack features.

This tutorial is intended for Kubernetes administrators or site reliability engineers.

## Objectives

  * Create a GKE cluster.
  * Deploy the ECK operator.
  * Configure Elasticsearch clusters and Kibana using the ECK operator.
  * Deploy a complete Elastic Stack using the ECK operator.
  * Autoscale Elasticsearch clusters and upgrade the Elastic Stack deployment.
  * Use Elastic Stack to monitor Kubernetes environments.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
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

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
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

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/container.clusterAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.


  * You must own a domain name. The domain name must be no longer than 63 characters. You can use [Cloud Domains](https://docs.cloud.google.com/domains/docs) or another registrar. 



## Prepare the environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell is preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/), [Helm](https://helm.sh/), and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To set up your environment with Cloud Shell, follow these steps:

  1. Launch a Cloud Shell session from the Google Cloud console, by clicking ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** in the [Google Cloud console](https://console.cloud.google.com/). This launches a session in the bottom pane of the Google Cloud console.

  2. Add a Helm chart repository and update it:
         
         helm repo add elastic https://helm.elastic.co
         helm repo update
         

  3. Clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
         

  4. Change to the working directory:
         
         cd kubernetes-engine-samples/observability/elastic-stack-tutorial
         




## Create a GKE cluster

Create a GKE cluster with control plane metrics collection enabled:
    
    
    gcloud container clusters create-auto elk-stack \
        --location="us-central1" \
        --monitoring="SYSTEM,WORKLOAD,API_SERVER,SCHEDULER,CONTROLLER_MANAGER"
    

## Deploy the ECK operator

Elastic Cloud on Kubernetes (ECK) is a platform for deploying and managing the Elastic Stack on Kubernetes clusters.

ECK automates the deployment and management of Elastic Stack clusters, simplifying the process of setting up and maintaining Elastic Stack on Kubernetes. It provides a set of Kubernetes custom resources that you can use to create and configure Elasticsearch, Kibana, Application Performance Management Server, and other Elastic Stack components in Kubernetes. This lets developers and DevOps teams configure and manage Elastic Stack clusters at scale.

ECK supports multiple Elasticsearch nodes, automatic application failover, seamless upgrades, and SSL encryption. ECK also includes features that let you monitor and troubleshoot Elasticsearch performance.

**Note** : This tutorial provides instructions for working with this app: ECKversion 2.8.0. The instructions might not represent newer versions of the app. For more information, see the documentation: [ECK](https://www.elastic.co/downloads/elastic-cloud-kubernetes). 

  1. Install the ECK Helm chart:
         
         helm upgrade --install "elastic-operator" "elastic/eck-operator" \
             --version="2.8.0" \
             --create-namespace \
             --namespace="elastic-system" \
             --set="resources.limits.cpu=250m" \
             --set="resources.limits.memory=512Mi" \
             --set="resources.limits.ephemeral-storage=1Gi" \
             --set="resources.requests.cpu=250m" \
             --set="resources.requests.memory=512Mi" \
             --set="resources.requests.ephemeral-storage=1Gi"
         

  2. Wait for the operator to be ready:
         
         watch kubectl get pods -n elastic-system
         

The output is similar to the following:
         
         NAME                 READY   STATUS    RESTARTS   AGE
         elastic-operator-0   1/1     Running   0          31s
         

When the operator `STATUS` is `Running`, return to the command line by pressing `Ctrl+C`.




## Configure Elastic Stack with ECK

By using Elastic Stack with Elasticsearch, Kibana, and Elastic Agent working in Fleet mode, you can set up a powerful, scalable, and fully-managed solution for managing and visualizing data using Kibana.

Kibana is an open source data analytics and visualization tool that lets you search, analyze and visualize data in Elasticsearch.

Elastic Agent is a lightweight data shipper that collects data from different sources, such as logs or metrics, and automatically sends it to Elasticsearch.

Elastic Fleet is a mode of operation in which Elastic agents report to a central fleet server, which handles their configuration and management. The fleet server simplifies the deployment, configuration, and scaling of Elastic agents, making it easier to manage large and complex deployments.

Elasticsearch autoscaling is a self-monitoring feature that can report when additional resources are needed based on an operator-defined policy. For example, a policy might specify that a certain tier should scale based on available disk space. Elasticsearch can monitor the disk space and suggest scaling if it predicts a shortage, although it is still up to the operator to add the necessary resources. For more information about Elasticsearch autoscaling see [Autoscaling](https://www.elastic.co/guide/en/elasticsearch/reference/current/xpack-autoscaling.html) in the Elasticsearch documentation.

### Configure an Elasticsearch cluster

Elasticsearch provides a distributed, RESTful search and analytics engine designed to store and search large volumes of data quickly and efficiently.

When deploying Elastic Stack on Kubernetes, you should manage the VM settings, specifically the `vm.max_map_count setting`, which is required by Elasticsearch. `vm.max_map_count` specifies the number of memory areas that a process can allocate to a file. Elasticsearch must have this value set to at least `262144` to run optimally. For more information, see [Virtual memory](https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-virtual-memory.html#k8s-virtual-memory) in the ECK documentation.

**Note** : This tutorial provides instructions for working with this app: Elasticversion 8.9.0. The instructions might not represent newer versions of the app. For more information, see the documentation: [Elastic](https://www.elastic.co/downloads/elasticsearch). 

  1. Review the following manifest:
         
         # Copyright 2023 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      https://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: scheduling.k8s.io/v1
         kind: PriorityClass
         metadata:
           name: user-daemonset-priority
         value: 999999999
         preemptionPolicy: PreemptLowerPriority
         globalDefault: false
         description: "User DaemonSet priority"
         ---
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: max-map-count-setter
           namespace: elastic-system
           labels:
             k8s-app: max-map-count-setter
         spec:
           selector:
             matchLabels:
               name: max-map-count-setter
           template:
             metadata:
               labels:
                 name: max-map-count-setter
             spec:
               priorityClassName: user-daemonset-priority
               nodeSelector:
                 cloud.google.com/compute-class: "Balanced"
               initContainers:
                 - name: max-map-count-setter
                   image: docker.io/bash:5.2.15
                   resources:
                     requests:
                       cpu: 10m
                       memory: 10Mi
                       ephemeral-storage: 10Mi
                     limits:
                       cpu: 50m
                       memory: 32Mi
                       ephemeral-storage: 10Mi
                   securityContext:
                     privileged: true
                     runAsUser: 0
                   command: ["/usr/local/bin/bash", "-e", "-c", "echo 262144 > /proc/sys/vm/max_map_count"]
               containers:
                 - name: sleep
                   image: docker.io/bash:5.2.15
                   command: ["sleep", "infinity"]
                   resources:
                     requests:
                       cpu: 10m
                       memory: 10Mi
                       ephemeral-storage: 10Mi
                     limits:
                       cpu: 10m
                       memory: 10Mi
                       ephemeral-storage: 10Mi
         

This manifest describes a DaemonSet that configures the kernel setting on the host directly. A DaemonSet is a Kubernetes controller that helps ensure that a copy of a Pod runs on each node in a cluster.

The preceding manifest is on an allowlist to run on Autopilot. Don't modify this manifest, including the container images.

  2. Apply this manifest to your cluster:
         
         kubectl apply -f max-map-count-setter-ds.yaml
         

  3. Review the following manifest:
         
         apiVersion: elasticsearch.k8s.elastic.co/v1
         kind: Elasticsearch
         metadata:
           name: elasticsearch
           namespace: elastic-system
         spec:
           version: "8.9.0"
           volumeClaimDeletePolicy: DeleteOnScaledownOnly
           podDisruptionBudget:
             spec:
               minAvailable: 2
               selector:
                 matchLabels:
                   elasticsearch.k8s.elastic.co/cluster-name: elasticsearch
           nodeSets:
             - name: default
               config:
                 node.roles: ["master", "data", "ingest", "ml", "remote_cluster_client"]
               podTemplate:
                 metadata:
                   labels:
                     app.kubernetes.io/name: elasticsearch
                     app.kubernetes.io/version: "8.9.0"
                     app.kubernetes.io/component: "elasticsearch"
                     app.kubernetes.io/part-of: "elk"
                 spec:
                   nodeSelector:
                     cloud.google.com/compute-class: "Balanced"
                   initContainers:
                     - name: max-map-count-check
                       command:
                         - sh
                         - -c
                         - while true; do mmc=$(cat /proc/sys/vm/max_map_count); if test ${mmc} -eq 262144; then exit 0; fi; sleep 1; done
                       resources:
                         requests:
                           cpu: 10m
                           memory: 16Mi
                           ephemeral-storage: 16Mi
                         limits:
                           cpu: 10m
                           memory: 16Mi
                           ephemeral-storage: 16Mi
                   containers:
                     - name: elasticsearch
                       resources:
                         requests:
                           cpu: 990m
                           memory: 4080Mi
                           ephemeral-storage: 1008Mi
                         limits:
                           cpu: 1000m
                           memory: 4080Mi
                           ephemeral-storage: 1008Mi
                       env:
                         - name: ES_JAVA_OPTS
                           value: "-Xms2g -Xmx2g"
               count: 3
               volumeClaimTemplates:
                 - metadata:
                     name: elasticsearch-data # Do not change this name unless you set up a volume mount for the data path.
                   spec:
                     accessModes:
                       - ReadWriteOnce
                     resources:
                       requests:
                         storage: 2Gi
                     storageClassName: standard-rwo

This manifest defines an Elasticsearch cluster with the following fields:

     * `initContainers`: waits for the virtual memory host's kernel settings to change.
     * `podDisruptionBudget`: specifies that the cluster won't be destroyed during the Pods' defragmentation process.
     * `config.node.roles`: Elasticsearch node roles configuration. For more information about node roles, see [Node](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-node.html) in the Elasticsearch documentation.
  4. Apply this manifest to your cluster:
         
         kubectl apply -f elasticsearch.yaml
         

  5. Wait for the Elasticsearch cluster to be ready:
         
         watch kubectl --namespace elastic-system get elasticsearches.elasticsearch.k8s.elastic.co
         

The output is similar to the following:
         
         NAME            HEALTH   NODES   VERSION   PHASE   AGE
         elasticsearch   green    3       8.8.0     Ready   5m3s
         

When the Elasticsearch cluster `HEALTH` is `green` and `PHASE` is `Ready`, return to the command line by pressing `Ctrl+C`.




## Configure Kibana

**Note** : This tutorial provides instructions for working with this app: Elasticversion 8.9.0. The instructions might not represent newer versions of the app. For more information, see the documentation: [Elastic](https://www.elastic.co/downloads/elasticsearch). 

  1. Review the following manifest:
         
         apiVersion: kibana.k8s.elastic.co/v1
         kind: Kibana
         metadata:
           name: kibana
           namespace: elastic-system
         spec:
           version: "8.9.0"
           count: 1
           elasticsearchRef:
             name: elasticsearch
             namespace: elastic-system
           http:
             tls:
               selfSignedCertificate:
                 disabled: true
           config:
             server.publicBaseUrl: https://elk.BASE_DOMAIN
             xpack.reporting.kibanaServer.port: 5601
             xpack.reporting.kibanaServer.protocol: http
             xpack.reporting.kibanaServer.hostname: kibana-kb-http.elastic-system.svc
             xpack.fleet.agents.elasticsearch.hosts: ["https://elasticsearch-es-http.elastic-system.svc:9200"]
             xpack.fleet.agents.fleet_server.hosts: ["https://fleet-server-agent-http.elastic-system.svc:8220"]
             xpack.fleet.packages:
             - name: system
               version: latest
             - name: elastic_agent
               version: latest
             - name: fleet_server
               version: latest
             - name: kubernetes
               version: latest
             xpack.fleet.agentPolicies:
             - name: Fleet Server on ECK policy
               id: eck-fleet-server
               namespace: default
               monitoring_enabled:
               - logs
               - metrics
               unenroll_timeout: 900
               package_policies:
               - name: fleet_server-1
                 id: fleet_server-1
                 package:
                   name: fleet_server
             - name: Elastic Agent on ECK policy
               id: eck-agent
               namespace: default
               monitoring_enabled:
               - logs
               - metrics
               unenroll_timeout: 900
               package_policies:
               - package:
                   name: system
                 name: system-1
               - package:
                   name: kubernetes
                 name: kubernetes-1
           podTemplate:
             metadata:
               labels:
                 app.kubernetes.io/name: kibana
                 app.kubernetes.io/version: "8.9.0"
                 app.kubernetes.io/component: "ui"
                 app.kubernetes.io/part-of: "elk"
             spec:
               containers:
               - name: kibana
                 resources:
                   requests:
                     memory: 1Gi
                     cpu: 500m
                     ephemeral-storage: 1Gi
                   limits:
                     memory: 1Gi
                     cpu: 500m
                     ephemeral-storage: 1Gi

This manifest describes a Kibana custom resource that configures agent policies for the fleet server and agents.

  2. Apply this manifest to your cluster:
         
         kubectl apply -f kibana.yaml
         

  3. Wait for the Pods to be ready:
         
         watch kubectl --namespace elastic-system get kibanas.kibana.k8s.elastic.co
         

The output is similar to the following:
         
         NAME     HEALTH   NODES   VERSION   AGE
         kibana   green    1       8.8.0     6m47s
         

When the Pods `HEALTH` is `green`, return to the command line by pressing `Ctrl+C`.




## Configure a load balancer to access Kibana

To access Kibana, create a Kubernetes Ingress object, a Google-managed certificate, a global IP address, and a DNS Zone.

  1. Create global external IP address:
         
         gcloud compute addresses create "elastic-stack" --global
         

  2. Create a managed zone and record set in Cloud DNS:
         
         gcloud dns managed-zones create "elk" \
             --description="DNS Zone for Airflow" \
             --dns-name="elk.BASE_DOMAIN" \
             --visibility="public"
         
         gcloud dns record-sets create "elk.BASE_DOMAIN" \
             --rrdatas="$(gcloud compute addresses describe "elastic-stack" --global --format="value(address)")" \
             --ttl="300" \
             --type="A" \
             --zone="elk"
         

  3. Delegate the DNS zone as a subdomain of the base domain by creating an NS record set with a name servers list. You can get a list of name servers using the following command:
         
         gcloud dns record-sets describe elk.BASE_DOMAIN \
             --type="NS" \
             --zone="elk" \
             --format="value(DATA)"
         

  4. Review the following manifest:
         
         # Copyright 2023 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      https://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: networking.gke.io/v1beta1
         kind: FrontendConfig
         metadata:
           name: elastic-stack
           namespace: elastic-system
         spec:
           redirectToHttps:
             enabled: true
             responseCodeName: MOVED_PERMANENTLY_DEFAULT
         ---
         apiVersion: networking.gke.io/v1
         kind: ManagedCertificate
         metadata:
           name: elastic-stack
           namespace: elastic-system
         spec:
           domains:
             - elk.BASE_DOMAIN
         ---
         apiVersion: networking.k8s.io/v1
         kind: Ingress
         metadata:
           name: kibana
           namespace: elastic-system
           annotations:
             networking.gke.io/managed-certificates: elastic-stack
             networking.gke.io/v1beta1.FrontendConfig: elastic-stack
             kubernetes.io/ingress.global-static-ip-name: elastic-stack
             kubernetes.io/ingress.class: gce
         spec:
           defaultBackend:
             service:
               name: kibana-kb-http
               port:
                 number: 5601
         

This manifest describes a ManagedCertificate that provisions an SSL certificate to establish the TLS connection.

  5. Apply the manifest to your cluster:
         
         kubectl apply -f ingress.yaml
         




## Configure Elastic Agents

**Note** : This tutorial provides instructions for working with this app: Elasticversion 8.9.0. The instructions might not represent newer versions of the app. For more information, see the documentation: [Elastic](https://www.elastic.co/downloads/elasticsearch). 

  1. Review the following manifest:
         
         apiVersion: agent.k8s.elastic.co/v1alpha1
         kind: Agent
         metadata:
           name: fleet-server
           namespace: elastic-system
         spec:
           version: 8.9.0
           kibanaRef:
             name: kibana
             namespace: elastic-system
           elasticsearchRefs:
             - name: elasticsearch
               namespace: elastic-system
           mode: fleet
           fleetServerEnabled: true
           policyID: eck-fleet-server
           deployment:
             replicas: 1
             podTemplate:
               metadata:
                 labels:
                   app.kubernetes.io/name: fleet-server
                   app.kubernetes.io/version: "8.9.0"
                   app.kubernetes.io/component: "agent"
                   app.kubernetes.io/part-of: "elk"
               spec:
                 containers:
                   - name: agent
                     resources:
                       requests:
                         memory: 512Mi
                         cpu: 250m
                         ephemeral-storage: 10Gi
                       limits:
                         memory: 512Mi
                         cpu: 250m
                         ephemeral-storage: 10Gi
                 volumes:
                   - name: "agent-data"
                     ephemeral:
                       volumeClaimTemplate:
                         spec:
                           accessModes: ["ReadWriteOnce"]
                           storageClassName: "standard-rwo"
                           resources:
                             requests:
                               storage: 10Gi
                 serviceAccountName: fleet-server
                 automountServiceAccountToken: true
                 securityContext:
                   runAsUser: 0

This manifest describes an Elastic Agent that configures a fleet server with ECK.

  2. Apply this manifest to your cluster:
         
         kubectl apply -f fleet-server-and-agents.yaml
         

  3. Wait for the Pods to be ready:
         
         watch kubectl --namespace elastic-system get agents.agent.k8s.elastic.co
         

The output is similar to the following:
         
         NAME            HEALTH   AVAILABLE   EXPECTED   VERSION   AGE
         elastic-agent   green    5           5          8.8.0     14m
         fleet-server    green    1           1          8.8.0     16m
         

When the Pods `HEALTH` is `green`, return to the command line by pressing `Ctrl+C`.




## Configure logging and monitoring

Elastic Stack can use the kube-state-metrics exporter to collect cluster-level metrics.

  1. Install kube-state-metrics:
         
         helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
         helm repo update
         helm install kube-state-metrics prometheus-community/kube-state-metrics --namespace elastic-system
         

  2. Get the default Kibana `elastic` user credentials:
         
         kubectl get secret elasticsearch-es-elastic-user -o yaml -n elastic-system -o jsonpath='{.data.elastic}' | base64 -d
         

  3. Open `https://elk.BASE_DOMAIN` in your browser and login to Kibana with the credentials.

  4. From the menu, select **Analytics** , then **Dashboards**.

  5. In the search text field, enter **Kubernetes overview** and select **Overview dashboard** to see base metrics.

Some of the dashboard panels might show no data or error messages because GKE limits access to some of the control plane endpoints that Kibana uses to get cluster metrics.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete the individual resources

If you used an existing project and you don't want to delete it, delete the individual resources.

  1. Delete the Elastic Stack components, ECK operator, and kube-state-metrics:
         
         kubectl --namespace elastic-system delete ingresses.networking.k8s.io elastic-stack
         kubectl --namespace elastic-system delete managedcertificates.networking.gke.io elastic-stack
         kubectl --namespace elastic-system delete frontendconfigs.networking.gke.io elastic-stack
         kubectl --namespace elastic-system delete agents.agent.k8s.elastic.co elastic-agent
         kubectl --namespace elastic-system delete agents.agent.k8s.elastic.co fleet-server
         kubectl --namespace elastic-system delete kibanas.kibana.k8s.elastic.co kibana
         kubectl --namespace elastic-system delete elasticsearches.elasticsearch.k8s.elastic.co elasticsearch
         kubectl --namespace elastic-system delete daemonsets.apps max-map-count-setter
         kubectl --namespace elastic-system delete pvc --selector='elasticsearch.k8s.elastic.co/cluster-name=elasticsearch'
         helm --namespace elastic-system uninstall kube-state-metrics
         helm --namespace elastic-system uninstall elastic-operator
         

  2. Delete the DNS record set, IP address, DNS managed zone, and GKE cluster:
         
         gcloud dns record-sets delete "elk.BASE_DOMAIN" \
             --type="A" \
             --zone="elk" \
             --quiet
         
         gcloud compute addresses delete "elastic-stack" \
             --global \
             --quiet
         
         gcloud dns managed-zones delete "elk" --quiet
         
         gcloud container clusters delete "elk-stack" \
             --location="us-central1" \
             --quiet
         




## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
