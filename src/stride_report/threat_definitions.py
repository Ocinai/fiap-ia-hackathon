"""
Threat definitions for different component types based on STRIDE.
"""

THREAT_DEFINITIONS = {
    "default": {
        "Spoofing": [
            "An attacker may impersonate a valid user.",
            "An attacker may impersonate a valid component."
        ],
        "Tampering": [
            "An attacker may alter data in transit.",
            "An attacker may alter data at rest."
        ],
        "Repudiation": [
            "A user may deny performing an action.",
            "A component may deny sending a message."
        ],
        "Information Disclosure": [
            "An attacker may gain access to sensitive data.",
            "An attacker may be able to intercept data in transit."
        ],
        "Denial of Service": [
            "An attacker may flood the component with requests, making it unavailable.",
            "An attacker may exploit a vulnerability to crash the component."
        ],
        "Elevation of Privilege": [
            "An attacker may gain administrative privileges.",
            "An attacker may be able to perform actions that they are not authorized to do."
        ]
    },
    "Database": {
        "Spoofing": [
            "An attacker may impersonate a valid application to gain access to the database."
        ],
        "Tampering": [
            "An attacker may alter data in the database.",
            "An attacker may delete data from the database."
        ],
        "Repudiation": [
            "A user may deny making changes to the database."
        ],
        "Information Disclosure": [
            "An attacker may gain access to sensitive data in the database.",
            "An attacker may be able to read the entire database."
        ],
        "Denial of Service": [
            "An attacker may flood the database with requests, making it unavailable.",
            "An attacker may exploit a vulnerability to crash the database."
        ],
        "Elevation of Privilege": [
            "An attacker may gain administrative privileges on the database."
        ]
    },
    "web-server": {
        "Spoofing": [
            "An attacker may impersonate a valid user.",
            "An attacker may impersonate a valid server in the cluster."
        ],
        "Tampering": [
            "An attacker may alter data in transit.",
            "An attacker may alter the content of the web server."
        ],
        "Repudiation": [
            "A user may deny performing an action."
        ],
        "Information Disclosure": [
            "An attacker may gain access to sensitive data on the web server.",
            "An attacker may be able to read the source code of the web application."
        ],
        "Denial of Service": [
            "An attacker may flood the web server with requests, making it unavailable.",
            "An attacker may exploit a vulnerability to crash the web server."
        ],
        "Elevation of Privilege": [
            "An attacker may gain administrative privileges on the web server."
        ]
    }
}
