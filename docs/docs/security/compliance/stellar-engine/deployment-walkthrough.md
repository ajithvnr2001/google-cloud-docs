---
url: https://docs.cloud.google.com/docs/security/compliance/stellar-engine/deployment-walkthrough/
title: Create a landing zone using Stellar Engine \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:42.261331+00:00
---

# Create a landing zone using Stellar Engine  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/stellar-engine/deployment-walkthrough/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Create a landing zone using Stellar Engine Stay organized with collections  Save and categorize content based on your preferences. 

The landing zone deployment process consists of [stages](https://docs.cloud.google.com/docs/security/compliance/stellar-engine/deployment-stages). During each stage, you must add certain variables to the `terraform.tfvars` file. After you complete a stage, Terraform writes a `STAGE_NAME-tfvar.auto.tfvars.json` file to the [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket that's created in the initial stage. Subsequent stages use the Google Cloud CLI to copy the files and a provider file that impersonates a stage-specific service account into the new stage folder.

Depending on the number of tenants, deploying a new environment takes approximately one hour.

## Prerequisites

Complete the following tasks before deploying Stellar Engine.

### Set up Google Cloud

Complete the following steps to set up Google Cloud:

  1. Select a Google Cloud organization. If you create a new organization, sign in to the [Google Admin console](https://admin.google.com) at least once.

  2. Configure multiple administrators to implement separation of duties. In a testing environment, one user might have administrator roles for all resources. However, in a production environment, you require multiple administrators. For more information, see [Set up your organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#setting-up).

**Note:** If you have access issues, grant the roles to yourself on the organization node or have your administrator grant them for you. You might need to reload the page in your browser or sign out and sign back in to the Google Cloud console to apply the new permissions.
  3. Enable [2-step verification](https://docs.cloud.google.com/docs/authentication/mfa-requirement) for all privileged accounts.

  4. [Disable Cloud Shell](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell). Cloud Shell isn't supported for IL4 or IL5 environments and must be disabled by a Google Workspace administrator.

  5. If you don't have a project, [create a bootstrap project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

[Create a project](https://console.cloud.google.com/projectcreate)

  6. Complete the following tasks in the bootstrap project:

     1. Enable billing. For instructions, see [Verify the billing status of your projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

     2. Enable the Cloud Monitoring API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com)



* Verify that your user account is a [Super Admin](https://admin.google.com/ac/roles).

* If your organization doesn't have a data classification scheme, create one.

### Assign roles

Assign the following [Identity and Access Management](https://docs.cloud.google.com/iam/docs) roles to the user account that's deploying Stellar Engine.

  1. Make sure that you have the following role or roles on the organization: Access Transparency Admin, Assured Workloads Administrator, Billing Account Administrator, Logging Admin, Organization Administrator, Organization Policy Admin, Organization Role Administrator, Owner, Project Creator, Service Account Admin, Service Account Token Creator, Tag Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
     2. Select the organization. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
     2. Select the organization. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



If you are starting with a new organization, you can run the following script that's located in the [fast/stages-aw/0-bootstrap](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/0-bootstrap) folder to apply the roles:
    
    
    ./setIAM.sh EMAIL_ADDRESS ORGANIZATION_ID
    

Replace the following:

  * `EMAIL_ADDRESS`: The email address of your user account.
  * `ORGANIZATION_ID`: Your organization ID.



This script adds all roles except for Billing Account Administrator and Super Admin.

**Caution:** When you run this script, you lose all current permissions for your user account except for Super Admin.

### Add groups and configure services

  1. Add the following groups, as described in [2\. Users and groups](https://docs.cloud.google.com/docs/enterprise/cloud-setup#checklist-heading-2):

     * `gcp-billing-admins@`DOMAIN
     * `gcp-developers@`DOMAIN
     * `gcp-devops@`DOMAIN
     * `gcp-hybrid-connectivity-admins@`DOMAIN
     * `gcp-logging-monitoring-admins@`DOMAIN
     * `gcp-logging-monitoring-viewers@`DOMAIN
     * `gcp-organization-admins@`DOMAIN
     * `gcp-vpc-network-admins@`DOMAIN
     * `gcp-security-admins@`DOMAIN

[Go to Stage 2](https://console.cloud.google.com/cloud-setup/overview)

Replace `DOMAIN` with your FQDN.

If prompted, skip the identity provider step.

**Note:** You don't have to complete subsequent steps, but make sure you finish Step 2.

Google might change the default group names. You can manually create a [group](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console) if it isn't in the setup guide.

  2. Enable the Assured Workloads, BigQuery, Cloud Billing, Cloud Logging, Cloud KMS, IAM, Pub/Sub, Resource Manager, Service Account Credentials, Service Usage, Organization Policy Service APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=assuredworkloads.googleapis.com,bigquery.googleapis.com,cloudbilling.googleapis.com,logging.googleapis.com,cloudkms.googleapis.com,iam.googleapis.com,pubsub.googleapis.com,cloudresourcemanager.googleapis.com,iamcredentials.googleapis.com,serviceusage.googleapis.com,orgpolicy.googleapis.com)

You can also use the [`fast/stages-aw/0-bootstrap/enableServices.sh`](https://github.com/google/stellar-engine/blob/main/fast/stages-aw/0-bootstrap/enableServices.sh) script to enable the services.

**Note:** If you encounter issues with the script, you can run the following deprecated command on macOS and other Unix variants: 
    
    echo "iam cloudkms pubsub serviceusage cloudresourcemanager bigquery assuredworkloads cloudbilling logging iamcredentials orgpolicy" | xargs -n1 -I {} gcloud services enable "{}.googleapis.com"

  3. [Enable Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable).

  4. If your quota is less than 13 projects, go to [Google Cloud Platform/API Project: Request Billing Quota Increase](https://support.google.com/code/contact/billing_quota_increase) to request 13 projects. For more information, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).




### Configure your local environment

Complete the following steps to configure your local environment:

  1. Clone the [Stellar Engine GitHub repository](https://github.com/google/stellar-engine/).
  2. Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
  3. Update your local [Terraform](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli) to a version that is 1.8.1 or later.
  4. Install the [jq binary](https://jqlang.github.io/jq/download/).
  5. Authenticate and set the bootstrap project as the active project:
         
         gcloud auth login
         gcloud config set project BOOTSTRAP_PROJECT_ID
         gcloud auth application-default login
         




### Modify modules

In most circumstances, you can use the repository without changes. If you need to modify a module, copy the entire module and use the naming convention `&lt;module-se&gt;` to avoid merge conflicts when periodic updates are pulled in from the Cloud foundation fabric repository.

## Run Stage 0: Bootstrap

Stage 0 aligns the existing parts of the network with the Terraform state. Stage 0 creates the initial IaC bootstrap service accounts and projects. Stage 0 designed to transition from whatever project the user initially has into a new core project and migrate the Terraform state.

  1. Change directory into [`fast/stages-aw/0-bootstrap`](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/0-bootstrap).

  2. Copy the `terraform.tfvars.sample` file:
         
         cp terraform.tfvars.sample terraform.tfvars
         

  3. Copy the `providers.tf.tmp` file to the `0-bootstrap-providers.tf` file:
         
         cp providers.tf.tmp 0-bootstrap-providers.tf
         

  4. Update the information in `fast/stages-aw/0-bootstrap/terraform.tfvars`:
         
         billing_account = {
         id = "BILLING_ACCOUNT_ID"
         }
         regions = {
         primary = "REGION"
         }
         organization = {
         domain = "DOMAIN"
         id = "ORGANIZATION_ID"
         customer_id = "CUSTOMER_ID"
         }
         outputs_location = "~/fast-config"
         prefix = "PREFIX"
         log_sinks = {
         audit-logs = {
         filter = "logName:\"/logs/cloudaudit.googleapis.com%2Factivity\" OR logName:\"/logs/cloudaudit.googleapis.com%2Fsystem_event\" OR protoPayload.metadata.@type=\"type.googleapis.com/google.cloud.audit.TransparencyLog\""
         type = "logging"
         }
         vpc-sc = {
         filter = "protoPayload.metadata.@type=\"type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata\""
         type = "logging"
         }
         workspace-audit-logs = {
         filter = "logName:\"/logs/cloudaudit.googleapis.com%2Fdata_access\" and protoPayload.serviceName:\"login.googleapis.com\""
         type = "logging"
         }
         empty-audit-logs = {
         filter = ""
         type = "logging"
         }
         }
         org_policies_config = {
           constraints = {
             "ALLOWED_POLICY_MEMBER_DOMAINS" = []
             }
           }
         fast_features = {
         envs = true
         }
         assured_workloads = {
         regime = "COMPLIANCE_REGIME"
         location = "LOCATION"
         }
         bootstrap_project = "BOOTSTRAP_PROJECT_ID"
         alert_email = "ALERT_EMAIL"
         

Replace the following:

     * `BILLING_ACCOUNT_ID`: The billing account to use for the deployment of the environments. To find the billing account information, see the Google Cloud console.

[Go to Billing](https://console.cloud.google.com/billing)

     * `REGION`: The primary region to deploy resources into. The default is `us-east4` for IL5 and FedRAMP.

To add a secondary region to deploy resources into, add `secondary=secondary`.

     * `DOMAIN`: The fully qualified domain name (FQDN). To view the FQDN, run `gcloud organizations list`.

     * `ORGANIZATION`: The organization ID for the Google Cloud organization. To view the organization ID, run `gcloud organizations list`.

     * `CUSTOMER_ID`: The Google Workspace Directory customer ID. To view the ID, run `gcloud organizations list`.

     * `PREFIX`: The prefix to append to the names for projects and resources that are deployed. The project name must be globally unique and the prefix must contain a maximum of six characters. A 409 error occurs if the project name isn't unique.

     * `ALLOWED_POLICY_MEMBER_DOMAINS`: If required, update with additional customer IDs. For more information, see [Restrict identities with domain-restricted sharing](https://docs.cloud.google.com/organization-policy/restrict-domains).

     * `COMPLIANCE_REGIME`: The [compliance regime](https://assuredworkloads.googleapis.com/$discovery/rest?version=v1) for this environment, one of `IL4`, `IL5`, `FEDRAMP_HIGH`, and `COMPLIANCE_REGIME_UNSPECIFIED`. If you don't want to use Assured Workloads, set this value to `COMPLIANCE_REGIME_UNSPECIFIED`.

     * `LOCATION`: The US region to deploy resources into. Dual regions such as `NAM9` or continents aren't supported.

     * `BOOTSTRAP_PROJECT_ID`: The bootstrap project ID that you created in Set up Google Cloud.

     * `ALERT_EMAIL`: The email address to send logging alert notifications to.

  5. Run `terraform init`.

  6. Run `terraform apply`:
         
         terraform apply -var bootstrap_user=$(gcloud config list --format
          'value(core.account)')
         

  7. Type `yes` when prompted.

  8. Switch to your new project:
         
         gcloud config set project PREFIX-prod-iac-core-0
         

  9. Copy the new local Terraform providers file:
         
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/providers/0-bootstrap-providers.tf ./
         

  10. Migrate the state from local to remote:
         
         terraform init --migrate-state
         

  11. Type `yes` when prompted.

  12. Run `./import.sh`.

  13. Run `terraform apply` one more time. Type `yes` when prompted.




## Run Stage 1: Resource management

Stage 1 creates the different folders, projects, and service accounts at the organization level that are used for subsequent stages. To create the environment, you must update the `terraform.tfvars` file in `fast/stages-aw/1-resman` to include a `tenants` variable. Each tenant (for example, a specific federal agency or internal development group) gets its own dedicated, isolated boundary to run its workloads. Each tenant inherits the centralized security controls, networking perimeter, policy guardrails, and audit log sinks that are created in Stage 0 and Stage 2.

  1. If you are using an external billing account, see Configure billing when using external billing accounts.

  2. Change directory into [`fast/stages-aw/1-resman`](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/1-resman).

  3. Copy the `terraform.tfvars.sample` file:
         
         cp terraform.tfvars.sample terraform.tfvars
         

  4. Update `terraform.tfvars` as follows:
         
         tenants = {
         ten-1 = {
           admin_principal = "group:gcp-devops@DOMAIN"
           descriptive_name = "TENANT_ONE_NAME"
           locations = {
             gcs = "REGION"
             kms = "REGION"
             }
           },
         ten-2 = {
           admin_principal = "group:gcp-devops@DOMAIN"
           descriptive_name = "TENANT_TWO_NAME"
           locations = {
             gcs = "REGION"
             kms = "REGION"
             }
           }
         }
         fast_features = {
         envs = true
         }
         envs_folders = {
         Prod = {
           admin = "gcp-organization-admins@DOMAIN"
         },
         Int = {
           admin = "gcp-organization-admins@DOMAIN"
         },
         Test = {
           admin = "gcp-organization-admins@DOMAIN"
         }
         }
         

Replace the following:

     * `DOMAIN`: The primary fully qualified domain name (FQDN). To view the FQDN, run `gcloud organizations list`.

     * `TENANT_ONE_NAME`: the name for the first tenant project that's deployed. Use a maximum of six characters.

     * `REGION`: The primary region to deploy resources into. The default is `us-east4` for IL5 and FedRAMP.

     * `TENANT_TWO_NAME`: the name for the second tenant project that's deployed. Use a maximum of six characters.

Add as many tenant definitions as you require.

  5. Copy the `tfvars` files from Cloud Storage:
         
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/providers/1-resman-providers.tf ./ &&
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/0-globals.auto.tfvars.json ./ &&
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/0-bootstrap.auto.tfvars.json ./
         

  6. Run `terraform init`.

  7. Run `terraform apply`. Type `yes` when prompted.




## Run Stage 2: Network creation

Stage 2 includes two networking options: one for FedRAMP High and one for IL4 or IL5.

### Configure networking for FedRAMP High

  1. If you are using an external billing account, see Configure billing when using external billing accounts.

  2. Change directory into [`fast/stages-aw/2-networking-a-fedramp-high`](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/2-networking-a-fedramp-high).

  3. Copy the provider and global tfvars files from the Cloud Storage buckets:
         
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/providers/2-networking-providers.tf ./ && \
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/0-globals.auto.tfvars.json ./ && \
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/0-bootstrap.auto.tfvars.json ./ && \
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/1-resman.auto.tfvars.json ./
         

  4. Copy the `terraform.tfvars.sample` file:
         
         cp terraform.tfvars.sample terraform.tfvars
         

  5. In the `terraform.tfvars` file, update the custom subnets, proxy subnets, firewall rules, named CIDRs, and DNS response policy rules.

  6. Run `terraform init`.

  7. Run `terraform apply`. Type `yes` when prompted.




### Configure networking for IL4 or IL5

This step deploys a pair of Palo Alto VM-Series Next-Generation Firewalls (NGFWs) into the network account. The NGFWs use the Bring Your Own License (BYOL) deployment image and require you to use the Palo Alto console to upload a VM code and register them. For more instructions, see the README in the [`2-networking-b-il5-ngfw`](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/2-networking-b-il5-ngfw) stage folder.

  1. If you are using an external billing account, see Configure billing when using external billing accounts.

  2. Change directory into [`fast/stages-aw/2-networking-b-il5-ngfw`](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/2-networking-b-il5-ngfw).

  3. Copy the provider and global tfvars files from the Cloud Storage buckets:
         
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/providers/2-networking-providers.tf ./ && \
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/0-globals.auto.tfvars.json ./ && \
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/0-bootstrap.auto.tfvars.json ./ && \
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/1-resman.auto.tfvars.json ./
         

  4. Copy the `terraform.tfvars.sample` file:
         
         cp terraform.tfvars.sample terraform.tfvars
         

  5. In the `terraform.tfvars` file, update the custom subnets (including mgmt), proxy subnets, firewall rules, named CIDRs, and DNS response policy rules.

  6. Run `terraform init`.

  7. Run `terraform apply`. Type `yes` when prompted.

If you receive an error about a service account or Cloud Key Management Service not existing, in the console, click **Settings** in the `PREFIX-net-vdss-host` storage account. The service account is generated.




## Run Stage 3: Security and audit account configuration

Stage 3 configures the security and audit projects. The security project (`prod-sec-core-0`) contains Cloud KMS and can contain Secret Manager. In IL5, CMEK is enabled by default for Compute Engine, Google Kubernetes Engine (GKE), Cloud Storage, and Cloud SQL. The following organization policy constraints are enforced:

  * `gcp.restrictNonCmekServices`: 
    * `denied_values: "compute.googleapis.com"`
    * `denied_values: "container.googleapis.com"`
    * `denied_values: "storage.googleapis.com"`
    * `denied_values: "sqladmin.googleapis.com"`
  * `gcp.restrictCmekCryptoKeyProjects`: `gcp.restrictCmekCryptoKeyProjects` includes a list of projects that can use CMEK.



In the `prod-sec-core-0` project, the following items are configured:

  * Cloud KMS restricted admins are granted the restricted Admin role so that they can grant decrypt permissions to other services.
  * Cloud KMS key rings in different locations are provisioned. The key ring locations must match the service locations. For example, a multi-regional key ring cannot be used in a single region's storage bucket.



The audit project contains a logging bucket for audit logs.

Security administrators are responsible for the security project and auditors are responsible for the audit project.

  1. If you are using an external billing account, see Configure billing when using external billing accounts.

  2. Change directory into [`fast/stages-aw/3-security`](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/3-security).

  3. Copy the configuration files from the Cloud Storage buckets:
         
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/providers/3-security-providers.tf ./ &&
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/0-globals.auto.tfvars.json ./ &&
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/0-bootstrap.auto.tfvars.json ./ &&
         gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/1-resman.auto.tfvars.json ./
         

  4. Run `terraform init`.

  5. Run `terraform apply`. Type `yes` when prompted.

If you encounter an issue with service accounts, rerun `terraform apply`.

  6. Run `./sa_lockdown.sh` to disable the service accounts that you used during deployment.

**Note:** You might be unable to deploy certain blueprints unless the service accounts are enabled. If you are deploying additional services or blueprints into the Stellar Engine environment, don't run this script until your deployments are complete.



## Configure billing when using external billing accounts

If you are using an external billing account, you must add the Billing Account Administrator role to the following service accounts:

  * `PREFIX-prod-resman-0@PREFIX-prod-iac-core-0.iam.gserviceaccount.com`: This account is created in stage 0.

  * `PREFIX-prod-resman-net-0@PREFIX-prod-iac-core-0.iam.gserviceaccount.com`: This service account is created in stage 1.

  * `PREFIX-security-0@PREFIX-prod-iac-core-0.iam.gserviceaccount.com`: This service account is created in stage 2.




To add the role to these service accounts, complete [Access the Permissions panel for a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/grant-access-to-billing#access-permissions-panel) and [Update roles and principals in the Permissions panel](https://docs.cloud.google.com/billing/docs/how-to/grant-access-to-billing#update-roles-principals).

**Note:** If you are using an external billing account where the service account cannot be granted billing permissions, you can use a billing override to run the project creation or billing links using your personal credentials. To use a billing override, define the `billing_override` variable in your `fast/stages-aw/1-resman/terraform.tfvars`: 
    
    
    billing_override = {
      project         = "QUOTA_PROJECT_ID"
      billing_project = "QUOTA_PROJECT_ID"
    }

Replace QUOTA_PROJECT_ID with the project ID for your quota project.

## Modify tenant projects

Perform the following steps when adding or removing tenant projects for an existing Stellar Engine deployment.

  1. Authenticate and set the active project:
         
         gcloud auth login
         gcloud config set project PREFIX-prod-iac-core-0
         gcloud auth application-default login
         

  2. Enable the service accounts for the stages:

     1. Change directory into [`fast/stages-aw/3-security`](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/3-security).

     2. Run `./sa_lockdown.sh --enable`.

  3. Apply Stage 1:

     1. Change directory into [`fast/stages-aw/1-resman`](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/1-resman).

     2. Update the information in `terraform.tfvars` to your new requirements.

     3. Run `terraform init`.

     4. Run `terraform apply`. Type `yes` when prompted.

  4. Apply Stage 2:

     1. Change directory into one of the following network folders:

        * [`fast/stages-aw/2-networking-a-fedramp-high`](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/2-networking-a-fedramp-high)
        * [`fast/stages-aw/2-networking-b-il5-ngfw`](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/2-networking-b-il5-ngfw)
     2. Copy the `1-resman` tfvars file from the Cloud Storage bucket:
    
    gcloud storage cp gs://PREFIX-prod-iac-core-outputs-0/tfvars/1-resman.auto.tfvars.json ./
    

     1. Run `terraform init`.

     2. Run `terraform apply`. Type `yes` when prompted.

  5. Disable the service accounts for the stages:

     1. Change directory into [`fast/stages-aw/3-security`](https://github.com/google/stellar-engine/tree/main/fast/stages-aw/3-security).

     2. Run `./sa_lockdown.sh`.




## Troubleshooting

This section describes some common errors and resolutions.

### BigQuery isn't usable error in stage 1

If you get an error that `bigquery.googleapis.com` isn't usable in Assured Workloads, complete the following:

  1. In the console, go to the Assured Workloads page.

[Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

  2. Select the `StellarEngine-COMPLIANCE_REGIME` folder and Networking folder, if applicable.

  3. Click **Review Available Updates**.

  4. Go to **Allowed Services**.

  5. Click **Allow services** to add the BigQuery APIs.

  6. If prompted, click **Yes** to confirm your choice.

  7. Wait about two minutes and then re-run `terraform apply`:
         
         terraform apply -var bootstrap_user=$(gcloud config list --format 'value(core.account)')
         

  8. Type `yes` when prompted.




### Your bootstrap project loses access to your billing account

If your bootstrap project loses access to your billing account, re-enable billing for your bootstrap project.

[Enable billing](https://console.cloud.google.com/billing/projects)

### Cloud KMS key errors

If key errors occur during the build process, you might have to manually enable the keys. For instructions, see [Enable a key version](https://docs.cloud.google.com/kms/docs/enable-disable#enable).

If you receive these errors, wait about one minute and rerun `terraform apply`.

### Symbolic links not working on Windows computers

On a Windows computer, symbolic links might not work. You might need to copy specific files over manually, specifically `psc.tf` and `log-metric-alerts.tf` during Stage 2.

### Billing or quota issues

If you encounter billing or quota issues, verify that your quota project is set. You can set it by running the following:
    
    
    gcloud auth application-default set-quota-project PREFIX-prod-iac-core-0
    

Optionally, you can use another project.

## What's next

  * For additional security configuration, see [Gemini security standards](https://docs.cloud.google.com/docs/security/compliance/stellar-engine/gemini-considerations).

  * Integrate a SIEM solution such as [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) to monitor the resources. Segment your SIEM in a separate Google Cloud project and on a separate VPC from where it is collecting data.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
