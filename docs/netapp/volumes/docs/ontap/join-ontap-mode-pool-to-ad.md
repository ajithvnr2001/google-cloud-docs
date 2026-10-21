---
url: https://docs.cloud.google.com/netapp/volumes/docs/ontap/join-ontap-mode-pool-to-ad/
title: Join an ONTAP-mode pool to Active Directory \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:39.783623+00:00
---

# Join an ONTAP-mode pool to Active Directory  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/ontap/join-ontap-mode-pool-to-ad/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Join an ONTAP-mode pool to Active Directory Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to join an ONTAP-mode pool to an Active Directory domain.

Flex Unified storage pools in ONTAP-mode don't use Active Directory policies. To use Active Directory with SMB volumes, join the ONTAP storage virtual machine (SVM) in the pool to your Windows domain by creating a CIFS server.

For Active Directory prerequisites and firewall rules, see [Google Cloud NetApp Volumes Active Directory integration](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad).

## Before you begin

Complete the following prerequisites:

  1. Make sure that the storage pool network can connect to the domain controllers and DNS servers.

  2. Configure Cloud DNS to forward DNS requests for your Windows domain to your Windows DNS servers.

  3. Complete the prerequisites in [Before you begin](https://docs.cloud.google.com/netapp/volumes/docs/ontap/common-ontap-mode-procedures#before_you_begin).

  4. Collect the following information:

     1. `AD_FQDN`: the fully qualified domain name, for example, corp.example.com.

     2. `AD_DNS_SERVERS`: one to three comma-separated IPv4 addresses for the Active Directory DNS servers.

     3. `AD_USERNAME` and `AD_PASSWORD`: a domain account that can create computer accounts, with a SAM account name of 20 characters or fewer.

     4. `COMPUTER_NAME`: a unique NetBIOS name for the computer account within the domain, with a maximum of 15 characters.

     5. `OU`: Optional: the distinguished name for the target organizational unit (OU), for example, OU=Computers,DC=corp,DC=example,DC=com.


**Note:** NetApp Volumes preconfigures the SVM, NTP, and data LIFs for ONTAP-mode pools. Look up the SVM name in the following sections.

## Overview

To join an ONTAP-mode pool to an Active Directory domain, complete the following steps:

  1. [Set up ontap_execute](https://docs.cloud.google.com/netapp/volumes/docs/ontap/common-ontap-mode-procedures#set_up_ontap_execute)

  2. Look up pool resources

  3. Configure DNS on the SVM

  4. Join the domain

  5. Configure SMB access

  6. Verify the domain join




## Look up pool resources

Look up the following resources of your storage pool:

  * SVM name

  * Data LIFs




### SVM name

To look up the SVM name:
    
    
     ontap_execute "vserver show -fields vserver,operational-state"
    

Note the Vserver name, for example, gcnv-7cf6ee41c1a94f0-svm-01. Use this name as `SVM_NAME` in later steps.

### Data LIFs

Before joining the domain, verify that your data LIFs can successfully reach your DNS servers and domain controllers.
    
    
     ontap_execute "network interface show -role data"
    

To test connectivity to a DNS server or domain controller, use a SAN LIF with the `-lif` flag. ONTAP-mode pools expose SAN LIFs named `SVM_NAME-san-1`, `SVM_NAME-san-2`, and additional LIFs as needed:
    
    
     ontap_execute "network ping -vserver SVM_NAME -destination DNS_OR_DC_IP -lif SVM_NAME-san-1"
    

**Note:** The `network ping` command requires the `-lif` flag. Use a SAN LIF, not the ILB NAS LIF.

If the ping fails, your storage pool can't connect to the DNS server or domain controller over the network. Virtual machines (VMs) in your VPC might still be able to connect to those hosts. For more information about troubleshooting connectivity issues, see [Why your NetApp Volumes can't connect to Active Directory and other networks behind your VPC](https://community.netapp.com/t5/Tech-ONTAP-Blogs/Why-your-NetApp-Volumes-can-t-reach-Active-Directory-and-other-networks-behind/ba-p/467585).

## Configure DNS on the SVM

To configure DNS on the SVM:
    
    
     ontap_execute "vserver services name-service dns create -vserver SVM_NAME -domains AD_FQDN -name-servers AD_DNS_SERVERS"
    

If the hosts name-service switch doesn't include DNS, add it:
    
    
     ontap_execute "vserver services name-service ns-switch modify -vserver SVM_NAME -database hosts -sources dns,files"
    

Verify the configuration:
    
    
     ontap_execute "vserver services name-service dns show -vserver SVM_NAME"
    

## Join the domain

This section describes the ONTAP CLI command, limitations of the CLI proxy, and how to join the domain using Python.

### ONTAP CLI command

On a system with direct ONTAP CLI access, run the following command:
    
    
     vserver cifs create -vserver SVM_NAME -cifs-server COMPUTER_NAME -domain AD_FQDN
    

To include optional parameters, use `-ou OU` and `-default-site SITE`. ONTAP prompts you for the domain password, and the command can take several minutes.

### Limitations of the CLI proxy

The ONTAP CLI proxy isn't interactive. Because the `vserver cifs create` command prompts for a password, you can't finish joining the domain through the proxy. Use the REST API instead. The API equivalent is `POST /protocols/cifs/services`.

The script advertises AES-256 only for Kerberos communication with Active Directory. This is the recommended setting for modern domains. To also advertise AES-128 or DES, add values to the `advertised_kdc_encryptions` array in the script before you run it, or modify the CIFS server after the domain join by using `vserver cifs security modify -advertised-enc-types`. DES isn't recommended because it uses weak encryption.

Valid encryption type values are `aes-256`, `aes-128`, `rc4`, and `des`. If you change advertised encryption types after the domain join, ONTAP resets the machine account password and prompts for Active Directory credentials.

### Join the domain using Python

Save the following script as `join_ad.py` and run it with Python 3.8 or later. The script uses only the Python standard library.
    
    
     #!/usr/bin/env python3
    """Join an ONTAP-mode SVM to Active Directory by creating a CIFS server."""
    
    import json
    import os
    import subprocess
    import sys
    import time
    import urllib.error
    import urllib.request
    
    # Required environment variables.
    REQUIRED = (
        "PROJECT_ID", "LOCATION", "POOL_NAME", "SVM_NAME",
        "AD_FQDN", "COMPUTER_NAME", "AD_USERNAME", "AD_PASSWORD",
    )
    missing = [name for name in REQUIRED if not os.environ.get(name)]
    if missing:
        sys.exit(f"Set required environment variables: {', '.join(missing)}")
    
    PROJECT_ID = os.environ["PROJECT_ID"]
    LOCATION = os.environ["LOCATION"]
    POOL_NAME = os.environ["POOL_NAME"]
    SVM_NAME = os.environ["SVM_NAME"]
    AD_FQDN = os.environ["AD_FQDN"]
    COMPUTER_NAME = os.environ["COMPUTER_NAME"]
    AD_USERNAME = os.environ["AD_USERNAME"]
    AD_PASSWORD = os.environ["AD_PASSWORD"]
    
    # Optional environment variables.
    OU = os.environ.get("OU", "")
    AD_SITE = os.environ.get("AD_SITE", "")
    POLL_INTERVAL = int(os.environ.get("POLL_INTERVAL", "10"))
    
    # Kerberos encryption types advertised to Active Directory. AES-256 only by default.
    # To add aes-128 or des (not recommended), extend this list before you run the script.
    ADVERTISED_KDC_ENCRYPTIONS = ["aes-256"]
    
    API_ROOT = (
        f"https://netapp.googleapis.com/v1/projects/{PROJECT_ID}"
        f"/locations/{LOCATION}/storagePools/{POOL_NAME}/ontap/api"
    )
    
    def get_access_token() -> str:
        return subprocess.check_output(
            ["gcloud", "auth", "print-access-token"], text=True
        ).strip()
    
    def api_request(method: str, path: str, body=None) -> dict:
        headers = {
            "Authorization": f"Bearer {get_access_token()}",
            "Content-Type": "application/json",
        }
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(f"{API_ROOT}{path}", data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode()
            sys.exit(f"API request failed ({exc.code}): {detail}")
    
    def job_record(response: dict) -> dict:
        return response.get("rawResponse") or response.get("body") or response
    
    def job_state(response: dict) -> str:
        return job_record(response).get("state", "")
    
    def format_job_error(response: dict) -> str:
        record = job_record(response)
        message = record.get("message") or record.get("error", {}).get("message")
        if message:
            return message
        return json.dumps(response, indent=2)
    
    def wait_for_job(job_uuid: str) -> None:
        print(f"ONTAP job UUID: {job_uuid}")
        while True:
            response = api_request("GET", f"/cluster/jobs/{job_uuid}")
            state = job_state(response)
            print(f"  Job state: {state}")
            if state == "success":
                print("Domain join completed.")
                return
            if state in ("failure", "error"):
                sys.exit(f"Job failed: {format_job_error(response)}")
            time.sleep(POLL_INTERVAL)
    
    def main() -> None:
        ad_domain = {
            "fqdn": AD_FQDN,
            "user": AD_USERNAME,
            "password": AD_PASSWORD,
        }
        if OU:
            ad_domain["organizational_unit"] = OU
        if AD_SITE:
            ad_domain["default_site"] = AD_SITE
    
        body = {
            "body": {
                "svm": {"name": SVM_NAME},
                "name": COMPUTER_NAME,
                "ad_domain": ad_domain,
                "security": {
                    "advertised_kdc_encryptions": ADVERTISED_KDC_ENCRYPTIONS,
                },
            }
        }
    
        print(f"Creating CIFS server and joining {AD_FQDN}...")
        response = api_request("POST", "/protocols/cifs/services?return_records=true", body)
    
        job = (response.get("body") or {}).get("job") or response.get("job")
        if not job or not job.get("uuid"):
            print(json.dumps(response, indent=2))
            return
        wait_for_job(job["uuid"])
    
    if __name__ == "__main__":
        main()
    

## Configure SMB access

Grant local administrator rights to a domain user or group:
    
    
     ontap_execute "vserver cifs users-and-groups local-group add-members -vserver SVM_NAME -group-name BUILTIN\\Administrators -member-names NETBIOS_DOMAIN\\username"
    

Replace `NETBIOS_DOMAIN` with the NetBIOS domain name, not the DNS name.

If you use Active Directory-integrated DNS, enable secure dynamic DNS updates. You must set the `-vserver-fqdn` flag to the CIFS server FQDN, for example `COMPUTER_NAME.AD_FQDN`:
    
    
     ontap_execute "vserver services name-service dns dynamic-update modify -vserver SVM_NAME -is-enabled true -use-secure true -vserver-fqdn COMPUTER_NAME.AD_FQDN"
    

## Verify the domain join

To verify the domain join:
    
    
     ontap_execute "vserver cifs show -vserver SVM_NAME"
    

Confirm that the CIFS server is online and joined to the expected domain.

## Remove a CIFS server

To delete the CIFS server and join the domain again, complete the following steps:

  1. Disable secure dynamic DNS updates:
         
         ontap_execute "vserver services name-service dns dynamic-update modify -vserver SVM_NAME -is-enabled false -use-secure false"
         

ONTAP blocks CIFS deletion while secure DDNS is enabled.

  2. Remove the computer account from Active Directory, or use a domain account that has permission to delete computer accounts in the target OU.

  3. Delete the CIFS server on ONTAP:
         
         ontap_execute "vserver cifs delete -vserver SVM_NAME -skip-ad-account-delete true"
         

Use `-skip-ad-account-delete true` if the computer account has already been removed from Active Directory or if the account used for deletion doesn't have permission to remove computer objects. In this case, ONTAP removes only the local CIFS configuration and doesn't try to delete an Active Directory object.

By default, `vserver cifs delete` also removes the computer account from Active Directory and prompts for domain administrator credentials. This prompt doesn't work through the ONTAP CLI proxy.




## What's next

  * [Create a volume](https://docs.cloud.google.com/netapp/volumes/docs/ontap/manage-ontap#create_a_volume) to create SMB volumes in the pool.

  * [Peer clusters and SVMs](https://docs.cloud.google.com/netapp/volumes/docs/ontap/peer-clusters-svms).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
