---
url: https://docs.cloud.google.com/java/getting-started/getting-started-on-compute-engine/
title: Getting started with Java on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:44.776143+00:00
---

# Getting started with Java on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/getting-started/getting-started-on-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Getting started with Java on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to get started with Compute Engine. Follow this tutorial by deploying a Hello World Java web app to Compute Engine. For help getting started with App Engine, see the [App Engine standard environment](https://docs.cloud.google.com/java/getting-started/tutorial-app).

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

[Go to Cloud Shell](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/getting-started-java&working_dir=gce)

Cloud Shell provides command-line access to your cloud resources directly from the browser.

  9. If you agree to clone the repository, click **Confirm** to download the sample code and change into the app directory. 

  10. In Cloud Shell, configure the gcloud CLI to use your new Google Cloud project: 
         
         # Configure gcloud for your project
         gcloud config set project YOUR_PROJECT_ID




## Running the app in Cloud Shell

  1. In Cloud Shell, start a local web server:
         
         mvn -Plocal clean jetty:run-exploded -DprojectID=YOUR-PROJECT-ID
         

  2. In Cloud Shell, click **Web preview** , and select **Preview on port 8080**. This opens a new window with your running app.

In your web browser, you see some Hello World text, served from your local machine.

  3. When you're ready to move on, stop the local web server by pressing `Control+C` in Cloud Shell.




## Deploying to a single instance

This section walks you through running a single instance of your app on Compute Engine.

![Single-instance deployment.](https://docs.cloud.google.com/static/languages/images/compute-single-instance.svg)

From Cloud Shell, you can deploy to a single Compute Engine instance virtual machine (VM) which runs your app.

### Use a startup script to initialize an instance

You need a way to instruct your instance to download and run your code. An instance can have a startup script that runs whenever the instance is started or restarted.

A startup script runs when an instance first boots.
    
    
    set -e
    set -v
    
    # Talk to the metadata server to get the project id
    PROJECTID=$(curl -s "http://metadata.google.internal/computeMetadata/v1/project/project-id" -H "Metadata-Flavor: Google")
    
    echo "Project ID: ${PROJECTID}"
    
    # Install dependencies from apt
    apt-get install -yq openjdk-11-jdk git maven
    
    mvn --version
    
    # Jetty Setup
    mkdir -p /opt/jetty/temp
    mkdir -p /var/log/jetty
    
    # Get Jetty
    curl -L https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-distribution/9.4.13.v20181111/jetty-distribution-9.4.13.v20181111.tar.gz -o jetty9.tgz
    tar xf jetty9.tgz  --strip-components=1 -C /opt/jetty
    
    # Add a Jetty User
    useradd --user-group --shell /bin/false --home-dir /opt/jetty/temp jetty
    
    cd /opt/jetty
    # Add running as "jetty"
    java -jar /opt/jetty/start.jar --add-to-startd=setuid
    cd /
    
    # Clone the source repository.
    git clone https://github.com/GoogleCloudPlatform/getting-started-java
    cd getting-started-java/gce
    
    # Build the .war file and rename.
    # very important - by renaming the war to root.war, it will run as the root servlet.
    mvn clean package -q
    mv target/getting-started-gce-1.0-SNAPSHOT.war /opt/jetty/webapps/root.war
    
    # Make sure "jetty" owns everything.
    chown --recursive jetty /opt/jetty
    
    # Configure the default paths for the Jetty service
    cp /opt/jetty/bin/jetty.sh /etc/init.d/jetty
    echo "JETTY_HOME=/opt/jetty" > /etc/default/jetty
    {
      echo "JETTY_BASE=/opt/jetty"
      echo "TMPDIR=/opt/jetty/temp"
      echo "JAVA_OPTIONS=-Djetty.http.port=80"
      echo "JETTY_LOGS=/var/log/jetty"
    } >> /etc/default/jetty
    
    # Reload daemon to pick up new service
    systemctl daemon-reload
    
    # Install logging monitor. The monitor will automatically pickup logs sent to syslog.
    curl -sSO https://dl.google.com/cloudagents/add-logging-agent-repo.sh
    sudo bash add-logging-agent-repo.sh --also-install
    
    service google-fluentd restart &
    
    service jetty start
    service jetty check
    
    echo "Startup Complete"

The startup script performs these tasks:

  * Installs Java 11 and makes it the default version.

  * Installs and configures Jetty.

  * Copies the Java WAR file from the Cloud Storage bucket to Jetty's `webapps` and renames it `root.war`. This makes it the root servlet, so it doesn't need to be named in the URL.

  * Installs the Cloud Logging agent and configures it to monitor the app logs. This means that the logging configured in the previous steps of this tutorial are uploaded just as if you were using the App Engine flexible environment.




### Create and configure a Compute Engine instance

  1. Create a Compute Engine instance:
         
         gcloud compute instances create my-app-instance   
             --image-family=debian-10   
             --image-project=debian-cloud   
             --machine-type=g1-small   
             --scopes userinfo-email,cloud-platform   
              --metadata-from-file startup-script=gce/startup-script.sh   
             --zone YOUR_ZONE   
             --tags http-server
           

Replace `YOUR_ZONE` with a development zone, for example `us-central1-a`. For more information on regions and zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions). 

This creates a new instance, allows it to access Google Cloud services, and runs your startup script. The instance name is `my-app-instance`.

  2. Check the progress of the instance creation:
         
         gcloud compute instances get-serial-port-output my-app-instance --zone YOUR_ZONE
         

When the startup script is complete, you see the following message:
         
         startup-script: INFO Finished running startup scripts.
         

  3. Create a firewall rule to allow traffic to your instance:
         
         gcloud compute firewall-rules create default-allow-http-80 \
             --allow tcp:80 \
             --source-ranges 0.0.0.0/0 \
             --target-tags http-server \
             --description "Allow port 80 access to http-server"
         

  4. Get the external IP address of your instance:
         
         gcloud compute instances list
         

  5. To see your app running, enter this URL in your browser:
         
         http://YOUR_INSTANCE_IP
         

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
    gcloud compute firewall-rules delete default-allow-http-80

## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 

  * For other Java resources for building your apps, see the following:

    * Manage and monitor your Instance Group deployment at [Compute Engine > Instance groups](https://console.cloud.google.com/compute/instanceGroups).
    * Manage your load balancing configuration, including URL maps and backend services, at [Network services > Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list). 
  * [Deploy an app to Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/deploy-app-container-image)

  * Explore other [Google Cloud services](https://docs.cloud.google.com/). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
