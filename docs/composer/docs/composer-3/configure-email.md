---
url: https://docs.cloud.google.com/composer/docs/composer-3/configure-email/
title: Configure email notifications \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:00.302840+00:00
---

# Configure email notifications  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/configure-email/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Configure email notifications Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/configure-email "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/configure-email "View this page for Managed Airflow \(Legacy Gen 1\)")

This page explains how to configure SMTP services for your Managed Airflow environment.

## Before you begin

  * If your Managed Airflow environment is [configured for Private IP](https://docs.cloud.google.com/composer/docs/composer-3/configure-private-ip), make sure that it has connectivity to the API endpoint for your external email service (such as `https://api.sendgrid.com`, or your preferred SMTP server).

  * Airflow components in Public IP environments establish outbound connections, including sending email messages, from automatically allocated public IP addresses and ports. If you want your Public IP environments to send email from predetermined IP addresses and ports, you can do so through [connecting a VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network) to your environment and [switching it to Private IP](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#about-networking-type). For more information about networking in Managed Airflow (Gen 3), see [Change environment networking type](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#about-networking-type).

  * The Airflow scheduler in Managed Airflow (Gen 3) supports only the following custom email backends:

    * airflow.providers.sendgrid.utils.emailer.send_email
    * airflow.utils.email.send_email_smtp

If you configure a different custom email backend, this configuration won't be propagated to the scheduler. As a result, sending email directly from the scheduler would lead to the scheduler becoming unresponsive and repeatedly failing.

Airflow workers and DAG processors support other custom backends, so you can send email from these components. One common case when email is sent directly from the scheduler is email alerts about DAG failures. As a workaround, you can send DAG failure alerts [through a registered callback](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/callbacks.html) instead. They will be sent from the DAG processor. You can also use other custom backends with Airflow operators that send email. In this case, email will be sent from an Airflow worker that processes the task.




## Configure SendGrid email services

To receive notifications, configure your environment variables to send email through the SendGrid email service.

### Sign up with SendGrid

If you haven't already, sign up with SendGrid in Google Cloud console, click Manage On Provider to go to the SendGrid domain, and click Settings to retrieve your username and to create an API key. As a Google Cloud developer, you can start with 12,000 free emails per month.

[Go to SendGrid Email API](https://console.cloud.google.com/marketplace/details/sendgrid-app/sendgrid-email)

### Configure variables

SendGrid uses the API key and a From email address for sending mail. You can provide this information with one of the following options:

  * (Recommended) Store values in Secret Manager

  * Store values in Airflow

**Caution:** If you use this option, the value for the SendGrid API key is stored in an Airflow connection.



#### Store values in Secret Manager

To store values in Secret Manager:

  1. [Configure Secret Manager](https://docs.cloud.google.com/composer/docs/composer-3/configure-secret-manager) for your environment. Make sure to set up permissions and Airflow configuration options for the secrets backend.

  2. [Override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the following Airflow configuration options:

Section | Key | Value  
---|---|---  
`email` | `email_conn_id` | `sendgrid_default`  
`email` | `email_backend` | `airflow.providers.sendgrid.utils.emailer.send_email`  
  3. Create a secret for the SendGrid connection named `airflow-connections-sendgrid_default`. Set the secret's value to the connection URI. For example:
         
         sendgrid://<username>:<sendgrid_api_key>@smtp.sendgrid.net:587
         

For more information about storing connections in Secret Manager, see [Manage Airflow connections](https://docs.cloud.google.com/composer/docs/composer-3/manage-airflow-connections).

  4. Configure the email address for SendGrid. It's not possible to set up the email address through a secret. Instead, [override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the following Airflow configuration option:

Section | Key | Value  
---|---|---  
`email` | `from_email` | The From email address, such as `noreply@example.com`.  



#### Store values in Airflow

  1. [Override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the following Airflow configuration options:

Section | Key | Value  
---|---|---  
`email` | `email_conn_id` | `sendgrid_default`  
`email` | `email_backend` | `airflow.providers.sendgrid.utils.emailer.send_email`  
  2. In Airflow, [configure the connection](https://docs.cloud.google.com/composer/docs/composer-3/manage-airflow-connections) named `sendgrid_default`. Specify the Sendgrid API key in the connection URI. For example:
         
         gcloud composer environments run ENVIRONMENT_NAME \
           --location LOCATION \
           connections add -- \
           --conn-uri "sendgrid://USERNAME:SENDGRID_API_KEY@smtp.sendgrid.net:587" \
           sendgrid_default
         

Replace the following:

     * `ENVIRONMENT_NAME`: the name of your environment.
     * `LOCATION`: the region where the environment is located.
     * `USERNAME`: the SendGrid username.
     * `SENDGRID_API_KEY`: the SendGrid API key.
  3. Configure the email address for SendGrid. It's not possible to set up the email address through a secret. Instead, [override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the following Airflow configuration option:

Section | Key | Value  
---|---|---  
`email` | `from_email` | The From email address, such as `noreply@example.com`.  



### Test your SendGrid configuration

To test SendGrid configuration:

  1. Create a test DAG that uses the `EmailOperator`. For example:


    
    
    import datetime
    
    import airflow
    from airflow.operators.email import EmailOperator
    
    
    with airflow.DAG(
        "composer_sample_sendgrid",
        start_date=datetime.datetime(2022, 1, 1),
    ) as dag:
        task_email = EmailOperator(
            task_id="send-email",
            conn_id="sendgrid_default",
            # You can specify more than one recipient with a list.
            to="user@example.com",
            subject="EmailOperator test for SendGrid",
            html_content="This is a test message sent through SendGrid.",
            dag=dag,
        )
    

  1. [Upload the DAG](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags#add) to your environment and check that the task succeeds.
  2. Sign in to SendGrid in with your SendGrid credentials.
  3. In the SendGrid UI, go to Activity page.
  4. Search the list for the email. You should see that SendGrid processed and delivered the email.
  5. If the email is not processed and delivered:

     * Check your SendGrid configuration.
     * Verify that you enabled the Secret Manager backend. Make sure that you granted extra permissions and set overrides for Airflow configuration options.
     * Check the spam filter in your email client.



## Configure third-party SMTP services

To send email through a third-party SMTP service, [override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the `email_backend` Airflow configuration option and configure other SMTP-related parameters.

**Note:** Using a third-party SMTP service requires setting an SMTP password. Managed Airflow does not support configuring the `smtp_password` because the value is stored in plain text in `airflow.cfg` and considered non-secure. See Configuring an SMTP password to learn about setting an SMTP password in a more secure way.

To configure a third-party SMTP service, [override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the following Airflow configuration options:

Section | Key | Value  
---|---|---  
`email` | `email_backend` | `airflow.utils.email.send_email_smtp`  
`smtp` | `smtp_host` | The hostname for the SMTP server.  
`smtp` | `smtp_user` | The username on the SMTP server.  
`smtp` | `smtp_port` | The port for the SMTP server. Port 25 is not available. You can use other ports, such as standard SMTP ports 465 and 587.  
`smtp` | `smtp_password` | Setting a password via `smtp_password` is not supported. To set an SMTP password, follow instructions provided in Configuring an SMTP password.  
`smtp` | `smtp_mail_from` | The From email address, such as `noreply-composer@`.  
`smtp` | `smtp_starttls` | For enhanced security, set to `True`.  
`smtp` | `smtp_ssl` | For enhanced security, set to `True`.  
  
### Configure an SMTP password for a third-party SMTP service

Keeping an SMTP password in plain text in Airflow configuration file is a bad security practice. That's why Managed Airflow does not support this method. Instead, you can use two other methods for configuring an SMTP password.

#### Using a command to retrieve the SMTP password

You can use a configuration override to specify a command that obtains the SMTP password. When communicating with your SMTP service, Airflow uses this command to get the value of the password. Specify a single command, without bash operators such as pipes and redirects.

To use this method, [override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the following Airflow configuration option:

Section | Key | Value  
---|---|---  
`smtp` | `smtp_password_cmd` | Specify a command that returns the SMTP password.  
  
#### Using a secret stored in Secret Manager to retrieve an SMTP password

You can [configure Secret Manager](https://docs.cloud.google.com/composer/docs/composer-3/configure-secret-manager) as your Airflow secrets backend.

**Note:** If the `smtp_ssl` Airflow configuration option is set to `True` for your environment, then disable this override if you get the `SSL_WRONG_VERSION_NUMBER` error.

Once you configure Secret Manager for your Composer environment, you can store an SMTP password in Secret Manager:

  1. Create a new secret:
         
         echo -n "SMTP_PASSWORD" | gcloud beta secrets create \
           airflow-config-smtp-password \
           --data-file=- \
           --replication-policy=automatic
         

Replace `SMTP_PASSWORD` with your SMTP password.

  2. Configure Airflow to obtain the SMTP password from Secret Manager. To do so, [override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the following Airflow configuration option. Airflow automatically prepends the `airflow-config-` prefix to the value you specify for `smtp_password_secret` when it retrieves the `airflow-config-smtp-password` secret from Secret Manager.

Section | Key | Value  
---|---|---  
`smtp` | `smtp_password_secret` | `smtp-password`  



## What's next

  * [Override Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations)
  * [Set environment variables](https://docs.cloud.google.com/composer/docs/composer-3/set-environment-variables)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
