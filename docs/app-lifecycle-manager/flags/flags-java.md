---
url: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-java/
title: Use App Lifecycle Manager feature flags with Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:31:01.034913+00:00
---

# Use App Lifecycle Manager feature flags with Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-java/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)



Send feedback 

#  Use App Lifecycle Manager feature flags with Java Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide explains how to integrate your Java applications with App Lifecycle Manager feature flags. You'll learn how to use the OpenFeature SDK with the `flagd` provider to evaluate flags managed by App Lifecycle Manager, allowing you to dynamically control feature availability and behavior in your Java services.

This guide assumes you have already set up the necessary App Lifecycle Manager resources (like App offerings, unit kinds, units, flags, and rollouts) by completing one of the following quickstarts:

  * **[Quickstart: Deploy feature flags with App Lifecycle Manager (Integrated)](https://docs.cloud.google.com/app-lifecycle-manager/flags-quickstart)** : If you manage your application deployments with App Lifecycle Manager.
  * **[Quickstart: Use feature flags standalone](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-standalone-quickstart)** : If you manage your application infrastructure independently but want to use App Lifecycle Manager for feature flag management.



## Prerequisites

Before you begin, ensure you have the following:

  1. **Java installed:** JDK 17 or later.
  2. **Completed an App Lifecycle Manager feature flags Quickstart:**
     * Successfully completed either the [integrated](https://docs.cloud.google.com/app-lifecycle-manager/flags-quickstart) or [standalone](https://docs.cloud.google.com/app-lifecycle-manager/flags-standalone-quickstart) feature flags quickstart to provision your target unit.
     * You should have environment variables or values from that quickstart, such as `PROJECT_ID`, `LOCATION_1` (the region of your Unit), `UNIT_ID`, and `FLAG_KEY`.
  3. **Authenticated`gcloud` for Application Default Credentials (ADC):** The Java application uses ADC to authenticate with Google Cloud services. Ensure you've authenticated in your environment:
         
         gcloud auth application-default login
         

  4. **IAM Permissions:** The identity running your Java application needs the `roles/saasconfig.viewer` Identity and Access Management role on your Google Cloud project to read flag configurations:
         
         gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
             --member="user:YOUR_EMAIL_ADDRESS" \
             --role="roles/saasconfig.viewer"
         

Replace `YOUR_PROJECT_ID` and `YOUR_EMAIL_ADDRESS` accordingly.




## Understand key environment variables

Your Java application relies on environment variables to connect to the correct flag configuration.

  * **`FLAGD_SOURCE_PROVIDER_ID`** : Specifies which feature flag configuration to fetch from the App Lifecycle Manager service. It must be the full resource name of the `FeatureFlagConfig` associated with your unit. 
    * **Format** : `projects/PROJECT_ID/locations/LOCATION/featureFlagsConfigs/UNIT_ID`
    * **Example** : `projects/my-gcp-project/locations/us-central1/featureFlagsConfigs/my-app-instance-01`



## Set up your Java project

Before you can run your application, you must initialize your project and configure the necessary dependencies.

  1. **Create a project directory:**
         
         mkdir java-featureflag-app
         cd java-featureflag-app
         

  2. **Add dependencies:** Configure your build system (Maven or Gradle) to include the following libraries. Ensure compatibility by using versions greater than OpenFeature 1.14.1, flagd 0.11.5, and gRPC 1.71.0.

     * `dev.openfeature:javasdk:1.14.1+`
     * `dev.openfeature.contrib.providers:flagd:0.11.5+`
     * `io.grpc:grpc-netty-shaded:1.71.0+`
     * `io.grpc:grpc-auth:1.71.0+`
     * `com.google.auth:google-auth-library-oauth2-http`
  3. **Create the initialization code:** Add a file named `FeatureManagement.java` with the following content. This class sets up gRPC interceptors to attach ADC and regional routing headers, and initializes the `FlagdProvider` using in-process resolution.
         
         import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
         import dev.openfeature.contrib.providers.flagd.Config;
         import dev.openfeature.contrib.providers.flagd.FlagdOptions;
         import dev.openfeature.contrib.providers.flagd.FlagdProvider;
         import dev.openfeature.sdk.OpenFeatureAPI;
         import io.grpc.*;
         import io.grpc.auth.MoreCallCredentials;
         import java.util.ArrayList;
         import java.util.List;
         
         public class FeatureManagement {
             public static void initialize() throws Exception {
                 // Read the full Unit resource name
                 String flagConfigId = System.getenv("FLAGD_SOURCE_PROVIDER_ID");
                 if (flagConfigId == null || flagConfigId.isEmpty()) {
                     throw new IllegalStateException("FLAGD_SOURCE_PROVIDER_ID environment variable is not set.");
                 }
         
                 // Configure gRPC Security and Routing
                 [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credentials = [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)();
                 CallCredentials callCredentials = MoreCallCredentials.from(credentials);
         
                 List<ClientInterceptor> interceptors = new ArrayList<>();
         
                 // Interceptor to inject the Unit name into headers for regional routing
                 interceptors.add(new ClientInterceptor() {
                     @Override
                     public <ReqT, RespT> ClientCall<ReqT, RespT> interceptCall(MethodDescriptor<ReqT, RespT> method, CallOptions callOptions, Channel next) {
                         return new ForwardingClientCall.SimpleForwardingClientCall<ReqT, RespT>(next.newCall(method, callOptions)) {
                             @Override
                             public void start(Listener<RespT> responseListener, Metadata headers) {
                                 headers.put(Metadata.Key.[of](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ClientId.html#com_google_auth_oauth2_ClientId_of_java_lang_String_java_lang_String_)("x-goog-request-params", Metadata.ASCII_STRING_MARSHALLER), "name=" + flagConfigId);
                                 super.start(responseListener, headers);
                             }
                         };
                     }
                 });
         
                 // Interceptor to attach ADC to the gRPC calls
                 interceptors.add(new ClientInterceptor() {
                     @Override
                     public <ReqT, RespT> ClientCall<ReqT, RespT> interceptCall(MethodDescriptor<ReqT, RespT> method, CallOptions callOptions, Channel next) {
                         return next.newCall(method, callOptions.withCallCredentials(callCredentials));
                     }
                 });
         
                 // Initialize the flagd provider with In-Process resolution
                 FlagdProvider provider = new FlagdProvider(
                     FlagdOptions.builder()
                         .resolverType(Config.Resolver.IN_PROCESS)
                         .host("saasconfig.googleapis.com").port(443)
                         .tls(true)
                         .providerId(flagConfigId)
                         .clientInterceptors(interceptors)
                         .syncMetadataDisabled(true)
                         .deadline(10000)
                         .build()
                 );
         
                 // Set the global provider
                 OpenFeatureAPI.getInstance().setProviderAndWait(provider);
             }
         }
         

  4. **Create the application logic:** Add a file named `Main.java` with the following content to execute the flag evaluation.
         
         import dev.openfeature.sdk.OpenFeatureAPI;
         import dev.openfeature.sdk.MutableContext;
         
         public class Main {
             public static void main(String[] args) throws Exception {
         
             // 1. Get Client
             var client = OpenFeatureAPI.getInstance().getClient("simple-api");
         
             // 2. Create Evaluation Context 
             var context = new dev.openfeature.sdk.MutableContext();
         
             // 3. Evaluate Flag
             // Default to false if evaluation fails or service is unreachable
             boolean isEnhanced = client.getBooleanValue("enhanced-search", false, context);
         
             // 4. Execute business logic based on result
             if (isEnhanced) {
                 System.out.println("Executing enhanced search algorithm...");
             } else {
                 System.out.println("Standard search algorithm...");
             }
         
             }
         }
         




## Run the Java application

You can execute the application either locally using your standalone configuration or deployed as a container.

### Run standalone (locally)

  1. **Set environment variables:**
         
         export PROJECT_ID="your-gcp-project-id"
         export LOCATION_1="us-central1"
         export UNIT_ID="my-app-instance-01"
         export FLAGD_SOURCE_PROVIDER_ID="projects/${PROJECT_ID}/locations/${LOCATION_1}/featureFlagsConfigs/${UNIT_ID}"
         

  2. **Run the application:** Execute the project using your preferred build tool command (e.g., `mvn compile exec:java` or `./gradlew run`).




### Run integrated (containerized)

  1. **Create a Dockerfile:** Define a container build that packages the Java binary.
         
         FROM maven:3.9-eclipse-temurin-17 AS builder
         WORKDIR /app
         COPY pom.xml .
         COPY src ./src
         RUN mvn clean package
         
         FROM eclipse-temurin:17-jre
         WORKDIR /app
         COPY --from=builder /app/target/java-featureflag-app.jar app.jar
         ENTRYPOINT ["java", "-jar", "app.jar"]
         

  2. **Build and push the image:**
         
         export PROJECT_ID="your-gcp-project-id"
         docker build -t gcr.io/${PROJECT_ID}/my-java-app:latest .
         docker push gcr.io/${PROJECT_ID}/my-java-app:latest
         

  3. **Deploy the service:** Update your unit blueprint to reference `gcr.io/${PROJECT_ID}/my-java-app:latest` and deploy the new release using an App Lifecycle Manager rollout.




## Verify flag changes

After your application is running, confirm that it evaluates flags correctly.

  1. **Observe the initial value:** Verify that the console output logs the evaluated value corresponding to the initial configuration state.
  2. **Update the flag in App Lifecycle Manager:** Modify the flag payload or targeting rules using Google Cloud console or `gcloud`.
  3. **Verify the updated value:** Re-run the local execution or observe the container logs to confirm the new evaluated state.



## What's next

  * Read the [App Lifecycle Manager feature flags overview](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-overview) for more conceptual details.
  * Learn about [App Lifecycle Manager Rollouts](https://docs.cloud.google.com/app-lifecycle-manager/update-saas-offering) for safer flag deployments.
  * Review the main [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
