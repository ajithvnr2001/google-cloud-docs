---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/auth-plugin/
title: Deprecated authentication plugin for Kubernetes clients \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:00.043881+00:00
---

# Deprecated authentication plugin for Kubernetes clients  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/auth-plugin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deprecated authentication plugin for Kubernetes clients Stay organized with collections  Save and categorize content based on your preferences. 

In Kubernetes version 1.22, the Kubernetes project deprecated the built-in authentication mechanism used by clients such as the `kubectl` command-line tool to access the Kubernetes API server. The built-in authentication mechanism is scheduled for removal in Kubernetes 1.26. For context, refer to [GitHub PR 102181](https://github.com/kubernetes/kubernetes/pull/102181).

The removal doesn't affect operators that are deployed in the cluster and use Kubernetes service accounts to communicate with the API server.

## What should you do?

GKE released an updated authentication plugin, `gke-gcloud-auth-plugin`. This plugin uses the [client-go Credential Plugins](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins) framework to provide authentication tokens to communicate with GKE clusters.

You must install the plugin before you update your command-line clients to version 1.26 and later. If you don't install the plugin, you'll notice an error message similar to the following.

For instructions, refer to [Install required plugins](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin).

### Example error: No auth provider found
    
    
    Unable to connect to the server: getting credentials: exec: executable gke-gcloud-auth-plugin not found
    
    panic: no Auth Provider found for name gcp
    

### Example error: Executable gke-gcloud-auth-plugin not found
    
    
    Unable to connect to the server: getting credentials: exec: executable gke-gcloud-auth-plugin not found
    
    It looks like you are trying to use a client-go credential plugin that is not installed.
    
    To learn more about this feature, consult the documentation available at:
          https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins
    
    Install gke-gcloud-auth-plugin for use with kubectl by following \
    https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
