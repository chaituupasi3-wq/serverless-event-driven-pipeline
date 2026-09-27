# ⚡ Serverless Event-Driven Pipeline (AWS Lambda & SQS)

An asynchronous, event-driven microservices architecture built on AWS using Lambda functions and Simple Queue Service (SQS) for decoupled, scalable data processing.

## 🏗️ Architecture Flow
1. **Producer Function:** Generates event payloads and securely pushes them to an Amazon SQS queue.
2. **Queueing Layer:** SQS buffers events reliably, preventing data loss during traffic surges.
3. **Consumer Function:** Automatically triggers upon receiving batches from SQS, processing items asynchronously.

## 🛠️ Tech Stack
* **Cloud Services:** AWS Lambda, Amazon SQS, AWS IAM
* **Language:** Python, Boto3

## 📦 Usage & Deployment

### 1. Clone the Repository
```bash
git clone [https://github.com/chaituupasi3-wq/serverless-event-driven-pipeline.git](https://github.com/chaituupasi3-wq/serverless-event-driven-pipeline.git)
cd serverless-event-driven-pipeline
