---
url: https://docs.cloud.google.com/compute/docs/tutorials/service-account-ssh/
title: Configure apps to use SSH \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:26.470218+00:00
---

# Configure apps to use SSH  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/service-account-ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure apps to use SSH Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure apps to programmatically connect between two virtual machine (VM) instances using SSH and OS Login. Enabling apps to use SSH can be useful for automating system management processes.

All code samples used in this guide are hosted on the [GoogleCloudPlatform/python-docs-samples GitHub page](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/compute/oslogin).

## Before you begin

  * [Set up SSH for a service account](https://docs.cloud.google.com/compute/docs/connect/set-up-service-account-ssh).
  * [Set up OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin) on your project, or on a VM that runs as a service account.
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




## Set up an SSH app

Set up your app to manage SSH keys and initiate SSH connections to Compute Engine VMs. At a high level, your app should do the following:

  1. Import the [Google OS Login library](https://docs.cloud.google.com/python/docs/reference/oslogin/latest) to build client libraries, which lets you to authenticate with the OS Login API.
  2. Initialize the OS Login Client object to enable your app to use OS Login.
  3. Implement a `create_ssh_key()` method that generates an SSH key for the VM's service account and adds the public key to the service account.
  4. Call the [`get_login_profile()` method](https://docs.cloud.google.com/python/docs/reference/oslogin/latest/google.cloud.oslogin_v1.services.os_login_service.OsLoginServiceClient#google_cloud_oslogin_v1_services_os_login_service_OsLoginServiceClient_get_login_profile) from the OS Login library to get the POSIX username that the service account uses.
  5. Implement a `run_ssh()` method to execute a remote SSH command.
  6. Remove the temporary SSH key files.



### Sample SSH app

The `oslogin_service_account_ssh.py` sample app demonstrates a possible implementation of an SSH app. In this example, the app uses the `run_ssh()` method to execute a command on a remote instance and return the command output.
    
    
    """
    Example of using the OS Login API to apply public SSH keys for a service
    account, and use that service account to run commands on a remote
    instance over SSH. This example uses zonal DNS names to address instances
    on the same internal VPC network.
    """
    from __future__ import annotations
    
    import argparse
    import subprocess
    import time
    from typing import Optional
    import uuid
    
    from google.cloud import [oslogin_v1](https://docs.cloud.google.com/python/docs/reference/oslogin/latest)
    import requests
    
    SERVICE_ACCOUNT_METADATA_URL = (
        "http://metadata.google.internal/computeMetadata/v1/instance/"
        "service-accounts/default/email"
    )
    HEADERS = {"Metadata-Flavor": "Google"}
    
    
    def execute(
        cmd: list[str],
        cwd: Optional[str] = None,
        capture_output: bool = False,
        env: Optional[dict] = None,
        raise_errors: bool = True,
    ) -> tuple[int, str]:
        """
        Run an external command (wrapper for Python subprocess).
    
        Args:
            cmd: The command to be run.
            cwd: Directory in which to run the command.
            capture_output: Should the command output be captured and returned or just ignored.
            env: Environmental variables passed to the child process.
            raise_errors: Should errors in run command raise exceptions.
    
        Returns:
            Return code and captured output.
        """
        print(f"Running command: {cmd}")
        process = subprocess.run(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE if capture_output else subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            text=True,
            env=env,
            check=raise_errors,
        )
        output = process.stdout
        returncode = process.returncode
    
        if returncode:
            print(f"Command returned error status {returncode}")
            if capture_output:
                print(f"With output: {output}")
    
        return returncode, output
    
    
    def create_ssh_key(
        oslogin_client: oslogin_v1.OsLoginServiceClient,
        account: str,
        expire_time: int = 300,
    ) -> str:
        """
        Generates a temporary SSH key pair and apply it to the specified account.
    
        Args:
            oslogin_client: OS Login client object.
            account: Name of the service account this key will be assigned to.
                This should be in form of `user/<service_account_username>`.
            expire_time: How many seconds from now should this key be valid.
    
        Returns:
            The path to private SSH key. Public key can be found by appending `.pub`
            to the file name.
    
        """
        private_key_file = f"/tmp/key-{uuid.uuid4()}"
        execute(["ssh-keygen", "-t", "rsa", "-N", "", "-f", private_key_file])
    
        with open(f"{private_key_file}.pub") as original:
            public_key = original.read().strip()
    
        # Expiration time is in microseconds.
        expiration = int((time.time() + expire_time) * 1000000)
    
        request = [oslogin_v1](https://docs.cloud.google.com/python/docs/reference/oslogin/latest).[ImportSshPublicKeyRequest](https://docs.cloud.google.com/python/docs/reference/oslogin/latest/google.cloud.oslogin_v1.types.ImportSshPublicKeyRequest.html)()
        request.parent = account
        request.ssh_public_key.key = public_key
        request.ssh_public_key.expiration_time_usec = expiration
    
        print(f"Setting key for {account}...")
        oslogin_client.import_ssh_public_key(request)
    
        # Let the key properly propagate
        time.sleep(5)
    
        return private_key_file
    
    
    def run_ssh(cmd: str, private_key_file: str, username: str, hostname: str) -> str:
        """
        Runs a command on a remote system.
    
        Args:
            cmd: command to be run.
            private_key_file: private SSH key to be used for authentication.
            username: username to be used for authentication.
            hostname: hostname of the machine you want to run the command on.
    
        Returns:
            Output of the executed command.
        """
        ssh_command = [
            "ssh",
            "-i",
            private_key_file,
            "-o",
            "StrictHostKeyChecking=no",
            "-o",
            "UserKnownHostsFile=/dev/null",
            f"{username}@{hostname}",
            cmd,
        ]
        print(f"Running ssh command: {' '.join(ssh_command)}")
        tries = 0
        while tries < 3:
            try:
                ssh = subprocess.run(
                    ssh_command,
                    shell=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    check=True,
                    env={"SSH_AUTH_SOCK": ""},
                    timeout=10,
                )
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as err:
                time.sleep(10)
                tries += 1
                if tries == 3:
                    if isinstance(err, subprocess.CalledProcessError):
                        print(
                            f"Failed to run SSH command (return code: {err.returncode}. Output received: {err.output}"
                        )
                    else:
                        print("Failed to run SSH - timed out.")
                    raise err
            else:
                return ssh.stdout
    
    
    def main(
        cmd: str,
        project: str,
        instance: Optional[str] = None,
        zone: Optional[str] = None,
        account: Optional[str] = None,
        hostname: Optional[str] = None,
        oslogin: Optional[[oslogin_v1](https://docs.cloud.google.com/python/docs/reference/oslogin/latest).[OsLoginServiceClient](https://docs.cloud.google.com/python/docs/reference/oslogin/latest/google.cloud.oslogin_v1.services.os_login_service.OsLoginServiceClient.html)] = None,
    ) -> str:
        """
        Runs a command on a remote system.
    
        Args:
            cmd: command to be executed on the remote host.
            project: name of the project in which te remote instance is hosted.
            instance: name of the remote system instance.
            zone: zone in which the remote system resides. I.e. us-west3-a
            account: account to be used for authentication.
            hostname: hostname of the remote system.
            oslogin: OSLogin service client object. If not provided, a new client will be created.
    
        Returns:
            The commands output.
        """
        # Create the OS Login API object.
        if oslogin is None:
            oslogin = [oslogin_v1](https://docs.cloud.google.com/python/docs/reference/oslogin/latest).[OsLoginServiceClient](https://docs.cloud.google.com/python/docs/reference/oslogin/latest/google.cloud.oslogin_v1.services.os_login_service.OsLoginServiceClient.html)()
    
        # Identify the service account ID if it is not already provided.
        account = (
            account or requests.get(SERVICE_ACCOUNT_METADATA_URL, headers=HEADERS).text
        )
    
        if not account.startswith("users/"):
            account = f"users/{account}"
    
        # Create a new SSH key pair and associate it with the service account.
        private_key_file = create_ssh_key(oslogin, account)
        try:
            # Using the OS Login API, get the POSIX username from the login profile
            # for the service account.
            profile = oslogin.[get_login_profile](https://docs.cloud.google.com/python/docs/reference/oslogin/latest/google.cloud.oslogin_v1.services.os_login_service.OsLoginServiceClient.html#google_cloud_oslogin_v1_services_os_login_service_OsLoginServiceClient_get_login_profile)(name=account)
            username = profile.posix_accounts[0].username
    
            # Create the hostname of the target instance using the instance name,
            # the zone where the instance is located, and the project that owns the
            # instance.
            hostname = hostname or f"{instance}.{zone}.c.{project}.internal"
    
            # Run a command on the remote instance over SSH.
            result = run_ssh(cmd, private_key_file, username, hostname)
    
            # Print the command line output from the remote instance.
            print(result)
            return result
        finally:
            # Shred the private key and delete the pair.
            execute(["shred", private_key_file])
            execute(["rm", private_key_file])
            execute(["rm", f"{private_key_file}.pub"])
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
        )
        parser.add_argument(
            "--cmd", default="uname -a", help="The command to run on the remote instance."
        )
        parser.add_argument("--project", help="Your Google Cloud project ID.")
        parser.add_argument("--zone", help="The zone where the target instance is located.")
        parser.add_argument("--instance", help="The target instance for the ssh command.")
        parser.add_argument("--account", help="The service account email.")
        parser.add_argument(
            "--hostname",
            help="The external IP address or hostname for the target instance.",
        )
        args = parser.parse_args()
    
        main(
            args.cmd,
            args.project,
            instance=args.instance,
            zone=args.zone,
            account=args.account,
            hostname=args.hostname,
        )

## Run the SSH app

After you create an app that uses SSH, you can run the app by following a process similar to the following example, which installs and runs the `oslogin_service_account_ssh.py` sample app. The libraries you install may differ, depending on the programming language the app uses.

Alternatively, you can write an app that imports `oslogin_service_account_ssh.py` and runs it directly.

  1. [Connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) that hosts the SSH app.

  2. On the VM, install `pip` and the Python 3 client library:
         
         sudo apt update && sudo apt install python3-pip -y && pip install --upgrade google-cloud-os-login requests
         

  3. Optional: If you are using the `oslogin_service_account_ssh.py` sample app, download it from [GoogleCloudPlatform/python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/compute/oslogin):
         
         curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/python-docs-samples/master/compute/oslogin/oslogin_service_account_ssh.py
         

  4. Run the SSH app. The sample app uses `argparse` to accept variables from the command line. In this example, instruct the app to install and run `cowsay` on another VM in your project.
         
         python3 service_account_ssh.py \
            --cmd 'sudo apt install cowsay -y && cowsay "It works!"' \
            --project=PROJECT_ID --instance=VM_NAME --zone=ZONE
         

Replace the following:

     * `PROJECT_ID`: the project ID of the VM that the app is connecting to.
     * `VM_NAME`: the name of the VM that the app is connecting to.
     * `ZONE`: the zone of the VM that the app is connecting to.

The output is similar to the following:
    
    ⋮
    ___________
     It works!
    -----------
          \   ^__^
           \  (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||
    




## What's next

  * Download and view the [full code sample](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/compute/oslogin). The full sample includes a small example of using all of these methods together. Feel free to download it, change it, and run it to suit your needs.
  * Learn more about [how SSH connections work in Compute Engine](https://docs.cloud.google.com/compute/docs/instances/ssh), including SSH key configuration and storage. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
