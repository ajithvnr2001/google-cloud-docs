---
url: https://docs.cloud.google.com/run/docs/configuring/configure-service-health/
title: Automate cross-region failover with Cloud Run service health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:35.150386+00:00
---

# Automate cross-region failover with Cloud Run service health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/configure-service-health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Automate cross-region failover with Cloud Run service health Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure and deploy a highly available, multi-region Cloud Run service with automated failover and failback capabilities.

Cloud Run service health exposes the aggregate health of your service in each region using Serverless Network Endpoint Groups (NEGs).

  * To route public (external) traffic, you configure service health with a global external Application Load Balancer.

  * To route private (internal) traffic, you configure service health with a [cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-serverless).




## How it works

Automated failover routes incoming requests from a global external Application Load Balancer or cross-region internal Application Load Balancer through regional serverless NEGs to your Cloud Run services. Individual container instances run readiness probes, which Cloud Run aggregates to determine the overall health status of each regional service.

A Cloud Run service in a region is healthy and receives traffic if 60% or more of its instances pass their readiness probes. If a region becomes unhealthy, the load balancer automatically reroutes traffic to a healthy region. Once the unhealthy region recovers, the load balancer gradually restores traffic to it.

## Limitations

The following limitations apply to Cloud Run service health:

  * You must configure at least one service-level or revision-level [minimum instance](https://docs.cloud.google.com/run/docs/configuring/min-instances) per region to calculate health. You can also use the [Container instance count](https://docs.cloud.google.com/run/docs/monitoring#built-in_metrics) metric in Cloud Monitoring to estimate the required minimum instances for your regions.
  * Failovers require at least two services from different regions. Otherwise, if one service fails, the error message `no healthy upstream` is displayed.
  * You can't configure a URL mask or tags in serverless NEGs.
  * If a Cloud Run service is deleted, Cloud Run doesn't report an unhealthy status to the load balancer.
  * Starting a new instance won't count the first readiness probe, so a request might briefly route to a newly started service before becoming unhealthy.
  * Cloud Run service health is computed across all instances. Revisions without probes and newly started instances that haven't completed their first readiness probe are treated as unknown. During a transition of all traffic between revisions, service health can briefly report `UNKNOWN` while new instances start and complete their first readiness probe. The load balancer treats unknown instances as healthy.
  * Service health computation might yield inaccurate results if instances are rapidly crashing.



## Best practices

You can use a combination of readiness probes, traffic splitting, and minimum instances to perform safe, gradual rollouts. This lets you verify the health of a new revision in a single "canary" region before promoting it, ensuring that the load balancer only sends traffic to healthy regional backends.

When configuring probes on your own application, add an HTTP/1 endpoint (the Cloud Run default, not HTTP/2) in your service code to respond to the probe. The endpoint name (for example, `/startup`, `/health`, or `/are_you_ready`) must match the `path` in the probe configuration. HTTP health check endpoints are externally accessible and follow the same principles as any other externally exposed HTTP service endpoints.

### Recommended rollout process

You can roll out a service revision on an existing Cloud Run service that's not using a readiness probe or Cloud Run service health. Follow this process one region at a time to safely deploy a new revision:

  1. Deploy the new revision in a single "canary" region with a readiness probe configured.

  2. Send a small amount of traffic (for example, 1%) to the new revision.

  3. Use non-zero minimum instances at the service level, rather than at the revision level.

  4. Check the readiness probe metric (`run.googleapis.com/container/instance_count_with_readiness`) to ensure that new instances are healthy.

  5. In incremental steps, increase the traffic percentage to the new revision. As you ramp up, monitor the regional Cloud Run service health metric (`run.googleapis.com/service_health_count`), which is used by the load balancer. Cloud Run service health reports `UNKNOWN` until enough traffic is routed to the new revision.

  6. Once the revision receives 100% of traffic and the regional Cloud Run service health is stable and healthy, repeat this process for all other regions.




For services that already use Cloud Run service health, you can run a two-step rollout in parallel across regions to avoid reporting `UNKNOWN`:

  1. Route a portion of traffic to the new revision. Wait for new instances to start and pass readiness probes.

  2. Route 100% of traffic to the new revision.




## Tutorial: Configure automated failover

This tutorial guides you through deploying a sample Go application to two regions, setting up a global external Application Load Balancer with serverless NEGs, and testing automated failover.

In this tutorial, you will:

  1. Prepare the sample application
  2. Deploy Cloud Run services in two regions with readiness probes
  3. Set up a global external Application Load Balancer
  4. Add your services through the serverless NEG
  5. Test failover



In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Build](https://cloud.google.com/build)
  * [Compute Engine](https://docs.cloud.google.com/compute)
  * [ Cloud Load Balancing](https://cloud.google.com/load-balancing)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Storage](https://cloud.google.com/storage)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Artifact Registry, Cloud Build, Cloud Run Admin API, Network Services API, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,cloudbuild.googleapis.com,compute.googleapis.com,run.googleapis.com,networkservices.googleapis.com)

  7. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  8. Update components: 
         
         gcloud components update

  9. Set the configuration variables used in this tutorial: 
         
         PROJECT_ID= gcloud config set core/project PROJECT_ID
         PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         SERVICE=health-example
         REGION_A=us-west1
         REGION_B=europe-west1

Replace PROJECT_ID with your Google Cloud project ID. 



### Set required roles

To deploy from source with build, you or your administrator must grant the Cloud Build service account the following IAM roles.

#### Click to view required roles for the Cloud Build service account

Cloud Build automatically uses the [Compute Engine default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) as the default Cloud Build service account to build your source code and Cloud Run resource, unless you override this behavior. For Cloud Build to build your sources, ask your administrator to grant [Cloud Run Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`) to the Compute Engine default service account on your project:
    
    
      gcloud projects add-iam-policy-binding PROJECT_ID \
          --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
          --role=roles/run.builder
      

Replace `PROJECT_NUMBER` with your Google Cloud project number, and `PROJECT_ID` with your Google Cloud project ID. For detailed instructions on how to find your project ID, and project number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

Granting the Cloud Run builder role to the Compute Engine default service account takes a couple of minutes to [propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To get the permissions that your [service identity](https://docs.cloud.google.com/run/docs/configuring/services/service-identity) needs to access the file and Cloud Storage bucket, ask your administrator to grant the service identity the [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) role. For more details on Cloud Storage roles and permissions, see [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Prepare the sample application

To retrieve the code sample for use:

  1. Clone the sample repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples
         

  2. Change to the directory that contains the Cloud Run sample code:
         
         cd golang-samples/run/service-health
         


**Note:** If you use your own application, add an HTTP/1 endpoint (the Cloud Run default, not HTTP/2) in your service code to respond to the probe. The endpoint name (for example, `/startup`, `/health`, or `/are_you_ready`) must match the `path` in the probe configuration. HTTP health check endpoints are externally accessible and follow the same principles as any other externally exposed HTTP service endpoints.

### Deploy the Cloud Run service in two regions with readiness probes

Failovers require at least [two services](https://docs.cloud.google.com/run/docs/deploying-source-code) from different regions. To deploy your services from source in two different regions with readiness probes, run the following commands. If you prefer to use Terraform, see [Deploy a multi-region service](https://docs.cloud.google.com/run/docs/multiple-regions#deploy) and ensure you add the [readiness probe configuration](https://docs.cloud.google.com/run/docs/configuring/healthchecks#readiness-probes).

  1. Deploy your service `health-example` in `us-west1` and `europe-west1` from the source directory. You need at least one minimum instance to configure service health with readiness probes:
         
         gcloud run deploy $SERVICE \
         --source=. \
         --regions=$REGION_A,$REGION_B \
         --min=10 \
         --readiness-probe httpGet.path="/are_you_ready"
         

  2. Respond to any prompts to install required APIs by responding `y` when prompted. You only need to do this once for a project. Respond to other prompts by supplying the platform and region, if you haven't set defaults for these as described in the Before you begin section.




### Set up a global external Application Load Balancer

To set up a global external Application Load Balancer to route traffic between `us-west1` and `europe-west1`, follow these steps. If you prefer to provision your load balancer using Terraform, see [Create a global external Application Load Balancer](https://docs.cloud.google.com/run/docs/multiple-regions#create-global-external-lb).

  1. Create a backend service:
         
         gcloud compute backend-services create $SERVICE-bs \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --global
         

  2. Set up a [global static external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses) to reach your load balancer:
         
         gcloud compute addresses create $SERVICE-ip \
           --network-tier=PREMIUM \
           --ip-version=IPV4 \
           --global
         

  3. Create a URL map to route incoming requests to the backend service:
         
         gcloud compute url-maps create $SERVICE-lb \
           --default-service $SERVICE-bs
         

  4. Create a target HTTP proxy to route requests to your URL map:
         
         gcloud compute target-http-proxies create $SERVICE-hp \
         --url-map=$SERVICE-lb
         

  5. Create a forwarding rule to route incoming requests to the proxy:
         
         gcloud compute forwarding-rules create $SERVICE-fr \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --network-tier=PREMIUM \
           --address=$SERVICE-ip \
           --target-http-proxy=$SERVICE-hp \
           --global \
           --ports=80
         




### Add your services through a serverless NEG

To add the services you deployed in `us-west1` and `europe-west1` using the Serverless NEG, follow these steps. If you prefer to provision your serverless NEGs using Terraform, see [Configure regional network endpoint groups](https://docs.cloud.google.com/run/docs/multiple-regions#serverless-neg).

  1. Create a [serverless network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) for your Cloud Run service in `us-west1` and `europe-west1`:
         
         gcloud compute network-endpoint-groups create $SERVICE-neg-$REGION_A \
             --region $REGION_A \
             --network-endpoint-type=serverless \
             --cloud-run-service=$SERVICE
         
         
         gcloud compute network-endpoint-groups create $SERVICE-neg-$REGION_B \
             --region $REGION_B \
             --network-endpoint-type=serverless \
             --cloud-run-service=$SERVICE
         

  2. Add the serverless NEG as a backend to the backend services in `us-west1` and `europe-west1`:
         
         gcloud compute backend-services add-backend $SERVICE-bs \
             --global \
             --network-endpoint-group=$SERVICE-neg-$REGION_A \
             --network-endpoint-group-region=$REGION_A
         
         
         gcloud compute backend-services add-backend $SERVICE-bs \
             --global \
             --network-endpoint-group=$SERVICE-neg-$REGION_B \
             --network-endpoint-group-region=$REGION_B
         




For additional configuration options, see [Set up a global external Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless#additional_configuration_options).

### Report regional health status

To aggregate regional Cloud Run service health and report a healthy or unhealthy status to the load balancer, perform the following steps:

  1. Deploy a Cloud Run service revision in multiple regions with one or more [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instancesj). Run the following command to use the readiness probe that you configured in the previous step:
         
         gcloud run deploy SERVICE_NAME \
         --regions=REGION_A,REGION_B \
         --min=MIN_INSTANCES

Replace the following:

     * SERVICE_NAME: the name of the service.
     * REGION_A, REGION_B: different regions for your service revision. For example, set REGION_A to `us-central1` and REGION_B to `europe-west1`.
     * MIN_INSTANCES: the number of container instances to be kept warm, ready to receive requests. You must set the minimum value to 1 or more.
  2. Configure a [gRPC or HTTP readiness probe](https://docs.cloud.google.com/run/docs/configuring/healthchecks#readiness-probes) set up on each container instance.

  3. Configure a global external Application Load Balancer or [cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-serverless) to shift traffic away from unhealthy regions.

  4. Set up [Serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless) for each Cloud Run service in each region.

  5. Configure a backend service to connect with serverless NEGs.




Learn how to [deploy a sample Cloud Run application to two regions with readiness probes](https://docs.cloud.google.com/run/docs/tutorials/configure-service-health).

### Test and verify failover

To test failover for ensuring the reliability and resilience of your Cloud Run services, follow these steps:

  1. Run the following command to get your load balancer's IP address:
         
         LBIP=$(gcloud compute addresses describe $SERVICE-ip --global --format='value(address)')
         

  2. Optional: Send a request to your load balancer if your services require authentication:
         
         curl  -H "Authorization: Bearer $(gcloud auth print-identity-token)" $LBIP
         

  3. Obtain the value of the LBIP variable by running the `echo $LBIP` command. This outputs the load balancer's IP address. For example, `11.22.33.44`

  4. To test a failover, navigate to the `http://LOAD_BALANCER_IP` URL where LOAD_BALANCER_IP is the value you obtained in the previous step. Click the toggle button for your region in the **Serving Regions** section. This designates the healthy region and the instance serving traffic:

![Automate cross-regional failover with Cloud Run service health](https://docs.cloud.google.com/run/docs/images/service-health-tutorial.png)


**Success:** You deployed a highly available, multi-region Cloud Run service with automated failover and failback for external traffic.

### Monitor health checks

After you set up Cloud Run service health, serverless NEGs collect the Cloud Monitoring service health metric. You can view the health status for the existing regional services.

If a service in a region is unhealthy, the load balancer diverts traffic from the unhealthy region to a healthy region. Traffic recovers after the region becomes healthy again.

### Use authenticated Pub/Sub push subscriptions with multi-region deployment

A Pub/Sub service by default delivers messages to push endpoints in the same Google Cloud region where the Pub/Sub service stores the messages. For a workaround to this behavior, refer to [Using an authenticated Pub/Sub push subscription with a multi-region Cloud Run deployment](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless#pubsub).

### Alternative: Configure manual failover

If you need to manually configure traffic to fail over to a healthy region without relying on probes, modify the global external Application Load Balancer URL map.

  1. To update the global external Application Load Balancer URL map, remove the NEG from the backend service, using the `--global` flag:
         
         gcloud compute backend-services remove-backend BACKEND_NAME \
         --network-endpoint-group=NEG_NAME \
         --network-endpoint-group-region=REGION \
         --global
         

Replace the following:

     * `BACKEND_NAME`: The name of the backend service.
     * `NEG_NAME`: The name of the network endpoint group resource, for example, `myservice-neg-uscentral1`.
     * `REGION`: The region where the NEG was created and where you want to remove your service from. For example, `us-central1,asia-east1`.
  2. To confirm that a healthy region is now serving traffic, navigate to https://`<domain-name>`.




To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this tutorial.

### Delete the project

If you created a new project for this tutorial, delete the project. If you used an existing project and need to keep it without the changes you added in this tutorial, delete resources that you created for the tutorial.

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete tutorial resources

  1. Delete the Cloud Run service you deployed in this tutorial. Cloud Run services don't incur costs until they receive requests.

To delete your Cloud Run service, run the following command:
         
         gcloud run services delete SERVICE-NAME

Replace SERVICE-NAME with the name of your service.

You can also delete Cloud Run services from the [Google Cloud console](https://console.cloud.google.com/run).

  2. Remove the `gcloud` default region configuration you added during tutorial setup:
         
         gcloud config unset run/region
         

  3. Remove the project configuration:
         
         gcloud config unset project
         




* * *

## What's next

  * Learn more about [Configuring health checks for Cloud Run services](https://docs.cloud.google.com/run/docs/configuring/healthchecks).
  * Deep dive into [global external Application Load Balancer setup with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless).
  * Explore multi-region configurations in other products like [Spanner Multi-region](https://docs.cloud.google.com/spanner/docs/instance-configurations#multi-region-configurations) and [Cloud Storage Locations](https://docs.cloud.google.com/storage/docs/locations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
