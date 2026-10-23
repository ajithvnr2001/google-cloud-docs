---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-developer-workflow/
title: Modern CI/CD with GKE: Apply the developer workflow \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:13.724612+00:00
---

# Modern CI/CD with GKE: Apply the developer workflow  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-developer-workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Modern CI/CD with GKE: Apply the developer workflow Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2023-09-11 UTC

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows how to onboard a new application, develop a feature for the application, and deploy the application to production using modern continuous integration/continuous delivery (CI/CD) techniques with Google Kubernetes Engine (GKE).

This document is part of a series:

  * [Modern CI/CD with GKE: A software delivery framework](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-user-guide)
  * [Modern CI/CD with GKE: Build a CI/CD system](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture) (reference architecture)
  * Modern CI/CD with GKE: Apply the developer workflow (this document)



In this tutorial, you use tools such as [Skaffold](https://skaffold.dev), [`kustomize`](https://github.com/kubernetes-sigs/kustomize#kustomize), [Artifact Registry](https://docs.cloud.google.com/artifact-registry), [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview), [Cloud Build](https://docs.cloud.google.com/build) and [Cloud Deploy](https://docs.cloud.google.com/deploy) to develop, build and deploy your application.

**Caution** : Skaffold [will be removed](https://groups.google.com/g/skaffold-users/c/FTR3xLJpePY) from gcloud CLI releases after January 15, 2027. Going forward, Skaffold can be installed following the instructions in the [Installing Skaffold documentation](https://skaffold.dev/docs/install/). On January 29, 2027 the Skaffold GitHub repository will be archived. All existing releases will remain available to users.

This document is intended for enterprise architects and application developers, as well as IT security, DevOps, and Site Reliability Engineering (SRE) teams. Some experience with automated deployment tools and processes is useful for understanding the concepts in this document.

## Architecture

In this tutorial, you onboard a new application. Then, you develop a new feature and deploy the application in dev, staging, and production environments. The reference architecture contains the infrastructure and tools needed to onboard and release a new application with the workflow shown in the following diagram:

![The development loop spans code repositories, cloudbuild and cloud deploy pipelines.](https://docs.cloud.google.com/static/architecture/images/modern-cicd-gke-developer-workflow-pipeline-overview.svg)

Starting at the code repository for CI, the workflow includes the following steps:

  1. You share your application source code through your application repositories.

  2. When you commit and push the code to the application repository, it automatically triggers a CI pipeline in Cloud Build. The CI process creates and pushes a container image to Artifact Registry.

  3. The CI process also creates a CD release for the application in Cloud Deploy.

  4. The CD release generates fully rendered kubernetes manifests for dev using `skaffold` and deploys them in the dev GKE cluster.

  5. The CD release is then promoted from dev to a staging target, that generates fully rendered staging manifests and deploys them in the staging GKE cluster.

  6. Then, The CD release is promoted from staging to production, that generates fully rendered production manifests and deploys them in production GKE clusters.




For more information about the tools and infrastructure used in this workflow, see [Modern CI/CD with GKE: Build a CI/CD system](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture).

## Objectives

  * Onboard a new application.

  * Deploy the application in the dev environment.

  * Develop a new feature and deploy it in the dev environment.

  * Promote the new feature to staging and then release it into production.

  * Test the resiliency of the application.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [ Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)
  * [ Cloud Build](https://docs.cloud.google.com/build/pricing)
  * [ Cloud Deploy](https://docs.cloud.google.com/deploy/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  * For this tutorial, deploy [the reference architecture](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture) in this series.



## Prepare your environment

  1. If you're continuing directly from [Modern CI/CD with GKE: Build a CI/CD system](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture), go to the next section. However, if you have a new session, or your session expired, open Cloud Shell and set the project where you installed the reference architecture infrastructure:
         
         gcloud config set core/project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project ID.




## Onboard a new application

The reference architecture contains an application factory. This factory is a collection of a git repository named `application-factory-repo` and the following Cloud Build triggers: 

  * `create-app`
  * `tf-plan`
  * `tf-apply`
  * `create-team`



You use the application factory to onboard a new application from starter repositories. Application onboarding consists of the following steps:

  1. **Create the application definition** : You create the application definition in a Terraform file and store it in `application-factory-repo` which acts as application catalog.

  2. **Create the application infrastructure** : You run Terraform on the application definition file to create the application infrastructure. Application infrastructure consists of the following:

     1. A [Landing zone](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture#application_landing_zones) for the new application includes defining the namespace, service account, and base policies in the `acm-gke-infrastructure-repo` repository. The landing zone is only created in a dev GKE cluster while onboarding a new application. This is done to unblock the developers so that they can use the dev environment and start iterating on it. The landing zone in the staging and production clusters are created with the GitOps approach. This approach is demonstrated later in this document when you are ready to promote the release in those clusters.

     2. The Infrastructure repository from [infrastructure starter repository](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture#infrastructure_starter_repositories) that hosts the code to create the CI pipeline in Cloud Build, the CD pipeline in Cloud Deploy, and the Artifact Registry repository for storing artifacts.

     3. An infrastructure Cloud Build trigger that takes the code in the infrastructure repository and creates the resources based on their definition.

     4. An application repository from the [application starter repository](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture#applications_starter_repositories) that hosts the application's source code.

  3. **Create application's CI/CD resources** : You use the application infrastructure to create CI/CD resources for the application.


**Note:** The reference architecture lets you automate entire application onboarding and deployment steps. So you can better understand the architecture, this document breaks out those steps.

### Create application definition:

Run the `create-app` trigger to generate an application definition file in `application-factory-repo`. The definition file contains the declarative definition of the resources required to create an application.

  1. In the Google Cloud console, go to the Cloud Build page:

[Go to the Cloud Build page](https://console.cloud.google.com/cloud-build/triggers)

  2. Click **`create-app` trigger**.

  3. Click **SHOW URL PREVIEW** to display the URL required to invoke the webhook.

  4. In Cloud Shell, invoke the trigger by making a curl request on the URL obtained from the previous step and passing the parameters as a payload to it.
         
         curl "WEBHOOK_URL" -d '{"message": {"app": "sample","runtime": "python","trigger_type": "webhook","github_team": ""}}'

In the previous code sample:

     * Replace `WEBHOOK_URL` with the URL obtained from the trigger.

     * `"app": "sample"` specifies the name of the application.

     * `"runtime": "python"` tells the application factory to use the python template to create application repositories.

     * `"trigger_type": "webhook"` specifies the type of CI/CD pipelines for the application.

     * `"github_team": ""` is a team in GitHub that's going to be associated with the repositories that are created for the application. Since, you haven't created a GitHub team yet, pass it as an empty string.

  5. Check the pipeline for `create-app` trigger:

[Go to the Cloud Build History page](https://console.cloud.google.com/cloud-build/builds).

There is a new pipeline for `create-app` trigger. When that has completed, the application definition is created in `application-factory-repo`.

  6. Review the application definition file:

     1. In a web browser, go to [GitHub](https://github.com/) and sign in to your account.

     2. Click the picture icon and click **`Your organizations`**. Choose your organization.

     3. Click the repository `application-factory-repo`, go to the folder `apps/python` and open the new file named `sample.tf` created by the `create-app` trigger. Inspect the file, this file contains Terraform code to create a new application.




### Create application infrastructure:

Now that you've created the application definition, you run the trigger `tf-apply` to create the application infrastructure.

  1. In Google Cloud console:

[Go to the Cloud Build page](https://console.cloud.google.com/cloud-build/triggers) .

Click `tf-apply` trigger.

  2. Click "SHOW URL PREVIEW" to display the URL required to invoke the webhook.

  3. Invoke the trigger:
         
         curl "WEBHOOK_URL" -d '{}'

In the previous code sample:

     * Replace `WEBHOOK_URL` with the URL obtained from the trigger.
  4. Check the pipeline for `tf-apply` trigger:

[Go to the Cloud Build History page](https://console.cloud.google.com/cloud-build/builds).

There is a new pipeline for `tf-apply` trigger. Wait for it to complete.




This trigger creates the application infrastructure.

### Review the application infrastructure:

Review the various components of the application infrastructure.

#### Landing zone

  1. Go to Cloud Shell and set the project. 
         
         gcloud config set core/project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Get credentials to the development GKE cluster.
         
         gcloud container clusters get-credentials gke-dev-us-central1 --location us-central1-a
         

  3. Check the namespace of the application. The namespace is named after the application, sample.
         
         kubectl get namespaces sample
         

The output resembles the following: 
         
         NAME     STATUS   AGE
         sample   Active   15m
         

  4. Check the service account in the namespace.
         
         kubectl get serviceaccounts -n sample
         

There is a service account in addition to the default. The output resembles the following: 
         
         NAME         SECRETS   AGE
         default      0         15m
         sample-ksa   0         15m
         




#### Infrastructure repository

In a web browser, go to [GitHub](https://github.com/) and sign in to your account. Click the picture icon. Then click `Your organizations`. Choose you organization and click the `sample-infra` repository.

This repository has four branches: `cicd-trigger`, `dev`, `staging` and `prod`. It also contains four folders cicd-trigger, dev, staging and prod. The default branch is `cicd-trigger` and you can push the code to it while other branches have protection rules so, you can't push code directly to those branches. In order to push the code to those branches, you need to create a pull request. The `cicd-trigger` folder has code to create CI/CD resources for the application while `dev`, `staging` and `prod` folders have code to create infrastructure for different environments of the application.

#### Infrastructure trigger

  * In Google Cloud console:

[Go to the Cloud Build page](https://console.cloud.google.com/cloud-build/triggers)

There is a new trigger named `deploy-infra-sample`.

  * This trigger is connected to the repository `sample-infra` such that when a code push happens to this repository, the trigger is invoked and identifies the branch where the push happened and goes to the corresponding folder on that branch and runs Terraform there. For example, if the code is pushed to `cicd-trigger` branch, the trigger runs Terraform on cicd-trigger folder of cicd-trigger branch. Similarly, when a push happens to the `dev` branch, the trigger runs Terraform on dev folder of the dev branch and so forth.




#### Application repository

  * Go to [GitHub](https://github.com/) and pull up the repositories under your organization. There is a new repository with the name `sample`. This repository hosts the source code and steps to build containers in `Dockerfile`, `kustomize` configs that describe needed configurations of the application and `skaffold.yaml` that defines the deployment steps to be used by Cloud Deploy for CD.



### Create application CI/CD resources

Now that you've created the skeleton of the application, run the trigger `deploy-infra-sample` to create its CI/CD resources. You can either invoke the trigger manually using its webhook URL or by making a commit to the git repository `sample-infra`.

  1. To invoke the Cloud Build trigger, add a new line in a file in the repository. Then, push the changes:

     1. If you've never used Git in Cloud Shell, configure Git with your name and email address. Git uses this information to identify you as the author of the commits that you create in Cloud Shell:
            
            git config --global user.email "GITHUB_EMAIL_ADDRESS"
            git config --global user.name "GITHUB_USERNAME"

Replace the following:

        * `GITHUB_EMAIL_ADDRESS`: the email address associated with your GitHub account
        * `GITHUB_USERNAME`: the username associated with your GitHub account
     2. Clone the git repository `sample-infra`:
            
            git clone https://github.com/GITHUB_ORG/sample-infra
            
            cd sample-infra

Replace the following:

        * `GITHUB_ORG` with your GitHub organization.

The default branch cicd-trigger is checked out.

     3. Add a new line to the file env/cicd-trigger/main.tf, commit the change and push.
            
            echo "" >> env/cicd-trigger/main.tf
            

     4. Commit and push the changes:
            
            git add .
            git commit -m "A dummy commit to invoke the infrastrucutre trigger"
            git push
            cd ..
            

As soon as the changes are pushed, the Cloud Deploy trigger `deploy-infra-sample` is started.

  2. Monitor the status of the trigger:

[Go to Cloud Build history page](https://console.cloud.google.com/cloud-build/builds) to view the pipeline and wait for it to complete.




### Review application CICD resources

Review the various CI/CD resources created for the application.

  1. In the Google Cloud console:

[Go to the Cloud Build page](https://console.cloud.google.com/cloud-build/triggers) and view the `deploy-app-sample` trigger.

This is the CI pipeline trigger. It's connected to the application code repository `sample`. The trigger gets invoked when a push is made to the application repository and performs the build steps as defined in the trigger configuration. To view the steps that the trigger performs when invoked, click the trigger name and then click **OPEN EDITOR** button.

  2. [Go to the Artifact Registry page](https://console.cloud.google.com/artifacts) and view the new repository with the name `sample`.

This Artifact Repository stores the application's artifacts.

  3. [Go to the Cloud Deploy pipeline page](https://console.cloud.google.com/deploy/delivery-pipelines) and view the pipeline with the name `sample`. This is the continuous deployment pipeline that deploys the application on the GKE clusters.




## Deploy the application in the dev environment

The trigger `deploy-app-sample` is connected to the application repository named `sample`. You can either invoke the trigger manually, using the webhook URL, or through a push to the application repository.

  1. Add a new line in a file in the repository `sample` and push the changes to invoke the Cloud Build trigger:

     1. Clone the git repository `sample`:

In Cloud Shell:
            
            git clone https://github.com/GITHUB_ORG/sample
            
            cd sample

Replace `GITHUB_ORG` with your GitHub prganization.

     2. Add a new line to the `skaffold.yaml` file.
            
            echo "" >> skaffold.yaml
            

     3. Commit and push the changes:
            
            git add .
            git commit -m "A dummy commit to invoke CI/CD trigger"
            git push
            

     4. As soon as the changes are pushed, the Cloud Deploy trigger `deploy-app-sample` is started.

  2. Monitor the status of the trigger:

[Go to Cloud Build history page](https://console.cloud.google.com/cloud-build/builds) to view the pipeline and wait for it to complete.

The trigger executes the steps defined in its configuration. The first step is to build a docker image from the application code in the repository `sample`. The last step is to kick-off the Cloud Deploy pipeline that deploys the application to the dev GKE cluster.

  3. Check the deployment in dev cluster:

[Go to Cloud Deploy pipeline page](https://console.cloud.google.com/deploy/delivery-pipelines).

Click `sample` pipeline, the deployment to the dev GKE cluster has been started. Wait for it to complete.




**Verify that the application has been deployed successfully** :

  1. Get credentials to the development cluster.
         
         gcloud container clusters get-credentials gke-dev-us-central1 --location us-central1-a
         

  2. Tunnel into GKE cluster.
         
         gcloud container clusters get-credentials gke-dev-us-central1 --location us-central1-a && kubectl port-forward --namespace sample $(kubectl get pod --namespace sample --selector="deploy.cloud.google.com/delivery-pipeline-id=sample" --output jsonpath='{.items[0].metadata.name}') 8080:8080
         

  3. On the Cloud Shell toolbar, click

preview **Web Preview** , and then click **Preview on port 8080** : ![Cloud Shell toolbar commands.](https://docs.cloud.google.com/static/architecture/images/modern-cicd-gke-developer-workflow-web-preview.png)

The output is the following:
         
         Hello World!
         

  4. In Cloud Shell, press `CTRL+C` to end the port forward.




## Add a new feature to the application

When you develop a new feature, you need to quickly deploy your changes into development environment in order to test and iterate on them. In this tutorial, you use make changes in application code repository and deploy them to development environment.

  1. In Cloud Shell, change directory to already cloned `sample` repository:

  2. Update the application to output a different message:
         
         sed -i "s/Hello World/My new feature/g" main.py
         

  3. Commit and push the changes:
         
         git add .
         git commit -m "Changed the message"
         git push
         

As soon as the code is pushed to the GitHub repository, the webhook trigger `deploy-app-sample` gets kicked-off.

  4. Monitor the status of the trigger on [Cloud Build history page](https://console.cloud.google.com/cloud-build/builds) and wait for it to complete.

  5. [Go to Cloud Deploy pipeline page](https://console.cloud.google.com/deploy/delivery-pipelines)

Click `sample` pipeline, the deployment to the dev GKE cluster has been started. Wait for it to complete.




**Verify that the application has been deployed successfully** :

  1. Get credentials to the development cluster if you opened a new Cloud Shell:
         
         gcloud container clusters get-credentials gke-dev-us-central1 --zone us-central1-a
         

  2. Tunnel into GKE cluster:
         
         gcloud container clusters get-credentials gke-dev-us-central1 --zone us-central1-a && kubectl port-forward --namespace sample $(kubectl get pod --namespace sample --selector="deploy.cloud.google.com/delivery-pipeline-id=sample" --output jsonpath='{.items[0].metadata.name}') 8080:8080
         

  3. On the Cloud Shell toolbar, click

preview **Web Preview** , and then click **Preview on port 8080** :

![Cloud Shell toolbar commands.](https://docs.cloud.google.com/static/architecture/images/modern-cicd-gke-developer-workflow-web-preview.png)

The output is the following:
         
         My new feature!
         

  4. In Cloud Shell, press `CTRL+C` to end the port forward.




## Promote your change to the staging and productions clusters

Before promoting the application to staging and production environments, you need to create the landing zone for the application in the GKE clusters for those environments. When you onboarded the application, the landing zone for dev was automatically created in dev GKE cluster by adding code to `acm-gke-infrastructure-repo` in the dev branch.

### Create landing zone in staging and prod GKE clusters

  1. Create landing zone in staging GKE cluster: You need to create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) from dev to staging branch in `acm-gke-infrastructure-repo` and merge it.

     1. Go to GitHub and traverse to the repository `acm-gke-infrastructure-repo`. Click `Pull requests` and then `New pull request` button. In the **Base** menu, choose **staging** and in the **Compare** menu, choose **dev**. Click the `Create pull request` button.

     2. Typically, someone who has access to the repository reviews the changes and then merge the PR to make sure only the intended changes are being promoted to the staging environment. To let the individuals try out the reference architecture, the branch protection rules have been relaxed so that the repository administrator are able to bypass the review and merge the PR. If you are an administrator on the repository, merge the pull request. Otherwise, get the administrator to merge it.

Config Sync syncs the changes that arrive on staging branch of the repository `acm-gke-infrastructure-repo` with the staging GKE cluster that results in landing zone creation for the application on the staging GKE cluster.

  2. Create landing zone in production GKE clusters: You need to create a pull request from staging to prod branch and merge it.

     1. Click `Pull requests` and then `New pull request` button. In the **Base** menu, choose **prod** and in the **Compare** menu, choose **staging**. Click the `Create pull request` button.

     2. If you are an administrator on the repository, merge the pull request. Otherwise, get the administrator to merge it.

Config Sync syncs the changes that arrive on prod branch of the repository `acm-gke-infrastructure-repo` with the production GKE clusters that results in landing zone creation for the application on production GKE clusters.




### Promote the changes from dev to staging

Now that you've created the landing zone for the application in staging and prod GKE clusters, promote the application from dev to staging environment.

  1. Find the latest release name and save it as an environment variable:
         
         export RELEASE=$(gcloud deploy targets describe dev --region=us-central1 --format="json" | jq -r '."Active Pipeline"[0]."projects/PROJECT_ID/locations/us-central1/deliveryPipelines/sample"."Latest release"' | awk -F '/' '{print $NF}')
          

Replace `PROJECT_ID` with your Google Cloud project ID.

Verify the environment variable has been set:
         
         echo $RELEASE
           

  2. In Cloud Shell, run the following command to trigger promotion of the release from dev to staging environment:
         
         gcloud deploy releases promote --release=$RELEASE --delivery-pipeline=sample  --region=us-central1 --to-target=staging --quiet
          

  3. Check staging deployment:

[Go to Cloud Deploy pipeline page](https://console.cloud.google.com/deploy/delivery-pipelines)

Click `sample` pipeline, the deployment to the staging GKE cluster has been started. Wait for it to complete.

  4. Verify the staging deployment has happened successfully:

     1. Get credentials to the staging cluster:
            
            gcloud container clusters get-credentials gke-staging-us-central1 --location us-central1-a
            

     2. Tunnel into GKE cluster:
            
            gcloud container clusters get-credentials gke-staging-us-central1 --location us-central1-a && kubectl port-forward --namespace sample $(kubectl get pod --namespace sample --selector="deploy.cloud.google.com/delivery-pipeline-id=sample" --output jsonpath='{.items[0].metadata.name}') 8080:8080
            

     3. On the Cloud Shell toolbar, click

preview **Web Preview** , and then click **Preview on port 8080** :

![Cloud Shell toolbar commands.](https://docs.cloud.google.com/static/architecture/images/modern-cicd-gke-developer-workflow-web-preview.png)

The output is the following:
            
            My new feature!
            

     4. In Cloud Shell, press `CTRL+C` to end the port forward.




### Promote the changes from staging to prod

Now, promote the release from staging to prod. You have two production clusters and Cloud Deploy has a target for each of them named prod1 and prod2 respectively.

  1. In Cloud Shell, run the following command to trigger promotion of the release from staging to prod1 cluster:
         
         gcloud deploy releases promote --release=$RELEASE --delivery-pipeline=sample  --region=us-central1 --to-target=prod1 --quiet
          

  2. Release to prod clusters require approval so the rollout waits until you approve it. To view it:

[Go to Cloud Deploy pipeline page](https://console.cloud.google.com/deploy/delivery-pipelines)

Click `sample` pipeline. The rollout to prod1 requires approval and clouddeploy.approver role is needed to approve the rollout. Since, you are the owner of the project, you have access to approve the release.

  3. Approve the release to prod1:

Run the following command to fetch the name of the rollout pending approval and save it in an environment variable:
         
         export ROLLOUT=$(gcloud deploy targets describe prod1 --region=us-central1 --format="json" | jq -r '."Pending Approvals"[]' | awk -F '/' '{print $NF}')
          

Approve the release:
         
         gcloud deploy rollouts approve $ROLLOUT --delivery-pipeline=sample --region=us-central1 --release=$RELEASE --quiet
          

  4. After the approval is given, prod1 release starts. Monitor the progress on [Cloud Deploy pipeline page](https://console.cloud.google.com/deploy/delivery-pipelines).

  5. After prod1 deployment is completed, kick-off prod2 release.
         
         gcloud deploy releases promote --release=$RELEASE --delivery-pipeline=sample  --region=us-central1 --to-target=prod2 --quiet
          

  6. Release to prod2 also requires approval. Approve the release to prod2 cluster:

Run the following command to fetch the name of the rollout pending approval and save it in an environment variable:
         
         export ROLLOUT=$(gcloud deploy targets describe prod2 --region=us-central1 --format="json" | jq -r '."Pending Approvals"[]' | awk -F '/' '{print $NF}')
          

Approve the release:
         
         gcloud deploy rollouts approve $ROLLOUT --delivery-pipeline=sample --region=us-central1 --release=$RELEASE --quiet
          

**Note:** Cloud Deploy lets you do parallel deployments in multiple GKE clusters so you can deploy to multiple production clusters simultaneously. See [Parallel deployment with Cloud Deploy](https://docs.cloud.google.com/deploy/docs/parallel) for details.
  7. After the approval is given, prod2 release starts. Monitor the progress on [Cloud Deploy pipeline page](https://console.cloud.google.com/deploy/delivery-pipelines).

  8. Verify the deployment in production cluster was successful after the Cloud Deploy pipelines in prod1 and prod2 are completed.

     1. There is [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress) created in production clusters and you use a load balancer to access the prod application. This Multi Cluster Ingress configurations are created using YAML files k8s/prod/mci.yaml and k8s/prod/mcs.yaml in the repository `sample`. When you send request to the IP address of the load balancer, Multi Cluster Ingress forwards the request to one of the two instances of the application running in two different GKE clusters.

     2. List the forwarding rule associated to the load balancer to find the IP address.
            
            gcloud compute forwarding-rules list

     3. The output resembles the following: 
            
            NAME: mci-qqxs9x-fw-sample-sample-ingress
            REGION:
            IP_ADDRESS: 34.36.123.118
            IP_PROTOCOL: TCP
            TARGET: mci-qqxs9x-sample-sample-ingress
            

     4. Open a web browser and enter the following in the URL: 
            
            http://IP_ADDRESS:80

Replace `IP_ADDRESS` with IP address of the load balancer.

The output is the following:
            
            My new feature!
            

This confirms the application is deployed as expected in production clusters.




### Test resiliency of the application

In this section you test the resiliency of the application running in production by re-starting one of the two production GKE clusters' nodes without impacting the application.

The application in production uses multi-cluster ingress and is accessible through a load balancer IP. When the application is accessed through that IP, multi-cluster ingress routes it to one of the two instances of the application running on two different GKE clusters. When one of the GKE clusters is unhealthy and the application instance running on it can't be reached, the multi-cluster ingress keeps sending the traffic to the healthy instance of the application running on the other GKE cluster. This makes the cluster outage invisible to the end user and the application continuously serves the requests.

To test the resiliency:

  1. Find the node pool of the production GKE clusters running in us-west1. 
         
         gcloud container clusters describe gke-prod-us-west1 --location=us-west1-a --format=json | jq ".nodePools[0].instanceGroupUrls[]" | tr '"' ' ' |  awk -F '/' '{for(i=NF-2; i<=NF; i=i+2) printf ("%s ",$i); print  ""}'

  2. The output resembles the following:
         
         us-west1-b gke-gke-prod-us-west1-node-pool-01-6ad4e1ed-grp
         us-west1-c gke-gke-prod-us-west1-node-pool-01-98407373-grp
         

The output has two columns, first column is the zone and the second column is the name of the instance group associated with the node pool of the production GKE cluster in us-west1 region.

  3. Restart the instance-group corresponding to the node pools:
         
         gcloud compute instance-groups managed rolling-action restart INSTANCE_GROUP_1  --zone=ZONE_1 --max-unavailable=100%
         
          gcloud compute instance-groups managed rolling-action restart INSTANCE_GROUP_2  --zone=ZONE_2 --max-unavailable=100%

Replace `INSTANCE_GROUP_1` with the name of the first instance group.

Replace `ZONE_1` with the zone of the first instance group.

Replace `INSTANCE_GROUP_2` with the name of the second instance group.

Replace `ZONE_2` with the zone of the second instance group.

  4. Check the status of the instance group.

[Go to Instance groups page](https://console.cloud.google.com/compute/instanceGroups/list)

The two instance groups are being rebooted while the other groups have a green tickmark against them.

![Status of the instance groups.](https://docs.cloud.google.com/static/architecture/images/modern-cicd-gke-developer-workflow-instance-groups.png)

  5. Open a web browser and enter the following in the URL: 
         
         http://IP_ADDRESS:80

Replace `IP_ADDRESS` with IP address of the load balancer.

Even when one of the two GKE clusters is down, the application is available and the output is the following:
         
         My new feature!
          

This shows that your application is resilient and highly available.




### Manage the application

When you created this application from the application factory, you got separate git repos, infrastrucutre and CI/CD pipelines for the application. You used these resources to deploy the application and add a new feature. In order to manage the application further, you only need to interact with these git repos and the pipeline without needing to update the application factory. You can customize the application's pipelines and git repositories based on your requirements. As an application owner, you can define who gets access to the pipelines and git repos of your application to manage it.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn about [best practices for setting up identity federation](https://docs.cloud.google.com/solutions/migrating-consumer-accounts-to-cloud-identity-or-g-suite-best-practices-federation).
  * Read [Kubernetes and the challenges of continuous software deployment](https://docs.cloud.google.com/solutions/addressing-continuous-delivery-challenges-in-a-kubernetes-world).
  * Learn about [hybrid and multi-cloud monitoring and logging patterns](https://docs.cloud.google.com/solutions/hybrid-and-multi-cloud-monitoring-and-logging-patterns).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2023-09-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2023-09-11 UTC."],[],[]] 
