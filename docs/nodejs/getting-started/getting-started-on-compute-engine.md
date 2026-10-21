---
url: https://docs.cloud.google.com/nodejs/getting-started/getting-started-on-compute-engine/
title: Getting started with Node.js on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:29:55.382966+00:00
---

# Getting started with Node.js on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/getting-started/getting-started-on-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Guides ](https://docs.cloud.google.com/nodejs/docs/setup)



Send feedback 

#  Getting started with Node.js on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to get started with Compute Engine. Follow this tutorial by deploying a Hello World Node.js web app to Compute Engine. For help getting started with App Engine, see the [App Engine standard environment](https://docs.cloud.google.com/nodejs/getting-started/tutorial-app).

## Objectives

  * Use Cloud Shell to download and deploy a Hello World sample app. 
  * Deploy a Hello World sample app to a single Compute Engine instance.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://cloud.google.com/compute/all-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute)

  8. In the Google Cloud console, open the app in [Cloud Shell](https://docs.cloud.google.com/shell). 

[Go to Cloud Shell](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/nodejs-getting-started.git&working_dir=gce)

Cloud Shell provides command-line access to your cloud resources directly from the browser.

  9. If you agree to clone the repository, click **Confirm** to download the sample code and change into the app directory. 

  10. In Cloud Shell, configure the gcloud CLI to use your new Google Cloud project: 
         
         # Configure gcloud for your project
         gcloud config set project YOUR_PROJECT_ID




## Run the app in Cloud Shell

If you clicked **Go to Cloud Shell** in the preceding section, Cloud Shell cloned the `nodejs-getting-started` repository to your instance. After the instance launches, your working directory is `~/cloudshell_open/nodejs-getting-started/gce`. If you are not in this directory, see the steps in Before you begin.

  1. Install dependencies:
         
         npm install
         

  2. Run the app:
         
         npm start
         

  3. In Cloud Shell, click **Web preview** , and select **Preview on port 8080**. This opens a new window with your running app.




To stop the local web server, press `Control+C`.

## Set up Cloud Source Repositories

  1. Enable the Cloud Source Repositories API.

[Enable the Cloud Source Repositories API](https://console.cloud.google.com/apis/enableflow?apiid=sourcerepo.googleapis.com&amp;redirect=https://cloud.google.com/source-repositories/docs/create-code-repository)

  2. In the Google Cloud console, go to Cloud Source Repositories.

[ Go to Cloud Source Repositories](https://source.cloud.google.com/repos)

  3. Select **Add repository**.

![Select add repository.](https://docs.cloud.google.com/static/nodejs/images/addRepository.png)

  4. Select **Create new repository** , and then click **Continue**.

  5. In the **Repository name** field, enter `new-repo`.

  6. In the **Project** field, enter the project ID of the project that you created or selected for this tutorial, and then click **Continue**.

  7. Select **Clone your repository to a local Git repository**.

  8. In Cloud Shell, return to root and clone the repository by following the instructions in the **Google Cloud SDK** tab, and keep this tab open.

![follow instructions to clone youre repository to a local Git repository](https://docs.cloud.google.com/static/nodejs/images/cloneRepoUsingGoogleCloudSDK.png)

  9. Before completing the final step under the instructions, copy your app into your new repository in Cloud Shell:
         
         cd new-repo
         cp ../cloudshell_open/nodejs-getting-started/gce/app.js app.js
         cp ../cloudshell_open/nodejs-getting-started/gce/package.json package.json

  10. Follow the remaining instructions in the **Google Cloud SDK** tab to commit your changes to your repository. Confirm that you have added your code to the repository by refreshing the browser and checking that your code was added to the repo `new-repo`.




## Deploy to a single instance

This section walks you through running a single instance of your app on Compute Engine.

![Single-instance deployment.](https://docs.cloud.google.com/static/languages/images/compute-single-instance.svg)

From Cloud Shell, you can deploy to a single Compute Engine instance virtual machine (VM) which runs your app.

### Use a startup script to initialize an instance

You need a way to instruct your instance to download and run your code. An instance can have a startup script that runs whenever the instance is started or restarted.

Here is the startup script that is included in the Hello World sample app:
    
    
    set -ve
    
    
    # Talk to the metadata server to get the project id
    PROJECTID=$(curl -s "http://metadata.google.internal/computeMetadata/v1/project/project-id" -H "Metadata-Flavor: Google")
    
    # Install logging monitor. The monitor will automatically pick up logs sent to
    # syslog.
    curl -s "https://storage.googleapis.com/signals-agents/logging/google-fluentd-install.sh" | bash
    service google-fluentd restart &
    
    # Install dependencies from apt
    apt-get update
    apt-get install -yq ca-certificates git build-essential supervisor
    
    # git requires $HOME and it's not set during the startup script.
    # Fetch source code
    export HOME=/root
    git clone https://github.com/GoogleCloudPlatform/nodejs-getting-started.git /opt/app
    
    # Install nodejs
    mkdir /opt/nodejs
    curl https://nodejs.org/dist/v22.14.0/node-v22.14.0-linux-x64.tar.xz | tar xvfJ - -C /opt/nodejs --strip-components=1
    ln -s /opt/nodejs/bin/node /usr/bin/node
    ln -s /opt/nodejs/bin/npm /usr/bin/npm
    
    # Install app dependencies
    cd /opt/app/gce
    npm install
    
    # Create a nodeapp user. The application will run as this user.
    useradd -m -d /home/nodeapp nodeapp
    chown -R nodeapp:nodeapp /opt/app
    
    # Configure supervisor to run the node app.
    cat >/etc/supervisor/conf.d/node-app.conf << EOF
    [program:nodeapp]
    directory=/opt/app/gce
    command=npm start
    autostart=true
    autorestart=true
    user=nodeapp
    environment=HOME="/home/nodeapp",USER="nodeapp",NODE_ENV="production"
    stdout_logfile=syslog
    stderr_logfile=syslog
    EOF
    
    supervisorctl reread
    supervisorctl update
    
    # Application should now be running under supervisor

The startup script performs the following tasks:

  * Installs the Cloud Logging agent. The agent automatically collects logs from syslog.

  * Installs [Supervisor](http://supervisord.org/) to run the app as a daemon.

  * Clones the app's source code from Cloud Source Repositories and installs dependencies.

  * Configures Supervisor to run the app. Supervisor makes sure the app is restarted if it exits unexpectedly or is terminated by an admin or other process. It also sends the app's `stdout` and `stderr` to syslog to be collected by the Logging agent.




### Create and configure a Compute Engine instance

  1. Create a Compute Engine instance:

### Linux/macOS
         
         gcloud compute instances create my-app-instance \
             --image-family=debian-9 \
             --image-project=debian-cloud \
             --machine-type=g1-small \
             --scopes userinfo-email,cloud-platform \
             --metadata app-location=us-central1-f \
             --metadata-from-file startup-script=gce/startup-script.sh \
             --zone us-central1-f \
             --tags http-server
         

### Windows
         
         gcloud compute instances create my-app-instance ^
             --image-family=debian-9 ^
             --image-project=debian-cloud ^
             --machine-type=g1-small ^
             --scopes userinfo-email,cloud-platform ^
             --metadata-from-file startup-script=gce/startup-script.sh ^
             --zone us-central1-f ^
             --tags http-server
         

Replace the zone with a development zone, for example `us-central1-a`. For more information on regions and zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions). 

This creates a new instance, allows it to access Google Cloud services, and runs your startup script. The instance name is `my-app-instance`.

  2. Check the progress of the instance creation:
         
         gcloud compute instances get-serial-port-output my-app-instance --zone YOUR_ZONE
         

Replace `YOUR_ZONE` with the zone you deployed your instance to. 

When the startup script is complete, you see the following message:
         
         startup-script: INFO Finished running startup scripts.
         

  3. Create a firewall rule to allow traffic to your instance:
         
         gcloud compute firewall-rules create default-allow-http-8080 \
             --allow tcp:8080 \
             --source-ranges 0.0.0.0/0 \
             --target-tags http-server \
             --description "Allow port 8080 access to http-server"
         

  4. Get the external IP address of your instance:
         
         gcloud compute instances list
         

  5. To see your app running, enter this URL in your browser:
         
         http://YOUR_INSTANCE_IP:8080
         

Replace `YOUR_INSTANCE_IP` with the external IP address of your instance.




### Manage and monitor an instance

You can use the Google Cloud console to monitor and manage your instance.

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. 
  3. To view all of the logs generated by your Compute Engine resources, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

[Cloud Logging](https://docs.cloud.google.com/logging) is automatically configured to gather logs from various common services, including `syslog`. 




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources
    
    
    gcloud compute instances delete my-app-instance --zone=YOUR_ZONE --delete-disks=all
    gcloud compute firewall-rules delete default-allow-http-8080

## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 

  * For other Node.js resources for building your apps, see the following:

    * Manage and monitor your Instance Group deployment at [Compute Engine > Instance groups](https://console.cloud.google.com/compute/instanceGroups).
    * Manage your load balancing configuration, including URL maps and backend services, at [Network services > Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list).
    * [Handle sessions with Firestore](https://docs.cloud.google.com/nodejs/getting-started/session-handling-with-firestore)
    * [Authenticate users with Identity-Aware Proxy](https://docs.cloud.google.com/nodejs/getting-started/authenticate-users)
    * [Deploy an app to Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/deploy-app-container-image)
    * Explore other [Google Cloud services](https://docs.cloud.google.com/). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
