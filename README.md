# Event Sourcing Examples

This repository contains Python code examples demonstrating various aspects of Event Sourcing, a design pattern for persisting data changes as a sequence of events.

The goal is to demonstrate usage of different approaches using python only. In the most basic way possible. To remove any dependencies and focus on the core concepts.

## Table of Contents:

- [Key Concepts](#key-concepts)
- [Examples Included](#examples-included)
- [Getting Started](#getting-started)


## Key Concepts:

- **Events**: Atomic units of change that represent something happening in your system.
- **Event Store**: A specialized database for storing and retrieving events.
- **Materialized Views**: Projections of the current state derived from replaying events.

## Examples Included:

- **Basic Event Store**: A simple implementation using a `defaultdict` for in-memory storage.
- **Command and Event Handling**: Demonstrates how to create commands, process them, and persisting events.
- **Projection**: Projection of an event into a table.
- **CQRS**: Example of Command Query Responsibility Segregation with a separate read model.
- **Querying Event Streams and Projections:** Examples of querying events directly and using materialized views.
- **Test:** All examples come with a test

### Examples in progress:

- **Aggregate**: Demonstrates how to group related events into an aggregate.
- **Workflows**: Applying ES to run multi step operations.
- **Snapshotting**: How to use snapshots
- **Data pruning**: pruning old events to manage storage costs.
- **Data erase**: Encrytion shredding

## Getting Started:

Refer to the `tests` folder for example usage.

Example use of commands:
- `app/tests/test_create_post_command.py` - shows a basic use of a command with an event being persisted.
- `app/tests/test_publish_post_command.py` - shows a command that has validation in place. Validation checks if command can be executed.

Example use of projections:
- `app/tests/test_project_posts.py` - show an example of how we can listen to events. Projection is just one example of a side effect.

### Docker setup

1. `docker-compose build`
1. `docker-compose up -d`
1. `docker exec -it python-es-python-app-1 bash`


### Running tests

1. After accessing docker, run `pytest`