---
url: https://docs.cloud.google.com/chronicle/docs/administration/cli-user-guide/
title: Google SecOps CLI reference \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:15:15.760465+00:00
---

# Google SecOps CLI reference  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/cli-user-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google SecOps CLI reference

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

The Google Security Operations SDK provides a comprehensive command-line interface (CLI) that makes it easy to interact with Google SecOps products from your terminal. The new `secops` CLI replaces the legacy `chronicle_cli` with enhanced functionality and improved user experience.

## Overview

The `secops` CLI provides access to:

  * Search and analyze UDM events
  * Manage feeds, forwarders, and parsers
  * Create and manage detection rules
  * Handle alerts and cases
  * Manage reference lists and data tables
  * Export data to BigQuery and Google Cloud Storage
  * Query Gemini AI for security insights
  * And much more



Google SecOps CLI commands use the following syntax:
    
    
    $ secops COMMAND [SUBCOMMAND] [OPTIONS]

For example, to search for events:
    
    
    $ secops search --query "metadata.event_type = \"NETWORK_CONNECTION\"" --time-window 24

## Before you begin

Before installing the Google SecOps CLI, ensure you have:

  * Python 3.8 or higher installed in your environment. For more information, see [Installing Python](https://docs.cloud.google.com/python/docs/setup#installing_python).
  * A Google SecOps instance with appropriate access permissions.
  * Authentication credentials (service account or Application Default Credentials).



## Installation

Install the SecOps SDK which includes the CLI:
    
    
    pip install secops

Verify the installation:
    
    
    $ secops --help

## Authentication

The CLI supports multiple authentication methods:

### Using Application Default Credentials (Recommended)
    
    
    # Set up ADC with gcloud
    gcloud auth application-default login

### Using Service Account

Place your service account JSON file in a secure location and reference it in commands:
    
    
    $ secops search --service-account "/path/to/service-account.json" --customer-id "your-instance-id" --project-id "your-project-id" --query "metadata.event_type = \"USER_LOGIN\""

## Configuration

Save common settings to avoid repetition in commands:

### Save Configuration
    
    
    # Save instance and authentication settings
    $ secops config set --customer-id "your-instance-id" --project-id "your-project-id" --region "us"
    
    # Save service account path (optional)
    $ secops config set --service-account "/path/to/service-account.json" --customer-id "your-instance-id" --project-id "your-project-id"
    
    # Set default time window
    $ secops config set --time-window 48

### View Configuration
    
    
    $ secops config view

### Clear Configuration
    
    
    $ secops config clear

## Regions

The CLI supports all Google SecOps regions. You can set the region using:

  * The `--region` flag with any command
  * The configuration file using `secops config set --region REGION`



Supported regions include:

  * `US` (default)
  * `EUROPE`
  * `ASIA-SOUTHEAST1`
  * `ASIA-SOUTH1`
  * `AUSTRALIA-SOUTHEAST1`
  * `EUROPE-WEST2`, `EUROPE-WEST3`, `EUROPE-WEST6`, `EUROPE-WEST9`, `EUROPE-WEST12`
  * And more



## Core Commands

### Search Events

Search for UDM events using query syntax:
    
    
    # Search with UDM query
    $ secops search --query "metadata.event_type = \"NETWORK_CONNECTION\"" --time-window 24 --max-events 100
    
    # Search using natural language
    $ secops search --nl-query "show me failed login attempts" --time-window 24
    
    # Export results as CSV
    $ secops search --query "metadata.event_type = \"USER_LOGIN\" AND security_result.action = \"BLOCK\"" \
        --fields "metadata.event_timestamp,principal.user.userid,principal.ip" \
        --time-window 24 --csv

### Entity Information

Get detailed information about IPs, domains, or file hashes:
    
    
    $ secops entity --value "8.8.8.8" --time-window 24
    $ secops entity --value "example.com" --time-window 24
    $ secops entity --value "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" --time-window 24

### Statistics

Run statistical analyses on your data:
    
    
    $ secops stats --query "metadata.event_type = \"NETWORK_CONNECTION\"
    match:
      target.hostname
    outcome:
      \$count = count(metadata.id)
    order:
      \$count desc" --time-window 24

## Feed Management

Manage data ingestion feeds in Google SecOps:

### List Feeds
    
    
    $ secops feed list

### Create Feed
    
    
    # Create an HTTP feed
    $ secops feed create \
        --display-name "My HTTP Feed" \
        --details '{"logType":"projects/your-project-id/locations/us/instances/your-instance-id/logTypes/WINEVTLOG","feedSourceType":"HTTP","httpSettings":{"uri":"https://example.com/feed","sourceType":"FILES"}}'

### Update Feed
    
    
    $ secops feed update --id "feed-123" --display-name "Updated Feed Name"

### Enable/Disable Feed
    
    
    $ secops feed enable --id "feed-123"
    $ secops feed disable --id "feed-123"

### Delete Feed
    
    
    $ secops feed delete --id "feed-123"

## Parser Management

Parsers process and normalize raw log data into UDM format:

### List Parsers
    
    
    $ secops parser list
    $ secops parser list --log-type "WINDOWS"

### Get Parser Details
    
    
    $ secops parser get --log-type "WINDOWS" --id "pa_12345"

### Create Parser
    
    
    # Create from file
    $ secops parser create --log-type "CUSTOM_LOG" --parser-code-file "/path/to/parser.conf"
    
    # Create from string
    $ secops parser create --log-type "CUSTOM_LOG" --parser-code "filter { mutate { add_field => { \"test\" => \"value\" } } }"

### Test Parser

Test a parser against sample logs before deployment:
    
    
    # Test with inline logs
    $ secops parser run \
        --log-type OKTA \
        --parser-code-file "./parser.conf" \
        --log '{"message": "Test log 1"}' \
        --log '{"message": "Test log 2"}'
    
    # Test with logs from file
    $ secops parser run \
        --log-type WINDOWS \
        --parser-code-file "./parser.conf" \
        --logs-file "./sample_logs.txt"

### Activate/Deactivate Parser
    
    
    $ secops parser activate --log-type "WINDOWS" --id "pa_12345"
    $ secops parser deactivate --log-type "WINDOWS" --id "pa_12345"

### Delete Parser
    
    
    $ secops parser delete --log-type "WINDOWS" --id "pa_12345"

## Parser Extension Management

Parser extensions extend existing parsers without replacing them:

### List Extensions
    
    
    $ secops parser-extension list --log-type OKTA

### Create Extension
    
    
    $ secops parser-extension create --log-type OKTA \
        --log /path/to/sample.log \
        --parser-config-file /path/to/parser-config.conf

### Activate Extension
    
    
    $ secops parser-extension activate --log-type OKTA --id "1234567890"

## Forwarder Management

Forwarders are used to ingest logs with specific configurations:

### Create Forwarder
    
    
    # Basic forwarder
    $ secops forwarder create --display-name "my-custom-forwarder"
    
    # With metadata and settings
    $ secops forwarder create --display-name "prod-forwarder" \
        --metadata '{"environment":"prod","team":"security"}' \
        --upload-compression true \
        --http-settings '{"port":80,"host":"example.com"}'

### List Forwarders
    
    
    $ secops forwarder list --page-size 100

### Get Forwarder
    
    
    $ secops forwarder get --id "1234567890"

### Update Forwarder
    
    
    $ secops forwarder update --id "1234567890" --display-name "updated-name"

### Delete Forwarder
    
    
    $ secops forwarder delete --id "1234567890"

## BigQuery data access workflows

Google Security Operations supports self-service access to Google Security Operations data (both SIEM and SOAR) in BigQuery. You can use the Google Security Operations CLI to grant [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles that give the following permissions for a user email:

  * `roles/bigquery.dataViewer`
  * `roles/bigquery.jobUser`
  * `roles/storage.objectViewer`



The email must be a Google Accounts and ID Administration (GAIA) user email address of a Google SecOps customer.

For more information about these roles, see [Exporting table data](https://docs.cloud.google.com/bigquery/docs/exporting-data).

**Note:** BigQuery workflows in the Google SecOps CLI are interactive. After entering a command, you may be prompted for additional input.

### Commands

#### `bigquery` command

The `bigquery` command takes the `provide_access` argument.

Usage syntax:
    
    
    $ chronicle_cli bigquery ARGUMENT [OPTIONS]

### Arguments

#### `provide_access` argument

Prompts you to enter a user email address. The email must be a Google Accounts and ID Administration (GAIA) user email address of a Google SecOps Security customer. The user will receive the required IAM roles to do the following:

  * Read data and metadata from BigQuery tables (`roles/bigquery.dataViewer`)
  * Run queries on BigQuery table data (`roles/bigquery.jobUser`)
  * Read data in Cloud Storage buckets(`roles/storage.objectViewer`)



##### Sample usage
    
    
    $ chronicle_cli bigquery provide_access
    $ Enter email: xyz@gmail.com
    

##### Success response
    
    
    Providing BigQuery access...
    Access provided to email: xyz@gmail.com
    
    
    
    Providing BigQuery access...
    Error while providing access:
    Response code: 400
    

### Options

#### Help (-h / --help)

Use `-`h or `--`help option to view the usage or description for any command or option.

### Troubleshooting

This section shows the output displayed on the console against different types of response codes received from API response.

#### `provide_access` argument response codes

**Response Code** | **Console Output**  
---|---  
400  | Email does not exist.   
Any other response code  | Error while fetching feed. Response Code: `{status code}` Error: `{error message}`  
  
## Log Ingestion

Ingest logs into Google SecOps:

### Ingest Raw Logs
    
    
    # From file
    $ secops log ingest --type "OKTA" --file "/path/to/okta_logs.json"
    
    # With labels
    $ secops log ingest --type "WINDOWS" --file "/path/to/logs.xml" \
        --labels "environment=production,team=security"
    
    # Inline message
    $ secops log ingest --type "WINDOWS" --message "{\"event\": \"data\"}"

### Ingest UDM Events
    
    
    $ secops log ingest-udm --file "/path/to/udm_event.json"

### List Log Types
    
    
    $ secops log types
    $ secops log types --search "windows"

### Generate UDM Mapping
    
    
    $ secops log generate-udm-mapping \
        --log-format "JSON" \
        --log '{"id":"123","user":"test_user","source_ip":"192.168.1.10"}'

## Rule Management

Manage detection rules:

### List Rules
    
    
    $ secops rule list --page-size 50

### Create Rule
    
    
    $ secops rule create --file "/path/to/rule.yaral"

### Update Rule
    
    
    $ secops rule update --id "ru_12345" --file "/path/to/updated_rule.yaral"

### Enable/Disable Rule
    
    
    $ secops rule enable --id "ru_12345" --enabled true
    $ secops rule enable --id "ru_12345" --enabled false

### Test Rule

Test a rule against historical data:
    
    
    # Test for last 24 hours
    $ secops rule test --file "/path/to/rule.yaral" --time-window 24
    
    # Test with specific time range
    $ secops rule test --file "/path/to/rule.yaral" \
        --start-time "2023-07-01T00:00:00Z" \
        --end-time "2023-07-02T00:00:00Z" \
        --max-results 1000

### Validate Rule
    
    
    $ secops rule validate --file "/path/to/rule.yaral"

### Delete Rule
    
    
    $ secops rule delete --id "ru_12345"

## Alert Management

Get and manage alerts:
    
    
    $ secops alert --time-window 24 --max-alerts 50
    $ secops alert --snapshot-query "feedback_summary.status != \"CLOSED\"" --time-window 24

## Case Management

Retrieve case details:
    
    
    $ secops case --ids "case-123,case-456"

## Data Tables

Data tables are structured data collections for use in detection rules:

### Create Data Table
    
    
    $ secops data-table create \
        --name "suspicious_ips" \
        --description "Known suspicious IP addresses" \
        --header '{"ip_address":"CIDR","description":"STRING","severity":"STRING"}'

### Add Rows
    
    
    $ secops data-table add-rows \
        --name "suspicious_ips" \
        --rows '[["192.168.1.100","Scanning activity","Medium"]]'

### List Rows
    
    
    $ secops data-table list-rows --name "suspicious_ips"

### Delete Data Table
    
    
    $ secops data-table delete --name "suspicious_ips"

## Reference Lists

Reference lists are simple value lists for detection rules:

### Create Reference List
    
    
    $ secops reference-list create \
        --name "admin_accounts" \
        --description "Administrative accounts" \
        --entries "admin,administrator,root,superuser"

### Update Reference List
    
    
    $ secops reference-list update \
        --name "admin_accounts" \
        --entries "admin,administrator,root,superuser,sysadmin"

### List Reference Lists
    
    
    $ secops reference-list list

## Data Export

Export data for analysis:

### Create Export
    
    
    # Export specific log type
    $ secops export create \
        --gcs-bucket "projects/my-project/buckets/my-bucket" \
        --log-type "WINDOWS" \
        --time-window 24
    
    # Export all logs
    $ secops export create \
        --gcs-bucket "projects/my-project/buckets/my-bucket" \
        --all-logs \
        --time-window 168

### Check Export Status
    
    
    $ secops export status --id "export-123"

### Cancel Export
    
    
    $ secops export cancel --id "export-123"

### List Available Log Types for Export
    
    
    $ secops export log-types --time-window 24

## Gemini AI Integration

Query Gemini AI for security insights:
    
    
    # Ask about security concepts
    $ secops gemini --query "What is Windows event ID 4625?"
    
    # Generate detection rules
    $ secops gemini --query "Write a rule to detect PowerShell downloading files"
    
    # Get vulnerability information
    $ secops gemini --query "Tell me about CVE-2021-44228"

Opt-in to Gemini:
    
    
    $ secops gemini --opt-in

## Dashboard Management

Manage native dashboards:

### Create Dashboard
    
    
    $ secops dashboard create \
        --display-name "Security Overview" \
        --description "Security monitoring dashboard" \
        --access-type PRIVATE

### List Dashboards
    
    
    $ secops dashboard list --page-size 10

### Update Dashboard
    
    
    $ secops dashboard update --id dashboard-id \
        --display-name "Updated Security Dashboard" \
        --description "Updated security monitoring dashboard"

### Export/Import Dashboard
    
    
    # Export
    $ secops dashboard export --dashboard-names 'projects/your-project-id/locations/us/instances/your-instance-id/nativeDashboard/xxxxxxx'
    
    # Import
    $ secops dashboard import --dashboard-data-file dashboard_data.json

### Add Chart to Dashboard
    
    
    $ secops dashboard add-chart --dashboard-id dashboard-id \
        --display-name "DNS Query Chart" \
        --description "Shows DNS query patterns" \
        --query-file dns_query.txt \
        --chart_layout '{"startX": 0, "spanX": 12, "startY": 0, "spanY": 8}'

### Delete Dashboard
    
    
    $ secops dashboard delete --id dashboard-id

## Advanced Examples

### Complete Parser Workflow

Retrieve, test, and deploy a parser:
    
    
    # List parsers
    $ secops parser list --log-type "OKTA" > okta_parsers.json
    
    # Get parser details
    PARSER_ID=$(cat okta_parsers.json | jq -r '.[0].name' | awk -F'/' '{print $NF}')
    $ secops parser get --log-type "OKTA" --id "$PARSER_ID" > parser_details.json
    
    # Extract parser code
    cat parser_details.json | jq -r '.cbn' | base64 -d > okta_parser.conf
    
    # Test parser
    $ secops parser run \
        --log-type "OKTA" \
        --parser-code-file "okta_parser.conf" \
        --logs-file "sample_logs.txt" > parser_result.json
    
    # Activate if successful
    $ secops parser activate --log-type "OKTA" --id "$PARSER_ID"

### Search and Export Workflow

Search for events and export results:
    
    
    # Search for failed logins
    $ secops search \
        --query "metadata.event_type = \"USER_LOGIN\" AND security_result.action = \"BLOCK\"" \
        --fields "metadata.event_timestamp,principal.user.userid,principal.ip" \
        --time-window 24 \
        --csv > failed_logins.csv
    
    # Get entity details for suspicious IPs
    cat failed_logins.csv | awk -F',' '{print $3}' | sort -u | while read ip; do
        secops entity --value "$ip" --time-window 72
    done

### Rule Testing and Deployment

Create, test, and deploy a detection rule:
    
    
    # Create rule file
    cat > suspicious_activity.yaral << 'EOF'
    rule suspicious_powershell {
        meta:
            description = "Detects suspicious PowerShell activity"
            severity = "Medium"
        events:
            $e.metadata.event_type = "PROCESS_LAUNCH"
            $e.principal.process.file.full_path = /powershell\.exe/i nocase
            $e.principal.process.command_line = /download|invoke-expression|hidden/i nocase
        condition:
            $e
    }
    EOF
    
    # Validate rule
    $ secops rule validate --file suspicious_activity.yaral
    
    # Test against historical data
    $ secops rule test --file suspicious_activity.yaral --time-window 168
    
    # Create and enable if tests pass
    $ secops rule create --file suspicious_activity.yaral
    $ secops rule enable --id "ru_generated_id" --enabled true

## Troubleshooting

### Common Issues

#### Authentication Errors

If you encounter authentication errors:

  1. Verify your credentials are valid
  2. Check that your service account has the necessary permissions
  3. Ensure ADC is configured correctly: `gcloud auth application-default login`



#### Region Errors

If you get region-related errors:

  1. Verify the region is supported
  2. Check that your instance is in the specified region
  3. Use `--region` flag or set it in configuration



#### Rate Limiting

For rate limiting issues:

  1. Reduce the frequency of API calls
  2. Use pagination for large result sets
  3. Implement exponential backoff for retries



### Getting Help

View help for any command:
    
    
    $ secops --help
    $ secops search --help
    $ secops rule create --help

## Migration from chronicle_cli

If you're migrating from the legacy `chronicle_cli`, here's a mapping of common commands:

chronicle_cli | secops  
---|---  
`chronicle_cli feeds create` | `secops feed create`  
`chronicle_cli feeds list` | `secops feed list`  
`chronicle_cli feeds update` | `secops feed update`  
`chronicle_cli feeds delete` | `secops feed delete`  
`chronicle_cli parsers list` | `secops parser list`  
`chronicle_cli parsers create` | `secops parser create`  
`chronicle_cli parsers activate` | `secops parser activate`  
`chronicle_cli forwarders create` | `secops forwarder create`  
`chronicle_cli forwarders list` | `secops forwarder list`  
  
The new `secops` CLI offers many additional features not available in `chronicle_cli`, including:

  * Natural language search
  * Gemini AI integration
  * Dashboard management
  * Rule testing and validation
  * Data tables and reference lists
  * Case management
  * And much more



## Additional Resources

  * [SecOps SDK GitHub Repository](https://github.com/google/secops-wrapper)
  * [UDM Field Reference](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list)
  * [YARA-L 2.0 Language Reference](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
