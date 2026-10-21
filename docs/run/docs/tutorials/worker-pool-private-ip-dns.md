---
url: https://docs.cloud.google.com/run/docs/tutorials/worker-pool-private-ip-dns/
title: Register private IP addresses for worker pools using Cloud DNS \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:02.246082+00:00
---

# Register private IP addresses for worker pools using Cloud DNS  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/worker-pool-private-ip-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Register private IP addresses for worker pools using Cloud DNS Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to register the private IP address of a Cloud Run worker pool instance within a Cloud DNS managed zone. In this tutorial, you use a startup script to dynamically detect the instance IP through the metadata server, and create a Node.js application to handle ingress directly within your VPC network.

## Objectives

  * Create a Cloud DNS managed zone to host the records for your worker pool.
  * Create a Node.js application to handle ingress traffic over the VPC network.
  * Deploy a worker pool with Direct VPC ingress to assign a private IP address from your subnet to your worker instance.
  * Test your application to access the private IP address from a virtual machine (VM) instance on the same VPC network.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://docs.cloud.google.com/build/docs)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud DNS](https://cloud.google.com/dns)
  * [Compute Engine](https://docs.cloud.google.com/compute)



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

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud DNS, Cloud Run, Compute Engine, Artifact Registry, and Cloud Build APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dns.googleapis.com,run.googleapis.com,compute.googleapis.com,cloudbuild.googleapis.com,artifactregistry.googleapis.com)

  7. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  8. Update components: 
         
         gcloud components update

  9. Set your project ID by running the following command: 
         
         gcloud config set project PROJECT_ID

Replace PROJECT_ID with the ID of your Google Cloud project.



### Required roles

To get the permissions that you need to complete the tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`)
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Cloud DNS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete the tutorial. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

### Create a custom service account

Create a custom service account with the [minimum permissions required](https://docs.cloud.google.com/iam/docs/using-iam-securely) to register DNS records. To set up the service account, do the following:

  1. Create a service account by running the following command:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
           --display-name="DNS Worker Pool Service Account"

Replace SERVICE_ACCOUNT_NAME with a name for your custom service account, for example `dns-worker-sa`.

  2. Grant the Cloud DNS Admin role to the service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/dns.admin"




## Create a Cloud DNS zone

Create a private Cloud DNS managed zone named `test-wp` to register your worker pool's instance IP.
    
    
    gcloud dns managed-zones create test-wp --description="new DNS zone for worker pools"  --dns-name="workerpools.example.com."  --visibility="private" --networks=default

## Create a Node.js application

Create a Node.js application that retrieves the worker pool instance's IP address using the metadata server, and then registers it with Cloud DNS.

  1. Create a folder named `worker` and change the directory into it:
         
         mkdir worker
         cd worker
         

  2. Create a file named `setup_dns.sh` and add the following script that runs when your worker pool instance starts. This script uses the instance hostname to generate the DNS record name. If there is more than one instance, multiple instances can use the same hostname leading to the creation of overlapping DNS records.
         
         #!/bin/bash
         
         # --- Variables ---
         # The name of your Cloud DNS managed zone.
         ZONE_NAME="test-wp"
         # The base domain suffix for the DNS entry. Use the part *after* the hostname.
         # For example, for "testinstance.workerpools.example.com.", the suffix is ".workerpools.example.com."
         DNS_SUFFIX=".workerpools.example.com."
         # The Time-To-Live (TTL) in seconds.
         TTL="300"
         # The record type (A for IPv4).
         RECORD_TYPE="A"
         # -----------------
         
         # 1. Dynamically generate DNS_NAME
         # Get the simple hostname (e.g., "testinstance") and append the defined suffix.
         # We use 'hostname -s' to get the short hostname.
         SHORT_HOSTNAME=$(hostname -s)
         DNS_NAME="${SHORT_HOSTNAME}${DNS_SUFFIX}"
         
         # 2. Dynamically assign NEW_IP
         # Get the IP address from metadata server using predefined key.
         NEW_IP=$(curl "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/ip" -H "Metadata-Flavor: Google")
         
         # --- Input Validation ---
         if [ -z "$NEW_IP" ]; then
             echo "❌ ERROR: Could not obtain a valid IP address from metadata server. Aborting."
             exit 1
         fi
         
         echo "Starting DNS record update for ${DNS_NAME} in zone ${ZONE_NAME}..."
         echo "New IP detected on this instance: ${NEW_IP}"
         
         # 3. Get the current existing IP address (if any)
         # This is required to know what to put in the --rrdatas for the delete command.
         EXISTING_IP=$(gcloud dns record-sets list \
             --zone="${ZONE_NAME}" \
             --name="${DNS_NAME}" \
             --type="${RECORD_TYPE}" \
             --format="value(rrdatas[0])" 2>/dev/null)
         
         # --- Conditional Deletion/Skip Check ---
         if [ -n "$EXISTING_IP" ] && [ "$EXISTING_IP" != "$NEW_IP" ]; then
             echo "Found existing IP: ${EXISTING_IP}. It is different from the new IP."
         
             # Delete the existing record
             echo "Deleting old record..."
             gcloud dns record-sets delete "${DNS_NAME}" \
                 --zone="${ZONE_NAME}" \
                 --type="${RECORD_TYPE}" \
                 --quiet
         
             if [ $? -ne 0 ]; then
                 echo "❌ ERROR: Failed to delete existing record. Aborting."
                 exit 1
             fi
         elif [ -n "$EXISTING_IP" ] && [ "$EXISTING_IP" == "$NEW_IP" ]; then
             echo "Existing IP (${EXISTING_IP}) matches the new IP. Skipping update."
             exit 0
         else
             echo "No existing record found for ${DNS_NAME}. Proceeding with creation."
         fi
         # ----------------------------------------
         
         # 4. Add the new record
         echo "Creating new record with IP: ${NEW_IP}..."
         gcloud dns record-sets create "${DNS_NAME}" \
           --zone="${ZONE_NAME}" \
           --type="${RECORD_TYPE}" \
           --ttl="${TTL}" \
           --rrdatas="${NEW_IP}"
         
         # Final status check
         if [ $? -eq 0 ]; then
             echo "✅ Successfully created/updated DNS record for ${DNS_NAME} to ${NEW_IP}."
         else
             echo "❌ ERROR: Failed to create the new DNS record."
             exit 1
         fi
         

  3. Create a `server.js` file with the following code to handle the private IP address ingress:
         
         // server.js
         
         // 1. Import the built-in 'http' module
         console.log("hello from worker pool")
         const http = require('http');
         
         // Define the port the server will listen on
         const PORT = 3000;
         
         // 2. Create the server instance
         const server = http.createServer((req, res) => {
           // Set the response HTTP header with status and type of content
           res.writeHead(200, {'Content-Type': 'text/plain'});
           // Write the response body
           res.end('Hello World!\n');
         });
         
         // 3. Start the server and listen on the specified port
         server.listen(PORT, () => {
           console.log(`Server running at http://localhost:${PORT}/`);
         });
         

  4. Create a `start.sh` script with the following code to perform the DNS setup first, before running your Node.js application:
         
         #!/bin/bash
         set -e
         
         # 1. Execute the setup script
         echo "Running setup_dns.sh..."
         /app/setup_dns.sh
         
         # 2. Run the main application
         echo "Starting server.js..."
         exec node /app/server.js
         

  5. Create the following Dockerfile to package the application in an image:
         
         # Choose a base image. This image includes gcloud, kubectl, etc.
         FROM google/cloud-sdk:latest
         
         # Install Node.js on top of the Cloud SDK image.
         RUN apt-get update && \
             apt-get install -y curl && \
             curl -sL https://deb.nodesource.com/setup_lts.x | bash - && \
             apt-get install -y nodejs && \
             # Clean up to reduce image size
             apt-get clean && \
             rm -rf /var/lib/apt/lists/*
         
         # Set the working directory inside the container.
         WORKDIR /app
         
         # Copy the application and scripts into the container.
         COPY setup_dns.sh .
         COPY server.js .
         COPY start.sh .
         
         # Make both scripts executable.
         RUN chmod +x setup_dns.sh start.sh
         
         # Define the entrypoint and default command.
         ENTRYPOINT ["/app/start.sh"]
         CMD []
         




## Deploy a worker pool with Direct VPC ingress

Deploy a worker pool named `test-cli-dns` and attach it to a VPC network.
    
    
    gcloud run worker-pools deploy test-cli-dns \
      --network default \
      --subnet default \
      --region us-central1 \
      --source . \
      --service-account SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
      --project PROJECT_ID

Replace PROJECT_ID with your Google Cloud project ID and SERVICE_ACCOUNT_NAME with the name of the service account you created.

## Test your application

Cloud Run worker pools with Direct VPC ingress are designed for internal-only traffic. They don't have a public IP. To verify ingress functionality, follow these steps to run a request using `curl` from a Compute Engine VM hosted on the same VPC network and subnet:

  1. Create a [test VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) in the same network and region as your worker pool:
         
         gcloud compute instances create wp-test-vm \
              --zone=us-central1-a \
              --network=default \
              --subnet=default
         

  2. Connect to the test VM through SSH by running the following command:
         
         gcloud compute ssh wp-test-vm --zone=us-central1-a
         

  3. From the VM terminal, invoke your service at the private IP address of the worker pool instance registered with Cloud DNS:
         
         curl http://localhost.workerpools.example.com:3000

You should see the output:
         
         Hello World!




Success! You've successfully configured your Cloud Run worker pool with Direct VPC ingress using a private IP address and Cloud DNS.

## Clean up

To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this tutorial.

### Delete the project

If you created a new project for this tutorial, delete the project. If you used an existing project and need to keep it without the changes you added in this tutorial, delete resources that you created for the tutorial.

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



### Delete tutorial resources

  1. Delete the Cloud Run service you deployed in this tutorial. Cloud Run services don't incur costs until they receive requests.

To delete your Cloud Run service, run the following command:
         
         gcloud run services delete SERVICE-NAME

Replace SERVICE-NAME with the name of your service.

You can also delete Cloud Run services from the [Google Cloud console](https://console.cloud.google.com/run).

  2. Remove the `gcloud` default region configuration you added during tutorial setup:
         
         gcloud config unset run/region
         

  3. Remove the project configuration:
         
         gcloud config unset project
         

  4. Delete other Google Cloud resources created in this tutorial:

     * [Delete the Cloud Run worker pool](https://docs.cloud.google.com/run/docs/managing/workerpools#delete).
     * [Delete the worker pool container image](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images) from Artifact Registry.
     * [Delete a Cloud DNS managed zone](https://docs.cloud.google.com/dns/docs/zones#delete_a_managed_zone).



## What's next

  * Learn more about configuring a [Direct VPC with a VPC network](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc).
  * Learn more about [Cloud Run worker pools](https://docs.cloud.google.com/run/docs/deploy-worker-pools).
  * Explore other [Cloud Run demos, tutorials, and samples](https://docs.cloud.google.com/run/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
