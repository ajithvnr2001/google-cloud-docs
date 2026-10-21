---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/migrate/knative/
title: Migrating workloads to Knative OSS \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:32.149461+00:00
---

# Migrating workloads to Knative OSS  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/migrate/knative/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Migrating workloads to Knative OSS Stay organized with collections  Save and categorize content based on your preferences. 

Use this guide to migrate your workloads to run on the [open-source Knative](https://knative.dev/docs/) offering with Google Kubernetes Engine. In general, migrating your workloads requires you to install the [Knative Serving](https://knative.dev/docs/serving/) component in a new GKE cluster and then redeploy each of your services to that Knative cluster.

While the use, management, and support for open-source Knative is your choice and responsibility, migrating to Knative provides you with the opportunity to continue running you workloads on the Google Kubernetes Engine platform.

Notable differences:

  * Support is limited to Google Kubernetes Engine. You can contact the [Knative community](https://knative.dev/docs/community/) for Knative support.
  * Google Cloud CLI (`gcloud`) is supported by Google Kubernetes Engine only. Knative supports `kubectl` and `kn` commands. [Learn how to install `kn`](https://knative.dev/docs/install/client/install-kn/)



## Before you begin

  * You must have access to a new GKE cluster. 
    * You can create your new cluster in the same or a new Google Cloud project.
    * Your cluster must meet the [Knative requirements](https://knative.dev/docs/install/operator/knative-with-operators/).
    * Learn how to create a cluster: 
      * [Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster)
      * [Private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters)
  * You must manually port over any cluster configurations to your new Knative cluster, including but not limited to: 
    * [ConfigMaps](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configmap)
    * [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
    * [NVIDIA GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus)
    * [Multitenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy)
    * [Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc)
  * You must create and configure new IAM and RBAC access controls: 
    * [Configure access control](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control)
    * [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)



## Installing Knative on Google Kubernetes Engine

Knative provides several [installation options and networking layers](https://knative.dev/docs/install/) that you can choose to use. The following Knative installation steps use the [Knative Operator method](https://knative.dev/docs/install/operator/knative-with-operators/) and the [Istio networking layer](https://knative.dev/docs/install/installing-istio/).

  1. Install the Knative Operator:

     1. Deploy the Operator to your cluster:
            
            kubectl apply -f https://github.com/knative/operator/releases/download/knative-vVERSION/operator.yaml
            

Replace VERSION with a [version of the Knative Operator](https://github.com/knative/operator/releases).

Example:
            
            kubectl apply -f https://github.com/knative/operator/releases/download/knative-v1.3.1/operator.yaml
            

     2. Set the `kubectl` CLI to use the `default` namespace:
            
            kubectl config set-context --current --namespace=default
            

     3. Verify that the Operator was created successfully:
            
            kubectl get deployment knative-operator
            

Result:
            
            NAME               READY   UP-TO-DATE   AVAILABLE   AGE
            knative-operator   1/1     1            1           6m43s
            

  2. Install the Knative Serving component:

     1. Create a YAML file with the following, for example SERVING_FILENAME.yaml:
            
            apiVersion: v1
            kind: Namespace
            metadata:
              name: knative-serving
            ---
            apiVersion: operator.knative.dev/v1alpha1
            kind: KnativeServing
            metadata:
              name: knative-serving
              namespace: knative-serving
            

     2. Deploy your YAML file to your cluster:
            
            kubectl apply -f SERVING_FILENAME.yaml
            

Replace SERVING_FILENAME with the YAML file that you created.

  3. Install Istio with sidecar injection as the networking layer:

You have the option to perform and configure an alternate Istio installation. See all [Istio installation options](https://knative.dev/docs/install/installing-istio/#installing-istio-without-sidecar-injection) on the Knative website. Note that this installation can take than 30 minutes or more.

     1. [Download Istio from the release page](https://istio.io/latest/docs/setup/getting-started/#download).

     2. Install Istio by running the following command with the `--set hub=gcr.io/istio-release` flag to avoid [Docker rate limiting](https://istio.io/latest/blog/2020/docker-rate-limit/):
            
            istioctl install --set hub=gcr.io/istio-release
            

     3. Run the following command to enable sidecar injection:
            
            kubectl label namespace default istio-injection=enabled
            

     4. Optional: By default, Istio is installed in the `istio-system` namespace. If you want to configure a different namespace, you can use the following steps:

        1. To configure a custom namespace for Istion, you append the `spec.config.istio` attributes to your SERVING_FILENAME.yaml configuration file. For example:
               
               apiVersion: operator.knative.dev/v1alpha1
               kind: KnativeServing
               metadata:
                 name: knative-serving
                 namespace: knative-serving
               spec:
                 # ...
                 config:
                   istio:
                     local-gateway.LOCAL_GATEWAY_NAMESPACE.knative-local-gateway: "knative-local-gateway.ISTIO_NAMESPACE.svc.cluster.local"
               

Replace:

           * LOCAL_GATEWAY_NAMESPACE is the namespace where you installed Knative Serving. Default: `knative-serving`
           * ISTIO_NAMESPACE is the namespace where Istio is installed. Default: `istio-system`
        2. Deploy the updated SERVING_FILENAME.yaml service to your Knative cluster:
               
               kubectl apply -f SERVING_FILENAME.yaml
               

        3. Verify the Istio installation by confirming that `istio-ingressgateway` resides in your specified namespace:
               
               kubectl get svc istio-ingressgateway -n ISTIO_NAMESPACE
               

Replace ISTIO_NAMESPACE with the namespace where you installed Istio. Default: `istio-system`

Result:
               
               NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)                                      AGE
               istio-ingressgateway   LoadBalancer   10.232.10.190   34.123.5.116   15021:30337/TCP,80:32549/TCP,443:31210/TCP   119m
               




## Migrating a service

To migrate a service, you deploy your service's YAML configuration file to your Knative cluster.

**Note:** If you obtain and use the [original YAML configuration file](https://docs.cloud.google.com/anthos/run/docs/deploying#yaml) that you initially created for Knative serving, you can skip the export and modify steps. With the original YAML configuration file, you can simply deploy it directly to your Knative cluster to create your services.

  1. Export your Knative serving service to a local YAML file by running the following command:
         
         gcloud run services describe SERVICE --format export --namespace NAMESPACE --cluster CLUSTER --platform gke > FILENAME.yaml
         

Replace:

     * `SERVICE` with the name of your Knative serving service.
     * `NAMESPACE` with the namespace where your service is running.
     * `CLUSTER` with the name of the cluster where your service is running.
     * `FILENAME` with a unique filename of your choice.
  2. Modify the exported `FILENAME.yaml` file to remove unwanted Knative serving configurations by deleting any of the following attributes and their values:

     * `metadata.annotations.kubectl.kubernetes.io/last-applied-configuration`
     * `metadata.managedFields`
     * `spec.template.spec.containers.readinessProbes`
     * `spec.template.spec.enableServiceLinks`

For example, you might need to remove the following configuration from under the `spec:` > `template:` > `spec:` > `containers:` attributes:
           
           ...
            readinessProbe:
              successThreshold: 1
              tcpSocket: {}
           ...
           

  3. Deploy the modified `.yaml` file to your Knative cluster:
         
         kubectl apply -f SERVICE.yaml
         

Replace SERVICE with the name of your service's configuration file.

  4. Access your deployed service using a test domain or `cURL` commands. You can use a wildcard DNS service to test external access to your service. See the [configuring DNS](https://knative.dev/docs/install/operator/knative-with-operators/#configure-dns) section in the Knative docs for more options.

To use Magic DNS (sslip.io), run the following command.

Note that you can also directly use [sslip.io](http://sslip.io/).
         
         kubectl apply -f https://github.com/knative/serving/releases/download/knative-vVERSION/serving-default-domain.yaml
         

Replace VERSION with your [version of Knative Serving](https://github.com/knative/serving/releases/).

Example:
         
         kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.3.0/serving-default-domain.yaml
         




## Migrating traffic to your service

After you have tested your newly deployed services and are ready to migrate all of your production traffic, you can configure your custom domain and update your DNS records with your registrar. Follow the instructions at [Configuring custom domains](https://knative.dev/docs/serving/services/custom-domains/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
