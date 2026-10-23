---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster/
title: Quickstart: Deploy an app to a GKE cluster \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:32.218718+00:00
---

# Quickstart: Deploy an app to a GKE cluster  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy an app to a GKE cluster

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

In this quickstart, you deploy a sample web server [containerized application](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview#workloads) to a Google Kubernetes Engine (GKE) cluster. You learn how to create a cluster, and how to deploy the application to the cluster so that it can be accessed by users.

This page is for Operators and Developers who provision and configure cloud resources and deploy apps and services. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with [Kubernetes](https://kubernetes.io).

## Before you begin

Take the following steps to enable the Kubernetes Engine API: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Artifact Registry and Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Artifact Registry and Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com)




### Required roles

Grant roles to your user account. Run the following command once for each of the following IAM roles: ``roles/container.admin``
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
  * `ROLE`: The IAM role that you grant to your user account.



## Launch Cloud Shell

In this tutorial you will use [Cloud Shell](https://docs.cloud.google.com/shell/docs), which is a shell environment for managing resources hosted on Google Cloud.

Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and [kubectl](https://kubernetes.io/docs/reference/kubectl/) command-line tool. The gcloud CLI provides the primary command-line interface for Google Cloud, and `kubectl` provides the primary command-line interface for running commands against Kubernetes clusters.

Launch Cloud Shell:

  1. Go to the Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. From the upper-right corner of the console, click the **Activate Cloud Shell** button: ![](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png)




A Cloud Shell session opens inside a frame lower on the console. You use this shell to run `gcloud` and `kubectl` commands. Before you run commands, set your default project in the Google Cloud CLI using the following command:
    
    
    gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with your [project ID](https://support.google.com/cloud/answer/6158840).

## Create a GKE cluster

A [_cluster_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) consists of at least one _cluster control plane_ machine and multiple worker machines called _nodes_. Nodes are [Compute Engine virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/instances) that run the Kubernetes processes necessary to make them part of the cluster. You deploy applications to clusters, and the applications run on the nodes.

This section shows you how to create a cluster in _Autopilot mode_ , which is the recommended cluster mode for most production use cases. You could alternatively use a [GKE Standard mode cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster) to do these steps.

Create an Autopilot cluster named `hello-cluster`:
    
    
    gcloud container clusters create-auto hello-cluster \
        --location=us-central1
    

It might take several minutes to finish creating the cluster.

### Get authentication credentials for the cluster

After creating your cluster, you need to get authentication credentials to interact with the cluster:
    
    
    gcloud container clusters get-credentials hello-cluster \
        --location us-central1
    

This command configures `kubectl` to use the cluster you created.

## Deploy an application to the cluster

Now that you have created a cluster, you can deploy a [containerized application](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview#workloads) to it. For this quickstart, you can deploy our example web application, `hello-app`.

GKE uses Kubernetes objects to create and manage your cluster's resources. Kubernetes provides the [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) object for deploying stateless applications like web servers. [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) objects define rules and load balancing for accessing your application from the internet.

### Create the Deployment

To run `hello-app` in your cluster, you need to deploy the application by running the following command:
    
    
    kubectl create deployment hello-server \
        --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
    

This Kubernetes command, [`kubectl create deployment`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create), creates a Deployment named `hello-server`. The Deployment's [Pod](https://kubernetes.io/docs/concepts/workloads/pods) runs the `hello-app` container image.

In this command:

  * `--image` specifies a container image to deploy. In this case, the command pulls the example image from an [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) repository, `us-docker.pkg.dev/google-samples/containers/gke/hello-app`. `:1.0` indicates the specific image version to pull. If you don't specify a version, the image with the default `latest` tag is used.



### Expose the Deployment

After deploying the application, you need to expose it to the internet so that users can access it. You can expose your application by creating a Service, a Kubernetes resource that exposes your application to external traffic.

To expose your application, run the following [`kubectl expose`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#expose) command:
    
    
    kubectl expose deployment hello-server \
        --type LoadBalancer \
        --port 80 \
        --target-port 8080
    

Passing in the `--type LoadBalancer` flag creates a Compute Engine load balancer for your container. The `--port` flag initializes public port 80 to the internet and the `--target-port` flag routes the traffic to port 8080 of the application.

Load balancers are billed per Compute Engine's [load balancer pricing](https://docs.cloud.google.com/compute/pricing#lb).

### Inspect and view the application

  1. Inspect the running Pods by using [`kubectl get pods`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get):
         
         kubectl get pods
         

You should see one `hello-server` Pod running on your cluster.

  2. Inspect the `hello-server` Service by using [`kubectl get service`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get):
         
         kubectl get service hello-server
         

From this command's output, copy the Service's external IP address from the `EXTERNAL-IP` column.

**Note:** You might need to wait several minutes before the Service's external IP address populates. If the application's external IP is `<pending>`, run `kubectl get` again.
  3. View the application from your web browser by using the external IP address with the exposed port:
         
         http://EXTERNAL_IP
         




You have just deployed a containerized web application to GKE.

To track and organize your GKE resources in an application-centric way, you can add your resources as Services and workloads to [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) applications.

For more information on resources that App Hub supports, see [Supported resources](https://docs.cloud.google.com/app-hub/docs/supported-resources).

To learn how to set up App Hub on your project, see [Set up App Hub](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  1. Delete the application's Service by running [`kubectl delete`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete):
         
         kubectl delete service hello-server
         

This command deletes the Compute Engine load balancer that you created when you exposed the Deployment.

  2. Delete your cluster by running [`gcloud container clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/delete):
         
         gcloud container clusters delete hello-cluster \
             --location us-central1
         




## Optional: `hello-app` code review

`hello-app` is a web server application that consists of two files: `main.go` and a `Dockerfile`.

`hello-app` is packaged as a [Docker](https://docker.com/) container image. Container images are stored in any Docker image registry, such as Artifact Registry. We host `hello-app` in a Artifact Registry repository at `us-docker.pkg.dev/google-samples/containers/gke/hello-app`.

### main.go

`main.go` is a web server implementation written in the [Go programming language](https://golang.org). The server responds to any HTTP request with a "Hello, world!" message.
    
    
    package main
    
    import (
    	"fmt"
    	"log"
    	"net/http"
    	"os"
    )
    
    func main() {
    	// register hello function to handle all requests
    	mux := http.NewServeMux()
    	mux.HandleFunc("/", hello)
    
    	// use PORT environment variable, or default to 8080
    	port := os.Getenv("PORT")
    	if port == "" {
    		port = "8080"
    	}
    
    	// start the web server on port and accept requests
    	log.Printf("Server listening on port %s", port)
    	log.Fatal(http.ListenAndServe(":"+port, mux))
    }
    
    // hello responds to the request with a plain-text "Hello, world" message.
    func hello(w http.ResponseWriter, r *http.Request) {
    	log.Printf("Serving request: %s", r.URL.Path)
    	host, _ := os.Hostname()
    	fmt.Fprintf(w, "Hello, world!\n")
    	fmt.Fprintf(w, "Version: 1.0.0\n")
    	fmt.Fprintf(w, "Hostname: %s\n", host)
    }
    

### Dockerfile

`Dockerfile` describes the image you want Docker to build, including all of its resources and dependencies, and specifies which network port the app should expose. For more information about how this file works, see [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) in the Docker documentation.
    
    
    FROM golang:1.26.2 AS builder
    WORKDIR /app
    RUN go mod init hello-app
    COPY *.go ./
    RUN CGO_ENABLED=0 GOOS=linux go build -o /hello-app
    
    FROM gcr.io/distroless/static-debian12
    WORKDIR /
    COPY --from=builder /hello-app /hello-app
    ENV PORT=8080
    USER nonroot:nonroot
    CMD ["/hello-app"]

## What's next

  * Learn more about [creating clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-container-cluster).
  * Learn more about [Kubernetes](http://kubernetes.io/).
  * Learn how to [package, host, and deploy a simple web server application](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/hello-app).
  * [Deploy a Kubernetes application with Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/quickstart-local-dev) or [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/deploy-kubernetes-app).
  * Learn how to [Replatform Linux applications to containers](https://docs.cloud.google.com/code/docs/vscode/replatform-apps-to-containers).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how GKE performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try GKE free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
