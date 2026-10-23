---
url: https://docs.cloud.google.com/run/docs/migrate/from-kubernetes/
title: Migrate from Kubernetes to Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:37.673427+00:00
---

# Migrate from Kubernetes to Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/migrate/from-kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Migrate from Kubernetes to Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run and Kubernetes both use standard container images as deployment artifacts, they both use a declarative API model with resources that can be represented in YAML files with the same standard structure.

## Introduction

The [Cloud Run Admin API v1](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.services) is designed to maximize portability with Kubernetes, for example, the Cloud Run Admin API resources share the same structure conventions and attribute names as Kubernetes resources. See the [Cloud Run service YAML reference](https://docs.cloud.google.com/run/docs/reference/yaml/v1#service).

The Cloud Run Admin API v1 implements the [Knative Serving API specification](https://github.com/knative/specs/blob/main/specs/serving/knative-api-specification-1.0.md), but you do **not** need to be using Knative in your existing Kubernetes cluster in order to migrate some of your Kubernetes workloads to Cloud Run.

The primary resource of Cloud Run is the [service](https://docs.cloud.google.com/run/docs/resource-model). You can think of a Cloud Run service as a high level abstraction that looks like a Kubernetes [deployment](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/) with a built-in pod autoscaler and unique endpoint. A "Pod" in Kubernetes corresponds to an "instance" in Cloud Run. We recommend transforming your Kubernetes deployments into Cloud Run services, one service at a time. You will also be able to merge some configuration of your Kubernetes [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) and Kubernetes [services](https://kubernetes.io/docs/concepts/services-networking/service/) into the Cloud Run service.

Cloud Run does not have the concept of namespace, instead the Google Cloud project is used as an isolation boundary between resources. When migrating to Cloud Run from Kubernetes, we recommend creating one Google Cloud project for each namespace. In the [YAML of a Cloud Run service](https://docs.cloud.google.com/run/docs/reference/yaml/v1), the namespace value is the Google Cloud project number.

Cloud Run has a [built-in zonal redundancy](https://docs.cloud.google.com/architecture/disaster-recovery#cloud-run), this means that you do not need to provision replica to ensure your service is resilient to a zonal outage in the selected Google Cloud region.

## Quickstart

This quickstart is an example of a simple migration example.

### Simple resource comparison

Compare the following simple Kubernetes [deployment](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/) named `my-app` with the equivalent Cloud Run service. Note how the YAML files are almost identical.

The parts in `blue` are different and need to be changed. The parts in `red` should be deleted because Cloud Run has a built-in autoscaler.

Kubernetes deployment| Cloud Run service  
---|---  
      
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
      namespace: default
      labels:
        app: my-app
    spec:
      template:
        metadata:
          labels:
            app: my-app
        spec:
          containers:
          - image: gcr.io/cloudrun/hello
            env:
            - name: HELLO
              value: world
      replicas: 3
      selector:
        matchLabels:
          app: my-app
    

| 
    
    
    apiVersion: serving.knative.dev/v1
    kind: Service
    metadata:
      name: my-app
      namespace: 'PROJECT_NUMBER'
      labels:
        app: my-app
    spec:
      template:
        metadata:
          labels:
            app: my-app
        spec:
          containers:
          - image: gcr.io/cloudrun/hello
            env:
            - name: HELLO
              value: world
      
  
### Migrate a simple Kubernetes deployment to Cloud Run

  1. Download the YAML file of your deployment in the current directory with:
         
         kubectl get deployment  my-app -o yaml > my-app.yaml

  2. Modify the YAML to match a Cloud Run service. Update the `my-app.yaml` file:

     * For the "`kind`" attribute: replace the value "`Deployment`" with "`Service`"
     * For the "`apiVersion`" attribute: replace the value "`apps/v1`" with "`serving.knative.dev/v1`"
     * Delete the `metadata.namespace` attribute or change its value to match your Google Cloud project number.
     * Delete `spec.replicas` and `spec.selector`
  3. Deploy the `my-app.yaml` file to Cloud Run using the following command, replacing REGION with the desired Google Cloud region, for example `europe-west1`:
         
         gcloud run services replace my-app.yaml --region REGION




Invoking a Cloud Run service is protected by an IAM permission. If you want to expose the new Cloud Run service publicly to the internet and allow public access, run the following command:
    
    
    gcloud run services add-iam-policy-binding my-app --member="allUsers" --role="roles/run.invoker" --region REGION

## Features not supported by Cloud Run

Only workloads that are a [fit for Cloud Run](https://docs.cloud.google.com/run/docs/fit-for-run) can be migrated.

Notably, the following Kubernetes features are not supported by Cloud Run:

  * Fixed numbers of `replicas` (a workaround is to use the same number of [minimum](https://docs.cloud.google.com/run/docs/configuring/min-instances#yaml) and [maximum](https://docs.cloud.google.com/run/docs/configuring/max-instances#yaml) instances
  * Config Maps (workaround available)
  * Custom horizontal Pod autoscaler strategies
  * Service Discovery
  * Local Disk (Ephemeral and Persistent)



When migrating a YAML file from a Kubernetes deployment to a Cloud Run service, the `gcloud run services replace` command will return a clear error message for any attribute that is not supported by Cloud Run. Delete or update these attributes, then repeat the command until it succeeds.

You can refer to the [YAML Reference](https://docs.cloud.google.com/run/docs/reference/yaml/v1) for an exhaustive list of attributes support by Cloud Run.

## Migrate Kubernetes resources

### Migrate Kubernetes secrets

Like Kubernetes, Cloud Run supports mounting secrets as environment variables or volumes, but secrets should be stored in [Secret Manager](https://docs.cloud.google.com/secret-manager).

There are several important differences between Secret Manager secrets and Kubernetes secrets:

  * **Allowed characters in names** : 
    * [Kubernetes secrets](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names): `[a-z0-9-.]{1,253}`
    * Secret Manager secrets: `[a-zA-Z0-9_-]{1,255}`
  * **Versioning** : Secrets from Secret Manager are versioned, while Kubernetes secrets aren't.
  * **Payload** : Secrets from Secret Manager contain a single `[]byte`, while Kubernetes secrets contain a `map<string, string>`.



Follow the Secret Manager documentation to [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create) and [add a new secret version](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#add-secret-version) for every secret key your Kubernetes app depends on.

### Migrate Kubernetes ConfigMaps

Cloud Run does not have an equivalent of Kubernetes [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/), but because ConfigMaps can be seen as unencrypted Secrets, you can transform your ConfigMaps into secrets in Secret Manager instead. See instructions under Migrate Kubernetes secrets.

### Migrate a Kubernetes deployment

The Kubernetes deployment exposed by a service is the resource that maps the closest to a Cloud Run service. We recommend starting from the YAML of your Kubernetes deployment and editing it to transform it into a Cloud Run service.

The main required changes are:

  * The `namespace` must be replaced with the Google Cloud project number.
  * Labels (`metadata.labels` and `spec.template.metadata.labels`) must be [valid Google Cloud labels](https://docs.cloud.google.com/compute/docs/labeling-resources#requirements).
  * Containers must be stored in a [supported container registry](https://docs.cloud.google.com/run/docs/deploying#images).
  * [CPU](https://docs.cloud.google.com/run/docs/configuring/services/cpu) and [memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) limits might need to be adjusted.
  * When referencing a secret, the "`key`" attribute is used to capture the **version** in Secret Manager, with "`latest`" referencing the latest version of the secret.
  * `serviceAccountName` should reference a Service Account in the current Google Cloud project
  * References to ConfigMaps (`configMapKeyRef`) should be replaced with references to secrets (`secretKeyRef`)



If your Kubernetes deployment is accessing other resources in your Kubernetes cluster or resources on a VPC, you must [connect the Cloud Run service to the appropriate VPC](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc)

### Migrate a Kubernetes service

Cloud Run services automatically expose a unique endpoint that routes traffic to the container with a `containerPort`. After you have migrated your Kubernetes deployment to a Cloud Run service, you don't need to migrate the [Kubernetes services](https://kubernetes.io/docs/concepts/services-networking/service/) that was routing traffic to this deployment.

### Migrate a Kubernetes HorizontalPodAutoscaler

Cloud Run services have a built-in horizontal autoscaler: Cloud Run automatically scales pods (called "instances") using [a combination of factors](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) within the boundaries of its defined minimum and maximum number of instances.

Migrate the `minReplicas` and `maxReplicas` attributes of the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/) to the `autoscaling.knative.dev/minScale` and `autoscaling.knative.dev/maxScale` annotations of the Cloud Run service. Refer to the documentation on configuring [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances#yaml) and [maximum instances](https://docs.cloud.google.com/run/docs/configuring/max-instances#yaml).

### Migrate a Kubernetes deployment without a service

If your Kubernetes deployment performs background or scheduled tasks, and isn't exposed by a service, you can migrate to a [Cloud Run worker pool](https://docs.cloud.google.com/run/docs/deploy-worker-pools).

The following samples show the structural difference between a Kubernetes deployment and a Cloud Run worker pool:

Kubernetes deployment| Cloud Run worker pools  
---|---  
      
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
      namespace: default
      labels:
        app: my-app
    spec:
      template:
        metadata:
          labels:
            app: my-app
        spec:
          containers:
          - image: gcr.io/cloudrun/hello
            env:
            - name: HELLO
              value: world
      replicas: 3
      selector:
        matchLabels:
    

| 
    
    
    apiVersion: run.googleapis.com/v1
    kind: WorkerPool
    metadata:
      name: my-app
      annotations:
        run.googleapis.com/manualInstanceCount: '1'
    spec:
    template:
        metadata:
          labels:
          app: my-app
        spec:
          containers:
          - image: gcr.io/cloudrun/hello
            env:
            - name: HELLO
              value: world
      
  
### Migrate a Kubernetes job

Because a [Kubernetes job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) is similar to a [Cloud Run job execution](https://docs.cloud.google.com/run/docs/managing/job-executions). You can migrate to a [Cloud Run job](https://docs.cloud.google.com/run/docs/resource-model#jobs) and [execute the job](https://docs.cloud.google.com/run/docs/execute/jobs).

The following samples show the structural difference between a Kubernetes job and a Cloud Run job:

Kubernetes job| Cloud Run job  
---|---  
      
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: my-job
    spec:
      template:
        spec:
          containers:
          - image: us-docker.pkg.dev/cloudrun/container/job
    

| 
    
    
    apiVersion: run.googleapis.com/v1
    kind: Job
    metadata:
      name: my-job
    spec:
      template:
        spec:
          template:
            spec:
              containers:
              - image: us-docker.pkg.dev/cloudrun/container/job
      
  
## Migration strategy

After you create the equivalent resources, exposing external endpoints behind a global external Application Load Balancer enables you to gradually migrate traffic between Cloud Run and Google Kubernetes Engine (GKE).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
