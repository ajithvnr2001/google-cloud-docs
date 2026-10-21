---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/about-kubeconfig/
title: About Kubeconfig \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:15:07.045067+00:00
---

# About Kubeconfig  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/about-kubeconfig/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  About Kubeconfig Stay organized with collections  Save and categorize content based on your preferences. 

This page is for IT administrators and Operators who want to set up, monitor, and manage cloud infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Kubernetes configuration file

Kubernetes uses a YAML file called [`kubeconfig`](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) to store cluster authentication information for `kubectl`. `kubeconfig` contains a list of contexts to which `kubectl` refers when running commands. By default, the file is saved at `$HOME/.kube/config`.

A _context_ is a group of access parameters. Each context contains a Kubernetes cluster, a user, and a namespace. The _current context_ is the cluster that is currently the default for `kubectl`: all `kubectl` commands run against that cluster.

After you create a cluster, follow [Generate a `kubeconfig` entry](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-cluster-access-for-kubectl#generate_kubeconfig_entry) to add the context of the cluster to your local `kubeconfig`.

## Private endpoints

All clusters have a canonical endpoint. The endpoint exposes the Kubernetes API server that `kubectl` and other services use to communicate with your cluster control plane over TCP port 443. On AWS, this endpoint is a DNS name that is only resolvable inside the cluster— for example `gke-abcdefghijk-cp-ffabcdef123456.elb.us-west-1.amazonaws.com`. This endpoint is not accessible on the public internet. You can get the private cluster endpoint address from the `endpoint` field in the output of the [`gcloud container aws clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/describe) command.

### Connect gateway endpoint

By default, the `gcloud container aws clusters get-credentials` command generates a `kubeconfig` that uses [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway). With this `kubeconfig`, `kubectl` uses Connect, which then securely forwards the traffic to the private endpoint on your behalf. When you use Connect gateway, the endpoint looks like `https://connectgateway.googleapis.com/v1/projects/PROJECT_NUMBER/memberships/CLUSTER_NAME`, where PROJECT_NUMBER is your project number and CLUSTER_NAME is your cluster name.

If you have access to your cluster's private endpoint through your VPC, you can connect directly to the private endpoint. To generate a `kubeconfig` using the private endpoint, use the [`gcloud container aws clusters get-credentials --private-endpoint`](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-cluster-access-for-kubectl#private-endpoint) command.

## About authentication for `kubectl`

All GKE on AWS are configured to accept Google Cloud user and service account identities, by validating the credentials presented by `kubectl` and retrieving the email address associated with the user or service account identity. As a result, the credentials for those accounts must include the `userinfo.email` OAuth scope in order to successfully authenticate.

When you use `gcloud` to set up your environment's `kubeconfig` for a new or existing cluster, `gcloud` gives `kubectl` the same credentials used by `gcloud` itself. For example, if you use `gcloud auth login`, your personal credentials are provided to `kubectl`, including the `userinfo.email` scope. This allows the GKE on AWS to authenticate the `kubectl` client.

Once users or Google Cloud service accounts are authenticated, they must also be _authorized_ to perform any action on a GKE on AWS. The cluster admin is responsible for setting up the appropriate [Role-Based Access Control](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) to configure authorization.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
