---
url: https://docs.cloud.google.com/deploy/docs/deploy-app-canary/
title: Quickstart: Canary-deploy an application to a target \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:58.910998+00:00
---

# Quickstart: Canary-deploy an application to a target  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploy-app-canary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Canary-deploy an application to a target

This quickstart shows you how to use Cloud Deploy to deliver a sample application image in a canary deployment to either Google Kubernetes Engine or to Cloud Run. (You can also run a canary deployment [to GKE attached clusters](https://docs.cloud.google.com/deploy/docs/anthos-targets), but only GKE and Cloud Run are shown in this quickstart.)

A canary deployment splits traffic between an already-deployed version of the application and the new version. Cloud Run apportions traffic based on the percentages you configure in the delivery pipeline. GKE deploys the new version to a proportion of pods. This quickstart deploys to 50% first, then to 100%.

In this quickstart, there is only one [target](https://docs.cloud.google.com/deploy/docs/terminology#target), (`prod`). So we create only one GKE cluster or one Cloud Run service to run your application.

In this quickstart, you'll do the following:

  1. Create one GKE cluster or define one Cloud Run service.

You can canary deploy to GKE attached clusters too, but this quickstart uses GKE and Cloud Run only.

  2. Create a [Skaffold](https://cloud.google.com/skaffold) configuration and a Kubernetes manifest to specify the (pre-built) container image to deploy.

  3. Define your Cloud Deploy delivery pipeline and deployment [target](https://docs.cloud.google.com/deploy/docs/terminology#target).

  4. Invoke your delivery pipeline by creating a release, which automatically deploys to one target.

This first release skips the canary phase.

  5. View the delivery pipeline and release in the Google Cloud console.

  6. Create a second release, this time executing the canary stage to deploy the application to 50%.

  7. Advance the release to deploy to 100%.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Deploy, Cloud Build, GKE, Cloud Run, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-canary)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Deploy, Cloud Build, GKE, Cloud Run, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-canary)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

If you already have the CLI installed, make sure you're running the latest version:
    
    gcloud components update
    

  14. Make sure the [default Compute Engine service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account) has sufficient permissions. 

The service account might already have the necessary permissions. These steps are included for projects that disable automatic role grants for default service accounts.

     1. First add the `clouddeploy.jobRunner` role: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
                --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
                --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                --role="roles/clouddeploy.jobRunner"
            

     2. Add the developer role for your specific runtime.
        * For GKE, and GKE with Gateway API: 
              
              gcloud projects add-iam-policy-binding PROJECT_ID \
                  --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
                  --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                  --role="roles/container.developer"
              

        * For Cloud Run: 
              
              gcloud projects add-iam-policy-binding PROJECT_ID \
                  --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
                  --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                  --role="roles/run.developer"
              

     3. Add the `iam.serviceAccountUser` role, which includes the `actAs`permission to deploy to the runtime: 
            
            gcloud iam service-accounts add-iam-policy-binding $(gcloud projects describe PROJECT_ID \
                --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
                --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                --role="roles/iam.serviceAccountUser" \
                --project=PROJECT_ID
            




## Create your runtime environment

###  GKE 

Create one GKE [Autopilot](https://docs.cloud.google.com/deploy/docs/kubernetes-engine/docs/concepts/autopilot-overview) cluster:
    
    
     gcloud container clusters create-auto canary-quickstart-cluster \
                      --project=PROJECT_ID \
                      --region=us-central1
    

###  GKE + Gateway API 

  1. Create one GKE cluster, with recommended settings to support using with Istio:
         
         gcloud container clusters create canary-quickstart-cluster \
                --machine-type=n1-standard-1 \
                --num-nodes 4 \
                --region=us-central1 \
                --project=PROJECT_ID
         

  2. Get the cluster credentials:
         
         gcloud container clusters get-credentials canary-quickstart-cluster \
                --project=PROJECT_ID \
                --region=us-central1
         

  3. Install the Kubernetes Gateway API CRDs if not already present on the cluster.
         
         kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v0.6.2/standard-install.yaml
         

  4. Enable Istio's Gateway controller implementation by installing Istio.
         
         curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.17.2 sh - \
         && ./istio-1.17.2/bin/istioctl install --set profile=minimal -y
         




###  Cloud Run 

If you're using Cloud Run, you can skip this command, you don't need to do anything here.

## Prepare your Skaffold configuration and application manifest

Cloud Deploy uses [Skaffold](https://docs.cloud.google.com/deploy/docs/using-skaffold) to provide the details for what to deploy and how to deploy it properly to your [target](https://docs.cloud.google.com/deploy/docs/terminology#target).

In this quickstart, you create a `skaffold.yaml` file, which identifies the Kubernetes manifest or Cloud Run service configuration to be deployed.

  1. Open a terminal window.

  2. Create a new directory and navigate into it.

###  GKE 
         
         mkdir deploy-canary-quickstart-gke
         cd deploy-canary-quickstart-gke
         

###  GKE + Gateway API 
         
         mkdir deploy-canary-quickstart-gke-gatewayapi
         cd deploy-canary-quickstart-gke-gatewayapi
         

###  Cloud Run 
         
         mkdir deploy-canary-quickstart-run
         cd deploy-canary-quickstart-run
         

  3. Create a file named `skaffold.yaml` with the following contents:

###  GKE 
         
         apiVersion: skaffold/v4beta7
         kind: Config
         manifests:
           rawYaml:
           - kubernetes.yaml
         deploy:
           kubectl: {}
         

###  GKE + Gateway API 
         
         apiVersion: skaffold/v4beta7
         kind: Config
         manifests:
           rawYaml:
           - kubernetes.yaml
         deploy:
           kubectl: {}
         

###  Cloud Run 
         
         apiVersion: skaffold/v4beta7
         kind: Config
         manifests:
           rawYaml:
           - run.yaml
         deploy:
           cloudrun: {}
         

This file is a minimal Skaffold config, identifying your manifest. For this quickstart, you create the file. But you can also [have Cloud Deploy create one for you](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold#have_generate_your_skaffoldyaml), for simple, non-production applications.

See the [`skaffold.yaml` reference](https://skaffold.dev/docs/references/yaml/) for more information about this file.

  4. Create your application manifest.

###  GKE 

Create a file named `kubernetes.yaml`, in the `deploy-canary-quickstart-gke` directory, with the following contents:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-deployment
           labels:
             app: my-app
           namespace: default
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: my-app
           template:
             metadata:
               labels:
                 app: my-app
             spec:
               containers:
               - name: nginx
                 image: my-app-image
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: my-service
           namespace: default
         spec:
           selector:
             app: my-app
           ports:
             - protocol: TCP
               port: 80
         

This file is a Kubernetes [manifest](https://kubernetes.io/docs/reference/glossary/?fundamental=true#term-manifest), which is applied to the cluster to deploy the application. This manifest includes the Service and Deployment resources required for canary deployment, plus an HTTPRoute and the Gateway resource needed for using Gateway API.

The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.

###  GKE + Gateway API

Create a file named `kubernetes.yaml`, in the `deploy-canary-quickstart-gke-gatewayapi` directory, with the following contents:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: my-gateway
           annotations:
             networking.istio.io/service-type: "ClusterIP"
         spec:
           gatewayClassName: istio
           listeners:
           - name: default
             hostname: "*.example.com"
             port: 80
             protocol: HTTP
             allowedRoutes:
               namespaces:
                 from: All
         ---
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: my-httproute
         spec:
           parentRefs:
           - kind: Gateway
             name: my-gateway
           hostnames:
           - "test.example.com"
           rules:
           - backendRefs:
             - name: my-service
               port: 80
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: my-service
         spec:
           selector:
             app: my-app
           ports:
           - name: tcp-port
             protocol: TCP
             port: 80
             targetPort: 8080
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-deployment
           labels:
             app: my-app
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: my-app
           template:
             metadata:
               labels:
                 app: my-app
             spec:
               containers:
               - name: nginx
                 image: my-app-image
         

This file is a Kubernetes [manifest](https://kubernetes.io/docs/reference/glossary/?fundamental=true#term-manifest), which is applied to the cluster to deploy the application. This manifest includes the Service and Deployment resources required for canary deployment, plus an HTTPRoute and the Gateway resource needed for using Gateway API.

The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.

###  Cloud Run 

Create a file named `run.yaml`, in the `deploy-canary-quickstart-run` directory, with the following contents:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: my-canary-run-service
         spec:
           template:
             spec:
               containers:
               - image: my-app-image
         

This file is a basic Cloud Run service definition, which is applied at deploy time to create your service in Cloud Run. The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.


**Note:** If you want to use different manifests per target, read [this article about managing manifests](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) to find out more about using Skaffold profiles.

## Create your delivery pipeline and targets

You can define your delivery pipeline and targets in one file or in separate files. In this quickstart, we create one file for our pipeline and our single target:

###  GKE 

Create a file named `clouddeploy.yaml`, in the `deploy-canary-quickstart-gke` directory, with the following contents:
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: DeliveryPipeline
    metadata:
      name: my-canary-demo-app-1
    description: main application pipeline
    serialPipeline:
      stages:
      - targetId: prod
        profiles: []
        strategy:
          canary:
            runtimeConfig:
              kubernetes:
                serviceNetworking:
                  service: "my-service"
                  deployment: "my-deployment"
            canaryDeployment:
              percentages: [50]
              verify: false
    ---
    apiVersion: deploy.cloud.google.com/v1
    kind: Target
    metadata:
      name: prod
    description: prod GKE cluster
    gke:
     cluster: projects/PROJECT_ID/locations/us-central1/clusters/canary-quickstart-cluster
    

###  GKE + Gateway API 

Create a file named `clouddeploy.yaml`, in the `deploy-canary-quickstart-gke-gatewayapi` directory, with the following contents:
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: DeliveryPipeline
    metadata:
      name: my-canary-demo-app-1
    description: main application pipeline
    serialPipeline:
      stages:
      - targetId: prod
        profiles: []
        strategy:
          canary:
            runtimeConfig:
              kubernetes:
                gatewayServiceMesh:
                  httpRoute: "my-httproute"
                  service: "my-service"
                  deployment: "my-deployment"
            canaryDeployment:
              percentages: [50]
              verify: false
    ---
    apiVersion: deploy.cloud.google.com/v1
    kind: Target
    metadata:
      name: prod
    description: prod GKE cluster
    gke:
     cluster: projects/PROJECT_ID/locations/us-central1/clusters/canary-quickstart-cluster
    

###  Cloud Run 

Create a file named `clouddeploy.yaml`, in the `deploy-canary-quickstart-run` directory, with the following contents:
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: DeliveryPipeline
    metadata:
      name: my-canary-demo-app-1
    description: main application pipeline
    serialPipeline:
      stages:
      - targetId: prod
        profiles: []
        strategy:
          canary:
            runtimeConfig:
              cloudRun:
                automaticTrafficControl: true
            canaryDeployment:
              percentages: [50]
              verify: false
    ---
    apiVersion: deploy.cloud.google.com/v1
    kind: Target
    metadata:
      name: prod
    description: prod Run Service
    run:
      location: projects/PROJECT_ID/locations/us-central1
    

  1. Register your pipeline and targets with the Cloud Deploy service:
         
         gcloud deploy apply --file=clouddeploy.yaml --region=us-central1 --project=PROJECT_ID
         

You now have a pipeline, with one target configured for a canary deployment strategy.

  2. Confirm your pipeline and targets:

In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view of list of your available delivery pipelines.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

The delivery pipeline you just created is shown, and the one target you configured is listed in the **Targets** column.

![delivery pipeline visualization in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/pipelines-page-canary1.png)




## Create a release

A release is the central Cloud Deploy resource representing the changes being deployed. The delivery pipeline defines the lifecycle of that release. See [Cloud Deploy service architecture](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release) for details about that lifecycle.

To create a `release` resource that represents the container image to deploy, run the following command from the `deploy-canary-quickstart-gke`, `deploy-canary-quickstart-gke-gatewayapi`, or `deploy-canary-quickstart-run` directory:

###  GKE 
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=my-canary-demo-app-1 \
       --images=my-app-image=gcr.io/google-containers/nginx@sha256:f49a843c290594dcf4d193535d1f4ba8af7d56cea2cf79d1e9554f077f1e7aaa
    

###  GKE + Gateway API 
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=my-canary-demo-app-1 \
       --images=my-app-image=gcr.io/google-containers/nginx@sha256:f49a843c290594dcf4d193535d1f4ba8af7d56cea2cf79d1e9554f077f1e7aaa
    

###  Cloud Run 
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=my-canary-demo-app-1 \
       --images=my-app-image=us-docker.pkg.dev/cloudrun/container/hello@sha256:95ade4b17adcd07623b0a0c68359e344fe54e65d0cb01b989e24c39f2fcd296a
    

Notice the [`--images=` flag](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--images), which you use to replace the placeholder (`my-app-image`) in the manifest or service definition with the specific, SHA-qualified image. Google recommends that you templatize your manifests this way, and that you use SHA-qualified image names at release creation.

When you create a release, Cloud Deploy automatically creates a rollout resource too, to immediately deploy to your one target, `prod`.

### We skip to the stable phase

With this first release, we skip the canary phase, and deploy to 100% (stable phase). This is because the application hasn't been deployed previously, so there's no way to calculate 50% of pods (for GKE) or how traffic is split for the service (for Cloud Run). The pods (GKE) or revisions (Cloud Run) don't exist yet.

Having skipped the canary phase, we're now ready to start the stable phase, which takes traffic to 100%. After that, we'll create another release, and that will execute the canary.

In a real-world situation, you will usually execute a canary deployment where your application is already running, so this phase skipping will be rare.

## View the release in Google Cloud console

Now that you've created the first release, the rollout is created, and you can view the release and the rollout in Google Cloud console. You can also view the pipeline visualization, which shows the current status of the release.

  1. In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view your **my-canary-demo-app-1** delivery pipeline.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

  2. Click the name of your delivery pipeline "my-canary-demo-app-1".

The pipeline visualization shows the app's deployment status. Because there's only one stage in the pipeline, the visualization shows only one node.

![delivery pipeline visualization in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/canary_qs_pipeline_viz1.png)

And your release is listed on the **Releases** tab under **Delivery pipeline details**.

  3. Click the release name, `test-release-001`.

Your rollouts appear under **Rollouts**. You can click a rollout to view its details, including the deployment log.

![rollouts in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/canary_rollouts_success.png)

Notice that the rollout status is "Pending advance," and the target shown in the pipeline visualization has a link to "Advance to stable."




## Advance the rollout phase

After the first release, the canary phase was skipped, and the rollout is waiting to start the "stable" phase, which deploys the application to 100%:

  1. In the pipeline visualization, click **Advance to stable**.

  2. When prompted, click **Advance** to confirm.




After a few minutes, the rollout is now in the "stable" phase, and the application is deployed to 100%.

![delivery pipeline in stable phase](https://docs.cloud.google.com/static/deploy/images/canary_qs_prod_100.png)

## Execute the canary deployment

Because the first release skipped the canary phase, we'll now create another release, which this time does execute a canary deployment.

  1. To create a new `release`, run the following command from the `deploy-canary-quickstart-gke`, `deploy-canary-quickstart-gke-gatewayapi` or `deploy-canary-quickstart-run` directory:

###  GKE 
         
         gcloud deploy releases create test-release-002 \
           --project=PROJECT_ID \
           --region=us-central1 \
           --delivery-pipeline=my-canary-demo-app-1 \
           --images=my-app-image=gcr.io/google-containers/nginx@sha256:f49a843c290594dcf4d193535d1f4ba8af7d56cea2cf79d1e9554f077f1e7aaa
         

###  GKE + Gateway API 
         
         gcloud deploy releases create test-release-002 \
           --project=PROJECT_ID \
           --region=us-central1 \
           --delivery-pipeline=my-canary-demo-app-1 \
           --images=my-app-image=gcr.io/google-containers/nginx@sha256:f49a843c290594dcf4d193535d1f4ba8af7d56cea2cf79d1e9554f077f1e7aaa
         

###  Cloud Run 
         
         gcloud deploy releases create test-release-002 \
           --project=PROJECT_ID \
           --region=us-central1 \
           --delivery-pipeline=my-canary-demo-app-1 \
           --images=my-app-image=us-docker.pkg.dev/cloudrun/container/hello@sha256:95ade4b17adcd07623b0a0c68359e344fe54e65d0cb01b989e24c39f2fcd296a
         

After a few minutes, a rollout is created, and this time the canary stage is executed:

![delivery pipeline starting canary phase](https://docs.cloud.google.com/static/deploy/images/canary_qs_after_rel2.png)

When the first rollout phase finishes, the rollout is now in the canary phase:

![delivery pipeline visualization in Google Cloud console, with application deployed to 50%](https://docs.cloud.google.com/static/deploy/images/canary_qs_viz_in_canary.png)

This means that the application is now deployed to 50%. For serviceNetworking-based GKE, it's deployed to half of your pods. For Gateway API-based GKE and Cloud Run traffic is allocated to 50%.

  2. Click **Advance Rollout** , then click **Advance** when prompted.

This advances the rollout to the "stable" phase, deploying the application to 100%.

![delivery pipeline in stable phase, deployed to 100%](https://docs.cloud.google.com/static/deploy/images/canary_qs_viz_in_stable.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the `canary-quickstart-cluster` cluster (GKE only):
         
         gcloud container clusters delete canary-quickstart-cluster --region=us-central1 --project=PROJECT_ID
         

  2. Delete the `my-canary-run-service` service (Cloud Run only):
         
         gcloud run services delete my-canary-run-service --region=us-central1 --project=PROJECT_ID
         

  3. Delete the delivery pipeline, target, and all release and rollout resources:
         
         gcloud deploy delete --file=clouddeploy.yaml --force --region=us-central1 --project=PROJECT_ID
         

  4. Delete the Cloud Storage buckets that Cloud Deploy created.

One ends with `_clouddeploy`, and the other is `[region].deploy-artifacts.[project].appspot.com`.

[Open the Cloud Storage browser page](https://console.cloud.google.com/storage/browser)




That's it, you completed this quickstart!

## What's next

  * [Learn more about Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview).

  * [Learn the basics of deploying applications](https://docs.cloud.google.com/deploy/docs/deploying-application).

  * Learn how to [manage your manifests](https://docs.cloud.google.com/deploy/docs/skaffold).

  * [Learn how to combine Google Cloud CI/CD tools to develop and deliver software effectively to GKE](https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
