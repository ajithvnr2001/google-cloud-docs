---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged/
title: Get started with self-deployed collection \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:51.676975+00:00
---

# Get started with self-deployed collection  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Get started with self-deployed collection Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up Google Cloud Managed Service for Prometheus with self-deployed collection. An example application is deployed to a Kubernetes cluster and is monitored by a Prometheus server that stores collected metrics in Monarch.

**Compute Engine users:** If you want to collect Prometheus metrics from Compute Engine VM instances, then the recommended option is to [use the Ops Agent and configure the Prometheus receiver](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/prometheus). 

This document shows you how to do the following:

  * Set up your environment and command-line tools.
  * Configure a service account for Workload Identity Federation for GKE-enabled clusters.
  * Run the drop-in Prometheus binary on Kubernetes.
  * Control which metrics are ingested into Managed Service for Prometheus.
  * Integrate Managed Service for Prometheus with prometheus-operator setups.
  * Manually compile and run the Prometheus binary.



With self-deployed data collection, you manage your Prometheus installation as you always have. The only difference is that you run the Managed Service for Prometheus drop-in replacement binary, `gke.gcr.io/prometheus-engine/prometheus:v2.53.5-gmp.1-gke.2`, instead of the upstream Prometheus binary.

The drop-in binary provides additional configuration options with the `--export.*` flags. For more information, see the output of the `--help` option. This document points out the most important options.

**Managed Service for Prometheus does not support exporting metrics from a federation server or from a server used as a remote-write receiver**. You can replicate all federation server functionality, including reducing ingestion volume by aggregating data before sending to Monarch, by using filters and [local aggregations](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls#local-aggregation).

Streaming data to Managed Service for Prometheus consumes additional resources. If you are self-deploying collectors, then we recommend increasing CPU and memory limits by 5x and adjusting them based on actual usage.

For more information about managed and self-deployed data collection, see [Data collection with Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus#gmp-data-collection).

**Note:** Google Cloud technical support provides limited assistance for self-deployed collection.

## Before you begin

This section describes the configuration needed for the tasks described in this document.

### Set up projects and tools

To use Google Cloud Managed Service for Prometheus, you need the following resources:

  * A Google Cloud project with the Cloud Monitoring API enabled.

    * If you don't have a Google Cloud project, then do the following:

      1. In the Google Cloud console, go to **New Project** :

[Create a New Project](https://console.cloud.google.com/projectcreate)

      2. In the **Project Name** field, enter a name for your project and then click **Create**.

      3. Go to **Billing** :

[Go to Billing](https://console.cloud.google.com/billing)

      4. Select the project you just created if it isn't already selected at the top of the page.

      5. You are prompted to choose an existing payments profile or to create a new one.

The Monitoring API is enabled by default for new projects.

    * If you already have a Google Cloud project, then ensure that the Monitoring API is enabled:

      1. Go to the Monitoring API library page in the Google Cloud console:

[Go to the **Library** page](https://console.cloud.google.com/apis/library/monitoring.googleapis.com)

      2. Select your project.

      3. The Monitoring API is enabled if you see a **Manage** button on the library page. If you see an **Enable** button, then the API isn't enabled, and you must click the **Enable** button to enable it.

  * A Kubernetes cluster. If you don't have a Kubernetes cluster, then follow the instructions in the [Quickstart for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster).




You also need the following command-line tools:

  * `gcloud`
  * `kubectl`



The `gcloud` and `kubectl` tools are part of the Google Cloud CLI. For information about installing them, see [Managing Google Cloud CLI components](https://docs.cloud.google.com/sdk/docs/components). To see the gcloud CLI components you have installed, run the following command:
    
    
    gcloud components list
    

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

The following command grants the Google Cloud service account, `gmp-test-sa`, the Monitoring API roles it needs to write metric data.

If you have already granted the Google Cloud service account a specific role as part of prior task, then you don't need to do it again.
    
    
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

## Set up self-deployed collection

This section describes how to set up and run an example application that uses self-deployed collection.

### Deploy the example application

The [example application](https://github.com/nilebox/prometheus-example-app) emits the `example_requests_total` counter metric and the `example_random_numbers` histogram metric (among others) on its `metrics` port. The manifest for the application defines three replicas.

To deploy the example application, run the following command:
    
    
    kubectl -n NAMESPACE_NAME apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/prometheus-engine/v0.17.2/examples/example-app.yaml
    

### Run the replacement Prometheus binary

To ingest the metric data emitted by the example application, you deploy Google's forked version of the Prometheus server, which is configured to scrape the workload's metrics as well as its own metrics endpoint.

  1. To deploy the forked server, run the following command:
         
         kubectl -n NAMESPACE_NAME apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/prometheus-engine/v0.17.2/examples/prometheus.yaml
         

This deployed Prometheus server is a thin fork of the upstream Prometheus binary. It behaves like a standard Prometheus server, but it also ingests data into Managed Service for Prometheus.

The manifest above provides a basic working example that sends data to the global datastore, Monarch. It does not persistently store a local copy of data. For information on how this predefined configuration works and how to extend it, see the open source [Prometheus configuration documentation](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).

The prebuilt image only works on Linux nodes. To scrape targets running on Windows nodes, either deploy the server on a Linux node and configure it to scrape endpoints on the Windows nodes or build the binary for Windows yourself.

  2. Verify that the pods for the Prometheus server and the example application deployed successfully:
         
         kubectl -n NAMESPACE_NAME get pod
         

If the deployment was successful, then you see output similar to the following:
         
         NAME                            READY   STATUS    RESTARTS   AGE
         prom-example-84c6f547f5-fglbr   1/1     Running   0          5m
         prom-example-84c6f547f5-jnjp4   1/1     Running   0          5m
         prom-example-84c6f547f5-sqdww   1/1     Running   0          5m
         prometheus-test-0               2/2     Running   1          3m
         




If you are running on GKE, then you can do the following:

  * To query the metrics ingested by the example application, see [Query using Cloud Monitoring](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-cm) or [Query using Grafana](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query).
  * To learn about using prometheus-operator and kube-prometheus with self-deployed collection, and to see how to build and run the binary for the managed service, see Additional topics for self-deployed collection.



If you are running outside of GKE, then you need to create a service account and authorize it to write your metric data, as described in the following section.

### Provide credentials explicitly

When running on GKE, the collecting Prometheus server automatically retrieves credentials from the environment based on the node's service account or the Workload Identity Federation for GKE setup. In non-GKE Kubernetes clusters, credentials must be explicitly provided to the collecting Prometheus server by using flags or the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.

  1. Set the context to your target project:
         
         gcloud config set project PROJECT_ID
         

  2. Create a service account:
         
         gcloud iam service-accounts create gmp-test-sa
         

This step creates the service account that you might have already created in the Workload Identity Federation for GKE instructions. 

  3. Grant the required permissions to the service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID\
           --member=serviceAccount:gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com \
           --role=roles/monitoring.metricWriter
         

  4. Create and download a key for the service account:
         
         gcloud iam service-accounts keys create gmp-test-sa-key.json \
           --iam-account=gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com
         

  5. Add the key file as a secret to your non-GKE cluster:
         
         kubectl -n NAMESPACE_NAME create secret generic gmp-test-sa \
           --from-file=key.json=gmp-test-sa-key.json
         

  6. Open the Prometheus StatefulSet resource for editing:
         
         kubectl -n NAMESPACE_NAME edit statefulset prometheus-test
         

     1. Add the text shown in bold to the resource:
            
            apiVersion: apps/v1
            kind: StatefulSet
            metadata:
              namespace: NAMESPACE_NAME
              name: example
            spec:
              template
                containers:
                - name: prometheus
                  args:
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

## Additional topics for self-deployed collection

This section describes how to do the following:

     * Filter the data you export to the managed service.
     * Convert your existing deployment configurations.
     * Run the Prometheus binary in high-availability mode.
     * Build and run the replacement Prometheus binary.
     * Run Managed Service for Prometheus outside of Google Cloud.

### Filter exported metrics

If you collect a lot of data, you might want to prevent some time series from being sent to Managed Service for Prometheus to keep costs down.

You can use regular [metric-relabeling configs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config) in your Prometheus scraping configuration. With relabeling configs, you can drop metrics based on label matches at ingestion time.

Sometimes, you might want to ingest data locally but not export it to Managed Service for Prometheus. To filter exported metrics, you can use the `--export.match` flag.

The flag specifies one or more [PromQL series selectors](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors), and the flag can be used multiple times. A time series is exported to Managed Service for Prometheus if it satisfies all of the selectors in at least one of the flags; that is, when determining eligibility, conditions within a single flag are ANDed while conditions in separate flags are ORed. The following example uses two instances of the flag:
    
    ./prometheus \
      --export.match='{job="prometheus"}' \
      --export.match='{__name__=~"job:.+"}' \
      ...
    

This change causes only metrics for the "prometheus" job as well as metrics produced by recording rules that aggregate to the job level (when following naming best practices) to be exported. Samples for all other series are filtered out. By default, no selectors are specified and all time series are exported.

The `--export.match` flag has the same semantics as the `match[]` parameter for Prometheus federation. You can therefore migrate federation setups to Managed Service for Prometheus by using the selectors from your federation server directly as flags on the Prometheus servers scraped by your federation Prometheus server. **Exporting metrics from a federation server to the managed service is not supported**.

To include `histogram`-type metrics in a filter, you must specify the `_count`, `_sum`, and `_bucket` metrics. You can also do this with a wildcard matcher, for example the selector `{__name__=~"histogram_metric_.+"}`.

If you are using the `prometheus-operator` library, then set any `--export.match` flags using the `EXTRA_ARGS` environment variable of the container. For more information, see Use with prometheus-operator.

You can combine filter flags with locally run recording rules to "roll up" data before sending to Monarch, reducing your cardinality and cost. For more information, see [Cost controls and attribution](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls#local-aggregation).

The Cloud Monitoring **Metrics Management** page provides information that can help you control the amount you spend on billable metrics without affecting observability. The **Metrics Management** page reports the following information: 

     * Ingestion volumes for both byte- and sample-based billing, across metric domains and for individual metrics.
     * Data about labels and cardinality of metrics.
     * Number of reads for each metric.
     * Use of metrics in alerting policies and custom dashboards.
     * Rate of metric-write errors.

You can also use the **Metrics Management** page to [exclude unneeded metrics](https://docs.cloud.google.com/monitoring/docs/metrics-management#exclude-metrics), eliminating the cost of ingesting them. For more information about the **Metrics Management** page, see [View and manage metric usage](https://docs.cloud.google.com/monitoring/docs/metrics-management).

### Use with prometheus-operator

The Managed Service for Prometheus Prometheus binary can also be used with an existing GKE Prometheus deployment managed by [prometheus-operator](https://github.com/prometheus-operator).

To use the managed service's binary, replace the image specification in the Prometheus resource:
    
    apiVersion: monitoring.coreos.com/v1
      kind: Prometheus
      metadata:
        name: NAMESPACE_NAME
        namespace: gmp-system
      **spec:
        image: gke.gcr.io/prometheus-engine/prometheus:v2.53.5-gmp.1-gke.2**
        ...
        replicas: 1
        serviceAccountName: default
        version: v2.35.0
        ...
    

If you are in a Workload Identity Federation for GKE cluster and the namespace or service account in your resource differs, repeat the Workload Identity Federation for GKE instructions for the additional namespace and Kubernetes service account pair.

When running on a non-GKE Kubernetes cluster, you need to manually provide credentials. To provide credentials, do the following:

     1. Add an appropriate service account key file as a secret, as described in Provide credentials explicitly.

     2. Modify the Prometheus resource to add the text shown in bold type:
            
            apiVersion: monitoring.coreos.com/v1
              kind: Prometheus
              metadata:
                namespace: NAMESPACE_NAME
                name: example
              spec:
                ...
                **secrets:
                - gmp-test-sa
                containers:
                - name: prometheus
                  env:
                  - name: GOOGLE_APPLICATION_CREDENTIALS
                    value: /gmp/key.json
                  volumeMounts:
                  - name: secret-gmp-test-sa
                    mountPath: /gmp
                    readOnly: true**
            

You can set the `EXTRA_ARGS` environment variable of the container to add additional flags, such as the metric filtering flags. This is done through an environment variable because the `args` section of the container specification is managed by Prometheus Operator.

### Use with kube-prometheus

You can configure deployments created using the popular [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus#quickstart) library to use Managed Service for Prometheus.

Kube-prometheus has some tight internal dependencies on its default namespaces and service accounts, so we recommend only changing the minimum number of fields necessary to send data to Managed Service for Prometheus.

Within `manifests/prometheus-prometheus.yaml`, replace the image specification and turn off high-availability collection by reducing `replicas` to 1:
    
    apiVersion: monitoring.coreos.com/v1
        kind: Prometheus
        ...
        **spec:
          image: gke.gcr.io/prometheus-engine/prometheus:v2.53.5-gmp.1-gke.2**
          ...
          replicas: 1
          version: v2.35.0
          ...
      

If you are running on GKE and have not modified the default service account on the node, applying the modified manifests should immediately start sending data to Managed Service for Prometheus. Otherwise, you might have to configure and apply a service account. When running on GKE and using workload identity, you might have to create and authorize the `prometheus-k8s` service account within the `monitoring` namespace. When running on a non-GKE Kubernetes cluster, follow the instructions in the prometheus-operator section.

Note that kube-prometheus collects a lot of metrics by default, most of which are often not necessary in a managed Kubernetes environment like GKE. To save on ingestion costs, you can customize kube-prometheus so that it scrapes only metrics you care about and filter exported metrics aggressively.

For more suggestions, see [Cost controls and attribution](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls).

### High-availability deployment

The replacement Prometheus binary comes with built-in support for highly available collection by using leader election. Replicated Prometheus servers in high-availability mode both collect metrics and evaluate rules as usual, but only one of them sends data to Google Cloud Managed Service for Prometheus.

Replicas of the same Prometheus server must always have identical configurations, including the same [`external_labels`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/). This requirement differs from other systems, which rely on a special external label, such as `__replica__`, to make replicas explicitly different.

The Kubernetes API server is a supported leader-election backend and can be enabled by setting the following flags:
    
    ./prometheus
      ...
      --export.ha.backend=kube \
      --export.ha.kube.namespace=LEASE_NAMESPACE \
      --export.ha.kube.name=LEASE_NAME
    

The LEASE_NAMESPACE and LEASE_NAME values identify the [Lease resource](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/lease-v1) through which leader election takes place. All Prometheus servers pointing at the same resource belong to the same replica set. The Kubernetes service account of the Prometheus deployment needs permission to read and write the respective Lease resource. When running the Prometheus server outside of a Kubernetes cluster, you can provide an explicit config by using the `--export.ha.kube.config` flag.

After you do this, you can increase the `replicas` value to 2 or greater.

### Reserved labels

Managed Service for Prometheus uses six reserved labels to uniquely identify a resource in Monarch:

     * `project_id`: The identifier of the Google Cloud project associated with your metric. Required.
     * `location`: The physical location (Google Cloud region) where the data is stored. This value is typically the region of your GKE cluster. If data is collected from an AWS or on-premises deployment, then the value might be the closest Google Cloud region. Required.
     * `cluster`: The name of the Kubernetes cluster associated with your metric. If not running on Kubernetes, this can be used as an arbitrary hierarchy level such as an instance group. Optional but strongly recommended.
     * `namespace`: The name of the Kubernetes namespace associated with your metric. If not running on Kubernetes, this can be used as an arbitrary hierarchy level such as an instance sub-group. Optional but strongly recommended.
     * `job`: The job label of the Prometheus target, if known; might be empty for rule-evaluation results. Required and typically added automatically by Prometheus.
     * `instance`: The instance label of the Prometheus target, if known; might be empty for rule-evaluation results. Required and typically added automatically by Prometheus. If manually set or relabeled, don't use hardcoded values like `localhost`, as doing so causes time series collisions.

When running on Google Cloud, the `project_id`, `location`, and `cluster` labels are automatically added to every metric.

While not recommended when running on Google Cloud, you can override the `project_id`, `location`, `cluster`, and `namespace` labels using the `global.external_labels` section of your Prometheus config. For more information, see Run self-deployed collection outside of Google Cloud.

If you use any reserved labels as metric labels, self-deployed collection will use the metric label as the value for the reserved label. This can provide some flexibility, but also may lead to errors if, for example, you use the label `location` to refer to something other than a Google Cloud region.

### Configure statsd_exporter and other exporters that report metrics centrally

If you use the statsd_exporter for Prometheus, Envoy for Istio, the SNMP exporter, the Prometheus Pushgateway, kube-state-metrics, or you otherwise have a similar exporter that intermediates and reports metrics on behalf of other resources running in your environment, then you need to make some small changes for your exporter to work with Managed Service for Prometheus.

For instructions on configuring these exporters, see [this note in the Troubleshooting section](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#context-deadline-increase).

### Binary deployments

If you want to run in a non-containerized environment, you can build the replacement Prometheus binary directly.

#### Building the source

If you have an existing process for compiling Prometheus yourself, you can transparently substitute our [GitHub repository](https://github.com/GoogleCloudPlatform/prometheus) into your process. Managed Service for Prometheus has its own version-tag extension to distinguish its releases from upstream releases.

To build the plain binary, the Go toolchain and recent versions of NPM/Yarn must be installed on the machine. For more information, see the [upstream build instructions](https://github.com/prometheus/prometheus#building-from-source).

     1. Clone the repository:
            
            git clone https://github.com/GoogleCloudPlatform/prometheus &&
            cd prometheus
            

     2. Check out the desired version tag:
            
            git checkout v2.53.5-gmp.1
            

     3. To create a Managed Service for Prometheus tarball, run the following commands:
            
            make build && make tarball
            

The resulting tarball and binaries are fully compatible with their upstream variants in terms of directory structure and functionality.

### Limits on creating and updating metrics and labels

Managed Service for Prometheus enforces a per-minute rate limit on creating new metrics and on adding new metric labels to existing metrics. This rate limit is usually only hit when first integrating with Managed Service for Prometheus, for example when you migrate an existing, mature Prometheus deployment to use self-deployed collection. **This is not a rate limit on ingesting data points**. This rate limit only applies when creating never-before-seen metrics or when adding new labels to existing metrics.

This quota is fixed, but any issues should automatically resolve as new metrics and metric labels get created up to the per-minute limit.

For more information, see [Troubleshooting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#descriptor_limits).

### Run self-deployed collection outside of Google Cloud

In Compute Engine environments, GKE environments, or on a machine where you ran `gcloud login` with a sufficiently authorized account, you can run self-deployed collection without further configuration. Outside of Google Cloud, you need to explicitly provide credentials, a `project_id` to contain your metrics, and a `location` (Google Cloud region) to store your metrics in. You should also set the `cluster` and `namespace` labels, even if running in a non-Kubernetes environment.

You can provide a service account key by using the `--export.credentials-file` flag or the `GOOGLE_APPLICATION_CREDENTIALS` environment variable as described in Provide credentials explicitly.

We recommend choosing `project_id` based on your planned tenancy model for reads. Pick a project to store metrics in based on how you plan to organize reads later with [metrics scopes](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#scoping-intro). If you don't care, you can put everything into one project.

For `location`, we recommend choosing the nearest Google Cloud region to your deployment. The further the chosen Google Cloud region is from your deployment, the more write latency you'll have and the more you'll be affected by potential networking issues. You might want to consult this [list of regions across multiple clouds](https://www.cloudinfrastructuremap.com/). If you don't care, you can put everything into one Google Cloud region. You can't use `global` as your location.

If running in a Kubernetes environment, set the `cluster` and `namespace` values to the local cluster and namespace. If running outside Kubernetes, set them to values that make sense hierarchically. For example, in a VM-based environment running on AWS, set the `cluster` value to `__aws__` and the `namespace` value to the instance ID. You can dynamically fill in the instance ID by using a relabeling rule that calls the local metadata server.

For a minimal working example, you can run a local, self-monitoring Prometheus binary with the following command:
    
    ./prometheus \
      --config.file=documentation/examples/prometheus.yaml \
      --export.label.project-id=PROJECT_ID \
      --export.label.location=REGION \
      --export.label.cluster=CLUSTER_NAME \
    

This example assumes you have set the `REGION` variable to a value like `us-central1`, for example.

However, we recommend that you set the `export` target labels for the managed service in the `global.external_labels` section of your Prometheus config. For example, in Kubernetes environments you might use the following config:
    
    global:
      external_labels:
        project_id: PROJECT_ID
        location: REGION
        cluster: CLUSTER_NAME
        namespace: local-testing
    
    scrape_configs:
      ...
    

Running Managed Service for Prometheus outside of Google Cloud incurs data transfer fees. There are fees to transfer data into Google Cloud, and you might incur fees to transfer data out of another cloud. You can minimize this cost by enabling compression with the `--export.compression=gzip` flag.

## What's next

     * [Use PromQL in Cloud Monitoring to query Prometheus metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-cm).
     * [Use Grafana to query Prometheus metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query).
     * Use [PromQL alerts in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting).
     * Set up [managed rule evaluation](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).
     * Set up [self-deployed rule evaluation](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-unmanaged).
     * Reduce cardinality and cost by [configuring local aggregations](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls#local-aggregation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
