---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/workload-identity/
title: Using Workload Identity Federation for GKE \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:01.642955+00:00
---

# Using Workload Identity Federation for GKE  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/workload-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Using Workload Identity Federation for GKE Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to authenticate your Knative serving services with [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to access [Google Cloud APIs](https://docs.cloud.google.com/apis) such as the Compute APIs, Storage and Database APIs, or Machine Learning APIs.

To authenticate your Knative serving services, you must:

  1. Enable Workload Identity Federation for GKE in your cluster
  2. Create a [Kubernetes Service Account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) and grant it the required IAM roles



After following these steps, you can deploy a new Knative serving service that uses the identity that you created.

## Enabling Workload Identity Federation for GKE on your cluster

To set up Workload Identity Federation for GKE with Knative serving, you can set up [fleet Workload Identity Federation](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity) instead of using a Google Cloud Service Account JSON file.

## Configure permissions to enable all metrics

To enable metrics, like reporting request count or request latency to Google Cloud Observability, you need to grant write permissions for Cloud Monitoring. For example, you can grant the [Monitoring Metric Writer role](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) (`roles/monitoring.metricWriter`) to the Kubernetes Service Account that is associated with Knative serving because it includes the necessary permissions for writing monitoring data.

## Granting IAM roles to a Kubernetes Service Account

Any Knative serving service running as the Kubernetes Service Account that you configure automatically authenticates with its federated identity when accessing Google Cloud APIs. The Kubernetes Service Account must exist within the cluster and namespace of the Knative serving service for which you want to use Workload Identity Federation for GKE.

  1. If a Kubernetes Service Account doesn't exist, create one in the same Kubernetes namespace as your Knative serving service; otherwise, skip to the next step:
         
         kubectl create serviceaccount --namespace K8S_NAMESPACE KUBERNETES_SERVICEACCOUNT

  2. Grant the required [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) directly to your Kubernetes Service Account:
         
         gcloud projects add-iam-policy-binding RESOURCE_PROJECT_ID \
             --member "principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/K8S_NAMESPACE/sa/KUBERNETES_SERVICEACCOUNT" \
             --role "ROLE_NAME" \
             --condition=None

Replace:

     * RESOURCE_PROJECT_ID with the Google Cloud project ID where the target Google Cloud resources reside.
     * PROJECT_NUMBER with the project number of the Google Cloud project for the cluster where your Kubernetes Service Account and Knative serving services reside.
     * PROJECT_ID with the ID of the Google Cloud project for the cluster where your Kubernetes Service Account and Knative serving services reside.
     * K8S_NAMESPACE and KUBERNETES_SERVICEACCOUNT with the namespace and name of your Kubernetes Service Account.
     * ROLE_NAME with the IAM role to assign to your Kubernetes Service Account, such as `roles/monitoring.metricWriter`.



## Deploying a new service to use Workload Identity Federation for GKE

Deploy a new Knative serving service that uses the Workload Identity Federation for GKE you created.

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click **Create Service** if you are configuring a new service you are deploying to. If you are configuring an existing service, click on the service, then click **Edit & Deploy New Revision**.

  3. Under _Advanced settings_ , click **Container**.

  4. Click the **Service account** dropdown and select the desired service account.

  5. Click **Next** to continue to the next section.

  6. In the **Configure how this service is triggered** section, select which connectivity you would like to use to invoke the service.

  7. Click **Create** to deploy the image to Knative serving and wait for the deployment to finish.




### Command line

  * For existing services, set the Kubernetes Service Account by running the [`gcloud run services update`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) command with the following parameters:
        
        gcloud run services update SERVICE --service-account KUBERNETES_SERVICEACCOUNT

Replace:

    * SERVICE with the name of your Knative serving service.
    * KUBERNETES_SERVICEACCOUNT with the Kubernetes Service Account that you used to create the workload identity.
  * For new services, set the Kubernetes Service Account by running the `gcloud run deploy` command with the [`--service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--service-account) parameter:
        
        gcloud run deploy --image IMAGE_URL --service-account KUBERNETES_SERVICEACCOUNT

Replace:

    * IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.
    * KUBERNETES_SERVICEACCOUNT with the Kubernetes Service Account that you used to create the workload identity.



### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

  2. In your local file, update the `serviceAccountName:` attribute:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             spec:
               serviceAccountName: KUBERNETES_SERVICEACCOUNT

Replace

     * SERVICE with the name of your Knative serving service.
     * KUBERNETES_SERVICEACCOUNT with the Kubernetes Service Account that you used to create the workload identity.
  3. Deploy the configuration to your Knative serving service by running the following command:
         
         gcloud run services replace service.yaml




## Migrating existing services to use Workload Identity Federation for GKE

If you enabled Workload Identity Federation for GKE on an existing cluster, each service on that cluster for which you want to use Workload Identity Federation for GKE must be migrated. [Learn how to migrate existing services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#migrate_applications_to).

## Next steps

Learn how to [manage access](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/managing-access) to your services.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
