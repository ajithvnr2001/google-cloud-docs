---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/cis-ubuntu-benchmark/
title: CIS Ubuntu Benchmark \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:41.650023+00:00
---

# CIS Ubuntu Benchmark  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/cis-ubuntu-benchmark/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  CIS Ubuntu Benchmark Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the level of compliance that Google Distributed Cloud has with the CIS Ubuntu Benchmark.

## Access the benchmark

The CIS Ubuntu Benchmark is available on the [CIS website](https://www.cisecurity.org/benchmark/ubuntu_linux/).

## Configuration profile

In the CIS Ubuntu Benchmark document, you can read about configuration profiles. The Ubuntu images used by Google Distributed Cloud are hardened to meet the Level 2 - Server profile.

## Evaluation on Google Distributed Cloud

We use the following values to specify the status of Ubuntu recommendations in Google Distributed Cloud.

Status | Description  
---|---  
pass | Complies with a benchmark recommendation.  
fail | Deviates from a benchmark recommendation.  
notapplicable | Isn't relevant to be tested on the system being evaluated.  
  
## Status of Google Distributed Cloud

The Ubuntu images used with Google Distributed Cloud are hardened to meet the CIS Level 2 - Server profile. The following table gives justifications for why Google Distributed Cloud components did not pass certain recommendations. Benchmarks that have a `Passed` status are not included in the following table.

### 1.33 and 1.32

### Versions

This section refers to these versions:

Google Distributed Cloud version | Ubuntu version | CIS Ubuntu Benchmark version | CIS level   
---|---|---|---  
1.32 | 22.04 LTS | v1.0.0 | Level 2 Server  
  
### Failed recommendations

The following table lists the recommendations for which Google Distributed Cloud deviates from the benchmark's recommendations. These findings apply to cluster nodes and the admin workstation.

# | Recommendation | Severity | Status  
---|---|---|---  
1.1.2.1 | Ensure /tmp Located On Separate Partition | low | fail  
1.1.3.1 | Ensure /var Located On Separate Partition | low | fail  
1.1.4.1 | Ensure /var/tmp Located On Separate Partition | medium | fail  
1.1.5.1 | Ensure /var/log Located On Separate Partition | low | fail  
1.1.6.1 | Ensure /var/log/audit Located On Separate Partition | low | fail  
1.1.7.1 | Ensure /home Located On Separate Partition | low | fail  
1.4.1 | Set Boot Loader Password in grub2 | high | fail  
1.4.3 | Ensure Authentication Required for Single User Mode | medium | fail  
2.3.6 | Uninstall rpcbind Package | low | fail  
3.2.2 | Disable Kernel Parameter for IP Forwarding on IPv4 Interfaces | medium | fail  
3.3.7 | Enable Kernel Parameter to Use Reverse Path Filtering on all IPv4 Interfaces by Default | medium | fail  
3.3.7 | Enable Kernel Parameter to Use Reverse Path Filtering on all IPv4 Interfaces | medium | fail  
3.5.2.8 | Ensure nftables default deny firewall policy | medium | fail  
3.5.2.10 | Ensure nftables rules are permanent | medium | fail  
4.2.3 | Verify permissions of log files | medium | fail  
5.2.4 | Limit Users' SSH Access | unknown | fail  
5.3.4 | Ensure Users Re-Authenticate for Privilege Escalation - sudo | medium | fail  
5.5.1.2 | Set Password Maximum Age | medium | fail  
  
### Passed recommendations

The following table lists the recommendations for which Google Distributed Cloud complies with the benchmark's recommendations.

# | Recommendation | Severity | Status  
---|---|---|---  
1.1.1.1 | Disable Mounting of cramfs | low | pass  
1.1.1.2 | Disable Mounting of squashfs | low | pass  
1.1.1.3 | Disable Mounting of udf | low | pass  
1.1.8.1 | Add nodev Option to /dev/shm | medium | pass  
1.1.8.2 | Add noexec Option to /dev/shm | medium | pass  
1.1.8.3 | Add nosuid Option to /dev/shm | medium | pass  
1.1.9 | Disable the Automounter | medium | pass  
1.1.10 | Disable Modprobe Loading of USB Storage Driver | medium | pass  
1.4.2 | Verify /boot/grub/grub.cfg Permissions | medium | pass  
1.5.1 | Enable Randomized Layout of Virtual Address Space | medium | pass  
1.5.2 | Package "prelink" Must not be Installed | medium | pass  
1.5.3 | Disable Apport Service | unknown | pass  
1.5.4 | Disable Core Dumps for All Users | medium | pass  
1.5.4 | Disable Core Dumps for SUID programs | medium | pass  
1.6.1.1 | Ensure AppArmor is installed | medium | pass  
1.6.1.2 | Ensure AppArmor is enabled in the bootloader configuration | medium | pass  
1.6.1.4 | Enforce all AppArmor Profiles | medium | pass  
1.7.1 | Modify the System Message of the Day Banner | medium | pass  
1.7.2 | Modify the System Login Banner | medium | pass  
1.7.3 | Modify the System Login Banner for Remote Connections | medium | pass  
1.7.4 | Verify Group Ownership of Message of the Day Banner | medium | pass  
1.7.4 | Verify ownership of Message of the Day Banner | medium | pass  
1.7.4 | Verify permissions on Message of the Day Banner | medium | pass  
1.7.5 | Verify Group Ownership of System Login Banner | medium | pass  
1.7.5 | Verify ownership of System Login Banner | medium | pass  
1.7.5 | Verify permissions on System Login Banner | medium | pass  
1.7.6 | Verify Group Ownership of System Login Banner for Remote Connections | medium | pass  
1.7.6 | Verify ownership of System Login Banner for Remote Connections | medium | pass  
1.7.6 | Verify permissions on System Login Banner for Remote Connections | medium | pass  
2.1.1.1 | Install the systemd_timesyncd Service | high | pass  
2.1.3.2 | Enable systemd_timesyncd Service | high | pass  
2.2.1 | Remove the X Windows Package Group | medium | pass  
2.2.2 | Disable Avahi Server Software | medium | pass  
2.2.2 | Uninstall avahi Server Package | medium | pass  
2.2.3 | Disable the CUPS Service | unknown | pass  
2.2.3 | Uninstall CUPS Package | unknown | pass  
2.2.4 | Uninstall DHCP Server Package | medium | pass  
2.2.5 | Uninstall openldap-servers Package | low | pass  
2.2.6 | Uninstall nfs-kernel-server Package | low | pass  
2.2.7 | Uninstall bind Package | low | pass  
2.2.8 | Uninstall vsftpd Package | high | pass  
2.2.9 | Uninstall httpd Package | unknown | pass  
2.2.9 | Uninstall nginx Package | unknown | pass  
2.2.10 | Uninstall cyrus-imapd Package | unknown | pass  
2.2.10 | Uninstall dovecot Package | unknown | pass  
2.2.11 | Uninstall Samba Package | unknown | pass  
2.2.12 | Uninstall squid Package | unknown | pass  
2.2.13 | Uninstall net-snmp Package | unknown | pass  
2.2.14 | Uninstall the nis package | low | pass  
2.2.15 | Ensure Mail Transfer Agent is not Listening on any non-loopback Address | medium | pass  
2.2.16 | Uninstall rsync Package | medium | pass  
2.3.2 | Uninstall rsh Package | unknown | pass  
2.3.3 | Uninstall talk Package | medium | pass  
2.3.4 | Remove telnet Clients | low | pass  
2.3.5 | Ensure LDAP client is not installed | low | pass  
3.1.2 | Deactivate Wireless Network Interfaces | medium | pass  
3.2.1 | Disable Kernel Parameter for Sending ICMP Redirects on all IPv4 Interfaces by Default | medium | pass  
3.2.1 | Disable Kernel Parameter for Sending ICMP Redirects on all IPv4 Interfaces | medium | pass  
3.2.2 | Disable Kernel Parameter for IPv6 Forwarding | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on all IPv4 Interfaces | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on all IPv6 Interfaces | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on IPv4 Interfaces by Default | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on IPv6 Interfaces by Default | medium | pass  
3.3.2 | Disable Accepting ICMP Redirects for All IPv4 Interfaces | medium | pass  
3.3.2 | Disable Accepting ICMP Redirects for All IPv6 Interfaces | medium | pass  
3.3.2 | Disable Kernel Parameter for Accepting ICMP Redirects by Default on IPv4 Interfaces | medium | pass  
3.3.2 | Disable Kernel Parameter for Accepting ICMP Redirects by Default on IPv6 Interfaces | medium | pass  
3.3.3 | Configure Kernel Parameter for Accepting Secure Redirects By Default | medium | pass  
3.3.3 | Disable Kernel Parameter for Accepting Secure ICMP Redirects on all IPv4 Interfaces | medium | pass  
3.3.4 | Enable Kernel Parameter to Log Martian Packets on all IPv4 Interfaces | unknown | pass  
3.3.4 | Enable Kernel Parameter to Log Martian Packets on all IPv4 Interfaces by Default | unknown | pass  
3.3.5 | Enable Kernel Parameter to Ignore ICMP Broadcast Echo Requests on IPv4 Interfaces | medium | pass  
3.3.6 | Enable Kernel Parameter to Ignore Bogus ICMP Error Responses on IPv4 Interfaces | unknown | pass  
3.3.8 | Enable Kernel Parameter to Use TCP Syncookies on Network Interfaces | medium | pass  
3.3.9 | Configure Accepting Router Advertisements on All IPv6 Interfaces | medium | pass  
3.3.9 | Disable Accepting Router Advertisements on all IPv6 Interfaces by Default | medium | pass  
3.4.1 | Disable DCCP Support | medium | pass  
3.4.2 | Disable SCTP Support | medium | pass  
3.4.3 | Disable RDS Support | low | pass  
3.4.4 | Disable TIPC Support | low | pass  
3.5.1.2 | Remove iptables-persistent Package | medium | pass  
3.5.2.1 | Install nftables Package | medium | pass  
3.5.2.4 | Ensure a Table Exists for Nftables | medium | pass  
3.5.2.5 | Ensure Base Chains Exist for Nftables | medium | pass  
3.5.2.9 | Verify nftables Service is Enabled | medium | pass  
3.5.3.1.1 | Install iptables Package | medium | pass  
3.5.3.1.3 | Remove ufw Package | medium | pass  
4.1.1.1 | Ensure the audit Subsystem is Installed | medium | pass  
4.1.1.2 | Enable auditd Service | medium | pass  
4.1.1.4 | Extend Audit Backlog Limit for the Audit Daemon | low | pass  
4.1.2.1 | Configure auditd Max Log File Size | medium | pass  
4.1.2.2 | Configure auditd max_log_file_action Upon Reaching Maximum Log Size | medium | pass  
4.1.2.3 | Configure auditd admin_space_left Action on Low Disk Space | medium | pass  
4.1.2.3 | Configure auditd mail_acct Action on Low Disk Space | medium | pass  
4.1.2.3 | Configure auditd space_left Action on Low Disk Space | medium | pass  
4.1.3.1 | Ensure auditd Collects System Administrator Actions | medium | pass  
4.1.3.2 | Record Events When Privileged Executables Are Run | medium | pass  
4.1.3.3 | Record Attempts to perform maintenance activities | medium | pass  
4.1.3.4 | Record Attempts to Alter the localtime File | medium | pass  
4.1.3.4 | Record attempts to alter time through adjtimex | medium | pass  
4.1.3.4 | Record Attempts to Alter Time Through clock_settime | medium | pass  
4.1.3.4 | Record attempts to alter time through settimeofday | medium | pass  
4.1.3.4 | Record Attempts to Alter Time Through stime | medium | pass  
4.1.3.5 | Record Events that Modify the System's Network Environment | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - su | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - sudo | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - sudoedit | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - umount | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - unix_chkpwd | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - creat | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - ftruncate | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - open | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - openat | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - truncate | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/group | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/gshadow | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/passwd | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/security/opasswd | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/shadow | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - chmod | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - chown | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchmod | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchmodat | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchown | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchownat | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fremovexattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fsetxattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - lchown | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - lremovexattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - lsetxattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - removexattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - setxattr | medium | pass  
4.1.3.10 | Ensure auditd Collects Information on Exporting to Media (successful) | medium | pass  
4.1.3.11 | Record Attempts to Alter Process and Session Initiation Information | medium | pass  
4.1.3.12 | Record Attempts to Alter Logon and Logout Events - faillog | medium | pass  
4.1.3.12 | Record Attempts to Alter Logon and Logout Events - lastlog | medium | pass  
4.1.3.12 | Record Attempts to Alter Logon and Logout Events - tallylog | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - rename | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - renameat | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - unlink | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - unlinkat | medium | pass  
4.1.3.14 | Record Events that Modify the System's Mandatory Access Controls | medium | pass  
4.1.3.15 | Record Any Attempts to Run chcon | medium | pass  
4.1.3.16 | Record Any Attempts to Run setfacl | medium | pass  
4.1.3.17 | Record Any Attempts to Run chacl | medium | pass  
4.1.3.18 | Ensure auditd Collects Information on the Use of Privileged Commands - usermod | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on Kernel Module Loading - init_module | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on Kernel Module Unloading - delete_module | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on the Use of Privileged Commands - insmod | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on the Use of Privileged Commands - modprobe | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on the Use of Privileged Commands - rmmod | medium | pass  
4.1.3.20 | Make the auditd Configuration Immutable | medium | pass  
4.1.4.1 | System Audit Logs Must Have Mode 0640 or Less Permissive | medium | pass  
4.1.4.2 | System Audit Logs Must Be Owned By Root | medium | pass  
4.1.4.3 | System Audit Logs Must Be Group Owned By Root | medium | pass  
4.1.4.4 | System Audit Logs Must Have Mode 0750 or Less Permissive | medium | pass  
4.1.4.5 | Verify Permissions on /etc/audit/auditd.conf | medium | pass  
4.1.4.5 | Verify Permissions on /etc/audit/rules.d/*.rules | medium | pass  
4.1.4.6 | Audit Configuration Files Must Be Owned By Root | medium | pass  
4.1.4.7 | Audit Configuration Files Must Be Owned By Group root | medium | pass  
4.1.4.8 | Verify that audit tools Have Mode 0755 or less | medium | pass  
4.1.4.9 | Verify that audit tools are owned by root | medium | pass  
4.1.4.10 | Verify that audit tools are owned by group root | medium | pass  
4.2.1.1.1 | Install systemd-journal-remote Package | medium | pass  
4.2.1.1.4 | Disable systemd-journal-remote Socket | medium | pass  
4.2.1.2 | Enable systemd-journald Service | medium | pass  
4.2.1.3 | Ensure journald is configured to compress large log files | medium | pass  
4.2.1.4 | Ensure journald is configured to write log files to persistent disk | medium | pass  
4.2.2.1 | Ensure rsyslog is Installed | medium | pass  
4.2.2.2 | Enable rsyslog Service | medium | pass  
4.2.2.4 | Ensure rsyslog Default File Permissions Configured | medium | pass  
4.2.2.7 | Ensure rsyslog Does Not Accept Remote Messages Unless Acting As Log Server | medium | pass  
5.1.1 | Enable cron Service | medium | pass  
5.1.2 | Verify Group Who Owns Crontab | medium | pass  
5.1.2 | Verify Owner on crontab | medium | pass  
5.1.2 | Verify Permissions on crontab | medium | pass  
5.1.3 | Verify Group Who Owns cron.hourly | medium | pass  
5.1.3 | Verify Owner on cron.hourly | medium | pass  
5.1.3 | Verify Permissions on cron.hourly | medium | pass  
5.1.4 | Verify Group Who Owns cron.daily | medium | pass  
5.1.4 | Verify Owner on cron.daily | medium | pass  
5.1.4 | Verify Permissions on cron.daily | medium | pass  
5.1.5 | Verify Group Who Owns cron.weekly | medium | pass  
5.1.5 | Verify Owner on cron.weekly | medium | pass  
5.1.5 | Verify Permissions on cron.weekly | medium | pass  
5.1.6 | Verify Group Who Owns cron.monthly | medium | pass  
5.1.6 | Verify Owner on cron.monthly | medium | pass  
5.1.6 | Verify Permissions on cron.monthly | medium | pass  
5.1.7 | Verify Group Who Owns cron.d | medium | pass  
5.1.7 | Verify Owner on cron.d | medium | pass  
5.1.7 | Verify Permissions on cron.d | medium | pass  
5.1.8 | Ensure that /etc/cron.deny does not exist | medium | pass  
5.1.8 | Verify Group Who Owns /etc/cron.allow file | medium | pass  
5.1.8 | Verify Permissions on /etc/cron.allow file | medium | pass  
5.1.8 | Verify User Who Owns /etc/cron.allow file | medium | pass  
5.1.9 | Ensure that /etc/at.deny does not exist | medium | pass  
5.1.9 | Verify Group Who Owns /etc/at.allow file | medium | pass  
5.1.9 | Verify Permissions on /etc/at.allow file | medium | pass  
5.1.9 | Verify User Who Owns /etc/at.allow file | medium | pass  
5.2.1 | Verify Group Who Owns SSH Server config file | medium | pass  
5.2.1 | Verify Owner on SSH Server config file | medium | pass  
5.2.1 | Verify Permissions on SSH Server config file | medium | pass  
5.2.2 | Verify Permissions on SSH Server Private *_key Key Files | medium | pass  
5.2.3 | Verify Permissions on SSH Server Public *.pub Key Files | medium | pass  
5.2.5 | Set LogLevel to INFO | low | pass  
5.2.6 | Enable PAM | medium | pass  
5.2.7 | Disable SSH Root Login | medium | pass  
5.2.8 | Disable Host-Based Authentication | medium | pass  
5.2.9 | Disable SSH Access via Empty Passwords | high | pass  
5.2.10 | Do Not Allow SSH Environment Options | medium | pass  
5.2.11 | Disable SSH Support for .rhosts Files | medium | pass  
5.2.12 | Disable X11 Forwarding | medium | pass  
5.2.13 | Use Only Strong Ciphers | medium | pass  
5.2.14 | Use Only Strong MACs | medium | pass  
5.2.15 | Use Only Strong Key Exchange algorithms | medium | pass  
5.2.16 | Disable SSH TCP Forwarding | medium | pass  
5.2.17 | Enable SSH Warning Banner | medium | pass  
5.2.18 | Set SSH authentication attempt limit | medium | pass  
5.2.19 | Ensure SSH MaxStartups is configured | medium | pass  
5.2.20 | Set SSH MaxSessions limit | medium | pass  
5.2.21 | Ensure SSH LoginGraceTime is configured | medium | pass  
5.2.22 | Set SSH Client Alive Count Max | medium | pass  
5.2.22 | Set SSH Client Alive Interval | medium | pass  
5.3.1 | Install sudo Package | medium | pass  
5.3.2 | Ensure Only Users Logged In To Real tty Can Execute Sudo - sudo use_pty | medium | pass  
5.3.3 | Ensure Sudo Logfile Exists - sudo logfile | low | pass  
5.3.5 | Ensure Users Re-Authenticate for Privilege Escalation - sudo !authenticate | medium | pass  
5.3.6 | Require Re-Authentication When Using the sudo Command | medium | pass  
5.3.7 | Enforce Usage of pam_wheel with Group Parameter for su Authentication | medium | pass  
5.3.7 | Ensure the Group Used by pam_wheel Module Exists on System and is Empty | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Authentication Retry Prompts Permitted Per-Session | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Different Categories | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Digit Characters | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Length | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Lowercase Characters | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Special Characters | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Uppercase Characters | medium | pass  
5.4.1 | Install pam_pwquality Package | medium | pass  
5.4.2 | Lock Accounts After Failed Password Attempts | medium | pass  
5.4.2 | Set Interval For Counting Failed Password Attempts | medium | pass  
5.4.2 | Set Lockout Time for Failed Password Attempts | medium | pass  
5.4.3 | Limit Password Reuse | medium | pass  
5.4.4 | Set Password Hashing Algorithm in /etc/login.defs | medium | pass  
5.5.1.1 | Set Existing Passwords Minimum Age | medium | pass  
5.5.1.1 | Set Password Minimum Age | medium | pass  
5.5.1.2 | Set Existing Passwords Maximum Age | medium | pass  
5.5.1.3 | Set Password Warning Age | medium | pass  
5.5.1.4 | Set Account Expiration Following Inactivity | medium | pass  
5.5.1.5 | Ensure all users last password change date is in the past | medium | pass  
5.5.2 | Ensure that System Accounts Do Not Run a Shell Upon Login | medium | pass  
5.5.3 | Verify Root Has A Primary GID 0 | high | pass  
5.5.4 | Ensure the Default Bash Umask is Set Correctly | medium | pass  
5.5.4 | Ensure the Default Umask is Set Correctly For Interactive Users | medium | pass  
5.5.4 | Ensure the Default Umask is Set Correctly in /etc/profile | medium | pass  
5.5.4 | Ensure the Default Umask is Set Correctly in login.defs | medium | pass  
5.5.5 | Set Interactive Session Timeout | medium | pass  
6.1.1 | Verify Group Who Owns passwd File | medium | pass  
6.1.1 | Verify Permissions on passwd File | medium | pass  
6.1.1 | Verify User Who Owns passwd File | medium | pass  
6.1.2 | Verify Group Who Owns Backup passwd File | medium | pass  
6.1.2 | Verify Permissions on Backup passwd File | medium | pass  
6.1.2 | Verify User Who Owns Backup passwd File | medium | pass  
6.1.3 | Verify Group Who Owns group File | medium | pass  
6.1.3 | Verify Permissions on group File | medium | pass  
6.1.3 | Verify User Who Owns group File | medium | pass  
6.1.4 | Verify Group Who Owns Backup group File | medium | pass  
6.1.4 | Verify Permissions on Backup group File | medium | pass  
6.1.4 | Verify User Who Owns Backup group File | medium | pass  
6.1.5 | Verify Group Who Owns shadow File | medium | pass  
6.1.5 | Verify Permissions on shadow File | medium | pass  
6.1.5 | Verify User Who Owns shadow File | medium | pass  
6.1.6 | Verify Group Who Owns Backup shadow File | medium | pass  
6.1.6 | Verify Permissions on Backup shadow File | medium | pass  
6.1.6 | Verify User Who Owns Backup shadow File | medium | pass  
6.1.7 | Verify Group Who Owns gshadow File | medium | pass  
6.1.7 | Verify Permissions on gshadow File | medium | pass  
6.1.7 | Verify User Who Owns gshadow File | medium | pass  
6.1.8 | Verify Group Who Owns Backup gshadow File | medium | pass  
6.1.8 | Verify Permissions on Backup gshadow File | medium | pass  
6.1.8 | Verify User Who Owns Backup gshadow File | medium | pass  
6.1.10 | Ensure All Files Are Owned by a User | medium | pass  
6.2.1 | Verify All Account Password Hashes are Shadowed | medium | pass  
6.2.2 | Ensure There Are No Accounts With Blank or Null Passwords | high | pass  
6.2.3 | All GIDs referenced in /etc/passwd must be defined in /etc/group | low | pass  
6.2.4 | Ensure shadow group is empty | medium | pass  
6.2.5 | Ensure All Accounts on the System Have Unique User IDs | medium | pass  
6.2.6 | Ensure All Groups on the System Have Unique Group ID | medium | pass  
6.2.7 | Ensure All Accounts on the System Have Unique Names | medium | pass  
6.2.8 | Ensure All Groups on the System Have Unique Group Names | medium | pass  
6.2.9 | Ensure that Root's Path Does Not Include Relative Paths or Null Directories | unknown | pass  
6.2.9 | Ensure that Root's Path Does Not Include World or Group-Writable Directories | medium | pass  
6.2.10 | Verify Only Root Has UID 0 | high | pass  
6.2.11 | All Interactive Users Home Directories Must Exist | medium | pass  
6.2.12 | All Interactive User Home Directories Must Be Group-Owned By The Primary Group | medium | pass  
6.2.12 | All Interactive User Home Directories Must Be Owned By The Primary User | medium | pass  
6.2.13 | All Interactive User Home Directories Must Have mode 0750 Or Less Permissive | medium | pass  
6.2.14 | Verify No netrc Files Exist | medium | pass  
6.2.15 | Verify No .forward Files Exist | medium | pass  
6.2.16 | Remove Rsh Trust Files | high | pass  
6.2.17 | User Initialization Files Must Be Group-Owned By The Primary Group | medium | pass  
6.2.17 | User Initialization Files Must Be Owned By the Primary User | medium | pass  
6.2.17 | User Initialization Files Must Not Run World-Writable Programs | medium | pass  
  
### Not applicable recommendations

The following table lists the recommendations that don't apply for Google Distributed Cloud.

# | Recommendation | Severity | Status  
---|---|---|---  
1.1.2.2 | Add nodev Option to /tmp | medium | notapplicable  
1.1.2.3 | Add noexec Option to /tmp | medium | notapplicable  
1.1.2.4 | Add nosuid Option to /tmp | medium | notapplicable  
1.1.3.2 | Add nodev Option to /var | medium | notapplicable  
1.1.3.3 | Add nosuid Option to /var | medium | notapplicable  
1.1.4.2 | Add noexec Option to /var/tmp | medium | notapplicable  
1.1.4.3 | Add nosuid Option to /var/tmp | medium | notapplicable  
1.1.4.4 | Add nodev Option to /var/tmp | medium | notapplicable  
1.1.5.2 | Add nodev Option to /var/log | medium | notapplicable  
1.1.5.3 | Add noexec Option to /var/log | medium | notapplicable  
1.1.5.4 | Add nosuid Option to /var/log | medium | notapplicable  
1.1.6.2 | Add noexec Option to /var/log/audit | medium | notapplicable  
1.1.6.3 | Add nodev Option to /var/log/audit | medium | notapplicable  
1.1.6.4 | Add nosuid Option to /var/log/audit | medium | notapplicable  
1.1.7.2 | Add nodev Option to /home | unknown | notapplicable  
1.1.7.3 | Add nosuid Option to /home | medium | notapplicable  
1.10 | Configure GNOME3 DConf User Profile | high | notapplicable  
1.4.1 | Set the UEFI Boot Loader Password | high | notapplicable  
1.8.1 | Remove the GDM Package Group | medium | notapplicable  
1.8.10 | Disable XDMCP in GDM | high | notapplicable  
1.8.4 | Enable GNOME3 Screensaver Lock After Idle Period | medium | notapplicable  
1.8.5 | Set GNOME3 Screensaver Lock Delay After Activation Period | medium | notapplicable  
1.8.6 | Disable GNOME3 Automount Opening | medium | notapplicable  
1.8.6 | Disable GNOME3 Automounting | medium | notapplicable  
1.8.8 | Disable GNOME3 Automount running | low | notapplicable  
2.1.4.1 | Configure server restrictions for ntpd | medium | notapplicable  
2.1.4.3 | Configure ntpd To Run As ntp User | medium | notapplicable  
2.1.4.4 | Enable the NTP Daemon | high | notapplicable  
2.2.15 | Disable Postfix Network Listening | medium | notapplicable  
3.5.1.3 | Verify ufw Enabled | medium | notapplicable  
3.5.1.4 | Set UFW Loopback Traffic | medium | notapplicable  
3.5.1.6 | Ensure ufw Firewall Rules Exist for All Open Ports | medium | notapplicable  
3.5.1.7 | Ensure ufw Default Deny Firewall Policy | medium | notapplicable  
3.5.3.2.1 | Set Default iptables Policy for Incoming Packets | medium | notapplicable  
3.5.3.2.2 | Set configuration for loopback traffic | medium | notapplicable  
3.5.3.2.4 | Ensure iptables Firewall Rules Exist for All Open Ports | medium | notapplicable  
3.5.3.3.1 | Set Default ip6tables Policy for Incoming Packets | medium | notapplicable  
3.5.3.3.4 | Ensure ip6tables Firewall Rules Exist for All Open Ports | medium | notapplicable  
  
### 1.31

### Versions

This section refers to these versions:

Google Distributed Cloud version | Ubuntu version | CIS Ubuntu Benchmark version | CIS level   
---|---|---|---  
1.31 | 22.04 LTS | v1.0.0 | Level 2 Server  
  
### Failed recommendations

The following table lists the recommendations for which Google Distributed Cloud deviates from the benchmark's recommendations. These findings apply to cluster nodes and the admin workstation.

# | Recommendation | Severity | Status  
---|---|---|---  
1.1.2.1 | Ensure /tmp Located On Separate Partition | low | fail  
1.1.3.1 | Ensure /var Located On Separate Partition | low | fail  
1.1.4.1 | Ensure /var/tmp Located On Separate Partition | medium | fail  
1.1.5.1 | Ensure /var/log Located On Separate Partition | low | fail  
1.1.6.1 | Ensure /var/log/audit Located On Separate Partition | low | fail  
1.1.7.1 | Ensure /home Located On Separate Partition | low | fail  
1.4.1 | Set Boot Loader Password in grub2 | high | fail  
1.4.3 | Ensure Authentication Required for Single User Mode | medium | fail  
2.3.6 | Uninstall rpcbind Package | low | fail  
3.2.2 | Disable Kernel Parameter for IP Forwarding on IPv4 Interfaces | medium | fail  
3.3.7 | Enable Kernel Parameter to Use Reverse Path Filtering on all IPv4 Interfaces by Default | medium | fail  
3.3.7 | Enable Kernel Parameter to Use Reverse Path Filtering on all IPv4 Interfaces | medium | fail  
3.5.2.8 | Ensure nftables default deny firewall policy | medium | fail  
3.5.2.10 | Ensure nftables rules are permanent | medium | fail  
4.2.3 | Verify permissions of log files | medium | fail  
5.2.4 | Limit Users' SSH Access | unknown | fail  
5.3.4 | Ensure Users Re-Authenticate for Privilege Escalation - sudo | medium | fail  
5.5.1.2 | Set Password Maximum Age | medium | fail  
  
### Passed recommendations

The following table lists the recommendations for which Google Distributed Cloud complies with the benchmark's recommendations.

# | Recommendation | Severity | Status  
---|---|---|---  
1.1.1.1 | Disable Mounting of cramfs | low | pass  
1.1.1.2 | Disable Mounting of squashfs | low | pass  
1.1.1.3 | Disable Mounting of udf | low | pass  
1.1.8.1 | Add nodev Option to /dev/shm | medium | pass  
1.1.8.2 | Add noexec Option to /dev/shm | medium | pass  
1.1.8.3 | Add nosuid Option to /dev/shm | medium | pass  
1.1.9 | Disable the Automounter | medium | pass  
1.1.10 | Disable Modprobe Loading of USB Storage Driver | medium | pass  
1.4.2 | Verify /boot/grub/grub.cfg Permissions | medium | pass  
1.5.1 | Enable Randomized Layout of Virtual Address Space | medium | pass  
1.5.2 | Package "prelink" Must not be Installed | medium | pass  
1.5.3 | Disable Apport Service | unknown | pass  
1.5.4 | Disable Core Dumps for All Users | medium | pass  
1.5.4 | Disable Core Dumps for SUID programs | medium | pass  
1.6.1.1 | Ensure AppArmor is installed | medium | pass  
1.6.1.2 | Ensure AppArmor is enabled in the bootloader configuration | medium | pass  
1.6.1.4 | Enforce all AppArmor Profiles | medium | pass  
1.7.1 | Modify the System Message of the Day Banner | medium | pass  
1.7.2 | Modify the System Login Banner | medium | pass  
1.7.3 | Modify the System Login Banner for Remote Connections | medium | pass  
1.7.4 | Verify Group Ownership of Message of the Day Banner | medium | pass  
1.7.4 | Verify ownership of Message of the Day Banner | medium | pass  
1.7.4 | Verify permissions on Message of the Day Banner | medium | pass  
1.7.5 | Verify Group Ownership of System Login Banner | medium | pass  
1.7.5 | Verify ownership of System Login Banner | medium | pass  
1.7.5 | Verify permissions on System Login Banner | medium | pass  
1.7.6 | Verify Group Ownership of System Login Banner for Remote Connections | medium | pass  
1.7.6 | Verify ownership of System Login Banner for Remote Connections | medium | pass  
1.7.6 | Verify permissions on System Login Banner for Remote Connections | medium | pass  
2.1.1.1 | Install the systemd_timesyncd Service | high | pass  
2.1.3.2 | Enable systemd_timesyncd Service | high | pass  
2.2.1 | Remove the X Windows Package Group | medium | pass  
2.2.2 | Disable Avahi Server Software | medium | pass  
2.2.2 | Uninstall avahi Server Package | medium | pass  
2.2.3 | Disable the CUPS Service | unknown | pass  
2.2.3 | Uninstall CUPS Package | unknown | pass  
2.2.4 | Uninstall DHCP Server Package | medium | pass  
2.2.5 | Uninstall openldap-servers Package | low | pass  
2.2.6 | Uninstall nfs-kernel-server Package | low | pass  
2.2.7 | Uninstall bind Package | low | pass  
2.2.8 | Uninstall vsftpd Package | high | pass  
2.2.9 | Uninstall httpd Package | unknown | pass  
2.2.9 | Uninstall nginx Package | unknown | pass  
2.2.10 | Uninstall cyrus-imapd Package | unknown | pass  
2.2.10 | Uninstall dovecot Package | unknown | pass  
2.2.11 | Uninstall Samba Package | unknown | pass  
2.2.12 | Uninstall squid Package | unknown | pass  
2.2.13 | Uninstall net-snmp Package | unknown | pass  
2.2.14 | Uninstall the nis package | low | pass  
2.2.15 | Ensure Mail Transfer Agent is not Listening on any non-loopback Address | medium | pass  
2.2.16 | Uninstall rsync Package | medium | pass  
2.3.2 | Uninstall rsh Package | unknown | pass  
2.3.3 | Uninstall talk Package | medium | pass  
2.3.4 | Remove telnet Clients | low | pass  
2.3.5 | Ensure LDAP client is not installed | low | pass  
3.1.2 | Deactivate Wireless Network Interfaces | medium | pass  
3.2.1 | Disable Kernel Parameter for Sending ICMP Redirects on all IPv4 Interfaces by Default | medium | pass  
3.2.1 | Disable Kernel Parameter for Sending ICMP Redirects on all IPv4 Interfaces | medium | pass  
3.2.2 | Disable Kernel Parameter for IPv6 Forwarding | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on all IPv4 Interfaces | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on all IPv6 Interfaces | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on IPv4 Interfaces by Default | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on IPv6 Interfaces by Default | medium | pass  
3.3.2 | Disable Accepting ICMP Redirects for All IPv4 Interfaces | medium | pass  
3.3.2 | Disable Accepting ICMP Redirects for All IPv6 Interfaces | medium | pass  
3.3.2 | Disable Kernel Parameter for Accepting ICMP Redirects by Default on IPv4 Interfaces | medium | pass  
3.3.2 | Disable Kernel Parameter for Accepting ICMP Redirects by Default on IPv6 Interfaces | medium | pass  
3.3.3 | Configure Kernel Parameter for Accepting Secure Redirects By Default | medium | pass  
3.3.3 | Disable Kernel Parameter for Accepting Secure ICMP Redirects on all IPv4 Interfaces | medium | pass  
3.3.4 | Enable Kernel Parameter to Log Martian Packets on all IPv4 Interfaces | unknown | pass  
3.3.4 | Enable Kernel Parameter to Log Martian Packets on all IPv4 Interfaces by Default | unknown | pass  
3.3.5 | Enable Kernel Parameter to Ignore ICMP Broadcast Echo Requests on IPv4 Interfaces | medium | pass  
3.3.6 | Enable Kernel Parameter to Ignore Bogus ICMP Error Responses on IPv4 Interfaces | unknown | pass  
3.3.8 | Enable Kernel Parameter to Use TCP Syncookies on Network Interfaces | medium | pass  
3.3.9 | Configure Accepting Router Advertisements on All IPv6 Interfaces | medium | pass  
3.3.9 | Disable Accepting Router Advertisements on all IPv6 Interfaces by Default | medium | pass  
3.4.1 | Disable DCCP Support | medium | pass  
3.4.2 | Disable SCTP Support | medium | pass  
3.4.3 | Disable RDS Support | low | pass  
3.4.4 | Disable TIPC Support | low | pass  
3.5.1.2 | Remove iptables-persistent Package | medium | pass  
3.5.2.1 | Install nftables Package | medium | pass  
3.5.2.4 | Ensure a Table Exists for Nftables | medium | pass  
3.5.2.5 | Ensure Base Chains Exist for Nftables | medium | pass  
3.5.2.9 | Verify nftables Service is Enabled | medium | pass  
3.5.3.1.1 | Install iptables Package | medium | pass  
3.5.3.1.3 | Remove ufw Package | medium | pass  
4.1.1.1 | Ensure the audit Subsystem is Installed | medium | pass  
4.1.1.2 | Enable auditd Service | medium | pass  
4.1.1.4 | Extend Audit Backlog Limit for the Audit Daemon | low | pass  
4.1.2.1 | Configure auditd Max Log File Size | medium | pass  
4.1.2.2 | Configure auditd max_log_file_action Upon Reaching Maximum Log Size | medium | pass  
4.1.2.3 | Configure auditd admin_space_left Action on Low Disk Space | medium | pass  
4.1.2.3 | Configure auditd mail_acct Action on Low Disk Space | medium | pass  
4.1.2.3 | Configure auditd space_left Action on Low Disk Space | medium | pass  
4.1.3.1 | Ensure auditd Collects System Administrator Actions | medium | pass  
4.1.3.2 | Record Events When Privileged Executables Are Run | medium | pass  
4.1.3.3 | Record Attempts to perform maintenance activities | medium | pass  
4.1.3.4 | Record Attempts to Alter the localtime File | medium | pass  
4.1.3.4 | Record attempts to alter time through adjtimex | medium | pass  
4.1.3.4 | Record Attempts to Alter Time Through clock_settime | medium | pass  
4.1.3.4 | Record attempts to alter time through settimeofday | medium | pass  
4.1.3.4 | Record Attempts to Alter Time Through stime | medium | pass  
4.1.3.5 | Record Events that Modify the System's Network Environment | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - su | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - sudo | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - sudoedit | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - umount | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - unix_chkpwd | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - creat | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - ftruncate | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - open | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - openat | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - truncate | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/group | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/gshadow | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/passwd | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/security/opasswd | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/shadow | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - chmod | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - chown | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchmod | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchmodat | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchown | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchownat | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fremovexattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fsetxattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - lchown | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - lremovexattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - lsetxattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - removexattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - setxattr | medium | pass  
4.1.3.10 | Ensure auditd Collects Information on Exporting to Media (successful) | medium | pass  
4.1.3.11 | Record Attempts to Alter Process and Session Initiation Information | medium | pass  
4.1.3.12 | Record Attempts to Alter Logon and Logout Events - faillog | medium | pass  
4.1.3.12 | Record Attempts to Alter Logon and Logout Events - lastlog | medium | pass  
4.1.3.12 | Record Attempts to Alter Logon and Logout Events - tallylog | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - rename | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - renameat | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - unlink | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - unlinkat | medium | pass  
4.1.3.14 | Record Events that Modify the System's Mandatory Access Controls | medium | pass  
4.1.3.15 | Record Any Attempts to Run chcon | medium | pass  
4.1.3.16 | Record Any Attempts to Run setfacl | medium | pass  
4.1.3.17 | Record Any Attempts to Run chacl | medium | pass  
4.1.3.18 | Ensure auditd Collects Information on the Use of Privileged Commands - usermod | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on Kernel Module Loading - init_module | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on Kernel Module Unloading - delete_module | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on the Use of Privileged Commands - insmod | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on the Use of Privileged Commands - modprobe | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on the Use of Privileged Commands - rmmod | medium | pass  
4.1.3.20 | Make the auditd Configuration Immutable | medium | pass  
4.1.4.1 | System Audit Logs Must Have Mode 0640 or Less Permissive | medium | pass  
4.1.4.2 | System Audit Logs Must Be Owned By Root | medium | pass  
4.1.4.3 | System Audit Logs Must Be Group Owned By Root | medium | pass  
4.1.4.4 | System Audit Logs Must Have Mode 0750 or Less Permissive | medium | pass  
4.1.4.5 | Verify Permissions on /etc/audit/auditd.conf | medium | pass  
4.1.4.5 | Verify Permissions on /etc/audit/rules.d/*.rules | medium | pass  
4.1.4.6 | Audit Configuration Files Must Be Owned By Root | medium | pass  
4.1.4.7 | Audit Configuration Files Must Be Owned By Group root | medium | pass  
4.1.4.8 | Verify that audit tools Have Mode 0755 or less | medium | pass  
4.1.4.9 | Verify that audit tools are owned by root | medium | pass  
4.1.4.10 | Verify that audit tools are owned by group root | medium | pass  
4.2.1.1.1 | Install systemd-journal-remote Package | medium | pass  
4.2.1.1.4 | Disable systemd-journal-remote Socket | medium | pass  
4.2.1.2 | Enable systemd-journald Service | medium | pass  
4.2.1.3 | Ensure journald is configured to compress large log files | medium | pass  
4.2.1.4 | Ensure journald is configured to write log files to persistent disk | medium | pass  
4.2.2.1 | Ensure rsyslog is Installed | medium | pass  
4.2.2.2 | Enable rsyslog Service | medium | pass  
4.2.2.4 | Ensure rsyslog Default File Permissions Configured | medium | pass  
4.2.2.7 | Ensure rsyslog Does Not Accept Remote Messages Unless Acting As Log Server | medium | pass  
5.1.1 | Enable cron Service | medium | pass  
5.1.2 | Verify Group Who Owns Crontab | medium | pass  
5.1.2 | Verify Owner on crontab | medium | pass  
5.1.2 | Verify Permissions on crontab | medium | pass  
5.1.3 | Verify Group Who Owns cron.hourly | medium | pass  
5.1.3 | Verify Owner on cron.hourly | medium | pass  
5.1.3 | Verify Permissions on cron.hourly | medium | pass  
5.1.4 | Verify Group Who Owns cron.daily | medium | pass  
5.1.4 | Verify Owner on cron.daily | medium | pass  
5.1.4 | Verify Permissions on cron.daily | medium | pass  
5.1.5 | Verify Group Who Owns cron.weekly | medium | pass  
5.1.5 | Verify Owner on cron.weekly | medium | pass  
5.1.5 | Verify Permissions on cron.weekly | medium | pass  
5.1.6 | Verify Group Who Owns cron.monthly | medium | pass  
5.1.6 | Verify Owner on cron.monthly | medium | pass  
5.1.6 | Verify Permissions on cron.monthly | medium | pass  
5.1.7 | Verify Group Who Owns cron.d | medium | pass  
5.1.7 | Verify Owner on cron.d | medium | pass  
5.1.7 | Verify Permissions on cron.d | medium | pass  
5.1.8 | Ensure that /etc/cron.deny does not exist | medium | pass  
5.1.8 | Verify Group Who Owns /etc/cron.allow file | medium | pass  
5.1.8 | Verify Permissions on /etc/cron.allow file | medium | pass  
5.1.8 | Verify User Who Owns /etc/cron.allow file | medium | pass  
5.1.9 | Ensure that /etc/at.deny does not exist | medium | pass  
5.1.9 | Verify Group Who Owns /etc/at.allow file | medium | pass  
5.1.9 | Verify Permissions on /etc/at.allow file | medium | pass  
5.1.9 | Verify User Who Owns /etc/at.allow file | medium | pass  
5.2.1 | Verify Group Who Owns SSH Server config file | medium | pass  
5.2.1 | Verify Owner on SSH Server config file | medium | pass  
5.2.1 | Verify Permissions on SSH Server config file | medium | pass  
5.2.2 | Verify Permissions on SSH Server Private *_key Key Files | medium | pass  
5.2.3 | Verify Permissions on SSH Server Public *.pub Key Files | medium | pass  
5.2.5 | Set LogLevel to INFO | low | pass  
5.2.6 | Enable PAM | medium | pass  
5.2.7 | Disable SSH Root Login | medium | pass  
5.2.8 | Disable Host-Based Authentication | medium | pass  
5.2.9 | Disable SSH Access via Empty Passwords | high | pass  
5.2.10 | Do Not Allow SSH Environment Options | medium | pass  
5.2.11 | Disable SSH Support for .rhosts Files | medium | pass  
5.2.12 | Disable X11 Forwarding | medium | pass  
5.2.13 | Use Only Strong Ciphers | medium | pass  
5.2.14 | Use Only Strong MACs | medium | pass  
5.2.15 | Use Only Strong Key Exchange algorithms | medium | pass  
5.2.16 | Disable SSH TCP Forwarding | medium | pass  
5.2.17 | Enable SSH Warning Banner | medium | pass  
5.2.18 | Set SSH authentication attempt limit | medium | pass  
5.2.19 | Ensure SSH MaxStartups is configured | medium | pass  
5.2.20 | Set SSH MaxSessions limit | medium | pass  
5.2.21 | Ensure SSH LoginGraceTime is configured | medium | pass  
5.2.22 | Set SSH Client Alive Count Max | medium | pass  
5.2.22 | Set SSH Client Alive Interval | medium | pass  
5.3.1 | Install sudo Package | medium | pass  
5.3.2 | Ensure Only Users Logged In To Real tty Can Execute Sudo - sudo use_pty | medium | pass  
5.3.3 | Ensure Sudo Logfile Exists - sudo logfile | low | pass  
5.3.5 | Ensure Users Re-Authenticate for Privilege Escalation - sudo !authenticate | medium | pass  
5.3.6 | Require Re-Authentication When Using the sudo Command | medium | pass  
5.3.7 | Enforce Usage of pam_wheel with Group Parameter for su Authentication | medium | pass  
5.3.7 | Ensure the Group Used by pam_wheel Module Exists on System and is Empty | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Authentication Retry Prompts Permitted Per-Session | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Different Categories | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Digit Characters | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Length | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Lowercase Characters | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Special Characters | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Uppercase Characters | medium | pass  
5.4.1 | Install pam_pwquality Package | medium | pass  
5.4.2 | Lock Accounts After Failed Password Attempts | medium | pass  
5.4.2 | Set Interval For Counting Failed Password Attempts | medium | pass  
5.4.2 | Set Lockout Time for Failed Password Attempts | medium | pass  
5.4.3 | Limit Password Reuse | medium | pass  
5.4.4 | Set Password Hashing Algorithm in /etc/login.defs | medium | pass  
5.5.1.1 | Set Existing Passwords Minimum Age | medium | pass  
5.5.1.1 | Set Password Minimum Age | medium | pass  
5.5.1.2 | Set Existing Passwords Maximum Age | medium | pass  
5.5.1.3 | Set Password Warning Age | medium | pass  
5.5.1.4 | Set Account Expiration Following Inactivity | medium | pass  
5.5.1.5 | Ensure all users last password change date is in the past | medium | pass  
5.5.2 | Ensure that System Accounts Do Not Run a Shell Upon Login | medium | pass  
5.5.3 | Verify Root Has A Primary GID 0 | high | pass  
5.5.4 | Ensure the Default Bash Umask is Set Correctly | medium | pass  
5.5.4 | Ensure the Default Umask is Set Correctly For Interactive Users | medium | pass  
5.5.4 | Ensure the Default Umask is Set Correctly in /etc/profile | medium | pass  
5.5.4 | Ensure the Default Umask is Set Correctly in login.defs | medium | pass  
5.5.5 | Set Interactive Session Timeout | medium | pass  
6.1.1 | Verify Group Who Owns passwd File | medium | pass  
6.1.1 | Verify Permissions on passwd File | medium | pass  
6.1.1 | Verify User Who Owns passwd File | medium | pass  
6.1.2 | Verify Group Who Owns Backup passwd File | medium | pass  
6.1.2 | Verify Permissions on Backup passwd File | medium | pass  
6.1.2 | Verify User Who Owns Backup passwd File | medium | pass  
6.1.3 | Verify Group Who Owns group File | medium | pass  
6.1.3 | Verify Permissions on group File | medium | pass  
6.1.3 | Verify User Who Owns group File | medium | pass  
6.1.4 | Verify Group Who Owns Backup group File | medium | pass  
6.1.4 | Verify Permissions on Backup group File | medium | pass  
6.1.4 | Verify User Who Owns Backup group File | medium | pass  
6.1.5 | Verify Group Who Owns shadow File | medium | pass  
6.1.5 | Verify Permissions on shadow File | medium | pass  
6.1.5 | Verify User Who Owns shadow File | medium | pass  
6.1.6 | Verify Group Who Owns Backup shadow File | medium | pass  
6.1.6 | Verify Permissions on Backup shadow File | medium | pass  
6.1.6 | Verify User Who Owns Backup shadow File | medium | pass  
6.1.7 | Verify Group Who Owns gshadow File | medium | pass  
6.1.7 | Verify Permissions on gshadow File | medium | pass  
6.1.7 | Verify User Who Owns gshadow File | medium | pass  
6.1.8 | Verify Group Who Owns Backup gshadow File | medium | pass  
6.1.8 | Verify Permissions on Backup gshadow File | medium | pass  
6.1.8 | Verify User Who Owns Backup gshadow File | medium | pass  
6.1.10 | Ensure All Files Are Owned by a User | medium | pass  
6.2.1 | Verify All Account Password Hashes are Shadowed | medium | pass  
6.2.2 | Ensure There Are No Accounts With Blank or Null Passwords | high | pass  
6.2.3 | All GIDs referenced in /etc/passwd must be defined in /etc/group | low | pass  
6.2.4 | Ensure shadow group is empty | medium | pass  
6.2.5 | Ensure All Accounts on the System Have Unique User IDs | medium | pass  
6.2.6 | Ensure All Groups on the System Have Unique Group ID | medium | pass  
6.2.7 | Ensure All Accounts on the System Have Unique Names | medium | pass  
6.2.8 | Ensure All Groups on the System Have Unique Group Names | medium | pass  
6.2.9 | Ensure that Root's Path Does Not Include Relative Paths or Null Directories | unknown | pass  
6.2.9 | Ensure that Root's Path Does Not Include World or Group-Writable Directories | medium | pass  
6.2.10 | Verify Only Root Has UID 0 | high | pass  
6.2.11 | All Interactive Users Home Directories Must Exist | medium | pass  
6.2.12 | All Interactive User Home Directories Must Be Group-Owned By The Primary Group | medium | pass  
6.2.12 | All Interactive User Home Directories Must Be Owned By The Primary User | medium | pass  
6.2.13 | All Interactive User Home Directories Must Have mode 0750 Or Less Permissive | medium | pass  
6.2.14 | Verify No netrc Files Exist | medium | pass  
6.2.15 | Verify No .forward Files Exist | medium | pass  
6.2.16 | Remove Rsh Trust Files | high | pass  
6.2.17 | User Initialization Files Must Be Group-Owned By The Primary Group | medium | pass  
6.2.17 | User Initialization Files Must Be Owned By the Primary User | medium | pass  
6.2.17 | User Initialization Files Must Not Run World-Writable Programs | medium | pass  
  
### Not applicable recommendations

The following table lists the recommendations that don't apply for Google Distributed Cloud.

# | Recommendation | Severity | Status  
---|---|---|---  
1.1.2.2 | Add nodev Option to /tmp | medium | notapplicable  
1.1.2.3 | Add noexec Option to /tmp | medium | notapplicable  
1.1.2.4 | Add nosuid Option to /tmp | medium | notapplicable  
1.1.3.2 | Add nodev Option to /var | medium | notapplicable  
1.1.3.3 | Add nosuid Option to /var | medium | notapplicable  
1.1.4.2 | Add noexec Option to /var/tmp | medium | notapplicable  
1.1.4.3 | Add nosuid Option to /var/tmp | medium | notapplicable  
1.1.4.4 | Add nodev Option to /var/tmp | medium | notapplicable  
1.1.5.2 | Add nodev Option to /var/log | medium | notapplicable  
1.1.5.3 | Add noexec Option to /var/log | medium | notapplicable  
1.1.5.4 | Add nosuid Option to /var/log | medium | notapplicable  
1.1.6.2 | Add noexec Option to /var/log/audit | medium | notapplicable  
1.1.6.3 | Add nodev Option to /var/log/audit | medium | notapplicable  
1.1.6.4 | Add nosuid Option to /var/log/audit | medium | notapplicable  
1.1.7.2 | Add nodev Option to /home | unknown | notapplicable  
1.1.7.3 | Add nosuid Option to /home | medium | notapplicable  
1.4.1 | Set the UEFI Boot Loader Password | high | notapplicable  
1.8.1 | Remove the GDM Package Group | medium | notapplicable  
1.8.4 | Enable GNOME3 Screensaver Lock After Idle Period | medium | notapplicable  
1.8.5 | Set GNOME3 Screensaver Lock Delay After Activation Period | medium | notapplicable  
1.8.6 | Disable GNOME3 Automount Opening | medium | notapplicable  
1.8.6 | Disable GNOME3 Automounting | medium | notapplicable  
1.8.8 | Disable GNOME3 Automount running | low | notapplicable  
1.8.10 | Disable XDMCP in GDM | high | notapplicable  
1.10 | Configure GNOME3 DConf User Profile | high | notapplicable  
2.1.4.1 | Configure server restrictions for ntpd | medium | notapplicable  
2.1.4.3 | Configure ntpd To Run As ntp User | medium | notapplicable  
2.1.4.4 | Enable the NTP Daemon | high | notapplicable  
2.2.15 | Disable Postfix Network Listening | medium | notapplicable  
3.5.1.3 | Verify ufw Enabled | medium | notapplicable  
3.5.1.4 | Set UFW Loopback Traffic | medium | notapplicable  
3.5.1.6 | Ensure ufw Firewall Rules Exist for All Open Ports | medium | notapplicable  
3.5.1.7 | Ensure ufw Default Deny Firewall Policy | medium | notapplicable  
3.5.3.2.1 | Set Default iptables Policy for Incoming Packets | medium | notapplicable  
3.5.3.2.2 | Set configuration for loopback traffic | medium | notapplicable  
3.5.3.2.4 | Ensure iptables Firewall Rules Exist for All Open Ports | medium | notapplicable  
3.5.3.3.1 | Set Default ip6tables Policy for Incoming Packets | medium | notapplicable  
3.5.3.3.4 | Ensure ip6tables Firewall Rules Exist for All Open Ports | medium | notapplicable  
  
### 1.30

### Versions

This section refers to these versions:

Google Distributed Cloud version | Ubuntu version | CIS Ubuntu Benchmark version | CIS level   
---|---|---|---  
1.30 | 22.04 LTS | v1.0.0 | Level 2 Server  
  
### Failed recommendations

The following table lists the recommendations for which Google Distributed Cloud deviates from the benchmark's recommendations. These findings apply to cluster nodes and the admin workstation.

# | Recommendation | Severity | Status  
---|---|---|---  
1.1.2.1 | Ensure /tmp Located On Separate Partition | low | fail  
1.1.3.1 | Ensure /var Located On Separate Partition | low | fail  
1.1.4.1 | Ensure /var/tmp Located On Separate Partition | medium | fail  
1.1.5.1 | Ensure /var/log Located On Separate Partition | low | fail  
1.1.6.1 | Ensure /var/log/audit Located On Separate Partition | low | fail  
1.1.7.1 | Ensure /home Located On Separate Partition | low | fail  
1.4.1 | Set Boot Loader Password in grub2 | high | fail  
1.4.3 | Ensure Authentication Required for Single User Mode | medium | fail  
2.3.6 | Uninstall rpcbind Package | low | fail  
3.2.2 | Disable Kernel Parameter for IP Forwarding on IPv4 Interfaces | medium | fail  
3.3.7 | Enable Kernel Parameter to Use Reverse Path Filtering on all IPv4 Interfaces by Default | medium | fail  
3.3.7 | Enable Kernel Parameter to Use Reverse Path Filtering on all IPv4 Interfaces | medium | fail  
3.5.2.8 | Ensure nftables default deny firewall policy | medium | fail  
3.5.2.10 | Ensure nftables rules are permanent | medium | fail  
4.2.3 | Verify permissions of log files | medium | fail  
5.2.4 | Limit Users' SSH Access | unknown | fail  
5.3.4 | Ensure Users Re-Authenticate for Privilege Escalation - sudo | medium | fail  
5.5.1.2 | Set Password Maximum Age | medium | fail  
  
### Passed recommendations

The following table lists the recommendations for which Google Distributed Cloud complies with the benchmark's recommendations.

# | Recommendation | Severity | Status  
---|---|---|---  
1.1.1.1 | Disable Mounting of cramfs | low | pass  
1.1.1.2 | Disable Mounting of squashfs | low | pass  
1.1.1.3 | Disable Mounting of udf | low | pass  
1.1.8.1 | Add nodev Option to /dev/shm | medium | pass  
1.1.8.2 | Add noexec Option to /dev/shm | medium | pass  
1.1.8.3 | Add nosuid Option to /dev/shm | medium | pass  
1.1.9 | Disable the Automounter | medium | pass  
1.1.10 | Disable Modprobe Loading of USB Storage Driver | medium | pass  
1.4.2 | Verify /boot/grub/grub.cfg Permissions | medium | pass  
1.5.1 | Enable Randomized Layout of Virtual Address Space | medium | pass  
1.5.2 | Package "prelink" Must not be Installed | medium | pass  
1.5.3 | Disable Apport Service | unknown | pass  
1.5.4 | Disable Core Dumps for All Users | medium | pass  
1.5.4 | Disable Core Dumps for SUID programs | medium | pass  
1.6.1.1 | Ensure AppArmor is installed | medium | pass  
1.6.1.2 | Ensure AppArmor is enabled in the bootloader configuration | medium | pass  
1.6.1.4 | Enforce all AppArmor Profiles | medium | pass  
1.7.1 | Modify the System Message of the Day Banner | medium | pass  
1.7.2 | Modify the System Login Banner | medium | pass  
1.7.3 | Modify the System Login Banner for Remote Connections | medium | pass  
1.7.4 | Verify Group Ownership of Message of the Day Banner | medium | pass  
1.7.4 | Verify ownership of Message of the Day Banner | medium | pass  
1.7.4 | Verify permissions on Message of the Day Banner | medium | pass  
1.7.5 | Verify Group Ownership of System Login Banner | medium | pass  
1.7.5 | Verify ownership of System Login Banner | medium | pass  
1.7.5 | Verify permissions on System Login Banner | medium | pass  
1.7.6 | Verify Group Ownership of System Login Banner for Remote Connections | medium | pass  
1.7.6 | Verify ownership of System Login Banner for Remote Connections | medium | pass  
1.7.6 | Verify permissions on System Login Banner for Remote Connections | medium | pass  
2.1.1.1 | Install the systemd_timesyncd Service | high | pass  
2.1.3.2 | Enable systemd_timesyncd Service | high | pass  
2.2.1 | Remove the X Windows Package Group | medium | pass  
2.2.2 | Disable Avahi Server Software | medium | pass  
2.2.2 | Uninstall avahi Server Package | medium | pass  
2.2.3 | Disable the CUPS Service | unknown | pass  
2.2.3 | Uninstall CUPS Package | unknown | pass  
2.2.4 | Uninstall DHCP Server Package | medium | pass  
2.2.5 | Uninstall openldap-servers Package | low | pass  
2.2.6 | Uninstall nfs-kernel-server Package | low | pass  
2.2.7 | Uninstall bind Package | low | pass  
2.2.8 | Uninstall vsftpd Package | high | pass  
2.2.9 | Uninstall httpd Package | unknown | pass  
2.2.9 | Uninstall nginx Package | unknown | pass  
2.2.10 | Uninstall cyrus-imapd Package | unknown | pass  
2.2.10 | Uninstall dovecot Package | unknown | pass  
2.2.11 | Uninstall Samba Package | unknown | pass  
2.2.12 | Uninstall squid Package | unknown | pass  
2.2.13 | Uninstall net-snmp Package | unknown | pass  
2.2.14 | Uninstall the nis package | low | pass  
2.2.15 | Ensure Mail Transfer Agent is not Listening on any non-loopback Address | medium | pass  
2.2.16 | Uninstall rsync Package | medium | pass  
2.3.2 | Uninstall rsh Package | unknown | pass  
2.3.3 | Uninstall talk Package | medium | pass  
2.3.4 | Remove telnet Clients | low | pass  
2.3.5 | Ensure LDAP client is not installed | low | pass  
3.1.2 | Deactivate Wireless Network Interfaces | medium | pass  
3.2.1 | Disable Kernel Parameter for Sending ICMP Redirects on all IPv4 Interfaces by Default | medium | pass  
3.2.1 | Disable Kernel Parameter for Sending ICMP Redirects on all IPv4 Interfaces | medium | pass  
3.2.2 | Disable Kernel Parameter for IPv6 Forwarding | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on all IPv4 Interfaces | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on all IPv6 Interfaces | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on IPv4 Interfaces by Default | medium | pass  
3.3.1 | Disable Kernel Parameter for Accepting Source-Routed Packets on IPv6 Interfaces by Default | medium | pass  
3.3.2 | Disable Accepting ICMP Redirects for All IPv4 Interfaces | medium | pass  
3.3.2 | Disable Accepting ICMP Redirects for All IPv6 Interfaces | medium | pass  
3.3.2 | Disable Kernel Parameter for Accepting ICMP Redirects by Default on IPv4 Interfaces | medium | pass  
3.3.2 | Disable Kernel Parameter for Accepting ICMP Redirects by Default on IPv6 Interfaces | medium | pass  
3.3.3 | Configure Kernel Parameter for Accepting Secure Redirects By Default | medium | pass  
3.3.3 | Disable Kernel Parameter for Accepting Secure ICMP Redirects on all IPv4 Interfaces | medium | pass  
3.3.4 | Enable Kernel Parameter to Log Martian Packets on all IPv4 Interfaces | unknown | pass  
3.3.4 | Enable Kernel Parameter to Log Martian Packets on all IPv4 Interfaces by Default | unknown | pass  
3.3.5 | Enable Kernel Parameter to Ignore ICMP Broadcast Echo Requests on IPv4 Interfaces | medium | pass  
3.3.6 | Enable Kernel Parameter to Ignore Bogus ICMP Error Responses on IPv4 Interfaces | unknown | pass  
3.3.8 | Enable Kernel Parameter to Use TCP Syncookies on Network Interfaces | medium | pass  
3.3.9 | Configure Accepting Router Advertisements on All IPv6 Interfaces | medium | pass  
3.3.9 | Disable Accepting Router Advertisements on all IPv6 Interfaces by Default | medium | pass  
3.4.1 | Disable DCCP Support | medium | pass  
3.4.2 | Disable SCTP Support | medium | pass  
3.4.3 | Disable RDS Support | low | pass  
3.4.4 | Disable TIPC Support | low | pass  
3.5.1.2 | Remove iptables-persistent Package | medium | pass  
3.5.2.1 | Install nftables Package | medium | pass  
3.5.2.4 | Ensure a Table Exists for Nftables | medium | pass  
3.5.2.5 | Ensure Base Chains Exist for Nftables | medium | pass  
3.5.2.9 | Verify nftables Service is Enabled | medium | pass  
3.5.3.1.1 | Install iptables Package | medium | pass  
3.5.3.1.3 | Remove ufw Package | medium | pass  
4.1.1.1 | Ensure the audit Subsystem is Installed | medium | pass  
4.1.1.2 | Enable auditd Service | medium | pass  
4.1.1.4 | Extend Audit Backlog Limit for the Audit Daemon | low | pass  
4.1.2.1 | Configure auditd Max Log File Size | medium | pass  
4.1.2.2 | Configure auditd max_log_file_action Upon Reaching Maximum Log Size | medium | pass  
4.1.2.3 | Configure auditd admin_space_left Action on Low Disk Space | medium | pass  
4.1.2.3 | Configure auditd mail_acct Action on Low Disk Space | medium | pass  
4.1.2.3 | Configure auditd space_left Action on Low Disk Space | medium | pass  
4.1.3.1 | Ensure auditd Collects System Administrator Actions | medium | pass  
4.1.3.2 | Record Events When Privileged Executables Are Run | medium | pass  
4.1.3.3 | Record Attempts to perform maintenance activities | medium | pass  
4.1.3.4 | Record Attempts to Alter the localtime File | medium | pass  
4.1.3.4 | Record attempts to alter time through adjtimex | medium | pass  
4.1.3.4 | Record Attempts to Alter Time Through clock_settime | medium | pass  
4.1.3.4 | Record attempts to alter time through settimeofday | medium | pass  
4.1.3.4 | Record Attempts to Alter Time Through stime | medium | pass  
4.1.3.5 | Record Events that Modify the System's Network Environment | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - su | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - sudo | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - sudoedit | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - umount | medium | pass  
4.1.3.6 | Ensure auditd Collects Information on the Use of Privileged Commands - unix_chkpwd | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - creat | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - ftruncate | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - open | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - openat | medium | pass  
4.1.3.7 | Record Unsuccessful Access Attempts to Files - truncate | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/group | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/gshadow | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/passwd | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/security/opasswd | medium | pass  
4.1.3.8 | Record Events that Modify User/Group Information - /etc/shadow | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - chmod | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - chown | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchmod | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchmodat | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchown | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fchownat | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fremovexattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - fsetxattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - lchown | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - lremovexattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - lsetxattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - removexattr | medium | pass  
4.1.3.9 | Record Events that Modify the System's Discretionary Access Controls - setxattr | medium | pass  
4.1.3.10 | Ensure auditd Collects Information on Exporting to Media (successful) | medium | pass  
4.1.3.11 | Record Attempts to Alter Process and Session Initiation Information | medium | pass  
4.1.3.12 | Record Attempts to Alter Logon and Logout Events - faillog | medium | pass  
4.1.3.12 | Record Attempts to Alter Logon and Logout Events - lastlog | medium | pass  
4.1.3.12 | Record Attempts to Alter Logon and Logout Events - tallylog | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - rename | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - renameat | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - unlink | medium | pass  
4.1.3.13 | Ensure auditd Collects File Deletion Events by User - unlinkat | medium | pass  
4.1.3.14 | Record Events that Modify the System's Mandatory Access Controls | medium | pass  
4.1.3.15 | Record Any Attempts to Run chcon | medium | pass  
4.1.3.16 | Record Any Attempts to Run setfacl | medium | pass  
4.1.3.17 | Record Any Attempts to Run chacl | medium | pass  
4.1.3.18 | Ensure auditd Collects Information on the Use of Privileged Commands - usermod | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on Kernel Module Loading - init_module | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on Kernel Module Unloading - delete_module | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on the Use of Privileged Commands - insmod | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on the Use of Privileged Commands - modprobe | medium | pass  
4.1.3.19 | Ensure auditd Collects Information on the Use of Privileged Commands - rmmod | medium | pass  
4.1.3.20 | Make the auditd Configuration Immutable | medium | pass  
4.1.4.1 | System Audit Logs Must Have Mode 0640 or Less Permissive | medium | pass  
4.1.4.2 | System Audit Logs Must Be Owned By Root | medium | pass  
4.1.4.3 | System Audit Logs Must Be Group Owned By Root | medium | pass  
4.1.4.4 | System Audit Logs Must Have Mode 0750 or Less Permissive | medium | pass  
4.1.4.5 | Verify Permissions on /etc/audit/auditd.conf | medium | pass  
4.1.4.5 | Verify Permissions on /etc/audit/rules.d/*.rules | medium | pass  
4.1.4.6 | Audit Configuration Files Must Be Owned By Root | medium | pass  
4.1.4.7 | Audit Configuration Files Must Be Owned By Group root | medium | pass  
4.1.4.8 | Verify that audit tools Have Mode 0755 or less | medium | pass  
4.1.4.9 | Verify that audit tools are owned by root | medium | pass  
4.1.4.10 | Verify that audit tools are owned by group root | medium | pass  
4.2.1.1.1 | Install systemd-journal-remote Package | medium | pass  
4.2.1.1.4 | Disable systemd-journal-remote Socket | medium | pass  
4.2.1.2 | Enable systemd-journald Service | medium | pass  
4.2.1.3 | Ensure journald is configured to compress large log files | medium | pass  
4.2.1.4 | Ensure journald is configured to write log files to persistent disk | medium | pass  
4.2.2.1 | Ensure rsyslog is Installed | medium | pass  
4.2.2.2 | Enable rsyslog Service | medium | pass  
4.2.2.4 | Ensure rsyslog Default File Permissions Configured | medium | pass  
4.2.2.7 | Ensure rsyslog Does Not Accept Remote Messages Unless Acting As Log Server | medium | pass  
5.1.1 | Enable cron Service | medium | pass  
5.1.2 | Verify Group Who Owns Crontab | medium | pass  
5.1.2 | Verify Owner on crontab | medium | pass  
5.1.2 | Verify Permissions on crontab | medium | pass  
5.1.3 | Verify Group Who Owns cron.hourly | medium | pass  
5.1.3 | Verify Owner on cron.hourly | medium | pass  
5.1.3 | Verify Permissions on cron.hourly | medium | pass  
5.1.4 | Verify Group Who Owns cron.daily | medium | pass  
5.1.4 | Verify Owner on cron.daily | medium | pass  
5.1.4 | Verify Permissions on cron.daily | medium | pass  
5.1.5 | Verify Group Who Owns cron.weekly | medium | pass  
5.1.5 | Verify Owner on cron.weekly | medium | pass  
5.1.5 | Verify Permissions on cron.weekly | medium | pass  
5.1.6 | Verify Group Who Owns cron.monthly | medium | pass  
5.1.6 | Verify Owner on cron.monthly | medium | pass  
5.1.6 | Verify Permissions on cron.monthly | medium | pass  
5.1.7 | Verify Group Who Owns cron.d | medium | pass  
5.1.7 | Verify Owner on cron.d | medium | pass  
5.1.7 | Verify Permissions on cron.d | medium | pass  
5.1.8 | Ensure that /etc/cron.deny does not exist | medium | pass  
5.1.8 | Verify Group Who Owns /etc/cron.allow file | medium | pass  
5.1.8 | Verify Permissions on /etc/cron.allow file | medium | pass  
5.1.8 | Verify User Who Owns /etc/cron.allow file | medium | pass  
5.1.9 | Ensure that /etc/at.deny does not exist | medium | pass  
5.1.9 | Verify Group Who Owns /etc/at.allow file | medium | pass  
5.1.9 | Verify Permissions on /etc/at.allow file | medium | pass  
5.1.9 | Verify User Who Owns /etc/at.allow file | medium | pass  
5.2.1 | Verify Group Who Owns SSH Server config file | medium | pass  
5.2.1 | Verify Owner on SSH Server config file | medium | pass  
5.2.1 | Verify Permissions on SSH Server config file | medium | pass  
5.2.2 | Verify Permissions on SSH Server Private *_key Key Files | medium | pass  
5.2.3 | Verify Permissions on SSH Server Public *.pub Key Files | medium | pass  
5.2.5 | Set LogLevel to INFO | low | pass  
5.2.6 | Enable PAM | medium | pass  
5.2.7 | Disable SSH Root Login | medium | pass  
5.2.8 | Disable Host-Based Authentication | medium | pass  
5.2.9 | Disable SSH Access via Empty Passwords | high | pass  
5.2.10 | Do Not Allow SSH Environment Options | medium | pass  
5.2.11 | Disable SSH Support for .rhosts Files | medium | pass  
5.2.12 | Disable X11 Forwarding | medium | pass  
5.2.13 | Use Only Strong Ciphers | medium | pass  
5.2.14 | Use Only Strong MACs | medium | pass  
5.2.15 | Use Only Strong Key Exchange algorithms | medium | pass  
5.2.16 | Disable SSH TCP Forwarding | medium | pass  
5.2.17 | Enable SSH Warning Banner | medium | pass  
5.2.18 | Set SSH authentication attempt limit | medium | pass  
5.2.19 | Ensure SSH MaxStartups is configured | medium | pass  
5.2.20 | Set SSH MaxSessions limit | medium | pass  
5.2.21 | Ensure SSH LoginGraceTime is configured | medium | pass  
5.2.22 | Set SSH Client Alive Count Max | medium | pass  
5.2.22 | Set SSH Client Alive Interval | medium | pass  
5.3.1 | Install sudo Package | medium | pass  
5.3.2 | Ensure Only Users Logged In To Real tty Can Execute Sudo - sudo use_pty | medium | pass  
5.3.3 | Ensure Sudo Logfile Exists - sudo logfile | low | pass  
5.3.5 | Ensure Users Re-Authenticate for Privilege Escalation - sudo !authenticate | medium | pass  
5.3.6 | Require Re-Authentication When Using the sudo Command | medium | pass  
5.3.7 | Enforce Usage of pam_wheel with Group Parameter for su Authentication | medium | pass  
5.3.7 | Ensure the Group Used by pam_wheel Module Exists on System and is Empty | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Authentication Retry Prompts Permitted Per-Session | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Different Categories | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Digit Characters | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Length | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Lowercase Characters | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Special Characters | medium | pass  
5.4.1 | Ensure PAM Enforces Password Requirements - Minimum Uppercase Characters | medium | pass  
5.4.1 | Install pam_pwquality Package | medium | pass  
5.4.2 | Lock Accounts After Failed Password Attempts | medium | pass  
5.4.2 | Set Interval For Counting Failed Password Attempts | medium | pass  
5.4.2 | Set Lockout Time for Failed Password Attempts | medium | pass  
5.4.3 | Limit Password Reuse | medium | pass  
5.4.4 | Set Password Hashing Algorithm in /etc/login.defs | medium | pass  
5.5.1.1 | Set Existing Passwords Minimum Age | medium | pass  
5.5.1.1 | Set Password Minimum Age | medium | pass  
5.5.1.2 | Set Existing Passwords Maximum Age | medium | pass  
5.5.1.3 | Set Password Warning Age | medium | pass  
5.5.1.4 | Set Account Expiration Following Inactivity | medium | pass  
5.5.1.5 | Ensure all users last password change date is in the past | medium | pass  
5.5.2 | Ensure that System Accounts Do Not Run a Shell Upon Login | medium | pass  
5.5.3 | Verify Root Has A Primary GID 0 | high | pass  
5.5.4 | Ensure the Default Bash Umask is Set Correctly | medium | pass  
5.5.4 | Ensure the Default Umask is Set Correctly For Interactive Users | medium | pass  
5.5.4 | Ensure the Default Umask is Set Correctly in /etc/profile | medium | pass  
5.5.4 | Ensure the Default Umask is Set Correctly in login.defs | medium | pass  
5.5.5 | Set Interactive Session Timeout | medium | pass  
6.1.1 | Verify Group Who Owns passwd File | medium | pass  
6.1.1 | Verify Permissions on passwd File | medium | pass  
6.1.1 | Verify User Who Owns passwd File | medium | pass  
6.1.2 | Verify Group Who Owns Backup passwd File | medium | pass  
6.1.2 | Verify Permissions on Backup passwd File | medium | pass  
6.1.2 | Verify User Who Owns Backup passwd File | medium | pass  
6.1.3 | Verify Group Who Owns group File | medium | pass  
6.1.3 | Verify Permissions on group File | medium | pass  
6.1.3 | Verify User Who Owns group File | medium | pass  
6.1.4 | Verify Group Who Owns Backup group File | medium | pass  
6.1.4 | Verify Permissions on Backup group File | medium | pass  
6.1.4 | Verify User Who Owns Backup group File | medium | pass  
6.1.5 | Verify Group Who Owns shadow File | medium | pass  
6.1.5 | Verify Permissions on shadow File | medium | pass  
6.1.5 | Verify User Who Owns shadow File | medium | pass  
6.1.6 | Verify Group Who Owns Backup shadow File | medium | pass  
6.1.6 | Verify Permissions on Backup shadow File | medium | pass  
6.1.6 | Verify User Who Owns Backup shadow File | medium | pass  
6.1.7 | Verify Group Who Owns gshadow File | medium | pass  
6.1.7 | Verify Permissions on gshadow File | medium | pass  
6.1.7 | Verify User Who Owns gshadow File | medium | pass  
6.1.8 | Verify Group Who Owns Backup gshadow File | medium | pass  
6.1.8 | Verify Permissions on Backup gshadow File | medium | pass  
6.1.8 | Verify User Who Owns Backup gshadow File | medium | pass  
6.1.10 | Ensure All Files Are Owned by a User | medium | pass  
6.2.1 | Verify All Account Password Hashes are Shadowed | medium | pass  
6.2.2 | Ensure There Are No Accounts With Blank or Null Passwords | high | pass  
6.2.3 | All GIDs referenced in /etc/passwd must be defined in /etc/group | low | pass  
6.2.4 | Ensure shadow group is empty | medium | pass  
6.2.5 | Ensure All Accounts on the System Have Unique User IDs | medium | pass  
6.2.6 | Ensure All Groups on the System Have Unique Group ID | medium | pass  
6.2.7 | Ensure All Accounts on the System Have Unique Names | medium | pass  
6.2.8 | Ensure All Groups on the System Have Unique Group Names | medium | pass  
6.2.9 | Ensure that Root's Path Does Not Include Relative Paths or Null Directories | unknown | pass  
6.2.9 | Ensure that Root's Path Does Not Include World or Group-Writable Directories | medium | pass  
6.2.10 | Verify Only Root Has UID 0 | high | pass  
6.2.11 | All Interactive Users Home Directories Must Exist | medium | pass  
6.2.12 | All Interactive User Home Directories Must Be Group-Owned By The Primary Group | medium | pass  
6.2.12 | All Interactive User Home Directories Must Be Owned By The Primary User | medium | pass  
6.2.13 | All Interactive User Home Directories Must Have mode 0750 Or Less Permissive | medium | pass  
6.2.14 | Verify No netrc Files Exist | medium | pass  
6.2.15 | Verify No .forward Files Exist | medium | pass  
6.2.16 | Remove Rsh Trust Files | high | pass  
6.2.17 | User Initialization Files Must Be Group-Owned By The Primary Group | medium | pass  
6.2.17 | User Initialization Files Must Be Owned By the Primary User | medium | pass  
6.2.17 | User Initialization Files Must Not Run World-Writable Programs | medium | pass  
  
### Not applicable recommendations

The following table lists the recommendations that don't apply for Google Distributed Cloud.

# | Recommendation | Severity | Status  
---|---|---|---  
1.1.2.2 | Add nodev Option to /tmp | medium | notapplicable  
1.1.2.3 | Add noexec Option to /tmp | medium | notapplicable  
1.1.2.4 | Add nosuid Option to /tmp | medium | notapplicable  
1.1.3.2 | Add nodev Option to /var | medium | notapplicable  
1.1.3.3 | Add nosuid Option to /var | medium | notapplicable  
1.1.4.2 | Add noexec Option to /var/tmp | medium | notapplicable  
1.1.4.3 | Add nosuid Option to /var/tmp | medium | notapplicable  
1.1.4.4 | Add nodev Option to /var/tmp | medium | notapplicable  
1.1.5.2 | Add nodev Option to /var/log | medium | notapplicable  
1.1.5.3 | Add noexec Option to /var/log | medium | notapplicable  
1.1.5.4 | Add nosuid Option to /var/log | medium | notapplicable  
1.1.6.2 | Add noexec Option to /var/log/audit | medium | notapplicable  
1.1.6.3 | Add nodev Option to /var/log/audit | medium | notapplicable  
1.1.6.4 | Add nosuid Option to /var/log/audit | medium | notapplicable  
1.1.7.2 | Add nodev Option to /home | unknown | notapplicable  
1.1.7.3 | Add nosuid Option to /home | medium | notapplicable  
1.4.1 | Set the UEFI Boot Loader Password | high | notapplicable  
1.8.1 | Remove the GDM Package Group | medium | notapplicable  
1.8.4 | Enable GNOME3 Screensaver Lock After Idle Period | medium | notapplicable  
1.8.5 | Set GNOME3 Screensaver Lock Delay After Activation Period | medium | notapplicable  
1.8.6 | Disable GNOME3 Automount Opening | medium | notapplicable  
1.8.6 | Disable GNOME3 Automounting | medium | notapplicable  
1.8.8 | Disable GNOME3 Automount running | low | notapplicable  
1.8.10 | Disable XDMCP in GDM | high | notapplicable  
1.10 | Configure GNOME3 DConf User Profile | high | notapplicable  
2.1.4.1 | Configure server restrictions for ntpd | medium | notapplicable  
2.1.4.3 | Configure ntpd To Run As ntp User | medium | notapplicable  
2.1.4.4 | Enable the NTP Daemon | high | notapplicable  
2.2.15 | Disable Postfix Network Listening | medium | notapplicable  
3.5.1.3 | Verify ufw Enabled | medium | notapplicable  
3.5.1.4 | Set UFW Loopback Traffic | medium | notapplicable  
3.5.1.6 | Ensure ufw Firewall Rules Exist for All Open Ports | medium | notapplicable  
3.5.1.7 | Ensure ufw Default Deny Firewall Policy | medium | notapplicable  
3.5.3.2.1 | Set Default iptables Policy for Incoming Packets | medium | notapplicable  
3.5.3.2.2 | Set configuration for loopback traffic | medium | notapplicable  
3.5.3.2.4 | Ensure iptables Firewall Rules Exist for All Open Ports | medium | notapplicable  
3.5.3.3.1 | Set Default ip6tables Policy for Incoming Packets | medium | notapplicable  
3.5.3.3.4 | Ensure ip6tables Firewall Rules Exist for All Open Ports | medium | notapplicable  
  
## Configure AIDE cron job

AIDE is a file integrity checking tool that verifies compliance with CIS L1 Server benchmark 1.4 `Filesystem Integrity Checking`. In Google Distributed Cloud, the AIDE process has been causing high resource usage issues.

The AIDE process on nodes is disabled by default to prevent resource issues. This will affect compliance with CIS L1 Server benchmark 1.4.2: `Ensure filesystem integrity is regularly checked.`

If you want to opt in to run the AIDE cron job, complete the following steps to re-enable AIDE:

  1. Create a DaemonSet.

Here's a manifest for a DaemonSet:
         
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
         name: enable-aide-pool1
         spec:
         selector:
           matchLabels:
             app: enable-aide-pool1
         template:
           metadata:
             labels:
               app: enable-aide-pool1
           spec:
             hostIPC: true
             hostPID: true
             nodeSelector:
               cloud.google.com/gke-nodepool: pool-1
             containers:
             - name: update-audit-rule
               image: ubuntu
               command: ["chroot", "/host", "bash", "-c"]
               args:
               - |
                 set -x
                 while true; do
                   # change daily cronjob schedule
                   minute=30;hour=5
                   sed -E "s/([0-9]+ [0-9]+)(.*run-parts --report \/etc\/cron.daily.*)/$minute $hour\2/g" -i /etc/crontab
         
                   # enable aide
                   chmod 755 /etc/cron.daily/aide
         
                   sleep 3600
                 done
               volumeMounts:
               - name: host
                 mountPath: /host
               securityContext:
                 privileged: true
             volumes:
             - name: host
               hostPath:
                 path: /
         

In the preceding manifest:

     * The AIDE cron job will only run on node pool `pool-1` as specified by the nodeSelector `cloud.google.com/gke-nodepool: pool-1`. You can configure the AIDE process to run on as many node pools as you want by specifying the pools under the `nodeSelector` field. To run the same cron job schedule across different node pools, remove the `nodeSelector` field. However, to avoid host resource congestions, we recommend you maintain separate schedules.

     * The cron job is scheduled to run daily at 5:30am as specified by the configuration `minute=30;hour=5`. You can configure different schedules for the AIDE cron job as required.

  2. Copy the manifest to a file named `enable-aide.yaml`, and create the DaemonSet:
         
         kubectl apply --kubeconfig USER_CLUSTER_KUBECONFIG -f enable-aide.yaml
         

where USER_CLUSTER_KUBECONFIG is the path of the [kubeconfig file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster#locate-user-cluster-kubeconfig) for your user cluster.




## Use Security Content Automation Protocol (SCAP) evaluation

We recommend that you scan your installation yourself to evaluate its Level 2 compliance with the [Ubuntu Linux CIS benchmark](https://www.cisecurity.org/benchmark/ubuntu_linux). There are a variety of tools available for scanning your clusters and admin workstation. You can use the following steps to install and run the [OpenSCAP open-source toolset](https://www.open-scap.org/) to perform a Level 2 security assessment:

  1. Copy the following script to a file called `cis-benchmark.sh`:
         
         #!/bin/bash
         
         set -x
         
         REPORTS_DIR="$1"
         
         mkdir -p "${REPORTS_DIR}"
         
         echo "Start CIS L2 benchmark evaluation..."
         apt update
         apt install libopenscap8
         sudo oscap xccdf eval \
             --profile cis_level2_server_customized \
             --tailoring-file /etc/cloud/usg/tailored-cis-level2-server-anthos-wmware.xml \
             --results "${REPORTS_DIR}"/cis-results.xml \
             --report "${REPORTS_DIR}"/cis-report.html \
             --verbose INFO \
             --verbose-log-file "${REPORTS_DIR}/cis-output-verbose.log" \
             /etc/cloud/usg/ssg-ubuntu2204-ds-1.2.xml > "${REPORTS_DIR}"/cis-output.log 2>&1
         chmod -R 755 "${REPORTS_DIR}/.."
         echo "Done CIS L2 benchmark evaluation"
         

  2. Make the script executable:
         
         chmod +x cis-benchmark.sh
         

  3. Run the script:
         
         ./cis-benchmark.sh REPORTS_DIR
         

Replace `REPORTS_DIR` with the path of an existing directory where you want to save the generated evaluation report.

When the script completes successfully, the `REPORTS_DIR` directory contains the generated `cis-report.html` file.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
