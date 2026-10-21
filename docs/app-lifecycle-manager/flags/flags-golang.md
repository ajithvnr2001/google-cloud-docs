---
url: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-golang/
title: Use App Lifecycle Manager feature flags with Go \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:53:18.859236+00:00
---

# Use App Lifecycle Manager feature flags with Go  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-golang/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)



Send feedback 

#  Use App Lifecycle Manager feature flags with Go Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide explains how to integrate your Go applications with App Lifecycle Manager feature flags. You'll learn how to use the OpenFeature SDK with the `flagd` provider to evaluate flags managed by App Lifecycle Manager, allowing you to dynamically control feature availability and behavior in your Go services.

This guide assumes you have already set up the necessary App Lifecycle Manager resources (like App offerings, unit kinds, units, flags, and rollouts) by completing one of the following quickstarts:

  * **[Quickstart: Deploy feature flags with App Lifecycle Manager (Integrated)](https://docs.cloud.google.com/app-lifecycle-manager/flags-quickstart)** : If you manage your application deployments with App Lifecycle Manager.
  * **[Quickstart: Use feature flags Standalone](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-standalone-quickstart)** : If you manage your application infrastructure independently but want to use App Lifecycle Manager for feature flag management.



## Prerequisites

Before you begin, ensure you have the following:

  1. **Go installed:** Version 1.23 or later.
  2. **Completed an App Lifecycle Manager feature flags Quickstart:**
     * Successfully completed either the [integrated](https://docs.cloud.google.com/app-lifecycle-manager/flags-quickstart) or [standalone](https://docs.cloud.google.com/app-lifecycle-manager/flags-standalone-quickstart) feature flags quickstart to provision your target unit.
     * You should have environment variables or values from that quickstart, such as `PROJECT_ID`, `LOCATION_1` (the region of your Unit), `UNIT_ID`, and `FLAG_KEY`.
  3. **Authenticated`gcloud` for Application Default Credentials (ADC):** The Go application uses ADC to authenticate with Google Cloud services. If running locally (for standalone usage, or local Docker testing), ensure you've authenticated in your environment:
         
         gcloud auth application-default login
         

  4. **IAM Permissions:** The identity running your Go application needs the `roles/saasconfig.viewer` Identity and Access Management role on your Google Cloud project to read flag configurations:
         
         gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
             --member="user:YOUR_EMAIL_ADDRESS" \
             --role="roles/saasconfig.viewer"
         

Replace `YOUR_PROJECT_ID` and `YOUR_EMAIL_ADDRESS` accordingly.




## Understand key environment variables

Your Go application relies on environment variables to connect to the correct flag configuration and evaluate the intended flag.

  * **`FLAGD_SOURCE_PROVIDER_ID`** : Specifies which feature flag configuration to fetch from the App Lifecycle Manager service. It must be the full resource name of the `FeatureFlagConfig` associated with your unit. 
    * **Format** : `projects/PROJECT_ID/locations/LOCATION/featureFlagsConfigs/UNIT_ID`
    * **Example** : `projects/my-gcp-project/locations/us-central1/featureFlagsConfigs/my-app-instance-01`



## Set up your Go project

Before you can run your application, initialize your module and add the necessary initialization and evaluation logic.

  1. **Create a project directory:**
         
         mkdir go-featureflag-app
         cd go-featureflag-app
         go mod init go-featureflag-app
         

  2. **Create application code:** Add a file named `main.go` with the following content to initialize the provider and evaluate a flag.
         
         package main
         
         import (
             "context"
             "fmt"
             "log"
             "os"
         
             flagd "github.com/open-feature/go-sdk-contrib/providers/flagd/pkg"
             "github.com/open-feature/go-sdk/openfeature"
             "google.golang.org/grpc"
             "google.golang.org/grpc/credentials"
             "google.golang.org/grpc/credentials/oauth"
             "google.golang.org/grpc/metadata"
         )
         
         // GetNewFlagdProvider initializes a flagd provider configured for  App Lifecycle Manager
         func GetNewFlagdProvider(ctx context.Context) (*flagd.Provider, error) {
             providerID := os.Getenv("FLAGD_SOURCE_PROVIDER_ID")
             if providerID == "" {
                 return nil, fmt.Errorf("FLAGD_SOURCE_PROVIDER_ID environment variable is not set")
             }
         
             creds, err := oauth.NewApplicationDefault(ctx)
             if err != nil {
                 return nil, err
             }
         
             // Interceptor to inject the Unit name into headers for regional routing
             routingInterceptor := func(ctx context.Context, desc *grpc.StreamDesc, cc *grpc.ClientConn, method string, streamer grpc.Streamer, opts ...grpc.CallOption) (grpc.ClientStream, error) {
                 md := metadata.Pairs("x-goog-request-params", fmt.Sprintf("name=%s", providerID))
                 ctx = metadata.NewOutgoingContext(ctx, md)
                 return streamer(ctx, desc, cc, method, opts...)
             }
         
             options := []flagd.ProviderOption{
                 flagd.WithHost("saasconfig.googleapis.com"),
                 flagd.WithPort(443),
                 flagd.WithInProcessResolver(),
                 flagd.WithProviderID(providerID),
                 flagd.WithGrpcDialOptionsOverride([]grpc.DialOption{
                     grpc.WithTransportCredentials(credentials.NewTLS(nil)),
                     grpc.WithPerRPCCredentials(creds),
                     grpc.WithStreamInterceptor(routingInterceptor),
                 }),
             }
         
             return flagd.NewProvider(options...)
         }
         
         // InitializeFeatureManagement registers the provider globally
         func InitializeFeatureManagement(ctx context.Context) error {
             provider, err := GetNewFlagdProvider(ctx)
             if err != nil {
                 return err
             }
             openfeature.SetProvider(provider)
             return nil
         }
         
         func main() {
         ctx := context.Background()
         InitializeFeatureManagement(ctx);
         
         // 1. Get Client
         client := openfeature.NewClient("simple-api")
         
         // 2. Create Evaluation Context
         evalCtx := openfeature.NewEvaluationContext()
         
         // 3. Evaluate Flag
         // Default to false if evaluation fails
         isEnhanced, err := client.BooleanValue(context.Background(), "enhanced-search", false, evalCtx)
         if err != nil {
         log.Printf("Flag evaluation failed: %v", err)
         }
         
         // 4. Return response
         if isEnhanced {
         fmt.Println("Enhanced search feature is enabled.")
         } else {
         fmt.Println("Enhanced search feature is disabled.")
         }
         
         }
         

  3. **Create go.mod:** Using specific versions ensures stability.
         
         module go-featureflag-app
         
         go 1.23
         
         require (
             github.com/open-feature/go-sdk v1.15.1
             github.com/open-feature/go-sdk-contrib/providers/flagd v0.3.0
             google.golang.org/grpc v1.74.2
             golang.org/x/oauth2 v0.22.0
         )
         

  4. **Get dependencies:**
         
         go mod tidy
         go mod download
         




## Run the Go application

You can execute the application either locally using your standalone configuration or deployed as a container.

### Run standalone (locally)

  1. **Set environment variables:**
         
         export PROJECT_ID="your-gcp-project-id"
         export LOCATION_1="us-central1"
         export UNIT_ID="my-app-instance-01"
         export FLAGD_SOURCE_PROVIDER_ID="projects/${PROJECT_ID}/locations/${LOCATION_1}/featureFlagsConfigs/${UNIT_ID}"
         

  2. **Run the application:**
         
         go run main.go
         




### Run integrated (containerized)

  1. **Create a Dockerfile:**
         
         FROM golang:1.23 as builder
         WORKDIR /app
         COPY go.mod go.sum ./
         RUN go mod download
         COPY . .
         RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o /go-featureflag-app .
         
         FROM gcr.io/distroless/static-debian11
         WORKDIR /
         COPY --from=builder /go-featureflag-app /go-featureflag-app
         ENTRYPOINT ["/go-featureflag-app"]
         

  2. **Build and push the image:**
         
         export PROJECT_ID="your-gcp-project-id"
         docker build -t gcr.io/${PROJECT_ID}/my-go-app:latest .
         docker push gcr.io/${PROJECT_ID}/my-go-app:latest
         

  3. **Deploy the service:** Update your unit blueprint to reference `gcr.io/${PROJECT_ID}/my-go-app:latest` and deploy the new release using an App Lifecycle Manager rollout.




## Verify flag changes

After your application is running, confirm that it evaluates flags correctly.

  1. **Observe the initial value:** Verify that the output logs the value corresponding to the initial state.
  2. **Update the flag in App Lifecycle Manager:** Modify the flag behavior using Google Cloud console or `gcloud`.
  3. **Verify the updated value:** Re-run the local compilation or observe the container logs to see the updated result.



## What's next

  * Read the [App Lifecycle Manager feature flags overview](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-overview) for more conceptual details.
  * Learn about [App Lifecycle Manager Rollouts](https://docs.cloud.google.com/app-lifecycle-manager/update-saas-offering) for safer flag deployments.
  * Review the main [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
