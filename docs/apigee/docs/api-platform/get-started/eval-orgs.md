---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/eval-orgs/
title: Provisioning an eval org \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:45.843279+00:00
---

# Provisioning an eval org  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/eval-orgs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Provisioning an eval org Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section describes how to set up an Apigee evaluation organization (or _eval org_) using the console. For more information, see [ Organization types](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure#org_types). We also support using Terraform to provision eval orgs. See [Terraform overview](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/terraform-overview).

**Tip:** We recommend you review the [ Apigee architecture](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/overview) topic before you do the provisioning steps.

**Video:** Check out this short video to learn about setting up and testing an Apigee eval org. 

## Creating an eval org with the Apigee provisioning wizard

This section describes how to use the [](https://apigee.google.com/setup)Apigee provisioning wizard to create an eval org.

### Get started

#### Permissions required for this task

The Apigee provisioner must have sufficient permission to use the wizard. To grant this permission, a Google Cloud admin can give the Apigee provisioner the predefined [ Apigee Organization Admin](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) role, or give more [ fine-grained permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#provisioning-wizard-permissions) to provide the least privilege necessary. 

* * *

  1. Ensure that you have met the [ prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites) before you continue. 
  2. Create a [ Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) if you have not done so already. 
  3. In the Google Cloud console, go to the **Set up Apigee Evaluation** page. 

[Go to Set up Apigee Evaluation](https://console.cloud.google.com/apigee/setup/eval)

  4. Select your Google Cloud project ID in the **Project picker** list. 

If you do not have permission to manage the project, or if the project does not exist, you will see an error message. Make sure the project ID you entered is correct, and that it is the project ID and not the project name, if they are different. 

If the project is already associated with a paid Apigee account, you cannot create an evaluation org for the project. See [ Provisioning > Paid orgs > Before you begin](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview) to use the console to provision a paid org. 

**Note:** The Apigee provisioning wizard keeps track of your steps for this project. As you complete each step, the **Edit** icon is displayed by the next step. Once you complete a step, you can exit the wizard. When you return, the wizard continues with the next step. 



###  Enable APIs 

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [ Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [ API enablement permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#api-enablement-permissions). 

* * *

Enable the Google Cloud APIs needed for Apigee to function. 

  1. Click **Edit** next to **Enable APIs**. If all required APIs are already enabled, the setup automatically advances to the networking step. 
  2. Click **Enable APIs** in the **Enable APIs** pane. The following APIs are enabled for your project: 
     * Apigee API
     * Compute Engine API
     * Service Networking API
  3. Wait a few moments for the step to complete. When the APIs are enabled, a check is displayed next to the **Enable APIs** step and the next step becomes available.

**Tip:** You can see the APIs enabled for your project in the [Google Cloud APIs & Services Dashboard](https://console.cloud.google.com/apis/dashboard). 



###  Networking 

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [ Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [ Service networking permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#service-networking-permissions).

* * *

Set up networking for your local Virtual Private Cloud (VPC). 

  1. Click **Edit** next to **Networking**.

  2. Select a network from the **Authorized network** drop-down list. For most eval orgs, you will select `default`, which is the network that Google Cloud created for you when you created your Google Cloud project. If you have a different Cloud network and want to use it, select it from the list. (Note that the network must have a /22 CIDR block of IP addresses free.)

If your project is using shared VPC networking, select the network that manages the network settings for your project. If you do not see that network in the dropdown list, have a user with permission to manage the network log in to complete this step. Then you can return to the wizard and continue. For more information on Shared VPC networking, see [ Using Shared VPC networks](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs). 

After you select a network the wizard displays the peering range selection options. 

Select how you want Apigee to identify IP addresses for your network. For eval organizations it is most common to select **Automatically allocate IP range**. If you prefer to specify a range, select **Select one or more existing IP ranges or create a new one**. You must specify both a name and a specific IP range, like `10.20.238.0/22`. 

Click **Allocate and connect** to continue. 

The wizard creates the network and allocates IP addresses for the services within that network. The network creation takes a couple of minutes to complete.




###  Apigee evaluation organization 

#### Permissions required for this task

You can give the Apigee provisioner predefined roles that include the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [ Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) or [ Organization creation permissions (eval org)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#organization-creation-permissions-eval-org).

* * *

Create an Apigee eval [ organization](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure). 

  1. Click **Edit** next to **Apigee evaluation organization**.

The **Create an Apigee evaluation organization** pane is displayed.

  2. Select an analytics hosting region and a runtime location. For a list of available Apigee API Analytics and runtime locations, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations). 
  3. Click **Provision**.

The Apigee provisioning wizard creates the eval org and its associated runtime instance. The eval org has the same name and ID as your project ID.

**Note:** This process can take up to 45 minutes.

When this step is done, a check is displayed next to **Apigee evaluation organization** , and the next step becomes available.




###  Access routing 

In this step, you choose whether to expose your new cluster to external requests or to keep it private (and only allow requests from within your VPC). The manner in which you access API proxies depends on whether you decide to allow external requests or restricted requests to internal only: 

Access Type | Description of the configuration and deployment process  
---|---  
External |  Allow external access to API proxies. The wizard deploys a Hello World proxy to your runtime instance for you. You can then send a request to the API proxy from your administration machine or any machine with access to the internet.   
Internal |  Allow only internal access to API proxies. The wizard deploys a Hello World proxy to your runtime instance for you. You must manually create a new VM inside your VPC and connect to it. From the new VM, you can send requests to the API proxy.  **Caution:** Because of a [limitation](https://docs.cloud.google.com/load-balancing/docs/l7-internal#limitations) on Google Cloud internal Application Load Balancer, the Apigee internal routing option does not support HTTP 1.0 requests. Incoming client requests that specify the HTTP 1.0 protocol will fail. Later HTTP versions are supported.  
  
Follow the steps under the External Access or Internal Access tab below:

### External Access

This section describes how to configure routing when you're using the Apigee provisioning wizard and you want to allow _external_ access to your API proxy.

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [ Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [ Access routing permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#access-routing-permissions). 

* * *

**To configure routing for external access in the Apigee provisioning wizard:**

  1. Open the [](https://apigee.google.com/setup)Apigee provisioning wizard if it is not currently open. The wizard returns to the most recent incomplete task in the list.
  2. Click create**Edit** next to **Access routing**.

  3. Select **Enable internet access** from the Configure access panel.

The wizard displays additional options for configuring the instance.

  4. For the domain setting, enter a valid DNS name that you own, or choose to use a wildcard DNS service, such as [nip.io](https://nip.io/). If you choose the wildcard service, a static external IP address is reserved for you. The wildcard option is easy to use, but is only recommended for testing purposes. 
  5. (Optional) You can change the virtual machine instance name to something more meaningful. As part of the provisioning process, Apigee creates a managed instance group (MIG) containing multiple VMs to proxy traffic between the load balancer and the Apigee runtime. To change the VM instance name, click **Edit** and make your changes. 
  6. Select the subnet used to host the MIG of VMs to bridge to the Apigee runtime. The subnet size can be small (e.g. /28) as it needs to host at most three VMs. The subnet can be shared and used by VMs or other entities. 
  7. If you are using a wildcard DNS service, just note that a Google-managed certificate will be created for the domain. You do not have to take further action. See also [ Using Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs). 

If you are using your own domain, select whether to supply a certificate you manage or use a [ Google-managed certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs):

     * Supply a **self-managed certificate** : 
       1. Generate a certificate/key pair if you don't already have one. For test environments, this can be a self-signed certificate. For a production system you should use a certificate signed by a Certificate Authority. See [ Using self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs). 
       2. In the respective fields, browse your file system and attach the files containing the certificate and private key. Both must be PEM-formatted. 
     * Use a **Google-managed certificate**. To use a [ Google-managed certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-types), do not enter a signed certificate or RSA private key. The Google-managed certificate will be created for you. 
  8. Click **Set access**.

Apigee prepares your cluster for external access. This includes setting up the MIG to proxy traffic, creating firewall rules, uploading certificates, and creating a load balancer. 

This process can take several minutes to complete.

  9. When Apigee finishes setting up your runtime's access, you'll notice that there is a check mark next to all steps in the wizard. 
  10. Click **Continue**.

The wizard displays **Recommended next steps**. The steps shown depend on whether you used your own DNS name or a wildcard DNS.

**Note:** DNS changes are published immediately, but may take time to propagate. Because of this delay, you may have to wait up to an hour before you can call the sample proxy.
     * If you specified your own domain name, go to your domain registrar and create an A record for your domain hostname that points to the IP address shown in the wizard. When that is done, click **Launch** to call the API proxy that was deployed for you. 
     * If you used a wildcard DNS, then just click **Launch** to call the **hello-world** API proxy that was deployed for you. 
  11. (Optional) Add users and roles for your organization. See [ Users and roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/users-roles-overview).



You have now completed the steps to configure external internet access to API proxies. 

### Internal Access

This section describes how to configure routing when you're using the Apigee provisioning wizard and you _do not_ want to allow external access to your API proxy. Instead, you want to limit access to _internal_ requests only that originate from within the VPC.

**Caution:** Because of a [ limitation](https://docs.cloud.google.com/load-balancing/docs/l7-internal#limitations) on Google Cloud internal Application Load Balancer, the Apigee internal routing option does not support HTTP 1.0 requests. Incoming client requests that specify the HTTP 1.0 protocol will fail. Later HTTP versions are supported. 

**To configure routing for internal access in the Apigee provisioning wizard:**

  1. Click **Edit** next to the Access Routing step.
  2. Select **No internet access** in the **Configure access to the 'eval-group' env group** panel. 

  3. Click **Continue**.
  4. You'll notice that there is a check mark next to all steps in the wizard. This indicates all steps were completed successfully.

  5. Click **Continue**. 
  6. To test your newly provisioned organization, follow the instructions in [ Calling an API proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies). In those steps, you will create a Virtual Machine (VM) inside your VPC from which API proxy requests can be sent to the internal load balancer (ingress), which forwards them to your Apigee runtime instance. For convenience, the provisioning wizard created and deployed a test proxy for you, called `hello-world`. 
  7. (Optional) Add users and roles for your organization. See [ Users and roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/users-roles-overview).



If you encounter errors during this part of the process, see [Troubleshooting](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/troubleshooting-install).

###  View organization details 

Finally, open the Apigee UI to view details about your organization. 

#### Permissions required for this task

If you have Apigee Org Admin role, you can complete this task. To learn about other roles you can employ for using the Apigee UI, see [ Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles). 

* * *

  1. Click **Open Apigee console** to open the Apigee UI.
  2. Make sure the project you just created is selected in the Apigee UI.

If the org you just created is not the one selected, click the project name to drop down a list of projects. 

If your project is not in the list of available projects, you may need to wait a few moments before it is available. Refresh your browser and check again. 

  3. Your org configuration can be viewed as follows:

Location | Property | Value  
---|---|---  
**Management > Instances** [Go to Instances](https://console.cloud.google.com/apigee/instances) | Name | `eval-instance`  
| IP address | This is your org's internal load balancer IP address.   
**Management > Environments > Environments** [Go to Environments](https://console.cloud.google.com/apigee/environments/overview) | Environment name | `eval`  
**Management > Environments > Environment Groups** [Go to Environment Groups](https://console.cloud.google.com/apigee/environments/groups) | Environment group | `eval-group`  
**Management > Environments > Environment Groups** [Go to Environment Groups](https://console.cloud.google.com/apigee/environments/groups) | Hostnames | `PROJECT_NAME.DOMAIN`  
  4. Apigee created an API proxy called `hello-world` for you when you provisioned the eval org. Location | Property | Value  
---|---|---  
**Proxy development > API Proxies** [Go to API Proxies](https://console.cloud.google.com/apigee/proxies) | API proxy name | `hello-world`  



## Deleting an evaluation organization

To delete (or _deprovision_) an eval organization, use the [gcloud alpha apigee organizations delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/delete) command.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[CIDR]: Classless Inter-Domain Routing
