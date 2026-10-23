---
url: https://docs.cloud.google.com/run/docs/deploy-functions/
title: Deploy a Cloud Run function \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:09.324903+00:00
---

# Deploy a Cloud Run function  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/deploy-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Deploy a Cloud Run function Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to deploy and modify a Cloud Run function. For an example walkthrough of deploying a Hello World function, see [Deploy a sample function](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console).

Cloud Run function deployments automatically use Google Cloud's buildpacks and Cloud Build to build container images from your function's source code. You don't need to install Docker on your machine or set up buildpacks or Cloud Build.

Cloud Run function deployments also use Artifact Registry to store artifacts and manage container images. Artifact Registry automatically creates the Artifact Registry repository called `cloud-run-source-deploy`, if your project hasn't already created one with this name.

If you have existing functions and need to use the `gcloud functions deploy` command, the Cloud Functions v2 API, or the `google_cloudfunctions2_function` Terraform configuration for backward compatibility, see [Deploy functions with the `gcloud functions deploy` command](https://docs.cloud.google.com/functions/docs/deploy).

## Before you begin

  1. Make sure you have set up a new project for Cloud Run, as described in the [setup](https://docs.cloud.google.com/run/docs/setup) page.

  2. Enable the Artifact Registry, Cloud Build, Cloud Run Admin API, and Cloud Logging APIs:
         
         gcloud services enable artifactregistry.googleapis.com \
               cloudbuild.googleapis.com \
               run.googleapis.com \
               logging.googleapis.com
         

Optionally, enable the Eventarc API to use event triggers:
         
         gcloud services enable eventarc.googleapis.com
         

  3. If you are under a domain restriction organization policy [restricting](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) unauthenticated invocations for your project, you will need to access your deployed service as described under [Testing private services](https://docs.cloud.google.com/run/docs/triggering/https-request#testing-private).




### Required roles

To deploy Cloud Run functions, you or your administrator must grant the following IAM roles to the deployer account and the service account:

#### Click to view required roles for the deployer account

To get the permissions that you need to build and deploy from source, ask your administrator to grant you the following IAM roles:

  * [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`) on your project
  * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on your project
  * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Cloud Run service identity



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

#### Click to view required roles for the service account if using Eventarc

Optionally, if you are using Eventarc, grant the following roles to your service account:

  * [Cloud Build Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Cloud Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Create Service Accounts](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Cloud Run Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) (`roles/run.invoker`)
  * [Eventarc Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`)
  * [Project IAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting specific roles for your Eventarc triggers, see [Roles and permissions for Cloud Run targets](https://docs.cloud.google.com/eventarc/docs/roles-permissions).

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create and deploy a function

You can deploy a Cloud Run function using the Google Cloud console, or the gcloud CLI. Click the tab for instructions on using the tool of your choice.

###  Console 

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click **Write a function**.

  3. In the **Service name** field, enter a name to describe your function. Service names must only begin with a letter, and contain up to 49 characters or less, including letters, numbers, or hyphens. Service names can't end with hyphens, and must be unique per region and project. A service name cannot be changed later and is publicly visible.

  4. In the **Region** list, use the default value, or select the region where you want to deploy your function.

  5. In the **Runtime** list, use the default value, or select a runtime version.

  6. Optionally, in the **Trigger** section, click **Add trigger** and select an option. The **Eventarc trigger** pane opens, where you can modify the following details for the trigger:

     1. In the **Trigger name** field, enter a name for the trigger, or use the default name.

     2. Select a **Trigger type** from the list to specify one of the following trigger types:

        * **Google Sources** to specify triggers for Pub/Sub, Cloud Storage, Firestore, and other Google event providers.

        * **Custom** to produce and consume events from your application code. Follow the prompts in the **Eventarc trigger** pane to create a [channel](https://docs.cloud.google.com/eventarc/docs/third-parties/create-channels). A channel is a resource used as a pipeline to deliver custom events from producers to consumers. Custom events are published to a channel, and an Eventarc trigger subscribes to those events.

        * **Third-party** to integrate with non-Google providers that offer an Eventarc source. For more information, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/docs/third-parties/third-parties-overview).

     3. Select an **Event provider** from the list, to select a product that provides the type of event for triggering your function. For the list of event providers, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/docs/event-providers-targets).

     4. Select an **Event type** from the list. Your trigger configuration varies depending on the supported event type. For more information, see [Event types](https://docs.cloud.google.com/eventarc/docs/event-types).

     5. In the **Region** field, select a [location](https://docs.cloud.google.com/eventarc/docs/overview#trigger-location) for the Eventarc trigger. In general, the location of an Eventarc trigger should match the location of the Google Cloud resource that you want to monitor for events. In most scenarios, you should also deploy your function in the same region. See [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations) for more details about Eventarc trigger locations.

     6. In the **Service account** field, select a service account. Eventarc triggers are linked to service accounts to use as an identity when invoking your function. Your Eventarc trigger's service account must have the permission to invoke your function. By default, Cloud Run uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

     7. Optionally, specify the **Service URL path** to send the incoming request to. This is the relative path on the destination service to which the events for the trigger should be sent. For example: `/`, `/route`, `route`, and `route/subroute`.

     8. Once you've completed the required fields, click **Save trigger**.

  7. Under **Authentication** , configure the following:

     * If you are creating a public HTTP function, for example a webhook, select **Allow public access**. Selecting this assigns the IAM Invoker role to the special identifier `allUser`. You can [use IAM to edit this setting](https://docs.cloud.google.com/run/docs/securing/authenticating#service-to-service) later after you create the service. If you don't have permissions (Cloud Run Admin role) to select this, the service will deploy and require authentication.

     * If you are creating an event-triggered function, select **Require authentication**.

  8. Optionally, update the following additional configurations for your functions:

     1. Set [**Billing**](https://docs.cloud.google.com/run/docs/configuring/billing-settings) as needed.

     2. Under **Service scaling** , if you use the default Cloud Run [autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling), optionally specify the [minimum](https://docs.cloud.google.com/run/docs/configuring/min-instances) instances. If you use [manual scaling](https://docs.cloud.google.com/run/docs/configuring/services/manual-scaling), specify the number of instances for the service.

     3. Set the [**Ingress control**](https://docs.cloud.google.com/run/docs/securing/ingress) settings as needed.

     4. Expand the **Container(s), Volumes, Networking, Security** section, to set other optional settings in the appropriate tabs:

        * [Concurrency](https://docs.cloud.google.com/run/docs/configuring/concurrency)
        * [Container configuration](https://docs.cloud.google.com/run/docs/configuring/services/containers)
        * [CPU limits](https://docs.cloud.google.com/run/docs/configuring/services/cpu)
        * [Memory limits](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits)
        * [Request timeout](https://docs.cloud.google.com/run/docs/configuring/request-timeout)
        * [Secrets](https://docs.cloud.google.com/run/docs/configuring/services/secrets)
        * [Environment variables](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables)
        * [Execution environment](https://docs.cloud.google.com/run/docs/configuring/execution-environments)
        * [HTTP/2](https://docs.cloud.google.com/run/docs/configuring/http2)
        * [Service accounts](https://docs.cloud.google.com/run/docs/configuring/services/service-identity)
        * [Cloud SQL connections](https://docs.cloud.google.com/run/docs/configuring/connect-cloudsql)
        * [VPC connection](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc)
  9. Click **Create** , and wait for Cloud Run to create the service using a placeholder revision.

  10. The console will redirect you to the **Source** tab where you can see the source code of your function. Click **Save and redeploy**.

  11. In the **Source** tab, you can optionally click **Show Payload** to see an example payload of incoming events.

  12. After deployment, test the created function by clicking the **Test** button.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Update `gcloud` components to the latest version:
         
         gcloud components update

  3. Run the following command in the directory that contains the sample code:
         
         gcloud run deploy FUNCTION \
                --source . \
                --function FUNCTION_ENTRYPOINT \
                --base-image BASE_IMAGE \
                --region REGION
         

Replace:

     * FUNCTION with the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

     * FUNCTION_ENTRYPOINT with the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.

     * BASE_IMAGE with the base image environment for your function, like `nodejs24`, `python314`, `go127`, `java25`, `dotnet10`, `ruby40`, or `php85`. For more details about base images and the packages included in each image, see [Runtimes base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).

     * REGION with the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) where you want to deploy your function. For example, `europe-west1`.

Optional:

     * If you are creating a public HTTP function, for example a webhook, specify the `--allow-unauthenticated` flag. This flag assigns the Cloud Run IAM Invoker role to the special identifier `allUser`. You can [use IAM to edit this setting](https://docs.cloud.google.com/run/docs/securing/authenticating#service-to-service) later after you create the service. If you are creating an event-triggered function or authenticated service, you can omit this flag.



Optionally, after deploying your function, you can add Eventarc triggers to your function. To add a trigger, run the following command:
    
    
      gcloud eventarc triggers create EVENTARC_TRIGGER_NAME \
          --location=EVENTARC_TRIGGER_LOCATION \
          --destination-run-service=FUNCTION \
          --destination-run-region=REGION \
          --event-filters="type=EVENTARC_FILTER_TYPE" \
          --event-filters="EVENTARC_EVENT_FILTER" \
          --service-account=EVENTARC_TRIGGER_SERVICE_ACCOUNT
    

Replace:

  * EVENTARC_TRIGGER_NAME with the name of the Eventarc trigger.

  * EVENTARC_TRIGGER_LOCATION with the location for the Eventarc trigger. In general, the location of an Eventarc trigger should match the location of the Google Cloud resource that you want to monitor for events. In most scenarios, you should also deploy your function in the same region. See [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations) for more details about Eventarc trigger locations.

  * FUNCTION with the name of your deployed function.

  * REGION with the Cloud Run [region](https://docs.cloud.google.com/run/docs/locations) of the function.

  * EVENTARC_FILTER_TYPE with the event filters that the trigger monitors. An event that matches all the `--event-filters` filters triggers calls to your function. Each trigger must have a supported event type in the form `--event-filters="type=EVENTARC_FILTER_TYPE"`. This event type can't be changed after creation. To change `EVENT_FILTER_TYPE`, create a new trigger and delete the old one. Optionally, you can repeat the `--event-filters` flag with a supported filter in the form `ATTRIBUTE=VALUE` to add more filters.

  * EVENTARC_TRIGGER_SERVICE_ACCOUNT with a service account. Eventarc triggers are linked to service accounts to use as an identity when invoking your function. Your Eventarc trigger's service account must have the permission to invoke your function. By default, Cloud Run uses the [Default compute service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).




###  Terraform 

To manage functions using [Terraform](https://learn.hashicorp.com/terraform/getting-started/install.html), you must build your function code into a container image, then define your Cloud Run service in a Terraform configuration using the [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource from the [Google Cloud Platform Provider](https://www.terraform.io/docs/providers/google/index.html).

  1. Follow the instructions for [building a function on scratch](https://docs.cloud.google.com/run/docs/building/functions#building_a_function_for_automatic_base_image_updates) to create a container image that is compatible with [automatic security updates](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates). Copy the full path of the container image for the IMAGE_URL variable used in the next step.

  2. Create a new `main.tf` file with this content:
         
         provider "google" {
           project = "PROJECT-ID"
         }
         
         resource "google_cloud_run_v2_service" "default" {
           name     = "SERVICE"
           location = "REGION"
           client   = "terraform"
           template {
             containers {
               name = "SERVICE"
               image = "IMAGE_URL" # Container image built from your function in the previous step.
               base_image_uri = "BASE_IMAGE"
             }
           }
           build_config{
             function_target = "FUNCTION_TARGET"
             image_uri = "IMAGE_URL"
             base_image = "BASE_IMAGE"
             enable_automatic_updates = true
           }
         }
         resource "google_cloud_run_v2_service_iam_member" "noauth" {
           location = google_cloud_run_v2_service.default.location
           name     = google_cloud_run_v2_service.default.name
           role     = "roles/run.invoker"
           member   = "allUsers"
         }
         

Replace:

     * PROJECT-ID with the Google Cloud project ID.
     * REGION with the Google Cloud region. For example, `europe-west1`.
     * SERVICE with the name of your Cloud Run service. Service names must be 49 characters or less and must be unique per region and project.
     * IMAGE_URL with a reference to the [container image containing only your built function](https://docs.cloud.google.com/run/docs/building/functions#building_a_function_for_automatic_base_image_updates)
     * BASE_IMAGE with the base image environment for your function, like `nodejs24`, `python314`, `go127`, `java25`, `dotnet10`, `ruby40`, or `php85`. For more details about base images and the packages included in each image, see [Runtimes base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).
     * FUNCTION_TARGET with the function name you want to use as the entrypoint.

This configuration allows public access (the equivalent of `--allow-unauthenticated`). To make the service private, remove the `google_cloud_run_v2_service_iam_member` stanza.

  3. Initialize Terraform:
         
         terraform init

  4. Apply the Terraform configuration:
         
         terraform apply

Confirm you want to apply the actions described by entering `yes`.




### Cloud Run locations

Cloud Run is regional, which means the infrastructure that runs your Cloud Run services is located in a specific region and is managed by Google to be redundantly available across [all the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).   
  


Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your Cloud Run services are run. You can generally select the region nearest to your users but you should consider the location of the [other Google Cloud products](https://cloud.google.com/about/locations/#locations) that are used by your Cloud Run service. Using Google Cloud products together across multiple locations can affect your service's latency as well as cost.  
  


Cloud Run is available in the following regions:

#### Subject to [Tier 1 pricing](https://cloud.google.com/run/pricing#tables)

  * `asia-east1` (Taiwan) 
  * `asia-northeast1` (Tokyo) 
  * `asia-northeast2` (Osaka) 
  * `asia-south1` (Mumbai, India) 
  * `asia-southeast3 ` (Bangkok) 
  * `europe-north1` (Finland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-north2` (Stockholm) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-southwest1` (Madrid) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west1` (Belgium) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west4` (Netherlands) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west8` (Milan) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west9` (Paris) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-west1` (Tel Aviv) 
  * `northamerica-south1` (Mexico) 
  * `us-central1` (Iowa) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-east1` (South Carolina) 
  * `us-east4` (Northern Virginia) 
  * `us-east5` (Columbus) 
  * `us-south1` (Dallas) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west1` (Oregon) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)



#### Subject to [Tier 2 pricing](https://cloud.google.com/run/pricing#tables)

  * `africa-south1` (Johannesburg) 
  * `asia-east2` (Hong Kong) 
  * `asia-northeast3` (Seoul, South Korea) 
  * `asia-southeast1` (Singapore) 
  * `asia-southeast2 ` (Jakarta) 
  * `asia-south2` (Delhi, India) 
  * `australia-southeast1` (Sydney) 
  * `australia-southeast2` (Melbourne) 
  * `europe-central2` (Warsaw, Poland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west10` (Berlin) 
  * `europe-west12` (Turin) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west2` (London, UK) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west3` (Frankfurt, Germany) 
  * `europe-west6` (Zurich, Switzerland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-central1` (Doha) 
  * `me-central2` (Dammam) 
  * `northamerica-northeast1` (Montreal) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `northamerica-northeast2` (Toronto) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-east1` (Sao Paulo, Brazil) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-west1` (Santiago, Chile) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west2` (Los Angeles) 
  * `us-west3` (Salt Lake City) 
  * `us-west4` (Las Vegas) 



If you already created a Cloud Run service, you can view the region in the Cloud Run dashboard in the [Google Cloud console](https://console.cloud.google.com/run).

OK

### Enable event retries

Eventarc uses Pub/Sub as its transport layer and has a default retry policy that might not work well for your function.

After creating an Eventarc trigger, we strongly recommend updating the [retry policy](https://docs.cloud.google.com/eventarc/docs/retry-events) in Eventarc and configuring [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic) in Pub/Sub.

### Specify an image repository

Cloud Run function deployments use Artifact Registry to store artifacts and manage container images. Artifact Registry automatically creates the Artifact Registry repository `REGION-docker.pkg.dev/PROJECT_ID/cloud-run-source-deploy` if your project hasn't already created one with this name.

To specify a self-created Artifact Registry repository, use the following command:

###  gcloud 
    
    
    gcloud run deploy FUNCTION \
      --source . \
      --function FUNCTION_ENTRYPOINT \
      --base-image BASE_IMAGE \
      --region REGION \
      --image IMAGE_URL

Replace the following:

  * FUNCTION with the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

  * FUNCTION_ENTRYPOINT with the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.

  * BASE_IMAGE with the base image environment for your function, like `nodejs24`, `python314`, `go127`, `java25`, `dotnet10`, `ruby40`, or `php85`. For more details about base images and the packages included in each image, see [Runtimes base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).

  * REGION with the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) where you want to deploy your function. For example, `europe-west1`.

  * IMAGE_URL with a reference to the image path using the Artifact Registry image repository of your choice, for example `projects/PROJECT_NAME/locations/LOCATION/repositories/REPOSITORY_NAME/FUNCTION`. The image name must match the name of the function you care creating. If only the repository path is provided, the image will be created using the function name FUNCTION.




When specifying an Artifact Registry repository located in a different project or region, you must consider the following:

IAM configurations in the Artifact Registry project:

  * Ensure that you have configured IAM permissions to deploy images from [other Google Cloud projects](https://docs.cloud.google.com/run/docs/deploying#other-projects): 
    * Grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) to the Cloud Run service agent (`service-FUNCTION_PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com`) from the function project.
    * Grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) to the deploying identity:
    * For deployments using the Cloud Run API (for example, `gcloud run deploy`), grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) to the deploying user or service account.
    * For deployments using the Cloud Functions API (for example, `gcloud functions deploy`), grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) to the Cloud Functions service agent (`service-FUNCTION_PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com`) from the function project.
  * Grant the Artifact Registry Reader (`roles/artifactregistry.reader`) and Artifact Registry Writer (`roles/artifactregistry.writer`) roles to the [build service account](https://docs.cloud.google.com/run/docs/configuring/services/build-service-account) (`--build-service-account`) from the function project.



Network configurations:

  * Ensure that the target REPOSITORY is reachable from the current project configuration.



VPC Service Controls configurations:

  * Ensure that the build service account can reach the target REPOSITORY within the VPC-SC perimeter.



Data residency constraints:

  * Note that specifying a REPOSITORY in a different region from where your function is located leads to data transfer across regions.



## Modify an existing function

You can either modify the configuration or the code of your function:

### Modify configuration

To modify configuration parameters, such as billing options, memory, and VPC connectivity, follow the instructions in the appropriate tab:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Locate the service you want to update in the services list, and click to open the details of that service.

  3. Modify the configuration settings within the appropriate tabs.

  4. Click **View diff & redeploy**, then **Deploy changes** to deploy your changes.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To update one or more service configuration setting, use the [`gcloud run services update SERVICE`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) command with the command line flags of the configuration you want to update. Replace SERVICE with the name of the service.




### Re-deploy new source code

You can modify your function's base image, runtime, and source code using either the Google Cloud console or the gcloud CLI.

Click the tab for instructions using the tool of your choice.

###  Console 

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Locate the function you want to update in the **Services** list, and click to open the details of that function.

  3. Navigate to the **Source** tab, and click **Edit Source**.

  4. Click mode **Edit runtime and security updates** next to **Base image** , and select a different **Runtime** or **Environment** from the list as needed, and click **Save and redeploy**.

  5. Modify the **Function entry point** as needed.

  6. In the **Files** section, select add **Add file** to create a new file, mode **Rename file** to rename a file, or delete **Delete file** to delete a file.

  7. In the **Code** section, modify your source code as needed.

  8. Click **Save and Redeploy** , and wait for the deployment to finish.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the following command in the directory that contains the function's source code:
         
         gcloud run deploy FUNCTION \
                --source . \
                --function FUNCTION_ENTRYPOINT \
                --base-image BASE_IMAGE \
                --region REGION
         

Replace:

     * FUNCTION with the name of the function you want to modify.

     * FUNCTION_ENTRYPOINT with the entry point to your function in your source code.

     * BASE_IMAGE with the base image environment for your function, like `nodejs24`, `python314`, `go127`, `java25`, `dotnet10`, `ruby40`, or `php85`.

Alternatively, if you want to use a specific system package in the stack or specify the region where the base image is downloaded from, you can specify one of the following:

       * The full base image path, such as `us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/nodejs24`. This option lets you specify the base image, a specific system package in the stack, and the region where the base image is downloaded from.
       * The alias of the full base image path, such as `google-24/nodejs24` or `google-24-full/nodejs24`. This shorter alias option lets you specify the base image and a specific system package in the stack.

For more details about base images and the packages included in each image, see [Runtime base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).

     * REGION with the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) where you want to deploy your function. For example, `europe-west1`.

### Optional flags

You can configure the following optional flags while modifying your function:

     * [Build environment variables](https://docs.cloud.google.com/run/docs/configuring/services/build-environment-variables) flags for specifying environment variables during the build step, such as for configuring build-time specific certificates, or parameters.

     * [Worker pool](https://docs.cloud.google.com/run/docs/configuring/services/build-worker-pools) flags for specifying which worker pool to use in VPC Service Controls secured build context.

     * [Custom build service accounts](https://docs.cloud.google.com/run/docs/configuring/services/build-service-account) flags for specifying an alternative to the default build service account for increased security.

     * [Automatic base image updates](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates) flag to disable automatic updates. By default, functions have automatic security updates enabled.




## Disabling the deployment health check

By default, Cloud Run checks that your deployment is healthy by starting an instance and waiting for its startup probe to pass. If the health check fails, the revision will be marked as unhealthy and the traffic won't be routed to it.

If it is not needed or to increase deployment speed, the deployment health check can be disabled:

###  gcloud 

To disable the deployment health check, use the `--no-deploy-health-check` flag:
    
    
    gcloud run deploy --image IMAGE_URL --no-deploy-health-check

Replace the following:

  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .



Use `--deploy-health-check` to re-enable the deployment health check if it was previous disabled.

### YAML

To disable the deployment health check, add the `run.googleapis.com/health-check-disabled` annotation with value `'true'` to `spec.template.metadata.annotations`.
    
    
    apiVersion: serving.knative.dev/v1
    kind: Service
    metadata:
      name: SERVICE
    spec:
      template:
        metadata:
          annotations:
            run.googleapis.com/health-check-disabled: 'true'
    

### Terraform

To disable the deployment health check, set the `health_check_disabled` argument to `true` in the `template` block.
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE"
      ...
      template {
        health_check_disabled = true
        ...
      }
    }
    

## Source bucket

Your source code must be accessible to the build process and the Google Cloud console source editor. This is accomplished by uploading your source code to a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets).

When you deploy using the gcloud CLI or the Google Cloud console, a Cloud Storage bucket is automatically provisioned, and your source code is uploaded for you. By default, your code is stored in a bucket named `run-sources-PROJECT_ID-REGION`. You are responsible for managing the [Access Control Lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) and source objects within this bucket.

If you need to use a specific bucket, such as to use [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/run/docs/securing/using-cmek#source-deploy), you must first package your local source files into an archive (such as a ZIP file). Then, upload this archive to your bucket. To deploy from this custom location, use the gcloud CLI with the flag `--source=gs://BUCKET_NAME/OBJECT_PATH`.

## What's next

After you deploy a new Cloud Run function, you can do the following:

  * [View or delete functions](https://docs.cloud.google.com/run/docs/managing/revisions)
  * [Manage services](https://docs.cloud.google.com/run/docs/managing/services)
  * [View logs](https://docs.cloud.google.com/run/docs/logging)
  * [Build function containers](https://docs.cloud.google.com/run/docs/building/functions) in your own toolchain and deploy it to Cloud Run
  * [Trigger with events](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events)
  * [Trigger functions from Cloud Storage using Eventarc](https://docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
