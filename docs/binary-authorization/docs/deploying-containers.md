---
url: https://docs.cloud.google.com/binary-authorization/docs/deploying-containers/
title: Deploy containers (GKE, Distributed Cloud) \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:12.215956+00:00
---

# Deploy containers (GKE, Distributed Cloud)  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/deploying-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Deploy containers (GKE, Distributed Cloud) Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to deploy a container image to a GKE cluster (on Google Cloud or Google Distributed Cloud) where Binary Authorization is enabled. The `kubectl` commands you use to deploy the image are the same as the ones you use to deploy images to clusters that don't use Binary Authorization.

## Before you begin

Make sure you have the Binary Authorization API enabled in your project and a GKE cluster with Binary Authorization enabled. See [setting up on Google Kubernetes Engine](https://docs.cloud.google.com/binary-authorization/docs/setting-up) or [setting up on Distributed Cloud](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem).

Install [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl) for interacting with GKE.

## Configure `kubectl`

You must update the local `kubeconfig` file for your `kubectl` installation. This provides the credentials and endpoint information required to access the cluster in GKE or Distributed Cloud.

To configure `kubectl`, run the following `gcloud` command:

###  GKE 
    
    
    gcloud container clusters get-credentials \
        --zone ZONE \
        CLUSTER_NAME
    

Replace the following:

  * ZONE: the name of the GKE zone where the cluster is running, for example, `us-central1-a`
  * CLUSTER_NAME: the name of the cluster



###  Distributed Cloud 
    
    
    gcloud container fleet memberships get-credentials \
        --location LOCATION \
        MEMBERSHIP_NAME
    

Replace the following:

  * LOCATION: the location of the fleet membership of the GKE cluster, for example, `global`
  * MEMBERSHIP_NAME: the name of the fleet membership of the GKE cluster



## Deploy the container image

Deploy your container image as follows:

  1. Configure environment variables:
         
         POD_NAME=POD_NAME
         IMAGE_PATH=IMAGE_PATH
         IMAGE_DIGEST=IMAGE_DIGEST
         

Replace the following:

     * POD_NAME: the name you want to use for the GKE workload
     * IMAGE_PATH: path of the image in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs), or another registry.
     * IMAGE_DIGEST: the digest of the image manifest. Example is as follows:

       * Artifact Registry: 
         * Path: `us-docker.pkg.dev/google-samples/containers/gke/hello-app`
         * Digest: `sha256:37e5287945774f27b418ce567cd77f4bbc9ef44a1bcd1a2312369f31f9cce567`

To learn how to get the digest of an image in Artifact Registry, see [Managing images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#gcloud).

  2. Deploy your image using the `kubectl run` command.

You must deploy the image using the digest rather than a tag like `1.0` or `latest`, as Binary Authorization uses the digest to look up [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations).

To deploy the image, run the following `kubectl` command:
         
         kubectl run ${POD_NAME} \
             --image ${IMAGE_PATH}@${IMAGE_DIGEST}
         

Now, verify that the deployment was blocked by Binary Authorization:
         
         kubectl get pods
         

You see your Pod listed.




## Fail open

If GKE is unable to reach the Binary Authorization server for any reason, or if the server returns an error, GKE cannot determine whether Binary Authorization would allow or deny the image. In this case, GKE fails open: it defaults to allowing the image to be deployed, but creates a log entry in Cloud Audit Logs to record why the image was allowed.

GKE enforcement fails open because of a tradeoff between reliability and security. GKE sends a request to the Binary Authorization whenever a Pod is created or updated. This includes scenarios where Pods are automatically created or updated by higher level Kubernetes workload controllers, like ReplicaSets and StatefulSets. If GKE failed closed instead of open, any Binary Authorization outage would stop these Pods from running. Moreover, when Pods are denied, failover can lead to cascading failures as redirected traffic overloads Pods that are still running. Any Binary Authorization outage could trigger a complete outage for your cluster, even without deploying any new images.

**Note:** Operations that send enough requests to Binary Authorization to exceed the per-project, per-user, per-minute [quota](https://docs.cloud.google.com/binary-authorization/quotas) will trigger fail open. For example, testing whether Binary Authorization denies an image by trying to rapidly deploy that image repeatedly will cause the image to be allowed when the quota is exceeded. It is possible to [request additional quota](https://docs.cloud.google.com/binary-authorization/quotas#quota_increases), if needed.

## Deploy images that violate the policy

Binary Authorization supports a feature known as _breakglass_ that allows an image to be deployed, even if it violates the policy.

For more information, see [Using breakglass](https://docs.cloud.google.com/binary-authorization/docs/using-breakglass)

## Clean up

To clean up, delete the Pod by executing the following command:
    
    
      kubectl delete pod ${POD_NAME}
      

## What's next

  * Learn about [dry-run mode](https://docs.cloud.google.com/binary-authorization/docs/enabling-dry-run).
  * Learn how to [use CV](https://docs.cloud.google.com/binary-authorization/docs/overview-cv).
  * Learn how to [use legacy continuous validation](https://docs.cloud.google.com/binary-authorization/docs/using-cv) ([deprecated](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy)).
  * Learn how to [use image digests in Kubernetes manifests](https://docs.cloud.google.com/architecture/using-container-image-digests-in-kubernetes-manifests).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
