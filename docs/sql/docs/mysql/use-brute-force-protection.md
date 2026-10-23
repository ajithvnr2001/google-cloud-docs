---
url: https://docs.cloud.google.com/sql/docs/mysql/use-brute-force-protection/
title: Use Cloud SQL brute-force protection \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:18.910774+00:00
---

# Use Cloud SQL brute-force protection  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/use-brute-force-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use Cloud SQL brute-force protection Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/use-brute-force-protection "View this page for the PostgreSQL database engine") | SQL Server

Brute-force protection is a built-in security feature that protects your instances from brute-force access attempts by preventing unauthorized access to your Cloud SQL resources. Brute-force access attempts occur when bad actors systematically try different username and password combinations to automate repeated login attempts and gain access to your database.

Cloud SQL provides the following options to protect your databases against brute-force access attempts:

  * **Brute-force access detection** : Cloud SQL continuously monitors failed login attempts for each instance and detects the first successful login. If the number of consecutive login attempts exceeds the Cloud SQL defined threshold, Cloud SQL generates a warning message in the instance logs. This log message identifies the brute-force access attempt, including the associated IP address and username.

Brute-force access detection is available for all Cloud SQL editions.

  * **Brute-force access protection** : When Cloud SQL detects a brute-force access attempt, Cloud SQL automatically slows down login attempts by adding a delay to the login response and throttling it in real-time. If Cloud SQL identifies a connection as a brute-force access attempt and that connection leads to a successful login, then Cloud SQL throttles it and generates a log event to identify this successful login. This log event identifies the brute-force access attempt, along with the associated IP address and username.

Brute-force access protection is available for Cloud SQL Enterprise Plus edition only.




By providing brute-force access detection and protection for your instances, Cloud SQL helps identify the source of and mitigate the risks caused by these brute-force access attempts. Use the IP addresses and usernames identified in these brute-force access attempts to secure your instance and protect it from future brute-force access attempts. To identify brute-force attempts for your instance, see View logs for brute-force attempts.

## View logs for brute-force access attempts

When Cloud SQL detects a brute-force access attempt, it logs an event in your [instance logs](https://docs.cloud.google.com/sql/docs/mysql/logging#view_logs), with a text that states `an anomaly was found`. Cloud SQL logs the following detailed events:

Event | Description  
---|---  
**Detection of brute-force access attempt** | Failed login attempt into the account `user` from IP `IP`. An anomaly was found, repeated failed login attempts from this IP.  
**Automatic throttling to mitigate brute-force access attempt** ([Enterprise Plus Edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) only) | Failed login attempt into the account `user` from IP `IP`. An anomaly was found, repeated failed login attempts from this IP. Cloud SQL throttled the response to mitigate a potential brute-force attempt.  
**Detection of first successful login after repeated login failures** | An anomaly was found, successful login into the account `user` from IP `IP` after repeated failed login attempts. It's recommended to change the user password if this activity is unexpected.  
**Automatic throttling of first successful login after repeated login failures** (Enterprise Plus Edition only) | An anomaly was found, successful login into the account `user` from IP `IP` after repeated failed login attempts. Cloud SQL throttled the response to mitigate a potential brute-force attempt. Change the user password if this activity is unexpected.  
  
To see details about these brute-force attempts, [view your instance's logs ](https://docs.cloud.google.com/sql/docs/mysql/logging#view_logs) and look for `An anomaly was found` in the text for each log.

### Set up a log-based alert policy

You can set up a log-based alert policy to be notified when a brute-force access attempt is detected or throttled for your Cloud SQL instances. For more information on how to set up this alert, see [Configure log-based alerting policy by using the Logs explorer](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition).

For example, you can use the following query in the alert policy to identify successful brute-force access attempt logs:
    
    
    resource.type="cloudsql_database"
    textPayload =~ "An anomaly was found, successful login into the account"
    

## Secure your instance

You should consider securing your instance if brute-force access attempts are identified. To view potential brute-force access attempts, see View logs for brute-force access attempts.

If Cloud SQL identifies a brute-force access attempt to your instance, do the following:

  * If Cloud SQL detects a brute-force access attempt, but the login failed, then remove the identified IP addresses from your authorized networks to prevent future login attempts from these IPs. To do so, use narrow IP ranges in the [authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks) for your instance, or remove the IP address from your authorized networks list.
  * If Cloud SQL detects brute-force access attempt and a successful login resulted from the identified IP address and username, then [change the password for the user account](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#change-pwd) and remove the IP from your [authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks) list.



Additionally, you can also use the [Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) or the [Cloud SQL language connectors](https://docs.cloud.google.com/sql/docs/mysql/language-connectors) to connect to your instance instead of authorized networks. The Auth Proxy and Cloud SQL Language Connectors use [Identity and Access Management authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication) to manage connections to your instance, which provides a more secure connection and doesn't require you to add specific IP addresses to your instance authorized networks list.

To further protect your Cloud SQL instances, use [private IP](https://docs.cloud.google.com/sql/docs/mysql/private-ip) instead of [public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip), and use [IAM-based database authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication#iam-db-auth) instead of username and password based authentication.

## Monitor brute-force access attempts

To monitor brute-force access attempts, Cloud SQL counts the number of occurrences of each type of connection event to your instance using the `/database/network/connection_attempt_count` metric. This metric uses the following fields to determine if a connection is a brute-force access attempt:

  * `login_status`: tracks if the connection led to a successful login.
  * `anomaly_detected`: tracks if the connection is a brute-force access attempt based on whether the connection exceeded the login attempt threshold set by Cloud SQL.
  * `anomalous_connection_throttled`: tracks if brute-force access attempt connection is throttled.



You can [monitor](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance) this metric to identify the count of each type of connection event. The following table shows the connection events tracked by the metric and their corresponding field values:

**Event** | **Description**  
---|---  
Successful login | A successful login to your instance with no brute-force access attempt detected. Tracked field values:  

    
    
              login_status: succeeded
              anomaly_detected: none
              anomalous_connection_throttled: false
              
  
Failed login | A failed login to your instance with no brute-force access attempt detected. Tracked field values:  

    
    
              login_status: failed
              anomaly_detected: none
              anomalous_connection_throttled: false
              
  
Brute-force login attempt detected (not throttled) | A failed login attempt that is identified as a brute-force access attempt as it exceeds the login attempt threshold set by Cloud SQL. The connection wasn't throttled. Tracked field values:  

    
    
              login_status: failed
              anomaly_detected: brute-force login
              anomalous_connection_throttled: false
              
  
Brute-force login attempt detected and throttled | A failed login attempt that is identified as a brute-force access attempt as it exceeds the login attempt threshold set by Cloud SQL and is throttled to prevent login. Tracked field values:  

    
    
              login_status: failed
              anomaly_detected: brute-force login
              anomalous_connection_throttled: true
              
  
Successful login after brute-force access attempt detected (not throttled) | A successful login to your instance after the connection was identified as a brute-force access attempt. The connection wasn't throttled. Tracked field values:  

    
    
              login_status: succeeded
              anomaly_detected: brute-force login
              anomalous_connection_throttled: false
              
  
Successful login after brute-force access attempt detected and throttled | A successful login to your instance after the connection was identified as a brute-force access attempt and throttled. Tracked field values:  

    
    
              login_status: succeeded
              anomaly_detected: brute-force login
              anomalous_connection_throttled: true
              
  
## Limitations

  * Brute-force protection requires a minimum maintenance version of `MYSQL_$version.R20250531.01_23` For more information, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance). 
  * Brute-force protection is only available for MySQL version 5.7 and later. 



## What's next

  * [View instance logs](https://docs.cloud.google.com/sql/docs/mysql/logging#view_logs)
  * [Monitor your Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
