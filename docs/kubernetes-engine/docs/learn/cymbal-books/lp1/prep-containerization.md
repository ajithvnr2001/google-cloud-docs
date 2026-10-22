---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/prep-containerization/
title: Learning Path: Transform a monolith into a GKE app - Prepare the modular app for containerization \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:49.318985+00:00
---

# Learning Path: Transform a monolith into a GKE app - Prepare the modular app for containerization  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/prep-containerization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Learning Path: Transform a monolith into a GKE app - Prepare the modular app for containerization Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This is the third tutorial in a learning path that teaches you how to modularize and containerize a monolithic app.

The learning path consists of the following tutorials:

  1. [Overview](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/overview)
  2. [Understand the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/monolith)
  3. [Modularize the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/modular)
  4. Prepare the modular app for containerization (this tutorial)
  5. [Containerize the modular app](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/containerize)
  6. [Deploy the app to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/deploy)



In the previous tutorial, [Modularize the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/modular), you saw how to split up the Cymbal Books app into independent Flask modules. In this tutorial, you learn about a single change that needs to be made to the modular app to prepare it for containerization.

## Costs

You can complete this tutorial without incurring any charges. However, following the steps in the [final tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/deploy) of this series incurs charges on your Google Cloud account. Costs begin when you enable GKE and deploy the Cymbal Books app to a GKE cluster. These costs include per-cluster charges for GKE, as outlined on the [Pricing page](https://cloud.google.com/kubernetes-engine/pricing), and charges for running Compute Engine VMs.

To avoid unnecessary charges, ensure that you disable GKE or delete the project once you have completed this tutorial.

## Before you begin

Before you begin this tutorial, make sure that you've completed the earlier tutorials in the series. For an overview of the whole series, and links to particular tutorials, see [Learning Path: Transform a monolith into a GKE app - Overview](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/overview).

If you already completed the first tutorial, you cloned a GitHub repository. All three versions of the Cymbal Books app are located in that repository, inside the following folders:

  * `monolith/`
  * `modular/`
  * `containerized/`



Check that these folders are on your machine before you continue.

## Change the modular code

In the previous tutorial, you learned that the homepage module communicates with the other modules. It sends requests to the other modules' endpoints to retrieve book details, reviews, and images, and then presents this data in HTML pages.

In the `modular/` folder, the endpoints are hardcoded in `home.py`, using `localhost`, like this:
    
    
    BOOK_SERVICE_URL = "http://localhost:8081"     # Book details module listens on port 8081
    REVIEW_SERVICE_URL = "http://localhost:8082"   # Book reviews module listens on port 8082
    IMAGE_SERVICE_URL = "http://localhost:8083"    # Image module listens on port 8083
    

These URLs work when all the modules run on the same machine. But in a Kubernetes environment, modules can be moved to different machines to handle failures or to balance load, which means their IP addresses might change.

To make sure the homepage module can still reach the other modules, the URLs must use Kubernetes Service names instead of `localhost`. A Service name acts like an alias that Kubernetes uses to route requests to the correct module—no matter where it's running. For example, when the homepage module sends a request to `http://book-details-service/book/1`, Kubernetes helps ensure that the request reaches the book-details module.

You don't need to update these URLs yourself. The version of the app in the `containerized/` folder already includes this change: the hardcoded `localhost` URLs have been replaced with Kubernetes Service names. You can see the updated version in `containerized/home_app/home_app.py`:
    
    
    BOOK_SERVICE_URL = "http://book-details-service"
    REVIEW_SERVICE_URL = "http://book-reviews-service"
    IMAGE_SERVICE_URL = "http://images-service"
    

This update helps ensure the app will work correctly when it's running in a Kubernetes environment.

## The Kubernetes manifest

In the previous section, you saw how the modules' endpoints were updated to use Kubernetes Service names. You define the Service names in the _Kubernetes manifest_.

The Kubernetes manifest is a configuration file that defines what kind of Kubernetes cluster you want to create to host your modular app. The manifest is written in YAML or JSON. In it, you define things such as the Services (for routing between modules), the number of replicas (instances) of each module, and how much CPU and memory each module is allowed to use.

An entire tutorial series could be written about [Kubernetes manifests](https://kubernetes.io/docs/concepts/overview/working-with-objects/#describing-a-kubernetes-object). The manifest is complex because it defines everything about your Kubernetes cluster—its structure, behavior, and capabilities. In this tutorial, you look at only how the Service names in the manifest match the names that are used in the modules' endpoints. In a later tutorial, you run the `kubectl apply` command to create the GKE cluster according to the configuration that's defined in the manifest, but in this tutorial, you only review the manifest.

### View the manifest

In this section, you examine how Services are defined in a Kubernetes manifest that has been written for you. The manifest file, which is a YAML file, is in the `containerized/` folder of the GitHub repository you cloned in the first tutorial of this series. Follow these steps to view a Service definition:

  1. In your terminal, navigate to the containerized directory in the cloned repository:
         
         cd containerized
         

  2. In a text editor, open the Kubernetes manifest file:
         
         cat kubernetes_manifest.yaml
         

  3. Find the Service definition for the `book-details` module. It looks like the following example:
         
         apiVersion: v1
         kind: Service
         metadata:
         name: book-details-service
         spec:
         selector:
             app: book-details-app
         ports:
             - protocol: TCP
             port: 80  # External traffic on port 80
             targetPort: 8080  # Targeting container port 8080
         type: ClusterIP
         




The `book-details-service` Service name in the manifest matches the name that's used in the module's endpoint: `http://book-details-service`. When your app runs in Kubernetes, Kubernetes uses these Service names to route requests to the correct modules.

The Kubernetes manifest defines the features of your Kubernetes cluster, including Services that handle request routing. Each module in your app has a corresponding Service that's defined in the manifest. By updating the URLs in the modular code to match these Service names, you ensure that Kubernetes can route requests to the correct modules when the app runs in a cluster.

## Summary

In this tutorial, you saw how the URLs in the modular code were updated to use Kubernetes Service names, such as `http://book-details-service`. These Service names enable Kubernetes to route requests between modules even when their locations in the cluster change. You also examined the Kubernetes manifest and saw how the Service names in the modular code match the names defined in the manifest.

## What's next

In the next tutorial, [Containerize the modular app](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/containerize), you learn how to containerize a module by packaging it into something called a _container image_. You then see how to run a container image as a container, test its features, and push the container image to Google's Artifact Registry.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
