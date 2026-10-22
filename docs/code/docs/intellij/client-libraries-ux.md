---
url: https://docs.cloud.google.com/code/docs/intellij/client-libraries-ux/
title: Manage Cloud APIs and libraries in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:55.980144+00:00
---

# Manage Cloud APIs and libraries in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/client-libraries-ux/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)



Send feedback 

#  Manage Cloud APIs and libraries in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

You can access Google Cloud products and services from your code using [Cloud APIs](https://docs.cloud.google.com/apis/docs/overview). These Cloud APIs expose a simple JSON REST interface that you can call via client libraries.

This document describes how to browse available APIs, enable Cloud APIs and add Cloud Client Libraries to your project, and set up authentication depending on your development needs.

**Note:** For projects that don't use both Java and Maven, Cloud Code does not add the Cloud Client Libraries to your build automatically, but does support the other features described here and provides build snippets for your build system.

## Browsing Cloud APIs

To explore all available Google Cloud APIs in your IDE, follow these steps: 

  1. Select **Tools** > **Cloud Code** > **Add Cloud Libraries and Manage Cloud APIs**.
  2. Expand the Google Cloud APIs explorer tree to view all available APIs. The explorer groups Cloud APIs by category. You can also look for a specific API using the Search APIs search bar.
![Screenshot showing the list of Cloud APIs shown in the tree
            view explorer.](https://docs.cloud.google.com/static/code/docs/intellij/images/client-library-detail-enable.png)
  3. Click an API to view more details, such as its status, language-specific installation instructions for its corresponding client libraries, and relevant documentation.



## Enabling Cloud APIs

To quickly enable Cloud APIs for a project using the API details, follow these steps: 

  1. In the Cloud API details view, choose a Google Cloud project that you'd like to enable the Cloud API for.
  2. Click the **Enable API** button. 

Once the API has been enabled you'll see a message confirming this change. 




## Adding the Cloud Client Libraries

To add libraries to your project in IntelliJ, follow these steps:

### For Java Maven projects

  1. Select **Tools** > **Cloud Code** > **Cloud APIs**.

The **Manage Google Cloud APIs** dialog displays the supported libraries.

![Screenshot showing the Manage Cloud APIs dialog. This dialog
          provides a drop-down menu to select a module to add the libraries to,
          displays the list of APIs available to add, and provides a work area
          that displays information about the API.](https://docs.cloud.google.com/static/code/docs/intellij/images/add-maven-library.png)
  2. Select your preferred library type from the choice of Google Cloud Client Library (recommended) or Java Spring Google Cloud Library.
  3. In the **Module** drop-down menu, select the module that you want to add the library to.
**Note:** **Google Cloud Java** solves version conflicts between libraries by adding the [ Google Cloud Java Bill of Materials (BOM)](https://github.com/googleapis/google-cloud-java#version-management) to the `pom.xml` file of your projects.
  4. Click **Add Maven Dependency** to add BOM and client library to your project.



### For all other projects

  1. Select **Tools** > **Cloud Code** > **Add Cloud Libraries and Manage Cloud APIs**.

The **Add Google Cloud Libraries** dialog displays the supported libraries.

![Screenshot showing the Add Cloud Libraries dialog. This
                      dialog displays the list of APIs available to add and
                      provides a work area that displays information about the
                      API.](https://docs.cloud.google.com/static/code/docs/intellij/images/client-library-detail-enable.png)
  2. Install the API using the installation instructions listed on the API details page for your preferred language. If you're developing a Java application, you need to also specify your library preference, Google Cloud Client Library (recommended) or Java Spring Google Cloud Library. 



## Setting up authentication

After you've enabled the required APIs and added the necessary client libraries, you need to configure your application in order for it to be successfully authenticated. Your configuration depends on your type of development and the platform you're running on.

Once you complete the relevant authentication steps, your application can authenticate and is ready to be deployed.

### Local development

### minikube

  1. Ensure that you have Application Default Credentials (ADC) set by running `gcloud auth application-default login`. This lets minikube find your ADC to authenticate with.



### minikube

  1. Ensure that you have Application Default Credentials (ADC) set by running `gcloud auth application-default login`. This lets minikube find your ADC to authenticate with.
  2. Start minikube with `minikube start --addons gcp-auth`. This mounts your ADC in your pods. For a detailed minikube auth guide for Google Cloud, refer to the [minikube gcp-auth docs](https://minikube.sigs.k8s.io/docs/handbook/addons/gcp-auth/). 



### Local Kubernetes cluster

  1. Ensure that you have Application Default Credentials (ADC) set by running `gcloud auth application-default login`.
  2. Mount your local `gcloud` directory in your Kubernetes pods by editing the deployment manifests, so that the Google Cloud client libraries can find your credentials. Kubernetes pod configuration example: 
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: my-app
           labels:
             name: my-app
         spec:
           containers:
           - name: my-app
             image: gcr.io/google-containers/busybox
             ports:
               - containerPort: 8080
             **volumeMounts :
               - mountPath: /root/.config/gcloud
                 name: gcloud-volume
           volumes:
             - name: gcloud-volume
               hostPath:
                 path: /path/to/home/.config/gcloud**




### Cloud Run

  1. Ensure that you have Application Default Credentials (ADC) set by running `gcloud auth application-default login`. This lets the Cloud Run local simulated environment find your ADC to authenticate with. 



### Remote development

### Google Kubernetes Engine

  1. [Configure your GKE cluster and application with Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to authenticate Google Cloud services on GKE. This associates your Kubernetes service account with your Google service account. 
  2. If the Google Cloud service you're trying to access requires additional roles, grant them for the Google service account you're using to develop your app.  
For a list of IAM role types and predefined roles you can grant to identities, see the [Understanding roles guide](https://cloud.google.com/iam/docs/understanding-roles). For steps to grant the roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  3. Configure your Kubernetes Deployment to reference the Kubernetes service account by setting the `.spec.serviceAccountName` field in your Kubernetes Deployment YAML file.   
If you're working on an app created from a Cloud Code template, this file is located under the kubernetes-manifests folder. 



### Cloud Run

  1. To create a new unique service account for deploying your Cloud Run application, on the Service Accounts page, select the project that your secret is stored in. 

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **Create service account**. 
  3. In the **Create service account** dialog, enter a descriptive name for the service account. 
  4. Change the **Service account ID** to a unique, recognizable value and then click **Create**. 
  5. If the Google Cloud service you're trying to access requires additional roles, grant them, click **Continue** , and then click **Done**. 
  6. To add your service account to your deploy configuration, navigate to your **Cloud Run: Deploy** run configuration, expand the **Advanced revision settings** section, and then specify your service account in the **Service Account** field.   
![Advanced revision settings section expanded in Cloud Run: Deploy and Service Account field filled in with service account name of the format service-account-name@project-name.iam.gserviceaccount.com](https://docs.cloud.google.com/static/code/docs/intellij/images/cloud-run-service-account.png)



### Cloud Run

  1. [Configure your GKE cluster and application with Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to authenticate Google Cloud services on GKE. This associates your Kubernetes service account with your Google service account. 
  2. If the Google Cloud service you're trying to access requires additional roles, grant them for the Google service account you're using to develop your app.   
The [Understanding roles guide](https://cloud.google.com/iam/docs/understanding-roles) describes IAM role types and lists available predefined roles you can grant to identities. 
  3. To add your Kubernetes service account to your deploy configuration, navigate to your **Cloud Run: Deploy** run configuration, expand the **Advanced revision settings** section, and then specify your Kubernetes service account in the **Service Account** field.  
![Advanced revision settings section expanded in Cloud Run: Deploy and Service Account field filled in with Kubernetes service account name](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-service-account.png)



### Remote development with Secret Manager enabled

If you're developing remotely, using a service account for authentication, and your application uses [secrets](https://docs.cloud.google.com/code/docs/intellij/secret-manager-ux), you need to complete a few more steps to assign your Google service account the role required to access a particular Secret Manager secret:

  1. Open the Secret Manager panel and select the secret you want to access in your code.

![Secret Manager in Cloud Code highlighted in the right sidebar and Secret Manager panel open with three secrets listed and the version details of the secret 'test' listed in the bottom pane](https://docs.cloud.google.com/static/code/docs/intellij/images/secret-ui.png)

  2. Switch to the Permissions tab and then configure your secret's permissions by clicking edit **Edit Permission**. The Secret Manager configuration page for the secret opens in your web browser.

![Permissions tab selected within the Secret Manager and Edit Permissions icon highlighted](https://docs.cloud.google.com/static/code/docs/intellij/images/configure-secret.png)

  3. In Google Cloud console, click **Show Info Panel** and then click **Add principal**.

  4. Assign your service account the **Secret Manager Secret Accessor** role.

Your service account has permission to access this secret.




## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
