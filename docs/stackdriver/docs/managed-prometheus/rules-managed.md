---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed/
title: Managed rule evaluation and alerting \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:36.256811+00:00
---

# Managed rule evaluation and alerting  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Managed rule evaluation and alerting Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Managed Service for Prometheus supports Prometheus-compatible rule evaluation and alerting. This document describes how to set up managed rule evaluation.

## Rule evaluation

Managed Service for Prometheus provides a rule-evaluator component that allows you to safely write rules in the context of a global Prometheus backend, preventing you from interfering with other users' data in larger organizations. The component is automatically deployed as part of [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) when running on Kubernetes clusters.

You can write rules and alerts on both Managed Service for Prometheus metrics and [Cloud Monitoring metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql). You need to use the GlobalRules resource when writing rules for Cloud Monitoring metrics.

**Note:** You can create Cloud Monitoring alerting policies based on PromQL queries and Prometheus alert rules. For more information, see [Alerting policies with PromQL](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting).

### Rules

The managed rule-evaluator uses the [Rules resource](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#rules) to configure recording and alerting rules. The following is an example Rules resource:
    
    
    apiVersion: monitoring.googleapis.com/v1
    kind: Rules
    metadata:
      namespace: NAMESPACE_NAME
      name: example-rules
    spec:
      groups:
      - name: example
        interval: 30s
        rules:
        - record: job:up:sum
          expr: sum without(instance) (up)
        - alert: AlwaysFiring
          expr: vector(1)
    

The format of the `.spec.groups` element is identical to the upstream Prometheus [`rule_group`](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#rule_group) array. Alerting and recording rules defined in `Rules` are scoped to `project_id`, `cluster`, and `namespace` of the resource. For example, the `job:up:sum` rule in the above resource effectively queries `sum without(instance) (up{project_id="test-project", cluster="test-cluster", namespace="NAMESPACE_NAME"})`. This guarantee ensures that alerting or recording rules do not accidentally evaluate metrics from applications you may not even know about.

To apply the example rules to your cluster, run the following command:
    
    
    kubectl apply -n NAMESPACE_NAME -f https://raw.githubusercontent.com/GoogleCloudPlatform/prometheus-engine/v0.17.2/examples/rules.yaml
    

After a few minutes, the metric `job:up:sum` becomes available. The alert `AlwaysFiring` also starts firing. For information about about how to send alerts to an Alertmanager, see Alertmanager configuration.

The [ClusterRules](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#clusterrules) and [GlobalRules](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#globalrules) resources provide the same interface as the `Rules` resource, but they apply the rules to wider scopes. ClusterRules select data by using the `project_id` and `cluster` labels, and GlobalRules select all data in the queried metrics scope without restricting labels.

For reference documentation about all the Managed Service for Prometheus custom resources, see the [prometheus-engine/doc/api reference](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md).

#### Converting from Prometheus rules to Rules

The Rules resource provides a compatible interface to Prometheus rules to provide a seamless migration path for incorporating existing rules into managed rule evaluation. You can include your existing rules in a Rules resource. For example, the following is a Prometheus rule:
    
    
    groups:
    - name: example
      interval: 30s
      rules:
      - record: job:up:sum
        expr: sum without(instance) (up)
      - alert: AlwaysFiring
        expr: vector(1)
    

The corresponding Rules resource, with the original Prometheus rule in bold type, follows:
    
    
    apiVersion: monitoring.googleapis.com/v1
    kind: Rules
    metadata:
      namespace: NAMESPACE_NAME
      name: example-rules
    spec:
      **groups:
      - name: example
        interval: 30s
        rules:
        - record: job:up:sum
          expr: sum without(instance) (up)
        - alert: AlwaysFiring
          expr: vector(1)**
    

### ClusterRules

You can use the [ClusterRules resource](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#clusterrules) to configure recording and alerting rules that can evaluate all time series sent to Managed Service for Prometheus from all namespaces in a particular cluster. The spec is identical to that of `Rules`. The previous example Prometheus rule becomes the following `ClusterRules` resource:
    
    
    apiVersion: monitoring.googleapis.com/v1
    kind: ClusterRules
    metadata:
      name: example-clusterrules
    spec:
      **groups:
      - name: example
        interval: 30s
        rules:
        - record: job:up:sum
          expr: sum without(instance) (up)
        - alert: AlwaysFiring
          expr: vector(1)**
    

We recommend that you use ClusterRules resources only on horizontal metrics, such as those produced by a service mesh. For metrics of individual deployments, use Rules resources to ensure that the evaluation doesn't include unintended data.

### GlobalRules

You can use the [GlobalRules resource](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#globalrules) to configure recording and alerting rules that can evaluate all time series sent to Managed Service for Prometheus across all projects within a [metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope). The spec is identical to that of `Rules`. The previous example Prometheus rule becomes the following `GlobalRules` resource:
    
    
    apiVersion: monitoring.googleapis.com/v1
    kind: GlobalRules
    metadata:
      name: example-globalrules
    spec:
      **groups:
      - name: example
        interval: 30s
        rules:
        - record: job:up:sum
          expr: sum without(instance) (up)
        - alert: AlwaysFiring
          expr: vector(1)**
    

Because [Cloud Monitoring metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql) are not scoped to a namespace or cluster, you must use the GlobalRules resource when writing rules or alerts for Cloud Monitoring metrics. Using GlobalRules is also required when alerting on [Google Kubernetes Engine system metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes).

If your rule does not preserve the `project_id` or `location` labels, they default to the values of the cluster.

For Managed Service for Prometheus metrics, we recommend that you use GlobalRules only for those rare use cases where an alert might need data across all clusters at once. For metrics of individual deployments, use Rules or ClusterRules resources for higher reliability and to ensure that the evaluation doesn't include unintended data. We strongly recommend preserving the `cluster` and `namespace` labels in rule evaluation results unless the purpose of the rule is to aggregate away those labels, otherwise query performance might decline and you might encounter cardinality limits. Removing both labels is strongly discouraged.

#### Multi-project and global rule evaluation

When deployed on Google Kubernetes Engine, the rule evaluator uses the Google Cloud project associated with the cluster, which the rule evaluator automatically detects. To evaluate rules that span projects, you must configure the rule evaluator that executes the GlobalRules resource to use a project with a multi-project metrics scope. You can do this in two ways:

  * Place your GlobalRules resource in a project that has a multi-project metrics scope.
  * Set the `queryProjectID` field within the [OperatorConfig](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#ruleevaluatorspec) to use a project with a multi-project metrics scope.



You must also update the permissions of the service account used by the rule evaluator (which is usually the default service account on the node) so the service account can read from the scoping project and write to all monitored projects in the metrics scope.

If your metrics scope contains all your projects, then your rules evaluate globally. For more information, see [Metrics scopes](https://docs.cloud.google.com/monitoring/settings#concept-scope).

### Alerting using Cloud Monitoring metrics

You can use the GlobalRules resource to alert on [Google Cloud system metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp) using PromQL. For instructions on how to create a valid query, see [PromQL for Cloud Monitoring metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql).

### Configuring rules and alerts using Terraform

You can automate the creation and management of Rules, ClusterRules, and GlobalRules resources by using the [`kubernetes_manifest` Terraform resource type](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/manifest) or the [`kubectl_manifest` Terraform resource type](https://registry.terraform.io/providers/gavinbunney/kubectl/latest/docs/resources/kubectl_manifest), either of which lets you specify arbitrary custom resources.

For general information about using Google Cloud with Terraform, see [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

## Provide credentials explicitly

When running on GKE, the rule-evaluator automatically retrieves credentials from the environment based on the node's service account. In non-GKE Kubernetes clusters, credentials must be explicitly provided through the [OperatorConfig resource](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#operatorconfig) in the gmp-public namespace.

  1. Set the context to your target project:
         
         gcloud config set project PROJECT_ID
         

  2. Create a service account:
         
         gcloud iam service-accounts create gmp-test-sa
         

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
         
         kubectl -n gmp-public create secret generic gmp-test-sa \
           --from-file=key.json=gmp-test-sa-key.json
         

  6. Open the OperatorConfig resource for editing:
         
         kubectl -n gmp-public edit operatorconfig config
         

     1. Add the text shown in bold to the resource:
            
            apiVersion: monitoring.googleapis.com/v1
            kind: OperatorConfig
            metadata:
              namespace: gmp-public
              name: config
            **rules:
              credentials:
                name: gmp-test-sa
                key: key.json**
            

Make sure you also [add these credentials to the `collection` section](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#explicit-credentials) so that managed collection works. 
     2. Save the file and close the editor. After the change is applied, the pods are re-created and start authenticating to the metric backend with the given service account. 

## Scaling rule-evaluation

The `rule-evaluator` Deployment runs as a single replica with fixed resource requests and limits. You might notice that the workload experiences disruptions, such as being OOMKilled when evaluating a high number of rules. To mitigate this issue, you can use a [`VerticalPodAutoscaler`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) to vertically scale the deployment.

To configure vertical pod autoscaling on your cluster, do the following:

     1. Ensure that [Vertical Pod Autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#update-requests-automatically) is enabled on your Kubernetes cluster.
     2. Configure vertical pod autoscaling using one of the following methods:

        * **Autopilot and Standard clusters** : Enable vertical pod autoscaling for Managed Service for Prometheus workloads in your `OperatorConfig` resource. On Autopilot clusters, the `rule-evaluator` Deployment runs in the managed `gke-gmp-system` namespace, where direct resource creation is restricted, so you must configure VPA through the `OperatorConfig` resource:
              
              kubectl -n gmp-public patch operatorconfig/config -p '{"scaling":{"vpa":{"enabled":true}}}' --type=merge
              

For more information, see [Enable vertical pod autoscaling (VPA) for managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#vpa).

        * **Custom VPA policy on Standard clusters** : On Standard clusters, if you want to apply a custom `VerticalPodAutoscaler` policy only to `rule-evaluator` without enabling VPA for all Managed Service for Prometheus components, then apply a `VerticalPodAutoscaler` resource in the `gmp-system` namespace:
              
              apiVersion: autoscaling.k8s.io/v1
              kind: VerticalPodAutoscaler
              metadata:
                name: rule-evaluator
                namespace: gmp-system
              spec:
                resourcePolicy:
                  containerPolicies:
                  - containerName: evaluator
                    controlledResources:
                      - memory
                    maxAllowed:
                      memory: 4Gi
                    minAllowed:
                      memory: 16Mi
                    mode: Auto
                targetRef:
                  apiVersion: apps/v1
                  kind: Deployment
                  name: rule-evaluator
                updatePolicy:
                  updateMode: Auto
              

To verify that the autoscaler is working, check the status of the `VerticalPodAutoscaler` resource. On Standard clusters, check the `gmp-system` namespace; on Autopilot clusters, check the `gke-gmp-system` namespace:
    
    kubectl get vpa --namespace gmp-system rule-evaluator
    

If the autoscaler is working, then it reports that it calculated the resource recommendations for the workload in the `PROVIDED` column:
    
    NAME             MODE   CPU   MEM        PROVIDED   AGE
    rule-evaluator   Auto   2m    11534336   True       30m
    

### Compress configurations

If you have many Rules resources, you might run out of ConfigMap space. To fix this, [enable `gzip` compression](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#configspec) in your [OperatorConfig resource](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#operatorconfig):
    
    apiVersion: monitoring.googleapis.com/v1
      kind: OperatorConfig
      metadata:
        namespace: gmp-public
        name: config
      **features:
        config:
          compression: gzip**
    

## Alertmanager configuration

You can use the [OperatorConfig resource](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#operatorconfig) to configure the managed rule-evaluator to send alerts to a Prometheus [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/). You can send alerts to the automatically-deployed managed Alertmanager in addition to any self-deployed Alertmanagers.

### Managed Alertmanager

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Managed Service for Prometheus deploys a managed instance of Alertmanager, to which the rule evaluators are automatically configured to forward alerts. By default, this configuration is set with a specifically named Kubernetes Secret containing an [Alertmanager config file](https://prometheus.io/docs/alerting/latest/configuration/).

To enable and configure reporting to the deployed Alertmanager instance, do the following:

     1. Create a local config file containing your [Alertmanager settings](https://prometheus.io/docs/alerting/latest/configuration/) (see [sample config templates](https://prometheus.io/docs/alerting/latest/notification_examples/)):
            
            touch alertmanager.yaml
            

     2. Update the file with your desired [Alertmanager settings](https://prometheus.io/docs/alerting/latest/configuration/) and create a Secret named `alertmanager` in the `gmp-public` namespace:
            
            kubectl create secret generic alertmanager \
              -n gmp-public \
              --from-file=alertmanager.yaml
            

After a few moments, Managed Service for Prometheus picks up the new config Secret and enables the managed Alertmanager with your settings.

#### Customizing the config Secret name

The managed Alertmanager also supports custom Secret names for loading the config. This capability is useful when you have multiple config Secrets and you want your Alertmanager instance to switch between the corresponding configs. For example, you might want to change the alert notification channels based on rotating on-call shifts, or you might want to swap in an experimental Alertmanager config to test a new alerting route.

To specify a non-default Secret name by using the OperatorConfig resource, do the following:

     1. Create a Secret from your local Alertmanager config file:
            
            kubectl create secret generic SECRET_NAME \
              -n gmp-public \
              --from-file=FILE_NAME
            

     2. Open the OperatorConfig resource for editing:
            
            kubectl -n gmp-public edit operatorconfig config
            

     3. To enable the managed Alertmanager reporting, edit the resource by modifying the `managedAlertmanager` section as shown in the following bold text:
            
            apiVersion: monitoring.googleapis.com/v1
            kind: OperatorConfig
            metadata:
              namespace: gmp-public
              name: config
            **managedAlertmanager:
              configSecret:
                name: SECRET_NAME
                key: FILE_NAME**
            

If you need to make any changes to the Alertmanager configuration, then you can then edit the configuration for this Alertmanager by updating the Secret you created earlier.

#### Customizing the external URL

You can configure the external URL for the managed Alertmanager so that alert notifications can provide a callback link to your alerting UI. This is equivalent to using upstream Prometheus Alertmanager's `--web.external-url` flag.
    
    apiVersion: monitoring.googleapis.com/v1
    kind: OperatorConfig
    metadata:
      namespace: gmp-public
      name: config
    **managedAlertmanager:
      externalURL: EXTERNAL_URL**
    

### Self-deployed Alertmanager

To configure the rule-evaluator for a self-deployed Alertmanager, do the following:

     1. Open the OperatorConfig resource for editing:
            
            kubectl -n gmp-public edit operatorconfig config
            

     2. Configure the resource to send alerts to your Alertmanager service:
            
            apiVersion: monitoring.googleapis.com/v1
            kind: OperatorConfig
            metadata:
              namespace: gmp-public
              name: config
            rules:
              alerting:
                alertmanagers:
                - name: SERVICE_NAME
                  namespace: SERVICE_NAMESPACE
                  port: PORT_NAME
            

If your Alertmanager is located in a different cluster than your rule-evaluator, you might need to set up a [Endpoints resource](https://kubernetes.io/docs/concepts/services-networking/service/#services-without-selectors). For example, if your OperatorConfig says that Alertmanager endpoints can be found in Endpoints object `ns=alertmanager/name=alertmanager`, you can manually or programmatically create this object yourself and populate it with reachable IPs from the other cluster. The [AlertmanagerEndpoints configuration section](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/doc/api.md#alertmanagerendpoints) provides options for authorization configuration if necessary.

## Conserving resources when idle

When no Rules, ClusterRules, or GlobalRules resources are configured, GKE scales the rule-evaluator and Alertmanager deployments to zero to conserve cluster resources for customers who don't use managed rules or alerts. These deployments will automatically scale up when you apply a new Rules resource. You can force them to scale up by applying a Rules resource which doesn't do anything.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
