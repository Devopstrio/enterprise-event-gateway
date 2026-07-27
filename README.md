<div align="center">

<img src="https://raw.githubusercontent.com/Devopstrio/.github/main/assets/Browser_logo.png" height="90" alt="Devopstrio Logo" />

# Enterprise Event Gateway

### CNCF CloudEvents 1.0 High-Throughput Event Ingestion, Content-Based Routing & DLQ Replay Engine

[![CloudEvents 1.0](https://img.shields.io/badge/Spec-CNCF_CloudEvents_1.0-blue?style=flat-square)](https://cloudevents.io)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=flat-square)](https://devopstrio.co.uk)

</div>

---

## 🎯 Architecture Overview & Problem Statement

Event-driven architectures across multi-cloud infrastructure frequently suffer from fragmented event payloads, unvalidated schemas, and lost events during downstream sink outages.

The **Enterprise Event Gateway** standardizes all cross-domain event telemetry using the **CNCF CloudEvents 1.0 Specification**. It provides content-based routing rules, automated schema validation, Prometheus operational metrics, and deterministic Dead Letter Queue (DLQ) event replay mechanisms.

![Event Gateway Flowchart](docs/images/architecture_diagram.jpg)

---

## 🔄 Execution Pipeline

```mermaid
flowchart TD
    Ingress[Inbound Event Producers / Webhooks] --> Validate[CloudEvents 1.0 Envelope Validator]
    Validate --> Router{Content-Based Router Matrix}
    
    Router -->|Payment Events| Kafka[Kafka Payments Topic]
    Router -->|User Events| SQS[AWS SQS Queue]
    Router -->|Audit Logs| S3[AWS S3 Bucket]
    Router -->|Unmatched / Invalid| DLQ[Dead Letter Queue & Replay Buffer]
```

---

## 💻 CLI Quickstart (`eegctl`)

Manage events, inspect schemas, and replay dead-lettered payloads directly using the built-in `eegctl` tool:

```bash
# Validate CloudEvent v1.0 Envelope
python -m cmd.eegctl.main validate

# Execute Content-Based Routing Evaluation
python -m cmd.eegctl.main route

# Replay Dead Letter Queue (DLQ) Items
python -m cmd.eegctl.main replay
```

---

## 📦 Deployment via Helm

```bash
# Deploy to Kubernetes Cluster via Helm
helm upgrade --install enterprise-event-gateway deploy/helm/enterprise-event-gateway \
  --namespace event-mesh \
  --create-namespace
```

---

## 🧪 Testing Suite

```bash
# Execute Pytest Unit & Integration Tests
pytest -v tests/
```

<div align="center">

<sub>&copy; 2026 Devopstrio &mdash; Engineering Uninterrupted Global Workforce Productivity.</sub>

</div>
