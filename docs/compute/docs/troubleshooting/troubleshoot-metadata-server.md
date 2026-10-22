---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-metadata-server/
title: Troubleshooting metadata server access issues \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:53.415700+00:00
---

# Troubleshooting metadata server access issues  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-metadata-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting metadata server access issues Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document shows you how to resolve issues with the Compute Engine metadata server.

Compute Engine VMs store metadata on a metadata server. VMs automatically have access to the metadata server API without any additional authorization. However, sometimes VMs might lose access to the metadata server due to one of the following causes:

  * Failure to resolve the metadata server domain name
  * Connection to the metadata server is blocked by one of the following: 
    * OS level firewall configuration
    * Proxy setup
    * Custom routing



When VMs can't access the metadata server, some processes might fail.

For information about troubleshooting the `gke-metadata-server`, see [Troubleshoot GKE authentication issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/authentication).

## Before you begin

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




## Troubleshoot server codes

The following server codes are returned when you make calls to the Compute Engine metadata server. Review this section to see how to respond to each server code returned by the metadata server.

### Common server codes

These server codes are frequently returned from the metadata server.

**Server code** | **Description** | **Resolution**  
---|---|---  
200 | _OK_ : the request was successful | N/A  
400 | _Bad Request:_ this error status is returned for many different scenarios such as when a request has improper query parameters or requirements for that endpoint have not been met.  | Review the error message for suggestions on how to fix the error  
403 | _Forbidden:_ this error status is returned in the following scenarios: 

  * The requested endpoint is disabled by project or instances settings
  * The request fails security checks. This issue can happen if your TCP connection to the server was closed at the networking layer.

| Check your project and instance settings to ensure the endpoint is enabled, or check your network configuration  
404 | _Not Found:_ the requested endpoint doesn't exist | Fix the request path  
429 | _Too many requests:_ this occurs because some endpoints use rate limiting to prevent overloading on the backing service. Retrying with exponential backoff is strongly encouraged. For more information, see the list of rate limited endpoints. | Wait a few seconds and retry the call  
503 | _Service unavailable:_ the metadata server isn't ready to serve. The metadata server might return the `Error 503` status code in any of the following circumstances: 

  * The metadata server is still booting
  * The metadata server is in the process of migrating
  * The metadata server is temporarily unavailable
  * The host machine is performing a maintenance event
  * The metadata server might return a `503` when rate limiting some endpoints.

| 503s are transient and should resolve after, at most, a few seconds. To resolve, wait a few seconds and retry the call.  
  
### Rare server codes

These server codes, though rare, might also be returned from the metadata server.

**Server code** | **Description** | **Resolution**  
---|---|---  
301 | _Moved Permanently:_ this is provided for paths that have redirects | Update the request path  
405 | _Not Allowed:_ this error code is returned if an unsupported method is requested.  
  
The metadata server only supports `GET` operations, with the exception of guest-writable metadata, which allows `SET` operations. | Update the method in your request path  
  
### Rate limited endpoints error codes

The following endpoints are rate limited and might return error codes. To handle these returned error codes, see Retry Guidance.

**Endpoint** | **Status Code** | **Description**  
---|---|---  
`oslogin/` | `429` | OS Login rate limits are shared between user, authorize, and group requests.  
`instance/service-accounts/identity` | `429` | The identity signing endpoint returns `429` response code to indicate a rate limited response.  
`instance/service-accounts/default/token` | `429` | Cached tokens in the metadata server are not rate limited. Non-cached tokens are subject to rate limiting.  
`instance/guest-attributes/` | `429`, `503` | Guest attributes requests might be throttled if you exceed 3 QPS or 10 QPM. If throttling occurs, error codes `429` or `503` are returned.  
  
### Retry guidance

The metadata server routinely returns 503 and 429 error codes. To make your applications resilient, we recommend that you implement retry logic for applications that query the metadata server. We also suggest that you implement [exponential backoff](https://wikipedia.org/wiki/Exponential_backoff) in your scripts to account for any possible rate limiting.

## Troubleshoot failed requests to the metadata server

The following are example errors that you might encounter if your VM fails to reach the metadata server:
    
    
    curl: (6) Could not resolve host: metadata.google.internal
    
    
    
    postAttribute error: Put "http://metadata.google.internal/computeMetadata/v1/instance/guest-attributes/guestInventory/ShortName": dial tcp: lookup metadata.google.internal on [::1]:53: read udp [::1]:58319->[::1]:53: read: connection refused
    

If your VM has lost access to the metadata server, do the following:

###  Linux 

  1. [Connect](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) to your Linux VM.
  2. From your Linux VM, run the following commands to test connectivity to the metadata server:

     1. Query the Domain Name Server:
            
            nslookup metadata.google.internal

The output should look similar to the following for VMs using **IPv4** :
            
            Server:         169.254.169.254
            Address:        169.254.169.254#53
            
            Non-authoritative answer:
            Name:   metadata.google.internal
            Address: 169.254.169.254
            

     2. Check that the metadata server is reachable. To verify, run the following commands:
            
            ping -c 3 metadata.google.internal

The output should look similar to the following:
            
            PING metadata.google.internal (169.254.169.254) 56(84) bytes of data.
            64 bytes from metadata.google.internal (169.254.169.254): icmp_seq=1 ttl=255 time=0.812 ms
            
            
            ping -c 3 169.254.169.254

The output should look similar to the following:
            
            PING 169.254.169.254 (169.254.169.254) 56(84) bytes of data.
            64 bytes from 169.254.169.254: icmp_seq=1 ttl=255 time=1.11 ms
            

     3. If using an IPv6 only instance, then check that the IPv6 metadata server is reachable. To verify, run the following command:
            
            ping -c 3 fd20:ce::254

The output should look similar to the following:
            
            PING fd20:ce::254(fd20:ce::254) 56 data bytes
            64 bytes from fd20:ce::254: icmp_seq=1 ttl=255 time=1.11 ms
            

     4. If the output of the preceding commands matches the suggested output, your VM is connected to the metadata server and no further action is required. If the commands fail, do the following:

        1. Check that the name server is configured to the Metadata server:
               
               cat /etc/resolv.conf

The output should look similar to the following:
               
               domain ZONE.c.PROJECT_ID.internal
               search ZONE.c.PROJECT_ID.internal. c.PROJECT_ID.internal. google.internal.
               nameserver 169.254.169.254
               

If the output doesn't have the preceding lines, refer to your operating system documentation for information about how to edit the [DHCP Policy](https://kb.isc.org/docs/isc-dhcp-41-manual-pages-dhclientconf) to persist the name server configuration to `169.254.169.254`. If [zonal DNS](https://docs.cloud.google.com/compute/docs/internal-dns#zonal-dns-config) settings are applied to the VMs within your project, changes to `/etc/resolv.conf` are overwritten in one hour. If your project is still using a [global DNS](https://docs.cloud.google.com/compute/docs/internal-dns#global-dns-config), the `resolv.conf` file is reverted to the default DHCP in 24 hours.

        2. Check that the mapping between the metadata server domain name and its IP address exist:
               
               cat /etc/hosts

The following line should be in the output:
               
               169.254.169.254 metadata.google.internal  # Added by Google
               

If the output doesn't have the preceding line, run the following command:
               
               echo "169.254.169.254 metadata.google.internal" >> /etc/hosts




###  Windows 

  1. [Connect](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) to your Windows VM.
  2. From your Windows VM, run the following commands:

     1. Query the Domain Name Server:
            
            nslookup metadata.google.internal

The output should look similar to the following:
            
            Server:  UnKnown
            Address:  10.128.0.1
            
            Non-authoritative answer:
            Name:    metadata.google.internal
            Address:  169.254.169.254
            

     2. Check that the metadata server is reachable. To verify, run the following commands:
            
            ping -n 3 metadata.google.internal

The output should look similar to the following: 
            
            Pinging metadata.google.internal [169.254.169.254] with 32 bytes of data:
            Reply from 169.254.169.254: bytes=32 time=1ms TTL=255
            
            
            ping -n 3 169.254.169.254

The output should look similar to the following:
            
            Pinging 169.254.169.254 with 32 bytes of data:
            Reply from 169.254.169.254: bytes=32 time=1ms TTL=255
            

     3. If your VM has an IPv6 address, then check that an IPv6 only instance is reachable. To verify, run the following command:
            
            ping -n 3 fd20:ce::254

The output should look similar to the following for IPv6 VMs:
            
            Pinging fd20:ce::254 with 32 bytes of data:
            Reply from fd20:ce::254: bytes=32 time=1ms TTL=255
            

     4. If the output of the preceding commands matches the suggested output, your VM is connected to the metadata server and no further action is required. If the commands fail, do the following:

        1. Check that there's a persistent route to the metadata server by running the command:
               
               route print

The output should contain the following:
               
               Persistent Routes:
               Network Address          Netmask  Gateway Address  Metric
               169.254.169.254  255.255.255.255         On-link        1
               

If the output doesn't have the preceding line, add the route using the following commands:
               
               $Adapters = Get-NetKVMAdapterRegistry
               $FirstAdapter = $Adapters | Select-Object -First 1
               route /p add 169.254.169.254 mask 255.255.255.255 0.0.0.0 'if' $FirstAdapter.InterfaceIndex metric 1

        2. Check that the mapping between the metadata server domain name and its IP address exists:
               
               type %WINDIR%\System32\Drivers\Etc\Hosts

The following line should be in the output:
               
               169.254.169.254 metadata.google.internal  # Added by Google
               

If the output doesn't have the preceding line, run the following command:
               
               echo 169.254.169.254 metadata.google.internal >> %WINDIR%\System32\Drivers\Etc\Hosts




## Troubleshoot failed requests while using a network proxy

A network proxy server prevents VM's direct access to the Internet. All queries sent from within a VM are handled by the proxy server instead.

When using an application that gets credentials from the metadata server, like an authentication token, the VM requires direct access to the metadata server. If the VM is behind a proxy, you must set the `NO_PROXY` configuration for both the IP address and Hostname.

If you don't set the `NO_PROXY` configuration, you might see errors when running Google Cloud CLI commands or querying the metadata server directly since the calls to `metadata.google.internal` will be sent to the proxy without having them resolved locally on the instance itself.

The following is an example of an error that you might see:
    
    
    ERROR 403 (Forbidden): Your client does not have permission to get URL
    

To resolve this proxy issue, add the metadata server hostname and IP address to the environment variable `NO_PROXY` by doing the following:

###  Linux 

  1. [Connect](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) to your Linux VM.
  2. From your Linux VM, run the following commands:
         
         export no_proxy=169.254.169.254,fd20:ce::254,metadata,metadata.google.internal

To save the changes, run the following command:
         
         echo no_proxy=169.254.169.254,fd20:ce::254,metadata,metadata.google.internal >> /etc/environment




###  Windows 

  1. [Connect](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) to your Windows VM.
  2. From your Windows VM, run the following commands:
         
         set NO_PROXY=169.254.169.254,fd20:ce::254,metadata,metadata.google.internal

To save the changes, run the following command:
         
         setx NO_PROXY 169.254.169.254,fd20:ce::254,metadata,metadata.google.internal /m




## Troubleshoot failed requests to the HTTPS metadata server endpoint

This section covers some of the errors that you might see when you are [querying the HTTPS metadata server endpoint](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#query-https-mds).

The errors listed in this section are returned when you query using the cURL tool to query, however the returned error message is similar for other tools.

### Incorrect client certificate

The following errors occur if you provide an incorrect value for the `-E` flag.

  * curl: (56) OpenSSL SSL_read: error:1409445C:SSL routines:ssl3_read_bytes:tlsv13 alert certificate
        required, errno 0

  * curl: (58)  unable to set private key file:

  * curl: (58) could not load PEM client certificate, OpenSSL error error:02001002:system library:fopen:No such file or directory




To resolve this issue, provide the correct path to the client identity certificate. To view the location for client identity certificates, see [Client identity certificates](https://docs.cloud.google.com/compute/docs/metadata/overview#https-mds-client-certs).

### Incorrect hostname

The following error occurs if the hostname used to access the metadata server isn't found on the certificate.
    
    
    curl: (60) SSL: no alternative certificate subject name matches target host name

To resolve this issue, verify that the root URL or hostname in your query is `metadata.google.internal`. For more information about the root URL for the metadata server, see [Parts of a metadata request](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#parts-of-a-request).

### Incorrect root or client certificate

You might see the following error when you query the HTTPS metadata server endpoint:
    
    
    curl: (77) error setting certificate verify locations:

This might happen in the following scenarios:

  * The path for the `--cacert` flag might be malformed
  * The root certificate might be missing from the trust store



To resolve this issue, you need to specify both the root certificate and the client certificate when querying the https endpoint. For certificate locations, see [Where are certificates stored](https://docs.cloud.google.com/compute/docs/metadata/overview#https-mds-certificates).

For example, to query the boot image for a VM, run the following query:
    
    
    user@myinst:~$ curl "https://metadata.google.internal/computeMetadata/v1/instance/image" \
        -E /run/google-mds-mtls/client.key \
        --cacert /run/google-mds-mtls/root.crt \
        -H "Metadata-Flavor: Google"
    

## Troubleshoot incorrect header format

The metadata server performs formatting checks to ensure that headers comply with the header formatting guideline [RFC 7230 Section 3.2](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2). If the header format fails these checks the following occurs:

  * The request is accepted. However, you'll receive recommendations that you have VMs making requests to the metadata server with incorrectly formatted headers. Recommendations are sent once per VM. You can access these recommendations by using the Google Cloud CLI, or the Recommender REST API.

After you have applied the recommendation, [set the recommendation state to `succeeded`](https://docs.cloud.google.com/recommender/docs/using-api#change-recommendation-state).

  * Starting January 20, 2024, the metadata server denies any request with an incorrectly formatted header.




The following shows examples of valid and invalid header request formats.

Not valid: contains whitespace between the header name and colon
    
    
    Metadata-Flavor : Google

Valid: no whitespace between header name and colon, whitespace after the colon is ignored by the checker
    
    
    Metadata-Flavor: Google

Valid: no whitespace in header
    
    
    Metadata-Flavor:Google

For more information about making queries to metadata server, see [Access VM metadata](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#query).

## Troubleshoot failure to obtain token

You might see one of the following errors when you query the metadata server:

  * ERROR: gcloud crashed (MetadataServerException): HTTP Error 401: Unauthorized

  * curl: (22) The requested URL returned error: 401




These errors might arise if the service account attached to the VM is in a disabled state. To resolve these errors, [enable the service account](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable) or attach different service account.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
