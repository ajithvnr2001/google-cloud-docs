---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-unmanaged/
title: Self-deployed rule evaluation and alerting \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:18.115572+00:00
---

# Self-deployed rule evaluation and alerting  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-unmanaged/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Self-deployed rule evaluation and alerting Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Managed Service for Prometheus supports Prometheus-compatible rule evaluation and alerting. This document describes how to set up self-deployed rule evaluation, including the standalone rule-evaluator component.

You only need to follow these instructions if you want to execute rules and alerts against the global datastore.

## Rule evaluation for self-deployed collection

After you have deployed Managed Service for Prometheus, you can continue to evaluate rules locally in each deployed instance by using the [`rule_files`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file) field of your Prometheus configuration file. However, the maximum query window for the rules is constrained by how long the server keeps local data.

Most rules execute only over the last few minutes of data, so running rules on each local server is often a valid strategy. In that case, no further setup is necessary.

However, sometimes it's useful to be able to evaluate rules against the global metric backend, for example, when all data for a rule is not co-located on a given Prometheus instance. For these cases, Managed Service for Prometheus also provides a rule-evaluator component.

**Note:** You can create Cloud Monitoring alerting policies based on PromQL queries and Prometheus alert rules. For more information, see [Alerting policies with PromQL](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting).

## Before you begin

This section describes the configuration needed for the tasks described in this document.

### Configure your environment

To avoid repeatedly entering your project ID or cluster name, perform the following configuration:

  * Configure the command-line tools as follows:

    * Configure the gcloud CLI to refer to the ID of your Google Cloud project:
          
          gcloud config set project PROJECT_ID
          

    * If running on GKE, use gcloud CLI to set your cluster:
          
          gcloud container clusters get-credentials CLUSTER_NAME --location LOCATION --project PROJECT_ID
          

    * Otherwise, use the `kubectl` CLI to set your cluster:
          
          kubectl config set-cluster CLUSTER_NAME
          

For more information about these tools, see the following:

    * [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud)
    * [`kubectl` commands](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)



### Set up a namespace

Create the `NAMESPACE_NAME` Kubernetes namespace for resources you create as part of the example application. We recommend using the namespace name `gmp-test` when using this documentation to configure an example Prometheus setup.

Create the namespace by running the following:
    
    
    kubectl create ns NAMESPACE_NAME
    

### Verify service account credentials

**If your Kubernetes cluster has[Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled, then you can skip this section.**

When running on GKE, Managed Service for Prometheus automatically retrieves credentials from the environment based on the Compute Engine default service account. The default service account has the necessary permissions. If you don't use Workload Identity Federation for GKE and if you have previously removed either the `monitoring.metricWriter` and `monitoring.viewer` role grant from the default node service account, then you have to [re-add those missing roles](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#perm-node-svcacct) before continuing.

### Configure a service account for Workload Identity Federation for GKE

**If your Kubernetes cluster doesn't have[Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled, then you can skip this section.**

Managed Service for Prometheus captures metric data by using the Cloud Monitoring API. If your cluster is using Workload Identity Federation for GKE, you must grant your Kubernetes service account permission to the Monitoring API. This section describes the following:

  * Creating a dedicated [Google Cloud service account](https://docs.cloud.google.com/iam/docs/service-accounts), `gmp-test-sa`.
  * Binding the Google Cloud service account to the default [Kubernetes service account](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/) in a test namespace, `NAMESPACE_NAME`.
  * Granting the necessary permission to the Google Cloud service account.



#### Create and bind the service account

This step appears in several places in the Managed Service for Prometheus documentation. If you have already performed this step as part of a prior task, then you don't need to repeat it. Skip ahead to Authorize the service account.

First, create a service account if you haven't yet done so:
    
    
    gcloud config set project PROJECT_ID \
    &&
    gcloud iam service-accounts create gmp-test-sa
    

Then use the following command sequence to bind the`gmp-test-sa` service account to the default Kubernetes service account in the `NAMESPACE_NAME` namespace:
    
    
    gcloud config set project PROJECT_ID \
    &&
    gcloud iam service-accounts add-iam-policy-binding \
      --role roles/iam.workloadIdentityUser \
      --condition=None \
      --member "serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE_NAME/default]" \
      gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com \
    &&
    kubectl annotate serviceaccount \
      --namespace NAMESPACE_NAME \
      default \
      iam.gke.io/gcp-service-account=gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com
    

If you are using a different GKE namespace or service account, adjust the commands appropriately.

#### Authorize the service account

Groups of related permissions are collected into _roles_ , and you grant the roles to a principal, in this example, the Google Cloud service account. For more information about Monitoring roles, see [Access control](https://docs.cloud.google.com/monitoring/access-control).

The following command grants the Google Cloud service account, `gmp-test-sa`, the Monitoring API roles it needs to read and write metric data.

If you have already granted the Google Cloud service account a specific role as part of prior task, then you don't need to do it again.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com \
      --role=roles/monitoring.viewer \
      --condition=None \
    && \
    gcloud projects add-iam-policy-binding PROJECT_ID\
      --member=serviceAccount:gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com \
      --role=roles/monitoring.metricWriter \
      --condition=None \
    && \
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com \
      --role=roles/iam.serviceAccountTokenCreator \
      --condition=None
    

#### Debug your Workload Identity Federation for GKE configuration

If you are having trouble getting Workload Identity Federation for GKE to work, see the documentation for [verifying your Workload Identity Federation for GKE setup](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#verify_the_setup) and the [Workload Identity Federation for GKE troubleshooting guide](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-security#pod_cant_authenticate_to).

As typos and partial copy-pastes are the most common sources of errors when configuring Workload Identity Federation for GKE, we **strongly** recommend using the editable variables and clickable copy-paste icons embedded in the code samples in these instructions.

#### Workload Identity Federation for GKE in production environments

The example described in this document binds the Google Cloud service account to the default Kubernetes service account and gives the Google Cloud service account all necessary permissions to use the Monitoring API.

In a production environment, you might want to use a finer-grained approach, with a service account for each component, each with minimal permissions. For more information on configuring service accounts for workload-identity management, see [Using Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

## Deploy the standalone rule evaluator

The Managed Service for Prometheus rule evaluator evaluates Prometheus alerting and recording rules against the Managed Service for Prometheus [HTTP API](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#api-prometheus) and writes the results back to Monarch. It accepts the same configuration-file format and rule-file format as Prometheus. The flags are mostly identical, as well.

  1. Create an example deployment of the rule evaluator that is pre-configured to evaluate an alerting and a recording rule:
         
         kubectl apply -n NAMESPACE_NAME -f https://raw.githubusercontent.com/GoogleCloudPlatform/prometheus-engine/v0.17.2/manifests/rule-evaluator.yaml
         

  2. Verify that the pods for the rule-evaluator deployed successfully:
         
         kubectl -n NAMESPACE_NAME get pod
         

If the deployment was successful, then you see output similar to the following:
         
         NAME                              READY   STATUS    RESTARTS   AGE
         ...
         rule-evaluator-64475b696c-95z29   2/2     Running   0          1m
         




After you verify that the rule-evaluator deployed successfully, you can make adjustments to the installed manifests to do the following:

  * Add your custom rules files.
  * Configure the rule-evaluator to send alerts to a self-deployed Prometheus [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) by using the [`alertmanager_config`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alertmanager_config) field of the configuration file.



If your Alertmanager is located in a different cluster than your rule-evaluator, then you might need to set up an [Endpoints resource](https://kubernetes.io/docs/concepts/services-networking/service/#services-without-selectors). For example, if your OperatorConfig specifies that Alertmanager endpoints can be found in Endpoints object `ns=alertmanager/name=alertmanager`, then you can manually or programmatically create this object yourself and populate it with reachable IPs from the other cluster.

### Provide credentials explicitly

When running on GKE, the rule-evaluator automatically retrieves credentials from the environment based on the node's service account or the Workload Identity Federation for GKE setup. In non-GKE Kubernetes clusters, credentials must be explicitly provided to the rule-evaluator by using flags or the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.

  1. Set the context to your target project:
         
         gcloud config set project PROJECT_ID
         

  2. Create a service account:
         
         gcloud iam service-accounts create gmp-test-sa
         

This step creates the service account that you might have already created in the Workload Identity Federation for GKE instructions. 

  3. Grant the required permissions to the service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=serviceAccount:gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com \
           --role=roles/monitoring.viewer \
         && \
         gcloud projects add-iam-policy-binding PROJECT_ID\
           --member=serviceAccount:gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com \
           --role=roles/monitoring.metricWriter
         

  4. Create and download a key for the service account:
         
         gcloud iam service-accounts keys create gmp-test-sa-key.json \
           --iam-account=gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com
         

  5. Add the key file as a secret to your non-GKE cluster:
         
         kubectl -n NAMESPACE_NAME create secret generic gmp-test-sa \
           --from-file=key.json=gmp-test-sa-key.json
         

  6. Open the rule-evaluator Deployment resource for editing:
         
         kubectl -n NAMESPACE_NAME edit deploy rule-evaluator
         

     1. Add the text shown in bold to the resource:
            
            apiVersion: apps/v1
            kind: Deployment
            metadata:
              namespace: NAMESPACE_NAME
              name: rule-evaluator
            spec:
              template
                containers:
                - name: evaluator
                  args:
                  **- --query.credentials-file=/gmp/key.json**
                  **- --export.credentials-file=/gmp/key.json**
            ...
                  volumeMounts:
                  **- name: gmp-sa
                    mountPath: /gmp
                    readOnly: true**
            ...
                volumes:
                **- name: gmp-sa
                  secret:
                    secretName: gmp-test-sa**
            ...
            

     2. Save the file and close the editor. After the change is applied, the pods are re-created and start authenticating to the metric backend with the given service account. 

Alternatively, instead of using the flags set in this example, you can set the key-file path by using the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. 

### Multi-project and global rule evaluation

We recommend that you run one instance of the rule evaluator in each Google Cloud project and region rather than running one instance that evaluates against many projects and regions. However, we do support multi-project rule evaluation for scenarios that require it.

When deployed on Google Kubernetes Engine, the rule evaluator uses the Google Cloud project associated with the cluster, which it automatically detects. To evaluate rules that span projects, you can override the queried project by using the `--query.project-id` flag and specifying a project with a multi-project metrics scope. If your metrics scope contains all your projects, then your rules evaluate globally. For more information, see [Metrics scopes](https://docs.cloud.google.com/monitoring/settings#concept-scope).

You must also update the permissions of the service account used by the rule evaluator so the service account can read from the scoping project and write to all monitored projects in the metrics scope.

### Preserve labels when writing rules

For data the evaluator writes back to Managed Service for Prometheus, the evaluator supports the same `--export.*` flags and `external_labels`-based configuration as the Managed Service for Prometheus server binary. We strongly recommend that you write rules so that the `project_id`, `location`, `cluster`, and `namespace` labels are preserved appropriately for their aggregation level, otherwise query performance might decline and you might encounter cardinality limits.

The `project_id` or `location` labels are mandatory. If these labels are missing, then the values in rule-evaluation results are set based on the configuration of the rule evaluator. Missing `cluster` or `namespace` labels are not given values.

### Self-observability

The rule-evaluator emits Prometheus metrics on a configurable port using the `--web.listen-address` flag.

For example, if the pod `rule-evaluator-64475b696c-95z29` is exposing these metrics on port `9092`, the metrics can be viewed manually by using `kubectl`:
    
    # Port forward the metrics endpoint.
    kubectl port-forward rule-evaluator-64475b696c-95z29 9092
    # Then query in a separate terminal.
    curl localhost:9092/metrics
    

You can configure your Prometheus stack to collect these so you have visibility to the performance of the rule-evaluator.

### High-availability deployments

The rule evaluator can run in a highly available setup by following the [same approach](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged#ha-collection) as documented for the Prometheus server.

### Alerting using Cloud Monitoring metrics

You can configure the rule evaluator to alert on [Google Cloud system metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp) using PromQL. For instructions on how to create a valid query, see [PromQL for Cloud Monitoring metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
