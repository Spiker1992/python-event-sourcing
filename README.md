# Event Sourcing Examples

This repository contains Python code examples demonstrating various aspects of Event Sourcing, a design pattern for persisting data changes as a sequence of events.

## Key Concepts:

- **Events**: Atomic units of change that represent something happening in your system.
- **Event Store**: A specialized database for storing and retrieving events.
- **Materialized Views**: Projections of the current state derived from replaying events.

## Examples Included:

- **Basic Event Store**: A simple implementation using a `defaultdict` for in-memory storage.
- **Command and Event Handling**: Demonstrates how to create commands, process them, and persisting events.

## Getting Started:

Refer to the `tests` folder for example usage.

### Docker setup

1. `docker-compose build`
1. `docker-compose up -d`
1. `docker exec -it python-es-python-app-1 bash`


### Running tests

1. After accessing docker, run `pytest`