---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/anthos-identity-service/
title: Manage identity with GKE Identity Service \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:58.582642+00:00
---

# Manage identity with GKE Identity Service  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/anthos-identity-service/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Manage identity with GKE Identity Service Stay organized with collections  Save and categorize content based on your preferences. 

GKE on AWS supports [OpenID Connect (OIDC)](https://openid.net/connect/) and [AWS IAM](https://aws.amazon.com/iam/) as an authentication mechanism for interacting with a cluster's Kubernetes API server, using GKE Identity Service. GKE Identity Service is an authentication service that lets you bring your existing identity solutions for authentication to multiple environments. Users can log in to and use your GKE clusters from the command line or from the Google Cloud console, all using your existing identity provider.

For an overview of how GKE Identity Service works, see [Introducing GKE Identity Service](https://docs.cloud.google.com/anthos/identity).

If you already use or want to use Google identities to log in to your GKE clusters, we recommend using the `gcloud containers aws clusters get-credentials` command for authentication. Find out more in [Connect and authenticate to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/connect-and-authenticate-to-your-cluster#google-identity).

## OpenID Connect authentication

### Before you begin

  1. To use OIDC authentication, users must be able to connect to the cluster's control plane. See [Connect to your cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/connect-and-authenticate-to-your-cluster#connect-to-vpn).

  2. To authenticate through the Google Cloud console, you must [register each cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) that you want to configure with your project fleet. For GKE on AWS, this is automatic once you have created a node pool.

  3. To allow users to authenticate through the Google Cloud console, ensure that all clusters you want to configure are [registered with your project fleet](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster). For GKE on AWS, this is automatic once you have created a node pool.




### Setup process and options

  1. Register GKE Identity Service as a client with your OIDC provider following the instructions in [Configuring providers for GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/provider).

  2. Choose from the following cluster configuration options:

     * Configure your clusters at the fleet-level following the instructions in [Configuring clusters for fleet-level GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/fleet-cluster). With this option, your authentication configuration is centrally managed by Google Cloud.

     * Configure your clusters individually following the instructions in [Configuring clusters for GKE Identity Service with OIDC](https://docs.cloud.google.com/anthos/identity/setup/per-cluster).

  3. Set up user access to your clusters, including role-based access control (RBAC), following the instructions in [Setting up user access for GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/user-access).




### Accessing clusters

After GKE Identity Service has been set up on a cluster, users can log in to clusters using either the command line or the Google Cloud console.

  * Learn how to log in to registered clusters with your OIDC ID in [Accessing clusters using GKE Identity Service](https://docs.cloud.google.com/anthos/identity/accessing).
  * Learn how to log in to clusters from the Google Cloud console in [Logging in to a cluster from the Google Cloud console](https://docs.cloud.google.com/anthos/multicluster-management/console/logging-in).



## AWS IAM authentication

The AWS IAM support on GKE on AWS uses [GKE Identity Service](https://docs.cloud.google.com/anthos/identity).

### Before you begin

To use AWS IAM authentication, users must be able to connect to the cluster's control plane. See [Connect to your cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/connect-and-authenticate-to-your-cluster#connect-to-vpn).

### Setup process and options

To configure your cluster to allow AWS IAM authentication for a particular AWS region, do the following:

  1. Edit the `ClientConfig` resource on your cluster:
         
         kubectl --kubeconfig=KUBECONFIG_PATH edit ClientConfigs default -n kube-public
         

Replace `KUBECONFIG_PATH` with the path to your cluster's kubeconfig file—for example `$HOME/.kube/config`.

Your text editor loads your cluster's ClientConfig resource. Add the `spec.authentication.aws` object as shown below. Do not modify any default data that has already been written.
         
         apiVersion: authentication.gke.io/v2alpha1
         kind: ClientConfig
         metadata:
           name: default
           namespace: kube-public
         spec:
           authentication:
           - name: NAME
             aws:
               region: AWS_REGION
         

Replace the following:

     * `NAME`: an arbitrary name of this authentication method. e.g. "aws-iam".
     * `AWS_REGION`: the AWS region where the user info is retrieved. It needs to match the region configured on your users' AWS CLI.
  2. To enable your cluster users to use AWS IAM, follow [Setting up user access for GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/user-access).




### Accessing clusters

After GKE Identity Service has been set up on a cluster, users can log in to clusters using either the command line or the Google Cloud console.

To learn how to log in to registered clusters with your AWS IAM identity, see [Accessing clusters using GKE Identity Service](https://docs.cloud.google.com/anthos/identity/accessing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
