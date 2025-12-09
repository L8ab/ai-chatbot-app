# Security Policy

## Supported Versions

We actively support security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, please follow these steps:

1. **Do NOT** open a public issue
2. Email security details to: L8ab@proton.me
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

## Security Best Practices

### For Users
- Keep dependencies updated
- Use environment variables for secrets
- Enable HTTPS in production
- Regularly rotate API keys and tokens
- Use strong passwords
- Enable 2FA where available

### For Developers
- Never commit secrets to version control
- Use `.env` files for local development
- Review dependencies for vulnerabilities
- Follow secure coding practices
- Implement proper input validation
- Use parameterized queries
- Enable rate limiting
- Implement proper error handling

## Known Vulnerabilities

None at this time.

## Security Updates

Security updates are released as soon as possible after discovery and verification.

---

**POWERED BY L8AB** ⚡

