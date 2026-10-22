---
url: https://docs.cloud.google.com/data-studio/set-up-a-google-cloud-service-account/
title: Set up a Google Cloud service account for Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:38.767850+00:00
---

# Set up a Google Cloud service account for Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/set-up-a-google-cloud-service-account/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Set up a Google Cloud service account for Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

**Audience:** This page is intended for Google Cloud administrators.

To learn how to use an existing service account in your Data Studio data source, see [Data credentials](https://docs.cloud.google.com/data-studio/data-credentials).

Instead of delegating access using [Owner's credentials](https://docs.cloud.google.com/data-studio/data-credentials), or requiring individual report viewers to have access to the data using viewer's credentials, Data Studio can use a service account to access data. A service account is a special type of Google Account that is intended to represent a non-human user that can authenticate and be authorized to access data in Google APIs and products.

**Note:** Service account credentials are available only for BigQuery data sources.

Learn more about [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).

## Benefits of using a service account with Data Studio

Using a service account instead of an individual user's credentials provides these benefits:

  * Data sources using service account credentials won't break if the creator leaves your company.
  * Service account credentials support access to data that is located behind [VPC Service Controls perimeters that use device policies](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).
  * Automated features like scheduled emails, alerts, and scheduled data extracts work with data sources that are behind a VPC Service Controls perimeter. (See the Notes and limits for an important caveat.)
  * You can create [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) to allow the service account access to and from the resources and clients that are protected by service perimeters.

**Tip:** Rather than add Data Studio data access to an existing service account, **we recommend** that you create a new service account that is for use solely with Data Studio. Using dedicated service accounts can help maintain appropriate data management and simplify data access.

## Required roles

Following are the roles required to configure a service account for Data Studio:

### For administrators

  * To get the Data Studio service agent, you must be a Google Workspace or Cloud Identity user.
  * To set up a service account, you need to have the **Service Account Admin** (`roles/iam.serviceAccountAdmin`) or **Create Service Accounts** (`roles/iam.serviceAccountCreator`) role on your Google Cloud project. Learn more about [service account roles](https://docs.cloud.google.com/iam/docs/roles-permissions/iam).
  * To configure the service account to access a BigQuery table or dataset, you must have the **BigQuery Data Owner** (`roles/bigquery.dataOwner`) role on the table or dataset, or another role that gives you the `bigquery.datasets.setIamPolicy` permission.



### For the service account

  * At a minimum, the service account must be granted the **BigQuery Data Viewer** (`roles/bigquery.dataViewer`) role on the specific tables or datasets that it needs to access.
  * **Custom queries:** If the data source uses a custom query, the service account must also be granted the **BigQuery Job User** (`roles/bigquery.jobUser`) role on the Google Cloud project that contains the data.



## Setup instructions

To set up a service account that provides access to BigQuery data, follow these steps:

  1. **Get the Data Studio service agent**. In this step, you'll copy the service agent email address so that you can use it in the next step. This address is created for you automatically by Data Studio.
  2. **Create a service account for Data Studio**. In this step, you'll create the non-human user that will access the data.
  3. **Allow the Data Studio service agent to access your service account**. In this step, you'll grant the service agent the required role on the service account.
  4. **Grant user roles**. In this step, you'll grant your users the required role so that they can create data sources that use service account credentials.
  5. **Enable the service account to access your BigQuery data**. In this step, you'll grant the service account the required role so that it can access a BigQuery table or dataset.

**Tip:** You'll need to perform the instructions on this page only once unless you want to create different service accounts for different teams or groups of users. To create multiple service accounts, repeat these instructions for each additional service account.

### Step 1: Get the Data Studio service agent

To allow the service account to access your data, you'll need to provide the Data Studio service agent for your organization. You can get the service agent from a help page in Data Studio:

  1. Navigate to the [Data Studio service agent help page](https://datastudio.google.com/c/serviceAgentHelp).
  2. Copy the service agent email address that's shown on that page.



### Step 2: Create a service account for Data Studio

See the [Google Cloud IAM documentation](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) for instructions on creating a service account. You can use either the Google Cloud console or the Cloud Shell command line to create the service account.

### Console

  1. From the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create)

  2. Select a project.
  3. Enter a service account name to display in the Google Cloud console. 

The Google Cloud console generates a service account ID that's based on this name. Edit the ID now if necessary. You can't change the ID later.

  4. Optional: Enter a description for the service account.
  5. Click **CREATE AND CONTINUE**. 
  6. In **Permissions** , grant the service account the **BigQuery Job User** [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles) in the project that contains the data to which you want to connect in Data Studio. Note that this might be different from the project in which you created the service account. 
  7. Click **Continue**.
  8. In the **Service account users role** field, add the users who can use this service account to provide credentials for their data sources. If you're not ready to add users now, you can do so later by following the directions in Grant user roles.
  9. Click **DONE** to save the service account and return to the service accounts list page for your project.



### gcloud

Follow the general steps that are listed under **Cloud Shell** in [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-gcloud).

  1. [Open the Cloud Shell](https://console.cloud.google.com/home/dashboard?cloudshell=true).
  2. Select a project, if necessary.
  3. To create the service account, run the [gcloud iam service-accounts create](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create) command. You can use whatever account name, description, and display name that you choose.



**Example:**
    
    
    gcloud iam service-accounts create looker-studio-service-account \
    --description="Use for Data Studio access to BigQuery"  \
    --display-name="LS_BQ"
    

  4. To access BigQuery data on the Google Cloud project that you want to use with Data Studio, give the service account the `bigquery.jobs.create` permission in that project. You can grant the **BigQuery Job User** [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles) to give this permission.

In addition, give the service account `bigquery.tables.getData` and `bigquery.tables.get` permissions on the project or dataset that you want to use with Data Studio. You can grant the **BigQuery Data Viewer** role (`roles/bigquery.dataViewer`) to give these permissions.

To grant these roles, run the [gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. In the following examples, replace PROJECT_ID with your project ID.




**Example: Grant the BigQuery Job User role**
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:looker-studio-service-account@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/bigquery.jobUser"
    

**Example: Grant the BigQuery Data Viewer role**
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:looker-studio-service-account@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/bigquery.dataViewer"
    

### Step 3: Allow the Data Studio service agent to access your service account

To allow the Data Studio service agent to access data by using the service account, grant the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`) to the service agent.

### Console

  1. Return to the [Google Cloud console service accounts list](https://console.cloud.google.com/iam-admin/serviceaccounts).
  2. Select the Data Studio service account that you just created by clicking it in the list.
  3. Click **Principals with access**.
  4. Click person_add**GRANT ACCESS**.
  5. In **Add principals to`PROJECT_ID`**, paste the Data Studio service agent email (which you copied in step 1 previously) into the **New principals** box. Your service agent's address looks like this: 
         
         service-org-ORG-ID@gcp-sa-datastudio.iam.gserviceaccount.com
         

Replace ORG-ID with your Google Cloud organization ID. 
  6. Select a role that gives the service agent the `iam.serviceAccounts.getAccessToken`permission. For example, you can use the **Service Account Token Creator** role, but you can also use any custom role that grants this permission.
  7. Click **SAVE**.



### gcloud

Run the [gcloud iam service-accounts add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command. In the following example, replace ORG_ID with your organization's ID.

**Example:**
    
    
    gcloud iam service-accounts add-iam-policy-binding looker-studio-service-account@PROJECT_ID.iam.gserviceaccount.com \
    --member="serviceAccount:service-org-ORG_ID@gcp-sa-datastudio.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountTokenCreator"
    

### Step 4: Grant user roles

Data Studio users who will create or edit data sources need to be granted a role that includes the `iam.serviceAccounts.actAs` permission, such as the **Service Account User** role (`roles/iam.serviceAccountUser`). You can grant this role on the project or on an individual service account, but we recommend that you grant the role on the service account only. For instructions, see [Managing service account impersonation](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts).

We recommend that you **not** grant non-service agent users the **Service Account Token Creator** role — it is not needed for Data Studio.

**Notes:**

  * This step is optional if you already added Data Studio users while creating the service account, as described in Create a service account for Data Studio.
  * If you're not ready to complete this step, you can come back to it later.
  * Users who will only view Data Studio reports don't need to have permissions on the service account.



### Console

  1. Navigate to the [Console service accounts list](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts).
  2. Select your Data Studio service account by clicking it in the list.
  3. Click the **Principals with access**.
  4. Click  person_add  **GRANT ACCESS**.
  5. In **Add principals and roles for Service Account** , enter the email addresses of your users in the **New principals** box.
  6. Select the **Service Account User** role.
  7. Click **SAVE**.



### gcloud

To grant the **Service Account User** role, run the [gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. In the following examples, replace PROJECT_ID with your project ID, and replace USER_EMAIL with one or more valid email addresses (separate multiple entries with commas). 

**Example:**
    
    
    gcloud iam service-accounts add-iam-policy-binding  looker-studio-service-account@PROJECT_ID.iam.gserviceaccount.com  \
    --member="user:USER_EMAIL" \
    --role="roles/iam.serviceAccountUser"
    

### Step 5: Enable the service account to access your BigQuery data

To allow Data Studio to access your data, grant the **BigQuery Data Viewer** role to the service account at the table or dataset level. We **don't recommend** granting service account access at the project level.

**Note:** If your Data Studio data source uses a custom query, the service account must also have the **BigQuery Job User** role (`roles/bigquery.jobUser`) on the Google Cloud project that contains the data, in addition to the **BigQuery Data Viewer** role. BigQuery requires project-level job creation permissions to run custom queries.

**Important:** You must have a role on the table or dataset that `bigquery.datasets.setIamPolicy` permission for that table or dataset, such as the **BigQuery Data Owner** role. Otherwise, you won't be able to give the service account access to the data.

To complete this step, copy the Data Studio service account email address, as described previously in Step 2. Create a Data Studio service account so that you can paste it into the **Add principal** dialog when instructed to do so.

### Console

**To grant access to a table** :

  1. Copy the Data Studio service account, as described previously in Step 2: Create a service account for Data Studio.
  2. Navigate to [BigQuery](https://console.cloud.google.com/bigquery), and then select a project.
  3. Click dataset **Datasets** , and then select a dataset.
  4. Select a table.
  5. In the toolbar, the click person_add **SHARE** menu, and then click **Share**.
  6. In the **Share permissions** panel, click person_add **ADD PRINCIPAL**.
  7. In the **New principals** box, paste the Data Studio service account email address.
  8. Select the **BigQuery Data Viewer** role.
  9. Click **SAVE**.



**To grant access to a dataset** :

  1. Copy the Data Studio service account, as described previously in Step 2: Create a service account for Data Studio.
  2. Navigate to [BigQuery](https://console.cloud.google.com/bigquery), and then select a project.
  3. Click dataset **Datasets** and then select a dataset.
  4. Click more_vert **Actions** chevron_forward **Share** chevron_forward **Manage permissions**.
  5. In the **Share permissions** panel, click person_add **ADD PRINCIPAL**.
  6. In the **New principals** box, paste the Data Studio service account email address.
  7. Select the **BigQuery Data Viewer** role.
  8. Click **SAVE**.



### gcloud

We recommend using the Google Cloud console instructions to grant access to data. To grant access to data using the `bq` command line tool, see [ Controlling access to datasets](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls#granting_access_to_a-dataset) in the BigQuery documentation.

## Provide the Data Studio service account(s) to your Data Studio users

Data Studio users will need to know which service account to use when they create data sources. As there is no way to see the list of available service accounts from within Data Studio, you should make this information available using your organization's documentation, internal website, or email.

**Notes** :

  * You don't need to manage service account keys manually, nor do users need to download service account keys from Google Cloud console and upload them to Data Studio.
  * The limit of 10 service account keys per service account doesn't apply to Data Studio.
  * Simply knowing the service agent name doesn't allow a user to access data. The service agent needs to be added to a service account, and end users need to have permission to act as that service account.



## Create a data source that uses service account credentials

To create data sources that use service account credentials, Data Studio users can follow the same basic steps as for other [data credential types](https://docs.cloud.google.com/data-studio/data-credentials):

  1. [Create or edit a BigQuery data source](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery).
  2. In the toolbar, click **Data Credentials**.
  3. Select **Service** **Account Credentials**.
  4. Enter your **Service account** email address in the box.
  5. Click **Update**.



## Edit a data source that uses service account credentials

When someone edits a data source that uses service account credentials, Data Studio checks to see if they have permission to use the service account. If they don't, the data source switches to use that person's credentials instead.

## See who is using the service account to access data

You can [check the audit logs for service accounts](https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts) in the Google Cloud console. You must [enable IAM audit logs for Data Access activity](https://docs.cloud.google.com/iam/docs/audit-logging#enabling_audit_logging) if you want to receive audit logs for service accounts.

## Service account example scenario

Suppose you want to make sure that Data Studio users in your company have access only to the data for their country's subsidiary. A solution is to create a service account for each country, and only give Data Studio users in that country permission to act as the service account.

### Example setup

In this example, you'll create three service accounts: one for the UK, one for France, and one for Germany. You'll then assign as principals your service agent and any users whom you want to be able to create data sources that use the service account. You'll also assign the proper roles to each.

#### UK service account

`service-account-1@example-org-uk-example-project.iam.gserviceaccount.com`

#### UK principals

Principals | Roles  
---|---  
`service-org-12345@gcp-sa-datastudio.iam.gserviceaccount.com` _This is the service agent._ | `Service Account Token Creator`  
User 1 | `Service Account User`  
User 2 | `Service Account User`  
  
#### France service account

`service-account-1@example-org-fr-example-project.iam.gserviceaccount.com`

#### France principals

Principals | Roles  
---|---  
`service-org-12345@gcp-sa-datastudio.iam.gserviceaccount.com` _This is the service agent._ | `Service Account Token Creator`  
User 3 | `Service Account User`  
User 4 | `Service Account User`  
  
#### Germany service account

`service-account-1@example-org-de-example-project.iam.gserviceaccount.com`

#### Germany principals

Principals | Roles  
---|---  
`service-org-12345@gcp-sa-datastudio.iam.gserviceaccount.com` _This is the service agent._ | `Service Account Token Creator`  
User 5 | `Service Account User`  
User 6 | `Service Account User`  
**Key Point:** The service account name is not sensitive information: Even if User 5 knows that `service-account-1@example-org-fr-example-project.iam.gserviceaccount.com` exists, they can't use it because they don't have the right permissions. The service agent needs to be added to a service account for it to function. (The service agent is just how Data Studio makes use of the service account.)

## Errors

This section explains the errors that Data Studio data source creators and report viewers might see when they try to use a service account. In most cases, these errors have the same root cause: incorrect or incomplete setup of the service account.

#### Missing service agent role

#### Messages

  * Data Studio's service agent is missing `iam.serviceAccounts.getAccessToken` permission for this service.
  * The service agent used by this data source's service account is missing the "Service Account Token Creator" role.

  
---  
  
#### Cause

The service agent hasn't been granted the **Service Account Token Creator** role (or another role that includes the `iam.serviceAccounts.getAccessToken` permission).  
  
#### Solution

Grant the **Service Account Token Creator** role to the service agent.  
  
#### No access to the data 

#### Message 

This service account can't access the underlying dataset.   
---  
  
#### Causes 

  * The service account hasn't been granted access to the project's data.
  * The billing project is connected to a project that the service account doesn't have access to.
  * The data source uses a custom query, but the service account doesn't have the **BigQuery Job User** role on the project.

  
  
#### Solution 

  * At a minimum, grant the **BigQuery Data Viewer** role to your service account on the underlying table, dataset, or project.
  * If you're using a custom query, also grant the **BigQuery Job User** role to the service account on the project in which the query runs.

  
  
#### Missing user role

#### Message 

You don't have permission to use this service account.  
---  
  
#### Cause 

The user hasn't been added as a principal to the service account with the **Service Account User** role.  
  
#### Solution 

Grant the **Service Account User** role to the user on the service account.  
  
#### Service agent not available for the account

#### Messages 

  * Service agents cannot be generated for this account — try again with a Google Workspace or Cloud Identity managed account.
  * Service agent credentials are available only for Google Workspace or Cloud Identity managed organizations. Please use a different account to use this feature.

  
---  
  
#### Cause 

The user is trying to use a standard (consumer user) Google Account to access data that's controlled by a service account.  
  
#### Solution 

Use a Google Workspace or Cloud Identity account to access the data.  
  
#### Can't use service agent in credentials dialog

#### Message 

Data Studio service **agents** can't be used to directly connect to data. Use a service **account** instead.  
---  
  
#### Solution 

Service agents and service accounts are different. Enter a service account in the credentials dialog. You can find the list of available service accounts using either the Google Cloud console or the Cloud Shell: 

### Console

  1. Navigate to the [Google Cloud Platform > IAM & Admin > Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page. 
  2. Select a project, if necessary.
  3. In the **Service accounts for project** page, locate the service account that Data Studio will use to access your BigQuery data.
  4. Copy the email address for that account.



### gcloud

  1. [Open the Cloud Shell](https://console.cloud.google.com/home/dashboard?cloudShell=true). 
  2. Select a project, if necessary.
  3. To list the service accounts to which you have access, run the [gcloud iam service-accounts list](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list) command. 

**Example:**
    
    
    gcloud iam service-accounts list  
  
## Notes and limits of service account credentials

  * Service account credentials are available only for BigQuery data sources. [IAM limits](https://docs.cloud.google.com/iam/quotas#limits) apply to service accounts.
  * It might take a few minutes for changes to service account permissions to be reflected in Data Studio. 
  * Because Data Studio runs on Google-managed infrastructure with dynamic IP addresses and project allocations, you can't configure VPC Service Controls perimeters by using static IP allowlists or project rules. To permit Data Studio access through a VPC Service Controls perimeter, you must add a service account as a principal in your access levels or ingress and egress rules.



## Related resources

  * [Understanding service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts)
  * [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules)
  * [Connect to BigQuery: Support for VPC Service Controls](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery)
  * [Launching Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
