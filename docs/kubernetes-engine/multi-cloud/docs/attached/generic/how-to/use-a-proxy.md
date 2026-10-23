---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/use-a-proxy/
title: Proxy support for CNCF conformant attached clusters \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:52.552883+00:00
---

# Proxy support for CNCF conformant attached clusters  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/use-a-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/concepts/overview)



Send feedback 

#  Proxy support for CNCF conformant attached clusters Stay organized with collections  Save and categorize content based on your preferences. 

If your organization uses an HTTP proxy for internet traffic, you need to configure GKE attached clusters accordingly. This document describes how to perform this configuration.

## Before you begin

GKE attached clusters requires connectivity to various Google Cloud services. Make sure your proxy server allows traffic to the following domains:

  * `.gcr.io`
  * `cloudresourcemanager.googleapis.com`
  * `container.googleapis.com`
  * `gkeconnect.googleapis.com`
  * `gkehub.googleapis.com`
  * `oauth2.googleapis.com`
  * `securetoken.googleapis.com`
  * `storage.googleapis.com`
  * `sts.googleapis.com`
  * `www.googleapis.com`
  * `servicecontrol.googleapis.com`
  * `logging.googleapis.com`
  * `monitoring.googleapis.com`
  * `opsconfigmonitoring.googleapis.com`
  * `GCP_LOCATION-gkemulticloud.googleapis.com`



Replace `GCP_LOCATION` with the Google Cloud region in which your cluster resides. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/reference/supported-regions).

## Configure proxy support for GKE attached clusters

To configure proxy support for GKE attached clusters, follow these steps:

  1. Create a proxy configuration file which contains values for `httpProxy`, `noProxy`, and `httpsProxy` keys:
         
         {
         "httpProxy": HTTP_PROXY_AUTHENTICATION_URL,
         "httpsProxy": HTTPS_PROXY_AUTH_URL,
         "noProxy": NO_PROXY_ADDRESSES
         }
         

Replace the following:

     * `HTTP_PROXY_AUTHENTICATION_URL`: the proxy server URL, which consists of a hostname/IP address, and optionally a port, username, and password. For example: `http://user:password@192.0.2.0:80` or just `198.51.100.255`.
     * `HTTPS_PROXY_AUTH_URL`: the proxy URL for encrypted HTTPS traffic, which consists of a hostname/IP address, and optionally a port, username, and password.
     * `NO_PROXY_ADDRESSES`: a comma-separated list of URLs, CIDR blocks, and DNS names of resources that can bypass the proxy. This directs GKE attached clusters to avoid using the proxy for the specified resources. Keep in mind the following: 
       * Values can be individual IP addresses, CIDR ranges, domain names, or even the asterix character (*). Using a single asterix (`*`) in the `noProxy` field tells GKE attached clusters to skip the proxy for all traffic.
       * A domain leading with a dot, such as `.google.com`, targets all its subdomains. For example, `.google.com` includes addresses such as `mail.google.com` and `drive.google.com`, but excludes `google.com`.
       * Ensure that you include `kubernetes.default.svc.cluster.local` and `kubernetes.default.svc` domains for proper logging. Here's an example: `198.51.100.0,192.0.2.0/16,examplepetstore.com,.altostrat.com,kubernetes.default.svc.cluster.local, kubernetes.default.svc`.

When creating the proxy configuration file, adhere to the following guidelines:

     * The `httpProxy` and `httpsProxy` fields don't accept `https://` prefixes. Use `http://`, even if the real proxy server address begins with `https://`. For example, represent `https://proxy.example.com:3128` as `http://proxy.example.com:3128`.
     * It's compulsory to provide values for all three fields: `httpProxy`, `httpsProxy`, and `noProxy`.
     * Consider appending additional domains, IP addresses, or CIDRs to the `noProxy` list. We recommend that you include the VPC IP range.
  2. Create a Kubernetes Secret, which contains the proxy configuration, by running the following command:
         
         kubectl create secret generic SECRET_NAME \
         --from-file=PROXY_CONFIGURATION_FILE
         

Replace the following:

     * `SECRET_NAME`: the name of the Kubernetes Secret
     * `PROXY_CONFIGURATION_FILE`: the path to the proxy configuration you created in step 1.
  3. Mark the Kubernetes Secret as [immutable](https://kubernetes.io/docs/concepts/configuration/secret/#secret-immutable) by setting its `immutable` field to `true`:
         
         kubectl edit secret SECRET_NAME
         

Replace `SECRET_NAME` with the name of the Kubernetes Secret.

  4. Configure a new or existing cluster to use the proxy:

###  New cluster

To register a new cluster and apply the proxy configuration, use the [`gcloud container attached clusters register` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register). Make sure to provide the optional arguments `--proxy-secret-name` and `--proxy-secret-namespace`:
         
         gcloud container attached clusters register CLUSTER_NAME \
           --proxy-secret-name=SECRET_NAME \
           --proxy-secret-namespace=SECRET_NAMESPACE
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster
     * `SECRET_NAME`: the name of the Kubernetes Secret containing the proxy configuration
     * `SECRET_NAMESPACE`: the Kubernetes namespace where the Secret is stored

For information about all the arguments you can use when registering a cluster, see the [`gcloud container attached clusters register` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register).

###  Existing cluster

To update a previously registered cluster with a new proxy configuration, use the [`gcloud container attached clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update). Make sure to provide the optional arguments `--proxy-secret-name` and `--proxy-secret-namespace`:
    
    gcloud container attached clusters update CLUSTER_NAME \
      --proxy-secret-name=SECRET_NAME \
      --proxy-secret-namespace=SECRET_NAMESPACE
    

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster
     * `SECRET_NAME`: the name of the Kubernetes Secret containing the proxy configuration
     * `SECRET_NAMESPACE`: the Kubernetes namespace where the Secret is stored

This step is required if your proxy server details have changed, or if an initial cluster registration overlooked proxy requirements.

For information about all the arguments you can use when updating a cluster, see the [`gcloud container attached clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update).




After performing these steps, GKE attached clusters processes outbound internet traffic using the proxy server specified in the configuration file.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
