---
url: https://docs.cloud.google.com/bare-metal/docs/troubleshooting/troubleshoot-access-issues/
title: Troubleshoot access issues \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:02.149902+00:00
---

# Troubleshoot access issues  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/troubleshooting/troubleshoot-access-issues/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot access issues

This page provides troubleshooting tips for Bare Metal Solution access issues.

Check if your question or problem has already been addressed on the [Known issues and limitations](https://docs.cloud.google.com/bare-metal/docs/known-issues) page.

## SSH client unable to connect

If your SSH client fails to connect to a server, you might see one of the following errors:

  * `connection timeout` or `connection refused`: The SSH client can't connect.

  * `Permission denied (publickey)`: The SSH client fails to authenticate.




To diagnose failed SSH connections, follow these steps:

  1. Test connectivity.

Ensure that the host is reachable and that the SSH port (22) is open using `ping`, `traceroute`, and `nc` commands.
         
         ping SERVER_NAME
         
         
         traceroute SERVER_NAME
         
         
         echo "" | nc SERVER_NAME 22
         

If this does not work, then the issue might be in the networking layer and not with the SSH.

  2. Examine the client side debug output.

     1. Turn on the verbosity of the SSH protocol.
            
            ssh -v SERVER_NAME -i ~/.ssh/id_ecdsa
            

The command prints the debug output that shows the key events of the client side SSH protocol.

The following example output shows that the client sent its key, but the server rejected it. The server asked the authentication to continue with another public key, but the client has no additional keys to offer.
            
            .. .. ..
            debug1: Server host key: ecdsa-sha2-nistp256 SHA256:V9cRYdqcAJv+RPfN+oofNTVdUxs6VlocP4uMWOxeGKI
            debug1: Host 'bms-server' is known and matches the ECDSA host key.
            debug1: Found key in /root/.ssh/known_hosts:1
            debug1: rekey after 134217728 blocks
            debug1: SSH2_MSG_NEWKEYS sent
            debug1: expecting SSH2_MSG_NEWKEYS
            debug1: SSH2_MSG_NEWKEYS received
            debug1: rekey after 134217728 blocks
            debug1: SSH2_MSG_EXT_INFO received
            debug1: kex_input_ext_info: server-sig-algs=
            debug1: SSH2_MSG_SERVICE_ACCEPT received
            debug1: Authentications that can continue: publickey
            debug1: Next authentication method: publickey
            debug1: Offering ECDSA public key: /root/.ssh/id_ecdsa
            debug1: Authentications that can continue: publickey
            debug1: No more authentication methods to try.
            Permission denied (publickey).
            

     2. If the SSH verbose output does not clearly indicate the cause of the error message, run the `strace` command:
            
            strace ssh SERVER_NAME -i ~/.ssh/id_ecdsa > strace-ssh.txt 2>&1
            

     3. Examine the `strace` output for errors related to the core problem.

In some cases, the client side debug output is not enough to identify the problem. You might also need to run server side tracing to find the error. Until you can't SSH into your server, use the [interactive serial console](https://docs.cloud.google.com/bare-metal/docs/troubleshooting/configure-serial-console) to perform the next steps.

  3. Examine the server side debug output.

     1. Find the current SSH settings.
            
            grep -v "^#" /etc/ssh/sshd_config | grep -v "^$"
            

     2. To obtain detailed information about SSH, set the following parameters in `/etc/ssh/sshd_config` file to obtain detailed information.
            
            SyslogFacility AUTH
            LogLevel DEBUG
            

     3. To apply the changes, restart the service.
            
            service sshd restart
            

     4. At the client side, run the `ssh` command and extract the `sshd` messages from the logs:
            
            grep sshd /var/log/messages
            

Or, you can export all relevant messages for the time period using the following command:
            
            journalctl -u sshd -S "START_TIME" -U "END_TIME" --utc
            

Replace the following:

        * `START_TIME`: The start time of the time period in format `yyyy-mm-dd hh:mm:ss`.
        * `END_TIME`: The end time of the time period in format `yyyy-mm-dd hh:mm:ss`.

Example:
    
    journalctl -u sshd -S "2023-04-25 18:38:00" -U "2023-04-25 18:40:00" --utc
    




To fix these issues, consider the following steps:

  * Verify if the client key file is set with read-only permissions (flag `400`). Otherwise, the SSH client does not accept it.

To set the read-only flag for the private key that's in use, run the following command:
        
        chmod 400 ~/.ssh/id_ed25519
        

  * At the server side, check if the client public key is specified in the corresponding user's local configuration file (`~/.ssh/authorized_keys`).

  * In some cases, the problem might be related to the SSH protocol version or the SSH algorithm. The server side and the client side debug outputs might indicate such a problem. Typically, the `man` pages for `ssh` and `sshd_config` provide the details for maintaining the necessary configuration. For example, to find the key exchange algorithms or ciphers that are supported, use the following commands:
        
        # Find key exchange algorithms
        ssh -Q kex
        # Find the symmetric encryption ciphers
        ssh -Q cipher
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
