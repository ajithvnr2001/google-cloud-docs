---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/migrate/cloud-run/
title: Migrating a Knative serving service to Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:30.343388+00:00
---

# Migrating a Knative serving service to Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/migrate/cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Migrating a Knative serving service to Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

Use this guide to migrate your workloads to Cloud Run. In general, migrating your workloads requires you to port over any of the Kubernetes-based features and then redeploy each of your existing services to Cloud Run.

Key benefits of migrating to Cloud Run:

  * Fully managed serverless product that implements the [Knative Serving API specification](https://github.com/knative/specs/blob/main/specs/serving/knative-api-specification-1.0.md) and adheres to the container contract.

  * The [v1 Admin API of Cloud Run](https://docs.cloud.google.com/run/docs/reference/rest) is designed to maximize portability with Knative serving.

  * The user experience is similar across Cloud Run and Knative serving:

    * The `gcloud run` command group is used across both products.
    * Similar user interface layout and behavior in Google Cloud console.



## Before you begin

The following Google Kubernetes Engine features are not supported in Cloud Run, including:

  * Cluster and pod features, for example [Startup, Liveness and Readiness probes, and Service Discovery](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).
  * Configuration: 
    * [ConfigMaps](https://docs.cloud.google.com/anthos/run/archive/docs/configuring/using-configmaps) \- You can transform your ConfigMaps into secrets with Secret Manager.
    * [NVIDIA GPUs](https://docs.cloud.google.com/anthos/run/archive/docs/configuring/compute-power-gpu)
  * Access controls:

    * [GKE specific IAM roles](https://docs.cloud.google.com/anthos/run/docs/deploying#permissions_required_to_deploy)
    * [Workload Identity](https://docs.cloud.google.com/anthos/run/archive/docs/configuring/workload-identity)
    * [Cluster multi-tenancy](https://docs.cloud.google.com/anthos/run/archive/docs/multi-tenancy)

You can use [IAM in Cloud Run](https://docs.cloud.google.com/run/docs/securing/managing-access) to achieve the same control over access to your resources. Also consider using [Service identity](https://docs.cloud.google.com/run/docs/securing/service-identity).




## Migration considerations

You must review and understand the following differences across the products to ensure that you can port over all your dependencies and requirements.

### Secrets

In Cloud Run, you can choose to mount secrets as environment variables or volumes, but secrets with sensitive information should be stored in [Secret Manager](https://docs.cloud.google.com/secret-manager).

Important differences between [secrets in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) and [Kubernetes secrets](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names):

Feature | Secret Manager secrets | Kubernetes secrets  
---|---|---  
Allowed characters in names | `[a-zA-Z0-9_-]{1,255}` | `[a-z0-9-.]{1,253}`  
Versioning | Secrets are versioned | No support  
Secret Payload | Single `[]byte` | Map: `<string, string>`  
  
Learn how to use Secret Manager to [create versioned secrets](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create) for the secret keys of your Knative serving services.

### Networking

Use the following information to help you port over your existing network configuration to Cloud Run.

Service Endpoints
    The [Kubernetes Endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#service_endpoints) of your Knative serving services are not supported in Cloud Run. [Learn more about the unique endpoints in Cloud Run](https://docs.cloud.google.com/run/docs/resource-model).
Domains Mappings
    The Cloud Run [DomainMapping API](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.domainmappings#DomainMapping) is compatible with Knative serving. However, Cloud Run offers domain mapping in a subset of the available [Cloud Run locations](https://docs.cloud.google.com/run/docs/locations#domains). A recommended alternative is to leverage [Global HTTP(S) Load Balancer](https://docs.cloud.google.com/run/docs/mapping-custom-domains) for your custom domains.
VPC connectivity
    Cloud Run services reside outside your VPC. To communicate with resources within a VPC, you must use the [Serverless VPC Access Connector](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls).
Ingress controls
    If your Knative serving service is configured for a private internal network and uses an internal load balancer (ILB), you can configure your Cloud Run service to [`Ingress = Internal`](https://docs.cloud.google.com/run/docs/securing/ingress). Configuring your services to `internal` restricts access to within your VPC or other Cloud Run services. [Learn more about service to service communication](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

## Migrating a service

To migrate a service, you must export your Knative serving service, edit the exported YAML file, and then deploy your reconfigured service to Cloud Run.

**Note:** If you obtain and use the [original YAML configuration file](https://docs.cloud.google.com/anthos/run/docs/deploying#yaml) that you initially created for Knative serving, you can skip the export and modify steps. With the original YAML configuration file, you can simply deploy it directly to Cloud Run to create your services.

  1. Export your Knative serving service to a local YAML file by running the following command:
         
         gcloud run services describe SERVICE --format export --namespace NAMESPACE --cluster CLUSTER --platform gke > FILENAME.yaml
         

Replace:

     * `SERVICE` with the name of your Knative serving service.
     * `NAMESPACE` with the namespace where your service is running.
     * `CLUSTER` with the name of the cluster where your service is running.
     * `FILENAME` with a unique filename of your choice.
  2. Modify the exported `FILENAME.yaml` file for Cloud Run:

     * You must search and replace the Kubernetes namespace with the ID of your Google Cloud project. For example, you must replace `namespace:`_`default`_ with `namespace:`**`my-unique-id`**.
     * You must update all configurations for any of the unsupported features.
     * You must delete any of the following attributes and their values:

       * `metadata.annotations.kubectl.kubernetes.io/last-applied-configuration`
       * `metadata.managedFields`
       * `spec.template.spec.containers.readinessProbes`
       * `spec.template.spec.enableServiceLinks`

For example, you might need to remove the following configuration from under the `spec:` > `template:` > `spec:` > `containers:` attributes:
    
    ...
     readinessProbe:
       successThreshold: 1
       tcpSocket: {}
    ...
    

  3. Deploy the modified `.yaml` file to Cloud Run using the `--platform managed` flag. [Learn more about deploying](https://docs.cloud.google.com/run/docs/deploying).

Note that you can use the same Google Cloud project for Cloud Run.
         
         gcloud run services replace FILENAME.yaml --platform managed --region REGION
         

Replace:

     * `FILENAME` with the name of the exported configuration file that you created.
     * `REGION` with a [supported Cloud Run location](https://docs.cloud.google.com/run/docs/locations). For example: `us-central1`
  4. Configure access to your Cloud Run service:

     * By default, a Cloud Run service is not externally accessible. To publicly expose your service to the internet and allow unauthenticated requests, you must [allow public (unauthenticated) access](https://docs.cloud.google.com/run/docs/authenticating/public).

     * To configure this service for private internal-only access like between your Cloud Run services, see [Authenticating service-to-service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

  5. In the Google Cloud console, within your services page, you can click the displayed URL link to open the unique and stable endpoint of your deployed service.

[Go to Cloud Run](https://console.cloud.google.com/run)




## Migrating traffic to your service

After you have tested your newly deployed services and are ready to migrate all of your production traffic, you can configure your custom domain and update your DNS records with your registrar. Follow the instructions at [Mapping custom domains](https://docs.cloud.google.com/run/docs/mapping-custom-domains).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
