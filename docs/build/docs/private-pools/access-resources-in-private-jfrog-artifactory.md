---
url: https://docs.cloud.google.com/build/docs/private-pools/access-resources-in-private-jfrog-artifactory/
title: Access resources in a private JFrog Artifactory with private pools \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:29.919258+00:00
---

# Access resources in a private JFrog Artifactory with private pools  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/private-pools/access-resources-in-private-jfrog-artifactory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Access resources in a private JFrog Artifactory with private pools Stay organized with collections  Save and categorize content based on your preferences. 

This page demonstrates how to use Cloud Build [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) to access resources from a private Virtual Private Cloud network.

In this tutorial, you will create a [JFrog Artifactory](https://jfrog.com/artifactory/) in Compute Engine hosted in a private VPC network, and then configure a build running in a private pool to access data from that Artifactory. The Jfrog Artifactory is an open-source binary repository manager.

## Objectives

  * Set up a Jfrog Artifactory on Compute Engine
  * Upload a file to the Artifactory
  * Create a private pool
  * Peer the service producer network that hosts the private pool to the Artifactory's Virtual Private Cloud network
  * Write a [build configuration file](https://docs.cloud.google.com/build/docs/build-config-file-schema) to access the data in Artifactory



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Compute Engine
  * Cloud Build



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

  4. Enable the Compute Engine, Cloud Build, Service Networking APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,cloudbuild.googleapis.com,servicenetworking.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine, Cloud Build, Service Networking APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,cloudbuild.googleapis.com,servicenetworking.googleapis.com)




### Option A: Use Cloud Shell

You can follow this tutorial using [Cloud Shell](https://docs.cloud.google.com/shell), which comes preinstalled with the Google Cloud CLI used in this tutorial. If you use Cloud Shell, you don't need to install these command-line tools on your workstation.

To use Cloud Shell:

  1. Go to the [Google Cloud console](https://console.cloud.google.com/). 

[ Google Cloud console](https://console.cloud.google.com/)

  2. Click the **Activate Cloud Shell** ![Activate Shell Button](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png) button at the top of the Google Cloud console window.

A Cloud Shell session opens inside a new frame at the bottom of the Google Cloud console and displays a command-line prompt.

![Cloud Shell session](https://docs.cloud.google.com/static/shell/docs/images/new-console.png)




### Option B: Use command-line tools locally

If you prefer to follow this tutorial on your workstation, follow these steps to install the necessary tools.

**Note:** If you are using an existing environment where `gcloud` has already been installed, make sure `gcloud` is [initialized with your user account](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the).

  1. [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

**Note:** If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.



## Create the private Artifactory

  1. Create a Compute Engine instance from a container:
         
         gcloud compute instances create-with-container jfrog \
         --container-image docker.bintray.io/jfrog/artifactory-jcr:latest \
         --zone us-central1-a
         

  2. SSH into the instance. The container may take a couple of minutes to initialize.
         
         gcloud compute ssh --zone us-central1-a jfrog
         

  3. Test the connection by running the following command. Once the container is ready, it will respond with a `200` HTTP code, followed by an HTML page.
         
         curl -i http://localhost:8081
         

  4. To create a repository in the Artifactory, you must sign the JFrog EULA (End User License Agreement):
         
         curl -XPOST -vu admin:password http://localhost:8081/artifactory/ui/jcr/eula/accept
         

You will see an output similar to the following:
         
         *   Trying 127.0.0.1:8081...
             * Connected to localhost (127.0.0.1) port 8081 (#0)
             * Server auth using Basic with user 'admin'
             > POST /artifactory/ui/jcr/eula/accept HTTP/1.1
             > Host: localhost:8081
             > Authorization: Basic ….
             > User-Agent: curl/7.74.0
             > Accept: */*
             >
             * Mark bundle as not supporting multiuse
             < HTTP/1.1 200 OK
             < X-JFrog-Version: Artifactory/7.19.9 71909900
             < X-Artifactory-Id: ….
             < X-Artifactory-Node-Id: jfrog2
             < SessionValid: false
             < Content-Length: 0
             < Date: Fri, 25 Jun 2021 19:08:10 GMT
         
             * Connection #0 to host localhost left intact
         




## Upload a file to the Artifactory

  1. Create a txt file to upload to the Artifactory:
         
         echo "Hello world" >> helloworld.txt
         

  2. JFrog comes with a default example repository. Upload to the repository using the default credentials:
         
         curl -u admin:password -X PUT \
         "http://localhost:8081/artifactory/example-repo-local/helloworld.txt" \
         -T helloworld.txt
         

This should return:
         
         {
             "repo" : "example-repo-local",
             "path" : "/helloworld.txt",
             "created" : "2021-06-25T19:08:24.176Z",
             "createdBy" : "admin",
             "downloadUri" : "http://localhost:8081/artifactory/example-repo-local/helloworld.txt",
             "mimeType" : "text/plain",
             "size" : "12",
             "checksums" : {
               "sha1" : "...",
               "md5" : "...",
               "sha256" : "..."
             },
             "originalChecksums" : {
               "sha256" : "..."
             },
             "uri" : "http://localhost:8081/artifactory/example-repo-local/helloworld.txt"
             }
         

  3. End the SSH session by typing `exit`.

  4. Remove the external IP address, so the Artifactory will only be accessible from private internal sources.
         
         gcloud compute instances delete-access-config --zone us-central1-a jfrog
         




## Try accessing the data from the Artifactory

  1. Set environment variables to store your project ID and project number:
         
         PROJECT_ID=$(gcloud config list --format='value(core.project)')
         PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
         

  2. Grant the **Compute Engine Viewer** role to the service account you are using for the build to be able to view the internal IP address for your JFrog instance:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member=serviceAccount:SERVICE_ACCOUNT \
             --role=roles/compute.viewer
         

Where SERVICE_ACCOUNT is the service account email.

  3. Create a file named `cloudbuild.yaml` containing the following code to read from the Artifactory. This is the build configuration file.

The first step fetches the internal IP address from the Artifactory you created. The second step sends a request to that address to read the `helloworld.txt` file you created. The steps are separated to make it easier to isolate permissions and networking errors. If the first step fails, this is due to a permissions error and you will need to ensure that the build service account has access to the Compute Engine resources, as shown in the previous step. If the second step fails, this is due to a networking error. The rest of this tutorial addresses the network configurations.
         
         steps:
           - id: Get Private Artifactory Address
             name: gcr.io/cloud-builders/gcloud
             entrypoint: /bin/bash
             args: 
               - -c
               - |
                 gcloud compute instances describe jfrog \
                 --zone us-central1-a \
                 --format="value(networkInterfaces.networkIP)" >> _INTERNAL_IP_ADDRESS
         
           - id: Pull from Private Artifactory
             name: gcr.io/cloud-builders/curl
             entrypoint: /bin/bash
             args:
               - -c
               - |
                 curl -u admin:password --connect-timeout 10.00 \
                 http://$(cat _INTERNAL_IP_ADDRESS):8081/artifactory/example-repo-local/helloworld.txt

  4. Start a build using the build config file.

By default, when you run a build on Cloud Build, the build runs in a secure, hosted environment with access to the public internet. Each build runs on its own worker and is isolated from other workloads. The default pool has limits on how much you can customize the environment, particularly around private network access. In this example, you are trying to access a private network from a public worker.

Run the `cloudbuild.yaml` with the following command. It should fail.
         
         gcloud builds submit --no-source
         

The output will look something like:
         
         BUILD
         Starting Step #0 - "Get Private Artifactory Address"
         Step #0 - "Get Private Artifactory Address": Already have image (with digest): gcr.io/cloud-builders/gcloud
         Finished Step #0 - "Get Private Artifactory Address"
         Starting Step #1 - "Pull from Private Artifactory"
         Step #1 - "Pull from Private Artifactory": Already have image (with digest): gcr.io/cloud-builders/curl
         Step #1 - "Pull from Private Artifactory":   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
         Step #1 - "Pull from Private Artifactory":                                  Dload  Upload   Total   Spent    Left  Speed
           0     0    0     0    0     0      0      0 --:--:--  0:02:09 --:--:--     0curl: (7) Failed to connect to 10.128.0.2 port 8081: Connection timed out
         Finished Step #1 - "Pull from Private Artifactory"
         ERROR
         ERROR: build step 1 "gcr.io/cloud-builders/curl" failed: step exited with non-zero status: 7
         

You can see by the connection timeout that Cloud Build is not able to reach the internal IP address. In order to access this private resource, you must use Cloud Build Private Pools.




## Create a private connection between the Artifactory's VPC network and the service producer network

  1. First, ensure your VPC network allows ingress. Create a [firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls) to allow inbound internal traffic to the network with the `jfrog` instance. The range `10.0.0.0/16` is in a [private address space](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges), which you will use for the Cloud Build private pools in the steps below.
         
         gcloud compute firewall-rules create allow-private-pools --direction=INGRESS \
         --priority=1000 --network=default --action=ALLOW --rules=all --source-ranges=10.0.0.0/16
         

  2. Create a reserved range for the Cloud Build private pool to utilize for the workers. The reserved range must be in the network where your Artifactory is located. In this case, it is the `default` compute network.

You have two options when you set your reserved ranges. You can either specify the range explicitly by providing `--addresses` and `--prefix-length`, or you can allow Google Cloud to provision an available range based on a provided `prefix-length`.

In the example below, you explicitly set the addresses to match the firewall rule you created. The private pool will use this address space and the inbound traffic will not be blocked.
         
         gcloud compute addresses create jfrog-ranges --global --purpose=VPC_PEERING \
         --addresses=10.0.0.0 --prefix-length=16 --network=default
         

  3. Peer the VPC network with the Service Networking API.

Cloud Build private pools run workers using the Service Networking API. This enables you to offer your managed services on internal IP addresses. This is achieved by peering the Google-managed VPC running the Cloud Build private pool workers with your own VPC. This may take a few minutes to complete.
         
         gcloud services vpc-peerings connect --service=servicenetworking.googleapis.com \
         --ranges=jfrog-ranges --network=default
         




## Create the private pool

  1. The `default` VPC network is now ready for use with Cloud Build private pools. Create the private pool and peer it with the VPC network.
         
         gcloud builds worker-pools create jfrog-pool --region us-central1 \
          --peered-network=projects/${PROJECT_ID}/global/networks/default
         

  2. To run your build with the new private pool, you can either pass in the `--worker-pool` flag with the `gcloud` command or update your `cloudbuild.yaml` config to ensure it always uses the private pool. For this tutorial, update the `cloudbuild.yaml` by adding the following option:
         
         options:
           pool:
             name: 'projects/${PROJECT_ID}/locations/us-central1/workerPools/jfrog-pool'

  3. The complete file will look like the following:
         
         steps:
           - id: Get Private Artifactory Address
             name: gcr.io/cloud-builders/gcloud
             entrypoint: /bin/bash
             args: 
               - -c
               - |
                 gcloud compute instances describe jfrog \
                 --zone us-central1-a \
                 --format="value(networkInterfaces.networkIP)" >> _INTERNAL_IP_ADDRESS
         
           - id: Pull from Private Artifactory
             name: gcr.io/cloud-builders/curl
             entrypoint: /bin/bash
             args:
               - -c
               - |
                 curl -u admin:password --connect-timeout 10.00 \
                 http://$(cat _INTERNAL_IP_ADDRESS):8081/artifactory/example-repo-local/helloworld.txt
         
         options:
           pool:
             name: 'projects/${PROJECT_ID}/locations/us-central1/workerPools/jfrog-pool'

  4. Start the build:
         
         gcloud builds submit --no-source
         

  5. The build will use the new private pool, peered with the VPC network, allowing it to access the internal IP address of the Artifactory. The output will be successful and `Step #1` should print "Hello world".




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

If you created a new project for this tutorial, delete the project. If you used an existing project and wish to keep it without the changes added in this tutorial, delete resources created for the tutorial.

### Deleting the project

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



### Deleting tutorial resources

  1. Delete the Compute Engine service you deployed in this tutorial:
         
         gcloud compute instances delete jfrog
         

  2. Delete the firewall rule:
         
         gcloud compute firewall-rules delete allow-private-pools --network=default
         

  3. Remove the reserved range:
         
         gcloud compute addresses delete jfrog-ranges --global
         

  4. Delete the Cloud Build private pool:
         
         gcloud builds worker-pools delete jfrog-pool
         




## What's next

  * Learn how to configure commonly-used [private network setups with private pools](https://cloud.google.com/build/docs/private-pools/use-in-private-network)
  * Learn how to use [VPC service controls with private pools](https://cloud.google.com/build/docs/private-pools/using-vpc-service-controls)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
