---
url: https://docs.cloud.google.com/eventarc/standard/docs/gke/quickstart-cal/
title: Quickstart: Receive events using Cloud Audit Logs (Google Cloud CLI) \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:04.696829+00:00
---

# Quickstart: Receive events using Cloud Audit Logs (Google Cloud CLI)  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/gke/quickstart-cal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Receive events using Cloud Audit Logs (gcloud CLI)

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This quickstart shows you how to set up a Google Kubernetes Engine (GKE) service as a destination to receive events from Cloud Storage using Eventarc.

**Note:** Support for GKE as an Eventarc destination includes the public endpoints of private and public services running in a GKE cluster.

In this quickstart, you will:

  1. Set up a service account so that Eventarc can pull events and forward it to the target.
  2. Create a Cloud Storage bucket to be the event source.
  3. Create a GKE cluster.
  4. Initialize GKE destinations in Eventarc.
  5. Deploy a GKE service that receives events.
  6. Create an Eventarc trigger that sends events from Cloud Storage to the GKE service.
  7. Upload a file to the Cloud Storage bucket to generate an event and view the event in the GKE pod logs.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Update Google Cloud CLI components: 
         
         gcloud components update

  13. Enable the Eventarc, Resource Manager, and Google Kubernetes Engine APIs: 
         
         gcloud services enable eventarc.googleapis.com \
             cloudresourcemanager.googleapis.com \
             container.googleapis.com

  14. Set the configuration variables used in this quickstart: 
         
         PROJECT_ID=$(gcloud config get-value project)
         TRIGGER_SA=eventarc-sa
         CLUSTER_NAME=events-cluster
         SERVICE_NAME=hello-gke

  15. If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

If you are not the project creator, required permissions must be granted on the project to the appropriate _principal_. For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads). For more information, see the [Roles and permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions) page for your event destination.

#### Required permissions

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

     * [Eventarc Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`)
     * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
     * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  16. Make note of the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) as you will attach it to an Eventarc trigger to represent the identity of the trigger for testing purposes. This service account is automatically created after enabling or using a Google Cloud service that uses Compute Engine, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
         
         gcloud projects describe PROJECT_ID --format='value(projectNumber)'

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  17. Grant the [Pub/Sub Subscriber role](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.subscriber) (`roles/pubsub.subscriber`) on the project to the Compute Engine default service account so that the Eventarc trigger can pull events from Pub/Sub. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/pubsub.subscriber

  18. Grant the [Eventarc Event Receiver role](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver) (`roles/eventarc.eventReceiver`) on the project to the Compute Engine default service account so that the Eventarc trigger can receive events from event providers. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/eventarc.eventReceiver

  19. If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021, to support authenticated Pub/Sub push requests, grant the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) to the service agent. Otherwise, this role is granted by default: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountTokenCreator

  20. For Google Cloud Storage, enable log types for these services: **Admin Read** , **Data Read** , and **Data Write** : 
     1. Read your project's IAM policy and store it in a file: 
            
            gcloud projects get-iam-policy PROJECT_ID > /tmp/policy.yaml

     2. Edit your policy in `/tmp/policy.yaml`, adding or changing *only* the Data Access audit logs configuration. Caution: You must preserve the `bindings:` and `etag:` sections without changes. Failure to do so might cause your project to become unusable. 
            
            auditConfigs:
              - auditLogConfigs:
                - logType: ADMIN_READ
                - logType: DATA_WRITE
                - logType: DATA_READ
                service: storage.googleapis.com
              bindings:
              - members:
                - user:EMAIL_ADDRESS
                role: roles/owner
              etag: BwW_bHKTV5U=
              version: 1

Replace `EMAIL_ADDRESS` with your email address.
     3. Write your new IAM policy: 
            
            gcloud projects set-iam-policy PROJECT_ID /tmp/policy.yaml

If the preceding command reports a conflict with another change, then repeat these steps, starting with reading the project's IAM policy. 



## Create a Cloud Storage bucket

This quickstart uses Cloud Storage as the event source. Create a Cloud Storage bucket:
    
    
    gcloud storage buckets create  gs://events-quickstart-$(gcloud config get-value project) --location=us-central1

After the event source is created, you can deploy the event receiver service on GKE.

## Create a GKE cluster

A GKE [cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) consists of at least one cluster control plane machine and multiple worker machines called nodes. Nodes are [Compute Engine virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/instances) that run the Kubernetes processes necessary to make them part of the cluster. You deploy applications to clusters, and the applications run on the nodes.

Create an Autopilot cluster named `events-cluster`:
    
    
    gcloud container clusters create-auto $CLUSTER_NAME --region us-central1

It might take several minutes for the creation of the cluster to complete. Once the cluster is created, the output should be similar to the following:
    
    
    Creating cluster events-cluster...done.
    Created [https://container.googleapis.com/v1/projects/MY_PROJECT/zones/us-central1/clusters/events-cluster].
    [...]
    STATUS: RUNNING
    

This creates a GKE cluster named `events-cluster` in a project with a Google Cloud project ID of `MY_PROJECT`.

## Enable GKE destinations

For each trigger that targets a GKE service, Eventarc creates an event forwarder component that pulls events from Pub/Sub and forwards it to the target. To create the component and manage resources in the GKE cluster, grant permissions to the Eventarc service agent:

  1. Enable GKE destinations for Eventarc:
         
         gcloud eventarc gke-destinations init

  2. At the prompt to bind the required roles, enter `y`.

The following roles are bound to the service account:

     * `compute.viewer`
     * `container.developer`
     * `iam.serviceAccountAdmin`



## Create a GKE service destination

Deploy a GKE service that will receive and log events using a prebuilt image, `us-docker.pkg.dev/cloudrun/container/hello`:

  1. Kubernetes uses a YAML file called [`kubeconfig`](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) to store cluster authentication information for `kubectl`. Update the `kubeconfig` file with credentials and endpoint information to point `kubectl` at the GKE cluster:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --region us-central1
         

  2. Create a Kubernetes deployment:
         
         kubectl create deployment $SERVICE_NAME \
             --image=us-docker.pkg.dev/cloudrun/container/hello
         

  3. Expose it as a Kubernetes service:
         
         kubectl expose deployment $SERVICE_NAME \
             --type ClusterIP --port 80 --target-port 8080
         




## Create an Eventarc trigger

When you upload a file to Cloud Storage, the Eventarc trigger sends events from Cloud Storage to the `hello-gke` GKE service.

  1. Create a Cloud Audit Logs trigger:
         
         gcloud eventarc triggers create my-gke-trigger \
             --location="us-central1" \
             --destination-gke-cluster="events-cluster" \
             --destination-gke-location="us-central1" \
             --destination-gke-namespace="default" \
             --destination-gke-service="hello-gke" \
             --destination-gke-path="/" \
             --event-filters="type=google.cloud.audit.log.v1.written" \
             --event-filters="serviceName=storage.googleapis.com" \
             --event-filters="methodName=storage.objects.create" \
             --service-account="PROJECT_NUMBER-compute@developer.gserviceaccount.com"
         

This creates a trigger called `my-gke-trigger`.

  2. Confirm that the trigger was successfully created:
         
         gcloud eventarc triggers list

**Note:** It can take up to two minutes for the trigger to be fully functional.

The output should be similar to the following:
         
         NAME: my-gke-trigger
         TYPE: google.cloud.audit.log.v1.written
         DESTINATION: GKE: hello-gke
         ACTIVE: By 20:39:43
         LOCATION: us-central1
         




## Generate and view an event

Upload a text file to Cloud Storage to generate an event and trigger the GKE service. You can then view the event's message in the pod logs.

  1. Upload a text file to Cloud Storage:
         
         echo "Hello World" > random.txt
         gcloud storage cp random.txt gs://events-quickstart-$(gcloud config get-value project)/random.txt

The upload generates an event and the GKE pod logs the event's message.

  2. To view the event message:

     1. Find the pod ID:
            
            kubectl get pods

The output should be similar to the following:
            
            NAME                                         READY   STATUS             RESTARTS   AGE
            hello-gke-645964f578-2mjjt                   1/1     Running            0          35s

Copy the `NAME` of the pod to use in the next step.

     2. Check the logs of the pod:
            
            kubectl logs NAME

Replace `NAME` with the name of the pod you copied.

     3. Look for a log entry similar to:
            
            2022/02/24 22:23:49 Hello from Cloud Run! The container started successfully and is listening for HTTP requests on $PORT
            {"severity":"INFO","eventType":"google.cloud.audit.log.v1.written","message":"Received event of type google.cloud.audit.log.v1.written. [...]}
            




## Clean up

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created.

You can:

  1. [Delete the Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets).

  2. [Delete the Eventarc trigger](https://docs.cloud.google.com/eventarc/docs/managing-triggers#deleting_triggers).

  3. [Delete the GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster#deleting_a_cluster).




Alternatively, you can delete your Google Cloud project to avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project.

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

If you plan to explore multiple tutorials and quickstarts, reusing projects can help you avoid exceeding project quota limits.

## What's next

[Receive events using Pub/Sub (Google Cloud CLI)](https://docs.cloud.google.com/eventarc/standard/docs/gke/quickstart-pubsub)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
