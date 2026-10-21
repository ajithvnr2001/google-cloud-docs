---
url: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-monitor-ca-expiry/
title: Monitor expiring Certificate Authorities \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:06:28.264905+00:00
---

# Monitor expiring Certificate Authorities  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/samples/privateca-monitor-ca-expiry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Samples ](https://docs.cloud.google.com/certificate-authority-service/docs/samples)



#  Monitor expiring Certificate Authorities Stay organized with collections  Save and categorize content based on your preferences. 

Create a monitoring policy that notifies 30 days before a managed CA expires.

## Code sample

### Java

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.monitoring.v3.[AlertPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.AlertPolicyServiceClient.html);
    import com.google.cloud.monitoring.v3.[NotificationChannelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.NotificationChannelServiceClient.html);
    import com.google.monitoring.v3.[AlertPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.html);
    import com.google.monitoring.v3.[AlertPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.html).[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.html);
    import com.google.monitoring.v3.[AlertPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.html).[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.html).[MonitoringQueryLanguageCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.MonitoringQueryLanguageCondition.html);
    import com.google.monitoring.v3.[AlertPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.html).[ConditionCombinerType](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.ConditionCombinerType.html);
    import com.google.monitoring.v3.[NotificationChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.NotificationChannel.html);
    import com.google.monitoring.v3.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ProjectName.html);
    import java.io.IOException;
    
    public class MonitorCertificateAuthority {
    
      public static final String POLICY_NAME = "policy-name";
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "your-project-id";
        createCaMonitoringPolicy(project);
      }
    
      // Creates a monitoring policy that notifies you 30 days before a managed CA expires.
      public static String createCaMonitoringPolicy(String project) throws IOException {
        /* Initialize client that will be used to send requests. This client only needs to be created
        once, and can be reused for multiple requests. After completing all of your requests, call
        the `client.close()` method on the client to safely
        clean up any remaining background resources. */
        try ([AlertPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.AlertPolicyServiceClient.html) client = [AlertPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.AlertPolicyServiceClient.html).create();
            [NotificationChannelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.NotificationChannelServiceClient.html) notificationClient =
                [NotificationChannelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.NotificationChannelServiceClient.html).create()) {
    
          /* Query which indicates the resource to monitor and the constraints.
          Here, the alert policy notifies you 30 days before a managed CA expires.
          For more info on creating queries, see: https://cloud.google.com/monitoring/mql/alerts */
          String query =
              "fetch privateca.googleapis.com/CertificateAuthority"
                  + "| metric 'privateca.googleapis.com/ca/cert_chain_expiration'"
                  + "| group_by 5m,"
                  + "[value_cert_chain_expiration_mean: mean(value.cert_chain_expiration)]"
                  + "| every 5m"
                  + "| condition val() < 2.592e+06 's'";
    
          // Create a notification channel.
          [NotificationChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.NotificationChannel.html) notificationChannel =
              [NotificationChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.NotificationChannel.html).newBuilder()
                  .setType("email")
                  .putLabels("email_address", "java-docs-samples-testing@google.com")
                  .build();
          [NotificationChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.NotificationChannel.html) channel =
              notificationClient.createNotificationChannel(
                  [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ProjectName.html).of(project), notificationChannel);
    
          // Set the query and notification channel.
          [AlertPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.html) alertPolicy =
              [AlertPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.html).newBuilder()
                  .setDisplayName(POLICY_NAME)
                  .[addConditions](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Builder.html#com_google_monitoring_v3_AlertPolicy_Builder_addConditions_com_google_monitoring_v3_AlertPolicy_Condition_)(
                      [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.html).newBuilder()
                          .setDisplayName("ca-cert-chain-expiration")
                          .[setConditionMonitoringQueryLanguage](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.Builder.html#com_google_monitoring_v3_AlertPolicy_Condition_Builder_setConditionMonitoringQueryLanguage_com_google_monitoring_v3_AlertPolicy_Condition_MonitoringQueryLanguageCondition_)(
                              [MonitoringQueryLanguageCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Condition.MonitoringQueryLanguageCondition.html).newBuilder().setQuery(query).build())
                          .build())
                  .[setCombiner](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.Builder.html#com_google_monitoring_v3_AlertPolicy_Builder_setCombiner_com_google_monitoring_v3_AlertPolicy_ConditionCombinerType_)([ConditionCombinerType](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.ConditionCombinerType.html).AND)
                  .addNotificationChannels(channel.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.NotificationChannel.html#com_google_monitoring_v3_NotificationChannel_getName__)())
                  .build();
    
          [AlertPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.html) policy = client.createAlertPolicy([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ProjectName.html).of(project), alertPolicy);
    
          System.out.println("Monitoring policy successfully created !" + policy.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.html#com_google_monitoring_v3_AlertPolicy_getName__)());
          return policy.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.AlertPolicy.html#com_google_monitoring_v3_AlertPolicy_getName__)();
        }
      }
    }

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.monitoring_v3 as monitoring_v3
    
    
    def create_ca_monitor_policy(project_id: str) -> None:
        """
        Create a monitoring policy that notifies you 30 days before a managed CA expires.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
        """
    
        alertPolicyServiceClient = monitoring_v3.AlertPolicyServiceClient()
        notificationChannelServiceClient = monitoring_v3.NotificationChannelServiceClient()
    
        # Query which indicates the resource to monitor and the constraints.
        # Here, the alert policy notifies you 30 days before a managed CA expires.
        # For more information on creating queries, see: https://cloud.google.com/monitoring/mql/alerts
        query = (
            "fetch privateca.googleapis.com/CertificateAuthority"
            "| metric 'privateca.googleapis.com/ca/cert_chain_expiration'"
            "| group_by 5m,"
            "[value_cert_chain_expiration_mean: mean(value.cert_chain_expiration)]"
            "| every 5m"
            "| condition val() < 2.592e+06 's'"
        )
    
        # Create a notification channel.
        notification_channel = monitoring_v3.NotificationChannel(
            type_="email",
            labels={"email_address": "python-docs-samples-testing@google.com"},
        )
        channel = notificationChannelServiceClient.create_notification_channel(
            name=notificationChannelServiceClient.common_project_path(project_id),
            notification_channel=notification_channel,
        )
    
        # Set the query and notification channel.
        alert_policy = monitoring_v3.AlertPolicy(
            display_name="policy-name",
            conditions=[
                monitoring_v3.AlertPolicy.Condition(
                    display_name="ca-cert-chain-expiration",
                    condition_monitoring_query_language=monitoring_v3.AlertPolicy.Condition.MonitoringQueryLanguageCondition(
                        query=query,
                    ),
                )
            ],
            combiner=monitoring_v3.AlertPolicy.ConditionCombinerType.AND,
            notification_channels=[channel.name],
        )
    
        policy = alertPolicyServiceClient.create_alert_policy(
            name=notificationChannelServiceClient.common_project_path(project_id),
            alert_policy=alert_policy,
        )
    
        print("Monitoring policy successfully created!", policy.name)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=certificateauthorityservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
