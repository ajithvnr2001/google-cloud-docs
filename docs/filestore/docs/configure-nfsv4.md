---
url: https://docs.cloud.google.com/filestore/docs/configure-nfsv4/
title: About NFSv4.1 protocol \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:34.015448+00:00
---

# About NFSv4.1 protocol  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/configure-nfsv4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  About NFSv4.1 protocol Stay organized with collections  Save and categorize content based on your preferences. 

The following guide describes the NFSv4.1 protocol.

Filestore offers NFSv4.1 protocol support for instances created in the following [service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers):

  * Zonal
  * Regional
  * Enterprise



This capability can be integrated with [Managed Service for Microsoft Active Directory (Managed Microsoft AD)](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview) to support workloads that require client and server authentication, message data integrity checks, and in-transit data encryption, capabilities previously unavailable in Filestore.

Authentication is supported using [LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) and [Kerberos](https://web.mit.edu/kerberos/krb5-latest/doc/) and includes the following security flavors (settings):

  * Client and server authentication (`krb5`).
  * Message integrity checks (`krb5i`). Includes the capabilities of the previous setting.
  * In-transit data encryption (`krb5p`). Includes the capabilities of the previous setting.



Managed Microsoft AD is the only fully-managed Google Cloud solution that supports both [LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) and [Kerberos](https://web.mit.edu/kerberos/krb5-latest/doc/), requirements for the NFSv4.1 protocol and its security and privacy benefits. While integration with Managed Microsoft AD is not required, it is highly recommended for an optimal Google Cloud user experience to manage user accounts and fluctuating groups and permissions.

## Should you use NFSv4.1?

Many enterprise organizations rely on legacy systems for business-critical operations. Many of these systems require authentication and in-transit encryption for their network file storage. NFSv3 was not designed with authentication in mind. Filestore's NFSv4.1 protocol integration with Managed Microsoft AD now meets this critical user requirement.

For more information on NFSv4.1 benefits, see [About supported protocols](https://docs.cloud.google.com/filestore/docs/about-supported-protocols).

## Understanding network-based access control lists (ACLs) in NFSv4.1.

In NFSv3, only the `sys` security flavor is supported. This setting trusts the user `uid` and `gid` provided by the client during mounting.

In the Filestore NFSv4.1 protocol, several network ACL security flavors or settings are available:

  * `krb5`

Authenticates the client using a Kerberos ticket, which is validated against the Managed Microsoft AD Kerberos server.

  * `krb5i`

Includes the authentication provided by `krb5` and also uses Kerberos to run message integrity checks on all network traffic to and from the instance.

  * `krb5p`

Includes the authentication provided by `krb5` and message integrity checks of `krb5i` and also uses Kerberos for in-transit data encryption.




If you want to take advantage of these options, Managed Service for Microsoft Active Directory integration is required. For more information, see [Create a Filestore instance with Managed Microsoft AD](https://docs.cloud.google.com/filestore/docs/configure-nfsv4-managed-ad).

If a Managed Service for Microsoft Active Directory domain isn't specified, only the `sys` security flavor is supported.

For more information, see [NFSv4.1 limitations](https://docs.cloud.google.com/filestore/docs/about-supported-protocols#nfsv4-limitations).

## Mounting Filestore NFSv4.1 instances on Linux clients

The following steps show you how to mount instances on Linux clients.

  * Mount with `sec=sys` for standard NFS permissions:
        
        sudo mount -vvvv -t nfs4 -o vers=4.1,sec=sys,rw \ FILESTORE-INSTANCE-FQDN:/INSTANCE_SHARE_POINT /MOUNT_POINT
        

  * Mount with `sec=krb5` for Kerberos-based authentication:
        
        sudo mount -vvvv -t nfs4 -o vers=4.1,sec=krb5,rw \ FILESTORE-INSTANCE-FQDN:/INSTANCE_SHARE_POINT /MOUNT_POINT
        

  * Mount with `sec=krb5i` for Kerberos-based authentication and message integrity checks:
        
        sudo mount -vvvv -t nfs4 -o vers=4.1,sec=krb5i,rw \ FILESTORE-INSTANCE-FQDN:/INSTANCE_SHARE_POINT /MOUNT_POINT
        

  * Mount with `sec=krb5p` for Kerberos-based authentication, integrity checks, and in-transit encryption:
        
        sudo mount -vvvv -t nfs4 -o vers=4.1,sec=krb5p,rw \ FILESTORE-INSTANCE-FQ
        DN:/INSTANCE_SHARE_POINT /MOUNT_POINT
        

Replace the following:

    * FILESTORE-INSTANCE-FQDN is the fully-qualified domain name where the Filestore instance is located.
    * INSTANCE_SHARE_POINT is the file share name of the Filestore instance that you want to connect.
    * MOUNT_POINT is the mount point or directory name where you want to mount.



## Linux client configuration

An NFSv4.1 Filestore instance allows clients to perform NFS operations using various security flavors. These flavors are configured by the instance administrator through network ACLs on the Filestore NFSv4.1 instance, during creation or if updated after creation.

The `sys` security flavor uses standard Unix authentication, while `krb5`, `krb5i`, and `krb5p` flavors use Kerberos-based authentication.

The `krb5`, `krb5i`, and `krb5p` flavors require the clients to be connected to the same Managed Microsoft AD domain as the Filestore instance. Complete the following steps appropriate for your environment.

###  Ubuntu image 

  1. SSH to the Compute Engine instance.
  2. Run the following commands to join the Managed Microsoft AD domain.

     1. Run the following setup command:
            
            sudo apt-get update \
            sudo apt-get -y -qq install adcli realmd sssd sssd-tools packagekit krb5-user \ nfs-common expect retry
            

     2. When prompted for realm, replace the existing entry with the Managed Microsoft AD domain used on the Filestore instance. Enter the value in uppercase, then press the arrow key to select _OK_ , then press _Enter_.

     3. When prompted for hosts, leave it empty and proceed.

     4. Complete either of the following steps:

        * For VMs with a hostname length that is less than or equal to 15 characters, run the following command:
              
              sudo realm join -vU JOIN_DOMAIN_USER --automatic-id-mapping=no MANAGED_AD_DOMAIN_NAME
              

Replace the following:

          * JOIN_DOMAIN_USER is the name of the user account used to join the domain.
          * MANAGED_AD_DOMAIN_NAME is the domain name of the Managed Microsoft AD service you want to use.
        * For VMs with a hostname length that is greater than 15 characters, run the following command:
              
              sudo realm join -vU JOIN_DOMAIN_USER --automatic-id-mapping=no \ --user-principal=host/`hostname -f`@MANAGED_AD_REALM_NAME MANAGED_AD_DOMAIN_NAME
              

Replace the following:

          * JOIN_DOMAIN_USER is the name of the user account used to join the domain.
          * MANAGED_AD_REALM_NAME is the realm name of the Managed Microsoft AD service you want to use.
          * MANAGED_AD_DOMAIN_NAME is the domain name of the Managed Microsoft AD service you want to use.
  3. Update Kerberos configuration. Update `/etc/krb5.conf` with the required realm definition and realm-domain mapping:
         
         [realms]
                   DOMAIN_NAME = {
                            kdc = DOMAIN_NAME
                            default_domain = DOMAIN_NAME
                   }
          [domain_realm]
                   .domain_name_lowercase = DOMAIN_NAME
                   domain_name_lowercase = DOMAIN_NAME
         

Replace the following:

     * DOMAIN_NAME is the domain name you want to use, entered in uppercase.
     * domain_name_lowercase is the domain name you want to use, entered in lowercase.

Refer to the following for an example:
    
    [realms]
           FILE.DEMO.LOCAL = {
                    kdc = FILE.DEMO.LOCAL
                    default_domain = FILE.DEMO.LOCAL
           }
    
    [domain_realm]
           .file.demo.local = FILE.DEMO.LOCAL
           file.demo.local = FILE.DEMO.LOCAL
    

  4. Run the rpc-gssd service. Add the following `No-Strip` attribute value to `[General]` section inside `/etc/idmapd.conf`:
         
         [General]
          No-Strip = both
         

  5. Run the following command:
         
         sudo systemctl restart rpc-gssd
         




###  Centos image 

  1. Ssh to the Compute Engine instance.
  2. Join the Managed Microsoft AD domain:
         
         sudo yum update \
         sudo yum install -y adcli realmd sssd samba-common-tools krb5-workstation nfs-utils \ bind-utils openldap-clients
         

  3. Complete either of the following steps:

     * For VMs with a hostname length less than or equal to 15 characters, run the following command:
           
           sudo realm join -vU JOIN_DOMAIN_USER --automatic-id-mapping=no MANAGED_AD_DOMAIN_NAME
           

Replace the following:

       * JOIN_DOMAIN_USER is the name of the user account used to join the domain.
       * MANAGED_AD_DOMAIN_NAME is the domain name of the Managed Microsoft AD service you want to use.
     * For VMs with a hostname length greater than 15 characters, run the following command:
           
           sudo realm join -vU JOIN_DOMAIN_USER --automatic-id-mapping=no \ --user-principal=host/`hostname -f`@MANAGED_AD_REALM_NAME MANAGED_AD_DOMAIN_NAME
           

Replace the following:

       * JOIN_DOMAIN_USER is the name of the user account used to join the domain.
       * MANAGED_AD_REALM_NAME is the realm name of the Managed Microsoft AD service you want to use.
       * MANAGED_AD_DOMAIN_NAME is the domain name of the Managed Microsoft AD service you want to use.
  4. Ensure that sssd service is running:
         
         sudo systemctl status sssd
         

  5. Run rpc-gssd service. Add the following below the `No-Strip` attribute value to the `[General]` section inside `/etc/idmapd.conf`:
         
         [General]
         No-Strip = both
         

  6. Run the following command. This command helps ensure the NFS client won't strip the domain name from the NFS server hostname. For more information, see [NFS Ganesha List Archives](https://lists.nfs-ganesha.org/archives/list/devel@lists.nfs-ganesha.org/thread/AGEYVZCF2Z7QFAPXRWAB2J4DBBUWJNDZ/) and [Arch Linux Archive](https://man.archlinux.org/man/idmapd.conf.5.en):
         
         sudo systemctl start rpc-gssd
         




## What's next

  * [Edit a Filestore instance](https://docs.cloud.google.com/filestore/docs/editing-instances)
  * [Create an instance on a Shared VPC network in service projects](https://docs.cloud.google.com/filestore/docs/shared-vpc)
  * [Create a Filestore instance with Private Service Connect](https://docs.cloud.google.com/filestore/docs/configure-psc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
