# **Grafana Loki and Promtail**

## **1. Grafana Loki**
Grafana Loki is a log aggregation system optimized for simplicity, scalability, and efficiency. It focuses on storing and indexing log metadata rather than the full-text logs.   

## Using LOKI   
In order to get logs for the server , will need to install the agent on the client(promtail)

### **Key Features**
- **No Full-Text Indexing:** Stores logs as compressed chunks, indexing only metadata to reduce resource usage.
- **Prometheus-Like Labels:** Organizes logs using labels, similar to Prometheus metrics.
- **Scalable Architecture:** Horizontally scalable with minimal overhead.
- **Cost-Effective Storage:** Logs are stored in cloud-native storage solutions (e.g., S3, GCS).

### **Use Cases**
- Centralized log management for cloud-native apps.
- Correlating logs with metrics for better troubleshooting.
- Cost-efficient logging for DevOps and SRE teams.

---

## **2. Promtail**
Promtail is a log-collecting agent that forwards logs to Loki. It integrates closely with Kubernetes and other environments.

### **Key Features**
- **Log Collection:** Reads logs from local files, system logs, or application logs.
- **Label Assignment:** Tags logs with metadata (e.g., Kubernetes labels, host details).
- **Kubernetes Integration:** Auto-discovers Kubernetes logs using annotations.
- **Pipeline Stages:** Supports log filtering, parsing, and field extraction.

### **Use Cases**
- Collecting and forwarding logs to Loki.
- Adding structured metadata to logs.
- Simplifying Kubernetes logging pipelines.

---

## **How Loki and Promtail Work Together**
1. **Log Collection by Promtail:** Promtail collects logs from sources like files or Kubernetes containers.
2. **Logs Sent to Loki:** Logs, labeled with metadata, are sent to Loki for storage.
3. **Visualization in Grafana:** Logs are queried and visualized in Grafana, enabling correlation with Prometheus metrics.

---

## **Advantages**
- **Ease of Use:** Simple integration with Grafana and Kubernetes.
- **Cost Efficiency:** Lightweight and low resource requirements.
- **Metrics-Logs Correlation:** Ideal for troubleshooting in cloud-native environments.

---

## **When to Use Loki and Promtail**
- For teams using Grafana and Prometheus.
- When scalability and cost efficiency are crucial.
- In Kubernetes or cloud-native environments.   

# DEMO   

## Installing Loki   
1. Locally   
- Download and install both Loki and Alloy.   
- Download config files for both programs.   
- Start Loki.   
- Update the Alloy config file to get your logs into Loki. 
  
- Start The Server.     
### Manual Install   
1. Browse to the [release page](https://github.com/grafana/loki/releases/).

2. Find the Assets section for the version that you want to install.

3. Download the Loki and Promtail archive files that correspond to your system.

4. Don’t download LogCLI or Loki Canary at this time. LogCLI allows you to run Loki queries in a command line interface. Loki Canary is a tool to audit Loki performance.

5. Extract the package contents into the same directory. This is where the two programs will run.

6. In the command line, change directory (cd on most systems) to the directory with Loki and Promtail.

7. Copy and paste the following commands into your command line to download generic configuration files.
~~~
wget https://raw.githubusercontent.com/grafana/loki/main/cmd/loki/loki-local-config.yaml
wget https://raw.githubusercontent.com/grafana/loki/main/clients/cmd/promtail/promtail-local-config.yaml
~~~   
### Starting the Server   
~~~
./loki-linux-amd64 -config.file=loki-local-config.yaml
~~~   
## Installing the Agent   
Every Grafana Loki release includes binaries for Promtail which can be found on the [Releases page](https://github.com/grafana/loki/releases) as part of the release assets.     

## View the Logs   
***NB*** Need to have Grafana installed first   
start the grafana server   
~~~
 sudo systemctl status grafana-server 
~~~