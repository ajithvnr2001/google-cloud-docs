---
url: https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/using-mailgun/
title: Sending email with Mailgun \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:22.584822+00:00
---

# Sending email with Mailgun  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/using-mailgun/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Sending email with Mailgun Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud works with Mailgun to provide an email service that has a programmatic API, log retention, email personalization, analytics, and email validation.

The following instructions show you how to configure Mailgun as an email relay with Postfix.

## Before you begin

  1. Sign up for and create a new Mailgun account on the [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/details/mailgun/emailapi).

  2. Get your credentials. The instructions require that you know your Mailgun SMTP username, password, and hostname. Get your username and password from the Mailgun control panel, under the **Domains** section.

Depending on how the domain is configured in Mailgun, the SMTP hostname is either `smtp.mailgun.org` or `smtp.eu.mailgun.org`.

  3. Configure your [firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) to allow outgoing traffic on TCP port `2525`.




## Configuring Mailgun as a mail relay with Postfix

Configuring Mailgun as a mail relay allows the [Postfix](http://www.postfix.org) mail transfer agent to forward emails destined for remote delivery.

  1. Connect to your instance using SSH.
         
         gcloud compute ssh [INSTANCE_NAME]
         

where `[INSTANCE_NAME]` is the name of the VM instance where you want to send email from.

  2. Become a superuser and set a safe umask.
         
         user@test-instance:~$ sudo su -
         
         
         root@test-instance:~# umask 077
         

  3. Install the Postfix Mail Transport Agent.

###  Debian 
         
         root@test-instance:~# apt update && apt -y install postfix libsasl2-modules
         

###  CentOS 
         
         root@test-instance:~# yum install postfix cyrus-sasl-plain cyrus-sasl-md5 -y
         

  4. When prompted, select the `Local Only` configuration and accept the default choices for domain names.

  5. Modify the Postfix configuration options. Postfix configuration options are set in the `main.cf` file. Open the file with the text editor of your choice.
         
         root@test-instance:~# vi /etc/postfix/main.cf
         

  6. If they exist, comment out the following lines.
         
         # default_transport = error
         # relay_transport = error
         

  7. Add the Mailgun SMTP service by adding the following line to the end of the file.
         
         relayhost = [smtp.mailgun.org]:2525
         

**Note:** You must use port `2525` because port `25` isn't allowed on Compute Engine.
  8. To enforce SSL/TLS support and configure SMTP authentication for these requests, add the following lines to the end of the file. A simple access and security layer (SASL) module handles authentication in the Postfix configuration.
         
         smtp_tls_security_level = encrypt
         smtp_sasl_auth_enable = yes
         smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
         smtp_sasl_security_options = noanonymous
         

  9. Save your changes and close the file.

  10. Generate the SASL password map.

     1. Create a new password file that is ready for standard input.
            
            root@test-instance:~# cat > /etc/postfix/sasl_passwd << EOF
            

     2. At the prompt, enter the service details, replacing `YOUR_SMTP_LOGIN` and `YOUR_SMTP_PASSWORD` with your credentials. See the [Mailgun help](https://help.mailgun.com/hc/en-us/articles/203380100-Where-Can-I-Find-My-API-Key-and-SMTP-Credentials) for instructions on how to view or change your per-domain credentials.
            
            > [smtp.mailgun.org]:2525 YOUR_SMTP_LOGIN:YOUR_SMTP_PASSWORD
            

     3. Close and save the file by typing the delimiter, `EOF`.
            
            > EOF
            

  11. Use the `postmap` utility to generate a `.db` file.
         
         root@test-instance:~# postmap /etc/postfix/sasl_passwd
         
         
         root@test-instance:~# ls -l /etc/postfix/sasl_passwd*
         
         -rw------- 1 root root    68 Jun  1 10:50 /etc/postfix/sasl_passwd
         -rw------- 1 root root 12288 Jun  1 10:51 /etc/postfix/sasl_passwd.db
         

  12. Next, remove the file that contains your credentials because it is no longer needed.
         
         root@test-instance:~# rm /etc/postfix/sasl_passwd
         

  13. Set the permissions on your `.db` file.
         
         root@test-instance:~# chmod 600 /etc/postfix/sasl_passwd.db
         
         
         root@test-instance:~# ls -la /etc/postfix/sasl_passwd.db
         
         -rw------- 1 root root 12288 Aug 31 18:51 /etc/postfix/sasl_passwd.db
         

  14. Finally, reload your configuration to load the modified parameters.

###  Debian 
         
         root@test-wheezy:~# /etc/init.d/postfix restart
         

###  CentOS 
         
         [root@test-centos ~]# postfix reload
         

  15. Test your configuration. Install the `mailx` or `mailutils` package and test your configuration.

###  Debian 
         
         root@test-wheezy:~# apt -y install mailutils
         

###  CentOS 
         
         [root@test-centos ~]# yum install mailx -y
         

Send a test message.
         
         root@test-instance:~# echo 'Test passed.' | mail -s 'Test-Email' EMAIL@EXAMPLE.COM
         

Look in your systems logs for a status line containing `status` and the successful server response code `(250)`.

###  Debian 
         
         root@test-wheezy:~# tail -n 5 /var/log/syslog
         

###  CentOS 
         
         [root@test-centos ~]# tail -n 5 /var/log/maillog
         




For detailed examples and information about other topics including tracking and routing messages, read the [Mailgun documentation](https://documentation.mailgun.com).

Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
