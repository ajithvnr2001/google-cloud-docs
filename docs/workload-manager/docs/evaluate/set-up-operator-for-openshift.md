---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-operator-for-openshift/
title: Set up the Cluster Services for OpenShift Telemetry operator \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:32.178973+00:00
---

# Set up the Cluster Services for OpenShift Telemetry operator  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-operator-for-openshift/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Set up the Cluster Services for OpenShift Telemetry operator Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to install the [Cluster Services for OpenShift Telemetry operator](https://docs.cloud.google.com/openshift-cluster/automate-cluster-config-validation#about-cso-telemetry-operator) and configure it to connect with an OpenShift cluster that runs on a Compute Engine instance.

After you install and configure it, this telemetry operator deploys a host-network telemetry daemon that continuously monitors cluster health and cluster configuration. The operator sends the collected metrics to Workload Manager. You can then use [Workload Manager evaluation](https://docs.cloud.google.com/workload-manager/docs/about-evaluations) to scan the workloads that run in your cluster for deviations from best practices for OpenShift clusters.

## Before you begin

Before you install and configure the telemetry operator, you need to make sure that the following prerequisites are met:

  * You're using version 4.18 or later of the Red Hat OpenShift Container Platform.
  * You've deployed an OpenShift cluster on one or more compute instances.
  * Your administrator has granted you the **ClusterAdmin** role for your cluster in the Red Hat OpenShift Container Platform.
  * You've [downloaded and installed the Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud#download_and_install_the) in your terminal. If you're using [Cloud Shell](https://docs.cloud.google.com/shell/docs), then you can skip this prerequisite.
  * You've installed the OpenShift CLI (`oc`) in your cluster. For information about how to install this CLI, see the Red Hat document [Installing the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_tools/openshift-cli-oc#installing-openshift-cli).
  * You've installed the Cloud Credentials Operator (`ccoctl`) utility. For information about how to install this utility, see the Red Hat document [How to obtain the `ccoctl` tool for OpenShift 4](https://access.redhat.com/solutions/7001811).
  * You've reviewed the [supported regions](https://docs.cloud.google.com/workload-manager/docs/evaluate/locations) where you can create Workload Manager evaluations.
  * Your administrator has granted you [IAM roles required to create and run Workload Manager evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles).
  * You've enabled access to Cloud APIs.



### Enable access to Cloud APIs

Compute Engine recommends configuring your instances to allow all access scopes to all Cloud APIs and using only the IAM permissions of the instance service account to control access to Google Cloud resources. For more information, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

If you limit access to the Cloud APIs, then the Cluster Services for OpenShift Telemetry operator requires at minimum the following Cloud APIs access scopes on the host compute instance:
    
    
    https://www.googleapis.com/auth/cloud-platform
    

For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice).

If you're running an OpenShift cluster on a compute instance that doesn't have an external IP address, then you need to enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on the instance's subnet so that the Cluster Services for OpenShift Telemetry operator can access the Google APIs and services. For information about how to enable Private Google Access, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access). 

## Authenticate users to OpenShift cluster

To perform administrative actions, you or your users need to be authenticated to your OpenShift cluster by using the OpenShift CLI. To authenticate users to your OpenShift cluster, you can choose from the following options:

  * Run the following command and follow the prompts:
        
        oc login "https://api.CLUSTER_DOMAIN:6443" -u kubeadmin
        

  * Alternatively, get a session authentication token for use with the `oc` binary. To get this token, open the following URL in a web browser:
        
        https://oauth-openshift.apps.CLUSTER_DOMAIN/oauth/token/request
        




Replace `CLUSTER_DOMAIN` with the domain of your OpenShift cluster. For example: `mycluster.google.com`.

## Authenticate the operator to Google Cloud

To let the telemetry operator authenticate itself and access Google Cloud resources, you must create a service account for it in your Google Cloud project.

You can authenticate the telemetry operator as the service account by using the following options:

  * (Recommended) Authenticate by using Workload Identity Federation
  * Authenticate by using a service account key



### Authenticate operator by using Workload Identity Federation

To authenticate the telemetry operator as the service account by using Workload Identity Federation, complete the following steps:

  1. In your terminal, extract the `CredentialsRequest` manifest from the telemetry operator bundle into a local directory:
         
         mkdir -p credrequests
         oc image extract us-docker.pkg.dev/workload-agent-products/cluster-services-for-openshift-telemetry/bundle:VERSION --path /manifests/:./credrequests --confirm
         

Replace `VERSION` with the version number that you subscribed for the telemetry operator in the OperatorHub. You can see the list of certified version numbers for the telemetry operator in the Red Hat Ecosystem Catalog.

  2. By using the `ccoctl` utility, process the extracted `CredentialsRequest` manifest and provision Google Cloud Identity and Access Management (IAM) bindings and credentials:
         
         ccoctl gcp create-all \
           --name=cso-telemetry \
           --region=REGION \
           --project=PROJECT_ID \
           --credentials-requests-dir=./credrequests \
           --output-dir=./ccoctl-out
         

Replace the following:

     * `REGION`: the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones) where your OpenShift cluster runs
     * `PROJECT_ID`: the project ID of the Google Cloud project where your OpenShift cluster runs
  3. Apply the generated OpenID Connect (OIDC) provider, IAM roles, and secret manifests to the cluster:
         
         oc apply -f ./ccoctl-out/manifests/
         




The preceding steps create a service account in your Google Cloud project and assign the following IAM roles to it:

  * To collect metrics from the compute instance: [Compute Viewer (`roles/compute.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer)
  * To write data to Workload Manager data warehouse: [Workload Manager Insights Writer (`roles/workloadmanager.insightWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter)
  * To send operator logs to Cloud Logging: [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter)



### Authenticate operator by using a service account key

If your organization doesn't support using Workload Identity Federation for authentication purposes, then you can authenticate the telemetry operator by using a service account key.

To authenticate the telemetry operator as the service account by using a service account key, complete the following steps:

  1. In your terminal, extract the `CredentialsRequest` manifest from the telemetry operator bundle into a local directory:
         
         mkdir -p credrequests
         oc image extract us-docker.pkg.dev/workload-agent-products/cluster-services-for-openshift-telemetry/bundle:VERSION --path /manifests/:./credrequests --confirm
         

  2. In your Google Cloud project, create a service account for the telemetry operator:
         
         gcloud iam service-accounts create cso-telemetry-agent \
           --description="Service account for OpenShift Telemetry Operator" \
           --display-name="CSO Telemetry Agent" \
           --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the Google Cloud project where your OpenShift cluster runs.

  3. To let the service account access Google Cloud resources, grant the service account the IAM roles defined in the `CredentialsRequest` manifest. This manifest includes the following minimum set of IAM roles that the operator needs:

     * To collect metrics from the compute instance: [Compute Viewer (`roles/compute.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer)
     * To write data to Workload Manager data warehouse: [Workload Manager Insights Writer (`roles/workloadmanager.insightWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter)
     * To send operator logs to Cloud Logging: [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter)

For each IAM role defined in this manifest, run the following command:
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="serviceAccount:cso-telemetry-agent@PROJECT_ID.iam.gserviceaccount.com" \
      --role="IAM_ROLE"
    

Replace `IAM_ROLE` with the IAM role that you want to grant to the service account.

  4. Create and download a private key for the service account:
         
         gcloud iam service-accounts keys create ./sa_key.json \
           --iam-account=cso-telemetry-agent@PROJECT_ID.iam.gserviceaccount.com \
           --project=PROJECT_ID
         

  5. In the `openshift-operators` namespace, create a secret named `telemetry-agent-sa` for the service account key that you created:
         
         oc create secret generic telemetry-agent-sa \
           --from-file=workload_agent_sa_key.json=./sa_key.json \
           -n openshift-operators
         




## Install the Cluster Services for OpenShift Telemetry operator

You can install the Cluster Services for OpenShift Telemetry operator either by using the Red Hat OpenShift Container Platform web console or the declarative subscription YAML manifests. For information about these options, see the Red Hat document [Adding Operators to a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html/operators/administrator-tasks#olm-adding-operators-to-a-cluster).

###  OpenShift web console 

To install the telemetry operator in your OpenShift cluster by using the OpenShift Container Platform web console, complete the following steps:

  1. Sign in to the Red Hat OpenShift web console.
  2. Verify that you're in the **Administrator** perspective.
  3. In the left navigation, expand the **Operators** section and click **OperatorHub**.
  4. In the search bar under **All items** , enter **Cluster Services for OpenShift Telemetry**.

Alternatively, you can search by entering **Google**. This filters the operators provided by Google, which includes the Cluster Services for OpenShift Telemetry operator.

  5. Click the card named **Cluster Services for OpenShift Telemetry**.

  6. In the **Cluster Services for OpenShift Telemetry** pane, click **Install**.

  7. In the **Install Operator** page, complete the following steps:

     1. In the **Update channel** field, select **stable**.
     2. In the **Installation mode** field, select **A specific namespace on the cluster**.
     3. In the **Installed Namespace** field, select the **openshift-operators** project or create a custom monitoring namespace.
     4. In the **Approval Strategy** field, select **Automatic** or **Manual**.
     5. Click **Install**.
  8. To verify that the operator is successfully installed, complete the following steps:

     1. Go to **Operators > Installed Operators**.
     2. In the list of operators, search and verify that the **Cluster Services for OpenShift Telemetry** operator is present.
     3. Verify that the **Status** column shows the value **Succeeded** or **Up to date**.
     4. Optionally, click the operator to view its details.



###  OpenShift CLI 

To install the telemetry operator in your OpenShift cluster by using the OpenShift CLI and a declarative `Subscription` YAML manifest, complete the following steps:

  1. Create a `Subscription` custom resource manifest named `subscription.yaml` with the following configuration:
         
         apiVersion: operators.coreos.com/v1alpha1
         kind: Subscription
         metadata:
           name: google-cloud-cluster-services-for-openshift-telemetry
           namespace: openshift-operators
         spec:
           channel: stable
           installPlanApproval: Automatic
           name: google-cloud-cluster-services-for-openshift-telemetry
           source: certified-operators
           sourceNamespace: openshift-marketplace
         

  2. Apply the subscription to your cluster:
         
         oc apply -f subscription.yaml
         

  3. Verify that the telemetry operator is successfully installed by checking the status of `ClusterServiceVersion`:
         
         oc get csv -n openshift-operators
         

In the output, verify that the value in the **`PHASE`** column for `cluster-services-for-openshift-telemetry` is **`Succeeded`**.




## Enable metrics collection

To enable the operator to collect metrics from your OpenShift cluster, you must apply a `TelemetryConfig` custom resource. This resource deploys daemon pods on your cluster nodes for the Agent for Compute Workloads.

To enable the operator to collect metrics from your OpenShift cluster, complete the following steps:

  1. Create a `TelemetryConfig` custom resource manifest named `telemetryconfig.yaml`:

     * If you've set up authentication for the telemetry operator by using Workload Identity Federation, then use the following minimum custom resource. This custom resource automatically fetches the credentials stored in the `google-cloud-cluster-services-telemetry-agent-wif-secret` secret.
           
           apiVersion: cluster-services-openshift.cloud.google.com/v1alpha1
           kind: TelemetryConfig
           metadata:
             name: telemetryconfig
             namespace: openshift-operators
           spec:
             enabled: true
           

     * If you've set up authentication for the telemetry operator by using a service account key, then use the following custom resource:
           
           apiVersion: cluster-services-openshift.cloud.google.com/v1alpha1
           kind: TelemetryConfig
           metadata:
             name: telemetryconfig
             namespace: openshift-operators
           spec:
             enabled: true
             serviceAccountCredentialsSecretName: telemetry-agent-sa
             serviceAccountCredentialsPath: SERVICE_ACCOUNT_KEY_PATH
           

Replace `SERVICE_ACCOUNT_KEY_PATH` with the path where you mounted the service account key. The name of the mount must match the service account key JSON file. For example: `/var/run/secrets/google/workload_agent_sa_key.json`.

  2. Apply the custom resource to your cluster:
         
         oc apply -f telemetryconfig.yaml
         

  3. Verify that the state of the telemetry agent pod is **Running** :
         
         oc get pods -n openshift-operators -l app.kubernetes.io/name=workloadagent-operator
         

You can also verify metrics collection by inspecting the logs of the pod:
         
         "openshiftmetrics/openshiftmetrics.go:126","msg":"Metric payload after collection","pid":5,"context":"OpenShiftMetricCollection","payload":"version:\"v0.1.0-pre\" agent_version:\"1.3\"




## View operator logs in Cloud Logging

By default, logs from the Cluster Services for OpenShift Telemetry operator are sent to Cloud Logging. You can view these logs in Logging. To view the operator logs in Logging, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the query pane, enter a query:

     * To filter the logs for your Google Cloud project, use the following query:
           
           logName="projects/PROJECT_ID/logs/google-cloud-workload-agent"

Replace `PROJECT_ID` with the project ID of the Google Cloud project where your OpenShift cluster runs.

     * If you're running multiple clusters in your Google Cloud project and want to filter logs from a specific cluster, then use the following query:
           
           resource.labels.instance_id=("COMPUTE_INSTANCE_ID_1" OR "COMPUTE_INSTANCE_ID_2" OR "COMPUTE_INSTANCE_ID_3")

Replace `COMPUTE_INSTANCE_ID` with the **Instance ID** of the Compute Engine instances that run your OpenShift cluster. For information about how to find your compute instance ID, see [View the details of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details).

  3. Click **Run query**.




### Set up log-based alerting policies

By default, logs from the telemetry operator are sent to Cloud Logging. We recommend that you configure alerting policies based on the telemetry operator logs, which notify you when specific messages appear in the logs. These alerts help you monitor the operator's functioning and troubleshoot issues.

To configure an alerting policy based on the logs generated by the telemetry operator, complete the following steps:

  1. Verify that you've met the prerequisites described in the "Before you begin" section of [Configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

  2. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  3. In the query pane, enter the required query:
         
         logName="projects/PROJECT_ID/logs/google-cloud-workload-agent"
         severity=SEVERITY_LEVEL

Replace `SEVERITY_LEVEL` with a supported severity level value, which includes: `DEBUG`, `INFO`, `WARNING`, and `ERROR`. We recommend that you use `ERROR` or a higher log level value.

  4. Click **Run query** to validate the query.

  5. Create a log alert.

To learn how to create this alert, see step three in the procedure that's described in [Create a log-based alerting policy by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition).




## Optional: Enable production-specific evaluations

Of the best practices that Workload Manager supports for OpenShift clusters, some are applied only to production environments. Workload Manager makes this distinction by checking your cluster, deployment, or pod for the label `environment`. If the value associated with this label is `production`, then Workload Manager considers that resource as a production resource.

To inform Workload Manager that a cluster belongs to a production environment, complete the following steps:

  1. Create a `workloadmanager` namespace:
         
         oc create namespace workloadmanager
         

  2. Create a `ConfigMap` in the `workloadmanager` namespace by using the following configuration:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: wlm-cluster-environment
           namespace: workloadmanager
         data:
           # Options: "production" or "non-production"
           environment: "production"
         




To inform Workload Manager that a deployment or pod belongs to a production environment, add a label named `environment` to the resource definition by using one of the following options:

  * Manually apply the following configuration:
        
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: my-app
          labels:
            # Options: "production" or "non-production"
            environment: "production"
        spec:
        ...
        

  * Run the following command:
        
        oc label --overwrite deployments DEPLOYMENT_NAME environment=production
        

Replace `DEPLOYMENT_NAME` with the name of your deployment.




If you apply the `environment` label on your OpenShift cluster as well as a deployment or pod that runs on the cluster, then Workload Manager gives precedence to the label value set for the deployment or pod over the label value set for the cluster.

## Optional: Trigger metrics collection

After you successfully set up the Cluster Services for OpenShift Telemetry operator in your OpenShift cluster, the operator collects metrics from the cluster and sends them to Workload Manager every 30 minutes.

Optionally, instead of waiting 30 minutes for the scheduled collection of metrics, you can manually trigger the operator to collect metrics and send them to Workload Manager.

To manually trigger the operator for metrics collection, complete the following steps:

  1. Open your terminal.

  2. Find the name of the running pod:
         
         POD_NAME=$(oc get pods -l app.kubernetes.io/name=workloadagent-operator --field-selector=status.phase=Running -o=name)
         

  3. Trigger the operator to collect and send metrics:
         
         oc debug -t $POD_NAME -- /openshift-docker-entrypoint.sh
         




## What's next

  * [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation)
  * Learn about the [Workload Manager best practices for OpenShift](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general#openshift-cost-optimization)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
