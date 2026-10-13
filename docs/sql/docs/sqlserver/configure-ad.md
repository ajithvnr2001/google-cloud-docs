---
url: https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad/
title: Use Managed Microsoft AD with Cloud SQL \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:57.246226+00:00
---

# Use Managed Microsoft AD with Cloud SQL  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Use Managed Microsoft AD with Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes the ways to use Cloud SQL to:

  * Integrate with Managed Service for Microsoft Active Directory (also called Managed Microsoft AD).
  * Connect to an instance with an AD user.



A Cloud SQL instance that is integrated with Managed Microsoft AD supports [Windows Authentication](https://docs.microsoft.com/windows-server/security/windows-authentication/windows-authentication-overview) in addition to SQL Authentication.

**Note:** Before integrating, review the [ Overview of Managed Microsoft AD in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/ad), including the [ Limitations and alternatives](https://docs.cloud.google.com/sql/docs/sqlserver/ad#limitations-and-alternatives). 

## Before you begin

  1. In the Google Cloud console, [select your project name](https://console.cloud.google.com/projectselector2/home/dashboard).
  2. Make sure that billing is enabled for your Google Cloud project. [Learn how to confirm billing is enabled for your project](https://cloud.google.com/billing/docs/how-to/modify-project).
  3. Install and initialize [the gcloud CLI](https://docs.cloud.google.com/sdk/docs).
  4. Make sure that you have the `Cloud SQL Admin` role on your user account. [Go to the IAM page](https://console.cloud.google.com/iam-admin/iam).
  5. Review the [ prerequisites for integration](https://docs.cloud.google.com/sql/docs/sqlserver/ad#prerequisites-for-integration).



## Create an instance with Windows Authentication

**Note:** If you are integrating with a managed AD domain in a different project, first review the procedures and constraints.

You can integrate with Managed Microsoft AD during [instance creation](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance), enabling Windows Authentication for the instance. To integrate, you choose a domain for the instance to join. If joining a domain fails, instance creation fails.

In preparation for creating an instance with Windows Authentication, review the tips and the [limitations and alternatives](https://docs.cloud.google.com/sql/docs/sqlserver/ad#limitations-and-alternatives).

**Note:** In rare cases, instance creation that includes Windows Authentication can take up to 30 minutes. 

An instance with public IP is supported, as long as it has private IP as well; private IP must be enabled for the instance. Then you can choose to use public IP or private IP to connect to the instance, as long as both are available.

**Note:** After you create an instance with Windows Authentication, an extra Cloud SQL for SQL Server login is created. The login is in the format `[domain]\sql_[letters-and-digits]`. For example, Cloud SQL might create a login named `AD\sql_1a1a6145bc1aaaa`. The login is in the Managed AD domain. You can ignore the login. You can't remove it. However, if you disable Windows Authentication for the instance, the login is automatically deleted. 

The following are the options for creating an instance that is integrated with Managed Microsoft AD.

### Console

**Note:** Before starting the following steps, review the [ prerequisites for integration](https://docs.cloud.google.com/sql/docs/sqlserver/ad#prerequisites-for-integration). Additionally, note the  procedures and constraints for integrating with a managed AD domain in a different project. 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. Click **Choose SQL Server**.
  4. Enter a name for the instance. Do not include sensitive or personally identifiable information in your instance name; it is externally visible. You do not need to include the project ID in the instance name. This is created automatically where appropriate (for example, in the log files).
  5. Enter the password for the `'sqlserver'` [user](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users).
  6. Set the region for your instance. See [ Best practices for integrating with Managed Microsoft AD](https://docs.cloud.google.com/sql/docs/sqlserver/ad#best-practices-for-integrating). 
  7. In the **Configuration options** section, set your desired options (but wait until the next step for the authentication options).
  8. Click **Authentication**. The dropdown menu for joining a managed Active Directory domain lists any [ Managed Microsoft AD domains](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain) that previously were added in your project. 
  9. From the dropdown menu for joining a managed Active Directory domain, select a domain.
  10. When you are finished selecting your configuration options, click **Create**. Cloud SQL automatically creates a Per-Product, Per-Project Service account for you. If the account doesn't have the appropriate role, you are prompted to grant the `managedidentities.sqlintegrator` role.



### gcloud

**Note:** Before starting the following steps, review the [ prerequisites for integration](https://docs.cloud.google.com/sql/docs/sqlserver/ad#prerequisites-for-integration). Additionally, note the  procedures and constraints for integrating with a managed AD domain in a different project. 

The following command creates an instance that is integrated with Managed Microsoft AD and thus is enabled for Windows Authentication. For information about the basic command for creating an instance, see [Creating instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

Specify a parameter of `--active-directory-domain=DOMAIN` in the `gcloud` command. For example, specify the following: `--active-directory-domain=ad.mydomain.com`

Here is a prototype of the `gcloud` command:
    
    
    gcloud beta sql instances create INSTANCE_NAME \
    --database-version=EDITION \
    --root-password=PASSWORD \
    --active-directory-domain=DOMAIN\
    --cpu=CPU \
    --memory=MEMORY  \
    --network=NETWORK

### Terraform

To create an instance that is integrated with Managed Microsoft AD, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "google_sql_database_instance" "instance_with_ad" {
      name             = "database-instance-name"
      region           = "us-central1"
      database_version = "SQLSERVER_2019_STANDARD"
      root_password    = "INSERT-PASSWORD-HERE"
    
      depends_on = [google_service_networking_connection.private_vpc_connection]
    
      settings {
        tier = "db-custom-2-7680"
        active_directory_config {
          domain = "ad.domain.com"
        }
        ip_configuration {
          ipv4_enabled    = "false"
          private_network = google_compute_network.private_network.id
        }
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
    }

### REST

**Note:** Before starting the following steps, review the [ prerequisites for integration](https://docs.cloud.google.com/sql/docs/sqlserver/ad#prerequisites-for-integration). Additionally, note the  procedures and constraints for integrating with a managed AD domain in a different project. 

Using the REST API, you can create an instance that is integrated with Managed Microsoft AD. Specify a domain, such as `subdomain.mydomain.com`, for the `domain` field, as shown in this prototype of a request:
    
    
    {
       "databaseVersion":"database-version",
       "name":"instance-id",
       "region":"region",
       "rootPassword":"password",
       "settings":{
          "tier":"machine-type",
          "ipConfiguration":{
             "privateNetwork":"network"
          },
          "activeDirectoryConfig":{
             "domain":"domain"
          }
       }
    }
    

## Update an instance with Windows Authentication

You can update the domain of an existing instance, changing or adding a domain.

**Caution:** Removing Windows Authentication causes an instance [ to restart](https://docs.cloud.google.com/sql/docs/sqlserver/start-stop-restart-instance#restart). 

For general information about updating an instance, see [Editing instances](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance).

**Note:** Before starting the steps in this section, review the [ prerequisites for integration](https://docs.cloud.google.com/sql/docs/sqlserver/ad#prerequisites-for-integration) and the [ best practices](https://docs.cloud.google.com/sql/docs/sqlserver/ad#best-practices-for-integrating). 

If an instance is currently joined with a Managed AD domain, the instance is initially unjoined from that domain, before it is joined to the new domain. If the update fails, the instance may no longer be joined to any domain.

**Note:** An instance with public IP is supported, as long as it has private IP as well; private IP must be enabled for the instance. Then you can choose to use public IP or private IP to connect to the instance, as long as both are available. 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. Click **Authentication**. The **Join an Active Directory domain** dropdown menu lists the [ Managed Microsoft AD domains](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain) that previously were added in your project.
  5. From the dropdown menu for joining a managed Active Directory domain, select a new (replacement) domain for your instance.
  6. Click **Save** to apply your changes.



### gcloud

The following is a prototype of a command to update an existing instance. The command either adds or replaces a domain. Pass `--active-directory-domain=DOMAIN` to the command, as follows:
    
    
    gcloud beta sql instances patch INSTANCE_NAME \
    --active-directory-domain=DOMAIN

### REST

Using the REST API, you can update an existing instance. Specify a domain, such as `subdomain.mydomain.com`, in the `domain` field. The following is a prototype of a request:
    
    
    {
       "settings":{
          "activeDirectoryConfig":{
             "domain":"domain"
          }
       }
    }
    

## Integrate with a managed AD domain in a different project

You can integrate your instance with a Managed Microsoft AD domain that is in a different project.

**Note:** Integrating with an AD domain in a different project requires use of `gcloud` commands or the Cloud SQL REST API. Currently, you can't use the Google Cloud console for this purpose.

While planning your integration, review the constraints.

### Enable domain peering

Before proceeding with the steps in the sections below, [enable domain peering](https://cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-peering) so your domain is available to all necessary projects with Cloud SQL for SQL Server instances.

For a list of domains from other projects that already are available, you can specify the following:
    
    
    `gcloud active-directory peerings list`

For more information, see [List domain peerings](https://cloud.google.com/managed-microsoft-ad/docs/list-describe-delete-domain-peering#list_domain_peerings).

The `gcloud active-directory peerings list` command requires the `managedidentities.peerings.list` permission. The following roles have this permission:

  * `roles/managedidentities.peeringViewer`
  * `roles/managedidentities.viewer`



For more information, see [Access control with IAM](https://cloud.google.com/managed-microsoft-ad/docs/access-control).

### Create a service account

Repeat these steps for each project that contains a Cloud SQL for SQL Server instance that you intend to integrate.

  1. Review the [background information for creating service accounts](https://docs.cloud.google.com/sql/docs/sqlserver/ad#creating-a-service-account).
  2. Use a command similar to the following to create a service account. Specify the ID of the project containing Cloud SQL for SQL Server instances:
         
         gcloud beta services identity create --service=sqladmin.googleapis.com \
         --project=[PROJECT_ID]

  3. Grant the `managedidentities.sqlintegrator` role in the project with the Managed Microsoft AD instance. Specify the ID of the project containing the Managed Microsoft AD instance:
         
         gcloud projects add-iam-policy-binding [PROJECT_ID] \
         --member=serviceAccount:SERVICE_ACCOUNT --role=roles/managedidentities.sqlintegrator




### Enable cross-project Windows authentication

You can integrate with an AD domain in a different project using `gcloud` commands or the Cloud SQL REST API. In either case, you must specify the full domain resource name.

Specify the full domain resource name when a Cloud SQL for SQL Server instance is created or updated. Two formats are supported:

  * `projects/PROJECT_ID/locations/global/domains/DOMAIN_NAME`
  * `projects/PROJECT_NUMBER/locations/global/domains/DOMAIN_NAME`



Here is an example using `gcloud`:
    
    
    gcloud beta sql instances patch INSTANCE_NAME \
    --active-directory-domain=projects/PROJECT_ID/locations/global/domains/DOMAIN_NAME

If you use a short domain resource name (such as `DOMAIN_NAME`), the system assumes that your Managed Microsoft AD domain is in the same project as your Cloud SQL for SQL Server instances.

### Constraints for integrating with different projects

If you are integrating with a managed AD domain in a different project, the following constraints apply:

  * Up to 10 networks with Cloud SQL for SQL Server instances can share one Managed Microsoft AD instance located in a different project.
  * The Google Cloud console only supports Managed Microsoft AD instances located in the same project. Instead of using the Google Cloud console, you can integrate using `gcloud` commands or the Cloud SQL REST API.
  * If VPC Service Controls are used, Cloud SQL for SQL Server instances and a Managed Microsoft AD instance must be located in the same perimeter.



Additionally, if an instance is integrated with a managed AD domain in a different project, the fully qualified domain name (FQDN) shown in the Google Cloud console might be inaccurate for that instance. Specifically, on the **Overview** page for that instance, under **Connect to this instance** , the FQDNs might contain strings separated by slashes, which you can ignore. For example, an inaccurate FQDN might be shown as:
    
    
    private.myinstance.myregion.myproject.projects/mydirectory/locations/global/domains/mydomain.com

In that case, the accurate FQDN is: 
    
    
    private.myinstance.myregion.myproject.cloudsql.mydomain.com

## Remove Windows Authentication from an instance

You can remove Windows Authentication, and thus a Managed Microsoft AD integration, from an existing instance.

**Caution:** Removing Windows Authentication causes an instance [to restart](https://cloud.google.com/sql/faq#shutdown). 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. Click **Authentication**. The dropdown menu for joining a managed Active Directory domain lists the [ Managed Microsoft AD domains](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain) that previously were added in your project.
  5. From the dropdown menu, select **No domain/Join later** for your instance.
  6. Read the message about instance restart, and click **Close**. 
  7. Click **Save** to apply your changes.



### gcloud

To remove an instance from a domain, thus removing Windows Authentication, use a blank value for the domain. That is, in your command, use a blank value for the`--active-directory-domain` parameter, as follows:
    
    
    gcloud beta sql instances patch INSTANCE_NAME \
    --active-directory-domain=

### REST

Using the REST API, you can remove an instance from a domain. Specify a blank value in the `domain` field, as follows:
    
    
    {
       "settings":{
          "activeDirectoryConfig":{
             "domain":""
          }
       }
    }
    

## Connect to an instance with a user

For Cloud SQL for SQL Server, the default [user](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users) is `sqlserver`.

After you integrate an instance with Managed Microsoft AD, you can connect to the instance with the `sqlserver` user, as follows:

  1. Create a SQL Server login based on a Windows user or group, as follows:
         
         CREATE LOGIN [domain\user_or_group] FROM WINDOWS

  2. Log in to the instance, using Windows Authentication, with the instance DNS name. Examples of instance DNS names to specify are the following:

     * To connect through private IP: 
           
           private.myinstance.us-central1.myproject.cloudsql.mydomain.com

     * To connect via public IP: 
           
           public.myinstance.us-central1.myproject.cloudsql.mydomain.com

     * To connect via the Cloud SQL Auth Proxy (also see below): 
           
           proxy.myinstance.us-central1.myproject.cloudsql.mydomain.com

If you use the instance IP address, you must [configure](https://docs.microsoft.com/en-us/windows-server/security/kerberos/configuring-kerberos-over-ip) the Kerberos clients. to support IP hostnames. Cloud SQL doesn't support logins from domains connected through a trust relationship.


**Note:** Cloud SQL doesn't support this connection functionality from domains connected using a trust relationship. For such domains, see  On-premises AD users: Creating a Windows login. 

## Use the Cloud SQL Auth Proxy with Windows Authentication

You can use the Cloud SQL Auth Proxy with your Managed Microsoft AD integration.

Before you begin, review:

  * [About the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy)

  * [Connecting using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy)




### Steps for Windows Authentication

For background on starting the Cloud SQL Auth Proxy, see [Start the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy#start-proxy).

For Windows Authentication, you must run the Cloud SQL Auth Proxy on port 1433. To map a predefined Service Principal Name (SPN) entry to a Cloud SQL Auth Proxy address, use:
    
    
    proxy.[instance].[location].[project].cloudsql.[domain]

#### Run the Cloud SQL Auth Proxy locally

If you run the Cloud SQL Auth Proxy locally, use your hosts file to map the following to `127.0.0.1`:
    
    
    proxy.[instance].[location].[project].cloudsql.[domain]

As an example, you could add the following to the hosts file (for example, to `c:\windows\system32\drivers\etc\hosts`):
    
    
    127.0.0.1 proxy.[instance].[location].[project].cloudsql.[domain]

In that example, you could run the Cloud SQL Auth Proxy using this command, and make it available on `127.0.0.1:1433`:
    
    
    cloud-sql-proxy.exe --credentials-file credential.json project:name

#### Run the Cloud SQL Auth Proxy non-locally

To run the Cloud SQL Auth Proxy non-locally, follow the instructions in Running the Cloud SQL Auth Proxy locally, but use a different entry in the hosts file.

Specifically, if a non-local host is, for example, `MyOtherHost`, you could add the following to the hosts file:
    
    
    127.0.0.1 MyOtherHost proxy.[instance].[location].[project].cloudsql.[domain]

## Troubleshoot for NTLM fallback in clients

If you use Windows Authentication and an instance IP address to log in to an instance, you must [configure](https://docs.microsoft.com/en-us/windows-server/security/kerberos/configuring-kerberos-over-ip) a Kerberos client to support IP hostnames.

Cloud SQL doesn't support NTLM authentication, but some Kerberos clients might try to fall back to it. As discussed in this section, if you try to connect with SQL Server Management Studio (SSMS), and the following error message occurs, a likely cause is NTLM fallback:
    
    
    Login failed. The login is from an untrusted domain and cannot be used with Integrated authentication. (Microsoft SQL Server, Error: 18452)

NTLM is a set of Microsoft security protocols for authentication. Also see Reasons for NTLM fallback.

### Verification of an NTLM fallback for a Windows client

From Windows, to verify that an NTLM fallback caused an error::

  1. Log in with the desired on-premises credentials (do not use "Run as...").
  2. Open a command prompt.
  3. Run `klist purge`.
  4. From SSMS, try to connect to SQL Server with Windows Authentication.
  5. Run `klist` and check if there's a ticket issued for `"MSSQLSvc/<address>:1433 @ domain"`.
  6. If there's no such ticket, NTLM fallback is the likely cause for the error.
  7. If there is such a ticket, check that your SQL Server driver doesn't enforce NTLM authentication. Also check if NTLM authentication is enforced via Group Policy.



### Verification of an NTLM fallback for a Linux client

From Ubuntu 16.04, to verify that an NTLM fallback caused an error, use the steps in this section. The steps are similar as those for other Linux distributions.

#### Set up Kerberos authentication

  1. Set up a Kerberos client:
         
         sudo apt-get install krb5-user
         

  2. When you are prompted for the default realm, type an on-premises domain name in uppercase letters.

  3. Run the following to install SQL Server command-line tools:
         
         curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
         curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list
         sudo apt-get update
         sudo apt-get install mssql-tools unixodbc-dev
         




#### Connect with Windows Authentication

  1. Run the kinit tool as follows: `kinit <user_account>`
  2. To connect with Windows Authentication, run: `/opt/mssql-tools/bin/sqlcmd -S <address >>`
  3. Run the `klist` command and check whether a ticket was issued specifically for: `"MSSQLSvc/<address>:1433 @ domain"`
  4. If the ticket wasn't issued, the above error likely indicates an issue that causes NTLM fallback.



### Reasons for NTLM fallback

Fallback onto NTLM is a client misconfiguration that can be associated with the following conditions:

  * By default, Windows doesn't attempt Kerberos authentication for a host if the hostname is an IP address. To enable Kerberos authentication from the managed domain, try the method described in the [Microsoft documentation](https://docs.microsoft.com/en-us/windows-server/security/kerberos/configuring-kerberos-over-ip). This method doesn't work with on-premises credentials when you must use FQDNS.
  * Kerberos authentication over external trusts doesn't work. Use forest trusts instead, as described [here](https://cloud.google.com/managed-microsoft-ad/docs/create-trust).
  * Kerberos authentication requires name suffix routing to enable the finding of services in another forest. Try the method described [here](https://cloud.google.com/managed-microsoft-ad/docs/manage-trusts).
  * Kerberos authentication doesn't work if there's no SPN registered for the service. Use only FQDNs or IP addresses you obtain from the Google Cloud console to connect with Windows Authentication.



## On-premises AD users: Creating a Windows login

**Note:** Using an on-premises AD user to create a Windows login isn't recommended. Instead, use a Managed AD user or a `sqlserver` account in Cloud SQL.

You can use an on-premises AD user to create a Windows login to Cloud SQL for SQL Server.

As an example, you can connect using SQL Server Management Studio (SMSS) running on a Windows VM hosted in your Google Cloud project's Virtual Private Cloud (VPC).

For Windows Authentication in this context, Cloud SQL for SQL Server only supports the Kerberos protocol. For Kerberos-based Windows Authentication, the client must resolve the DNS name of the on-premises AD and the Managed Microsoft AD.

### Configure one-way or two-way trust

Initially, decide whether to use a [one-way or two-way trust relationship](https://cloud.google.com/managed-microsoft-ad/docs/create-trust). **Note:** We strongly recommend that you use a two-way trust relationship between a Managed AD domain and an on-premises domain because one-way trust instances might experience long-running connection drops and can't run certain privileged operations, such as create and drop login. For more information, see [Understand Active Directory authentication for SQL Server on Linux and containers](https://learn.microsoft.com/th-th/sql/linux/sql-server-linux-ad-auth-understanding?view=sql-server-2017#sql-server-group-refresh). 

Then, follow the [instructions for establishing trust](https://cloud.google.com/managed-microsoft-ad/docs/create-trust#before_you_begin) between the on-premises AD domain and the Managed Microsoft AD domain.

### Set up a Windows VM and create a Windows login

After you establish trust between the on-premises AD domain and the Managed Microsoft AD domain, complete the following steps. For example purposes, these steps use SQL Server Management Studio (SSMS), running on a Windows VM, hosted in your Google Cloud project's VPC:

  1. Create a Windows VM. 
     * [Create a VM](https://cloud.google.com/compute/docs/create-windows-server-vm-instance#create_a_virtual_machine_instance) with a [version of Windows supported by Managed Microsoft AD](https://cloud.google.com/managed-microsoft-ad/docs/os-versions#windows-domain-join).
     * Create the VM in the project that hosts your Managed Microsoft AD domain. If there is a Shared VPC that is an authorized network, you can also create the VM in any of its service projects.
     * Create the VM on a VPC network that is an authorized network of the Managed Microsoft AD domain and has configured private service access for Cloud SQL.
  2. [Join](https://cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-windows) the Windows VM to the Managed Microsoft AD domain.
  3. [Install SSMS](https://docs.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms) on the Windows VM.
  4. Resolve the on-premises domain in the VPC network. 
     * From the authorized network on which the Windows VM is running, enable on-premises DNS resolution using the steps on the [Resolve queries for non-Managed Microsoft AD objects](https://cloud.google.com/managed-microsoft-ad/docs/resolve-non-managed-objects-vpc) page. The steps on that page are prerequisites for Kerberos-based Windows Authentication to work for on-premises users.
  5. Create a Windows login for an on-premises user.

     * Follow the [CREATE LOGIN instructions](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-login-transact-sql?view=sql-server-ver15) for creating a Windows login for an on-premises user. For example, specify a command similar to the following:
    
    CREATE LOGIN [DOMAIN_NAME\USER_NAME] FROM WINDOWS
    

  6. Log in to your Cloud SQL for SQL Server instance using the application-specific instructions for logging in an on-premises user. For example, if you are using SQL Server Management Studio, refer to [these instructions](https://docs.microsoft.com/sql/ssms/tutorials/connect-query-sql-server).




### Resolve problems related to an on-premises AD user

If a problem occurs during a login to a Cloud SQL for SQL Server instance, perform these verifications:

  * Verify the firewall configurations of the on-premises network and project-authorized VPC, using the instructions for [creating a trust with an on-premises domain](https://cloud.google.com/managed-microsoft-ad/docs/create-one-way-trust).
  * Verify the [Name Suffix Routing](https://cloud.google.com/managed-microsoft-ad/docs/manage-trusts#name-suffix-routing) for the on-premises trust relationship.
  * Verify that you can perform these DNS resolution operations from the Windows VM that is running SSMS: 
    * `nslookup fqdn-for-managed-ad-domain`
    * `nslookup fqdn-for-on-premises-ad-domain`
    * `nslookup fqdn-for-cloud-sql-server-instance`



## Tips

**Note:** In addition to reviewing the tips in this section, see [ Limitations and alternatives](https://docs.cloud.google.com/sql/docs/sqlserver/ad#limitations-and-alternatives). 

  * An instance with public IP is supported, as long as it has private IP as well; private IP must be enabled for the instance. Then you can choose to use public IP or private IP to connect to the instance, as long as both are available.
  * Before creating an instance, including as a replacement instance, review the following as needed: 
    * [ Learn about using private IP](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip)
    * [ Configure public IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip)
  * [Terraform](https://cloud.google.com/docs/terraform) is supported.
  * If you receive one of the following errors, confirm that you have met all of the [ prerequisites for integration](https://docs.cloud.google.com/sql/docs/sqlserver/ad#prerequisites-for-integration): 
    * "Per-Product Per-Project Service Account is not found"
    * "Insufficient permission to integrate with Managed Service for Microsoft Active Directory domain"
  * If you receive the error "Domain not found", verify that the case-sensitive domain name is correct.
  * If Windows Authentication fails from a domain that is connected through a trust relationship, verify that Windows Authentication works for a user from a managed domain. If it does, then: 
    1. Verify that you used a DNS name. IP addresses aren't supported from domains connected using a trust relationship.
    2. Ensure that you followed [all of the steps for creating a trust with an on-premises domain](https://cloud.google.com/managed-microsoft-ad/docs/create-trust), including the opening of all firewall ports.
    3. [Validate](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/validate-state) the trust.
    4. Verify that the direction of the trust allows users from the domain (connected through a trust relationship) to authenticate in the managed domain.
    5. [Verify](https://cloud.google.com/managed-microsoft-ad/docs/manage-trusts) that the name suffix routing is set on the domain that is connected through a trust relationship.
    6. Verify that the trust works without using Cloud SQL for SQL Server: 
       1. Create a Windows VM.
       2. Join it to the Managed Microsoft AD domain.
       3. Try to run, for example, Notepad as a user from the domain that is connected through a trust relationship.
    7. Restart the client VM and retest Windows Authentication.
  * You may try to create a SQL Server login, but then receive the following error: "Windows NT user or group domain\name not found. Check the name again". This may have occurred because domain local groups are not supported; if applicable, use global or universal groups instead.
  * When issued by a user from a domain connected through a trust relationship, SQL Server queries can result in the following error: "Could not obtain information about Windows NT group/user". This error can occur, for example, if you are creating logins from domains connected through a trust relationship. The error also can occur if you are granting privileges to logins from domains connected through a trust relationship. In these cases, retrying the operation is often successful. If retrying fails, close the connection and open a new connection.
  * If you get an error "Could not obtain information about Windows NT group/user", check the network connectivity to on-premises domains using the log file `active_directory.log` available in Cloud Logging for the Cloud SQL for SQL Server instance. This file contains the following diagnostics regarding connectivity changes to the on-premises domain:

**Note:** The timestamps in the file are in local time.
    * Trusted on-premises domains by the Cloud SQL for SQL Server instance. For example, the following log shows the change from no trusted domains to two new trusted domains as their NetBIOS names, `ONPREM` and `CHILD`: 
          
          2023-06-12 20:55:09.975 Detected change in trusted onprem domains: Previously trusted onprem domains: []. Current trusted onprem domains: [ONPREM CHILD]

If an on-premises domain is not listed or is logged as not trusted, then check if the trust exists with the Managed AD domain and is validated. If there is a one-way trust between the Managed AD domain and on-premises domain, other on-premises domains trusted by the on-premises domain might not be visible.
    * Reachable and unreachable on-premises domains using a regular ping from the Cloud SQL for SQL Server instance. For example, the following log shows the change from no reachable domains to two new reachable domains, `onprem.com` and `child.onprem.com`: 
          
          2023-06-12 20:55:10.664 Detected change in reachable onprem domains: Previously reachable onprem domains: []. Current reachable onprem domains: [onprem.com child.onprem.com]

If a domain is not listed in reachability logs, then ensure that it is logged as a trusted domain first. Otherwise, it is not checked for reachability. We always have a VPC peering between a project with on-premises instances and Google Cloud projects. Having even one more VPC peering introduces transitive peering connection, which Cloud SQL doesn't support. Instead, we recommend that you use a VPN tunnel to connect an on-premises domain to Cloud SQL. There should be at most one peering connection between the on-premises project and the Google Cloud project with the Cloud SQL for SQL Server instances.
    * Successful and unsuccessful [Microsoft remote procedure call (MSRPC)](https://learn.microsoft.com/en-us/windows/win32/rpc/rpc-start-page) pings to on-premises domains from the Cloud SQL for SQL Server instance. For example, the following log shows the change from having no MSRPC pingable domains to two new MSRPC pingable domains, `ONPREM` and `CHILD`: 
          
          2023-06-12 20:55:10.664 Detected change in MSRPC pingable domains: Previously pingable onprem domains: []. Current pingable onprem domains: [ONPREM CHILD]

MSRPC pings are included as additional diagnostics and they might not work on some configurations. You can still verify on-premises domain connectivity through the first two diagnostics.
  * If SQL Server queries result in the error, "The login is from an untrusted domain", note that IP addresses aren't supported for users from domains connected through a trust relationship. Additionally, the following actions may resolve this issue:

    * If an IP address is used to connect users from a managed domain, follow [these instructions](https://docs.microsoft.com/en-us/windows-server/security/kerberos/configuring-kerberos-over-ip).
    * Avoid using any proxies, and always use the same DNS name to connect to Cloud SQL for SQL Server, as you see the name in the Google Cloud console.
    * Purge the existing Kerberos tickets. The above error might occur if you had a client that recently was connected to a Cloud SQL for SQL Server instance and the instance was stopped and started. Alternatively, the error might occur if Windows Authentication was disabled and then re-enabled for the Cloud SQL for SQL Server instance. If the client uses the Windows credentials cache, then lock and unlock the client workstation, or run `klist purge`.
  * An attempt to enable Windows Authentication may result in the error, "This instance would need a more recent creation date to support Managed Service for Microsoft Active Directory." Note the following about this error:

    * In Cloud SQL, if a Cloud SQL for SQL Server instance was created on or before March 12, 2021, it cannot be integrated with Managed Microsoft AD.
    * In certain cases, if you create a Cloud SQL for SQL Server instance and do not enable Managed Microsoft AD at creation, you may receive the same error. After you review the other tips in this section, create a new instance, enabling Managed Microsoft AD at the time you create the instance.
  * An attempt to create a Cloud SQL for SQL Server instance may result in the error, "This instance does not support Managed Service for Microsoft Active Directory." If you receive this error, the project may be unsupported; try using a different project.

  * If an instance has ongoing problems with Windows Authentication (whether or not the instance was recently updated), try unjoining the managed Active Directory domain and then rejoining it. To do so, use the update procedure to unjoin and then to rejoin the domain. Doing so doesn't remove any existing Windows-authenticated users or logins that exist in your databases. However, removing Windows Authentication causes an instance [to restart](https://cloud.google.com/sql/faq#shutdown).

  * [Use the AD diagnosis tool](https://docs.cloud.google.com/sql/docs/sqlserver/ad-diagnosis-tool) to troubleshoot AD setup issues with your on-premises domain and Cloud SQL for SQL Server instances in Google Cloud console.




## Troubleshoot

Click the links in the table for details:

For this error... | The issue might be... | Try this...  
---|---|---  
`Per-product, per-project service account not found.` | The service account name is incorrect. | On the [ Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts), ensure that you created a service account for the correct user project.  
`Insufficient permission to integrate with Managed Service for Microsoft Active Directory domain.` | The `managedidentities.sqlintegrator` role is missing on the service account. | From the [ IAM and Admin page](https://console.cloud.google.com/iam-admin/iam/project), add the `managedidentities.sqlintegrator` role on your service account.   
`Domain not found`. | The domain does not exist or was mistyped. | Ensure the domain name is correct. It is case sensitive.  
`The domain is busy with another operation. Please retry.` | Another Cloud SQL instance is running an operation on the same Managed Active Directory domain. | Retry the operation. If you are performing a batch of updates to Cloud SQL instances connected to the same domain, limit how many are performed in parallel.  
`The operation completed but an update to Active Directory failed. You may experience issues with Windows Authentication on this instance, please see [ https://cloud.google.com/sql/docs/sqlserver/configure-ad](https://cloud.google.com/sql/docs/sqlserver/configure-ad) for tips`. | The required updates could not be performed on the Managed Active Directory domain. | If you experience issues with Windows Authentication, you can try unjoining the managed Active Directory domain and then rejoining it. To do so, use the  update procedure to unjoin and then to rejoin the domain. Doing so doesn't remove any existing Windows-authenticated users or logins that exist in your databases. However, removing Windows Authentication causes an instance [to restart](https://cloud.google.com/sql/faq#shutdown).  
`This instance would need a more recent creation date to support Managed Service for Microsoft Active Directory.` | In Cloud SQL, if a Cloud SQL for SQL Server instance was created on or before March 12, 2021, it cannot be integrated with Managed Microsoft AD. | Try your operation on an instance created after March 12, 2021.  
  
## What's next

  * Confirm that you have fully reviewed the [ overview page](https://docs.cloud.google.com/sql/docs/sqlserver/ad), which includes limitations and unsupported features. That page also includes links to additional documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
