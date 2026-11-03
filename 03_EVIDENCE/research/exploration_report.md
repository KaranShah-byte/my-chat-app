# Opportunity Exploration Report
**Date:** November 2026

## 1. Problem Space & Alternatives
The objective was to identify a high-impact software engineering project bridging theoretical computer science (data structures, system design, network protocols) with real-world cloud deployment. 

Three directions were evaluated:
*   **MPLAD Scheme Implementation Platform:** Track/manage funds and projects under the Members of Parliament Local Area Development Scheme. 
    *   *Verdict:* Rejected. Heavily reliant on static CRUD operations and external datasets; limits exposure to real-time concurrency.
*   **Educational App for Paleontologists:** A dinosaur dataset curation tool and platform for a Nebius hackathon.
    *   *Verdict:* Rejected for the primary system-design capstone. Heavy emphasis on data curation rather than backend architecture and network management.
*   **Cloud Chat Web Application:** A real-time, multi-room chat application using WebSockets and mobile authentication.
    *   *Verdict:* **Selected.** Directly exercises core system design concepts: managing volatile state, handling real-time bidirectional communication, bypassing mixed-content security blocks, and integrating third-party telecom APIs.

## 2. Selected Project Thesis
**Project:** Cloud Chat Web Application
**Target:** Users requiring secure, partitioned, and instant group communication without native app installation.
**Strategic Value:** Applying hash map concepts from data structures practice to production memory management. Bypasses static request-response cycles to tackle continuous asynchronous connections and cloud infrastructure constraints (Render PaaS).
