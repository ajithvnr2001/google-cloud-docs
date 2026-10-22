---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-suse-registration/
title: Troubleshooting SLES pay-as-you-go registration \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:58.708927+00:00
---

# Troubleshooting SLES pay-as-you-go registration  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-suse-registration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting SLES pay-as-you-go registration Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how to resolve issues you might encounter when you connect Compute Engine virtual machine (VM) instances running pay-as-you-go (PAYG) SUSE Linux Enterprise Server (SLES) to the SUSE Subscription Management Tool (SMT) repository.

## Before you begin

  * Ensure that the VM has an associated [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts).
  * Ensure that the [Service Metadata API](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity) is accessible from the VM.
  * Ensure network connectivity from the VM to the respective [Region Servers](https://susepubliccloudinfo.suse.com/v1/google/servers/regionserver.xml) and [SMT Servers](https://susepubliccloudinfo.suse.com/v1/google/servers/smt.xml)
  * Use the [sc-repocheck](https://github.com/rfparedes/susecloud-repocheck) tool to automatically troubleshoot the issues.
  * Check the steps described in the [ SUSE PAYG troubleshooting](https://opensource.suse.com/premium-support/docs/data-collection/repo-issues.html) guide.
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




## Network issues

### Unresolvable domain name

You might encounter the following issues if the VM can't connect to the `smt-gce.susecloud.net` SMT server:
    
    
    SUSEConnect error: SocketError: getaddrinfo: Name or service not known
    
    
    
    ping: unknown host smt-gce.susecloud.net
    

The cause of these issues is generally because of an incorrect resolution of the SMT server domain name `smt-gce.susecloud.net`. This domain isn't globally resolvable, so you must set its IP address according to the VM region by doing the following:

Check the `/etc/hosts` file to make sure it contains an entry with the `smt-gce.susecloud.net` domain.
    
    
    cat /etc/hosts | grep -i smt

The output looks similar to the following, but the IP address might be different:
    
    
    # Added by SMT registration do not remove, retain comment as well
    108.59.80.221   smt-gce.susecloud.net   smt-gce
    

If the `/etc/hosts` file doesn't contain the same lines as the preceding example, do the following:

  1. Find an IP address that corresponds with your VM's region from the [list of SUSE SMT IP addresses](https://pint.suse.com/?resource=servers&csp=google&serverType=smt).

  2. Edit the file to add the SUSE SMT IP address and any other information that is missing.


While you can modify the `/etc/hosts` file for troubleshooting purposes, it's important to know that the `registercloudguest` tool might overwrite your changes. 

### Network unavailability

You may encounter the following errors due to network unavailability, even if the VM is able to resolve Compute Engine Update Server domain name:
    
    
    Unexpected exception.
    Not ready to read within timeout.
    
    
    
    Repository 'SLE-Module-Adv-Systems-Management12-Pool' is invalid.
    Repository 'SLE-Module-Adv-Systems-Management12-Updates' is invalid.
    

The following are some examples of errors you might find in the `/var/log/cloudregister` log file during the investigation:
    
    
    WARNING:Unable to remove client registration from server
    WARNING:HTTPSConnectionPool(host='smt-gce.susecloud.net', port=443): Max retries exceeded with url: /connect/systems (Caused by NewConnectionError(': Failed to establish a new connection: [Errno 110] Connection timed out',))
    
    
    
    INFO:Region server arguments: ?regionHint=europe-central2
    ERROR:No response from: [('34.118.112.80', None), ('34.116.251.218', None), ('34.116.224.144', None)]
    

To learn more about the cause of the issue, perform a network connectivity test. The following example shows how to test an HTTPS connection using `cURL`:
    
    
    curl -sSI -m 5 -o /dev/null \
      -w 'Response code (>0 is OK): %{http_code}\n' \
      'https://smt-gce.susecloud.net'

The command's output contains an [HTTP response code](https://developer.mozilla.org/docs/Web/HTTP/Status) or an error message. The following are common responses and errors:

  * Successful response:
        
        Response code (>0 is OK): 200
        

  * Request timeout error:
        
        Response code (>0 is OK): 000
        curl: (28) Connection timed out after 5001 milliseconds
        

  * Unresolvable domain error:
        
        Response code (>0 is OK): 000
        curl: (6) Could not resolve host: smt-gce.susecloud.net
        


Any response code greater than `0` is a positive response because the VM established a connection with the server, even if the response contains a client or server error response code. 

In certain scenarios, such as strict host firewall rules, the default IP address associated with the `smt-gce.susecloud.net` domain might not be available. To ensure that the issue isn't only related to the current IP address, test network connectivity for alternate regional servers. Retrieve the list of regional servers:

Go to [SUSE WebUI](https://pint.suse.com/?resource=servers&csp=google) to obtain the list of regional update servers.

Use `pint` tool to obtain the list of regional update servers by CLI.

  1. Install required package
         
         sudo zypper install python3-susepubliccloudinfo

  2. Use the following command with specific region
         
         pint google servers --region us-central1

  3. A successful output contains a list of entries in XML format
         
         <?xml version='1.0' encoding='UTF-8'?>
             <servers>
               <server ip="146.148.73.14" name="" region="us-central1" type="regionserver-sles"/>
               <server ip="162.222.182.90" name="" region="us-central1" type="regionserver-sap"/>
               <server ip="108.59.80.221" name="smt-gce.susecloud.net" region="us-central1" type="smt"/>
               <server ip="108.59.85.41" name="smt-gce.susecloud.net" region="us-central1" type="smt"/>
               <server ip="108.59.80.58" name="smt-gce.susecloud.net" region="us-central1" type="smt"/>
             </servers>
         




To find the full list of SUSE server IPs for Google Cloud, view the following documents:

  * [Region Servers](https://susepubliccloudinfo.suse.com/v1/google/servers/regionserver.xml)
  * [SMT Servers](https://susepubliccloudinfo.suse.com/v1/google/servers/smt.xml)



A VM misconfiguration might cause network unavailability. If you have issues, perform [network diagnostics](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-networking) to identify the root cause.

### Registration failed

You might encounter the following error if you have VMs with a private IP address in Cloud NAT:
    
    
    ERROR:  Registration failed: Registering system to registration proxy https://smt-gce.susecloud.net
    command '/usr/bin/zypper --non-interactive refs Python_3_Module_x86_64' failed
    Error: zypper returned 4 with 'Problem retrieving the repository index file for service 'Python_3_Module_x86_64':
    Timeout exceeded when accessing 'https://smt-gce.susecloud.net/services/2045/repo/repoindex.xml?credentials=Python_3_Module_x86_64'.
    

To resolve this issue, review your Cloud NAT configuration and verify that you've set the **minimum ports per VM instance** parameter to at least **256**.

For more information, check the [Registration and zypper failed for Compute Engine instances behind Cloud NAT](https://www.suse.com/support/kb/doc/?id=000019662) SUSE support bulletin.

### No response

If your VM experiences problems communicating with update and region servers, you might see the following errors:

  * `SUSEConnect` error:
        
        SUSEConnect error: Errno::ETIMEDOUT: Connection timed out - connect(2) for "smt-gce.susecloud.net" port 443
        

  * `zypper` error:
        
        Error retrieving metadata for 'SLE-Module-Adv-Systems-Management12-Pool':
        Not ready to read within timeout.
        ...
        




These errors can occur when update and region servers don't respond. To verify if this is the case, check the `/var/log/cloudregister` logs for similar content:
    
    
    INFO:Region server arguments: ?regionHint=europe-central2
    INFO:Using API: regionInfo
    INFO:Region server arguments: ?regionHint=europe-central2
    INFO:Getting update server information, attempt 1
    INFO:   Using region server: 130.211.242.136
    ERROR:  No response from: 130.211.242.136
    INFO:   Using region server: 35.187.193.56
    ERROR:  No response from: 35.187.193.56
    INFO:   Using region server: 162.222.182.90
    ERROR:  No response from: 162.222.182.90
    INFO:   Using region server: 130.211.88.88
    ERROR:  No response from: 130.211.88.88
    ERROR:  None of the servers responded
    ERROR:  Attempted: [IPv4Address('130.211.242.136'), IPv4Address('35.187.193.56'), IPv4Address('162.222.182.90'), IPv4Address('130.211.88.88')]
    ...
    ...
    ...
    ERROR:Request not answered by any server after 3 attempts
    ERROR:Exiting without registration
    

To resolve this issue, try one or more of the following:

  * Confirm that the VM has an external IP address or that the Virtual Private Cloud subnet uses a NAT (either Cloud NAT or custom solution).

  * If you modified the default network routing rules, such as limiting public Internet access or routing traffic through an on-premises network, add routes manually for SMT IPs through the default Compute Engine gateway, by doing the following:

    1. Go to the **Routes** page in the Google Cloud console.

[Go to the Routes page](https://console.cloud.google.com/networking/routes/list)

    2. Under the **Route Management** tab look for a route that includes the SUSE SMT IP addresses and verify that it has the Compute Engine default gateway as the next hop.

    3. If the route is missing, add it by clicking **Create Route** and entering the necessary information.

  * If you're using an internal passthrough Network Load Balancer, for example with additional intermediary network software (like firewalls or custom NATs), make sure that the load balancer is the next hop for VM traffic, by doing the following:

    1. Go to the **VM instances** page in the Google Cloud console.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

    2. Click the name of the VM you want to check. The **VM details** page opens.

    3. In the **Network interfaces** section, click **View details**.

    4. In the **Firewall and routes details** section locate the route that defines the path to the selected IP address range.

    5. Click the name of the route and confirm that internal passthrough Network Load Balancer or its IP address is the next hop.

If there is no route that defines the path to the selected IP address range, or if the route's next hop is different from internal passthrough Network Load Balancer, then [set up internal passthrough Network Load Balancer as the next hop](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview).

  * If you're using an internal passthrough Network Load Balancer, confirm that it's located in the same region as the VM.

    1. Go to the **VM instances** page in the Google Cloud console.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

    2. Locate the VM you want to check and note down its region.

    3. Go to the **Load balancing** page in the Google Cloud console.

[Go to the Load balancing page](https://console.cloud.google.com/net-services/loadbalancing/list/loadBalancers)

    4. Locate the internal passthrough Network Load Balancer used and check if it is in the same region as the VM.

    5. If the VM and the internal passthrough Network Load Balancer aren't in the same region, enable [global access](https://docs.cloud.google.com/load-balancing/docs/internal#client-access).




### Registration behind proxies

You might encounter an issue if your VMs use non-transparent proxies or other software that performs person-in-the-middle (PITM) inspection (for example, Barracuda CloudGen Firewall, Palo Alto). The following example demonstrates an attempt to register SLES by using an HTTP proxy.
    
    
    ERROR: Baseproduct registration failed
    ERROR: Registering system to registration proxy https://smt-gce.susecloud.net
    
    Announcing system to https://smt-gce.susecloud.net ...
    SUSEConnect error: Net::HTTPFatalError: 503 "Service Unavailable"
    

SUSE doesn't officially support SLES registration behind both person-in-the-middle (PITM) and non-transparent proxies on Compute Engine. PITM proxy configurations fail during registration due to certificate pinning.

Google Cloud doesn't provide support for the registration process when you use third-party proxying software. 

We recommend using a [Cloud NAT configuration](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation) or setting up a custom SMT server.

### VPC Service Controls violation

If your organization uses VPC Service Controls (VPC-SC), registration might fail and you might see a `Request is prohibited by organization's policy` error message. This failure can be caused by ingress or egress violations if you haven't configured exceptions for SUSE Update Infrastructure in your VPC-SC policy.

To resolve this issue, add the following components to an allowlist in your VPC-SC policy to allow the VM to communicate with SUSE Update Infrastructure:

  * Update Infrastructure Project: `Suse-gce-smt` (Project Number: 778092048372)
  * Service Account: `778092048372@project.gserviceaccount.com`
  * Required Method: `compute.alpha.InstancesService.GetLicenses`



## OS configuration issues

### Unknown registration status

If you don't know if your pay-as-you-go (PAYG) SUSE Linux Enterprise Server (SLES) is registered, run the following command:
    
    
    sudo SUSEConnect --status-text

The output contains the version and registration status of the SUSE products, including SUSE Linux Enterprise Server.
    
    
    Installed Products:
    ------------------------------------------
    
      SUSE Linux Enterprise Server 12 SP5
      (SLES/12.5/x86_64)
    
      Registered
    
    ------------------------------------------
    ...
    

If the status is `Not Registered`, re-register the VM to fix the issue:
    
    
    sudo registercloudguest --force-new

### Incorrect base product symlink

You might encounter the following errors if the base product link points to an incorrect product file:
    
    
    2020-06-17 12:03:56,124 ERROR:Unable to obtain product information from server "108.59.85.41,None"
            Unprocessable Entity
            {"type":"error","error":"Unmet product dependencies, activate one of these products first: SUSE Linux Enterprise Server 12 x86_64, SUSE Linux Enterprise Server for SAP Applications 12 x86_64, SUSE Linux Enterprise Server 12 SP1 x86_64, ...","localized_error":"..."}
    Unable to register modules, exiting.
    

This error occurs when the `/etc/products.d/baseproduct` symbolic link points to an incorrect product file (for example, `sle-module-toolchain.prod`).

To resolve this issue, update the symlink at `/etc/products.d/baseproduct` to point to the appropriate base product file:

  1. Navigate to the `/etc/products.d` directory
         
         cd /etc/products.d

  2. Run the following command replacing `SLES.prod` with `SLES_SAP.prod` if you've installed SLES for SAP:
         
         sudo ln -sf SLES.prod baseproduct


**Note:** If the `SLES.prod` or `SLES_SAP.prod` product file is missing, you can [create a new VM instance](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance) with the same boot disk image and copy the correct file from there to the `/etc/products.d` directory.

### Instance identity information unavailability

You might encounter the following errors if the instance identity information isn't available for the VM. This issue can occur if a service account isn't attached to the instance, or if the attached service account was deactivated.

**Note:** There is a known issue where deleting and re-creating a service account with the same name can cause instance identity information to become unavailable.
    
    
    ERROR:Data collected from stderr for instance data collection "b'Unable to access instance identity information\n'"
    

To access the instance metadata for [identity tokens](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity) all VMs must have an associated [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts).

For more information, read the [Public Cloud Infrastructure Update](https://www.suse.com/support/kb/doc/?id=000019633).

To check the status of your VM's service account, run the following command on the VM:
    
    
    curl -s -H 'Metadata-Flavor: Google' \
      'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity?audience=test'

Example of a successful response with an identity token:
    
    
    eyJhbGciOiJSUzI1NiIsImtpZCI6IjkzOTd0MDQxSHQ2NDNxNzkzUjY1MDIwNzEyMjZPNnppaTdqNTl3eTciLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJ0ZXN0IiwiYXpwIjoiMjY1MDIwMDUyMzgzMjYyNTk0ODU2IiwiZXhwIjoxNjgzNzEyNTQzLCJpYXQiOjE2ODM3MTI4NjQsImlzcyI6Imh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbSIsInN1YiI6IjQ1NjA2MzQ5MDg5Mzc0Njg3ODI5NyJ9.EpzQ3NZ8mKStdpH10fL34qsKG0rjQEflzvLJLm2tVNX4xBJAkMhi8lcs5InUEY-QMK3njgbzdzNtD1fXoIfKoeWsqkA8vG3NkBz5zqRrtaB2STcO14H5tjIdTBsrCtET447tRXlGG5cvgMcWnRDZG92-jUZEpWki_Ri4T69X5-bBWkfE2Thm3oSUW4fScdeVOEmOgWnzD2jeVqQ_2YniywvpkT-rLzKfN-5AgN66zgBfXqJVTC90KFMebfiaOoL7z6ZSM9AjZGf45QEMZjxjd-Xzyee6ZWK8s0RE3hJlytb3zYcLt3tJwQ1WhnrC2ToJ-ZmKxxK3xKDLCvCQ6Ny5to
    

If the VM is unaffected, you receive a token. If the VM is affected, the metadata that's returned is an error message similar the following:
    
    
    {
      "error": "invalid_request",
      "error_description": "Service account not enabled on this instance"
    }
    

To fix this issue, perform the following steps:

  1. Stop the VM:
         
         gcloud compute instances stop VM_NAME

  2. Add a service account to the VM:
         
         gcloud compute instances set-service-account VM_NAME \
           --service account SERVICE_ACCOUNT \
           --no-scopes

**Note:** The `--no-scopes` flag removes all scopes from the VM. If you don't specify a flag for access scope, the system assigns default scopes to the compute instance service account, or the service account retains its current scopes.
  3. Start the VM:
         
         gcloud compute instances start VM_NAME

  4. After adding the missing service account, run the following command from the VM to re-register SLES:
         
         sudo registercloudguest --force-new




### Missing required packages

Registration can fail if your VM is missing essential packages like `cloud-regionsrv-client`, `regionServiceClientConfigGCE`, `cloud-netconfig-gce`, or `suseconnect-ng`.

To resolve this issue, install the required packages, clean up registration files, and re-register the VM.

  1. Install any missing packages.
         
         sudo zypper install PACKAGE_NAME

Replace `PACKAGE_NAME` with the name of the missing package.

  2. Clean up old registration files:
         
         sudo registercloudguest --clean
         sudo SUSEConnect --cleanup
         sudo rm -f /etc/zypp/credentials.d/*
         sudo rm -f /etc/zypp/repos.d/*
         sudo rm -f /etc/zypp/services.d/*

  3. Re-register the VM:
         
         sudo registercloudguest --force-new




### Wrong python3 symbolic link

If you run `registercloudguest` and see the `ModuleNotFoundError: No module named 'requests'` error, an incorrect `/usr/bin/python3` symbolic link might be the cause, for example, if you manually overwrote it.
    
    
    Traceback (most recent call last):
    File "/usr/sbin/registercloudguest", line 34, in <module>
    import requests
    ModuleNotFoundError: No module named 'requests'
    

To resolve this issue, re-create the symbolic link to point to the correct Python version.

  1. Confirm the installed Python version on the instance:
         
         sudo zypper info python3

  2. Check the `python3` symbolic link:
         
         ls -ll /usr/bin | grep -i python3

  3. If the link is incorrect, remove it and create a new link that points to the correct Python version (for example, `python3.6`):
         
         sudo rm /usr/bin/python3
         sudo ln -sf /usr/bin/python3.6 /usr/bin/python3




### SSL certificate verification failed

If certificate files are missing from the `/etc/pki/trust/anchors` directory, you might see errors like `Curl error 60` or `ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED]`. Here's a more detailed example of an error you might see in `/var/log/cloudregister`:
    
    
    Traceback (most recent call last):
     File "/usr/lib/python3.6/site-packages/urllib3/connectionpool.py", line 677, in urlopen
     ...
     File "/usr/lib64/python3.6/ssl.py", line 689, in do_handshake
     self._sslobj.do_handshake()
     ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:852)
    

You can confirm that certificate files are missing by running the following command and seeing empty output:
    
    
    ls -lart /etc/pki/trust/anchors

The output should be empty if certificates are missing:
    
    
    total 0
    

To resolve this issue, try one of the following options:

  * **Option 1: Clean up and re-register**

Clean up all files associated with registration, then force a new registration. The registration process downloads the necessary certificates from the region servers.
        
        sudo registercloudguest --clean && \
          sudo SUSEConnect --cleanup && \
          sudo rm -f /etc/zypp/credentials.d/* && \
          sudo rm -f /etc/zypp/repos.d/* && \
          sudo rm -f /etc/zypp/services.d/* && \
          sudo rm -f /etc/pki/trust/anchors/* && \
          sudo sed -i '/^# Added by SMT reg/,+1d' /etc/hosts && \
          sudo registercloudguest --force-new

  * **Option 2: Copy certificates from a working instance**

If cleaning up and re-registering doesn't resolve the issue, you can copy the certificate files from a working instance using [`gcloud compute scp`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/scp) or by attaching the boot disk of a working instance to the failing instance.

If you attach and mount the disk of a working instance at `MOUNT_PATH`, run the following commands:
        
        sudo cp MOUNT_PATH/etc/pki/trust/anchors/* /etc/pki/trust/anchors/
        sudo update-ca-certificates
        sudo cp -pr MOUNT_PATH/usr/lib/regionService /usr/lib/regionService
        sudo registercloudguest --force-new




### libzypp package incompatibility

A PAYG SUSE VM with SLES for SAP 15 might fail to register with an error similar to the following:
    
    
    ERROR:Baseproduct registration failed
    Registering system to registration proxy https://smt-gce.susecloud.net
    ...
    command '/usr/bin/zypper --non-interactive refs SUSE_Linux_Enterprise_Server_for_SAP_Applications_x86_64' failed
    Error: zypper returned 1 with 'Error occurred while setting download (curl) options for 'https://smt-gce.susecloud.net/services/2294?credentials=SUSE_Linux_Enterprise_Server_for_SAP_Applications_x86_64':
    Unexpected exception.
    Unknown error reading from 'plugin:/susecloud?credentials=SUSE_Linux_Enterprise_Server_for_SAP_Applications_x86_64&path=/services/2294'
    ...
    - Error occurred while setting download (curl) options for 'https://smt-gce.susecloud.net/services/2294?credentials=SUSE_Linux_Enterprise_Server_for_SAP_Applications_x86_64':
    

This issue can occur when an update to the `libzypp` package leaves an incompatible version of the `libcurl4` package. When `libzypp` tries to self-update, it can no longer use `libcurl4` to make requests to package locations.

To resolve this issue, manually update the `libzypp` package. The following command is an example, and you might need to adjust the version number:
    
    
    sudo rpm -i libzypp-17.31.31-150400.3.52.2.x86_64.rpm

### Unsupported OS version or outdated packages

If you're running an OS version that is outside of its general support period—for example, SLES 12 SP4, for which General Support ended June 30, 2020—registration might fail. This failure can occur because outdated packages on the VM are unable to communicate with SUSE update infrastructure. You might see errors about unreachable IPs in the `/var/log/cloudregister` log file, even if network connectivity seems partially successful (for example, if using `telnet` to SMT servers returns a `403 Forbidden` error).

To check if packages are outdated, you can view their installation dates. Packages that haven't been updated in over a year might be outdated. To check the last update time for a package, use the following command:
    
    
    rpm -qa --qf '%{NAME}-%{VERSION} : %{INSTALLTIME:date}\n' | grep PACKAGE_NAME

To resolve this issue, upgrade to a [supported SLES version](https://www.suse.com/lifecycle/). You might also need to update specific packages as described in [SUSE Technical Information Documents (TIDs)](https://www.suse.com/support/kb/articles/). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
