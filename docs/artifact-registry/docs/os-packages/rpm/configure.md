---
url: https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure/
title: Configure VMs to install RPM packages \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:43.071952+00:00
---

# Configure VMs to install RPM packages  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Configure VMs to install RPM packages Stay organized with collections  Save and categorize content based on your preferences. 

This page describes configuring VMs to install RPM packages from an Artifact Registry Yum repository. Artifact Registry Yum repositories support `yum` and `dnf` clients.

## Before you begin

If the target Yum repository does not exist, [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos). You can create a private repository or a public repository that does not require authentication.

## Prepare a VM to access a Yum repository

To prepare a VM to access a Yum repository, use the `yum` or `dnf` client tool:

###  Private repository 

  1. Choose the service account you will use to grant access.

     * For Compute Engine VMs, this might be the [default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). Artifact Registry automatically retrieves Compute Engine VM service account credentials for any VM using a service account.
     * For other VMs, [create](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) or choose a service account to act on behalf of your VM. You will need the location of the service account key file to configure the VM. You can view and create keys for existing accounts on the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page.
  2. [Grant repository access permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#compute) to your service account.

  3. Prepare the VM to access the repository.

###  Compute Engine VM 

     1. Assign [`cloud-platform` API access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) to the VM. For information about setting access scopes, see [Changing the service account and access scopes for an instance](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes).

     2. Update the package cache using the following command:
            
            sudo yum makecache
            

     3. Install the Artifact Registry plugin on the VM, using the following command:
            
            sudo yum install FORMAT-plugin-artifact-registry
            

Replace the following:

        * `FORMAT` with one of the following: 
          * `yum`, if your operating system is Enterprise Linux 7 or earlier
          * `dnf`, if your operating system is Enterprise Linux 8 or later

###  Other VM 

     1. Install the RPM signing key using the following command:
            
            sudo rpm --import https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
            

     2. Create a file named `/etc/yum.repos.d/artifact-registry-plugin.repo` with the following contents:
            
            [ar-plugin]
            name=Artifact Registry Plugin
            baseurl=https://packages.cloud.google.com/yum/repos/FORMAT-plugin-artifact-registry-DISTRO-stable
            enabled=1
            gpgcheck=1
            

Replace the following:

        * `FORMAT` with one of the following: 
          * `yum`, if your operating system is Enterprise Linux 7 or earlier
          * `dnf`, if your operating system is Enterprise Linux 8 or later
        * `DISTRO` with the Red Hat Enterprise Linux major release in the format `elX` where `X` is the release version. Examples of valid `DISTRO` values are `el7` and `el8`.
     3. Update Yum using the following command:
            
            sudo yum makecache
            

     4. Install the Artifact Registry plugin on the VM, using the following command:
            
            yum install FORMAT-plugin-artifact-registry
            

Replace `FORMAT` with one of the following:

        * `yum`, if your operating system is Enterprise Linux 7 or earlier
        * `dnf`, if your operating system is Enterprise Linux 8 or later
     5. Find the `#service_account_json = "/path/to/creds.json"` line in the `artifact-registry.conf` file, then uncomment the line and add the path of your service account key.

        * For Enterprise Linux 7 or earlier operating systems, the path to the configuration file is `/etc/yum/pluginconf.d/artifact-registry.conf`.
        * For Enterprise Linux 8 or later operating systems, the path to the configuration file is `/etc/dnf/plugins/artifact-registry.conf`.

Config file entry:
    
    service_account_json = "PATH_TO_SERVICE_ACCOUNT_KEY"
    

Replace `PATH_TO_SERVICE_ACCOUNT_KEY` with the path to your service account key JSON file.




###  Public repository 

[Configure public access](https://docs.cloud.google.com/artifact-registry/docs/access-control#public) to the repository.

## Configure a VM to access a standard Yum repository

To configure a VM to access a Yum repository, use the `yum` or `dnf` client tool:

  1. Generate the VM configuration command by running the [`gcloud beta artifacts print-settings yum` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/print-settings/yum):
         
         gcloud beta artifacts print-settings yum \
             --repository=REPOSITORY \
             --location=LOCATION
         

Replace the following:

     * `REPOSITORY` is the name of the Artifact Registry repository.
     * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 

The output is similar to the following:
    
    # To configure your package manager with this repository:
    
    # Update Yum:
    sudo yum makecache
    
    # Install the Yum credential helper:
    sudo yum install yum-plugin-artifact-registry
    
    # Configure your VM to access Artifact Registry packages using the following
    # command:
    
    sudo tee -a /etc/yum.repos.d/artifact-registry.repo << EOL
    [REPOSITORY]
    name=REPOSITORY
    baseurl=https://LOCATION-yum.pkg.dev/projects/PROJECT/REPOSITORY
    enabled=1
    repo_gpgcheck=0
    gpgcheck=0
    EOL
    
    # Update Yum:
    sudo yum makecache
    

  2. Configure the `yum` client tool to fetch packages from your repository using the `tee` command from the output of the `print-settings` command.

For example, to install packages from the public `my-repo` in the project `my-project` and in the location `us-west1`, use the following command:
         
         sudo tee -a /etc/yum.repos.d/artifact-registry.repo << EOL
         [my-repo]
         name=My Repository
         baseurl=https://us-west1-yum.pkg.dev/projects/my-project/my-repo
         enabled=1
         repo_gpgcheck=0
         gpgcheck=0
         EOL
         

**Note:** Yum repository-level GPG validation, using `repo_gpgcheck`, isn't supported for Artifact Registry repositories. Artifact Registry repositories are served over HTTPS (using SSL certificates), and serving over HTTPS is considered more trustworthy.
  3. Update your repository sources with the following command:
         
         sudo yum makecache
         




Yum can now connect to the repository.

If you create additional Yum repositories, create a `.repo` file for each one in `/etc/yum.repos.d/`. Rerun `sudo yum update` to update repository sources.

## Configure a VM to access a remote Yum repository

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To configure a VM to only use a remote Yum repository instead of a standard upstream Yum repository, replace the standard repository in the VM's repository list with the remote repository.

If the standard repository is defined in the configuration file instead of a separate repository file (`.repo`) you can delete the entry in the configuration file and replace it with your remote, or define a new repository file in the `/etc/yum.repos.d/` directory.

**Warning:** re-ordering and deleting repositories from the configuration file for Yum can have serious consequences. If you're not sure you want to remove the standard repository, you can configure Yum to use a remote Yum repository as a backup.

  1. Go to the [VM instances page](https://console.cloud.google.com/compute/instances).

  2. In the row with your VM, click **SSH**. A new window opens with a terminal session on the VM.

  3. Open the VM's `/etc/yum.repos.d/` folder and find the appropriate repository file (`.repo`) that contains the standard upstream repository. This is sometimes referred to as the base repository. The base repository can be identified by the Yum repository name containing `[base]` or `[baseos]`.

  4. To replace the base repository completely, remove default settings under `[base]` or `[baseos]`. If you want to keep the standard upstream repository and add the remote repository as a fall-back option, then don't remove the default settings.

  5. Add the following settings under `[base]` or `[baseos]`:
         
         name=YUM_REPOSITORY_NAME
         baseurl=https://LOCATION-yum.pkg.dev/remote/PROJECT_ID/REMOTE_REPOSITORY_NAME
         enabled=1
         gpgcheck=1
         

Replace the following:



  * `YUM_REPOSITORY_NAME` with a one word unique repository ID for your remote Yum repository. This name can match the upstream repository name if you have deleted the standard upstream repository configuration, or if you are keeping the standard upstream repository, then you can use a different name to identify it as a remote repository.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
  * `PROJECT_ID` with the project ID of the VM.
  * `REMOTE_REPOSITORY_NAME` with the human readable name of the remote repository.

**Note:** Yum repository-level GPG validation, using `repo_gpgcheck`, is not supported for Artifact Registry repositories. Artifact Registry repositories are served over HTTPS (using SSL certificates), and serving over HTTPS is considered more trustworthy.

### Use a remote Yum repository as a backup

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you want to keep the standard upstream as the first option and add the remote repository as a fall-back option, you can keep the standard upstream in the repository file, and create a new repository file in the `/etc/yum.repos.d` folder.

To create a new repository file in the `/etc/yum.repos.d` folder, run the following command:
    
    
    sudo tee -a /etc/yum.repos.d/artifact-registry.repo << EOF
    [YUM_REPOSITORY_NAME]
    name=REPOSITORY_NAME
    baseurl=https://LOCATION-yum.pkg.dev/remote/PROJECT_ID/REMOTE_REPOSITORY_NAME
    enabled=1
    gpgcheck=1
    EOF
    

Replace the following:

  * `YUM_REPOSITORY_NAME` with a one word unique repository ID for your remote Yum repository.
  * `REPOSITORY_NAME` with the human readable name of the repository.
  * `LOCATION` with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the remote repository.
  * `PROJECT_ID` with the project ID of the VM.
  * `REMOTE_REPOSITORY_NAME` with the name you gave your remote repository.



For example, the following command configures the VM to fetch the repository `my-repo` in the project `my-project` and location `us-west1` when Yum installs the repository `my-repo`.

**Note:** The `YUM_REPOSITORY_NAME` and Artifact Registry `REMOTE_REPOSITORY_NAME` can be different, but the `YUM_REPOSITORY_NAME` is used in error reporting, so it's helpful to keep it the same as the repository name.
    
    
    sudo tee -a /etc/yum.repos.d/artifact-registry.repo << EOF
    [my-repo]
    name=My Repository
    baseurl=https://us-west1-yum.pkg.dev/remote/my-project/my-repo
    enabled=1
    gpgcheck=1
    EOF
    

## What's next

  * [Learn about managing packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/manage-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
