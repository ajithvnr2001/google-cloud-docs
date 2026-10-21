---
url: https://docs.cloud.google.com/artifact-registry/docs/os-packages/troubleshoot/
title: Troubleshoot OS package issues \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:29.708870+00:00
---

# Troubleshoot OS package issues  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/os-packages/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Troubleshoot OS package issues Stay organized with collections  Save and categorize content based on your preferences. 

Learn about troubleshooting steps that you might find helpful if you run into problems managing OS packages in Artifact Registry.

For information about resolving issues with Artifact Registry remote repositories for OS packages, see [Troubleshoot remote repositories](https://docs.cloud.google.com/artifact-registry/docs/troubleshoot-remote#os-pkgs). 

## Authentication and permissions issues

You cannot connect to a repository for actions such as installing a package. The output from the package manager includes a `401` or `403` error, which indicates issues with authentication or permissions.

Example Apt errors:
    
    
    Err:1 ar+https://us-west1-apt.pkg.dev/projects/my-project my-package Release
      Error downloading: code 401
    
    
    
    E: Failed to fetch https://us-west1-apt.pkg.dev/projects/my-project/dists/quickstart-apt-repo/main/binary-amd64/Packages  403  Forbidden [IP: 74.125.20.82 443]
    E: Some index files failed to download. They have been ignored, or old ones used instead.
    

Example Yum error:
    
    
    /repodata/repomd.xml: [Errno 14] HTTPS Error 403 - Forbidden
    

There are a number of possible causes for these errors. Ensure that your VM meets the following requirements:

  1. Verify that the VM has an associated service account.

###  Compute Engine VM 

     1. Go to the [VM instances](https://console.cloud.google.com/compute/instances) page.
     2. In the list of VMs, click the name of your VM.

On the **Details** tab, the service account and access scopes appear under **API and identity management**.

By default, Compute Engine VMs use the Compute Engine [default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) and have a limited set of [access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_scopes). The default service account email address is in the format `PROJECT_NUMBER-compute@developer.gserviceaccount.com`.

Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To change the service account or attach a service account to a VM, see the [Changing the service account and access scopes for an instance](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes).

###  Other VM 

For other VMs, you must have a service account to act on behalf of the VM.

     1. If you don't have a service account, then [create a service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#createanewserviceaccount).

     2. Grant the Artifact Registry Reader (`roles.artifactregistry.reader`) role while you're creating the service account so that you don't need to configure permissions in a separate step.

  2. Ensure that the VM service account has read permissions to the repository as well as the `cloud-platform` API access scope.

###  Compute Engine VM 

Artifact Registry automatically retrieves VM service account credentials. If the repository is in a different project than the VM, then you must [grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the Artifact Registry Reader role to the VM service account. You must also ensure that the VM has the `cloud-platform` access scope.

To set the `cloud-platform` access scope,

     1. Stop the VM instance, replacing `INSTANCE` with the VM instance name.
            
            gcloud compute instances stop INSTANCE
            

     2. Set the access scope:
            
            gcloud compute instances set-service-account INSTANCE \
                --scopes=cloud-platform
            

     3. Restart the VM instance.
            
            gcloud compute instances start INSTANCE
            

###  Other VM 

[Grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the Artifact Registry Reader role to the VM service account. By default user-managed service accounts have the `cloud-platform` access scope.

  3. Verify that you have followed the steps to prepare the VM to access the repository. See the [Apt](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure#prepare-apt) or [Yum](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure#prepare-yum) preparation instructions.

  4. Verify that you have correctly configured [Apt](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure#config-apt) or [Yum](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure#config-yum) to access the repository.

If you are connecting to an Apt repository from a Compute Engine VM, make sure that the repository URL includes the `ar+` prefix.




## Credential helper issues

The following error message appears when the VM can't locate the Apt credential helper:
    
    
    E: Unable to locate package apt-transport-artifact-registry
    

The error occurs when you try to install the `apt-transport-artifact-registry` package on a VM that was created from an image that doesn't include the Apt repository signing key.

To resolve this issue, do the following:

  1. Install the signing key on the VM:

###  Debian VM 

Install the Apt repository signing keys, using the following command:
         
         curl https://LOCATION-apt.pkg.dev/doc/repo-signing-key.gpg | sudo apt-key add -
         

Replace `LOCATION` with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 

###  Ubuntu VM 

Install the Apt repository signing keys, using the following command:
         
         curl https://LOCATION-apt.pkg.dev/doc/repo-signing-key.gpg | sudo apt-key add - && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
         

Replace `LOCATION` with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 

  2. Re-try the [VM preparation steps](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure#compute-engine-vm).




## Authentication plugin issues

The following error message appears when there is an issue with the Yum or DNF authentication plugin:
    
    
    Plugin "artifact-registry" can't be imported
    

This error can occur for several reasons. To resolve the error, try running the plugin directly to confirm dependencies, check for Python issues, or reveal other possible underlying problems.

To run the plugin directly, use one the of following commands:

  * For the Yum plugin:
        
        python /usr/lib/yum-plugins/artifact-registry.py
        

  * For the DNF plugin:
        
        python3 /usr/lib/pythonVERSION-NUMBER/site-packages/dnf-plugins/artifact-registry.py
        

Replace `VERSION-NUMBER` with the default Python version for the Linux distribution. For example, Enterprise Linux 8 includes Python 3.6.

You can list the files in the installed plugin package to verify name of the Python library directory.
        
        rpm -ql dnf-plugin-artifact-registry|grep artifact-registry.py
        




## Missing recently uploaded artifacts

If your Apt or Yum client does not find a package that was recently uploaded or imported to your repository, it might be because the process to regenerate the Apt or Yum package index is not yet complete.

For small repositories, regenerating the Apt or Yum index file can take several seconds. For larger repositories, reindexing might take several minutes or longer.

To verify that a package was successfully added to the repository, use the Google Cloud CLI to list files in the package. Run the command:
    
    
    gcloud artifacts files list \
        --package=PACKAGE \
        --project=PROJECT-ID \
        --repository=REPOSITORY \
        --location=LOCATION
    

For example, you can check that the `python-gflags` package named `python3-gflags_1.5.1-5_all.deb` was uploaded successfully to the repository `us-west1-apt.pkg.dev\apt-project\apt-repo` with the command:
    
    
    gcloud artifacts files list \
        --package=python-gflags \
        --project=apt-project \
        --repository=apt-repo \
        --location=us-west1
    

If the package was uploaded successfully, the file appears in the output with a unique identifier in the filename, similar to the following example:
    
    
    FILE                                                                  CREATE_TIME          UPDATE_TIME          SIZE (MB)  OWNER
    pool/python3-gflags_1.5.1-5_all_2414c7af6a64c99a5f488aad366d637a.deb  2023-01-12T20:39:53  2023-01-12T20:39:53  0.035      projects/apt-project/locations/us-west1/repositories/apt-repo/packages/python3-gflags/versions/1.5.1-5
    

## Authentication error for some uploaded or imported packages

If the time to import or upload files exceeds the authentication token expiry period, uploads beyond the expiry period will fail. Tokens expire 60 minutes after you obtain them. An error similar to the following example appears in output from the import command if the token has expired.
    
    
    errors:
    - error:
        code: 16
        message: The request does not have valid authentication credentials.
      gcsSource:
        uris:
        - gs://my-bucket/debs/python/python3-gflags_1.5.1-5_all.deb
    

To address this issue:

  1. Try uploading or importing the specific package only to verify that you can add the package individually instead of in a batch import.
  2. If multiple packages failed, import or upload in smaller batches so that the operation does not exceed the token expiry period.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
