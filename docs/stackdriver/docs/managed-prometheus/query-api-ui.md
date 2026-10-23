---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui/
title: Query using the Prometheus API or UI \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:37.717205+00:00
---

# Query using the Prometheus API or UI  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Query using the Prometheus API or UI Stay organized with collections  Save and categorize content based on your preferences. 

After you have deployed Google Cloud Managed Service for Prometheus, you can query the data sent to the managed service and display the results in charts and dashboards.

This document describes _metrics scopes_ , which determine the data you can query, and the following Prometheus-based ways to retrieve and use the data you've collected:

  * The Prometheus HTTP API
  * The Prometheus UI



All query interfaces for Managed Service for Prometheus are configured to retrieve data from Monarch using the Cloud Monitoring API. By querying Monarch instead of querying data from local Prometheus servers, you get global monitoring at scale.

## Before you begin

If you have not already deployed the managed service, then set up [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) or [self-deployed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged). You can skip this if you're only interested in [querying Cloud Monitoring metrics using PromQL](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql).

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

The following command grants the Google Cloud service account, `gmp-test-sa`, the Monitoring API roles it needs to read metric data.

If you have already granted the Google Cloud service account a specific role as part of prior task, then you don't need to do it again.

To authorize your service account to read from a multi-project metrics scope, follow these instructions and then see Change the queried project. 
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com \
      --role=roles/monitoring.viewer \
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

## Queries and metrics scopes

The data you can query is determined by the Cloud Monitoring construct _metrics scope_ , regardless of the method you use to query the data. For example, if you use Grafana to query Managed Service for Prometheus data, then each metrics scope must be configured as a separate data source.

A Monitoring metrics scope is a read-time-only construct that lets you query metric data belonging to multiple Google Cloud projects. Every metrics scope is hosted by a designated Google Cloud project, called the _scoping project_.

By default, a project is the scoping project for its own metrics scope, and the metrics scope contains the metrics and configuration for that project. A scoping project can have more than one monitored project in its metrics scope, and the metrics and configurations from all the monitored projects in the metrics scope are visible to the scoping project. A monitored project can also belong to more than one metrics scope.

When you query the metrics in a scoping project, and if that scoping project hosts a multi-project metrics scope, you can retrieve data from multiple projects. If your metrics scope contains all your projects, then your queries and rules evaluate globally.

For more information about scoping projects and metrics scope, see [Metrics scopes](https://docs.cloud.google.com/monitoring/settings#concept-scope). For information about configuring multi-project metrics scope, see [View metrics for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

## Managed Service for Prometheus data in Cloud Monitoring

The simplest way to verify that your Prometheus data is being exported is to use the Cloud Monitoring Metrics Explorer page in the Google Cloud console, which supports PromQL. For instructions, see [Querying using PromQL in Cloud Monitoring](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-cm#promql-monitoring).

## Standalone Prometheus frontend UI

You can use the standalone Prometheus frontend UI to access and visualize ingested data. This UI runs PromQL queries against all data in your Google Cloud project, as determined by the metrics scope associated with your project.

The frontend UI also acts as an authentication proxy for accessing ingested data. This feature can be used for client tools that don't support OAuth2 for service accounts, including Grafana or [horizontal pod autoscaling using the `prometheus-adapter` library](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/hpa#prometheus-adapter). 

We strongly recommend configuring Grafana to visualize data from Managed Service for Prometheus using the [data source syncer](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query). The instructions for configuring Grafana using the standalone Prometheus frontend UI are included here as reference for users who have previously configured Grafana using this method.

### Deploy the frontend UI

To deploy the standalone Prometheus frontend UI for Managed Service for Prometheus, run the following commands:

  1. Deploy the `frontend` service and configure it to query the [scoping project of your metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope) of your choice:
         
         curl https://raw.githubusercontent.com/GoogleCloudPlatform/prometheus-engine/e2cd07628f5bf3be5dc794ce8f4d4b9a206447ec/examples/frontend.yaml |
         sed 's/\$PROJECT_ID/PROJECT_ID/' |
         kubectl apply -n NAMESPACE_NAME -f -
         

  2. Port-forward the `frontend` service to your local machine. The following example forwards the service to port 9090:
         
         kubectl -n NAMESPACE_NAME port-forward svc/frontend 9090
         

This command does not return, and while it is running, it reports accesses to the URL.




If you want to continue using a Grafana deployment installed by kube-prometheus, then deploy the standalone Prometheus frontend UI in the `monitoring` namespace instead.

You can access the standalone Prometheus frontend UI in your browser at the URL `http://localhost:9090`. If you are using Cloud Shell for this step, you can get access by using the [Web Preview](https://docs.cloud.google.com/shell/docs/using-web-preview?previewing_the_application) button.

The following screenshot shows a table in the standalone Prometheus frontend UI that displays the `up` metric:

![Viewing a metric in the Prometheus interface.](https://docs.cloud.google.com/static/stackdriver/images/prometheus-ui.png)

You can also set up suitable authentication and authorization on the `frontend` service by using, for example, [Identity Aware Proxy](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto). For more information on exposing services, see [Exposing applications using services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps).

### Change the queried project to get multi-project monitoring

The `frontend` deployment uses the configured Google Cloud project as the scoping project. If this project is the scoping project of a [multi-project metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope), then it can read metrics from all projects in the metrics scope.

You can specify a project with a multi-project metrics scope by using the `--query.project-id` flag.

Typically, you use a dedicated project as a scoping project, and this project is not the same project the `frontend` deployment runs in. To let the deployment read a different target project, you must do the following:

  * Tell the `frontend` deployment which project is the target project.
  * Grant the service account permission to read the target project. If you have been using the Compute Engine `default` service account, you can do one of the following:

    * Enable Workload Identity Federation for GKE for your cluster and follow the configuration steps.

    * Provide an explicit service-account key.




To grant the permissions needed to access a different Google Cloud project, do the following:

  1. Grant the service account permission to read from the target project you want to query:
         
         gcloud projects add-iam-policy-binding SCOPING_PROJECT_ID \
           --member=serviceAccount:gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com \
           --role=roles/monitoring.viewer
         

  2. Open the `frontend` deployment created previously for editing:
         
         kubectl -n NAMESPACE_NAME edit deploy frontend
         

  3. Specify the target project by using the `--query.project-id` flag:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           namespace: NAMESPACE_NAME
           name: frontend
         spec:
           template
             containers:
             - name: frontend
               args:
               **- --query.project-id= SCOPING_PROJECT_ID**
         ...
         

Save the file and close the editor. After the change is applied, the frontend pods are restarted and query the new scoping project.




### Authenticate the frontend UI

The `frontend` deployment supports [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) for authenticated access in versions 0.5.0 and above. To enable authentication, add the `AUTH_USERNAME` and `AUTH_PASSWORD` environment variables to the deployment: 
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      namespace: NAMESPACE_NAME
      name: frontend
    spec:
      template
        containers:
        - name: frontend
          **env:
          - name: AUTH_USERNAME
            value: USERNAME
          - name: AUTH_PASSWORD
            value: PASSWORD**
    ...
    

### Provide credentials explicitly

**You can skip this section if you are running the`frontend` container in a Google Kubernetes Engine cluster.** If you are having authentication issues on GKE, see Verify service account credentials.

When running on GKE, the frontend automatically retrieves credentials from the environment based on the node's service account or the Workload Identity Federation for GKE setup. In non-GKE Kubernetes clusters, credentials must be explicitly provided to the frontend by using flags or the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.

  1. Set the context to your target project:
         
         gcloud config set project PROJECT_ID
         

  2. Create a service account:
         
         gcloud iam service-accounts create gmp-test-sa
         

This step creates the service account that you might have already created in the Workload Identity Federation for GKE instructions. 

  3. Grant the required permissions to the service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=serviceAccount:gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com \
           --role=roles/monitoring.viewer
         

  4. Create and download a key for the service account:
         
         gcloud iam service-accounts keys create gmp-test-sa-key.json \
           --iam-account=gmp-test-sa@PROJECT_ID.iam.gserviceaccount.com
         

  5. Add the key file as a secret to your non-GKE cluster:
         
         kubectl -n NAMESPACE_NAME create secret generic gmp-test-sa \
           --from-file=key.json=gmp-test-sa-key.json
         

  6. Open the frontend Deployment resource for editing:
         
         kubectl -n NAMESPACE_NAME edit deploy frontend
         

     1. Add the text shown in bold to the resource:
            
            apiVersion: apps/v1
            kind: Deployment
            metadata:
              namespace: NAMESPACE_NAME
              name: frontend
            spec:
              template
                containers:
                - name: frontend
                  args:
                  **- --query.credentials-file=/gmp/key.json**
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

## Using Grafana through the Frontend Proxy

Managed Service for Prometheus uses the built-in Prometheus data source for Grafana, meaning that you can keep using any community-created or personal Grafana dashboards without any changes. You can also [import your Grafana dashboards into Cloud Monitoring](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/import-grafana-dashboards).

### Authenticating to Google Cloud APIs

**Warning:** We strongly recommend configuring Grafana to visualize data from Managed Service for Prometheus using the [data source syncer](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query). These instructions for configuring Grafana using the standalone Prometheus frontend UI are included here as reference for users who have previously configured Grafana using this method.

Google Cloud APIs all require authentication using OAuth2; however, Grafana doesn't support OAuth2 authentication for service accounts used with Prometheus data sources. To use Grafana with Managed Service for Prometheus, you can use the standalone Prometheus frontend UI as an authentication proxy.

**You must point Grafana at the standalone frontend UI proxy to query data globally.** If you do not follow these steps, then Grafana only executes queries against data in the local Prometheus server.

If you have not already deployed the Prometheus UI `frontend` service as a proxy, deploy it now by running the following command:
    
    curl https://raw.githubusercontent.com/GoogleCloudPlatform/prometheus-engine/v0.17.2/examples/frontend.yaml |
    sed 's/\$PROJECT_ID/PROJECT_ID/' |
    kubectl apply -n NAMESPACE_NAME -f -
    

For non-GKE Kubernetes clusters such as Anthos clusters, also see Provide credentials explicitly to give the `frontend` service the permissions needed to query metrics.

See change the queried project for instructions on configuring the [metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope) used by the `frontend` service to query across multiple projects.

If you have a pre-existing Grafana deployment, such as one installed by the `kube-prometheus` library or one installed using a helm chart, you can continue using it with Managed Service for Prometheus. If so, see Configure a data source for next steps. Otherwise, you must first deploy Grafana.

### Deploy Grafana

If you don't have a running Grafana deployment in your cluster, then you can create an ephemeral test deployment to experiment with.

To create an ephemeral Grafana deployment, apply the Managed Service for Prometheus `grafana.yaml` manifest to your cluster, and port-forward the `grafana` service to your local machine. The following example forwards the service to port 3000.

     1. Apply the `grafana.yaml` manifest:
            
            kubectl -n NAMESPACE_NAME apply -f  https://raw.githubusercontent.com/GoogleCloudPlatform/prometheus-engine/beb779d32f4dd531a3faad9f2916617b8d9baefd/examples/grafana.yaml
            

     2. Port-forward the `grafana` service to your local machine. This example forwards the service to port 3000:
            
            kubectl -n NAMESPACE_NAME port-forward svc/grafana 3000
            

This command does not return, and while it is running, it reports accesses to the URL.

You can access Grafana in your browser at the URL `http://localhost:3000` with the username:password `admin:admin`.

### Configure a data source

To query Managed Service for Prometheus in Grafana by using the Prometheus UI as the authentication proxy, you must add a new data source to Grafana. To add a data source for the managed service, do the following:

     1. Go to your Grafana deployment, for example, by browsing to the URL `http://localhost:3000` to reach the Grafana welcome page.

     2. Select **Configuration** from the main Grafana menu, then select **Data Sources**.

![Adding a data source in Grafana.](https://docs.cloud.google.com/static/stackdriver/images/grafana-welcome.png)

     3. Select **Add data source** , and select Prometheus as the time series database.

![Adding a Prometheus data source.](https://docs.cloud.google.com/static/stackdriver/images/grafana-add-datasource.png)

     4. In the **URL** field of the **HTTP** pane, enter the URL of the Managed Service for Prometheus `frontend` service. If you configured the Prometheus frontend UI to run on port 9090, then the service URL for this field is `http://frontend.NAMESPACE_NAME.svc:9090`.

In the **Timeout** field of the **HTTP** pane, set the value to `120`.

If you configured the frontend UI proxy with Basic auth, enable the **Basic auth** switch in the **Auth** pane and fill out the username and password.

In the **Query timeout** field, set the value to `2m`.

In the **HTTP Method** field, select `GET`.

In the **Prometheus type** field, select `Prometheus`.

In the **Prometheus version** field, select `2.40.x` or higher.

If you have multiple Prometheus data sources, then you might give this one a name like "Managed Prometheus Service". You can leave other fields with their default values.

![Configuring a Managed Service for Prometheus data source.](https://docs.cloud.google.com/static/stackdriver/images/grafana-data-source.png)

     5. Click **Save & Test**, and look for the message "The data source is working".

![Testing your Managed Service for Prometheus data source.](https://docs.cloud.google.com/static/stackdriver/images/grafana-test-and-save.png)

**Note:** You can also deploy the `frontend` container as a sidecar in the Grafana pod, and that data source can access it at the URL `http://localhost:9090`.

### Use the new data source

You can now create Grafana dashboards using the new data source. You can also redirect existing dashboards to the new data source. The following screenshot shows a Grafana chart that displays the `up` metric:

![Grafana chart for the Managed Service for Prometheus up metric.](https://docs.cloud.google.com/static/stackdriver/images/grafana-chart.png)

## Connecting Managed Service for Prometheus to Thanos

You can federate Managed Service for Prometheus to a self-deployed [Thanos](https://thanos.io) stack by using the open-source [thanos-promql-connector](https://github.com/thanos-community/thanos-promql-connector). Google Cloud does not provide support for this integration.

## Prometheus HTTP API

Managed Service for Prometheus supports the upstream [Prometheus HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/) at the URL prefixed by `https://monitoring.googleapis.com/v1/projects/PROJECT_ID/location/global/prometheus/api/v1/`. For information about the supported endpoints, see API compatibility.

This API can be accessed by any tool that can interact with a standard Prometheus server. This is an API endpoint only; it doesn't serve a UI. As a Google Cloud API, the API uses OAuth2 authentication, and as part of the Cloud Monitoring API, the value of the `PROJECT_ID` is the scoping project of a metrics scope, so you can retrieve data from any project in the metrics scope. For more information about scoping, see [Metrics scopes](https://docs.cloud.google.com/monitoring/settings#concept-scope).

To use this endpoint, provide a [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) expression. For example, the following instant query retrieves all time series that have the metric name `up`:
    
    curl https://monitoring.googleapis.com/v1/projects/PROJECT_ID/location/global/prometheus/api/v1/query \
      -d "query=up" \
      -H "Authorization: Bearer $(gcloud auth print-access-token)"
    

If the request is successful, then the query returns a result like the following, which has been formatted for readability:
    
    {
      "status":"success",
      "data":{
        "resultType":"vector",
        "result":[{
          "metric": {
            "__name__":"up",
            "cluster":"gmp-test",
            "instance":"prom-example-84c6f547f5-g4ljn:web",
            "job":"prometheus",
            "location":"us-central1-a",
            "project_id":"a-gcp-project"
          },
          "value": [1634873239.971,"1"]
        }]
      }
    }
    

For information about querying [Google Cloud system metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp) using PromQL, see [PromQL for Cloud Monitoring metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql).

## API compatibility

The following [Prometheus HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/) endpoints are supported by Managed Service for Prometheus under the URL prefixed by `https://monitoring.googleapis.com/v1/projects/PROJECT_ID/location/global/prometheus/api/v1/`.

For full documentation, see the [Cloud Monitoring API reference documentation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1). The Promethus HTTP endpoints aren't available in the Cloud Monitoring language-specific client libraries.

For information about PromQL compatibility, see [PromQL support](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql-differences).

     * The following endpoints are fully supported:

       * [`/api/v1/query`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/query)
       * [`/api/v1/query_range`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/query_range)
       * [`/api/v1/metadata`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1.metadata/list)
       * [`/api/v1/labels`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/labels)
       * [`/api/v1/query_exemplars`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/query_exemplars)
     * The [`/api/v1/label/<label_name>/values`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1.label/values) endpoint only works if the `__name__` label is provided either by using it as the `<label_name>` value or by exactly matching on it using a series selector. For example, the following calls are fully supported:

       * `/api/v1/label/__name__/values`
       * `/api/v1/label/__name__/values?match[]={__name__=~".*metricname.*"}`
       * `/api/v1/label/labelname/values?match[]={__name__="metricname"}`

This limitation causes `label_values($label)` variable queries in Grafana to fail. Instead, you can use `label_values($metric, $label)`. This type of query is recommended because it avoids fetching values for labels on metrics that are not relevant to the given dashboard.

     * The [`/api/v1/series`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/series) endpoint is supported for `GET` but not `POST` requests. When you use the [data source syncer](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#grafana-oauth) or [frontend proxy](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui#ui-prometheus), this restriction is managed for you. You can also configure your Prometheus data sources in Grafana to issue only `GET` requests. The `match[]` parameter does not support regular expression matching on the `__name__` label.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
