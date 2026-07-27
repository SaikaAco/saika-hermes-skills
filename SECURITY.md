# Security Policy

Hermes skills are executable instructions for an AI agent even when they contain no conventional binary code. Treat every skill as third-party automation policy: read it before installation and verify its requested tools, side effects, paths, and authority boundaries.

## Reporting a vulnerability

Use GitHub's private security-advisory flow for vulnerabilities that could expose secrets, bypass approval, create unsafe side effects, or enable prompt injection. Do not place credentials, private paths, tokens, or exploit details containing live secrets in a public issue.

Ordinary documentation defects and non-sensitive behavior bugs may be reported through GitHub Issues.

## Repository guarantees

Every published candidate is checked for:

- required `SKILL.md` frontmatter;
- directory/name agreement;
- symlinks;
- personal absolute paths and handles;
- common secret/token/private-key formats;
- balanced Markdown code fences.

These checks reduce risk but do not replace human review or Hermes' own community-skill security scan.
