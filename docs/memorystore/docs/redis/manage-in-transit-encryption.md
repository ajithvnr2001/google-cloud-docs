---
url: https://docs.cloud.google.com/memorystore/docs/redis/manage-in-transit-encryption/
title: Manage in-transit encryption \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:52.979826+00:00
---

# Manage in-transit encryption  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/manage-in-transit-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Manage in-transit encryption Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to enable in-transit encryption during Redis instance creation, and how to manage in-transit encryption for the instance. In-transit encryption uses the Transport Layer Security (TLS) protocol.

For information on the general behavior and benefits of using in-transit encryption, see [In-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption).

For a list of permissions that a user needs in order to perform the management tasks on this page, see [In-transit encryption permissions](https://docs.cloud.google.com/memorystore/docs/redis/access-control#in-transit_encryption_permissions).

You can only enable in-transit encryptions when you initially create your Redis instance. In-transit encryption can't be disabled for instances created in this way.

**Important** : Certificate Authorities (CAs) are valid for 10 years from the date that they're created. New CAs are available for you to download and install on your clients that connect to the instance about five years before the current CAs expire. Existing CAs are valid until their expiration dates. After the CAs expire, you can uninstall them from your clients.

For instances that have replicas, replicated data is encrypted fully at the network level, based on Google Cloud encryption standards. Also, Memorystore for Redis supports the TLS protocol, versions 1.2 and later.

## Creating a Redis instance with in-transit encryption

### Console

When you [create a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances), select **Enable in-transit encryption**.

### gcloud

To [create a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances) that has in-transit encryption, enter the following command, replacing variables with appropriate values:
    
    
    gcloud redis instances create instance-id --transit-encryption-mode=SERVER_AUTHENTICATION --size=size --region=region-id
    

Where:

  * `--transit-encryption-mode=SERVER_AUTHENTICATION` enables in-transit encryption for your instance.



## Downloading the Certificate Authority

### Console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. View your instance's _Instance details_ page by clicking on your _Instance ID_.

  3. Click the **Download** or **Download All** button under **TLS server certificate**.




### gcloud

If in-transit encryption is enabled on your instance, you see the contents of the Certificate Authority(ies) when you run the following command:
    
    
    gcloud redis instances describe instance-id --region=region
    

The response body will include all applicable Certificate Authorities. The following is an example Certificate Authority (CA) for Memorystore for Redis:
    
    
    -----BEGIN CERTIFICATE-----
    MIIDnTCCAoWgAwIBAgIBADANBgkqhkiG9w0BAQsFADCBhTEtMCsGA1UELhMkNzYx
    NTc4OGMtMTI2Yi00Nzk0LWI2MWMtY2YxOWE2Y2Y1ZjNiMTEwLwYDVQQDEyhHb29n
    bGUgQ2xvdWQgTWVtb3J5c3RvcmUgUmVkaXMgU2VydmVyIENBMRQwEgYDVQQKEwtH
    b29nbGUsIEluYzELMAkGA1UEBhMCVVMwHhcNMjAwOTE3MjEzNDE1WhcNMzAwOTE1
    MjEzNTE1WjCBhTEtMCsGA1UELhMkNzYxNTc4OGMtMTI2Yi00Nzk0LWI2MWMtY2Yx
    OWE2Y2Y1ZjNiMTEwLwYDVQQDEyhHb29nbGUgQ2xvdWQgTWVtb3J5c3RvcmUgUmVk
    aXMgU2VydmVyIENBMRQwEgYDVQQKEwtHb29nbGUsIEluYzELMAkGA1UEBhMCVVMw
    ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCyDKmDHZm6tzMhNtKOnp8H
    8+zTv1qA6OkBToVqCjKTTMGO18ovNtAAMjbGvclLuJNLbA2WTTWVttHen6Cn82h0
    3gG9HMk9AwK1cVT7gW072h++TRsYddIRlwnSweRWL8jUX+PNt7CjFqH+sma/Hb1m
    CktHdBOa897JiYHrMVNTcpS8SFwwz05yHUTEVGlHdkvlaJXfHLe6keCMABLyjaMh
    1Jl4gZI2WqLMV680pJusK6FI6q/NmqENFc9ywMEg395lHTK9w9e014WIXg0q7sU3
    84ChVVS2yYOMEUWeov4Qx6XeVfA4ss5t7OCqsMQkvslkE90mJZcVvhBj3QvTH9Rz
    AgMBAAGjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwDQYJKoZIhvcNAQELBQADggEB
    AJkn+MDE4V10DZn4uEc0s0Mg4FEMC1fDewmDYwSNnxRlzfEi+wAX2AaqrJ4m4Qa7
    xIyuSYxArEOY6QeyJyw7/06dom8aAv4aO2p8hE04Ih6QwaTMFIlT2Jf6TidVd3eT
    wfjwFJVoJ+dgxsaCv2uMFZWee5aRHmKzj9LhqPwpWnTs9Q/qmOheUNoe2/1i8yvn
    662M7RZMR7fZH6ETsdz5w1nPXXiRqJ7K0EGKoPNjMlYK3/U1X3sazI4tpMNgTdxG
    rnNh9Sd9REMBmDCPj9dUI9k4hQX4yQZp96fnLT6cet22OPajEKnpzyqJs1s4iX/g
    lEtWs4V/YBhKA56CW6ASZS8=
    -----END CERTIFICATE-----
    
    

Copy and save all of the CAs temporarily so you can [install](https://docs.cloud.google.com/memorystore/docs/redis/enabling-in-transit-encryption#installing_a_certificate_authority_on_your_client) them on clients accessing the Redis instance.

**Important:** When you copy and paste the text of the CAs to your client you _must include_ the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines.

## Installing a Certificate Authority on your client

You must install your Redis instance's Certificate Authority(ies) on the connecting client. CA installation can vary depending on the client type. The steps below explain how to install a CA on a Compute Engine Linux VM.

  1. Connect with SSH to your Compute Engine Linux client.

  2. Create a file called `server_ca.pem` in your client by running the following command:
         
         sudo vim /tmp/server_ca.pem
         

  3. [Download the Certificate Authority](https://docs.cloud.google.com/memorystore/docs/redis/enabling-in-transit-encryption#downloading_the_certificate_authority) and paste it into the previously created `server_ca.pem` file.

The text of the CA must be formatted correctly:  


     * Copy the entire Certificate Authority including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines.
     * Make sure that the text of the CA is completely left justified. There should be no spaces in front of any line of the CA.



## Configuring your client for in-transit encryption

The client that you use to connect to the Redis instance must [support TLS](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption#in-transit_encryption_prerequisites) or use a third-party sidecar to enable TLS.

If your client supports TLS, configure it to point to your Redis instance's IP, port `6378`, and the file containing the Certificate Authority. If you choose to use a sidecar, we recommend [using Stunnel](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance#connect_to_a_redis_instance_securely_by_using_stunnel_and_telnet).

#### Additional client configuration

Some clients do not accept self-signed certificates by default and will require additional configuration.

For example, [Lettuce](https://lettuce.io/) is a popular Java client for Redis. Their documentation provides an example for connecting natively with TLS (see [Example 47](https://lettuce.io/core/release/reference/#ssl)). Given that the Java Security Manager does not allow self-signed certificates by default, an additional option needs to be specified in the Redis URI construction `.withVerifyPeer(false)`.

## Securely connecting to a Redis instance using Stunnel and telnet

For instructions on using Stunnel to enable in-transit encryption on a Compute Engine client, see [Connect to a Redis instance securely by using Stunnel and telnet](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance#connect_to_a_redis_instance_securely_by_using_stunnel_and_telnet).

## Managing Certificate Authority rotation

You should [install](https://docs.cloud.google.com/memorystore/docs/redis/enabling-in-transit-encryption#installing_a_certificate_authority_on_your_client) all [downloadable](https://docs.cloud.google.com/memorystore/docs/redis/enabling-in-transit-encryption#downloading_the_certificate_authority) Certificate Authorities on clients accessing the Redis instance.

Installing the new CA, in addition to the previous CA, [once it becomes available](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption#certificate_authority_rotation) is the simplest form of ensuring that you have the necessary CA when the Certificate Authority rotation event occurs.

Run the following command once a new Certificate Authority is introduced to view the contents of the new CA:
    
    
    gcloud redis instances describe instance-id --region=region
    

Next, copy and paste the newest Certificate Authority into the file in your client in which you saved the previous CA.

The file should use the following format. The order of the CAs does not matter:
    
    
    -----BEGIN CERTIFICATE-----
    MIIDnTCCAoWgAwIBAgIBADANBgkqhkiG9w0BAQsFADCBhTEtMCsGA1UELhMkNzYx
    NTc4OGMtMTI2Yi00Nzk0LWI2MWMtY2YxOWE2Y2Y1ZjNiMTEwLwYDVQQDEyhHb29n
    bGUgQ2xvdWQgTWVtb3J5c3RvcmUgUmVkaXMgU2VydmVyIENBMRQwEgYDVQQKEwtH
    b29nbGUsIEluYzELMAkGA1UEBhMCVVMwHhcNMjAwOTE3MjEzNDE1WhcNMzAwOTE1
    MjEzNTE1WjCBhTEtMCsGA1UELhMkNzYxNTc4OGMtMTI2Yi00Nzk0LWI2MWMtY2Yx
    OWE2Y2Y1ZjNiMTEwLwYDVQQDEyhHb29nbGUgQ2xvdWQgTWVtb3J5c3RvcmUgUmVk
    aXMgU2VydmVyIENBMRQwEgYDVQQKEwtHb29nbGUsIEluYzELMAkGA1UEBhMCVVMw
    ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCyDKmDHZm6tzMhNtKOnp8H
    8+zTv1qA6OkBToVqCjKTTMGO18ovNtAAMjbGvclLuJNLbA2WTTWVttHen6Cn82h0
    3gG9HMk9AwK1cVT7gW072h++TRsYddIRlwnSweRWL8jUX+PNt7CjFqH+sma/Hb1m
    CktHdBOa897JiYHrMVNTcpS8SFwwz05yHUTEVGlHdkvlaJXfHLe6keCMABLyjaMh
    1Jl4gZI2WqLMV680pJusK6FI6q/NmqENFc9ywMEg395lHTK9w9e014WIXg0q7sU3
    84ChVVS2yYOMEUWeov4Qx6XeVfA4ss5t7OCqsMQkvslkE90mJZcVvhBj3QvTH9Rz
    AgMBAAGjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwDQYJKoZIhvcNAQELBQADggEB
    AJkn+MDE4V10DZn4uEc0s0Mg4FEMC1fDewmDYwSNnxRlzfEi+wAX2AaqrJ4m4Qa7
    xIyuSYxArEOY6QeyJyw7/06dom8aAv4aO2p8hE04Ih6QwaTMFIlT2Jf6TidVd3eT
    wfjwFJVoJ+dgxsaCv2uMFZWee5aRHmKzj9LhqPwpWnTs9Q/qmOheUNoe2/1i8yvn
    662M7RZMR7fZH6ETsdz5w1nPXXiRqJ7K0EGKoPNjMlYK3/U1X3sazI4tpMNgTdxG
    rnNh9Sd9REMBmDCPj9dUI9k4hQX4yQZp96fnLT6cet22OPajEKnpzyqJs1s4iX/g
    lEtWs4V/YBhKA56CW6ASZS8=
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    MIIDnTCCAoWgAwIBAgIBADANBgkqhkiG9w0BAQsFADCBhTEtMCsGA1UELhMkYjg4
    ZTUzYTMtODdmNC00N2VhLWJjN2MtYTdhMzM4NmIwZmU4MTEwLwYDVQQDEyhHb29n
    bGUgQ2xvdWQgTWVtb3J5c3RvcmUgUmVkaXMgU2VydmVyIENBMRQwEgYDVQQKEwtH
    b29nbGUsIEluYzELMAkGA1UEBhMCVVMwHhcNMjAwOTE4MjEzMTI3WhcNMzAwOTE2
    MjEzMjI3WjCBhTEtMCsGA1UELhMkYjg4ZTUzYTMtODdmNC00N2VhLWJjN2MtYTdh
    MzM4NmIwZmU4MTEwLwYDVQQDEyhHb29nbGUgQ2xvdWQgTWVtb3J5c3RvcmUgUmVk
    aXMgU2VydmVyIENBMRQwEgYDVQQKEwtHb29nbGUsIEluYzELMAkGA1UEBhMCVVMw
    ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDEO4Zs/So5DA6wtftkAElD
    8BVREob4gby2mGBYAtd3JJQKFC+zIqCf2DhrWihrCeXhsdsZqJUF16E3MsCCWS2T
    UWt6T37zObU2fzKmb7X+TSw1tunIUcIXwWzoMhqdGrIvfI9guMbF+KssQIjDMs9M
    G/hY6cY1NB5THOxXqcxzYrwSKB1EE160EDz4RgKAYQhw7AyVOBBAbWqA5pTEDuUy
    qpsz+NFpKYTwaeTpzil0xIl0JJS3DOd4G7ZnMG2wFT2j3wt+P0SkAPuOWgmX82iO
    gGmKoaCh3KcICie/rZRTfsRPjMm+yswRQRDeLB5eoMmH+gbUInVZU0qOJ/7gOYEb
    AgMBAAGjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwDQYJKoZIhvcNAQELBQADggEB
    AF4xlEbwLUK5VjoKlJBtKXLYrYcW+AbQLhZQFP8exE8bOW7p39h+5J0nl3ItPxu6
    97BCt1P5TFisba8pBxaExiDsYmjKQrhtizMkzl5h9hGksOgoLlAqaaxfA97+Q9Tq
    5gaYChESur/159Z3jiM47obKoZmHfgSgr//7tjII7yZxUGhOjIVffv/fEa4aixqM
    0yH1V1s8hWHZeui2VFrHmTxY20IH9ktyedjSUgnFXzsEH6sbR18p0wBZqyrrtURs
    DaUIeoOHfHgEJM8k/wphSJI0V6pMC6nax2JhexLTRiUsiGTLRDe3VtsdWqS2DLa9
    9DmrfdF0eFrfWw3VRNLwwXg=
    -----END CERTIFICATE-----
    

All you need to do to make sure that you have the required CA is to make sure that the CAs saved in your client file match those shown by `gcloud redis instances describe`. After a rotation event begins there are multiple CAs to ensure ample time for rotations with minimal downtime.

## What's next

  * Read the overview for [In-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption).
  * Learn about the [Redis AUTH feature](https://docs.cloud.google.com/memorystore/docs/redis/auth-overview) on Memorystore for Redis.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
