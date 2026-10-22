---
url: https://docs.cloud.google.com/appengine/migration-center/standard/java/images-to-cloud-run/
title: Migrate from the App Engine Images service to Cloud Run \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:15.038531+00:00
---

# Migrate from the App Engine Images service to Cloud Run  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/java/images-to-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate from the App Engine Images service to Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

To modernize image processing in your existing App Engine applications, you can deploy a containerized image transformation service to Cloud Run and route your App Engine [Images service](https://docs.cloud.google.com/appengine/docs/standard/services/images) calls to it.

This migration doesn't require major rewrites to your image processing code or hosting your App Engine application on Cloud Run. Instead, when you configure your application, the App Engine services SDK intercepts your App Engine Images service calls and routes them to the Cloud Run service. The service processes the images using an open-source [Pillow](https://pypi.org/project/pillow/) engine over [gRPC](https://grpc.io) and returns the results to your App Engine application. This setup replaces the legacy App Engine Images service backend with a modern, cloud-native solution.

**Note:** Modernizing the App Engine Images API separates image processing from image serving. The Cloud Run service acts as a private backend for image processing tasks that your application requests, such as resizing, cropping, and rotating. To host and deliver images, store them in a [**Cloud Storage**](https://docs.cloud.google.com/storage/docs) bucket or distribute them using [**Cloud CDN**](https://docs.cloud.google.com/cdn/docs/overview).

### Limitations

  * When you use the custom image processing service with `APPENGINE_USE_CUSTOM_IMAGES_GRPC_SERVICE` set to `true`, you can't generate serving URLs. App Engine throws a runtime exception when you invoke the `getServingUrl()` method. You can use this method only when `APPENGINE_USE_CUSTOM_IMAGES_GRPC_SERVICE` is set to `false` or not set. This restriction prevents reliance on the legacy backend for storing and serving images.

To serve images, we recommend that you serve them directly from a Cloud Storage URL or use a Cloud Storage bucket backed by Cloud CDN.

Existing URLs you created by using legacy calls to the `getServingUrl()` method continue to serve images.

  * When you upgrade your App Engine services SDK version, App Engine doesn't automatically route calls to the Cloud Run service. Your application applies the new behavior only after you configure the `APPENGINE_USE_CUSTOM_IMAGES_GRPC_SERVICE` and `APPENGINE_IMAGES_SERVICE_ENDPOINT` environment variables.




## Before you begin

  1. Make sure that you have access to the App Engine source code.

  2. Enable the Cloud Run Admin API and the Artifact Registry API:

[Enable APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,artifactregistry.googleapis.com&_ga=2.109139269.1795509783.1687809390-606913076.1686784330)




### Required roles

You can choose to either create a new service account or use the same user-managed service account in Cloud Run that you are using for App Engine. You or your administrator must grant the deployer account and the Cloud Build service account the following IAM roles.

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

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Migration process

This migration includes the following steps:

  1. Deploy the image transformation service on Cloud Run to obtain your service URL.
  2. Configure your App Engine source files with your Cloud Run service URL and routing flags, and then deploy or redeploy your App Engine application.
  3. Test your application to check your image processing functionality.



### Deploy the image transformation service on Cloud Run

To deploy the image transformation service and configure its access to Cloud Storage, follow these steps:

  1. Deploy the prebuilt image transformation service container to the Cloud Run service. Make sure you deploy with authentication enforced (`--no-allow-unauthenticated`). The App Engine services SDK handles authentication when making calls to this service:
         
         gcloud run deploy image-processing-service \
             --image=us-central1-docker.pkg.dev/gae-bundled-services-images/release/image-processing-service:latest \
             --no-allow-unauthenticated \
             --region=REGION
         

Replace REGION with the region where you deploy the Cloud Run service. We recommend that you deploy the service in the same region as your App Engine service.

Note the service URL of your deployed Cloud Run service, for example, `https://image-processing-service-xyz-uc.a.run.app`.

  2. Grant the [Cloud Run Invoker](https://docs.cloud.google.com/run/docs/securing/managing-access#add-principals) (`roles/run.invoker`) role to the default App Engine service account. This allows your App Engine application to authorize and route calls to the private Cloud Run service:
         
         gcloud run services add-iam-policy-binding image-processing-service \
             --member="serviceAccount:PROJECT_ID@appspot.gserviceaccount.com" \
             --role="roles/run.invoker" \
             --region=REGION
         

  3. Grant the [Cloud Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.objectViewer) (`roles/storage.objectViewer`) role to the default Compute Engine service account. This allows the image transformation service to read images stored in Cloud Storage:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/storage.objectViewer"
         

Replace the following:

     * PROJECT_ID: the ID of the project where you deploy the Cloud Run service.
     * PROJECT_NUMBER: the project number of the project where you deploy the Cloud Run service.



### Configure your source files

To configure your Java application to use the image transformation service on Cloud Run, follow these steps:

  1. Update the `pom.xml` file to include the following dependencies:

     * Add or update the `appengine-api-1.0-sdk` dependency:
           
           <dependency>
             <groupId>com.google.appengine</groupId>
             <artifactId>appengine-api-1.0-sdk</artifactId>
             <version>5.1.0</version>
           </dependency>
           

     * Add the `google-auth-library-oauth2-http` dependency for secure communication with Cloud Run:
           
           <dependency>
             <groupId>com.google.auth</groupId>
             <artifactId>google-auth-library-oauth2-http</artifactId>
             <version>1.20.0</version>
           </dependency>
           

  2. Update the `appengine-web.xml` file to configure the required environment variables:
         
         <?xml version="1.0" encoding="utf-8"?>
         <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
             <runtime>RUNTIME</runtime> <!-- a supported Java runtime version -->
             <threadsafe>true</threadsafe>
         
             <!-- List the Images service -->
             <app-engine-bundled-services>
                 <api>images</api>
             </app-engine-bundled-services>
         
             <env-variables>
                 <!-- Enable the custom gRPC Images service -->
                 <env-var name="APPENGINE_USE_CUSTOM_IMAGES_GRPC_SERVICE" value="true" />
         
                 <!-- The URL of the Cloud Run service you deployed -->
                 <env-var name="APPENGINE_IMAGES_SERVICE_ENDPOINT" value="RUN_SERVICE_URL" />
             </env-variables>
         </appengine-web-app>
         

Replace the following:

     * RUNTIME: a [supported](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#java) Java runtime version.
     * RUN_SERVICE_URL: the URL of your deployed Cloud Run service.
  3. Deploy your application to App Engine:
         
         mvn clean package appengine:deploy clean
         

  4. Launch your browser, and access your web service by running the following command:
         
         gcloud app browse
         




### Test your application

To verify that your application is successfully using the Cloud Run image transformation service:

  1. Trigger the image processing functionality in your deployed App Engine application.
  2. [Check the Logs Explorer](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs?tab=java#view_logs) for your App Engine application. Make sure that there are no errors related to `com.google.appengine.api.images` calls.
  3. [Check the logs of your Cloud Run `image-processing-service`](https://docs.cloud.google.com/run/docs/logging) to verify that Cloud Run received and processed the requests.



## What's next

  * [Migrate off of legacy bundled services](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
