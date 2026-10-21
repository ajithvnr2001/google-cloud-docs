---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protecting-cluster-metadata/
title: Protecting cluster metadata \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:26:12.885622+00:00
---

# Protecting cluster metadata  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protecting-cluster-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Protecting cluster metadata Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) uses [instance metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) to configure node virtual machines (VMs), but some of this metadata is potentially sensitive and should be protected from workloads running on the cluster.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Configure node service account

Each node's service account credentials continue to be exposed to workloads. By default, your nodes use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). You should configure a **minimally-privileged service account** for your nodes to use instead of the Compute Engine default service account. Then, attach this service account to your nodes, so that an attacker cannot circumvent GKE metadata protections by using the Compute Engine API to access the underlying VM instances directly.

For more information, refer to [Use least privilege node service accounts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

**Caution:** Do not use a service account that has `compute.instances.get` permission, the Compute Instance Admin role, or other similar permissions, as they allow potential attackers to obtain instance metadata using the Compute Engine API. Restrict the permissions of a node VM by using service account permissions, _not access scopes_. For more information, see [Migrating from legacy access scopes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes#service_account).

To create a minimally privileged node service account, perform the following steps:

  1. Create a new Identity and Access Management (IAM) service account and save the email address in an environment variable:
         
         gcloud iam service-accounts create NODE_SA_NAME \
             --display-name="DISPLAY_NAME"
         export NODE_SA_EMAIL=$(gcloud iam service-accounts list --format='value(email)' \
             --filter='displayName:DISPLAY_NAME')
         

Replace the following:

     * `NODE_SA_NAME`: the name of your new node service account.
     * `DISPLAY_NAME`: the display name of the new service account.

The node service account email address has the format `NODE_SA_NAME@PROJECT_ID.iam.gserviceaccount.com`.

  2. Configure your service account with the minimum roles and permissions to run your GKE nodes:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:$NODE_SA_EMAIL \
             --role=roles/monitoring.metricWriter
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:$NODE_SA_EMAIL \
             --role=roles/monitoring.viewer
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:$NODE_SA_EMAIL \
             --role=roles/logging.logWriter
         

Replace `PROJECT_ID` with your Google Cloud project ID.

Additionally, if your cluster pulls private images from [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/access-control), add the `roles/artifactregistry.reader` role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:$NODE_SA_EMAIL \
             --role=roles/artifactregistry.reader
         




## Metadata concealment

**Warning:** [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) replaces the need to use metadata concealment and the two approaches are incompatible. We recommend that you use Workload Identity Federation for GKE instead of metadata concealment.

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

GKE _metadata concealment_ prevents user Pods from accessing `kube-env`, which contains kubelet credentials, and the VM's [instance identity token](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity).

Metadata concealment firewalls traffic from user Pods (Pods _not_ running on `HostNetwork`) to the cluster metadata server, only allowing safe queries. The firewall prevents user Pods from using kubelet credentials for privilege escalation attacks, or from using VM identity for instance escalation attacks.

Workload Identity Federation for GKE replaces the need to use metadata concealment and expands on the protections that metadata concealment offers. You should use Workload Identity Federation for GKE instead of metadata concealment in all situations. To learn more, see [About Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity).

To enable metadata concealment, use the deprecated `--workload-metadata=SECURE` option in your [`gcloud beta container clusters create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/create#--workload-metadata) or in your [`gcloud beta container node-pools create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/node-pools/create#--workload-metadata).

### Limitations

Metadata concealment has limitations such as the following:

  * Metadata concealment only protects access to `kube-env` and the node's instance identity token.
  * Metadata concealment does not restrict access to the node's [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts).
  * Metadata concealment does not restrict access to other related instance metadata.
  * Metadata concealment does not restrict access to other legacy metadata APIs.
  * Metadata concealment doesn't restrict traffic from Pods running on the host network (`hostNetwork: true` in the Pod specification).



## Disabling and transitioning from legacy metadata APIs

The `v0.1` and `v1beta1` Compute Engine metadata server endpoints were deprecated and shutdown on **September 30, 2020**.

For the shutdown schedule, refer to [`v0.1` and `v1beta1` metadata server endpoints deprecation](https://docs.cloud.google.com/compute/docs/deprecations/v0.1-v1beta1-metadata-server).

## What's next

  * Learn how to [authenticate to Google Cloud APIs from GKE workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).
  * Learn more about [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity).
  * Learn more about [troubleshooting GKE authentication issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/authentication).
  * Learn how to [harden your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
