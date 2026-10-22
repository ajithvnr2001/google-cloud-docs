---
url: https://docs.cloud.google.com/code/docs/intellij/client-libraries/
title: Manage Cloud APIs and Cloud Client Libraries in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:57.571309+00:00
---

# Manage Cloud APIs and Cloud Client Libraries in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/client-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Manage Cloud APIs and Cloud Client Libraries in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

You can access Google Cloud products and services from your code using [Cloud APIs](https://docs.cloud.google.com/apis/docs/overview). These Cloud APIs expose a simple JSON REST interface that you can call via client libraries.

This document describes how to enable Cloud APIs and add Cloud Client Libraries to your project.

**Note:** For projects that don't use both Java and Maven, Cloud Code doesn't add the Cloud Client Libraries to your build automatically, but does support the other features described here and provides build snippets for your build system.

## Browse Cloud APIs

**Note:** Cloud Code's list of APIs and libraries covers the majority, but not all, APIs.

To explore all available Google Cloud APIs in your IDE, follow these steps:

  1. Navigate to **Tools** > **Google Cloud Code** > **Cloud APIs**.

  2. The **Manage Google Cloud APIs** window groups Cloud APIs by category. You can also use the **Search APIs** search bar to find specific APIs.

![Cloud APIs explorer showing the list of Cloud APIs.](https://docs.cloud.google.com/static/code/docs/intellij/images/client-library-detail-enable.png)

  3. Click an API to view more details, such as its status, language-specific installation instructions for its corresponding client libraries, and relevant documentation.




## Enable Cloud APIs

To enable Cloud APIs for a project using the API details, follow these steps:

  1. In the **Cloud API** details view, select a Google Cloud project that you want to enable the Cloud API for.

  2. Click **Enable API**.

When the API is enabled, a message appears to confirm the change.




## Add the Cloud Client Libraries

To add libraries to your project in IntelliJ, follow these steps:

### For Java Maven projects

  1. Navigate to **Tools** > **Google Cloud Code** > **Cloud APIs**.

The **Install Client Library** section in the **Manage Google Cloud APIs** dialog displays the supported libraries.

  2. Select your preferred library type as **Google Cloud Client Library** (recommended for most projects) or **Java Spring Google Cloud** (recommended if your project uses Java Spring).
  3. Follow the rest of the instructions in the **Install Client Library** in your IDE, if applicable.
**Note:** **Google Cloud Java** solves version conflicts between libraries by adding the [ Google Cloud Java Bill of Materials (BOM)](https://github.com/googleapis/google-cloud-java#version-management) to the `pom.xml` file of your projects.
  4. When you're finished, click **Close**.



### For all other projects

  1. Navigate to **Tools** > **Google Cloud Code** > **Cloud APIs**.

The **Install Client Library** section in the **Manage Google Cloud APIs** dialog displays the supported libraries.

  2. To install the API, follow the installation instructions listed on the API details page for your preferred language. 

If you're developing a Java application, you need to also specify your library preference as **Google Cloud Client Library** (recommended) or **Java Spring Google Cloud**. 

  3. When you're finished, click **Close**.



## Use API code samples

To search for and use code samples for each API in the API explorer, follow these steps:

  1. Navigate to **Tools** > **Google Cloud Code** > **Cloud APIs**.

  2. To open the detail view, click the name of an API.

  3. To view code samples for the API, click the **Code Samples** tab.

  4. To filter the list of samples, type text to search for or select a programming language from the **Language** drop-down menu.




## Set up authentication

After you've enabled the required APIs and added the necessary client libraries, you need to configure your application in order for it to be successfully authenticated. Your configuration depends on your type of development and the platform you're running on.

Once you complete the relevant authentication steps, your application can authenticate and is ready to be deployed.

### Local development

### Local machine

Cloud Code ensures you have your Application Default Credentials (ADC) set if you logged into Google Cloud via your IDE. If you're not signing in with Cloud Code, run `gcloud auth application-default login` manually.

### minikube

  1. Cloud Code ensures you have your Application Default Credentials (ADC) set if you logged into Google Cloud via your IDE. If you're not signing in with Cloud Code, run `gcloud auth application-default login` manually.
  2. Start minikube with `minikube start --addons gcp-auth`. This mounts your ADC in your pods. For a detailed minikube auth guide for Google Cloud, refer to the [minikube gcp-auth docs](https://minikube.sigs.k8s.io/docs/handbook/addons/gcp-auth/). 



### Other local K8s clusters

  1. Cloud Code ensures you have your Application Default Credentials (ADC) set if you logged into Google Cloud via your IDE. If you're not signing in with Cloud Code, run `gcloud auth application-default login` manually.
  2. Mount your local `gcloud` directory in your Kubernetes pods by editing the Pod specification in the Pod or Deployment manifests, so that the Google Cloud Client Libraries can find your credentials. Kubernetes pod configuration example: 
         
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

Cloud Code ensures you have your Application Default Credentials (ADC) set if you logged into Google Cloud via your IDE. If you're not signing in with Cloud Code, run `gcloud auth application-default login` manually.

### Remote development

### Google Kubernetes Engine

  
Depending on the scope of your project, you can choose how you authenticate Google Cloud services on GKE: 

  * **(Development only)** **Note:** GKE cluster service account and access scope settings are permanent; once your cluster is created, these settings cannot be changed. Specify the settings as recommended below. 
    1. [Create a GKE cluster](https://console.cloud.google.com/kubernetes/add) with the following settings: 
       * Ensure you're using the service account GKE uses by default, the Compute Engine default service account, and that **Access scopes** is set at **Allow full access to all Cloud APIs** (both settings accessible in the **Node Pools** > **Security** section).  
Since the Compute Engine service account is shared by all workloads deployed on your node, this method overprovisions permissions and should only be used for development.
       * Ensure Workload Identity is not enabled on your cluster (in the **Cluster** > **Security** section).
    2. Assign the necessary roles to the Compute Engine default service account: 
       * If you're trying to access a secret, follow these Secret Manager-specific steps to set up the required roles on your service account.
       * If the Compute Engine default service account is being used, the correct IAM roles may already be applied.
       * For a list of IAM role types and predefined roles you can grant to identities, see the [Understanding roles guide](https://cloud.google.com/iam/docs/understanding-roles).

For steps to grant the roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * **(Recommended for production)**
    1. [Configure your GKE cluster and application with Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to authenticate Google Cloud services on GKE. This associates your Kubernetes service account with your Google service account.
    2. Configure your Kubernetes Deployment to reference the Kubernetes service account by setting the `.spec.serviceAccountName` field in your Kubernetes Deployment YAML file.   
If you're working on an app created from a Cloud Code template, this file is located under the kubernetes-manifests folder. 
    3. If the Google Cloud service you're trying to access requires additional roles, grant them for the Google service account you're using to develop your app: 
       * If you're trying to access a secret, follow these Secret Manager-specific steps to set up the required roles on your service account.
       * For a list of IAM role types and predefined roles you can grant to identities, see the [Understanding roles guide](https://cloud.google.com/iam/docs/understanding-roles).

For steps to grant the roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




### Cloud Run

  


  1. To create a new unique service account for deploying your Cloud Run application, on the Service Accounts page, select the project that your secret is stored in.   


[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **Create service account**. 
  3. In the **Create service account** dialog, enter a descriptive name for the service account. 
  4. Change the **Service account ID** to a unique, recognizable value and then click **Create**. 
  5. If the Google Cloud service you're trying to access requires additional roles, grant them, click **Continue** , and then click **Done**. 
  6. To add your Kubernetes service account to your deploy configuration, navigate to **Run** > **Edit Configurations** , and then specify your service account in the **Service Name** field. 



### Cloud Run

  
Depending on the scope of your project, you can choose how you authenticate Google Cloud services on GKE: 

  * **(Development only)** **Note:** GKE cluster service account and access scope settings are permanent; once your cluster is created, these settings cannot be changed. Specify the settings as recommended below. 
    1. [Create a GKE cluster](https://console.cloud.google.com/kubernetes/add) with the following settings: 
       * Ensure you're using the service account GKE uses by default, the Compute Engine default service account, and that **Access scopes** is set at **Allow full access to all Cloud APIs** (both settings accessible in the **Node Pools** > **Security** section).  
Since the Compute Engine service account is shared by all workloads deployed on your node, this method overprovisions permissions and should only be used for development.  

       * Ensure Workload Identity is not enabled on your cluster (in the **Cluster** > **Security** section).
    2. Assign the necessary roles to the Compute Engine default service account: 
       * If you're trying to access a secret, follow these Secret Manager-specific steps to set up the required roles on your service account.
       * If the Compute Engine default service account is being used, the correct IAM roles may already be applied.
       * For a list of IAM role types and predefined roles you can grant to identities, see the [Understanding roles guide](https://cloud.google.com/iam/docs/understanding-roles).

For steps to grant the roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * **(Recommended for production)**
    1. [Configure your GKE cluster and application with Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to authenticate Google Cloud services on GKE. This associates your Kubernetes service account with your Google service account.
    2. To add your Kubernetes service account to your deploy configuration, navigate to **Run** > **Edit Configurations** , and then specify your Kubernetes service account in the **Service Name** field.   

    3. If the Google Cloud service you're trying to access requires additional roles, grant them for the Google service account you're using to develop your app: 
       * If you're trying to access a secret, follow these Secret Manager-specific steps to set up the required roles on your service account.
       * For a list of IAM role types and predefined roles you can grant to identities, see the [Understanding roles guide](https://cloud.google.com/iam/docs/understanding-roles).

For steps to grant the roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




### Remote development with Secret Manager permissions enabled

If you're developing remotely, using a service account for authentication, and your application uses [secrets](https://docs.cloud.google.com/code/docs/intellij/secret-manager), you need to complete a few more steps in addition to the remote development instructions. These steps assign your Google service account the [role required](https://docs.cloud.google.com/secret-manager/docs/access-control) to access a particular Secret Manager secret:

  1. To open the Secret Manager tool window, navigate to **Tools** > **Google Cloud Code** > **Secret Manager**.

  2. Select the secret that you want to access in your code.

  3. Click the **Permissions** tab and then configure your secret's permissions by clicking edit **Edit Permission**.

![Permissions tab selected within the Secret Manager and Edit Permissions icon highlighted](https://docs.cloud.google.com/static/code/docs/intellij/images/configure-secret.png)

The Google Cloud console opens in a new window of your web browser, displaying the Secret Manager configuration page of your secret.

  4. In the Google Cloud console, click the **Permissions** tab and then click **Grant Access**.

  5. In the **New principals** field, enter your service account.

  6. In the **Select a role** dropdown field, select the **Secret Manager Secret Accessor** role.

  7. When you're finished, click **Save**.

Your service account has permission to access this secret.




## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
