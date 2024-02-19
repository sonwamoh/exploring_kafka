**README: Setting Up Kafka for Your Personal Project on WIndows OS**

### Installation Steps

1. **Java JDK Installation:**
   - Ensure you have Java JDK version 8 or higher installed on your system.
   - You can download it from the official Oracle website or use a package manager if available.

2. **Download and Extract Kafka:**
   - Head over to the [Kafka downloads page](https://kafka.apache.org/downloads).
   - Download the Kafka binary (`kafka_2.13-3.6.1.tgz`) suitable for Windows.
   - Extract the downloaded file to a directory of your choice on your local machine.

3. **Configure Zookeeper:**
   - Navigate to the `config` folder inside the extracted Kafka files.
   - Open the `zookeeper.properties` file in a text editor.
   - Locate the `dataDir` property and append `/zookeeper-data` to the path.
   - Save the changes made to the `zookeeper.properties` file.

4. **Start Zookeeper:**
   - Open a new command prompt or terminal window.
   - Navigate to the Kafka directory where you extracted the files.
   - Execute the following command to start Zookeeper:
     ```
     .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
     ```

5. **Start Kafka Server:**
   - Open another command prompt or terminal window.
   - Navigate to the Kafka directory.
   - Execute the following command to start Kafka:
     ```
     .\bin\windows\kafka-server-start.bat .\config\server.properties
     ```

### Common Operations

- **Creating a Topic:**
  ```
  .\bin\windows\kafka-topics.bat --create --topic <topic_name> --bootstrap-server localhost:9092 --replication-factor 1 --partitions <num_partitions>
  ```

- **Launching a Producer:**
  ```
  .\bin\windows\kafka-console-producer.bat --topic <topic_name> --bootstrap-server localhost:9092
  ```

- **Sending Events to Specific Partition:**
  ```
  .\bin\windows\kafka-console-producer.bat --topic <topic_name> --bootstrap-server localhost:9092 --property "parse.key=true" --property "key.separator=," --property "partition=<partition_number>"
  ```

- **Launching a Consumer:**
  ```
  .\bin\windows\kafka-console-consumer.bat --topic <topic_name> --from-beginning --bootstrap-server localhost:9092
  ```

- **Consuming Events from Specific Partition and Offset:**
  ```
  .\bin\windows\kafka-console-consumer.bat --topic <topic_name> --from-beginning --bootstrap-server localhost:9092 --partition <partition_number> --offset <offset_number>
  ```

### Testing Your Kafka Stream

- When testing Kafka streams, ensure to run the consumer and producer files (`.py`) on separate terminals.
- Always run the producer file before the consumer file.

