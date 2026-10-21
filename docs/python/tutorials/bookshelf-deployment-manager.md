---
url: https://docs.cloud.google.com/python/tutorials/bookshelf-deployment-manager/
title: Deploying the Python Bookshelf app using Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:33.889371+00:00
---

# Deploying the Python Bookshelf app using Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/tutorials/bookshelf-deployment-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Guides ](https://docs.cloud.google.com/python/docs/setup)



Send feedback 

#  Deploying the Python Bookshelf app using Cloud Deployment Manager Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to deploy the Python Bookshelf sample app using [Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs).

Deployment Manager lets you create the necessary Google Cloud [resources](https://docs.cloud.google.com/deployment-manager/latest/resources) for a deployment in a single step, through a declarative, repeatable process. With Deployment Manager, you can update your deployments, track your modifications over time, create templates using [Jinja](http://jinja.pocoo.org/) or Python, and parameterize your templates, so that similar deployments share a template.

## Objectives

  * Clone and configure the Bookshelf sample app.
  * Create Deployment Manager configurations and templates.
  * Create Deployment Manager deployments.
  * Deploy the Bookshelf sample app using Deployment Manager.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [Datastore](https://docs.cloud.google.com/datastore/pricing)
  * [Cloud Logging](https://docs.cloud.google.com/stackdriver/pricing)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Datastore API, Cloud Storage API, Pub/Sub API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datastore.googleapis.com,pubsub,storage_api,logging)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Datastore API, Cloud Storage API, Pub/Sub API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datastore.googleapis.com,pubsub,storage_api,logging)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Install Python, `pip`, and `virtualenv` on your system. For instructions, see [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup) for Google Cloud. 



## Creating a Cloud Storage bucket

The following instructions detail how to create a Cloud Storage bucket. Buckets are the basic containers that hold your data in Cloud Storage.

**Note:** You can choose [any name](https://docs.cloud.google.com/storage/docs/buckets#naming) for your Cloud Storage bucket. It's a good practice to give your bucket the same name as your project ID. Bucket names must be unique across all of Google Cloud, so it's possible that you can't use your project ID as the bucket name.

  1. In your terminal window, create a Cloud Storage bucket, where YOUR_BUCKET_NAME represents the name of your bucket:
         
         gcloud storage buckets create gs://YOUR_BUCKET_NAME

  2. To view uploaded images in the Bookshelf app, set the bucket's Identity and Access Management policy to grant the `legacyObjectReader` role to `allUsers`:
         
         gcloud storage buckets add-iam-policy-binding gs://YOUR_BUCKET_NAME
         --member=allUsers --role=roles/storage.legacyObjectReader




## Cloning the sample app

The sample app is available on GitHub at [`GoogleCloudPlatform/getting-started-python`](https://github.com/GoogleCloudPlatform/getting-started-python).

  1. Clone the repository:
         
         git clone https://github.com/GoogleCloudPlatform/getting-started-python.git -b steps
         

  2. Go to the sample directory:
         
         cd getting-started-python/7-gce
         




## Configuring the app

  1. Open `config.py` for editing.

     * Set the value of `PROJECT_ID` to your project ID.

     * Set the value `CLOUD_STORAGE_BUCKET` to the name of your Cloud Storage bucket.

  2. Save and close `config.py`.




## Running the app on your local computer

  1. Create an isolated Python environment, and install dependencies:

### Linux/macOS
         
         virtualenv -p python3 env
         source env/bin/activate
         pip install -r requirements.txt
         

### Windows
         
         virtualenv -p python3 env
         env\scripts\activate
         pip install -r requirements.txt
         

  2. Run the application:
         
         python main.py
         

  3. In your browser, enter the following address:

<http://localhost:8080>




To stop the local web server, press `Control+C`. If you want to exit the virtual environment, enter `deactivate`.

## Deploying the sample app

### Push your code to a repository

You can get your code onto a running Compute Engine instance in several ways. One way is to use [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories). Every project includes a Git repository that is available to Compute Engine instances. Your instances then pull the latest version of your app's code during startup. Using a Git repository is convenient because updating your app doesn't require configuring new images or instances; just restart an existing instance or create one.

  1. For your first time using Git, use `git config --global` to set up [your identity](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup#_your_identify).

  2. In your Google Cloud console, create a repository:

[Create repository](https://console.cloud.google.com/code/develop/repo)

  3. Then push your app code to your project's repository where `[YOUR_PROJECT_ID]` is your project ID and `[YOUR_REPO]` is the name of your repository:
         
         git commit -am "Updating configuration"
         git config credential.helper gcloud.sh
         git remote add cloud https://source.developers.google.com/p/[YOUR_PROJECT_ID]/r/[YOUR_REPO]
         git push cloud master
         




### Create the deployment

After your configuration is committed and your code is uploaded to Cloud Source Repositories, you can use the Deployment Manager to create the deployment:

  1. Go to the `deployment_manager` directory:
         
         cd getting-started-python/7-gce/gce/deployment_manager
         

  2. Create the deployment:
         
         gcloud deployment-manager deployments create my-deployment --config config.yaml
         

  3. View a list of all the deployments:
         
         gcloud deployment-manager deployments list
         

  4. Get a description of the deployment and the resources it created:
         
         gcloud deployment-manager deployments describe my-deployment
         




### View your app

After you create the forwarding rule, it can take several minutes for your configuration to propagate and for traffic to be routed to your instances.

  1. To check the progress:
         
         gcloud compute backend-services get-health bookshelf-my-deployment-frontend --global
         

  2. When at least one of your instances reports `HEALTHY`, get the forwarding IP address for the load balancer:
         
         gcloud compute forwarding-rules list --global
         

Your forwarding-rules IP address is in the `IP_ADDRESS` column.

  3. In your browser, enter the IP address from the list.

Your app is now running on Google Cloud.




## Understanding the code

### Configure the deployment

You can see how the deployment is configured in `config.yaml`:
    
    
    imports:
    - name: bookshelf.jinja
      path: ./bookshelf.jinja
    
    resources:
    - name: bookshelf
      type: bookshelf.jinja
      properties:
        zone: us-central1-f
        machine-type: n1-standard-1
        machine-image: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/family/debian-9
        min-instances: 1
        max-instances: 10
        target-utilization: 0.6
        scopes:
        - https://www.googleapis.com/auth/cloud-platform
    

The configuration file imports the template file as a resource and uses it to define a resource named `bookshelf`. The template takes several properties as parameters. For more information about creating Deployment Manager configuration files, see [Creating a configuration](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/create-a-configuration).

### Configure the deployment template's schema

Look at the schema file `bookshelf.jinja.schema`, which defines and documents the parameters that the deployment is expected to provide in its configuration file. For more information about configuration schemas, see [Using schemas](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/using-schemas).
    
    
    info:
      title: Bookshelf GCE Deploy
      author: Google Inc.
      description: Creates a GCE Deployment
    
    imports:
    - name: startup-script
      path: ../startup-script.sh
    
    required:
    - zone
    - machine-type
    - min-instances
    - max-instances
    - scopes
    
    properties:
      zone:
        description: Zone to create the resources in.
        type: string
      machine-type:
        description: Type of machine to use
        type: string
      machine-image:
        description: The OS image to use on the machines
        type: string
      min-instances:
        description: The minimum number of VMs the autoscaler will create
        type: integer
      max-instances:
        description: The maximum number of VMs the autoscaler will create
        type: integer
      target-utilization:
        description: The target CPU usage for the autoscaler to base its scaling on
        type: number
      scopes:
        description: A list of scopes to create the VM with
        type: array
        minItems: 1
        items:
          type: string
    

### Configure the deployment template

The template defines several resources needed to create an autoscaled, load- balanced, managed instance group. For a full description of the resources created, see the comments in the template and review the [Bookshelf on Compute Engine](https://docs.cloud.google.com/python/getting-started/run-on-compute-engine) tutorial.

Keep in mind that Deployment Manager provides a way to declaratively define resources, but most of the configuration for a given resource is defined by its API. For example, most of the configuration options for the instance template resource are found in the [instance template resource definition](https://docs.cloud.google.com/compute/docs/reference/latest/instanceTemplates#resource) in the reference documentation for the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/latest).

The template is written using the [Jinja](http://jinja.pocoo.org/) templating language. When writing Deployment Manager templates, you can either use Jinja or Python. Jinja has the advantage of being more declarative, which can be more readable and easier to understand than Python. For some complex deployments, the full expressiveness of Python might make things simpler. In this case, Jinja is sufficient to create the necessary resources.

In a template, certain environment variables are automatically set, and you can access these variables by using the `env` dictionary. In this case, the name of the deployment is referenced as a name to be reused when assigning names to the resources that are created. For more information about available environment variables, see [Using environment variables](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables) in the Deployment Manager documentation:
    
    
    {% set NAME = "bookshelf-" + env["deployment"] %}
    {% set SERVICE = "bookshelf-" + env["deployment"] + "-frontend" %}

The template uses the same startup script that is used in the [Compute Engine tutorial](https://docs.cloud.google.com/python/getting-started/run-on-compute-engine). The script's content is inserted into the template, and the [Jinja indent directive](https://jinja.palletsprojects.com/en/3.1.x/templates/) indents the content correctly:
    
    
                value: |
    {{imports['startup-script']|indent(14, true)}}

In a Deployment Manager Jinja template, you can also refer to resources created elsewhere in the template. In the following example, the backend service uses the reference of the managed instance group to obtain the instance group it should point to:
    
    
    - group: $(ref.{{ NAME }}-frontend-group.instanceGroup)
      zone: {{ properties['zone'] }}

Properties specified in `config.yaml` can be used in the template:
    
    
    minNumReplicas: {{ properties['min-instances'] }}
    maxNumReplicas: {{ properties['max-instances'] }}
    loadBalancingUtilization:
      utilizationTarget: {{ properties['target-utilization'] }}

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

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



### Delete your deployment

To delete your deployment, enter the following command. This command deletes the load balancer and any Compute Engine instances that are associated with your deployment:
    
    
    gcloud deployment-manager deployments delete my-deployment
    

## What's next

  * Learn more about [defining Deployment Manager templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/adding-templates).

  * Learn how to [run the Python Bookshelf sample app on Google Kubernetes Engine](https://docs.cloud.google.com/python/tutorials/bookshelf-on-kubernetes-engine).

  * Learn how to [run the Python Bookshelf sample app in the App Engine flexible environment](https://docs.cloud.google.com/python/getting-started/tutorial-app).

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 

  * Explore other [Google Cloud services](https://docs.cloud.google.com/).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
