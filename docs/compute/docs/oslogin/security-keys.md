---
url: https://docs.cloud.google.com/compute/docs/oslogin/security-keys/
title: Enable security keys with OS Login \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:20.228225+00:00
---

# Enable security keys with OS Login  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/security-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Enable security keys with OS Login Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to use the physical security keys registered in your Google Account to connect to virtual machine (VM) instances that use OS Login.

Physical security keys are used to generate private SSH key files for connecting to VMs. When you use the Google Cloud console SSH-in-browser tool or the Google Cloud CLI to connect to VMs using security keys, OS Login retrieves the private SSH key file associated with your security key and configures the SSH key file for you. When you use [third-party tools](https://docs.cloud.google.com/compute/docs/oslogin/security-keys#third-party-tools) to connect, you must use the OS Login API to retrieve the SSH key information and configure the SSH key file yourself.

## Before you begin

  * [ Add a security key to your Google Account](https://support.google.com/accounts/answer/6103523?visit_id=637673282586358398-2383089289&rd=1).
  * [Set up OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Limitations

  * VMs that have security keys enabled only accept connections from SSH keys that are attached to the physical security keys registered in your Google Account.
  * You can't use Cloud Shell to connect to VMs that have security keys enabled.
  * Both the VM you're connecting to and the workstation you're connecting from must use a version of OpenSSH 8.2 or later that supports security key SSH types. The following Compute Engine VM operating systems support security keys:

    * Debian 11 (or later)
    * SUSE Linux Enterprise Server (SLES) 15 (or later)
    * Ubuntu 20.04 LTS (or later)
    * Container-Optimized OS 93 LTS (or later)
    * Rocky Linux 9 (or later)

To check if your environment supports security keys, run the following command:
    
    ssh -Q key | grep ^sk-
    

If the command doesn't return any output, your environment doesn't support security keys.

  * The SSH client on the workstation you're connecting from must support security keys and include the required libraries, such as `libfido2`.


**Note:** Service accounts continue to connect to VMs without using security keys. If you are connecting from a service or application that doesn't support security keys, [connect to the VM as a service account](https://docs.cloud.google.com/compute/docs/tutorials/service-account-ssh).

## Enable security keys with OS Login

You can enable use of security keys for all VMs that use OS Login in your project, or for single VMs.

### Enable security keys for all OS Login-enabled VMs in a project

To enable security keys on all VMs that use OS Login in your project, use the Google Cloud console or the gcloud CLI.

###  Console 

To enable security keys for all OS Login-enabled VMs, use the Google Cloud console to set `enable-oslogin` and `enable-oslogin-sk` to `TRUE` in project metadata:

  1. Go to the **Metadata** page.

[Go to Metadata](https://console.cloud.google.com/compute/metadata)

  2. Click **Edit**.

  3. Click **Add item**.

     1. In the **Key** field, enter `enable-oslogin`.
     2. In the **Value** field, enter `TRUE`.
  4. Click **Add item**.

     1. In the **Key** field, enter `enable-oslogin-sk`.
     2. In the **Value** field, enter `TRUE`.
  5. Click **Save**.




###  gcloud 

To enable security keys for all OS Login-enabled VMs, use the [`gcloud compute project-info add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata) to set `enable-oslogin=TRUE` and `enable-oslogin-sk=TRUE` in project metadata:
    
    
    gcloud compute project-info add-metadata \
        --metadata enable-oslogin=TRUE,enable-oslogin-sk=TRUE
    

### Enable security keys on a single OS Login-enabled VM

To enable security keys on a VM that uses OS Login, use the Google Cloud console or the gcloud CLI.

###  Console 

To enable security keys on a single VM, use the Google Cloud console to set `enable-oslogin` and `enable-oslogin-sk` to `TRUE` in instance metadata:

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM you want to enable security keys for.

  3. Click **Edit**.

  4. In the **Metadata** section, click **Add item**.

     1. In the **Key** field, enter `enable-oslogin`.
     2. In the **Value** field, enter `TRUE`.
  5. Click **Add item**.

     1. In the **Key** field, enter `enable-oslogin-sk`.
     2. In the **Value** field, enter `TRUE`.
  6. Click **Save**.




###  gcloud 

To enable security keys on a single VM, use the [`gcloud compute instances add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata) to set `enable-oslogin=TRUE` and `enable-oslogin-sk=TRUE` in instance metadata:
    
    
    gcloud compute instances add-metadata VM_NAME \
        --metadata enable-oslogin=TRUE,enable-oslogin-sk=TRUE
    

Replace `VM_NAME` with the name of your VM.

## Connect to a VM using a security key

You can connect to a VM that uses security keys using the Google Cloud console, the gcloud CLI, or third-party tools. If you connect to VMs using the Google Cloud console or the gcloud CLI, Compute Engine configures your SSH key for you. If you connect to VMs using third-party tools, you must perform the configuration yourself.

**Note:** VMs that have security keys enabled don't support gcloud CLI connections from Windows workstations. Connect using the Google Cloud console or third-party tools instead.

###  Console 

When you connect to VMs using the Google Cloud console [SSH-in-browser](https://docs.cloud.google.com/compute/docs/connect/ssh-in-browser) tool, SSH-in-browser retrieves the private keys associated with your security keys.

**Note:** The private key file can't be used to access your VM without physical access to your security key device.

To connect to a VM that has security keys enabled, do the following:

  1. In the Google Cloud console, go to the **VM instances** page.

  2. In the list of VMs, click **SSH** in the row of the VM that you want to connect to.

  3. When prompted, touch your security key.




###  gcloud 

When you connect to VMs using the gcloud CLI, the gcloud CLI retrieves the private keys associated with your security keys and configures the private key files. This configuration is persistent and applies to all VMs that use security keys.

**Note:** The private key file can't be used to access your VM without physical access to your security key device.

Use the [`gcloud beta compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/ssh) to connect to a VM that has security keys enabled:
    
    
    gcloud beta compute ssh VM_NAME
    

###  Third-party tools 

Before you connect to a VM that has security keys enabled, you must retrieve the private keys associated with your security keys and configure the private key files. This example uses the Python client library to perform the configuration.

**Note:** The private key file can't be used to access your VM without physical access to your security key device.

You only need to perform this configuration the first time you connect to a VM. The configuration is persistent and applies to all VMs that use security keys in your project.

From a terminal on your workstation, do the following:

  1. Install the Google client library for Python, if you haven't already, by running the following command:
         
         pip3 install google-api-python-client
         

  2. Save the following sample Python script, which retrieves the private keys associated with your security keys, configures the private key files, and connects to the VM.
         
         import argparse
         import os
         import subprocess
         from typing import Optional
         
         import googleapiclient.discovery
         
         
         def write_ssh_key_files(security_keys: list[dict], directory: str) -> list[str]:
             """
             Store the SSH key files.
         
             Saves the SSH keys into files inside specified directory. Using the naming
             template of `google_sk_{i}`.
         
             Args:
                 security_keys: list of dictionaries representing security keys retrieved
                     from the OSLogin API.
                 directory: path to directory in which the security keys will be stored.
         
             Returns:
                 List of paths to the saved keys.
             """
             key_files = []
             for index, key in enumerate(security_keys):
                 key_file = os.path.join(directory, f"google_sk_{index}")
                 with open(key_file, "w") as f:
                     f.write(key.get("privateKey"))
                     os.chmod(key_file, 0o600)
                     key_files.append(key_file)
             return key_files
         
         
         def ssh_command(key_files: list[str], username: str, ip_address: str) -> list[str]:
             """
             Construct the SSH command for a given IP address and key files.
         
             Args:
                 key_files: SSH keys to be used for authentication.
                 username: username used to authenticate.
                 ip_address: the IP address or hostname of the remote system.
         
             Returns:
                 SSH command as a list of strings.
             """
             command = ["ssh"]
             for key_file in key_files:
                 command.extend(["-i", key_file])
             command.append(f"{username}@{ip_address}")
             return command
         
         
         def main(
             user_key: str, ip_address: str, dryrun: bool, directory: Optional[str] = None
         ) -> None:
             """
             Configure SSH key files and print SSH command.
         
             Args:
                 user_key: name of the user you want to authenticate as. Usually an email address.
                 ip_address: the IP address of the machine you want to connect to.
                 dryrun: bool flag to do dry run, without connecting to the remote machine.
                 directory: the directory to store SSH private keys.
             """
             directory = directory or os.path.join(os.path.expanduser("~"), ".ssh")
         
             # Create the OS Login API object.
             oslogin = googleapiclient.discovery.build("oslogin", "v1beta")
         
             # Retrieve security keys and OS Login username from a user's Google account.
             profile = (
                 oslogin.users()
                 .getLoginProfile(name=f"users/{user_key}", view="SECURITY_KEY")
                 .execute()
             )
         
             if "posixAccounts" not in profile:
                 print("You don't have a POSIX account configured.")
                 print("Please make sure that you have enabled OS Login for your VM.")
                 return
         
             username = profile.get("posixAccounts")[0].get("username")
         
             # Write the SSH private key files.
             security_keys = profile.get("securityKeys")
         
             if security_keys is None:
                 print(
                     "The account you are using to authenticate does not have any security keys assigned to it."
                 )
                 print(
                     "Please check your Application Default Credentials "
                     "(https://cloud.google.com/docs/authentication/application-default-credentials)."
                 )
                 print(
                     "More info about using security keys: https://cloud.google.com/compute/docs/oslogin/security-keys"
                 )
                 return
         
             key_files = write_ssh_key_files(security_keys, directory)
         
             # Compose the SSH command.
             command = ssh_command(key_files, username, ip_address)
         
             if dryrun:
                 # Print the SSH command.
                 print(" ".join(command))
             else:
                 # Connect to the IP address over SSH.
                 subprocess.call(command)
         
         
         if __name__ == "__main__":
             parser = argparse.ArgumentParser(
                 description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
             )
             parser.add_argument("--user_key", help="Your primary email address.")
             parser.add_argument(
                 "--ip_address", help="The external IP address of the VM you want to connect to."
             )
             parser.add_argument("--directory", help="The directory to store SSH private keys.")
             parser.add_argument(
                 "--dryrun",
                 dest="dryrun",
                 default=False,
                 action="store_true",
                 help="Turn off dryrun mode to execute the SSH command",
             )
             args = parser.parse_args()
         
             main(args.user_key, args.ip_address, args.dryrun, args.directory)

  3. Run the script to configure your keys and optionally connect to the VM.
         
         python3 SCRIPT_NAME.py --user_key=USER_KEY --ip_address=IP_ADDRESS [--dryrun]
         

Replace the following:

     * `SCRIPT_NAME`: the name of your configuration script.
     * `USER_KEY`: your primary email address.
     * `IP_ADDRESS`: the external IP address of the VM you're connecting to.
     * `[--dryrun]`: (Optional) add the `--dryrun` flag to print the connection command without connecting to the VM. If you don't specify this flag, the script runs the connection command.



## What's next?

  * Learn how to [set up OS Login with 2-step verification](https://docs.cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication).
  * Learn how to [manage OS Login in an organization](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
