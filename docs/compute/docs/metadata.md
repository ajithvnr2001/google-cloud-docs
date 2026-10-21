---
url: https://docs.cloud.google.com/compute/docs/metadata/
title: About VM metadata \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:41:08.456837+00:00
---

# About VM metadata  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About VM metadata Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Every Compute Engine instance stores its metadata on a metadata server. This metadata is crucial for the configuration and management of your compute instances. The metadata stores details such as instance properties, network settings, and user-defined data. Your compute instances automatically access the metadata server API without additional authorization.

You can programmatically retrieve unique compute instance details and automate tasks like resource allocation, performance optimization, and troubleshooting instance configurations. Compute Engine organizes these metadata keys and values for your compute instances and projects in a hierarchical directory structure, storing entries as key-value pairs.

This overview explains the types and properties of instance-level metadata and project-level metadata, helping you effectively manage and automate your environments.

## VM metadata uses

The following sections describe a few scenarios where you can use metadata entries to manage your VMs.

### Startup and shutdown scripts

The metadata server is particularly useful when used in combination with startup and shutdown scripts because you can use the metadata server to programmatically get unique information about a VM, without additional authorization.

For example, you can write a startup script that gets the metadata key-value pair for a VM's external IP and use that IP in your script to set up a database. Because the Compute Engine predefined metadata keys are the same on every VM, you can reuse your script without having to update it for each VM. This helps you create less brittle code for your applications.

  * For more information about startup scripts, see the [startup script overview](https://docs.cloud.google.com/compute/docs/instances/startup-scripts).
  * For more information about shutdown scripts, see [Running shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript).



### Host maintenance

The metadata server provides information about a VM's scheduling option in the `scheduling/` metadata directory by using the `maintenance-event` key. You can use these metadata values to notify you when a maintenance event is about to happen so that you can prepare your environment for the event. For more information, see [Get live migration notices](https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice).

### Guest attributes

Guest attributes are a specific type of custom metadata that your applications can write to while running on your VMs. Use guest attributes only for use cases that require small amounts of data that don't change frequently. For more information about guest attributes, see [Set and query guest attributes](https://docs.cloud.google.com/compute/docs/metadata/manage-guest-attributes).

### Partner attributes

**Note:** If you're using managed workload identities, using partner attributes with managed workload identities has been deprecated.

Partner attributes are a specific type of instance metadata. Google Cloud services can use partner attributes to create a namespace within which they can define instance metadata entries. You can set, update, delete, and view the values of the instance metadata entries to configure that service.

## Metadata security considerations

When you make a request to get information from the metadata server, your request and the subsequent metadata response never leave the physical host that is running the VM.

However, any process that can [query the metadata URL](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata), has access to all values in the metadata server. This includes any custom metadata values, client certificates, and private keys that you write to the server. Google recommends that you exercise caution when writing sensitive values to the metadata server or when running third-party processes. You must sandbox any process that shouldn't be able to access the metadata server.

## Pricing

Interacting with the metadata server, from within a VM, does not incur costs or impact your Compute Engine API quotas. This applies to both querying metadata entries and writing guest attributes.

However, managing metadata by using the `gcloud` CLI or the Compute Engine API from outside the VM is still subject to [standard API quotas](https://docs.cloud.google.com/compute/api-quota) for your project.

The following list describes how the metadata server handles costs and quotas for calls made from within the VM:

  * **Costs** : calls to the metadata server, including those using the DNS name (`metadata.google.internal`) or IP addresses (`169.254.169.254` or `fd20:ce::254`), don't incur egress or service charges.
  * **Compute Engine API quota** : calls to the metadata server don't consume `compute.googleapis.com` API rate limits or regional quotas.
  * **IAM API quota** : the metadata server doesn't interact with global Identity and Access Management API quotas.
  * **Throttling** : the metadata server has internal limits, but standard polling patterns shouldn't cause throttling.



## Metadata server endpoints

The metadata server is accessible from both HTTP and HTTPS endpoints.

### HTTP metadata server endpoints

HTTP endpoints are accessible from all compute instance types, including Shielded VMs.

You can use the following endpoints to access the metadata server using HTTP:

  * DNS Name (**Recommended**): `http://metadata.google.internal/computeMetadata/v1`
  * IPv4 address: `http://169.254.169.254/computeMetadata/v1`
  * IPv6 address (only for IPv6-only VMs): `http://[fd20:ce::254]/computeMetadata/v1`



### HTTPS metadata server endpoints

HTTPS metadata server endpoints provide added security for transmission of information between the metadata server and the VM. These endpoints are only available for Shielded VMs.

You can use the following endpoints to access the metadata server from a Shielded VM using HTTPS:

  * DNS Name (**Recommended**): `https://metadata.google.internal/computeMetadata/v1`
  * IPv4 address: `https://169.254.169.254/computeMetadata/v1`
  * IPv6 address (only for IPv6-only VMs): `https://[fd20:ce::254]/computeMetadata/v1`



#### Benefits of using the HTTPS metadata server endpoint

Using the HTTPS endpoint to query the metadata server provides the following benefits:

  * _Improves security_ : helps to prevent unauthorized access to your sensitive metadata. It prevents an attacker from being able to perform any of the following actions:

    * Spoofing or impersonating the metadata server to gain access to a VM
    * Viewing or tampering with sensitive metadata before it reaches the VM 
  * _Reduces costs_ : helps you avoid the costs associated with security breaches




#### How the process works

For shielded VMs that have the guest environment installed, the following processes take place on your VM:

  1. Compute Engine creates three certificates as follows:

     * **A self-signed root certificate:** a unique certificate Compute Engine generates for the VM. Compute Engine generates this certificate only on the first boot of the VM, and it is valid for 50 years.
     * **A server identity certificate:** a certificate for the metadata server.
     * **A client identity certificate:** a certificate for the client. The metadata server does not cache this certificate. The guest environment receives a new certificate from the metadata server on each call to the client certificate endpoint. This certificate is valid for 7 days. The guest environment must call the endpoint at least every 7 days to get a new certificate and maintain a valid one.

For storage locations of client identity and root certificates, see Where are certificates stored.

  2. On first boot, Compute Engine transfers the public portion of the root certificate to the guest environment of the VM by using a Google-generated UEFI variable. This root certificate is then stored on the VM.

  3. Periodically, the guest environment requests a client identity certificate. When this happens, the guest agent downloads this certificate from the metadata server and validates it by using the root certificate for that VM.




When you make a [query to the HTTPS metadata server endpoint](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#query-https-mds), you specify the client identity certificates which are then used by the metadata server and the VM to verify that this query is authorized.

#### Enable automatic certificate setup

If you want your instances or projects to automatically set up the HTTPS MDS certificates, set the `disable-https-mds-setup` metadata key on your instance or project to `FALSE`.

For more information, see [Predefined Metadata Keys](https://docs.cloud.google.com/compute/docs/metadata/predefined-metadata-keys).

#### Where are certificates stored

The following sections list the storage location for root and client identity certificates that are generated by Compute Engine.

##### Root certificates

###  CentOS/RHEL/Rocky 

Root certificates for CentOS, Red Hat Enterprise Linux (RHEL), and Rocky Linux VMs are stored in the following location:
    
    
    /run/google-mds-mtls/root.crt

###  Debian/Ubuntu 

Root certificates for Debian and Ubuntu VMs are stored in the following location:
    
    
    /run/google-mds-mtls/root.crt

###  Fedora 

Root certificates for Fedora VMs are stored in the following location:
    
    
    /run/google-mds-mtls/root.crt

###  SLES 

Root certificates for SUSE Linux Enterprise Server (SLES) VMs are stored in the following location:
    
    
    /run/google-mds-mtls/root.crt

###  Windows 

Root certificates for Windows VMs are stored in the following location:
    
    
    C:\ProgramData\Google\ComputeEngine\mds-mtls-root.crt

##### Client identity certificates

Client identity certificates are accessible to all processes that are running on the VM. This is needed so that all processes have access to the metadata server by using the HTTPS endpoint, similar to the HTTP endpoint. For more information, see Metadata security considerations.

###  Linux 

Client identity certificates for Linux VMs are stored in the following location:
    
    
    /run/google-mds-mtls/client.key

###  Windows 

Client identity certificates for Windows VMs are stored in the following locations:

  * C:\ProgramData\Google\ComputeEngine\mds-mtls-client.key




#### Enabling root certificate storage in OS trust store

If you want Compute Engine to automatically add the HTTPS metadata server root certificate to your OS trust store, set the `enable-https-mds-native-cert-store` metadata key on your instance or project to `TRUE`.

If you enable this option, Compute Engine adds the root certificate to the following locations in addition to their default location.

###  CentOS/RHEL/Rocky 
    
    
    /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem

###  Debian/Ubuntu 
    
    
    /etc/ssl/certs/ca-certificates.crt

###  Fedora 
    
    
    /etc/pki/tls/certs/ca-bundle.crt

###  SLES 
    
    
    /etc/ssl/ca-bundle.pem

###  Windows 

**Caution:** Adding certificates to the OS trust store might cause issues with LDAPS. For more information about these potential issues, see [Microsoft documentation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/enable-ldap-over-ssl-3rd-certification-authority#possible-issues).
    
    
    Cert:\LocalMachine\Root

For more information, see [Predefined Metadata Keys](https://docs.cloud.google.com/compute/docs/metadata/predefined-metadata-keys).

#### Root certificate rotation

The HTTPS metadata server root certificate is rotated any time an instance starts and stops. When this occurs, any certificates based on the previous root certificate are no longer valid for making HTTPS connections to the metadata server. If automatic certificate setup is enabled, then the guest environment updates the previous client and root certificates on the file system using the same process as on a first boot.

## Predefined and custom metadata keys

Each metadata entry is stored on the metadata server as key-value pairs. Metadata keys are case sensitive. Your keys can be either predefined or custom metadata keys. 

### Predefined metadata keys

Predefined metadata keys are metadata keys that are created by Compute Engine. When you create a VM, Compute Engine automatically sets the metadata values for some of these keys on that VM—for example, the VM instance ID or the project ID. For predefined keys where Compute Engine doesn't automatically set a value, you can choose from a set of values that are available depending on the system configuration. For example, to enable OS login for a VM, you can set the value of the `enable-oslogin` predefined key to `TRUE` for that VM. To disable OS login for that VM, you can update the value of the key to `FALSE`. You can only update the values for these keys but not the keys themselves. 

For more information about predefined metadata keys and a list of these keys, see [Predefined metadata keys](https://docs.cloud.google.com/compute/docs/metadata/predefined-metadata-keys).

### Custom metadata keys

Custom metadata enables you to create and use your own metadata key-value pairs on an individual VM or a project. You can add new custom metadata keys, update the values of your existing keys, and remove any custom metadata entries when you don't need them. Setting custom metadata is useful for passing in arbitrary values to VMs in a project. It is also useful for creating [startup](https://docs.cloud.google.com/compute/docs/startupscript) and [shutdown](https://docs.cloud.google.com/compute/docs/shutdownscript) scripts. 

To learn how you can add, update, or remove custom metadata for your VMs, see [Configure custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata). 

## Types of metadata

VM metadata entries can provide information specific to an individual VM or a project. Your metadata is divided into project, zonal, and instance metadata, based on the scope at which you set the metadata.

### Project metadata

Project metadata is defined at project scope and provides information that applies to all VMs in a project. When you set this metadata, the metadata entries propagate to all VMs in that project.

You can use both predefined and custom metadata keys to set project metadata. Learn more about [predefined project metadata keys](https://docs.cloud.google.com/compute/docs/metadata/predefined-metadata-keys#project-metadata) and how to [set custom project metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-wide-metadata).

### Zonal metadata

Zonal metadata is defined at a zonal scope within a project and provides information about VMs in that specific zone in that project. When you set zonal metadata, the metadata entries propagate to all VMs in that configured zone in that project. When compared to project metadata, zonal metadata helps you with fault isolation and provides greater reliability.

Compute Engine doesn't provide any predefined keys for zonal metadata. You must create your own custom metadata keys to set zonal metadata. Learn more about how to [set custom zonal metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-zonal-metadata).

**Tip:** Google recommends that you use zonal metadata over project metadata when you have workloads that require regional isolation. By using zonal metadata values, you gain more control over the project metadata for your VMs and limit the impact of any incorrect metadata updates to VMs within the specific zone.

### Instance metadata

Instance metadata provides information about a specific VM instance. You set instance metadata separately for each individual VM instance.

You can use both predefined and custom metadata keys to set instance metadata. Learn more about predefined instance metadata keys and how to [Set custom instance metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-instance-metadata).

## How metadata is arranged

Compute Engine stores and maintains the metadata keys and values for your VMs and projects in directory listings. Depending on the type of metadata, Compute Engine stores metadata entries in one of the following directories:

Type of metadata | Directory  
---|---  
Project and zonal metadata | 

  * HTTP endpoint: 
        
        http://metadata.google.internal/computeMetadata/v1/project

  * HTTPS endpoint: 
        
        https://metadata.google.internal/computeMetadata/v1/project


  
Instance metadata | 

  * HTTP endpoint: 
        
        http://metadata.google.internal/computeMetadata/v1/instance

  * HTTPS endpoint: 
        
        https://metadata.google.internal/computeMetadata/v1/instance


  
  
Each directory stores metadata entries in the form of key-value pairs. Some metadata entries are also directories that contain other metadata keys. The metadata entries that function as directories are marked by a trailing slash (`/`) in the metadata key name. For example, `/project/attributes/` is a directory under the `project/` directory that contains other metadata keys. To create your own metadata directory listing, you must use a trailing slash (`/`) in the metadata key name when you create your custom metadata entry.

When you query a metadata endpoint, the format of the response body depends on the endpoint. If you query an endpoint that stores a single value, such as `hostname`, the response body contains that value as plain text. If you query an endpoint that acts as a directory, such as `/project/attributes/`, the response body contains a list of the entries within that directory, with one entry per line.

For more information about querying metadata endpoints, including how to recursively query directories or format the response as JSON, see [View and query VM metadata](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata).

Project and zonal metadata entries are stored in the same `project/` directory. If you set different values for the same custom metadata keys for VMs on a project level and on a zonal level, then the zonal metadata values for those keys take precedence over the project metadata values in the respective zones. 

  * If you add a zonal metadata value for a metadata key that already has a project metadata value, then Compute Engine overrides the project metadata value for the VMs in this specified zone and updates the `/project` directory with the zonal value.
  * If you add a new project metadata value for a metadata key that already has a zonal metadata value, then nothing changes. Compute Engine retains the zonal metadata value in the `/project` directory in the specific zone.
  * If you don't specify a zonal metadata value for a custom metadata key in a specific zone, but the key has a project metadata value, then your VMs continue to have the project metadata values in those zones.



For example, suppose you define a project metadata pair of `key-1=value-1`. Suppose you also define a zonal metadata pair of `key-1=zonal-value-1` for only the `us-central1-a` zone. All the VMs in the `us-central1-a` zone for your project inherit `key-1=zonal-value1` as the metadata pair. The metadata pair remains `key-1=value-1` for all VMs in other zones where you haven't set any zonal metadata for `key-1`. 

## What's next?

  * Learn about the [predefined metadata keys](https://docs.cloud.google.com/compute/docs/metadata/predefined-metadata-keys) that Google Cloud offers.
  * Learn how to [configure custom metadata entries](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).
  * Learn how to [set and query guest attributes](https://docs.cloud.google.com/compute/docs/metadata/manage-guest-attributes).
  * After setting values for your metadata keys, learn how to [view and query VM metadata information](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata) for a VM or a project.
  * Learn how to [get live migration notices](https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice) from the metadata server.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
