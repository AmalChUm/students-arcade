<!-- 
Instructions for Contributors: 
Please ensure all items are completed and checked off before submitting your pull request. 
-->

## Pull-Request Checklist

### 1. Contribution Basics
- [ ] Worked in a dedicated feature branch using the recommended format.
- [ ] Changes are tightly focused on this specific issue.
- [ ] Preserved the MIT license and existing attribution.

### 2. Plugin Structure & Requirements
- [ ] **File Location:** Placed the plugin file inside the `plugins/` directory.
- [ ] **Filename:** Verified the filename is unique.
- [ ] **Metadata:** Explicitly defined `AUTHOR` and `APP_NAME` variables.
- [ ] **Execution Logic:** Defined the `run()` function to return or print a readable result.
- [ ] **Standard Library:** Used only the Python standard library (unless otherwise approved).
- [ ] **Import Guard:** Avoided running unintended code when the module is imported.

### 3. Verification & Security
- [ ] **Execution Check:** Verified the result by running `python main.py` (avoided modifying `main.py` unless explicitly required).
- [ ] **No-Credentials Check:** Confirmed that no credentials, tokens, private information, or unnecessary dependencies are included.

### 4. Pull-Request Description
- [ ] Linked this issue (#31) in the pull-request description.
- [ ] Provided a clear explanation of the verification steps performed.

