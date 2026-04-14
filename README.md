Project Title:
Impact of Backup Configuration on the Forensic Recoverability and Accessibility of WhatsApp Disappearing Message Artifacts on Android Devices

Author:
Rehasun Tanjin Rony
The University of Winnipeg
Winnipeg, MB, Canada

Course:
Theory and Practice of Security and Privacy


1. PROJECT OVERVIEW

This project investigates the forensic recoverability of WhatsApp disappearing messages on Android devices. The study focuses on how different backup configurations and user actions affect the availability and persistence of forensic artifacts.

The main objective is to evaluate whether evidence related to disappearing messages can still be recovered under realistic conditions, even when messages are deleted automatically or manually.


2. EXPERIMENTAL SETUP

All experiments were conducted in a controlled environment:

- Device: Android Emulator (Pixel 4)
- Android Version: Android 11 (API 30)
- WhatsApp Version: 2.26.12.72

Tools used:

- Android Studio (Panda 3) → Emulator setup
- ADB (Platform Tools) → Data extraction
- Python 3.11.6 → Data processing
- DB Browser for SQLite → Database inspection
- ALEAPP → Artifact parsing and log analysis
- WhatsApp Key/DB Extractor (v4.7) → Attempted key extraction


3. DATA ACQUISITION METHOD

A logical acquisition approach was used. Artifacts were extracted from:

/sdcard/Android/media/com.whatsapp/WhatsApp/

Collected data includes:

- Encrypted database files (.crypt14)
- Media files (images)
- Notification logs

ADB commands were used to pull data and capture system logs.


4. EXPERIMENTAL SCENARIOS

Six scenarios were designed to evaluate forensic behavior:

Scenario A:
Backup disabled

Scenario B:
Backup enabled but not executed

Scenario C:
Backup performed before message deletion

Scenario D:
Backup performed after message deletion

Scenario E:
Backup followed by device reset and restore

Scenario F:
Anti-forensic case (manual deletion of chat and media)


5. KEY FINDINGS

- Database files (.crypt14) appear only after backup execution
- Database persists across deletion, restore, and anti-forensic scenarios
- Backup timing directly affects database state
- Hash analysis shows identical database states across some scenarios (D, E, F)
- Media files persist after deletion but are removed after device reset
- Media can be removed through anti-forensic actions
- Notification logs may contain traces of message activity


6. IMPORTANT FORENSIC LIMITATION

The WhatsApp database could not be decrypted.

Reason:
- No root access
- Android security restrictions
- Key extraction not possible

This is NOT a failure.

It reflects a real-world forensic limitation, where encrypted data may be present but inaccessible.


7. FORENSIC SIGNIFICANCE

This project demonstrates that:

- Evidence can still exist even when messages disappear
- Backup configuration is a critical forensic factor
- Artifact-level analysis is essential when decryption is not possible
- Multiple evidence sources (database, media, logs) must be correlated

The findings are useful for real-world digital investigations involving encrypted messaging applications.


11. PROJECT FILE STRUCTURE

The project directory is organized as follows:


/evidence_A
/evidence_B
/evidence_C
/evidence_D
/evidence_E
/evidence_F

These folders contain extracted forensic artifacts for each experimental scenario (A–F). Each folder includes:

- WhatsApp database files (.crypt14)
- Media files (images)
- Scenario-specific extracted data


/Screenshots of the Experiments

This folder contains all screenshots used in the report, including:

- ADB extraction outputs
- Database presence/absence verification
- Media persistence observations
- WhatsApp interface screenshots


/wa-crypt-tools-main

Tool directory used for WhatsApp cryptographic analysis and experimentation.


/WhatsApp-Key-DB-Extractor-master

Contains the WhatsApp Key/DB extraction tool used during the experiment.

Outcome:
- Tool execution failed due to modern Android restrictions


Hash Files

- Hash for all scenarios (Text file)
- hash_scenario_C.py
- hash_scenario_D.py
- hash_scenario_F.py

These files were used to compute and compare hash values of database files across scenarios to analyze data consistency and persistence.


Notification Analysis

- notification_results (Excel file)
- Notifications (Jupyter Notebook)

These files contain processed notification log data and scripts used for extracting forensic traces from system logs.


Other Files

- .git → Version control (not part of analysis)
- .ipynb_checkpoints → Auto-generated (not relevant to forensic analysis)



END OF SECTION


9. LIMITATIONS

- No root access (limits deep acquisition)
- Database content cannot be decrypted
- Emulator-based environment (not physical device)


10. FUTURE WORK

- Use rooted devices for full database decryption
- Analyze physical devices instead of emulator
- Extend analysis to other messaging apps
- Investigate cloud backup artifacts


