---
url: https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure/
title: Configure VMs to install Debian packages \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:42.376763+00:00
---

# Configure VMs to install Debian packages  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Configure VMs to install Debian packages Stay organized with collections  Save and categorize content based on your preferences. 

Configuring virtual machine (VM) instances to connect to an Artifact Registry Apt repository lets you install and update Debian packages using standard Apt tools. You can set up authentication and repository sources for Compute Engine VMs to pull packages from private or public repositories.

## Before you begin

If the target Apt repository doesn't exist, create a [standard](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) or [remote](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo) repository. You can create a private repository, or a public repository that doesn't require authentication. 

## Prepare a VM to access an Apt repository

###  Private repository 

  1. Choose the service account you will use to grant access.

     * For Compute Engine VMs, this might be the [default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). Artifact Registry automatically retrieves Compute Engine VM service account credentials for any VM using a service account.
     * For other VMs, [create](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) or choose a service account to act on behalf of your VM. You will need the location of the service account key file to configure the VM. You can view and create keys for existing accounts on the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page.
  2. [Grant repository access permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#compute) to your service account.

  3. Prepare the VM to access the repository.

###  Compute Engine VM 

###  Debian VM 

     1. Assign [`cloud-platform` API access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) to the VM. For information about setting access scopes, see [Changing the service account and access scopes for an instance](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes).

     2. Update Apt using the following command:
            
            sudo apt update
            

     3. Install the `apt-transport-artifact-registry` package on the VM:
            
            sudo apt install apt-transport-artifact-registry
            

###  Ubuntu VM 

     1. Install the Apt repository signing keys, using the following command:
            
            curl https://LOCATION-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/artifact-registry.gpg && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/google-cloud-sdk.gpg
            

Replace `LOCATION` with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 

     2. Assign [`cloud-platform` API access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) to the VM. For information about setting access scopes, see [Changing the service account and access scopes for an instance](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes).

     3. Configure your VM to access Artifact Registry packages using the following command:
            
            echo 'deb http://packages.cloud.google.com/apt apt-transport-artifact-registry-stable main' | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
            

     4. Update Apt using the following command:
            
            sudo apt update
            

     5. Install the `apt-transport-artifact-registry` package on the VM:
            
            sudo apt install apt-transport-artifact-registry
            

###  Other VM 

     1. Install the Apt repository signing keys, using the following command:
            
            curl https://LOCATION-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/artifact-registry.gpg && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/google-cloud-sdk.gpg
            

Replace `LOCATION` with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 

     2. Configure your VM to access Artifact Registry packages using the following command:
            
            echo 'deb http://packages.cloud.google.com/apt apt-transport-artifact-registry-stable main' | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
            

     3. Update Apt using the following command:
            
            sudo apt update
            

     4. Install the `apt-transport-artifact-registry` package on the VM:
            
            sudo apt install apt-transport-artifact-registry
            

     5. Find the `#Service-Account-JSON "/path/to/creds.json";` line in the `/etc/apt/apt.conf.d/90artifact-registry` file, then uncomment the line and add the path of your service account key.

Config file entry:
            
            Service-Account-JSON  "PATH_TO_SERVICE_ACCOUNT_KEY";
            

Replace `PATH_TO_SERVICE_ACCOUNT_KEY` with the path to your service account key JSON file.




###  Public repository 

  1. [Configure public access](https://docs.cloud.google.com/artifact-registry/docs/access-control#public) to the repository.

  2. If you're configuring a VM outside of Google Cloud, prepare your machine to access the repository. If you're configuring a Compute Engine VM, proceed to the next step.

Install the public signature verification key, using the following command:
         
         curl https://LOCATION-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/artifact-registry.gpg
         

Replace `LOCATION` with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 

  3. Update Apt using the following command:
         
         sudo apt update
         




## Configure a VM to access a standard Apt repository

Configure a VM to access an Apt repository:

  1. Generate the VM configuration command by running the [`gcloud beta artifacts print-settings apt` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/print-settings/apt):
         
         gcloud beta artifacts print-settings apt \
             --repository=REPOSITORY \
             --location=LOCATION
         

Replace the following:

     * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
     * `REPOSITORY` is the name of the Artifact Registry repository.

The output is similar to the following:
    
    # To configure your package manager with this repository:
    
    # Update Apt:
    sudo apt update
    
    # Install the Apt credential helper:
    sudo apt install apt-transport-artifact-registry
    
    # Configure your VM to access Artifact Registry packages using the following
    # command:
    
    echo "deb [signed-by=/etc/apt/trusted.gpg.d/artifact-registry.gpg] ar+https://LOCATION-apt.pkg.dev/projects/PROJECT REPOSITORY main" | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
    
    # Update Apt:
    sudo apt update
    

  2. Configure Apt to fetch packages from your repository using the `echo` command from the output of the `print-settings` command.

For example, to install packages from the public repository `my-repo` in the project `my-project` and in the location `us-west1`, use the following command:
         
         echo 'deb ar+https://us-west1-apt.pkg.dev/projects/my-project my-repo main'
         

  3. Update your repository sources with the following command:
         
         sudo apt update
         




Apt can now connect to the repository.

If you create additional Apt repositories, you can add them to the `artifact-registry.list` file and then rerun `sudo apt update` to update repository sources.

## Configure a VM to access a remote Apt repository

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To configure a VM to only use a remote Apt repository instead of a standard upstream Apt repository, replace the standard repository with your remote repository in the VM's `/etc/apt/sources.list` file.

**Warning:** re-ordering and deleting repositories from the `sources.list` file can have serious consequences. If you're not sure you want to remove the standard repository, you can configure Apt to use a remote Apt repository as a backup.

  1. Grant project wide Artifact Registry write permissions to the default Compute Engine service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
            --role=roles/artifactregistry.writer
         

  2. Go to the [VM instances page](https://console.cloud.google.com/compute/instances).

  3. In the row with your VM, click **SSH**.

A new window opens with a terminal session on the VM.

  4. Open the VM's `/etc/apt/sources.list` file and locate the standard repository you want to replace with your new remote repository.

  5. Delete the standard repository line, and replace it with the following:
         
         deb ar+https://LOCATION-apt.pkg.dev/remote/PROJECT_ID/REMOTE_REPOSITORY_NAME UPSTREAM_REPOSITORY_NAME COMPONENTS
         

Replace the following:

     * `LOCATION` with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the remote repository.
     * `PROJECT_ID` with the project ID of the VM.
     * `REMOTE_REPOSITORY_NAME` with the name you gave your remote repository.
     * `UPSTREAM_REPOSITORY_NAME` with the name of the upstream repository for your remote.
     * `COMPONENTS` with a whitespace separated list of component names.

For example, the following configures the VM to fetch packages from the repository `my-repo` in the project `my-project` in location `us-east1` using `stable` as the upstream repository for components `main`, `contrib`, and `non-free`.
    
    deb ar+https://us-east1-apt.pkg.dev/remote/my-project/my-repo stable main contrib non-free
    

  6. Update your repository sources with the following command:
         
         sudo apt update
         

Apt can now connect to the repository.




### Use a remote Apt repository as a backup

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you want to keep the standard upstream as the first option and add the remote repository as a fall-back option, you can keep the standard upstream in the `sources.list` file, and either append the remote repository to the end of the `sources.list` file, or create a new list in the `sources.list.d` folder.

To create a new `artifact-registry.list` file in the `sources.list.d`folder, run the following command:
    
    
    echo 'deb ar+https://LOCATION-apt.pkg.dev/remote/PROJECT_ID/REMOTE_REPOSITORY_NAME UPSTREAM_REPOSITORY_NAME COMPONENTS' | sudo tee -a  /etc/apt/sources.list.d/artifact-registry.list
    

Replace the following:

  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
  * `PROJECT_ID` with the project ID of the VM.
  * `REMOTE_REPOSITORY_NAME` with the name you gave your remote repository.
  * `UPSTREAM_REPOSITORY_NAME` with the name of the upstream repository for your remote.
  * `COMPONENTS` with a whitespace separated list of component names.



If you create additional Apt repositories, you can add them to the `artifact-registry.list` or `sources.list` file and then rerun `sudo apt update` to update repository sources. 

## Configure HTTP access to an Apt repository

If using older client tools that don't support SSL encryption, you can configure public access to your Apt repository and access it via HTTP. Requests sent to public readable repositories using HTTP will be rejected if an authentication token is presented with the request.

  1. [Configure public access](https://docs.cloud.google.com/artifact-registry/docs/access-control#public) to the repository.

**Note:** HTTP access is only enabled for publicly readable repositories.
  2. To configure Apt to fetch packages from your repository using HTTP, run the following command:
         
         echo 'deb http://LOCATION-apt.pkg.dev/projects/PROJECT_ID \
          REPOSITORY main' | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
         

Replace the following:

     * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
     * `PROJECT_ID` is the project ID of the repository.
     * `REPOSITORY` is the repository name.

For example, to install packages from the public repository `my-repo` in the project `my-project` and in the location `us-west1` using HTTP, use the following command:
    
    echo 'deb http://us-west1-apt.pkg.dev/projects/my-project my-repo main' | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
    

  3. Update your repository sources with the following command:
         
         sudo apt update
         




Apt can now connect to the repository.

If you create additional Apt repositories, you can add them to the `artifact-registry.list` file and then rerun `sudo apt update` to update repository sources.

## What's next

  * [Learn about managing Debian packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/manage-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
