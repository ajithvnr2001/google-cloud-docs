---
url: https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds/
title: Configure Workload Identity Federation with AWS or Azure VMs \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:35.283375+00:00
---

# Configure Workload Identity Federation with AWS or Azure VMs  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure Workload Identity Federation with AWS or Azure VMs Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to use Workload Identity Federation to let AWS and Azure VM workloads authenticate to Google Cloud without a service account key.

If you use Amazon Elastic Kubernetes Service (Amazon EKS) or Azure Kubernetes Service (AKS), see [Configure Workload Identity Federation with Kubernetes](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes) to learn how to configure Workload Identity Federation for your clusters. This page covers only configuring Workload Identity Federation for AWS and Azure VMs.

By using Workload Identity Federation, workloads that run on AWS EC2 and Azure VMs can exchange their environment-specific credentials for short-lived Google Cloud Security Token Service tokens.

Environment-specific credentials include the following:

  * AWS EC2 instances can use instance profiles to request [temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html).
  * Azure VMs can use [managed identities](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview) to obtain Azure access tokens.



By setting up Workload Identity Federation, you can let these workloads exchange these environment-specific credentials against short-lived Google Cloud credentials. Workloads can use these short-lived credentials to access Google Cloud APIs.

## Before you begin

  * Set up authentication.

**Important:** New Amazon EC2 instances use [IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html). If your instance uses IMDSv2, you must follow the gcloud CLI instructions instead of the Google Cloud console instructions. To learn more, see [Amazon EC2 Instance Metadata Service (IMDSv2) by default](https://aws.amazon.com/blogs/aws/amazon-ec2-instance-metadata-service-imdsv2-by-default/).

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 




## Prepare your external identity provider

You only need to perform these steps once for each Microsoft Entra ID tenant or AWS account.

###  AWS 

Google Cloud supports two mechanisms for federating with AWS workloads:

  * **AWS outbound identity federation** : AWS acts as an OpenID Connect (OIDC) identity provider (IdP) and issues short-lived JSON Web Tokens (JWTs) to your workloads.

    * If you're using AWS outbound identity federation, to set up Workload Identity Federation, first follow the instructions in the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_getting_started.html) to configure permissions and obtain your account's OIDC issuer URL. Then, follow the instructions in [Configure Workload Identity Federation with other providers (OIDC)](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers) to set up your pool, provider, and credential configuration.
  * **AWS IAM Credentials** : Your workloads use AWS temporary security credentials (IAM roles or instance profiles), and Google Cloud verifies them using the AWS `GetCallerIdentity` API. You don't need to make any configuration changes in your AWS account for this option.




The remainder of this page describes how to configure federation using the **AWS IAM Credentials** mechanism.

After you configure a workload identity pool to trust your AWS account, you can let [AWS users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users) and [AWS roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles) use permanent or temporary AWS security credentials to obtain short-lived Google Cloud credentials.

###  Azure 

You must create a new [Microsoft Entra ID application](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals#application-object) in your Microsoft Entra ID tenant and configure it so that it can be used for Workload Identity Federation.

After you configure a workload identity pool to trust the application, Azure users and service principals can request access tokens for this application and exchange these access tokens against short-lived Google Cloud credentials.

To create the application, do the following:

  1. [Create a Microsoft Entra ID application and service principal](https://docs.microsoft.com/en-au/azure/active-directory/develop/howto-create-service-principal-portal#register-an-application-with-azure-ad-and-create-a-service-principal).

  2. Set an **Application ID URI** for the application. You can use the default Application ID URI (`APPID`) or specify a custom URI.

You need the Application ID URI later when you configure the workload identity pool provider.




To let an application obtain access tokens for the Microsoft Entra ID application, you can use [managed identities](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview):

  1. [Create a managed identity](https://docs.microsoft.com/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-portal). Note the Object ID of the managed identity. You need it later when you configure impersonation.

  2. [Assign the managed identity](https://docs.microsoft.com/azure/active-directory/managed-identities-azure-resources/qs-configure-portal-windows-vm#user-assigned-managed-identity) to a virtual machine or another resource that runs your application.


**Note:** If you use Azure's default settings, the new application grants all users in the Microsoft Entra ID tenant permission to obtain access tokens. Use [app role assignments](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-assign-app-role-managed-identity-powershell#assign-a-managed-identity-access-to-another-applications-app-role) to restrict which identities can obtain access tokens for the application.

## Configure Workload Identity Federation

You only need to perform these steps once per AWS account or Microsoft Entra ID tenant. You can then use the same workload identity pool and provider for multiple workloads and across multiple Google Cloud projects.

To start configuring Workload Identity Federation, do the following:

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

It's best to [ use a dedicated project to manage workload identity pools and providers](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#dedicated-project). 
  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the IAM, Resource Manager, Service Account Credentials, and Security Token Service APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,cloudresourcemanager.googleapis.com,iamcredentials.googleapis.com,sts.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Define an attribute mapping and condition

The environment-specific credentials of your AWS or Azure workload contain multiple attributes, and you must decide which attribute you want to use as subject identifier (`google.subject`) in Google Cloud.

Google Cloud uses the subject identifier in Cloud Audit Logs and in [principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers) to uniquely identify an AWS or Azure user or role.

Optionally, you can [map additional attributes](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping). You can then refer to these additional attributes when granting access to resources.

###  AWS 

Your attribute mapping can use the [response fields for `GetCallerIdentity`](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html) as source attributes. These fields include the following:

  * `account`: the AWS account number.
  * `arn`: the AWS ARN of the external entity.
  * `userid`: the unique identifier of the calling entity.



If your application runs on an [Amazon Elastic Compute Cloud (EC2) instance with an attached role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html), you can use the following attribute mapping:
    
    
    google.subject=assertion.arn
    attribute.account=assertion.account
    attribute.aws_role=assertion.arn.extract('assumed-role/{role_name}/')
    attribute.aws_ec2_instance=assertion.arn.extract('assumed-role/{role_and_session}').extract('/{session}')
    

The mapping does the following:

  * Uses the ARN as subject identifier—for example: `"arn:aws:sts::000000000000:assumed-role/ec2-my-role/i-00000000000000000`
  * Introduces a custom attribute `account` and assigns it the AWS account ID
  * Introduces a custom attribute `aws_role` and assigns it the AWS role name—for example: `ec2-my-role`
  * Introduces a custom attribute `aws_ec2_instance` and assigns it the EC2 instance ID—for example: `i-00000000000000000`



Using this mapping, you can grant access to:

  * A specific EC2 instance: 
        
        principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.aws_ec2_instance/EC2_INSTANCE_ID
        

  * All users and instances in a role: 
        
        principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.aws_role/ROLE_NAME
        




###  Azure 

Your attribute mappings can use the [claims embedded in Azure access tokens](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens#claims-in-access-tokens), including custom claims, as source attributes. In most cases, it's best to use the `sub` claim as subject identifier:
    
    
    google.subject=assertion.sub
    

When the `sub` claim surpasses the 127-character limit for `google.subject`, we recommend that you use the [`extract` function](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#extract) to derive a subject identifier—for example:
    
    
    google.subject=assertion.sub.extract('/eid1/c/pub/t/{sub_claim}')
    

For an access token issued to a [managed identity](https://docs.microsoft.com/azure/active-directory/managed-identities-azure-resources/qs-configure-portal-windows-vm#user-assigned-managed-identity), the `sub` claim contains the Object ID of the managed identity. If you use a different claim, make sure that the claim is unique and can't be reassigned.

If you're unsure about the list of claims you can reference, do the following:

  1. Connect to an Azure VM that has an assigned managed identity.

  2. Obtain an access token from the [Azure Instance Metadata Service (IMDS)](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-use-vm-token#get-a-token-using-http):

#### Bash
         
         curl \
           "http://169.254.169.254/metadata/identity/oauth2/token?resource=APP_ID_URI&api-version=2018-02-01" \
           -H "Metadata: true" | jq -r .access_token
         

This command uses the [`jq` tool](https://stedolan.github.io/jq/). `jq` is available by default in Cloud Shell.

#### PowerShell
         
         $SubjectTokenType = "urn:ietf:params:oauth:token-type:jwt"
         $SubjectToken = (Invoke-RestMethod `
           -Uri "http://169.254.169.254/metadata/identity/oauth2/token?resource=APP_ID_URI&api-version=2018-02-01" `
           -Headers @{Metadata="true"}).access_token
         Write-Host $SubjectToken
         

Replace `APP_ID_URI` with the **Application ID URI** of the application that you've configured for Workload Identity Federation.

  3. In a web browser, go to [`https://jwt.ms/`](https://jwt.ms/) and paste the access token into the field.

  4. Click **Claims** to view the list of claims embedded in the access token.




For service identities, it's typically not necessary to create a mapping for `google.groups` or any custom attributes.

Optionally, define an [attribute condition](https://docs.cloud.google.com/iam/docs/workload-identity-federation#conditions). Attribute conditions are CEL expressions that can check assertion attributes and target attributes. If the attribute condition evaluates to `true` for a given credential, the credential is accepted. Otherwise, the credential is rejected.

###  AWS 

You can use an attribute condition to restrict which IAM users and roles can use Workload Identity Federation to obtain short-lived Google Cloud tokens.

For example, the following condition restricts access to AWS roles and disallows [other IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html):
    
    
    assertion.arn.startsWith('arn:aws:sts::AWS_ACCOUNT_ID:assumed-role/')
    

###  Azure 

You can use an attribute condition to restrict which users and service principals can use Workload Identity Federation to obtain short-lived Google Cloud tokens. Alternatively, you can configure your Microsoft Entra ID application to use [app role assignments](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-assign-app-role-managed-identity-powershell#assign-a-managed-identity-access-to-another-applications-app-role).

### Create the workload identity pool and provider

#### Required roles

To get the permissions that you need to configure Workload Identity Federation, ask your administrator to grant you the following IAM roles on the project: 

  * [Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Alternatively, the IAM Owner (`roles/owner`) basic role also includes permissions to configure identity federation. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

You now have collected all of the information that you need to create a workload identity pool and provider:

###  Console 

  1. In the Google Cloud console, go to the **New workload provider and pool** page.

[Go to New workload provider and pool](https://console.cloud.google.com/iam-admin/workload-identity-pools/create)

  2. In the **Create an identity pool** section, enter the following:

     * **Name** : Name for the pool. The name is also used as the pool ID. You can't change the pool ID later.
     * **Description** : Text that describes the purpose of the pool.
  3. Click **Continue**.

  4. Configure provider settings:

###  AWS 

Configure the following provider settings:

     * **Select a provider** : **AWS**.
     * **Provider name** : the name for the provider. The name is also used as the provider ID. You cannot change the provider ID later.

###  Azure 

Configure the following provider settings:

     * **Select a provider** : **OpenID Connect (OIDC)**.
     * **Provider name** : Name for the provider. The name is also used as the provider ID. You cannot change the provider ID later.
     * **Issuer URL** : `https://sts.windows.net/TENANT_ID`. Replace `TENANT_ID` with the [tenant ID](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id) (GUID) of your Microsoft Entra ID tenant.
     * **Allowed audiences** : **Application ID URI** that you used when you registered the application in Microsoft Entra ID.

  5. Click **Continue**.

  6. In the **Configure provider attributes** section, add the attribute mappings that you've identified previously.

  7. In the **Attribute conditions** section, enter the attribute condition that you identified previously. Leave the field blank if you don't have an attribute condition.

  8. Click **Save** to create the workload identity pool and provider.




###  gcloud 

  1. Create a new workload identity pool:
         
         gcloud iam workload-identity-pools create POOL_ID \
             --location="global" \
             --description="DESCRIPTION" \
             --display-name="DISPLAY_NAME"
         

Replace the following:

     * `POOL_ID`: the unique ID for the pool.
     * `DISPLAY_NAME`: the name of the pool.
     * `DESCRIPTION`: the description of the pool. This description appears when granting access to pool identities.
  2. Add a workload identity pool provider:

###  AWS 

To create the workload identity pool provider for AWS, execute the following command:
         
         gcloud iam workload-identity-pools providers create-aws PROVIDER_ID \
           --location="global" \
           --workload-identity-pool="POOL_ID" \
           --account-id="ACCOUNT_ID" \
           --attribute-mapping="MAPPINGS" \
           --attribute-condition="CONDITIONS"
         

Replace the following:

     * `PROVIDER_ID`: the unique ID for the provider.
     * `POOL_ID`: the ID of the pool.
     * `ACCOUNT_ID`: the 12-digit number [that identifies your AWS account](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html).
     * `MAPPINGS`: Comma-separated list of attribute mappings that you've identified previously.
     * `CONDITIONS`: Attribute condition that you've identified previously. Remove the parameter if you don't have an attribute condition.

Example:
    
    gcloud iam workload-identity-pools providers create-aws example-provider \
      --location="global" \
      --workload-identity-pool="pool-1" \
      --account-id="123456789000" \
      --attribute-mapping="google.subject=assertion.arn"

###  Azure 

To create the workload identity pool provider for Azure, execute the following command:
    
    gcloud iam workload-identity-pools providers create-oidc PROVIDER_ID \
        --location="global" \
        --workload-identity-pool="POOL_ID" \
        --issuer-uri="ISSUER_URI" \
        --allowed-audiences="APPLICATION_ID_URI" \
        --attribute-mapping="MAPPINGS" \
        --attribute-condition="CONDITIONS"
    

Replace the following:

     * `PROVIDER_ID`: The unique ID for the provider.
     * `POOL_ID`: The ID of the pool.
     * `ISSUER_URI`: The [tenant ID](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id) (GUID) of your Microsoft Entra ID tenant, sometimes formatted as `https://sts.windows.net/TENANT_ID`. The issuer URI can vary, and to find your issuer URI, you can debug your JWT using [JWT.io](http://jwt.io).
     * `APPLICATION_ID_URI`: **Application ID URI** that you used when you registered the application in Microsoft Entra ID.
     * `MAPPINGS`: The comma-separated list of attribute mappings that you previously identified.
     * `CONDITIONS`: (Optional) The attribute condition that you previously identified.

Example:
    
    gcloud iam workload-identity-pools providers create-oidc example-provider \
        --location="global" \
        --workload-identity-pool="pool-1" \
        --issuer-uri="https://sts.windows.net/00000000-1111-2222-3333-444444444444" \
        --allowed-audiences="api://my-app" \
        --attribute-mapping="google.subject=assertion.sub,google.groups=assertion.groups"




**Note:** The prefix `gcp-` is reserved and can't be used in a pool or provider ID.

## Authenticate a workload

You must perform these steps once per workload.

### Allow your external workload to access Google Cloud resources

To provide your workload with access to Google Cloud resources, we recommend that you grant direct resource access to the principal. In this case, the principal is the federated user. Some Google Cloud products have [Google Cloud API limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services). If your workload calls an API endpoint that has a limitation, you can instead use service account impersonation. In this case, the principal is the Google Cloud service account, which acts as the identity. You grant access to the service account on the resource.

### Direct resource access

You can grant access to a federated identity directly on resources by using the Google Cloud console or the gcloud CLI.

### Console

To use the Google Cloud console to grant IAM roles directly on a resource, you must go to the resource's page, and then grant the role. The following example shows you how to go to the Cloud Storage page and grant the role Storage Object Viewer (`roles/storage.objectViewer`) to a federated identity directly on a Cloud Storage bucket.

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to grant the role.

  3. Select the **Permissions** tab near the top of the page.

  4. Click the _add_box_ **Grant access** button.

The **Add principals** dialog appears.

  5. In the **New principals** field, enter one or more identities that need access to your bucket.

###  By subject 
         
         principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT
         

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `POOL_ID`: the workload pool ID
     * `SUBJECT`: the individual subject mapped from your IdP—for example, `administrator@example.com`

###  By group 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP
    

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `WORKLOAD_POOL_ID`: the workload pool ID
     * `GROUP`: the group mapped from your IdP—for example: `administrator-group@example.com`

###  By attribute 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE
    

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `WORKLOAD_POOL_ID`: the workload pool ID
     * `ATTRIBUTE_NAME`: one of the attributes that was mapped from your IdP
     * `ATTRIBUTE_VALUE`: the value of the attribute

  6. Select a role (or roles) from the **Select a role** drop-down menu. The roles you select appear in the pane with a short description of the permissions they grant.

  7. Click **Save**.




###  gcloud 

To use the gcloud CLI to grant IAM roles on a resource in a project, do the following:

  1. Obtain the project number of the project in which the resource is defined.
         
         gcloud projects describe $(gcloud config get-value core/project) --format=value\(projectNumber\)
         

  2. Grant access to the resource.

To use the gcloud CLI to grant the role Storage Object Viewer (`roles/storage.objectViewer`) to external identities that meet certain criteria, run the following command. 

### By subject
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT"

### By group
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP"

### By attribute
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE"

Replace the following:

     * `BUCKET_ID`: the bucket on which to grant access
     * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). of the project that contains the workload identity pool
     * `POOL_ID`: the pool ID of the workload identity pool
     * `SUBJECT`: the expected value for the attribute that you've mapped to `google.subject`
     * `GROUP`: the expected value for the attribute that you've mapped to `google.groups`
     * `ATTRIBUTE_NAME`: the name of a custom attribute in your attribute mapping
     * `ATTRIBUTE_VALUE`: the value of the custom attribute in your attribute mapping

You can grant roles on any Google Cloud resource that supports IAM allow policies.

**Note:** You must use the project number, not the project ID, in the member identifier.



### Service account impersonation

  1. To create a service account for the external workload, do the following:

     1. Enable the IAM, Security Token Service, and Service Account Credentials APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,sts.googleapis.com,iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)

     2. [Create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that represents the workload. We recommend that you [use a dedicated service account for each workload](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#use-dedicated-service-accounts). The service account doesn't need to be in the same project as the workload identity pool, but you must refer to the project that contains the service account.

     3. [Grant the service account access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to resources that you want external identities to access.

  2. To let the federated identity impersonate the service account, do the following:




### Console

To use the Google Cloud console to grant IAM roles to a federated identity with service account, do the following:

### Service Account in the same project

  1. To grant access using service account impersonation for a service account in the same project, do the following:

     1. Go to the **Workload Identity Pools** page.

[Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools)

     2. Select **Grant access**.

     3. In the **Grant access to service account** dialog, select **Grant access using Service Account impersonation**.

     4. In the **Service accounts** list, select the service account for the external identities to impersonate, and do the following:

     5. To choose which identities in the pool can impersonate the service account, perform one of the following actions:

        * To allow only specific identities of the workload identity pool to impersonate the service account, select **Only identities matching the filter**.

        * In the **Attribute name** list, select the attribute that you want to filter on.

        * In the **Attribute value** field, enter the expected value of the attribute; for example, if you use an attribute mapping `google.subject=assertion.sub`, set **Attribute** name to `subject` and **Attribute value** to the value of the `sub` claim in tokens that are issued by your external identity provider.

     6. To save the configuration, click **Save** and then **Dismiss**.




### Service account in a different project

**Note:** Service accounts from different projects won't appear in the "CONNECTED SERVICE ACCOUNTS" section of your **Workload Identity Pool**.

  1. To grant access using service account impersonation for a service account in a different project, do the following:

     1. Go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select the service account that you want to impersonate.

     3. Click **Manage access**.

     4. Click **Add principal**.

     5. In the **New principal** field, enter one of the following [principal identifiers](https://docs.cloud.google.com/iam/docs/workload-identity-federation#principal-types) for the identities in your pool that will impersonate the service account.

###  By subject 
            
            principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT
            

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `POOL_ID`: the workload pool ID
        * `SUBJECT`: the individual subject mapped from your IdP—for example, `administrator@example.com`

###  By group 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID
        * `GROUP`: the group mapped from your IdP—for example: `administrator-group@example.com`

###  By attribute 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID
        * `ATTRIBUTE_NAME`: one of the attributes that was mapped from your IdP
        * `ATTRIBUTE_VALUE`: the value of the attribute

### By pool
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID

     6. In **Select a role** , select the Workload Identity User role (`roles/iam.workloadIdentityUser`).

     7. To save the configuration, click **Save**.




### gcloud

To grant the Workload Identity User role (`roles/iam.workloadIdentityUser`) to a federated principal or principal set, run the following command. To learn more about Workload Identity Federation principal identifiers, see [Principal types](https://docs.cloud.google.com/iam/docs/workload-identity-federation#principal-types). 

### By subject
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT"

### By group
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP"

### By attribute
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE"

Replace the following:

  * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account
  * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). of the project that contains the workload identity pool
  * `POOL_ID`: the pool ID of the workload identity pool
  * `SUBJECT`: the expected value for the attribute that you've mapped to `google.subject`
  * `GROUP`: the expected value for the attribute that you've mapped to `google.groups`
  * `ATTRIBUTE_NAME`: the name of a custom attribute in your attribute mapping
  * `ATTRIBUTE_VALUE`: the value of the custom attribute in your attribute mapping

**Note:** You must use the project number, not the project ID, in the member identifier.

### Download or create a credential configuration

The [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries), the gcloud CLI, and Terraform, can automatically obtain external credentials, and use these credentials to impersonate a service account. To let libraries and tools complete this process, you have to provide a credential configuration file. This file defines the following:

  * Where to obtain external credentials from
  * Which workload identity pool and provider to use
  * Which service account to impersonate

**Note:** Unlike a [service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys), a credential configuration file doesn't contain a private key and doesn't need to be kept confidential. Details about the credential configuration file are available at <https://google.aip.dev/auth/4117>.

To create a credential configuration file, do the following:

###  Console 

To download a credential configuration file in the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Workload Identity Pools** page.

[Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools)

  2. Find the workload identity pool for the IdP that you want to use and click it.

  3. If you chose to use direct resource access, do the following:

     1. Click **Grant access**.

     2. Select **Grant access using federated identities (Recommended)**.

     3. Click **Download**.

     4. Continue with instructions to **Configure your application** dialog, later in this procedure.

  4. If you chose to use service account impersonation, do the following:

     1. Select **Connected service accounts**.

     2. Find the service account you want to use and click file_download **Download**.

     3. Continue with instructions to **Configure your application** dialog, later in this procedure.

  5. In the **Configure your application** dialog, select the provider that contains the external identities.

  6. Provide the following additional settings:

###  AWS 

No additional settings required.

###  Azure 

**Application ID URL** : Application ID URI of the Azure application

  7. Select file_download **Download config** to download the credential configuration file, then click **Dismiss**.




If you want to use the Security Token Service regional endpoints—for example, `https://sts.us-central1.rep.googleapis.com`, refer to [Using regional Security Token Service endpoints for better reliability](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#sts-regional-endpoints).

###  gcloud 

To create a credential configuration file by using [`gcloud iam workload-identity-pools create-cred-config`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create-cred-config), do the following:

###  AWS 

To create a credential configuration file that lets the library obtain an access token from EC2 instance metadata, do the following:
    
    
    gcloud iam workload-identity-pools create-cred-config \
        projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID \
        --service-account=SERVICE_ACCOUNT_EMAIL \
        --service-account-token-lifetime-seconds=SERVICE_ACCOUNT_TOKEN_LIFETIME \
        --aws \
        --sts-location=REGION \
        --output-file=FILEPATH.json
    

Replace the following:

  * `PROJECT_NUMBER`: The project number of the project that contains the workload identity pool
  * `POOL_ID`: The ID of the workload identity pool.
  * `PROVIDER_ID`: The ID of the workload identity pool provider.
  * `SERVICE_ACCOUNT_EMAIL`: If you use service account impersonation, replace with the email address of the service account. Omit this flag if you don't use service account impersonation.
  * `SERVICE_ACCOUNT_TOKEN_LIFETIME`: If you use service account impersonation, replace with the lifetime of the service account access token, in seconds; this defaults to one hour when not provided. Omit this flag if you don't use service account impersonation. To specify a lifetime longer than one hour, you must configure the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` [organizational policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).
  * `FILEPATH`: The file to save configuration to.
  * `REGION`: Optional. Specify the region of the [regional Security Token Service endpoints](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#sts-regional-endpoints), if they are available.



If you use [AWS IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html), an additional flag `--enable-imdsv2` needs to be added to the [`gcloud iam workload-identity-pools create-cred-config`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create-cred-config) command:
    
    
    gcloud iam workload-identity-pools create-cred-config \
        projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID \
        --service-account=SERVICE_ACCOUNT_EMAIL \
        --aws \
        --enable-imdsv2 \
        --sts-location=REGION \
        --output-file=FILEPATH.json
    

If using the AWS metadata server isn't an option, you can provide AWS security credentials through the following AWS environment variables:

  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * Either of `AWS_REGION` or `AWS_DEFAULT_REGION`
  * Optional: `AWS_SESSION_TOKEN`



The gcloud CLI and libraries use these AWS environment variables when the AWS metadata server is unavailable.

###  Azure 

Create a credential configuration file that lets the library obtain an access token from the Azure Instance Metadata Service (IMDS):
    
    
    gcloud iam workload-identity-pools create-cred-config \
        projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID \
        --service-account=SERVICE_ACCOUNT_EMAIL \
        --service-account-token-lifetime-seconds=SERVICE_ACCOUNT_TOKEN_LIFETIME \
        --azure \
        --app-id-uri APPLICATION_ID_URI \
        --sts-location=REGION \
        --output-file=FILEPATH.json
    

Replace the following:

  * `PROJECT_NUMBER`: The project number of the project that contains the workload identity pool.
  * `POOL_ID`: The ID of the workload identity pool.
  * `PROVIDER_ID`: The ID of the workload identity pool provider.
  * `SERVICE_ACCOUNT_EMAIL`: If you use service account impersonation, replace with the email address of the service account. Omit this flag if you don't use service account impersonation.
  * `APPLICATION_ID_URI`: The Application ID URI of the Azure application.
  * `SERVICE_ACCOUNT_TOKEN_LIFETIME`: If you use service account impersonation,lifetime of the service account access token, in seconds; this defaults to one hour when not provided. Omit this flag if you don't use service account impersonation. To specify a lifetime longer than one hour, you must configure the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` [organizational policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).
  * `FILEPATH`: The file to save configuration to.
  * `REGION`: Optional. Specify the region of the [regional Security Token Service endpoints](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#sts-regional-endpoints), if they are available.



### Use the credential configuration to access Google Cloud

To let tools and client libraries use your credential configuration, do the following in your AWS or Azure environment:

  1. Initialize an environment variable `GOOGLE_APPLICATION_CREDENTIALS` and point it to the credential configuration file:

#### Bash
         
         export GOOGLE_APPLICATION_CREDENTIALS=`pwd`/FILEPATH.json
           

where `FILEPATH` is the relative path to the credential configuration file. 

#### PowerShell
         
         $env:GOOGLE_APPLICATION_CREDENTIALS = Resolve-Path 'FILEPATH.json'
           

where `FILEPATH` is the relative path to the credential configuration file. 

  2. Use a client library or tool that supports Workload Identity Federation and can [find credentials automatically](https://docs.cloud.google.com/docs/authentication/application-default-credentials):

###  C++ 

The [Google Cloud Client Libraries for C++](https://docs.cloud.google.com/cpp/docs) support Workload Identity Federation since version [v2.6.0](https://github.com/googleapis/google-cloud-cpp/releases/tag/v2.6.0). To use Workload Identity Federation, you must build the client libraries with version 1.36.0 or later of gRPC.

###  Go 

Client libraries for Go support Workload Identity Federation if they use version v0.0.0-20210218202405-ba52d332ba99 or later of the `golang.org/x/oauth2` module.

To check which version of this module your client library uses, run the following commands:
         
         cd $GOPATH/src/cloud.google.com/go
         go list -m golang.org/x/oauth2
         

###  Java 

Client libraries for Java support Workload Identity Federation if they use version 0.24.0 or later of the [`com.google.auth:google-auth-library-oauth2-http` artifact](https://search.maven.org/artifact/com.google.auth/google-auth-library-oauth2-http).

To check which version of this artifact your client library uses, run the following Maven command in your application directory:
         
         mvn dependency:list -DincludeArtifactIds=google-auth-library-oauth2-http
         

###  Node.js 

Client libraries for Node.js support Workload Identity Federation if they use version 7.0.2 or later of the [`google-auth-library` package](https://github.com/googleapis/google-auth-library-nodejs).

To check which version of this package your client library uses, run the following command in your application directory:
         
         npm list google-auth-library
         

When you create a `GoogleAuth` object, you can specify a project ID, or you can allow `GoogleAuth` to find the project ID automatically. To find the project ID automatically, the service account in the configuration file must have the Browser role (`roles/browser`), or a role with equivalent permissions, on your project. For details, see the [`README` for the `google-auth-library` package](https://github.com/googleapis/google-auth-library-nodejs#using-external-identities).

###  Python 

Client libraries for Python support Workload Identity Federation if they use version 1.27.0 or later of the [`google-auth` package](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth).

To check which version of this package your client library uses, run the following command in the environment where the package is installed:
         
         pip show google-auth
         

To specify a project ID for the authentication client, you can set the `GOOGLE_CLOUD_PROJECT` environment variable, or you can allow the client to find the project ID automatically. To find the project ID automatically, the service account in the configuration file must have the Browser role (`roles/browser`), or a role with equivalent permissions, on your project. For details, see the [user guide for the `google-auth` package](https://github.com/googleapis/google-cloud-python/blob/main/packages/google-auth/docs/user-guide.rst#using-external-identities).

###  gcloud 

To authenticate using Workload Identity Federation, use the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command:
         
         gcloud auth login --cred-file=FILEPATH.json
         

Replace `FILEPATH` with the path to the credential configuration file.

Support for Workload Identity Federation in gcloud CLI is available in [version 363.0.0 and later versions of the gcloud CLI](https://docs.cloud.google.com/sdk/docs/components#updating_components).

###  Terraform 

The [Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) supports Workload Identity Federation if you use version 3.61.0 or later:
         
         terraform {
           required_providers {
             google = {
               source  = "hashicorp/google"
               version = "~> 3.61.0"
             }
           }
         }
         

###  bq 

To authenticate using Workload Identity Federation, use the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command, as follows:
         
         gcloud auth login --cred-file=FILEPATH.json
         

Replace `FILEPATH` with the path to the credential configuration file.

Support for Workload Identity Federation in bq is available in [version 390.0.0 and later versions of the gcloud CLI](https://docs.cloud.google.com/sdk/docs/components#updating_components).

If you can't use a client library that supports Workload Identity Federation, you can authenticate programmatically by using the REST API.




## Advanced scenarios

### Authenticate a workload using the REST API

If you can't use the client libraries, you can follow these steps to let an external workload obtain a short-lived access token by using the REST API:

  1. Obtain credentials from your external IdP:

###  AWS 

Create a JSON document that contains the information that you would normally include in a request to the AWS [`GetCallerIdentity()`](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity) endpoint, including a valid [request signature](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

Workload Identity Federation refers to this JSON document as a `GetCallerIdentity` token. The token lets Workload Identity Federation verify the identity without revealing the AWS secret access key.

A `GetCallerIdentity` token looks similar to the following:
         
         {
           "url": "https://sts.amazonaws.com?Action=GetCallerIdentity&Version=2011-06-15",
           "method": "POST",
           "headers": [
             {
               "key": "Authorization",
               "value": "AWS4-HMAC-SHA256 Credential=AKIASOZTBDV4D7ABCDEDF/20200228/us-east-1/sts/aws4_request, SignedHeaders=host;x-amz-date;x-goog-cloud-target-resource, Signature=abcedefdfedfd"
             },
             {
               "key": "host",
               "value": "sts.amazonaws.com"
             },
             {
               "key": "x-amz-date",
               "value": "20200228T225005Z"
             },
             {
               "key": "x-goog-cloud-target-resource",
               "value": "//iam.googleapis.com/projects/12345678/locations/global/workloadIdentityPools/my-pool/providers/my-aws-provider"
             },
             {
               "key": "x-amz-security-token",
               "value": "GizFWJTqYX...xJ55YoJ8E9HNU="
             }
           ]
         }
         

The token contains the following fields:

     * `url`: The URL of the AWS STS endpoint for `GetCallerIdentity()`, with the body of a standard `GetCallerIdentity()` request appended as query parameters. For example, `https://sts.amazonaws.com?Action=GetCallerIdentity&Version=2011-06-15`. We recommend that you use regional STS endpoints and [design a reliable infrastructure for your workloads](https://docs.cloud.google.com/architecture/infra-reliability-guide/design). For more information, see [Regional AWS STS endpoints](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html#sts-endpoints).
     * `method`: The HTTP request method: `POST`.
     * `headers`: The HTTP request headers, which must include: 
       * `Authorization`: The request signature.
       * `host`: The hostname of the `url` field; for example, `sts.amazonaws.com`.
       * `x-amz-date`: The time you will send the request, formatted as an [ISO 8601 Basic](https://docs.aws.amazon.com/general/latest/gr/sigv4_elements.html#sigv4_elements_date) string. This value is typically set to the current time and is used to help prevent replay attacks.
       * `x-goog-cloud-target-resource`: The full resource name of the IdP without an `https:` prefix. To help ensure data integrity, we recommend that you include this header in the `SignedHeaders` field of the signed request. For example: 
             
             //iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID
             

       * `x-amz-security-token`: Session token. Only required if you are using [temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html).

The following example creates a URL-encoded `GetCallerIdentity` token. Extract the URL-encoded token for later use. It also creates a human-readable token just for your reference:
    
    import json
    import urllib
    
    import boto3
    from botocore.auth import SigV4Auth
    from botocore.awsrequest import AWSRequest
    
    
    def create_token_aws(project_number: str, pool_id: str, provider_id: str) -> None:
        # Prepare a GetCallerIdentity request.
        request = AWSRequest(
            method="POST",
            url="https://sts.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15",
            headers={
                "Host": "sts.amazonaws.com",
                "x-goog-cloud-target-resource": f"//iam.googleapis.com/projects/{project_number}/locations/global/workloadIdentityPools/{pool_id}/providers/{provider_id}",
            },
        )
    
        # Set the session credentials and Sign the request.
        # get_credentials loads the required credentials as environment variables.
        # Refer:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
        SigV4Auth(boto3.Session().get_credentials(), "sts", "us-east-1").add_auth(request)
    
        # Create token from signed request.
        token = {"url": request.url, "method": request.method, "headers": []}
        for key, value in request.headers.items():
            token["headers"].append({"key": key, "value": value})
    
        # The token lets workload identity federation verify the identity without revealing the AWS secret access key.
        print("Token:\n%s" % json.dumps(token, indent=2, sort_keys=True))
        print("URL encoded token:\n%s" % urllib.parse.quote(json.dumps(token)))
    
    
    def main() -> None:
        # TODO(Developer): Replace the below credentials.
        # project_number: Google Project number (not the project id)
        project_number = "my-project-number"
        pool_id = "my-pool-id"
        provider_id = "my-provider-id"
    
        create_token_aws(project_number, pool_id, provider_id)
    
    
    if __name__ == "__main__":
        main()

Initialize the following variables:

#### Bash
    
    SUBJECT_TOKEN_TYPE="urn:ietf:params:aws:token-type:aws4_request"
    SUBJECT_TOKEN=TOKEN
    

#### PowerShell
    
    $SubjectTokenType = "urn:ietf:params:aws:token-type:aws4_request"
    $SubjectToken = "TOKEN"
    

Where `TOKEN` is the [URL encoded](https://en.wikipedia.org/wiki/Percent-encoding) `GetCallerIdentity` token that was generated by the script.

###  Azure 

Connect to an Azure VM that has an [assigned managed identity](https://docs.microsoft.com/azure/active-directory/managed-identities-azure-resources/qs-configure-portal-windows-vm#user-assigned-managed-identity) and [obtain an access token](https://docs.microsoft.com/azure/active-directory/managed-identities-azure-resources/qs-configure-portal-windows-vm#user-assigned-managed-identity) from the Azure Instance Metadata Service (IMDS):

#### Bash
    
    SUBJECT_TOKEN_TYPE="urn:ietf:params:oauth:token-type:jwt"
    SUBJECT_TOKEN=$(curl \
      "http://169.254.169.254/metadata/identity/oauth2/token?resource=APP_ID_URI&api-version=2018-02-01" \
      -H "Metadata: true" | jq -r .access_token)
    echo $SUBJECT_TOKEN
    

This command uses the [`jq` tool](https://stedolan.github.io/jq/). `jq` is available by default in Cloud Shell.

#### PowerShell
    
    $SubjectTokenType = "urn:ietf:params:oauth:token-type:jwt"
    $SubjectToken = (Invoke-RestMethod `
      -Uri "http://169.254.169.254/metadata/identity/oauth2/token?resource=APP_ID_URI&api-version=2018-02-01" `
      -Headers @{Metadata="true"}).access_token
    Write-Host $SubjectToken
    

Where `APP_ID_URI` is the **Application ID URI** of the application that you've [configured for Workload Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation#prepare).

  2. Use the [Security Token Service API](https://docs.cloud.google.com/iam/docs/reference/sts/rest) to exchange the credential against a short-lived access token:

#### Bash
         
         STS_TOKEN=$(curl https://sts.googleapis.com/v1/token \
             --data-urlencode "audience=//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID" \
             --data-urlencode "grant_type=urn:ietf:params:oauth:grant-type:token-exchange" \
             --data-urlencode "requested_token_type=urn:ietf:params:oauth:token-type:access_token" \
             --data-urlencode "scope=https://www.googleapis.com/auth/cloud-platform" \
             --data-urlencode "subject_token_type=$SUBJECT_TOKEN_TYPE" \
             --data-urlencode "subject_token=$SUBJECT_TOKEN" | jq -r .access_token)
         echo $STS_TOKEN
         

#### PowerShell
         
         [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
         $StsToken = (Invoke-RestMethod `
             -Method POST `
             -Uri "https://sts.googleapis.com/v1/token" `
             -ContentType "application/json" `
             -Body (@{
                 "audience"           = "//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID"
                 "grantType"          = "urn:ietf:params:oauth:grant-type:token-exchange"
                 "requestedTokenType" = "urn:ietf:params:oauth:token-type:access_token"
                 "scope"              = "https://www.googleapis.com/auth/cloud-platform"
                 "subjectTokenType"   = $SubjectTokenType
                 "subjectToken"       = $SubjectToken
             } | ConvertTo-Json)).access_token
         Write-Host $StsToken
         

Replace the following values:

     * `PROJECT_NUMBER`: Project number of the project that contains the workload identity pool
     * `POOL_ID`: ID of the workload identity pool
     * `PROVIDER_ID`: ID of the workload identity pool provider

To use regional Security Token Service endpoints, replace `https://sts.googleapis.com/v1/token` with the following:
    
    https://sts.REGION.rep.googleapis.com/v1/token 

Replace `REGION` with a [Google Cloud location](https://cloud.google.com/about/locations), for example, `us-central1` or `europe-west4`.

**Note:** The audience must not include a `https:` scheme.
  3. If you use service account impersonation, use the token from the Security Token Service to invoke the [`generateAccessToken` method](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateAccessToken) of the [IAM Service Account Credentials API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest) to obtain an access token.




#### Tokens for Cloud Run services

When accessing a Cloud Run service, you must use an ID token.

#### Bash
    
    
    TOKEN=$(curl -0 -X POST https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT_EMAIL:generateIdToken \
        -H "Content-Type: text/json; charset=utf-8" \
        -H "Authorization: Bearer $STS_TOKEN" \
        -d @- <<EOF | jq -r .token
        {
            "audience": "SERVICE_URL"
        }
    EOF
    )
    echo $TOKEN
    

#### PowerShell
    
    
    $Token = (Invoke-RestMethod `
        -Method POST `
        -Uri "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT_EMAIL:generateIdToken" `
        -Headers @{ "Authorization" = "Bearer $StsToken" } `
        -ContentType "application/json" `
        -Body (@{
            "audience" = "SERVICE_URL"
        } | ConvertTo-Json)).token
    Write-Host $Token
    

Replace the following: 

  * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account. 
  * `SERVICE_URL`: the URL of the service—for example, `https://my-service-12345-us-central1.run.app`. You can also set it to your custom service endpoint. For more information, see [Understanding custom audiences](https://cloud.google.com/run/docs/configuring/custom-audiences#understanding). 



#### Tokens for other platforms

When accessing another service, you must use an access token.

#### Bash
    
    
    TOKEN=$(curl -0 -X POST https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT_EMAIL:generateAccessToken \
        -H "Content-Type: text/json; charset=utf-8" \
        -H "Authorization: Bearer $STS_TOKEN" \
        -d @- <<EOF | jq -r .accessToken
        {
            "scope": [ "https://www.googleapis.com/auth/cloud-platform" ]
        }
    EOF
    )
    echo $TOKEN
    

#### PowerShell
    
    
    $Token = (Invoke-RestMethod `
        -Method POST `
        -Uri "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT_EMAIL:generateAccessToken" `
        -Headers @{ "Authorization" = "Bearer $StsToken" } `
        -ContentType "application/json" `
        -Body (@{
            "scope" = , "https://www.googleapis.com/auth/cloud-platform"
        } | ConvertTo-Json)).accessToken
    Write-Host $Token
    

Replace the following: 

  * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account. 



## What's next

  * Read more about [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).
  * Learn about [best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation).
  * See how you can [manage workload identity pools and providers](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
