## Review: Security Validations checklist
**The following items must be checked before merging to the Master branch**
**For any exceptions contact the Security Team**

- [ ] **Secrets are not hardcoded or stored in the code** (e.g. Passwords, AWS access keys, tokens, connection strings, SSH Keys, PGP Keys, etc)
- [ ] **All API endpoints verify the identity of the user and don't allow cross-user access**
- [ ] **All input parameters are validated and/or sanitized** (including form fields, query strings, cookies, and HTTP headers).
- [ ] **API response data is sanitized**, returned based on access control and only what is needed.
- [ ] **Sensitive information is not being transmitted in an unencrypted or unsecured manner (api, files)**
- [ ] **Sensitive data is not passed in query strings or URL.** URL data is sanitized, validated and use with care.
- [ ] **All relevant user / system actions are properly logged**. Errors, failures and issues (e.g. missing data, bad data) are logged.
- [ ] **New libraries and packages have been reviewed and approved by the security team**
- [ ] **New HTTP headers have been reviewed and approved by the security team**
- [ ] **Any changes to the structure or content type of cookies have been reviewed and approved by the security team**
- [ ] **iFrames, redirects, domain or subdomain usage were reviewed and approved by the security team**
- [ ] **Access to system level resources is restricted. There is no shell execution.**


## NOTE: examples and guidelines please see

[FrontEnd Guidelines](https://github.com/bluevine-dev/bv_security/wiki/Security-Validations-Checklist-FrontEnd-Guidelines)

[BackEnd Guidelines](https://github.com/bluevine-dev/bv_security/wiki/Security-Validations-Checklist-BackEnd-Guidelines)
