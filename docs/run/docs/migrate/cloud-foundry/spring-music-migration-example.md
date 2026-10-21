---
url: https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/spring-music-migration-example/
title: Sample Cloud Foundry to Cloud Run migration: Spring Music \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:45.284553+00:00
---

# Sample Cloud Foundry to Cloud Run migration: Spring Music  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/spring-music-migration-example/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Sample Cloud Foundry to Cloud Run migration: Spring Music Stay organized with collections  Save and categorize content based on your preferences. 

This sample migration uses the [Spring Music](https://github.com/cloudfoundry-samples/spring-music) project to show how a Cloud Foundry application can be built as an OCI-compliant application image. This sample is using the [lift and shift strategy](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/oci-compliant-strategy#modifying_a_cloud_foundry_application_lift_and_shift), which uses open source components from the Cloud Foundry ecosystem. After you create the application image, you need to configure the application for deployment to Cloud Run.

## Before you start

  * Make sure you have set up a new project for Cloud Run as described in the [setup](https://docs.cloud.google.com/run/docs/setup) page.
  * Make sure you have a `REGISTRY_URI` for storing containers. Cloud Run recommends using Artifact Registry.
  * If you are under a domain restriction organization policy [restricting](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) unauthenticated invocations for your project, you will need to access your deployed service as described under [Testing private services](https://docs.cloud.google.com/run/docs/triggering/https-request#testing-private).

  * Install Docker on your workstation. Docker is used to create intermediate images to build the project.



## Permissions required to deploy

For this guide you need permissions to build, store the built container image and deploy.

You must have the following roles:

  * [Cloud Build Editor role](https://docs.cloud.google.com/build/docs/iam-roles-permissions)
  * [Artifact Registry Admin role](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles)
  * [Storage Admin role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)
  * [Cloud Run Admin role](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run#fully-managed)
  * [Service Account User role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser)



### Project Structure

For this guide we suggest that you create a project directory e.g. `cr-spring-music/` and create sub-directories as you progress through the guide.
    
    
    cr-spring-music/
    ├── build
    ├── run
    └── spring-music
    
    

### Create the build Image

This section creates a build image using `cflinux3` as the base image. The build image is used as the build environment for creating the application image.

  1. Create a directory called `build/` and `cd` into it:
         
         mkdir build && cd build
         

  2. In the `build/` folder, create a new file called `Dockerfile` and paste in the following code:
         
         ARG CF_LINUX_FS=cloudfoundry/cflinuxfs3
         
         FROM golang:1.20-bullseye AS builder_build
         WORKDIR /build
         RUN ["git", "clone", "--depth=1", "https://github.com/cloudfoundry/buildpackapplifecycle.git"]
         WORKDIR /build/buildpackapplifecycle
         RUN ["go", "mod", "init", "code.cloudfoundry.org/buildpackapplifecycle"]
         RUN ["go", "mod", "tidy"]
         RUN CGO_ENABLD=0 go build -o /builder ./builder/
         
         FROM $CF_LINUX_FS
         # Set up container tools related to building applications
         WORKDIR /lifecycle
         COPY --from=builder_build /builder /lifecycle/builder
         
         # Set up environment to match Cloud Foundry's build.
         # https://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#app-system-env
         WORKDIR /staging/app
         WORKDIR /tmp
         ENV CF_INSTANCE_ADDR=127.0.0.1:8080 \
         CF_INSTANCE_IP=127.0.0.1 \
         CF_INSTANCE_INTERNAL_IP=127.0.0.1 \
         VCAP_APP_HOST=127.0.0.1 \
         CF_INSTANCE_PORT=8080 \
         LANG=en_US.UTF-8 \
         INSTANCE_GUID=00000000-0000-0000-0000-000000000000 \
         VCAP_APPLICATION={} \
         VCAP_SERVICES={} \
         CF_STACK=cflinuxfs3
         

  3. Use Cloud Build to build and publish the `builder` image
         
         gcloud builds \
             submit --tag "REGISTRY_URI/builder:stable"
         

Replace `REGISTRY_URI` with the address of the Artifact Registry where you want to publish the build image. For example: `REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/builder:stable`.




### Create the runtime Image

This section creates a run image using `cflinux3` as the base image. The run image is used as the base image when you create the final application image.

  1. Create a directory called `run/` and `cd` into it:
         
         mkdir run && cd run
         

  2. In the `run/` folder, create a new shell script called `entrypoint.bash` with the following code:
         
         #!/usr/bin/env bash
         set -e
         
         if [[ "$@" == "" ]]; then
         exec /lifecycle/launcher "/home/vcap/app" "" ""
         else
         exec /lifecycle/launcher "/home/vcap/app" "$@" ""
         fi
         

  3. In the `run/` folder, create a new file called `Dockerfile` and paste in the following code:
         
         ARG CF_LINUX_FS=cloudfoundry/cflinuxfs3
         
         FROM golang:1.20-bullseye AS launcher_build
         WORKDIR /build
         RUN ["git", "clone", "--depth=1", "https://github.com/cloudfoundry/buildpackapplifecycle.git"]
         WORKDIR /build/buildpackapplifecycle
         RUN ["go", "mod", "init", "code.cloudfoundry.org/buildpackapplifecycle"]
         RUN ["go", "mod", "tidy"]
         RUN CGO_ENABLD=0 go build -o /launcher ./launcher/
         
         FROM $CF_LINUX_FS
         # Set up container tools related to launching the application
         WORKDIR /lifecycle
         COPY entrypoint.bash /lifecycle/entrypoint.bash
         RUN ["chmod", "+rx", "/lifecycle/entrypoint.bash"]
         COPY --from=launcher_build /launcher /lifecycle/launcher
         
         # Set up environment to match Cloud Foundry
         WORKDIR /home/vcap
         USER vcap:vcap
         ENTRYPOINT ["/lifecycle/entrypoint.bash"]
         
         # Expose 8080 to allow app to be run on Cloud Foundry,
         # and PORT so the container can be run locally.
         # These do nothing on Cloud Run.
         EXPOSE 8080/tcp
         # Set up environment variables similar to Cloud Foundry.
         ENV CF_INSTANCE_ADDR=127.0.0.1:8080 \
         CF_INSTANCE_IP=127.0.0.1 \
         INSTANCE_IP=127.0.0.1 \
         CF_INSTANCE_INTERNAL_IP=127.0.0.1 \
         VCAP_APP_HOST=127.0.0.1 \
         CF_INSTANCE_PORT=80 \
         LANG=en_US.UTF-8 \
         CF_INSTANCE_GUID=00000000-0000-0000-0000-000000000000 \
         INSTANCE_GUID=00000000-0000-0000-0000-000000000000 \
         CF_INSTANCE_INDEX=0 \
         INSTANCE_INDEX=0 \
         PORT=8080 \
         VCAP_APP_PORT=8080 \
         VCAP_APPLICATION={} \
         VCAP_SERVICES={}
         

  4. Use Cloud Build to build and publish the `runtime` image:
         
         gcloud builds submit \
             --tag "REGISTRY_URI/runtime:stable"
         

Replace `REGISTRY_URI` with the address to the Artifact Registry where you want to publish the build image. For example: `REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/runtime:stable.`




### Build Spring Music for Cloud Foundry

To clone the [Spring Music](https://github.com/cloudfoundry-samples/spring-music) project and run the build commands as if we were deploying the project to Cloud Foundry:

  1. Clone the [Spring Music](https://github.com/cloudfoundry-samples/spring-music) repository:
         
         git clone https://github.com/cloudfoundry-samples/spring-music.git
         

  2. For the purposes of this guide, we will be using an older version of the Spring Music application that uses Java 8 and Spring Boot 2. To do this we will move to an older revision of the Spring Music project:
         
         git checkout 610ba471a643a20dee7a62d88a7879f13a21d6a3
         

  3. Move into the repository:
         
         cd spring-music
         

  4. Build the Spring Music binary:
         
         ./gradlew clean assemble
         




You now have a `build/` folder with the compiled Spring Music app ready to be pushed into a Cloud Foundry instance.

### Convert Spring Music into a Cloud Run compatible application

You must take the output of the build command to prepare the Spring Music artifact for deployment into Cloud Run.

  1. Create a staging directory `cr-app` and a `src` sub-directory inside of it:
         
         mkdir -p cr-app/src
         

  2. Mimic `cf push` by extracting the contents of the compiled JAR into the `src` directory:
         
         unzip build/libs/spring-music-1.0.jar -d cr-app/src
         

  3. Change directory into `cr-app/`:
         
         cd cr-app/
         

  4. Create a new file called `Dockerfile`. This `Dockerfile` will use the build image and runtime image created in the previous steps to create the runnable application image for Spring Music, using the Java buildpack.

  5. Paste the following code into the `Dockerfile`:
         
         ARG BUILD_IMAGE
         ARG RUN_IMAGE
         FROM $BUILD_IMAGE as build
         
         COPY src /staging/app
         COPY src /tmp/app
         
         ARG BUILDPACKS
         RUN /lifecycle/builder \
         -buildArtifactsCacheDir=/tmp/cache \
         -buildDir=/tmp/app \
         -buildpacksDir=/tmp/buildpacks \
         -outputBuildArtifactsCache=/tmp/output-cache \
         -outputDroplet=/tmp/droplet \
         -outputMetadata=/tmp/result.json \
         "-buildpackOrder=${BUILDPACKS}" \
         "-skipDetect=true"
         
         FROM $RUN_IMAGE
         COPY --from=build /tmp/droplet droplet
         RUN tar -xzf droplet && rm droplet
         




### Build Spring Music as an OCI compliant image

In this step, you instruct Cloud Build how to construct an OCI-compliant image using the build image, runtime image, and application Dockerfile created in the previous steps.

To create the OCI-compliant image:

  1. Create a file called `cloudbuild.yaml`. This is a [build configuration](https://docs.cloud.google.com/build/docs/build-config-file-schema) that will instruct Cloud Build how to build the application.

  2. Paste the following configuration into `cloudbuild.yaml`:
         
         steps:
         - name: gcr.io/cloud-builders/docker
           args:
           - 'build'
           - '--network'
           - 'cloudbuild'
           - '--tag'
           - '${_TAG}'
           - '--build-arg'
           - 'BUILD_IMAGE=${_BUILD_IMAGE}'
           - '--build-arg'
           - 'RUN_IMAGE=${_RUN_IMAGE}'
           - '--build-arg'
           - 'BUILDPACKS=${_BUILDPACKS}'
           - '.'
         images:
         - "${_TAG}"
         options:
           # Substitute build environment variables as an array of KEY=VALUE formatted strings here.
           env: []
         substitutions:
           _BUILD_IMAGE: REGISTRY_URI/builder:stable
           _RUN_IMAGE:  REGISTRY_URI/runtime:stable
           _BUILDPACKS: https://github.com/cloudfoundry/java-buildpack
           _TAG: REGISTRY_URI/spring-music:latest
         

     * Replace `REGISTRY_URI` with the URI of the container registry where you have published the builder and runner.
  3. Build the application image using Cloud Build:
         
         gcloud builds submit .
         

When the build completes, make note of the resulting image URI. You will need it when deploying the application in the next steps. The resulting image will be an OCI-compliant container image for running the Spring Music app, built using open source Cloud Foundry components.




### Deploy to Cloud Run

You must create a service definition file to use in Cloud Run:

  1. Create a service account for your application:
         
         gcloud iam service-accounts create spring-music
         

  2. Create a `service.yaml` file with the following code:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: "spring-music"
           # Set this to be the project number of the project you're deploying to.
           namespace: "PROJECT_NUMBER"
           labels:
             cloud.googleapis.com/location: us-central1
             migrated-from: cloud-foundry
           annotations:
             run.googleapis.com/ingress: all
         spec:
           template:
             metadata:
               annotations:
                 autoscaling.knative.dev/minScale: '1'
                 autoscaling.knative.dev/maxScale: '1'
                 run.googleapis.com/cpu-throttling: 'true'
                 run.googleapis.com/startup-cpu-boost: 'true'
                 run.googleapis.com/sessionAffinity: 'false'
             spec:
               containerConcurrency: 1000
               timeoutSeconds: 900
               serviceAccountName: spring-music@PROJECT_NUMBER.iam.gserviceaccount.com
               containers:
               - name: user-container
                 # Set the following value to either:
                 # - The image you built for your application in the last section of the guide.
                 image: SPRING_IMAGE_URI
                 ports:
                 - name: http1
                   containerPort: 8080
                 env:
                 - name: VCAP_APPLICATION
                   value: |-
                         {
                             "application_id": "00000000-0000-0000-0000-000000000000",
                             "application_name": "spring-music",
                             "application_uris": [],
                             "limits": {
                             "disk": 0,
                             "mem": 1024
                             },
                             "name": "spring-music",
                             "process_id": "00000000-0000-0000-0000-000000000000",
                             "process_type": "web",
                             "space_name": "none",
                             "uris": []
                         }
                 - name: MEMORY_LIMIT
                   value: '1024M'
                 resources:
                   limits:
                     memory: 1024Mi
                     cpu: "1"
                 startupProbe:
                   httpGet:
                     path: /
                     port: 8080
                   timeoutSeconds: 1
                   failureThreshold: 30
                   successThreshold: 1
                   periodSeconds: 2
                 livenessProbe:
                   httpGet:
                     path: /
                     port: 8080
                   timeoutSeconds: 1
                   failureThreshold: 1
                   successThreshold: 1
                   periodSeconds: 30
           traffic:
           - percent: 100
             latestRevision: true
         

     * Replace `PROJECT_NUMBER` with your project number.
     * Replace `SPRING_IMAGE_URI` with the URI of the application image created under build Spring Music as an OCI compliant image.
  3. Deploy the service to Cloud Run:
         
         gcloud run services replace service.yaml
         

Once the deployment completes, you will be able to visit the running Spring Music application at the deployed URL.




## What's Next

  * For a more in-depth look at the containerization process see [Migrate to OCI containers](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-to-oci-containers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
