---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/common-error-messages/
title: Google Distributed Cloud common error messages \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:52.730141+00:00
---

# Google Distributed Cloud common error messages  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/common-error-messages/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Google Distributed Cloud common error messages Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/common-error-messages)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/common-error-messages)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



Here is a list of common errors you may encounter during Google Distributed Cloud installation. See [Known issues](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) for more information on other errors or limitations you might encounter with Google Distributed Cloud.

The installation process for Google Distributed Cloud is a continuous reconciliation loop. As a result, you might see transient error messages in the log during installation.

As long as the installation completes successfully, these errors can be safely ignored. The following is a list of typical transient error log messages:
    
    
      Internal error occurred: failed calling webhook "webhook.cert-manager.io": Post
      https://cert-manager-webhook.cert-manager.svc:443/mutate?timeout=10s:
      dial tcp IP_ADDRESS:443: connect: connection refused
    
    
    
      Internal error occurred: failed calling webhook "vcluster.kb.io": Post
      https://webhook-service.kube-system.svc:443/validate-baremetal-cluster-gke-io-v1-cluster?timeout=30s:
      dial tcp IP_ADDRESS:443: connect: connection refused
    
    
    
      Failed to register cluster with GKE Hub; gcloud output: error running command
      'gcloud container fleet memberships register CLUSTER_NAME  --verbosity=error --quiet':
      error: exit status 1, stderr: 'ERROR: (gcloud.container.hub.memberships.register)
      Failed to check if the user is a cluster-admin: Unable to connect to the server: EOF
    
    
    
      Get
      https://127.0.0.1:34483/apis/infrastructure.baremetal.cluster.gke.io/v1/namespaces/cluster-
      cluster1/baremetalmachines: dial tcp 127.0.0.1:34483: connect: connection refused"
    
    
    
      Create Kind Cluster "msg"="apply run failed" "error"="unable to recognize \"/tmp/kout088683152\": no matches for kind \"NetworkLogging\" in version \"networking.gke.io/v1alpha1\""
      Create Kind Cluster "msg"="apply run failed" "error"="unable to recognize \"/tmp/kout869681888\": no matches for kind \"Provider\" in version \"clusterctl.cluster.x-k8s.io/v1alpha3\""
    

If your Google Cloud service account key has expired, you will see the following error messages from `bmctl`:
    
    
    Error validating cluster config: 3 errors occurred:
            * GKEConnect check failed: Get https://gkehub.googleapis.com/v1beta1/projects/project/locations/global/memberships/admin: oauth2: cannot fetch token: 400 Bad Request
    Response: {"error":"invalid_grant","error_description":"Invalid JWT Signature."}
            * ClusterOperations check failed: Post https://cloudresourcemanager.googleapis.com/v1/projects/project:testIamPermissions?alt=json&prettyPrint=false: oauth2: cannot fetch token: 400 Bad Request
    Response: {"error":"invalid_grant","error_description":"Invalid JWT Signature."}
            * GCR pull permission for bucket: artifacts.anthos-baremetal-release.appspot.com failed: Get https://storage.googleapis.com/storage/v1/b/artifacts.anthos-baremetal-release.appspot.com/iam/testPermissions?alt=json&permissions=storage.objects.get&permissions=storage.objects.list&prettyPrint=false: oauth2: cannot fetch token: 400 Bad Request
    Response: {"error":"invalid_grant","error_description":"Invalid JWT Signature."}
    

You will need to generate a [new service account key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
