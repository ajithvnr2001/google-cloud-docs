---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-reads-print/
title: Read and print \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:59.552976+00:00
---

# Read and print  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-reads-print/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read and print Stay organized with collections  Save and categorize content based on your preferences. 

Read and print a row.

## Code sample

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Bigtable.Common.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.html);
    using [Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.html);
    using System;
    using System.Linq;
    using System.Threading.Tasks;
    
    
    
    namespace Reads
    {
        public class ReadSnippets
        {
            // Write your code here.
            // ...
            public string PrintRow([Row](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html) row)
            {
                string result = $"Reading data for {row.[Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Key).ToStringUtf8()}\n";
                foreach ([Family](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Family.html) family in row.[Families](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Families))
                {
                    result += $"Column Family {family.Name}\n";
    
                    foreach ([Column](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Column.html) column in family.Columns)
                    {
                        foreach ([Cell](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Cell.html) cell in column.[Cells](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Column.html#Google_Cloud_Bigtable_V2_Column_Cells))
                        {
                            result += $"\t{column.Qualifier.ToStringUtf8()}: {cell.[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Value.html).ToStringUtf8()} @{cell.TimestampMicros} {cell.Labels}\n";
                        }
                    }
                }
                result += "\n";
                Console.WriteLine(result);
                return result;
            }
        }
    }

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func printRow(w io.Writer, row bigtable.Row) {
    	fmt.Fprintf(w, "Reading data for %s:\n", row.Key())
    	for columnFamily, cols := range row {
    		fmt.Fprintf(w, "Column Family %s\n", columnFamily)
    		for _, col := range cols {
    			qualifier := col.Column[strings.IndexByte(col.Column, ':')+1:]
    			fmt.Fprintf(w, "\t%s: %s @%d\n", qualifier, col.Value, col.Timestamp)
    		}
    	}
    	fmt.Fprintln(w)
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static com.google.cloud.bigtable.data.v2.models.[Filters](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.html).FILTERS;
    
    import com.google.api.gax.rpc.[ServerStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStream.html);
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.models.[Filters](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.html);
    import com.google.cloud.bigtable.data.v2.models.[Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html);
    import com.google.cloud.bigtable.data.v2.models.[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html);
    import com.google.cloud.bigtable.data.v2.models.[RowCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowCell.html);
    import com.google.cloud.bigtable.data.v2.models.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html);
    import java.io.IOException;
    
    public class Reads {
    
      // Write your code here.
      // ...
    
      private static void printRow([Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) row) {
        System.out.printf("Reading data for %s%n", row.[getKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getKey__)().toStringUtf8());
        String colFamily = "";
        for ([RowCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowCell.html) cell : row.[getCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getCells__)()) {
          if (!cell.getFamily().equals(colFamily)) {
            colFamily = cell.getFamily();
            System.out.printf("Column Family %s%n", colFamily);
          }
          System.out.printf(
              "\t%s: %s @%s%n",
              cell.getQualifier().toStringUtf8(), cell.getValue().toStringUtf8(), cell.getTimestamp());
        }
        System.out.println();
      }
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Helper function for printing the row data
    function print_row(string $key, array $row): void
    {
        printf('Reading data for row %s' . PHP_EOL, $key);
        foreach ((array) $row as $family => $cols) {
            printf('Column Family %s' . PHP_EOL, $family);
            foreach ($cols as $col => $data) {
                for ($i = 0; $i < count($data); $i++) {
                    printf(
                        "\t%s: %s @%s%s" . PHP_EOL,
                        $col,
                        $data[$i]['value'],
                        $data[$i]['timeStamp'],
                        $data[$i]['labels'] ? sprintf(' [%s]', $data[$i]['labels']) : ''
                    );
                }
            }
        }
        print(PHP_EOL);
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def print_row(row):
        print("Reading data for {}:".format(row.row_key.decode("utf-8")))
        for cf, cols in sorted(row.cells.items()):
            print("Column Family {}".format(cf))
            for col, cells in sorted(cols.items()):
                for cell in cells:
                    labels = (
                        " [{}]".format(",".join(cell.labels)) if len(cell.labels) else ""
                    )
                    print(
                        "\t{}: {} @{}{}".format(
                            col.decode("utf-8"),
                            cell.value.decode("utf-8"),
                            cell.timestamp,
                            labels,
                        )
                    )
        print("")
    
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Import google bigtable client lib
    require "google/cloud/bigtable"
    # Write your code here.
    # ...
    def print_row row
      puts "Reading data for #{row.key}:"
    
      row.cells.each do |column_family, data|
        puts "Column Family #{column_family}"
        data.each do |cell|
          labels = !cell.labels.empty? ? " [#{cell.labels.join ','}]" : ""
          puts "\t#{cell.qualifier}: #{cell.value} @#{cell.timestamp}#{labels}"
        end
      end
      puts "\n"
    end
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
