---
url: https://docs.cloud.google.com/run/docs/migrate/to-gke/
title: Migrate from Cloud Run to Google Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:51.086036+00:00
---

# Migrate from Cloud Run to Google Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/migrate/to-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Migrate from Cloud Run to Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run and Kubernetes both use standard container images as deployment artifacts, they both use a declarative API model with resources that can be represented in YAML files with the same standard structure.

## Introduction

The [Cloud Run Admin API v1](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.services) is designed to maximize portability with Kubernetes, for example, the Cloud Run Admin API resources share the same structure conventions and attribute names as Kubernetes resources. See the [Cloud Run service YAML reference](https://docs.cloud.google.com/run/docs/reference/yaml/v1#service).

The Cloud Run Admin API v1 implements the [Knative Serving API specification](https://github.com/knative/specs/blob/main/specs/serving/knative-api-specification-1.0.md), but you do **not** need to migrate to Knative to move your Cloud Run workloads to a Kubernetes cluster like GKE.

## Quickstart

This quickstart is an example of a simple migration.

### Simple resource comparison

Compare the following simple Cloud Run service named `my-app` with the equivalent Kubernetes [deployment](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/). Note how the YAML files are almost identical.

However, the parts in `blue` are different and need to be changed. The parts in `green` should be added.

Cloud Run service| Kubernetes deployment  
---|---  
      
    
    apiVersion: serving.knative.dev/v1
    kind: Service
    metadata:
      name: my-app
      namespace: 'PROJECT_NUMBER'
    spec:
      template:
        spec:
          containers:
          - image: gcr.io/cloudrun/hello
            env:
            - name: HELLO
              value: world
    

| 
    
    
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
      
  
### Migrate a Cloud Run service to GKE

  1. Download service YAML file into the current directory:
         
         gcloud run services describe my-app --format export > my-app.yaml

  2. Modify the YAML to match a Kubernetes deployment:

     * For the "`kind`" attribute: replace the value "`Service`" with "`Deployment`"
     * For the "`apiVersion`" attribute: replace the value "`serving.knative.dev/v1`" with "`apps/v1`"
     * Replace `metadata.namespace` with the namespace of the GKE cluster you want to deploy to, for example `default`.
     * Add a new label to under `metadata` and `spec.template.metadata`.
     * Set a fixed number of instances ("replicas") using `spec.template.spec.replicas` and set a label selector in `spec.template.spec.selector`.
  3. [Install](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl) and use the `kubectl` command line tool to deploy the `my-app.yaml` file to your GKE cluster:
         
         kubectl apply -f ./my-app.yaml

  4. Expose the deployment as a service:
         
         kubectl expose deployment my-app --type LoadBalancer --port 80 --target-port 8080




## Considerations when migrating from Cloud Run to GKE

**Cluster** :

  * Cloud Run is a fully managed platform, while GKE requires more platform management. If you have not yet created a GKE cluster, use [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).

  * The scalability of GKE workloads is restricted by the size of the cluster. If you are not using an Autopilot cluster, consider using [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) and a [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) to resize your cluster.

  * Cloud Run has a [built-in zonal redundancy](https://docs.cloud.google.com/architecture/disaster-recovery#cloud-run), so migrate to a [regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) and provision enough replicas to ensure your service is resilient to a zonal outage in the selected Google Cloud region.




**Pricing**

Cloud Run [charges](https://cloud.google.com/run/pricing) for used resources, while GKE [charges](https://cloud.google.com/kubernetes-engine/pricing) for provisioned resources.

**Security** :

  * Contrary to Cloud Run, invoking a GKE service is not subject to an [IAM invoker permission](https://docs.cloud.google.com/run/docs/reference/iam/permissions).

  * Because GKE does not provide strong isolation between containers, consider using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) if you need to execute unknown or untrusted code.




**Networking**

Cloud Run requires a Serverless VPC Access connector to access other resources in a VPC. GKE workloads are directly in a VPC and do not need a connector.

## Features not supported by Google Kubernetes Engine

The following Cloud Run features are not available on GKE:

  * Configuration versioning via [revisions](https://docs.cloud.google.com/run/docs/resource-model#revisions)
  * [Traffic splitting](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration) for gradual rollouts and rollbacks of revisions
  * [Request-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings)
  * [CPU boost](https://docs.cloud.google.com/run/docs/configuring/services/cpu#startup-boost)
  * [Session affinity](https://docs.cloud.google.com/run/docs/configuring/session-affinity)
  * [Labels](https://docs.cloud.google.com/run/docs/configuring/services/labels) on GKE workloads are not Google Cloud labels
  * [Tags](https://docs.cloud.google.com/run/docs/configuring/tags) on workloads



## Migrate Cloud Run resources

The following sections describe migrating resources used in Cloud Run, such as Cloud Run services, jobs, and secrets.

### Migrate Cloud Run services

You can migrate a Cloud Run service to the following resources on GKE:

  1. [Kubernetes deployment](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/) to create instances (called "pods" in Kubernetes).
  2. [Kubernetes services](https://kubernetes.io/docs/concepts/services-networking/service/) to expose the deployment at a specific endpoint.
  3. [Kubernetes Horizontal Pod Autoscaler](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/): to automatically scale the deployment.



The attributes of a Kubernetes deployment are a superset of the attributes of a Cloud Run services. As shown in the quickstart, after you change the `apiVersion` and `kind` attributes to `apps/v1` and `Deployment`, you also need to change the following:

  * Replace `namespace` with the GKE cluster namespace to deploy to, for example `default`.
  * `serviceAccountName` should reference a Kubernetes service account, which can optionally act as an IAM service account with Workload Identity Federation for GKE.
  * Add a LABEL at `metadata.labels` and `spec.template.metadata.labels` that will be used to select the deployment and pods. For example: `app: NAME`
  * Under `spec.template`: 
    * Add a `replicas` attribute to specify a number of "instances".
    * Add a `selector.matchLabels` attribute that selects on the label LABEL.
  * If your Cloud Run service mounts secrets, see Migrate secrets.
  * If the migrated Cloud Run service was accessing resources on a Virtual Private Cloud, you do not need to use a Serverless VPC Access connector.



After creating the Kubernetes deployment, create a Kubernetes services to expose it:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: NAME
    spec:
      selector:
        LABEL
      ports:
        - protocol: TCP
          port: 80
          targetPort: PORT
    

Replace:

  * NAME: with the name of your service.
  * LABEL: with the label defined in your deployment. For example `app: NAME`.
  * PORT: with the `containerPort` of the container receiving requests in the Cloud Run service, which defaults to `8080`.



You can then optionally create a Kubernetes Horizontal Pod Autoscaler in order to automatically scale the number of pods. Follow the Kubernetes [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) documentation to create an `HorizontalPodAutoscaler`. Use the [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances#yaml) (`autoscaling.knative.dev/minScale`) and [maximum instances](https://docs.cloud.google.com/run/docs/configuring/max-instances#yaml) (`autoscaling.knative.dev/maxScale`) values of your Cloud Run service as values for the `minReplicas` and `maxReplicas` attributes `HorizontalPodAutoscaler`.

### Migrate Cloud Run worker pools

You can migrate a [Cloud Run worker pool](https://docs.cloud.google.com/run/docs/deploy-worker-pools) to a [Kubernetes deployment](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/) on GKE.

The following samples show the structural difference between a Cloud Run worker pool and a Kubernetes deployment.

Cloud Run worker pools| Kubernetes deployment  
---|---  
      
    
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
    

| 
    
    
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
      
  
### Migrate Cloud Run jobs

You can migrate a [Cloud Run job](https://docs.cloud.google.com/run/docs/resource-model#jobs) to a [Kubernetes job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) on GKE.

Contrary to Cloud Run jobs, Kubernetes jobs are executed when they are created. If you want to execute the job again, you need to create a new job.

The following samples show the structural difference between a Cloud Run job and a Kubernetes job:

Cloud Run job| Kubernetes job  
---|---  
      
    
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
    

| 
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: my-job
    spec:
      template:
        spec:
          containers:
          - image: us-docker.pkg.dev/cloudrun/container/job
      
  
### Migrate secrets

You can keep existing secrets in Secret Manager or you can migrate them to Kubernetes secrets.

If you choose to keep secrets in Secret Manager, you will need to [update how you use them on GKE](https://docs.cloud.google.com/secret-manager/docs/using-other-products#google-kubernetes-engine)

If you choose to migrate from Secret Manager to Kubernetes secrets, consider these differences between Secret Manager secrets and Kubernetes secrets:

  * **Allowed characters in names** : 
    * [Kubernetes secrets](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names): `[a-z0-9-.]{1,253}`
    * Secret Manager secrets: `[a-zA-Z0-9_-]{1,255}`
  * **Versioning** : Secrets from Secret Manager are versioned, while Kubernetes secrets aren't.
  * **Payload** : Secrets from Secret Manager contain a single `[]byte`, while Kubernetes secrets contain a `map<string, string>`.



## Migration strategy

After you create the equivalent resources, exposing external endpoints behind a global external Application Load Balancer enables you to gradually migrate traffic between Cloud Run and Google Kubernetes Engine (GKE).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
