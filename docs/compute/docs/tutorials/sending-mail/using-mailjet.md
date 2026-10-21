---
url: https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/using-mailjet/
title: Sending email with Mailjet \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:19:44.213807+00:00
---

# Sending email with Mailjet  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/using-mailjet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Sending email with Mailjet Stay organized with collections  Save and categorize content based on your preferences. 

[Mailjet](https://www.mailjet.com/integration/google/?p=google) is a third-party global email service that offers Compute Engine users a free tier with 6,000 emails each month. In addition, Mailjet also offers:

  * An API, user interface, and SMTP relay to send transactional and marketing email.
  * European data privacy compliance.
  * Email and deliverability features, such as customizable priority settings and automated throttle management.
  * API resource library in Go, PHP, Nodejs, Java, Python, and Ruby to manage sub-accounts, authentication, contacts, campaigns, custom payloads, statistics, real time events, and parsing through the [Event API](https://dev.mailjet.com/email/guides/#event-api-real-time-notifications).
  * Integrated [MJML](http://www.mjml.io/) framework to create responsive HTML email templates.
  * 24/7 follow-the-sun support in 4+ languages.
  * Ability to send email messages from domains other than `gmail.com`.



This document describes how to configure your VM instance to send mail through Mailjet using the following methods:

  * Through an [SMTP](https://wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) relay with: 
    * [Postfix](http://www.postfix.org/)
    * [Nodemailer](https://nodemailer.com/about/) on Node.js
  * Directly through the Mailjet API using Java



For extensive documentation of other email solutions, including examples of integration with most common SMTP servers, libraries, and frameworks, see [Mailjet's documentation](https://dev.mailjet.com/).

## Before you begin

  1. Create a new Mailjet account on Mailjet's [Google partner page](https://www.mailjet.com/google/?p=google)*. When signing up, provide the domain and email address from which you want to send email messages.

  2. [Get your Mailjet SMTP account credentials](https://app.mailjet.com/account/apikeys).

  3. Make sure the email address you want to send emails from has been [validated](https://documentation.mailjet.com/hc/en-us/articles/360042759253-How-to-add-a-sender-address).

  4. [Set up a firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) to allow TCP traffic on port 2525.




_* Google is compensated for customers who sign up for a non-free account._

## Configuring Mailjet as an SMTP relay

Configuring Mailjet as a mail relay lets you forward email messages to Mailjet for remote delivery.

### Using Postfix

  1. Connect to your VM using SSH, replacing `instance-name` with the name of the instance you want to send email messages from:
         
         gcloud compute ssh instance-name

  2. On the VM, install the Postfix Mail Transport Agent. When prompted, accept the default choices for domain names but select the `Local Only` configuration.

###  Debian 
         
         sudo apt update && sudo apt -y install postfix libsasl2-modules
         

###  CentOS 
         
         sudo yum install postfix cyrus-sasl-plain cyrus-sasl-md5 -y
         

  3. Modify the Postfix configuration options. Postfix configuration options are set in the `main.cf` file. Open the file with the text editor of your choice:
         
         sudo vi /etc/postfix/main.cf
         

  4. Update the file:

     1. Comment out the following lines:
            
            # default_transport = error
            # relay_transport = error
            

     2. Add the following lines to the end of the file:
            
            relayhost = in-v3.mailjet.com:2525
            smtp_tls_security_level = encrypt
            smtp_sasl_auth_enable = yes
            smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
            smtp_sasl_security_options = noanonymous
            

These lines enforce SSL/TLS support and configure SMTP authentication for these requests. A simple access and security layer (SASL) module handles authentication in the Postfix configuration.

**Note:** You must use port 2525 because port 25 is not allowed on Compute Engine.
     3. Save your changes and close the file.

  5. Create the SASL password map with the text editor of your choice:
         
         sudo vi /etc/postfix/sasl_passwd
         

  6. To the `sasl_passwd` file, add the following lines to provide the credentials for Mailjet:
         
         in-v3.mailjet.com:2525 YOUR_API_KEY:YOUR_SECRET_KEY
         

  7. Use the `postmap` utility to generate a `.db` file:
         
         sudo postmap /etc/postfix/sasl_passwd
         sudo ls -l /etc/postfix/sasl_passwd*
         

You should receive the following response:
         
         -rw------- 1 root root    68 Jun  1 10:50 /etc/postfix/sasl_passwd
         -rw------- 1 root root 12288 Jun  1 10:51 /etc/postfix/sasl_passwd.db
         

  8. Next, remove the file that contains your credentials because it is no longer needed:
         
         sudo rm /etc/postfix/sasl_passwd
         

  9. Set the permissions on your `.db` file:
         
         sudo chmod 600 /etc/postfix/sasl_passwd.db
         sudo ls -la /etc/postfix/sasl_passwd.db
         

  10. Finally, reload your configuration to load the modified parameters:

###  Debian 
         
         sudo /etc/init.d/postfix restart
         

###  CentOS 
         
         sudo postfix reload
         

  11. Test your configuration. Install the `mailx` or `mailutils` package and test your configuration.

###  Debian 
         
         sudo apt -y install mailutils
         

###  CentOS 
         
         sudo yum install mailx -y
         

Send a test message:
         
         echo 'Test passed.' | mail -s 'Test-Email' -aFrom:from-email destination-email

Replace the following:

     * `from-email`: An email address that has been [validated](https://documentation.mailjet.com/hc/en-us/articles/360042759253-How-to-add-a-sender-address).
     * `destination-email`: The address to send the email message to.

Look in your system's logs for a status line containing `status` and the successful server response code `(250)`:

###  Debian 
    
    sudo tail -n 5 /var/log/syslog
    

###  CentOS 
    
    sudo tail -n 5 /var/log/maillog
    




If you run into issues setting up Postfix with Mailjet, see the [Mailjet Postfix setup instructions](https://dev.mailjet.com/smtp-relay/configuration/#postfix-installation).

### Using Nodemailer

The following instructions describe how to use Mailjet with Node.js on Debian Wheezy.

Debian

  1. Connect to your instance using SSH: 
         
         gcloud compute ssh instance-name

  2. Update your package repositories: 
         
         user@test-wheezy:~# sudo apt update

  3. Install Node.js dependencies: 
         
         user@test-wheezy:~# sudo apt -y install git-core curl build-essential openssl libssl-dev

  4. Clone the Node.js repo from github: 
         
         user@test-wheezy:~# git clone https://github.com/nodejs/node

  5. Change the directory to the Node.js source tree: 
         
         user@test-wheezy:~# cd node

  6. Configure node software for this OS and virtual machine: 
         
         user@test-wheezy:~# ./configure

  7. Build Node.js, npm, and related objects: 
         
         user@test-wheezy:~# sudo make

This can take a few minutes to complete.

  8. Install Node.js, npm, and other software in the default location: 
         
         user@test-wheezy:~# sudo make install

  9. Install the mailer package: 
         
         user@test-wheezy:~# npm install nodemailer nodemailer-smtp-transport

  10. In the `node` directory, create a new file named `sendmail.js` that contains the following JavaScript: 
         
         const mailer = require('nodemailer');
         async function mailjet() {
           const transport = mailer.createTransport({
             host: 'in.mailjet.com',
             port: 2525,
             auth: {
               user: process.env.MAILJET_API_KEY || '<your-mailjet-api-key>',
               pass: process.env.MAILJET_API_SECRET || '<your-mailjet-api-secret>',
             },
           });
         
           const json = await transport.sendMail({
             from: 'ANOTHER_EMAIL@ANOTHER_EXAMPLE.COM', // From address
             to: 'EMAIL@EXAMPLE.COM', // To address
             subject: 'test email from Node.js on Google Cloud Platform', // Subject
             text: 'Hello!\n\nThis a test email from Node.js.', // Content
           });
           console.log(json);
         }
         mailjet();

  11. Run the program to send an email message through Mailjet: 
         
         user@test-wheezy:~# node sendmail.js


CentOS

  1. Connect to your instance using SSH: 
         
         gcloud compute ssh instance-name

  2. Update package repositories: 
         
         user@test-centos:~# sudo yum update -y

  3. Install Node.js dependencies: 
         
         user@test-centos:~# sudo yum install git-core curl openssl openssl-dev -y
         ...
         user@test-centos:~# sudo yum groupinstall "Development Tools" -y
         ...

  4. Clone Node.js repository from github: 
         
         user@test-centos:~# git clone https://github.com/nodejs/node

  5. Change directory to the Node.js source tree: 
         
         user@test-centos:~# cd node

  6. Configure node software for this OS and virtual machine: 
         
         user@test-centos:~# ./configure

  7. Build Node.js, npm, and related objects: 
         
         user@test-centos:~# sudo make

This can take a few minutes to complete.

  8. Install Node.js, npm, and other software in the default location: 
         
         user@test-centos:~# sudo make install

  9. Install the mailer package: 
         
         user@test-centos:~# npm install npm install nodemailer nodemailer-smtp-transport

  10. In the `node` directory, create a new file named `sendmail.js` that contains the following JavaScript: 
         
         const mailer = require('nodemailer');
         async function mailjet() {
           const transport = mailer.createTransport({
             host: 'in.mailjet.com',
             port: 2525,
             auth: {
               user: process.env.MAILJET_API_KEY || '<your-mailjet-api-key>',
               pass: process.env.MAILJET_API_SECRET || '<your-mailjet-api-secret>',
             },
           });
         
           const json = await transport.sendMail({
             from: 'ANOTHER_EMAIL@ANOTHER_EXAMPLE.COM', // From address
             to: 'EMAIL@EXAMPLE.COM', // To address
             subject: 'test email from Node.js on Google Cloud Platform', // Subject
             text: 'Hello!\n\nThis a test email from Node.js.', // Content
           });
           console.log(json);
         }
         mailjet();

  11. Run the program to send an email message through Mailjet: 
         
         user@test-centos:~# node sendmail.js




## Sending mail through the Mailjet API with Java

For more examples of using the Mailjet API, see the [official Mailjet documentation](https://app.mailjet.com/docs/code).

Debian

  1. Connect to your instance using SSH: 
         
         gcloud compute ssh instance-name

  2. Update your package repositories and install the required packages: 
         
         user@test-instance:~# sudo apt update && sudo apt install git-core openjdk-8-jdk maven

  3. Clone the Java repo from GitHub: 
         
         user@test-instance:~# git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git

  4. Go to the main source code for the example, located at: 
         
         /root/java-docs-samples/compute/mailjet/src/main/java/com/example/compute/mailjet

  5. Configure your Mailjet settings. Refer to the Mailjet [Authentication](https://dev.mailjet.com/email/guides/#authentication) documentation on how to replace the following variables: 

     * `your-mailjet-api-key`: An API key for your Mailjet account.
     * `your-mailjet-secret-key`: The corresponding secret key for your Mailjet account.
    
    public class MailjetSender {
    
      public static void main(String[] args) throws MailjetException {
        final String mailjetApiKey = "YOUR-MAILJET-API-KEY";
        final String mailjetSecretKey = "YOUR-MAILJET-SECRET-KEY";
        ClientOptions options =
            ClientOptions.builder().apiKey(mailjetApiKey).apiSecretKey(mailjetSecretKey).build();
        MailjetClient client = new MailjetClient(options);
    
        MailjetSender sender = new MailjetSender();
        sender.sendMailjet(args[0], args[1], client);
      }
    
      public MailjetResponse sendMailjet(String recipient, String sender, MailjetClient client)
          throws MailjetException {
        MailjetRequest email =
            new MailjetRequest(Emailv31.resource)
                .property(
                    Emailv31.MESSAGES,
                    new JSONArray()
                        .put(
                            new JSONObject()
                                .put(
                                    Emailv31.Message.FROM,
                                    new JSONObject().put("Email", sender).put("Name", "pandora"))
                                .put(
                                    Emailv31.Message.TO,
                                    new JSONArray().put(new JSONObject().put("Email", recipient)))
                                .put(Emailv31.Message.SUBJECT, "Your email flight plan!")
                                .put(
                                    Emailv31.Message.TEXTPART,
                                    "Dear passenger, welcome to Mailjet!" 
                                    + "May the delivery force be with you!")
                                .put(
                                    Emailv31.Message.HTMLPART,
                                    "<h3>Dear passenger, welcome to Mailjet!</h3>"
                                    + "<br />May the delivery force be with you!")));
    
        try {
          // trigger the API call
          MailjetResponse response = client.post(email);
          // Read the response data and status
          System.out.println(response.getStatus());
          System.out.println(response.getData());
          return response;
        } catch (MailjetException e) {
          System.out.println("Mailjet Exception: " + e);
          return null;
        }
      }
    }

  6. From the `mailjet` directory, use Maven to package the class as a JAR file: 
         
         user@test-instance:~# mvn clean package

  7. Ensure that you are using OpenJDK 8: 
         
         user@test-instance:~# sudo update-alternatives --config java

  8. To send an email: from the target directory, run the JAR file with your recipient and sender email addresses as arguments: 
         
         user@test-instance:~# java -jar
                 compute-mailjet-1.0-SNAPSHOT-jar-with-dependencies.jar
                 recipient-email sender-email


CentOS

  1. Connect to your instance using SSH: 
         
         gcloud compute ssh instance-name

  2. Update your package repositories and install the required packages: 
         
         user@test-centos:~# sudo yum update && sudo yum install git-core openjdk-8-jdk maven

  3. Clone the Java repo from GitHub: 
         
         user@test-centos:~# git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git

  4. Go to the main source code for the example, located at: 
         
         /root/java-docs-samples/compute/mailjet/src/main/java/com/example/compute/mailjet

  5. Configure your Mailjet settings. For information about how to replace the following variables, refer to the Mailjet [Authentication](https://dev.mailjet.com/email/guides/#authentication) documentation: 

     * `your-mailjet-api-key`: An API key for your Mailjet account.
     * `your-mailjet-secret-key`: The corresponding secret key for your Mailjet account.
    
    public class MailjetSender {
    
      public static void main(String[] args) throws MailjetException {
        final String mailjetApiKey = "YOUR-MAILJET-API-KEY";
        final String mailjetSecretKey = "YOUR-MAILJET-SECRET-KEY";
        ClientOptions options =
            ClientOptions.builder().apiKey(mailjetApiKey).apiSecretKey(mailjetSecretKey).build();
        MailjetClient client = new MailjetClient(options);
    
        MailjetSender sender = new MailjetSender();
        sender.sendMailjet(args[0], args[1], client);
      }
    
      public MailjetResponse sendMailjet(String recipient, String sender, MailjetClient client)
          throws MailjetException {
        MailjetRequest email =
            new MailjetRequest(Emailv31.resource)
                .property(
                    Emailv31.MESSAGES,
                    new JSONArray()
                        .put(
                            new JSONObject()
                                .put(
                                    Emailv31.Message.FROM,
                                    new JSONObject().put("Email", sender).put("Name", "pandora"))
                                .put(
                                    Emailv31.Message.TO,
                                    new JSONArray().put(new JSONObject().put("Email", recipient)))
                                .put(Emailv31.Message.SUBJECT, "Your email flight plan!")
                                .put(
                                    Emailv31.Message.TEXTPART,
                                    "Dear passenger, welcome to Mailjet!" 
                                    + "May the delivery force be with you!")
                                .put(
                                    Emailv31.Message.HTMLPART,
                                    "<h3>Dear passenger, welcome to Mailjet!</h3>"
                                    + "<br />May the delivery force be with you!")));
    
        try {
          // trigger the API call
          MailjetResponse response = client.post(email);
          // Read the response data and status
          System.out.println(response.getStatus());
          System.out.println(response.getData());
          return response;
        } catch (MailjetException e) {
          System.out.println("Mailjet Exception: " + e);
          return null;
        }
      }
    }

  6. From the `mailjet` directory, use Maven to package the class as a JAR file: 
         
         user@test-centos:~# mvn clean package

  7. Ensure that you are using OpenJDK 8: 
         
         user@test-centos:~# sudo alternatives --config java

  8. To send an email, from the target directory, run the JAR file with your recipient and sender email addresses as arguments: 
         
         user@test-centos:~# java -jar
                 compute-mailjet-1.0-SNAPSHOT-jar-with-dependencies.jar
                 recipient-email sender-email




## Mailjet SMTP settings

Here is a quick reference to Mailjet-specific SMTP settings that are used to configure clients:

  * **Host: in-v3.mailjet.com**
  * **Port: 2525**



## What's next

Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
