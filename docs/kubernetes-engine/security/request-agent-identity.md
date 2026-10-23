---
url: https://docs.cloud.google.com/kubernetes-engine/security/request-agent-identity/
title: Request an agent identity for a GKE agent \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:37.069962+00:00
---

# Request an agent identity for a GKE agent  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/security/request-agent-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Request an agent identity for a GKE agent Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Agent Identity for GKE**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Agent workloads that you deploy on Google Kubernetes Engine (GKE) clusters often need to access external tools and services, either as the agent's own identity or on behalf of end users. Security administrators and platform administrators also want to know what deployed agents do across Google Cloud services. This document shows you how to configure authentication for agent workloads by requesting an _Agent Identity_ for your Pods. This agent identity lets you configure authentication without having to manually manage credentials for different workflows, and integrates your GKE agents with Gemini Enterprise Agent Platform. This document is intended for application developers who build and run agent workloads on GKE clusters.

You should already be familiar with the following topics:

  * [About Agent Identity for GKE](https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity)
  * [Declarative management of Kubernetes objects](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/#overview)



## Pricing

Agent Identity is provided at no additional cost in GKE.

## Limitations

  * You can automatically register only Deployments in Agent Registry. Other workload controllers and static Pods don't support automatic registration. Although you can request agent identities for all workload types, registration in Agent Registry lets you integrate those identities with Agent Platform.
  * Bound agent identity access tokens use only the `https://www.googleapis.com/auth/cloud-platform` OAuth scope. You can't specify a different scope for the bound access tokens.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable the Agent Registry API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        
        gcloud services enable agentregistry.googleapis.com

  * Verify that you have an existing Autopilot cluster or a Standard cluster that has [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled and runs GKE version 1.37.0-gke.3503000 or later.

  * Verify that you have enough quota for token exchange operations. This quota has the name **Exchange Workload Identity Token Requests per minute per region**. For more information, see [Quotas and limits](https://docs.cloud.google.com/kubernetes-engine/quotas).




### Required roles

To get the permissions that you need to request an agent identity and deploy workloads, ask your administrator to grant you the [Kubernetes Engine Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer) (`roles/container.developer`) IAM role on your Google Cloud project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Request an agent identity for a workload

To get an agent identity for Pods, you add annotations to your Pod specification to request a SPIFFE ID for the workload and to inject the X.509 certificate bundle into each Pod. For Pods that are managed by Deployments, you should also add an annotation and a label to register the agent in Agent Registry. Although registration is optional, only registered agents can use Agent Platform services like Agent Gateway. For more information about the specific annotations and labels, see [Workload-level configuration](https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity#workload-configuration).

The following steps show you how to create an example Deployment that requests agent identities:

  1. Find your organization ID. If your project isn't in an organization, then skip this step and [find your project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) instead.
         
         gcloud projects get-ancestors PROJECT_ID
         

Replace `PROJECT_ID` with the cluster project ID.

The output is similar to the following:
         
         ID: my-project
         TYPE: project
         ID: 811159889184
         TYPE: folder
         ID: 301928500920
         TYPE: organization
         

Make a note of the value in the `ID` field for the `organization` resource.

  2. Connect to your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster's control plane.
  3. Create a namespace to run the example Deployment:
         
         kubectl create namespace NAMESPACE_NAME
         

Replace `NAMESPACE_NAME` with a name for the namespace.

  4. Create a Kubernetes ServiceAccount for the Deployment:
         
         kubectl create serviceaccount SERVICEACCOUNT_NAME \
             --namespace=NAMESPACE_NAME
         

Replace `SERVICEACCOUNT_NAME` with a name for the ServiceAccount.

  5. Save the following Deployment manifest as `agent-identity-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: agent-identity-deployment
           namespace: NAMESPACE_NAME
           **# Add the agent to Agent Registry
           labels:
             registry.gke.io/functional-type: "AGENT"
           annotations:
             # A2A protocol metadata annotation for automated Agent Card discovery
             a2a-protocol.org/agent-card: |
               card:
                 endpoint: /.well-known/agent-card.json
                 protocol: HTTP
                 port: 8080**
         spec:
           replicas: 2
           selector:
             matchLabels:
               workload-type: agent
           template:
             metadata:
               name: agent-identity-pod
               **annotations :
                 iam.gke.io/identity: "spiffe://TRUST_DOMAIN/*" # The trust domain from which to assign SPIFFE IDs.
                 iam.gke.io/inject-podcertificates: "true" # Inject X.509 certificates and per-Pod private key into each Pod.
                 iam.gke.io/spiffe-identity-type: "agent-identity" # Required for Agent Registry registration.**
               labels:
                 workload-type: agent
             spec:
               serviceAccountName: SERVICEACCOUNT_NAME
               containers:
               - name: agent
                 image: python:3.11-slim
                 command: ["sleep","infinity"]
         

Replace `TRUST_DOMAIN` with the trust domain that issues identities for agents in your project. This value must use one of the following syntaxes, depending on whether your project is in an organization:

     * **Projects that are in an organization** : `agents.global.org-ORGANIZATION_ID.system.id.goog`, where `ORGANIZATION_ID` is the ID of the organization.
     * **Projects that aren't in an organization** : `agents.global.proj-PROJECT_NUMBER.system.id.goog`, where `PROJECT_NUMBER` is the project number of the cluster project.

This Deployment requests an agent identity for the workload, adds the per-Pod X.509 certificates to the Pods, and registers the agent in Agent Registry.

  6. Create the Deployment:
         
         kubectl apply -f agent-identity-deployment.yaml
         

  7. Verify that the Pods are running:
         
         kubectl get pods -l workload-type=agent -n NAMESPACE_NAME
         




## Check the assigned agent identity

After you deploy a workload that requests an agent identity, you can verify the identity by checking the X.509 certificates. If you disable certificate injection, then you can get an unbound identity token from the GKE metadata server to check the subject field, as described in [Authenticate to Google Cloud APIs](https://docs.cloud.google.com/kubernetes-engine/security/authenticate-agent-identity#authenticate-google-cloud-apis).

To read the X.509 certificate in a Pod, follow these steps:

  1. Check whether a Pod has access to the X.509 certificate and private key:
         
         kubectl get pod POD_NAME -n NAMESPACE_NAME \
             -o=jsonpath='{range .spec.volumes[*]}{.name}{"\n"}{end}'
         

Replace `POD_NAME` with the name of a Pod that uses Agent Identity.

The output is similar to the following:
         
         kube-api-access-bx86g
         gke-workload-spiffe-credentials
         

In this output, the `gke-workload-spiffe-credentials` volume is the location of the injected certificates. If you don't see this volume, then verify that the `iam.gke.io/inject-podcertificates` annotation is set to a value of `true` in the Pod specification.

  2. Create an interactive shell session in the Pod:
         
         kubectl exec -n NAMESPACE_NAME -it POD_NAME -- /bin/bash
         

  3. In the shell session, list the credentials in the `gke-workload-spiffe-credentials` volume:
         
         ls -1 /var/run/secrets/workload-spiffe-credentials/
         

The output is similar to the following:
         
         x509.credential-bundle.private-key.pem
         TRUST_DOMAIN.spiffe-trust-bundle.pem
         

The output displays the following files:

     * `x509.credential-bundle.private-key.pem`: the agent identity credential bundle, which includes the X.509 certificate chain and a private key that's unique to the Pod. This credential bundle is used to request access tokens and ID tokens and to authenticate to Google Cloud APIs by using mTLS.
     * `TRUST_DOMAIN.spiffe-trust-bundle.pem`: the root CA trust bundle, which contains the self-signed certificates that form the trust anchor for the agent identity credentials. This trust bundle is primarily used to validate TLS certificates from other workloads during mTLS handshakes.
  4. To get the SPIFFE ID that's associated with the Pod, read the X.509 certificate:
         
         openssl x509 -in /var/run/secrets/workload-spiffe-credentials/x509.credential-bundle.private-key.pem -text -noout
         

The output is similar to the following:
         
         Certificate:
             Data:
             # Multiple lines are omitted here
                 X509v3 extensions:
                     # Multiple lines are omitted here
                     **X509v3 Subject Alternative Name: critical
                         URI:spiffe://agents.global.org-301928500920.system.id.goog/resources/container/projects/729788050015/locations/us-central1/clusters/cluster-2/ns/agent-identity-ns/sa/agent-identity-sa**
             # Multiple lines are omitted here
         

In this output, the value that's in the `URI` field for the `X509v3 Subject Alternative Name` field is the SPIFFE ID of the agent.




If your agent Pod has an assigned SPIFFE ID, then your request for an agent identity is successful. You can use the assigned identity to authenticate to various tools and services.

## What's next

  * [Authenticate by using an agent identity in GKE](https://docs.cloud.google.com/kubernetes-engine/security/authenticate-agent-identity)
  * [Set up tracing for agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/tracing)
  * [Set up logging for agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/logging)
  * [Set up monitoring for agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/monitoring)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
