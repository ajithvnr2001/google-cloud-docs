---
url: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/deploy-app-container-image/
title: Learning Path: Transform a monolith into a GKE app - Containerize the modular app \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:34:51.384336+00:00
---

# Learning Path: Transform a monolith into a GKE app - Containerize the modular app  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/deploy-app-container-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Learning Path: Transform a monolith into a GKE app - Containerize the modular app Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This is the fourth tutorial in a learning path that teaches you how to modularize and containerize a monolithic app.

The learning path consists of the following tutorials:

  1. [Overview](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/overview)
  2. [Understand the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/monolith)
  3. [Modularize the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/modular)
  4. [Prepare the modular app for containerization](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/prep-containerization)
  5. Containerize the modular app (this tutorial)
  6. [Deploy the app to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/deploy)



In the previous tutorial, [Prepare the modular app for containerization](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/prep-containerization), you saw what changes needed to be made to the modular version of the Cymbal Books app to prepare it for containerization. In this tutorial, you containerize the app.

## Costs

You can complete this tutorial without incurring any charges. However, following the steps in the [next tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/deploy) of this series incurs charges on your Google Cloud account. Costs begin when you enable GKE and deploy the Cymbal Books app to a GKE cluster. These costs include per-cluster charges for GKE, as outlined on the [Pricing page](https://cloud.google.com/kubernetes-engine/pricing), and charges for running Compute Engine VMs.

To avoid unnecessary charges, ensure that you disable GKE or delete the project once you've completed this tutorial.

## Before you begin

Before you begin this tutorial, make sure you completed the earlier tutorials in the series. For an overview of the whole series, and links to particular tutorials, see [Learning Path: Transform a monolith into a GKE app - Overview](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/overview).

## Set up your environment

In this section, you set up an environment in which you containerize the modular app. Specifically, you perform the following steps:

  1. Select or create a Google Cloud project
  2. Enable the necessary APIs
  3. Connect Cloud Shell to your Google Cloud project
  4. Set the default environment variables
  5. Create a repository in Artifact Registry
  6. Configure Docker for Artifact Registry
  7. Get the tutorial code



### Select or create a Google Cloud project

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Enable the necessary APIs

To work with container images and Kubernetes in your Google Cloud project, you need to enable the following APIs:

  * **Artifact Registry API** : this API enables Artifact Registry, which is a service for storing and managing your container images.
  * **Kubernetes Engine API** : this API provides access to GKE.



To enable these APIs, visit [enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com) in Google Cloud console.

### Connect Cloud Shell to your Google Cloud project

Now that you've set up your Google Cloud project, you need to launch a [Cloud Shell](https://docs.cloud.google.com/shell/docs) instance and connect it to your Google Cloud project. Cloud Shell is a command-line tool that lets you create and manage a project's resources directly from your browser. Cloud Shell comes preinstalled with two important tools: the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and the [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) CLI. In this tutorial, you use the gcloud CLI to interact with Google Cloud and in the next tutorial, you use the `kubectl` CLI to manage the Cymbal Books app that runs on GKE.

To connect a Cloud Shell instance with your Google Cloud project, follow these steps:

  1. Go to the Google Cloud console:

[Google Cloud console](https://console.cloud.google.com/)

  2. In the console, click the **Activate Cloud Shell** button: ![Activate Cloud Shell](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png)

A Cloud Shell session opens inside a frame lower on the console.

  3. Set your default project in the Google Cloud CLI using the following command:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the project ID of the project that you created or selected in the previous section, Select or create Google Cloud project. A project ID is a unique string that differentiates your project from all other projects in Google Cloud. To locate the project ID, go to the [project selector](https://console.cloud.google.com/projectselector2/home/dashboard). On that page, you can see the project IDs for each of your Google Cloud projects.




### Set the default environment variables

To simplify the commands that you run throughout this tutorial, you now set some environment variables in Cloud Shell. These variables store values such as your project ID, repository region, and image tag. After you define these variables, you can reuse them in multiple commands by referencing the variable name (for example, `$REPOSITORY_NAME`) instead of retyping or replacing values each time. This approach makes the tutorial easier to follow and reduces the risk of errors.

To set up your environment with Cloud Shell, perform the following steps:
    
    
    export PROJECT_ID=$(gcloud config get project)
    export REPOSITORY_REGION=REPOSITORY_REGION
    export REPOSITORY_NAME=REPOSITORY_NAME
    export REPOSITORY_DESCRIPTION="REPOSITORY_DESCRIPTION"
    export TAG=TAG
    

Replace the following:

  * `REPOSITORY_REGION`: the [region](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) where you want your Artifact Registry repository to be hosted. For example, `us-central1` (Iowa), `us-west1` (Oregon), or `europe-west1` (Belgium). For a complete list of regions, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * `REPOSITORY_NAME`: the name of your repository. For example, `book-review-service-repo`.
  * `REPOSITORY_DESCRIPTION`: a brief description of the repository's purpose. For example, `"Repository for storing Docker images for the book review service"`.
  * `TAG`: the tag that you want to apply to an image. A tag is a label that you can attach to a specific version of a container image. You can use tag naming conventions like these to clearly indicate different versions of an image: 
    * `v1`
    * `v1.2.3`
    * A descriptive tag, such as `feature-x-dev`
    * A tag that indicates the environment, such as `test`



### Create a repository in Artifact Registry

Next, you create a repository in Artifact Registry. A repository is a storage location where you keep container images. When you build a container image, you need somewhere to store it so that it can later be deployed to a Kubernetes cluster. Artifact Registry lets you create and manage these repositories within your Google Cloud project.

To create a repository in Artifact Registry, run the following command:
    
    
    gcloud artifacts repositories create ${REPOSITORY_NAME} \
        --repository-format=docker \
        --location=${REPOSITORY_REGION} \
        --description="${REPOSITORY_DESCRIPTION}"
    

Successful output from the command looks like the following:
    
    
    Waiting for operation [...] to complete...done.
    Created repository [book-review-service-repo].
    

## Configure Docker for Artifact Registry

Next, you configure Docker so that it can securely communicate with Google Cloud's Artifact Registry. Docker is a tool that you can use to package and run software in a consistent way across different environments. You learn more about how Docker works in the next section. For now, you need to configure it so that it can connect to Artifact Registry.

If you don't configure Docker in this way, you can't push the container images to Artifact Registry (a task you perform later in this tutorial). You also can't pull the container images from Artifact Registry and deploy them to a GKE cluster (a task you perform in the next tutorial).

To configure Docker to authenticate with Artifact Registry, run this command:
    
    
    gcloud auth configure-docker ${REPOSITORY_REGION}-docker.pkg.dev
    

## Get the tutorial code

Now that your Cloud Shell environment is configured, you need to download the tutorial code within Cloud Shell. Even if you previously cloned the repository on your local machine, you need to clone it again here on your Cloud Shell instance.

Although it's possible to complete this tutorial on your local machine, you would have to manually install and configure several tools such as Docker, `kubectl`, and gcloud CLI. Using Cloud Shell is easier because it comes preconfigured with all of these tools.

In your Cloud Shell instance, run the following command to clone the GitHub repository:
    
    
    git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
    

## Containerization basics: container images, containers, and Dockerfiles

Now that you have set up your environment and downloaded the containerized code, you're ready to containerize the app. Containerizing the app consists of using a Dockerfile to package each module of Cymbal Books (homepage, book details, images, and book reviews) into a container image. When the application is deployed to the GKE cluster, Kubernetes uses these container images to create running containers in the cluster.

The following sections explain these concepts in detail.

### What is containerization?

Containerization packages a module and all its dependencies, such as libraries and configuration files, into a unit called a container image. Developers use this container image to create and run containers across any environment—from a developer's laptop to a testing server or a production Kubernetes cluster.

### What are container images?

A container image contains all the files that are needed to run an application. These files include the application code itself, system libraries, the runtime environment (for example, the Python interpreter), static data, and any other dependencies.

In this tutorial, you create a container image for each module of the book reviews app.

### What is a container?

A container is an isolated environment where code from a container image runs. You can create containers in two ways: by using the `docker run` command for testing during development, or by deploying container images to a Kubernetes cluster.

In the containerized version of the Cymbal Books app, each module from the modular app runs in its own container:

  * The homepage container runs the homepage module and handles requests to `/`.
  * The book details container runs the book details module and serves data for endpoints such as `/book/1` or `/book/3`.
  * The book reviews container runs the book reviews module and manages requests to endpoints such as `/book/2/reviews`.
  * The images container runs the images module and serves book cover images for endpoints such as `/images/fungi_frontier.jpg`.



A key advantage of containers is that Kubernetes can automatically create more containers when needed. For example, if numerous users are reading book reviews, Kubernetes can start additional book reviews containers to handle the load.

To implement scaling in a modular app that doesn't use containers, you'd need to write custom code to launch new instances of a module and distribute traffic between them. With Kubernetes, this scaling capability is built-in: you don't need to write any custom scaling code.

### What are Dockerfiles?

A Dockerfile is a script that defines how to package a module into a container image. In this tutorial, you don't need to create any Dockerfiles—they're already provided for you in the GitHub repository you cloned earlier. Each module's directory in your local copy of `kubernetes-engine-samples/quickstarts/monolith-to-microservices/containerized/` contains its own Dockerfile.

For example, you can find the `home_app` module's Dockerfile in your Cloud Shell instance at `kubernetes-engine-samples/quickstarts/monolith-to-microservices/containerized/home_app/Dockerfile`. This Dockerfile looks like the following:
    
    
    # Dockerfile for home_app
    FROM python:3.9-slim #line 1
    WORKDIR /app #line 2
    COPY requirements.txt . #line 3
    RUN pip install --no-cache-dir -r requirements.txt #line 4
    COPY home_app.py . #line 5
    COPY templates/ ./templates/ #line 6
    COPY static/ ./static/ #line 7
    CMD ["python", "home_app.py"] #line 8
    

This Dockerfile performs the following steps to create the container image for the `home_app` module:

  * **Line 1:** `FROM python:3.9-slim` downloads a Python 3.9 interpreter and its required files into the container image. These files enable the module to run.
  * **Line 2:** `WORKDIR /app` creates a directory called `/app` inside the container and sets this directory as the current working directory. All commands that are run inside the container will run from within this directory.
  * **Lines 3 and 4:** `COPY requirements.txt .` copies the `requirements.txt` file from your local machine into the container image's `/app` directory. The `requirements.txt` file lists all the Python libraries that `home_app.py` needs. The line `RUN pip install` installs those libraries into the container image.
  * **Lines 5 to 7:** The `COPY` commands that appear in these lines copy the module's code (`home_app.py`) and its supporting files (templates and static assets) to the `/app` directory within the container image.
  * **Line 8:`CMD`** specifies the default command that Docker runs when the container starts. In this Dockerfile, `CMD ["python", "home_app.py"]` tells Docker to use the Python interpreter to execute the `home_app.py` module automatically when the container is launched.



### How containerization can enforce stricter data isolation

Lines 5 to 7 of the Dockerfile, which were described in the previous section, show how containerization can enforce stricter data isolation than the modularized version of the app. In a previous tutorial, in the section [Give each module access to only the data it needs](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/modular#only-data-needed), you learned that the modular version of the app organized data into separate directories, but modules still shared the same file system and could potentially access each other's data.

Here, in the containerized version of the app, each module's container includes only its necessary files. For example, if the `home_app` module doesn't need access to book reviews data, that data simply doesn't exist inside the `home_app` container. By default, a container can't access files from another container unless explicitly configured to do so. This helps ensure that each module is fully isolated, and also helps prevent accidental or unauthorized data access.

In the next section, you see how the `docker build` command takes a Dockerfile as input, and follows the instructions in the Dockerfile to create a container image.

## Build container images using Docker

In this section, you build Docker container images for each of the book review modules and push them to your Artifact Registry repository. You'll use these container images in a following tutorial to deploy and run the Cymbal Books sample app in Kubernetes.

  1. Navigate to the root directory of the containerized application:
         
         cd kubernetes-engine-samples/quickstarts/monolith-to-microservices/containerized/
         

  2. Create the container images by using the `docker build` command:
         
         docker build -t ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/home-app:${TAG} ./home_app
         docker build -t ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/book-details-app:${TAG} ./book_details_app
         docker build -t ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/book-reviews-app:${TAG} ./book_reviews_app
         docker build -t ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/images-app:${TAG} ./images_app
         

  3. View the container images that were built inside your Cloud Shell instance:
         
         docker images
         

Check that the following images appear in the list:

     * `home-app`
     * `book-details-app`
     * `book-reviews-app`
     * `images-app`

If all four images are listed, you successfully created the container images.




## Test containers in Cloud Shell

To verify that the container images are built correctly, you can run them as containers and test their endpoints in Cloud Shell.

The `book_details_app`, `book_reviews_app`, and `images_app` containers can be tested individually because they don't need to communicate with each other. However, testing the `home_app` container by using Docker is difficult because `home_app`is configured to find the other containers that use service names such as `http://book-details-service:8081`.

Although it's possible to test the `home_app` container by finding each container's IP address and configuring `home_app` to use them instead of service names, this approach requires a lot of effort. Instead, it's a good idea to defer testing the `home_app` container until after you deploy the application to a Kubernetes cluster. After the app is on the cluster, you can determine whether the home module is working correctly.

Follow these steps to test the containers:

  1. Start the `book_details_app`, `book_reviews_app`, and `images_app` containers:
         
         docker run -d -p 8081:8080 ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/book-details-app:${TAG}
         docker run -d -p 8082:8080 ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/book-reviews-app:${TAG}
         docker run -d -p 8083:8080 ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/images-app:${TAG}
         

  2. Check that the containers are running by listing all active containers:
         
         docker ps
         

Output from this command should show three containers that are running, with the status `Up`:
         
         CONTAINER ID   IMAGE                PORTS                        STATUS
         a1b2c3d4e5f6   REGION/.../details   0.0.0.0:8081->8080/tcp       Up
         g7h8i9j0k1l2   REGION/.../reviews   0.0.0.0:8082->8080/tcp       Up
         m3n4o5p6q7r8   REGION/.../images    0.0.0.0:8083->8080/tcp       Up
         

  3. To test the endpoints of the `book_details_app` container, use the following `curl` commands:
         
         curl http://localhost:8081/books
         curl http://localhost:8081/book/1
         curl http://localhost:8081/book/2
         curl http://localhost:8081/book/3
         

Each of these commands returns data in JSON format. For example, the output from the `curl http://localhost:8081/book/1` command looks like this:
         
         {"author":"Aria Clockwork","description":"In a world where time is a tangible substance, a young clockmaker discovers she can manipulate the fabric of time itself, leading to unforeseen consequences in her steampunk-inspired city.","id":1,"image_url":"zephyrs_timepiece.jpg","title":"Zephyr's Timepiece","year":2023}
         

  4. Retrieve book reviews from the `book_reviews_app` container by using this `curl` command:
         
         curl http://localhost:8082/book/1/reviews
         

This command returns a list of 20 reviews of book 1 in JSON format. Here's an example of one review from the list:
         
         {
         "content": "The concept of time as a tangible substance is brilliantly explored in 'Zephyr's Timepiece'.",
         "rating": 5
         }
         

  5. Test the `images_app` container:

     1. Click the `**Web Preview**` button ![Web Preview Button](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg)

     2. Select **Change port** and enter 8083. A browser window opens with a URL similar to this:
            
            https://8083-your-instance-id.cs-your-region.cloudshell.dev/?authuser=0
            

     3. Remove `?authuser=0` at the end of the URL and add the path to an image file, such as `/images/fungi_frontier.jpg`. The following is an example:
            
            https://8083-your-instance-id.cs-your-region.cloudshell.dev/images/fungi_frontier.jpg
            

You should see the book cover image for _Fungi Frontier_ displayed in your browser.

  6. After testing, stop the containers to release resources:

     1. List the running containers and find their container IDs:
            
            docker ps
            

     2. Stop each container:
            
            docker stop CONTAINER_ID
            

Replace `CONTAINER_ID` with the ID of the container you want to stop.




## Push the container images to Artifact Registry

Before you can deploy your app to a Kubernetes cluster, the container images need to be stored in a location that the cluster can access. In this step, you push the images to the Artifact Registry repository you created earlier. In the next tutorial, you deploy those images from the Artifact Registry repository to a GKE cluster:

  1. To push your container images to Artifact Registry, run these commands:
         
         docker push ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/home-app:${TAG}
         docker push ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/book-details-app:${TAG}
         docker push ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/book-reviews-app:${TAG}
         docker push ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/images-app:${TAG}
         

  2. After pushing the images, verify that they were successfully uploaded by listing them:
         
         gcloud artifacts docker images list ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}
         

You should see output similar to the following:
         
         Listing items under project ${PROJECT_ID}, location ${REPOSITORY_REGION}, repository ${REPOSITORY_NAME}.
         
         IMAGE: ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/book-details-app
         DIGEST: sha256:f7b78f44d70f2eedf7f7d4dc72c36070e7c0dd05daa5f473e1ebcfd1d44b95b1
         CREATE_TIME: 2024-11-14T00:38:53
         UPDATE_TIME: 2024-11-14T00:38:53
         SIZE: 52260143
         
         IMAGE: ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/book-reviews-app
         DIGEST: sha256:875ac8d94ef54db2ff637e49ad2d1c50291087623718b854a34ad657748fac86
         CREATE_TIME: 2024-11-14T00:39:04
         UPDATE_TIME: 2024-11-14T00:39:04
         SIZE: 52262041
         
         IMAGE: ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/home-app
         DIGEST: sha256:70ddc54ffd683e2525d87ee0451804d273868c7143d0c2a75ce423502c10638a
         CREATE_TIME: 2024-11-14T00:33:56
         UPDATE_TIME: 2024-11-14T00:33:56
         SIZE: 52262412
         
         IMAGE: ${REPOSITORY_REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/images-app
         DIGEST: sha256:790f0d8c2f83b09dc3b431c4c04d7dc68254fecc76c48f00a83babc2a5dc0484
         CREATE_TIME: 2024-11-14T00:39:15
         UPDATE_TIME: 2024-11-14T00:39:15
         SIZE: 53020815
         

The output includes the following details for each image:

     * **IMAGE** : the repository path and image name.
     * **DIGEST** : a unique identifier for the image.
     * **CREATE_TIME or UPDATE_TIME** : when the image was created or last modified.
     * **SIZE** : the size of the image in bytes.



## Update the Kubernetes manifest with paths to container images

As you learned in the previous tutorial, [Prepare the modular app for containerization](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/prep-containerization), a Kubernetes manifest is a YAML file that defines how your app runs in a Kubernetes cluster. It includes details such as the following:

  * The modules of your app (for example,`home-app`, `book-details-app`)
  * Paths to the container images
  * Configuration details such as resource limits
  * Service definitions for routing requests between modules



In this section, you update the same manifest file that you reviewed in the previous tutorial. That file is `kubernetes-manifest.yaml` and it contains placeholder values for the image paths. You need to replace those placeholders with the actual paths to the container images you pushed to your Artifact Registry repository in the previous section.

To update the `kubernetes-manifest.yaml` Kubernetes manifest file, follow these steps:

  1. In Cloud Shell, navigate to the `containerized/` directory, which contains the Kubernetes manifest file `kubernetes-manifest.yaml`:
         
         cd kubernetes-engine-samples/quickstarts/monolith-to-microservices/containerized/
         

  2. Open the `kubernetes-manifest.yaml` file in a text editor:
         
         vim kubernetes-manifest.yaml
         

  3. Locate the `image` fields that contain placeholders such as this:
         
         image: REPOSITORY_REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/home-app:TAG
         

Replace each placeholder with the actual paths to the container images that you pushed to Artifact Registry:

     * `REPOSITORY_REGION`: the region that you specified when you created a repository in Artifact Registry.

     * `PROJECT_ID`: your Google Cloud project ID, which you can find in the [project selector](https://console.cloud.google.com/projectselector2/home/dashboard) page.

     * `REPOSITORY_NAME`: the name of your repository, which you specified when you created a repository in Artifact Registry. For example, `book-review-service-repo`.

     * `TAG`: the tag that you chose when you Built the container images.

Here's what a path might look like after making these replacements:
    
    image:us-west1-docker.pkg.dev/your-project-id/book-review-service-repo/home-app:v1
    

  4. Update the paths for all container images:

     * `home-app`
     * `book-details-app`
     * `book-reviews-app`
     * `images-app`
  5. After you update the paths, save the manifest file and close the editor. For example, if you're using vim, press `Esc` to enter command mode, type `wq`, and press `Enter` to save and exit.




Your Kubernetes manifest is now configured to deploy the container images from your Artifact Registry repository to a Kubernetes cluster.

## Summary

In this tutorial, you prepared the modular Cymbal Books app for deployment to a Kubernetes cluster by performing the following tasks:

  1. Set up a Google Cloud project and configured Cloud Shell for your environment.
  2. Reviewed the provided Dockerfiles for each app module.
  3. Built container images for the app modules by using Docker.
  4. Tested containers in Cloud Shell to verify their functionality.
  5. Pushed the container images to Artifact Registry for storage.
  6. Updated the Kubernetes manifest to use the correct container image paths from Artifact Registry.



## What's next

In the next tutorial, [Deploy the app to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/deploy), you deploy the containerized application to a GKE cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
