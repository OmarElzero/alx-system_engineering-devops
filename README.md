# ALX System Engineering & DevOps

This repository contains coursework and hands-on exercises from the ALX Software Engineering program's System Engineering & DevOps track. It covers the foundations of Linux system administration, shell scripting, networking, web infrastructure design, configuration management, SSH, firewalls, database administration, monitoring, and consuming REST APIs — organized as a series of numbered project directories, each with its own README describing the exercise objectives.

![Last Commit](https://img.shields.io/github/last-commit/OmarElzero/alx-system_engineering-devops)
![Top Language](https://img.shields.io/github/languages/top/OmarElzero/alx-system_engineering-devops)
![Repo Size](https://img.shields.io/github/repo-size/OmarElzero/alx-system_engineering-devops)

## Features

- Shell scripting fundamentals: navigation, permissions, redirections, variables and expansions
- Regular expressions in Ruby for text parsing
- Networking basics: OSI model, TCP/UDP, MAC/IP addressing, port scanning
- Web infrastructure design diagrams (simple stack through distributed, secured, and scaled architectures)
- Configuration management with Puppet manifests (`.pp` files) for package installation, file creation, and command execution
- SSH key generation and configuration
- Web stack debugging exercises (Nginx, process ownership, port binding)
- Firewall configuration (UFW rules, port forwarding)
- MySQL primary/replica configuration and backup scripting
- Python scripts that consume REST APIs (JSONPlaceholder, GitHub, Reddit) to fetch, filter, and export data as CSV/JSON
- Web stack monitoring setup with Datadog

## Tech Stack

- **Shell (Bash)** — the majority of the exercises
- **Python 3** — API consumption scripts (`requests` library)
- **Ruby** — regular expression exercises
- **Puppet** — configuration management manifests
- Supporting tools: Nginx, MySQL, UFW, Datadog agent

## Project Structure

| Path | Description |
|---|---|
| `0x00-shell_basics/` | Basic navigation and file manipulation shell scripts |
| `0x01-shell_permissions/` | File permission and ownership exercises |
| `0x02-shell_redirections/` | I/O redirection and stream manipulation |
| `0x03-shell_variables_expansions/` | Shell variables, arithmetic, and expansions |
| `0x06-regular_expressions/` | Ruby regex scripts |
| `0x07-networking_basics/` & `0x08-networking_basics_2/` | Networking fundamentals and IP configuration |
| `0x09-web_infrastructure_design/` | Architecture diagrams for web stacks of increasing complexity |
| `0x0A-configuration_management/` | Puppet manifests for automated provisioning |
| `0x0B-ssh/` | SSH key pairs and client configuration |
| `0x0D`, `0x0E`, `0x12`, `0x17`, `0x1B-web_stack_debugging_*/` | Progressive Nginx/web stack debugging challenges |
| `0x13-firewall/` | UFW firewall rule exercises |
| `0x14-mysql/` | MySQL replication and backup scripts |
| `0x15-api/` | Python scripts consuming a REST API and exporting results |
| `0x16-api_advanced/` | Python scripts using the Reddit API (subreddit subscribers, hot posts, recursion) |
| `0x18-webstack_monitoring/` | Datadog agent setup for server monitoring |
| `0x1A-application_server/` | Nginx reverse proxy / application server configuration |

## Installation

Most exercises are standalone scripts with no build step.

```bash
git clone https://github.com/OmarElzero/alx-system_engineering-devops.git
cd alx-system_engineering-devops
# For Python scripts:
pip install requests
```

## Usage

Shell scripts and Puppet manifests can be run directly:

```bash
chmod +x 0x00-shell_basics/0-current_working_directory
./0x00-shell_basics/0-current_working_directory

sudo puppet apply 0x0A-configuration_management/1-install_a_package.pp
```

Python API scripts take command-line arguments, for example:

```bash
./0x15-api/0-gather_data_from_an_API.py <employee_id>
```

## Demo

No live demo is available for this project.

---

**Author:** OmarElzero · [GitHub](https://github.com/OmarElzero)
Last updated: 2026-08-23
