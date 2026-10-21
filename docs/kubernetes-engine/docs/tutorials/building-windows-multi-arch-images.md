---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/building-windows-multi-arch-images/
title: Building Windows Server multi-arch images \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:27.656793+00:00
---

# Building Windows Server multi-arch images  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/building-windows-multi-arch-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Building Windows Server multi-arch images Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial demonstrates how to manage the versioning complexity of building images that target multiple Windows Server versions. Windows Server containers have [version compatibility requirements](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#version_compatibility) that prevent containers from running on more than one Windows Server host version. However, Docker on Windows Server supports multi-arch (or multi-platform) container images that can run across multiple Windows Server versions. 

With multi-arch images, you can upgrade your Google Kubernetes Engine (GKE) Windows Server node pools to your preferred Windows Server version without rebuilding the image and changing the Pod specs. For example:

  * GKE version 1.15 supports Windows Server 1809
  * GKE version 1.16 supports Windows Server 1909



To upgrade from one GKE version to a later version automatically, you must build multi-arch images for your Windows workloads. Building a multi-arch image involves building an image for each Windows Server version, and then building a manifest that references those images for each Windows Server version. You can build the images manually if you want full control over the image creation and build process. Alternatively, you can use Cloud Build to automatically build the Windows Server multi-arch images.

## Objectives

In this tutorial, you learn how to create Windows Server multi-arch images manually or by using Cloud Build. 

  * Build the images manually:

    * Create 2 Docker images with different versions or types of Windows Server, for example Long-Term Servicing Channel (LTSC) 2019 and LTSC 2022.
    * Create a Windows Server VM.
    * Create a manifest and push it to the registry.
  * Build the images using Cloud Build:

    * Prepare your environment by creating a project, enabling APIs, and granting permissions.
    * Create an application, Dockerfiles, and build files.
    * Run a command to build the image.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://cloud.google.com/compute/pricing)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/pricing)
  * [Cloud Build](https://cloud.google.com/build/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  1. [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) to run `gcloud` commands.
  2. [Install Docker](https://docs.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=Windows-Server) to build containers.
  3. [Install Go](https://golang.org/doc/install) to build Windows Server binaries.
  4. This tutorial uses Artifact Registry as the repository. Ensure you have [created your Docker repository](https://docs.cloud.google.com/artifact-registry/docs/manage-repos).

**Note:** The `gcloud` commands in this tutorial assume you are using a Linux machine.

## Building multi-arch images manually

**Warning:** The instructions in this section make use of an [ experimental feature in Docker](https://docs.docker.com/engine/reference/commandline/manifest) which should not be used in production environments. Consider the implications of enabling this feature on your systems.

Building multi-arch images manually provides you with the flexibility to build an image that includes any Windows Server versions that you need. To build a multi-arch image manually:

  1. Create an LTSC 2019 Docker single-arch image. See details about creating Docker images in [Deploying a Windows Server application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-windows-app#create_a_windows_server_application_image_for_use_with_private_clusters). For example, `us-docker.pkg.dev/my-project/docker-repo/foo:1.0-2019`.
  2. Create an LTSC 2022 Docker single-arch image. For example, `us-docker.pkg.dev/my-project/docker-repo/foo:1.0-2022`
  3. Create a Windows Server VM, for example version 20H2. See the [Quickstart using a Windows Server VM](https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance).
  4. Use RDP to connect to the VM.
  5. Open a PowerShell window to run the commands in the next steps.
  6. Enable the `docker manifest` experimental feature. A Docker manifest is a list of images to push to a registry:
         
         PS C:\> $env:DOCKER_CLI_EXPERIMENTAL = 'enabled'
         

  7. Create the multi-arch manifest:
         
         docker manifest create `
           REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/foo:1.0 `
           REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/foo:1.0-2019 `
           REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/foo:1.0-2022 `
         

  8. Push the newly created multi-arch image manifest to your Artifact Registry repository:
         
         docker manifest push `
            REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/foo:1.0
         

  9. To ensure that your multi-arch image was built and pushed successfully, navigate to `REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/foo` and click on that image. You'll see the 3 images inside:

     * `foo:1.0-2019`
     * `foo:1.0-2022`
     * `foo:1.0-20h2`
     * `foo:1.0`



Now you can refer to the multi-arch image `REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/foo:1.0` in your Pod specs. This will let you safely use auto-upgrade for your GKE Windows node pools.

## Building multi-arch images using the Cloud Build gke-windows-builder

To ease the effort of the manual build steps, you can use the [gke-windows-builder](https://console.cloud.google.com/artifacts/docker/gke-windows-tools/us/docker-repo/gke-windows-builder) based on the [OSS gke-windows-builder](https://github.com/GoogleCloudPlatform/kubernetes-engine-windows-tools/tree/master/gke-windows-builder). You can use the gke-windows-builder with Cloud Build to build the Windows Server multi-arch images automatically. GKE updates the builder to include new supported Windows LTSC versions when they are released. Another benefit of using the builder is that you don't have to create your own Windows VM with Powershell to build the images. The Windows VM is replaced by a Docker container that runs the commands for you inside Cloud Build.

To help you understand how the builder works, follow this example to build a "hello world" multi-arch image. These steps can be performed on Linux or Windows servers.

### Preparing the environment

To prepare your environment, complete the following steps:

  1. Create a workspace directory on your work machine, for example: `~/gke-windows-builder/hello-world`.
  2. Create or select a project for this tutorial.
  3. Make sure that [billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project) for your project.
  4. Enable the Compute Engine, Cloud Build and Artifact Registry APIs for your project. The gke-windows-builder is invoked using Cloud Build, and the resulting multi-arch container images are pushed to Artifact Registry. Compute Engine is required for the builder to create and manage Windows Server VMs.
         
         gcloud services enable compute.googleapis.com cloudbuild.googleapis.com \
           artifactregistry.googleapis.com cloudbuild.googleapis.com
         

  5. Grant the following Identity and Access Management (IAM) roles to your Cloud Build service account by using the Google Cloud CLI:

     1. Set variables:
            
            export PROJECT=$(gcloud info --format='value(config.project)')
            export MEMBER=$(gcloud projects describe $PROJECT --format 'value(projectNumber)')@cloudbuild.gserviceaccount.com
            

     2. Assign roles. These roles are required for the builder to create the Windows Server VMs, to copy the workspace to a Cloud Storage bucket, to configure the networks to build the Docker image and to push resulting image to Artifact Registry:
            
            gcloud projects add-iam-policy-binding $PROJECT --member=serviceAccount:$MEMBER --role='roles/compute.instanceAdmin'
            gcloud projects add-iam-policy-binding $PROJECT --member=serviceAccount:$MEMBER --role='roles/iam.serviceAccountUser'
            gcloud projects add-iam-policy-binding $PROJECT --member=serviceAccount:$MEMBER --role='roles/compute.networkViewer'
            gcloud projects add-iam-policy-binding $PROJECT --member=serviceAccount:$MEMBER --role='roles/storage.admin'
            gcloud projects add-iam-policy-binding $PROJECT --member=serviceAccount:$MEMBER --role='roles/artifactregistry.writer'
            gcloud projects add-iam-policy-binding $PROJECT --member=serviceAccount:$MEMBER --role='roles/cloudbuild.builds.editor'
            

  6. Add a firewall rule named `allow-winrm-ingress` to allow WinRM to connect to Windows Server VMs to run a Docker build:

**Note:** The firewall rule name must be `allow-winrm-ingress`, as gke-windows-builder uses this particular name to check whether this firewall rule exists.
         
         gcloud compute firewall-rules create allow-winrm-ingress --allow=tcp:5986 --direction=INGRESS
         

  7. Create a Docker repository in Artifact Registry for your project. If you have never used Docker repositories in Artifact Registry before, complete the [Quickstart for Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/quickstart) first. Run this command to create your repository:
         
         gcloud artifacts repositories create REPOSITORY \
           --repository-format=docker --location=REGISTRY_REGION \
           --description="Docker repository"
         

Replace the following:

     * `REPOSITORY`: a name such as `windows-multi-arch-images`.
     * `REGISTRY_REGION`: a valid [Artifact Registry location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations).



### Creating the hello.exe binary in your workspace

For this tutorial, create a simple "hello world" application, written in Go. The code for the sample app is [on GitHub](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/windows/windows-multi-arch).

  1. Clone the repository containing the sample code for this tutorial to your local machine by using the following commands:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
          cd kubernetes-engine-samples/windows/windows-multi-arch
         

  2. The `hello.go` file prints the words "Hello World":
         
         package main
         
         import "fmt"
         
         func main() {
         	fmt.Println("Hello World!")
         }
         

  3. Generate the `hello.exe` binary:
         
         GOOS=windows go build hello.go
         




You'll see the `hello.exe` binary in your workspace.

### Creating a Dockerfile and build files in your workspace

In this section you use a `Dockerfile` to build each _single-arch_ Windows Server image and then use a build file to trigger the Cloud Build. The build combines the single-arch images into a multi-arch image.

  1. The `Dockerfile` is a text document that contains instructions for Docker to build an image. The gke-windows-builder replaces the `WINDOWS_VERSION` with a specific Windows Server version to build the image for. For example, the builder will run `docker build -t multi-arch-helloworld:latest_20h2 --build-arg WINDOWS_VERSION=20H2 .` on Windows Server 20H2.
         
         ARG WINDOWS_VERSION=
         FROM mcr.microsoft.com/windows/servercore:${WINDOWS_VERSION}
         COPY hello.exe /hello.exe
         USER ContainerUser
         ENTRYPOINT ["hello.exe"]

  2. In the same directory that contains the `Dockerfile`, the `cloudbuild.yaml` file is your build config file. Replace <REPOSITORY> and <REGISTRY_REGION> with the name and region for the Artifact Registry repository that you created in the previous step. At build time, Cloud Build automatically replaces `$PROJECT_ID` with your project ID.
         
         timeout: 3600s
         steps:
         - name: 'us-docker.pkg.dev/gke-windows-tools/docker-repo/gke-windows-builder:latest'
           args:
           - --container-image-name
           # Replace <REGISTRY_REGION> and <REPOSITORY>.
           - '<REGISTRY_REGION>-docker.pkg.dev/$PROJECT_ID/<REPOSITORY>/multiarch-helloworld:latest'
           # Specify specific variants of images to be built. Or, remove the following 2 lines to default to all available variants.
           - --versions
           - '20H2,ltsc2019'




### Building the image

Now you can build the image and view your logs to verify a successful build.

  1. To build the image, run the following command:
         
         gcloud builds submit --config=cloudbuild.yaml .
         

**Note:** This command takes several minutes to complete.
  2. You'll see logs like the following example. The last line in the log shows that the build succeeded:
         
         Creating temporary tarball archive of 2 file(s) totalling 492 bytes before compression.
         Uploading tarball of [.] to [gs://PROJECT_ID_cloudbuild/source/1600082502.509759-b949721a922d462c94a75da9be9f1181.tgz]
         Created [https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/builds/ec333452-1301-47e8-90e2-716aeb2f5650].
         Logs are available at [https://console.cloud.google.com/cloud-build/builds/ec333452-1301-47e8-90e2-716aeb2f5650?project=840737568665].
         ------------------------ REMOTE BUILD OUTPUT---------------------------------------
         ...
         ...
         
         Created manifest list REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/multiarch-helloworld:latest
         sha256:3ecbbc9f5144f358f81f7c7f1a7e28f069c98423d59c40eaff72bf184af0be02
         2020/09/14 11:34:25 Instance: 35.184.178.49 shut down successfully
         PUSH
         DONE
         -----------------------------------------------------------------------------------
         
         ID                                    CREATE_TIME                DURATION  SOURCE                                                                                      IMAGES  STATUS
         ec333452-1301-47e8-90e2-716aeb2f5650  2020-09-14T11:21:43+00:00  12M43S    gs://PROJECT_ID_cloudbuild/source/1600082502.509759-b949721a922d462c94a75da9be9f1181.tgz  -                 SUCCESS
         




You've just built the image using the build config file and pushed the image to Artifact Registry at `REGISTRY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/multiarch-helloworld:latest`.

### Deploying the image

To deploy the multi-arch Windows image onto a cluster, see [Deploying a Windows Server application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-windows-app) to learn how to deploy the image.

### Advanced gke-windows-builder usage

You can customize the behavior of the gke-windows-builder by adding flags to the `args` section of the `cloudbuild.yaml` build config file. Some flags for common behaviors are described in this section, but this is not an exhaustive list; to see the full list of flags that gke-windows-builder supports, run the following command on a Linux server or in [Cloud Shell](https://ssh.cloud.google.com/cloudshell/editor?shellonly=true):
    
    
    docker run -it us-docker.pkg.dev/gke-windows-tools/docker-repo/gke-windows-builder:latest --help
    

To speed up your builds you can use a larger machine type for the Windows instances:
    
    
      - --machineType
      - 'n1-standard-8'
    

Instead of building the image for all Windows versions that GKE supports, you can choose specific Windows Server versions to build for by using the `--versions` flag:
    
    
      - --versions
      - '20H2,ltsc2019'
    

If your workspace has many files, your image build will be more reliable if you configure the builder to copy the workspace via Cloud Storage rather than WinRM. [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) in your project, such as `gs://{your project}_builder`, then set the `--workspace-bucket` flag:
    
    
      - --workspace-bucket
      - '{your project}_builder'
    

To run the Windows builder instances in a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) service project, use these flags that control the instance's network setup:
    
    
      - --subnetwork-project
      - 'shared-vpc-host-project'
      - --subnetwork
      - 'host-project-subnet-shared-with-service-project'
    

## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Deleting the image

To delete the `multiarch-helloworld` images on Artifact Registry, see [Deleting images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images).

### Deleting the project

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



## What's next

  * Explore other [Kubernetes Engine tutorials](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials). 

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
