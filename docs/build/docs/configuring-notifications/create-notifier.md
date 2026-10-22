---
url: https://docs.cloud.google.com/build/docs/configuring-notifications/create-notifier/
title: Creating your own notifier \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:06.469289+00:00
---

# Creating your own notifier  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/configuring-notifications/create-notifier/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Creating your own notifier Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build can notify you of updates to your build status by sending you notifications to selected channels. In addition to notifiers maintained by Cloud Build such as [Slack](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-smtp) or [SMTP](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-smtp), you can also use the provided library in the [cloud-build-notifiers](http://github.com/GoogleCloudPlatform/cloud-build-notifiers) repository to create your own notifier.

This page explains how you can create your own notifier.

## Before you begin

  * Enable the Cloud Build, Cloud Run, Pub/Sub, and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,run.googleapis.com,pubsub.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/configuring-notifications/create-notifier)



  * Install the [Go programming language](https://golang.org/doc/install).

**Note:** Cloud Build notifiers is written in Go. To create your own notifier using the library provided by the `cloud-build-notifiers` repository, you will need to install Go on your machine.
  * Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).




## Setting up

  1. Open a terminal window on your machine.

  2. Clone and navigate into the [cloud-build-notifiers](http://github.com/GoogleCloudPlatform/cloud-build-notifiers) repository:
         
         git clone https://github.com/GoogleCloudPlatform/cloud-build-notifiers.git && cd cloud-build-notifiers
         

  3. Add a directory for your own notifier and navigate into it, where DIRECTORY_NAME is the name of your directory:
         
         mkdir DIRECTORY_NAME && cd DIRECTORY_NAME
         

  4. Initialize go modules in your new directory, where DIRECTORY_NAME is the name of your new directory:
         
         go mod init github.com/GoogleCloudPlatform/cloud-build-notifiers/DIRECTORY_NAME
         

You should now see a `go.mod` file in your directory.

  5. Add the following line to your `go.mod` file to ensure you are using the latest version of notifiers:
         
         replace github.com/GoogleCloudPlatform/cloud-build-notifiers/lib/notifiers => ../
         




Your dependencies are now set up and you are ready to create your own notifier.

## Creating your own notifier

The `cloud-build-notifiers` contains a `lib/notifiers` directory. In the `lib/notifiers` directory, you will see a file named `notifier.go`. This file contains the framework you can use to create your own notifier.

You will need to define two methods to create a notifier in your main file.

  1. In the new directory, create a file named `main.go`.

  2. In `main.go`, import the notifiers library framework and any other dependencies:
         
         package main
         
         import (
         	"context"
         	"fmt"
         
         	cbpb "cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
         	"github.com/GoogleCloudPlatform/cloud-build-notifiers/lib/notifiers"
         	log "github.com/golang/glog"
         	"google.golang.org/protobuf/encoding/prototext"
         )
         

  3. Define a main method for your notifier. In this example, `logger` is the name of the notifier:
         
         func main() {
         	if err := notifiers.Main(new(logger)); err != nil {
         		log.Fatalf("fatal error: %v", err)
         	}
         }
         

The `main` method uses the `Main` method defined in the [`notifier.go`](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/lib/notifiers/notifiers.go) file, which is used to set up notifier binaries.

  4. Define a struct for your notifier, where you will define the variables for your interface. In this example, `logger` is the name of the notifier:
         
         type logger struct {
         	filter notifiers.EventFilter
         }
         

  5. Add the notifier functionality. The notifier interface is defined by two methods:

     * `SetUp`: The `SetUp` method accepts a configuration, fetches secrets, and pulls specified filters out of the configuration and stores them as a Common Expression Language predicate that can be used to send notifications. To learn more about CEL, see the [`cel-spec` repository](https://github.com/google/cel-spec).
     * `SendNotification`: The `SendNotification` method is what is used to send notifications to your selected channel or service.

The definition of the notifier is available in [`notifier.go`](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/49b5666c012e71376ea6c73bdd1a2b53758fed21/lib/notifiers/notifiers.go) and in the [Go documentation](https://pkg.go.dev/github.com/GoogleCloudPlatform/cloud-build-notifiers/lib/notifiers#Notifier).

In the following example, the notifier interface is defined using the `SetUp` and the `SendNotification` method to print build logs, with `logger` as the name of your notifier:
           
           func (h *logger) SetUp(_ context.Context, cfg *notifiers.Config, _ notifiers.SecretGetter, _ notifiers.BindingResolver) error {
           	prd, err := notifiers.MakeCELPredicate(cfg.Spec.Notification.Filter)
           	if err != nil {
           		return fmt.Errorf("failed to create CELPredicate: %w", err)
           	}
           	h.filter = prd
           	return nil
           }
           
           func (h *logger) SendNotification(ctx context.Context, build *cbpb.Build) error {
           	// Include custom functionality here.
           	// This example logs the build.
           	if h.filter.Apply(ctx, build) {
           		log.V(1).Infof("printing build\n%s", prototext.Format(build))
           	} else {
           		log.V(1).Infof("build (%q, %q) did NOT match CEL filter", build.ProjectId, build.Id)
           	}
           
           	return nil
           }
           

Your final `main.go` file should look similar to the following file. In this example, `logger` is used as the name of the notifier.
           
           package main
           
           import (
           	"context"
           	"fmt"
           
           	cbpb "cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
           	"github.com/GoogleCloudPlatform/cloud-build-notifiers/lib/notifiers"
           	log "github.com/golang/glog"
           	"google.golang.org/protobuf/encoding/prototext"
           )
           
           
           func main() {
           	if err := notifiers.Main(new(logger)); err != nil {
           		log.Fatalf("fatal error: %v", err)
           	}
           }
           
           
           type logger struct {
           	filter notifiers.EventFilter
           }
           
           
           func (h *logger) SetUp(_ context.Context, cfg *notifiers.Config, _ notifiers.SecretGetter, _ notifiers.BindingResolver) error {
           	prd, err := notifiers.MakeCELPredicate(cfg.Spec.Notification.Filter)
           	if err != nil {
           		return fmt.Errorf("failed to create CELPredicate: %w", err)
           	}
           	h.filter = prd
           	return nil
           }
           
           func (h *logger) SendNotification(ctx context.Context, build *cbpb.[Build](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb.html#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_Build)) error {
           	// Include custom functionality here.
           	// This example logs the build.
           	if h.filter.Apply(ctx, build) {
           		log.V(1).Infof("printing build\n%s", prototext.Format(build))
           	} else {
           		log.V(1).Infof("build (%q, %q) did NOT match CEL filter", build.ProjectId, build.Id)
           	}
           
           	return nil
           }
           

Next, configure your notifier.




## Configure notifications

  1. Write a notifier configuration file to configure your notifier and filter on build events:

In the following example notifier configuration file, the `filter` field uses [CEL](https://github.com/google/cel-spec) with the available variable, `build`, to filter build events with a `SUCCESS` status:
         
         apiVersion: cloud-build-notifiers/v1
         kind: YourNotifier
         metadata:
           name: logging-sample
         spec:
           notification:
             filter: build.status == Build.Status.SUCCESS

Where:

     * `logging-sample` is the name of the notifier.

For additional fields you can filter by, see the [Build](https://docs.cloud.google.com/cloud-build/docs/api/reference/rest/v1/projects.builds) resource. For additional filtering examples, see [Using CEL to filter build events](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-slack#using_cel_to_filter_build_events).

  2. Upload your notifier configuration file to a Cloud Storage bucket:

     1. If you don't have a Cloud Storage bucket, then run the following command to create a bucket, where BUCKET_NAME is the name you want to give your bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
            
            gcloud storage buckets create gs://BUCKET_NAME/
            

     2. Upload the notifier configuration file to your bucket:
            
            gcloud storage cp CONFIG_FILE_NAME gs://BUCKET_NAME/CONFIG_FILE_NAME
            

Where:

        * `BUCKET_NAME` is the name of your bucket.
        * `CONFIG_FILE_NAME` is the name of your configuration file.
  3. Build and deploy your notifier:

     1. Create a Dockerfile for the `logging-sample`:
            
            FROM us-docker.pkg.dev/artifact-foundry-prod/docker-3p-trusted/golang@sha256:11fd8f7f63db3b6fb198797042ba4c40a4a34dc83325d3328ca3bc4bb7726786 AS build-env
            COPY . /go-src/
            WORKDIR /go-src/
            RUN go build -o /go-app .
            
            # From the Cloud Run docs:
            # https://cloud.google.com/run/docs/tutorials/pubsub#looking_at_the_code
            # Use the official Debian slim image for a lean production container.
            # https://hub.docker.com/_/debian
            # https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
            FROM debian:buster-slim
            # Modify sources.list to point to the Debian archive
            RUN sed -i 's|deb.debian.org|archive.debian.org|g' /etc/apt/sources.list && \
                sed -i 's|security.debian.org|archive.debian.org/debian-security|g' /etc/apt/sources.list && \
                sed -i '/buster-updates/d' /etc/apt/sources.list && \
                echo "deb http://archive.debian.org/debian buster-updates main contrib non-free" >> /etc/apt/sources.list && \
                set -x && \
                apt-get update --allow-releaseinfo-change && \
                DEBIAN_FRONTEND=noninteractive apt-get install -y ca-certificates && \
                rm -rf /var/lib/apt/lists/*
            
            
            FROM gcr.io/distroless/base
            COPY --from=build-env /go-app /
            ENTRYPOINT ["/go-app", "--v=1", "--alsologtostderr"]
            

     2. Build and deploy the notifier using the following `cloudbuild.yaml` file.
            
            steps:
            - # Build the binary and put it into the builder image.
              name: gcr.io/cloud-builders/docker
              args: ['build', '--tag=gcr.io/$PROJECT_ID/logging-sample', '.']
            
            - # Push the container image to Container Registry
              name: gcr.io/cloud-builders/docker
              args: ['push', 'gcr.io/$PROJECT_ID/logging-sample']
            
            - # Deploy to Cloud Run
              name: google/cloud-sdk
              args: 
                - gcloud
                - run
                - deploy
                - logging-sample-notifier
                - --platform=managed
                - --region=us-central1
                - --image=gcr.io/$PROJECT_ID/logging-sample
                - --no-allow-unauthenticated
                - --update-env-vars=CONFIG_PATH=${_CONFIG_PATH}
            
            # Push the image with tags.
            images:
            - gcr.io/$PROJECT_ID/logging-sample

Where:

        * `_CONFIG_PATH` is the path to your notifier configuration, such as `gs://BUCKET_NAME/CONFIG_FILE_NAME.yaml`.

To run the `cloudbuild.yaml`, pass in the notifier path as a substitution variable.
    
    gcloud builds submit .  --substitutions=_CONFIG_PATH=gs://BUCKET_NAME/CONFIG_FILE_NAME
    

**Note:** Cloud Build hosts existing notifier images in [Artifact Registry](https://console.cloud.google.com/artifacts/docker/gcb-release/us-east1/cloud-build-notifiers?project=gcb-release). Since you are creating your own notifier instead of used one Cloud Build hosts, you need to build your notifier to create a notifier image. To see an example of a `cloudbuild.yaml` file for another notifier type, such as the `slack` notifier, see [`buildtest.cloudbuild.yaml`](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/slack/buildtest.cloudbuild.yaml). To see an example of the `Dockerfile` used in the `buildtest.cloudbuild.yaml` file, see [`Dockerfile`](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/slack/Dockerfile).
  4. Grant Pub/Sub permissions to create authentication tokens in your project:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
            --role=roles/iam.serviceAccountTokenCreator
         

Where:

     * `PROJECT_ID` is the ID of your Google Cloud project.
     * `PROJECT_NUMBER` is your Google Cloud project number.
  5. Create a service account to represent your Pub/Sub subscription identity:
         
         gcloud iam service-accounts create cloud-run-pubsub-invoker \
           --display-name "Cloud Run Pub/Sub Invoker"
         

You can use `cloud-run-pubsub-invoker` or use a name unique within your Google Cloud project.

  6. Give the `cloud-run-pubsub-invoker` service account the Cloud Run `Invoker` permission:
         
         gcloud run services add-iam-policy-binding SERVICE_NAME \
            --member=serviceAccount:cloud-run-pubsub-invoker@PROJECT_ID.iam.gserviceaccount.com \
            --role=roles/run.invoker
         

Where:

     * `SERVICE_NAME` is the name of the Cloud Run service to which you're deploying the image.
     * `PROJECT_ID` is the ID of your Google Cloud project.
  7. Create the `cloud-builds` topic to receive build update messages for your notifier:
         
         gcloud pubsub topics create cloud-builds
         

You can also define a custom topic name in your build config file so that messages are sent to the custom topic instead. In this case, you would create a topic with the same custom topic name:
         
         gcloud pubsub topics create topic-name
         

For more information, see [Pub/Sub topics for build notifications](https://docs.cloud.google.com/build/docs/configuring-notifications/notifiers#pubsub-topic-config).

  8. Create a Pub/Sub push subscriber for your notifier:



    
    
         gcloud pubsub subscriptions create subscriber-id \
           --topic=cloud-builds \
           --push-endpoint=SERVICE_URL \
           --push-auth-service-account=SUB_IDENTITY_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com
    

Where: \+ `SUBSCRIBER_ID` is the name you want to give your subscription. \+ `SERVICE_URL` is the Cloud Run-generated URL for your new service. \+ `PROJECT_ID` is the ID of your Google Cloud project.
    
    
    Note: By default, [subscriptions expire after 31 days of inactivity](/pubsub/docs/subscription-overview#lifecycle).
    You can adjust or disable the expiration period by including the
    [`--expiration-period` flag](/sdk/gcloud/reference/pubsub/subscriptions/create#--expiration-period)
    when creating the subscription.
    

Notifications for your Cloud Build project are now set up. The next time you invoke a build, you will receive a notification in your channel if the build matches the filter you've configured.

## Test notifications

To test notifications for the example used in this guide, you can invoke a build by running the `gcloud builds submit` command.

In the following example, we specify `success.yaml` as the configuration path. Running this command should result in a minimal successful build. You should also be able to see an output of your build logs.
    
    
     gcloud builds submit --no-source --config=success.yaml
    

Where `success.yaml` is:
    
    
     steps:
     - name: busybox
       args: ["true"]
    

In the following example, we specify `failure.yaml` as the configuration path. Running this command should result in a failed build. Instead of seeing an output of your build logs, you will see an output informing you that there was no match for the CEL filters you specified in your source.
    
    
    gcloud builds submit --no-source --config=failure.yaml
    

Where `failure.yaml` is:
    
    
     steps:
     - name: busybox
       args: ["false"]
    

If you created a notifier that's configured to perform another task other than logging output to Cloud Run service logs, you can also run the `gcloud builds submit` command to test your notifications. To examine errors associated with your build, check the Cloud Run logs for your service. To learn more, see [Viewing logs in Cloud Run](https://docs.cloud.google.com/run/docs/logging).

## What's next

  * Learn about [Cloud Build notifiers](https://docs.cloud.google.com/build/docs/configuring-notifications/notifiers).
  * Learn how to [subscribe to build notifications](https://docs.cloud.google.com/build/docs/subscribe-build-notifications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
