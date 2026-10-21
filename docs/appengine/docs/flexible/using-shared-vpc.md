---
url: https://docs.cloud.google.com/appengine/docs/flexible/using-shared-vpc/
title: Using the App Engine flexible environment on a Shared VPC network \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:10.905637+00:00
---

# Using the App Engine flexible environment on a Shared VPC network  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/using-shared-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Using the App Engine flexible environment on a Shared VPC network Stay organized with collections  Save and categorize content based on your preferences. 

In the App Engine flexible environment, you can specify a network to deploy your service's instances on. This page shows you how to configure your project to use the App Engine flexible environment on a Shared VPC network.

See [Provisioning Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc) for more information about setting up a Shared VPC network.

## Setting up the App Engine flexible environment with Shared VPC

Deploying App Engine flexible environment instances on a Shared VPC network involves three steps:

  1. Create a firewall rule to allow App Engine flexible environment traffic on the Shared VPC network

  2. Grant appropriate permissions to service accounts in the Shared VPC service project

  3. Configure your App Engine services to use the Shared VPC network




If you use the Google Cloud CLI, update to the latest version before following this guide by running the command:
    
    
    gcloud components update
    

### Allowing traffic to the Shared VPC network

A Shared VPC Admin needs to create a firewall rule in the Shared VPC host project in order to allow traffic to the App Engine flexible environment on the Shared VPC network. The firewall rule allows serving and health check traffic to flexible environment instances.

The firewall rule must have the following properties:

  * **Network** : The name of the Shared VPC network
  * **Direction of traffic** : Ingress
  * **Action on match** : Allow
  * **Targets** : Specified target tags
  * **Target tags** : `aef-instance`
  * **Source filter** : IP ranges
  * **Source IP ranges** : `35.191.0.0/16`, `130.211.0.0/22`
  * **Protocols and ports** : Specified protocols and ports 
    * **tcp** : 8443, 10402



A Shared VPC Admin can create the firewall rule using the Google Cloud console or the Google Cloud CLI:

### Console

To create the firewall rule using the Google Cloud console:

  1. Go to the firewall rule creation page.

[Create a firewall rule](https://console.cloud.google.com/networking/firewalls/add)

  2. In the **Name** and **Description** fields, provide a name and description for the firewall rule.

  3. Fill in the necessary properties as specified above.

  4. Click **Create**.




### gcloud

To create the firewall rule using the Google Cloud CLI, run the following command:
    
    
    gcloud compute firewall-rules create NETWORK_NAME-flex-firewall \
    --project HOST_PROJECT_ID \
    --network NETWORK_NAME \
    --allow tcp:10402,tcp:8443 \
    --target-tags aef-instance \
    --source-ranges 35.191.0.0/16,130.211.0.0/22 \
    --description 'Allows traffic to App Engine flexible environment'
    

where:

  * `NETWORK_NAME` is the name of the Shared VPC network.
  * `HOST_PROJECT_ID` is the Google Cloud project ID of the Shared VPC host project.



### Setting up permissions

A Shared VPC Admin must grant the following two service accounts the [Compute Network User](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) role in order to allow a service project to deploy instances in the App Engine flexible environment to the network:

  * Google APIs service agent (`PROJECT_NUM@cloudservices.gserviceaccount.com`)
  * App Engine flexible environment service agent (`service-PROJECT_NUM@gae-api-prod.google.com.iam.gserviceaccount.com`)

**Note:** App Engine creates the App Engine flexible environment service agent (`service-PROJECT_NUM@gae-api-prod.google.com.iam.gserviceaccount.com`) when you deploy your first app to the flexible environment. You can verify if the service agent exists in your project by following [these steps](https://docs.cloud.google.com/appengine/docs/flexible/service-agent#verifying_the_service_agent).

### Console

To set up permissions using the Google Cloud console:

  1. Go to the IAM Settings page for the **service project** and take note of the **Project number**.

[Go to IAM Settings](https://console.cloud.google.com/iam-admin/settings)

  2. Go to the IAM page for the **host project**.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  3. Click **Add**.

  4. In the **New members** field, enter the following email addresses separated by a comma. Replace `PROJECT_NUM` with the project number obtained in step 1.

     * `PROJECT_NUM@cloudservices.gserviceaccount.com`
     * `service-PROJECT_NUM@gae-api-prod.google.com.iam.gserviceaccount.com`
  5. In the **Select a role** dropdown, select **Compute Engine** > **Compute Network User**.

  6. Click **Save**.




### gcloud

  1. Get the project number of the service project where the App Engine app is deployed. Run the following command, replacing `SERVICE_PROJECT_ID` with the project ID of the service project:
         
         export SERVICE_PROJECT_NUM=$(gcloud projects describe SERVICE_PROJECT_ID --format="value(projectNumber)")
         

  2. Grant the service project's Google APIs Service Agent the `compute.networkUser` role in the host project:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
         --member=serviceAccount:$SERVICE_PROJECT_NUM@cloudservices.gserviceaccount.com \
         --role=roles/compute.networkUser
         

where `HOST_PROJECT_ID` is the Google Cloud project ID of the Shared VPC host project.

  3. Grant the service project's App Engine Flexible Environment Service Agent the `compute.networkUser` role in the host project:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
         --member=serviceAccount:service-$SERVICE_PROJECT_NUM@gae-api-prod.google.com.iam.gserviceaccount.com \
         --role=roles/compute.networkUser
         




### Configuring and deploying your service

After the firewall rule and proper permissions are set up, you can deploy either a new service or an existing App Engine flexible environment service to the Shared VPC network.

  1. In the `app.yaml` file, use the [network settings](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#network_settings) `name` field to specify the fully-qualified name of the Shared VPC network:
         
         network:
           name: projects/HOST_PROJECT_ID/global/networks/NETWORK_NAME
         

where

     * `HOST_PROJECT_ID` is the Google Cloud project ID of the Shared VPC host project.
     * `NETWORK_NAME` is the name of the Shared VPC network.

To configure the service to be part of a subnetwork named `SUBNETWORK_NAME`, also set the `subnetwork_name` field:
    
    network:
      name: projects/HOST_PROJECT_ID/global/networks/NETWORK_NAME
      subnetwork_name: SUBNETWORK_NAME
    

  2. Deploy the service: 
         
         gcloud app deploy
         




## Verifying your configuration

To verify that your App Engine flexible environment service is running on the Shared VPC network, view the version configuration on the App Engine versions page in the Google Cloud console:

  1. Go to the App Engine Versions page.

[Go to App Engine versions](https://console.cloud.google.com/appengine/versions)

  2. In the **Config** column on the right, click on **View** for the desired version.

  3. Verify that the network name in the configuration is the name of the Shared VPC network.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
