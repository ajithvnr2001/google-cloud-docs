---
url: https://docs.cloud.google.com/dotnet/docs/getting-started/getting-started-on-compute-engine-net-netframework/
title: Deploy an ASP.NET application to Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:36.555705+00:00
---

# Deploy an ASP.NET application to Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/getting-started/getting-started-on-compute-engine-net-netframework/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Guides ](https://docs.cloud.google.com/dotnet/docs/setup)



Send feedback 

#  Deploy an ASP.NET application to Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to a deploy a .NET web application to Compute Engine.

This tutorial is intended for developers and DevOps engineers who have basic knowledge of Microsoft .NET and Compute Engine.

## Objectives

Deploy an ASP.NET Core web application that uses .NET 6 and runs on Linux to a single Compute Engine instance.

**Note:** For information on deploying an ASP.NET Model-View-Controller (MVC) web-application that uses .NET Framework 4 and runs on Windows, see [Deploy an ASP.NET MVC application to Compute Engine](https://docs.cloud.google.com/dotnet/docs/getting-started/getting-started-on-compute-engine-net-netframework-windows).

This tutorial shows you how to complete the following tasks to reach your objective: 

  * Deploy a Compute Engine VM
  * Set up load balancing
  * Deploy the ASP.NET application



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine virtual machine (VM) instances](https://cloud.google.com/compute/all-pricing)
  * [Compute Engine persistent disks](https://cloud.google.com/compute/all-pricing#disk)



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

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

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

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)




## Deploy a Compute Engine VM

This section shows you how to create a Linux VM, or a Windows Server VM that runs [Microsoft Internet Information Services (IIS) web servers](https://www.iis.net/) on Compute Engine.

  1. Set default values for your project ID and Compute Engine zone. This helps you save time.
         
         gcloud config set project PROJECT_ID
         gcloud config set compute/zone ZONE
         

Replace the following:

     * `PROJECT_ID` with the ID of your Google Cloud project.
     * `ZONE` with the name of the zone that you're going to use for creating resources. If you are unsure about which zone to pick, use the zone geographically located closest to you.

For example:
    
    gcloud config set project test-project-12345
    gcloud config set compute/zone us-central1-a
    

  2. Create a VM instance:

To create a Linux VM, do the following:

     1. Create a [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/window) for the VM instance. The script runs during VM initialization and [install the .NET runtime](https://learn.microsoft.com/en-us/dotnet/core/install/linux-debian):
            
            "if ! dpkg-query -W aspnetcore-runtime-6.0
            then
                curl https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb  -O
                sudo dpkg -i packages-microsoft-prod.deb
                rm packages-microsoft-prod.deb
                sudo apt-get update && sudo apt-get install -y aspnetcore-runtime-6.0
            fi
            " | Out-File -Encoding ASCII startup.sh
            

     2. Create the VM instance and use `startup.sh` as startup script:
            
            gcloud compute instances create clouddemo-1 `
                --image-family debian-11 `
                --image-project debian-cloud `
                --machine-type n1-standard-2 `
                --boot-disk-type pd-ssd `
                --tags loadbalancer-backend `
                --metadata-from-file startup-script=startup.sh
            

  3. Monitor the initialization process of the VM by viewing its serial port output:
         
         gcloud compute instances tail-serial-port-output clouddemo-1
         

Wait about 5 minutes until you see the output `Instance setup finished` or `Startup finished`, and then press Ctrl+C. At this point, the installation of prerequisites is complete and the VM instance is ready to be used.




## Set up load balancing

To make your ASP.NET app available over the internet, you have to use an [HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/https). To associate your VM instance with the load balancer, create an [instance group](https://docs.cloud.google.com/compute/docs/instance-groups) and assign this instance group to the load balancer:

  1. Create an [unmanaged instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances) and add the VM instance:
         
         gcloud compute instance-groups unmanaged create clouddemo-1
         gcloud compute instance-groups unmanaged add-instances clouddemo-1 --instances clouddemo-1
         

  2. Create a health check that checks if the web server is running:
         
         gcloud compute http-health-checks create clouddemo-health `
             --check-interval 5s `
             --unhealthy-threshold 2 `
             --request-path / `
             --port 5000
         gcloud compute instance-groups set-named-ports clouddemo-1 --named-ports=http:5000
         

  3. Create a load balancer backend service that uses the HTTP health check and the instance group that you created previously:
         
         gcloud compute backend-services create clouddemo-backend `
           --http-health-checks clouddemo-health `
           --port-name http `
           --protocol HTTP `
           --global
         gcloud compute backend-services add-backend clouddemo-backend `
           --instance-group clouddemo-1 `
           --global `
           --instance-group-zone $(gcloud config get-value compute/zone)
         

  4. Create a front-end for the load balancer:
         
         gcloud compute url-maps create clouddemo-map --default-service clouddemo-backend
         gcloud compute target-http-proxies create clouddemo-proxy --url-map clouddemo-map
         gcloud compute forwarding-rules create clouddemo-frontend --global --target-http-proxy clouddemo-proxy --ports 80
         

  5. Create a [firewall rule that allows the load balancer](https://docs.cloud.google.com/load-balancing/docs/https#firewall-rules) to send HTTP requests to instances that have been annotated with the `loadbalancer-backend` tag.
         
         gcloud compute firewall-rules create loadbalancer-backend `
           --source-ranges "130.211.0.0/22,35.191.0.0/16" `
           --target-tags loadbalancer-backend `
           --allow tcp:80,tcp:5000
         

  6. Lookup the IP address of the load balancer:
         
         gcloud compute forwarding-rules describe clouddemo-frontend --global --format "value(IPAddress)"
         

Take note of the IP address. You will need it later.




## Deploy the ASP.NET application

  1. Open a PowerShell console.

  2. [Download and unzip](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/archive/refs/heads/main.zip) or clone the sample repository from github:
         
         git clone https://github.com/GoogleCloudPlatform/dotnet-docs-samples.git
         

  3. Build the deployment package:

     1. Switch to the directory that contains the sample application:
            
            cd dotnet-docs-samples\applications\clouddemo\netcore
            

     2. Build the solution:
            
            dotnet publish -c Release
            

  4. Copy the deployment package to the VM:

     1. Copy the contents of the `publish` folder to your home directory on the VM:
            
            gcloud compute scp --recurse CloudDemo.MvcCore\bin\Release\net6.0\publish clouddemo-1:
            

     2. [Connect to the VM by using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

     3. On the VM, create a folder `/var/www/clouddemo` and copy the application files into this folder:
            
            sudo mkdir -p /var/www/clouddemo
            sudo chown -R www-data:www-data /var/www/clouddemo
            sudo cp -r publish/* /var/www/clouddemo
            

     4. Register the application as a systemd unit:
            
            cat <<EOF > kestrel-clouddemo.service
            [Unit]
            Description=Cloud Demo ASP.NET app
            
            [Service]
            WorkingDirectory=/var/www/clouddemo
            ExecStart=/usr/bin/dotnet /var/www/clouddemo/CloudDemo.MvcCore.dll
            Restart=always
            Environment=ASPNETCORE_ENVIRONMENT=Production
            Environment=ASPNETCORE_URLS=http://0.0.0.0:5000
            
            [Install]
            WantedBy=multi-user.target
            EOF
            
            sudo mv kestrel-clouddemo.service /etc/systemd/system/
            sudo systemctl daemon-reload
            sudo systemctl start kestrel-clouddemo
            

  5. On your local computer, open a web browser and navigate to the following address:
         
         http://LOADBALANCER_IP/
         

Replace `LOADBALANCER_IP` with the IP address that you obtained after deploying the load balancer.

You now see the demo application and the title _This app is running on Compute Engine_.




## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources.

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

You'll need to individually delete all the resources created for the project (for example: instance groups, health checks, backend services, http proxy, and forwarding rules). You can't delete the VM instances until delete all these resources.

## What's next

  * Learn more about [creating and running virtual machines on Google infrastructure](https://docs.cloud.google.com/compute/docs).
  * Review the best practices in the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
