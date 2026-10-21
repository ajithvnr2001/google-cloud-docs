---
url: https://docs.cloud.google.com/solutions/using-gke-applications-page-cloud-console/
title: Using the GKE Applications page in the Google Cloud console \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:55:29.252012+00:00
---

# Using the GKE Applications page in the Google Cloud console  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/using-gke-applications-page-cloud-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Using the GKE Applications page in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to use the [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine) [**Applications** page](https://console.cloud.google.com/kubernetes/application) in the Google Cloud console.

When you adopt [Kubernetes](https://kubernetes.io/) for many applications and resources, it can be challenging to identify and track the various components related to one application. When you deploy multiple applications in each namespace, it can be difficult to know what resources are related to which application. Furthermore, you must often search in multiple locations for documentation and metadata that describe what the applications are, who the owners are, and how to interact with the services.

GKE helps solve these challenges with the **Applications** page:

![A partial view of the Applications page that shows a list of applications
along with various properties.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-applications-page.png)

The **Applications** page is an independent resource within your architecture that describes metadata about your system. You can use this page to visually organize your resources without changing the architecture. By defining values in a YAML file, you can group all your application resources and include vital metadata for your operations team. Creating, modifying, and deleting the YAML file doesn't affect existing resources, so you can immediately work with resources without risk to your system.

To demonstrate this page, this tutorial shows how to implement the [Kubernetes Application resource](https://github.com/kubernetes-sigs/application) against an application and add user-defined metadata in order to organize and simplify management of the application in GKE.

This tutorial is intended for developers who create applications to run in GKE. It assumes that you're familiar with basic Kubernetes concepts and have some experience writing Kubernetes resource YAML files.

## Objectives

  * Introduce the Kubernetes Application resource.
  * Add the Kubernetes Application resource to an existing architecture.
  * Create and view custom information about an application through the Google Cloud console.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Compute Engine and Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,container.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

You run the commands for this tutorial in Cloud Shell or the [Cloud Shell Editor](https://docs.cloud.google.com/shell/docs/viewing-and-editing-files).




## Preparing your environment

  1. In Cloud Shell, set the environment variables for your project:
         
         export PROJECT_ID=PROJECT_ID
         gcloud config set core/project $PROJECT_ID
         gcloud config set compute/zone us-central1-c

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Create a GKE cluster:
         
         gcloud container clusters create sample-cluster
         

For this tutorial, you run applications in a default GKE cluster.




## Installing the sample applications

In this tutorial, you simulate multiple applications running in the same namespace by using a basic Nginx sample application and the Bank of Anthos sample application.

  1. In Cloud Shell, install the Nginx sample application:
         
         kubectl apply -f https://raw.githubusercontent.com/kubernetes/website/master/content/en/examples/application/web/web.yaml
         

This command creates a StatefulSet resource called `web` and a service called `nginx`. In the Google Cloud console, you can view these resources on the GKE [**Workloads**](https://console.cloud.google.com/kubernetes/workload) and [**Services & Ingress**](https://console.cloud.google.com/kubernetes/discovery) pages.

  2. Clone the GitHub repository that contains the Bank of Anthos sample application:
         
         git clone https://github.com/GoogleCloudPlatform/bank-of-anthos.git
         cd bank-of-anthos
         

  3. Generate an SSH key and store it as a Kubernetes Secret:
         
         openssl genrsa -out jwtRS256.key 4096
         openssl rsa -in jwtRS256.key -outform PEM -pubout -out jwtRS256.key.pub
         kubectl create secret generic jwt-key --from-file=./jwtRS256.key --from-file=./jwtRS256.key.pub
         

The Bank of Anthos sample application requires an SSH key to run.

  4. Deploy the sample application to your cluster:
         
         kubectl apply -f kubernetes-manifests
         

After a few moments, you can view the application resources on the following pages in the Google Cloud console:

     * The [**Workloads** page](https://console.cloud.google.com/kubernetes/workload)
     * The [**Services & Ingress** page](https://console.cloud.google.com/kubernetes/discovery)

Note the following:

     * The resources for the Nginx and Bank of Anthos sample applications are intermingled.
     * No resources are displayed yet on the [**Applications** page](https://console.cloud.google.com/kubernetes/application). You populate the **Applications** page in later steps.



## Preparing GKE

The resources that the **Applications** page displays are specified with the Kubernetes Application resource type, a custom resource definition (CRD) provided by the open source Kubernetes project. By default, the Application CRD isn't enabled in Kubernetes. Some services in GKE, such as Marketplace and Application Deployment, install the Application CRD, but if you're not using any of those services, the Application CRD isn't available by default.

To install the Application CRD, do the following:

  1. In Cloud Shell, apply the Application CRD once on each cluster:
         
         kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/application/master/deploy/kube-app-manager-aio.yaml
         

  2. (Optional) After the command completes, view the Application CRD on the cluster:
         
         kubectl get crd
         

The following output is a list of installed CRDs, including `applications.app.k8s.io`:
         
         NAME                                    CREATED AT
         applications.app.k8s.io                 2020-07-24T19:32:20Z
         backendconfigs.cloud.google.com         2020-07-24T19:28:40Z
         managedcertificates.networking.gke.io   2020-07-24T19:28:57Z
         scalingpolicies.scalingpolicy.kope.io   2020-07-24T19:28:57Z
         updateinfos.nodemanagement.gke.io       2020-07-24T19:28:57Z
         




## Including application resources

Now that the Application CRD is available in the cluster, the next step is to create and deploy an instance of the Application resource.

Because the Application resource is a Kubernetes resource, it has a similar structure to other Kubernetes resources, including fields and options for `apiVersion`, `kind`, `metadata`, and `spec`:
    
    
    apiVersion: app.k8s.io/v1beta1
    kind: Application
    metadata:
      name: ...
    spec:
       ...
    

In the following sections, you work with various fields and options that are available in the Application resource.

### Create the base Application resource

You can add the Application resource to any existing set of resources. In this tutorial, you begin with an empty resource and fill in each section.

  1. In Cloud Shell, create and edit an `application.yaml` file in the `kubernetes-manifests` directory:
         
         touch kubernetes-manifests/application.yaml
         edit kubernetes-manifests/application.yaml
         

The Cloud Shell Editor opens and displays a blank file.

  2. Paste the following lines to define your first application:
         
         apiVersion: app.k8s.io/v1beta1
         kind: Application
         metadata:
           name: "bank-of-anthos"
         

  3. On the Cloud Shell menu bar, click **Open Terminal**.

  4. In Cloud Shell, apply the resource:
         
         kubectl apply -f kubernetes-manifests/application.yaml
         

  5. In the Google Cloud console, go to the **Applications** page.

[Go to Applications](https://console.cloud.google.com/kubernetes/application)

The **Applications** page displays the resources that you added:

![The Bank of Anthos application is included in the list of applications.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-app-name.png)




### Include resources by component

The **Applications** page shows the Bank of Anthos application. When you [click **bank-of-anthos** in the **Name** field](https://console.cloud.google.com/kubernetes/application/us-central1-c/sample-cluster/default/bank-of-anthos/details), you see basic information about the application:

![Application details include cluster, namespace, and creation
date.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-app-details.png)

You can add various types of components to display in the Google Cloud console. For example, to show Services, Deployments, and StatefulSets, you edit the `componentKinds` section of the `application.yaml` definition—for example, as follows:
    
    
    spec:
      componentKinds:
        - group: v1
          kind: Service
        - group: apps
          kind: Deployment
        - group: v1
          kind: StatefulSet
    

In the following steps, you add these components to the Bank of Anthos resource definition:

  1. On the Cloud Shell menu bar, click **Open Editor**.

  2. In the Cloud Shell Editor, overwrite the contents of the `kubernetes-manifests/application.yaml` file by pasting the following:
         
         apiVersion: app.k8s.io/v1beta1
         kind: Application
         metadata:
           name: "bank-of-anthos"
         spec:
           componentKinds:
             - group: v1
               kind: Service
             - group: apps
               kind: Deployment
             - group: v1
               kind: StatefulSet
         

The addition of the `spec` section adds `Service`, `Deployment`, and `StatefulSet` to your application definition.

  3. In Cloud Shell, apply the resource:
         
         kubectl apply -f kubernetes-manifests/application.yaml
         

  4. In the Google Cloud console, go to the details page for the Bank of Anthos application.

[Go to Bank of Anthos details](https://console.cloud.google.com/kubernetes/application/us-central1-c/sample-cluster/default/bank-of-anthos/details)

The components of a given type are displayed:

![The list of details includes component types such as
Service and Deployment.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-components.png)




### Filter resources with selectors

At this point in the tutorial, the list of components includes all the resources for both sample applications for the defined set of components from the entire namespace. For example, the following diagram shows the `nginx` Service from the Nginx sample application and the `transactionhistory` Deployment from the Bank of Anthos sample application:

![The list of components is generated from all applications in the
namespace.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-selectors.png)

To ensure that only the resources for one application are displayed—for instance, for the Bank of Anthos application—you can use selectors to identify specific resources. To see how selectors work, you add a label to your resource in the following steps:

  1. In Cloud Shell, open the `frontend.yaml` file:
         
         edit kubernetes-manifests/frontend.yaml
         

  2. In the Cloud Shell Editor, paste the following `label` entry after line 18:
         
         labels:
             app.kubernetes.io/name: "bank-of-anthos"
         

The `metadata` section looks like following:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: frontend
           labels:
             app.kubernetes.io/name: "bank-of-anthos"
         spec:
         

The completed `application.yaml` file looks like the following:
         
         apiVersion: app.k8s.io/v1beta1
         kind: Application
         metadata:
           name: "bank-of-anthos"
           labels:
             app.kubernetes.io/name: "bank-of-anthos"
         spec:
           selector:
             matchLabels:
              app.kubernetes.io/name: "bank-of-anthos"
           componentKinds:
             - group: v1
               kind: Service
             - group: apps
               kind: Deployment
             - group: v1
               kind: StatefulSet
         

  3. In Cloud Shell, apply the resources:
         
         kubectl apply -f kubernetes-manifests/
         

  4. In the Google Cloud console, go to the details page for the Bank of Anthos application.

[Go to Bank of Anthos details](https://console.cloud.google.com/kubernetes/application/us-central1-c/sample-cluster/default/bank-of-anthos/details)

The only resource that matches a specific label is displayed:

![The components list shows the Deployment resource.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-labels.png)




### Apply labels to all resources with `kustomize`

Manually applying labels to every resource in an application can be tedious. The following steps show how to use [`kustomize`](https://kustomize.io/) to efficiently add labels to all resources:

  1. In Cloud Shell, download `kustomize`:
         
         curl -s "https://raw.githubusercontent.com/\
         kubernetes-sigs/kustomize/master/hack/install_kustomize.sh" | bash
         

  2. Create and edit a `kustomization.yaml` file:
         
         touch kubernetes-manifests/kustomization.yaml
         edit kubernetes-manifests/kustomization.yaml
         

  3. In the Cloud Shell Editor, add the following lines to `kustomization.yaml`:
         
         apiVersion: kustomize.config.k8s.io/v1beta1
         kind: Kustomization
         
         resources:
         - accounts-db.yaml
         - application.yaml
         - balance-reader.yaml
         - config.yaml
         - contacts.yaml
         - frontend.yaml
         - ledger-db.yaml
         - ledger-writer.yaml
         - loadgenerator.yaml
         - transaction-history.yaml
         - userservice.yaml
         
         commonLabels:
             app.kubernetes.io/name: "bank-of-anthos"
         

In this `kustomization.yaml` definition, you specify which resources to apply the modifications to and what modifications to make. In this case, you specify that all resources should have a common label of `app.kubernetes.io/name: "bank-of-anthos"`.

  4. In Cloud Shell, delete the old resources:
         
         kubectl delete -f kubernetes-manifests/
         

It is necessary to delete the old resources before you apply the new resources that are specified in `kustomization.yaml`.

  5. Apply the resources using the `kustomize` flag instead of the `file` flag:
         
         ./kustomize build kubernetes-manifests/ | kubectl apply -f -
         

  6. In the Google Cloud console, go to the details page for the Bank of Anthos application.

[Go to Bank of Anthos details](https://console.cloud.google.com/kubernetes/application/us-central1-c/sample-cluster/default/bank-of-anthos/details)

The details page displays the resources for the Bank of Anthos sample application and no resources from the Nginx sample application:

![Only Bank of Anthos components, such as StatefulSet, are
displayed.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-filtered-components.png)




## Adding useful metadata in the display

You can display custom metadata for an application in the Google Cloud console. You might include what the application does, who owns it, where to find more information about it, and how to log in to it. This type of information is valuable for various use cases—for instance, if you operate multiple applications within your organization.

The following sections describe some of the metadata that you can add.

### Add a description and documentation

You can add a description and links that appear in the **Application info** panel. To access this panel from the **Details** page, click **Show Info Panel**.

To display information in this panel, you define elements such as `description` and `links` in the `descriptor` section of your `application.yaml` file.
    
    
    descriptor:
        description:
        links:
        - description:
          url:
    

To update the `descriptor` section, do the following:

  1. In Cloud Shell Editor, overwrite the contents of the `application.yaml` file by pasting the following:
         
         apiVersion: app.k8s.io/v1beta1
         kind: Application
         metadata:
           name: "bank-of-anthos"
           labels:
             app.kubernetes.io/name: "bank-of-anthos"
         spec:
           selector:
             matchLabels:
              app.kubernetes.io/name: "bank-of-anthos"
         
           componentKinds:
             - group: v1
               kind: Service
             - group: apps
               kind: Deployment
             - group: v1
               kind: StatefulSet
         
           descriptor:
             description: |-
                 This application simulates a bank's payment processing network using
                 [Anthos](/anthos/).
                 Bank of Anthos allows users to create artificial accounts and
                 simulate transactions between accounts. Bank of Anthos was developed
                 to create an end-to-end sample demonstrating Anthos best practices.
         
             links:
             - description: 'About Anthos on GCP'
               url: /anthos/
             - description: 'Bank of Anthos GitHub Repository'
               url: https://github.com/GoogleCloudPlatform/bank-of-anthos
         

  2. In Cloud Shell, deploy the Application resource:
         
         kubectl apply -f kubernetes-manifests/application.yaml
         

  3. In the Google Cloud console, go to the details page for the Bank of Anthos application.

[Go to Bank of Anthos details](https://console.cloud.google.com/kubernetes/application/us-central1-c/sample-cluster/default/bank-of-anthos/details)

  4. To review the updates, click **Show Info Panel**.

The **Application info** panel shows a description and a list of documents:

![The documents in the list are formatted as hyperlinks.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-app-info.png)




### Include the software type

The **Applications** page includes a field (**Software**) for software type in the applications list. You can customize this field to help organize and categorize your applications according to your needs. For example, you might indicate that the software is internal or external. Or, if you have multiple apps built from a shared base type, you might indicate what base type an application implements.

To add a custom description to the software type, you use the `type` field in the `descriptor` section of the `application.yaml` file:
    
    
     descriptor:
        type: External App
    

You can display the value for `type` as a hyperlink in the Google Cloud console. You specify the URL for the hyperlink by using the first entry from the `links` section. In the following steps, you update the `links` section as follows:
    
    
        links:
        - description: 'Bank of Anthos GitHub Repository'
          url: https://github.com/GoogleCloudPlatform/bank-of-anthos
    

  1. In the Cloud Shell Editor, overwrite the contents of `application.yaml` by pasting the following:
         
         apiVersion: app.k8s.io/v1beta1
         kind: Application
         metadata:
           name: "bank-of-anthos"
           labels:
             app.kubernetes.io/name: "bank-of-anthos"
         spec:
           selector:
             matchLabels:
              app.kubernetes.io/name: "bank-of-anthos"
         
           componentKinds:
             - group: v1
               kind: Service
             - group: apps
               kind: Deployment
             - group: v1
               kind: StatefulSet
         
           descriptor:
             type: External App
         
             description: |-
                 This application simulates a bank's payment processing network using [Anthos](/anthos/).
                 Bank of Anthos allows users to create artificial accounts and simulate transactions between accounts. Bank of Anthos was developed to create an end-to-end sample demonstrating Anthos best practices.
         
             links:
             - description: 'About Anthos on GCP'
               url: /anthos/
             - description: 'Bank of Anthos GitHub Repository'
               url: https://github.com/GoogleCloudPlatform/bank-of-anthos
         

  2. In Cloud Shell, deploy the Application resource:
         
         kubectl apply -f kubernetes-manifests/application.yaml
         

  3. In the Google Cloud console, go to the **Applications** page.

[Go to Applications](https://console.cloud.google.com/kubernetes/application)

**External App** is displayed in the **Software** field:

![The software type External App is formatted as a hyperlink.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-software-type.png)




### Include an application version

The main **Applications** page includes a field for version. In practice, the value for this field is updated programmatically to reference the actual version deployed.

To populate the version field, you include the `version` field under `descriptor` as in the following example:
    
    
      descriptor:
        type: External App
        version: "2.3.2"
    

In the following steps, you add a field for the application version.

  1. In the Cloud Shell Editor, overwrite the contents of the `application.yaml` file by pasting the following:
         
         apiVersion: app.k8s.io/v1beta1
         kind: Application
         metadata:
           name: "bank-of-anthos"
           labels:
             app.kubernetes.io/name: "bank-of-anthos"
         spec:
           selector:
             matchLabels:
              app.kubernetes.io/name: "bank-of-anthos"
         
           componentKinds:
             - group: v1
               kind: Service
             - group: apps
               kind: Deployment
             - group: v1
               kind: StatefulSet
         
           descriptor:
             type: External App
         
             version: "2.3.2"
         
             description: |-
                 This application simulates a bank's payment processing network using [Anthos](/anthos/).
                 Bank of Anthos allows users to create artificial accounts and simulate transactions between accounts. Bank of Anthos was developed to create an end-to-end sample demonstrating Anthos best practices.
         
             links:
             - description: 'About Anthos on GCP'
               url: /anthos/
             - description: 'Bank of Anthos GitHub Repository'
               url: https://github.com/GoogleCloudPlatform/bank-of-anthos
         

  2. In Cloud Shell, deploy the Application resource:
         
         kubectl apply -f kubernetes-manifests/application.yaml
         

  3. In the Google Cloud console, go to the **Applications** page.

[Go to Applications](https://console.cloud.google.com/kubernetes/application)

The **Version** field for the Bank of Anthos application is shown as **2.3.2** :

![Details for the application include the software type and version fields.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-version.png)




### Add maintainer details

In this step, you add custom static text to the main section of the **Applications** page. You specify these details in the `info` section of the `application.yaml` file as follows:
    
    
      info:
      - name: LABEL
        value: STRING

To include static values, you provide details for `LABEL` and `STRING` in the `info` section. For example, you might enter `Owner` for `name` and `John Smith` for `value`.

  1. In the Cloud Shell Editor, overwrite the contents of `application.yaml` by pasting the following:
         
         apiVersion: app.k8s.io/v1beta1
         kind: Application
         metadata:
           name: "bank-of-anthos"
           labels:
             app.kubernetes.io/name: "bank-of-anthos"
         spec:
           selector:
             matchLabels:
              app.kubernetes.io/name: "bank-of-anthos"
         
           componentKinds:
             - group: v1
               kind: Service
             - group: apps
               kind: Deployment
             - group: v1
               kind: StatefulSet
         
           descriptor:
             type: External App
         
             version: "2.3.2"
         
             description: |-
                 This application simulates a bank's payment processing network using [Anthos](/anthos/).
                 Bank of Anthos allows users to create artificial accounts and simulate transactions between accounts. Bank of Anthos was developed to create an end-to-end sample demonstrating Anthos best practices.
         
             links:
             - description: 'About Anthos on GCP'
               url: /anthos/
             - description: 'Bank of Anthos GitHub Repository'
               url: https://github.com/GoogleCloudPlatform/bank-of-anthos
         
           info:
           - name: Owner
             value: John Smith
         

  2. In Cloud Shell, deploy the Application resource:
         
         kubectl apply -f kubernetes-manifests/application.yaml
         

  3. In the Google Cloud console, go to the details page for the Bank of Anthos application.

[Go to Bank of Anthos details](https://console.cloud.google.com/kubernetes/application/us-central1-c/sample-cluster/default/bank-of-anthos/details)

The details page includes an owner for the Bank of Anthos application:

![John Smith is listed as the owner.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-app-details-2.png)




### Expose an application endpoint

In addition to static values, you can expose dynamic values from the Deployment itself. In the following steps, you surface the load balancer IP address so that anyone who views the application details page can access the application directly.

To surface this value, you use the [`serviceRef`](https://github.com/kubernetes-sigs/application/blob/master/config/crd/bases/app.k8s.io_applications.yaml#L345) specification. Other valid specifications include [`configMapKeyRef`](https://github.com/kubernetes-sigs/application/blob/master/config/crd/bases/app.k8s.io_applications.yaml#L219), [`ingressRef`](https://github.com/kubernetes-sigs/application/blob/master/config/crd/bases/app.k8s.io_applications.yaml#L259), and [`secretKeyRef`](https://github.com/kubernetes-sigs/application/blob/master/config/crd/bases/app.k8s.io_applications.yaml#L305).

In the `serviceRef` specification, you include these dynamic values by using the `Reference` type. For this tutorial, the specification for `serviceRef` is the following:
    
    
     info:
      - name: LABEL
        type: Reference
        valueFrom:
          serviceRef:
            name: SERVICE_NAME
            fieldPath: DATA_LOCATION

You can replace the following values:

  * `LABEL`: a label that describes a specific Reference instance—for example, `App Frontend URL`
  * `SERVICE_NAME`: the name that identifies the Service$mdash;for example, `frontend`
  * `DATA_LOCATION`: the location of the data in the Service—for example, `status.loadBalancer.ingress[0].ip`



The `serviceRef` and `ingressRef` specifications also support the `path` element. If your URL requires path-related details, you include those details in the `path` field:
    
    
     info:
      - name: LABEL
        type: Reference
        valueFrom:
          serviceRef:
            name: SERVICE_NAME
            fieldPath: DATA_LOCATION
            path: /wp-admin

The endpoint IP address and path are concatenated—for example, `35.202.90.0/wp-admin`.

You can also force the use of HTTP or HTTPS by using the `protocol` field as follows:
    
    
     info:
      - name: LABEL
        type: Reference
        valueFrom:
          serviceRef:
            name: SERVICE_NAME
            fieldPath: DATA_LOCATION
            path: /wp-admin
            protocol: HTTPS

These details produce the following URL:
    
    
    https://35.202.90.0/wp-admin
    

In the following steps, you use `serviceRef` to expose the Service load balancer IP address for the Bank of Anthos application:

  1. In the Cloud Shell Editor, overwrite the contents of the `application.yaml` file with the following:
         
         apiVersion: app.k8s.io/v1beta1
         kind: Application
         metadata:
           name: "bank-of-anthos"
           labels:
             app.kubernetes.io/name: "bank-of-anthos"
         spec:
           selector:
             matchLabels:
              app.kubernetes.io/name: "bank-of-anthos"
         
           componentKinds:
             - group: v1
               kind: Service
             - group: apps
               kind: Deployment
             - group: v1
               kind: StatefulSet
         
           descriptor:
             type: External App
         
             version: "2.3.2"
         
             description: |-
                 This application simulates a bank's payment processing network using [Anthos](/anthos/).
                 Bank of Anthos allows users to create artificial accounts and simulate transactions between accounts. Bank of Anthos was developed to create an end-to-end sample demonstrating Anthos best practices.
         
             links:
             - description: 'About Anthos on GCP'
               url: /anthos/
             - description: 'Bank of Anthos GitHub Repository'
               url: https://github.com/GoogleCloudPlatform/bank-of-anthos
         
           info:
           - name: Owner
             value: John Smith
           - name: App Frontend URL
             type: Reference
             valueFrom:
               serviceRef:
                 name: frontend
                 fieldPath: status.loadBalancer.ingress[0].ip
                 protocol: HTTPS
         

  2. In Cloud Shell, deploy the Application resource:
         
         kubectl apply -f kubernetes-manifests/application.yaml
         

  3. In the Google Cloud console, go to the details page for the Bank of Anthos application.

[Go to Bank of Anthos details](https://console.cloud.google.com/kubernetes/application/us-central1-c/sample-cluster/default/bank-of-anthos/details)

The details page includes an endpoint IP address for the Bank of Anthos application:

![The IP address is labeled App Frontend URL.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-app-details-3.png)




### Provide access credentials

As mentioned earlier, you can expose Kubernetes Secrets through the Google Cloud console using the [`secretKeyRef`](https://github.com/kubernetes-sigs/application/blob/master/config/crd/bases/app.k8s.io_applications.yaml#L305) element. In this tutorial, you provide a username and password to the operator so that they can log in to the application.

  1. In Cloud Shell, create the Secret:
         
         kubectl create secret generic boa-access --from-literal=boa-user=testuser --from-literal=boa-pass=password
         

**Note:** This Secret isn't used in the application. You create it for demonstration purposes in this tutorial.
  2. In the Cloud Shell Editor, overwrite the contents of the `application.yaml` file by pasting the following. This update includes references to the username and password in the `secretKeyRef` annotation.
         
         apiVersion: app.k8s.io/v1beta1
         kind: Application
         metadata:
           name: "bank-of-anthos"
           labels:
             app.kubernetes.io/name: "bank-of-anthos"
         spec:
           selector:
             matchLabels:
              app.kubernetes.io/name: "bank-of-anthos"
         
           componentKinds:
             - group: v1
               kind: Service
             - group: apps
               kind: Deployment
             - group: v1
               kind: StatefulSet
         
           descriptor:
             type: External App
         
             version: "2.3.2"
         
             description: |-
                 This application simulates a bank's payment processing network using [Anthos](/anthos/).
                 Bank of Anthos allows users to create artificial accounts and simulate transactions between accounts. Bank of Anthos was developed to create an end-to-end sample demonstrating Anthos best practices.
         
             links:
             - description: 'About Anthos on GCP'
               url: /anthos/
             - description: 'Bank of Anthos GitHub Repository'
               url: https://github.com/GoogleCloudPlatform/bank-of-anthos
         
           info:
           - name: Owner
             value: John Smith
           - name: App Frontend URL
             type: Reference
             valueFrom:
               serviceRef:
                 name: frontend
                 fieldPath: status.loadBalancer.ingress[0].ip
                 protocol: HTTPS
           - name: TestUser username
             type: Reference
             valueFrom:
               secretKeyRef:
                 name: boa-access
                 key: boa-user
         
           - name: TestUser password
             type: Reference
             valueFrom:
               secretKeyRef:
                 name: boa-access
                 key: boa-pass
         

  3. In Cloud Shell, deploy the Application resource:
         
         kubectl apply -f kubernetes-manifests/application.yaml
         

  4. In the Google Cloud console, go to the details page for the Bank of Anthos application.

[Go to Bank of Anthos details](https://console.cloud.google.com/kubernetes/application/us-central1-c/sample-cluster/default/bank-of-anthos/details)

  5. Click **preview secret data**. The username and password are revealed:

![The application details include links to access
credentials.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-app-details-4.png)




The ability to reveal Secret data can be a helpful feature for your operations teams. However, the ability to view these Secrets is governed by Identity and Access Management (IAM) access permissions for the GKE details page. Anyone with permissions to view clusters can also view Secrets, so it's important to consider carefully what you expose.

### Add an application icon

To make your application stand out, you can include a logo that's displayed on the applications list and your details page. To include a logo, you specify the [data URI](https://wikipedia.org/wiki/Data_URI_scheme) of the image in the `kubernetes-engine.cloud.google.com/icon` annotation.

Converting an image to a data URI is outside the scope of this tutorial. However, a Google search on "convert image to data uri" returns various utilities to help you produce the data string from an image. Because the data URI for the image used in this section is so long, it's impractical to include it in the tutorial. The full data URI can be seen in the [completed `application.yaml` file](https://gist.github.com/cgrant/c576747ecf808907cd9d51fda447f454). The data URI string should begin like this: `data:image/png;base64,iVBORw0KGgoAAAANSUhEUg....` It ends with `K5CYII=`. Be sure not to include any trailing quotation marks or HTML characters.

The full [`application.yaml` file is available as a gist](https://gist.github.com/cgrant/c576747ecf808907cd9d51fda447f454) for your reference.

To add an icon, you update the `metadata` section of `application.yaml`:

  1. Copy the following code:
         
         annotations:
           kubernetes-engine.cloud.google.com/icon: >-
             data:image/png;base64,DATA_URI

Replace `DATA_URI` with the string found in the completed `application.yaml` file that is referenced earlier.

  2. In the Cloud Shell Editor, paste the code that you copied after the `labels` section in the `metadata` section of `application.yaml`.

That section of `application.yaml` looks similar to the following, where `DATA_URI` represents the data URI value.
         
         apiVersion: app.k8s.io/v1beta1
         kind: Application
         metadata:
           name: "bank-of-anthos"
           labels:
             app.kubernetes.io/name: "bank-of-anthos"
           annotations:
             kubernetes-engine.cloud.google.com/icon: >-
               data:image/png;base64,DATA_URI
         spec:
         

  3. In Cloud Shell, deploy the application resource:
         
         kubectl apply -f kubernetes-manifests/application.yaml
         

  4. In the Google Cloud console, go to the **Applications** page.

[Go to Applications](https://console.cloud.google.com/kubernetes/application)

A logo is displayed in the list of applications:

![A logo is displayed next to the application name in the list of
applications.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-icon-1.png)

  5. In the Google Cloud console, go to the details page for the Bank of Anthos application.

[Go to Bank of Anthos details](https://console.cloud.google.com/kubernetes/application/us-central1-c/sample-cluster/default/bank-of-anthos/details)

A logo is displayed in the header of the details page:

![A logo is shown at the top of the list of application
details.](https://docs.cloud.google.com/static/solutions/images/using-gke-applications-page-cloud-console-icon-2.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, you can delete the Google Cloud project that you created for this tutorial.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Review other examples of `application.yaml` files files in the [Kubernetes folder of the `click-to-deploy` GitHub repository](https://github.com/GoogleCloudPlatform/click-to-deploy/tree/master/k8s). Look for other `application.yaml` files under `chart/<application>/templates/` for the various apps—for example, [as seen in this file](https://github.com/GoogleCloudPlatform/click-to-deploy/blob/master/k8s/magento/chart/magento/templates/application.yaml).
  * Use [Marketplace deployments](https://console.cloud.google.com/marketplace/browse?filter=solution-type:k8s) for Google Click to Deploy solutions for GKE.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
